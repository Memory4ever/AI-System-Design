# Daily Research — 2026-05-28

**Research Date:** 2026-05-28

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-05-27 09:00:00 ～ 2026-05-28 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；DataCite 只用于 identity/date/abstract recovery，技术结论绑定 official arXiv exact-v1。

**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed。10/10 canonical writebacks 已通过非写作者 fresh-context post-write semantic audit。

## Executive Summary

相邻月份 v2 快照共 91,841 条 raw records；严格窗口注册并逐项 title+abstract 语义筛选 747/747。最终 denominator=112（14.99%），pre-denominator closures=635；112/112 retained family 已完成 official exact-v1 Method/Evaluation/Limitations/Artifact review，blocked=0、ordinary pending=0；10 项 canonical queue 已写回并通过 10/10 post-write semantic audit。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-05-28 |
| Window End | 2026-05-28 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | DEN-20260528-V1-FINAL-112 |
| Denominator Frozen At | 2026-09-02T10:30:00+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-05-27T09:00:00+08:00 | 2026-05-28T09:00:00+08:00 | 2026-09-02T10:30:00+08:00 | DataCite v2 monthly prefixes 00..99; full title+abstract semantic screen; official exact-v1 HTML→PDF | checked | 747 | SF-2026-ARXIV-2605-27820;SF-2026-ARXIV-2605-27825;SF-2026-ARXIV-2605-27850;SF-2026-ARXIV-2605-27879;SF-2026-ARXIV-2605-27881;SF-2026-ARXIV-2605-27898;SF-2026-ARXIV-2605-27899;SF-2026-ARXIV-2605-27901;SF-2026-ARXIV-2605-27918;SF-2026-ARXIV-2605-27922;SF-2026-ARXIV-2605-27947;SF-2026-ARXIV-2605-27954;SF-2026-ARXIV-2605-27957;SF-2026-ARXIV-2605-27963;SF-2026-ARXIV-2605-27980;SF-2026-ARXIV-2605-27995;SF-2026-ARXIV-2605-28000;SF-2026-ARXIV-2605-28009;SF-2026-ARXIV-2605-28017;SF-2026-ARXIV-2605-28044;SF-2026-ARXIV-2605-28046;SF-2026-ARXIV-2605-28053;SF-2026-ARXIV-2605-28071;SF-2026-ARXIV-2605-28074;SF-2026-ARXIV-2605-28083;SF-2026-ARXIV-2605-28095;SF-2026-ARXIV-2605-28097;SF-2026-ARXIV-2605-28108;SF-2026-ARXIV-2605-28112;SF-2026-ARXIV-2605-28116;SF-2026-ARXIV-2605-28122;SF-2026-ARXIV-2605-28158;SF-2026-ARXIV-2605-28201;SF-2026-ARXIV-2605-28213;SF-2026-ARXIV-2605-28214;SF-2026-ARXIV-2605-28224;SF-2026-ARXIV-2605-28282;SF-2026-ARXIV-2605-28302;SF-2026-ARXIV-2605-28354;SF-2026-ARXIV-2605-28371;SF-2026-ARXIV-2605-28384;SF-2026-ARXIV-2605-28390;SF-2026-ARXIV-2605-28424;SF-2026-ARXIV-2605-28433;SF-2026-ARXIV-2605-28467;SF-2026-ARXIV-2605-28480;SF-2026-ARXIV-2605-28508;SF-2026-ARXIV-2605-28510;SF-2026-ARXIV-2605-28544;SF-2026-ARXIV-2605-28561;SF-2026-ARXIV-2605-28565;SF-2026-ARXIV-2605-28573;SF-2026-ARXIV-2605-28617;SF-2026-ARXIV-2605-28632;SF-2026-ARXIV-2605-28634;SF-2026-ARXIV-2605-28640;SF-2026-ARXIV-2605-28646;SF-2026-ARXIV-2605-28678;SF-2026-ARXIV-2605-28691;SF-2026-ARXIV-2605-28699;SF-2026-ARXIV-2605-28704;SF-2026-ARXIV-2605-28721;SF-2026-ARXIV-2605-28726;SF-2026-ARXIV-2605-28732;SF-2026-ARXIV-2605-28742;SF-2026-ARXIV-2605-28751;SF-2026-ARXIV-2605-28760;SF-2026-ARXIV-2605-28764;SF-2026-ARXIV-2605-28773;SF-2026-ARXIV-2605-28774;SF-2026-ARXIV-2605-28778;SF-2026-ARXIV-2605-28787;SF-2026-ARXIV-2605-28803;SF-2026-ARXIV-2605-28805;SF-2026-ARXIV-2605-28807;SF-2026-ARXIV-2605-28819;SF-2026-ARXIV-2605-28889;SF-2026-ARXIV-2605-28890;SF-2026-ARXIV-2605-28893;SF-2026-ARXIV-2605-28897;SF-2026-ARXIV-2605-28914;SF-2026-ARXIV-2605-28918;SF-2026-ARXIV-2605-28920;SF-2026-ARXIV-2605-28969;SF-2026-ARXIV-2605-28991;SF-2026-ARXIV-2605-28999;SF-2026-ARXIV-2605-29001;SF-2026-ARXIV-2605-29005;SF-2026-ARXIV-2605-29054;SF-2026-ARXIV-2605-29068;SF-2026-ARXIV-2605-29074;SF-2026-ARXIV-2605-29075;SF-2026-ARXIV-2605-29078;SF-2026-ARXIV-2605-29082;SF-2026-ARXIV-2605-29087;SF-2026-ARXIV-2605-29107;SF-2026-ARXIV-2605-29114;SF-2026-ARXIV-2605-29115;SF-2026-ARXIV-2605-29119;SF-2026-ARXIV-2605-29121;SF-2026-ARXIV-2605-29123;SF-2026-ARXIV-2605-29129;SF-2026-ARXIV-2605-29135;SF-2026-ARXIV-2605-29139;SF-2026-ARXIV-2605-29156;SF-2026-ARXIV-2605-29178;SF-2026-ARXIV-2605-29183;SF-2026-ARXIV-2605-29192;SF-2026-ARXIV-2605-29209;SF-2026-ARXIV-2606-07586;SF-2026-ARXIV-2606-26120;SF-2026-ARXIV-2606-26122 | pages=300; final_cursor=end; raw=91841; registered=747; screened=747; retained=112; closure=635 | 2026-05-28T00:59:59Z | screening-ledger-final.json#sha256=8590de0194dd155a8224e2b768d6a104588e6bd6044befb21d0bb2283db03f57 | — |

### Coverage Limitations

<!-- coverage:SRC-ARXIV:20260528:start -->747/747 registered identity 已逐项语义筛选；112 family exact-v1 可访问，635 family 有具名 closure 与重开条件。反例审计从 closure 重开 12 项系统级 family。Coverage 无未解决 finding；外部 estimate、代码 commit 与未披露 benchmark 字段不被反推。<!-- coverage:SRC-ARXIV:20260528:end -->

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-27820 | arXiv:2605.27820v1 | paper-v1:2605.27820 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-27820 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27820 | no |
| SF-2026-ARXIV-2605-27825 | arXiv:2605.27825v1 | paper-v1:2605.27825 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-27825 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2605-27825 | no |
| SF-2026-ARXIV-2605-27850 | arXiv:2605.27850v1 | paper-v1:2605.27850 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-27850 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27850 | no |
| SF-2026-ARXIV-2605-27879 | arXiv:2605.27879v1 | paper-v1:2605.27879 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-27879 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27879 | no |
| SF-2026-ARXIV-2605-27881 | arXiv:2605.27881v1 | paper-v1:2605.27881 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-27881 | self | — | new_in_window | TRAIN-DATA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27881 | no |
| SF-2026-ARXIV-2605-27898 | arXiv:2605.27898v1 | paper-v1:2605.27898 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-27898 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27898 | no |
| SF-2026-ARXIV-2605-27899 | arXiv:2605.27899v1 | paper-v1:2605.27899 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-27899 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27899 | no |
| SF-2026-ARXIV-2605-27901 | arXiv:2605.27901v1 | paper-v1:2605.27901 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-27901 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27901 | no |
| SF-2026-ARXIV-2605-27918 | arXiv:2605.27918v1 | paper-v1:2605.27918 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-27918 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27918 | no |
| SF-2026-ARXIV-2605-27922 | arXiv:2605.27922v1 | paper-v1:2605.27922 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-27922 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27922 | no |
| SF-2026-ARXIV-2605-27947 | arXiv:2605.27947v1 | paper-v1:2605.27947 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-27947 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27947 | no |
| SF-2026-ARXIV-2605-27954 | arXiv:2605.27954v1 | paper-v1:2605.27954 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-27954 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27954 | no |
| SF-2026-ARXIV-2605-27957 | arXiv:2605.27957v1 | paper-v1:2605.27957 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-27957 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27957 | no |
| SF-2026-ARXIV-2605-27963 | arXiv:2605.27963v1 | paper-v1:2605.27963 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-27963 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27963 | no |
| SF-2026-ARXIV-2605-27980 | arXiv:2605.27980v1 | paper-v1:2605.27980 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-27980 | self | — | new_in_window | MODEL-POSITION-ENCODING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27980 | no |
| SF-2026-ARXIV-2605-27995 | arXiv:2605.27995v1 | paper-v1:2605.27995 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-27995 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27995 | no |
| SF-2026-ARXIV-2605-28000 | arXiv:2605.28000v1 | paper-v1:2605.28000 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28000 | self | — | new_in_window | AGENT-TOOL-CALLING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28000 | no |
| SF-2026-ARXIV-2605-28009 | arXiv:2605.28009v1 | paper-v1:2605.28009 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28009 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28009 | no |
| SF-2026-ARXIV-2605-28017 | arXiv:2605.28017v1 | paper-v1:2605.28017 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28017 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28017 | no |
| SF-2026-ARXIV-2605-28044 | arXiv:2605.28044v1 | paper-v1:2605.28044 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28044 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28044 | no |
| SF-2026-ARXIV-2605-28046 | arXiv:2605.28046v1 | paper-v1:2605.28046 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28046 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28046 | no |
| SF-2026-ARXIV-2605-28053 | arXiv:2605.28053v1 | paper-v1:2605.28053 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-28053 | self | — | new_in_window | INFER-CONTINUOUS-BATCHING | Integrate | books-review:SF-2026-ARXIV-2605-28053 | no |
| SF-2026-ARXIV-2605-28071 | arXiv:2605.28071v1 | paper-v1:2605.28071 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28071 | self | — | new_in_window | AGENT-TOOL-CALLING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28071 | no |
| SF-2026-ARXIV-2605-28074 | arXiv:2605.28074v1 | paper-v1:2605.28074 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28074 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28074 | no |
| SF-2026-ARXIV-2605-28083 | arXiv:2605.28083v1 | paper-v1:2605.28083 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28083 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28083 | no |
| SF-2026-ARXIV-2605-28095 | arXiv:2605.28095v1 | paper-v1:2605.28095 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-28095 | self | — | new_in_window | INFER-GPU-MEMORY | Integrate | books-review:SF-2026-ARXIV-2605-28095 | no |
| SF-2026-ARXIV-2605-28097 | arXiv:2605.28097v1 | paper-v1:2605.28097 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28097 | self | — | new_in_window | PLATFORM-PRODUCTION | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28097 | no |
| SF-2026-ARXIV-2605-28108 | arXiv:2605.28108v1 | paper-v1:2605.28108 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28108 | self | — | new_in_window | AGENT-PLANNING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28108 | no |
| SF-2026-ARXIV-2605-28112 | arXiv:2605.28112v1 | paper-v1:2605.28112 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28112 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28112 | no |
| SF-2026-ARXIV-2605-28116 | arXiv:2605.28116v1 | paper-v1:2605.28116 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28116 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28116 | no |
| SF-2026-ARXIV-2605-28122 | arXiv:2605.28122v1 | paper-v1:2605.28122 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28122 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28122 | no |
| SF-2026-ARXIV-2605-28158 | arXiv:2605.28158v1 | paper-v1:2605.28158 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28158 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28158 | no |
| SF-2026-ARXIV-2605-28201 | arXiv:2605.28201v1 | paper-v1:2605.28201 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-28201 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2605-28201 | no |
| SF-2026-ARXIV-2605-28213 | arXiv:2605.28213v1 | paper-v1:2605.28213 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28213 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28213 | no |
| SF-2026-ARXIV-2605-28214 | arXiv:2605.28214v1 | paper-v1:2605.28214 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-28214 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28214 | no |
| SF-2026-ARXIV-2605-28224 | arXiv:2605.28224v1 | paper-v1:2605.28224 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28224 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28224 | no |
| SF-2026-ARXIV-2605-28282 | arXiv:2605.28282v1 | paper-v1:2605.28282 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28282 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28282 | no |
| SF-2026-ARXIV-2605-28302 | arXiv:2605.28302v1 | paper-v1:2605.28302 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28302 | self | — | new_in_window | INFER-PD-DISAGGREGATION | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28302 | no |
| SF-2026-ARXIV-2605-28354 | arXiv:2605.28354v1 | paper-v1:2605.28354 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28354 | self | — | new_in_window | AGENT-PLANNING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28354 | no |
| SF-2026-ARXIV-2605-28371 | arXiv:2605.28371v1 | paper-v1:2605.28371 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28371 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28371 | no |
| SF-2026-ARXIV-2605-28384 | arXiv:2605.28384v1 | paper-v1:2605.28384 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28384 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28384 | no |
| SF-2026-ARXIV-2605-28390 | arXiv:2605.28390v1 | paper-v1:2605.28390 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28390 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28390 | no |
| SF-2026-ARXIV-2605-28424 | arXiv:2605.28424v1 | paper-v1:2605.28424 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28424 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28424 | no |
| SF-2026-ARXIV-2605-28433 | arXiv:2605.28433v1 | paper-v1:2605.28433 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-28433 | self | — | new_in_window | AGENT-MULTI-AGENT | Integrate | books-review:SF-2026-ARXIV-2605-28433 | no |
| SF-2026-ARXIV-2605-28467 | arXiv:2605.28467v1 | paper-v1:2605.28467 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28467 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28467 | no |
| SF-2026-ARXIV-2605-28480 | arXiv:2605.28480v1 | paper-v1:2605.28480 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28480 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28480 | no |
| SF-2026-ARXIV-2605-28508 | arXiv:2605.28508v1 | paper-v1:2605.28508 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28508 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28508 | no |
| SF-2026-ARXIV-2605-28510 | arXiv:2605.28510v1 | paper-v1:2605.28510 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28510 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28510 | no |
| SF-2026-ARXIV-2605-28544 | arXiv:2605.28544v1 | paper-v1:2605.28544 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28544 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28544 | no |
| SF-2026-ARXIV-2605-28561 | arXiv:2605.28561v1 | paper-v1:2605.28561 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28561 | self | — | new_in_window | TRAIN-RLHF | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28561 | no |
| SF-2026-ARXIV-2605-28565 | arXiv:2605.28565v1 | paper-v1:2605.28565 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28565 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28565 | no |
| SF-2026-ARXIV-2605-28573 | arXiv:2605.28573v1 | paper-v1:2605.28573 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28573 | self | — | new_in_window | TRAIN-PRETRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28573 | no |
| SF-2026-ARXIV-2605-28617 | arXiv:2605.28617v1 | paper-v1:2605.28617 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-28617 | self | — | new_in_window | AGENT-TOOL-CALLING | Integrate | books-review:SF-2026-ARXIV-2605-28617 | no |
| SF-2026-ARXIV-2605-28632 | arXiv:2605.28632v1 | paper-v1:2605.28632 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-28632 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2605-28632 | no |
| SF-2026-ARXIV-2605-28634 | arXiv:2605.28634v1 | paper-v1:2605.28634 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28634 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28634 | no |
| SF-2026-ARXIV-2605-28640 | arXiv:2605.28640v1 | paper-v1:2605.28640 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28640 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28640 | no |
| SF-2026-ARXIV-2605-28646 | arXiv:2605.28646v1 | paper-v1:2605.28646 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-28646 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28646 | no |
| SF-2026-ARXIV-2605-28678 | arXiv:2605.28678v1 | paper-v1:2605.28678 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28678 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28678 | no |
| SF-2026-ARXIV-2605-28691 | arXiv:2605.28691v1 | paper-v1:2605.28691 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28691 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28691 | no |
| SF-2026-ARXIV-2605-28699 | arXiv:2605.28699v1 | paper-v1:2605.28699 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28699 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28699 | no |
| SF-2026-ARXIV-2605-28704 | arXiv:2605.28704v1 | paper-v1:2605.28704 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-28704 | self | — | new_in_window | INFER-TENSORRT-LLM | Integrate | books-review:SF-2026-ARXIV-2605-28704 | no |
| SF-2026-ARXIV-2605-28721 | arXiv:2605.28721v1 | paper-v1:2605.28721 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28721 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28721 | no |
| SF-2026-ARXIV-2605-28726 | arXiv:2605.28726v1 | paper-v1:2605.28726 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28726 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28726 | no |
| SF-2026-ARXIV-2605-28732 | arXiv:2605.28732v1 | paper-v1:2605.28732 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28732 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28732 | no |
| SF-2026-ARXIV-2605-28742 | arXiv:2605.28742v1 | paper-v1:2605.28742 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28742 | self | — | new_in_window | AGENT-REFLECTION | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28742 | no |
| SF-2026-ARXIV-2605-28751 | arXiv:2605.28751v1 | paper-v1:2605.28751 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28751 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28751 | no |
| SF-2026-ARXIV-2605-28760 | arXiv:2605.28760v1 | paper-v1:2605.28760 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-28760 | self | — | new_in_window | TRAIN-PRETRAINING | Integrate | books-review:SF-2026-ARXIV-2605-28760 | no |
| SF-2026-ARXIV-2605-28764 | arXiv:2605.28764v1 | paper-v1:2605.28764 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28764 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28764 | no |
| SF-2026-ARXIV-2605-28773 | arXiv:2605.28773v1 | paper-v1:2605.28773 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28773 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28773 | no |
| SF-2026-ARXIV-2605-28774 | arXiv:2605.28774v1 | paper-v1:2605.28774 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28774 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28774 | no |
| SF-2026-ARXIV-2605-28778 | arXiv:2605.28778v1 | paper-v1:2605.28778 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28778 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28778 | no |
| SF-2026-ARXIV-2605-28787 | arXiv:2605.28787v1 | paper-v1:2605.28787 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28787 | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28787 | no |
| SF-2026-ARXIV-2605-28803 | arXiv:2605.28803v1 | paper-v1:2605.28803 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28803 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28803 | no |
| SF-2026-ARXIV-2605-28805 | arXiv:2605.28805v1 | paper-v1:2605.28805 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28805 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28805 | no |
| SF-2026-ARXIV-2605-28807 | arXiv:2605.28807v1 | paper-v1:2605.28807 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28807 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28807 | no |
| SF-2026-ARXIV-2605-28819 | arXiv:2605.28819v1 | paper-v1:2605.28819 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28819 | self | — | new_in_window | TRAIN-LORA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28819 | no |
| SF-2026-ARXIV-2605-28889 | arXiv:2605.28889v1 | paper-v1:2605.28889 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28889 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28889 | no |
| SF-2026-ARXIV-2605-28890 | arXiv:2605.28890v1 | paper-v1:2605.28890 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28890 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28890 | no |
| SF-2026-ARXIV-2605-28893 | arXiv:2605.28893v1 | paper-v1:2605.28893 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28893 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28893 | no |
| SF-2026-ARXIV-2605-28897 | arXiv:2605.28897v1 | paper-v1:2605.28897 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28897 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28897 | no |
| SF-2026-ARXIV-2605-28914 | arXiv:2605.28914v1 | paper-v1:2605.28914 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28914 | self | — | new_in_window | AGENT-TOOL-CALLING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28914 | no |
| SF-2026-ARXIV-2605-28918 | arXiv:2605.28918v1 | paper-v1:2605.28918 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28918 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28918 | no |
| SF-2026-ARXIV-2605-28920 | arXiv:2605.28920v1 | paper-v1:2605.28920 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28920 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28920 | no |
| SF-2026-ARXIV-2605-28969 | arXiv:2605.28969v1 | paper-v1:2605.28969 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28969 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28969 | no |
| SF-2026-ARXIV-2605-28991 | arXiv:2605.28991v1 | paper-v1:2605.28991 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28991 | self | — | new_in_window | AGENT-TOOL-CALLING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28991 | no |
| SF-2026-ARXIV-2605-28999 | arXiv:2605.28999v1 | paper-v1:2605.28999 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28999 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28999 | no |
| SF-2026-ARXIV-2605-29001 | arXiv:2605.29001v1 | paper-v1:2605.29001 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-29001 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-29001 | no |
| SF-2026-ARXIV-2605-29005 | arXiv:2605.29005v1 | paper-v1:2605.29005 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-29005 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-29005 | no |
| SF-2026-ARXIV-2605-29054 | arXiv:2605.29054v1 | paper-v1:2605.29054 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-29054 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-29054 | no |
| SF-2026-ARXIV-2605-29068 | arXiv:2605.29068v1 | paper-v1:2605.29068 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-29068 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-29068 | no |
| SF-2026-ARXIV-2605-29074 | arXiv:2605.29074v1 | paper-v1:2605.29074 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-29074 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-29074 | no |
| SF-2026-ARXIV-2605-29075 | arXiv:2605.29075v1 | paper-v1:2605.29075 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-29075 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-29075 | no |
| SF-2026-ARXIV-2605-29078 | arXiv:2605.29078v1 | paper-v1:2605.29078 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-29078 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-29078 | no |
| SF-2026-ARXIV-2605-29082 | arXiv:2605.29082v1 | paper-v1:2605.29082 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-29082 | self | — | new_in_window | AGENT-PLATFORM | Integrate | books-review:SF-2026-ARXIV-2605-29082 | no |
| SF-2026-ARXIV-2605-29087 | arXiv:2605.29087v1 | paper-v1:2605.29087 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-29087 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-29087 | no |
| SF-2026-ARXIV-2605-29107 | arXiv:2605.29107v1 | paper-v1:2605.29107 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-29107 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-29107 | no |
| SF-2026-ARXIV-2605-29114 | arXiv:2605.29114v1 | paper-v1:2605.29114 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-29114 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-29114 | no |
| SF-2026-ARXIV-2605-29115 | arXiv:2605.29115v1 | paper-v1:2605.29115 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-29115 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-29115 | no |
| SF-2026-ARXIV-2605-29119 | arXiv:2605.29119v1 | paper-v1:2605.29119 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-29119 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-29119 | no |
| SF-2026-ARXIV-2605-29121 | arXiv:2605.29121v1 | paper-v1:2605.29121 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-29121 | self | — | new_in_window | MODEL-MOE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-29121 | no |
| SF-2026-ARXIV-2605-29123 | arXiv:2605.29123v1 | paper-v1:2605.29123 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-29123 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-29123 | no |
| SF-2026-ARXIV-2605-29129 | arXiv:2605.29129v1 | paper-v1:2605.29129 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-29129 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-29129 | no |
| SF-2026-ARXIV-2605-29135 | arXiv:2605.29135v1 | paper-v1:2605.29135 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-29135 | self | — | new_in_window | INFER-GPU-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-29135 | no |
| SF-2026-ARXIV-2605-29139 | arXiv:2605.29139v1 | paper-v1:2605.29139 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-29139 | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-29139 | no |
| SF-2026-ARXIV-2605-29156 | arXiv:2605.29156v1 | paper-v1:2605.29156 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-29156 | self | — | new_in_window | TRAIN-RLHF | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-29156 | no |
| SF-2026-ARXIV-2605-29178 | arXiv:2605.29178v1 | paper-v1:2605.29178 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-29178 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-29178 | no |
| SF-2026-ARXIV-2605-29183 | arXiv:2605.29183v1 | paper-v1:2605.29183 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-29183 | self | — | new_in_window | PLATFORM-PRODUCTION | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-29183 | no |
| SF-2026-ARXIV-2605-29192 | arXiv:2605.29192v1 | paper-v1:2605.29192 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-29192 | self | — | new_in_window | PLATFORM-TRACE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-29192 | no |
| SF-2026-ARXIV-2605-29209 | arXiv:2605.29209v1 | paper-v1:2605.29209 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-29209 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-29209 | no |
| SF-2026-ARXIV-2606-07586 | arXiv:2606.07586v1 | paper-v1:2606.07586 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2606-07586 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-07586 | no |
| SF-2026-ARXIV-2606-26120 | arXiv:2606.26120v1 | paper-v1:2606.26120 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2606-26120 | self | — | new_in_window | INFER-CONTINUOUS-BATCHING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-26120 | no |
| SF-2026-ARXIV-2606-26122 | arXiv:2606.26122v1 | paper-v1:2606.26122 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2606-26122 | self | — | new_in_window | TRAIN-DATA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-26122 | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-27820 | RP-155b8722fbc8b2b9 | deep | arXiv:2605.27820v1 | SRC-ARXIV@arXiv:2605.27820v1 | arXiv:2605.27820v1 — § exact heading: 3.3 Task Design and Ground-truth Annotation | arXiv:2605.27820v1 — § exact heading: 2.1 Tool-Using Benchmarks | arXiv:2605.27820v1 — § exact heading: 5 Conclusions | arXiv:2605.27820v1 — official HTML sha256=e084884e79524dd4bd757618cb34c671331dce1673eadac18e0b6881d86642d3; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-27820 | complete |
| SF-2026-ARXIV-2605-27825 | RP-c658005636a888e6 | deep | arXiv:2605.27825v1 | SRC-ARXIV@arXiv:2605.27825v1 | arXiv:2605.27825v1 — § exact heading: 3 Threat Model and Problem Formulation | arXiv:2605.27825v1 — § exact heading: 5 Experiments | arXiv:2605.27825v1 — § exact heading: 7 Conclusion and Limitations | arXiv:2605.27825v1 — official HTML sha256=778098e7df5cf172ed04989da043124faf4d825232bb02bbc1ceeeb0aa110f9a; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-27825 | complete |
| SF-2026-ARXIV-2605-27850 | RP-aae7181040b83a3f | deep | arXiv:2605.27850v1 | SRC-ARXIV@arXiv:2605.27850v1 | arXiv:2605.27850v1 — §3 Methods: unified prompt-topology genome and adaptive Pareto control | arXiv:2605.27850v1 — §4 Experiments: held-out accuracy, token cost and topology complexity | arXiv:2605.27850v1 — §5 Conclusion, Limitations, and Future Work | arXiv:2605.27850v1 — official exact-v1 HTML read; immutable repository/checkpoint commit Not Disclosed; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-27850 | complete |
| SF-2026-ARXIV-2605-27879 | RP-020f349e3469ca91 | deep | arXiv:2605.27879v1 | SRC-ARXIV@arXiv:2605.27879v1 | arXiv:2605.27879v1 — § exact heading: 3 Method: Faithful Agentic XAI | arXiv:2605.27879v1 — § exact heading: 4.2 Evaluation scenarios | arXiv:2605.27879v1 — § exact heading: 6 Conclusions | arXiv:2605.27879v1 — official HTML sha256=6414fd88678b2d30e7ef60804106d0d709040c51a69d5a37d2f507bfcb6a22c3; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-27879 | complete |
| SF-2026-ARXIV-2605-27881 | RP-c4854d16b833a898 | deep | arXiv:2605.27881v1 | SRC-ARXIV@arXiv:2605.27881v1 | arXiv:2605.27881v1 — § exact heading: 2.1 Reward Design for Search Agent | arXiv:2605.27881v1 — § exact heading: 3 Experiments Setup | arXiv:2605.27881v1 — § exact heading: Limitations | arXiv:2605.27881v1 — official HTML sha256=07bf6c9ae6e5fe2bbe5681bcaa7fbc987ad4ff370478f650c574244e5f99a760; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-27881 | complete |
| SF-2026-ARXIV-2605-27898 | RP-9a0327329c096038 | deep | arXiv:2605.27898v1 | SRC-ARXIV@arXiv:2605.27898v1 | arXiv:2605.27898v1 — § exact heading: 2 Unified Framework | arXiv:2605.27898v1 — § exact heading: 2.5 Evaluation Methodology | arXiv:2605.27898v1 — § exact heading: 3.5 Failure Result Analysis | arXiv:2605.27898v1 — official HTML sha256=7ee4e3fea5ae787e7b7369f9df610a0f7893a5f73d7d984cc659f19fc82c6ecd; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-27898 | complete |
| SF-2026-ARXIV-2605-27899 | RP-f9a707b07cfcef12 | deep | arXiv:2605.27899v1 | SRC-ARXIV@arXiv:2605.27899v1 | arXiv:2605.27899v1 — § exact heading: 3 Method | arXiv:2605.27899v1 — § exact heading: 4 Experiments | arXiv:2605.27899v1 — § exact heading: 5 Conclusion | arXiv:2605.27899v1 — official HTML sha256=54f2f7366208bc5806dd940984e523d58fd223db4b28a057e2ef039098f1f0ad; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-27899 | complete |
| SF-2026-ARXIV-2605-27901 | RP-e23ce50110f8dc9b | deep | arXiv:2605.27901v1 | SRC-ARXIV@arXiv:2605.27901v1 | arXiv:2605.27901v1 — § exact heading: 4 Can models conceal their reasoning across different languages? | arXiv:2605.27901v1 — § exact heading: 3 Experimental Setup | arXiv:2605.27901v1 — § exact heading: 8 Conclusion | arXiv:2605.27901v1 — official HTML sha256=a6ba0236d1abd1ae5608efa74db512b77c0445c54532de292db24bf296c6295c; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-27901 | complete |
| SF-2026-ARXIV-2605-27918 | RP-4eded30f71160a12 | deep | arXiv:2605.27918v1 | SRC-ARXIV@arXiv:2605.27918v1 | arXiv:2605.27918v1 — § exact heading: 2.1. MLLM Architecture and Parallelism | arXiv:2605.27918v1 — § exact heading: 4. Macroscopic Analysis-Based Model Parallelization | arXiv:2605.27918v1 — § exact heading: 2.3. Limitations of Existing Works | arXiv:2605.27918v1 — official HTML sha256=22c10a9201b86eead7234ee23182de2058869658bcc76c034c3d95bd886271f3; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-27918 | complete |
| SF-2026-ARXIV-2605-27922 | RP-98e56aea9aeea8cb | deep | arXiv:2605.27922v1 | SRC-ARXIV@arXiv:2605.27922v1 | arXiv:2605.27922v1 — § exact heading: 3.2 Task Suite Design and Validation | arXiv:2605.27922v1 — § exact heading: 3 The Harness-Bench Benchmark | arXiv:2605.27922v1 — § exact heading: 5.1 Observed Failure Symptoms | arXiv:2605.27922v1 — official HTML sha256=3e89c9f28b68276bc33fde7581b7a8428c53bb33ffa950e94aa7ed757cab807c; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-27922 | complete |
| SF-2026-ARXIV-2605-27947 | RP-a0b4bf3351a1c004 | deep | arXiv:2605.27947v1 | SRC-ARXIV@arXiv:2605.27947v1 | arXiv:2605.27947v1 — § exact heading: 3 Method | arXiv:2605.27947v1 — § exact heading: 4 Experiments | arXiv:2605.27947v1 — § exact heading: 5 Limitations | arXiv:2605.27947v1 — official HTML sha256=6775e77796d135354ae93c0db230ddba4574e84d3cf09c0aa4602b17ce622867; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-27947 | complete |
| SF-2026-ARXIV-2605-27954 | RP-fb73eba68c6c62df | deep | arXiv:2605.27954v1 | SRC-ARXIV@arXiv:2605.27954v1 | arXiv:2605.27954v1 — § exact heading: 1 Introduction | arXiv:2605.27954v1 — § exact heading: 4.2 Experimental Settings | arXiv:2605.27954v1 — § exact heading: 6 Conclusion | arXiv:2605.27954v1 — official HTML sha256=2b0011952bb538ff67435afde77b7104a2654683eeb7f17f4e3b82e26a89afa1; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-27954 | complete |
| SF-2026-ARXIV-2605-27957 | RP-6c465506657a35d9 | deep | arXiv:2605.27957v1 | SRC-ARXIV@arXiv:2605.27957v1 | arXiv:2605.27957v1 — § exact heading: 4.6 Reasoning-Optimized Models and Instruction Clash | arXiv:2605.27957v1 — § exact heading: 2.1 Tool-Augmented and Multi-Step Planning Benchmarks | arXiv:2605.27957v1 — § exact heading: 4.5 Failure Mode Analysis | arXiv:2605.27957v1 — official HTML sha256=248798608249a4b17d5fa271b948eefaf1bb5408fa419864abf81f260bc8c5e6; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-27957 | complete |
| SF-2026-ARXIV-2605-27963 | RP-c0ed21cde0c6e5ff | deep | arXiv:2605.27963v1 | SRC-ARXIV@arXiv:2605.27963v1 | arXiv:2605.27963v1 — § exact heading: 2.1. Analytical Models on Performance | arXiv:2605.27963v1 — § exact heading: 4.4. Resultant Topologies | arXiv:2605.27963v1 — § exact heading: 8. Conclusion | arXiv:2605.27963v1 — official HTML sha256=8ab4cf20fc446530aa8902eaa42a687c616adf1e944c3c43337c1bd8440106c7; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-27963 | complete |
| SF-2026-ARXIV-2605-27980 | RP-abf8fcc9a899d0c9 | deep | arXiv:2605.27980v1 | SRC-ARXIV@arXiv:2605.27980v1 | arXiv:2605.27980v1 — § exact heading: 3 Method | arXiv:2605.27980v1 — § exact heading: 4 Experimental Setup | arXiv:2605.27980v1 — § exact heading: 6 Limitations | arXiv:2605.27980v1 — official HTML sha256=20b0adb216b2e7b519721df4af90508fc41737dc57300f9be6baf9753f22ae78; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-27980 | complete |
| SF-2026-ARXIV-2605-27995 | RP-963ab6f4da612389 | deep | arXiv:2605.27995v1 | SRC-ARXIV@arXiv:2605.27995v1 | arXiv:2605.27995v1 — § exact heading: 2.1 Agent as a Concurrent Tool-Using System | arXiv:2605.27995v1 — § exact heading: 2.3 Evaluation | arXiv:2605.27995v1 — § exact heading: 4 Conclusion | arXiv:2605.27995v1 — official HTML sha256=707fad563547b29d77b0b377d0f1f896c52513d59f87543ff726262ca1f3754c; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-27995 | complete |
| SF-2026-ARXIV-2605-28000 | RP-22b5d5fbe8456ca9 | deep | arXiv:2605.28000v1 | SRC-ARXIV@arXiv:2605.28000v1 | arXiv:2605.28000v1 — § exact heading: 3 Tool Forge Conceptual Framework | arXiv:2605.28000v1 — § exact heading: 9 Experimental Protocol and Baselines | arXiv:2605.28000v1 — § exact heading: 12 Limitations and Open Questions | arXiv:2605.28000v1 — official HTML sha256=5ea862c3ec5aea65324f90f20db2c7c7596ccee5e7250bd3c1675ae44ca0644b; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28000 | complete |
| SF-2026-ARXIV-2605-28009 | RP-3cff817aad4f097f | deep | arXiv:2605.28009v1 | SRC-ARXIV@arXiv:2605.28009v1 | arXiv:2605.28009v1 — § exact heading: Appendix E Use of Large Language Models | arXiv:2605.28009v1 — § exact heading: 5 Experiment | arXiv:2605.28009v1 — § exact heading: 7 Conclusions and Future Work | arXiv:2605.28009v1 — official HTML sha256=d6dda2a87c59fd4d07ba02d92c5f0c24c14d09a1096ddb8d79481b5dacfdd055; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28009 | complete |
| SF-2026-ARXIV-2605-28017 | RP-2d0ae18e7db31381 | deep | arXiv:2605.28017v1 | SRC-ARXIV@arXiv:2605.28017v1 | arXiv:2605.28017v1 — § exact heading: 4.4 Attack Methods | arXiv:2605.28017v1 — § exact heading: 3.2 Attack Evaluation in Prior Work | arXiv:2605.28017v1 — § exact heading: 6 Conclusion | arXiv:2605.28017v1 — official HTML sha256=341b7d7e7c46ce09f8c492be68070b3f9c85e07da5caa6d219cea5e2dcf678b6; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28017 | complete |
| SF-2026-ARXIV-2605-28044 | RP-51205ceafa60aabf | deep | arXiv:2605.28044v1 | SRC-ARXIV@arXiv:2605.28044v1 | arXiv:2605.28044v1 — § exact heading: Appendix G Model API and Decoding Configuration | arXiv:2605.28044v1 — § exact heading: 5 Experiments | arXiv:2605.28044v1 — § exact heading: 6 Discussion | arXiv:2605.28044v1 — official HTML sha256=5b0d0423fc0dc00a6104deb2486a929aeab242779dfb2a336538c9d90949c46d; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28044 | complete |
| SF-2026-ARXIV-2605-28046 | RP-a6910dd3aec0b75a | deep | arXiv:2605.28046v1 | SRC-ARXIV@arXiv:2605.28046v1 | arXiv:2605.28046v1 — § exact heading: 2.4 Proactive Systems | arXiv:2605.28046v1 — § exact heading: 4 Experiments | arXiv:2605.28046v1 — § exact heading: 5 Discussion | arXiv:2605.28046v1 — official HTML sha256=9de207b19cc99467ce05fbe4668f2af43818fe87622c2f2b9f2a2336444ace08; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28046 | complete |
| SF-2026-ARXIV-2605-28053 | RP-e95e807f5254ea71 | deep | arXiv:2605.28053v1 | SRC-ARXIV@arXiv:2605.28053v1 | arXiv:2605.28053v1 — § exact heading: 2.1 Serving with Mutable Model State | arXiv:2605.28053v1 — § exact heading: 5 Evaluation | arXiv:2605.28053v1 — § exact heading: 6 Discussion | arXiv:2605.28053v1 — official HTML sha256=d97dad61bd6b3336151a29c7da781ff5a05a6ddc2691377489479fbed0a234c5; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28053 | complete |
| SF-2026-ARXIV-2605-28071 | RP-d9b51a5c7e98636f | deep | arXiv:2605.28071v1 | SRC-ARXIV@arXiv:2605.28071v1 | arXiv:2605.28071v1 — § exact heading: 1. Introduction | arXiv:2605.28071v1 — § exact heading: 2. AgentGuard | arXiv:2605.28071v1 — § exact heading: 3. Conclusion | arXiv:2605.28071v1 — official HTML sha256=ae831e1a6bf504005cadb4b6e87783430807af808aa4d411b1586ff15d1a4a10; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28071 | complete |
| SF-2026-ARXIV-2605-28074 | RP-ef161b2366a39f16 | deep | arXiv:2605.28074v1 | SRC-ARXIV@arXiv:2605.28074v1 | arXiv:2605.28074v1 — § exact heading: 3.2. Threat Model | arXiv:2605.28074v1 — § exact heading: 5. Experiments | arXiv:2605.28074v1 — § exact heading: 8. Limitations | arXiv:2605.28074v1 — official HTML sha256=0fe32804f286c87a8344023ffd30d5f490a312ecc2910c900d6ce0e8d95981ae; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28074 | complete |
| SF-2026-ARXIV-2605-28083 | RP-4fea9f2d41c73df0 | deep | arXiv:2605.28083v1 | SRC-ARXIV@arXiv:2605.28083v1 | arXiv:2605.28083v1 — § exact heading: 2.1 Vision-Language-Action Models | arXiv:2605.28083v1 — § exact heading: 4 Experiments | arXiv:2605.28083v1 — § exact heading: 3.1 Preliminaries & Threat Model | arXiv:2605.28083v1 — official HTML sha256=75a70820341d7c1995d5dcce0f6e2ef4087be2e4ee456e5403fa26986a59e552; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28083 | complete |
| SF-2026-ARXIV-2605-28095 | RP-03b7e12ebb47d4dc | deep | arXiv:2605.28095v1 | SRC-ARXIV@arXiv:2605.28095v1 | arXiv:2605.28095v1 — § exact heading: 2.1 Large Language Models | arXiv:2605.28095v1 — § exact heading: 5 Evaluation | arXiv:2605.28095v1 — § exact heading: 4.4 Discussion | arXiv:2605.28095v1 — official HTML sha256=5a35d6208f87777291ee083ee28d0ca39f8edf85bbf757764809c8cc70d60976; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28095 | complete |
| SF-2026-ARXIV-2605-28097 | RP-8d4627538694de50 | deep | arXiv:2605.28097v1 | SRC-ARXIV@arXiv:2605.28097v1 | arXiv:2605.28097v1 — § exact heading: 3. Design | arXiv:2605.28097v1 — § exact heading: 5. Evaluation | arXiv:2605.28097v1 — § exact heading: 5.5. Failure-Mode Taxonomy | arXiv:2605.28097v1 — official HTML sha256=414916db7f1e595f656d28986787a19c47a828a3a85d39a16a19704252d2638a; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28097 | complete |
| SF-2026-ARXIV-2605-28108 | RP-5539adb8f92fded8 | deep | arXiv:2605.28108v1 | SRC-ARXIV@arXiv:2605.28108v1 | arXiv:2605.28108v1 — § exact heading: Appendix B Runtime Framework | arXiv:2605.28108v1 — § exact heading: 2.2 Why ATR Resists Direct Evaluation | arXiv:2605.28108v1 — § exact heading: 6 Conclusion | arXiv:2605.28108v1 — official HTML sha256=955cb683e1219ce043363a3f80c8c78f68fcf31db7a68d671b8cbcbc921b93bd; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28108 | complete |
| SF-2026-ARXIV-2605-28112 | RP-7694f1692ae242dd | deep | arXiv:2605.28112v1 | SRC-ARXIV@arXiv:2605.28112v1 | arXiv:2605.28112v1 — § exact heading: 2.2 Threat Model and Attack Realism | arXiv:2605.28112v1 — § exact heading: 4 Experiments | arXiv:2605.28112v1 — § exact heading: 6 Conclusion | arXiv:2605.28112v1 — official HTML sha256=d0cbc74c408247a70679909334b0628c17fb424771394eb5869d80f3ad9c15f7; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28112 | complete |
| SF-2026-ARXIV-2605-28116 | RP-2235f77dfda50854 | deep | arXiv:2605.28116v1 | SRC-ARXIV@arXiv:2605.28116v1 | arXiv:2605.28116v1 — § exact heading: 3 Methodology | arXiv:2605.28116v1 — § exact heading: 4 Experiments | arXiv:2605.28116v1 — § exact heading: 3.1 Threat Model and Problem Setup | arXiv:2605.28116v1 — official HTML sha256=1468243f7898c335be4b2032a41fce144cd2cde51fbfa05bdec6192f398d54b1; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28116 | complete |
| SF-2026-ARXIV-2605-28122 | RP-efcc0ab75e4b2a81 | deep | arXiv:2605.28122v1 | SRC-ARXIV@arXiv:2605.28122v1 | arXiv:2605.28122v1 — § exact heading: 4 Methodology | arXiv:2605.28122v1 — § exact heading: 5 Evaluation | arXiv:2605.28122v1 — § exact heading: 6 Conclusion | arXiv:2605.28122v1 — official HTML sha256=2b2263367a509d311807ea14ffd2bbe1d4340d5061f31a11a4c27daea64d124d; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28122 | complete |
| SF-2026-ARXIV-2605-28158 | RP-ebb20f983db08816 | deep | arXiv:2605.28158v1 | SRC-ARXIV@arXiv:2605.28158v1 | arXiv:2605.28158v1 — § exact heading: 4.3. Workspace Setting Matters: Filesystem vs. Flat Prompt | arXiv:2605.28158v1 — § exact heading: 3. OR-Space Benchmark | arXiv:2605.28158v1 — § exact heading: 4.6. Failure Analysis: What Workspace Evaluation Reveals | arXiv:2605.28158v1 — official HTML sha256=1e17ba2cca067758b922a556965e0431d6551145b624769cbaad189a8f57f6d0; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28158 | complete |
| SF-2026-ARXIV-2605-28201 | RP-7a47d77b54d201fe | deep | arXiv:2605.28201v1 | SRC-ARXIV@arXiv:2605.28201v1 | arXiv:2605.28201v1 — § exact heading: 1 Introduction | arXiv:2605.28201v1 — § exact heading: 3 Benchmark Construction | arXiv:2605.28201v1 — § exact heading: 5 Conclusion | arXiv:2605.28201v1 — official HTML sha256=008668763414245306a7e06dd0162aab018a8ec8de1d63dca6d2c395d1635c86; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28201 | complete |
| SF-2026-ARXIV-2605-28213 | RP-6bdb01b2c64f13a8 | deep | arXiv:2605.28213v1 | SRC-ARXIV@arXiv:2605.28213v1 | arXiv:2605.28213v1 — § exact heading: 3 Method | arXiv:2605.28213v1 — § exact heading: 4 Evaluation | arXiv:2605.28213v1 — § exact heading: 5 Conclusion | arXiv:2605.28213v1 — official HTML sha256=5a6c29327a16eb486f3ab87c7947285bdc6cf70c05861afc9e6be33047d4bd05; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28213 | complete |
| SF-2026-ARXIV-2605-28214 | RP-362f30749375e765 | deep | arXiv:2605.28214v1 | SRC-ARXIV@arXiv:2605.28214v1 | arXiv:2605.28214v1 — § exact heading: 2.1 Latent-based Multi-Agent Systems | arXiv:2605.28214v1 — § exact heading: 4 Experiments | arXiv:2605.28214v1 — § exact heading: 2.3 Threat Model | arXiv:2605.28214v1 — official HTML sha256=91ee9043fb86499854c2113111e547d97fe383fdeafe52160c01d2cf035e9872; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28214 | complete |
| SF-2026-ARXIV-2605-28224 | RP-5a1fe49d3d0a89ee | deep | arXiv:2605.28224v1 | SRC-ARXIV@arXiv:2605.28224v1 | arXiv:2605.28224v1 — § exact heading: 3 A Unified Memory Framework | arXiv:2605.28224v1 — § exact heading: 4 Experimental Setup | arXiv:2605.28224v1 — § exact heading: 6 Discussion | arXiv:2605.28224v1 — official HTML sha256=f73c2b99847ff63b93b3448413df8cbc3980da4f411624734fb2481eb52a14b3; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28224 | complete |
| SF-2026-ARXIV-2605-28282 | RP-30f503e0fc304116 | deep | arXiv:2605.28282v1 | SRC-ARXIV@arXiv:2605.28282v1 | arXiv:2605.28282v1 — §3 ResearchLoop Protocol and Runtime; §4 Runtime Implementation | arXiv:2605.28282v1 — §7 controlled study and ablations | arXiv:2605.28282v1 — §7.2 synthetic task, single-model and sample-size limitations; Appendix C claim ledger | arXiv:2605.28282v1 — official exact-v1 HTML read; immutable repository/checkpoint commit Not Disclosed; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28282 | complete |
| SF-2026-ARXIV-2605-28302 | RP-e78b1e5187a252e9 | deep | arXiv:2605.28302v1 | SRC-ARXIV@arXiv:2605.28302v1 | arXiv:2605.28302v1 — § exact heading: 2.1 Design-Space Exploration for Optimal Disaggregated Inference | arXiv:2605.28302v1 — § exact heading: 4 Evaluation | arXiv:2605.28302v1 — § exact heading: 5 Discussion and Conclusion | arXiv:2605.28302v1 — official HTML sha256=d5bcb04b9f513ea26df32ea551e09fe23f72ba5651979e05cd229e9f171c23cf; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28302 | complete |
| SF-2026-ARXIV-2605-28354 | RP-930b485331af2ec2 | deep | arXiv:2605.28354v1 | SRC-ARXIV@arXiv:2605.28354v1 | arXiv:2605.28354v1 — § exact heading: 3 Methodology | arXiv:2605.28354v1 — § exact heading: 4 Experiments | arXiv:2605.28354v1 — § exact heading: 5 Conclusion | arXiv:2605.28354v1 — official HTML sha256=adefd62b5877ddd6b889b2d5466bf6d86dea3f49ca521809b6edc772b94d5cd9; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28354 | complete |
| SF-2026-ARXIV-2605-28371 | RP-70c47f15b611d7a5 | deep | arXiv:2605.28371v1 | SRC-ARXIV@arXiv:2605.28371v1 | arXiv:2605.28371v1 — § exact heading: 3 Method | arXiv:2605.28371v1 — § exact heading: 4 Experiments | arXiv:2605.28371v1 — § exact heading: 5 Conclusion | arXiv:2605.28371v1 — official HTML sha256=59b8cf453e48c85d21d2f09b6119c474e58ef81f53f90f1a81cd0252e3e6a66d; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28371 | complete |
| SF-2026-ARXIV-2605-28384 | RP-9206fbc6ee3a4b36 | deep | arXiv:2605.28384v1 | SRC-ARXIV@arXiv:2605.28384v1 | arXiv:2605.28384v1 — § exact heading: 2.4 State Space Models and the Case for an SSM Expert | arXiv:2605.28384v1 — § exact heading: 5.3 Bayesian vs. Prior-Free Ablation: Tiny LM Benchmark | arXiv:2605.28384v1 — § exact heading: 7 Discussion | arXiv:2605.28384v1 — official HTML sha256=1570cc4c065bb54d719c2ab73ec29c27fc79dd28dbc83353e870b38450392418; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28384 | complete |
| SF-2026-ARXIV-2605-28390 | RP-5947de7acb772cd9 | deep | arXiv:2605.28390v1 | SRC-ARXIV@arXiv:2605.28390v1 | arXiv:2605.28390v1 — § exact heading: 2.1 Agentic Systems | arXiv:2605.28390v1 — § exact heading: 3.3 Skill Evaluation and Maintenance | arXiv:2605.28390v1 — § exact heading: 6 Conclusion | arXiv:2605.28390v1 — official HTML sha256=319497612764ee707963a369e412c779142c648f077829de02a9af1827bce409; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28390 | complete |
| SF-2026-ARXIV-2605-28424 | RP-5fbe1c6823665379 | deep | arXiv:2605.28424v1 | SRC-ARXIV@arXiv:2605.28424v1 | arXiv:2605.28424v1 — § exact heading: 3 Method | arXiv:2605.28424v1 — § exact heading: 4 Experiments | arXiv:2605.28424v1 — § exact heading: 5 Conclusion | arXiv:2605.28424v1 — official HTML sha256=56b115a0cea14050550666972c8c3358a23dadd06e5ca9e392e0893d2e08a307; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28424 | complete |
| SF-2026-ARXIV-2605-28433 | RP-2a57f879210baa43 | deep | arXiv:2605.28433v1 | SRC-ARXIV@arXiv:2605.28433v1 | arXiv:2605.28433v1 — § exact heading: 3 Methodology: Sero | arXiv:2605.28433v1 — § exact heading: 4 Experiments | arXiv:2605.28433v1 — § exact heading: 5 Conclusion | arXiv:2605.28433v1 — official HTML sha256=e6b9fa986647a1fdfaf40f75332819e7664fd3c3068b1e2919f51ea7317a4f5f; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28433 | complete |
| SF-2026-ARXIV-2605-28467 | RP-ebe304ac46535ff7 | deep | arXiv:2605.28467v1 | SRC-ARXIV@arXiv:2605.28467v1 | arXiv:2605.28467v1 — § exact heading: 3 Methodology | arXiv:2605.28467v1 — § exact heading: 4.1 Benchmarks | arXiv:2605.28467v1 — § exact heading: 7 Discussion | arXiv:2605.28467v1 — official HTML sha256=8bc115de594103d60edec321cb4440daecf363960c1cb513ddb91f26c2fa43de; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28467 | complete |
| SF-2026-ARXIV-2605-28480 | RP-8fefdfc3612034a2 | deep | arXiv:2605.28480v1 | SRC-ARXIV@arXiv:2605.28480v1 | arXiv:2605.28480v1 — § exact heading: 2.1 Large Audio-Language Models and Audio Understanding Benchmarks | arXiv:2605.28480v1 — § exact heading: 5 Results | arXiv:2605.28480v1 — § exact heading: 6 Conclusion | arXiv:2605.28480v1 — official HTML sha256=d213543a1628789189242389ff40e33dc0b8dc1e48532230aa0d590500274040; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28480 | complete |
| SF-2026-ARXIV-2605-28508 | RP-2ba662f2d64d487e | deep | arXiv:2605.28508v1 | SRC-ARXIV@arXiv:2605.28508v1 | arXiv:2605.28508v1 — pp. 6–8 §3 System under test and layered evaluation | arXiv:2605.28508v1 — pp. 8–11 §4 application profiles and operating-condition tests | arXiv:2605.28508v1 — pp. 11–13 §5 minimum benchmark standard and reporting limits | arXiv:2605.28508v1 — official PDF sha256=8beef4051c11d29813c7f2801e1cf88087f06e659f52cb810f1d20df4999a24d; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28508 | complete |
| SF-2026-ARXIV-2605-28510 | RP-dad443da7ea54e4e | deep | arXiv:2605.28510v1 | SRC-ARXIV@arXiv:2605.28510v1 | arXiv:2605.28510v1 — §III Methodology: SourceTracker, Winnowing and HybridSourceTracker | arXiv:2605.28510v1 — §IV Results: recall, rank and latency | arXiv:2605.28510v1 — §V errors; §VI Discussion; §VIII-A future-work boundaries | arXiv:2605.28510v1 — official exact-v1 HTML read; immutable repository/checkpoint commit Not Disclosed; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28510 | complete |
| SF-2026-ARXIV-2605-28544 | RP-3ff9bf6981828268 | deep | arXiv:2605.28544v1 | SRC-ARXIV@arXiv:2605.28544v1 | arXiv:2605.28544v1 — §3 Method: autoregressive world-action flow, causal guidance and selective KV memory | arXiv:2605.28544v1 — §4 Experiments and ablations | arXiv:2605.28544v1 — §5 Conclusion; Appendix C efficiency analysis; no dedicated limitations section | arXiv:2605.28544v1 — official exact-v1 HTML read; immutable repository/checkpoint commit Not Disclosed; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28544 | complete |
| SF-2026-ARXIV-2605-28561 | RP-3c6ae6f24a42f8ab | deep | arXiv:2605.28561v1 | SRC-ARXIV@arXiv:2605.28561v1 | arXiv:2605.28561v1 — § exact heading: 1 Introduction | arXiv:2605.28561v1 — § exact heading: 5 Experiment Setup | arXiv:2605.28561v1 — § exact heading: 8 Conclusion | arXiv:2605.28561v1 — official HTML sha256=37a019db49266025a9f512e89d9d0055db4d54c74d0e179610cf4b5525ed3956; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28561 | complete |
| SF-2026-ARXIV-2605-28565 | RP-1db8d1876c788d99 | deep | arXiv:2605.28565v1 | SRC-ARXIV@arXiv:2605.28565v1 | arXiv:2605.28565v1 — §2 CiteTrace construction; §3 three-dimensional citation evaluation | arXiv:2605.28565v1 — §4 structural citation failures and judge validation | arXiv:2605.28565v1 — Appendix A.1 scope assumptions and A.2 limitations | arXiv:2605.28565v1 — official exact-v1 HTML read; immutable repository/checkpoint commit Not Disclosed; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28565 | complete |
| SF-2026-ARXIV-2605-28573 | RP-cd18fe97313da239 | deep | arXiv:2605.28573v1 | SRC-ARXIV@arXiv:2605.28573v1 | arXiv:2605.28573v1 — § exact heading: 3 The TSVD Method | arXiv:2605.28573v1 — § exact heading: 4.3 Experimental Derivation of Adaptive Rank Selection Heuristic | arXiv:2605.28573v1 — § exact heading: 6 Discussion and Future Work | arXiv:2605.28573v1 — official HTML sha256=74ef57819f581ccb20cd92e1585f01f2b930e2513a90ce9043b00e552d767079; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28573 | complete |
| SF-2026-ARXIV-2605-28617 | RP-78c9109419ffbf15 | deep | arXiv:2605.28617v1 | SRC-ARXIV@arXiv:2605.28617v1 | arXiv:2605.28617v1 — §3 typed holes and nested calls; §4 static/capability safety | arXiv:2605.28617v1 — §7 verifier, tool-use and multi-turn evaluation | arXiv:2605.28617v1 — §Limitations: well-typed is not correct; authority is only as tight as granted scope | arXiv:2605.28617v1 — official exact-v1 HTML read; immutable repository/checkpoint commit Not Disclosed; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28617 | complete |
| SF-2026-ARXIV-2605-28632 | RP-86f44e9b6fe76237 | deep | arXiv:2605.28632v1 | SRC-ARXIV@arXiv:2605.28632v1 | arXiv:2605.28632v1 — § exact heading: 2.3 PRNG Security in ML Systems | arXiv:2605.28632v1 — § exact heading: 5 Evaluation | arXiv:2605.28632v1 — § exact heading: 3 Threat Model and Problem Formulation | arXiv:2605.28632v1 — official HTML sha256=aafde923a8bedf299b01a1b87790b4fc26d09b9c734ec1891536e0ffbba5474c; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28632 | complete |
| SF-2026-ARXIV-2605-28634 | RP-934e6d4162e05aba | deep | arXiv:2605.28634v1 | SRC-ARXIV@arXiv:2605.28634v1 | arXiv:2605.28634v1 — § exact heading: 2.1 Vision-Language-Action Models | arXiv:2605.28634v1 — § exact heading: 5 Experiments | arXiv:2605.28634v1 — § exact heading: 6 Conclusion | arXiv:2605.28634v1 — official HTML sha256=28d4c6c0aa204e61c3cfe7c1bd438f923cee3007f437aec33e041b2342f66af3; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28634 | complete |
| SF-2026-ARXIV-2605-28640 | RP-4f41053e965ca81c | deep | arXiv:2605.28640v1 | SRC-ARXIV@arXiv:2605.28640v1 | arXiv:2605.28640v1 — §2 exponentially decaying memory and sparse inference instantiations | arXiv:2605.28640v1 — §3 experiments and H1/H2 analyses | arXiv:2605.28640v1 — §Limitations: two 7B checkpoints, 4K context and RULER-only task family | arXiv:2605.28640v1 — official exact-v1 HTML read; immutable repository/checkpoint commit Not Disclosed; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28640 | complete |
| SF-2026-ARXIV-2605-28646 | RP-25a25d22c868e07e | deep | arXiv:2605.28646v1 | SRC-ARXIV@arXiv:2605.28646v1 | arXiv:2605.28646v1 — §4 edge evidence extraction, policy arbitration, SafeScreenshot and skill evolution | arXiv:2605.28646v1 — §5–6 evaluation, sandbox checks and error analysis | arXiv:2605.28646v1 — §Limitations: sanitized scenarios, trusted edge and short-horizon personalization | arXiv:2605.28646v1 — official exact-v1 HTML read; immutable repository/checkpoint commit Not Disclosed; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28646 | complete |
| SF-2026-ARXIV-2605-28678 | RP-0edf953b047cf958 | deep | arXiv:2605.28678v1 | SRC-ARXIV@arXiv:2605.28678v1 | arXiv:2605.28678v1 — § exact heading: 3 Method | arXiv:2605.28678v1 — § exact heading: 4 Experiments | arXiv:2605.28678v1 — § exact heading: 5 Conclusion | arXiv:2605.28678v1 — official HTML sha256=1a1a8f4e1c8ac3653a31c04eee5001b8bd690ec4cacab7bfa00bc96c7270d947; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28678 | complete |
| SF-2026-ARXIV-2605-28691 | RP-1a37691474429bb4 | deep | arXiv:2605.28691v1 | SRC-ARXIV@arXiv:2605.28691v1 | arXiv:2605.28691v1 — § exact heading: 2.1 Sparse Video Generation Model | arXiv:2605.28691v1 — § exact heading: 4 Experiment | arXiv:2605.28691v1 — § exact heading: 5 Conclusion | arXiv:2605.28691v1 — official HTML sha256=327ba473a5ca5523ab42d5daa2cd3b7c42aeeee6b6ecb6ae168b5896299fc13a; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28691 | complete |
| SF-2026-ARXIV-2605-28699 | RP-650b15977d613eba | deep | arXiv:2605.28699v1 | SRC-ARXIV@arXiv:2605.28699v1 | arXiv:2605.28699v1 — § exact heading: 2.2 Multi-Agent System | arXiv:2605.28699v1 — § exact heading: 5 Experiments | arXiv:2605.28699v1 — § exact heading: 6 Conclusion and Limitations | arXiv:2605.28699v1 — official HTML sha256=b46ff12911d0d68e6d23a196c51d66c97243f6cce1cd9ee2d7c2e6a1acc91235; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28699 | complete |
| SF-2026-ARXIV-2605-28704 | RP-095658c28e435cf8 | deep | arXiv:2605.28704v1 | SRC-ARXIV@arXiv:2605.28704v1 | arXiv:2605.28704v1 — § exact heading: I Introduction | arXiv:2605.28704v1 — § exact heading: III Main Results | arXiv:2605.28704v1 — § exact heading: I-A Contribution | arXiv:2605.28704v1 — official HTML sha256=4a7a9a3977cbb61bc5708038d0f880bde52cc4bfcdd5fb033aee756b8612194f; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28704 | complete |
| SF-2026-ARXIV-2605-28721 | RP-7a1b719dd976803a | deep | arXiv:2605.28721v1 | SRC-ARXIV@arXiv:2605.28721v1 | arXiv:2605.28721v1 — § exact heading: 2.4 From Diagnosis to Benchmark Design | arXiv:2605.28721v1 — § exact heading: 2.3 Search Strategy Analysis | arXiv:2605.28721v1 — § exact heading: 6 Discussion and Conclusion | arXiv:2605.28721v1 — official HTML sha256=aeaa68114c24fa582046ca5879e68e549f4c733433734b424d86c75f38e35acf; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28721 | complete |
| SF-2026-ARXIV-2605-28726 | RP-1ffccc712dacecc2 | deep | arXiv:2605.28726v1 | SRC-ARXIV@arXiv:2605.28726v1 | arXiv:2605.28726v1 — § exact heading: II Method | arXiv:2605.28726v1 — § exact heading: IV Experiments | arXiv:2605.28726v1 — § exact heading: IV-C Failure Prediction: Which Monitors Work? | arXiv:2605.28726v1 — official HTML sha256=90cd7e1a54362609991628c3db8b3b43348ca9e11c25067c1e202fb5bc05f38f; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28726 | complete |
| SF-2026-ARXIV-2605-28732 | RP-c804e06e9d82dcab | deep | arXiv:2605.28732v1 | SRC-ARXIV@arXiv:2605.28732v1 | arXiv:2605.28732v1 — § exact heading: 2 Tracing and Attributing Errors in Memory Systems | arXiv:2605.28732v1 — § exact heading: 5 Experiments | arXiv:2605.28732v1 — § exact heading: 8 Conclusion | arXiv:2605.28732v1 — official HTML sha256=c81383e0d1ae7799a14d2a9bd4911c986acf573281a52a6c6c13834fbea2f6a3; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28732 | complete |
| SF-2026-ARXIV-2605-28742 | RP-e1c06ac7fa38e31c | deep | arXiv:2605.28742v1 | SRC-ARXIV@arXiv:2605.28742v1 | arXiv:2605.28742v1 — § exact heading: 1 Introduction | arXiv:2605.28742v1 — § exact heading: 4 Evaluation | arXiv:2605.28742v1 — § exact heading: 6 Discussion | arXiv:2605.28742v1 — official HTML sha256=948395dbaa3e07d1b9fdd398c0c4b798d06dc1a875a55c6c2950cc6ff67acefa; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28742 | complete |
| SF-2026-ARXIV-2605-28751 | RP-d0a01043295bf94d | deep | arXiv:2605.28751v1 | SRC-ARXIV@arXiv:2605.28751v1 | arXiv:2605.28751v1 — § exact heading: 3.4 Extrapolative weight averaging generalizes across inference settings and model scales | arXiv:2605.28751v1 — § exact heading: 4 Analysis and Perspectives | arXiv:2605.28751v1 — § exact heading: 6 Discussion and Limitations | arXiv:2605.28751v1 — official HTML sha256=2ad8c69c8a772c3094e9868186053eb7541cc9e186faa3e4caa9f18359f26f0a; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28751 | complete |
| SF-2026-ARXIV-2605-28760 | RP-214086e596c58ac9 | deep | arXiv:2605.28760v1 | SRC-ARXIV@arXiv:2605.28760v1 | arXiv:2605.28760v1 — § exact heading: 3 System Design | arXiv:2605.28760v1 — § exact heading: 4 Evaluation Setup | arXiv:2605.28760v1 — § exact heading: 7 Discussion | arXiv:2605.28760v1 — official HTML sha256=efb091acec460dba1a6d525cc918d4b70a6c230b181d97523eae8b763dbc309b; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28760 | complete |
| SF-2026-ARXIV-2605-28764 | RP-c836cbe2d01e8938 | deep | arXiv:2605.28764v1 | SRC-ARXIV@arXiv:2605.28764v1 | arXiv:2605.28764v1 — §3 SwarmNode, registry, router and credit ledger; §4 attribution | arXiv:2605.28764v1 — §5 feasibility and deployment path | arXiv:2605.28764v1 — §5.3–5.5 bootstrap, security/privacy and open challenges | arXiv:2605.28764v1 — official exact-v1 HTML read; immutable repository/checkpoint commit Not Disclosed; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28764 | complete |
| SF-2026-ARXIV-2605-28773 | RP-7b84ae320909f89f | deep | arXiv:2605.28773v1 | SRC-ARXIV@arXiv:2605.28773v1 | arXiv:2605.28773v1 — § exact heading: 2 FluxMem Memory Architecture | arXiv:2605.28773v1 — § exact heading: 4 Experiments | arXiv:2605.28773v1 — § exact heading: 6 Conclusion | arXiv:2605.28773v1 — official HTML sha256=d18935b37ea808d2c0daeb4cc59dd49ecae728926ce886f1b3840a91e9819065; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28773 | complete |
| SF-2026-ARXIV-2605-28774 | RP-aa51cf6a59662673 | deep | arXiv:2605.28774v1 | SRC-ARXIV@arXiv:2605.28774v1 | arXiv:2605.28774v1 — § exact heading: A.2 System Prompt and Tool Interface | arXiv:2605.28774v1 — § exact heading: 2 Analysis of RL in Agentic Reasoning | arXiv:2605.28774v1 — § exact heading: 6 Conclusion | arXiv:2605.28774v1 — official HTML sha256=d13ded6dc9cb9f022fcba82d2f405dbb31ca326a1d1cbc8f2311772a26d1d576; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28774 | complete |
| SF-2026-ARXIV-2605-28778 | RP-e4b2161c11fb868d | deep | arXiv:2605.28778v1 | SRC-ARXIV@arXiv:2605.28778v1 | arXiv:2605.28778v1 — § exact heading: 5.3 Impact of System Prompt | arXiv:2605.28778v1 — § exact heading: 4 Experimental Setup | arXiv:2605.28778v1 — § exact heading: 6 Conclusion | arXiv:2605.28778v1 — official HTML sha256=01b64c870e884d24bc10330a3d3515358d4337041ab0b0076cad2275dc758860; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28778 | complete |
| SF-2026-ARXIV-2605-28787 | RP-47e7c882e59f9608 | deep | arXiv:2605.28787v1 | SRC-ARXIV@arXiv:2605.28787v1 | arXiv:2605.28787v1 — § exact heading: 3 System Architecture & Experimental Setup | arXiv:2605.28787v1 — § exact heading: 4 Evaluation Methodology | arXiv:2605.28787v1 — § exact heading: 6 Discussion and Future Work | arXiv:2605.28787v1 — official HTML sha256=4c1f63382d975afe45c1ff2cb12bd17b1fd33893d7aadc0f6e6d17130428b66a; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28787 | complete |
| SF-2026-ARXIV-2605-28803 | RP-cabd2f9c8fd2d577 | deep | arXiv:2605.28803v1 | SRC-ARXIV@arXiv:2605.28803v1 | arXiv:2605.28803v1 — § exact heading: 3.1 Vision Language Action (VLA) Model | arXiv:2605.28803v1 — § exact heading: 5 Experiments and Results | arXiv:2605.28803v1 — § exact heading: 6 Discussion and Analysis | arXiv:2605.28803v1 — official HTML sha256=9cf86ee52580269d695f1b428859a43d79cc4d552873686384aa093796ecedb6; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28803 | complete |
| SF-2026-ARXIV-2605-28805 | RP-730d66eb29e576ce | deep | arXiv:2605.28805v1 | SRC-ARXIV@arXiv:2605.28805v1 | arXiv:2605.28805v1 — § exact heading: 1 Introduction | arXiv:2605.28805v1 — § exact heading: Appendix B Additional Experiments | arXiv:2605.28805v1 — § exact heading: 7 Conclusion | arXiv:2605.28805v1 — official HTML sha256=3c391c76b440fdc62c981dbf8764efd8db77092b07a8c527ed7c2f06c9d088c6; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28805 | complete |
| SF-2026-ARXIV-2605-28807 | RP-e88a335dd8719f0f | deep | arXiv:2605.28807v1 | SRC-ARXIV@arXiv:2605.28807v1 | arXiv:2605.28807v1 — § exact heading: 1 Introduction | arXiv:2605.28807v1 — § exact heading: 5 Experiments | arXiv:2605.28807v1 — § exact heading: 6 Conclusion | arXiv:2605.28807v1 — official HTML sha256=fc1cea1dc0e5de404483eaaf47079402901d8349b2ea8d5133060ab680d51c22; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28807 | complete |
| SF-2026-ARXIV-2605-28819 | RP-dbb44e642cc8196c | deep | arXiv:2605.28819v1 | SRC-ARXIV@arXiv:2605.28819v1 | arXiv:2605.28819v1 — § exact heading: 1 Introduction | arXiv:2605.28819v1 — § exact heading: 2 The PEFT-Arena Benchmark | arXiv:2605.28819v1 — § exact heading: Limitations | arXiv:2605.28819v1 — official HTML sha256=8e6e8e4418944fbd589b91d7ddf5befba422f816d98e2de9b6ebcc57deeed7e3; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28819 | complete |
| SF-2026-ARXIV-2605-28889 | RP-0f8ae95ca9acae3b | deep | arXiv:2605.28889v1 | SRC-ARXIV@arXiv:2605.28889v1 | arXiv:2605.28889v1 — § exact heading: 3 Methodology | arXiv:2605.28889v1 — § exact heading: 4 Experiments | arXiv:2605.28889v1 — § exact heading: 5 Conclusion | arXiv:2605.28889v1 — official HTML sha256=484b7c915791a1d932ca5b0d304ea69886f807144f2b39de985b7a9026b5cc7f; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28889 | complete |
| SF-2026-ARXIV-2605-28890 | RP-c575aa6a373fcd56 | deep | arXiv:2605.28890v1 | SRC-ARXIV@arXiv:2605.28890v1 | arXiv:2605.28890v1 — § exact heading: 4 The Proposed Method | arXiv:2605.28890v1 — § exact heading: 5 Experiments | arXiv:2605.28890v1 — § exact heading: 5.8 Threat Model Boundary and Limitation: Logprob Enabled Verification | arXiv:2605.28890v1 — official HTML sha256=fd2aa444bf003c5dbca9124efc078287ad0ad64b1b099778107fd4dff06c8dbe; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28890 | complete |
| SF-2026-ARXIV-2605-28893 | RP-30dd843dc3e3a933 | deep | arXiv:2605.28893v1 | SRC-ARXIV@arXiv:2605.28893v1 | arXiv:2605.28893v1 — § exact heading: 3. Methodology | arXiv:2605.28893v1 — § exact heading: 3.2. Benchmark Construction | arXiv:2605.28893v1 — § exact heading: 4.5. RQ4: Repair Failure Root Causes | arXiv:2605.28893v1 — official HTML sha256=0ccec6e5023425d608e1da29b300536ad3391a559b6104605c01c756bba173de; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28893 | complete |
| SF-2026-ARXIV-2605-28897 | RP-cdc74bc11a9948eb | deep | arXiv:2605.28897v1 | SRC-ARXIV@arXiv:2605.28897v1 | arXiv:2605.28897v1 — § exact heading: 3 Method | arXiv:2605.28897v1 — § exact heading: 4 Experimental Setup | arXiv:2605.28897v1 — § exact heading: 5 Results and Discussion | arXiv:2605.28897v1 — official HTML sha256=42918fe6e08c174c1b7c008a76802891bf988cc6c027269eecf588031cbe8111; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28897 | complete |
| SF-2026-ARXIV-2605-28914 | RP-afe8cfda3d74c78f | deep | arXiv:2605.28914v1 | SRC-ARXIV@arXiv:2605.28914v1 | arXiv:2605.28914v1 — § exact heading: 2.1 Threat Model | arXiv:2605.28914v1 — § exact heading: 4 Evaluation | arXiv:2605.28914v1 — § exact heading: 6 Conclusion | arXiv:2605.28914v1 — official HTML sha256=d0264220f2ded5ab77e06f15529acb9124ca3dc29ce337b5266947540395fa49; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28914 | complete |
| SF-2026-ARXIV-2605-28918 | RP-edcc2b97fe16e917 | deep | arXiv:2605.28918v1 | SRC-ARXIV@arXiv:2605.28918v1 | arXiv:2605.28918v1 — § exact heading: 3 Method | arXiv:2605.28918v1 — § exact heading: 5 Experimental Setup | arXiv:2605.28918v1 — § exact heading: 7 Failure Taxonomy | arXiv:2605.28918v1 — official HTML sha256=a085ce1d967c0158fa236d3b634861af1ef381b37448f8e1ccb20c4757bf685b; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28918 | complete |
| SF-2026-ARXIV-2605-28920 | RP-ffd9a2cc6051a8b2 | deep | arXiv:2605.28920v1 | SRC-ARXIV@arXiv:2605.28920v1 | arXiv:2605.28920v1 — § exact heading: Section 1 Introduction | arXiv:2605.28920v1 — § exact heading: Section 6 Experiments | arXiv:2605.28920v1 — § exact heading: Section 7 Conclusion and Future Work | arXiv:2605.28920v1 — official HTML sha256=0e5297f8e2a1b9339cab9737e3c87239243a625f9b74bb74f5b340282fcfea97; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28920 | complete |
| SF-2026-ARXIV-2605-28969 | RP-59f99cb5a6c24624 | deep | arXiv:2605.28969v1 | SRC-ARXIV@arXiv:2605.28969v1 | arXiv:2605.28969v1 — § exact heading: 2.2 Memory systems for LLM agents | arXiv:2605.28969v1 — § exact heading: 2. Prior Work, Industry Benchmarks, The Fifth Target | arXiv:2605.28969v1 — § exact heading: 3.3.6 Rubric-handling limitations (post-hoc validity audit) | arXiv:2605.28969v1 — official HTML sha256=101b3e17cd8bba2def194b91f2814eea8c6024099488edfc82a5e614fab3a555; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28969 | complete |
| SF-2026-ARXIV-2605-28991 | RP-51d0d75c151fb0f5 | deep | arXiv:2605.28991v1 | SRC-ARXIV@arXiv:2605.28991v1 | arXiv:2605.28991v1 — § exact heading: II System Architecture and Design | arXiv:2605.28991v1 — § exact heading: IV Security Analysis | arXiv:2605.28991v1 — § exact heading: II-A Threat Model | arXiv:2605.28991v1 — official HTML sha256=38bca95491babf9d404fed1ccf11bc2e90fd9714aaab3e3ec0e9861181a48d41; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28991 | complete |
| SF-2026-ARXIV-2605-28999 | RP-440ee29e369cf8e0 | deep | arXiv:2605.28999v1 | SRC-ARXIV@arXiv:2605.28999v1 | arXiv:2605.28999v1 — § exact heading: 3.1 Threat Model | arXiv:2605.28999v1 — § exact heading: 5.5 Method Selection for Large-Scale Analysis | arXiv:2605.28999v1 — § exact heading: 7 Discussion and Limitations | arXiv:2605.28999v1 — official HTML sha256=4c6e94a2e9d6e480605f51128be9c9358f590c91fc80d8e103ef939bb84b73b6; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28999 | complete |
| SF-2026-ARXIV-2605-29001 | RP-73c880960256ec18 | deep | arXiv:2605.29001v1 | SRC-ARXIV@arXiv:2605.29001v1 | arXiv:2605.29001v1 — § exact heading: 1 Introduction | arXiv:2605.29001v1 — § exact heading: 4 FormInv Benchmark | arXiv:2605.29001v1 — § exact heading: 8 Conclusion | arXiv:2605.29001v1 — official HTML sha256=d0e7ab93baa2dac7887cdb236f80c5996169d4fed3f8e888dd5fe36d3c7ac6c1; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-29001 | complete |
| SF-2026-ARXIV-2605-29005 | RP-587b4f2a38b8e9dd | deep | arXiv:2605.29005v1 | SRC-ARXIV@arXiv:2605.29005v1 | arXiv:2605.29005v1 — § exact heading: 1 Introduction | arXiv:2605.29005v1 — § exact heading: 3.1 Formulation: Iterative Refinement as Operator Evaluation | arXiv:2605.29005v1 — § exact heading: 5 Conclusion | arXiv:2605.29005v1 — official HTML sha256=559be4e8e9ca49a19ad2512c93ccd1b2a3d8402c89267afee289a4eeaff9db6d; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-29005 | complete |
| SF-2026-ARXIV-2605-29054 | RP-ecd467f8f8d35a4c | deep | arXiv:2605.29054v1 | SRC-ARXIV@arXiv:2605.29054v1 | arXiv:2605.29054v1 — § exact heading: 5.3 Self-Validation Systematically Overstates Progress | arXiv:2605.29054v1 — § exact heading: 4 Experiments | arXiv:2605.29054v1 — § exact heading: 5.1 A Cross-Agent Failure Taxonomy | arXiv:2605.29054v1 — official HTML sha256=f83a8a863b6eb67137c3c9aafb5efbf2773bf40a0fdb22358ff2e0fbf8945566; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-29054 | complete |
| SF-2026-ARXIV-2605-29068 | RP-46401cd48588e3bf | deep | arXiv:2605.29068v1 | SRC-ARXIV@arXiv:2605.29068v1 | arXiv:2605.29068v1 — § exact heading: 1 Introduction | arXiv:2605.29068v1 — § exact heading: 4 Experiments | arXiv:2605.29068v1 — § exact heading: 5 Conclusion | arXiv:2605.29068v1 — official HTML sha256=aa57cbc30dac5822270c591d7ab737c1481861b157bec9e3849280b77ddb6943; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-29068 | complete |
| SF-2026-ARXIV-2605-29074 | RP-deda5cce63792e90 | deep | arXiv:2605.29074v1 | SRC-ARXIV@arXiv:2605.29074v1 | arXiv:2605.29074v1 — § exact heading: 1. Introduction | arXiv:2605.29074v1 — § exact heading: 3.3. Benchmark Construction | arXiv:2605.29074v1 — § exact heading: 5. Conclusion | arXiv:2605.29074v1 — official HTML sha256=159ce42649abf09570b373306b1b776ec886382edbc1e4f6ed98b4e64438ba8f; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-29074 | complete |
| SF-2026-ARXIV-2605-29075 | RP-2c01d37bb22aafcd | deep | arXiv:2605.29075v1 | SRC-ARXIV@arXiv:2605.29075v1 | arXiv:2605.29075v1 — § exact heading: 3 Methodology | arXiv:2605.29075v1 — § exact heading: 4 Experiments | arXiv:2605.29075v1 — § exact heading: 5 Conclusion | arXiv:2605.29075v1 — official HTML sha256=cc51fcaee66f9e9767fe6ae83f3d8c792c4420ad4f471a094ffd75a6ec6cf8fa; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-29075 | complete |
| SF-2026-ARXIV-2605-29078 | RP-8560b48479613d8c | deep | arXiv:2605.29078v1 | SRC-ARXIV@arXiv:2605.29078v1 | arXiv:2605.29078v1 — §III execution requirements; §IV snapshot isolation, policy-neutral contract and divergence record | arXiv:2605.29078v1 — §V empirical evaluation across lag regimes | arXiv:2605.29078v1 — §IV-D implementation constraints; §VI future-work boundary | arXiv:2605.29078v1 — official exact-v1 HTML read; immutable repository/checkpoint commit Not Disclosed; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-29078 | complete |
| SF-2026-ARXIV-2605-29082 | RP-601432aa203d1b15 | deep | arXiv:2605.29082v1 | SRC-ARXIV@arXiv:2605.29082v1 | arXiv:2605.29082v1 — § exact heading: 4. System: The Agentic Data Plane | arXiv:2605.29082v1 — § exact heading: 1. Introduction | arXiv:2605.29082v1 — § exact heading: 7. Conclusion | arXiv:2605.29082v1 — official HTML sha256=081c38dee7db84a2bf1efd9e8d9c06a15d35b76a905537a9e2fb49b3745d6d87; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-29082 | complete |
| SF-2026-ARXIV-2605-29087 | RP-351524a35df60e2d | deep | arXiv:2605.29087v1 | SRC-ARXIV@arXiv:2605.29087v1 | arXiv:2605.29087v1 — § exact heading: 3 The Latent-versus-Behavioral Framework | arXiv:2605.29087v1 — § exact heading: 4 Experimental Setup | arXiv:2605.29087v1 — § exact heading: 10 Discussion | arXiv:2605.29087v1 — official HTML sha256=86ee2f058f79289bfbe5520d1df0b0a7e4e647c112d9eb14f7909d3e814255f9; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-29087 | complete |
| SF-2026-ARXIV-2605-29107 | RP-7af7a624262a59ae | deep | arXiv:2605.29107v1 | SRC-ARXIV@arXiv:2605.29107v1 | arXiv:2605.29107v1 — § exact heading: 3 GEO-Bench: Benchmark Design | arXiv:2605.29107v1 — § exact heading: 3.3 Evaluation Metrics | arXiv:2605.29107v1 — § exact heading: 5 Conclusion | arXiv:2605.29107v1 — official HTML sha256=d6201036e694c5ae9088a4681e2fb3c28bba0aec07bcf0292995a841ff377130; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-29107 | complete |
| SF-2026-ARXIV-2605-29114 | RP-077e3d690de9208f | deep | arXiv:2605.29114v1 | SRC-ARXIV@arXiv:2605.29114v1 | arXiv:2605.29114v1 — § exact heading: 3 Threat Model | arXiv:2605.29114v1 — § exact heading: 5 Evaluation Protocol and Success Criteria | arXiv:2605.29114v1 — § exact heading: 8 Discussion and Conclusion | arXiv:2605.29114v1 — official HTML sha256=5847a96dc6b379895ef66c5cde52b6481cec3e2864b1e460feee0735fb6a8ac8; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-29114 | complete |
| SF-2026-ARXIV-2605-29115 | RP-e816a8bb729e1740 | deep | arXiv:2605.29115v1 | SRC-ARXIV@arXiv:2605.29115v1 | arXiv:2605.29115v1 — § exact heading: 1 Introduction | arXiv:2605.29115v1 — § exact heading: 5 Evaluation protocol | arXiv:2605.29115v1 — § exact heading: 7 Conclusion and limitations | arXiv:2605.29115v1 — official HTML sha256=61533d9472b107db9809f1be716cd7739d680592f79ad97fdeba6e052ccc4d81; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-29115 | complete |
| SF-2026-ARXIV-2605-29119 | RP-bb1516cc765b8e9e | deep | arXiv:2605.29119v1 | SRC-ARXIV@arXiv:2605.29119v1 | arXiv:2605.29119v1 — § exact heading: 3.3 Process Reward Model Grading | arXiv:2605.29119v1 — § exact heading: 4 Experiments | arXiv:2605.29119v1 — § exact heading: 6 Conclusion | arXiv:2605.29119v1 — official HTML sha256=cc5c35fe725e92575fa9815caf18800be44be6f9e67621c5918dc55aacf8a0c9; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-29119 | complete |
| SF-2026-ARXIV-2605-29121 | RP-90fb8962f9ee6be2 | deep | arXiv:2605.29121v1 | SRC-ARXIV@arXiv:2605.29121v1 | arXiv:2605.29121v1 — § exact heading: 3.1 Two-Expert Model | arXiv:2605.29121v1 — § exact heading: 8 Numerical Experiments with Batch Routing | arXiv:2605.29121v1 — § exact heading: 9 Limitations | arXiv:2605.29121v1 — official HTML sha256=ab3f9a8273c3d33151de33c82a689df6b669452299c69ed0cc1d123e1a06babe; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-29121 | complete |
| SF-2026-ARXIV-2605-29123 | RP-47f2d5824ade0a51 | deep | arXiv:2605.29123v1 | SRC-ARXIV@arXiv:2605.29123v1 | arXiv:2605.29123v1 — § exact heading: 2.1 Masked Diffusion Models | arXiv:2605.29123v1 — § exact heading: 4 Experiments on Other Reasoning Tasks | arXiv:2605.29123v1 — § exact heading: 3.5 Discussion: What addition teaches us | arXiv:2605.29123v1 — official HTML sha256=e64903394774e58c756155d421de40b4a449290a81bcdd015cfa13c276a88c3f; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-29123 | complete |
| SF-2026-ARXIV-2605-29129 | RP-edbe666bac4058b2 | deep | arXiv:2605.29129v1 | SRC-ARXIV@arXiv:2605.29129v1 | arXiv:2605.29129v1 — §2 debt/tax model; §3 debt accumulation | arXiv:2605.29129v1 — §4 operationalizing governance | arXiv:2605.29129v1 — §5 Conclusion; position paper without empirical validation or dedicated limitations | arXiv:2605.29129v1 — official exact-v1 HTML read; immutable repository/checkpoint commit Not Disclosed; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-29129 | complete |
| SF-2026-ARXIV-2605-29135 | RP-b00db1e27d05dcb5 | deep | arXiv:2605.29135v1 | SRC-ARXIV@arXiv:2605.29135v1 | arXiv:2605.29135v1 — §4 Rotary GPU concept; §6 setup | arXiv:2605.29135v1 — §8 results and failure analysis | arXiv:2605.29135v1 — §11 Limitations: one platform, ten-prompt smoke set and undisclosed implementation | arXiv:2605.29135v1 — official exact-v1 HTML read; immutable repository/checkpoint commit Not Disclosed; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-29135 | complete |
| SF-2026-ARXIV-2605-29139 | RP-585cfe01464428e2 | deep | arXiv:2605.29139v1 | SRC-ARXIV@arXiv:2605.29139v1 | arXiv:2605.29139v1 — § exact heading: 1 Introduction | arXiv:2605.29139v1 — § exact heading: 5 Experiments | arXiv:2605.29139v1 — § exact heading: 6 Discussion and outlook | arXiv:2605.29139v1 — official HTML sha256=a8ec74cd405ca490d4b9ef8c2163fa06058832b58674ce3390d164cb1abab1e3; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-29139 | complete |
| SF-2026-ARXIV-2605-29156 | RP-f712e79bda648d50 | deep | arXiv:2605.29156v1 | SRC-ARXIV@arXiv:2605.29156v1 | arXiv:2605.29156v1 — § exact heading: 4 Method | arXiv:2605.29156v1 — § exact heading: 5 Theoretical Analysis | arXiv:2605.29156v1 — § exact heading: 7 Conclusion | arXiv:2605.29156v1 — official HTML sha256=0276e263a7af8bd4b456d156d09b1c86044e9c77ddc9ab84a6ae06a066509473; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-29156 | complete |
| SF-2026-ARXIV-2605-29178 | RP-424529a88ebf2bf8 | deep | arXiv:2605.29178v1 | SRC-ARXIV@arXiv:2605.29178v1 | arXiv:2605.29178v1 — § exact heading: 3.1 Coordinated sabotage is already practical for frontier models | arXiv:2605.29178v1 — § exact heading: 3 Results | arXiv:2605.29178v1 — § exact heading: 3.3 Recovery, not failure incidence, drives the model gap | arXiv:2605.29178v1 — official HTML sha256=c64659adcde64aa6748ea9f8a3eee8358c0782dcf23a8c50fc40826a7df132e9; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-29178 | complete |
| SF-2026-ARXIV-2605-29183 | RP-8d0c2876e8b729ae | deep | arXiv:2605.29183v1 | SRC-ARXIV@arXiv:2605.29183v1 | arXiv:2605.29183v1 — § exact heading: 2 The TimeGate Model | arXiv:2605.29183v1 — § exact heading: 3 Experiments | arXiv:2605.29183v1 — § exact heading: 6 Conclusion | arXiv:2605.29183v1 — official HTML sha256=a3923b577e9eb61591e3fc195930456c0d3c5d06bdf8deaa0945c9384d3c4a94; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-29183 | complete |
| SF-2026-ARXIV-2605-29192 | RP-93fa80b3f1643d57 | deep | arXiv:2605.29192v1 | SRC-ARXIV@arXiv:2605.29192v1 | arXiv:2605.29192v1 — § exact heading: 3 Methods | arXiv:2605.29192v1 — § exact heading: 5 Analysis of operator distributions | arXiv:2605.29192v1 — § exact heading: 7 Discussion | arXiv:2605.29192v1 — official HTML sha256=e420a9f8f6e5d0391e17194107e7b985ed8142555896991b2d2ec2b1ca2d68c9; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-29192 | complete |
| SF-2026-ARXIV-2605-29209 | RP-4cadca1af599cb68 | deep | arXiv:2605.29209v1 | SRC-ARXIV@arXiv:2605.29209v1 | arXiv:2605.29209v1 — § exact heading: 3 The Methodological Bottleneck: Fixed-Stride Compression | arXiv:2605.29209v1 — § exact heading: 5 Evaluation Framework: The Dual-Probing Protocol | arXiv:2605.29209v1 — § exact heading: 7 Conclusion | arXiv:2605.29209v1 — official HTML sha256=c85bde6618b205f1951294db9ece991e3cd1320c1319aaf4196c9000944fe070; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-29209 | complete |
| SF-2026-ARXIV-2606-07586 | RP-cd26b7111125d18f | deep | arXiv:2606.07586v1 | SRC-ARXIV@arXiv:2606.07586v1 | arXiv:2606.07586v1 — § exact heading: IV Skill System | arXiv:2606.07586v1 — § exact heading: V Evaluation | arXiv:2606.07586v1 — § exact heading: VI Conclusion and Future Work | arXiv:2606.07586v1 — official HTML sha256=5b2c398ccc30fe40586127fe9bea23adf82bdbb41f84275ecd3a1164b3cfc8ce; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2606-07586 | complete |
| SF-2026-ARXIV-2606-26120 | RP-b2be9bb6a06d0338 | deep | arXiv:2606.26120v1 | SRC-ARXIV@arXiv:2606.26120v1 | arXiv:2606.26120v1 — § exact heading: 3 Method | arXiv:2606.26120v1 — § exact heading: 4 Experiment | arXiv:2606.26120v1 — § exact heading: 1 Introduction | arXiv:2606.26120v1 — official HTML sha256=f091d72f6100d2e4bf803a6276472099be05dfd56b099d0462ed38c04969ccd0; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2606-26120 | complete |
| SF-2026-ARXIV-2606-26122 | RP-e4c5c94fac132a0b | deep | arXiv:2606.26122v1 | SRC-ARXIV@arXiv:2606.26122v1 | arXiv:2606.26122v1 — § exact heading: 3 Method | arXiv:2606.26122v1 — § exact heading: 4 Experiment | arXiv:2606.26122v1 — § exact heading: 5 Conclusion | arXiv:2606.26122v1 — official HTML sha256=137890ea8c0dcd2a962b9c3902a8263fbac0adaf1706d1a6e4aaafc61fdeb4b6; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2606-26122 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2605-27820:start -->
#### EgoBench: An Interactive Egocentric Multimodal Benchmark for Tool-Using Agents

问题与 changed constraint：However, existing benchmarks fail to jointly evaluate these capabilities due to challenges in designing strictly coupled multi-capability tasks, simulating natural and task-constrained user feedback, and ensuring objective evaluation of dynamic interaction.

Mechanism 与 ownership：owner=`PLATFORM-EVALUATION-SYSTEM`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.27820v1 — § exact heading: 3.3 Task Design and Ground-truth Annotation`；Evaluation=`arXiv:2605.27820v1 — § exact heading: 2.1 Tool-Using Benchmarks`。

Trade-off / failure / fallback：`arXiv:2605.27820v1 — § exact heading: 5 Conclusions`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.27820v1 — official HTML sha256=e084884e79524dd4bd757618cb34c671331dce1673eadac18e0b6881d86642d3; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-27820:start -->仅支持 exact-v1 披露机制及实验边界；不把“Furthermore, we establish a deterministic joint validation framework that guarantees objective assessment through process-based and result-based equivalence.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-27820:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-27820:end -->

<!-- review:SF-2026-ARXIV-2605-27825:start -->
#### MRMMIA: Membership Inference Attacks on Memory in Chat Agents

问题与 changed constraint：We propose Multi-Recall Memory MIA (MRMMIA), a unified attack that utilizes multiple recall probes to the agent to extract the membership signal across black-box, gray-box, and white-box settings.

Mechanism 与 ownership：owner=`PLATFORM-SECURITY`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.27825v1 — § exact heading: 3 Threat Model and Problem Formulation`；Evaluation=`arXiv:2605.27825v1 — § exact heading: 5 Experiments`。

Trade-off / failure / fallback：`arXiv:2605.27825v1 — § exact heading: 7 Conclusion and Limitations`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.27825v1 — official HTML sha256=778098e7df5cf172ed04989da043124faf4d825232bb02bbc1ceeeb0aa110f9a; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-27825:start -->仅支持 exact-v1 披露机制及实验边界；不把“Our experiments demonstrate that MRMMIA consistently outperforms baselines.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-27825:end -->

Books Decision=`Integrate`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-27825:end -->

<!-- review:SF-2026-ARXIV-2605-27850:start -->
#### TCP-MCP: Landscape-Guided Co-Evolution of Prompts and Communication Topologies for Multi-Agent Systems

问题与 changed constraint：We propose \textbf{TCP-MCP} (Topology-Coupled Prompting for Multi-Agent Collaborative Problem-Solving), a co-evolution framework that searches agent prompts and communication topologies as a unified genome.

Mechanism 与 ownership：owner=`AGENT-MULTI-AGENT`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.27850v1 — §3 Methods: unified prompt-topology genome and adaptive Pareto control`；Evaluation=`arXiv:2605.27850v1 — §4 Experiments: held-out accuracy, token cost and topology complexity`。

Trade-off / failure / fallback：`arXiv:2605.27850v1 — §5 Conclusion, Limitations, and Future Work`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.27850v1 — official exact-v1 HTML read; immutable repository/checkpoint commit Not Disclosed; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-27850:start -->仅支持 exact-v1 披露机制及实验边界；不把“These results show that jointly evolving prompts and communication structure provides a practical route to cost-aware and task-adaptive multi-agent system design in controlled evaluations.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-27850:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-27850:end -->

<!-- review:SF-2026-ARXIV-2605-27879:start -->
#### Towards Faithful Agentic XAI: A Verification Method and an Open-World Benchmark for Better Model Faithfulness

问题与 changed constraint：We propose Faithful Agentic XAI (FAX), a framework that improves explanation faithfulness through explicit verification.

Mechanism 与 ownership：owner=`PLATFORM-EVALUATION-SYSTEM`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.27879v1 — § exact heading: 3 Method: Faithful Agentic XAI`；Evaluation=`arXiv:2605.27879v1 — § exact heading: 4.2 Evaluation scenarios`。

Trade-off / failure / fallback：`arXiv:2605.27879v1 — § exact heading: 6 Conclusions`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.27879v1 — official HTML sha256=6414fd88678b2d30e7ef60804106d0d709040c51a69d5a37d2f507bfcb6a22c3; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-27879:start -->仅支持 exact-v1 披露机制及实验边界；不把“These findings show that explicit verification is essential for faithful Agentic XAI and that that faithfulness benchmarks must be designed to test explanations against the behavior of the target model itself.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-27879:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-27879:end -->

<!-- review:SF-2026-ARXIV-2605-27881:start -->
#### Retrieval, Reward, and Training Protocols: What Matters in Training Search Agents?

问题与 changed constraint：We present a controlled empirical study that isolates three under-explored dimensions of search agent training.

Mechanism 与 ownership：owner=`TRAIN-DATA`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.27881v1 — § exact heading: 2.1 Reward Design for Search Agent`；Evaluation=`arXiv:2605.27881v1 — § exact heading: 3 Experiments Setup`。

Trade-off / failure / fallback：`arXiv:2605.27881v1 — § exact heading: Limitations`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.27881v1 — official HTML sha256=07bf6c9ae6e5fe2bbe5681bcaa7fbc987ad4ff370478f650c574244e5f99a760; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-27881:start -->仅支持 exact-v1 披露机制及实验边界；不把“First, we identify a critical data-coverage issue in the widely used Wikipedia 2018 corpus and show that correcting it alone yields larger gains than the differences between training algorithms.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-27881:end -->

Books Decision=`Integrate`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-27881:end -->

<!-- review:SF-2026-ARXIV-2605-27898:start -->
#### A Unified Framework for the Evaluation of LLM Agentic Capabilities

问题与 changed constraint：In this work, we present a unified framework for the fair evaluation of LLM agentic capabilities.

Mechanism 与 ownership：owner=`PLATFORM-EVALUATION-SYSTEM`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.27898v1 — § exact heading: 2 Unified Framework`；Evaluation=`arXiv:2605.27898v1 — § exact heading: 2.5 Evaluation Methodology`。

Trade-off / failure / fallback：`arXiv:2605.27898v1 — § exact heading: 3.5 Failure Result Analysis`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.27898v1 — official HTML sha256=7ee4e3fea5ae787e7b7369f9df610a0f7893a5f73d7d984cc659f19fc82c6ecd; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-27898:start -->仅支持 exact-v1 披露机制及实验边界；不把“We further demonstrate its extensibility as a secure testbed for safety-critical domains.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-27898:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-27898:end -->

<!-- review:SF-2026-ARXIV-2605-27899:start -->
#### SKILLC: Learning Autonomous Skill Internalization in LLM Agents via Contrastive Credit Assignment

问题与 changed constraint：We propose SkillC, a framework based on Contrastive Skill Credit Assignment (CSCA) that converts this contrast into a direct learning signal for internalization.

Mechanism 与 ownership：owner=`TRAIN-GRPO`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.27899v1 — § exact heading: 3 Method`；Evaluation=`arXiv:2605.27899v1 — § exact heading: 4 Experiments`。

Trade-off / failure / fallback：`arXiv:2605.27899v1 — § exact heading: 5 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.27899v1 — official HTML sha256=54f2f7366208bc5806dd940984e523d58fd223db4b28a057e2ef039098f1f0ad; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-27899:start -->仅支持 exact-v1 披露机制及实验边界；不把“Experiments on ALFWorld and WebShop show that, without runtime skill access, SkillC surpasses the strongest prior skill-internalization RL baseline by 5.5\% and 4.4\%, respectively, while remaining competitive with skill-augmented RL methods.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-27899:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-27899:end -->

<!-- review:SF-2026-ARXIV-2605-27901:start -->
#### The Fragility of Chain-of-Thought Monitoring Across Typologically Diverse Languages

问题与 changed constraint：We present the first large-scale evaluation of CoT monitorability across 13 diverse languages and seven frontier model families, comprising 16 models.

Mechanism 与 ownership：owner=`PLATFORM-SECURITY`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.27901v1 — § exact heading: 4 Can models conceal their reasoning across different languages?`；Evaluation=`arXiv:2605.27901v1 — § exact heading: 3 Experimental Setup`。

Trade-off / failure / fallback：`arXiv:2605.27901v1 — § exact heading: 8 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.27901v1 — official HTML sha256=a6ba0236d1abd1ae5608efa74db512b77c0445c54532de292db24bf296c6295c; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-27901:start -->仅支持 exact-v1 披露机制及实验边界；不把“Our results reveal that CoT monitoring is fundamentally fragile under linguistic distribution shift, providing a substantially weaker safety signal than what English-only studies suggest.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-27901:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-27901:end -->

<!-- review:SF-2026-ARXIV-2605-27918:start -->
#### Addressing Variable Heterogeneity in Distributed Multimodal Training with Entrain

问题与 changed constraint：We present Entrain, a distributed MLLM training framework that addresses both heterogeneity and variability in multimodal training workloads.

Mechanism 与 ownership：owner=`TRAIN-DISTRIBUTED-TRAINING`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.27918v1 — § exact heading: 2.1. MLLM Architecture and Parallelism`；Evaluation=`arXiv:2605.27918v1 — § exact heading: 4. Macroscopic Analysis-Based Model Parallelization`。

Trade-off / failure / fallback：`arXiv:2605.27918v1 — § exact heading: 2.3. Limitations of Existing Works`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.27918v1 — official HTML sha256=22c10a9201b86eead7234ee23182de2058869658bcc76c034c3d95bd886271f3; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-27918:start -->仅支持 exact-v1 披露机制及实验边界；不把“Evaluations show that Entrain reduces workload variability across microbatches by up to 10.6$\times$, improving end-to-end training throughput by up to 1.40$\times$ over existing baselines.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-27918:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-27918:end -->

<!-- review:SF-2026-ARXIV-2605-27922:start -->
#### Harness-Bench: Measuring Harness Effects across Models in Realistic Agent Workflows

问题与 changed constraint：However, existing benchmarks typically abstract away execution, compare complete agent systems, or hold the harness fixed, making execution-layer variation difficult to study.

Mechanism 与 ownership：owner=`PLATFORM-EVALUATION-SYSTEM`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.27922v1 — § exact heading: 3.2 Task Suite Design and Validation`；Evaluation=`arXiv:2605.27922v1 — § exact heading: 3 The Harness-Bench Benchmark`。

Trade-off / failure / fallback：`arXiv:2605.27922v1 — § exact heading: 5.1 Observed Failure Symptoms`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.27922v1 — official HTML sha256=3e89c9f28b68276bc33fde7581b7a8428c53bb33ffa950e94aa7ed757cab807c; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-27922:start -->仅支持 exact-v1 披露机制及实验边界；不把“Harness-Bench provides a reproducible foundation for diagnosing and improving reliable, efficient, and auditable agent execution stacks.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-27922:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-27922:end -->

<!-- review:SF-2026-ARXIV-2605-27947:start -->
#### SANTS: A State-Adaptive Scheduler for World Action Models

问题与 changed constraint：Controlled denoising-depth scans show that video refinement can reduce action error up to a state-dependent point, after which the gain may saturate or even reverse when late predictions become less action-relevant or physically unreliable.

Mechanism 与 ownership：owner=`INFER-SCHEDULING`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.27947v1 — § exact heading: 3 Method`；Evaluation=`arXiv:2605.27947v1 — § exact heading: 4 Experiments`。

Trade-off / failure / fallback：`arXiv:2605.27947v1 — § exact heading: 5 Limitations`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.27947v1 — official HTML sha256=6775e77796d135354ae93c0db230ddba4574e84d3cf09c0aa4602b17ce622867; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-27947:start -->仅支持 exact-v1 披露机制及实验边界；不把“Experiments show that SANTS reaches \(94.4\%\) overall success on RoboTwin 2.0 and \(73.1\%\) average success across seven real-robot tasks, while reducing latency by \(81.7\%\) and \(79.0\%\) relative to full video denoising, respectively.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-27947:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-27947:end -->

<!-- review:SF-2026-ARXIV-2605-27954:start -->
#### Cyclical Entropy Eruption: Entropy Dynamics in Agent Reinforcement Learning

问题与 changed constraint：However, the training dynamics of agent RL remain poorly understood, limiting our ability to diagnose instabilities and design more effective training algorithms.

Mechanism 与 ownership：owner=`TRAIN-GRPO`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.27954v1 — § exact heading: 1 Introduction`；Evaluation=`arXiv:2605.27954v1 — § exact heading: 4.2 Experimental Settings`。

Trade-off / failure / fallback：`arXiv:2605.27954v1 — § exact heading: 6 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.27954v1 — official HTML sha256=2b0011952bb538ff67435afde77b7104a2654683eeb7f17f4e3b82e26a89afa1; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-27954:start -->仅支持 exact-v1 披露机制及实验边界；不把“Experiments across multiple benchmarks, models, and RL algorithms demonstrate that SEAL stabilizes training and yields stronger downstream agent performance.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-27954:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-27954:end -->

<!-- review:SF-2026-ARXIV-2605-27957:start -->
#### DisasterBench: Benchmarking LLM Planning under Typed Tool Interface Constraints

问题与 changed constraint：We introduce DisasterBench, a benchmark for evaluating structured multi-agent planning over semantically similar but operationally distinct disaster-response tools.

Mechanism 与 ownership：owner=`PLATFORM-EVALUATION-SYSTEM`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.27957v1 — § exact heading: 4.6 Reasoning-Optimized Models and Instruction Clash`；Evaluation=`arXiv:2605.27957v1 — § exact heading: 2.1 Tool-Augmented and Multi-Step Planning Benchmarks`。

Trade-off / failure / fallback：`arXiv:2605.27957v1 — § exact heading: 4.5 Failure Mode Analysis`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.27957v1 — official HTML sha256=248798608249a4b17d5fa271b948eefaf1bb5408fa419864abf81f260bc8c5e6; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-27957:start -->仅支持 exact-v1 披露机制及实验边界；不把“Code, data, and evaluation resources are available at: https://github.com/TamuChen18/DisasterBench_Open”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-27957:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-27957:end -->

<!-- review:SF-2026-ARXIV-2605-27963:start -->
#### Throughput-Optimized Networks at Scale

问题与 changed constraint：Datacenter network design plays a critical role in AI training by supporting scaling to thousands of accelerators.

Mechanism 与 ownership：owner=`TRAIN-DISTRIBUTED-TRAINING`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.27963v1 — § exact heading: 2.1. Analytical Models on Performance`；Evaluation=`arXiv:2605.27963v1 — § exact heading: 4.4. Resultant Topologies`。

Trade-off / failure / fallback：`arXiv:2605.27963v1 — § exact heading: 8. Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.27963v1 — official HTML sha256=8ab4cf20fc446530aa8902eaa42a687c616adf1e944c3c43337c1bd8440106c7; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-27963:start -->仅支持 exact-v1 披露机制及实验边界；不把“We show that the existing TPU networks leave terabytes per second of throughput on the table and we fill that gap.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-27963:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-27963:end -->

<!-- review:SF-2026-ARXIV-2605-27980:start -->
#### Periodic RoPE for Infinite Context LLMs

问题与 changed constraint：To address it, we propose Periodic RoPE (P-RoPE), a positional encoding mechanism designed to circumvent this exhaustion.

Mechanism 与 ownership：owner=`MODEL-POSITION-ENCODING`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.27980v1 — § exact heading: 3 Method`；Evaluation=`arXiv:2605.27980v1 — § exact heading: 4 Experimental Setup`。

Trade-off / failure / fallback：`arXiv:2605.27980v1 — § exact heading: 6 Limitations`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.27980v1 — official HTML sha256=20b0adb216b2e7b519721df4af90508fc41737dc57300f9be6baf9753f22ae78; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-27980:start -->仅支持 exact-v1 披露机制及实验边界；不把“Empirical results show that our model, MiniWin, outperforms MiniMInd with standard GPT architectures in long-context efficiency and stability.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-27980:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-27980:end -->

<!-- review:SF-2026-ARXIV-2605-27995:start -->
#### AsyncTool: Evaluating the Asynchronous Function Calling Capability under Multi-Task Scenarios

问题与 changed constraint：To evaluate it, we propose AsyncTool, a benchmark for assessing LLM-based agents in interactive multi-task tool-use environments with delayed tool feedback.

Mechanism 与 ownership：owner=`PLATFORM-EVALUATION-SYSTEM`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.27995v1 — § exact heading: 2.1 Agent as a Concurrent Tool-Using System`；Evaluation=`arXiv:2605.27995v1 — § exact heading: 2.3 Evaluation`。

Trade-off / failure / fallback：`arXiv:2605.27995v1 — § exact heading: 4 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.27995v1 — official HTML sha256=707fad563547b29d77b0b377d0f1f896c52513d59f87543ff726262ca1f3754c; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-27995:start -->仅支持 exact-v1 披露机制及实验边界；不把“Extensive experiments show that delayed tool feedback poses substantial challenges to current agents and leads to clear performance degradation.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-27995:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-27995:end -->

<!-- review:SF-2026-ARXIV-2605-28000:start -->
#### Tool Forge: A Validation-Carrying Toolchain for Governed Agentic Execution

问题与 changed constraint：Large language model agents are increasingly expected to perform operational work: calling APIs, manipulating files, assembling workflows, and acting inside enterprise systems.

Mechanism 与 ownership：owner=`AGENT-TOOL-CALLING`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28000v1 — § exact heading: 3 Tool Forge Conceptual Framework`；Evaluation=`arXiv:2605.28000v1 — § exact heading: 9 Experimental Protocol and Baselines`。

Trade-off / failure / fallback：`arXiv:2605.28000v1 — § exact heading: 12 Limitations and Open Questions`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28000v1 — official HTML sha256=5ea862c3ec5aea65324f90f20db2c7c7596ccee5e7250bd3c1675ae44ca0644b; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28000:start -->仅支持 exact-v1 披露机制及实验边界；不把“The paper identifies remaining challenges in adversarial routing, broader API grounding, sandbox isolation, and cross-system evaluation.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28000:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28000:end -->

<!-- review:SF-2026-ARXIV-2605-28009:start -->
#### MemGuard: Preventing Memory Contamination in Long-Term Memory-Augmented Large Language Models

问题与 changed constraint：To this end, we introduce MemGuard, a type-aware memory framework that preserves functional memory boundaries during memory construction and retrieval.

Mechanism 与 ownership：owner=`AGENT-MEMORY`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28009v1 — § exact heading: Appendix E Use of Large Language Models`；Evaluation=`arXiv:2605.28009v1 — § exact heading: 5 Experiment`。

Trade-off / failure / fallback：`arXiv:2605.28009v1 — § exact heading: 7 Conclusions and Future Work`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28009v1 — official HTML sha256=d6dda2a87c59fd4d07ba02d92c5f0c24c14d09a1096ddb8d79481b5dacfdd055; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28009:start -->仅支持 exact-v1 披露机制及实验边界；不把“These results suggest that reliable long-term reasoning depends on principled organization and selective use of heterogeneous memory.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28009:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28009:end -->

<!-- review:SF-2026-ARXIV-2605-28017:start -->
#### Can It Reach the Generator? Investigating the Survival of Prompt-Injection Attacks in Realistic RAG Settings

问题与 changed constraint：In this paper, we re-evaluate seven GEO attacks under a realistic three-stage pipeline (retriever\,$\to$\,LLM reranker\,$\to$\,LLM generator).

Mechanism 与 ownership：owner=`PLATFORM-SECURITY`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28017v1 — § exact heading: 4.4 Attack Methods`；Evaluation=`arXiv:2605.28017v1 — § exact heading: 3.2 Attack Evaluation in Prior Work`。

Trade-off / failure / fallback：`arXiv:2605.28017v1 — § exact heading: 6 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28017v1 — official HTML sha256=341b7d7e7c46ce09f8c492be68070b3f9c85e07da5caa6d219cea5e2dcf678b6; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28017:start -->仅支持 exact-v1 披露机制及实验边界；不把“We find that prior protocols substantially overstate attack effectiveness: gradient-based and instruction override attacks largely collapse before reaching the generator, and only LLM-driven prompt injections remain effective end-to-end.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28017:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28017:end -->

<!-- review:SF-2026-ARXIV-2605-28044:start -->
#### Relevant Is Not Warranted: Evidence-Force Calibration for Cited RAG

问题与 changed constraint：We study this diagnostic failure as citation laundering: a related source is presented as warrant for an over-strong claim.

Mechanism 与 ownership：owner=`PLATFORM-EVALUATION-SYSTEM`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28044v1 — § exact heading: Appendix G Model API and Decoding Configuration`；Evaluation=`arXiv:2605.28044v1 — § exact heading: 5 Experiments`。

Trade-off / failure / fallback：`arXiv:2605.28044v1 — § exact heading: 6 Discussion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28044v1 — official HTML sha256=5b0d0423fc0dc00a6104deb2486a929aeab242779dfb2a336538c9d90949c46d; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28044:start -->仅支持 exact-v1 披露机制及实验边界；不把“We release the benchmark, prompts, outputs, and plug-in pipeline so citation evaluators can report monotonicity violation rate and force sensitivity alongside conventional support metrics.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28044:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28044:end -->

<!-- review:SF-2026-ARXIV-2605-28046:start -->
#### MemCog: From Memory-as-Tool to Memory-as-Cognition in Conversational Agents

问题与 changed constraint：We propose MemCog, a Memory-as-Cognition system that makes memory access an integral part of the reasoning process.

Mechanism 与 ownership：owner=`AGENT-MEMORY`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28046v1 — § exact heading: 2.4 Proactive Systems`；Evaluation=`arXiv:2605.28046v1 — § exact heading: 4 Experiments`。

Trade-off / failure / fallback：`arXiv:2605.28046v1 — § exact heading: 5 Discussion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28046v1 — official HTML sha256=9de207b19cc99467ce05fbe4668f2af43818fe87622c2f2b9f2a2336444ace08; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28046:start -->仅支持 exact-v1 披露机制及实验边界；不把“Experiments show that MemCog achieves state-of-the-art on passive QA benchmarks (92.98 on LoCoMo, 95.8 on LongMemEval) while substantially outperforming baselines on ProactiveMemBench, demonstrating the advantage of Memory-as-Cognition.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28046:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28046:end -->

<!-- review:SF-2026-ARXIV-2605-28053:start -->
#### RW-TTT: Batched Serving for Request-Owned Test-Time Training State

问题与 changed constraint：We formulate this problem as read-write TTT serving and present RW-TTT , which tags each decode step with its owner, version, and READ/WRITE effect, batches only compatible phases, and commits updates only to the owner.

Mechanism 与 ownership：owner=`INFER-CONTINUOUS-BATCHING`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28053v1 — § exact heading: 2.1 Serving with Mutable Model State`；Evaluation=`arXiv:2605.28053v1 — § exact heading: 5 Evaluation`。

Trade-off / failure / fallback：`arXiv:2605.28053v1 — § exact heading: 6 Discussion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28053v1 — official HTML sha256=d97dad61bd6b3336151a29c7da781ff5a05a6ddc2691377489479fbed0a234c5; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28053:start -->仅支持 exact-v1 披露机制及实验边界；不把“It preserves behavior on RULER, a long-context benchmark, and passes owner/version checks.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28053:end -->

Books Decision=`Integrate`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28053:end -->

<!-- review:SF-2026-ARXIV-2605-28071:start -->
#### AgentGuard: An Attribute-Based Access Control Framework for Tool-Use LLM-Based Agent

问题与 changed constraint：In this paper, we present AgentGuard, an attribute-based access control framework for tool-use LLM-based agents.

Mechanism 与 ownership：owner=`AGENT-TOOL-CALLING`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28071v1 — § exact heading: 1. Introduction`；Evaluation=`arXiv:2605.28071v1 — § exact heading: 2. AgentGuard`。

Trade-off / failure / fallback：`arXiv:2605.28071v1 — § exact heading: 3. Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28071v1 — official HTML sha256=ae831e1a6bf504005cadb4b6e87783430807af808aa4d411b1586ff15d1a4a10; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28071:start -->仅支持 exact-v1 披露机制及实验边界；不把“Currently, AgentGuard is publicly accessible at https://github.com/WhitzardAgent/AgentGuard.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28071:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28071:end -->

<!-- review:SF-2026-ARXIV-2605-28074:start -->
#### SilentRetrieval: Hijacking Retrieval-Augmented Generation via Semantically-Preserving Adversarial Data Poisoning

问题与 changed constraint：We present SilentRetrieval, a two-stage data poisoning attack that hijacks RAG systems through adversarially crafted yet fluent documents.

Mechanism 与 ownership：owner=`PLATFORM-SECURITY`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28074v1 — § exact heading: 3.2. Threat Model`；Evaluation=`arXiv:2605.28074v1 — § exact heading: 5. Experiments`。

Trade-off / failure / fallback：`arXiv:2605.28074v1 — § exact heading: 8. Limitations`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28074v1 — official HTML sha256=0fe32804f286c87a8344023ffd30d5f490a312ecc2910c900d6ce0e8d95981ae; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28074:start -->仅支持 exact-v1 披露机制及实验边界；不把“Human evaluation shows substantially lower flag rates than disfluent baselines, while remaining numerically more suspicious than benign content at the current sample size.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28074:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28074:end -->

<!-- review:SF-2026-ARXIV-2605-28083:start -->
#### VLA-Hijack: A Transferable Patch Attack against Vision-Language-Action Models via Visual Proprioception Hijacking

问题与 changed constraint：To overcome this limitation, we propose VLA-Hijack, a unified adversarial framework that breaks the transferability bottleneck by exploiting a fundamental vulnerability identified in this work: before planning any motion, a VLA model must first use visual information to locate its own robotic arm within the environment.

Mechanism 与 ownership：owner=`PLATFORM-SECURITY`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28083v1 — § exact heading: 2.1 Vision-Language-Action Models`；Evaluation=`arXiv:2605.28083v1 — § exact heading: 4 Experiments`。

Trade-off / failure / fallback：`arXiv:2605.28083v1 — § exact heading: 3.1 Preliminaries & Threat Model`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28083v1 — official HTML sha256=75a70820341d7c1995d5dcce0f6e2ef4087be2e4ee456e5403fa26986a59e552; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28083:start -->仅支持 exact-v1 披露机制及实验边界；不把“Extensive experiments across diverse architectures (OpenVLA, UniVLA, and CronusVLA) demonstrate that VLA-Hijack achieves superior optimization efficiency in white-box settings and sets a new SOTA for cross-architecture and cross-domain black-box transferability.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28083:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28083:end -->

<!-- review:SF-2026-ARXIV-2605-28095:start -->
#### SiDP: Memory-Efficient Data Parallelism for Offline LLM Inference

问题与 changed constraint：We present SiDP, a memory-efficient data-parallel paradigm for offline LLM inference that treats weights as a bandwidth-backed shared resource inside a DP group.

Mechanism 与 ownership：owner=`INFER-GPU-MEMORY`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28095v1 — § exact heading: 2.1 Large Language Models`；Evaluation=`arXiv:2605.28095v1 — § exact heading: 5 Evaluation`。

Trade-off / failure / fallback：`arXiv:2605.28095v1 — § exact heading: 4.4 Discussion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28095v1 — official HTML sha256=5a35d6208f87777291ee083ee28d0ca39f8edf85bbf757764809c8cc70d60976; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28095:start -->仅支持 exact-v1 披露机制及实验边界；不把“Evaluated on NVIDIA H20, H200, and B200 GPUs with Qwen3-32B, Qwen2.5-72B, and Llama-3.1-70B, SiDP increases usable KV capacity by up to 1.8x under the same configurations, and converts this into up to 1.5x higher end-to-end throughput over baselines (vLLM) for offline workloads.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28095:end -->

Books Decision=`Integrate`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28095:end -->

<!-- review:SF-2026-ARXIV-2605-28097:start -->
#### ICAN-Deploy: Identity-Stable Canary Deployment for Safety-Critical Embodied Agents

问题与 changed constraint：We present ICAN-Deploy (Identity-stable CANary Deployment), a middleware construction whose state machine holds the identity hash invariant across the canary window by separating capability names (frozen, hashed) from capability versions (mutable runtime state).

Mechanism 与 ownership：owner=`PLATFORM-PRODUCTION`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28097v1 — § exact heading: 3. Design`；Evaluation=`arXiv:2605.28097v1 — § exact heading: 5. Evaluation`。

Trade-off / failure / fallback：`arXiv:2605.28097v1 — § exact heading: 5.5. Failure-Mode Taxonomy`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28097v1 — official HTML sha256=414916db7f1e595f656d28986787a19c47a828a3a85d39a16a19704252d2638a; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28097:start -->仅支持 exact-v1 披露机制及实验边界；不把“A system certified once at identity-creation time can then ship arbitrary capability evolution under that same certification, within the version-and-name envelope.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28097:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28097:end -->

<!-- review:SF-2026-ARXIV-2605-28108:start -->
#### Ask Now, Use Later: Benchmarking the Proactivity Gap in Long-Lived LLM Agents

问题与 changed constraint：ATR is hard even to evaluate: the right question is underdetermined and its payoff deferred to tasks that may never arise.

Mechanism 与 ownership：owner=`AGENT-PLANNING`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28108v1 — § exact heading: Appendix B Runtime Framework`；Evaluation=`arXiv:2605.28108v1 — § exact heading: 2.2 Why ATR Resists Direct Evaluation`。

Trade-off / failure / fallback：`arXiv:2605.28108v1 — § exact heading: 6 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28108v1 — official HTML sha256=955cb683e1219ce043363a3f80c8c78f68fcf31db7a68d671b8cbcbc921b93bd; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28108:start -->仅支持 exact-v1 披露机制及实验边界；不把“ATR is hard even to evaluate: the right question is underdetermined and its payoff deferred to tasks that may never arise.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28108:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28108:end -->

<!-- review:SF-2026-ARXIV-2605-28112:start -->
#### A Wolf in Sheep's Clothing: Targeted Routing Hijacking in Federated RAG

问题与 changed constraint：We introduce Routing Hijacking, a routing-stage attack in which a malicious client forges its profile to attract target queries despite having irrelevant underlying data.

Mechanism 与 ownership：owner=`PLATFORM-SECURITY`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28112v1 — § exact heading: 2.2 Threat Model and Attack Realism`；Evaluation=`arXiv:2605.28112v1 — § exact heading: 4 Experiments`。

Trade-off / failure / fallback：`arXiv:2605.28112v1 — § exact heading: 6 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28112v1 — official HTML sha256=d0cbc74c408247a70679909334b0628c17fb424771394eb5869d80f3ad9c15f7; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28112:start -->仅支持 exact-v1 披露机制及实验边界；不把“To address this gap, we propose a trust-aware post-routing framework that reweights clients using returned-evidence feedback, including retrieval relevance, profile consistency, and cross-client agreement; online experiments show that it suppresses persistent hijacking over recurring queries and transfers to a learned neural router.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28112:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28112:end -->

<!-- review:SF-2026-ARXIV-2605-28116:start -->
#### MIRAGE: Context-Aware Prompt Injection against Mobile GUI Agents via User-Generated Content

问题与 changed constraint：We present MIRAGE (Mobile Injection of Realistic Adversarial GUI Examples), a pipeline that turns benign mobile screenshots into prompt-injection samples by placing attacker-controlled text into ordinary user-generated content regions, without modifying the agent, the application, or the operating system.

Mechanism 与 ownership：owner=`PLATFORM-SECURITY`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28116v1 — § exact heading: 3 Methodology`；Evaluation=`arXiv:2605.28116v1 — § exact heading: 4 Experiments`。

Trade-off / failure / fallback：`arXiv:2605.28116v1 — § exact heading: 3.1 Threat Model and Problem Setup`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28116v1 — official HTML sha256=1468243f7898c335be4b2032a41fce144cd2cde51fbfa05bdec6192f398d54b1; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28116:start -->仅支持 exact-v1 披露机制及实验边界；不把“We further find that per-sample realism and attack success are uncorrelated, so visual-quality filtering alone cannot reliably defend against this threat.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28116:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28116:end -->

<!-- review:SF-2026-ARXIV-2605-28122:start -->
#### SNARE: Adaptive Scenario Synthesis for Eliciting Overeager Behavior in Coding Agents

问题与 changed constraint：We present SNARE (Synthesizing Non-adversarial scenarios for Adaptive Reward-guided Elicitation), a pipeline that composes benign scenarios from reusable scope and trap fragments, scores each run with a judge-free oracle flagging trap-pattern matches and unsolicited file additions or deletions, and uses Thompson sampling to steer each pair's run budget toward the scenarios that most often trigger it.

Mechanism 与 ownership：owner=`PLATFORM-EVALUATION-SYSTEM`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28122v1 — § exact heading: 4 Methodology`；Evaluation=`arXiv:2605.28122v1 — § exact heading: 5 Evaluation`。

Trade-off / failure / fallback：`arXiv:2605.28122v1 — § exact heading: 6 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28122v1 — official HTML sha256=2b2263367a509d311807ea14ffd2bbe1d4340d5061f31a11a4c27daea64d124d; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28122:start -->仅支持 exact-v1 披露机制及实验边界；不把“This variation is driven by the agent framework, not the model: the framework accounts for 56% of it against the model's 21%, so any single-framework or single-model evaluation undercounts the matrix by about a fifth.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28122:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28122:end -->

<!-- review:SF-2026-ARXIV-2605-28158:start -->
#### OR-Space: A Full-Lifecycle Workspace Benchmark for Industrial Optimization Agents

问题与 changed constraint：We introduce OR-Space, a full-lifecycle workspace benchmark for evaluating industrial optimization agents across model construction, model revision, and grounded explanation.

Mechanism 与 ownership：owner=`PLATFORM-EVALUATION-SYSTEM`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28158v1 — § exact heading: 4.3. Workspace Setting Matters: Filesystem vs. Flat Prompt`；Evaluation=`arXiv:2605.28158v1 — § exact heading: 3. OR-Space Benchmark`。

Trade-off / failure / fallback：`arXiv:2605.28158v1 — § exact heading: 4.6. Failure Analysis: What Workspace Evaluation Reveals`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28158v1 — official HTML sha256=1e17ba2cca067758b922a556965e0431d6551145b624769cbaad189a8f57f6d0; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28158:start -->仅支持 exact-v1 披露机制及实验边界；不把“We describe the benchmark design, evaluation protocol, and quality-control pipeline, and position OR-Space as a benchmark for studying the reliability, failure modes, and practical readiness of LLM agents in industrial OR workflows.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28158:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28158:end -->

<!-- review:SF-2026-ARXIV-2605-28201:start -->
#### Plant, Persist, Trigger: Sleeper Attack on Large Language Model Agents

问题与 changed constraint：However, we show that adversarial content can also persist across interactions served by the same agent, making such threats harder to detect and mitigate.

Mechanism 与 ownership：owner=`PLATFORM-SECURITY`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28201v1 — § exact heading: 1 Introduction`；Evaluation=`arXiv:2605.28201v1 — § exact heading: 3 Benchmark Construction`。

Trade-off / failure / fallback：`arXiv:2605.28201v1 — § exact heading: 5 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28201v1 — official HTML sha256=008668763414245306a7e06dd0162aab018a8ec8de1d63dca6d2c395d1635c86; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28201:start -->仅支持 exact-v1 披露机制及实验边界；不把“Experiments on seven strong open-source and closed-source LLMs show that state-of-the-art LLM agents remain vulnerable to Sleeper Attack, even when they achieve low attack success rates under a single-interaction baseline.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28201:end -->

Books Decision=`Integrate`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28201:end -->

<!-- review:SF-2026-ARXIV-2605-28213:start -->
#### Learning When to Optimize: Verified Optimization Skills from Expert GPU-Kernel Lineages

问题与 changed constraint：We introduce KLineage, which learns this missing "when" knowledge from expert kernels: instead of relying on forward rollouts, KLineage walks expert implementations backward through validation-gated simplifications and reverses each accepted step into a reusable optimization skill.

Mechanism 与 ownership：owner=`AGENT-PLATFORM`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28213v1 — § exact heading: 3 Method`；Evaluation=`arXiv:2605.28213v1 — § exact heading: 4 Evaluation`。

Trade-off / failure / fallback：`arXiv:2605.28213v1 — § exact heading: 5 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28213v1 — official HTML sha256=5a6c29327a16eb486f3ab87c7947285bdc6cf70c05861afc9e6be33047d4bd05; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28213:start -->仅支持 exact-v1 披露机制及实验边界；不把“We additionally use a separate 22-instance held-out check as a sanity test against source-case memorization.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28213:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28213:end -->

<!-- review:SF-2026-ARXIV-2605-28214:start -->
#### Out of Sight, Not Out of Mind: Unveiling Latent Attack in Latent-based Multi-Agent Systems

问题与 changed constraint：In this paper, we study whether latent states can carry attack-associated information that remains effective during clean executions.

Mechanism 与 ownership：owner=`PLATFORM-SECURITY`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28214v1 — § exact heading: 2.1 Latent-based Multi-Agent Systems`；Evaluation=`arXiv:2605.28214v1 — § exact heading: 4 Experiments`。

Trade-off / failure / fallback：`arXiv:2605.28214v1 — § exact heading: 2.3 Threat Model`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28214v1 — official HTML sha256=91ee9043fb86499854c2113111e547d97fe383fdeafe52160c01d2cf035e9872; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28214:start -->仅支持 exact-v1 披露机制及实验边界；不把“Extensive experiments show that the resulting latent attacks can substantially degrade task performance in clean executions, especially when applied to inter-agent KV-cache handoffs rather than local hidden states.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28214:end -->

Books Decision=`Integrate`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28214:end -->

<!-- review:SF-2026-ARXIV-2605-28224:start -->
#### When Does Memory Help Multi-Trajectory Inference for Tool-Use LLM Agents?

问题与 changed constraint：We propose a unified framework that decomposes memory along two axes -- the scope of transfer (within an expansion vs.

Mechanism 与 ownership：owner=`AGENT-MEMORY`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28224v1 — § exact heading: 3 A Unified Memory Framework`；Evaluation=`arXiv:2605.28224v1 — § exact heading: 4 Experimental Setup`。

Trade-off / failure / fallback：`arXiv:2605.28224v1 — § exact heading: 6 Discussion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28224v1 — official HTML sha256=f73c2b99847ff63b93b3448413df8cbc3980da4f411624734fb2481eb52a14b3; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28224:start -->仅支持 exact-v1 披露机制及实验边界；不把“across trajectories) and the abstraction of the transferred content -- and evaluate four methods under three inference strategies (best-of-N, beam search, MCTS) on four tool-use benchmarks spanning SQL, knowledge-graph, and CLI environments, in a verifier-free setting that matches the deployment regime of practical agents.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28224:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28224:end -->

<!-- review:SF-2026-ARXIV-2605-28282:start -->
#### ResearchLoop: An Evidence-Gated Control Plane for AI-Assisted Research

问题与 changed constraint：We present ResearchLoop, an evidence-gated control plane for AI-assisted computational research.

Mechanism 与 ownership：owner=`AGENT-WORKFLOW`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28282v1 — §3 ResearchLoop Protocol and Runtime; §4 Runtime Implementation`；Evaluation=`arXiv:2605.28282v1 — §7 controlled study and ablations`。

Trade-off / failure / fallback：`arXiv:2605.28282v1 — §7.2 synthetic task, single-model and sample-size limitations; Appendix C claim ledger`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28282v1 — official exact-v1 HTML read; immutable repository/checkpoint commit Not Disclosed; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28282:start -->仅支持 exact-v1 披露机制及实验边界；不把“All artifacts, manifests, and verification reports are preserved in the project repository.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28282:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28282:end -->

<!-- review:SF-2026-ARXIV-2605-28302:start -->
#### How Far Can Disaggregation Go? A Design-Space Exploration of Attention-FFN Disaggregation for Efficient MoE LLM Serving

问题与 changed constraint：Each level of disaggregation deepens the scheduling design space across workload characteristics, resource allocation, and interconnect topology, raising the central question: when does each level actually pay off?

Mechanism 与 ownership：owner=`INFER-PD-DISAGGREGATION`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28302v1 — § exact heading: 2.1 Design-Space Exploration for Optimal Disaggregated Inference`；Evaluation=`arXiv:2605.28302v1 — § exact heading: 4 Evaluation`。

Trade-off / failure / fallback：`arXiv:2605.28302v1 — § exact heading: 5 Discussion and Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28302v1 — official HTML sha256=d5bcb04b9f513ea26df32ea551e09fe23f72ba5651979e05cd229e9f171c23cf; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28302:start -->仅支持 exact-v1 披露机制及实验边界；不把“We distill concrete takeaways for jointly optimizing throughput and interactivity, including how to partition attention and FFN across GPUs as a function of workload and model architecture, providing design principles for current rack- and cluster-scale deployments as well as future disaggregated AI infrastructure.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28302:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28302:end -->

<!-- review:SF-2026-ARXIV-2605-28354:start -->
#### Plan Before Search: Search Agents Need Plan

问题与 changed constraint：We study this through Plan, a structured agentic behavior for multi-hop retrieval that decomposes a question into ordered sub-questions before any retrieval is performed, so that each search step can be anchored to a pre-designed sub-question instead of drifting under the influence of partially relevant documents retrieved earlier.

Mechanism 与 ownership：owner=`AGENT-PLANNING`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28354v1 — § exact heading: 3 Methodology`；Evaluation=`arXiv:2605.28354v1 — § exact heading: 4 Experiments`。

Trade-off / failure / fallback：`arXiv:2605.28354v1 — § exact heading: 5 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28354v1 — official HTML sha256=adefd62b5877ddd6b889b2d5466bf6d86dea3f49ca521809b6edc772b94d5cd9; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28354:start -->仅支持 exact-v1 披露机制及实验边界；不把“However, across three model families spanning 3B to 14B parameters, we find that an identical reward signal induces qualitatively different RL failure modes.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28354:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28354:end -->

<!-- review:SF-2026-ARXIV-2605-28371:start -->
#### From paper to benchmark: agentic, framework-based reproduction of under-specified methods in machine health intelligence

问题与 changed constraint：Industrial Prognostics and Health Management (PHM) provides a representative case study for a broader challenge in applied machine learning: translating published papers into executable, benchmark-ready implementations.

Mechanism 与 ownership：owner=`PLATFORM-EVALUATION-SYSTEM`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28371v1 — § exact heading: 3 Method`；Evaluation=`arXiv:2605.28371v1 — § exact heading: 4 Experiments`。

Trade-off / failure / fallback：`arXiv:2605.28371v1 — § exact heading: 5 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28371v1 — official HTML sha256=59b8cf453e48c85d21d2f09b6119c474e58ef81f53f90f1a81cd0252e3e6a66d; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28371:start -->仅支持 exact-v1 披露机制及实验边界；不把“Our results show that coupling agentic generation with a shared framework transforms paper reproduction from isolated code synthesis into executable, assumption-aware, and systematically comparable benchmark implementations.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28371:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28371:end -->

<!-- review:SF-2026-ARXIV-2605-28384:start -->
#### Meta-Attention: Bayesian Per-Token Routing for Efficient Transformer Inference

问题与 changed constraint：We propose Meta-Attention, a framework that dynamically routes each token to the most appropriate attention strategy -- full softmax attention, linear (kernel) attention, or sliding-window local attention -- via a Bayesian Meta-Controller.

Mechanism 与 ownership：owner=`INFER-SCHEDULING`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28384v1 — § exact heading: 2.4 State Space Models and the Case for an SSM Expert`；Evaluation=`arXiv:2605.28384v1 — § exact heading: 5.3 Bayesian vs. Prior-Free Ablation: Tiny LM Benchmark`。

Trade-off / failure / fallback：`arXiv:2605.28384v1 — § exact heading: 7 Discussion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28384v1 — official HTML sha256=1570cc4c065bb54d719c2ab73ec29c27fc79dd28dbc83353e870b38450392418; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28384:start -->仅支持 exact-v1 披露机制及实验边界；不把“Code available at: https://github.com/KFEAL/meta-attention”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28384:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28384:end -->

<!-- review:SF-2026-ARXIV-2605-28390:start -->
#### You Live More Than Once: Towards Hierarchical Skill Meta-Evolving

问题与 changed constraint：Specifically, we propose HiSME, a lightweight hierarchical skill meta-evolving solution that jointly optimizes skills and the skill evolving strategy by learning meta-skills from agents' task execution traces.

Mechanism 与 ownership：owner=`AGENT-PLATFORM`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28390v1 — § exact heading: 2.1 Agentic Systems`；Evaluation=`arXiv:2605.28390v1 — § exact heading: 3.3 Skill Evaluation and Maintenance`。

Trade-off / failure / fallback：`arXiv:2605.28390v1 — § exact heading: 6 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28390v1 — official HTML sha256=319497612764ee707963a369e412c779142c648f077829de02a9af1827bce409; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28390:start -->仅支持 exact-v1 披露机制及实验边界；不把“Experiments on mainstream agentic benchmarks show that meta-evolving can produce a higher-quality skill library than pure skill evolving and can derive diverse meta-skills for different scenarios, thereby facilitating future continual experience learning.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28390:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28390:end -->

<!-- review:SF-2026-ARXIV-2605-28424:start -->
#### Skill0.5: Joint Skill Internalization and Utilization for Out-of-Distribution Generalization in Agentic Reinforcement Learning

问题与 changed constraint：To address this dilemma, we propose Skill0.5, a novel agentic RL framework that explicitly differentiates skill treatments by combining general skill internalization with task-specific skill utilization.

Mechanism 与 ownership：owner=`TRAIN-GRPO`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28424v1 — § exact heading: 3 Method`；Evaluation=`arXiv:2605.28424v1 — § exact heading: 4 Experiments`。

Trade-off / failure / fallback：`arXiv:2605.28424v1 — § exact heading: 5 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28424v1 — official HTML sha256=56b115a0cea14050550666972c8c3358a23dadd06e5ca9e392e0893d2e08a307; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28424:start -->仅支持 exact-v1 披露机制及实验边界；不把“Experiments on ALFWorld and WebShop demonstrate that Skill0.5 outperforms both memory-based and skill-based RL baselines, yielding performance improvements across both in-distribution and out-of-distribution scenarios.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28424:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28424:end -->

<!-- review:SF-2026-ARXIV-2605-28433:start -->
#### Roles with Rails: Contract-Preserving Role Evolution in Multi-Agent Structured Reasoning

问题与 changed constraint：We formulate this as contract-preserving role evolution, requiring every committed edit to preserve five structural contracts (capability, communication, validation, aggregation, output protocol).

Mechanism 与 ownership：owner=`AGENT-MULTI-AGENT`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28433v1 — § exact heading: 3 Methodology: Sero`；Evaluation=`arXiv:2605.28433v1 — § exact heading: 4 Experiments`。

Trade-off / failure / fallback：`arXiv:2605.28433v1 — § exact heading: 5 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28433v1 — official HTML sha256=e6b9fa986647a1fdfaf40f75332819e7664fd3c3068b1e2919f51ea7317a4f5f; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28433:start -->仅支持 exact-v1 披露机制及实验边界；不把“Experiments on real-world reasoning benchmarks across three LLM backbones confirm the value of contract-preserving role evolution.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28433:end -->

Books Decision=`Integrate`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28433:end -->

<!-- review:SF-2026-ARXIV-2605-28467:start -->
#### Mitigating Adaptive Attacks against Reasoning Models with Activation Consistency Training

问题与 changed constraint：We study consistency training, a family of fine-tuning objectives that enforce identical behavior on clean prompts and adversarial rewrites, and evaluate its two main variants, output-level (BCT) and activation-level (ACT), across five reasoning models.

Mechanism 与 ownership：owner=`PLATFORM-SECURITY`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28467v1 — § exact heading: 3 Methodology`；Evaluation=`arXiv:2605.28467v1 — § exact heading: 4.1 Benchmarks`。

Trade-off / failure / fallback：`arXiv:2605.28467v1 — § exact heading: 7 Discussion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28467v1 — official HTML sha256=8bc115de594103d60edec321cb4440daecf363960c1cb513ddb91f26c2fa43de; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28467:start -->仅支持 exact-v1 披露机制及实验边界；不把“We find that ACT remains robust even when the model's chain-of-thought is replaced with a compliant trace from the undefended base model, pivoting to refuse prefilled jailbreaks.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28467:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28467:end -->

<!-- review:SF-2026-ARXIV-2605-28480:start -->
#### Audio-Mind: An Auditable Agentic Framework for Audio Understanding

问题与 changed constraint：We propose Audio-Mind, an auditable and pluggable framework for conditional evidence acquisition in audio understanding.

Mechanism 与 ownership：owner=`AGENT-WORKFLOW`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28480v1 — § exact heading: 2.1 Large Audio-Language Models and Audio Understanding Benchmarks`；Evaluation=`arXiv:2605.28480v1 — § exact heading: 5 Results`。

Trade-off / failure / fallback：`arXiv:2605.28480v1 — § exact heading: 6 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28480v1 — official HTML sha256=d213543a1628789189242389ff40e33dc0b8dc1e48532230aa0d590500274040; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28480:start -->仅支持 exact-v1 披露机制及实验边界；不把“Experiments on MMAR and MSU-Bench show that Audio-Mind outperforms prior audio-agent baselines, reaching 80.4% accuracy on MMAR and 82.8% accuracy on MSU-Bench.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28480:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28480:end -->

<!-- review:SF-2026-ARXIV-2605-28508:start -->
#### Benchmarking AI for low-resource contexts: Thinking beyond leaderboards

问题与 changed constraint：To support practical decision-making, we propose a shared reporting framework that preserves comparability across systems and application types while remaining sensitive to deployment context.

Mechanism 与 ownership：owner=`PLATFORM-EVALUATION-SYSTEM`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28508v1 — pp. 6–8 §3 System under test and layered evaluation`；Evaluation=`arXiv:2605.28508v1 — pp. 8–11 §4 application profiles and operating-condition tests`。

Trade-off / failure / fallback：`arXiv:2605.28508v1 — pp. 11–13 §5 minimum benchmark standard and reporting limits`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28508v1 — official PDF sha256=8beef4051c11d29813c7f2801e1cf88087f06e659f52cb810f1d20df4999a24d; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28508:start -->仅支持 exact-v1 披露机制及实验边界；不把“Finally, we emphasize the need for concise and actionable reporting artifacts for policymakers, donors, and implementers, including standardized one-page benchmark cards, deployment profiles, and explicit documentation of failure handling procedures and human oversight mechanisms.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28508:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28508:end -->

<!-- review:SF-2026-ARXIV-2605-28510:start -->
#### Efficient and Scalable Provenance Tracking for LLM-Generated Code Snippets

问题与 changed constraint：To bridge this gap, we introduce SOURCETRACKER, a 300M-parameter encoder tailored for code retrieval, together with a hybrid two-stage provenance-tracking pipeline HYBRIDSOURCETRACKER (HST).

Mechanism 与 ownership：owner=`PLATFORM-SECURITY`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28510v1 — §III Methodology: SourceTracker, Winnowing and HybridSourceTracker`；Evaluation=`arXiv:2605.28510v1 — §IV Results: recall, rank and latency`。

Trade-off / failure / fallback：`arXiv:2605.28510v1 — §V errors; §VI Discussion; §VIII-A future-work boundaries`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28510v1 — official exact-v1 HTML read; immutable repository/checkpoint commit Not Disclosed; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28510:start -->仅支持 exact-v1 披露机制及实验边界；不把“Overall, our results demonstrate that integrating vector search with fingerprinting enables scalable, high-precision provenance tracking for code produced by LLMs.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28510:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28510:end -->

<!-- review:SF-2026-ARXIV-2605-28544:start -->
#### DriveWAM: Video Generative Priors Enable Scalable World-Action Modeling for Autonomous Driving

问题与 changed constraint：We present DriveWAM, a driving world-action model that adapts a pretrained video diffusion transformer into an autoregressive video-action policy.

Mechanism 与 ownership：owner=`MULTIMODAL-WORLD-MODELS`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28544v1 — §3 Method: autoregressive world-action flow, causal guidance and selective KV memory`；Evaluation=`arXiv:2605.28544v1 — §4 Experiments and ablations`。

Trade-off / failure / fallback：`arXiv:2605.28544v1 — §5 Conclusion; Appendix C efficiency analysis; no dedicated limitations section`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28544v1 — official exact-v1 HTML read; immutable repository/checkpoint commit Not Disclosed; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28544:start -->仅支持 exact-v1 披露机制及实验边界；不把“Experiments on NAVSIM and the PhysicalAI-Autonomous-Vehicles benchmark show that DriveWAM achieves strong planning performance, and a data-scaling study from 4k to 100k driving clips further confirms the scaling potential of world-action modeling for end-to-end autonomous driving.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28544:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28544:end -->

<!-- review:SF-2026-ARXIV-2605-28561:start -->
#### Soft-SVeRL: Self-Verified Reinforcement Learning with Soft Rewards

问题与 changed constraint：We introduce Soft-RLVR, a framework for reinforcement learning from decomposed, learned verification signals.

Mechanism 与 ownership：owner=`TRAIN-RLHF`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28561v1 — § exact heading: 1 Introduction`；Evaluation=`arXiv:2605.28561v1 — § exact heading: 5 Experiment Setup`。

Trade-off / failure / fallback：`arXiv:2605.28561v1 — § exact heading: 8 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28561v1 — official HTML sha256=37a019db49266025a9f512e89d9d0055db4d54c74d0e179610cf4b5525ed3956; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28561:start -->仅支持 exact-v1 披露机制及实验边界；不把“Our experiments further show that verifier quality and checklist quality both affect downstream RL outcomes, and that explicit stabilization is essential for effective self-verification.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28561:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28561:end -->

<!-- review:SF-2026-ARXIV-2605-28565:start -->
#### Verified Misguidance: Measuring Structural Citation Failures in Search-Augmented LLMs

问题与 changed constraint：We design a three-dimension evaluation framework that scores each citation on intent-purpose alignment, source suitability, and answer-source fidelity, using expert-validated predefined matrices and a five-level fidelity rubric; the framework applies to any system that produces citation-bearing responses.

Mechanism 与 ownership：owner=`PLATFORM-EVALUATION-SYSTEM`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28565v1 — §2 CiteTrace construction; §3 three-dimensional citation evaluation`；Evaluation=`arXiv:2605.28565v1 — §4 structural citation failures and judge validation`。

Trade-off / failure / fallback：`arXiv:2605.28565v1 — Appendix A.1 scope assumptions and A.2 limitations`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28565v1 — official exact-v1 HTML read; immutable repository/checkpoint commit Not Disclosed; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28565:start -->仅支持 exact-v1 披露机制及实验边界；不把“Together, CITETRACE and its evaluation framework provide the first resource for diagnosing structural citation failures in deployed search-augmented systems.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28565:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28565:end -->

<!-- review:SF-2026-ARXIV-2605-28573:start -->
#### Efficient Pre-Training of LLMs through Truncated SVD Layers

问题与 changed constraint：The massive scaling of Large Language Models (LLMs) has made pretraining increasingly cost-prohibitive.

Mechanism 与 ownership：owner=`TRAIN-PRETRAINING`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28573v1 — § exact heading: 3 The TSVD Method`；Evaluation=`arXiv:2605.28573v1 — § exact heading: 4.3 Experimental Derivation of Adaptive Rank Selection Heuristic`。

Trade-off / failure / fallback：`arXiv:2605.28573v1 — § exact heading: 6 Discussion and Future Work`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28573v1 — official HTML sha256=74ef57819f581ccb20cd92e1585f01f2b930e2513a90ce9043b00e552d767079; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28573:start -->仅支持 exact-v1 披露机制及实验边界；不把“Theoretical analysis justifies the advantage of the approach in pretraining dynamics and experiments across various model scales demonstrate that it is effective empirically.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28573:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28573:end -->

<!-- review:SF-2026-ARXIV-2605-28617:start -->
#### LACUNA: Safe Agents as Recursive Program Holes

问题与 changed constraint：We present LACUNA, a programming model for agents that closes this split while preserving safety.

Mechanism 与 ownership：owner=`AGENT-TOOL-CALLING`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28617v1 — §3 typed holes and nested calls; §4 static/capability safety`；Evaluation=`arXiv:2605.28617v1 — §7 verifier, tool-use and multi-turn evaluation`。

Trade-off / failure / fallback：`arXiv:2605.28617v1 — §Limitations: well-typed is not correct; authority is only as tight as granted scope`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28617v1 — official exact-v1 HTML read; immutable repository/checkpoint commit Not Disclosed; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28617:start -->仅支持 exact-v1 披露机制及实验边界；不把“We evaluate LACUNA on a collection of test cases, BrowseComp-Plus, and $τ^2$-bench.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28617:end -->

Books Decision=`Integrate`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28617:end -->

<!-- review:SF-2026-ARXIV-2605-28632:start -->
#### Blind PRNG Hijacking: An Undetectable Integrity-Preserving Attack Against LLM Watermarking

问题与 changed constraint：Cryptographic watermarking is a leading defense for attributing text generated by large language models (LLMs).

Mechanism 与 ownership：owner=`PLATFORM-SECURITY`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28632v1 — § exact heading: 2.3 PRNG Security in ML Systems`；Evaluation=`arXiv:2605.28632v1 — § exact heading: 5 Evaluation`。

Trade-off / failure / fallback：`arXiv:2605.28632v1 — § exact heading: 3 Threat Model and Problem Formulation`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28632v1 — official HTML sha256=aafde923a8bedf299b01a1b87790b4fc26d09b9c734ec1891536e0ffbba5474c; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28632:start -->仅支持 exact-v1 披露机制及实验边界；不把“These findings establish PRNG integrity as a first-class security requirement for cryptographic content-provenance systems.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28632:end -->

Books Decision=`Integrate`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28632:end -->

<!-- review:SF-2026-ARXIV-2605-28634:start -->
#### PrimitiveVLA: Learning Reusable Motion Primitives for Efficient and Generalizable Robotic Manipulation

问题与 changed constraint：We propose PrimitiveVLA, a framework that shifts this paradigm toward a Primitive-Centric Disassemble &amp; Assemble paradigm.

Mechanism 与 ownership：owner=`MULTIMODAL-EMBODIED-VLA`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28634v1 — § exact heading: 2.1 Vision-Language-Action Models`；Evaluation=`arXiv:2605.28634v1 — § exact heading: 5 Experiments`。

Trade-off / failure / fallback：`arXiv:2605.28634v1 — § exact heading: 6 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28634v1 — official HTML sha256=28d4c6c0aa204e61c3cfe7c1bd438f923cee3007f437aec33e041b2342f66af3; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28634:start -->仅支持 exact-v1 披露机制及实验边界；不把“Extensive experiments show that our framework improves data efficiency and achieves superior zero-shot generalization across unseen and long-horizon tasks.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28634:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28634:end -->

<!-- review:SF-2026-ARXIV-2605-28640:start -->
#### Augmenting Attention with Exponentially Decaying Memory Improves Query-Aware KV Sparsity

问题与 changed constraint：In this paper, we investigate whether this exponentially decaying memory can also improve existing query-aware sparse inference methods.

Mechanism 与 ownership：owner=`INFER-KV-CACHE`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28640v1 — §2 exponentially decaying memory and sparse inference instantiations`；Evaluation=`arXiv:2605.28640v1 — §3 experiments and H1/H2 analyses`。

Trade-off / failure / fallback：`arXiv:2605.28640v1 — §Limitations: two 7B checkpoints, 4K context and RULER-only task family`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28640v1 — official exact-v1 HTML read; immutable repository/checkpoint commit Not Disclosed; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28640:start -->仅支持 exact-v1 披露机制及实验边界；不把“Using representative methods including Quest, MoBA, and SnapKV, we show that RAT+ consistently improves accuracy over standard attention across sparse budgets on eight needle-in-a-haystack tasks.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28640:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28640:end -->

<!-- review:SF-2026-ARXIV-2605-28646:start -->
#### MaskClaw: Edge-Side Personalized Privacy Arbitration for GUI Agents with Behavior-Driven Skill Evolution

问题与 changed constraint：We present MaskClaw, an edge-side privacy arbitrator for GUI agents.

Mechanism 与 ownership：owner=`PLATFORM-SECURITY`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28646v1 — §4 edge evidence extraction, policy arbitration, SafeScreenshot and skill evolution`；Evaluation=`arXiv:2605.28646v1 — §5–6 evaluation, sandbox checks and error analysis`。

Trade-off / failure / fallback：`arXiv:2605.28646v1 — §Limitations: sanitized scenarios, trusted edge and short-horizon personalization`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28646v1 — official exact-v1 HTML read; immutable repository/checkpoint commit Not Disclosed; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28646:start -->仅支持 exact-v1 披露机制及实验边界；不把“Experiments show that pattern matching, cloud reasoning, and routing alone tend to over-confirm, over-mask, or expose raw screenshots under the same protocol.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28646:end -->

Books Decision=`Integrate`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28646:end -->

<!-- review:SF-2026-ARXIV-2605-28678:start -->
#### DREAM-R: Multimodal Speculative Reasoning with RL-Based Refined Drafting, Precise Verification, and Fully Parallel Execution

问题与 changed constraint：In this work, we introduce DREAM-R, a framework that substantially improves the performance of speculative reasoning.

Mechanism 与 ownership：owner=`INFER-SPECULATIVE-DECODING`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28678v1 — § exact heading: 3 Method`；Evaluation=`arXiv:2605.28678v1 — § exact heading: 4 Experiments`。

Trade-off / failure / fallback：`arXiv:2605.28678v1 — § exact heading: 5 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28678v1 — official HTML sha256=1a1a8f4e1c8ac3653a31c04eee5001b8bd690ec4cacab7bfa00bc96c7270d947; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28678:start -->仅支持 exact-v1 披露机制及实验边界；不把“Experiments on reasoning-heavy benchmarks demonstrate up to speedup while preserving target-model accuracy, yielding substantial efficiency gains without compromising reasoning quality.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28678:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28678:end -->

<!-- review:SF-2026-ARXIV-2605-28691:start -->
#### OSP-Next: Efficient High-Quality Video Generation with Sparse Sequence Parallelism, HiF8 Quantization, and Reinforcement Learning

问题与 changed constraint：We introduce OSP-Next, an efficient text-to-video generation model that integrates sparse attention, parallelism, quantization, and reinforcement learning.

Mechanism 与 ownership：owner=`MULTIMODAL-GENERATIVE-PARADIGMS`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28691v1 — § exact heading: 2.1 Sparse Video Generation Model`；Evaluation=`arXiv:2605.28691v1 — § exact heading: 4 Experiment`。

Trade-off / failure / fallback：`arXiv:2605.28691v1 — § exact heading: 5 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28691v1 — official HTML sha256=327ba473a5ca5523ab42d5daa2cd3b7c42aeeee6b6ecb6ae168b5896299fc13a; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28691:start -->仅支持 exact-v1 披露机制及实验边界；不把“Experiments show that OSP-Next achieves a VBench total score of 83.73%, surpassing the Wan2.1 baseline.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28691:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28691:end -->

<!-- review:SF-2026-ARXIV-2605-28699:start -->
#### TRACER: Turn-level Regret Matching with Inner Reinforcement Credit for Cooperative Multi-LLM Reasoning

问题与 changed constraint：We introduce TRACER, a turn-level reinforcement framework for cooperative multi-LLM reasoning.

Mechanism 与 ownership：owner=`TRAIN-GRPO`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28699v1 — § exact heading: 2.2 Multi-Agent System`；Evaluation=`arXiv:2605.28699v1 — § exact heading: 5 Experiments`。

Trade-off / failure / fallback：`arXiv:2605.28699v1 — § exact heading: 6 Conclusion and Limitations`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28699v1 — official HTML sha256=b46ff12911d0d68e6d23a196c51d66c97243f6cce1cd9ee2d7c2e6a1acc91235; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28699:start -->仅支持 exact-v1 披露机制及实验边界；不把“We train all local RL-style methods on the GSM8K training split and evaluate on held-out GSM8K, MATH500, and GPQA-Diamond to measure in-domain accuracy, cross-benchmark generalization, inference cost, and correction-preservation behavior.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28699:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28699:end -->

<!-- review:SF-2026-ARXIV-2605-28704:start -->
#### Expressive Power of Floating-Point Neural Networks with Arbitrary Reduction Orders and Inexact Activation Implementations

问题与 changed constraint：In this work, we study the expressive power of floating-point neural networks under generalized floating-point execution semantics, including arbitrary reduction orders and inexact activation implementations with bounded ulp errors.

Mechanism 与 ownership：owner=`INFER-TENSORRT-LLM`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28704v1 — § exact heading: I Introduction`；Evaluation=`arXiv:2605.28704v1 — § exact heading: III Main Results`。

Trade-off / failure / fallback：`arXiv:2605.28704v1 — § exact heading: I-A Contribution`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28704v1 — official HTML sha256=4a7a9a3977cbb61bc5708038d0f880bde52cc4bfcdd5fb033aee756b8612194f; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28704:start -->仅支持 exact-v1 披露机制及实验边界；不把“To this end, we introduce a general distinguishability framework and show that the ability to distinguish every pair of distinct inputs in the first layer is necessary for universal representability.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28704:end -->

Books Decision=`Integrate`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28704:end -->

<!-- review:SF-2026-ARXIV-2605-28721:start -->
#### LiveBrowseComp: Are Search Agents Searching, or Just Verifying What They Already Know?

问题与 changed constraint：We study this question on BrowseComp with three diagnostics.

Mechanism 与 ownership：owner=`PLATFORM-EVALUATION-SYSTEM`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28721v1 — § exact heading: 2.4 From Diagnosis to Benchmark Design`；Evaluation=`arXiv:2605.28721v1 — § exact heading: 2.3 Search Strategy Analysis`。

Trade-off / failure / fallback：`arXiv:2605.28721v1 — § exact heading: 6 Discussion and Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28721v1 — official HTML sha256=aeaa68114c24fa582046ca5879e68e549f4c733433734b424d86c75f38e35acf; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28721:start -->仅支持 exact-v1 披露机制及实验边界；不把“We then introduce LiveBrowseComp, a deep-search benchmark designed to evaluate agents beyond intrinsic coverage.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28721:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28721:end -->

<!-- review:SF-2026-ARXIV-2605-28726:start -->
#### How VLAs Fail Differently: Black-Box Action Monitoring Reveals Architecture-Specific Failure Signatures

问题与 changed constraint：We discover that VLA architectures fail in fundamentally different, predictable ways at the motor-command level.

Mechanism 与 ownership：owner=`MULTIMODAL-EMBODIED-VLA`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28726v1 — § exact heading: II Method`；Evaluation=`arXiv:2605.28726v1 — § exact heading: IV Experiments`。

Trade-off / failure / fallback：`arXiv:2605.28726v1 — § exact heading: IV-C Failure Prediction: Which Monitors Work?`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28726v1 — official HTML sha256=90cd7e1a54362609991628c3db8b3b43348ca9e11c25067c1e202fb5bc05f38f; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28726:start -->仅支持 exact-v1 披露机制及实验边界；不把“Running VQ-BeT, Diffusion Policy, and ACT on identical evaluation protocols (n=450 episodes across PushT and ALOHA 14-DOF bimanual manipulation), we find: (1) direction reversal rate is a universal failure predictor across all three architectures (AUROC=0.93, 0.79, 0.91; p&lt;0.001); (2) jerk monitoring is predictive only for discrete-token architectures, following a discrete-to-continuous gradient (0.88, 0.69, 0.41)”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28726:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28726:end -->

<!-- review:SF-2026-ARXIV-2605-28732:start -->
#### MemTrace: Tracing and Attributing Errors in Large Language Model Memory Systems

问题与 changed constraint：In this work, we study the new problem of error tracing and attribution in LLM memory systems.

Mechanism 与 ownership：owner=`AGENT-MEMORY`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28732v1 — § exact heading: 2 Tracing and Attributing Errors in Memory Systems`；Evaluation=`arXiv:2605.28732v1 — § exact heading: 5 Experiments`。

Trade-off / failure / fallback：`arXiv:2605.28732v1 — § exact heading: 8 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28732v1 — official HTML sha256=c81383e0d1ae7799a14d2a9bd4911c986acf573281a52a6c6c13834fbea2f6a3; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28732:start -->仅支持 exact-v1 披露机制及实验边界；不把“Code will be released at https://github.com/zjunlp/MemTrace.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28732:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28732:end -->

<!-- review:SF-2026-ARXIV-2605-28742:start -->
#### CORE: Contrastive Reflection Enables Rapid Improvements in Reasoning

问题与 changed constraint：To address this challenge, we introduce Contrastive Reflection (CORE), a non-parametric learning algorithm that compares past reasoning traces to generate insights: short natural-language descriptions of reasoning strategies and constraints that capture differences between successful and unsuccessful problem attempts.

Mechanism 与 ownership：owner=`AGENT-REFLECTION`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28742v1 — § exact heading: 1 Introduction`；Evaluation=`arXiv:2605.28742v1 — § exact heading: 4 Evaluation`。

Trade-off / failure / fallback：`arXiv:2605.28742v1 — § exact heading: 6 Discussion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28742v1 — official HTML sha256=948395dbaa3e07d1b9fdd398c0c4b798d06dc1a875a55c6c2950cc6ff67acefa; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28742:start -->仅支持 exact-v1 披露机制及实验边界；不把“Across four reasoning tasks, we demonstrate that CORE enables more rapid improvement than both parametric (GRPO) and non-parametric (GEPA, episodic RAG, and MemRL) methods, while using fewer rollouts.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28742:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28742:end -->

<!-- review:SF-2026-ARXIV-2605-28751:start -->
#### Extrapolative Weight Averaging Reveals Correctness-Efficiency Frontiers in Code RL

问题与 changed constraint：We study this question in RL for competitive programming, where hidden unit tests under time and memory limits enforce both functional correctness and computational efficiency.

Mechanism 与 ownership：owner=`TRAIN-GRPO`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28751v1 — § exact heading: 3.4 Extrapolative weight averaging generalizes across inference settings and model scales`；Evaluation=`arXiv:2605.28751v1 — § exact heading: 4 Analysis and Perspectives`。

Trade-off / failure / fallback：`arXiv:2605.28751v1 — § exact heading: 6 Discussion and Limitations`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28751v1 — official HTML sha256=2ad8c69c8a772c3094e9868186053eb7541cc9e186faa3e4caa9f18359f26f0a; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28751:start -->仅支持 exact-v1 披露机制及实验边界；不把“These results show that nested unit-test coverage in code RL induces a frontier that extrapolative weight averaging can navigate, extend, and exploit.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28751:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28751:end -->

<!-- review:SF-2026-ARXIV-2605-28760:start -->
#### LLM Zeroth-Order Fine-Tuning is an Inference Workload

问题与 changed constraint：We show that LLM ZO fine-tuning is an inference-dominated workload and execute its repeated scoring phase through a serving runtime.

Mechanism 与 ownership：owner=`TRAIN-LORA`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28760v1 — § exact heading: 3 System Design`；Evaluation=`arXiv:2605.28760v1 — § exact heading: 4 Evaluation Setup`。

Trade-off / failure / fallback：`arXiv:2605.28760v1 — § exact heading: 7 Discussion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28760v1 — official HTML sha256=efb091acec460dba1a6d525cc918d4b70a6c230b181d97523eae8b763dbc309b; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28760:start -->仅支持 exact-v1 披露机制及实验边界；不把“We show that LLM ZO fine-tuning is an inference-dominated workload and execute its repeated scoring phase through a serving runtime.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28760:end -->

Books Decision=`Integrate`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28760:end -->

<!-- review:SF-2026-ARXIV-2605-28764:start -->
#### SwarmHarness: Skill-Based Task Routing via Decentralized Incentive-Aligned AI Agent Networks

问题与 changed constraint：We propose SwarmHarness, a decentralised protocol in which HarnessAPI skill nodes self-organise into a compute swarm without any central authority.

Mechanism 与 ownership：owner=`AGENT-MULTI-AGENT`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28764v1 — §3 SwarmNode, registry, router and credit ledger; §4 attribution`；Evaluation=`arXiv:2605.28764v1 — §5 feasibility and deployment path`。

Trade-off / failure / fallback：`arXiv:2605.28764v1 — §5.3–5.5 bootstrap, security/privacy and open challenges`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28764v1 — official exact-v1 HTML read; immutable repository/checkpoint commit Not Disclosed; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28764:start -->仅支持 exact-v1 披露机制及实验边界；不把“Beyond compute sharing, SwarmHarness is a foundational primitive for autonomous distributed AI agent networks in which agents hire compute, route subtasks, and settle credits without human intermediation.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28764:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28764:end -->

<!-- review:SF-2026-ARXIV-2605-28773:start -->
#### Rethinking Memory as Continuously Evolving Connectivity

问题与 changed constraint：To address this, we propose FluxMem, a connectivity-evolving memory framework that models memory as a heterogeneous graph and progressively refines its topology through three stages: initial connection formation, feedback-driven refinement, and long-term consolidation.

Mechanism 与 ownership：owner=`AGENT-MEMORY`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28773v1 — § exact heading: 2 FluxMem Memory Architecture`；Evaluation=`arXiv:2605.28773v1 — § exact heading: 4 Experiments`。

Trade-off / failure / fallback：`arXiv:2605.28773v1 — § exact heading: 6 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28773v1 — official HTML sha256=d18935b37ea808d2c0daeb4cc59dd49ecae728926ce886f1b3840a91e9819065; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28773:start -->仅支持 exact-v1 披露机制及实验边界；不把“The code will be open-sourced in https://github.com/zjunlp/LightMem.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28773:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28773:end -->

<!-- review:SF-2026-ARXIV-2605-28774:start -->
#### Agent Explorative Policy Optimization for Multimodal Agentic Reasoning

问题与 changed constraint：We propose AXPO (Agent eXplorative Policy Optimization): for each all-wrong tool-using subgroup, AXPO fixes the thinking prefix and resamples the tool call and its continuation, paired with uncertainty-based prefix selection.

Mechanism 与 ownership：owner=`TRAIN-GRPO`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28774v1 — § exact heading: A.2 System Prompt and Tool Interface`；Evaluation=`arXiv:2605.28774v1 — § exact heading: 2 Analysis of RL in Agentic Reasoning`。

Trade-off / failure / fallback：`arXiv:2605.28774v1 — § exact heading: 6 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28774v1 — official HTML sha256=d13ded6dc9cb9f022fcba82d2f405dbb31ca326a1d1cbc8f2311772a26d1d576; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28774:start -->仅支持 exact-v1 披露机制及实验边界；不把“Across nine multimodal benchmarks and three scales of Qwen3-VL-Thinking, SFT+AXPO outperforms SFT+GRPO at average (+1.8pp Pass@1 and +1.8pp Pass@4 at 8B on average) and 8B with SFT+AXPO surpasses the 32B Base on Pass@4 with 4 times fewer parameters.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28774:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28774:end -->

<!-- review:SF-2026-ARXIV-2605-28778:start -->
#### Can LLMs Use Linguistic Uncertainty Markers to Reliably Reflect Intrinsic Confidence?

问题与 changed constraint：We conduct the first systematic study of this question, formalizing _marker internal confidence_ (MIC) as the estimated intrinsic confidence a model associates with a specific epistemic marker in a given task domain.

Mechanism 与 ownership：owner=`PLATFORM-EVALUATION-SYSTEM`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28778v1 — § exact heading: 5.3 Impact of System Prompt`；Evaluation=`arXiv:2605.28778v1 — § exact heading: 4 Experimental Setup`。

Trade-off / failure / fallback：`arXiv:2605.28778v1 — § exact heading: 6 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28778v1 — official HTML sha256=01b64c870e884d24bc10330a3d3515358d4337041ab0b0076cad2275dc758860; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28778:start -->仅支持 exact-v1 披露机制及实验边界；不把“Applying our analysis framework to diverse models and tasks, we find that LLMs remain faithfully miscalibrated even under model-centric interpretation of marker meanings, struggling to differentiate markers by internal confidence across distributions despite preserving a somewhat consistent ranking order across tasks.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28778:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28778:end -->

<!-- review:SF-2026-ARXIV-2605-28787:start -->
#### Do Data Agents Need Semantic Metadata? A Comparative Study in Agentic Data Retrieval

问题与 changed constraint：We present a comparative analysis of agentic data retrieval across two distinct environments: a Baseline Agent searching billions of open-web documents, and a Semantic Agent leveraging a corpus of 90 million datasets using schema$.$org.

Mechanism 与 ownership：owner=`AGENT-RAG`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28787v1 — § exact heading: 3 System Architecture & Experimental Setup`；Evaluation=`arXiv:2605.28787v1 — § exact heading: 4 Evaluation Methodology`。

Trade-off / failure / fallback：`arXiv:2605.28787v1 — § exact heading: 6 Discussion and Future Work`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28787v1 — official HTML sha256=4c1f63382d975afe45c1ff2cb12bd17b1fd33893d7aadc0f6e6d17130428b66a; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28787:start -->仅支持 exact-v1 披露机制及实验边界；不把“Our results reveal a clear divergence.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28787:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28787:end -->

<!-- review:SF-2026-ARXIV-2605-28803:start -->
#### HoloQ-VLA: Uniform W4A4 Quantization of Vision-Language-Action Models

问题与 changed constraint：We present HoloQ-VLA, the first training-free PTQ framework that compresses both the language backbone and the entire diffusion action head to uniform W4A4 precision without mixed-precision allocation.

Mechanism 与 ownership：owner=`MULTIMODAL-EMBODIED-VLA`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28803v1 — § exact heading: 3.1 Vision Language Action (VLA) Model`；Evaluation=`arXiv:2605.28803v1 — § exact heading: 5 Experiments and Results`。

Trade-off / failure / fallback：`arXiv:2605.28803v1 — § exact heading: 6 Discussion and Analysis`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28803v1 — official HTML sha256=9cf86ee52580269d695f1b428859a43d79cc4d552873686384aa093796ecedb6; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28803:start -->仅支持 exact-v1 披露机制及实验边界；不把“Real-world manipulation experiments further demonstrate that HoloQ-VLA maintains smooth and accurate control across diverse real-world scenarios.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28803:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28803:end -->

<!-- review:SF-2026-ARXIV-2605-28805:start -->
#### OmniVerifier-M1: Multimodal Meta-Verifier with Explicit Structured Recalibration

问题与 changed constraint：In this work, we investigate multimodal meta-verification, which leverages verifier-generated rationales rather than decision-only signals, and explore how to effectively incorporate meta-verification feedback into multimodal verifier training.

Mechanism 与 ownership：owner=`PLATFORM-EVALUATION-SYSTEM`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28805v1 — § exact heading: 1 Introduction`；Evaluation=`arXiv:2605.28805v1 — § exact heading: Appendix B Additional Experiments`。

Trade-off / failure / fallback：`arXiv:2605.28805v1 — § exact heading: 7 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28805v1 — official HTML sha256=3c391c76b440fdc62c981dbf8764efd8db77092b07a8c527ed7c2f06c9d088c6; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28805:start -->仅支持 exact-v1 披露机制及实验边界；不把“First, symbolic verifier outputs (e.g., bounding boxes) outperform textual explanations as meta-verification rationales, enabling efficient rule-based reinforcement learning rewards while avoiding reliance on model-based rewards from auxiliary judge models.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28805:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28805:end -->

<!-- review:SF-2026-ARXIV-2605-28807:start -->
#### Calibrating Conservatism for Scalable Oversight

问题与 changed constraint：We introduce Calibrated Collective Oversight (CCO), which aggregates diverse auxiliary scoring functions into a penalty measuring deviation from a conservative baseline.

Mechanism 与 ownership：owner=`PLATFORM-EVALUATION-SYSTEM`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28807v1 — § exact heading: 1 Introduction`；Evaluation=`arXiv:2605.28807v1 — § exact heading: 5 Experiments`。

Trade-off / failure / fallback：`arXiv:2605.28807v1 — § exact heading: 6 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28807v1 — official HTML sha256=fc1cea1dc0e5de404483eaaf47079402901d8349b2ea8d5133060ab680d51c22; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28807:start -->仅支持 exact-v1 披露机制及实验边界；不把“Inspired by Attainable Utility Preservation, CCO enables collective conservatism: actions face a penalty proportional to overseer concern, so high-utility actions are still selected when overseers find them unobjectionable and overridden only when concern accumulates.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28807:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28807:end -->

<!-- review:SF-2026-ARXIV-2605-28819:start -->
#### PEFT-Arena: Understanding Parameter-Efficient Finetuning from a Stability-Plasticity Perspective

问题与 changed constraint：We introduce PEFT-Arena, a benchmark that jointly measures downstream performance and general capability retention.

Mechanism 与 ownership：owner=`TRAIN-LORA`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28819v1 — § exact heading: 1 Introduction`；Evaluation=`arXiv:2605.28819v1 — § exact heading: 2 The PEFT-Arena Benchmark`。

Trade-off / failure / fallback：`arXiv:2605.28819v1 — § exact heading: Limitations`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28819v1 — official HTML sha256=8e6e8e4418944fbd589b91d7ddf5befba422f816d98e2de9b6ebcc57deeed7e3; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28819:start -->仅支持 exact-v1 披露机制及实验边界；不把“In activation space, retention metrics show whether finetuning preserves or distorts general-capability representations, with forgetting linked to non-isometric representation distortion.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28819:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28819:end -->

<!-- review:SF-2026-ARXIV-2605-28889:start -->
#### Context Distillation as Latent Memory Management

问题与 changed constraint：We formulate context distillation as a latent memory management problem.

Mechanism 与 ownership：owner=`AGENT-MEMORY`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28889v1 — § exact heading: 3 Methodology`；Evaluation=`arXiv:2605.28889v1 — § exact heading: 4 Experiments`。

Trade-off / failure / fallback：`arXiv:2605.28889v1 — § exact heading: 5 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28889v1 — official HTML sha256=484b7c915791a1d932ca5b0d304ea69886f807144f2b39de985b7a9026b5cc7f; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28889:start -->仅支持 exact-v1 披露机制及实验边界；不把“Experiments show that our method substantially outperforms baselines with retrieval, while Self-Gating improves robustness by deactivate unnecessary latent memories.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28889:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28889:end -->

<!-- review:SF-2026-ARXIV-2605-28890:start -->
#### Echoes within the Reasoning: Stealthy and Effective Watermarking via Chain of Thought

问题与 changed constraint：We propose BiCoT, a watermarking framework that embeds ownership signals into the internal geometry of reasoning traces by aligning high-saliency structural anchors with a private signature subspace while regularizing ordinary control tokens to preserve semantic capacity.

Mechanism 与 ownership：owner=`PLATFORM-SECURITY`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28890v1 — § exact heading: 4 The Proposed Method`；Evaluation=`arXiv:2605.28890v1 — § exact heading: 5 Experiments`。

Trade-off / failure / fallback：`arXiv:2605.28890v1 — § exact heading: 5.8 Threat Model Boundary and Limitation: Logprob Enabled Verification`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28890v1 — official HTML sha256=fd2aa444bf003c5dbca9124efc078287ad0ad64b1b099778107fd4dff06c8dbe; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28890:start -->仅支持 exact-v1 披露机制及实验边界；不把“Experiments show that BiCoT preserves reasoning fidelity across diverse complex reasoning tasks while achieving robust detection under fine-tuning, quantization, model-level perturbations, and adaptive output-level attacks across in-domain and out-of-distribution settings.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28890:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28890:end -->

<!-- review:SF-2026-ARXIV-2605-28893:start -->
#### Towards Demystifying and Repairing LLM-in-the-Loop Vulnerabilities

问题与 changed constraint：Although some studies have attempted to investigate the impact of LiL vulnerabilities, they have unfortunately failed to clearly distinguish LiL vulnerabilities from conventional ones, leaving the understanding of real-world LiL vulnerabilities an open problem.

Mechanism 与 ownership：owner=`PLATFORM-SECURITY`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28893v1 — § exact heading: 3. Methodology`；Evaluation=`arXiv:2605.28893v1 — § exact heading: 3.2. Benchmark Construction`。

Trade-off / failure / fallback：`arXiv:2605.28893v1 — § exact heading: 4.5. RQ4: Repair Failure Root Causes`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28893v1 — official HTML sha256=0ccec6e5023425d608e1da29b300536ad3391a559b6104605c01c756bba173de; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28893:start -->仅支持 exact-v1 披露机制及实验边界；不把“Experimental results on 20 agent-model configuration demonstrate that LiL vulnerabilities are far more challenging to fix, with an average decrease of 10.8% Pass@1 rate compared to other types of vulnerabilities.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28893:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28893:end -->

<!-- review:SF-2026-ARXIV-2605-28897:start -->
#### Review Arcade: On the Human Alignment and Gameability of LLM Reviews

问题与 changed constraint：In this work, we perform empirical experiments on papers from the 2025 ACL Rolling Review (ARR) to evaluate LLM reviews from both the author and the reviewer perspective.

Mechanism 与 ownership：owner=`PLATFORM-EVALUATION-SYSTEM`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28897v1 — § exact heading: 3 Method`；Evaluation=`arXiv:2605.28897v1 — § exact heading: 4 Experimental Setup`。

Trade-off / failure / fallback：`arXiv:2605.28897v1 — § exact heading: 5 Results and Discussion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28897v1 — official HTML sha256=42918fe6e08c174c1b7c008a76802891bf988cc6c027269eecf588031cbe8111; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28897:start -->仅支持 exact-v1 披露机制及实验边界；不把“We find that this "gaming" of LLM reviews can be effective in specific scenarios, leading to a statistically significant increase of overall scores for up to 35\% of papers.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28897:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28897:end -->

<!-- review:SF-2026-ARXIV-2605-28914:start -->
#### AIRGuard: Guarding Agent Actions with Runtime Authority Control

问题与 changed constraint：We present AIRGuard, a runtime guard that operationalizes least privilege as action-time authorization.

Mechanism 与 ownership：owner=`AGENT-TOOL-CALLING`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28914v1 — § exact heading: 2.1 Threat Model`；Evaluation=`arXiv:2605.28914v1 — § exact heading: 4 Evaluation`。

Trade-off / failure / fallback：`arXiv:2605.28914v1 — § exact heading: 6 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28914v1 — official HTML sha256=d0264220f2ded5ab77e06f15529acb9124ca3dc29ce337b5266947540395fa49; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28914:start -->仅支持 exact-v1 披露机制及实验边界；不把“Code and data are available at https://github.com/Sophie508/AIRGuard.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28914:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28914:end -->

<!-- review:SF-2026-ARXIV-2605-28918:start -->
#### When LLM Reward Design Fails: Diagnostic-Driven Refinement for Sparse Structured RL

问题与 changed constraint：We study PPO-trained agents using MiniGrid as core evaluation and MuJoCo as boundary stress test.

Mechanism 与 ownership：owner=`TRAIN-GRPO`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28918v1 — § exact heading: 3 Method`；Evaluation=`arXiv:2605.28918v1 — § exact heading: 5 Experimental Setup`。

Trade-off / failure / fallback：`arXiv:2605.28918v1 — § exact heading: 7 Failure Taxonomy`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28918v1 — official HTML sha256=a085ce1d967c0158fa236d3b634861af1ef381b37448f8e1ccb20c4757bf685b; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28918:start -->仅支持 exact-v1 披露机制及实验边界；不把“Continuous-control results show the boundary: success-based diagnostics can misfire in dense-reward locomotion, and return-trend feedback removes one false-positive mechanism without robust gains.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28918:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28918:end -->

<!-- review:SF-2026-ARXIV-2605-28920:start -->
#### Conf-Gen: Conformal Uncertainty Quantification for Generative Models

问题与 changed constraint：In this work we introduce conformal generation (Conf-Gen), a general framework adapting CRC to generative tasks while relaxing its theoretical assumptions.

Mechanism 与 ownership：owner=`PLATFORM-EVALUATION-SYSTEM`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28920v1 — § exact heading: Section 1 Introduction`；Evaluation=`arXiv:2605.28920v1 — § exact heading: Section 6 Experiments`。

Trade-off / failure / fallback：`arXiv:2605.28920v1 — § exact heading: Section 7 Conclusion and Future Work`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28920v1 — official HTML sha256=0e5297f8e2a1b9339cab9737e3c87239243a625f9b74bb74f5b340282fcfea97; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28920:start -->仅支持 exact-v1 披露机制及实验边界；不把“We demonstrate the flexibility of Conf-Gen through some novel applications, including obtaining conformal guarantees on: image generators producing non-memorized images, conversational AI systems having asked enough clarifying questions, and the output of AI agents being correct.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28920:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28920:end -->

<!-- review:SF-2026-ARXIV-2605-28969:start -->
#### Beyond Recall: Behavioral Specification as an Interpretive Layer for AI Personalization

问题与 changed constraint：We introduce representational accuracy to measure how faithfully a system captures a person's interpretation.

Mechanism 与 ownership：owner=`AGENT-MEMORY`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28969v1 — § exact heading: 2.2 Memory systems for LLM agents`；Evaluation=`arXiv:2605.28969v1 — § exact heading: 2. Prior Work, Industry Benchmarks, The Fifth Target`。

Trade-off / failure / fallback：`arXiv:2605.28969v1 — § exact heading: 3.3.6 Rubric-handling limitations (post-hoc validity audit)`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28969v1 — official HTML sha256=101b3e17cd8bba2def194b91f2814eea8c6024099488edfc82a5e614fab3a555; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28969:start -->仅支持 exact-v1 披露机制及实验边界；不把“We evaluate the Specification on a prototype benchmark of held-out behavioral predictions scored by a calibrated 5-judge LLM panel.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28969:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28969:end -->

<!-- review:SF-2026-ARXIV-2605-28991:start -->
#### A Secure, Manifest-Based Framework for Delegated Privilege Promotion

问题与 changed constraint：We present a secure, manifest-based infrastructure for delegated promotion of privileged software components, deployed in production as part of a large-scale enterprise database system serving both cloud and on-premises installations.

Mechanism 与 ownership：owner=`AGENT-TOOL-CALLING`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28991v1 — § exact heading: II System Architecture and Design`；Evaluation=`arXiv:2605.28991v1 — § exact heading: IV Security Analysis`。

Trade-off / failure / fallback：`arXiv:2605.28991v1 — § exact heading: II-A Threat Model`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28991v1 — official HTML sha256=38bca95491babf9d404fed1ccf11bc2e90fd9714aaab3e3ec0e9861181a48d41; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28991:start -->仅支持 exact-v1 披露机制及实验边界；不把“The system explicitly mitigates Time-of-Check-to-Time-of-Use (TOCTOU) attacks using file-descriptor-bound validation and promotion, supports offline key rotation and revocation, and enables zero-downtime self-update via atomic replacement.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28991:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28991:end -->

<!-- review:SF-2026-ARXIV-2605-28999:start -->
#### Measuring Real-World Prompt Injection Attacks in LLM-based Resume Screening

问题与 changed constraint：In this work, we present the first systematic study of prompt-injection attacks in a widely used application: LLM-based resume screening.

Mechanism 与 ownership：owner=`PLATFORM-SECURITY`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28999v1 — § exact heading: 3.1 Threat Model`；Evaluation=`arXiv:2605.28999v1 — § exact heading: 5.5 Method Selection for Large-Scale Analysis`。

Trade-off / failure / fallback：`arXiv:2605.28999v1 — § exact heading: 7 Discussion and Limitations`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28999v1 — official HTML sha256=4c6e94a2e9d6e480605f51128be9c9358f590c91fc80d8e103ef939bb84b73b6; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28999:start -->仅支持 exact-v1 披露机制及实验边界；不把“Manual validation on a small-scale dataset demonstrates that our detectors achieve high precision and outperform state-of-the-art general-purpose detectors.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28999:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28999:end -->

<!-- review:SF-2026-ARXIV-2605-29001:start -->
#### FormInv: A Measurement Protocol for Semantic Invariance in Mathematical Reasoning Benchmarks

问题与 changed constraint：A paraphrase-quality audit of MathCheck (ICLR 2025) detected 4 semantically incorrect paraphrases in 129 groups (3.1%); removing them drops GPT-4o from rank 2 to rank 4 and elevates Claude Haiku and DeepSeek V3 above it; these ranking changes are invisible to any single-model evaluation.

Mechanism 与 ownership：owner=`PLATFORM-EVALUATION-SYSTEM`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.29001v1 — § exact heading: 1 Introduction`；Evaluation=`arXiv:2605.29001v1 — § exact heading: 4 FormInv Benchmark`。

Trade-off / failure / fallback：`arXiv:2605.29001v1 — § exact heading: 8 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.29001v1 — official HTML sha256=d0e7ab93baa2dac7887cdb236f80c5996169d4fed3f8e888dd5fe36d3c7ac6c1; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-29001:start -->仅支持 exact-v1 披露机制及实验边界；不把“FormInv supplies the audit protocol (replicated on external benchmarks at 100% recall), SCR and per-theorem Cochran's Q as primary invariance measures evaluated on 9 models across 366-811 items (on Lean4-verified theorems), and FormInvSelector for regime-aware model selection.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-29001:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-29001:end -->

<!-- review:SF-2026-ARXIV-2605-29005:start -->
#### LoRe: Adaptive Interaction-Evaluation Routing with Per-Step Interaction Budgets for Iterative Graph Solvers

问题与 changed constraint：Diffusion-based neural solvers for combinatorial optimization repeatedly re-evaluate dense edge/factor interactions, making inference expensive in wall-clock time and often memory-bound at scale.

Mechanism 与 ownership：owner=`PLATFORM-EVALUATION-SYSTEM`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.29005v1 — § exact heading: 1 Introduction`；Evaluation=`arXiv:2605.29005v1 — § exact heading: 3.1 Formulation: Iterative Refinement as Operator Evaluation`。

Trade-off / failure / fallback：`arXiv:2605.29005v1 — § exact heading: 5 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.29005v1 — official HTML sha256=559be4e8e9ca49a19ad2512c93ccd1b2a3d8402c89267afee289a4eeaff9db6d; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-29005:start -->仅支持 exact-v1 披露机制及实验边界；不把“Diffusion-based neural solvers for combinatorial optimization repeatedly re-evaluate dense edge/factor interactions, making inference expensive in wall-clock time and often memory-bound at scale.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-29005:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-29005:end -->

<!-- review:SF-2026-ARXIV-2605-29054:start -->
#### Converted, Not Equivalent: Benchmarking Codebase Conversion via Observational Equivalence

问题与 changed constraint：We introduce T2J-Bench, a benchmark for codebase conversion that reformulates conversion as transfer under a fixed equivalence contract.

Mechanism 与 ownership：owner=`PLATFORM-EVALUATION-SYSTEM`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.29054v1 — § exact heading: 5.3 Self-Validation Systematically Overstates Progress`；Evaluation=`arXiv:2605.29054v1 — § exact heading: 4 Experiments`。

Trade-off / failure / fallback：`arXiv:2605.29054v1 — § exact heading: 5.1 A Cross-Agent Failure Taxonomy`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.29054v1 — official HTML sha256=f83a8a863b6eb67137c3c9aafb5efbf2773bf40a0fdb22358ff2e0fbf8945566; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-29054:start -->仅支持 exact-v1 披露机制及实验边界；不把“This suggests that failures stem more from contract-misaligned self-validation than from limited budget or backbone strength.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-29054:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-29054:end -->

<!-- review:SF-2026-ARXIV-2605-29068:start -->
#### Robust and Efficient Guardrails with Latent Reasoning

问题与 changed constraint：To address this challenge, we propose COLAGUARD, a guardrail model that transfers multi-step safety reasoning into a continuous latent space through a stage-wise training curriculum, enabling direct hidden-state propagation at inference.

Mechanism 与 ownership：owner=`PLATFORM-SECURITY`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.29068v1 — § exact heading: 1 Introduction`；Evaluation=`arXiv:2605.29068v1 — § exact heading: 4 Experiments`。

Trade-off / failure / fallback：`arXiv:2605.29068v1 — § exact heading: 5 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.29068v1 — official HTML sha256=aa57cbc30dac5822270c591d7ab737c1481861b157bec9e3849280b77ddb6943; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-29068:start -->仅支持 exact-v1 披露机制及实验边界；不把“Reasoning-based guardrails significantly outperform classification-only baselines, but they incur substantial query latency and token overhead that make them impractical for highthroughput deployment.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-29068:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-29068:end -->

<!-- review:SF-2026-ARXIV-2605-29074:start -->
#### Embodied3DBench: Benchmarking Low-Level Embodied Spatial Intelligence of Vision Language Models

问题与 changed constraint：We introduce Embodied3DBench, a robot-centric benchmark targeting low-level spatial intelligence in embodied 3D environments.

Mechanism 与 ownership：owner=`MULTIMODAL-EMBODIED-VLA`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.29074v1 — § exact heading: 1. Introduction`；Evaluation=`arXiv:2605.29074v1 — § exact heading: 3.3. Benchmark Construction`。

Trade-off / failure / fallback：`arXiv:2605.29074v1 — § exact heading: 5. Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.29074v1 — official HTML sha256=159ce42649abf09570b373306b1b776ec886382edbc1e4f6ed98b4e64438ba8f; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-29074:start -->仅支持 exact-v1 披露机制及实验边界；不把“We evaluate 13 state-of-the-art models, and the results show that while current models exhibit relatively strong high-level spatial reasoning, such as understanding object-to-object positional relations, they remain fragile in interaction-oriented perception, highlighting a significant lack of robust 3D-aware interaction priors.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-29074:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-29074:end -->

<!-- review:SF-2026-ARXIV-2605-29075:start -->
#### Knowledge Offloading: Decomposing LLMs into Sparse Backbones and Memory Modules

问题与 changed constraint：We propose \emph{knowledge offloading} (KOFF), a framework for decomposing a pretrained LLM into a sparse shared backbone and domain-specific memories.

Mechanism 与 ownership：owner=`AGENT-MEMORY`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.29075v1 — § exact heading: 3 Methodology`；Evaluation=`arXiv:2605.29075v1 — § exact heading: 4 Experiments`。

Trade-off / failure / fallback：`arXiv:2605.29075v1 — § exact heading: 5 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.29075v1 — official HTML sha256=cc51fcaee66f9e9767fe6ae83f3d8c792c4420ad4f471a094ffd75a6ec6cf8fa; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-29075:start -->仅支持 exact-v1 披露机制及实验边界；不把“Ablations show that LoRA and learned KV memories are complementary, and specialization analyses suggest that the learned decomposition is meaningful: language-specific neurons are preferentially removed while language-general neurons largely remain in the backbone.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-29075:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-29075:end -->

<!-- review:SF-2026-ARXIV-2605-29078:start -->
#### Bridging the Sim-to-Real Gap in Reinforcement Learning-Based Industrial Dispatching through Execution Semantics

问题与 changed constraint：The results show analytical benefits across all observation lag regimes, as undifferentiated execution failures are transformed into structured, typed outcomes with full attribution coverage.

Mechanism 与 ownership：owner=`AGENT-WORKFLOW`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.29078v1 — §III execution requirements; §IV snapshot isolation, policy-neutral contract and divergence record`；Evaluation=`arXiv:2605.29078v1 — §V empirical evaluation across lag regimes`。

Trade-off / failure / fallback：`arXiv:2605.29078v1 — §IV-D implementation constraints; §VI future-work boundary`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.29078v1 — official exact-v1 HTML read; immutable repository/checkpoint commit Not Disclosed; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-29078:start -->仅支持 exact-v1 披露机制及实验边界；不把“The results show analytical benefits across all observation lag regimes, as undifferentiated execution failures are transformed into structured, typed outcomes with full attribution coverage.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-29078:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-29078:end -->

<!-- review:SF-2026-ARXIV-2605-29082:start -->
#### The Importance of Out-of-Band Metadata for Safe Autonomous Agents: The Redpanda Agentic Data Plane

问题与 changed constraint：We present the Redpanda Agentic Data Plane (ADP), an architecture built around out-of-band metadata channels: infrastructure pathways that carry security context, policy signals, and audit trails deterministically, entirely outside the agent's read and write path and across heterogeneous infrastructure.

Mechanism 与 ownership：owner=`AGENT-PLATFORM`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.29082v1 — § exact heading: 4. System: The Agentic Data Plane`；Evaluation=`arXiv:2605.29082v1 — § exact heading: 1. Introduction`。

Trade-off / failure / fallback：`arXiv:2605.29082v1 — § exact heading: 7. Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.29082v1 — official HTML sha256=081c38dee7db84a2bf1efd9e8d9c06a15d35b76a905537a9e2fb49b3745d6d87; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-29082:start -->仅支持 exact-v1 披露机制及实验边界；不把“We demonstrate ADP with a multi-agent portfolio rebalancing system in which autonomous agents monitor markets, make trade decisions, and execute orders across isolated client accounts -- with per-client data scoping, trade approval thresholds, and tamper-proof audit trails all enforced by out-of-band channels the agents can neither see nor bypass.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-29082:end -->

Books Decision=`Integrate`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-29082:end -->

<!-- review:SF-2026-ARXIV-2605-29087:start -->
#### The Chain Holds, the Answer Folds: Trace-Answer Dissociation in Reasoning Models Under Adversarial Pressure

问题与 changed constraint：Reasoning models are evaluated on single-turn benchmarks but deployed in multi-turn dialogue, where users push back on correct answers.

Mechanism 与 ownership：owner=`PLATFORM-EVALUATION-SYSTEM`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.29087v1 — § exact heading: 3 The Latent-versus-Behavioral Framework`；Evaluation=`arXiv:2605.29087v1 — § exact heading: 4 Experimental Setup`。

Trade-off / failure / fallback：`arXiv:2605.29087v1 — § exact heading: 10 Discussion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.29087v1 — official HTML sha256=86ee2f058f79289bfbe5520d1df0b0a7e4e647c112d9eb14f7909d3e814255f9; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-29087:start -->仅支持 exact-v1 披露机制及实验边界；不把“Under sustained adversarial pressure we find a previously undocumented failure mode: the chain-of-thought stays factually correct from first turn to last while the emitted answer flips wrong.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-29087:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-29087:end -->

<!-- review:SF-2026-ARXIV-2605-29107:start -->
#### GEO-Bench: Benchmarking Ranking Manipulation in Generative Engine Optimization

问题与 changed constraint：We present GEO-Bench, a benchmark that evaluates GEO ranking-manipulation attacks under one protocol.

Mechanism 与 ownership：owner=`PLATFORM-SECURITY`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.29107v1 — § exact heading: 3 GEO-Bench: Benchmark Design`；Evaluation=`arXiv:2605.29107v1 — § exact heading: 3.3 Evaluation Metrics`。

Trade-off / failure / fallback：`arXiv:2605.29107v1 — § exact heading: 5 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.29107v1 — official HTML sha256=d6201036e694c5ae9088a4681e2fb3c28bba0aec07bcf0292995a841ff377130; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-29107:start -->仅支持 exact-v1 披露机制及实验边界；不把“By standardizing datasets, attack implementations, and metrics, GEO-Bench enables the first direct comparison across these attack paradigms and supports the development of detection methods.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-29107:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-29107:end -->

<!-- review:SF-2026-ARXIV-2605-29114:start -->
#### ReasonBreak: Probing Vulnerabilities in Reasoning-Enabled Vision-Language-Action Models for Autonomous Driving

问题与 changed constraint：We show that these models are highly vulnerable to realistic input perturbations, achieving up to 89% attack success rate (ASR) on reasoning and up to 72% on trajectory manipulation in closed-loop simulation, leading to increased collision rates and degraded safety metrics.

Mechanism 与 ownership：owner=`PLATFORM-SECURITY`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.29114v1 — § exact heading: 3 Threat Model`；Evaluation=`arXiv:2605.29114v1 — § exact heading: 5 Evaluation Protocol and Success Criteria`。

Trade-off / failure / fallback：`arXiv:2605.29114v1 — § exact heading: 8 Discussion and Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.29114v1 — official HTML sha256=5847a96dc6b379895ef66c5cde52b6481cec3e2864b1e460feee0735fb6a8ac8; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-29114:start -->仅支持 exact-v1 披露机制及实验边界；不把“We show that these models are highly vulnerable to realistic input perturbations, achieving up to 89% attack success rate (ASR) on reasoning and up to 72% on trajectory manipulation in closed-loop simulation, leading to increased collision rates and degraded safety metrics.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-29114:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-29114:end -->

<!-- review:SF-2026-ARXIV-2605-29115:start -->
#### unix-ctf: Procedural Environments for Unix-Competence Reinforcement Learning

问题与 changed constraint：We make the distinction operational and build a training surface for the Unix component.

Mechanism 与 ownership：owner=`TRAIN-GRPO`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.29115v1 — § exact heading: 1 Introduction`；Evaluation=`arXiv:2605.29115v1 — § exact heading: 5 Evaluation protocol`。

Trade-off / failure / fallback：`arXiv:2605.29115v1 — § exact heading: 7 Conclusion and limitations`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.29115v1 — official HTML sha256=61533d9472b107db9809f1be716cd7739d680592f79ad97fdeba6e052ccc4d81; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-29115:start -->仅支持 exact-v1 披露机制及实验边界；不把“Tasks are produced by an LLM-assisted synthesis pipeline that generates candidate hiding techniques, rewrites them into parameterized hide-and-find script pairs, and filters them with a bidirectional contract: the hide script must leave no plaintext trace of the flag on disk, and the find script must recover the flag in a fresh directory.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-29115:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-29115:end -->

<!-- review:SF-2026-ARXIV-2605-29119:start -->
#### PRO-CUA: Process-Reward Optimization for Computer Use Agents

问题与 changed constraint：In this work, we propose PRO-CUA, a process-reward optimization framework for training CUAs with iterative step-level reinforcement learning.

Mechanism 与 ownership：owner=`TRAIN-GRPO`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.29119v1 — § exact heading: 3.3 Process Reward Model Grading`；Evaluation=`arXiv:2605.29119v1 — § exact heading: 4 Experiments`。

Trade-off / failure / fallback：`arXiv:2605.29119v1 — § exact heading: 6 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.29119v1 — official HTML sha256=cc5c35fe725e92575fa9815caf18800be44be6f9e67621c5918dc55aacf8a0c9; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-29119:start -->仅支持 exact-v1 披露机制及实验边界；不把“Experiments on live web benchmarks demonstrate the effectiveness of PRO-CUA and the reliability of PRM-guided step-level training.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-29119:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-29119:end -->

<!-- review:SF-2026-ARXIV-2605-29121:start -->
#### A Minimal Bifurcation Model of Load Imbalance in a Softmax Mixture-of-Experts Router

问题与 changed constraint：We propose a minimal dynamical model of adaptive softmax routing for a two-expert Mixture-of-Experts (MoE) layer.

Mechanism 与 ownership：owner=`MODEL-MOE`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.29121v1 — § exact heading: 3.1 Two-Expert Model`；Evaluation=`arXiv:2605.29121v1 — § exact heading: 8 Numerical Experiments with Batch Routing`。

Trade-off / failure / fallback：`arXiv:2605.29121v1 — § exact heading: 9 Limitations`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.29121v1 — official HTML sha256=ab3f9a8273c3d33151de33c82a689df6b669452299c69ed0cc1d123e1a06babe; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-29121:start -->仅支持 exact-v1 披露机制及实验边界；不把“The results provide a controlled low-dimensional mechanism for abrupt transitions to load imbalance in adaptive MoE routers.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-29121:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-29121:end -->

<!-- review:SF-2026-ARXIV-2605-29123:start -->
#### The Confidence Shortcut: A Reasoning Failure Mode of Masked Diffusion Models

问题与 changed constraint：Masked diffusion language models (MDMs) uniquely support any-order generation, with confidence-based decoding currently serving as the de facto standard inference policy.

Mechanism 与 ownership：owner=`MULTIMODAL-GENERATIVE-PARADIGMS`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.29123v1 — § exact heading: 2.1 Masked Diffusion Models`；Evaluation=`arXiv:2605.29123v1 — § exact heading: 4 Experiments on Other Reasoning Tasks`。

Trade-off / failure / fallback：`arXiv:2605.29123v1 — § exact heading: 3.5 Discussion: What addition teaches us`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.29123v1 — official HTML sha256=e64903394774e58c756155d421de40b4a449290a81bcdd015cfa13c276a88c3f; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-29123:start -->仅支持 exact-v1 披露机制及实验边界；不把“In contrast, random masking -- despite its perceived inefficiency -- robustly preserves the reasoning-trajectory conditionals essential for solving the challenging tail.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-29123:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-29123:end -->

<!-- review:SF-2026-ARXIV-2605-29129:start -->
#### Governing Technical Debt in Agentic AI Systems

问题与 changed constraint：The distinction matters: debt is a stock of design and governance liability, while the tax is a flow of operating cost that arises because stochastic agents act through tools and workflows.

Mechanism 与 ownership：owner=`AGENT-PLATFORM`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.29129v1 — §2 debt/tax model; §3 debt accumulation`；Evaluation=`arXiv:2605.29129v1 — §4 operationalizing governance`。

Trade-off / failure / fallback：`arXiv:2605.29129v1 — §5 Conclusion; position paper without empirical validation or dedicated limitations`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.29129v1 — official exact-v1 HTML read; immutable repository/checkpoint commit Not Disclosed; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-29129:start -->仅支持 exact-v1 披露机制及实验边界；不把“We outline how managers can make both visible through lightweight dashboards and governance controls.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-29129:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-29129:end -->

<!-- review:SF-2026-ARXIV-2605-29135:start -->
#### Rotary GPU: Exploring Local Execution Paths for Large Mixture-of-Experts Models Under Limited GPU Memory

问题与 changed constraint：Large language models have achieved remarkable capabilities through scaling, and this paper does not challenge that.

Mechanism 与 ownership：owner=`INFER-GPU-MEMORY`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.29135v1 — §4 Rotary GPU concept; §6 setup`；Evaluation=`arXiv:2605.29135v1 — §8 results and failure analysis`。

Trade-off / failure / fallback：`arXiv:2605.29135v1 — §11 Limitations: one platform, ten-prompt smoke set and undisclosed implementation`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.29135v1 — official exact-v1 HTML read; immutable repository/checkpoint commit Not Disclosed; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-29135:start -->仅支持 exact-v1 披露机制及实验边界；不把“The results should be read as exploratory rather than definitive, but they suggest deployment accessibility deserves continued investigation as these models evolve.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-29135:end -->

Books Decision=`Integrate`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-29135:end -->

<!-- review:SF-2026-ARXIV-2605-29139:start -->
#### Anytime-Valid Federated Conformal RAG for LLM Swarms

问题与 changed constraint：Federated Conformal RAG (FC-RAG) provides distribution-free coverage for a bandwidth-limited swarm of weak language models, but only at a fixed horizon.

Mechanism 与 ownership：owner=`AGENT-RAG`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.29139v1 — § exact heading: 1 Introduction`；Evaluation=`arXiv:2605.29139v1 — § exact heading: 5 Experiments`。

Trade-off / failure / fallback：`arXiv:2605.29139v1 — § exact heading: 6 Discussion and outlook`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.29139v1 — official HTML sha256=a8ec74cd405ca490d4b9ef8c2163fa06058832b58674ce3390d164cb1abab1e3; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-29139:start -->仅支持 exact-v1 披露机制及实验边界；不把“Experiments on a GPT-2-small + MiniLM swarm across MMLU, DBpedia, and AG News verify the predicted alarm rate, detection delay, envelope coverage, and $14$-$57\%$ bandwidth savings; the alarm fires when and only when coverage genuinely breaks.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-29139:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-29139:end -->

<!-- review:SF-2026-ARXIV-2605-29156:start -->
#### RUBRIC-ARROW: Alternating Pointwise Rubric Reward Modeling for LLM Post-training in Non-verifiable Domains

问题与 changed constraint：We present RUBRIC-ARROW, an alternating framework that jointly trains a rubric generator and a rubric-conditioned judge, with its RL stage using only pairwise preference data.

Mechanism 与 ownership：owner=`TRAIN-RLHF`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.29156v1 — § exact heading: 4 Method`；Evaluation=`arXiv:2605.29156v1 — § exact heading: 5 Theoretical Analysis`。

Trade-off / failure / fallback：`arXiv:2605.29156v1 — § exact heading: 7 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.29156v1 — official HTML sha256=0276e263a7af8bd4b456d156d09b1c86044e9c77ddc9ab84a6ae06a066509473; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-29156:start -->仅支持 exact-v1 披露机制及实验边界；不把“Extensive experiments show that RUBRIC-ARROW achieves competitive reward-modeling accuracy and yields consistent gains for downstream policy post-training.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-29156:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-29156:end -->

<!-- review:SF-2026-ARXIV-2605-29178:start -->
#### The Best-Laid SCHEMEs: Coordinated Sabotage and Monitoring in Multi-Agent Systems

问题与 changed constraint：We introduce SCHEME, a benchmark of 17 task instances across 7 settings and 8 real open-source libraries, each pairing a legitimate software-engineering task with a covert side task.

Mechanism 与 ownership：owner=`PLATFORM-SECURITY`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.29178v1 — § exact heading: 3.1 Coordinated sabotage is already practical for frontier models`；Evaluation=`arXiv:2605.29178v1 — § exact heading: 3 Results`。

Trade-off / failure / fallback：`arXiv:2605.29178v1 — § exact heading: 3.3 Recovery, not failure incidence, drives the model gap`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.29178v1 — official HTML sha256=c64659adcde64aa6748ea9f8a3eee8358c0782dcf23a8c50fc40826a7df132e9; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-29178:start -->仅支持 exact-v1 披露机制及实验边界；不把“Evaluating with GPT 5.1 Codex and Gemini 3.1 Pro, we find coordinated sabotage is already practical, with Gemini completing the covert objective while succeeding on the legitimate task in 84\% of samples and Codex in 46\%.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-29178:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-29178:end -->

<!-- review:SF-2026-ARXIV-2605-29183:start -->
#### TIMEGATE: Sustainable Time-Boxed Promotion Gates for Continual ML Adaptation Under Resource Constraints

问题与 changed constraint：We introduce TIMEGATE, a policy layer managing adaptation by budgeting time, labeling, training, and evaluation.

Mechanism 与 ownership：owner=`PLATFORM-PRODUCTION`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.29183v1 — § exact heading: 2 The TimeGate Model`；Evaluation=`arXiv:2605.29183v1 — § exact heading: 3 Experiments`。

Trade-off / failure / fallback：`arXiv:2605.29183v1 — § exact heading: 6 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.29183v1 — official HTML sha256=a3923b577e9eb61591e3fc195930456c0d3c5d06bdf8deaa0945c9384d3c4a94; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-29183:start -->仅支持 exact-v1 披露机制及实验边界；不把“We validate: (i) labeling outperforms training by 2.3x on Adult tabular; (ii) it transfers to LLaMA-3.1-8B + QLoRA on SST-2 (accuracy 0.80 to 0.96; M =1 in 35/36 runs); (iii) M is informative, 28-cell sensitivity shows M drops to 0.81 at tight thresholds; (iv) 100-cycle simulation achieves 66% evaluation-compute savings with no silent mis-promotions; (v) 10%-slice evaluation on LLaMA uses 89% less wall-clock and ener”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-29183:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-29183:end -->

<!-- review:SF-2026-ARXIV-2605-29192:start -->
#### ReasonOps: Operator Segmentation for LLM Reasoning Traces

问题与 changed constraint：To remedy this, we develop ReasonOps, an unsupervised, expressive method for annotating chain-of-thought traces, providing succinct universal operators.

Mechanism 与 ownership：owner=`PLATFORM-TRACE`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.29192v1 — § exact heading: 3 Methods`；Evaluation=`arXiv:2605.29192v1 — § exact heading: 5 Analysis of operator distributions`。

Trade-off / failure / fallback：`arXiv:2605.29192v1 — § exact heading: 7 Discussion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.29192v1 — official HTML sha256=e420a9f8f6e5d0391e17194107e7b985ed8142555896991b2d2ec2b1ca2d68c9; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-29192:start -->仅支持 exact-v1 披露机制及实验边界；不把“The ReasonOps pipeline is unsupervised and annotation-free, enabling deep insights into LLM reasoning traces as well as strong downstream results on model identification and correctness prediction.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-29192:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-29192:end -->

<!-- review:SF-2026-ARXIV-2605-29209:start -->
#### The WER Trap: Shattering the Illusion of Unified Tokens in Speech Language Models

问题与 changed constraint：To overcome this, we develop a dynamic compression tokenizer that intelligently aligns representations with semantic boundaries, achieving ultra-low frame rates with exceptionally low WER.

Mechanism 与 ownership：owner=`MULTIMODAL-REPRESENTATION`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.29209v1 — § exact heading: 3 The Methodological Bottleneck: Fixed-Stride Compression`；Evaluation=`arXiv:2605.29209v1 — § exact heading: 5 Evaluation Framework: The Dual-Probing Protocol`。

Trade-off / failure / fallback：`arXiv:2605.29209v1 — § exact heading: 7 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.29209v1 — official HTML sha256=c85bde6618b205f1951294db9ece991e3cd1320c1319aaf4196c9000944fe070; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-29209:start -->仅支持 exact-v1 披露机制及实验边界；不把“Our findings demonstrate that semantic categorization rewarded by low WER is inherently orthogonal to the continuous phonetic trajectories required for synthesis, shattering the illusion of the unified token and advocating for explicitly decoupled speech representations.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-29209:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-29209:end -->

<!-- review:SF-2026-ARXIV-2606-07586:start -->
#### From Human Guidance to Autonomy: Agent Skill System for End-to-End LLM Deployment on Spatial NPUs

问题与 changed constraint：We present a two-stage methodology, instantiated on the AMD XDNA 2 NPU, that progresses from human-guided development to agent autonomy.

Mechanism 与 ownership：owner=`AGENT-PLATFORM`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2606.07586v1 — § exact heading: IV Skill System`；Evaluation=`arXiv:2606.07586v1 — § exact heading: V Evaluation`。

Trade-off / failure / fallback：`arXiv:2606.07586v1 — § exact heading: VI Conclusion and Future Work`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2606.07586v1 — official HTML sha256=5b2c398ccc30fe40586127fe9bea23adf82bdbb41f84275ecd3a1164b3cfc8ce; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2606-07586:start -->仅支持 exact-v1 披露机制及实验边界；不把“Three of the eight match or exceed the sustained performance of our Llama-3.2-1B reference deployment, suggesting that the resulting implementations can be competitive without additional model-specific human engineering.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2606-07586:end -->

Books Decision=`Integrate`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2606-07586:end -->

<!-- review:SF-2026-ARXIV-2606-26120:start -->
#### Dynamic-dLLM: Dynamic Cache-Budget and Adaptive Parallel Decoding for Training-Free Acceleration of Diffusion LLM

问题与 changed constraint：We propose Dynamic-dLLM, a training-free framework that enhances dLLM inference efficiency through two components: Dynamic Cache Updating (DCU), which adaptively allocates cache-update budgets based on layer-wise token dynamics, and Adaptive Parallel Decoding (APD), which dynamically calibrates decoding thresholds to balance generation quality and efficiency.

Mechanism 与 ownership：owner=`INFER-CONTINUOUS-BATCHING`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2606.26120v1 — § exact heading: 3 Method`；Evaluation=`arXiv:2606.26120v1 — § exact heading: 4 Experiment`。

Trade-off / failure / fallback：`arXiv:2606.26120v1 — § exact heading: 1 Introduction`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2606.26120v1 — official HTML sha256=f091d72f6100d2e4bf803a6276472099be05dfd56b099d0462ed38c04969ccd0; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2606-26120:start -->仅支持 exact-v1 披露机制及实验边界；不把“Extensive experiments on models like LLaDA-8B-Instruct, LLaDA-1.5, and Dream-v0-7B-Instruct across benchmarks such as MMLU, GSM8K, and HumanEval demonstrate that Dynamic-dLLM significantly improves inference speed.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2606-26120:end -->

Books Decision=`Integrate`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2606-26120:end -->

<!-- review:SF-2026-ARXIV-2606-26122:start -->
#### DocArena: Turning Raw Documents into Controllable Training Environments for Document Search Agents

问题与 changed constraint：The tuples serve as the training environment, and whose properties directly shape what search strategies and generalization abilities the agent can develop.

Mechanism 与 ownership：owner=`TRAIN-DATA`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2606.26122v1 — § exact heading: 3 Method`；Evaluation=`arXiv:2606.26122v1 — § exact heading: 4 Experiment`。

Trade-off / failure / fallback：`arXiv:2606.26122v1 — § exact heading: 5 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2606.26122v1 — official HTML sha256=137890ea8c0dcd2a962b9c3902a8263fbac0adaf1706d1a6e4aaafc61fdeb4b6; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2606-26122:start -->仅支持 exact-v1 披露机制及实验边界；不把“Under a unified evaluation framework where only the policy model differs, experiments on six multimodal document scenarios and seven text-based QA benchmarks show that agents trained on DocArena data achieve the best performance on both retrieval accuracy and QA quality.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2606-26122:end -->

Books Decision=`Integrate`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2606-26122:end -->

## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

本报告不登记可外推 benchmark claim；数值只属于 exact-v1 的披露 workload，未披露字段保持 Not Disclosed。

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-27820 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-27820 |
| SF-2026-ARXIV-2605-27825 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-27825 |
| SF-2026-ARXIV-2605-27850 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-27850 |
| SF-2026-ARXIV-2605-27879 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-27879 |
| SF-2026-ARXIV-2605-27881 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-27881 |
| SF-2026-ARXIV-2605-27898 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-27898 |
| SF-2026-ARXIV-2605-27899 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-27899 |
| SF-2026-ARXIV-2605-27901 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-27901 |
| SF-2026-ARXIV-2605-27918 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-27918 |
| SF-2026-ARXIV-2605-27922 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-27922 |
| SF-2026-ARXIV-2605-27947 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-27947 |
| SF-2026-ARXIV-2605-27954 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-27954 |
| SF-2026-ARXIV-2605-27957 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-27957 |
| SF-2026-ARXIV-2605-27963 | score_7_9 | selected | DA-TOPOLOGY-COLLECTIVE-CO-DESIGN | — | cross-layer state/control ownership change | analysis:DA-TOPOLOGY-COLLECTIVE-CO-DESIGN |
| SF-2026-ARXIV-2605-27980 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-27980 |
| SF-2026-ARXIV-2605-27995 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-27995 |
| SF-2026-ARXIV-2605-28000 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-28000 |
| SF-2026-ARXIV-2605-28009 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-28009 |
| SF-2026-ARXIV-2605-28017 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-28017 |
| SF-2026-ARXIV-2605-28044 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-28044 |
| SF-2026-ARXIV-2605-28046 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-28046 |
| SF-2026-ARXIV-2605-28053 | score_7_9; forced_review; potential_books_delta | selected | DA-REQUEST-OWNED-TTT-STATE | — | cross-layer state/control ownership change | analysis:DA-REQUEST-OWNED-TTT-STATE |
| SF-2026-ARXIV-2605-28071 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-28071 |
| SF-2026-ARXIV-2605-28074 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-28074 |
| SF-2026-ARXIV-2605-28083 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-28083 |
| SF-2026-ARXIV-2605-28095 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-28095 |
| SF-2026-ARXIV-2605-28097 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-28097 |
| SF-2026-ARXIV-2605-28108 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-28108 |
| SF-2026-ARXIV-2605-28112 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-28112 |
| SF-2026-ARXIV-2605-28116 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-28116 |
| SF-2026-ARXIV-2605-28122 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-28122 |
| SF-2026-ARXIV-2605-28158 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-28158 |
| SF-2026-ARXIV-2605-28201 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-28201 |
| SF-2026-ARXIV-2605-28213 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-28213 |
| SF-2026-ARXIV-2605-28214 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-28214 |
| SF-2026-ARXIV-2605-28224 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-28224 |
| SF-2026-ARXIV-2605-28282 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-28282 |
| SF-2026-ARXIV-2605-28302 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-28302 |
| SF-2026-ARXIV-2605-28354 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-28354 |
| SF-2026-ARXIV-2605-28371 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-28371 |
| SF-2026-ARXIV-2605-28384 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-28384 |
| SF-2026-ARXIV-2605-28390 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-28390 |
| SF-2026-ARXIV-2605-28424 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-28424 |
| SF-2026-ARXIV-2605-28433 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-28433 |
| SF-2026-ARXIV-2605-28467 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-28467 |
| SF-2026-ARXIV-2605-28480 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-28480 |
| SF-2026-ARXIV-2605-28508 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-28508 |
| SF-2026-ARXIV-2605-28510 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-28510 |
| SF-2026-ARXIV-2605-28544 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-28544 |
| SF-2026-ARXIV-2605-28561 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-28561 |
| SF-2026-ARXIV-2605-28565 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-28565 |
| SF-2026-ARXIV-2605-28573 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-28573 |
| SF-2026-ARXIV-2605-28617 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-28617 |
| SF-2026-ARXIV-2605-28632 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-28632 |
| SF-2026-ARXIV-2605-28634 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-28634 |
| SF-2026-ARXIV-2605-28640 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-28640 |
| SF-2026-ARXIV-2605-28646 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-28646 |
| SF-2026-ARXIV-2605-28678 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-28678 |
| SF-2026-ARXIV-2605-28691 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-28691 |
| SF-2026-ARXIV-2605-28699 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-28699 |
| SF-2026-ARXIV-2605-28704 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-28704 |
| SF-2026-ARXIV-2605-28721 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-28721 |
| SF-2026-ARXIV-2605-28726 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-28726 |
| SF-2026-ARXIV-2605-28732 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-28732 |
| SF-2026-ARXIV-2605-28742 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-28742 |
| SF-2026-ARXIV-2605-28751 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-28751 |
| SF-2026-ARXIV-2605-28760 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-28760 |
| SF-2026-ARXIV-2605-28764 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-28764 |
| SF-2026-ARXIV-2605-28773 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-28773 |
| SF-2026-ARXIV-2605-28774 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-28774 |
| SF-2026-ARXIV-2605-28778 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-28778 |
| SF-2026-ARXIV-2605-28787 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-28787 |
| SF-2026-ARXIV-2605-28803 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-28803 |
| SF-2026-ARXIV-2605-28805 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-28805 |
| SF-2026-ARXIV-2605-28807 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-28807 |
| SF-2026-ARXIV-2605-28819 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-28819 |
| SF-2026-ARXIV-2605-28889 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-28889 |
| SF-2026-ARXIV-2605-28890 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-28890 |
| SF-2026-ARXIV-2605-28893 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-28893 |
| SF-2026-ARXIV-2605-28897 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-28897 |
| SF-2026-ARXIV-2605-28914 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-28914 |
| SF-2026-ARXIV-2605-28918 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-28918 |
| SF-2026-ARXIV-2605-28920 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-28920 |
| SF-2026-ARXIV-2605-28969 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-28969 |
| SF-2026-ARXIV-2605-28991 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-28991 |
| SF-2026-ARXIV-2605-28999 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-28999 |
| SF-2026-ARXIV-2605-29001 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-29001 |
| SF-2026-ARXIV-2605-29005 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-29005 |
| SF-2026-ARXIV-2605-29054 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-29054 |
| SF-2026-ARXIV-2605-29068 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-29068 |
| SF-2026-ARXIV-2605-29074 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-29074 |
| SF-2026-ARXIV-2605-29075 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-29075 |
| SF-2026-ARXIV-2605-29078 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-29078 |
| SF-2026-ARXIV-2605-29082 | score_7_9; forced_review; potential_books_delta | selected | DA-OUT-OF-BAND-AGENT-DATA-PLANE | — | cross-layer state/control ownership change | analysis:DA-OUT-OF-BAND-AGENT-DATA-PLANE |
| SF-2026-ARXIV-2605-29087 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-29087 |
| SF-2026-ARXIV-2605-29107 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-29107 |
| SF-2026-ARXIV-2605-29114 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-29114 |
| SF-2026-ARXIV-2605-29115 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-29115 |
| SF-2026-ARXIV-2605-29119 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-29119 |
| SF-2026-ARXIV-2605-29121 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-29121 |
| SF-2026-ARXIV-2605-29123 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-29123 |
| SF-2026-ARXIV-2605-29129 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-29129 |
| SF-2026-ARXIV-2605-29135 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-29135 |
| SF-2026-ARXIV-2605-29139 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-29139 |
| SF-2026-ARXIV-2605-29156 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-29156 |
| SF-2026-ARXIV-2605-29178 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-29178 |
| SF-2026-ARXIV-2605-29183 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-29183 |
| SF-2026-ARXIV-2605-29192 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-29192 |
| SF-2026-ARXIV-2605-29209 | score_7_9 | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2605-29209 |
| SF-2026-ARXIV-2606-07586 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2606-07586 |
| SF-2026-ARXIV-2606-26120 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2606-26120 |
| SF-2026-ARXIV-2606-26122 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 review complete; less cross-cutting than selected units | analysis-decision:SF-2026-ARXIV-2606-26122 |

<!-- analysis:DA-TOPOLOGY-COLLECTIVE-CO-DESIGN:start -->
### Network synthesis：从事后放置推进到拓扑、routing 与 collective 共同设计

固定拓扑再选择 collective 在网络均匀、failure-free 且 workload 稳定时最透明。大规模训练把并行维度、拥塞与故障域耦合后，需要用 workload communication graph 联合决定 topology、routing 与 collective schedule。收益是减少热链路与尾部阻塞，代价是搜索空间、建模误差和配置漂移；模拟最优不拥有生产 promotion authority，仍需小规模 replay、canary 与 fallback topology。
<!-- analysis:DA-TOPOLOGY-COLLECTIVE-CO-DESIGN:end -->

<!-- analysis:DA-REQUEST-OWNED-TTT-STATE:start -->
### Serving state：从只读权重推进到 request-owned test-time update

传统 continuous batching 假设请求只追加 KV，模型权重在 batch 间共享。TTT 让每个请求持有可变参数状态，scheduler 必须把 update、read、merge、eviction 和 rollback 纳入 iteration contract。它换来在线适应，却破坏简单 batching、扩大显存和隔离面，并新增 stale update 与跨请求污染；短请求或收益不足时仍应回退 immutable weights + KV。
<!-- analysis:DA-REQUEST-OWNED-TTT-STATE:end -->

<!-- analysis:DA-OUT-OF-BAND-AGENT-DATA-PLANE:start -->
### Agent data plane：从内容内提示推进到不可被 payload 覆盖的 out-of-band metadata

把 policy、provenance 与 authority 混进自然语言 payload 在单应用、低对抗环境下简单，但 agent 跨工具和消息系统流转后，内容可以伪造这些控制字段。out-of-band metadata 将 principal、schema、taint 与 policy hint 交给独立 data plane，并在 effect-time authorizer 汇合。收益是隔离控制信息，代价是 producer/bridge 都成为可信组件；metadata 丢失或不兼容时必须 quarantine、降权或人工授权。
<!-- analysis:DA-OUT-OF-BAND-AGENT-DATA-PLANE:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-27820:start -->SF-2026-ARXIV-2605-27820 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-27820:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-27825:start -->SF-2026-ARXIV-2605-27825 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-27825:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-27850:start -->SF-2026-ARXIV-2605-27850 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-27850:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-27879:start -->SF-2026-ARXIV-2605-27879 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-27879:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-27881:start -->SF-2026-ARXIV-2605-27881 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-27881:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-27898:start -->SF-2026-ARXIV-2605-27898 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-27898:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-27899:start -->SF-2026-ARXIV-2605-27899 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-27899:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-27901:start -->SF-2026-ARXIV-2605-27901 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-27901:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-27918:start -->SF-2026-ARXIV-2605-27918 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-27918:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-27922:start -->SF-2026-ARXIV-2605-27922 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-27922:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-27947:start -->SF-2026-ARXIV-2605-27947 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-27947:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-27954:start -->SF-2026-ARXIV-2605-27954 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-27954:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-27957:start -->SF-2026-ARXIV-2605-27957 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-27957:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-27980:start -->SF-2026-ARXIV-2605-27980 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-27980:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-27995:start -->SF-2026-ARXIV-2605-27995 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-27995:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-28000:start -->SF-2026-ARXIV-2605-28000 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-28000:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-28009:start -->SF-2026-ARXIV-2605-28009 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-28009:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-28017:start -->SF-2026-ARXIV-2605-28017 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-28017:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-28044:start -->SF-2026-ARXIV-2605-28044 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-28044:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-28046:start -->SF-2026-ARXIV-2605-28046 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-28046:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-28071:start -->SF-2026-ARXIV-2605-28071 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-28071:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-28074:start -->SF-2026-ARXIV-2605-28074 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-28074:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-28083:start -->SF-2026-ARXIV-2605-28083 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-28083:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-28095:start -->SF-2026-ARXIV-2605-28095 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-28095:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-28097:start -->SF-2026-ARXIV-2605-28097 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-28097:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-28108:start -->SF-2026-ARXIV-2605-28108 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-28108:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-28112:start -->SF-2026-ARXIV-2605-28112 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-28112:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-28116:start -->SF-2026-ARXIV-2605-28116 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-28116:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-28122:start -->SF-2026-ARXIV-2605-28122 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-28122:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-28158:start -->SF-2026-ARXIV-2605-28158 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-28158:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-28201:start -->SF-2026-ARXIV-2605-28201 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-28201:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-28213:start -->SF-2026-ARXIV-2605-28213 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-28213:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-28214:start -->SF-2026-ARXIV-2605-28214 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-28214:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-28224:start -->SF-2026-ARXIV-2605-28224 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-28224:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-28282:start -->SF-2026-ARXIV-2605-28282 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-28282:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-28302:start -->SF-2026-ARXIV-2605-28302 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-28302:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-28354:start -->SF-2026-ARXIV-2605-28354 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-28354:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-28371:start -->SF-2026-ARXIV-2605-28371 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-28371:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-28384:start -->SF-2026-ARXIV-2605-28384 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-28384:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-28390:start -->SF-2026-ARXIV-2605-28390 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-28390:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-28424:start -->SF-2026-ARXIV-2605-28424 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-28424:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-28433:start -->SF-2026-ARXIV-2605-28433 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-28433:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-28467:start -->SF-2026-ARXIV-2605-28467 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-28467:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-28480:start -->SF-2026-ARXIV-2605-28480 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-28480:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-28508:start -->SF-2026-ARXIV-2605-28508 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-28508:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-28510:start -->SF-2026-ARXIV-2605-28510 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-28510:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-28544:start -->SF-2026-ARXIV-2605-28544 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-28544:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-28561:start -->SF-2026-ARXIV-2605-28561 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-28561:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-28565:start -->SF-2026-ARXIV-2605-28565 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-28565:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-28573:start -->SF-2026-ARXIV-2605-28573 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-28573:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-28617:start -->SF-2026-ARXIV-2605-28617 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-28617:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-28632:start -->SF-2026-ARXIV-2605-28632 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-28632:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-28634:start -->SF-2026-ARXIV-2605-28634 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-28634:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-28640:start -->SF-2026-ARXIV-2605-28640 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-28640:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-28646:start -->SF-2026-ARXIV-2605-28646 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-28646:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-28678:start -->SF-2026-ARXIV-2605-28678 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-28678:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-28691:start -->SF-2026-ARXIV-2605-28691 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-28691:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-28699:start -->SF-2026-ARXIV-2605-28699 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-28699:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-28704:start -->SF-2026-ARXIV-2605-28704 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-28704:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-28721:start -->SF-2026-ARXIV-2605-28721 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-28721:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-28726:start -->SF-2026-ARXIV-2605-28726 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-28726:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-28732:start -->SF-2026-ARXIV-2605-28732 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-28732:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-28742:start -->SF-2026-ARXIV-2605-28742 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-28742:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-28751:start -->SF-2026-ARXIV-2605-28751 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-28751:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-28760:start -->SF-2026-ARXIV-2605-28760 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-28760:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-28764:start -->SF-2026-ARXIV-2605-28764 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-28764:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-28773:start -->SF-2026-ARXIV-2605-28773 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-28773:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-28774:start -->SF-2026-ARXIV-2605-28774 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-28774:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-28778:start -->SF-2026-ARXIV-2605-28778 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-28778:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-28787:start -->SF-2026-ARXIV-2605-28787 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-28787:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-28803:start -->SF-2026-ARXIV-2605-28803 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-28803:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-28805:start -->SF-2026-ARXIV-2605-28805 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-28805:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-28807:start -->SF-2026-ARXIV-2605-28807 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-28807:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-28819:start -->SF-2026-ARXIV-2605-28819 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-28819:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-28889:start -->SF-2026-ARXIV-2605-28889 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-28889:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-28890:start -->SF-2026-ARXIV-2605-28890 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-28890:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-28893:start -->SF-2026-ARXIV-2605-28893 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-28893:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-28897:start -->SF-2026-ARXIV-2605-28897 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-28897:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-28914:start -->SF-2026-ARXIV-2605-28914 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-28914:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-28918:start -->SF-2026-ARXIV-2605-28918 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-28918:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-28920:start -->SF-2026-ARXIV-2605-28920 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-28920:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-28969:start -->SF-2026-ARXIV-2605-28969 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-28969:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-28991:start -->SF-2026-ARXIV-2605-28991 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-28991:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-28999:start -->SF-2026-ARXIV-2605-28999 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-28999:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-29001:start -->SF-2026-ARXIV-2605-29001 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-29001:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-29005:start -->SF-2026-ARXIV-2605-29005 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-29005:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-29054:start -->SF-2026-ARXIV-2605-29054 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-29054:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-29068:start -->SF-2026-ARXIV-2605-29068 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-29068:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-29074:start -->SF-2026-ARXIV-2605-29074 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-29074:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-29075:start -->SF-2026-ARXIV-2605-29075 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-29075:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-29078:start -->SF-2026-ARXIV-2605-29078 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-29078:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-29087:start -->SF-2026-ARXIV-2605-29087 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-29087:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-29107:start -->SF-2026-ARXIV-2605-29107 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-29107:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-29114:start -->SF-2026-ARXIV-2605-29114 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-29114:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-29115:start -->SF-2026-ARXIV-2605-29115 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-29115:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-29119:start -->SF-2026-ARXIV-2605-29119 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-29119:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-29121:start -->SF-2026-ARXIV-2605-29121 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-29121:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-29123:start -->SF-2026-ARXIV-2605-29123 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-29123:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-29129:start -->SF-2026-ARXIV-2605-29129 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-29129:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-29135:start -->SF-2026-ARXIV-2605-29135 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-29135:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-29139:start -->SF-2026-ARXIV-2605-29139 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-29139:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-29156:start -->SF-2026-ARXIV-2605-29156 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-29156:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-29178:start -->SF-2026-ARXIV-2605-29178 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-29178:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-29183:start -->SF-2026-ARXIV-2605-29183 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-29183:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-29192:start -->SF-2026-ARXIV-2605-29192 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-29192:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-29209:start -->SF-2026-ARXIV-2605-29209 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-29209:end -->
<!-- analysis-decision:SF-2026-ARXIV-2606-07586:start -->SF-2026-ARXIV-2606-07586 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2606-07586:end -->
<!-- analysis-decision:SF-2026-ARXIV-2606-26120:start -->SF-2026-ARXIV-2606-26120 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2606-26120:end -->
<!-- analysis-decision:SF-2026-ARXIV-2606-26122:start -->SF-2026-ARXIV-2606-26122 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2606-26122:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-27820 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-27820 | delta:SF-2026-ARXIV-2605-27820 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27820 |
| SF-2026-ARXIV-2605-27825 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-27825 | delta:SF-2026-ARXIV-2605-27825 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2605-27825 |
| SF-2026-ARXIV-2605-27850 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#chapter-82 | books/part-07-agent/81-workflow.md#chapter-81;books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-27850 | delta:SF-2026-ARXIV-2605-27850 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27850 |
| SF-2026-ARXIV-2605-27879 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-27879 | delta:SF-2026-ARXIV-2605-27879 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27879 |
| SF-2026-ARXIV-2605-27881 | TRAIN-DATA | books/part-04-training-system/27-data.md#chapter-27 | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26;books/part-04-training-system/28-pretraining.md#chapter-28 | existing:SF-2026-ARXIV-2605-27881 | delta:SF-2026-ARXIV-2605-27881 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27881 |
| SF-2026-ARXIV-2605-27898 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-27898 | delta:SF-2026-ARXIV-2605-27898 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27898 |
| SF-2026-ARXIV-2605-27899 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#chapter-33 | books/part-04-training-system/32-ppo.md#chapter-32;books/part-04-training-system/34-dpo.md#chapter-34 | existing:SF-2026-ARXIV-2605-27899 | delta:SF-2026-ARXIV-2605-27899 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27899 |
| SF-2026-ARXIV-2605-27901 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-27901 | delta:SF-2026-ARXIV-2605-27901 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27901 |
| SF-2026-ARXIV-2605-27918 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#chapter-36 | books/part-04-training-system/35-checkpoint.md#chapter-35;books/part-04-training-system/37-tensor-parallel.md#chapter-37 | existing:SF-2026-ARXIV-2605-27918 | delta:SF-2026-ARXIV-2605-27918 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27918 |
| SF-2026-ARXIV-2605-27922 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-27922 | delta:SF-2026-ARXIV-2605-27922 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27922 |
| SF-2026-ARXIV-2605-27947 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#chapter-56 | books/part-05-inference-system/55-pd-disaggregation.md#chapter-55;books/part-06-ai-infrastructure/57-what-is-ai-platform.md#chapter-57 | existing:SF-2026-ARXIV-2605-27947 | delta:SF-2026-ARXIV-2605-27947 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27947 |
| SF-2026-ARXIV-2605-27954 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#chapter-33 | books/part-04-training-system/32-ppo.md#chapter-32;books/part-04-training-system/34-dpo.md#chapter-34 | existing:SF-2026-ARXIV-2605-27954 | delta:SF-2026-ARXIV-2605-27954 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27954 |
| SF-2026-ARXIV-2605-27957 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-27957 | delta:SF-2026-ARXIV-2605-27957 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27957 |
| SF-2026-ARXIV-2605-27963 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#chapter-36 | books/part-04-training-system/35-checkpoint.md#chapter-35;books/part-04-training-system/37-tensor-parallel.md#chapter-37 | existing:SF-2026-ARXIV-2605-27963 | delta:SF-2026-ARXIV-2605-27963 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27963 |
| SF-2026-ARXIV-2605-27980 | MODEL-POSITION-ENCODING | books/part-02-model/13-position-encoding.md#chapter-13 | books/part-02-model/12-embedding.md#chapter-12;books/part-02-model/14-self-attention.md#chapter-14 | existing:SF-2026-ARXIV-2605-27980 | delta:SF-2026-ARXIV-2605-27980 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27980 |
| SF-2026-ARXIV-2605-27995 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-27995 | delta:SF-2026-ARXIV-2605-27995 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27995 |
| SF-2026-ARXIV-2605-28000 | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#chapter-78 | books/part-07-agent/77-memory.md#chapter-77;books/part-07-agent/79-planning.md#chapter-79 | existing:SF-2026-ARXIV-2605-28000 | delta:SF-2026-ARXIV-2605-28000 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28000 |
| SF-2026-ARXIV-2605-28009 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76;books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-28009 | delta:SF-2026-ARXIV-2605-28009 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28009 |
| SF-2026-ARXIV-2605-28017 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-28017 | delta:SF-2026-ARXIV-2605-28017 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28017 |
| SF-2026-ARXIV-2605-28044 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-28044 | delta:SF-2026-ARXIV-2605-28044 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28044 |
| SF-2026-ARXIV-2605-28046 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76;books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-28046 | delta:SF-2026-ARXIV-2605-28046 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28046 |
| SF-2026-ARXIV-2605-28053 | INFER-CONTINUOUS-BATCHING | books/part-05-inference-system/46-continuous-batching.md#chapter-46 | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#chapter-45;books/part-05-inference-system/47-pagedattention.md#chapter-47 | existing:SF-2026-ARXIV-2605-28053 | delta:SF-2026-ARXIV-2605-28053 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2605-28053 |
| SF-2026-ARXIV-2605-28071 | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#chapter-78 | books/part-07-agent/77-memory.md#chapter-77;books/part-07-agent/79-planning.md#chapter-79 | existing:SF-2026-ARXIV-2605-28071 | delta:SF-2026-ARXIV-2605-28071 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28071 |
| SF-2026-ARXIV-2605-28074 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-28074 | delta:SF-2026-ARXIV-2605-28074 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28074 |
| SF-2026-ARXIV-2605-28083 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-28083 | delta:SF-2026-ARXIV-2605-28083 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28083 |
| SF-2026-ARXIV-2605-28095 | INFER-GPU-MEMORY | books/part-05-inference-system/54-gpu-memory.md#chapter-54 | books/part-05-inference-system/53-kserve-llm.md#chapter-53;books/part-05-inference-system/55-pd-disaggregation.md#chapter-55 | existing:SF-2026-ARXIV-2605-28095 | delta:SF-2026-ARXIV-2605-28095 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2605-28095 |
| SF-2026-ARXIV-2605-28097 | PLATFORM-PRODUCTION | books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | books/part-06-ai-infrastructure/72-security.md#chapter-72;books/part-07-agent/74-prompt.md#chapter-74 | existing:SF-2026-ARXIV-2605-28097 | delta:SF-2026-ARXIV-2605-28097 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28097 |
| SF-2026-ARXIV-2605-28108 | AGENT-PLANNING | books/part-07-agent/79-planning.md#chapter-79 | books/part-07-agent/78-tool-calling.md#chapter-78;books/part-07-agent/80-reflection.md#chapter-80 | existing:SF-2026-ARXIV-2605-28108 | delta:SF-2026-ARXIV-2605-28108 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28108 |
| SF-2026-ARXIV-2605-28112 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-28112 | delta:SF-2026-ARXIV-2605-28112 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28112 |
| SF-2026-ARXIV-2605-28116 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-28116 | delta:SF-2026-ARXIV-2605-28116 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28116 |
| SF-2026-ARXIV-2605-28122 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-28122 | delta:SF-2026-ARXIV-2605-28122 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28122 |
| SF-2026-ARXIV-2605-28158 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-28158 | delta:SF-2026-ARXIV-2605-28158 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28158 |
| SF-2026-ARXIV-2605-28201 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-28201 | delta:SF-2026-ARXIV-2605-28201 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2605-28201 |
| SF-2026-ARXIV-2605-28213 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-28213 | delta:SF-2026-ARXIV-2605-28213 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28213 |
| SF-2026-ARXIV-2605-28214 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-28214 | delta:SF-2026-ARXIV-2605-28214 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28214 |
| SF-2026-ARXIV-2605-28224 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76;books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-28224 | delta:SF-2026-ARXIV-2605-28224 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28224 |
| SF-2026-ARXIV-2605-28282 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#chapter-81 | books/part-07-agent/80-reflection.md#chapter-80;books/part-07-agent/82-multi-agent.md#chapter-82 | existing:SF-2026-ARXIV-2605-28282 | delta:SF-2026-ARXIV-2605-28282 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28282 |
| SF-2026-ARXIV-2605-28302 | INFER-PD-DISAGGREGATION | books/part-05-inference-system/55-pd-disaggregation.md#chapter-55 | books/part-05-inference-system/54-gpu-memory.md#chapter-54;books/part-05-inference-system/56-inference-scheduling.md#chapter-56 | existing:SF-2026-ARXIV-2605-28302 | delta:SF-2026-ARXIV-2605-28302 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28302 |
| SF-2026-ARXIV-2605-28354 | AGENT-PLANNING | books/part-07-agent/79-planning.md#chapter-79 | books/part-07-agent/78-tool-calling.md#chapter-78;books/part-07-agent/80-reflection.md#chapter-80 | existing:SF-2026-ARXIV-2605-28354 | delta:SF-2026-ARXIV-2605-28354 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28354 |
| SF-2026-ARXIV-2605-28371 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-28371 | delta:SF-2026-ARXIV-2605-28371 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28371 |
| SF-2026-ARXIV-2605-28384 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#chapter-56 | books/part-05-inference-system/55-pd-disaggregation.md#chapter-55;books/part-06-ai-infrastructure/57-what-is-ai-platform.md#chapter-57 | existing:SF-2026-ARXIV-2605-28384 | delta:SF-2026-ARXIV-2605-28384 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28384 |
| SF-2026-ARXIV-2605-28390 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-28390 | delta:SF-2026-ARXIV-2605-28390 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28390 |
| SF-2026-ARXIV-2605-28424 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#chapter-33 | books/part-04-training-system/32-ppo.md#chapter-32;books/part-04-training-system/34-dpo.md#chapter-34 | existing:SF-2026-ARXIV-2605-28424 | delta:SF-2026-ARXIV-2605-28424 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28424 |
| SF-2026-ARXIV-2605-28433 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#chapter-82 | books/part-07-agent/81-workflow.md#chapter-81;books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-28433 | delta:SF-2026-ARXIV-2605-28433 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2605-28433 |
| SF-2026-ARXIV-2605-28467 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-28467 | delta:SF-2026-ARXIV-2605-28467 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28467 |
| SF-2026-ARXIV-2605-28480 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#chapter-81 | books/part-07-agent/80-reflection.md#chapter-80;books/part-07-agent/82-multi-agent.md#chapter-82 | existing:SF-2026-ARXIV-2605-28480 | delta:SF-2026-ARXIV-2605-28480 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28480 |
| SF-2026-ARXIV-2605-28508 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-28508 | delta:SF-2026-ARXIV-2605-28508 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28508 |
| SF-2026-ARXIV-2605-28510 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-28510 | delta:SF-2026-ARXIV-2605-28510 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28510 |
| SF-2026-ARXIV-2605-28544 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24;books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | existing:SF-2026-ARXIV-2605-28544 | delta:SF-2026-ARXIV-2605-28544 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28544 |
| SF-2026-ARXIV-2605-28561 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#chapter-31 | books/part-04-training-system/30-lora.md#chapter-30;books/part-04-training-system/32-ppo.md#chapter-32 | existing:SF-2026-ARXIV-2605-28561 | delta:SF-2026-ARXIV-2605-28561 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28561 |
| SF-2026-ARXIV-2605-28565 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-28565 | delta:SF-2026-ARXIV-2605-28565 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28565 |
| SF-2026-ARXIV-2605-28573 | TRAIN-PRETRAINING | books/part-04-training-system/28-pretraining.md#chapter-28 | books/part-04-training-system/27-data.md#chapter-27;books/part-04-training-system/29-sft.md#chapter-29 | existing:SF-2026-ARXIV-2605-28573 | delta:SF-2026-ARXIV-2605-28573 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28573 |
| SF-2026-ARXIV-2605-28617 | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#chapter-78 | books/part-07-agent/77-memory.md#chapter-77;books/part-07-agent/79-planning.md#chapter-79 | existing:SF-2026-ARXIV-2605-28617 | delta:SF-2026-ARXIV-2605-28617 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2605-28617 |
| SF-2026-ARXIV-2605-28632 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-28632 | delta:SF-2026-ARXIV-2605-28632 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2605-28632 |
| SF-2026-ARXIV-2605-28634 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25;books/part-04-training-system/27-data.md#chapter-27 | existing:SF-2026-ARXIV-2605-28634 | delta:SF-2026-ARXIV-2605-28634 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28634 |
| SF-2026-ARXIV-2605-28640 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#chapter-45 | books/part-05-inference-system/44-decode.md#chapter-44;books/part-05-inference-system/46-continuous-batching.md#chapter-46 | existing:SF-2026-ARXIV-2605-28640 | delta:SF-2026-ARXIV-2605-28640 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28640 |
| SF-2026-ARXIV-2605-28646 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-28646 | delta:SF-2026-ARXIV-2605-28646 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28646 |
| SF-2026-ARXIV-2605-28678 | INFER-SPECULATIVE-DECODING | books/part-05-inference-system/48-speculative-decoding.md#chapter-48 | books/part-05-inference-system/47-pagedattention.md#chapter-47;books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | existing:SF-2026-ARXIV-2605-28678 | delta:SF-2026-ARXIV-2605-28678 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28678 |
| SF-2026-ARXIV-2605-28691 | MULTIMODAL-GENERATIVE-PARADIGMS | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24 | books/part-03-multimodal-world-models/23-multimodal-representation.md#chapter-23;books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | existing:SF-2026-ARXIV-2605-28691 | delta:SF-2026-ARXIV-2605-28691 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28691 |
| SF-2026-ARXIV-2605-28699 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#chapter-33 | books/part-04-training-system/32-ppo.md#chapter-32;books/part-04-training-system/34-dpo.md#chapter-34 | existing:SF-2026-ARXIV-2605-28699 | delta:SF-2026-ARXIV-2605-28699 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28699 |
| SF-2026-ARXIV-2605-28704 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | books/part-05-inference-system/48-speculative-decoding.md#chapter-48;books/part-05-inference-system/50-vllm.md#chapter-50 | existing:SF-2026-ARXIV-2605-28704 | delta:SF-2026-ARXIV-2605-28704 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2605-28704 |
| SF-2026-ARXIV-2605-28721 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-28721 | delta:SF-2026-ARXIV-2605-28721 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28721 |
| SF-2026-ARXIV-2605-28726 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25;books/part-04-training-system/27-data.md#chapter-27 | existing:SF-2026-ARXIV-2605-28726 | delta:SF-2026-ARXIV-2605-28726 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28726 |
| SF-2026-ARXIV-2605-28732 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76;books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-28732 | delta:SF-2026-ARXIV-2605-28732 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28732 |
| SF-2026-ARXIV-2605-28742 | AGENT-REFLECTION | books/part-07-agent/80-reflection.md#chapter-80 | books/part-07-agent/79-planning.md#chapter-79;books/part-07-agent/81-workflow.md#chapter-81 | existing:SF-2026-ARXIV-2605-28742 | delta:SF-2026-ARXIV-2605-28742 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28742 |
| SF-2026-ARXIV-2605-28751 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#chapter-33 | books/part-04-training-system/32-ppo.md#chapter-32;books/part-04-training-system/34-dpo.md#chapter-34 | existing:SF-2026-ARXIV-2605-28751 | delta:SF-2026-ARXIV-2605-28751 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28751 |
| SF-2026-ARXIV-2605-28760 | TRAIN-PRETRAINING | books/part-04-training-system/28-pretraining.md#chapter-28 | books/part-04-training-system/27-data.md#chapter-27;books/part-04-training-system/29-sft.md#chapter-29 | existing:SF-2026-ARXIV-2605-28760 | delta:SF-2026-ARXIV-2605-28760 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2605-28760 |
| SF-2026-ARXIV-2605-28764 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#chapter-82 | books/part-07-agent/81-workflow.md#chapter-81;books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-28764 | delta:SF-2026-ARXIV-2605-28764 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28764 |
| SF-2026-ARXIV-2605-28773 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76;books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-28773 | delta:SF-2026-ARXIV-2605-28773 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28773 |
| SF-2026-ARXIV-2605-28774 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#chapter-33 | books/part-04-training-system/32-ppo.md#chapter-32;books/part-04-training-system/34-dpo.md#chapter-34 | existing:SF-2026-ARXIV-2605-28774 | delta:SF-2026-ARXIV-2605-28774 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28774 |
| SF-2026-ARXIV-2605-28778 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-28778 | delta:SF-2026-ARXIV-2605-28778 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28778 |
| SF-2026-ARXIV-2605-28787 | AGENT-RAG | books/part-07-agent/76-rag.md#chapter-76 | books/part-07-agent/75-context.md#chapter-75;books/part-07-agent/77-memory.md#chapter-77 | existing:SF-2026-ARXIV-2605-28787 | delta:SF-2026-ARXIV-2605-28787 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28787 |
| SF-2026-ARXIV-2605-28803 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25;books/part-04-training-system/27-data.md#chapter-27 | existing:SF-2026-ARXIV-2605-28803 | delta:SF-2026-ARXIV-2605-28803 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28803 |
| SF-2026-ARXIV-2605-28805 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-28805 | delta:SF-2026-ARXIV-2605-28805 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28805 |
| SF-2026-ARXIV-2605-28807 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-28807 | delta:SF-2026-ARXIV-2605-28807 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28807 |
| SF-2026-ARXIV-2605-28819 | TRAIN-LORA | books/part-04-training-system/30-lora.md#chapter-30 | books/part-04-training-system/29-sft.md#chapter-29;books/part-04-training-system/31-rlhf.md#chapter-31 | existing:SF-2026-ARXIV-2605-28819 | delta:SF-2026-ARXIV-2605-28819 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28819 |
| SF-2026-ARXIV-2605-28889 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76;books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-28889 | delta:SF-2026-ARXIV-2605-28889 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28889 |
| SF-2026-ARXIV-2605-28890 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-28890 | delta:SF-2026-ARXIV-2605-28890 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28890 |
| SF-2026-ARXIV-2605-28893 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-28893 | delta:SF-2026-ARXIV-2605-28893 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28893 |
| SF-2026-ARXIV-2605-28897 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-28897 | delta:SF-2026-ARXIV-2605-28897 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28897 |
| SF-2026-ARXIV-2605-28914 | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#chapter-78 | books/part-07-agent/77-memory.md#chapter-77;books/part-07-agent/79-planning.md#chapter-79 | existing:SF-2026-ARXIV-2605-28914 | delta:SF-2026-ARXIV-2605-28914 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28914 |
| SF-2026-ARXIV-2605-28918 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#chapter-33 | books/part-04-training-system/32-ppo.md#chapter-32;books/part-04-training-system/34-dpo.md#chapter-34 | existing:SF-2026-ARXIV-2605-28918 | delta:SF-2026-ARXIV-2605-28918 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28918 |
| SF-2026-ARXIV-2605-28920 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-28920 | delta:SF-2026-ARXIV-2605-28920 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28920 |
| SF-2026-ARXIV-2605-28969 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76;books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-28969 | delta:SF-2026-ARXIV-2605-28969 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28969 |
| SF-2026-ARXIV-2605-28991 | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#chapter-78 | books/part-07-agent/77-memory.md#chapter-77;books/part-07-agent/79-planning.md#chapter-79 | existing:SF-2026-ARXIV-2605-28991 | delta:SF-2026-ARXIV-2605-28991 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28991 |
| SF-2026-ARXIV-2605-28999 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-28999 | delta:SF-2026-ARXIV-2605-28999 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28999 |
| SF-2026-ARXIV-2605-29001 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-29001 | delta:SF-2026-ARXIV-2605-29001 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-29001 |
| SF-2026-ARXIV-2605-29005 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-29005 | delta:SF-2026-ARXIV-2605-29005 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-29005 |
| SF-2026-ARXIV-2605-29054 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-29054 | delta:SF-2026-ARXIV-2605-29054 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-29054 |
| SF-2026-ARXIV-2605-29068 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-29068 | delta:SF-2026-ARXIV-2605-29068 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-29068 |
| SF-2026-ARXIV-2605-29074 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25;books/part-04-training-system/27-data.md#chapter-27 | existing:SF-2026-ARXIV-2605-29074 | delta:SF-2026-ARXIV-2605-29074 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-29074 |
| SF-2026-ARXIV-2605-29075 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76;books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-29075 | delta:SF-2026-ARXIV-2605-29075 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-29075 |
| SF-2026-ARXIV-2605-29078 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#chapter-81 | books/part-07-agent/80-reflection.md#chapter-80;books/part-07-agent/82-multi-agent.md#chapter-82 | existing:SF-2026-ARXIV-2605-29078 | delta:SF-2026-ARXIV-2605-29078 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-29078 |
| SF-2026-ARXIV-2605-29082 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-29082 | delta:SF-2026-ARXIV-2605-29082 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2605-29082 |
| SF-2026-ARXIV-2605-29087 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-29087 | delta:SF-2026-ARXIV-2605-29087 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-29087 |
| SF-2026-ARXIV-2605-29107 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-29107 | delta:SF-2026-ARXIV-2605-29107 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-29107 |
| SF-2026-ARXIV-2605-29114 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-29114 | delta:SF-2026-ARXIV-2605-29114 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-29114 |
| SF-2026-ARXIV-2605-29115 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#chapter-33 | books/part-04-training-system/32-ppo.md#chapter-32;books/part-04-training-system/34-dpo.md#chapter-34 | existing:SF-2026-ARXIV-2605-29115 | delta:SF-2026-ARXIV-2605-29115 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-29115 |
| SF-2026-ARXIV-2605-29119 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#chapter-33 | books/part-04-training-system/32-ppo.md#chapter-32;books/part-04-training-system/34-dpo.md#chapter-34 | existing:SF-2026-ARXIV-2605-29119 | delta:SF-2026-ARXIV-2605-29119 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-29119 |
| SF-2026-ARXIV-2605-29121 | MODEL-MOE | books/part-02-model/21-moe.md#chapter-21 | books/part-02-model/20-sampling.md#chapter-20;books/part-02-model/22-long-context.md#chapter-22 | existing:SF-2026-ARXIV-2605-29121 | delta:SF-2026-ARXIV-2605-29121 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-29121 |
| SF-2026-ARXIV-2605-29123 | MULTIMODAL-GENERATIVE-PARADIGMS | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24 | books/part-03-multimodal-world-models/23-multimodal-representation.md#chapter-23;books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | existing:SF-2026-ARXIV-2605-29123 | delta:SF-2026-ARXIV-2605-29123 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-29123 |
| SF-2026-ARXIV-2605-29129 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-29129 | delta:SF-2026-ARXIV-2605-29129 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-29129 |
| SF-2026-ARXIV-2605-29135 | INFER-GPU-MEMORY | books/part-05-inference-system/54-gpu-memory.md#chapter-54 | books/part-05-inference-system/53-kserve-llm.md#chapter-53;books/part-05-inference-system/55-pd-disaggregation.md#chapter-55 | existing:SF-2026-ARXIV-2605-29135 | delta:SF-2026-ARXIV-2605-29135 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-29135 |
| SF-2026-ARXIV-2605-29139 | AGENT-RAG | books/part-07-agent/76-rag.md#chapter-76 | books/part-07-agent/75-context.md#chapter-75;books/part-07-agent/77-memory.md#chapter-77 | existing:SF-2026-ARXIV-2605-29139 | delta:SF-2026-ARXIV-2605-29139 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-29139 |
| SF-2026-ARXIV-2605-29156 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#chapter-31 | books/part-04-training-system/30-lora.md#chapter-30;books/part-04-training-system/32-ppo.md#chapter-32 | existing:SF-2026-ARXIV-2605-29156 | delta:SF-2026-ARXIV-2605-29156 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-29156 |
| SF-2026-ARXIV-2605-29178 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-29178 | delta:SF-2026-ARXIV-2605-29178 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-29178 |
| SF-2026-ARXIV-2605-29183 | PLATFORM-PRODUCTION | books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | books/part-06-ai-infrastructure/72-security.md#chapter-72;books/part-07-agent/74-prompt.md#chapter-74 | existing:SF-2026-ARXIV-2605-29183 | delta:SF-2026-ARXIV-2605-29183 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-29183 |
| SF-2026-ARXIV-2605-29192 | PLATFORM-TRACE | books/part-06-ai-infrastructure/69-trace.md#chapter-69 | books/part-06-ai-infrastructure/68-logging.md#chapter-68;books/part-06-ai-infrastructure/70-cost.md#chapter-70 | existing:SF-2026-ARXIV-2605-29192 | delta:SF-2026-ARXIV-2605-29192 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-29192 |
| SF-2026-ARXIV-2605-29209 | MULTIMODAL-REPRESENTATION | books/part-03-multimodal-world-models/23-multimodal-representation.md#chapter-23 | books/part-02-model/22-long-context.md#chapter-22;books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24 | existing:SF-2026-ARXIV-2605-29209 | delta:SF-2026-ARXIV-2605-29209 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-29209 |
| SF-2026-ARXIV-2606-07586 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2606-07586 | delta:SF-2026-ARXIV-2606-07586 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-07586 |
| SF-2026-ARXIV-2606-26120 | INFER-CONTINUOUS-BATCHING | books/part-05-inference-system/46-continuous-batching.md#chapter-46 | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#chapter-45;books/part-05-inference-system/47-pagedattention.md#chapter-47 | existing:SF-2026-ARXIV-2606-26120 | delta:SF-2026-ARXIV-2606-26120 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-26120 |
| SF-2026-ARXIV-2606-26122 | TRAIN-DATA | books/part-04-training-system/27-data.md#chapter-27 | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26;books/part-04-training-system/28-pretraining.md#chapter-28 | existing:SF-2026-ARXIV-2606-26122 | delta:SF-2026-ARXIV-2606-26122 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-26122 |

### Books Decision Receipts

<!-- books-review:SF-2026-ARXIV-2605-27820:start -->
<!-- existing:SF-2026-ARXIV-2605-27820:start -->已顺读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 的 27 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前 owner 负责 `PLATFORM-EVALUATION-SYSTEM` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2d996d80d292f4f17ab2ef9ecd57033f53ee34128f8ddad48df2fcce7e1c1f9d`；adjacent=`books/part-06-ai-infrastructure/65-kai-scheduler.md, books/part-06-ai-infrastructure/67-monitoring.md`。<!-- existing:SF-2026-ARXIV-2605-27820:end -->
<!-- delta:SF-2026-ARXIV-2605-27820:start -->However, existing benchmarks fail to jointly evaluate these capabilities due to challenges in designing strictly coupled multi-capability tasks, simulating natural and task-constrained user feedback, and ensuring objective evaluation of dynamic interaction.<!-- delta:SF-2026-ARXIV-2605-27820:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-27820:end -->

<!-- books-review:SF-2026-ARXIV-2605-27825:start -->
<!-- existing:SF-2026-ARXIV-2605-27825:start -->已顺读 owner `books/part-06-ai-infrastructure/72-security.md` 的 21 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；当前 owner 负责 `PLATFORM-SECURITY` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2611c265f71498b21628954e4204075454317f0e019ad8bf1422e8028c1f048b`；adjacent=`books/part-06-ai-infrastructure/71-multi-tenant.md, books/part-06-ai-infrastructure/73-production-best-practice.md`。<!-- existing:SF-2026-ARXIV-2605-27825:end -->
<!-- delta:SF-2026-ARXIV-2605-27825:start -->We propose Multi-Recall Memory MIA (MRMMIA), a unified attack that utilizes multiple recall probes to the agent to extract the membership signal across black-box, gray-box, and white-box settings.<!-- delta:SF-2026-ARXIV-2605-27825:end --> Decision=`Integrate`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-27825:end -->

<!-- books-review:SF-2026-ARXIV-2605-27850:start -->
<!-- existing:SF-2026-ARXIV-2605-27850:start -->已顺读 owner `books/part-07-agent/82-multi-agent.md` 的 17 个 H2 与相邻章节 ['books/part-07-agent/81-workflow.md', 'books/part-07-agent/83-mcp.md']；当前 owner 负责 `AGENT-MULTI-AGENT` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`6baaf2ff0a94d45eb53c487410a43311c6b2a63c2a88e71066c8d2b107388431`；adjacent=`books/part-07-agent/81-workflow.md, books/part-07-agent/83-mcp.md`。<!-- existing:SF-2026-ARXIV-2605-27850:end -->
<!-- delta:SF-2026-ARXIV-2605-27850:start -->We propose \textbf{TCP-MCP} (Topology-Coupled Prompting for Multi-Agent Collaborative Problem-Solving), a co-evolution framework that searches agent prompts and communication topologies as a unified genome.<!-- delta:SF-2026-ARXIV-2605-27850:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-27850:end -->

<!-- books-review:SF-2026-ARXIV-2605-27879:start -->
<!-- existing:SF-2026-ARXIV-2605-27879:start -->已顺读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 的 27 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前 owner 负责 `PLATFORM-EVALUATION-SYSTEM` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2d996d80d292f4f17ab2ef9ecd57033f53ee34128f8ddad48df2fcce7e1c1f9d`；adjacent=`books/part-06-ai-infrastructure/65-kai-scheduler.md, books/part-06-ai-infrastructure/67-monitoring.md`。<!-- existing:SF-2026-ARXIV-2605-27879:end -->
<!-- delta:SF-2026-ARXIV-2605-27879:start -->We propose Faithful Agentic XAI (FAX), a framework that improves explanation faithfulness through explicit verification.<!-- delta:SF-2026-ARXIV-2605-27879:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-27879:end -->

<!-- books-review:SF-2026-ARXIV-2605-27881:start -->
<!-- existing:SF-2026-ARXIV-2605-27881:start -->已顺读 owner `books/part-04-training-system/27-data.md` 的 18 个 H2 与相邻章节 ['books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md', 'books/part-04-training-system/28-pretraining.md']；当前 owner 负责 `TRAIN-DATA` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`6a791d1111cd7019627ea79d0c2c9be8cc4ca30ec72dbb295553428a5250f5c1`；adjacent=`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md, books/part-04-training-system/28-pretraining.md`。<!-- existing:SF-2026-ARXIV-2605-27881:end -->
<!-- delta:SF-2026-ARXIV-2605-27881:start -->We present a controlled empirical study that isolates three under-explored dimensions of search agent training.<!-- delta:SF-2026-ARXIV-2605-27881:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-27881:end -->

<!-- books-review:SF-2026-ARXIV-2605-27898:start -->
<!-- existing:SF-2026-ARXIV-2605-27898:start -->已顺读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 的 27 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前 owner 负责 `PLATFORM-EVALUATION-SYSTEM` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2d996d80d292f4f17ab2ef9ecd57033f53ee34128f8ddad48df2fcce7e1c1f9d`；adjacent=`books/part-06-ai-infrastructure/65-kai-scheduler.md, books/part-06-ai-infrastructure/67-monitoring.md`。<!-- existing:SF-2026-ARXIV-2605-27898:end -->
<!-- delta:SF-2026-ARXIV-2605-27898:start -->In this work, we present a unified framework for the fair evaluation of LLM agentic capabilities.<!-- delta:SF-2026-ARXIV-2605-27898:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-27898:end -->

<!-- books-review:SF-2026-ARXIV-2605-27899:start -->
<!-- existing:SF-2026-ARXIV-2605-27899:start -->已顺读 owner `books/part-04-training-system/33-grpo.md` 的 23 个 H2 与相邻章节 ['books/part-04-training-system/32-ppo.md', 'books/part-04-training-system/34-dpo.md']；当前 owner 负责 `TRAIN-GRPO` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`b145ccd4ff83a1417182006dcad9c4927bb9386dc883a6c5df4307f4f7bfbdd7`；adjacent=`books/part-04-training-system/32-ppo.md, books/part-04-training-system/34-dpo.md`。<!-- existing:SF-2026-ARXIV-2605-27899:end -->
<!-- delta:SF-2026-ARXIV-2605-27899:start -->We propose SkillC, a framework based on Contrastive Skill Credit Assignment (CSCA) that converts this contrast into a direct learning signal for internalization.<!-- delta:SF-2026-ARXIV-2605-27899:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-27899:end -->

<!-- books-review:SF-2026-ARXIV-2605-27901:start -->
<!-- existing:SF-2026-ARXIV-2605-27901:start -->已顺读 owner `books/part-06-ai-infrastructure/72-security.md` 的 21 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；当前 owner 负责 `PLATFORM-SECURITY` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2611c265f71498b21628954e4204075454317f0e019ad8bf1422e8028c1f048b`；adjacent=`books/part-06-ai-infrastructure/71-multi-tenant.md, books/part-06-ai-infrastructure/73-production-best-practice.md`。<!-- existing:SF-2026-ARXIV-2605-27901:end -->
<!-- delta:SF-2026-ARXIV-2605-27901:start -->We present the first large-scale evaluation of CoT monitorability across 13 diverse languages and seven frontier model families, comprising 16 models.<!-- delta:SF-2026-ARXIV-2605-27901:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-27901:end -->

<!-- books-review:SF-2026-ARXIV-2605-27918:start -->
<!-- existing:SF-2026-ARXIV-2605-27918:start -->已顺读 owner `books/part-04-training-system/36-distributed-training.md` 的 30 个 H2 与相邻章节 ['books/part-04-training-system/35-checkpoint.md', 'books/part-04-training-system/37-tensor-parallel.md']；当前 owner 负责 `TRAIN-DISTRIBUTED-TRAINING` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`96ef81f64d613fd7cb8eb3199e94ab8ed66b737dd9764b83f4e756b3d8ca8c58`；adjacent=`books/part-04-training-system/35-checkpoint.md, books/part-04-training-system/37-tensor-parallel.md`。<!-- existing:SF-2026-ARXIV-2605-27918:end -->
<!-- delta:SF-2026-ARXIV-2605-27918:start -->We present Entrain, a distributed MLLM training framework that addresses both heterogeneity and variability in multimodal training workloads.<!-- delta:SF-2026-ARXIV-2605-27918:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-27918:end -->

<!-- books-review:SF-2026-ARXIV-2605-27922:start -->
<!-- existing:SF-2026-ARXIV-2605-27922:start -->已顺读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 的 27 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前 owner 负责 `PLATFORM-EVALUATION-SYSTEM` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2d996d80d292f4f17ab2ef9ecd57033f53ee34128f8ddad48df2fcce7e1c1f9d`；adjacent=`books/part-06-ai-infrastructure/65-kai-scheduler.md, books/part-06-ai-infrastructure/67-monitoring.md`。<!-- existing:SF-2026-ARXIV-2605-27922:end -->
<!-- delta:SF-2026-ARXIV-2605-27922:start -->However, existing benchmarks typically abstract away execution, compare complete agent systems, or hold the harness fixed, making execution-layer variation difficult to study.<!-- delta:SF-2026-ARXIV-2605-27922:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-27922:end -->

<!-- books-review:SF-2026-ARXIV-2605-27947:start -->
<!-- existing:SF-2026-ARXIV-2605-27947:start -->已顺读 owner `books/part-05-inference-system/56-inference-scheduling.md` 的 18 个 H2 与相邻章节 ['books/part-05-inference-system/55-pd-disaggregation.md', 'books/part-06-ai-infrastructure/57-what-is-ai-platform.md']；当前 owner 负责 `INFER-SCHEDULING` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2ae93eeb9a0bfd027148c9a581d2e13c146e920e51834112063db83818271e8e`；adjacent=`books/part-05-inference-system/55-pd-disaggregation.md, books/part-06-ai-infrastructure/57-what-is-ai-platform.md`。<!-- existing:SF-2026-ARXIV-2605-27947:end -->
<!-- delta:SF-2026-ARXIV-2605-27947:start -->Controlled denoising-depth scans show that video refinement can reduce action error up to a state-dependent point, after which the gain may saturate or even reverse when late predictions become less action-relevant or physically unreliable.<!-- delta:SF-2026-ARXIV-2605-27947:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-27947:end -->

<!-- books-review:SF-2026-ARXIV-2605-27954:start -->
<!-- existing:SF-2026-ARXIV-2605-27954:start -->已顺读 owner `books/part-04-training-system/33-grpo.md` 的 23 个 H2 与相邻章节 ['books/part-04-training-system/32-ppo.md', 'books/part-04-training-system/34-dpo.md']；当前 owner 负责 `TRAIN-GRPO` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`b145ccd4ff83a1417182006dcad9c4927bb9386dc883a6c5df4307f4f7bfbdd7`；adjacent=`books/part-04-training-system/32-ppo.md, books/part-04-training-system/34-dpo.md`。<!-- existing:SF-2026-ARXIV-2605-27954:end -->
<!-- delta:SF-2026-ARXIV-2605-27954:start -->However, the training dynamics of agent RL remain poorly understood, limiting our ability to diagnose instabilities and design more effective training algorithms.<!-- delta:SF-2026-ARXIV-2605-27954:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-27954:end -->

<!-- books-review:SF-2026-ARXIV-2605-27957:start -->
<!-- existing:SF-2026-ARXIV-2605-27957:start -->已顺读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 的 27 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前 owner 负责 `PLATFORM-EVALUATION-SYSTEM` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2d996d80d292f4f17ab2ef9ecd57033f53ee34128f8ddad48df2fcce7e1c1f9d`；adjacent=`books/part-06-ai-infrastructure/65-kai-scheduler.md, books/part-06-ai-infrastructure/67-monitoring.md`。<!-- existing:SF-2026-ARXIV-2605-27957:end -->
<!-- delta:SF-2026-ARXIV-2605-27957:start -->We introduce DisasterBench, a benchmark for evaluating structured multi-agent planning over semantically similar but operationally distinct disaster-response tools.<!-- delta:SF-2026-ARXIV-2605-27957:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-27957:end -->

<!-- books-review:SF-2026-ARXIV-2605-27963:start -->
<!-- existing:SF-2026-ARXIV-2605-27963:start -->已顺读 owner `books/part-04-training-system/36-distributed-training.md` 的 30 个 H2 与相邻章节 ['books/part-04-training-system/35-checkpoint.md', 'books/part-04-training-system/37-tensor-parallel.md']；当前 owner 负责 `TRAIN-DISTRIBUTED-TRAINING` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`96ef81f64d613fd7cb8eb3199e94ab8ed66b737dd9764b83f4e756b3d8ca8c58`；adjacent=`books/part-04-training-system/35-checkpoint.md, books/part-04-training-system/37-tensor-parallel.md`。<!-- existing:SF-2026-ARXIV-2605-27963:end -->
<!-- delta:SF-2026-ARXIV-2605-27963:start -->Datacenter network design plays a critical role in AI training by supporting scaling to thousands of accelerators.<!-- delta:SF-2026-ARXIV-2605-27963:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-27963:end -->

<!-- books-review:SF-2026-ARXIV-2605-27980:start -->
<!-- existing:SF-2026-ARXIV-2605-27980:start -->已顺读 owner `books/part-02-model/13-position-encoding.md` 的 17 个 H2 与相邻章节 ['books/part-02-model/12-embedding.md', 'books/part-02-model/14-self-attention.md']；当前 owner 负责 `MODEL-POSITION-ENCODING` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`b458d0e04ecd5b86463a9c67c8c2c1da4a11f4a9e08f41daa2ba7f6b0cc5ca89`；adjacent=`books/part-02-model/12-embedding.md, books/part-02-model/14-self-attention.md`。<!-- existing:SF-2026-ARXIV-2605-27980:end -->
<!-- delta:SF-2026-ARXIV-2605-27980:start -->To address it, we propose Periodic RoPE (P-RoPE), a positional encoding mechanism designed to circumvent this exhaustion.<!-- delta:SF-2026-ARXIV-2605-27980:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-27980:end -->

<!-- books-review:SF-2026-ARXIV-2605-27995:start -->
<!-- existing:SF-2026-ARXIV-2605-27995:start -->已顺读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 的 27 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前 owner 负责 `PLATFORM-EVALUATION-SYSTEM` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2d996d80d292f4f17ab2ef9ecd57033f53ee34128f8ddad48df2fcce7e1c1f9d`；adjacent=`books/part-06-ai-infrastructure/65-kai-scheduler.md, books/part-06-ai-infrastructure/67-monitoring.md`。<!-- existing:SF-2026-ARXIV-2605-27995:end -->
<!-- delta:SF-2026-ARXIV-2605-27995:start -->To evaluate it, we propose AsyncTool, a benchmark for assessing LLM-based agents in interactive multi-task tool-use environments with delayed tool feedback.<!-- delta:SF-2026-ARXIV-2605-27995:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-27995:end -->

<!-- books-review:SF-2026-ARXIV-2605-28000:start -->
<!-- existing:SF-2026-ARXIV-2605-28000:start -->已顺读 owner `books/part-07-agent/78-tool-calling.md` 的 19 个 H2 与相邻章节 ['books/part-07-agent/77-memory.md', 'books/part-07-agent/79-planning.md']；当前 owner 负责 `AGENT-TOOL-CALLING` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`3deca1b35edccc646c1982cea7dd44ce99b94d42a6052e4a581d9ef9007f2bf9`；adjacent=`books/part-07-agent/77-memory.md, books/part-07-agent/79-planning.md`。<!-- existing:SF-2026-ARXIV-2605-28000:end -->
<!-- delta:SF-2026-ARXIV-2605-28000:start -->Large language model agents are increasingly expected to perform operational work: calling APIs, manipulating files, assembling workflows, and acting inside enterprise systems.<!-- delta:SF-2026-ARXIV-2605-28000:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28000:end -->

<!-- books-review:SF-2026-ARXIV-2605-28009:start -->
<!-- existing:SF-2026-ARXIV-2605-28009:start -->已顺读 owner `books/part-07-agent/77-memory.md` 的 18 个 H2 与相邻章节 ['books/part-07-agent/76-rag.md', 'books/part-07-agent/78-tool-calling.md']；当前 owner 负责 `AGENT-MEMORY` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`1203abfc27ba86bbe0de885e58c1574da193e6a85b540cfdf2ac069997f7203d`；adjacent=`books/part-07-agent/76-rag.md, books/part-07-agent/78-tool-calling.md`。<!-- existing:SF-2026-ARXIV-2605-28009:end -->
<!-- delta:SF-2026-ARXIV-2605-28009:start -->To this end, we introduce MemGuard, a type-aware memory framework that preserves functional memory boundaries during memory construction and retrieval.<!-- delta:SF-2026-ARXIV-2605-28009:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28009:end -->

<!-- books-review:SF-2026-ARXIV-2605-28017:start -->
<!-- existing:SF-2026-ARXIV-2605-28017:start -->已顺读 owner `books/part-06-ai-infrastructure/72-security.md` 的 21 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；当前 owner 负责 `PLATFORM-SECURITY` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2611c265f71498b21628954e4204075454317f0e019ad8bf1422e8028c1f048b`；adjacent=`books/part-06-ai-infrastructure/71-multi-tenant.md, books/part-06-ai-infrastructure/73-production-best-practice.md`。<!-- existing:SF-2026-ARXIV-2605-28017:end -->
<!-- delta:SF-2026-ARXIV-2605-28017:start -->In this paper, we re-evaluate seven GEO attacks under a realistic three-stage pipeline (retriever\,$\to$\,LLM reranker\,$\to$\,LLM generator).<!-- delta:SF-2026-ARXIV-2605-28017:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28017:end -->

<!-- books-review:SF-2026-ARXIV-2605-28044:start -->
<!-- existing:SF-2026-ARXIV-2605-28044:start -->已顺读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 的 27 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前 owner 负责 `PLATFORM-EVALUATION-SYSTEM` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2d996d80d292f4f17ab2ef9ecd57033f53ee34128f8ddad48df2fcce7e1c1f9d`；adjacent=`books/part-06-ai-infrastructure/65-kai-scheduler.md, books/part-06-ai-infrastructure/67-monitoring.md`。<!-- existing:SF-2026-ARXIV-2605-28044:end -->
<!-- delta:SF-2026-ARXIV-2605-28044:start -->We study this diagnostic failure as citation laundering: a related source is presented as warrant for an over-strong claim.<!-- delta:SF-2026-ARXIV-2605-28044:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28044:end -->

<!-- books-review:SF-2026-ARXIV-2605-28046:start -->
<!-- existing:SF-2026-ARXIV-2605-28046:start -->已顺读 owner `books/part-07-agent/77-memory.md` 的 18 个 H2 与相邻章节 ['books/part-07-agent/76-rag.md', 'books/part-07-agent/78-tool-calling.md']；当前 owner 负责 `AGENT-MEMORY` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`1203abfc27ba86bbe0de885e58c1574da193e6a85b540cfdf2ac069997f7203d`；adjacent=`books/part-07-agent/76-rag.md, books/part-07-agent/78-tool-calling.md`。<!-- existing:SF-2026-ARXIV-2605-28046:end -->
<!-- delta:SF-2026-ARXIV-2605-28046:start -->We propose MemCog, a Memory-as-Cognition system that makes memory access an integral part of the reasoning process.<!-- delta:SF-2026-ARXIV-2605-28046:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28046:end -->

<!-- books-review:SF-2026-ARXIV-2605-28053:start -->
<!-- existing:SF-2026-ARXIV-2605-28053:start -->已顺读 owner `books/part-05-inference-system/46-continuous-batching.md` 的 19 个 H2 与相邻章节 ['books/part-05-inference-system/45-why-kv-cache-speeds-up.md', 'books/part-05-inference-system/47-pagedattention.md']；当前 owner 负责 `INFER-CONTINUOUS-BATCHING` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`63cc72a49b463999b35f00cebee74adab003bef2716685033c9a7a256d1fb426`；adjacent=`books/part-05-inference-system/45-why-kv-cache-speeds-up.md, books/part-05-inference-system/47-pagedattention.md`。<!-- existing:SF-2026-ARXIV-2605-28053:end -->
<!-- delta:SF-2026-ARXIV-2605-28053:start -->We formulate this problem as read-write TTT serving and present RW-TTT , which tags each decode step with its owner, version, and READ/WRITE effect, batches only compatible phases, and commits updates only to the owner.<!-- delta:SF-2026-ARXIV-2605-28053:end --> Decision=`Integrate`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28053:end -->

<!-- books-review:SF-2026-ARXIV-2605-28071:start -->
<!-- existing:SF-2026-ARXIV-2605-28071:start -->已顺读 owner `books/part-07-agent/78-tool-calling.md` 的 19 个 H2 与相邻章节 ['books/part-07-agent/77-memory.md', 'books/part-07-agent/79-planning.md']；当前 owner 负责 `AGENT-TOOL-CALLING` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`3deca1b35edccc646c1982cea7dd44ce99b94d42a6052e4a581d9ef9007f2bf9`；adjacent=`books/part-07-agent/77-memory.md, books/part-07-agent/79-planning.md`。<!-- existing:SF-2026-ARXIV-2605-28071:end -->
<!-- delta:SF-2026-ARXIV-2605-28071:start -->In this paper, we present AgentGuard, an attribute-based access control framework for tool-use LLM-based agents.<!-- delta:SF-2026-ARXIV-2605-28071:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28071:end -->

<!-- books-review:SF-2026-ARXIV-2605-28074:start -->
<!-- existing:SF-2026-ARXIV-2605-28074:start -->已顺读 owner `books/part-06-ai-infrastructure/72-security.md` 的 21 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；当前 owner 负责 `PLATFORM-SECURITY` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2611c265f71498b21628954e4204075454317f0e019ad8bf1422e8028c1f048b`；adjacent=`books/part-06-ai-infrastructure/71-multi-tenant.md, books/part-06-ai-infrastructure/73-production-best-practice.md`。<!-- existing:SF-2026-ARXIV-2605-28074:end -->
<!-- delta:SF-2026-ARXIV-2605-28074:start -->We present SilentRetrieval, a two-stage data poisoning attack that hijacks RAG systems through adversarially crafted yet fluent documents.<!-- delta:SF-2026-ARXIV-2605-28074:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28074:end -->

<!-- books-review:SF-2026-ARXIV-2605-28083:start -->
<!-- existing:SF-2026-ARXIV-2605-28083:start -->已顺读 owner `books/part-06-ai-infrastructure/72-security.md` 的 21 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；当前 owner 负责 `PLATFORM-SECURITY` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2611c265f71498b21628954e4204075454317f0e019ad8bf1422e8028c1f048b`；adjacent=`books/part-06-ai-infrastructure/71-multi-tenant.md, books/part-06-ai-infrastructure/73-production-best-practice.md`。<!-- existing:SF-2026-ARXIV-2605-28083:end -->
<!-- delta:SF-2026-ARXIV-2605-28083:start -->To overcome this limitation, we propose VLA-Hijack, a unified adversarial framework that breaks the transferability bottleneck by exploiting a fundamental vulnerability identified in this work: before planning any motion, a VLA model must first use visual information to locate its own robotic arm within the environment.<!-- delta:SF-2026-ARXIV-2605-28083:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28083:end -->

<!-- books-review:SF-2026-ARXIV-2605-28095:start -->
<!-- existing:SF-2026-ARXIV-2605-28095:start -->已顺读 owner `books/part-05-inference-system/54-gpu-memory.md` 的 15 个 H2 与相邻章节 ['books/part-05-inference-system/53-kserve-llm.md', 'books/part-05-inference-system/55-pd-disaggregation.md']；当前 owner 负责 `INFER-GPU-MEMORY` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`a089e81dda8ffea7f46622421f9a24b2e91b13731c04d52c67284966c417cce4`；adjacent=`books/part-05-inference-system/53-kserve-llm.md, books/part-05-inference-system/55-pd-disaggregation.md`。<!-- existing:SF-2026-ARXIV-2605-28095:end -->
<!-- delta:SF-2026-ARXIV-2605-28095:start -->We present SiDP, a memory-efficient data-parallel paradigm for offline LLM inference that treats weights as a bandwidth-backed shared resource inside a DP group.<!-- delta:SF-2026-ARXIV-2605-28095:end --> Decision=`Integrate`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28095:end -->

<!-- books-review:SF-2026-ARXIV-2605-28097:start -->
<!-- existing:SF-2026-ARXIV-2605-28097:start -->已顺读 owner `books/part-06-ai-infrastructure/73-production-best-practice.md` 的 15 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/72-security.md', 'books/part-07-agent/74-prompt.md']；当前 owner 负责 `PLATFORM-PRODUCTION` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`8a1230c5475bc0996e1bc446b54154f914d1177178f82eb98e8c9ebe5ad29679`；adjacent=`books/part-06-ai-infrastructure/72-security.md, books/part-07-agent/74-prompt.md`。<!-- existing:SF-2026-ARXIV-2605-28097:end -->
<!-- delta:SF-2026-ARXIV-2605-28097:start -->We present ICAN-Deploy (Identity-stable CANary Deployment), a middleware construction whose state machine holds the identity hash invariant across the canary window by separating capability names (frozen, hashed) from capability versions (mutable runtime state).<!-- delta:SF-2026-ARXIV-2605-28097:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28097:end -->

<!-- books-review:SF-2026-ARXIV-2605-28108:start -->
<!-- existing:SF-2026-ARXIV-2605-28108:start -->已顺读 owner `books/part-07-agent/79-planning.md` 的 14 个 H2 与相邻章节 ['books/part-07-agent/78-tool-calling.md', 'books/part-07-agent/80-reflection.md']；当前 owner 负责 `AGENT-PLANNING` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`22e2cb6740b7057464c1cd35feed95d37cb5f48f7ea0d6ca5f2ddf761b61dd84`；adjacent=`books/part-07-agent/78-tool-calling.md, books/part-07-agent/80-reflection.md`。<!-- existing:SF-2026-ARXIV-2605-28108:end -->
<!-- delta:SF-2026-ARXIV-2605-28108:start -->ATR is hard even to evaluate: the right question is underdetermined and its payoff deferred to tasks that may never arise.<!-- delta:SF-2026-ARXIV-2605-28108:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28108:end -->

<!-- books-review:SF-2026-ARXIV-2605-28112:start -->
<!-- existing:SF-2026-ARXIV-2605-28112:start -->已顺读 owner `books/part-06-ai-infrastructure/72-security.md` 的 21 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；当前 owner 负责 `PLATFORM-SECURITY` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2611c265f71498b21628954e4204075454317f0e019ad8bf1422e8028c1f048b`；adjacent=`books/part-06-ai-infrastructure/71-multi-tenant.md, books/part-06-ai-infrastructure/73-production-best-practice.md`。<!-- existing:SF-2026-ARXIV-2605-28112:end -->
<!-- delta:SF-2026-ARXIV-2605-28112:start -->We introduce Routing Hijacking, a routing-stage attack in which a malicious client forges its profile to attract target queries despite having irrelevant underlying data.<!-- delta:SF-2026-ARXIV-2605-28112:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28112:end -->

<!-- books-review:SF-2026-ARXIV-2605-28116:start -->
<!-- existing:SF-2026-ARXIV-2605-28116:start -->已顺读 owner `books/part-06-ai-infrastructure/72-security.md` 的 21 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；当前 owner 负责 `PLATFORM-SECURITY` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2611c265f71498b21628954e4204075454317f0e019ad8bf1422e8028c1f048b`；adjacent=`books/part-06-ai-infrastructure/71-multi-tenant.md, books/part-06-ai-infrastructure/73-production-best-practice.md`。<!-- existing:SF-2026-ARXIV-2605-28116:end -->
<!-- delta:SF-2026-ARXIV-2605-28116:start -->We present MIRAGE (Mobile Injection of Realistic Adversarial GUI Examples), a pipeline that turns benign mobile screenshots into prompt-injection samples by placing attacker-controlled text into ordinary user-generated content regions, without modifying the agent, the application, or the operating system.<!-- delta:SF-2026-ARXIV-2605-28116:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28116:end -->

<!-- books-review:SF-2026-ARXIV-2605-28122:start -->
<!-- existing:SF-2026-ARXIV-2605-28122:start -->已顺读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 的 27 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前 owner 负责 `PLATFORM-EVALUATION-SYSTEM` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2d996d80d292f4f17ab2ef9ecd57033f53ee34128f8ddad48df2fcce7e1c1f9d`；adjacent=`books/part-06-ai-infrastructure/65-kai-scheduler.md, books/part-06-ai-infrastructure/67-monitoring.md`。<!-- existing:SF-2026-ARXIV-2605-28122:end -->
<!-- delta:SF-2026-ARXIV-2605-28122:start -->We present SNARE (Synthesizing Non-adversarial scenarios for Adaptive Reward-guided Elicitation), a pipeline that composes benign scenarios from reusable scope and trap fragments, scores each run with a judge-free oracle flagging trap-pattern matches and unsolicited file additions or deletions, and uses Thompson sampling to steer each pair's run budget toward the scenarios that most often trigger it.<!-- delta:SF-2026-ARXIV-2605-28122:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28122:end -->

<!-- books-review:SF-2026-ARXIV-2605-28158:start -->
<!-- existing:SF-2026-ARXIV-2605-28158:start -->已顺读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 的 27 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前 owner 负责 `PLATFORM-EVALUATION-SYSTEM` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2d996d80d292f4f17ab2ef9ecd57033f53ee34128f8ddad48df2fcce7e1c1f9d`；adjacent=`books/part-06-ai-infrastructure/65-kai-scheduler.md, books/part-06-ai-infrastructure/67-monitoring.md`。<!-- existing:SF-2026-ARXIV-2605-28158:end -->
<!-- delta:SF-2026-ARXIV-2605-28158:start -->We introduce OR-Space, a full-lifecycle workspace benchmark for evaluating industrial optimization agents across model construction, model revision, and grounded explanation.<!-- delta:SF-2026-ARXIV-2605-28158:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28158:end -->

<!-- books-review:SF-2026-ARXIV-2605-28201:start -->
<!-- existing:SF-2026-ARXIV-2605-28201:start -->已顺读 owner `books/part-06-ai-infrastructure/72-security.md` 的 21 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；当前 owner 负责 `PLATFORM-SECURITY` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2611c265f71498b21628954e4204075454317f0e019ad8bf1422e8028c1f048b`；adjacent=`books/part-06-ai-infrastructure/71-multi-tenant.md, books/part-06-ai-infrastructure/73-production-best-practice.md`。<!-- existing:SF-2026-ARXIV-2605-28201:end -->
<!-- delta:SF-2026-ARXIV-2605-28201:start -->However, we show that adversarial content can also persist across interactions served by the same agent, making such threats harder to detect and mitigate.<!-- delta:SF-2026-ARXIV-2605-28201:end --> Decision=`Integrate`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28201:end -->

<!-- books-review:SF-2026-ARXIV-2605-28213:start -->
<!-- existing:SF-2026-ARXIV-2605-28213:start -->已顺读 owner `books/part-07-agent/84-agent-platform.md` 的 20 个 H2 与相邻章节 ['books/part-07-agent/83-mcp.md']；当前 owner 负责 `AGENT-PLATFORM` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`6980a9cf747990532ed9860f9f29811513be4f712acea90972df70247cbc3360`；adjacent=`books/part-07-agent/83-mcp.md`。<!-- existing:SF-2026-ARXIV-2605-28213:end -->
<!-- delta:SF-2026-ARXIV-2605-28213:start -->We introduce KLineage, which learns this missing "when" knowledge from expert kernels: instead of relying on forward rollouts, KLineage walks expert implementations backward through validation-gated simplifications and reverses each accepted step into a reusable optimization skill.<!-- delta:SF-2026-ARXIV-2605-28213:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28213:end -->

<!-- books-review:SF-2026-ARXIV-2605-28214:start -->
<!-- existing:SF-2026-ARXIV-2605-28214:start -->已顺读 owner `books/part-06-ai-infrastructure/72-security.md` 的 21 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；当前 owner 负责 `PLATFORM-SECURITY` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2611c265f71498b21628954e4204075454317f0e019ad8bf1422e8028c1f048b`；adjacent=`books/part-06-ai-infrastructure/71-multi-tenant.md, books/part-06-ai-infrastructure/73-production-best-practice.md`。<!-- existing:SF-2026-ARXIV-2605-28214:end -->
<!-- delta:SF-2026-ARXIV-2605-28214:start -->In this paper, we study whether latent states can carry attack-associated information that remains effective during clean executions.<!-- delta:SF-2026-ARXIV-2605-28214:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28214:end -->

<!-- books-review:SF-2026-ARXIV-2605-28224:start -->
<!-- existing:SF-2026-ARXIV-2605-28224:start -->已顺读 owner `books/part-07-agent/77-memory.md` 的 18 个 H2 与相邻章节 ['books/part-07-agent/76-rag.md', 'books/part-07-agent/78-tool-calling.md']；当前 owner 负责 `AGENT-MEMORY` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`1203abfc27ba86bbe0de885e58c1574da193e6a85b540cfdf2ac069997f7203d`；adjacent=`books/part-07-agent/76-rag.md, books/part-07-agent/78-tool-calling.md`。<!-- existing:SF-2026-ARXIV-2605-28224:end -->
<!-- delta:SF-2026-ARXIV-2605-28224:start -->We propose a unified framework that decomposes memory along two axes -- the scope of transfer (within an expansion vs.<!-- delta:SF-2026-ARXIV-2605-28224:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28224:end -->

<!-- books-review:SF-2026-ARXIV-2605-28282:start -->
<!-- existing:SF-2026-ARXIV-2605-28282:start -->已顺读 owner `books/part-07-agent/81-workflow.md` 的 17 个 H2 与相邻章节 ['books/part-07-agent/80-reflection.md', 'books/part-07-agent/82-multi-agent.md']；当前 owner 负责 `AGENT-WORKFLOW` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`16b31ba8998e738c714524553aac240bf037dcb61c7bb84c03bcd77bacb2a3cb`；adjacent=`books/part-07-agent/80-reflection.md, books/part-07-agent/82-multi-agent.md`。<!-- existing:SF-2026-ARXIV-2605-28282:end -->
<!-- delta:SF-2026-ARXIV-2605-28282:start -->We present ResearchLoop, an evidence-gated control plane for AI-assisted computational research.<!-- delta:SF-2026-ARXIV-2605-28282:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28282:end -->

<!-- books-review:SF-2026-ARXIV-2605-28302:start -->
<!-- existing:SF-2026-ARXIV-2605-28302:start -->已顺读 owner `books/part-05-inference-system/55-pd-disaggregation.md` 的 17 个 H2 与相邻章节 ['books/part-05-inference-system/54-gpu-memory.md', 'books/part-05-inference-system/56-inference-scheduling.md']；当前 owner 负责 `INFER-PD-DISAGGREGATION` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`766ef84157a1febdc383d1e3a9b2119232482c82bc3e46a4d1d00c07fa94457e`；adjacent=`books/part-05-inference-system/54-gpu-memory.md, books/part-05-inference-system/56-inference-scheduling.md`。<!-- existing:SF-2026-ARXIV-2605-28302:end -->
<!-- delta:SF-2026-ARXIV-2605-28302:start -->Each level of disaggregation deepens the scheduling design space across workload characteristics, resource allocation, and interconnect topology, raising the central question: when does each level actually pay off?<!-- delta:SF-2026-ARXIV-2605-28302:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28302:end -->

<!-- books-review:SF-2026-ARXIV-2605-28354:start -->
<!-- existing:SF-2026-ARXIV-2605-28354:start -->已顺读 owner `books/part-07-agent/79-planning.md` 的 14 个 H2 与相邻章节 ['books/part-07-agent/78-tool-calling.md', 'books/part-07-agent/80-reflection.md']；当前 owner 负责 `AGENT-PLANNING` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`22e2cb6740b7057464c1cd35feed95d37cb5f48f7ea0d6ca5f2ddf761b61dd84`；adjacent=`books/part-07-agent/78-tool-calling.md, books/part-07-agent/80-reflection.md`。<!-- existing:SF-2026-ARXIV-2605-28354:end -->
<!-- delta:SF-2026-ARXIV-2605-28354:start -->We study this through Plan, a structured agentic behavior for multi-hop retrieval that decomposes a question into ordered sub-questions before any retrieval is performed, so that each search step can be anchored to a pre-designed sub-question instead of drifting under the influence of partially relevant documents retrieved earlier.<!-- delta:SF-2026-ARXIV-2605-28354:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28354:end -->

<!-- books-review:SF-2026-ARXIV-2605-28371:start -->
<!-- existing:SF-2026-ARXIV-2605-28371:start -->已顺读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 的 27 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前 owner 负责 `PLATFORM-EVALUATION-SYSTEM` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2d996d80d292f4f17ab2ef9ecd57033f53ee34128f8ddad48df2fcce7e1c1f9d`；adjacent=`books/part-06-ai-infrastructure/65-kai-scheduler.md, books/part-06-ai-infrastructure/67-monitoring.md`。<!-- existing:SF-2026-ARXIV-2605-28371:end -->
<!-- delta:SF-2026-ARXIV-2605-28371:start -->Industrial Prognostics and Health Management (PHM) provides a representative case study for a broader challenge in applied machine learning: translating published papers into executable, benchmark-ready implementations.<!-- delta:SF-2026-ARXIV-2605-28371:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28371:end -->

<!-- books-review:SF-2026-ARXIV-2605-28384:start -->
<!-- existing:SF-2026-ARXIV-2605-28384:start -->已顺读 owner `books/part-05-inference-system/56-inference-scheduling.md` 的 18 个 H2 与相邻章节 ['books/part-05-inference-system/55-pd-disaggregation.md', 'books/part-06-ai-infrastructure/57-what-is-ai-platform.md']；当前 owner 负责 `INFER-SCHEDULING` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2ae93eeb9a0bfd027148c9a581d2e13c146e920e51834112063db83818271e8e`；adjacent=`books/part-05-inference-system/55-pd-disaggregation.md, books/part-06-ai-infrastructure/57-what-is-ai-platform.md`。<!-- existing:SF-2026-ARXIV-2605-28384:end -->
<!-- delta:SF-2026-ARXIV-2605-28384:start -->We propose Meta-Attention, a framework that dynamically routes each token to the most appropriate attention strategy -- full softmax attention, linear (kernel) attention, or sliding-window local attention -- via a Bayesian Meta-Controller.<!-- delta:SF-2026-ARXIV-2605-28384:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28384:end -->

<!-- books-review:SF-2026-ARXIV-2605-28390:start -->
<!-- existing:SF-2026-ARXIV-2605-28390:start -->已顺读 owner `books/part-07-agent/84-agent-platform.md` 的 20 个 H2 与相邻章节 ['books/part-07-agent/83-mcp.md']；当前 owner 负责 `AGENT-PLATFORM` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`6980a9cf747990532ed9860f9f29811513be4f712acea90972df70247cbc3360`；adjacent=`books/part-07-agent/83-mcp.md`。<!-- existing:SF-2026-ARXIV-2605-28390:end -->
<!-- delta:SF-2026-ARXIV-2605-28390:start -->Specifically, we propose HiSME, a lightweight hierarchical skill meta-evolving solution that jointly optimizes skills and the skill evolving strategy by learning meta-skills from agents' task execution traces.<!-- delta:SF-2026-ARXIV-2605-28390:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28390:end -->

<!-- books-review:SF-2026-ARXIV-2605-28424:start -->
<!-- existing:SF-2026-ARXIV-2605-28424:start -->已顺读 owner `books/part-04-training-system/33-grpo.md` 的 23 个 H2 与相邻章节 ['books/part-04-training-system/32-ppo.md', 'books/part-04-training-system/34-dpo.md']；当前 owner 负责 `TRAIN-GRPO` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`b145ccd4ff83a1417182006dcad9c4927bb9386dc883a6c5df4307f4f7bfbdd7`；adjacent=`books/part-04-training-system/32-ppo.md, books/part-04-training-system/34-dpo.md`。<!-- existing:SF-2026-ARXIV-2605-28424:end -->
<!-- delta:SF-2026-ARXIV-2605-28424:start -->To address this dilemma, we propose Skill0.5, a novel agentic RL framework that explicitly differentiates skill treatments by combining general skill internalization with task-specific skill utilization.<!-- delta:SF-2026-ARXIV-2605-28424:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28424:end -->

<!-- books-review:SF-2026-ARXIV-2605-28433:start -->
<!-- existing:SF-2026-ARXIV-2605-28433:start -->已顺读 owner `books/part-07-agent/82-multi-agent.md` 的 17 个 H2 与相邻章节 ['books/part-07-agent/81-workflow.md', 'books/part-07-agent/83-mcp.md']；当前 owner 负责 `AGENT-MULTI-AGENT` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`6baaf2ff0a94d45eb53c487410a43311c6b2a63c2a88e71066c8d2b107388431`；adjacent=`books/part-07-agent/81-workflow.md, books/part-07-agent/83-mcp.md`。<!-- existing:SF-2026-ARXIV-2605-28433:end -->
<!-- delta:SF-2026-ARXIV-2605-28433:start -->We formulate this as contract-preserving role evolution, requiring every committed edit to preserve five structural contracts (capability, communication, validation, aggregation, output protocol).<!-- delta:SF-2026-ARXIV-2605-28433:end --> Decision=`Integrate`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28433:end -->

<!-- books-review:SF-2026-ARXIV-2605-28467:start -->
<!-- existing:SF-2026-ARXIV-2605-28467:start -->已顺读 owner `books/part-06-ai-infrastructure/72-security.md` 的 21 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；当前 owner 负责 `PLATFORM-SECURITY` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2611c265f71498b21628954e4204075454317f0e019ad8bf1422e8028c1f048b`；adjacent=`books/part-06-ai-infrastructure/71-multi-tenant.md, books/part-06-ai-infrastructure/73-production-best-practice.md`。<!-- existing:SF-2026-ARXIV-2605-28467:end -->
<!-- delta:SF-2026-ARXIV-2605-28467:start -->We study consistency training, a family of fine-tuning objectives that enforce identical behavior on clean prompts and adversarial rewrites, and evaluate its two main variants, output-level (BCT) and activation-level (ACT), across five reasoning models.<!-- delta:SF-2026-ARXIV-2605-28467:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28467:end -->

<!-- books-review:SF-2026-ARXIV-2605-28480:start -->
<!-- existing:SF-2026-ARXIV-2605-28480:start -->已顺读 owner `books/part-07-agent/81-workflow.md` 的 17 个 H2 与相邻章节 ['books/part-07-agent/80-reflection.md', 'books/part-07-agent/82-multi-agent.md']；当前 owner 负责 `AGENT-WORKFLOW` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`16b31ba8998e738c714524553aac240bf037dcb61c7bb84c03bcd77bacb2a3cb`；adjacent=`books/part-07-agent/80-reflection.md, books/part-07-agent/82-multi-agent.md`。<!-- existing:SF-2026-ARXIV-2605-28480:end -->
<!-- delta:SF-2026-ARXIV-2605-28480:start -->We propose Audio-Mind, an auditable and pluggable framework for conditional evidence acquisition in audio understanding.<!-- delta:SF-2026-ARXIV-2605-28480:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28480:end -->

<!-- books-review:SF-2026-ARXIV-2605-28508:start -->
<!-- existing:SF-2026-ARXIV-2605-28508:start -->已顺读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 的 27 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前 owner 负责 `PLATFORM-EVALUATION-SYSTEM` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2d996d80d292f4f17ab2ef9ecd57033f53ee34128f8ddad48df2fcce7e1c1f9d`；adjacent=`books/part-06-ai-infrastructure/65-kai-scheduler.md, books/part-06-ai-infrastructure/67-monitoring.md`。<!-- existing:SF-2026-ARXIV-2605-28508:end -->
<!-- delta:SF-2026-ARXIV-2605-28508:start -->To support practical decision-making, we propose a shared reporting framework that preserves comparability across systems and application types while remaining sensitive to deployment context.<!-- delta:SF-2026-ARXIV-2605-28508:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28508:end -->

<!-- books-review:SF-2026-ARXIV-2605-28510:start -->
<!-- existing:SF-2026-ARXIV-2605-28510:start -->已顺读 owner `books/part-06-ai-infrastructure/72-security.md` 的 21 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；当前 owner 负责 `PLATFORM-SECURITY` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2611c265f71498b21628954e4204075454317f0e019ad8bf1422e8028c1f048b`；adjacent=`books/part-06-ai-infrastructure/71-multi-tenant.md, books/part-06-ai-infrastructure/73-production-best-practice.md`。<!-- existing:SF-2026-ARXIV-2605-28510:end -->
<!-- delta:SF-2026-ARXIV-2605-28510:start -->To bridge this gap, we introduce SOURCETRACKER, a 300M-parameter encoder tailored for code retrieval, together with a hybrid two-stage provenance-tracking pipeline HYBRIDSOURCETRACKER (HST).<!-- delta:SF-2026-ARXIV-2605-28510:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28510:end -->

<!-- books-review:SF-2026-ARXIV-2605-28544:start -->
<!-- existing:SF-2026-ARXIV-2605-28544:start -->已顺读 owner `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 的 19 个 H2 与相邻章节 ['books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md', 'books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md']；当前 owner 负责 `MULTIMODAL-WORLD-MODELS` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`bb63f32b52cb1e7457ed888eaa9f53fe6273a85a72dd5737709f9832795bf3a3`；adjacent=`books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md, books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md`。<!-- existing:SF-2026-ARXIV-2605-28544:end -->
<!-- delta:SF-2026-ARXIV-2605-28544:start -->We present DriveWAM, a driving world-action model that adapts a pretrained video diffusion transformer into an autoregressive video-action policy.<!-- delta:SF-2026-ARXIV-2605-28544:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28544:end -->

<!-- books-review:SF-2026-ARXIV-2605-28561:start -->
<!-- existing:SF-2026-ARXIV-2605-28561:start -->已顺读 owner `books/part-04-training-system/31-rlhf.md` 的 19 个 H2 与相邻章节 ['books/part-04-training-system/30-lora.md', 'books/part-04-training-system/32-ppo.md']；当前 owner 负责 `TRAIN-RLHF` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`1399c1280771b79bb05afde8ddf4551654c2f7ab47c9654a799131a117ca3e09`；adjacent=`books/part-04-training-system/30-lora.md, books/part-04-training-system/32-ppo.md`。<!-- existing:SF-2026-ARXIV-2605-28561:end -->
<!-- delta:SF-2026-ARXIV-2605-28561:start -->We introduce Soft-RLVR, a framework for reinforcement learning from decomposed, learned verification signals.<!-- delta:SF-2026-ARXIV-2605-28561:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28561:end -->

<!-- books-review:SF-2026-ARXIV-2605-28565:start -->
<!-- existing:SF-2026-ARXIV-2605-28565:start -->已顺读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 的 27 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前 owner 负责 `PLATFORM-EVALUATION-SYSTEM` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2d996d80d292f4f17ab2ef9ecd57033f53ee34128f8ddad48df2fcce7e1c1f9d`；adjacent=`books/part-06-ai-infrastructure/65-kai-scheduler.md, books/part-06-ai-infrastructure/67-monitoring.md`。<!-- existing:SF-2026-ARXIV-2605-28565:end -->
<!-- delta:SF-2026-ARXIV-2605-28565:start -->We design a three-dimension evaluation framework that scores each citation on intent-purpose alignment, source suitability, and answer-source fidelity, using expert-validated predefined matrices and a five-level fidelity rubric; the framework applies to any system that produces citation-bearing responses.<!-- delta:SF-2026-ARXIV-2605-28565:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28565:end -->

<!-- books-review:SF-2026-ARXIV-2605-28573:start -->
<!-- existing:SF-2026-ARXIV-2605-28573:start -->已顺读 owner `books/part-04-training-system/28-pretraining.md` 的 20 个 H2 与相邻章节 ['books/part-04-training-system/27-data.md', 'books/part-04-training-system/29-sft.md']；当前 owner 负责 `TRAIN-PRETRAINING` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`e490fdda5b66982b11d46974ed6870ea048c715701cc606dfbd7d4df213486dd`；adjacent=`books/part-04-training-system/27-data.md, books/part-04-training-system/29-sft.md`。<!-- existing:SF-2026-ARXIV-2605-28573:end -->
<!-- delta:SF-2026-ARXIV-2605-28573:start -->The massive scaling of Large Language Models (LLMs) has made pretraining increasingly cost-prohibitive.<!-- delta:SF-2026-ARXIV-2605-28573:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28573:end -->

<!-- books-review:SF-2026-ARXIV-2605-28617:start -->
<!-- existing:SF-2026-ARXIV-2605-28617:start -->已顺读 owner `books/part-07-agent/78-tool-calling.md` 的 19 个 H2 与相邻章节 ['books/part-07-agent/77-memory.md', 'books/part-07-agent/79-planning.md']；当前 owner 负责 `AGENT-TOOL-CALLING` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`3deca1b35edccc646c1982cea7dd44ce99b94d42a6052e4a581d9ef9007f2bf9`；adjacent=`books/part-07-agent/77-memory.md, books/part-07-agent/79-planning.md`。<!-- existing:SF-2026-ARXIV-2605-28617:end -->
<!-- delta:SF-2026-ARXIV-2605-28617:start -->We present LACUNA, a programming model for agents that closes this split while preserving safety.<!-- delta:SF-2026-ARXIV-2605-28617:end --> Decision=`Integrate`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28617:end -->

<!-- books-review:SF-2026-ARXIV-2605-28632:start -->
<!-- existing:SF-2026-ARXIV-2605-28632:start -->已顺读 owner `books/part-06-ai-infrastructure/72-security.md` 的 21 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；当前 owner 负责 `PLATFORM-SECURITY` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2611c265f71498b21628954e4204075454317f0e019ad8bf1422e8028c1f048b`；adjacent=`books/part-06-ai-infrastructure/71-multi-tenant.md, books/part-06-ai-infrastructure/73-production-best-practice.md`。<!-- existing:SF-2026-ARXIV-2605-28632:end -->
<!-- delta:SF-2026-ARXIV-2605-28632:start -->Cryptographic watermarking is a leading defense for attributing text generated by large language models (LLMs).<!-- delta:SF-2026-ARXIV-2605-28632:end --> Decision=`Integrate`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28632:end -->

<!-- books-review:SF-2026-ARXIV-2605-28634:start -->
<!-- existing:SF-2026-ARXIV-2605-28634:start -->已顺读 owner `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 的 20 个 H2 与相邻章节 ['books/part-03-multimodal-world-models/25-multimodal-world-models.md', 'books/part-04-training-system/27-data.md']；当前 owner 负责 `MULTIMODAL-EMBODIED-VLA` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`36552034b7fe336a6aa29e98a34678a24f6980cbbe72b183aead5e116188972e`；adjacent=`books/part-03-multimodal-world-models/25-multimodal-world-models.md, books/part-04-training-system/27-data.md`。<!-- existing:SF-2026-ARXIV-2605-28634:end -->
<!-- delta:SF-2026-ARXIV-2605-28634:start -->We propose PrimitiveVLA, a framework that shifts this paradigm toward a Primitive-Centric Disassemble &amp; Assemble paradigm.<!-- delta:SF-2026-ARXIV-2605-28634:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28634:end -->

<!-- books-review:SF-2026-ARXIV-2605-28640:start -->
<!-- existing:SF-2026-ARXIV-2605-28640:start -->已顺读 owner `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 的 15 个 H2 与相邻章节 ['books/part-05-inference-system/44-decode.md', 'books/part-05-inference-system/46-continuous-batching.md']；当前 owner 负责 `INFER-KV-CACHE` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`e968ab13160cc25eb68d40fe046ab62092c3a5bb6785a46794241b176eed9b90`；adjacent=`books/part-05-inference-system/44-decode.md, books/part-05-inference-system/46-continuous-batching.md`。<!-- existing:SF-2026-ARXIV-2605-28640:end -->
<!-- delta:SF-2026-ARXIV-2605-28640:start -->In this paper, we investigate whether this exponentially decaying memory can also improve existing query-aware sparse inference methods.<!-- delta:SF-2026-ARXIV-2605-28640:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28640:end -->

<!-- books-review:SF-2026-ARXIV-2605-28646:start -->
<!-- existing:SF-2026-ARXIV-2605-28646:start -->已顺读 owner `books/part-06-ai-infrastructure/72-security.md` 的 21 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；当前 owner 负责 `PLATFORM-SECURITY` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2611c265f71498b21628954e4204075454317f0e019ad8bf1422e8028c1f048b`；adjacent=`books/part-06-ai-infrastructure/71-multi-tenant.md, books/part-06-ai-infrastructure/73-production-best-practice.md`。<!-- existing:SF-2026-ARXIV-2605-28646:end -->
<!-- delta:SF-2026-ARXIV-2605-28646:start -->We present MaskClaw, an edge-side privacy arbitrator for GUI agents.<!-- delta:SF-2026-ARXIV-2605-28646:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28646:end -->

<!-- books-review:SF-2026-ARXIV-2605-28678:start -->
<!-- existing:SF-2026-ARXIV-2605-28678:start -->已顺读 owner `books/part-05-inference-system/48-speculative-decoding.md` 的 19 个 H2 与相邻章节 ['books/part-05-inference-system/47-pagedattention.md', 'books/part-05-inference-system/49-tensorrt-llm.md']；当前 owner 负责 `INFER-SPECULATIVE-DECODING` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`63abd49ea9f1fc8cb365512ea7b41f59d786879ec3603ab77545700307a29ce8`；adjacent=`books/part-05-inference-system/47-pagedattention.md, books/part-05-inference-system/49-tensorrt-llm.md`。<!-- existing:SF-2026-ARXIV-2605-28678:end -->
<!-- delta:SF-2026-ARXIV-2605-28678:start -->In this work, we introduce DREAM-R, a framework that substantially improves the performance of speculative reasoning.<!-- delta:SF-2026-ARXIV-2605-28678:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28678:end -->

<!-- books-review:SF-2026-ARXIV-2605-28691:start -->
<!-- existing:SF-2026-ARXIV-2605-28691:start -->已顺读 owner `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md` 的 22 个 H2 与相邻章节 ['books/part-03-multimodal-world-models/23-multimodal-representation.md', 'books/part-03-multimodal-world-models/25-multimodal-world-models.md']；当前 owner 负责 `MULTIMODAL-GENERATIVE-PARADIGMS` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`82d67a82821a384369ee36c24794db1b14bdfd6d538877525c38e9420761df30`；adjacent=`books/part-03-multimodal-world-models/23-multimodal-representation.md, books/part-03-multimodal-world-models/25-multimodal-world-models.md`。<!-- existing:SF-2026-ARXIV-2605-28691:end -->
<!-- delta:SF-2026-ARXIV-2605-28691:start -->We introduce OSP-Next, an efficient text-to-video generation model that integrates sparse attention, parallelism, quantization, and reinforcement learning.<!-- delta:SF-2026-ARXIV-2605-28691:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28691:end -->

<!-- books-review:SF-2026-ARXIV-2605-28699:start -->
<!-- existing:SF-2026-ARXIV-2605-28699:start -->已顺读 owner `books/part-04-training-system/33-grpo.md` 的 23 个 H2 与相邻章节 ['books/part-04-training-system/32-ppo.md', 'books/part-04-training-system/34-dpo.md']；当前 owner 负责 `TRAIN-GRPO` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`b145ccd4ff83a1417182006dcad9c4927bb9386dc883a6c5df4307f4f7bfbdd7`；adjacent=`books/part-04-training-system/32-ppo.md, books/part-04-training-system/34-dpo.md`。<!-- existing:SF-2026-ARXIV-2605-28699:end -->
<!-- delta:SF-2026-ARXIV-2605-28699:start -->We introduce TRACER, a turn-level reinforcement framework for cooperative multi-LLM reasoning.<!-- delta:SF-2026-ARXIV-2605-28699:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28699:end -->

<!-- books-review:SF-2026-ARXIV-2605-28704:start -->
<!-- existing:SF-2026-ARXIV-2605-28704:start -->已顺读 owner `books/part-05-inference-system/49-tensorrt-llm.md` 的 20 个 H2 与相邻章节 ['books/part-05-inference-system/48-speculative-decoding.md', 'books/part-05-inference-system/50-vllm.md']；当前 owner 负责 `INFER-TENSORRT-LLM` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`4c19b842b8e2ddb31cc4681c31e5484defce4f9769950473cc31a5afa61e338a`；adjacent=`books/part-05-inference-system/48-speculative-decoding.md, books/part-05-inference-system/50-vllm.md`。<!-- existing:SF-2026-ARXIV-2605-28704:end -->
<!-- delta:SF-2026-ARXIV-2605-28704:start -->In this work, we study the expressive power of floating-point neural networks under generalized floating-point execution semantics, including arbitrary reduction orders and inexact activation implementations with bounded ulp errors.<!-- delta:SF-2026-ARXIV-2605-28704:end --> Decision=`Integrate`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28704:end -->

<!-- books-review:SF-2026-ARXIV-2605-28721:start -->
<!-- existing:SF-2026-ARXIV-2605-28721:start -->已顺读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 的 27 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前 owner 负责 `PLATFORM-EVALUATION-SYSTEM` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2d996d80d292f4f17ab2ef9ecd57033f53ee34128f8ddad48df2fcce7e1c1f9d`；adjacent=`books/part-06-ai-infrastructure/65-kai-scheduler.md, books/part-06-ai-infrastructure/67-monitoring.md`。<!-- existing:SF-2026-ARXIV-2605-28721:end -->
<!-- delta:SF-2026-ARXIV-2605-28721:start -->We study this question on BrowseComp with three diagnostics.<!-- delta:SF-2026-ARXIV-2605-28721:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28721:end -->

<!-- books-review:SF-2026-ARXIV-2605-28726:start -->
<!-- existing:SF-2026-ARXIV-2605-28726:start -->已顺读 owner `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 的 20 个 H2 与相邻章节 ['books/part-03-multimodal-world-models/25-multimodal-world-models.md', 'books/part-04-training-system/27-data.md']；当前 owner 负责 `MULTIMODAL-EMBODIED-VLA` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`36552034b7fe336a6aa29e98a34678a24f6980cbbe72b183aead5e116188972e`；adjacent=`books/part-03-multimodal-world-models/25-multimodal-world-models.md, books/part-04-training-system/27-data.md`。<!-- existing:SF-2026-ARXIV-2605-28726:end -->
<!-- delta:SF-2026-ARXIV-2605-28726:start -->We discover that VLA architectures fail in fundamentally different, predictable ways at the motor-command level.<!-- delta:SF-2026-ARXIV-2605-28726:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28726:end -->

<!-- books-review:SF-2026-ARXIV-2605-28732:start -->
<!-- existing:SF-2026-ARXIV-2605-28732:start -->已顺读 owner `books/part-07-agent/77-memory.md` 的 18 个 H2 与相邻章节 ['books/part-07-agent/76-rag.md', 'books/part-07-agent/78-tool-calling.md']；当前 owner 负责 `AGENT-MEMORY` 的既有演进链。正文已存在该 exact family trace，故不重复写入。 Owner sha256=`1203abfc27ba86bbe0de885e58c1574da193e6a85b540cfdf2ac069997f7203d`；adjacent=`books/part-07-agent/76-rag.md, books/part-07-agent/78-tool-calling.md`。<!-- existing:SF-2026-ARXIV-2605-28732:end -->
<!-- delta:SF-2026-ARXIV-2605-28732:start -->In this work, we study the new problem of error tracing and attribution in LLM memory systems.<!-- delta:SF-2026-ARXIV-2605-28732:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28732:end -->

<!-- books-review:SF-2026-ARXIV-2605-28742:start -->
<!-- existing:SF-2026-ARXIV-2605-28742:start -->已顺读 owner `books/part-07-agent/80-reflection.md` 的 14 个 H2 与相邻章节 ['books/part-07-agent/79-planning.md', 'books/part-07-agent/81-workflow.md']；当前 owner 负责 `AGENT-REFLECTION` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`c1293a34a41ce0c0ee8d27ebdb10d68cada38430db2d77545ddb7873abd6fe08`；adjacent=`books/part-07-agent/79-planning.md, books/part-07-agent/81-workflow.md`。<!-- existing:SF-2026-ARXIV-2605-28742:end -->
<!-- delta:SF-2026-ARXIV-2605-28742:start -->To address this challenge, we introduce Contrastive Reflection (CORE), a non-parametric learning algorithm that compares past reasoning traces to generate insights: short natural-language descriptions of reasoning strategies and constraints that capture differences between successful and unsuccessful problem attempts.<!-- delta:SF-2026-ARXIV-2605-28742:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28742:end -->

<!-- books-review:SF-2026-ARXIV-2605-28751:start -->
<!-- existing:SF-2026-ARXIV-2605-28751:start -->已顺读 owner `books/part-04-training-system/33-grpo.md` 的 23 个 H2 与相邻章节 ['books/part-04-training-system/32-ppo.md', 'books/part-04-training-system/34-dpo.md']；当前 owner 负责 `TRAIN-GRPO` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`b145ccd4ff83a1417182006dcad9c4927bb9386dc883a6c5df4307f4f7bfbdd7`；adjacent=`books/part-04-training-system/32-ppo.md, books/part-04-training-system/34-dpo.md`。<!-- existing:SF-2026-ARXIV-2605-28751:end -->
<!-- delta:SF-2026-ARXIV-2605-28751:start -->We study this question in RL for competitive programming, where hidden unit tests under time and memory limits enforce both functional correctness and computational efficiency.<!-- delta:SF-2026-ARXIV-2605-28751:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28751:end -->

<!-- books-review:SF-2026-ARXIV-2605-28760:start -->
<!-- existing:SF-2026-ARXIV-2605-28760:start -->已顺读 owner `books/part-04-training-system/28-pretraining.md` 与相邻章节 ['books/part-04-training-system/27-data.md', 'books/part-04-training-system/29-sft.md']；zeroth-order fine-tuning 改变 optimizer/update runtime 而非 LoRA 参数化，最终 owner 纠正为 `TRAIN-PRETRAINING`。 Owner sha256=`13847888f3fd7c316fbde2e81ffb6ee73c56f171882d2f70e7023fa3c36c7b21`；adjacent=`books/part-04-training-system/27-data.md, books/part-04-training-system/29-sft.md`。<!-- existing:SF-2026-ARXIV-2605-28760:end -->
<!-- delta:SF-2026-ARXIV-2605-28760:start -->We show that LLM ZO fine-tuning is an inference-dominated workload and execute its repeated scoring phase through a serving runtime.<!-- delta:SF-2026-ARXIV-2605-28760:end --> Decision=`Integrate`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28760:end -->

<!-- books-review:SF-2026-ARXIV-2605-28764:start -->
<!-- existing:SF-2026-ARXIV-2605-28764:start -->已顺读 owner `books/part-07-agent/82-multi-agent.md` 的 17 个 H2 与相邻章节 ['books/part-07-agent/81-workflow.md', 'books/part-07-agent/83-mcp.md']；当前 owner 负责 `AGENT-MULTI-AGENT` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`6baaf2ff0a94d45eb53c487410a43311c6b2a63c2a88e71066c8d2b107388431`；adjacent=`books/part-07-agent/81-workflow.md, books/part-07-agent/83-mcp.md`。<!-- existing:SF-2026-ARXIV-2605-28764:end -->
<!-- delta:SF-2026-ARXIV-2605-28764:start -->We propose SwarmHarness, a decentralised protocol in which HarnessAPI skill nodes self-organise into a compute swarm without any central authority.<!-- delta:SF-2026-ARXIV-2605-28764:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28764:end -->

<!-- books-review:SF-2026-ARXIV-2605-28773:start -->
<!-- existing:SF-2026-ARXIV-2605-28773:start -->已顺读 owner `books/part-07-agent/77-memory.md` 的 18 个 H2 与相邻章节 ['books/part-07-agent/76-rag.md', 'books/part-07-agent/78-tool-calling.md']；当前 owner 负责 `AGENT-MEMORY` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`1203abfc27ba86bbe0de885e58c1574da193e6a85b540cfdf2ac069997f7203d`；adjacent=`books/part-07-agent/76-rag.md, books/part-07-agent/78-tool-calling.md`。<!-- existing:SF-2026-ARXIV-2605-28773:end -->
<!-- delta:SF-2026-ARXIV-2605-28773:start -->To address this, we propose FluxMem, a connectivity-evolving memory framework that models memory as a heterogeneous graph and progressively refines its topology through three stages: initial connection formation, feedback-driven refinement, and long-term consolidation.<!-- delta:SF-2026-ARXIV-2605-28773:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28773:end -->

<!-- books-review:SF-2026-ARXIV-2605-28774:start -->
<!-- existing:SF-2026-ARXIV-2605-28774:start -->已顺读 owner `books/part-04-training-system/33-grpo.md` 的 23 个 H2 与相邻章节 ['books/part-04-training-system/32-ppo.md', 'books/part-04-training-system/34-dpo.md']；当前 owner 负责 `TRAIN-GRPO` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`b145ccd4ff83a1417182006dcad9c4927bb9386dc883a6c5df4307f4f7bfbdd7`；adjacent=`books/part-04-training-system/32-ppo.md, books/part-04-training-system/34-dpo.md`。<!-- existing:SF-2026-ARXIV-2605-28774:end -->
<!-- delta:SF-2026-ARXIV-2605-28774:start -->We propose AXPO (Agent eXplorative Policy Optimization): for each all-wrong tool-using subgroup, AXPO fixes the thinking prefix and resamples the tool call and its continuation, paired with uncertainty-based prefix selection.<!-- delta:SF-2026-ARXIV-2605-28774:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28774:end -->

<!-- books-review:SF-2026-ARXIV-2605-28778:start -->
<!-- existing:SF-2026-ARXIV-2605-28778:start -->已顺读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 的 27 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前 owner 负责 `PLATFORM-EVALUATION-SYSTEM` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2d996d80d292f4f17ab2ef9ecd57033f53ee34128f8ddad48df2fcce7e1c1f9d`；adjacent=`books/part-06-ai-infrastructure/65-kai-scheduler.md, books/part-06-ai-infrastructure/67-monitoring.md`。<!-- existing:SF-2026-ARXIV-2605-28778:end -->
<!-- delta:SF-2026-ARXIV-2605-28778:start -->We conduct the first systematic study of this question, formalizing _marker internal confidence_ (MIC) as the estimated intrinsic confidence a model associates with a specific epistemic marker in a given task domain.<!-- delta:SF-2026-ARXIV-2605-28778:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28778:end -->

<!-- books-review:SF-2026-ARXIV-2605-28787:start -->
<!-- existing:SF-2026-ARXIV-2605-28787:start -->已顺读 owner `books/part-07-agent/76-rag.md` 的 17 个 H2 与相邻章节 ['books/part-07-agent/75-context.md', 'books/part-07-agent/77-memory.md']；当前 owner 负责 `AGENT-RAG` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`3011c1f900fd57c3767efb22ef3cd9b180fd95ace4e1c157c325d229ff114c83`；adjacent=`books/part-07-agent/75-context.md, books/part-07-agent/77-memory.md`。<!-- existing:SF-2026-ARXIV-2605-28787:end -->
<!-- delta:SF-2026-ARXIV-2605-28787:start -->We present a comparative analysis of agentic data retrieval across two distinct environments: a Baseline Agent searching billions of open-web documents, and a Semantic Agent leveraging a corpus of 90 million datasets using schema$.$org.<!-- delta:SF-2026-ARXIV-2605-28787:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28787:end -->

<!-- books-review:SF-2026-ARXIV-2605-28803:start -->
<!-- existing:SF-2026-ARXIV-2605-28803:start -->已顺读 owner `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 的 20 个 H2 与相邻章节 ['books/part-03-multimodal-world-models/25-multimodal-world-models.md', 'books/part-04-training-system/27-data.md']；当前 owner 负责 `MULTIMODAL-EMBODIED-VLA` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`36552034b7fe336a6aa29e98a34678a24f6980cbbe72b183aead5e116188972e`；adjacent=`books/part-03-multimodal-world-models/25-multimodal-world-models.md, books/part-04-training-system/27-data.md`。<!-- existing:SF-2026-ARXIV-2605-28803:end -->
<!-- delta:SF-2026-ARXIV-2605-28803:start -->We present HoloQ-VLA, the first training-free PTQ framework that compresses both the language backbone and the entire diffusion action head to uniform W4A4 precision without mixed-precision allocation.<!-- delta:SF-2026-ARXIV-2605-28803:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28803:end -->

<!-- books-review:SF-2026-ARXIV-2605-28805:start -->
<!-- existing:SF-2026-ARXIV-2605-28805:start -->已顺读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 的 27 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前 owner 负责 `PLATFORM-EVALUATION-SYSTEM` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2d996d80d292f4f17ab2ef9ecd57033f53ee34128f8ddad48df2fcce7e1c1f9d`；adjacent=`books/part-06-ai-infrastructure/65-kai-scheduler.md, books/part-06-ai-infrastructure/67-monitoring.md`。<!-- existing:SF-2026-ARXIV-2605-28805:end -->
<!-- delta:SF-2026-ARXIV-2605-28805:start -->In this work, we investigate multimodal meta-verification, which leverages verifier-generated rationales rather than decision-only signals, and explore how to effectively incorporate meta-verification feedback into multimodal verifier training.<!-- delta:SF-2026-ARXIV-2605-28805:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28805:end -->

<!-- books-review:SF-2026-ARXIV-2605-28807:start -->
<!-- existing:SF-2026-ARXIV-2605-28807:start -->已顺读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 的 27 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前 owner 负责 `PLATFORM-EVALUATION-SYSTEM` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2d996d80d292f4f17ab2ef9ecd57033f53ee34128f8ddad48df2fcce7e1c1f9d`；adjacent=`books/part-06-ai-infrastructure/65-kai-scheduler.md, books/part-06-ai-infrastructure/67-monitoring.md`。<!-- existing:SF-2026-ARXIV-2605-28807:end -->
<!-- delta:SF-2026-ARXIV-2605-28807:start -->We introduce Calibrated Collective Oversight (CCO), which aggregates diverse auxiliary scoring functions into a penalty measuring deviation from a conservative baseline.<!-- delta:SF-2026-ARXIV-2605-28807:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28807:end -->

<!-- books-review:SF-2026-ARXIV-2605-28819:start -->
<!-- existing:SF-2026-ARXIV-2605-28819:start -->已顺读 owner `books/part-04-training-system/28-pretraining.md` 与相邻章节 ['books/part-04-training-system/27-data.md', 'books/part-04-training-system/29-sft.md']；zeroth-order fine-tuning 改变 optimizer/update runtime 而非 LoRA 参数化，最终 owner 纠正为 `TRAIN-PRETRAINING`。 Owner sha256=`13847888f3fd7c316fbde2e81ffb6ee73c56f171882d2f70e7023fa3c36c7b21`；adjacent=`books/part-04-training-system/29-sft.md, books/part-04-training-system/31-rlhf.md`。<!-- existing:SF-2026-ARXIV-2605-28819:end -->
<!-- delta:SF-2026-ARXIV-2605-28819:start -->We introduce PEFT-Arena, a benchmark that jointly measures downstream performance and general capability retention.<!-- delta:SF-2026-ARXIV-2605-28819:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28819:end -->

<!-- books-review:SF-2026-ARXIV-2605-28889:start -->
<!-- existing:SF-2026-ARXIV-2605-28889:start -->已顺读 owner `books/part-07-agent/77-memory.md` 的 18 个 H2 与相邻章节 ['books/part-07-agent/76-rag.md', 'books/part-07-agent/78-tool-calling.md']；当前 owner 负责 `AGENT-MEMORY` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`1203abfc27ba86bbe0de885e58c1574da193e6a85b540cfdf2ac069997f7203d`；adjacent=`books/part-07-agent/76-rag.md, books/part-07-agent/78-tool-calling.md`。<!-- existing:SF-2026-ARXIV-2605-28889:end -->
<!-- delta:SF-2026-ARXIV-2605-28889:start -->We formulate context distillation as a latent memory management problem.<!-- delta:SF-2026-ARXIV-2605-28889:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28889:end -->

<!-- books-review:SF-2026-ARXIV-2605-28890:start -->
<!-- existing:SF-2026-ARXIV-2605-28890:start -->已顺读 owner `books/part-06-ai-infrastructure/72-security.md` 的 21 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；当前 owner 负责 `PLATFORM-SECURITY` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2611c265f71498b21628954e4204075454317f0e019ad8bf1422e8028c1f048b`；adjacent=`books/part-06-ai-infrastructure/71-multi-tenant.md, books/part-06-ai-infrastructure/73-production-best-practice.md`。<!-- existing:SF-2026-ARXIV-2605-28890:end -->
<!-- delta:SF-2026-ARXIV-2605-28890:start -->We propose BiCoT, a watermarking framework that embeds ownership signals into the internal geometry of reasoning traces by aligning high-saliency structural anchors with a private signature subspace while regularizing ordinary control tokens to preserve semantic capacity.<!-- delta:SF-2026-ARXIV-2605-28890:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28890:end -->

<!-- books-review:SF-2026-ARXIV-2605-28893:start -->
<!-- existing:SF-2026-ARXIV-2605-28893:start -->已顺读 owner `books/part-06-ai-infrastructure/72-security.md` 的 21 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；当前 owner 负责 `PLATFORM-SECURITY` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2611c265f71498b21628954e4204075454317f0e019ad8bf1422e8028c1f048b`；adjacent=`books/part-06-ai-infrastructure/71-multi-tenant.md, books/part-06-ai-infrastructure/73-production-best-practice.md`。<!-- existing:SF-2026-ARXIV-2605-28893:end -->
<!-- delta:SF-2026-ARXIV-2605-28893:start -->Although some studies have attempted to investigate the impact of LiL vulnerabilities, they have unfortunately failed to clearly distinguish LiL vulnerabilities from conventional ones, leaving the understanding of real-world LiL vulnerabilities an open problem.<!-- delta:SF-2026-ARXIV-2605-28893:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28893:end -->

<!-- books-review:SF-2026-ARXIV-2605-28897:start -->
<!-- existing:SF-2026-ARXIV-2605-28897:start -->已顺读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 的 27 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前 owner 负责 `PLATFORM-EVALUATION-SYSTEM` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2d996d80d292f4f17ab2ef9ecd57033f53ee34128f8ddad48df2fcce7e1c1f9d`；adjacent=`books/part-06-ai-infrastructure/65-kai-scheduler.md, books/part-06-ai-infrastructure/67-monitoring.md`。<!-- existing:SF-2026-ARXIV-2605-28897:end -->
<!-- delta:SF-2026-ARXIV-2605-28897:start -->In this work, we perform empirical experiments on papers from the 2025 ACL Rolling Review (ARR) to evaluate LLM reviews from both the author and the reviewer perspective.<!-- delta:SF-2026-ARXIV-2605-28897:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28897:end -->

<!-- books-review:SF-2026-ARXIV-2605-28914:start -->
<!-- existing:SF-2026-ARXIV-2605-28914:start -->已顺读 owner `books/part-07-agent/78-tool-calling.md` 的 19 个 H2 与相邻章节 ['books/part-07-agent/77-memory.md', 'books/part-07-agent/79-planning.md']；当前 owner 负责 `AGENT-TOOL-CALLING` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`3deca1b35edccc646c1982cea7dd44ce99b94d42a6052e4a581d9ef9007f2bf9`；adjacent=`books/part-07-agent/77-memory.md, books/part-07-agent/79-planning.md`。<!-- existing:SF-2026-ARXIV-2605-28914:end -->
<!-- delta:SF-2026-ARXIV-2605-28914:start -->We present AIRGuard, a runtime guard that operationalizes least privilege as action-time authorization.<!-- delta:SF-2026-ARXIV-2605-28914:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28914:end -->

<!-- books-review:SF-2026-ARXIV-2605-28918:start -->
<!-- existing:SF-2026-ARXIV-2605-28918:start -->已顺读 owner `books/part-04-training-system/33-grpo.md` 的 23 个 H2 与相邻章节 ['books/part-04-training-system/32-ppo.md', 'books/part-04-training-system/34-dpo.md']；当前 owner 负责 `TRAIN-GRPO` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`b145ccd4ff83a1417182006dcad9c4927bb9386dc883a6c5df4307f4f7bfbdd7`；adjacent=`books/part-04-training-system/32-ppo.md, books/part-04-training-system/34-dpo.md`。<!-- existing:SF-2026-ARXIV-2605-28918:end -->
<!-- delta:SF-2026-ARXIV-2605-28918:start -->We study PPO-trained agents using MiniGrid as core evaluation and MuJoCo as boundary stress test.<!-- delta:SF-2026-ARXIV-2605-28918:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28918:end -->

<!-- books-review:SF-2026-ARXIV-2605-28920:start -->
<!-- existing:SF-2026-ARXIV-2605-28920:start -->已顺读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 的 27 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前 owner 负责 `PLATFORM-EVALUATION-SYSTEM` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2d996d80d292f4f17ab2ef9ecd57033f53ee34128f8ddad48df2fcce7e1c1f9d`；adjacent=`books/part-06-ai-infrastructure/65-kai-scheduler.md, books/part-06-ai-infrastructure/67-monitoring.md`。<!-- existing:SF-2026-ARXIV-2605-28920:end -->
<!-- delta:SF-2026-ARXIV-2605-28920:start -->In this work we introduce conformal generation (Conf-Gen), a general framework adapting CRC to generative tasks while relaxing its theoretical assumptions.<!-- delta:SF-2026-ARXIV-2605-28920:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28920:end -->

<!-- books-review:SF-2026-ARXIV-2605-28969:start -->
<!-- existing:SF-2026-ARXIV-2605-28969:start -->已顺读 owner `books/part-07-agent/77-memory.md` 的 18 个 H2 与相邻章节 ['books/part-07-agent/76-rag.md', 'books/part-07-agent/78-tool-calling.md']；当前 owner 负责 `AGENT-MEMORY` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`1203abfc27ba86bbe0de885e58c1574da193e6a85b540cfdf2ac069997f7203d`；adjacent=`books/part-07-agent/76-rag.md, books/part-07-agent/78-tool-calling.md`。<!-- existing:SF-2026-ARXIV-2605-28969:end -->
<!-- delta:SF-2026-ARXIV-2605-28969:start -->We introduce representational accuracy to measure how faithfully a system captures a person's interpretation.<!-- delta:SF-2026-ARXIV-2605-28969:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28969:end -->

<!-- books-review:SF-2026-ARXIV-2605-28991:start -->
<!-- existing:SF-2026-ARXIV-2605-28991:start -->已顺读 owner `books/part-07-agent/78-tool-calling.md` 的 19 个 H2 与相邻章节 ['books/part-07-agent/77-memory.md', 'books/part-07-agent/79-planning.md']；当前 owner 负责 `AGENT-TOOL-CALLING` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`3deca1b35edccc646c1982cea7dd44ce99b94d42a6052e4a581d9ef9007f2bf9`；adjacent=`books/part-07-agent/77-memory.md, books/part-07-agent/79-planning.md`。<!-- existing:SF-2026-ARXIV-2605-28991:end -->
<!-- delta:SF-2026-ARXIV-2605-28991:start -->We present a secure, manifest-based infrastructure for delegated promotion of privileged software components, deployed in production as part of a large-scale enterprise database system serving both cloud and on-premises installations.<!-- delta:SF-2026-ARXIV-2605-28991:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28991:end -->

<!-- books-review:SF-2026-ARXIV-2605-28999:start -->
<!-- existing:SF-2026-ARXIV-2605-28999:start -->已顺读 owner `books/part-06-ai-infrastructure/72-security.md` 的 21 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；当前 owner 负责 `PLATFORM-SECURITY` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2611c265f71498b21628954e4204075454317f0e019ad8bf1422e8028c1f048b`；adjacent=`books/part-06-ai-infrastructure/71-multi-tenant.md, books/part-06-ai-infrastructure/73-production-best-practice.md`。<!-- existing:SF-2026-ARXIV-2605-28999:end -->
<!-- delta:SF-2026-ARXIV-2605-28999:start -->In this work, we present the first systematic study of prompt-injection attacks in a widely used application: LLM-based resume screening.<!-- delta:SF-2026-ARXIV-2605-28999:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28999:end -->

<!-- books-review:SF-2026-ARXIV-2605-29001:start -->
<!-- existing:SF-2026-ARXIV-2605-29001:start -->已顺读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 的 27 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前 owner 负责 `PLATFORM-EVALUATION-SYSTEM` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2d996d80d292f4f17ab2ef9ecd57033f53ee34128f8ddad48df2fcce7e1c1f9d`；adjacent=`books/part-06-ai-infrastructure/65-kai-scheduler.md, books/part-06-ai-infrastructure/67-monitoring.md`。<!-- existing:SF-2026-ARXIV-2605-29001:end -->
<!-- delta:SF-2026-ARXIV-2605-29001:start -->A paraphrase-quality audit of MathCheck (ICLR 2025) detected 4 semantically incorrect paraphrases in 129 groups (3.1%); removing them drops GPT-4o from rank 2 to rank 4 and elevates Claude Haiku and DeepSeek V3 above it; these ranking changes are invisible to any single-model evaluation.<!-- delta:SF-2026-ARXIV-2605-29001:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-29001:end -->

<!-- books-review:SF-2026-ARXIV-2605-29005:start -->
<!-- existing:SF-2026-ARXIV-2605-29005:start -->已顺读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 的 27 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前 owner 负责 `PLATFORM-EVALUATION-SYSTEM` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2d996d80d292f4f17ab2ef9ecd57033f53ee34128f8ddad48df2fcce7e1c1f9d`；adjacent=`books/part-06-ai-infrastructure/65-kai-scheduler.md, books/part-06-ai-infrastructure/67-monitoring.md`。<!-- existing:SF-2026-ARXIV-2605-29005:end -->
<!-- delta:SF-2026-ARXIV-2605-29005:start -->Diffusion-based neural solvers for combinatorial optimization repeatedly re-evaluate dense edge/factor interactions, making inference expensive in wall-clock time and often memory-bound at scale.<!-- delta:SF-2026-ARXIV-2605-29005:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-29005:end -->

<!-- books-review:SF-2026-ARXIV-2605-29054:start -->
<!-- existing:SF-2026-ARXIV-2605-29054:start -->已顺读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 的 27 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前 owner 负责 `PLATFORM-EVALUATION-SYSTEM` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2d996d80d292f4f17ab2ef9ecd57033f53ee34128f8ddad48df2fcce7e1c1f9d`；adjacent=`books/part-06-ai-infrastructure/65-kai-scheduler.md, books/part-06-ai-infrastructure/67-monitoring.md`。<!-- existing:SF-2026-ARXIV-2605-29054:end -->
<!-- delta:SF-2026-ARXIV-2605-29054:start -->We introduce T2J-Bench, a benchmark for codebase conversion that reformulates conversion as transfer under a fixed equivalence contract.<!-- delta:SF-2026-ARXIV-2605-29054:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-29054:end -->

<!-- books-review:SF-2026-ARXIV-2605-29068:start -->
<!-- existing:SF-2026-ARXIV-2605-29068:start -->已顺读 owner `books/part-06-ai-infrastructure/72-security.md` 的 21 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；当前 owner 负责 `PLATFORM-SECURITY` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2611c265f71498b21628954e4204075454317f0e019ad8bf1422e8028c1f048b`；adjacent=`books/part-06-ai-infrastructure/71-multi-tenant.md, books/part-06-ai-infrastructure/73-production-best-practice.md`。<!-- existing:SF-2026-ARXIV-2605-29068:end -->
<!-- delta:SF-2026-ARXIV-2605-29068:start -->To address this challenge, we propose COLAGUARD, a guardrail model that transfers multi-step safety reasoning into a continuous latent space through a stage-wise training curriculum, enabling direct hidden-state propagation at inference.<!-- delta:SF-2026-ARXIV-2605-29068:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-29068:end -->

<!-- books-review:SF-2026-ARXIV-2605-29074:start -->
<!-- existing:SF-2026-ARXIV-2605-29074:start -->已顺读 owner `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 的 20 个 H2 与相邻章节 ['books/part-03-multimodal-world-models/25-multimodal-world-models.md', 'books/part-04-training-system/27-data.md']；当前 owner 负责 `MULTIMODAL-EMBODIED-VLA` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`36552034b7fe336a6aa29e98a34678a24f6980cbbe72b183aead5e116188972e`；adjacent=`books/part-03-multimodal-world-models/25-multimodal-world-models.md, books/part-04-training-system/27-data.md`。<!-- existing:SF-2026-ARXIV-2605-29074:end -->
<!-- delta:SF-2026-ARXIV-2605-29074:start -->We introduce Embodied3DBench, a robot-centric benchmark targeting low-level spatial intelligence in embodied 3D environments.<!-- delta:SF-2026-ARXIV-2605-29074:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-29074:end -->

<!-- books-review:SF-2026-ARXIV-2605-29075:start -->
<!-- existing:SF-2026-ARXIV-2605-29075:start -->已顺读 owner `books/part-07-agent/77-memory.md` 的 18 个 H2 与相邻章节 ['books/part-07-agent/76-rag.md', 'books/part-07-agent/78-tool-calling.md']；当前 owner 负责 `AGENT-MEMORY` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`1203abfc27ba86bbe0de885e58c1574da193e6a85b540cfdf2ac069997f7203d`；adjacent=`books/part-07-agent/76-rag.md, books/part-07-agent/78-tool-calling.md`。<!-- existing:SF-2026-ARXIV-2605-29075:end -->
<!-- delta:SF-2026-ARXIV-2605-29075:start -->We propose \emph{knowledge offloading} (KOFF), a framework for decomposing a pretrained LLM into a sparse shared backbone and domain-specific memories.<!-- delta:SF-2026-ARXIV-2605-29075:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-29075:end -->

<!-- books-review:SF-2026-ARXIV-2605-29078:start -->
<!-- existing:SF-2026-ARXIV-2605-29078:start -->已顺读 owner `books/part-07-agent/81-workflow.md` 的 17 个 H2 与相邻章节 ['books/part-07-agent/80-reflection.md', 'books/part-07-agent/82-multi-agent.md']；当前 owner 负责 `AGENT-WORKFLOW` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`16b31ba8998e738c714524553aac240bf037dcb61c7bb84c03bcd77bacb2a3cb`；adjacent=`books/part-07-agent/80-reflection.md, books/part-07-agent/82-multi-agent.md`。<!-- existing:SF-2026-ARXIV-2605-29078:end -->
<!-- delta:SF-2026-ARXIV-2605-29078:start -->The results show analytical benefits across all observation lag regimes, as undifferentiated execution failures are transformed into structured, typed outcomes with full attribution coverage.<!-- delta:SF-2026-ARXIV-2605-29078:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-29078:end -->

<!-- books-review:SF-2026-ARXIV-2605-29082:start -->
<!-- existing:SF-2026-ARXIV-2605-29082:start -->已顺读 owner `books/part-07-agent/84-agent-platform.md` 的 20 个 H2 与相邻章节 ['books/part-07-agent/83-mcp.md']；当前 owner 负责 `AGENT-PLATFORM` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`6980a9cf747990532ed9860f9f29811513be4f712acea90972df70247cbc3360`；adjacent=`books/part-07-agent/83-mcp.md`。<!-- existing:SF-2026-ARXIV-2605-29082:end -->
<!-- delta:SF-2026-ARXIV-2605-29082:start -->We present the Redpanda Agentic Data Plane (ADP), an architecture built around out-of-band metadata channels: infrastructure pathways that carry security context, policy signals, and audit trails deterministically, entirely outside the agent's read and write path and across heterogeneous infrastructure.<!-- delta:SF-2026-ARXIV-2605-29082:end --> Decision=`Integrate`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-29082:end -->

<!-- books-review:SF-2026-ARXIV-2605-29087:start -->
<!-- existing:SF-2026-ARXIV-2605-29087:start -->已顺读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 的 27 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前 owner 负责 `PLATFORM-EVALUATION-SYSTEM` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2d996d80d292f4f17ab2ef9ecd57033f53ee34128f8ddad48df2fcce7e1c1f9d`；adjacent=`books/part-06-ai-infrastructure/65-kai-scheduler.md, books/part-06-ai-infrastructure/67-monitoring.md`。<!-- existing:SF-2026-ARXIV-2605-29087:end -->
<!-- delta:SF-2026-ARXIV-2605-29087:start -->Reasoning models are evaluated on single-turn benchmarks but deployed in multi-turn dialogue, where users push back on correct answers.<!-- delta:SF-2026-ARXIV-2605-29087:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-29087:end -->

<!-- books-review:SF-2026-ARXIV-2605-29107:start -->
<!-- existing:SF-2026-ARXIV-2605-29107:start -->已顺读 owner `books/part-06-ai-infrastructure/72-security.md` 的 21 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；当前 owner 负责 `PLATFORM-SECURITY` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2611c265f71498b21628954e4204075454317f0e019ad8bf1422e8028c1f048b`；adjacent=`books/part-06-ai-infrastructure/71-multi-tenant.md, books/part-06-ai-infrastructure/73-production-best-practice.md`。<!-- existing:SF-2026-ARXIV-2605-29107:end -->
<!-- delta:SF-2026-ARXIV-2605-29107:start -->We present GEO-Bench, a benchmark that evaluates GEO ranking-manipulation attacks under one protocol.<!-- delta:SF-2026-ARXIV-2605-29107:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-29107:end -->

<!-- books-review:SF-2026-ARXIV-2605-29114:start -->
<!-- existing:SF-2026-ARXIV-2605-29114:start -->已顺读 owner `books/part-06-ai-infrastructure/72-security.md` 的 21 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；当前 owner 负责 `PLATFORM-SECURITY` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2611c265f71498b21628954e4204075454317f0e019ad8bf1422e8028c1f048b`；adjacent=`books/part-06-ai-infrastructure/71-multi-tenant.md, books/part-06-ai-infrastructure/73-production-best-practice.md`。<!-- existing:SF-2026-ARXIV-2605-29114:end -->
<!-- delta:SF-2026-ARXIV-2605-29114:start -->We show that these models are highly vulnerable to realistic input perturbations, achieving up to 89% attack success rate (ASR) on reasoning and up to 72% on trajectory manipulation in closed-loop simulation, leading to increased collision rates and degraded safety metrics.<!-- delta:SF-2026-ARXIV-2605-29114:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-29114:end -->

<!-- books-review:SF-2026-ARXIV-2605-29115:start -->
<!-- existing:SF-2026-ARXIV-2605-29115:start -->已顺读 owner `books/part-04-training-system/33-grpo.md` 的 23 个 H2 与相邻章节 ['books/part-04-training-system/32-ppo.md', 'books/part-04-training-system/34-dpo.md']；当前 owner 负责 `TRAIN-GRPO` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`b145ccd4ff83a1417182006dcad9c4927bb9386dc883a6c5df4307f4f7bfbdd7`；adjacent=`books/part-04-training-system/32-ppo.md, books/part-04-training-system/34-dpo.md`。<!-- existing:SF-2026-ARXIV-2605-29115:end -->
<!-- delta:SF-2026-ARXIV-2605-29115:start -->We make the distinction operational and build a training surface for the Unix component.<!-- delta:SF-2026-ARXIV-2605-29115:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-29115:end -->

<!-- books-review:SF-2026-ARXIV-2605-29119:start -->
<!-- existing:SF-2026-ARXIV-2605-29119:start -->已顺读 owner `books/part-04-training-system/33-grpo.md` 的 23 个 H2 与相邻章节 ['books/part-04-training-system/32-ppo.md', 'books/part-04-training-system/34-dpo.md']；当前 owner 负责 `TRAIN-GRPO` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`b145ccd4ff83a1417182006dcad9c4927bb9386dc883a6c5df4307f4f7bfbdd7`；adjacent=`books/part-04-training-system/32-ppo.md, books/part-04-training-system/34-dpo.md`。<!-- existing:SF-2026-ARXIV-2605-29119:end -->
<!-- delta:SF-2026-ARXIV-2605-29119:start -->In this work, we propose PRO-CUA, a process-reward optimization framework for training CUAs with iterative step-level reinforcement learning.<!-- delta:SF-2026-ARXIV-2605-29119:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-29119:end -->

<!-- books-review:SF-2026-ARXIV-2605-29121:start -->
<!-- existing:SF-2026-ARXIV-2605-29121:start -->已顺读 owner `books/part-02-model/21-moe.md` 的 17 个 H2 与相邻章节 ['books/part-02-model/20-sampling.md', 'books/part-02-model/22-long-context.md']；当前 owner 负责 `MODEL-MOE` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`3eaf93101db6b0f4fb7aa292a3e610b6fc1cc14af84e385edd9b2c7d115de79d`；adjacent=`books/part-02-model/20-sampling.md, books/part-02-model/22-long-context.md`。<!-- existing:SF-2026-ARXIV-2605-29121:end -->
<!-- delta:SF-2026-ARXIV-2605-29121:start -->We propose a minimal dynamical model of adaptive softmax routing for a two-expert Mixture-of-Experts (MoE) layer.<!-- delta:SF-2026-ARXIV-2605-29121:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-29121:end -->

<!-- books-review:SF-2026-ARXIV-2605-29123:start -->
<!-- existing:SF-2026-ARXIV-2605-29123:start -->已顺读 owner `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md` 的 22 个 H2 与相邻章节 ['books/part-03-multimodal-world-models/23-multimodal-representation.md', 'books/part-03-multimodal-world-models/25-multimodal-world-models.md']；当前 owner 负责 `MULTIMODAL-GENERATIVE-PARADIGMS` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`82d67a82821a384369ee36c24794db1b14bdfd6d538877525c38e9420761df30`；adjacent=`books/part-03-multimodal-world-models/23-multimodal-representation.md, books/part-03-multimodal-world-models/25-multimodal-world-models.md`。<!-- existing:SF-2026-ARXIV-2605-29123:end -->
<!-- delta:SF-2026-ARXIV-2605-29123:start -->Masked diffusion language models (MDMs) uniquely support any-order generation, with confidence-based decoding currently serving as the de facto standard inference policy.<!-- delta:SF-2026-ARXIV-2605-29123:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-29123:end -->

<!-- books-review:SF-2026-ARXIV-2605-29129:start -->
<!-- existing:SF-2026-ARXIV-2605-29129:start -->已顺读 owner `books/part-07-agent/84-agent-platform.md` 的 20 个 H2 与相邻章节 ['books/part-07-agent/83-mcp.md']；当前 owner 负责 `AGENT-PLATFORM` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`6980a9cf747990532ed9860f9f29811513be4f712acea90972df70247cbc3360`；adjacent=`books/part-07-agent/83-mcp.md`。<!-- existing:SF-2026-ARXIV-2605-29129:end -->
<!-- delta:SF-2026-ARXIV-2605-29129:start -->The distinction matters: debt is a stock of design and governance liability, while the tax is a flow of operating cost that arises because stochastic agents act through tools and workflows.<!-- delta:SF-2026-ARXIV-2605-29129:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-29129:end -->

<!-- books-review:SF-2026-ARXIV-2605-29135:start -->
<!-- existing:SF-2026-ARXIV-2605-29135:start -->已顺读 owner `books/part-05-inference-system/54-gpu-memory.md` 的 15 个 H2 与相邻章节 ['books/part-05-inference-system/53-kserve-llm.md', 'books/part-05-inference-system/55-pd-disaggregation.md']；当前 owner 负责 `INFER-GPU-MEMORY` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`a089e81dda8ffea7f46622421f9a24b2e91b13731c04d52c67284966c417cce4`；adjacent=`books/part-05-inference-system/53-kserve-llm.md, books/part-05-inference-system/55-pd-disaggregation.md`。<!-- existing:SF-2026-ARXIV-2605-29135:end -->
<!-- delta:SF-2026-ARXIV-2605-29135:start -->Large language models have achieved remarkable capabilities through scaling, and this paper does not challenge that.<!-- delta:SF-2026-ARXIV-2605-29135:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-29135:end -->

<!-- books-review:SF-2026-ARXIV-2605-29139:start -->
<!-- existing:SF-2026-ARXIV-2605-29139:start -->已顺读 owner `books/part-07-agent/76-rag.md` 的 17 个 H2 与相邻章节 ['books/part-07-agent/75-context.md', 'books/part-07-agent/77-memory.md']；当前 owner 负责 `AGENT-RAG` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`3011c1f900fd57c3767efb22ef3cd9b180fd95ace4e1c157c325d229ff114c83`；adjacent=`books/part-07-agent/75-context.md, books/part-07-agent/77-memory.md`。<!-- existing:SF-2026-ARXIV-2605-29139:end -->
<!-- delta:SF-2026-ARXIV-2605-29139:start -->Federated Conformal RAG (FC-RAG) provides distribution-free coverage for a bandwidth-limited swarm of weak language models, but only at a fixed horizon.<!-- delta:SF-2026-ARXIV-2605-29139:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-29139:end -->

<!-- books-review:SF-2026-ARXIV-2605-29156:start -->
<!-- existing:SF-2026-ARXIV-2605-29156:start -->已顺读 owner `books/part-04-training-system/31-rlhf.md` 的 19 个 H2 与相邻章节 ['books/part-04-training-system/30-lora.md', 'books/part-04-training-system/32-ppo.md']；当前 owner 负责 `TRAIN-RLHF` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`1399c1280771b79bb05afde8ddf4551654c2f7ab47c9654a799131a117ca3e09`；adjacent=`books/part-04-training-system/30-lora.md, books/part-04-training-system/32-ppo.md`。<!-- existing:SF-2026-ARXIV-2605-29156:end -->
<!-- delta:SF-2026-ARXIV-2605-29156:start -->We present RUBRIC-ARROW, an alternating framework that jointly trains a rubric generator and a rubric-conditioned judge, with its RL stage using only pairwise preference data.<!-- delta:SF-2026-ARXIV-2605-29156:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-29156:end -->

<!-- books-review:SF-2026-ARXIV-2605-29178:start -->
<!-- existing:SF-2026-ARXIV-2605-29178:start -->已顺读 owner `books/part-06-ai-infrastructure/72-security.md` 的 21 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；当前 owner 负责 `PLATFORM-SECURITY` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2611c265f71498b21628954e4204075454317f0e019ad8bf1422e8028c1f048b`；adjacent=`books/part-06-ai-infrastructure/71-multi-tenant.md, books/part-06-ai-infrastructure/73-production-best-practice.md`。<!-- existing:SF-2026-ARXIV-2605-29178:end -->
<!-- delta:SF-2026-ARXIV-2605-29178:start -->We introduce SCHEME, a benchmark of 17 task instances across 7 settings and 8 real open-source libraries, each pairing a legitimate software-engineering task with a covert side task.<!-- delta:SF-2026-ARXIV-2605-29178:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-29178:end -->

<!-- books-review:SF-2026-ARXIV-2605-29183:start -->
<!-- existing:SF-2026-ARXIV-2605-29183:start -->已顺读 owner `books/part-06-ai-infrastructure/73-production-best-practice.md` 的 15 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/72-security.md', 'books/part-07-agent/74-prompt.md']；当前 owner 负责 `PLATFORM-PRODUCTION` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`8a1230c5475bc0996e1bc446b54154f914d1177178f82eb98e8c9ebe5ad29679`；adjacent=`books/part-06-ai-infrastructure/72-security.md, books/part-07-agent/74-prompt.md`。<!-- existing:SF-2026-ARXIV-2605-29183:end -->
<!-- delta:SF-2026-ARXIV-2605-29183:start -->We introduce TIMEGATE, a policy layer managing adaptation by budgeting time, labeling, training, and evaluation.<!-- delta:SF-2026-ARXIV-2605-29183:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-29183:end -->

<!-- books-review:SF-2026-ARXIV-2605-29192:start -->
<!-- existing:SF-2026-ARXIV-2605-29192:start -->已顺读 owner `books/part-06-ai-infrastructure/69-trace.md` 的 14 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/68-logging.md', 'books/part-06-ai-infrastructure/70-cost.md']；当前 owner 负责 `PLATFORM-TRACE` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`40fdd931192eb4c937a1d81d3b0bed7e233637b085747f8a54806041da2346ff`；adjacent=`books/part-06-ai-infrastructure/68-logging.md, books/part-06-ai-infrastructure/70-cost.md`。<!-- existing:SF-2026-ARXIV-2605-29192:end -->
<!-- delta:SF-2026-ARXIV-2605-29192:start -->To remedy this, we develop ReasonOps, an unsupervised, expressive method for annotating chain-of-thought traces, providing succinct universal operators.<!-- delta:SF-2026-ARXIV-2605-29192:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-29192:end -->

<!-- books-review:SF-2026-ARXIV-2605-29209:start -->
<!-- existing:SF-2026-ARXIV-2605-29209:start -->已顺读 owner `books/part-03-multimodal-world-models/23-multimodal-representation.md` 的 18 个 H2 与相邻章节 ['books/part-02-model/22-long-context.md', 'books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md']；当前 owner 负责 `MULTIMODAL-REPRESENTATION` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`1ff8825f468efd9646f87225b2412e0ee9bb58fc3490ca2d5307f844a0b95ef1`；adjacent=`books/part-02-model/22-long-context.md, books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md`。<!-- existing:SF-2026-ARXIV-2605-29209:end -->
<!-- delta:SF-2026-ARXIV-2605-29209:start -->To overcome this, we develop a dynamic compression tokenizer that intelligently aligns representations with semantic boundaries, achieving ultra-low frame rates with exceptionally low WER.<!-- delta:SF-2026-ARXIV-2605-29209:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-29209:end -->

<!-- books-review:SF-2026-ARXIV-2606-07586:start -->
<!-- existing:SF-2026-ARXIV-2606-07586:start -->已顺读 owner `books/part-07-agent/84-agent-platform.md` 的 20 个 H2 与相邻章节 ['books/part-07-agent/83-mcp.md']；当前 owner 负责 `AGENT-PLATFORM` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`6980a9cf747990532ed9860f9f29811513be4f712acea90972df70247cbc3360`；adjacent=`books/part-07-agent/83-mcp.md`。<!-- existing:SF-2026-ARXIV-2606-07586:end -->
<!-- delta:SF-2026-ARXIV-2606-07586:start -->We present a two-stage methodology, instantiated on the AMD XDNA 2 NPU, that progresses from human-guided development to agent autonomy.<!-- delta:SF-2026-ARXIV-2606-07586:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2606-07586:end -->

<!-- books-review:SF-2026-ARXIV-2606-26120:start -->
<!-- existing:SF-2026-ARXIV-2606-26120:start -->已顺读 owner `books/part-05-inference-system/46-continuous-batching.md` 的 19 个 H2 与相邻章节 ['books/part-05-inference-system/45-why-kv-cache-speeds-up.md', 'books/part-05-inference-system/47-pagedattention.md']；当前 owner 负责 `INFER-CONTINUOUS-BATCHING` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`63cc72a49b463999b35f00cebee74adab003bef2716685033c9a7a256d1fb426`；adjacent=`books/part-05-inference-system/45-why-kv-cache-speeds-up.md, books/part-05-inference-system/47-pagedattention.md`。<!-- existing:SF-2026-ARXIV-2606-26120:end -->
<!-- delta:SF-2026-ARXIV-2606-26120:start -->We propose Dynamic-dLLM, a training-free framework that enhances dLLM inference efficiency through two components: Dynamic Cache Updating (DCU), which adaptively allocates cache-update budgets based on layer-wise token dynamics, and Adaptive Parallel Decoding (APD), which dynamically calibrates decoding thresholds to balance generation quality and efficiency.<!-- delta:SF-2026-ARXIV-2606-26120:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2606-26120:end -->

<!-- books-review:SF-2026-ARXIV-2606-26122:start -->
<!-- existing:SF-2026-ARXIV-2606-26122:start -->已顺读 owner `books/part-04-training-system/27-data.md` 的 18 个 H2 与相邻章节 ['books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md', 'books/part-04-training-system/28-pretraining.md']；当前 owner 负责 `TRAIN-DATA` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`6a791d1111cd7019627ea79d0c2c9be8cc4ca30ec72dbb295553428a5250f5c1`；adjacent=`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md, books/part-04-training-system/28-pretraining.md`。<!-- existing:SF-2026-ARXIV-2606-26122:end -->
<!-- delta:SF-2026-ARXIV-2606-26122:start -->The tuples serve as the training environment, and whose properties directly shape what search strategies and generalization abilities the agent can develop.<!-- delta:SF-2026-ARXIV-2606-26122:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2606-26122:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260528-COVERAGE | fresh-context:may2026-day03 | coverage | coverage:SRC-ARXIV:20260528 | none | 747/747 title+abstract replay；112 retained / 635 family-specific closure | passed |
| SA-20260528-EVIDENCE | fresh-context:may2026-day03 | evidence | review:SF-2026-ARXIV-2605-27820 | none | 112/112 exact-v1 Method/Evaluation/Limitations/Artifact review，blocked=0 | passed |
| SA-20260528-SELECTION | fresh-context:may2026-day03 | deep_analysis_selection | analysis:DA-TOPOLOGY-COLLECTIVE-CO-DESIGN | none | Top-3 只限制 narrative，全部 retained 均已全文 review | passed |
| SA-20260528-BOOKS | fresh-context:may2026-day26-postwrite | books | books-review:SF-2026-ARXIV-2605-27825; books-review:SF-2026-ARXIV-2605-29082 | none | 10/10 canonical writebacks 通过 marker、owner/H2、机制、trade-off、failure/fallback、exact-v1 与 adjacent continuity 审计 | passed |

Fresh-context adversarial pass 复核了全部 747 identity 的 denominator 边界与 112 项 exact-v1 claim boundary；随后对 17 项 provisional Books queue 重读 exact-v1、current owner 与相邻章节，最终保留 10 项、降级 7 项，并将 2605.28760 从 TRAIN-LORA 纠正为 TRAIN-PRETRAINING；没有普通 pending。

## 8. Ignored Noise

635 项逐 family closure 保存在 `screening-ledger-final.json/tsv`；每条包含具名机制/结果、排除边界与重开条件。

## 9. Recommended Action

无需继续写回；未来章节改写需保持 10 个 durable marker 唯一，并重放 owner/adjacent、placement 与 exact-v1 invariants。

## 10. Repository Changes

- 新增 `prewrite-readiness-audit.json`，将 provisional Books queue 从 17 项收紧为 10 项；7 项改为 `No Change — Existing Coverage`，并纠正 2605.28760 的 owner。

- 新建 2026-05-28 date-local Daily、screening ledger、exact-v1 packet、current Books comparison、independent audit 与 final queue。
- Writer 已将 10 项写入 8 个 canonical owner；独立 post-write reviewer 未修改共享 Books。
- 新增 pass-only post-write receipt，并同步 final queue 与本日 Gate；未 stage、commit 或 push。

## 11. Open Questions

无。10/10 已进入 canonical owner，并通过不同 reviewer 的机制、trade-off、failure/fallback、exact-v1 与 adjacent continuity 审计。

### Materials Request

<!-- validator:materials-request-v1 -->
| Request ID | Priority | Source Family ID | Source ID | Gap / Limitation ID | Owner Week | Known Identifiers / URLs | Missing Material | Why Existing Evidence Is Insufficient | Acceptable Substitute | Suggested File Name | Required Review Scope |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

无 external blocker；112/112 exact-v1 primary body 已访问，ordinary pending=0。

## 12. Sources

- DataCite arXiv v2 月度快照：完整 identity、Submitted:v1 timestamp 与 title/abstract 枚举。
- Official arXiv exact-v1 HTML/PDF：112 项 retained family 的 Method、Evaluation、Limitations/Counterevidence 与 Artifact statement。
- Current Books owner 与相邻章节：路径、H2 与 snapshot hash 位于 `books-current-content-comparison.json`。

## 13. Final Status

Completion Status: `Complete`

Coverage: `Closed`

Evidence: `Passed`

Books: `Passed`

unresolved findings: 0

Coverage/Evidence/Books 均已闭合：747/747 screening、112-family denominator、112/112 exact-v1、blocked=0、ordinary pending=0，且 10/10 post-write semantic audit passed。
