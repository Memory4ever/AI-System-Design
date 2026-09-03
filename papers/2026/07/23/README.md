# Daily Research — 2026-07-23

**Research Date:** 2026-07-23

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-07-22 09:00:00 ～ 2026-07-23 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；Historical Daily 独立重建，不使用 Weekly 作为 discovery、评分或 Review 来源

**Status:** In Progress；Coverage=Open、Evidence=Open、Books=Open；author-side evidence 已闭合，等待独立 Semantic Audit 与 root Books 比较

## Executive Summary

官方 owner inventory 共 **444** 个 identity；全量 title + abstract 筛选后冻结 **117** 个候选与 **327** 个 family-specific closure，retain rate **26.35%**。exact-v1 Review 为 117/117：Deep 56、Standard 61、blocked 0。

当前只是 author-side evidence 闭合：Books disposition 仍为 `Not Assessed`，四项 fresh-context 独立审计保持 Open。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-07-23 |
| Window End | 2026-07-23 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | daily-2026-07-23-0900-v2.1-sha256:41da5e42221a984d7bffcd552283515845f46ee621224cf09812ac94a04efa2b |
| Denominator Frozen At | 2026-09-04T18:30:00+08:00 |
| Completion Status | In Progress |
| Coverage Gate | Open |
| Evidence Gate | Open |
| Books Gate | Open |

### Source Coverage Receipt

<!-- coverage:SRC-ARXIV:20260723:start -->
<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-07-22T09:00:00+08:00 | 2026-07-23T09:00:00+08:00 | 2026-09-04T18:30:00+08:00 | official listings + v1 history + availability schedule; DataCite created only for cycle reconciliation | checked | 444 | SF-2026-ARXIV-2607-19349;SF-2026-ARXIV-2607-19351;SF-2026-ARXIV-2607-19353;SF-2026-ARXIV-2607-19355;SF-2026-ARXIV-2607-19356;SF-2026-ARXIV-2607-19358;SF-2026-ARXIV-2607-19359;SF-2026-ARXIV-2607-19361;SF-2026-ARXIV-2607-19362;SF-2026-ARXIV-2607-19363;SF-2026-ARXIV-2607-19367;SF-2026-ARXIV-2607-19368;SF-2026-ARXIV-2607-19386;SF-2026-ARXIV-2607-19390;SF-2026-ARXIV-2607-19393;SF-2026-ARXIV-2607-19395;SF-2026-ARXIV-2607-19396;SF-2026-ARXIV-2607-19399;SF-2026-ARXIV-2607-19405;SF-2026-ARXIV-2607-19407;SF-2026-ARXIV-2607-19408;SF-2026-ARXIV-2607-19424;SF-2026-ARXIV-2607-19430;SF-2026-ARXIV-2607-19431;SF-2026-ARXIV-2607-19432;SF-2026-ARXIV-2607-19433;SF-2026-ARXIV-2607-19438;SF-2026-ARXIV-2607-19442;SF-2026-ARXIV-2607-19449;SF-2026-ARXIV-2607-19450;SF-2026-ARXIV-2607-19456;SF-2026-ARXIV-2607-19490;SF-2026-ARXIV-2607-19515;SF-2026-ARXIV-2607-19523;SF-2026-ARXIV-2607-19539;SF-2026-ARXIV-2607-19547;SF-2026-ARXIV-2607-19592;SF-2026-ARXIV-2607-19595;SF-2026-ARXIV-2607-19604;SF-2026-ARXIV-2607-19608;SF-2026-ARXIV-2607-19616;SF-2026-ARXIV-2607-19623;SF-2026-ARXIV-2607-19629;SF-2026-ARXIV-2607-19638;SF-2026-ARXIV-2607-19653;SF-2026-ARXIV-2607-19670;SF-2026-ARXIV-2607-19678;SF-2026-ARXIV-2607-19683;SF-2026-ARXIV-2607-19686;SF-2026-ARXIV-2607-19691;SF-2026-ARXIV-2607-19695;SF-2026-ARXIV-2607-19701;SF-2026-ARXIV-2607-19704;SF-2026-ARXIV-2607-19712;SF-2026-ARXIV-2607-19719;SF-2026-ARXIV-2607-19747;SF-2026-ARXIV-2607-19749;SF-2026-ARXIV-2607-19771;SF-2026-ARXIV-2607-19774;SF-2026-ARXIV-2607-19790;SF-2026-ARXIV-2607-19793;SF-2026-ARXIV-2607-19806;SF-2026-ARXIV-2607-19809;SF-2026-ARXIV-2607-19824;SF-2026-ARXIV-2607-19827;SF-2026-ARXIV-2607-19829;SF-2026-ARXIV-2607-19837;SF-2026-ARXIV-2607-19848;SF-2026-ARXIV-2607-19850;SF-2026-ARXIV-2607-19857;SF-2026-ARXIV-2607-19865;SF-2026-ARXIV-2607-19876;SF-2026-ARXIV-2607-19880;SF-2026-ARXIV-2607-19894;SF-2026-ARXIV-2607-19899;SF-2026-ARXIV-2607-19910;SF-2026-ARXIV-2607-19913;SF-2026-ARXIV-2607-19919;SF-2026-ARXIV-2607-19922;SF-2026-ARXIV-2607-19932;SF-2026-ARXIV-2607-19949;SF-2026-ARXIV-2607-19957;SF-2026-ARXIV-2607-19962;SF-2026-ARXIV-2607-19971;SF-2026-ARXIV-2607-19985;SF-2026-ARXIV-2607-19996;SF-2026-ARXIV-2607-20064;SF-2026-ARXIV-2607-20083;SF-2026-ARXIV-2607-20090;SF-2026-ARXIV-2607-20110;SF-2026-ARXIV-2607-20120;SF-2026-ARXIV-2607-20121;SF-2026-ARXIV-2607-20125;SF-2026-ARXIV-2607-20129;SF-2026-ARXIV-2607-20145;SF-2026-ARXIV-2607-20146;SF-2026-ARXIV-2607-20166;SF-2026-ARXIV-2607-20174;SF-2026-ARXIV-2607-20192;SF-2026-ARXIV-2607-20205;SF-2026-ARXIV-2607-20214;SF-2026-ARXIV-2607-20220;SF-2026-ARXIV-2607-20265;SF-2026-ARXIV-2607-20286;SF-2026-ARXIV-2607-20289;SF-2026-ARXIV-2607-20293;SF-2026-ARXIV-2607-20300;SF-2026-ARXIV-2607-20301;SF-2026-ARXIV-2607-20327;SF-2026-ARXIV-2607-20345;SF-2026-ARXIV-2607-20351;SF-2026-ARXIV-2607-20357;SF-2026-ARXIV-2607-20368;SF-2026-ARXIV-2607-20372;SF-2026-ARXIV-2607-20379;SF-2026-ARXIV-2607-20389;SF-2026-ARXIV-2607-20402 | all registered category pages; cross-category dedup complete | 2026-07-23T09:00:00+08:00 | sha256:41da5e42221a984d7bffcd552283515845f46ee621224cf09812ac94a04efa2b | — |
<!-- coverage:SRC-ARXIV:20260723:end -->

### Coverage Limitations

- DataCite 只辅助 owner reconciliation；技术结论全部回到 official exact arXiv v1。
- author-side receipt 已闭合，独立 false-positive / false-negative audit 尚未签收。

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-19349 | arXiv:2607.19349v1 | paper-v1:2607.19349 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-19349 | self | — | new_in_window | INFER-SCHEDULING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19351 | arXiv:2607.19351v1 | paper-v1:2607.19351 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-19351 | self | — | new_in_window | AGENT-MULTI-AGENT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19353 | arXiv:2607.19353v1 | paper-v1:2607.19353 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-19353 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19355 | arXiv:2607.19355v1 | paper-v1:2607.19355 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-19355 | self | — | new_in_window | AGENT-RAG | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19356 | arXiv:2607.19356v1 | paper-v1:2607.19356 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-19356 | self | — | new_in_window | AGENT-TOOL-CALLING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19358 | arXiv:2607.19358v1 | paper-v1:2607.19358 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-19358 | self | — | new_in_window | MODEL-LONG-CONTEXT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19359 | arXiv:2607.19359v1 | paper-v1:2607.19359 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-19359 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19361 | arXiv:2607.19361v1 | paper-v1:2607.19361 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-19361 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19362 | arXiv:2607.19362v1 | paper-v1:2607.19362 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-19362 | self | — | new_in_window | AGENT-RAG | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19363 | arXiv:2607.19363v1 | paper-v1:2607.19363 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-19363 | self | — | new_in_window | MODEL-POSITION-ENCODING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19367 | arXiv:2607.19367v1 | paper-v1:2607.19367 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-19367 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19368 | arXiv:2607.19368v1 | paper-v1:2607.19368 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-19368 | self | — | new_in_window | INFER-PREFILL | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19386 | arXiv:2607.19386v1 | paper-v1:2607.19386 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-19386 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19390 | arXiv:2607.19390v1 | paper-v1:2607.19390 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-19390 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19393 | arXiv:2607.19393v1 | paper-v1:2607.19393 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-19393 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19395 | arXiv:2607.19395v1 | paper-v1:2607.19395 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-19395 | self | — | new_in_window | AGENT-WORKFLOW | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19396 | arXiv:2607.19396v1 | paper-v1:2607.19396 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-19396 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19399 | arXiv:2607.19399v1 | paper-v1:2607.19399 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-19399 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19405 | arXiv:2607.19405v1 | paper-v1:2607.19405 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-19405 | self | — | new_in_window | MODEL-DECODER-ONLY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19407 | arXiv:2607.19407v1 | paper-v1:2607.19407 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-19407 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19408 | arXiv:2607.19408v1 | paper-v1:2607.19408 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-19408 | self | — | new_in_window | TRAIN-PRETRAINING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19424 | arXiv:2607.19424v1 | paper-v1:2607.19424 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-19424 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19430 | arXiv:2607.19430v1 | paper-v1:2607.19430 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-19430 | self | — | new_in_window | AGENT-MULTI-AGENT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19431 | arXiv:2607.19431v1 | paper-v1:2607.19431 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-19431 | self | — | new_in_window | INFER-TENSORRT-LLM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19432 | arXiv:2607.19432v1 | paper-v1:2607.19432 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-19432 | self | — | new_in_window | AGENT-MCP | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19433 | arXiv:2607.19433v1 | paper-v1:2607.19433 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-19433 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19438 | arXiv:2607.19438v1 | paper-v1:2607.19438 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-19438 | self | — | new_in_window | INFER-TENSORRT-LLM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19442 | arXiv:2607.19442v1 | paper-v1:2607.19442 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-19442 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19449 | arXiv:2607.19449v1 | paper-v1:2607.19449 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-19449 | self | — | new_in_window | AGENT-TOOL-CALLING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19450 | arXiv:2607.19450v1 | paper-v1:2607.19450 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-19450 | self | — | new_in_window | TRAIN-RLHF | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19456 | arXiv:2607.19456v1 | paper-v1:2607.19456 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-19456 | self | — | new_in_window | INFER-DECODE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19490 | arXiv:2607.19490v1 | paper-v1:2607.19490 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-19490 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19515 | arXiv:2607.19515v1 | paper-v1:2607.19515 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-19515 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19523 | arXiv:2607.19523v1 | paper-v1:2607.19523 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-19523 | self | — | new_in_window | WORLDVIEW-LLM-INTELLIGENCE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19539 | arXiv:2607.19539v1 | paper-v1:2607.19539 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-19539 | self | — | new_in_window | MODEL-MOE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19547 | arXiv:2607.19547v1 | paper-v1:2607.19547 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-19547 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19592 | arXiv:2607.19592v1 | paper-v1:2607.19592 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-19592 | self | — | new_in_window | AGENT-REFLECTION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19595 | arXiv:2607.19595v1 | paper-v1:2607.19595 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-19595 | self | — | new_in_window | AGENT-PLATFORM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19604 | arXiv:2607.19604v1 | paper-v1:2607.19604 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-19604 | self | — | new_in_window | TRAIN-PRETRAINING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19608 | arXiv:2607.19608v1 | paper-v1:2607.19608 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-19608 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19616 | arXiv:2607.19616v1 | paper-v1:2607.19616 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-19616 | self | — | new_in_window | TRAIN-GRPO | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19623 | arXiv:2607.19623v1 | paper-v1:2607.19623 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-19623 | self | — | new_in_window | INFER-GPU-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19629 | arXiv:2607.19629v1 | paper-v1:2607.19629 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-19629 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19638 | arXiv:2607.19638v1 | paper-v1:2607.19638 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-19638 | self | — | new_in_window | PLATFORM-GPU-SCHEDULER | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19653 | arXiv:2607.19653v1 | paper-v1:2607.19653 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-19653 | self | — | new_in_window | AGENT-REFLECTION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19670 | arXiv:2607.19670v1 | paper-v1:2607.19670 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-19670 | self | — | new_in_window | AGENT-PLATFORM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19678 | arXiv:2607.19678v1 | paper-v1:2607.19678 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-19678 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19683 | arXiv:2607.19683v1 | paper-v1:2607.19683 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-19683 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19686 | arXiv:2607.19686v1 | paper-v1:2607.19686 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-19686 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19691 | arXiv:2607.19691v1 | paper-v1:2607.19691 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-19691 | self | — | new_in_window | WORLDVIEW-LLM-INTELLIGENCE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19695 | arXiv:2607.19695v1 | paper-v1:2607.19695 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-19695 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19701 | arXiv:2607.19701v1 | paper-v1:2607.19701 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-19701 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19704 | arXiv:2607.19704v1 | paper-v1:2607.19704 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-19704 | self | — | new_in_window | INFER-SCHEDULING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19712 | arXiv:2607.19712v1 | paper-v1:2607.19712 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-19712 | self | — | new_in_window | TRAIN-RLHF | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19719 | arXiv:2607.19719v1 | paper-v1:2607.19719 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-19719 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19747 | arXiv:2607.19747v1 | paper-v1:2607.19747 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-19747 | self | — | new_in_window | AGENT-RAG | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19749 | arXiv:2607.19749v1 | paper-v1:2607.19749 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-19749 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19771 | arXiv:2607.19771v1 | paper-v1:2607.19771 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-19771 | self | — | new_in_window | TRAIN-PRETRAINING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19774 | arXiv:2607.19774v1 | paper-v1:2607.19774 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-19774 | self | — | new_in_window | AGENT-MULTI-AGENT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19790 | arXiv:2607.19790v1 | paper-v1:2607.19790 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-19790 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19793 | arXiv:2607.19793v1 | paper-v1:2607.19793 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-19793 | self | — | new_in_window | AGENT-PLATFORM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19806 | arXiv:2607.19806v1 | paper-v1:2607.19806 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-19806 | self | — | new_in_window | WORLDVIEW-LLM-INTELLIGENCE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19809 | arXiv:2607.19809v1 | paper-v1:2607.19809 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-19809 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19824 | arXiv:2607.19824v1 | paper-v1:2607.19824 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-19824 | self | — | new_in_window | TRAIN-DPO | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19827 | arXiv:2607.19827v1 | paper-v1:2607.19827 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-19827 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19829 | arXiv:2607.19829v1 | paper-v1:2607.19829 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-19829 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19837 | arXiv:2607.19837v1 | paper-v1:2607.19837 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-19837 | self | — | new_in_window | AGENT-PLATFORM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19848 | arXiv:2607.19848v1 | paper-v1:2607.19848 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-19848 | self | — | new_in_window | TRAIN-DATA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19850 | arXiv:2607.19850v1 | paper-v1:2607.19850 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-19850 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19857 | arXiv:2607.19857v1 | paper-v1:2607.19857 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-19857 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19865 | arXiv:2607.19865v1 | paper-v1:2607.19865 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-19865 | self | — | new_in_window | AGENT-WORKFLOW | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19876 | arXiv:2607.19876v1 | paper-v1:2607.19876 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-19876 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19880 | arXiv:2607.19880v1 | paper-v1:2607.19880 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-19880 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19894 | arXiv:2607.19894v1 | paper-v1:2607.19894 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-19894 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19899 | arXiv:2607.19899v1 | paper-v1:2607.19899 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-19899 | self | — | new_in_window | AGENT-MULTI-AGENT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19910 | arXiv:2607.19910v1 | paper-v1:2607.19910 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-19910 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19913 | arXiv:2607.19913v1 | paper-v1:2607.19913 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-19913 | self | — | new_in_window | AGENT-PLATFORM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19919 | arXiv:2607.19919v1 | paper-v1:2607.19919 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-19919 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19922 | arXiv:2607.19922v1 | paper-v1:2607.19922 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-19922 | self | — | new_in_window | INFER-GPU-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19932 | arXiv:2607.19932v1 | paper-v1:2607.19932 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-19932 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19949 | arXiv:2607.19949v1 | paper-v1:2607.19949 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-19949 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19957 | arXiv:2607.19957v1 | paper-v1:2607.19957 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-19957 | self | — | new_in_window | INFER-KV-CACHE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19962 | arXiv:2607.19962v1 | paper-v1:2607.19962 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-19962 | self | — | new_in_window | TRAIN-DPO | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19971 | arXiv:2607.19971v1 | paper-v1:2607.19971 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-19971 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19985 | arXiv:2607.19985v1 | paper-v1:2607.19985 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-19985 | self | — | new_in_window | AGENT-MULTI-AGENT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19996 | arXiv:2607.19996v1 | paper-v1:2607.19996 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-19996 | self | — | new_in_window | AGENT-RAG | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20064 | arXiv:2607.20064v1 | paper-v1:2607.20064 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-20064 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20083 | arXiv:2607.20083v1 | paper-v1:2607.20083 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-20083 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20090 | arXiv:2607.20090v1 | paper-v1:2607.20090 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-20090 | self | — | new_in_window | AGENT-RAG | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20110 | arXiv:2607.20110v1 | paper-v1:2607.20110 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-20110 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20120 | arXiv:2607.20120v1 | paper-v1:2607.20120 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-20120 | self | — | new_in_window | PLATFORM-GPU-SCHEDULER | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20121 | arXiv:2607.20121v1 | paper-v1:2607.20121 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-20121 | self | — | new_in_window | AGENT-TOOL-CALLING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20125 | arXiv:2607.20125v1 | paper-v1:2607.20125 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-20125 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20129 | arXiv:2607.20129v1 | paper-v1:2607.20129 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-20129 | self | — | new_in_window | INFER-DECODE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20145 | arXiv:2607.20145v1 | paper-v1:2607.20145 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-20145 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20146 | arXiv:2607.20146v1 | paper-v1:2607.20146 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-20146 | self | — | new_in_window | WORLDVIEW-LLM-INTELLIGENCE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20166 | arXiv:2607.20166v1 | paper-v1:2607.20166 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-20166 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20174 | arXiv:2607.20174v1 | paper-v1:2607.20174 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-20174 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20192 | arXiv:2607.20192v1 | paper-v1:2607.20192 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-20192 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20205 | arXiv:2607.20205v1 | paper-v1:2607.20205 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-20205 | self | — | new_in_window | TRAIN-LORA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20214 | arXiv:2607.20214v1 | paper-v1:2607.20214 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-20214 | self | — | new_in_window | MODEL-SELF-ATTENTION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20220 | arXiv:2607.20220v1 | paper-v1:2607.20220 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-20220 | self | — | new_in_window | MODEL-MOE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20265 | arXiv:2607.20265v1 | paper-v1:2607.20265 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-20265 | self | — | new_in_window | TRAIN-PRETRAINING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20286 | arXiv:2607.20286v1 | paper-v1:2607.20286 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-20286 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20289 | arXiv:2607.20289v1 | paper-v1:2607.20289 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-20289 | self | — | new_in_window | AGENT-PLANNING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20293 | arXiv:2607.20293v1 | paper-v1:2607.20293 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-20293 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20300 | arXiv:2607.20300v1 | paper-v1:2607.20300 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-20300 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20301 | arXiv:2607.20301v1 | paper-v1:2607.20301 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-20301 | self | — | new_in_window | TRAIN-LORA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20327 | arXiv:2607.20327v1 | paper-v1:2607.20327 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-20327 | self | — | new_in_window | INFER-SCHEDULING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20345 | arXiv:2607.20345v1 | paper-v1:2607.20345 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-20345 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20351 | arXiv:2607.20351v1 | paper-v1:2607.20351 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-20351 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20357 | arXiv:2607.20357v1 | paper-v1:2607.20357 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-20357 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20368 | arXiv:2607.20368v1 | paper-v1:2607.20368 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-20368 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20372 | arXiv:2607.20372v1 | paper-v1:2607.20372 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-20372 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20379 | arXiv:2607.20379v1 | paper-v1:2607.20379 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-20379 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20389 | arXiv:2607.20389v1 | paper-v1:2607.20389 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-20389 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20402 | arXiv:2607.20402v1 | paper-v1:2607.20402 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-20402 | self | — | new_in_window | WORLDVIEW-REPRESENTATION | Not Assessed | — | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-19349 | RP-a796a4e40885a132 | deep | arXiv:2607.19349v1 | SRC-ARXIV@arXiv:2607.19349v1 | https://arxiv.org/html/2607.19349v1#A3.SS1 — C.1. Architecture-Specific Input–Output Token Models; https://arxiv.org/html/2607.19349v1#S3 — 3. Characterizing Architectures and Scales | https://arxiv.org/html/2607.19349v1#S1 — 1. Introduction; https://arxiv.org/html/2607.19349v1#S2 — 2. Preliminary and Motivation | https://arxiv.org/html/2607.19349v1#S6 — 6. Conclusion | Exact v1 links https://github.com/hihiztc1/FineServe, https://github.com/microsoft/DeepSpeed-MII, https://github.com/NVIDIA/TensorRT-LLM; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19349 | complete |
| SF-2026-ARXIV-2607-19351 | RP-d8ffffee54dead3c | deep | arXiv:2607.19351v1 | SRC-ARXIV@arXiv:2607.19351v1 | https://arxiv.org/html/2607.19351v1#A1.SS2 — A.2 Implementation Details; https://arxiv.org/html/2607.19351v1#A2 — Appendix B Full Algorithm | https://arxiv.org/html/2607.19351v1#A3 — Appendix C Additional Experiment Results; https://arxiv.org/html/2607.19351v1#A1 — Appendix A Experiment Details | https://arxiv.org/html/2607.19351v1#A6 — Appendix F Limitations; https://arxiv.org/html/2607.19351v1#S5 — 5 Conclusion | Exact v1 links https://neurips.cc/public/guides/CodeSubmissionPolicy, https://paperswithcode.com/datasets, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19351 | complete |
| SF-2026-ARXIV-2607-19353 | RP-2433867da649f917 | deep | arXiv:2607.19353v1 | SRC-ARXIV@arXiv:2607.19353v1 | https://arxiv.org/html/2607.19353v1#S3.SS4 — 3.4 Load-Generation Methodology; https://arxiv.org/html/2607.19353v1#S3.SS2 — 3.2 Models and Execution Modes | https://arxiv.org/html/2607.19353v1#A1 — Appendix A Full Closed-Loop Results; https://arxiv.org/html/2607.19353v1#S3 — 3 Experimental Setup | https://arxiv.org/html/2607.19353v1#S7 — 7 Limitations and Threats to Validity; https://arxiv.org/html/2607.19353v1#S6 — 6 Discussion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19353 | complete |
| SF-2026-ARXIV-2607-19355 | RP-7defa631d5b16816 | standard | arXiv:2607.19355v1 | SRC-ARXIV@arXiv:2607.19355v1 | https://arxiv.org/html/2607.19355v1#A8.SS1 — H.1 Model Setup | https://arxiv.org/html/2607.19355v1#A10 — Appendix J Additional Main Experiment Results; https://arxiv.org/html/2607.19355v1#A3.SS4 — C.4 Results | https://arxiv.org/html/2607.19355v1#S10 — 10 Discussion | Exact v1 links https://github.com/josh-ashkinaze/l2d-public, https://huggingface.co/datasets/CogComp/trec, https://huggingface.co/prajjwal1/bert-tiny; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19355 | complete |
| SF-2026-ARXIV-2607-19356 | RP-f5399eea1dd495d2 | deep | arXiv:2607.19356v1 | SRC-ARXIV@arXiv:2607.19356v1 | https://arxiv.org/html/2607.19356v1#S4 — 4 The NEXUS Framework; https://arxiv.org/html/2607.19356v1#A1 — Appendix A Runtime Monitoring Algorithm | https://arxiv.org/html/2607.19356v1#A11 — Appendix K Error Analysis; https://arxiv.org/html/2607.19356v1#A14 — Appendix N R-Judge IoT: Trace-Level Failure Analysis | https://arxiv.org/html/2607.19356v1#A14 — Appendix N R-Judge IoT: Trace-Level Failure Analysis; https://arxiv.org/html/2607.19356v1#A17 — Appendix Q Deployment Posture and Future Extensions | Exact v1 links https://github.com/openai/swarm, https://github.com/eliashossain001/nexus, https://huggingface.co/EliasHossain/nexus-risk-scorer; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19356 | complete |
| SF-2026-ARXIV-2607-19358 | RP-23968e97a4a251de | deep | arXiv:2607.19358v1 | SRC-ARXIV@arXiv:2607.19358v1 | https://arxiv.org/html/2607.19358v1#S3 — 3 Method; https://arxiv.org/html/2607.19358v1#S4.SS1 — 4.1 Implementation Details | https://arxiv.org/html/2607.19358v1#S4 — 4 Experiments; https://arxiv.org/html/2607.19358v1#S4.SS4 — 4.4 Main Results | https://arxiv.org/html/2607.19358v1#S5 — 5 Conclusion; https://arxiv.org/html/2607.19358v1#S6 — 6 Limitations | Exact v1 links https://huggingface.co/datasets/Maxwell-Jia/AIME_2024, https://huggingface.co/datasets/opencompass/AIME2025, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19358 | complete |
| SF-2026-ARXIV-2607-19359 | RP-408ea417f460817b | deep | arXiv:2607.19359v1 | SRC-ARXIV@arXiv:2607.19359v1 | https://arxiv.org/html/2607.19359v1#A3 — Appendix C Baseline Implementation Details | https://arxiv.org/html/2607.19359v1#S4 — 4 MemHop Benchmark; https://arxiv.org/html/2607.19359v1#S5 — 5 Experiments | https://arxiv.org/html/2607.19359v1#S6 — 6 Discussion; https://arxiv.org/html/2607.19359v1#S7 — 7 Conclusion | Exact v1 links https://github.com/ShengtongZhu/ProGraph, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19359 | complete |
| SF-2026-ARXIV-2607-19361 | RP-7b4f6472b66098a4 | deep | arXiv:2607.19361v1 | SRC-ARXIV@arXiv:2607.19361v1 | https://arxiv.org/html/2607.19361v1#S4 — 4 The CRA Framework; https://arxiv.org/html/2607.19361v1#S5 — 5 Design Consistency Properties | https://arxiv.org/html/2607.19361v1#S9.SS9 — 9.9 Ablation analysis; https://arxiv.org/html/2607.19361v1#S2.SS1 — 2.1 Multi-turn safety evaluation and dialogue state modeling | https://arxiv.org/html/2607.19361v1#S12 — 12 Discussion and Limitations; https://arxiv.org/html/2607.19361v1#S13 — 13 Conclusions | Exact v1 links https://huggingface.co/datasets/Asap7772/cosafe_all_rollouts, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19361 | complete |
| SF-2026-ARXIV-2607-19362 | RP-05779ca20748771b | standard | arXiv:2607.19362v1 | SRC-ARXIV@arXiv:2607.19362v1 | https://arxiv.org/html/2607.19362v1#S2 — 2. System Overview | https://arxiv.org/html/2607.19362v1#S3.SS2 — 3.2. Scenario 2: Comparative Retrieval Analysis; https://arxiv.org/html/2607.19362v1#S4 — 4. Experimental Study | https://arxiv.org/html/2607.19362v1#S5 — 5. Conclusions and Future Works | Exact v1 links https://github.com/asmath472/GraphContainer, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19362 | complete |
| SF-2026-ARXIV-2607-19363 | RP-33240c0e0078e38b | standard | arXiv:2607.19363v1 | SRC-ARXIV@arXiv:2607.19363v1 | https://arxiv.org/html/2607.19363v1#S3.SS3 — 3.3 Design of AdaRoPE; https://arxiv.org/html/2607.19363v1#S3.SS4 — 3.4 Implementation and Overhead | https://arxiv.org/html/2607.19363v1#A2 — Appendix B Additional Results; https://arxiv.org/html/2607.19363v1#A2.SS1 — B.1 Analysis on Synthetic Tasks | https://arxiv.org/html/2607.19363v1#S6 — 6 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19363 | complete |
| SF-2026-ARXIV-2607-19367 | RP-7eec19f21c372848 | deep | arXiv:2607.19367v1 | SRC-ARXIV@arXiv:2607.19367v1 | https://arxiv.org/html/2607.19367v1#S4 — 4 Methodology; https://arxiv.org/html/2607.19367v1#S4.SS2 — 4.2 Confidence Estimation Methods | https://arxiv.org/html/2607.19367v1#A3 — Appendix C Full Benchmark Results; https://arxiv.org/html/2607.19367v1#A2 — Appendix B Experimental Setup | https://arxiv.org/html/2607.19367v1#A1.SS2 — A.2 Limitations of LLM-Based Semantic Clustering; https://arxiv.org/html/2607.19367v1#S5 — 5 Discussion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19367 | complete |
| SF-2026-ARXIV-2607-19368 | RP-9aa903952bf7288a | deep | arXiv:2607.19368v1 | SRC-ARXIV@arXiv:2607.19368v1 | https://arxiv.org/html/2607.19368v1#S3 — 3 Method; https://arxiv.org/html/2607.19368v1#A2.SS1 — B.1 Implementation Summary | https://arxiv.org/html/2607.19368v1#A3 — Appendix C Additional Experimental Results; https://arxiv.org/html/2607.19368v1#S5 — 5 Experiments and Results | https://arxiv.org/html/2607.19368v1#S6 — 6 Discussion and Limitations; https://arxiv.org/html/2607.19368v1#S5.SS7 — 5.7 Results Discussion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19368 | complete |
| SF-2026-ARXIV-2607-19386 | RP-5784ca85a8ceb79d | standard | arXiv:2607.19386v1 | SRC-ARXIV@arXiv:2607.19386v1 | https://arxiv.org/html/2607.19386v1#S3.SSx1 — Methodological Variance Exceeds Architectural Variance; https://arxiv.org/html/2607.19386v1#A4.SS1 — D.1 Pythia SAE models | https://arxiv.org/html/2607.19386v1#A2 — Appendix B Experiments; https://arxiv.org/html/2607.19386v1#A2.SS1 — B.1 Experiment Overview | https://arxiv.org/html/2607.19386v1#S5 — 5 Conclusion | Exact v1 links https://huggingface.co/datasets/codeparrot/github-code, https://neurips.cc/public/guides/CodeSubmissionPolicy, https://paperswithcode.com/datasets; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19386 | complete |
| SF-2026-ARXIV-2607-19390 | RP-c6a3bc512b306191 | standard | arXiv:2607.19390v1 | SRC-ARXIV@arXiv:2607.19390v1 | https://arxiv.org/html/2607.19390v1#S11.SS0.SSS0.Px1 — Benchmark-driven architecture selection.; https://arxiv.org/html/2607.19390v1#S12.SS0.SSS0.Px3 — Orthogonalization in learning systems. | https://arxiv.org/html/2607.19390v1#S11.SS0.SSS0.Px1 — Benchmark-driven architecture selection.; https://arxiv.org/html/2607.19390v1#S6.SS0.SSS0.Px1 — Swap evaluations. | https://arxiv.org/html/2607.19390v1#S11 — 11 Discussion; https://arxiv.org/html/2607.19390v1#S13 — 13 Limitations | Exact v1 links https://github.com/no-way-labs/recurrent-memory-scaffold, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19390 | complete |
| SF-2026-ARXIV-2607-19393 | RP-1942ff2c443421d7 | standard | arXiv:2607.19393v1 | SRC-ARXIV@arXiv:2607.19393v1 | https://arxiv.org/html/2607.19393v1#S5.SS1 — 5.1 Design | https://arxiv.org/html/2607.19393v1#S4 — 4 A Benchmark Leak in Near-OOD Evaluation; https://arxiv.org/html/2607.19393v1#A2 — Appendix B Per-Seed Results for the Leak | https://arxiv.org/html/2607.19393v1#S10 — 10 Conclusion; https://arxiv.org/html/2607.19393v1#S9 — 9 Discussion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19393 | complete |
| SF-2026-ARXIV-2607-19395 | RP-92ca6e979d2a8094 | standard | arXiv:2607.19395v1 | SRC-ARXIV@arXiv:2607.19395v1 | https://arxiv.org/html/2607.19395v1#S3 — 3 Method; https://arxiv.org/html/2607.19395v1#A2 — Appendix B Implementation Details in Each Environment | https://arxiv.org/html/2607.19395v1#A3 — Appendix C Additional Experimental Results; https://arxiv.org/html/2607.19395v1#A3.SS1 — C.1 Additional TextCraft Objective Ablations | https://arxiv.org/html/2607.19395v1#S5 — 5 Conclusion and Future Work; https://arxiv.org/html/2607.19395v1#A4.SS3 — D.3 Failure Modes | Exact v1 links https://github.com/HappynessI/Prefix_GRPO, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19395 | complete |
| SF-2026-ARXIV-2607-19396 | RP-c920ef378916a6d2 | deep | arXiv:2607.19396v1 | SRC-ARXIV@arXiv:2607.19396v1 | https://arxiv.org/html/2607.19396v1#S2.SS1 — 2.1 Prompt injection in LLM-integrated systems; https://arxiv.org/html/2607.19396v1#S2.SS6 — 2.6 Testing methodology and security framing | https://arxiv.org/html/2607.19396v1#S4.SS1 — 4.1 Benchmark construction and problem setup; https://arxiv.org/html/2607.19396v1#S4.SS8 — 4.8 Evaluation metrics | https://arxiv.org/html/2607.19396v1#S6 — 6 Conclusion | Exact v1 links https://github.com/tldrsec/prompt-injection-defenses, https://www.promptfoo.dev/lm-security-db/vuln/invisible-unicode-jailbreak-779fc810, https://huggingface.co/meta-llama/Prompt-Guard-86M; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19396 | complete |
| SF-2026-ARXIV-2607-19399 | RP-4435a6d881218484 | standard | arXiv:2607.19399v1 | SRC-ARXIV@arXiv:2607.19399v1 | https://arxiv.org/html/2607.19399v1#S4 — 4 Method; https://arxiv.org/html/2607.19399v1#S2.SS1 — 2.1 Reinforcement Learning for Vision–Language–Action Models | https://arxiv.org/html/2607.19399v1#S5 — 5 Experiments; https://arxiv.org/html/2607.19399v1#S5.SS1 — 5.1 Baseline Results and Reproduction | https://arxiv.org/html/2607.19399v1#S6.SS3 — 6.3 Discussion of SFT-Initialized RL; https://arxiv.org/html/2607.19399v1#S6.SS4 — 6.4 Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19399 | complete |
| SF-2026-ARXIV-2607-19405 | RP-89fe0364dfe4e56c | standard | arXiv:2607.19405v1 | SRC-ARXIV@arXiv:2607.19405v1 | https://arxiv.org/html/2607.19405v1#S2 — 2 Methodology | https://arxiv.org/html/2607.19405v1#S4.SS1 — 4.1 Phase change analysis | https://arxiv.org/html/2607.19405v1#S5 — 5 Conclusion | Exact v1 links https://github.com/COMP6258-Reproducibility-Challenge/CoTFormer, https://github.com/epfml/CoTFormer, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19405 | complete |
| SF-2026-ARXIV-2607-19407 | RP-1a1c7369dc77e043 | standard | arXiv:2607.19407v1 | SRC-ARXIV@arXiv:2607.19407v1 | https://arxiv.org/html/2607.19407v1#A4.SS2 — D.2 Cross ITP translation benchmarks and systems; https://arxiv.org/html/2607.19407v1#S3 — 3 Benchmark Design | https://arxiv.org/html/2607.19407v1#S4 — 4 Evaluation and Results; https://arxiv.org/html/2607.19407v1#A1 — Appendix A Full Per-Model Results | https://arxiv.org/html/2607.19407v1#A6.SS4 — F.4 Failure Examples; https://arxiv.org/html/2607.19407v1#S4.SS9 — 4.9 Discussion | Exact v1 links https://huggingface.co/datasets/jiayi005/ITPEval, https://github.com/lean-dojo/ITPEval, https://github.com/rocq-community/coqtail-math; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19407 | complete |
| SF-2026-ARXIV-2607-19408 | RP-6e9a53498114eb87 | deep | arXiv:2607.19408v1 | SRC-ARXIV@arXiv:2607.19408v1 | https://arxiv.org/html/2607.19408v1#A1 — Appendix A Algorithmic Conventions: MeZO and ES-at-Scale | https://arxiv.org/html/2607.19408v1#A5 — Appendix E Pre-Training Degeneracy Probe: Protocol and Results; https://arxiv.org/html/2607.19408v1#A5.SS0.SSS0.Px2 — Results. | https://arxiv.org/html/2607.19408v1#S5 — 5 Discussion and Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19408 | complete |
| SF-2026-ARXIV-2607-19424 | RP-78cb8ef643430a59 | standard | arXiv:2607.19424v1 | SRC-ARXIV@arXiv:2607.19424v1 | https://arxiv.org/html/2607.19424v1#A1.SS3 — A.3 Jailbreak Methods in Jailbreak Attack Dataset; https://arxiv.org/html/2607.19424v1#A3.SS4 — C.4 Model Sensitivity of Various Evaluation Methods | https://arxiv.org/html/2607.19424v1#S5 — 5 Experiments and Analysis; https://arxiv.org/html/2607.19424v1#A3 — Appendix C Supplementary Experiments | https://arxiv.org/html/2607.19424v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.19424v1#Sx1 — Limitations | Exact v1 links https://github.com/Magi2B0y/JailMeter, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19424 | complete |
| SF-2026-ARXIV-2607-19430 | RP-3d3241791e201c6a | deep | arXiv:2607.19430v1 | SRC-ARXIV@arXiv:2607.19430v1 | https://arxiv.org/html/2607.19430v1#S4 — 4. The ChannelGuard Framework; https://arxiv.org/html/2607.19430v1#A2 — Appendix B The Full Pipeline Algorithm and Three Further Formal Properties | https://arxiv.org/html/2607.19430v1#A6 — Appendix F Gate Ablation; https://arxiv.org/html/2607.19430v1#S5 — 5. Experimental Setup | https://arxiv.org/html/2607.19430v1#S7 — 7. Discussion and Limitations; https://arxiv.org/html/2607.19430v1#A15 — Appendix O Reproducibility Notes on Two Failure Modes | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19430 | complete |
| SF-2026-ARXIV-2607-19431 | RP-5160bd5ac2fcfdce | deep | arXiv:2607.19431v1 | SRC-ARXIV@arXiv:2607.19431v1 | https://arxiv.org/html/2607.19431v1#S3 — 3. BRIM Methodology; https://arxiv.org/html/2607.19431v1#S3.SS2 — 3.2. Hardware Architecture | https://arxiv.org/html/2607.19431v1#S4 — 4. Experimental Setup; https://arxiv.org/html/2607.19431v1#S5 — 5. Evaluation | https://arxiv.org/html/2607.19431v1#S6 — 6. Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19431 | complete |
| SF-2026-ARXIV-2607-19432 | RP-cadcada33f773b0b | deep | arXiv:2607.19432v1 | SRC-ARXIV@arXiv:2607.19432v1 | https://arxiv.org/html/2607.19432v1#S2.SS1 — II-A MCP Architecture; https://arxiv.org/html/2607.19432v1#S4 — IV ChainWatch Framework | https://arxiv.org/html/2607.19432v1#S3 — III Threat Analysis; https://arxiv.org/html/2607.19432v1#S5 — V Evaluation | https://arxiv.org/html/2607.19432v1#S3 — III Threat Analysis; https://arxiv.org/html/2607.19432v1#S6 — VI Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19432 | complete |
| SF-2026-ARXIV-2607-19433 | RP-4f3623e4392e02cc | deep | arXiv:2607.19433v1 | SRC-ARXIV@arXiv:2607.19433v1 | https://arxiv.org/html/2607.19433v1#S2.SS1 — II-A Foundational Architectures: Mapping the BDI Stack; https://arxiv.org/html/2607.19433v1#S3.SS3 — III-C Agent Session Smuggling in Multi-Agent Systems | https://arxiv.org/html/2607.19433v1#S4 — IV Case Study: EchoLeak and Zero-Click Exfiltration | https://arxiv.org/html/2607.19433v1#S2.SS4 — II-D Threat Model and Adversarial Capabilities; https://arxiv.org/html/2607.19433v1#S7 — VII Future Directions: Hardware-Anchored Trust | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19433 | complete |
| SF-2026-ARXIV-2607-19438 | RP-26fc47a1b837962e | deep | arXiv:2607.19438v1 | SRC-ARXIV@arXiv:2607.19438v1 | https://arxiv.org/html/2607.19438v1#S1 — 1 Introduction; https://arxiv.org/html/2607.19438v1#S1.SS1 — 1.1 Contributions | https://arxiv.org/html/2607.19438v1#S4 — 4 Evaluation; https://arxiv.org/html/2607.19438v1#S4.SS1 — 4.1 Experimental Setup | https://arxiv.org/html/2607.19438v1#S4.SS4 — 4.4 Discussion of Results; https://arxiv.org/html/2607.19438v1#S5 — 5 Discussion | Exact v1 links https://github.com/basecompute/baseRT, https://github.com/ggml-org/llama.cpp, https://github.com/ml-explore/mlx; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19438 | complete |
| SF-2026-ARXIV-2607-19442 | RP-37b01adc8d6a875f | standard | arXiv:2607.19442v1 | SRC-ARXIV@arXiv:2607.19442v1 | https://arxiv.org/html/2607.19442v1#A2 — Appendix B Methods and Hyperparameters | https://arxiv.org/html/2607.19442v1#S1 — 1 Introduction; https://arxiv.org/html/2607.19442v1#S2 — 2 Controlled Testbed with a Matched Retraining Reference | https://arxiv.org/html/2607.19442v1#S11 — 11 Limitations; https://arxiv.org/html/2607.19442v1#S12 — 12 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19442 | complete |
| SF-2026-ARXIV-2607-19449 | RP-fb1f0662cf709832 | standard | arXiv:2607.19449v1 | SRC-ARXIV@arXiv:2607.19449v1 | https://arxiv.org/html/2607.19449v1#S3.SS3 — 3.3. Prompt Design; https://arxiv.org/html/2607.19449v1#S6 — 6. Ablation: Effect of Safety-Framed System Prompt | https://arxiv.org/html/2607.19449v1#S3 — 3. Experimental Setup; https://arxiv.org/html/2607.19449v1#S4 — 4. Results | https://arxiv.org/html/2607.19449v1#S3.SS2 — 3.2. Failure Injection; https://arxiv.org/html/2607.19449v1#S4.SS2 — 4.2. Breakdown by Failure Type | Exact v1 links https://github.com/langchain-ai/langchain, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19449 | complete |
| SF-2026-ARXIV-2607-19450 | RP-0be702b655632fe8 | standard | arXiv:2607.19450v1 | SRC-ARXIV@arXiv:2607.19450v1 | https://arxiv.org/html/2607.19450v1#A2 — Appendix B Reward Design Across Domains; https://arxiv.org/html/2607.19450v1#S3 — 3 Methodology | https://arxiv.org/html/2607.19450v1#S4.SS3 — 4.3 Ablations and Analysis; https://arxiv.org/html/2607.19450v1#A1 — Appendix A Other Evaluation Criteria | https://arxiv.org/html/2607.19450v1#S5 — 5 Conclusion and Discussion | Exact v1 links https://huggingface.co/datasets/HuggingFaceH4/ifeval-like-data, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19450 | complete |
| SF-2026-ARXIV-2607-19456 | RP-b35d01dfb6519956 | standard | arXiv:2607.19456v1 | SRC-ARXIV@arXiv:2607.19456v1 | https://arxiv.org/html/2607.19456v1#S3 — 3 Python Implementation; https://arxiv.org/html/2607.19456v1#S3.SSx2 — MoA - Based Implementation | https://arxiv.org/html/2607.19456v1#S1 — 1 Introduction; https://arxiv.org/html/2607.19456v1#S1.SS1 — 1.1 Background | https://arxiv.org/html/2607.19456v1#S8 — 8 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19456 | complete |
| SF-2026-ARXIV-2607-19490 | RP-e0e4ecc1effd14d4 | deep | arXiv:2607.19490v1 | SRC-ARXIV@arXiv:2607.19490v1 | https://arxiv.org/html/2607.19490v1#S3 — 3 Method; https://arxiv.org/html/2607.19490v1#S4.SS4 — 4.4 Experimental design | https://arxiv.org/html/2607.19490v1#S5 — 5 Experimental Results; https://arxiv.org/html/2607.19490v1#S4 — 4 Experimental Setup | https://arxiv.org/html/2607.19490v1#S6 — 6 Limitations and Future Work; https://arxiv.org/html/2607.19490v1#S3.SS2 — 3.2 Threat model | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19490 | complete |
| SF-2026-ARXIV-2607-19515 | RP-f0ac1f6310fc3deb | deep | arXiv:2607.19515v1 | SRC-ARXIV@arXiv:2607.19515v1 | https://arxiv.org/html/2607.19515v1#S2 — 2. Methodology | https://arxiv.org/html/2607.19515v1#S2.SS4 — 2.4. Metrics and P-Frame Analysis; https://arxiv.org/html/2607.19515v1#S3 — 3. Results and Discussion | https://arxiv.org/html/2607.19515v1#S3 — 3. Results and Discussion; https://arxiv.org/html/2607.19515v1#S4 — 4. Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19515 | complete |
| SF-2026-ARXIV-2607-19523 | RP-e5317b56635de9f6 | standard | arXiv:2607.19523v1 | SRC-ARXIV@arXiv:2607.19523v1 | https://arxiv.org/html/2607.19523v1#A1 — Appendix A Implementation Details | https://arxiv.org/html/2607.19523v1#S4 — 4 Main Experiments: Policy Evaluation and Game-Playing; https://arxiv.org/html/2607.19523v1#A2 — Appendix B Additional Experiments | https://arxiv.org/html/2607.19523v1#S6 — 6 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19523 | complete |
| SF-2026-ARXIV-2607-19539 | RP-e1f5f7bc2fb5d895 | deep | arXiv:2607.19539v1 | SRC-ARXIV@arXiv:2607.19539v1 | https://arxiv.org/html/2607.19539v1#S3 — 3. System Design; https://arxiv.org/html/2607.19539v1#S2.SS1 — 2.1. Mixture-of-Experts Architectures | https://arxiv.org/html/2607.19539v1#S4 — 4. Experimental Results; https://arxiv.org/html/2607.19539v1#S4.SS1 — 4.1. Experimental Setup | https://arxiv.org/html/2607.19539v1#S6 — 6. Conclusion | Exact v1 links https://github.com/NVIDIA/cutlass, https://github.com/fanshiqing/grouped_gemm, https://github.com/NVIDIA/TransformerEngine; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19539 | complete |
| SF-2026-ARXIV-2607-19547 | RP-710885697b084d0b | deep | arXiv:2607.19547v1 | SRC-ARXIV@arXiv:2607.19547v1 | https://arxiv.org/html/2607.19547v1#S2 — 2 Methodology | https://arxiv.org/html/2607.19547v1#S3 — 3 Results and Discussion | https://arxiv.org/html/2607.19547v1#S3 — 3 Results and Discussion; https://arxiv.org/html/2607.19547v1#S4 — 4 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19547 | complete |
| SF-2026-ARXIV-2607-19592 | RP-2bc2b2522961a3eb | standard | arXiv:2607.19592v1 | SRC-ARXIV@arXiv:2607.19592v1 | https://arxiv.org/html/2607.19592v1#S3.SS1 — 3.1 System Overview | https://arxiv.org/html/2607.19592v1#A11 — Appendix K Benchmark Details; https://arxiv.org/html/2607.19592v1#A4 — Appendix D Prompts by Benchmark | https://arxiv.org/html/2607.19592v1#S5 — 5 Conclusion | Exact v1 links https://github.com/recursive-knowledge/KSI, https://github.com/block/goose, https://github.com/krafton-ai/KIRA; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19592 | complete |
| SF-2026-ARXIV-2607-19595 | RP-c1f4f114747c2be6 | deep | arXiv:2607.19595v1 | SRC-ARXIV@arXiv:2607.19595v1 | https://arxiv.org/html/2607.19595v1#A4 — Appendix D SWE-agent system prompts; https://arxiv.org/html/2607.19595v1#S3 — 3 Methodology | https://arxiv.org/html/2607.19595v1#S5.SS2 — 5.2 Main Results Across Benchmarks; https://arxiv.org/html/2607.19595v1#A1 — Appendix A Implementation of the guardrails and ablation study | https://arxiv.org/html/2607.19595v1#A6 — Appendix F Failure case study; https://arxiv.org/html/2607.19595v1#S6 — 6 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19595 | complete |
| SF-2026-ARXIV-2607-19604 | RP-6bff82504f0df3b2 | standard | arXiv:2607.19604v1 | SRC-ARXIV@arXiv:2607.19604v1 | https://arxiv.org/html/2607.19604v1#A4 — Appendix D Hypernetwork Architecture Details; https://arxiv.org/html/2607.19604v1#A4.SS2 — D.2 Encoder Architecture | https://arxiv.org/html/2607.19604v1#S3.SS3 — 3.3 Evaluation Protocol and OOD Splits; https://arxiv.org/html/2607.19604v1#S5 — 5 Experiments | https://arxiv.org/html/2607.19604v1#S6 — 6 Conclusion and Future Work | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19604 | complete |
| SF-2026-ARXIV-2607-19608 | RP-16a1ce6fb8df91fc | standard | arXiv:2607.19608v1 | SRC-ARXIV@arXiv:2607.19608v1 | https://arxiv.org/html/2607.19608v1#S4.SS4 — 4.4 Prompt Design; https://arxiv.org/html/2607.19608v1#S4.SS1 — 4.1 Models | https://arxiv.org/html/2607.19608v1#A1 — Appendix A Experimental Details; https://arxiv.org/html/2607.19608v1#A2 — Appendix B Prompt-Variant Results | https://arxiv.org/html/2607.19608v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.19608v1#Sx1 — Limitations | Exact v1 links https://github.com/farajimahdieh/language-model-task-competence-vs-instruction-following, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19608 | complete |
| SF-2026-ARXIV-2607-19616 | RP-fa3395931bdb55a3 | standard | arXiv:2607.19616v1 | SRC-ARXIV@arXiv:2607.19616v1 | https://arxiv.org/html/2607.19616v1#S4 — 4 Method; https://arxiv.org/html/2607.19616v1#S4.SSx4 — Study Design | https://arxiv.org/html/2607.19616v1#S5 — 5 Experimental Setup; https://arxiv.org/html/2607.19616v1#S6 — 6 Results | https://arxiv.org/html/2607.19616v1#S8 — 8 Discussion; https://arxiv.org/html/2607.19616v1#S9 — 9 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19616 | complete |
| SF-2026-ARXIV-2607-19623 | RP-dbd79eb7460f73d6 | deep | arXiv:2607.19623v1 | SRC-ARXIV@arXiv:2607.19623v1 | https://arxiv.org/html/2607.19623v1#S5 — 5. Hardware Architecture: Unequal Error Protection for ML Inference; https://arxiv.org/html/2607.19623v1#S6 — 6. Design Space Exploration and Reliability | https://arxiv.org/html/2607.19623v1#S3 — 3. Fault modeling and experimental setup; https://arxiv.org/html/2607.19623v1#S4 — 4. Bit-Position Sensitivity Results | https://arxiv.org/html/2607.19623v1#S7 — 7. Discussion, Limitations, and Future Work; https://arxiv.org/html/2607.19623v1#S8 — 8. Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19623 | complete |
| SF-2026-ARXIV-2607-19629 | RP-6ca542a42c264596 | standard | arXiv:2607.19629v1 | SRC-ARXIV@arXiv:2607.19629v1 | https://arxiv.org/html/2607.19629v1#Sx10.SSx2 — Design Properties; https://arxiv.org/html/2607.19629v1#Sx2.SSx1 — Paternalism–Autonomy Tradeoffs in AI Design | https://arxiv.org/html/2607.19629v1#Sx3.SSx1 — Experimental Setup; https://arxiv.org/html/2607.19629v1#Sx3.SSx4 — Analysis Procedure | https://arxiv.org/html/2607.19629v1#Sx5.SSx1 — Limitations and Future Work; https://arxiv.org/html/2607.19629v1#Sx6 — Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19629 | complete |
| SF-2026-ARXIV-2607-19638 | RP-704393854c8dd70b | deep | arXiv:2607.19638v1 | SRC-ARXIV@arXiv:2607.19638v1 | https://arxiv.org/html/2607.19638v1#S3.SS4 — 3.4 Reduction to a generalized Kuramoto system | https://arxiv.org/html/2607.19638v1#S4 — 4 Analysis; https://arxiv.org/html/2607.19638v1#S6 — 6 Numerical study | https://arxiv.org/html/2607.19638v1#S7 — 7 Discussion; https://arxiv.org/html/2607.19638v1#S8 — 8 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19638 | complete |
| SF-2026-ARXIV-2607-19653 | RP-f2eeb5a99c47f131 | standard | arXiv:2607.19653v1 | SRC-ARXIV@arXiv:2607.19653v1 | https://arxiv.org/html/2607.19653v1#S1 — I Introduction; https://arxiv.org/html/2607.19653v1#S2 — II Benchmarks Overview | https://arxiv.org/html/2607.19653v1#A4 — Appendix D Manual Review of Per-Task Win/Loss Analysis; https://arxiv.org/html/2607.19653v1#S2 — II Benchmarks Overview | https://arxiv.org/html/2607.19653v1#S7 — VII Conclusion and Future Work; https://arxiv.org/html/2607.19653v1#S6 — VI Threats to Validity | Exact v1 links https://github.com/openai/codex, https://github.com/benfred/py-spy, https://huggingface.co/moonshotai/Kimi-K2-Instruct; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19653 | complete |
| SF-2026-ARXIV-2607-19670 | RP-0e2b588e9ab54772 | standard | arXiv:2607.19670v1 | SRC-ARXIV@arXiv:2607.19670v1 | https://arxiv.org/html/2607.19670v1#S3 — 3 Formal Framework; https://arxiv.org/html/2607.19670v1#S4 — 4 Minimal Empirical Design and Estimation | https://arxiv.org/html/2607.19670v1#S5 — 5 Results; https://arxiv.org/html/2607.19670v1#S4.SS1 — 4.1 Source study and retained scope | https://arxiv.org/html/2607.19670v1#S6 — 6 Discussion; https://arxiv.org/html/2607.19670v1#S7 — 7 Limitations and Validity | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19670 | complete |
| SF-2026-ARXIV-2607-19678 | RP-715fe45fd809178d | standard | arXiv:2607.19678v1 | SRC-ARXIV@arXiv:2607.19678v1 | https://arxiv.org/html/2607.19678v1#S3 — 3 Methodology; https://arxiv.org/html/2607.19678v1#A1 — Appendix A Implementation Details | https://arxiv.org/html/2607.19678v1#S5 — 5 Results and Analysis; https://arxiv.org/html/2607.19678v1#A5 — Appendix E Experimental Setup | https://arxiv.org/html/2607.19678v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.19678v1#Sx1 — Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19678 | complete |
| SF-2026-ARXIV-2607-19683 | RP-e15fd7f447d195dc | standard | arXiv:2607.19683v1 | SRC-ARXIV@arXiv:2607.19683v1 | https://arxiv.org/html/2607.19683v1#S3 — 3. Threat Model and Challenges; https://arxiv.org/html/2607.19683v1#S3.SS1 — 3.1. Threat Model | https://arxiv.org/html/2607.19683v1#S5 — 5. Experiments and Results; https://arxiv.org/html/2607.19683v1#S5.SS1 — 5.1. Experimental Setup | https://arxiv.org/html/2607.19683v1#S9 — 9. Conclusion, Limitations, and Future Work; https://arxiv.org/html/2607.19683v1#S3 — 3. Threat Model and Challenges | Exact v1 links https://github.com/Ye-ze-yu/GhostPrompt, https://huggingface.co/ProtectAI/deberta-v3-base-prompt-injection-v2, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19683 | complete |
| SF-2026-ARXIV-2607-19686 | RP-184b2070bdc2c0c1 | deep | arXiv:2607.19686v1 | SRC-ARXIV@arXiv:2607.19686v1 | https://arxiv.org/html/2607.19686v1#S3 — 3 Methodology; https://arxiv.org/html/2607.19686v1#S2.SS1 — 2.1 Discrete Diffusion Models | https://arxiv.org/html/2607.19686v1#A3 — Appendix C Experiment Settings and Additional Results; https://arxiv.org/html/2607.19686v1#A2 — Appendix B Theoretical Analysis of Discrete Consistency Distillation | https://arxiv.org/html/2607.19686v1#S5 — 5 Discussion | Exact v1 links https://github.com/ML-GSAI/LLaDA, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19686 | complete |
| SF-2026-ARXIV-2607-19691 | RP-36f6d2c266791e9c | standard | arXiv:2607.19691v1 | SRC-ARXIV@arXiv:2607.19691v1 | https://arxiv.org/html/2607.19691v1#S4 — 4 Methodology; https://arxiv.org/html/2607.19691v1#A1 — Appendix A Implementation Details | https://arxiv.org/html/2607.19691v1#A1.SS5 — A.5 Inference and Evaluation; https://arxiv.org/html/2607.19691v1#A4 — Appendix D Latent Geometry Analysis | https://arxiv.org/html/2607.19691v1#S8 — 8 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19691 | complete |
| SF-2026-ARXIV-2607-19695 | RP-8709a105707d054c | standard | arXiv:2607.19695v1 | SRC-ARXIV@arXiv:2607.19695v1 | https://arxiv.org/html/2607.19695v1#A1.SS7 — A.7 System Setup and Runtime; https://arxiv.org/html/2607.19695v1#A2.SS3 — B.3 Outdoor Terrain and Road Modeling | https://arxiv.org/html/2607.19695v1#A1 — Appendix A Benchmark Interface and Evaluation Protocol; https://arxiv.org/html/2607.19695v1#S3.SS3 — 3.3 Benchmark and Evaluation | https://arxiv.org/html/2607.19695v1#S5 — 5 Conclusion | Exact v1 links https://github.com/isaac-sim/IsaacSim, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19695 | complete |
| SF-2026-ARXIV-2607-19701 | RP-4fca6ab3a03a06f0 | standard | arXiv:2607.19701v1 | SRC-ARXIV@arXiv:2607.19701v1 | https://arxiv.org/html/2607.19701v1#S3 — 3. Methodology; https://arxiv.org/html/2607.19701v1#S3.SS4 — 3.4. Systemic Generation Workflow | https://arxiv.org/html/2607.19701v1#S4.SS2 — 4.2. Main Results and Analysis; https://arxiv.org/html/2607.19701v1#S4 — 4. Experiments | https://arxiv.org/html/2607.19701v1#S5 — 5. Conclusion | Exact v1 links https://github.com/JoFrc/SafeGen, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19701 | complete |
| SF-2026-ARXIV-2607-19704 | RP-06d835aa7701ca12 | deep | arXiv:2607.19704v1 | SRC-ARXIV@arXiv:2607.19704v1 | https://arxiv.org/html/2607.19704v1#A1 — Appendix A Design Considerations and Technical Details; https://arxiv.org/html/2607.19704v1#S3 — 3 Method | https://arxiv.org/html/2607.19704v1#A6 — Appendix F Additional Experiment Results; https://arxiv.org/html/2607.19704v1#A5 — Appendix E Computational Complexity Analysis | https://arxiv.org/html/2607.19704v1#S6 — 6 Conclusion | Exact v1 links https://huggingface.co/datasets/HuggingFaceTB/cosmopedia, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19704 | complete |
| SF-2026-ARXIV-2607-19712 | RP-f4950aec51fc9eb8 | deep | arXiv:2607.19712v1 | SRC-ARXIV@arXiv:2607.19712v1 | https://arxiv.org/html/2607.19712v1#S3 — 3 Methodology; https://arxiv.org/html/2607.19712v1#S3.SS4 — 3.4 Statistical Method | https://arxiv.org/html/2607.19712v1#S4 — 4 Results | https://arxiv.org/html/2607.19712v1#S3.SS7 — 3.7 Hardware and Limitations; https://arxiv.org/html/2607.19712v1#S5 — 5 Discussion | Exact v1 links https://github.com/vishnup22/reward-model-benchmarks, https://github.com/onnx/onnx, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19712 | complete |
| SF-2026-ARXIV-2607-19719 | RP-a3472d01fc0077eb | deep | arXiv:2607.19719v1 | SRC-ARXIV@arXiv:2607.19719v1 | https://arxiv.org/html/2607.19719v1#S4 — IV Method; https://arxiv.org/html/2607.19719v1#S2.SS1 — II-A Latent World Models | https://arxiv.org/html/2607.19719v1#S6 — VI Experiments and Analysis; https://arxiv.org/html/2607.19719v1#A0.SS1 — -A DMC Proprioceptive Benchmark Details | https://arxiv.org/html/2607.19719v1#S7 — VII Discussion; https://arxiv.org/html/2607.19719v1#S8 — VIII Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19719 | complete |
| SF-2026-ARXIV-2607-19747 | RP-573572bddcc3d940 | standard | arXiv:2607.19747v1 | SRC-ARXIV@arXiv:2607.19747v1 | https://arxiv.org/html/2607.19747v1#A1 — Appendix A Implementation Details of SetwiseEvalKit; https://arxiv.org/html/2607.19747v1#A4 — Appendix D Model Prompts | https://arxiv.org/html/2607.19747v1#A2 — Appendix B More Experimental Results; https://arxiv.org/html/2607.19747v1#S4.SS2 — 4.2 Results on Rubric-Oriented Evaluation | https://arxiv.org/html/2607.19747v1#S6 — 6 Conclusion and Limitation | Exact v1 links https://github.com/Rubric4Setwise/Rubric4Setwise, https://huggingface.co/collections/placeholder, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19747 | complete |
| SF-2026-ARXIV-2607-19749 | RP-2d0dd0fb5a615929 | deep | arXiv:2607.19749v1 | SRC-ARXIV@arXiv:2607.19749v1 | https://arxiv.org/html/2607.19749v1#S4.SS3 — 4.3 The world model retains everything we can measure; https://arxiv.org/html/2607.19749v1#S5 — 5 Recovery from the World Model Alone | https://arxiv.org/html/2607.19749v1#S3 — 3 Experimental Setup; https://arxiv.org/html/2607.19749v1#S6.SS1 — 6.1 Four-task result | https://arxiv.org/html/2607.19749v1#S10 — 10 Conclusion; https://arxiv.org/html/2607.19749v1#S9 — 9 Limitations | Exact v1 links https://github.com/gurpnijjer/dream-rehearsal, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19749 | complete |
| SF-2026-ARXIV-2607-19771 | RP-3e1cdf65e9f00352 | deep | arXiv:2607.19771v1 | SRC-ARXIV@arXiv:2607.19771v1 | https://arxiv.org/html/2607.19771v1#S2.SS3 — 2.3 Result: the three methods have equal val loss; https://arxiv.org/html/2607.19771v1#S3.SS3 — 3.3 Core result: isotropy across the three methods | https://arxiv.org/html/2607.19771v1#S2.SS2 — 2.2 Experimental setup; https://arxiv.org/html/2607.19771v1#S2.SS3 — 2.3 Result: the three methods have equal val loss | https://arxiv.org/html/2607.19771v1#S3.SS4 — 3.4 L0 / L5 load balancing: a phase transition and LFB failure; https://arxiv.org/html/2607.19771v1#S4.SS2 — 4.2 The bf16 FA failure mechanism (from the reference paper) | Exact v1 links https://github.com/karpathy/nanoGPT, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19771 | complete |
| SF-2026-ARXIV-2607-19774 | RP-a373bb93fd7ea0e4 | standard | arXiv:2607.19774v1 | SRC-ARXIV@arXiv:2607.19774v1 | https://arxiv.org/html/2607.19774v1#S3 — III Method; https://arxiv.org/html/2607.19774v1#S3.SS2 — III-B Overall Architecture | https://arxiv.org/html/2607.19774v1#S4 — IV Experiments; https://arxiv.org/html/2607.19774v1#S4.SS1 — IV-A Experimental Setup | https://arxiv.org/html/2607.19774v1#S5 — V Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19774 | complete |
| SF-2026-ARXIV-2607-19790 | RP-d4491cca41d5b61c | standard | arXiv:2607.19790v1 | SRC-ARXIV@arXiv:2607.19790v1 | https://arxiv.org/html/2607.19790v1#S1 — 1 Introduction; https://arxiv.org/html/2607.19790v1#S2 — 2 Related Work | https://arxiv.org/html/2607.19790v1#A2 — Appendix B Experimental Details; https://arxiv.org/html/2607.19790v1#A2.SS2 — B.2 External evaluation suite | https://arxiv.org/html/2607.19790v1#S7 — 7 Limitations and Future Work; https://arxiv.org/html/2607.19790v1#S8 — 8 Conclusion | Exact v1 links https://github.com/embodiedreasoning/ERQA, https://huggingface.co/datasets/xai-org/RealworldQA, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19790 | complete |
| SF-2026-ARXIV-2607-19793 | RP-aebba8f6f9ee8ae0 | standard | arXiv:2607.19793v1 | SRC-ARXIV@arXiv:2607.19793v1 | https://arxiv.org/html/2607.19793v1#S2 — 2. Method | https://arxiv.org/html/2607.19793v1#S3 — 3. Experiments; https://arxiv.org/html/2607.19793v1#S3.SS1 — 3.1. Experimental Setup | https://arxiv.org/html/2607.19793v1#S2.SS2 — 2.2. Taxonomy of Silent Failures; https://arxiv.org/html/2607.19793v1#S4 — 4. Conclusion | Exact v1 links https://github.com/DingWu1021/silent-failures-multimodal-agentic-search, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19793 | complete |
| SF-2026-ARXIV-2607-19806 | RP-dd00fa7d5550804c | standard | arXiv:2607.19806v1 | SRC-ARXIV@arXiv:2607.19806v1 | https://arxiv.org/html/2607.19806v1#S3 — 3 Methodology; https://arxiv.org/html/2607.19806v1#S4.SS1 — 4.1 Models and Baselines | https://arxiv.org/html/2607.19806v1#A2 — Appendix B Ablation Studies; https://arxiv.org/html/2607.19806v1#A3 — Appendix C Over-Refusal Evaluation Details | https://arxiv.org/html/2607.19806v1#S6 — 6 Conclusion and Future Directions; https://arxiv.org/html/2607.19806v1#S5 — 5 Limitations | Exact v1 links https://www.lesswrong.com/posts/CbSEZSpjdpnvBcEvc/i-found-greater-than-800-orthogonal-write-code-steering, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19806 | complete |
| SF-2026-ARXIV-2607-19809 | RP-dca22b9d81ae7dc6 | standard | arXiv:2607.19809v1 | SRC-ARXIV@arXiv:2607.19809v1 | https://arxiv.org/html/2607.19809v1#Pt0.A1 — Appendix 0.A Algorithms; https://arxiv.org/html/2607.19809v1#S2.SS2 — 2.2 World Model | https://arxiv.org/html/2607.19809v1#S3 — 3 Experiments; https://arxiv.org/html/2607.19809v1#S3.SS3 — 3.3 Results | https://arxiv.org/html/2607.19809v1#S4 — 4 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19809 | complete |
| SF-2026-ARXIV-2607-19824 | RP-4c567777d867e063 | standard | arXiv:2607.19824v1 | SRC-ARXIV@arXiv:2607.19824v1 | https://arxiv.org/html/2607.19824v1#Sx5 — Method; https://arxiv.org/html/2607.19824v1#A1 — Appendix A Reward Computation Algorithm | https://arxiv.org/html/2607.19824v1#A2.SSx3 — Evaluation Benchmarks; https://arxiv.org/html/2607.19824v1#A2 — Appendix B Experimental Details | https://arxiv.org/html/2607.19824v1#Sx7 — Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19824 | complete |
| SF-2026-ARXIV-2607-19827 | RP-cf604e17b77aa9da | deep | arXiv:2607.19827v1 | SRC-ARXIV@arXiv:2607.19827v1 | https://arxiv.org/html/2607.19827v1#S2 — II Approach; https://arxiv.org/html/2607.19827v1#S2.SS1 — II-A System Overview | https://arxiv.org/html/2607.19827v1#S1 — I Introduction; https://arxiv.org/html/2607.19827v1#S2 — II Approach | https://arxiv.org/html/2607.19827v1#S4 — IV Discussion; https://arxiv.org/html/2607.19827v1#S5 — V Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19827 | complete |
| SF-2026-ARXIV-2607-19829 | RP-196c86085697ee46 | deep | arXiv:2607.19829v1 | SRC-ARXIV@arXiv:2607.19829v1 | https://arxiv.org/html/2607.19829v1#S3 — 3 THE DARWIN FRAMEWORK | https://arxiv.org/html/2607.19829v1#S4 — 4 Experiments; https://arxiv.org/html/2607.19829v1#S4.SS1 — 4.1 Experimental Setup | https://arxiv.org/html/2607.19829v1#S1 — 1 Introduction; https://arxiv.org/html/2607.19829v1#S2 — 2 Related Work | Exact v1 links https://huggingface.co/datasets/llm-semantic-router/jailbreak-detection-dataset, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19829 | complete |
| SF-2026-ARXIV-2607-19837 | RP-2fc3374ea93306c0 | deep | arXiv:2607.19837v1 | SRC-ARXIV@arXiv:2607.19837v1 | https://arxiv.org/html/2607.19837v1#S3 — III Threat Model and System Assumptions; https://arxiv.org/html/2607.19837v1#S5 — V The KYA Framework | https://arxiv.org/html/2607.19837v1#A1 — Appendix A Ablation Study: Full Curves; https://arxiv.org/html/2607.19837v1#A2.SS6 — B-F Per-Cell Observation Behind the Tier Result | https://arxiv.org/html/2607.19837v1#S3 — III Threat Model and System Assumptions; https://arxiv.org/html/2607.19837v1#S7 — VII Conclusion | Exact v1 links https://owasp.org/www-project-top-10-for-large-language-model-applications/, https://huggingface.co/ProtectAI/deberta-v3-base-prompt-injection-v2, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19837 | complete |
| SF-2026-ARXIV-2607-19848 | RP-24ae0114f6a5796c | standard | arXiv:2607.19848v1 | SRC-ARXIV@arXiv:2607.19848v1 | https://arxiv.org/html/2607.19848v1#S3 — 3 System Overview | https://arxiv.org/html/2607.19848v1#A4 — Appendix D Details of Heuristic Evaluation; https://arxiv.org/html/2607.19848v1#S4 — 4 Evaluation | https://arxiv.org/html/2607.19848v1#S6 — 6 Conclusion | Exact v1 links https://github.com/nlpsoc/emb-diversity/, https://github.com/nlpsoc/emb-diversity/blob/main/optimization_doc.md, https://huggingface.co/AnnaWegmann/Style-Embedding; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19848 | complete |
| SF-2026-ARXIV-2607-19850 | RP-fac5055cfbf80e4d | standard | arXiv:2607.19850v1 | SRC-ARXIV@arXiv:2607.19850v1 | https://arxiv.org/html/2607.19850v1#S3 — III Method | https://arxiv.org/html/2607.19850v1#S4 — IV Experiment; https://arxiv.org/html/2607.19850v1#S4.SS1 — IV-A Experiment Settings | https://arxiv.org/html/2607.19850v1#S5 — V CONCLUSIONS | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19850 | complete |
| SF-2026-ARXIV-2607-19857 | RP-08f9be8f0dd50c62 | deep | arXiv:2607.19857v1 | SRC-ARXIV@arXiv:2607.19857v1 | https://arxiv.org/html/2607.19857v1#S4 — IV SkyAnchor Method; https://arxiv.org/html/2607.19857v1#S4.SS1 — IV-A Model Overview | https://arxiv.org/html/2607.19857v1#S5 — V Experiment; https://arxiv.org/html/2607.19857v1#S5.SS1 — V-A Experimental Setup | https://arxiv.org/html/2607.19857v1#S6 — VI Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19857 | complete |
| SF-2026-ARXIV-2607-19865 | RP-13cf625e4b02d630 | deep | arXiv:2607.19865v1 | SRC-ARXIV@arXiv:2607.19865v1 | https://arxiv.org/html/2607.19865v1#S3.SS1 — 3.1 Taxonomy Design; https://arxiv.org/html/2607.19865v1#A8 — Appendix H Model Serving Details | https://arxiv.org/html/2607.19865v1#A5 — Appendix E Full Skill-Injection Results; https://arxiv.org/html/2607.19865v1#A6 — Appendix F Verifier Fidelity Evaluation | https://arxiv.org/html/2607.19865v1#Sx1 — Conclusion; https://arxiv.org/html/2607.19865v1#Sx2 — Limitations | Exact v1 links https://github.com/icip-cas/DocOps, https://github.com/anthropics/skills, https://github.com/anthropics/claude-code; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19865 | complete |
| SF-2026-ARXIV-2607-19876 | RP-60a920ec437d8d2d | deep | arXiv:2607.19876v1 | SRC-ARXIV@arXiv:2607.19876v1 | https://arxiv.org/html/2607.19876v1#S3 — 3 Methodology; https://arxiv.org/html/2607.19876v1#S3.SS3 — 3.3 Four-Suite Benchmark Design | https://arxiv.org/html/2607.19876v1#S2.SS2 — 2.2 Benchmarks for Embodied World Models; https://arxiv.org/html/2607.19876v1#S2.SS3 — 2.3 Evaluation Metrics: From Pixels to 3D Kinematics | https://arxiv.org/html/2607.19876v1#S5 — 5 Discussion and Limitations; https://arxiv.org/html/2607.19876v1#S6 — 6 Conclusion | Exact v1 links https://github.com/minecraft-zzz/KineBench, https://huggingface.co/datasets/Zorkzak/KineBenchDatasets, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19876 | complete |
| SF-2026-ARXIV-2607-19880 | RP-7bd829cb4d43e1c4 | standard | arXiv:2607.19880v1 | SRC-ARXIV@arXiv:2607.19880v1 | https://arxiv.org/html/2607.19880v1#A1.SS5 — A.5. Model Architecture and Ablation Details; https://arxiv.org/html/2607.19880v1#S3 — 3. Method | https://arxiv.org/html/2607.19880v1#A1.SS4 — A.4. Evaluation Environment Setup; https://arxiv.org/html/2607.19880v1#A1.SS5 — A.5. Model Architecture and Ablation Details | https://arxiv.org/html/2607.19880v1#S5 — 5. Conclusion and Limitation | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19880 | complete |
| SF-2026-ARXIV-2607-19894 | RP-1f008a20db47aed8 | standard | arXiv:2607.19894v1 | SRC-ARXIV@arXiv:2607.19894v1 | https://arxiv.org/html/2607.19894v1#S3.SS2 — 3.2. Observing Model Behaviors; https://arxiv.org/html/2607.19894v1#S4 — 4. Threat Model | https://arxiv.org/html/2607.19894v1#A2 — Appendix B Evaluation; https://arxiv.org/html/2607.19894v1#A2.SS1 — B.1. Experimental Setup | https://arxiv.org/html/2607.19894v1#S10 — 10. Conclusion; https://arxiv.org/html/2607.19894v1#S4 — 4. Threat Model | Exact v1 links https://github.com/tatsu-lab/stanford_alpaca, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19894 | complete |
| SF-2026-ARXIV-2607-19899 | RP-5732e1a023269a49 | standard | arXiv:2607.19899v1 | SRC-ARXIV@arXiv:2607.19899v1 | https://arxiv.org/html/2607.19899v1#S4 — 4 ARAT Architecture; https://arxiv.org/html/2607.19899v1#S6.SS4 — 6.4 Escalation Model and Routing Signals | https://arxiv.org/html/2607.19899v1#S5 — 5 Experimental Setup; https://arxiv.org/html/2607.19899v1#S6 — 6 Results | https://arxiv.org/html/2607.19899v1#S7 — 7 Discussion; https://arxiv.org/html/2607.19899v1#S8 — 8 Limitations | Exact v1 links https://github.com/McDonnelletal/arat-paper, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19899 | complete |
| SF-2026-ARXIV-2607-19910 | RP-4a1b039014d2f478 | standard | arXiv:2607.19910v1 | SRC-ARXIV@arXiv:2607.19910v1 | https://arxiv.org/html/2607.19910v1#S2.SS3 — 2.3 Coordinated Multi-View Interface Design and Benchmarking; https://arxiv.org/html/2607.19910v1#S4 — 4 Evaluation Methodology | https://arxiv.org/html/2607.19910v1#S5 — 5 Experimental Results; https://arxiv.org/html/2607.19910v1#S2.SS3 — 2.3 Coordinated Multi-View Interface Design and Benchmarking | https://arxiv.org/html/2607.19910v1#S6.SS2 — 6.2 Limitations and Future Directions; https://arxiv.org/html/2607.19910v1#S6 — 6 Discussion | Exact v1 links https://aclanthology.org/2023.acl-demo.11/, https://dx.doi.org/10.18653/v1/2023.acl-demo.11, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19910 | complete |
| SF-2026-ARXIV-2607-19913 | RP-fc073e3cc49f0cb4 | deep | arXiv:2607.19913v1 | SRC-ARXIV@arXiv:2607.19913v1 | https://arxiv.org/html/2607.19913v1#Sx2 — Method; https://arxiv.org/html/2607.19913v1#A1.SSx2 — Additional Implementation Details | https://arxiv.org/html/2607.19913v1#A1 — Appendix A Experimental Setup; https://arxiv.org/html/2607.19913v1#A1.SSx1 — Benchmark Configuration | https://arxiv.org/html/2607.19913v1#Sx6 — Conclusion; https://arxiv.org/html/2607.19913v1#Sx7 — Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19913 | complete |
| SF-2026-ARXIV-2607-19919 | RP-d59fbeac106302d4 | standard | arXiv:2607.19919v1 | SRC-ARXIV@arXiv:2607.19919v1 | https://arxiv.org/html/2607.19919v1#S1 — 1 Introduction; https://arxiv.org/html/2607.19919v1#S2 — 2 Preliminaries | https://arxiv.org/html/2607.19919v1#A3 — Appendix C Experiment Settings; https://arxiv.org/html/2607.19919v1#A4 — Appendix D Additional Results | https://arxiv.org/html/2607.19919v1#S5 — 5 Limitations; https://arxiv.org/html/2607.19919v1#S6 — 6 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19919 | complete |
| SF-2026-ARXIV-2607-19922 | RP-b20fbbb45076c45c | deep | arXiv:2607.19922v1 | SRC-ARXIV@arXiv:2607.19922v1 | https://arxiv.org/html/2607.19922v1#S4 — 4. Methodology; https://arxiv.org/html/2607.19922v1#S4.SS2 — 4.2. NUMA Architecture Topology | https://arxiv.org/html/2607.19922v1#S5 — 5. Evaluation; https://arxiv.org/html/2607.19922v1#S5.SS1 — 5.1. Experimental Setup | https://arxiv.org/html/2607.19922v1#S6 — 6. Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19922 | complete |
| SF-2026-ARXIV-2607-19932 | RP-74b9d3523e46b24d | deep | arXiv:2607.19932v1 | SRC-ARXIV@arXiv:2607.19932v1 | https://arxiv.org/html/2607.19932v1#A5 — Appendix E Other Efficient-reasoning Methods; https://arxiv.org/html/2607.19932v1#S3 — 3. Method | https://arxiv.org/html/2607.19932v1#S4.SS3 — 4.3. Ablation and Analysis; https://arxiv.org/html/2607.19932v1#A3 — Appendix C Evaluation Configuration | https://arxiv.org/html/2607.19932v1#S5 — 5. Limitations; https://arxiv.org/html/2607.19932v1#S6 — 6. Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19932 | complete |
| SF-2026-ARXIV-2607-19949 | RP-57d21bb15452302d | standard | arXiv:2607.19949v1 | SRC-ARXIV@arXiv:2607.19949v1 | https://arxiv.org/html/2607.19949v1#S3 — III The SenWorld Method; https://arxiv.org/html/2607.19949v1#S3.SS1 — III-A Overview and Method Contract | https://arxiv.org/html/2607.19949v1#S4 — IV Evaluation Setup; https://arxiv.org/html/2607.19949v1#S4.SS3 — IV-C RQ1: Benchmark Comparison | https://arxiv.org/html/2607.19949v1#S6 — VI Conclusion and Future Work | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19949 | complete |
| SF-2026-ARXIV-2607-19957 | RP-33c7b00cf9126232 | deep | arXiv:2607.19957v1 | SRC-ARXIV@arXiv:2607.19957v1 | https://arxiv.org/html/2607.19957v1#S4.SS1 — 4.1 Threat Model | https://arxiv.org/html/2607.19957v1#S6 — 6 Experimental Setup; https://arxiv.org/html/2607.19957v1#S7 — 7 Experiment | https://arxiv.org/html/2607.19957v1#S8 — 8 Limitations and Discussion; https://arxiv.org/html/2607.19957v1#S4.SS1 — 4.1 Threat Model | Exact v1 links https://github.com/YichiCS/KV-Cache-Hijack, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19957 | complete |
| SF-2026-ARXIV-2607-19962 | RP-e91963f38fda0ff5 | standard | arXiv:2607.19962v1 | SRC-ARXIV@arXiv:2607.19962v1 | https://arxiv.org/html/2607.19962v1#S3 — 3 Method | https://arxiv.org/html/2607.19962v1#S4 — 4 Experiments; https://arxiv.org/html/2607.19962v1#S4.SS1 — 4.1 Experimental Setups | https://arxiv.org/html/2607.19962v1#S5 — 5 Conclusion and Future Work | Exact v1 links https://huggingface.co/datasets/math-ai/aime25, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19962 | complete |
| SF-2026-ARXIV-2607-19971 | RP-23f4d0ec7ef17f3b | standard | arXiv:2607.19971v1 | SRC-ARXIV@arXiv:2607.19971v1 | https://arxiv.org/html/2607.19971v1#S11.SS1 — 11.1 Skill Conflict in Other Architecture; https://arxiv.org/html/2607.19971v1#S3 — 3 Methods | https://arxiv.org/html/2607.19971v1#S4.SS2 — 4.2 Experimental Results; https://arxiv.org/html/2607.19971v1#S10 — 10 Qualitative Results | https://arxiv.org/html/2607.19971v1#S15 — 15 Future Direction; https://arxiv.org/html/2607.19971v1#S5 — 5 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19971 | complete |
| SF-2026-ARXIV-2607-19985 | RP-7fe3e0a865078381 | standard | arXiv:2607.19985v1 | SRC-ARXIV@arXiv:2607.19985v1 | https://arxiv.org/html/2607.19985v1#S3 — III PROPOSED METHOD | https://arxiv.org/html/2607.19985v1#S4 — IV EXPERIMENTS; https://arxiv.org/html/2607.19985v1#S4.SS1 — IV-A Experimental Setup | https://arxiv.org/html/2607.19985v1#S5 — V CONCLUSION | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19985 | complete |
| SF-2026-ARXIV-2607-19996 | RP-d8da81302ba12afb | standard | arXiv:2607.19996v1 | SRC-ARXIV@arXiv:2607.19996v1 | https://arxiv.org/html/2607.19996v1#S4 — 4 Methods; https://arxiv.org/html/2607.19996v1#S3.SS1 — 3.1 Logic Programs and Stable Model Semantics | https://arxiv.org/html/2607.19996v1#S5 — 5 Experiments; https://arxiv.org/html/2607.19996v1#S6 — 6 Discussion on Experiments | https://arxiv.org/html/2607.19996v1#S7 — 7 Conclusions and Future Work; https://arxiv.org/html/2607.19996v1#S6 — 6 Discussion on Experiments | Exact v1 links https://github.com/azreasoners/lpmln, https://github.com/dig-team/amie, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19996 | complete |
| SF-2026-ARXIV-2607-20064 | RP-0da8bb7a69e39feb | deep | arXiv:2607.20064v1 | SRC-ARXIV@arXiv:2607.20064v1 | https://arxiv.org/html/2607.20064v1#A2.SS1 — B.1 System Prompt: (PRO-LONG); https://arxiv.org/html/2607.20064v1#A2.SS2 — B.2 System Prompt: No-Log | https://arxiv.org/html/2607.20064v1#S3 — 3 Main Results; https://arxiv.org/html/2607.20064v1#S3.SS1 — 3.1 Benchmark Performance | https://arxiv.org/html/2607.20064v1#S5 — 5 Conclusion | Exact v1 links https://github.com/alexisfox7/PRO-LONG, https://github.com/arcprize/ARC-AGI-3-Agents, https://github.com/DriesSmit/ARC3-solution; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20064 | complete |
| SF-2026-ARXIV-2607-20083 | RP-90064b0fb6c88be9 | deep | arXiv:2607.20083v1 | SRC-ARXIV@arXiv:2607.20083v1 | https://arxiv.org/html/2607.20083v1#S3 — 3 Methodology; https://arxiv.org/html/2607.20083v1#A1 — Appendix A DynamicRubric Training Algorithm | https://arxiv.org/html/2607.20083v1#A3.SS1 — C.1 Benchmark Details for Evaluator Evaluation; https://arxiv.org/html/2607.20083v1#A3.SS2 — C.2 Benchmark Details for Open-Ended Generation Tasks Evaluation | https://arxiv.org/html/2607.20083v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.20083v1#Sx1 — Limitations | Exact v1 links https://github.com/huggingface/math-verify, https://github.com/tatsu-lab/alpaca_eval, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20083 | complete |
| SF-2026-ARXIV-2607-20090 | RP-23027bd6c6a0c863 | deep | arXiv:2607.20090v1 | SRC-ARXIV@arXiv:2607.20090v1 | https://arxiv.org/html/2607.20090v1#S3 — 3 Methodology; https://arxiv.org/html/2607.20090v1#S6.SS2 — 6.2 Large Language Models as Agents | https://arxiv.org/html/2607.20090v1#S5 — 5 Results and Analysis; https://arxiv.org/html/2607.20090v1#S4 — 4 Experimental Setup | https://arxiv.org/html/2607.20090v1#S7 — 7 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20090 | complete |
| SF-2026-ARXIV-2607-20110 | RP-10768e5fd6180efb | standard | arXiv:2607.20110v1 | SRC-ARXIV@arXiv:2607.20110v1 | https://arxiv.org/html/2607.20110v1#S3 — III System Overview; https://arxiv.org/html/2607.20110v1#S4.SS1 — IV-A Policy Architecture | https://arxiv.org/html/2607.20110v1#S6.SS2 — VI-B Ablation and Analysis; https://arxiv.org/html/2607.20110v1#S6 — VI Experiments | https://arxiv.org/html/2607.20110v1#S6.SS4 — VI-D Limitations; https://arxiv.org/html/2607.20110v1#S7 — VII Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20110 | complete |
| SF-2026-ARXIV-2607-20120 | RP-71d94857c3856809 | standard | arXiv:2607.20120v1 | SRC-ARXIV@arXiv:2607.20120v1 | https://arxiv.org/html/2607.20120v1#S2.SS1 — 2.1 Precision-Oriented Approaches; https://arxiv.org/html/2607.20120v1#S2.SS3 — 2.3 Memory- and Communication-Centric Approaches | https://arxiv.org/html/2607.20120v1#S4 — 4 Experimental Setup; https://arxiv.org/html/2607.20120v1#S4.SS2 — 4.2 Experimental Environment | https://arxiv.org/html/2607.20120v1#S7 — 7 Conclusion and Future Work | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20120 | complete |
| SF-2026-ARXIV-2607-20121 | RP-96d05319d0f09981 | deep | arXiv:2607.20121v1 | SRC-ARXIV@arXiv:2607.20121v1 | https://arxiv.org/html/2607.20121v1#S4.SS2 — 4.2 RQ1. How Robust Are Current Agent Systems to Real-World Risky Skills? | https://arxiv.org/html/2607.20121v1#A2 — Appendix B Benchmark Construction Details; https://arxiv.org/html/2607.20121v1#A2.SS6 — B.6 Benchmark Statistics | https://arxiv.org/html/2607.20121v1#S5 — 5 Conclusion | Exact v1 links https://github.com/Miaow-Lab/OpenSkillRisk, https://code.claude.com/docs/en/overview, https://code.claude.com/docs/en/permissions; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20121 | complete |
| SF-2026-ARXIV-2607-20125 | RP-7b9d55cc5d94a406 | deep | arXiv:2607.20125v1 | SRC-ARXIV@arXiv:2607.20125v1 | https://arxiv.org/html/2607.20125v1#S1 — 1 Introduction; https://arxiv.org/html/2607.20125v1#S2 — 2 Related Work | https://arxiv.org/html/2607.20125v1#A6 — Appendix F Additional Qualitative Results; https://arxiv.org/html/2607.20125v1#S5 — 5 Experiments | https://arxiv.org/html/2607.20125v1#S6 — 6 Conclusion | Exact v1 links https://github.com/sjlgaga/HeadCast, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20125 | complete |
| SF-2026-ARXIV-2607-20129 | RP-b08bd092342d4e8b | deep | arXiv:2607.20129v1 | SRC-ARXIV@arXiv:2607.20129v1 | https://arxiv.org/html/2607.20129v1#A3 — Appendix C Methodological relation to the prior preprint; https://arxiv.org/html/2607.20129v1#S4 — 4 Method | https://arxiv.org/html/2607.20129v1#S7 — 7 Ablations and Diagnostic Analysis; https://arxiv.org/html/2607.20129v1#A4 — Appendix D Additional experiments for component attribution and generalization | https://arxiv.org/html/2607.20129v1#S8 — 8 Limitations; https://arxiv.org/html/2607.20129v1#S9 — 9 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20129 | complete |
| SF-2026-ARXIV-2607-20145 | RP-6c62666ce99a07a3 | deep | arXiv:2607.20145v1 | SRC-ARXIV@arXiv:2607.20145v1 | https://arxiv.org/html/2607.20145v1#A3 — Appendix C Solver-Verified OR-CPT Data Synthesis: Engine Design and Illustrative Cases; https://arxiv.org/html/2607.20145v1#A3.SS2 — C.2 End-to-end engine architecture | https://arxiv.org/html/2607.20145v1#S4 — 4 Experimental Results; https://arxiv.org/html/2607.20145v1#A4 — Appendix D CPT–SFT–Deployment–Evaluation Provenance | https://arxiv.org/html/2607.20145v1#S5 — 5 Conclusion, Limitations, and Future Directions | Exact v1 links https://github.com/SLAI-AITP/Deepseek-OR, https://huggingface.co/datasets/albertge/synthetic-orqa, https://github.com/Gurobi/modeling-examples; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20145 | complete |
| SF-2026-ARXIV-2607-20146 | RP-32868f7ac9023a71 | standard | arXiv:2607.20146v1 | SRC-ARXIV@arXiv:2607.20146v1 | https://arxiv.org/html/2607.20146v1#A3 — Appendix C Method - Detailed; https://arxiv.org/html/2607.20146v1#S4 — 4 Method | https://arxiv.org/html/2607.20146v1#A10 — Appendix J Ablation Heatmaps: All Three Experiments; https://arxiv.org/html/2607.20146v1#A5 — Appendix E Full Clustering Results | https://arxiv.org/html/2607.20146v1#S6 — 6 Discussion; https://arxiv.org/html/2607.20146v1#S7 — 7 Conclusion | Exact v1 links https://github.com/TransformerLensOrg/TransformerLens, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20146 | complete |
| SF-2026-ARXIV-2607-20166 | RP-75e95fd8946bb991 | standard | arXiv:2607.20166v1 | SRC-ARXIV@arXiv:2607.20166v1 | https://arxiv.org/html/2607.20166v1#S2 — 2 Audio-Zero: A Label-Free Self-Evolution Framework; https://arxiv.org/html/2607.20166v1#A1.SS1 — A.1 Additional Implementation Details | https://arxiv.org/html/2607.20166v1#S3 — 3 Experiments and Analysis; https://arxiv.org/html/2607.20166v1#A2 — Appendix B Evaluation Protocol | https://arxiv.org/html/2607.20166v1#S5 — 5 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20166 | complete |
| SF-2026-ARXIV-2607-20174 | RP-7762f20e3d93545d | standard | arXiv:2607.20174v1 | SRC-ARXIV@arXiv:2607.20174v1 | https://arxiv.org/html/2607.20174v1#S4 — IV Method | https://arxiv.org/html/2607.20174v1#S5 — V Experiments; https://arxiv.org/html/2607.20174v1#S5.SS1 — V-A Experimental Settings | https://arxiv.org/html/2607.20174v1#S5.SS3 — V-C Ablation Studies and Discussion; https://arxiv.org/html/2607.20174v1#S6 — VI Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20174 | complete |
| SF-2026-ARXIV-2607-20192 | RP-5cc33b232c75b1f3 | standard | arXiv:2607.20192v1 | SRC-ARXIV@arXiv:2607.20192v1 | https://arxiv.org/html/2607.20192v1#S3.SS1 — 3.1 Gradient Method Baseline; https://arxiv.org/html/2607.20192v1#S3.SS2 — 3.2 Newton Method with Gradient Regularization | https://arxiv.org/html/2607.20192v1#S1 — 1 Introduction; https://arxiv.org/html/2607.20192v1#S1.SS1 — 1.1 Certified Unlearning and Optimization | https://arxiv.org/html/2607.20192v1#S1 — 1 Introduction; https://arxiv.org/html/2607.20192v1#S1.SS1 — 1.1 Certified Unlearning and Optimization | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20192 | complete |
| SF-2026-ARXIV-2607-20205 | RP-dbfe031dce11446f | standard | arXiv:2607.20205v1 | SRC-ARXIV@arXiv:2607.20205v1 | https://arxiv.org/html/2607.20205v1#S4.SS3 — 4.3 The StatLoRA Algorithm | https://arxiv.org/html/2607.20205v1#A2.SS1 — B.1 Main Results; https://arxiv.org/html/2607.20205v1#A3.SS1 — C.1 Main Results | https://arxiv.org/html/2607.20205v1#S6 — 6 Conclusion and Discussion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20205 | complete |
| SF-2026-ARXIV-2607-20214 | RP-2009d84a7bd2d7d5 | deep | arXiv:2607.20214v1 | SRC-ARXIV@arXiv:2607.20214v1 | https://arxiv.org/html/2607.20214v1#S3 — 3 Methodology; https://arxiv.org/html/2607.20214v1#A1 — Appendix A Branch Algorithms for ELSAA | https://arxiv.org/html/2607.20214v1#A4 — Appendix D Experiment Hyperparameters; https://arxiv.org/html/2607.20214v1#S5 — 5 Experimental Setup | https://arxiv.org/html/2607.20214v1#A2.SS3 — B.3 Hall deficiency and weighted Hall failure; https://arxiv.org/html/2607.20214v1#S7 — 7 Results and Discussion | Exact v1 links https://github.com/mahdiheidari721/ELSAA, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20214 | complete |
| SF-2026-ARXIV-2607-20220 | RP-a3c457c1f3d67113 | deep | arXiv:2607.20220v1 | SRC-ARXIV@arXiv:2607.20220v1 | https://arxiv.org/html/2607.20220v1#S2 — 2. Routing Algorithm | https://arxiv.org/html/2607.20220v1#S3 — 3. Evaluation; https://arxiv.org/html/2607.20220v1#S3.SS4 — 3.4. Analysis | https://arxiv.org/html/2607.20220v1#S4 — 4. Discussion; https://arxiv.org/html/2607.20220v1#S6 — 6. Conclusion | Exact v1 links https://huggingface.co/Qwen/Qwen3.5-397B-A17B, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20220 | complete |
| SF-2026-ARXIV-2607-20265 | RP-6f87d4a4b8901f98 | standard | arXiv:2607.20265v1 | SRC-ARXIV@arXiv:2607.20265v1 | https://arxiv.org/html/2607.20265v1#S3 — 3 Methodology | https://arxiv.org/html/2607.20265v1#S4 — 4 Experimental Setup; https://arxiv.org/html/2607.20265v1#S5 — 5 Results | https://arxiv.org/html/2607.20265v1#S7 — 7 Discussion, limitations, and next steps; https://arxiv.org/html/2607.20265v1#S9 — 9 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20265 | complete |
| SF-2026-ARXIV-2607-20286 | RP-8541d667495d610c | deep | arXiv:2607.20286v1 | SRC-ARXIV@arXiv:2607.20286v1 | https://arxiv.org/html/2607.20286v1#A1.SS1 — A.1 Algorithms 1 and 2 | https://arxiv.org/html/2607.20286v1#A1.SS2 — A.2 Experiment III; https://arxiv.org/html/2607.20286v1#A1.SS3 — A.3 Experiment IV | https://arxiv.org/html/2607.20286v1#S6 — 6 Discussion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20286 | complete |
| SF-2026-ARXIV-2607-20289 | RP-99eb43e6fac989f3 | standard | arXiv:2607.20289v1 | SRC-ARXIV@arXiv:2607.20289v1 | https://arxiv.org/html/2607.20289v1#S1 — I Introduction; https://arxiv.org/html/2607.20289v1#S2 — II Related Work | https://arxiv.org/html/2607.20289v1#S6 — VI Experiments and Results | https://arxiv.org/html/2607.20289v1#S7 — VII Limitations and Future Work; https://arxiv.org/html/2607.20289v1#S2.SS2 — II-B Anticipating Future Tasks in Persistent Environments | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20289 | complete |
| SF-2026-ARXIV-2607-20293 | RP-e95747f9e56c6944 | deep | arXiv:2607.20293v1 | SRC-ARXIV@arXiv:2607.20293v1 | https://arxiv.org/html/2607.20293v1#S3 — 3 Method | https://arxiv.org/html/2607.20293v1#S4 — 4 Experiments; https://arxiv.org/html/2607.20293v1#S4.SS1 — 4.1 Experimental Setup | https://arxiv.org/html/2607.20293v1#S5 — 5 Conclusion | Exact v1 links https://github.com/pillom/EVO, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20293 | complete |
| SF-2026-ARXIV-2607-20300 | RP-c598bff2cd0b5ffe | deep | arXiv:2607.20300v1 | SRC-ARXIV@arXiv:2607.20300v1 | https://arxiv.org/html/2607.20300v1#Sx1.SSx1 — Supply Chain Construction; https://arxiv.org/html/2607.20300v1#Sx1.SSx2 — License Categorization | https://arxiv.org/html/2607.20300v1#Sx2 — Unknown Laundering; https://arxiv.org/html/2607.20300v1#Sx3 — Category Laundering | https://arxiv.org/html/2607.20300v1#Sx4 — Threats to Validity | Exact v1 links https://github.com/SAILResearch/LicenseLaundering/, https://huggingface.co/bigcode/starcoder, https://huggingface.co/docs/huggingface_hub/en/guides/model-cards; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20300 | complete |
| SF-2026-ARXIV-2607-20301 | RP-28ab1dc88df31cf3 | standard | arXiv:2607.20301v1 | SRC-ARXIV@arXiv:2607.20301v1 | https://arxiv.org/html/2607.20301v1#S1 — 1 Introduction; https://arxiv.org/html/2607.20301v1#S2 — 2 Related Work | https://arxiv.org/html/2607.20301v1#A6 — Appendix F Additional Experimental Results; https://arxiv.org/html/2607.20301v1#S3.SS2 — 3.2 Experimental Results | https://arxiv.org/html/2607.20301v1#S5 — 5 Discussion; https://arxiv.org/html/2607.20301v1#S6 — 6 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20301 | complete |
| SF-2026-ARXIV-2607-20327 | RP-2b786eaf85ba8006 | deep | arXiv:2607.20327v1 | SRC-ARXIV@arXiv:2607.20327v1 | https://arxiv.org/html/2607.20327v1#S3 — 3 Method; https://arxiv.org/html/2607.20327v1#S3.SS2 — 3.2 The Collaborative Inference Architecture of PyroDash | https://arxiv.org/html/2607.20327v1#S4.SS4 — 4.4 Ablation and Analysis; https://arxiv.org/html/2607.20327v1#S4 — 4 Experiments | https://arxiv.org/html/2607.20327v1#S6 — 6 Limitations and Future Work; https://arxiv.org/html/2607.20327v1#S5 — 5 Conclusion | Exact v1 links https://huggingface.co/datasets/HuggingFaceH4/aime_2024, https://huggingface.co/datasets/yentinglin/aime_2025, https://huggingface.co/datasets/pyromind/easyhard-24k; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20327 | complete |
| SF-2026-ARXIV-2607-20345 | RP-488012d1df15a4eb | deep | arXiv:2607.20345v1 | SRC-ARXIV@arXiv:2607.20345v1 | https://arxiv.org/html/2607.20345v1#S2 — II DEED Framework | https://arxiv.org/html/2607.20345v1#S2.SS3 — II-C In/Out-Distribution Analysis Tool; https://arxiv.org/html/2607.20345v1#S3 — III Experiments | https://arxiv.org/html/2607.20345v1#S3.SS3 — III-C Discussion; https://arxiv.org/html/2607.20345v1#S4 — IV Conclusions | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20345 | complete |
| SF-2026-ARXIV-2607-20351 | RP-16dcf9229f46b7b2 | standard | arXiv:2607.20351v1 | SRC-ARXIV@arXiv:2607.20351v1 | https://arxiv.org/html/2607.20351v1#A5.SS2 — E.2 Test-Time Training on the Thinking Model; https://arxiv.org/html/2607.20351v1#S3.SS1 — 3.1 Modality-Ordering Failure in Vision-Language Models | https://arxiv.org/html/2607.20351v1#A2 — Appendix B CHAIR Hallucination Evaluation; https://arxiv.org/html/2607.20351v1#A5 — Appendix E Thinking-Mode Ablations | https://arxiv.org/html/2607.20351v1#S6 — 6 Discussion, Limitations, and Future Work; https://arxiv.org/html/2607.20351v1#S3.SS1 — 3.1 Modality-Ordering Failure in Vision-Language Models | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20351 | complete |
| SF-2026-ARXIV-2607-20357 | RP-db816538f44b9ebe | deep | arXiv:2607.20357v1 | SRC-ARXIV@arXiv:2607.20357v1 | https://arxiv.org/html/2607.20357v1#S1 — 1 Introduction; https://arxiv.org/html/2607.20357v1#S2 — 2 Related Work | https://arxiv.org/html/2607.20357v1#S4 — 4 Experiments and Results; https://arxiv.org/html/2607.20357v1#S4.SS1 — 4.1 Experiment Setup | https://arxiv.org/html/2607.20357v1#S5 — 5 Conclusion and Discussion; https://arxiv.org/html/2607.20357v1#S4.SS2 — 4.2 Main Results and Discussion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20357 | complete |
| SF-2026-ARXIV-2607-20368 | RP-970a5c03e48ba896 | deep | arXiv:2607.20368v1 | SRC-ARXIV@arXiv:2607.20368v1 | https://arxiv.org/html/2607.20368v1#S3 — 3 Method | https://arxiv.org/html/2607.20368v1#A1 — Appendix A Additional Experimental Details; https://arxiv.org/html/2607.20368v1#A7 — Appendix G Additional Qualitative Results | https://arxiv.org/html/2607.20368v1#A6 — Appendix F Limitations; https://arxiv.org/html/2607.20368v1#S5 — 5 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20368 | complete |
| SF-2026-ARXIV-2607-20372 | RP-a65278ee39026f69 | standard | arXiv:2607.20372v1 | SRC-ARXIV@arXiv:2607.20372v1 | https://arxiv.org/html/2607.20372v1#S3 — 3 Methods; https://arxiv.org/html/2607.20372v1#A4 — Appendix D Implementation details | https://arxiv.org/html/2607.20372v1#A2 — Appendix B Quantitative analyses on Qwen-2.5-1.5B-Instruct results; https://arxiv.org/html/2607.20372v1#S4 — 4 Results | https://arxiv.org/html/2607.20372v1#S5 — 5 Conclusion; https://arxiv.org/html/2607.20372v1#Sx1 — Limitations | Exact v1 links https://github.com/ChangLiu-DrPatient/Notes-to-self, https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro/blob/main/DeepSeek_V4.pdf, https://huggingface.co/datasets/HuggingFaceH4/MATH-500/viewer/default/test?row=122; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20372 | complete |
| SF-2026-ARXIV-2607-20379 | RP-0d8f52a3672cfb11 | deep | arXiv:2607.20379v1 | SRC-ARXIV@arXiv:2607.20379v1 | https://arxiv.org/html/2607.20379v1#A5 — Appendix E Released-System Audit Details; https://arxiv.org/html/2607.20379v1#S5.SS1 — 5.1 Method | https://arxiv.org/html/2607.20379v1#A2 — Appendix B Safety Experiment 1: The Discrepancy Detector; https://arxiv.org/html/2607.20379v1#A3 — Appendix C Safety Experiment 2: Legibility Persistence Under Head-Free Fine-Tuning | https://arxiv.org/html/2607.20379v1#S8 — 8 Discussion and Limitations; https://arxiv.org/html/2607.20379v1#S9 — 9 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20379 | complete |
| SF-2026-ARXIV-2607-20389 | RP-5431a55c222f081d | standard | arXiv:2607.20389v1 | SRC-ARXIV@arXiv:2607.20389v1 | https://arxiv.org/html/2607.20389v1#S2.SS1 — 2.1 Video Captioning and Multi-modal Large Language Models; https://arxiv.org/html/2607.20389v1#S5.SS1 — 5.1 Implementation Details | https://arxiv.org/html/2607.20389v1#S5 — 5 Results and Analysis; https://arxiv.org/html/2607.20389v1#S5.SS2 — 5.2 Benchmarks and Evaluation Metrics | https://arxiv.org/html/2607.20389v1#S5.SS5 — 5.5 Limitations; https://arxiv.org/html/2607.20389v1#S6 — 6 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20389 | complete |
| SF-2026-ARXIV-2607-20402 | RP-542d446b797d3374 | standard | arXiv:2607.20402v1 | SRC-ARXIV@arXiv:2607.20402v1 | https://arxiv.org/html/2607.20402v1#S3 — 3 Technical Approach; https://arxiv.org/html/2607.20402v1#S3.SS2 — 3.2 SoftReason Architecture | https://arxiv.org/html/2607.20402v1#S4 — 4 Experimental Evaluation | https://arxiv.org/html/2607.20402v1#S5 — 5 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20402 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2607-19349:start -->
### FineServe: A Fine-Grained Dataset and Characterization of Global LLM Serving Workloads

<!-- claim:SF-2026-ARXIV-2607-19349:start -->Large language models (LLMs) are increasingly deployed as always-on online services, making efficient LLM serving a critical systems challenge. Achieving low latency and high throughput under volatile demand requires deep understanding of real-world serving workloads, yet existing studies often rely on proxy traces or coarse-grained characterizations that fail to capture the heterogeneity of modern multi-model LLM platforms. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19349:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language models (LLMs) are increasingly deployed as always-on online services, making efficient LLM serving a critical systems challenge.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Large language models (LLMs) are increasingly deployed as always-on online services, making efficient LLM serving a critical systems challenge.

**证据证明什么。** FineServe is available at https://github.com/hihiztc1/FineServe.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19349v1#A3.SS1 — C.1. Architecture-Specific Input–Output Token Models; https://arxiv.org/html/2607.19349v1#S3 — 3. Characterizing Architectures and Scales。Evaluation：https://arxiv.org/html/2607.19349v1#S1 — 1. Introduction; https://arxiv.org/html/2607.19349v1#S2 — 2. Preliminary and Motivation。Limitations / counterevidence：https://arxiv.org/html/2607.19349v1#S6 — 6. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/hihiztc1/FineServe, https://github.com/microsoft/DeepSpeed-MII, https://github.com/NVIDIA/TensorRT-LLM; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-SCHEDULING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19349:end -->

<!-- review:SF-2026-ARXIV-2607-19351:start -->
### OpenEvoShield: Dual Non-Stationary Continual Defense for Open-World Multi-Agent System Attacks

<!-- claim:SF-2026-ARXIV-2607-19351:start -->LLM-based multi-agent systems (LLM-MAS) are increasingly deployed in safety-critical applications, where adversaries inject malicious instructions through inter-agent communication to propagate harmful behaviors. Unlike static threats, these attacks are doubly dynamic: adversaries refine injection strategies against deployed defenses while normal-agent behavior drifts with system expansion. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19351:end -->

**为什么进入候选分母。** 摘要首要问题为“LLM-based multi-agent systems (LLM-MAS) are increasingly deployed in safety-critical applications, where adversaries inject malicious instructions through inter-agent communication to propagate harmful behaviors.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** We propose OpenEvoShield, a co-evolutionary continual defense framework for LLM-MAS.

**证据证明什么。** Experiments over 100 deployment rounds across five benchmarks and four MAS topologies show that OpenEvoShield outperforms static and continual baselines, detecting most previously unseen attacks while keeping false positive rates low.

**证据没有证明什么。** Third, we do not evaluate against adaptive adversaries who are aware of the detection mechanism; such threat models represent an important direction for future work. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19351v1#A1.SS2 — A.2 Implementation Details; https://arxiv.org/html/2607.19351v1#A2 — Appendix B Full Algorithm。Evaluation：https://arxiv.org/html/2607.19351v1#A3 — Appendix C Additional Experiment Results; https://arxiv.org/html/2607.19351v1#A1 — Appendix A Experiment Details。Limitations / counterevidence：https://arxiv.org/html/2607.19351v1#A6 — Appendix F Limitations; https://arxiv.org/html/2607.19351v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://neurips.cc/public/guides/CodeSubmissionPolicy, https://paperswithcode.com/datasets, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Third, we do not evaluate against adaptive adversaries who are aware of the detection mechanism; such threat models represent an important direction for future work.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-MULTI-AGENT`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19351:end -->

<!-- review:SF-2026-ARXIV-2607-19353:start -->
### Benchmarking Confidential GPU Inference on NVIDIA H100 under Intel TDX

<!-- claim:SF-2026-ARXIV-2607-19353:start -->Confidential computing is becoming a practical deployment requirement for AI inference workloads that process sensitive inputs or protect proprietary model assets. However, the performance cost of enabling confidential execution for GPU-accelerated large language model serving remains workload dependent and operationally important. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19353:end -->

**为什么进入候选分母。** 摘要首要问题为“Confidential computing is becoming a practical deployment requirement for AI inference workloads that process sensitive inputs or protect proprietary model assets.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** However, the performance cost of enabling confidential execution for GPU-accelerated large language model serving remains workload dependent and operationally important.

**证据证明什么。** The results suggest that confidential GPU inference can retain usable throughput under load, but capacity planning must account for both the steady throughput penalty and the earlier saturation behavior observed for larger models.

**证据没有证明什么。** 7 Limitations and Threats to Validity • The benchmark covers two models and one GPU configuration. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19353v1#S3.SS4 — 3.4 Load-Generation Methodology; https://arxiv.org/html/2607.19353v1#S3.SS2 — 3.2 Models and Execution Modes。Evaluation：https://arxiv.org/html/2607.19353v1#A1 — Appendix A Full Closed-Loop Results; https://arxiv.org/html/2607.19353v1#S3 — 3 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.19353v1#S7 — 7 Limitations and Threats to Validity; https://arxiv.org/html/2607.19353v1#S6 — 6 Discussion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：7 Limitations and Threats to Validity • The benchmark covers two models and one GPU configuration.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19353:end -->

<!-- review:SF-2026-ARXIV-2607-19355:start -->
### Information Discernment in Large Language Models

<!-- claim:SF-2026-ARXIV-2607-19355:start -->LLMs are increasingly used with external knowledge sources like the internet. Do they weigh information appropriately -- updating more for reliable sources (source discernment) and more when claims bring priors closer to the truth (truth discernment)? 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19355:end -->

**为什么进入候选分母。** 摘要首要问题为“LLMs are increasingly used with external knowledge sources like the internet.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We formalize this as information discernment and introduce Learn2Discern (L2D), an experimental framework and benchmark grounded in three normative axioms with interpretable metrics.

**证据证明什么。** Across 13 models and nearly 670K trials, we find consistent failures across both dimensions: models perform near chance on source and truth discernment, rely on source popularity twice as much as source reliability, and update roughly equally whether a claim improves or worsens their position relative to the ground truth.

**证据没有证明什么。** The second is that by orthogonally varying source reliability and claim accuracy, we separate their independent effects—something we cannot do with naturally occurring misinformation. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19355v1#A8.SS1 — H.1 Model Setup。Evaluation：https://arxiv.org/html/2607.19355v1#A10 — Appendix J Additional Main Experiment Results; https://arxiv.org/html/2607.19355v1#A3.SS4 — C.4 Results。Limitations / counterevidence：https://arxiv.org/html/2607.19355v1#S10 — 10 Discussion。

**Artifact boundary。** Exact v1 links https://github.com/josh-ashkinaze/l2d-public, https://huggingface.co/datasets/CogComp/trec, https://huggingface.co/prajjwal1/bert-tiny; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：The second is that by orthogonally varying source reliability and claim accuracy, we separate their independent effects—something we cannot do with naturally occurring misinformation.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-RAG`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19355:end -->

<!-- review:SF-2026-ARXIV-2607-19356:start -->
### NEXUS: Structured Runtime Safety for Tool-Using LLM Agents

<!-- claim:SF-2026-ARXIV-2607-19356:start -->Tool-using LLM agents increasingly execute high-impact actions, making runtime safety monitoring essential. We present NEXUS (Neural EXecution Utility and Safety), a structured-plan safety monitor that applies a formal intervention policy to select among four actions: allow, block, request confirmation, or request revision. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19356:end -->

**为什么进入候选分母。** 摘要首要问题为“Tool-using LLM agents increasingly execute high-impact actions, making runtime safety monitoring essential.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** We present NEXUS (Neural EXecution Utility and Safety), a structured-plan safety monitor that applies a formal intervention policy to select among four actions: allow, block, request confirmation, or request revision.

**证据证明什么。** On a 128-instance synthetic benchmark, NEXUS achieves an F1 score of 0.949 and a 4-class intervention accuracy of 0.6406, outperforming rule-only intervention selection by 27.3 percentage points.

**证据没有证明什么。** NEXUS is explicitly not a replacement for model alignment, content-safety filtering, or post-execution audit; it is a runtime layer between plan production and execution that complements those other mechanisms. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19356v1#S4 — 4 The NEXUS Framework; https://arxiv.org/html/2607.19356v1#A1 — Appendix A Runtime Monitoring Algorithm。Evaluation：https://arxiv.org/html/2607.19356v1#A11 — Appendix K Error Analysis; https://arxiv.org/html/2607.19356v1#A14 — Appendix N R-Judge IoT: Trace-Level Failure Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.19356v1#A14 — Appendix N R-Judge IoT: Trace-Level Failure Analysis; https://arxiv.org/html/2607.19356v1#A17 — Appendix Q Deployment Posture and Future Extensions。

**Artifact boundary。** Exact v1 links https://github.com/openai/swarm, https://github.com/eliashossain001/nexus, https://huggingface.co/EliasHossain/nexus-risk-scorer; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：NEXUS is explicitly not a replacement for model alignment, content-safety filtering, or post-execution audit; it is a runtime layer between plan production and execution that complements those other mechanisms.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-TOOL-CALLING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19356:end -->

<!-- review:SF-2026-ARXIV-2607-19358:start -->
### LISA: Linear-Indexed Sparse Attention for Efficient Long-Context Reasoning

<!-- claim:SF-2026-ARXIV-2607-19358:start -->Recent advances in long chain-of-thought reasoning models such as DeepSeek-R1 have led to increasingly longer inference context lengths under the test-time scaling paradigm. However, the O(n^2) computational complexity of standard self-attention causes inference costs to grow sharply with long sequences, limiting the deployment of long-CoT reasoning in production settings. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19358:end -->

**为什么进入候选分母。** 摘要首要问题为“Recent advances in long chain-of-thought reasoning models such as DeepSeek-R1 have led to increasingly longer inference context lengths under the test-time scaling paradigm.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** To address this, we propose LISA (Linear-Indexed Sparse Attention), a plug-and-play attention replacement module that requires no pretraining from scratch.

**证据证明什么。** Experiments on DeepSeek-distilled-Qwen models demonstrate that LISA achieves a 50% inference speedup under 16K-token context, while improving average performance by 5.6% on reasoning benchmarks including AIME and MATH-500.

**证据没有证明什么。** While this design ensures the plug-and-play property and avoids catastrophic forgetting, it also means that the synergy between the main model and the new components cannot be further optimized through fine-tuning. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19358v1#S3 — 3 Method; https://arxiv.org/html/2607.19358v1#S4.SS1 — 4.1 Implementation Details。Evaluation：https://arxiv.org/html/2607.19358v1#S4 — 4 Experiments; https://arxiv.org/html/2607.19358v1#S4.SS4 — 4.4 Main Results。Limitations / counterevidence：https://arxiv.org/html/2607.19358v1#S5 — 5 Conclusion; https://arxiv.org/html/2607.19358v1#S6 — 6 Limitations。

**Artifact boundary。** Exact v1 links https://huggingface.co/datasets/Maxwell-Jia/AIME_2024, https://huggingface.co/datasets/opencompass/AIME2025, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：While this design ensures the plug-and-play property and avoids catastrophic forgetting, it also means that the synergy between the main model and the new components cannot be further optimized through fine-tuning.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MODEL-LONG-CONTEXT`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19358:end -->

<!-- review:SF-2026-ARXIV-2607-19359:start -->
### Profile-Graph Memory for LLM Agents: Implicit Cross-Entity Traversal through Narrative Profiles

<!-- claim:SF-2026-ARXIV-2607-19359:start -->Long-term memory is essential for LLM agents that interact across sessions, yet current memory benchmarks primarily evaluate single-hop recall, leaving multi-hop association largely unmeasured. First, we introduce MemHop, a multi-hop memory benchmark of 1,000 questions at hop depths 1-5 across 10 social-network scenarios, with per-hop evidence annotations. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19359:end -->

**为什么进入候选分母。** 摘要首要问题为“Long-term memory is essential for LLM agents that interact across sessions, yet current memory benchmarks primarily evaluate single-hop recall, leaving multi-hop association largely unmeasured.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** First, we introduce MemHop, a multi-hop memory benchmark of 1,000 questions at hop depths 1-5 across 10 social-network scenarios, with per-hop evidence annotations.

**证据证明什么。** ProGraph averages 80.1% on MemHop (matching the FullContext reference) and 78.4% on LoCoMo (exceeding FullContext by 11.3pp), outperforming Mem0, A-Mem, HippoRAG, and RAG on both.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19359v1#A3 — Appendix C Baseline Implementation Details。Evaluation：https://arxiv.org/html/2607.19359v1#S4 — 4 MemHop Benchmark; https://arxiv.org/html/2607.19359v1#S5 — 5 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.19359v1#S6 — 6 Discussion; https://arxiv.org/html/2607.19359v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/ShengtongZhu/ProGraph, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19359:end -->

<!-- review:SF-2026-ARXIV-2607-19361:start -->
### Stateful Guardrails for Multi-Turn LLM Systems: A Conversational Risk Accumulation Framework

<!-- claim:SF-2026-ARXIV-2607-19361:start -->Most safety guardrails for large language models (LLMs) evaluate each prompt-response pair in isolation, which misses failures that arise only over a dialogue as benign turns compose into harm. We term this Conversational Risk Accumulation (CRA): gradual intent drift, fragmented assembly of prohibited instructions, and sensitivity build-up from repeated disclosures. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19361:end -->

**为什么进入候选分母。** 摘要首要问题为“Most safety guardrails for large language models (LLMs) evaluate each prompt-response pair in isolation, which misses failures that arise only over a dialogue as benign turns compose into harm.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We propose a session-layer CRA Framework that tracks three trajectory signals: semantic drift from a session anchor, a sensitivity-weighted information accumulation graph over extracted entities, and a compliance-gradient signal capturing increasing willingness to comply.

**证据证明什么。** For scoring, we provide (i) an unsupervised convex fusion for attribution and ablations, and (ii) CRA-Net DA, a compact learned trajectory model trained with family-adversarial objectives to reduce length and topic-coverage confounds.

**证据没有证明什么。** CoSafe diagnostics (Section 9 ) and benign-traffic calibration (Section 9.7 ) complement the primary CRA-Bench and Human-CRA-Transfer evidence; the small- WildChat probe is footnoted only. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19361v1#S4 — 4 The CRA Framework; https://arxiv.org/html/2607.19361v1#S5 — 5 Design Consistency Properties。Evaluation：https://arxiv.org/html/2607.19361v1#S9.SS9 — 9.9 Ablation analysis; https://arxiv.org/html/2607.19361v1#S2.SS1 — 2.1 Multi-turn safety evaluation and dialogue state modeling。Limitations / counterevidence：https://arxiv.org/html/2607.19361v1#S12 — 12 Discussion and Limitations; https://arxiv.org/html/2607.19361v1#S13 — 13 Conclusions。

**Artifact boundary。** Exact v1 links https://huggingface.co/datasets/Asap7772/cosafe_all_rollouts, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：CoSafe diagnostics (Section 9 ) and benign-traffic calibration (Section 9.7 ) complement the primary CRA-Bench and Human-CRA-Transfer evidence; the small- WildChat probe is footnoted only.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19361:end -->

<!-- review:SF-2026-ARXIV-2607-19362:start -->
### GraphContainer: A Unified Platform for Comparing and Debugging Graph RAG Methods

<!-- claim:SF-2026-ARXIV-2607-19362:start -->Graph RAG mitigates hallucinations and stale knowledge in LLMs, particularly for multi-hop question answering. However, existing approaches remain highly fragmented and incompatible. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19362:end -->

**为什么进入候选分母。** 摘要首要问题为“Graph RAG mitigates hallucinations and stale knowledge in LLMs, particularly for multi-hop question answering.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** To bridge this gap, we propose GraphContainer, a novel platform designed to unify and visualize diverse graph RAG workflows.

**证据证明什么。** Through an interactive web interface, we demonstrate GraphContainer's ability to import heterogeneous graphs and perform live, traceable visual debugging of graph RAG methods.

**证据没有证明什么。** Conclusions and Future Works In this paper, we presented GraphContainer , a unified visual analytics platform designed to evaluate and debug graph RAG methods across heterogeneous formats. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19362v1#S2 — 2. System Overview。Evaluation：https://arxiv.org/html/2607.19362v1#S3.SS2 — 3.2. Scenario 2: Comparative Retrieval Analysis; https://arxiv.org/html/2607.19362v1#S4 — 4. Experimental Study。Limitations / counterevidence：https://arxiv.org/html/2607.19362v1#S5 — 5. Conclusions and Future Works。

**Artifact boundary。** Exact v1 links https://github.com/asmath472/GraphContainer, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Conclusions and Future Works In this paper, we presented GraphContainer , a unified visual analytics platform designed to evaluate and debug graph RAG methods across heterogeneous formats.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-RAG`；evidence-stage relation：`principle_reuse`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19362:end -->

<!-- review:SF-2026-ARXIV-2607-19363:start -->
### AdaRoPE: Not All Attention Heads Should Rotate and Scale Equally

<!-- claim:SF-2026-ARXIV-2607-19363:start -->Rotary Position Embedding (RoPE) is widely adopted in Transformers to encode positional information, yet standard implementations enforce a uniform frequency schedule and scaling across all attention heads. Using simplified retrieval tasks and length generalization scenarios, we show -- both empirically and theoretically -- that heads with different functional roles require distinct frequency ranges and attention scaling factors to operate effectively. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19363:end -->

**为什么进入候选分母。** 摘要首要问题为“Rotary Position Embedding (RoPE) is widely adopted in Transformers to encode positional information, yet standard implementations enforce a uniform frequency schedule and scaling across all attention heads.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** For context extension, we further show that uniform frequency and attention scaling, used in methods such as YaRN, are suboptimal.

**证据证明什么。** Pretrained LLMs with AdaRoPE consistently outperform existing RoPE variants, including partial RoPE and NoPE baselines.

**证据没有证明什么。** To address this limitation, we propose AdaRoPE, a drop-in extension that learns head-wise, dimension-wise frequencies (AdaFreq) and length-aware attention scaling (AdaScale). 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19363v1#S3.SS3 — 3.3 Design of AdaRoPE; https://arxiv.org/html/2607.19363v1#S3.SS4 — 3.4 Implementation and Overhead。Evaluation：https://arxiv.org/html/2607.19363v1#A2 — Appendix B Additional Results; https://arxiv.org/html/2607.19363v1#A2.SS1 — B.1 Analysis on Synthetic Tasks。Limitations / counterevidence：https://arxiv.org/html/2607.19363v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：To address this limitation, we propose AdaRoPE, a drop-in extension that learns head-wise, dimension-wise frequencies (AdaFreq) and length-aware attention scaling (AdaScale).

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MODEL-POSITION-ENCODING`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19363:end -->

<!-- review:SF-2026-ARXIV-2607-19367:start -->
### Rethinking Uncertainty Evaluation in Large Language Models

<!-- claim:SF-2026-ARXIV-2607-19367:start -->Calibration is the primary criterion for evaluating LLM confidence, but it is insufficient: it admits trivially incoherent estimators, depends on the evaluation distribution, and does not test the extent to which the estimation can be interpreted as a consistent, underlying probability function. What we actually need is for LLM confidence estimates to satisfy the conditions required of coherent probabilistic beliefs. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19367:end -->

**为什么进入候选分母。** 摘要首要问题为“Calibration is the primary criterion for evaluating LLM confidence, but it is insufficient: it admits trivially incoherent estimators, depends on the evaluation distribution, and does not test the extent to which the estimation can be interpreted as a consistent, underlying probability function.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Our results show current LLM confidence estimates cannot be interpreted as coherent probabilities; our framework provides the tools to measure and close this gap.

**证据证明什么。** Our results show current LLM confidence estimates cannot be interpreted as coherent probabilities; our framework provides the tools to measure and close this gap.

**证据没有证明什么。** Faithfulness and calibration are distinguishable axes, and a single metric cannot adjudicate between them. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19367v1#S4 — 4 Methodology; https://arxiv.org/html/2607.19367v1#S4.SS2 — 4.2 Confidence Estimation Methods。Evaluation：https://arxiv.org/html/2607.19367v1#A3 — Appendix C Full Benchmark Results; https://arxiv.org/html/2607.19367v1#A2 — Appendix B Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.19367v1#A1.SS2 — A.2 Limitations of LLM-Based Semantic Clustering; https://arxiv.org/html/2607.19367v1#S5 — 5 Discussion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Faithfulness and calibration are distinguishable axes, and a single metric cannot adjudicate between them.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19367:end -->

<!-- review:SF-2026-ARXIV-2607-19368:start -->
### Spectral-LSH: Sub-Quadratic Prompt Compression via Krylov-Projected Locality-Sensitive Hashing

<!-- claim:SF-2026-ARXIV-2607-19368:start -->Long-prompt inference remains expensive because prefill attention scales quadratically with sequence length. We propose Spectral-LSH, a training-free prompt compression method that operates before the prompt enters the language model. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19368:end -->

**为什么进入候选分母。** 摘要首要问题为“Long-prompt inference remains expensive because prefill attention scales quadratically with sequence length.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** We propose Spectral-LSH, a training-free prompt compression method that operates before the prompt enters the language model.

**证据证明什么。** At $ρ= 16 \times$, Qwen2.5-7B (adaptive) reduces the PPL ratio from 353.409 to 196.963, while Qwen2.5-14B (adaptive) reduces it from 9.533 to 3.427.

**证据没有证明什么。** The method needs the LLM’s input embedding matrix, which is available for open-weight models but not API-only services like GPT-4. (2) Model-dependent quality. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19368v1#S3 — 3 Method; https://arxiv.org/html/2607.19368v1#A2.SS1 — B.1 Implementation Summary。Evaluation：https://arxiv.org/html/2607.19368v1#A3 — Appendix C Additional Experimental Results; https://arxiv.org/html/2607.19368v1#S5 — 5 Experiments and Results。Limitations / counterevidence：https://arxiv.org/html/2607.19368v1#S6 — 6 Discussion and Limitations; https://arxiv.org/html/2607.19368v1#S5.SS7 — 5.7 Results Discussion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：The method needs the LLM’s input embedding matrix, which is available for open-weight models but not API-only services like GPT-4. (2) Model-dependent quality.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-PREFILL`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19368:end -->

<!-- review:SF-2026-ARXIV-2607-19386:start -->
### Building Fast, Evaluating Slow: Pipeline Choices Dominate Autointerpretability Score Variance

<!-- claim:SF-2026-ARXIV-2607-19386:start -->Cross-paper comparison of sparse autoencoder (SAE) interpretability often relies on autointerpretability scores. In this evaluation pipeline, a language model (LM) explains each feature, and another LM scores the explanation. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19386:end -->

**为什么进入候选分母。** 摘要首要问题为“Cross-paper comparison of sparse autoencoder (SAE) interpretability often relies on autointerpretability scores.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Through systematic experiments across four metrics (simulation, detection, fuzzing, purity), two models (Pythia-160M, Apertus-8B), and four axes of methodological variation, we show that this assumption does not hold.

**证据证明什么。** Through systematic experiments across four metrics (simulation, detection, fuzzing, purity), two models (Pythia-160M, Apertus-8B), and four axes of methodological variation, we show that this assumption does not hold.

**证据没有证明什么。** Future work could examine alternative evaluations that do not rely solely on LLM-judged explanations. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19386v1#S3.SSx1 — Methodological Variance Exceeds Architectural Variance; https://arxiv.org/html/2607.19386v1#A4.SS1 — D.1 Pythia SAE models。Evaluation：https://arxiv.org/html/2607.19386v1#A2 — Appendix B Experiments; https://arxiv.org/html/2607.19386v1#A2.SS1 — B.1 Experiment Overview。Limitations / counterevidence：https://arxiv.org/html/2607.19386v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://huggingface.co/datasets/codeparrot/github-code, https://neurips.cc/public/guides/CodeSubmissionPolicy, https://paperswithcode.com/datasets; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Future work could examine alternative evaluations that do not rely solely on LLM-judged explanations.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19386:end -->

<!-- review:SF-2026-ARXIV-2607-19390:start -->
### The Orthogonalized Read Is a Removable Training Scaffold for Recurrent Memory

<!-- claim:SF-2026-ARXIV-2607-19390:start -->A recent report finds that orthogonalizing the mLSTM memory matrix at read time (five Newton-Schulz iterations, trained through) substantially improves noisy associative recall. The effect replicates, but it is not a memory improvement. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19390:end -->

**为什么进入候选分母。** 摘要首要问题为“A recent report finds that orthogonalizing the mLSTM memory matrix at read time (five Newton-Schulz iterations, trained through) substantially improves noisy associative recall.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** Two conclusions travel beyond the intervention: recall benchmarks used for architecture selection partly measure trainability, and the system is a fully instrumented model organism of "emergence," in which a sharp behavioral threshold demonstrably arises from a censored metric over gradually accumulating structure.

**证据证明什么。** The effect replicates, but it is not a memory improvement.

**证据没有证明什么。** The hazard model treats destabilization as independent censoring; a joint competing-risks model might refine the hot-edge story. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19390v1#S11.SS0.SSS0.Px1 — Benchmark-driven architecture selection.; https://arxiv.org/html/2607.19390v1#S12.SS0.SSS0.Px3 — Orthogonalization in learning systems.。Evaluation：https://arxiv.org/html/2607.19390v1#S11.SS0.SSS0.Px1 — Benchmark-driven architecture selection.; https://arxiv.org/html/2607.19390v1#S6.SS0.SSS0.Px1 — Swap evaluations.。Limitations / counterevidence：https://arxiv.org/html/2607.19390v1#S11 — 11 Discussion; https://arxiv.org/html/2607.19390v1#S13 — 13 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/no-way-labs/recurrent-memory-scaffold, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：The hazard model treats destabilization as independent censoring; a joint competing-risks model might refine the hot-edge story.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19390:end -->

<!-- review:SF-2026-ARXIV-2607-19393:start -->
### Decodable but Not Detectable: A Leakage Fingerprint for Near-OOD Benchmarks

<!-- claim:SF-2026-ARXIV-2607-19393:start -->While auditing a perturbation-based OOD detector on a document benchmark, we recorded an AUROC of 0.326 -- well below the 0.5 chance level. The cause is a benchmark leak: the designated "OOD" class is one the model was trained on, so its examples sit inside the in-distribution fit set and the detector is penalized for correctly ranking them as familiar. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19393:end -->

**为什么进入候选分母。** 摘要首要问题为“While auditing a perturbation-based OOD detector on a document benchmark, we recorded an AUROC of 0.326 -- well below the 0.5 chance level.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** The contributions are a corrected protocol and a validated leak diagnostic, not a new OOD method.

**证据证明什么。** Under the corrected protocol, perturbation signals are decodable but not detectable: a supervised reader recovers the OOD signal (AUROC 0.87-1.00) while no unsupervised detector does, and the perturbation method does not improve on plain Mahalanobis distance.

**证据没有证明什么。** We correct the protocol, propose and validate a fingerprint that audits a designated split for the same contamination without backbone re-training (in embedding space: sensitivity , specificity across the full of four fine-tuned backbones), run the audit it enables across standard OOD benchmark pairs (where it fires on only the one intrinsically-hard pair our scope predicts, confirming standard construction is clean and the test specific in the wild), and, under the correction, show that perturbation signatures are decodable but not detectable, adding nothing useful over the embeddings they come from. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19393v1#S5.SS1 — 5.1 Design。Evaluation：https://arxiv.org/html/2607.19393v1#S4 — 4 A Benchmark Leak in Near-OOD Evaluation; https://arxiv.org/html/2607.19393v1#A2 — Appendix B Per-Seed Results for the Leak。Limitations / counterevidence：https://arxiv.org/html/2607.19393v1#S10 — 10 Conclusion; https://arxiv.org/html/2607.19393v1#S9 — 9 Discussion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：We correct the protocol, propose and validate a fingerprint that audits a designated split for the same contamination without backbone re-training (in embedding space: sensitivity , specificity across the full of four fine-tuned backbones), run the audit it enables across standard OOD benchmark pairs (where it fires on only the one intrinsically-hard pair our scope predicts, confirming standard construction is clean and the test specific in the wild), and, under the correction, show that perturbation signatures are decodable but not detectable, adding nothing useful over the embeddings they come from.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19393:end -->

<!-- review:SF-2026-ARXIV-2607-19395:start -->
### From Trajectories to Prefixes: Reusing Teacher Trajectories via Replayed Prefixes and Online Continuation

<!-- claim:SF-2026-ARXIV-2607-19395:start -->Small language models are attractive backbones for interactive agents, but direct distillation from strong teacher trajectories often turns rich multi-turn behavior into one-shot imitation targets. This is inefficient in long-horizon environments, where early decisions shape later states and rewards. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19395:end -->

**为什么进入候选分母。** 摘要首要问题为“Small language models are attractive backbones for interactive agents, but direct distillation from strong teacher trajectories often turns rich multi-turn behavior into one-shot imitation targets.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We propose Prefix-GRPO, a reinforcement learning framework that decomposes teacher trajectories into replay-aligned prefix queries and online continuations.

**证据证明什么。** Experiments on TextCraft, BabyAI, and ALFWorld show that Prefix-GRPO improves small-model agents over distillation and standard RL baselines, while ablations show that replay alone is insufficient without explicit prefix-token optimization.

**证据没有证明什么。** Most failures are not parser failures: only one failed sample ends with an invalid action. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19395v1#S3 — 3 Method; https://arxiv.org/html/2607.19395v1#A2 — Appendix B Implementation Details in Each Environment。Evaluation：https://arxiv.org/html/2607.19395v1#A3 — Appendix C Additional Experimental Results; https://arxiv.org/html/2607.19395v1#A3.SS1 — C.1 Additional TextCraft Objective Ablations。Limitations / counterevidence：https://arxiv.org/html/2607.19395v1#S5 — 5 Conclusion and Future Work; https://arxiv.org/html/2607.19395v1#A4.SS3 — D.3 Failure Modes。

**Artifact boundary。** Exact v1 links https://github.com/HappynessI/Prefix_GRPO, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Most failures are not parser failures: only one failed sample ends with an invalid action.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-WORKFLOW`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19395:end -->

<!-- review:SF-2026-ARXIV-2607-19396:start -->
### CrackedPDFs: A Controlled Benchmark for Hidden Prompt Injection in PDFs

<!-- claim:SF-2026-ARXIV-2607-19396:start -->Document-based LLM systems often flatten a PDF before guardrails inspect it. That step can discard evidence that an instruction was never visible to the user. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19396:end -->

**为什么进入候选分母。** 摘要首要问题为“Document-based LLM systems often flatten a PDF before guardrails inspect it.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** Document-based LLM systems often flatten a PDF before guardrails inspect it.

**证据证明什么。** These results show that document-aware hybrid detection is useful under controlled paired evaluation.

**证据没有证明什么。** The main result is not that every simple detector works. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19396v1#S2.SS1 — 2.1 Prompt injection in LLM-integrated systems; https://arxiv.org/html/2607.19396v1#S2.SS6 — 2.6 Testing methodology and security framing。Evaluation：https://arxiv.org/html/2607.19396v1#S4.SS1 — 4.1 Benchmark construction and problem setup; https://arxiv.org/html/2607.19396v1#S4.SS8 — 4.8 Evaluation metrics。Limitations / counterevidence：https://arxiv.org/html/2607.19396v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/tldrsec/prompt-injection-defenses, https://www.promptfoo.dev/lm-security-db/vuln/invisible-unicode-jailbreak-779fc810, https://huggingface.co/meta-llama/Prompt-Guard-86M; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：The main result is not that every simple detector works.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19396:end -->

<!-- review:SF-2026-ARXIV-2607-19399:start -->
### Leveraging Offline Supervision for Efficient and Generalizable Reinforcement Learning in Large-Scale Vision-Language-Action Models

<!-- claim:SF-2026-ARXIV-2607-19399:start -->It is commonly observed that online reinforcement learning (RL) produces better-performing strategies than offline methods across a broad range of performance measures. In particular, RL-trained policies exhibit stronger out-of-distribution (OOD) behavior, where models trained only with imitation learning approaches often struggle. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19399:end -->

**为什么进入候选分母。** 摘要首要问题为“It is commonly observed that online reinforcement learning (RL) produces better-performing strategies than offline methods across a broad range of performance measures.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** Specifically, we study RL methods regularized by offline supervision via either offline data or an offline-trained reference policy.

**证据证明什么。** Our results show that although offline training achieves limited OOD performance by itself, incorporating offline supervision into RL preserves strong OOD capability while substantially improving training efficiency.

**证据没有证明什么。** This slower adaptation is not uniform across OOD dimensions. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19399v1#S4 — 4 Method; https://arxiv.org/html/2607.19399v1#S2.SS1 — 2.1 Reinforcement Learning for Vision–Language–Action Models。Evaluation：https://arxiv.org/html/2607.19399v1#S5 — 5 Experiments; https://arxiv.org/html/2607.19399v1#S5.SS1 — 5.1 Baseline Results and Reproduction。Limitations / counterevidence：https://arxiv.org/html/2607.19399v1#S6.SS3 — 6.3 Discussion of SFT-Initialized RL; https://arxiv.org/html/2607.19399v1#S6.SS4 — 6.4 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：This slower adaptation is not uniform across OOD dimensions.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19399:end -->

<!-- review:SF-2026-ARXIV-2607-19405:start -->
### Reproducing Recurrent Transformers: The CoTFormer

<!-- claim:SF-2026-ARXIV-2607-19405:start -->The CoTFormer architecture formalizes Chain-of-Thought as a form of recurrent latent computation, preserving intermediate states as attendable representations to mimic explicit reasoning traces. In this work, we evaluate CoTFormer and its structural variants across perplexity and compute efficiency metrics. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19405:end -->

**为什么进入候选分母。** 摘要首要问题为“The CoTFormer architecture formalizes Chain-of-Thought as a form of recurrent latent computation, preserving intermediate states as attendable representations to mimic explicit reasoning traces.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** Furthermore, we extend evaluation to controlled algorithmic settings to determine whether this recurrent framework improves out-of-distribution generalisation on inductive reasoning tasks.

**证据证明什么。** Furthermore, we extend evaluation to controlled algorithmic settings to determine whether this recurrent framework improves out-of-distribution generalisation on inductive reasoning tasks.

**证据没有证明什么。** Repeated latent computation helps on p-hop induction, where the target resembles iterative retrieval, but does not by itself induce robust OOD counting on shifted-start. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19405v1#S2 — 2 Methodology。Evaluation：https://arxiv.org/html/2607.19405v1#S4.SS1 — 4.1 Phase change analysis。Limitations / counterevidence：https://arxiv.org/html/2607.19405v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/COMP6258-Reproducibility-Challenge/CoTFormer, https://github.com/epfml/CoTFormer, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Repeated latent computation helps on p-hop induction, where the target resembles iterative retrieval, but does not by itself induce robust OOD counting on shifted-start.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MODEL-DECODER-ONLY`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19405:end -->

<!-- review:SF-2026-ARXIV-2607-19407:start -->
### ITPEval: Benchmarking Formal Translation Across Interactive Theorem Provers

<!-- claim:SF-2026-ARXIV-2607-19407:start -->Formal theorem proving has emerged as a frontier challenge for machine learning, yet the ecosystem is fragmented: proofs remain siloed across incompatible systems, limiting both training data for learning-based provers and the portability of verified results. We present ITPEval, the first benchmark for evaluating automated formal proof translation across four major ITPs (Lean 4, Rocq, Isabelle, and HOL Light), spanning two distinct logical foundations. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19407:end -->

**为什么进入候选分母。** 摘要首要问题为“Formal theorem proving has emerged as a frontier challenge for machine learning, yet the ecosystem is fragmented: proofs remain siloed across incompatible systems, limiting both training data for learning-based provers and the portability of verified results.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We present ITPEval, the first benchmark for evaluating automated formal proof translation across four major ITPs (Lean 4, Rocq, Isabelle, and HOL Light), spanning two distinct logical foundations.

**证据证明什么。** In addition to pass@k evaluation, a deterministic Lean 4 BEq check establishes equivalence for 54.0% of verified source-to-Lean 4 miniF2F statement translations, showing that native type-checking alone can substantially overestimate semantic fidelity; in an autoformalization/auto-informalization round-trip study, Rocq and HOL Light are easier formalization targets than Lean 4 and Isabelle, while multi-ITP context improves pooled Lean 4 success from 4.8% to 10.6%.

**证据没有证明什么。** F.4 Failure Examples We illustrate three classes of BEq failures from DeepSeek-V4-Pro’s backward-only cases. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19407v1#A4.SS2 — D.2 Cross ITP translation benchmarks and systems; https://arxiv.org/html/2607.19407v1#S3 — 3 Benchmark Design。Evaluation：https://arxiv.org/html/2607.19407v1#S4 — 4 Evaluation and Results; https://arxiv.org/html/2607.19407v1#A1 — Appendix A Full Per-Model Results。Limitations / counterevidence：https://arxiv.org/html/2607.19407v1#A6.SS4 — F.4 Failure Examples; https://arxiv.org/html/2607.19407v1#S4.SS9 — 4.9 Discussion。

**Artifact boundary。** Exact v1 links https://huggingface.co/datasets/jiayi005/ITPEval, https://github.com/lean-dojo/ITPEval, https://github.com/rocq-community/coqtail-math; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：F.4 Failure Examples We illustrate three classes of BEq failures from DeepSeek-V4-Pro’s backward-only cases.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`principle_reuse`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19407:end -->

<!-- review:SF-2026-ARXIV-2607-19408:start -->
### Reward-Aware Population Scaling of Evolutionary Strategies in LLM Fine-Tuning

<!-- claim:SF-2026-ARXIV-2607-19408:start -->Using Evolutionary Strategies (ES) for fine-tuning large language models is attractive because it is memory-efficient, parallel, and compatible with black-box or discrete rewards. Yet its population-size conclusions conflict sharply: fine-tuning with cross-entropy (CE) reward succeeds with $N=1$, while binary-reward training often needs $N \approx 30$. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19408:end -->

**为什么进入候选分母。** 摘要首要问题为“Using Evolutionary Strategies (ES) for fine-tuning large language models is attractive because it is memory-efficient, parallel, and compatible with black-box or discrete rewards.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** Yet its population-size conclusions conflict sharply: fine-tuning with cross-entropy (CE) reward succeeds with $N=1$, while binary-reward training often needs $N \approx 30$.

**证据证明什么。** We show this gap is largely about reward design and normalization, not population size.

**证据没有证明什么。** 5 Discussion and Limitations Practical recommendation: estimate via the zero-training probe (Appendix E ) and start with the smallest that clears it. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19408v1#A1 — Appendix A Algorithmic Conventions: MeZO and ES-at-Scale。Evaluation：https://arxiv.org/html/2607.19408v1#A5 — Appendix E Pre-Training Degeneracy Probe: Protocol and Results; https://arxiv.org/html/2607.19408v1#A5.SS0.SSS0.Px2 — Results.。Limitations / counterevidence：https://arxiv.org/html/2607.19408v1#S5 — 5 Discussion and Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：5 Discussion and Limitations Practical recommendation: estimate via the zero-training probe (Appendix E ) and start with the smallest that clears it.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`TRAIN-PRETRAINING`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19408:end -->

<!-- review:SF-2026-ARXIV-2607-19424:start -->
### JailMeter: An Evidence-Based Evaluation Framework for Jailbreak Attacks on Large Language Models

<!-- claim:SF-2026-ARXIV-2607-19424:start -->The assessment of jailbreak attacks against large language models currently suffers from inconsistent evaluation criteria and methods, leading to unreliable estimates of attack success rates. We propose JailMeter, an evidence-based evaluation framework designed to more faithfully measure jailbreak effectiveness. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19424:end -->

**为什么进入候选分母。** 摘要首要问题为“The assessment of jailbreak attacks against large language models currently suffers from inconsistent evaluation criteria and methods, leading to unreliable estimates of attack success rates.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We propose JailMeter, an evidence-based evaluation framework designed to more faithfully measure jailbreak effectiveness.

**证据证明什么。** JailMeter achieves an accuracy of 97.27%, substantially outperforming existing evaluation methods.

**证据没有证明什么。** We hope our work provide a reliable foundation for future research on jailbreak attack and evaluation. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19424v1#A1.SS3 — A.3 Jailbreak Methods in Jailbreak Attack Dataset; https://arxiv.org/html/2607.19424v1#A3.SS4 — C.4 Model Sensitivity of Various Evaluation Methods。Evaluation：https://arxiv.org/html/2607.19424v1#S5 — 5 Experiments and Analysis; https://arxiv.org/html/2607.19424v1#A3 — Appendix C Supplementary Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.19424v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.19424v1#Sx1 — Limitations。

**Artifact boundary。** Exact v1 links https://github.com/Magi2B0y/JailMeter, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：We hope our work provide a reliable foundation for future research on jailbreak attack and evaluation.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19424:end -->

<!-- review:SF-2026-ARXIV-2607-19430:start -->
### ChannelGuard: Safe Models Do Not Compose into Safe Multi-Agent Systems

<!-- claim:SF-2026-ARXIV-2607-19430:start -->Multi-agent LLM applications chain a planner, worker agents, a verifier, and a synthesizer, and every hop between agents is an unmonitored channel through which an adversary can smuggle instructions. Existing defenses guard only the input boundary (IBProtector, Llama Guard, perplexity filters, SmoothLLM) or run outside the application as opaque, stochastic provider-side filters. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19430:end -->

**为什么进入候选分母。** 摘要首要问题为“Multi-agent LLM applications chain a planner, worker agents, a verifier, and a synthesizer, and every hop between agents is an unmonitored channel through which an adversary can smuggle instructions.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** We present ChannelGuard, a training-free defense-in-depth framework placing information-bottleneck gates on every inter-agent channel; each scores channel text against an adversarial phrase bank by embedding similarity and deterministically passes, compresses, or blocks it, adding no LLM call, while an attribution method records which layer stopped each attack.

**证据证明什么。** We show this gap carries a consequence rarely measured: on a 2,100-trace evaluation across eight attack families, five defenses, and three model backends, an undefended pipeline that appears fully safe under standard reporting (attack success 0.000 on tool- and memory-poisoning) owes that safety almost entirely to the cloud provider's server-side filter (54 of 60 blocks on Azure GPT-5), and silently shifts to the agent model's own alignment on a backend without such a filter.

**证据没有证明什么。** First, an early version of the Azure client silently dropped roughly 12% of a main slice: the reasoning model rejects an explicit zero temperature, and the fallback that removes the parameter did not persist across retries, so a transient-error handler occasionally cycled on what was actually a content-filter rejection and reported it as a bare failure rather than as a provider-filter block. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19430v1#S4 — 4. The ChannelGuard Framework; https://arxiv.org/html/2607.19430v1#A2 — Appendix B The Full Pipeline Algorithm and Three Further Formal Properties。Evaluation：https://arxiv.org/html/2607.19430v1#A6 — Appendix F Gate Ablation; https://arxiv.org/html/2607.19430v1#S5 — 5. Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.19430v1#S7 — 7. Discussion and Limitations; https://arxiv.org/html/2607.19430v1#A15 — Appendix O Reproducibility Notes on Two Failure Modes。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：First, an early version of the Azure client silently dropped roughly 12% of a main slice: the reasoning model rejects an explicit zero temperature, and the fallback that removes the parameter did not persist across retries, so a transient-error handler occasionally cycled on what was actually a content-filter rejection and reported it as a bare failure rather than as a provider-filter block.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-MULTI-AGENT`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19430:end -->

<!-- review:SF-2026-ARXIV-2607-19431:start -->
### BRIM: Workload-Balanced Dual-Sided Bit-Serial Sparse Inference Accelerator

<!-- claim:SF-2026-ARXIV-2607-19431:start -->Bit-serial accelerators exploit bit-level sparsity to reduce DNN inference cost, but existing designs exploit sparsity on only one operand, bounding the speedup. Extending sparsity exploitation to both operands simultaneously yields compounding reductions in partial products but introduces a critical new bottleneck: workload imbalance. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19431:end -->

**为什么进入候选分母。** 摘要首要问题为“Bit-serial accelerators exploit bit-level sparsity to reduce DNN inference cost, but existing designs exploit sparsity on only one operand, bounding the speedup.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** We present BRIM, a hardware - software co-designed dual-sided bit-serial sparse accelerator that directly targets this bottleneck.

**证据证明什么。** Evaluated across CNNs, ViTs, and LLMs under iso-area constraints, BRIM achieves over 90% PE utilization, up to 2.37x speedup, and up to 1.63x energy efficiency improvement over prior dual-sided designs.

**证据没有证明什么。** The key enabler is the product structure of the per-lane cost: CBP operates on one factor offline, slot donation handles residual variance in the other at runtime, and together they recover utilization that neither mechanism could achieve independently. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19431v1#S3 — 3. BRIM Methodology; https://arxiv.org/html/2607.19431v1#S3.SS2 — 3.2. Hardware Architecture。Evaluation：https://arxiv.org/html/2607.19431v1#S4 — 4. Experimental Setup; https://arxiv.org/html/2607.19431v1#S5 — 5. Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.19431v1#S6 — 6. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：The key enabler is the product structure of the per-lane cost: CBP operates on one factor offline, slot donation handles residual variance in the other at runtime, and together they recover utilization that neither mechanism could achieve independently.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-TENSORRT-LLM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19431:end -->

<!-- review:SF-2026-ARXIV-2607-19432:start -->
### ChainWatch: A Kill Chain-Aligned Sequential Detection Framework for Multi-Step Attacks in MCP-Based AI Agent Systems

<!-- claim:SF-2026-ARXIV-2607-19432:start -->The Model Context Protocol (MCP) is an open-source standard that allows AI agents to connect to external tools, databases, and services. While this connectivity enables powerful agent capabilities, it also introduces multi-step attacks that existing per-call defenses cannot reliably detect. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19432:end -->

**为什么进入候选分母。** 摘要首要问题为“The Model Context Protocol (MCP) is an open-source standard that allows AI agents to connect to external tools, databases, and services.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** This paper presents ChainWatch, a sequential detection framework for identifying multi-step attacks in MCP-based AI agent systems.

**证据证明什么。** We demonstrate the approach using five representative attack scenarios from the security literature, showing how ChainWatch detects attack chains that evade traditional per-call security mechanisms.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19432v1#S2.SS1 — II-A MCP Architecture; https://arxiv.org/html/2607.19432v1#S4 — IV ChainWatch Framework。Evaluation：https://arxiv.org/html/2607.19432v1#S3 — III Threat Analysis; https://arxiv.org/html/2607.19432v1#S5 — V Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.19432v1#S3 — III Threat Analysis; https://arxiv.org/html/2607.19432v1#S6 — VI Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-MCP`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19432:end -->

<!-- review:SF-2026-ARXIV-2607-19433:start -->
### The Chronos Vulnerability: A Taxonomy of Temporal Persistence and Memory-Based Deception in Agentic AI

<!-- claim:SF-2026-ARXIV-2607-19433:start -->The transition from stateless generative models in artificial intelligence to stateful, autonomous agents represents an architectural evolution that, while providing the capabilities of long-term planning and the automation of enterprise workflows, also represents the introduction of a new form of security threat, the Chronos Vulnerability. The Chronos Vulnerability represents the threat of memory-based attacks, including the Memory Injection Attack (MINJA) and the sleeper agent, in which the internal belief system of the autonomous agent is compromised, effectively decoupling the attack vector from the final catastrophic event. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19433:end -->

**为什么进入候选分母。** 摘要首要问题为“The transition from stateless generative models in artificial intelligence to stateful, autonomous agents represents an architectural evolution that, while providing the capabilities of long-term planning and the automation of enterprise workflows, also represents the introduction of a new form of security threat, the Chronos Vulnerability.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** The Chronos Vulnerability represents the threat of memory-based attacks, including the Memory Injection Attack (MINJA) and the sleeper agent, in which the internal belief system of the autonomous agent is compromised, effectively decoupling the attack vector from the final catastrophic event.

**证据证明什么。** Consequently, this study synthesizes a defense-in-depth landscape, categorizing emerging frameworks such as diagnostic trajectory guardrails (AgentDoG), formal temporal verification (Agent-C), immunological memory consensus (A-MemGuard), and hardware-anchored trust via GPU-based Trusted Execution Environments (TEEs) and Zero-Trust memory architectures.

**证据没有证明什么。** II-D Threat Model and Adversarial Capabilities To operationalize this cognitive vulnerability into a concrete exploit, it is necessary to define the threat model using various notations from well-established security frameworks like AgentPoison [ 6 ] and Portcullis [ 7 ] . 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19433v1#S2.SS1 — II-A Foundational Architectures: Mapping the BDI Stack; https://arxiv.org/html/2607.19433v1#S3.SS3 — III-C Agent Session Smuggling in Multi-Agent Systems。Evaluation：https://arxiv.org/html/2607.19433v1#S4 — IV Case Study: EchoLeak and Zero-Click Exfiltration。Limitations / counterevidence：https://arxiv.org/html/2607.19433v1#S2.SS4 — II-D Threat Model and Adversarial Capabilities; https://arxiv.org/html/2607.19433v1#S7 — VII Future Directions: Hardware-Anchored Trust。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：II-D Threat Model and Adversarial Capabilities To operationalize this cognitive vulnerability into a concrete exploit, it is necessary to define the threat model using various notations from well-established security frameworks like AgentPoison [ 6 ] and Portcullis [ 7 ] .

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19433:end -->

<!-- review:SF-2026-ARXIV-2607-19438:start -->
### BaseRT: Advancing Best-in-Class LLM Inference with Apple M5 Neural Accelerators

<!-- claim:SF-2026-ARXIV-2607-19438:start -->Apple's M5 generation introduces a redesigned GPU architecture in which every core carries a dedicated Neural Accelerator: on-die matrix units exposed through the Metal~4 tensor API. We show that BaseRT, our native Metal inference runtime for large language models on Apple Silicon, exploits these units to push inference throughput on Apple hardware substantially beyond both llama.cpp and MLX. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19438:end -->

**为什么进入候选分母。** 摘要首要问题为“Apple's M5 generation introduces a redesigned GPU architecture in which every core carries a dedicated Neural Accelerator: on-die matrix units exposed through the Metal~4 tensor API.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** Building on BaseRT's framework-free design, we add a family of hand-written Metal~4 tensor-core kernels (including dense and mixture-of-experts GEMM and flash-attention prefill kernels) that route the compute-bound matrix multiplications of inference through the M5 Neural Accelerators while leaving the memory-bound decode path on our existing specialised kernels.

**证据证明什么。** These results establish a new performance ceiling for on-device LLM inference and show that the M5's tensor cores are the decisive lever for prompt processing on Apple Silicon.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19438v1#S1 — 1 Introduction; https://arxiv.org/html/2607.19438v1#S1.SS1 — 1.1 Contributions。Evaluation：https://arxiv.org/html/2607.19438v1#S4 — 4 Evaluation; https://arxiv.org/html/2607.19438v1#S4.SS1 — 4.1 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.19438v1#S4.SS4 — 4.4 Discussion of Results; https://arxiv.org/html/2607.19438v1#S5 — 5 Discussion。

**Artifact boundary。** Exact v1 links https://github.com/basecompute/baseRT, https://github.com/ggml-org/llama.cpp, https://github.com/ml-explore/mlx; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-TENSORRT-LLM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19438:end -->

<!-- review:SF-2026-ARXIV-2607-19442:start -->
### Unlearning as Distribution Restoration: A Controlled Counterfactual Study, a Validated Selective Screen, and the Limits of Oracle-Free Certification

<!-- claim:SF-2026-ARXIV-2607-19442:start -->Machine unlearning is commonly evaluated by matching a retrained oracle on trained probes. In a controlled nonce-fact testbed with a matched retraining reference, we find this criterion can favor methods that retain held-out knowledge: candidates it rates adequate score held-out forget facts $-2.82$ nats below the never-learned level (cluster CI $[-3.16,-2.48]$). 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19442:end -->

**为什么进入候选分母。** 摘要首要问题为“Machine unlearning is commonly evaluated by matching a retrained oracle on trained probes.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** A fixed-magnitude logit-suppression attack defeats the full forward battery in 12/45 cells, so forward-only certification is not sound; our method is an empirical selective test for methods-as-produced.

**证据证明什么。** In a controlled nonce-fact testbed with a matched retraining reference, we find this criterion can favor methods that retain held-out knowledge: candidates it rates adequate score held-out forget facts $-2.82$ nats below the never-learned level (cluster CI $[-3.16,-2.48]$).

**证据没有证明什么。** And the boundary is quantified rather than assumed: a fixed-magnitude suppression attack defeats this forward-only battery in a quarter of cells, which is the empirical face of the identifiability and finite-query limits that scope oracle-free selection. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19442v1#A2 — Appendix B Methods and Hyperparameters。Evaluation：https://arxiv.org/html/2607.19442v1#S1 — 1 Introduction; https://arxiv.org/html/2607.19442v1#S2 — 2 Controlled Testbed with a Matched Retraining Reference。Limitations / counterevidence：https://arxiv.org/html/2607.19442v1#S11 — 11 Limitations; https://arxiv.org/html/2607.19442v1#S12 — 12 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：And the boundary is quantified rather than assumed: a fixed-magnitude suppression attack defeats this forward-only battery in a quarter of cells, which is the empirical face of the identifiability and finite-query limits that scope oracle-free selection.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19442:end -->

<!-- review:SF-2026-ARXIV-2607-19449:start -->
### Guardrails as Scapegoats: Auditing Unfaithful Safety Refusals in Tool-Augmented LLM Agents

<!-- claim:SF-2026-ARXIV-2607-19449:start -->Evaluation frameworks for tool-augmented LLM agents focus overwhelmingly on capability metrics or explicit tool crashes, leaving silent infrastructure failures and HTTP 200 responses with empty, null, or malformed payloads largely unaudited. We introduce a lightweight black-box auditing framework that injects four silent failure profiles across 12 production-adjacent tool stubs and classifies agent responses into three mutually exclusive behavioral classes: Honest Surrender (HSR), Fabrication (FAR), and Unfaithful Safety Refusal (USR). 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19449:end -->

**为什么进入候选分母。** 摘要首要问题为“Evaluation frameworks for tool-augmented LLM agents focus overwhelmingly on capability metrics or explicit tool crashes, leaving silent infrastructure failures and HTTP 200 responses with empty, null, or malformed payloads largely unaudited.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** We introduce a lightweight black-box auditing framework that injects four silent failure profiles across 12 production-adjacent tool stubs and classifies agent responses into three mutually exclusive behavioral classes: Honest Surrender (HSR), Fabrication (FAR), and Unfaithful Safety Refusal (USR).

**证据证明什么。** Evaluating two frontier and two open-source models at temperature zero under a neutral system prompt, we find that FAR dominates (56.6% of valid responses): agents treat empty payloads as real data, silently returning fabricated results.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19449v1#S3.SS3 — 3.3. Prompt Design; https://arxiv.org/html/2607.19449v1#S6 — 6. Ablation: Effect of Safety-Framed System Prompt。Evaluation：https://arxiv.org/html/2607.19449v1#S3 — 3. Experimental Setup; https://arxiv.org/html/2607.19449v1#S4 — 4. Results。Limitations / counterevidence：https://arxiv.org/html/2607.19449v1#S3.SS2 — 3.2. Failure Injection; https://arxiv.org/html/2607.19449v1#S4.SS2 — 4.2. Breakdown by Failure Type。

**Artifact boundary。** Exact v1 links https://github.com/langchain-ai/langchain, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-TOOL-CALLING`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19449:end -->

<!-- review:SF-2026-ARXIV-2607-19450:start -->
### REGEN: Replay-recycling for Expert-to-Generalist distillation with Offline Reinforcement Learning

<!-- claim:SF-2026-ARXIV-2607-19450:start -->Large-scale online reinforcement learning (RL) is the predominant means of eliciting advanced abilities including long-term reasoning and agentic tool use in large language models (LLMs). However, continuing to scale it across vast task domains of interest remains challenging in both computational infrastructure and cost, especially when considering RL as merely a one-off learning stage. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19450:end -->

**为什么进入候选分母。** 摘要首要问题为“Large-scale online reinforcement learning (RL) is the predominant means of eliciting advanced abilities including long-term reasoning and agentic tool use in large language models (LLMs).”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** To address these challenges, we propose REGEN: Replay-recycling for Expert-to-Generalist Distillation with Offline RL.

**证据证明什么。** REGEN completely decouples the rollout sampling from the backward training process and thus greatly reduces the training cost.

**证据没有证明什么。** Our work effectively demonstrates the potential of reusing replay memory; however, the optimal strategy for leveraging this resource remains an open question worthy of deeper investigation. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19450v1#A2 — Appendix B Reward Design Across Domains; https://arxiv.org/html/2607.19450v1#S3 — 3 Methodology。Evaluation：https://arxiv.org/html/2607.19450v1#S4.SS3 — 4.3 Ablations and Analysis; https://arxiv.org/html/2607.19450v1#A1 — Appendix A Other Evaluation Criteria。Limitations / counterevidence：https://arxiv.org/html/2607.19450v1#S5 — 5 Conclusion and Discussion。

**Artifact boundary。** Exact v1 links https://huggingface.co/datasets/HuggingFaceH4/ifeval-like-data, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Our work effectively demonstrates the potential of reusing replay memory; however, the optimal strategy for leveraging this resource remains an open question worthy of deeper investigation.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-RLHF`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19450:end -->

<!-- review:SF-2026-ARXIV-2607-19456:start -->
### MoA-Structured Decode Attention DNF Derivation, KV-Cache Accumulation, GQA/MQA, and OpenACC Kernel

<!-- claim:SF-2026-ARXIV-2607-19456:start -->We derive four memory-optimal inference artifacts for transformer attention using the Mathematics of Arrays (MoA), each following directly from the forward-pass Denotational Normal Form (DNF) of with the query-row index fixed to the current decode step. All programs are verified against PyTorch scaled_dot_product_attention. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19456:end -->

**为什么进入候选分母。** 摘要首要问题为“We derive four memory-optimal inference artifacts for transformer attention using the Mathematics of Arrays (MoA), each following directly from the forward-pass Denotational Normal Form (DNF) of with the query-row index fixed to the current decode step.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** All programs are verified against PyTorch scaled_dot_product_attention.

**证据证明什么。** All programs are verified against PyTorch scaled_dot_product_attention.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19456v1#S3 — 3 Python Implementation; https://arxiv.org/html/2607.19456v1#S3.SSx2 — MoA - Based Implementation。Evaluation：https://arxiv.org/html/2607.19456v1#S1 — 1 Introduction; https://arxiv.org/html/2607.19456v1#S1.SS1 — 1.1 Background。Limitations / counterevidence：https://arxiv.org/html/2607.19456v1#S8 — 8 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`INFER-DECODE`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19456:end -->

<!-- review:SF-2026-ARXIV-2607-19490:start -->
### Integrity of peer-to-peer distributed LLM inference under malicious nodes

<!-- claim:SF-2026-ARXIV-2607-19490:start -->Peer-to-peer distributed inference executes a Large Language Model (LLM) on pooled consumer hardware by spreading its layers across many nodes. Every request passes through nodes that are owned and controlled by multiple independent parties. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19490:end -->

**为什么进入候选分母。** 摘要首要问题为“Peer-to-peer distributed inference executes a Large Language Model (LLM) on pooled consumer hardware by spreading its layers across many nodes.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** In this paper, we propose a method that checks the output integrity by measuring the variation in the activations that each node passes to the next.

**证据证明什么。** We study 408 configurations with metrics and success criteria fixed before any experiment ran; the detector reaches AUROC 1.0, correctly ranking the malicious shard above every benign shard on every canary in every configuration.

**证据没有证明什么。** We assume the adversary observes , knows , tampers on every query including canaries, but cannot distinguish a canary from a real query at serving time and so cannot selectively spare the canaries. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19490v1#S3 — 3 Method; https://arxiv.org/html/2607.19490v1#S4.SS4 — 4.4 Experimental design。Evaluation：https://arxiv.org/html/2607.19490v1#S5 — 5 Experimental Results; https://arxiv.org/html/2607.19490v1#S4 — 4 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.19490v1#S6 — 6 Limitations and Future Work; https://arxiv.org/html/2607.19490v1#S3.SS2 — 3.2 Threat model。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：We assume the adversary observes , knows , tampers on every query including canaries, but cannot distinguish a canary from a real query at serving time and so cannot selectively spare the canaries.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19490:end -->

<!-- review:SF-2026-ARXIV-2607-19515:start -->
### BLUE: Semantics-Preserving Video Compression for Efficient Vision-Language Surveillance Analytics

<!-- claim:SF-2026-ARXIV-2607-19515:start -->Continuous surveillance video creates a growing storage, transmission, and inference burden for enterprise video analytics systems. While modern codecs such as H.265 reduce bitrate for human-viewable video, aggressive compression can degrade downstream computer-vision performance and does not necessarily reduce the number of vision-language model (VLM) inference calls required for semantic video understanding. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19515:end -->

**为什么进入候选分母。** 摘要首要问题为“Continuous surveillance video creates a growing storage, transmission, and inference burden for enterprise video analytics systems.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** Continuous surveillance video creates a growing storage, transmission, and inference burden for enterprise video analytics systems.

**证据证明什么。** The results show no measurable degradation in semantic inference quality.

**证据没有证明什么。** The results also show that BLUE’s compression benefit is not obtained at the expense of machine perception. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19515v1#S2 — 2. Methodology。Evaluation：https://arxiv.org/html/2607.19515v1#S2.SS4 — 2.4. Metrics and P-Frame Analysis; https://arxiv.org/html/2607.19515v1#S3 — 3. Results and Discussion。Limitations / counterevidence：https://arxiv.org/html/2607.19515v1#S3 — 3. Results and Discussion; https://arxiv.org/html/2607.19515v1#S4 — 4. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：The results also show that BLUE’s compression benefit is not obtained at the expense of machine perception.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-REPRESENTATION`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19515:end -->

<!-- review:SF-2026-ARXIV-2607-19523:start -->
### When Reasoning Narrows the Move: Diversity Collapse in LLM Game Play

<!-- claim:SF-2026-ARXIV-2607-19523:start -->Supervised fine-tuning (SFT) is widely used to adapt large language models to downstream tasks, but its effect on behavioral diversity in sequential decision-making remains under-explored. We study this question in a controlled suite of deterministic board games based on tic-tac-toe variants, where optimal actions are exactly computable and diversity can be measured directly. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19523:end -->

**为什么进入候选分母。** 摘要首要问题为“Supervised fine-tuning (SFT) is widely used to adapt large language models to downstream tasks, but its effect on behavioral diversity in sequential decision-making remains under-explored.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We study this question in a controlled suite of deterministic board games based on tic-tac-toe variants, where optimal actions are exactly computable and diversity can be measured directly.

**证据证明什么。** We then show that action augmentation, which trains on all optimal actions per state rather than a single demonstrated action, would partially mitigates this effect.

**证据没有证明什么。** Our study is limited to small deterministic games and a single main model family. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19523v1#A1 — Appendix A Implementation Details。Evaluation：https://arxiv.org/html/2607.19523v1#S4 — 4 Main Experiments: Policy Evaluation and Game-Playing; https://arxiv.org/html/2607.19523v1#A2 — Appendix B Additional Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.19523v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Our study is limited to small deterministic games and a single main model family.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`WORLDVIEW-LLM-INTELLIGENCE`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19523:end -->

<!-- review:SF-2026-ARXIV-2607-19539:start -->
### Fine-grained Computation-Communication Overlap via Tile-level Signaling and Scheduling for Mixture-of-Experts

<!-- claim:SF-2026-ARXIV-2607-19539:start -->Mixture-of-Experts (MoE) architectures increase model capacity without proportionally increasing computation cost and have become a key building block for scaling large language models (LLMs) to trillion-parameter regimes. Efficient deployment of these MoE models relies on distributed execution across multiple GPUs, where each MoE layer involves two all-to-all communications: dispatching tokens to expert ranks and returning the expert outputs to their source ranks. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19539:end -->

**为什么进入候选分母。** 摘要首要问题为“Mixture-of-Experts (MoE) architectures increase model capacity without proportionally increasing computation cost and have become a key building block for scaling large language models (LLMs) to trillion-parameter regimes.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** We present a fine-grained approach that overlaps expert compute with the second all-to-all via tile-level signaling and scheduling.

**证据证明什么。** On a 4-A100 GPU platform, evaluated on three MoE models against four state-of-the-art MoE systems, our approach achieves up to 2.64x end-to-end speedup and 2.74x MoE-layer speedup.

**证据没有证明什么。** Future work includes extension to the backward pass for training, adaptive SM partition selection, support for additional parallelism regimes, and deployment on larger machines. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19539v1#S3 — 3. System Design; https://arxiv.org/html/2607.19539v1#S2.SS1 — 2.1. Mixture-of-Experts Architectures。Evaluation：https://arxiv.org/html/2607.19539v1#S4 — 4. Experimental Results; https://arxiv.org/html/2607.19539v1#S4.SS1 — 4.1. Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.19539v1#S6 — 6. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/NVIDIA/cutlass, https://github.com/fanshiqing/grouped_gemm, https://github.com/NVIDIA/TransformerEngine; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：Future work includes extension to the backward pass for training, adaptive SM partition selection, support for additional parallelism regimes, and deployment on larger machines.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MODEL-MOE`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19539:end -->

<!-- review:SF-2026-ARXIV-2607-19547:start -->
### ChronoStitch: Training-Free Composition of Visual KV Memories for Long-Horizon Temporal Reasoning

<!-- claim:SF-2026-ARXIV-2607-19547:start -->Long-video question answering requires a model to preserve visual evidence over time without repeatedly reprocessing the same video. A practical approach is to store the vision-language model's internal key-value (KV) cache for each video chunk and retrieve that state at query time. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19547:end -->

**为什么进入候选分母。** 摘要首要问题为“Long-video question answering requires a model to preserve visual evidence over time without repeatedly reprocessing the same video.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** The method first re-bases stored post-rotary keys onto a global three-axis multimodal RoPE coordinate system that preserves time, height, and width structure.

**证据证明什么。** We show why a one-dimensional scalar re-indexing is geometrically inconsistent for visual tokens because it turns spatial order within a frame into false temporal displacement.

**证据没有证明什么。** The independently stored chunks did not observe earlier chunks during their original computation, so no rotation of keys alone can recreate the missing content. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19547v1#S2 — 2 Methodology。Evaluation：https://arxiv.org/html/2607.19547v1#S3 — 3 Results and Discussion。Limitations / counterevidence：https://arxiv.org/html/2607.19547v1#S3 — 3 Results and Discussion; https://arxiv.org/html/2607.19547v1#S4 — 4 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：The independently stored chunks did not observe earlier chunks during their original computation, so no rotation of keys alone can recreate the missing content.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19547:end -->

<!-- review:SF-2026-ARXIV-2607-19592:start -->
### Knowledge-Centric Self-Improvement

<!-- claim:SF-2026-ARXIV-2607-19592:start -->Self-improving AI systems typically treat the agent as the object that improves, by optimizing prompts, workflows, harnesses, or even the agent's own code. This agent-centric view can make improvements expensive to maintain and difficult to transfer, because gains become tied to a particular agent design, task distribution, or adaptation run. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19592:end -->

**为什么进入候选分母。** 摘要首要问题为“Self-improving AI systems typically treat the agent as the object that improves, by optimizing prompts, workflows, harnesses, or even the agent's own code.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** These results support a new view of self-improving agentic systems: progress can be driven primarily by the curated persistent knowledge.

**证据证明什么。** These results support a new view of self-improving agentic systems: progress can be driven primarily by the curated persistent knowledge.

**证据没有证明什么。** Extending the protocol to incorporate human-expert contributions, which we did not study in this paper, is another natural direction. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19592v1#S3.SS1 — 3.1 System Overview。Evaluation：https://arxiv.org/html/2607.19592v1#A11 — Appendix K Benchmark Details; https://arxiv.org/html/2607.19592v1#A4 — Appendix D Prompts by Benchmark。Limitations / counterevidence：https://arxiv.org/html/2607.19592v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/recursive-knowledge/KSI, https://github.com/block/goose, https://github.com/krafton-ai/KIRA; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Extending the protocol to incorporate human-expert contributions, which we did not study in this paper, is another natural direction.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-REFLECTION`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19592:end -->

<!-- review:SF-2026-ARXIV-2607-19595:start -->
### Twin Agent: Context Residual Compression for Privilege Separated Agents

<!-- claim:SF-2026-ARXIV-2607-19595:start -->Large language model (LLM) agents are vulnerable to security risks, such as prompt injection attacks from untrusted context that manipulate downstream reasoning and tool use. Existing secure-by-design approaches mitigate this risk by separating untrusted observations from privileged execution and careful control of information flow, but often degrade utility and require extensive task-specific engineering. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19595:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language model (LLM) agents are vulnerable to security risks, such as prompt injection attacks from untrusted context that manipulate downstream reasoning and tool use.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** Existing secure-by-design approaches mitigate this risk by separating untrusted observations from privileged execution and careful control of information flow, but often degrade utility and require extensive task-specific engineering.

**证据证明什么。** This design reduces the information needed to preserve task utility and thus achieves a better security--utility tradeoff, which we empirically verify by measuring how utility and attack success change as the length of hints varies.

**证据没有证明什么。** Instead of exposing a privileged agent to raw untrusted context or forcing a rigid plan-first workflow, Twin Agent separates exploration from execution and allows the Explore Agent to send only compact hints to the Safe Agent. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19595v1#A4 — Appendix D SWE-agent system prompts; https://arxiv.org/html/2607.19595v1#S3 — 3 Methodology。Evaluation：https://arxiv.org/html/2607.19595v1#S5.SS2 — 5.2 Main Results Across Benchmarks; https://arxiv.org/html/2607.19595v1#A1 — Appendix A Implementation of the guardrails and ablation study。Limitations / counterevidence：https://arxiv.org/html/2607.19595v1#A6 — Appendix F Failure case study; https://arxiv.org/html/2607.19595v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Instead of exposing a privileged agent to raw untrusted context or forcing a rigid plan-first workflow, Twin Agent separates exploration from execution and allows the Explore Agent to send only compact hints to the Safe Agent.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-PLATFORM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19595:end -->

<!-- review:SF-2026-ARXIV-2607-19604:start -->
### Scaling Laws for Hypernetwork-Based Knowledge Injection in Large Language Models

<!-- claim:SF-2026-ARXIV-2607-19604:start -->Injecting factual knowledge into large language models (LLMs) reliably and at scale remains an open challenge. Hypernetworks provide a promising solution to large-scale knowledge injection. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19604:end -->

**为什么进入候选分母。** 摘要首要问题为“Injecting factual knowledge into large language models (LLMs) reliably and at scale remains an open challenge.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** Our results reveal: (i) hypernetwork-based injection exhibits broadly predictive power law scaling along all architecture axes; and (ii) hypernetworks are capable of reliable OOD generalization at increasing scales, suggesting that hypernetwork provides a promising alternative to other train-time adaptation methods such as LoRA finetuning and full fine-tuning, exhibiting steeper scaling exponents in all OOD evaluations.

**证据证明什么。** Together, these results establish hypernetworks as a principled and scalable substrate for train-time adaptation, and provide the first empirically grounded scaling laws to guide hypernetworks for factual reasoning in large language models.

**证据没有证明什么。** This parameter overhead significantly limits the practical deployability of large hypernetworks and motivates future work on more parameter-efficient hypernetwork architectures, such as shared weight generation across layers, low-rank hypernetwork designs, or distillation of large hypernetworks into smaller ones after training. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19604v1#A4 — Appendix D Hypernetwork Architecture Details; https://arxiv.org/html/2607.19604v1#A4.SS2 — D.2 Encoder Architecture。Evaluation：https://arxiv.org/html/2607.19604v1#S3.SS3 — 3.3 Evaluation Protocol and OOD Splits; https://arxiv.org/html/2607.19604v1#S5 — 5 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.19604v1#S6 — 6 Conclusion and Future Work。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：This parameter overhead significantly limits the practical deployability of large hypernetworks and motivates future work on more parameter-efficient hypernetwork architectures, such as shared weight generation across layers, low-rank hypernetwork designs, or distillation of large hypernetworks into smaller ones after training.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-PRETRAINING`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19604:end -->

<!-- review:SF-2026-ARXIV-2607-19608:start -->
### Task Competence Is Not Instruction Following: Evaluating Instruction-Conflicting Behavior in Small Language Models

<!-- claim:SF-2026-ARXIV-2607-19608:start -->Instruction tuning is meant to make language models follow user requests, yet it is unclear whether small models comply when an instruction conflicts with their usual task behavior. We study this across three tasks - multiple-choice question answering (MCQA), sentiment classification, and mathematical question answering - by pairing a standard instruction with a conflicting non-standard one (select an incorrect option, output the opposite sentiment, or return twice the answer). 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19608:end -->

**为什么进入候选分母。** 摘要首要问题为“Instruction tuning is meant to make language models follow user requests, yet it is unclear whether small models comply when an instruction conflicts with their usual task behavior.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We study this across three tasks - multiple-choice question answering (MCQA), sentiment classification, and mathematical question answering - by pairing a standard instruction with a conflicting non-standard one (select an incorrect option, output the opposite sentiment, or return twice the answer).

**证据证明什么。** Small models stay competent yet routinely ignore the non-standard instruction, while larger models show a clear gap between the two settings.

**证据没有证明什么。** Scale therefore narrows the gap between task competence and instruction following, and instruction-tuned models should be evaluated not only on whether they know the answer, but on whether they follow the requested behavior. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19608v1#S4.SS4 — 4.4 Prompt Design; https://arxiv.org/html/2607.19608v1#S4.SS1 — 4.1 Models。Evaluation：https://arxiv.org/html/2607.19608v1#A1 — Appendix A Experimental Details; https://arxiv.org/html/2607.19608v1#A2 — Appendix B Prompt-Variant Results。Limitations / counterevidence：https://arxiv.org/html/2607.19608v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.19608v1#Sx1 — Limitations。

**Artifact boundary。** Exact v1 links https://github.com/farajimahdieh/language-model-task-competence-vs-instruction-following, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Scale therefore narrows the gap between task competence and instruction following, and instruction-tuned models should be evaluated not only on whether they know the answer, but on whether they follow the requested behavior.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19608:end -->

<!-- review:SF-2026-ARXIV-2607-19616:start -->
### The Mechanism Matters: When Knowledge Graphs Help Reinforcement Learning

<!-- claim:SF-2026-ARXIV-2607-19616:start -->Knowledge graphs (KGs) are widely used to inject prior knowledge into reinforcement learning (RL), yet the literature is dominated by single-domain, positive-result method papers, so we lack a systematic account of when KG structure helps an agent, when it is neutral, and when it hurts. We conduct a controlled study that independently varies the RL task, the injection mechanism (state features, action masking, or potential-based reward shaping), and KG quality. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19616:end -->

**为什么进入候选分母。** 摘要首要问题为“Knowledge graphs (KGs) are widely used to inject prior knowledge into reinforcement learning (RL), yet the literature is dominated by single-domain, positive-result method papers, so we lack a systematic account of when KG structure helps an agent, when it is neutral, and when it hurts.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** Knowledge graphs (KGs) are widely used to inject prior knowledge into reinforcement learning (RL), yet the literature is dominated by single-domain, positive-result method papers, so we lack a systematic account of when KG structure helps an agent, when it is neutral, and when it hurts.

**证据证明什么。** Our results give practitioners concrete guidance on how, and how much, to trust a KG when using it to guide RL.

**证据没有证明什么。** Second, prefer soft, optimality-preserving injection (reward shaping) when the KG may be incomplete or noisy, since it cannot change the optimal policy and a wrong KG is at worst neutral for a sufficiently robust learner. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19616v1#S4 — 4 Method; https://arxiv.org/html/2607.19616v1#S4.SSx4 — Study Design。Evaluation：https://arxiv.org/html/2607.19616v1#S5 — 5 Experimental Setup; https://arxiv.org/html/2607.19616v1#S6 — 6 Results。Limitations / counterevidence：https://arxiv.org/html/2607.19616v1#S8 — 8 Discussion; https://arxiv.org/html/2607.19616v1#S9 — 9 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Second, prefer soft, optimality-preserving injection (reward shaping) when the KG may be incomplete or noisy, since it cannot change the optimal policy and a wrong KG is at worst neutral for a sufficiently robust learner.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-GRPO`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19616:end -->

<!-- review:SF-2026-ARXIV-2607-19623:start -->
### From Bit-Position Sensitivity to Unequal Error Protection for DNN Inference Memory

<!-- claim:SF-2026-ARXIV-2607-19623:start -->We characterize per-bit-position fault sensitivity in ML inference across 16 workloads -- spanning transformer-based models and attention-free CNNs -- and across three floating-point formats. Our central empirical finding is a sharp bit-sensitivity transition: flipping any of the least-significant fraction bits up to a data-type-specific threshold, Xsafe, degrades task metrics by less than 1% under deterministic single-bit stress tests. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19623:end -->

**为什么进入候选分母。** 摘要首要问题为“We characterize per-bit-position fault sensitivity in ML inference across 16 workloads -- spanning transformer-based models and attention-free CNNs -- and across three floating-point formats.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** Our central empirical finding is a sharp bit-sensitivity transition: flipping any of the least-significant fraction bits up to a data-type-specific threshold, Xsafe, degrades task metrics by less than 1% under deterministic single-bit stress tests.

**证据证明什么。** The codec reduces ECC area by 27.8% relative to uniform SECDED; dual-voltage operation of the non-critical partition lowers gross BF16 read energy by about 17%, with a roughly 4% dual-partition macro-area overhead.

**证据没有证明什么。** Three limitations remain: synthetic plus bounded-neighborhood injection only partially captures field-correlated fault processes ( Sullivan et al., 2021 ; Meza et al., 2015 ; Sridharan et al., 2015 ; Alam and Gupta, 2022 ) , the study does not yet include a full accelerator prototype with the selective-ECC controller in the execution loop, and dual-voltage SRAM integration is constrained by bank-level partition granularity, rail-switch latency, and physical-routing overhead. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19623v1#S5 — 5. Hardware Architecture: Unequal Error Protection for ML Inference; https://arxiv.org/html/2607.19623v1#S6 — 6. Design Space Exploration and Reliability。Evaluation：https://arxiv.org/html/2607.19623v1#S3 — 3. Fault modeling and experimental setup; https://arxiv.org/html/2607.19623v1#S4 — 4. Bit-Position Sensitivity Results。Limitations / counterevidence：https://arxiv.org/html/2607.19623v1#S7 — 7. Discussion, Limitations, and Future Work; https://arxiv.org/html/2607.19623v1#S8 — 8. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：Three limitations remain: synthetic plus bounded-neighborhood injection only partially captures field-correlated fault processes ( Sullivan et al., 2021 ; Meza et al., 2015 ; Sridharan et al., 2015 ; Alam and Gupta, 2022 ) , the study does not yet include a full accelerator prototype with the selective-ECC controller in the execution loop, and dual-voltage SRAM integration is constrained by bank-level partition granularity, rail-switch latency, and physical-routing overhead.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-GPU-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19623:end -->

<!-- review:SF-2026-ARXIV-2607-19629:start -->
### Adaptive Capitulation: A Structural Failure Mode of LLM Responses in Vulnerability Contexts

<!-- claim:SF-2026-ARXIV-2607-19629:start -->Large language models operating in emotionally sensitive contexts face a structural trilemma: when users in vulnerable states request information that may reinforce maladaptive attribution, current response architectures resolve the tension through protective restriction, uninflected facilitation, or unintegrated co-presence of both imperatives -- each preserving one objective at the cost of the other. Administering a three-turn escalating vulnerability vignette to three commercial LLMs (900 sessions across material, relational, and somatic status-proxy variants) and coding responses with two binary indices (VCC/VCI), we characterize a previously undocumented failure mode we term adaptive capitulation: the model validates the social injustice underlying the user's distress before pivoting to detailed facilitation of the very acquisition it nominally discouraged. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19629:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language models operating in emotionally sensitive contexts face a structural trilemma: when users in vulnerable states request information that may reinforce maladaptive attribution, current response architectures resolve the tension through protective restriction, uninflected facilitation, or unintegrated co-presence of both imperatives -- each preserving one objective at the cost of the other.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** Administering a three-turn escalating vulnerability vignette to three commercial LLMs (900 sessions across material, relational, and somatic status-proxy variants) and coding responses with two binary indices (VCC/VCI), we characterize a previously undocumented failure mode we term adaptive capitulation: the model validates the social injustice underlying the user's distress before pivoting to detailed facilitation of the very acquisition it nominally discouraged.

**证据证明什么。** We show that the trilemma is structural rather than incidental, and propose Minimal Reattributive Sufficiency (MRS), an architecture-neutral design principle that embeds a single reattributive cue within an otherwise validating response, preserving a pathway toward autonomous reattribution without contesting the user's stated goal.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19629v1#Sx10.SSx2 — Design Properties; https://arxiv.org/html/2607.19629v1#Sx2.SSx1 — Paternalism–Autonomy Tradeoffs in AI Design。Evaluation：https://arxiv.org/html/2607.19629v1#Sx3.SSx1 — Experimental Setup; https://arxiv.org/html/2607.19629v1#Sx3.SSx4 — Analysis Procedure。Limitations / counterevidence：https://arxiv.org/html/2607.19629v1#Sx5.SSx1 — Limitations and Future Work; https://arxiv.org/html/2607.19629v1#Sx6 — Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19629:end -->

<!-- review:SF-2026-ARXIV-2607-19638:start -->
### Do Co-Located AI Training Jobs Synchronize? Load-Dependent Throttling as a Coupling Mechanism for Phase-Locking Behind a Shared Power Cap

<!-- claim:SF-2026-ARXIV-2607-19638:start -->Large-scale AI training turns computing facilities into multi-megawatt loads whose power draw is periodic: tens of thousands of accelerators step in lockstep between compute-bound phases near peak power and communication-bound phases where they idle. Prior work treats each facility as an exogenous periodic forcing on the grid. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19638:end -->

**为什么进入候选分母。** 摘要首要问题为“Large-scale AI training turns computing facilities into multi-megawatt loads whose power draw is periodic: tens of thousands of accelerators step in lockstep between compute-bound phases near peak power and communication-bound phases where they idle.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** Formalizing the fleet as a generalized Kuramoto system, we obtain three operator-facing statements.

**证据证明什么。** The prediction is falsifiable by a two-job co-capped measurement, which we specify.

**证据没有证明什么。** Answering it required identifying the physical coupling, which is neither grid frequency (the clocks are decoupled) nor a common forcing (which cannot break symmetry), but load-dependent throttling gated by each job’s own compute phase. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19638v1#S3.SS4 — 3.4 Reduction to a generalized Kuramoto system。Evaluation：https://arxiv.org/html/2607.19638v1#S4 — 4 Analysis; https://arxiv.org/html/2607.19638v1#S6 — 6 Numerical study。Limitations / counterevidence：https://arxiv.org/html/2607.19638v1#S7 — 7 Discussion; https://arxiv.org/html/2607.19638v1#S8 — 8 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：Answering it required identifying the physical coupling, which is neither grid frequency (the clocks are decoupled) nor a common forcing (which cannot break symmetry), but load-dependent throttling gated by each job’s own compute phase.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-GPU-SCHEDULER`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19638:end -->

<!-- review:SF-2026-ARXIV-2607-19653:start -->
### PerfAgent: Profiler-Guided Iterative Refinement for Repository-Level Code Optimization

<!-- claim:SF-2026-ARXIV-2607-19653:start -->Large language model (LLM) agents now perform well on correctness-oriented repository-level tasks, including SWE-Bench issue resolution and feature implementation in real codebases. However, they still struggle with repository-level code optimization, which requires preserving behavior while improving runtime performance. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19653:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language model (LLM) agents now perform well on correctness-oriented repository-level tasks, including SWE-Bench issue resolution and feature implementation in real codebases.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We present PerfAgent, a profiler-guided, verifier-in-the-loop workflow that gives an off-the-shelf coding agent the feedback needed to find real hotspots, improve beyond the first passing patch, and use profiler evidence rather than timing alone to decide what to optimize next.

**证据证明什么。** It also surpasses an oracle best-of-five baseline at substantially lower cost, showing that the gains come from better feedback rather than additional test-time sampling.

**证据没有证明什么。** Our findings span two benchmarks, roughly a dozen Python-centric repositories, two models (GPT-5.1 and Kimi-K2), and a single base harness (Mini-SWE-Agent), and may not transfer to other languages, models, or harnesses; although PerfAgent is harness-independent by construction, we have not measured its gains on OpenHands or Codex. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19653v1#S1 — I Introduction; https://arxiv.org/html/2607.19653v1#S2 — II Benchmarks Overview。Evaluation：https://arxiv.org/html/2607.19653v1#A4 — Appendix D Manual Review of Per-Task Win/Loss Analysis; https://arxiv.org/html/2607.19653v1#S2 — II Benchmarks Overview。Limitations / counterevidence：https://arxiv.org/html/2607.19653v1#S7 — VII Conclusion and Future Work; https://arxiv.org/html/2607.19653v1#S6 — VI Threats to Validity。

**Artifact boundary。** Exact v1 links https://github.com/openai/codex, https://github.com/benfred/py-spy, https://huggingface.co/moonshotai/Kimi-K2-Instruct; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Our findings span two benchmarks, roughly a dozen Python-centric repositories, two models (GPT-5.1 and Kimi-K2), and a single base harness (Mini-SWE-Agent), and may not transfer to other languages, models, or harnesses; although PerfAgent is harness-independent by construction, we have not measured its gains on OpenHands or Codex.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-REFLECTION`；evidence-stage relation：`principle_reuse`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19653:end -->

<!-- review:SF-2026-ARXIV-2607-19670:start -->
### Same Game, Different Story: A Minimal Conservative Strategic Robustness Benchmark for Large Language Model Agents

<!-- claim:SF-2026-ARXIV-2607-19670:start -->Large language model (LLM) agents increasingly operate in strategic settings where outcomes depend on the actions of other agents. This raises a reliability question: will a model choose consistently when the same incentives are presented through different narratives? 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19670:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language model (LLM) agents increasingly operate in strategic settings where outcomes depend on the actions of other agents.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We illustrate the framework through a secondary analysis of published aggregate cooperation rates for GPT-3.5, GPT-4, and LLaMa-2 across four social-dilemma games.

**证据证明什么。** The results indicate that social-relational framing can substantially alter LLM behavior even when the underlying action sets and payoffs remain fixed.

**证据没有证明什么。** 7 Limitations and Validity The main limitation is data provenance. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19670v1#S3 — 3 Formal Framework; https://arxiv.org/html/2607.19670v1#S4 — 4 Minimal Empirical Design and Estimation。Evaluation：https://arxiv.org/html/2607.19670v1#S5 — 5 Results; https://arxiv.org/html/2607.19670v1#S4.SS1 — 4.1 Source study and retained scope。Limitations / counterevidence：https://arxiv.org/html/2607.19670v1#S6 — 6 Discussion; https://arxiv.org/html/2607.19670v1#S7 — 7 Limitations and Validity。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：7 Limitations and Validity The main limitation is data provenance.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-PLATFORM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19670:end -->

<!-- review:SF-2026-ARXIV-2607-19678:start -->
### Reference-Free Evaluation of Reasoning in Open-Ended Question Answering

<!-- claim:SF-2026-ARXIV-2607-19678:start -->AI-generated answers in high-stakes domains are often fluent but difficult to verify, especially when they contain multi-step reasoning rather than a single final answer. We propose a reasoning-based, reference-free framework for auditing LLM-generated outputs. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19678:end -->

**为什么进入候选分母。** 摘要首要问题为“AI-generated answers in high-stakes domains are often fluent but difficult to verify, especially when they contain multi-step reasoning rather than a single final answer.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We propose a reasoning-based, reference-free framework for auditing LLM-generated outputs.

**证据证明什么。** Our results show that QA evaluation should account for how inferential relations compose across a reasoning trace, rather than relying only on final answers or LLMs as verifiers.

**证据没有证明什么。** However, this means that the audit is not fully independent of LLM behaviour. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19678v1#S3 — 3 Methodology; https://arxiv.org/html/2607.19678v1#A1 — Appendix A Implementation Details。Evaluation：https://arxiv.org/html/2607.19678v1#S5 — 5 Results and Analysis; https://arxiv.org/html/2607.19678v1#A5 — Appendix E Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.19678v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.19678v1#Sx1 — Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：However, this means that the audit is not fully independent of LLM behaviour.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19678:end -->

<!-- review:SF-2026-ARXIV-2607-19683:start -->
### GhostPrompt: Cross-Image Adversarial Prompt for Vision-Language Models

<!-- claim:SF-2026-ARXIV-2607-19683:start -->Vision-Language Models (VLMs) are known to be vulnerable to adversarial attacks, where subtle perturbations to images or texts induce erroneous outputs. However, most text-based attacks are adapted from language-model-centric methods, in which the visual input is fixed during optimization, resulting in adversarial prompts that are tied to specific images and thus limiting their attack effectiveness. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19683:end -->

**为什么进入候选分母。** 摘要首要问题为“Vision-Language Models (VLMs) are known to be vulnerable to adversarial attacks, where subtle perturbations to images or texts induce erroneous outputs.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** Extensive experiments on prevalent VLMs verify that \ourmethod achieves an improvement of over 30% in attack success rates compared to state-of-the-art (SoTA) baselines, while reducing computation time by ~70%.

**证据证明什么。** Extensive experiments on prevalent VLMs verify that \ourmethod achieves an improvement of over 30% in attack success rates compared to state-of-the-art (SoTA) baselines, while reducing computation time by ~70%.

**证据没有证明什么。** Finally, performance on commercial VLMs ( e.g., GPT-4V) remains limited, which we leave for future work. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19683v1#S3 — 3. Threat Model and Challenges; https://arxiv.org/html/2607.19683v1#S3.SS1 — 3.1. Threat Model。Evaluation：https://arxiv.org/html/2607.19683v1#S5 — 5. Experiments and Results; https://arxiv.org/html/2607.19683v1#S5.SS1 — 5.1. Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.19683v1#S9 — 9. Conclusion, Limitations, and Future Work; https://arxiv.org/html/2607.19683v1#S3 — 3. Threat Model and Challenges。

**Artifact boundary。** Exact v1 links https://github.com/Ye-ze-yu/GhostPrompt, https://huggingface.co/ProtectAI/deberta-v3-base-prompt-injection-v2, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Finally, performance on commercial VLMs ( e.g., GPT-4V) remains limited, which we leave for future work.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19683:end -->

<!-- review:SF-2026-ARXIV-2607-19686:start -->
### Multi-Mask Diffusion Language Models for Few-Step Generation

<!-- claim:SF-2026-ARXIV-2607-19686:start -->Masked diffusion models (MDMs) are a promising family of language generators, but achieving high-quality few-step generation remains challenging. In MDMs, all forward trajectories collapse to a single fully masked state, leaving no terminal entropy for consistency-style few-step generation. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19686:end -->

**为什么进入候选分母。** 摘要首要问题为“Masked diffusion models (MDMs) are a promising family of language generators, but achieving high-quality few-step generation remains challenging.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** In this work, we propose a multi-mask diffusion model (MultiMDM) that preserves the masking structure towards few-step generation.

**证据证明什么。** Experiments on pretraining and distillation show that MultiMDM provides an effective foundation for principled few-step generation.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19686v1#S3 — 3 Methodology; https://arxiv.org/html/2607.19686v1#S2.SS1 — 2.1 Discrete Diffusion Models。Evaluation：https://arxiv.org/html/2607.19686v1#A3 — Appendix C Experiment Settings and Additional Results; https://arxiv.org/html/2607.19686v1#A2 — Appendix B Theoretical Analysis of Discrete Consistency Distillation。Limitations / counterevidence：https://arxiv.org/html/2607.19686v1#S5 — 5 Discussion。

**Artifact boundary。** Exact v1 links https://github.com/ML-GSAI/LLaDA, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-GENERATIVE-PARADIGMS`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19686:end -->

<!-- review:SF-2026-ARXIV-2607-19691:start -->
### SLPO: Scaling Latent Reasoning via a Surrogate Policy

<!-- claim:SF-2026-ARXIV-2607-19691:start -->Reinforcement learning with verifiable rewards has become the predominant recipe for eliciting test-time scaling in explicit Chain-of-Thought reasoners. Yet this scaling path remains computationally costly, since every intermediate step must be decoded as a language token. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19691:end -->

**为什么进入候选分母。** 摘要首要问题为“Reinforcement learning with verifiable rewards has become the predominant recipe for eliciting test-time scaling in explicit Chain-of-Thought reasoners.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We introduce Surrogate Latent Policy Optimization (SLPO) to bring outcome-reward RL to autoregressive latent reasoners: an empirical surrogate policy density over latent transitions for trajectory-level credit assignment, and a correctness-supervised stopping head that outcome-reward optimization refines into a variable-horizon policy.

**证据证明什么。** Across continuous and soft thinking settings, SLPO improves Pass@$k$ under parallel sampling and allocates longer latent computation to harder instances with higher deterministic accuracy.

**证据没有证明什么。** Future work will extend SLPO to larger backbones, open-ended reasoning, and multimodal latent architectures. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19691v1#S4 — 4 Methodology; https://arxiv.org/html/2607.19691v1#A1 — Appendix A Implementation Details。Evaluation：https://arxiv.org/html/2607.19691v1#A1.SS5 — A.5 Inference and Evaluation; https://arxiv.org/html/2607.19691v1#A4 — Appendix D Latent Geometry Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.19691v1#S8 — 8 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Future work will extend SLPO to larger backbones, open-ended reasoning, and multimodal latent architectures.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`WORLDVIEW-LLM-INTELLIGENCE`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19691:end -->

<!-- review:SF-2026-ARXIV-2607-19695:start -->
### NavVerse: Benchmarking Indoor-to-Outdoor Embodied Navigation in Continuous Robot Simulation

<!-- claim:SF-2026-ARXIV-2607-19695:start -->Robots deployed in delivery, campus, and emergency-response settings often need to navigate from buildings to streets within a single continuous episode. Existing benchmarks usually evaluate indoor and outdoor navigation separately, and many abstract away robot execution, leaving exit finding, boundary traversal, adaptation, and kinodynamic failures underexplored. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19695:end -->

**为什么进入候选分母。** 摘要首要问题为“Robots deployed in delivery, campus, and emergency-response settings often need to navigate from buildings to streets within a single continuous episode.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We introduce NavVerse, a physics-enabled benchmark for indoor-to-outdoor embodied navigation.

**证据证明什么。** Zero-shot experiments with RL, VLA, and modular baselines show that current agents remain far from solving cross-context navigation: end-to-end VLAs obtain the highest zero-shot success, while the modular method provides the strongest safety profile.

**证据没有证明什么。** Finally, outdoor-to-indoor transition is not explored in this work, we leave this setting to future extensions. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19695v1#A1.SS7 — A.7 System Setup and Runtime; https://arxiv.org/html/2607.19695v1#A2.SS3 — B.3 Outdoor Terrain and Road Modeling。Evaluation：https://arxiv.org/html/2607.19695v1#A1 — Appendix A Benchmark Interface and Evaluation Protocol; https://arxiv.org/html/2607.19695v1#S3.SS3 — 3.3 Benchmark and Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.19695v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/isaac-sim/IsaacSim, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Finally, outdoor-to-indoor transition is not explored in this work, we leave this setting to future extensions.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19695:end -->

<!-- review:SF-2026-ARXIV-2607-19701:start -->
### SafeGen: Goal-Conditioned Video Diffusion of Safety-Critical Scenarios for VLM-Based Autonomous Driving

<!-- claim:SF-2026-ARXIV-2607-19701:start -->VLMs are increasingly deployed in AD systems, creating an urgent need for rigorous safety evaluation under rare yet safety-critical scenarios. Among these, interactions with vulnerable road users represent a major source of real-world failures. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19701:end -->

**为什么进入候选分母。** 摘要首要问题为“VLMs are increasingly deployed in AD systems, creating an urgent need for rigorous safety evaluation under rare yet safety-critical scenarios.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** We present SafeGen, a goal-conditioned diffusion framework for safety-critical scenario generation in VLMADs.

**证据证明什么。** Furthermore, fine-tuning a VLMAD improves performance in real-world driving scenes by an average of 15.9%.

**证据没有证明什么。** Future work includes extending the framework to multi-agent interactions. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19701v1#S3 — 3. Methodology; https://arxiv.org/html/2607.19701v1#S3.SS4 — 3.4. Systemic Generation Workflow。Evaluation：https://arxiv.org/html/2607.19701v1#S4.SS2 — 4.2. Main Results and Analysis; https://arxiv.org/html/2607.19701v1#S4 — 4. Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.19701v1#S5 — 5. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/JoFrc/SafeGen, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Future work includes extending the framework to multi-agent interactions.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`principle_reuse`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19701:end -->

<!-- review:SF-2026-ARXIV-2607-19704:start -->
### Efficient Clustering with Provable Guardrails for LLM Inference at Scale

<!-- claim:SF-2026-ARXIV-2607-19704:start -->Scaling LLM-based applications to millions of users is bottlenecked by the inference cost and latency of modern foundation models. A natural fix is to cluster the inputs and call the LLM only on cluster representatives, letting other members inherit the output -- but this is only safe if each member is measurably close to its representative. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19704:end -->

**为什么进入候选分母。** 摘要首要问题为“Scaling LLM-based applications to millions of users is bottlenecked by the inference cost and latency of modern foundation models.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** Deployed on 38 million customers for a persona-based recommender, the clustering method cut downstream cost and latency by 50-fold while preserving personalization and unblocked the production launch.

**证据证明什么。** Deployed on 38 million customers for a persona-based recommender, the clustering method cut downstream cost and latency by 50-fold while preserving personalization and unblocked the production launch.

**证据没有证明什么。** Future directions include richer similarity metrics that better predict LLM output agreement, and learned representatives that minimize cluster count under the guardrail. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19704v1#A1 — Appendix A Design Considerations and Technical Details; https://arxiv.org/html/2607.19704v1#S3 — 3 Method。Evaluation：https://arxiv.org/html/2607.19704v1#A6 — Appendix F Additional Experiment Results; https://arxiv.org/html/2607.19704v1#A5 — Appendix E Computational Complexity Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.19704v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://huggingface.co/datasets/HuggingFaceTB/cosmopedia, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：Future directions include richer similarity metrics that better predict LLM output agreement, and learned representatives that minimize cluster count under the guardrail.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-SCHEDULING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19704:end -->

<!-- review:SF-2026-ARXIV-2607-19712:start -->
### How Fast Can Reward Models Score? A Systems Study of C++ and PyTorch Inference Runtimes for RLHF

<!-- claim:SF-2026-ARXIV-2607-19712:start -->In RLHF pipelines, reward scoring blocks policy updates. Slow scoring bottlenecks the entire loop, since no update runs until every rollout gets a score. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19712:end -->

**为什么进入候选分母。** 摘要首要问题为“In RLHF pipelines, reward scoring blocks policy updates.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** Slow scoring bottlenecks the entire loop, since no update runs until every rollout gets a score.

**证据证明什么。** The results are from repeated, independent runs, since single runs just aren't reliable enough to trust.

**证据没有证明什么。** Recompilation risk remains the primary variable our fixed 60 row shape distribution cannot fully rule out. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19712v1#S3 — 3 Methodology; https://arxiv.org/html/2607.19712v1#S3.SS4 — 3.4 Statistical Method。Evaluation：https://arxiv.org/html/2607.19712v1#S4 — 4 Results。Limitations / counterevidence：https://arxiv.org/html/2607.19712v1#S3.SS7 — 3.7 Hardware and Limitations; https://arxiv.org/html/2607.19712v1#S5 — 5 Discussion。

**Artifact boundary。** Exact v1 links https://github.com/vishnup22/reward-model-benchmarks, https://github.com/onnx/onnx, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Recompilation risk remains the primary variable our fixed 60 row shape distribution cannot fully rule out.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`TRAIN-RLHF`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19712:end -->

<!-- review:SF-2026-ARXIV-2607-19719:start -->
### Koopman Dreamer: Spectrally Constrained Latent Dynamics for Stable World-Model Imagination

<!-- claim:SF-2026-ARXIV-2607-19719:start -->Latent world models improve sample efficiency in continuous control by optimizing policies over imagined latent trajectories, but common neural transitions offer limited direct control over modal persistence and error accumulation in long rollouts. We propose Koopman Dreamer, a Dreamer-style world model with a spectrally constrained deterministic latent dynamics core. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19719:end -->

**为什么进入候选分母。** 摘要首要问题为“Latent world models improve sample efficiency in continuous control by optimizing policies over imagined latent trajectories, but common neural transitions offer limited direct control over modal persistence and error accumulation in long rollouts.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We propose Koopman Dreamer, a Dreamer-style world model with a spectrally constrained deterministic latent dynamics core.

**证据证明什么。** Experimental results on proprioceptive continuous-control tasks from the DeepMind Control Suite and UAV-LiDAR autonomous navigation demonstrate that Koopman Dreamer improves the stability of long-horizon latent rollouts and achieves stronger closed-loop control performance on tasks that rely on high-quality multi-step imagination.

**证据没有证明什么。** The linear and bilinear action terms further adapt the backbone to controlled dynamics by representing both globally consistent and state-dependent action effects. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19719v1#S4 — IV Method; https://arxiv.org/html/2607.19719v1#S2.SS1 — II-A Latent World Models。Evaluation：https://arxiv.org/html/2607.19719v1#S6 — VI Experiments and Analysis; https://arxiv.org/html/2607.19719v1#A0.SS1 — -A DMC Proprioceptive Benchmark Details。Limitations / counterevidence：https://arxiv.org/html/2607.19719v1#S7 — VII Discussion; https://arxiv.org/html/2607.19719v1#S8 — VIII Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：The linear and bilinear action terms further adapt the backbone to controlled dynamics by representing both globally consistent and state-dependent action effects.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19719:end -->

<!-- review:SF-2026-ARXIV-2607-19747:start -->
### Beyond Relevance-Centric Retrieval: Rubric-Oriented Document Set Selection and Ranking

<!-- claim:SF-2026-ARXIV-2607-19747:start -->As large language models and AI agents become the primary consumers of search results, document set quality determines the upper bound of downstream generation. Yet existing evaluation systems remain confined to scoring documents independently and aggregating via nDCG, ignoring inter-document interactions (redundancy, conflict, complementarity) and unable to answer what makes one document set better than another. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19747:end -->

**为什么进入候选分母。** 摘要首要问题为“As large language models and AI agents become the primary consumers of search results, document set quality determines the upper bound of downstream generation.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** To address these issues, we propose a complete evaluate-diagnose-optimize framework.

**证据证明什么。** As large language models and AI agents become the primary consumers of search results, document set quality determines the upper bound of downstream generation.

**证据没有证明什么。** 6 Conclusion and Limitation We present an evaluate-diagnose-optimize framework for document set quality. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19747v1#A1 — Appendix A Implementation Details of SetwiseEvalKit; https://arxiv.org/html/2607.19747v1#A4 — Appendix D Model Prompts。Evaluation：https://arxiv.org/html/2607.19747v1#A2 — Appendix B More Experimental Results; https://arxiv.org/html/2607.19747v1#S4.SS2 — 4.2 Results on Rubric-Oriented Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.19747v1#S6 — 6 Conclusion and Limitation。

**Artifact boundary。** Exact v1 links https://github.com/Rubric4Setwise/Rubric4Setwise, https://huggingface.co/collections/placeholder, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：6 Conclusion and Limitation We present an evaluate-diagnose-optimize framework for document set quality.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-RAG`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19747:end -->

<!-- review:SF-2026-ARXIV-2607-19749:start -->
### The World Model Remembers, the Actor Forgets: Dream Rehearsal for Continual Model-Based RL

<!-- claim:SF-2026-ARXIV-2607-19749:start -->Model-based reinforcement-learning agents of the DreamerV3 family forget catastrophically when trained on task sequences, even when an unbounded replay buffer preserves every earlier experience. We ask a question the continual-RL literature has assumed an answer to but never measured: which component forgets? 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19749:end -->

**为什么进入候选分母。** 摘要首要问题为“Model-based reinforcement-learning agents of the DreamerV3 family forget catastrophically when trained on task sequences, even when an unbounded replay buffer preserves every earlier experience.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We ask a question the continual-RL literature has assumed an answer to but never measured: which component forgets?

**证据证明什么。** The dream-grading step is load-bearing: we characterize two scoring failure modes, provide an offline selection gauge that caught both before they contaminated results, and give a realized-first grading rule that closes them.

**证据没有证明什么。** 9 Limitations MiniGrid scale; a 17M-parameter world model; one task ordering per chain length; return bars rather than normalized scores (we additionally report retention relative to each task’s own post-acquisition competence). with real run-level nondeterminism — identical seeds can diverge qualitatively — so we report dispersion and bar-distance, not only pass counts. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19749v1#S4.SS3 — 4.3 The world model retains everything we can measure; https://arxiv.org/html/2607.19749v1#S5 — 5 Recovery from the World Model Alone。Evaluation：https://arxiv.org/html/2607.19749v1#S3 — 3 Experimental Setup; https://arxiv.org/html/2607.19749v1#S6.SS1 — 6.1 Four-task result。Limitations / counterevidence：https://arxiv.org/html/2607.19749v1#S10 — 10 Conclusion; https://arxiv.org/html/2607.19749v1#S9 — 9 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/gurpnijjer/dream-rehearsal, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：9 Limitations MiniGrid scale; a 17M-parameter world model; one task ordering per chain length; return bars rather than normalized scores (we additionally report retention relative to each task’s own post-acquisition competence). with real run-level nondeterminism — identical seeds can diverge qualitatively — so we report dispersion and bar-distance, not only pass counts.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19749:end -->

<!-- review:SF-2026-ARXIV-2607-19771:start -->
### An Isotropy-Preserving Spectral Cap for Muon: Theory and Three Case Studies

<!-- claim:SF-2026-ARXIV-2607-19771:start -->Muon and related matrix-sign optimizers are increasingly used to pre-train large language models, but their effect on the internal geometry of individual weight matrices is not well understood. This preliminary report proposes a unified framework built on a single idealizing assumption -- exact scale invariance of the loss under weight rescaling, which holds approximately in normalization-heavy networks. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19771:end -->

**为什么进入候选分母。** 摘要首要问题为“Muon and related matrix-sign optimizers are increasingly used to pre-train large language models, but their effect on the internal geometry of individual weight matrices is not well understood.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We then study three systems trained with Muon: a nanoGPT feed-forward projection, a 64-expert mixture-of-experts router, and the query/key projections of a bf16 FlashAttention block.

**证据证明什么。** We emphasize that the scale-invariance assumption is strong and that these small-scale results are preliminary; comments are welcome.

**证据没有证明什么。** With a bf16 mantissa of 7 bits, at a score scale of the resolution is only . 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19771v1#S2.SS3 — 2.3 Result: the three methods have equal val loss; https://arxiv.org/html/2607.19771v1#S3.SS3 — 3.3 Core result: isotropy across the three methods。Evaluation：https://arxiv.org/html/2607.19771v1#S2.SS2 — 2.2 Experimental setup; https://arxiv.org/html/2607.19771v1#S2.SS3 — 2.3 Result: the three methods have equal val loss。Limitations / counterevidence：https://arxiv.org/html/2607.19771v1#S3.SS4 — 3.4 L0 / L5 load balancing: a phase transition and LFB failure; https://arxiv.org/html/2607.19771v1#S4.SS2 — 4.2 The bf16 FA failure mechanism (from the reference paper)。

**Artifact boundary。** Exact v1 links https://github.com/karpathy/nanoGPT, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：With a bf16 mantissa of 7 bits, at a score scale of the resolution is only .

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`TRAIN-PRETRAINING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19771:end -->

<!-- review:SF-2026-ARXIV-2607-19774:start -->
### Defer to Plan: Adaptive Multi-Agent Fusion for End-to-End V2X Driving

<!-- claim:SF-2026-ARXIV-2607-19774:start -->Vehicle-to-everything-aided autonomous driving (V2X-AD) significantly enhances driving performance through information sharing. However, existing collaborative perception methods only optimize module-level perception capabilities and fail to effectively serve the ultimate planning and control tasks. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19774:end -->

**为什么进入候选分母。** 摘要首要问题为“Vehicle-to-everything-aided autonomous driving (V2X-AD) significantly enhances driving performance through information sharing.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We propose an end-to-end collaborative driving system that directly optimizes planning task performance.

**证据证明什么。** Experiments demonstrate that our method achieves a driving score of 79.72, surpassing the state-of-the-art CoDriving baseline (77.15) by 3.33% in closed-loop evaluation while maintaining communication efficiency.

**证据没有证明什么。** Our system assumes fixed communication topology; future work can explore dynamic agent selection based on relevance. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19774v1#S3 — III Method; https://arxiv.org/html/2607.19774v1#S3.SS2 — III-B Overall Architecture。Evaluation：https://arxiv.org/html/2607.19774v1#S4 — IV Experiments; https://arxiv.org/html/2607.19774v1#S4.SS1 — IV-A Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.19774v1#S5 — V Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Our system assumes fixed communication topology; future work can explore dynamic agent selection based on relevance.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MULTI-AGENT`；evidence-stage relation：`principle_reuse`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19774:end -->

<!-- review:SF-2026-ARXIV-2607-19790:start -->
### Trace: A Taxonomy-Guided Environment for Multidomain Visual Reasoning

<!-- claim:SF-2026-ARXIV-2607-19790:start -->Reinforcement learning with verifiable rewards (RLVR) has substantially improved language-model reasoning, yet its extension to vision-language models remains constrained by the lack of training data that are simultaneously broad, exactly verifiable, and reproducible. We introduce Trace, a taxonomy-guided environment for multidomain visual reasoning. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19790:end -->

**为什么进入候选分母。** 摘要首要问题为“Reinforcement learning with verifiable rewards (RLVR) has substantially improved language-model reasoning, yet its extension to vision-language models remains constrained by the lack of training data that are simultaneously broad, exactly verifiable, and reproducible.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We introduce Trace, a taxonomy-guided environment for multidomain visual reasoning.

**证据证明什么。** Reinforcement learning with verifiable rewards (RLVR) has substantially improved language-model reasoning, yet its extension to vision-language models remains constrained by the lack of training data that are simultaneously broad, exactly verifiable, and reproducible.

**证据没有证明什么。** 7 Limitations and Future Work The Trace taxonomy is explicit but human-designed: task boundaries can still involve judgment, and the 1,000 authored tasks do not exhaust visual reasoning. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19790v1#S1 — 1 Introduction; https://arxiv.org/html/2607.19790v1#S2 — 2 Related Work。Evaluation：https://arxiv.org/html/2607.19790v1#A2 — Appendix B Experimental Details; https://arxiv.org/html/2607.19790v1#A2.SS2 — B.2 External evaluation suite。Limitations / counterevidence：https://arxiv.org/html/2607.19790v1#S7 — 7 Limitations and Future Work; https://arxiv.org/html/2607.19790v1#S8 — 8 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/embodiedreasoning/ERQA, https://huggingface.co/datasets/xai-org/RealworldQA, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：7 Limitations and Future Work The Trace taxonomy is explicit but human-designed: task boundaries can still involve judgment, and the 1,000 authored tasks do not exhaust visual reasoning.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19790:end -->

<!-- review:SF-2026-ARXIV-2607-19793:start -->
### Silent Failures in Multimodal Agentic Search:A Diagnostic Taxonomy and Cross-Judge Evaluation

<!-- claim:SF-2026-ARXIV-2607-19793:start -->Multimodal agentic search systems increasingly rely on external tools to answer knowledge-intensive visual questions. However, existing evaluations mainly focus on final-answer accuracy and may miss failures in the search trajectory. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19793:end -->

**为什么进入候选分母。** 摘要首要问题为“Multimodal agentic search systems increasingly rely on external tools to answer knowledge-intensive visual questions.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Multimodal agentic search systems increasingly rely on external tools to answer knowledge-intensive visual questions.

**证据证明什么。** Experiments on MMSearch-Plus trajectories across four frontier multimodal models show that surface accuracy consistently overestimates true trajectory-level correctness.

**证据没有证明什么。** This failure reflects a central challenge in multimodal search: the model must not only retrieve evidence, but also check consistency between visual and textual evidence. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19793v1#S2 — 2. Method。Evaluation：https://arxiv.org/html/2607.19793v1#S3 — 3. Experiments; https://arxiv.org/html/2607.19793v1#S3.SS1 — 3.1. Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.19793v1#S2.SS2 — 2.2. Taxonomy of Silent Failures; https://arxiv.org/html/2607.19793v1#S4 — 4. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/DingWu1021/silent-failures-multimodal-agentic-search, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：This failure reflects a central challenge in multimodal search: the model must not only retrieve evidence, but also check consistency between visual and textual evidence.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-PLATFORM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19793:end -->

<!-- review:SF-2026-ARXIV-2607-19806:start -->
### OPIUM: Mitigating Steering Externalities and Over-Refusal via Dual Objective Latent Optimization

<!-- claim:SF-2026-ARXIV-2607-19806:start -->Activation steering provides a lightweight mechanism for controlling large language models at inference time, but steering vectors can have unintended externalities: utility vectors may weaken safety behavior, while refusal vectors may induce over-refusal on benign prompts. We introduce OPIUM (Optimizing Protected Injections via Utility Manifolds), a training-free method for sanitizing steering vectors through representation matching. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19806:end -->

**为什么进入候选分母。** 摘要首要问题为“Activation steering provides a lightweight mechanism for controlling large language models at inference time, but steering vectors can have unintended externalities: utility vectors may weaken safety behavior, while refusal vectors may induce over-refusal on benign prompts.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** We introduce OPIUM (Optimizing Protected Injections via Utility Manifolds), a training-free method for sanitizing steering vectors through representation matching.

**证据证明什么。** Across steering-externality and over-refusal settings, OPIUM improves the safety--utility tradeoff relative to vanilla steering and directional ablation, suggesting that harmful side effects of activation steering can often be mitigated directly in activation space.

**证据没有证明什么。** 6 Conclusion and Future Directions We presented OPIUM, a training-free method for mitigating side effects of activation steering. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19806v1#S3 — 3 Methodology; https://arxiv.org/html/2607.19806v1#S4.SS1 — 4.1 Models and Baselines。Evaluation：https://arxiv.org/html/2607.19806v1#A2 — Appendix B Ablation Studies; https://arxiv.org/html/2607.19806v1#A3 — Appendix C Over-Refusal Evaluation Details。Limitations / counterevidence：https://arxiv.org/html/2607.19806v1#S6 — 6 Conclusion and Future Directions; https://arxiv.org/html/2607.19806v1#S5 — 5 Limitations。

**Artifact boundary。** Exact v1 links https://www.lesswrong.com/posts/CbSEZSpjdpnvBcEvc/i-found-greater-than-800-orthogonal-write-code-steering, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：6 Conclusion and Future Directions We presented OPIUM, a training-free method for mitigating side effects of activation steering.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`WORLDVIEW-LLM-INTELLIGENCE`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19806:end -->

<!-- review:SF-2026-ARXIV-2607-19809:start -->
### Dreamer-CPC: Message Learning with World Models for Decentralized Multi-agent Reinforcement Learning

<!-- claim:SF-2026-ARXIV-2607-19809:start -->In multi-agent reinforcement learning (MARL), inter-agent communication is effective for improving performance under partial observability. Representation learning-based approaches enable decentralized agents to learn messages grounded in their own observations, but they rely only on current observations and cannot convey information accumulated over time. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19809:end -->

**为什么进入候选分母。** 摘要首要问题为“In multi-agent reinforcement learning (MARL), inter-agent communication is effective for improving performance under partial observability.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We propose Dreamer-CPC, a decentralized model-based MARL method that integrates message learning based on Collective Predictive Coding (CPC) into the world model of DreamerV3.

**证据证明什么。** In both environments, Dreamer-CPC outperformed IPPO-CPC, an existing CPC-based method that generates messages from current observations, as well as no-communication baselines.

**证据没有证明什么。** First, we did not analyze what information the learned messages carry. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19809v1#Pt0.A1 — Appendix 0.A Algorithms; https://arxiv.org/html/2607.19809v1#S2.SS2 — 2.2 World Model。Evaluation：https://arxiv.org/html/2607.19809v1#S3 — 3 Experiments; https://arxiv.org/html/2607.19809v1#S3.SS3 — 3.3 Results。Limitations / counterevidence：https://arxiv.org/html/2607.19809v1#S4 — 4 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：First, we did not analyze what information the learned messages carry.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19809:end -->

<!-- review:SF-2026-ARXIV-2607-19824:start -->
### Rewarding Better Thinking for LLM Preference Alignment

<!-- claim:SF-2026-ARXIV-2607-19824:start -->LLM preference alignment aims to optimize models toward human preferences across diverse user instructions. Reinforcement learning has become a major post-training approach for this goal, but existing proxy rewards are often outcome-level, mainly evaluating the final response while providing limited guidance for the reasoning trajectory. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19824:end -->

**为什么进入候选分母。** 摘要首要问题为“LLM preference alignment aims to optimize models toward human preferences across diverse user instructions.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** To address this limitation, we propose Thinking Checklist Reward (TCR), a process-oriented reward for RL-based preference alignment.

**证据证明什么。** Experiments on five models from three model families show that TCR consistently improves alignment performance across diverse benchmarks, with ablations further validating the importance of EMA-based residual formulation and sample-specific checklist supervision.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19824v1#Sx5 — Method; https://arxiv.org/html/2607.19824v1#A1 — Appendix A Reward Computation Algorithm。Evaluation：https://arxiv.org/html/2607.19824v1#A2.SSx3 — Evaluation Benchmarks; https://arxiv.org/html/2607.19824v1#A2 — Appendix B Experimental Details。Limitations / counterevidence：https://arxiv.org/html/2607.19824v1#Sx7 — Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-DPO`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19824:end -->

<!-- review:SF-2026-ARXIV-2607-19827:start -->
### Clinical Pathways as Safety Specifications for Physical AI in Hospital Wards

<!-- claim:SF-2026-ARXIV-2607-19827:start -->Ensuring safety in Physical AI systems operating in real-world environments is a critical challenge, particularly in hospital wards where vulnerable patients, clinical staff, medical devices, and assistive robots coexist. In this paper, we reinterpret Clinical Pathways as explicit runtime safety specifications for embodied medical AI. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19827:end -->

**为什么进入候选分母。** 摘要首要问题为“Ensuring safety in Physical AI systems operating in real-world environments is a critical challenge, particularly in hospital wards where vulnerable patients, clinical staff, medical devices, and assistive robots coexist.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** We propose a conceptual robotic architecture that integrates wearable sensors, smart medical devices, and assistive robotic components into a unified framework for real-time safety monitoring.

**证据证明什么。** This work contributes to Safe Physical AI by operationalizing domain-specific clinical knowledge as enforceable safety constraints, bridging learning-based perception and runtime safety monitoring to assist nursing staff in real-world hospital wards.

**证据没有证明什么。** Embodiment as a safety asset : the robot’s active sensing yields redundancy a passive network cannot, allowing a tampered wearable to be cross-checked against on-board perception. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19827v1#S2 — II Approach; https://arxiv.org/html/2607.19827v1#S2.SS1 — II-A System Overview。Evaluation：https://arxiv.org/html/2607.19827v1#S1 — I Introduction; https://arxiv.org/html/2607.19827v1#S2 — II Approach。Limitations / counterevidence：https://arxiv.org/html/2607.19827v1#S4 — IV Discussion; https://arxiv.org/html/2607.19827v1#S5 — V Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Embodiment as a safety asset : the robot’s active sensing yields redundancy a passive network cannot, allowing a tampered wearable to be cross-checked against on-board perception.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19827:end -->

<!-- review:SF-2026-ARXIV-2607-19829:start -->
### DARWIN: Evolving Jailbreak Adversary and Guardrail for LLM Safety Evaluation and Protection

<!-- claim:SF-2026-ARXIV-2607-19829:start -->Most existing LLM safety evaluation and defense methods follow a static formulation: jailbreak vulnerabilities are evaluated with fixed attack methods, and guardrails are trained on fixed malicious prompt datasets. However, real-world adversaries continuously evolve their capabilities and expand the attack space. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19829:end -->

**为什么进入候选分母。** 摘要首要问题为“Most existing LLM safety evaluation and defense methods follow a static formulation: jailbreak vulnerabilities are evaluated with fixed attack methods, and guardrails are trained on fixed malicious prompt datasets.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** To address this challenge, we propose DARWIN, an evolutionary attack-defense framework that formulates jailbreaking as an open-ended evolution process and continuously updates guardrails through an evolving attack-defense loop.

**证据证明什么。** DARWIN-Guard achieves an average unsafe recall of 91.6% across 12 safety benchmarks, outperforming strong guardrails such as YuFeng-XGuard and Nemotron Guard, while maintaining a nearly 100% pass rate on standard benign datasets.

**证据没有证明什么。** DARWIN overcomes the limitations of static paradigms by establishing a continuous loop of attack prompt generation and guardrail training. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19829v1#S3 — 3 THE DARWIN FRAMEWORK。Evaluation：https://arxiv.org/html/2607.19829v1#S4 — 4 Experiments; https://arxiv.org/html/2607.19829v1#S4.SS1 — 4.1 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.19829v1#S1 — 1 Introduction; https://arxiv.org/html/2607.19829v1#S2 — 2 Related Work。

**Artifact boundary。** Exact v1 links https://huggingface.co/datasets/llm-semantic-router/jailbreak-detection-dataset, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：DARWIN overcomes the limitations of static paradigms by establishing a continuous loop of attack prompt generation and guardrail training.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19829:end -->

<!-- review:SF-2026-ARXIV-2607-19837:start -->
### Know Your Agent: Reconnaissance-Driven Pentesting of AI Agents

<!-- claim:SF-2026-ARXIV-2607-19837:start -->Traditional pentesting uses reconnaissance at each step to uncover unseen weaknesses, build stronger attacks, and advance the objective; we argue that AI agents require the same treatment. We formalize agent reconnaissance by modeling the process and identifying the knowledge assets it seeks to extract: what they are, how they are used, and which agent weaknesses they exploit to give adversaries leverage in indirect prompt injection attacks. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19837:end -->

**为什么进入候选分母。** 摘要首要问题为“Traditional pentesting uses reconnaissance at each step to uncover unseen weaknesses, build stronger attacks, and advance the objective; we argue that AI agents require the same treatment.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** We instantiate these insights in Know Your Agent (KYA), a framework that automates black-box, reconnaissance-driven pentesting by probing agents, building target profiles, and using those profiles to craft stronger attacks.

**证据证明什么。** We evaluate KYA on agent-security benchmarks and a real-world coding agent, and release KYA, its benchmarks, and baseline implementations for reproducibility.

**证据没有证明什么。** These results suggest that securing AI agents requires testing not only whether attacks succeed, but also what operational knowledge agents expose and how that knowledge can be used against them. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19837v1#S3 — III Threat Model and System Assumptions; https://arxiv.org/html/2607.19837v1#S5 — V The KYA Framework。Evaluation：https://arxiv.org/html/2607.19837v1#A1 — Appendix A Ablation Study: Full Curves; https://arxiv.org/html/2607.19837v1#A2.SS6 — B-F Per-Cell Observation Behind the Tier Result。Limitations / counterevidence：https://arxiv.org/html/2607.19837v1#S3 — III Threat Model and System Assumptions; https://arxiv.org/html/2607.19837v1#S7 — VII Conclusion。

**Artifact boundary。** Exact v1 links https://owasp.org/www-project-top-10-for-large-language-model-applications/, https://huggingface.co/ProtectAI/deberta-v3-base-prompt-injection-v2, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：These results suggest that securing AI agents requires testing not only whether attacks succeed, but also what operational knowledge agents expose and how that knowledge can be used against them.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-PLATFORM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19837:end -->

<!-- review:SF-2026-ARXIV-2607-19848:start -->
### emb-diversity: A Tool for Embedding-Based Measurement of Data Diversity

<!-- claim:SF-2026-ARXIV-2607-19848:start -->There is growing evidence that data diversity is crucial for developing fair and robust NLP models. However, current approaches to measure diversity remain inconsistent and fragmented: While there exist a number of tools for measuring the lexical diversity of texts, researchers lack standardized tools for quantifying diversity based on embeddings. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19848:end -->

**为什么进入候选分母。** 摘要首要问题为“There is growing evidence that data diversity is crucial for developing fair and robust NLP models.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** However, current approaches to measure diversity remain inconsistent and fragmented: While there exist a number of tools for measuring the lexical diversity of texts, researchers lack standardized tools for quantifying diversity based on embeddings.

**证据证明什么。** We demonstrate its potential for several use cases: measuring the stylistic, semantic, language and speaker diversity of datasets. https://github.com/nlpsoc/emb-diversity/

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19848v1#S3 — 3 System Overview。Evaluation：https://arxiv.org/html/2607.19848v1#A4 — Appendix D Details of Heuristic Evaluation; https://arxiv.org/html/2607.19848v1#S4 — 4 Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.19848v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/nlpsoc/emb-diversity/, https://github.com/nlpsoc/emb-diversity/blob/main/optimization_doc.md, https://huggingface.co/AnnaWegmann/Style-Embedding; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-DATA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19848:end -->

<!-- review:SF-2026-ARXIV-2607-19850:start -->
### SOPD-SocialNav: Selective On-Policy Distillation for Vision-Language Social Navigation

<!-- claim:SF-2026-ARXIV-2607-19850:start -->Vision-language models have shown strong potential for social robot navigation by leveraging rich semantic understanding of complex environments and human behaviors. However, large scale VLMs are difficult to deploy on resource-constrained robotic platforms, while lightweight VLMs often lack sufficient social reasoning capability. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19850:end -->

**为什么进入候选分母。** 摘要首要问题为“Vision-language models have shown strong potential for social robot navigation by leveraging rich semantic understanding of complex environments and human behaviors.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** To address this problem, we propose SOPD-SocialNav, a selective on-policy distillation (SOPD) method that transfers social navigation knowledge from a large teacher VLM to a lightweight student VLM.

**证据证明什么。** Experiments on the SNEI and MUSON benchmarks demonstrate that SOPD consistently outperforms supervised fine-tuning, off-policy distillation, and standard on-policy distillation baselines in action prediction, perception consistency, and reasoning consistency.

**证据没有证明什么。** In future work, we plan to further investigate adaptive entropy threshold selection, extend SOPD to longer-horizon navigation trajectories, and evaluate the method in more diverse real-world human-robot interaction scenarios. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19850v1#S3 — III Method。Evaluation：https://arxiv.org/html/2607.19850v1#S4 — IV Experiment; https://arxiv.org/html/2607.19850v1#S4.SS1 — IV-A Experiment Settings。Limitations / counterevidence：https://arxiv.org/html/2607.19850v1#S5 — V CONCLUSIONS。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：In future work, we plan to further investigate adaptive entropy threshold selection, extend SOPD to longer-horizon navigation trajectories, and evaluate the method in more diverse real-world human-robot interaction scenarios.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19850:end -->

<!-- review:SF-2026-ARXIV-2607-19857:start -->
### Memory-Augmented Multimodal Large Language Models for Small Object Understanding in Streaming Aerial Videos

<!-- claim:SF-2026-ARXIV-2607-19857:start -->Language-guided aerial perception aims to understand user-specified tiny targets in complex unmanned aerial vehicle (UAV) scenes. In real UAV deployment, the UAV must respond while it flies, so such perception runs in an online streaming manner, where frames arrive sequentially and the model responds to each one without access to future frames. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19857:end -->

**为什么进入候选分母。** 摘要首要问题为“Language-guided aerial perception aims to understand user-specified tiny targets in complex unmanned aerial vehicle (UAV) scenes.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** From the method perspective, we propose \textbf{SkyAnchor}, an MLLM with two designs to the above challenges: a Semantics-Aware Token Router that preserves small-target under a reduced visual-token budget, and a Hierarchical Memory Bank that keeps the target consistently understood on streams.

**证据证明什么。** From the method perspective, we propose \textbf{SkyAnchor}, an MLLM with two designs to the above challenges: a Semantics-Aware Token Router that preserves small-target under a reduced visual-token budget, and a Hierarchical Memory Bank that keeps the target consistently understood on streams.

**证据没有证明什么。** Future work will pursue further model compression and hardware-aware optimization, enabling the pipeline to better match the native capture rate under fast target or platform motion. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19857v1#S4 — IV SkyAnchor Method; https://arxiv.org/html/2607.19857v1#S4.SS1 — IV-A Model Overview。Evaluation：https://arxiv.org/html/2607.19857v1#S5 — V Experiment; https://arxiv.org/html/2607.19857v1#S5.SS1 — V-A Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.19857v1#S6 — VI Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Future work will pursue further model compression and hardware-aware optimization, enabling the pipeline to better match the native capture rate under fast target or platform motion.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19857:end -->

<!-- review:SF-2026-ARXIV-2607-19865:start -->
### DocOps: A Verifiable Benchmark for Autonomous Agents in Complex Document Operations

<!-- claim:SF-2026-ARXIV-2607-19865:start -->As autonomous agents rapidly evolve, their ability to reliably manipulate ubiquitous digital documents has become critical for enabling general-purpose AI assistants and automating complex workspace workflows. In this paper, we introduce DocOps, a deterministically verifiable evaluation framework underpinned by a hierarchical taxonomy that deconstructs document operations inspired by real-world practices into atomic dimensions and escalating workflow complexities. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19865:end -->

**为什么进入候选分母。** 摘要首要问题为“As autonomous agents rapidly evolve, their ability to reliably manipulate ubiquitous digital documents has become critical for enabling general-purpose AI assistants and automating complex workspace workflows.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** In this paper, we introduce DocOps, a deterministically verifiable evaluation framework underpinned by a hierarchical taxonomy that deconstructs document operations inspired by real-world practices into atomic dimensions and escalating workflow complexities.

**证据证明什么。** Ultimately, our work exposes the capability boundaries of agents in maintaining global document consistency, shedding light on the future design of robust, non-destructive agents for complex digital ecosystems.

**证据没有证明什么。** Limitations 1) DocOps focuses on deterministic, offline document-editing tasks and does not cover workflows requiring live external services, collaborative editing, or interactive user clarification. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19865v1#S3.SS1 — 3.1 Taxonomy Design; https://arxiv.org/html/2607.19865v1#A8 — Appendix H Model Serving Details。Evaluation：https://arxiv.org/html/2607.19865v1#A5 — Appendix E Full Skill-Injection Results; https://arxiv.org/html/2607.19865v1#A6 — Appendix F Verifier Fidelity Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.19865v1#Sx1 — Conclusion; https://arxiv.org/html/2607.19865v1#Sx2 — Limitations。

**Artifact boundary。** Exact v1 links https://github.com/icip-cas/DocOps, https://github.com/anthropics/skills, https://github.com/anthropics/claude-code; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Limitations 1) DocOps focuses on deterministic, offline document-editing tasks and does not cover workflows requiring live external services, collaborative editing, or interactive user clarification.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-WORKFLOW`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19865:end -->

<!-- review:SF-2026-ARXIV-2607-19876:start -->
### KineBench: Benchmarking Embodied World Models via IDM-Free Kinematic Grounding

<!-- claim:SF-2026-ARXIV-2607-19876:start -->Evaluating the physical consistency of embodied world models(EWMs) is a critical open challenge. While closed-loop evaluation via simulator rollouts offers a more faithful assessment of physical plausibility than open-loop alternatives, existing frameworks almost exclusively rely on Inverse Dynamics Models(IDMs) for action extraction. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19876:end -->

**为什么进入候选分母。** 摘要首要问题为“Evaluating the physical consistency of embodied world models(EWMs) is a critical open challenge.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** To reduce this ambiguity, we present KineBench, an IDM-free closed-loop benchmark for EWMs, built upon an explicit kinematic grounding pipeline.

**证据证明什么。** To reduce this ambiguity, we present KineBench, an IDM-free closed-loop benchmark for EWMs, built upon an explicit kinematic grounding pipeline.

**证据没有证明什么。** Future iterations will integrate human teleoperation data to enrich the action distribution. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19876v1#S3 — 3 Methodology; https://arxiv.org/html/2607.19876v1#S3.SS3 — 3.3 Four-Suite Benchmark Design。Evaluation：https://arxiv.org/html/2607.19876v1#S2.SS2 — 2.2 Benchmarks for Embodied World Models; https://arxiv.org/html/2607.19876v1#S2.SS3 — 2.3 Evaluation Metrics: From Pixels to 3D Kinematics。Limitations / counterevidence：https://arxiv.org/html/2607.19876v1#S5 — 5 Discussion and Limitations; https://arxiv.org/html/2607.19876v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/minecraft-zzz/KineBench, https://huggingface.co/datasets/Zorkzak/KineBenchDatasets, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Future iterations will integrate human teleoperation data to enrich the action distribution.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19876:end -->

<!-- review:SF-2026-ARXIV-2607-19880:start -->
### EA-Nav: Learning Safe Visual Navigation Policies with Embodiment Awareness

<!-- claim:SF-2026-ARXIV-2607-19880:start -->Cross-embodiment navigation is a key challenge in embodied intelligence. Due to differences in embodiment, the same visual observation may imply different actions for different agents, making prediction ambiguous when relying solely on vision. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19880:end -->

**为什么进入候选分母。** 摘要首要问题为“Cross-embodiment navigation is a key challenge in embodied intelligence.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** To address these challenges, we propose an imitation-learning-based embodiment-aware navigation framework with a modular multi-stage design.

**证据证明什么。** Experimental results show that the proposed method effectively improves navigation performance across different embodiment settings, demonstrating the effectiveness of incorporating embodiment geometry into embodied navigation.

**证据没有证明什么。** Our current method does not comprehensively model a wider range of embodiment-related factors, such as turning radius and motion constraints, which limits real-world deployment across embodiments with different motion patterns. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19880v1#A1.SS5 — A.5. Model Architecture and Ablation Details; https://arxiv.org/html/2607.19880v1#S3 — 3. Method。Evaluation：https://arxiv.org/html/2607.19880v1#A1.SS4 — A.4. Evaluation Environment Setup; https://arxiv.org/html/2607.19880v1#A1.SS5 — A.5. Model Architecture and Ablation Details。Limitations / counterevidence：https://arxiv.org/html/2607.19880v1#S5 — 5. Conclusion and Limitation。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Our current method does not comprehensively model a wider range of embodiment-related factors, such as turning radius and motion constraints, which limits real-world deployment across embodiments with different motion patterns.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19880:end -->

<!-- review:SF-2026-ARXIV-2607-19894:start -->
### Defense Against LLM Backdoors using Critical Neuron Isolation Pruning

<!-- claim:SF-2026-ARXIV-2607-19894:start -->Large language models (LLMs) are vulnerable to backdoor attacks, where hidden triggers induce malicious outputs. Existing defenses generally fall into inference-time detection or training-time mitigation, but face two key limitations. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19894:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language models (LLMs) are vulnerable to backdoor attacks, where hidden triggers induce malicious outputs.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** Consequently, these methods focus on surface-level behavioral patterns while neglecting the deeper representational causes of malicious activations.

**证据证明什么。** Extensive evaluations on six open-source LLMs and two benchmark datasets demonstrate that DeCNIP achieves over 95% relative reduction in Attack Success Rate (ASR), outperforming seven state-of-the-art defenses with only 0.1% neuron intervention.

**证据没有证明什么。** Threat Model We define a realistic threat model that considers the objectives and capabilities of both an attacker who poisons the model and a defender who aims to mitigate the threat. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19894v1#S3.SS2 — 3.2. Observing Model Behaviors; https://arxiv.org/html/2607.19894v1#S4 — 4. Threat Model。Evaluation：https://arxiv.org/html/2607.19894v1#A2 — Appendix B Evaluation; https://arxiv.org/html/2607.19894v1#A2.SS1 — B.1. Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.19894v1#S10 — 10. Conclusion; https://arxiv.org/html/2607.19894v1#S4 — 4. Threat Model。

**Artifact boundary。** Exact v1 links https://github.com/tatsu-lab/stanford_alpaca, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Threat Model We define a realistic threat model that considers the objectives and capabilities of both an attacker who poisons the model and a defender who aims to mitigate the threat.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19894:end -->

<!-- review:SF-2026-ARXIV-2607-19899:start -->
### Harnessing Disagreement: Detecting Correlated Agreement Blindness in Multi-Agent Triage

<!-- claim:SF-2026-ARXIV-2607-19899:start -->Disagreement-triggered escalation can create a structural blind spot in multi-agent arbitration: as base learners improve, they tend to converge, weakening safety monitoring where correlated failures concentrate. We term this correlated agreement blindness and present ARAT (Arbitrated Reasoning Agents for Alarm Triage), a directed-star system combining an inductive Random Forest (RF) agent, an analogical case-based k-nearest neighbour (k-NN) agent, and a calibrated meta-model to mitigate this effect. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19899:end -->

**为什么进入候选分母。** 摘要首要问题为“Disagreement-triggered escalation can create a structural blind spot in multi-agent arbitration: as base learners improve, they tend to converge, weakening safety monitoring where correlated failures concentrate.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We term this correlated agreement blindness and present ARAT (Arbitrated Reasoning Agents for Alarm Triage), a directed-star system combining an inductive Random Forest (RF) agent, an analogical case-based k-nearest neighbour (k-NN) agent, and a calibrated meta-model to mitigate this effect.

**证据证明什么。** ARAT reduces under-prediction relative to soft voting from 4.80% to 1.70% via conservative override (-2.6pp) and a safety-flag gate (-0.5pp), demonstrating architectural gains.

**证据没有证明什么。** Finally, we benchmark against single-model, loss-tuned, and naive aggregation baselines but not learned multi-agent coordination frameworks, which ARAT deliberately forgoes in favour of auditable fixed routing; that comparison is future work. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19899v1#S4 — 4 ARAT Architecture; https://arxiv.org/html/2607.19899v1#S6.SS4 — 6.4 Escalation Model and Routing Signals。Evaluation：https://arxiv.org/html/2607.19899v1#S5 — 5 Experimental Setup; https://arxiv.org/html/2607.19899v1#S6 — 6 Results。Limitations / counterevidence：https://arxiv.org/html/2607.19899v1#S7 — 7 Discussion; https://arxiv.org/html/2607.19899v1#S8 — 8 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/McDonnelletal/arat-paper, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Finally, we benchmark against single-model, loss-tuned, and naive aggregation baselines but not learned multi-agent coordination frameworks, which ARAT deliberately forgoes in favour of auditable fixed routing; that comparison is future work.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MULTI-AGENT`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19899:end -->

<!-- review:SF-2026-ARXIV-2607-19910:start -->
### MV-Bench: Benchmarking Multimodal Large Language Models for Coordinated Multi-View Interface Construction

<!-- claim:SF-2026-ARXIV-2607-19910:start -->Multimodal large language models (MLLMs) are increasingly expected to automate visualization development by generating code directly from visual designs. However, existing evaluations mainly focus on single-chart generation and overlook coordinated multi-view interface construction, which requires joint reasoning about data semantics, view coordination, and interaction logic. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19910:end -->

**为什么进入候选分母。** 摘要首要问题为“Multimodal large language models (MLLMs) are increasingly expected to automate visualization development by generating code directly from visual designs.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We introduce MV-Bench, a benchmark for evaluating MLLMs on coordinated multi-view interface construction.

**证据证明什么。** Iterative refinement improves code executability but does not substantially reduce the gap in data binding and interaction generation.

**证据没有证明什么。** Our metrics do not exhaustively capture all data-semantic errors, and interaction replay covers only the episodes encoded in the specification rather than all possible user trajectories. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19910v1#S2.SS3 — 2.3 Coordinated Multi-View Interface Design and Benchmarking; https://arxiv.org/html/2607.19910v1#S4 — 4 Evaluation Methodology。Evaluation：https://arxiv.org/html/2607.19910v1#S5 — 5 Experimental Results; https://arxiv.org/html/2607.19910v1#S2.SS3 — 2.3 Coordinated Multi-View Interface Design and Benchmarking。Limitations / counterevidence：https://arxiv.org/html/2607.19910v1#S6.SS2 — 6.2 Limitations and Future Directions; https://arxiv.org/html/2607.19910v1#S6 — 6 Discussion。

**Artifact boundary。** Exact v1 links https://aclanthology.org/2023.acl-demo.11/, https://dx.doi.org/10.18653/v1/2023.acl-demo.11, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Our metrics do not exhaustively capture all data-semantic errors, and interaction replay covers only the episodes encoded in the specification rather than all possible user trajectories.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19910:end -->

<!-- review:SF-2026-ARXIV-2607-19913:start -->
### JANUS: Foreseeing Latent Risk for Long-Horizon Agent Safety

<!-- claim:SF-2026-ARXIV-2607-19913:start -->Agent safety is moving from content moderation toward preventing operational failures before tool-using agents act. We propose Janus, a foresight-oriented framework for long-horizon agent safety that trains guards to anticipate delayed risks from partial trajectories. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19913:end -->

**为什么进入候选分母。** 摘要首要问题为“Agent safety is moving from content moderation toward preventing operational failures before tool-using agents act.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** We propose Janus, a foresight-oriented framework for long-horizon agent safety that trains guards to anticipate delayed risks from partial trajectories.

**证据证明什么。** Across four agent-safety benchmarks, Vanguard improves average protection by 15.9 percentage points over baseline guards while increasing benign task completion by 5.1 percentage points.

**证据没有证明什么。** These findings highlight future-risk anticipation as a key capability for building proactive, trajectory-aware safeguards for tool-using agents. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19913v1#Sx2 — Method; https://arxiv.org/html/2607.19913v1#A1.SSx2 — Additional Implementation Details。Evaluation：https://arxiv.org/html/2607.19913v1#A1 — Appendix A Experimental Setup; https://arxiv.org/html/2607.19913v1#A1.SSx1 — Benchmark Configuration。Limitations / counterevidence：https://arxiv.org/html/2607.19913v1#Sx6 — Conclusion; https://arxiv.org/html/2607.19913v1#Sx7 — Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：These findings highlight future-risk anticipation as a key capability for building proactive, trajectory-aware safeguards for tool-using agents.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-PLATFORM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19913:end -->

<!-- review:SF-2026-ARXIV-2607-19919:start -->
### Diffusion ReRoll: Revisable Denoising for Robotic Sequential Prediction

<!-- claim:SF-2026-ARXIV-2607-19919:start -->We propose Diffusion ReRoll, a diffusion-based framework for robotic sequential prediction that enables revisable denoising over horizons. Existing diffusion-based sequence predictors typically perform a single monotonic denoising process. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19919:end -->

**为什么进入候选分母。** 摘要首要问题为“We propose Diffusion ReRoll, a diffusion-based framework for robotic sequential prediction that enables revisable denoising over horizons.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We propose Diffusion ReRoll, a diffusion-based framework for robotic sequential prediction that enables revisable denoising over horizons.

**证据证明什么。** In unified video-action prediction, Diffusion ReRoll improves policy and inverse dynamics performance, especially under out-of-distribution evaluation, and achieves the best action-video consistency.

**证据没有证明什么。** Validation in general robot models or larger VLAs remains future work. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19919v1#S1 — 1 Introduction; https://arxiv.org/html/2607.19919v1#S2 — 2 Preliminaries。Evaluation：https://arxiv.org/html/2607.19919v1#A3 — Appendix C Experiment Settings; https://arxiv.org/html/2607.19919v1#A4 — Appendix D Additional Results。Limitations / counterevidence：https://arxiv.org/html/2607.19919v1#S5 — 5 Limitations; https://arxiv.org/html/2607.19919v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Validation in general robot models or larger VLAs remains future work.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19919:end -->

<!-- review:SF-2026-ARXIV-2607-19922:start -->
### DGNA: Dissecting GPU NUMA Architecture through Microbenchmarking and Data Analysis

<!-- claim:SF-2026-ARXIV-2607-19922:start -->Graphics Processing Units (GPUs), due to their immense parallel processing capabilities, have become essential across various fields, including gaming and artificial intelligence. With significant advancements in GPU cores, GPU memory efficiency has lagged, resulting in bottlenecks that can limit workload efficiency. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19922:end -->

**为什么进入候选分母。** 摘要首要问题为“Graphics Processing Units (GPUs), due to their immense parallel processing capabilities, have become essential across various fields, including gaming and artificial intelligence.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** In this paper, we introduce DGNA, a methodology designed to unveil the NUMA architecture of the GPU memory hierarchy through microbenchmarking and data analysis.

**证据证明什么。** To the best of our knowledge, this is the first paper to detail the NUMA architecture within the GPU memory subsystem.

**证据没有证明什么。** DGNA independently measures L2 and DRAM latencies without relying on vendor-specific instructions, ensuring accurate metrics by using a Gaussian mixture model to filter outliers. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19922v1#S4 — 4. Methodology; https://arxiv.org/html/2607.19922v1#S4.SS2 — 4.2. NUMA Architecture Topology。Evaluation：https://arxiv.org/html/2607.19922v1#S5 — 5. Evaluation; https://arxiv.org/html/2607.19922v1#S5.SS1 — 5.1. Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.19922v1#S6 — 6. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：DGNA independently measures L2 and DRAM latencies without relying on vendor-specific instructions, ensuring accurate metrics by using a Gaussian mixture model to filter outliers.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-GPU-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19922:end -->

<!-- review:SF-2026-ARXIV-2607-19932:start -->
### Efficient Chain-of-Modality Reasoning via Progressive Compression for Spoken Language Models

<!-- claim:SF-2026-ARXIV-2607-19932:start -->Spoken language models (SLMs) enable natural human-computer interaction, but their reasoning ability still lags behind that of text-based large language models, especially on spoken mathematical question answering tasks. One important reason is that SLMs reason over purely verbalized mathematical expressions, which are harder to interpret than symbolic text. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19932:end -->

**为什么进入候选分母。** 摘要首要问题为“Spoken language models (SLMs) enable natural human-computer interaction, but their reasoning ability still lags behind that of text-based large language models, especially on spoken mathematical question answering tasks.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** To address this challenge, we propose Efficient Chain-of-Modality Reasoning (ECoM Reasoning), the first framework to introduce compressed reasoning into SLMs.

**证据证明什么。** Experiments on spoken mathematical question answering benchmarks show that ECoM Reasoning improves accuracy by 21% over standard CoM without explicit reasoning, and by 3% over CoM with full reasoning traces while using only 40% of the text tokens, demonstrating that it enhances SLM reasoning while remaining inference-efficient.

**证据没有证明什么。** Third, our study is limited to English and does not evaluate cross-lingual or multilingual settings. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19932v1#A5 — Appendix E Other Efficient-reasoning Methods; https://arxiv.org/html/2607.19932v1#S3 — 3. Method。Evaluation：https://arxiv.org/html/2607.19932v1#S4.SS3 — 4.3. Ablation and Analysis; https://arxiv.org/html/2607.19932v1#A3 — Appendix C Evaluation Configuration。Limitations / counterevidence：https://arxiv.org/html/2607.19932v1#S5 — 5. Limitations; https://arxiv.org/html/2607.19932v1#S6 — 6. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：Third, our study is limited to English and does not evaluate cross-lingual or multilingual settings.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-REPRESENTATION`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19932:end -->

<!-- review:SF-2026-ARXIV-2607-19949:start -->
### SenWorld: A Digital-Twin Simulation for Generating Context-Rich Evaluation Data

<!-- claim:SF-2026-ARXIV-2607-19949:start -->Smartphone personal assistants reason over longitudinal personal data, yet evaluating them requires context-rich evaluation data whose correct answers are known, and real device traces are too privacy-sensitive to share. To address this challenge, we present SenWorld, a physically grounded, deterministic, event-sourced digital-twin simulation that generates such data with ground truth fixed by construction. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19949:end -->

**为什么进入候选分母。** 摘要首要问题为“Smartphone personal assistants reason over longitudinal personal data, yet evaluating them requires context-rich evaluation data whose correct answers are known, and real device traces are too privacy-sensitive to share.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** We evaluate this method with 16 personas in Beijing.

**证据证明什么。** Overall, SenWorld offers a privacy-safe, reproducible, and distribution-checked path to evaluation data whose labels are fixed by construction.

**证据没有证明什么。** The benchmark, the generated data, and the evaluation cases cannot be released under the applicable data-governance policy. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19949v1#S3 — III The SenWorld Method; https://arxiv.org/html/2607.19949v1#S3.SS1 — III-A Overview and Method Contract。Evaluation：https://arxiv.org/html/2607.19949v1#S4 — IV Evaluation Setup; https://arxiv.org/html/2607.19949v1#S4.SS3 — IV-C RQ1: Benchmark Comparison。Limitations / counterevidence：https://arxiv.org/html/2607.19949v1#S6 — VI Conclusion and Future Work。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：The benchmark, the generated data, and the evaluation cases cannot be released under the applicable data-governance policy.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`principle_reuse`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19949:end -->

<!-- review:SF-2026-ARXIV-2607-19957:start -->
### HijackKV: New Threat in Position-Independent KV Cache Reuse

<!-- claim:SF-2026-ARXIV-2607-19957:start -->Key-Value (KV) cache reduces inference latency in large language models (LLMs). Traditional prefix-based reuse has low cache hit rates across inference requests because it requires exact token and position matches. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19957:end -->

**为什么进入候选分母。** 摘要首要问题为“Key-Value (KV) cache reduces inference latency in large language models (LLMs).”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** We introduce HIJACKKV, the first attack framework that systematically exploits this vulnerability, demonstrating its severity and practicality.

**证据证明什么。** We show this design introduces a new threat, KV Cache Hijacking.

**证据没有证明什么。** 4.1 Threat Model We formally define the threat model guiding our analysis, including the system model, the attacker’s goal, capability, and knowledge. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19957v1#S4.SS1 — 4.1 Threat Model。Evaluation：https://arxiv.org/html/2607.19957v1#S6 — 6 Experimental Setup; https://arxiv.org/html/2607.19957v1#S7 — 7 Experiment。Limitations / counterevidence：https://arxiv.org/html/2607.19957v1#S8 — 8 Limitations and Discussion; https://arxiv.org/html/2607.19957v1#S4.SS1 — 4.1 Threat Model。

**Artifact boundary。** Exact v1 links https://github.com/YichiCS/KV-Cache-Hijack, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：4.1 Threat Model We formally define the threat model guiding our analysis, including the system model, the attacker’s goal, capability, and knowledge.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-KV-CACHE`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19957:end -->

<!-- review:SF-2026-ARXIV-2607-19962:start -->
### EvoThink: Evolving Thinking in Large Reasoning Models via Self-Pruning and Aha-Moment Preference Optimization

<!-- claim:SF-2026-ARXIV-2607-19962:start -->Large Reasoning Models (LRMs) often suffer from overthinking due to redundant verification steps. Existing approaches for mitigating overthinking, such as fast-slow thinking switching and reasoning trajectory compression, fail to make a fine-grained distinction between beneficial and redundant steps within the LRM's reasoning process, and may thus impair reasoning capability in their pursuit of efficiency. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19962:end -->

**为什么进入候选分母。** 摘要首要问题为“Large Reasoning Models (LRMs) often suffer from overthinking due to redundant verification steps.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** To simultaneously improve reasoning efficiency and capability, we propose EvoThink, a framework that reduces redundant verification and encourages the exploration of new reasoning paths.

**证据证明什么。** Extensive evaluations across mathematical reasoning and code generation benchmarks demonstrate that EvoThink not only substantially reduces inference-time token usage but also improves the reasoning capability of LRMs.

**证据没有证明什么。** For future work, we plan to investigate why the from-wrong-to-right learning pattern adopted by AMPO is particularly effective for model training. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19962v1#S3 — 3 Method。Evaluation：https://arxiv.org/html/2607.19962v1#S4 — 4 Experiments; https://arxiv.org/html/2607.19962v1#S4.SS1 — 4.1 Experimental Setups。Limitations / counterevidence：https://arxiv.org/html/2607.19962v1#S5 — 5 Conclusion and Future Work。

**Artifact boundary。** Exact v1 links https://huggingface.co/datasets/math-ai/aime25, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：For future work, we plan to investigate why the from-wrong-to-right learning pattern adopted by AMPO is particularly effective for model training.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-DPO`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19962:end -->

<!-- review:SF-2026-ARXIV-2607-19971:start -->
### Unified Prediction and Planning via Conflict-Aware Disjoint Parameter Training

<!-- claim:SF-2026-ARXIV-2607-19971:start -->Accurate motion prediction of surrounding agents and safe motion planning are two closely coupled key tasks for social robot navigation in crowded environments. Deploying these systems on resource-constrained edge devices necessitates compact, unified models that can perform both tasks simultaneously. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19971:end -->

**为什么进入候选分母。** 摘要首要问题为“Accurate motion prediction of surrounding agents and safe motion planning are two closely coupled key tasks for social robot navigation in crowded environments.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** To resolve this, we propose a novel model-merging-based framework, Disjoint Parameter Training (DPT).

**证据证明什么。** Evaluated on standard crowd navigation benchmarks (JRDB and JTA), our framework demonstrates superior performance, validating its versatility and effectiveness for safe, resource-efficient robot navigation.

**证据没有证明什么。** 15 Future Direction As a future direction, DPT can be extended to more general multi-task settings with a larger number of tasks. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19971v1#S11.SS1 — 11.1 Skill Conflict in Other Architecture; https://arxiv.org/html/2607.19971v1#S3 — 3 Methods。Evaluation：https://arxiv.org/html/2607.19971v1#S4.SS2 — 4.2 Experimental Results; https://arxiv.org/html/2607.19971v1#S10 — 10 Qualitative Results。Limitations / counterevidence：https://arxiv.org/html/2607.19971v1#S15 — 15 Future Direction; https://arxiv.org/html/2607.19971v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：15 Future Direction As a future direction, DPT can be extended to more general multi-task settings with a larger number of tasks.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19971:end -->

<!-- review:SF-2026-ARXIV-2607-19985:start -->
### Coordinating from Memory: Graph-Structured Experience Reuse for Multi-Agent Adaptation in Dynamic Manufacturing

<!-- claim:SF-2026-ARXIV-2607-19985:start -->Dynamic manufacturing environments require multi-agent systems to coordinate effectively under frequent operational disturbances such as machine failures, urgent job arrivals, and processing time variations. Existing multi-agent reinforcement learning approaches treat each disturbance episode independently, discarding valuable coordination experience that could accelerate future adaptation. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19985:end -->

**为什么进入候选分母。** 摘要首要问题为“Dynamic manufacturing environments require multi-agent systems to coordinate effectively under frequent operational disturbances such as machine failures, urgent job arrivals, and processing time variations.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** In this paper, we propose a Graph-Structured Experiential Memory (GSEM) framework for multi-agent coordination in dynamic manufacturing.

**证据证明什么。** Experiments on dynamic flexible job-shop scheduling benchmarks with three disturbance types show that GSEM reduces makespan by 4.1%-10.0% and adaptation time by 33%-38% compared to the strongest memory-augmented baseline, with the advantage increasing under higher disturbance frequency.

**证据没有证明什么。** Future directions include scaling to larger instances, integrating human operator feedback, and extending the framework to other dynamic combinatorial optimization domains. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19985v1#S3 — III PROPOSED METHOD。Evaluation：https://arxiv.org/html/2607.19985v1#S4 — IV EXPERIMENTS; https://arxiv.org/html/2607.19985v1#S4.SS1 — IV-A Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.19985v1#S5 — V CONCLUSION。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Future directions include scaling to larger instances, integrating human operator feedback, and extending the framework to other dynamic combinatorial optimization domains.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MULTI-AGENT`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19985:end -->

<!-- review:SF-2026-ARXIV-2607-19996:start -->
### CLARK: Closed-loop Learning for Adaptive Reasoning over Knowledge Graphs

<!-- claim:SF-2026-ARXIV-2607-19996:start -->Machine Learning models are widely used for automating classification tasks by extracting statistical patterns from data. However, their performance deteriorates if the data distribution changes, making them ill-suited to handle uncertain and evolving information. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19996:end -->

**为什么进入候选分母。** 摘要首要问题为“Machine Learning models are widely used for automating classification tasks by extracting statistical patterns from data.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** To address these limitations, we present CLARK (Closed-loop Learning for Adaptive Reasoning over Knowledge Graphs), a framework that integrates knowledge graphs, symbolic rule mining, and probabilistic reasoning under the Logic Programs with Markov Logic Networks (LP$^{\text{MLN}}$) formalism.

**证据证明什么。** Results demonstrate that CLARK leads to improved classification performance and more generalisable inference.

**证据没有证明什么。** Several directions for future work emerge from this study. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19996v1#S4 — 4 Methods; https://arxiv.org/html/2607.19996v1#S3.SS1 — 3.1 Logic Programs and Stable Model Semantics。Evaluation：https://arxiv.org/html/2607.19996v1#S5 — 5 Experiments; https://arxiv.org/html/2607.19996v1#S6 — 6 Discussion on Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.19996v1#S7 — 7 Conclusions and Future Work; https://arxiv.org/html/2607.19996v1#S6 — 6 Discussion on Experiments。

**Artifact boundary。** Exact v1 links https://github.com/azreasoners/lpmln, https://github.com/dig-team/amie, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Several directions for future work emerge from this study.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-RAG`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19996:end -->

<!-- review:SF-2026-ARXIV-2607-20064:start -->
### PRO-LONG: Programmatic Memory Enables Long-Horizon Reasoning

<!-- claim:SF-2026-ARXIV-2607-20064:start -->Long-horizon tasks require sustained perception, reasoning, and exploration, and are a persistent challenge for large language model (LLM) agents. This gap is reflected in their limited performance on continual learning benchmarks such as ARC-AGI-3, especially when models are evaluated out of the box. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20064:end -->

**为什么进入候选分母。** 摘要首要问题为“Long-horizon tasks require sustained perception, reasoning, and exploration, and are a persistent challenge for large language model (LLM) agents.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We propose PRO-LONG, a minimal context management framework built around programmatic memory for LLM agents in long-horizon, exploratory settings.

**证据证明什么。** With Fable 5, PRO-LONG achieves 97.4% best@2 at a total cost of \$1,750.

**证据没有证明什么。** This variance motivates several directions for future work. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20064v1#A2.SS1 — B.1 System Prompt: (PRO-LONG); https://arxiv.org/html/2607.20064v1#A2.SS2 — B.2 System Prompt: No-Log。Evaluation：https://arxiv.org/html/2607.20064v1#S3 — 3 Main Results; https://arxiv.org/html/2607.20064v1#S3.SS1 — 3.1 Benchmark Performance。Limitations / counterevidence：https://arxiv.org/html/2607.20064v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/alexisfox7/PRO-LONG, https://github.com/arcprize/ARC-AGI-3-Agents, https://github.com/DriesSmit/ARC3-solution; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：This variance motivates several directions for future work.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20064:end -->

<!-- review:SF-2026-ARXIV-2607-20083:start -->
### Co-Evolving LLM Evaluators and Policies via DynamicRubric

<!-- claim:SF-2026-ARXIV-2607-20083:start -->Post-training with evaluator feedback on policy-induced samples serves as a major mechanism for improving large language models. As policies improve, these sampled responses become close in quality. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20083:end -->

**为什么进入候选分母。** 摘要首要问题为“Post-training with evaluator feedback on policy-induced samples serves as a major mechanism for improving large language models.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Motivated by this view, we propose DynamicRubric, a response-set-conditioned evaluator--policy co-evolution framework that generates weighted binary rubric items for each candidate set and aggregates the resulting judgments into response-level scores.

**证据证明什么。** As policies improve, these sampled responses become close in quality.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20083v1#S3 — 3 Methodology; https://arxiv.org/html/2607.20083v1#A1 — Appendix A DynamicRubric Training Algorithm。Evaluation：https://arxiv.org/html/2607.20083v1#A3.SS1 — C.1 Benchmark Details for Evaluator Evaluation; https://arxiv.org/html/2607.20083v1#A3.SS2 — C.2 Benchmark Details for Open-Ended Generation Tasks Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.20083v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.20083v1#Sx1 — Limitations。

**Artifact boundary。** Exact v1 links https://github.com/huggingface/math-verify, https://github.com/tatsu-lab/alpaca_eval, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20083:end -->

<!-- review:SF-2026-ARXIV-2607-20090:start -->
### Reinforcement Learning for Large Language Model Selective Evidence Adoption from Contaminated Retrieval Results

<!-- claim:SF-2026-ARXIV-2607-20090:start -->Retrieval-augmented large language models frequently face contexts that interleave useful evidence with misleading statements or instruction-like content. Blanket refusal discards valid evidence, whereas uncritical adoption yields incorrect or unsafe answers. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20090:end -->

**为什么进入候选分母。** 摘要首要问题为“Retrieval-augmented large language models frequently face contexts that interleave useful evidence with misleading statements or instruction-like content.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** We introduce SelectBench, a controlled benchmark and training set for selective evidence adoption, and post-train Qwen3.5-4B directly with DAPO using either deterministic rule rewards or a frozen semantic judge.

**证据证明什么。** These results demonstrate a directional improvement in selective evidence use, while identifying injection resistance and statistical robustness as important remaining challenges for future work.

**证据没有证明什么。** The gains are modest, do not remain significant after multiple-comparison correction, and do not improve prompt-injection following. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20090v1#S3 — 3 Methodology; https://arxiv.org/html/2607.20090v1#S6.SS2 — 6.2 Large Language Models as Agents。Evaluation：https://arxiv.org/html/2607.20090v1#S5 — 5 Results and Analysis; https://arxiv.org/html/2607.20090v1#S4 — 4 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.20090v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：The gains are modest, do not remain significant after multiple-comparison correction, and do not improve prompt-injection following.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-RAG`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20090:end -->

<!-- review:SF-2026-ARXIV-2607-20110:start -->
### Extreme-RGMT: Continual Learning of Highly Dynamic Skills for Robust Generalist Humanoid Control

<!-- claim:SF-2026-ARXIV-2607-20110:start -->Humans can progressively acquire highly dynamic motor skills while preserving reliable everyday motor abilities. In contrast, existing humanoid controllers face a trade-off between generalist and specialist capabilities: generalist motion tracking policies struggle to reliably execute rare highly dynamic motions, whereas specialist training can degrade previously acquired behaviors. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20110:end -->

**为什么进入候选分母。** 摘要首要问题为“Humans can progressively acquire highly dynamic motor skills while preserving reliable everyday motor abilities.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We introduce Extreme-RGMT, a two-stage continual learning framework for robust generalist humanoid control.

**证据证明什么。** Experiments show that Extreme-RGMT achieves state-of-the-art generalist whole-body motion-tracking performance, including substantially improved completion of challenging highly dynamic motions.

**证据没有证明什么。** Accordingly, the policy has limited generalization to motions that differ substantially from the training distribution. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20110v1#S3 — III System Overview; https://arxiv.org/html/2607.20110v1#S4.SS1 — IV-A Policy Architecture。Evaluation：https://arxiv.org/html/2607.20110v1#S6.SS2 — VI-B Ablation and Analysis; https://arxiv.org/html/2607.20110v1#S6 — VI Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.20110v1#S6.SS4 — VI-D Limitations; https://arxiv.org/html/2607.20110v1#S7 — VII Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Accordingly, the policy has limited generalization to motions that differ substantially from the training distribution.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20110:end -->

<!-- review:SF-2026-ARXIV-2607-20120:start -->
### Ascend to Science: Exploration of AI Chips for Scientific Computing

<!-- claim:SF-2026-ARXIV-2607-20120:start -->The rapid rise of AI-oriented accelerators has reshaped compute systems around low-precision tensor engines, raising a practical question for the HPC community: under what conditions can such hardware support scientific workloads that demand numerical robustness, irregular memory access, and scalability? Using the Ascend 910 NPU series as a representative tensor-centric platform, we characterize precision, execution, and memory-hierarchy bottlenecks that hinder the direct deployment of scientific codes. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20120:end -->

**为什么进入候选分母。** 摘要首要问题为“The rapid rise of AI-oriented accelerators has reshaped compute systems around low-precision tensor engines, raising a practical question for the HPC community: under what conditions can such hardware support scientific workloads that demand numerical robustness, irregular memory access, and scalability?”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** The rapid rise of AI-oriented accelerators has reshaped compute systems around low-precision tensor engines, raising a practical question for the HPC community: under what conditions can such hardware support scientific workloads that demand numerical robustness, irregular memory access, and scalability?

**证据证明什么。** These studies show that AI-native NPUs can achieve numerical robustness, competitive performance, and satisfactory scalability when numerical formulation, execution placement, and data movement are addressed in a coordinated manner.

**证据没有证明什么。** We therefore do not claim architecture-independent performance, but instead identify which optimization principles generalize and which remain platform-specific. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20120v1#S2.SS1 — 2.1 Precision-Oriented Approaches; https://arxiv.org/html/2607.20120v1#S2.SS3 — 2.3 Memory- and Communication-Centric Approaches。Evaluation：https://arxiv.org/html/2607.20120v1#S4 — 4 Experimental Setup; https://arxiv.org/html/2607.20120v1#S4.SS2 — 4.2 Experimental Environment。Limitations / counterevidence：https://arxiv.org/html/2607.20120v1#S7 — 7 Conclusion and Future Work。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：We therefore do not claim architecture-independent performance, but instead identify which optimization principles generalize and which remain platform-specific.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-GPU-SCHEDULER`；evidence-stage relation：`principle_reuse`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20120:end -->

<!-- review:SF-2026-ARXIV-2607-20121:start -->
### OpenSkillRisk: Benchmarking Agent Safety When Using Real-World Risky Third-Party Skills

<!-- claim:SF-2026-ARXIV-2607-20121:start -->LLM-based agents leverage third-party skills to extend their capabilities in open-world scenarios. However, third-party skills can introduce extra security vulnerabilities, as seemingly harmless skills can contain latent safety risks that only emerge during actual execution. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20121:end -->

**为什么进入候选分母。** 摘要首要问题为“LLM-based agents leverage third-party skills to extend their capabilities in open-world scenarios.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** Context-dependent and system-level risks are especially difficult for current agent systems to avoid.

**证据证明什么。** Experimental results show that no tested system handles risky skills reliably: even the safest configurations still execute unsafe actions in about 17% of cases.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20121v1#S4.SS2 — 4.2 RQ1. How Robust Are Current Agent Systems to Real-World Risky Skills?。Evaluation：https://arxiv.org/html/2607.20121v1#A2 — Appendix B Benchmark Construction Details; https://arxiv.org/html/2607.20121v1#A2.SS6 — B.6 Benchmark Statistics。Limitations / counterevidence：https://arxiv.org/html/2607.20121v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/Miaow-Lab/OpenSkillRisk, https://code.claude.com/docs/en/overview, https://code.claude.com/docs/en/permissions; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-TOOL-CALLING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20121:end -->

<!-- review:SF-2026-ARXIV-2607-20125:start -->
### HeadCast: Casting Attention Heads for Efficient Autoregressive Video Generation

<!-- claim:SF-2026-ARXIV-2607-20125:start -->Autoregressive (AR) video diffusion models have become a promising paradigm for long and streaming video synthesis, but the continuously growing Key-Value (KV) cache makes attention the dominant inference cost, especially at high resolution where each frame contributes many tokens. Existing remedies either evict the cache with coarse heuristics that cause inter-frame flickering, or require model re-training. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20125:end -->

**为什么进入候选分母。** 摘要首要问题为“Autoregressive (AR) video diffusion models have become a promising paradigm for long and streaming video synthesis, but the continuously growing Key-Value (KV) cache makes attention the dominant inference cost, especially at high resolution where each frame contributes many tokens.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** We propose HeadCast, a training-free, plug-and-play acceleration framework built on the observation that a pre-trained AR model's attention heads exhibit stable, heterogeneous behaviors.

**证据证明什么。** Code is available at https://github.com/sjlgaga/HeadCast .

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20125v1#S1 — 1 Introduction; https://arxiv.org/html/2607.20125v1#S2 — 2 Related Work。Evaluation：https://arxiv.org/html/2607.20125v1#A6 — Appendix F Additional Qualitative Results; https://arxiv.org/html/2607.20125v1#S5 — 5 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.20125v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/sjlgaga/HeadCast, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-GENERATIVE-PARADIGMS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20125:end -->

<!-- review:SF-2026-ARXIV-2607-20129:start -->
### CUSUM-Shaped Inference-Time Monitoring and Targeted Re-Decoding for Quantized Small Language Model Reasoning

<!-- claim:SF-2026-ARXIV-2607-20129:start -->Quantized small reasoning models can enter repetitive or otherwise unproductive trajectories, yet standard decoding does not adapt to the trajectory as it unfolds. We study MGT-B, a fixed, weight-preserving controller that converts overlapping windows of uncertainty, repetition, and local-change features into position-conditional empirical tail probabilities. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20129:end -->

**为什么进入候选分母。** 摘要首要问题为“Quantized small reasoning models can enter repetitive or otherwise unproductive trajectories, yet standard decoding does not adapt to the trajectory as it unfolds.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** On MATH-500, a paired three-seed evaluation over 1,500 generations per method raises exact-normalized accuracy from 54.73% for vanilla decoding to 56.40% (+1.67 percentage points; problem-clustered bootstrap 95% CI [+0.47, +2.80]), while a prospectively profiled random-intervention control reaches 54.60%.

**证据证明什么。** Seed-0 ablations show that rollback alone does not explain the result and that an isolated repetition penalty is harmful.

**证据没有证明什么。** The broader 467-pair historical-coverage set yields a larger 4.50-point difference, but it includes seed-1 IDs exposed before or during threshold selection and is therefore not treated as independent evidence for . 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20129v1#A3 — Appendix C Methodological relation to the prior preprint; https://arxiv.org/html/2607.20129v1#S4 — 4 Method。Evaluation：https://arxiv.org/html/2607.20129v1#S7 — 7 Ablations and Diagnostic Analysis; https://arxiv.org/html/2607.20129v1#A4 — Appendix D Additional experiments for component attribution and generalization。Limitations / counterevidence：https://arxiv.org/html/2607.20129v1#S8 — 8 Limitations; https://arxiv.org/html/2607.20129v1#S9 — 9 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：The broader 467-pair historical-coverage set yields a larger 4.50-point difference, but it includes seed-1 IDs exposed before or during threshold selection and is therefore not treated as independent evidence for .

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-DECODE`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20129:end -->

<!-- review:SF-2026-ARXIV-2607-20145:start -->
### SLAI T-Rex: Full-Parameter Post-training of the DeepSeek-V4 Family on Ascend SuperPOD

<!-- claim:SF-2026-ARXIV-2607-20145:start -->Full-parameter post-training of trillion-parameter-scale MoE models introduces substantial system-level challenges for large-scale distributed training, including severe memory pressure, non-overlapped communication overhead, and inefficient kernel execution. While most large-scale LLM training systems are built around GPU-based clusters, this report presents an end-to-end optimization practice on the Ascend NPU SuperPOD. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20145:end -->

**为什么进入候选分母。** 摘要首要问题为“Full-parameter post-training of trillion-parameter-scale MoE models introduces substantial system-level challenges for large-scale distributed training, including severe memory pressure, non-overlapped communication overhead, and inefficient kernel execution.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We refer to the integrated framework as SLAI T-Rex.

**证据证明什么。** The resulting system achieves 34.22% Model FLOPs Utilization (MFU) with a 2.93x improvement over the open-source baseline recipe while maintaining training stability.

**证据没有证明什么。** 5 Conclusion, Limitations, and Future Directions This technical report presents a first-stage practice for full-parameter post-training of the DeepSeek-V4 model family on Ascend NPU SuperPOD. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20145v1#A3 — Appendix C Solver-Verified OR-CPT Data Synthesis: Engine Design and Illustrative Cases; https://arxiv.org/html/2607.20145v1#A3.SS2 — C.2 End-to-end engine architecture。Evaluation：https://arxiv.org/html/2607.20145v1#S4 — 4 Experimental Results; https://arxiv.org/html/2607.20145v1#A4 — Appendix D CPT–SFT–Deployment–Evaluation Provenance。Limitations / counterevidence：https://arxiv.org/html/2607.20145v1#S5 — 5 Conclusion, Limitations, and Future Directions。

**Artifact boundary。** Exact v1 links https://github.com/SLAI-AITP/Deepseek-OR, https://huggingface.co/datasets/albertge/synthetic-orqa, https://github.com/Gurobi/modeling-examples; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：5 Conclusion, Limitations, and Future Directions This technical report presents a first-stage practice for full-parameter post-training of the DeepSeek-V4 model family on Ascend NPU SuperPOD.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`TRAIN-DISTRIBUTED-TRAINING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20145:end -->

<!-- review:SF-2026-ARXIV-2607-20146:start -->
### Gotta Catch them all: the modes of Sycophancy

<!-- claim:SF-2026-ARXIV-2607-20146:start -->Large language models often align with users' beliefs at the expense of factual accuracy, a behavior known as sycophancy. Prior mechanistic studies largely treat sycophancy as a single behavioral dimension that can be uniformly amplified or suppressed. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20146:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language models often align with users' beliefs at the expense of factual accuracy, a behavior known as sycophancy.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Prior mechanistic studies largely treat sycophancy as a single behavioral dimension that can be uniformly amplified or suppressed.

**证据证明什么。** These results show that sycophancy is not a monolithic tendency, but a structured family of representationally and computationally distinct modes, motivating more precise measurement and intervention.

**证据没有证明什么。** This creates an important gap between what models internally compute and what they express in text: output-based evaluations capture only part of the underlying behavior. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20146v1#A3 — Appendix C Method - Detailed; https://arxiv.org/html/2607.20146v1#S4 — 4 Method。Evaluation：https://arxiv.org/html/2607.20146v1#A10 — Appendix J Ablation Heatmaps: All Three Experiments; https://arxiv.org/html/2607.20146v1#A5 — Appendix E Full Clustering Results。Limitations / counterevidence：https://arxiv.org/html/2607.20146v1#S6 — 6 Discussion; https://arxiv.org/html/2607.20146v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/TransformerLensOrg/TransformerLens, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：This creates an important gap between what models internally compute and what they express in text: output-based evaluations capture only part of the underlying behavior.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`WORLDVIEW-LLM-INTELLIGENCE`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20146:end -->

<!-- review:SF-2026-ARXIV-2607-20166:start -->
### Audio-Zero: Label-Free Self-Evolution for Fine-Grained Audio Reasoning

<!-- claim:SF-2026-ARXIV-2607-20166:start -->Large Audio Language models (LALMs) have made rapid progress on acoustic understanding, yet they still struggle with fine-grained audio reasoning (e.g., recognizing event order, repetitions and duration). Existing post-training methods heavily rely on expensive external labels or provide only coarse semantic signals. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20166:end -->

**为什么进入候选分母。** 摘要首要问题为“Large Audio Language models (LALMs) have made rapid progress on acoustic understanding, yet they still struggle with fine-grained audio reasoning (e.g., recognizing event order, repetitions and duration).”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** To bridge this gap, we introduce Audio-Zero, the first label-free self-evolution framework in the field of LALMs that improves fine-grained auditory perception and reasoning.

**证据证明什么。** Experiments with Qwen2-Audio-7B-Instruct and Qwen2.5-Omni-7B on TREA, MMAU Test-mini and MMAR show that Audio-Zero improves fine-grained audio reasoning while preserving broad audio understanding.

**证据没有证明什么。** Instead of relying on human-annotated transcripts, QA labels, or reasoning traces, Audio-Zero converts unlabeled audio contrast pairs into an auditory self-play game, where the model alternates between generating listening-stage descriptions and performing attribution-stage reasoning to identify the odd listener. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20166v1#S2 — 2 Audio-Zero: A Label-Free Self-Evolution Framework; https://arxiv.org/html/2607.20166v1#A1.SS1 — A.1 Additional Implementation Details。Evaluation：https://arxiv.org/html/2607.20166v1#S3 — 3 Experiments and Analysis; https://arxiv.org/html/2607.20166v1#A2 — Appendix B Evaluation Protocol。Limitations / counterevidence：https://arxiv.org/html/2607.20166v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Instead of relying on human-annotated transcripts, QA labels, or reasoning traces, Audio-Zero converts unlabeled audio contrast pairs into an auditory self-play game, where the model alternates between generating listening-stage descriptions and performing attribution-stage reasoning to identify the odd listener.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-REPRESENTATION`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20166:end -->

<!-- review:SF-2026-ARXIV-2607-20174:start -->
### StreamHOI: Interaction-aware Temporal Memory Adaptation for Streaming HOI Video Generation

<!-- claim:SF-2026-ARXIV-2607-20174:start -->Existing human--object interaction (HOI) video generation methods are largely limited to offline short-video generation with complex driving conditions, making them unsuitable for real-time interactive applications. We present \emph{StreamHOI}, a low-latency streaming framework for long-duration HOI video generation. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20174:end -->

**为什么进入候选分母。** 摘要首要问题为“Existing human--object interaction (HOI) video generation methods are largely limited to offline short-video generation with complex driving conditions, making them unsuitable for real-time interactive applications.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We present \emph{StreamHOI}, a low-latency streaming framework for long-duration HOI video generation.

**证据证明什么。** We find that the standard sink-local memory design faces a trade-off in streaming HOI generation, and different transformer blocks show different historical-memory preferences for HOI regions and surrounding regions.

**证据没有证明什么。** VI Limitations When the human–object interaction in the reference image is unclear, such as ambiguous contact regions or occluded objects, StreamHOI may generate less stable interactions. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20174v1#S4 — IV Method。Evaluation：https://arxiv.org/html/2607.20174v1#S5 — V Experiments; https://arxiv.org/html/2607.20174v1#S5.SS1 — V-A Experimental Settings。Limitations / counterevidence：https://arxiv.org/html/2607.20174v1#S5.SS3 — V-C Ablation Studies and Discussion; https://arxiv.org/html/2607.20174v1#S6 — VI Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：VI Limitations When the human–object interaction in the reference image is unclear, such as ambiguous contact regions or occluded objects, StreamHOI may generate less stable interactions.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-GENERATIVE-PARADIGMS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20174:end -->

<!-- review:SF-2026-ARXIV-2607-20192:start -->
### On Optimization Complexity of Second-Order Certified Unlearning

<!-- claim:SF-2026-ARXIV-2607-20192:start -->We study machine unlearning: the removal of memorized training data from a trained model. Specifically, we investigate the algorithmic complexity of certified unlearning from an optimization perspective. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20192:end -->

**为什么进入候选分母。** 摘要首要问题为“We study machine unlearning: the removal of memorized training data from a trained model.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We prove fast rates for our method in achieving certified unlearning for linear models with quasi-self-concordant losses.

**证据证明什么。** Thus we theoretically demonstrate that if the removed data is well-predicted by the unlearned model, the corresponding optimization problem is simple.

**证据没有证明什么。** However, such noise may erase not only the information to be forgotten, but also useful information about the retained data , yielding a model that is far from the desired solution ( 2 ). 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20192v1#S3.SS1 — 3.1 Gradient Method Baseline; https://arxiv.org/html/2607.20192v1#S3.SS2 — 3.2 Newton Method with Gradient Regularization。Evaluation：https://arxiv.org/html/2607.20192v1#S1 — 1 Introduction; https://arxiv.org/html/2607.20192v1#S1.SS1 — 1.1 Certified Unlearning and Optimization。Limitations / counterevidence：https://arxiv.org/html/2607.20192v1#S1 — 1 Introduction; https://arxiv.org/html/2607.20192v1#S1.SS1 — 1.1 Certified Unlearning and Optimization。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：However, such noise may erase not only the information to be forgotten, but also useful information about the retained data , yielding a model that is far from the desired solution ( 2 ).

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20192:end -->

<!-- review:SF-2026-ARXIV-2607-20205:start -->
### Statistical Inference for Rank Allocation in Low-Rank Adaptation

<!-- claim:SF-2026-ARXIV-2607-20205:start -->Low-rank adaptation (LoRA) has become a widely used parameter-efficient fine-tuning method for large language models. Since different modules and layers may contribute unequally to downstream adaptation, allocating rank resources under a fixed parameter budget is an important problem for balancing efficiency, expressiveness, and generalization. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20205:end -->

**为什么进入候选分母。** 摘要首要问题为“Low-rank adaptation (LoRA) has become a widely used parameter-efficient fine-tuning method for large language models.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** Low-rank adaptation (LoRA) has become a widely used parameter-efficient fine-tuning method for large language models.

**证据证明什么。** Experiments show that StatLoRA achieves comparable or better performance than vanilla LoRA, AdaLoRA, and IGU-LoRA under matched rank budgets.

**证据没有证明什么。** Within the LoRA fine-tuning setting, we further derived central limit theory for empirical LoRA scores using the delta method. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20205v1#S4.SS3 — 4.3 The StatLoRA Algorithm。Evaluation：https://arxiv.org/html/2607.20205v1#A2.SS1 — B.1 Main Results; https://arxiv.org/html/2607.20205v1#A3.SS1 — C.1 Main Results。Limitations / counterevidence：https://arxiv.org/html/2607.20205v1#S6 — 6 Conclusion and Discussion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Within the LoRA fine-tuning setting, we further derived central limit theory for empirical LoRA scores using the delta method.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-LORA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20205:end -->

<!-- review:SF-2026-ARXIV-2607-20214:start -->
### ELSAA: Efficient Low-Rank and Sparse Attention Approximation for Training Transformers

<!-- claim:SF-2026-ARXIV-2607-20214:start -->The quadratic $N\times N$ attention score matrix remains a central obstacle to extending Transformers to longer input lengths. Existing efficient attention methods usually reduce this bottleneck by either imposing sparsity, so that each query attends to only a small subset of keys, or by using low-rank/kernel sketches, so that global interactions are compressed into a lower-dimensional representation. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20214:end -->

**为什么进入候选分母。** 摘要首要问题为“The quadratic $N\times N$ attention score matrix remains a central obstacle to extending Transformers to longer input lengths.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We propose \emph{ELSAA}, an efficient low-rank and sparse approximation of attention.

**证据证明什么。** Existing efficient attention methods usually reduce this bottleneck by either imposing sparsity, so that each query attends to only a small subset of keys, or by using low-rank/kernel sketches, so that global interactions are compressed into a lower-dimensional representation.

**证据没有证明什么。** We organize the discussion around four observations: (i) ELSAA improves on Sort_Lsh_RACE consistently, isolating the contribution of the denominator-aware correction; (ii) the relative strength of the sparse and low-rank branches reflects a fundamental structural difference between vision and long-text tasks; (iii) exact full attention is not merely expensive at very long contexts but can fail to optimize at all; and (iv) ELSAA is the only method that extrapolates reliably across all lengths on NIAH, including lengths shorter than training. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20214v1#S3 — 3 Methodology; https://arxiv.org/html/2607.20214v1#A1 — Appendix A Branch Algorithms for ELSAA。Evaluation：https://arxiv.org/html/2607.20214v1#A4 — Appendix D Experiment Hyperparameters; https://arxiv.org/html/2607.20214v1#S5 — 5 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.20214v1#A2.SS3 — B.3 Hall deficiency and weighted Hall failure; https://arxiv.org/html/2607.20214v1#S7 — 7 Results and Discussion。

**Artifact boundary。** Exact v1 links https://github.com/mahdiheidari721/ELSAA, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：We organize the discussion around four observations: (i) ELSAA improves on Sort_Lsh_RACE consistently, isolating the contribution of the denominator-aware correction; (ii) the relative strength of the sparse and low-rank branches reflects a fundamental structural difference between vision and long-text tasks; (iii) exact full attention is not merely expensive at very long contexts but can fail to optimize at all; and (iv) ELSAA is the only method that extrapolates reliably across all lengths on NIAH, including lengths shorter than training.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MODEL-SELF-ATTENTION`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20214:end -->

<!-- review:SF-2026-ARXIV-2607-20220:start -->
### MoX: Efficient MoE Routing on Direct-Connect Topologies

<!-- claim:SF-2026-ARXIV-2607-20220:start -->Optically switched networks suit the regular communication of dense ML models, but MoE introduces sparse, runtime-dependent traffic. We show that efficient offline-optimized routing enables efficient MoE training and inference on direct-connect topologies without the need for MoE traffic matrix or dynamic topology reconfiguration. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20220:end -->

**为什么进入候选分母。** 摘要首要问题为“Optically switched networks suit the regular communication of dense ML models, but MoE introduces sparse, runtime-dependent traffic.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** We show that efficient offline-optimized routing enables efficient MoE training and inference on direct-connect topologies without the need for MoE traffic matrix or dynamic topology reconfiguration.

**证据证明什么。** These results show that high-performance MoE on static direct-connect fabrics can be achieved via optimized load-oblivious routing without demand-driven reconfiguration.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20220v1#S2 — 2. Routing Algorithm。Evaluation：https://arxiv.org/html/2607.20220v1#S3 — 3. Evaluation; https://arxiv.org/html/2607.20220v1#S3.SS4 — 3.4. Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.20220v1#S4 — 4. Discussion; https://arxiv.org/html/2607.20220v1#S6 — 6. Conclusion。

**Artifact boundary。** Exact v1 links https://huggingface.co/Qwen/Qwen3.5-397B-A17B, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MODEL-MOE`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20220:end -->

<!-- review:SF-2026-ARXIV-2607-20265:start -->
### The Maskability Index: Predicting Task-Objective Alignment in Pretrained Language Models

<!-- claim:SF-2026-ARXIV-2607-20265:start -->Large-scale pretrained language models such as T5 and BERT have demonstrated strong capabilities for generating structured knowledge. However, their performance depends on how closely the prompting strategy matches the objectives used during pretraining. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20265:end -->

**为什么进入候选分母。** 摘要首要问题为“Large-scale pretrained language models such as T5 and BERT have demonstrated strong capabilities for generating structured knowledge.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We introduce the Maskability Index (MI), a quantitative metric that estimates whether a knowledge relation is better suited to masked-style prompting or prefix-style prompting in few-shot generation.

**证据证明什么。** Large-scale pretrained language models such as T5 and BERT have demonstrated strong capabilities for generating structured knowledge.

**证据没有证明什么。** It is not a full theoretical guarantee — caveats include tokenization artifacts (very frequent tokens like “to” can bias DepthRank averages) and dependence on the base pretrained model. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20265v1#S3 — 3 Methodology。Evaluation：https://arxiv.org/html/2607.20265v1#S4 — 4 Experimental Setup; https://arxiv.org/html/2607.20265v1#S5 — 5 Results。Limitations / counterevidence：https://arxiv.org/html/2607.20265v1#S7 — 7 Discussion, limitations, and next steps; https://arxiv.org/html/2607.20265v1#S9 — 9 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：It is not a full theoretical guarantee — caveats include tokenization artifacts (very frequent tokens like “to” can bias DepthRank averages) and dependence on the base pretrained model.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-PRETRAINING`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20265:end -->

<!-- review:SF-2026-ARXIV-2607-20286:start -->
### Sound Probabilistic Safety Bounds for Large Language Models

<!-- claim:SF-2026-ARXIV-2607-20286:start -->We propose a novel framework for computing rigorous bounds on the probability that a large language model (LLM) generates harmful output to a given prompt. We study a new application of the Clopper-Pearson confidence intervals to obtain probably approximately correct (PAC) bounds for this problem. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20286:end -->

**为什么进入候选分母。** 摘要首要问题为“We propose a novel framework for computing rigorous bounds on the probability that a large language model (LLM) generates harmful output to a given prompt.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We propose a novel framework for computing rigorous bounds on the probability that a large language model (LLM) generates harmful output to a given prompt.

**证据证明什么。** Our approach in particular enables the efficient computation of useful lower bounds, even in scenarios where the true harm probability is extremely small, and crucially, the obtained lower bounds are sound, i.e., formally proven to be less than the actual harmfulness probability: our experimental results demonstrate the effectiveness of our method by computing non-trivial lower bounds on state-of-the-art LLMs.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20286v1#A1.SS1 — A.1 Algorithms 1 and 2。Evaluation：https://arxiv.org/html/2607.20286v1#A1.SS2 — A.2 Experiment III; https://arxiv.org/html/2607.20286v1#A1.SS3 — A.3 Experiment IV。Limitations / counterevidence：https://arxiv.org/html/2607.20286v1#S6 — 6 Discussion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20286:end -->

<!-- review:SF-2026-ARXIV-2607-20289:start -->
### Courteous Anticipation: Improving Long-Lived Task Planning in Persistent Shared Environments

<!-- claim:SF-2026-ARXIV-2607-20289:start -->We consider a task planning scenario in which robots sharing a persistent environment are assigned tasks one at a time from a held-out sequence. Standard task planners, lacking foresight of future tasks and inconsiderate of others' constraints, solve each task in isolation, leaving terminal states that increase future cost for all, side effects that compound over lengthy task sequences. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20289:end -->

**为什么进入候选分母。** 摘要首要问题为“We consider a task planning scenario in which robots sharing a persistent environment are assigned tasks one at a time from a held-out sequence.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** Therefore, we present courteous anticipatory planning, wherein a model-based planner proposes candidate plans and selects the one that jointly minimizes immediate cost and aggregated expected future cost across all robots, estimated via independent per-robot learned estimators.

**证据证明什么。** To reduce cost over the sequence, a robot must anticipate how its actions now may impact performance on future tasks for all robots sharing the environment.

**证据没有证明什么。** Nevertheless, all these techniques are single-robot techniques; they only consider how a robot’s actions influence its future tasks but not how these actions limit or enable other robots with varying structural constraints and goals in a shared space. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20289v1#S1 — I Introduction; https://arxiv.org/html/2607.20289v1#S2 — II Related Work。Evaluation：https://arxiv.org/html/2607.20289v1#S6 — VI Experiments and Results。Limitations / counterevidence：https://arxiv.org/html/2607.20289v1#S7 — VII Limitations and Future Work; https://arxiv.org/html/2607.20289v1#S2.SS2 — II-B Anticipating Future Tasks in Persistent Environments。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Nevertheless, all these techniques are single-robot techniques; they only consider how a robot’s actions influence its future tasks but not how these actions limit or enable other robots with varying structural constraints and goals in a shared space.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-PLANNING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20289:end -->

<!-- review:SF-2026-ARXIV-2607-20293:start -->
### Evolving Cache Schedules for Fast Diffusion Policy Inference

<!-- claim:SF-2026-ARXIV-2607-20293:start -->Diffusion policies achieve strong visuomotor control by iteratively denoising action chunks, but repeated denoising makes real-time deployment computationally demanding. Cache-based methods reduce inference cost by reusing intermediate activations, but existing training-free schedules typically allocate computation uniformly across blocks, ignoring heterogeneous redundancy across blocks and leading to a suboptimal performance-efficiency trade-off. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20293:end -->

**为什么进入候选分母。** 摘要首要问题为“Diffusion policies achieve strong visuomotor control by iteratively denoising action chunks, but repeated denoising makes real-time deployment computationally demanding.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** To bridge this gap, we introduce Evolving Cache Schedules (EVO), a training-free acceleration framework that globally schedules cache refreshes via evolutionary search.

**证据证明什么。** Diffusion policies achieve strong visuomotor control by iteratively denoising action chunks, but repeated denoising makes real-time deployment computationally demanding.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20293v1#S3 — 3 Method。Evaluation：https://arxiv.org/html/2607.20293v1#S4 — 4 Experiments; https://arxiv.org/html/2607.20293v1#S4.SS1 — 4.1 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.20293v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/pillom/EVO, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20293:end -->

<!-- review:SF-2026-ARXIV-2607-20300:start -->
### Don't Trust the Label: License Laundering in AI Supply Chains

<!-- claim:SF-2026-ARXIV-2607-20300:start -->AI artifacts move through a multi-platform supply chain, spanning datasets and models on Hugging Face and applications on GitHub. While each artifact carries a license whose obligations should propagate through redistribution, no study has yet measured whether those obligations survive the chain or are stripped and replaced as artifacts move downstream. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20300:end -->

**为什么进入候选分母。** 摘要首要问题为“AI artifacts move through a multi-platform supply chain, spanning datasets and models on Hugging Face and applications on GitHub.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** While each artifact carries a license whose obligations should propagate through redistribution, no study has yet measured whether those obligations survive the chain or are stripped and replaced as artifacts move downstream.

**证据证明什么。** We find that 62.3% of chains pass through at least one artifact with no declared license (concentrated in a small set of foundational datasets), and that every obligation-bearing license category falls below 7% end-to-end survival while the Permissive category reaches 95.1%.

**证据没有证明什么。** If some of these strings represent intentional license choices that we cannot resolve, the Unknown count may be overstated. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20300v1#Sx1.SSx1 — Supply Chain Construction; https://arxiv.org/html/2607.20300v1#Sx1.SSx2 — License Categorization。Evaluation：https://arxiv.org/html/2607.20300v1#Sx2 — Unknown Laundering; https://arxiv.org/html/2607.20300v1#Sx3 — Category Laundering。Limitations / counterevidence：https://arxiv.org/html/2607.20300v1#Sx4 — Threats to Validity。

**Artifact boundary。** Exact v1 links https://github.com/SAILResearch/LicenseLaundering/, https://huggingface.co/bigcode/starcoder, https://huggingface.co/docs/huggingface_hub/en/guides/model-cards; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：If some of these strings represent intentional license choices that we cannot resolve, the Unknown count may be overstated.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20300:end -->

<!-- review:SF-2026-ARXIV-2607-20301:start -->
### The Blessing of Dimensionality: How Near-Orthogonality in High-Dimensional Spaces Explains Temporal Portability

<!-- claim:SF-2026-ARXIV-2607-20301:start -->Fine-tuning has been widely used to adapt large language models (LLMs) for domain-specific tasks. Parameter efficient fine-tuning (PEFT) methods such as low-rank adaptation (LoRA) are frequently used to reduce computational costs. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20301:end -->

**为什么进入候选分母。** 摘要首要问题为“Fine-tuning has been widely used to adapt large language models (LLMs) for domain-specific tasks.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** Parameter efficient fine-tuning (PEFT) methods such as low-rank adaptation (LoRA) are frequently used to reduce computational costs.

**证据证明什么。** Although the initial PortLLM results show that LoRA patches exhibit short-term temporal portability, the long-term performance of PortLLM across several updates of continual pretraining remains underexplored.

**证据没有证明什么。** In Section 4.3 that leverages the relationships between pretraining optimization steps to characterize RQ3, our results depend on Assumption 1 that the pretraining and fine-tuning gradients are approximately orthogonal to bound their inner product. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20301v1#S1 — 1 Introduction; https://arxiv.org/html/2607.20301v1#S2 — 2 Related Work。Evaluation：https://arxiv.org/html/2607.20301v1#A6 — Appendix F Additional Experimental Results; https://arxiv.org/html/2607.20301v1#S3.SS2 — 3.2 Experimental Results。Limitations / counterevidence：https://arxiv.org/html/2607.20301v1#S5 — 5 Discussion; https://arxiv.org/html/2607.20301v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：In Section 4.3 that leverages the relationships between pretraining optimization steps to characterize RQ3, our results depend on Assumption 1 that the pretraining and fine-tuning gradients are approximately orthogonal to bound their inner product.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-LORA`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20301:end -->

<!-- review:SF-2026-ARXIV-2607-20327:start -->
### PyroDash: Cost-Efficient Token-Level Small-Large Language Model Collaborative Inference

<!-- claim:SF-2026-ARXIV-2607-20327:start -->Large language models (LLMs) provide strong reasoning capabilities but are expensive to serve at scale, whereas small language models (SLMs) are cheaper but less reliable on difficult problems. We introduce PyroDash, a cost-aware framework for token-level SLM-LLM collaborative inference. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20327:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language models (LLMs) provide strong reasoning capabilities but are expensive to serve at scale, whereas small language models (SLMs) are cheaper but less reliable on difficult problems.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** We introduce PyroDash, a cost-aware framework for token-level SLM-LLM collaborative inference.

**证据证明什么。** These results show that learned token-level handoffs can reduce LLM use while preserving strong reasoning performance.

**证据没有证明什么。** 6 Limitations and Future Work The current evaluation reports accuracy and LLM usage but does not examine the rationality of individual offloading decisions. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20327v1#S3 — 3 Method; https://arxiv.org/html/2607.20327v1#S3.SS2 — 3.2 The Collaborative Inference Architecture of PyroDash。Evaluation：https://arxiv.org/html/2607.20327v1#S4.SS4 — 4.4 Ablation and Analysis; https://arxiv.org/html/2607.20327v1#S4 — 4 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.20327v1#S6 — 6 Limitations and Future Work; https://arxiv.org/html/2607.20327v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://huggingface.co/datasets/HuggingFaceH4/aime_2024, https://huggingface.co/datasets/yentinglin/aime_2025, https://huggingface.co/datasets/pyromind/easyhard-24k; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：6 Limitations and Future Work The current evaluation reports accuracy and LLM usage but does not examine the rationality of individual offloading decisions.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-SCHEDULING`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20327:end -->

<!-- review:SF-2026-ARXIV-2607-20345:start -->
### Closing the Lab-to-Store Gap: A Data-Efficient Post-Training and Experience-Driven Learning VLA Framework for Retail Humanoids

<!-- claim:SF-2026-ARXIV-2607-20345:start -->Closing the gap between benchmark performance and reliable real-world operation remains a central challenge for Vision-Language-Action (VLA) humanoid robots, which must handle execution errors, distribution shifts, and environmental variability. This paper presents DEED (Data-Efficient Post-Training and Experience-Driven Learning), a systems-level approach evaluated on a supermarket chip-restocking task using a Unitree G1-Edu humanoid robot and the GR00T N1.6 foundation model. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20345:end -->

**为什么进入候选分母。** 摘要首要问题为“Closing the gap between benchmark performance and reliable real-world operation remains a central challenge for Vision-Language-Action (VLA) humanoid robots, which must handle execution errors, distribution shifts, and environmental variability.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** This paper presents DEED (Data-Efficient Post-Training and Experience-Driven Learning), a systems-level approach evaluated on a supermarket chip-restocking task using a Unitree G1-Edu humanoid robot and the GR00T N1.6 foundation model.

**证据证明什么。** Our results suggest that bridging the lab-to-store gap is primarily a systems integration challenge rather than an architectural one: careful data design and targeted post-training can transform a policy that fails under naive fine-tuning into a competent real-world system using only a single GPU.

**证据没有证明什么。** These conclusions are limited by a single task, one platform, a binary success metric, few evaluation episodes, and two refinement iterations. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20345v1#S2 — II DEED Framework。Evaluation：https://arxiv.org/html/2607.20345v1#S2.SS3 — II-C In/Out-Distribution Analysis Tool; https://arxiv.org/html/2607.20345v1#S3 — III Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.20345v1#S3.SS3 — III-C Discussion; https://arxiv.org/html/2607.20345v1#S4 — IV Conclusions。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：These conclusions are limited by a single task, one platform, a binary success metric, few evaluation episodes, and two refinement iterations.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20345:end -->

<!-- review:SF-2026-ARXIV-2607-20351:start -->
### Test-Time Training for Modality Order Consistency in Vision-Language Models

<!-- claim:SF-2026-ARXIV-2607-20351:start -->We find that vision-language models are sensitive to a specific semantically irrelevant change: the order in which the image and question are presented. Across three models and three benchmarks, image first prompting consistently outperforms question-first prompting, revealing a repeatable modality order failure. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20351:end -->

**为什么进入候选分母。** 摘要首要问题为“We find that vision-language models are sensitive to a specific semantically irrelevant change: the order in which the image and question are presented.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We use this gap to design an order-consistent test-time training method.

**证据证明什么。** Together, our results identify modality-order sensitivity as a circuit-level failure in VLMs and demonstrate that simple, asymmetric test-time adaptation can effectively mitigate it and even improve performance over the baseline.

**证据没有证明什么。** 6 Discussion, Limitations, and Future Work The main implication of our findings is that prompt formatting can induce systematic computational differences, even when the task content is unchanged. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20351v1#A5.SS2 — E.2 Test-Time Training on the Thinking Model; https://arxiv.org/html/2607.20351v1#S3.SS1 — 3.1 Modality-Ordering Failure in Vision-Language Models。Evaluation：https://arxiv.org/html/2607.20351v1#A2 — Appendix B CHAIR Hallucination Evaluation; https://arxiv.org/html/2607.20351v1#A5 — Appendix E Thinking-Mode Ablations。Limitations / counterevidence：https://arxiv.org/html/2607.20351v1#S6 — 6 Discussion, Limitations, and Future Work; https://arxiv.org/html/2607.20351v1#S3.SS1 — 3.1 Modality-Ordering Failure in Vision-Language Models。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：6 Discussion, Limitations, and Future Work The main implication of our findings is that prompt formatting can induce systematic computational differences, even when the task content is unchanged.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-REPRESENTATION`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20351:end -->

<!-- review:SF-2026-ARXIV-2607-20357:start -->
### Look Less, Think Faster: Joint Token-Compute Adaptation for Multimodal LLMs

<!-- claim:SF-2026-ARXIV-2607-20357:start -->Multimodal Large Language Models (MLLMs) have recently demonstrated strong performance across vision-language tasks. However, their high inference cost, arising from both the large number of input visual tokens and the heavy computation of the large language model (LLM), remains a key barrier to practical deployment. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20357:end -->

**为什么进入候选分母。** 摘要首要问题为“Multimodal Large Language Models (MLLMs) have recently demonstrated strong performance across vision-language tasks.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** To bridge the gap, we propose SmartVL, a unified adaptive inference framework that jointly controls vision token number and model compute capability in response to varying input contents and compute budgets.

**证据证明什么。** Experiments across multiple MLLM benchmarks demonstrate that, with joint scheduling, SmartVL consistently outperforms prior adaptive methods and achieves superior accuracy-efficiency Pareto frontiers.

**证据没有证明什么。** AdaLLaVA-PruMerge achieves comparable accuracy in the mid-range but is limited to a few manually configured token-retention ratios (we test 25% PruMerge+ token retention with AdaLLaVA layers at 65%, 80%, and 100%) and cannot adapt continuously. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20357v1#S1 — 1 Introduction; https://arxiv.org/html/2607.20357v1#S2 — 2 Related Work。Evaluation：https://arxiv.org/html/2607.20357v1#S4 — 4 Experiments and Results; https://arxiv.org/html/2607.20357v1#S4.SS1 — 4.1 Experiment Setup。Limitations / counterevidence：https://arxiv.org/html/2607.20357v1#S5 — 5 Conclusion and Discussion; https://arxiv.org/html/2607.20357v1#S4.SS2 — 4.2 Main Results and Discussion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：AdaLLaVA-PruMerge achieves comparable accuracy in the mid-range but is limited to a few manually configured token-retention ratios (we test 25% PruMerge+ token retention with AdaLLaVA layers at 65%, 80%, and 100%) and cannot adapt continuously.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-REPRESENTATION`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20357:end -->

<!-- review:SF-2026-ARXIV-2607-20368:start -->
### Self Gradient Forcing: Native Long Video Extrapolation

<!-- claim:SF-2026-ARXIV-2607-20368:start -->Recent autoregressive video diffusion methods are increasingly built upon Self Forcing, where the student is trained on histories produced by its own rollout rather than ground-truth video contexts. This reduces exposure bias, but the historical key-value cache is still used by future frames only as frozen rollout state. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20368:end -->

**为什么进入候选分母。** 摘要首要问题为“Recent autoregressive video diffusion methods are increasingly built upon Self Forcing, where the student is trained on histories produced by its own rollout rather than ground-truth video contexts.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We propose Self Gradient Forcing (SGF), a two-pass training strategy that restores this missing supervision signal without backpropagating through the full serial rollout.

**证据证明什么。** This reduces exposure bias, but the historical key-value cache is still used by future frames only as frozen rollout state.

**证据没有证明什么。** It supervises how recorded self-generated latents are written into future-readable memory, but it does not update the sampled latents themselves through future losses, nor does it optimize the sequence of denoising decisions that produced them. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20368v1#S3 — 3 Method。Evaluation：https://arxiv.org/html/2607.20368v1#A1 — Appendix A Additional Experimental Details; https://arxiv.org/html/2607.20368v1#A7 — Appendix G Additional Qualitative Results。Limitations / counterevidence：https://arxiv.org/html/2607.20368v1#A6 — Appendix F Limitations; https://arxiv.org/html/2607.20368v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：It supervises how recorded self-generated latents are written into future-readable memory, but it does not update the sampled latents themselves through future losses, nor does it optimize the sequence of denoising decisions that produced them.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-GENERATIVE-PARADIGMS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20368:end -->

<!-- review:SF-2026-ARXIV-2607-20372:start -->
### Notes to Self: Can LLMs Benefit from Experiential Abstractions?

<!-- claim:SF-2026-ARXIV-2607-20372:start -->Humans distill experience into reusable abstractions, e.g., strategies and cautionary reminders, and apply them to gradually solve problems more effectively. We study whether Large Language Models (LLMs) can similarly benefit from such experiential abstractions. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20372:end -->

**为什么进入候选分母。** 摘要首要问题为“Humans distill experience into reusable abstractions, e.g., strategies and cautionary reminders, and apply them to gradually solve problems more effectively.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** Self-extracted abstractions match teacher-extracted ones, and our abstraction usage framework can transfer to other datasets and models.

**证据证明什么。** Experiential abstractions improve LLM performance on mathematical and logical reasoning benchmarks.

**证据没有证明什么。** Limitations Our results further depend on several fixed design choices: a particular teacher model, sentence encoder, retrieval cutoff , and deduplication threshold, for which we do not provide a sensitivity analysis. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20372v1#S3 — 3 Methods; https://arxiv.org/html/2607.20372v1#A4 — Appendix D Implementation details。Evaluation：https://arxiv.org/html/2607.20372v1#A2 — Appendix B Quantitative analyses on Qwen-2.5-1.5B-Instruct results; https://arxiv.org/html/2607.20372v1#S4 — 4 Results。Limitations / counterevidence：https://arxiv.org/html/2607.20372v1#S5 — 5 Conclusion; https://arxiv.org/html/2607.20372v1#Sx1 — Limitations。

**Artifact boundary。** Exact v1 links https://github.com/ChangLiu-DrPatient/Notes-to-self, https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro/blob/main/DeepSeek_V4.pdf, https://huggingface.co/datasets/HuggingFaceH4/MATH-500/viewer/default/test?row=122; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Limitations Our results further depend on several fixed design choices: a particular teacher model, sentence encoder, retrieval cutoff , and deduplication threshold, for which we do not provide a sensitivity analysis.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20372:end -->

<!-- review:SF-2026-ARXIV-2607-20379:start -->
### Train the Model, Not the Reader: Decodability Supervision for Verifiable Activation Explanations

<!-- claim:SF-2026-ARXIV-2607-20379:start -->Natural-language autoencoders score explanations of hidden activations by reconstruction. An explanation is deemed faithful if the activation can be regenerated from it. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20379:end -->

**为什么进入候选分母。** 摘要首要问题为“Natural-language autoencoders score explanations of hidden activations by reconstruction.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** An explanation is deemed faithful if the activation can be regenerated from it.

**证据证明什么。** We show the test is passed in two ways, neither faithful.

**证据没有证明什么。** Second, RECAP must be co-trained in and cannot be retrofitted onto a frozen model, and it depends on choosing a good target: a poorly chosen one can report success while decoding nothing. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20379v1#A5 — Appendix E Released-System Audit Details; https://arxiv.org/html/2607.20379v1#S5.SS1 — 5.1 Method。Evaluation：https://arxiv.org/html/2607.20379v1#A2 — Appendix B Safety Experiment 1: The Discrepancy Detector; https://arxiv.org/html/2607.20379v1#A3 — Appendix C Safety Experiment 2: Legibility Persistence Under Head-Free Fine-Tuning。Limitations / counterevidence：https://arxiv.org/html/2607.20379v1#S8 — 8 Discussion and Limitations; https://arxiv.org/html/2607.20379v1#S9 — 9 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Second, RECAP must be co-trained in and cannot be retrofitted onto a frozen model, and it depends on choosing a good target: a poorly chosen one can report success while decoding nothing.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20379:end -->

<!-- review:SF-2026-ARXIV-2607-20389:start -->
### PercepCap: Video Captioner with Structured Spatio-Temporal Perception

<!-- claim:SF-2026-ARXIV-2607-20389:start -->Video captioning requires fine-grained spatio-temporal understanding of videos, including spatial perception of where objects are located and temporal perception of when events occur. Existing MLLMs usually generate captions directly from video inputs without exposing the perceptual evidence behind descriptions. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20389:end -->

**为什么进入候选分母。** 摘要首要问题为“Video captioning requires fine-grained spatio-temporal understanding of videos, including spatial perception of where objects are located and temporal perception of when events occur.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** To address these issues, we present PercepCap, a perception-aware video captioning framework that makes perceptual evidence explicit before producing the final caption.

**证据证明什么。** Across direct caption and caption-to-QA evaluation, PercepCap consistently improves upon the Qwen3-VL baseline and demonstrates leading caption quality.

**证据没有证明什么。** Third, the reward pipeline relies on parsing structured outputs and computing perception-level matching scores, making training more involved than caption-only optimization. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20389v1#S2.SS1 — 2.1 Video Captioning and Multi-modal Large Language Models; https://arxiv.org/html/2607.20389v1#S5.SS1 — 5.1 Implementation Details。Evaluation：https://arxiv.org/html/2607.20389v1#S5 — 5 Results and Analysis; https://arxiv.org/html/2607.20389v1#S5.SS2 — 5.2 Benchmarks and Evaluation Metrics。Limitations / counterevidence：https://arxiv.org/html/2607.20389v1#S5.SS5 — 5.5 Limitations; https://arxiv.org/html/2607.20389v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：Third, the reward pipeline relies on parsing structured outputs and computing perception-level matching scores, making training more involved than caption-only optimization.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-REPRESENTATION`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20389:end -->

<!-- review:SF-2026-ARXIV-2607-20402:start -->
### SoftReason: A Fully Differentiable Neuro-Soft-Symbolic Deductive Reasoning Architecture over High-Dimensional Perceptual Data

<!-- claim:SF-2026-ARXIV-2607-20402:start -->In many reasoning problems, the premises are not observed as discrete symbols, but must be inferred from high-dimensional inputs. Further, the predicate vocabulary, argument structure, and trusted evidence are supplied by a Knowledge Graph (KG), or rule definitions. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20402:end -->

**为什么进入候选分母。** 摘要首要问题为“In many reasoning problems, the premises are not observed as discrete symbols, but must be inferred from high-dimensional inputs.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We present a neuro-soft-symbolic architecture for differentiable deductive reasoning over latent perceptual facts and knowledge-provided predicates.

**证据证明什么。** We instantiate the framework on Knowledge-aware Visual Question Answering (KVQA), and demonstrates how SoftReason supports end-to-end perceptual grounding, KG evidence injection, and differentiable deductive closure in one trainable architecture.

**证据没有证明什么。** Horn-chain reasoning is recovered as a limiting case. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20402v1#S3 — 3 Technical Approach; https://arxiv.org/html/2607.20402v1#S3.SS2 — 3.2 SoftReason Architecture。Evaluation：https://arxiv.org/html/2607.20402v1#S4 — 4 Experimental Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.20402v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Horn-chain reasoning is recovered as a limiting case.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`WORLDVIEW-REPRESENTATION`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20402:end -->

## 4. Benchmark Contracts

None。数值只在各 Source Review 的 exact-v1 evaluation contract 内使用，不形成跨配置 benchmark claim。

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-19349 | score_7_9 | selected | DA-20260723-01 | — | V2=9/9；相对其他 eligible family 提供更直接、可迁移且不重复的 state/control/evaluation 机制。 | analysis:DA-20260723-01 |
| SF-2026-ARXIV-2607-19351 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-19351 |
| SF-2026-ARXIV-2607-19353 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-19353 |
| SF-2026-ARXIV-2607-19356 | score_7_9 | selected | DA-20260723-02 | — | V2=9/9；相对其他 eligible family 提供更直接、可迁移且不重复的 state/control/evaluation 机制。 | analysis:DA-20260723-02 |
| SF-2026-ARXIV-2607-19358 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-19358 |
| SF-2026-ARXIV-2607-19359 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-19359 |
| SF-2026-ARXIV-2607-19361 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-19361 |
| SF-2026-ARXIV-2607-19367 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-19367 |
| SF-2026-ARXIV-2607-19368 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-19368 |
| SF-2026-ARXIV-2607-19396 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-19396 |
| SF-2026-ARXIV-2607-19408 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-19408 |
| SF-2026-ARXIV-2607-19430 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-19430 |
| SF-2026-ARXIV-2607-19431 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-19431 |
| SF-2026-ARXIV-2607-19432 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-19432 |
| SF-2026-ARXIV-2607-19433 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-19433 |
| SF-2026-ARXIV-2607-19438 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-19438 |
| SF-2026-ARXIV-2607-19490 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-19490 |
| SF-2026-ARXIV-2607-19515 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-19515 |
| SF-2026-ARXIV-2607-19539 | score_7_9 | selected | DA-20260723-03 | — | V2=9/9；相对其他 eligible family 提供更直接、可迁移且不重复的 state/control/evaluation 机制。 | analysis:DA-20260723-03 |
| SF-2026-ARXIV-2607-19547 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-19547 |
| SF-2026-ARXIV-2607-19595 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-19595 |
| SF-2026-ARXIV-2607-19623 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-19623 |
| SF-2026-ARXIV-2607-19638 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-19638 |
| SF-2026-ARXIV-2607-19686 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-19686 |
| SF-2026-ARXIV-2607-19704 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-19704 |
| SF-2026-ARXIV-2607-19712 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-19712 |
| SF-2026-ARXIV-2607-19719 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-19719 |
| SF-2026-ARXIV-2607-19749 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-19749 |
| SF-2026-ARXIV-2607-19771 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-19771 |
| SF-2026-ARXIV-2607-19827 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-19827 |
| SF-2026-ARXIV-2607-19829 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-19829 |
| SF-2026-ARXIV-2607-19837 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-19837 |
| SF-2026-ARXIV-2607-19857 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-19857 |
| SF-2026-ARXIV-2607-19865 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-19865 |
| SF-2026-ARXIV-2607-19876 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-19876 |
| SF-2026-ARXIV-2607-19913 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-19913 |
| SF-2026-ARXIV-2607-19922 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-19922 |
| SF-2026-ARXIV-2607-19932 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-19932 |
| SF-2026-ARXIV-2607-19957 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-19957 |
| SF-2026-ARXIV-2607-20064 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-20064 |
| SF-2026-ARXIV-2607-20083 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-20083 |
| SF-2026-ARXIV-2607-20090 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-20090 |
| SF-2026-ARXIV-2607-20121 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-20121 |
| SF-2026-ARXIV-2607-20125 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-20125 |
| SF-2026-ARXIV-2607-20129 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-20129 |
| SF-2026-ARXIV-2607-20145 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-20145 |
| SF-2026-ARXIV-2607-20214 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-20214 |
| SF-2026-ARXIV-2607-20220 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-20220 |
| SF-2026-ARXIV-2607-20286 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-20286 |
| SF-2026-ARXIV-2607-20293 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-20293 |
| SF-2026-ARXIV-2607-20300 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-20300 |
| SF-2026-ARXIV-2607-20327 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-20327 |
| SF-2026-ARXIV-2607-20345 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-20345 |
| SF-2026-ARXIV-2607-20357 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-20357 |
| SF-2026-ARXIV-2607-20368 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-20368 |
| SF-2026-ARXIV-2607-20379 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-20379 |

### Selection Decisions

<!-- analysis-decision:SF-2026-ARXIV-2607-19351:start -->
`SF-2026-ARXIV-2607-19351` 的 exact-v1 Deep Review 已保留。其机制为：We propose OpenEvoShield, a co-evolutionary continual defense framework for LLM-MAS. 为避免挤压 `AGENT-MULTI-AGENT` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-19351:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-19353:start -->
`SF-2026-ARXIV-2607-19353` 的 exact-v1 Deep Review 已保留。其机制为：However, the performance cost of enabling confidential execution for GPU-accelerated large language model serving remains workload dependent and operationally important. 为避免挤压 `PLATFORM-SECURITY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-19353:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-19358:start -->
`SF-2026-ARXIV-2607-19358` 的 exact-v1 Deep Review 已保留。其机制为：To address this, we propose LISA (Linear-Indexed Sparse Attention), a plug-and-play attention replacement module that requires no pretraining from scratch. 为避免挤压 `MODEL-LONG-CONTEXT` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-19358:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-19359:start -->
`SF-2026-ARXIV-2607-19359` 的 exact-v1 Deep Review 已保留。其机制为：First, we introduce MemHop, a multi-hop memory benchmark of 1,000 questions at hop depths 1-5 across 10 social-network scenarios, with per-hop evidence annotations. 为避免挤压 `AGENT-MEMORY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-19359:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-19361:start -->
`SF-2026-ARXIV-2607-19361` 的 exact-v1 Deep Review 已保留。其机制为：We propose a session-layer CRA Framework that tracks three trajectory signals: semantic drift from a session anchor, a sensitivity-weighted information accumulation graph over extracted entities, and a compliance-gradient signal capturing increasing willingness to comply. 为避免挤压 `PLATFORM-SECURITY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-19361:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-19367:start -->
`SF-2026-ARXIV-2607-19367` 的 exact-v1 Deep Review 已保留。其机制为：Our results show current LLM confidence estimates cannot be interpreted as coherent probabilities; our framework provides the tools to measure and close this gap. 为避免挤压 `PLATFORM-EVALUATION-SYSTEM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-19367:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-19368:start -->
`SF-2026-ARXIV-2607-19368` 的 exact-v1 Deep Review 已保留。其机制为：We propose Spectral-LSH, a training-free prompt compression method that operates before the prompt enters the language model. 为避免挤压 `INFER-PREFILL` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-19368:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-19396:start -->
`SF-2026-ARXIV-2607-19396` 的 exact-v1 Deep Review 已保留。其机制为：Document-based LLM systems often flatten a PDF before guardrails inspect it. 为避免挤压 `PLATFORM-SECURITY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-19396:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-19408:start -->
`SF-2026-ARXIV-2607-19408` 的 exact-v1 Deep Review 已保留。其机制为：Yet its population-size conclusions conflict sharply: fine-tuning with cross-entropy (CE) reward succeeds with $N=1$, while binary-reward training often needs $N \approx 30$. 为避免挤压 `TRAIN-PRETRAINING` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-19408:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-19430:start -->
`SF-2026-ARXIV-2607-19430` 的 exact-v1 Deep Review 已保留。其机制为：We present ChannelGuard, a training-free defense-in-depth framework placing information-bottleneck gates on every inter-agent channel; each scores channel text against an adversarial phrase bank by embedding similarity and deterministically passes, compresses, or blocks it, adding no LLM call, while an attribution method records which layer stopped each attack. 为避免挤压 `AGENT-MULTI-AGENT` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-19430:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-19431:start -->
`SF-2026-ARXIV-2607-19431` 的 exact-v1 Deep Review 已保留。其机制为：We present BRIM, a hardware - software co-designed dual-sided bit-serial sparse accelerator that directly targets this bottleneck. 为避免挤压 `INFER-TENSORRT-LLM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-19431:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-19432:start -->
`SF-2026-ARXIV-2607-19432` 的 exact-v1 Deep Review 已保留。其机制为：This paper presents ChainWatch, a sequential detection framework for identifying multi-step attacks in MCP-based AI agent systems. 为避免挤压 `AGENT-MCP` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-19432:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-19433:start -->
`SF-2026-ARXIV-2607-19433` 的 exact-v1 Deep Review 已保留。其机制为：The Chronos Vulnerability represents the threat of memory-based attacks, including the Memory Injection Attack (MINJA) and the sleeper agent, in which the internal belief system of the autonomous agent is compromised, effectively decoupling the attack vector from the final catastrophic event. 为避免挤压 `AGENT-MEMORY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-19433:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-19438:start -->
`SF-2026-ARXIV-2607-19438` 的 exact-v1 Deep Review 已保留。其机制为：Building on BaseRT's framework-free design, we add a family of hand-written Metal~4 tensor-core kernels (including dense and mixture-of-experts GEMM and flash-attention prefill kernels) that route the compute-bound matrix multiplications of inference through the M5 Neural Accelerators while leaving the memory-bound decode path on our existing specialised kernels. 为避免挤压 `INFER-TENSORRT-LLM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-19438:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-19490:start -->
`SF-2026-ARXIV-2607-19490` 的 exact-v1 Deep Review 已保留。其机制为：In this paper, we propose a method that checks the output integrity by measuring the variation in the activations that each node passes to the next. 为避免挤压 `PLATFORM-SECURITY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-19490:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-19515:start -->
`SF-2026-ARXIV-2607-19515` 的 exact-v1 Deep Review 已保留。其机制为：Continuous surveillance video creates a growing storage, transmission, and inference burden for enterprise video analytics systems. 为避免挤压 `MULTIMODAL-REPRESENTATION` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-19515:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-19547:start -->
`SF-2026-ARXIV-2607-19547` 的 exact-v1 Deep Review 已保留。其机制为：The method first re-bases stored post-rotary keys onto a global three-axis multimodal RoPE coordinate system that preserves time, height, and width structure. 为避免挤压 `MULTIMODAL-WORLD-MODELS` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-19547:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-19595:start -->
`SF-2026-ARXIV-2607-19595` 的 exact-v1 Deep Review 已保留。其机制为：Existing secure-by-design approaches mitigate this risk by separating untrusted observations from privileged execution and careful control of information flow, but often degrade utility and require extensive task-specific engineering. 为避免挤压 `AGENT-PLATFORM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-19595:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-19623:start -->
`SF-2026-ARXIV-2607-19623` 的 exact-v1 Deep Review 已保留。其机制为：Our central empirical finding is a sharp bit-sensitivity transition: flipping any of the least-significant fraction bits up to a data-type-specific threshold, Xsafe, degrades task metrics by less than 1% under deterministic single-bit stress tests. 为避免挤压 `INFER-GPU-MEMORY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-19623:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-19638:start -->
`SF-2026-ARXIV-2607-19638` 的 exact-v1 Deep Review 已保留。其机制为：Formalizing the fleet as a generalized Kuramoto system, we obtain three operator-facing statements. 为避免挤压 `PLATFORM-GPU-SCHEDULER` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-19638:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-19686:start -->
`SF-2026-ARXIV-2607-19686` 的 exact-v1 Deep Review 已保留。其机制为：In this work, we propose a multi-mask diffusion model (MultiMDM) that preserves the masking structure towards few-step generation. 为避免挤压 `MULTIMODAL-GENERATIVE-PARADIGMS` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-19686:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-19704:start -->
`SF-2026-ARXIV-2607-19704` 的 exact-v1 Deep Review 已保留。其机制为：Deployed on 38 million customers for a persona-based recommender, the clustering method cut downstream cost and latency by 50-fold while preserving personalization and unblocked the production launch. 为避免挤压 `INFER-SCHEDULING` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-19704:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-19712:start -->
`SF-2026-ARXIV-2607-19712` 的 exact-v1 Deep Review 已保留。其机制为：Slow scoring bottlenecks the entire loop, since no update runs until every rollout gets a score. 为避免挤压 `TRAIN-RLHF` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-19712:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-19719:start -->
`SF-2026-ARXIV-2607-19719` 的 exact-v1 Deep Review 已保留。其机制为：We propose Koopman Dreamer, a Dreamer-style world model with a spectrally constrained deterministic latent dynamics core. 为避免挤压 `MULTIMODAL-WORLD-MODELS` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-19719:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-19749:start -->
`SF-2026-ARXIV-2607-19749` 的 exact-v1 Deep Review 已保留。其机制为：We ask a question the continual-RL literature has assumed an answer to but never measured: which component forgets? 为避免挤压 `MULTIMODAL-WORLD-MODELS` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-19749:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-19771:start -->
`SF-2026-ARXIV-2607-19771` 的 exact-v1 Deep Review 已保留。其机制为：We then study three systems trained with Muon: a nanoGPT feed-forward projection, a 64-expert mixture-of-experts router, and the query/key projections of a bf16 FlashAttention block. 为避免挤压 `TRAIN-PRETRAINING` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-19771:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-19827:start -->
`SF-2026-ARXIV-2607-19827` 的 exact-v1 Deep Review 已保留。其机制为：We propose a conceptual robotic architecture that integrates wearable sensors, smart medical devices, and assistive robotic components into a unified framework for real-time safety monitoring. 为避免挤压 `MULTIMODAL-EMBODIED-VLA` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-19827:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-19829:start -->
`SF-2026-ARXIV-2607-19829` 的 exact-v1 Deep Review 已保留。其机制为：To address this challenge, we propose DARWIN, an evolutionary attack-defense framework that formulates jailbreaking as an open-ended evolution process and continuously updates guardrails through an evolving attack-defense loop. 为避免挤压 `PLATFORM-SECURITY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-19829:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-19837:start -->
`SF-2026-ARXIV-2607-19837` 的 exact-v1 Deep Review 已保留。其机制为：We instantiate these insights in Know Your Agent (KYA), a framework that automates black-box, reconnaissance-driven pentesting by probing agents, building target profiles, and using those profiles to craft stronger attacks. 为避免挤压 `AGENT-PLATFORM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-19837:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-19857:start -->
`SF-2026-ARXIV-2607-19857` 的 exact-v1 Deep Review 已保留。其机制为：From the method perspective, we propose \textbf{SkyAnchor}, an MLLM with two designs to the above challenges: a Semantics-Aware Token Router that preserves small-target under a reduced visual-token budget, and a Hierarchical Memory Bank that keeps the target consistently understood on streams. 为避免挤压 `AGENT-MEMORY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-19857:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-19865:start -->
`SF-2026-ARXIV-2607-19865` 的 exact-v1 Deep Review 已保留。其机制为：In this paper, we introduce DocOps, a deterministically verifiable evaluation framework underpinned by a hierarchical taxonomy that deconstructs document operations inspired by real-world practices into atomic dimensions and escalating workflow complexities. 为避免挤压 `AGENT-WORKFLOW` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-19865:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-19876:start -->
`SF-2026-ARXIV-2607-19876` 的 exact-v1 Deep Review 已保留。其机制为：To reduce this ambiguity, we present KineBench, an IDM-free closed-loop benchmark for EWMs, built upon an explicit kinematic grounding pipeline. 为避免挤压 `MULTIMODAL-WORLD-MODELS` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-19876:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-19913:start -->
`SF-2026-ARXIV-2607-19913` 的 exact-v1 Deep Review 已保留。其机制为：We propose Janus, a foresight-oriented framework for long-horizon agent safety that trains guards to anticipate delayed risks from partial trajectories. 为避免挤压 `AGENT-PLATFORM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-19913:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-19922:start -->
`SF-2026-ARXIV-2607-19922` 的 exact-v1 Deep Review 已保留。其机制为：In this paper, we introduce DGNA, a methodology designed to unveil the NUMA architecture of the GPU memory hierarchy through microbenchmarking and data analysis. 为避免挤压 `INFER-GPU-MEMORY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-19922:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-19932:start -->
`SF-2026-ARXIV-2607-19932` 的 exact-v1 Deep Review 已保留。其机制为：To address this challenge, we propose Efficient Chain-of-Modality Reasoning (ECoM Reasoning), the first framework to introduce compressed reasoning into SLMs. 为避免挤压 `MULTIMODAL-REPRESENTATION` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-19932:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-19957:start -->
`SF-2026-ARXIV-2607-19957` 的 exact-v1 Deep Review 已保留。其机制为：We introduce HIJACKKV, the first attack framework that systematically exploits this vulnerability, demonstrating its severity and practicality. 为避免挤压 `INFER-KV-CACHE` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-19957:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-20064:start -->
`SF-2026-ARXIV-2607-20064` 的 exact-v1 Deep Review 已保留。其机制为：We propose PRO-LONG, a minimal context management framework built around programmatic memory for LLM agents in long-horizon, exploratory settings. 为避免挤压 `AGENT-MEMORY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-20064:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-20083:start -->
`SF-2026-ARXIV-2607-20083` 的 exact-v1 Deep Review 已保留。其机制为：Motivated by this view, we propose DynamicRubric, a response-set-conditioned evaluator--policy co-evolution framework that generates weighted binary rubric items for each candidate set and aggregates the resulting judgments into response-level scores. 为避免挤压 `PLATFORM-EVALUATION-SYSTEM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-20083:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-20090:start -->
`SF-2026-ARXIV-2607-20090` 的 exact-v1 Deep Review 已保留。其机制为：We introduce SelectBench, a controlled benchmark and training set for selective evidence adoption, and post-train Qwen3.5-4B directly with DAPO using either deterministic rule rewards or a frozen semantic judge. 为避免挤压 `AGENT-RAG` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-20090:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-20121:start -->
`SF-2026-ARXIV-2607-20121` 的 exact-v1 Deep Review 已保留。其机制为：Context-dependent and system-level risks are especially difficult for current agent systems to avoid. 为避免挤压 `AGENT-TOOL-CALLING` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-20121:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-20125:start -->
`SF-2026-ARXIV-2607-20125` 的 exact-v1 Deep Review 已保留。其机制为：We propose HeadCast, a training-free, plug-and-play acceleration framework built on the observation that a pre-trained AR model's attention heads exhibit stable, heterogeneous behaviors. 为避免挤压 `MULTIMODAL-GENERATIVE-PARADIGMS` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-20125:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-20129:start -->
`SF-2026-ARXIV-2607-20129` 的 exact-v1 Deep Review 已保留。其机制为：On MATH-500, a paired three-seed evaluation over 1,500 generations per method raises exact-normalized accuracy from 54.73% for vanilla decoding to 56.40% (+1.67 percentage points; problem-clustered bootstrap 95% CI [+0.47, +2.80]), while a prospectively profiled random-intervention control reaches 54.60%. 为避免挤压 `INFER-DECODE` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-20129:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-20145:start -->
`SF-2026-ARXIV-2607-20145` 的 exact-v1 Deep Review 已保留。其机制为：We refer to the integrated framework as SLAI T-Rex. 为避免挤压 `TRAIN-DISTRIBUTED-TRAINING` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-20145:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-20214:start -->
`SF-2026-ARXIV-2607-20214` 的 exact-v1 Deep Review 已保留。其机制为：We propose \emph{ELSAA}, an efficient low-rank and sparse approximation of attention. 为避免挤压 `MODEL-SELF-ATTENTION` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-20214:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-20220:start -->
`SF-2026-ARXIV-2607-20220` 的 exact-v1 Deep Review 已保留。其机制为：We show that efficient offline-optimized routing enables efficient MoE training and inference on direct-connect topologies without the need for MoE traffic matrix or dynamic topology reconfiguration. 为避免挤压 `MODEL-MOE` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-20220:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-20286:start -->
`SF-2026-ARXIV-2607-20286` 的 exact-v1 Deep Review 已保留。其机制为：We propose a novel framework for computing rigorous bounds on the probability that a large language model (LLM) generates harmful output to a given prompt. 为避免挤压 `PLATFORM-SECURITY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-20286:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-20293:start -->
`SF-2026-ARXIV-2607-20293` 的 exact-v1 Deep Review 已保留。其机制为：To bridge this gap, we introduce Evolving Cache Schedules (EVO), a training-free acceleration framework that globally schedules cache refreshes via evolutionary search. 为避免挤压 `MULTIMODAL-EMBODIED-VLA` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-20293:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-20300:start -->
`SF-2026-ARXIV-2607-20300` 的 exact-v1 Deep Review 已保留。其机制为：While each artifact carries a license whose obligations should propagate through redistribution, no study has yet measured whether those obligations survive the chain or are stripped and replaced as artifacts move downstream. 为避免挤压 `PLATFORM-SECURITY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-20300:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-20327:start -->
`SF-2026-ARXIV-2607-20327` 的 exact-v1 Deep Review 已保留。其机制为：We introduce PyroDash, a cost-aware framework for token-level SLM-LLM collaborative inference. 为避免挤压 `INFER-SCHEDULING` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-20327:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-20345:start -->
`SF-2026-ARXIV-2607-20345` 的 exact-v1 Deep Review 已保留。其机制为：This paper presents DEED (Data-Efficient Post-Training and Experience-Driven Learning), a systems-level approach evaluated on a supermarket chip-restocking task using a Unitree G1-Edu humanoid robot and the GR00T N1.6 foundation model. 为避免挤压 `MULTIMODAL-EMBODIED-VLA` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-20345:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-20357:start -->
`SF-2026-ARXIV-2607-20357` 的 exact-v1 Deep Review 已保留。其机制为：To bridge the gap, we propose SmartVL, a unified adaptive inference framework that jointly controls vision token number and model compute capability in response to varying input contents and compute budgets. 为避免挤压 `MULTIMODAL-REPRESENTATION` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-20357:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-20368:start -->
`SF-2026-ARXIV-2607-20368` 的 exact-v1 Deep Review 已保留。其机制为：We propose Self Gradient Forcing (SGF), a two-pass training strategy that restores this missing supervision signal without backpropagating through the full serial rollout. 为避免挤压 `MULTIMODAL-GENERATIVE-PARADIGMS` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-20368:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-20379:start -->
`SF-2026-ARXIV-2607-20379` 的 exact-v1 Deep Review 已保留。其机制为：An explanation is deemed faithful if the activation can be regenerated from it. 为避免挤压 `PLATFORM-EVALUATION-SYSTEM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-20379:end -->

### Selected Analysis Narratives

<!-- analysis:DA-20260723-01:start -->
### FineServe: A Fine-Grained Dataset and Characterization of Global LLM Serving Workloads

**约束变化与机制。** Large language models (LLMs) are increasingly deployed as always-on online services, making efficient LLM serving a critical systems challenge.

**证明与未证明。** FineServe is available at https://github.com/hihiztc1/FineServe. 但 Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 旧方案在不承受该约束时仍成立。

关联：`review:SF-2026-ARXIV-2607-19349`。
<!-- analysis:DA-20260723-01:end -->

<!-- analysis:DA-20260723-02:start -->
### NEXUS: Structured Runtime Safety for Tool-Using LLM Agents

**约束变化与机制。** We present NEXUS (Neural EXecution Utility and Safety), a structured-plan safety monitor that applies a formal intervention policy to select among four actions: allow, block, request confirmation, or request revision.

**证明与未证明。** On a 128-instance synthetic benchmark, NEXUS achieves an F1 score of 0.949 and a 4-class intervention accuracy of 0.6406, outperforming rule-only intervention selection by 27.3 percentage points. 但 NEXUS is explicitly not a replacement for model alignment, content-safety filtering, or post-execution audit; it is a runtime layer between plan production and execution that complements those other mechanisms. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：NEXUS is explicitly not a replacement for model alignment, content-safety filtering, or post-execution audit; it is a runtime layer between plan production and execution that complements those other mechanisms. 旧方案在不承受该约束时仍成立。

关联：`review:SF-2026-ARXIV-2607-19356`。
<!-- analysis:DA-20260723-02:end -->

<!-- analysis:DA-20260723-03:start -->
### Fine-grained Computation-Communication Overlap via Tile-level Signaling and Scheduling for Mixture-of-Experts

**约束变化与机制。** We present a fine-grained approach that overlaps expert compute with the second all-to-all via tile-level signaling and scheduling.

**证明与未证明。** On a 4-A100 GPU platform, evaluated on three MoE models against four state-of-the-art MoE systems, our approach achieves up to 2.64x end-to-end speedup and 2.74x MoE-layer speedup. 但 Future work includes extension to the backward pass for training, adaptive SM partition selection, support for additional parallelism regimes, and deployment on larger machines. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：Future work includes extension to the backward pass for training, adaptive SM partition selection, support for additional parallelism regimes, and deployment on larger machines. 旧方案在不承受该约束时仍成立。

关联：`review:SF-2026-ARXIV-2607-19539`。
<!-- analysis:DA-20260723-03:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

None。建议路由已冻结到 date-local queue；最终 disposition 等待 root 按日期串行对读 Books。

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260723-COVERAGE-INDEPENDENT | fresh-context:pending-root-auditor | coverage | coverage:SRC-ARXIV:20260723 | GAP-20260723-COVERAGE-INDEPENDENT：全量筛选尚未被独立反向审计 | Pending — 逐项核验 false positive / false negative | open |
| SA-20260723-EVIDENCE-INDEPENDENT | fresh-context:pending-root-auditor | evidence | validator:review-completion-v1 | GAP-20260723-EVIDENCE-INDEPENDENT：RP 尚需独立对照 exact v1 | Pending — finding 绑定具体 family | open |
| SA-20260723-SELECTION-INDEPENDENT | fresh-context:pending-root-auditor | deep_analysis_selection | validator:deep-analysis-selection-v1 | GAP-20260723-SELECTION-INDEPENDENT：三项选择尚需 adversarial comparison | Pending — 比较 impact、反证与 owner 独立性 | open |
| SA-20260723-BOOKS-ROOT | fresh-context:pending-root-books-owner | books | validator:books-comparison-v1 | GAP-20260723-BOOKS-ROOT：尚未逐项对读 Books | Pending — root 消费 frozen queue | open |

## 8. Ignored Noise

327 项均有 family-specific pre-denominator closure：

- `embodied_task_local_method`：19
- `incremental_method_without_durable_system_delta`：251
- `local_benchmark_without_release_delta`：12
- `prior_retained_candidate`：1
- `theory_without_ai_system_contract`：5
- `vertical_application_without_system_delta`：39

## 9. Recommended Action

1. 独立审计 Coverage、Evidence 与 Selection；finding 只重开具体 family。
2. root 逐项比较 Books。建议起点：Integrate 50、No Change 67、Structural 0；不是最终决定。

## 10. Repository Changes

- 重建 `papers/2026/07/23/README.md` 及 date-local frozen queue。
- 未修改 Books、ROADMAP、docs、Learning State、Weekly。

## 11. Open Questions

- 独立审计是否恢复 closure 中的漏项？
- proposed Integrate 是否已被现有 Books 命题覆盖？

## 12. Sources

- [FineServe: A Fine-Grained Dataset and Characterization of Global LLM Serving Workloads](https://arxiv.org/html/2607.19349v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [OpenEvoShield: Dual Non-Stationary Continual Defense for Open-World Multi-Agent System Attacks](https://arxiv.org/html/2607.19351v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [Benchmarking Confidential GPU Inference on NVIDIA H100 under Intel TDX](https://arxiv.org/html/2607.19353v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [Information Discernment in Large Language Models](https://arxiv.org/html/2607.19355v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [NEXUS: Structured Runtime Safety for Tool-Using LLM Agents](https://arxiv.org/html/2607.19356v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [LISA: Linear-Indexed Sparse Attention for Efficient Long-Context Reasoning](https://arxiv.org/html/2607.19358v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [Profile-Graph Memory for LLM Agents: Implicit Cross-Entity Traversal through Narrative Profiles](https://arxiv.org/html/2607.19359v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [Stateful Guardrails for Multi-Turn LLM Systems: A Conversational Risk Accumulation Framework](https://arxiv.org/html/2607.19361v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [GraphContainer: A Unified Platform for Comparing and Debugging Graph RAG Methods](https://arxiv.org/html/2607.19362v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [AdaRoPE: Not All Attention Heads Should Rotate and Scale Equally](https://arxiv.org/html/2607.19363v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [Rethinking Uncertainty Evaluation in Large Language Models](https://arxiv.org/html/2607.19367v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [Spectral-LSH: Sub-Quadratic Prompt Compression via Krylov-Projected Locality-Sensitive Hashing](https://arxiv.org/html/2607.19368v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [Building Fast, Evaluating Slow: Pipeline Choices Dominate Autointerpretability Score Variance](https://arxiv.org/html/2607.19386v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [The Orthogonalized Read Is a Removable Training Scaffold for Recurrent Memory](https://arxiv.org/html/2607.19390v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [Decodable but Not Detectable: A Leakage Fingerprint for Near-OOD Benchmarks](https://arxiv.org/html/2607.19393v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [From Trajectories to Prefixes: Reusing Teacher Trajectories via Replayed Prefixes and Online Continuation](https://arxiv.org/html/2607.19395v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [CrackedPDFs: A Controlled Benchmark for Hidden Prompt Injection in PDFs](https://arxiv.org/html/2607.19396v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [Leveraging Offline Supervision for Efficient and Generalizable Reinforcement Learning in Large-Scale Vision-Language-Action Models](https://arxiv.org/html/2607.19399v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [Reproducing Recurrent Transformers: The CoTFormer](https://arxiv.org/html/2607.19405v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [ITPEval: Benchmarking Formal Translation Across Interactive Theorem Provers](https://arxiv.org/html/2607.19407v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [Reward-Aware Population Scaling of Evolutionary Strategies in LLM Fine-Tuning](https://arxiv.org/html/2607.19408v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [JailMeter: An Evidence-Based Evaluation Framework for Jailbreak Attacks on Large Language Models](https://arxiv.org/html/2607.19424v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [ChannelGuard: Safe Models Do Not Compose into Safe Multi-Agent Systems](https://arxiv.org/html/2607.19430v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [BRIM: Workload-Balanced Dual-Sided Bit-Serial Sparse Inference Accelerator](https://arxiv.org/html/2607.19431v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [ChainWatch: A Kill Chain-Aligned Sequential Detection Framework for Multi-Step Attacks in MCP-Based AI Agent Systems](https://arxiv.org/html/2607.19432v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [The Chronos Vulnerability: A Taxonomy of Temporal Persistence and Memory-Based Deception in Agentic AI](https://arxiv.org/html/2607.19433v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [BaseRT: Advancing Best-in-Class LLM Inference with Apple M5 Neural Accelerators](https://arxiv.org/html/2607.19438v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [Unlearning as Distribution Restoration: A Controlled Counterfactual Study, a Validated Selective Screen, and the Limits of Oracle-Free Certification](https://arxiv.org/html/2607.19442v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [Guardrails as Scapegoats: Auditing Unfaithful Safety Refusals in Tool-Augmented LLM Agents](https://arxiv.org/html/2607.19449v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [REGEN: Replay-recycling for Expert-to-Generalist distillation with Offline Reinforcement Learning](https://arxiv.org/html/2607.19450v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [MoA-Structured Decode Attention DNF Derivation, KV-Cache Accumulation, GQA/MQA, and OpenACC Kernel](https://arxiv.org/html/2607.19456v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [Integrity of peer-to-peer distributed LLM inference under malicious nodes](https://arxiv.org/html/2607.19490v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [BLUE: Semantics-Preserving Video Compression for Efficient Vision-Language Surveillance Analytics](https://arxiv.org/html/2607.19515v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [When Reasoning Narrows the Move: Diversity Collapse in LLM Game Play](https://arxiv.org/html/2607.19523v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [Fine-grained Computation-Communication Overlap via Tile-level Signaling and Scheduling for Mixture-of-Experts](https://arxiv.org/html/2607.19539v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [ChronoStitch: Training-Free Composition of Visual KV Memories for Long-Horizon Temporal Reasoning](https://arxiv.org/html/2607.19547v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [Knowledge-Centric Self-Improvement](https://arxiv.org/html/2607.19592v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [Twin Agent: Context Residual Compression for Privilege Separated Agents](https://arxiv.org/html/2607.19595v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [Scaling Laws for Hypernetwork-Based Knowledge Injection in Large Language Models](https://arxiv.org/html/2607.19604v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [Task Competence Is Not Instruction Following: Evaluating Instruction-Conflicting Behavior in Small Language Models](https://arxiv.org/html/2607.19608v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [The Mechanism Matters: When Knowledge Graphs Help Reinforcement Learning](https://arxiv.org/html/2607.19616v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [From Bit-Position Sensitivity to Unequal Error Protection for DNN Inference Memory](https://arxiv.org/html/2607.19623v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [Adaptive Capitulation: A Structural Failure Mode of LLM Responses in Vulnerability Contexts](https://arxiv.org/html/2607.19629v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [Do Co-Located AI Training Jobs Synchronize? Load-Dependent Throttling as a Coupling Mechanism for Phase-Locking Behind a Shared Power Cap](https://arxiv.org/html/2607.19638v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [PerfAgent: Profiler-Guided Iterative Refinement for Repository-Level Code Optimization](https://arxiv.org/html/2607.19653v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [Same Game, Different Story: A Minimal Conservative Strategic Robustness Benchmark for Large Language Model Agents](https://arxiv.org/html/2607.19670v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [Reference-Free Evaluation of Reasoning in Open-Ended Question Answering](https://arxiv.org/html/2607.19678v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [GhostPrompt: Cross-Image Adversarial Prompt for Vision-Language Models](https://arxiv.org/html/2607.19683v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [Multi-Mask Diffusion Language Models for Few-Step Generation](https://arxiv.org/html/2607.19686v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [SLPO: Scaling Latent Reasoning via a Surrogate Policy](https://arxiv.org/html/2607.19691v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [NavVerse: Benchmarking Indoor-to-Outdoor Embodied Navigation in Continuous Robot Simulation](https://arxiv.org/html/2607.19695v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [SafeGen: Goal-Conditioned Video Diffusion of Safety-Critical Scenarios for VLM-Based Autonomous Driving](https://arxiv.org/html/2607.19701v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [Efficient Clustering with Provable Guardrails for LLM Inference at Scale](https://arxiv.org/html/2607.19704v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [How Fast Can Reward Models Score? A Systems Study of C++ and PyTorch Inference Runtimes for RLHF](https://arxiv.org/html/2607.19712v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [Koopman Dreamer: Spectrally Constrained Latent Dynamics for Stable World-Model Imagination](https://arxiv.org/html/2607.19719v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [Beyond Relevance-Centric Retrieval: Rubric-Oriented Document Set Selection and Ranking](https://arxiv.org/html/2607.19747v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [The World Model Remembers, the Actor Forgets: Dream Rehearsal for Continual Model-Based RL](https://arxiv.org/html/2607.19749v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [An Isotropy-Preserving Spectral Cap for Muon: Theory and Three Case Studies](https://arxiv.org/html/2607.19771v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [Defer to Plan: Adaptive Multi-Agent Fusion for End-to-End V2X Driving](https://arxiv.org/html/2607.19774v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [Trace: A Taxonomy-Guided Environment for Multidomain Visual Reasoning](https://arxiv.org/html/2607.19790v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [Silent Failures in Multimodal Agentic Search:A Diagnostic Taxonomy and Cross-Judge Evaluation](https://arxiv.org/html/2607.19793v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [OPIUM: Mitigating Steering Externalities and Over-Refusal via Dual Objective Latent Optimization](https://arxiv.org/html/2607.19806v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [Dreamer-CPC: Message Learning with World Models for Decentralized Multi-agent Reinforcement Learning](https://arxiv.org/html/2607.19809v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [Rewarding Better Thinking for LLM Preference Alignment](https://arxiv.org/html/2607.19824v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [Clinical Pathways as Safety Specifications for Physical AI in Hospital Wards](https://arxiv.org/html/2607.19827v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [DARWIN: Evolving Jailbreak Adversary and Guardrail for LLM Safety Evaluation and Protection](https://arxiv.org/html/2607.19829v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [Know Your Agent: Reconnaissance-Driven Pentesting of AI Agents](https://arxiv.org/html/2607.19837v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [emb-diversity: A Tool for Embedding-Based Measurement of Data Diversity](https://arxiv.org/html/2607.19848v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [SOPD-SocialNav: Selective On-Policy Distillation for Vision-Language Social Navigation](https://arxiv.org/html/2607.19850v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [Memory-Augmented Multimodal Large Language Models for Small Object Understanding in Streaming Aerial Videos](https://arxiv.org/html/2607.19857v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [DocOps: A Verifiable Benchmark for Autonomous Agents in Complex Document Operations](https://arxiv.org/html/2607.19865v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [KineBench: Benchmarking Embodied World Models via IDM-Free Kinematic Grounding](https://arxiv.org/html/2607.19876v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [EA-Nav: Learning Safe Visual Navigation Policies with Embodiment Awareness](https://arxiv.org/html/2607.19880v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [Defense Against LLM Backdoors using Critical Neuron Isolation Pruning](https://arxiv.org/html/2607.19894v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [Harnessing Disagreement: Detecting Correlated Agreement Blindness in Multi-Agent Triage](https://arxiv.org/html/2607.19899v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [MV-Bench: Benchmarking Multimodal Large Language Models for Coordinated Multi-View Interface Construction](https://arxiv.org/html/2607.19910v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [JANUS: Foreseeing Latent Risk for Long-Horizon Agent Safety](https://arxiv.org/html/2607.19913v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [Diffusion ReRoll: Revisable Denoising for Robotic Sequential Prediction](https://arxiv.org/html/2607.19919v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [DGNA: Dissecting GPU NUMA Architecture through Microbenchmarking and Data Analysis](https://arxiv.org/html/2607.19922v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [Efficient Chain-of-Modality Reasoning via Progressive Compression for Spoken Language Models](https://arxiv.org/html/2607.19932v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [SenWorld: A Digital-Twin Simulation for Generating Context-Rich Evaluation Data](https://arxiv.org/html/2607.19949v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [HijackKV: New Threat in Position-Independent KV Cache Reuse](https://arxiv.org/html/2607.19957v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [EvoThink: Evolving Thinking in Large Reasoning Models via Self-Pruning and Aha-Moment Preference Optimization](https://arxiv.org/html/2607.19962v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [Unified Prediction and Planning via Conflict-Aware Disjoint Parameter Training](https://arxiv.org/html/2607.19971v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [Coordinating from Memory: Graph-Structured Experience Reuse for Multi-Agent Adaptation in Dynamic Manufacturing](https://arxiv.org/html/2607.19985v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [CLARK: Closed-loop Learning for Adaptive Reasoning over Knowledge Graphs](https://arxiv.org/html/2607.19996v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [PRO-LONG: Programmatic Memory Enables Long-Horizon Reasoning](https://arxiv.org/html/2607.20064v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [Co-Evolving LLM Evaluators and Policies via DynamicRubric](https://arxiv.org/html/2607.20083v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [Reinforcement Learning for Large Language Model Selective Evidence Adoption from Contaminated Retrieval Results](https://arxiv.org/html/2607.20090v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [Extreme-RGMT: Continual Learning of Highly Dynamic Skills for Robust Generalist Humanoid Control](https://arxiv.org/html/2607.20110v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [Ascend to Science: Exploration of AI Chips for Scientific Computing](https://arxiv.org/html/2607.20120v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [OpenSkillRisk: Benchmarking Agent Safety When Using Real-World Risky Third-Party Skills](https://arxiv.org/html/2607.20121v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [HeadCast: Casting Attention Heads for Efficient Autoregressive Video Generation](https://arxiv.org/html/2607.20125v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [CUSUM-Shaped Inference-Time Monitoring and Targeted Re-Decoding for Quantized Small Language Model Reasoning](https://arxiv.org/html/2607.20129v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [SLAI T-Rex: Full-Parameter Post-training of the DeepSeek-V4 Family on Ascend SuperPOD](https://arxiv.org/html/2607.20145v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [Gotta Catch them all: the modes of Sycophancy](https://arxiv.org/html/2607.20146v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [Audio-Zero: Label-Free Self-Evolution for Fine-Grained Audio Reasoning](https://arxiv.org/html/2607.20166v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [StreamHOI: Interaction-aware Temporal Memory Adaptation for Streaming HOI Video Generation](https://arxiv.org/html/2607.20174v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [On Optimization Complexity of Second-Order Certified Unlearning](https://arxiv.org/html/2607.20192v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [Statistical Inference for Rank Allocation in Low-Rank Adaptation](https://arxiv.org/html/2607.20205v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [ELSAA: Efficient Low-Rank and Sparse Attention Approximation for Training Transformers](https://arxiv.org/html/2607.20214v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [MoX: Efficient MoE Routing on Direct-Connect Topologies](https://arxiv.org/html/2607.20220v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [The Maskability Index: Predicting Task-Objective Alignment in Pretrained Language Models](https://arxiv.org/html/2607.20265v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [Sound Probabilistic Safety Bounds for Large Language Models](https://arxiv.org/html/2607.20286v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [Courteous Anticipation: Improving Long-Lived Task Planning in Persistent Shared Environments](https://arxiv.org/html/2607.20289v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [Evolving Cache Schedules for Fast Diffusion Policy Inference](https://arxiv.org/html/2607.20293v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [Don't Trust the Label: License Laundering in AI Supply Chains](https://arxiv.org/html/2607.20300v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [The Blessing of Dimensionality: How Near-Orthogonality in High-Dimensional Spaces Explains Temporal Portability](https://arxiv.org/html/2607.20301v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [PyroDash: Cost-Efficient Token-Level Small-Large Language Model Collaborative Inference](https://arxiv.org/html/2607.20327v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [Closing the Lab-to-Store Gap: A Data-Efficient Post-Training and Experience-Driven Learning VLA Framework for Retail Humanoids](https://arxiv.org/html/2607.20345v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [Test-Time Training for Modality Order Consistency in Vision-Language Models](https://arxiv.org/html/2607.20351v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [Look Less, Think Faster: Joint Token-Compute Adaptation for Multimodal LLMs](https://arxiv.org/html/2607.20357v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [Self Gradient Forcing: Native Long Video Extrapolation](https://arxiv.org/html/2607.20368v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [Notes to Self: Can LLMs Benefit from Experiential Abstractions?](https://arxiv.org/html/2607.20372v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [Train the Model, Not the Reader: Decodability Supervision for Verifiable Activation Explanations](https://arxiv.org/html/2607.20379v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [PercepCap: Video Captioner with Structured Spatio-Temporal Perception](https://arxiv.org/html/2607.20389v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04
- [SoftReason: A Fully Differentiable Neuro-Soft-Symbolic Deductive Reasoning Architecture over High-Dimensional Perceptual Data](https://arxiv.org/html/2607.20402v1) — first-public（Asia/Shanghai）：2026-07-23；exact evidence：v1；accessed：2026-09-04

## 13. Final Status

Author-side screening、denominator、exact-v1 access、117/117 Review 与 Deep Selection receipt 已构建；Books 写回冻结，四项独立审计未完成。

State Truth: Completion=In Progress；Coverage=Open；Evidence=Open；Books=Open；Unresolved Findings=4。
