# Daily Research — 2026-07-22

**Research Date:** 2026-07-22

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-07-21 09:00:00 ～ 2026-07-22 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；Historical Daily 独立重建，不使用 Weekly 作为 discovery、评分或 Review 来源

**Status:** In Progress；Coverage=Open、Evidence=Open、Books=Open；author-side evidence 已闭合，等待独立 Semantic Audit 与 root Books 比较

## Executive Summary

官方 owner inventory 共 **495** 个 identity；全量 title + abstract 筛选后冻结 **96** 个候选与 **399** 个 family-specific closure，retain rate **19.39%**。exact-v1 Review 为 96/96：Deep 40、Standard 56、blocked 0。

当前只是 author-side evidence 闭合：Books disposition 仍为 `Not Assessed`，四项 fresh-context 独立审计保持 Open。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-07-22 |
| Window End | 2026-07-22 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | daily-2026-07-22-0900-v2.1-sha256:e5b11c474080b42f6163da82709ce54e116b29df3ffe74393344133b4ead8042 |
| Denominator Frozen At | 2026-09-04T10:00:00+08:00 |
| Completion Status | In Progress |
| Coverage Gate | Open |
| Evidence Gate | Open |
| Books Gate | Open |

### Source Coverage Receipt

<!-- coverage:SRC-ARXIV:20260722:start -->
<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-07-21T09:00:00+08:00 | 2026-07-22T09:00:00+08:00 | 2026-09-04T10:00:00+08:00 | official listings + v1 history + availability schedule; DataCite created only for cycle reconciliation | checked | 495 | SF-2026-ARXIV-2607-18240;SF-2026-ARXIV-2607-18241;SF-2026-ARXIV-2607-18242;SF-2026-ARXIV-2607-18243;SF-2026-ARXIV-2607-18246;SF-2026-ARXIV-2607-18253;SF-2026-ARXIV-2607-18254;SF-2026-ARXIV-2607-18261;SF-2026-ARXIV-2607-18264;SF-2026-ARXIV-2607-18265;SF-2026-ARXIV-2607-18280;SF-2026-ARXIV-2607-18284;SF-2026-ARXIV-2607-18292;SF-2026-ARXIV-2607-18295;SF-2026-ARXIV-2607-18305;SF-2026-ARXIV-2607-18314;SF-2026-ARXIV-2607-18316;SF-2026-ARXIV-2607-18336;SF-2026-ARXIV-2607-18347;SF-2026-ARXIV-2607-18357;SF-2026-ARXIV-2607-18360;SF-2026-ARXIV-2607-18366;SF-2026-ARXIV-2607-18367;SF-2026-ARXIV-2607-18445;SF-2026-ARXIV-2607-18454;SF-2026-ARXIV-2607-18476;SF-2026-ARXIV-2607-18481;SF-2026-ARXIV-2607-18485;SF-2026-ARXIV-2607-18496;SF-2026-ARXIV-2607-18508;SF-2026-ARXIV-2607-18532;SF-2026-ARXIV-2607-18548;SF-2026-ARXIV-2607-18553;SF-2026-ARXIV-2607-18575;SF-2026-ARXIV-2607-18577;SF-2026-ARXIV-2607-18580;SF-2026-ARXIV-2607-18603;SF-2026-ARXIV-2607-18631;SF-2026-ARXIV-2607-18639;SF-2026-ARXIV-2607-18659;SF-2026-ARXIV-2607-18664;SF-2026-ARXIV-2607-18665;SF-2026-ARXIV-2607-18673;SF-2026-ARXIV-2607-18684;SF-2026-ARXIV-2607-18709;SF-2026-ARXIV-2607-18711;SF-2026-ARXIV-2607-18715;SF-2026-ARXIV-2607-18722;SF-2026-ARXIV-2607-18754;SF-2026-ARXIV-2607-18759;SF-2026-ARXIV-2607-18785;SF-2026-ARXIV-2607-18802;SF-2026-ARXIV-2607-18816;SF-2026-ARXIV-2607-18821;SF-2026-ARXIV-2607-18826;SF-2026-ARXIV-2607-18828;SF-2026-ARXIV-2607-18840;SF-2026-ARXIV-2607-18847;SF-2026-ARXIV-2607-18859;SF-2026-ARXIV-2607-18867;SF-2026-ARXIV-2607-18886;SF-2026-ARXIV-2607-18915;SF-2026-ARXIV-2607-18917;SF-2026-ARXIV-2607-18924;SF-2026-ARXIV-2607-18957;SF-2026-ARXIV-2607-18975;SF-2026-ARXIV-2607-18979;SF-2026-ARXIV-2607-19022;SF-2026-ARXIV-2607-19033;SF-2026-ARXIV-2607-19038;SF-2026-ARXIV-2607-19058;SF-2026-ARXIV-2607-19096;SF-2026-ARXIV-2607-19102;SF-2026-ARXIV-2607-19139;SF-2026-ARXIV-2607-19182;SF-2026-ARXIV-2607-19190;SF-2026-ARXIV-2607-19191;SF-2026-ARXIV-2607-19194;SF-2026-ARXIV-2607-19214;SF-2026-ARXIV-2607-19215;SF-2026-ARXIV-2607-19243;SF-2026-ARXIV-2607-19257;SF-2026-ARXIV-2607-19262;SF-2026-ARXIV-2607-19267;SF-2026-ARXIV-2607-19292;SF-2026-ARXIV-2607-19297;SF-2026-ARXIV-2607-19301;SF-2026-ARXIV-2607-19317;SF-2026-ARXIV-2607-19322;SF-2026-ARXIV-2607-19326;SF-2026-ARXIV-2607-19336;SF-2026-ARXIV-2607-19338;SF-2026-ARXIV-2607-19339;SF-2026-ARXIV-2607-19343;SF-2026-ARXIV-2607-19344;SF-2026-ARXIV-2607-19345 | all registered category pages; cross-category dedup complete | 2026-07-22T09:00:00+08:00 | sha256:e5b11c474080b42f6163da82709ce54e116b29df3ffe74393344133b4ead8042 | — |
<!-- coverage:SRC-ARXIV:20260722:end -->

### Coverage Limitations

- DataCite 只辅助 owner reconciliation；技术结论全部回到 official exact arXiv v1。
- author-side receipt 已闭合，独立 false-positive / false-negative audit 尚未签收。

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-18240 | arXiv:2607.18240v1 | paper-v1:2607.18240 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-18240 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18241 | arXiv:2607.18241v1 | paper-v1:2607.18241 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-18241 | self | — | new_in_window | AGENT-WORKFLOW | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18242 | arXiv:2607.18242v1 | paper-v1:2607.18242 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-18242 | self | — | new_in_window | AGENT-MCP | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18243 | arXiv:2607.18243v1 | paper-v1:2607.18243 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-18243 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18246 | arXiv:2607.18246v1 | paper-v1:2607.18246 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-18246 | self | — | new_in_window | AGENT-PLATFORM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18253 | arXiv:2607.18253v1 | paper-v1:2607.18253 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-18253 | self | — | new_in_window | INFER-SCHEDULING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18254 | arXiv:2607.18254v1 | paper-v1:2607.18254 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-18254 | self | — | new_in_window | INFER-TENSORRT-LLM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18261 | arXiv:2607.18261v1 | paper-v1:2607.18261 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-18261 | self | — | new_in_window | AGENT-TOOL-CALLING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18264 | arXiv:2607.18264v1 | paper-v1:2607.18264 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-18264 | self | — | new_in_window | MODEL-DECODER-ONLY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18265 | arXiv:2607.18265v1 | paper-v1:2607.18265 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-18265 | self | — | new_in_window | AGENT-MULTI-AGENT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18280 | arXiv:2607.18280v1 | paper-v1:2607.18280 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-18280 | self | — | new_in_window | INFER-GPU-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18284 | arXiv:2607.18284v1 | paper-v1:2607.18284 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-18284 | self | — | new_in_window | INFER-GPU-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18292 | arXiv:2607.18292v1 | paper-v1:2607.18292 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-18292 | self | — | new_in_window | WORLDVIEW-LLM-INTELLIGENCE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18295 | arXiv:2607.18295v1 | paper-v1:2607.18295 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-18295 | self | — | new_in_window | TRAIN-RLHF | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18305 | arXiv:2607.18305v1 | paper-v1:2607.18305 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-18305 | self | — | new_in_window | WORLDVIEW-WHY-MODELS-LEARN | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18314 | arXiv:2607.18314v1 | paper-v1:2607.18314 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-18314 | self | — | new_in_window | PLATFORM-TRAINING-OPERATOR | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18316 | arXiv:2607.18316v1 | paper-v1:2607.18316 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-18316 | self | — | new_in_window | AGENT-TOOL-CALLING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18336 | arXiv:2607.18336v1 | paper-v1:2607.18336 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-18336 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18347 | arXiv:2607.18347v1 | paper-v1:2607.18347 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-18347 | self | — | new_in_window | AGENT-PLATFORM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18357 | arXiv:2607.18357v1 | paper-v1:2607.18357 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-18357 | self | — | new_in_window | MODEL-SAMPLING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18360 | arXiv:2607.18360v1 | paper-v1:2607.18360 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-18360 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18366 | arXiv:2607.18366v1 | paper-v1:2607.18366 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-18366 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18367 | arXiv:2607.18367v1 | paper-v1:2607.18367 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-18367 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18445 | arXiv:2607.18445v1 | paper-v1:2607.18445 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-18445 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18454 | arXiv:2607.18454v1 | paper-v1:2607.18454 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-18454 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18476 | arXiv:2607.18476v1 | paper-v1:2607.18476 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-18476 | self | — | new_in_window | MODEL-SAMPLING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18481 | arXiv:2607.18481v1 | paper-v1:2607.18481 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-18481 | self | — | new_in_window | TRAIN-GRPO | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18485 | arXiv:2607.18485v1 | paper-v1:2607.18485 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-18485 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18496 | arXiv:2607.18496v1 | paper-v1:2607.18496 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-18496 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18508 | arXiv:2607.18508v1 | paper-v1:2607.18508 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-18508 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18532 | arXiv:2607.18532v1 | paper-v1:2607.18532 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-18532 | self | — | new_in_window | TRAIN-GRPO | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18548 | arXiv:2607.18548v1 | paper-v1:2607.18548 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-18548 | self | — | new_in_window | AGENT-PLATFORM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18553 | arXiv:2607.18553v1 | paper-v1:2607.18553 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-18553 | self | — | new_in_window | AGENT-REFLECTION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18575 | arXiv:2607.18575v1 | paper-v1:2607.18575 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-18575 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18577 | arXiv:2607.18577v1 | paper-v1:2607.18577 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-18577 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18580 | arXiv:2607.18580v1 | paper-v1:2607.18580 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-18580 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18603 | arXiv:2607.18603v1 | paper-v1:2607.18603 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-18603 | self | — | new_in_window | AGENT-RAG | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18631 | arXiv:2607.18631v1 | paper-v1:2607.18631 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-18631 | self | — | new_in_window | MODEL-MOE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18639 | arXiv:2607.18639v1 | paper-v1:2607.18639 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-18639 | self | — | new_in_window | TRAIN-RLHF | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18659 | arXiv:2607.18659v1 | paper-v1:2607.18659 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-18659 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18664 | arXiv:2607.18664v1 | paper-v1:2607.18664 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-18664 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18665 | arXiv:2607.18665v1 | paper-v1:2607.18665 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-18665 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18673 | arXiv:2607.18673v1 | paper-v1:2607.18673 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-18673 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18684 | arXiv:2607.18684v1 | paper-v1:2607.18684 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-18684 | self | — | new_in_window | INFER-SCHEDULING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18709 | arXiv:2607.18709v1 | paper-v1:2607.18709 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-18709 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18711 | arXiv:2607.18711v1 | paper-v1:2607.18711 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-18711 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18715 | arXiv:2607.18715v1 | paper-v1:2607.18715 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-18715 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18722 | arXiv:2607.18722v1 | paper-v1:2607.18722 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-18722 | self | — | new_in_window | TRAIN-GRPO | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18754 | arXiv:2607.18754v1 | paper-v1:2607.18754 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-18754 | self | — | new_in_window | PLATFORM-TRACE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18759 | arXiv:2607.18759v1 | paper-v1:2607.18759 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-18759 | self | — | new_in_window | MODEL-POSITION-ENCODING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18785 | arXiv:2607.18785v1 | paper-v1:2607.18785 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-18785 | self | — | new_in_window | AGENT-PLATFORM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18802 | arXiv:2607.18802v1 | paper-v1:2607.18802 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-18802 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18816 | arXiv:2607.18816v1 | paper-v1:2607.18816 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-18816 | self | — | new_in_window | AGENT-PLATFORM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18821 | arXiv:2607.18821v1 | paper-v1:2607.18821 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-18821 | self | — | new_in_window | AGENT-WORKFLOW | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18826 | arXiv:2607.18826v1 | paper-v1:2607.18826 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-18826 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18828 | arXiv:2607.18828v1 | paper-v1:2607.18828 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-18828 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18840 | arXiv:2607.18840v1 | paper-v1:2607.18840 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-18840 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18847 | arXiv:2607.18847v1 | paper-v1:2607.18847 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-18847 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18859 | arXiv:2607.18859v1 | paper-v1:2607.18859 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-18859 | self | — | new_in_window | AGENT-PLATFORM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18867 | arXiv:2607.18867v1 | paper-v1:2607.18867 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-18867 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18886 | arXiv:2607.18886v1 | paper-v1:2607.18886 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-18886 | self | — | new_in_window | AGENT-WORKFLOW | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18915 | arXiv:2607.18915v1 | paper-v1:2607.18915 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-18915 | self | — | new_in_window | TRAIN-GRPO | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18917 | arXiv:2607.18917v1 | paper-v1:2607.18917 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-18917 | self | — | new_in_window | AGENT-RAG | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18924 | arXiv:2607.18924v1 | paper-v1:2607.18924 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-18924 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18957 | arXiv:2607.18957v1 | paper-v1:2607.18957 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-18957 | self | — | new_in_window | PLATFORM-MODEL-REGISTRY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18975 | arXiv:2607.18975v1 | paper-v1:2607.18975 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-18975 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18979 | arXiv:2607.18979v1 | paper-v1:2607.18979 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-18979 | self | — | new_in_window | TRAIN-GRPO | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19022 | arXiv:2607.19022v1 | paper-v1:2607.19022 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-19022 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19033 | arXiv:2607.19033v1 | paper-v1:2607.19033 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-19033 | self | — | new_in_window | MODEL-TOKENIZER | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19038 | arXiv:2607.19038v1 | paper-v1:2607.19038 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-19038 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19058 | arXiv:2607.19058v1 | paper-v1:2607.19058 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-19058 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19096 | arXiv:2607.19096v1 | paper-v1:2607.19096 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-19096 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19102 | arXiv:2607.19102v1 | paper-v1:2607.19102 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-19102 | self | — | new_in_window | PLATFORM-TRACE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19139 | arXiv:2607.19139v1 | paper-v1:2607.19139 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-19139 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19182 | arXiv:2607.19182v1 | paper-v1:2607.19182 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-19182 | self | — | new_in_window | PLATFORM-KUBEFLOW | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19190 | arXiv:2607.19190v1 | paper-v1:2607.19190 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-19190 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19191 | arXiv:2607.19191v1 | paper-v1:2607.19191 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-19191 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19194 | arXiv:2607.19194v1 | paper-v1:2607.19194 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-19194 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19214 | arXiv:2607.19214v1 | paper-v1:2607.19214 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-19214 | self | — | new_in_window | PLATFORM-COST | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19215 | arXiv:2607.19215v1 | paper-v1:2607.19215 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-19215 | self | — | new_in_window | AGENT-PLATFORM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19243 | arXiv:2607.19243v1 | paper-v1:2607.19243 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-19243 | self | — | new_in_window | MODEL-SAMPLING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19257 | arXiv:2607.19257v1 | paper-v1:2607.19257 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-19257 | self | — | new_in_window | AGENT-PROMPT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19262 | arXiv:2607.19262v1 | paper-v1:2607.19262 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-19262 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19267 | arXiv:2607.19267v1 | paper-v1:2607.19267 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-19267 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19292 | arXiv:2607.19292v1 | paper-v1:2607.19292 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-19292 | self | — | new_in_window | PLATFORM-MONITORING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19297 | arXiv:2607.19297v1 | paper-v1:2607.19297 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-19297 | self | — | new_in_window | AGENT-WORKFLOW | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19301 | arXiv:2607.19301v1 | paper-v1:2607.19301 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-19301 | self | — | new_in_window | AGENT-RAG | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19317 | arXiv:2607.19317v1 | paper-v1:2607.19317 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-19317 | self | — | new_in_window | WORLDVIEW-REPRESENTATION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19322 | arXiv:2607.19322v1 | paper-v1:2607.19322 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-19322 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19326 | arXiv:2607.19326v1 | paper-v1:2607.19326 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-19326 | self | — | new_in_window | AGENT-RAG | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19336 | arXiv:2607.19336v1 | paper-v1:2607.19336 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-19336 | self | — | new_in_window | AGENT-PLATFORM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19338 | arXiv:2607.19338v1 | paper-v1:2607.19338 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-19338 | self | — | new_in_window | AGENT-PLATFORM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19339 | arXiv:2607.19339v1 | paper-v1:2607.19339 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-19339 | self | — | new_in_window | AGENT-TOOL-CALLING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19343 | arXiv:2607.19343v1 | paper-v1:2607.19343 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-19343 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19344 | arXiv:2607.19344v1 | paper-v1:2607.19344 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-19344 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-19345 | arXiv:2607.19345v1 | paper-v1:2607.19345 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-19345 | self | — | new_in_window | MODEL-LONG-CONTEXT | Not Assessed | — | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-18240 | RP-db1213b61b8be62f | standard | arXiv:2607.18240v1 | SRC-ARXIV@arXiv:2607.18240v1 | https://arxiv.org/html/2607.18240v1#S4 — 4 Method: Evidence Chain Evaluation as Implemented | https://arxiv.org/html/2607.18240v1#S4 — 4 Method: Evidence Chain Evaluation as Implemented; https://arxiv.org/html/2607.18240v1#S5 — 5 Experiments | https://arxiv.org/html/2607.18240v1#S6 — 6 Discussion; https://arxiv.org/html/2607.18240v1#S6.SS2 — 6.2 Limitations | Exact v1 links https://github.com/cheshireyang/ECE.git, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18240 | complete |
| SF-2026-ARXIV-2607-18241 | RP-e2ac746111d7cb7c | deep | arXiv:2607.18241v1 | SRC-ARXIV@arXiv:2607.18241v1 | https://arxiv.org/html/2607.18241v1#S3 — 3 System Design; https://arxiv.org/html/2607.18241v1#S3.SS1 — 3.1 Architecture Overview | https://arxiv.org/html/2607.18241v1#S6 — 6 Empirical Evaluation; https://arxiv.org/html/2607.18241v1#S6.SS3 — 6.3 Comparative Evaluation | https://arxiv.org/html/2607.18241v1#S8 — 8 Limitations and Future Work; https://arxiv.org/html/2607.18241v1#S6.SS6 — 6.6 Discussion | Exact v1 links https://github.com/langchain-ai/langchain, https://github.com/run-llama/llama_index, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18241 | complete |
| SF-2026-ARXIV-2607-18242 | RP-018d489869dabb74 | standard | arXiv:2607.18242v1 | SRC-ARXIV@arXiv:2607.18242v1 | https://arxiv.org/html/2607.18242v1#S3 — 3. ToolDNS System Design; https://arxiv.org/html/2607.18242v1#S3.SS4 — 3.4. Iterative Resolution Algorithm | https://arxiv.org/html/2607.18242v1#S5 — 5. Experiments; https://arxiv.org/html/2607.18242v1#S5.SS4 — 5.4. Comparative Evaluation of Network Efficiency | https://arxiv.org/html/2607.18242v1#S2.SS2 — 2.2. Limitations of Existing Paradigms; https://arxiv.org/html/2607.18242v1#S6 — 6. Conclusion | Exact v1 links https://github.com/hku-icl/ToolDNS.git, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18242 | complete |
| SF-2026-ARXIV-2607-18243 | RP-81db8cb677d8e622 | standard | arXiv:2607.18243v1 | SRC-ARXIV@arXiv:2607.18243v1 | https://arxiv.org/html/2607.18243v1#S3 — III System and Threat Model; https://arxiv.org/html/2607.18243v1#S4 — IV Proposed Method | https://arxiv.org/html/2607.18243v1#S5 — V Performance Evaluation | https://arxiv.org/html/2607.18243v1#S3 — III System and Threat Model; https://arxiv.org/html/2607.18243v1#S4.SS1 — IV-A CPSAINT : Structural Failure Decomposition | Exact v1 links https://github.com/coderhard/friesa-k-DSN-crai2026, https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18243 | complete |
| SF-2026-ARXIV-2607-18246 | RP-6b2c2cacb54f3771 | deep | arXiv:2607.18246v1 | SRC-ARXIV@arXiv:2607.18246v1 | https://arxiv.org/html/2607.18246v1#A3.SS1 — C.1 Determinism Verification Methodology; https://arxiv.org/html/2607.18246v1#S2.SS1 — 2.1 Deterministic AI Systems | https://arxiv.org/html/2607.18246v1#A3 — Appendix C Experimental Evidence and Reproducibility; https://arxiv.org/html/2607.18246v1#A3.SS4 — C.4 Failure Injection Results | https://arxiv.org/html/2607.18246v1#A3.SS4 — C.4 Failure Injection Results; https://arxiv.org/html/2607.18246v1#S4.SS4 — 4.4 Failure Classification and Recovery | Exact v1 links https://github.com/halvrenofviryel/phionyx-research, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18246 | complete |
| SF-2026-ARXIV-2607-18253 | RP-2e83001ada056372 | deep | arXiv:2607.18253v1 | SRC-ARXIV@arXiv:2607.18253v1 | https://arxiv.org/html/2607.18253v1#S2 — 2 Background on LLM serving frameworks; https://arxiv.org/html/2607.18253v1#S4.SS1 — 4.1 Serving Framework Simulation (SFS) for latency estimation | https://arxiv.org/html/2607.18253v1#A7 — Appendix G Additional Experimental Results; https://arxiv.org/html/2607.18253v1#A4 — Appendix D Response Evaluation using LLM-as-a-judge | https://arxiv.org/html/2607.18253v1#S1 — 1 Introduction; https://arxiv.org/html/2607.18253v1#S2 — 2 Background on LLM serving frameworks | Exact v1 links https://github.com/tatsu-lab/stanford_alpaca, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18253 | complete |
| SF-2026-ARXIV-2607-18254 | RP-dbd62c2c8b5fced7 | standard | arXiv:2607.18254v1 | SRC-ARXIV@arXiv:2607.18254v1 | https://arxiv.org/html/2607.18254v1#S3 — 3 Method; https://arxiv.org/html/2607.18254v1#S4.SS1 — 4.1 Models | https://arxiv.org/html/2607.18254v1#S4 — 4 Experimental Setup; https://arxiv.org/html/2607.18254v1#S4.SS2 — 4.2 Benchmarks | https://arxiv.org/html/2607.18254v1#S7 — 7 Limitations; https://arxiv.org/html/2607.18254v1#S8 — 8 Future Work | Exact v1 links https://github.com/plawanrath/slm-to-mlir-constrained-emitter, https://huggingface.co/datasets/plawanrath/MLIR-Spec-150, https://huggingface.co/datasets/plawanrath/Linalg-Spec-30; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18254 | complete |
| SF-2026-ARXIV-2607-18261 | RP-edfe50236f5a9934 | standard | arXiv:2607.18261v1 | SRC-ARXIV@arXiv:2607.18261v1 | https://arxiv.org/html/2607.18261v1#A1 — Appendix A Model-by-Category Heatmap | https://arxiv.org/html/2607.18261v1#S3 — 3 Benchmark; https://arxiv.org/html/2607.18261v1#S4 — 4 Evaluation | https://arxiv.org/html/2607.18261v1#S6 — 6 Discussion; https://arxiv.org/html/2607.18261v1#S7 — 7 Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18261 | complete |
| SF-2026-ARXIV-2607-18264 | RP-a6b0212447cfa8d2 | standard | arXiv:2607.18264v1 | SRC-ARXIV@arXiv:2607.18264v1 | https://arxiv.org/html/2607.18264v1#S11 — 11 Method and training details; https://arxiv.org/html/2607.18264v1#S11.SS1 — 11.1 Implementation details | https://arxiv.org/html/2607.18264v1#S10 — 10 Benchmark details; https://arxiv.org/html/2607.18264v1#S4 — 4 Theoretical analysis | https://arxiv.org/html/2607.18264v1#S12 — 12 Limitations and broader impact; https://arxiv.org/html/2607.18264v1#S6 — 6 Conclusion | Exact v1 links https://github.com/MisakiTaro0414/mux, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18264 | complete |
| SF-2026-ARXIV-2607-18265 | RP-e7ce1f0bc6b90433 | standard | arXiv:2607.18265v1 | SRC-ARXIV@arXiv:2607.18265v1 | https://arxiv.org/html/2607.18265v1#S2 — II Methodology; https://arxiv.org/html/2607.18265v1#S6.SS1 — VI-A Mixed-model relays | https://arxiv.org/html/2607.18265v1#S2.SS5 — II-E Evaluation Metrics and Logging; https://arxiv.org/html/2607.18265v1#S3 — III Results | https://arxiv.org/html/2607.18265v1#S3.SS2 — III-B Failure Modes; https://arxiv.org/html/2607.18265v1#S4 — IV Discussion and Analysis | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18265 | complete |
| SF-2026-ARXIV-2607-18280 | RP-c3c98ba13a454e7b | deep | arXiv:2607.18280v1 | SRC-ARXIV@arXiv:2607.18280v1 | https://arxiv.org/html/2607.18280v1#S2 — 2 Methodology | https://arxiv.org/html/2607.18280v1#S3 — 3 Experiments; https://arxiv.org/html/2607.18280v1#S3.SS2 — 3.2 Main Results | https://arxiv.org/html/2607.18280v1#S4 — 4 Conclusion; https://arxiv.org/html/2607.18280v1#Sx1 — Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18280 | complete |
| SF-2026-ARXIV-2607-18284 | RP-afa31dce20e9acd7 | standard | arXiv:2607.18284v1 | SRC-ARXIV@arXiv:2607.18284v1 | https://arxiv.org/html/2607.18284v1#S3.SS1 — III-A The Transformer Architecture; https://arxiv.org/html/2607.18284v1#S3.SS3 — III-C BERT-based Architectures | https://arxiv.org/html/2607.18284v1#S6 — VI Experimental Results; https://arxiv.org/html/2607.18284v1#S6.SS1 — VI-A Experimental Setup | https://arxiv.org/html/2607.18284v1#S7 — VII Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18284 | complete |
| SF-2026-ARXIV-2607-18292 | RP-e028cc8565cd3f1e | standard | arXiv:2607.18292v1 | SRC-ARXIV@arXiv:2607.18292v1 | https://arxiv.org/html/2607.18292v1#A1 — Appendix A Models, Data, and Verifier Protocol; https://arxiv.org/html/2607.18292v1#A7 — Appendix G Detector Implementation | https://arxiv.org/html/2607.18292v1#S1 — 1 Introduction; https://arxiv.org/html/2607.18292v1#S2 — 2 Self-Conditioning Converts Persistent Risk into Bias | https://arxiv.org/html/2607.18292v1#S6 — 6 Discussion and Implications; https://arxiv.org/html/2607.18292v1#Sx1 — Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18292 | complete |
| SF-2026-ARXIV-2607-18295 | RP-636a95bbadffac9f | standard | arXiv:2607.18295v1 | SRC-ARXIV@arXiv:2607.18295v1 | https://arxiv.org/html/2607.18295v1#A1 — Appendix A Theoretical Framework; https://arxiv.org/html/2607.18295v1#S3 — 3 Method | https://arxiv.org/html/2607.18295v1#S2.SS2 — 2.2 Impossibility and No-Go Results in Alignment; https://arxiv.org/html/2607.18295v1#S4 — 4 Experiments | https://arxiv.org/html/2607.18295v1#S5 — 5 Discussion and Conclusion; https://arxiv.org/html/2607.18295v1#S2.SS1 — 2.1 Limitations of RLHF and Preference-Based Alignment | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18295 | complete |
| SF-2026-ARXIV-2607-18305 | RP-589896d810825a4c | standard | arXiv:2607.18305v1 | SRC-ARXIV@arXiv:2607.18305v1 | https://arxiv.org/html/2607.18305v1#S1 — 1 Introduction; https://arxiv.org/html/2607.18305v1#S2 — 2 Related Work | https://arxiv.org/html/2607.18305v1#S5.SS4 — 5.4 Experimental setup; https://arxiv.org/html/2607.18305v1#S7 — 7 Results | https://arxiv.org/html/2607.18305v1#S8 — 8 Discussion; https://arxiv.org/html/2607.18305v1#S9 — 9 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18305 | complete |
| SF-2026-ARXIV-2607-18314 | RP-3bec0ee17a5d7fbf | deep | arXiv:2607.18314v1 | SRC-ARXIV@arXiv:2607.18314v1 | https://arxiv.org/html/2607.18314v1#S2 — 2 System at a Glance; https://arxiv.org/html/2607.18314v1#S3 — 3 Control-Plane Design | https://arxiv.org/html/2607.18314v1#S5.SS2 — 5.2 From Request to Recorded Result | https://arxiv.org/html/2607.18314v1#S7 — 7 Conclusion; https://arxiv.org/html/2607.18314v1#Sx1 — Limitations | Exact v1 links https://github.com/yuntian-group/interactive-training, https://doi.org/10.18653/v1/2020.emnlp-demos.6, https://doi.org/10.18653/v1/2025.emnlp-demos.65; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18314 | complete |
| SF-2026-ARXIV-2607-18316 | RP-138d658a711bf89a | standard | arXiv:2607.18316v1 | SRC-ARXIV@arXiv:2607.18316v1 | https://arxiv.org/html/2607.18316v1#A3 — Appendix C Compute Environment and Model Details; https://arxiv.org/html/2607.18316v1#S5.SS3 — 5.3 Per-Model Heterogeneity | https://arxiv.org/html/2607.18316v1#A2 — Appendix B Per-Pattern Analysis; https://arxiv.org/html/2607.18316v1#S3 — 3 Benchmark | https://arxiv.org/html/2607.18316v1#S5.SS5 — 5.5 The Two Failure Modes Respond Oppositely; https://arxiv.org/html/2607.18316v1#S7 — 7 Limitations | Exact v1 links https://github.com/shashank-indukuri/binding-drift, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18316 | complete |
| SF-2026-ARXIV-2607-18336 | RP-4a6bdd1f9d83d1ea | standard | arXiv:2607.18336v1 | SRC-ARXIV@arXiv:2607.18336v1 | https://arxiv.org/html/2607.18336v1#S2 — 2 Methodology; https://arxiv.org/html/2607.18336v1#S2.SS2 — 2.2 Overall Architecture | https://arxiv.org/html/2607.18336v1#S4 — 4 Experimental Results and Analysis; https://arxiv.org/html/2607.18336v1#S3 — 3 Experimental Settings | https://arxiv.org/html/2607.18336v1#S5 — 5 Conclusions and Future Work | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18336 | complete |
| SF-2026-ARXIV-2607-18347 | RP-f8beac28329afb6d | standard | arXiv:2607.18347v1 | SRC-ARXIV@arXiv:2607.18347v1 | https://arxiv.org/html/2607.18347v1#S3.SS1 — 3.1 Design-science approach; https://arxiv.org/html/2607.18347v1#S2.SS1 — 2.1 Agent-facing commerce is a distributed systems problem | https://arxiv.org/html/2607.18347v1#S6 — 6 Evaluation and results; https://arxiv.org/html/2607.18347v1#S6.SS4 — 6.4 Controlled ablation results | https://arxiv.org/html/2607.18347v1#S7.SS4 — 7.4 Limitations and threats to validity; https://arxiv.org/html/2607.18347v1#S3.SS3 — 3.3 Threat model | Exact v1 links https://github.com/dmsfiris/agentic-commerce-blueprint, https://github.com/dmsfiris/agentic-commerce-blueprint/releases/tag/v0.9.2, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18347 | complete |
| SF-2026-ARXIV-2607-18357 | RP-47240309fdd7d0de | deep | arXiv:2607.18357v1 | SRC-ARXIV@arXiv:2607.18357v1 | https://arxiv.org/html/2607.18357v1#S5 — 5. Implementation and Scope | https://arxiv.org/html/2607.18357v1#S6 — 6. Evaluation | https://arxiv.org/html/2607.18357v1#S3.SS1 — 3.1. The failure: negative transfer, not ignorance; https://arxiv.org/html/2607.18357v1#S5.SS4 — 5.4. Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18357 | complete |
| SF-2026-ARXIV-2607-18360 | RP-f2028eda8974a43f | standard | arXiv:2607.18360v1 | SRC-ARXIV@arXiv:2607.18360v1 | https://arxiv.org/html/2607.18360v1#A7 — Appendix G bibtex-updater: the co-designed reference tool | https://arxiv.org/html/2607.18360v1#A2 — Appendix B Evaluation protocol and reproducibility; https://arxiv.org/html/2607.18360v1#A3 — Appendix C Core results and validity | https://arxiv.org/html/2607.18360v1#A4 — Appendix D Failure mode (i): agentic aggregation; https://arxiv.org/html/2607.18360v1#A5 — Appendix E Failure mode (ii): base-rate precision and deployment | Exact v1 links https://pypi.org/project/harcx/, https://github.com/amazon-science/RefChecker, https://github.com/rpatrik96/bibtexupdater; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18360 | complete |
| SF-2026-ARXIV-2607-18366 | RP-7fba4ac90a9935d6 | standard | arXiv:2607.18366v1 | SRC-ARXIV@arXiv:2607.18366v1 | https://arxiv.org/pdf/2607.18366v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.18366v1#page=2 — PDF page 2 | https://arxiv.org/pdf/2607.18366v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.18366v1#page=2 — PDF page 2 | https://arxiv.org/pdf/2607.18366v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.18366v1#page=2 — PDF page 2 | Exact v1 links https://github.com/WooooDyy/LLM-Agent-Paper-List, https://github.com/xiye17/TextualExplInContext, https://github.com/noahshinn024/reflexion; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18366 | complete |
| SF-2026-ARXIV-2607-18367 | RP-0604d4f81d8399f0 | deep | arXiv:2607.18367v1 | SRC-ARXIV@arXiv:2607.18367v1 | https://arxiv.org/html/2607.18367v1#S3.SS2 — 3.2 Bidirectional Model Pre-Training – Establishing the General Video Prior; https://arxiv.org/html/2607.18367v1#S3.SS3 — 3.3 Autoregressive Model Training – Control and Memory Integration | https://arxiv.org/html/2607.18367v1#S4 — 4 Results; https://arxiv.org/html/2607.18367v1#S4.SS1 — 4.1 Experimental Setup | https://arxiv.org/html/2607.18367v1#S5 — 5 Conclusion | Exact v1 links https://github.com/AlayaLab/AlayaWorld, https://github.com/JaidedAI/EasyOCR, https://huggingface.co/moonshotai/Kimi-K2.6; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18367 | complete |
| SF-2026-ARXIV-2607-18445 | RP-6f2065eaf55481ed | standard | arXiv:2607.18445v1 | SRC-ARXIV@arXiv:2607.18445v1 | https://arxiv.org/html/2607.18445v1#A3.SS1 — C.1 Models, Tokenizers, and Hardware; https://arxiv.org/html/2607.18445v1#A5 — Appendix E Reference Detector Implementation | https://arxiv.org/html/2607.18445v1#A1.SS8 — A.8 Supplementary Results: Quality Cost and Self-Healing; https://arxiv.org/html/2607.18445v1#A3 — Appendix C Experimental Protocol and Reproducibility | https://arxiv.org/html/2607.18445v1#A4.SS2 — D.2 FPR Recalibration: SD Recipe and Failure Modes; https://arxiv.org/html/2607.18445v1#S7 — 7 Discussion | Exact v1 links https://digital-strategy.ec.europa.eu/en/library/first-draft-code-practice-transparency-ai-generated-content, https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct, https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18445 | complete |
| SF-2026-ARXIV-2607-18454 | RP-fffb3a99d6508d45 | standard | arXiv:2607.18454v1 | SRC-ARXIV@arXiv:2607.18454v1 | https://arxiv.org/html/2607.18454v1#A6 — Appendix F All Methods Loss by Distributions; https://arxiv.org/html/2607.18454v1#S2.SS2 — 2.2 Sampling Methods | https://arxiv.org/html/2607.18454v1#S5 — 5 Experimental Results; https://arxiv.org/html/2607.18454v1#A4 — Appendix D Experimental and Implementation Details | https://arxiv.org/html/2607.18454v1#S7 — 7 Discussion and Limitations; https://arxiv.org/html/2607.18454v1#S8 — 8 Conclusion | Exact v1 links https://github.com/TransformerLensOrg/TransformerLens, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18454 | complete |
| SF-2026-ARXIV-2607-18476 | RP-a27f0e141c073419 | standard | arXiv:2607.18476v1 | SRC-ARXIV@arXiv:2607.18476v1 | https://arxiv.org/html/2607.18476v1#S3 — 3 Method | https://arxiv.org/html/2607.18476v1#S4 — 4 Results | https://arxiv.org/html/2607.18476v1#S5 — 5 Limitations; https://arxiv.org/html/2607.18476v1#S6 — 6 Discussion | Exact v1 links https://github.com/tap2k/modelun, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18476 | complete |
| SF-2026-ARXIV-2607-18481 | RP-f4cffb2b149ea50a | deep | arXiv:2607.18481v1 | SRC-ARXIV@arXiv:2607.18481v1 | https://arxiv.org/html/2607.18481v1#S4 — 4 Methodology | https://arxiv.org/html/2607.18481v1#S5 — 5 Experiments; https://arxiv.org/html/2607.18481v1#S5.SS2 — 5.2 Main Results | https://arxiv.org/html/2607.18481v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.18481v1#Sx1 — Limitations | Exact v1 links https://doi.org/10.18653/v1/2024.acl-demos.38, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18481 | complete |
| SF-2026-ARXIV-2607-18485 | RP-259724256cd016be | standard | arXiv:2607.18485v1 | SRC-ARXIV@arXiv:2607.18485v1 | https://arxiv.org/html/2607.18485v1#S5.SS1 — 5.1 Shared parallel-filesystem poisoning; https://arxiv.org/html/2607.18485v1#S4 — 4 Threat Model: The Hijacked Authorized Agent | https://arxiv.org/html/2607.18485v1#S7.SS2 — 7.2 Toward a benchmark: TaskBound | https://arxiv.org/html/2607.18485v1#S4 — 4 Threat Model: The Hijacked Authorized Agent; https://arxiv.org/html/2607.18485v1#S8 — 8 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18485 | complete |
| SF-2026-ARXIV-2607-18496 | RP-63320b48777e5d37 | standard | arXiv:2607.18496v1 | SRC-ARXIV@arXiv:2607.18496v1 | https://arxiv.org/html/2607.18496v1#S2 — 2. Data and Methodology | https://arxiv.org/html/2607.18496v1#S3.SS1 — 3.1. Case Study: Impostor Scams; https://arxiv.org/html/2607.18496v1#S3.SS2 — 3.2. Case Study: Identity Theft | https://arxiv.org/html/2607.18496v1#S4 — 4. Failure Modes, Generalizability and Abuse; https://arxiv.org/html/2607.18496v1#S5 — 5. Conclusion and Open Problems | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18496 | complete |
| SF-2026-ARXIV-2607-18508 | RP-cb0d077a9be66033 | standard | arXiv:2607.18508v1 | SRC-ARXIV@arXiv:2607.18508v1 | https://arxiv.org/html/2607.18508v1#A2 — Appendix B Judge and Probe Implementation | https://arxiv.org/html/2607.18508v1#A1 — Appendix A Evaluation Protocol; https://arxiv.org/html/2607.18508v1#S3 — 3. Experimental Setup | https://arxiv.org/html/2607.18508v1#S7 — 7. Conclusion | Exact v1 links https://github.com/jiabingyang01/EmoPrefer-Audit, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18508 | complete |
| SF-2026-ARXIV-2607-18532 | RP-b0620174459daf3c | deep | arXiv:2607.18532v1 | SRC-ARXIV@arXiv:2607.18532v1 | https://arxiv.org/html/2607.18532v1#S3 — 3 Reasoning as a Switching Dynamical System; https://arxiv.org/html/2607.18532v1#S3.SS2 — 3.2 Switching Dynamical System Formulation | https://arxiv.org/html/2607.18532v1#A5 — Appendix E Additional Robustness and Modeling Choice Ablations; https://arxiv.org/html/2607.18532v1#A5.SS4 — E.4 Projection and inference ablations | https://arxiv.org/html/2607.18532v1#S8.SS2 — 8.2 SDS-Guided Pruning of Failure-Prone Prefixes; https://arxiv.org/html/2607.18532v1#S9 — 9 Conclusion | Exact v1 links https://github.com/withmartian/mi-cot, https://github.com/meta-llama/llama3/blob/main/MODEL_CARD.md, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18532 | complete |
| SF-2026-ARXIV-2607-18548 | RP-25c23fb9d99f4185 | standard | arXiv:2607.18548v1 | SRC-ARXIV@arXiv:2607.18548v1 | https://arxiv.org/html/2607.18548v1#S10.SS1 — X-A Emerging Design Patterns; https://arxiv.org/html/2607.18548v1#S10.SS2 — X-B Systemic Failure Modes | https://arxiv.org/html/2607.18548v1#S6 — VI The Evolution of AI Safety Evaluation; https://arxiv.org/html/2607.18548v1#S6.SS1 — VI-A Representation-Level Evaluation | https://arxiv.org/html/2607.18548v1#S10.SS2 — X-B Systemic Failure Modes; https://arxiv.org/html/2607.18548v1#S11.SS2 — XI-B Systemic Failure Modes | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18548 | complete |
| SF-2026-ARXIV-2607-18553 | RP-c6190439c2e55b6e | deep | arXiv:2607.18553v1 | SRC-ARXIV@arXiv:2607.18553v1 | https://arxiv.org/html/2607.18553v1#Sx14.SSx3 — Appendix C — Tap architectures and training details; https://arxiv.org/html/2607.18553v1#Sx5.SSx6 — 4.6 Is the loop necessary? A non-looped architecture control | https://arxiv.org/html/2607.18553v1#Sx1 — Results at a glance; https://arxiv.org/html/2607.18553v1#Sx13.SSx4 — 12.4 The experiment queue, in priority order | https://arxiv.org/html/2607.18553v1#Sx11.SSx1 — 10.1 Controls, failures, and surviving claims; https://arxiv.org/html/2607.18553v1#Sx12 — 11. Limitations | Exact v1 links https://github.com/VykosMolt, https://github.com/VykosMolt/Branching-Looped-Transformer, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18553 | complete |
| SF-2026-ARXIV-2607-18575 | RP-2d1345ed1bc49a41 | standard | arXiv:2607.18575v1 | SRC-ARXIV@arXiv:2607.18575v1 | https://arxiv.org/html/2607.18575v1#S3 — III Design of Receipt Verification; https://arxiv.org/html/2607.18575v1#S3.SS1 — III-A Receipt Architecture | https://arxiv.org/html/2607.18575v1#S5 — V Evaluation; https://arxiv.org/html/2607.18575v1#S5.SS1 — V-A Experiment Setup | https://arxiv.org/html/2607.18575v1#S6 — VI Discussion; https://arxiv.org/html/2607.18575v1#S8 — VIII Conclusion | Exact v1 links https://owasp.org/www-project-benchmark/, https://projectzero.google/2024/10/from-naptime-to-big-sleep.html, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18575 | complete |
| SF-2026-ARXIV-2607-18577 | RP-a6b8074a7672dacc | standard | arXiv:2607.18577v1 | SRC-ARXIV@arXiv:2607.18577v1 | https://arxiv.org/html/2607.18577v1#S3 — 3 Methods; https://arxiv.org/html/2607.18577v1#S3.SS1 — 3.1 Models and Datasets | https://arxiv.org/html/2607.18577v1#S4 — 4 Experiments and Results; https://arxiv.org/html/2607.18577v1#S3.SS2 — 3.2 Evaluation Protocol | https://arxiv.org/html/2607.18577v1#S5 — 5 Discussion and Conclusion; https://arxiv.org/html/2607.18577v1#S4.SS1 — 4.1 Attention Grounding Failure | Exact v1 links https://github.com/thedatasense/medicalvlm_attention_without_grounding, https://huggingface.co/collections/saillab/mechanistically-guided-lora-chil-2026-69ff7afccce7547a00180b2a, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18577 | complete |
| SF-2026-ARXIV-2607-18580 | RP-7096c707e73b3f5f | standard | arXiv:2607.18580v1 | SRC-ARXIV@arXiv:2607.18580v1 | https://arxiv.org/html/2607.18580v1#S4 — 4 Method; https://arxiv.org/html/2607.18580v1#S4.SS1 — 4.1 System 2: Language-to-STL Task Planning | https://arxiv.org/html/2607.18580v1#S5 — 5 Evaluation | https://arxiv.org/html/2607.18580v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.18580v1#S7 — 7 Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18580 | complete |
| SF-2026-ARXIV-2607-18603 | RP-95a8eb8c0dbe16dd | deep | arXiv:2607.18603v1 | SRC-ARXIV@arXiv:2607.18603v1 | https://arxiv.org/html/2607.18603v1#A1.SS2 — A.2 Design Decisions and Implementation Notes; https://arxiv.org/html/2607.18603v1#S6 — 6 Framework Analysis and Discussion | https://arxiv.org/html/2607.18603v1#S5 — 5 Experimental Results; https://arxiv.org/html/2607.18603v1#A1.SS1 — A.1 Claude Sonnet 4.6 Results | https://arxiv.org/html/2607.18603v1#S6.SS4 — 6.4 Limitations and Future Work; https://arxiv.org/html/2607.18603v1#S6 — 6 Framework Analysis and Discussion | Exact v1 links https://github.com/auto-index/autoindex, https://github.com/auto-index/autoindex/blob/main/query_splits.json, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18603 | complete |
| SF-2026-ARXIV-2607-18631 | RP-0b2a7ea5ad59873c | deep | arXiv:2607.18631v1 | SRC-ARXIV@arXiv:2607.18631v1 | https://arxiv.org/html/2607.18631v1#S3 — III Design; https://arxiv.org/html/2607.18631v1#S3.SS2 — III-B Dual-fidelity cost model | https://arxiv.org/html/2607.18631v1#S5 — V Evaluation; https://arxiv.org/html/2607.18631v1#S5.SS5 — V-E RQ5: Ablation and discriminative power | https://arxiv.org/html/2607.18631v1#S6.SS4 — VI-D Limitations and threats to validity; https://arxiv.org/html/2607.18631v1#S6 — VI Discussion | Exact v1 links https://github.com/deepseek-ai/DeepEP, https://github.com/deepseek-ai/DeepGEMM, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18631 | complete |
| SF-2026-ARXIV-2607-18639 | RP-f4c1f7e22b86beca | standard | arXiv:2607.18639v1 | SRC-ARXIV@arXiv:2607.18639v1 | https://arxiv.org/html/2607.18639v1#A5 — Appendix E Cross-Architecture Details; https://arxiv.org/html/2607.18639v1#S2 — 2 Method | https://arxiv.org/html/2607.18639v1#A10 — Appendix J Open-Ended Format: Representation Analysis; https://arxiv.org/html/2607.18639v1#A2 — Appendix B Evaluation Details | https://arxiv.org/html/2607.18639v1#S6 — 6 Discussion; https://arxiv.org/html/2607.18639v1#S7 — 7 Conclusion | Exact v1 links https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro/blob/main/DeepSeek_V4.pdf, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18639 | complete |
| SF-2026-ARXIV-2607-18659 | RP-3d3b91be66ace022 | standard | arXiv:2607.18659v1 | SRC-ARXIV@arXiv:2607.18659v1 | https://arxiv.org/html/2607.18659v1#S4.SS4 — 4.4 Experiment Framework; https://arxiv.org/html/2607.18659v1#S3 — 3 Threat Model and Research Questions | https://arxiv.org/html/2607.18659v1#S5 — 5 Evaluations and Results; https://arxiv.org/html/2607.18659v1#S4 — 4 Experiments Setup | https://arxiv.org/html/2607.18659v1#S3 — 3 Threat Model and Research Questions; https://arxiv.org/html/2607.18659v1#S3.SS1 — 3.1 Threat Model | Exact v1 links https://github.com/browser-use/browser-use, https://github.com/FoundationAgents/OpenManus, https://github.com/nanobrowser/nanobrowser; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18659 | complete |
| SF-2026-ARXIV-2607-18664 | RP-216ef426d413f3ca | deep | arXiv:2607.18664v1 | SRC-ARXIV@arXiv:2607.18664v1 | https://arxiv.org/html/2607.18664v1#S3 — 3 DeforM Framework; https://arxiv.org/html/2607.18664v1#S3.SS4 — 3.4 DeforM-Injection: Training-based Method | https://arxiv.org/html/2607.18664v1#Pt0.A3 — Appendix C Details of Evaluation; https://arxiv.org/html/2607.18664v1#S4 — 4 Experiments | https://arxiv.org/html/2607.18664v1#S5 — 5 Conclusion | Exact v1 links https://nemosunny.github.io/DeforM-ProjectPage/, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18664 | complete |
| SF-2026-ARXIV-2607-18665 | RP-fb07be0c8400d197 | standard | arXiv:2607.18665v1 | SRC-ARXIV@arXiv:2607.18665v1 | https://arxiv.org/html/2607.18665v1#A11.SS2 — K.2 Design Rationale: Decomposition into Executability and Net-New Risk; https://arxiv.org/html/2607.18665v1#A3 — Appendix C Overview of Baseline Methods | https://arxiv.org/html/2607.18665v1#S6 — 6 Experimental Results and Analysis; https://arxiv.org/html/2607.18665v1#A8 — Appendix H More results from the perturbation experiment | https://arxiv.org/html/2607.18665v1#A12 — Appendix L Limitations and Future Work; https://arxiv.org/html/2607.18665v1#A11 — Appendix K Additional Discussion | Exact v1 links https://github.com/bytedance/deer-flow, https://github.com/ScienceOne-AI/S1-DeepResearch, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18665 | complete |
| SF-2026-ARXIV-2607-18673 | RP-e62f750cce5fbb38 | standard | arXiv:2607.18673v1 | SRC-ARXIV@arXiv:2607.18673v1 | https://arxiv.org/html/2607.18673v1#S2 — 2 Methods; https://arxiv.org/html/2607.18673v1#S3.SS2 — 3.2 Results of Object Detection Models | https://arxiv.org/html/2607.18673v1#S2.SS2 — 2.2 Evaluation and Metrics; https://arxiv.org/html/2607.18673v1#S3 — 3 Results | https://arxiv.org/html/2607.18673v1#S4 — 4 Limitations and Furture Work; https://arxiv.org/html/2607.18673v1#S5 — 5 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18673 | complete |
| SF-2026-ARXIV-2607-18684 | RP-1534de0838bf26b8 | standard | arXiv:2607.18684v1 | SRC-ARXIV@arXiv:2607.18684v1 | https://arxiv.org/html/2607.18684v1#S4 — 4 Methodology; https://arxiv.org/html/2607.18684v1#S4.SS1 — 4.1 System Overview | https://arxiv.org/html/2607.18684v1#S6 — 6 Results; https://arxiv.org/html/2607.18684v1#S6.SS1 — 6.1 Main Results | https://arxiv.org/html/2607.18684v1#S7 — 7 Discussion; https://arxiv.org/html/2607.18684v1#S8 — 8 Conclusion | Exact v1 links https://github.com/jayaratned/AutomotiveTD, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18684 | complete |
| SF-2026-ARXIV-2607-18709 | RP-e0e79ab4c188c036 | deep | arXiv:2607.18709v1 | SRC-ARXIV@arXiv:2607.18709v1 | https://arxiv.org/html/2607.18709v1#S4 — 4 Method; https://arxiv.org/html/2607.18709v1#S2.SS2 — 2.2 Embodied reasoning and world modeling for actions. | https://arxiv.org/html/2607.18709v1#S5 — 5 Benchmarking and Experiments; https://arxiv.org/html/2607.18709v1#A1.SS4 — A.4 Additional Qualitative results on RoboInter-VLA | https://arxiv.org/html/2607.18709v1#S6 — 6 Conclusion | Exact v1 links https://github.com/InternRobotics/RoboInter, https://huggingface.co/datasets/InternRobotics/RoboInter-Data, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18709 | complete |
| SF-2026-ARXIV-2607-18711 | RP-d8659c258568d6c3 | standard | arXiv:2607.18711v1 | SRC-ARXIV@arXiv:2607.18711v1 | https://arxiv.org/html/2607.18711v1#A3 — Appendix C Design and Measurement Notes; https://arxiv.org/html/2607.18711v1#S3 — III Methodology | https://arxiv.org/html/2607.18711v1#S5 — V Results and Analysis; https://arxiv.org/html/2607.18711v1#S4 — IV Experimental Setup | https://arxiv.org/html/2607.18711v1#S6 — VI Discussion and Future Work; https://arxiv.org/html/2607.18711v1#S6.SS2 — VI-B Threats to Validity and Limitations | Exact v1 links https://github.com/SecurityLab-UCD/CNTG, https://github.com/SecurityLab-UCD/CGNTG, https://github.com/DaveGamble/cJSON; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18711 | complete |
| SF-2026-ARXIV-2607-18715 | RP-f98685d0c903e176 | deep | arXiv:2607.18715v1 | SRC-ARXIV@arXiv:2607.18715v1 | https://arxiv.org/html/2607.18715v1#S4 — 4 DWM: World/Action Disentanglement for Latent World Models | https://arxiv.org/html/2607.18715v1#S5.SS1 — 5.1 Benchmarks and Experimental Setup; https://arxiv.org/html/2607.18715v1#S5 — 5 Experiments | https://arxiv.org/html/2607.18715v1#S6 — 6 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18715 | complete |
| SF-2026-ARXIV-2607-18722 | RP-437a277f5fb3a7b3 | deep | arXiv:2607.18722v1 | SRC-ARXIV@arXiv:2607.18722v1 | https://arxiv.org/html/2607.18722v1#A5 — Appendix E How Does Each Stability Approach Work in Async RL? | https://arxiv.org/html/2607.18722v1#A6 — Appendix F Experimental Details; https://arxiv.org/html/2607.18722v1#S5 — 5 Experiments | https://arxiv.org/html/2607.18722v1#S6 — 6 Limitations and Open Questions; https://arxiv.org/html/2607.18722v1#S7 — 7 Conclusion | Exact v1 links https://github.com/Tencent-Hunyuan/GradLoc, https://github.com/THUDM/slime, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18722 | complete |
| SF-2026-ARXIV-2607-18754 | RP-a9c28d53d239fbba | deep | arXiv:2607.18754v1 | SRC-ARXIV@arXiv:2607.18754v1 | https://arxiv.org/html/2607.18754v1#A1 — Appendix A System and Prompt Details; https://arxiv.org/html/2607.18754v1#S3 — 3 System Overview | https://arxiv.org/html/2607.18754v1#A3 — Appendix C Evaluation Protocol; https://arxiv.org/html/2607.18754v1#S4 — 4 Evaluation | https://arxiv.org/html/2607.18754v1#A5 — Appendix E Limitations; https://arxiv.org/html/2607.18754v1#S3.SS4 — 3.4 Extensible Failure Taxonomy | Exact v1 links https://github.com/AgentDebugX/AgentDebugX, https://pypi.org/project/agentdebugx/, https://github.com/langfuse/langfuse; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18754 | complete |
| SF-2026-ARXIV-2607-18759 | RP-ba737c699caf501b | standard | arXiv:2607.18759v1 | SRC-ARXIV@arXiv:2607.18759v1 | https://arxiv.org/html/2607.18759v1#S5.SS2 — 5.2 Bridging to a Realistic Architecture | https://arxiv.org/html/2607.18759v1#A5 — Appendix E Experimental Details and Reproducibility; https://arxiv.org/html/2607.18759v1#S4 — 4 An Implicit-Bias Analysis | https://arxiv.org/html/2607.18759v1#S7 — 7 Discussion and Limitations; https://arxiv.org/html/2607.18759v1#S8 — 8 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18759 | complete |
| SF-2026-ARXIV-2607-18785 | RP-f790a63cb60d1949 | standard | arXiv:2607.18785v1 | SRC-ARXIV@arXiv:2607.18785v1 | https://arxiv.org/html/2607.18785v1#Sx1 — Introduction; https://arxiv.org/html/2607.18785v1#Sx2 — Related Work | https://arxiv.org/html/2607.18785v1#Sx3 — Analysis; https://arxiv.org/html/2607.18785v1#Sx5 — Experiments | https://arxiv.org/html/2607.18785v1#Sx6 — Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18785 | complete |
| SF-2026-ARXIV-2607-18802 | RP-ecc9ff7101fcc129 | deep | arXiv:2607.18802v1 | SRC-ARXIV@arXiv:2607.18802v1 | https://arxiv.org/html/2607.18802v1#S3 — III Methodology; https://arxiv.org/html/2607.18802v1#S3.SS4 — III-D On-Device Implementation | https://arxiv.org/html/2607.18802v1#S3.SS3 — III-C Experimental Setup; https://arxiv.org/html/2607.18802v1#S4 — IV Results | https://arxiv.org/html/2607.18802v1#S5 — V Discussion; https://arxiv.org/html/2607.18802v1#S6 — VI Conclusion | Exact v1 links https://github.com/STMicroelectronics/stm32ai-modelzoo, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18802 | complete |
| SF-2026-ARXIV-2607-18816 | RP-faf337ce8659b7f4 | standard | arXiv:2607.18816v1 | SRC-ARXIV@arXiv:2607.18816v1 | https://arxiv.org/html/2607.18816v1#S3 — 3. System Overview | https://arxiv.org/html/2607.18816v1#S1 — 1. Introduction; https://arxiv.org/html/2607.18816v1#S2 — 2. Related Works | https://arxiv.org/html/2607.18816v1#S5 — 5. Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18816 | complete |
| SF-2026-ARXIV-2607-18821 | RP-77e0d3efaaffc264 | standard | arXiv:2607.18821v1 | SRC-ARXIV@arXiv:2607.18821v1 | https://arxiv.org/html/2607.18821v1#S6 — 6 Evaluation Design; https://arxiv.org/html/2607.18821v1#A1.SS6 — A.6 Model Checkpoint Replication | https://arxiv.org/html/2607.18821v1#S6 — 6 Evaluation Design; https://arxiv.org/html/2607.18821v1#S7 — 7 Results | https://arxiv.org/html/2607.18821v1#A1.SS2 — A.2 Future this; https://arxiv.org/html/2607.18821v1#S10 — 10 Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18821 | complete |
| SF-2026-ARXIV-2607-18826 | RP-f8a912dd7e9d96fc | standard | arXiv:2607.18826v1 | SRC-ARXIV@arXiv:2607.18826v1 | https://arxiv.org/html/2607.18826v1#A6 — Appendix F Second Native-Framework Probe: LangGraph Traces; https://arxiv.org/html/2607.18826v1#S3 — 3 Method | https://arxiv.org/html/2607.18826v1#S4.SS2 — 4.2 Experimental Protocol and Main Results; https://arxiv.org/html/2607.18826v1#A3 — Appendix C Supplementary Evaluation Tables | https://arxiv.org/html/2607.18826v1#A7 — Appendix G A 2 FV Qualitative Outcomes and Failure Modes; https://arxiv.org/html/2607.18826v1#S3.SS1 — 3.1 Problem Setup and Threat Model | Exact v1 links https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro, https://huggingface.co/google/gemma-4-31B-it, https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18826 | complete |
| SF-2026-ARXIV-2607-18828 | RP-f84b1d9c87b530ce | standard | arXiv:2607.18828v1 | SRC-ARXIV@arXiv:2607.18828v1 | https://arxiv.org/html/2607.18828v1#Sx1.SSx3 — 2. Methods; https://arxiv.org/html/2607.18828v1#Sx1.SSx12 — Appendix E. Supplementary robustness tables (all four models) | https://arxiv.org/html/2607.18828v1#Sx1.SSx4 — 3. Results | https://arxiv.org/html/2607.18828v1#Sx1.SSx11 — Appendix D. Example failures (open-ended probe); https://arxiv.org/html/2607.18828v1#Sx1.SSx5 — 4. Discussion | Exact v1 links https://github.com/KAVentures/health-ai-readiness-robustness, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18828 | complete |
| SF-2026-ARXIV-2607-18840 | RP-8dd8cf7bdc6a9819 | deep | arXiv:2607.18840v1 | SRC-ARXIV@arXiv:2607.18840v1 | https://arxiv.org/html/2607.18840v1#S3 — 3 Method; https://arxiv.org/html/2607.18840v1#S2.SS1 — 2.1 World Action Models for Robotic Manipulation | https://arxiv.org/html/2607.18840v1#S4.SS1 — 4.1 Benchmark Setup and Evaluation Protocol; https://arxiv.org/html/2607.18840v1#S4.SS3 — 4.3 Simulation Benchmark Results | https://arxiv.org/html/2607.18840v1#S5 — 5 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18840 | complete |
| SF-2026-ARXIV-2607-18847 | RP-e12bdda3262fc812 | deep | arXiv:2607.18847v1 | SRC-ARXIV@arXiv:2607.18847v1 | https://arxiv.org/html/2607.18847v1#S3 — III Methodology; https://arxiv.org/html/2607.18847v1#S3.SS2 — III-B Threat Model | https://arxiv.org/html/2607.18847v1#S4 — IV Evaluation; https://arxiv.org/html/2607.18847v1#S4.SS1 — IV-A Experimental Setup | https://arxiv.org/html/2607.18847v1#S3.SS2 — III-B Threat Model; https://arxiv.org/html/2607.18847v1#S6 — VI Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18847 | complete |
| SF-2026-ARXIV-2607-18859 | RP-93eb521a9d52518b | deep | arXiv:2607.18859v1 | SRC-ARXIV@arXiv:2607.18859v1 | https://arxiv.org/html/2607.18859v1#S2 — II Methods | https://arxiv.org/html/2607.18859v1#S3 — III Experiments; https://arxiv.org/html/2607.18859v1#S3.SS1 — III-A Experimental Settings | https://arxiv.org/html/2607.18859v1#S5 — V Threats to Validity; https://arxiv.org/html/2607.18859v1#S6 — VI Conclusion | Exact v1 links https://github.com/DeepSoftwareAnalytics/PhoenixRepair, https://github.com/SWE-agent/mini-swe-agent, https://github.com/reworkd/AgentGPT; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18859 | complete |
| SF-2026-ARXIV-2607-18867 | RP-78639a5efae5b6ac | standard | arXiv:2607.18867v1 | SRC-ARXIV@arXiv:2607.18867v1 | https://arxiv.org/html/2607.18867v1#S5 — 5 The 15-Model Leaderboard | https://arxiv.org/html/2607.18867v1#S1 — 1 Introduction; https://arxiv.org/html/2607.18867v1#S2 — 2 Related Work | https://arxiv.org/html/2607.18867v1#S9 — 9 Limitations | Exact v1 links https://github.com/Khaozhe/hindsightbench, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18867 | complete |
| SF-2026-ARXIV-2607-18886 | RP-33e9f632fb2f8a6f | deep | arXiv:2607.18886v1 | SRC-ARXIV@arXiv:2607.18886v1 | https://arxiv.org/html/2607.18886v1#S3.SS3 — 3.3. Designer Agent; https://arxiv.org/html/2607.18886v1#S4.SS4 — 4.4. Implementation Details | https://arxiv.org/html/2607.18886v1#S2.SS1 — 2.1. Inadequacy of Existing Benchmarks for Complex Development Scenarios; https://arxiv.org/html/2607.18886v1#S4 — 4. Experimental Setup | https://arxiv.org/html/2607.18886v1#S5.SS4 — 5.4. Threats to Validity; https://arxiv.org/html/2607.18886v1#S6 — 6. discussion | Exact v1 links https://github.com/ISSE-Lab/ISSTA2026-TraceDev, https://github.com/tree-sitter/tree-sitter, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18886 | complete |
| SF-2026-ARXIV-2607-18915 | RP-d9f23bbec02bfca4 | deep | arXiv:2607.18915v1 | SRC-ARXIV@arXiv:2607.18915v1 | https://arxiv.org/html/2607.18915v1#A1 — Appendix A Implementation Details of our method; https://arxiv.org/html/2607.18915v1#S4 — 4 Method: Step-Level Self-Consistency Group Relative Policy Optimization | https://arxiv.org/html/2607.18915v1#A4 — Appendix D Further Analysis: Context-Augmented Data Evaluation; https://arxiv.org/html/2607.18915v1#A6 — Appendix F SSC-GRPO Perfermance in Augmented Benchmarks | https://arxiv.org/html/2607.18915v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.18915v1#Sx1 — Limitations | Exact v1 links https://huggingface.co/datasets/inclusionAI/AReaL-boba-Data, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18915 | complete |
| SF-2026-ARXIV-2607-18917 | RP-f1049c0d8b29e56b | standard | arXiv:2607.18917v1 | SRC-ARXIV@arXiv:2607.18917v1 | https://arxiv.org/html/2607.18917v1#A3 — Appendix C Framework Prompt Templates; https://arxiv.org/html/2607.18917v1#S3 — 3 Method | https://arxiv.org/html/2607.18917v1#S4 — 4 Experiments; https://arxiv.org/html/2607.18917v1#S4.SS1 — 4.1 Experimental Setup | https://arxiv.org/html/2607.18917v1#S5 — 5 Conclusion; https://arxiv.org/html/2607.18917v1#Sx1 — Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18917 | complete |
| SF-2026-ARXIV-2607-18924 | RP-cfcba51e4b62d4db | standard | arXiv:2607.18924v1 | SRC-ARXIV@arXiv:2607.18924v1 | https://arxiv.org/html/2607.18924v1#S4 — 4 Method; https://arxiv.org/html/2607.18924v1#A3 — Appendix S3 Human Evaluation Implementation Details | https://arxiv.org/html/2607.18924v1#A3 — Appendix S3 Human Evaluation Implementation Details; https://arxiv.org/html/2607.18924v1#A4 — Appendix S4 More Experiments | https://arxiv.org/html/2607.18924v1#S6 — 6 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18924 | complete |
| SF-2026-ARXIV-2607-18957 | RP-d5d297952b4361f0 | deep | arXiv:2607.18957v1 | SRC-ARXIV@arXiv:2607.18957v1 | https://arxiv.org/html/2607.18957v1#S3.SS1 — 3.1. System Model; https://arxiv.org/html/2607.18957v1#S3.SS2 — 3.2. Programming Framework and Runtime | https://arxiv.org/html/2607.18957v1#A3 — Appendix C Additional Burst Cold-Start Results; https://arxiv.org/html/2607.18957v1#S2.SS2 — 2.2. Problem Analysis | https://arxiv.org/html/2607.18957v1#S9 — 9. Conclusion | Exact v1 links https://claude.com/product/claude-code, https://github.com/huggingface/safetensors, https://github.com/features/copilot; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18957 | complete |
| SF-2026-ARXIV-2607-18975 | RP-8822c7555b3b9523 | deep | arXiv:2607.18975v1 | SRC-ARXIV@arXiv:2607.18975v1 | https://arxiv.org/html/2607.18975v1#S3.SS2 — 3.2 Framework: Lifecycle Architecture and Interfaces; https://arxiv.org/html/2607.18975v1#S6.SS2 — 6.2 Method: Dual-Loop Framework for Bounded Evolution | https://arxiv.org/html/2607.18975v1#A6.SS2 — F.2 Experimental Configuration; https://arxiv.org/html/2607.18975v1#A8 — Appendix H Evaluation Protocol Details | https://arxiv.org/html/2607.18975v1#S8.SS2 — 8.2 Cross-Module Findings and Limitations; https://arxiv.org/html/2607.18975v1#S9 — 9 Conclusion and Outlook | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18975 | complete |
| SF-2026-ARXIV-2607-18979 | RP-3a93a8b6957fffdb | deep | arXiv:2607.18979v1 | SRC-ARXIV@arXiv:2607.18979v1 | https://arxiv.org/html/2607.18979v1#A2 — Appendix B Evaluation Prompt for Path-subset in Generative Reward Model; https://arxiv.org/html/2607.18979v1#A7 — Appendix G The Use of Large Language Models | https://arxiv.org/html/2607.18979v1#S4.SS2 — 4.2 Main Results Analysis; https://arxiv.org/html/2607.18979v1#A2 — Appendix B Evaluation Prompt for Path-subset in Generative Reward Model | https://arxiv.org/html/2607.18979v1#S5 — 5 Conclusion and Future Work; https://arxiv.org/html/2607.18979v1#Sx1 — Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18979 | complete |
| SF-2026-ARXIV-2607-19022 | RP-343dd3e84c89e525 | standard | arXiv:2607.19022v1 | SRC-ARXIV@arXiv:2607.19022v1 | https://arxiv.org/html/2607.19022v1#S3 — 3. Methodology; https://arxiv.org/html/2607.19022v1#S3.SS1 — 3.1. Theoretical Lens: The IAD Framework | https://arxiv.org/html/2607.19022v1#S4.SS2 — 4.2. Results; https://arxiv.org/html/2607.19022v1#S5.SS2 — 5.2. Results | https://arxiv.org/html/2607.19022v1#S10 — 10. Conclusion; https://arxiv.org/html/2607.19022v1#S8 — 8. Discussion | Exact v1 links https://octoverse.github.com/, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19022 | complete |
| SF-2026-ARXIV-2607-19033 | RP-31261183b9464731 | standard | arXiv:2607.19033v1 | SRC-ARXIV@arXiv:2607.19033v1 | https://arxiv.org/html/2607.19033v1#S2 — 2 Method; https://arxiv.org/html/2607.19033v1#S2.SS2 — 2.2 Model Overview | https://arxiv.org/html/2607.19033v1#S3 — 3 Experiments | https://arxiv.org/html/2607.19033v1#S4 — 4 Conclusion | Exact v1 links https://github.com/nyrahealth/PINT, https://huggingface.co/hexgrad/Kokoro-82M, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19033 | complete |
| SF-2026-ARXIV-2607-19038 | RP-8db8de34d3000b12 | standard | arXiv:2607.19038v1 | SRC-ARXIV@arXiv:2607.19038v1 | https://arxiv.org/html/2607.19038v1#S4 — 4 Methodology | https://arxiv.org/html/2607.19038v1#S11 — 11 Human Evaluation Protocol; https://arxiv.org/html/2607.19038v1#S5 — 5 Evaluation | https://arxiv.org/html/2607.19038v1#S12.SS1 — 12.1 Limitations and Future Work; https://arxiv.org/html/2607.19038v1#S12 — 12 Discussion | Exact v1 links https://github.com/HBAI-Ltd/Toonflow-app, https://github.com/HITsz-TMG/VideoClaw, https://github.com/HaoTone-monster/N2FBaseline; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19038 | complete |
| SF-2026-ARXIV-2607-19058 | RP-7848f4e48a9b7ca1 | deep | arXiv:2607.19058v1 | SRC-ARXIV@arXiv:2607.19058v1 | https://arxiv.org/html/2607.19058v1#S3.SS0.SSS0.Px4 — Memory model.; https://arxiv.org/html/2607.19058v1#S4.SS0.SSS0.Px1 — Model. | https://arxiv.org/html/2607.19058v1#A4 — Appendix D Zero-shot evaluation detail; https://arxiv.org/html/2607.19058v1#S4 — 4 Experimental setup | https://arxiv.org/html/2607.19058v1#S6 — 6 Limitations; https://arxiv.org/html/2607.19058v1#S7 — 7 Conclusion | Exact v1 links https://github.com/EleutherAI/lm-evaluation-harness, https://github.com/nuemaan/skewadam, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19058 | complete |
| SF-2026-ARXIV-2607-19096 | RP-87b408cd043a3d86 | standard | arXiv:2607.19096v1 | SRC-ARXIV@arXiv:2607.19096v1 | https://arxiv.org/html/2607.19096v1#S3 — 3 System Design; https://arxiv.org/html/2607.19096v1#A1 — Appendix A Methodology details | https://arxiv.org/html/2607.19096v1#A4.SS1 — D.1 Benchmark fixture sizes; https://arxiv.org/html/2607.19096v1#A4.SS4 — D.4 Existing-output error-analysis frame | https://arxiv.org/html/2607.19096v1#A4.SS5 — D.5 Vector-store and synthesis-probe limitations; https://arxiv.org/html/2607.19096v1#S4.SS9 — 4.9 Threat from benchmark contamination | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19096 | complete |
| SF-2026-ARXIV-2607-19102 | RP-8f96a023b9a99d0a | deep | arXiv:2607.19102v1 | SRC-ARXIV@arXiv:2607.19102v1 | https://arxiv.org/html/2607.19102v1#S3 — 3. Contrast Design | https://arxiv.org/html/2607.19102v1#S5 — 5. Trace Comparison Benchmark; https://arxiv.org/html/2607.19102v1#S6 — 6. Evaluation | https://arxiv.org/html/2607.19102v1#S8 — 8. Discussion; https://arxiv.org/html/2607.19102v1#S9 — 9. Conclusions | Exact v1 links https://github.com/jaegertracing/jaeger/issues/6814, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19102 | complete |
| SF-2026-ARXIV-2607-19139 | RP-ea206ea532b98c83 | standard | arXiv:2607.19139v1 | SRC-ARXIV@arXiv:2607.19139v1 | https://arxiv.org/html/2607.19139v1#S10.SS3 — 10.3 Extending the Analysis to Distilled and Edit Models; https://arxiv.org/html/2607.19139v1#S2.SS1 — 2.1 Attention Sinks in Generative Models | https://arxiv.org/html/2607.19139v1#S10 — 10 Extended Experiments; https://arxiv.org/html/2607.19139v1#S10.SS1 — 10.1 Extending the Analysis to FLUX.2 | https://arxiv.org/html/2607.19139v1#S5 — 5 Discussion and Conclusion; https://arxiv.org/html/2607.19139v1#S6 — 6 Limitations and Future Work | Exact v1 links https://github.com/Met4physics/DiT-Interpretability, https://github.com/black-forest-labs/flux, https://github.com/modelscope/DiffSynth-Studio; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19139 | complete |
| SF-2026-ARXIV-2607-19182 | RP-988eba3f99c3f0f7 | deep | arXiv:2607.19182v1 | SRC-ARXIV@arXiv:2607.19182v1 | https://arxiv.org/html/2607.19182v1#S2.SS3 — II-C Why OpenTelemetry Changes the Design Space; https://arxiv.org/html/2607.19182v1#S4 — IV ARBITER Control Architecture | https://arxiv.org/html/2607.19182v1#S8 — VIII Evaluation Results; https://arxiv.org/html/2607.19182v1#S7 — VII Evaluation Methodology | https://arxiv.org/html/2607.19182v1#S11 — XI Conclusion | Exact v1 links https://github.com/pooyan/arbiter, https://github.com/kubernetes/perf-tests/tree/master/clusterloader2, https://github.com/kubernetes-sigs/descheduler; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19182 | complete |
| SF-2026-ARXIV-2607-19190 | RP-1bf7211636841ae4 | deep | arXiv:2607.19190v1 | SRC-ARXIV@arXiv:2607.19190v1 | https://arxiv.org/html/2607.19190v1#S3 — 3 Method; https://arxiv.org/html/2607.19190v1#S3.SS1 — 3.1 System Overview | https://arxiv.org/html/2607.19190v1#S4 — 4 Experiments; https://arxiv.org/html/2607.19190v1#S4.SS1 — 4.1 Evaluation Metric | https://arxiv.org/html/2607.19190v1#S5 — 5 Conclusions, Limitations and Future Work | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19190 | complete |
| SF-2026-ARXIV-2607-19191 | RP-b32c842100ce8179 | deep | arXiv:2607.19191v1 | SRC-ARXIV@arXiv:2607.19191v1 | https://arxiv.org/html/2607.19191v1#S4.SS4 — 4.4 Full-Stack Co-Design for Real-Time World Rollout | https://arxiv.org/html/2607.19191v1#S5 — 5 Evaluation; https://arxiv.org/html/2607.19191v1#S5.SS1 — 5.1 WorldRoamBench Evaluation | https://arxiv.org/html/2607.19191v1#S6 — 6 Discussion and Future Work; https://arxiv.org/html/2607.19191v1#S7 — 7 Conclusion | Exact v1 links https://github.com/amap-cvlab/ABot-World, https://github.com/madebyollin/taehv, https://github.com/lllyasviel/FramePack; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19191 | complete |
| SF-2026-ARXIV-2607-19194 | RP-40e2bc04d3303d03 | standard | arXiv:2607.19194v1 | SRC-ARXIV@arXiv:2607.19194v1 | https://arxiv.org/html/2607.19194v1#S3 — 3 Method | https://arxiv.org/html/2607.19194v1#S4.SS6 — 4.6 Ablation Studies and Sensitivity Analysis; https://arxiv.org/html/2607.19194v1#S4 — 4 Experiments | https://arxiv.org/html/2607.19194v1#S4.SS5 — 4.5 Long-Tail Robustness and Failure Analysis; https://arxiv.org/html/2607.19194v1#S5 — 5 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19194 | complete |
| SF-2026-ARXIV-2607-19214 | RP-23e1116a39b0d0d0 | deep | arXiv:2607.19214v1 | SRC-ARXIV@arXiv:2607.19214v1 | https://arxiv.org/html/2607.19214v1#S4 — 4 Method | https://arxiv.org/html/2607.19214v1#S5 — 5 Results | https://arxiv.org/html/2607.19214v1#S6 — 6 Discussion: rational adoption, and the provider response it forces; https://arxiv.org/html/2607.19214v1#S7 — 7 Threats to validity | Exact v1 links https://github.com/Aider-AI/aider/blob/main/HISTORY.md, https://github.com/yujiachen-y/claude-code-cache-keepalive, https://github.com/openclaw/openclaw/issues/62475; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19214 | complete |
| SF-2026-ARXIV-2607-19215 | RP-71b9de6915e01004 | deep | arXiv:2607.19215v1 | SRC-ARXIV@arXiv:2607.19215v1 | https://arxiv.org/html/2607.19215v1#A4 — Appendix D Algorithms and Baselines; https://arxiv.org/html/2607.19215v1#A4.SS1 — D.1 HACO Algorithm | https://arxiv.org/html/2607.19215v1#S4.SS2 — 4.2 Experimental Results; https://arxiv.org/html/2607.19215v1#A3 — Appendix C Experimental Setup Details | https://arxiv.org/html/2607.19215v1#A6 — Appendix F Limitations; https://arxiv.org/html/2607.19215v1#S5 — 5 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19215 | complete |
| SF-2026-ARXIV-2607-19243 | RP-ed9acee7b1617869 | standard | arXiv:2607.19243v1 | SRC-ARXIV@arXiv:2607.19243v1 | https://arxiv.org/html/2607.19243v1#A4.SS1 — D.1 System prompt; https://arxiv.org/html/2607.19243v1#A6 — Appendix F Intervention implementation details | https://arxiv.org/html/2607.19243v1#A2.SS1 — B.1 Multilingual factual benchmark curation; https://arxiv.org/html/2607.19243v1#A3.SS2 — C.2 Evaluation pipeline | https://arxiv.org/html/2607.19243v1#S9 — 9 Conclusion and Future work; https://arxiv.org/html/2607.19243v1#S10 — 10 Limitations | Exact v1 links https://github.com/alexandermanev/cross-lingual-llm-consistency, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19243 | complete |
| SF-2026-ARXIV-2607-19257 | RP-a6bd48c305526edb | standard | arXiv:2607.19257v1 | SRC-ARXIV@arXiv:2607.19257v1 | https://arxiv.org/html/2607.19257v1#S4.SS1 — 4.1 Design; https://arxiv.org/html/2607.19257v1#S5.SS1 — 5.1 Design | https://arxiv.org/html/2607.19257v1#S2.SS5 — 2.5 Synthetic, Contamination-Free Hallucination Benchmarks; https://arxiv.org/html/2607.19257v1#S4 — 4 Experiment 1: Instruction-Following Decay | https://arxiv.org/html/2607.19257v1#S10 — 10 Future Work; https://arxiv.org/html/2607.19257v1#S11 — 11 Conclusion | Exact v1 links https://github.com/iNetanel/veyrabench, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19257 | complete |
| SF-2026-ARXIV-2607-19262 | RP-3f1470f104517f03 | standard | arXiv:2607.19262v1 | SRC-ARXIV@arXiv:2607.19262v1 | https://arxiv.org/html/2607.19262v1#S5 — Methods; https://arxiv.org/html/2607.19262v1#S3.SS1 — No model–harness pairing exceeds 50% mean pass rate | https://arxiv.org/html/2607.19262v1#S2 — Benchmark construction; https://arxiv.org/html/2607.19262v1#S2.SS1 — Evaluation inventory | https://arxiv.org/html/2607.19262v1#S3.SS3 — Failure patterns are consistent across configurations; https://arxiv.org/html/2607.19262v1#S4 — Discussion | Exact v1 links https://github.com/latchbio/biosecbench-surveillance, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19262 | complete |
| SF-2026-ARXIV-2607-19267 | RP-af350e3c7e5dfaac | standard | arXiv:2607.19267v1 | SRC-ARXIV@arXiv:2607.19267v1 | https://arxiv.org/html/2607.19267v1#S3 — 3 Methods; https://arxiv.org/html/2607.19267v1#S2 — 2 Threat model | https://arxiv.org/html/2607.19267v1#S4 — 4 Results | https://arxiv.org/html/2607.19267v1#S2 — 2 Threat model; https://arxiv.org/html/2607.19267v1#S5 — 5 Discussion | Exact v1 links https://github.com/senthex-security/senthex-research, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19267 | complete |
| SF-2026-ARXIV-2607-19292 | RP-d955949e6e758c89 | standard | arXiv:2607.19292v1 | SRC-ARXIV@arXiv:2607.19292v1 | https://arxiv.org/html/2607.19292v1#S3.SS5 — 3.5. Ecosystem Integrity: Synthetic Evidence Pollution and the Erosion of Collective Error Correction | https://arxiv.org/html/2607.19292v1#S3.SS4 — 3.4. Organizational Integrity: Evaluation Deception, Fictional Oversight, and Diffused Accountability | https://arxiv.org/html/2607.19292v1#S2 — 2. From Bad Outputs to Integrity Failures; https://arxiv.org/html/2607.19292v1#S7 — 7. Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19292 | complete |
| SF-2026-ARXIV-2607-19297 | RP-2a123cd867fab375 | deep | arXiv:2607.19297v1 | SRC-ARXIV@arXiv:2607.19297v1 | https://arxiv.org/html/2607.19297v1#S3 — 3 Recipe 1: SQL Analytics with Repair Loops; https://arxiv.org/html/2607.19297v1#S5 — 5 Recipe 3: HITL Policy Review | https://arxiv.org/html/2607.19297v1#S7 — 7 Cross-Recipe Comparison; https://arxiv.org/html/2607.19297v1#S8 — 8 Failure Modes and Testing | https://arxiv.org/html/2607.19297v1#S9.SS2 — 9.2 Limitations; https://arxiv.org/html/2607.19297v1#S10 — 10 Conclusion | Exact v1 links https://github.com/langchain-ai/langgraph, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19297 | complete |
| SF-2026-ARXIV-2607-19301 | RP-d331a6b1dbdaaa76 | deep | arXiv:2607.19301v1 | SRC-ARXIV@arXiv:2607.19301v1 | https://arxiv.org/html/2607.19301v1#Sx1 — Introduction; https://arxiv.org/html/2607.19301v1#Sx2 — Related Work | https://arxiv.org/html/2607.19301v1#Sx4 — Evaluation; https://arxiv.org/html/2607.19301v1#Sx4.SSx1 — Experimental Setup | https://arxiv.org/html/2607.19301v1#Sx5 — Conclusion | Exact v1 links https://github.com/CXY0112/PAGE-RAG, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19301 | complete |
| SF-2026-ARXIV-2607-19317 | RP-1227a2c232b99e56 | standard | arXiv:2607.19317v1 | SRC-ARXIV@arXiv:2607.19317v1 | https://arxiv.org/html/2607.19317v1#S3 — 3 Architecture; https://arxiv.org/html/2607.19317v1#S11.SS1 — 11.1 Algorithm Validation on IOI (Node Level) | https://arxiv.org/html/2607.19317v1#A1 — Appendix A Experimental Protocols; https://arxiv.org/html/2607.19317v1#S6 — 6 Faithfulness Evaluation | https://arxiv.org/html/2607.19317v1#S12 — 12 Conclusion; https://arxiv.org/html/2607.19317v1#S13 — 13 Limitations, Ethics, and Broader Impact | Exact v1 links https://github.com/Lexsi-Labs/CircuitKIT, https://github.com/TransformerLensOrg/TransformerLens, https://github.com/UFO-101/auto-circuit; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19317 | complete |
| SF-2026-ARXIV-2607-19322 | RP-e8246b882565f675 | standard | arXiv:2607.19322v1 | SRC-ARXIV@arXiv:2607.19322v1 | https://arxiv.org/html/2607.19322v1#S3 — 3 A Two-Level Meta-Rubric Framework for Evaluating Open-Ended Generation; https://arxiv.org/html/2607.19322v1#S5 — 5 Evaluating Models on Gamut | https://arxiv.org/html/2607.19322v1#S2.SS1 — 2.1 Long-Form Factuality Evaluation; https://arxiv.org/html/2607.19322v1#S2.SS2 — 2.2 Rubric-Based Evaluation | https://arxiv.org/html/2607.19322v1#S7 — 7 Conclusion | Exact v1 links https://github.com/facebookresearch/GAMUT, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19322 | complete |
| SF-2026-ARXIV-2607-19326 | RP-33315fcc2f69435b | standard | arXiv:2607.19326v1 | SRC-ARXIV@arXiv:2607.19326v1 | https://arxiv.org/html/2607.19326v1#A1 — Appendix A System overview; https://arxiv.org/html/2607.19326v1#A9 — Appendix I MaRA architecture details | https://arxiv.org/html/2607.19326v1#A9.SS2 — I.2 Architecture ablation (full analysis); https://arxiv.org/html/2607.19326v1#A7 — Appendix G State-usage probe: per-cell results | https://arxiv.org/html/2607.19326v1#A6 — Appendix F Modulation by token role: extended discussion; https://arxiv.org/html/2607.19326v1#S6 — 6 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19326 | complete |
| SF-2026-ARXIV-2607-19336 | RP-e312b0365993429c | standard | arXiv:2607.19336v1 | SRC-ARXIV@arXiv:2607.19336v1 | https://arxiv.org/html/2607.19336v1#S3.SS1 — 3.1. Agentic Systems: History and Definitions | https://arxiv.org/html/2607.19336v1#S3.SS4 — 3.4. Evaluation Beyond Benchmarks | https://arxiv.org/html/2607.19336v1#S1 — 1. Tutorial Description; https://arxiv.org/html/2607.19336v1#S2 — 2. Expected Audience Takeaways | Exact v1 links https://aclanthology.org/2024.emnlp-demo.8.pdf, https://aclanthology.org/2023.acl-demo.11.pdf, https://aclanthology.org/2024.emnlp-demo.8/; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19336 | complete |
| SF-2026-ARXIV-2607-19338 | RP-b7267b31c97a5407 | deep | arXiv:2607.19338v1 | SRC-ARXIV@arXiv:2607.19338v1 | https://arxiv.org/html/2607.19338v1#S3 — 3 Method; https://arxiv.org/html/2607.19338v1#A3 — Appendix C Cross-Model Generalization: Gemini | https://arxiv.org/html/2607.19338v1#A4 — Appendix D Per-Benchmark CRC Frontiers: TACO Difficulty Ladder; https://arxiv.org/html/2607.19338v1#S5 — 5 Experiments | https://arxiv.org/html/2607.19338v1#S6 — 6 Conclusion | Exact v1 links https://github.com/Qijia-He/agent-budget-control, https://openai.com/index/introducing-codex/, https://huggingface.co/Qwen/Qwen3.5-4B; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19338 | complete |
| SF-2026-ARXIV-2607-19339 | RP-a760e3c1248ad79d | deep | arXiv:2607.19339v1 | SRC-ARXIV@arXiv:2607.19339v1 | https://arxiv.org/html/2607.19339v1#A2.SS4 — B.4 MCQ design and text-only guessability filter; https://arxiv.org/html/2607.19339v1#S3 — 3 Method | https://arxiv.org/html/2607.19339v1#S4 — 4 Experiments; https://arxiv.org/html/2607.19339v1#S4.SS2 — 4.2 Main Results | https://arxiv.org/html/2607.19339v1#S5 — 5 Conclusion; https://arxiv.org/html/2607.19339v1#Sx1 — Limitations | Exact v1 links https://github.com/RockyChen0205/OmniReasoner, https://huggingface.co/datasets/HuggingFaceFV/finevideo, https://github.com/huggingface/trl; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19339 | complete |
| SF-2026-ARXIV-2607-19343 | RP-baa52a073ad68acd | deep | arXiv:2607.19343v1 | SRC-ARXIV@arXiv:2607.19343v1 | https://arxiv.org/html/2607.19343v1#A5.SS1 — E.1 Gemini system prompt; https://arxiv.org/html/2607.19343v1#S4 — 4 Method | https://arxiv.org/html/2607.19343v1#A3 — Appendix C Full quantitative results; https://arxiv.org/html/2607.19343v1#A5 — Appendix E VLM Evaluation Protocol | https://arxiv.org/html/2607.19343v1#S6 — 6 Discussion and Conclusions | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19343 | complete |
| SF-2026-ARXIV-2607-19344 | RP-ad79b0b931d0714f | deep | arXiv:2607.19344v1 | SRC-ARXIV@arXiv:2607.19344v1 | https://arxiv.org/html/2607.19344v1#Pt0.A1.SS4 — 0.A.4 Architecture; https://arxiv.org/html/2607.19344v1#S3 — 3 Method | https://arxiv.org/html/2607.19344v1#S5 — 5 Experiments & Results; https://arxiv.org/html/2607.19344v1#Pt0.A3 — Appendix 0.C Ablations | https://arxiv.org/html/2607.19344v1#Pt0.A6 — Appendix 0.F Limitation & Discussion with Future Works; https://arxiv.org/html/2607.19344v1#S6 — 6 Conclusion | Exact v1 links https://github.com/black-forest-labs/flux, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19344 | complete |
| SF-2026-ARXIV-2607-19345 | RP-3e7acb8d73f43209 | deep | arXiv:2607.19345v1 | SRC-ARXIV@arXiv:2607.19345v1 | https://arxiv.org/html/2607.19345v1#S4.SS1 — 4.1 Reward Design; https://arxiv.org/html/2607.19345v1#A1.SS1 — A.1 Repetitive Copying across Models | https://arxiv.org/html/2607.19345v1#A1.SS4 — A.4 Detailed Results for Section 3.3; https://arxiv.org/html/2607.19345v1#S3.SS1 — 3.1 Experimental Setup | https://arxiv.org/html/2607.19345v1#S6 — 6 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-19345 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2607-18240:start -->
### Calibrated Selective Fact-Checking via Evidence Chain Evaluation

<!-- claim:SF-2026-ARXIV-2607-18240:start -->Large language models (LLMs) can achieve strong fact-checking accuracy, yet forced binary decisions conceal a critical reliability problem: systems may issue confident verdicts even when supporting evidence is weak, sparse, or internally inconsistent. We address this issue through Evidence Chain Evaluation (ECE), a selective fact-checking framework that permits abstention via an uncertain verdict instead of requiring a true/false decision for every claim. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18240:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language models (LLMs) can achieve strong fact-checking accuracy, yet forced binary decisions conceal a critical reliability problem: systems may issue confident verdicts even when supporting evidence is weak, sparse, or internally inconsistent.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We address this issue through Evidence Chain Evaluation (ECE), a selective fact-checking framework that permits abstention via an uncertain verdict instead of requiring a true/false decision for every claim.

**证据证明什么。** On ECE-Bench, ECE achieves 91.6% standard accuracy, 93.7% coverage, and 97.8% selective accuracy on answered claims.

**证据没有证明什么。** 6.2 Limitations • Search remains stronger overall : the Search baseline achieves higher standard accuracy and better ECE, Brier, and AURC values than ECE. • Source levels are system-generated : source-level labels are assigned during inference rather than coming from benchmark annotation, so they should be treated as analysis metadata rather than ground truth. • Small benchmark : ECE-Bench contains only 95 claims, which limits statistical power and domain coverage. • Implementation scope : the evaluated system is a tool-routed agent, not a fully implemented dense retriever, reranker, or evidence-graph pipeline. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18240v1#S4 — 4 Method: Evidence Chain Evaluation as Implemented。Evaluation：https://arxiv.org/html/2607.18240v1#S4 — 4 Method: Evidence Chain Evaluation as Implemented; https://arxiv.org/html/2607.18240v1#S5 — 5 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.18240v1#S6 — 6 Discussion; https://arxiv.org/html/2607.18240v1#S6.SS2 — 6.2 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/cheshireyang/ECE.git, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：6.2 Limitations • Search remains stronger overall : the Search baseline achieves higher standard accuracy and better ECE, Brier, and AURC values than ECE. • Source levels are system-generated : source-level labels are assigned during inference rather than coming from benchmark annotation, so they should be treated as analysis metadata rather than ground truth. • Small benchmark : ECE-Bench contains only 95 claims, which limits statistical power and domain coverage. • Implementation scope : the evaluated system is a tool-routed agent, not a fully implemented dense retriever, reranker, or evidence-graph pipeline.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18240:end -->

<!-- review:SF-2026-ARXIV-2607-18241:start -->
### BatchDAG: LLM-Planned Execution Graphs for Scalable Ad-Hoc Analysis Over Enterprise Data

<!-- claim:SF-2026-ARXIV-2607-18241:start -->Large language models (LLMs) excel at analyzing individual documents but break down on exhaustive, cross-entity analytical questions over enterprise-scale datasets due to context overflow, loss of per-entity attribution, and linear latency from sequential tool calls. We present BatchDAG, a system in which an LLM generates a typed directed acyclic graph (DAG) of operations -- SQL queries, semantic searches, in-memory transforms, parallel fan-outs, and single-shot analyses -- which a deterministic engine evaluates with topological-wave parallelism and structured JSON data flow. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18241:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language models (LLMs) excel at analyzing individual documents but break down on exhaustive, cross-entity analytical questions over enterprise-scale datasets due to context overflow, loss of per-entity attribution, and linear latency from sequential tool calls.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We present BatchDAG, a system in which an LLM generates a typed directed acyclic graph (DAG) of operations -- SQL queries, semantic searches, in-memory transforms, parallel fan-outs, and single-shot analyses -- which a deterministic engine evaluates with topological-wave parallelism and structured JSON data flow.

**证据证明什么。** A controlled ablation shows structured JSON intermediates reduce hallucinations by 27% versus prose summaries (paired t-test, p=0.107, n=12).

**证据没有证明什么。** 8 Limitations and Future Work BatchDAG has several limitations. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18241v1#S3 — 3 System Design; https://arxiv.org/html/2607.18241v1#S3.SS1 — 3.1 Architecture Overview。Evaluation：https://arxiv.org/html/2607.18241v1#S6 — 6 Empirical Evaluation; https://arxiv.org/html/2607.18241v1#S6.SS3 — 6.3 Comparative Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.18241v1#S8 — 8 Limitations and Future Work; https://arxiv.org/html/2607.18241v1#S6.SS6 — 6.6 Discussion。

**Artifact boundary。** Exact v1 links https://github.com/langchain-ai/langchain, https://github.com/run-llama/llama_index, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：8 Limitations and Future Work BatchDAG has several limitations.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-WORKFLOW`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18241:end -->

<!-- review:SF-2026-ARXIV-2607-18242:start -->
### AI Tool Discovery at Scale: All You Need is DNS

<!-- claim:SF-2026-ARXIV-2607-18242:start -->The coming era of autonomous AI agents demands a discovery mechanism capable of navigating millions of tools, yet existing solutions buckle under O(N) complexity and centralized governance. Instead of building another fragile overlay, we propose ToolDNS, a radical framework that retrofits semantic tool discovery onto the Internet's most resilient substrate: the Domain Name System (DNS). 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18242:end -->

**为什么进入候选分母。** 摘要首要问题为“The coming era of autonomous AI agents demands a discovery mechanism capable of navigating millions of tools, yet existing solutions buckle under O(N) complexity and centralized governance.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** Instead of building another fragile overlay, we propose ToolDNS, a radical framework that retrofits semantic tool discovery onto the Internet's most resilient substrate: the Domain Name System (DNS).

**证据证明什么。** Furthermore, its UDP-native design reduces discovery latency by orders of magnitude compared to HTTP-based registries.

**证据没有证明什么。** However, these additions bring significant implementation and maintenance complexity, and many of them still rely on a global index at their core, inheriting the same scaling limitations as vector-based retrieval. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18242v1#S3 — 3. ToolDNS System Design; https://arxiv.org/html/2607.18242v1#S3.SS4 — 3.4. Iterative Resolution Algorithm。Evaluation：https://arxiv.org/html/2607.18242v1#S5 — 5. Experiments; https://arxiv.org/html/2607.18242v1#S5.SS4 — 5.4. Comparative Evaluation of Network Efficiency。Limitations / counterevidence：https://arxiv.org/html/2607.18242v1#S2.SS2 — 2.2. Limitations of Existing Paradigms; https://arxiv.org/html/2607.18242v1#S6 — 6. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/hku-icl/ToolDNS.git, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：However, these additions bring significant implementation and maintenance complexity, and many of them still rely on a global index at their core, inheriting the same scaling limitations as vector-based retrieval.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MCP`；evidence-stage relation：`structural_candidate`。
- Books 候选路由（尚非最终决定）：`Structural Candidate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18242:end -->

<!-- review:SF-2026-ARXIV-2607-18243:start -->
### From Agent Failure Paths to Quantified Residual Risk: A Compositional Framework for Resilient Agentic AI

<!-- claim:SF-2026-ARXIV-2607-18243:start -->Agentic AI is crossing trust boundaries faster than current risk models can represent. Existing approaches provide one of two partial views. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18243:end -->

**为什么进入候选分母。** 摘要首要问题为“Agentic AI is crossing trust boundaries faster than current risk models can represent.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** We formalize structural composability linking valid failure paths to well-defined risk instances and show the framework on two contrasting scenarios a hard real-time warehouse robot and a governance-instrumented financial-services agent.

**证据证明什么。** We formalize structural composability linking valid failure paths to well-defined risk instances and show the framework on two contrasting scenarios a hard real-time warehouse robot and a governance-instrumented financial-services agent.

**证据没有证明什么。** Domain transfer occurs through instantiation of nodes, edges, and path content, not by changing the layer grammar itself. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18243v1#S3 — III System and Threat Model; https://arxiv.org/html/2607.18243v1#S4 — IV Proposed Method。Evaluation：https://arxiv.org/html/2607.18243v1#S5 — V Performance Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.18243v1#S3 — III System and Threat Model; https://arxiv.org/html/2607.18243v1#S4.SS1 — IV-A CPSAINT : Structural Failure Decomposition。

**Artifact boundary。** Exact v1 links https://github.com/coderhard/friesa-k-DSN-crai2026, https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Domain transfer occurs through instantiation of nodes, edges, and path content, not by changing the layer grammar itself.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18243:end -->

<!-- review:SF-2026-ARXIV-2607-18246:start -->
### Phionyx: A Deterministic AI Runtime Architecture with Structured State Management and Pre-Response Governance

<!-- claim:SF-2026-ARXIV-2607-18246:start -->We present Phionyx, a deterministic AI runtime architecture derived from the broader Echoism interaction framework that introduces a governance-first approach to AI engineering: treating large language model (LLM) outputs as noisy sensor measurements rather than direct decisions. Unlike probabilistic agents, Phionyx enforces deterministic state evolution via a structured state vector governed by deterministic state-evolution equations, enabling reproducible behavior in applications requiring auditability and governance. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18246:end -->

**为什么进入候选分母。** 摘要首要问题为“We present Phionyx, a deterministic AI runtime architecture derived from the broader Echoism interaction framework that introduces a governance-first approach to AI engineering: treating large language model (LLM) outputs as noisy sensor measurements rather than direct decisions.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We present Phionyx, a deterministic AI runtime architecture derived from the broader Echoism interaction framework that introduces a governance-first approach to AI engineering: treating large language model (LLM) outputs as noisy sensor measurements rather than direct decisions.

**证据证明什么。** Experimental validation on single-instance deployments demonstrates approximately 31% reduction in computational overhead vs. post-hoc filtering (at 30% unsafe input ratio, simulated cost model) and up to 24% improvement in high-value data retention vs.

**证据没有证明什么。** All tests use controlled fixtures, not live traffic. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18246v1#A3.SS1 — C.1 Determinism Verification Methodology; https://arxiv.org/html/2607.18246v1#S2.SS1 — 2.1 Deterministic AI Systems。Evaluation：https://arxiv.org/html/2607.18246v1#A3 — Appendix C Experimental Evidence and Reproducibility; https://arxiv.org/html/2607.18246v1#A3.SS4 — C.4 Failure Injection Results。Limitations / counterevidence：https://arxiv.org/html/2607.18246v1#A3.SS4 — C.4 Failure Injection Results; https://arxiv.org/html/2607.18246v1#S4.SS4 — 4.4 Failure Classification and Recovery。

**Artifact boundary。** Exact v1 links https://github.com/halvrenofviryel/phionyx-research, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：All tests use controlled fixtures, not live traffic.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-PLATFORM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18246:end -->

<!-- review:SF-2026-ARXIV-2607-18253:start -->
### Beyond Accuracy and Cost: Latency-Aware LLM Query Routing for Dynamic Workloads

<!-- claim:SF-2026-ARXIV-2607-18253:start -->Modern language query routers improve inference efficiency by assigning each query to a model that balances response quality and monetary cost. However, current query routers are largely latency-agnostic and do not consider the generation latency experienced by queries at model instances. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18253:end -->

**为什么进入候选分母。** 摘要首要问题为“Modern language query routers improve inference efficiency by assigning each query to a model that balances response quality and monetary cost.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** We design a lightweight latency estimator that simulates autoregressive token batch processing in the serving framework and estimates the time-to-first-token (TTFT) of queries.

**证据证明什么。** Our experimental results indicate that this joint optimization yields up to 40% improvement in accuracy--cost utility while maintaining the same latencies as standard load-balancing approaches.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18253v1#S2 — 2 Background on LLM serving frameworks; https://arxiv.org/html/2607.18253v1#S4.SS1 — 4.1 Serving Framework Simulation (SFS) for latency estimation。Evaluation：https://arxiv.org/html/2607.18253v1#A7 — Appendix G Additional Experimental Results; https://arxiv.org/html/2607.18253v1#A4 — Appendix D Response Evaluation using LLM-as-a-judge。Limitations / counterevidence：https://arxiv.org/html/2607.18253v1#S1 — 1 Introduction; https://arxiv.org/html/2607.18253v1#S2 — 2 Background on LLM serving frameworks。

**Artifact boundary。** Exact v1 links https://github.com/tatsu-lab/stanford_alpaca, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-SCHEDULING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18253:end -->

<!-- review:SF-2026-ARXIV-2607-18254:start -->
### Cross-Dialect Generalization Without Retraining: Benchmarks and Evaluation of Schema-Derived Constrained Decoding for MLIR

<!-- claim:SF-2026-ARXIV-2607-18254:start -->Multi-Level Intermediate Representation (MLIR) underlies modern ML compiler infrastructure (TensorFlow, JAX/StableHLO, PyTorch Inductor, IREE), yet appears only in trace amounts in code-LM pretraining corpora. MLIR is also extensible by design: new dialects ship per application domain, so a fine-tuned model per dialect does not scale. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18254:end -->

**为什么进入候选分母。** 摘要首要问题为“Multi-Level Intermediate Representation (MLIR) underlies modern ML compiler infrastructure (TensorFlow, JAX/StableHLO, PyTorch Inductor, IREE), yet appears only in trace amounts in code-LM pretraining corpora.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** MLIR is also extensible by design: new dialects ship per application domain, so a fine-tuned model per dialect does not scale.

**证据证明什么。** We release benchmarks, decoder, all per-prompt generations, and a reproducibility Docker image.

**证据没有证明什么。** Two smaller threads: (i) the in-line coupled decoder hit max_tokens on every prompt in our pilot (§ 7 ), leaving the empirical-decoder gap as future work for anyone aiming to remove the 5-retry budget; (ii) extending the grammar to scf, affine, gpu, async, transform, tensor, vector is a few-day derivation per dialect on the existing pipeline, not a research question. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18254v1#S3 — 3 Method; https://arxiv.org/html/2607.18254v1#S4.SS1 — 4.1 Models。Evaluation：https://arxiv.org/html/2607.18254v1#S4 — 4 Experimental Setup; https://arxiv.org/html/2607.18254v1#S4.SS2 — 4.2 Benchmarks。Limitations / counterevidence：https://arxiv.org/html/2607.18254v1#S7 — 7 Limitations; https://arxiv.org/html/2607.18254v1#S8 — 8 Future Work。

**Artifact boundary。** Exact v1 links https://github.com/plawanrath/slm-to-mlir-constrained-emitter, https://huggingface.co/datasets/plawanrath/MLIR-Spec-150, https://huggingface.co/datasets/plawanrath/Linalg-Spec-30; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Two smaller threads: (i) the in-line coupled decoder hit max_tokens on every prompt in our pilot (§ 7 ), leaving the empirical-decoder gap as future work for anyone aiming to remove the 5-retry budget; (ii) extending the grammar to scf, affine, gpu, async, transform, tensor, vector is a few-day derivation per dialect on the existing pipeline, not a research question.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`INFER-TENSORRT-LLM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18254:end -->

<!-- review:SF-2026-ARXIV-2607-18261:start -->
### When JSON Is Not Enough: Semantic Reliability of Schema-Constrained LLM Ordering Agents

<!-- claim:SF-2026-ARXIV-2607-18261:start -->LLM agents are increasingly used as transaction compilers: a user states an intent in natural language, and the model emits a structured object that an API can execute. JSON Schema and provider-level structured-output modes are useful because they remove a large class of parse failures, but they do not by themselves decide whether the object is a safe, faithful transaction. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18261:end -->

**为什么进入候选分母。** 摘要首要问题为“LLM agents are increasingly used as transaction compilers: a user states an intent in natural language, and the model emits a structured object that an API can execute.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** We introduce OrderBench, a deterministic benchmark for restaurant ordering agents that separates syntactic validity, schema validity, status decisions, exact item semantics, constraint preservation, and unsafe acceptances.

**证据证明什么。** Across 2,400 Nebius Token Factory calls to four open models in prompt-only and JSON-schema modes, we find that schema-valid output can still have large semantic error rates.

**证据没有证明什么。** It cannot ensure that a requested allergen conflict was rejected, that “one without onion and one normal” was split into two item objects, or that “pineapple” was not silently invented as a modifier. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18261v1#A1 — Appendix A Model-by-Category Heatmap。Evaluation：https://arxiv.org/html/2607.18261v1#S3 — 3 Benchmark; https://arxiv.org/html/2607.18261v1#S4 — 4 Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.18261v1#S6 — 6 Discussion; https://arxiv.org/html/2607.18261v1#S7 — 7 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：It cannot ensure that a requested allergen conflict was rejected, that “one without onion and one normal” was split into two item objects, or that “pineapple” was not silently invented as a modifier.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-TOOL-CALLING`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18261:end -->

<!-- review:SF-2026-ARXIV-2607-18264:start -->
### MUX: Continuous Reasoning via Multiplexed Tokens

<!-- claim:SF-2026-ARXIV-2607-18264:start -->Language models solve complex problems by articulating intermediate reasoning steps in natural language. While effective, this process is computationally bottlenecked: each reasoning step conveys only a single subword, and many are spent expressing a thought instead of carrying out computation. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18264:end -->

**为什么进入候选分母。** 摘要首要问题为“Language models solve complex problems by articulating intermediate reasoning steps in natural language.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We propose MUX, a simple method for high-bandwidth and compact reasoning based on distillation of discrete reasoning into continuous multiplexed tokens in a latent space.

**证据证明什么。** We further show that multiplexed reasoning can perform parallel exploration in problems that require search.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18264v1#S11 — 11 Method and training details; https://arxiv.org/html/2607.18264v1#S11.SS1 — 11.1 Implementation details。Evaluation：https://arxiv.org/html/2607.18264v1#S10 — 10 Benchmark details; https://arxiv.org/html/2607.18264v1#S4 — 4 Theoretical analysis。Limitations / counterevidence：https://arxiv.org/html/2607.18264v1#S12 — 12 Limitations and broader impact; https://arxiv.org/html/2607.18264v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/MisakiTaro0414/mux, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MODEL-DECODER-ONLY`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18264:end -->

<!-- review:SF-2026-ARXIV-2607-18265:start -->
### State Compression in Two-Agent LLM Relays: A Closed-World Study of Constraint Preservation

<!-- claim:SF-2026-ARXIV-2607-18265:start -->Long-running Large Language Model (LLM)-based agents often accumulate large intermediate traces containing audits, eliminations, and numeric calculations. In practice, this state is compressed before handing it to a downstream decision step, creating an information bottleneck in which small omissions can break strict numeric or categorical constraints. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18265:end -->

**为什么进入候选分母。** 摘要首要问题为“Long-running Large Language Model (LLM)-based agents often accumulate large intermediate traces containing audits, eliminations, and numeric calculations.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** In practice, this state is compressed before handing it to a downstream decision step, creating an information bottleneck in which small omissions can break strict numeric or categorical constraints.

**证据证明什么。** Results show that hand-off representation strongly affects downstream feasibility under a small decision model.

**证据没有证明什么。** This is consistent with the view that agent reliability often depends on externalized infrastructure and harness design rather than model capability alone [ 12 ] . 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18265v1#S2 — II Methodology; https://arxiv.org/html/2607.18265v1#S6.SS1 — VI-A Mixed-model relays。Evaluation：https://arxiv.org/html/2607.18265v1#S2.SS5 — II-E Evaluation Metrics and Logging; https://arxiv.org/html/2607.18265v1#S3 — III Results。Limitations / counterevidence：https://arxiv.org/html/2607.18265v1#S3.SS2 — III-B Failure Modes; https://arxiv.org/html/2607.18265v1#S4 — IV Discussion and Analysis。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：This is consistent with the view that agent reliability often depends on externalized infrastructure and harness design rather than model capability alone [ 12 ] .

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MULTI-AGENT`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18265:end -->

<!-- review:SF-2026-ARXIV-2607-18280:start -->
### Beyond Single-Dimensional Compression: The Compound Sparsity Frontier of Large Language Models

<!-- claim:SF-2026-ARXIV-2607-18280:start -->Large language models (LLMs) are often compressed through static parameter pruning or dynamic token-level computation, yet aggressive sparsification can trigger rapid performance degradation beyond an essential sparsity boundary. This work asks \emph{whether combining these two mechanisms can delay such degradation by distributing the compression burden}. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18280:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language models (LLMs) are often compressed through static parameter pruning or dynamic token-level computation, yet aggressive sparsification can trigger rapid performance degradation beyond an essential sparsity boundary.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** We study a minimalist compound sparsity framework that first applies low-rank approximation and channel pruning to obtain a statically compressed backbone, and then introduces lightweight routers for per-token dynamic layer skipping.

**证据证明什么。** These results demonstrate that compound compression provides a practical way to improve LLM compression, while revealing a broader cross-dimensional sparsity boundary that ultimately limits further compression.

**证据没有证明什么。** Our empirical evidence proves that sharing compression pressure across parameter and token dimensions cannot bypass the inherent sparsity limit, but merely defers performance degradation. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18280v1#S2 — 2 Methodology。Evaluation：https://arxiv.org/html/2607.18280v1#S3 — 3 Experiments; https://arxiv.org/html/2607.18280v1#S3.SS2 — 3.2 Main Results。Limitations / counterevidence：https://arxiv.org/html/2607.18280v1#S4 — 4 Conclusion; https://arxiv.org/html/2607.18280v1#Sx1 — Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：Our empirical evidence proves that sharing compression pressure across parameter and token dimensions cannot bypass the inherent sparsity limit, but merely defers performance degradation.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-GPU-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18280:end -->

<!-- review:SF-2026-ARXIV-2607-18284:start -->
### Compressing What Matters: Neuron Importance Meets Data-Aware Low Rank Approximation for Language Model Compression

<!-- claim:SF-2026-ARXIV-2607-18284:start -->To excel at their domain large language models are comprised of billions of parameters. Yet this comes at the cost of huge memory requirements restricting their applicability in resource-constrained environments. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18284:end -->

**为什么进入候选分母。** 摘要首要问题为“To excel at their domain large language models are comprised of billions of parameters.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** Contrary to them in this work we propose an enhanced and computationally efficient algorithm for dynamic compression rate allocation.

**证据证明什么。** Experimental results support the efficacy of the proposed approach which performs on par or substantially better than the previous state-of-the-art especially under high compression ratios.

**证据没有证明什么。** Experimental results demonstrate that NIDA-SVD consistently outperforms prior state-of-the-art methods under diverse allocation strategies, while our proposed rank allocation algorithm also independently strengthens both NIDA-SVD and previous approaches. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18284v1#S3.SS1 — III-A The Transformer Architecture; https://arxiv.org/html/2607.18284v1#S3.SS3 — III-C BERT-based Architectures。Evaluation：https://arxiv.org/html/2607.18284v1#S6 — VI Experimental Results; https://arxiv.org/html/2607.18284v1#S6.SS1 — VI-A Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.18284v1#S7 — VII Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：Experimental results demonstrate that NIDA-SVD consistently outperforms prior state-of-the-art methods under diverse allocation strategies, while our proposed rank allocation algorithm also independently strengthens both NIDA-SVD and previous approaches.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`INFER-GPU-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18284:end -->

<!-- review:SF-2026-ARXIV-2607-18292:start -->
### Reliability Scales Inversely: Hallucinations Snowball Faster in Bigger Language Models

<!-- claim:SF-2026-ARXIV-2607-18292:start -->Across three families, three benchmarks and six rungs, including in-the-wild chat logs, scaling closes the start-of-response knowledge gap up to $7\times$ while within-response knowledge degradation grows up to $39\times$. We trace that residual to one variable, the per-position disagreement $δ= \log p_M - \log p_O$ against a stronger oracle, whose second moment splits exactly into bias$^2$ $\mathrm{KL}(p_M \,\|\, p_O)^2$ and decoding risk $\mathrm{Var}[δ]$. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18292:end -->

**为什么进入候选分母。** 摘要首要问题为“Bigger language models are less reliable.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We trace that residual to one variable, the per-position disagreement $δ= \log p_M - \log p_O$ against a stronger oracle, whose second moment splits exactly into bias$^2$ $\mathrm{KL}(p_M \,\|\, p_O)^2$ and decoding risk $\mathrm{Var}[δ]$.

**证据证明什么。** Bigger models snowball mistakes faster, through a failure mode that is dominant, self-perpetuating, causal and invisible to the model itself.

**证据没有证明什么。** The failure mode that dominates the error budget, self-perpetuates across a response, and worsens with scale is exactly the one self-monitoring structurally cannot capture. “The model knows but hallucinates” is that asymmetry in miniature: bias small, risk not. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18292v1#A1 — Appendix A Models, Data, and Verifier Protocol; https://arxiv.org/html/2607.18292v1#A7 — Appendix G Detector Implementation。Evaluation：https://arxiv.org/html/2607.18292v1#S1 — 1 Introduction; https://arxiv.org/html/2607.18292v1#S2 — 2 Self-Conditioning Converts Persistent Risk into Bias。Limitations / counterevidence：https://arxiv.org/html/2607.18292v1#S6 — 6 Discussion and Implications; https://arxiv.org/html/2607.18292v1#Sx1 — Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：The failure mode that dominates the error budget, self-perpetuates across a response, and worsens with scale is exactly the one self-monitoring structurally cannot capture. “The model knows but hallucinates” is that asymmetry in miniature: bias small, risk not.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`WORLDVIEW-LLM-INTELLIGENCE`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18292:end -->

<!-- review:SF-2026-ARXIV-2607-18295:start -->
### On the Limits of Support-Preserving Alignment and Bounded Filtering

<!-- claim:SF-2026-ARXIV-2607-18295:start -->We study whether alignment schemes that reshape a base model's output distribution, combined with bounded safety filters, can drive the probability of harmful behavior to zero in modern large language models. Recent research suggests that harmful behaviors can persist under preference-based alignment and that external filtering can be computationally hard in the worst case, but it remains unclear whether practical alignment pipelines that largely preserve internal representations can eliminate harmful behavior entirely rather than merely suppressing its most visible forms. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18295:end -->

**为什么进入候选分母。** 摘要首要问题为“We study whether alignment schemes that reshape a base model's output distribution, combined with bounded safety filters, can drive the probability of harmful behavior to zero in modern large language models.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** Building on this framework, we provide computational and information-theoretic arguments indicating that, under these constraints, bounded filtering may fail to eliminate all harmful outputs supported by the base model's distribution.

**证据证明什么。** Across models, filter classes, and query budgets, the estimated harmful-output rate decreases with additional filtering compute but consistently plateaus above zero, suggesting a persistent empirical harm floor.

**证据没有证明什么。** Rather, they identify structural conditions under which external filtering and probability reshaping alone cannot guarantee universal safety: when alignment preserves support and filters are computationally limited, some residual harmful mass can remain even as filters are strengthened. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18295v1#A1 — Appendix A Theoretical Framework; https://arxiv.org/html/2607.18295v1#S3 — 3 Method。Evaluation：https://arxiv.org/html/2607.18295v1#S2.SS2 — 2.2 Impossibility and No-Go Results in Alignment; https://arxiv.org/html/2607.18295v1#S4 — 4 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.18295v1#S5 — 5 Discussion and Conclusion; https://arxiv.org/html/2607.18295v1#S2.SS1 — 2.1 Limitations of RLHF and Preference-Based Alignment。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Rather, they identify structural conditions under which external filtering and probability reshaping alone cannot guarantee universal safety: when alignment preserves support and filters are computationally limited, some residual harmful mass can remain even as filters are strengthened.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-RLHF`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18295:end -->

<!-- review:SF-2026-ARXIV-2607-18305:start -->
### The Information Shadow: Measuring Structural Limits on What Language Models Can Learn

<!-- claim:SF-2026-ARXIV-2607-18305:start -->Some limits on what language models know are not gaps in data coverage but structural properties of learning from text. We introduce the information shadow: the region of phenomena that a text-trained learner cannot acquire regardless of scale, comprising (I) structures language cannot express, (II) functions that are statistically non-identifiable from the training distribution, and (III) functions that are representable but unreachable by gradient-based training. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18305:end -->

**为什么进入候选分母。** 摘要首要问题为“Some limits on what language models know are not gaps in data coverage but structural properties of learning from text.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We introduce the information shadow: the region of phenomena that a text-trained learner cannot acquire regardless of scale, comprising (I) structures language cannot express, (II) functions that are statistically non-identifiable from the training distribution, and (III) functions that are representable but unreachable by gradient-based training.

**证据证明什么。** We release the probe suite and discuss implications for benchmark design, capability auditing, and shadow-aware uncertainty.

**证据没有证明什么。** 9 Conclusion The information shadow reframes a family of language-model limitations as structural rather than incidental, and makes each kind measurable. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18305v1#S1 — 1 Introduction; https://arxiv.org/html/2607.18305v1#S2 — 2 Related Work。Evaluation：https://arxiv.org/html/2607.18305v1#S5.SS4 — 5.4 Experimental setup; https://arxiv.org/html/2607.18305v1#S7 — 7 Results。Limitations / counterevidence：https://arxiv.org/html/2607.18305v1#S8 — 8 Discussion; https://arxiv.org/html/2607.18305v1#S9 — 9 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：9 Conclusion The information shadow reframes a family of language-model limitations as structural rather than incidental, and makes each kind measurable.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`WORLDVIEW-WHY-MODELS-LEARN`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18305:end -->

<!-- review:SF-2026-ARXIV-2607-18314:start -->
### Interactive Training 2: Auditable Control Plane for Live Model Training

<!-- claim:SF-2026-ARXIV-2607-18314:start -->Experiment trackers show how training is progressing, but changing a live run still usually requires trainer-specific code. We present Interactive Training 2, an open-source control plane for steering training through a shared protocol. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18314:end -->

**为什么进入候选分母。** 摘要首要问题为“Experiment trackers show how training is progressing, but changing a live run still usually requires trainer-specific code.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** We demonstrate the system across five NLP and reinforcement-learning workflows.

**证据证明什么。** We demonstrate the system across five NLP and reinforcement-learning workflows.

**证据没有证明什么。** Value bounds, type checks, permissions, and human controls limit what an agent may do, but they cannot guarantee safe or optimal actions. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18314v1#S2 — 2 System at a Glance; https://arxiv.org/html/2607.18314v1#S3 — 3 Control-Plane Design。Evaluation：https://arxiv.org/html/2607.18314v1#S5.SS2 — 5.2 From Request to Recorded Result。Limitations / counterevidence：https://arxiv.org/html/2607.18314v1#S7 — 7 Conclusion; https://arxiv.org/html/2607.18314v1#Sx1 — Limitations。

**Artifact boundary。** Exact v1 links https://github.com/yuntian-group/interactive-training, https://doi.org/10.18653/v1/2020.emnlp-demos.6, https://doi.org/10.18653/v1/2025.emnlp-demos.65; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：Value bounds, type checks, permissions, and human controls limit what an agent may do, but they cannot guarantee safe or optimal actions.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-TRAINING-OPERATOR`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18314:end -->

<!-- review:SF-2026-ARXIV-2607-18316:start -->
### Binding Drift in Multi-Step Tool-Augmented Agents

<!-- claim:SF-2026-ARXIV-2607-18316:start -->Tool-augmented language-model agents execute multi-step workflows over external systems, resolving an entity once and then acting on it across subsequent steps. Prior work shows that in single-step actions, agents select the correct tool but bind it to the wrong entity 24-26% of the time. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18316:end -->

**为什么进入候选分母。** 摘要首要问题为“Tool-augmented language-model agents execute multi-step workflows over external systems, resolving an entity once and then acting on it across subsequent steps.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** Tool-augmented language-model agents execute multi-step workflows over external systems, resolving an entity once and then acting on it across subsequent steps.

**证据证明什么。** Prior work shows that in single-step actions, agents select the correct tool but bind it to the wrong entity 24-26% of the time.

**证据没有证明什么。** The practical implication is that practitioners cannot deploy a single persistence mechanism and assume both problems are solved; re-derivation (as bounded by our oracle experiment) addresses propagation where persistence cannot. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18316v1#A3 — Appendix C Compute Environment and Model Details; https://arxiv.org/html/2607.18316v1#S5.SS3 — 5.3 Per-Model Heterogeneity。Evaluation：https://arxiv.org/html/2607.18316v1#A2 — Appendix B Per-Pattern Analysis; https://arxiv.org/html/2607.18316v1#S3 — 3 Benchmark。Limitations / counterevidence：https://arxiv.org/html/2607.18316v1#S5.SS5 — 5.5 The Two Failure Modes Respond Oppositely; https://arxiv.org/html/2607.18316v1#S7 — 7 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/shashank-indukuri/binding-drift, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：The practical implication is that practitioners cannot deploy a single persistence mechanism and assume both problems are solved; re-derivation (as bounded by our oracle experiment) addresses propagation where persistence cannot.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-TOOL-CALLING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18316:end -->

<!-- review:SF-2026-ARXIV-2607-18336:start -->
### EmoEUS: Uncertainty Supervision for Multimodal Emotion Recognition in Conversation

<!-- claim:SF-2026-ARXIV-2607-18336:start -->Multimodal emotion recognition in conversation (MERC) can leverage multimodal and contextual cues to boost recognition performance. However, existing fusion approaches in MERC often ignore modality-specific uncertainty across utterances caused by conflicting cues, varying noise, and missing modality-specific signals. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18336:end -->

**为什么进入候选分母。** 摘要首要问题为“Multimodal emotion recognition in conversation (MERC) can leverage multimodal and contextual cues to boost recognition performance.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We propose EmoEUS, an explicit uncertainty supervision framework for MERC.

**证据证明什么。** Experiments on IEMOCAP and MELD show that EmoEUS consistently outperforms state-of-the-art methods.

**证据没有证明什么。** 5 Conclusions and Future Work We propose the EmoEUS, a novel framework that incorporates explicit uncertainty supervision for MERC. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18336v1#S2 — 2 Methodology; https://arxiv.org/html/2607.18336v1#S2.SS2 — 2.2 Overall Architecture。Evaluation：https://arxiv.org/html/2607.18336v1#S4 — 4 Experimental Results and Analysis; https://arxiv.org/html/2607.18336v1#S3 — 3 Experimental Settings。Limitations / counterevidence：https://arxiv.org/html/2607.18336v1#S5 — 5 Conclusions and Future Work。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：5 Conclusions and Future Work We propose the EmoEUS, a novel framework that incorporates explicit uncertainty supervision for MERC.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18336:end -->

<!-- review:SF-2026-ARXIV-2607-18347:start -->
### A Decision-Centered Reference Architecture for Trustworthy Agentic Commerce

<!-- claim:SF-2026-ARXIV-2607-18347:start -->Agentic commerce extends agentic shopping into software agents that interpret policy, prepare checkout, generate transaction-facing language, and act under delegated payment authority. Protocols standardize external exchanges, but merchants still need one authoritative representation of commercial eligibility, actor authority, checkout validity, payment dispatch, generated claims, and evidence. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18347:end -->

**为什么进入候选分母。** 摘要首要问题为“Agentic commerce extends agentic shopping into software agents that interpret policy, prepare checkout, generate transaction-facing language, and act under delegated payment authority.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** Protocols standardize external exchanges, but merchants still need one authoritative representation of commercial eligibility, actor authority, checkout validity, payment dispatch, generated claims, and evidence.

**证据证明什么。** Results support protected-dependency change detection, bounded outcome derivation, stale-decision prevention, surface-bound status consistency, refusal propagation, and verified-state identity under synthetic fixtures, but do not establish rule completeness, production security, performance, legal compliance, live interoperability, population error rates, or independent replication.

**证据没有证明什么。** 7.4 Limitations and threats to validity First, the author designed the artifact, the seven deterministic rules, the scenario corpus, and the ablation fixtures, creating confirmation and implementation-bias risk. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18347v1#S3.SS1 — 3.1 Design-science approach; https://arxiv.org/html/2607.18347v1#S2.SS1 — 2.1 Agent-facing commerce is a distributed systems problem。Evaluation：https://arxiv.org/html/2607.18347v1#S6 — 6 Evaluation and results; https://arxiv.org/html/2607.18347v1#S6.SS4 — 6.4 Controlled ablation results。Limitations / counterevidence：https://arxiv.org/html/2607.18347v1#S7.SS4 — 7.4 Limitations and threats to validity; https://arxiv.org/html/2607.18347v1#S3.SS3 — 3.3 Threat model。

**Artifact boundary。** Exact v1 links https://github.com/dmsfiris/agentic-commerce-blueprint, https://github.com/dmsfiris/agentic-commerce-blueprint/releases/tag/v0.9.2, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：7.4 Limitations and threats to validity First, the author designed the artifact, the seven deterministic rules, the scenario corpus, and the ablation fixtures, creating confirmation and implementation-bias risk.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-PLATFORM`；evidence-stage relation：`structural_candidate`。
- Books 候选路由（尚非最终决定）：`Structural Candidate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18347:end -->

<!-- review:SF-2026-ARXIV-2607-18357:start -->
### Decode-Time Grammars: Constrained LLM Generation over a Refinement Order of Grammar Fragments

<!-- claim:SF-2026-ARXIV-2607-18357:start -->Large language models now write a growing share of the world's code, increasingly inside agents and serving systems that compile, execute, or dispatch generated code without line-by-line review. This works well for mainstream languages but remains brittle for low-resource programming surfaces such as domain-specific languages, custom library APIs, and command-line tools. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18357:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language models now write a growing share of the world's code, increasingly inside agents and serving systems that compile, execute, or dispatch generated code without line-by-line review.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** Large language models now write a growing share of the world's code, increasingly inside agents and serving systems that compile, execute, or dispatch generated code without line-by-line review.

**证据证明什么。** We formalize grammar fragments as environment-indexed grammars ordered by refinement, prove No-Ghost soundness for Gamma-slotted fragments, show that refinement preserves this support-set guarantee, and characterize the boundary of mask-enforceable properties.

**证据没有证明什么。** These failures are not caused only by lack of data. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18357v1#S5 — 5. Implementation and Scope。Evaluation：https://arxiv.org/html/2607.18357v1#S6 — 6. Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.18357v1#S3.SS1 — 3.1. The failure: negative transfer, not ignorance; https://arxiv.org/html/2607.18357v1#S5.SS4 — 5.4. Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：These failures are not caused only by lack of data.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MODEL-SAMPLING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18357:end -->

<!-- review:SF-2026-ARXIV-2607-18360:start -->
### HALLMARK: Diagnosing Three Failure Modes in LLM Citation Verifiers

<!-- claim:SF-2026-ARXIV-2607-18360:start -->Large language models (LLMs) now routinely draft literature reviews and assist with academic writing, which means a higher risk of fabricated references: GPTZero found 53 papers with hallucinated citations among NeurIPS 2025's accepted set. Rule- and LLM-based verifiers are emerging, but no shared benchmark compares them and gives detailed failure diagnostics. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18360:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language models (LLMs) now routinely draft literature reviews and assist with academic writing, which means a higher risk of fabricated references: GPTZero found 53 papers with hallucinated citations among NeurIPS 2025's accepted set.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Rule- and LLM-based verifiers are emerging, but no shared benchmark compares them and gives detailed failure diagnostics.

**证据证明什么。** Thus FPR is the deployment bottleneck, but an undetected fabrication remains the costlier error for the scientific record.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18360v1#A7 — Appendix G bibtex-updater: the co-designed reference tool。Evaluation：https://arxiv.org/html/2607.18360v1#A2 — Appendix B Evaluation protocol and reproducibility; https://arxiv.org/html/2607.18360v1#A3 — Appendix C Core results and validity。Limitations / counterevidence：https://arxiv.org/html/2607.18360v1#A4 — Appendix D Failure mode (i): agentic aggregation; https://arxiv.org/html/2607.18360v1#A5 — Appendix E Failure mode (ii): base-rate precision and deployment。

**Artifact boundary。** Exact v1 links https://pypi.org/project/harcx/, https://github.com/amazon-science/RefChecker, https://github.com/rpatrik96/bibtexupdater; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18360:end -->

<!-- review:SF-2026-ARXIV-2607-18366:start -->
### Operational Hallucination and Safety Drift in AI Agents

<!-- claim:SF-2026-ARXIV-2607-18366:start -->Large language models (LLMs) serving as planners in tool-using autonomous agents introduce dynamic reliability risks in multi-turn execution. While single-turn safety mechanisms are relatively mature, extended interactions reveal structural vulnerabilities where initial alignment degrades over time. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18366:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language models (LLMs) serving as planners in tool-using autonomous agents introduce dynamic reliability risks in multi-turn execution.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** We propose an Action-Aware Supervision Layer - a lightweight, plug-and-play architectural blueprint incorporating intent-action consistency checks, runtime state tracking, and forced termination primitives.

**证据证明什么。** Post-hoc simulation on captured failure trajectories shows the layer can intercept observed violations without false positives on benign cases.

**证据没有证明什么。** However, these works remain largely descriptive in terms of agent behavior and evaluation objectives, and they do not 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/pdf/2607.18366v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.18366v1#page=2 — PDF page 2。Evaluation：https://arxiv.org/pdf/2607.18366v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.18366v1#page=2 — PDF page 2。Limitations / counterevidence：https://arxiv.org/pdf/2607.18366v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.18366v1#page=2 — PDF page 2。

**Artifact boundary。** Exact v1 links https://github.com/WooooDyy/LLM-Agent-Paper-List, https://github.com/xiye17/TextualExplInContext, https://github.com/noahshinn024/reflexion; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：However, these works remain largely descriptive in terms of agent behavior and evaluation objectives, and they do not

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18366:end -->

<!-- review:SF-2026-ARXIV-2607-18367:start -->
### AlayaWorld: Interactive Long-Horizon World Modeling -- Full Technical Report

<!-- claim:SF-2026-ARXIV-2607-18367:start -->Unlike conventional video game development, which relies on labor-intensive pipelines for asset production, animation, physics, and programming, video world models generate interactive environments from user inputs instantly. It enable us to create customized, explorable, and continuously evolving virtual world from text, an image, or video. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18367:end -->

**为什么进入候选分母。** 摘要首要问题为“Unlike conventional video game development, which relies on labor-intensive pipelines for asset production, animation, physics, and programming, video world models generate interactive environments from user inputs instantly.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We present AlayaWorld, an interactive long-horizon video world model that generates 24-fps video at 540p and 720p.

**证据证明什么。** On iWorld-Bench, AlayaWorld achieves the best performance over long-horizon generation.

**证据没有证明什么。** Rather than addressing these properties independently, AlayaWorld integrates them within a unified autoregressive framework in which several design choices simultaneously benefit multiple objectives. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18367v1#S3.SS2 — 3.2 Bidirectional Model Pre-Training – Establishing the General Video Prior; https://arxiv.org/html/2607.18367v1#S3.SS3 — 3.3 Autoregressive Model Training – Control and Memory Integration。Evaluation：https://arxiv.org/html/2607.18367v1#S4 — 4 Results; https://arxiv.org/html/2607.18367v1#S4.SS1 — 4.1 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.18367v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/AlayaLab/AlayaWorld, https://github.com/JaidedAI/EasyOCR, https://huggingface.co/moonshotai/Kimi-K2.6; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Rather than addressing these properties independently, AlayaWorld integrates them within a unified autoregressive framework in which several design choices simultaneously benefit multiple objectives.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18367:end -->

<!-- review:SF-2026-ARXIV-2607-18445:start -->
### ChainMark: Model-Free LLM Watermarking with Closed-Form Calibration

<!-- claim:SF-2026-ARXIV-2607-18445:start -->Regulatory regimes such as the EU AI Act mandate machine-readable marking of synthetic text, but existing watermark detectors rely on the generating LM and on heuristic thresholds with no closed-form calibration. We introduce ChainMark, an active watermark that partitions the vocabulary into S states via keyed SHA-256 and forces a hard Markov transition on a fraction rho of positions; the detector replays the partition from the same key in O(n) hash operations, with no LM access. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18445:end -->

**为什么进入候选分母。** 摘要首要问题为“Regulatory regimes such as the EU AI Act mandate machine-readable marking of synthetic text, but existing watermark detectors rely on the generating LM and on heuristic thresholds with no closed-form calibration.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** We introduce ChainMark, an active watermark that partitions the vocabulary into S states via keyed SHA-256 and forces a hard Markov transition on a fraction rho of positions; the detector replays the partition from the same key in O(n) hash operations, with no LM access.

**证据证明什么。** Across three instruction-tuned LLMs and four domains, ChainMark strictly dominates KGW and SWEET under translation and random-substitution attacks at matched budget; a one-corpus empirical recalibration restores the 1% target FPR on natural-language text.

**证据没有证明什么。** Only the empirical-SD recipe (Fix 1) brings FPR within pp of the target ( ); the other four sit at – FPR or collapse TPR. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18445v1#A3.SS1 — C.1 Models, Tokenizers, and Hardware; https://arxiv.org/html/2607.18445v1#A5 — Appendix E Reference Detector Implementation。Evaluation：https://arxiv.org/html/2607.18445v1#A1.SS8 — A.8 Supplementary Results: Quality Cost and Self-Healing; https://arxiv.org/html/2607.18445v1#A3 — Appendix C Experimental Protocol and Reproducibility。Limitations / counterevidence：https://arxiv.org/html/2607.18445v1#A4.SS2 — D.2 FPR Recalibration: SD Recipe and Failure Modes; https://arxiv.org/html/2607.18445v1#S7 — 7 Discussion。

**Artifact boundary。** Exact v1 links https://digital-strategy.ec.europa.eu/en/library/first-draft-code-practice-transparency-ai-generated-content, https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct, https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：Only the empirical-SD recipe (Fix 1) brings FPR within pp of the target ( ); the other four sit at – FPR or collapse TPR.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18445:end -->

<!-- review:SF-2026-ARXIV-2607-18454:start -->
### Estimating Rare Events in Language Models with Proper Evaluation

<!-- claim:SF-2026-ARXIV-2607-18454:start -->Quantifying the risk of rare failures in language models, such as those triggered by adversarial distribution shifts or very large-scale deployments, requires estimating probabilities far too small for random sampling. While recent work has formalized Low Probability Estimation, existing pipelines remain fragile in the rarest regimes: estimators can suffer zero-estimate collapse or systematic bias, and standard evaluation losses can become unstable or poorly matched to asymmetric safety costs. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18454:end -->

**为什么进入候选分母。** 摘要首要问题为“Quantifying the risk of rare failures in language models, such as those triggered by adversarial distribution shifts or very large-scale deployments, requires estimating probabilities far too small for random sampling.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** In this work, we introduce Gradient Activation Adaptive Multi-Level Splitting (GA-AMLS), which adapts rare-event Monte Carlo methods to the continuous activation space of language models.

**证据证明什么。** Experiments on small transformer models reveal a bias-variance tradeoff: GA-AMLS achieves the lowest loss under symmetric evaluation, reducing average log-space squared error relative to the strongest baseline across model sizes, while methods with overestimation bias prevail under asymmetric penalties.

**证据没有证明什么。** However, the gap between continuous activations and discrete inputs remains a fundamental limitation of activation-space methods, including QLD. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18454v1#A6 — Appendix F All Methods Loss by Distributions; https://arxiv.org/html/2607.18454v1#S2.SS2 — 2.2 Sampling Methods。Evaluation：https://arxiv.org/html/2607.18454v1#S5 — 5 Experimental Results; https://arxiv.org/html/2607.18454v1#A4 — Appendix D Experimental and Implementation Details。Limitations / counterevidence：https://arxiv.org/html/2607.18454v1#S7 — 7 Discussion and Limitations; https://arxiv.org/html/2607.18454v1#S8 — 8 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/TransformerLensOrg/TransformerLens, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：However, the gap between continuous activations and discrete inputs remains a fundamental limitation of activation-space methods, including QLD.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18454:end -->

<!-- review:SF-2026-ARXIV-2607-18476:start -->
### Structured Output Collapses Answer Diversity Across 44 Language Models

<!-- claim:SF-2026-ARXIV-2607-18476:start -->When a language model must choose one answer from a large space of equally valid options, a format clause -- "Reply with JSON only" -- changes which answer it chooses. We re-run the One-Word Census (arXiv:2607.12796): 31 wide-answer-space category prompts asked of 44 models, now with the reply requested in JSON -- no schema enforcement, no constrained decoding, only the request. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18476:end -->

**为什么进入候选分母。** 摘要首要问题为“When a language model must choose one answer from a large space of equally valid options, a format clause -- "Reply with JSON only" -- changes which answer it chooses.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We re-run the One-Word Census (arXiv:2607.12796): 31 wide-answer-space category prompts asked of 44 models, now with the reply requested in JSON -- no schema enforcement, no constrained decoding, only the request.

**证据证明什么。** Structured output is how software consumes language models, and that surface is served by a measurably more homogeneous model than the chat surface on which models are evaluated, compared, and chosen.

**证据没有证明什么。** Each format is probed with a single clause wording, so we cannot separate the register from the particular phrasing that invokes it; a clause-paraphrase column is the natural control. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18476v1#S3 — 3 Method。Evaluation：https://arxiv.org/html/2607.18476v1#S4 — 4 Results。Limitations / counterevidence：https://arxiv.org/html/2607.18476v1#S5 — 5 Limitations; https://arxiv.org/html/2607.18476v1#S6 — 6 Discussion。

**Artifact boundary。** Exact v1 links https://github.com/tap2k/modelun, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Each format is probed with a single clause wording, so we cannot separate the register from the particular phrasing that invokes it; a clause-paraphrase column is the natural control.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MODEL-SAMPLING`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18476:end -->

<!-- review:SF-2026-ARXIV-2607-18481:start -->
### Search-on-Graph-R1: Training Large Language Models to Search Knowledge Graphs with Reinforcement Learning

<!-- claim:SF-2026-ARXIV-2607-18481:start -->Knowledge graph question answering (KGQA) requires navigating from topic entities to an answer several relations away. Recent methods prompt a frontier LLM to explore the graph through a retrieval tool, but their reliance on frontier-scale inference makes them costly to deploy. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18481:end -->

**为什么进入候选分母。** 摘要首要问题为“Knowledge graph question answering (KGQA) requires navigating from topic entities to an answer several relations away.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** Recent methods prompt a frontier LLM to explore the graph through a retrieval tool, but their reliance on frontier-scale inference makes them costly to deploy.

**证据证明什么。** On WebQSP, CWQ, and GrailQA, \sogrone{} at 8B surpasses every frozen frontier-LLM system in our comparison and posts the strongest results on CWQ of any system we compare against.

**证据没有证明什么。** Limitations We evaluate SoG-R1 only on Freebase, the KG underlying WebQSP, CWQ, and GrailQA, and our pipeline assumes a KG that exposes 1-hop neighbour retrieval and a per-question gold SPARQL query at training time. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18481v1#S4 — 4 Methodology。Evaluation：https://arxiv.org/html/2607.18481v1#S5 — 5 Experiments; https://arxiv.org/html/2607.18481v1#S5.SS2 — 5.2 Main Results。Limitations / counterevidence：https://arxiv.org/html/2607.18481v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.18481v1#Sx1 — Limitations。

**Artifact boundary。** Exact v1 links https://doi.org/10.18653/v1/2024.acl-demos.38, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Limitations We evaluate SoG-R1 only on Freebase, the KG underlying WebQSP, CWQ, and GrailQA, and our pipeline assumes a KG that exposes 1-hop neighbour retrieval and a per-question gold SPARQL query at training time.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`TRAIN-GRPO`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18481:end -->

<!-- review:SF-2026-ARXIV-2607-18485:start -->
### Trusted Credentials, Untrusted Behavior: Benchmarking LLM-Agent Security in High-Performance Computing

<!-- claim:SF-2026-ARXIV-2607-18485:start -->Large language model (LLM) agents are starting to take on routine work in high-performance computing (HPC), including monitoring Slurm jobs, diagnosing failed builds, inspecting simulation output, and coordinating scientific workflows. To do this work, an agent commonly acts under its user's credentials and inherits the user's access to files and the scheduler. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18485:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language model (LLM) agents are starting to take on routine work in high-performance computing (HPC), including monitoring Slurm jobs, diagnosing failed builds, inspecting simulation output, and coordinating scientific workflows.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** To do this work, an agent commonly acts under its user's credentials and inherits the user's access to files and the scheduler.

**证据证明什么。** It concludes with a research agenda and a plan for an empirical benchmark, TaskBound.

**证据没有证明什么。** The immediate question is not whether all HPC agents are unsafe. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18485v1#S5.SS1 — 5.1 Shared parallel-filesystem poisoning; https://arxiv.org/html/2607.18485v1#S4 — 4 Threat Model: The Hijacked Authorized Agent。Evaluation：https://arxiv.org/html/2607.18485v1#S7.SS2 — 7.2 Toward a benchmark: TaskBound。Limitations / counterevidence：https://arxiv.org/html/2607.18485v1#S4 — 4 Threat Model: The Hijacked Authorized Agent; https://arxiv.org/html/2607.18485v1#S8 — 8 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：The immediate question is not whether all HPC agents are unsafe.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18485:end -->

<!-- review:SF-2026-ARXIV-2607-18496:start -->
### Towards an Automated Test of LLM Security Knowledge

<!-- claim:SF-2026-ARXIV-2607-18496:start -->Large language models (LLMs) are increasingly used for a range of software, hardware and human-centered security tasks. Consequently, LLM performance on security tasks is an active area of measurement and research, often with a focus on identifying areas in which LLM security "knowledge" may be insufficient. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18496:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language models (LLMs) are increasingly used for a range of software, hardware and human-centered security tasks.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We introduce a partially-automated method for assessing LLM knowledge of a security area.

**证据证明什么。** We demonstrate the method for 2 security topics, identity theft and impostor scams, and 5 LLMs in 2 leading LLM families, Gemini and GPT, using publicly available information about identity theft and impostor scams from 6 CPAs.

**证据没有证明什么。** This method does not rely on labeled data and can be implemented by a generalist as it requires only authoritative information, for example, publicly available information from Consumer Protection Agencies. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18496v1#S2 — 2. Data and Methodology。Evaluation：https://arxiv.org/html/2607.18496v1#S3.SS1 — 3.1. Case Study: Impostor Scams; https://arxiv.org/html/2607.18496v1#S3.SS2 — 3.2. Case Study: Identity Theft。Limitations / counterevidence：https://arxiv.org/html/2607.18496v1#S4 — 4. Failure Modes, Generalizability and Abuse; https://arxiv.org/html/2607.18496v1#S5 — 5. Conclusion and Open Problems。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：This method does not rely on labeled data and can be implemented by a generalist as it requires only authoritative information, for example, publicly available information from Consumer Protection Agencies.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18496:end -->

<!-- review:SF-2026-ARXIV-2607-18508:start -->
### Style over Substance: A Shortcut Audit of Emotion-Description Preference Evaluation

<!-- claim:SF-2026-ARXIV-2607-18508:start -->Preference over model-generated emotion descriptions is emerging as a standard evaluation metric for multimodal emotion understanding, exemplified by the MER2026 MER-Prefer track on EmoPrefer. Such benchmarks assume that predicting the preferred description requires grounded cross-modal understanding of the video. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18508:end -->

**为什么进入候选分母。** 摘要首要问题为“Preference over model-generated emotion descriptions is emerging as a standard evaluation metric for multimodal emotion understanding, exemplified by the MER2026 MER-Prefer track on EmoPrefer.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We conduct a systematic shortcut audit of EmoPrefer using content-blind probes.

**证据证明什么。** Instead, they show that the current scores can be reached without verifying either description against the video.

**证据没有证明什么。** These conclusions concern the data and judges tested, not what stronger models or re-annotation could recover. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18508v1#A2 — Appendix B Judge and Probe Implementation。Evaluation：https://arxiv.org/html/2607.18508v1#A1 — Appendix A Evaluation Protocol; https://arxiv.org/html/2607.18508v1#S3 — 3. Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.18508v1#S7 — 7. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/jiabingyang01/EmoPrefer-Audit, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：These conclusions concern the data and judges tested, not what stronger models or re-annotation could recover.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18508:end -->

<!-- review:SF-2026-ARXIV-2607-18532:start -->
### Reasoning Fine-Tuning Induces Persistent Latent Policy States

<!-- claim:SF-2026-ARXIV-2607-18532:start -->Reasoning-specialized language models show large performance gains over base models, yet the internal changes responsible for improved multi-step reasoning remain poorly understood. It is unclear whether reasoning fine-tuning improves local token-level competence or globally reorganizes how models structure inference over time. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18532:end -->

**为什么进入候选分母。** 摘要首要问题为“Reasoning-specialized language models show large performance gains over base models, yet the internal changes responsible for improved multi-step reasoning remain poorly understood.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** Our framework combines time-aware contrastive representation learning with discrete regime discovery to recover latent policies from activation trajectories.

**证据证明什么。** Causal interventions further show that the regimes are functionally meaningful: state-swap ablations reduce one-step predictive fit, while transplanting reasoning dynamics into base models improves performance on challenging reasoning problems.

**证据没有证明什么。** The only decrease occurs for Qwen-14B on MMLU-Pro. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18532v1#S3 — 3 Reasoning as a Switching Dynamical System; https://arxiv.org/html/2607.18532v1#S3.SS2 — 3.2 Switching Dynamical System Formulation。Evaluation：https://arxiv.org/html/2607.18532v1#A5 — Appendix E Additional Robustness and Modeling Choice Ablations; https://arxiv.org/html/2607.18532v1#A5.SS4 — E.4 Projection and inference ablations。Limitations / counterevidence：https://arxiv.org/html/2607.18532v1#S8.SS2 — 8.2 SDS-Guided Pruning of Failure-Prone Prefixes; https://arxiv.org/html/2607.18532v1#S9 — 9 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/withmartian/mi-cot, https://github.com/meta-llama/llama3/blob/main/MODEL_CARD.md, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：The only decrease occurs for Qwen-14B on MMLU-Pro.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`TRAIN-GRPO`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18532:end -->

<!-- review:SF-2026-ARXIV-2607-18548:start -->
### Engineering Trustworthy Agentic AI for Critical Systems

<!-- claim:SF-2026-ARXIV-2607-18548:start -->Agentic artificial intelligence systems, capable of autonomous perception, planning, tool use, and multi-step action, are increasingly proposed for critical engineering domains where decisions carry physical, operational, or economic consequences. This survey addresses a gap in current literature by treating trustworthiness, whether agentic behavior can be verified, audited, and trusted under the constraints that engineering practice actually requires, as a first-class engineering property, rather than evaluating agentic AI by task capability alone. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18548:end -->

**为什么进入候选分母。** 摘要首要问题为“Agentic artificial intelligence systems, capable of autonomous perception, planning, tool use, and multi-step action, are increasingly proposed for critical engineering domains where decisions carry physical, operational, or economic consequences.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** Building on this foundation, agentic systems architectures, threats, concrete trust mechanisms, and quantitative metrics are surveyed for direct application in agentic systems development and evaluation.

**证据证明什么。** Synthesizing across those domains, agentic AI trustworthiness is shown to be a single problem, with a path outlined toward a reusable, cross-domain assurance framework analogous to the graded certification regimes used by mature safety-critical engineering fields.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18548v1#S10.SS1 — X-A Emerging Design Patterns; https://arxiv.org/html/2607.18548v1#S10.SS2 — X-B Systemic Failure Modes。Evaluation：https://arxiv.org/html/2607.18548v1#S6 — VI The Evolution of AI Safety Evaluation; https://arxiv.org/html/2607.18548v1#S6.SS1 — VI-A Representation-Level Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.18548v1#S10.SS2 — X-B Systemic Failure Modes; https://arxiv.org/html/2607.18548v1#S11.SS2 — XI-B Systemic Failure Modes。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-PLATFORM`；evidence-stage relation：`structural_candidate`。
- Books 候选路由（尚非最终决定）：`Structural Candidate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18548:end -->

<!-- review:SF-2026-ARXIV-2607-18553:start -->
### Operational Proto-Introspection in Looped Language Models: Process-Quality Taps, Executable Branching, and the Readout-Control Boundary

<!-- claim:SF-2026-ARXIV-2607-18553:start -->Can a language model read the quality of its ongoing computation, and can an external intervention turn that readout into better outcomes? We test both questions in a frozen 2.6B looped transformer, Ouro-RLTT. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18553:end -->

**为什么进入候选分母。** 摘要首要问题为“Can a language model read the quality of its ongoing computation, and can an external intervention turn that readout into better outcomes?”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We test both questions in a frozen 2.6B looped transformer, Ouro-RLTT.

**证据证明什么。** Hidden-state-based scores improve risk-coverage over shortcut-only scores in four sealed selective-prediction arms, and terminal selection beats matched random even when every candidate is well formed (27/32 correct selections versus 64.8% expected; p = 0.0086).

**证据没有证明什么。** The readout–control boundary is empirical; we do not have a mechanistic account of it. • Frozen results only. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18553v1#Sx14.SSx3 — Appendix C — Tap architectures and training details; https://arxiv.org/html/2607.18553v1#Sx5.SSx6 — 4.6 Is the loop necessary? A non-looped architecture control。Evaluation：https://arxiv.org/html/2607.18553v1#Sx1 — Results at a glance; https://arxiv.org/html/2607.18553v1#Sx13.SSx4 — 12.4 The experiment queue, in priority order。Limitations / counterevidence：https://arxiv.org/html/2607.18553v1#Sx11.SSx1 — 10.1 Controls, failures, and surviving claims; https://arxiv.org/html/2607.18553v1#Sx12 — 11. Limitations。

**Artifact boundary。** Exact v1 links https://github.com/VykosMolt, https://github.com/VykosMolt/Branching-Looped-Transformer, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：The readout–control boundary is empirical; we do not have a mechanistic account of it. • Frozen results only.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-REFLECTION`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18553:end -->

<!-- review:SF-2026-ARXIV-2607-18575:start -->
### RECEIPT: Deterministic, Reward-Hacking-Resistant Verification for White-Box Agentic XSS Discovery

<!-- claim:SF-2026-ARXIV-2607-18575:start -->Cross-Site Scripting (XSS) remains one of the most prevalent and damaging classes of web vulnerabilities. LLM-based coding agents offer a promising approach to XSS discovery by combining source-code reasoning with interactive testing against a running application. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18575:end -->

**为什么进入候选分母。** 摘要首要问题为“Cross-Site Scripting (XSS) remains one of the most prevalent and damaging classes of web vulnerabilities.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** We present RECEIPT, a verification framework that makes agent-reported XSS findings trustworthy by enforcing environment isolation, PoC constraints, role separation, and verdict binding.

**证据证明什么。** Compared with the same agent using self-judgment and with black-box scanners, RECEIPT confirms more real exploits while admitting no false positives.

**证据没有证明什么。** Receipt accepts a finding only when the submitted proof of concept reproduces script execution in a victim browser under a realistic threat model, so each confirmed finding provides evidence of a real exploit rather than a reward-hacking artifact produced by an underconstrained verifier. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18575v1#S3 — III Design of Receipt Verification; https://arxiv.org/html/2607.18575v1#S3.SS1 — III-A Receipt Architecture。Evaluation：https://arxiv.org/html/2607.18575v1#S5 — V Evaluation; https://arxiv.org/html/2607.18575v1#S5.SS1 — V-A Experiment Setup。Limitations / counterevidence：https://arxiv.org/html/2607.18575v1#S6 — VI Discussion; https://arxiv.org/html/2607.18575v1#S8 — VIII Conclusion。

**Artifact boundary。** Exact v1 links https://owasp.org/www-project-benchmark/, https://projectzero.google/2024/10/from-naptime-to-big-sleep.html, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：Receipt accepts a finding only when the submitted proof of concept reproduces script execution in a victim browser under a realistic threat model, so each confirmed finding provides evidence of a real exploit rather than a reward-hacking artifact produced by an underconstrained verifier.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18575:end -->

<!-- review:SF-2026-ARXIV-2607-18577:start -->
### Attention Without Grounding: Causal Evaluation of Visual Explanations in Medical VLMs

<!-- claim:SF-2026-ARXIV-2607-18577:start -->Attention and saliency heatmaps are widely used to explain medical Vision-Language Model (VLM) outputs on chest X-rays, yet whether they truly highlight the image evidence driving predictions has not been causally tested. We audit faithfulness via overlap with radiologist bounding boxes on PadChest (n=637), attribution mass within radiologist masks on CheXlocalize (n=643), and 16x16 patch-occlusion maps that record which regions, when hidden, change the answer. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18577:end -->

**为什么进入候选分母。** 摘要首要问题为“Attention and saliency heatmaps are widely used to explain medical Vision-Language Model (VLM) outputs on chest X-rays, yet whether they truly highlight the image evidence driving predictions has not been causally tested.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Attention also misses annotated anatomy: overlap with true regions never beats shifted or random controls, and no method places more than 22% of its mass inside radiologist masks.

**证据证明什么。** These heatmaps are visually reassuring but not faithful; clinical explanations require controlled localization metrics and causal perturbation, not visual inspection alone.

**证据没有证明什么。** Fine-tuning trades consistency for text-only agreement and yields only modest grounding gains: raw-attention AMiM still leaves four fifths of mass outside the mask, and Winsor-CAM does not improve. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18577v1#S3 — 3 Methods; https://arxiv.org/html/2607.18577v1#S3.SS1 — 3.1 Models and Datasets。Evaluation：https://arxiv.org/html/2607.18577v1#S4 — 4 Experiments and Results; https://arxiv.org/html/2607.18577v1#S3.SS2 — 3.2 Evaluation Protocol。Limitations / counterevidence：https://arxiv.org/html/2607.18577v1#S5 — 5 Discussion and Conclusion; https://arxiv.org/html/2607.18577v1#S4.SS1 — 4.1 Attention Grounding Failure。

**Artifact boundary。** Exact v1 links https://github.com/thedatasense/medicalvlm_attention_without_grounding, https://huggingface.co/collections/saillab/mechanistically-guided-lora-chil-2026-69ff7afccce7547a00180b2a, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Fine-tuning trades consistency for text-only agreement and yields only modest grounding gains: raw-attention AMiM still leaves four fifths of mass outside the mask, and Winsor-CAM does not improve.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-REPRESENTATION`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18577:end -->

<!-- review:SF-2026-ARXIV-2607-18580:start -->
### STeP: Signal Temporal Logic for Precise Specifications for Action Generation with Vision Language Models

<!-- claim:SF-2026-ARXIV-2607-18580:start -->Vision-language-action (VLA) models have shown impressive generalization, but often lack interpretability and can struggle to follow precise natural language instructions that encode spatial, temporal, and logical requirements. We propose a hierarchical framework that uses Signal Temporal Logic (STL) as a shared representation connecting high-level language understanding with low-level robot execution. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18580:end -->

**为什么进入候选分母。** 摘要首要问题为“Vision-language-action (VLA) models have shown impressive generalization, but often lack interpretability and can struggle to follow precise natural language instructions that encode spatial, temporal, and logical requirements.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** We propose a hierarchical framework that uses Signal Temporal Logic (STL) as a shared representation connecting high-level language understanding with low-level robot execution.

**证据证明什么。** We evaluate the approach on a real-world tabletop domain, demonstrating how formal specifications can improve the precision, reliability, and interpretability of language-conditioned robot planning.

**证据没有证明什么。** 7 Limitations Our current implementation has several limitations. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18580v1#S4 — 4 Method; https://arxiv.org/html/2607.18580v1#S4.SS1 — 4.1 System 2: Language-to-STL Task Planning。Evaluation：https://arxiv.org/html/2607.18580v1#S5 — 5 Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.18580v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.18580v1#S7 — 7 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：7 Limitations Our current implementation has several limitations.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18580:end -->

<!-- review:SF-2026-ARXIV-2607-18603:start -->
### AutoIndex: Learning Representation Programs for Retrieval

<!-- claim:SF-2026-ARXIV-2607-18603:start -->We present AutoIndex, a framework for learning representation programs: executable transformations that map raw documents into the representations exposed to a retrieval system. Rather than tuning retrievers, rerankers, or a small set of preprocessing hyperparameters, AutoIndex searches over programs that slice, enrich, normalize, reweight, or reorganize documents before indexing. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18603:end -->

**为什么进入候选分母。** 摘要首要问题为“We present AutoIndex, a framework for learning representation programs: executable transformations that map raw documents into the representations exposed to a retrieval system.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We present AutoIndex, a framework for learning representation programs: executable transformations that map raw documents into the representations exposed to a retrieval system.

**证据证明什么。** Code to reproduce our results is available at https://github.com/auto-index/autoindex.

**证据没有证明什么。** 6.4 Limitations and Future Work AutoIndex currently optimizes primarily for Recall@100 with a fixed BM25 retriever, limited iteration budget, and small number of seeds. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18603v1#A1.SS2 — A.2 Design Decisions and Implementation Notes; https://arxiv.org/html/2607.18603v1#S6 — 6 Framework Analysis and Discussion。Evaluation：https://arxiv.org/html/2607.18603v1#S5 — 5 Experimental Results; https://arxiv.org/html/2607.18603v1#A1.SS1 — A.1 Claude Sonnet 4.6 Results。Limitations / counterevidence：https://arxiv.org/html/2607.18603v1#S6.SS4 — 6.4 Limitations and Future Work; https://arxiv.org/html/2607.18603v1#S6 — 6 Framework Analysis and Discussion。

**Artifact boundary。** Exact v1 links https://github.com/auto-index/autoindex, https://github.com/auto-index/autoindex/blob/main/query_splits.json, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：6.4 Limitations and Future Work AutoIndex currently optimizes primarily for Recall@100 with a fixed BM25 retriever, limited iteration budget, and small number of seeds.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-RAG`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18603:end -->

<!-- review:SF-2026-ARXIV-2607-18631:start -->
### Searching for Plans You Can Actually Build: A Realizability-Aware Full-Space Optimizer for MoE Training and Serving

<!-- claim:SF-2026-ARXIV-2607-18631:start -->Mixture-of-Experts (MoE) systems split a program's plan space in two: the space a cost model can rank, and the smaller space a real toolchain can actually build. Automatic optimizers rank the first and silently assume the two coincide -- so they can return a plan that is optimal on paper and impossible to emit. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18631:end -->

**为什么进入候选分母。** 摘要首要问题为“Mixture-of-Experts (MoE) systems split a program's plan space in two: the space a cost model can rank, and the smaller space a real toolchain can actually build.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** Mixture-of-Experts (MoE) systems split a program's plan space in two: the space a cost model can rank, and the smaller space a real toolchain can actually build.

**证据证明什么。** All predictions are pre-registered in a frozen, artifact-hashed adjudication file before the H800 runs, and every outcome is reported as-is.

**证据没有证明什么。** VI-D Limitations and threats to validity We state the threats ourselves, and for each we bound what it does and does not undermine. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18631v1#S3 — III Design; https://arxiv.org/html/2607.18631v1#S3.SS2 — III-B Dual-fidelity cost model。Evaluation：https://arxiv.org/html/2607.18631v1#S5 — V Evaluation; https://arxiv.org/html/2607.18631v1#S5.SS5 — V-E RQ5: Ablation and discriminative power。Limitations / counterevidence：https://arxiv.org/html/2607.18631v1#S6.SS4 — VI-D Limitations and threats to validity; https://arxiv.org/html/2607.18631v1#S6 — VI Discussion。

**Artifact boundary。** Exact v1 links https://github.com/deepseek-ai/DeepEP, https://github.com/deepseek-ai/DeepGEMM, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：VI-D Limitations and threats to validity We state the threats ourselves, and for each we bound what it does and does not undermine.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MODEL-MOE`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18631:end -->

<!-- review:SF-2026-ARXIV-2607-18639:start -->
### Mark, Don't Erase: Token Inoculation for Dual-Use Knowledge in LLMs

<!-- claim:SF-2026-ARXIV-2607-18639:start -->Safety interventions on dual-use knowledge typically choose between destroying hazardous content (e.g., unlearning, filtering) and suppressing it at the output layer (e.g., refusal training); both pay a tax in adjacent-domain competence or over-refusal. We argue that the right operation is conditioning, not reduction: we show that hazardous knowledge can be retained in the model and behaviorally gated by a privileged control token. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18639:end -->

**为什么进入候选分母。** 摘要首要问题为“Safety interventions on dual-use knowledge typically choose between destroying hazardous content (e.g., unlearning, filtering) and suppressing it at the output layer (e.g., refusal training); both pay a tax in adjacent-domain competence or over-refusal.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** Our method, Token Inoculation, introduces a binding-and-branching approach.

**证据证明什么。** We argue that the right operation is conditioning, not reduction: we show that hazardous knowledge can be retained in the model and behaviorally gated by a privileged control token.

**证据没有证明什么。** Verifying Token Inoculation under from-scratch pre-training with marking and on natively authored open-ended corpora remains important future work. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18639v1#A5 — Appendix E Cross-Architecture Details; https://arxiv.org/html/2607.18639v1#S2 — 2 Method。Evaluation：https://arxiv.org/html/2607.18639v1#A10 — Appendix J Open-Ended Format: Representation Analysis; https://arxiv.org/html/2607.18639v1#A2 — Appendix B Evaluation Details。Limitations / counterevidence：https://arxiv.org/html/2607.18639v1#S6 — 6 Discussion; https://arxiv.org/html/2607.18639v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro/blob/main/DeepSeek_V4.pdf, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Verifying Token Inoculation under from-scratch pre-training with marking and on natively authored open-ended corpora remains important future work.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-RLHF`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18639:end -->

<!-- review:SF-2026-ARXIV-2607-18659:start -->
### Broken Gates: Re-evaluating Web Bot Defenses in the Age of LLM Agents

<!-- claim:SF-2026-ARXIV-2607-18659:start -->LLM-based browser agents are rapidly changing the threat landscape for web security. Unlike traditional automation frameworks that execute predefined scripts, these agents can autonomously navigate websites, reason about page content, and interact with web interfaces using natural-language instructions. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18659:end -->

**为什么进入候选分母。** 摘要首要问题为“LLM-based browser agents are rapidly changing the threat landscape for web security.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** In this paper, we present a systematic measurement study evaluating the resilience of both interactive challenge-based defenses and non-interactive trust-based defenses against two attacker classes: commercial Captcha-solving services and LLM-based browser agents.

**证据证明什么。** Our results show that challenge-based defenses are broadly ineffective against commercial solvers, which achieve near-perfect bypass at negligible cost.

**证据没有证明什么。** 3.1 Threat Model We model an economically motivated web attacker who seeks to bypass the bot management barrier to execute a downstream automated action, such as login attempts, form submissions, or large-scale scraping. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18659v1#S4.SS4 — 4.4 Experiment Framework; https://arxiv.org/html/2607.18659v1#S3 — 3 Threat Model and Research Questions。Evaluation：https://arxiv.org/html/2607.18659v1#S5 — 5 Evaluations and Results; https://arxiv.org/html/2607.18659v1#S4 — 4 Experiments Setup。Limitations / counterevidence：https://arxiv.org/html/2607.18659v1#S3 — 3 Threat Model and Research Questions; https://arxiv.org/html/2607.18659v1#S3.SS1 — 3.1 Threat Model。

**Artifact boundary。** Exact v1 links https://github.com/browser-use/browser-use, https://github.com/FoundationAgents/OpenManus, https://github.com/nanobrowser/nanobrowser; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：3.1 Threat Model We model an economically motivated web attacker who seeks to bypass the bot management barrier to execute a downstream automated action, such as login attempts, form submissions, or large-scale scraping.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18659:end -->

<!-- review:SF-2026-ARXIV-2607-18664:start -->
### DeforM: Reasoning-Guided Physics-Aware Video Generation via Spatial-Temporal Masking

<!-- claim:SF-2026-ARXIV-2607-18664:start -->Video generation models achieve high visual quality but often struggle to generate physics-aware videos. Unlike rigid-body motion, which can be described by explicit trajectories or formulas, complex deformation dynamics remain challenging to synthesize. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18664:end -->

**为什么进入候选分母。** 摘要首要问题为“Video generation models achieve high visual quality but often struggle to generate physics-aware videos.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** In this paper, we propose DeforM, a reasoning-guided image-to-video generation framework that directs the model's focus toward physics-critical regions.

**证据证明什么。** Experimental results demonstrate that DeforM improves the realism of generated deformation scenarios, outperforming baseline models in both visual quality and physical consistency.

**证据没有证明什么。** These limitations may be alleviated by future advances in grounding, reasoning, and foundation video generation. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18664v1#S3 — 3 DeforM Framework; https://arxiv.org/html/2607.18664v1#S3.SS4 — 3.4 DeforM-Injection: Training-based Method。Evaluation：https://arxiv.org/html/2607.18664v1#Pt0.A3 — Appendix C Details of Evaluation; https://arxiv.org/html/2607.18664v1#S4 — 4 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.18664v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://nemosunny.github.io/DeforM-ProjectPage/, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：These limitations may be alleviated by future advances in grounding, reasoning, and foundation video generation.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-GENERATIVE-PARADIGMS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18664:end -->

<!-- review:SF-2026-ARXIV-2607-18665:start -->
### SciHazard: A Benchmark for Measuring Scientific Safety Risks with Decomposed Harm Scoring

<!-- claim:SF-2026-ARXIV-2607-18665:start -->Large language models (LLMs) increasingly support science, but they can also convert hazardous scientific knowledge into actionable misuse guidance. Existing benchmarks often rely on templated queries disconnected from real-world hazards, and employ LLM-as-a-Judge paradigms without domain grounding. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18665:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language models (LLMs) increasingly support science, but they can also convert hazardous scientific knowledge into actionable misuse guidance.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** To address this, we introduce SciHazard, a real-world-grounded benchmark for scientific risks and a dataset agnostic evaluation framework for measuring harmfulness.

**证据证明什么。** An expert-validation study shows that \textsc{DeHarm-Score} improves agreement with expert annotations by 90.17\% over the strongest baseline.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18665v1#A11.SS2 — K.2 Design Rationale: Decomposition into Executability and Net-New Risk; https://arxiv.org/html/2607.18665v1#A3 — Appendix C Overview of Baseline Methods。Evaluation：https://arxiv.org/html/2607.18665v1#S6 — 6 Experimental Results and Analysis; https://arxiv.org/html/2607.18665v1#A8 — Appendix H More results from the perturbation experiment。Limitations / counterevidence：https://arxiv.org/html/2607.18665v1#A12 — Appendix L Limitations and Future Work; https://arxiv.org/html/2607.18665v1#A11 — Appendix K Additional Discussion。

**Artifact boundary。** Exact v1 links https://github.com/bytedance/deer-flow, https://github.com/ScienceOne-AI/S1-DeepResearch, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18665:end -->

<!-- review:SF-2026-ARXIV-2607-18673:start -->
### MissingBench-Verified: Probing Vision-Language Models' Inability to Detect Missing Object Parts

<!-- claim:SF-2026-ARXIV-2607-18673:start -->Vision Language Models (VLMs) are well known for hallucinating non-existent objects in images. Objects with missing parts present a unique challenge for VLMs, stemming from both real-world knowledge bias and the scarcity of such images in training data. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18673:end -->

**为什么进入候选分母。** 摘要首要问题为“Vision Language Models (VLMs) are well known for hallucinating non-existent objects in images.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We present MissingBench-Verified, a benchmark designed to evaluate a specific and practically relevant scenario: when vision-language models fail to recognize that an essential component of an object has been removed.

**证据证明什么。** We find that existing mitigation strategies, including tool-assisted verification, autonomous visual reasoning, longer reasoning durations, and fine-tuning on an easier dataset, provide negligible improvement, indicating that this failure mode cannot be addressed through current prompting or post-hoc correction techniques.

**证据没有证明什么。** Another limitation is that we did not explore hallucination-specific training-based mitigation strategies. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18673v1#S2 — 2 Methods; https://arxiv.org/html/2607.18673v1#S3.SS2 — 3.2 Results of Object Detection Models。Evaluation：https://arxiv.org/html/2607.18673v1#S2.SS2 — 2.2 Evaluation and Metrics; https://arxiv.org/html/2607.18673v1#S3 — 3 Results。Limitations / counterevidence：https://arxiv.org/html/2607.18673v1#S4 — 4 Limitations and Furture Work; https://arxiv.org/html/2607.18673v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Another limitation is that we did not explore hallucination-specific training-based mitigation strategies.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18673:end -->

<!-- review:SF-2026-ARXIV-2607-18684:start -->
### When to Trust the Map: Confidence-Aware LLM Routing for Automotive CVE-to-ATM Mapping

<!-- claim:SF-2026-ARXIV-2607-18684:start -->Public CVE descriptions report the technical conditions and impact of vulnerabilities, whereas the Auto-ISAC Automotive Threat Matrix (ATM) expresses an adversary's tactics and techniques. Because the two representations are not directly aligned, incorrect automated mappings in safety-critical environments may distort threat interpretation and mitigation prioritization, motivating a confidence-aware approach that distinguishes auto-confirmable mappings from uncertain cases. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18684:end -->

**为什么进入候选分母。** 摘要首要问题为“Public CVE descriptions report the technical conditions and impact of vulnerabilities, whereas the Auto-ISAC Automotive Threat Matrix (ATM) expresses an adversary's tactics and techniques.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** These results show that the framework can support selective automation by isolating auto-confirmable mappings from those requiring analyst review.

**证据证明什么。** These results show that the framework can support selective automation by isolating auto-confirmable mappings from those requiring analyst review.

**证据没有证明什么。** Larger datasets and analyst field study in the REVIEW tier remain future work. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18684v1#S4 — 4 Methodology; https://arxiv.org/html/2607.18684v1#S4.SS1 — 4.1 System Overview。Evaluation：https://arxiv.org/html/2607.18684v1#S6 — 6 Results; https://arxiv.org/html/2607.18684v1#S6.SS1 — 6.1 Main Results。Limitations / counterevidence：https://arxiv.org/html/2607.18684v1#S7 — 7 Discussion; https://arxiv.org/html/2607.18684v1#S8 — 8 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/jayaratned/AutomotiveTD, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：Larger datasets and analyst field study in the REVIEW tier remain future work.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`INFER-SCHEDULING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18684:end -->

<!-- review:SF-2026-ARXIV-2607-18709:start -->
### RoboInter1.5: A Holistic Intermediate Representation Suite for Embodied World Modeling and Robotic Manipulation

<!-- claim:SF-2026-ARXIV-2607-18709:start -->Existing robot datasets remain expensive to curate, embodiment-specific, and insufficiently annotated with the fine-grained structure required for generalizable reasoning, execution, or long-horizon environment dynamics simulation. Building on our prior work, RoboInter1.0, we present RoboInter1.5, an extended and holistic suite of intermediate representations for both robotic manipulation and embodied world modeling. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18709:end -->

**为什么进入候选分母。** 摘要首要问题为“Existing robot datasets remain expensive to curate, embodiment-specific, and insufficiently annotated with the fine-grained structure required for generalizable reasoning, execution, or long-horizon environment dynamics simulation.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** Building on our prior work, RoboInter1.0, we present RoboInter1.5, an extended and holistic suite of intermediate representations for both robotic manipulation and embodied world modeling.

**证据证明什么。** Extensive evaluations demonstrate that RoboInter1.5 provides a unified spatiotemporal scaffolding for intermediate representations.

**证据没有证明什么。** As its core, RoboInter-Data provides over 230k episodes with dense, per-frame annotations, establishing a new standard of scale and quality for real-world manipulation datasets. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18709v1#S4 — 4 Method; https://arxiv.org/html/2607.18709v1#S2.SS2 — 2.2 Embodied reasoning and world modeling for actions.。Evaluation：https://arxiv.org/html/2607.18709v1#S5 — 5 Benchmarking and Experiments; https://arxiv.org/html/2607.18709v1#A1.SS4 — A.4 Additional Qualitative results on RoboInter-VLA。Limitations / counterevidence：https://arxiv.org/html/2607.18709v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/InternRobotics/RoboInter, https://huggingface.co/datasets/InternRobotics/RoboInter-Data, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：As its core, RoboInter-Data provides over 230k episodes with dense, per-frame annotations, establishing a new standard of scale and quality for real-world manipulation datasets.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18709:end -->

<!-- review:SF-2026-ARXIV-2607-18711:start -->
### LLM-Based Invariant Testing for Software Functional Bugs

<!-- claim:SF-2026-ARXIV-2607-18711:start -->Manually writing unit tests to uncover functional bugs in software libraries is not only time-consuming but also requires a deep understanding of the intended semantics of the APIs. Heuristic-based test generation methods suffer from low usability because they cannot reason about program semantics or interpret source code and documentation as humans do. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18711:end -->

**为什么进入候选分母。** 摘要首要问题为“Manually writing unit tests to uncover functional bugs in software libraries is not only time-consuming but also requires a deep understanding of the intended semantics of the APIs.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** To overcome these limitations, we present LISA, a novel LLM-based invariant testing framework for software functional bugs.

**证据证明什么。** LISA iteratively generates API sequences and program invariants guided by API n-gram feedback, achieving higher bug-detection rates and competitive code coverage compared with both fuzzing and prior LLM-based test generation approaches, and reporting each finding as a high-confidence bug candidate for developer confirmation.

**证据没有证明什么。** VI-B Threats to Validity and Limitations We organize the residual threats along the standard three axes. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18711v1#A3 — Appendix C Design and Measurement Notes; https://arxiv.org/html/2607.18711v1#S3 — III Methodology。Evaluation：https://arxiv.org/html/2607.18711v1#S5 — V Results and Analysis; https://arxiv.org/html/2607.18711v1#S4 — IV Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.18711v1#S6 — VI Discussion and Future Work; https://arxiv.org/html/2607.18711v1#S6.SS2 — VI-B Threats to Validity and Limitations。

**Artifact boundary。** Exact v1 links https://github.com/SecurityLab-UCD/CNTG, https://github.com/SecurityLab-UCD/CGNTG, https://github.com/DaveGamble/cJSON; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：VI-B Threats to Validity and Limitations We organize the residual threats along the standard three axes.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`principle_reuse`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18711:end -->

<!-- review:SF-2026-ARXIV-2607-18715:start -->
### DWM: Separating World Effects from Actions in Latent World Models

<!-- claim:SF-2026-ARXIV-2607-18715:start -->Latent world models underpin much of modern model-based control, yet current action-conditioned formulations supervise the next-latent transition with a single, undifferentiated target, forcing a monolithic learning signal to absorb every source of state change. In real world, however, transitions arise from two heterogeneous sources: an action-driven component induced by the agent, and an action-invariant world effect -- the change that would still occur under a null action, dictated by the environment's intrinsic dynamics (e.g., gravity-driven sliding, inertia, contact rebound, and persistent drift). 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18715:end -->

**为什么进入候选分母。** 摘要首要问题为“Latent world models underpin much of modern model-based control, yet current action-conditioned formulations supervise the next-latent transition with a single, undifferentiated target, forcing a monolithic learning signal to absorb every source of state change.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We introduce DWM (Decomposed World Model), a supervision-level framework that operationalizes this decomposition.

**证据证明什么。** DWM matches strong baselines on the flat counterparts and delivers a mean absolute improvement of 13.1% in CEM planning success across the W-variants.

**证据没有证明什么。** 6 Conclusion We identified a supervision-level limitation of action-conditioned latent world models: their next-latent transition is treated as a single, undifferentiated target, fusing action-driven and action-invariant components into one learning signal. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18715v1#S4 — 4 DWM: World/Action Disentanglement for Latent World Models。Evaluation：https://arxiv.org/html/2607.18715v1#S5.SS1 — 5.1 Benchmarks and Experimental Setup; https://arxiv.org/html/2607.18715v1#S5 — 5 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.18715v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：6 Conclusion We identified a supervision-level limitation of action-conditioned latent world models: their next-latent transition is treated as a single, undifferentiated target, fusing action-driven and action-invariant components into one learning signal.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18715:end -->

<!-- review:SF-2026-ARXIV-2607-18722:start -->
### Stale but Stable: Staleness-Adaptive Trust Regions for Stabilizing Asynchronous Reinforcement Learning

<!-- claim:SF-2026-ARXIV-2607-18722:start -->Asynchronous reinforcement learning improves throughput by decoupling rollout generation from optimization, but the resulting staleness is an inevitable byproduct, compounded jointly by policy lag, engine delays, and mixture-of-experts routing. From a trust-region perspective, this mismatch is critical: in the finite-horizon improvement bound, training-inference divergence governs the approximation error, whereas PPO clipping only gates sampled outward updates and therefore acts as a sampled surrogate rather than a full-policy constraint. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18722:end -->

**为什么进入候选分母。** 摘要首要问题为“Asynchronous reinforcement learning improves throughput by decoupling rollout generation from optimization, but the resulting staleness is an inevitable byproduct, compounded jointly by policy lag, engine delays, and mixture-of-experts routing.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We introduce the Staleness-Adaptive Trust Region (SAT), which uses the detached sampled log-ratio as a practical staleness proxy, identifies the high-mismatch tail within each batch through Staleness-based kernel function scaling, and contracts only the sign-selected endpoint of the nominal PPO interval using Effective contraction factors.

**证据证明什么。** More broadly, the results indicate that aligning the clip interval with observed staleness heterogeneity is an effective way to stabilize the reported asynchronous regime.

**证据没有证明什么。** PPO does not impose such a bound and instead clips an advantage-dependent sampled surrogate. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18722v1#A5 — Appendix E How Does Each Stability Approach Work in Async RL?。Evaluation：https://arxiv.org/html/2607.18722v1#A6 — Appendix F Experimental Details; https://arxiv.org/html/2607.18722v1#S5 — 5 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.18722v1#S6 — 6 Limitations and Open Questions; https://arxiv.org/html/2607.18722v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/Tencent-Hunyuan/GradLoc, https://github.com/THUDM/slime, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：PPO does not impose such a bound and instead clips an advantage-dependent sampled surrogate.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`TRAIN-GRPO`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18722:end -->

<!-- review:SF-2026-ARXIV-2607-18754:start -->
### AgentDebugX: An Open-Source Toolkit for Failure Observability, Attribution, and Recovery in LLM Agents

<!-- claim:SF-2026-ARXIV-2607-18754:start -->LLM agent failures are difficult to debug because the step where an error surfaces is often not the one that caused it. Existing observability tools replay execution traces but provide little support for identifying the root cause or translating diagnosis into recovery. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18754:end -->

**为什么进入候选分母。** 摘要首要问题为“LLM agent failures are difficult to debug because the step where an error surfaces is often not the one that caused it.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** We present AgentDebugX, an open-source debugging framework that organizes debugging as a closed loop of Detect, Attribute, Recover, and Rerun.

**证据证明什么。** On the Who and When benchmark, DeepDebug achieves the best strict attribution accuracy among the evaluated methods on both tested open-weight backbones, reaching 28.8 percent exact agent-and-step accuracy on qwen3.5-9b versus 21.7 percent for the strongest single-pass baseline.

**证据没有证明什么。** A fixed taxonomy cannot anticipate every long-tail error, so AgentDebugX proposes extensions for human review: when the judge meets a recurring failure outside the seed set it records a novel-mode candidate, and an inducer collects such residuals, clusters them (label, then lexical or embedding similarity, gated by a support threshold), proposes one candidate mode per cluster, and deduplicates against the seed. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18754v1#A1 — Appendix A System and Prompt Details; https://arxiv.org/html/2607.18754v1#S3 — 3 System Overview。Evaluation：https://arxiv.org/html/2607.18754v1#A3 — Appendix C Evaluation Protocol; https://arxiv.org/html/2607.18754v1#S4 — 4 Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.18754v1#A5 — Appendix E Limitations; https://arxiv.org/html/2607.18754v1#S3.SS4 — 3.4 Extensible Failure Taxonomy。

**Artifact boundary。** Exact v1 links https://github.com/AgentDebugX/AgentDebugX, https://pypi.org/project/agentdebugx/, https://github.com/langfuse/langfuse; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：A fixed taxonomy cannot anticipate every long-tail error, so AgentDebugX proposes extensions for human review: when the judge meets a recurring failure outside the seed set it records a novel-mode candidate, and an inducer collects such residuals, clusters them (label, then lexical or embedding similarity, gated by a support threshold), proposes one candidate mode per cluster, and deduplicates against the seed.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-TRACE`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18754:end -->

<!-- review:SF-2026-ARXIV-2607-18759:start -->
### Relative Positions Generalize, Absolute Positions Memorize: An Implicit-Bias Account of Length Generalization in Attention

<!-- claim:SF-2026-ARXIV-2607-18759:start -->Transformers with relative positional encodings often extrapolate to sequences longer than those seen during training, whereas transformers with learned absolute encodings typically do not. This is a robust empirical regularity, and the explanations offered for it so far are chiefly about expressivity, that is, about whether a length-generalizing solution exists. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18759:end -->

**为什么进入候选分母。** 摘要首要问题为“Transformers with relative positional encodings often extrapolate to sequences longer than those seen during training, whereas transformers with learned absolute encodings typically do not.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** This is a robust empirical regularity, and the explanations offered for it so far are chiefly about expressivity, that is, about whether a length-generalizing solution exists.

**证据证明什么。** A linear-attention control shows the mechanism is specific to softmax: without normalization, training selects a min-norm interpolant that does not extrapolate.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18759v1#S5.SS2 — 5.2 Bridging to a Realistic Architecture。Evaluation：https://arxiv.org/html/2607.18759v1#A5 — Appendix E Experimental Details and Reproducibility; https://arxiv.org/html/2607.18759v1#S4 — 4 An Implicit-Bias Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.18759v1#S7 — 7 Discussion and Limitations; https://arxiv.org/html/2607.18759v1#S8 — 8 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MODEL-POSITION-ENCODING`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18759:end -->

<!-- review:SF-2026-ARXIV-2607-18785:start -->
### SkillSight: Calibrating Generic Content Bias for Skill Retrieval

<!-- claim:SF-2026-ARXIV-2607-18785:start -->As large language model agents gain access to increasingly large skill libraries, retrieving the right skill becomes critical to reliable capability selection and execution. Existing retrievers often treat skill contents as ordinary documents, overlooking their highly regular structure: shared descriptive patterns recur across many skills while providing little evidence for distinguishing the required capability. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18785:end -->

**为什么进入候选分母。** 摘要首要问题为“As large language model agents gain access to increasingly large skill libraries, retrieving the right skill becomes critical to reliable capability selection and execution.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** Based on this observation, we propose SkillSight, a training-free retrieval framework that calibrates shared background in both semantic and lexical spaces.

**证据证明什么。** In end-to-end evaluation, SkillSight achieves the best overall performance across three agent models and outperforms LLM Selection by up to 4.97 percentage points.

**证据没有证明什么。** Future work may extend background calibration to dynamically evolving skill libraries and retrieval models with jointly learned background representations. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18785v1#Sx1 — Introduction; https://arxiv.org/html/2607.18785v1#Sx2 — Related Work。Evaluation：https://arxiv.org/html/2607.18785v1#Sx3 — Analysis; https://arxiv.org/html/2607.18785v1#Sx5 — Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.18785v1#Sx6 — Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Future work may extend background calibration to dynamically evolving skill libraries and retrieval models with jointly learned background representations.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-PLATFORM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18785:end -->

<!-- review:SF-2026-ARXIV-2607-18802:start -->
### QScheduler: Adaptive Gradient Sampling for Zeroth-Order On-Device Training on INT8 NPUs

<!-- claim:SF-2026-ARXIV-2607-18802:start -->Zeroth-Order (ZO) optimization enables On-Device Learning (ODL) on NPU-equipped microcontrollers by estimating gradients through forward passes alone, bypassing the need for backpropagation primitives and reducing memory requirements. The number of gradient samples q critically affects training: insufficient samples produce noisy gradients that plateau early, while excessive samples consume more computational resources. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18802:end -->

**为什么进入候选分母。** 摘要首要问题为“Zeroth-Order (ZO) optimization enables On-Device Learning (ODL) on NPU-equipped microcontrollers by estimating gradients through forward passes alone, bypassing the need for backpropagation primitives and reducing memory requirements.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** The number of gradient samples q critically affects training: insufficient samples produce noisy gradients that plateau early, while excessive samples consume more computational resources.

**证据证明什么。** Experiments on EuroSAT and STL-10 show that QScheduler matches well-tuned fixed-q configurations for both ResNet18 and MobileNetV2, without requiring prior q hyperparameter optimization.

**证据没有证明什么。** This suggests that beyond a certain point, the inherent approximation error of the ZO method (not the number of samples ) becomes the limiting factor. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18802v1#S3 — III Methodology; https://arxiv.org/html/2607.18802v1#S3.SS4 — III-D On-Device Implementation。Evaluation：https://arxiv.org/html/2607.18802v1#S3.SS3 — III-C Experimental Setup; https://arxiv.org/html/2607.18802v1#S4 — IV Results。Limitations / counterevidence：https://arxiv.org/html/2607.18802v1#S5 — V Discussion; https://arxiv.org/html/2607.18802v1#S6 — VI Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/STMicroelectronics/stm32ai-modelzoo, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：This suggests that beyond a certain point, the inherent approximation error of the ZO method (not the number of samples ) becomes the limiting factor.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`TRAIN-DISTRIBUTED-TRAINING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18802:end -->

<!-- review:SF-2026-ARXIV-2607-18816:start -->
### AgentTrails: Towards Trust and Reuse for Agentic Tasks

<!-- claim:SF-2026-ARXIV-2607-18816:start -->LLM-powered agents increasingly tackle complex tasks by invoking tools, querying databases, executing code, and manipulating intermediate artifacts. These agents follow trajectories that are typically stored as chronological logs, obscuring the underlying dataflow -- the dependencies between their actions and the artifacts they create and manipulate. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18816:end -->

**为什么进入候选分母。** 摘要首要问题为“LLM-powered agents increasingly tackle complex tasks by invoking tools, querying databases, executing code, and manipulating intermediate artifacts.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** We present AgentTrails, a prototype system for agent provenance and sensemaking.

**证据证明什么。** We demonstrate AgentTrails on real-world agent trajectories, showing that it reveals hidden dependencies, aligns divergent executions, and surfaces recurring tool-use patterns beyond chronological logs.

**证据没有证明什么。** Usage scenarios on SciAgentGym and Discovera traces demonstrate that the system surfaces dependency structure and workflow patterns that are not recoverable from raw sequential logs. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18816v1#S3 — 3. System Overview。Evaluation：https://arxiv.org/html/2607.18816v1#S1 — 1. Introduction; https://arxiv.org/html/2607.18816v1#S2 — 2. Related Works。Limitations / counterevidence：https://arxiv.org/html/2607.18816v1#S5 — 5. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：Usage scenarios on SciAgentGym and Discovera traces demonstrate that the system surfaces dependency structure and workflow patterns that are not recoverable from raw sequential logs.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-PLATFORM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18816:end -->

<!-- review:SF-2026-ARXIV-2607-18821:start -->
### VirtualSet: Typed Ontology Worlds as an LLM Generation Target for Grounded Queries and Guarded Decisions

<!-- claim:SF-2026-ARXIV-2607-18821:start -->Large language models increasingly read and act on enterprise data, but SQL gives a late error signal: hallucinated fields or relations can execute and return plausible wrong answers, while incorrect writes cannot be safely assessed after execution. We present VirtualSet, a live, receiver-typed ontology-world interface and generation target for LLMs. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18821:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language models increasingly read and act on enterprise data, but SQL gives a late error signal: hallucinated fields or relations can execute and return plausible wrong answers, while incorrect writes cannot be safely assessed after execution.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We present VirtualSet, a live, receiver-typed ontology-world interface and generation target for LLMs.

**证据证明什么。** On a frozen 1,072-question split, VirtualSet achieves 67.5% accuracy versus 63.5% for glossary-matched direct SQL with repair and voting (+4.0 points; McNemar exact p = 0.00117) using deepseek-reasoner.

**证据没有证明什么。** Fourth, the write-chain evidence is corpus-scale, not benchmark-scale. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18821v1#S6 — 6 Evaluation Design; https://arxiv.org/html/2607.18821v1#A1.SS6 — A.6 Model Checkpoint Replication。Evaluation：https://arxiv.org/html/2607.18821v1#S6 — 6 Evaluation Design; https://arxiv.org/html/2607.18821v1#S7 — 7 Results。Limitations / counterevidence：https://arxiv.org/html/2607.18821v1#A1.SS2 — A.2 Future this; https://arxiv.org/html/2607.18821v1#S10 — 10 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Fourth, the write-chain evidence is corpus-scale, not benchmark-scale.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-WORKFLOW`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18821:end -->

<!-- review:SF-2026-ARXIV-2607-18826:start -->
### Cross-Agent Campaign Attribution: Linking Asynchronous Attacks Across LLM Agents

<!-- claim:SF-2026-ARXIV-2607-18826:start -->LLM-agent defenses are typically evaluated one session at a time. In deployment, however, attacks can be distributed across independent agents, teams, and runtimes, leaving each local guardrail with only a sparse fragment. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18826:end -->

**为什么进入候选分母。** 摘要首要问题为“LLM-agent defenses are typically evaluated one session at a time.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** We introduce Asynchronous Attribution Fingerprint Vectors ($A^2FV$), a lightweight proxy-side reference protocol for scoring pairwise campaign similarity from proxy-observable tool-use, timing, and prompt residue.

**证据证明什么。** Crossed-style controls show that the signal is partly style-sensitive but not reducible to style alone.

**证据没有证明什么。** The proxy can rank or cluster sessions even when individual sessions are not independently classified as unsafe. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18826v1#A6 — Appendix F Second Native-Framework Probe: LangGraph Traces; https://arxiv.org/html/2607.18826v1#S3 — 3 Method。Evaluation：https://arxiv.org/html/2607.18826v1#S4.SS2 — 4.2 Experimental Protocol and Main Results; https://arxiv.org/html/2607.18826v1#A3 — Appendix C Supplementary Evaluation Tables。Limitations / counterevidence：https://arxiv.org/html/2607.18826v1#A7 — Appendix G A 2 FV Qualitative Outcomes and Failure Modes; https://arxiv.org/html/2607.18826v1#S3.SS1 — 3.1 Problem Setup and Threat Model。

**Artifact boundary。** Exact v1 links https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro, https://huggingface.co/google/gemma-4-31B-it, https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：The proxy can rank or cluster sessions even when individual sessions are not independently classified as unsafe.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18826:end -->

<!-- review:SF-2026-ARXIV-2607-18828:start -->
### Evaluating medical AI under missing information: same-provider judges and human raters change apparent safety

<!-- claim:SF-2026-ARXIV-2607-18828:start -->Readiness stress-testing of medical AI has focused on closed-ended and multimodal benchmarks. We extend it to open-ended clinical conversation under missing information, where safe behavior means recognizing absent information and qualifying, clarifying, or not over-committing - and where the evaluator becomes part of the measurement. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18828:end -->

**为什么进入候选分母。** 摘要首要问题为“Readiness stress-testing of medical AI has focused on closed-ended and multimodal benchmarks.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We extend it to open-ended clinical conversation under missing information, where safe behavior means recognizing absent information and qualifying, clarifying, or not over-committing - and where the evaluator becomes part of the measurement.

**证据证明什么。** We release the harness, prompts, per-item outputs, judge panel, perturbation audit, and human-annotation protocol.

**证据没有证明什么。** On the axis that governs safety (declining to over-commit when information is missing), it is improved but not solved, and the residual failure rate is large relative to any acceptable clinical error budget only if one accepts a prespecified threshold — which we do not set here, so we report the rate (roughly 1 in 12 to 1 in 3 depending on model, modality, and judge) rather than grade it. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18828v1#Sx1.SSx3 — 2. Methods; https://arxiv.org/html/2607.18828v1#Sx1.SSx12 — Appendix E. Supplementary robustness tables (all four models)。Evaluation：https://arxiv.org/html/2607.18828v1#Sx1.SSx4 — 3. Results。Limitations / counterevidence：https://arxiv.org/html/2607.18828v1#Sx1.SSx11 — Appendix D. Example failures (open-ended probe); https://arxiv.org/html/2607.18828v1#Sx1.SSx5 — 4. Discussion。

**Artifact boundary。** Exact v1 links https://github.com/KAVentures/health-ai-readiness-robustness, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：On the axis that governs safety (declining to over-commit when information is missing), it is improved but not solved, and the residual failure rate is large relative to any acceptable clinical error budget only if one accepts a prespecified threshold — which we do not set here, so we report the rate (roughly 1 in 12 to 1 in 3 depending on model, modality, and judge) rather than grade it.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18828:end -->

<!-- review:SF-2026-ARXIV-2607-18840:start -->
### WorldScape Policy 2.0: Empowering Steerable World Action Modeling with Reasoning-Augmented Memory

<!-- claim:SF-2026-ARXIV-2607-18840:start -->World Action Models (WAMs) offer a promising paradigm for robotic manipulation by jointly modeling visual state transitions and robot actions. However, existing WAMs are constrained by limited temporal context, coarse episode-level language supervision, and predominantly text-only conditioning, which hinder task-progress tracking and fine-grained language-video-action grounding while limiting visual-context reasoning and cross-embodiment transfer. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18840:end -->

**为什么进入候选分母。** 摘要首要问题为“World Action Models (WAMs) offer a promising paradigm for robotic manipulation by jointly modeling visual state transitions and robot actions.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** In this paper, we introduce WorldScape Policy 2.0, a controllable WAM with reasoning-augmented long short-term memory.

**证据证明什么。** Experiments in both simulation and real-world platforms demonstrate superior capabilities in long-horizon autonomous planning, fine-grained instruction following and in-context adaptation.

**证据没有证明什么。** These results advance WAMs from passive future prediction toward memory-grounded and multimodally controllable manipulation. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18840v1#S3 — 3 Method; https://arxiv.org/html/2607.18840v1#S2.SS1 — 2.1 World Action Models for Robotic Manipulation。Evaluation：https://arxiv.org/html/2607.18840v1#S4.SS1 — 4.1 Benchmark Setup and Evaluation Protocol; https://arxiv.org/html/2607.18840v1#S4.SS3 — 4.3 Simulation Benchmark Results。Limitations / counterevidence：https://arxiv.org/html/2607.18840v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：These results advance WAMs from passive future prediction toward memory-grounded and multimodally controllable manipulation.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18840:end -->

<!-- review:SF-2026-ARXIV-2607-18847:start -->
### Data Leakage Prevention in Agentic Applications via Preemptive Hardening

<!-- claim:SF-2026-ARXIV-2607-18847:start -->Agentic systems integrate LLM driven planning with interfaces to external tools, making data leakage and tool misuse feasible via instruction/data boundary failures and prompt injection attacks. Enforcing required controls consistently is particularly challenging in workflows spanning many codebases and heterogeneous agents. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18847:end -->

**为什么进入候选分母。** 摘要首要问题为“Agentic systems integrate LLM driven planning with interfaces to external tools, making data leakage and tool misuse feasible via instruction/data boundary failures and prompt injection attacks.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** To address this challenge in multi agentic systems, we present a pre-deployment pipeline for scanning, hardening, and validation of agentic applications.

**证据证明什么。** The resulting modifications of application code were shown to eliminate leaks when targeted by basic jailbreak and instruction-override attacks, achieving a 100% reduction in leakage, and reduce leaks by 91% under conditions of stress-induced manipulation, without the need of continuous runtime policy enforcement.

**证据没有证明什么。** A few limitations still remain: stress-framed prompts are reduced but not eliminated, schema-preserving tampering of inter-agent artifacts evades our structural checks, and multi-user deployments require stronger authorization and context isolation than we currently enforce. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18847v1#S3 — III Methodology; https://arxiv.org/html/2607.18847v1#S3.SS2 — III-B Threat Model。Evaluation：https://arxiv.org/html/2607.18847v1#S4 — IV Evaluation; https://arxiv.org/html/2607.18847v1#S4.SS1 — IV-A Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.18847v1#S3.SS2 — III-B Threat Model; https://arxiv.org/html/2607.18847v1#S6 — VI Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：A few limitations still remain: stress-framed prompts are reduced but not eliminated, schema-preserving tampering of inter-agent artifacts evades our structural checks, and multi-user deployments require stronger authorization and context isolation than we currently enforce.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18847:end -->

<!-- review:SF-2026-ARXIV-2607-18859:start -->
### PhoenixRepair: Rethinking Repair Strategy Exploration in Software Agents

<!-- claim:SF-2026-ARXIV-2607-18859:start -->While Large Language Models have greatly advanced automated issue resolution, existing agent-based methods exhibit a fundamental limitation in their insufficient exploration of repair strategies. This insufficiency manifests in two key aspects. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18859:end -->

**为什么进入候选分母。** 摘要首要问题为“While Large Language Models have greatly advanced automated issue resolution, existing agent-based methods exhibit a fundamental limitation in their insufficient exploration of repair strategies.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** To address these challenges, we present PhoenixRepair, a multi-agent framework that systematically explores multiple candidate edit locations and performs iterative reflection and refinement on patch generation, thereby expanding the search space of repair strategies.

**证据证明什么。** Experiments on SWE-bench-Verified demonstrate that PhoenixRepair achieves the largest relative improvement of 7.8\% over SWE-agent under DeepSeek-V3.1, and attains the highest resolved rate of 76.0\% Pass@1 under MiniMax-M2.5.

**证据没有证明什么。** However, we mitigate this limitation by demonstrating consistent performance improvements across all five models, suggesting that the effectiveness of our framework is not tied to a specific model architecture. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18859v1#S2 — II Methods。Evaluation：https://arxiv.org/html/2607.18859v1#S3 — III Experiments; https://arxiv.org/html/2607.18859v1#S3.SS1 — III-A Experimental Settings。Limitations / counterevidence：https://arxiv.org/html/2607.18859v1#S5 — V Threats to Validity; https://arxiv.org/html/2607.18859v1#S6 — VI Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/DeepSoftwareAnalytics/PhoenixRepair, https://github.com/SWE-agent/mini-swe-agent, https://github.com/reworkd/AgentGPT; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：However, we mitigate this limitation by demonstrating consistent performance improvements across all five models, suggesting that the effectiveness of our framework is not tied to a specific model architecture.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-PLATFORM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18859:end -->

<!-- review:SF-2026-ARXIV-2607-18867:start -->
### HindsightBench: A Black-Box Behavioral Audit Protocol for Parametric Hindsight in Time-Indexed LLM Decision Tasks

<!-- claim:SF-2026-ARXIV-2607-18867:start -->Large language models leak parametric knowledge of what followed a historical date into decision tasks indexed by that date -- not necessarily a lookup of the realized outcome, but knowledge of the period all the same. Existence is settled; what users lack is a cheap way to audit a given model. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18867:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language models leak parametric knowledge of what followed a historical date into decision tasks indexed by that date -- not necessarily a lookup of the realized outcome, but knowledge of the period all the same.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We present HindsightBench, a black-box audit protocol that profiles parametric hindsight in any time-indexed LLM decision task at probe-level cost (no backtests, no logprobs, no corpus access).

**证据证明什么。** We release the panel, preregistrations, audit rows, transcripts, and one-command regeneration.

**证据没有证明什么。** English-only prompts on a U.S.-centric panel; corpus-culture effects on the trigger are an open question the leaderboard’s vendor spread hints at but cannot settle. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18867v1#S5 — 5 The 15-Model Leaderboard。Evaluation：https://arxiv.org/html/2607.18867v1#S1 — 1 Introduction; https://arxiv.org/html/2607.18867v1#S2 — 2 Related Work。Limitations / counterevidence：https://arxiv.org/html/2607.18867v1#S9 — 9 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/Khaozhe/hindsightbench, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：English-only prompts on a U.S.-centric panel; corpus-culture effects on the trigger are an open question the leaderboard’s vendor spread hints at but cannot settle.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18867:end -->

<!-- review:SF-2026-ARXIV-2607-18886:start -->
### TraceDev: A Traceability-Driven Multi-agent Framework for Requirement-to-Code Development

<!-- claim:SF-2026-ARXIV-2607-18886:start -->In modern software development, the rapid advancement of Large Language Models (LLMs) has made the end-to-end transformation of Natural Language Requirements (NLRs) into executable repository-level code increasingly feasible. However, existing approaches typically rely on simplified instructions (e.g., single-sentence descriptions), failing to reflect complex software development scenarios. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18886:end -->

**为什么进入候选分母。** 摘要首要问题为“In modern software development, the rapid advancement of Large Language Models (LLMs) has made the end-to-end transformation of Natural Language Requirements (NLRs) into executable repository-level code increasingly feasible.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** To address these limitations, we propose TraceDev, a multi-agent framework for automated software development grounded in use cases that contain multiple functional points and complex semantics.

**证据证明什么。** These results demonstrate the effectiveness of TraceDev in repository-level code generation from requirements.

**证据没有证明什么。** However, according to related study ( Boehm, 1984 ) , coding accounts for only about 20% of the software lifecycle while maintenance occupies roughly 80%. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18886v1#S3.SS3 — 3.3. Designer Agent; https://arxiv.org/html/2607.18886v1#S4.SS4 — 4.4. Implementation Details。Evaluation：https://arxiv.org/html/2607.18886v1#S2.SS1 — 2.1. Inadequacy of Existing Benchmarks for Complex Development Scenarios; https://arxiv.org/html/2607.18886v1#S4 — 4. Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.18886v1#S5.SS4 — 5.4. Threats to Validity; https://arxiv.org/html/2607.18886v1#S6 — 6. discussion。

**Artifact boundary。** Exact v1 links https://github.com/ISSE-Lab/ISSTA2026-TraceDev, https://github.com/tree-sitter/tree-sitter, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：However, according to related study ( Boehm, 1984 ) , coding accounts for only about 20% of the software lifecycle while maintenance occupies roughly 80%.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-WORKFLOW`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18886:end -->

<!-- review:SF-2026-ARXIV-2607-18915:start -->
### Reasoning Error from Known Fact: Step-Level Self-Consistency Group Relative Policy Optimization for LLM

<!-- claim:SF-2026-ARXIV-2607-18915:start -->With the rapid advancement of large language models (LLMs), modern systems not only possess strong foundational capabilities and extensive knowledge, but can also solve complex problems via long, multi-step reasoning. However, as reasoning traces become longer, LLMs may produce a substantial amount of hallucinated content during the reasoning process, which is often difficult to detect. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18915:end -->

**为什么进入候选分母。** 摘要首要问题为“With the rapid advancement of large language models (LLMs), modern systems not only possess strong foundational capabilities and extensive knowledge, but can also solve complex problems via long, multi-step reasoning.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** Compared with prior methods, SSC-GRPO achieves state-of-the-art performance on both mathematical reasoning benchmarks and hallucination leaderboards.

**证据证明什么。** Our results offer a new perspective for detecting and mitigating hallucinations in the reasoning process of large language models.

**证据没有证明什么。** Limitations Due to resource constraints, SSC-GRPO has only been evaluated on the Qwen and Llama model families at the 4B and 8B scales. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18915v1#A1 — Appendix A Implementation Details of our method; https://arxiv.org/html/2607.18915v1#S4 — 4 Method: Step-Level Self-Consistency Group Relative Policy Optimization。Evaluation：https://arxiv.org/html/2607.18915v1#A4 — Appendix D Further Analysis: Context-Augmented Data Evaluation; https://arxiv.org/html/2607.18915v1#A6 — Appendix F SSC-GRPO Perfermance in Augmented Benchmarks。Limitations / counterevidence：https://arxiv.org/html/2607.18915v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.18915v1#Sx1 — Limitations。

**Artifact boundary。** Exact v1 links https://huggingface.co/datasets/inclusionAI/AReaL-boba-Data, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Limitations Due to resource constraints, SSC-GRPO has only been evaluated on the Qwen and Llama model families at the 4B and 8B scales.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`TRAIN-GRPO`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18915:end -->

<!-- review:SF-2026-ARXIV-2607-18917:start -->
### TAP-RAG: Task-Aware Policy Control for Long-Document Multimodal Question Answering

<!-- claim:SF-2026-ARXIV-2607-18917:start -->Long-document multimodal question answering requires more than retrieving relevant chunks from a large document. Different queries require different evidence behavior. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18917:end -->

**为什么进入候选分母。** 摘要首要问题为“Long-document multimodal question answering requires more than retrieving relevant chunks from a large document.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** We present TAP-RAG, a task-aware policy-controlled RAG framework for long-document multimodal QA.

**证据证明什么。** Existing multimodal RAG systems improve evidence access through text chunks, page images, graph links, or heterogeneous document elements, but they often apply a largely query-agnostic evidence-use strategy.

**证据没有证明什么。** The same-backbone comparison with RAG-Anything shows that improvements come from query-time evidence control, not a stronger generator. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18917v1#A3 — Appendix C Framework Prompt Templates; https://arxiv.org/html/2607.18917v1#S3 — 3 Method。Evaluation：https://arxiv.org/html/2607.18917v1#S4 — 4 Experiments; https://arxiv.org/html/2607.18917v1#S4.SS1 — 4.1 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.18917v1#S5 — 5 Conclusion; https://arxiv.org/html/2607.18917v1#Sx1 — Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：The same-backbone comparison with RAG-Anything shows that improvements come from query-time evidence control, not a stronger generator.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-RAG`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18917:end -->

<!-- review:SF-2026-ARXIV-2607-18924:start -->
### Learning Explicit Physical Parameter Control and Benchmarking for Video Generation

<!-- claim:SF-2026-ARXIV-2607-18924:start -->Recent advances in image-to-video generation have improved visual realism, making physically grounded and controllable dynamics an important step toward future world simulation. Current models often generate plausible motion, but it is not reliably governed by explicit physical causes, and instance-level constraints can leak or become entangled in multi-object interactions. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18924:end -->

**为什么进入候选分母。** 摘要首要问题为“Recent advances in image-to-video generation have improved visual realism, making physically grounded and controllable dynamics an important step toward future world simulation.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** To bridge this gap, we introduce PhyParam-Dataset, an interaction-centric collection of 130K physically simulated videos with dense physical parameterization, including force vectors, object material properties, and environmental constants across five representative rigid-body motion types.

**证据证明什么。** Experiments show that PhyParam improves physical consistency while maintaining high visual fidelity, advancing explicit rigid-body physical-parameter control for image-to-video generation.

**证据没有证明什么。** It does not explicitly model torque from off-center force application; it also does not cover deformable objects, fluids, cloth, fracture, soft bodies, or articulated dynamics. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18924v1#S4 — 4 Method; https://arxiv.org/html/2607.18924v1#A3 — Appendix S3 Human Evaluation Implementation Details。Evaluation：https://arxiv.org/html/2607.18924v1#A3 — Appendix S3 Human Evaluation Implementation Details; https://arxiv.org/html/2607.18924v1#A4 — Appendix S4 More Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.18924v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：It does not explicitly model torque from off-center force application; it also does not cover deformable objects, fluids, cloth, fracture, soft bodies, or articulated dynamics.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-GENERATIVE-PARADIGMS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18924:end -->

<!-- review:SF-2026-ARXIV-2607-18957:start -->
### InstantInfer: Enabling Fast LLM Cold Start with Communicating Finite Automata

<!-- claim:SF-2026-ARXIV-2607-18957:start -->Cold starts in large language model (LLM) inference services significantly affect user experience, yet they remain inefficient due to sequential initialization and a massive number of fine-grained I/O requests issued by complex software components. Although refactoring the program can yield advantages such as concurrent execution and I/O merging, this approach is error-prone and carries correctness risks when dealing with massive, heterogeneous components. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18957:end -->

**为什么进入候选分母。** 摘要首要问题为“Cold starts in large language model (LLM) inference services significantly affect user experience, yet they remain inefficient due to sequential initialization and a massive number of fine-grained I/O requests issued by complex software components.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** We propose the Communicating Finite Automata (CFA) abstraction to systematically analyze cross-component optimization opportunities, and design a programming framework to enable CFA-based component program refactoring.

**证据证明什么。** Extensive experiments demonstrate that InstantInfer substantially accelerates LLM cold starts (achieving up to 7.2 times speedup) and exhibits robustness across diverse GPUs, workloads, and scales.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18957v1#S3.SS1 — 3.1. System Model; https://arxiv.org/html/2607.18957v1#S3.SS2 — 3.2. Programming Framework and Runtime。Evaluation：https://arxiv.org/html/2607.18957v1#A3 — Appendix C Additional Burst Cold-Start Results; https://arxiv.org/html/2607.18957v1#S2.SS2 — 2.2. Problem Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.18957v1#S9 — 9. Conclusion。

**Artifact boundary。** Exact v1 links https://claude.com/product/claude-code, https://github.com/huggingface/safetensors, https://github.com/features/copilot; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-MODEL-REGISTRY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18957:end -->

<!-- review:SF-2026-ARXIV-2607-18975:start -->
### Mi-Memory: A Lifecycle Memory Framework for Personal AI

<!-- claim:SF-2026-ARXIV-2607-18975:start -->Personal AI is moving beyond chat-only interaction toward continuous services that span phones, cars, homes, wearables, cameras, and tools. In this setting, memory cannot remain a cache of prior conversations. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18975:end -->

**为什么进入候选分母。** 摘要首要问题为“Personal AI is moving beyond chat-only interaction toward continuous services that span phones, cars, homes, wearables, cameras, and tools.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** MiMemory is a step toward auditable, evidence-gated, and deployment-aware memory systems for Personal AI.

**证据证明什么。** Project homepage: https://darwin-agent.github.io/Mi-Memory/ .

**证据没有证明什么。** These compatibility observations are not a substitute for joint ablation. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18975v1#S3.SS2 — 3.2 Framework: Lifecycle Architecture and Interfaces; https://arxiv.org/html/2607.18975v1#S6.SS2 — 6.2 Method: Dual-Loop Framework for Bounded Evolution。Evaluation：https://arxiv.org/html/2607.18975v1#A6.SS2 — F.2 Experimental Configuration; https://arxiv.org/html/2607.18975v1#A8 — Appendix H Evaluation Protocol Details。Limitations / counterevidence：https://arxiv.org/html/2607.18975v1#S8.SS2 — 8.2 Cross-Module Findings and Limitations; https://arxiv.org/html/2607.18975v1#S9 — 9 Conclusion and Outlook。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：These compatibility observations are not a substitute for joint ablation.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18975:end -->

<!-- review:SF-2026-ARXIV-2607-18979:start -->
### Fishing Out Free Riders: Shapley-Based Reward Attribution for Parallel Reasoning via Reinforcement Learning

<!-- claim:SF-2026-ARXIV-2607-18979:start -->Large Language Models (LLMs) excel at multi-step reasoning, yet current parallel reasoning approaches often fail to distinguish the contributions of individual reasoning paths. Many paths may be redundant, misleading, or even detrimental, but outcome-level rewards assign uniform reward, leading to ambiguous learning signals and unstable training. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18979:end -->

**为什么进入候选分母。** 摘要首要问题为“Large Language Models (LLMs) excel at multi-step reasoning, yet current parallel reasoning approaches often fail to distinguish the contributions of individual reasoning paths.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We propose Parallel Shapley, a reinforcement learning framework that attributes fine-grained, path-level contributions in multi-path reasoning.

**证据证明什么。** Experiments on mathematical reasoning benchmarks show that Parallel Shapley outperforms existing baselines while providing more stable and interpretable training.

**证据没有证明什么。** First, due to computational constraints, our experiments are conducted on Qwen3-4B-Base, and the method has not yet been evaluated on larger-scale models; we plan to extend validation to larger backbones in future work. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18979v1#A2 — Appendix B Evaluation Prompt for Path-subset in Generative Reward Model; https://arxiv.org/html/2607.18979v1#A7 — Appendix G The Use of Large Language Models。Evaluation：https://arxiv.org/html/2607.18979v1#S4.SS2 — 4.2 Main Results Analysis; https://arxiv.org/html/2607.18979v1#A2 — Appendix B Evaluation Prompt for Path-subset in Generative Reward Model。Limitations / counterevidence：https://arxiv.org/html/2607.18979v1#S5 — 5 Conclusion and Future Work; https://arxiv.org/html/2607.18979v1#Sx1 — Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：First, due to computational constraints, our experiments are conducted on Qwen3-4B-Base, and the method has not yet been evaluated on larger-scale models; we plan to extend validation to larger backbones in future work.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`TRAIN-GRPO`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18979:end -->

<!-- review:SF-2026-ARXIV-2607-19022:start -->
### From Collaboration to Regulation: Characterizing Governance Practice in Three Deep Learning Open Source Communities

<!-- claim:SF-2026-ARXIV-2607-19022:start -->Collaboration in Open Source Software (OSS) projects creates substantial coordination and quality-control challenges across diverse contributor bases. Projects address these challenges through documented governance rules, yet maintainers have limited systematic guidance on what rules to codify, when to introduce or revise them, and how to organize them across documents. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19022:end -->

**为什么进入候选分母。** 摘要首要问题为“Collaboration in Open Source Software (OSS) projects creates substantial coordination and quality-control challenges across diverse contributor bases.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** We conducted a mixed-methods empirical study of three mature deep learning frameworks: PyTorch, TensorFlow, and Paddle.

**证据证明什么。** Synthesizing these findings, we derive 33 actionable governance practices for mature, large-scale OSS projects with substantial coordination demands and organizational involvement.

**证据没有证明什么。** The findings show that operational rule themes, such as contribution submission guidance and code acceptance criteria, were broadly shared and commonly documented in contributing files and templates. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19022v1#S3 — 3. Methodology; https://arxiv.org/html/2607.19022v1#S3.SS1 — 3.1. Theoretical Lens: The IAD Framework。Evaluation：https://arxiv.org/html/2607.19022v1#S4.SS2 — 4.2. Results; https://arxiv.org/html/2607.19022v1#S5.SS2 — 5.2. Results。Limitations / counterevidence：https://arxiv.org/html/2607.19022v1#S10 — 10. Conclusion; https://arxiv.org/html/2607.19022v1#S8 — 8. Discussion。

**Artifact boundary。** Exact v1 links https://octoverse.github.com/, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：The findings show that operational rule themes, such as contribution submission guidance and code acceptance criteria, were broadly shared and commonly documented in contributing files and templates.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`principle_reuse`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19022:end -->

<!-- review:SF-2026-ARXIV-2607-19033:start -->
### Content is What Remains: Invariant Speech Tokenization from Parallel Utterances

<!-- claim:SF-2026-ARXIV-2607-19033:start -->Discrete speech tokenizers aim to disentangle semantic from acoustic information, yet targets from self-supervised learning (SSL) models like HuBERT retain non-linguistic variation: speaker identity, prosody, and channel conditions leak into the tokens, inflating entropy. Our key insight is that when enough speakers utter the same words under varying conditions, linguistic content is the only shared factor. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19033:end -->

**为什么进入候选分母。** 摘要首要问题为“Discrete speech tokenizers aim to disentangle semantic from acoustic information, yet targets from self-supervised learning (SSL) models like HuBERT retain non-linguistic variation: speaker identity, prosody, and channel conditions leak into the tokens, inflating entropy.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We propose PINT (Parallel INvariant Tokenization), which fine-tunes an SSL encoder with alignment losses across parallel utterances and augmentations to distill this shared residual.

**证据证明什么。** Experiments show a 98.7% relative reduction in speaker probe accuracy (93.1% to 1.2%), a 42% lower ABX error rate, and 27-30% lower LM perplexity versus baselines, confirming that the right invariance is key to efficient learning.

**证据没有证明什么。** Future work includes multilingual extension via synthetic data, codec integration, and duration-factorized generation schemes that exploit PINT’s RLE compressibility. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19033v1#S2 — 2 Method; https://arxiv.org/html/2607.19033v1#S2.SS2 — 2.2 Model Overview。Evaluation：https://arxiv.org/html/2607.19033v1#S3 — 3 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.19033v1#S4 — 4 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/nyrahealth/PINT, https://huggingface.co/hexgrad/Kokoro-82M, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Future work includes multilingual extension via synthetic data, codec integration, and duration-factorized generation schemes that exploit PINT’s RLE compressibility.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MODEL-TOKENIZER`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19033:end -->

<!-- review:SF-2026-ARXIV-2607-19038:start -->
### FilmWorld: Agentic Novel-to-Film Generation through Dynamic Cinematic World Modeling

<!-- claim:SF-2026-ARXIV-2607-19038:start -->Translating novels into films poses a grand challenge for generative artificial intelligence, requiring conversion of abstract literary prose into long-form, multi-scene visual narratives. While current video generation models excel at short, single-scene clips within narrow temporal and spatial contexts, novel-to-film generation operates in a more complex regime, demanding long-duration content across diverse scenes with dynamically evolving entity states. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19038:end -->

**为什么进入候选分母。** 摘要首要问题为“Translating novels into films poses a grand challenge for generative artificial intelligence, requiring conversion of abstract literary prose into long-form, multi-scene visual narratives.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** To address the evaluation gap in long-form generation, we introduce FilmEval, a systematic evaluation framework that couples a difficulty-graded benchmark of 15 representative novels with an automated protocol of nine objective metrics spanning three dimensions: cinematic presentation, film consistency, and novel fidelity.

**证据证明什么。** Experiments demonstrate that FilmWorld consistently outperforms state-of-the-art video generation agent systems, with particularly pronounced improvements in narrative fidelity and cross-scene consistency.

**证据没有证明什么。** 12.1 Limitations and Future Work Despite its strong empirical performance, FilmWorld has several limitations that delineate its current boundary and point to directions for future work. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19038v1#S4 — 4 Methodology。Evaluation：https://arxiv.org/html/2607.19038v1#S11 — 11 Human Evaluation Protocol; https://arxiv.org/html/2607.19038v1#S5 — 5 Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.19038v1#S12.SS1 — 12.1 Limitations and Future Work; https://arxiv.org/html/2607.19038v1#S12 — 12 Discussion。

**Artifact boundary。** Exact v1 links https://github.com/HBAI-Ltd/Toonflow-app, https://github.com/HITsz-TMG/VideoClaw, https://github.com/HaoTone-monster/N2FBaseline; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：12.1 Limitations and Future Work Despite its strong empirical performance, FilmWorld has several limitations that delineate its current boundary and point to directions for future work.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19038:end -->

<!-- review:SF-2026-ARXIV-2607-19058:start -->
### Where Should Optimizer State Live? Tiered State Allocation for Memory-Efficient Mixture-of-Experts Training

<!-- claim:SF-2026-ARXIV-2607-19058:start -->Optimizer state is the largest single line item in the memory budget of mixture-of-experts (MoE) training. On a 6.78B-parameter MoE language model AdamW keeps 50.6 GB of first and second moments to update 12.6 GB of bfloat16 weights. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19058:end -->

**为什么进入候选分母。** 摘要首要问题为“Optimizer state is the largest single line item in the memory budget of mixture-of-experts (MoE) training.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** On a 6.78B-parameter MoE language model AdamW keeps 50.6 GB of first and second moments to update 12.6 GB of bfloat16 weights.

**证据证明什么。** Where optimizer state lives, these results suggest, matters at least as much as how much of it there is.

**证据没有证明什么。** Finally, the downstream evaluations are near chance and should be read as a completeness check, not evidence of capability. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19058v1#S3.SS0.SSS0.Px4 — Memory model.; https://arxiv.org/html/2607.19058v1#S4.SS0.SSS0.Px1 — Model.。Evaluation：https://arxiv.org/html/2607.19058v1#A4 — Appendix D Zero-shot evaluation detail; https://arxiv.org/html/2607.19058v1#S4 — 4 Experimental setup。Limitations / counterevidence：https://arxiv.org/html/2607.19058v1#S6 — 6 Limitations; https://arxiv.org/html/2607.19058v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/EleutherAI/lm-evaluation-harness, https://github.com/nuemaan/skewadam, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：Finally, the downstream evaluations are near chance and should be read as a completeness check, not evidence of capability.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`TRAIN-DISTRIBUTED-TRAINING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19058:end -->

<!-- review:SF-2026-ARXIV-2607-19096:start -->
### Supra Cognitive Modes: A Routed Architecture for Agent Memory

<!-- claim:SF-2026-ARXIV-2607-19096:start -->Agent-memory workloads mix direct factual lookup, relation-chain and current-state reasoning, and broad synthesis over long histories. We describe Supra Cognitive Modes (SCM), an architecture that maps explicit or automatically selected per-query modes to retrieval and synthesis payloads over one shared ingest substrate. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19096:end -->

**为什么进入候选分母。** 摘要首要问题为“Agent-memory workloads mix direct factual lookup, relation-chain and current-state reasoning, and broad synthesis over long histories.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We describe Supra Cognitive Modes (SCM), an architecture that maps explicit or automatically selected per-query modes to retrieval and synthesis payloads over one shared ingest substrate.

**证据证明什么。** The results characterize one implemented routed configuration and its diagnostic failure patterns, while source inspection verifies the per-query control interface and shared-substrate design.

**证据没有证明什么。** More importantly, a constant offset cannot recover the missing per-question Stage-3 time for LoCoMo and LongMem. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19096v1#S3 — 3 System Design; https://arxiv.org/html/2607.19096v1#A1 — Appendix A Methodology details。Evaluation：https://arxiv.org/html/2607.19096v1#A4.SS1 — D.1 Benchmark fixture sizes; https://arxiv.org/html/2607.19096v1#A4.SS4 — D.4 Existing-output error-analysis frame。Limitations / counterevidence：https://arxiv.org/html/2607.19096v1#A4.SS5 — D.5 Vector-store and synthesis-probe limitations; https://arxiv.org/html/2607.19096v1#S4.SS9 — 4.9 Threat from benchmark contamination。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：More importantly, a constant offset cannot recover the missing per-question Stage-3 time for LoCoMo and LongMem.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19096:end -->

<!-- review:SF-2026-ARXIV-2607-19102:start -->
### Enabling Multi-Dimensional Distributed Trace Comparison with Contrast

<!-- claim:SF-2026-ARXIV-2607-19102:start -->Diagnosis using distributed traces is fundamentally a comparative task: operators seek to understand how an anomalous execution differs from expected behavior, how a deployment changes system execution, or how two individual executions differ. Trace comparison is challenging because useful differences between executions can manifest across multiple dimensions, and no single diagnostic interface is effective at capturing all of them. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19102:end -->

**为什么进入候选分母。** 摘要首要问题为“Diagnosis using distributed traces is fundamentally a comparative task: operators seek to understand how an anomalous execution differs from expected behavior, how a deployment changes system execution, or how two individual executions differ.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** This paper presents Contrast, a system for multi-dimensional comparative trace analysis.

**证据证明什么。** We demonstrate the effectiveness and efficiency of Contrast through controlled experiments on traces from DeathStarBench and evaluation on production traces from Uber.

**证据没有证明什么。** Exploring alternative modalities represents an interesting direction for future work. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19102v1#S3 — 3. Contrast Design。Evaluation：https://arxiv.org/html/2607.19102v1#S5 — 5. Trace Comparison Benchmark; https://arxiv.org/html/2607.19102v1#S6 — 6. Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.19102v1#S8 — 8. Discussion; https://arxiv.org/html/2607.19102v1#S9 — 9. Conclusions。

**Artifact boundary。** Exact v1 links https://github.com/jaegertracing/jaeger/issues/6814, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：Exploring alternative modalities represents an interesting direction for future work.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-TRACE`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19102:end -->

<!-- review:SF-2026-ARXIV-2607-19139:start -->
### Text Template Tokens Are Implicit Semantic Registers in Diffusion Transformers

<!-- claim:SF-2026-ARXIV-2607-19139:start -->Modern text-to-image diffusion transformers (DiTs) generate images through joint attention, in which text and image tokens interact directly within a single sequence. In large-scale DiTs, the conditioning input contains not only the user prompt but also chat-template tokens introduced by LLM-based text encoders. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19139:end -->

**为什么进入候选分母。** 摘要首要问题为“Modern text-to-image diffusion transformers (DiTs) generate images through joint attention, in which text and image tokens interact directly within a single sequence.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** To probe this, we introduce a causal interpretability framework.

**证据证明什么。** We show that they acquire this identity indirectly.

**证据没有证明什么。** 6 Limitations and Future Work Our study is primarily analytical. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19139v1#S10.SS3 — 10.3 Extending the Analysis to Distilled and Edit Models; https://arxiv.org/html/2607.19139v1#S2.SS1 — 2.1 Attention Sinks in Generative Models。Evaluation：https://arxiv.org/html/2607.19139v1#S10 — 10 Extended Experiments; https://arxiv.org/html/2607.19139v1#S10.SS1 — 10.1 Extending the Analysis to FLUX.2。Limitations / counterevidence：https://arxiv.org/html/2607.19139v1#S5 — 5 Discussion and Conclusion; https://arxiv.org/html/2607.19139v1#S6 — 6 Limitations and Future Work。

**Artifact boundary。** Exact v1 links https://github.com/Met4physics/DiT-Interpretability, https://github.com/black-forest-labs/flux, https://github.com/modelscope/DiffSynth-Studio; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：6 Limitations and Future Work Our study is primarily analytical.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-GENERATIVE-PARADIGMS`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19139:end -->

<!-- review:SF-2026-ARXIV-2607-19182:start -->
### ARBITER: Guarded Agentic Control for SLO-Oriented Kubernetes Remediation

<!-- claim:SF-2026-ARXIV-2607-19182:start -->Maintaining service-level objectives (SLOs) on Kubernetes microservices remains difficult because autoscalers observe coarse resource metrics, recent SLO controllers often depend on custom telemetry, and unconstrained agentic operators cannot safely mutate production clusters. We present ARBITER, a guarded control plane for SLO-oriented Kubernetes remediation. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19182:end -->

**为什么进入候选分母。** 摘要首要问题为“Maintaining service-level objectives (SLOs) on Kubernetes microservices remains difficult because autoscalers observe coarse resource metrics, recent SLO controllers often depend on custom telemetry, and unconstrained agentic operators cannot safely mutate production clusters.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We present ARBITER, a guarded control plane for SLO-oriented Kubernetes remediation.

**证据证明什么。** We release the controller, replay corpus, harnesses, safety tests, and figure artifacts: https://github.com/pooyan/arbiter.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19182v1#S2.SS3 — II-C Why OpenTelemetry Changes the Design Space; https://arxiv.org/html/2607.19182v1#S4 — IV ARBITER Control Architecture。Evaluation：https://arxiv.org/html/2607.19182v1#S8 — VIII Evaluation Results; https://arxiv.org/html/2607.19182v1#S7 — VII Evaluation Methodology。Limitations / counterevidence：https://arxiv.org/html/2607.19182v1#S11 — XI Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/pooyan/arbiter, https://github.com/kubernetes/perf-tests/tree/master/clusterloader2, https://github.com/kubernetes-sigs/descheduler; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-KUBEFLOW`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19182:end -->

<!-- review:SF-2026-ARXIV-2607-19190:start -->
### Agentic Real2Sim: Physics-based World Modeling with Vision-Language Agents

<!-- claim:SF-2026-ARXIV-2607-19190:start -->Real-to-sim conversion for robotic interaction with objects remains labor-intensive because it requires more than visual reconstruction: a streamlined real2sim process must recover scene geometries and object states, infer physical parameters, and assemble actors, objects, cameras, poses, and trajectories into a runnable physical simulation. Today this process still depends on manual tuning of visual foundation models, mesh cleanup, coordinate-frame alignment, and brittle workflow glue across visual perception tools and simulators. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19190:end -->

**为什么进入候选分母。** 摘要首要问题为“Real-to-sim conversion for robotic interaction with objects remains labor-intensive because it requires more than visual reconstruction: a streamlined real2sim process must recover scene geometries and object states, infer physical parameters, and assemble actors, objects, cameras, poses, and trajectories into a runnable physical simulation.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We introduce \textit{Agentic Real2Sim}, a framework for generalized physical world modeling with vision-language agents, converting a real-world recording of object-robot interaction into a simulatable episodic twin which preserves observations, geometries, robot interactions, and object states.

**证据证明什么。** The project site is available at https://agentic-real2sim.github.io/.

**证据没有证明什么。** 5 Conclusions, Limitations and Future Work We introduced Agentic Real2Sim , a framework for converting real-world physical interaction recordings into simulatable digital twins. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19190v1#S3 — 3 Method; https://arxiv.org/html/2607.19190v1#S3.SS1 — 3.1 System Overview。Evaluation：https://arxiv.org/html/2607.19190v1#S4 — 4 Experiments; https://arxiv.org/html/2607.19190v1#S4.SS1 — 4.1 Evaluation Metric。Limitations / counterevidence：https://arxiv.org/html/2607.19190v1#S5 — 5 Conclusions, Limitations and Future Work。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：5 Conclusions, Limitations and Future Work We introduced Agentic Real2Sim , a framework for converting real-world physical interaction recordings into simulatable digital twins.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19190:end -->

<!-- review:SF-2026-ARXIV-2607-19191:start -->
### ABot-World-0: Infinite Interactive World Rollout on a Single Desktop GPU

<!-- claim:SF-2026-ARXIV-2607-19191:start -->We present ABot-World-0, an action-conditioned video world model for real-time, long-horizon closed-loop interaction, supported by a multi-source data infrastructure spanning AAA games, simulation engines, and internet videos to learn controllable world dynamics. WorldExplorer performs agent-driven collection guided by training feedback, while a unified pipeline applies 14 deterministic quality checks, VLM-based assessment, and synchronized action and text annotation. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19191:end -->

**为什么进入候选分母。** 摘要首要问题为“We present ABot-World-0, an action-conditioned video world model for real-time, long-horizon closed-loop interaction, supported by a multi-source data infrastructure spanning AAA games, simulation engines, and internet videos to learn controllable world dynamics.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** We present ABot-World-0, an action-conditioned video world model for real-time, long-horizon closed-loop interaction, supported by a multi-source data infrastructure spanning AAA games, simulation engines, and internet videos to learn controllable world dynamics.

**证据证明什么。** Experiments on WorldRoamBench and extended interactive rollouts demonstrate competitive controllability and coherent long-horizon world evolution.

**证据没有证明什么。** 6 Discussion and Future Work Explicit actions admit simple conditioning. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19191v1#S4.SS4 — 4.4 Full-Stack Co-Design for Real-Time World Rollout。Evaluation：https://arxiv.org/html/2607.19191v1#S5 — 5 Evaluation; https://arxiv.org/html/2607.19191v1#S5.SS1 — 5.1 WorldRoamBench Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.19191v1#S6 — 6 Discussion and Future Work; https://arxiv.org/html/2607.19191v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/amap-cvlab/ABot-World, https://github.com/madebyollin/taehv, https://github.com/lllyasviel/FramePack; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：6 Discussion and Future Work Explicit actions admit simple conditioning.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19191:end -->

<!-- review:SF-2026-ARXIV-2607-19194:start -->
### Cognitive Dual-Process Planning for Autonomous Driving with Structured Scene Knowledge and Verifiable Reasoning-Action Consistency

<!-- claim:SF-2026-ARXIV-2607-19194:start -->High-level planning for autonomous driving is a knowledge-intensive engineering decision task that requires accurate scene understanding, timely inference, and internally consistent action selection. Vision-language models (VLMs) can make intermediate reasoning explicit, but their use in deployed planners is constrained by costly structured supervision, unnecessary reasoning in routine scenes, and possible inconsistencies between generated rationales and driving actions. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19194:end -->

**为什么进入候选分母。** 摘要首要问题为“High-level planning for autonomous driving is a knowledge-intensive engineering decision task that requires accurate scene understanding, timely inference, and internally consistent action selection.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** We present a cognitive dual-process planning framework that represents planning-relevant scene knowledge in a machine-parsable structured chain-of-thought (S-CoT) schema.

**证据证明什么。** Together, these results show how explicit scene knowledge can be operationalized through adaptive reasoning and rule-based verification to support high-level VLM planning decisions.

**证据没有证明什么。** In the manual audit, the generated annotations achieve 91.8% CoT accuracy and 98.5% LCS. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19194v1#S3 — 3 Method。Evaluation：https://arxiv.org/html/2607.19194v1#S4.SS6 — 4.6 Ablation Studies and Sensitivity Analysis; https://arxiv.org/html/2607.19194v1#S4 — 4 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.19194v1#S4.SS5 — 4.5 Long-Tail Robustness and Failure Analysis; https://arxiv.org/html/2607.19194v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：In the manual audit, the generated annotations achieve 91.8% CoT accuracy and 98.5% LCS.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19194:end -->

<!-- review:SF-2026-ARXIV-2607-19214:start -->
### Keeping the Cache Warm Pays: Keepalive Economics for Agentic Workloads

<!-- claim:SF-2026-ARXIV-2607-19214:start -->Frontier LLM providers cache a prompt's processed prefix so that a follow-up request sharing it pays ~10% of the input price and skips most of the prefill latency. Agentic workloads systematically destroy this benefit: the agent sends a request, runs a tool or waits for approval for minutes, and by the time the follow-up is sent the cached prefix has been evicted, so the agent pays the full prefill again. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19214:end -->

**为什么进入候选分母。** 摘要首要问题为“Frontier LLM providers cache a prompt's processed prefix so that a follow-up request sharing it pays ~10% of the input price and skips most of the prefill latency.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** Agentic workloads systematically destroy this benefit: the agent sends a request, runs a tool or waits for approval for minutes, and by the time the follow-up is sent the cached prefix has been evicted, so the agent pays the full prefill again.

**证据证明什么。** A client-side keepalive, replaying the prefix on a timer during the pause, prevents this, and it is individually rational: across Anthropic, OpenAI, Google, and DeepSeek we show that a keepalive holds the prefix warm through gaps where idle baselines are evicted, cutting the post-pause request cost by up to 12.5x.

**证据没有证明什么。** Residency today is priced per read , not per token held per second, and the price does not rise when the tier is hot. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19214v1#S4 — 4 Method。Evaluation：https://arxiv.org/html/2607.19214v1#S5 — 5 Results。Limitations / counterevidence：https://arxiv.org/html/2607.19214v1#S6 — 6 Discussion: rational adoption, and the provider response it forces; https://arxiv.org/html/2607.19214v1#S7 — 7 Threats to validity。

**Artifact boundary。** Exact v1 links https://github.com/Aider-AI/aider/blob/main/HISTORY.md, https://github.com/yujiachen-y/claude-code-cache-keepalive, https://github.com/openclaw/openclaw/issues/62475; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：Residency today is priced per read , not per token held per second, and the price does not rise when the tier is hot.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-COST`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19214:end -->

<!-- review:SF-2026-ARXIV-2607-19215:start -->
### HACO: Hedged Agent Computing for Reliable LLM Systems

<!-- claim:SF-2026-ARXIV-2607-19215:start -->As large language model (LLM) agents move from isolated prompting to longhorizon workflows, failures increasingly arise at the role-to-instance binding boundary, where task-specific role requests must be assigned to concrete agent instances under current service, network, and query conditions. Existing agent system research has improved role specialization, workflow topology, memory, and tool use, but often assumes a fixed stable execution environment. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19215:end -->

**为什么进入候选分母。** 摘要首要问题为“As large language model (LLM) agents move from isolated prompting to longhorizon workflows, failures increasingly arise at the role-to-instance binding boundary, where task-specific role requests must be assigned to concrete agent instances under current service, network, and query conditions.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** Existing agent system research has improved role specialization, workflow topology, memory, and tool use, but often assumes a fixed stable execution environment.

**证据证明什么。** Experiments on various benchmarks, together with runtime degradation studies, show that HACO improves robustness and output quality under changing deployment conditions, while using lower token and latency cost than exhaustive parallel execution.

**证据没有证明什么。** HACO views each role invocation as a runtime decision that jointly depends on role type, LLM choice, and execution environment, instead of treating it as a fixed call determined only by a role–agent instance pair. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19215v1#A4 — Appendix D Algorithms and Baselines; https://arxiv.org/html/2607.19215v1#A4.SS1 — D.1 HACO Algorithm。Evaluation：https://arxiv.org/html/2607.19215v1#S4.SS2 — 4.2 Experimental Results; https://arxiv.org/html/2607.19215v1#A3 — Appendix C Experimental Setup Details。Limitations / counterevidence：https://arxiv.org/html/2607.19215v1#A6 — Appendix F Limitations; https://arxiv.org/html/2607.19215v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：HACO views each role invocation as a runtime decision that jointly depends on role type, LLM choice, and execution environment, instead of treating it as a fixed call determined only by a role–agent instance pair.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-PLATFORM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19215:end -->

<!-- review:SF-2026-ARXIV-2607-19243:start -->
### Inference-Time Steering for Cross-Lingual Factual Consistency in LLMs

<!-- claim:SF-2026-ARXIV-2607-19243:start -->Although Large Language Models (LLMs) demonstrate remarkable multilingual fluency, their internal knowledge representations remain disproportionately biased toward high-resource languages. This leads to cross-lingual factual inconsistency, where they shift their empirical answer distributions based solely on the prompt language. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19243:end -->

**为什么进入候选分母。** 摘要首要问题为“Although Large Language Models (LLMs) demonstrate remarkable multilingual fluency, their internal knowledge representations remain disproportionately biased toward high-resource languages.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** These findings suggest that cross-lingual inconsistency is at least partly a selection problem, and that simple contextual interventions may outperform more invasive methods for robust, transferable alignment.

**证据证明什么。** Although Large Language Models (LLMs) demonstrate remarkable multilingual fluency, their internal knowledge representations remain disproportionately biased toward high-resource languages.

**证据没有证明什么。** Although this choice was justified by both multilingual quality and computational feasibility, the results should not be interpreted as model-independent. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19243v1#A4.SS1 — D.1 System prompt; https://arxiv.org/html/2607.19243v1#A6 — Appendix F Intervention implementation details。Evaluation：https://arxiv.org/html/2607.19243v1#A2.SS1 — B.1 Multilingual factual benchmark curation; https://arxiv.org/html/2607.19243v1#A3.SS2 — C.2 Evaluation pipeline。Limitations / counterevidence：https://arxiv.org/html/2607.19243v1#S9 — 9 Conclusion and Future work; https://arxiv.org/html/2607.19243v1#S10 — 10 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/alexandermanev/cross-lingual-llm-consistency, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Although this choice was justified by both multilingual quality and computational feasibility, the results should not be interpreted as model-independent.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MODEL-SAMPLING`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19243:end -->

<!-- review:SF-2026-ARXIV-2607-19257:start -->
### Prompt Design at Scale: How Format, Instruction Count, and Context Length Shape Instruction Adherence and Hallucination in Large Language Models

<!-- claim:SF-2026-ARXIV-2607-19257:start -->Practitioners make three prompt-design decisions with almost no controlled evidence behind them: how to format instructions and context (markdown, plain text, prose, or tabular), how many simultaneous instructions a system prompt can carry before compliance degrades, and how much context a model can hold before recall and honesty degrade. We report two controlled experiments crossing all three factors on one held, contamination-free synthetic corpus (the "Book of Veyra," 8,780 uniquely-named entities, deterministically regenerable from a fixed seed), evaluated across five models. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19257:end -->

**为什么进入候选分母。** 摘要首要问题为“Practitioners make three prompt-design decisions with almost no controlled evidence behind them: how to format instructions and context (markdown, plain text, prose, or tabular), how many simultaneous instructions a system prompt can carry before compliance degrades, and how much context a model can hold before recall and honesty degrade.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Experiment 1 (960 calls/model) measures instruction-following decay as rule count N grows from 10 to 160, crossed with four formats and system-prompt vs. user-turn placement.

**证据证明什么。** No model shows a reliable markdown advantage; one 35B model favors plain text instead.

**证据没有证明什么。** Our design cannot test this mechanism directly, since doing so would require comparing a base model against its own instruction-tuned counterpart on the identical probe, holding everything except the alignment step fixed. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19257v1#S4.SS1 — 4.1 Design; https://arxiv.org/html/2607.19257v1#S5.SS1 — 5.1 Design。Evaluation：https://arxiv.org/html/2607.19257v1#S2.SS5 — 2.5 Synthetic, Contamination-Free Hallucination Benchmarks; https://arxiv.org/html/2607.19257v1#S4 — 4 Experiment 1: Instruction-Following Decay。Limitations / counterevidence：https://arxiv.org/html/2607.19257v1#S10 — 10 Future Work; https://arxiv.org/html/2607.19257v1#S11 — 11 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/iNetanel/veyrabench, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Our design cannot test this mechanism directly, since doing so would require comparing a base model against its own instruction-tuned counterpart on the identical probe, holding everything except the alignment step fixed.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-PROMPT`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19257:end -->

<!-- review:SF-2026-ARXIV-2607-19262:start -->
### BioSecBench-Surveillance: A Verifiable Benchmark for AI Agents in Pathogen Genomic Surveillance

<!-- claim:SF-2026-ARXIV-2607-19262:start -->As pathogen genomic surveillance scales, the bottleneck is shifting from data generation to analysis. We present BioSecBench-Surveillance, a verifiable benchmark of 100 evaluations testing whether AI agents can infer the right analysis pipeline from raw sequencing data and surveillance context. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19262:end -->

**为什么进入候选分母。** 摘要首要问题为“As pathogen genomic surveillance scales, the bottleneck is shifting from data generation to analysis.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We present BioSecBench-Surveillance, a verifiable benchmark of 100 evaluations testing whether AI agents can infer the right analysis pipeline from raw sequencing data and surveillance context.

**证据证明什么。** BioSecBench-Surveillance provides a standard for measuring whether agents can be trusted to perform genomic surveillance when the next outbreak arrives.

**证据没有证明什么。** Several limitations of the benchmark suggest directions for future work. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19262v1#S5 — Methods; https://arxiv.org/html/2607.19262v1#S3.SS1 — No model–harness pairing exceeds 50% mean pass rate。Evaluation：https://arxiv.org/html/2607.19262v1#S2 — Benchmark construction; https://arxiv.org/html/2607.19262v1#S2.SS1 — Evaluation inventory。Limitations / counterevidence：https://arxiv.org/html/2607.19262v1#S3.SS3 — Failure patterns are consistent across configurations; https://arxiv.org/html/2607.19262v1#S4 — Discussion。

**Artifact boundary。** Exact v1 links https://github.com/latchbio/biosecbench-surveillance, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Several limitations of the benchmark suggest directions for future work.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19262:end -->

<!-- review:SF-2026-ARXIV-2607-19267:start -->
### They'll Verify. They Just Won't Act. How Authority Framing and Laundered Code Turn a Trusted Agentic CI/CD Pipeline Into an Attack Surface

<!-- claim:SF-2026-ARXIV-2607-19267:start -->We study a five-agent CI/CD pipeline (triage -&gt; developer -&gt; security-scan -&gt; review -&gt; approve/deploy), built from five distinct production LLMs across three providers, behind an LLM firewall in shadow mode. A single untrusted input - an external issue requesting a "usage-telemetry" feature - asks for code that exfiltrates process secrets (dict(os.environ)) to an attacker URL, laundered as observability. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19267:end -->

**为什么进入候选分母。** 摘要首要问题为“We study a five-agent CI/CD pipeline (triage -&gt; developer -&gt; security-scan -&gt; review -&gt; approve/deploy), built from five distinct production LLMs across three providers, behind an LLM firewall in shadow mode.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** The failure is systemic: neither prompt secrecy nor distributed verification protects; a provenance-aware control at the entry, independent of both, would have.

**证据证明什么。** All data is 100% synthetic; the sink is mocked and the exfil URL is never contacted.

**证据没有证明什么。** Content-based detection, the dominant paradigm, cannot catch an attack whose payload is syntactically benign and whose malice lies only in provenance and intent (Fig. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19267v1#S3 — 3 Methods; https://arxiv.org/html/2607.19267v1#S2 — 2 Threat model。Evaluation：https://arxiv.org/html/2607.19267v1#S4 — 4 Results。Limitations / counterevidence：https://arxiv.org/html/2607.19267v1#S2 — 2 Threat model; https://arxiv.org/html/2607.19267v1#S5 — 5 Discussion。

**Artifact boundary。** Exact v1 links https://github.com/senthex-security/senthex-research, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Content-based detection, the dominant paradigm, cannot catch an attack whose payload is syntactically benign and whose malice lies only in provenance and intent (Fig.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19267:end -->

<!-- review:SF-2026-ARXIV-2607-19292:start -->
### The safety failures we are not instrumenting: a perspective on hidden safety-critical challenges in modern AI systems

<!-- claim:SF-2026-ARXIV-2607-19292:start -->Current AI safety discourse still focuses disproportionately on visible failures, including obvious harms, dramatic misuse, and hypothetical catastrophic scenarios. In deployed systems, many of the most consequential failures are quieter: plausible rather than spectacular, distributed across components rather than localized in a single output, and normalized by workflows before they are recognized as hazards. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19292:end -->

**为什么进入候选分母。** 摘要首要问题为“Current AI safety discourse still focuses disproportionately on visible failures, including obvious harms, dramatic misuse, and hypothetical catastrophic scenarios.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** In deployed systems, many of the most consequential failures are quieter: plausible rather than spectacular, distributed across components rather than localized in a single output, and normalized by workflows before they are recognized as hazards.

**证据证明什么。** We conclude with design and governance recommendations and a research agenda for shifting AI safety from model-centric evaluation toward socio-technical reliability.

**证据没有证明什么。** From Bad Outputs to Integrity Failures A useful AI safety taxonomy should help practitioners answer not only “What can the model do?” but also “What becomes easier to get wrong, harder to inspect, and harder to correct once the model is embedded into a real decision pipeline?” The answer depends on multiple layers of integrity. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19292v1#S3.SS5 — 3.5. Ecosystem Integrity: Synthetic Evidence Pollution and the Erosion of Collective Error Correction。Evaluation：https://arxiv.org/html/2607.19292v1#S3.SS4 — 3.4. Organizational Integrity: Evaluation Deception, Fictional Oversight, and Diffused Accountability。Limitations / counterevidence：https://arxiv.org/html/2607.19292v1#S2 — 2. From Bad Outputs to Integrity Failures; https://arxiv.org/html/2607.19292v1#S7 — 7. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：From Bad Outputs to Integrity Failures A useful AI safety taxonomy should help practitioners answer not only “What can the model do?” but also “What becomes easier to get wrong, harder to inspect, and harder to correct once the model is embedded into a real decision pipeline?” The answer depends on multiple layers of integrity.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-MONITORING`；evidence-stage relation：`structural_candidate`。
- Books 候选路由（尚非最终决定）：`Structural Candidate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19292:end -->

<!-- review:SF-2026-ARXIV-2607-19297:start -->
### Graph-Based Agentic AI with LangGraph: Workflow Pathways for Long-Running Stateful Business Processes

<!-- claim:SF-2026-ARXIV-2607-19297:start -->This paper is a practitioner guide to graph-based workflow pathways for long-running, stateful, multi-step generative AI systems in business processes. Rather than treating LangGraph, a low-level orchestration framework for stateful agents, as a model-quality benchmark target, we present three executable recipes -- SQL analytics with repair loops, agentic retrieval-augmented generation with evidence gating, and human-in-the-loop policy review with interrupt and checkpoint recovery -- to show how typed state, conditional routing, deterministic tools, retries, interrupts, checkpoints, and traces fit together. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19297:end -->

**为什么进入候选分母。** 摘要首要问题为“This paper is a practitioner guide to graph-based workflow pathways for long-running, stateful, multi-step generative AI systems in business processes.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** Rather than treating LangGraph, a low-level orchestration framework for stateful agents, as a model-quality benchmark target, we present three executable recipes -- SQL analytics with repair loops, agentic retrieval-augmented generation with evidence gating, and human-in-the-loop policy review with interrupt and checkpoint recovery -- to show how typed state, conditional routing, deterministic tools, retries, interrupts, checkpoints, and traces fit together.

**证据证明什么。** Rather than treating LangGraph, a low-level orchestration framework for stateful agents, as a model-quality benchmark target, we present three executable recipes -- SQL analytics with repair loops, agentic retrieval-augmented generation with evidence gating, and human-in-the-loop policy review with interrupt and checkpoint recovery -- to show how typed state, conditional routing, deterministic tools, retries, interrupts, checkpoints, and traces fit together.

**证据没有证明什么。** The point is not that LangGraph improves model quality. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19297v1#S3 — 3 Recipe 1: SQL Analytics with Repair Loops; https://arxiv.org/html/2607.19297v1#S5 — 5 Recipe 3: HITL Policy Review。Evaluation：https://arxiv.org/html/2607.19297v1#S7 — 7 Cross-Recipe Comparison; https://arxiv.org/html/2607.19297v1#S8 — 8 Failure Modes and Testing。Limitations / counterevidence：https://arxiv.org/html/2607.19297v1#S9.SS2 — 9.2 Limitations; https://arxiv.org/html/2607.19297v1#S10 — 10 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/langchain-ai/langgraph, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：The point is not that LangGraph improves model quality.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-WORKFLOW`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19297:end -->

<!-- review:SF-2026-ARXIV-2607-19301:start -->
### PAGE-RAG: Evidence-Grounded Adaptive Graph Retrieval for Long-Document Question Answering

<!-- claim:SF-2026-ARXIV-2607-19301:start -->GraphRAG improves long-document question answering by introducing structured representations beyond conventional retrieval. However, automatically constructed graphs are inherently incomplete projections of source documents, and treating them as independent knowledge sources may lead to unreliable retrieval and generation. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19301:end -->

**为什么进入候选分母。** 摘要首要问题为“GraphRAG improves long-document question answering by introducing structured representations beyond conventional retrieval.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** We propose PAGE-RAG, a projection-aware adaptive graph retrieval framework for reliable long-document question answering.

**证据证明什么。** Experiments demonstrate that PAGE-RAG achieves competitive answer quality while improving retrieval efficiency and knowledge reliability, highlighting the importance of projection-aware graph modeling, adaptive retrieval, and explicit knowledge boundary control for trustworthy GraphRAG systems.

**证据没有证明什么。** Future work will explore finer-grained access control, cross-domain graph construction, and more precise task-adaptive graph computation. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19301v1#Sx1 — Introduction; https://arxiv.org/html/2607.19301v1#Sx2 — Related Work。Evaluation：https://arxiv.org/html/2607.19301v1#Sx4 — Evaluation; https://arxiv.org/html/2607.19301v1#Sx4.SSx1 — Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.19301v1#Sx5 — Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/CXY0112/PAGE-RAG, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：Future work will explore finer-grained access control, cross-domain graph construction, and more precise task-adaptive graph computation.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-RAG`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19301:end -->

<!-- review:SF-2026-ARXIV-2607-19317:start -->
### CircuitKIT : Circuit Discovery, Evaluation, and Application Toolkit for Mechanistic Interpretability

<!-- claim:SF-2026-ARXIV-2607-19317:start -->Circuit analysis can support not only model explanation but also downstream interventions such as pruning, editing, steering, and selective fine-tuning. However, conducting such analyses currently requires stitching together separate implementations for discovery, evaluation, and intervention, as well as hand-authoring the contrastive prompts required by many discovery methods. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19317:end -->

**为什么进入候选分母。** 摘要首要问题为“Circuit analysis can support not only model explanation but also downstream interventions such as pruning, editing, steering, and selective fine-tuning.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** This fragmentation makes methods difficult to compare and limits their application beyond canonical tasks.

**证据证明什么。** The library, examples, notebooks, and documentation are released at https://github.com/Lexsi-Labs/CircuitKIT .

**证据没有证明什么。** The release mitigates this without pretending to eliminate it: the library ships aggregate scores and evaluation reports, not harmful prompts or pre-ablated checkpoints; the steering, editing, and fine-tuning modules require explicit import; and the case-study data is research-use only. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19317v1#S3 — 3 Architecture; https://arxiv.org/html/2607.19317v1#S11.SS1 — 11.1 Algorithm Validation on IOI (Node Level)。Evaluation：https://arxiv.org/html/2607.19317v1#A1 — Appendix A Experimental Protocols; https://arxiv.org/html/2607.19317v1#S6 — 6 Faithfulness Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.19317v1#S12 — 12 Conclusion; https://arxiv.org/html/2607.19317v1#S13 — 13 Limitations, Ethics, and Broader Impact。

**Artifact boundary。** Exact v1 links https://github.com/Lexsi-Labs/CircuitKIT, https://github.com/TransformerLensOrg/TransformerLens, https://github.com/UFO-101/auto-circuit; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：The release mitigates this without pretending to eliminate it: the library ships aggregate scores and evaluation reports, not harmful prompts or pre-ablated checkpoints; the steering, editing, and fine-tuning modules require explicit import; and the case-study data is research-use only.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`WORLDVIEW-REPRESENTATION`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19317:end -->

<!-- review:SF-2026-ARXIV-2607-19322:start -->
### Two-Level Meta-Rubrics for Evaluating Open-Ended Generation: GAMUT, a Benchmark for Factual Completeness

<!-- claim:SF-2026-ARXIV-2607-19322:start -->Rubric-based evaluation of open-ended generation faces a fundamental tension between expressiveness and reliability. Authoring a faithful rubric requires expressing the structure of the space of good answers: open-ended sets of acceptable options, ordered processes, and the relative importance of facts. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19322:end -->

**为什么进入候选分母。** 摘要首要问题为“Rubric-based evaluation of open-ended generation faces a fundamental tension between expressiveness and reliability.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We resolve this tension with a two-level meta-rubric framework.

**证据证明什么。** Evaluating 14 frontier and open-weight models, we find Gamut genuinely challenging (best score 58.7% from Gemini 3.1 Pro), highly discriminative, and robust to the choice of judge.

**证据没有证明什么。** This resolves the tension between expressiveness and reliability in rubric-based evaluation, and our analysis shows the structure is not incidental: 98% of Gamut ’s questions require a component beyond isolated facts that a flat checklist cannot represent. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19322v1#S3 — 3 A Two-Level Meta-Rubric Framework for Evaluating Open-Ended Generation; https://arxiv.org/html/2607.19322v1#S5 — 5 Evaluating Models on Gamut。Evaluation：https://arxiv.org/html/2607.19322v1#S2.SS1 — 2.1 Long-Form Factuality Evaluation; https://arxiv.org/html/2607.19322v1#S2.SS2 — 2.2 Rubric-Based Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.19322v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/facebookresearch/GAMUT, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：This resolves the tension between expressiveness and reliability in rubric-based evaluation, and our analysis shows the structure is not incidental: 98% of Gamut ’s questions require a component beyond isolated facts that a flat checklist cannot represent.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19322:end -->

<!-- review:SF-2026-ARXIV-2607-19326:start -->
### Selective State-Space Adaptation and Retrieval for Language Model Reasoning

<!-- claim:SF-2026-ARXIV-2607-19326:start -->Low-rank adaptation introduces a static learned update applied identically to every input. The update provides task-level adaptation but does not explicitly represent token-level or instance-level state variation. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19326:end -->

**为什么进入候选分母。** 摘要首要问题为“Low-rank adaptation introduces a static learned update applied identically to every input.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** The update provides task-level adaptation but does not explicitly represent token-level or instance-level state variation.

**证据证明什么。** The token-level adapter improves over low-rank adaptation.

**证据没有证明什么。** The shared pattern (relevance-blind, role-sensitive) explains why the modulator and MaRA are non-redundant: the modulator reshapes the low-rank update by token role and cannot perform evidence selection, so MaRA contributes an orthogonal capability. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19326v1#A1 — Appendix A System overview; https://arxiv.org/html/2607.19326v1#A9 — Appendix I MaRA architecture details。Evaluation：https://arxiv.org/html/2607.19326v1#A9.SS2 — I.2 Architecture ablation (full analysis); https://arxiv.org/html/2607.19326v1#A7 — Appendix G State-usage probe: per-cell results。Limitations / counterevidence：https://arxiv.org/html/2607.19326v1#A6 — Appendix F Modulation by token role: extended discussion; https://arxiv.org/html/2607.19326v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：The shared pattern (relevance-blind, role-sensitive) explains why the modulator and MaRA are non-redundant: the modulator reshapes the low-rank update by token role and cannot perform evidence selection, so MaRA contributes an orthogonal capability.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-RAG`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19326:end -->

<!-- review:SF-2026-ARXIV-2607-19336:start -->
### Agents in the Wild: Where Research Meets Deployment

<!-- claim:SF-2026-ARXIV-2607-19336:start -->Agentic systems large language model (LLM) based architectures capable of reasoning, planning, acting, and coordinating with tools and other agents are rapidly transitioning from research prototypes to production scale deployments across domains such as software engineering, scientific discovery, and finance. While academic work has emphasized benchmarks and algorithmic innovation, deployment raises new challenges around robustness, safety, and reliability. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19336:end -->

**为什么进入候选分母。** 摘要首要问题为“Agentic systems large language model (LLM) based architectures capable of reasoning, planning, acting, and coordinating with tools and other agents are rapidly transitioning from research prototypes to production scale deployments across domains such as software engineering, scientific discovery, and finance.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Through applied case studies in pharmaceutical discovery and financial systems, we analyze common design patterns that make agentic systems successful, and discuss practical mitigation strategies for failure modes, such as verification pipelines, fallback mechanisms, and human in the loop supervision.

**证据证明什么。** Attendees will gain a comprehensive view of the field along with concrete design patterns, evaluation checklists, and templates for safe and reliable deployment across industries.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19336v1#S3.SS1 — 3.1. Agentic Systems: History and Definitions。Evaluation：https://arxiv.org/html/2607.19336v1#S3.SS4 — 3.4. Evaluation Beyond Benchmarks。Limitations / counterevidence：https://arxiv.org/html/2607.19336v1#S1 — 1. Tutorial Description; https://arxiv.org/html/2607.19336v1#S2 — 2. Expected Audience Takeaways。

**Artifact boundary。** Exact v1 links https://aclanthology.org/2024.emnlp-demo.8.pdf, https://aclanthology.org/2023.acl-demo.11.pdf, https://aclanthology.org/2024.emnlp-demo.8/; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-PLATFORM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19336:end -->

<!-- review:SF-2026-ARXIV-2607-19338:start -->
### CodeRescue: Budget-Calibrated Recovery Routing for Coding Agents

<!-- claim:SF-2026-ARXIV-2607-19338:start -->Coding agents increasingly operate in executable environments where a failed attempt produces actionable feedback rather than merely an incorrect answer. Existing cost-aware systems typically treat such failures as cascade decisions: try a cheap model first, then escalate hard cases to a stronger and more expensive model. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19338:end -->

**为什么进入候选分母。** 摘要首要问题为“Coding agents increasingly operate in executable environments where a failed attempt produces actionable feedback rather than merely an incorrect answer.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** Existing cost-aware systems typically treat such failures as cascade decisions: try a cheap model first, then escalate hard cases to a stronger and more expensive model.

**证据证明什么。** The calibrated frontier improves over fixed actions, prompt-only routers, and a binary cascade baseline; in the main GPT-5.4-nano/GPT-5.4 setting, one CRC-calibrated frontier point exceeds always-escalate solve rate while using 35% of its mean recovery cost.

**证据没有证明什么。** Future work should extend recovery routing to multi-step agent trajectories and richer deployment constraints. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19338v1#S3 — 3 Method; https://arxiv.org/html/2607.19338v1#A3 — Appendix C Cross-Model Generalization: Gemini。Evaluation：https://arxiv.org/html/2607.19338v1#A4 — Appendix D Per-Benchmark CRC Frontiers: TACO Difficulty Ladder; https://arxiv.org/html/2607.19338v1#S5 — 5 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.19338v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/Qijia-He/agent-budget-control, https://openai.com/index/introducing-codex/, https://huggingface.co/Qwen/Qwen3.5-4B; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：Future work should extend recovery routing to multi-step agent trajectories and richer deployment constraints.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-PLATFORM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19338:end -->

<!-- review:SF-2026-ARXIV-2607-19339:start -->
### OmniReasoner: Thinking with Long Audio-Video via Native Tool Use

<!-- claim:SF-2026-ARXIV-2607-19339:start -->Long audio-video reasoning is difficult for omnimodal LLMs because the decisive evidence is often sparse, cross-modal, and too expensive to preserve with uniformly high-fidelity inputs. We introduce OmniReasoner, a tool-use post-training framework for Thinking with Long Audio-Video: omni-modal LLMs learn, via supervised fine-tuning and reinforcement learning, to decide whether and where to call a zoom-in tool before answering. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19339:end -->

**为什么进入候选分母。** 摘要首要问题为“Long audio-video reasoning is difficult for omnimodal LLMs because the decisive evidence is often sparse, cross-modal, and too expensive to preserve with uniformly high-fidelity inputs.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We introduce OmniReasoner, a tool-use post-training framework for Thinking with Long Audio-Video: omni-modal LLMs learn, via supervised fine-tuning and reinforcement learning, to decide whether and where to call a zoom-in tool before answering.

**证据证明什么。** Experiments across omnimodal and video benchmarks show that OmniReasoner improves both answer accuracy and temporal grounding while concentrating high-fidelity computation on informative regions.

**证据没有证明什么。** We did not experiment with Qwen-Omni-3, a larger and more recent model, due to limited compute resources and our team’s relative inexperience with large-scale infrastructure engineering. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19339v1#A2.SS4 — B.4 MCQ design and text-only guessability filter; https://arxiv.org/html/2607.19339v1#S3 — 3 Method。Evaluation：https://arxiv.org/html/2607.19339v1#S4 — 4 Experiments; https://arxiv.org/html/2607.19339v1#S4.SS2 — 4.2 Main Results。Limitations / counterevidence：https://arxiv.org/html/2607.19339v1#S5 — 5 Conclusion; https://arxiv.org/html/2607.19339v1#Sx1 — Limitations。

**Artifact boundary。** Exact v1 links https://github.com/RockyChen0205/OmniReasoner, https://huggingface.co/datasets/HuggingFaceFV/finevideo, https://github.com/huggingface/trl; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：We did not experiment with Qwen-Omni-3, a larger and more recent model, due to limited compute resources and our team’s relative inexperience with large-scale infrastructure engineering.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-TOOL-CALLING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19339:end -->

<!-- review:SF-2026-ARXIV-2607-19343:start -->
### Masked Visual Actions for Unified World Modeling

<!-- claim:SF-2026-ARXIV-2607-19343:start -->Video models absorb rich priors over how the visual world moves, interacts, and responds to contact, making them promising substrates for robotic world modeling. The central challenge is how to communicate action to such models in a form aligned with the visual space in which they learned these interaction priors, yet still grounded in physical manipulation. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19343:end -->

**为什么进入候选分母。** 摘要首要问题为“Video models absorb rich priors over how the visual world moves, interacts, and responds to contact, making them promising substrates for robotic world modeling.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We introduce Masked Visual Actions, a pixel-space control interface that expresses action as a partially revealed trajectory of an arbitrary entity in a video.

**证据证明什么。** Finetuned with only 15 hours of masked examples from real videos and simulation, a single checkpoint achieves strong visual fidelity and controllability across diverse scenes and multiple embodiments.

**证据没有证明什么。** Limitations It is worth noting that our model, similarly to existing generative models, learns the correlation between object interaction rather than causal relationships , which remains an open research question. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19343v1#A5.SS1 — E.1 Gemini system prompt; https://arxiv.org/html/2607.19343v1#S4 — 4 Method。Evaluation：https://arxiv.org/html/2607.19343v1#A3 — Appendix C Full quantitative results; https://arxiv.org/html/2607.19343v1#A5 — Appendix E VLM Evaluation Protocol。Limitations / counterevidence：https://arxiv.org/html/2607.19343v1#S6 — 6 Discussion and Conclusions。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Limitations It is worth noting that our model, similarly to existing generative models, learns the correlation between object interaction rather than causal relationships , which remains an open research question.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19343:end -->

<!-- review:SF-2026-ARXIV-2607-19344:start -->
### Appearance Pointers -- Multimodal Region Control of Diffusion Transformers

<!-- claim:SF-2026-ARXIV-2607-19344:start -->Controllable image generation remains challenging for creative professionals, who often require precise regional control over materials, object identities, and spatial arrangements that cannot be reliably achieved through text prompting alone. Diffusion Transformers (DiTs) can natively ingest heterogeneous tokens stemming from texts and images, but they lack mechanisms for determining where and how these tokens should influence the output. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19344:end -->

**为什么进入候选分母。** 摘要首要问题为“Controllable image generation remains challenging for creative professionals, who often require precise regional control over materials, object identities, and spatial arrangements that cannot be reliably achieved through text prompting alone.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We introduce appearance pointers, compact tokens that guide DiTs toward the correct appearance cues at the correct spatial locations by aligning text or image inputs with user-specified masks.

**证据证明什么。** Controllable image generation remains challenging for creative professionals, who often require precise regional control over materials, object identities, and spatial arrangements that cannot be reliably achieved through text prompting alone.

**证据没有证明什么。** These findings demonstrate that appearance pointers provide a simple, extensible, and effective interface for precise multimodal guidance, enabling generative models to better realize not only what users intend to create, but where and how the content should appear. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19344v1#Pt0.A1.SS4 — 0.A.4 Architecture; https://arxiv.org/html/2607.19344v1#S3 — 3 Method。Evaluation：https://arxiv.org/html/2607.19344v1#S5 — 5 Experiments & Results; https://arxiv.org/html/2607.19344v1#Pt0.A3 — Appendix 0.C Ablations。Limitations / counterevidence：https://arxiv.org/html/2607.19344v1#Pt0.A6 — Appendix 0.F Limitation & Discussion with Future Works; https://arxiv.org/html/2607.19344v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/black-forest-labs/flux, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：These findings demonstrate that appearance pointers provide a simple, extensible, and effective interface for precise multimodal guidance, enabling generative models to better realize not only what users intend to create, but where and how the content should appear.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-GENERATIVE-PARADIGMS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19344:end -->

<!-- review:SF-2026-ARXIV-2607-19345:start -->
### Copy Less, Ground More: Overcoming Repetitive Copying in Long-Context Reasoning via Evidence-Aware Reinforcement Learning

<!-- claim:SF-2026-ARXIV-2607-19345:start -->Large language models that generate step-by-step reasoning traces have achieved strong performance on complex tasks, and extending them to long-context settings has emerged as an important frontier. However, we identify a critical failure mode in this regime: \emph{repetitive copying}, where models extensively copy text from the input into their reasoning traces rather than productively solving the problem. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-19345:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language models that generate step-by-step reasoning traces have achieved strong performance on complex tasks, and extending them to long-context settings has emerged as an important frontier.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** Motivated by this diagnosis, we propose GEAR (Grounding Evidence-Aware Reward), a reward shaping method that augments the accuracy signal with a grounding reward for overlap with key evidence and a distractor penalty for overlap with irrelevant context.

**证据证明什么。** We validate GEAR across multiple model scales and benchmarks, showing consistent improvements of up to +4.6 average points over standard RL with accuracy-based rewards, with larger gains at longer contexts, while also reducing repetitive copying and thinking length.

**证据没有证明什么。** Experiments across three model scales and five benchmarks show that GEAR consistently improves over accuracy-only RL, with gains that generalize to context lengths 4 beyond the training distribution. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.19345v1#S4.SS1 — 4.1 Reward Design; https://arxiv.org/html/2607.19345v1#A1.SS1 — A.1 Repetitive Copying across Models。Evaluation：https://arxiv.org/html/2607.19345v1#A1.SS4 — A.4 Detailed Results for Section 3.3; https://arxiv.org/html/2607.19345v1#S3.SS1 — 3.1 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.19345v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Experiments across three model scales and five benchmarks show that GEAR consistently improves over accuracy-only RL, with gains that generalize to context lengths 4 beyond the training distribution.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MODEL-LONG-CONTEXT`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-19345:end -->

## 4. Benchmark Contracts

None。数值只在各 Source Review 的 exact-v1 evaluation contract 内使用，不形成跨配置 benchmark claim。

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-18241 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-18241 |
| SF-2026-ARXIV-2607-18246 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-18246 |
| SF-2026-ARXIV-2607-18253 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-18253 |
| SF-2026-ARXIV-2607-18280 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-18280 |
| SF-2026-ARXIV-2607-18314 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-18314 |
| SF-2026-ARXIV-2607-18357 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-18357 |
| SF-2026-ARXIV-2607-18367 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-18367 |
| SF-2026-ARXIV-2607-18481 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-18481 |
| SF-2026-ARXIV-2607-18532 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-18532 |
| SF-2026-ARXIV-2607-18553 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-18553 |
| SF-2026-ARXIV-2607-18603 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-18603 |
| SF-2026-ARXIV-2607-18631 | score_7_9 | selected | DA-20260722-01 | — | V2=9/9；相对其他 eligible family 提供更直接、可迁移且不重复的 state/control/evaluation 机制。 | analysis:DA-20260722-01 |
| SF-2026-ARXIV-2607-18664 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-18664 |
| SF-2026-ARXIV-2607-18709 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-18709 |
| SF-2026-ARXIV-2607-18715 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-18715 |
| SF-2026-ARXIV-2607-18722 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-18722 |
| SF-2026-ARXIV-2607-18754 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-18754 |
| SF-2026-ARXIV-2607-18802 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-18802 |
| SF-2026-ARXIV-2607-18840 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-18840 |
| SF-2026-ARXIV-2607-18847 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-18847 |
| SF-2026-ARXIV-2607-18859 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-18859 |
| SF-2026-ARXIV-2607-18886 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-18886 |
| SF-2026-ARXIV-2607-18915 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-18915 |
| SF-2026-ARXIV-2607-18957 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-18957 |
| SF-2026-ARXIV-2607-18975 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-18975 |
| SF-2026-ARXIV-2607-18979 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-18979 |
| SF-2026-ARXIV-2607-19058 | score_7_9 | selected | DA-20260722-02 | — | V2=9/9；相对其他 eligible family 提供更直接、可迁移且不重复的 state/control/evaluation 机制。 | analysis:DA-20260722-02 |
| SF-2026-ARXIV-2607-19102 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-19102 |
| SF-2026-ARXIV-2607-19182 | score_7_9 | selected | DA-20260722-03 | — | V2=9/9；相对其他 eligible family 提供更直接、可迁移且不重复的 state/control/evaluation 机制。 | analysis:DA-20260722-03 |
| SF-2026-ARXIV-2607-19190 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-19190 |
| SF-2026-ARXIV-2607-19191 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-19191 |
| SF-2026-ARXIV-2607-19214 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-19214 |
| SF-2026-ARXIV-2607-19215 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-19215 |
| SF-2026-ARXIV-2607-19297 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-19297 |
| SF-2026-ARXIV-2607-19301 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-19301 |
| SF-2026-ARXIV-2607-19338 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-19338 |
| SF-2026-ARXIV-2607-19339 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-19339 |
| SF-2026-ARXIV-2607-19343 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-19343 |
| SF-2026-ARXIV-2607-19344 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-19344 |
| SF-2026-ARXIV-2607-19345 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-19345 |

### Selection Decisions

<!-- analysis-decision:SF-2026-ARXIV-2607-18241:start -->
`SF-2026-ARXIV-2607-18241` 的 exact-v1 Deep Review 已保留。其机制为：We present BatchDAG, a system in which an LLM generates a typed directed acyclic graph (DAG) of operations -- SQL queries, semantic searches, in-memory transforms, parallel fan-outs, and single-shot analyses -- which a deterministic engine evaluates with topological-wave parallelism and structured JSON data flow. 为避免挤压 `AGENT-WORKFLOW` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-18241:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-18246:start -->
`SF-2026-ARXIV-2607-18246` 的 exact-v1 Deep Review 已保留。其机制为：We present Phionyx, a deterministic AI runtime architecture derived from the broader Echoism interaction framework that introduces a governance-first approach to AI engineering: treating large language model (LLM) outputs as noisy sensor measurements rather than direct decisions. 为避免挤压 `AGENT-PLATFORM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-18246:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-18253:start -->
`SF-2026-ARXIV-2607-18253` 的 exact-v1 Deep Review 已保留。其机制为：We design a lightweight latency estimator that simulates autoregressive token batch processing in the serving framework and estimates the time-to-first-token (TTFT) of queries. 为避免挤压 `INFER-SCHEDULING` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-18253:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-18280:start -->
`SF-2026-ARXIV-2607-18280` 的 exact-v1 Deep Review 已保留。其机制为：We study a minimalist compound sparsity framework that first applies low-rank approximation and channel pruning to obtain a statically compressed backbone, and then introduces lightweight routers for per-token dynamic layer skipping. 为避免挤压 `INFER-GPU-MEMORY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-18280:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-18314:start -->
`SF-2026-ARXIV-2607-18314` 的 exact-v1 Deep Review 已保留。其机制为：We demonstrate the system across five NLP and reinforcement-learning workflows. 为避免挤压 `PLATFORM-TRAINING-OPERATOR` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-18314:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-18357:start -->
`SF-2026-ARXIV-2607-18357` 的 exact-v1 Deep Review 已保留。其机制为：Large language models now write a growing share of the world's code, increasingly inside agents and serving systems that compile, execute, or dispatch generated code without line-by-line review. 为避免挤压 `MODEL-SAMPLING` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-18357:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-18367:start -->
`SF-2026-ARXIV-2607-18367` 的 exact-v1 Deep Review 已保留。其机制为：We present AlayaWorld, an interactive long-horizon video world model that generates 24-fps video at 540p and 720p. 为避免挤压 `MULTIMODAL-WORLD-MODELS` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-18367:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-18481:start -->
`SF-2026-ARXIV-2607-18481` 的 exact-v1 Deep Review 已保留。其机制为：Recent methods prompt a frontier LLM to explore the graph through a retrieval tool, but their reliance on frontier-scale inference makes them costly to deploy. 为避免挤压 `TRAIN-GRPO` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-18481:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-18532:start -->
`SF-2026-ARXIV-2607-18532` 的 exact-v1 Deep Review 已保留。其机制为：Our framework combines time-aware contrastive representation learning with discrete regime discovery to recover latent policies from activation trajectories. 为避免挤压 `TRAIN-GRPO` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-18532:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-18553:start -->
`SF-2026-ARXIV-2607-18553` 的 exact-v1 Deep Review 已保留。其机制为：We test both questions in a frozen 2.6B looped transformer, Ouro-RLTT. 为避免挤压 `AGENT-REFLECTION` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-18553:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-18603:start -->
`SF-2026-ARXIV-2607-18603` 的 exact-v1 Deep Review 已保留。其机制为：We present AutoIndex, a framework for learning representation programs: executable transformations that map raw documents into the representations exposed to a retrieval system. 为避免挤压 `AGENT-RAG` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-18603:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-18664:start -->
`SF-2026-ARXIV-2607-18664` 的 exact-v1 Deep Review 已保留。其机制为：In this paper, we propose DeforM, a reasoning-guided image-to-video generation framework that directs the model's focus toward physics-critical regions. 为避免挤压 `MULTIMODAL-GENERATIVE-PARADIGMS` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-18664:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-18709:start -->
`SF-2026-ARXIV-2607-18709` 的 exact-v1 Deep Review 已保留。其机制为：Building on our prior work, RoboInter1.0, we present RoboInter1.5, an extended and holistic suite of intermediate representations for both robotic manipulation and embodied world modeling. 为避免挤压 `MULTIMODAL-EMBODIED-VLA` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-18709:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-18715:start -->
`SF-2026-ARXIV-2607-18715` 的 exact-v1 Deep Review 已保留。其机制为：We introduce DWM (Decomposed World Model), a supervision-level framework that operationalizes this decomposition. 为避免挤压 `MULTIMODAL-WORLD-MODELS` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-18715:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-18722:start -->
`SF-2026-ARXIV-2607-18722` 的 exact-v1 Deep Review 已保留。其机制为：We introduce the Staleness-Adaptive Trust Region (SAT), which uses the detached sampled log-ratio as a practical staleness proxy, identifies the high-mismatch tail within each batch through Staleness-based kernel function scaling, and contracts only the sign-selected endpoint of the nominal PPO interval using Effective contraction factors. 为避免挤压 `TRAIN-GRPO` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-18722:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-18754:start -->
`SF-2026-ARXIV-2607-18754` 的 exact-v1 Deep Review 已保留。其机制为：We present AgentDebugX, an open-source debugging framework that organizes debugging as a closed loop of Detect, Attribute, Recover, and Rerun. 为避免挤压 `PLATFORM-TRACE` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-18754:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-18802:start -->
`SF-2026-ARXIV-2607-18802` 的 exact-v1 Deep Review 已保留。其机制为：The number of gradient samples q critically affects training: insufficient samples produce noisy gradients that plateau early, while excessive samples consume more computational resources. 为避免挤压 `TRAIN-DISTRIBUTED-TRAINING` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-18802:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-18840:start -->
`SF-2026-ARXIV-2607-18840` 的 exact-v1 Deep Review 已保留。其机制为：In this paper, we introduce WorldScape Policy 2.0, a controllable WAM with reasoning-augmented long short-term memory. 为避免挤压 `MULTIMODAL-WORLD-MODELS` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-18840:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-18847:start -->
`SF-2026-ARXIV-2607-18847` 的 exact-v1 Deep Review 已保留。其机制为：To address this challenge in multi agentic systems, we present a pre-deployment pipeline for scanning, hardening, and validation of agentic applications. 为避免挤压 `PLATFORM-SECURITY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-18847:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-18859:start -->
`SF-2026-ARXIV-2607-18859` 的 exact-v1 Deep Review 已保留。其机制为：To address these challenges, we present PhoenixRepair, a multi-agent framework that systematically explores multiple candidate edit locations and performs iterative reflection and refinement on patch generation, thereby expanding the search space of repair strategies. 为避免挤压 `AGENT-PLATFORM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-18859:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-18886:start -->
`SF-2026-ARXIV-2607-18886` 的 exact-v1 Deep Review 已保留。其机制为：To address these limitations, we propose TraceDev, a multi-agent framework for automated software development grounded in use cases that contain multiple functional points and complex semantics. 为避免挤压 `AGENT-WORKFLOW` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-18886:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-18915:start -->
`SF-2026-ARXIV-2607-18915` 的 exact-v1 Deep Review 已保留。其机制为：Compared with prior methods, SSC-GRPO achieves state-of-the-art performance on both mathematical reasoning benchmarks and hallucination leaderboards. 为避免挤压 `TRAIN-GRPO` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-18915:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-18957:start -->
`SF-2026-ARXIV-2607-18957` 的 exact-v1 Deep Review 已保留。其机制为：We propose the Communicating Finite Automata (CFA) abstraction to systematically analyze cross-component optimization opportunities, and design a programming framework to enable CFA-based component program refactoring. 为避免挤压 `PLATFORM-MODEL-REGISTRY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-18957:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-18975:start -->
`SF-2026-ARXIV-2607-18975` 的 exact-v1 Deep Review 已保留。其机制为：MiMemory is a step toward auditable, evidence-gated, and deployment-aware memory systems for Personal AI. 为避免挤压 `AGENT-MEMORY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-18975:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-18979:start -->
`SF-2026-ARXIV-2607-18979` 的 exact-v1 Deep Review 已保留。其机制为：We propose Parallel Shapley, a reinforcement learning framework that attributes fine-grained, path-level contributions in multi-path reasoning. 为避免挤压 `TRAIN-GRPO` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-18979:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-19102:start -->
`SF-2026-ARXIV-2607-19102` 的 exact-v1 Deep Review 已保留。其机制为：This paper presents Contrast, a system for multi-dimensional comparative trace analysis. 为避免挤压 `PLATFORM-TRACE` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-19102:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-19190:start -->
`SF-2026-ARXIV-2607-19190` 的 exact-v1 Deep Review 已保留。其机制为：We introduce \textit{Agentic Real2Sim}, a framework for generalized physical world modeling with vision-language agents, converting a real-world recording of object-robot interaction into a simulatable episodic twin which preserves observations, geometries, robot interactions, and object states. 为避免挤压 `MULTIMODAL-WORLD-MODELS` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-19190:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-19191:start -->
`SF-2026-ARXIV-2607-19191` 的 exact-v1 Deep Review 已保留。其机制为：We present ABot-World-0, an action-conditioned video world model for real-time, long-horizon closed-loop interaction, supported by a multi-source data infrastructure spanning AAA games, simulation engines, and internet videos to learn controllable world dynamics. 为避免挤压 `MULTIMODAL-WORLD-MODELS` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-19191:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-19214:start -->
`SF-2026-ARXIV-2607-19214` 的 exact-v1 Deep Review 已保留。其机制为：Agentic workloads systematically destroy this benefit: the agent sends a request, runs a tool or waits for approval for minutes, and by the time the follow-up is sent the cached prefix has been evicted, so the agent pays the full prefill again. 为避免挤压 `PLATFORM-COST` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-19214:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-19215:start -->
`SF-2026-ARXIV-2607-19215` 的 exact-v1 Deep Review 已保留。其机制为：Existing agent system research has improved role specialization, workflow topology, memory, and tool use, but often assumes a fixed stable execution environment. 为避免挤压 `AGENT-PLATFORM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-19215:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-19297:start -->
`SF-2026-ARXIV-2607-19297` 的 exact-v1 Deep Review 已保留。其机制为：Rather than treating LangGraph, a low-level orchestration framework for stateful agents, as a model-quality benchmark target, we present three executable recipes -- SQL analytics with repair loops, agentic retrieval-augmented generation with evidence gating, and human-in-the-loop policy review with interrupt and checkpoint recovery -- to show how typed state, conditional routing, deterministic tools, retries, interrupts, checkpoints, and traces fit together. 为避免挤压 `AGENT-WORKFLOW` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-19297:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-19301:start -->
`SF-2026-ARXIV-2607-19301` 的 exact-v1 Deep Review 已保留。其机制为：We propose PAGE-RAG, a projection-aware adaptive graph retrieval framework for reliable long-document question answering. 为避免挤压 `AGENT-RAG` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-19301:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-19338:start -->
`SF-2026-ARXIV-2607-19338` 的 exact-v1 Deep Review 已保留。其机制为：Existing cost-aware systems typically treat such failures as cascade decisions: try a cheap model first, then escalate hard cases to a stronger and more expensive model. 为避免挤压 `AGENT-PLATFORM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-19338:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-19339:start -->
`SF-2026-ARXIV-2607-19339` 的 exact-v1 Deep Review 已保留。其机制为：We introduce OmniReasoner, a tool-use post-training framework for Thinking with Long Audio-Video: omni-modal LLMs learn, via supervised fine-tuning and reinforcement learning, to decide whether and where to call a zoom-in tool before answering. 为避免挤压 `AGENT-TOOL-CALLING` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-19339:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-19343:start -->
`SF-2026-ARXIV-2607-19343` 的 exact-v1 Deep Review 已保留。其机制为：We introduce Masked Visual Actions, a pixel-space control interface that expresses action as a partially revealed trajectory of an arbitrary entity in a video. 为避免挤压 `MULTIMODAL-WORLD-MODELS` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-19343:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-19344:start -->
`SF-2026-ARXIV-2607-19344` 的 exact-v1 Deep Review 已保留。其机制为：We introduce appearance pointers, compact tokens that guide DiTs toward the correct appearance cues at the correct spatial locations by aligning text or image inputs with user-specified masks. 为避免挤压 `MULTIMODAL-GENERATIVE-PARADIGMS` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-19344:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-19345:start -->
`SF-2026-ARXIV-2607-19345` 的 exact-v1 Deep Review 已保留。其机制为：Motivated by this diagnosis, we propose GEAR (Grounding Evidence-Aware Reward), a reward shaping method that augments the accuracy signal with a grounding reward for overlap with key evidence and a distractor penalty for overlap with irrelevant context. 为避免挤压 `MODEL-LONG-CONTEXT` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-19345:end -->

### Selected Analysis Narratives

<!-- analysis:DA-20260722-01:start -->
### Searching for Plans You Can Actually Build: A Realizability-Aware Full-Space Optimizer for MoE Training and Serving

**约束变化与机制。** Mixture-of-Experts (MoE) systems split a program's plan space in two: the space a cost model can rank, and the smaller space a real toolchain can actually build.

**证明与未证明。** All predictions are pre-registered in a frozen, artifact-hashed adjudication file before the H800 runs, and every outcome is reported as-is. 但 VI-D Limitations and threats to validity We state the threats ourselves, and for each we bound what it does and does not undermine. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：VI-D Limitations and threats to validity We state the threats ourselves, and for each we bound what it does and does not undermine. 旧方案在不承受该约束时仍成立。

关联：`review:SF-2026-ARXIV-2607-18631`。
<!-- analysis:DA-20260722-01:end -->

<!-- analysis:DA-20260722-02:start -->
### Where Should Optimizer State Live? Tiered State Allocation for Memory-Efficient Mixture-of-Experts Training

**约束变化与机制。** On a 6.78B-parameter MoE language model AdamW keeps 50.6 GB of first and second moments to update 12.6 GB of bfloat16 weights.

**证明与未证明。** Where optimizer state lives, these results suggest, matters at least as much as how much of it there is. 但 Finally, the downstream evaluations are near chance and should be read as a completeness check, not evidence of capability. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：Finally, the downstream evaluations are near chance and should be read as a completeness check, not evidence of capability. 旧方案在不承受该约束时仍成立。

关联：`review:SF-2026-ARXIV-2607-19058`。
<!-- analysis:DA-20260722-02:end -->

<!-- analysis:DA-20260722-03:start -->
### ARBITER: Guarded Agentic Control for SLO-Oriented Kubernetes Remediation

**约束变化与机制。** We present ARBITER, a guarded control plane for SLO-oriented Kubernetes remediation.

**证明与未证明。** We release the controller, replay corpus, harnesses, safety tests, and figure artifacts: https://github.com/pooyan/arbiter. 但 Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 旧方案在不承受该约束时仍成立。

关联：`review:SF-2026-ARXIV-2607-19182`。
<!-- analysis:DA-20260722-03:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

None。建议路由已冻结到 date-local queue；最终 disposition 等待 root 按日期串行对读 Books。

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260722-COVERAGE-INDEPENDENT | fresh-context:pending-root-auditor | coverage | coverage:SRC-ARXIV:20260722 | GAP-20260722-COVERAGE-INDEPENDENT：全量筛选尚未被独立反向审计 | Pending — 逐项核验 false positive / false negative | open |
| SA-20260722-EVIDENCE-INDEPENDENT | fresh-context:pending-root-auditor | evidence | validator:review-completion-v1 | GAP-20260722-EVIDENCE-INDEPENDENT：RP 尚需独立对照 exact v1 | Pending — finding 绑定具体 family | open |
| SA-20260722-SELECTION-INDEPENDENT | fresh-context:pending-root-auditor | deep_analysis_selection | validator:deep-analysis-selection-v1 | GAP-20260722-SELECTION-INDEPENDENT：三项选择尚需 adversarial comparison | Pending — 比较 impact、反证与 owner 独立性 | open |
| SA-20260722-BOOKS-ROOT | fresh-context:pending-root-books-owner | books | validator:books-comparison-v1 | GAP-20260722-BOOKS-ROOT：尚未逐项对读 Books | Pending — root 消费 frozen queue | open |

## 8. Ignored Noise

399 项均有 family-specific pre-denominator closure：

- `embodied_task_local_method`：26
- `incremental_method_without_durable_system_delta`：313
- `local_benchmark_without_release_delta`：13
- `theory_without_ai_system_contract`：2
- `vertical_application_without_system_delta`：45

## 9. Recommended Action

1. 独立审计 Coverage、Evidence 与 Selection；finding 只重开具体 family。
2. root 逐项比较 Books。建议起点：Integrate 40、No Change 52、Structural 4；不是最终决定。

## 10. Repository Changes

- 重建 `papers/2026/07/22/README.md` 及 date-local frozen queue。
- 未修改 Books、ROADMAP、docs、Learning State、Weekly。

## 11. Open Questions

- 独立审计是否恢复 closure 中的漏项？
- proposed Integrate 是否已被现有 Books 命题覆盖？

## 12. Sources

- [Calibrated Selective Fact-Checking via Evidence Chain Evaluation](https://arxiv.org/html/2607.18240v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [BatchDAG: LLM-Planned Execution Graphs for Scalable Ad-Hoc Analysis Over Enterprise Data](https://arxiv.org/html/2607.18241v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [AI Tool Discovery at Scale: All You Need is DNS](https://arxiv.org/html/2607.18242v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [From Agent Failure Paths to Quantified Residual Risk: A Compositional Framework for Resilient Agentic AI](https://arxiv.org/html/2607.18243v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [Phionyx: A Deterministic AI Runtime Architecture with Structured State Management and Pre-Response Governance](https://arxiv.org/html/2607.18246v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [Beyond Accuracy and Cost: Latency-Aware LLM Query Routing for Dynamic Workloads](https://arxiv.org/html/2607.18253v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [Cross-Dialect Generalization Without Retraining: Benchmarks and Evaluation of Schema-Derived Constrained Decoding for MLIR](https://arxiv.org/html/2607.18254v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [When JSON Is Not Enough: Semantic Reliability of Schema-Constrained LLM Ordering Agents](https://arxiv.org/html/2607.18261v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [MUX: Continuous Reasoning via Multiplexed Tokens](https://arxiv.org/html/2607.18264v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [State Compression in Two-Agent LLM Relays: A Closed-World Study of Constraint Preservation](https://arxiv.org/html/2607.18265v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [Beyond Single-Dimensional Compression: The Compound Sparsity Frontier of Large Language Models](https://arxiv.org/html/2607.18280v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [Compressing What Matters: Neuron Importance Meets Data-Aware Low Rank Approximation for Language Model Compression](https://arxiv.org/html/2607.18284v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [Reliability Scales Inversely: Hallucinations Snowball Faster in Bigger Language Models](https://arxiv.org/html/2607.18292v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [On the Limits of Support-Preserving Alignment and Bounded Filtering](https://arxiv.org/html/2607.18295v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [The Information Shadow: Measuring Structural Limits on What Language Models Can Learn](https://arxiv.org/html/2607.18305v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [Interactive Training 2: Auditable Control Plane for Live Model Training](https://arxiv.org/html/2607.18314v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [Binding Drift in Multi-Step Tool-Augmented Agents](https://arxiv.org/html/2607.18316v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [EmoEUS: Uncertainty Supervision for Multimodal Emotion Recognition in Conversation](https://arxiv.org/html/2607.18336v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [A Decision-Centered Reference Architecture for Trustworthy Agentic Commerce](https://arxiv.org/html/2607.18347v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [Decode-Time Grammars: Constrained LLM Generation over a Refinement Order of Grammar Fragments](https://arxiv.org/html/2607.18357v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [HALLMARK: Diagnosing Three Failure Modes in LLM Citation Verifiers](https://arxiv.org/html/2607.18360v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [Operational Hallucination and Safety Drift in AI Agents](https://arxiv.org/pdf/2607.18366v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [AlayaWorld: Interactive Long-Horizon World Modeling -- Full Technical Report](https://arxiv.org/html/2607.18367v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [ChainMark: Model-Free LLM Watermarking with Closed-Form Calibration](https://arxiv.org/html/2607.18445v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [Estimating Rare Events in Language Models with Proper Evaluation](https://arxiv.org/html/2607.18454v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [Structured Output Collapses Answer Diversity Across 44 Language Models](https://arxiv.org/html/2607.18476v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [Search-on-Graph-R1: Training Large Language Models to Search Knowledge Graphs with Reinforcement Learning](https://arxiv.org/html/2607.18481v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [Trusted Credentials, Untrusted Behavior: Benchmarking LLM-Agent Security in High-Performance Computing](https://arxiv.org/html/2607.18485v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [Towards an Automated Test of LLM Security Knowledge](https://arxiv.org/html/2607.18496v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [Style over Substance: A Shortcut Audit of Emotion-Description Preference Evaluation](https://arxiv.org/html/2607.18508v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [Reasoning Fine-Tuning Induces Persistent Latent Policy States](https://arxiv.org/html/2607.18532v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [Engineering Trustworthy Agentic AI for Critical Systems](https://arxiv.org/html/2607.18548v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [Operational Proto-Introspection in Looped Language Models: Process-Quality Taps, Executable Branching, and the Readout-Control Boundary](https://arxiv.org/html/2607.18553v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [RECEIPT: Deterministic, Reward-Hacking-Resistant Verification for White-Box Agentic XSS Discovery](https://arxiv.org/html/2607.18575v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [Attention Without Grounding: Causal Evaluation of Visual Explanations in Medical VLMs](https://arxiv.org/html/2607.18577v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [STeP: Signal Temporal Logic for Precise Specifications for Action Generation with Vision Language Models](https://arxiv.org/html/2607.18580v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [AutoIndex: Learning Representation Programs for Retrieval](https://arxiv.org/html/2607.18603v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [Searching for Plans You Can Actually Build: A Realizability-Aware Full-Space Optimizer for MoE Training and Serving](https://arxiv.org/html/2607.18631v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [Mark, Don't Erase: Token Inoculation for Dual-Use Knowledge in LLMs](https://arxiv.org/html/2607.18639v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [Broken Gates: Re-evaluating Web Bot Defenses in the Age of LLM Agents](https://arxiv.org/html/2607.18659v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [DeforM: Reasoning-Guided Physics-Aware Video Generation via Spatial-Temporal Masking](https://arxiv.org/html/2607.18664v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [SciHazard: A Benchmark for Measuring Scientific Safety Risks with Decomposed Harm Scoring](https://arxiv.org/html/2607.18665v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [MissingBench-Verified: Probing Vision-Language Models' Inability to Detect Missing Object Parts](https://arxiv.org/html/2607.18673v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [When to Trust the Map: Confidence-Aware LLM Routing for Automotive CVE-to-ATM Mapping](https://arxiv.org/html/2607.18684v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [RoboInter1.5: A Holistic Intermediate Representation Suite for Embodied World Modeling and Robotic Manipulation](https://arxiv.org/html/2607.18709v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [LLM-Based Invariant Testing for Software Functional Bugs](https://arxiv.org/html/2607.18711v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [DWM: Separating World Effects from Actions in Latent World Models](https://arxiv.org/html/2607.18715v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [Stale but Stable: Staleness-Adaptive Trust Regions for Stabilizing Asynchronous Reinforcement Learning](https://arxiv.org/html/2607.18722v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [AgentDebugX: An Open-Source Toolkit for Failure Observability, Attribution, and Recovery in LLM Agents](https://arxiv.org/html/2607.18754v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [Relative Positions Generalize, Absolute Positions Memorize: An Implicit-Bias Account of Length Generalization in Attention](https://arxiv.org/html/2607.18759v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [SkillSight: Calibrating Generic Content Bias for Skill Retrieval](https://arxiv.org/html/2607.18785v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [QScheduler: Adaptive Gradient Sampling for Zeroth-Order On-Device Training on INT8 NPUs](https://arxiv.org/html/2607.18802v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [AgentTrails: Towards Trust and Reuse for Agentic Tasks](https://arxiv.org/html/2607.18816v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [VirtualSet: Typed Ontology Worlds as an LLM Generation Target for Grounded Queries and Guarded Decisions](https://arxiv.org/html/2607.18821v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [Cross-Agent Campaign Attribution: Linking Asynchronous Attacks Across LLM Agents](https://arxiv.org/html/2607.18826v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [Evaluating medical AI under missing information: same-provider judges and human raters change apparent safety](https://arxiv.org/html/2607.18828v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [WorldScape Policy 2.0: Empowering Steerable World Action Modeling with Reasoning-Augmented Memory](https://arxiv.org/html/2607.18840v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [Data Leakage Prevention in Agentic Applications via Preemptive Hardening](https://arxiv.org/html/2607.18847v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [PhoenixRepair: Rethinking Repair Strategy Exploration in Software Agents](https://arxiv.org/html/2607.18859v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [HindsightBench: A Black-Box Behavioral Audit Protocol for Parametric Hindsight in Time-Indexed LLM Decision Tasks](https://arxiv.org/html/2607.18867v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [TraceDev: A Traceability-Driven Multi-agent Framework for Requirement-to-Code Development](https://arxiv.org/html/2607.18886v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [Reasoning Error from Known Fact: Step-Level Self-Consistency Group Relative Policy Optimization for LLM](https://arxiv.org/html/2607.18915v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [TAP-RAG: Task-Aware Policy Control for Long-Document Multimodal Question Answering](https://arxiv.org/html/2607.18917v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [Learning Explicit Physical Parameter Control and Benchmarking for Video Generation](https://arxiv.org/html/2607.18924v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [InstantInfer: Enabling Fast LLM Cold Start with Communicating Finite Automata](https://arxiv.org/html/2607.18957v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [Mi-Memory: A Lifecycle Memory Framework for Personal AI](https://arxiv.org/html/2607.18975v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [Fishing Out Free Riders: Shapley-Based Reward Attribution for Parallel Reasoning via Reinforcement Learning](https://arxiv.org/html/2607.18979v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [From Collaboration to Regulation: Characterizing Governance Practice in Three Deep Learning Open Source Communities](https://arxiv.org/html/2607.19022v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [Content is What Remains: Invariant Speech Tokenization from Parallel Utterances](https://arxiv.org/html/2607.19033v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [FilmWorld: Agentic Novel-to-Film Generation through Dynamic Cinematic World Modeling](https://arxiv.org/html/2607.19038v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [Where Should Optimizer State Live? Tiered State Allocation for Memory-Efficient Mixture-of-Experts Training](https://arxiv.org/html/2607.19058v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [Supra Cognitive Modes: A Routed Architecture for Agent Memory](https://arxiv.org/html/2607.19096v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [Enabling Multi-Dimensional Distributed Trace Comparison with Contrast](https://arxiv.org/html/2607.19102v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [Text Template Tokens Are Implicit Semantic Registers in Diffusion Transformers](https://arxiv.org/html/2607.19139v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [ARBITER: Guarded Agentic Control for SLO-Oriented Kubernetes Remediation](https://arxiv.org/html/2607.19182v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [Agentic Real2Sim: Physics-based World Modeling with Vision-Language Agents](https://arxiv.org/html/2607.19190v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [ABot-World-0: Infinite Interactive World Rollout on a Single Desktop GPU](https://arxiv.org/html/2607.19191v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [Cognitive Dual-Process Planning for Autonomous Driving with Structured Scene Knowledge and Verifiable Reasoning-Action Consistency](https://arxiv.org/html/2607.19194v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [Keeping the Cache Warm Pays: Keepalive Economics for Agentic Workloads](https://arxiv.org/html/2607.19214v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [HACO: Hedged Agent Computing for Reliable LLM Systems](https://arxiv.org/html/2607.19215v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [Inference-Time Steering for Cross-Lingual Factual Consistency in LLMs](https://arxiv.org/html/2607.19243v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [Prompt Design at Scale: How Format, Instruction Count, and Context Length Shape Instruction Adherence and Hallucination in Large Language Models](https://arxiv.org/html/2607.19257v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [BioSecBench-Surveillance: A Verifiable Benchmark for AI Agents in Pathogen Genomic Surveillance](https://arxiv.org/html/2607.19262v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [They'll Verify. They Just Won't Act. How Authority Framing and Laundered Code Turn a Trusted Agentic CI/CD Pipeline Into an Attack Surface](https://arxiv.org/html/2607.19267v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [The safety failures we are not instrumenting: a perspective on hidden safety-critical challenges in modern AI systems](https://arxiv.org/html/2607.19292v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [Graph-Based Agentic AI with LangGraph: Workflow Pathways for Long-Running Stateful Business Processes](https://arxiv.org/html/2607.19297v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [PAGE-RAG: Evidence-Grounded Adaptive Graph Retrieval for Long-Document Question Answering](https://arxiv.org/html/2607.19301v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [CircuitKIT : Circuit Discovery, Evaluation, and Application Toolkit for Mechanistic Interpretability](https://arxiv.org/html/2607.19317v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [Two-Level Meta-Rubrics for Evaluating Open-Ended Generation: GAMUT, a Benchmark for Factual Completeness](https://arxiv.org/html/2607.19322v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [Selective State-Space Adaptation and Retrieval for Language Model Reasoning](https://arxiv.org/html/2607.19326v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [Agents in the Wild: Where Research Meets Deployment](https://arxiv.org/html/2607.19336v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [CodeRescue: Budget-Calibrated Recovery Routing for Coding Agents](https://arxiv.org/html/2607.19338v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [OmniReasoner: Thinking with Long Audio-Video via Native Tool Use](https://arxiv.org/html/2607.19339v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [Masked Visual Actions for Unified World Modeling](https://arxiv.org/html/2607.19343v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [Appearance Pointers -- Multimodal Region Control of Diffusion Transformers](https://arxiv.org/html/2607.19344v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04
- [Copy Less, Ground More: Overcoming Repetitive Copying in Long-Context Reasoning via Evidence-Aware Reinforcement Learning](https://arxiv.org/html/2607.19345v1) — first-public（Asia/Shanghai）：2026-07-22；exact evidence：v1；accessed：2026-09-04

## 13. Final Status

Author-side screening、denominator、exact-v1 access、96/96 Review 与 Deep Selection receipt 已构建；Books 写回冻结，四项独立审计未完成。

State Truth: Completion=In Progress；Coverage=Open；Evidence=Open；Books=Open；Unresolved Findings=4。
