# Daily Research — 2026-07-21

**Research Date:** 2026-07-21

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-07-20 09:00:00 ～ 2026-07-21 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；Historical Daily 独立重建，不使用 Weekly 作为 discovery、评分或 Review 来源

**Status:** In Progress；Coverage=Open、Evidence=Open、Books=Open；author-side evidence 已闭合，等待独立 Semantic Audit 与 root Books 比较

## Executive Summary

官方 owner inventory 共 **919** 个 identity；全量 title + abstract 筛选后冻结 **147** 个候选与 **772** 个 family-specific closure，retain rate **16.00%**。exact-v1 Review 为 147/147：Deep 33、Standard 114、blocked 0。

当前只是 author-side evidence 闭合：Books disposition 仍为 `Not Assessed`，四项 fresh-context 独立审计保持 Open。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-07-21 |
| Window End | 2026-07-21 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | daily-2026-07-21-0900-v2.1-sha256:8b30eecca0ca86dd1a13f9e9b422c261365aeefcee669ee053fc532107b147af |
| Denominator Frozen At | 2026-09-04T09:00:00+08:00 |
| Completion Status | In Progress |
| Coverage Gate | Open |
| Evidence Gate | Open |
| Books Gate | Open |

### Source Coverage Receipt

<!-- coverage:SRC-ARXIV:20260721:start -->
<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-07-20T09:00:00+08:00 | 2026-07-21T09:00:00+08:00 | 2026-09-04T09:00:00+08:00 | official listings + v1 history + availability schedule; DataCite created only for cycle reconciliation | checked | 919 | SF-2026-ARXIV-2607-16200;SF-2026-ARXIV-2607-16204;SF-2026-ARXIV-2607-16208;SF-2026-ARXIV-2607-16211;SF-2026-ARXIV-2607-16213;SF-2026-ARXIV-2607-16215;SF-2026-ARXIV-2607-16239;SF-2026-ARXIV-2607-16241;SF-2026-ARXIV-2607-16242;SF-2026-ARXIV-2607-16244;SF-2026-ARXIV-2607-16246;SF-2026-ARXIV-2607-16247;SF-2026-ARXIV-2607-16248;SF-2026-ARXIV-2607-16254;SF-2026-ARXIV-2607-16257;SF-2026-ARXIV-2607-16259;SF-2026-ARXIV-2607-16266;SF-2026-ARXIV-2607-16269;SF-2026-ARXIV-2607-16311;SF-2026-ARXIV-2607-16314;SF-2026-ARXIV-2607-16326;SF-2026-ARXIV-2607-16339;SF-2026-ARXIV-2607-16345;SF-2026-ARXIV-2607-16352;SF-2026-ARXIV-2607-16401;SF-2026-ARXIV-2607-16414;SF-2026-ARXIV-2607-16442;SF-2026-ARXIV-2607-16451;SF-2026-ARXIV-2607-16473;SF-2026-ARXIV-2607-16488;SF-2026-ARXIV-2607-16506;SF-2026-ARXIV-2607-16523;SF-2026-ARXIV-2607-16555;SF-2026-ARXIV-2607-16560;SF-2026-ARXIV-2607-16596;SF-2026-ARXIV-2607-16602;SF-2026-ARXIV-2607-16612;SF-2026-ARXIV-2607-16617;SF-2026-ARXIV-2607-16621;SF-2026-ARXIV-2607-16632;SF-2026-ARXIV-2607-16636;SF-2026-ARXIV-2607-16643;SF-2026-ARXIV-2607-16646;SF-2026-ARXIV-2607-16648;SF-2026-ARXIV-2607-16673;SF-2026-ARXIV-2607-16704;SF-2026-ARXIV-2607-16708;SF-2026-ARXIV-2607-16710;SF-2026-ARXIV-2607-16716;SF-2026-ARXIV-2607-16721;SF-2026-ARXIV-2607-16726;SF-2026-ARXIV-2607-16740;SF-2026-ARXIV-2607-16745;SF-2026-ARXIV-2607-16784;SF-2026-ARXIV-2607-16789;SF-2026-ARXIV-2607-16800;SF-2026-ARXIV-2607-16836;SF-2026-ARXIV-2607-16848;SF-2026-ARXIV-2607-16851;SF-2026-ARXIV-2607-16868;SF-2026-ARXIV-2607-16872;SF-2026-ARXIV-2607-16892;SF-2026-ARXIV-2607-16900;SF-2026-ARXIV-2607-16973;SF-2026-ARXIV-2607-16999;SF-2026-ARXIV-2607-17019;SF-2026-ARXIV-2607-17175;SF-2026-ARXIV-2607-17181;SF-2026-ARXIV-2607-17188;SF-2026-ARXIV-2607-17205;SF-2026-ARXIV-2607-17213;SF-2026-ARXIV-2607-17225;SF-2026-ARXIV-2607-17247;SF-2026-ARXIV-2607-17250;SF-2026-ARXIV-2607-17257;SF-2026-ARXIV-2607-17269;SF-2026-ARXIV-2607-17288;SF-2026-ARXIV-2607-17291;SF-2026-ARXIV-2607-17299;SF-2026-ARXIV-2607-17347;SF-2026-ARXIV-2607-17352;SF-2026-ARXIV-2607-17384;SF-2026-ARXIV-2607-17389;SF-2026-ARXIV-2607-17409;SF-2026-ARXIV-2607-17415;SF-2026-ARXIV-2607-17419;SF-2026-ARXIV-2607-17422;SF-2026-ARXIV-2607-17425;SF-2026-ARXIV-2607-17454;SF-2026-ARXIV-2607-17525;SF-2026-ARXIV-2607-17528;SF-2026-ARXIV-2607-17535;SF-2026-ARXIV-2607-17545;SF-2026-ARXIV-2607-17558;SF-2026-ARXIV-2607-17568;SF-2026-ARXIV-2607-17572;SF-2026-ARXIV-2607-17574;SF-2026-ARXIV-2607-17575;SF-2026-ARXIV-2607-17598;SF-2026-ARXIV-2607-17619;SF-2026-ARXIV-2607-17621;SF-2026-ARXIV-2607-17624;SF-2026-ARXIV-2607-17641;SF-2026-ARXIV-2607-17644;SF-2026-ARXIV-2607-17652;SF-2026-ARXIV-2607-17673;SF-2026-ARXIV-2607-17696;SF-2026-ARXIV-2607-17701;SF-2026-ARXIV-2607-17710;SF-2026-ARXIV-2607-17715;SF-2026-ARXIV-2607-17733;SF-2026-ARXIV-2607-17751;SF-2026-ARXIV-2607-17780;SF-2026-ARXIV-2607-17786;SF-2026-ARXIV-2607-17843;SF-2026-ARXIV-2607-17879;SF-2026-ARXIV-2607-17884;SF-2026-ARXIV-2607-17914;SF-2026-ARXIV-2607-17924;SF-2026-ARXIV-2607-17937;SF-2026-ARXIV-2607-17973;SF-2026-ARXIV-2607-17979;SF-2026-ARXIV-2607-17986;SF-2026-ARXIV-2607-18002;SF-2026-ARXIV-2607-18016;SF-2026-ARXIV-2607-18026;SF-2026-ARXIV-2607-18039;SF-2026-ARXIV-2607-18046;SF-2026-ARXIV-2607-18057;SF-2026-ARXIV-2607-18060;SF-2026-ARXIV-2607-18063;SF-2026-ARXIV-2607-18080;SF-2026-ARXIV-2607-18081;SF-2026-ARXIV-2607-18086;SF-2026-ARXIV-2607-18098;SF-2026-ARXIV-2607-18100;SF-2026-ARXIV-2607-18101;SF-2026-ARXIV-2607-18108;SF-2026-ARXIV-2607-18110;SF-2026-ARXIV-2607-18114;SF-2026-ARXIV-2607-18141;SF-2026-ARXIV-2607-18155;SF-2026-ARXIV-2607-18161;SF-2026-ARXIV-2607-18171;SF-2026-ARXIV-2607-18199;SF-2026-ARXIV-2607-18213;SF-2026-ARXIV-2607-18231 | all registered category pages; cross-category dedup complete | 2026-07-21T09:00:00+08:00 | sha256:8b30eecca0ca86dd1a13f9e9b422c261365aeefcee669ee053fc532107b147af | — |
<!-- coverage:SRC-ARXIV:20260721:end -->

### Coverage Limitations

- DataCite 只辅助 owner reconciliation；技术结论全部回到 official exact arXiv v1。
- author-side receipt 已闭合，独立 false-positive / false-negative audit 尚未签收。

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-16200 | arXiv:2607.16200v1 | paper-v1:2607.16200 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-16200 | self | — | new_in_window | AGENT-PLATFORM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16204 | arXiv:2607.16204v1 | paper-v1:2607.16204 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-16204 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16208 | arXiv:2607.16208v1 | paper-v1:2607.16208 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-16208 | self | — | new_in_window | AGENT-RAG | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16211 | arXiv:2607.16211v1 | paper-v1:2607.16211 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-16211 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16213 | arXiv:2607.16213v1 | paper-v1:2607.16213 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-16213 | self | — | new_in_window | INFER-KV-CACHE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16215 | arXiv:2607.16215v1 | paper-v1:2607.16215 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-16215 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16239 | arXiv:2607.16239v1 | paper-v1:2607.16239 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-16239 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16241 | arXiv:2607.16241v1 | paper-v1:2607.16241 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-16241 | self | — | new_in_window | INFER-TENSORRT-LLM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16242 | arXiv:2607.16242v1 | paper-v1:2607.16242 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-16242 | self | — | new_in_window | TRAIN-RLHF | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16244 | arXiv:2607.16244v1 | paper-v1:2607.16244 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-16244 | self | — | new_in_window | TRAIN-GRPO | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16246 | arXiv:2607.16246v1 | paper-v1:2607.16246 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-16246 | self | — | new_in_window | TRAIN-PRETRAINING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16247 | arXiv:2607.16247v1 | paper-v1:2607.16247 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-16247 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16248 | arXiv:2607.16248v1 | paper-v1:2607.16248 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-16248 | self | — | new_in_window | INFER-KV-CACHE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16254 | arXiv:2607.16254v1 | paper-v1:2607.16254 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-16254 | self | — | new_in_window | MODEL-FFN | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16257 | arXiv:2607.16257v1 | paper-v1:2607.16257 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-16257 | self | — | new_in_window | TRAIN-GRPO | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16259 | arXiv:2607.16259v1 | paper-v1:2607.16259 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-16259 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16266 | arXiv:2607.16266v1 | paper-v1:2607.16266 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-16266 | self | — | new_in_window | AGENT-MULTI-AGENT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16269 | arXiv:2607.16269v1 | paper-v1:2607.16269 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-16269 | self | — | new_in_window | AGENT-PLATFORM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16311 | arXiv:2607.16311v1 | paper-v1:2607.16311 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-16311 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16314 | arXiv:2607.16314v1 | paper-v1:2607.16314 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-16314 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16326 | arXiv:2607.16326v1 | paper-v1:2607.16326 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-16326 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16339 | arXiv:2607.16339v1 | paper-v1:2607.16339 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-16339 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16345 | arXiv:2607.16345v1 | paper-v1:2607.16345 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-16345 | self | — | new_in_window | AGENT-PLATFORM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16352 | arXiv:2607.16352v1 | paper-v1:2607.16352 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-16352 | self | — | new_in_window | AGENT-TOOL-CALLING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16401 | arXiv:2607.16401v1 | paper-v1:2607.16401 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-16401 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16414 | arXiv:2607.16414v1 | paper-v1:2607.16414 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-16414 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16442 | arXiv:2607.16442v1 | paper-v1:2607.16442 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-16442 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16451 | arXiv:2607.16451v1 | paper-v1:2607.16451 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-16451 | self | — | new_in_window | WORLDVIEW-LLM-INTELLIGENCE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16473 | arXiv:2607.16473v1 | paper-v1:2607.16473 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-16473 | self | — | new_in_window | INFER-SCHEDULING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16488 | arXiv:2607.16488v1 | paper-v1:2607.16488 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-16488 | self | — | new_in_window | INFER-SCHEDULING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16506 | arXiv:2607.16506v1 | paper-v1:2607.16506 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-16506 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16523 | arXiv:2607.16523v1 | paper-v1:2607.16523 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-16523 | self | — | new_in_window | MODEL-SAMPLING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16555 | arXiv:2607.16555v1 | paper-v1:2607.16555 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-16555 | self | — | new_in_window | INFER-TENSORRT-LLM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16560 | arXiv:2607.16560v1 | paper-v1:2607.16560 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-16560 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16596 | arXiv:2607.16596v1 | paper-v1:2607.16596 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-16596 | self | — | new_in_window | PLATFORM-MODEL-REGISTRY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16602 | arXiv:2607.16602v1 | paper-v1:2607.16602 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-16602 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16612 | arXiv:2607.16612v1 | paper-v1:2607.16612 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-16612 | self | — | new_in_window | TRAIN-PRETRAINING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16617 | arXiv:2607.16617v1 | paper-v1:2607.16617 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-16617 | self | — | new_in_window | TRAIN-DATA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16621 | arXiv:2607.16621v1 | paper-v1:2607.16621 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-16621 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16632 | arXiv:2607.16632v1 | paper-v1:2607.16632 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-16632 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16636 | arXiv:2607.16636v1 | paper-v1:2607.16636 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-16636 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16643 | arXiv:2607.16643v1 | paper-v1:2607.16643 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-16643 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16646 | arXiv:2607.16646v1 | paper-v1:2607.16646 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-16646 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16648 | arXiv:2607.16648v1 | paper-v1:2607.16648 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-16648 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16673 | arXiv:2607.16673v1 | paper-v1:2607.16673 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-16673 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16704 | arXiv:2607.16704v1 | paper-v1:2607.16704 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-16704 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16708 | arXiv:2607.16708v1 | paper-v1:2607.16708 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-16708 | self | — | new_in_window | AGENT-MULTI-AGENT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16710 | arXiv:2607.16710v1 | paper-v1:2607.16710 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-16710 | self | — | new_in_window | TRAIN-DATA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16716 | arXiv:2607.16716v1 | paper-v1:2607.16716 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-16716 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16721 | arXiv:2607.16721v1 | paper-v1:2607.16721 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-16721 | self | — | new_in_window | MODEL-MOE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16726 | arXiv:2607.16726v1 | paper-v1:2607.16726 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-16726 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16740 | arXiv:2607.16740v1 | paper-v1:2607.16740 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-16740 | self | — | new_in_window | AGENT-PLATFORM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16745 | arXiv:2607.16745v1 | paper-v1:2607.16745 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-16745 | self | — | new_in_window | AGENT-MULTI-AGENT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16784 | arXiv:2607.16784v1 | paper-v1:2607.16784 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-16784 | self | — | new_in_window | INFER-SCHEDULING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16789 | arXiv:2607.16789v1 | paper-v1:2607.16789 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-16789 | self | — | new_in_window | TRAIN-LORA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16800 | arXiv:2607.16800v1 | paper-v1:2607.16800 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-16800 | self | — | new_in_window | TRAIN-PRETRAINING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16836 | arXiv:2607.16836v1 | paper-v1:2607.16836 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-16836 | self | — | new_in_window | PLATFORM-FOUNDATIONS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16848 | arXiv:2607.16848v1 | paper-v1:2607.16848 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-16848 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16851 | arXiv:2607.16851v1 | paper-v1:2607.16851 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-16851 | self | — | new_in_window | AGENT-PLATFORM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16868 | arXiv:2607.16868v1 | paper-v1:2607.16868 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-16868 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16872 | arXiv:2607.16872v1 | paper-v1:2607.16872 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-16872 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16892 | arXiv:2607.16892v1 | paper-v1:2607.16892 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-16892 | self | — | new_in_window | INFER-KV-CACHE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16900 | arXiv:2607.16900v1 | paper-v1:2607.16900 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-16900 | self | — | new_in_window | AGENT-TOOL-CALLING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16973 | arXiv:2607.16973v1 | paper-v1:2607.16973 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-16973 | self | — | new_in_window | AGENT-RAG | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16999 | arXiv:2607.16999v1 | paper-v1:2607.16999 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-16999 | self | — | new_in_window | TRAIN-GRPO | Not Assessed | — | no |
| SF-2026-ARXIV-2607-17019 | arXiv:2607.17019v1 | paper-v1:2607.17019 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-17019 | self | — | new_in_window | INFER-KV-CACHE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-17175 | arXiv:2607.17175v1 | paper-v1:2607.17175 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-17175 | self | — | new_in_window | INFER-SCHEDULING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-17181 | arXiv:2607.17181v1 | paper-v1:2607.17181 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-17181 | self | — | new_in_window | INFER-SCHEDULING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-17188 | arXiv:2607.17188v1 | paper-v1:2607.17188 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-17188 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-17205 | arXiv:2607.17205v1 | paper-v1:2607.17205 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-17205 | self | — | new_in_window | TRAIN-DATA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-17213 | arXiv:2607.17213v1 | paper-v1:2607.17213 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-17213 | self | — | new_in_window | AGENT-WORKFLOW | Not Assessed | — | no |
| SF-2026-ARXIV-2607-17225 | arXiv:2607.17225v1 | paper-v1:2607.17225 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-17225 | self | — | new_in_window | AGENT-PLATFORM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-17247 | arXiv:2607.17247v1 | paper-v1:2607.17247 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-17247 | self | — | new_in_window | TRAIN-GRPO | Not Assessed | — | no |
| SF-2026-ARXIV-2607-17250 | arXiv:2607.17250v1 | paper-v1:2607.17250 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-17250 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-17257 | arXiv:2607.17257v1 | paper-v1:2607.17257 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-17257 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-17269 | arXiv:2607.17269v1 | paper-v1:2607.17269 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-17269 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-17288 | arXiv:2607.17288v1 | paper-v1:2607.17288 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-17288 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-17291 | arXiv:2607.17291v1 | paper-v1:2607.17291 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-17291 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-17299 | arXiv:2607.17299v1 | paper-v1:2607.17299 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-17299 | self | — | new_in_window | TRAIN-GRPO | Not Assessed | — | no |
| SF-2026-ARXIV-2607-17347 | arXiv:2607.17347v1 | paper-v1:2607.17347 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-17347 | self | — | new_in_window | AGENT-PLATFORM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-17352 | arXiv:2607.17352v1 | paper-v1:2607.17352 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-17352 | self | — | new_in_window | AGENT-REFLECTION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-17384 | arXiv:2607.17384v1 | paper-v1:2607.17384 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-17384 | self | — | new_in_window | AGENT-MULTI-AGENT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-17389 | arXiv:2607.17389v1 | paper-v1:2607.17389 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-17389 | self | — | new_in_window | INFER-TENSORRT-LLM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-17409 | arXiv:2607.17409v1 | paper-v1:2607.17409 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-17409 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-17415 | arXiv:2607.17415v1 | paper-v1:2607.17415 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-17415 | self | — | new_in_window | INFER-SCHEDULING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-17419 | arXiv:2607.17419v1 | paper-v1:2607.17419 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-17419 | self | — | new_in_window | MODEL-SELF-ATTENTION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-17422 | arXiv:2607.17422v1 | paper-v1:2607.17422 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-17422 | self | — | new_in_window | INFER-SCHEDULING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-17425 | arXiv:2607.17425v1 | paper-v1:2607.17425 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-17425 | self | — | new_in_window | WORLDVIEW-REPRESENTATION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-17454 | arXiv:2607.17454v1 | paper-v1:2607.17454 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-17454 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-17525 | arXiv:2607.17525v1 | paper-v1:2607.17525 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-17525 | self | — | new_in_window | PLATFORM-GATEWAY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-17528 | arXiv:2607.17528v1 | paper-v1:2607.17528 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-17528 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-17535 | arXiv:2607.17535v1 | paper-v1:2607.17535 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-17535 | self | — | new_in_window | AGENT-RAG | Not Assessed | — | no |
| SF-2026-ARXIV-2607-17545 | arXiv:2607.17545v1 | paper-v1:2607.17545 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-17545 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-17558 | arXiv:2607.17558v1 | paper-v1:2607.17558 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-17558 | self | — | new_in_window | AGENT-RAG | Not Assessed | — | no |
| SF-2026-ARXIV-2607-17568 | arXiv:2607.17568v1 | paper-v1:2607.17568 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-17568 | self | — | new_in_window | INFER-GPU-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-17572 | arXiv:2607.17572v1 | paper-v1:2607.17572 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-17572 | self | — | new_in_window | TRAIN-GRPO | Not Assessed | — | no |
| SF-2026-ARXIV-2607-17574 | arXiv:2607.17574v1 | paper-v1:2607.17574 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-17574 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-17575 | arXiv:2607.17575v1 | paper-v1:2607.17575 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-17575 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-17598 | arXiv:2607.17598v1 | paper-v1:2607.17598 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-17598 | self | — | new_in_window | AGENT-CONTEXT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-17619 | arXiv:2607.17619v1 | paper-v1:2607.17619 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-17619 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-17621 | arXiv:2607.17621v1 | paper-v1:2607.17621 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-17621 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-17624 | arXiv:2607.17624v1 | paper-v1:2607.17624 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-17624 | self | — | new_in_window | MODEL-TRANSFORMER-LAYER | Not Assessed | — | no |
| SF-2026-ARXIV-2607-17641 | arXiv:2607.17641v1 | paper-v1:2607.17641 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-17641 | self | — | new_in_window | AGENT-REFLECTION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-17644 | arXiv:2607.17644v1 | paper-v1:2607.17644 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-17644 | self | — | new_in_window | TRAIN-TENSOR-PARALLEL | Not Assessed | — | no |
| SF-2026-ARXIV-2607-17652 | arXiv:2607.17652v1 | paper-v1:2607.17652 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-17652 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-17673 | arXiv:2607.17673v1 | paper-v1:2607.17673 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-17673 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-17696 | arXiv:2607.17696v1 | paper-v1:2607.17696 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-17696 | self | — | new_in_window | MODEL-LONG-CONTEXT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-17701 | arXiv:2607.17701v1 | paper-v1:2607.17701 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-17701 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-17710 | arXiv:2607.17710v1 | paper-v1:2607.17710 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-17710 | self | — | new_in_window | AGENT-PLANNING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-17715 | arXiv:2607.17715v1 | paper-v1:2607.17715 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-17715 | self | — | new_in_window | INFER-KV-CACHE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-17733 | arXiv:2607.17733v1 | paper-v1:2607.17733 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-17733 | self | — | new_in_window | INFER-GPU-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-17751 | arXiv:2607.17751v1 | paper-v1:2607.17751 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-17751 | self | — | new_in_window | AGENT-TOOL-CALLING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-17780 | arXiv:2607.17780v1 | paper-v1:2607.17780 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-17780 | self | — | new_in_window | AGENT-PLATFORM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-17786 | arXiv:2607.17786v1 | paper-v1:2607.17786 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-17786 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-17843 | arXiv:2607.17843v1 | paper-v1:2607.17843 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-17843 | self | — | new_in_window | MODEL-TRANSFORMER-LAYER | Not Assessed | — | no |
| SF-2026-ARXIV-2607-17879 | arXiv:2607.17879v1 | paper-v1:2607.17879 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-17879 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-17884 | arXiv:2607.17884v1 | paper-v1:2607.17884 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-17884 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-17914 | arXiv:2607.17914v1 | paper-v1:2607.17914 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-17914 | self | — | new_in_window | AGENT-MULTI-AGENT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-17924 | arXiv:2607.17924v1 | paper-v1:2607.17924 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-17924 | self | — | new_in_window | TRAIN-GRPO | Not Assessed | — | no |
| SF-2026-ARXIV-2607-17937 | arXiv:2607.17937v1 | paper-v1:2607.17937 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-17937 | self | — | new_in_window | AGENT-CONTEXT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-17973 | arXiv:2607.17973v1 | paper-v1:2607.17973 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-17973 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-17979 | arXiv:2607.17979v1 | paper-v1:2607.17979 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-17979 | self | — | new_in_window | INFER-TENSORRT-LLM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-17986 | arXiv:2607.17986v1 | paper-v1:2607.17986 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-17986 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18002 | arXiv:2607.18002v1 | paper-v1:2607.18002 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-18002 | self | — | new_in_window | INFER-SCHEDULING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18016 | arXiv:2607.18016v1 | paper-v1:2607.18016 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-18016 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18026 | arXiv:2607.18026v1 | paper-v1:2607.18026 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-18026 | self | — | new_in_window | TRAIN-PRETRAINING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18039 | arXiv:2607.18039v1 | paper-v1:2607.18039 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-18039 | self | — | new_in_window | AGENT-WORKFLOW | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18046 | arXiv:2607.18046v1 | paper-v1:2607.18046 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-18046 | self | — | new_in_window | TRAIN-DATA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18057 | arXiv:2607.18057v1 | paper-v1:2607.18057 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-18057 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18060 | arXiv:2607.18060v1 | paper-v1:2607.18060 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-18060 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18063 | arXiv:2607.18063v1 | paper-v1:2607.18063 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-18063 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18080 | arXiv:2607.18080v1 | paper-v1:2607.18080 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-18080 | self | — | new_in_window | AGENT-RAG | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18081 | arXiv:2607.18081v1 | paper-v1:2607.18081 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-18081 | self | — | new_in_window | INFER-GPU-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18086 | arXiv:2607.18086v1 | paper-v1:2607.18086 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-18086 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18098 | arXiv:2607.18098v1 | paper-v1:2607.18098 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-18098 | self | — | new_in_window | INFER-SCHEDULING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18100 | arXiv:2607.18100v1 | paper-v1:2607.18100 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-18100 | self | — | new_in_window | MODEL-SAMPLING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18101 | arXiv:2607.18101v1 | paper-v1:2607.18101 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-18101 | self | — | new_in_window | INFER-TENSORRT-LLM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18108 | arXiv:2607.18108v1 | paper-v1:2607.18108 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-18108 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18110 | arXiv:2607.18110v1 | paper-v1:2607.18110 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-18110 | self | — | new_in_window | TRAIN-RLHF | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18114 | arXiv:2607.18114v1 | paper-v1:2607.18114 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-18114 | self | — | new_in_window | TRAIN-RLHF | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18141 | arXiv:2607.18141v1 | paper-v1:2607.18141 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-18141 | self | — | new_in_window | INFER-GPU-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18155 | arXiv:2607.18155v1 | paper-v1:2607.18155 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-18155 | self | — | new_in_window | AGENT-RAG | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18161 | arXiv:2607.18161v1 | paper-v1:2607.18161 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-18161 | self | — | new_in_window | AGENT-PLATFORM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18171 | arXiv:2607.18171v1 | paper-v1:2607.18171 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-18171 | self | — | new_in_window | AGENT-PLATFORM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18199 | arXiv:2607.18199v1 | paper-v1:2607.18199 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-18199 | self | — | new_in_window | TRAIN-DATA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18213 | arXiv:2607.18213v1 | paper-v1:2607.18213 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-18213 | self | — | new_in_window | AGENT-PLATFORM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-18231 | arXiv:2607.18231v1 | paper-v1:2607.18231 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-18231 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-16200 | RP-0b06f4b530f95ce0 | standard | arXiv:2607.16200v1 | SRC-ARXIV@arXiv:2607.16200v1 | https://arxiv.org/pdf/2607.16200v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.16200v1#page=2 — PDF page 2 | https://arxiv.org/pdf/2607.16200v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.16200v1#page=2 — PDF page 2 | https://arxiv.org/pdf/2607.16200v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.16200v1#page=2 — PDF page 2 | Exact v1 links https://github.com/abshkbh/arrakis, https://github.com/spf13/cobra, https://github.com/elazarl/goproxy; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16200 | complete |
| SF-2026-ARXIV-2607-16204 | RP-593e73ee93237526 | deep | arXiv:2607.16204v1 | SRC-ARXIV@arXiv:2607.16204v1 | https://arxiv.org/html/2607.16204v1#A3 — Appendix C World Model Training Dataset Curation Details; https://arxiv.org/html/2607.16204v1#A4 — Appendix D Environment Setup for Downstream RL Agent Training with World Model Backend | https://arxiv.org/html/2607.16204v1#A1 — Appendix A Human Evaluations; https://arxiv.org/html/2607.16204v1#A2 — Appendix B Fairness of Evaluation | https://arxiv.org/html/2607.16204v1#A8 — Appendix H World Model Failure Modes; https://arxiv.org/html/2607.16204v1#S5 — 5 Results and Discussion | Exact v1 links https://huggingface.co/PatronusAI/world_model_corpus, https://github.com/patronus-ai/mdlm_world_modeling, https://huggingface.co/datasets/danilopeixoto/pandora-tool-calling; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16204 | complete |
| SF-2026-ARXIV-2607-16208 | RP-60627647630b95b2 | standard | arXiv:2607.16208v1 | SRC-ARXIV@arXiv:2607.16208v1 | https://arxiv.org/html/2607.16208v1#S3 — 3 Method; https://arxiv.org/html/2607.16208v1#S4.SS1 — 4.1 Experimental objective and design | https://arxiv.org/html/2607.16208v1#S4 — 4 Experiments; https://arxiv.org/html/2607.16208v1#S4.SS1 — 4.1 Experimental objective and design | https://arxiv.org/html/2607.16208v1#S5 — 5 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16208 | complete |
| SF-2026-ARXIV-2607-16211 | RP-a2bfaa4a96f65394 | standard | arXiv:2607.16211v1 | SRC-ARXIV@arXiv:2607.16211v1 | https://arxiv.org/html/2607.16211v1#S2.SS2 — 2.2 Agent Frameworks and Planning; https://arxiv.org/html/2607.16211v1#S3 — 3 Method | https://arxiv.org/html/2607.16211v1#S2.SS4 — 2.4 Memory Evaluation Benchmarks; https://arxiv.org/html/2607.16211v1#S3.SS9 — 3.9 Convergence Analysis | https://arxiv.org/html/2607.16211v1#S6 — 6 Discussion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16211 | complete |
| SF-2026-ARXIV-2607-16213 | RP-b9cd8ab629a9d5e3 | deep | arXiv:2607.16213v1 | SRC-ARXIV@arXiv:2607.16213v1 | https://arxiv.org/html/2607.16213v1#S3 — 3 Method; https://arxiv.org/html/2607.16213v1#A6 — Appendix F Implementation Details | https://arxiv.org/html/2607.16213v1#A3 — Appendix C Category-Level Analysis; https://arxiv.org/html/2607.16213v1#A5 — Appendix E Long-Context Evaluation (31,500 Tokens) | https://arxiv.org/html/2607.16213v1#S5 — 5 Conclusion | Exact v1 links https://github.com/ThisisBillhe/ZipCache/, https://github.com/SUSTechBruce/LOOK-M, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16213 | complete |
| SF-2026-ARXIV-2607-16215 | RP-599969fb507d96e3 | standard | arXiv:2607.16215v1 | SRC-ARXIV@arXiv:2607.16215v1 | https://arxiv.org/html/2607.16215v1#S2.SS1 — 2.1 Responsible AI Evaluation Frameworks; https://arxiv.org/html/2607.16215v1#S3 — 3 Methodology | https://arxiv.org/html/2607.16215v1#S2.SS1 — 2.1 Responsible AI Evaluation Frameworks; https://arxiv.org/html/2607.16215v1#S3.SS1 — 3.1 Multi-Dimensional Evaluation | https://arxiv.org/html/2607.16215v1#S4.SS3 — 4.3 Experiment 1: Baseline Failure Rate (RQ1); https://arxiv.org/html/2607.16215v1#S5.SS1 — 5.1 Experiment 1: Baseline Failure Rate | Exact v1 links https://github.com/Responsible-AI-Labs/rail-score-sdk, https://github.com/Responsible-AI-Labs/rail-score-js, https://huggingface.co/datasets/responsible-ai-labs/rail-guard-benchmark; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16215 | complete |
| SF-2026-ARXIV-2607-16239 | RP-0d04310b82cc37b0 | standard | arXiv:2607.16239v1 | SRC-ARXIV@arXiv:2607.16239v1 | https://arxiv.org/html/2607.16239v1#A1.SS2 — A.2 WebDesign evaluation; https://arxiv.org/html/2607.16239v1#A4.SS1 — D.1 Framework | https://arxiv.org/html/2607.16239v1#A1 — Appendix A Additional Evaluation Results; https://arxiv.org/html/2607.16239v1#A1.SS1 — A.1 More on MQM evaluation | https://arxiv.org/html/2607.16239v1#S4 — 4 Discussion | Exact v1 links https://github.com/diaryofnewton/bacon-calibration, https://github.com/tatsu-lab/alpaca_eval, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16239 | complete |
| SF-2026-ARXIV-2607-16241 | RP-9e13f7825d4840cf | deep | arXiv:2607.16241v1 | SRC-ARXIV@arXiv:2607.16241v1 | https://arxiv.org/html/2607.16241v1#A12.SS1 — L.1 Methodology; https://arxiv.org/html/2607.16241v1#S2 — 2 Evaluation Methodology | https://arxiv.org/html/2607.16241v1#A10 — Appendix J Tolerance Sensitivity Analysis; https://arxiv.org/html/2607.16241v1#A12.SS2 — L.2 Aggregate Results | https://arxiv.org/html/2607.16241v1#A12.SS4 — L.4 Discussion; https://arxiv.org/html/2607.16241v1#A7 — Appendix G Failure Mode Analysis | Exact v1 links https://github.com/facebookresearch/kernel_bench_verified, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16241 | complete |
| SF-2026-ARXIV-2607-16242 | RP-1605f5366422ca92 | standard | arXiv:2607.16242v1 | SRC-ARXIV@arXiv:2607.16242v1 | https://arxiv.org/html/2607.16242v1#S5.SS5 — V-E Integration and Boost on Existing Methods; https://arxiv.org/html/2607.16242v1#A1.SS1 — A-A Implementation Details | https://arxiv.org/html/2607.16242v1#A1.SS2 — A-B Full Utility Results across Fine-Tuning Depth; https://arxiv.org/html/2607.16242v1#A1.SS3 — A-C Ablation Study | https://arxiv.org/html/2607.16242v1#S7 — VII Discussion and Limitations; https://arxiv.org/html/2607.16242v1#S7.SS2 — VII-B Limitations and Future Directions | Exact v1 links https://huggingface.co/datasets/b-mc2/sql-create-context, https://github.com/huggingface/accelerate, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16242 | complete |
| SF-2026-ARXIV-2607-16244 | RP-dcadd7b52ee98bb0 | deep | arXiv:2607.16244v1 | SRC-ARXIV@arXiv:2607.16244v1 | https://arxiv.org/html/2607.16244v1#S4 — 4 CIGPO Method | https://arxiv.org/html/2607.16244v1#S6.SS3 — 6.3 Full Benchmark Results; https://arxiv.org/html/2607.16244v1#S5 — 5 Experimental Setup | https://arxiv.org/html/2607.16244v1#A1.SS3 — A.3 CIGPO Failure Example (Step 200, Valid Format); https://arxiv.org/html/2607.16244v1#S7 — 7 Discussion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16244 | complete |
| SF-2026-ARXIV-2607-16246 | RP-a9277d646f508f52 | deep | arXiv:2607.16246v1 | SRC-ARXIV@arXiv:2607.16246v1 | https://arxiv.org/html/2607.16246v1#S5.SS1 — 5.1 Experimental Design; https://arxiv.org/html/2607.16246v1#S4.SS1 — 4.1 Model Setup | https://arxiv.org/html/2607.16246v1#S4 — 4 Experimental Setup; https://arxiv.org/html/2607.16246v1#S4.SS3 — 4.3 Evaluation Protocol | https://arxiv.org/html/2607.16246v1#S8 — 8 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16246 | complete |
| SF-2026-ARXIV-2607-16247 | RP-7dc890a3c91582e6 | standard | arXiv:2607.16247v1 | SRC-ARXIV@arXiv:2607.16247v1 | https://arxiv.org/html/2607.16247v1#Pt0.A1 — Appendix 0.A Additional Method Details; https://arxiv.org/html/2607.16247v1#S4 — 4 Method | https://arxiv.org/html/2607.16247v1#Pt0.A2.SS5 — 0.B.5 Evaluation Protocol and Inference Cost; https://arxiv.org/html/2607.16247v1#Pt0.A3 — Appendix 0.C Extended Experimental Details | https://arxiv.org/html/2607.16247v1#Pt0.A4.SS2 — 0.D.2 Limitations and Future Work; https://arxiv.org/html/2607.16247v1#S6 — 6 Conclusion | Exact v1 links https://github.com/DyMessi/JIT-Memory, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16247 | complete |
| SF-2026-ARXIV-2607-16248 | RP-9848ef3a3572e97b | deep | arXiv:2607.16248v1 | SRC-ARXIV@arXiv:2607.16248v1 | https://arxiv.org/html/2607.16248v1#S4 — 4 Methodology | https://arxiv.org/html/2607.16248v1#S3.SS2 — 3.2 Decode-Time Analysis of Accuracy Loss; https://arxiv.org/html/2607.16248v1#S5 — 5 Experimental Setup | https://arxiv.org/html/2607.16248v1#S7 — 7 Limitations and Future Work; https://arxiv.org/html/2607.16248v1#S6 — 6 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16248 | complete |
| SF-2026-ARXIV-2607-16254 | RP-fcff4fbde066cd86 | standard | arXiv:2607.16254v1 | SRC-ARXIV@arXiv:2607.16254v1 | https://arxiv.org/html/2607.16254v1#S3.SS2 — 3.2 Intervention design: native FFN scaling | https://arxiv.org/html/2607.16254v1#S4 — 4 Experimental Setup; https://arxiv.org/html/2607.16254v1#S5 — 5 Results | https://arxiv.org/html/2607.16254v1#S6 — 6 Discussion; https://arxiv.org/html/2607.16254v1#S7 — 7 Limitations | Exact v1 links https://github.com/gkamradt/needle-in-a-haystack, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16254 | complete |
| SF-2026-ARXIV-2607-16257 | RP-b3fbeb9a296c4b5a | standard | arXiv:2607.16257v1 | SRC-ARXIV@arXiv:2607.16257v1 | https://arxiv.org/html/2607.16257v1#A3 — Appendix C Embedding Model Ablation | https://arxiv.org/html/2607.16257v1#A1 — Appendix A Experimental Details; https://arxiv.org/html/2607.16257v1#A1.SS2 — A.2 Experimental Settings. | https://arxiv.org/html/2607.16257v1#S7 — 7 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16257 | complete |
| SF-2026-ARXIV-2607-16259 | RP-a930c3318c41fe6b | standard | arXiv:2607.16259v1 | SRC-ARXIV@arXiv:2607.16259v1 | https://arxiv.org/html/2607.16259v1#A1 — Appendix A Rank CIs definitions and methods; https://arxiv.org/html/2607.16259v1#S2.SS2 — 2.2 Statistical Choices in Balanced Designs | https://arxiv.org/html/2607.16259v1#A2 — Appendix B Additional Results; https://arxiv.org/html/2607.16259v1#S3.SS1 — 3.1 Benchmark-Level Variability | https://arxiv.org/html/2607.16259v1#S5 — 5 Conclusions | Exact v1 links https://github.com/BityaNeuhof/quantifying-rank-uncertainty.git, https://huggingface.co/datasets/PromptEval/PromptEval_MMLU_correctness, https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16259 | complete |
| SF-2026-ARXIV-2607-16266 | RP-6126ba7974dd1261 | standard | arXiv:2607.16266v1 | SRC-ARXIV@arXiv:2607.16266v1 | https://arxiv.org/html/2607.16266v1#S3 — 3 Model | https://arxiv.org/html/2607.16266v1#S1 — 1 Introduction; https://arxiv.org/html/2607.16266v1#S2 — 2 Preliminaries | https://arxiv.org/html/2607.16266v1#S1 — 1 Introduction; https://arxiv.org/html/2607.16266v1#S2 — 2 Preliminaries | Exact v1 links https://github.com/julianmendez/verification-pipeline, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16266 | complete |
| SF-2026-ARXIV-2607-16269 | RP-afc6dad0d1780b1f | standard | arXiv:2607.16269v1 | SRC-ARXIV@arXiv:2607.16269v1 | https://arxiv.org/html/2607.16269v1#S2.SS1 — II-A The Complexity of ISAC System Design; https://arxiv.org/html/2607.16269v1#S2 — II Why ISAC Needs a New Design Abstraction | https://arxiv.org/html/2607.16269v1#S4.SS2 — IV-B Runtime Adaptation and Numerical Results; https://arxiv.org/html/2607.16269v1#S4 — IV Case Study | https://arxiv.org/html/2607.16269v1#S2.SS2 — II-B Limitations of Existing Approaches; https://arxiv.org/html/2607.16269v1#S6 — VI Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16269 | complete |
| SF-2026-ARXIV-2607-16311 | RP-31b38f6c92e32460 | standard | arXiv:2607.16311v1 | SRC-ARXIV@arXiv:2607.16311v1 | https://arxiv.org/html/2607.16311v1#A6.SS0.SSS0.Px3 — Model-level summary.; https://arxiv.org/html/2607.16311v1#A7.SS0.SSS0.Px1 — Model-level common tool deltas. | https://arxiv.org/html/2607.16311v1#S6 — 6 Experiments and Analysis; https://arxiv.org/html/2607.16311v1#A4 — Appendix D Evaluation Configuration | https://arxiv.org/html/2607.16311v1#S7 — 7 Conclusion; https://arxiv.org/html/2607.16311v1#S8 — 8 Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16311 | complete |
| SF-2026-ARXIV-2607-16314 | RP-464c900acac90c22 | standard | arXiv:2607.16314v1 | SRC-ARXIV@arXiv:2607.16314v1 | https://arxiv.org/html/2607.16314v1#S3 — 3 Method; https://arxiv.org/html/2607.16314v1#S2.SS1 — 2.1 Latent world models and JEPA-style prediction | https://arxiv.org/html/2607.16314v1#S3.SS3 — 3.3 Data and evaluation setting; https://arxiv.org/html/2607.16314v1#S3.SS4 — 3.4 Surprise evaluation protocol | https://arxiv.org/html/2607.16314v1#S5 — 5 Discussion; https://arxiv.org/html/2607.16314v1#S6 — 6 Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16314 | complete |
| SF-2026-ARXIV-2607-16326 | RP-f0fa51c58f43882b | standard | arXiv:2607.16326v1 | SRC-ARXIV@arXiv:2607.16326v1 | https://arxiv.org/html/2607.16326v1#S3 — III Method; https://arxiv.org/html/2607.16326v1#S2.SS1 — II-A Large Vision-Language Models | https://arxiv.org/html/2607.16326v1#S4 — IV Experiments; https://arxiv.org/html/2607.16326v1#S4.SS1 — IV-A Experimental Settings | https://arxiv.org/html/2607.16326v1#S5 — V Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16326 | complete |
| SF-2026-ARXIV-2607-16339 | RP-fb235abd471092c0 | deep | arXiv:2607.16339v1 | SRC-ARXIV@arXiv:2607.16339v1 | https://arxiv.org/html/2607.16339v1#S3 — 3 Method | https://arxiv.org/html/2607.16339v1#A4 — Appendix D The acceleration of LaCache on LLaDA-base on multiple benchmarks; https://arxiv.org/html/2607.16339v1#A5 — Appendix E The acceleration of LaCache on LLaDA-1.5 on multiple benchmarks | https://arxiv.org/html/2607.16339v1#S5 — 5 Conclusion; https://arxiv.org/html/2607.16339v1#Sx1 — Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16339 | complete |
| SF-2026-ARXIV-2607-16345 | RP-9480a22952abd276 | standard | arXiv:2607.16345v1 | SRC-ARXIV@arXiv:2607.16345v1 | https://arxiv.org/html/2607.16345v1#S4 — 4 Method; https://arxiv.org/html/2607.16345v1#S6 — 6 System and Deployment | https://arxiv.org/html/2607.16345v1#S4.SS1 — 4.1 Skill-Defined Evaluation Contract; https://arxiv.org/html/2607.16345v1#S4.SS4 — 4.4 Independent Analysis Pass | https://arxiv.org/html/2607.16345v1#S8 — 8 Discussion; https://arxiv.org/html/2607.16345v1#S9 — 9 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16345 | complete |
| SF-2026-ARXIV-2607-16352 | RP-39227033927330f2 | standard | arXiv:2607.16352v1 | SRC-ARXIV@arXiv:2607.16352v1 | https://arxiv.org/html/2607.16352v1#A1 — Appendix A Method Details; https://arxiv.org/html/2607.16352v1#A1.SS1 — A.1. Architecture | https://arxiv.org/html/2607.16352v1#A3 — Appendix C Extended Experimental Results; https://arxiv.org/html/2607.16352v1#A2 — Appendix B 3D Clarify Benchmark Details | https://arxiv.org/html/2607.16352v1#A3.SS3 — C.3. Statistical Analysis of Failure Modes; https://arxiv.org/html/2607.16352v1#A3.SS4 — C.4. Failure Case Analysis | Exact v1 links https://github.com/xyzhu1225/CLARE, https://github.com/ZiYang-xie/WorldGen, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16352 | complete |
| SF-2026-ARXIV-2607-16401 | RP-5523b2ea2621bbd6 | standard | arXiv:2607.16401v1 | SRC-ARXIV@arXiv:2607.16401v1 | https://arxiv.org/html/2607.16401v1#A1 — Appendix A Orchard Design Principles and Data Card; https://arxiv.org/html/2607.16401v1#A1.SS1 — A.1 Design Principles | https://arxiv.org/html/2607.16401v1#A3 — Appendix C Benchmark Protocol and Prompt Templates; https://arxiv.org/html/2607.16401v1#A3.SS3 — C.3 Protocol Ablations | https://arxiv.org/html/2607.16401v1#A8 — Appendix H Limitations; https://arxiv.org/html/2607.16401v1#S4.SS5 — 4.5 Qualitative Failure Analysis | Exact v1 links https://github.com/isaac-sim/IsaacSim, https://github.com/OpenSenseNova/SenseNova-U1, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16401 | complete |
| SF-2026-ARXIV-2607-16414 | RP-b00ea0ebf71caeb4 | standard | arXiv:2607.16414v1 | SRC-ARXIV@arXiv:2607.16414v1 | https://arxiv.org/html/2607.16414v1#S2.SS2 — 2.2 Metadata: Coarse System Knowledge and Low-Resource Observation; https://arxiv.org/html/2607.16414v1#S2 — 2 Signal-Based Model Access Risk Taxonomy | https://arxiv.org/html/2607.16414v1#S3 — 3 Risk Landscape Analysis and Procurement Decision Considerations | https://arxiv.org/html/2607.16414v1#S1 — 1 Introduction; https://arxiv.org/html/2607.16414v1#S2 — 2 Signal-Based Model Access Risk Taxonomy | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16414 | complete |
| SF-2026-ARXIV-2607-16442 | RP-0c82b02764623545 | standard | arXiv:2607.16442v1 | SRC-ARXIV@arXiv:2607.16442v1 | https://arxiv.org/html/2607.16442v1#S5.SS2 — 5.2. Experiment Design; https://arxiv.org/html/2607.16442v1#S3 — 3. Threat Model | https://arxiv.org/html/2607.16442v1#A3 — Appendix C Exp 2 Ablation: LoRA Magnitude Analysis; https://arxiv.org/html/2607.16442v1#A5 — Appendix E Full Experimental Results | https://arxiv.org/html/2607.16442v1#A4 — Appendix D Target-String Failure Examples; https://arxiv.org/html/2607.16442v1#S3 — 3. Threat Model | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16442 | complete |
| SF-2026-ARXIV-2607-16451 | RP-eb95f92ceda01739 | standard | arXiv:2607.16451v1 | SRC-ARXIV@arXiv:2607.16451v1 | https://arxiv.org/html/2607.16451v1#S1 — 1 Introduction; https://arxiv.org/html/2607.16451v1#S2 — 2 Behavioral study | https://arxiv.org/html/2607.16451v1#S2.SS2 — 2.2 Results: the wrong commitment is near-deterministic; https://arxiv.org/html/2607.16451v1#S2 — 2 Behavioral study | https://arxiv.org/html/2607.16451v1#S2.SS3 — 2.3 A truncation artifact that almost reversed a conclusion; https://arxiv.org/html/2607.16451v1#S5 — 5 Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16451 | complete |
| SF-2026-ARXIV-2607-16473 | RP-0f79c1178bef4af3 | deep | arXiv:2607.16473v1 | SRC-ARXIV@arXiv:2607.16473v1 | https://arxiv.org/html/2607.16473v1#S2.SS1 — 2.1. NPU Architecture; https://arxiv.org/html/2607.16473v1#S3 — 3. Design and Implementation | https://arxiv.org/html/2607.16473v1#S4 — 4. Evaluation; https://arxiv.org/html/2607.16473v1#S4.SS1 — 4.1. Experimental Setup | https://arxiv.org/html/2607.16473v1#S5 — 5. Discussion; https://arxiv.org/html/2607.16473v1#S7 — 7. Conclusion | Exact v1 links https://github.com/google-coral/coralnpu, https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro, https://huggingface.co/Qwen/Qwen3-Next-80B-A3B-Thinking; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16473 | complete |
| SF-2026-ARXIV-2607-16488 | RP-bd5cce9803ab6cef | deep | arXiv:2607.16488v1 | SRC-ARXIV@arXiv:2607.16488v1 | https://arxiv.org/html/2607.16488v1#S2.SS2 — 2.2. System Architecture of NPUs; https://arxiv.org/html/2607.16488v1#S3 — 3. Design and Implementation | https://arxiv.org/html/2607.16488v1#S5 — 5. Evaluation; https://arxiv.org/html/2607.16488v1#S5.SS1 — 5.1. Experimental Setup | https://arxiv.org/html/2607.16488v1#S6 — 6. Discussion; https://arxiv.org/html/2607.16488v1#S8 — 8. Conclusion | Exact v1 links https://github.com/features/copilot, https://github.com/AI-Hypercomputer/JetStream, https://github.com/Azure/AzurePublicDataset/blob/master/AzureLLMInferenceDataset2023.md; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16488 | complete |
| SF-2026-ARXIV-2607-16506 | RP-f0599c8f53f4c5c3 | standard | arXiv:2607.16506v1 | SRC-ARXIV@arXiv:2607.16506v1 | https://arxiv.org/html/2607.16506v1#S1 — I Introduction; https://arxiv.org/html/2607.16506v1#S2 — II Related Work | https://arxiv.org/html/2607.16506v1#S6 — VI Experiments; https://arxiv.org/html/2607.16506v1#S7 — VII Results | https://arxiv.org/html/2607.16506v1#S8 — VIII Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16506 | complete |
| SF-2026-ARXIV-2607-16523 | RP-c55ec7d137d2feaf | standard | arXiv:2607.16523v1 | SRC-ARXIV@arXiv:2607.16523v1 | https://arxiv.org/html/2607.16523v1#S3 — 3 Design Process; https://arxiv.org/html/2607.16523v1#S2.SS2 — 2.2 Algorithm Selection and Propagation | https://arxiv.org/html/2607.16523v1#S4 — 4 Experiments; https://arxiv.org/html/2607.16523v1#S4.SS2 — 4.2 Evaluation | https://arxiv.org/html/2607.16523v1#S5 — 5 Conclusion and Future Work | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16523 | complete |
| SF-2026-ARXIV-2607-16555 | RP-673a2107e5f27b5a | deep | arXiv:2607.16555v1 | SRC-ARXIV@arXiv:2607.16555v1 | https://arxiv.org/html/2607.16555v1#S3 — 3 Method; https://arxiv.org/html/2607.16555v1#S4.SS3 — 4.3 Models | https://arxiv.org/html/2607.16555v1#S4 — 4 Experimental Setup; https://arxiv.org/html/2607.16555v1#S4.SS4 — 4.4 Evaluation metrics | https://arxiv.org/html/2607.16555v1#S5 — 5 Results and Discussion; https://arxiv.org/html/2607.16555v1#S5.SS7 — 5.7 Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16555 | complete |
| SF-2026-ARXIV-2607-16560 | RP-34ddfaa0ccf3d903 | standard | arXiv:2607.16560v1 | SRC-ARXIV@arXiv:2607.16560v1 | https://arxiv.org/html/2607.16560v1#S2 — 2 From Observations to Propositions: A Compositional Framework | https://arxiv.org/html/2607.16560v1#S3 — 3 Experiments | https://arxiv.org/html/2607.16560v1#S4 — 4 Conclusion | Exact v1 links https://huggingface.co/datasets/nvidia/PhysicalAI-Autonomous-Vehicles, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16560 | complete |
| SF-2026-ARXIV-2607-16596 | RP-8ba11189f51a8a72 | deep | arXiv:2607.16596v1 | SRC-ARXIV@arXiv:2607.16596v1 | https://arxiv.org/html/2607.16596v1#S3.SS1 — III-A Design space; https://arxiv.org/html/2607.16596v1#S4.SS2 — IV-B Design | https://arxiv.org/html/2607.16596v1#S5 — V Evaluation | https://arxiv.org/html/2607.16596v1#S4.SS1 — IV-A Threat model; https://arxiv.org/html/2607.16596v1#S6 — VI Discussion and Lessons | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16596 | complete |
| SF-2026-ARXIV-2607-16602 | RP-24825ab903b2f9e4 | deep | arXiv:2607.16602v1 | SRC-ARXIV@arXiv:2607.16602v1 | https://arxiv.org/html/2607.16602v1#S3 — 3 Method; https://arxiv.org/html/2607.16602v1#S3.SS1 — 3.1 World Model Architecture and Training | https://arxiv.org/html/2607.16602v1#A1.SS4 — A.4 Ablation Study of VJEPA Reward; https://arxiv.org/html/2607.16602v1#S4 — 4 Experiments | https://arxiv.org/html/2607.16602v1#S5 — 5 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16602 | complete |
| SF-2026-ARXIV-2607-16612 | RP-9aa9933cdaf47466 | standard | arXiv:2607.16612v1 | SRC-ARXIV@arXiv:2607.16612v1 | https://arxiv.org/html/2607.16612v1#A5.SS3 — E.3 Tabular Model Architecture; https://arxiv.org/html/2607.16612v1#A6.SS2 — F.2 Image Model Architecture | https://arxiv.org/html/2607.16612v1#A4 — Appendix D General Experimental Protocol; https://arxiv.org/html/2607.16612v1#A5.SS2 — E.2 Tabular Experimental Protocol | https://arxiv.org/html/2607.16612v1#S5 — 5 Discussion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16612 | complete |
| SF-2026-ARXIV-2607-16617 | RP-0e2bc3abf62aa7ed | deep | arXiv:2607.16617v1 | SRC-ARXIV@arXiv:2607.16617v1 | https://arxiv.org/html/2607.16617v1#S3 — 3 System Architecture; https://arxiv.org/html/2607.16617v1#S4.SS3 — 4.3 Efficiency and System Cost ( RQ2 ) | https://arxiv.org/html/2607.16617v1#S4 — 4 Experiments; https://arxiv.org/html/2607.16617v1#S4.SS1 — 4.1 Experimental Setup | https://arxiv.org/html/2607.16617v1#S5 — 5 Conclusion | Exact v1 links https://github.com/OpenDCAI/DataFlow-WebUI, https://docs.anthropic.com/claude/docs/claude-code, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16617 | complete |
| SF-2026-ARXIV-2607-16621 | RP-595472b16affa8e4 | standard | arXiv:2607.16621v1 | SRC-ARXIV@arXiv:2607.16621v1 | https://arxiv.org/html/2607.16621v1#S4 — 4 Method; https://arxiv.org/html/2607.16621v1#S8 — 8 Implementation Details of MSCE | https://arxiv.org/html/2607.16621v1#S10 — 10 Experimental Details; https://arxiv.org/html/2607.16621v1#S10.SS1 — 10.1 Experimental Settings | https://arxiv.org/html/2607.16621v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.16621v1#Sx1 — Limitations | Exact v1 links https://github.com/MemTensor/MemOS, https://github.com/HKUDS/OpenSpace, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16621 | complete |
| SF-2026-ARXIV-2607-16632 | RP-64149f62184e2e88 | standard | arXiv:2607.16632v1 | SRC-ARXIV@arXiv:2607.16632v1 | https://arxiv.org/html/2607.16632v1#S3 — 3 Benchmark Design; https://arxiv.org/html/2607.16632v1#S3.SSx1 — Design Principles | https://arxiv.org/html/2607.16632v1#S3 — 3 Benchmark Design; https://arxiv.org/html/2607.16632v1#S3.SSx5 — Hidden Evaluation and Anti-Gaming | https://arxiv.org/html/2607.16632v1#S6 — 6 Discussion and Limitations; https://arxiv.org/html/2607.16632v1#S7 — 7 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16632 | complete |
| SF-2026-ARXIV-2607-16636 | RP-10d65fae8b48fc93 | deep | arXiv:2607.16636v1 | SRC-ARXIV@arXiv:2607.16636v1 | https://arxiv.org/html/2607.16636v1#S3 — 3 System Design; https://arxiv.org/html/2607.16636v1#S2.SS3 — 2.3 Agentic Systems | https://arxiv.org/html/2607.16636v1#S4.SS4 — 4.4 Benchmarking as an Instrument for Self-Evolution; https://arxiv.org/html/2607.16636v1#S5 — 5 Experiments | https://arxiv.org/html/2607.16636v1#S6 — 6 Conclusion and Future Work; https://arxiv.org/html/2607.16636v1#S6.SS2 — 6.2 Limitations | Exact v1 links https://github.com/PhyAgentOS/PhyAgentOS, https://huggingface.co/WorldAgents-c/world_dreamer-robocasa365-multi_task, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16636 | complete |
| SF-2026-ARXIV-2607-16643 | RP-d7bc596f9969722c | standard | arXiv:2607.16643v1 | SRC-ARXIV@arXiv:2607.16643v1 | https://arxiv.org/html/2607.16643v1#A1.SS2 — A.2 Baseline Methods; https://arxiv.org/html/2607.16643v1#S4 — 4 Methodology | https://arxiv.org/html/2607.16643v1#S6 — 6 Results and Analysis; https://arxiv.org/html/2607.16643v1#A1 — Appendix A Experimental Details | https://arxiv.org/html/2607.16643v1#S7 — 7 Conclusion; https://arxiv.org/html/2607.16643v1#Sx1 — Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16643 | complete |
| SF-2026-ARXIV-2607-16646 | RP-c62b0a91aedf72dd | standard | arXiv:2607.16646v1 | SRC-ARXIV@arXiv:2607.16646v1 | https://arxiv.org/html/2607.16646v1#S11 — 11 Prompts and implementation details; https://arxiv.org/html/2607.16646v1#S2.SS1 — 2.1 LLMs for optimization modeling | https://arxiv.org/html/2607.16646v1#S10 — 10 Parse coverage, benchmark audit, and additional tables; https://arxiv.org/html/2607.16646v1#S2.SS4 — 2.4 Sensitivity analysis and comparative statics | https://arxiv.org/html/2607.16646v1#S7.SS6 — 7.6 Scope and limitations; https://arxiv.org/html/2607.16646v1#S8 — 8 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16646 | complete |
| SF-2026-ARXIV-2607-16648 | RP-08e683e040000c4b | standard | arXiv:2607.16648v1 | SRC-ARXIV@arXiv:2607.16648v1 | https://arxiv.org/html/2607.16648v1#S8 — 8 Evaluation Methodology; https://arxiv.org/html/2607.16648v1#S5 — 5 Recovery Algorithms | https://arxiv.org/html/2607.16648v1#S3.SS1 — 3.1 Probabilistic Analysis; https://arxiv.org/html/2607.16648v1#S6 — 6 Security Analysis | https://arxiv.org/html/2607.16648v1#S10 — 10 Conclusions and Future Research; https://arxiv.org/html/2607.16648v1#S9.SS5 — 9.5 Future Research | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16648 | complete |
| SF-2026-ARXIV-2607-16673 | RP-1fa97b36c33607e2 | deep | arXiv:2607.16673v1 | SRC-ARXIV@arXiv:2607.16673v1 | https://arxiv.org/html/2607.16673v1#S3 — 3. System Overview; https://arxiv.org/html/2607.16673v1#S2.SS2 — 2.2. Linear Attention and Stateful Sequence Models | https://arxiv.org/html/2607.16673v1#S8 — 8. Evaluation; https://arxiv.org/html/2607.16673v1#S8.SS1 — 8.1. Experimental Setup | https://arxiv.org/html/2607.16673v1#S9 — 9. Conclusion | Exact v1 links https://huggingface.co/m-a-p/1.3B-100B-GatedDeltaNet-pure, https://github.com/NVlabs/GatedDeltaNet, https://huggingface.co/Qwen/Qwen3-Next-80B-A3B-Instruct; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16673 | complete |
| SF-2026-ARXIV-2607-16704 | RP-0ce2870df136510a | standard | arXiv:2607.16704v1 | SRC-ARXIV@arXiv:2607.16704v1 | https://arxiv.org/html/2607.16704v1#S5 — 5 Scientific Feasibility Control Algorithm; https://arxiv.org/html/2607.16704v1#S5.SS5 — 5.5 Domain-Adaptive Implementation | https://arxiv.org/html/2607.16704v1#S6 — 6 Experiments and Main Results | https://arxiv.org/html/2607.16704v1#S7 — 7 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16704 | complete |
| SF-2026-ARXIV-2607-16708 | RP-e89c8536341cd2f5 | standard | arXiv:2607.16708v1 | SRC-ARXIV@arXiv:2607.16708v1 | https://arxiv.org/html/2607.16708v1#S3 — 3. Proposed Approach; https://arxiv.org/html/2607.16708v1#S5.SS2 — 5.2. Design Rationale | https://arxiv.org/html/2607.16708v1#S4.SS3 — 4.3. Evaluation Settings; https://arxiv.org/html/2607.16708v1#S2.SS4 — 2.4. Case Study | https://arxiv.org/html/2607.16708v1#S5 — 5. Discussion; https://arxiv.org/html/2607.16708v1#S5.SS5 — 5.5. Threats to Validity | Exact v1 links https://github.com/wrwei/RADIANT/tree/main/malcom.requirement/malcom.requirement.model/metamodel, https://github.com/wrwei/RADIANT/tree/main/malcom.bifrost/malcom.bifrost.model/metamodel, https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16708 | complete |
| SF-2026-ARXIV-2607-16710 | RP-e7b345d264aaf0e2 | standard | arXiv:2607.16710v1 | SRC-ARXIV@arXiv:2607.16710v1 | https://arxiv.org/html/2607.16710v1#S1 — 1. Introduction; https://arxiv.org/html/2607.16710v1#S2 — 2. Curation Plans and Disclosure Semantics | https://arxiv.org/html/2607.16710v1#S1 — 1. Introduction; https://arxiv.org/html/2607.16710v1#S2 — 2. Curation Plans and Disclosure Semantics | https://arxiv.org/html/2607.16710v1#S1 — 1. Introduction; https://arxiv.org/html/2607.16710v1#S2 — 2. Curation Plans and Disclosure Semantics | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16710 | complete |
| SF-2026-ARXIV-2607-16716 | RP-05b7c7e3b8a7dbf8 | standard | arXiv:2607.16716v1 | SRC-ARXIV@arXiv:2607.16716v1 | https://arxiv.org/html/2607.16716v1#S1 — 1 Introduction; https://arxiv.org/html/2607.16716v1#S2 — 2 Related Work | https://arxiv.org/html/2607.16716v1#S4 — 4 Evaluation and Results; https://arxiv.org/html/2607.16716v1#A3 — Appendix C Extended Human Validation Analysis | https://arxiv.org/html/2607.16716v1#S5 — 5 Conclusion; https://arxiv.org/html/2607.16716v1#S6 — 6 Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16716 | complete |
| SF-2026-ARXIV-2607-16721 | RP-49aef6e98d937a32 | standard | arXiv:2607.16721v1 | SRC-ARXIV@arXiv:2607.16721v1 | https://arxiv.org/html/2607.16721v1#S3 — 3 Method | https://arxiv.org/html/2607.16721v1#S4 — 4 Experimental Setup; https://arxiv.org/html/2607.16721v1#S5 — 5 Results | https://arxiv.org/html/2607.16721v1#S6 — 6 Limitations and Future Work; https://arxiv.org/html/2607.16721v1#S7 — 7 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16721 | complete |
| SF-2026-ARXIV-2607-16726 | RP-f24771748f2f3982 | standard | arXiv:2607.16726v1 | SRC-ARXIV@arXiv:2607.16726v1 | https://arxiv.org/html/2607.16726v1#S2 — 2 Methodology | https://arxiv.org/html/2607.16726v1#S3 — 3 Experiments and Results; https://arxiv.org/html/2607.16726v1#S3.SS1 — 3.1 Experimental Settings | https://arxiv.org/html/2607.16726v1#S4 — 4 Conclusion | Exact v1 links https://github.com/BioMedIA-MBZUAI/MoBE-A-Test-Time-Modality-Generalization-Method, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16726 | complete |
| SF-2026-ARXIV-2607-16740 | RP-f7efd2f99e1c3b2c | standard | arXiv:2607.16740v1 | SRC-ARXIV@arXiv:2607.16740v1 | https://arxiv.org/html/2607.16740v1#S3.SS2 — 3.2. Experimental Design | https://arxiv.org/html/2607.16740v1#S4 — 4. Experimental Results; https://arxiv.org/html/2607.16740v1#S3.SS2 — 3.2. Experimental Design | https://arxiv.org/html/2607.16740v1#S5 — 5. Implications and Conclusion; https://arxiv.org/html/2607.16740v1#S5.SS2 — 5.2. Threats to Validity | Exact v1 links https://github.com/harbor-framework/harbor, https://aclanthology.org/2025.emnlp-demos.15/, https://dx.doi.org/10.18653/v1/2025.emnlp-demos.15; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16740 | complete |
| SF-2026-ARXIV-2607-16745 | RP-0348fbf4fb3711d8 | standard | arXiv:2607.16745v1 | SRC-ARXIV@arXiv:2607.16745v1 | https://arxiv.org/html/2607.16745v1#A1.SS1 — A.1 LLMs for Automated Heuristic Design; https://arxiv.org/html/2607.16745v1#S3 — 3 Methodology | https://arxiv.org/html/2607.16745v1#A3 — Appendix C Experimental Settings; https://arxiv.org/html/2607.16745v1#S4 — 4 Experiments | https://arxiv.org/html/2607.16745v1#S1 — 1 Introduction; https://arxiv.org/html/2607.16745v1#S2 — 2 Preliminary | Exact v1 links https://aclanthology.org/2024.emnlp-demo.25/, https://dx.doi.org/10.18653/v1/2024.emnlp-demo.25, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16745 | complete |
| SF-2026-ARXIV-2607-16784 | RP-c9996d3473a5a420 | deep | arXiv:2607.16784v1 | SRC-ARXIV@arXiv:2607.16784v1 | https://arxiv.org/html/2607.16784v1#S4 — 4. Roomie : System Design; https://arxiv.org/html/2607.16784v1#S2.SS3 — 2.3. Challenges in Modeling Kernel-Level Interference | https://arxiv.org/html/2607.16784v1#S5 — 5. Experimental Setup; https://arxiv.org/html/2607.16784v1#S6 — 6. Evaluation | https://arxiv.org/html/2607.16784v1#S8 — 8. Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16784 | complete |
| SF-2026-ARXIV-2607-16789 | RP-33eadcf5d1fe1a5c | standard | arXiv:2607.16789v1 | SRC-ARXIV@arXiv:2607.16789v1 | https://arxiv.org/html/2607.16789v1#S1 — 1 Introduction; https://arxiv.org/html/2607.16789v1#S2 — 2 Related work | https://arxiv.org/html/2607.16789v1#A1.SS2 — A.2 Ablation study; https://arxiv.org/html/2607.16789v1#S4 — 4 Experiments | https://arxiv.org/html/2607.16789v1#S6 — 6 Discussion | Exact v1 links https://github.com/sanatonek/MultiLoReFT, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16789 | complete |
| SF-2026-ARXIV-2607-16800 | RP-cbb6b6b270ac079e | standard | arXiv:2607.16800v1 | SRC-ARXIV@arXiv:2607.16800v1 | https://arxiv.org/html/2607.16800v1#S3.SS3 — 3.3 Effective single-entangler circuit (IP-PDT architecture); https://arxiv.org/html/2607.16800v1#S4.SS1 — 4.1 Continuation-theoretic framework | https://arxiv.org/html/2607.16800v1#S4 — 4 Theoretical Analysis; https://arxiv.org/html/2607.16800v1#S5 — 5 Experiments | https://arxiv.org/html/2607.16800v1#A2 — Appendix B Extended Theoretical Discussion; https://arxiv.org/html/2607.16800v1#A2.SS1 — B.1 Identity-embedding property: extended discussion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16800 | complete |
| SF-2026-ARXIV-2607-16836 | RP-96484cf33b518f11 | deep | arXiv:2607.16836v1 | SRC-ARXIV@arXiv:2607.16836v1 | https://arxiv.org/html/2607.16836v1#S5.SS1 — 5.1. A Design Space for Stateful Runtime Architectures; https://arxiv.org/html/2607.16836v1#A1.SS2 — A.2. Replicated, Transactional, and Memory-Resident Systems as Boundary References | https://arxiv.org/html/2607.16836v1#S6 — 6. Evaluation and Research Outlook; https://arxiv.org/html/2607.16836v1#S6.SS1 — 6.1. Evaluation Dimensions for Future Surveys and Systems | https://arxiv.org/html/2607.16836v1#S5.SS2 — 5.2. Failure Modes and Anti-Patterns; https://arxiv.org/html/2607.16836v1#S6.SS1 — 6.1. Evaluation Dimensions for Future Surveys and Systems | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16836 | complete |
| SF-2026-ARXIV-2607-16848 | RP-28b6752dcb4b175a | standard | arXiv:2607.16848v1 | SRC-ARXIV@arXiv:2607.16848v1 | https://arxiv.org/html/2607.16848v1#S2.SS2 — 2.2 Three foundational systems; https://arxiv.org/html/2607.16848v1#S2.SS5 — 2.5 Open-source frameworks | https://arxiv.org/html/2607.16848v1#S6 — 6 Experimental evaluation; https://arxiv.org/html/2607.16848v1#S2.SS7 — 2.7 Memory and scientific-QA benchmarks | https://arxiv.org/html/2607.16848v1#S8 — 8 Discussion and limitations; https://arxiv.org/html/2607.16848v1#A1.SSx1 — PQ4 – saturation with integration failures | Exact v1 links https://huggingface.co/datasets/quantellence/srb-data, https://github.com/crewAIInc/crewAI, https://code.claude.com/docs/en/memory; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16848 | complete |
| SF-2026-ARXIV-2607-16851 | RP-ef9149d7c1149650 | standard | arXiv:2607.16851v1 | SRC-ARXIV@arXiv:2607.16851v1 | https://arxiv.org/html/2607.16851v1#S2 — 2 The AgentBrew Framework; https://arxiv.org/html/2607.16851v1#S2.SS2 — 2.2 Framework Overview | https://arxiv.org/html/2607.16851v1#A1.SS2 — A.2 Detailed Setting of Benchmarks; https://arxiv.org/html/2607.16851v1#S3 — 3 Evaluation | https://arxiv.org/html/2607.16851v1#S5 — 5 Conclusion | Exact v1 links https://github.com/HKUDS/UpSkill, https://docs.anthropic.com/en/docs/claude-code, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16851 | complete |
| SF-2026-ARXIV-2607-16868 | RP-9a1ccb4dc29d9544 | standard | arXiv:2607.16868v1 | SRC-ARXIV@arXiv:2607.16868v1 | https://arxiv.org/html/2607.16868v1#S1.SS2 — 1.2 Our Logical Graph-Based Uncertainty Framework; https://arxiv.org/html/2607.16868v1#A1 — Appendix A Algorithms of Logical Graph Uncertainty | https://arxiv.org/html/2607.16868v1#A2 — Appendix B Experiment Details and Ablations; https://arxiv.org/html/2607.16868v1#A2.SS4 — B.4 Additional Experiments and Analysis | https://arxiv.org/html/2607.16868v1#S5 — 5 Discussion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16868 | complete |
| SF-2026-ARXIV-2607-16872 | RP-d56b38a4c7c420bf | standard | arXiv:2607.16872v1 | SRC-ARXIV@arXiv:2607.16872v1 | https://arxiv.org/html/2607.16872v1#A1 — Appendix A Additional Method Details; https://arxiv.org/html/2607.16872v1#S3 — 3 Method | https://arxiv.org/html/2607.16872v1#A3 — Appendix C Experimental Details; https://arxiv.org/html/2607.16872v1#A3.SS5 — C.5 Evaluation Protocol | https://arxiv.org/html/2607.16872v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.16872v1#Sx1 — Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16872 | complete |
| SF-2026-ARXIV-2607-16892 | RP-c62683f5ebd2beba | deep | arXiv:2607.16892v1 | SRC-ARXIV@arXiv:2607.16892v1 | https://arxiv.org/html/2607.16892v1#S3 — III System Model and Problem Formulation; https://arxiv.org/html/2607.16892v1#S3.SS1 — III-A System Overview | https://arxiv.org/html/2607.16892v1#S5.SS5 — V-E Ablation Analysis; https://arxiv.org/html/2607.16892v1#S5 — V Performance Evaluation | https://arxiv.org/html/2607.16892v1#S6 — VI Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16892 | complete |
| SF-2026-ARXIV-2607-16900 | RP-1a8d4f3491b1065a | standard | arXiv:2607.16900v1 | SRC-ARXIV@arXiv:2607.16900v1 | https://arxiv.org/html/2607.16900v1#A11.SS2 — K.2 API Schema Design; https://arxiv.org/html/2607.16900v1#S3 — 3 Method | https://arxiv.org/html/2607.16900v1#A6 — Appendix F Full Experimental Results; https://arxiv.org/html/2607.16900v1#S4.SS1 — 4.1 Results on AppWorld Benchmark | https://arxiv.org/html/2607.16900v1#A1.SS2 — A.2 Failure Analysis; https://arxiv.org/html/2607.16900v1#A2.SS2 — B.2 Failure Analysis | Exact v1 links https://doi.org/10.18653/v1/2020.emnlp-demos.6, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16900 | complete |
| SF-2026-ARXIV-2607-16973 | RP-1c6797d3a346edb4 | standard | arXiv:2607.16973v1 | SRC-ARXIV@arXiv:2607.16973v1 | https://arxiv.org/html/2607.16973v1#S3 — III System Design; https://arxiv.org/html/2607.16973v1#S2.SS2 — II-B TurboQuant Algorithm | https://arxiv.org/html/2607.16973v1#S4.SS2 — IV-B Results; https://arxiv.org/html/2607.16973v1#S4.SS3 — IV-C Analysis | https://arxiv.org/html/2607.16973v1#S8 — VIII Limitations and Future Work; https://arxiv.org/html/2607.16973v1#S2.SS5 — II-E Threat Model | Exact v1 links https://huggingface.co/datasets/Qdrant/dbpedia-entities-openai3-text-embedding-3-large-1536-1M, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16973 | complete |
| SF-2026-ARXIV-2607-16999 | RP-a1ca76fff72bc9b1 | standard | arXiv:2607.16999v1 | SRC-ARXIV@arXiv:2607.16999v1 | https://arxiv.org/html/2607.16999v1#A4.SS5 — D.5 PTR Buffer Design (Section B ); https://arxiv.org/html/2607.16999v1#A7 — Appendix G Credit Assignment Methods: Detailed Comparison | https://arxiv.org/html/2607.16999v1#A5 — Appendix E Additional Experiments; https://arxiv.org/html/2607.16999v1#S5 — 5 Experiments | https://arxiv.org/html/2607.16999v1#A6 — Appendix F Limitations and Future Work; https://arxiv.org/html/2607.16999v1#S6 — 6 Conclusion | Exact v1 links https://github.com/Farama-Foundation/Minigrid, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16999 | complete |
| SF-2026-ARXIV-2607-17019 | RP-ddc3d5ea08a37a20 | standard | arXiv:2607.17019v1 | SRC-ARXIV@arXiv:2607.17019v1 | https://arxiv.org/html/2607.17019v1#S3 — 3 Method | https://arxiv.org/html/2607.17019v1#S4 — 4 Experimental Setup; https://arxiv.org/html/2607.17019v1#S5 — 5 Results | https://arxiv.org/html/2607.17019v1#S7 — 7 Limitations; https://arxiv.org/html/2607.17019v1#S8 — 8 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-17019 | complete |
| SF-2026-ARXIV-2607-17175 | RP-0037b57dd85f2479 | deep | arXiv:2607.17175v1 | SRC-ARXIV@arXiv:2607.17175v1 | https://arxiv.org/html/2607.17175v1#S4 — 4 LMEdge System Architecture; https://arxiv.org/html/2607.17175v1#S5 — 5 LMEdge Heuristic Algorithm | https://arxiv.org/html/2607.17175v1#S7 — 7 Evaluation Results; https://arxiv.org/html/2607.17175v1#S6 — 6 Evaluation Setup | https://arxiv.org/html/2607.17175v1#S8 — 8 Conclusion | Exact v1 links https://pypi.org/project/PuLP/, https://huggingface.co/nvidia/prompt-task-and-complexity-classifier, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-17175 | complete |
| SF-2026-ARXIV-2607-17181 | RP-1a07c2e107a17494 | deep | arXiv:2607.17181v1 | SRC-ARXIV@arXiv:2607.17181v1 | https://arxiv.org/html/2607.17181v1#S3 — 3 Design; https://arxiv.org/html/2607.17181v1#S3.SS1 — 3.1 System Overview | https://arxiv.org/html/2607.17181v1#S5 — 5 Evaluation | https://arxiv.org/html/2607.17181v1#S7 — 7 Conclusion | Exact v1 links https://huggingface.co/blog/huggingface/state-of-os-hf-spring-2026, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-17181 | complete |
| SF-2026-ARXIV-2607-17188 | RP-3f373ca4d1b303e0 | standard | arXiv:2607.17188v1 | SRC-ARXIV@arXiv:2607.17188v1 | https://arxiv.org/html/2607.17188v1#A1.SS2 — A.2. Generalization vs. Training-based Methods; https://arxiv.org/html/2607.17188v1#A1.SS3 — A.3. Reliability vs. Entropy-based Methods | https://arxiv.org/html/2607.17188v1#A1 — Appendix A Extended Experimental Main Results; https://arxiv.org/html/2607.17188v1#S6.SS3 — 6.3. Ablation and In-Depth Analysis | https://arxiv.org/html/2607.17188v1#S7 — 7. Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-17188 | complete |
| SF-2026-ARXIV-2607-17205 | RP-106346de469453f4 | standard | arXiv:2607.17205v1 | SRC-ARXIV@arXiv:2607.17205v1 | https://arxiv.org/pdf/2607.17205v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.17205v1#page=10 — PDF page 10 | https://arxiv.org/pdf/2607.17205v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.17205v1#page=10 — PDF page 10 | https://arxiv.org/pdf/2607.17205v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.17205v1#page=10 — PDF page 10 | Exact v1 links https://github.com/hanzunye/swe-trajectory-quality-study; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-17205 | complete |
| SF-2026-ARXIV-2607-17213 | RP-a2de84c72a3c22ce | standard | arXiv:2607.17213v1 | SRC-ARXIV@arXiv:2607.17213v1 | https://arxiv.org/html/2607.17213v1#A1 — Appendix A Historical Lineage: Programming Models and System Abstractions for Hardware and Robots; https://arxiv.org/html/2607.17213v1#A1.SS8 — A-H Modern Learning Frameworks | https://arxiv.org/html/2607.17213v1#A6 — Appendix F Experiment Details; https://arxiv.org/html/2607.17213v1#A6.SS1 — F-A Benchmark Implementation Footprint | https://arxiv.org/html/2607.17213v1#A1.SS9 — A-I Robotics Middleware: ROS Limitations; https://arxiv.org/html/2607.17213v1#S7 — VII Conclusion | Exact v1 links https://github.com/openretriever/retriever, https://github.com/dora-rs/dora, https://github.com/ApolloAuto/apollo/tree/master/cyber; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-17213 | complete |
| SF-2026-ARXIV-2607-17225 | RP-023dc39b1689ee88 | standard | arXiv:2607.17225v1 | SRC-ARXIV@arXiv:2607.17225v1 | https://arxiv.org/html/2607.17225v1#S1 — 1. Introduction; https://arxiv.org/html/2607.17225v1#S2 — 2. When to Use Agents: the AJR | https://arxiv.org/html/2607.17225v1#S1 — 1. Introduction; https://arxiv.org/html/2607.17225v1#S2 — 2. When to Use Agents: the AJR | https://arxiv.org/html/2607.17225v1#S5 — 5. Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-17225 | complete |
| SF-2026-ARXIV-2607-17247 | RP-ef3ae4fc5e40a5a6 | standard | arXiv:2607.17247v1 | SRC-ARXIV@arXiv:2607.17247v1 | https://arxiv.org/html/2607.17247v1#S3 — 3 Method; https://arxiv.org/html/2607.17247v1#A2 — Appendix B Implementation Details | https://arxiv.org/html/2607.17247v1#S3.SS1 — 3.1 Observation and Analysis; https://arxiv.org/html/2607.17247v1#S5 — 5 Experiments | https://arxiv.org/html/2607.17247v1#A1 — Appendix A Limitation; https://arxiv.org/html/2607.17247v1#S6 — 6 Conclusion | Exact v1 links https://github.com/597358816/Distilled-RL, https://github.com/hiyouga/EasyR1, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-17247 | complete |
| SF-2026-ARXIV-2607-17250 | RP-0bd776bd3d78bbf9 | standard | arXiv:2607.17250v1 | SRC-ARXIV@arXiv:2607.17250v1 | https://arxiv.org/html/2607.17250v1#A5 — Appendix E Evaluation Framework; https://arxiv.org/html/2607.17250v1#S3 — 3 The EvolvingWorld Framework | https://arxiv.org/html/2607.17250v1#A6 — Appendix F Full Results on EvolvingWorld Benchmark; https://arxiv.org/html/2607.17250v1#A11.SS3 — K.3 Evaluation Prompts | https://arxiv.org/html/2607.17250v1#S5 — 5 Conclusion; https://arxiv.org/html/2607.17250v1#Sx1 — Limitations | Exact v1 links https://github.com/HKUST-KnowComp/EvolvingWorld, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-17250 | complete |
| SF-2026-ARXIV-2607-17257 | RP-a53d455e6cab71ca | standard | arXiv:2607.17257v1 | SRC-ARXIV@arXiv:2607.17257v1 | https://arxiv.org/html/2607.17257v1#A1 — Appendix A Method Implementation Details; https://arxiv.org/html/2607.17257v1#S3 — 3 Method | https://arxiv.org/html/2607.17257v1#A2.SS2 — B.2 Additional Experiments Results; https://arxiv.org/html/2607.17257v1#A2 — Appendix B Experiment Details | https://arxiv.org/html/2607.17257v1#A2.SS3 — B.3 Failure Analysis; https://arxiv.org/html/2607.17257v1#S5 — 5 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-17257 | complete |
| SF-2026-ARXIV-2607-17269 | RP-2a13d15d8693531d | standard | arXiv:2607.17269v1 | SRC-ARXIV@arXiv:2607.17269v1 | https://arxiv.org/html/2607.17269v1#S3.SS2 — 3.2 System Architecture and Implementation; https://arxiv.org/html/2607.17269v1#S2.SS2 — 2.2 LLM-Augmentation and Agent Frameworks | https://arxiv.org/html/2607.17269v1#S4 — 4 Results and Analysis; https://arxiv.org/html/2607.17269v1#S4.SS2 — 4.2 Three-Tier Microbenchmarks and Ablation | https://arxiv.org/html/2607.17269v1#S5 — 5 Discussion; https://arxiv.org/html/2607.17269v1#S5.SS4 — 5.4 Limitations | Exact v1 links https://github.com/neo4j/neo4j/wiki/Neo4j-2025-changelog, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-17269 | complete |
| SF-2026-ARXIV-2607-17288 | RP-a697d0f19bc14c32 | standard | arXiv:2607.17288v1 | SRC-ARXIV@arXiv:2607.17288v1 | https://arxiv.org/html/2607.17288v1#S2 — 2. Model and Design Foundations; https://arxiv.org/html/2607.17288v1#S3 — 3. System Overview | https://arxiv.org/html/2607.17288v1#S5 — 5. Evaluation | https://arxiv.org/html/2607.17288v1#S6 — 6. Conclusion | Exact v1 links https://github.com/graphuofm/SAGA, https://github.com/IBM/AMLSim, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-17288 | complete |
| SF-2026-ARXIV-2607-17291 | RP-0384204de907c6b3 | standard | arXiv:2607.17291v1 | SRC-ARXIV@arXiv:2607.17291v1 | https://arxiv.org/html/2607.17291v1#S1 — 1 Introduction; https://arxiv.org/html/2607.17291v1#S2 — 2 Related Work | https://arxiv.org/html/2607.17291v1#A3 — Appendix C Evaluation Parameters; https://arxiv.org/html/2607.17291v1#A4 — Appendix D Intervention and Ablation Prompts | https://arxiv.org/html/2607.17291v1#S7 — 7 Limitations; https://arxiv.org/html/2607.17291v1#S8 — 8 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-17291 | complete |
| SF-2026-ARXIV-2607-17299 | RP-2735c6b69378fe60 | deep | arXiv:2607.17299v1 | SRC-ARXIV@arXiv:2607.17299v1 | https://arxiv.org/html/2607.17299v1#Sx3 — WAR System Design; https://arxiv.org/html/2607.17299v1#Sx6.SSx1 — RL Training Systems | https://arxiv.org/html/2607.17299v1#Sx5 — Evaluation; https://arxiv.org/html/2607.17299v1#Sx5.SSx1 — End-to-End Evaluation | https://arxiv.org/html/2607.17299v1#Sx7 — Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-17299 | complete |
| SF-2026-ARXIV-2607-17347 | RP-6679453450d69082 | standard | arXiv:2607.17347v1 | SRC-ARXIV@arXiv:2607.17347v1 | https://arxiv.org/html/2607.17347v1#S4 — 4. Supervision and Models | https://arxiv.org/html/2607.17347v1#S6 — 6. Experiments; https://arxiv.org/html/2607.17347v1#S6.SS1 — 6.1. In-domain adaptation on benchmark subsets | https://arxiv.org/html/2607.17347v1#S7 — 7. Discussion; https://arxiv.org/html/2607.17347v1#S8 — 8. Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-17347 | complete |
| SF-2026-ARXIV-2607-17352 | RP-bac13fc735ba14ba | standard | arXiv:2607.17352v1 | SRC-ARXIV@arXiv:2607.17352v1 | https://arxiv.org/html/2607.17352v1#S3 — 3 Method; https://arxiv.org/html/2607.17352v1#A2 — Appendix B Benchmark-update algorithm | https://arxiv.org/html/2607.17352v1#A1 — Appendix A Experimental details and hyperparameters; https://arxiv.org/html/2607.17352v1#A2 — Appendix B Benchmark-update algorithm | https://arxiv.org/html/2607.17352v1#S5 — 5 Discussion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-17352 | complete |
| SF-2026-ARXIV-2607-17384 | RP-90f6b8e10ac38f18 | standard | arXiv:2607.17384v1 | SRC-ARXIV@arXiv:2607.17384v1 | https://arxiv.org/html/2607.17384v1#S3 — 3. A Weighted Swap Law for Model Pairs; https://arxiv.org/html/2607.17384v1#S3.SS2 — 3.2. The Complete Lift Model | https://arxiv.org/html/2607.17384v1#S5 — 5. Datasets & Experimental Setup; https://arxiv.org/html/2607.17384v1#S9 — 9. Analysis & Limitations | https://arxiv.org/html/2607.17384v1#S10 — 10. Conclusion; https://arxiv.org/html/2607.17384v1#S9 — 9. Analysis & Limitations | Exact v1 links https://huggingface.co/datasets/Idavidrein/gpqa, https://huggingface.co/datasets/IcyApril/deciban, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-17384 | complete |
| SF-2026-ARXIV-2607-17389 | RP-69f1b4a2665b5988 | standard | arXiv:2607.17389v1 | SRC-ARXIV@arXiv:2607.17389v1 | https://arxiv.org/html/2607.17389v1#S4 — 4 Architecture of the Proposed Solution; https://arxiv.org/html/2607.17389v1#S10 — 10 Evaluation of the Model | https://arxiv.org/html/2607.17389v1#S10 — 10 Evaluation of the Model; https://arxiv.org/html/2607.17389v1#S7 — 7 Basic Dataset Analysis | https://arxiv.org/html/2607.17389v1#S12 — 12 Conclusion | Exact v1 links https://github.com/alexfru/SmallerC, https://github.com/DaveGamble/cJSON, https://github.com/json-c/json-c; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-17389 | complete |
| SF-2026-ARXIV-2607-17409 | RP-d8d334463d123371 | standard | arXiv:2607.17409v1 | SRC-ARXIV@arXiv:2607.17409v1 | https://arxiv.org/html/2607.17409v1#S4.SS1 — 4.1 RIPr-based approach; https://arxiv.org/html/2607.17409v1#S4.SS2 — 4.2 Testing-by-betting-based approach | https://arxiv.org/html/2607.17409v1#A1 — Appendix A Experiment details and supplemental results; https://arxiv.org/html/2607.17409v1#S5.SS2 — 5.2 Analysis of the shrinkage behavior of CSs | https://arxiv.org/html/2607.17409v1#S7 — 7 Conclusion | Exact v1 links https://projecteuclid.org/proceedings/berkeley-symposium-on-mathematical-statistics-and-probability/Proceedings-of-the-Fourth-Berkeley-Symposium-on-Mathematical-Statistics-and/Chapter/Optimal-Gambling-Systems-for-Favorable-Games/bsmsp/1200512159, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-17409 | complete |
| SF-2026-ARXIV-2607-17415 | RP-691c490a3315951d | deep | arXiv:2607.17415v1 | SRC-ARXIV@arXiv:2607.17415v1 | https://arxiv.org/html/2607.17415v1#S3 — III Methodology; https://arxiv.org/html/2607.17415v1#S3.SS1 — III-A Full-Model Inference Trace Collection | https://arxiv.org/html/2607.17415v1#S4 — IV Evaluation Results; https://arxiv.org/html/2607.17415v1#S3.SS3 — III-C Jetson Multi-Backend Benchmarking | https://arxiv.org/html/2607.17415v1#S5 — V Future Work; https://arxiv.org/html/2607.17415v1#S6 — VI Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-17415 | complete |
| SF-2026-ARXIV-2607-17419 | RP-c1bc08ad4e668fc9 | standard | arXiv:2607.17419v1 | SRC-ARXIV@arXiv:2607.17419v1 | https://arxiv.org/html/2607.17419v1#A6.SS4 — F.4 Per-method architectures and reproducibility; https://arxiv.org/html/2607.17419v1#A1.SS1 — A.1 Kernel methods | https://arxiv.org/html/2607.17419v1#A5 — Appendix E Hardware implementation and benchmarks; https://arxiv.org/html/2607.17419v1#A5.SS2 — E.2 Induction-head benchmark | https://arxiv.org/html/2607.17419v1#S7 — 7 Discussion and Limitations | Exact v1 links https://github.com/ayghri/kata, https://github.com/fla-org/flash-linear-attention, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-17419 | complete |
| SF-2026-ARXIV-2607-17422 | RP-a5770367147c549e | deep | arXiv:2607.17422v1 | SRC-ARXIV@arXiv:2607.17422v1 | https://arxiv.org/html/2607.17422v1#S4 — 4. DAN-Scheduler Design; https://arxiv.org/html/2607.17422v1#S5 — 5. Experimental Methodology | https://arxiv.org/html/2607.17422v1#S5 — 5. Experimental Methodology; https://arxiv.org/html/2607.17422v1#S6 — 6. Evaluation | https://arxiv.org/html/2607.17422v1#S8 — 8. Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-17422 | complete |
| SF-2026-ARXIV-2607-17425 | RP-1756cc823fb2578f | standard | arXiv:2607.17425v1 | SRC-ARXIV@arXiv:2607.17425v1 | https://arxiv.org/html/2607.17425v1#A1.SS10 — A.10 Optimization and architecture audits; https://arxiv.org/html/2607.17425v1#A1.SS2 — A.2 Language-model protocol and paired GPT-2 evaluation | https://arxiv.org/html/2607.17425v1#S5 — 5 Experiments and Results; https://arxiv.org/html/2607.17425v1#A1 — Appendix A Experimental Details | https://arxiv.org/html/2607.17425v1#S7 — 7 Discussion, Limitations, and Future Work | Exact v1 links https://github.com/aniket-desh/decoder-preserving-sae, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-17425 | complete |
| SF-2026-ARXIV-2607-17454 | RP-cd5de2f6b6b021b2 | standard | arXiv:2607.17454v1 | SRC-ARXIV@arXiv:2607.17454v1 | https://arxiv.org/html/2607.17454v1#S3 — 3 Method | https://arxiv.org/html/2607.17454v1#S4 — 4 Experiments; https://arxiv.org/html/2607.17454v1#S4.SS1 — 4.1 Experimental Setup | https://arxiv.org/html/2607.17454v1#S3.SS1 — 3.1 Action–Future Gate for Selective Sampling; https://arxiv.org/html/2607.17454v1#S4.SS5 — 4.5 Best-of- Failure Analysis | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-17454 | complete |
| SF-2026-ARXIV-2607-17525 | RP-1daaadf4e58fa5f2 | deep | arXiv:2607.17525v1 | SRC-ARXIV@arXiv:2607.17525v1 | https://arxiv.org/html/2607.17525v1#S2.SS1 — 2.1 Distributed-Systems Failure Taxonomies; https://arxiv.org/html/2607.17525v1#S3 — 3 Taxonomy Design | https://arxiv.org/html/2607.17525v1#S2.SS2 — 2.2 LLM Evaluation and Reliability | https://arxiv.org/html/2607.17525v1#S7 — 7 Discussion: Why Silent Failures Dominate; https://arxiv.org/html/2607.17525v1#A1 — Appendix A Full Failure Catalog | Exact v1 links https://github.com/BerriAI/litellm, https://github.com/Portkey-AI/gateway, https://github.com/Vishal-sys-code/failure-atlas; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-17525 | complete |
| SF-2026-ARXIV-2607-17528 | RP-d22d78fe04786124 | standard | arXiv:2607.17528v1 | SRC-ARXIV@arXiv:2607.17528v1 | https://arxiv.org/html/2607.17528v1#S1 — 1. Introduction; https://arxiv.org/html/2607.17528v1#S2 — 2. Related Work | https://arxiv.org/html/2607.17528v1#A1.SS2 — A.2. Result Score; https://arxiv.org/html/2607.17528v1#S3 — 3. Benchmark Construction | https://arxiv.org/html/2607.17528v1#S6 — 6. Conclusion | Exact v1 links https://docs.anthropic.com/en/docs/claude-code/overview, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-17528 | complete |
| SF-2026-ARXIV-2607-17535 | RP-2d810306ef47e49c | standard | arXiv:2607.17535v1 | SRC-ARXIV@arXiv:2607.17535v1 | https://arxiv.org/html/2607.17535v1#S4 — 4. Attack Design; https://arxiv.org/html/2607.17535v1#S5.SS1 — 5.1. Design Goals | https://arxiv.org/html/2607.17535v1#A3 — Appendix C Additional Evaluation Results; https://arxiv.org/html/2607.17535v1#A9 — Appendix I Benchmark Construction Details | https://arxiv.org/html/2607.17535v1#S10 — 10. Conclusion; https://arxiv.org/html/2607.17535v1#S2 — 2. Background and Threat Model | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-17535 | complete |
| SF-2026-ARXIV-2607-17545 | RP-1716b0dc9e88dc70 | standard | arXiv:2607.17545v1 | SRC-ARXIV@arXiv:2607.17545v1 | https://arxiv.org/html/2607.17545v1#Sx3 — Methodology | https://arxiv.org/html/2607.17545v1#A2 — Appendix B Reproducibility and Experimental Detail; https://arxiv.org/html/2607.17545v1#A2.SSx6 — Independently Split Full-History Four-Action Evaluation | https://arxiv.org/html/2607.17545v1#Sx5 — Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-17545 | complete |
| SF-2026-ARXIV-2607-17558 | RP-66de97a95a5fddae | standard | arXiv:2607.17558v1 | SRC-ARXIV@arXiv:2607.17558v1 | https://arxiv.org/html/2607.17558v1#S3 — 3 Method; https://arxiv.org/html/2607.17558v1#A2 — Appendix B Training Variants and Implementation Details | https://arxiv.org/html/2607.17558v1#A3 — Appendix C Experimental Details; https://arxiv.org/html/2607.17558v1#A3.SS3 — C.3 Final Evaluation of EMA-Regularized FA-SD | https://arxiv.org/html/2607.17558v1#S4.SS7 — 4.7 Discussion; https://arxiv.org/html/2607.17558v1#S5 — 5 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-17558 | complete |
| SF-2026-ARXIV-2607-17568 | RP-0cb2cef40d66ba56 | standard | arXiv:2607.17568v1 | SRC-ARXIV@arXiv:2607.17568v1 | https://arxiv.org/html/2607.17568v1#A13 — Appendix M Baseline Methods; https://arxiv.org/html/2607.17568v1#S2 — 2 Method | https://arxiv.org/html/2607.17568v1#A14 — Appendix N Evaluation Protocol; https://arxiv.org/html/2607.17568v1#A15 — Appendix O Full Per-Model Results | https://arxiv.org/html/2607.17568v1#A24 — Appendix X Limitations; https://arxiv.org/html/2607.17568v1#S6 — 6 Conclusion | Exact v1 links https://github.com/GongZhiren/CoCurve, https://huggingface.co/blog/falcon3, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-17568 | complete |
| SF-2026-ARXIV-2607-17572 | RP-c7611ade6e1fa82f | standard | arXiv:2607.17572v1 | SRC-ARXIV@arXiv:2607.17572v1 | https://arxiv.org/html/2607.17572v1#Sx3 — Method; https://arxiv.org/html/2607.17572v1#A3 — Appendix C JAGG Implementation Pseudocode | https://arxiv.org/html/2607.17572v1#A1 — Appendix A Experiment Figures; https://arxiv.org/html/2607.17572v1#A4 — Appendix D Experimental Setup and Hyperparameters | https://arxiv.org/html/2607.17572v1#Sx5 — Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-17572 | complete |
| SF-2026-ARXIV-2607-17574 | RP-5ce7062f2c5b7a1e | standard | arXiv:2607.17574v1 | SRC-ARXIV@arXiv:2607.17574v1 | https://arxiv.org/html/2607.17574v1#S3 — 3 Method; https://arxiv.org/html/2607.17574v1#S4.SS2 — 4.2 Reward Design | https://arxiv.org/html/2607.17574v1#S5 — 5 Experiments; https://arxiv.org/html/2607.17574v1#S5.SS2 — 5.2 Ablation Study | https://arxiv.org/html/2607.17574v1#S5.SS5 — 5.5 Discussion; https://arxiv.org/html/2607.17574v1#S6 — 6 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-17574 | complete |
| SF-2026-ARXIV-2607-17575 | RP-ad9641f1309dae15 | standard | arXiv:2607.17575v1 | SRC-ARXIV@arXiv:2607.17575v1 | https://arxiv.org/html/2607.17575v1#S3 — 3 Proposed Method | https://arxiv.org/html/2607.17575v1#S5 — 5 Result Analysis; https://arxiv.org/html/2607.17575v1#A2 — Appendix B Faithfulness Analysis of Explanation Spans | https://arxiv.org/html/2607.17575v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.17575v1#Sx1 — Limitations | Exact v1 links https://anth2023.emnlp-demo.40/, https://dx.doi.org/10.18653/v1/2023.emnlp-demo.40, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-17575 | complete |
| SF-2026-ARXIV-2607-17598 | RP-04a8da30dbcd74a2 | standard | arXiv:2607.17598v1 | SRC-ARXIV@arXiv:2607.17598v1 | https://arxiv.org/html/2607.17598v1#A1 — Appendix A Methodology details; https://arxiv.org/html/2607.17598v1#S3.SS2 — 3.2 The three approaches | https://arxiv.org/html/2607.17598v1#A3 — Appendix C Additional experimental results; https://arxiv.org/html/2607.17598v1#A2 — Appendix B Experimental setup | https://arxiv.org/html/2607.17598v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.17598v1#Sx1 — Limitations | Exact v1 links https://github.com/benchflow-ai/benchflow, https://www.latent.space/p/claude-code, https://github.com/yusufkaraaslan/Skill_Seekers; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-17598 | complete |
| SF-2026-ARXIV-2607-17619 | RP-f47689e33f44a5e6 | standard | arXiv:2607.17619v1 | SRC-ARXIV@arXiv:2607.17619v1 | https://arxiv.org/html/2607.17619v1#S5 — 5. Study Design; https://arxiv.org/html/2607.17619v1#S2.SS1 — 2.1. Large Language Model-based Code Generation | https://arxiv.org/html/2607.17619v1#S5.SS3 — 5.3. Experimental Pipeline; https://arxiv.org/html/2607.17619v1#S5.SS4 — 5.4. Evaluation Metrics | https://arxiv.org/html/2607.17619v1#S9 — 9. Conclusion and Future Work; https://arxiv.org/html/2607.17619v1#S4 — 4. Threat Model | Exact v1 links https://github.com/filestack/filestack-python/blob/0e44e337e88051ade0b2873c600ada0744d10794/examples/intelligent_ingestion.py#L2, https://copilot.github.com/, https://codeql.github.com/; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-17619 | complete |
| SF-2026-ARXIV-2607-17621 | RP-1616d7eadc87e45f | standard | arXiv:2607.17621v1 | SRC-ARXIV@arXiv:2607.17621v1 | https://arxiv.org/html/2607.17621v1#A2 — Appendix B Algorithm of AGMR; https://arxiv.org/html/2607.17621v1#A5.SS3 — E.3 Other implementation details | https://arxiv.org/html/2607.17621v1#A3.SS3 — C.3 Ablation validation of retrieval heads; https://arxiv.org/html/2607.17621v1#A5 — Appendix E Experiments details | https://arxiv.org/html/2607.17621v1#S5 — 5 Conclusion | Exact v1 links https://anonymous.4open.science/r/AGMR_code-3262/, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-17621 | complete |
| SF-2026-ARXIV-2607-17624 | RP-79291f3160e8f0c7 | standard | arXiv:2607.17624v1 | SRC-ARXIV@arXiv:2607.17624v1 | https://arxiv.org/html/2607.17624v1#S2 — 2 Proposed Method to Optimize Architectures; https://arxiv.org/html/2607.17624v1#S3.SS2 — 3.2 Compatibility of Optimized Architectures Across Algorithmic Tasks | https://arxiv.org/html/2607.17624v1#A3 — Appendix C Additional Results on Algorithmic Tasks; https://arxiv.org/html/2607.17624v1#A4 — Appendix D Additional Results on Language Modeling | https://arxiv.org/html/2607.17624v1#S6 — 6 Discussion | Exact v1 links https://github.com/idiap/lm-afs, https://huggingface.co/microsoft/CodeGPT-small-py, https://github.com/KellerJordan/modded-nanogpt; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-17624 | complete |
| SF-2026-ARXIV-2607-17641 | RP-d9f59bdd101ed7dd | standard | arXiv:2607.17641v1 | SRC-ARXIV@arXiv:2607.17641v1 | https://arxiv.org/html/2607.17641v1#S4 — 4 Method; https://arxiv.org/html/2607.17641v1#A1 — Appendix A Derivations, Algorithms, and Reference Policies | https://arxiv.org/html/2607.17641v1#A4 — Appendix D Full Stopping and Cross-Benchmark Results; https://arxiv.org/html/2607.17641v1#A1.SS3 — A.3 Proof and Numerical Evaluation of Lemma 1 | https://arxiv.org/html/2607.17641v1#A3 — Appendix C Full Loop Dynamics and Failure Cases; https://arxiv.org/html/2607.17641v1#A3.SS2 — C.2 A Representative Failure Trace | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-17641 | complete |
| SF-2026-ARXIV-2607-17644 | RP-6499f13f73262835 | deep | arXiv:2607.17644v1 | SRC-ARXIV@arXiv:2607.17644v1 | https://arxiv.org/html/2607.17644v1#S1 — 1 Introduction; https://arxiv.org/html/2607.17644v1#S2 — 2 Background | https://arxiv.org/html/2607.17644v1#S4 — 4 Evaluation | https://arxiv.org/html/2607.17644v1#S8 — 8 Discussion and Limitations; https://arxiv.org/html/2607.17644v1#S4.SS7 — 4.7 Limitations and scope | Exact v1 links https://github.com/NVIDIA/Megatron-LM, https://github.com/deepseek-ai/DeepEP, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-17644 | complete |
| SF-2026-ARXIV-2607-17652 | RP-736de9ac95ffa7f1 | deep | arXiv:2607.17652v1 | SRC-ARXIV@arXiv:2607.17652v1 | https://arxiv.org/html/2607.17652v1#S4 — 4 FlowBlock Framework | https://arxiv.org/html/2607.17652v1#S5 — 5 Evaluation; https://arxiv.org/html/2607.17652v1#S5.SS1 — 5.1 Experimental Setup | https://arxiv.org/html/2607.17652v1#S6 — 6 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-17652 | complete |
| SF-2026-ARXIV-2607-17673 | RP-e2c2d1d521a50878 | standard | arXiv:2607.17673v1 | SRC-ARXIV@arXiv:2607.17673v1 | https://arxiv.org/html/2607.17673v1#S3 — 3 Method | https://arxiv.org/html/2607.17673v1#S4 — 4 Experiments; https://arxiv.org/html/2607.17673v1#S4.SS2 — 4.2 Experimental Setup | https://arxiv.org/html/2607.17673v1#S5 — 5 Conclusion, Limitations & Future Work | Exact v1 links https://github.com/TillmannRheude/gpe, https://github.com/Lightning-AI/lightning, http://github.com/google-research/tuning_playbook; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-17673 | complete |
| SF-2026-ARXIV-2607-17696 | RP-05d19c37c0d65560 | standard | arXiv:2607.17696v1 | SRC-ARXIV@arXiv:2607.17696v1 | https://arxiv.org/html/2607.17696v1#S3.SS8 — 3.8 Computational complexity of Algorithms 1 and 3; https://arxiv.org/html/2607.17696v1#S4.SS1 — 4.1 Simulation model and metrics | https://arxiv.org/html/2607.17696v1#S4.SS3 — 4.3 Running results | https://arxiv.org/html/2607.17696v1#S5 — 5 Conclusion and limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-17696 | complete |
| SF-2026-ARXIV-2607-17701 | RP-44232a48ef62342c | standard | arXiv:2607.17701v1 | SRC-ARXIV@arXiv:2607.17701v1 | https://arxiv.org/html/2607.17701v1#S1 — 1 Introduction; https://arxiv.org/html/2607.17701v1#S2 — 2 Related Work | https://arxiv.org/html/2607.17701v1#S5.SS1 — 5.1 Results Analysis; https://arxiv.org/html/2607.17701v1#A3 — Appendix C ProEvent Realism Evaluation | https://arxiv.org/html/2607.17701v1#S5.SS2 — 5.2 Discussion; https://arxiv.org/html/2607.17701v1#S6 — 6 Conclusion | Exact v1 links https://github.com/volcengine/MineContext, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-17701 | complete |
| SF-2026-ARXIV-2607-17710 | RP-008928bf3b5bbf25 | standard | arXiv:2607.17710v1 | SRC-ARXIV@arXiv:2607.17710v1 | https://arxiv.org/html/2607.17710v1#S3 — 3 The Chain of Computation (COC) Architecture | https://arxiv.org/html/2607.17710v1#A1 — Appendix A Experimental Setup; https://arxiv.org/html/2607.17710v1#A8 — Appendix H Extended Training Scaling Results | https://arxiv.org/html/2607.17710v1#S7 — 7 Conclusion and Future Work; https://arxiv.org/html/2607.17710v1#S6 — 6 Discussion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-17710 | complete |
| SF-2026-ARXIV-2607-17715 | RP-9f52aad1558c5487 | deep | arXiv:2607.17715v1 | SRC-ARXIV@arXiv:2607.17715v1 | https://arxiv.org/html/2607.17715v1#A3.SS2 — C.2. Method-Specific TTFT Components; https://arxiv.org/html/2607.17715v1#S2.SS3 — 2.3. Limitations of Existing Reuse Methods | https://arxiv.org/html/2607.17715v1#A2.SS2 — B.2. Evaluation Setup; https://arxiv.org/html/2607.17715v1#A4 — Appendix D Full Results | https://arxiv.org/html/2607.17715v1#A5 — Appendix E Limitations and Future Work; https://arxiv.org/html/2607.17715v1#S2.SS3 — 2.3. Limitations of Existing Reuse Methods | Exact v1 links https://github.com/s7a9/C2KV, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-17715 | complete |
| SF-2026-ARXIV-2607-17733 | RP-c58f68c026140319 | deep | arXiv:2607.17733v1 | SRC-ARXIV@arXiv:2607.17733v1 | https://arxiv.org/html/2607.17733v1#A1.SS1 — A.1 Language Model Usage in the Paper | https://arxiv.org/html/2607.17733v1#A1.SS10 — A.10 Additional Results for the Ablation Study; https://arxiv.org/html/2607.17733v1#S5 — 5 Experimental Results | https://arxiv.org/html/2607.17733v1#S7 — 7 Conclusion | Exact v1 links https://github.com/parsa-epfl/mxsens, https://huggingface.co/datasets/wikitext/tree/main, https://huggingface.co/meta-llama/Meta-Llama-3-8B; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-17733 | complete |
| SF-2026-ARXIV-2607-17751 | RP-718319387c6a58f6 | standard | arXiv:2607.17751v1 | SRC-ARXIV@arXiv:2607.17751v1 | https://arxiv.org/html/2607.17751v1#S3.SS1 — 3.1 Dataset Construction via a State-Machine-Driven Framework; https://arxiv.org/html/2607.17751v1#S3.SS3 — 3.3 Preference Reward Modeling | https://arxiv.org/html/2607.17751v1#S6.SS1 — 6.1 Evaluation Benchmarks; https://arxiv.org/html/2607.17751v1#S2.SS2 — 2.2 Benchmarks for Tool Retrieval | https://arxiv.org/html/2607.17751v1#S7 — 7 Conclusion | Exact v1 links https://huggingface.co/Alibaba-NLP/gte-Qwen2-7B-instruct, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-17751 | complete |
| SF-2026-ARXIV-2607-17780 | RP-31d806eb74e5935a | standard | arXiv:2607.17780v1 | SRC-ARXIV@arXiv:2607.17780v1 | https://arxiv.org/html/2607.17780v1#S3.SS3 — 3.3. Design Restrictions; https://arxiv.org/html/2607.17780v1#S7 — 7. Implementation | https://arxiv.org/html/2607.17780v1#S5.SS1 — 5.1. Expression Evaluation; https://arxiv.org/html/2607.17780v1#S8 — 8. Evaluation | https://arxiv.org/html/2607.17780v1#S10 — 10. Conclusion | Exact v1 links https://github.com/etas-project/etas, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-17780 | complete |
| SF-2026-ARXIV-2607-17786 | RP-83d21e19d30ee094 | standard | arXiv:2607.17786v1 | SRC-ARXIV@arXiv:2607.17786v1 | https://arxiv.org/html/2607.17786v1#S4 — 4 Cross-stage robustness across reasoning architectures; https://arxiv.org/html/2607.17786v1#A15 — Appendix O LIBERO-Plus naturalistic-perturbation cross-benchmark: per-(model, factor) details | https://arxiv.org/html/2607.17786v1#A11 — Appendix K Amplification analysis: full results; https://arxiv.org/html/2607.17786v1#A13 — Appendix M CoT-disabled ablation: full results | https://arxiv.org/html/2607.17786v1#S6 — 6 Discussion and conclusion; https://arxiv.org/html/2607.17786v1#A16 — Appendix P Limitations (extended) | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-17786 | complete |
| SF-2026-ARXIV-2607-17843 | RP-124d7a1ab61228e7 | standard | arXiv:2607.17843v1 | SRC-ARXIV@arXiv:2607.17843v1 | https://arxiv.org/html/2607.17843v1#S2 — 2 Methodology; https://arxiv.org/html/2607.17843v1#A1 — Appendix A Implementation Notes | https://arxiv.org/html/2607.17843v1#S2.SS4 — 2.4 Training and Evaluation Objectives; https://arxiv.org/html/2607.17843v1#S3 — 3 Main Results | https://arxiv.org/html/2607.17843v1#S5 — 5 Next Version and Future Work | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-17843 | complete |
| SF-2026-ARXIV-2607-17879 | RP-d401646f09f2dba3 | standard | arXiv:2607.17879v1 | SRC-ARXIV@arXiv:2607.17879v1 | https://arxiv.org/html/2607.17879v1#S3 — 3 Methodology; https://arxiv.org/html/2607.17879v1#S3.SS2 — 3.2 EAR Framework | https://arxiv.org/html/2607.17879v1#S4.SS5 — 4.5 Results and Analysis; https://arxiv.org/html/2607.17879v1#S5.SS2 — 5.2 Results and Analysis | https://arxiv.org/html/2607.17879v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.17879v1#Sx1 — Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-17879 | complete |
| SF-2026-ARXIV-2607-17884 | RP-2cdff9efac51152b | standard | arXiv:2607.17884v1 | SRC-ARXIV@arXiv:2607.17884v1 | https://arxiv.org/html/2607.17884v1#S3 — 3 Method; https://arxiv.org/html/2607.17884v1#S6.SS1 — 6.1 Methodological Analysis | https://arxiv.org/html/2607.17884v1#A1 — Appendix A Additional Experiments and Analyses; https://arxiv.org/html/2607.17884v1#A1.SS1 — A.1 Prompt Configurations and Experimental Settings | https://arxiv.org/html/2607.17884v1#A1.SS9 — A.9 Limitations and Future Work; https://arxiv.org/html/2607.17884v1#S7 — 7 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-17884 | complete |
| SF-2026-ARXIV-2607-17914 | RP-e7321f69bf7aa56f | standard | arXiv:2607.17914v1 | SRC-ARXIV@arXiv:2607.17914v1 | https://arxiv.org/html/2607.17914v1#S3.SS2 — III-B Actor-Critic Architecture in MARL; https://arxiv.org/html/2607.17914v1#S4 — IV Methodology | https://arxiv.org/html/2607.17914v1#A3 — Appendix C Extended Experimental Results; https://arxiv.org/html/2607.17914v1#S5.SS2 — V-B Results and Analysis | https://arxiv.org/html/2607.17914v1#S6 — VI Conclusion | Exact v1 links https://github.com/robust-comm-marl-IROS2026/Value-Aware-Prediction-Under-Communication-Loss, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-17914 | complete |
| SF-2026-ARXIV-2607-17924 | RP-a121d44e1505339f | standard | arXiv:2607.17924v1 | SRC-ARXIV@arXiv:2607.17924v1 | https://arxiv.org/html/2607.17924v1#S1 — 1 Introduction; https://arxiv.org/html/2607.17924v1#S2 — 2 Preliminaries | https://arxiv.org/html/2607.17924v1#A3 — Appendix C Experimental Details and Additional Results; https://arxiv.org/html/2607.17924v1#S4.SS2 — 4.2 Experiment Results | https://arxiv.org/html/2607.17924v1#A5 — Appendix E Discussion; https://arxiv.org/html/2607.17924v1#S5 — 5 Conclusion | Exact v1 links https://github.com/RS2002/MAPO, https://github.com/LucasAlegre/sumo-rl, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-17924 | complete |
| SF-2026-ARXIV-2607-17937 | RP-64e19328766e56b3 | standard | arXiv:2607.17937v1 | SRC-ARXIV@arXiv:2607.17937v1 | https://arxiv.org/html/2607.17937v1#S3 — 3 White-Box Study Design; https://arxiv.org/html/2607.17937v1#S3.SS1 — 3.1 Design Goals | https://arxiv.org/html/2607.17937v1#A2.SS2 — B.2 Experimental Matrix; https://arxiv.org/html/2607.17937v1#S4.SS4 — 4.4 Statistical Analysis | https://arxiv.org/html/2607.17937v1#A1 — Appendix A Failure-Coding Guide; https://arxiv.org/html/2607.17937v1#S2.SS4 — 2.4 Visible Failure Locations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-17937 | complete |
| SF-2026-ARXIV-2607-17973 | RP-d4324acbad78d547 | standard | arXiv:2607.17973v1 | SRC-ARXIV@arXiv:2607.17973v1 | https://arxiv.org/html/2607.17973v1#A1.SS3 — A.3 Architecture and Training Details; https://arxiv.org/html/2607.17973v1#S2.SS1 — 2.1 Latent World Model Planning | https://arxiv.org/html/2607.17973v1#A1.SS2 — A.2 Canonical Evaluation Protocol; https://arxiv.org/html/2607.17973v1#A1.SS6 — A.6 Per-Seed Main Results | https://arxiv.org/html/2607.17973v1#S5 — 5 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-17973 | complete |
| SF-2026-ARXIV-2607-17979 | RP-a4242f92da1463fc | deep | arXiv:2607.17979v1 | SRC-ARXIV@arXiv:2607.17979v1 | https://arxiv.org/html/2607.17979v1#S2 — 2 Harness System Design; https://arxiv.org/html/2607.17979v1#S5.SS2 — 5.2 Implementation Stack | https://arxiv.org/html/2607.17979v1#S4 — 4 Experimental Evaluation; https://arxiv.org/html/2607.17979v1#A4 — Appendix D Ablation Notes | https://arxiv.org/html/2607.17979v1#S6 — 6 Limitations and Future Directions; https://arxiv.org/html/2607.17979v1#S7 — 7 Conclusion | Exact v1 links https://github.com/syhya/mlsys26-flashinfer-contest, https://github.com/syhya/mlsys26-flashinfer-solution-fused-moe, https://github.com/syhya/mlsys26-flashinfer-solution-sparse-attention; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-17979 | complete |
| SF-2026-ARXIV-2607-17986 | RP-ca6fe9b2da8ab78d | standard | arXiv:2607.17986v1 | SRC-ARXIV@arXiv:2607.17986v1 | https://arxiv.org/html/2607.17986v1#A6.SS1 — F.1. Harness Architecture; https://arxiv.org/html/2607.17986v1#S3 — 3. Limits of Operating System Defenses | https://arxiv.org/html/2607.17986v1#A6 — Appendix F Experimental Settings; https://arxiv.org/html/2607.17986v1#A7.SS3 — G.3. Workload-Conditioning Ablation: B1 vs B2 Detail | https://arxiv.org/html/2607.17986v1#A5 — Appendix E Mapping of the Canonical Cells to Established Threat Catalogs; https://arxiv.org/html/2607.17986v1#A7 — Appendix G Extended Discussion | Exact v1 links https://github.com/anomalyco/opencode, https://docs.claude.com/en/docs/claude-code/overview, https://blogs.cisco.com/ai/identifying-and-remediating-a-persistent-memory-compromise-in-claude-code; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-17986 | complete |
| SF-2026-ARXIV-2607-18002 | RP-7d87ab481513688e | deep | arXiv:2607.18002v1 | SRC-ARXIV@arXiv:2607.18002v1 | https://arxiv.org/html/2607.18002v1#S4.SS1 — 4.1. GPU Sharing Design Space; https://arxiv.org/html/2607.18002v1#S2.SS2 — 2.2. GPU Execution Model | https://arxiv.org/html/2607.18002v1#S7 — 7. Evaluation; https://arxiv.org/html/2607.18002v1#S7.SS1 — 7.1. Experiment Setup | https://arxiv.org/html/2607.18002v1#S9 — 9. Conclusion | Exact v1 links https://github.com/deepseek-ai/open-infra-index/blob/main/202502OpenSourceWeek/day_6_one_more_thing_deepseekV3R1_inference_system_overview.md, https://github.com/deepseek-ai/DeepEP, https://github.com/tile-ai/TileRT; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18002 | complete |
| SF-2026-ARXIV-2607-18016 | RP-4f150343dba2824e | deep | arXiv:2607.18016v1 | SRC-ARXIV@arXiv:2607.18016v1 | https://arxiv.org/html/2607.18016v1#A1 — Appendix Appendix A Additional Method and Experiment Details; https://arxiv.org/html/2607.18016v1#S2.SS3 — 2.3 Humanoid Loco-Manipulation Systems | https://arxiv.org/html/2607.18016v1#A1 — Appendix Appendix A Additional Method and Experiment Details; https://arxiv.org/html/2607.18016v1#S4 — 4 Experiments | https://arxiv.org/html/2607.18016v1#S5 — 5 Conclusion and Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18016 | complete |
| SF-2026-ARXIV-2607-18026 | RP-4628fc59bfba31d4 | standard | arXiv:2607.18026v1 | SRC-ARXIV@arXiv:2607.18026v1 | https://arxiv.org/html/2607.18026v1#S3 — 3 Method | https://arxiv.org/html/2607.18026v1#A1 — Appendix A Additional Task-Level Results; https://arxiv.org/html/2607.18026v1#A3.SS1 — C.1 Ablation Controls and Baseline Comparisons | https://arxiv.org/html/2607.18026v1#S7 — 7 Conclusion; https://arxiv.org/html/2607.18026v1#Sx1 — Limitations | Exact v1 links https://github.com/bigcode-project/bigcode-evaluation-harness, https://huggingface.co/Qwen/Qwen3-4B-Thinking-2507, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18026 | complete |
| SF-2026-ARXIV-2607-18039 | RP-f274a2b7177daa0f | standard | arXiv:2607.18039v1 | SRC-ARXIV@arXiv:2607.18039v1 | https://arxiv.org/html/2607.18039v1#S4 — 4. Method; https://arxiv.org/html/2607.18039v1#S4.SS2 — 4.2. Evidence-Grounded Workflow Design | https://arxiv.org/html/2607.18039v1#S6 — 6. Experiments; https://arxiv.org/html/2607.18039v1#S6.SS1 — 6.1. Evaluation Scope and Claims | https://arxiv.org/html/2607.18039v1#S8 — 8. Limitations and Future Work; https://arxiv.org/html/2607.18039v1#S7 — 7. Discussion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18039 | complete |
| SF-2026-ARXIV-2607-18046 | RP-ae052286f878deb9 | standard | arXiv:2607.18046v1 | SRC-ARXIV@arXiv:2607.18046v1 | https://arxiv.org/html/2607.18046v1#S1 — 1. Introduction; https://arxiv.org/html/2607.18046v1#S2 — 2. Related Work | https://arxiv.org/html/2607.18046v1#S5 — 5. Experiment; https://arxiv.org/html/2607.18046v1#S5.SS1 — 5.1. Experimental Setup | https://arxiv.org/html/2607.18046v1#S6 — 6. Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18046 | complete |
| SF-2026-ARXIV-2607-18057 | RP-724b31a888d6efa8 | standard | arXiv:2607.18057v1 | SRC-ARXIV@arXiv:2607.18057v1 | https://arxiv.org/html/2607.18057v1#S3 — III Methodology | https://arxiv.org/html/2607.18057v1#S3.SS3 — III-C RQ2: Measuring Diff Coverage and Analysis; https://arxiv.org/html/2607.18057v1#S4 — IV Results | https://arxiv.org/html/2607.18057v1#S5 — V Discussion and Future Direction; https://arxiv.org/html/2607.18057v1#S6 — VI Related Work, Limitations | Exact v1 links https://github.com/SageSELab/Agentic-Pull-Request-Test-Coverage/, https://pypi.org/project/pytest-cov/, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18057 | complete |
| SF-2026-ARXIV-2607-18060 | RP-1fecfeb77fc61d18 | standard | arXiv:2607.18060v1 | SRC-ARXIV@arXiv:2607.18060v1 | https://arxiv.org/html/2607.18060v1#S4 — 4 Methodology | https://arxiv.org/html/2607.18060v1#S5 — 5 Experimental Setup and Baselines; https://arxiv.org/html/2607.18060v1#S5.SS1 — 5.1 Experimental Setup | https://arxiv.org/html/2607.18060v1#S9 — 9 Limitations and Future Work; https://arxiv.org/html/2607.18060v1#S10 — 10 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18060 | complete |
| SF-2026-ARXIV-2607-18063 | RP-e2c71b9fbf9e1265 | standard | arXiv:2607.18063v1 | SRC-ARXIV@arXiv:2607.18063v1 | https://arxiv.org/html/2607.18063v1#S3 — 3 Design principles; https://arxiv.org/html/2607.18063v1#A2.SSx1 — B.0 Model inventory | https://arxiv.org/html/2607.18063v1#A2 — Appendix B Cross-Benchmark Metric Tables; https://arxiv.org/html/2607.18063v1#A2.SSx13 — B.12 Adaptivity ablation: non-adaptive attacker and stateful defender | https://arxiv.org/html/2607.18063v1#A3.SSx1 — C.1 memleak : Opus failure mode; https://arxiv.org/html/2607.18063v1#A3.SSx2 — C.2 smarthomejack : GPT-5.4 failure mode | Exact v1 links https://github.com/UKGovernmentBEIS/inspect_evals/tree/main/src/inspect_evals/ipi_coding_agent, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18063 | complete |
| SF-2026-ARXIV-2607-18080 | RP-8a28c66e5d1108d9 | standard | arXiv:2607.18080v1 | SRC-ARXIV@arXiv:2607.18080v1 | https://arxiv.org/html/2607.18080v1#A3.SSx1 — Reward Design Details; https://arxiv.org/html/2607.18080v1#Sx3 — Method | https://arxiv.org/html/2607.18080v1#A4 — Appendix D Reward Ablation Study; https://arxiv.org/html/2607.18080v1#Sx4 — Experiments | https://arxiv.org/html/2607.18080v1#Sx1 — Introduction; https://arxiv.org/html/2607.18080v1#Sx2 — Related Work | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18080 | complete |
| SF-2026-ARXIV-2607-18081 | RP-8cbe57ec59501622 | deep | arXiv:2607.18081v1 | SRC-ARXIV@arXiv:2607.18081v1 | https://arxiv.org/html/2607.18081v1#S2.SS2 — 2.2 Model-Specific Neurons | https://arxiv.org/html/2607.18081v1#S6 — 6 Evaluation | https://arxiv.org/html/2607.18081v1#S8 — 8 Conclusion | Exact v1 links https://www.projectpro.io/article/large-language-model-use-cases-and-applications/887, https://github.com/zylon-ai/private-gpt, https://huggingface.co/meta-llama/Llama-3.2-3B; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18081 | complete |
| SF-2026-ARXIV-2607-18086 | RP-1ec726ad96e1100e | standard | arXiv:2607.18086v1 | SRC-ARXIV@arXiv:2607.18086v1 | https://arxiv.org/pdf/2607.18086v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.18086v1#page=10 — PDF page 10 | https://arxiv.org/pdf/2607.18086v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.18086v1#page=10 — PDF page 10 | https://arxiv.org/pdf/2607.18086v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.18086v1#page=10 — PDF page 10 | Exact v1 links https://github.com/aiden-ygu/health-ai-, https://huggingface.co/datasets/jjfenglab/Real-, https://github.com/MAGIC-AI4Med/MedRBench; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18086 | complete |
| SF-2026-ARXIV-2607-18098 | RP-03246198b63f7e48 | standard | arXiv:2607.18098v1 | SRC-ARXIV@arXiv:2607.18098v1 | https://arxiv.org/html/2607.18098v1#S3 — 3 Method; https://arxiv.org/html/2607.18098v1#A4 — Appendix D Rasch Difficulty Estimation Implementation | https://arxiv.org/html/2607.18098v1#S5 — 5 Experimental Results and Discussion; https://arxiv.org/html/2607.18098v1#A1 — Appendix A Difficulty Analysis Prompt | https://arxiv.org/html/2607.18098v1#S5 — 5 Experimental Results and Discussion; https://arxiv.org/html/2607.18098v1#S6 — 6 Conclusion | Exact v1 links https://huggingface.co/datasets/lmarena-ai/arena-expert-5k, https://github.com/ulab-uiuc/LLMRouter, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18098 | complete |
| SF-2026-ARXIV-2607-18100 | RP-af1124bd8c03fd6f | standard | arXiv:2607.18100v1 | SRC-ARXIV@arXiv:2607.18100v1 | https://arxiv.org/html/2607.18100v1#S4 — 4 Methodology | https://arxiv.org/html/2607.18100v1#A2 — Appendix B Detailed Phase-Trajectory Analysis; https://arxiv.org/html/2607.18100v1#S2 — 2 Reasoning-State Transition Analysis | https://arxiv.org/html/2607.18100v1#S6 — 6 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18100 | complete |
| SF-2026-ARXIV-2607-18101 | RP-312502d3fef040b3 | standard | arXiv:2607.18101v1 | SRC-ARXIV@arXiv:2607.18101v1 | https://arxiv.org/html/2607.18101v1#S3 — 3 Experimental Methodology; https://arxiv.org/html/2607.18101v1#S3.SS1 — 3.1 Heterogeneous On-Device Adaptation Architecture | https://arxiv.org/html/2607.18101v1#S3 — 3 Experimental Methodology; https://arxiv.org/html/2607.18101v1#S3.SS3 — 3.3 Experimental Setup | https://arxiv.org/html/2607.18101v1#S5 — 5 Conclusion | Exact v1 links https://github.com/MatPiech/onnxruntime, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18101 | complete |
| SF-2026-ARXIV-2607-18108 | RP-cbf748fa76cba9d0 | standard | arXiv:2607.18108v1 | SRC-ARXIV@arXiv:2607.18108v1 | https://arxiv.org/html/2607.18108v1#S2 — 2 Methodology; https://arxiv.org/html/2607.18108v1#S3.SS3 — 3.3 Evaluation Methodology: LLM-as-a-Judge | https://arxiv.org/html/2607.18108v1#S3.SS1 — 3.1 Evaluation Benchmarks; https://arxiv.org/html/2607.18108v1#S4 — 4 Results and Analysis | https://arxiv.org/html/2607.18108v1#S5 — 5 Discussion and Limitation; https://arxiv.org/html/2607.18108v1#S4.SS1 — 4.1 Inference Capability on Unknown Threats (Answering RQ1) | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18108 | complete |
| SF-2026-ARXIV-2607-18110 | RP-cc8cda9c1a7084cb | standard | arXiv:2607.18110v1 | SRC-ARXIV@arXiv:2607.18110v1 | https://arxiv.org/html/2607.18110v1#S2 — 2 Method | https://arxiv.org/html/2607.18110v1#A1 — Appendix A Details of Experiments; https://arxiv.org/html/2607.18110v1#A1.SS2 — A.2 Ablation Prompt Templates | https://arxiv.org/html/2607.18110v1#S4 — 4 Discussion; https://arxiv.org/html/2607.18110v1#S6 — 6 Conclusion | Exact v1 links https://aka.ms/el-code, https://github.com/EQ-bench/creative-writing-bench, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18110 | complete |
| SF-2026-ARXIV-2607-18114 | RP-a923cd44f9e3bd1e | standard | arXiv:2607.18114v1 | SRC-ARXIV@arXiv:2607.18114v1 | https://arxiv.org/html/2607.18114v1#S3 — 3 Methodology | https://arxiv.org/html/2607.18114v1#A3 — Appendix C Cluster structure analysis; https://arxiv.org/html/2607.18114v1#S4 — 4 Experimental Setup | https://arxiv.org/html/2607.18114v1#S10 — 10 Conclusion; https://arxiv.org/html/2607.18114v1#S9 — 9 Discussion | Exact v1 links https://github.com/prakharg55/bias-direction-EMNLP, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18114 | complete |
| SF-2026-ARXIV-2607-18141 | RP-b9e92cecfce168a6 | deep | arXiv:2607.18141v1 | SRC-ARXIV@arXiv:2607.18141v1 | https://arxiv.org/html/2607.18141v1#S1 — 1. Introduction; https://arxiv.org/html/2607.18141v1#S2 — 2. Background and Motivation | https://arxiv.org/html/2607.18141v1#S5 — 5. Experimental Setup; https://arxiv.org/html/2607.18141v1#S6 — 6. Evaluation | https://arxiv.org/html/2607.18141v1#S8 — 8. Conclusion | Exact v1 links https://github.com/ai-dynamo/nixl, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18141 | complete |
| SF-2026-ARXIV-2607-18155 | RP-17e78518b406159e | standard | arXiv:2607.18155v1 | SRC-ARXIV@arXiv:2607.18155v1 | https://arxiv.org/html/2607.18155v1#S2.SS2 — 2.2. Evaluation Metrics for RAG Systems; https://arxiv.org/html/2607.18155v1#S3 — 3. Chunk Coverage for Testing RAG Systems | https://arxiv.org/html/2607.18155v1#S2.SS2 — 2.2. Evaluation Metrics for RAG Systems; https://arxiv.org/html/2607.18155v1#S4 — 4. Experimental Setup | https://arxiv.org/html/2607.18155v1#S4.SS3 — 4.3. Failures and Faults in RAG Systems; https://arxiv.org/html/2607.18155v1#S7 — 7. Threats to Validity | Exact v1 links https://github.com/dbr7/issta26-chunk-coverage-artifact, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18155 | complete |
| SF-2026-ARXIV-2607-18161 | RP-17d3dc83436667d2 | standard | arXiv:2607.18161v1 | SRC-ARXIV@arXiv:2607.18161v1 | https://arxiv.org/html/2607.18161v1#S4 — IV Methodology; https://arxiv.org/html/2607.18161v1#S4.SS1 — IV-A System Overview | https://arxiv.org/html/2607.18161v1#S5 — V Experimental Design; https://arxiv.org/html/2607.18161v1#S5.SS2 — V-B Evaluation Metrics | https://arxiv.org/html/2607.18161v1#S8 — VIII Threats to Validity; https://arxiv.org/html/2607.18161v1#S8.SS1 — VIII-A Discussion | Exact v1 links https://claude.com/product/claude-code, https://github.com/features/copilot, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18161 | complete |
| SF-2026-ARXIV-2607-18171 | RP-3fafa117997b0357 | standard | arXiv:2607.18171v1 | SRC-ARXIV@arXiv:2607.18171v1 | https://arxiv.org/html/2607.18171v1#S9.SS1 — 9.1 Video World Model (WorldPlay) | https://arxiv.org/html/2607.18171v1#S9 — 9 Extended Deployment Results and Scaling Analysis; https://arxiv.org/html/2607.18171v1#S5 — 5 Experiments | https://arxiv.org/html/2607.18171v1#S6 — 6 Conclusion | Exact v1 links https://github.com/Infini-AI-Lab/FlashRT, https://code.claude.com/docs/en/overview, https://github.com/krea-ai/realtime-video; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18171 | complete |
| SF-2026-ARXIV-2607-18199 | RP-f6c1048d7de9d66e | standard | arXiv:2607.18199v1 | SRC-ARXIV@arXiv:2607.18199v1 | https://arxiv.org/html/2607.18199v1#S3 — 3 Methodology; https://arxiv.org/html/2607.18199v1#S4.SS1 — 4.1 Benchmarks and Models | https://arxiv.org/html/2607.18199v1#S4 — 4 Experiments and Results; https://arxiv.org/html/2607.18199v1#A2 — Appendix B Theoretical Analysis | https://arxiv.org/html/2607.18199v1#A2.SS2 — B.2 Discussion on Pruning Rates; https://arxiv.org/html/2607.18199v1#S6 — 6 Conclusion | Exact v1 links https://aclanthology.org/2020.emnlp-demos.6/, https://dx.doi.org/10.18653/v1/2020.emnlp-demos.6, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18199 | complete |
| SF-2026-ARXIV-2607-18213 | RP-38d899d238f09653 | standard | arXiv:2607.18213v1 | SRC-ARXIV@arXiv:2607.18213v1 | https://arxiv.org/html/2607.18213v1#S3 — 3 Method | https://arxiv.org/html/2607.18213v1#A3 — Appendix C Oolong Benchmark Conversion; https://arxiv.org/html/2607.18213v1#S4 — 4 Experiments | https://arxiv.org/html/2607.18213v1#S7 — 7 Conclusion; https://arxiv.org/html/2607.18213v1#Sx1 — Limitations | Exact v1 links https://github.com/Ayanami1314/swe-pruner-pro, https://github.com/SWE-agent/mini-swe-agent, https://huggingface.co/BAAI/bge-reranker-v2-m3; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18213 | complete |
| SF-2026-ARXIV-2607-18231 | RP-dac583b8a1aecc27 | standard | arXiv:2607.18231v1 | SRC-ARXIV@arXiv:2607.18231v1 | https://arxiv.org/html/2607.18231v1#A5.SS1 — E.1 Architecture details; https://arxiv.org/html/2607.18231v1#S3 — 3 Methodology | https://arxiv.org/html/2607.18231v1#A1 — Appendix A Additional Real-World Results; https://arxiv.org/html/2607.18231v1#A2 — Appendix B Task Definitions and Evaluation Protocol | https://arxiv.org/html/2607.18231v1#S5 — 5 Limitations; https://arxiv.org/html/2607.18231v1#S6 — 6 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-18231 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2607-16200:start -->
### Deterministic Replay for AI Agent Systems

<!-- claim:SF-2026-ARXIV-2607-16200:start -->AI agent systems that couple large language models (LLMs) with external tools and APIs are inherently non-deterministic: LLM sampling variance, external API state, CDN infrastructure headers, and execution-environment noise collectively prevent any prior agent run from being faithfully re-executed. Existing observability platforms capture execution logs but cannot reproduce a run in isolation. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16200:end -->

**为什么进入候选分母。** 摘要首要问题为“AI agent systems that couple large language models (LLMs) with external tools and APIs are inherently non-deterministic: LLM sampling variance, external API state, CDN infrastructure headers, and execution-environment noise collectively prevent any prior agent run from being faithfully re-executed.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** We present agrepl, a developer-first CLI framework for deterministic replay of agent executions. agrepl intercepts all external interactions at the transport layer via a man-in-the-middle (MITM) proxy, serialises them as structured execution traces, and replays them in a strictly isolated environment with zero outbound network access.

**证据证明什么。** Empirical evaluation across five workloads (n = 250 replay instances) demonstrates replay fidelity F = 1.0 and a median per-step latency reduction of 98.3%. agrepl is implemented in Go, ships as a single static binary, and is released under the MIT licence.

**证据没有证明什么。** Existing observability platforms capture execution logs but cannot reproduce a run in isolation. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/pdf/2607.16200v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.16200v1#page=2 — PDF page 2。Evaluation：https://arxiv.org/pdf/2607.16200v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.16200v1#page=2 — PDF page 2。Limitations / counterevidence：https://arxiv.org/pdf/2607.16200v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.16200v1#page=2 — PDF page 2。

**Artifact boundary。** Exact v1 links https://github.com/abshkbh/arrakis, https://github.com/spf13/cobra, https://github.com/elazarl/goproxy; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：Existing observability platforms capture execution logs but cannot reproduce a run in isolation.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-PLATFORM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16200:end -->

<!-- review:SF-2026-ARXIV-2607-16204:start -->
### Masked Diffusion Language Models are Strong and Steerable Text-Based World Models for Agentic RL

<!-- claim:SF-2026-ARXIV-2607-16204:start -->Recent growth in reinforcement learning (RL) has surfaced a need for diverse, specialized training environments. Hand-curated environments with fixed task and reward difficulties become ineffective signals as model performance improves, and sparse rewards over long horizons induce mode collapse on specific workflows or tool structures. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16204:end -->

**为什么进入候选分母。** 摘要首要问题为“Recent growth in reinforcement learning (RL) has surfaced a need for diverse, specialized training environments.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We introduce a plug-and-play GRPO training framework with deterministic state checks, and perform zero-shot transfer ablations on three OOD environments (ScienceWorld, ALFWorld, AppWorld) across three 1.2B-7B agent backbones (LFM2.5, Qwen3, Mistral), achieving up to 47% absolute gains over baselines without environment-specific fine-tuning.

**证据证明什么。** We compare AR LMs and masked diffusion language models (MDLMs), showing MDLMs, via bidirectional anchor-aware denoising, achieve better coherence, groundedness, and empirically validated rollout diversity than LLMs over 4x their parameter size, at comparable inference latency.

**证据没有证明什么。** Agent: open cupboard WM: ‘‘Error during execution: name ‘cupboard_is_opened’ is not defined’’ fabricated [2pt] Agent: activate solar panel WM: ‘‘Solar panels cannot be used directly.’’ not a ScienceWorld response (iii) JSON-wrapped responses SW WM outputs structured JSON instead of plain-text environment observations. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16204v1#A3 — Appendix C World Model Training Dataset Curation Details; https://arxiv.org/html/2607.16204v1#A4 — Appendix D Environment Setup for Downstream RL Agent Training with World Model Backend。Evaluation：https://arxiv.org/html/2607.16204v1#A1 — Appendix A Human Evaluations; https://arxiv.org/html/2607.16204v1#A2 — Appendix B Fairness of Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.16204v1#A8 — Appendix H World Model Failure Modes; https://arxiv.org/html/2607.16204v1#S5 — 5 Results and Discussion。

**Artifact boundary。** Exact v1 links https://huggingface.co/PatronusAI/world_model_corpus, https://github.com/patronus-ai/mdlm_world_modeling, https://huggingface.co/datasets/danilopeixoto/pandora-tool-calling; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Agent: open cupboard WM: ‘‘Error during execution: name ‘cupboard_is_opened’ is not defined’’ fabricated [2pt] Agent: activate solar panel WM: ‘‘Solar panels cannot be used directly.’’ not a ScienceWorld response (iii) JSON-wrapped responses SW WM outputs structured JSON instead of plain-text environment observations.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16204:end -->

<!-- review:SF-2026-ARXIV-2607-16208:start -->
### ColGraphRAG: Late-Interaction Evidence Retrieval for Multimodal GraphRAG

<!-- claim:SF-2026-ARXIV-2607-16208:start -->Graph-grounded multimodal question answering organizes text, tables, and images in a structured evidence graph, yet end-to-end accuracy depends on which multimodal assets are ranked highly enough to enter downstream reasoning; for graph-linked images, single-vector bi-encoder similarity can discard patch- and token-level structure needed for fine-grained alignment. We evaluate replacing the visual candidate-ranking operator over graph-linked image nodes with late-interaction MaxSim-style multi-vector scoring in the ColBERT/ColPali lineage, while keeping offline graph construction, text- and table-side retrieval, structured extraction, and downstream reasoning unchanged. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16208:end -->

**为什么进入候选分母。** 摘要首要问题为“Graph-grounded multimodal question answering organizes text, tables, and images in a structured evidence graph, yet end-to-end accuracy depends on which multimodal assets are ranked highly enough to enter downstream reasoning; for graph-linked images, single-vector bi-encoder similarity can discard patch- and token-level structure needed for fine-grained alignment.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We evaluate replacing the visual candidate-ranking operator over graph-linked image nodes with late-interaction MaxSim-style multi-vector scoring in the ColBERT/ColPali lineage, while keeping offline graph construction, text- and table-side retrieval, structured extraction, and downstream reasoning unchanged.

**证据证明什么。** On MultimodalQA, this change is associated with improved retrieval-stage point estimates for graph-linked image candidates and downstream QA gains, with larger movement where visual evidence matters most and mixed trends on text-dominant questions; we interpret the pattern as mechanism-level evidence for graph-linked visual evidence inclusion, while broader validation and finer graph-level diagnostics remain important future work.

**证据没有证明什么。** 5 Conclusion We isolated graph-linked image candidate ranking within a graph-grounded multimodal QA pipeline by keeping offline construction of , baseline text- and table-side retrieval, and graph-grounded answering unchanged while replacing only the graph-linked image ranker with late-interaction MaxSim scoring [ 13 , 15 ] ; on MultimodalQA this is associated with improved retrieval-stage candidate-ranking point estimates and higher aggregate EM/F1 point estimates, but yields mixed modality trends, including a small regression on text-dominant items. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16208v1#S3 — 3 Method; https://arxiv.org/html/2607.16208v1#S4.SS1 — 4.1 Experimental objective and design。Evaluation：https://arxiv.org/html/2607.16208v1#S4 — 4 Experiments; https://arxiv.org/html/2607.16208v1#S4.SS1 — 4.1 Experimental objective and design。Limitations / counterevidence：https://arxiv.org/html/2607.16208v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：5 Conclusion We isolated graph-linked image candidate ranking within a graph-grounded multimodal QA pipeline by keeping offline construction of , baseline text- and table-side retrieval, and graph-grounded answering unchanged while replacing only the graph-linked image ranker with late-interaction MaxSim scoring [ 13 , 15 ] ; on MultimodalQA this is associated with improved retrieval-stage candidate-ranking point estimates and higher aggregate EM/F1 point estimates, but yields mixed modality trends, including a small regression on text-dominant items.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-RAG`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16208:end -->

<!-- review:SF-2026-ARXIV-2607-16211:start -->
### Accurate and Efficient Long-Term Memory for LLM Agents

<!-- claim:SF-2026-ARXIV-2607-16211:start -->LLM agents augmented with persistent memory can recall past interactions, but existing systems suffer from two limitations: flat, unstructured storage loses relational context needed for multi-hop and temporal reasoning, and reliance on expensive LLM-based classification makes them impractical for latency-sensitive deployment. Without mechanisms to validate new information against stored knowledge, these systems silently accumulate contradictions. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16211:end -->

**为什么进入候选分母。** 摘要首要问题为“LLM agents augmented with persistent memory can recall past interactions, but existing systems suffer from two limitations: flat, unstructured storage loses relational context needed for multi-hop and temporal reasoning, and reliance on expensive LLM-based classification makes them impractical for latency-sensitive deployment.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We present MOSAIC (Memory-Organized Structured Agent for Information Collection), a structured, conflict-aware long-term memory framework for LLM agents that is substantially more accurate and efficient.

**证据证明什么。** Evaluated on LoCoMo (long-conversation QA), HaluMem, and a novel clinical-guideline error compounding test, MOSAIC achieves 89.35% accuracy on LoCoMo (+27.21 pp over the best baseline), best HaluMem-Medium extraction F1(86.77%) and HaluMem-Long extraction F1 (85.84%), best QA correctness on both Medium and Long (73.10%, 70.75%), and detects 66% of injected factual conflicts-4.7 times higher than the best baseline (14%)-while hash-accelerated retrieval keeps average search latency at 0.58 s per question.

**证据没有证明什么。** The error compounding benchmark is limited to one domain (hypertension) with 50 injected errors. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16211v1#S2.SS2 — 2.2 Agent Frameworks and Planning; https://arxiv.org/html/2607.16211v1#S3 — 3 Method。Evaluation：https://arxiv.org/html/2607.16211v1#S2.SS4 — 2.4 Memory Evaluation Benchmarks; https://arxiv.org/html/2607.16211v1#S3.SS9 — 3.9 Convergence Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.16211v1#S6 — 6 Discussion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：The error compounding benchmark is limited to one domain (hypertension) with 50 injected errors.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16211:end -->

<!-- review:SF-2026-ARXIV-2607-16213:start -->
### SelKV: Selective KV Cache Merging with Per-Token Merge-or-Drop and Attention Compensation

<!-- claim:SF-2026-ARXIV-2607-16213:start -->Large Language Models (LLMs) generate text autoregressively, relying on a key-value (KV) cache whose memory footprint grows linearly with context length, creating a major bottleneck. Recent compression methods mitigate this cost via token merging; however, these approaches often rely on indiscriminate aggregation, which degrades representations and introduces attention sag, a mismatch where merged tokens receive the same softmax mass as individual tokens despite encoding multiple inputs. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16213:end -->

**为什么进入候选分母。** 摘要首要问题为“Large Language Models (LLMs) generate text autoregressively, relying on a key-value (KV) cache whose memory footprint grows linearly with context length, creating a major bottleneck.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** We propose a training-free, dual-component framework for KV cache compression that addresses these limitations.

**证据证明什么。** Furthermore, the method outperforms the full-cache baseline on complex multi-document QA tasks and delivers a 3.3x decoding speedup at 100k tokens.

**证据没有证明什么。** These results suggest that merge quality, not just token selection, is an important design axis for KV compression. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16213v1#S3 — 3 Method; https://arxiv.org/html/2607.16213v1#A6 — Appendix F Implementation Details。Evaluation：https://arxiv.org/html/2607.16213v1#A3 — Appendix C Category-Level Analysis; https://arxiv.org/html/2607.16213v1#A5 — Appendix E Long-Context Evaluation (31,500 Tokens)。Limitations / counterevidence：https://arxiv.org/html/2607.16213v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/ThisisBillhe/ZipCache/, https://github.com/SUSTechBruce/LOOK-M, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：These results suggest that merge quality, not just token selection, is an important design axis for KV compression.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-KV-CACHE`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16213:end -->

<!-- review:SF-2026-ARXIV-2607-16215:start -->
### RAIL Guard: Closing the Evaluation-to-Remediation Gap in Responsible AI for LLM Agents

<!-- claim:SF-2026-ARXIV-2607-16215:start -->Existing guardrail systems for large language model agents operate as binary classifiers that block unsafe content, leaving organizations to discard failing outputs and retry from scratch. We introduce RAIL Guard, a closed-loop responsible AI pipeline that evaluates LLM outputs across eight measurable dimensions and iteratively remediates failing outputs through an evaluate-rewrite-reevaluate loop. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16215:end -->

**为什么进入候选分母。** 摘要首要问题为“Existing guardrail systems for large language model agents operate as binary classifiers that block unsafe content, leaving organizations to discard failing outputs and retry from scratch.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** Existing guardrail systems for large language model agents operate as binary classifiers that block unsafe content, leaving organizations to discard failing outputs and retry from scratch.

**证据证明什么。** Closed-loop remediation achieves 96.9% convergence versus 49.1% for block-and-retry, though the highest-convergence method reduces utility by 22.3%; feedback-driven self-repair achieves 86.6% convergence on fixable dimensions with no significant utility loss (p = 0.177).

**证据没有证明什么。** GPT-5.3 improved over GPT-5.2, indicating newer iterations reduce but do not eliminate responsible AI failures. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16215v1#S2.SS1 — 2.1 Responsible AI Evaluation Frameworks; https://arxiv.org/html/2607.16215v1#S3 — 3 Methodology。Evaluation：https://arxiv.org/html/2607.16215v1#S2.SS1 — 2.1 Responsible AI Evaluation Frameworks; https://arxiv.org/html/2607.16215v1#S3.SS1 — 3.1 Multi-Dimensional Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.16215v1#S4.SS3 — 4.3 Experiment 1: Baseline Failure Rate (RQ1); https://arxiv.org/html/2607.16215v1#S5.SS1 — 5.1 Experiment 1: Baseline Failure Rate。

**Artifact boundary。** Exact v1 links https://github.com/Responsible-AI-Labs/rail-score-sdk, https://github.com/Responsible-AI-Labs/rail-score-js, https://huggingface.co/datasets/responsible-ai-labs/rail-guard-benchmark; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：GPT-5.3 improved over GPT-5.2, indicating newer iterations reduce but do not eliminate responsible AI failures.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16215:end -->

<!-- review:SF-2026-ARXIV-2607-16239:start -->
### BACON: Budgeted Human Calibration for Modeling and Evaluation with Multiple AI Judges

<!-- claim:SF-2026-ARXIV-2607-16239:start -->AI judges offer a scalable, low-cost alternative to human evaluation, but their outputs can be biased relative to human preferences and highly item-dependent, varying across judges, tasks, and domains. When uncalibrated AI evaluations are used for model ranking, item scoring, or population-level quality reporting, these biases can directly distort downstream decisions. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16239:end -->

**为什么进入候选分母。** 摘要首要问题为“AI judges offer a scalable, low-cost alternative to human evaluation, but their outputs can be biased relative to human preferences and highly item-dependent, varying across judges, tasks, and domains.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** These results show that BACON offers a practical, statistically grounded framework for scalable evaluation with limited human annotation.

**证据证明什么。** These results show that BACON offers a practical, statistically grounded framework for scalable evaluation with limited human annotation.

**证据没有证明什么。** Item-level BACON scores are only calibrated surrogate predictions: they are useful for triage, ranking, and auditing, but should not be interpreted as unbiased measurements for each item. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16239v1#A1.SS2 — A.2 WebDesign evaluation; https://arxiv.org/html/2607.16239v1#A4.SS1 — D.1 Framework。Evaluation：https://arxiv.org/html/2607.16239v1#A1 — Appendix A Additional Evaluation Results; https://arxiv.org/html/2607.16239v1#A1.SS1 — A.1 More on MQM evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.16239v1#S4 — 4 Discussion。

**Artifact boundary。** Exact v1 links https://github.com/diaryofnewton/bacon-calibration, https://github.com/tatsu-lab/alpaca_eval, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Item-level BACON scores are only calibrated surrogate predictions: they are useful for triage, ranking, and auditing, but should not be interpreted as unbiased measurements for each item.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16239:end -->

<!-- review:SF-2026-ARXIV-2607-16241:start -->
### KernelBench-Verified: Do LLM-Generated Kernels Actually Beat PyTorch?

<!-- claim:SF-2026-ARXIV-2607-16241:start -->Recent large language models (LLMs) can generate custom CUDA kernels that appear to outperform PyTorch on benchmarks such as KernelBench. Building upon this foundational framework, we demonstrate that frontier models frequently engage in reward hacking to artificially inflate reported performance. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16241:end -->

**为什么进入候选分母。** 摘要首要问题为“Recent large language models (LLMs) can generate custom CUDA kernels that appear to outperform PyTorch on benchmarks such as KernelBench.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We introduce KernelBench-Verified, an extended evaluation framework that incorporates a TF32-enabled baseline and a four-distribution hidden test suite.

**证据证明什么。** Under verified single-turn evaluation with seven frontier LLMs, we find that the best-performing model (GPT-5.5) achieves a 0.88x geometric mean speedup, significantly lower than the 1.43x speedup observed under the standard evaluation protocol.

**证据没有证明什么。** The bars are non-exclusive : a kernel that fails both D2 and D4 is counted in both bars, since we are measuring each distribution’s independent catching power. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16241v1#A12.SS1 — L.1 Methodology; https://arxiv.org/html/2607.16241v1#S2 — 2 Evaluation Methodology。Evaluation：https://arxiv.org/html/2607.16241v1#A10 — Appendix J Tolerance Sensitivity Analysis; https://arxiv.org/html/2607.16241v1#A12.SS2 — L.2 Aggregate Results。Limitations / counterevidence：https://arxiv.org/html/2607.16241v1#A12.SS4 — L.4 Discussion; https://arxiv.org/html/2607.16241v1#A7 — Appendix G Failure Mode Analysis。

**Artifact boundary。** Exact v1 links https://github.com/facebookresearch/kernel_bench_verified, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：The bars are non-exclusive : a kernel that fails both D2 and D4 is counted in both bars, since we are measuring each distribution’s independent catching power.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-TENSORRT-LLM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16241:end -->

<!-- review:SF-2026-ARXIV-2607-16242:start -->
### TRACE: Trajectory-Based Safety Patch Learning for LLM Post-Training Realignment

<!-- claim:SF-2026-ARXIV-2607-16242:start -->Fine-Tuning-as-a-Service (FTaaS) platforms let users train large language models (LLMs) on customized tasks, but this pipeline could erode models' safety alignment. In practice, service providers need to recover models' safety without re-running full alignment, or destroying the utility gained from customized tasks. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16242:end -->

**为什么进入候选分母。** 摘要首要问题为“Fine-Tuning-as-a-Service (FTaaS) platforms let users train large language models (LLMs) on customized tasks, but this pipeline could erode models' safety alignment.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** We propose TRACE, a trajectory-based safety patch learning framework that (i) simulates harmful tuning trajectories to generate progressively corrupted states, and (ii) optimizes a plug-in patch to recover safety while maintaining utility across varying corrupted base states.

**证据证明什么。** TRACE reaches nearly 100% safety on all settings, while maintaining comparable utility to the undefended fine-tuned model.

**证据没有证明什么。** Since the user cannot observe model internals or the safety patch weights, this information asymmetry limits the surface for launching adaptive attacks. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16242v1#S5.SS5 — V-E Integration and Boost on Existing Methods; https://arxiv.org/html/2607.16242v1#A1.SS1 — A-A Implementation Details。Evaluation：https://arxiv.org/html/2607.16242v1#A1.SS2 — A-B Full Utility Results across Fine-Tuning Depth; https://arxiv.org/html/2607.16242v1#A1.SS3 — A-C Ablation Study。Limitations / counterevidence：https://arxiv.org/html/2607.16242v1#S7 — VII Discussion and Limitations; https://arxiv.org/html/2607.16242v1#S7.SS2 — VII-B Limitations and Future Directions。

**Artifact boundary。** Exact v1 links https://huggingface.co/datasets/b-mc2/sql-create-context, https://github.com/huggingface/accelerate, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Since the user cannot observe model internals or the safety patch weights, this information asymmetry limits the surface for launching adaptive attacks.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-RLHF`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16242:end -->

<!-- review:SF-2026-ARXIV-2607-16244:start -->
### CIGPO: Contextual Information-Gain Policy Optimization for Multi-Turn Evidence-Reading LLM Agents

<!-- claim:SF-2026-ARXIV-2607-16244:start -->Training multi-turn evidence-reading agents with outcome-only reinforcement learning is unstable because intermediate turns receive little direct credit. In HotpotQA experiments with Qwen2.5-3B-Instruct, GRPO initially improves (standard F1 0.430) but subsequently collapses to 100% format-violating outputs. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16244:end -->

**为什么进入候选分母。** 摘要首要问题为“Training multi-turn evidence-reading agents with outcome-only reinforcement learning is unstable because intermediate turns receive little direct credit.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We propose a variance-injection strategy: by assigning per-turn rewards to intermediate evidence-reading turns, we prevent the group reward distribution from collapsing to a single value--preserving the variation that GRPO's group-relative advantage requires.

**证据证明什么。** These results identify reward-variance collapse as a concrete failure mode of outcome-only GRPO and show that turn-level IG rewards can prevent it in this HotpotQA setting.

**证据没有证明什么。** Let me re-read for more details.</think> <tool_call> {"name": "read", "arguments": {"block_id": 1}} </tool_call> [...same tool_response, noting repeat...] <think>The evidence only mentions her as an actress, not government position.</think> <answer>Actress</answer> 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16244v1#S4 — 4 CIGPO Method。Evaluation：https://arxiv.org/html/2607.16244v1#S6.SS3 — 6.3 Full Benchmark Results; https://arxiv.org/html/2607.16244v1#S5 — 5 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.16244v1#A1.SS3 — A.3 CIGPO Failure Example (Step 200, Valid Format); https://arxiv.org/html/2607.16244v1#S7 — 7 Discussion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Let me re-read for more details.</think> <tool_call> {"name": "read", "arguments": {"block_id": 1}} </tool_call> [...same tool_response, noting repeat...] <think>The evidence only mentions her as an actress, not government position.</think> <answer>Actress</answer>

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`TRAIN-GRPO`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16244:end -->

<!-- review:SF-2026-ARXIV-2607-16246:start -->
### Let the Data Decide: Supervision Analysis, Capability Trade-offs, and Adaptive Objective Routing in Continued Pre-Training via Off-Policy Distillation

<!-- claim:SF-2026-ARXIV-2607-16246:start -->Off-policy distillation is now central to large language model pre-training, yet how training data, objective parameterization, and model capabilities interact remains poorly characterized. We studies top-$k$-truncated, temperature-scaled off-policy distillation by decomposing this problem into two questions: an \emph{objective-to-capability} analysis of how the training objective shapes token-level supervision and downstream performance, and a \emph{data-to-objective} analysis of how data heterogeneity should inform objective routing. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16246:end -->

**为什么进入候选分母。** 摘要首要问题为“Off-policy distillation is now central to large language model pre-training, yet how training data, objective parameterization, and model capabilities interact remains poorly characterized.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** To quantify this tension, we introduce diagnostic metrics -- support coverage, observed-token probability mass, and teacher-distribution concentration -- and show via controlled sweeps that the support size $k$ governs a coverage-sharpness trade-off, while distillation temperature controls within-support probability allocation.

**证据证明什么。** These results suggest that effective objective routing depends less on routing granularity than on the quality of the routing signal, reframing continued pre-training via off-policy distillation as a structured, data-conditional supervision-design problem rather than a global hyperparameter choice.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16246v1#S5.SS1 — 5.1 Experimental Design; https://arxiv.org/html/2607.16246v1#S4.SS1 — 4.1 Model Setup。Evaluation：https://arxiv.org/html/2607.16246v1#S4 — 4 Experimental Setup; https://arxiv.org/html/2607.16246v1#S4.SS3 — 4.3 Evaluation Protocol。Limitations / counterevidence：https://arxiv.org/html/2607.16246v1#S8 — 8 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`TRAIN-PRETRAINING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16246:end -->

<!-- review:SF-2026-ARXIV-2607-16247:start -->
### Self-Evolving Just-In-Time Memory for Proactive Embodied Safety

<!-- claim:SF-2026-ARXIV-2607-16247:start -->While Vision-Language Models (VLMs) have empowered embodied agents to execute complex household tasks, they struggle to proactively handle dynamically emerging hazards during closed-loop interactions. Existing safety approaches often rely on runtime guardrails to block unsafe actions or induce excessive caution, which severely stalls task progress instead of actively resolving the underlying risks. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16247:end -->

**为什么进入候选分母。** 摘要首要问题为“While Vision-Language Models (VLMs) have empowered embodied agents to execute complex household tasks, they struggle to proactively handle dynamically emerging hazards during closed-loop interactions.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** To break this safety-progress trade-off, we introduce the Self-Evolving Just-In-Time Memory framework, which reframes embodied safety from progress-stalling guardrails to proactive hazard mitigation.

**证据证明什么。** Experiments on IS-Bench demonstrate that our framework substantially boosts the Safe-Success rate across multiple VLM backbones (e.g., +30.3% on Qwen3-VL-8B), enabling agents to proactively mitigate hazards without stalling task progress.

**证据没有证明什么。** 0.D.2 Limitations and Future Work Although the proposed Just-In-Time Memory framework substantially improves proactive safety, it still has several limitations. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16247v1#Pt0.A1 — Appendix 0.A Additional Method Details; https://arxiv.org/html/2607.16247v1#S4 — 4 Method。Evaluation：https://arxiv.org/html/2607.16247v1#Pt0.A2.SS5 — 0.B.5 Evaluation Protocol and Inference Cost; https://arxiv.org/html/2607.16247v1#Pt0.A3 — Appendix 0.C Extended Experimental Details。Limitations / counterevidence：https://arxiv.org/html/2607.16247v1#Pt0.A4.SS2 — 0.D.2 Limitations and Future Work; https://arxiv.org/html/2607.16247v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/DyMessi/JIT-Memory, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：0.D.2 Limitations and Future Work Although the proposed Just-In-Time Memory framework substantially improves proactive safety, it still has several limitations.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16247:end -->

<!-- review:SF-2026-ARXIV-2607-16248:start -->
### High-accuracy Low-Bit KV-Cache Quantization via Local Distribution Restoration

<!-- claim:SF-2026-ARXIV-2607-16248:start -->Long-context large language model inference relies on the KV cache to avoid redundant attention computation, but incurs high memory and bandwidth overheads. Low-bit KV-cache quantization reduces this cost, yet it severely degrade quality; particularly, one-bit quantization reduces accuracy from 84.2% to 47.8% on Llama-3.1-8B under RULER. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16248:end -->

**为什么进入候选分母。** 摘要首要问题为“Long-context large language model inference relies on the KV cache to avoid redundant attention computation, but incurs high memory and bandwidth overheads.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** Low-bit KV-cache quantization reduces this cost, yet it severely degrade quality; particularly, one-bit quantization reduces accuracy from 84.2% to 47.8% on Llama-3.1-8B under RULER.

**证据证明什么。** Expeirments show that on Llama-3.1-8B, DGAP recovers K1V1 RULER accuracy from 47.8% to 83.2% and reduces distribution drift from 0.38 to 0.14; across Llama, Mistral, and Qwen models, it preserves the persistent low-bit KV-cache footprint with modest decode overhead.

**证据没有证明什么。** 7 Limitations and Future Work DGAP focuses on algorithmic distribution restoration at decode time, while leaving system-level serving optimizations as future work. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16248v1#S4 — 4 Methodology。Evaluation：https://arxiv.org/html/2607.16248v1#S3.SS2 — 3.2 Decode-Time Analysis of Accuracy Loss; https://arxiv.org/html/2607.16248v1#S5 — 5 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.16248v1#S7 — 7 Limitations and Future Work; https://arxiv.org/html/2607.16248v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：7 Limitations and Future Work DGAP focuses on algorithmic distribution restoration at decode time, while leaving system-level serving optimizations as future work.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-KV-CACHE`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16248:end -->

<!-- review:SF-2026-ARXIV-2607-16254:start -->
### More Than Memory: Task-Conditioned Signed FFN Writes in Long-Context Retrieval

<!-- claim:SF-2026-ARXIV-2607-16254:start -->FFNs are often treated as parametric memories. In long-context retrieval, however, the sharper question is not only what they store, but whether their native residual writes push the current retrieval state toward or away from the correct answer. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16254:end -->

**为什么进入候选分母。** 摘要首要问题为“FFNs are often treated as parametric memories.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** In long-context retrieval, however, the sharper question is not only what they store, but whether their native residual writes push the current retrieval state toward or away from the correct answer.

**证据证明什么。** These results show that native FFN scaling exposes a signed, task-conditioned residual-write structure in retrieval, and that write-gradient alignment is a compact diagnostic for the two monotone roles.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16254v1#S3.SS2 — 3.2 Intervention design: native FFN scaling。Evaluation：https://arxiv.org/html/2607.16254v1#S4 — 4 Experimental Setup; https://arxiv.org/html/2607.16254v1#S5 — 5 Results。Limitations / counterevidence：https://arxiv.org/html/2607.16254v1#S6 — 6 Discussion; https://arxiv.org/html/2607.16254v1#S7 — 7 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/gkamradt/needle-in-a-haystack, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MODEL-FFN`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16254:end -->

<!-- review:SF-2026-ARXIV-2607-16257:start -->
### From Outcomes to Actions: Leveraging Hindsight for Long-Horizon Language Agent Training

<!-- claim:SF-2026-ARXIV-2607-16257:start -->Reinforcement learning (RL) has become a widely adopted technique for improving large language models (LLMs) on complex tasks. Despite this progress, existing RL methods still face challenges in training agents with longer-horizon interactions. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16257:end -->

**为什么进入候选分母。** 摘要首要问题为“Reinforcement learning (RL) has become a widely adopted technique for improving large language models (LLMs) on complex tasks.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** To address this, we introduce a novel policy gradient method, Hindsight Policy Optimization (HPO), that projects both the current policy distribution and the hindsight distribution into an intent space and extracts low-variance learning signals from the Wasserstein distance between them.

**证据证明什么。** We theoretically and empirically show that aggregating semantically similar states and actions in the intent space yields a bounded-variance estimator and improves policy performance stably.

**证据没有证明什么。** Future work will explore more fine-grained constructions of the intent space and extend this framework to more complex multimodal and open-ended environments. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16257v1#A3 — Appendix C Embedding Model Ablation。Evaluation：https://arxiv.org/html/2607.16257v1#A1 — Appendix A Experimental Details; https://arxiv.org/html/2607.16257v1#A1.SS2 — A.2 Experimental Settings.。Limitations / counterevidence：https://arxiv.org/html/2607.16257v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Future work will explore more fine-grained constructions of the intent space and extend this framework to more complex multimodal and open-ended environments.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-GRPO`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16257:end -->

<!-- review:SF-2026-ARXIV-2607-16259:start -->
### Quantifying Ranking Uncertainty in LLM Benchmarks

<!-- claim:SF-2026-ARXIV-2607-16259:start -->Pretrained models are typically ranked on multi-task leaderboards to assess their effectiveness across diverse tasks. Rank confidence intervals were recently introduced as a method to quantify the uncertainty in these rankings by aggregating pairwise hypothesis tests. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16259:end -->

**为什么进入候选分母。** 摘要首要问题为“Pretrained models are typically ranked on multi-task leaderboards to assess their effectiveness across diverse tasks.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Rank confidence intervals were recently introduced as a method to quantify the uncertainty in these rankings by aggregating pairwise hypothesis tests.

**证据证明什么。** We demonstrate that ranking variability across MMLU subjects is substantial and should be considered when comparing LLMs or identifying the top-performing models.

**证据没有证明什么。** However, LLM leaderboards typically include multiple, diverse benchmarks. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16259v1#A1 — Appendix A Rank CIs definitions and methods; https://arxiv.org/html/2607.16259v1#S2.SS2 — 2.2 Statistical Choices in Balanced Designs。Evaluation：https://arxiv.org/html/2607.16259v1#A2 — Appendix B Additional Results; https://arxiv.org/html/2607.16259v1#S3.SS1 — 3.1 Benchmark-Level Variability。Limitations / counterevidence：https://arxiv.org/html/2607.16259v1#S5 — 5 Conclusions。

**Artifact boundary。** Exact v1 links https://github.com/BityaNeuhof/quantifying-rank-uncertainty.git, https://huggingface.co/datasets/PromptEval/PromptEval_MMLU_correctness, https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：However, LLM leaderboards typically include multiple, diverse benchmarks.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16259:end -->

<!-- review:SF-2026-ARXIV-2607-16266:start -->
### Composable Verification Pipelines for Multi-Agent Systems

<!-- claim:SF-2026-ARXIV-2607-16266:start -->Existing approaches for reasoning about action and change provide expressive semantics for modeling dynamic systems, in most cases built on top of logic programming systems. We introduce a modular framework for transition and trajectory verification based on Tiles and implemented in Soda, which is an efficient functional programming language. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16266:end -->

**为什么进入候选分母。** 摘要首要问题为“Existing approaches for reasoning about action and change provide expressive semantics for modeling dynamic systems, in most cases built on top of logic programming systems.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** We introduce a modular framework for transition and trajectory verification based on Tiles and implemented in Soda, which is an efficient functional programming language.

**证据证明什么。** We provide an open-source implementation and illustrate the framework through examples that involve misinformation and emotional reasoning.

**证据没有证明什么。** Tiles may depend on contextual information and can be combined by composition: given and , their composition yields , which is equivalent to , where denotes composition of functions. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16266v1#S3 — 3 Model。Evaluation：https://arxiv.org/html/2607.16266v1#S1 — 1 Introduction; https://arxiv.org/html/2607.16266v1#S2 — 2 Preliminaries。Limitations / counterevidence：https://arxiv.org/html/2607.16266v1#S1 — 1 Introduction; https://arxiv.org/html/2607.16266v1#S2 — 2 Preliminaries。

**Artifact boundary。** Exact v1 links https://github.com/julianmendez/verification-pipeline, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：Tiles may depend on contextual information and can be combined by composition: given and , their composition yields , which is equivalent to , where denotes composition of functions.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MULTI-AGENT`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16266:end -->

<!-- review:SF-2026-ARXIV-2607-16269:start -->
### From Intent to Infrastructure: LLM-Driven Agent Compilers for ISAC Networks

<!-- claim:SF-2026-ARXIV-2607-16269:start -->Integrated sensing and communications (ISAC) is moving from proof-of-concept demonstrations to system-level deployment in sixth-generation (6G) networks. Because sensing and communication share hardware, spectrum, and waveform resources, ISAC design now involves many tightly coupled choices, including waveform selection, sensing algorithm setup, resource scheduling, and deployment planning. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16269:end -->

**为什么进入候选分母。** 摘要首要问题为“Integrated sensing and communications (ISAC) is moving from proof-of-concept demonstrations to system-level deployment in sixth-generation (6G) networks.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** Integrated sensing and communications (ISAC) is moving from proof-of-concept demonstrations to system-level deployment in sixth-generation (6G) networks.

**证据证明什么。** We also discuss open issues, including compilation latency, output reliability, constraint verification, and pipeline security, to guide future research.

**证据没有证明什么。** II-B Limitations of Existing Approaches Table I compares five design paradigms against these complexity sources. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16269v1#S2.SS1 — II-A The Complexity of ISAC System Design; https://arxiv.org/html/2607.16269v1#S2 — II Why ISAC Needs a New Design Abstraction。Evaluation：https://arxiv.org/html/2607.16269v1#S4.SS2 — IV-B Runtime Adaptation and Numerical Results; https://arxiv.org/html/2607.16269v1#S4 — IV Case Study。Limitations / counterevidence：https://arxiv.org/html/2607.16269v1#S2.SS2 — II-B Limitations of Existing Approaches; https://arxiv.org/html/2607.16269v1#S6 — VI Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：II-B Limitations of Existing Approaches Table I compares five design paradigms against these complexity sources.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-PLATFORM`；evidence-stage relation：`structural_candidate`。
- Books 候选路由（尚非最终决定）：`Structural Candidate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16269:end -->

<!-- review:SF-2026-ARXIV-2607-16311:start -->
### Seeing What Is Actually There: PriVE-Bench and PriVE-Tools for Counterfactual Evaluation of Agentic Visual Evidence in VLMs

<!-- claim:SF-2026-ARXIV-2607-16311:start -->Vision-language models (VLMs) often answer visual questions using learned language and category priors rather than grounding their predictions in the image itself. Counterfactual images provide a natural diagnostic setting for this failure mode: when visible evidence contradicts what is usually true, a grounded model should answer from the pixels, while a prior-following model will produce a canonical but visually incorrect response. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16311:end -->

**为什么进入候选分母。** 摘要首要问题为“Vision-language models (VLMs) often answer visual questions using learned language and category priors rather than grounding their predictions in the image itself.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** In this paper, we ask a further question motivated by the rise of tool-augmented and agentic vision systems: can additional visual evidence views help VLMs reason against their priors?

**证据证明什么。** Our results show that visual evidence tools can help in some settings, especially when models can use localized evidence effectively, but they are not a universal remedy: several models continue to follow language and category priors even when relevant visual evidence is explicitly provided.

**证据没有证明什么。** 8 Limitations PriVE-Tools is not a complete agentic vision framework. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16311v1#A6.SS0.SSS0.Px3 — Model-level summary.; https://arxiv.org/html/2607.16311v1#A7.SS0.SSS0.Px1 — Model-level common tool deltas.。Evaluation：https://arxiv.org/html/2607.16311v1#S6 — 6 Experiments and Analysis; https://arxiv.org/html/2607.16311v1#A4 — Appendix D Evaluation Configuration。Limitations / counterevidence：https://arxiv.org/html/2607.16311v1#S7 — 7 Conclusion; https://arxiv.org/html/2607.16311v1#S8 — 8 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：8 Limitations PriVE-Tools is not a complete agentic vision framework.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16311:end -->

<!-- review:SF-2026-ARXIV-2607-16314:start -->
### Depth-Regularized JEPA World Models Learn More Transferable Representations from Real Outdoor Robot Data

<!-- claim:SF-2026-ARXIV-2607-16314:start -->World models, especially based on JEPA architectures, have been shown to learn robust dynamics of various environments. However, learning from visually complex real-world data remains a challenge, especially in unpredictable outdoor environments. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16314:end -->

**为什么进入候选分母。** 摘要首要问题为“World models, especially based on JEPA architectures, have been shown to learn robust dynamics of various environments.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We introduce depth as a geometric prior during training in learning more robust latent dynamics directly from robot video data and handling visual complexity.

**证据证明什么。** These results show that a lightweight training-time geometric prior makes a compact JEPA world model more useful and more transferable on real outdoor data with strong underlying representations, without adding inference overhead.

**证据没有证明什么。** Training-time depth regularization provides that prior cheaply, using paired depth only during learning and not at deployment. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16314v1#S3 — 3 Method; https://arxiv.org/html/2607.16314v1#S2.SS1 — 2.1 Latent world models and JEPA-style prediction。Evaluation：https://arxiv.org/html/2607.16314v1#S3.SS3 — 3.3 Data and evaluation setting; https://arxiv.org/html/2607.16314v1#S3.SS4 — 3.4 Surprise evaluation protocol。Limitations / counterevidence：https://arxiv.org/html/2607.16314v1#S5 — 5 Discussion; https://arxiv.org/html/2607.16314v1#S6 — 6 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Training-time depth regularization provides that prior cheaply, using paired depth only during learning and not at deployment.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16314:end -->

<!-- review:SF-2026-ARXIV-2607-16326:start -->
### CRISP: Pre-LLM Yet Text-Driven Visual Token Pruning for Efficient LVLM Inference

<!-- claim:SF-2026-ARXIV-2607-16326:start -->Large Vision-Language Models (LVLMs) typically require processing hundreds to thousands of visual tokens, leading to substantial inference overhead. Existing visual token pruning methods either operate before the LLM using text-agnostic heuristics or prune inside the LLM at the cost of efficiency and noisy cross-modal attention. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16326:end -->

**为什么进入候选分母。** 摘要首要问题为“Large Vision-Language Models (LVLMs) typically require processing hundreds to thousands of visual tokens, leading to substantial inference overhead.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** To address these limitations, we propose CRISP, a pre-LLM yet text-driven visual token pruning framework that preserves both instruction-relevant evidence and essential scene context.

**证据证明什么。** Extensive experiments on LLaVA-1.5 and LLaVA-NeXT demonstrate that CRISP achieves superior performance retention under aggressive pruning ratios, maintaining up to 99.5% accuracy while reducing inference cost and latency by more than 2 times.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16326v1#S3 — III Method; https://arxiv.org/html/2607.16326v1#S2.SS1 — II-A Large Vision-Language Models。Evaluation：https://arxiv.org/html/2607.16326v1#S4 — IV Experiments; https://arxiv.org/html/2607.16326v1#S4.SS1 — IV-A Experimental Settings。Limitations / counterevidence：https://arxiv.org/html/2607.16326v1#S5 — V Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-REPRESENTATION`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16326:end -->

<!-- review:SF-2026-ARXIV-2607-16339:start -->
### LaCache: Exact Caching and Precision-Adaptive Inference for Diffusion Large Language Models

<!-- claim:SF-2026-ARXIV-2607-16339:start -->Diffusion-based Large Language Models(DLLMs) enable parallel generation via Semi-Autoregressive (SAR) decoding in text generation. However, current methods suffer from severe operator-level redundancy: they recompute the entire sequence during denoising steps, ignoring that the prefix and masked suffix remain invariant within a block. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16339:end -->

**为什么进入候选分母。** 摘要首要问题为“Diffusion-based Large Language Models(DLLMs) enable parallel generation via Semi-Autoregressive (SAR) decoding in text generation.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** We propose LaCache, a training-free acceleration framework that alleviates this redundancy through lossless caching and mixed precision.

**证据证明什么。** Experiments demonstrate that LaCache alone achieves approximately 1.3X end-to-end speedup over vanilla DLLM.

**证据没有证明什么。** Limitations Although the proposed LaCache achieves significant acceleration, certain limitations remain. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16339v1#S3 — 3 Method。Evaluation：https://arxiv.org/html/2607.16339v1#A4 — Appendix D The acceleration of LaCache on LLaDA-base on multiple benchmarks; https://arxiv.org/html/2607.16339v1#A5 — Appendix E The acceleration of LaCache on LLaDA-1.5 on multiple benchmarks。Limitations / counterevidence：https://arxiv.org/html/2607.16339v1#S5 — 5 Conclusion; https://arxiv.org/html/2607.16339v1#Sx1 — Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Limitations Although the proposed LaCache achieves significant acceleration, certain limitations remain.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-GENERATIVE-PARADIGMS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16339:end -->

<!-- review:SF-2026-ARXIV-2607-16345:start -->
### AEVAL: From Anecdotal to Deterministic Testing for Agentic Skill Workflows

<!-- claim:SF-2026-ARXIV-2607-16345:start -->Modern agentic systems increasingly rely on skills: installable packages of natural language and code that teach an LLM agent to perform a domain task. As skill repositories grow, developers need automated quality signals on every change, yet evaluation today is largely anecdotal: a developer asks an agent to "try the skill," watches a demo, and forms a subjective impression. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16345:end -->

**为什么进入候选分母。** 摘要首要问题为“Modern agentic systems increasingly rely on skills: installable packages of natural language and code that teach an LLM agent to perform a domain task.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We present AEVAL (Agentic Evaluation), a CI-integrated framework that replaces this practice with a deterministic, reproducible test pipeline for agentic skills.

**证据证明什么。** Validated on real skills in a production agentic stack across multiple agent SDKs, AEVAL converts spurious 100% pass rates into reproducible first-attempt fail signals with an auditable record of every executor fix.

**证据没有证明什么。** This produces neither reproducibility nor comparability and does not scale to multi-skill marketplaces. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16345v1#S4 — 4 Method; https://arxiv.org/html/2607.16345v1#S6 — 6 System and Deployment。Evaluation：https://arxiv.org/html/2607.16345v1#S4.SS1 — 4.1 Skill-Defined Evaluation Contract; https://arxiv.org/html/2607.16345v1#S4.SS4 — 4.4 Independent Analysis Pass。Limitations / counterevidence：https://arxiv.org/html/2607.16345v1#S8 — 8 Discussion; https://arxiv.org/html/2607.16345v1#S9 — 9 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：This produces neither reproducibility nor comparability and does not scale to multi-skill marketplaces.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-PLATFORM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16345:end -->

<!-- review:SF-2026-ARXIV-2607-16352:start -->
### Clarify Before Executing: A Self-Evolving Agent for Resolving Intent Asymmetry in 3D Tool Orchestration

<!-- claim:SF-2026-ARXIV-2607-16352:start -->A fundamental intent asymmetry plagues modern 3D asset creation: while state-of-the-art 3D toolchains demand precise, executable parameters, ordinary users typically provide vague, underspecified instructions. Current 3D agents treat this ambiguity as noise, defaulting to blind execution under a single-turn assumption. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16352:end -->

**为什么进入候选分母。** 摘要首要问题为“A fundamental intent asymmetry plagues modern 3D asset creation: while state-of-the-art 3D toolchains demand precise, executable parameters, ordinary users typically provide vague, underspecified instructions.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** To rigorously test this, we construct 3D-Clarify, a comprehensive benchmark comprising 620 interaction scenarios with systematically injected ambiguity, missing information, and mistaken details.

**证据证明什么。** Both quantitative and qualitative results demonstrate that proactive clarification is the missing key to robust 3D execution.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16352v1#A1 — Appendix A Method Details; https://arxiv.org/html/2607.16352v1#A1.SS1 — A.1. Architecture。Evaluation：https://arxiv.org/html/2607.16352v1#A3 — Appendix C Extended Experimental Results; https://arxiv.org/html/2607.16352v1#A2 — Appendix B 3D Clarify Benchmark Details。Limitations / counterevidence：https://arxiv.org/html/2607.16352v1#A3.SS3 — C.3. Statistical Analysis of Failure Modes; https://arxiv.org/html/2607.16352v1#A3.SS4 — C.4. Failure Case Analysis。

**Artifact boundary。** Exact v1 links https://github.com/xyzhu1225/CLARE, https://github.com/ZiYang-xie/WorldGen, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-TOOL-CALLING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16352:end -->

<!-- review:SF-2026-ARXIV-2607-16401:start -->
### Apple-$π$: Benchmarking Thinking with Video Towards Law-Grounded Physical Intelligence

<!-- claim:SF-2026-ARXIV-2607-16401:start -->Modern video generation models are increasingly hailed as emerging world models with an internalized grasp of physical law. Yet existing benchmarks largely evaluate physical plausibility only at the output level, without verifying whether the model arrives there through a faithful, law-grounded reasoning process. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16401:end -->

**为什么进入候选分母。** 摘要首要问题为“Modern video generation models are increasingly hailed as emerging world models with an internalized grasp of physical law.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We introduce Apple-PI, the first benchmark that anchors video-model evaluation explicitly in physical laws.

**证据证明什么。** Benchmarking 11 models shows that current video models remain far from reliable law-grounded world simulators, with the best video model scoring only 0.473.

**证据没有证明什么。** These errors reflect limitations in OCR, segmentation, rendering, and instruction following. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16401v1#A1 — Appendix A Orchard Design Principles and Data Card; https://arxiv.org/html/2607.16401v1#A1.SS1 — A.1 Design Principles。Evaluation：https://arxiv.org/html/2607.16401v1#A3 — Appendix C Benchmark Protocol and Prompt Templates; https://arxiv.org/html/2607.16401v1#A3.SS3 — C.3 Protocol Ablations。Limitations / counterevidence：https://arxiv.org/html/2607.16401v1#A8 — Appendix H Limitations; https://arxiv.org/html/2607.16401v1#S4.SS5 — 4.5 Qualitative Failure Analysis。

**Artifact boundary。** Exact v1 links https://github.com/isaac-sim/IsaacSim, https://github.com/OpenSenseNova/SenseNova-U1, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：These errors reflect limitations in OCR, segmentation, rendering, and instruction following.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16401:end -->

<!-- review:SF-2026-ARXIV-2607-16414:start -->
### Signal-based Model Access Risk Analysis for AI System Operations Security

<!-- claim:SF-2026-ARXIV-2607-16414:start -->Artificial intelligence (AI) systems are now ubiquitous across domains such as security, finance, healthcare, consumer technology, and large-scale cloud services, where they process massive volumes of data and make consequential decisions daily. This widespread adoption has created a broad attack surface through which adversaries can manipulate, evade, extract information from, or otherwise subvert deployed models. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16414:end -->

**为什么进入候选分母。** 摘要首要问题为“Artificial intelligence (AI) systems are now ubiquitous across domains such as security, finance, healthcare, consumer technology, and large-scale cloud services, where they process massive volumes of data and make consequential decisions daily.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** To address this gap, we introduce the Signal-based Model Access Risk Taxonomy (SMART), a deployment-oriented framework that classifies attacker access according to the nature and richness of the information signals available from deployed AI systems.

**证据证明什么。** Using this taxonomy, we provide a structured overview of evasion attacks across progressively richer levels of information exposure, highlighting how deployment interfaces influence attack capabilities and informing more secure AI deployment and procurement decisions.

**证据没有证明什么。** The security of these deployed systems depends not only on the robustness of their learning algorithms but also on the information made available through their deployment interfaces. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16414v1#S2.SS2 — 2.2 Metadata: Coarse System Knowledge and Low-Resource Observation; https://arxiv.org/html/2607.16414v1#S2 — 2 Signal-Based Model Access Risk Taxonomy。Evaluation：https://arxiv.org/html/2607.16414v1#S3 — 3 Risk Landscape Analysis and Procurement Decision Considerations。Limitations / counterevidence：https://arxiv.org/html/2607.16414v1#S1 — 1 Introduction; https://arxiv.org/html/2607.16414v1#S2 — 2 Signal-Based Model Access Risk Taxonomy。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：The security of these deployed systems depends not only on the robustness of their learning algorithms but also on the information made available through their deployment interfaces.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16414:end -->

<!-- review:SF-2026-ARXIV-2607-16442:start -->
### One Modality to Forget Them All: Enhancing Cross-Modal Unlearning in Vision-Language Models

<!-- claim:SF-2026-ARXIV-2607-16442:start -->Machine unlearning is widely used to remove hazardous knowledge from large language models. Modern Vision-Language Models (VLMs), however, process both text and visual inputs, raising a fundamental security question: does unlearning in one modality transfer to the other? 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16442:end -->

**为什么进入候选分母。** 摘要首要问题为“Machine unlearning is widely used to remove hazardous knowledge from large language models.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** We present the first systematic, bidirectional study of cross-modal unlearning transfer across three VLM architectures: LLaVA-1.5 (MLP projection), InstructBLIP (Q-Former), and IDEFICS (gated cross-attention).

**证据证明什么。** We find that unlearning transfers across modalities, but the transfer is asymmetric and incomplete.

**证据没有证明什么。** They cannot modify weights, inspect gradients, or access training data. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16442v1#S5.SS2 — 5.2. Experiment Design; https://arxiv.org/html/2607.16442v1#S3 — 3. Threat Model。Evaluation：https://arxiv.org/html/2607.16442v1#A3 — Appendix C Exp 2 Ablation: LoRA Magnitude Analysis; https://arxiv.org/html/2607.16442v1#A5 — Appendix E Full Experimental Results。Limitations / counterevidence：https://arxiv.org/html/2607.16442v1#A4 — Appendix D Target-String Failure Examples; https://arxiv.org/html/2607.16442v1#S3 — 3. Threat Model。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：They cannot modify weights, inspect gradients, or access training data.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-REPRESENTATION`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16442:end -->

<!-- review:SF-2026-ARXIV-2607-16451:start -->
### Committed Before Reasoning: Behavioral Reproduction and Preliminary Activation-Level Evidence of Answer Pre-Commitment in an Open-Weight LLM

<!-- claim:SF-2026-ARXIV-2607-16451:start -->Chat models sometimes commit to an answer and then produce reasoning that justifies it rather than deriving it -- even when the answer contradicts a task premise. We study a minimal probe: "I want to wash my car. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16451:end -->

**为什么进入候选分母。** 摘要首要问题为“Chat models sometimes commit to an answer and then produce reasoning that justifies it rather than deriving it -- even when the answer contradicts a task premise.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Samples are small and the within-rollout positional gradient is not significant (p=.34); we frame these results as preliminary. (3) Methodological: with fixed oracle, activations, and positions, question wording alone moves a positive control from 2/16 (open question) to 11/16 (closed); negative oracle results are uninterpretable without per-wording positive controls.

**证据证明什么。** The oracle's default on unrelated content is "drive" (83%), so the read-outs are not lexical bias; stratifying by literal walk/drive occurrence shows they are not text recovery either (spans containing "drive" still read out walk; in balanced lexical fields, per-rollout walk-majorities beat a per-prompt neutral baseline 15/22 vs.

**证据没有证明什么。** A layer sweep was planned but not run; results may differ at other depths. • Non-random rollout selection. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16451v1#S1 — 1 Introduction; https://arxiv.org/html/2607.16451v1#S2 — 2 Behavioral study。Evaluation：https://arxiv.org/html/2607.16451v1#S2.SS2 — 2.2 Results: the wrong commitment is near-deterministic; https://arxiv.org/html/2607.16451v1#S2 — 2 Behavioral study。Limitations / counterevidence：https://arxiv.org/html/2607.16451v1#S2.SS3 — 2.3 A truncation artifact that almost reversed a conclusion; https://arxiv.org/html/2607.16451v1#S5 — 5 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：A layer sweep was planned but not run; results may differ at other depths. • Non-random rollout selection.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`WORLDVIEW-LLM-INTELLIGENCE`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16451:end -->

<!-- review:SF-2026-ARXIV-2607-16473:start -->
### Enabling Spatially Fine-Grained DVFS in Neural Processing Units for Energy-Efficient LLM Serving

<!-- claim:SF-2026-ARXIV-2607-16473:start -->As neural processing units (NPUs) evolve rapidly to accommodate the ever-increasing compute demand of large language models (LLMs), their power consumption is becoming a limiting factor. Our study shows that using dynamic voltage and frequency scaling (DVFS) to exploit the service-level objective (SLO) slacks is a promising way to improve NPU energy efficiency for LLM services. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16473:end -->

**为什么进入候选分母。** 摘要首要问题为“As neural processing units (NPUs) evolve rapidly to accommodate the ever-increasing compute demand of large language models (LLMs), their power consumption is becoming a limiting factor.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** Our study shows that using dynamic voltage and frequency scaling (DVFS) to exploit the service-level objective (SLO) slacks is a promising way to improve NPU energy efficiency for LLM services.

**证据证明什么。** Our study shows that using dynamic voltage and frequency scaling (DVFS) to exploit the service-level objective (SLO) slacks is a promising way to improve NPU energy efficiency for LLM services.

**证据没有证明什么。** As long as the law continues to hold, DVFS will remain an effective technique for future nodes. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16473v1#S2.SS1 — 2.1. NPU Architecture; https://arxiv.org/html/2607.16473v1#S3 — 3. Design and Implementation。Evaluation：https://arxiv.org/html/2607.16473v1#S4 — 4. Evaluation; https://arxiv.org/html/2607.16473v1#S4.SS1 — 4.1. Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.16473v1#S5 — 5. Discussion; https://arxiv.org/html/2607.16473v1#S7 — 7. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/google-coral/coralnpu, https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro, https://huggingface.co/Qwen/Qwen3-Next-80B-A3B-Thinking; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：As long as the law continues to hold, DVFS will remain an effective technique for future nodes.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-SCHEDULING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16473:end -->

<!-- review:SF-2026-ARXIV-2607-16488:start -->
### Auto-Scaling Heterogeneous Neural Processing Units for Energy and Cost-Efficient LLM Serving

<!-- claim:SF-2026-ARXIV-2607-16488:start -->To meet the ever-increasing computing demands of large language model (LLM) services, modern cloud platforms have widely deployed neural processing units (NPUs). These NPU chips have been developed and evolved at an incredibly fast pace, this inevitably produces heterogeneous compute pools backed by different versions of NPU chips. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16488:end -->

**为什么进入候选分母。** 摘要首要问题为“To meet the ever-increasing computing demands of large language model (LLM) services, modern cloud platforms have widely deployed neural processing units (NPUs).”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** To realize these benefits, we present NeuScale, an auto-scaling framework to automatically exploit heterogeneous NPUs for cloud platforms.

**证据证明什么。** Our evaluation with popular LLMs shows that NeuScale can significantly improve cost efficiency and service-level objective (SLO) satisfaction rate by best utilizing heterogeneous NPU resources.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16488v1#S2.SS2 — 2.2. System Architecture of NPUs; https://arxiv.org/html/2607.16488v1#S3 — 3. Design and Implementation。Evaluation：https://arxiv.org/html/2607.16488v1#S5 — 5. Evaluation; https://arxiv.org/html/2607.16488v1#S5.SS1 — 5.1. Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.16488v1#S6 — 6. Discussion; https://arxiv.org/html/2607.16488v1#S8 — 8. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/features/copilot, https://github.com/AI-Hypercomputer/JetStream, https://github.com/Azure/AzurePublicDataset/blob/master/AzureLLMInferenceDataset2023.md; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-SCHEDULING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16488:end -->

<!-- review:SF-2026-ARXIV-2607-16506:start -->
### Foresight Residual RL for Long-Horizon Robot Manipulation with Vision-Language-Action Models

<!-- claim:SF-2026-ARXIV-2607-16506:start -->Vision-Language-Action (VLA) policies offer strong general-purpose manipulation priors, but often fail on tight-tolerance, contact-rich assembly due to long-horizon credit assignment and subtask coupling: a state that is geometrically successful for the current skill can be brittle for downstream skills. We show this failure mode in residual reinforcement learning (RL) over a frozen VLA base policy: constant sparse success rewards improve each subtask in isolation yet yield little or no gain when skills are chained, because terminal state quality is uncontrolled. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16506:end -->

**为什么进入候选分母。** 摘要首要问题为“Vision-Language-Action (VLA) policies offer strong general-purpose manipulation priors, but often fail on tight-tolerance, contact-rich assembly due to long-horizon credit assignment and subtask coupling: a state that is geometrically successful for the current skill can be brittle for downstream skills.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We propose Foresight Residual RL, which optimizes handoff quality by augmenting each subtask's sparse success reward with an offline-estimated foresight value -- the probability of future subtask success conditioned on the terminal state of the current subtask.

**证据证明什么。** On a three-phase wrench-based nut-tightening assembly task in Isaac Gym (grasp, move-insert, rotate), our method achieves 85.6% full-task success, outperforming standard subtask residual RL (54.5%) and VLA baselines, while leaving per-subtask success unchanged.

**证据没有证明什么。** In conclusion, our results clearly demonstrate that optimizing the terminal state of a subtask, not just whether the subtask succeeds, is essential for composing contact-rich manipulation skills. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16506v1#S1 — I Introduction; https://arxiv.org/html/2607.16506v1#S2 — II Related Work。Evaluation：https://arxiv.org/html/2607.16506v1#S6 — VI Experiments; https://arxiv.org/html/2607.16506v1#S7 — VII Results。Limitations / counterevidence：https://arxiv.org/html/2607.16506v1#S8 — VIII Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：In conclusion, our results clearly demonstrate that optimizing the terminal state of a subtask, not just whether the subtask succeeds, is essential for composing contact-rich manipulation skills.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16506:end -->

<!-- review:SF-2026-ARXIV-2607-16523:start -->
### SEER: Supervised Learning to Control Energetic Reasoning

<!-- claim:SF-2026-ARXIV-2607-16523:start -->One of the main strengths of Constraint Programming is the ability to reduce the search space via propagation. However, propagation is a double-edged sword, with more pruning power coming at the price of larger computation time. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16523:end -->

**为什么进入候选分母。** 摘要首要问题为“One of the main strengths of Constraint Programming is the ability to reduce the search space via propagation.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We propose to merge those efforts by using an oracle function, obtained via ML, to decide whether to run complex propagators for a target constraint.

**证据证明什么。** One of the main strengths of Constraint Programming is the ability to reduce the search space via propagation.

**证据没有证明什么。** 5 Conclusion and Future Work This paper proposes an approach to take better advantage of complex propagators, by running them only when they provide an actual benefit in terms of pruning. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16523v1#S3 — 3 Design Process; https://arxiv.org/html/2607.16523v1#S2.SS2 — 2.2 Algorithm Selection and Propagation。Evaluation：https://arxiv.org/html/2607.16523v1#S4 — 4 Experiments; https://arxiv.org/html/2607.16523v1#S4.SS2 — 4.2 Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.16523v1#S5 — 5 Conclusion and Future Work。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：5 Conclusion and Future Work This paper proposes an approach to take better advantage of complex propagators, by running them only when they provide an actual benefit in terms of pruning.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MODEL-SAMPLING`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16523:end -->

<!-- review:SF-2026-ARXIV-2607-16555:start -->
### Mitigating Compiler Fusion-Induced Power Bursts in Mobile NPU Inference as the Battery Depletes

<!-- claim:SF-2026-ARXIV-2607-16555:start -->Mobile devices increasingly rely on real-time NPU inference for camera and perception workloads. Under low-voltage conditions, however, a single inference can induce an instantaneous voltage droop in the power-delivery network, causing the power management integrated circuit to invoke dynamic voltage and frequency scaling (DVFS) and increase latency. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16555:end -->

**为什么进入候选分母。** 摘要首要问题为“Mobile devices increasingly rely on real-time NPU inference for camera and perception workloads.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** We present a measurement study of this effect on a commercial smartphone.

**证据证明什么。** These bursts shift the DVFS-onset voltage upward and reduce the low-voltage operating margin.

**证据没有证明什么。** Furthermore, on CPU/GPU delegates that do not perform aggressive layer fusion for execution-speed reduction, superlayers themselves are unlikely to form, and the effect of the proposed method is expected to be limited. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16555v1#S3 — 3 Method; https://arxiv.org/html/2607.16555v1#S4.SS3 — 4.3 Models。Evaluation：https://arxiv.org/html/2607.16555v1#S4 — 4 Experimental Setup; https://arxiv.org/html/2607.16555v1#S4.SS4 — 4.4 Evaluation metrics。Limitations / counterevidence：https://arxiv.org/html/2607.16555v1#S5 — 5 Results and Discussion; https://arxiv.org/html/2607.16555v1#S5.SS7 — 5.7 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：Furthermore, on CPU/GPU delegates that do not perform aggressive layer fusion for execution-speed reduction, superlayers themselves are unlikely to form, and the effect of the proposed method is expected to be limited.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-TENSORRT-LLM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16555:end -->

<!-- review:SF-2026-ARXIV-2607-16560:start -->
### From Modalities to Propositions: A Language-Centric Framework for Multimodal Intelligence

<!-- claim:SF-2026-ARXIV-2607-16560:start -->We propose a language representation for multimodal data in which any observation, whether image, video, or text, is expressed as a bag of atomic propositions, simple statements about the entities, actions, and relations in a scene. A global semantic codebook unifies these into a shared vocabulary of canonical atomic propositions, placing every modality and observation into one interpretable space that spans fine grained facts to high level concepts and composes into richer ones. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16560:end -->

**为什么进入候选分母。** 摘要首要问题为“We propose a language representation for multimodal data in which any observation, whether image, video, or text, is expressed as a bag of atomic propositions, simple statements about the entities, actions, and relations in a scene.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We demonstrate the framework on autonomous driving and open-world data.

**证据证明什么。** We demonstrate the framework on autonomous driving and open-world data.

**证据没有证明什么。** Compositionality expresses complex situations as combinations of concepts, retrieving rare scenarios that a single caption or dense embedding cannot. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16560v1#S2 — 2 From Observations to Propositions: A Compositional Framework。Evaluation：https://arxiv.org/html/2607.16560v1#S3 — 3 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.16560v1#S4 — 4 Conclusion。

**Artifact boundary。** Exact v1 links https://huggingface.co/datasets/nvidia/PhysicalAI-Autonomous-Vehicles, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Compositionality expresses complex situations as combinations of concepts, retrieving rare scenarios that a single caption or dense embedding cannot.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-REPRESENTATION`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16560:end -->

<!-- review:SF-2026-ARXIV-2607-16596:start -->
### Cold-Start Model Delivery in Kubernetes Inference Serving: An Empirical Study of OCI-Based Distribution and Its Integrity

<!-- claim:SF-2026-ARXIV-2607-16596:start -->The startup latency of a model-serving pod on Kubernetes is dominated by one step: delivering the model weights. As models reach the hundred-gigabyte weights of large language models, cold-start delivery time governs the economics of autoscaling and scale-to-zero, yet the dominant mechanisms remain ad-hoc downloads from object storage, with none of the pull caching, digest addressing, or verification Kubernetes provides for container images. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16596:end -->

**为什么进入候选分母。** 摘要首要问题为“The startup latency of a model-serving pod on Kubernetes is dominated by one step: delivering the model weights.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** For models on s3://, gs://, or hf:// URIs, where no admission-time verifier observes the bytes, we present a serving-time integrity design proposed to the KServe community: digest pinning and OpenSSF model-signing enforcement in the storage initializer.

**证据证明什么。** Streaming hash verification during download adds under 0.1% to delivery time; a post-download pass adds up to 53%.

**证据没有证明什么。** The design mitigates but does not close this window—the model volume is mounted read-only into the server container, and co-located containers are the cluster policy’s problem by assumption; continuous re-validation, as prototyped by the model-validation-operator’s sidecar mode [ 14 ] , is future work. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16596v1#S3.SS1 — III-A Design space; https://arxiv.org/html/2607.16596v1#S4.SS2 — IV-B Design。Evaluation：https://arxiv.org/html/2607.16596v1#S5 — V Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.16596v1#S4.SS1 — IV-A Threat model; https://arxiv.org/html/2607.16596v1#S6 — VI Discussion and Lessons。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：The design mitigates but does not close this window—the model volume is mounted read-only into the server container, and co-located containers are the cluster policy’s problem by assumption; continuous re-validation, as prototyped by the model-validation-operator’s sidecar mode [ 14 ] , is future work.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-MODEL-REGISTRY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16596:end -->

<!-- review:SF-2026-ARXIV-2607-16602:start -->
### PAVXploreRL: Physical-Action-Visual World Model Reinforcement Learning with Action Exploration

<!-- claim:SF-2026-ARXIV-2607-16602:start -->Action-conditioned world models are a key component of embodied AI, serving as scalable policy evaluators that reduce reliance on expensive real-world rollouts. To accurately capture diverse action-induced dynamics, such models should satisfy three key objectives-Physical Plausibility (P), Action Adherence (A), and Visual Fidelity (V), collectively referred to as PAV-while remaining robust to both in-distribution (ID) expert demonstrations and out-of-distribution (OOD) actions. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16602:end -->

**为什么进入候选分母。** 摘要首要问题为“Action-conditioned world models are a key component of embodied AI, serving as scalable policy evaluators that reduce reliance on expensive real-world rollouts.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** To address this, we propose PAVXploreRL, a reinforcement learning framework built on a pretrained latent world model that explicitly optimizes PAV objectives through reward-driven training.

**证据证明什么。** Experiments show that PAVXploreRL consistently outperforms pretrained baselines, achieving a 5.6% average gain across benchmarks and producing higher-quality PAV properties.

**证据没有证明什么。** A limitation of this work is that our focus is primarily on RL design, while the base world model does not explicitly incorporate components such as multi-view consistency. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16602v1#S3 — 3 Method; https://arxiv.org/html/2607.16602v1#S3.SS1 — 3.1 World Model Architecture and Training。Evaluation：https://arxiv.org/html/2607.16602v1#A1.SS4 — A.4 Ablation Study of VJEPA Reward; https://arxiv.org/html/2607.16602v1#S4 — 4 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.16602v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：A limitation of this work is that our focus is primarily on RL design, while the base world model does not explicitly incorporate components such as multi-view consistency.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16602:end -->

<!-- review:SF-2026-ARXIV-2607-16612:start -->
### Backpropagation-Free Trunk Training via the Split Forward Gradients

<!-- claim:SF-2026-ARXIV-2607-16612:start -->Backpropagation makes training deep networks memory intensive because it must store intermediate activations. Forward-mode methods avoid this cost, but their gradient estimates become increasingly noisy as the number of trained parameters grows. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16612:end -->

**为什么进入候选分母。** 摘要首要问题为“Backpropagation makes training deep networks memory intensive because it must store intermediate activations.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** Forward-mode methods avoid this cost, but their gradient estimates become increasingly noisy as the number of trained parameters grows.

**证据证明什么。** This reduces estimator variance and requires no backward pass through the trunk, while retaining an Adam-style convergence guarantee.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16612v1#A5.SS3 — E.3 Tabular Model Architecture; https://arxiv.org/html/2607.16612v1#A6.SS2 — F.2 Image Model Architecture。Evaluation：https://arxiv.org/html/2607.16612v1#A4 — Appendix D General Experimental Protocol; https://arxiv.org/html/2607.16612v1#A5.SS2 — E.2 Tabular Experimental Protocol。Limitations / counterevidence：https://arxiv.org/html/2607.16612v1#S5 — 5 Discussion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-PRETRAINING`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16612:end -->

<!-- review:SF-2026-ARXIV-2607-16617:start -->
### DataFlow-Harness: A Grounded Code-Agent Platform for Constructing Editable LLM Data Pipelines

<!-- claim:SF-2026-ARXIV-2607-16617:start -->Large language models (LLMs) are increasingly used to automate data-processing workflows, yet coding agents typically produce scripts that are not automatically materialized as persistent, editable platform artifacts. We call this disconnect the \textit{NL2Pipeline gap}. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16617:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language models (LLMs) are increasingly used to automate data-processing workflows, yet coding agents typically produce scripts that are not automatically materialized as persistent, editable platform artifacts.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** To bridge it, we introduce \textsc{DataFlow-Harness}, a platform that guides an LLM agent to construct platform-native directed acyclic graphs (DAGs) through typed, incremental mutations rather than free-form scripts.

**证据证明什么。** These results show that live platform grounding can produce persistent, editable workflow artifacts with an observed reliability close to script-generation baselines and with lower measured construction cost and latency.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16617v1#S3 — 3 System Architecture; https://arxiv.org/html/2607.16617v1#S4.SS3 — 4.3 Efficiency and System Cost ( RQ2 )。Evaluation：https://arxiv.org/html/2607.16617v1#S4 — 4 Experiments; https://arxiv.org/html/2607.16617v1#S4.SS1 — 4.1 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.16617v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/OpenDCAI/DataFlow-WebUI, https://docs.anthropic.com/claude/docs/claude-code, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`TRAIN-DATA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16617:end -->

<!-- review:SF-2026-ARXIV-2607-16621:start -->
### From Memory to Skills: Evidence-Grounded Co-Evolution Governance for Long-Horizon LLM Agents

<!-- claim:SF-2026-ARXIV-2607-16621:start -->Existing memory systems for long-horizon LLM agents often retrieve prior traces as passive context rather than converting them into executable capabilities. In this paper, we propose MSCE, a training-free Memory--Skill Co-Evolution framework that organizes agent experience into grounded step traces, reusable procedural policies, and declarative environmental cognition. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16621:end -->

**为什么进入候选分母。** 摘要首要问题为“Existing memory systems for long-horizon LLM agents often retrieve prior traces as passive context rather than converting them into executable capabilities.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** In this paper, we propose MSCE, a training-free Memory--Skill Co-Evolution framework that organizes agent experience into grounded step traces, reusable procedural policies, and declarative environmental cognition.

**证据证明什么。** Experiments on EvoAgentBench and LoCoMo demonstrate that MSCE significantly outperforms state-of-the-art skill-augmented and memory-driven agent baselines, exhibiting strong cross-domain transferability and lifelong-evolution capabilities.

**证据没有证明什么。** They support ranking, filtering, and revision of memory objects, but do not guarantee that a promoted policy would cause success under counterfactual intervention. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16621v1#S4 — 4 Method; https://arxiv.org/html/2607.16621v1#S8 — 8 Implementation Details of MSCE。Evaluation：https://arxiv.org/html/2607.16621v1#S10 — 10 Experimental Details; https://arxiv.org/html/2607.16621v1#S10.SS1 — 10.1 Experimental Settings。Limitations / counterevidence：https://arxiv.org/html/2607.16621v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.16621v1#Sx1 — Limitations。

**Artifact boundary。** Exact v1 links https://github.com/MemTensor/MemOS, https://github.com/HKUDS/OpenSpace, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：They support ranking, filtering, and revision of memory objects, but do not guarantee that a promoted policy would cause success under counterfactual intervention.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16621:end -->

<!-- review:SF-2026-ARXIV-2607-16632:start -->
### CLOSER-Bench: Evaluating Budgeted Cross-Stage Design Closure for Hardware Agents

<!-- claim:SF-2026-ARXIV-2607-16632:start -->Hardware engineering exposes coding agents to a form of long-horizon work that is difficult to capture with pass-at-k: progress is continuous, tool feedback is delayed and heterogeneous, and a backend failure may require revising RTL rather than tuning another physical-design parameter. Existing benchmarks measure RTL generation, repository repair, verification, PPA evolution, or physical implementation, but their different designs and oracles make it hard to determine where an agent succeeds or fails across abstraction boundaries. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16632:end -->

**为什么进入候选分母。** 摘要首要问题为“Hardware engineering exposes coding agents to a form of long-horizon work that is difficult to capture with pass-at-k: progress is continuous, tool feedback is delayed and heterogeneous, and a backend failure may require revising RTL rather than tuning another physical-design parameter.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We introduce CLOSER-Bench, a controlled evaluation protocol for budgeted cross-stage design closure.

**证据证明什么。** These results motivate treating hardware closure as a budgeted sequential decision problem rather than a collection of independent code generation tasks.

**证据没有证明什么。** 7 Conclusion Closer-Bench reframes hardware-agent evaluation around a controlled question: given the same design objective, does an agent benefit from explicit stage boundaries, and can it spend limited EDA calls and recover across those boundaries when they are removed? 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16632v1#S3 — 3 Benchmark Design; https://arxiv.org/html/2607.16632v1#S3.SSx1 — Design Principles。Evaluation：https://arxiv.org/html/2607.16632v1#S3 — 3 Benchmark Design; https://arxiv.org/html/2607.16632v1#S3.SSx5 — Hidden Evaluation and Anti-Gaming。Limitations / counterevidence：https://arxiv.org/html/2607.16632v1#S6 — 6 Discussion and Limitations; https://arxiv.org/html/2607.16632v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：7 Conclusion Closer-Bench reframes hardware-agent evaluation around a controlled question: given the same design objective, does an agent benefit from explicit stage boundaries, and can it spend limited EDA calls and recover across those boundaries when they are removed?

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16632:end -->

<!-- review:SF-2026-ARXIV-2607-16636:start -->
### PhyAgentOS: A Self-Evolving Operating System for Embodied Agents with Decoupled Cognitive Planning and Physical Execution

<!-- claim:SF-2026-ARXIV-2607-16636:start -->Vision-language-action models, world models, and agentic planners each advance physical intelligence, yet their composition lacks a common execution abstraction, shared state, semantic verification, and persistent experience across heterogeneous embodiments. We present PhyAgentOS, a runtime foundation delivering scheduling, verification, memory, benchmarking, and safety as system-level services. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16636:end -->

**为什么进入候选分母。** 摘要首要问题为“Vision-language-action models, world models, and agentic planners each advance physical intelligence, yet their composition lacks a common execution abstraction, shared state, semantic verification, and persistent experience across heterogeneous embodiments.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We present PhyAgentOS, a runtime foundation delivering scheduling, verification, memory, benchmarking, and safety as system-level services.

**证据证明什么。** Benchmarking reuses the deployment session and verification path, so results trace to real execution.

**证据没有证明什么。** 6.2 Limitations Several properties of the current system bound its applicability and point toward future work. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16636v1#S3 — 3 System Design; https://arxiv.org/html/2607.16636v1#S2.SS3 — 2.3 Agentic Systems。Evaluation：https://arxiv.org/html/2607.16636v1#S4.SS4 — 4.4 Benchmarking as an Instrument for Self-Evolution; https://arxiv.org/html/2607.16636v1#S5 — 5 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.16636v1#S6 — 6 Conclusion and Future Work; https://arxiv.org/html/2607.16636v1#S6.SS2 — 6.2 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/PhyAgentOS/PhyAgentOS, https://huggingface.co/WorldAgents-c/world_dreamer-robocasa365-multi_task, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：6.2 Limitations Several properties of the current system bound its applicability and point toward future work.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16636:end -->

<!-- review:SF-2026-ARXIV-2607-16643:start -->
### Diversity-Oriented Fine-Tuning for Uncertainty-Based Hallucination Detection

<!-- claim:SF-2026-ARXIV-2607-16643:start -->Existing hallucination detection methods are typically conducted at the inference stage, without making any modifications to the model itself. In this paper, we are interested in exploring fine-tuning strategies that enhance the detectability of hallucinations in the resulting model. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16643:end -->

**为什么进入候选分母。** 摘要首要问题为“Existing hallucination detection methods are typically conducted at the inference stage, without making any modifications to the model itself.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** To address this, we propose diversity-oriented fine-tuning to encourage more varied generations.

**证据证明什么。** We find that after adopting our fine-tuning methods, the models become less likely to produce low semantic entropy responses for hallucinated answers, thereby improving the effectiveness of hallucination detection, eventually yielding results better than or comparable with state of the art methods.

**证据没有证明什么。** Limitations The proposed diversity-oriented fine-tuning approach improves semantic-entropy-based hallucination detection but has several limitations. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16643v1#A1.SS2 — A.2 Baseline Methods; https://arxiv.org/html/2607.16643v1#S4 — 4 Methodology。Evaluation：https://arxiv.org/html/2607.16643v1#S6 — 6 Results and Analysis; https://arxiv.org/html/2607.16643v1#A1 — Appendix A Experimental Details。Limitations / counterevidence：https://arxiv.org/html/2607.16643v1#S7 — 7 Conclusion; https://arxiv.org/html/2607.16643v1#Sx1 — Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Limitations The proposed diversity-oriented fine-tuning approach improves semantic-entropy-based hallucination detection but has several limitations.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16643:end -->

<!-- review:SF-2026-ARXIV-2607-16646:start -->
### Falsification-Based Verification of LLM-Generated Optimization Models: Sound Test Batteries and Their Detection Limits

<!-- claim:SF-2026-ARXIV-2607-16646:start -->Large language models now translate natural-language descriptions of decision problems into solver-ready optimization models, and they fail silently. A generated model often runs and still encodes the wrong problem, while standard evaluation compares optimal values against labeled answers that deployment does not provide. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16646:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language models now translate natural-language descriptions of decision problems into solver-ready optimization models, and they fail silently.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** A generated model often runs and still encodes the wrong problem, while standard evaluation compares optimal values against labeled answers that deployment does not provide.

**证据证明什么。** Classical sensitivity analysis and duality thus offer a rigorous, label-free audit that complements existing evaluation of AI-generated optimization models.

**证据没有证明什么。** The blind set of Section 5 is not empty, and provably cannot be; Proposition 5.2 makes all guarantees orbit-relative, and Remark 4.5 makes the implemented limit tests probe-scale-relative. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16646v1#S11 — 11 Prompts and implementation details; https://arxiv.org/html/2607.16646v1#S2.SS1 — 2.1 LLMs for optimization modeling。Evaluation：https://arxiv.org/html/2607.16646v1#S10 — 10 Parse coverage, benchmark audit, and additional tables; https://arxiv.org/html/2607.16646v1#S2.SS4 — 2.4 Sensitivity analysis and comparative statics。Limitations / counterevidence：https://arxiv.org/html/2607.16646v1#S7.SS6 — 7.6 Scope and limitations; https://arxiv.org/html/2607.16646v1#S8 — 8 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：The blind set of Section 5 is not empty, and provably cannot be; Proposition 5.2 makes all guarantees orbit-relative, and Remark 4.5 makes the implemented limit tests probe-scale-relative.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16646:end -->

<!-- review:SF-2026-ARXIV-2607-16648:start -->
### Synchronization-Free Algebraic Fingerprints for Large Language Models: From Autoregressive to Diffusion Models

<!-- claim:SF-2026-ARXIV-2607-16648:start -->Large Language Models (LLMs) have created an urgent need for reliable watermarking methods that enable attribution of generated text while remaining robust to editing and paraphrasing. We propose a novel synchronization-free watermarking scheme in which every watermark consists of a single binary congruence generated from a pair of neighbouring tokens. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16648:end -->

**为什么进入候选分母。** 摘要首要问题为“Large Language Models (LLMs) have created an urgent need for reliable watermarking methods that enable attribution of generated text while remaining robust to editing and paraphrasing.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** Unlike existing block-based watermarking schemes, the proposed method avoids synchronization problems while providing a flexible framework for embedding both short and long secret identities.

**证据证明什么。** The analysis shows that reliable recovery requires only a small redundancy even for relatively high token corruption rates.

**证据没有证明什么。** The obtained results indicate that only a modest redundancy is required to recover the embedded identity with high probability even when a significant fraction of watermark bits is corrupted. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16648v1#S8 — 8 Evaluation Methodology; https://arxiv.org/html/2607.16648v1#S5 — 5 Recovery Algorithms。Evaluation：https://arxiv.org/html/2607.16648v1#S3.SS1 — 3.1 Probabilistic Analysis; https://arxiv.org/html/2607.16648v1#S6 — 6 Security Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.16648v1#S10 — 10 Conclusions and Future Research; https://arxiv.org/html/2607.16648v1#S9.SS5 — 9.5 Future Research。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：The obtained results indicate that only a modest redundancy is required to recover the embedded identity with high probability even when a significant fraction of watermark bits is corrupted.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16648:end -->

<!-- review:SF-2026-ARXIV-2607-16673:start -->
### SpecLA: Efficient Speculative Decoding for Linear-Attention Models

<!-- claim:SF-2026-ARXIV-2607-16673:start -->Linear-attention models replace the growing KV cache with recurrent states, but autoregressive decoding still reads, updates, and writes these states one token at a time. Speculative decoding can reduce this cost by verifying several draft tokens in one target pass, yet existing speculative systems are designed for Transformer KV caches. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16673:end -->

**为什么进入候选分母。** 摘要首要问题为“Linear-attention models replace the growing KV cache with recurrent states, but autoregressive decoding still reads, updates, and writes these states one token at a time.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** Speculative decoding can reduce this cost by verifying several draft tokens in one target pass, yet existing speculative systems are designed for Transformer KV caches.

**证据证明什么。** On an NVIDIA H100 with a public GDN-1.3B target, SpecLA achieves up to 1.70x end-to-end speedup over autoregressive decoding.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16673v1#S3 — 3. System Overview; https://arxiv.org/html/2607.16673v1#S2.SS2 — 2.2. Linear Attention and Stateful Sequence Models。Evaluation：https://arxiv.org/html/2607.16673v1#S8 — 8. Evaluation; https://arxiv.org/html/2607.16673v1#S8.SS1 — 8.1. Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.16673v1#S9 — 9. Conclusion。

**Artifact boundary。** Exact v1 links https://huggingface.co/m-a-p/1.3B-100B-GatedDeltaNet-pure, https://github.com/NVlabs/GatedDeltaNet, https://huggingface.co/Qwen/Qwen3-Next-80B-A3B-Instruct; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-SPECULATIVE-DECODING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16673:end -->

<!-- review:SF-2026-ARXIV-2607-16704:start -->
### Though Language Models Err While They Strive: Conformal Prediction for Self-Correcting Scientific Generation

<!-- claim:SF-2026-ARXIV-2607-16704:start -->Large language models frequently violate fundamental scientific principles when generating technical content, undermining their reliability in scientific applications. We introduce Scientific Feasibility Control SFC, a graph-structured conformal prediction framework that provides statistical guarantees for scientific reasoning validity through progressive absolute-coherent-factuality validation. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16704:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language models frequently violate fundamental scientific principles when generating technical content, undermining their reliability in scientific applications.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We introduce Scientific Feasibility Control SFC, a graph-structured conformal prediction framework that provides statistical guarantees for scientific reasoning validity through progressive absolute-coherent-factuality validation.

**证据证明什么。** We demonstrate SFC across established scientific reasoning benchmarks including PhyX multimodal physics, MATH, ScienceQA, and ARC Challenge, achieving 50.1 percent accuracy on PhyX physics reasoning, substantially outperforming recent reasoning models including DeepSeek-R1 49.8 percent and GPT-4 45.8 percent while providing 91.7 percent scientific validity with formal conformal coverage guarantees at alpha equals 0.10 confidence level and reducing scientific law violations by 73 percent across multiple model architectures.

**证据没有证明什么。** Our key contributions include formalizing absolute-coherent-factuality to capture scientific reasoning structure, extending conformal prediction to graph-structured dependencies, and demonstrating substantial improvements across challenging scientific benchmarks. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16704v1#S5 — 5 Scientific Feasibility Control Algorithm; https://arxiv.org/html/2607.16704v1#S5.SS5 — 5.5 Domain-Adaptive Implementation。Evaluation：https://arxiv.org/html/2607.16704v1#S6 — 6 Experiments and Main Results。Limitations / counterevidence：https://arxiv.org/html/2607.16704v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Our key contributions include formalizing absolute-coherent-factuality to capture scientific reasoning structure, extending conformal prediction to graph-structured dependencies, and demonstrating substantial improvements across challenging scientific benchmarks.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16704:end -->

<!-- review:SF-2026-ARXIV-2607-16708:start -->
### Model-Driven Discipline for Multi-Agent LLMs: Requirement-to-Verification Generation of Traceable System Models

<!-- claim:SF-2026-ARXIV-2607-16708:start -->Software complexity is a long-standing challenge for system engineers. Model-Driven Engineering (MDE) addresses it by treating models as first-class artefacts, but a typical MDE process spans many tools and produces heterogeneous models of different system aspects, making traceability, maintenance, and change management difficult. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16708:end -->

**为什么进入候选分母。** 摘要首要问题为“Software complexity is a long-standing challenge for system engineers.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** We propose RADIANT, an engineering methodology that combines MDE with Multi-Agent Large Language Models (LLMs) for complete model-based system development, with a focus on safety-critical systems.

**证据证明什么。** Evaluating RADIANT across three LLMs, we find that the multi-agent decomposition reliably improves the \emph{syntactic validity} of the generated formal artefacts over a single-agent baseline -- and their \emph{executability} where the model's code generation permits -- while gains in semantic accuracy are model-dependent.

**证据没有证明什么。** Model coverage spans three frontier LLMs (one open-weight, two proprietary) but is not exhaustive; in particular the model-dependent finding motivates a broader model sweep as future work. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16708v1#S3 — 3. Proposed Approach; https://arxiv.org/html/2607.16708v1#S5.SS2 — 5.2. Design Rationale。Evaluation：https://arxiv.org/html/2607.16708v1#S4.SS3 — 4.3. Evaluation Settings; https://arxiv.org/html/2607.16708v1#S2.SS4 — 2.4. Case Study。Limitations / counterevidence：https://arxiv.org/html/2607.16708v1#S5 — 5. Discussion; https://arxiv.org/html/2607.16708v1#S5.SS5 — 5.5. Threats to Validity。

**Artifact boundary。** Exact v1 links https://github.com/wrwei/RADIANT/tree/main/malcom.requirement/malcom.requirement.model/metamodel, https://github.com/wrwei/RADIANT/tree/main/malcom.bifrost/malcom.bifrost.model/metamodel, https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：Model coverage spans three frontier LLMs (one open-weight, two proprietary) but is not exhaustive; in particular the model-dependent finding motivates a broader model sweep as future work.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MULTI-AGENT`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16708:end -->

<!-- review:SF-2026-ARXIV-2607-16710:start -->
### Towards Inference-Aware Privacy Guidance for Data Preparation

<!-- claim:SF-2026-ARXIV-2607-16710:start -->Data preparation often begins with sensitive data and produces a releasable artifact for analysis, sharing, or model training. Existing workflows are primarily guided by utility: a curator drops attributes, coarsens values, filters populations, and suppresses tuples until the resulting dataset appears useful and safe. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16710:end -->

**为什么进入候选分母。** 摘要首要问题为“Data preparation often begins with sensitive data and produces a releasable artifact for analysis, sharing, or model training.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** We propose privacy-aware data preparation as an interactive guidance problem.

**证据证明什么。** We conclude by identifying the key challenges in building interactive, inference-aware data preparation systems.

**证据没有证明什么。** A final-only privacy check cannot explain which operator caused the change, in what direction, or by how much. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16710v1#S1 — 1. Introduction; https://arxiv.org/html/2607.16710v1#S2 — 2. Curation Plans and Disclosure Semantics。Evaluation：https://arxiv.org/html/2607.16710v1#S1 — 1. Introduction; https://arxiv.org/html/2607.16710v1#S2 — 2. Curation Plans and Disclosure Semantics。Limitations / counterevidence：https://arxiv.org/html/2607.16710v1#S1 — 1. Introduction; https://arxiv.org/html/2607.16710v1#S2 — 2. Curation Plans and Disclosure Semantics。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：A final-only privacy check cannot explain which operator caused the change, in what direction, or by how much.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-DATA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16710:end -->

<!-- review:SF-2026-ARXIV-2607-16716:start -->
### RECON: Benchmarking Agent Memory for Compositional Reasoning over Long Contexts

<!-- claim:SF-2026-ARXIV-2607-16716:start -->Large language models and LLM-based agents are widely used as personal chat assistants, enterprise copilots, and autonomous workflow agents. In all these applications, memory (the ability to retain, access, and reason over information accumulated over long contexts and multiple interactions) plays a crucial role in determining the reliability of any agent. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16716:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language models and LLM-based agents are widely used as personal chat assistants, enterprise copilots, and autonomous workflow agents.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We introduce RECON (Reasoning over Extended Contexts with Obfuscated Narratives), a benchmark for evaluating compositional reasoning over long contexts.

**证据证明什么。** Our evaluation reveals substantial limitations across current architectures: even the strongest non-Oracle system reaches only 22.4% Accuracy, with retrieval and reasoning each surfacing as challenges.

**证据没有证明什么。** We mitigate this by generating unique characters and evidence structures, but sensitivity to narrative style cannot be fully ruled out. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16716v1#S1 — 1 Introduction; https://arxiv.org/html/2607.16716v1#S2 — 2 Related Work。Evaluation：https://arxiv.org/html/2607.16716v1#S4 — 4 Evaluation and Results; https://arxiv.org/html/2607.16716v1#A3 — Appendix C Extended Human Validation Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.16716v1#S5 — 5 Conclusion; https://arxiv.org/html/2607.16716v1#S6 — 6 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：We mitigate this by generating unique characters and evidence structures, but sensitivity to narrative style cannot be fully ruled out.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16716:end -->

<!-- review:SF-2026-ARXIV-2607-16721:start -->
### Half the Experts, All the Code: One-Shot Domain Pruning of Mixture-of-Experts LLMs for Coding

<!-- claim:SF-2026-ARXIV-2607-16721:start -->The strongest open-weight coding models are mixture-of-experts (MoE) networks: most of their size comes from large pools of "expert" subnetworks, of which only a few act on any token. That pool is why these models do not fit on the machines most developers own, yet for a user who only wants coding help, most experts encode abilities that will never be invoked. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16721:end -->

**为什么进入候选分母。** 摘要首要问题为“The strongest open-weight coding models are mixture-of-experts (MoE) networks: most of their size comes from large pools of "expert" subnetworks, of which only a few act on any token.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** That pool is why these models do not fit on the machines most developers own, yet for a user who only wants coding help, most experts encode abilities that will never be invoked.

**证据证明什么。** We further show that perplexity, the metric much of the pruning literature leans on, can rate a broken model above an intact one; that a lightweight fine-tune recovers about half of what aggressive pruning loses; and that against quantizing the full model to the same memory, pruning wins only where quantization would have to drop below 3 bits per weight.

**证据没有证明什么。** 6 Limitations and Future Work Our study covers two model families under one controlled protocol; the criterion reversal of Section 5.3 is exactly the kind of finding that argues for more, and we make no claim that a third family would side with either of ours. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16721v1#S3 — 3 Method。Evaluation：https://arxiv.org/html/2607.16721v1#S4 — 4 Experimental Setup; https://arxiv.org/html/2607.16721v1#S5 — 5 Results。Limitations / counterevidence：https://arxiv.org/html/2607.16721v1#S6 — 6 Limitations and Future Work; https://arxiv.org/html/2607.16721v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：6 Limitations and Future Work Our study covers two model families under one controlled protocol; the criterion reversal of Section 5.3 is exactly the kind of finding that argues for more, and we make no claim that a third family would side with either of ours.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MODEL-MOE`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16721:end -->

<!-- review:SF-2026-ARXIV-2607-16726:start -->
### Can Experts Adapt Without Training? On Test-Time Modality Generalization in MVLMs

<!-- claim:SF-2026-ARXIV-2607-16726:start -->Medical vision-language models (MVLMs) promise broad zero-shot generalization, yet their reliability collapses when confronted with unseen modalities and domains, precisely where clinical robustness matters most. To address this gap, we revisit test-time modality generalization from the perspective of Mixture-of-Experts (MoE) and ask: can experts route-and-adapt without any optimization during inference? 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16726:end -->

**为什么进入候选分母。** 摘要首要问题为“Medical vision-language models (MVLMs) promise broad zero-shot generalization, yet their reliability collapses when confronted with unseen modalities and domains, precisely where clinical robustness matters most.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** To address this, we propose MoBE: a fully optimization-free framework that performs dynamic expert selection and adaptation at test time.

**证据证明什么。** Without parametric updates, MoBE augments a static MVLM with test-time routing and online statistics, achieving average accuracy gains of +4.72, +7.17, and +4.3 over state-of-the-art TTA methods across seen, unseen, and heterogeneous medical benchmarks, highlighting the effectiveness of training-free expert adaptation for robust modality generalization.

**证据没有证明什么。** Future work should reduce this overhead (e.g., via early-exit routing, pruning/distillation, or caching) and improve robustness when available expert-bank coverage of the test distribution is limited. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16726v1#S2 — 2 Methodology。Evaluation：https://arxiv.org/html/2607.16726v1#S3 — 3 Experiments and Results; https://arxiv.org/html/2607.16726v1#S3.SS1 — 3.1 Experimental Settings。Limitations / counterevidence：https://arxiv.org/html/2607.16726v1#S4 — 4 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/BioMedIA-MBZUAI/MoBE-A-Test-Time-Modality-Generalization-Method, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Future work should reduce this overhead (e.g., via early-exit routing, pruning/distillation, or caching) and improve robustness when available expert-bank coverage of the test distribution is limited.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-REPRESENTATION`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16726:end -->

<!-- review:SF-2026-ARXIV-2607-16740:start -->
### Agentic Code Review in the Terminal: A Trajectory-Level Analysis of Behavior, Cost, and Human-Alignment

<!-- claim:SF-2026-ARXIV-2607-16740:start -->Agentic code review in terminal-based environments enables early feedback during local development before pull request creation. However, existing evaluations remain performance-centric and fail to capture the dynamic behaviors of repository-grounded agentic reviewers. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16740:end -->

**为什么进入候选分母。** 摘要首要问题为“Agentic code review in terminal-based environments enables early feedback during local development before pull request creation.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** These findings highlight the potential benefits of trajectory-aware and cost-sensitive evaluation of future agentic code review systems.

**证据证明什么。** Our results show that agentic reviewers achieve higher review precision but incur substantial exploration and validation overhead, while successful reviews are associated with stronger planning and less downstream validation.

**证据没有证明什么。** Finally, findings may not generalize to future agents and systems; we release a replication package to support verification and future work. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16740v1#S3.SS2 — 3.2. Experimental Design。Evaluation：https://arxiv.org/html/2607.16740v1#S4 — 4. Experimental Results; https://arxiv.org/html/2607.16740v1#S3.SS2 — 3.2. Experimental Design。Limitations / counterevidence：https://arxiv.org/html/2607.16740v1#S5 — 5. Implications and Conclusion; https://arxiv.org/html/2607.16740v1#S5.SS2 — 5.2. Threats to Validity。

**Artifact boundary。** Exact v1 links https://github.com/harbor-framework/harbor, https://aclanthology.org/2025.emnlp-demos.15/, https://dx.doi.org/10.18653/v1/2025.emnlp-demos.15; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Finally, findings may not generalize to future agents and systems; we release a replication package to support verification and future work.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-PLATFORM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16740:end -->

<!-- review:SF-2026-ARXIV-2607-16745:start -->
### RELIC: Revealed Principles for Learning Interpretable Composable Skills in Multi-Agent Planning

<!-- claim:SF-2026-ARXIV-2607-16745:start -->Multi-agent planning becomes substantially harder when agents must improve specialized decision-making skills while keeping their executable implementations private. This setting arises when independently developed agents expose heterogeneous interfaces, observations, and capabilities, yet must coordinate under a shared team objective. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16745:end -->

**为什么进入候选分母。** 摘要首要问题为“Multi-agent planning becomes substantially harder when agents must improve specialized decision-making skills while keeping their executable implementations private.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We introduce RELIC, a framework for learning interpretable and composable programmatic skills through revealed principles.

**证据证明什么。** A shared principle memory accumulates transferable knowledge and promotes abstractions that repeatedly improve team-level performance.

**证据没有证明什么。** In such settings, the key challenge is not merely to optimize each skill independently, but to discover transferable coordination structure : what aspects of a successful local policy can be abstracted, communicated, and re-instantiated by another agent with a different interface and role. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16745v1#A1.SS1 — A.1 LLMs for Automated Heuristic Design; https://arxiv.org/html/2607.16745v1#S3 — 3 Methodology。Evaluation：https://arxiv.org/html/2607.16745v1#A3 — Appendix C Experimental Settings; https://arxiv.org/html/2607.16745v1#S4 — 4 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.16745v1#S1 — 1 Introduction; https://arxiv.org/html/2607.16745v1#S2 — 2 Preliminary。

**Artifact boundary。** Exact v1 links https://aclanthology.org/2024.emnlp-demo.25/, https://dx.doi.org/10.18653/v1/2024.emnlp-demo.25, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：In such settings, the key challenge is not merely to optimize each skill independently, but to discover transferable coordination structure : what aspects of a successful local policy can be abstracted, communicated, and re-instantiated by another agent with a different interface and role.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MULTI-AGENT`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16745:end -->

<!-- review:SF-2026-ARXIV-2607-16784:start -->
### Roomie: Interference-Aware Colocation for Efficient Model Serving

<!-- claim:SF-2026-ARXIV-2607-16784:start -->As demand for DNN inference grows, GPU capacity is increasingly oversubscribed, forcing operators to colocate multiple models on the same device in both cloud and edge deployments. Whether colocation succeeds or violates SLOs depends on the temporal overlap of kernels from concurrently executing models -- an effect that existing serving systems either ignore or approximate using aggregate resource profiles that fail to capture temporal dynamics. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16784:end -->

**为什么进入候选分母。** 摘要首要问题为“As demand for DNN inference grows, GPU capacity is increasingly oversubscribed, forcing operators to colocate multiple models on the same device in both cloud and edge deployments.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** Whether colocation succeeds or violates SLOs depends on the temporal overlap of kernels from concurrently executing models -- an effect that existing serving systems either ignore or approximate using aggregate resource profiles that fail to capture temporal dynamics.

**证据证明什么。** Our experimental evaluation compares Roomie against state-of-the-art solutions across both cloud-grade server clusters and embedded edge devices, demonstrating that Roomie reduces SLO violations (i.e., inference latency) by up to 3x, while maintaining comparable, and in many cases superior, goodput relative to existing approaches.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16784v1#S4 — 4. Roomie : System Design; https://arxiv.org/html/2607.16784v1#S2.SS3 — 2.3. Challenges in Modeling Kernel-Level Interference。Evaluation：https://arxiv.org/html/2607.16784v1#S5 — 5. Experimental Setup; https://arxiv.org/html/2607.16784v1#S6 — 6. Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.16784v1#S8 — 8. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-SCHEDULING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16784:end -->

<!-- review:SF-2026-ARXIV-2607-16789:start -->
### MultiLoReFT: Decoupling Shared and Modality-Specific Subspaces in Multimodal Learning via Low-Rank Representation Fine-Tuning

<!-- claim:SF-2026-ARXIV-2607-16789:start -->Real-world perception and decision making are inherently multimodal, integrating complementary signals across modalities. However, training multimodal models faces two main obstacles. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16789:end -->

**为什么进入候选分母。** 摘要首要问题为“Real-world perception and decision making are inherently multimodal, integrating complementary signals across modalities.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We introduce MultiLoReFT, an efficient and scalable low-rank representation fine-tuning framework for multimodal learning with pretrained unimodal models.

**证据证明什么。** Across simulated and real-world benchmarks, it produces representations that support multimodal prediction while explicitly revealing how shared and modality-specific information is distributed across modalities.

**证据没有证明什么。** Future work could explore integrating MultiLoReFT with joint or continual pretraining, scaling to larger multimodal corpora, and developing principled methods to identify and overcome limitations of unimodal pretrained encoders during fine-tuning. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16789v1#S1 — 1 Introduction; https://arxiv.org/html/2607.16789v1#S2 — 2 Related work。Evaluation：https://arxiv.org/html/2607.16789v1#A1.SS2 — A.2 Ablation study; https://arxiv.org/html/2607.16789v1#S4 — 4 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.16789v1#S6 — 6 Discussion。

**Artifact boundary。** Exact v1 links https://github.com/sanatonek/MultiLoReFT, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Future work could explore integrating MultiLoReFT with joint or continual pretraining, scaling to larger multimodal corpora, and developing principled methods to identify and overcome limitations of unimodal pretrained encoders during fine-tuning.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-LORA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16789:end -->

<!-- review:SF-2026-ARXIV-2607-16800:start -->
### Identity-Paired Progressive Depth Training: When Trainability Persists Beyond Expressibility

<!-- claim:SF-2026-ARXIV-2607-16800:start -->Variational Quantum Algorithms (VQAs) are a leading paradigm for near-term quantum computing, yet their training suffers from sensitivity to circuit depth, initialization, and landscape pathologies such as barren plateaus. We study \emph{progressive depth training} (PDT) -- a layerwise curriculum that trains a shallow circuit before appending new layers -- and identify a fundamental obstacle: fixed entangling gates (CNOTs) in hardware-efficient ansätze cause \emph{initialization shock}, an energy spike when new layers are added. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16800:end -->

**为什么进入候选分母。** 摘要首要问题为“Variational Quantum Algorithms (VQAs) are a leading paradigm for near-term quantum computing, yet their training suffers from sensitivity to circuit depth, initialization, and landscape pathologies such as barren plateaus.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We formalize IP-PDT as a continuation method on nested manifolds, prove monotone energy guarantees under an acceptance rule, and connect energy error to ground-state fidelity through spectral-gap inequalities.

**证据证明什么。** A detailed resource analysis shows that IP-PDT achieves lower total gate cost than both baselines by eliminating most CNOT gates.

**证据没有证明什么。** This monotonicity is the key ingredient for both Corollary 4.5 (optimal energy cannot increase with depth) and Theorem 4.9 (practical monotonicity via the acceptance rule). 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16800v1#S3.SS3 — 3.3 Effective single-entangler circuit (IP-PDT architecture); https://arxiv.org/html/2607.16800v1#S4.SS1 — 4.1 Continuation-theoretic framework。Evaluation：https://arxiv.org/html/2607.16800v1#S4 — 4 Theoretical Analysis; https://arxiv.org/html/2607.16800v1#S5 — 5 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.16800v1#A2 — Appendix B Extended Theoretical Discussion; https://arxiv.org/html/2607.16800v1#A2.SS1 — B.1 Identity-embedding property: extended discussion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：This monotonicity is the key ingredient for both Corollary 4.5 (optimal energy cannot increase with depth) and Theorem 4.9 (practical monotonicity via the acceptance rule).

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-PRETRAINING`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16800:end -->

<!-- review:SF-2026-ARXIV-2607-16836:start -->
### Beyond Storage: State as a Runtime Control Problem in Parallel and Distributed Systems

<!-- claim:SF-2026-ARXIV-2607-16836:start -->Shared state increasingly shapes both performance and failure behavior in streaming, serving, retrieval, and continual-learning systems. Existing studies, however, often isolate access control, hardware-aware execution, memory management, and long-horizon updates. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16836:end -->

**为什么进入候选分母。** 摘要首要问题为“Shared state increasingly shapes both performance and failure behavior in streaming, serving, retrieval, and continual-learning systems.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** Shared state increasingly shapes both performance and failure behavior in streaming, serving, retrieval, and continual-learning systems.

**证据证明什么。** Taken together, the evidence characterizes state management as a runtime control problem.

**证据没有证明什么。** Evaluation Dimensions for Future Surveys and Systems An enduring weakness is evaluation fragmentation. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16836v1#S5.SS1 — 5.1. A Design Space for Stateful Runtime Architectures; https://arxiv.org/html/2607.16836v1#A1.SS2 — A.2. Replicated, Transactional, and Memory-Resident Systems as Boundary References。Evaluation：https://arxiv.org/html/2607.16836v1#S6 — 6. Evaluation and Research Outlook; https://arxiv.org/html/2607.16836v1#S6.SS1 — 6.1. Evaluation Dimensions for Future Surveys and Systems。Limitations / counterevidence：https://arxiv.org/html/2607.16836v1#S5.SS2 — 5.2. Failure Modes and Anti-Patterns; https://arxiv.org/html/2607.16836v1#S6.SS1 — 6.1. Evaluation Dimensions for Future Surveys and Systems。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：Evaluation Dimensions for Future Surveys and Systems An enduring weakness is evaluation fragmentation.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-FOUNDATIONS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16836:end -->

<!-- review:SF-2026-ARXIV-2607-16848:start -->
### Beyond Memory Leaderboards: Evaluating Scientific Memory as Budgeted Context Restoration

<!-- claim:SF-2026-ARXIV-2607-16848:start -->Long-term memory is becoming a core component of LLM agents, but most memory benchmarks evaluate conversations or compact summaries, while research agents need to restore evidence from full scientific papers. We introduce two full-text scientific-memory benchmarks, Public AI Memory (PAIM; 81 papers, 66 questions) and Public Transformers (PTr; 252 papers, 98 questions). 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16848:end -->

**为什么进入候选分母。** 摘要首要问题为“Long-term memory is becoming a core component of LLM agents, but most memory benchmarks evaluate conversations or compact summaries, while research agents need to restore evidence from full scientific papers.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We evaluate eight memory/retrieval systems, including our own proposed Theoria, plus a no-retrieval baseline.

**证据证明什么。** Our results show that memory leaderboards are not interpretable without the full protocol: ingestion granularity, raw-text preservation, retrieval budget, retrieval modality, rubric audit, and judge choice all affect the outcome.

**证据没有证明什么。** MAGMA is described as a multi-graph agentic memory architecture…” [the relevant numbers were in the episode body that the KG-only mode does not return.] Reading. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16848v1#S2.SS2 — 2.2 Three foundational systems; https://arxiv.org/html/2607.16848v1#S2.SS5 — 2.5 Open-source frameworks。Evaluation：https://arxiv.org/html/2607.16848v1#S6 — 6 Experimental evaluation; https://arxiv.org/html/2607.16848v1#S2.SS7 — 2.7 Memory and scientific-QA benchmarks。Limitations / counterevidence：https://arxiv.org/html/2607.16848v1#S8 — 8 Discussion and limitations; https://arxiv.org/html/2607.16848v1#A1.SSx1 — PQ4 – saturation with integration failures。

**Artifact boundary。** Exact v1 links https://huggingface.co/datasets/quantellence/srb-data, https://github.com/crewAIInc/crewAI, https://code.claude.com/docs/en/memory; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：MAGMA is described as a multi-graph agentic memory architecture…” [the relevant numbers were in the episode body that the KG-only mode does not return.] Reading.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16848:end -->

<!-- review:SF-2026-ARXIV-2607-16851:start -->
### AgentBrew: Lifelong Knowledge Brewing from Strong Teachers to Weak LLM Agents

<!-- claim:SF-2026-ARXIV-2607-16851:start -->Deploying LLM agents typically requires a compact test-time student, even if a stronger teacher is available during training. We study knowledge brewing: distilling a teacher's interactive experience into a persistent external memory for the student. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16851:end -->

**为什么进入候选分母。** 摘要首要问题为“Deploying LLM agents typically requires a compact test-time student, even if a stronger teacher is available during training.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** To address these hurdles, we propose AgentBrew, comprising two coupled components.

**证据证明什么。** Extensive evaluations and comprehensive ablations across coding, math, and tool-use tasks demonstrate that this asymmetric, training-free brewing paradigm produces highly capable yet deployable LLM agents.

**证据没有证明什么。** Its three components directly address the key obstacles: a failure-triggered teacher with Ralph Loop validation converts sparse binary feedback into environment-certified notes (Q1); student-aware synthesis paired with reactive validation bridges the teacher–student capability gap (Q2); and an append-only skill-scoped memory accumulates knowledge across tasks without modifying the student model (Q3). 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16851v1#S2 — 2 The AgentBrew Framework; https://arxiv.org/html/2607.16851v1#S2.SS2 — 2.2 Framework Overview。Evaluation：https://arxiv.org/html/2607.16851v1#A1.SS2 — A.2 Detailed Setting of Benchmarks; https://arxiv.org/html/2607.16851v1#S3 — 3 Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.16851v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/HKUDS/UpSkill, https://docs.anthropic.com/en/docs/claude-code, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Its three components directly address the key obstacles: a failure-triggered teacher with Ralph Loop validation converts sparse binary feedback into environment-certified notes (Q1); student-aware synthesis paired with reactive validation bridges the teacher–student capability gap (Q2); and an append-only skill-scoped memory accumulates knowledge across tasks without modifying the student model (Q3).

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-PLATFORM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16851:end -->

<!-- review:SF-2026-ARXIV-2607-16868:start -->
### Beyond Semantic Equivalence: Logical Graphs for LLM Uncertainty Quantification

<!-- claim:SF-2026-ARXIV-2607-16868:start -->Large Language Models often produce confidently stated yet unreliable outputs, posing critical challenges for deployment in safety-sensitive applications. Existing uncertainty metrics such as semantic entropy capture agreement at the level of semantic equivalence, but largely ignore the logical relationships between distinct answers. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16868:end -->

**为什么进入候选分母。** 摘要首要问题为“Large Language Models often produce confidently stated yet unreliable outputs, posing critical challenges for deployment in safety-sensitive applications.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We propose Logical Graph Uncertainty (LGU), a framework that explicitly models implication and incompatibility among answers.

**证据证明什么。** Across multiple question-answering benchmarks and model families, LGU ranks first on average among existing uncertainty measures, with its largest gains---up to +7.1\% AUROC and +3.5\% AUARC over semantic entropy---on questions whose sampled answers are logically structured.

**证据没有证明什么。** 5 Discussion This work addresses a fundamental limitation in current uncertainty quantification methods for large language models: the inability to capture the logical structure that underlies model responses. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16868v1#S1.SS2 — 1.2 Our Logical Graph-Based Uncertainty Framework; https://arxiv.org/html/2607.16868v1#A1 — Appendix A Algorithms of Logical Graph Uncertainty。Evaluation：https://arxiv.org/html/2607.16868v1#A2 — Appendix B Experiment Details and Ablations; https://arxiv.org/html/2607.16868v1#A2.SS4 — B.4 Additional Experiments and Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.16868v1#S5 — 5 Discussion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：5 Discussion This work addresses a fundamental limitation in current uncertainty quantification methods for large language models: the inability to capture the logical structure that underlies model responses.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16868:end -->

<!-- review:SF-2026-ARXIV-2607-16872:start -->
### Trace-Based On-Policy Distillation for Masked Diffusion Language Models

<!-- claim:SF-2026-ARXIV-2607-16872:start -->Diffusion large language models (dLLMs) are a promising alternative to autoregressive generation. However, reasoning-oriented post-training for dLLMs remains challenging. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16872:end -->

**为什么进入候选分母。** 摘要首要问题为“Diffusion large language models (dLLMs) are a promising alternative to autoregressive generation.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** This paper proposes \textbf{trace-based on-policy distillation (TOPD)}, a teacher-supervised framework that transfers reasoning ability to a target dLLM without reward estimation.

**证据证明什么。** Compared with the RL-trained counterpart, TOPD achieves this with 4$\times$ fewer rollout rounds, corresponding to an estimated 96.0$\times$ to-accuracy model-compute speedup.

**证据没有证明什么。** Second, the evaluation is limited to mathematical reasoning benchmarks, including MATH500, AIME2024, and GSM8K, and does not cover broader reasoning tasks such as code generation, tool use, or open-ended instruction following. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16872v1#A1 — Appendix A Additional Method Details; https://arxiv.org/html/2607.16872v1#S3 — 3 Method。Evaluation：https://arxiv.org/html/2607.16872v1#A3 — Appendix C Experimental Details; https://arxiv.org/html/2607.16872v1#A3.SS5 — C.5 Evaluation Protocol。Limitations / counterevidence：https://arxiv.org/html/2607.16872v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.16872v1#Sx1 — Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Second, the evaluation is limited to mathematical reasoning benchmarks, including MATH500, AIME2024, and GSM8K, and does not cover broader reasoning tasks such as code generation, tool use, or open-ended instruction following.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-GENERATIVE-PARADIGMS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16872:end -->

<!-- review:SF-2026-ARXIV-2607-16892:start -->
### Robust KV Cache Management for LLM Serving under Output Token Length Uncertainty

<!-- claim:SF-2026-ARXIV-2607-16892:start -->KV cache memory is a primary bottleneck in modern LLM serving systems deployed on GPU clusters. A fundamental challenge is that the KV cache must be reserved upon request arrival, while the output token length remains unknown until generation completes. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16892:end -->

**为什么进入候选分母。** 摘要首要问题为“KV cache memory is a primary bottleneck in modern LLM serving systems deployed on GPU clusters.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** We present a robust KV cache management framework for LLM serving that jointly optimizes GPU parallelism configuration, KV cache reservation per request class, request routing across heterogeneous serving groups, and prefix caching for shared prompts.

**证据证明什么。** Under-reservation triggers preemption -- forcing termination and recomputation of requests and incurring significant overhead -- whereas over-reservation wastes memory and reduces throughput.

**证据没有证明什么。** Future work includes integration with production serving runtimes, online adaptation using streaming workload statistics, and joint optimization with energy-aware and geographically distributed inference scheduling. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16892v1#S3 — III System Model and Problem Formulation; https://arxiv.org/html/2607.16892v1#S3.SS1 — III-A System Overview。Evaluation：https://arxiv.org/html/2607.16892v1#S5.SS5 — V-E Ablation Analysis; https://arxiv.org/html/2607.16892v1#S5 — V Performance Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.16892v1#S6 — VI Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Future work includes integration with production serving runtimes, online adaptation using streaming workload statistics, and joint optimization with energy-aware and geographically distributed inference scheduling.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-KV-CACHE`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16892:end -->

<!-- review:SF-2026-ARXIV-2607-16900:start -->
### Environment-free Synthetic Data Generation for API-Calling Agents

<!-- claim:SF-2026-ARXIV-2607-16900:start -->Training API-calling large language model (LLM) agents demands massive amounts of high-quality trajectories. However, collecting such data at scale typically requires fully implemented environments with executable APIs and realistic, pre-populated backend databases, creating a major bottleneck for scalability. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16900:end -->

**为什么进入候选分母。** 摘要首要问题为“Training API-calling large language model (LLM) agents demands massive amounts of high-quality trajectories.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** Our results establish LLM-based API simulation as a practical, scalable solution for training agents across diverse API ecosystems.

**证据证明什么。** Our results establish LLM-based API simulation as a practical, scalable solution for training agents across diverse API ecosystems.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16900v1#A11.SS2 — K.2 API Schema Design; https://arxiv.org/html/2607.16900v1#S3 — 3 Method。Evaluation：https://arxiv.org/html/2607.16900v1#A6 — Appendix F Full Experimental Results; https://arxiv.org/html/2607.16900v1#S4.SS1 — 4.1 Results on AppWorld Benchmark。Limitations / counterevidence：https://arxiv.org/html/2607.16900v1#A1.SS2 — A.2 Failure Analysis; https://arxiv.org/html/2607.16900v1#A2.SS2 — B.2 Failure Analysis。

**Artifact boundary。** Exact v1 links https://doi.org/10.18653/v1/2020.emnlp-demos.6, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-TOOL-CALLING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16900:end -->

<!-- review:SF-2026-ARXIV-2607-16973:start -->
### TurboVec: A Case Study in Cost-Efficient Private Retrieval for Enterprise RAG via Codebook-Oblivious Quantization

<!-- claim:SF-2026-ARXIV-2607-16973:start -->Retrieval-Augmented Generation (RAG) systems increasingly power enterprise LLM applications, yet the vector retrieval layer introduces two underexplored challenges: (1) trained codebook quantizers may expose corpus statistics during index construction, creating a leakage channel in multi-tenant deployments, and (2) post-hoc filtering for tenant isolation degrades recall on selective queries. We study TurboVec, an open-source vector index built on TurboQuant - a codebook-oblivious scalar quantizer requiring no corpus-dependent training. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16973:end -->

**为什么进入候选分母。** 摘要首要问题为“Retrieval-Augmented Generation (RAG) systems increasingly power enterprise LLM applications, yet the vector retrieval layer introduces two underexplored challenges: (1) trained codebook quantizers may expose corpus statistics during index construction, creating a leakage channel in multi-tenant deployments, and (2) post-hoc filtering for tenant isolation degrades recall on selective queries.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** Retrieval-Augmented Generation (RAG) systems increasingly power enterprise LLM applications, yet the vector retrieval layer introduces two underexplored challenges: (1) trained codebook quantizers may expose corpus statistics during index construction, creating a leakage channel in multi-tenant deployments, and (2) post-hoc filtering for tenant isolation degrades recall on selective queries.

**证据证明什么。** Codebook-oblivious design reduces membership inference accuracy to near-random (50.0%) versus 57.3% for PQ codebooks.

**证据没有证明什么。** II-E Threat Model We consider the following narrow threat model: • Adversary : A malicious or compromised tenant who has gained read access to the shared quantized index structure (codebook or TQ+ parameters), but does not have access to: raw vectors, other tenants’ compressed vectors, query patterns, or access logs. • Attack surface : Codebook centroids and/or TQ+ calibration parameters only. • Goal : Infer membership (whether a candidate vector was in the training corpus) or reconstruct approximate original embeddings via codebook inversion. • Explicitly out of scope : Query-content privacy, access-pattern privacy, compressed-vector leakage, side-channel attacks. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16973v1#S3 — III System Design; https://arxiv.org/html/2607.16973v1#S2.SS2 — II-B TurboQuant Algorithm。Evaluation：https://arxiv.org/html/2607.16973v1#S4.SS2 — IV-B Results; https://arxiv.org/html/2607.16973v1#S4.SS3 — IV-C Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.16973v1#S8 — VIII Limitations and Future Work; https://arxiv.org/html/2607.16973v1#S2.SS5 — II-E Threat Model。

**Artifact boundary。** Exact v1 links https://huggingface.co/datasets/Qdrant/dbpedia-entities-openai3-text-embedding-3-large-1536-1M, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：II-E Threat Model We consider the following narrow threat model: • Adversary : A malicious or compromised tenant who has gained read access to the shared quantized index structure (codebook or TQ+ parameters), but does not have access to: raw vectors, other tenants’ compressed vectors, query patterns, or access logs. • Attack surface : Codebook centroids and/or TQ+ calibration parameters only. • Goal : Infer membership (whether a candidate vector was in the training corpus) or reconstruct approximate original embeddings via codebook inversion. • Explicitly out of scope : Query-content privacy, access-pattern privacy, compressed-vector leakage, side-channel attacks.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-RAG`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16973:end -->

<!-- review:SF-2026-ARXIV-2607-16999:start -->
### Counterfactual Shapley Credit Assignment

<!-- claim:SF-2026-ARXIV-2607-16999:start -->The Credit Assignment Problem (CAP) is fundamental to developing efficient and explainable Reinforcement Learning (RL) agents. Existing frameworks, whether relying on temporal contiguity or hindsight-conditioned reward reweighting, frequently fail to attribute properly between an agent's policy (skill) and environmental stochasticity (luck). 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16999:end -->

**为什么进入候选分母。** 摘要首要问题为“The Credit Assignment Problem (CAP) is fundamental to developing efficient and explainable Reinforcement Learning (RL) agents.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We introduce Counterfactual Shapley Credit Assignment, a novel framework grounded in causal theory that attributes credit and blame via the Counterfactual Shapley Value ($ϕ$-value).

**证据证明什么。** Empirical results demonstrate that $ϕ$-values align precisely to the ground truth causes of task rewards with superior sample efficiency in challenging environments where prior state-of-the-art methods fail to converge.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16999v1#A4.SS5 — D.5 PTR Buffer Design (Section B ); https://arxiv.org/html/2607.16999v1#A7 — Appendix G Credit Assignment Methods: Detailed Comparison。Evaluation：https://arxiv.org/html/2607.16999v1#A5 — Appendix E Additional Experiments; https://arxiv.org/html/2607.16999v1#S5 — 5 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.16999v1#A6 — Appendix F Limitations and Future Work; https://arxiv.org/html/2607.16999v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/Farama-Foundation/Minigrid, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-GRPO`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16999:end -->

<!-- review:SF-2026-ARXIV-2607-17019:start -->
### Regularize or Localize: When Training-Time KV-Cache Geometry Pays Under Quantization

<!-- claim:SF-2026-ARXIV-2607-17019:start -->We study whether \sigreg -- LeJEPA's anti-collapse objective -- can reshape representations during standard autoregressive language-model pretraining, and when the resulting geometry helps \kv-cache quantization. We train 110M-parameter models on 10B FineWeb tokens and report three findings. \textbf{(1)} At $λ{=}0.01$, \sigreg reduces hidden-state pairwise-cosine anisotropy by $38\%$ across three paired seeds. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-17019:end -->

**为什么进入候选分母。** 摘要首要问题为“We study whether \sigreg -- LeJEPA's anti-collapse objective -- can reshape representations during standard autoregressive language-model pretraining, and when the resulting geometry helps \kv-cache quantization.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We train 110M-parameter models on 10B FineWeb tokens and report three findings. \textbf{(1)} At $λ{=}0.01$, \sigreg reduces hidden-state pairwise-cosine anisotropy by $38\%$ across three paired seeds.

**证据证明什么。** Applying \sigreg directly to K and V during continued training, however, reduces mean cache anisotropy by $94\%$ across four checkpoints.

**证据没有证明什么。** Quantization is simulated (fake quantization in cache-disabled full-sequence forwards, NLL-only) and was not pre-specified in the plan—no deployed cache and no wall-clock or memory measurements. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.17019v1#S3 — 3 Method。Evaluation：https://arxiv.org/html/2607.17019v1#S4 — 4 Experimental Setup; https://arxiv.org/html/2607.17019v1#S5 — 5 Results。Limitations / counterevidence：https://arxiv.org/html/2607.17019v1#S7 — 7 Limitations; https://arxiv.org/html/2607.17019v1#S8 — 8 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Quantization is simulated (fake quantization in cache-disabled full-sequence forwards, NLL-only) and was not pre-specified in the plan—no deployed cache and no wall-clock or memory measurements.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`INFER-KV-CACHE`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-17019:end -->

<!-- review:SF-2026-ARXIV-2607-17175:start -->
### LMEdge: QoS-Aware LLM Inference Orchestration on Edge Clusters

<!-- claim:SF-2026-ARXIV-2607-17175:start -->Large language model (LLM) services increasingly operate on edge infrastructure, enabling low-latency and privacy-preserving AI services. However, efficiently serving LLM requests across heterogeneous and resource-constrained edge devices require orchestration mechanisms that jointly determine model configuration (family, size, and quantization level) and execution placement while satisfying user- and system-level quality of service (QoS) requirements. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-17175:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language model (LLM) services increasingly operate on edge infrastructure, enabling low-latency and privacy-preserving AI services.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** However, efficiently serving LLM requests across heterogeneous and resource-constrained edge devices require orchestration mechanisms that jointly determine model configuration (family, size, and quantization level) and execution placement while satisfying user- and system-level quality of service (QoS) requirements.

**证据证明什么。** Evaluation on a Kubernetes-based edge testbed with 57 instances and diverse query categories shows that LMEdge reduces latency, preserves accuracy, improves resource utilization, and increases serving ratio compared to two baselines.

**证据没有证明什么。** Future work will investigate online learning, energy-aware scheduling, and larger GPU-equipped edge clusters. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.17175v1#S4 — 4 LMEdge System Architecture; https://arxiv.org/html/2607.17175v1#S5 — 5 LMEdge Heuristic Algorithm。Evaluation：https://arxiv.org/html/2607.17175v1#S7 — 7 Evaluation Results; https://arxiv.org/html/2607.17175v1#S6 — 6 Evaluation Setup。Limitations / counterevidence：https://arxiv.org/html/2607.17175v1#S8 — 8 Conclusion。

**Artifact boundary。** Exact v1 links https://pypi.org/project/PuLP/, https://huggingface.co/nvidia/prompt-task-and-complexity-classifier, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Future work will investigate online learning, energy-aware scheduling, and larger GPU-equipped edge clusters.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-SCHEDULING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-17175:end -->

<!-- review:SF-2026-ARXIV-2607-17181:start -->
### Talaria: Session-Aware Serverless Serving of Hundred-Billion-Parameter LLMs

<!-- claim:SF-2026-ARXIV-2607-17181:start -->Serverless multi-model LLM systems multiplex popularity-skewed model catalogs over shared GPU pools, yet typically schedule each request independently. Tool-using agents break this abstraction: a session repeatedly calls an LLM across short tool gaps, carries a long reusable KV prefix, and is judged by session completion time (SCT). 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-17181:end -->

**为什么进入候选分母。** 摘要首要问题为“Serverless multi-model LLM systems multiplex popularity-skewed model catalogs over shared GPU pools, yet typically schedule each request independently.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** We present Talaria, a session-aware serverless multi-model serving system that makes session continuity a joint placement-and-admission decision.

**证据证明什么。** Against an otherwise identical round scheduler with SP, host-KV restoration, and D2D staging disabled, Talaria cuts p50 SCT from 1000 s to 189 s and p95 from 2296 s to 867 s, speedups of 5.3x and 2.6x.

**证据没有证明什么。** On the two-worker placement testbed, the router eliminates every avoidable model open at low and medium load and leaves only one at high load. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.17181v1#S3 — 3 Design; https://arxiv.org/html/2607.17181v1#S3.SS1 — 3.1 System Overview。Evaluation：https://arxiv.org/html/2607.17181v1#S5 — 5 Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.17181v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://huggingface.co/blog/huggingface/state-of-os-hf-spring-2026, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：On the two-worker placement testbed, the router eliminates every avoidable model open at low and medium load and leaves only one at high load.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-SCHEDULING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-17181:end -->

<!-- review:SF-2026-ARXIV-2607-17188:start -->
### UPAIR: Diagnosing Reasoning States via Uncertainty-Progress Alignment for Selective Intervention

<!-- claim:SF-2026-ARXIV-2607-17188:start -->While test-time scaling improves the problem-solving ability of large reasoning models (LRMs) through additional inference-time computation, it can also exacerbate overthinking and underthinking, which we formulate as reasoning state--action mismatch. Resolving this mismatch requires reliable reasoning state diagnosis, yet single-signal monitors provide ambiguous evidence, while steering-based controllers often rely on outcome-labeled supervision or model-specific calibration. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-17188:end -->

**为什么进入候选分母。** 摘要首要问题为“While test-time scaling improves the problem-solving ability of large reasoning models (LRMs) through additional inference-time computation, it can also exacerbate overthinking and underthinking, which we formulate as reasoning state--action mismatch.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** Building on this insight, we propose UPAIR, a training-free framework that couples lightweight uncertainty monitoring with event-triggered joint diagnosis and maps the resulting state to native continuation, selective strategy switching, or verification-guided stopping.

**证据证明什么。** End to end, UPAIR improves accuracy by up to 16.67 percentage points and reduces generated tokens by up to 29.64%, demonstrating the effectiveness of its integrated diagnosis and intervention, while online diagnosis costs less than 1% of natural-generation time.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.17188v1#A1.SS2 — A.2. Generalization vs. Training-based Methods; https://arxiv.org/html/2607.17188v1#A1.SS3 — A.3. Reliability vs. Entropy-based Methods。Evaluation：https://arxiv.org/html/2607.17188v1#A1 — Appendix A Extended Experimental Main Results; https://arxiv.org/html/2607.17188v1#S6.SS3 — 6.3. Ablation and In-Depth Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.17188v1#S7 — 7. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-17188:end -->

<!-- review:SF-2026-ARXIV-2607-17205:start -->
### A Systematic Evaluation of Trajectory Data Curation for LoRA Fine-Tuning of Code Agents

<!-- claim:SF-2026-ARXIV-2607-17205:start -->Supervised fine-tuning (SFT) of open-weight LLMs on expert agent trajectories has emerged as a prominent approach to building capable code agents without reliance on proprietary models. A central yet underexplored question is how trajectory quality and quantity jointly shape model performance. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-17205:end -->

**为什么进入候选分母。** 摘要首要问题为“Supervised fine-tuning (SFT) of open-weight LLMs on expert agent trajectories has emerged as a prominent approach to building capable code agents without reliance on proprietary models.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We propose a two-axis quality scoring framework -- Efficiency and Style -- and evaluate it through 16 controlled experiments spanning strategy, scale, and ablation analyses.

**证据证明什么。** Our results reveal a scale-dependent quality-quantity trade-off: at small scales, doubling the dataset (500 to 1,000) yields ~12.7% CE-loss reduction whereas the TopQ-Random gap stays &lt;1% (Mann-Whitney p &gt; 0.10); at 2,000 trajectories this same gap widens to 3.6% (p = 0.016).

**证据没有证明什么。** Since 7B -scale models attain near-zero SWE-bench resolve rates, we adopt cross -entropy (CE) loss on held -out trajectories as the primary metric, validated via first -action generation: CE loss and ROUGE-L are perfectly rank-correlated (Spearman 𝜌 = −1.00 ), with limited -sample evidence supporting but not conclusively establishing this proxy. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/pdf/2607.17205v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.17205v1#page=10 — PDF page 10。Evaluation：https://arxiv.org/pdf/2607.17205v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.17205v1#page=10 — PDF page 10。Limitations / counterevidence：https://arxiv.org/pdf/2607.17205v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.17205v1#page=10 — PDF page 10。

**Artifact boundary。** Exact v1 links https://github.com/hanzunye/swe-trajectory-quality-study; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Since 7B -scale models attain near-zero SWE-bench resolve rates, we adopt cross -entropy (CE) loss on held -out trajectories as the primary metric, validated via first -action generation: CE loss and ROUGE-L are perfectly rank-correlated (Spearman 𝜌 = −1.00 ), with limited -sample evidence supporting but not conclusively establishing this proxy.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-DATA`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-17205:end -->

<!-- review:SF-2026-ARXIV-2607-17213:start -->
### Retriever: Composing Closed-Loop Asynchronous Robot Programs

<!-- claim:SF-2026-ARXIV-2607-17213:start -->Building long-horizon robot agents requires composing closed-loop pipelines -- perception, belief update, planning, and control -- whose components run at different clocks and with variable latency. Today, these systems are often assembled with ad-hoc concurrency and pub/sub conventions that make timing and input-consumption semantics implicit, yielding schedule-dependent behavior that is hard to reproduce, debug, and reuse. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-17213:end -->

**为什么进入候选分母。** 摘要首要问题为“Building long-horizon robot agents requires composing closed-loop pipelines -- perception, belief update, planning, and control -- whose components run at different clocks and with variable latency.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** Current solutions typically solve parts of this problem at either the algorithmic or the systems layer, but not both.

**证据证明什么。** We formalize this view via an asynchronous environment-agent loop over continuous-time streams and show that finite-memory causal policies can be represented by compositions of these operators.

**证据没有证明什么。** These traces may support training future, more integrated end-to-end systems. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.17213v1#A1 — Appendix A Historical Lineage: Programming Models and System Abstractions for Hardware and Robots; https://arxiv.org/html/2607.17213v1#A1.SS8 — A-H Modern Learning Frameworks。Evaluation：https://arxiv.org/html/2607.17213v1#A6 — Appendix F Experiment Details; https://arxiv.org/html/2607.17213v1#A6.SS1 — F-A Benchmark Implementation Footprint。Limitations / counterevidence：https://arxiv.org/html/2607.17213v1#A1.SS9 — A-I Robotics Middleware: ROS Limitations; https://arxiv.org/html/2607.17213v1#S7 — VII Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/openretriever/retriever, https://github.com/dora-rs/dora, https://github.com/ApolloAuto/apollo/tree/master/cyber; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：These traces may support training future, more integrated end-to-end systems.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-WORKFLOW`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-17213:end -->

<!-- review:SF-2026-ARXIV-2607-17225:start -->
### Specifying the Delegated-Autonomy Boundary: Requirements Engineering for Agentic AI

<!-- claim:SF-2026-ARXIV-2607-17225:start -->Agentic AI systems do not just predict or recommend; they plan, maintain state, and act in external environments with varying degrees of autonomy. This changes the requirements engineering problem in a specific and under-addressed way: it introduces what we call the delegated-autonomy boundary -- the set of decisions about what may be delegated to the system, under what graduated authority, with what oversight, and how control is returned. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-17225:end -->

**为什么进入候选分母。** 摘要首要问题为“Agentic AI systems do not just predict or recommend; they plan, maintain state, and act in external environments with varying degrees of autonomy.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** Agentic AI systems do not just predict or recommend; they plan, maintain state, and act in external environments with varying degrees of autonomy.

**证据证明什么。** We illustrate the framework with two contrasting examples: a safety-critical hospital discharge coordination agent and an automated code review agent.

**证据没有证明什么。** Conclusion Agentic AI is not simply “AI with tools”; it is software to which humans delegate bounded, graduated autonomy. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.17225v1#S1 — 1. Introduction; https://arxiv.org/html/2607.17225v1#S2 — 2. When to Use Agents: the AJR。Evaluation：https://arxiv.org/html/2607.17225v1#S1 — 1. Introduction; https://arxiv.org/html/2607.17225v1#S2 — 2. When to Use Agents: the AJR。Limitations / counterevidence：https://arxiv.org/html/2607.17225v1#S5 — 5. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Conclusion Agentic AI is not simply “AI with tools”; it is software to which humans delegate bounded, graduated autonomy.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-PLATFORM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-17225:end -->

<!-- review:SF-2026-ARXIV-2607-17247:start -->
### Distilled Reinforcement Learning for LLM Post-training

<!-- claim:SF-2026-ARXIV-2607-17247:start -->Large language model (LLM) post-training is essential for improving reasoning, adaptation, and alignment. Existing methods mainly follow two paradigms: reinforcement learning (RL) and on-policy distillation (OPD). 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-17247:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language model (LLM) post-training is essential for improving reasoning, adaptation, and alignment.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** Existing methods mainly follow two paradigms: reinforcement learning (RL) and on-policy distillation (OPD).

**证据证明什么。** Extensive experiments across both within-family and cross-family distillation settings show that Distilled RL substantially outperforms standard RL and OPD in terms of both pass@1 and pass@k.

**证据没有证明什么。** Consequently, the training procedure cannot directly determine whether the teacher is capable of solving a given problem. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.17247v1#S3 — 3 Method; https://arxiv.org/html/2607.17247v1#A2 — Appendix B Implementation Details。Evaluation：https://arxiv.org/html/2607.17247v1#S3.SS1 — 3.1 Observation and Analysis; https://arxiv.org/html/2607.17247v1#S5 — 5 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.17247v1#A1 — Appendix A Limitation; https://arxiv.org/html/2607.17247v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/597358816/Distilled-RL, https://github.com/hiyouga/EasyR1, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Consequently, the training procedure cannot directly determine whether the teacher is capable of solving a given problem.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-GRPO`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-17247:end -->

<!-- review:SF-2026-ARXIV-2607-17250:start -->
### EvolvingWorld: An Open-Schema Framework for Co-Evolving Role-Play Agents and World Model in Interactive Literary World

<!-- claim:SF-2026-ARXIV-2607-17250:start -->This paper introduces EvolvingWorld, a framework and benchmark for character and world co-evolution in interactive literary worlds. Existing systems either treat interactive literary simulation as static persona imitation or isolated scene generation, failing to capture how characters and worlds evolve together over time. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-17250:end -->

**为什么进入候选分母。** 摘要首要问题为“This paper introduces EvolvingWorld, a framework and benchmark for character and world co-evolution in interactive literary worlds.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** Unlike prior systems relying on fixed schemas, EvolvingWorld adopts an open-schema framework to support simulation across diverse literary worlds.

**证据证明什么。** Experiments show that EvolvingWorld can improve long-horizon simulation by effectively maintaining persistent, coherent character and world development.

**证据没有证明什么。** However, this is mainly a constraint of the data rather than of the framework. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.17250v1#A5 — Appendix E Evaluation Framework; https://arxiv.org/html/2607.17250v1#S3 — 3 The EvolvingWorld Framework。Evaluation：https://arxiv.org/html/2607.17250v1#A6 — Appendix F Full Results on EvolvingWorld Benchmark; https://arxiv.org/html/2607.17250v1#A11.SS3 — K.3 Evaluation Prompts。Limitations / counterevidence：https://arxiv.org/html/2607.17250v1#S5 — 5 Conclusion; https://arxiv.org/html/2607.17250v1#Sx1 — Limitations。

**Artifact boundary。** Exact v1 links https://github.com/HKUST-KnowComp/EvolvingWorld, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：However, this is mainly a constraint of the data rather than of the framework.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-17250:end -->

<!-- review:SF-2026-ARXIV-2607-17257:start -->
### Asynchronous Multimodal Diffusion Policy Composition via Latency-Aware Guidance Fusion

<!-- claim:SF-2026-ARXIV-2607-17257:start -->Diffusion policies have shown strong potential for robotic imitation learning, and recent extensions incorporate additional modalities to improve manipulation performance. However, these modalities often differ not only in information content but also in sensing rates and inference latencies. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-17257:end -->

**为什么进入候选分母。** 摘要首要问题为“Diffusion policies have shown strong potential for robotic imitation learning, and recent extensions incorporate additional modalities to improve manipulation performance.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** We propose LAG-Fusion, a latency-aware guidance fusion framework for asynchronous multimodal diffusion policy composition.

**证据证明什么。** Diffusion policies have shown strong potential for robotic imitation learning, and recent extensions incorporate additional modalities to improve manipulation performance.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.17257v1#A1 — Appendix A Method Implementation Details; https://arxiv.org/html/2607.17257v1#S3 — 3 Method。Evaluation：https://arxiv.org/html/2607.17257v1#A2.SS2 — B.2 Additional Experiments Results; https://arxiv.org/html/2607.17257v1#A2 — Appendix B Experiment Details。Limitations / counterevidence：https://arxiv.org/html/2607.17257v1#A2.SS3 — B.3 Failure Analysis; https://arxiv.org/html/2607.17257v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-17257:end -->

<!-- review:SF-2026-ARXIV-2607-17269:start -->
### An Explicit World Model Based on Data-First Ontology: DaoQL Multimodal Storage Validation and Counterfactual Reasoning Evaluation

<!-- claim:SF-2026-ARXIV-2607-17269:start -->Large language models encode world models implicitly in neural weights, which exposes four structural risks in high-precision domains such as medicine and finance: hallucination, frozen knowledge, poor explainability, and poor modifiability. This paper proposes data-first ontology: LLMs are treated as reasoning and language engines, while deterministic knowledge is moved into an explicit multimodal database, DaoQL. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-17269:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language models encode world models implicitly in neural weights, which exposes four structural risks in high-precision domains such as medicine and finance: hallucination, frozen knowledge, poor explainability, and poor modifiability.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** The implemented system focuses on DaoQL's verified storage layer and explicit Eval path, integrating graph, column, vector, and full-text engines within one process.

**证据证明什么。** In a five-domain counterfactual experiment (n = 1250), DaoQL+GPT-4o achieves 94% composable counterfactual decomposability, 49 percentage points above GPT-4o alone.

**证据没有证明什么。** Ratios should not be read as kernel-only superiority. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.17269v1#S3.SS2 — 3.2 System Architecture and Implementation; https://arxiv.org/html/2607.17269v1#S2.SS2 — 2.2 LLM-Augmentation and Agent Frameworks。Evaluation：https://arxiv.org/html/2607.17269v1#S4 — 4 Results and Analysis; https://arxiv.org/html/2607.17269v1#S4.SS2 — 4.2 Three-Tier Microbenchmarks and Ablation。Limitations / counterevidence：https://arxiv.org/html/2607.17269v1#S5 — 5 Discussion; https://arxiv.org/html/2607.17269v1#S5.SS4 — 5.4 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/neo4j/neo4j/wiki/Neo4j-2025-changelog, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：Ratios should not be read as kernel-only superiority.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`structural_candidate`。
- Books 候选路由（尚非最终决定）：`Structural Candidate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-17269:end -->

<!-- review:SF-2026-ARXIV-2607-17288:start -->
### SAGA: Synthetic Agentic Graph Architecture for Temporal Benchmark Generation

<!-- claim:SF-2026-ARXIV-2607-17288:start -->High quality temporal graph benchmarks with rich semantics and ground-truth anomaly labels are essential for training graph neural networks, yet remain scarce due to privacy constraints and annotation costs. We present SAGA (Synthetic Agentic Graph Architecture), a system for generating large-scale, semantically rich temporal graphs via a four-phase pipeline. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-17288:end -->

**为什么进入候选分母。** 摘要首要问题为“High quality temporal graph benchmarks with rich semantics and ground-truth anomaly labels are essential for training graph neural networks, yet remain scarce due to privacy constraints and annotation costs.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We present SAGA (Synthetic Agentic Graph Architecture), a system for generating large-scale, semantically rich temporal graphs via a four-phase pipeline.

**证据证明什么。** Unlike structural generators (e.g., LDBC SNB, Kronecker/R-MAT) or purely LLM-based approaches, SAGA achieves structural realism, semantic richness, and automatic anomaly labeling in a unified framework.

**证据没有证明什么。** Conclusion SAGA demonstrates that treating logical conflicts between independent LLM agents as features naturally produces ground-truth anomaly labels. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.17288v1#S2 — 2. Model and Design Foundations; https://arxiv.org/html/2607.17288v1#S3 — 3. System Overview。Evaluation：https://arxiv.org/html/2607.17288v1#S5 — 5. Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.17288v1#S6 — 6. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/graphuofm/SAGA, https://github.com/IBM/AMLSim, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Conclusion SAGA demonstrates that treating logical conflicts between independent LLM agents as features naturally produces ground-truth anomaly labels.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-17288:end -->

<!-- review:SF-2026-ARXIV-2607-17291:start -->
### DRNOISE: Benchmarking Deep Research Agents in Misleading Evidence Environments

<!-- claim:SF-2026-ARXIV-2607-17291:start -->Deep research agents increasingly operate over the open web, where relevant records coexist with redundant summaries, outdated reports, and misleading documents. Existing evaluations offer limited insight into whether agents preserve sound evidential standards when an ordinary-looking false document is deliberately seeded into a searchable environment and offers a direct shortcut to a conflicting answer. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-17291:end -->

**为什么进入候选分母。** 摘要首要问题为“Deep research agents increasingly operate over the open web, where relevant records coexist with redundant summaries, outdated reports, and misleading documents.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We introduce DRNOISE, a 100-task benchmark for answer recovery under misleading evidence.

**证据证明什么。** Generic verification prompts reduce but do not close this gap.

**证据没有证明什么。** Future deep research evaluations should therefore test not only whether agents can find and cite evidence, but whether they can reconcile direct claims with record-level evidence in noisy information environments. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.17291v1#S1 — 1 Introduction; https://arxiv.org/html/2607.17291v1#S2 — 2 Related Work。Evaluation：https://arxiv.org/html/2607.17291v1#A3 — Appendix C Evaluation Parameters; https://arxiv.org/html/2607.17291v1#A4 — Appendix D Intervention and Ablation Prompts。Limitations / counterevidence：https://arxiv.org/html/2607.17291v1#S7 — 7 Limitations; https://arxiv.org/html/2607.17291v1#S8 — 8 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Future deep research evaluations should therefore test not only whether agents can find and cite evidence, but whether they can reconcile direct claims with record-level evidence in noisy information environments.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-17291:end -->

<!-- review:SF-2026-ARXIV-2607-17299:start -->
### WAR: Workload-Aware Rollouts for Synchronous Agentic Reinforcement Learning

<!-- claim:SF-2026-ARXIV-2607-17299:start -->Long-horizon rollout generation has become the dominant systems bottleneck in agentic reinforcement learning (RL). As agents interact with environments over many turns, trajectories rapidly grow to tens of thousands of tokens, making synchronous RL training increasingly constrained by rollout. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-17299:end -->

**为什么进入候选分母。** 摘要首要问题为“Long-horizon rollout generation has become the dominant systems bottleneck in agentic reinforcement learning (RL).”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** We propose WAR, a workload-aware rollout system that substantially accelerates synchronous agentic RL by jointly optimizing decoding and scheduling.

**证据证明什么。** These results show that WAR removes a major rollout bottleneck in synchronous agentic RL and provides a practical path toward scalable long-context agent training.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.17299v1#Sx3 — WAR System Design; https://arxiv.org/html/2607.17299v1#Sx6.SSx1 — RL Training Systems。Evaluation：https://arxiv.org/html/2607.17299v1#Sx5 — Evaluation; https://arxiv.org/html/2607.17299v1#Sx5.SSx1 — End-to-End Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.17299v1#Sx7 — Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`TRAIN-GRPO`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-17299:end -->

<!-- review:SF-2026-ARXIV-2607-17347:start -->
### Adapting Embedding Models for Agent Capability Retrieval

<!-- claim:SF-2026-ARXIV-2607-17347:start -->Open agent marketplaces list native agents, tool bundles, and reusable skill packages in the same search interface, yet practitioners still have little guidance on how to retrieve across this mixed catalog. We study whether off-the-shelf retrieval models, trained for general text retrieval, can be adapted to match user queries to executable agent capabilities, and whether the learned signal transfers beyond the benchmark used for tuning. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-17347:end -->

**为什么进入候选分母。** 摘要首要问题为“Open agent marketplaces list native agents, tool bundles, and reusable skill packages in the same search interface, yet practitioners still have little guidance on how to retrieve across this mixed catalog.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We study whether off-the-shelf retrieval models, trained for general text retrieval, can be adapted to match user queries to executable agent capabilities, and whether the learned signal transfers beyond the benchmark used for tuning.

**证据证明什么。** Code and data will be released upon publication.

**证据没有证明什么。** Discussion Capability-profile supervision transfers beyond its training benchmark across all three retriever families, though the size of the gain differs by model, and the ClawHub results show that the signal is not limited to native-agent catalogs. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.17347v1#S4 — 4. Supervision and Models。Evaluation：https://arxiv.org/html/2607.17347v1#S6 — 6. Experiments; https://arxiv.org/html/2607.17347v1#S6.SS1 — 6.1. In-domain adaptation on benchmark subsets。Limitations / counterevidence：https://arxiv.org/html/2607.17347v1#S7 — 7. Discussion; https://arxiv.org/html/2607.17347v1#S8 — 8. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Discussion Capability-profile supervision transfers beyond its training benchmark across all three retriever families, though the size of the gain differs by model, and the ClawHub results show that the signal is not limited to native-agent catalogs.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-PLATFORM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-17347:end -->

<!-- review:SF-2026-ARXIV-2607-17352:start -->
### Self-Modifying Lean Proof Agents with Verifier-Grounded Benchmark Coevolution

<!-- claim:SF-2026-ARXIV-2607-17352:start -->Designing effective Lean proof agents is a central challenge in formal mathematical reasoning. Beyond building stronger provers, recent work emphasizes the workflow around Lean: how an agent decomposes proof obligations, uses tools and compiler feedback, diagnoses failures, repairs proofs, and maintains structured proof context. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-17352:end -->

**为什么进入候选分母。** 摘要首要问题为“Designing effective Lean proof agents is a central challenge in formal mathematical reasoning.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** Unlike most self-evolving systems, which optimize against a fixed external benchmark, our system coevolves the agent and its benchmark.

**证据证明什么。** The best coevolving agent reaches a 45.1% held-out solve rate, versus 12.7% for the seed and 32.0% for the best fixed-benchmark agent, showing that verifier-grounded self-evolution can improve Lean proof workflows under a coevolving benchmark.

**证据没有证明什么。** In the present -generation runs, however, the agent has not yet evolved a deep, durable proof-context graph. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.17352v1#S3 — 3 Method; https://arxiv.org/html/2607.17352v1#A2 — Appendix B Benchmark-update algorithm。Evaluation：https://arxiv.org/html/2607.17352v1#A1 — Appendix A Experimental details and hyperparameters; https://arxiv.org/html/2607.17352v1#A2 — Appendix B Benchmark-update algorithm。Limitations / counterevidence：https://arxiv.org/html/2607.17352v1#S5 — 5 Discussion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：In the present -generation runs, however, the agent has not yet evolved a deep, durable proof-context graph.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-REFLECTION`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-17352:end -->

<!-- review:SF-2026-ARXIV-2607-17384:start -->
### Quantifying Diversity of Thought: A Predictive Law of Weighted LLM Ensemble Lift

<!-- claim:SF-2026-ARXIV-2607-17384:start -->This paper provides an experimentally verified formal law for calculating the uplift that diversity of thought provides in Large Language Model (LLM) ensembles. From first principles, we derive an exact decomposition of LLM ensemble lift into rescue and damage masses, which yields a compact heuristic for calculating uplift. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-17384:end -->

**为什么进入候选分母。** 摘要首要问题为“This paper provides an experimentally verified formal law for calculating the uplift that diversity of thought provides in Large Language Model (LLM) ensembles.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** From first principles, we derive an exact decomposition of LLM ensemble lift into rescue and damage masses, which yields a compact heuristic for calculating uplift.

**证据证明什么。** Raw $ϕ$ has almost no predictive power ($R^2\le 0.09$ throughout); the accuracy-adjusted $ϕ_{\mathrm{adj}}$ is markedly superior ($R^2=0.67$ on SuperGPQA), and the heuristic combining these metrics is the most stable pre-pooling predictor across the three datasets.

**证据没有证明什么。** Secondly, the 45 pairs share ten models and a common question set, so pair-level statistics are not independent replicates; transfer is task transfer for this fixed fleet, not model-level external validation. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.17384v1#S3 — 3. A Weighted Swap Law for Model Pairs; https://arxiv.org/html/2607.17384v1#S3.SS2 — 3.2. The Complete Lift Model。Evaluation：https://arxiv.org/html/2607.17384v1#S5 — 5. Datasets & Experimental Setup; https://arxiv.org/html/2607.17384v1#S9 — 9. Analysis & Limitations。Limitations / counterevidence：https://arxiv.org/html/2607.17384v1#S10 — 10. Conclusion; https://arxiv.org/html/2607.17384v1#S9 — 9. Analysis & Limitations。

**Artifact boundary。** Exact v1 links https://huggingface.co/datasets/Idavidrein/gpqa, https://huggingface.co/datasets/IcyApril/deciban, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Secondly, the 45 pairs share ten models and a common question set, so pair-level statistics are not independent replicates; transfer is task transfer for this fixed fleet, not model-level external validation.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MULTI-AGENT`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-17384:end -->

<!-- review:SF-2026-ARXIV-2607-17389:start -->
### Portable models as a replacement for industrial heuristics in compiler optimizations

<!-- claim:SF-2026-ARXIV-2607-17389:start -->The paper investigates the possibility of predicting function-inlining decisions in compact compilers, source-to-source tools, and interpreters where the reuse of GCC or LLVM optimization infrastructure is impractical. The relevance of this work is determined by the need to transfer mature inlining heuristics to systems with limited compiler infrastructure, restricted runtime dependencies, and reduced access to target-specific analysis. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-17389:end -->

**为什么进入候选分母。** 摘要首要问题为“The paper investigates the possibility of predicting function-inlining decisions in compact compilers, source-to-source tools, and interpreters where the reuse of GCC or LLVM optimization infrastructure is impractical.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** To overcome these constraints, we propose a portable inlining-prediction framework.

**证据证明什么。** Under leave-one-project-out validation, CatBoost reaches ROC-AUC 0.928 and PR-AUC 0.713; after threshold tuning, F1 improves from 0.670 to 0.729 and the false-positive rate drops from 0.192 to 0.084.

**证据没有证明什么。** The AST/site-only experiment suggests that a useful lower-dependency model is possible even without structural-IR-derived counters. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.17389v1#S4 — 4 Architecture of the Proposed Solution; https://arxiv.org/html/2607.17389v1#S10 — 10 Evaluation of the Model。Evaluation：https://arxiv.org/html/2607.17389v1#S10 — 10 Evaluation of the Model; https://arxiv.org/html/2607.17389v1#S7 — 7 Basic Dataset Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.17389v1#S12 — 12 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/alexfru/SmallerC, https://github.com/DaveGamble/cJSON, https://github.com/json-c/json-c; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：The AST/site-only experiment suggests that a useful lower-dependency model is possible even without structural-IR-derived counters.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`INFER-TENSORRT-LLM`；evidence-stage relation：`principle_reuse`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-17389:end -->

<!-- review:SF-2026-ARXIV-2607-17409:start -->
### Efficient Sequential Evaluation of Large Language Models

<!-- claim:SF-2026-ARXIV-2607-17409:start -->We study the problem of sequentially evaluating a new large language model (LLM) on a fixed question set using historical performance data from prior LLMs. Our goal is to construct a confidence sequence (CS) for the model's capability on this question set and to design active querying rules that shrink the CS width as quickly as possible. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-17409:end -->

**为什么进入候选分母。** 摘要首要问题为“We study the problem of sequentially evaluating a new large language model (LLM) on a fixed question set using historical performance data from prior LLMs.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Interestingly, we observe that the simplest querying rule, uniform sampling, can sometimes outperform more adaptive querying rules for both methods.

**证据证明什么。** We first study these approaches under an oracle setting, and demonstrate the oracle optimality of the RIPr-based construction.

**证据没有证明什么。** Future work includes developing more effective querying rules, possibly using reinforcement learning. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.17409v1#S4.SS1 — 4.1 RIPr-based approach; https://arxiv.org/html/2607.17409v1#S4.SS2 — 4.2 Testing-by-betting-based approach。Evaluation：https://arxiv.org/html/2607.17409v1#A1 — Appendix A Experiment details and supplemental results; https://arxiv.org/html/2607.17409v1#S5.SS2 — 5.2 Analysis of the shrinkage behavior of CSs。Limitations / counterevidence：https://arxiv.org/html/2607.17409v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://projecteuclid.org/proceedings/berkeley-symposium-on-mathematical-statistics-and-probability/Proceedings-of-the-Fourth-Berkeley-Symposium-on-Mathematical-Statistics-and/Chapter/Optimal-Gambling-Systems-for-Favorable-Games/bsmsp/1200512159, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Future work includes developing more effective querying rules, possibly using reinforcement learning.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-17409:end -->

<!-- review:SF-2026-ARXIV-2607-17415:start -->
### Transition-Aware Backend Dispatch for Edge LLM Inference

<!-- claim:SF-2026-ARXIV-2607-17415:start -->Efficient large language model (LLM) inference on edge platforms is limited not only by model size, but also by shape-dependent performance differences across execution backends. Static backend assignment cannot exploit this variation, while independent per-operator selection can introduce costly device and framework switches. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-17415:end -->

**为什么进入候选分母。** 摘要首要问题为“Efficient large language model (LLM) inference on edge platforms is limited not only by model size, but also by shape-dependent performance differences across execution backends.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** Static backend assignment cannot exploit this variation, while independent per-operator selection can introduce costly device and framework switches.

**证据证明什么。** These results demonstrate that incorporating operator shape and backend-transition context can improve selective backend dispatch for edge transformer workloads.

**证据没有证明什么。** V Future Work Future work will integrate the selector into a mixed-backend runtime, enabling direct validation of measurement-backed replay predictions during connected model execution. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.17415v1#S3 — III Methodology; https://arxiv.org/html/2607.17415v1#S3.SS1 — III-A Full-Model Inference Trace Collection。Evaluation：https://arxiv.org/html/2607.17415v1#S4 — IV Evaluation Results; https://arxiv.org/html/2607.17415v1#S3.SS3 — III-C Jetson Multi-Backend Benchmarking。Limitations / counterevidence：https://arxiv.org/html/2607.17415v1#S5 — V Future Work; https://arxiv.org/html/2607.17415v1#S6 — VI Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：V Future Work Future work will integrate the selector into a mixed-backend runtime, enabling direct validation of measurement-backed replay predictions during connected model execution.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-SCHEDULING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-17415:end -->

<!-- review:SF-2026-ARXIV-2607-17419:start -->
### Kernelized Linear Attention: Breaking the Capacity Wall with Symmetric Cones

<!-- claim:SF-2026-ARXIV-2607-17419:start -->Linear attention promises constant-time recurrent inference but degrades sharply on associative recall. We formulate attention recall as a spherical-packing problem and introduce Kernelized Linear Attention Activations (KATA), a framework whose feature maps are derived from first principles by certifying nonnegative attention weights through a self-dual homogeneous cone. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-17419:end -->

**为什么进入候选分母。** 摘要首要问题为“Linear attention promises constant-time recurrent inference but degrades sharply on associative recall.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We formulate attention recall as a spherical-packing problem and introduce Kernelized Linear Attention Activations (KATA), a framework whose feature maps are derived from first principles by certifying nonnegative attention weights through a self-dual homogeneous cone.

**证据证明什么。** Induction preserves near-perfect recall, while kernel benchmarks show that the maps can be implemented efficiently.

**证据没有证明什么。** 7 Discussion and Limitations The results separate three aspects of associative attention that are often grouped under capacity : the geometry available for storing bindings, the ability of training to realize that geometry, and the contextual fluency needed to construct the correct association from language. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.17419v1#A6.SS4 — F.4 Per-method architectures and reproducibility; https://arxiv.org/html/2607.17419v1#A1.SS1 — A.1 Kernel methods。Evaluation：https://arxiv.org/html/2607.17419v1#A5 — Appendix E Hardware implementation and benchmarks; https://arxiv.org/html/2607.17419v1#A5.SS2 — E.2 Induction-head benchmark。Limitations / counterevidence：https://arxiv.org/html/2607.17419v1#S7 — 7 Discussion and Limitations。

**Artifact boundary。** Exact v1 links https://github.com/ayghri/kata, https://github.com/fla-org/flash-linear-attention, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：7 Discussion and Limitations The results separate three aspects of associative attention that are often grouped under capacity : the geometry available for storing bindings, the ability of training to realize that geometry, and the contextual fluency needed to construct the correct association from language.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MODEL-SELF-ATTENTION`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-17419:end -->

<!-- review:SF-2026-ARXIV-2607-17422:start -->
### LATTICE: Constraint-Directed Scheduling, Memory Planning, and Pipeline Refinement for NPUs

<!-- claim:SF-2026-ARXIV-2607-17422:start -->General-purpose NPUs execute fine-grained command DAGs across heterogeneous compute and memory-transfer engines backed by finite, explicitly managed on-chip memories. This execution model creates a directed dependency between scheduling and memory planning: different legal topological orders induce different lifetime overlap, placement opportunities, and spill behavior, while a materialized layout introduces physical-address reuse constraints absent from the input precedence DAG. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-17422:end -->

**为什么进入候选分母。** 摘要首要问题为“General-purpose NPUs execute fine-grained command DAGs across heterogeneous compute and memory-transfer engines backed by finite, explicitly managed on-chip memories.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** We present LATTICE, a deterministic constraint-directed compiler pipeline.

**证据证明什么。** Across six artifact-provided command traces labeled as derived from a Da Vinci NPU flow, LATTICE achieves the best or tied-best result in all 24 evaluated workload-metric comparisons.

**证据没有证明什么。** Future work will extend this direction to larger graphs, multi-core execution, and tighter runtime and system-level coordination. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.17422v1#S4 — 4. DAN-Scheduler Design; https://arxiv.org/html/2607.17422v1#S5 — 5. Experimental Methodology。Evaluation：https://arxiv.org/html/2607.17422v1#S5 — 5. Experimental Methodology; https://arxiv.org/html/2607.17422v1#S6 — 6. Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.17422v1#S8 — 8. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：Future work will extend this direction to larger graphs, multi-core execution, and tighter runtime and system-level coordination.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-SCHEDULING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-17422:end -->

<!-- review:SF-2026-ARXIV-2607-17425:start -->
### Decoder-Preserving Sparse Autoencoders: Which Readouts Survive Sparse Compression?

<!-- claim:SF-2026-ARXIV-2607-17425:start -->Sparse autoencoders (SAEs) compress model activations into sparse codes, but equal reconstruction error and sparsity can preserve different linearly decodable signals. We formalize this ambiguity as a matrix-valued distortion between optimal ridge-prediction operators and train decoder-preserving SAEs by combining this distortion with reconstruction loss. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-17425:end -->

**为什么进入候选分母。** 摘要首要问题为“Sparse autoencoders (SAEs) compress model activations into sparse codes, but equal reconstruction error and sparsity can preserve different linearly decodable signals.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We formalize this ambiguity as a matrix-valued distortion between optimal ridge-prediction operators and train decoder-preserving SAEs by combining this distortion with reconstruction loss.

**证据证明什么。** The same checkpoints pass an average natural-text output-KL noninferiority test, but one matched Pythia pair shows no improvement in probes restricted to a few sparse features.

**证据没有证明什么。** Future work will replicate the readout effect across layers, model families, widths, and sparse architectures; construct task priors from independently specified real prediction families; and compare adaptive decoder preservation with static baselines along genuinely matched reconstruction–sparsity frontiers. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.17425v1#A1.SS10 — A.10 Optimization and architecture audits; https://arxiv.org/html/2607.17425v1#A1.SS2 — A.2 Language-model protocol and paired GPT-2 evaluation。Evaluation：https://arxiv.org/html/2607.17425v1#S5 — 5 Experiments and Results; https://arxiv.org/html/2607.17425v1#A1 — Appendix A Experimental Details。Limitations / counterevidence：https://arxiv.org/html/2607.17425v1#S7 — 7 Discussion, Limitations, and Future Work。

**Artifact boundary。** Exact v1 links https://github.com/aniket-desh/decoder-preserving-sae, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Future work will replicate the readout effect across layers, model families, widths, and sparse architectures; construct task priors from independently specified real prediction families; and compare adaptive decoder preservation with static baselines along genuinely matched reconstruction–sparsity frontiers.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`WORLDVIEW-REPRESENTATION`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-17425:end -->

<!-- review:SF-2026-ARXIV-2607-17454:start -->
### Test-Time Scaling for World Action Models via Zero-Shot Geometric Evaluation

<!-- claim:SF-2026-ARXIV-2607-17454:start -->Test-time scaling improves foundation-model inference by spending additional computation, but robot control requires deciding whether extra compute is useful before executing an action. World Action Models (WAMs) make this decision natural: each rollout exposes both an action chunk and predicted future observations. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-17454:end -->

**为什么进入候选分母。** 摘要首要问题为“Test-time scaling improves foundation-model inference by spending additional computation, but robot control requires deciding whether extra compute is useful before executing an action.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We propose \methodgated, a training-free selective test-time scaling framework for WAMs.

**证据证明什么。** Test-time scaling improves foundation-model inference by spending additional computation, but robot control requires deciding whether extra compute is useful before executing an action.

**证据没有证明什么。** Given , we compute dense optical flow between the current primary-view observation and the predicted future frame . 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.17454v1#S3 — 3 Method。Evaluation：https://arxiv.org/html/2607.17454v1#S4 — 4 Experiments; https://arxiv.org/html/2607.17454v1#S4.SS1 — 4.1 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.17454v1#S3.SS1 — 3.1 Action–Future Gate for Selective Sampling; https://arxiv.org/html/2607.17454v1#S4.SS5 — 4.5 Best-of- Failure Analysis。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Given , we compute dense optical flow between the current primary-view observation and the predicted future frame .

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-17454:end -->

<!-- review:SF-2026-ARXIV-2607-17525:start -->
### FailureAtlas: A Taxonomy of Failure Modes in Multi-Provider LLM Serving Infrastructure

<!-- claim:SF-2026-ARXIV-2607-17525:start -->Multi-provider LLM gateways reverse proxies that route, load-balance, and rate-limit requests across foundation-model APIs have become critical production infrastructure. Yet the failure modes specific to this architectural layer remain undocumented, scattered across issue trackers and post-mortems with no unifying framework. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-17525:end -->

**为什么进入候选分母。** 摘要首要问题为“Multi-provider LLM gateways reverse proxies that route, load-balance, and rate-limit requests across foundation-model APIs have become critical production infrastructure.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Yet the failure modes specific to this architectural layer remain undocumented, scattered across issue trackers and post-mortems with no unifying framework.

**证据证明什么。** Two such silent failures a concurrency race condition causing history loss and a streaming index collision corrupting tool-call payloads were discovered first-hand during \cb{} evaluation campaigns.

**证据没有证明什么。** 7 Discussion: Why Silent Failures Dominate The FA catalog is deliberately small, but its composition points to a structural reality about modern LLM-powered applications: the most dangerous failures are not the ones that take the system offline, but the ones that quietly corrupt its internal state while reporting perfect health. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.17525v1#S2.SS1 — 2.1 Distributed-Systems Failure Taxonomies; https://arxiv.org/html/2607.17525v1#S3 — 3 Taxonomy Design。Evaluation：https://arxiv.org/html/2607.17525v1#S2.SS2 — 2.2 LLM Evaluation and Reliability。Limitations / counterevidence：https://arxiv.org/html/2607.17525v1#S7 — 7 Discussion: Why Silent Failures Dominate; https://arxiv.org/html/2607.17525v1#A1 — Appendix A Full Failure Catalog。

**Artifact boundary。** Exact v1 links https://github.com/BerriAI/litellm, https://github.com/Portkey-AI/gateway, https://github.com/Vishal-sys-code/failure-atlas; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：7 Discussion: Why Silent Failures Dominate The FA catalog is deliberately small, but its composition points to a structural reality about modern LLM-powered applications: the most dangerous failures are not the ones that take the system offline, but the ones that quietly corrupt its internal state while reporting perfect health.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-GATEWAY`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-17525:end -->

<!-- review:SF-2026-ARXIV-2607-17528:start -->
### Can AI Agents Really Complete RTL-to-GDS? Lessons from Benchmarking Tool-Interactive EDA Workflows

<!-- claim:SF-2026-ARXIV-2607-17528:start -->Large language model (LLM) agents are extending electronic design automation (EDA) beyond static RTL generation toward long-horizon, tool-interactive workflows. Yet it remains unclear whether general-purpose coding agents, even with domain-specific EDA skills, can reliably execute an end-to-end RTL-to-GDS flow encompassing synthesis, physical implementation, and engineering change order (ECO) optimization. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-17528:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language model (LLM) agents are extending electronic design automation (EDA) beyond static RTL generation toward long-horizon, tool-interactive workflows.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Yet it remains unclear whether general-purpose coding agents, even with domain-specific EDA skills, can reliably execute an end-to-end RTL-to-GDS flow encompassing synthesis, physical implementation, and engineering change order (ECO) optimization.

**证据证明什么。** First, domain-specific skills improve agents' understanding of individual subtasks but do not ensure reliable completion of a long-horizon EDA flow.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.17528v1#S1 — 1. Introduction; https://arxiv.org/html/2607.17528v1#S2 — 2. Related Work。Evaluation：https://arxiv.org/html/2607.17528v1#A1.SS2 — A.2. Result Score; https://arxiv.org/html/2607.17528v1#S3 — 3. Benchmark Construction。Limitations / counterevidence：https://arxiv.org/html/2607.17528v1#S6 — 6. Conclusion。

**Artifact boundary。** Exact v1 links https://docs.anthropic.com/en/docs/claude-code/overview, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-17528:end -->

<!-- review:SF-2026-ARXIV-2607-17535:start -->
### Salience Induction against Multi-Hop RAG Agents: Threat and Defense

<!-- claim:SF-2026-ARXIV-2607-17535:start -->Agentic retrieval-augmented generation (RAG) systems increasingly retrieve external evidence and orchestrate tools for knowledge-intensive applications. In Multi-Hop question answering, agents chain facts across documents. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-17535:end -->

**为什么进入候选分母。** 摘要首要问题为“Agentic retrieval-augmented generation (RAG) systems increasingly retrieve external evidence and orchestrate tools for knowledge-intensive applications.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** Agentic retrieval-augmented generation (RAG) systems increasingly retrieve external evidence and orchestrate tools for knowledge-intensive applications.

**证据证明什么。** These results show that truthfulness and instruction filtering alone are insufficient: robust agentic RAG also requires defenses against salience-relevance decoupling.

**证据没有证明什么。** Agentic RAG systems should therefore scrutinize how evidence is presented, not only what it asserts. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.17535v1#S4 — 4. Attack Design; https://arxiv.org/html/2607.17535v1#S5.SS1 — 5.1. Design Goals。Evaluation：https://arxiv.org/html/2607.17535v1#A3 — Appendix C Additional Evaluation Results; https://arxiv.org/html/2607.17535v1#A9 — Appendix I Benchmark Construction Details。Limitations / counterevidence：https://arxiv.org/html/2607.17535v1#S10 — 10. Conclusion; https://arxiv.org/html/2607.17535v1#S2 — 2. Background and Threat Model。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Agentic RAG systems should therefore scrutinize how evidence is presented, not only what it asserts.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-RAG`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-17535:end -->

<!-- review:SF-2026-ARXIV-2607-17545:start -->
### Retain or Consolidate? Budget-Dependent Operator Selection for Language Agent Memory

<!-- claim:SF-2026-ARXIV-2607-17545:start -->Language agents depend on memory across interactions. However, the limited context windows of large language models (LLMs) and their inference costs constrain how much memory can be used at once. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-17545:end -->

**为什么进入候选分母。** 摘要首要问题为“Language agents depend on memory across interactions.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** Existing systems mainly follow two strategies: memory retention and memory consolidation.

**证据证明什么。** The public LongMemEval and LoCoMo benchmarks show the same budget-dependent pattern.

**证据没有证明什么。** Conclusion We formulate memory management as a joint, budget-dependent when–which decision. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.17545v1#Sx3 — Methodology。Evaluation：https://arxiv.org/html/2607.17545v1#A2 — Appendix B Reproducibility and Experimental Detail; https://arxiv.org/html/2607.17545v1#A2.SSx6 — Independently Split Full-History Four-Action Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.17545v1#Sx5 — Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：Conclusion We formulate memory management as a joint, budget-dependent when–which decision.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-17545:end -->

<!-- review:SF-2026-ARXIV-2607-17558:start -->
### Why Does Feedback-Augmented Self-Distillation Fail to Improve Retrieval-Interleaved Search Agents?

<!-- claim:SF-2026-ARXIV-2607-17558:start -->On-policy self-distillation (OPSD) offers a promising approach for training large language models without relying on a separate teacher model. However, its effectiveness on complex agentic tasks remains largely unexplored. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-17558:end -->

**为什么进入候选分母。** 摘要首要问题为“On-policy self-distillation (OPSD) offers a promising approach for training large language models without relying on a separate teacher model.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** To mitigate this inconsistency, we introduce an exponential moving average (EMA) teacher to stabilize the self-teacher and provide more consistent supervision signals.

**证据证明什么。** To understand its underlying cause, we show that although the self-teacher achieves stronger performance, learning remains inherently unstable due to inconsistent supervision signals.

**证据没有证明什么。** Fixed-reference and EMA teachers stabilize training but do not fully resolve this difficulty. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.17558v1#S3 — 3 Method; https://arxiv.org/html/2607.17558v1#A2 — Appendix B Training Variants and Implementation Details。Evaluation：https://arxiv.org/html/2607.17558v1#A3 — Appendix C Experimental Details; https://arxiv.org/html/2607.17558v1#A3.SS3 — C.3 Final Evaluation of EMA-Regularized FA-SD。Limitations / counterevidence：https://arxiv.org/html/2607.17558v1#S4.SS7 — 4.7 Discussion; https://arxiv.org/html/2607.17558v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Fixed-reference and EMA teachers stabilize training but do not fully resolve this difficulty.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-RAG`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-17558:end -->

<!-- review:SF-2026-ARXIV-2607-17568:start -->
### CoCurve: Cross-Module Co-Pruning Curvature for Training-Free Structured LLM Pruning

<!-- claim:SF-2026-ARXIV-2607-17568:start -->Structured pruning compresses large language models (LLMs) by removing whole computational units, such as attention heads and feed-forward (FFN) channel groups. Most training-free methods, however, rank these units independently, implicitly treating the loss from pruning a set as the sum of its individual losses. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-17568:end -->

**为什么进入候选分母。** 摘要首要问题为“Structured pruning compresses large language models (LLMs) by removing whole computational units, such as attention heads and feed-forward (FFN) channel groups.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** We introduce CoCurve (Cross-Module Co-Pruning Curvature), a calibration-only, fine-tuning-free method that prunes attention and FFN units jointly.

**证据证明什么。** Pruning then reduces to one budgeted quadratic program, solved in a single shot under a shared attention--FFN budget, with no labels, fine-tuning, or recovery.

**证据没有证明什么。** Crucially this is gated by a label-free calibration statistic and the method degrades to a strong diagonal selector in that regime ( Appendix T ), so the dependence bounds the edge benefit, not the method’s usability. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.17568v1#A13 — Appendix M Baseline Methods; https://arxiv.org/html/2607.17568v1#S2 — 2 Method。Evaluation：https://arxiv.org/html/2607.17568v1#A14 — Appendix N Evaluation Protocol; https://arxiv.org/html/2607.17568v1#A15 — Appendix O Full Per-Model Results。Limitations / counterevidence：https://arxiv.org/html/2607.17568v1#A24 — Appendix X Limitations; https://arxiv.org/html/2607.17568v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/GongZhiren/CoCurve, https://huggingface.co/blog/falcon3, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：Crucially this is gated by a label-free calibration statistic and the method degrades to a strong diagonal selector in that regime ( Appendix T ), so the dependence bounds the edge benefit, not the method’s usability.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`INFER-GPU-MEMORY`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-17568:end -->

<!-- review:SF-2026-ARXIV-2607-17572:start -->
### JAGG: Jacobian-Aggregated Group Gradient for Efficient GRPO Training of Diffusion Models

<!-- claim:SF-2026-ARXIV-2607-17572:start -->Group Relative Policy Optimization (GRPO) is a powerful reinforcement learning algorithm for aligning generative models with human preferences. While successful in large language models~\cite{shao2024deepseekmathpushinglimitsmathematical}, its extension to diffusion and flow matching models introduces a severe computational bottleneck: gradients must be back-propagated through the high-capacity DiT backbone at \emph{every} timestep of the sampling trajectory, making high-resolution text-to-image (T2I) training prohibitively expensive. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-17572:end -->

**为什么进入候选分母。** 摘要首要问题为“Group Relative Policy Optimization (GRPO) is a powerful reinforcement learning algorithm for aligning generative models with human preferences.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** Training-free DiT inference acceleration methods (e.g., $Δ$-DiT, ScalingCache) exploit the fact that DiT hidden states and velocity predictions vary \emph{smoothly and nearly linearly} along the trajectory.

**证据证明什么。** Experiments on T2I benchmarks show JAGG delivers $\sim$2$\times$ backward speedup with negligible quality degradation.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.17572v1#Sx3 — Method; https://arxiv.org/html/2607.17572v1#A3 — Appendix C JAGG Implementation Pseudocode。Evaluation：https://arxiv.org/html/2607.17572v1#A1 — Appendix A Experiment Figures; https://arxiv.org/html/2607.17572v1#A4 — Appendix D Experimental Setup and Hyperparameters。Limitations / counterevidence：https://arxiv.org/html/2607.17572v1#Sx5 — Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-GRPO`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-17572:end -->

<!-- review:SF-2026-ARXIV-2607-17574:start -->
### Predictive Training with Latent Imagination for Visual Quadruped Navigation

<!-- claim:SF-2026-ARXIV-2607-17574:start -->Reinforcement-learning navigation policies for legged robots select actions reactively from current observations and short-term memory, with limited capacity to anticipate how moving obstacles will evolve in the near future. In dynamic environments, this reactivity causes the robot to respond too late because collision risk depends on short-horizon scene structure rather than on current obstacle positions alone. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-17574:end -->

**为什么进入候选分母。** 摘要首要问题为“Reinforcement-learning navigation policies for legged robots select actions reactively from current observations and short-term memory, with limited capacity to anticipate how moving obstacles will evolve in the near future.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** On simulated and real-world navigation benchmarks with dynamic obstacles, our method substantially improves navigation success while reducing collision rates through the predictive training signal alone, without additional inference-time parameters.

**证据证明什么。** On simulated and real-world navigation benchmarks with dynamic obstacles, our method substantially improves navigation success while reducing collision rates through the predictive training signal alone, without additional inference-time parameters.

**证据没有证明什么。** Future work includes extending predictive supervision to longer rollout horizons for rare collision-critical events, and decomposing the recurrent state into task-relevant components to enable more structured dynamics learning. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.17574v1#S3 — 3 Method; https://arxiv.org/html/2607.17574v1#S4.SS2 — 4.2 Reward Design。Evaluation：https://arxiv.org/html/2607.17574v1#S5 — 5 Experiments; https://arxiv.org/html/2607.17574v1#S5.SS2 — 5.2 Ablation Study。Limitations / counterevidence：https://arxiv.org/html/2607.17574v1#S5.SS5 — 5.5 Discussion; https://arxiv.org/html/2607.17574v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Future work includes extending predictive supervision to longer rollout horizons for rare collision-critical events, and decomposing the recurrent state into task-relevant components to enable more structured dynamics learning.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-17574:end -->

<!-- review:SF-2026-ARXIV-2607-17575:start -->
### A Dual-Hypothesis Reasoning Framework for LLM Guardrails

<!-- claim:SF-2026-ARXIV-2607-17575:start -->We propose ARBITER, a novel LLM guardrail framework that introduces two key ideas: (i) dual-hypothesis reasoning, a reasoning method for LLM guardrails that explicitly considers both safe and unsafe interpretations of a prompt before making a safety decision, and (ii) multi-component supervised fine-tuning (MC-SFT), a structured training loss for reasoning-based guardrails that decomposes LLM outputs into logical components and weights them according to their importance. Existing reasoning-based guardrails often rely on expensive procedures, such as generating reasoning traces using larger or closed-source teacher models and applying full-parameter fine-tuning. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-17575:end -->

**为什么进入候选分母。** 摘要首要问题为“We propose ARBITER, a novel LLM guardrail framework that introduces two key ideas: (i) dual-hypothesis reasoning, a reasoning method for LLM guardrails that explicitly considers both safe and unsafe interpretations of a prompt before making a safety decision, and (ii) multi-component supervised fine-tuning (MC-SFT), a structured training loss for reasoning-based guardrails that decomposes LLM outputs into logical com”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** We propose ARBITER, a novel LLM guardrail framework that introduces two key ideas: (i) dual-hypothesis reasoning, a reasoning method for LLM guardrails that explicitly considers both safe and unsafe interpretations of a prompt before making a safety decision, and (ii) multi-component supervised fine-tuning (MC-SFT), a structured training loss for reasoning-based guardrails that decomposes LLM outputs into logical components and weights them according to their importance.

**证据证明什么。** Experiments on three safety moderation benchmarks show that ARBITER outperforms existing reasoning-based and non-reasoning guardrail baselines, with clear gains in out-of-domain evaluations.

**证据没有证明什么。** Limitations Our experiments focus on English safety moderation benchmarks with prompt-level safety labels and span-level explanation annotations. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.17575v1#S3 — 3 Proposed Method。Evaluation：https://arxiv.org/html/2607.17575v1#S5 — 5 Result Analysis; https://arxiv.org/html/2607.17575v1#A2 — Appendix B Faithfulness Analysis of Explanation Spans。Limitations / counterevidence：https://arxiv.org/html/2607.17575v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.17575v1#Sx1 — Limitations。

**Artifact boundary。** Exact v1 links https://anth2023.emnlp-demo.40/, https://dx.doi.org/10.18653/v1/2023.emnlp-demo.40, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Limitations Our experiments focus on English safety moderation benchmarks with prompt-level safety labels and span-level explanation annotations.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-17575:end -->

<!-- review:SF-2026-ARXIV-2607-17598:start -->
### Is Progressive Disclosure All You Need for Long-Context Agents?

<!-- claim:SF-2026-ARXIV-2607-17598:start -->Long-document question answering usually forces a choice between loading the whole document into the context window and bolting on a separate retriever. Agentic AI suggests a broader option, giving the agent the document path and letting it decide how and what to read. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-17598:end -->

**为什么进入候选分母。** 摘要首要问题为“Long-document question answering usually forces a choice between loading the whole document into the context window and bolting on a separate retriever.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** Agentic AI suggests a broader option, giving the agent the document path and letting it decide how and what to read.

**证据证明什么。** Progressive disclosure buys context, not intelligence: it is redundant while a strong agent can locate the right passages itself, and decisive once the corpus grows too large to navigate by reading.

**证据没有证明什么。** For packaging book-length material the guidance is concrete: package a book as one skill layered progressive disclosure, not as a multiple parallel packages of child skills with always-loaded description. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.17598v1#A1 — Appendix A Methodology details; https://arxiv.org/html/2607.17598v1#S3.SS2 — 3.2 The three approaches。Evaluation：https://arxiv.org/html/2607.17598v1#A3 — Appendix C Additional experimental results; https://arxiv.org/html/2607.17598v1#A2 — Appendix B Experimental setup。Limitations / counterevidence：https://arxiv.org/html/2607.17598v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.17598v1#Sx1 — Limitations。

**Artifact boundary。** Exact v1 links https://github.com/benchflow-ai/benchflow, https://www.latent.space/p/claude-code, https://github.com/yusufkaraaslan/Skill_Seekers; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：For packaging book-length material the guidance is concrete: package a book as one skill layered progressive disclosure, not as a multiple parallel packages of child skills with always-loaded description.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-CONTEXT`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-17598:end -->

<!-- review:SF-2026-ARXIV-2607-17619:start -->
### Insecure Coding Preferences in Long-Term Memory: Security Risks for LLM-based Code Generation

<!-- claim:SF-2026-ARXIV-2607-17619:start -->LLM-based systems increasingly incorporate long-term memory to improve cross-session continuity. However, once insecure coding preferences are stored, they may silently influence security-critical decisions in subsequent generations. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-17619:end -->

**为什么进入候选分母。** 摘要首要问题为“LLM-based systems increasingly incorporate long-term memory to improve cross-session continuity.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** LLM-based systems increasingly incorporate long-term memory to improve cross-session continuity.

**证据证明什么。** Our results show that insecure memories significantly increase the risk of generating vulnerable code by 2.7-50.3 percentage points (pp).

**证据没有证明什么。** Once the preference is stored as a long-term memory entry, it may be retrieved in later, independent sessions and silently influence security-critical implementation choices, even when the user does not explicitly repeat the preference in the current prompt. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.17619v1#S5 — 5. Study Design; https://arxiv.org/html/2607.17619v1#S2.SS1 — 2.1. Large Language Model-based Code Generation。Evaluation：https://arxiv.org/html/2607.17619v1#S5.SS3 — 5.3. Experimental Pipeline; https://arxiv.org/html/2607.17619v1#S5.SS4 — 5.4. Evaluation Metrics。Limitations / counterevidence：https://arxiv.org/html/2607.17619v1#S9 — 9. Conclusion and Future Work; https://arxiv.org/html/2607.17619v1#S4 — 4. Threat Model。

**Artifact boundary。** Exact v1 links https://github.com/filestack/filestack-python/blob/0e44e337e88051ade0b2873c600ada0744d10794/examples/intelligent_ingestion.py#L2, https://copilot.github.com/, https://codeql.github.com/; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Once the preference is stored as a long-term memory entry, it may be retrieved in later, independent sessions and silently influence security-critical implementation choices, even when the user does not explicitly repeat the preference in the current prompt.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-17619:end -->

<!-- review:SF-2026-ARXIV-2607-17621:start -->
### Mechanistic Attention Guidance for Agent Memory Refinement

<!-- claim:SF-2026-ARXIV-2607-17621:start -->Existing self-evolving memory systems mainly improve agent memory based on textual outputs, such as task trajectories and reflections. However, this text-based paradigm rarely incorporates internal mechanistic signals, leaving how retrieved memory is actually utilized during task execution underexplored. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-17621:end -->

**为什么进入候选分母。** 摘要首要问题为“Existing self-evolving memory systems mainly improve agent memory based on textual outputs, such as task trajectories and reflections.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** Building on this observation, we propose Attention-Guided Memory Refinement (AGMR), a framework that uses utilization patterns revealed by attention to guide targeted segment-level memory updates.

**证据证明什么。** Experiments on interactive decision-making benchmarks show that AGMR improves both task performance and memory efficiency over text-only memory refinement baselines.

**证据没有证明什么。** Another limitation is that the refinement pipeline is performed offline before evaluation. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.17621v1#A2 — Appendix B Algorithm of AGMR; https://arxiv.org/html/2607.17621v1#A5.SS3 — E.3 Other implementation details。Evaluation：https://arxiv.org/html/2607.17621v1#A3.SS3 — C.3 Ablation validation of retrieval heads; https://arxiv.org/html/2607.17621v1#A5 — Appendix E Experiments details。Limitations / counterevidence：https://arxiv.org/html/2607.17621v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://anonymous.4open.science/r/AGMR_code-3262/, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Another limitation is that the refinement pipeline is performed offline before evaluation.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-17621:end -->

<!-- review:SF-2026-ARXIV-2607-17624:start -->
### Can Transformers Really Do It All? On the Compatibility of Inductive Biases Across Tasks

<!-- claim:SF-2026-ARXIV-2607-17624:start -->Transformers are remarkably versatile and their design is largely consistent across a variety of applications. But are they optimal for any given task or dataset? 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-17624:end -->

**为什么进入候选分母。** 摘要首要问题为“Transformers are remarkably versatile and their design is largely consistent across a variety of applications.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** The answer may be key for pushing AI beyond merely scaling current designs. *Method.* We present a method to optimize a transformer architecture for a given dataset, which we use as a tool to study optimal task-specific inductive biases.

**证据证明什么。** Our results show that standard transformers are rarely a local optimum in the space of architectures.

**证据没有证明什么。** Complex forms of attention ( Hashemi et al., 2025 ) or interactions like gated linear units (GLU, Shazeer 2020 ) cannot be represented in our formulation. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.17624v1#S2 — 2 Proposed Method to Optimize Architectures; https://arxiv.org/html/2607.17624v1#S3.SS2 — 3.2 Compatibility of Optimized Architectures Across Algorithmic Tasks。Evaluation：https://arxiv.org/html/2607.17624v1#A3 — Appendix C Additional Results on Algorithmic Tasks; https://arxiv.org/html/2607.17624v1#A4 — Appendix D Additional Results on Language Modeling。Limitations / counterevidence：https://arxiv.org/html/2607.17624v1#S6 — 6 Discussion。

**Artifact boundary。** Exact v1 links https://github.com/idiap/lm-afs, https://huggingface.co/microsoft/CodeGPT-small-py, https://github.com/KellerJordan/modded-nanogpt; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Complex forms of attention ( Hashemi et al., 2025 ) or interactions like gated linear units (GLU, Shazeer 2020 ) cannot be represented in our formulation.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MODEL-TRANSFORMER-LAYER`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-17624:end -->

<!-- review:SF-2026-ARXIV-2607-17641:start -->
### Verify, Repair, Repeat, or Stop? Robust Stopping for Noisy Verify-Repair Loops in LLM Agents

<!-- claim:SF-2026-ARXIV-2607-17641:start -->Verify-repair loops are a standard means for large language model (LLM) agents to correct faulty plans in code generation, mathematical reasoning, and tool use. When both the verifier and the repairer are noisy, repair can damage already-correct plans, and reported acceptance keeps rising while true validity falls, so existing methods lack a principled basis for deciding when repair should stop. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-17641:end -->

**为什么进入候选分母。** 摘要首要问题为“Verify-repair loops are a standard means for large language model (LLM) agents to correct faulty plans in code generation, mathematical reasoning, and tool use.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** We propose VRR-Stop, a robust stopping framework for noisy verify-repair-repeat (VRR) loops.

**证据证明什么。** On a GSM8K stress setting, VRR-Stop improves final true validity by 60.6 percentage points over fixed five-round repair at an average cost of 0.72 repair rounds.

**证据没有证明什么。** All of these are raw-label statistics, independent of the stopping rule and its calibration. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.17641v1#S4 — 4 Method; https://arxiv.org/html/2607.17641v1#A1 — Appendix A Derivations, Algorithms, and Reference Policies。Evaluation：https://arxiv.org/html/2607.17641v1#A4 — Appendix D Full Stopping and Cross-Benchmark Results; https://arxiv.org/html/2607.17641v1#A1.SS3 — A.3 Proof and Numerical Evaluation of Lemma 1。Limitations / counterevidence：https://arxiv.org/html/2607.17641v1#A3 — Appendix C Full Loop Dynamics and Failure Cases; https://arxiv.org/html/2607.17641v1#A3.SS2 — C.2 A Representative Failure Trace。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：All of these are raw-label statistics, independent of the stopping rule and its calibration.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-REFLECTION`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-17641:end -->

<!-- review:SF-2026-ARXIV-2607-17644:start -->
### A Training-Memory Regression in MLA Sequence Parallelism: Why Megatron-Core Forbids Absorption, and LAGA -- a Communication-Efficient Fix

<!-- claim:SF-2026-ARXIV-2607-17644:start -->Multi-head Latent Attention (MLA) ships two implementations in Megatron-Core: an explicit form used for training and an absorbed form -- which slashes collective communication by gathering only the compressed latent -- that is fully implemented but hard-asserted out of training (the forward opens with "assert not (self.training and self.cache_mla_latents)"), allowed only in inference decode. We show the restriction is well-founded and quantify why: ported to training, the absorbed form is a memory trap -- its intermediates live in n_h x d_kv dimensions per token, larger than the per-head K/V they replace -- inflating activation memory by 20-34%, up to 9.2 GB at DeepSeek-V3 scale (n_h=128, seq=16384, SP=8, eager kernel; the gap widens to 19.2 GB under a fused kernel), enough to change device-fit. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-17644:end -->

**为什么进入候选分母。** 摘要首要问题为“Multi-head Latent Attention (MLA) ships two implementations in Megatron-Core: an explicit form used for training and an absorbed form -- which slashes collective communication by gathering only the compressed latent -- that is fully implemented but hard-asserted out of training (the forward opens with "assert not (self.training and self.cache_mla_latents)"), allowed only in inference decode.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** We show the restriction is well-founded and quantify why: ported to training, the absorbed form is a memory trap -- its intermediates live in n_h x d_kv dimensions per token, larger than the per-head K/V they replace -- inflating activation memory by 20-34%, up to 9.2 GB at DeepSeek-V3 scale (n_h=128, seq=16384, SP=8, eager kernel; the gap widens to 19.2 GB under a fused kernel), enough to change device-fit.

**证据证明什么。** On 8x Ascend 910B at real DeepSeek-V3 dimensions, LAGA cuts collective communication 1.98x, matches explicit memory within 0.5%, is bit-identical to explicit at SP=1 and equivalent to within 1e-3 at SP=2-8, and under a fused attention kernel improves attention-block throughput 1.04-1.06x single-node and 1.07-1.24x cross-node -- leading at all sequence lengths in the cross-node regime MLA is deployed for.

**证据没有证明什么。** Comm is per-layer and analytical, and the memory-trap mechanism ( intermediates) is structural and independent of depth; however, end-to-end wall-clock and MFU at full model depth (where attention’s share of total compute is smaller) remain future work. • Convergence at toy scale. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.17644v1#S1 — 1 Introduction; https://arxiv.org/html/2607.17644v1#S2 — 2 Background。Evaluation：https://arxiv.org/html/2607.17644v1#S4 — 4 Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.17644v1#S8 — 8 Discussion and Limitations; https://arxiv.org/html/2607.17644v1#S4.SS7 — 4.7 Limitations and scope。

**Artifact boundary。** Exact v1 links https://github.com/NVIDIA/Megatron-LM, https://github.com/deepseek-ai/DeepEP, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：Comm is per-layer and analytical, and the memory-trap mechanism ( intermediates) is structural and independent of depth; however, end-to-end wall-clock and MFU at full model depth (where attention’s share of total compute is smaller) remain future work. • Convergence at toy scale.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`TRAIN-TENSOR-PARALLEL`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-17644:end -->

<!-- review:SF-2026-ARXIV-2607-17652:start -->
### FlowBlock: Wavefront-Parallel Decoding for Self-Correcting Diffusion Language Models

<!-- claim:SF-2026-ARXIV-2607-17652:start -->Block-wise diffusion large language models (dLLMs) decode sequentially at the block level, enabling effective KV-cache reuse across blocks but making inter-block decoding strictly serial. Prior work has attempted to unlock inter-block parallelism through post-training methods, but achieves only modest speedups and often degrades accuracy. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-17652:end -->

**为什么进入候选分母。** 摘要首要问题为“Block-wise diffusion large language models (dLLMs) decode sequentially at the block level, enabling effective KV-cache reuse across blocks but making inter-block decoding strictly serial.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** We propose \textbf{\flowblock{}}, a training-free parallel decoding framework built on two mechanisms. (i) \emph{Gated Wavefront Decoding} admits blocks into a bounded wavefront only when a readiness gate is satisfied, jointly refines active blocks via T2T editing, and commits blocks in order under a windowed block-causal mask that preserves exact frozen-prefix KV caches reuse. (ii) \emph{Heterogeneous Wavefront Packing} assigns each request an independent wavefront while packing asynchronous windows into dense, shape-stable batched forwards.

**证据证明什么。** It also improves average accuracy by 1.3 points.

**证据没有证明什么。** Its key insight is that T2T self-correction relaxes inter-block dependencies, turning block finality from a strict prerequisite into a scheduling decision. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.17652v1#S4 — 4 FlowBlock Framework。Evaluation：https://arxiv.org/html/2607.17652v1#S5 — 5 Evaluation; https://arxiv.org/html/2607.17652v1#S5.SS1 — 5.1 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.17652v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Its key insight is that T2T self-correction relaxes inter-block dependencies, turning block finality from a strict prerequisite into a scheduling decision.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-GENERATIVE-PARADIGMS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-17652:end -->

<!-- review:SF-2026-ARXIV-2607-17673:start -->
### Beyond Objective Expressivity: Geometry Preservation in Multimodal Contrastive Learning

<!-- claim:SF-2026-ARXIV-2607-17673:start -->Contrastive learning is increasingly moving toward settings with three or more modalities instead of image-text pairs. Yet, extending models from pairwise to higher-order multimodal alignment can introduce optimization and representation challenges. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-17673:end -->

**为什么进入候选分母。** 摘要首要问题为“Contrastive learning is increasingly moving toward settings with three or more modalities instead of image-text pairs.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We introduce geometry-preserving encoders (GPEs) by directly conditioning the Jacobian through regularization and demonstrating that simple modifications like LeakyReLU activations and residual paths recover these geometric benefits.

**证据证明什么。** More broadly, our results show that multimodal contrastive learning depends not only on objective expressivity, but also on the geometric and optimization properties of the underlying encoders.

**证据没有证明什么。** 5 Conclusion, Limitations & Future Work We showed that multimodal contrastive learning depends strongly on encoder Jacobian conditioning. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.17673v1#S3 — 3 Method。Evaluation：https://arxiv.org/html/2607.17673v1#S4 — 4 Experiments; https://arxiv.org/html/2607.17673v1#S4.SS2 — 4.2 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.17673v1#S5 — 5 Conclusion, Limitations & Future Work。

**Artifact boundary。** Exact v1 links https://github.com/TillmannRheude/gpe, https://github.com/Lightning-AI/lightning, http://github.com/google-research/tuning_playbook; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：5 Conclusion, Limitations & Future Work We showed that multimodal contrastive learning depends strongly on encoder Jacobian conditioning.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-REPRESENTATION`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-17673:end -->

<!-- review:SF-2026-ARXIV-2607-17696:start -->
### An Adjoint-Sensitivity Framework for Lost-in-the-Middle Phenomena in Causal Residual Transformers

<!-- claim:SF-2026-ARXIV-2607-17696:start -->We develop an adjoint-sensitivity framework for positional influence in causal residual Transformers and separate unconditional analytic results from conditional boundary-shape conclusions. The principal unconditional theorem is the residual-to-depth-flow estimate for layer controls converging in $L^1$, complemented by a finite-token-to-Volterra attention estimate that explicitly controls the first cells near the causal endpoint. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-17696:end -->

**为什么进入候选分母。** 摘要首要问题为“We develop an adjoint-sensitivity framework for positional influence in causal residual Transformers and separate unconditional analytic results from conditional boundary-shape conclusions.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We develop an adjoint-sensitivity framework for positional influence in causal residual Transformers and separate unconditional analytic results from conditional boundary-shape conclusions.

**证据证明什么。** We develop an adjoint-sensitivity framework for positional influence in causal residual Transformers and separate unconditional analytic results from conditional boundary-shape conclusions.

**证据没有证明什么。** The paper does not prove that causal masking and residual connections universally generate Lost-in-the-Middle. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.17696v1#S3.SS8 — 3.8 Computational complexity of Algorithms 1 and 3; https://arxiv.org/html/2607.17696v1#S4.SS1 — 4.1 Simulation model and metrics。Evaluation：https://arxiv.org/html/2607.17696v1#S4.SS3 — 4.3 Running results。Limitations / counterevidence：https://arxiv.org/html/2607.17696v1#S5 — 5 Conclusion and limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：The paper does not prove that causal masking and residual connections universally generate Lost-in-the-Middle.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MODEL-LONG-CONTEXT`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-17696:end -->

<!-- review:SF-2026-ARXIV-2607-17701:start -->
### ProEvent: An Event-centric Benchmark for Proactive Agents

<!-- claim:SF-2026-ARXIV-2607-17701:start -->Proactive agents are expected to anticipate user needs and provide autonomous assistance by perceiving environmental context without explicit instructions. A fundamental capability of such agents is to identify and track users' upcoming events, enabling continuous and event-specific assistance. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-17701:end -->

**为什么进入候选分母。** 摘要首要问题为“Proactive agents are expected to anticipate user needs and provide autonomous assistance by perceiving environmental context without explicit instructions.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** To bridge these gaps, we introduce ProEvent, the first event-centric benchmark designed to assess an agent's ability to proactively maintain a user's timetable based on ongoing instant messaging chats.

**证据证明什么。** Further qualitative analysis reveals fundamental limitations of current LLMs as proactive agents, particularly in detecting implicit events and reasoning from the user's first-person perspective.

**证据没有证明什么。** We hope that ProEvent will facilitate future research on enhancing LLMs’ capabilities for proactive event tracking in real-world settings. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.17701v1#S1 — 1 Introduction; https://arxiv.org/html/2607.17701v1#S2 — 2 Related Work。Evaluation：https://arxiv.org/html/2607.17701v1#S5.SS1 — 5.1 Results Analysis; https://arxiv.org/html/2607.17701v1#A3 — Appendix C ProEvent Realism Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.17701v1#S5.SS2 — 5.2 Discussion; https://arxiv.org/html/2607.17701v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/volcengine/MineContext, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：We hope that ProEvent will facilitate future research on enhancing LLMs’ capabilities for proactive event tracking in real-world settings.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-17701:end -->

<!-- review:SF-2026-ARXIV-2607-17710:start -->
### Planning with Transformers: Chain of Computation and Structured Context Windows

<!-- claim:SF-2026-ARXIV-2607-17710:start -->Large Language Models (LLMs) have had a remarkable impact across many areas of machine learning. However, recent studies have shown that they struggle to reliably solve planning problems. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-17710:end -->

**为什么进入候选分母。** 摘要首要问题为“Large Language Models (LLMs) have had a remarkable impact across many areas of machine learning.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We propose Chain of Computation (COC), a computational architecture that places a transformer-based LM inside an iterative loop, leveraging its strength as a pattern-matching system.

**证据证明什么。** At the same time, theoretical results have shown that transformers, the core architecture underlying modern LLMs, are Turing-complete.

**证据没有证明什么。** We later show that planning for TOH does not require pointers and that the only operations needed on the SCW are push and pop. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.17710v1#S3 — 3 The Chain of Computation (COC) Architecture。Evaluation：https://arxiv.org/html/2607.17710v1#A1 — Appendix A Experimental Setup; https://arxiv.org/html/2607.17710v1#A8 — Appendix H Extended Training Scaling Results。Limitations / counterevidence：https://arxiv.org/html/2607.17710v1#S7 — 7 Conclusion and Future Work; https://arxiv.org/html/2607.17710v1#S6 — 6 Discussion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：We later show that planning for TOH does not require pointers and that the only operations needed on the SCW are push and pop.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-PLANNING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-17710:end -->

<!-- review:SF-2026-ARXIV-2607-17715:start -->
### C$^2$KV: Compressed and Composable KV Cache Reuse for Efficient LLM Inference

<!-- claim:SF-2026-ARXIV-2607-17715:start -->Long-context inference is central to modern large language model (LLM) applications such as retrieval-augmented generation and multi-document reasoning. To mitigate the growing inference cost, recent work has explored key-value (KV) cache reuse to reduce redundant prefill computation. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-17715:end -->

**为什么进入候选分母。** 摘要首要问题为“Long-context inference is central to modern large language model (LLM) applications such as retrieval-augmented generation and multi-document reasoning.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** In this work, we propose C$^2$KV, a unified framework for non-prefix KV reuse that jointly optimizes KV extraction and inference-time concatenation.

**证据证明什么。** Extensive experiments across multiple long-context benchmarks and model families demonstrate that C$^2$KV significantly reduces KV cache storage and transfer costs, achieving up to 17$\times$ inference speedup under long contexts, while preserving generation quality.

**证据没有证明什么。** Limitations of Existing Reuse Methods Despite their potential, both categories of methods face critical bottlenecks that prevent efficient and lossless serving. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.17715v1#A3.SS2 — C.2. Method-Specific TTFT Components; https://arxiv.org/html/2607.17715v1#S2.SS3 — 2.3. Limitations of Existing Reuse Methods。Evaluation：https://arxiv.org/html/2607.17715v1#A2.SS2 — B.2. Evaluation Setup; https://arxiv.org/html/2607.17715v1#A4 — Appendix D Full Results。Limitations / counterevidence：https://arxiv.org/html/2607.17715v1#A5 — Appendix E Limitations and Future Work; https://arxiv.org/html/2607.17715v1#S2.SS3 — 2.3. Limitations of Existing Reuse Methods。

**Artifact boundary。** Exact v1 links https://github.com/s7a9/C2KV, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Limitations of Existing Reuse Methods Despite their potential, both categories of methods face critical bottlenecks that prevent efficient and lossless serving.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-KV-CACHE`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-17715:end -->

<!-- review:SF-2026-ARXIV-2607-17733:start -->
### MXSens: Sensitivity-Aware Mixed-Precision Quantization for Efficient LLM Inference

<!-- claim:SF-2026-ARXIV-2607-17733:start -->4-bit quantization enables efficient LLM inference, but suffers from significant accuracy degradation due to outliers. Prior work addresses this problem via data rotation or mixed-precision integer quantization, but often relies on software-managed scaling and frequent dequantization, incurring substantial overhead. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-17733:end -->

**为什么进入候选分母。** 摘要首要问题为“4-bit quantization enables efficient LLM inference, but suffers from significant accuracy degradation due to outliers.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** We introduce MXSens, a training-free method that assigns mixed mantissa bitwidths (4/6/8) based on column- and layer-wise sensitivity, naturally leveraging the block-wise structure of MXINT.

**证据证明什么。** MXSens outperforms state-of-the-art quantization methods across a range of models and tasks.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.17733v1#A1.SS1 — A.1 Language Model Usage in the Paper。Evaluation：https://arxiv.org/html/2607.17733v1#A1.SS10 — A.10 Additional Results for the Ablation Study; https://arxiv.org/html/2607.17733v1#S5 — 5 Experimental Results。Limitations / counterevidence：https://arxiv.org/html/2607.17733v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/parsa-epfl/mxsens, https://huggingface.co/datasets/wikitext/tree/main, https://huggingface.co/meta-llama/Meta-Llama-3-8B; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-GPU-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-17733:end -->

<!-- review:SF-2026-ARXIV-2607-17751:start -->
### MagicSelector: Joint Optimization for Agent Tool Selection via Counterfactual Decomposition and Progressive Reranking

<!-- claim:SF-2026-ARXIV-2607-17751:start -->We present MagicSelector, a joint optimization framework integrating Counterfactual task decomposition, Progressive reranking, and Dynamic Top-K, designed to address the fundamental challenges of tool retrieval in agents. MagicSelector is a specialized framework capable of translating ambiguous user instructions into executable atomic subtasks and guiding high-precision tool retrieval, effectively mitigating redundant noise and severe context distraction in out-of-domain (OOD) scenarios. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-17751:end -->

**为什么进入候选分母。** 摘要首要问题为“We present MagicSelector, a joint optimization framework integrating Counterfactual task decomposition, Progressive reranking, and Dynamic Top-K, designed to address the fundamental challenges of tool retrieval in agents.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We present MagicSelector, a joint optimization framework integrating Counterfactual task decomposition, Progressive reranking, and Dynamic Top-K, designed to address the fundamental challenges of tool retrieval in agents.

**证据证明什么。** Extensive experiments demonstrate that MagicSelector significantly outperforms state-of-the-art methods in terms of tool retrieval accuracy, OOD generalization capability, and overall token efficiency, thereby demonstrating the effectiveness of our proposed framework.

**证据没有证明什么。** We believe this work not only provides a robust solution for high-precision tool retrieval in complex mobile assistant scenarios but also offers a scalable and effective paradigm for developing autonomous agents capable of navigating ambiguous, open-ended real-world environments. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.17751v1#S3.SS1 — 3.1 Dataset Construction via a State-Machine-Driven Framework; https://arxiv.org/html/2607.17751v1#S3.SS3 — 3.3 Preference Reward Modeling。Evaluation：https://arxiv.org/html/2607.17751v1#S6.SS1 — 6.1 Evaluation Benchmarks; https://arxiv.org/html/2607.17751v1#S2.SS2 — 2.2 Benchmarks for Tool Retrieval。Limitations / counterevidence：https://arxiv.org/html/2607.17751v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://huggingface.co/Alibaba-NLP/gte-Qwen2-7B-instruct, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：We believe this work not only provides a robust solution for high-precision tool retrieval in complex mobile assistant scenarios but also offers a scalable and effective paradigm for developing autonomous agents capable of navigating ambiguous, open-ended real-world environments.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-TOOL-CALLING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-17751:end -->

<!-- review:SF-2026-ARXIV-2607-17780:start -->
### ETAS: An Effect-Typed Language for Agent Systems

<!-- claim:SF-2026-ARXIV-2607-17780:start -->ETAS is a programming language for agent systems that treats model-backed agents, tool calls, prompts, typed memory, human approvals, policies, and execution traces as semantic program elements rather than library conventions. It separates deterministic computation from agentic nondeterminism and externally visible actions while preserving a direct programming style. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-17780:end -->

**为什么进入候选分母。** 摘要首要问题为“ETAS is a programming language for agent systems that treats model-backed agents, tool calls, prompts, typed memory, human approvals, policies, and execution traces as semantic program elements rather than library conventions.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** ETAS is a programming language for agent systems that treats model-backed agents, tool calls, prompts, typed memory, human approvals, policies, and execution traces as semantic program elements rather than library conventions.

**证据证明什么。** ETAS provides a programming-language foundation for reasoning about authorization, nondeterminism, recovery, and audit evidence before and during agent execution.

**证据没有证明什么。** The broader conclusion is that agent-system safety and auditability need not be recovered from callbacks and logs after the fact: they can be made part of the language interface that programmers write, compilers check, and runtimes enforce. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.17780v1#S3.SS3 — 3.3. Design Restrictions; https://arxiv.org/html/2607.17780v1#S7 — 7. Implementation。Evaluation：https://arxiv.org/html/2607.17780v1#S5.SS1 — 5.1. Expression Evaluation; https://arxiv.org/html/2607.17780v1#S8 — 8. Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.17780v1#S10 — 10. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/etas-project/etas, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：The broader conclusion is that agent-system safety and auditability need not be recovered from callbacks and logs after the fact: they can be made part of the language interface that programmers write, compilers check, and runtimes enforce.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-PLATFORM`；evidence-stage relation：`structural_candidate`。
- Books 候选路由（尚非最终决定）：`Structural Candidate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-17780:end -->

<!-- review:SF-2026-ARXIV-2607-17786:start -->
### Reasoning as a Double-Edged Sword: Architecture and Cross-Stage Robustness in Vision-Language-Action Models

<!-- claim:SF-2026-ARXIV-2607-17786:start -->Does adding a reasoning step make a Vision-Language-Action (VLA) model more robust to perturbation? Intuitively, a policy that reasons before acting should absorb a perturbed input better than one that maps observations directly to actions. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-17786:end -->

**为什么进入候选分母。** 摘要首要问题为“Does adding a reasoning step make a Vision-Language-Action (VLA) model more robust to perturbation?”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Intuitively, a policy that reasons before acting should absorb a perturbed input better than one that maps observations directly to actions.

**证据证明什么。** We find that the latent-iterative model is by far the least robust: under both stochastic noise and white-box perturbation its task success collapses, while the other two hold.

**证据没有证明什么。** 6 Discussion and conclusion We do not propose a defense. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.17786v1#S4 — 4 Cross-stage robustness across reasoning architectures; https://arxiv.org/html/2607.17786v1#A15 — Appendix O LIBERO-Plus naturalistic-perturbation cross-benchmark: per-(model, factor) details。Evaluation：https://arxiv.org/html/2607.17786v1#A11 — Appendix K Amplification analysis: full results; https://arxiv.org/html/2607.17786v1#A13 — Appendix M CoT-disabled ablation: full results。Limitations / counterevidence：https://arxiv.org/html/2607.17786v1#S6 — 6 Discussion and conclusion; https://arxiv.org/html/2607.17786v1#A16 — Appendix P Limitations (extended)。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：6 Discussion and conclusion We do not propose a defense.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-17786:end -->

<!-- review:SF-2026-ARXIV-2607-17843:start -->
### Mobius Learning: Cyclic Depth Folding in Transformers

<!-- claim:SF-2026-ARXIV-2607-17843:start -->Transformer-based language models organize computation along an ordered depth axis, where shallow and deep blocks often develop distinct representational roles. We challenge the conventional view that these roles must remain tied to a block's position in the ordered sequence. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-17843:end -->

**为什么进入候选分母。** 摘要首要问题为“Transformer-based language models organize computation along an ordered depth axis, where shallow and deep blocks often develop distinct representational roles.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We introduce Mobius Learning, a training architecture based on cyclic depth folding, in which different data streams follow cyclically shifted block orders.

**证据证明什么。** This counterintuitive result shows that a block group need not remain confined to one fixed shallow or deep role within the block sequence and opens a new design space based on cyclic depth folding.

**证据没有证明什么。** 5 Next Version and Future Work The next version will broaden the current four-worker scaling study. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.17843v1#S2 — 2 Methodology; https://arxiv.org/html/2607.17843v1#A1 — Appendix A Implementation Notes。Evaluation：https://arxiv.org/html/2607.17843v1#S2.SS4 — 2.4 Training and Evaluation Objectives; https://arxiv.org/html/2607.17843v1#S3 — 3 Main Results。Limitations / counterevidence：https://arxiv.org/html/2607.17843v1#S5 — 5 Next Version and Future Work。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：5 Next Version and Future Work The next version will broaden the current four-worker scaling study.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MODEL-TRANSFORMER-LAYER`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-17843:end -->

<!-- review:SF-2026-ARXIV-2607-17879:start -->
### Exploratory and Assimilating Reflection: Reflective Recall Cycle for Long-term Memory

<!-- claim:SF-2026-ARXIV-2607-17879:start -->LLM-based autonomous agents require external memory to overcome their statelessness and limited context window for long-term interaction and dynamic knowledge reasoning. However, existing memory retrieval methods often lack adaptability and sample efficiency, and struggle to retrieve the right mixture of memories from heterogeneous stores. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-17879:end -->

**为什么进入候选分母。** 摘要首要问题为“LLM-based autonomous agents require external memory to overcome their statelessness and limited context window for long-term interaction and dynamic knowledge reasoning.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We propose Exploratory-Assimilating Reflection (EAR), a framework for high initial retrieval performance and sample-efficient adaptation.

**证据证明什么。** Experiments show that EAR improves retrieval by up to 17.9% over the baseline retriever on two long-term dialogue benchmarks.

**证据没有证明什么。** Limitations While this work demonstrates a promising direction, we acknowledge several limitations that open avenues for future research. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.17879v1#S3 — 3 Methodology; https://arxiv.org/html/2607.17879v1#S3.SS2 — 3.2 EAR Framework。Evaluation：https://arxiv.org/html/2607.17879v1#S4.SS5 — 4.5 Results and Analysis; https://arxiv.org/html/2607.17879v1#S5.SS2 — 5.2 Results and Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.17879v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.17879v1#Sx1 — Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Limitations While this work demonstrates a promising direction, we acknowledge several limitations that open avenues for future research.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-17879:end -->

<!-- review:SF-2026-ARXIV-2607-17884:start -->
### ST-Veto: Spatio-Temporal Token Veto for Diffusion MLLMs via Taylor Prediction and Visual Grounding

<!-- claim:SF-2026-ARXIV-2607-17884:start -->Vision Language Models (VLMs) achieve strong reasoning with Chain-of-Thought (CoT) prompting but incur high sequential-generation cost, error accumulation, and limited self-correction. Diffusion Multimodal Large Language Models (dMLLMs) unmask tokens in an order-agnostic process, improving efficiency and enabling iterative refinement, yet their reasoning and how to enhance it remain underexplored. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-17884:end -->

**为什么进入候选分母。** 摘要首要问题为“Vision Language Models (VLMs) achieve strong reasoning with Chain-of-Thought (CoT) prompting but incur high sequential-generation cost, error accumulation, and limited self-correction.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** We propose a training-free method, Spatio-Temporal Token Veto (ST-Veto), which leverages the ability to observe all token positions at each diffusion step.

**证据证明什么。** Analyses show that ST-Veto steers generation toward higher-confidence, better-grounded paths.

**证据没有证明什么。** A.9 Limitations and Future Work ST-Veto relies on internal confidence and attention signals, which are useful but imperfect proxies. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.17884v1#S3 — 3 Method; https://arxiv.org/html/2607.17884v1#S6.SS1 — 6.1 Methodological Analysis。Evaluation：https://arxiv.org/html/2607.17884v1#A1 — Appendix A Additional Experiments and Analyses; https://arxiv.org/html/2607.17884v1#A1.SS1 — A.1 Prompt Configurations and Experimental Settings。Limitations / counterevidence：https://arxiv.org/html/2607.17884v1#A1.SS9 — A.9 Limitations and Future Work; https://arxiv.org/html/2607.17884v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：A.9 Limitations and Future Work ST-Veto relies on internal confidence and attention signals, which are useful but imperfect proxies.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-GENERATIVE-PARADIGMS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-17884:end -->

<!-- review:SF-2026-ARXIV-2607-17914:start -->
### Value-Aware Prediction for Robust Multi-Agent Coordination Under Communication Loss

<!-- claim:SF-2026-ARXIV-2607-17914:start -->Robust multi-agent coordination relies heavily on inter-agent communication, which is frequently disrupted by physical and environmental constraints in real-world deployments. To maintain operation during these intermittent communication failures, agents can employ internal prediction models to estimate missing shared state information. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-17914:end -->

**为什么进入候选分母。** 摘要首要问题为“Robust multi-agent coordination relies heavily on inter-agent communication, which is frequently disrupted by physical and environmental constraints in real-world deployments.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** In this paper, we propose a value-aware extension of Multi-Agent Observation Sharing under Communication Dropout (MARO) to patch communication gaps; we refer to this method as Value-Aware MARO.

**证据证明什么。** In these environments, our method achieves an average improvement in mean returns of more than 20% and reduces performance variance by a mean of 64.7% compared to the standard unweighted baseline.

**证据没有证明什么。** Extending the framework to larger teams, temporally correlated or bandwidth-limited communication, and more complex environments remains an open direction. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.17914v1#S3.SS2 — III-B Actor-Critic Architecture in MARL; https://arxiv.org/html/2607.17914v1#S4 — IV Methodology。Evaluation：https://arxiv.org/html/2607.17914v1#A3 — Appendix C Extended Experimental Results; https://arxiv.org/html/2607.17914v1#S5.SS2 — V-B Results and Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.17914v1#S6 — VI Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/robust-comm-marl-IROS2026/Value-Aware-Prediction-Under-Communication-Loss, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Extending the framework to larger teams, temporally correlated or bandwidth-limited communication, and more complex environments remains an open direction.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MULTI-AGENT`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-17914:end -->

<!-- review:SF-2026-ARXIV-2607-17924:start -->
### Aggregate in the Advantage, Not the Ratio: A Canonical-Form Analysis of Cooperative Multi-Agent Policy Optimization

<!-- claim:SF-2026-ARXIV-2607-17924:start -->Multi-agent policy optimization, exemplified by PPO-based methods, is a key branch of cooperative Multi-Agent Reinforcement Learning (MARL). A central design question is how many neighboring agents\footnote{In this paper, "neighbors" refer not only to physical proximity but also to agents whose actions influence one another.} to aggregate in order to effectively utilize global information for cooperation. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-17924:end -->

**为什么进入候选分母。** 摘要首要问题为“Multi-agent policy optimization, exemplified by PPO-based methods, is a key branch of cooperative Multi-Agent Reinforcement Learning (MARL).”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** Multi-agent policy optimization, exemplified by PPO-based methods, is a key branch of cooperative Multi-Agent Reinforcement Learning (MARL).

**证据证明什么。** The resulting design principle is unambiguous: aggregate neighbors in the advantage, sized to the coupling neighborhood, and keep the ratio per-agent.

**证据没有证明什么。** Our analysis reveals that the expected policy gradient depends on these supports only through their matrix product , establishing a gauge freedom that renders the two supports mutually redundant in terms of the gradient signal. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.17924v1#S1 — 1 Introduction; https://arxiv.org/html/2607.17924v1#S2 — 2 Preliminaries。Evaluation：https://arxiv.org/html/2607.17924v1#A3 — Appendix C Experimental Details and Additional Results; https://arxiv.org/html/2607.17924v1#S4.SS2 — 4.2 Experiment Results。Limitations / counterevidence：https://arxiv.org/html/2607.17924v1#A5 — Appendix E Discussion; https://arxiv.org/html/2607.17924v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/RS2002/MAPO, https://github.com/LucasAlegre/sumo-rl, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Our analysis reveals that the expected policy gradient depends on these supports only through their matrix product , establishing a gauge freedom that renders the two supports mutually redundant in terms of the gradient signal.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-GRPO`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-17924:end -->

<!-- review:SF-2026-ARXIV-2607-17937:start -->
### When and How Context Rot Appears in Coding Agents: A White-Box Study of Agent Skills in Code Auditing

<!-- claim:SF-2026-ARXIV-2607-17937:start -->Agent Skills package procedural instructions and checks for use by general-purpose agents, but loading a skill does not guarantee that every requirement remains active throughout a long tool-using trajectory. We study this problem in a production-derived, white-box code-audit workflow. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-17937:end -->

**为什么进入候选分母。** 摘要首要问题为“Agent Skills package procedural instructions and checks for use by general-purpose agents, but loading a skill does not guarantee that every requirement remains active throughout a long tool-using trajectory.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We do not introduce context rot or a new general monitoring method; we provide a bounded failure classification and empirical case study for white-box code auditing.

**证据证明什么。** Requirement coverage nevertheless stays above 92% in both long conditions, showing that a few omissions can invalidate an otherwise complete artifact.

**证据没有证明什么。** Coding begins only after the frozen checker has assigned PASS or FAIL. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.17937v1#S3 — 3 White-Box Study Design; https://arxiv.org/html/2607.17937v1#S3.SS1 — 3.1 Design Goals。Evaluation：https://arxiv.org/html/2607.17937v1#A2.SS2 — B.2 Experimental Matrix; https://arxiv.org/html/2607.17937v1#S4.SS4 — 4.4 Statistical Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.17937v1#A1 — Appendix A Failure-Coding Guide; https://arxiv.org/html/2607.17937v1#S2.SS4 — 2.4 Visible Failure Locations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Coding begins only after the frozen checker has assigned PASS or FAIL.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-CONTEXT`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-17937:end -->

<!-- review:SF-2026-ARXIV-2607-17973:start -->
### SAGE: Subgoal-Conditioned Action Generation for Latent World Model Planning

<!-- claim:SF-2026-ARXIV-2607-17973:start -->Latent world models have emerged as a powerful planning paradigm by learning action-conditioned predictive dynamics and using them as internal simulators to imagine and evaluate candidate action sequences. However, as the planning horizon grows, performance becomes increasingly constrained by proposal quality: a fixed candidate budget must search an exponentially larger action space, making it difficult to expose the world model to high-quality candidate futures for evaluation. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-17973:end -->

**为什么进入候选分母。** 摘要首要问题为“Latent world models have emerged as a powerful planning paradigm by learning action-conditioned predictive dynamics and using them as internal simulators to imagine and evaluate candidate action sequences.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** In this paper, we introduce a prior-conditioned planner that replaces random proposal initialization with structured guidance.

**证据证明什么。** Experiments on PushT and OGBench Cube show that coupling latent subgoal decomposition with prior-conditioned action generation substantially improves long-horizon planning while preserving strong short-horizon performance.

**证据没有证明什么。** The frozen world model then evaluates and refines these structured proposals, preserving its role as an action-conditioned simulator while improving the candidate futures exposed to it. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.17973v1#A1.SS3 — A.3 Architecture and Training Details; https://arxiv.org/html/2607.17973v1#S2.SS1 — 2.1 Latent World Model Planning。Evaluation：https://arxiv.org/html/2607.17973v1#A1.SS2 — A.2 Canonical Evaluation Protocol; https://arxiv.org/html/2607.17973v1#A1.SS6 — A.6 Per-Seed Main Results。Limitations / counterevidence：https://arxiv.org/html/2607.17973v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：The frozen world model then evaluates and refines these structured proposals, preserving its role as an action-conditioned simulator while improving the candidate futures exposed to it.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-GENERATIVE-PARADIGMS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-17973:end -->

<!-- review:SF-2026-ARXIV-2607-17979:start -->
### Harness Engineering for LLM-Driven GPU Kernel Generation

<!-- claim:SF-2026-ARXIV-2607-17979:start -->Large language models (LLMs) can assist GPU kernel generation, but their practical effectiveness depends on whether generated code can be reliably constrained, validated, profiled, and selected. This paper presents a harness-centered system for LLM-driven GPU kernel optimization in the MLSys 2026 FlashInfer AI Kernel Generation Contest on NVIDIA Blackwell B200 GPUs. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-17979:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language models (LLMs) can assist GPU kernel generation, but their practical effectiveness depends on whether generated code can be reliably constrained, validated, profiled, and selected.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** This paper presents a harness-centered system for LLM-driven GPU kernel optimization in the MLSys 2026 FlashInfer AI Kernel Generation Contest on NVIDIA Blackwell B200 GPUs.

**证据证明什么。** Across five operator definitions, the retained official-aligned artifacts achieved mean-latency speedups over supplied FlashInfer baselines of 1.62x, 18.05x, 29.68x, 1.12x, and 13.70x.

**证据没有证明什么。** 6 Limitations and Future Directions The main limitation is that this paper evaluates an Agent-Assisted engineering workflow, not an isolated LLM. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.17979v1#S2 — 2 Harness System Design; https://arxiv.org/html/2607.17979v1#S5.SS2 — 5.2 Implementation Stack。Evaluation：https://arxiv.org/html/2607.17979v1#S4 — 4 Experimental Evaluation; https://arxiv.org/html/2607.17979v1#A4 — Appendix D Ablation Notes。Limitations / counterevidence：https://arxiv.org/html/2607.17979v1#S6 — 6 Limitations and Future Directions; https://arxiv.org/html/2607.17979v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/syhya/mlsys26-flashinfer-contest, https://github.com/syhya/mlsys26-flashinfer-solution-fused-moe, https://github.com/syhya/mlsys26-flashinfer-solution-sparse-attention; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：6 Limitations and Future Directions The main limitation is that this paper evaluates an Agent-Assisted engineering workflow, not an isolated LLM.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-TENSORRT-LLM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-17979:end -->

<!-- review:SF-2026-ARXIV-2607-17986:start -->
### Self-State Attacks on Self-Hosted AI Agents: How Far Can OS Defenses Go?

<!-- claim:SF-2026-ARXIV-2607-17986:start -->Self-hosted AI agents read and write their own memory and configuration files to function. An agent may get compromised via corruption of its own state -- a compromise realized via legitimate OS system call invocation. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-17986:end -->

**为什么进入候选分母。** 摘要首要问题为“Self-hosted AI agents read and write their own memory and configuration files to function.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** An agent may get compromised via corruption of its own state -- a compromise realized via legitimate OS system call invocation.

**证据证明什么。** The empirical results show that a layered defense stack (access-control prevention on the instruction and configuration layers, workload-conditioned detection on the memory layer, and periodic backup for recovery) is effective on most attack cells while a small residual attack surface remains structurally indistinguishable at the OS level.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.17986v1#A6.SS1 — F.1. Harness Architecture; https://arxiv.org/html/2607.17986v1#S3 — 3. Limits of Operating System Defenses。Evaluation：https://arxiv.org/html/2607.17986v1#A6 — Appendix F Experimental Settings; https://arxiv.org/html/2607.17986v1#A7.SS3 — G.3. Workload-Conditioning Ablation: B1 vs B2 Detail。Limitations / counterevidence：https://arxiv.org/html/2607.17986v1#A5 — Appendix E Mapping of the Canonical Cells to Established Threat Catalogs; https://arxiv.org/html/2607.17986v1#A7 — Appendix G Extended Discussion。

**Artifact boundary。** Exact v1 links https://github.com/anomalyco/opencode, https://docs.claude.com/en/docs/claude-code/overview, https://blogs.cisco.com/ai/identifying-and-remediating-a-persistent-memory-compromise-in-claude-code; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-17986:end -->

<!-- review:SF-2026-ARXIV-2607-18002:start -->
### ExpertPlex: A High-Goodput Disaggregated Serving System for MoE LLMs with Adaptive Persistent Kernels

<!-- claim:SF-2026-ARXIV-2607-18002:start -->LLMs scale Mixture-of-Experts (MoE) parameters for superior intelligence, but massive weights and dynamic computation impede efficient serving. Existing instance-level prefill-decode disaggregation isolates the phases on separate full-model replicas. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18002:end -->

**为什么进入候选分母。** 摘要首要问题为“LLMs scale Mixture-of-Experts (MoE) parameters for superior intelligence, but massive weights and dynamic computation impede efficient serving.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** We present ExpertPlex, which shares massive MoE experts across phases while disaggregating lightweight attention modules.

**证据证明什么。** Experiments serving MiniMax-M2.7 and GLM-5.1-FP8 show that ExpertPlex improves goodput by up to 2.01$\times$ over instance-level prefill-decode disaggregation and 1.66$\times$ over prefill-decode colocation.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18002v1#S4.SS1 — 4.1. GPU Sharing Design Space; https://arxiv.org/html/2607.18002v1#S2.SS2 — 2.2. GPU Execution Model。Evaluation：https://arxiv.org/html/2607.18002v1#S7 — 7. Evaluation; https://arxiv.org/html/2607.18002v1#S7.SS1 — 7.1. Experiment Setup。Limitations / counterevidence：https://arxiv.org/html/2607.18002v1#S9 — 9. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/deepseek-ai/open-infra-index/blob/main/202502OpenSourceWeek/day_6_one_more_thing_deepseekV3R1_inference_system_overview.md, https://github.com/deepseek-ai/DeepEP, https://github.com/tile-ai/TileRT; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-SCHEDULING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18002:end -->

<!-- review:SF-2026-ARXIV-2607-18016:start -->
### Closing the Loop in Humanoid VLA: Persistent 3D Object Tokens for Verifiable Loco-Manipulation

<!-- claim:SF-2026-ARXIV-2607-18016:start -->Vision-language-action policies are a promising foundation for general robot control, but long-horizon humanoid loco-manipulation requires the robot to treat task objects as persistent physical entities across movement, contact, occlusion, and recovery. We study this problem as object-state divergence: the object state used to condition a whole-body action can differ from the state used to decide whether the action achieved the intended physical relation. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18016:end -->

**为什么进入候选分母。** 摘要首要问题为“Vision-language-action policies are a promising foundation for general robot control, but long-horizon humanoid loco-manipulation requires the robot to treat task objects as persistent physical entities across movement, contact, occlusion, and recovery.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We propose \emph{Persistent Object Tokenization} (POT), which maintains role-indexed 3D object records from RGB-D observations and converts them into object tokens for a whole-body action expert.

**证据证明什么。** On a Unitree G1, POT-VLA improves a matched direct GR00T-N1.7 baseline from 39/80 to 71/80 successes over eight real-world task families.

**证据没有证明什么。** Future work will extend POT to active multi-view memory, richer contact, dexterity, and human interaction. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18016v1#A1 — Appendix Appendix A Additional Method and Experiment Details; https://arxiv.org/html/2607.18016v1#S2.SS3 — 2.3 Humanoid Loco-Manipulation Systems。Evaluation：https://arxiv.org/html/2607.18016v1#A1 — Appendix Appendix A Additional Method and Experiment Details; https://arxiv.org/html/2607.18016v1#S4 — 4 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.18016v1#S5 — 5 Conclusion and Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Future work will extend POT to active multi-view memory, richer contact, dexterity, and human interaction.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18016:end -->

<!-- review:SF-2026-ARXIV-2607-18026:start -->
### Rethinking Heterogeneous LLM Merging: A Weighted Model Averaging Perspective

<!-- claim:SF-2026-ARXIV-2607-18026:start -->Can large language models with substantially different parameter spaces be merged by direct weighted averaging, without training or semantic alignment? Existing heterogeneous fusion methods typically introduce distillation, adapters, learned latent spaces, routing, or feature alignment, leaving open whether a simpler recipe can work for genuinely different billion-parameter checkpoints. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18026:end -->

**为什么进入候选分母。** 摘要首要问题为“Can large language models with substantially different parameter spaces be merged by direct weighted averaging, without training or semantic alignment?”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** Existing heterogeneous fusion methods typically introduce distillation, adapters, learned latent spaces, routing, or feature alignment, leaving open whether a simpler recipe can work for genuinely different billion-parameter checkpoints.

**证据证明什么。** These results show that simple parameter averaging, when paired with lightweight dimensional adaptation and carefully controlled ratios, is a surprisingly strong baseline for heterogeneous LLM merging, suggesting that the limits of direct weighted fusion may also bound what more complex heterogeneous merging methods can achieve at scale.

**证据没有证明什么。** Limitations This study focuses on Qwen-family checkpoints, offline benchmarks, and representative ratios; broader evaluation of long-context, multilingual, tool-use, efficiency, calibration, robustness, and safety settings remains future work. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18026v1#S3 — 3 Method。Evaluation：https://arxiv.org/html/2607.18026v1#A1 — Appendix A Additional Task-Level Results; https://arxiv.org/html/2607.18026v1#A3.SS1 — C.1 Ablation Controls and Baseline Comparisons。Limitations / counterevidence：https://arxiv.org/html/2607.18026v1#S7 — 7 Conclusion; https://arxiv.org/html/2607.18026v1#Sx1 — Limitations。

**Artifact boundary。** Exact v1 links https://github.com/bigcode-project/bigcode-evaluation-harness, https://huggingface.co/Qwen/Qwen3-4B-Thinking-2507, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Limitations This study focuses on Qwen-family checkpoints, offline benchmarks, and representative ratios; broader evaluation of long-context, multilingual, tool-use, efficiency, calibration, robustness, and safety settings remains future work.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-PRETRAINING`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18026:end -->

<!-- review:SF-2026-ARXIV-2607-18039:start -->
### Evidence-in-the-Loop: Trace-Driven Optimization for Customer-Service LLM Agents

<!-- claim:SF-2026-ARXIV-2607-18039:start -->Production customer-service bots must improve answer quality across iterative releases, yet large language models must not bypass evidence boundaries, policy rules, or human-handoff safeguards. We present an \textbf{Evidence-Grounded Customer-Service Agent Workflow} deployed in a real-world customer-service setting. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18039:end -->

**为什么进入候选分母。** 摘要首要问题为“Production customer-service bots must improve answer quality across iterative releases, yet large language models must not bypass evidence boundaries, policy rules, or human-handoff safeguards.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** We present an \textbf{Evidence-Grounded Customer-Service Agent Workflow} deployed in a real-world customer-service setting.

**证据证明什么。** Production customer-service bots must improve answer quality across iterative releases, yet large language models must not bypass evidence boundaries, policy rules, or human-handoff safeguards.

**证据没有证明什么。** Limitations and Future Work Experiments focus on one financial customer-service domain and use curated internal labels rather than web-scale retrieval suites such as BEIR ( Thakur et al., 2021 ) . 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18039v1#S4 — 4. Method; https://arxiv.org/html/2607.18039v1#S4.SS2 — 4.2. Evidence-Grounded Workflow Design。Evaluation：https://arxiv.org/html/2607.18039v1#S6 — 6. Experiments; https://arxiv.org/html/2607.18039v1#S6.SS1 — 6.1. Evaluation Scope and Claims。Limitations / counterevidence：https://arxiv.org/html/2607.18039v1#S8 — 8. Limitations and Future Work; https://arxiv.org/html/2607.18039v1#S7 — 7. Discussion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：Limitations and Future Work Experiments focus on one financial customer-service domain and use curated internal labels rather than web-scale retrieval suites such as BEIR ( Thakur et al., 2021 ) .

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-WORKFLOW`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18039:end -->

<!-- review:SF-2026-ARXIV-2607-18046:start -->
### SEE: Structure-aware Exploring &amp; Exploiting for Long-horizon GUI Agent Trajectory Synthesis

<!-- claim:SF-2026-ARXIV-2607-18046:start -->Graphical User Interface (GUI) agents powered by vision-language models hold promise for automating real-world mobile tasks. However, progress is limited by the lack of high-coverage, long-horizon interaction trajectories collected from element-rich and rapidly evolving apps. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18046:end -->

**为什么进入候选分母。** 摘要首要问题为“Graphical User Interface (GUI) agents powered by vision-language models hold promise for automating real-world mobile tasks.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** To address this problem, we propose SEE, a two-stage data synthesis framework consisting of (i) an efficient exploration stage that builds an explicit UI transition graph over screens and elements, and (ii) a graph-based synthesis stage that composes diverse multi-step trajectories via planning and controlled sampling.

**证据证明什么。** Across multiple real-world apps, SEE produces trajectories with an average length of 14.8 steps while avoiding spurious loops, and agents fine-tuned on SEE achieve improved task success and generalization to unseen screens.

**证据没有证明什么。** In future work, we plan to extend SEE to more complex instruction settings and synthesize longer-horizon trajectories. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18046v1#S1 — 1. Introduction; https://arxiv.org/html/2607.18046v1#S2 — 2. Related Work。Evaluation：https://arxiv.org/html/2607.18046v1#S5 — 5. Experiment; https://arxiv.org/html/2607.18046v1#S5.SS1 — 5.1. Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.18046v1#S6 — 6. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：In future work, we plan to extend SEE to more complex instruction settings and synthesize longer-horizon trajectories.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-DATA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18046:end -->

<!-- review:SF-2026-ARXIV-2607-18057:start -->
### Test Coverage Analysis of Agentic Pull Requests

<!-- claim:SF-2026-ARXIV-2607-18057:start -->AI coding agents increasingly submit complete pull requests (PRs) with minimal human intervention, shifting software development from AI-assisted to autonomous workflows. As these agents become more prevalent, ensuring the code they generate is adequately tested, by existing tests or by tests the agents write, is critical to preventing regressions, yet little is known about testing in agentic PRs. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18057:end -->

**为什么进入候选分母。** 摘要首要问题为“AI coding agents increasingly submit complete pull requests (PRs) with minimal human intervention, shifting software development from AI-assisted to autonomous workflows.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** As these agents become more prevalent, ensuring the code they generate is adequately tested, by existing tests or by tests the agents write, is critical to preventing regressions, yet little is known about testing in agentic PRs.

**证据证明什么。** Agent-written tests improve coverage over existing tests, but only in a minority of PRs: 35.9% of Java and 22.5% of Python Code + Tests PRs show a coverage gain.

**证据没有证明什么。** As existing tests often leave agent changes not covered, agents cannot assume existing tests will test their newly added code. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18057v1#S3 — III Methodology。Evaluation：https://arxiv.org/html/2607.18057v1#S3.SS3 — III-C RQ2: Measuring Diff Coverage and Analysis; https://arxiv.org/html/2607.18057v1#S4 — IV Results。Limitations / counterevidence：https://arxiv.org/html/2607.18057v1#S5 — V Discussion and Future Direction; https://arxiv.org/html/2607.18057v1#S6 — VI Related Work, Limitations。

**Artifact boundary。** Exact v1 links https://github.com/SageSELab/Agentic-Pull-Request-Test-Coverage/, https://pypi.org/project/pytest-cov/, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：As existing tests often leave agent changes not covered, agents cannot assume existing tests will test their newly added code.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18057:end -->

<!-- review:SF-2026-ARXIV-2607-18060:start -->
### RoboHarness: Memory-Driven Orchestration of Heterogeneous Robot Policies for Long-Horizon Planning

<!-- claim:SF-2026-ARXIV-2607-18060:start -->Long-horizon robotic tasks require diverse capabilities that no single policy can reliably provide. Heterogeneous policies offer complementary strengths, but orchestrating them requires reasoning over uncertain capability boundaries and cross-policy distribution mismatch, which are largely overlooked by existing planning methods built on homogeneous, predefined skills with fixed applicability. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18060:end -->

**为什么进入候选分母。** 摘要首要问题为“Long-horizon robotic tasks require diverse capabilities that no single policy can reliably provide.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We propose RoboHarness, a unified framework that encapsulates independently developed robot control systems as reusable agentic skills.

**证据证明什么。** Extensive experiments on three public benchmarks, 500 customized tasks, and 135 real-robot experiments demonstrate effective capability-aware routing and stable policy orchestration, yielding substantial improvements in zero-shot long-horizon planning and out-of-distribution robustness.

**证据没有证明什么。** 9 Limitations and Future Work RoboHarness is constrained by the collective capabilities of its underlying policy library: orchestration can combine complementary strengths but cannot solve subtasks that fall outside the capabilities of all available policies. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18060v1#S4 — 4 Methodology。Evaluation：https://arxiv.org/html/2607.18060v1#S5 — 5 Experimental Setup and Baselines; https://arxiv.org/html/2607.18060v1#S5.SS1 — 5.1 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.18060v1#S9 — 9 Limitations and Future Work; https://arxiv.org/html/2607.18060v1#S10 — 10 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：9 Limitations and Future Work RoboHarness is constrained by the collective capabilities of its underlying policy library: orchestration can combine complementary strengths but cannot solve subtasks that fall outside the capabilities of all available policies.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18060:end -->

<!-- review:SF-2026-ARXIV-2607-18063:start -->
### Adaptive Adversaries: A Multi-Turn, Multi-LLM Benchmark for LLM Agent Security

<!-- claim:SF-2026-ARXIV-2607-18063:start -->LLM-based agents process external content, exposing them to prompt injection and multi-turn manipulation. Most safety benchmarks evaluate defenders against fixed attack pools collected before evaluation, single-turn or multi-turn. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18063:end -->

**为什么进入候选分母。** 摘要首要问题为“LLM-based agents process external content, exposing them to prompt injection and multi-turn manipulation.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We present a 21-scenario benchmark for \emph{adaptive multi-round attacks against memoryless LLM defenders}: an autonomous LLM attacker observes prior defender responses and pivots across rounds, while each defender response is evaluated as a fresh interaction.

**证据证明什么。** We release the benchmark -- 21 evaluation scenarios, 10 public development scenarios, the orchestrator, baseline harnesses, and a multi-attacker CLI -- plus 945 transcripts from the 3$\times$3 frontier matrix, an attack-replay dataset, and 18{,}422 gpt-oss-20b battles from an open competition's final scoring rounds.

**证据没有证明什么。** C.1 memleak : Opus failure mode Figure 9: Threat-snapshot card for memleak . 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18063v1#S3 — 3 Design principles; https://arxiv.org/html/2607.18063v1#A2.SSx1 — B.0 Model inventory。Evaluation：https://arxiv.org/html/2607.18063v1#A2 — Appendix B Cross-Benchmark Metric Tables; https://arxiv.org/html/2607.18063v1#A2.SSx13 — B.12 Adaptivity ablation: non-adaptive attacker and stateful defender。Limitations / counterevidence：https://arxiv.org/html/2607.18063v1#A3.SSx1 — C.1 memleak : Opus failure mode; https://arxiv.org/html/2607.18063v1#A3.SSx2 — C.2 smarthomejack : GPT-5.4 failure mode。

**Artifact boundary。** Exact v1 links https://github.com/UKGovernmentBEIS/inspect_evals/tree/main/src/inspect_evals/ipi_coding_agent, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：C.1 memleak : Opus failure mode Figure 9: Threat-snapshot card for memleak .

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18063:end -->

<!-- review:SF-2026-ARXIV-2607-18080:start -->
### Sparse Evidence Can Suffice: Agentic Evidence Seeking for Multimodal Video Misinformation Detection

<!-- claim:SF-2026-ARXIV-2607-18080:start -->Multimodal video misinformation detection is commonly formulated as a holistic video-understanding task, where the entire video and its associated content are processed and judged in a single pass. However, real-world misinformation often exhibits a sparse and compositional evidence structure: a reliable decision may depend on only a few coupled clues, while most video content contributes limited additional information. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18080:end -->

**为什么进入候选分母。** 摘要首要问题为“Multimodal video misinformation detection is commonly formulated as a holistic video-understanding task, where the entire video and its associated content are processed and judged in a single pass.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** Accordingly, we propose SIEVE, a framework for Sparse Interactive Evidence Verification via Extraction in multimodal video misinformation detection.

**证据证明什么。** Experiments on multiple video misinformation benchmarks show that SIEVE consistently outperforms the evaluated baselines and supports reliable verification using compact evidence packages.

**证据没有证明什么。** However, the same ease of video creation and dissemination also accelerates the spread of misinformation, threatening the credibility of online information ecosystems and public discourse ( Bu et al. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18080v1#A3.SSx1 — Reward Design Details; https://arxiv.org/html/2607.18080v1#Sx3 — Method。Evaluation：https://arxiv.org/html/2607.18080v1#A4 — Appendix D Reward Ablation Study; https://arxiv.org/html/2607.18080v1#Sx4 — Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.18080v1#Sx1 — Introduction; https://arxiv.org/html/2607.18080v1#Sx2 — Related Work。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：However, the same ease of video creation and dissemination also accelerates the spread of misinformation, threatening the credibility of online information ecosystems and public discourse ( Bu et al.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-RAG`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18080:end -->

<!-- review:SF-2026-ARXIV-2607-18081:start -->
### SelectInfer: Selective Neuron Loading and Computation for On-Device LLMs

<!-- claim:SF-2026-ARXIV-2607-18081:start -->Large Language Models (LLMs) have demonstrated remarkable capabilities across a range of Natural Language Processing (NLP) tasks, but their high computational and memory demands pose significant challenges for deployment on resource-constrained edge devices. Existing approaches to model compression and optimization often rely on coarse-grained pruning or quantization, which can compromise accuracy or require re-training and fine-tuning. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18081:end -->

**为什么进入候选分母。** 摘要首要问题为“Large Language Models (LLMs) have demonstrated remarkable capabilities across a range of Natural Language Processing (NLP) tasks, but their high computational and memory demands pose significant challenges for deployment on resource-constrained edge devices.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** In this work, we introduce SelectInfer, a neuron-level optimization framework that enables efficient LLM inference on edge devices through selective neuron loading and computation.

**证据证明什么。** Evaluation across multiple datasets shows that SelectInfer achieves significant reductions in memory footprint and computation while preserving task performance, making it a practical step towards enabling LLM deployment on edge devices

**证据没有证明什么。** In addition, further research will address the current limitation of manually identifying task-specific neurons offline. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18081v1#S2.SS2 — 2.2 Model-Specific Neurons。Evaluation：https://arxiv.org/html/2607.18081v1#S6 — 6 Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.18081v1#S8 — 8 Conclusion。

**Artifact boundary。** Exact v1 links https://www.projectpro.io/article/large-language-model-use-cases-and-applications/887, https://github.com/zylon-ai/private-gpt, https://huggingface.co/meta-llama/Llama-3.2-3B; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：In addition, further research will address the current limitation of manually identifying task-specific neurons offline.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-GPU-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18081:end -->

<!-- review:SF-2026-ARXIV-2607-18086:start -->
### Judge-dependent safety gains and model-specific helpfulness costs of evidence-sufficiency prompting in clinical LLMs

<!-- claim:SF-2026-ARXIV-2607-18086:start -->Background: LLM judges increasingly score whether clinical language models give overconfident answers under incomplete evidence, yet whether a measured "safety gain" reflects real behavior change or the judge's calibration is unresolved. Using a structured evidence-sufficiency prompt as a test case, we asked whether it reduces unsafe overconfident answers, how far that effect depends on the scoring judge, and what it costs in helpfulness. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18086:end -->

**为什么进入候选分母。** 摘要首要问题为“Background: LLM judges increasingly score whether clinical language models give overconfident answers under incomplete evidence, yet whether a measured "safety gain" reflects real behavior change or the judge's calibration is unresolved.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Methods: In a retrospective public-data benchmark (Real-POCQi, HealthBench, MedRBench), four models (GPT-5.5, Claude Opus 4.8, Gemini 3.5 Flash, Grok 4.3) answered a fully paired common panel (1,200 cells) with a standard prompt and the wrapper.

**证据证明什么。** Matched scaffold controls showed genuine behavior change, not judge circularity.

**证据没有证明什么。** The low positive predictive value (~15%) quantiﬁes the over-labeling but should not be over-read: it rests on only 6 to 8 clinician-unsafe cases, is base-rate dependent, and is measured on the enrichment-balanced review sample rather than transported directly onto the panel-wide rate. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/pdf/2607.18086v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.18086v1#page=10 — PDF page 10。Evaluation：https://arxiv.org/pdf/2607.18086v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.18086v1#page=10 — PDF page 10。Limitations / counterevidence：https://arxiv.org/pdf/2607.18086v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.18086v1#page=10 — PDF page 10。

**Artifact boundary。** Exact v1 links https://github.com/aiden-ygu/health-ai-, https://huggingface.co/datasets/jjfenglab/Real-, https://github.com/MAGIC-AI4Med/MedRBench; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：The low positive predictive value (~15%) quantiﬁes the over-labeling but should not be over-read: it rests on only 6 to 8 clinician-unsafe cases, is base-rate dependent, and is measured on the enrichment-balanced review sample rather than transported directly onto the panel-wide rate.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18086:end -->

<!-- review:SF-2026-ARXIV-2607-18098:start -->
### VDAR-Router: Adaptive LLMs Routing via Verbalized Query Difficulty Analysis Retrieval

<!-- claim:SF-2026-ARXIV-2607-18098:start -->Large language models are increasingly used in practical systems, making efficient model selection important for reducing deployment cost. LLM routing has emerged as a practical solution for allocating each input query to an appropriate model under a desired cost-performance trade-off. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18098:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language models are increasingly used in practical systems, making efficient model selection important for reducing deployment cost.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** To address the challenge, we propose VDAR-Router, a difficulty-aware retrieval-based routing framework.

**证据证明什么。** These results demonstrate the effectiveness of difficulty-aware retrieval for training-free LLM routing.

**证据没有证明什么。** This design facilitates a training-free and more human-interpretable routing decision, while reducing the dependence on explicit routing labels, complete prompt-level scores, or additional router training. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18098v1#S3 — 3 Method; https://arxiv.org/html/2607.18098v1#A4 — Appendix D Rasch Difficulty Estimation Implementation。Evaluation：https://arxiv.org/html/2607.18098v1#S5 — 5 Experimental Results and Discussion; https://arxiv.org/html/2607.18098v1#A1 — Appendix A Difficulty Analysis Prompt。Limitations / counterevidence：https://arxiv.org/html/2607.18098v1#S5 — 5 Experimental Results and Discussion; https://arxiv.org/html/2607.18098v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://huggingface.co/datasets/lmarena-ai/arena-expert-5k, https://github.com/ulab-uiuc/LLMRouter, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：This design facilitates a training-free and more human-interpretable routing decision, while reducing the dependence on explicit routing labels, complete prompt-level scores, or additional router training.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`INFER-SCHEDULING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18098:end -->

<!-- review:SF-2026-ARXIV-2607-18100:start -->
### Can We Break LLMs Out of Self-Loops? Fine-Grained Reasoning Control with Activation Steering

<!-- claim:SF-2026-ARXIV-2607-18100:start -->Extended reasoning has become standard for frontier Large Language Models (LLMs), yet the trajectories these models produce remain largely uncontrollable. Existing methods for shaping how a model reasons are prompt based approaches and operate at the input level, offering no fine-grained control over the reasoning process itself. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18100:end -->

**为什么进入候选分母。** 摘要首要问题为“Extended reasoning has become standard for frontier Large Language Models (LLMs), yet the trajectories these models produce remain largely uncontrollable.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** To intervene on these failures, We propose SOPHIA: Steering Of reasoning Processes via Hidden-state Intervention and Activations.

**证据证明什么。** End task accuracy and token efficiency indicate that fine-grained controllability results in better reasoning quality.

**证据没有证明什么。** Across multiple models and benchmarks, transition-aware steering outperforms state-agnostic alternatives, with gains concentrated where greedy decoding cannot escape. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18100v1#S4 — 4 Methodology。Evaluation：https://arxiv.org/html/2607.18100v1#A2 — Appendix B Detailed Phase-Trajectory Analysis; https://arxiv.org/html/2607.18100v1#S2 — 2 Reasoning-State Transition Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.18100v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Across multiple models and benchmarks, transition-aware steering outperforms state-agnostic alternatives, with gains concentrated where greedy decoding cannot escape.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MODEL-SAMPLING`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18100:end -->

<!-- review:SF-2026-ARXIV-2607-18101:start -->
### Empowering On-Device Model Adaptation with an Edge AI Inference Accelerator

<!-- claim:SF-2026-ARXIV-2607-18101:start -->On-device model adaptation is essential to enable lifelong personalization on resource-constrained hardware, but compute, power, and memory limitations of such devices make end-to-end backpropagation impractical for modern deep neural networks. This work proposes a heterogeneous adaptation pipeline that repurposes a commercial edge AI inference accelerator, Hailo-8L, for frozen-backbone feature extraction during on-device training. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18101:end -->

**为什么进入候选分母。** 摘要首要问题为“On-device model adaptation is essential to enable lifelong personalization on resource-constrained hardware, but compute, power, and memory limitations of such devices make end-to-end backpropagation impractical for modern deep neural networks.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** This work proposes a heterogeneous adaptation pipeline that repurposes a commercial edge AI inference accelerator, Hailo-8L, for frozen-backbone feature extraction during on-device training.

**证据证明什么。** Overall, the results demonstrate a practical approach to efficient on-device adaptation using inference-oriented edge accelerators.

**证据没有证明什么。** Peak memory usage was not quantified in this study; instead, the evaluation was limited to latency/throughput and energy metrics. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18101v1#S3 — 3 Experimental Methodology; https://arxiv.org/html/2607.18101v1#S3.SS1 — 3.1 Heterogeneous On-Device Adaptation Architecture。Evaluation：https://arxiv.org/html/2607.18101v1#S3 — 3 Experimental Methodology; https://arxiv.org/html/2607.18101v1#S3.SS3 — 3.3 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.18101v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/MatPiech/onnxruntime, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：Peak memory usage was not quantified in this study; instead, the evaluation was limited to latency/throughput and energy metrics.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`INFER-TENSORRT-LLM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18101:end -->

<!-- review:SF-2026-ARXIV-2607-18108:start -->
### GARAGE: Characterizing the Automation Boundary in LLM-based Attack Graph Generation

<!-- claim:SF-2026-ARXIV-2607-18108:start -->While modern vehicle security depends on effective Cyber Threat Intelligence (CTI) synthesis, current automated tools struggle with unstructured data and automotive-specific architectural nuances. To bridge this gap, we introduce GARAGE, a RAG-powered framework that converts fragmented CTI into an actionable, domain-specific knowledge base for automated attack graph generation. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18108:end -->

**为什么进入候选分母。** 摘要首要问题为“While modern vehicle security depends on effective Cyber Threat Intelligence (CTI) synthesis, current automated tools struggle with unstructured data and automotive-specific architectural nuances.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** To bridge this gap, we introduce GARAGE, a RAG-powered framework that converts fragmented CTI into an actionable, domain-specific knowledge base for automated attack graph generation.

**证据证明什么。** By formalizing tactical-pattern-level scenarios through granular kill chain analysis, GARAGE achieves threat generation capabilities.

**证据没有证明什么。** However, these aggregate scores alone cannot explain the inter-model and inter-case performance variations. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18108v1#S2 — 2 Methodology; https://arxiv.org/html/2607.18108v1#S3.SS3 — 3.3 Evaluation Methodology: LLM-as-a-Judge。Evaluation：https://arxiv.org/html/2607.18108v1#S3.SS1 — 3.1 Evaluation Benchmarks; https://arxiv.org/html/2607.18108v1#S4 — 4 Results and Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.18108v1#S5 — 5 Discussion and Limitation; https://arxiv.org/html/2607.18108v1#S4.SS1 — 4.1 Inference Capability on Unknown Threats (Answering RQ1)。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：However, these aggregate scores alone cannot explain the inter-model and inter-case performance variations.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18108:end -->

<!-- review:SF-2026-ARXIV-2607-18110:start -->
### LLM-as-a-Coach: Experiential Learning for Non-Verifiable Tasks

<!-- claim:SF-2026-ARXIV-2607-18110:start -->Reinforcement learning (RL) on open-ended tasks compresses an LLM's rubric-based evaluation into a scalar reward, discarding rich textual feedback and conflating responses with distinct quality profiles. We propose Experiential Learning (EL), which repurposes the feedback model from an LLM-as-a-Judge into an LLM-as-a-Coach. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18110:end -->

**为什么进入候选分母。** 摘要首要问题为“Reinforcement learning (RL) on open-ended tasks compresses an LLM's rubric-based evaluation into a scalar reward, discarding rich textual feedback and conflating responses with distinct quality profiles.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We propose Experiential Learning (EL), which repurposes the feedback model from an LLM-as-a-Judge into an LLM-as-a-Coach.

**证据证明什么。** Across two policy families, with feedback from the policy itself or a proprietary model, EL consistently outperforms rubric-based RL on held-out and unseen open-ended tasks.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18110v1#S2 — 2 Method。Evaluation：https://arxiv.org/html/2607.18110v1#A1 — Appendix A Details of Experiments; https://arxiv.org/html/2607.18110v1#A1.SS2 — A.2 Ablation Prompt Templates。Limitations / counterevidence：https://arxiv.org/html/2607.18110v1#S4 — 4 Discussion; https://arxiv.org/html/2607.18110v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://aka.ms/el-code, https://github.com/EQ-bench/creative-writing-bench, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-RLHF`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18110:end -->

<!-- review:SF-2026-ARXIV-2607-18114:start -->
### How Does Alignment Tuning Shape Representations of Sycophancy and Related Cue-Induced Biases in LLMs?

<!-- claim:SF-2026-ARXIV-2607-18114:start -->Modern LLMs are alarmingly susceptible to surprisingly simple immaterial changes of input prompts: a casual hint, an incorrectly labeled few-shot example, or a fake prior assistant turn often flips an originally correct answer. We study where this susceptibility, spanning sycophancy and related cue-induced biases, lives inside the model. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18114:end -->

**为什么进入候选分母。** 摘要首要问题为“Modern LLMs are alarmingly susceptible to surprisingly simple immaterial changes of input prompts: a casual hint, an incorrectly labeled few-shot example, or a fake prior assistant turn often flips an originally correct answer.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We study where this susceptibility, spanning sycophancy and related cue-induced biases, lives inside the model.

**证据证明什么。** Cue-induced bias is therefore best understood not as a single flaw in LLMs but as a family of causally effective linear directions that are largely shaped by alignment tuning.

**证据没有证明什么。** If the relevant directions are installed or strongly amplified during post-training, then mitigation should target alignment recipes themselves, not only inference-time defenses. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18114v1#S3 — 3 Methodology。Evaluation：https://arxiv.org/html/2607.18114v1#A3 — Appendix C Cluster structure analysis; https://arxiv.org/html/2607.18114v1#S4 — 4 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.18114v1#S10 — 10 Conclusion; https://arxiv.org/html/2607.18114v1#S9 — 9 Discussion。

**Artifact boundary。** Exact v1 links https://github.com/prakharg55/bias-direction-EMNLP, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：If the relevant directions are installed or strongly amplified during post-training, then mitigation should target alignment recipes themselves, not only inference-time defenses.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-RLHF`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18114:end -->

<!-- review:SF-2026-ARXIV-2607-18141:start -->
### A CXL Memory Rack for Multi-Turn LLM Serving

<!-- claim:SF-2026-ARXIV-2607-18141:start -->Long-context, multi-turn, and agentic LLM workloads increasingly reuse previously processed context, making KV-cache reuse essential for reducing redundant computation. However, this reuse shifts the bottleneck to the memory tier that stores and serves reusable KV states at cluster scale. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18141:end -->

**为什么进入候选分母。** 摘要首要问题为“Long-context, multi-turn, and agentic LLM workloads increasingly reuse previously processed context, making KV-cache reuse essential for reducing redundant computation.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** However, this reuse shifts the bottleneck to the memory tier that stores and serves reusable KV states at cluster scale.

**证据证明什么。** Under the same DRAM budget, HyMCache outperforms local LMCache by 3.0x in single-node serving and 1.45x in PD-disaggregated serving.

**证据没有证明什么。** Our evaluation on a real CXL-HM prototype under both single-aggregator and PD-disaggregated serving shows that HyMCache enables scalable and cost-efficient remote KV-cache capacity for future LLM serving systems. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18141v1#S1 — 1. Introduction; https://arxiv.org/html/2607.18141v1#S2 — 2. Background and Motivation。Evaluation：https://arxiv.org/html/2607.18141v1#S5 — 5. Experimental Setup; https://arxiv.org/html/2607.18141v1#S6 — 6. Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.18141v1#S8 — 8. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/ai-dynamo/nixl, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：Our evaluation on a real CXL-HM prototype under both single-aggregator and PD-disaggregated serving shows that HyMCache enables scalable and cost-efficient remote KV-cache capacity for future LLM serving systems.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-GPU-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18141:end -->

<!-- review:SF-2026-ARXIV-2607-18155:start -->
### Testing Retrieval-Augmented Generation Systems with Chunk Coverage

<!-- claim:SF-2026-ARXIV-2607-18155:start -->Retrieval-Augmented Generation (RAG)-based systems\footnote{For brevity, RAG-based systems are referred to as RAG systems throughout this paper.} are increasingly deployed in high-stakes settings where correct behaviour depends not only on the language model but also on the retrieval component that selects external documents at inference time. While existing RAG evaluation metrics assess retrieval and generation quality on a per-query basis, typically relying on query-level test oracles such as reference answers or relevance annotations, they provide limited insight into whether a test suite adequately exercises the retrieval behaviour of the system as a whole. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18155:end -->

**为什么进入候选分母。** 摘要首要问题为“Retrieval-Augmented Generation (RAG)-based systems\footnote{For brevity, RAG-based systems are referred to as RAG systems throughout this paper.} are increasingly deployed in high-stakes settings where correct behaviour depends not only on the language model but also on the retrieval component that selects external documents at inference time.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** In this paper, we introduce Chunk Coverage (CC), an oracle-independent test adequacy criterion for testing the retrieval component of RAG systems.

**证据证明什么。** These results show that CC captures retrieval diversity relevant to effective testing without requiring test oracles.

**证据没有证明什么。** Formally, let denote the set of chunks retrieved for a query . 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18155v1#S2.SS2 — 2.2. Evaluation Metrics for RAG Systems; https://arxiv.org/html/2607.18155v1#S3 — 3. Chunk Coverage for Testing RAG Systems。Evaluation：https://arxiv.org/html/2607.18155v1#S2.SS2 — 2.2. Evaluation Metrics for RAG Systems; https://arxiv.org/html/2607.18155v1#S4 — 4. Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.18155v1#S4.SS3 — 4.3. Failures and Faults in RAG Systems; https://arxiv.org/html/2607.18155v1#S7 — 7. Threats to Validity。

**Artifact boundary。** Exact v1 links https://github.com/dbr7/issta26-chunk-coverage-artifact, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Formally, let denote the set of chunks retrieved for a query .

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-RAG`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18155:end -->

<!-- review:SF-2026-ARXIV-2607-18161:start -->
### TRIM: Reducing AI-Generated CodeSlop via Agent Trajectory Minimization

<!-- claim:SF-2026-ARXIV-2607-18161:start -->Coding agents are increasingly used to accelerate code generation in many downstream tasks, such as fixing bugs, building applications, and prototyping. However, despite their value as coding assistants, agent-generated code tends to be larger and more verbose than the corresponding human-written implementation. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18161:end -->

**为什么进入候选分母。** 摘要首要问题为“Coding agents are increasingly used to accelerate code generation in many downstream tasks, such as fixing bugs, building applications, and prototyping.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** However, despite their value as coding assistants, agent-generated code tends to be larger and more verbose than the corresponding human-written implementation.

**证据证明什么。** As we show empirically, this indirect technique of minimizing CodeSlop is highly effective: TRIM cuts CodeSlop by 17.9%-32.9% across agentic scaffolds, with negligible performance regression.

**证据没有证明什么。** Unlike Delta Debugging, which treats patches as largely independent hunks, Trim exploits the dependencies naturally encoded in repair trajectories, matching exhaustive hunk-level minimization at roughly half the validation cost. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18161v1#S4 — IV Methodology; https://arxiv.org/html/2607.18161v1#S4.SS1 — IV-A System Overview。Evaluation：https://arxiv.org/html/2607.18161v1#S5 — V Experimental Design; https://arxiv.org/html/2607.18161v1#S5.SS2 — V-B Evaluation Metrics。Limitations / counterevidence：https://arxiv.org/html/2607.18161v1#S8 — VIII Threats to Validity; https://arxiv.org/html/2607.18161v1#S8.SS1 — VIII-A Discussion。

**Artifact boundary。** Exact v1 links https://claude.com/product/claude-code, https://github.com/features/copilot, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：Unlike Delta Debugging, which treats patches as largely independent hunks, Trim exploits the dependencies naturally encoded in repair trajectories, matching exhaustive hunk-level minimization at roughly half the validation cost.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-PLATFORM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18161:end -->

<!-- review:SF-2026-ARXIV-2607-18171:start -->
### FlashRT: Agent Harness for Guiding Agents to Deploy Real-Time Multimodal Applications

<!-- claim:SF-2026-ARXIV-2607-18171:start -->Real-time multimodal applications, including voice agents and interactive video generation, compose heterogeneous models into pipelines whose efficient deployment requires application-specific decisions about placement, streaming, and intra-model parallelism. Existing serving systems and auto-parallelism compilers commit to limited transformations and fixed workload assumptions, so achieving high performance on a new application requires hand-crafting an efficient implementation. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18171:end -->

**为什么进入候选分母。** 摘要首要问题为“Real-time multimodal applications, including voice agents and interactive video generation, compose heterogeneous models into pipelines whose efficient deployment requires application-specific decisions about placement, streaming, and intra-model parallelism.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** We present FlashRT, an agent harness that guides coding agents to lift simple developer-written reference implementations into optimized multi-GPU deployments that flexibly weigh target metrics like latency and throughput.

**证据证明什么。** In fact, for Qwen3-Omni text-to-audio inference, FlashRT reduces response latency by 65% compared to the expert vLLM-Omni implementation on AMD MI355X.

**证据没有证明什么。** A current limitation of our system is that we have not integrated LLM kernel optimization agents. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18171v1#S9.SS1 — 9.1 Video World Model (WorldPlay)。Evaluation：https://arxiv.org/html/2607.18171v1#S9 — 9 Extended Deployment Results and Scaling Analysis; https://arxiv.org/html/2607.18171v1#S5 — 5 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.18171v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/Infini-AI-Lab/FlashRT, https://code.claude.com/docs/en/overview, https://github.com/krea-ai/realtime-video; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：A current limitation of our system is that we have not integrated LLM kernel optimization agents.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-PLATFORM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18171:end -->

<!-- review:SF-2026-ARXIV-2607-18199:start -->
### PPL-Factory: Task-Aware and Budget-Aware Data Selection from Language Modeling to Reasoning

<!-- claim:SF-2026-ARXIV-2607-18199:start -->Not all training samples contribute equally to large language model fine-tuning. Selecting informative training samples can reduce the computational cost while preserving downstream performance. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18199:end -->

**为什么进入候选分母。** 摘要首要问题为“Not all training samples contribute equally to large language model fine-tuning.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** In this paper, we propose PPL-Factory, a simple and interpretable data selection framework that combines task-aware perplexity-based scores and data budget-aware selection criteria.

**证据证明什么。** Experiments on GSM8K demonstrate that PPL-Factory outperforms other state-of-the-art data selection methods using only $1\%$ of the training set.

**证据没有证明什么。** B.2 Discussion on Pruning Rates The shape of the optimal selector is controlled by the budget-dependent utility . 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18199v1#S3 — 3 Methodology; https://arxiv.org/html/2607.18199v1#S4.SS1 — 4.1 Benchmarks and Models。Evaluation：https://arxiv.org/html/2607.18199v1#S4 — 4 Experiments and Results; https://arxiv.org/html/2607.18199v1#A2 — Appendix B Theoretical Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.18199v1#A2.SS2 — B.2 Discussion on Pruning Rates; https://arxiv.org/html/2607.18199v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://aclanthology.org/2020.emnlp-demos.6/, https://dx.doi.org/10.18653/v1/2020.emnlp-demos.6, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：B.2 Discussion on Pruning Rates The shape of the optimal selector is controlled by the budget-dependent utility .

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-DATA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18199:end -->

<!-- review:SF-2026-ARXIV-2607-18213:start -->
### SWE-Pruner Pro: The Coder LLM Already Knows What to Prune

<!-- claim:SF-2026-ARXIV-2607-18213:start -->Pruning long context for coding agents has been a vital technology for efficient context management. While existing context pruning methods such as SWE-Pruner realize this by attaching a separate code classifier, we find the agent itself encodes internal representations indicating the relevance of code context when reading tool output. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18213:end -->

**为什么进入候选分母。** 摘要首要问题为“Pruning long context for coding agents has been a vital technology for efficient context management.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** Based on this finding, we propose SWE-Pruner Pro, which prunes tool outputs directly inside the agent.

**证据证明什么。** While existing context pruning methods such as SWE-Pruner realize this by attaching a separate code classifier, we find the agent itself encodes internal representations indicating the relevance of code context when reading tool output.

**证据没有证明什么。** As for language coverage, although our agent-task benchmarks are Python-centric, the pipeline is language-agnostic, and Oolong (a long-context natural-language aggregation benchmark) gives an out-of-domain check on which SWE-Pruner Pro preserves both token savings and quality on both backbones (Table 1 ); broader coverage across programming languages reuses the same pipeline and is left to future work. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18213v1#S3 — 3 Method。Evaluation：https://arxiv.org/html/2607.18213v1#A3 — Appendix C Oolong Benchmark Conversion; https://arxiv.org/html/2607.18213v1#S4 — 4 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.18213v1#S7 — 7 Conclusion; https://arxiv.org/html/2607.18213v1#Sx1 — Limitations。

**Artifact boundary。** Exact v1 links https://github.com/Ayanami1314/swe-pruner-pro, https://github.com/SWE-agent/mini-swe-agent, https://huggingface.co/BAAI/bge-reranker-v2-m3; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：As for language coverage, although our agent-task benchmarks are Python-centric, the pipeline is language-agnostic, and Oolong (a long-context natural-language aggregation benchmark) gives an out-of-domain check on which SWE-Pruner Pro preserves both token savings and quality on both backbones (Table 1 ); broader coverage across programming languages reuses the same pipeline and is left to future work.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-PLATFORM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18213:end -->

<!-- review:SF-2026-ARXIV-2607-18231:start -->
### FM-VLA: Force-based Memory for Vision-Language-Action Models in Contact-Rich Manipulation

<!-- claim:SF-2026-ARXIV-2607-18231:start -->Vision-language-action (VLA) models have achieved impressive generalization in robotic manipulation, and recent memory-augmented VLAs have relaxed the Markovian assumption by conditioning on past images or language summaries. Vision-based memory approaches address this by conditioning on sampled past image frames, but they are computationally expensive and fundamentally limited when temporal events are visually ambiguous, e.g., pushing a button multiple times with small movements. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-18231:end -->

**为什么进入候选分母。** 摘要首要问题为“Vision-language-action (VLA) models have achieved impressive generalization in robotic manipulation, and recent memory-augmented VLAs have relaxed the Markovian assumption by conditioning on past images or language summaries.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We propose FM-VLA, a VLA model with force-based memory, enabling temporal context reasoning for non-Markovian, contact-rich manipulation.

**证据证明什么。** Our lightweight force memory achieves over 80% success rate with minimal inference overhead, significantly outperforming baseline approaches.

**证据没有证明什么。** This equips the model with accumulated event memory even when the visual observation is limited or ambiguous, a capability neither vision-based memory nor single-token force conditioning provides. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.18231v1#A5.SS1 — E.1 Architecture details; https://arxiv.org/html/2607.18231v1#S3 — 3 Methodology。Evaluation：https://arxiv.org/html/2607.18231v1#A1 — Appendix A Additional Real-World Results; https://arxiv.org/html/2607.18231v1#A2 — Appendix B Task Definitions and Evaluation Protocol。Limitations / counterevidence：https://arxiv.org/html/2607.18231v1#S5 — 5 Limitations; https://arxiv.org/html/2607.18231v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：This equips the model with accumulated event memory even when the visual observation is limited or ambiguous, a capability neither vision-based memory nor single-token force conditioning provides.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-18231:end -->

## 4. Benchmark Contracts

None。数值只在各 Source Review 的 exact-v1 evaluation contract 内使用，不形成跨配置 benchmark claim。

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-16204 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-16204 |
| SF-2026-ARXIV-2607-16213 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-16213 |
| SF-2026-ARXIV-2607-16241 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-16241 |
| SF-2026-ARXIV-2607-16244 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-16244 |
| SF-2026-ARXIV-2607-16246 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-16246 |
| SF-2026-ARXIV-2607-16248 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-16248 |
| SF-2026-ARXIV-2607-16339 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-16339 |
| SF-2026-ARXIV-2607-16473 | score_7_9 | selected | DA-20260721-01 | — | V2=9/9；相对其他 eligible family 提供更直接、可迁移且不重复的 state/control/evaluation 机制。 | analysis:DA-20260721-01 |
| SF-2026-ARXIV-2607-16488 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-16488 |
| SF-2026-ARXIV-2607-16555 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-16555 |
| SF-2026-ARXIV-2607-16596 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-16596 |
| SF-2026-ARXIV-2607-16602 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-16602 |
| SF-2026-ARXIV-2607-16617 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-16617 |
| SF-2026-ARXIV-2607-16636 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-16636 |
| SF-2026-ARXIV-2607-16673 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-16673 |
| SF-2026-ARXIV-2607-16784 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-16784 |
| SF-2026-ARXIV-2607-16836 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-16836 |
| SF-2026-ARXIV-2607-16892 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-16892 |
| SF-2026-ARXIV-2607-17175 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-17175 |
| SF-2026-ARXIV-2607-17181 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-17181 |
| SF-2026-ARXIV-2607-17299 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-17299 |
| SF-2026-ARXIV-2607-17415 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-17415 |
| SF-2026-ARXIV-2607-17422 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-17422 |
| SF-2026-ARXIV-2607-17525 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-17525 |
| SF-2026-ARXIV-2607-17644 | score_7_9 | selected | DA-20260721-02 | — | V2=9/9；相对其他 eligible family 提供更直接、可迁移且不重复的 state/control/evaluation 机制。 | analysis:DA-20260721-02 |
| SF-2026-ARXIV-2607-17652 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-17652 |
| SF-2026-ARXIV-2607-17715 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-17715 |
| SF-2026-ARXIV-2607-17733 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-17733 |
| SF-2026-ARXIV-2607-17979 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-17979 |
| SF-2026-ARXIV-2607-18002 | score_7_9 | selected | DA-20260721-03 | — | V2=9/9；相对其他 eligible family 提供更直接、可迁移且不重复的 state/control/evaluation 机制。 | analysis:DA-20260721-03 |
| SF-2026-ARXIV-2607-18016 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-18016 |
| SF-2026-ARXIV-2607-18081 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-18081 |
| SF-2026-ARXIV-2607-18141 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-18141 |

### Selection Decisions

<!-- analysis-decision:SF-2026-ARXIV-2607-16204:start -->
`SF-2026-ARXIV-2607-16204` 的 exact-v1 Deep Review 已保留。其机制为：We introduce a plug-and-play GRPO training framework with deterministic state checks, and perform zero-shot transfer ablations on three OOD environments (ScienceWorld, ALFWorld, AppWorld) across three 1.2B-7B agent backbones (LFM2.5, Qwen3, Mistral), achieving up to 47% absolute gains over baselines without environment-specific fine-tuning. 为避免挤压 `MULTIMODAL-WORLD-MODELS` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-16204:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-16213:start -->
`SF-2026-ARXIV-2607-16213` 的 exact-v1 Deep Review 已保留。其机制为：We propose a training-free, dual-component framework for KV cache compression that addresses these limitations. 为避免挤压 `INFER-KV-CACHE` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-16213:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-16241:start -->
`SF-2026-ARXIV-2607-16241` 的 exact-v1 Deep Review 已保留。其机制为：We introduce KernelBench-Verified, an extended evaluation framework that incorporates a TF32-enabled baseline and a four-distribution hidden test suite. 为避免挤压 `INFER-TENSORRT-LLM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-16241:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-16244:start -->
`SF-2026-ARXIV-2607-16244` 的 exact-v1 Deep Review 已保留。其机制为：We propose a variance-injection strategy: by assigning per-turn rewards to intermediate evidence-reading turns, we prevent the group reward distribution from collapsing to a single value--preserving the variation that GRPO's group-relative advantage requires. 为避免挤压 `TRAIN-GRPO` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-16244:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-16246:start -->
`SF-2026-ARXIV-2607-16246` 的 exact-v1 Deep Review 已保留。其机制为：To quantify this tension, we introduce diagnostic metrics -- support coverage, observed-token probability mass, and teacher-distribution concentration -- and show via controlled sweeps that the support size $k$ governs a coverage-sharpness trade-off, while distillation temperature controls within-support probability allocation. 为避免挤压 `TRAIN-PRETRAINING` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-16246:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-16248:start -->
`SF-2026-ARXIV-2607-16248` 的 exact-v1 Deep Review 已保留。其机制为：Low-bit KV-cache quantization reduces this cost, yet it severely degrade quality; particularly, one-bit quantization reduces accuracy from 84.2% to 47.8% on Llama-3.1-8B under RULER. 为避免挤压 `INFER-KV-CACHE` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-16248:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-16339:start -->
`SF-2026-ARXIV-2607-16339` 的 exact-v1 Deep Review 已保留。其机制为：We propose LaCache, a training-free acceleration framework that alleviates this redundancy through lossless caching and mixed precision. 为避免挤压 `MULTIMODAL-GENERATIVE-PARADIGMS` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-16339:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-16488:start -->
`SF-2026-ARXIV-2607-16488` 的 exact-v1 Deep Review 已保留。其机制为：To realize these benefits, we present NeuScale, an auto-scaling framework to automatically exploit heterogeneous NPUs for cloud platforms. 为避免挤压 `INFER-SCHEDULING` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-16488:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-16555:start -->
`SF-2026-ARXIV-2607-16555` 的 exact-v1 Deep Review 已保留。其机制为：We present a measurement study of this effect on a commercial smartphone. 为避免挤压 `INFER-TENSORRT-LLM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-16555:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-16596:start -->
`SF-2026-ARXIV-2607-16596` 的 exact-v1 Deep Review 已保留。其机制为：For models on s3://, gs://, or hf:// URIs, where no admission-time verifier observes the bytes, we present a serving-time integrity design proposed to the KServe community: digest pinning and OpenSSF model-signing enforcement in the storage initializer. 为避免挤压 `PLATFORM-MODEL-REGISTRY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-16596:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-16602:start -->
`SF-2026-ARXIV-2607-16602` 的 exact-v1 Deep Review 已保留。其机制为：To address this, we propose PAVXploreRL, a reinforcement learning framework built on a pretrained latent world model that explicitly optimizes PAV objectives through reward-driven training. 为避免挤压 `MULTIMODAL-WORLD-MODELS` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-16602:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-16617:start -->
`SF-2026-ARXIV-2607-16617` 的 exact-v1 Deep Review 已保留。其机制为：To bridge it, we introduce \textsc{DataFlow-Harness}, a platform that guides an LLM agent to construct platform-native directed acyclic graphs (DAGs) through typed, incremental mutations rather than free-form scripts. 为避免挤压 `TRAIN-DATA` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-16617:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-16636:start -->
`SF-2026-ARXIV-2607-16636` 的 exact-v1 Deep Review 已保留。其机制为：We present PhyAgentOS, a runtime foundation delivering scheduling, verification, memory, benchmarking, and safety as system-level services. 为避免挤压 `MULTIMODAL-EMBODIED-VLA` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-16636:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-16673:start -->
`SF-2026-ARXIV-2607-16673` 的 exact-v1 Deep Review 已保留。其机制为：Speculative decoding can reduce this cost by verifying several draft tokens in one target pass, yet existing speculative systems are designed for Transformer KV caches. 为避免挤压 `INFER-SPECULATIVE-DECODING` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-16673:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-16784:start -->
`SF-2026-ARXIV-2607-16784` 的 exact-v1 Deep Review 已保留。其机制为：Whether colocation succeeds or violates SLOs depends on the temporal overlap of kernels from concurrently executing models -- an effect that existing serving systems either ignore or approximate using aggregate resource profiles that fail to capture temporal dynamics. 为避免挤压 `INFER-SCHEDULING` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-16784:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-16836:start -->
`SF-2026-ARXIV-2607-16836` 的 exact-v1 Deep Review 已保留。其机制为：Shared state increasingly shapes both performance and failure behavior in streaming, serving, retrieval, and continual-learning systems. 为避免挤压 `PLATFORM-FOUNDATIONS` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-16836:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-16892:start -->
`SF-2026-ARXIV-2607-16892` 的 exact-v1 Deep Review 已保留。其机制为：We present a robust KV cache management framework for LLM serving that jointly optimizes GPU parallelism configuration, KV cache reservation per request class, request routing across heterogeneous serving groups, and prefix caching for shared prompts. 为避免挤压 `INFER-KV-CACHE` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-16892:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-17175:start -->
`SF-2026-ARXIV-2607-17175` 的 exact-v1 Deep Review 已保留。其机制为：However, efficiently serving LLM requests across heterogeneous and resource-constrained edge devices require orchestration mechanisms that jointly determine model configuration (family, size, and quantization level) and execution placement while satisfying user- and system-level quality of service (QoS) requirements. 为避免挤压 `INFER-SCHEDULING` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-17175:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-17181:start -->
`SF-2026-ARXIV-2607-17181` 的 exact-v1 Deep Review 已保留。其机制为：We present Talaria, a session-aware serverless multi-model serving system that makes session continuity a joint placement-and-admission decision. 为避免挤压 `INFER-SCHEDULING` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-17181:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-17299:start -->
`SF-2026-ARXIV-2607-17299` 的 exact-v1 Deep Review 已保留。其机制为：We propose WAR, a workload-aware rollout system that substantially accelerates synchronous agentic RL by jointly optimizing decoding and scheduling. 为避免挤压 `TRAIN-GRPO` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-17299:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-17415:start -->
`SF-2026-ARXIV-2607-17415` 的 exact-v1 Deep Review 已保留。其机制为：Static backend assignment cannot exploit this variation, while independent per-operator selection can introduce costly device and framework switches. 为避免挤压 `INFER-SCHEDULING` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-17415:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-17422:start -->
`SF-2026-ARXIV-2607-17422` 的 exact-v1 Deep Review 已保留。其机制为：We present LATTICE, a deterministic constraint-directed compiler pipeline. 为避免挤压 `INFER-SCHEDULING` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-17422:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-17525:start -->
`SF-2026-ARXIV-2607-17525` 的 exact-v1 Deep Review 已保留。其机制为：Yet the failure modes specific to this architectural layer remain undocumented, scattered across issue trackers and post-mortems with no unifying framework. 为避免挤压 `PLATFORM-GATEWAY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-17525:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-17652:start -->
`SF-2026-ARXIV-2607-17652` 的 exact-v1 Deep Review 已保留。其机制为：We propose \textbf{\flowblock{}}, a training-free parallel decoding framework built on two mechanisms. (i) \emph{Gated Wavefront Decoding} admits blocks into a bounded wavefront only when a readiness gate is satisfied, jointly refines active blocks via T2T editing, and commits blocks in order under a windowed block-causal mask that preserves exact frozen-prefix KV caches reuse. (ii) \emph{Heterogeneous Wavefront Packing} assigns each request an independent wavefront while packing asynchronous windows into dense, shape-stable batched forwards. 为避免挤压 `MULTIMODAL-GENERATIVE-PARADIGMS` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-17652:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-17715:start -->
`SF-2026-ARXIV-2607-17715` 的 exact-v1 Deep Review 已保留。其机制为：In this work, we propose C$^2$KV, a unified framework for non-prefix KV reuse that jointly optimizes KV extraction and inference-time concatenation. 为避免挤压 `INFER-KV-CACHE` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-17715:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-17733:start -->
`SF-2026-ARXIV-2607-17733` 的 exact-v1 Deep Review 已保留。其机制为：We introduce MXSens, a training-free method that assigns mixed mantissa bitwidths (4/6/8) based on column- and layer-wise sensitivity, naturally leveraging the block-wise structure of MXINT. 为避免挤压 `INFER-GPU-MEMORY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-17733:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-17979:start -->
`SF-2026-ARXIV-2607-17979` 的 exact-v1 Deep Review 已保留。其机制为：This paper presents a harness-centered system for LLM-driven GPU kernel optimization in the MLSys 2026 FlashInfer AI Kernel Generation Contest on NVIDIA Blackwell B200 GPUs. 为避免挤压 `INFER-TENSORRT-LLM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-17979:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-18016:start -->
`SF-2026-ARXIV-2607-18016` 的 exact-v1 Deep Review 已保留。其机制为：We propose \emph{Persistent Object Tokenization} (POT), which maintains role-indexed 3D object records from RGB-D observations and converts them into object tokens for a whole-body action expert. 为避免挤压 `MULTIMODAL-EMBODIED-VLA` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-18016:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-18081:start -->
`SF-2026-ARXIV-2607-18081` 的 exact-v1 Deep Review 已保留。其机制为：In this work, we introduce SelectInfer, a neuron-level optimization framework that enables efficient LLM inference on edge devices through selective neuron loading and computation. 为避免挤压 `INFER-GPU-MEMORY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-18081:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-18141:start -->
`SF-2026-ARXIV-2607-18141` 的 exact-v1 Deep Review 已保留。其机制为：However, this reuse shifts the bottleneck to the memory tier that stores and serves reusable KV states at cluster scale. 为避免挤压 `INFER-GPU-MEMORY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-18141:end -->

### Selected Analysis Narratives

<!-- analysis:DA-20260721-01:start -->
### Enabling Spatially Fine-Grained DVFS in Neural Processing Units for Energy-Efficient LLM Serving

**约束变化与机制。** Our study shows that using dynamic voltage and frequency scaling (DVFS) to exploit the service-level objective (SLO) slacks is a promising way to improve NPU energy efficiency for LLM services.

**证明与未证明。** Our study shows that using dynamic voltage and frequency scaling (DVFS) to exploit the service-level objective (SLO) slacks is a promising way to improve NPU energy efficiency for LLM services. 但 As long as the law continues to hold, DVFS will remain an effective technique for future nodes. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：As long as the law continues to hold, DVFS will remain an effective technique for future nodes. 旧方案在不承受该约束时仍成立。

关联：`review:SF-2026-ARXIV-2607-16473`。
<!-- analysis:DA-20260721-01:end -->

<!-- analysis:DA-20260721-02:start -->
### A Training-Memory Regression in MLA Sequence Parallelism: Why Megatron-Core Forbids Absorption, and LAGA -- a Communication-Efficient Fix

**约束变化与机制。** We show the restriction is well-founded and quantify why: ported to training, the absorbed form is a memory trap -- its intermediates live in n_h x d_kv dimensions per token, larger than the per-head K/V they replace -- inflating activation memory by 20-34%, up to 9.2 GB at DeepSeek-V3 scale (n_h=128, seq=16384, SP=8, eager kernel; the gap widens to 19.2 GB under a fused kernel), enough to change device-fit.

**证明与未证明。** On 8x Ascend 910B at real DeepSeek-V3 dimensions, LAGA cuts collective communication 1.98x, matches explicit memory within 0.5%, is bit-identical to explicit at SP=1 and equivalent to within 1e-3 at SP=2-8, and under a fused attention kernel improves attention-block throughput 1.04-1.06x single-node and 1.07-1.24x cross-node -- leading at all sequence lengths in the cross-node regime MLA is deployed for. 但 Comm is per-layer and analytical, and the memory-trap mechanism ( intermediates) is structural and independent of depth; however, end-to-end wall-clock and MFU at full model depth (where attention’s share of total compute is smaller) remain future work. • Convergence at toy scale. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：Comm is per-layer and analytical, and the memory-trap mechanism ( intermediates) is structural and independent of depth; however, end-to-end wall-clock and MFU at full model depth (where attention’s share of total compute is smaller) remain future work. • Convergence at toy scale. 旧方案在不承受该约束时仍成立。

关联：`review:SF-2026-ARXIV-2607-17644`。
<!-- analysis:DA-20260721-02:end -->

<!-- analysis:DA-20260721-03:start -->
### ExpertPlex: A High-Goodput Disaggregated Serving System for MoE LLMs with Adaptive Persistent Kernels

**约束变化与机制。** We present ExpertPlex, which shares massive MoE experts across phases while disaggregating lightweight attention modules.

**证明与未证明。** Experiments serving MiniMax-M2.7 and GLM-5.1-FP8 show that ExpertPlex improves goodput by up to 2.01$\times$ over instance-level prefill-decode disaggregation and 1.66$\times$ over prefill-decode colocation. 但 Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 旧方案在不承受该约束时仍成立。

关联：`review:SF-2026-ARXIV-2607-18002`。
<!-- analysis:DA-20260721-03:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

None。建议路由已冻结到 date-local queue；最终 disposition 等待 root 按日期串行对读 Books。

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260721-COVERAGE-INDEPENDENT | fresh-context:pending-root-auditor | coverage | coverage:SRC-ARXIV:20260721 | GAP-20260721-COVERAGE-INDEPENDENT：全量筛选尚未被独立反向审计 | Pending — 逐项核验 false positive / false negative | open |
| SA-20260721-EVIDENCE-INDEPENDENT | fresh-context:pending-root-auditor | evidence | validator:review-completion-v1 | GAP-20260721-EVIDENCE-INDEPENDENT：RP 尚需独立对照 exact v1 | Pending — finding 绑定具体 family | open |
| SA-20260721-SELECTION-INDEPENDENT | fresh-context:pending-root-auditor | deep_analysis_selection | validator:deep-analysis-selection-v1 | GAP-20260721-SELECTION-INDEPENDENT：三项选择尚需 adversarial comparison | Pending — 比较 impact、反证与 owner 独立性 | open |
| SA-20260721-BOOKS-ROOT | fresh-context:pending-root-books-owner | books | validator:books-comparison-v1 | GAP-20260721-BOOKS-ROOT：尚未逐项对读 Books | Pending — root 消费 frozen queue | open |

## 8. Ignored Noise

772 项均有 family-specific pre-denominator closure：

- `embodied_task_local_method`：65
- `incremental_method_without_durable_system_delta`：587
- `local_benchmark_without_release_delta`：18
- `prior_retained_candidate`：6
- `theory_without_ai_system_contract`：17
- `vertical_application_without_system_delta`：79

## 9. Recommended Action

1. 独立审计 Coverage、Evidence 与 Selection；finding 只重开具体 family。
2. root 逐项比较 Books。建议起点：Integrate 32、No Change 112、Structural 3；不是最终决定。

## 10. Repository Changes

- 重建 `papers/2026/07/21/README.md` 及 date-local frozen queue。
- 未修改 Books、ROADMAP、docs、Learning State、Weekly。

## 11. Open Questions

- 独立审计是否恢复 closure 中的漏项？
- proposed Integrate 是否已被现有 Books 命题覆盖？

## 12. Sources

- [Deterministic Replay for AI Agent Systems](https://arxiv.org/pdf/2607.16200v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Masked Diffusion Language Models are Strong and Steerable Text-Based World Models for Agentic RL](https://arxiv.org/html/2607.16204v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [ColGraphRAG: Late-Interaction Evidence Retrieval for Multimodal GraphRAG](https://arxiv.org/html/2607.16208v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Accurate and Efficient Long-Term Memory for LLM Agents](https://arxiv.org/html/2607.16211v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [SelKV: Selective KV Cache Merging with Per-Token Merge-or-Drop and Attention Compensation](https://arxiv.org/html/2607.16213v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [RAIL Guard: Closing the Evaluation-to-Remediation Gap in Responsible AI for LLM Agents](https://arxiv.org/html/2607.16215v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [BACON: Budgeted Human Calibration for Modeling and Evaluation with Multiple AI Judges](https://arxiv.org/html/2607.16239v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [KernelBench-Verified: Do LLM-Generated Kernels Actually Beat PyTorch?](https://arxiv.org/html/2607.16241v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [TRACE: Trajectory-Based Safety Patch Learning for LLM Post-Training Realignment](https://arxiv.org/html/2607.16242v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [CIGPO: Contextual Information-Gain Policy Optimization for Multi-Turn Evidence-Reading LLM Agents](https://arxiv.org/html/2607.16244v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Let the Data Decide: Supervision Analysis, Capability Trade-offs, and Adaptive Objective Routing in Continued Pre-Training via Off-Policy Distillation](https://arxiv.org/html/2607.16246v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Self-Evolving Just-In-Time Memory for Proactive Embodied Safety](https://arxiv.org/html/2607.16247v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [High-accuracy Low-Bit KV-Cache Quantization via Local Distribution Restoration](https://arxiv.org/html/2607.16248v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [More Than Memory: Task-Conditioned Signed FFN Writes in Long-Context Retrieval](https://arxiv.org/html/2607.16254v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [From Outcomes to Actions: Leveraging Hindsight for Long-Horizon Language Agent Training](https://arxiv.org/html/2607.16257v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Quantifying Ranking Uncertainty in LLM Benchmarks](https://arxiv.org/html/2607.16259v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Composable Verification Pipelines for Multi-Agent Systems](https://arxiv.org/html/2607.16266v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [From Intent to Infrastructure: LLM-Driven Agent Compilers for ISAC Networks](https://arxiv.org/html/2607.16269v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Seeing What Is Actually There: PriVE-Bench and PriVE-Tools for Counterfactual Evaluation of Agentic Visual Evidence in VLMs](https://arxiv.org/html/2607.16311v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Depth-Regularized JEPA World Models Learn More Transferable Representations from Real Outdoor Robot Data](https://arxiv.org/html/2607.16314v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [CRISP: Pre-LLM Yet Text-Driven Visual Token Pruning for Efficient LVLM Inference](https://arxiv.org/html/2607.16326v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [LaCache: Exact Caching and Precision-Adaptive Inference for Diffusion Large Language Models](https://arxiv.org/html/2607.16339v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [AEVAL: From Anecdotal to Deterministic Testing for Agentic Skill Workflows](https://arxiv.org/html/2607.16345v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Clarify Before Executing: A Self-Evolving Agent for Resolving Intent Asymmetry in 3D Tool Orchestration](https://arxiv.org/html/2607.16352v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Apple-$π$: Benchmarking Thinking with Video Towards Law-Grounded Physical Intelligence](https://arxiv.org/html/2607.16401v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Signal-based Model Access Risk Analysis for AI System Operations Security](https://arxiv.org/html/2607.16414v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [One Modality to Forget Them All: Enhancing Cross-Modal Unlearning in Vision-Language Models](https://arxiv.org/html/2607.16442v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Committed Before Reasoning: Behavioral Reproduction and Preliminary Activation-Level Evidence of Answer Pre-Commitment in an Open-Weight LLM](https://arxiv.org/html/2607.16451v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Enabling Spatially Fine-Grained DVFS in Neural Processing Units for Energy-Efficient LLM Serving](https://arxiv.org/html/2607.16473v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Auto-Scaling Heterogeneous Neural Processing Units for Energy and Cost-Efficient LLM Serving](https://arxiv.org/html/2607.16488v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Foresight Residual RL for Long-Horizon Robot Manipulation with Vision-Language-Action Models](https://arxiv.org/html/2607.16506v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [SEER: Supervised Learning to Control Energetic Reasoning](https://arxiv.org/html/2607.16523v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Mitigating Compiler Fusion-Induced Power Bursts in Mobile NPU Inference as the Battery Depletes](https://arxiv.org/html/2607.16555v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [From Modalities to Propositions: A Language-Centric Framework for Multimodal Intelligence](https://arxiv.org/html/2607.16560v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Cold-Start Model Delivery in Kubernetes Inference Serving: An Empirical Study of OCI-Based Distribution and Its Integrity](https://arxiv.org/html/2607.16596v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [PAVXploreRL: Physical-Action-Visual World Model Reinforcement Learning with Action Exploration](https://arxiv.org/html/2607.16602v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Backpropagation-Free Trunk Training via the Split Forward Gradients](https://arxiv.org/html/2607.16612v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [DataFlow-Harness: A Grounded Code-Agent Platform for Constructing Editable LLM Data Pipelines](https://arxiv.org/html/2607.16617v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [From Memory to Skills: Evidence-Grounded Co-Evolution Governance for Long-Horizon LLM Agents](https://arxiv.org/html/2607.16621v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [CLOSER-Bench: Evaluating Budgeted Cross-Stage Design Closure for Hardware Agents](https://arxiv.org/html/2607.16632v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [PhyAgentOS: A Self-Evolving Operating System for Embodied Agents with Decoupled Cognitive Planning and Physical Execution](https://arxiv.org/html/2607.16636v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Diversity-Oriented Fine-Tuning for Uncertainty-Based Hallucination Detection](https://arxiv.org/html/2607.16643v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Falsification-Based Verification of LLM-Generated Optimization Models: Sound Test Batteries and Their Detection Limits](https://arxiv.org/html/2607.16646v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Synchronization-Free Algebraic Fingerprints for Large Language Models: From Autoregressive to Diffusion Models](https://arxiv.org/html/2607.16648v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [SpecLA: Efficient Speculative Decoding for Linear-Attention Models](https://arxiv.org/html/2607.16673v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Though Language Models Err While They Strive: Conformal Prediction for Self-Correcting Scientific Generation](https://arxiv.org/html/2607.16704v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Model-Driven Discipline for Multi-Agent LLMs: Requirement-to-Verification Generation of Traceable System Models](https://arxiv.org/html/2607.16708v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Towards Inference-Aware Privacy Guidance for Data Preparation](https://arxiv.org/html/2607.16710v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [RECON: Benchmarking Agent Memory for Compositional Reasoning over Long Contexts](https://arxiv.org/html/2607.16716v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Half the Experts, All the Code: One-Shot Domain Pruning of Mixture-of-Experts LLMs for Coding](https://arxiv.org/html/2607.16721v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Can Experts Adapt Without Training? On Test-Time Modality Generalization in MVLMs](https://arxiv.org/html/2607.16726v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Agentic Code Review in the Terminal: A Trajectory-Level Analysis of Behavior, Cost, and Human-Alignment](https://arxiv.org/html/2607.16740v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [RELIC: Revealed Principles for Learning Interpretable Composable Skills in Multi-Agent Planning](https://arxiv.org/html/2607.16745v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Roomie: Interference-Aware Colocation for Efficient Model Serving](https://arxiv.org/html/2607.16784v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [MultiLoReFT: Decoupling Shared and Modality-Specific Subspaces in Multimodal Learning via Low-Rank Representation Fine-Tuning](https://arxiv.org/html/2607.16789v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Identity-Paired Progressive Depth Training: When Trainability Persists Beyond Expressibility](https://arxiv.org/html/2607.16800v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Beyond Storage: State as a Runtime Control Problem in Parallel and Distributed Systems](https://arxiv.org/html/2607.16836v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Beyond Memory Leaderboards: Evaluating Scientific Memory as Budgeted Context Restoration](https://arxiv.org/html/2607.16848v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [AgentBrew: Lifelong Knowledge Brewing from Strong Teachers to Weak LLM Agents](https://arxiv.org/html/2607.16851v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Beyond Semantic Equivalence: Logical Graphs for LLM Uncertainty Quantification](https://arxiv.org/html/2607.16868v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Trace-Based On-Policy Distillation for Masked Diffusion Language Models](https://arxiv.org/html/2607.16872v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Robust KV Cache Management for LLM Serving under Output Token Length Uncertainty](https://arxiv.org/html/2607.16892v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Environment-free Synthetic Data Generation for API-Calling Agents](https://arxiv.org/html/2607.16900v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [TurboVec: A Case Study in Cost-Efficient Private Retrieval for Enterprise RAG via Codebook-Oblivious Quantization](https://arxiv.org/html/2607.16973v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Counterfactual Shapley Credit Assignment](https://arxiv.org/html/2607.16999v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Regularize or Localize: When Training-Time KV-Cache Geometry Pays Under Quantization](https://arxiv.org/html/2607.17019v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [LMEdge: QoS-Aware LLM Inference Orchestration on Edge Clusters](https://arxiv.org/html/2607.17175v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Talaria: Session-Aware Serverless Serving of Hundred-Billion-Parameter LLMs](https://arxiv.org/html/2607.17181v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [UPAIR: Diagnosing Reasoning States via Uncertainty-Progress Alignment for Selective Intervention](https://arxiv.org/html/2607.17188v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [A Systematic Evaluation of Trajectory Data Curation for LoRA Fine-Tuning of Code Agents](https://arxiv.org/pdf/2607.17205v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Retriever: Composing Closed-Loop Asynchronous Robot Programs](https://arxiv.org/html/2607.17213v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Specifying the Delegated-Autonomy Boundary: Requirements Engineering for Agentic AI](https://arxiv.org/html/2607.17225v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Distilled Reinforcement Learning for LLM Post-training](https://arxiv.org/html/2607.17247v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [EvolvingWorld: An Open-Schema Framework for Co-Evolving Role-Play Agents and World Model in Interactive Literary World](https://arxiv.org/html/2607.17250v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Asynchronous Multimodal Diffusion Policy Composition via Latency-Aware Guidance Fusion](https://arxiv.org/html/2607.17257v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [An Explicit World Model Based on Data-First Ontology: DaoQL Multimodal Storage Validation and Counterfactual Reasoning Evaluation](https://arxiv.org/html/2607.17269v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [SAGA: Synthetic Agentic Graph Architecture for Temporal Benchmark Generation](https://arxiv.org/html/2607.17288v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [DRNOISE: Benchmarking Deep Research Agents in Misleading Evidence Environments](https://arxiv.org/html/2607.17291v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [WAR: Workload-Aware Rollouts for Synchronous Agentic Reinforcement Learning](https://arxiv.org/html/2607.17299v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Adapting Embedding Models for Agent Capability Retrieval](https://arxiv.org/html/2607.17347v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Self-Modifying Lean Proof Agents with Verifier-Grounded Benchmark Coevolution](https://arxiv.org/html/2607.17352v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Quantifying Diversity of Thought: A Predictive Law of Weighted LLM Ensemble Lift](https://arxiv.org/html/2607.17384v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Portable models as a replacement for industrial heuristics in compiler optimizations](https://arxiv.org/html/2607.17389v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Efficient Sequential Evaluation of Large Language Models](https://arxiv.org/html/2607.17409v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Transition-Aware Backend Dispatch for Edge LLM Inference](https://arxiv.org/html/2607.17415v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Kernelized Linear Attention: Breaking the Capacity Wall with Symmetric Cones](https://arxiv.org/html/2607.17419v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [LATTICE: Constraint-Directed Scheduling, Memory Planning, and Pipeline Refinement for NPUs](https://arxiv.org/html/2607.17422v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Decoder-Preserving Sparse Autoencoders: Which Readouts Survive Sparse Compression?](https://arxiv.org/html/2607.17425v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Test-Time Scaling for World Action Models via Zero-Shot Geometric Evaluation](https://arxiv.org/html/2607.17454v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [FailureAtlas: A Taxonomy of Failure Modes in Multi-Provider LLM Serving Infrastructure](https://arxiv.org/html/2607.17525v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Can AI Agents Really Complete RTL-to-GDS? Lessons from Benchmarking Tool-Interactive EDA Workflows](https://arxiv.org/html/2607.17528v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Salience Induction against Multi-Hop RAG Agents: Threat and Defense](https://arxiv.org/html/2607.17535v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Retain or Consolidate? Budget-Dependent Operator Selection for Language Agent Memory](https://arxiv.org/html/2607.17545v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Why Does Feedback-Augmented Self-Distillation Fail to Improve Retrieval-Interleaved Search Agents?](https://arxiv.org/html/2607.17558v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [CoCurve: Cross-Module Co-Pruning Curvature for Training-Free Structured LLM Pruning](https://arxiv.org/html/2607.17568v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [JAGG: Jacobian-Aggregated Group Gradient for Efficient GRPO Training of Diffusion Models](https://arxiv.org/html/2607.17572v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Predictive Training with Latent Imagination for Visual Quadruped Navigation](https://arxiv.org/html/2607.17574v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [A Dual-Hypothesis Reasoning Framework for LLM Guardrails](https://arxiv.org/html/2607.17575v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Is Progressive Disclosure All You Need for Long-Context Agents?](https://arxiv.org/html/2607.17598v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Insecure Coding Preferences in Long-Term Memory: Security Risks for LLM-based Code Generation](https://arxiv.org/html/2607.17619v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Mechanistic Attention Guidance for Agent Memory Refinement](https://arxiv.org/html/2607.17621v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Can Transformers Really Do It All? On the Compatibility of Inductive Biases Across Tasks](https://arxiv.org/html/2607.17624v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Verify, Repair, Repeat, or Stop? Robust Stopping for Noisy Verify-Repair Loops in LLM Agents](https://arxiv.org/html/2607.17641v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [A Training-Memory Regression in MLA Sequence Parallelism: Why Megatron-Core Forbids Absorption, and LAGA -- a Communication-Efficient Fix](https://arxiv.org/html/2607.17644v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [FlowBlock: Wavefront-Parallel Decoding for Self-Correcting Diffusion Language Models](https://arxiv.org/html/2607.17652v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Beyond Objective Expressivity: Geometry Preservation in Multimodal Contrastive Learning](https://arxiv.org/html/2607.17673v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [An Adjoint-Sensitivity Framework for Lost-in-the-Middle Phenomena in Causal Residual Transformers](https://arxiv.org/html/2607.17696v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [ProEvent: An Event-centric Benchmark for Proactive Agents](https://arxiv.org/html/2607.17701v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Planning with Transformers: Chain of Computation and Structured Context Windows](https://arxiv.org/html/2607.17710v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [C$^2$KV: Compressed and Composable KV Cache Reuse for Efficient LLM Inference](https://arxiv.org/html/2607.17715v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [MXSens: Sensitivity-Aware Mixed-Precision Quantization for Efficient LLM Inference](https://arxiv.org/html/2607.17733v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [MagicSelector: Joint Optimization for Agent Tool Selection via Counterfactual Decomposition and Progressive Reranking](https://arxiv.org/html/2607.17751v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [ETAS: An Effect-Typed Language for Agent Systems](https://arxiv.org/html/2607.17780v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Reasoning as a Double-Edged Sword: Architecture and Cross-Stage Robustness in Vision-Language-Action Models](https://arxiv.org/html/2607.17786v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Mobius Learning: Cyclic Depth Folding in Transformers](https://arxiv.org/html/2607.17843v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Exploratory and Assimilating Reflection: Reflective Recall Cycle for Long-term Memory](https://arxiv.org/html/2607.17879v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [ST-Veto: Spatio-Temporal Token Veto for Diffusion MLLMs via Taylor Prediction and Visual Grounding](https://arxiv.org/html/2607.17884v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Value-Aware Prediction for Robust Multi-Agent Coordination Under Communication Loss](https://arxiv.org/html/2607.17914v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Aggregate in the Advantage, Not the Ratio: A Canonical-Form Analysis of Cooperative Multi-Agent Policy Optimization](https://arxiv.org/html/2607.17924v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [When and How Context Rot Appears in Coding Agents: A White-Box Study of Agent Skills in Code Auditing](https://arxiv.org/html/2607.17937v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [SAGE: Subgoal-Conditioned Action Generation for Latent World Model Planning](https://arxiv.org/html/2607.17973v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Harness Engineering for LLM-Driven GPU Kernel Generation](https://arxiv.org/html/2607.17979v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Self-State Attacks on Self-Hosted AI Agents: How Far Can OS Defenses Go?](https://arxiv.org/html/2607.17986v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [ExpertPlex: A High-Goodput Disaggregated Serving System for MoE LLMs with Adaptive Persistent Kernels](https://arxiv.org/html/2607.18002v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Closing the Loop in Humanoid VLA: Persistent 3D Object Tokens for Verifiable Loco-Manipulation](https://arxiv.org/html/2607.18016v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Rethinking Heterogeneous LLM Merging: A Weighted Model Averaging Perspective](https://arxiv.org/html/2607.18026v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Evidence-in-the-Loop: Trace-Driven Optimization for Customer-Service LLM Agents](https://arxiv.org/html/2607.18039v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [SEE: Structure-aware Exploring &amp; Exploiting for Long-horizon GUI Agent Trajectory Synthesis](https://arxiv.org/html/2607.18046v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Test Coverage Analysis of Agentic Pull Requests](https://arxiv.org/html/2607.18057v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [RoboHarness: Memory-Driven Orchestration of Heterogeneous Robot Policies for Long-Horizon Planning](https://arxiv.org/html/2607.18060v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Adaptive Adversaries: A Multi-Turn, Multi-LLM Benchmark for LLM Agent Security](https://arxiv.org/html/2607.18063v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Sparse Evidence Can Suffice: Agentic Evidence Seeking for Multimodal Video Misinformation Detection](https://arxiv.org/html/2607.18080v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [SelectInfer: Selective Neuron Loading and Computation for On-Device LLMs](https://arxiv.org/html/2607.18081v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Judge-dependent safety gains and model-specific helpfulness costs of evidence-sufficiency prompting in clinical LLMs](https://arxiv.org/pdf/2607.18086v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [VDAR-Router: Adaptive LLMs Routing via Verbalized Query Difficulty Analysis Retrieval](https://arxiv.org/html/2607.18098v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Can We Break LLMs Out of Self-Loops? Fine-Grained Reasoning Control with Activation Steering](https://arxiv.org/html/2607.18100v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Empowering On-Device Model Adaptation with an Edge AI Inference Accelerator](https://arxiv.org/html/2607.18101v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [GARAGE: Characterizing the Automation Boundary in LLM-based Attack Graph Generation](https://arxiv.org/html/2607.18108v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [LLM-as-a-Coach: Experiential Learning for Non-Verifiable Tasks](https://arxiv.org/html/2607.18110v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [How Does Alignment Tuning Shape Representations of Sycophancy and Related Cue-Induced Biases in LLMs?](https://arxiv.org/html/2607.18114v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [A CXL Memory Rack for Multi-Turn LLM Serving](https://arxiv.org/html/2607.18141v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [Testing Retrieval-Augmented Generation Systems with Chunk Coverage](https://arxiv.org/html/2607.18155v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [TRIM: Reducing AI-Generated CodeSlop via Agent Trajectory Minimization](https://arxiv.org/html/2607.18161v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [FlashRT: Agent Harness for Guiding Agents to Deploy Real-Time Multimodal Applications](https://arxiv.org/html/2607.18171v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [PPL-Factory: Task-Aware and Budget-Aware Data Selection from Language Modeling to Reasoning](https://arxiv.org/html/2607.18199v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [SWE-Pruner Pro: The Coder LLM Already Knows What to Prune](https://arxiv.org/html/2607.18213v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04
- [FM-VLA: Force-based Memory for Vision-Language-Action Models in Contact-Rich Manipulation](https://arxiv.org/html/2607.18231v1) — first-public（Asia/Shanghai）：2026-07-21；exact evidence：v1；accessed：2026-09-04

## 13. Final Status

Author-side screening、denominator、exact-v1 access、147/147 Review 与 Deep Selection receipt 已构建；Books 写回冻结，四项独立审计未完成。

State Truth: Completion=In Progress；Coverage=Open；Evidence=Open；Books=Open；Unresolved Findings=4。
