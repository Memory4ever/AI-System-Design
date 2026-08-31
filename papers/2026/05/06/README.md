# Daily Research — 2026-05-06

**Research Date:** 2026-05-06

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-05-05 09:00:00 ～ 2026-05-06 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；DataCite 仅用于 identity/date/abstract recovery；技术结论绑定 arXiv exact-v1。

**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed。513/513 screening、63-family denominator、63/63 body-level Review、Books Decision、27 项 writeback/post-write audit 与 withdrawn identity closure 均已闭合；ordinary pending=0、blocker=0。

## Executive Summary

相邻月份 v2 快照共 91,841 条 raw records；严格窗口注册 513 条 identity。513/513 已逐项完成 title+abstract 语义筛选；root challenge 后分母曾由 31 修正为 64，withdrawal reconciliation 再将 `2605.04356v1` 作为 pre-denominator identity closure，最终分母为 63 项（12.28%），其余 450 项均有 family-specific closure。63/63 项完成 body-level Review，27 项 Books writeback 已通过独立 post-write audit。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-05-06 |
| Window End | 2026-05-06 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | DEN-20260506-V2-WITHDRAWAL-RECONCILED |
| Denominator Frozen At | 2026-09-01T14:45:23+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-05-05T09:00:00+08:00 | 2026-05-06T09:00:00+08:00 | 2026-09-01T00:45:00+08:00 | DataCite v2 prefixes 00..99 + 513/513 semantic screen + exact-v1 HTML/PDF | checked | 513 | SF-2026-ARXIV-2605-03275;SF-2026-ARXIV-2605-03309;SF-2026-ARXIV-2605-03310;SF-2026-ARXIV-2605-03312;SF-2026-ARXIV-2605-03314;SF-2026-ARXIV-2605-03327;SF-2026-ARXIV-2605-03353;SF-2026-ARXIV-2605-03354;SF-2026-ARXIV-2605-03375;SF-2026-ARXIV-2605-03378;SF-2026-ARXIV-2605-03379;SF-2026-ARXIV-2605-03408;SF-2026-ARXIV-2605-03425;SF-2026-ARXIV-2605-03482;SF-2026-ARXIV-2605-03505;SF-2026-ARXIV-2605-03534;SF-2026-ARXIV-2605-03561;SF-2026-ARXIV-2605-03562;SF-2026-ARXIV-2605-03566;SF-2026-ARXIV-2605-03596;SF-2026-ARXIV-2605-03644;SF-2026-ARXIV-2605-03667;SF-2026-ARXIV-2605-03675;SF-2026-ARXIV-2605-03677;SF-2026-ARXIV-2605-03762;SF-2026-ARXIV-2605-03838;SF-2026-ARXIV-2605-03858;SF-2026-ARXIV-2605-03862;SF-2026-ARXIV-2605-03884;SF-2026-ARXIV-2605-03952;SF-2026-ARXIV-2605-03971;SF-2026-ARXIV-2605-03986;SF-2026-ARXIV-2605-04018;SF-2026-ARXIV-2605-04019;SF-2026-ARXIV-2605-04036;SF-2026-ARXIV-2605-04039;SF-2026-ARXIV-2605-04116;SF-2026-ARXIV-2605-04135;SF-2026-ARXIV-2605-04172;SF-2026-ARXIV-2605-04178;SF-2026-ARXIV-2605-04209;SF-2026-ARXIV-2605-04213;SF-2026-ARXIV-2605-04215;SF-2026-ARXIV-2605-04236;SF-2026-ARXIV-2605-04256;SF-2026-ARXIV-2605-04263;SF-2026-ARXIV-2605-04264;SF-2026-ARXIV-2605-04266;SF-2026-ARXIV-2605-04269;SF-2026-ARXIV-2605-04295;SF-2026-ARXIV-2605-04312;SF-2026-ARXIV-2605-04333;SF-2026-ARXIV-2605-04341;SF-2026-ARXIV-2605-04357;SF-2026-ARXIV-2605-04361;SF-2026-ARXIV-2605-04373;SF-2026-ARXIV-2605-04375;SF-2026-ARXIV-2605-05248;SF-2026-ARXIV-2605-05253;SF-2026-ARXIV-2605-08190;SF-2026-ARXIV-2605-08192;SF-2026-ARXIV-2605-08195;SF-2026-ARXIV-2605-10959 | pages=100; final_cursor=end; prefixes=00..99; raw=91,841; registered=513; screened=513; retained=63; closure=450; denominator_sha256=2536ca8823b4d872984b41ad78decacac36ce1c4d24bccd3623c9e65c8a0a851 | 2026-05-06T00:59:59Z | papers/2026/05/_sources/daily-20260506/screening-ledger-final.json#sha256:2536ca8823b4d872984b41ad78decacac36ce1c4d24bccd3623c9e65c8a0a851 | — |

### Coverage Limitations

<!-- coverage:SRC-ARXIV:20260506:start -->Coverage recall and 513/513 semantic screening are closed. DataCite supports identity/date/abstract only; all 63 denominator families have body-level evidence, including `2605.03275v1` recovered through a matching licensed mirror. official arXiv abs confirms `2605.04356v1` was withdrawn by Joe Benton and administratively removed because the submitter lacked the right to agree to the license; it is therefore an auditable pre-denominator closure rather than a candidate blocker.<!-- coverage:SRC-ARXIV:20260506:end -->

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-03275 | arXiv:2605.03275v1 | paper-v1:2605.03275 | 2026-W19 | 2026-05-05 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-03275 | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-03275 | yes |
| SF-2026-ARXIV-2605-03309 | arXiv:2605.03309v1 | paper-v1:2605.03309 | 2026-W19 | 2026-05-05 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-03309 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2605-03309 | yes |
| SF-2026-ARXIV-2605-03310 | arXiv:2605.03310v1 | paper-v1:2605.03310 | 2026-W19 | 2026-05-05 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-03310 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-03310 | yes |
| SF-2026-ARXIV-2605-03312 | arXiv:2605.03312v1 | paper-v1:2605.03312 | 2026-W19 | 2026-05-05 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-03312 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-03312 | yes |
| SF-2026-ARXIV-2605-03314 | arXiv:2605.03314v1 | paper-v1:2605.03314 | 2026-W19 | 2026-05-05 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-03314 | self | — | new_in_window | AGENT-CONTEXT | Integrate | books-review:SF-2026-ARXIV-2605-03314 | yes |
| SF-2026-ARXIV-2605-03327 | arXiv:2605.03327v1 | paper-v1:2605.03327 | 2026-W19 | 2026-05-05 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-03327 | self | — | new_in_window | TRAIN-GRPO | Integrate | books-review:SF-2026-ARXIV-2605-03327 | yes |
| SF-2026-ARXIV-2605-03353 | arXiv:2605.03353v1 | paper-v1:2605.03353 | 2026-W19 | 2026-05-05 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-03353 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-03353 | yes |
| SF-2026-ARXIV-2605-03354 | arXiv:2605.03354v1 | paper-v1:2605.03354 | 2026-W19 | 2026-05-05 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-03354 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-03354 | yes |
| SF-2026-ARXIV-2605-03375 | arXiv:2605.03375v1 | paper-v1:2605.03375 | 2026-W19 | 2026-05-05 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-03375 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-03375 | yes |
| SF-2026-ARXIV-2605-03378 | arXiv:2605.03378v1 | paper-v1:2605.03378 | 2026-W19 | 2026-05-05 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-03378 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-03378 | yes |
| SF-2026-ARXIV-2605-03379 | arXiv:2605.03379v1 | paper-v1:2605.03379 | 2026-W19 | 2026-05-05 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-03379 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-03379 | yes |
| SF-2026-ARXIV-2605-03408 | arXiv:2605.03408v1 | paper-v1:2605.03408 | 2026-W19 | 2026-05-05 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-03408 | self | — | new_in_window | TRAIN-RLHF | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-03408 | yes |
| SF-2026-ARXIV-2605-03425 | arXiv:2605.03425v1 | paper-v1:2605.03425 | 2026-W19 | 2026-05-05 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-03425 | self | — | new_in_window | TRAIN-PRETRAINING | Integrate | books-review:SF-2026-ARXIV-2605-03425 | yes |
| SF-2026-ARXIV-2605-03482 | arXiv:2605.03482v1 | paper-v1:2605.03482 | 2026-W19 | 2026-05-05 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-03482 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-03482 | yes |
| SF-2026-ARXIV-2605-03505 | arXiv:2605.03505v1 | paper-v1:2605.03505 | 2026-W19 | 2026-05-05 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-03505 | self | — | new_in_window | PLATFORM-MONITORING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-03505 | yes |
| SF-2026-ARXIV-2605-03534 | arXiv:2605.03534v1 | paper-v1:2605.03534 | 2026-W19 | 2026-05-05 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-03534 | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-03534 | yes |
| SF-2026-ARXIV-2605-03561 | arXiv:2605.03561v1 | paper-v1:2605.03561 | 2026-W19 | 2026-05-05 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-03561 | self | — | new_in_window | PLATFORM-MONITORING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-03561 | yes |
| SF-2026-ARXIV-2605-03562 | arXiv:2605.03562v1 | paper-v1:2605.03562 | 2026-W19 | 2026-05-05 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-03562 | self | — | new_in_window | INFER-KV-CACHE | Integrate | books-review:SF-2026-ARXIV-2605-03562 | yes |
| SF-2026-ARXIV-2605-03566 | arXiv:2605.03566v1 | paper-v1:2605.03566 | 2026-W19 | 2026-05-05 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-03566 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-03566 | yes |
| SF-2026-ARXIV-2605-03596 | arXiv:2605.03596v1 | paper-v1:2605.03596 | 2026-W19 | 2026-05-05 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-03596 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2605-03596 | yes |
| SF-2026-ARXIV-2605-03644 | arXiv:2605.03644v1 | paper-v1:2605.03644 | 2026-W19 | 2026-05-05 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-03644 | self | — | new_in_window | INFER-KV-CACHE | Integrate | books-review:SF-2026-ARXIV-2605-03644 | yes |
| SF-2026-ARXIV-2605-03667 | arXiv:2605.03667v1 | paper-v1:2605.03667 | 2026-W19 | 2026-05-05 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-03667 | self | — | new_in_window | TRAIN-PRETRAINING | Integrate | books-review:SF-2026-ARXIV-2605-03667 | yes |
| SF-2026-ARXIV-2605-03675 | arXiv:2605.03675v1 | paper-v1:2605.03675 | 2026-W19 | 2026-05-05 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-03675 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-03675 | yes |
| SF-2026-ARXIV-2605-03677 | arXiv:2605.03677v1 | paper-v1:2605.03677 | 2026-W19 | 2026-05-05 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-03677 | self | — | new_in_window | TRAIN-RLHF | Integrate | books-review:SF-2026-ARXIV-2605-03677 | yes |
| SF-2026-ARXIV-2605-03762 | arXiv:2605.03762v1 | paper-v1:2605.03762 | 2026-W19 | 2026-05-05 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-03762 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-03762 | yes |
| SF-2026-ARXIV-2605-03838 | arXiv:2605.03838v1 | paper-v1:2605.03838 | 2026-W19 | 2026-05-05 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-03838 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-03838 | yes |
| SF-2026-ARXIV-2605-03858 | arXiv:2605.03858v1 | paper-v1:2605.03858 | 2026-W19 | 2026-05-05 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-03858 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-03858 | yes |
| SF-2026-ARXIV-2605-03862 | arXiv:2605.03862v1 | paper-v1:2605.03862 | 2026-W19 | 2026-05-05 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-03862 | self | — | new_in_window | TRAIN-RLHF | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-03862 | yes |
| SF-2026-ARXIV-2605-03884 | arXiv:2605.03884v1 | paper-v1:2605.03884 | 2026-W19 | 2026-05-05 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-03884 | self | — | new_in_window | AGENT-MULTI-AGENT | Integrate | books-review:SF-2026-ARXIV-2605-03884 | yes |
| SF-2026-ARXIV-2605-03952 | arXiv:2605.03952v1 | paper-v1:2605.03952 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-03952 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-03952 | yes |
| SF-2026-ARXIV-2605-03971 | arXiv:2605.03971v1 | paper-v1:2605.03971 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-03971 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-03971 | yes |
| SF-2026-ARXIV-2605-03986 | arXiv:2605.03986v1 | paper-v1:2605.03986 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-03986 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-03986 | yes |
| SF-2026-ARXIV-2605-04018 | arXiv:2605.04018v1 | paper-v1:2605.04018 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-04018 | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-04018 | yes |
| SF-2026-ARXIV-2605-04019 | arXiv:2605.04019v1 | paper-v1:2605.04019 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2605-04019 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-04019 | yes |
| SF-2026-ARXIV-2605-04036 | arXiv:2605.04036v1 | paper-v1:2605.04036 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-04036 | self | — | new_in_window | TRAIN-SFT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-04036 | yes |
| SF-2026-ARXIV-2605-04039 | arXiv:2605.04039v1 | paper-v1:2605.04039 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-04039 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-04039 | yes |
| SF-2026-ARXIV-2605-04116 | arXiv:2605.04116v1 | paper-v1:2605.04116 | 2026-W19 | 2026-05-05 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-04116 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2605-04116 | yes |
| SF-2026-ARXIV-2605-04135 | arXiv:2605.04135v1 | paper-v1:2605.04135 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-04135 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2605-04135 | yes |
| SF-2026-ARXIV-2605-04172 | arXiv:2605.04172v1 | paper-v1:2605.04172 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-04172 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-04172 | yes |
| SF-2026-ARXIV-2605-04178 | arXiv:2605.04178v1 | paper-v1:2605.04178 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-04178 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-04178 | yes |
| SF-2026-ARXIV-2605-04209 | arXiv:2605.04209v1 | paper-v1:2605.04209 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-04209 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2605-04209 | yes |
| SF-2026-ARXIV-2605-04213 | arXiv:2605.04213v1 | paper-v1:2605.04213 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-04213 | self | — | new_in_window | PLATFORM-MONITORING | Integrate | books-review:SF-2026-ARXIV-2605-04213 | yes |
| SF-2026-ARXIV-2605-04215 | arXiv:2605.04215v1 | paper-v1:2605.04215 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-04215 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | Integrate | books-review:SF-2026-ARXIV-2605-04215 | yes |
| SF-2026-ARXIV-2605-04236 | arXiv:2605.04236v1 | paper-v1:2605.04236 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-04236 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-04236 | yes |
| SF-2026-ARXIV-2605-04256 | arXiv:2605.04256v1 | paper-v1:2605.04256 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-04256 | self | — | new_in_window | AGENT-MCP | Integrate | books-review:SF-2026-ARXIV-2605-04256 | yes |
| SF-2026-ARXIV-2605-04263 | arXiv:2605.04263v1 | paper-v1:2605.04263 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-04263 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | Integrate | books-review:SF-2026-ARXIV-2605-04263 | yes |
| SF-2026-ARXIV-2605-04264 | arXiv:2605.04264v1 | paper-v1:2605.04264 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-04264 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-04264 | yes |
| SF-2026-ARXIV-2605-04266 | arXiv:2605.04266v1 | paper-v1:2605.04266 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-04266 | self | — | new_in_window | TRAIN-RLHF | Integrate | books-review:SF-2026-ARXIV-2605-04266 | yes |
| SF-2026-ARXIV-2605-04269 | arXiv:2605.04269v1 | paper-v1:2605.04269 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-04269 | self | — | new_in_window | TRAIN-PRETRAINING | Integrate | books-review:SF-2026-ARXIV-2605-04269 | yes |
| SF-2026-ARXIV-2605-04295 | arXiv:2605.04295v1 | paper-v1:2605.04295 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-04295 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-04295 | yes |
| SF-2026-ARXIV-2605-04312 | arXiv:2605.04312v1 | paper-v1:2605.04312 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-04312 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-04312 | yes |
| SF-2026-ARXIV-2605-04333 | arXiv:2605.04333v1 | paper-v1:2605.04333 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-04333 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Integrate | books-review:SF-2026-ARXIV-2605-04333 | yes |
| SF-2026-ARXIV-2605-04341 | arXiv:2605.04341v1 | paper-v1:2605.04341 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-04341 | self | — | new_in_window | TRAIN-LORA | Integrate | books-review:SF-2026-ARXIV-2605-04341 | yes |
| SF-2026-ARXIV-2605-04357 | arXiv:2605.04357v1 | paper-v1:2605.04357 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-04357 | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-2026-ARXIV-2605-04357 | yes |
| SF-2026-ARXIV-2605-04361 | arXiv:2605.04361v1 | paper-v1:2605.04361 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-04361 | self | — | new_in_window | AGENT-CONTEXT | Integrate | books-review:SF-2026-ARXIV-2605-04361 | yes |
| SF-2026-ARXIV-2605-04373 | arXiv:2605.04373v1 | paper-v1:2605.04373 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-04373 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-04373 | yes |
| SF-2026-ARXIV-2605-04375 | arXiv:2605.04375v1 | paper-v1:2605.04375 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-04375 | self | — | new_in_window | AGENT-WORKFLOW | Integrate | books-review:SF-2026-ARXIV-2605-04375 | yes |
| SF-2026-ARXIV-2605-05248 | arXiv:2605.05248v1 | paper-v1:2605.05248 | 2026-W19 | 2026-05-05 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-05248 | self | — | new_in_window | AGENT-WORKFLOW | Integrate | books-review:SF-2026-ARXIV-2605-05248 | yes |
| SF-2026-ARXIV-2605-05253 | arXiv:2605.05253v1 | paper-v1:2605.05253 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-05253 | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-05253 | yes |
| SF-2026-ARXIV-2605-08190 | arXiv:2605.08190v1 | paper-v1:2605.08190 | 2026-W19 | 2026-05-05 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-08190 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Integrate | books-review:SF-2026-ARXIV-2605-08190 | yes |
| SF-2026-ARXIV-2605-08192 | arXiv:2605.08192v1 | paper-v1:2605.08192 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-08192 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2605-08192 | yes |
| SF-2026-ARXIV-2605-08195 | arXiv:2605.08195v1 | paper-v1:2605.08195 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-08195 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-08195 | yes |
| SF-2026-ARXIV-2605-10959 | arXiv:2605.10959v1 | paper-v1:2605.10959 | 2026-W19 | 2026-05-05 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2605-10959 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-10959 | yes |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-03275 | RP-a0118756b8c07079 | deep | arXiv:2605.03275v1 | SRC-ARXIV@arXiv:2605.03275v1 | https://www.researchgate.net/publication/404476862_Beyond_Similarity_Search_A_Unified_Data_Layer_for_Production_RAG_Systems §2-5 | https://www.researchgate.net/publication/404476862_Beyond_Similarity_Search_A_Unified_Data_Layer_for_Production_RAG_Systems §6.1-6.5 | https://www.researchgate.net/publication/404476862_Beyond_Similarity_Search_A_Unified_Data_Layer_for_Production_RAG_Systems §7.1-7.3 | Not Disclosed — no event-time implementation artifact or immutable commit is named in the recovered manuscript | claim:SF-2026-ARXIV-2605-03275 | complete |
| SF-2026-ARXIV-2605-03309 | RP-5c9aba81762ce0ea | deep | arXiv:2605.03309v1 | SRC-ARXIV@arXiv:2605.03309v1 | https://arxiv.org/html/2605.03309v1 §4 Two-Layer Archive Format; §5 Cryptographic Registry Identity; §6 Dual-Signature Distribution Model | https://arxiv.org/html/2605.03309v1 §12 Evaluation | https://arxiv.org/html/2605.03309v1 §13.1 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO | https://arxiv.org/html/2605.03309v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-03309 | complete |
| SF-2026-ARXIV-2605-03310 | RP-8a701186e175bd4c | deep | arXiv:2605.03310v1 | SRC-ARXIV@arXiv:2605.03310v1 | https://arxiv.org/html/2605.03310v1 §3 Coordination as an Architectural Layer; §4 Reference Architectures | https://arxiv.org/html/2605.03310v1 §5 Experimental Design; §6 Results | https://arxiv.org/html/2605.03310v1 §7 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO | https://arxiv.org/html/2605.03310v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-03310 | complete |
| SF-2026-ARXIV-2605-03312 | RP-6eefcd898c41c348 | deep | arXiv:2605.03312v1 | SRC-ARXIV@arXiv:2605.03312v1 | https://arxiv.org/html/2605.03312v1 §3 MemFlow Architecture; §4 Intent Router and Memory Tiers | https://arxiv.org/html/2605.03312v1 §5 Experiments | https://arxiv.org/html/2605.03312v1 §6 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO | https://arxiv.org/html/2605.03312v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-03312 | complete |
| SF-2026-ARXIV-2605-03314 | RP-9c49b0314c17a33b | deep | arXiv:2605.03314v1 | SRC-ARXIV@arXiv:2605.03314v1 | https://arxiv.org/html/2605.03314v1 §2 Generation under Coupled State and Commitment; §3 Method | https://arxiv.org/html/2605.03314v1 §4 Experiments | https://arxiv.org/html/2605.03314v1 §F Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO | https://arxiv.org/html/2605.03314v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-03314 | complete |
| SF-2026-ARXIV-2605-03327 | RP-86d2fe8112b2955b | deep | arXiv:2605.03327v1 | SRC-ARXIV@arXiv:2605.03327v1 | https://arxiv.org/html/2605.03327v1 §3 Distribution-Guided Policy Optimization; §3.2 Advantage Redistribution; §3.3 Objective | https://arxiv.org/html/2605.03327v1 §4 Experiments and Ablations | https://arxiv.org/html/2605.03327v1 Appendix A Theory; Appendix B Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO | https://arxiv.org/html/2605.03327v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-03327 | complete |
| SF-2026-ARXIV-2605-03353 | RP-ce8e6577c8151ada | deep | arXiv:2605.03353v1 | SRC-ARXIV@arXiv:2605.03353v1 | https://arxiv.org/html/2605.03353v1 §3 SkIR; §4 Four-Phase Compilation Pipeline | https://arxiv.org/html/2605.03353v1 §5 Evaluation | https://arxiv.org/html/2605.03353v1 §6 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO | https://arxiv.org/html/2605.03353v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-03353 | complete |
| SF-2026-ARXIV-2605-03354 | RP-bc6359b3b3436aef | deep | arXiv:2605.03354v1 | SRC-ARXIV@arXiv:2605.03354v1 | https://arxiv.org/html/2605.03354v1 §3 Circuit Tracing Method; §4 Write-Manage-Read Circuits | https://arxiv.org/html/2605.03354v1 §5 Experiments; §6 Diagnosis | https://arxiv.org/html/2605.03354v1 §7 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO | https://arxiv.org/html/2605.03354v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-03354 | complete |
| SF-2026-ARXIV-2605-03375 | RP-48597d606f2201e2 | deep | arXiv:2605.03375v1 | SRC-ARXIV@arXiv:2605.03375v1 | https://arxiv.org/html/2605.03375v1 §3 GPU-Centric KV Object Store; §4 GPU io_uring; §5 Slack-Aware Scheduling | https://arxiv.org/html/2605.03375v1 §7 Evaluation | https://arxiv.org/html/2605.03375v1 §8 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO | https://arxiv.org/html/2605.03375v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-03375 | complete |
| SF-2026-ARXIV-2605-03378 | RP-d08c61c0419e9a25 | deep | arXiv:2605.03378v1 | SRC-ARXIV@arXiv:2605.03378v1 | https://arxiv.org/html/2605.03378v1 §3 Threat Model; §4 ARGUS Causal-Provenance Auditor | https://arxiv.org/html/2605.03378v1 §5 AgentLure; §6 Evaluation | https://arxiv.org/html/2605.03378v1 §7 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO | https://arxiv.org/html/2605.03378v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-03378 | complete |
| SF-2026-ARXIV-2605-03379 | RP-a981743bedf0cae3 | deep | arXiv:2605.03379v1 | SRC-ARXIV@arXiv:2605.03379v1 | https://arxiv.org/html/2605.03379v1 §2 Latent Success Model; §3 Two-Call Identification | https://arxiv.org/html/2605.03379v1 §4 Vote-Accuracy Curves; §5 Empirical Evaluation | https://arxiv.org/html/2605.03379v1 §6 Scope and Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO | https://arxiv.org/html/2605.03379v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-03379 | complete |
| SF-2026-ARXIV-2605-03408 | RP-7003391d854b82a6 | deep | arXiv:2605.03408v1 | SRC-ARXIV@arXiv:2605.03408v1 | https://arxiv.org/html/2605.03408v1 §3 RL Interface Discovery; §3.2 Observation and Reward Synthesis | https://arxiv.org/html/2605.03408v1 §4 Experimental Setup; §5 Results | https://arxiv.org/html/2605.03408v1 §6 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO | https://arxiv.org/html/2605.03408v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-03408 | complete |
| SF-2026-ARXIV-2605-03425 | RP-942b454a41a0e952 | deep | arXiv:2605.03425v1 | SRC-ARXIV@arXiv:2605.03425v1 | https://arxiv.org/html/2605.03425v1 §3 Filter-Aware Innovation Bias Correction; §4 FIBER | https://arxiv.org/html/2605.03425v1 §5 Experiments and Ablations | https://arxiv.org/html/2605.03425v1 §6 Limitations and Privacy Scope; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO | https://arxiv.org/html/2605.03425v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-03425 | complete |
| SF-2026-ARXIV-2605-03482 | RP-01293ab1ffcb111e | deep | arXiv:2605.03482v1 | SRC-ARXIV@arXiv:2605.03482v1 | https://arxiv.org/html/2605.03482v1 §3 Stackelberg Threat Model; §4 MEMSAD | https://arxiv.org/html/2605.03482v1 §5 Theory; §6 Experiments | https://arxiv.org/html/2605.03482v1 §7 Limitations and Discrete Loophole; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO | https://arxiv.org/html/2605.03482v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-03482 | complete |
| SF-2026-ARXIV-2605-03505 | RP-dc2ca0e9f68558de | deep | arXiv:2605.03505v1 | SRC-ARXIV@arXiv:2605.03505v1 | https://arxiv.org/html/2605.03505v1 §3 LATS-RCA Architecture; §3.2 Reflection-Guided Tree Search | https://arxiv.org/html/2605.03505v1 §4 Experimental Setup; §5 Results | https://arxiv.org/html/2605.03505v1 §6 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO | https://arxiv.org/html/2605.03505v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-03505 | complete |
| SF-2026-ARXIV-2605-03534 | RP-68eb18579a7aabfe | deep | arXiv:2605.03534v1 | SRC-ARXIV@arXiv:2605.03534v1 | https://arxiv.org/html/2605.03534v1 §3 SURE-RAG; §4 Set-Level Aggregation | https://arxiv.org/html/2605.03534v1 §5 Experimental Protocol; §6 Results | https://arxiv.org/html/2605.03534v1 §7 Boundary Mapping and Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO | https://arxiv.org/html/2605.03534v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-03534 | complete |
| SF-2026-ARXIV-2605-03561 | RP-821f32ec39f06070 | deep | arXiv:2605.03561v1 | SRC-ARXIV@arXiv:2605.03561v1 | https://arxiv.org/html/2605.03561v1 §3 Heterogeneous hpcanalysis Framework; §4 C++ and GPU Paths | https://arxiv.org/html/2605.03561v1 §5 Evaluation on Aurora | https://arxiv.org/html/2605.03561v1 §6 Limitations and Portability Boundary; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO | https://arxiv.org/html/2605.03561v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-03561 | complete |
| SF-2026-ARXIV-2605-03562 | RP-38716cc1dc45fd9f | deep | arXiv:2605.03562v1 | SRC-ARXIV@arXiv:2605.03562v1 | https://arxiv.org/html/2605.03562v1 §3 Model-Visible KV Geometry; §4 HeadQ | https://arxiv.org/html/2605.03562v1 §2 Experimental Setup; §5 Empirical Results | https://arxiv.org/html/2605.03562v1 §8 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO | https://arxiv.org/html/2605.03562v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-03562 | complete |
| SF-2026-ARXIV-2605-03566 | RP-82de15918299e3e4 | deep | arXiv:2605.03566v1 | SRC-ARXIV@arXiv:2605.03566v1 | https://arxiv.org/html/2605.03566v1 §3 Tensor Lifting; §4 AIE Lowering Pipeline | https://arxiv.org/html/2605.03566v1 §5 Scientific-Workload Evaluation | https://arxiv.org/html/2605.03566v1 §6 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO | https://arxiv.org/html/2605.03566v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-03566 | complete |
| SF-2026-ARXIV-2605-03596 | RP-ddd7a7bc32c8224c | deep | arXiv:2605.03596v1 | SRC-ARXIV@arXiv:2605.03596v1 | https://arxiv.org/html/2605.03596v1 §3 Workspace-Bench Construction; §4 Dependency and Task Model | https://arxiv.org/html/2605.03596v1 §5 Evaluation Protocol; §6 Results | https://arxiv.org/html/2605.03596v1 §7 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO | https://arxiv.org/html/2605.03596v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-03596 | complete |
| SF-2026-ARXIV-2605-03644 | RP-52a5c5aa33866c67 | deep | arXiv:2605.03644v1 | SRC-ARXIV@arXiv:2605.03644v1 | https://arxiv.org/html/2605.03644v1 §3 AdapShot; §3.2 Adaptive Shot Selection; §3.3 Semantic-Aware KV Reuse | https://arxiv.org/html/2605.03644v1 §4 Experiments and Ablations | https://arxiv.org/html/2605.03644v1 §5 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO | https://arxiv.org/html/2605.03644v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-03644 | complete |
| SF-2026-ARXIV-2605-03667 | RP-ca444d79a34a990c | deep | arXiv:2605.03667v1 | SRC-ARXIV@arXiv:2605.03667v1 | https://arxiv.org/html/2605.03667v1 §3 ELAS Low-Rank and 2:4 Sparse Training | https://arxiv.org/html/2605.03667v1 §4 Experiments and Ablations | https://arxiv.org/html/2605.03667v1 §5 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO | https://arxiv.org/html/2605.03667v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-03667 | complete |
| SF-2026-ARXIV-2605-03675 | RP-52551d4f3a0bddcf | deep | arXiv:2605.03675v1 | SRC-ARXIV@arXiv:2605.03675v1 | https://arxiv.org/html/2605.03675v1 §3 MemTier Architecture; §4 Retrieval Engine | https://arxiv.org/html/2605.03675v1 §5 Evaluation | https://arxiv.org/html/2605.03675v1 §6 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO | https://arxiv.org/html/2605.03675v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-03675 | complete |
| SF-2026-ARXIV-2605-03677 | RP-0735560a086c2fa0 | deep | arXiv:2605.03677v1 | SRC-ARXIV@arXiv:2605.03677v1 | https://arxiv.org/html/2605.03677v1 §3 Dual-Perspective OPD; §3.2 Exploration; §3.3 Teacher Reliability | https://arxiv.org/html/2605.03677v1 §4 Experiments and Ablations | https://arxiv.org/html/2605.03677v1 §5 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO | https://arxiv.org/html/2605.03677v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-03677 | complete |
| SF-2026-ARXIV-2605-03762 | RP-dbfb845233815520 | deep | arXiv:2605.03762v1 | SRC-ARXIV@arXiv:2605.03762v1 | https://arxiv.org/html/2605.03762v1 §3 OracleProto Protocol; §4 Temporal Masking | https://arxiv.org/html/2605.03762v1 §5 Evaluation | https://arxiv.org/html/2605.03762v1 §6 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO | https://arxiv.org/html/2605.03762v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-03762 | complete |
| SF-2026-ARXIV-2605-03838 | RP-0154a88cbe8b4d25 | deep | arXiv:2605.03838v1 | SRC-ARXIV@arXiv:2605.03838v1 | https://arxiv.org/html/2605.03838v1 §3 TRACE Measurement Model; §4 Assurance Case | https://arxiv.org/html/2605.03838v1 §5 Worked Evaluation | https://arxiv.org/html/2605.03838v1 §6 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO | https://arxiv.org/html/2605.03838v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-03838 | complete |
| SF-2026-ARXIV-2605-03858 | RP-a8911933b3fcc6b1 | deep | arXiv:2605.03858v1 | SRC-ARXIV@arXiv:2605.03858v1 | https://arxiv.org/html/2605.03858v1 §3 MCJudgeBench Construction; §4 Constraint-Level Protocol | https://arxiv.org/html/2605.03858v1 §5 Experiments | https://arxiv.org/html/2605.03858v1 §6 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO | https://arxiv.org/html/2605.03858v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-03858 | complete |
| SF-2026-ARXIV-2605-03862 | RP-b83e77097fe9429c | deep | arXiv:2605.03862v1 | SRC-ARXIV@arXiv:2605.03862v1 | https://arxiv.org/html/2605.03862v1 §3 Executor-Grounded Reward; §4 Training | https://arxiv.org/html/2605.03862v1 §5 Experiments and Ablations | https://arxiv.org/html/2605.03862v1 §6 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO | https://arxiv.org/html/2605.03862v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-03862 | complete |
| SF-2026-ARXIV-2605-03884 | RP-20eb36e064217070 | deep | arXiv:2605.03884v1 | SRC-ARXIV@arXiv:2605.03884v1 | https://arxiv.org/pdf/2605.03884v1 PDF §3 Problem Formulation; §4 QKVShare Method | https://arxiv.org/pdf/2605.03884v1 PDF §5 Experimental Setup; §6 Results | https://arxiv.org/pdf/2605.03884v1 PDF §7 Discussion and Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO | https://arxiv.org/pdf/2605.03884v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-03884 | complete |
| SF-2026-ARXIV-2605-03952 | RP-dc5191565e7d924c | deep | arXiv:2605.03952v1 | SRC-ARXIV@arXiv:2605.03952v1 | https://arxiv.org/html/2605.03952v1 §3 Threat Model; §4 MOSAIC-Bench | https://arxiv.org/html/2605.03952v1 §5 Evaluation Protocol; §6 Results | https://arxiv.org/html/2605.03952v1 §7 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO | https://arxiv.org/html/2605.03952v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-03952 | complete |
| SF-2026-ARXIV-2605-03971 | RP-9d981d8bfd420198 | deep | arXiv:2605.03971v1 | SRC-ARXIV@arXiv:2605.03971v1 | https://arxiv.org/html/2605.03971v1 §4 LaaB Logical-Constraint Framework | https://arxiv.org/html/2605.03971v1 §5 Experiments and Effect Analysis | https://arxiv.org/html/2605.03971v1 §6 Limitations; Appendix; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO | https://arxiv.org/html/2605.03971v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-03971 | complete |
| SF-2026-ARXIV-2605-03986 | RP-64278046164a8b22 | deep | arXiv:2605.03986v1 | SRC-ARXIV@arXiv:2605.03986v1 | https://arxiv.org/html/2605.03986v1 §3 Intent-to-Workflow Composition; §4 Agent Recommendation | https://arxiv.org/html/2605.03986v1 §5 Evaluation | https://arxiv.org/html/2605.03986v1 §6 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO | https://arxiv.org/html/2605.03986v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-03986 | complete |
| SF-2026-ARXIV-2605-04018 | RP-446d6d479dee8ed0 | deep | arXiv:2605.04018v1 | SRC-ARXIV@arXiv:2605.04018v1 | https://arxiv.org/html/2605.04018v1 §3 Bright-Pro; §4 Evaluation Protocol; §5 RTriever | https://arxiv.org/html/2605.04018v1 §6 Experiments | https://arxiv.org/html/2605.04018v1 §F Agent Configuration and stated protocol limits; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO | https://arxiv.org/html/2605.04018v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-04018 | complete |
| SF-2026-ARXIV-2605-04019 | RP-704310a5020b5419 | standard | arXiv:2605.04019v1 | SRC-ARXIV@arXiv:2605.04019v1 | https://arxiv.org/html/2605.04019v1 §3 Agent Architecture; §4 Workflow Generation | https://arxiv.org/html/2605.04019v1 §5 Llama Scout Case Study | https://arxiv.org/html/2605.04019v1 §6 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO | https://arxiv.org/html/2605.04019v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-04019 | complete |
| SF-2026-ARXIV-2605-04036 | RP-fc7215b1898e21dc | deep | arXiv:2605.04036v1 | SRC-ARXIV@arXiv:2605.04036v1 | https://arxiv.org/html/2605.04036v1 §3 Trajectory Construction; §4 OpenSeeker-v2 SFT | https://arxiv.org/html/2605.04036v1 §5 Experiments and Ablations | https://arxiv.org/html/2605.04036v1 §6 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO | https://arxiv.org/html/2605.04036v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-04036 | complete |
| SF-2026-ARXIV-2605-04039 | RP-abe5aa120da54c91 | deep | arXiv:2605.04039v1 | SRC-ARXIV@arXiv:2605.04039v1 | https://arxiv.org/html/2605.04039v1 §3 SaFE-Scale Framework; §4 Safety Dimensions | https://arxiv.org/html/2605.04039v1 §5 Scaling Experiments | https://arxiv.org/html/2605.04039v1 §6 Limitations and Clinical Scope; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO | https://arxiv.org/html/2605.04039v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-04039 | complete |
| SF-2026-ARXIV-2605-04116 | RP-6f8587bbc89d9afc | deep | arXiv:2605.04116v1 | SRC-ARXIV@arXiv:2605.04116v1 | https://arxiv.org/html/2605.04116v1 §3 Threat Model; §4 Prefix-Based Membership Attacks | https://arxiv.org/html/2605.04116v1 §5 Experimental Setup; §6 Results | https://arxiv.org/html/2605.04116v1 §7 Defense and Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO | https://arxiv.org/html/2605.04116v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-04116 | complete |
| SF-2026-ARXIV-2605-04135 | RP-47be52f21554d0ef | deep | arXiv:2605.04135v1 | SRC-ARXIV@arXiv:2605.04135v1 | https://arxiv.org/html/2605.04135v1 §2 Frontier-Lag Audit Method; §3 Configuration and Date Coding | https://arxiv.org/html/2605.04135v1 §4 Bibliometric Results | https://arxiv.org/html/2605.04135v1 §5 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO | https://arxiv.org/html/2605.04135v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-04135 | complete |
| SF-2026-ARXIV-2605-04172 | RP-add9e840a64e5cee | deep | arXiv:2605.04172v1 | SRC-ARXIV@arXiv:2605.04172v1 | https://arxiv.org/html/2605.04172v1 §3 täkō Memory Consistency Model; §4 Formal Semantics | https://arxiv.org/html/2605.04172v1 §5 Litmus Tests and Validation | https://arxiv.org/html/2605.04172v1 §6 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO | https://arxiv.org/html/2605.04172v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-04172 | complete |
| SF-2026-ARXIV-2605-04178 | RP-f46586a5d489f85f | deep | arXiv:2605.04178v1 | SRC-ARXIV@arXiv:2605.04178v1 | https://arxiv.org/html/2605.04178v1 §3 Microbenchmark Suite; §4 Analytical Models | https://arxiv.org/html/2605.04178v1 §5 Validation on B200 and MI300A | https://arxiv.org/html/2605.04178v1 §6 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO | https://arxiv.org/html/2605.04178v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-04178 | complete |
| SF-2026-ARXIV-2605-04209 | RP-e59c9bc8a2dc8555 | deep | arXiv:2605.04209v1 | SRC-ARXIV@arXiv:2605.04209v1 | https://arxiv.org/html/2605.04209v1 §3 Sparse Backdoor Construction; §4 Undetectability Analysis | https://arxiv.org/html/2605.04209v1 §5 Experiments | https://arxiv.org/html/2605.04209v1 §6 Limitations and Threat-Model Boundary; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO | https://arxiv.org/html/2605.04209v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-04209 | complete |
| SF-2026-ARXIV-2605-04213 | RP-506a038fc210543d | deep | arXiv:2605.04213v1 | SRC-ARXIV@arXiv:2605.04213v1 | https://arxiv.org/html/2605.04213v1 §3 Gate-Level Fault-Injection Method; §4 SDC Taxonomy | https://arxiv.org/html/2605.04213v1 §5 Error-Pattern Results; §6 Modeling Guidance | https://arxiv.org/html/2605.04213v1 §7 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO | https://arxiv.org/html/2605.04213v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-04213 | complete |
| SF-2026-ARXIV-2605-04215 | RP-15c1dce810e38888 | deep | arXiv:2605.04215v1 | SRC-ARXIV@arXiv:2605.04215v1 | https://arxiv.org/html/2605.04215v1 §3 Predict-then-Diffuse; §3.1 Adaptive Response Length Predictor | https://arxiv.org/html/2605.04215v1 §4 Experiments | https://arxiv.org/html/2605.04215v1 §5 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO | https://arxiv.org/html/2605.04215v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-04215 | complete |
| SF-2026-ARXIV-2605-04236 | RP-071f693e5ba5940f | deep | arXiv:2605.04236v1 | SRC-ARXIV@arXiv:2605.04236v1 | https://arxiv.org/html/2605.04236v1 §3 DASE Sequential Evidence Accumulation; §3.3 Commit Routing | https://arxiv.org/html/2605.04236v1 §4 Experiments and Calibration | https://arxiv.org/html/2605.04236v1 §5 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO | https://arxiv.org/html/2605.04236v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-04236 | complete |
| SF-2026-ARXIV-2605-04256 | RP-1dedbce653caaf3a | deep | arXiv:2605.04256v1 | SRC-ARXIV@arXiv:2605.04256v1 | https://arxiv.org/html/2605.04256v1 §3 phys-MCP Control Plane; §4 Resource and Capability Model | https://arxiv.org/html/2605.04256v1 §5 Prototype Evaluation | https://arxiv.org/html/2605.04256v1 §6 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO | https://arxiv.org/html/2605.04256v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-04256 | complete |
| SF-2026-ARXIV-2605-04263 | RP-9ac69b0de251f20d | deep | arXiv:2605.04263v1 | SRC-ARXIV@arXiv:2605.04263v1 | https://arxiv.org/html/2605.04263v1 §3 PARSE; §3.2 Parallel Prefix Verification | https://arxiv.org/html/2605.04263v1 §4 Experiments and Ablations | https://arxiv.org/html/2605.04263v1 §5 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO | https://arxiv.org/html/2605.04263v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-04263 | complete |
| SF-2026-ARXIV-2605-04264 | RP-584dcb5c24f37bf5 | deep | arXiv:2605.04264v1 | SRC-ARXIV@arXiv:2605.04264v1 | https://arxiv.org/pdf/2605.04264v1 PDF §2 Selection Regimes; §3 Layered Memory Architecture | https://arxiv.org/pdf/2605.04264v1 PDF §4 Documented Traces | https://arxiv.org/pdf/2605.04264v1 PDF §5 Limitations and Design Agenda; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO | https://arxiv.org/pdf/2605.04264v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-04264 | complete |
| SF-2026-ARXIV-2605-04266 | RP-c7d6818f1b8eb296 | deep | arXiv:2605.04266v1 | SRC-ARXIV@arXiv:2605.04266v1 | https://arxiv.org/html/2605.04266v1 §3 Stackelberg Formulation; §4 Gradient Decomposition; §5 FPO | https://arxiv.org/html/2605.04266v1 §6 Experiments | https://arxiv.org/html/2605.04266v1 §7 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO | https://arxiv.org/html/2605.04266v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-04266 | complete |
| SF-2026-ARXIV-2605-04269 | RP-dc3b4fca867afce2 | deep | arXiv:2605.04269v1 | SRC-ARXIV@arXiv:2605.04269v1 | https://arxiv.org/html/2605.04269v1 §3 Nonstationary Adam Analysis; §4 Tracking and Stationarity Bounds | https://arxiv.org/html/2605.04269v1 §5 Experiments | https://arxiv.org/html/2605.04269v1 §6 Assumptions and Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO | https://arxiv.org/html/2605.04269v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-04269 | complete |
| SF-2026-ARXIV-2605-04295 | RP-5b63c21f2bc75ae1 | deep | arXiv:2605.04295v1 | SRC-ARXIV@arXiv:2605.04295v1 | https://arxiv.org/html/2605.04295v1 §2 Semantic Entropy; §3 Adaptive Conformal Semantic Entropy | https://arxiv.org/html/2605.04295v1 §4 Evaluation and Ablations | https://arxiv.org/html/2605.04295v1 §5 Limitations; Appendix Proofs; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO | https://arxiv.org/html/2605.04295v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-04295 | complete |
| SF-2026-ARXIV-2605-04312 | RP-ab661eb5f65dda31 | deep | arXiv:2605.04312v1 | SRC-ARXIV@arXiv:2605.04312v1 | https://arxiv.org/html/2605.04312v1 §3 Agent Island Environment; §4 Dynamic Evaluation Protocol | https://arxiv.org/html/2605.04312v1 §5 Experiments | https://arxiv.org/html/2605.04312v1 §6 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO | https://arxiv.org/html/2605.04312v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-04312 | complete |
| SF-2026-ARXIV-2605-04333 | RP-629285c7e6d2d163 | deep | arXiv:2605.04333v1 | SRC-ARXIV@arXiv:2605.04333v1 | https://arxiv.org/html/2605.04333v1 §2 MRC Transport; §3 Multi-Plane Clos and SRv6 | https://arxiv.org/html/2605.04333v1 §4 Simulation and Evaluation | https://arxiv.org/html/2605.04333v1 §5 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO | https://arxiv.org/html/2605.04333v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-04333 | complete |
| SF-2026-ARXIV-2605-04341 | RP-579b5331d34c807d | deep | arXiv:2605.04341v1 | SRC-ARXIV@arXiv:2605.04341v1 | https://arxiv.org/html/2605.04341v1 §3 Budgeted LoRA; §3.2 Structured Compute Allocation | https://arxiv.org/html/2605.04341v1 §4 Experiments and Pareto Analysis | https://arxiv.org/html/2605.04341v1 §5 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO | https://arxiv.org/html/2605.04341v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-04341 | complete |
| SF-2026-ARXIV-2605-04357 | RP-bc365b6b63163e90 | deep | arXiv:2605.04357v1 | SRC-ARXIV@arXiv:2605.04357v1 | https://arxiv.org/html/2605.04357v1 §3 Multi-LLM Serving Problem; §4 Optimization; §5 Runtime | https://arxiv.org/html/2605.04357v1 §6 Evaluation | https://arxiv.org/html/2605.04357v1 §6.7 Sensitivity and §8 scope boundary; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO | https://arxiv.org/html/2605.04357v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-04357 | complete |
| SF-2026-ARXIV-2605-04361 | RP-7cd96ba3b20d9a84 | deep | arXiv:2605.04361v1 | SRC-ARXIV@arXiv:2605.04361v1 | https://arxiv.org/html/2605.04361v1 §3 Multi-Agent Design-Exploration Protocol; §4 Context Conditions | https://arxiv.org/html/2605.04361v1 §5 Crossover Results | https://arxiv.org/html/2605.04361v1 §6 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO | https://arxiv.org/html/2605.04361v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-04361 | complete |
| SF-2026-ARXIV-2605-04373 | RP-66ce0bc9081a80ea | deep | arXiv:2605.04373v1 | SRC-ARXIV@arXiv:2605.04373v1 | https://arxiv.org/html/2605.04373v1 §3 Regret-Maximization Discovery; §4 Runtime Protection | https://arxiv.org/html/2605.04373v1 §5 Evaluation | https://arxiv.org/html/2605.04373v1 §6 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO | https://arxiv.org/html/2605.04373v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-04373 | complete |
| SF-2026-ARXIV-2605-04375 | RP-63311e33aa11b0ab | deep | arXiv:2605.04375v1 | SRC-ARXIV@arXiv:2605.04375v1 | https://arxiv.org/html/2605.04375v1 §3 Experiment-as-Code Model; §4 Declarative Lab Stack | https://arxiv.org/html/2605.04375v1 §5 Case Studies and Evaluation | https://arxiv.org/html/2605.04375v1 §6 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO | https://arxiv.org/html/2605.04375v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-04375 | complete |
| SF-2026-ARXIV-2605-05248 | RP-e1ffce301f09f50b | deep | arXiv:2605.05248v1 | SRC-ARXIV@arXiv:2605.05248v1 | https://arxiv.org/html/2605.05248v1 §3 Governed Metaprogramming; §4 Pure Form Evaluation; §5 Governed Materialization | https://arxiv.org/html/2605.05248v1 §7 Implementation and Evaluation | https://arxiv.org/html/2605.05248v1 §8 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO | https://arxiv.org/html/2605.05248v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-05248 | complete |
| SF-2026-ARXIV-2605-05253 | RP-261686ab49810439 | deep | arXiv:2605.05253v1 | SRC-ARXIV@arXiv:2605.05253v1 | https://arxiv.org/html/2605.05253v1 §3 EnterpriseRAG-Bench Construction | https://arxiv.org/html/2605.05253v1 §4 Evaluation Protocol; §5 Results | https://arxiv.org/html/2605.05253v1 §6 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO | https://arxiv.org/html/2605.05253v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-05253 | complete |
| SF-2026-ARXIV-2605-08190 | RP-d306523679199521 | deep | arXiv:2605.08190v1 | SRC-ARXIV@arXiv:2605.08190v1 | https://arxiv.org/html/2605.08190v1 §3 Synergistic Simplex Architecture; §4 Safety Conditions | https://arxiv.org/html/2605.08190v1 §5 Autonomous-Vehicle Evaluation | https://arxiv.org/html/2605.08190v1 §6 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO | https://arxiv.org/html/2605.08190v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-08190 | complete |
| SF-2026-ARXIV-2605-08192 | RP-b51b2cc65ac40119 | deep | arXiv:2605.08192v1 | SRC-ARXIV@arXiv:2605.08192v1 | https://arxiv.org/html/2605.08192v1 §2 Evidential Inversion; §3 Proposed Reproducibility Standard | https://arxiv.org/html/2605.08192v1 §4 Worked Requirements and Cases | https://arxiv.org/html/2605.08192v1 §5 Limitations and Governance Scope; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO | https://arxiv.org/html/2605.08192v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-08192 | complete |
| SF-2026-ARXIV-2605-08195 | RP-19f7c035406c1f5a | deep | arXiv:2605.08195v1 | SRC-ARXIV@arXiv:2605.08195v1 | https://arxiv.org/html/2605.08195v1 §2 ExecuTorch Architecture; §3 Export and Delegation; §4 Runtime | https://arxiv.org/html/2605.08195v1 §5 Evaluation | https://arxiv.org/html/2605.08195v1 §6 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO | https://arxiv.org/html/2605.08195v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-08195 | complete |
| SF-2026-ARXIV-2605-10959 | RP-1c1527e6553a9f33 | standard | arXiv:2605.10959v1 | SRC-ARXIV@arXiv:2605.10959v1 | https://arxiv.org/html/2605.10959v1 §3 QuIDE Metric and Active Optimization | https://arxiv.org/html/2605.10959v1 §4 Experiments | https://arxiv.org/html/2605.10959v1 §5 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO | https://arxiv.org/html/2605.10959v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-10959 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2605-03275:start -->
#### Beyond Similarity Search: A Unified Data Layer for Production RAG Systems

官方 arXiv body 在执行环境中仍无法直接下载，但带相同 title、authors、arXiv DOI、CC BY 与 May 2026 manuscript identity 的公开全文镜像恢复了正文。系统机制不是“PostgreSQL 总是更快”，而是把 document、embedding、metadata 与 access policy 放回同一 transaction/query owner，使 freshness 与 authorization 在 candidate admission 前成立；split path 则把同步、join 与 filter failure 推给应用层。

Evaluation contract 为 50,000 documents、128-dimensional embeddings、20 tenants、5 categories、180-day distribution、每类 200 queries，报告 p50/p95/p99；runtime 是 PostgreSQL 16、pgvector 0.6.0 与 HNSW。关键反证是 Stack A 只在 PostgreSQL 内模拟 split-system table/merge，并非真实 Pinecone、Qdrant 或 Milvus；论文也明确承认 50k corpus 很小，并保留 pure ANN、超大规模 specialized store 与 hybrid hot/warm/cold tier 的成立边界。

<!-- claim:SF-2026-ARXIV-2605-03275:start -->结论只支持“freshness、tenant authorization 与 composed retrieval 是 data-layer state/transaction ownership 问题”，不接受 92%/74% 等作者数字为通用性能承诺，也不把受控模拟外推为外部向量数据库的比较结论。<!-- claim:SF-2026-ARXIV-2605-03275:end -->
<!-- review:SF-2026-ARXIV-2605-03275:end -->

<!-- review:SF-2026-ARXIV-2605-03309:start -->
#### Cryptographic Registry Provenance: Structural Defense Against Dependency Confusion in AI Package Ecosystems

问题与旧路径：旧路径在固定 workload、低风险或规模较小时仍可用。约束变化与机制：artifact distribution needs cryptographic registry identity, publisher/registry countersignatures and namespace-bound fail-closed resolution。Method：`https://arxiv.org/html/2605.03309v1 §4 Two-Layer Archive Format; §5 Cryptographic Registry Identity; §6 Dual-Signature Distribution Model`。

Evaluation：`https://arxiv.org/html/2605.03309v1 §12 Evaluation`。Counterevidence/limits：`https://arxiv.org/html/2605.03309v1 §13.1 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO`。Artifact：`https://arxiv.org/html/2605.03309v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。

<!-- claim:SF-2026-ARXIV-2605-03309:start -->长期结论只限 exact-v1 披露边界，不把作者 benchmark 外推到未测模型、硬件、精度、长度、batch、并发或 SLO。<!-- claim:SF-2026-ARXIV-2605-03309:end -->
<!-- review:SF-2026-ARXIV-2605-03309:end -->

<!-- review:SF-2026-ARXIV-2605-03310:start -->
#### Coordination as an Architectural Layer for LLM-Based Multi-Agent Systems

问题与旧路径：旧路径在固定 workload、低风险或规模较小时仍可用。约束变化与机制：multi-agent coordination is a configurable architecture whose information topology, compute allocation and aggregation leave distinct failure signatures。Method：`https://arxiv.org/html/2605.03310v1 §3 Coordination as an Architectural Layer; §4 Reference Architectures`。

Evaluation：`https://arxiv.org/html/2605.03310v1 §5 Experimental Design; §6 Results`。Counterevidence/limits：`https://arxiv.org/html/2605.03310v1 §7 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO`。Artifact：`https://arxiv.org/html/2605.03310v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。

<!-- claim:SF-2026-ARXIV-2605-03310:start -->长期结论只限 exact-v1 披露边界，不把作者 benchmark 外推到未测模型、硬件、精度、长度、batch、并发或 SLO。<!-- claim:SF-2026-ARXIV-2605-03310:end -->
<!-- review:SF-2026-ARXIV-2605-03310:end -->

<!-- review:SF-2026-ARXIV-2605-03312:start -->
#### MemFlow: Intent-Driven Memory Orchestration for Small Language Model Agents

问题与旧路径：旧路径在固定 workload、低风险或规模较小时仍可用。约束变化与机制：limited-capacity agents need intent-routed memory tiers, deterministic evidence compilation and validator-owned escalation instead of open-ended memory tool loops。Method：`https://arxiv.org/html/2605.03312v1 §3 MemFlow Architecture; §4 Intent Router and Memory Tiers`。

Evaluation：`https://arxiv.org/html/2605.03312v1 §5 Experiments`。Counterevidence/limits：`https://arxiv.org/html/2605.03312v1 §6 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO`。Artifact：`https://arxiv.org/html/2605.03312v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。

<!-- claim:SF-2026-ARXIV-2605-03312:start -->长期结论只限 exact-v1 披露边界，不把作者 benchmark 外推到未测模型、硬件、精度、长度、batch、并发或 SLO。<!-- claim:SF-2026-ARXIV-2605-03312:end -->
<!-- review:SF-2026-ARXIV-2605-03312:end -->

<!-- review:SF-2026-ARXIV-2605-03314:start -->
#### When to Think, When to Speak: Learning Disclosure Policies for LLM Reasoning

问题与旧路径：旧路径在固定 workload、低风险或规模较小时仍可用。约束变化与机制：public disclosure is an irreversible commitment distinct from private reasoning state, so visibility timing becomes a learned control decision with an entailment gate。Method：`https://arxiv.org/html/2605.03314v1 §2 Generation under Coupled State and Commitment; §3 Method`。

Evaluation：`https://arxiv.org/html/2605.03314v1 §4 Experiments`。Counterevidence/limits：`https://arxiv.org/html/2605.03314v1 §F Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO`。Artifact：`https://arxiv.org/html/2605.03314v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。

<!-- claim:SF-2026-ARXIV-2605-03314:start -->长期结论只限 exact-v1 披露边界，不把作者 benchmark 外推到未测模型、硬件、精度、长度、batch、并发或 SLO。<!-- claim:SF-2026-ARXIV-2605-03314:end -->
<!-- review:SF-2026-ARXIV-2605-03314:end -->

<!-- review:SF-2026-ARXIV-2605-03327:start -->
#### DGPO: Distribution Guided Policy Optimization for Fine Grained Credit Assignment

问题与旧路径：旧路径在固定 workload、低风险或规模较小时仍可用。约束变化与机制：fine-grained reasoning credit can be redistributed from sequence reward with a bounded distributional distance and an entropy gate, trading additional statistics and calibration for less diffuse token updates。Method：`https://arxiv.org/html/2605.03327v1 §3 Distribution-Guided Policy Optimization; §3.2 Advantage Redistribution; §3.3 Objective`。

Evaluation：`https://arxiv.org/html/2605.03327v1 §4 Experiments and Ablations`。Counterevidence/limits：`https://arxiv.org/html/2605.03327v1 Appendix A Theory; Appendix B Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO`。Artifact：`https://arxiv.org/html/2605.03327v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。

<!-- claim:SF-2026-ARXIV-2605-03327:start -->长期结论只限 exact-v1 披露边界，不把作者 benchmark 外推到未测模型、硬件、精度、长度、batch、并发或 SLO。<!-- claim:SF-2026-ARXIV-2605-03327:end -->
<!-- review:SF-2026-ARXIV-2605-03327:end -->

<!-- review:SF-2026-ARXIV-2605-03353:start -->
#### SkCC: Portable and Secure Skill Compilation for Cross-Framework LLM Agents

问题与旧路径：旧路径在固定 workload、低风险或规模较小时仍可用。约束变化与机制：portable skills require a typed intermediate representation and target-specific lowering, while static checks remain separate from runtime effect authorization。Method：`https://arxiv.org/html/2605.03353v1 §3 SkIR; §4 Four-Phase Compilation Pipeline`。

Evaluation：`https://arxiv.org/html/2605.03353v1 §5 Evaluation`。Counterevidence/limits：`https://arxiv.org/html/2605.03353v1 §6 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO`。Artifact：`https://arxiv.org/html/2605.03353v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。

<!-- claim:SF-2026-ARXIV-2605-03353:start -->长期结论只限 exact-v1 披露边界，不把作者 benchmark 外推到未测模型、硬件、精度、长度、batch、并发或 SLO。<!-- claim:SF-2026-ARXIV-2605-03353:end -->
<!-- review:SF-2026-ARXIV-2605-03353:end -->

<!-- review:SF-2026-ARXIV-2605-03354:start -->
#### What Happens Inside Agent Memory? Circuit Analysis from Emergence to Diagnosis

问题与旧路径：旧路径在固定 workload、低风险或规模较小时仍可用。约束变化与机制：memory write/read failures can be localized through stage-specific internal circuits, but circuit signals remain diagnostics rather than durable memory truth。Method：`https://arxiv.org/html/2605.03354v1 §3 Circuit Tracing Method; §4 Write-Manage-Read Circuits`。

Evaluation：`https://arxiv.org/html/2605.03354v1 §5 Experiments; §6 Diagnosis`。Counterevidence/limits：`https://arxiv.org/html/2605.03354v1 §7 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO`。Artifact：`https://arxiv.org/html/2605.03354v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。

<!-- claim:SF-2026-ARXIV-2605-03354:start -->长期结论只限 exact-v1 披露边界，不把作者 benchmark 外推到未测模型、硬件、精度、长度、batch、并发或 SLO。<!-- claim:SF-2026-ARXIV-2605-03354:end -->
<!-- review:SF-2026-ARXIV-2605-03354:end -->

<!-- review:SF-2026-ARXIV-2605-03375:start -->
#### Tutti: Making SSD-Backed KV Cache Practical for Long-Context LLM Serving

问题与旧路径：旧路径在固定 workload、低风险或规模较小时仍可用。约束变化与机制：SSD-backed KV restore must move both data and I/O submission ownership off the CPU critical path and schedule transfers against GPU slack。Method：`https://arxiv.org/html/2605.03375v1 §3 GPU-Centric KV Object Store; §4 GPU io_uring; §5 Slack-Aware Scheduling`。

Evaluation：`https://arxiv.org/html/2605.03375v1 §7 Evaluation`。Counterevidence/limits：`https://arxiv.org/html/2605.03375v1 §8 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO`。Artifact：`https://arxiv.org/html/2605.03375v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。

<!-- claim:SF-2026-ARXIV-2605-03375:start -->长期结论只限 exact-v1 披露边界，不把作者 benchmark 外推到未测模型、硬件、精度、长度、batch、并发或 SLO。<!-- claim:SF-2026-ARXIV-2605-03375:end -->
<!-- review:SF-2026-ARXIV-2605-03375:end -->

<!-- review:SF-2026-ARXIV-2605-03378:start -->
#### ARGUS: Defending LLM Agents Against Context-Aware Prompt Injection

问题与旧路径：旧路径在固定 workload、低风险或规模较小时仍可用。约束变化与机制：an agent action should commit only when benign evidence provides a complete causal justification and task invariants hold。Method：`https://arxiv.org/html/2605.03378v1 §3 Threat Model; §4 ARGUS Causal-Provenance Auditor`。

Evaluation：`https://arxiv.org/html/2605.03378v1 §5 AgentLure; §6 Evaluation`。Counterevidence/limits：`https://arxiv.org/html/2605.03378v1 §7 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO`。Artifact：`https://arxiv.org/html/2605.03378v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。

<!-- claim:SF-2026-ARXIV-2605-03378:start -->长期结论只限 exact-v1 披露边界，不把作者 benchmark 外推到未测模型、硬件、精度、长度、batch、并发或 SLO。<!-- claim:SF-2026-ARXIV-2605-03378:end -->
<!-- review:SF-2026-ARXIV-2605-03378:end -->

<!-- review:SF-2026-ARXIV-2605-03379:start -->
#### Two Calls, Two Moments, and the Vote-Accuracy Curve of Repeated LLM Inference

问题与旧路径：旧路径在固定 workload、低风险或规模较小时仍可用。约束变化与机制：test-time vote accuracy is governed by the latent per-example success distribution and same-example correlation, so one-call accuracy cannot specify a repeated-sampling evaluation contract。Method：`https://arxiv.org/html/2605.03379v1 §2 Latent Success Model; §3 Two-Call Identification`。

Evaluation：`https://arxiv.org/html/2605.03379v1 §4 Vote-Accuracy Curves; §5 Empirical Evaluation`。Counterevidence/limits：`https://arxiv.org/html/2605.03379v1 §6 Scope and Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO`。Artifact：`https://arxiv.org/html/2605.03379v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。

<!-- claim:SF-2026-ARXIV-2605-03379:start -->长期结论只限 exact-v1 披露边界，不把作者 benchmark 外推到未测模型、硬件、精度、长度、batch、并发或 SLO。<!-- claim:SF-2026-ARXIV-2605-03379:end -->
<!-- review:SF-2026-ARXIV-2605-03379:end -->

<!-- review:SF-2026-ARXIV-2605-03408:start -->
#### Discovering Reinforcement Learning Interfaces with Large Language Models

问题与旧路径：旧路径在固定 workload、低风险或规模较小时仍可用。约束变化与机制：an RL task interface jointly owns observation projection and reward rather than treating reward synthesis as an isolated prompt problem; generated interfaces still require environment-grounded validation。Method：`https://arxiv.org/html/2605.03408v1 §3 RL Interface Discovery; §3.2 Observation and Reward Synthesis`。

Evaluation：`https://arxiv.org/html/2605.03408v1 §4 Experimental Setup; §5 Results`。Counterevidence/limits：`https://arxiv.org/html/2605.03408v1 §6 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO`。Artifact：`https://arxiv.org/html/2605.03408v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。

<!-- claim:SF-2026-ARXIV-2605-03408:start -->长期结论只限 exact-v1 披露边界，不把作者 benchmark 外推到未测模型、硬件、精度、长度、batch、并发或 SLO。<!-- claim:SF-2026-ARXIV-2605-03408:end -->
<!-- review:SF-2026-ARXIV-2605-03408:end -->

<!-- review:SF-2026-ARXIV-2605-03425:start -->
#### FIBER: A Differentially Private Optimizer with Filter-Aware Innovation Bias Correction

问题与旧路径：旧路径在固定 workload、低风险或规模较小时仍可用。约束变化与机制：gradient filtering under differential privacy changes the noise statistics consumed by AdamW state, so optimizer bias correction must be derived from the filter rather than reused from unfiltered DP-SGD。Method：`https://arxiv.org/html/2605.03425v1 §3 Filter-Aware Innovation Bias Correction; §4 FIBER`。

Evaluation：`https://arxiv.org/html/2605.03425v1 §5 Experiments and Ablations`。Counterevidence/limits：`https://arxiv.org/html/2605.03425v1 §6 Limitations and Privacy Scope; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO`。Artifact：`https://arxiv.org/html/2605.03425v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。

<!-- claim:SF-2026-ARXIV-2605-03425:start -->长期结论只限 exact-v1 披露边界，不把作者 benchmark 外推到未测模型、硬件、精度、长度、batch、并发或 SLO。<!-- claim:SF-2026-ARXIV-2605-03425:end -->
<!-- review:SF-2026-ARXIV-2605-03425:end -->

<!-- review:SF-2026-ARXIV-2605-03482:start -->
#### MEMSAD: Gradient-Coupled Anomaly Detection for Memory Poisoning in Retrieval-Augmented Agents

问题与旧路径：旧路径在固定 workload、低风险或规模较小时仍可用。约束变化与机制：persistent memory poisoning needs calibrated anomaly admission tied to retrieval geometry, with synonym-invariant attacks kept as an explicit non-covered boundary。Method：`https://arxiv.org/html/2605.03482v1 §3 Stackelberg Threat Model; §4 MEMSAD`。

Evaluation：`https://arxiv.org/html/2605.03482v1 §5 Theory; §6 Experiments`。Counterevidence/limits：`https://arxiv.org/html/2605.03482v1 §7 Limitations and Discrete Loophole; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO`。Artifact：`https://arxiv.org/html/2605.03482v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。

<!-- claim:SF-2026-ARXIV-2605-03482:start -->长期结论只限 exact-v1 披露边界，不把作者 benchmark 外推到未测模型、硬件、精度、长度、batch、并发或 SLO。<!-- claim:SF-2026-ARXIV-2605-03482:end -->
<!-- review:SF-2026-ARXIV-2605-03482:end -->

<!-- review:SF-2026-ARXIV-2605-03505:start -->
#### LATS-RCA: Language Agent Tree Search for Root Cause Analysis in Microservices

问题与旧路径：旧路径在固定 workload、低风险或规模较小时仍可用。约束变化与机制：microservice diagnosis can branch over competing causal hypotheses and use reflection to allocate investigation, but an agent search trace does not replace telemetry identity or causal observability。Method：`https://arxiv.org/html/2605.03505v1 §3 LATS-RCA Architecture; §3.2 Reflection-Guided Tree Search`。

Evaluation：`https://arxiv.org/html/2605.03505v1 §4 Experimental Setup; §5 Results`。Counterevidence/limits：`https://arxiv.org/html/2605.03505v1 §6 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO`。Artifact：`https://arxiv.org/html/2605.03505v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。

<!-- claim:SF-2026-ARXIV-2605-03505:start -->长期结论只限 exact-v1 披露边界，不把作者 benchmark 外推到未测模型、硬件、精度、长度、batch、并发或 SLO。<!-- claim:SF-2026-ARXIV-2605-03505:end -->
<!-- review:SF-2026-ARXIV-2605-03505:end -->

<!-- review:SF-2026-ARXIV-2605-03534:start -->
#### SURE-RAG: Sufficiency and Uncertainty-Aware Evidence Verification for Selective Retrieval-Augmented Generation

问题与旧路径：旧路径在固定 workload、低风险或规模较小时仍可用。约束变化与机制：evidence sufficiency is a set-level claim contract over coverage, relation, conflict and uncertainty, not independent passage relevance。Method：`https://arxiv.org/html/2605.03534v1 §3 SURE-RAG; §4 Set-Level Aggregation`。

Evaluation：`https://arxiv.org/html/2605.03534v1 §5 Experimental Protocol; §6 Results`。Counterevidence/limits：`https://arxiv.org/html/2605.03534v1 §7 Boundary Mapping and Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO`。Artifact：`https://arxiv.org/html/2605.03534v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。

<!-- claim:SF-2026-ARXIV-2605-03534:start -->长期结论只限 exact-v1 披露边界，不把作者 benchmark 外推到未测模型、硬件、精度、长度、batch、并发或 SLO。<!-- claim:SF-2026-ARXIV-2605-03534:end -->
<!-- review:SF-2026-ARXIV-2605-03534:end -->

<!-- review:SF-2026-ARXIV-2605-03561:start -->
#### Enhancing Performance Insight at Scale: A Heterogeneous Framework for Exascale Diagnostics

问题与旧路径：旧路径在固定 workload、低风险或规模较小时仍可用。约束变化与机制：exascale diagnostic analysis must separate telemetry ingestion, GPU-parallel analysis and presentation so monitoring overhead scales below the workload being observed。Method：`https://arxiv.org/html/2605.03561v1 §3 Heterogeneous hpcanalysis Framework; §4 C++ and GPU Paths`。

Evaluation：`https://arxiv.org/html/2605.03561v1 §5 Evaluation on Aurora`。Counterevidence/limits：`https://arxiv.org/html/2605.03561v1 §6 Limitations and Portability Boundary; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO`。Artifact：`https://arxiv.org/html/2605.03561v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。

<!-- claim:SF-2026-ARXIV-2605-03561:start -->长期结论只限 exact-v1 披露边界，不把作者 benchmark 外推到未测模型、硬件、精度、长度、batch、并发或 SLO。<!-- claim:SF-2026-ARXIV-2605-03561:end -->
<!-- review:SF-2026-ARXIV-2605-03561:end -->

<!-- review:SF-2026-ARXIV-2605-03562:start -->
#### HeadQ: Model-Visible Distortion and Score-Space Correction for KV-Cache Quantization

问题与旧路径：旧路径在固定 workload、低风险或规模较小时仍可用。约束变化与机制：KV quantization error must be measured in attention-visible score/readout coordinates rather than raw storage MSE, with distinct K and V operators。Method：`https://arxiv.org/html/2605.03562v1 §3 Model-Visible KV Geometry; §4 HeadQ`。

Evaluation：`https://arxiv.org/html/2605.03562v1 §2 Experimental Setup; §5 Empirical Results`。Counterevidence/limits：`https://arxiv.org/html/2605.03562v1 §8 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO`。Artifact：`https://arxiv.org/html/2605.03562v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。

<!-- claim:SF-2026-ARXIV-2605-03562:start -->长期结论只限 exact-v1 披露边界，不把作者 benchmark 外推到未测模型、硬件、精度、长度、batch、并发或 SLO。<!-- claim:SF-2026-ARXIV-2605-03562:end -->
<!-- review:SF-2026-ARXIV-2605-03562:end -->

<!-- review:SF-2026-ARXIV-2605-03566:start -->
#### Lifting to tensors when compiling scientific computing workloads for AI Engines

问题与旧路径：旧路径在固定 workload、低风险或规模较小时仍可用。约束变化与机制：compiler lowering to an AI Engine needs tensor-level intermediate structure before hardware-specific mapping; source compatibility is obtained by changing the compiler owner, not by hiding data-movement constraints。Method：`https://arxiv.org/html/2605.03566v1 §3 Tensor Lifting; §4 AIE Lowering Pipeline`。

Evaluation：`https://arxiv.org/html/2605.03566v1 §5 Scientific-Workload Evaluation`。Counterevidence/limits：`https://arxiv.org/html/2605.03566v1 §6 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO`。Artifact：`https://arxiv.org/html/2605.03566v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。

<!-- claim:SF-2026-ARXIV-2605-03566:start -->长期结论只限 exact-v1 披露边界，不把作者 benchmark 外推到未测模型、硬件、精度、长度、batch、并发或 SLO。<!-- claim:SF-2026-ARXIV-2605-03566:end -->
<!-- review:SF-2026-ARXIV-2605-03566:end -->

<!-- review:SF-2026-ARXIV-2605-03596:start -->
#### Workspace-Bench 1.0: Benchmarking AI Agents on Workspace Tasks with Large-Scale File Dependencies

问题与旧路径：旧路径在固定 workload、低风险或规模较小时仍可用。约束变化与机制：workspace-agent evaluation must preserve cross-file dependency state and score both reads and mutations against a real workspace graph rather than treating files as independent prompt attachments。Method：`https://arxiv.org/html/2605.03596v1 §3 Workspace-Bench Construction; §4 Dependency and Task Model`。

Evaluation：`https://arxiv.org/html/2605.03596v1 §5 Evaluation Protocol; §6 Results`。Counterevidence/limits：`https://arxiv.org/html/2605.03596v1 §7 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO`。Artifact：`https://arxiv.org/html/2605.03596v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。

<!-- claim:SF-2026-ARXIV-2605-03596:start -->长期结论只限 exact-v1 披露边界，不把作者 benchmark 外推到未测模型、硬件、精度、长度、batch、并发或 SLO。<!-- claim:SF-2026-ARXIV-2605-03596:end -->
<!-- review:SF-2026-ARXIV-2605-03596:end -->

<!-- review:SF-2026-ARXIV-2605-03644:start -->
#### AdapShot: Adaptive Many-Shot In-Context Learning with Semantic-Aware KV Cache Reuse

问题与旧路径：旧路径在固定 workload、低风险或规模较小时仍可用。约束变化与机制：adaptive many-shot inference couples example selection with reusable prefix KV state, making context admission a joint quality-memory-latency decision rather than a fixed shot count。Method：`https://arxiv.org/html/2605.03644v1 §3 AdapShot; §3.2 Adaptive Shot Selection; §3.3 Semantic-Aware KV Reuse`。

Evaluation：`https://arxiv.org/html/2605.03644v1 §4 Experiments and Ablations`。Counterevidence/limits：`https://arxiv.org/html/2605.03644v1 §5 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO`。Artifact：`https://arxiv.org/html/2605.03644v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。

<!-- claim:SF-2026-ARXIV-2605-03644:start -->长期结论只限 exact-v1 披露边界，不把作者 benchmark 外推到未测模型、硬件、精度、长度、batch、并发或 SLO。<!-- claim:SF-2026-ARXIV-2605-03644:end -->
<!-- review:SF-2026-ARXIV-2605-03644:end -->

<!-- review:SF-2026-ARXIV-2605-03667:start -->
#### ELAS: Efficient Pre-Training of Low-Rank Large Language Models via 2:4 Activation Sparsity

问题与旧路径：旧路径在固定 workload、低风险或规模较小时仍可用。约束变化与机制：low-rank pretraining becomes hardware-useful only when the factorization is co-designed with supported structured activation sparsity; mathematical compression alone does not guarantee realized training throughput。Method：`https://arxiv.org/html/2605.03667v1 §3 ELAS Low-Rank and 2:4 Sparse Training`。

Evaluation：`https://arxiv.org/html/2605.03667v1 §4 Experiments and Ablations`。Counterevidence/limits：`https://arxiv.org/html/2605.03667v1 §5 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO`。Artifact：`https://arxiv.org/html/2605.03667v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。

<!-- claim:SF-2026-ARXIV-2605-03667:start -->长期结论只限 exact-v1 披露边界，不把作者 benchmark 外推到未测模型、硬件、精度、长度、batch、并发或 SLO。<!-- claim:SF-2026-ARXIV-2605-03667:end -->
<!-- review:SF-2026-ARXIV-2605-03667:end -->

<!-- review:SF-2026-ARXIV-2605-03675:start -->
#### MEMTIER: Tiered Memory Architecture and Retrieval Bottleneck Analysis for Long-Running Autonomous AI Agents

问题与旧路径：旧路径在固定 workload、低风险或规模较小时仍可用。约束变化与机制：long-running agent memory needs tiered episodic, semantic and working state plus measured retrieval-bottleneck ownership instead of a flat file。Method：`https://arxiv.org/html/2605.03675v1 §3 MemTier Architecture; §4 Retrieval Engine`。

Evaluation：`https://arxiv.org/html/2605.03675v1 §5 Evaluation`。Counterevidence/limits：`https://arxiv.org/html/2605.03675v1 §6 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO`。Artifact：`https://arxiv.org/html/2605.03675v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。

<!-- claim:SF-2026-ARXIV-2605-03675:start -->长期结论只限 exact-v1 披露边界，不把作者 benchmark 外推到未测模型、硬件、精度、长度、batch、并发或 SLO。<!-- claim:SF-2026-ARXIV-2605-03675:end -->
<!-- review:SF-2026-ARXIV-2605-03675:end -->

<!-- review:SF-2026-ARXIV-2605-03677:start -->
#### Uni-OPD: Unifying On-Policy Distillation with a Dual-Perspective Recipe

问题与旧路径：旧路径在固定 workload、低风险或规模较小时仍可用。约束变化与机制：on-policy distillation needs both exploration of informative student states and reliability-aware teacher supervision, so teacher outputs are conditional feedback rather than unconditional labels。Method：`https://arxiv.org/html/2605.03677v1 §3 Dual-Perspective OPD; §3.2 Exploration; §3.3 Teacher Reliability`。

Evaluation：`https://arxiv.org/html/2605.03677v1 §4 Experiments and Ablations`。Counterevidence/limits：`https://arxiv.org/html/2605.03677v1 §5 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO`。Artifact：`https://arxiv.org/html/2605.03677v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。

<!-- claim:SF-2026-ARXIV-2605-03677:start -->长期结论只限 exact-v1 披露边界，不把作者 benchmark 外推到未测模型、硬件、精度、长度、batch、并发或 SLO。<!-- claim:SF-2026-ARXIV-2605-03677:end -->
<!-- review:SF-2026-ARXIV-2605-03677:end -->

<!-- review:SF-2026-ARXIV-2605-03762:start -->
#### OracleProto: A Reproducible Framework for Benchmarking LLM Native Forecasting via Knowledge Cutoff and Temporal Masking

问题与旧路径：旧路径在固定 workload、低风险或规模较小时仍可用。约束变化与机制：forecast evaluation needs verifiable knowledge cutoffs, temporal masking and artifact provenance so future leakage cannot masquerade as predictive capability。Method：`https://arxiv.org/html/2605.03762v1 §3 OracleProto Protocol; §4 Temporal Masking`。

Evaluation：`https://arxiv.org/html/2605.03762v1 §5 Evaluation`。Counterevidence/limits：`https://arxiv.org/html/2605.03762v1 §6 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO`。Artifact：`https://arxiv.org/html/2605.03762v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。

<!-- claim:SF-2026-ARXIV-2605-03762:start -->长期结论只限 exact-v1 披露边界，不把作者 benchmark 外推到未测模型、硬件、精度、长度、batch、并发或 SLO。<!-- claim:SF-2026-ARXIV-2605-03762:end -->
<!-- review:SF-2026-ARXIV-2605-03762:end -->

<!-- review:SF-2026-ARXIV-2605-03838:start -->
#### TRACE: A Metrologically-Grounded Engineering Framework for Trustworthy Agentic AI Systems in Operationally Critical Domains

问题与旧路径：旧路径在固定 workload、低风险或规模较小时仍可用。约束变化与机制：operationally critical agent evidence needs traceable measurement units, uncertainty budgets and release criteria rather than a single trust score。Method：`https://arxiv.org/html/2605.03838v1 §3 TRACE Measurement Model; §4 Assurance Case`。

Evaluation：`https://arxiv.org/html/2605.03838v1 §5 Worked Evaluation`。Counterevidence/limits：`https://arxiv.org/html/2605.03838v1 §6 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO`。Artifact：`https://arxiv.org/html/2605.03838v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。

<!-- claim:SF-2026-ARXIV-2605-03838:start -->长期结论只限 exact-v1 披露边界，不把作者 benchmark 外推到未测模型、硬件、精度、长度、batch、并发或 SLO。<!-- claim:SF-2026-ARXIV-2605-03838:end -->
<!-- review:SF-2026-ARXIV-2605-03838:end -->

<!-- review:SF-2026-ARXIV-2605-03858:start -->
#### MCJudgeBench: A Benchmark for Constraint-Level Judge Evaluation in Multi-Constraint Instruction Following

问题与旧路径：旧路径在固定 workload、低风险或规模较小时仍可用。约束变化与机制：LLM judges need constraint-level correctness and completeness labels because aggregate verdicts hide which obligation failed。Method：`https://arxiv.org/html/2605.03858v1 §3 MCJudgeBench Construction; §4 Constraint-Level Protocol`。

Evaluation：`https://arxiv.org/html/2605.03858v1 §5 Experiments`。Counterevidence/limits：`https://arxiv.org/html/2605.03858v1 §6 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO`。Artifact：`https://arxiv.org/html/2605.03858v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。

<!-- claim:SF-2026-ARXIV-2605-03858:start -->长期结论只限 exact-v1 披露边界，不把作者 benchmark 外推到未测模型、硬件、精度、长度、batch、并发或 SLO。<!-- claim:SF-2026-ARXIV-2605-03858:end -->
<!-- review:SF-2026-ARXIV-2605-03858:end -->

<!-- review:SF-2026-ARXIV-2605-03862:start -->
#### Correct Is Not Enough: Training Reasoning Planners with Executor-Grounded Rewards

问题与旧路径：旧路径在固定 workload、低风险或规模较小时仍可用。约束变化与机制：planner training should bind reward to executor-observed intermediate state and feasibility, not only a final textual answer。Method：`https://arxiv.org/html/2605.03862v1 §3 Executor-Grounded Reward; §4 Training`。

Evaluation：`https://arxiv.org/html/2605.03862v1 §5 Experiments and Ablations`。Counterevidence/limits：`https://arxiv.org/html/2605.03862v1 §6 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO`。Artifact：`https://arxiv.org/html/2605.03862v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。

<!-- claim:SF-2026-ARXIV-2605-03862:start -->长期结论只限 exact-v1 披露边界，不把作者 benchmark 外推到未测模型、硬件、精度、长度、batch、并发或 SLO。<!-- claim:SF-2026-ARXIV-2605-03862:end -->
<!-- review:SF-2026-ARXIV-2605-03862:end -->

<!-- review:SF-2026-ARXIV-2605-03884:start -->
#### QKVShare: Quantized KV-Cache Handoff for Multi-Agent On-Device LLMs

问题与旧路径：旧路径在固定 workload、低风险或规模较小时仍可用。约束变化与机制：cross-agent latent handoff needs a versioned CacheCard carrying quantized KV state, bit allocation and receiver injection metadata, while prefix alignment and fused execution remain unresolved。Method：`https://arxiv.org/pdf/2605.03884v1 PDF §3 Problem Formulation; §4 QKVShare Method`。

Evaluation：`https://arxiv.org/pdf/2605.03884v1 PDF §5 Experimental Setup; §6 Results`。Counterevidence/limits：`https://arxiv.org/pdf/2605.03884v1 PDF §7 Discussion and Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO`。Artifact：`https://arxiv.org/pdf/2605.03884v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。

<!-- claim:SF-2026-ARXIV-2605-03884:start -->长期结论只限 exact-v1 披露边界，不把作者 benchmark 外推到未测模型、硬件、精度、长度、batch、并发或 SLO。<!-- claim:SF-2026-ARXIV-2605-03884:end -->
<!-- review:SF-2026-ARXIV-2605-03884:end -->

<!-- review:SF-2026-ARXIV-2605-03952:start -->
#### MOSAIC-Bench: Measuring Compositional Vulnerability Induction in Coding Agents

问题与旧路径：旧路径在固定 workload、低风险或规模较小时仍可用。约束变化与机制：coding-agent safety must evaluate cumulative diffs and end-state exploitability across innocuous ticket sequences, not approve each prompt independently。Method：`https://arxiv.org/html/2605.03952v1 §3 Threat Model; §4 MOSAIC-Bench`。

Evaluation：`https://arxiv.org/html/2605.03952v1 §5 Evaluation Protocol; §6 Results`。Counterevidence/limits：`https://arxiv.org/html/2605.03952v1 §7 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO`。Artifact：`https://arxiv.org/html/2605.03952v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。

<!-- claim:SF-2026-ARXIV-2605-03952:start -->长期结论只限 exact-v1 披露边界，不把作者 benchmark 外推到未测模型、硬件、精度、长度、batch、并发或 SLO。<!-- claim:SF-2026-ARXIV-2605-03952:end -->
<!-- review:SF-2026-ARXIV-2605-03952:end -->

<!-- review:SF-2026-ARXIV-2605-03971:start -->
#### Logical Consistency as a Bridge: Improving LLM Hallucination Detection via Label Constraint Modeling between Responses and Self-Judgments

问题与旧路径：旧路径在固定 workload、低风险或规模较小时仍可用。约束变化与机制：hallucination detection can combine response-intrinsic uncertainty with verbal self-judgment through explicit logical constraints, but detector confidence remains an evaluated signal rather than truth。Method：`https://arxiv.org/html/2605.03971v1 §4 LaaB Logical-Constraint Framework`。

Evaluation：`https://arxiv.org/html/2605.03971v1 §5 Experiments and Effect Analysis`。Counterevidence/limits：`https://arxiv.org/html/2605.03971v1 §6 Limitations; Appendix; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO`。Artifact：`https://arxiv.org/html/2605.03971v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。

<!-- claim:SF-2026-ARXIV-2605-03971:start -->长期结论只限 exact-v1 披露边界，不把作者 benchmark 外推到未测模型、硬件、精度、长度、batch、并发或 SLO。<!-- claim:SF-2026-ARXIV-2605-03971:end -->
<!-- review:SF-2026-ARXIV-2605-03971:end -->

<!-- review:SF-2026-ARXIV-2605-03986:start -->
#### From Intent to Execution: Composing Agentic Workflows with Agent Recommendation

问题与旧路径：旧路径在固定 workload、低风险或规模较小时仍可用。约束变化与机制：intent-to-execution automation separates plan synthesis, agent capability recommendation and executable graph construction; each stage requires typed validation before workflow commit。Method：`https://arxiv.org/html/2605.03986v1 §3 Intent-to-Workflow Composition; §4 Agent Recommendation`。

Evaluation：`https://arxiv.org/html/2605.03986v1 §5 Evaluation`。Counterevidence/limits：`https://arxiv.org/html/2605.03986v1 §6 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO`。Artifact：`https://arxiv.org/html/2605.03986v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。

<!-- claim:SF-2026-ARXIV-2605-03986:start -->长期结论只限 exact-v1 披露边界，不把作者 benchmark 外推到未测模型、硬件、精度、长度、batch、并发或 SLO。<!-- claim:SF-2026-ARXIV-2605-03986:end -->
<!-- review:SF-2026-ARXIV-2605-03986:end -->

<!-- review:SF-2026-ARXIV-2605-04018:start -->
#### Rethinking Reasoning-Intensive Retrieval: Evaluating and Advancing Retrievers in Agentic Search Systems

问题与旧路径：旧路径在固定 workload、低风险或规模较小时仍可用。约束变化与机制：reasoning retrieval should optimize complementary evidence portfolios and measure agent-loop completeness, iterations and answer quality under matched budgets。Method：`https://arxiv.org/html/2605.04018v1 §3 Bright-Pro; §4 Evaluation Protocol; §5 RTriever`。

Evaluation：`https://arxiv.org/html/2605.04018v1 §6 Experiments`。Counterevidence/limits：`https://arxiv.org/html/2605.04018v1 §F Agent Configuration and stated protocol limits; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO`。Artifact：`https://arxiv.org/html/2605.04018v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。

<!-- claim:SF-2026-ARXIV-2605-04018:start -->长期结论只限 exact-v1 披露边界，不把作者 benchmark 外推到未测模型、硬件、精度、长度、batch、并发或 SLO。<!-- claim:SF-2026-ARXIV-2605-04018:end -->
<!-- review:SF-2026-ARXIV-2605-04018:end -->

<!-- review:SF-2026-ARXIV-2605-04019:start -->
#### Redefining AI Red Teaming in the Agentic Era: From Weeks to Hours

问题与旧路径：旧路径在固定 workload、低风险或规模较小时仍可用。约束变化与机制：red-team workflow generation can reduce operator setup cost, but attack libraries and a single target case do not establish adaptive security coverage。Method：`https://arxiv.org/html/2605.04019v1 §3 Agent Architecture; §4 Workflow Generation`。

Evaluation：`https://arxiv.org/html/2605.04019v1 §5 Llama Scout Case Study`。Counterevidence/limits：`https://arxiv.org/html/2605.04019v1 §6 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO`。Artifact：`https://arxiv.org/html/2605.04019v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。

<!-- claim:SF-2026-ARXIV-2605-04019:start -->长期结论只限 exact-v1 披露边界，不把作者 benchmark 外推到未测模型、硬件、精度、长度、batch、并发或 SLO。<!-- claim:SF-2026-ARXIV-2605-04019:end -->
<!-- review:SF-2026-ARXIV-2605-04019:end -->

<!-- review:SF-2026-ARXIV-2605-04036:start -->
#### OpenSeeker-v2: Pushing the Limits of Search Agents with Informative and High-Difficulty Trajectories

问题与旧路径：旧路径在固定 workload、低风险或规模较小时仍可用。约束变化与机制：search-agent SFT quality depends on selecting informative, difficult trajectories rather than merely scaling trajectory count; the result is workload-bound and does not displace RL branches。Method：`https://arxiv.org/html/2605.04036v1 §3 Trajectory Construction; §4 OpenSeeker-v2 SFT`。

Evaluation：`https://arxiv.org/html/2605.04036v1 §5 Experiments and Ablations`。Counterevidence/limits：`https://arxiv.org/html/2605.04036v1 §6 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO`。Artifact：`https://arxiv.org/html/2605.04036v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。

<!-- claim:SF-2026-ARXIV-2605-04036:start -->长期结论只限 exact-v1 披露边界，不把作者 benchmark 外推到未测模型、硬件、精度、长度、batch、并发或 SLO。<!-- claim:SF-2026-ARXIV-2605-04036:end -->
<!-- review:SF-2026-ARXIV-2605-04036:end -->

<!-- review:SF-2026-ARXIV-2605-04039:start -->
#### Safety and accuracy follow different scaling laws in clinical large language models

问题与旧路径：旧路径在固定 workload、低风险或规模较小时仍可用。约束变化与机制：clinical accuracy and safety have different scaling curves, requiring risk-weighted, evidence-aware evaluation and abstention criteria instead of inferring deployment safety from mean accuracy。Method：`https://arxiv.org/html/2605.04039v1 §3 SaFE-Scale Framework; §4 Safety Dimensions`。

Evaluation：`https://arxiv.org/html/2605.04039v1 §5 Scaling Experiments`。Counterevidence/limits：`https://arxiv.org/html/2605.04039v1 §6 Limitations and Clinical Scope; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO`。Artifact：`https://arxiv.org/html/2605.04039v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。

<!-- claim:SF-2026-ARXIV-2605-04039:start -->长期结论只限 exact-v1 披露边界，不把作者 benchmark 外推到未测模型、硬件、精度、长度、batch、并发或 SLO。<!-- claim:SF-2026-ARXIV-2605-04039:end -->
<!-- review:SF-2026-ARXIV-2605-04039:end -->

<!-- review:SF-2026-ARXIV-2605-04116:start -->
#### Membership Inference Attacks for Retrieval Based In-Context Learning for Document Question Answering

问题与旧路径：旧路径在固定 workload、低风险或规模较小时仍可用。约束变化与机制：retrieval-selected in-context examples create a remotely observable membership channel, so example-store privacy belongs to the serving threat model。Method：`https://arxiv.org/html/2605.04116v1 §3 Threat Model; §4 Prefix-Based Membership Attacks`。

Evaluation：`https://arxiv.org/html/2605.04116v1 §5 Experimental Setup; §6 Results`。Counterevidence/limits：`https://arxiv.org/html/2605.04116v1 §7 Defense and Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO`。Artifact：`https://arxiv.org/html/2605.04116v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。

<!-- claim:SF-2026-ARXIV-2605-04116:start -->长期结论只限 exact-v1 披露边界，不把作者 benchmark 外推到未测模型、硬件、精度、长度、batch、并发或 SLO。<!-- claim:SF-2026-ARXIV-2605-04116:end -->
<!-- review:SF-2026-ARXIV-2605-04116:end -->

<!-- review:SF-2026-ARXIV-2605-04135:start -->
#### Frontier Lag: A Bibliometric Audit of Capability Misrepresentation in Academic AI Evaluation

问题与旧路径：旧路径在固定 workload、低风险或规模较小时仍可用。约束变化与机制：capability claims must bind model release, elicitation, tools and evaluation date because frontier lag can turn a valid historical measurement into a misleading current-system conclusion。Method：`https://arxiv.org/html/2605.04135v1 §2 Frontier-Lag Audit Method; §3 Configuration and Date Coding`。

Evaluation：`https://arxiv.org/html/2605.04135v1 §4 Bibliometric Results`。Counterevidence/limits：`https://arxiv.org/html/2605.04135v1 §5 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO`。Artifact：`https://arxiv.org/html/2605.04135v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。

<!-- claim:SF-2026-ARXIV-2605-04135:start -->长期结论只限 exact-v1 披露边界，不把作者 benchmark 外推到未测模型、硬件、精度、长度、batch、并发或 SLO。<!-- claim:SF-2026-ARXIV-2605-04135:end -->
<!-- review:SF-2026-ARXIV-2605-04135:end -->

<!-- review:SF-2026-ARXIV-2605-04172:start -->
#### täkōFormal: Enabling Robust Software for Programmable Memory Hierarchies (Extended Version)

问题与旧路径：旧路径在固定 workload、低风险或规模较小时仍可用。约束变化与机制：programmable memory callbacks require an ISA-level consistency contract across misses, evictions and writebacks; performance programmability without formal ordering moves hidden state into software。Method：`https://arxiv.org/html/2605.04172v1 §3 täkō Memory Consistency Model; §4 Formal Semantics`。

Evaluation：`https://arxiv.org/html/2605.04172v1 §5 Litmus Tests and Validation`。Counterevidence/limits：`https://arxiv.org/html/2605.04172v1 §6 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO`。Artifact：`https://arxiv.org/html/2605.04172v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。

<!-- claim:SF-2026-ARXIV-2605-04172:start -->长期结论只限 exact-v1 披露边界，不把作者 benchmark 外推到未测模型、硬件、精度、长度、batch、并发或 SLO。<!-- claim:SF-2026-ARXIV-2605-04172:end -->
<!-- review:SF-2026-ARXIV-2605-04172:end -->

<!-- review:SF-2026-ARXIV-2605-04178:start -->
#### Microbenchmark-Driven Analytical Performance Modeling Across Modern GPU Architectures

问题与旧路径：旧路径在固定 workload、低风险或规模较小时仍可用。约束变化与机制：GPU execution plans require architecture-specific microbenchmarks for memory hierarchy, matrix units, occupancy and precision; peak-FLOP rooflines are insufficient。Method：`https://arxiv.org/html/2605.04178v1 §3 Microbenchmark Suite; §4 Analytical Models`。

Evaluation：`https://arxiv.org/html/2605.04178v1 §5 Validation on B200 and MI300A`。Counterevidence/limits：`https://arxiv.org/html/2605.04178v1 §6 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO`。Artifact：`https://arxiv.org/html/2605.04178v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。

<!-- claim:SF-2026-ARXIV-2605-04178:start -->长期结论只限 exact-v1 披露边界，不把作者 benchmark 外推到未测模型、硬件、精度、长度、batch、并发或 SLO。<!-- claim:SF-2026-ARXIV-2605-04178:end -->
<!-- review:SF-2026-ARXIV-2605-04178:end -->

<!-- review:SF-2026-ARXIV-2605-04209:start -->
#### Undetectable Backdoors in Model Parameters: Hiding Sparse Secrets in High Dimensions

问题与旧路径：旧路径在固定 workload、低风险或规模较小时仍可用。约束变化与机制：model artifacts can carry statistically hidden parameter backdoors whose detectability is bounded by the attack distribution, extending supply-chain verification beyond file hashes and conventional weight scanning。Method：`https://arxiv.org/html/2605.04209v1 §3 Sparse Backdoor Construction; §4 Undetectability Analysis`。

Evaluation：`https://arxiv.org/html/2605.04209v1 §5 Experiments`。Counterevidence/limits：`https://arxiv.org/html/2605.04209v1 §6 Limitations and Threat-Model Boundary; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO`。Artifact：`https://arxiv.org/html/2605.04209v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。

<!-- claim:SF-2026-ARXIV-2605-04209:start -->长期结论只限 exact-v1 披露边界，不把作者 benchmark 外推到未测模型、硬件、精度、长度、batch、并发或 SLO。<!-- claim:SF-2026-ARXIV-2605-04209:end -->
<!-- review:SF-2026-ARXIV-2605-04209:end -->

<!-- review:SF-2026-ARXIV-2605-04213:start -->
#### The Anatomy of Silent Data Corruption: GPU Error Pattern Study and Modeling Guidance

问题与旧路径：旧路径在固定 workload、低风险或规模较小时仍可用。约束变化与机制：silent GPU corruption needs empirically grounded fault models tied to operation type and propagation pattern; generic random bit flips can invalidate resilience conclusions for large-scale training。Method：`https://arxiv.org/html/2605.04213v1 §3 Gate-Level Fault-Injection Method; §4 SDC Taxonomy`。

Evaluation：`https://arxiv.org/html/2605.04213v1 §5 Error-Pattern Results; §6 Modeling Guidance`。Counterevidence/limits：`https://arxiv.org/html/2605.04213v1 §7 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO`。Artifact：`https://arxiv.org/html/2605.04213v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。

<!-- claim:SF-2026-ARXIV-2605-04213:start -->长期结论只限 exact-v1 披露边界，不把作者 benchmark 外推到未测模型、硬件、精度、长度、batch、并发或 SLO。<!-- claim:SF-2026-ARXIV-2605-04213:end -->
<!-- review:SF-2026-ARXIV-2605-04213:end -->

<!-- review:SF-2026-ARXIV-2605-04215:start -->
#### Predict-then-Diffuse: Adaptive Response Length for Compute-Budgeted Inference in Diffusion LLMs

问题与旧路径：旧路径在固定 workload、低风险或规模较小时仍可用。约束变化与机制：fixed-length diffusion generation turns response-length prediction into an admission-time compute budget with explicit underprediction retry risk。Method：`https://arxiv.org/html/2605.04215v1 §3 Predict-then-Diffuse; §3.1 Adaptive Response Length Predictor`。

Evaluation：`https://arxiv.org/html/2605.04215v1 §4 Experiments`。Counterevidence/limits：`https://arxiv.org/html/2605.04215v1 §5 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO`。Artifact：`https://arxiv.org/html/2605.04215v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。

<!-- claim:SF-2026-ARXIV-2605-04215:start -->长期结论只限 exact-v1 披露边界，不把作者 benchmark 外推到未测模型、硬件、精度、长度、batch、并发或 SLO。<!-- claim:SF-2026-ARXIV-2605-04215:end -->
<!-- review:SF-2026-ARXIV-2605-04215:end -->

<!-- review:SF-2026-ARXIV-2605-04236:start -->
#### Adaptive Consensus in LLM Ensembles via Sequential Evidence Accumulation: Automatic Budget Identification and Calibrated Commit Signals

问题与旧路径：旧路径在固定 workload、低风险或规模较小时仍可用。约束变化与机制：ensemble deliberation needs an evidence-accumulation stopping and fallback contract because more samples can cross from useful consensus into degraded decisions。Method：`https://arxiv.org/html/2605.04236v1 §3 DASE Sequential Evidence Accumulation; §3.3 Commit Routing`。

Evaluation：`https://arxiv.org/html/2605.04236v1 §4 Experiments and Calibration`。Counterevidence/limits：`https://arxiv.org/html/2605.04236v1 §5 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO`。Artifact：`https://arxiv.org/html/2605.04236v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。

<!-- claim:SF-2026-ARXIV-2605-04236:start -->长期结论只限 exact-v1 披露边界，不把作者 benchmark 外推到未测模型、硬件、精度、长度、batch、并发或 SLO。<!-- claim:SF-2026-ARXIV-2605-04236:end -->
<!-- review:SF-2026-ARXIV-2605-04236:end -->

<!-- review:SF-2026-ARXIV-2605-04256:start -->
#### phys-MCP: A Control Plane for Heterogeneous Physical Neural Networks

问题与旧路径：旧路径在固定 workload、低风险或规模较小时仍可用。约束变化与机制：heterogeneous physical neural substrates require a typed control plane for capability discovery, timing, observation, actuation and safety rather than presenting every device as an interchangeable tool。Method：`https://arxiv.org/html/2605.04256v1 §3 phys-MCP Control Plane; §4 Resource and Capability Model`。

Evaluation：`https://arxiv.org/html/2605.04256v1 §5 Prototype Evaluation`。Counterevidence/limits：`https://arxiv.org/html/2605.04256v1 §6 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO`。Artifact：`https://arxiv.org/html/2605.04256v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。

<!-- claim:SF-2026-ARXIV-2605-04256:start -->长期结论只限 exact-v1 披露边界，不把作者 benchmark 外推到未测模型、硬件、精度、长度、batch、并发或 SLO。<!-- claim:SF-2026-ARXIV-2605-04256:end -->
<!-- review:SF-2026-ARXIV-2605-04256:end -->

<!-- review:SF-2026-ARXIV-2605-04263:start -->
#### Parallel Prefix Verification for Speculative Generation

问题与旧路径：旧路径在固定 workload、低风险或规模较小时仍可用。约束变化与机制：semantic speculative generation can verify multiple draft prefixes in one target pass, but must preserve a maximal valid commit boundary distinct from token-exact acceptance。Method：`https://arxiv.org/html/2605.04263v1 §3 PARSE; §3.2 Parallel Prefix Verification`。

Evaluation：`https://arxiv.org/html/2605.04263v1 §4 Experiments and Ablations`。Counterevidence/limits：`https://arxiv.org/html/2605.04263v1 §5 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO`。Artifact：`https://arxiv.org/html/2605.04263v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。

<!-- claim:SF-2026-ARXIV-2605-04263:start -->长期结论只限 exact-v1 披露边界，不把作者 benchmark 外推到未测模型、硬件、精度、长度、batch、并发或 SLO。<!-- claim:SF-2026-ARXIV-2605-04263:end -->
<!-- review:SF-2026-ARXIV-2605-04263:end -->

<!-- review:SF-2026-ARXIV-2605-04264:start -->
#### Governed Collaborative Memory as Artificial Selection in LLM-Based Multi-Agent Systems

问题与旧路径：旧路径在固定 workload、低风险或规模较小时仍可用。约束变化与机制：shared memory admission is a governed selection regime over provenance, correction and role preservation, not merely a retrieval score。Method：`https://arxiv.org/pdf/2605.04264v1 PDF §2 Selection Regimes; §3 Layered Memory Architecture`。

Evaluation：`https://arxiv.org/pdf/2605.04264v1 PDF §4 Documented Traces`。Counterevidence/limits：`https://arxiv.org/pdf/2605.04264v1 PDF §5 Limitations and Design Agenda; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO`。Artifact：`https://arxiv.org/pdf/2605.04264v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。

<!-- claim:SF-2026-ARXIV-2605-04264:start -->长期结论只限 exact-v1 披露边界，不把作者 benchmark 外推到未测模型、硬件、精度、长度、batch、并发或 SLO。<!-- claim:SF-2026-ARXIV-2605-04264:end -->
<!-- review:SF-2026-ARXIV-2605-04264:end -->

<!-- review:SF-2026-ARXIV-2605-04266:start -->
#### Explaining and Preventing Alignment Collapse in Iterative RLHF

问题与旧路径：旧路径在固定 workload、低风险或规模较小时仍可用。约束变化与机制：iterative RLHF creates a policy-to-future-reward-model feedback loop; omitting parameter steering allows self-reinforcing reward-model exploitation。Method：`https://arxiv.org/html/2605.04266v1 §3 Stackelberg Formulation; §4 Gradient Decomposition; §5 FPO`。

Evaluation：`https://arxiv.org/html/2605.04266v1 §6 Experiments`。Counterevidence/limits：`https://arxiv.org/html/2605.04266v1 §7 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO`。Artifact：`https://arxiv.org/html/2605.04266v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。

<!-- claim:SF-2026-ARXIV-2605-04266:start -->长期结论只限 exact-v1 披露边界，不把作者 benchmark 外推到未测模型、硬件、精度、长度、batch、并发或 SLO。<!-- claim:SF-2026-ARXIV-2605-04266:end -->
<!-- review:SF-2026-ARXIV-2605-04266:end -->

<!-- review:SF-2026-ARXIV-2605-04269:start -->
#### Adapt or Forget: Provable Tradeoffs Between Adam and SGD in Nonstationary Optimization

问题与旧路径：旧路径在固定 workload、低风险或规模较小时仍可用。约束变化与机制：under nonstationary objectives Adam's adaptive state trades faster tracking for longer optimizer memory, whereas SGD forgets differently; optimizer choice therefore depends on drift, projection and stationarity assumptions。Method：`https://arxiv.org/html/2605.04269v1 §3 Nonstationary Adam Analysis; §4 Tracking and Stationarity Bounds`。

Evaluation：`https://arxiv.org/html/2605.04269v1 §5 Experiments`。Counterevidence/limits：`https://arxiv.org/html/2605.04269v1 §6 Assumptions and Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO`。Artifact：`https://arxiv.org/html/2605.04269v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。

<!-- claim:SF-2026-ARXIV-2605-04269:start -->长期结论只限 exact-v1 披露边界，不把作者 benchmark 外推到未测模型、硬件、精度、长度、batch、并发或 SLO。<!-- claim:SF-2026-ARXIV-2605-04269:end -->
<!-- review:SF-2026-ARXIV-2605-04269:end -->

<!-- review:SF-2026-ARXIV-2605-04295:start -->
#### LLMs Uncertainty Quantification via Adaptive Conformal Semantic Entropy

问题与旧路径：旧路径在固定 workload、低风险或规模较小时仍可用。约束变化与机制：uncertainty can be estimated over semantic response clusters and calibrated with conformal acceptance, but coverage guarantees remain conditional on calibration exchangeability and the chosen semantic equivalence model。Method：`https://arxiv.org/html/2605.04295v1 §2 Semantic Entropy; §3 Adaptive Conformal Semantic Entropy`。

Evaluation：`https://arxiv.org/html/2605.04295v1 §4 Evaluation and Ablations`。Counterevidence/limits：`https://arxiv.org/html/2605.04295v1 §5 Limitations; Appendix Proofs; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO`。Artifact：`https://arxiv.org/html/2605.04295v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。

<!-- claim:SF-2026-ARXIV-2605-04295:start -->长期结论只限 exact-v1 披露边界，不把作者 benchmark 外推到未测模型、硬件、精度、长度、batch、并发或 SLO。<!-- claim:SF-2026-ARXIV-2605-04295:end -->
<!-- review:SF-2026-ARXIV-2605-04295:end -->

<!-- review:SF-2026-ARXIV-2605-04312:start -->
#### Agent Island: A Saturation- and Contamination-Resistant Benchmark from Multiagent Games

问题与旧路径：旧路径在固定 workload、低风险或规模较小时仍可用。约束变化与机制：a persistent multi-agent game can reduce benchmark saturation and contamination by making other agents part of the changing workload, while introducing opponent-population and reproducibility dependence。Method：`https://arxiv.org/html/2605.04312v1 §3 Agent Island Environment; §4 Dynamic Evaluation Protocol`。

Evaluation：`https://arxiv.org/html/2605.04312v1 §5 Experiments`。Counterevidence/limits：`https://arxiv.org/html/2605.04312v1 §6 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO`。Artifact：`https://arxiv.org/html/2605.04312v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。

<!-- claim:SF-2026-ARXIV-2605-04312:start -->长期结论只限 exact-v1 披露边界，不把作者 benchmark 外推到未测模型、硬件、精度、长度、batch、并发或 SLO。<!-- claim:SF-2026-ARXIV-2605-04312:end -->
<!-- review:SF-2026-ARXIV-2605-04312:end -->

<!-- review:SF-2026-ARXIV-2605-04333:start -->
#### Resilient AI Supercomputer Networking using MRC and SRv6

问题与旧路径：旧路径在固定 workload、低风险或规模较小时仍可用。约束变化与机制：large synchronous training networks need multipath transport, redundant Clos planes and explicit failure handling because tail latency and flow collisions dominate collective completion at scale。Method：`https://arxiv.org/html/2605.04333v1 §2 MRC Transport; §3 Multi-Plane Clos and SRv6`。

Evaluation：`https://arxiv.org/html/2605.04333v1 §4 Simulation and Evaluation`。Counterevidence/limits：`https://arxiv.org/html/2605.04333v1 §5 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO`。Artifact：`https://arxiv.org/html/2605.04333v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。

<!-- claim:SF-2026-ARXIV-2605-04333:start -->长期结论只限 exact-v1 披露边界，不把作者 benchmark 外推到未测模型、硬件、精度、长度、batch、并发或 SLO。<!-- claim:SF-2026-ARXIV-2605-04333:end -->
<!-- review:SF-2026-ARXIV-2605-04333:end -->

<!-- review:SF-2026-ARXIV-2605-04341:start -->
#### Budgeted LoRA: Distillation as Structured Compute Allocation for Efficient Inference

问题与旧路径：旧路径在固定 workload、低风险或规模较小时仍可用。约束变化与机制：parameter-efficient adaptation reduces training cost but not dense inference cost; budgeted distillation must allocate structural rank or compute under a deployment budget to produce an actually cheaper student。Method：`https://arxiv.org/html/2605.04341v1 §3 Budgeted LoRA; §3.2 Structured Compute Allocation`。

Evaluation：`https://arxiv.org/html/2605.04341v1 §4 Experiments and Pareto Analysis`。Counterevidence/limits：`https://arxiv.org/html/2605.04341v1 §5 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO`。Artifact：`https://arxiv.org/html/2605.04341v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。

<!-- claim:SF-2026-ARXIV-2605-04341:start -->长期结论只限 exact-v1 披露边界，不把作者 benchmark 外推到未测模型、硬件、精度、长度、batch、并发或 SLO。<!-- claim:SF-2026-ARXIV-2605-04341:end -->
<!-- review:SF-2026-ARXIV-2605-04341:end -->


<!-- review:SF-2026-ARXIV-2605-04357:start -->
#### Coral: Cost-Efficient Multi-LLM Serving over Heterogeneous Cloud GPUs

问题与旧路径：旧路径在固定 workload、低风险或规模较小时仍可用。约束变化与机制：heterogeneous multi-model serving must co-optimize model placement and resource allocation under per-model SLOs, separating offline serving templates from online allocation。Method：`https://arxiv.org/html/2605.04357v1 §3 Multi-LLM Serving Problem; §4 Optimization; §5 Runtime`。

Evaluation：`https://arxiv.org/html/2605.04357v1 §6 Evaluation`。Counterevidence/limits：`https://arxiv.org/html/2605.04357v1 §6.7 Sensitivity and §8 scope boundary; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO`。Artifact：`https://arxiv.org/html/2605.04357v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。

<!-- claim:SF-2026-ARXIV-2605-04357:start -->长期结论只限 exact-v1 披露边界，不把作者 benchmark 外推到未测模型、硬件、精度、长度、batch、并发或 SLO。<!-- claim:SF-2026-ARXIV-2605-04357:end -->
<!-- review:SF-2026-ARXIV-2605-04357:end -->

<!-- review:SF-2026-ARXIV-2605-04361:start -->
#### When Context Hurts: The Crossover Effect of Knowledge Transfer on Multi-Agent Design Exploration

问题与旧路径：旧路径在固定 workload、低风险或规模较小时仍可用。约束变化与机制：context artifacts have task-dependent crossover effects, so context admission must estimate marginal decision value and interference rather than assume that more relevant context monotonically helps。Method：`https://arxiv.org/html/2605.04361v1 §3 Multi-Agent Design-Exploration Protocol; §4 Context Conditions`。

Evaluation：`https://arxiv.org/html/2605.04361v1 §5 Crossover Results`。Counterevidence/limits：`https://arxiv.org/html/2605.04361v1 §6 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO`。Artifact：`https://arxiv.org/html/2605.04361v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。

<!-- claim:SF-2026-ARXIV-2605-04361:start -->长期结论只限 exact-v1 披露边界，不把作者 benchmark 外推到未测模型、硬件、精度、长度、batch、并发或 SLO。<!-- claim:SF-2026-ARXIV-2605-04361:end -->
<!-- review:SF-2026-ARXIV-2605-04361:end -->

<!-- review:SF-2026-ARXIV-2605-04373:start -->
#### Worst-Case Discovery and Runtime Protection for RL-Based Network Controllers

问题与旧路径：旧路径在固定 workload、低风险或规模较小时仍可用。约束变化与机制：learned controllers need adversarial worst-case discovery compiled into a lightweight runtime protection rule with a nominal-path fallback。Method：`https://arxiv.org/html/2605.04373v1 §3 Regret-Maximization Discovery; §4 Runtime Protection`。

Evaluation：`https://arxiv.org/html/2605.04373v1 §5 Evaluation`。Counterevidence/limits：`https://arxiv.org/html/2605.04373v1 §6 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO`。Artifact：`https://arxiv.org/html/2605.04373v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。

<!-- claim:SF-2026-ARXIV-2605-04373:start -->长期结论只限 exact-v1 披露边界，不把作者 benchmark 外推到未测模型、硬件、精度、长度、batch、并发或 SLO。<!-- claim:SF-2026-ARXIV-2605-04373:end -->
<!-- review:SF-2026-ARXIV-2605-04373:end -->

<!-- review:SF-2026-ARXIV-2605-04375:start -->
#### Experiment-as-Code Labs: A Declarative Stack for AI-Driven Scientific Discovery

问题与旧路径：旧路径在固定 workload、低风险或规模较小时仍可用。约束变化与机制：physical experiments need declarative experiment-as-code that binds instrument capabilities, execution state, provenance and human safety approval, extending durable workflow semantics beyond digital tools。Method：`https://arxiv.org/html/2605.04375v1 §3 Experiment-as-Code Model; §4 Declarative Lab Stack`。

Evaluation：`https://arxiv.org/html/2605.04375v1 §5 Case Studies and Evaluation`。Counterevidence/limits：`https://arxiv.org/html/2605.04375v1 §6 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO`。Artifact：`https://arxiv.org/html/2605.04375v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。

<!-- claim:SF-2026-ARXIV-2605-04375:start -->长期结论只限 exact-v1 披露边界，不把作者 benchmark 外推到未测模型、硬件、精度、长度、batch、并发或 SLO。<!-- claim:SF-2026-ARXIV-2605-04375:end -->
<!-- review:SF-2026-ARXIV-2605-04375:end -->

<!-- review:SF-2026-ARXIV-2605-05248:start -->
#### Governed Metaprogramming for Intelligent Systems: Reclassifying Eval as a Governed Effect

问题与旧路径：旧路径在固定 workload、低风险或规模较小时仍可用。约束变化与机制：turning generated symbolic structure into executable code is an authority-amplifying materialization effect that requires capability, policy and resource admission。Method：`https://arxiv.org/html/2605.05248v1 §3 Governed Metaprogramming; §4 Pure Form Evaluation; §5 Governed Materialization`。

Evaluation：`https://arxiv.org/html/2605.05248v1 §7 Implementation and Evaluation`。Counterevidence/limits：`https://arxiv.org/html/2605.05248v1 §8 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO`。Artifact：`https://arxiv.org/html/2605.05248v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。

<!-- claim:SF-2026-ARXIV-2605-05248:start -->长期结论只限 exact-v1 披露边界，不把作者 benchmark 外推到未测模型、硬件、精度、长度、batch、并发或 SLO。<!-- claim:SF-2026-ARXIV-2605-05248:end -->
<!-- review:SF-2026-ARXIV-2605-05248:end -->

<!-- review:SF-2026-ARXIV-2605-05253:start -->
#### EnterpriseRAG-Bench: A RAG Benchmark for Company Internal Knowledge

问题与旧路径：旧路径在固定 workload、低风险或规模较小时仍可用。约束变化与机制：enterprise RAG evaluation must preserve private-document heterogeneity, access boundaries and multi-document evidence needs, but a benchmark dataset does not itself define a new retrieval ownership mechanism。Method：`https://arxiv.org/html/2605.05253v1 §3 EnterpriseRAG-Bench Construction`。

Evaluation：`https://arxiv.org/html/2605.05253v1 §4 Evaluation Protocol; §5 Results`。Counterevidence/limits：`https://arxiv.org/html/2605.05253v1 §6 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO`。Artifact：`https://arxiv.org/html/2605.05253v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。

<!-- claim:SF-2026-ARXIV-2605-05253:start -->长期结论只限 exact-v1 披露边界，不把作者 benchmark 外推到未测模型、硬件、精度、长度、batch、并发或 SLO。<!-- claim:SF-2026-ARXIV-2605-05253:end -->
<!-- review:SF-2026-ARXIV-2605-05253:end -->

<!-- review:SF-2026-ARXIV-2605-08190:start -->
#### Synergistic Simplex: Cooperative Runtime Assurance for Safety-Critical Autonomous Systems

问题与旧路径：旧路径在固定 workload、低风险或规模较小时仍可用。约束变化与机制：runtime assurance may consume ML outputs only under formally derived cooperative monitor conditions and a verified safe fallback。Method：`https://arxiv.org/html/2605.08190v1 §3 Synergistic Simplex Architecture; §4 Safety Conditions`。

Evaluation：`https://arxiv.org/html/2605.08190v1 §5 Autonomous-Vehicle Evaluation`。Counterevidence/limits：`https://arxiv.org/html/2605.08190v1 §6 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO`。Artifact：`https://arxiv.org/html/2605.08190v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。

<!-- claim:SF-2026-ARXIV-2605-08190:start -->长期结论只限 exact-v1 披露边界，不把作者 benchmark 外推到未测模型、硬件、精度、长度、batch、并发或 SLO。<!-- claim:SF-2026-ARXIV-2605-08190:end -->
<!-- review:SF-2026-ARXIV-2605-08190:end -->

<!-- review:SF-2026-ARXIV-2605-08192:start -->
#### NeurIPS Should Require Reproducibility Standards for Frontier AI Safety Claims

问题与旧路径：旧路径在固定 workload、低风险或规模较小时仍可用。约束变化与机制：frontier-safety release claims need reproducible artifacts, configuration disclosure and independent rerun conditions; authority or venue cannot substitute for an inspectable evaluation contract。Method：`https://arxiv.org/html/2605.08192v1 §2 Evidential Inversion; §3 Proposed Reproducibility Standard`。

Evaluation：`https://arxiv.org/html/2605.08192v1 §4 Worked Requirements and Cases`。Counterevidence/limits：`https://arxiv.org/html/2605.08192v1 §5 Limitations and Governance Scope; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO`。Artifact：`https://arxiv.org/html/2605.08192v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。

<!-- claim:SF-2026-ARXIV-2605-08192:start -->长期结论只限 exact-v1 披露边界，不把作者 benchmark 外推到未测模型、硬件、精度、长度、batch、并发或 SLO。<!-- claim:SF-2026-ARXIV-2605-08192:end -->
<!-- review:SF-2026-ARXIV-2605-08192:end -->

<!-- review:SF-2026-ARXIV-2605-08195:start -->
#### ExecuTorch -- A Unified PyTorch Solution to Run AI Models On-Device

问题与旧路径：旧路径在固定 workload、低风险或规模较小时仍可用。约束变化与机制：on-device execution needs a portable exported program with delegated backend lowering while preserving framework semantics and explicit fallback。Method：`https://arxiv.org/html/2605.08195v1 §2 ExecuTorch Architecture; §3 Export and Delegation; §4 Runtime`。

Evaluation：`https://arxiv.org/html/2605.08195v1 §5 Evaluation`。Counterevidence/limits：`https://arxiv.org/html/2605.08195v1 §6 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO`。Artifact：`https://arxiv.org/html/2605.08195v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。

<!-- claim:SF-2026-ARXIV-2605-08195:start -->长期结论只限 exact-v1 披露边界，不把作者 benchmark 外推到未测模型、硬件、精度、长度、batch、并发或 SLO。<!-- claim:SF-2026-ARXIV-2605-08195:end -->
<!-- review:SF-2026-ARXIV-2605-08195:end -->

<!-- review:SF-2026-ARXIV-2605-10959:start -->
#### QuIDE: Mastering the Quantized Intelligence Trade-off via Active Optimization

问题与旧路径：旧路径在固定 workload、低风险或规模较小时仍可用。约束变化与机制：quantization decisions need workload-specific accuracy, compression and realized latency measurements, but collapsing them into one scalar intelligence index hides Pareto preferences and cannot be a universal execution objective。Method：`https://arxiv.org/html/2605.10959v1 §3 QuIDE Metric and Active Optimization`。

Evaluation：`https://arxiv.org/html/2605.10959v1 §4 Experiments`。Counterevidence/limits：`https://arxiv.org/html/2605.10959v1 §5 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO`。Artifact：`https://arxiv.org/html/2605.10959v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。

<!-- claim:SF-2026-ARXIV-2605-10959:start -->长期结论只限 exact-v1 披露边界，不把作者 benchmark 外推到未测模型、硬件、精度、长度、batch、并发或 SLO。<!-- claim:SF-2026-ARXIV-2605-10959:end -->
<!-- review:SF-2026-ARXIV-2605-10959:end -->

## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-03275 | controlled production-RAG data-layer comparison: 50,000 documents, 128-dimensional embeddings, 20 tenants, 5 categories, four query classes, 200 repetitions per class | Not Disclosed — retrieval pipeline, not a model benchmark | PostgreSQL 16 with pgvector 0.6.0 and HNSW; host hardware Not Disclosed | embeddings 128-d; numeric precision Not Disclosed | query constraints disclosed; token length Not Applicable | retrieval results only; output length Not Applicable | one query execution per repetition | Not Disclosed | p50/p95/p99 retrieval latency plus freshness, tenant-isolation and engineering-complexity checks | author protocol; Stack A simulated inside PostgreSQL; independent reproduction Not Disclosed |
| SF-2026-ARXIV-2605-03309 | exact-v1 disclosed workload for Cryptographic Registry Provenance: Structural Defense Against Dependency Confusion in AI Package Ecosystems | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-2026-ARXIV-2605-03310 | exact-v1 disclosed workload for Coordination as an Architectural Layer for LLM-Based Multi-Agent Systems | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-2026-ARXIV-2605-03312 | exact-v1 disclosed workload for MemFlow: Intent-Driven Memory Orchestration for Small Language Model Agents | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-2026-ARXIV-2605-03314 | exact-v1 disclosed workload for When to Think, When to Speak: Learning Disclosure Policies for LLM Reasoning | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-2026-ARXIV-2605-03327 | exact-v1 disclosed workload for DGPO: Distribution Guided Policy Optimization for Fine Grained Credit Assignment | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-2026-ARXIV-2605-03353 | exact-v1 disclosed workload for SkCC: Portable and Secure Skill Compilation for Cross-Framework LLM Agents | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-2026-ARXIV-2605-03354 | exact-v1 disclosed workload for What Happens Inside Agent Memory? Circuit Analysis from Emergence to Diagnosis | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-2026-ARXIV-2605-03375 | exact-v1 disclosed workload for Tutti: Making SSD-Backed KV Cache Practical for Long-Context LLM Serving | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-2026-ARXIV-2605-03378 | exact-v1 disclosed workload for ARGUS: Defending LLM Agents Against Context-Aware Prompt Injection | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-2026-ARXIV-2605-03379 | exact-v1 disclosed workload for Two Calls, Two Moments, and the Vote-Accuracy Curve of Repeated LLM Inference | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-2026-ARXIV-2605-03408 | exact-v1 disclosed workload for Discovering Reinforcement Learning Interfaces with Large Language Models | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-2026-ARXIV-2605-03425 | exact-v1 disclosed workload for FIBER: A Differentially Private Optimizer with Filter-Aware Innovation Bias Correction | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-2026-ARXIV-2605-03482 | exact-v1 disclosed workload for MEMSAD: Gradient-Coupled Anomaly Detection for Memory Poisoning in Retrieval-Augmented Agents | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-2026-ARXIV-2605-03505 | exact-v1 disclosed workload for LATS-RCA: Language Agent Tree Search for Root Cause Analysis in Microservices | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-2026-ARXIV-2605-03534 | exact-v1 disclosed workload for SURE-RAG: Sufficiency and Uncertainty-Aware Evidence Verification for Selective Retrieval-Augmented Generation | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-2026-ARXIV-2605-03561 | exact-v1 disclosed workload for Enhancing Performance Insight at Scale: A Heterogeneous Framework for Exascale Diagnostics | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-2026-ARXIV-2605-03562 | exact-v1 disclosed workload for HeadQ: Model-Visible Distortion and Score-Space Correction for KV-Cache Quantization | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-2026-ARXIV-2605-03566 | exact-v1 disclosed workload for Lifting to tensors when compiling scientific computing workloads for AI Engines | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-2026-ARXIV-2605-03596 | exact-v1 disclosed workload for Workspace-Bench 1.0: Benchmarking AI Agents on Workspace Tasks with Large-Scale File Dependencies | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-2026-ARXIV-2605-03644 | exact-v1 disclosed workload for AdapShot: Adaptive Many-Shot In-Context Learning with Semantic-Aware KV Cache Reuse | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-2026-ARXIV-2605-03667 | exact-v1 disclosed workload for ELAS: Efficient Pre-Training of Low-Rank Large Language Models via 2:4 Activation Sparsity | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-2026-ARXIV-2605-03675 | exact-v1 disclosed workload for MEMTIER: Tiered Memory Architecture and Retrieval Bottleneck Analysis for Long-Running Autonomous AI Agents | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-2026-ARXIV-2605-03677 | exact-v1 disclosed workload for Uni-OPD: Unifying On-Policy Distillation with a Dual-Perspective Recipe | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-2026-ARXIV-2605-03762 | exact-v1 disclosed workload for OracleProto: A Reproducible Framework for Benchmarking LLM Native Forecasting via Knowledge Cutoff and Temporal Masking | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-2026-ARXIV-2605-03838 | exact-v1 disclosed workload for TRACE: A Metrologically-Grounded Engineering Framework for Trustworthy Agentic AI Systems in Operationally Critical Domains | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-2026-ARXIV-2605-03858 | exact-v1 disclosed workload for MCJudgeBench: A Benchmark for Constraint-Level Judge Evaluation in Multi-Constraint Instruction Following | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-2026-ARXIV-2605-03862 | exact-v1 disclosed workload for Correct Is Not Enough: Training Reasoning Planners with Executor-Grounded Rewards | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-2026-ARXIV-2605-03884 | exact-v1 disclosed workload for QKVShare: Quantized KV-Cache Handoff for Multi-Agent On-Device LLMs | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-2026-ARXIV-2605-03952 | exact-v1 disclosed workload for MOSAIC-Bench: Measuring Compositional Vulnerability Induction in Coding Agents | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-2026-ARXIV-2605-03971 | exact-v1 disclosed workload for Logical Consistency as a Bridge: Improving LLM Hallucination Detection via Label Constraint Modeling between Responses and Self-Judgments | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-2026-ARXIV-2605-03986 | exact-v1 disclosed workload for From Intent to Execution: Composing Agentic Workflows with Agent Recommendation | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-2026-ARXIV-2605-04018 | exact-v1 disclosed workload for Rethinking Reasoning-Intensive Retrieval: Evaluating and Advancing Retrievers in Agentic Search Systems | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-2026-ARXIV-2605-04019 | exact-v1 disclosed workload for Redefining AI Red Teaming in the Agentic Era: From Weeks to Hours | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-2026-ARXIV-2605-04036 | exact-v1 disclosed workload for OpenSeeker-v2: Pushing the Limits of Search Agents with Informative and High-Difficulty Trajectories | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-2026-ARXIV-2605-04039 | exact-v1 disclosed workload for Safety and accuracy follow different scaling laws in clinical large language models | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-2026-ARXIV-2605-04116 | exact-v1 disclosed workload for Membership Inference Attacks for Retrieval Based In-Context Learning for Document Question Answering | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-2026-ARXIV-2605-04135 | exact-v1 disclosed workload for Frontier Lag: A Bibliometric Audit of Capability Misrepresentation in Academic AI Evaluation | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-2026-ARXIV-2605-04172 | exact-v1 disclosed workload for täkōFormal: Enabling Robust Software for Programmable Memory Hierarchies (Extended Version) | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-2026-ARXIV-2605-04178 | exact-v1 disclosed workload for Microbenchmark-Driven Analytical Performance Modeling Across Modern GPU Architectures | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-2026-ARXIV-2605-04209 | exact-v1 disclosed workload for Undetectable Backdoors in Model Parameters: Hiding Sparse Secrets in High Dimensions | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-2026-ARXIV-2605-04213 | exact-v1 disclosed workload for The Anatomy of Silent Data Corruption: GPU Error Pattern Study and Modeling Guidance | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-2026-ARXIV-2605-04215 | exact-v1 disclosed workload for Predict-then-Diffuse: Adaptive Response Length for Compute-Budgeted Inference in Diffusion LLMs | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-2026-ARXIV-2605-04236 | exact-v1 disclosed workload for Adaptive Consensus in LLM Ensembles via Sequential Evidence Accumulation: Automatic Budget Identification and Calibrated Commit Signals | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-2026-ARXIV-2605-04256 | exact-v1 disclosed workload for phys-MCP: A Control Plane for Heterogeneous Physical Neural Networks | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-2026-ARXIV-2605-04263 | exact-v1 disclosed workload for Parallel Prefix Verification for Speculative Generation | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-2026-ARXIV-2605-04264 | exact-v1 disclosed workload for Governed Collaborative Memory as Artificial Selection in LLM-Based Multi-Agent Systems | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-2026-ARXIV-2605-04266 | exact-v1 disclosed workload for Explaining and Preventing Alignment Collapse in Iterative RLHF | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-2026-ARXIV-2605-04269 | exact-v1 disclosed workload for Adapt or Forget: Provable Tradeoffs Between Adam and SGD in Nonstationary Optimization | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-2026-ARXIV-2605-04295 | exact-v1 disclosed workload for LLMs Uncertainty Quantification via Adaptive Conformal Semantic Entropy | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-2026-ARXIV-2605-04312 | exact-v1 disclosed workload for Agent Island: A Saturation- and Contamination-Resistant Benchmark from Multiagent Games | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-2026-ARXIV-2605-04333 | exact-v1 disclosed workload for Resilient AI Supercomputer Networking using MRC and SRv6 | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-2026-ARXIV-2605-04341 | exact-v1 disclosed workload for Budgeted LoRA: Distillation as Structured Compute Allocation for Efficient Inference | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-2026-ARXIV-2605-04357 | exact-v1 disclosed workload for Coral: Cost-Efficient Multi-LLM Serving over Heterogeneous Cloud GPUs | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-2026-ARXIV-2605-04361 | exact-v1 disclosed workload for When Context Hurts: The Crossover Effect of Knowledge Transfer on Multi-Agent Design Exploration | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-2026-ARXIV-2605-04373 | exact-v1 disclosed workload for Worst-Case Discovery and Runtime Protection for RL-Based Network Controllers | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-2026-ARXIV-2605-04375 | exact-v1 disclosed workload for Experiment-as-Code Labs: A Declarative Stack for AI-Driven Scientific Discovery | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-2026-ARXIV-2605-05248 | exact-v1 disclosed workload for Governed Metaprogramming for Intelligent Systems: Reclassifying Eval as a Governed Effect | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-2026-ARXIV-2605-05253 | exact-v1 disclosed workload for EnterpriseRAG-Bench: A RAG Benchmark for Company Internal Knowledge | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-2026-ARXIV-2605-08190 | exact-v1 disclosed workload for Synergistic Simplex: Cooperative Runtime Assurance for Safety-Critical Autonomous Systems | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-2026-ARXIV-2605-08192 | exact-v1 disclosed workload for NeurIPS Should Require Reproducibility Standards for Frontier AI Safety Claims | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-2026-ARXIV-2605-08195 | exact-v1 disclosed workload for ExecuTorch -- A Unified PyTorch Solution to Run AI Models On-Device | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-2026-ARXIV-2605-10959 | exact-v1 disclosed workload for QuIDE: Mastering the Quantized Intelligence Trade-off via Active Optimization | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-03275 | score_7_9 | not_selected | — | — | Full Source Review complete；本日报三项 Deep Analysis 优先覆盖更大的 execution/control-plane delta，本项由标准 Review 与 Books 对读闭合 | analysis-decision:SF-2026-ARXIV-2605-03275 |
| SF-2026-ARXIV-2605-03309 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 review remains complete; owner-local delta is retained in PLATFORM-SECURITY while the selected units cover the broader cross-stage transitions | analysis-decision:SF-2026-ARXIV-2605-03309 |
| SF-2026-ARXIV-2605-03310 | score_7_9 | not_selected | — | — | exact-v1 review remains complete; owner-local delta is retained in AGENT-MULTI-AGENT while the selected units cover the broader cross-stage transitions | analysis-decision:SF-2026-ARXIV-2605-03310 |
| SF-2026-ARXIV-2605-03312 | score_7_9 | not_selected | — | — | exact-v1 review remains complete; owner-local delta is retained in AGENT-MEMORY while the selected units cover the broader cross-stage transitions | analysis-decision:SF-2026-ARXIV-2605-03312 |
| SF-2026-ARXIV-2605-03314 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 review remains complete; owner-local delta is retained in AGENT-CONTEXT while the selected units cover the broader cross-stage transitions | analysis-decision:SF-2026-ARXIV-2605-03314 |
| SF-2026-ARXIV-2605-03327 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 review remains complete; owner-local delta is retained in TRAIN-GRPO while the selected units cover the broader cross-stage transitions | analysis-decision:SF-2026-ARXIV-2605-03327 |
| SF-2026-ARXIV-2605-03353 | score_7_9 | not_selected | — | — | exact-v1 review remains complete; owner-local delta is retained in AGENT-PLATFORM while the selected units cover the broader cross-stage transitions | analysis-decision:SF-2026-ARXIV-2605-03353 |
| SF-2026-ARXIV-2605-03354 | score_7_9 | not_selected | — | — | exact-v1 review remains complete; owner-local delta is retained in AGENT-MEMORY while the selected units cover the broader cross-stage transitions | analysis-decision:SF-2026-ARXIV-2605-03354 |
| SF-2026-ARXIV-2605-03375 | score_7_9 | selected | DA-GPU-OWNED-SSD-KV | — | selected because it changes cross-layer state/control ownership | analysis:DA-GPU-OWNED-SSD-KV |
| SF-2026-ARXIV-2605-03378 | score_7_9 | not_selected | — | — | exact-v1 review remains complete; owner-local delta is retained in PLATFORM-SECURITY while the selected units cover the broader cross-stage transitions | analysis-decision:SF-2026-ARXIV-2605-03378 |
| SF-2026-ARXIV-2605-03379 | score_7_9 | not_selected | — | — | exact-v1 review remains complete; owner-local delta is retained in PLATFORM-EVALUATION-SYSTEM while the selected units cover the broader cross-stage transitions | analysis-decision:SF-2026-ARXIV-2605-03379 |
| SF-2026-ARXIV-2605-03408 | score_7_9 | not_selected | — | — | exact-v1 review remains complete; owner-local delta is retained in TRAIN-RLHF while the selected units cover the broader cross-stage transitions | analysis-decision:SF-2026-ARXIV-2605-03408 |
| SF-2026-ARXIV-2605-03425 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 review remains complete; owner-local delta is retained in TRAIN-PRETRAINING while the selected units cover the broader cross-stage transitions | analysis-decision:SF-2026-ARXIV-2605-03425 |
| SF-2026-ARXIV-2605-03482 | score_7_9 | not_selected | — | — | exact-v1 review remains complete; owner-local delta is retained in PLATFORM-SECURITY while the selected units cover the broader cross-stage transitions | analysis-decision:SF-2026-ARXIV-2605-03482 |
| SF-2026-ARXIV-2605-03505 | score_7_9 | not_selected | — | — | exact-v1 review remains complete; owner-local delta is retained in PLATFORM-MONITORING while the selected units cover the broader cross-stage transitions | analysis-decision:SF-2026-ARXIV-2605-03505 |
| SF-2026-ARXIV-2605-03534 | score_7_9 | not_selected | — | — | exact-v1 review remains complete; owner-local delta is retained in AGENT-RAG while the selected units cover the broader cross-stage transitions | analysis-decision:SF-2026-ARXIV-2605-03534 |
| SF-2026-ARXIV-2605-03561 | score_7_9 | not_selected | — | — | exact-v1 review remains complete; owner-local delta is retained in PLATFORM-MONITORING while the selected units cover the broader cross-stage transitions | analysis-decision:SF-2026-ARXIV-2605-03561 |
| SF-2026-ARXIV-2605-03562 | score_7_9;forced_review;potential_books_delta | selected | DA-MODEL-VISIBLE-KV-ERROR | — | selected because it changes cross-layer state/control ownership | analysis:DA-MODEL-VISIBLE-KV-ERROR |
| SF-2026-ARXIV-2605-03566 | score_7_9 | not_selected | — | — | exact-v1 review remains complete; owner-local delta is retained in INFER-TENSORRT-LLM while the selected units cover the broader cross-stage transitions | analysis-decision:SF-2026-ARXIV-2605-03566 |
| SF-2026-ARXIV-2605-03596 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 review remains complete; owner-local delta is retained in PLATFORM-EVALUATION-SYSTEM while the selected units cover the broader cross-stage transitions | analysis-decision:SF-2026-ARXIV-2605-03596 |
| SF-2026-ARXIV-2605-03644 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 review remains complete; owner-local delta is retained in INFER-KV-CACHE while the selected units cover the broader cross-stage transitions | analysis-decision:SF-2026-ARXIV-2605-03644 |
| SF-2026-ARXIV-2605-03667 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 review remains complete; owner-local delta is retained in TRAIN-PRETRAINING while the selected units cover the broader cross-stage transitions | analysis-decision:SF-2026-ARXIV-2605-03667 |
| SF-2026-ARXIV-2605-03675 | score_7_9 | not_selected | — | — | exact-v1 review remains complete; owner-local delta is retained in AGENT-MEMORY while the selected units cover the broader cross-stage transitions | analysis-decision:SF-2026-ARXIV-2605-03675 |
| SF-2026-ARXIV-2605-03677 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 review remains complete; owner-local delta is retained in TRAIN-RLHF while the selected units cover the broader cross-stage transitions | analysis-decision:SF-2026-ARXIV-2605-03677 |
| SF-2026-ARXIV-2605-03762 | score_7_9 | not_selected | — | — | exact-v1 review remains complete; owner-local delta is retained in PLATFORM-EVALUATION-SYSTEM while the selected units cover the broader cross-stage transitions | analysis-decision:SF-2026-ARXIV-2605-03762 |
| SF-2026-ARXIV-2605-03838 | score_7_9 | not_selected | — | — | exact-v1 review remains complete; owner-local delta is retained in PLATFORM-EVALUATION-SYSTEM while the selected units cover the broader cross-stage transitions | analysis-decision:SF-2026-ARXIV-2605-03838 |
| SF-2026-ARXIV-2605-03858 | score_7_9 | not_selected | — | — | exact-v1 review remains complete; owner-local delta is retained in PLATFORM-EVALUATION-SYSTEM while the selected units cover the broader cross-stage transitions | analysis-decision:SF-2026-ARXIV-2605-03858 |
| SF-2026-ARXIV-2605-03862 | score_7_9 | not_selected | — | — | exact-v1 review remains complete; owner-local delta is retained in TRAIN-RLHF while the selected units cover the broader cross-stage transitions | analysis-decision:SF-2026-ARXIV-2605-03862 |
| SF-2026-ARXIV-2605-03884 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 review remains complete; owner-local delta is retained in AGENT-MULTI-AGENT while the selected units cover the broader cross-stage transitions | analysis-decision:SF-2026-ARXIV-2605-03884 |
| SF-2026-ARXIV-2605-03952 | score_7_9 | not_selected | — | — | exact-v1 review remains complete; owner-local delta is retained in PLATFORM-SECURITY while the selected units cover the broader cross-stage transitions | analysis-decision:SF-2026-ARXIV-2605-03952 |
| SF-2026-ARXIV-2605-03971 | score_7_9 | not_selected | — | — | exact-v1 review remains complete; owner-local delta is retained in PLATFORM-EVALUATION-SYSTEM while the selected units cover the broader cross-stage transitions | analysis-decision:SF-2026-ARXIV-2605-03971 |
| SF-2026-ARXIV-2605-03986 | score_7_9 | not_selected | — | — | exact-v1 review remains complete; owner-local delta is retained in AGENT-WORKFLOW while the selected units cover the broader cross-stage transitions | analysis-decision:SF-2026-ARXIV-2605-03986 |
| SF-2026-ARXIV-2605-04018 | score_7_9 | not_selected | — | — | exact-v1 review remains complete; owner-local delta is retained in AGENT-RAG while the selected units cover the broader cross-stage transitions | analysis-decision:SF-2026-ARXIV-2605-04018 |
| SF-2026-ARXIV-2605-04036 | score_7_9 | not_selected | — | — | exact-v1 review remains complete; owner-local delta is retained in TRAIN-SFT while the selected units cover the broader cross-stage transitions | analysis-decision:SF-2026-ARXIV-2605-04036 |
| SF-2026-ARXIV-2605-04039 | score_7_9 | not_selected | — | — | exact-v1 review remains complete; owner-local delta is retained in PLATFORM-EVALUATION-SYSTEM while the selected units cover the broader cross-stage transitions | analysis-decision:SF-2026-ARXIV-2605-04039 |
| SF-2026-ARXIV-2605-04116 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 review remains complete; owner-local delta is retained in PLATFORM-SECURITY while the selected units cover the broader cross-stage transitions | analysis-decision:SF-2026-ARXIV-2605-04116 |
| SF-2026-ARXIV-2605-04135 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 review remains complete; owner-local delta is retained in PLATFORM-EVALUATION-SYSTEM while the selected units cover the broader cross-stage transitions | analysis-decision:SF-2026-ARXIV-2605-04135 |
| SF-2026-ARXIV-2605-04172 | score_7_9 | not_selected | — | — | exact-v1 review remains complete; owner-local delta is retained in INFER-TENSORRT-LLM while the selected units cover the broader cross-stage transitions | analysis-decision:SF-2026-ARXIV-2605-04172 |
| SF-2026-ARXIV-2605-04178 | score_7_9 | not_selected | — | — | exact-v1 review remains complete; owner-local delta is retained in INFER-TENSORRT-LLM while the selected units cover the broader cross-stage transitions | analysis-decision:SF-2026-ARXIV-2605-04178 |
| SF-2026-ARXIV-2605-04209 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 review remains complete; owner-local delta is retained in PLATFORM-SECURITY while the selected units cover the broader cross-stage transitions | analysis-decision:SF-2026-ARXIV-2605-04209 |
| SF-2026-ARXIV-2605-04213 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 review remains complete; owner-local delta is retained in PLATFORM-MONITORING while the selected units cover the broader cross-stage transitions | analysis-decision:SF-2026-ARXIV-2605-04213 |
| SF-2026-ARXIV-2605-04215 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 review remains complete; owner-local delta is retained in MULTIMODAL-GENERATIVE-PARADIGMS while the selected units cover the broader cross-stage transitions | analysis-decision:SF-2026-ARXIV-2605-04215 |
| SF-2026-ARXIV-2605-04236 | score_7_9 | not_selected | — | — | exact-v1 review remains complete; owner-local delta is retained in PLATFORM-EVALUATION-SYSTEM while the selected units cover the broader cross-stage transitions | analysis-decision:SF-2026-ARXIV-2605-04236 |
| SF-2026-ARXIV-2605-04256 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 review remains complete; owner-local delta is retained in AGENT-MCP while the selected units cover the broader cross-stage transitions | analysis-decision:SF-2026-ARXIV-2605-04256 |
| SF-2026-ARXIV-2605-04263 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 review remains complete; owner-local delta is retained in INFER-SPECULATIVE-DECODING while the selected units cover the broader cross-stage transitions | analysis-decision:SF-2026-ARXIV-2605-04263 |
| SF-2026-ARXIV-2605-04264 | score_7_9 | not_selected | — | — | exact-v1 review remains complete; owner-local delta is retained in AGENT-MEMORY while the selected units cover the broader cross-stage transitions | analysis-decision:SF-2026-ARXIV-2605-04264 |
| SF-2026-ARXIV-2605-04266 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 review remains complete; owner-local delta is retained in TRAIN-RLHF while the selected units cover the broader cross-stage transitions | analysis-decision:SF-2026-ARXIV-2605-04266 |
| SF-2026-ARXIV-2605-04269 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 review remains complete; owner-local delta is retained in TRAIN-PRETRAINING while the selected units cover the broader cross-stage transitions | analysis-decision:SF-2026-ARXIV-2605-04269 |
| SF-2026-ARXIV-2605-04295 | score_7_9 | not_selected | — | — | exact-v1 review remains complete; owner-local delta is retained in PLATFORM-EVALUATION-SYSTEM while the selected units cover the broader cross-stage transitions | analysis-decision:SF-2026-ARXIV-2605-04295 |
| SF-2026-ARXIV-2605-04312 | score_7_9 | not_selected | — | — | exact-v1 review remains complete; owner-local delta is retained in PLATFORM-EVALUATION-SYSTEM while the selected units cover the broader cross-stage transitions | analysis-decision:SF-2026-ARXIV-2605-04312 |
| SF-2026-ARXIV-2605-04333 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 review remains complete; owner-local delta is retained in TRAIN-DISTRIBUTED-TRAINING while the selected units cover the broader cross-stage transitions | analysis-decision:SF-2026-ARXIV-2605-04333 |
| SF-2026-ARXIV-2605-04341 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 review remains complete; owner-local delta is retained in TRAIN-LORA while the selected units cover the broader cross-stage transitions | analysis-decision:SF-2026-ARXIV-2605-04341 |
| SF-2026-ARXIV-2605-04357 | score_7_9;forced_review;potential_books_delta | selected | DA-HETERO-MULTI-LLM-CONTROL | — | selected because it changes cross-layer state/control ownership | analysis:DA-HETERO-MULTI-LLM-CONTROL |
| SF-2026-ARXIV-2605-04361 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 review remains complete; owner-local delta is retained in AGENT-CONTEXT while the selected units cover the broader cross-stage transitions | analysis-decision:SF-2026-ARXIV-2605-04361 |
| SF-2026-ARXIV-2605-04373 | score_7_9 | not_selected | — | — | exact-v1 review remains complete; owner-local delta is retained in PLATFORM-SECURITY while the selected units cover the broader cross-stage transitions | analysis-decision:SF-2026-ARXIV-2605-04373 |
| SF-2026-ARXIV-2605-04375 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 review remains complete; owner-local delta is retained in AGENT-WORKFLOW while the selected units cover the broader cross-stage transitions | analysis-decision:SF-2026-ARXIV-2605-04375 |
| SF-2026-ARXIV-2605-05248 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 review remains complete; owner-local delta is retained in AGENT-WORKFLOW while the selected units cover the broader cross-stage transitions | analysis-decision:SF-2026-ARXIV-2605-05248 |
| SF-2026-ARXIV-2605-05253 | score_7_9 | not_selected | — | — | exact-v1 review remains complete; owner-local delta is retained in AGENT-RAG while the selected units cover the broader cross-stage transitions | analysis-decision:SF-2026-ARXIV-2605-05253 |
| SF-2026-ARXIV-2605-08190 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 review remains complete; owner-local delta is retained in MULTIMODAL-EMBODIED-VLA while the selected units cover the broader cross-stage transitions | analysis-decision:SF-2026-ARXIV-2605-08190 |
| SF-2026-ARXIV-2605-08192 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 review remains complete; owner-local delta is retained in PLATFORM-EVALUATION-SYSTEM while the selected units cover the broader cross-stage transitions | analysis-decision:SF-2026-ARXIV-2605-08192 |
| SF-2026-ARXIV-2605-08195 | score_7_9 | not_selected | — | — | exact-v1 review remains complete; owner-local delta is retained in INFER-TENSORRT-LLM while the selected units cover the broader cross-stage transitions | analysis-decision:SF-2026-ARXIV-2605-08195 |

<!-- analysis:DA-GPU-OWNED-SSD-KV:start -->
### SSD KV：从 CPU 发起 I/O 到 GPU 拥有数据与控制路径

GDS 仍由 CPU 为大量碎片 I/O 发起请求，在长上下文 prefix restore 中，GPU 等待的是控制路径而不只是介质带宽。Tutti 将 KV 封装为 GPU-native object，由 GPU io_uring 批量提交，并以 slack-aware policy 避免 I/O kernel 与推理 kernel 争抢。收益是把 SSD bandwidth 变成可用 cache tier；代价是 GPU 侧 object metadata、I/O kernel 生命周期和 contention policy。小 cache、低复用或 CPU 不成为瓶颈时，DRAM/普通 GDS 仍更简单。
<!-- analysis:DA-GPU-OWNED-SSD-KV:end -->

<!-- analysis:DA-MODEL-VISIBLE-KV-ERROR:start -->
### KV 量化：从存储误差到消费算子可见误差

最小化 K/V 的 raw MSE 在实现上简单，却把 attention 根本看不到的 key 平移与正交残差也视为同等重要。HeadQ 将 K 的目标改成 softmax 前 score-space，把 V 的目标改成 attention-weighted readout，并用 calibration query basis 保存低秩 residual。收益是预算花在行为可见坐标；代价是 calibration drift、side-code metadata 和额外 logit correction。论文主结果仍是 K-only、dense V、Python eager hooks，不证明 packed-kernel latency。
<!-- analysis:DA-MODEL-VISIBLE-KV-ERROR:end -->

<!-- analysis:DA-HETERO-MULTI-LLM-CONTROL:start -->
### 多模型异构 Serving：从逐模型 placement 到共同资源控制

逐模型独立选择最便宜 GPU 在资源充足、模型少时合理；共享稀缺 GPU 时会造成局部最优抢占和其他模型 SLO 不可行。Coral 把 `(model,SLO,node-combination,placement)` 固化为 offline Serving Template，再由 online allocator 在价格、供给和 demand 变化下共同选择。它把昂贵 placement search 移出在线路径，但新增 profile freshness、template coverage、迁移与重配置成本；其 6 模型、20 配置结果不能外推到任意互联与跨区域拓扑。
<!-- analysis:DA-HETERO-MULTI-LLM-CONTROL:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-03275:start -->SF-2026-ARXIV-2605-03275 已完成 body-level Source Review；未进入三项 Deep Analysis 不是跳过，而是因为其 durable delta 已由 `AGENT-RAG` 的现有 transaction/ACL/freshness 主线承载。<!-- analysis-decision:SF-2026-ARXIV-2605-03275:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-03309:start -->SF-2026-ARXIV-2605-03309 已完成 exact-v1 Review；不扩写只表示其 delta 更局部，不表示跳过 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-03309:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-03310:start -->SF-2026-ARXIV-2605-03310 已完成 exact-v1 Review；不扩写只表示其 delta 更局部，不表示跳过 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-03310:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-03312:start -->SF-2026-ARXIV-2605-03312 已完成 exact-v1 Review；不扩写只表示其 delta 更局部，不表示跳过 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-03312:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-03314:start -->SF-2026-ARXIV-2605-03314 已完成 exact-v1 Review；不扩写只表示其 delta 更局部，不表示跳过 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-03314:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-03327:start -->SF-2026-ARXIV-2605-03327 已完成 exact-v1 Review；不扩写只表示其 delta 更局部，不表示跳过 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-03327:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-03353:start -->SF-2026-ARXIV-2605-03353 已完成 exact-v1 Review；不扩写只表示其 delta 更局部，不表示跳过 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-03353:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-03354:start -->SF-2026-ARXIV-2605-03354 已完成 exact-v1 Review；不扩写只表示其 delta 更局部，不表示跳过 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-03354:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-03378:start -->SF-2026-ARXIV-2605-03378 已完成 exact-v1 Review；不扩写只表示其 delta 更局部，不表示跳过 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-03378:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-03379:start -->SF-2026-ARXIV-2605-03379 已完成 exact-v1 Review；不扩写只表示其 delta 更局部，不表示跳过 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-03379:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-03408:start -->SF-2026-ARXIV-2605-03408 已完成 exact-v1 Review；不扩写只表示其 delta 更局部，不表示跳过 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-03408:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-03425:start -->SF-2026-ARXIV-2605-03425 已完成 exact-v1 Review；不扩写只表示其 delta 更局部，不表示跳过 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-03425:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-03482:start -->SF-2026-ARXIV-2605-03482 已完成 exact-v1 Review；不扩写只表示其 delta 更局部，不表示跳过 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-03482:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-03505:start -->SF-2026-ARXIV-2605-03505 已完成 exact-v1 Review；不扩写只表示其 delta 更局部，不表示跳过 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-03505:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-03534:start -->SF-2026-ARXIV-2605-03534 已完成 exact-v1 Review；不扩写只表示其 delta 更局部，不表示跳过 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-03534:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-03561:start -->SF-2026-ARXIV-2605-03561 已完成 exact-v1 Review；不扩写只表示其 delta 更局部，不表示跳过 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-03561:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-03566:start -->SF-2026-ARXIV-2605-03566 已完成 exact-v1 Review；不扩写只表示其 delta 更局部，不表示跳过 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-03566:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-03596:start -->SF-2026-ARXIV-2605-03596 已完成 exact-v1 Review；不扩写只表示其 delta 更局部，不表示跳过 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-03596:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-03644:start -->SF-2026-ARXIV-2605-03644 已完成 exact-v1 Review；不扩写只表示其 delta 更局部，不表示跳过 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-03644:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-03667:start -->SF-2026-ARXIV-2605-03667 已完成 exact-v1 Review；不扩写只表示其 delta 更局部，不表示跳过 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-03667:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-03675:start -->SF-2026-ARXIV-2605-03675 已完成 exact-v1 Review；不扩写只表示其 delta 更局部，不表示跳过 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-03675:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-03677:start -->SF-2026-ARXIV-2605-03677 已完成 exact-v1 Review；不扩写只表示其 delta 更局部，不表示跳过 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-03677:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-03762:start -->SF-2026-ARXIV-2605-03762 已完成 exact-v1 Review；不扩写只表示其 delta 更局部，不表示跳过 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-03762:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-03838:start -->SF-2026-ARXIV-2605-03838 已完成 exact-v1 Review；不扩写只表示其 delta 更局部，不表示跳过 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-03838:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-03858:start -->SF-2026-ARXIV-2605-03858 已完成 exact-v1 Review；不扩写只表示其 delta 更局部，不表示跳过 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-03858:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-03862:start -->SF-2026-ARXIV-2605-03862 已完成 exact-v1 Review；不扩写只表示其 delta 更局部，不表示跳过 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-03862:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-03884:start -->SF-2026-ARXIV-2605-03884 已完成 exact-v1 Review；不扩写只表示其 delta 更局部，不表示跳过 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-03884:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-03952:start -->SF-2026-ARXIV-2605-03952 已完成 exact-v1 Review；不扩写只表示其 delta 更局部，不表示跳过 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-03952:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-03971:start -->SF-2026-ARXIV-2605-03971 已完成 exact-v1 Review；不扩写只表示其 delta 更局部，不表示跳过 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-03971:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-03986:start -->SF-2026-ARXIV-2605-03986 已完成 exact-v1 Review；不扩写只表示其 delta 更局部，不表示跳过 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-03986:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-04018:start -->SF-2026-ARXIV-2605-04018 已完成 exact-v1 Review；不扩写只表示其 delta 更局部，不表示跳过 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-04018:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-04019:start -->SF-2026-ARXIV-2605-04019 已完成 exact-v1 Review；不扩写只表示其 delta 更局部，不表示跳过 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-04019:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-04036:start -->SF-2026-ARXIV-2605-04036 已完成 exact-v1 Review；不扩写只表示其 delta 更局部，不表示跳过 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-04036:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-04039:start -->SF-2026-ARXIV-2605-04039 已完成 exact-v1 Review；不扩写只表示其 delta 更局部，不表示跳过 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-04039:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-04116:start -->SF-2026-ARXIV-2605-04116 已完成 exact-v1 Review；不扩写只表示其 delta 更局部，不表示跳过 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-04116:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-04135:start -->SF-2026-ARXIV-2605-04135 已完成 exact-v1 Review；不扩写只表示其 delta 更局部，不表示跳过 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-04135:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-04172:start -->SF-2026-ARXIV-2605-04172 已完成 exact-v1 Review；不扩写只表示其 delta 更局部，不表示跳过 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-04172:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-04178:start -->SF-2026-ARXIV-2605-04178 已完成 exact-v1 Review；不扩写只表示其 delta 更局部，不表示跳过 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-04178:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-04209:start -->SF-2026-ARXIV-2605-04209 已完成 exact-v1 Review；不扩写只表示其 delta 更局部，不表示跳过 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-04209:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-04213:start -->SF-2026-ARXIV-2605-04213 已完成 exact-v1 Review；不扩写只表示其 delta 更局部，不表示跳过 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-04213:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-04215:start -->SF-2026-ARXIV-2605-04215 已完成 exact-v1 Review；不扩写只表示其 delta 更局部，不表示跳过 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-04215:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-04236:start -->SF-2026-ARXIV-2605-04236 已完成 exact-v1 Review；不扩写只表示其 delta 更局部，不表示跳过 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-04236:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-04256:start -->SF-2026-ARXIV-2605-04256 已完成 exact-v1 Review；不扩写只表示其 delta 更局部，不表示跳过 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-04256:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-04263:start -->SF-2026-ARXIV-2605-04263 已完成 exact-v1 Review；不扩写只表示其 delta 更局部，不表示跳过 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-04263:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-04264:start -->SF-2026-ARXIV-2605-04264 已完成 exact-v1 Review；不扩写只表示其 delta 更局部，不表示跳过 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-04264:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-04266:start -->SF-2026-ARXIV-2605-04266 已完成 exact-v1 Review；不扩写只表示其 delta 更局部，不表示跳过 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-04266:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-04269:start -->SF-2026-ARXIV-2605-04269 已完成 exact-v1 Review；不扩写只表示其 delta 更局部，不表示跳过 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-04269:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-04295:start -->SF-2026-ARXIV-2605-04295 已完成 exact-v1 Review；不扩写只表示其 delta 更局部，不表示跳过 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-04295:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-04312:start -->SF-2026-ARXIV-2605-04312 已完成 exact-v1 Review；不扩写只表示其 delta 更局部，不表示跳过 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-04312:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-04333:start -->SF-2026-ARXIV-2605-04333 已完成 exact-v1 Review；不扩写只表示其 delta 更局部，不表示跳过 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-04333:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-04341:start -->SF-2026-ARXIV-2605-04341 已完成 exact-v1 Review；不扩写只表示其 delta 更局部，不表示跳过 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-04341:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-04361:start -->SF-2026-ARXIV-2605-04361 已完成 exact-v1 Review；不扩写只表示其 delta 更局部，不表示跳过 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-04361:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-04373:start -->SF-2026-ARXIV-2605-04373 已完成 exact-v1 Review；不扩写只表示其 delta 更局部，不表示跳过 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-04373:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-04375:start -->SF-2026-ARXIV-2605-04375 已完成 exact-v1 Review；不扩写只表示其 delta 更局部，不表示跳过 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-04375:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-05248:start -->SF-2026-ARXIV-2605-05248 已完成 exact-v1 Review；不扩写只表示其 delta 更局部，不表示跳过 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-05248:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-05253:start -->SF-2026-ARXIV-2605-05253 已完成 exact-v1 Review；不扩写只表示其 delta 更局部，不表示跳过 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-05253:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-08190:start -->SF-2026-ARXIV-2605-08190 已完成 exact-v1 Review；不扩写只表示其 delta 更局部，不表示跳过 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-08190:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-08192:start -->SF-2026-ARXIV-2605-08192 已完成 exact-v1 Review；不扩写只表示其 delta 更局部，不表示跳过 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-08192:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-08195:start -->SF-2026-ARXIV-2605-08195 已完成 exact-v1 Review；不扩写只表示其 delta 更局部，不表示跳过 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-08195:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-10959:start -->SF-2026-ARXIV-2605-10959 已完成 exact-v1 Review；不扩写只表示其 delta 更局部，不表示跳过 Source Review。<!-- analysis-decision:SF-2026-ARXIV-2605-10959:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-03275 | AGENT-RAG | books/part-07-agent/76-rag.md#chapter-76 | books/part-07-agent/75-context.md#chapter-75; books/part-07-agent/77-memory.md#chapter-77 | existing:SF-2026-ARXIV-2605-03275 | delta:SF-2026-ARXIV-2605-03275 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-03275 |
| SF-2026-ARXIV-2605-03309 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-03309 | delta:SF-2026-ARXIV-2605-03309 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-03309 |
| SF-2026-ARXIV-2605-03310 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#chapter-82 | books/part-07-agent/81-workflow.md#chapter-81; books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-03310 | delta:SF-2026-ARXIV-2605-03310 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-03310 |
| SF-2026-ARXIV-2605-03312 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76; books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-03312 | delta:SF-2026-ARXIV-2605-03312 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-03312 |
| SF-2026-ARXIV-2605-03314 | AGENT-CONTEXT | books/part-07-agent/75-context.md#chapter-75 | books/part-07-agent/74-prompt.md#chapter-74; books/part-07-agent/76-rag.md#chapter-76 | existing:SF-2026-ARXIV-2605-03314 | delta:SF-2026-ARXIV-2605-03314 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-03314 |
| SF-2026-ARXIV-2605-03327 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#chapter-33 | books/part-04-training-system/32-ppo.md#chapter-32; books/part-04-training-system/34-dpo.md#chapter-34 | existing:SF-2026-ARXIV-2605-03327 | delta:SF-2026-ARXIV-2605-03327 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-03327 |
| SF-2026-ARXIV-2605-03353 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-03353 | delta:SF-2026-ARXIV-2605-03353 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-03353 |
| SF-2026-ARXIV-2605-03354 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76; books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-03354 | delta:SF-2026-ARXIV-2605-03354 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-03354 |
| SF-2026-ARXIV-2605-03375 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#chapter-45 | books/part-05-inference-system/44-decode.md#chapter-44; books/part-05-inference-system/46-continuous-batching.md#chapter-46 | existing:SF-2026-ARXIV-2605-03375 | delta:SF-2026-ARXIV-2605-03375 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-03375 |
| SF-2026-ARXIV-2605-03378 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-03378 | delta:SF-2026-ARXIV-2605-03378 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-03378 |
| SF-2026-ARXIV-2605-03379 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-03379 | delta:SF-2026-ARXIV-2605-03379 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-03379 |
| SF-2026-ARXIV-2605-03408 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#chapter-31 | books/part-04-training-system/30-lora.md#chapter-30; books/part-04-training-system/32-ppo.md#chapter-32 | existing:SF-2026-ARXIV-2605-03408 | delta:SF-2026-ARXIV-2605-03408 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-03408 |
| SF-2026-ARXIV-2605-03425 | TRAIN-PRETRAINING | books/part-04-training-system/28-pretraining.md#chapter-28 | books/part-04-training-system/27-data.md#chapter-27; books/part-04-training-system/29-sft.md#chapter-29 | existing:SF-2026-ARXIV-2605-03425 | delta:SF-2026-ARXIV-2605-03425 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-03425 |
| SF-2026-ARXIV-2605-03482 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-03482 | delta:SF-2026-ARXIV-2605-03482 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-03482 |
| SF-2026-ARXIV-2605-03505 | PLATFORM-MONITORING | books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66; books/part-06-ai-infrastructure/68-logging.md#chapter-68 | existing:SF-2026-ARXIV-2605-03505 | delta:SF-2026-ARXIV-2605-03505 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-03505 |
| SF-2026-ARXIV-2605-03534 | AGENT-RAG | books/part-07-agent/76-rag.md#chapter-76 | books/part-07-agent/75-context.md#chapter-75; books/part-07-agent/77-memory.md#chapter-77 | existing:SF-2026-ARXIV-2605-03534 | delta:SF-2026-ARXIV-2605-03534 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-03534 |
| SF-2026-ARXIV-2605-03561 | PLATFORM-MONITORING | books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66; books/part-06-ai-infrastructure/68-logging.md#chapter-68 | existing:SF-2026-ARXIV-2605-03561 | delta:SF-2026-ARXIV-2605-03561 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-03561 |
| SF-2026-ARXIV-2605-03562 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#chapter-45 | books/part-05-inference-system/44-decode.md#chapter-44; books/part-05-inference-system/46-continuous-batching.md#chapter-46 | existing:SF-2026-ARXIV-2605-03562 | delta:SF-2026-ARXIV-2605-03562 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-03562 |
| SF-2026-ARXIV-2605-03566 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | books/part-05-inference-system/48-speculative-decoding.md#chapter-48; books/part-05-inference-system/50-vllm.md#chapter-50 | existing:SF-2026-ARXIV-2605-03566 | delta:SF-2026-ARXIV-2605-03566 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-03566 |
| SF-2026-ARXIV-2605-03596 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-03596 | delta:SF-2026-ARXIV-2605-03596 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-03596 |
| SF-2026-ARXIV-2605-03644 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#chapter-45 | books/part-05-inference-system/44-decode.md#chapter-44; books/part-05-inference-system/46-continuous-batching.md#chapter-46 | existing:SF-2026-ARXIV-2605-03644 | delta:SF-2026-ARXIV-2605-03644 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-03644 |
| SF-2026-ARXIV-2605-03667 | TRAIN-PRETRAINING | books/part-04-training-system/28-pretraining.md#chapter-28 | books/part-04-training-system/27-data.md#chapter-27; books/part-04-training-system/29-sft.md#chapter-29 | existing:SF-2026-ARXIV-2605-03667 | delta:SF-2026-ARXIV-2605-03667 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-03667 |
| SF-2026-ARXIV-2605-03675 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76; books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-03675 | delta:SF-2026-ARXIV-2605-03675 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-03675 |
| SF-2026-ARXIV-2605-03677 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#chapter-31 | books/part-04-training-system/30-lora.md#chapter-30; books/part-04-training-system/32-ppo.md#chapter-32 | existing:SF-2026-ARXIV-2605-03677 | delta:SF-2026-ARXIV-2605-03677 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-03677 |
| SF-2026-ARXIV-2605-03762 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-03762 | delta:SF-2026-ARXIV-2605-03762 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-03762 |
| SF-2026-ARXIV-2605-03838 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-03838 | delta:SF-2026-ARXIV-2605-03838 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-03838 |
| SF-2026-ARXIV-2605-03858 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-03858 | delta:SF-2026-ARXIV-2605-03858 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-03858 |
| SF-2026-ARXIV-2605-03862 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#chapter-31 | books/part-04-training-system/30-lora.md#chapter-30; books/part-04-training-system/32-ppo.md#chapter-32 | existing:SF-2026-ARXIV-2605-03862 | delta:SF-2026-ARXIV-2605-03862 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-03862 |
| SF-2026-ARXIV-2605-03884 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#chapter-82 | books/part-07-agent/81-workflow.md#chapter-81; books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-03884 | delta:SF-2026-ARXIV-2605-03884 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-03884 |
| SF-2026-ARXIV-2605-03952 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-03952 | delta:SF-2026-ARXIV-2605-03952 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-03952 |
| SF-2026-ARXIV-2605-03971 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-03971 | delta:SF-2026-ARXIV-2605-03971 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-03971 |
| SF-2026-ARXIV-2605-03986 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#chapter-81 | books/part-07-agent/80-reflection.md#chapter-80; books/part-07-agent/82-multi-agent.md#chapter-82 | existing:SF-2026-ARXIV-2605-03986 | delta:SF-2026-ARXIV-2605-03986 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-03986 |
| SF-2026-ARXIV-2605-04018 | AGENT-RAG | books/part-07-agent/76-rag.md#chapter-76 | books/part-07-agent/75-context.md#chapter-75; books/part-07-agent/77-memory.md#chapter-77 | existing:SF-2026-ARXIV-2605-04018 | delta:SF-2026-ARXIV-2605-04018 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-04018 |
| SF-2026-ARXIV-2605-04019 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-04019 | delta:SF-2026-ARXIV-2605-04019 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-04019 |
| SF-2026-ARXIV-2605-04036 | TRAIN-SFT | books/part-04-training-system/29-sft.md#chapter-29 | books/part-04-training-system/28-pretraining.md#chapter-28; books/part-04-training-system/30-lora.md#chapter-30 | existing:SF-2026-ARXIV-2605-04036 | delta:SF-2026-ARXIV-2605-04036 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-04036 |
| SF-2026-ARXIV-2605-04039 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-04039 | delta:SF-2026-ARXIV-2605-04039 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-04039 |
| SF-2026-ARXIV-2605-04116 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-04116 | delta:SF-2026-ARXIV-2605-04116 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-04116 |
| SF-2026-ARXIV-2605-04135 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-04135 | delta:SF-2026-ARXIV-2605-04135 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-04135 |
| SF-2026-ARXIV-2605-04172 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | books/part-05-inference-system/48-speculative-decoding.md#chapter-48; books/part-05-inference-system/50-vllm.md#chapter-50 | existing:SF-2026-ARXIV-2605-04172 | delta:SF-2026-ARXIV-2605-04172 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-04172 |
| SF-2026-ARXIV-2605-04178 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | books/part-05-inference-system/48-speculative-decoding.md#chapter-48; books/part-05-inference-system/50-vllm.md#chapter-50 | existing:SF-2026-ARXIV-2605-04178 | delta:SF-2026-ARXIV-2605-04178 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-04178 |
| SF-2026-ARXIV-2605-04209 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-04209 | delta:SF-2026-ARXIV-2605-04209 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-04209 |
| SF-2026-ARXIV-2605-04213 | PLATFORM-MONITORING | books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66; books/part-06-ai-infrastructure/68-logging.md#chapter-68 | existing:SF-2026-ARXIV-2605-04213 | delta:SF-2026-ARXIV-2605-04213 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-04213 |
| SF-2026-ARXIV-2605-04215 | MULTIMODAL-GENERATIVE-PARADIGMS | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24 | books/part-03-multimodal-world-models/23-multimodal-representation.md#chapter-23; books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | existing:SF-2026-ARXIV-2605-04215 | delta:SF-2026-ARXIV-2605-04215 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-04215 |
| SF-2026-ARXIV-2605-04236 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-04236 | delta:SF-2026-ARXIV-2605-04236 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-04236 |
| SF-2026-ARXIV-2605-04256 | AGENT-MCP | books/part-07-agent/83-mcp.md#chapter-83 | books/part-07-agent/82-multi-agent.md#chapter-82; books/part-07-agent/84-agent-platform.md#chapter-84 | existing:SF-2026-ARXIV-2605-04256 | delta:SF-2026-ARXIV-2605-04256 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-04256 |
| SF-2026-ARXIV-2605-04263 | INFER-SPECULATIVE-DECODING | books/part-05-inference-system/48-speculative-decoding.md#chapter-48 | books/part-05-inference-system/47-pagedattention.md#chapter-47; books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | existing:SF-2026-ARXIV-2605-04263 | delta:SF-2026-ARXIV-2605-04263 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-04263 |
| SF-2026-ARXIV-2605-04264 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76; books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-04264 | delta:SF-2026-ARXIV-2605-04264 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-04264 |
| SF-2026-ARXIV-2605-04266 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#chapter-31 | books/part-04-training-system/30-lora.md#chapter-30; books/part-04-training-system/32-ppo.md#chapter-32 | existing:SF-2026-ARXIV-2605-04266 | delta:SF-2026-ARXIV-2605-04266 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-04266 |
| SF-2026-ARXIV-2605-04269 | TRAIN-PRETRAINING | books/part-04-training-system/28-pretraining.md#chapter-28 | books/part-04-training-system/27-data.md#chapter-27; books/part-04-training-system/29-sft.md#chapter-29 | existing:SF-2026-ARXIV-2605-04269 | delta:SF-2026-ARXIV-2605-04269 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-04269 |
| SF-2026-ARXIV-2605-04295 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-04295 | delta:SF-2026-ARXIV-2605-04295 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-04295 |
| SF-2026-ARXIV-2605-04312 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-04312 | delta:SF-2026-ARXIV-2605-04312 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-04312 |
| SF-2026-ARXIV-2605-04333 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#chapter-36 | books/part-04-training-system/35-checkpoint.md#chapter-35; books/part-04-training-system/37-tensor-parallel.md#chapter-37 | existing:SF-2026-ARXIV-2605-04333 | delta:SF-2026-ARXIV-2605-04333 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-04333 |
| SF-2026-ARXIV-2605-04341 | TRAIN-LORA | books/part-04-training-system/30-lora.md#chapter-30 | books/part-04-training-system/29-sft.md#chapter-29; books/part-04-training-system/31-rlhf.md#chapter-31 | existing:SF-2026-ARXIV-2605-04341 | delta:SF-2026-ARXIV-2605-04341 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-04341 |
| SF-2026-ARXIV-2605-04357 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#chapter-56 | books/part-05-inference-system/55-pd-disaggregation.md#chapter-55 | existing:SF-2026-ARXIV-2605-04357 | delta:SF-2026-ARXIV-2605-04357 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-04357 |
| SF-2026-ARXIV-2605-04361 | AGENT-CONTEXT | books/part-07-agent/75-context.md#chapter-75 | books/part-07-agent/74-prompt.md#chapter-74; books/part-07-agent/76-rag.md#chapter-76 | existing:SF-2026-ARXIV-2605-04361 | delta:SF-2026-ARXIV-2605-04361 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-04361 |
| SF-2026-ARXIV-2605-04373 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-04373 | delta:SF-2026-ARXIV-2605-04373 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-04373 |
| SF-2026-ARXIV-2605-04375 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#chapter-81 | books/part-07-agent/80-reflection.md#chapter-80; books/part-07-agent/82-multi-agent.md#chapter-82 | existing:SF-2026-ARXIV-2605-04375 | delta:SF-2026-ARXIV-2605-04375 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-04375 |
| SF-2026-ARXIV-2605-05248 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#chapter-81 | books/part-07-agent/80-reflection.md#chapter-80; books/part-07-agent/82-multi-agent.md#chapter-82 | existing:SF-2026-ARXIV-2605-05248 | delta:SF-2026-ARXIV-2605-05248 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-05248 |
| SF-2026-ARXIV-2605-05253 | AGENT-RAG | books/part-07-agent/76-rag.md#chapter-76 | books/part-07-agent/75-context.md#chapter-75; books/part-07-agent/77-memory.md#chapter-77 | existing:SF-2026-ARXIV-2605-05253 | delta:SF-2026-ARXIV-2605-05253 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-05253 |
| SF-2026-ARXIV-2605-08190 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | existing:SF-2026-ARXIV-2605-08190 | delta:SF-2026-ARXIV-2605-08190 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-08190 |
| SF-2026-ARXIV-2605-08192 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-08192 | delta:SF-2026-ARXIV-2605-08192 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-08192 |
| SF-2026-ARXIV-2605-08195 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | books/part-05-inference-system/48-speculative-decoding.md#chapter-48; books/part-05-inference-system/50-vllm.md#chapter-50 | existing:SF-2026-ARXIV-2605-08195 | delta:SF-2026-ARXIV-2605-08195 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-08195 |
| SF-2026-ARXIV-2605-10959 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | books/part-05-inference-system/48-speculative-decoding.md#chapter-48; books/part-05-inference-system/50-vllm.md#chapter-50 | existing:SF-2026-ARXIV-2605-10959 | delta:SF-2026-ARXIV-2605-10959 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-10959 |
<!-- books-review:SF-2026-ARXIV-2605-03275:start -->
<!-- existing:SF-2026-ARXIV-2605-03275:start -->已对读 `AGENT-RAG` 与相邻 Context/Memory 章节。Ch76 已明确：ACL/tenant filter 必须在 candidate admission 前执行，增量更新需要 atomic publication/version semantics，storage/index 选择必须绑定 query constraint 与 scale。<!-- existing:SF-2026-ARXIV-2605-03275:end -->
<!-- delta:SF-2026-ARXIV-2605-03275:start -->恢复全文把证据边界收紧为受控 PostgreSQL 模拟：统一 transaction/query ownership 可消除该设置中的同步窗口与应用层过滤脆弱性，但不证明 PostgreSQL 对所有向量库、硬件、规模和 SLO 都更优；specialized ANN 与 hybrid tier 继续共存。<!-- delta:SF-2026-ARXIV-2605-03275:end --> Decision: `No Change — Existing Coverage`；不重复写入 Books。
<!-- books-review:SF-2026-ARXIV-2605-03275:end -->
<!-- books-review:SF-2026-ARXIV-2605-03309:start -->
<!-- existing:SF-2026-ARXIV-2605-03309:start -->已读取 `PLATFORM-SECURITY` 当前 owner 与相邻章节；旧路径在固定 workload、低风险或规模较小时仍成立。<!-- existing:SF-2026-ARXIV-2605-03309:end -->
<!-- delta:SF-2026-ARXIV-2605-03309:start -->artifact distribution needs cryptographic registry identity, publisher/registry countersignatures and namespace-bound fail-closed resolution<!-- delta:SF-2026-ARXIV-2605-03309:end --> Decision: `Integrate`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-03309:end -->
<!-- books-review:SF-2026-ARXIV-2605-03310:start -->
<!-- existing:SF-2026-ARXIV-2605-03310:start -->已读取 `AGENT-MULTI-AGENT` 当前 owner 与相邻章节；旧路径在固定 workload、低风险或规模较小时仍成立。<!-- existing:SF-2026-ARXIV-2605-03310:end -->
<!-- delta:SF-2026-ARXIV-2605-03310:start -->multi-agent coordination is a configurable architecture whose information topology, compute allocation and aggregation leave distinct failure signatures<!-- delta:SF-2026-ARXIV-2605-03310:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-03310:end -->
<!-- books-review:SF-2026-ARXIV-2605-03312:start -->
<!-- existing:SF-2026-ARXIV-2605-03312:start -->已读取 `AGENT-MEMORY` 当前 owner 与相邻章节；旧路径在固定 workload、低风险或规模较小时仍成立。<!-- existing:SF-2026-ARXIV-2605-03312:end -->
<!-- delta:SF-2026-ARXIV-2605-03312:start -->limited-capacity agents need intent-routed memory tiers, deterministic evidence compilation and validator-owned escalation instead of open-ended memory tool loops<!-- delta:SF-2026-ARXIV-2605-03312:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-03312:end -->
<!-- books-review:SF-2026-ARXIV-2605-03314:start -->
<!-- existing:SF-2026-ARXIV-2605-03314:start -->已读取 `AGENT-CONTEXT` 当前 owner 与相邻章节；旧路径在固定 workload、低风险或规模较小时仍成立。<!-- existing:SF-2026-ARXIV-2605-03314:end -->
<!-- delta:SF-2026-ARXIV-2605-03314:start -->public disclosure is an irreversible commitment distinct from private reasoning state, so visibility timing becomes a learned control decision with an entailment gate<!-- delta:SF-2026-ARXIV-2605-03314:end --> Decision: `Integrate`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-03314:end -->
<!-- books-review:SF-2026-ARXIV-2605-03327:start -->
<!-- existing:SF-2026-ARXIV-2605-03327:start -->已读取 `TRAIN-GRPO` 当前 owner 与相邻章节；旧路径在固定 workload、低风险或规模较小时仍成立。<!-- existing:SF-2026-ARXIV-2605-03327:end -->
<!-- delta:SF-2026-ARXIV-2605-03327:start -->fine-grained reasoning credit can be redistributed from sequence reward with a bounded distributional distance and an entropy gate, trading additional statistics and calibration for less diffuse token updates<!-- delta:SF-2026-ARXIV-2605-03327:end --> Decision: `Integrate`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-03327:end -->
<!-- books-review:SF-2026-ARXIV-2605-03353:start -->
<!-- existing:SF-2026-ARXIV-2605-03353:start -->已读取 `AGENT-PLATFORM` 当前 owner 与相邻章节；旧路径在固定 workload、低风险或规模较小时仍成立。<!-- existing:SF-2026-ARXIV-2605-03353:end -->
<!-- delta:SF-2026-ARXIV-2605-03353:start -->portable skills require a typed intermediate representation and target-specific lowering, while static checks remain separate from runtime effect authorization<!-- delta:SF-2026-ARXIV-2605-03353:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-03353:end -->
<!-- books-review:SF-2026-ARXIV-2605-03354:start -->
<!-- existing:SF-2026-ARXIV-2605-03354:start -->已读取 `AGENT-MEMORY` 当前 owner 与相邻章节；旧路径在固定 workload、低风险或规模较小时仍成立。<!-- existing:SF-2026-ARXIV-2605-03354:end -->
<!-- delta:SF-2026-ARXIV-2605-03354:start -->memory write/read failures can be localized through stage-specific internal circuits, but circuit signals remain diagnostics rather than durable memory truth<!-- delta:SF-2026-ARXIV-2605-03354:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-03354:end -->
<!-- books-review:SF-2026-ARXIV-2605-03375:start -->
<!-- existing:SF-2026-ARXIV-2605-03375:start -->已读取 `INFER-KV-CACHE` 当前 owner 与相邻章节；旧路径在固定 workload、低风险或规模较小时仍成立。<!-- existing:SF-2026-ARXIV-2605-03375:end -->
<!-- delta:SF-2026-ARXIV-2605-03375:start -->SSD-backed KV restore must move both data and I/O submission ownership off the CPU critical path and schedule transfers against GPU slack<!-- delta:SF-2026-ARXIV-2605-03375:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-03375:end -->
<!-- books-review:SF-2026-ARXIV-2605-03378:start -->
<!-- existing:SF-2026-ARXIV-2605-03378:start -->已读取 `PLATFORM-SECURITY` 当前 owner 与相邻章节；旧路径在固定 workload、低风险或规模较小时仍成立。<!-- existing:SF-2026-ARXIV-2605-03378:end -->
<!-- delta:SF-2026-ARXIV-2605-03378:start -->an agent action should commit only when benign evidence provides a complete causal justification and task invariants hold<!-- delta:SF-2026-ARXIV-2605-03378:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-03378:end -->
<!-- books-review:SF-2026-ARXIV-2605-03379:start -->
<!-- existing:SF-2026-ARXIV-2605-03379:start -->已读取 `PLATFORM-EVALUATION-SYSTEM` 当前 owner 与相邻章节；旧路径在固定 workload、低风险或规模较小时仍成立。<!-- existing:SF-2026-ARXIV-2605-03379:end -->
<!-- delta:SF-2026-ARXIV-2605-03379:start -->test-time vote accuracy is governed by the latent per-example success distribution and same-example correlation, so one-call accuracy cannot specify a repeated-sampling evaluation contract<!-- delta:SF-2026-ARXIV-2605-03379:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-03379:end -->
<!-- books-review:SF-2026-ARXIV-2605-03408:start -->
<!-- existing:SF-2026-ARXIV-2605-03408:start -->已读取 `TRAIN-RLHF` 当前 owner 与相邻章节；旧路径在固定 workload、低风险或规模较小时仍成立。<!-- existing:SF-2026-ARXIV-2605-03408:end -->
<!-- delta:SF-2026-ARXIV-2605-03408:start -->an RL task interface jointly owns observation projection and reward rather than treating reward synthesis as an isolated prompt problem; generated interfaces still require environment-grounded validation<!-- delta:SF-2026-ARXIV-2605-03408:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-03408:end -->
<!-- books-review:SF-2026-ARXIV-2605-03425:start -->
<!-- existing:SF-2026-ARXIV-2605-03425:start -->已读取 `TRAIN-PRETRAINING` 当前 owner 与相邻章节；旧路径在固定 workload、低风险或规模较小时仍成立。<!-- existing:SF-2026-ARXIV-2605-03425:end -->
<!-- delta:SF-2026-ARXIV-2605-03425:start -->gradient filtering under differential privacy changes the noise statistics consumed by AdamW state, so optimizer bias correction must be derived from the filter rather than reused from unfiltered DP-SGD<!-- delta:SF-2026-ARXIV-2605-03425:end --> Decision: `Integrate`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-03425:end -->
<!-- books-review:SF-2026-ARXIV-2605-03482:start -->
<!-- existing:SF-2026-ARXIV-2605-03482:start -->已读取 `PLATFORM-SECURITY` 当前 owner 与相邻章节；旧路径在固定 workload、低风险或规模较小时仍成立。<!-- existing:SF-2026-ARXIV-2605-03482:end -->
<!-- delta:SF-2026-ARXIV-2605-03482:start -->persistent memory poisoning needs calibrated anomaly admission tied to retrieval geometry, with synonym-invariant attacks kept as an explicit non-covered boundary<!-- delta:SF-2026-ARXIV-2605-03482:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-03482:end -->
<!-- books-review:SF-2026-ARXIV-2605-03505:start -->
<!-- existing:SF-2026-ARXIV-2605-03505:start -->已读取 `PLATFORM-MONITORING` 当前 owner 与相邻章节；旧路径在固定 workload、低风险或规模较小时仍成立。<!-- existing:SF-2026-ARXIV-2605-03505:end -->
<!-- delta:SF-2026-ARXIV-2605-03505:start -->microservice diagnosis can branch over competing causal hypotheses and use reflection to allocate investigation, but an agent search trace does not replace telemetry identity or causal observability<!-- delta:SF-2026-ARXIV-2605-03505:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-03505:end -->
<!-- books-review:SF-2026-ARXIV-2605-03534:start -->
<!-- existing:SF-2026-ARXIV-2605-03534:start -->已读取 `AGENT-RAG` 当前 owner 与相邻章节；旧路径在固定 workload、低风险或规模较小时仍成立。<!-- existing:SF-2026-ARXIV-2605-03534:end -->
<!-- delta:SF-2026-ARXIV-2605-03534:start -->evidence sufficiency is a set-level claim contract over coverage, relation, conflict and uncertainty, not independent passage relevance<!-- delta:SF-2026-ARXIV-2605-03534:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-03534:end -->
<!-- books-review:SF-2026-ARXIV-2605-03561:start -->
<!-- existing:SF-2026-ARXIV-2605-03561:start -->已读取 `PLATFORM-MONITORING` 当前 owner 与相邻章节；旧路径在固定 workload、低风险或规模较小时仍成立。<!-- existing:SF-2026-ARXIV-2605-03561:end -->
<!-- delta:SF-2026-ARXIV-2605-03561:start -->exascale diagnostic analysis must separate telemetry ingestion, GPU-parallel analysis and presentation so monitoring overhead scales below the workload being observed<!-- delta:SF-2026-ARXIV-2605-03561:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-03561:end -->
<!-- books-review:SF-2026-ARXIV-2605-03562:start -->
<!-- existing:SF-2026-ARXIV-2605-03562:start -->已读取 `INFER-KV-CACHE` 当前 owner 与相邻章节；旧路径在固定 workload、低风险或规模较小时仍成立。<!-- existing:SF-2026-ARXIV-2605-03562:end -->
<!-- delta:SF-2026-ARXIV-2605-03562:start -->KV quantization error must be measured in attention-visible score/readout coordinates rather than raw storage MSE, with distinct K and V operators<!-- delta:SF-2026-ARXIV-2605-03562:end --> Decision: `Integrate`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-03562:end -->
<!-- books-review:SF-2026-ARXIV-2605-03566:start -->
<!-- existing:SF-2026-ARXIV-2605-03566:start -->已读取 `INFER-TENSORRT-LLM` 当前 owner 与相邻章节；旧路径在固定 workload、低风险或规模较小时仍成立。<!-- existing:SF-2026-ARXIV-2605-03566:end -->
<!-- delta:SF-2026-ARXIV-2605-03566:start -->compiler lowering to an AI Engine needs tensor-level intermediate structure before hardware-specific mapping; source compatibility is obtained by changing the compiler owner, not by hiding data-movement constraints<!-- delta:SF-2026-ARXIV-2605-03566:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-03566:end -->
<!-- books-review:SF-2026-ARXIV-2605-03596:start -->
<!-- existing:SF-2026-ARXIV-2605-03596:start -->已读取 `PLATFORM-EVALUATION-SYSTEM` 当前 owner 与相邻章节；旧路径在固定 workload、低风险或规模较小时仍成立。<!-- existing:SF-2026-ARXIV-2605-03596:end -->
<!-- delta:SF-2026-ARXIV-2605-03596:start -->workspace-agent evaluation must preserve cross-file dependency state and score both reads and mutations against a real workspace graph rather than treating files as independent prompt attachments<!-- delta:SF-2026-ARXIV-2605-03596:end --> Decision: `Integrate`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-03596:end -->
<!-- books-review:SF-2026-ARXIV-2605-03644:start -->
<!-- existing:SF-2026-ARXIV-2605-03644:start -->已读取 `INFER-KV-CACHE` 当前 owner 与相邻章节；旧路径在固定 workload、低风险或规模较小时仍成立。<!-- existing:SF-2026-ARXIV-2605-03644:end -->
<!-- delta:SF-2026-ARXIV-2605-03644:start -->adaptive many-shot inference couples example selection with reusable prefix KV state, making context admission a joint quality-memory-latency decision rather than a fixed shot count<!-- delta:SF-2026-ARXIV-2605-03644:end --> Decision: `Integrate`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-03644:end -->
<!-- books-review:SF-2026-ARXIV-2605-03667:start -->
<!-- existing:SF-2026-ARXIV-2605-03667:start -->已读取 `TRAIN-PRETRAINING` 当前 owner 与相邻章节；旧路径在固定 workload、低风险或规模较小时仍成立。<!-- existing:SF-2026-ARXIV-2605-03667:end -->
<!-- delta:SF-2026-ARXIV-2605-03667:start -->low-rank pretraining becomes hardware-useful only when the factorization is co-designed with supported structured activation sparsity; mathematical compression alone does not guarantee realized training throughput<!-- delta:SF-2026-ARXIV-2605-03667:end --> Decision: `Integrate`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-03667:end -->
<!-- books-review:SF-2026-ARXIV-2605-03675:start -->
<!-- existing:SF-2026-ARXIV-2605-03675:start -->已读取 `AGENT-MEMORY` 当前 owner 与相邻章节；旧路径在固定 workload、低风险或规模较小时仍成立。<!-- existing:SF-2026-ARXIV-2605-03675:end -->
<!-- delta:SF-2026-ARXIV-2605-03675:start -->long-running agent memory needs tiered episodic, semantic and working state plus measured retrieval-bottleneck ownership instead of a flat file<!-- delta:SF-2026-ARXIV-2605-03675:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-03675:end -->
<!-- books-review:SF-2026-ARXIV-2605-03677:start -->
<!-- existing:SF-2026-ARXIV-2605-03677:start -->已读取 `TRAIN-RLHF` 当前 owner 与相邻章节；旧路径在固定 workload、低风险或规模较小时仍成立。<!-- existing:SF-2026-ARXIV-2605-03677:end -->
<!-- delta:SF-2026-ARXIV-2605-03677:start -->on-policy distillation needs both exploration of informative student states and reliability-aware teacher supervision, so teacher outputs are conditional feedback rather than unconditional labels<!-- delta:SF-2026-ARXIV-2605-03677:end --> Decision: `Integrate`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-03677:end -->
<!-- books-review:SF-2026-ARXIV-2605-03762:start -->
<!-- existing:SF-2026-ARXIV-2605-03762:start -->已读取 `PLATFORM-EVALUATION-SYSTEM` 当前 owner 与相邻章节；旧路径在固定 workload、低风险或规模较小时仍成立。<!-- existing:SF-2026-ARXIV-2605-03762:end -->
<!-- delta:SF-2026-ARXIV-2605-03762:start -->forecast evaluation needs verifiable knowledge cutoffs, temporal masking and artifact provenance so future leakage cannot masquerade as predictive capability<!-- delta:SF-2026-ARXIV-2605-03762:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-03762:end -->
<!-- books-review:SF-2026-ARXIV-2605-03838:start -->
<!-- existing:SF-2026-ARXIV-2605-03838:start -->已读取 `PLATFORM-EVALUATION-SYSTEM` 当前 owner 与相邻章节；旧路径在固定 workload、低风险或规模较小时仍成立。<!-- existing:SF-2026-ARXIV-2605-03838:end -->
<!-- delta:SF-2026-ARXIV-2605-03838:start -->operationally critical agent evidence needs traceable measurement units, uncertainty budgets and release criteria rather than a single trust score<!-- delta:SF-2026-ARXIV-2605-03838:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-03838:end -->
<!-- books-review:SF-2026-ARXIV-2605-03858:start -->
<!-- existing:SF-2026-ARXIV-2605-03858:start -->已读取 `PLATFORM-EVALUATION-SYSTEM` 当前 owner 与相邻章节；旧路径在固定 workload、低风险或规模较小时仍成立。<!-- existing:SF-2026-ARXIV-2605-03858:end -->
<!-- delta:SF-2026-ARXIV-2605-03858:start -->LLM judges need constraint-level correctness and completeness labels because aggregate verdicts hide which obligation failed<!-- delta:SF-2026-ARXIV-2605-03858:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-03858:end -->
<!-- books-review:SF-2026-ARXIV-2605-03862:start -->
<!-- existing:SF-2026-ARXIV-2605-03862:start -->已读取 `TRAIN-RLHF` 当前 owner 与相邻章节；旧路径在固定 workload、低风险或规模较小时仍成立。<!-- existing:SF-2026-ARXIV-2605-03862:end -->
<!-- delta:SF-2026-ARXIV-2605-03862:start -->planner training should bind reward to executor-observed intermediate state and feasibility, not only a final textual answer<!-- delta:SF-2026-ARXIV-2605-03862:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-03862:end -->
<!-- books-review:SF-2026-ARXIV-2605-03884:start -->
<!-- existing:SF-2026-ARXIV-2605-03884:start -->已读取 `AGENT-MULTI-AGENT` 当前 owner 与相邻章节；旧路径在固定 workload、低风险或规模较小时仍成立。<!-- existing:SF-2026-ARXIV-2605-03884:end -->
<!-- delta:SF-2026-ARXIV-2605-03884:start -->cross-agent latent handoff needs a versioned CacheCard carrying quantized KV state, bit allocation and receiver injection metadata, while prefix alignment and fused execution remain unresolved<!-- delta:SF-2026-ARXIV-2605-03884:end --> Decision: `Integrate`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-03884:end -->
<!-- books-review:SF-2026-ARXIV-2605-03952:start -->
<!-- existing:SF-2026-ARXIV-2605-03952:start -->已读取 `PLATFORM-SECURITY` 当前 owner 与相邻章节；旧路径在固定 workload、低风险或规模较小时仍成立。<!-- existing:SF-2026-ARXIV-2605-03952:end -->
<!-- delta:SF-2026-ARXIV-2605-03952:start -->coding-agent safety must evaluate cumulative diffs and end-state exploitability across innocuous ticket sequences, not approve each prompt independently<!-- delta:SF-2026-ARXIV-2605-03952:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-03952:end -->
<!-- books-review:SF-2026-ARXIV-2605-03971:start -->
<!-- existing:SF-2026-ARXIV-2605-03971:start -->已读取 `PLATFORM-EVALUATION-SYSTEM` 当前 owner 与相邻章节；旧路径在固定 workload、低风险或规模较小时仍成立。<!-- existing:SF-2026-ARXIV-2605-03971:end -->
<!-- delta:SF-2026-ARXIV-2605-03971:start -->hallucination detection can combine response-intrinsic uncertainty with verbal self-judgment through explicit logical constraints, but detector confidence remains an evaluated signal rather than truth<!-- delta:SF-2026-ARXIV-2605-03971:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-03971:end -->
<!-- books-review:SF-2026-ARXIV-2605-03986:start -->
<!-- existing:SF-2026-ARXIV-2605-03986:start -->已读取 `AGENT-WORKFLOW` 当前 owner 与相邻章节；旧路径在固定 workload、低风险或规模较小时仍成立。<!-- existing:SF-2026-ARXIV-2605-03986:end -->
<!-- delta:SF-2026-ARXIV-2605-03986:start -->intent-to-execution automation separates plan synthesis, agent capability recommendation and executable graph construction; each stage requires typed validation before workflow commit<!-- delta:SF-2026-ARXIV-2605-03986:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-03986:end -->
<!-- books-review:SF-2026-ARXIV-2605-04018:start -->
<!-- existing:SF-2026-ARXIV-2605-04018:start -->已读取 `AGENT-RAG` 当前 owner 与相邻章节；旧路径在固定 workload、低风险或规模较小时仍成立。<!-- existing:SF-2026-ARXIV-2605-04018:end -->
<!-- delta:SF-2026-ARXIV-2605-04018:start -->reasoning retrieval should optimize complementary evidence portfolios and measure agent-loop completeness, iterations and answer quality under matched budgets<!-- delta:SF-2026-ARXIV-2605-04018:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-04018:end -->
<!-- books-review:SF-2026-ARXIV-2605-04019:start -->
<!-- existing:SF-2026-ARXIV-2605-04019:start -->已读取 `PLATFORM-SECURITY` 当前 owner 与相邻章节；旧路径在固定 workload、低风险或规模较小时仍成立。<!-- existing:SF-2026-ARXIV-2605-04019:end -->
<!-- delta:SF-2026-ARXIV-2605-04019:start -->red-team workflow generation can reduce operator setup cost, but attack libraries and a single target case do not establish adaptive security coverage<!-- delta:SF-2026-ARXIV-2605-04019:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-04019:end -->
<!-- books-review:SF-2026-ARXIV-2605-04036:start -->
<!-- existing:SF-2026-ARXIV-2605-04036:start -->已读取 `TRAIN-SFT` 当前 owner 与相邻章节；旧路径在固定 workload、低风险或规模较小时仍成立。<!-- existing:SF-2026-ARXIV-2605-04036:end -->
<!-- delta:SF-2026-ARXIV-2605-04036:start -->search-agent SFT quality depends on selecting informative, difficult trajectories rather than merely scaling trajectory count; the result is workload-bound and does not displace RL branches<!-- delta:SF-2026-ARXIV-2605-04036:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-04036:end -->
<!-- books-review:SF-2026-ARXIV-2605-04039:start -->
<!-- existing:SF-2026-ARXIV-2605-04039:start -->已读取 `PLATFORM-EVALUATION-SYSTEM` 当前 owner 与相邻章节；旧路径在固定 workload、低风险或规模较小时仍成立。<!-- existing:SF-2026-ARXIV-2605-04039:end -->
<!-- delta:SF-2026-ARXIV-2605-04039:start -->clinical accuracy and safety have different scaling curves, requiring risk-weighted, evidence-aware evaluation and abstention criteria instead of inferring deployment safety from mean accuracy<!-- delta:SF-2026-ARXIV-2605-04039:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-04039:end -->
<!-- books-review:SF-2026-ARXIV-2605-04116:start -->
<!-- existing:SF-2026-ARXIV-2605-04116:start -->已读取 `PLATFORM-SECURITY` 当前 owner 与相邻章节；旧路径在固定 workload、低风险或规模较小时仍成立。<!-- existing:SF-2026-ARXIV-2605-04116:end -->
<!-- delta:SF-2026-ARXIV-2605-04116:start -->retrieval-selected in-context examples create a remotely observable membership channel, so example-store privacy belongs to the serving threat model<!-- delta:SF-2026-ARXIV-2605-04116:end --> Decision: `Integrate`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-04116:end -->
<!-- books-review:SF-2026-ARXIV-2605-04135:start -->
<!-- existing:SF-2026-ARXIV-2605-04135:start -->已读取 `PLATFORM-EVALUATION-SYSTEM` 当前 owner 与相邻章节；旧路径在固定 workload、低风险或规模较小时仍成立。<!-- existing:SF-2026-ARXIV-2605-04135:end -->
<!-- delta:SF-2026-ARXIV-2605-04135:start -->capability claims must bind model release, elicitation, tools and evaluation date because frontier lag can turn a valid historical measurement into a misleading current-system conclusion<!-- delta:SF-2026-ARXIV-2605-04135:end --> Decision: `Integrate`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-04135:end -->
<!-- books-review:SF-2026-ARXIV-2605-04172:start -->
<!-- existing:SF-2026-ARXIV-2605-04172:start -->已读取 `INFER-TENSORRT-LLM` 当前 owner 与相邻章节；旧路径在固定 workload、低风险或规模较小时仍成立。<!-- existing:SF-2026-ARXIV-2605-04172:end -->
<!-- delta:SF-2026-ARXIV-2605-04172:start -->programmable memory callbacks require an ISA-level consistency contract across misses, evictions and writebacks; performance programmability without formal ordering moves hidden state into software<!-- delta:SF-2026-ARXIV-2605-04172:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-04172:end -->
<!-- books-review:SF-2026-ARXIV-2605-04178:start -->
<!-- existing:SF-2026-ARXIV-2605-04178:start -->已读取 `INFER-TENSORRT-LLM` 当前 owner 与相邻章节；旧路径在固定 workload、低风险或规模较小时仍成立。<!-- existing:SF-2026-ARXIV-2605-04178:end -->
<!-- delta:SF-2026-ARXIV-2605-04178:start -->GPU execution plans require architecture-specific microbenchmarks for memory hierarchy, matrix units, occupancy and precision; peak-FLOP rooflines are insufficient<!-- delta:SF-2026-ARXIV-2605-04178:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-04178:end -->
<!-- books-review:SF-2026-ARXIV-2605-04209:start -->
<!-- existing:SF-2026-ARXIV-2605-04209:start -->已读取 `PLATFORM-SECURITY` 当前 owner 与相邻章节；旧路径在固定 workload、低风险或规模较小时仍成立。<!-- existing:SF-2026-ARXIV-2605-04209:end -->
<!-- delta:SF-2026-ARXIV-2605-04209:start -->model artifacts can carry statistically hidden parameter backdoors whose detectability is bounded by the attack distribution, extending supply-chain verification beyond file hashes and conventional weight scanning<!-- delta:SF-2026-ARXIV-2605-04209:end --> Decision: `Integrate`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-04209:end -->
<!-- books-review:SF-2026-ARXIV-2605-04213:start -->
<!-- existing:SF-2026-ARXIV-2605-04213:start -->已读取 `PLATFORM-MONITORING` 当前 owner 与相邻章节；旧路径在固定 workload、低风险或规模较小时仍成立。<!-- existing:SF-2026-ARXIV-2605-04213:end -->
<!-- delta:SF-2026-ARXIV-2605-04213:start -->silent GPU corruption needs empirically grounded fault models tied to operation type and propagation pattern; generic random bit flips can invalidate resilience conclusions for large-scale training<!-- delta:SF-2026-ARXIV-2605-04213:end --> Decision: `Integrate`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-04213:end -->
<!-- books-review:SF-2026-ARXIV-2605-04215:start -->
<!-- existing:SF-2026-ARXIV-2605-04215:start -->已读取 `MULTIMODAL-GENERATIVE-PARADIGMS` 当前 owner 与相邻章节；旧路径在固定 workload、低风险或规模较小时仍成立。<!-- existing:SF-2026-ARXIV-2605-04215:end -->
<!-- delta:SF-2026-ARXIV-2605-04215:start -->fixed-length diffusion generation turns response-length prediction into an admission-time compute budget with explicit underprediction retry risk<!-- delta:SF-2026-ARXIV-2605-04215:end --> Decision: `Integrate`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-04215:end -->
<!-- books-review:SF-2026-ARXIV-2605-04236:start -->
<!-- existing:SF-2026-ARXIV-2605-04236:start -->已读取 `PLATFORM-EVALUATION-SYSTEM` 当前 owner 与相邻章节；旧路径在固定 workload、低风险或规模较小时仍成立。<!-- existing:SF-2026-ARXIV-2605-04236:end -->
<!-- delta:SF-2026-ARXIV-2605-04236:start -->ensemble deliberation needs an evidence-accumulation stopping and fallback contract because more samples can cross from useful consensus into degraded decisions<!-- delta:SF-2026-ARXIV-2605-04236:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-04236:end -->
<!-- books-review:SF-2026-ARXIV-2605-04256:start -->
<!-- existing:SF-2026-ARXIV-2605-04256:start -->已读取 `AGENT-MCP` 当前 owner 与相邻章节；旧路径在固定 workload、低风险或规模较小时仍成立。<!-- existing:SF-2026-ARXIV-2605-04256:end -->
<!-- delta:SF-2026-ARXIV-2605-04256:start -->heterogeneous physical neural substrates require a typed control plane for capability discovery, timing, observation, actuation and safety rather than presenting every device as an interchangeable tool<!-- delta:SF-2026-ARXIV-2605-04256:end --> Decision: `Integrate`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-04256:end -->
<!-- books-review:SF-2026-ARXIV-2605-04263:start -->
<!-- existing:SF-2026-ARXIV-2605-04263:start -->已读取 `INFER-SPECULATIVE-DECODING` 当前 owner 与相邻章节；旧路径在固定 workload、低风险或规模较小时仍成立。<!-- existing:SF-2026-ARXIV-2605-04263:end -->
<!-- delta:SF-2026-ARXIV-2605-04263:start -->semantic speculative generation can verify multiple draft prefixes in one target pass, but must preserve a maximal valid commit boundary distinct from token-exact acceptance<!-- delta:SF-2026-ARXIV-2605-04263:end --> Decision: `Integrate`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-04263:end -->
<!-- books-review:SF-2026-ARXIV-2605-04264:start -->
<!-- existing:SF-2026-ARXIV-2605-04264:start -->已读取 `AGENT-MEMORY` 当前 owner 与相邻章节；旧路径在固定 workload、低风险或规模较小时仍成立。<!-- existing:SF-2026-ARXIV-2605-04264:end -->
<!-- delta:SF-2026-ARXIV-2605-04264:start -->shared memory admission is a governed selection regime over provenance, correction and role preservation, not merely a retrieval score<!-- delta:SF-2026-ARXIV-2605-04264:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-04264:end -->
<!-- books-review:SF-2026-ARXIV-2605-04266:start -->
<!-- existing:SF-2026-ARXIV-2605-04266:start -->已读取 `TRAIN-RLHF` 当前 owner 与相邻章节；旧路径在固定 workload、低风险或规模较小时仍成立。<!-- existing:SF-2026-ARXIV-2605-04266:end -->
<!-- delta:SF-2026-ARXIV-2605-04266:start -->iterative RLHF creates a policy-to-future-reward-model feedback loop; omitting parameter steering allows self-reinforcing reward-model exploitation<!-- delta:SF-2026-ARXIV-2605-04266:end --> Decision: `Integrate`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-04266:end -->
<!-- books-review:SF-2026-ARXIV-2605-04269:start -->
<!-- existing:SF-2026-ARXIV-2605-04269:start -->已读取 `TRAIN-PRETRAINING` 当前 owner 与相邻章节；旧路径在固定 workload、低风险或规模较小时仍成立。<!-- existing:SF-2026-ARXIV-2605-04269:end -->
<!-- delta:SF-2026-ARXIV-2605-04269:start -->under nonstationary objectives Adam's adaptive state trades faster tracking for longer optimizer memory, whereas SGD forgets differently; optimizer choice therefore depends on drift, projection and stationarity assumptions<!-- delta:SF-2026-ARXIV-2605-04269:end --> Decision: `Integrate`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-04269:end -->
<!-- books-review:SF-2026-ARXIV-2605-04295:start -->
<!-- existing:SF-2026-ARXIV-2605-04295:start -->已读取 `PLATFORM-EVALUATION-SYSTEM` 当前 owner 与相邻章节；旧路径在固定 workload、低风险或规模较小时仍成立。<!-- existing:SF-2026-ARXIV-2605-04295:end -->
<!-- delta:SF-2026-ARXIV-2605-04295:start -->uncertainty can be estimated over semantic response clusters and calibrated with conformal acceptance, but coverage guarantees remain conditional on calibration exchangeability and the chosen semantic equivalence model<!-- delta:SF-2026-ARXIV-2605-04295:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-04295:end -->
<!-- books-review:SF-2026-ARXIV-2605-04312:start -->
<!-- existing:SF-2026-ARXIV-2605-04312:start -->已读取 `PLATFORM-EVALUATION-SYSTEM` 当前 owner 与相邻章节；旧路径在固定 workload、低风险或规模较小时仍成立。<!-- existing:SF-2026-ARXIV-2605-04312:end -->
<!-- delta:SF-2026-ARXIV-2605-04312:start -->a persistent multi-agent game can reduce benchmark saturation and contamination by making other agents part of the changing workload, while introducing opponent-population and reproducibility dependence<!-- delta:SF-2026-ARXIV-2605-04312:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-04312:end -->
<!-- books-review:SF-2026-ARXIV-2605-04333:start -->
<!-- existing:SF-2026-ARXIV-2605-04333:start -->已读取 `TRAIN-DISTRIBUTED-TRAINING` 当前 owner 与相邻章节；旧路径在固定 workload、低风险或规模较小时仍成立。<!-- existing:SF-2026-ARXIV-2605-04333:end -->
<!-- delta:SF-2026-ARXIV-2605-04333:start -->large synchronous training networks need multipath transport, redundant Clos planes and explicit failure handling because tail latency and flow collisions dominate collective completion at scale<!-- delta:SF-2026-ARXIV-2605-04333:end --> Decision: `Integrate`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-04333:end -->
<!-- books-review:SF-2026-ARXIV-2605-04341:start -->
<!-- existing:SF-2026-ARXIV-2605-04341:start -->已读取 `TRAIN-LORA` 当前 owner 与相邻章节；旧路径在固定 workload、低风险或规模较小时仍成立。<!-- existing:SF-2026-ARXIV-2605-04341:end -->
<!-- delta:SF-2026-ARXIV-2605-04341:start -->parameter-efficient adaptation reduces training cost but not dense inference cost; budgeted distillation must allocate structural rank or compute under a deployment budget to produce an actually cheaper student<!-- delta:SF-2026-ARXIV-2605-04341:end --> Decision: `Integrate`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-04341:end -->
<!-- books-review:SF-2026-ARXIV-2605-04357:start -->
<!-- existing:SF-2026-ARXIV-2605-04357:start -->已读取 `INFER-SCHEDULING` 当前 owner 与相邻章节；旧路径在固定 workload、低风险或规模较小时仍成立。<!-- existing:SF-2026-ARXIV-2605-04357:end -->
<!-- delta:SF-2026-ARXIV-2605-04357:start -->heterogeneous multi-model serving must co-optimize model placement and resource allocation under per-model SLOs, separating offline serving templates from online allocation<!-- delta:SF-2026-ARXIV-2605-04357:end --> Decision: `Integrate`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-04357:end -->
<!-- books-review:SF-2026-ARXIV-2605-04361:start -->
<!-- existing:SF-2026-ARXIV-2605-04361:start -->已读取 `AGENT-CONTEXT` 当前 owner 与相邻章节；旧路径在固定 workload、低风险或规模较小时仍成立。<!-- existing:SF-2026-ARXIV-2605-04361:end -->
<!-- delta:SF-2026-ARXIV-2605-04361:start -->context artifacts have task-dependent crossover effects, so context admission must estimate marginal decision value and interference rather than assume that more relevant context monotonically helps<!-- delta:SF-2026-ARXIV-2605-04361:end --> Decision: `Integrate`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-04361:end -->
<!-- books-review:SF-2026-ARXIV-2605-04373:start -->
<!-- existing:SF-2026-ARXIV-2605-04373:start -->已读取 `PLATFORM-SECURITY` 当前 owner 与相邻章节；旧路径在固定 workload、低风险或规模较小时仍成立。<!-- existing:SF-2026-ARXIV-2605-04373:end -->
<!-- delta:SF-2026-ARXIV-2605-04373:start -->learned controllers need adversarial worst-case discovery compiled into a lightweight runtime protection rule with a nominal-path fallback<!-- delta:SF-2026-ARXIV-2605-04373:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-04373:end -->
<!-- books-review:SF-2026-ARXIV-2605-04375:start -->
<!-- existing:SF-2026-ARXIV-2605-04375:start -->已读取 `AGENT-WORKFLOW` 当前 owner 与相邻章节；旧路径在固定 workload、低风险或规模较小时仍成立。<!-- existing:SF-2026-ARXIV-2605-04375:end -->
<!-- delta:SF-2026-ARXIV-2605-04375:start -->physical experiments need declarative experiment-as-code that binds instrument capabilities, execution state, provenance and human safety approval, extending durable workflow semantics beyond digital tools<!-- delta:SF-2026-ARXIV-2605-04375:end --> Decision: `Integrate`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-04375:end -->
<!-- books-review:SF-2026-ARXIV-2605-05248:start -->
<!-- existing:SF-2026-ARXIV-2605-05248:start -->已读取 `AGENT-WORKFLOW` 当前 owner 与相邻章节；旧路径在固定 workload、低风险或规模较小时仍成立。<!-- existing:SF-2026-ARXIV-2605-05248:end -->
<!-- delta:SF-2026-ARXIV-2605-05248:start -->turning generated symbolic structure into executable code is an authority-amplifying materialization effect that requires capability, policy and resource admission<!-- delta:SF-2026-ARXIV-2605-05248:end --> Decision: `Integrate`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-05248:end -->
<!-- books-review:SF-2026-ARXIV-2605-05253:start -->
<!-- existing:SF-2026-ARXIV-2605-05253:start -->已读取 `AGENT-RAG` 当前 owner 与相邻章节；旧路径在固定 workload、低风险或规模较小时仍成立。<!-- existing:SF-2026-ARXIV-2605-05253:end -->
<!-- delta:SF-2026-ARXIV-2605-05253:start -->enterprise RAG evaluation must preserve private-document heterogeneity, access boundaries and multi-document evidence needs, but a benchmark dataset does not itself define a new retrieval ownership mechanism<!-- delta:SF-2026-ARXIV-2605-05253:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-05253:end -->
<!-- books-review:SF-2026-ARXIV-2605-08190:start -->
<!-- existing:SF-2026-ARXIV-2605-08190:start -->已读取 `MULTIMODAL-EMBODIED-VLA` 当前 owner 与相邻章节；旧路径在固定 workload、低风险或规模较小时仍成立。<!-- existing:SF-2026-ARXIV-2605-08190:end -->
<!-- delta:SF-2026-ARXIV-2605-08190:start -->runtime assurance may consume ML outputs only under formally derived cooperative monitor conditions and a verified safe fallback<!-- delta:SF-2026-ARXIV-2605-08190:end --> Decision: `Integrate`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-08190:end -->
<!-- books-review:SF-2026-ARXIV-2605-08192:start -->
<!-- existing:SF-2026-ARXIV-2605-08192:start -->已读取 `PLATFORM-EVALUATION-SYSTEM` 当前 owner 与相邻章节；旧路径在固定 workload、低风险或规模较小时仍成立。<!-- existing:SF-2026-ARXIV-2605-08192:end -->
<!-- delta:SF-2026-ARXIV-2605-08192:start -->frontier-safety release claims need reproducible artifacts, configuration disclosure and independent rerun conditions; authority or venue cannot substitute for an inspectable evaluation contract<!-- delta:SF-2026-ARXIV-2605-08192:end --> Decision: `Integrate`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-08192:end -->
<!-- books-review:SF-2026-ARXIV-2605-08195:start -->
<!-- existing:SF-2026-ARXIV-2605-08195:start -->已读取 `INFER-TENSORRT-LLM` 当前 owner 与相邻章节；旧路径在固定 workload、低风险或规模较小时仍成立。<!-- existing:SF-2026-ARXIV-2605-08195:end -->
<!-- delta:SF-2026-ARXIV-2605-08195:start -->on-device execution needs a portable exported program with delegated backend lowering while preserving framework semantics and explicit fallback<!-- delta:SF-2026-ARXIV-2605-08195:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-08195:end -->
<!-- books-review:SF-2026-ARXIV-2605-10959:start -->
<!-- existing:SF-2026-ARXIV-2605-10959:start -->已读取 `INFER-TENSORRT-LLM` 当前 owner 与相邻章节；旧路径在固定 workload、低风险或规模较小时仍成立。<!-- existing:SF-2026-ARXIV-2605-10959:end -->
<!-- delta:SF-2026-ARXIV-2605-10959:start -->quantization decisions need workload-specific accuracy, compression and realized latency measurements, but collapsing them into one scalar intelligence index hides Pareto preferences and cannot be a universal execution objective<!-- delta:SF-2026-ARXIV-2605-10959:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-10959:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260506-COVERAGE | fresh-context:root | coverage | coverage:SRC-ARXIV:20260506 | — | 513/513 replay 已闭合；withdrawal reconciliation 将分母 64→63、closure 449→450，withdrawn identity 保留 raw 审计轨迹但不进入候选 | passed |
| SA-20260506-EVIDENCE | fresh-context:root | evidence | review:SF-2026-ARXIV-2605-03275;review:SF-2026-ARXIV-2605-03309;review:SF-2026-ARXIV-2605-03310;review:SF-2026-ARXIV-2605-03312;review:SF-2026-ARXIV-2605-03314;review:SF-2026-ARXIV-2605-03327;review:SF-2026-ARXIV-2605-03353;review:SF-2026-ARXIV-2605-03354;review:SF-2026-ARXIV-2605-03375;review:SF-2026-ARXIV-2605-03378;review:SF-2026-ARXIV-2605-03379;review:SF-2026-ARXIV-2605-03408;review:SF-2026-ARXIV-2605-03425;review:SF-2026-ARXIV-2605-03482;review:SF-2026-ARXIV-2605-03505;review:SF-2026-ARXIV-2605-03534;review:SF-2026-ARXIV-2605-03561;review:SF-2026-ARXIV-2605-03562;review:SF-2026-ARXIV-2605-03566;review:SF-2026-ARXIV-2605-03596;review:SF-2026-ARXIV-2605-03644;review:SF-2026-ARXIV-2605-03667;review:SF-2026-ARXIV-2605-03675;review:SF-2026-ARXIV-2605-03677;review:SF-2026-ARXIV-2605-03762;review:SF-2026-ARXIV-2605-03838;review:SF-2026-ARXIV-2605-03858;review:SF-2026-ARXIV-2605-03862;review:SF-2026-ARXIV-2605-03884;review:SF-2026-ARXIV-2605-03952;review:SF-2026-ARXIV-2605-03971;review:SF-2026-ARXIV-2605-03986;review:SF-2026-ARXIV-2605-04018;review:SF-2026-ARXIV-2605-04019;review:SF-2026-ARXIV-2605-04036;review:SF-2026-ARXIV-2605-04039;review:SF-2026-ARXIV-2605-04116;review:SF-2026-ARXIV-2605-04135;review:SF-2026-ARXIV-2605-04172;review:SF-2026-ARXIV-2605-04178;review:SF-2026-ARXIV-2605-04209;review:SF-2026-ARXIV-2605-04213;review:SF-2026-ARXIV-2605-04215;review:SF-2026-ARXIV-2605-04236;review:SF-2026-ARXIV-2605-04256;review:SF-2026-ARXIV-2605-04263;review:SF-2026-ARXIV-2605-04264;review:SF-2026-ARXIV-2605-04266;review:SF-2026-ARXIV-2605-04269;review:SF-2026-ARXIV-2605-04295;review:SF-2026-ARXIV-2605-04312;review:SF-2026-ARXIV-2605-04333;review:SF-2026-ARXIV-2605-04341;review:SF-2026-ARXIV-2605-04357;review:SF-2026-ARXIV-2605-04361;review:SF-2026-ARXIV-2605-04373;review:SF-2026-ARXIV-2605-04375;review:SF-2026-ARXIV-2605-05248;review:SF-2026-ARXIV-2605-05253;review:SF-2026-ARXIV-2605-08190;review:SF-2026-ARXIV-2605-08192;review:SF-2026-ARXIV-2605-08195;review:SF-2026-ARXIV-2605-10959;claim:SF-2026-ARXIV-2605-03275;claim:SF-2026-ARXIV-2605-03309;claim:SF-2026-ARXIV-2605-03310;claim:SF-2026-ARXIV-2605-03312;claim:SF-2026-ARXIV-2605-03314;claim:SF-2026-ARXIV-2605-03327;claim:SF-2026-ARXIV-2605-03353;claim:SF-2026-ARXIV-2605-03354;claim:SF-2026-ARXIV-2605-03375;claim:SF-2026-ARXIV-2605-03378;claim:SF-2026-ARXIV-2605-03379;claim:SF-2026-ARXIV-2605-03408;claim:SF-2026-ARXIV-2605-03425;claim:SF-2026-ARXIV-2605-03482;claim:SF-2026-ARXIV-2605-03505;claim:SF-2026-ARXIV-2605-03534;claim:SF-2026-ARXIV-2605-03561;claim:SF-2026-ARXIV-2605-03562;claim:SF-2026-ARXIV-2605-03566;claim:SF-2026-ARXIV-2605-03596;claim:SF-2026-ARXIV-2605-03644;claim:SF-2026-ARXIV-2605-03667;claim:SF-2026-ARXIV-2605-03675;claim:SF-2026-ARXIV-2605-03677;claim:SF-2026-ARXIV-2605-03762;claim:SF-2026-ARXIV-2605-03838;claim:SF-2026-ARXIV-2605-03858;claim:SF-2026-ARXIV-2605-03862;claim:SF-2026-ARXIV-2605-03884;claim:SF-2026-ARXIV-2605-03952;claim:SF-2026-ARXIV-2605-03971;claim:SF-2026-ARXIV-2605-03986;claim:SF-2026-ARXIV-2605-04018;claim:SF-2026-ARXIV-2605-04019;claim:SF-2026-ARXIV-2605-04036;claim:SF-2026-ARXIV-2605-04039;claim:SF-2026-ARXIV-2605-04116;claim:SF-2026-ARXIV-2605-04135;claim:SF-2026-ARXIV-2605-04172;claim:SF-2026-ARXIV-2605-04178;claim:SF-2026-ARXIV-2605-04209;claim:SF-2026-ARXIV-2605-04213;claim:SF-2026-ARXIV-2605-04215;claim:SF-2026-ARXIV-2605-04236;claim:SF-2026-ARXIV-2605-04256;claim:SF-2026-ARXIV-2605-04263;claim:SF-2026-ARXIV-2605-04264;claim:SF-2026-ARXIV-2605-04266;claim:SF-2026-ARXIV-2605-04269;claim:SF-2026-ARXIV-2605-04295;claim:SF-2026-ARXIV-2605-04312;claim:SF-2026-ARXIV-2605-04333;claim:SF-2026-ARXIV-2605-04341;claim:SF-2026-ARXIV-2605-04357;claim:SF-2026-ARXIV-2605-04361;claim:SF-2026-ARXIV-2605-04373;claim:SF-2026-ARXIV-2605-04375;claim:SF-2026-ARXIV-2605-05248;claim:SF-2026-ARXIV-2605-05253;claim:SF-2026-ARXIV-2605-08190;claim:SF-2026-ARXIV-2605-08192;claim:SF-2026-ARXIV-2605-08195;claim:SF-2026-ARXIV-2605-10959 | — | 63/63 body-level Review complete；ordinary pending=0、blocker=0 | passed |
| SA-20260506-SELECTION | fresh-context:root | deep_analysis_selection | analysis:DA-GPU-OWNED-SSD-KV;analysis:DA-MODEL-VISIBLE-KV-ERROR;analysis:DA-HETERO-MULTI-LLM-CONTROL;analysis-decision:SF-2026-ARXIV-2605-03309;analysis-decision:SF-2026-ARXIV-2605-03310;analysis-decision:SF-2026-ARXIV-2605-03312;analysis-decision:SF-2026-ARXIV-2605-03314;analysis-decision:SF-2026-ARXIV-2605-03327;analysis-decision:SF-2026-ARXIV-2605-03353;analysis-decision:SF-2026-ARXIV-2605-03354;analysis-decision:SF-2026-ARXIV-2605-03378;analysis-decision:SF-2026-ARXIV-2605-03379;analysis-decision:SF-2026-ARXIV-2605-03408;analysis-decision:SF-2026-ARXIV-2605-03425;analysis-decision:SF-2026-ARXIV-2605-03482;analysis-decision:SF-2026-ARXIV-2605-03505;analysis-decision:SF-2026-ARXIV-2605-03534;analysis-decision:SF-2026-ARXIV-2605-03561;analysis-decision:SF-2026-ARXIV-2605-03566;analysis-decision:SF-2026-ARXIV-2605-03596;analysis-decision:SF-2026-ARXIV-2605-03644;analysis-decision:SF-2026-ARXIV-2605-03667;analysis-decision:SF-2026-ARXIV-2605-03675;analysis-decision:SF-2026-ARXIV-2605-03677;analysis-decision:SF-2026-ARXIV-2605-03762;analysis-decision:SF-2026-ARXIV-2605-03838;analysis-decision:SF-2026-ARXIV-2605-03858;analysis-decision:SF-2026-ARXIV-2605-03862;analysis-decision:SF-2026-ARXIV-2605-03884;analysis-decision:SF-2026-ARXIV-2605-03952;analysis-decision:SF-2026-ARXIV-2605-03971;analysis-decision:SF-2026-ARXIV-2605-03986;analysis-decision:SF-2026-ARXIV-2605-04018;analysis-decision:SF-2026-ARXIV-2605-04019;analysis-decision:SF-2026-ARXIV-2605-04036;analysis-decision:SF-2026-ARXIV-2605-04039;analysis-decision:SF-2026-ARXIV-2605-04116;analysis-decision:SF-2026-ARXIV-2605-04135;analysis-decision:SF-2026-ARXIV-2605-04172;analysis-decision:SF-2026-ARXIV-2605-04178;analysis-decision:SF-2026-ARXIV-2605-04209;analysis-decision:SF-2026-ARXIV-2605-04213;analysis-decision:SF-2026-ARXIV-2605-04215;analysis-decision:SF-2026-ARXIV-2605-04236;analysis-decision:SF-2026-ARXIV-2605-04256;analysis-decision:SF-2026-ARXIV-2605-04263;analysis-decision:SF-2026-ARXIV-2605-04264;analysis-decision:SF-2026-ARXIV-2605-04266;analysis-decision:SF-2026-ARXIV-2605-04269;analysis-decision:SF-2026-ARXIV-2605-04295;analysis-decision:SF-2026-ARXIV-2605-04312;analysis-decision:SF-2026-ARXIV-2605-04333;analysis-decision:SF-2026-ARXIV-2605-04341;analysis-decision:SF-2026-ARXIV-2605-04361;analysis-decision:SF-2026-ARXIV-2605-04373;analysis-decision:SF-2026-ARXIV-2605-04375;analysis-decision:SF-2026-ARXIV-2605-05248;analysis-decision:SF-2026-ARXIV-2605-05253;analysis-decision:SF-2026-ARXIV-2605-08190;analysis-decision:SF-2026-ARXIV-2605-08192;analysis-decision:SF-2026-ARXIV-2605-08195;analysis-decision:SF-2026-ARXIV-2605-10959 | — | 63-family eligibility pool 已逐项处置；三项 Deep Analysis 保持互补且其余候选均有明确未入选理由 | passed |
| SA-20260506-BOOKS | fresh-context:may2026_day02 | books | books-review:SF-2026-ARXIV-2605-03275;books-review:SF-2026-ARXIV-2605-03309;books-review:SF-2026-ARXIV-2605-03310;books-review:SF-2026-ARXIV-2605-03312;books-review:SF-2026-ARXIV-2605-03314;books-review:SF-2026-ARXIV-2605-03327;books-review:SF-2026-ARXIV-2605-03353;books-review:SF-2026-ARXIV-2605-03354;books-review:SF-2026-ARXIV-2605-03375;books-review:SF-2026-ARXIV-2605-03378;books-review:SF-2026-ARXIV-2605-03379;books-review:SF-2026-ARXIV-2605-03408;books-review:SF-2026-ARXIV-2605-03425;books-review:SF-2026-ARXIV-2605-03482;books-review:SF-2026-ARXIV-2605-03505;books-review:SF-2026-ARXIV-2605-03534;books-review:SF-2026-ARXIV-2605-03561;books-review:SF-2026-ARXIV-2605-03562;books-review:SF-2026-ARXIV-2605-03566;books-review:SF-2026-ARXIV-2605-03596;books-review:SF-2026-ARXIV-2605-03644;books-review:SF-2026-ARXIV-2605-03667;books-review:SF-2026-ARXIV-2605-03675;books-review:SF-2026-ARXIV-2605-03677;books-review:SF-2026-ARXIV-2605-03762;books-review:SF-2026-ARXIV-2605-03838;books-review:SF-2026-ARXIV-2605-03858;books-review:SF-2026-ARXIV-2605-03862;books-review:SF-2026-ARXIV-2605-03884;books-review:SF-2026-ARXIV-2605-03952;books-review:SF-2026-ARXIV-2605-03971;books-review:SF-2026-ARXIV-2605-03986;books-review:SF-2026-ARXIV-2605-04018;books-review:SF-2026-ARXIV-2605-04019;books-review:SF-2026-ARXIV-2605-04036;books-review:SF-2026-ARXIV-2605-04039;books-review:SF-2026-ARXIV-2605-04116;books-review:SF-2026-ARXIV-2605-04135;books-review:SF-2026-ARXIV-2605-04172;books-review:SF-2026-ARXIV-2605-04178;books-review:SF-2026-ARXIV-2605-04209;books-review:SF-2026-ARXIV-2605-04213;books-review:SF-2026-ARXIV-2605-04215;books-review:SF-2026-ARXIV-2605-04236;books-review:SF-2026-ARXIV-2605-04256;books-review:SF-2026-ARXIV-2605-04263;books-review:SF-2026-ARXIV-2605-04264;books-review:SF-2026-ARXIV-2605-04266;books-review:SF-2026-ARXIV-2605-04269;books-review:SF-2026-ARXIV-2605-04295;books-review:SF-2026-ARXIV-2605-04312;books-review:SF-2026-ARXIV-2605-04333;books-review:SF-2026-ARXIV-2605-04341;books-review:SF-2026-ARXIV-2605-04357;books-review:SF-2026-ARXIV-2605-04361;books-review:SF-2026-ARXIV-2605-04373;books-review:SF-2026-ARXIV-2605-04375;books-review:SF-2026-ARXIV-2605-05248;books-review:SF-2026-ARXIV-2605-05253;books-review:SF-2026-ARXIV-2605-08190;books-review:SF-2026-ARXIV-2605-08192;books-review:SF-2026-ARXIV-2605-08195;books-review:SF-2026-ARXIV-2605-10959 | — | 27/27 writebacks 通过 revision-3 post-write audit；其余 36 个候选完成 No Change 对读；withdrawn identity 不具 Books eligibility | passed |

## 8. Ignored Noise

450 项未进入 Candidate Denominator；逐项机制、证据与可重开条件保存在 `screening-ledger-final.json/tsv`，不是静默丢弃。

其中 `arXiv:2605.04356v1` 保留为 withdrawal-specific closure：identity/date 为 2026-05-05T23:25:00Z；official arXiv abs 标记 withdrawn by Joe Benton，并说明管理员因提交者当时无权同意许可而移除 v1。该 identity 不评分、不做 Source Review、不映射 Books owner，也不构成 blocker；若新 revision 公开，按其自身 first-public time 和 evidence identity 重新路由。

## 9. Recommended Action

无剩余动作。63-family Evidence/Books Decision、27 项 Books writeback/post-write audit 与 450 项 pre-denominator closure 均已闭合；withdrawn identity 只保留可审计状态，不再请求已撤回 v1 的全文。

## 10. Repository Changes

Author、root writer 与独立 reviewer 的既有修改保持不变；本轮只同步 `papers/2026/05/06` 与 `papers/2026/05/_sources/daily-20260506` 的 withdrawal closure、分母、收据、audit scope 与 Gate 真值。未修改共享 Books，未 stage、commit 或 push。

## 11. Open Questions

- 无阻塞 05-06 Gate 的 Open Question。若该工作以后以新 revision 重新公开，应按新 revision 的 first-public time、许可与 exact-version evidence 重新入场，而不是恢复已撤回 v1 的 candidate 身份。

## 12. Sources

- DataCite arXiv v2 month snapshots（identity/date/abstract recovery；accessed 2026-09-01）
- 62 项 official arXiv exact-v1 HTML/PDF，URL 逐项记录于 Review Completion Receipt（accessed 2026-09-01）
- `2605.03275v1` licensed full-text recovery receipt（exact title/authors/arXiv DOI reconciliation；accessed 2026-09-01）
- [official arXiv abs: 2605.04356v1](https://arxiv.org/abs/2605.04356v1)（withdrawn-by、admin removal、submission time 与 license status；rechecked 2026-09-01）

## 13. Final Status

Completion Status: `Complete`

Coverage: `Closed`

Evidence: `Passed`

Books: `Passed`

unresolved findings: 0

513/513 Coverage replay、63/63 body-level Review、所有 Books Decision 与 27/27 Books writeback 已通过 fresh-context / post-write audit。`2605.04356v1` 已按 official withdrawn 状态从 denominator 与全部 candidate-stage contracts 移除并转为 pre-denominator closure；ordinary pending=0、blocker=0，因此三个 Gate 均已通过。
