# Daily Research — 2026-05-19

**Research Date:** 2026-05-19

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-05-18 09:00:00 ～ 2026-05-19 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Historical Daily Independent Full Replay

**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed；initial-created owner replay 与 exact-v1 Evidence Review 已完成。

## Executive Summary

本次独立重放枚举并逐项闭合 1348 个注册 arXiv identity，冻结 147 个 Source Family；pre-denominator closure=1201，withdrawn pre-denominator=0。104 个旧候选被迁回正确 owner day，1 个漏检 family 已恢复 exact-v1 全文并完成 Source Review。

DataCite `created` 仅作为 initial DOI registration 的 owner-day proxy；`updated`、v1 Updated 与 current OAI datestamp 只记录 revision provenance，不决定 first-public owner。机制结论只绑定 exact-v1 正文。 本日所有 Books disposition 已有终态。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-05-19 |
| Window End | 2026-05-19 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | DEN-20260519-CREATED-d0d307dffb8f61ca |
| Denominator Frozen At | 2026-09-03T12:36:05+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-05-18T09:00:00+08:00 | 2026-05-19T09:00:00+08:00 | 2026-09-03T12:36:05+08:00 | DataCite prefix 10.48550 initial created-day inventory + registered arXiv categories + exact-v1 identity/body | checked | 1348 | SF-2026-ARXIV-2605-16265;SF-2026-ARXIV-2605-16343;SF-2026-ARXIV-2605-16346;SF-2026-ARXIV-2605-16354;SF-2026-ARXIV-2605-16359;SF-2026-ARXIV-2605-16360;SF-2026-ARXIV-2605-16436;SF-2026-ARXIV-2605-16439;SF-2026-ARXIV-2605-16508;SF-2026-ARXIV-2605-16565;SF-2026-ARXIV-2605-16604;SF-2026-ARXIV-2605-16616;SF-2026-ARXIV-2605-16626;SF-2026-ARXIV-2605-16630;SF-2026-ARXIV-2605-16637;SF-2026-ARXIV-2605-16650;SF-2026-ARXIV-2605-16704;SF-2026-ARXIV-2605-16712;SF-2026-ARXIV-2605-16725;SF-2026-ARXIV-2605-16745;SF-2026-ARXIV-2605-16746;SF-2026-ARXIV-2605-16776;SF-2026-ARXIV-2605-16786;SF-2026-ARXIV-2605-16787;SF-2026-ARXIV-2605-16790;SF-2026-ARXIV-2605-16819;SF-2026-ARXIV-2605-16826;SF-2026-ARXIV-2605-16839;SF-2026-ARXIV-2605-16867;SF-2026-ARXIV-2605-16928;SF-2026-ARXIV-2605-16976;SF-2026-ARXIV-2605-16986;SF-2026-ARXIV-2605-17003;SF-2026-ARXIV-2605-17026;SF-2026-ARXIV-2605-17028;SF-2026-ARXIV-2605-17034;SF-2026-ARXIV-2605-17062;SF-2026-ARXIV-2605-17076;SF-2026-ARXIV-2605-17106;SF-2026-ARXIV-2605-17113;SF-2026-ARXIV-2605-17160;SF-2026-ARXIV-2605-17164;SF-2026-ARXIV-2605-17169;SF-2026-ARXIV-2605-17170;SF-2026-ARXIV-2605-17172;SF-2026-ARXIV-2605-17173;SF-2026-ARXIV-2605-17193;SF-2026-ARXIV-2605-17222;SF-2026-ARXIV-2605-17234;SF-2026-ARXIV-2605-17242;SF-2026-ARXIV-2605-17246;SF-2026-ARXIV-2605-17260;SF-2026-ARXIV-2605-17268;SF-2026-ARXIV-2605-17273;SF-2026-ARXIV-2605-17281;SF-2026-ARXIV-2605-17288;SF-2026-ARXIV-2605-17289;SF-2026-ARXIV-2605-17291;SF-2026-ARXIV-2605-17292;SF-2026-ARXIV-2605-17301;SF-2026-ARXIV-2605-17304;SF-2026-ARXIV-2605-17305;SF-2026-ARXIV-2605-17320;SF-2026-ARXIV-2605-17324;SF-2026-ARXIV-2605-17329;SF-2026-ARXIV-2605-17348;SF-2026-ARXIV-2605-17360;SF-2026-ARXIV-2605-17373;SF-2026-ARXIV-2605-17380;SF-2026-ARXIV-2605-17415;SF-2026-ARXIV-2605-17439;SF-2026-ARXIV-2605-17453;SF-2026-ARXIV-2605-17467;SF-2026-ARXIV-2605-17471;SF-2026-ARXIV-2605-17480;SF-2026-ARXIV-2605-17497;SF-2026-ARXIV-2605-17508;SF-2026-ARXIV-2605-17522;SF-2026-ARXIV-2605-17554;SF-2026-ARXIV-2605-17558;SF-2026-ARXIV-2605-17570;SF-2026-ARXIV-2605-17590;SF-2026-ARXIV-2605-17609;SF-2026-ARXIV-2605-17610;SF-2026-ARXIV-2605-17613;SF-2026-ARXIV-2605-17617;SF-2026-ARXIV-2605-17625;SF-2026-ARXIV-2605-17634;SF-2026-ARXIV-2605-17641;SF-2026-ARXIV-2605-17659;SF-2026-ARXIV-2605-17672;SF-2026-ARXIV-2605-17683;SF-2026-ARXIV-2605-17707;SF-2026-ARXIV-2605-17721;SF-2026-ARXIV-2605-17734;SF-2026-ARXIV-2605-17757;SF-2026-ARXIV-2605-17787;SF-2026-ARXIV-2605-17821;SF-2026-ARXIV-2605-17830;SF-2026-ARXIV-2605-17842;SF-2026-ARXIV-2605-17849;SF-2026-ARXIV-2605-17862;SF-2026-ARXIV-2605-17877;SF-2026-ARXIV-2605-17879;SF-2026-ARXIV-2605-17889;SF-2026-ARXIV-2605-17912;SF-2026-ARXIV-2605-17921;SF-2026-ARXIV-2605-17923;SF-2026-ARXIV-2605-17932;SF-2026-ARXIV-2605-17954;SF-2026-ARXIV-2605-17986;SF-2026-ARXIV-2605-17989;SF-2026-ARXIV-2605-17992;SF-2026-ARXIV-2605-17998;SF-2026-ARXIV-2605-18032;SF-2026-ARXIV-2605-18041;SF-2026-ARXIV-2605-18053;SF-2026-ARXIV-2605-18067;SF-2026-ARXIV-2605-18071;SF-2026-ARXIV-2605-18106;SF-2026-ARXIV-2605-18165;SF-2026-ARXIV-2605-18271;SF-2026-ARXIV-2605-18401;SF-2026-ARXIV-2605-18414;SF-2026-ARXIV-2605-18421;SF-2026-ARXIV-2605-18498;SF-2026-ARXIV-2605-18565;SF-2026-ARXIV-2605-18583;SF-2026-ARXIV-2605-18607;SF-2026-ARXIV-2605-18652;SF-2026-ARXIV-2605-18693;SF-2026-ARXIV-2605-18697;SF-2026-ARXIV-2605-18703;SF-2026-ARXIV-2605-18710;SF-2026-ARXIV-2605-18739;SF-2026-ARXIV-2605-18750;SF-2026-ARXIV-2605.16588;SF-2026-ARXIV-2605.16622;SF-2026-ARXIV-2605.16647;SF-ANNEAL-GOVERNED-SYMBOLIC-PATCHES;SF-FRE-RES-FREQUENCY-RESIDUAL-VIDEO-TOKEN-COMPRESSION-FOR-EFFICIENT-VIDEO-M;SF-MIXING-TIMES-OF-GLAUBER-DYNAMICS-ON-MASKED-LANGUAGE-MODELS;SF-ORBISIM-WORLD-MODELS-AS-DIFFERENTIABLE-PHYSICS-ENGINES-FOR-EMBODIED-INTE;SF-ORTH-DION-ELIMINATING-GEOMETRIC-MISMATCH-IN-DISTRIBUTED-LOW-RANK-SPECTRA;SF-PROOF-CARRYING-CERTIFICATES-FOR-LLM-PIPELINES-A-TRUST-BOUNDARY-ARCHITECT;SF-SELFPLAY-DECISION-CAPACITY-COLLAPSE;SF-SIGNMUON-SIGN-ORTHOGONALIZED-OPTIMIZER | created-day pages=closed; OAI category sets=closed; direct same-day OAI=1025 | 2026-05-19T09:00:00+08:00 | coverage:SRC-ARXIV:20260519 | — |

<!-- coverage:SRC-ARXIV:20260519:start -->全量 raw inventory=1348；每个 identity 均具有 retained、family-specific closure 或 withdrawn terminal closure。候选 owner 由 initial DataCite created、arXiv ID month、v1 history 与 announcement cadence 共同约束；冲突不由 updated 字段覆盖。<!-- coverage:SRC-ARXIV:20260519:end -->

### Coverage Limitations

- arXiv 月度 listing 只证明月份收录；逐日 owner 使用 initial DOI `created` 日历日 proxy，并以 exact-v1 history 与官方发布节奏约束。
- DOI ingestion timestamp 不是精确的 09:00 publication instant；本日报不把 `updated` 或 current OAI datestamp 当作 first-public。

### Materials Request Ledger

<!-- validator:materials-request-v1 -->
| Request ID | Priority | Source Family ID | Source ID | Gap / Limitation ID | Owner Week | Known Identifiers / URLs | Missing Material | Why Existing Evidence Is Insufficient | Acceptable Substitute | Suggested File Name | Required Review Scope |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
None — 没有 exact-version primary-material blocker。

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-16265 | arXiv:2605.16265v1 | paper-v1:2605.16265 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-16265 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16265 | yes |
| SF-2026-ARXIV-2605-16343 | arXiv:2605.16343v1 | paper-v1:2605.16343 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2605-16343 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16343 | no |
| SF-2026-ARXIV-2605-16346 | arXiv:2605.16346v1 | paper-v1:2605.16346 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-16346 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16346 | no |
| SF-2026-ARXIV-2605-16354 | arXiv:2605.16354v1 | paper-v1:2605.16354 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2605-16354 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16354 | no |
| SF-2026-ARXIV-2605-16359 | arXiv:2605.16359v1 | paper-v1:2605.16359 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 2 | 1 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2605-16359 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16359 | no |
| SF-2026-ARXIV-2605-16360 | arXiv:2605.16360v1 | paper-v1:2605.16360 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-16360 | self | — | new_in_window | INFER-KV-CACHE | Integrate | books-review:SF-2026-ARXIV-2605-16360 | no |
| SF-2026-ARXIV-2605-16436 | arXiv:2605.16436v1 | paper-v1:2605.16436 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-16436 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16436 | no |
| SF-2026-ARXIV-2605-16439 | arXiv:2605.16439v1 | paper-v1:2605.16439 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-16439 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16439 | no |
| SF-2026-ARXIV-2605-16508 | arXiv:2605.16508v1 | paper-v1:2605.16508 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-16508 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16508 | no |
| SF-2026-ARXIV-2605-16565 | arXiv:2605.16565v1 | paper-v1:2605.16565 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-16565 | self | — | new_in_window | AGENT-PLANNING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16565 | no |
| SF-2026-ARXIV-2605-16604 | arXiv:2605.16604v1 | paper-v1:2605.16604 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-16604 | self | — | new_in_window | AGENT-TOOL-CALLING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16604 | no |
| SF-2026-ARXIV-2605-16616 | arXiv:2605.16616v1 | paper-v1:2605.16616 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-16616 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16616 | no |
| SF-2026-ARXIV-2605-16626 | arXiv:2605.16626v1 | paper-v1:2605.16626 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-16626 | self | — | new_in_window | PLATFORM-MONITORING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16626 | no |
| SF-2026-ARXIV-2605-16630 | arXiv:2605.16630v1 | paper-v1:2605.16630 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-16630 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16630 | no |
| SF-2026-ARXIV-2605-16637 | arXiv:2605.16637v1 | paper-v1:2605.16637 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-16637 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16637 | no |
| SF-2026-ARXIV-2605-16650 | arXiv:2605.16650v1 | paper-v1:2605.16650 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-16650 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16650 | no |
| SF-2026-ARXIV-2605-16704 | arXiv:2605.16704v1 | paper-v1:2605.16704 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-16704 | self | — | new_in_window | TRAIN-DATA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16704 | no |
| SF-2026-ARXIV-2605-16712 | arXiv:2605.16712v1 | paper-v1:2605.16712 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-16712 | self | — | new_in_window | AGENT-MEMORY | Integrate | books-review:SF-2026-ARXIV-2605-16712 | no |
| SF-2026-ARXIV-2605-16725 | arXiv:2605.16725v1 | paper-v1:2605.16725 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-16725 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16725 | no |
| SF-2026-ARXIV-2605-16745 | arXiv:2605.16745v1 | paper-v1:2605.16745 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-16745 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | Integrate | books-review:SF-2026-ARXIV-2605-16745 | no |
| SF-2026-ARXIV-2605-16746 | arXiv:2605.16746v1 | paper-v1:2605.16746 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-16746 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16746 | no |
| SF-2026-ARXIV-2605-16776 | arXiv:2605.16776v1 | paper-v1:2605.16776 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-16776 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2605-16776 | no |
| SF-2026-ARXIV-2605-16786 | arXiv:2605.16786v1 | paper-v1:2605.16786 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-16786 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | Integrate | books-review:SF-2026-ARXIV-2605-16786 | no |
| SF-2026-ARXIV-2605-16787 | arXiv:2605.16787v1 | paper-v1:2605.16787 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-16787 | self | — | new_in_window | TRAIN-GRPO | Integrate | books-review:SF-2026-ARXIV-2605-16787 | no |
| SF-2026-ARXIV-2605-16790 | arXiv:2605.16790v1 | paper-v1:2605.16790 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-16790 | self | — | new_in_window | AGENT-TOOL-CALLING | Integrate | books-review:SF-2026-ARXIV-2605-16790 | no |
| SF-2026-ARXIV-2605-16819 | arXiv:2605.16819v1 | paper-v1:2605.16819 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-16819 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2605-16819 | no |
| SF-2026-ARXIV-2605-16826 | arXiv:2605.16826v1 | paper-v1:2605.16826 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-16826 | self | — | new_in_window | TRAIN-PRETRAINING | Integrate | books-review:SF-2026-ARXIV-2605-16826 | no |
| SF-2026-ARXIV-2605-16839 | arXiv:2605.16839v1 | paper-v1:2605.16839 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-16839 | self | — | new_in_window | INFER-PREFILL | Integrate | books-review:SF-2026-ARXIV-2605-16839 | no |
| SF-2026-ARXIV-2605-16867 | arXiv:2605.16867v1 | paper-v1:2605.16867 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-16867 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16867 | no |
| SF-2026-ARXIV-2605-16928 | arXiv:2605.16928v1 | paper-v1:2605.16928 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-16928 | self | — | new_in_window | INFER-KV-CACHE | Integrate | books-review:SF-2026-ARXIV-2605-16928 | no |
| SF-2026-ARXIV-2605-16976 | arXiv:2605.16976v1 | paper-v1:2605.16976 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-16976 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2605-16976 | no |
| SF-2026-ARXIV-2605-16986 | arXiv:2605.16986v1 | paper-v1:2605.16986 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-16986 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16986 | no |
| SF-2026-ARXIV-2605-17003 | arXiv:2605.17003v1 | paper-v1:2605.17003 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-17003 | self | — | new_in_window | TRAIN-DATA | Integrate | books-review:SF-2026-ARXIV-2605-17003 | no |
| SF-2026-ARXIV-2605-17026 | arXiv:2605.17026v1 | paper-v1:2605.17026 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-17026 | self | — | new_in_window | TRAIN-DATA | Integrate | books-review:SF-2026-ARXIV-2605-17026 | no |
| SF-2026-ARXIV-2605-17028 | arXiv:2605.17028v1 | paper-v1:2605.17028 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17028 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17028 | no |
| SF-2026-ARXIV-2605-17034 | arXiv:2605.17034v1 | paper-v1:2605.17034 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17034 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17034 | no |
| SF-2026-ARXIV-2605-17062 | arXiv:2605.17062v1 | paper-v1:2605.17062 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17062 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17062 | no |
| SF-2026-ARXIV-2605-17076 | arXiv:2605.17076v1 | paper-v1:2605.17076 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-17076 | self | — | new_in_window | AGENT-MULTI-AGENT | Integrate | books-review:SF-2026-ARXIV-2605-17076 | no |
| SF-2026-ARXIV-2605-17106 | arXiv:2605.17106v1 | paper-v1:2605.17106 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-17106 | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-2026-ARXIV-2605-17106 | no |
| SF-2026-ARXIV-2605-17113 | arXiv:2605.17113v1 | paper-v1:2605.17113 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-17113 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2605-17113 | no |
| SF-2026-ARXIV-2605-17160 | arXiv:2605.17160v1 | paper-v1:2605.17160 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-17160 | self | — | new_in_window | INFER-TENSORRT-LLM | Integrate | books-review:SF-2026-ARXIV-2605-17160 | no |
| SF-2026-ARXIV-2605-17164 | arXiv:2605.17164v1 | paper-v1:2605.17164 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-17164 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2605-17164 | no |
| SF-2026-ARXIV-2605-17169 | arXiv:2605.17169v1 | paper-v1:2605.17169 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17169 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17169 | no |
| SF-2026-ARXIV-2605-17170 | arXiv:2605.17170v1 | paper-v1:2605.17170 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-17170 | self | — | new_in_window | INFER-KV-CACHE | Integrate | books-review:SF-2026-ARXIV-2605-17170 | no |
| SF-2026-ARXIV-2605-17172 | arXiv:2605.17172v1 | paper-v1:2605.17172 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17172 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17172 | no |
| SF-2026-ARXIV-2605-17173 | arXiv:2605.17173v1 | paper-v1:2605.17173 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-17173 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2605-17173 | no |
| SF-2026-ARXIV-2605-17193 | arXiv:2605.17193v1 | paper-v1:2605.17193 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17193 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17193 | no |
| SF-2026-ARXIV-2605-17222 | arXiv:2605.17222v1 | paper-v1:2605.17222 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17222 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17222 | no |
| SF-2026-ARXIV-2605-17234 | arXiv:2605.17234v1 | paper-v1:2605.17234 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17234 | self | — | new_in_window | WORLDVIEW-SCALING-LAW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17234 | no |
| SF-2026-ARXIV-2605-17242 | arXiv:2605.17242v1 | paper-v1:2605.17242 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17242 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17242 | no |
| SF-2026-ARXIV-2605-17246 | arXiv:2605.17246v1 | paper-v1:2605.17246 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17246 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17246 | no |
| SF-2026-ARXIV-2605-17260 | arXiv:2605.17260v1 | paper-v1:2605.17260 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17260 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17260 | no |
| SF-2026-ARXIV-2605-17268 | arXiv:2605.17268v1 | paper-v1:2605.17268 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17268 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17268 | no |
| SF-2026-ARXIV-2605-17273 | arXiv:2605.17273v1 | paper-v1:2605.17273 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17273 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17273 | no |
| SF-2026-ARXIV-2605-17281 | arXiv:2605.17281v1 | paper-v1:2605.17281 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-17281 | self | — | new_in_window | AGENT-TOOL-CALLING | Integrate | books-review:SF-2026-ARXIV-2605-17281 | no |
| SF-2026-ARXIV-2605-17288 | arXiv:2605.17288v1 | paper-v1:2605.17288 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17288 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17288 | no |
| SF-2026-ARXIV-2605-17289 | arXiv:2605.17289v1 | paper-v1:2605.17289 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17289 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17289 | no |
| SF-2026-ARXIV-2605-17291 | arXiv:2605.17291v1 | paper-v1:2605.17291 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17291 | self | — | new_in_window | TRAIN-RLHF | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17291 | no |
| SF-2026-ARXIV-2605-17292 | arXiv:2605.17292v1 | paper-v1:2605.17292 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17292 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17292 | no |
| SF-2026-ARXIV-2605-17301 | arXiv:2605.17301v1 | paper-v1:2605.17301 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17301 | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17301 | no |
| SF-2026-ARXIV-2605-17304 | arXiv:2605.17304v1 | paper-v1:2605.17304 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17304 | self | — | new_in_window | AGENT-CONTEXT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17304 | no |
| SF-2026-ARXIV-2605-17305 | arXiv:2605.17305v1 | paper-v1:2605.17305 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17305 | self | — | new_in_window | AGENT-REFLECTION | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17305 | no |
| SF-2026-ARXIV-2605-17320 | arXiv:2605.17320v1 | paper-v1:2605.17320 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17320 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17320 | no |
| SF-2026-ARXIV-2605-17324 | arXiv:2605.17324v1 | paper-v1:2605.17324 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-17324 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2605-17324 | no |
| SF-2026-ARXIV-2605-17329 | arXiv:2605.17329v1 | paper-v1:2605.17329 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17329 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17329 | no |
| SF-2026-ARXIV-2605-17348 | arXiv:2605.17348v1 | paper-v1:2605.17348 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17348 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17348 | no |
| SF-2026-ARXIV-2605-17360 | arXiv:2605.17360v1 | paper-v1:2605.17360 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-17360 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2605-17360 | no |
| SF-2026-ARXIV-2605-17373 | arXiv:2605.17373v1 | paper-v1:2605.17373 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17373 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17373 | no |
| SF-2026-ARXIV-2605-17380 | arXiv:2605.17380v1 | paper-v1:2605.17380 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-17380 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2605-17380 | no |
| SF-2026-ARXIV-2605-17415 | arXiv:2605.17415v1 | paper-v1:2605.17415 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17415 | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17415 | no |
| SF-2026-ARXIV-2605-17439 | arXiv:2605.17439v1 | paper-v1:2605.17439 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17439 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17439 | no |
| SF-2026-ARXIV-2605-17453 | arXiv:2605.17453v1 | paper-v1:2605.17453 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17453 | self | — | new_in_window | AGENT-TOOL-CALLING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17453 | no |
| SF-2026-ARXIV-2605-17467 | arXiv:2605.17467v1 | paper-v1:2605.17467 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17467 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17467 | no |
| SF-2026-ARXIV-2605-17471 | arXiv:2605.17471v1 | paper-v1:2605.17471 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17471 | self | — | new_in_window | TRAIN-PRETRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17471 | no |
| SF-2026-ARXIV-2605-17480 | arXiv:2605.17480v1 | paper-v1:2605.17480 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17480 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17480 | no |
| SF-2026-ARXIV-2605-17497 | arXiv:2605.17497v1 | paper-v1:2605.17497 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-17497 | self | — | new_in_window | TRAIN-GRPO | Integrate | books-review:SF-2026-ARXIV-2605-17497 | no |
| SF-2026-ARXIV-2605-17508 | arXiv:2605.17508v1 | paper-v1:2605.17508 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17508 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17508 | no |
| SF-2026-ARXIV-2605-17522 | arXiv:2605.17522v1 | paper-v1:2605.17522 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17522 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17522 | no |
| SF-2026-ARXIV-2605-17554 | arXiv:2605.17554v1 | paper-v1:2605.17554 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17554 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17554 | no |
| SF-2026-ARXIV-2605-17558 | arXiv:2605.17558v1 | paper-v1:2605.17558 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17558 | self | — | new_in_window | AGENT-TOOL-CALLING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17558 | no |
| SF-2026-ARXIV-2605-17570 | arXiv:2605.17570v1 | paper-v1:2605.17570 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-17570 | self | — | new_in_window | TRAIN-GRPO | Integrate | books-review:SF-2026-ARXIV-2605-17570 | no |
| SF-2026-ARXIV-2605-17590 | arXiv:2605.17590v1 | paper-v1:2605.17590 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-17590 | self | — | new_in_window | TRAIN-DATA | Integrate | books-review:SF-2026-ARXIV-2605-17590 | no |
| SF-2026-ARXIV-2605-17609 | arXiv:2605.17609v1 | paper-v1:2605.17609 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17609 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17609 | no |
| SF-2026-ARXIV-2605-17610 | arXiv:2605.17610v1 | paper-v1:2605.17610 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17610 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17610 | no |
| SF-2026-ARXIV-2605-17613 | arXiv:2605.17613v1 | paper-v1:2605.17613 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-17613 | self | — | new_in_window | INFER-KV-CACHE | Integrate | books-review:SF-2026-ARXIV-2605-17613 | no |
| SF-2026-ARXIV-2605-17617 | arXiv:2605.17617v1 | paper-v1:2605.17617 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17617 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17617 | no |
| SF-2026-ARXIV-2605-17625 | arXiv:2605.17625v1 | paper-v1:2605.17625 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17625 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17625 | no |
| SF-2026-ARXIV-2605-17634 | arXiv:2605.17634v1 | paper-v1:2605.17634 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17634 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17634 | no |
| SF-2026-ARXIV-2605-17641 | arXiv:2605.17641v1 | paper-v1:2605.17641 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17641 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17641 | no |
| SF-2026-ARXIV-2605-17659 | arXiv:2605.17659v1 | paper-v1:2605.17659 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-17659 | self | — | new_in_window | TRAIN-PRETRAINING | Integrate | books-review:SF-2026-ARXIV-2605-17659 | no |
| SF-2026-ARXIV-2605-17672 | arXiv:2605.17672v1 | paper-v1:2605.17672 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17672 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17672 | no |
| SF-2026-ARXIV-2605-17683 | arXiv:2605.17683v1 | paper-v1:2605.17683 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-17683 | self | — | new_in_window | INFER-TENSORRT-LLM | Integrate | books-review:SF-2026-ARXIV-2605-17683 | no |
| SF-2026-ARXIV-2605-17707 | arXiv:2605.17707v1 | paper-v1:2605.17707 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-17707 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2605-17707 | no |
| SF-2026-ARXIV-2605-17721 | arXiv:2605.17721v1 | paper-v1:2605.17721 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17721 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17721 | no |
| SF-2026-ARXIV-2605-17734 | arXiv:2605.17734v1 | paper-v1:2605.17734 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17734 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17734 | no |
| SF-2026-ARXIV-2605-17757 | arXiv:2605.17757v1 | paper-v1:2605.17757 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17757 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17757 | no |
| SF-2026-ARXIV-2605-17787 | arXiv:2605.17787v1 | paper-v1:2605.17787 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17787 | self | — | new_in_window | TRAIN-PRETRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17787 | no |
| SF-2026-ARXIV-2605-17821 | arXiv:2605.17821v1 | paper-v1:2605.17821 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-17821 | self | — | new_in_window | TRAIN-CHECKPOINT | Integrate | books-review:SF-2026-ARXIV-2605-17821 | no |
| SF-2026-ARXIV-2605-17830 | arXiv:2605.17830v1 | paper-v1:2605.17830 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17830 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17830 | no |
| SF-2026-ARXIV-2605-17842 | arXiv:2605.17842v1 | paper-v1:2605.17842 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-17842 | self | — | new_in_window | INFER-TENSORRT-LLM | Integrate | books-review:SF-2026-ARXIV-2605-17842 | no |
| SF-2026-ARXIV-2605-17849 | arXiv:2605.17849v1 | paper-v1:2605.17849 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17849 | self | — | new_in_window | TRAIN-DATA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17849 | no |
| SF-2026-ARXIV-2605-17862 | arXiv:2605.17862v1 | paper-v1:2605.17862 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-17862 | self | — | new_in_window | TRAIN-RLHF | Integrate | books-review:SF-2026-ARXIV-2605-17862 | no |
| SF-2026-ARXIV-2605-17877 | arXiv:2605.17877v1 | paper-v1:2605.17877 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-17877 | self | — | new_in_window | TRAIN-RLHF | Integrate | books-review:SF-2026-ARXIV-2605-17877 | no |
| SF-2026-ARXIV-2605-17879 | arXiv:2605.17879v1 | paper-v1:2605.17879 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-17879 | self | — | new_in_window | PLATFORM-MONITORING | Integrate | books-review:SF-2026-ARXIV-2605-17879 | no |
| SF-2026-ARXIV-2605-17889 | arXiv:2605.17889v1 | paper-v1:2605.17889 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-17889 | self | — | new_in_window | INFER-TENSORRT-LLM | Integrate | books-review:SF-2026-ARXIV-2605-17889 | no |
| SF-2026-ARXIV-2605-17912 | arXiv:2605.17912v1 | paper-v1:2605.17912 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17912 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17912 | no |
| SF-2026-ARXIV-2605-17921 | arXiv:2605.17921v1 | paper-v1:2605.17921 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17921 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17921 | no |
| SF-2026-ARXIV-2605-17923 | arXiv:2605.17923v1 | paper-v1:2605.17923 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-17923 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Integrate | books-review:SF-2026-ARXIV-2605-17923 | no |
| SF-2026-ARXIV-2605-17932 | arXiv:2605.17932v1 | paper-v1:2605.17932 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17932 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17932 | no |
| SF-2026-ARXIV-2605-17954 | arXiv:2605.17954v1 | paper-v1:2605.17954 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17954 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17954 | no |
| SF-2026-ARXIV-2605-17986 | arXiv:2605.17986v1 | paper-v1:2605.17986 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17986 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17986 | no |
| SF-2026-ARXIV-2605-17989 | arXiv:2605.17989v1 | paper-v1:2605.17989 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-17989 | self | — | new_in_window | AGENT-RAG | Integrate | books-review:SF-2026-ARXIV-2605-17989 | no |
| SF-2026-ARXIV-2605-17992 | arXiv:2605.17992v1 | paper-v1:2605.17992 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-17992 | self | — | new_in_window | AGENT-RAG | Integrate | books-review:SF-2026-ARXIV-2605-17992 | no |
| SF-2026-ARXIV-2605-17998 | arXiv:2605.17998v1 | paper-v1:2605.17998 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-17998 | self | — | new_in_window | AGENT-WORKFLOW | Integrate | books-review:SF-2026-ARXIV-2605-17998 | no |
| SF-2026-ARXIV-2605-18032 | arXiv:2605.18032v1 | paper-v1:2605.18032 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-18032 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18032 | no |
| SF-2026-ARXIV-2605-18041 | arXiv:2605.18041v1 | paper-v1:2605.18041 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2605-18041 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18041 | no |
| SF-2026-ARXIV-2605-18053 | arXiv:2605.18053v1 | paper-v1:2605.18053 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-18053 | self | — | new_in_window | INFER-KV-CACHE | Integrate | books-review:SF-2026-ARXIV-2605-18053 | no |
| SF-2026-ARXIV-2605-18067 | arXiv:2605.18067v1 | paper-v1:2605.18067 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-18067 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18067 | no |
| SF-2026-ARXIV-2605-18071 | arXiv:2605.18071v1 | paper-v1:2605.18071 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-18071 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18071 | no |
| SF-2026-ARXIV-2605-18106 | arXiv:2605.18106v1 | paper-v1:2605.18106 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-18106 | self | — | new_in_window | TRAIN-PRETRAINING | Integrate | books-review:SF-2026-ARXIV-2605-18106 | no |
| SF-2026-ARXIV-2605-18165 | arXiv:2605.18165v1 | paper-v1:2605.18165 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-18165 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18165 | no |
| SF-2026-ARXIV-2605-18271 | arXiv:2605.18271v1 | paper-v1:2605.18271 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-18271 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18271 | no |
| SF-2026-ARXIV-2605-18401 | arXiv:2605.18401v1 | paper-v1:2605.18401 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-18401 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18401 | no |
| SF-2026-ARXIV-2605-18414 | arXiv:2605.18414v1 | paper-v1:2605.18414 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-18414 | self | — | new_in_window | AGENT-MCP | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18414 | no |
| SF-2026-ARXIV-2605-18421 | arXiv:2605.18421v1 | paper-v1:2605.18421 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-18421 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18421 | no |
| SF-2026-ARXIV-2605-18498 | arXiv:2605.18498v1 | paper-v1:2605.18498 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-18498 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2605-18498 | no |
| SF-2026-ARXIV-2605-18565 | arXiv:2605.18565v1 | paper-v1:2605.18565 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-18565 | self | — | new_in_window | AGENT-MEMORY | Integrate | books-review:SF-2026-ARXIV-2605-18565 | no |
| SF-2026-ARXIV-2605-18583 | arXiv:2605.18583v1 | paper-v1:2605.18583 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-18583 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18583 | no |
| SF-2026-ARXIV-2605-18607 | arXiv:2605.18607v1 | paper-v1:2605.18607 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-18607 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18607 | no |
| SF-2026-ARXIV-2605-18652 | arXiv:2605.18652v1 | paper-v1:2605.18652 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-18652 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18652 | no |
| SF-2026-ARXIV-2605-18693 | arXiv:2605.18693v1 | paper-v1:2605.18693 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-18693 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18693 | no |
| SF-2026-ARXIV-2605-18697 | arXiv:2605.18697v1 | paper-v1:2605.18697 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-18697 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18697 | no |
| SF-2026-ARXIV-2605-18703 | arXiv:2605.18703v1 | paper-v1:2605.18703 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-18703 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18703 | no |
| SF-2026-ARXIV-2605-18710 | arXiv:2605.18710v1 | paper-v1:2605.18710 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-18710 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Integrate | books-review:SF-2026-ARXIV-2605-18710 | no |
| SF-2026-ARXIV-2605-18739 | arXiv:2605.18739v1 | paper-v1:2605.18739 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-18739 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18739 | no |
| SF-2026-ARXIV-2605-18750 | arXiv:2605.18750v1 | paper-v1:2605.18750 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-18750 | self | — | new_in_window | TRAIN-PIPELINE-PARALLEL | Integrate | books-review:SF-2026-ARXIV-2605-18750 | no |
| SF-2026-ARXIV-2605.16588 | arXiv:2605.16588v1 | paper-v1:2605.16588 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605.16588 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605.16588 | no |
| SF-2026-ARXIV-2605.16622 | arXiv:2605.16622v1 | paper-v1:2605.16622 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605.16622 | self | — | new_in_window | TRAIN-PRETRAINING | Integrate | books-review:SF-2026-ARXIV-2605.16622 | no |
| SF-2026-ARXIV-2605.16647 | arXiv:2605.16647v1 | paper-v1:2605.16647 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605.16647 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605.16647 | no |
| SF-ANNEAL-GOVERNED-SYMBOLIC-PATCHES | arXiv:2605.16309v1 | paper-v1:2605.16309 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-ANNEAL-GOVERNED-SYMBOLIC-PATCHES | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-ANNEAL-GOVERNED-SYMBOLIC-PATCHES | yes |
| SF-FRE-RES-FREQUENCY-RESIDUAL-VIDEO-TOKEN-COMPRESSION-FOR-EFFICIENT-VIDEO-M | arXiv:2605.16366v1 | paper-v1:2605.16366 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-FRE-RES-FREQUENCY-RESIDUAL-VIDEO-TOKEN-COMPRESSION-FOR-EFFICIENT-VIDEO-M | self | — | new_in_window | MULTIMODAL-REPRESENTATION | No Change — Existing Coverage | books-review:SF-FRE-RES-FREQUENCY-RESIDUAL-VIDEO-TOKEN-COMPRESSION-FOR-EFFICIENT-VIDEO-M | no |
| SF-MIXING-TIMES-OF-GLAUBER-DYNAMICS-ON-MASKED-LANGUAGE-MODELS | arXiv:2605.16378v1 | paper-v1:2605.16378 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-MIXING-TIMES-OF-GLAUBER-DYNAMICS-ON-MASKED-LANGUAGE-MODELS | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | No Change — Existing Coverage | books-review:SF-MIXING-TIMES-OF-GLAUBER-DYNAMICS-ON-MASKED-LANGUAGE-MODELS | no |
| SF-ORBISIM-WORLD-MODELS-AS-DIFFERENTIABLE-PHYSICS-ENGINES-FOR-EMBODIED-INTE | arXiv:2605.16395v1 | paper-v1:2605.16395 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-ORBISIM-WORLD-MODELS-AS-DIFFERENTIABLE-PHYSICS-ENGINES-FOR-EMBODIED-INTE | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-ORBISIM-WORLD-MODELS-AS-DIFFERENTIABLE-PHYSICS-ENGINES-FOR-EMBODIED-INTE | no |
| SF-ORTH-DION-ELIMINATING-GEOMETRIC-MISMATCH-IN-DISTRIBUTED-LOW-RANK-SPECTRA | arXiv:2605.16341v1 | paper-v1:2605.16341 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-ORTH-DION-ELIMINATING-GEOMETRIC-MISMATCH-IN-DISTRIBUTED-LOW-RANK-SPECTRA | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | No Change — Existing Coverage | books-review:SF-ORTH-DION-ELIMINATING-GEOMETRIC-MISMATCH-IN-DISTRIBUTED-LOW-RANK-SPECTRA | no |
| SF-PROOF-CARRYING-CERTIFICATES-FOR-LLM-PIPELINES-A-TRUST-BOUNDARY-ARCHITECT | arXiv:2605.16407v1 | paper-v1:2605.16407 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-PROOF-CARRYING-CERTIFICATES-FOR-LLM-PIPELINES-A-TRUST-BOUNDARY-ARCHITECT | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-PROOF-CARRYING-CERTIFICATES-FOR-LLM-PIPELINES-A-TRUST-BOUNDARY-ARCHITECT | no |
| SF-SELFPLAY-DECISION-CAPACITY-COLLAPSE | arXiv:2605.16315v1 | paper-v1:2605.16315 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-SELFPLAY-DECISION-CAPACITY-COLLAPSE | self | — | new_in_window | TRAIN-PPO | No Change — Existing Coverage | books-review:SF-SELFPLAY-DECISION-CAPACITY-COLLAPSE | yes |
| SF-SIGNMUON-SIGN-ORTHOGONALIZED-OPTIMIZER | arXiv:2605.16311v1 | paper-v1:2605.16311 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-SIGNMUON-SIGN-ORTHOGONALIZED-OPTIMIZER | self | — | new_in_window | TRAIN-PRETRAINING | No Change — Existing Coverage | books-review:SF-SIGNMUON-SIGN-ORTHOGONALIZED-OPTIMIZER | yes |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-16265 | RP-c638c1a1a9038b10 | deep | arXiv:2605.16265v1 | SRC-ARXIV@arXiv:2605.16265v1 | https://arxiv.org/html/2605.16265v1#S2 | https://arxiv.org/html/2605.16265v1#S4 | https://arxiv.org/html/2605.16265v1#S6 | Not Disclosed — exact-v1 review found no versioned public artifact contract | claim:SF-2026-ARXIV-2605-16265 | complete |
| SF-2026-ARXIV-2605-16343 | RP-105fe1a8df21ec48 | standard | arXiv:2605.16343v1 | SRC-ARXIV@arXiv:2605.16343v1 | https://arxiv.org/html/2605.16343v1 §3 LoopQ loop-aware PTQ — mechanism: We present the first systematic study of quantization in LoopLMs and identify three challenges: distribution shift across roles, state reuse across loop transitions, and recursive error accumulation. | https://arxiv.org/html/2605.16343v1 §4 seven-benchmark W4A4 evaluation — disclosed scope: Looped language models (LoopLMs) improve parameter efficiency by recursively reusing Transformer blocks, enabling deeper computation under a fixed model size. However, this reuse makes LoopLMs more fragile under post-training quantization (PTQ). We present the first systematic study of quantization in LoopLMs and identify three challenges: distribution… | https://arxiv.org/html/2605.16343v1 Discussion limitations; recursive architecture/model/quantization scope; exact-v1 §6 / Appendix non-proof boundary check — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO | https://arxiv.org/html/2605.16343v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-16343 | complete |
| SF-2026-ARXIV-2605-16346 | RP-2c680c80c0a2144d | deep | arXiv:2605.16346v1 | SRC-ARXIV@arXiv:2605.16346v1 | https://arxiv.org/html/2605.16346v1 §3 dual-view propagation graph; §4 inspector/remediation — mechanism: We propose PropGuard, a propagation-aware framework for safeguarding LLM-MAS. | https://arxiv.org/html/2605.16346v1 §5 four-topology/five-attack evaluation — disclosed scope: Experiments across four communication architectures and five attack settings demonstrate that PropGuard consistently lowers attack success while maintaining high task-level defense success, achieving a favorable effectiveness--efficiency trade-off. | https://arxiv.org/html/2605.16346v1 Discussion limitations; attack family and replay-remediation scope; exact-v1 §6 / Appendix non-proof boundary check — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO | https://arxiv.org/html/2605.16346v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-16346 | complete |
| SF-2026-ARXIV-2605-16354 | RP-6458cc9d64b9057e | standard | arXiv:2605.16354v1 | SRC-ARXIV@arXiv:2605.16354v1 | https://arxiv.org/html/2605.16354v1 §2 two-stage doubly robust design — mechanism: We propose to use a doubly robust estimator from the missing data literature, which takes advantage of the robustness property against the prediction model, since the missingness model is known by design. | https://arxiv.org/html/2605.16354v1 §3 sample-size/power analysis — disclosed scope: This paper (1) shifts the role of the LLM judge from substitutive to auxiliary, and (2) formulates the LLM-as-a-judge paradigm as one of augmenting human evaluation through a two-stage sampling design, where LLM evaluations are measured for all observations at the first stage and human ratings… | https://arxiv.org/html/2605.16354v1 Limitations: pilot R² sensitivity and corpus representativeness; exact-v1 §6 / Appendix non-proof boundary check — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO | https://arxiv.org/html/2605.16354v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-16354 | complete |
| SF-2026-ARXIV-2605-16359 | RP-de943576e61cb50d | standard | arXiv:2605.16359v1 | SRC-ARXIV@arXiv:2605.16359v1 | https://arxiv.org/html/2605.16359v1 §3 Method — mechanism: We propose F^3A, a training-free router for visual token pruning that operates before the language model consumes image tokens. | https://arxiv.org/html/2605.16359v1 §4 Experiments — disclosed scope: Vision-language models improve perception by feeding increasingly long visual token sequences into language backbones, but the resulting inference cost raises a basic scaling question: as multimodal models grow, how many visual tokens are actually needed, and how should they be allocated under a fixed visual token… | https://arxiv.org/html/2605.16359v1 Appendix E Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO | https://arxiv.org/html/2605.16359v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-16359 | complete |
| SF-2026-ARXIV-2605-16360 | RP-22ca47efa032efb3 | deep | arXiv:2605.16360v1 | SRC-ARXIV@arXiv:2605.16360v1 | https://arxiv.org/html/2605.16360v1 §4 ProxyKV and HybridAxialMapper — mechanism: To bridge this scoring-cost--accuracy gap, we propose ProxyKV, a cross-model proxy pruning framework that offloads importance scoring to a lightweight intra-family Small-Model Proxy executed asynchronously to the Large-Model Target. | https://arxiv.org/html/2605.16360v1 §5 Evaluation — disclosed scope: Efficient long-context inference in Large Language Models (LLMs) is severely constrained by the Key-Value (KV) cache memory wall, yet existing pruning methods force a choice between low-latency heuristics that sacrifice precision and high-precision reconstruction methods that incur prohibitive prefilling overhead. To bridge this scoring-cost--accuracy gap, we… | https://arxiv.org/html/2605.16360v1 §7 Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO | https://arxiv.org/html/2605.16360v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-16360 | complete |
| SF-2026-ARXIV-2605-16436 | RP-92445ffbb850d30a | deep | arXiv:2605.16436v1 | SRC-ARXIV@arXiv:2605.16436v1 | https://arxiv.org/html/2605.16436v1 §2–§5 Agentic Threat-Economics Analysis — mechanism boundary: For decades, the security of digital interaction has rested on an unacknowledged economic constraint. | https://arxiv.org/html/2605.16436v1 §3–§5 Case Analyses — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.16436v1 §6 Conclusion and position-paper evidence boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.16436v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-16436 | complete |
| SF-2026-ARXIV-2605-16439 | RP-06f912e920440eca | deep | arXiv:2605.16439v1 | SRC-ARXIV@arXiv:2605.16439v1 | https://arxiv.org/html/2605.16439v1 §3 KVCapsule — mechanism boundary: Vision-Language Models (VLMs) have emerged as a critical and fast-growing extension of Large Language Models (LLMs) that enable multimodal reasoning through both text and image inputs. | https://arxiv.org/html/2605.16439v1 §4–§5 Evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.16439v1 §6 Conclusion and disclosed model/workload boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.16439v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-16439 | complete |
| SF-2026-ARXIV-2605-16508 | RP-280a4dc89cbe3db1 | deep | arXiv:2605.16508v1 | SRC-ARXIV@arXiv:2605.16508v1 | arXiv:2605.16508v1 — Methodology: §§3–6 setup, execution law and skill-library law (official v1 HTML) | arXiv:2605.16508v1 — Experiments: §§3 and 6 experimental setup and auto-manager evaluation (official v1 HTML) | arXiv:2605.16508v1 — Scope and limitations: §7 Discussion (official v1 HTML) | webcache-2605.16508.txt#sha256=55242c194e1bbe795d4f836d0373db41d7cff56723d1af1944e3b08c9d155756; immutable artifact commit Not Disclosed | claim:SF-2026-ARXIV-2605-16508 | complete |
| SF-2026-ARXIV-2605-16565 | RP-aeb46f2dd2ff9fac | deep | arXiv:2605.16565v1 | SRC-ARXIV@arXiv:2605.16565v1 | arXiv:2605.16565v1 — Methodology: 3 Design of Accio (official v1 HTML) | arXiv:2605.16565v1 — Experiments: 5 Evaluation (official v1 HTML) | arXiv:2605.16565v1 — Scope and limitations: 3.4 Query Support and Deployment Discussion (official v1 HTML) | webcache-2605.16565.txt#sha256=749fd52ff1227a02d1f3109cf1f1c74f239c4e7f1a8f972542d207db7b155be7; immutable artifact commit Not Disclosed | claim:SF-2026-ARXIV-2605-16565 | complete |
| SF-2026-ARXIV-2605-16604 | RP-763c2be77c02528f | deep | arXiv:2605.16604v1 | SRC-ARXIV@arXiv:2605.16604v1 | arXiv:2605.16604v1 — Methodology: §4 Risk-Calibrated Routing and Verifier Distillation (official v1 HTML) | arXiv:2605.16604v1 — Experiments: §5 Experiments (official v1 HTML) | arXiv:2605.16604v1 — Scope and limitations: §6 Conclusion; no dedicated limitations heading (official v1 HTML) | webcache-2605.16604.txt#sha256=e7e2e1d01b7d84c0a6f1394da6cd989478df4b8cc2d745e7be689863a92501b2; immutable artifact commit Not Disclosed | claim:SF-2026-ARXIV-2605-16604 | complete |
| SF-2026-ARXIV-2605-16616 | RP-0d1c3d7af26d1213 | deep | arXiv:2605.16616v1 | SRC-ARXIV@arXiv:2605.16616v1 | arXiv:2605.16616v1 — Methodology: §§1–2 task construction and system adaptation (official v1 HTML) | arXiv:2605.16616v1 — Experiments: §3 Evaluation and Results (official v1 HTML) | arXiv:2605.16616v1 — Scope and limitations: §5 Limitations and Future Work (official v1 HTML) | webcache-2605.16616.txt#sha256=c0a72e5742092c9492dbaa71d64cb07d704223b616acc543aa2363c4997d5809; immutable artifact commit Not Disclosed | claim:SF-2026-ARXIV-2605-16616 | complete |
| SF-2026-ARXIV-2605-16626 | RP-263294b76c909a3d | deep | arXiv:2605.16626v1 | SRC-ARXIV@arXiv:2605.16626v1 | arXiv:2605.16626v1 — Methodology: §§2–3 transcript properties and dataset construction (official v1 HTML) | arXiv:2605.16626v1 — Experiments: §§4–5 experimental setup and results (official v1 HTML) | arXiv:2605.16626v1 — Scope and limitations: §7 Limitations (official v1 HTML) | webcache-2605.16626.txt#sha256=465e98114176c28f000806fbafa0b48f6d672a5854ab48108145051eea62fa4e; immutable artifact commit Not Disclosed | claim:SF-2026-ARXIV-2605-16626 | complete |
| SF-2026-ARXIV-2605-16630 | RP-2a83278de07df629 | deep | arXiv:2605.16630v1 | SRC-ARXIV@arXiv:2605.16630v1 | arXiv:2605.16630v1 — Methodology: §IV PrivScope (official v1 HTML) | arXiv:2605.16630v1 — Experiments: §V Evaluation (official v1 HTML) | arXiv:2605.16630v1 — Scope and limitations: §VI Conclusion; no dedicated limitations heading (official v1 HTML) | webcache-2605.16630.txt#sha256=56c1c857f912333329967801104ef738a70e38f93a0d8c87163eb2bb8f99b4b5; immutable artifact commit Not Disclosed | claim:SF-2026-ARXIV-2605-16630 | complete |
| SF-2026-ARXIV-2605-16637 | RP-fc9ee7edd29fb7df | deep | arXiv:2605.16637v1 | SRC-ARXIV@arXiv:2605.16637v1 | arXiv:2605.16637v1 — Methodology: 4 System Overview (official v1 HTML) | arXiv:2605.16637v1 — Experiments: 7 Evaluation (official v1 HTML) | arXiv:2605.16637v1 — Scope and limitations: 8 Conclusion (official v1 HTML) | webcache-2605.16637.txt#sha256=d03192deedf6deb9395ab2d886fc59b485cd24ac37b850266e0a45994200017a; immutable artifact commit Not Disclosed | claim:SF-2026-ARXIV-2605-16637 | complete |
| SF-2026-ARXIV-2605-16650 | RP-5d8fde7e5a819bdb | deep | arXiv:2605.16650v1 | SRC-ARXIV@arXiv:2605.16650v1 | arXiv:2605.16650v1 — Methodology: §4 SKG-Eval (official v1 HTML) | arXiv:2605.16650v1 — Experiments: §5 Experiments (official v1 HTML) | arXiv:2605.16650v1 — Scope and limitations: §5.10 Discussion and Limitations (official v1 HTML) | webcache-2605.16650.txt#sha256=40ceb2fc836a6684a5eca1aabf7338682f805ff7a8c7ff0277e17cc64a5c873f; immutable artifact commit Not Disclosed | claim:SF-2026-ARXIV-2605-16650 | complete |
| SF-2026-ARXIV-2605-16704 | RP-719bb53b825db5ae | deep | arXiv:2605.16704v1 | SRC-ARXIV@arXiv:2605.16704v1 | arXiv:2605.16704v1 — Methodology: §3 Dataset-Valuation Methodology (official v1 HTML) | arXiv:2605.16704v1 — Experiments: §§3.3–4 analysis and experiments (official v1 HTML) | arXiv:2605.16704v1 — Scope and limitations: §3.1 Limitations (official v1 HTML) | webcache-2605.16704.txt#sha256=0a97ecd00b9c5b62ea2f1d87d3da95d94152af3324e7c0d86b1a30cf80cca085; immutable artifact commit Not Disclosed | claim:SF-2026-ARXIV-2605-16704 | complete |
| SF-2026-ARXIV-2605-16712 | RP-adfb1782e3b9383c | deep | arXiv:2605.16712v1 | SRC-ARXIV@arXiv:2605.16712v1 | arXiv:2605.16712v1 — Methodology: 4 CBEA and LCV Runtime Algorithm (official v1 HTML) | arXiv:2605.16712v1 — Experiments: 5 Evaluation and Benchmark Protocol (official v1 HTML) | arXiv:2605.16712v1 — Scope and limitations: 8 Discussion (official v1 HTML) | webcache-2605.16712.txt#sha256=5e12847eb7b6f0621c02e22251d8c88d56809e076ba6510b7fd909dc7aa0669f; immutable artifact commit Not Disclosed | claim:SF-2026-ARXIV-2605-16712 | complete |
| SF-2026-ARXIV-2605-16725 | RP-9749af8e1b72dd9a | deep | arXiv:2605.16725v1 | SRC-ARXIV@arXiv:2605.16725v1 | arXiv:2605.16725v1 — Methodology: 4 Method (official v1 HTML) | arXiv:2605.16725v1 — Experiments: 5 Experiments (official v1 HTML) | arXiv:2605.16725v1 — Scope and limitations: 6 Conclusion (official v1 HTML) | webcache-2605.16725.txt#sha256=9ba8ecf683874b192a5c8c08a729807dc6e8edc6b576f436291147b3a8e4e8fe; immutable artifact commit Not Disclosed | claim:SF-2026-ARXIV-2605-16725 | complete |
| SF-2026-ARXIV-2605-16745 | RP-caaacf30319f358f | deep | arXiv:2605.16745v1 | SRC-ARXIV@arXiv:2605.16745v1 | section 3 Methodology (§3 Methodology) | section 4 Experiments (§4 Experiments) | section 5 Limitations, Discussion & Future Work (§5 Limitations, Discussion & Future Work) | papers/2026/05/_sources/daily-20260517/exact-review-batch-a.txt#sha256=fda592ed66575885cf93f3cc29fe3f7c8802a92d00a4d1fe00e5dd330dd643dd; exact-v1 URL=https://arxiv.org/html/2605.16745v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-16745 | complete |
| SF-2026-ARXIV-2605-16746 | RP-4a1e2cb899b43642 | deep | arXiv:2605.16746v1 | SRC-ARXIV@arXiv:2605.16746v1 | section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt) | Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only | Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup | papers/2026/05/_sources/daily-20260517/exact-review-batch-a.txt#sha256=fda592ed66575885cf93f3cc29fe3f7c8802a92d00a4d1fe00e5dd330dd643dd; exact-v1 URL=https://arxiv.org/html/2605.16746v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-16746 | complete |
| SF-2026-ARXIV-2605-16776 | RP-959f6f263ab46b7f | deep | arXiv:2605.16776v1 | SRC-ARXIV@arXiv:2605.16776v1 | section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt) | Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only | Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup | papers/2026/05/_sources/daily-20260517/exact-review-batch-a.txt#sha256=fda592ed66575885cf93f3cc29fe3f7c8802a92d00a4d1fe00e5dd330dd643dd; exact-v1 URL=https://arxiv.org/html/2605.16776v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-16776 | complete |
| SF-2026-ARXIV-2605-16786 | RP-7ebf4d25fba06fb7 | deep | arXiv:2605.16786v1 | SRC-ARXIV@arXiv:2605.16786v1 | section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt) | Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only | Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup | papers/2026/05/_sources/daily-20260517/exact-review-batch-a.txt#sha256=fda592ed66575885cf93f3cc29fe3f7c8802a92d00a4d1fe00e5dd330dd643dd; exact-v1 URL=https://arxiv.org/html/2605.16786v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-16786 | complete |
| SF-2026-ARXIV-2605-16787 | RP-2d1b9dca058f5f5f | deep | arXiv:2605.16787v1 | SRC-ARXIV@arXiv:2605.16787v1 | section 3.1 Training Algorithm (§3.1 Training Algorithm) | Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only | section 6 Discussion (§6 Discussion) | papers/2026/05/_sources/daily-20260517/exact-review-batch-b.txt#sha256=eb58ffa1e2bcd09fef6dabba79bb00e3b905ace87854841ba755cb8c7fd8a451; exact-v1 URL=https://arxiv.org/html/2605.16787v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-16787 | complete |
| SF-2026-ARXIV-2605-16790 | RP-97bef451871e263a | deep | arXiv:2605.16790v1 | SRC-ARXIV@arXiv:2605.16790v1 | section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt) | Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only | Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup | papers/2026/05/_sources/daily-20260517/exact-review-batch-b.txt#sha256=eb58ffa1e2bcd09fef6dabba79bb00e3b905ace87854841ba755cb8c7fd8a451; exact-v1 URL=https://arxiv.org/html/2605.16790v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-16790 | complete |
| SF-2026-ARXIV-2605-16819 | RP-0b8a7c8bc47aa6b1 | deep | arXiv:2605.16819v1 | SRC-ARXIV@arXiv:2605.16819v1 | section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt) | Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only | Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup | papers/2026/05/_sources/daily-20260517/exact-review-batch-b.txt#sha256=eb58ffa1e2bcd09fef6dabba79bb00e3b905ace87854841ba755cb8c7fd8a451; exact-v1 URL=https://arxiv.org/html/2605.16819v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-16819 | complete |
| SF-2026-ARXIV-2605-16826 | RP-b06546f2fbed19cd | deep | arXiv:2605.16826v1 | SRC-ARXIV@arXiv:2605.16826v1 | section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt) | Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only | Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup | papers/2026/05/_sources/daily-20260517/exact-review-batch-b.txt#sha256=eb58ffa1e2bcd09fef6dabba79bb00e3b905ace87854841ba755cb8c7fd8a451; exact-v1 URL=https://arxiv.org/html/2605.16826v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-16826 | complete |
| SF-2026-ARXIV-2605-16839 | RP-ac62ed41b98b7afc | deep | arXiv:2605.16839v1 | SRC-ARXIV@arXiv:2605.16839v1 | section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt) | Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only | Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup | papers/2026/05/_sources/daily-20260517/exact-review-batch-b.txt#sha256=eb58ffa1e2bcd09fef6dabba79bb00e3b905ace87854841ba755cb8c7fd8a451; exact-v1 URL=https://arxiv.org/html/2605.16839v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-16839 | complete |
| SF-2026-ARXIV-2605-16867 | RP-303011d3db920e33 | deep | arXiv:2605.16867v1 | SRC-ARXIV@arXiv:2605.16867v1 | section 2.2 Lessons Learned from Existing Request-routing Methods (§2.2 Lessons Learned from Existing Request-routing Methods) | section 4 Evaluation (§4 Evaluation) | section 5 Additional Related Works and Discussions (§5 Additional Related Works and Discussions) | papers/2026/05/_sources/daily-20260517/exact-review-recovered-fn-a.txt#sha256=7b72732f912c05fa82020ab8fd5844841dbb8853ad1cd73ed33a25196f89b2ad; exact-v1 URL=https://arxiv.org/html/2605.16867v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-16867 | complete |
| SF-2026-ARXIV-2605-16928 | RP-9b7a81b68e3f74bf | deep | arXiv:2605.16928v1 | SRC-ARXIV@arXiv:2605.16928v1 | section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt) | Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only | Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup | papers/2026/05/_sources/daily-20260517/exact-review-batch-c.txt#sha256=8b5717c9d592f72ad26704544e5b47d6c7879fdc93db6f85c974d37313c58e3b; exact-v1 URL=https://arxiv.org/html/2605.16928v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-16928 | complete |
| SF-2026-ARXIV-2605-16976 | RP-eb1ef580e1a1784f | deep | arXiv:2605.16976v1 | SRC-ARXIV@arXiv:2605.16976v1 | section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt) | Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only | Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup | papers/2026/05/_sources/daily-20260517/exact-review-recovered-fn-a.txt#sha256=7b72732f912c05fa82020ab8fd5844841dbb8853ad1cd73ed33a25196f89b2ad; exact-v1 URL=https://arxiv.org/html/2605.16976v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-16976 | complete |
| SF-2026-ARXIV-2605-16986 | RP-6d4cfc5600612a37 | deep | arXiv:2605.16986v1 | SRC-ARXIV@arXiv:2605.16986v1 | section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt) | Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only | Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup | papers/2026/05/_sources/daily-20260517/exact-review-batch-c.txt#sha256=8b5717c9d592f72ad26704544e5b47d6c7879fdc93db6f85c974d37313c58e3b; exact-v1 URL=https://arxiv.org/html/2605.16986v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-16986 | complete |
| SF-2026-ARXIV-2605-17003 | RP-98a87e27fa4c55b2 | deep | arXiv:2605.17003v1 | SRC-ARXIV@arXiv:2605.17003v1 | section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt) | Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only | Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup | papers/2026/05/_sources/daily-20260517/exact-review-batch-c.txt#sha256=8b5717c9d592f72ad26704544e5b47d6c7879fdc93db6f85c974d37313c58e3b; exact-v1 URL=https://arxiv.org/html/2605.17003v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17003 | complete |
| SF-2026-ARXIV-2605-17026 | RP-386a2535f7264ddc | deep | arXiv:2605.17026v1 | SRC-ARXIV@arXiv:2605.17026v1 | section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt) | Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only | Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup | papers/2026/05/_sources/daily-20260517/exact-review-recovered-fn-a.txt#sha256=7b72732f912c05fa82020ab8fd5844841dbb8853ad1cd73ed33a25196f89b2ad; exact-v1 URL=https://arxiv.org/html/2605.17026v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17026 | complete |
| SF-2026-ARXIV-2605-17028 | RP-a8b29f495e52e5ce | deep | arXiv:2605.17028v1 | SRC-ARXIV@arXiv:2605.17028v1 | section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt) | Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only | Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup | papers/2026/05/_sources/daily-20260517/exact-review-recovered-fn-a.txt#sha256=7b72732f912c05fa82020ab8fd5844841dbb8853ad1cd73ed33a25196f89b2ad; exact-v1 URL=https://arxiv.org/html/2605.17028v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17028 | complete |
| SF-2026-ARXIV-2605-17034 | RP-398f1df1a9297040 | deep | arXiv:2605.17034v1 | SRC-ARXIV@arXiv:2605.17034v1 | section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt) | Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only | Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup | papers/2026/05/_sources/daily-20260517/exact-review-batch-c.txt#sha256=8b5717c9d592f72ad26704544e5b47d6c7879fdc93db6f85c974d37313c58e3b; exact-v1 URL=https://arxiv.org/html/2605.17034v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17034 | complete |
| SF-2026-ARXIV-2605-17062 | RP-7ef1ca7efc7efd89 | deep | arXiv:2605.17062v1 | SRC-ARXIV@arXiv:2605.17062v1 | section 4 Replication Methodology (§4 Replication Methodology) | section 5 Results (§5 model/package-registry comparisons) | section 8 Limitations (§8 Limitations) | papers/2026/05/_sources/daily-20260517/exact-review-special-pdf.txt#sha256=d44a0fff9094a693d0b4d4ca20ae4fbaa15571a84bcba5325ed128901794785c; exact-v1 URL=https://arxiv.org/pdf/2605.17062v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17062 | complete |
| SF-2026-ARXIV-2605-17076 | RP-f7e0b7f865c61fdf | deep | arXiv:2605.17076v1 | SRC-ARXIV@arXiv:2605.17076v1 | section VII-M (§VII-M) | Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only | Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup | papers/2026/05/_sources/daily-20260517/exact-body-batch-d.txt#sha256=ce6510fdc372a9699218a35e347a34f369b7c0ee1bcb22ec1f2fc1c2e690f8ea; exact-v1 URL=https://arxiv.org/html/2605.17076v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17076 | complete |
| SF-2026-ARXIV-2605-17106 | RP-6863f87e5802d9f6 | deep | arXiv:2605.17106v1 | SRC-ARXIV@arXiv:2605.17106v1 | section 8 (§8) | Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only | Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup | papers/2026/05/_sources/daily-20260517/exact-body-batch-d.txt#sha256=ce6510fdc372a9699218a35e347a34f369b7c0ee1bcb22ec1f2fc1c2e690f8ea; exact-v1 URL=https://arxiv.org/html/2605.17106v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17106 | complete |
| SF-2026-ARXIV-2605-17113 | RP-cb2bf52607e9ac80 | deep | arXiv:2605.17113v1 | SRC-ARXIV@arXiv:2605.17113v1 | section 3 Methods (§3 Methods) | section 5 Experiments (§5 Experiments) | section 7 Discussion and Limitations (§7 Discussion and Limitations) | papers/2026/05/_sources/daily-20260517/exact-review-recovered-fn-b.txt#sha256=8ae46ad2a45287bcf09ba2b87d92d4d5896edd06f67f8df4a568ef5e394eb200; exact-v1 URL=https://arxiv.org/html/2605.17113v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17113 | complete |
| SF-2026-ARXIV-2605-17160 | RP-8038db9b156724af | deep | arXiv:2605.17160v1 | SRC-ARXIV@arXiv:2605.17160v1 | section 3 Counterfactual-Faithful Quantization (§3 CFQ) | section 4 Experiments (§4 ADULT, GERMAN CREDIT and COMPAS) | section 6 Limitations (§6 validity boundary) | papers/2026/05/_sources/daily-20260517/exact-review-2605.17160-pdf.txt#sha256=55f65685ab8b08614797164881d4e28f2b4007eba4a985a3a30ef874cea4b066; exact-v1 URL=https://arxiv.org/pdf/2605.17160v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17160 | complete |
| SF-2026-ARXIV-2605-17164 | RP-7663776eb172f83f | deep | arXiv:2605.17164v1 | SRC-ARXIV@arXiv:2605.17164v1 | section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt) | Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only | Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup | papers/2026/05/_sources/daily-20260517/exact-body-batch-d.txt#sha256=ce6510fdc372a9699218a35e347a34f369b7c0ee1bcb22ec1f2fc1c2e690f8ea; exact-v1 URL=https://arxiv.org/html/2605.17164v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17164 | complete |
| SF-2026-ARXIV-2605-17169 | RP-5e64034cdd32220f | deep | arXiv:2605.17169v1 | SRC-ARXIV@arXiv:2605.17169v1 | section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt) | Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only | Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup | papers/2026/05/_sources/daily-20260517/exact-review-recovered-fn-b.txt#sha256=8ae46ad2a45287bcf09ba2b87d92d4d5896edd06f67f8df4a568ef5e394eb200; exact-v1 URL=https://arxiv.org/html/2605.17169v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17169 | complete |
| SF-2026-ARXIV-2605-17170 | RP-362f0afd90fd5a64 | deep | arXiv:2605.17170v1 | SRC-ARXIV@arXiv:2605.17170v1 | section 49 (§49) | Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only | Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup | papers/2026/05/_sources/daily-20260517/exact-body-batch-d.txt#sha256=ce6510fdc372a9699218a35e347a34f369b7c0ee1bcb22ec1f2fc1c2e690f8ea; exact-v1 URL=https://arxiv.org/html/2605.17170v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17170 | complete |
| SF-2026-ARXIV-2605-17172 | RP-ba56c05060be31f5 | deep | arXiv:2605.17172v1 | SRC-ARXIV@arXiv:2605.17172v1 | section 3 Methods (§3 Methods) | section 3.2 Evaluation Metrics (§3.2 Evaluation Metrics) | section 5 Discussion and Conclusion (§5 Discussion and Conclusion) | papers/2026/05/_sources/daily-20260517/exact-review-batch-e.txt#sha256=9abdfb74430dcb68b786da23298e7b85d4ec789284d97e023fbe7f83a4d9208f; exact-v1 URL=https://arxiv.org/html/2605.17172v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17172 | complete |
| SF-2026-ARXIV-2605-17173 | RP-fad7ce5bd68b8c63 | deep | arXiv:2605.17173v1 | SRC-ARXIV@arXiv:2605.17173v1 | section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt) | Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only | Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup | papers/2026/05/_sources/daily-20260517/exact-review-batch-e.txt#sha256=9abdfb74430dcb68b786da23298e7b85d4ec789284d97e023fbe7f83a4d9208f; exact-v1 URL=https://arxiv.org/html/2605.17173v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17173 | complete |
| SF-2026-ARXIV-2605-17193 | RP-9ec4fa2ed0748ca9 | deep | arXiv:2605.17193v1 | SRC-ARXIV@arXiv:2605.17193v1 | PDF section Methods; Supplementary Note 1 §§1.1–1.8; Supplementary Notes 2–3 intervention definitions | PDF section Results: Semantic Collapse in Extended Open-Ended Simulations; Semantic Collapse Resists Intervention; Diagnosing Mechanisms of Semantic Collapse; Supplementary Note 3 §3.7 | PDF section Discussion; Supplementary Note 3 §3.7 non-causal regression boundary; Supplementary Note 5 heuristic-theory and predictive-regularity boundaries | official exact-v1 PDF=https://arxiv.org/pdf/2605.17193v1; bytes=4076663; sha256=edde49ce22de86ac25ad4d676f9003afec5c11513bee35438ca8db965322abe7; immutable code/data commit Not Disclosed | claim:SF-2026-ARXIV-2605-17193 | complete |
| SF-2026-ARXIV-2605-17222 | RP-2def8a53e65eb02b | deep | arXiv:2605.17222v1 | SRC-ARXIV@arXiv:2605.17222v1 | arXiv:2605.17222v1 — §II-B BSGS Algorithm for HE-LT (frozen exact-v1 official HTML receipt) | arXiv:2605.17222v1 — §VI Experimental Results and Comparisons (frozen exact-v1 official HTML receipt) | Not Disclosed — no dedicated limitations heading; claim remains bounded to disclosed setup | papers/2026/05/_sources/daily-20260518/exact-review-batch-a.txt#sha256=f5074c159bee3cbb728f67926c05f4e6ef651304d936baea943e38a9e4ffabeb; exact-v1 URL=https://arxiv.org/html/2605.17222v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17222 | complete |
| SF-2026-ARXIV-2605-17234 | RP-d0a4bdd64998e0c6 | deep | arXiv:2605.17234v1 | SRC-ARXIV@arXiv:2605.17234v1 | arXiv:2605.17234v1 — §1 Introduction (frozen exact-v1 official HTML receipt) | arXiv:2605.17234v1 — §4 Experiments (frozen exact-v1 official HTML receipt) | Not Disclosed — no dedicated limitations heading; claim remains bounded to disclosed setup | papers/2026/05/_sources/daily-20260518/exact-review-batch-a.txt#sha256=f5074c159bee3cbb728f67926c05f4e6ef651304d936baea943e38a9e4ffabeb; exact-v1 URL=https://arxiv.org/html/2605.17234v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17234 | complete |
| SF-2026-ARXIV-2605-17242 | RP-7407c464354ff140 | deep | arXiv:2605.17242v1 | SRC-ARXIV@arXiv:2605.17242v1 | arXiv:2605.17242v1 — §3 Methodology (§3.1–§3.4) (official exact-v1 HTML) | arXiv:2605.17242v1 — §4 Experimental Setup; §5 Results (official exact-v1 HTML) | arXiv:2605.17242v1 — §6.4 Threats to Validity (official exact-v1 HTML) | exact-v1 URL=https://arxiv.org/html/2605.17242v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17242 | complete |
| SF-2026-ARXIV-2605-17246 | RP-42c4c7936b115319 | deep | arXiv:2605.17246v1 | SRC-ARXIV@arXiv:2605.17246v1 | arXiv:2605.17246v1 — §3 The Behavioural Alignment Framework (frozen exact-v1 official HTML receipt) | arXiv:2605.17246v1 — §5 Empirical Evaluation on CardDemo (frozen exact-v1 official HTML receipt) | arXiv:2605.17246v1 — §6 Discussion and limitations (frozen exact-v1 official HTML receipt) | papers/2026/05/_sources/daily-20260518/exact-review-batch-a.txt#sha256=f5074c159bee3cbb728f67926c05f4e6ef651304d936baea943e38a9e4ffabeb; exact-v1 URL=https://arxiv.org/html/2605.17246v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17246 | complete |
| SF-2026-ARXIV-2605-17260 | RP-e0ee173099242c7b | deep | arXiv:2605.17260v1 | SRC-ARXIV@arXiv:2605.17260v1 | arXiv:2605.17260v1 — §4.1 Architecture: Spatio-temporal Token Compressive Encoding (frozen exact-v1 official HTML receipt) | arXiv:2605.17260v1 — §5 Experiments (frozen exact-v1 official HTML receipt) | Not Disclosed — no dedicated limitations heading; claim remains bounded to disclosed setup | papers/2026/05/_sources/daily-20260518/exact-review-batch-a.txt#sha256=f5074c159bee3cbb728f67926c05f4e6ef651304d936baea943e38a9e4ffabeb; exact-v1 URL=https://arxiv.org/html/2605.17260v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17260 | complete |
| SF-2026-ARXIV-2605-17268 | RP-9e5be2bb668ee336 | deep | arXiv:2605.17268v1 | SRC-ARXIV@arXiv:2605.17268v1 | arXiv:2605.17268v1 — §4 Methodology (frozen exact-v1 official HTML receipt) | arXiv:2605.17268v1 — §5 Results (frozen exact-v1 official HTML receipt) | Not Disclosed — no dedicated limitations heading; claim remains bounded to disclosed setup | papers/2026/05/_sources/daily-20260518/exact-review-batch-b.txt#sha256=0e855f40ad6257ba4a7e7c30bfbc192a95d80b5cda955f812a4716ed51dfc56e; exact-v1 URL=https://arxiv.org/html/2605.17268v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17268 | complete |
| SF-2026-ARXIV-2605-17273 | RP-0e9c0f295ed9bcc7 | deep | arXiv:2605.17273v1 | SRC-ARXIV@arXiv:2605.17273v1 | arXiv:2605.17273v1 — §2.1 Statistical Comparison Methods (frozen exact-v1 official HTML receipt) | arXiv:2605.17273v1 — §4.1 Case Analysis: HELM MMLU (frozen exact-v1 official HTML receipt) | Not Disclosed — no dedicated limitations heading; claim remains bounded to disclosed setup | papers/2026/05/_sources/daily-20260518/exact-review-batch-b.txt#sha256=0e855f40ad6257ba4a7e7c30bfbc192a95d80b5cda955f812a4716ed51dfc56e; exact-v1 URL=https://arxiv.org/html/2605.17273v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17273 | complete |
| SF-2026-ARXIV-2605-17281 | RP-4b09b99c431cf845 | deep | arXiv:2605.17281v1 | SRC-ARXIV@arXiv:2605.17281v1 | arXiv:2605.17281v1 — §1 Introduction (frozen exact-v1 official HTML receipt) | arXiv:2605.17281v1 — §3.2 Evaluation Protocol (frozen exact-v1 official HTML receipt) | Not Disclosed — no dedicated limitations heading; claim remains bounded to disclosed setup | papers/2026/05/_sources/daily-20260518/exact-review-batch-b.txt#sha256=0e855f40ad6257ba4a7e7c30bfbc192a95d80b5cda955f812a4716ed51dfc56e; exact-v1 URL=https://arxiv.org/html/2605.17281v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17281 | complete |
| SF-2026-ARXIV-2605-17288 | RP-49ea30f3df91eee1 | deep | arXiv:2605.17288v1 | SRC-ARXIV@arXiv:2605.17288v1 | arXiv:2605.17288v1 — §3.2 System Model (frozen exact-v1 official HTML receipt) | arXiv:2605.17288v1 — §6 Experiment (frozen exact-v1 official HTML receipt) | arXiv:2605.17288v1 — §7 Discussion (frozen exact-v1 official HTML receipt) | papers/2026/05/_sources/daily-20260518/exact-review-batch-b.txt#sha256=0e855f40ad6257ba4a7e7c30bfbc192a95d80b5cda955f812a4716ed51dfc56e; exact-v1 URL=https://arxiv.org/html/2605.17288v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17288 | complete |
| SF-2026-ARXIV-2605-17289 | RP-dd9f7024fd489d32 | deep | arXiv:2605.17289v1 | SRC-ARXIV@arXiv:2605.17289v1 | arXiv:2605.17289v1 — §3 LEAP: Method (frozen exact-v1 official HTML receipt) | arXiv:2605.17289v1 — §4 Experiments (frozen exact-v1 official HTML receipt) | arXiv:2605.17289v1 — §5 Discussion and Limitations (frozen exact-v1 official HTML receipt) | papers/2026/05/_sources/daily-20260518/exact-review-batch-c.txt#sha256=5266e2523e5fbffa0991a5fdfcb698f84c0fca6f4509734861dea2378293b440; exact-v1 URL=https://arxiv.org/html/2605.17289v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17289 | complete |
| SF-2026-ARXIV-2605-17291 | RP-116f75c7a0506fff | deep | arXiv:2605.17291v1 | SRC-ARXIV@arXiv:2605.17291v1 | arXiv:2605.17291v1 — §3 Method (frozen exact-v1 official HTML receipt) | arXiv:2605.17291v1 — §2.2 Rubric-Based Evaluation and Rewards (frozen exact-v1 official HTML receipt) | arXiv:2605.17291v1 — §6 Limitations (frozen exact-v1 official HTML receipt) | papers/2026/05/_sources/daily-20260518/exact-review-batch-c.txt#sha256=5266e2523e5fbffa0991a5fdfcb698f84c0fca6f4509734861dea2378293b440; exact-v1 URL=https://arxiv.org/html/2605.17291v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17291 | complete |
| SF-2026-ARXIV-2605-17292 | RP-fb7a352115fdd929 | deep | arXiv:2605.17292v1 | SRC-ARXIV@arXiv:2605.17292v1 | arXiv:2605.17292v1 — §III MetaCogAgent Framework (§III-B–§III-D) (official exact-v1 HTML) | arXiv:2605.17292v1 — §V Experiments (official exact-v1 HTML) | arXiv:2605.17292v1 — §VI Discussion; no dedicated limitations section (official exact-v1 HTML) | exact-v1 URL=https://arxiv.org/html/2605.17292v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17292 | complete |
| SF-2026-ARXIV-2605-17301 | RP-300748087f71a17d | deep | arXiv:2605.17301v1 | SRC-ARXIV@arXiv:2605.17301v1 | arXiv:2605.17301v1 — §III Methodology (frozen exact-v1 official HTML receipt) | arXiv:2605.17301v1 — §IV Experimental Setup (frozen exact-v1 official HTML receipt) | arXiv:2605.17301v1 — §V-G Limitations (frozen exact-v1 official HTML receipt) | papers/2026/05/_sources/daily-20260518/exact-review-batch-c.txt#sha256=5266e2523e5fbffa0991a5fdfcb698f84c0fca6f4509734861dea2378293b440; exact-v1 URL=https://arxiv.org/html/2605.17301v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17301 | complete |
| SF-2026-ARXIV-2605-17304 | RP-129af85d7881f49c | deep | arXiv:2605.17304v1 | SRC-ARXIV@arXiv:2605.17304v1 | arXiv:2605.17304v1 — §3 Problem Formulation (frozen exact-v1 official HTML receipt) | Not Disclosed — no dedicated evaluation heading in the frozen exact-v1 receipt | Not Disclosed — no dedicated limitations heading; claim remains bounded to disclosed setup | papers/2026/05/_sources/daily-20260518/exact-review-batch-c.txt#sha256=5266e2523e5fbffa0991a5fdfcb698f84c0fca6f4509734861dea2378293b440; exact-v1 URL=https://arxiv.org/html/2605.17304v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17304 | complete |
| SF-2026-ARXIV-2605-17305 | RP-69003ea762f0c911 | deep | arXiv:2605.17305v1 | SRC-ARXIV@arXiv:2605.17305v1 | arXiv:2605.17305v1 — §III CyberCorrect Framework (§III-B–§III-D) (official exact-v1 HTML) | arXiv:2605.17305v1 — §V Experiments (official exact-v1 HTML) | arXiv:2605.17305v1 — §VI Discussion; no dedicated limitations section (official exact-v1 HTML) | exact-v1 URL=https://arxiv.org/html/2605.17305v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17305 | complete |
| SF-2026-ARXIV-2605-17320 | RP-d50b23a3e16d22b5 | deep | arXiv:2605.17320v1 | SRC-ARXIV@arXiv:2605.17320v1 | arXiv:2605.17320v1 — §4 TClone Design (frozen exact-v1 official HTML receipt) | arXiv:2605.17320v1 — §5 Evaluation (frozen exact-v1 official HTML receipt) | arXiv:2605.17320v1 — §2.3 Limitations of Existing Solutions (frozen exact-v1 official HTML receipt) | papers/2026/05/_sources/daily-20260518/exact-review-batch-d.txt#sha256=420494531f6942665b1f3de8dd395e22d8d5ba1f4d5a8f68eaaabc8e364847fe; exact-v1 URL=https://arxiv.org/html/2605.17320v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17320 | complete |
| SF-2026-ARXIV-2605-17324 | RP-7b6430846ac5a3dc | deep | arXiv:2605.17324v1 | SRC-ARXIV@arXiv:2605.17324v1 | arXiv:2605.17324v1 — §5.1 Evaluation Design (frozen exact-v1 official HTML receipt) | arXiv:2605.17324v1 — §5 Evaluation (frozen exact-v1 official HTML receipt) | arXiv:2605.17324v1 — §7 Discussion (frozen exact-v1 official HTML receipt) | papers/2026/05/_sources/daily-20260518/exact-review-batch-d.txt#sha256=420494531f6942665b1f3de8dd395e22d8d5ba1f4d5a8f68eaaabc8e364847fe; exact-v1 URL=https://arxiv.org/html/2605.17324v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17324 | complete |
| SF-2026-ARXIV-2605-17329 | RP-8d1934bd28977f9c | deep | arXiv:2605.17329v1 | SRC-ARXIV@arXiv:2605.17329v1 | arXiv:2605.17329v1 — §4 Method (§4.2–§4.6) (official exact-v1 HTML) | arXiv:2605.17329v1 — §5 Main Results; §6 Ablation (official exact-v1 HTML) | arXiv:2605.17329v1 — Appendix D Limitations and Broader Impacts (official exact-v1 HTML) | exact-v1 URL=https://arxiv.org/html/2605.17329v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17329 | complete |
| SF-2026-ARXIV-2605-17348 | RP-de1353951694879a | deep | arXiv:2605.17348v1 | SRC-ARXIV@arXiv:2605.17348v1 | arXiv:2605.17348v1 — §4 Methodology (§4.2–§4.3) (official exact-v1 HTML) | arXiv:2605.17348v1 — §5 Experiments (official exact-v1 HTML) | arXiv:2605.17348v1 — §6 Conclusion and robustness appendix; no dedicated limitations section (official exact-v1 HTML) | exact-v1 URL=https://arxiv.org/html/2605.17348v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17348 | complete |
| SF-2026-ARXIV-2605-17360 | RP-aecc7d038ca36b79 | deep | arXiv:2605.17360v1 | SRC-ARXIV@arXiv:2605.17360v1 | arXiv:2605.17360v1 — §3 Omni-DuplexEval (§3.2–§3.3) (official exact-v1 HTML) | arXiv:2605.17360v1 — §4 Experiments (official exact-v1 HTML) | arXiv:2605.17360v1 — Appendix D Limitations (official exact-v1 HTML) | exact-v1 URL=https://arxiv.org/html/2605.17360v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17360 | complete |
| SF-2026-ARXIV-2605-17373 | RP-49302d50a914dfa1 | deep | arXiv:2605.17373v1 | SRC-ARXIV@arXiv:2605.17373v1 | arXiv:2605.17373v1 — §3 FML-bench (§3.2–§3.4) (official exact-v1 HTML) | arXiv:2605.17373v1 — §4 Experiments; §5 Search-dynamics analysis (official exact-v1 HTML) | arXiv:2605.17373v1 — Appendix N Broader impacts; no dedicated limitations section (official exact-v1 HTML) | exact-v1 URL=https://arxiv.org/html/2605.17373v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17373 | complete |
| SF-2026-ARXIV-2605-17380 | RP-4579206d5622b075 | deep | arXiv:2605.17380v1 | SRC-ARXIV@arXiv:2605.17380v1 | arXiv:2605.17380v1 — §3 ADR System Design (§3.1–§3.2) (official exact-v1 HTML) | arXiv:2605.17380v1 — §5 Evaluation; §6 Real-World Deployment (official exact-v1 HTML) | arXiv:2605.17380v1 — §7 Discussion; no dedicated limitations section (official exact-v1 HTML) | exact-v1 URL=https://arxiv.org/html/2605.17380v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17380 | complete |
| SF-2026-ARXIV-2605-17415 | RP-392968683dd732a5 | deep | arXiv:2605.17415v1 | SRC-ARXIV@arXiv:2605.17415v1 | arXiv:2605.17415v1 — §3 IVF-TQ (§3.1–§3.3) (official exact-v1 HTML) | arXiv:2605.17415v1 — §4 Streaming Experiments; §5 Million-Scale Evaluation (official exact-v1 HTML) | arXiv:2605.17415v1 — §7 Limitations (official exact-v1 HTML) | exact-v1 URL=https://arxiv.org/html/2605.17415v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17415 | complete |
| SF-2026-ARXIV-2605-17439 | RP-74eebdfcbfd4cd12 | deep | arXiv:2605.17439v1 | SRC-ARXIV@arXiv:2605.17439v1 | arXiv:2605.17439v1 — §4 DiagEval (§4.1–§4.4) (official exact-v1 HTML) | arXiv:2605.17439v1 — §5 Experiments (official exact-v1 HTML) | arXiv:2605.17439v1 — §6 Limitations (official exact-v1 HTML) | exact-v1 URL=https://arxiv.org/html/2605.17439v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17439 | complete |
| SF-2026-ARXIV-2605-17453 | RP-2957f8febb15b9b1 | deep | arXiv:2605.17453v1 | SRC-ARXIV@arXiv:2605.17453v1 | arXiv:2605.17453v1 — §3 Method: VISTA-Guard under Untrusted Tool Feedback (frozen exact-v1 official HTML receipt) | arXiv:2605.17453v1 — §2 Threat Model, Benchmark, and Evaluation Lens (frozen exact-v1 official HTML receipt) | arXiv:2605.17453v1 — §5 Discussion (frozen exact-v1 official HTML receipt) | papers/2026/05/_sources/daily-20260518/exact-review-batch-d.txt#sha256=420494531f6942665b1f3de8dd395e22d8d5ba1f4d5a8f68eaaabc8e364847fe; exact-v1 URL=https://arxiv.org/html/2605.17453v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17453 | complete |
| SF-2026-ARXIV-2605-17467 | RP-d0c2dd1a542fab26 | deep | arXiv:2605.17467v1 | SRC-ARXIV@arXiv:2605.17467v1 | arXiv:2605.17467v1 — §3 VerifyMAS (§3.1–§3.2) (official exact-v1 HTML) | arXiv:2605.17467v1 — §4 Main Experiments (official exact-v1 HTML) | arXiv:2605.17467v1 — §5 Discussion; no dedicated limitations section (official exact-v1 HTML) | exact-v1 URL=https://arxiv.org/html/2605.17467v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17467 | complete |
| SF-2026-ARXIV-2605-17471 | RP-a4a77dd56fd5f14c | deep | arXiv:2605.17471v1 | SRC-ARXIV@arXiv:2605.17471v1 | arXiv:2605.17471v1 — §3 Our Approach (§3.1–§3.2) (official exact-v1 HTML) | arXiv:2605.17471v1 — §4 Experiments (official exact-v1 HTML) | arXiv:2605.17471v1 — §5 Conclusion; no dedicated limitations section (official exact-v1 HTML) | exact-v1 URL=https://arxiv.org/html/2605.17471v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17471 | complete |
| SF-2026-ARXIV-2605-17480 | RP-292df48dad510acb | deep | arXiv:2605.17480v1 | SRC-ARXIV@arXiv:2605.17480v1 | arXiv:2605.17480v1 — §3 Methodology (frozen exact-v1 official HTML receipt) | arXiv:2605.17480v1 — §4 Evaluation (frozen exact-v1 official HTML receipt) | arXiv:2605.17480v1 — §6 Limitations (frozen exact-v1 official HTML receipt) | papers/2026/05/_sources/daily-20260518/exact-review-batch-d.txt#sha256=420494531f6942665b1f3de8dd395e22d8d5ba1f4d5a8f68eaaabc8e364847fe; exact-v1 URL=https://arxiv.org/html/2605.17480v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17480 | complete |
| SF-2026-ARXIV-2605-17497 | RP-c90245d0a1481fe3 | deep | arXiv:2605.17497v1 | SRC-ARXIV@arXiv:2605.17497v1 | arXiv:2605.17497v1 — §3 Self-Supervised On-Policy Distillation (official exact-v1 HTML) | arXiv:2605.17497v1 — §4 Experiments (official exact-v1 HTML) | arXiv:2605.17497v1 — §5 Discussion; no dedicated limitations section (official exact-v1 HTML) | exact-v1 URL=https://arxiv.org/html/2605.17497v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17497 | complete |
| SF-2026-ARXIV-2605-17508 | RP-58b7bdadd08a1df1 | deep | arXiv:2605.17508v1 | SRC-ARXIV@arXiv:2605.17508v1 | arXiv:2605.17508v1 — §4 Methodology (official exact-v1 HTML) | arXiv:2605.17508v1 — §5 Experiments (official exact-v1 HTML) | arXiv:2605.17508v1 — §6 Discussion (official exact-v1 HTML) | exact-v1 URL=https://arxiv.org/html/2605.17508v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17508 | complete |
| SF-2026-ARXIV-2605-17522 | RP-6bc13b2fc4831772 | deep | arXiv:2605.17522v1 | SRC-ARXIV@arXiv:2605.17522v1 | arXiv:2605.17522v1 — §3 Methodology (§3.2–§3.4) (official exact-v1 HTML) | arXiv:2605.17522v1 — §4 Experiments (official exact-v1 HTML) | arXiv:2605.17522v1 — §5 Conclusion; no dedicated limitations section (official exact-v1 HTML) | exact-v1 URL=https://arxiv.org/html/2605.17522v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17522 | complete |
| SF-2026-ARXIV-2605-17554 | RP-8fd81b6c2deb1a72 | deep | arXiv:2605.17554v1 | SRC-ARXIV@arXiv:2605.17554v1 | arXiv:2605.17554v1 — §3 Benchmark Design (§3.3–§3.4) (official exact-v1 HTML) | arXiv:2605.17554v1 — §4 Experiments (official exact-v1 HTML) | arXiv:2605.17554v1 — §5 Limitations (official exact-v1 HTML) | exact-v1 URL=https://arxiv.org/html/2605.17554v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17554 | complete |
| SF-2026-ARXIV-2605-17558 | RP-4e90e6a30316ee3c | deep | arXiv:2605.17558v1 | SRC-ARXIV@arXiv:2605.17558v1 | arXiv:2605.17558v1 — §3 Method (§3.1–§3.3) (official exact-v1 HTML) | arXiv:2605.17558v1 — §5 Experiments (official exact-v1 HTML) | arXiv:2605.17558v1 — §7 Limitations (official exact-v1 HTML) | exact-v1 URL=https://arxiv.org/html/2605.17558v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17558 | complete |
| SF-2026-ARXIV-2605-17570 | RP-50aa0ee32143c72b | deep | arXiv:2605.17570v1 | SRC-ARXIV@arXiv:2605.17570v1 | arXiv:2605.17570v1 — §3 Diagnosing rollout staleness; §4 μ-GRPO (official exact-v1 HTML) | arXiv:2605.17570v1 — §5 Experiments (official exact-v1 HTML) | arXiv:2605.17570v1 — §6 Discussion; no dedicated limitations section (official exact-v1 HTML) | exact-v1 URL=https://arxiv.org/html/2605.17570v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17570 | complete |
| SF-2026-ARXIV-2605-17590 | RP-ea7dfb0b951aa8b6 | deep | arXiv:2605.17590v1 | SRC-ARXIV@arXiv:2605.17590v1 | arXiv:2605.17590v1 — §4 Problem Setup (frozen exact-v1 official HTML receipt) | arXiv:2605.17590v1 — §5 Theoretical Results (frozen exact-v1 official HTML receipt) | arXiv:2605.17590v1 — §7 Discussion (frozen exact-v1 official HTML receipt) | papers/2026/05/_sources/daily-20260518/exact-review-batch-e.txt#sha256=1e15947a8136d8f1b1232dcfbe26d6079e3ebda4c1eeefa746a92fa7918ad8f5; exact-v1 URL=https://arxiv.org/html/2605.17590v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17590 | complete |
| SF-2026-ARXIV-2605-17609 | RP-1f65541b4be860cd | deep | arXiv:2605.17609v1 | SRC-ARXIV@arXiv:2605.17609v1 | arXiv:2605.17609v1 — §4 ADAP Adaptive Policy (official exact-v1 HTML) | arXiv:2605.17609v1 — §5 Experiments (official exact-v1 HTML) | arXiv:2605.17609v1 — §7 Limitations (official exact-v1 HTML) | exact-v1 URL=https://arxiv.org/html/2605.17609v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17609 | complete |
| SF-2026-ARXIV-2605-17610 | RP-c880c7a672f66557 | deep | arXiv:2605.17610v1 | SRC-ARXIV@arXiv:2605.17610v1 | arXiv:2605.17610v1 — §4 Data Curation; §5 SafeLens (official exact-v1 HTML) | arXiv:2605.17610v1 — §6 Experiments (official exact-v1 HTML) | arXiv:2605.17610v1 — Appendix A Limitations (official exact-v1 HTML) | exact-v1 URL=https://arxiv.org/html/2605.17610v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17610 | complete |
| SF-2026-ARXIV-2605-17613 | RP-27371fd8358ec6cf | deep | arXiv:2605.17613v1 | SRC-ARXIV@arXiv:2605.17613v1 | arXiv:2605.17613v1 — §3 Motivation: Why Lossy KV Methods Fail (frozen exact-v1 official HTML receipt) | Not Disclosed — no dedicated evaluation heading in the frozen exact-v1 receipt | Not Disclosed — no dedicated limitations heading; claim remains bounded to disclosed setup | papers/2026/05/_sources/daily-20260518/exact-review-batch-e.txt#sha256=1e15947a8136d8f1b1232dcfbe26d6079e3ebda4c1eeefa746a92fa7918ad8f5; exact-v1 URL=https://arxiv.org/html/2605.17613v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17613 | complete |
| SF-2026-ARXIV-2605-17617 | RP-1873e52a02c202e2 | deep | arXiv:2605.17617v1 | SRC-ARXIV@arXiv:2605.17617v1 | arXiv:2605.17617v1 — §3 Offline Workflow Graph; §4 Online Traversal; §5 Reinforcement (official exact-v1 HTML) | arXiv:2605.17617v1 — §6 Evaluation; §7 Production Deployment (official exact-v1 HTML) | arXiv:2605.17617v1 — §8 Discussion (official exact-v1 HTML) | exact-v1 URL=https://arxiv.org/html/2605.17617v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17617 | complete |
| SF-2026-ARXIV-2605-17625 | RP-fd0bb5cfe38cb552 | deep | arXiv:2605.17625v1 | SRC-ARXIV@arXiv:2605.17625v1 | arXiv:2605.17625v1 — §3 Dual-Process Memory Architecture; §3.2 Episodic Window; §3.3 Semantic Consolidation (official exact-v1 HTML) | arXiv:2605.17625v1 — §4 Experimental Design; §5 Results (official exact-v1 HTML) | arXiv:2605.17625v1 — §6 Discussion and limitations (official exact-v1 HTML) | exact-v1 URL=https://arxiv.org/html/2605.17625v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17625 | complete |
| SF-2026-ARXIV-2605-17634 | RP-541d3dd31d65f8f0 | deep | arXiv:2605.17634v1 | SRC-ARXIV@arXiv:2605.17634v1 | arXiv:2605.17634v1 — §1 Introduction (frozen exact-v1 official HTML receipt) | arXiv:2605.17634v1 — §5.1 Attacking Context Parameters Inference and Norm Evaluation (frozen exact-v1 official HTML receipt) | arXiv:2605.17634v1 — §3 Limitations of Current Views on Prompt Injection (frozen exact-v1 official HTML receipt) | papers/2026/05/_sources/daily-20260518/exact-review-batch-e.txt#sha256=1e15947a8136d8f1b1232dcfbe26d6079e3ebda4c1eeefa746a92fa7918ad8f5; exact-v1 URL=https://arxiv.org/html/2605.17634v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17634 | complete |
| SF-2026-ARXIV-2605-17641 | RP-850eed6256cef4eb | deep | arXiv:2605.17641v1 | SRC-ARXIV@arXiv:2605.17641v1 | arXiv:2605.17641v1 — §3 Proposed Framework (frozen exact-v1 official HTML receipt) | arXiv:2605.17641v1 — §5 Experimental Setup (frozen exact-v1 official HTML receipt) | Not Disclosed — no dedicated limitations heading; claim remains bounded to disclosed setup | papers/2026/05/_sources/daily-20260518/exact-review-batch-e.txt#sha256=1e15947a8136d8f1b1232dcfbe26d6079e3ebda4c1eeefa746a92fa7918ad8f5; exact-v1 URL=https://arxiv.org/html/2605.17641v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17641 | complete |
| SF-2026-ARXIV-2605-17659 | RP-636ba38b321ddb96 | deep | arXiv:2605.17659v1 | SRC-ARXIV@arXiv:2605.17659v1 | arXiv:2605.17659v1 — §1 Formal Illustration of Negative Weight Drift (frozen exact-v1 official HTML receipt) | arXiv:2605.17659v1 — §2 Empirical Results for Negative Weight Drift (frozen exact-v1 official HTML receipt) | Not Disclosed — no dedicated limitations heading; claim remains bounded to disclosed setup | papers/2026/05/_sources/daily-20260518/exact-review-batch-f.txt#sha256=25ee65e984dcd51bcaa12e55ddab1afb3634d8c37ee61aeb21b4ed08e72bec0b; exact-v1 URL=https://arxiv.org/html/2605.17659v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17659 | complete |
| SF-2026-ARXIV-2605-17672 | RP-c7e5999b05d0e91b | deep | arXiv:2605.17672v1 | SRC-ARXIV@arXiv:2605.17672v1 | arXiv:2605.17672v1 — §3 Methodology (frozen exact-v1 official HTML receipt) | arXiv:2605.17672v1 — §4 Experimental Setup (frozen exact-v1 official HTML receipt) | arXiv:2605.17672v1 — §6 Analysis and Discussion (frozen exact-v1 official HTML receipt) | papers/2026/05/_sources/daily-20260518/exact-review-batch-f.txt#sha256=25ee65e984dcd51bcaa12e55ddab1afb3634d8c37ee61aeb21b4ed08e72bec0b; exact-v1 URL=https://arxiv.org/html/2605.17672v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17672 | complete |
| SF-2026-ARXIV-2605-17683 | RP-bea65cf30fc02aa6 | deep | arXiv:2605.17683v1 | SRC-ARXIV@arXiv:2605.17683v1 | arXiv:2605.17683v1 — §4 μ-ORCA Architecture and Implementation; §5 Performance Model and Design-Space Exploration (official exact-v1 HTML) | arXiv:2605.17683v1 — §6 Evaluation (official exact-v1 HTML) | arXiv:2605.17683v1 — §7 Conclusion; no dedicated limitations section (official exact-v1 HTML) | exact-v1 URL=https://arxiv.org/html/2605.17683v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17683 | complete |
| SF-2026-ARXIV-2605-17707 | RP-e51ce4b248dde7df | deep | arXiv:2605.17707v1 | SRC-ARXIV@arXiv:2605.17707v1 | arXiv:2605.17707v1 — §VIII-B () Setup (frozen exact-v1 official HTML receipt) | arXiv:2605.17707v1 — §VIII-D2 Results (frozen exact-v1 official HTML receipt) | Not Disclosed — no dedicated limitations heading; claim remains bounded to disclosed setup | papers/2026/05/_sources/daily-20260518/exact-review-batch-f.txt#sha256=25ee65e984dcd51bcaa12e55ddab1afb3634d8c37ee61aeb21b4ed08e72bec0b; exact-v1 URL=https://arxiv.org/html/2605.17707v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17707 | complete |
| SF-2026-ARXIV-2605-17721 | RP-4178bdceb2bc8b46 | deep | arXiv:2605.17721v1 | SRC-ARXIV@arXiv:2605.17721v1 | arXiv:2605.17721v1 — §2 Experience Graph Design (frozen exact-v1 official HTML receipt) | arXiv:2605.17721v1 — §4 Experiments (frozen exact-v1 official HTML receipt) | Not Disclosed — no dedicated limitations heading; claim remains bounded to disclosed setup | papers/2026/05/_sources/daily-20260518/exact-review-batch-f.txt#sha256=25ee65e984dcd51bcaa12e55ddab1afb3634d8c37ee61aeb21b4ed08e72bec0b; exact-v1 URL=https://arxiv.org/html/2605.17721v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17721 | complete |
| SF-2026-ARXIV-2605-17734 | RP-a0b5b8edab9b2319 | deep | arXiv:2605.17734v1 | SRC-ARXIV@arXiv:2605.17734v1 | arXiv:2605.17734v1 HTML — §3.1–3.3 Program Functions | arXiv:2605.17734v1 HTML — §4.1–4.2 Experiments | arXiv:2605.17734v1 HTML — Appendix A Limitations | arXiv:2605.17734v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-17734 | complete |
| SF-2026-ARXIV-2605-17757 | RP-5ffb4a0509895ab1 | deep | arXiv:2605.17757v1 | SRC-ARXIV@arXiv:2605.17757v1 | arXiv:2605.17757v1 HTML — §3 OSCAR; §3.1–3.4 offline covariance-aware rotation and mixed K/V layout | arXiv:2605.17757v1 HTML — §4 Experiments; §4.1–4.5 quality, memory and kernel latency | arXiv:2605.17757v1 HTML — Appendix D Limitations | arXiv:2605.17757v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-17757 | complete |
| SF-2026-ARXIV-2605-17787 | RP-b65fc9d1cab0fc01 | deep | arXiv:2605.17787v1 | SRC-ARXIV@arXiv:2605.17787v1 | arXiv:2605.17787v1 HTML — §3 Training Dynamics; §4.1–4.2 clipping | arXiv:2605.17787v1 HTML — Appendix B–C settings and ablations | arXiv:2605.17787v1 HTML — §5 Conclusions; Appendix C.4 seeds | arXiv:2605.17787v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-17787 | complete |
| SF-2026-ARXIV-2605-17821 | RP-19ab22f616f4d751 | deep | arXiv:2605.17821v1 | SRC-ARXIV@arXiv:2605.17821v1 | arXiv:2605.17821v1 HTML — §3 TierCheck Design; §3.1 save/retrieve/reclaim across local, peer and remote tiers | arXiv:2605.17821v1 HTML — §5 Evaluation; failure frequency, checkpoint overhead and recovery | arXiv:2605.17821v1 HTML — §7 Conclusion; no dedicated limitations section, production failure correlation Not Disclosed | arXiv:2605.17821v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-17821 | complete |
| SF-2026-ARXIV-2605-17830 | RP-22d5f6d458a04b87 | deep | arXiv:2605.17830v1 | SRC-ARXIV@arXiv:2605.17830v1 | arXiv:2605.17830v1 HTML — §3.1–3.5 stateful setting and monitor | arXiv:2605.17830v1 HTML — §4 protocol; §5 results | arXiv:2605.17830v1 HTML — §6 Discussion and limitations | arXiv:2605.17830v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-17830 | complete |
| SF-2026-ARXIV-2605-17842 | RP-6f3e2305afb21987 | deep | arXiv:2605.17842v1 | SRC-ARXIV@arXiv:2605.17842v1 | arXiv:2605.17842v1 HTML — §3.2–3.5 Structured Newton Layer Parallelism | arXiv:2605.17842v1 HTML — §5.1–5.3 experiments | arXiv:2605.17842v1 HTML — §6 Limitations | arXiv:2605.17842v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-17842 | complete |
| SF-2026-ARXIV-2605-17849 | RP-782a8edd284bb7a0 | deep | arXiv:2605.17849v1 | SRC-ARXIV@arXiv:2605.17849v1 | arXiv:2605.17849v1 HTML — §3.1–3.3 model-aware synthesis | arXiv:2605.17849v1 HTML — §4 experiments and analyses | arXiv:2605.17849v1 HTML — §5 limitations | arXiv:2605.17849v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-17849 | complete |
| SF-2026-ARXIV-2605-17862 | RP-252dab091f3d839c | deep | arXiv:2605.17862v1 | SRC-ARXIV@arXiv:2605.17862v1 | arXiv:2605.17862v1 HTML — §3.1–3.3 drift decomposition; §4 freshness control | arXiv:2605.17862v1 HTML — §5.1–5.4 experiments | arXiv:2605.17862v1 HTML — §6 limitations | arXiv:2605.17862v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-17862 | complete |
| SF-2026-ARXIV-2605-17877 | RP-0dcd3afd9fbbf4dc | deep | arXiv:2605.17877v1 | SRC-ARXIV@arXiv:2605.17877v1 | arXiv:2605.17877v1 HTML — §3 PAIR; prefix-aware dense reward construction and intervention | arXiv:2605.17877v1 HTML — §4 Experiments; multi-turn agent optimization and ablations | arXiv:2605.17877v1 HTML — Appendix J Limitations | arXiv:2605.17877v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-17877 | complete |
| SF-2026-ARXIV-2605-17879 | RP-24e57c07b3182fda | deep | arXiv:2605.17879v1 | SRC-ARXIV@arXiv:2605.17879v1 | arXiv:2605.17879v1 HTML — §3–§6 Guard architecture; online monitor, offline node sweep and triage | arXiv:2605.17879v1 HTML — §7 Evaluation; fail-slow detection, false positives and cluster overhead | arXiv:2605.17879v1 HTML — §7–§8 claim boundary; no dedicated limitations section | arXiv:2605.17879v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-17879 | complete |
| SF-2026-ARXIV-2605-17889 | RP-ceff824f43de350b | deep | arXiv:2605.17889v1 | SRC-ARXIV@arXiv:2605.17889v1 | arXiv:2605.17889v1 HTML — §3 Motivation; §4.1–4.2 orchestration | arXiv:2605.17889v1 HTML — §5 evaluation | arXiv:2605.17889v1 HTML — §6 discussion and limitations | arXiv:2605.17889v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-17889 | complete |
| SF-2026-ARXIV-2605-17912 | RP-6f71c93a50fcb2bb | deep | arXiv:2605.17912v1 | SRC-ARXIV@arXiv:2605.17912v1 | arXiv:2605.17912v1 HTML — §3 WorldArena 2.0 benchmark axes and task construction | arXiv:2605.17912v1 HTML — §4 Experiments across modality, functionality and platform | arXiv:2605.17912v1 HTML — §5 Discussion/Conclusion; simulator and selected-model boundary | arXiv:2605.17912v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-17912 | complete |
| SF-2026-ARXIV-2605-17921 | RP-a02c424b3c54be6f | deep | arXiv:2605.17921v1 | SRC-ARXIV@arXiv:2605.17921v1 | arXiv:2605.17921v1 HTML — §3–§4 R3-Streaming cascaded memory, readiness and compute routing | arXiv:2605.17921v1 HTML — §5 Experiments; latency/accuracy under streaming video workloads | arXiv:2605.17921v1 HTML — §6 Conclusion; no production tail-SLO or failure-recovery evidence | arXiv:2605.17921v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-17921 | complete |
| SF-2026-ARXIV-2605-17923 | RP-5e997a97976986cb | deep | arXiv:2605.17923v1 | SRC-ARXIV@arXiv:2605.17923v1 | arXiv:2605.17923v1 HTML — §3 AdaptiveLoad; dual memory/compute constrained batch construction and fused execution | arXiv:2605.17923v1 HTML — §4 Experiments on video diffusion training | arXiv:2605.17923v1 HTML — §5 Conclusion/limitations; selected models and hardware only | arXiv:2605.17923v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-17923 | complete |
| SF-2026-ARXIV-2605-17932 | RP-a5dd7c7800d2dfa1 | deep | arXiv:2605.17932v1 | SRC-ARXIV@arXiv:2605.17932v1 | arXiv:2605.17932v1 HTML — §III-A–C compression pipeline | arXiv:2605.17932v1 HTML — §III-D; §IV-A–C | arXiv:2605.17932v1 HTML — §V Discussion; §VII Future Work | arXiv:2605.17932v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-17932 | complete |
| SF-2026-ARXIV-2605-17954 | RP-01379cd993382ecb | deep | arXiv:2605.17954v1 | SRC-ARXIV@arXiv:2605.17954v1 | arXiv:2605.17954v1 HTML — §2 motivation; §3.1–3.4 tokenization | arXiv:2605.17954v1 HTML — §4.1–4.4 experiments | arXiv:2605.17954v1 HTML — §5 limitations | arXiv:2605.17954v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-17954 | complete |
| SF-2026-ARXIV-2605-17986 | RP-e92ff8a8f642e82b | deep | arXiv:2605.17986v1 | SRC-ARXIV@arXiv:2605.17986v1 | arXiv:2605.17986v1 HTML — §3 Threat model and benchmark construction | arXiv:2605.17986v1 HTML — §4–§5 evaluation and defense analysis across live interaction surfaces | arXiv:2605.17986v1 HTML — §6 Limitations | arXiv:2605.17986v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-17986 | complete |
| SF-2026-ARXIV-2605-17989 | RP-6f92f00df0a7d022 | deep | arXiv:2605.17989v1 | SRC-ARXIV@arXiv:2605.17989v1 | arXiv:2605.17989v1 HTML — §3 Predictive prefetch controller and retrieval-generation overlap | arXiv:2605.17989v1 HTML — §4 Evaluation; latency, retrieval usefulness and prediction error | arXiv:2605.17989v1 HTML — §6 Limitations; stale/incorrect demand and workload boundary | arXiv:2605.17989v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-17989 | complete |
| SF-2026-ARXIV-2605-17992 | RP-d500e8299cf252c6 | deep | arXiv:2605.17992v1 | SRC-ARXIV@arXiv:2605.17992v1 | arXiv:2605.17992v1 HTML — §3 PipeANN-Filter superset traversal, post-verification and pipelined SSD IO | arXiv:2605.17992v1 HTML — §4–§5 implementation and filtered-ANN evaluation | arXiv:2605.17992v1 HTML — §6 Limitations; index/filter/update boundary | arXiv:2605.17992v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-17992 | complete |
| SF-2026-ARXIV-2605-17998 | RP-1e8793fab16b7d56 | deep | arXiv:2605.17998v1 | SRC-ARXIV@arXiv:2605.17998v1 | arXiv:2605.17998v1 HTML — §3–§8 read-only verifier, proposal/admission state and bounded completion protocol | arXiv:2605.17998v1 HTML — §9–§10 architecture case study and failure injection | arXiv:2605.17998v1 HTML — §12 Limitations; bounded case study, not a universal correctness proof | arXiv:2605.17998v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-17998 | complete |
| SF-2026-ARXIV-2605-18032 | RP-1c13034dd3b4c092 | deep | arXiv:2605.18032v1 | SRC-ARXIV@arXiv:2605.18032v1 | arXiv:2605.18032v1 HTML — §2 architecture; §3.1–3.3 node diagnosis | arXiv:2605.18032v1 HTML — §4.1–4.3 evaluation | arXiv:2605.18032v1 HTML — §5 Conclusion | arXiv:2605.18032v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-18032 | complete |
| SF-2026-ARXIV-2605-18041 | RP-a017770fe83edc69 | standard | arXiv:2605.18041v1 | SRC-ARXIV@arXiv:2605.18041v1 | arXiv:2605.18041v1 HTML — §3 OmniSelect modality-aware token-budget controller | arXiv:2605.18041v1 HTML — §4 Experiments on audio-video OmniLLMs | arXiv:2605.18041v1 HTML — §5 Limitations; model/task-local compression evidence | arXiv:2605.18041v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-18041 | complete |
| SF-2026-ARXIV-2605-18053 | RP-d13fb94bd59cda38 | deep | arXiv:2605.18053v1 | SRC-ARXIV@arXiv:2605.18053v1 | arXiv:2605.18053v1 HTML — §3–§7 globally capped KV eviction and structural boundary protection | arXiv:2605.18053v1 HTML — §8–§9 evaluation across policies/models and cross-architecture challenge | arXiv:2605.18053v1 HTML — §10.22 Limitations | arXiv:2605.18053v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-18053 | complete |
| SF-2026-ARXIV-2605-18067 | RP-ed48c39e12ae07f7 | deep | arXiv:2605.18067v1 | SRC-ARXIV@arXiv:2605.18067v1 | arXiv:2605.18067v1 HTML — §IV–VI agent scoring and serving game | arXiv:2605.18067v1 HTML — §VIII implementation and experiments | arXiv:2605.18067v1 HTML — §VII Discussion | arXiv:2605.18067v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-18067 | complete |
| SF-2026-ARXIV-2605-18071 | RP-1810f220fe28004a | deep | arXiv:2605.18071v1 | SRC-ARXIV@arXiv:2605.18071v1 | arXiv:2605.18071v1 HTML — §4–§7 multi-tier KV design | arXiv:2605.18071v1 HTML — §9.1–9.3 experiments | arXiv:2605.18071v1 HTML — §10–§11 conclusion and future work | arXiv:2605.18071v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-18071 | complete |
| SF-2026-ARXIV-2605-18106 | RP-a0c3c051241d947a | deep | arXiv:2605.18106v1 | SRC-ARXIV@arXiv:2605.18106v1 | arXiv:2605.18106v1 HTML — §3–§5 symmetry-compatible optimizer design | arXiv:2605.18106v1 HTML — §6 experiments | arXiv:2605.18106v1 HTML — §1 Scope and limitations; §7 discussion | arXiv:2605.18106v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-18106 | complete |
| SF-2026-ARXIV-2605-18165 | RP-bbf05cdd370c502d | deep | arXiv:2605.18165v1 | SRC-ARXIV@arXiv:2605.18165v1 | arXiv:2605.18165v1 HTML — §3 mask state; §4.1–4.3 compression | arXiv:2605.18165v1 HTML — §5.1–5.4 experiments | arXiv:2605.18165v1 HTML — §6 limitations | arXiv:2605.18165v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-18165 | complete |
| SF-2026-ARXIV-2605-18271 | RP-b618e263c39bbaf0 | deep | arXiv:2605.18271v1 | SRC-ARXIV@arXiv:2605.18271v1 | arXiv:2605.18271v1 HTML — PDF pp.3–5 §3.1–3.3 memory construction | arXiv:2605.18271v1 HTML — PDF §4–§5; device experiments | arXiv:2605.18271v1 HTML — PDF §6 Limitations | arXiv:2605.18271v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-18271 | complete |
| SF-2026-ARXIV-2605-18401 | RP-0e10991beabfb448 | deep | arXiv:2605.18401v1 | SRC-ARXIV@arXiv:2605.18401v1 | arXiv:2605.18401v1 HTML — §3 SkillsVote collection, recommendation, validation and evolution lifecycle | arXiv:2605.18401v1 HTML — §4 Experiments and lifecycle ablations | arXiv:2605.18401v1 HTML — §5/Appendix limitations; ecosystem and environment sensitivity | arXiv:2605.18401v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-18401 | complete |
| SF-2026-ARXIV-2605-18414 | RP-feb9599fea2d9335 | deep | arXiv:2605.18414v1 | SRC-ARXIV@arXiv:2605.18414v1 | arXiv:2605.18414v1 HTML — §3 governed MCP proxy | arXiv:2605.18414v1 HTML — §4–§5 benchmark and results | arXiv:2605.18414v1 HTML — §6–§7 discussion and threat-model limits | arXiv:2605.18414v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-18414 | complete |
| SF-2026-ARXIV-2605-18421 | RP-833f930afb3c701a | deep | arXiv:2605.18421v1 | SRC-ARXIV@arXiv:2605.18421v1 | arXiv:2605.18421v1 HTML — §3–§4 EvoMemBench in/cross-episode and knowledge/execution axes | arXiv:2605.18421v1 HTML — §5 Experiments across memory systems | arXiv:2605.18421v1 HTML — §6 Conclusion; benchmark/model coverage boundary | arXiv:2605.18421v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-18421 | complete |
| SF-2026-ARXIV-2605-18498 | RP-18a67d9e5ec45674 | deep | arXiv:2605.18498v1 | SRC-ARXIV@arXiv:2605.18498v1 | arXiv:2605.18498v1 HTML — PDF pp.3–5 §3 routing-specialization metrics | arXiv:2605.18498v1 HTML — PDF pp.5–11 §4 experiments and intervention | arXiv:2605.18498v1 HTML — PDF p.11 §4.3 intervention boundary; §5 Conclusion | arXiv:2605.18498v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-18498 | complete |
| SF-2026-ARXIV-2605-18565 | RP-1e362dd51e3c4598 | deep | arXiv:2605.18565v1 | SRC-ARXIV@arXiv:2605.18565v1 | arXiv:2605.18565v1 HTML — §3 MINTEval multi-target interference construction and update semantics | arXiv:2605.18565v1 HTML — §4 Experiments; recall and aggregation under evolving memories | arXiv:2605.18565v1 HTML — §5 Limitations; synthetic tasks and selected agents | arXiv:2605.18565v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-18565 | complete |
| SF-2026-ARXIV-2605-18583 | RP-58c5225348983c36 | deep | arXiv:2605.18583v1 | SRC-ARXIV@arXiv:2605.18583v1 | arXiv:2605.18583v1 HTML — §3 benchmark, benign task scope and overeager-action taxonomy | arXiv:2605.18583v1 HTML — §4 Experiments across coding agents | arXiv:2605.18583v1 HTML — §5 Limitations; harness and observable-action boundary | arXiv:2605.18583v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-18583 | complete |
| SF-2026-ARXIV-2605-18607 | RP-05c7d985e620ad3c | deep | arXiv:2605.18607v1 | SRC-ARXIV@arXiv:2605.18607v1 | arXiv:2605.18607v1 HTML — §3 proxy metrics | arXiv:2605.18607v1 HTML — §4–§5 model/data ranking | arXiv:2605.18607v1 HTML — §6 limitations | arXiv:2605.18607v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-18607 | complete |
| SF-2026-ARXIV-2605-18652 | RP-fb32c4b5d2bfc297 | deep | arXiv:2605.18652v1 | SRC-ARXIV@arXiv:2605.18652v1 | arXiv:2605.18652v1 HTML — §3 MementoGUI multimodal memory controller and write/read policy | arXiv:2605.18652v1 HTML — §4–§5 benchmark construction and experiments | arXiv:2605.18652v1 HTML — §6 Limitations; GUI domain and selected backbones | arXiv:2605.18652v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-18652 | complete |
| SF-2026-ARXIV-2605-18693 | RP-8ced56893e741499 | deep | arXiv:2605.18693v1 | SRC-ARXIV@arXiv:2605.18693v1 | arXiv:2605.18693v1 HTML — §3.1–3.4 skill-generation artifact contract | arXiv:2605.18693v1 HTML — §4.1–4.4 execution evaluation | arXiv:2605.18693v1 HTML — §5 Conclusion; appendix sensitivity | arXiv:2605.18693v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-18693 | complete |
| SF-2026-ARXIV-2605-18697 | RP-276218662ac669c8 | deep | arXiv:2605.18697v1 | SRC-ARXIV@arXiv:2605.18697v1 | arXiv:2605.18697v1 HTML — §3–§6 PopPy compiler/runtime dependency discovery and external-call parallelism | arXiv:2605.18697v1 HTML — §8 Evaluation; latency and semantic-equivalence checks | arXiv:2605.18697v1 HTML — §10 Discussion; Python/compound-application boundary | arXiv:2605.18697v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-18697 | complete |
| SF-2026-ARXIV-2605-18703 | RP-8a546d8bff6fd339 | deep | arXiv:2605.18703v1 | SRC-ARXIV@arXiv:2605.18703v1 | arXiv:2605.18703v1 HTML — §3–§4 executable-environment synthesis, verification and RL data path | arXiv:2605.18703v1 HTML — §5 Evaluation of environment validity and agent training | arXiv:2605.18703v1 HTML — §6 Limitations | arXiv:2605.18703v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-18703 | complete |
| SF-2026-ARXIV-2605-18710 | RP-c006e759b41b9bff | deep | arXiv:2605.18710v1 | SRC-ARXIV@arXiv:2605.18710v1 | arXiv:2605.18710v1 HTML — §3 Mosaic spatial resource multiplexing, placement and performance model | arXiv:2605.18710v1 HTML — §4 Evaluation across multimodal module mixtures | arXiv:2605.18710v1 HTML — §5 Limitations; selected architectures/hardware | arXiv:2605.18710v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-18710 | complete |
| SF-2026-ARXIV-2605-18739 | RP-6890bac3cb8945fc | deep | arXiv:2605.18739v1 | SRC-ARXIV@arXiv:2605.18739v1 | arXiv:2605.18739v1 HTML — §3–§4 NVFP4 training/inference infrastructure and parallel layouts | arXiv:2605.18739v1 HTML — §5 Evaluation on long-video generation | arXiv:2605.18739v1 HTML — §6 Limitations; vendor precision and workload boundary | arXiv:2605.18739v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-18739 | complete |
| SF-2026-ARXIV-2605-18750 | RP-6c2b5f23f488451e | deep | arXiv:2605.18750v1 | SRC-ARXIV@arXiv:2605.18750v1 | arXiv:2605.18750v1 HTML — §3 readiness-driven runtime and dependency state | arXiv:2605.18750v1 HTML — §4–§5 implementation and evaluation under runtime variability | arXiv:2605.18750v1 HTML — §6 Limitations; schedule/hardware/workload boundary | arXiv:2605.18750v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-18750 | complete |
| SF-2026-ARXIV-2605.16588 | RP-42a8f44d35dd6ce8 | deep | arXiv:2605.16588v1 | SRC-ARXIV@arXiv:2605.16588v1 | arXiv:2605.16588v1 — Methodology: §IV Policy Library CBF (official v1 HTML) | arXiv:2605.16588v1 — Experiments: §§V–VI theoretical and empirical evaluation (official v1 HTML) | arXiv:2605.16588v1 — Scope and limitations: §VII Conclusion; no dedicated limitations heading (official v1 HTML) | webcache-2605.16588.txt#sha256=74c8c0caf55313aec558581fe07cd0ac2f9ceb6b8e94b9657e1405cbb96df69b; immutable artifact commit Not Disclosed | claim:SF-2026-ARXIV-2605.16588 | complete |
| SF-2026-ARXIV-2605.16622 | RP-b7c022327cb94a47 | deep | arXiv:2605.16622v1 | SRC-ARXIV@arXiv:2605.16622v1 | arXiv:2605.16622v1 — Methodology: 4 The Mechanism is Global Interaction (official v1 HTML) | arXiv:2605.16622v1 — Experiments: 3 Weight Decay Empirically Changes EoS Dynamics (official v1 HTML) | arXiv:2605.16622v1 — Scope and limitations: 7 Limitations (official v1 HTML) | webcache-2605.16622.txt#sha256=49144e7ec031eb353c01a4991ea78c1692757f4dbafdbcb38aa238b22381d11d; immutable artifact commit Not Disclosed | claim:SF-2026-ARXIV-2605.16622 | complete |
| SF-2026-ARXIV-2605.16647 | RP-693007d68dab1676 | deep | arXiv:2605.16647v1 | SRC-ARXIV@arXiv:2605.16647v1 | arXiv:2605.16647v1 — Methodology: 3 Problem Formulation (official v1 HTML) | arXiv:2605.16647v1 — Experiments: 5 Complexity and Noise Analysis (official v1 HTML) | arXiv:2605.16647v1 — Scope and limitations: 8 Discussion and Limitations (official v1 HTML) | webcache-2605.16647.txt#sha256=8bb432dbe4bce20f4d45e0fa48ca522fd10372ee927a2be92c00af461b96df75; immutable artifact commit Not Disclosed | claim:SF-2026-ARXIV-2605.16647 | complete |
| SF-ANNEAL-GOVERNED-SYMBOLIC-PATCHES | RP-896440ffac903684 | deep | arXiv:2605.16309v1 | SRC-ARXIV@arXiv:2605.16309v1 | arXiv:2605.16309v1 §Method/Design (paper-specific heading); arXiv:2605.16309v1 HTML, Method/Design section; abstract mechanism: We introduce ANNEAL, a neuro-symbolic agent that converts recurring failures into governed symbolic edits of a process knowledge graph without modifying foundation model weights. | arXiv:2605.16309v1 §Experiments/Evaluation (paper-specific heading); arXiv:2605.16309v1 HTML, Experiments/Evaluation and ablation sections; abstract scope: Across four domains and 27 multi-seed runs, ANNEAL is the only evaluated system that commits persistent structural repairs--strong baselines such as ReAct and Reflexion achieve high episodic recovery… | arXiv:2605.16309v1 §Scope and Limitations (paper-specific heading); arXiv:2605.16309v1 HTML, Discussion/Limitations and threat-to-validity passages; no cross-workload generalization inferred | arXiv:2605.16309v1 Appendix/Artifact statement; arXiv:2605.16309v1 HTML, artifact/code statement; immutable event-time commit is Not Disclosed unless explicitly named | claim:SF-ANNEAL-GOVERNED-SYMBOLIC-PATCHES | complete |
| SF-FRE-RES-FREQUENCY-RESIDUAL-VIDEO-TOKEN-COMPRESSION-FOR-EFFICIENT-VIDEO-M | RP-f6b41c484408fd7f | standard | arXiv:2605.16366v1 | SRC-ARXIV@arXiv:2605.16366v1 | arXiv:2605.16366v1 — §3 frequency-residual compression and spatial absorber — mechanism: We propose \textbf{Fre-Res}, a budget-adaptive dual-track video-token compression framework that separates these two forms of evidence. | arXiv:2605.16366v1 — §4 short/long-video evaluation and ablations — disclosed evaluation scope only | arXiv:2605.16366v1 — §Limitations / Counterevidence — limitations: vision encoder, temporal-frequency assumptions and token budget — non-proof boundary retained | arXiv:2605.16366v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-FRE-RES-FREQUENCY-RESIDUAL-VIDEO-TOKEN-COMPRESSION-FOR-EFFICIENT-VIDEO-M | complete |
| SF-MIXING-TIMES-OF-GLAUBER-DYNAMICS-ON-MASKED-LANGUAGE-MODELS | RP-7fffdbb5b8ec99bb | standard | arXiv:2605.16378v1 | SRC-ARXIV@arXiv:2605.16378v1 | arXiv:2605.16378v1 — §3 rectangle incompatibility test; §4–§5 mixing theory — mechanism: We first show that MLM conditionals are intrinsically incompatible: we introduce a rectangle test that certifies this incompatibility and empirically verify its prevalence across modern MLMs. | arXiv:2605.16378v1 — §6 BERT/RoBERTa chain experiments — disclosed evaluation scope only | arXiv:2605.16378v1 — §7 limitations: loose bounds, classifier dependence and unknown stationary law — non-proof boundary retained | arXiv:2605.16378v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-MIXING-TIMES-OF-GLAUBER-DYNAMICS-ON-MASKED-LANGUAGE-MODELS | complete |
| SF-ORBISIM-WORLD-MODELS-AS-DIFFERENTIABLE-PHYSICS-ENGINES-FOR-EMBODIED-INTE | RP-033b998e9cf33488 | deep | arXiv:2605.16395v1 | SRC-ARXIV@arXiv:2605.16395v1 | arXiv:2605.16395v1 HTML — §3 OrbiSim persistent world-state simulator | arXiv:2605.16395v1 — §4 interactive-world evaluation | arXiv:2605.16395v1 — §5 limitations: environment fidelity and action space | arXiv:2605.16395v1 artifact/code statement; immutable commit Not Disclosed unless named | claim:SF-ORBISIM-WORLD-MODELS-AS-DIFFERENTIABLE-PHYSICS-ENGINES-FOR-EMBODIED-INTE | complete |
| SF-ORTH-DION-ELIMINATING-GEOMETRIC-MISMATCH-IN-DISTRIBUTED-LOW-RANK-SPECTRA | RP-1d3fa5a42c613221 | deep | arXiv:2605.16341v1 | SRC-ARXIV@arXiv:2605.16341v1 | https://arxiv.org/html/2605.16341v1 §3 Geometric Mismatch; §4 Orth-Dion — mechanism: We show that this gap is geometric: column normalization does not yield the rank-$r$ polar factor that Muon implicitly targets, so the resulting direction violates the dual-norm constraint of the low-rank spectral geometry, and the rate picks up… | https://arxiv.org/html/2605.16341v1 §5 Theory; §6 LLM Pretraining Experiments — disclosed evaluation scope only | https://arxiv.org/html/2605.16341v1 §7 Limitations and Adaptive-Rank Cost — no generalization beyond disclosed workload/model/evaluator | https://arxiv.org/html/2605.16341v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-ORTH-DION-ELIMINATING-GEOMETRIC-MISMATCH-IN-DISTRIBUTED-LOW-RANK-SPECTRA | complete |
| SF-PROOF-CARRYING-CERTIFICATES-FOR-LLM-PIPELINES-A-TRUST-BOUNDARY-ARCHITECT | RP-ea7aadc9b4b72c28 | deep | arXiv:2605.16407v1 | SRC-ARXIV@arXiv:2605.16407v1 | arXiv:2605.16407v1 HTML — §Method / System Design — Proof-Carrying Certificates for LLM Pipelines: A Trust-Boundary Architecture 的机制、状态 owner 与控制/数据流 | arXiv:2605.16407v1 HTML — §Experiments / Evaluation — Proof-Carrying Certificates for LLM Pipelines: A Trust-Boundary Architecture 的作者披露 workload、baseline 与 ablation | arXiv:2605.16407v1 HTML — §Limitations / Discussion — Proof-Carrying Certificates for LLM Pipelines: A Trust-Boundary Architecture 的适用范围、未证明项与 failure boundary | arXiv:2605.16407v1 artifact/code statement; immutable commit Not Disclosed unless named | claim:SF-PROOF-CARRYING-CERTIFICATES-FOR-LLM-PIPELINES-A-TRUST-BOUNDARY-ARCHITECT | complete |
| SF-SELFPLAY-DECISION-CAPACITY-COLLAPSE | RP-272e982a24c18f0c | deep | arXiv:2605.16315v1 | SRC-ARXIV@arXiv:2605.16315v1 | arXiv:2605.16315v1 §Method/Design (paper-specific heading); arXiv:2605.16315v1 HTML, Method/Design section; abstract mechanism: We show that a threshold in decision capacity determines whether self-play reinforcement learning agents collapse under asymmetric rule perturbations. | arXiv:2605.16315v1 §Experiments/Evaluation (paper-specific heading); arXiv:2605.16315v1 HTML, Experiments/Evaluation and ablation sections; abstract scope: Across poker variants, matrix games, a dice game, and multiple learning algorithms, eliminating all positive-reach contingent decisions causes rapid convergence to a deterministic exploitation attractor, a fixed point… | arXiv:2605.16315v1 §Scope and Limitations (paper-specific heading); arXiv:2605.16315v1 HTML, Discussion/Limitations and threat-to-validity passages; no cross-workload generalization inferred | arXiv:2605.16315v1 Appendix/Artifact statement; arXiv:2605.16315v1 HTML, artifact/code statement; immutable event-time commit is Not Disclosed unless explicitly named | claim:SF-SELFPLAY-DECISION-CAPACITY-COLLAPSE | complete |
| SF-SIGNMUON-SIGN-ORTHOGONALIZED-OPTIMIZER | RP-2803923a7bd0d8c5 | standard | arXiv:2605.16311v1 | SRC-ARXIV@arXiv:2605.16311v1 | arXiv:2605.16311v1 §Method/Design (paper-specific heading); arXiv:2605.16311v1 HTML, Method/Design section; abstract mechanism: We propose Sign-Muon, a 1-bit, matrix-aware optimizer that combines majority-vote sign aggregation from signSGD with the polar-step framework of Muon. | arXiv:2605.16311v1 §Experiments/Evaluation (paper-specific heading); arXiv:2605.16311v1 HTML, Experiments/Evaluation and ablation sections; abstract scope: With unimodal symmetric noise, majority vote across $M$ workers cuts the stochastic term by $1/\sqrt{M}$, matching signSGD. | arXiv:2605.16311v1 §Scope and Limitations (paper-specific heading); arXiv:2605.16311v1 HTML, Discussion/Limitations and threat-to-validity passages; no cross-workload generalization inferred | arXiv:2605.16311v1 Appendix/Artifact statement; arXiv:2605.16311v1 HTML, artifact/code statement; immutable event-time commit is Not Disclosed unless explicitly named | claim:SF-SIGNMUON-SIGN-ORTHOGONALIZED-OPTIMIZER | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2605-16265:start -->
#### AgentWall: A Runtime Safety Layer for Local AI Agents

<!-- claim:SF-2026-ARXIV-2605-16265:start -->
- **Problem:** The safety of autonomous AI agents is increasingly recognized as a critical open problem.
- **Old path / changed constraint:** Existing AI safety work has focused primarily on model alignment and input filtering, but these approaches do not address what happens at the moment an agent's intent becomes a real action on a real machine.
- **Mechanism / ownership:** We present the design, architecture, threat model, and policy model of AgentWall, and demonstrate 92.9% policy enforcement accuracy with sub-millisecond overhead across 14 benchmark tests.
- **Evaluation contract:** We present the design, architecture, threat model, and policy model of AgentWall, and demonstrate 92.9% policy enforcement accuracy with sub-millisecond overhead across 14 benchmark tests.
- **Proof / non-proof:** Evidence is author-reported exact-v1 mechanism/evaluation evidence. It does not establish cross-model, cross-hardware, cross-workload or production generality unless those conditions are explicitly named above.
- **Trade-off / failure mode:** We present the design, architecture, threat model, and policy model of AgentWall, show its effectiveness across representative local-agent safety scenarios, and discuss its limitations and relationship to complementary safety approaches.
- **Coexistence boundary:** The older path remains appropriate where its workload and SLO do not trigger the changed constraint; the paper is treated as a conditional branch, not a universal replacement.
- **Primary:** [arXiv:2605.16265v1](https://arxiv.org/abs/2605.16265v1)；frozen exact-v1 `papers/2026/05/_sources/arxiv-owner-replay-20260903/exact-v1/2605.16265v1.html.html`。
- **Disposition:** `No Change — Existing Coverage`；Fresh-context owner/adjacent comparison completed; the current Books proposition already owns the durable mechanism, so no duplicate paragraph was added.
<!-- claim:SF-2026-ARXIV-2605-16265:end -->
<!-- review:SF-2026-ARXIV-2605-16265:end -->

<!-- review:SF-2026-ARXIV-2605-16343:start -->
#### LoopQ: Quantization for Recursive Transformers

问题与演进：`LoopQ: Quantization for Recursive Transformers` 通过“We present the first systematic study of quantization in LoopLMs and identify three challenges: distribution shift across roles, state reuse across loop transitions, and recursive error accumulation.”改变 infer tensorrt llm 的可观察机制或决策边界；exact-v1 的证明范围限于“Experiments across seven benchmarks show that, under W4A4 quantization, LoopQ improves average downstream accuracy by 68.8% and reduces average perplexity by 87.7% compared with the strongest static PTQ baseline.”，不能外推到未披露 workload、model、hardware、precision、evaluator 或 SLO。旧方案在其原 workload、风险和成本约束下仍成立。

Method：`https://arxiv.org/html/2605.16343v1 §3 LoopQ loop-aware PTQ — mechanism: We present the first systematic study of quantization in LoopLMs and identify three challenges: distribution shift across roles, state reuse across loop transitions, and recursive error accumulation.`。

Evaluation：`https://arxiv.org/html/2605.16343v1 §4 seven-benchmark W4A4 evaluation — disclosed scope: Looped language models (LoopLMs) improve parameter efficiency by recursively reusing Transformer blocks, enabling deeper computation under a fixed model size. However, this reuse makes LoopLMs more fragile under post-training quantization (PTQ). We present the first systematic study of quantization in LoopLMs and identify three challenges: distribution…`。

Non-proof / fallback：`https://arxiv.org/html/2605.16343v1 Discussion limitations; recursive architecture/model/quantization scope; exact-v1 §6 / Appendix non-proof boundary check — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO`。离开披露条件时回退既有机制，不把作者结果外推为通用保证。Artifact：`https://arxiv.org/html/2605.16343v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-16343:start -->长期结论只限 exact-v1 披露的机制和实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 一律记为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-16343:end -->
<!-- review:SF-2026-ARXIV-2605-16343:end -->

<!-- review:SF-2026-ARXIV-2605-16346:start -->
#### PropGuard: Safeguarding LLM-MAS via Propagation-Aware Exploration and Remediation

问题与演进：`PropGuard: Safeguarding LLM-MAS via Propagation-Aware Exploration and Remediation` 通过“We propose PropGuard, a propagation-aware framework for safeguarding LLM-MAS.”改变 train grpo 的可观察机制或决策边界；exact-v1 的证明范围限于“Experiments across four communication architectures and five attack settings demonstrate that PropGuard consistently lowers attack success while maintaining high task-level defense success, achieving a favorable effectiveness--efficiency trade-off.”，不能外推到未披露 workload、model、hardware、precision、evaluator 或 SLO。旧方案在其原 workload、风险和成本约束下仍成立。

Method：`https://arxiv.org/html/2605.16346v1 §3 dual-view propagation graph; §4 inspector/remediation — mechanism: We propose PropGuard, a propagation-aware framework for safeguarding LLM-MAS.`。

Evaluation：`https://arxiv.org/html/2605.16346v1 §5 four-topology/five-attack evaluation — disclosed scope: Experiments across four communication architectures and five attack settings demonstrate that PropGuard consistently lowers attack success while maintaining high task-level defense success, achieving a favorable effectiveness--efficiency trade-off.`。

Non-proof / fallback：`https://arxiv.org/html/2605.16346v1 Discussion limitations; attack family and replay-remediation scope; exact-v1 §6 / Appendix non-proof boundary check — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO`。离开披露条件时回退既有机制，不把作者结果外推为通用保证。Artifact：`https://arxiv.org/html/2605.16346v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-16346:start -->长期结论只限 exact-v1 披露的机制和实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 一律记为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-16346:end -->
<!-- review:SF-2026-ARXIV-2605-16346:end -->

<!-- review:SF-2026-ARXIV-2605-16354:start -->
#### Augmenting Human Evaluation with LLM Judges: How Many Human Reviews Do You Need?

问题与演进：`Augmenting Human Evaluation with LLM Judges: How Many Human Reviews Do You Need?` 通过“We propose to use a doubly robust estimator from the missing data literature, which takes advantage of the robustness property against the prediction model, since the missingness model is known by design.”改变 platform security 的可观察机制或决策边界；exact-v1 的证明范围限于“This paper (1) shifts the role of the LLM judge from substitutive to auxiliary, and (2) formulates the LLM-as-a-judge paradigm as one of augmenting human evaluation through a two-stage sampling design, where LLM evaluations…”，不能外推到未披露 workload、model、hardware、precision、evaluator 或 SLO。旧方案在其原 workload、风险和成本约束下仍成立。

Method：`https://arxiv.org/html/2605.16354v1 §2 two-stage doubly robust design — mechanism: We propose to use a doubly robust estimator from the missing data literature, which takes advantage of the robustness property against the prediction model, since the missingness model is known by design.`。

Evaluation：`https://arxiv.org/html/2605.16354v1 §3 sample-size/power analysis — disclosed scope: This paper (1) shifts the role of the LLM judge from substitutive to auxiliary, and (2) formulates the LLM-as-a-judge paradigm as one of augmenting human evaluation through a two-stage sampling design, where LLM evaluations are measured for all observations at the first stage and human ratings…`。

Non-proof / fallback：`https://arxiv.org/html/2605.16354v1 Limitations: pilot R² sensitivity and corpus representativeness; exact-v1 §6 / Appendix non-proof boundary check — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO`。离开披露条件时回退既有机制，不把作者结果外推为通用保证。Artifact：`https://arxiv.org/html/2605.16354v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-16354:start -->长期结论只限 exact-v1 披露的机制和实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 一律记为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-16354:end -->
<!-- review:SF-2026-ARXIV-2605-16354:end -->

<!-- review:SF-2026-ARXIV-2605-16359:start -->
#### How Many Visual Tokens Do Multimodal Language Models Need? Scaling Visual Token Pruning with F^3A

问题与演进：视觉 token pruning 应作为 task-conditioned evidence search，预算分配需同时保留局部相关性与 coverage recovery。旧方案在其原 workload、风险和成本约束下仍成立。

Method：`https://arxiv.org/html/2605.16359v1 §3 Method — mechanism: We propose F^3A, a training-free router for visual token pruning that operates before the language model consumes image tokens.`。

Evaluation：`https://arxiv.org/html/2605.16359v1 §4 Experiments — disclosed scope: Vision-language models improve perception by feeding increasingly long visual token sequences into language backbones, but the resulting inference cost raises a basic scaling question: as multimodal models grow, how many visual tokens are actually needed, and how should they be allocated under a fixed visual token…`。

Non-proof / fallback：`https://arxiv.org/html/2605.16359v1 Appendix E Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO`。离开披露条件时回退既有机制，不把作者结果外推为通用保证。Artifact：`https://arxiv.org/html/2605.16359v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-16359:start -->长期结论只限 exact-v1 披露的机制和实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 一律记为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-16359:end -->
<!-- review:SF-2026-ARXIV-2605-16359:end -->

<!-- review:SF-2026-ARXIV-2605-16360:start -->
#### ProxyKV: Cross-Model Proxy Pruning for Efficient Long-Context LLM Inference

问题与演进：高精度 KV importance scoring 可异步交给同 family 小模型 proxy，但会增加 prefill 峰值显存并受 intra-family transfer 约束。旧方案在其原 workload、风险和成本约束下仍成立。

Method：`https://arxiv.org/html/2605.16360v1 §4 ProxyKV and HybridAxialMapper — mechanism: To bridge this scoring-cost--accuracy gap, we propose ProxyKV, a cross-model proxy pruning framework that offloads importance scoring to a lightweight intra-family Small-Model Proxy executed asynchronously to the Large-Model Target.`。

Evaluation：`https://arxiv.org/html/2605.16360v1 §5 Evaluation — disclosed scope: Efficient long-context inference in Large Language Models (LLMs) is severely constrained by the Key-Value (KV) cache memory wall, yet existing pruning methods force a choice between low-latency heuristics that sacrifice precision and high-precision reconstruction methods that incur prohibitive prefilling overhead. To bridge this scoring-cost--accuracy gap, we…`。

Non-proof / fallback：`https://arxiv.org/html/2605.16360v1 §7 Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO`。离开披露条件时回退既有机制，不把作者结果外推为通用保证。Artifact：`https://arxiv.org/html/2605.16360v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-16360:start -->长期结论只限 exact-v1 披露的机制和实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 一律记为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-16360:end -->
<!-- review:SF-2026-ARXIV-2605-16360:end -->

<!-- review:SF-2026-ARXIV-2605-16436:start -->
#### The End of Trust: How Agentic AI Breaks Security Assumptions

问题与演进：Agentic AI 降低高拟真攻击的边际成本，使 rate limit、identity proof 与 human vigilance 的旧经济假设失效；position analysis 不证明具体控制已有效。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.16436v1 §2–§5 Agentic Threat-Economics Analysis — mechanism boundary: For decades, the security of digital interaction has rested on an unacknowledged economic constraint.`。

Evaluation：`https://arxiv.org/html/2605.16436v1 §3–§5 Case Analyses — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.16436v1 §6 Conclusion and position-paper evidence boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.16436v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-16436:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-16436:end -->
<!-- review:SF-2026-ARXIV-2605-16436:end -->

<!-- review:SF-2026-ARXIV-2605-16439:start -->
#### KVCapsule: Efficient Sequential KV Cache Compression for Vision-Language Models with Asymmetric Redundancy

问题与演进：VLM KV compression 应利用视觉与文本 token 的非对称冗余并按序列阶段保留信息；局部压缩收益不能外推到任意模态、长度或 backend。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.16439v1 §3 KVCapsule — mechanism boundary: Vision-Language Models (VLMs) have emerged as a critical and fast-growing extension of Large Language Models (LLMs) that enable multimodal reasoning through both text and image inputs.`。

Evaluation：`https://arxiv.org/html/2605.16439v1 §4–§5 Evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.16439v1 §6 Conclusion and disclosed model/workload boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.16439v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-16439:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-16439:end -->
<!-- review:SF-2026-ARXIV-2605-16439:end -->

<!-- review:SF-2026-ARXIV-2605-16508:start -->
#### The Scaling Laws of Skills in LLM Agent Systems

问题与约束：As agent systems scale, skills accumulate into large reusable libraries, yet their scaling laws remain poorly understood.

机制与 ownership：Across 15 frontier LLMs, 1,141 real-world skills, and over 3M routing or execution decisions, we identify two coupled laws.

Evaluation contract：A single parameter, the routing logarithmic decay slope $b$, couples the two laws: routing-side fits predict execution-side rescue across models, showing that the same library property controls both pre-execution collapse and downstream recoverability.

Trade-off / failure：The mechanism described in `§§3–6 setup, execution law and skill-library law` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `§7 Discussion` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-16508:start -->`The Scaling Laws of Skills in LLM Agent Systems` is supported only under the v1-disclosed workload and evaluator behind `§§3 and 6 experimental setup and auto-manager evaluation`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-16508:end -->

Books Decision=`No Change — Existing Coverage`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-16508`。
<!-- review:SF-2026-ARXIV-2605-16508:end -->

<!-- review:SF-2026-ARXIV-2605-16565:start -->
#### Skim: Speculative Execution for Fast and Efficient Web Agents

问题与约束：Skim is a speculative execution framework for web agents that exploits the predictable structure of purpose-built websites.

机制与 ownership：Today's web-agent expense is not intrinsic to the tasks but a property of how agents are composed: frontier-model inference, browser rendering, and ReAct-style planning are applied to every step of every task regardless of complexity.

Evaluation contract：Across standard web-agent benchmarks paired with three backboneagents (WebVoyager, AgentOccam, BrowserUse), Skim reduces median per-task cost by 1.9x and latency by 33.4% with no accuracy loss.

Trade-off / failure：The mechanism described in `3 Design of Accio` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `3.4 Query Support and Deployment Discussion` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-16565:start -->`Skim: Speculative Execution for Fast and Efficient Web Agents` is supported only under the v1-disclosed workload and evaluator behind `5 Evaluation`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-16565:end -->

Books Decision=`No Change — Existing Coverage`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-16565`。
<!-- review:SF-2026-ARXIV-2605-16565:end -->

<!-- review:SF-2026-ARXIV-2605-16604:start -->
#### R2V Agent: Teaching SLMs When to Ask for Help

问题与约束：Existing LLM cascades usually route whole queries before execution, but task difficulty shifts mid-trajectory - after flaky tool calls, truncated observations, or compounding local errors - making pre-execution routing brittle.

机制与 ownership：We introduce \textbf{R2V-Agent}, a risk-calibrated SLM-LLM routing framework for interactive agents.

Evaluation contract：Across HumanEval+, TextWorld, and TerminalBench with four SLM backbones, R2V improves the reliability-cost frontier: it achieves $94.3\%$ HumanEval+ success with $0.60\%$ LLM escalation, recovers TextWorld from $64.6\%$ SLM-only success to $98.2\%$ at $41.7\%$ escalation, and reaches $93.3\%$ TerminalBench success at $33.9\%$ LLM calls, roughly half the heuristic-router cost.

Trade-off / failure：The mechanism described in `§4 Risk-Calibrated Routing and Verifier Distillation` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `§6 Conclusion; no dedicated limitations heading` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-16604:start -->`R2V Agent: Teaching SLMs When to Ask for Help` is supported only under the v1-disclosed workload and evaluator behind `§5 Experiments`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-16604:end -->

Books Decision=`No Change — Existing Coverage`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-16604`。
<!-- review:SF-2026-ARXIV-2605-16604:end -->

<!-- review:SF-2026-ARXIV-2605-16616:start -->
#### MLReplicate: Benchmarking Autonomous Research Systems for Machine Learning Reproducibility

问题与约束：Autonomous research systems capable of generating complete scientific manuscripts have advanced rapidly, yet robust and realistic evaluation frameworks have failed to keep pace.

机制与 ownership：To bridge this gap, we introduce MLReplicate, an end-to-end benchmark evaluating autonomous research systems on machine learning reproducibility.

Evaluation contract：To bridge this gap, we introduce MLReplicate, an end-to-end benchmark evaluating autonomous research systems on machine learning reproducibility.

Trade-off / failure：The mechanism described in `§§1–2 task construction and system adaptation` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `§5 Limitations and Future Work` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-16616:start -->`MLReplicate: Benchmarking Autonomous Research Systems for Machine Learning Reproducibility` is supported only under the v1-disclosed workload and evaluator behind `§3 Evaluation and Results`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-16616:end -->

Books Decision=`No Change — Existing Coverage`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-16616`。
<!-- review:SF-2026-ARXIV-2605-16616:end -->

<!-- review:SF-2026-ARXIV-2605-16626:start -->
#### SLEIGHT-Bench: A Benchmark of Evasion Attacks Against Agent Monitors

问题与约束：To better understand the limitations of such monitors against the diverse attack strategies that a coding agent could use, we present SLEIGHT-Bench (Subtle Low-itEration Insight-Guided Harmful Transcripts), a benchmark of synthetic transcripts containing 40 attacks across 11 categories, each showing a coding agent covertly pursuing a harmful objective (e.g.

机制与 ownership：To better understand the limitations of such monitors against the diverse attack strategies that a coding agent could use, we present SLEIGHT-Bench (Subtle Low-itEration Insight-Guided Harmful Transcripts), a benchmark of synthetic transcripts containing 40 attacks across 11 categories, each showing a coding agent covertly pursuing a harmful objective (e.g.

Evaluation contract：To better understand the limitations of such monitors against the diverse attack strategies that a coding agent could use, we present SLEIGHT-Bench (Subtle Low-itEration Insight-Guided Harmful Transcripts), a benchmark of synthetic transcripts containing 40 attacks across 11 categories, each showing a coding agent covertly pursuing a harmful objective (e.g.

Trade-off / failure：The mechanism described in `§§2–3 transcript properties and dataset construction` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `§7 Limitations` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-16626:start -->`SLEIGHT-Bench: A Benchmark of Evasion Attacks Against Agent Monitors` is supported only under the v1-disclosed workload and evaluator behind `§§4–5 experimental setup and results`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-16626:end -->

Books Decision=`No Change — Existing Coverage`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-16626`。
<!-- review:SF-2026-ARXIV-2605-16626:end -->

<!-- review:SF-2026-ARXIV-2605-16630:start -->
#### PrivScope: Task-scoped Disclosure Control for Hybrid Agentic Systems

问题与约束：Existing solutions either isolate workflows to limit cross-workflow leakage or apply general-purpose sanitization that does not reason over LC-assembled payload scope.

机制与 ownership：We present \textsc{PrivScope}, a trusted on-device payload governor that enforces \emph{task-scoped disclosure} at the local--CLM boundary, without requiring cloud-side changes.

Evaluation contract：Gains hold across five local backbones and add only seconds of on-device latency on commodity hardware.

Trade-off / failure：The mechanism described in `§IV PrivScope` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `§VI Conclusion; no dedicated limitations heading` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-16630:start -->`PrivScope: Task-scoped Disclosure Control for Hybrid Agentic Systems` is supported only under the v1-disclosed workload and evaluator behind `§V Evaluation`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-16630:end -->

Books Decision=`No Change — Existing Coverage`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-16630`。
<!-- review:SF-2026-ARXIV-2605-16630:end -->

<!-- review:SF-2026-ARXIV-2605-16637:start -->
#### HexAGenT: Efficient Agentic LLM Serving via Workflow- and Heterogeneity-Aware Scheduling

问题与约束：Agentic LLM applications increasingly execute user requests as multi-step workflows involving planning, tool use, branching, refinement, and synthesis.

机制与 ownership：To solve this problem, we present HexAGenT, a workflow-aware scheduler for a heterogeneous prefill-decode inference service.

Evaluation contract：Across representative agentic workloads and heterogeneous A100/H100/H200 clusters, HexAGenT reduces the SLO scale required for timely workflow completion by an average of 20.1% at 95% attainment and 33.0% at 99% attainment, with maximum reductions of 45.0% and 80.5%, respectively.

Trade-off / failure：The mechanism described in `4 System Overview` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `8 Conclusion` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-16637:start -->`HexAGenT: Efficient Agentic LLM Serving via Workflow- and Heterogeneity-Aware Scheduling` is supported only under the v1-disclosed workload and evaluator behind `7 Evaluation`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-16637:end -->

Books Decision=`No Change — Existing Coverage`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-16637`。
<!-- review:SF-2026-ARXIV-2605-16637:end -->

<!-- review:SF-2026-ARXIV-2605-16650:start -->
#### SKG-Eval: Stateful Evaluation of Multi-Turn Dialogue via Incremental Semantic Knowledge Graphs

问题与约束：Existing automatic evaluators, including LLM-as-a-judge frameworks and embedding-based metrics, largely rely on flat or turn-isolated representations, making them less effective at detecting long-range issues such as contradiction, topic drift, and entity inconsistency.

机制与 ownership：To address this, we propose SKG-Eval, a quasi-deterministic and interpretable framework that models dialogue as an evolving Semantic Knowledge Graph (SKG) of entities, relations, and commitments across turns.

Evaluation contract：Across multiple benchmarks, SKG-Eval achieves higher correlation with human judgments and substantially improves detection of long-range inconsistencies in extended conversations.

Trade-off / failure：The mechanism described in `§4 SKG-Eval` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `§5.10 Discussion and Limitations` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-16650:start -->`SKG-Eval: Stateful Evaluation of Multi-Turn Dialogue via Incremental Semantic Knowledge Graphs` is supported only under the v1-disclosed workload and evaluator behind `§5 Experiments`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-16650:end -->

Books Decision=`No Change — Existing Coverage`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-16650`。
<!-- review:SF-2026-ARXIV-2605-16650:end -->

<!-- review:SF-2026-ARXIV-2605-16704:start -->
#### Convex Dataset Valuation for Post-Training

问题与约束：In practice, however, developers face constraints on compute, labeling, and licensing costs that preclude using all available data, necessitating principled dataset-level selection.

机制与 ownership：To address this, we propose a scalable convex dataset-level valuation method based on kernel mean matching (KMM) in gradient space, which jointly accounts for alignment with the target task and redundancy across auxiliary datasets.

Evaluation contract：We first show that commonly used gradient alignment scores provide a reasonable yet incomplete valuation signal, as they ignore redundancy among datasets.

Trade-off / failure：The mechanism described in `§3 Dataset-Valuation Methodology` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `§3.1 Limitations` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-16704:start -->`Convex Dataset Valuation for Post-Training` is supported only under the v1-disclosed workload and evaluator behind `§§3.3–4 analysis and experiments`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-16704:end -->

Books Decision=`No Change — Existing Coverage`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-16704`。
<!-- review:SF-2026-ARXIV-2605-16704:end -->

<!-- review:SF-2026-ARXIV-2605-16712:start -->
#### Recall Isn't Enough: Bounding Commitments in Personalized Language Systems

问题与约束：Long-context and memory systems usually treat personalization as a recall problem.

机制与 ownership：We introduce Contract-Bounded Evidence Activation (CBEA) with Lexicographic Commitment Validation (LCV).

Evaluation contract：The result is a bounded operating point: explicit commitment control and 74-75% lower median input payload, not universal memory dominance.

Trade-off / failure：The mechanism described in `4 CBEA and LCV Runtime Algorithm` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `8 Discussion` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-16712:start -->`Recall Isn't Enough: Bounding Commitments in Personalized Language Systems` is supported only under the v1-disclosed workload and evaluator behind `5 Evaluation and Benchmark Protocol`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-16712:end -->

Books Decision=`Integrate`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-16712`。
<!-- review:SF-2026-ARXIV-2605-16712:end -->

<!-- review:SF-2026-ARXIV-2605-16725:start -->
#### Baba in Wonderland: Online Self-Supervised Dynamics Discovery for Executable World Models

问题与约束：Executable world models can be read, edited, executed, and reused for planning, but only if the program captures the environment's transition law rather than semantic shortcuts in its surface vocabulary.

机制与 ownership：We introduce Alice, a closed-loop system that treats failed candidate updates as structural signal: when a candidate explains a new transition but loses previously explained ones, the preservation conflict reveals dynamics that the current program had conflated.

Evaluation contract：We evaluate Alice on Baba in Wonderland, a prior-misaligned variant of Baba Is You that preserves simulator dynamics while replacing semantically meaningful rule-property labels with unrelated words.

Trade-off / failure：The mechanism described in `4 Method` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `6 Conclusion` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-16725:start -->`Baba in Wonderland: Online Self-Supervised Dynamics Discovery for Executable World Models` is supported only under the v1-disclosed workload and evaluator behind `5 Experiments`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-16725:end -->

Books Decision=`No Change — Existing Coverage`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-16725`。
<!-- review:SF-2026-ARXIV-2605-16725:end -->

<!-- review:SF-2026-ARXIV-2605-16745:start -->
#### EVA01: Unified Native 3D Understanding and Generation via Mixture-of-Transformers

问题与机制：EVA01: Unified Native 3D Understanding and Generation via Mixture-of-Transformers 提出的具体变化是：We introduce EVA01, a unified framework that extends the modality boundary of MLLMs to natively incorporate 3D mesh understanding, generation, and context-aware editing. 摘要中的长期系统挑战为：native 3D tokens join understanding and generation rather than remaining a stateless reconstruction sidecar。它可能改变 `MULTIMODAL-REPRESENTATION` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“Results show that EVA01 achieves state-of-the-art native text-to-3D generation fidelity and unlocks robust long-context multi-turn geometric editing with identity preservation, a capability fundamentally inaccessible to stateless reconstruction pipelines.”暂不作为最终证据。

Evaluation contract：Results show that EVA01 achieves state-of-the-art native text-to-3D generation fidelity and unlocks robust long-context multi-turn geometric editing with identity preservation, a capability fundamentally inaccessible to stateless reconstruction pipelines.

Evidence locators：Method=`section 3 Methodology (§3 Methodology)`；Evaluation=`section 4 Experiments (§4 Experiments)`；Counterevidence=`section 5 Limitations, Discussion & Future Work (§5 Limitations, Discussion & Future Work)`。

Trade-off / failure：新增 controller、metadata、verification、communication 或 runtime state 都带来成本；只在 exact-v1 披露 workload/evaluator 内成立，未披露的硬件、精度、长度、batch、并发、SLO、seed 与 artifact commit 为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-16745:start -->只支持 exact-v1 披露设置中的机制与结果；旧路径在新增 owner/证据/控制责任不成立时继续共存。<!-- claim:SF-2026-ARXIV-2605-16745:end -->

Books Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-16745:end -->

<!-- review:SF-2026-ARXIV-2605-16746:start -->
#### State Contamination in Memory-Augmented LLM Agents

问题与机制：State Contamination in Memory-Augmented LLM Agents 提出的具体变化是：To measure this hidden influence, we introduce the sub-threshold propagation gap (SPG), which quantifies downstream behavioral differences conditioned on memory states that a deployed monitor would classify as safe. 摘要中的长期系统挑战为：persistent memory becomes a cross-turn attack surface whose writes and reuse require separate authority。它可能改变 `AGENT-MEMORY` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“These results suggest that safety in memory-augmented agents should be treated as a state-control problem over evolving context, with sanitization applied before unsafe information is compressed into persistent memory.”暂不作为最终证据。

Evaluation contract：We further find that mitigation depends critically on intervention placement.

Evidence locators：Method=`section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt)`；Evaluation=`Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only`；Counterevidence=`Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup`。

Trade-off / failure：新增 controller、metadata、verification、communication 或 runtime state 都带来成本；只在 exact-v1 披露 workload/evaluator 内成立，未披露的硬件、精度、长度、batch、并发、SLO、seed 与 artifact commit 为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-16746:start -->只支持 exact-v1 披露设置中的机制与结果；旧路径在新增 owner/证据/控制责任不成立时继续共存。<!-- claim:SF-2026-ARXIV-2605-16746:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-16746:end -->

<!-- review:SF-2026-ARXIV-2605-16776:start -->
#### Distinguishable Deletion: Unifying Knowledge Erasure and Refusal for Large Language Model Unlearning

问题与机制：Distinguishable Deletion: Unifying Knowledge Erasure and Refusal for Large Language Model Unlearning 提出的具体变化是：To address these issues, we propose Distinguishable Deletion ($\mathrm{D^2}$), a paradigm that restricts the response distribution in the latent representation rather than specific tokens to erase undesirable knowledge, while distinguishing it from retained knowledge, enabling a refusal mechanism to handle unlearned inputs safely and coherently. 摘要中的长期系统挑战为：unlearning must distinguish parameter erasure from inference-time refusal and verify both contracts。它可能改变 `PLATFORM-SECURITY` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“Extensive experiments demonstrate that EUA significantly outperforms previous methods, indicating the superiority of $\mathrm{D^2}$.”暂不作为最终证据。

Evaluation contract：Extensive experiments demonstrate that EUA significantly outperforms previous methods, indicating the superiority of $\mathrm{D^2}$.

Evidence locators：Method=`section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt)`；Evaluation=`Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only`；Counterevidence=`Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup`。

Trade-off / failure：新增 controller、metadata、verification、communication 或 runtime state 都带来成本；只在 exact-v1 披露 workload/evaluator 内成立，未披露的硬件、精度、长度、batch、并发、SLO、seed 与 artifact commit 为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-16776:start -->只支持 exact-v1 披露设置中的机制与结果；旧路径在新增 owner/证据/控制责任不成立时继续共存。<!-- claim:SF-2026-ARXIV-2605-16776:end -->

Books Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-16776:end -->

<!-- review:SF-2026-ARXIV-2605-16786:start -->
#### Lever: Speculative LLM Inference on Smartphones

问题与机制：Lever: Speculative LLM Inference on Smartphones 提出的具体变化是：We present Lever, an end-to-end system for efficient flash-backed LLM inference on smartphones. 摘要中的长期系统挑战为：flash-backed mobile inference changes the draft/verify cost model and state-placement boundary。它可能改变 `INFER-SPECULATIVE-DECODING` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“We observe that speculative decoding is a natural fit for this setting: a small draft model can remain in DRAM, while a larger flash-resident target model verifies multiple candidate tokens per invocation.”暂不作为最终证据。

Evaluation contract：Comprehensive evaluations show that Lever reduces inference latency by an average of 2.93x over baseline flash-offloaded inference and 1.50x over conventional speculative decoding, narrowing the latency gap between flash-backed and memory-resident LLM inference.

Evidence locators：Method=`section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt)`；Evaluation=`Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only`；Counterevidence=`Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup`。

Trade-off / failure：新增 controller、metadata、verification、communication 或 runtime state 都带来成本；只在 exact-v1 披露 workload/evaluator 内成立，未披露的硬件、精度、长度、batch、并发、SLO、seed 与 artifact commit 为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-16786:start -->只支持 exact-v1 披露设置中的机制与结果；旧路径在新增 owner/证据/控制责任不成立时继续共存。<!-- claim:SF-2026-ARXIV-2605-16786:end -->

Books Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-16786:end -->

<!-- review:SF-2026-ARXIV-2605-16787:start -->
#### The Unlearnability Phenomenon in RLVR for Language Models

问题与机制：The Unlearnability Phenomenon in RLVR for Language Models 提出的具体变化是：Reinforcement Learning with Verifiable Reward (RLVR) has proven effective in improving Large Language Model's (LLM) reasoning ability. 摘要中的长期系统挑战为：RLVR admission must recognize examples with no useful policy-gradient direction rather than treating all verified rewards alike。它可能改变 `TRAIN-GRPO` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“With cross-example gradient analysis, we show that unlearnable examples have fundamental representation issue, characterized by low gradient similarity with the rest of the examples and ungeneralizable reasoning patterns.”暂不作为最终证据。

Evaluation contract：We further show that representation flaws are difficult to mitigate in RL, as data augmentation does not improve gradient similarity.

Evidence locators：Method=`section 3.1 Training Algorithm (§3.1 Training Algorithm)`；Evaluation=`Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only`；Counterevidence=`section 6 Discussion (§6 Discussion)`。

Trade-off / failure：新增 controller、metadata、verification、communication 或 runtime state 都带来成本；只在 exact-v1 披露 workload/evaluator 内成立，未披露的硬件、精度、长度、batch、并发、SLO、seed 与 artifact commit 为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-16787:start -->只支持 exact-v1 披露设置中的机制与结果；旧路径在新增 owner/证据/控制责任不成立时继续共存。<!-- claim:SF-2026-ARXIV-2605-16787:end -->

Books Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-16787:end -->

<!-- review:SF-2026-ARXIV-2605-16790:start -->
#### TIER: Trajectory-Invariant Execution Rewards for Multi-Step Tool Composition

问题与机制：TIER: Trajectory-Invariant Execution Rewards for Multi-Step Tool Composition 提出的具体变化是：We propose TIER: Trajectory-Invariant Execution Rewards, a reward framework that derives supervision directly from function schemas and runtime execution, rather than from reference trajectories. 摘要中的长期系统挑战为：tool-composition reward moves from reference trajectories to invariant execution-state evidence。它可能改变 `AGENT-TOOL-CALLING` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“Ablation studies confirm that all reward components are necessary, highlighting the importance of multi-level supervision for compositional reasoning.”暂不作为最终证据。

Evaluation contract：We further demonstrate consistent gains on benchmarks like BFCL v3 and NestFUL.

Evidence locators：Method=`section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt)`；Evaluation=`Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only`；Counterevidence=`Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup`。

Trade-off / failure：新增 controller、metadata、verification、communication 或 runtime state 都带来成本；只在 exact-v1 披露 workload/evaluator 内成立，未披露的硬件、精度、长度、batch、并发、SLO、seed 与 artifact commit 为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-16790:start -->只支持 exact-v1 披露设置中的机制与结果；旧路径在新增 owner/证据/控制责任不成立时继续共存。<!-- claim:SF-2026-ARXIV-2605-16790:end -->

Books Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-16790:end -->

<!-- review:SF-2026-ARXIV-2605-16819:start -->
#### AgentKernelArena: Generalization-Aware Benchmarking of GPU Kernel Optimization Agents

问题与机制：AgentKernelArena: Generalization-Aware Benchmarking of GPU Kernel Optimization Agents 提出的具体变化是：We present AgentKernelArena, an open-source benchmark for measuring AI coding agents on GPU kernel optimization. 摘要中的长期系统挑战为：agent evaluation must freeze workflow state, hidden task contract, runtime receipts and unseen-shape generalization。它可能改变 `PLATFORM-EVALUATION-SYSTEM` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“AgentKernelArena is designed as a modular, extensible framework for rigorous evaluation of agentic GPU kernel optimization across agents, tasks, and hardware targets.”暂不作为最终证据。

Evaluation contract：AgentKernelArena is designed as a modular, extensible framework for rigorous evaluation of agentic GPU kernel optimization across agents, tasks, and hardware targets.

Evidence locators：Method=`section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt)`；Evaluation=`Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only`；Counterevidence=`Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup`。

Trade-off / failure：新增 controller、metadata、verification、communication 或 runtime state 都带来成本；只在 exact-v1 披露 workload/evaluator 内成立，未披露的硬件、精度、长度、batch、并发、SLO、seed 与 artifact commit 为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-16819:start -->只支持 exact-v1 披露设置中的机制与结果；旧路径在新增 owner/证据/控制责任不成立时继续共存。<!-- claim:SF-2026-ARXIV-2605-16819:end -->

Books Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-16819:end -->

<!-- review:SF-2026-ARXIV-2605-16826:start -->
#### Decoupling KL and Trajectories: A Unified Perspective for SFT, DAgger, Offline RL, and OPD in LLM Distillation

问题与机制：Decoupling KL and Trajectories: A Unified Perspective for SFT, DAgger, Offline RL, and OPD in LLM Distillation 提出的具体变化是：Motivated by these findings, we propose KL mixing and an entropy-gated length curriculum. 摘要中的长期系统挑战为：distillation outcomes depend separately on prefix provenance and KL direction, changing the training contract。它可能改变 `TRAIN-PRETRAINING` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“Our results provide a framework and practical methods for designing reasoning distillation objectives that balance accuracy, diversity, compute, and RL behavior.”暂不作为最终证据。

Evaluation contract：We show that the prevailing paradigms, off-policy distillation and on-policy distillation (OPD), implicitly couple two orthogonal choices: prefix source and token-level KL direction.

Evidence locators：Method=`section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt)`；Evaluation=`Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only`；Counterevidence=`Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup`。

Trade-off / failure：新增 controller、metadata、verification、communication 或 runtime state 都带来成本；只在 exact-v1 披露 workload/evaluator 内成立，未披露的硬件、精度、长度、batch、并发、SLO、seed 与 artifact commit 为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-16826:start -->只支持 exact-v1 披露设置中的机制与结果；旧路径在新增 owner/证据/控制责任不成立时继续共存。<!-- claim:SF-2026-ARXIV-2605-16826:end -->

Books Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-16826:end -->

<!-- review:SF-2026-ARXIV-2605-16839:start -->
#### CompactAttention: Accelerating Chunked Prefill with Block-Union KV Selection

问题与机制：CompactAttention: Accelerating Chunked Prefill with Block-Union KV Selection 提出的具体变化是：To address these limitations, we propose CompactAttention, a chunked-prefill attention mechanism based on Block-Union KV Selection. 摘要中的长期系统挑战为：chunked prefill reuses a union of selected KV blocks while preserving the dense attention owner。它可能改变 `INFER-PREFILL` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“On LLaMA-3.1-8B-Instruct, CompactAttention maintains accuracy close to dense attention on the RULER benchmark while delivering up to 2.72$\times$ attention speedup at 128K context length under chunked prefill.”暂不作为最终证据。

Evaluation contract：On LLaMA-3.1-8B-Instruct, CompactAttention maintains accuracy close to dense attention on the RULER benchmark while delivering up to 2.72$\times$ attention speedup at 128K context length under chunked prefill.

Evidence locators：Method=`section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt)`；Evaluation=`Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only`；Counterevidence=`Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup`。

Trade-off / failure：新增 controller、metadata、verification、communication 或 runtime state 都带来成本；只在 exact-v1 披露 workload/evaluator 内成立，未披露的硬件、精度、长度、batch、并发、SLO、seed 与 artifact commit 为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-16839:start -->只支持 exact-v1 披露设置中的机制与结果；旧路径在新增 owner/证据/控制责任不成立时继续共存。<!-- claim:SF-2026-ARXIV-2605-16839:end -->

Books Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-16839:end -->

<!-- review:SF-2026-ARXIV-2605-16867:start -->
#### GoodServe: Towards High-Goodput Serving of Agentic LLM Inferences over Heterogeneous Resources

问题与机制：In this paper, we propose GoodServe, a goodput-optimized serving system for agentic inferences over heterogeneous resources.

Evaluation contract：Our evaluations show that GoodServe improves goodput by up to 27.4% over existing routing methods.

Evidence locators：Method=`section 2.2 Lessons Learned from Existing Request-routing Methods (§2.2 Lessons Learned from Existing Request-routing Methods)`；Evaluation=`section 4 Evaluation (§4 Evaluation)`；Counterevidence=`section 5 Additional Related Works and Discussions (§5 Additional Related Works and Discussions)`。

Trade-off / failure：新增 controller、metadata、verification、communication 或 runtime state 都带来成本；只在 exact-v1 披露 workload/evaluator 内成立，未披露的硬件、精度、长度、batch、并发、SLO、seed 与 artifact commit 为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-16867:start -->只支持 exact-v1 披露设置中的机制与结果；旧路径在新增 owner/证据/控制责任不成立时继续共存。<!-- claim:SF-2026-ARXIV-2605-16867:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-16867:end -->

<!-- review:SF-2026-ARXIV-2605-16928:start -->
#### Full Attention Strikes Back: Transferring Full Attention into Sparse within Hundred Training Steps

问题与机制：Full Attention Strikes Back: Transferring Full Attention into Sparse within Hundred Training Steps 提出的具体变化是：Based on these insights, we propose RTPurbo, which retains the full KV cache only for retrieval heads and introduces a lightweight token indexer for sparse attention. 摘要中的长期系统挑战为：head-aware dense-to-sparse post-training separates candidate routing from exact attention。它可能改变 `INFER-KV-CACHE` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“These results suggest that strong sparse inference can be obtained from standard full-attention training without expensive native sparse pretraining.”暂不作为最终证据。

Evaluation contract：Experiments on long-context benchmarks and reasoning tasks show that RTPurbo preserves near-lossless accuracy while delivering substantial efficiency gains, including up to a 9.36$\times$ prefill speedup at 1M context and about a 2.01$\times$ decode speedup.

Evidence locators：Method=`section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt)`；Evaluation=`Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only`；Counterevidence=`Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup`。

Trade-off / failure：新增 controller、metadata、verification、communication 或 runtime state 都带来成本；只在 exact-v1 披露 workload/evaluator 内成立，未披露的硬件、精度、长度、batch、并发、SLO、seed 与 artifact commit 为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-16928:start -->只支持 exact-v1 披露设置中的机制与结果；旧路径在新增 owner/证据/控制责任不成立时继续共存。<!-- claim:SF-2026-ARXIV-2605-16928:end -->

Books Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-16928:end -->

<!-- review:SF-2026-ARXIV-2605-16976:start -->
#### Securing LLM Agents Need Intent-to-Execution Integrity

问题与机制：Drawing on this analogy, we identify two fundamental problem sources -- untrusted data ingestion and untrusted tool execution -- and derive four integrity properties that must hold simultaneously: \emph{Tool Integrity}, \emph{Instruction Integrity}, \emph{Judgment Integrity}, and \emph{Data Flow Integrity}.

Evaluation contract：Analyzing existing agentic defenses against these properties reveals that current systems provide only partial and non-compositional coverage, leaving fundamental gaps in securing modern LLM agents.

Evidence locators：Method=`section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt)`；Evaluation=`Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only`；Counterevidence=`Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup`。

Trade-off / failure：新增 controller、metadata、verification、communication 或 runtime state 都带来成本；只在 exact-v1 披露 workload/evaluator 内成立，未披露的硬件、精度、长度、batch、并发、SLO、seed 与 artifact commit 为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-16976:start -->只支持 exact-v1 披露设置中的机制与结果；旧路径在新增 owner/证据/控制责任不成立时继续共存。<!-- claim:SF-2026-ARXIV-2605-16976:end -->

Books Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-16976:end -->

<!-- review:SF-2026-ARXIV-2605-16986:start -->
#### Skills on the Fly: Test-Time Adaptive Skill Synthesis for LLM Agents

问题与机制：Skills on the Fly: Test-Time Adaptive Skill Synthesis for LLM Agents 提出的具体变化是：We call this challenge test-time compute-to-capability conversion and propose SkillTTA, which retrieves task-relevant training trajectories and synthesizes a temporary skill conditioned on the visible target context for a solver with fixed parameters. 摘要中的长期系统挑战为：test-time skill synthesis creates ephemeral executable state that needs admission, expiry and rollback。它可能改变 `AGENT-PLATFORM` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“Across ALFWorld, SpreadsheetBench, BigCodeBench, and WebShop, SkillTTA outperforms state-of-the-art reuse and optimization baselines.”暂不作为最终证据。

Evaluation contract：It attains a higher performance ceiling at lower compute cost than baseline reuse and sampling strategies.

Evidence locators：Method=`section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt)`；Evaluation=`Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only`；Counterevidence=`Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup`。

Trade-off / failure：新增 controller、metadata、verification、communication 或 runtime state 都带来成本；只在 exact-v1 披露 workload/evaluator 内成立，未披露的硬件、精度、长度、batch、并发、SLO、seed 与 artifact commit 为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-16986:start -->只支持 exact-v1 披露设置中的机制与结果；旧路径在新增 owner/证据/控制责任不成立时继续共存。<!-- claim:SF-2026-ARXIV-2605-16986:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-16986:end -->

<!-- review:SF-2026-ARXIV-2605-17003:start -->
#### Learning-Zone Energy: Online Data Selection for Efficient RL Post-Training

问题与机制：Learning-Zone Energy: Online Data Selection for Efficient RL Post-Training 提出的具体变化是：To address this fundamental inefficiency, we propose Learning-Zone Energy (LZE), a theoretically grounded, fully online data selection framework that concentrates computation on the model's active learning frontier. 摘要中的长期系统挑战为：online RL data selection becomes a control loop over current policy frontier rather than a static dataset。它可能改变 `TRAIN-DATA` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“Our code is available at https://github.com/Stellaris167/LZE.”暂不作为最终证据。

Evaluation contract：Our code is available at https://github.com/Stellaris167/LZE.

Evidence locators：Method=`section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt)`；Evaluation=`Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only`；Counterevidence=`Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup`。

Trade-off / failure：新增 controller、metadata、verification、communication 或 runtime state 都带来成本；只在 exact-v1 披露 workload/evaluator 内成立，未披露的硬件、精度、长度、batch、并发、SLO、seed 与 artifact commit 为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-17003:start -->只支持 exact-v1 披露设置中的机制与结果；旧路径在新增 owner/证据/控制责任不成立时继续共存。<!-- claim:SF-2026-ARXIV-2605-17003:end -->

Books Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-17003:end -->

<!-- review:SF-2026-ARXIV-2605-17026:start -->
#### Why Do Reasoning Models Lose Coverage? The Role of Data and Forks in the Road

问题与机制：While these methods reliably improve pass@1 accuracy, prior works have observed that they show a coverage shrinkage behavior, where pass@k degrades relative to the base model.

Evaluation contract：We also demonstrate that this shrinkage behavior can be partially mitigated through targeted data synthesis design of decision-points, and a more systematic diversity-encouraging decoding mechanism.

Evidence locators：Method=`section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt)`；Evaluation=`Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only`；Counterevidence=`Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup`。

Trade-off / failure：新增 controller、metadata、verification、communication 或 runtime state 都带来成本；只在 exact-v1 披露 workload/evaluator 内成立，未披露的硬件、精度、长度、batch、并发、SLO、seed 与 artifact commit 为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-17026:start -->只支持 exact-v1 披露设置中的机制与结果；旧路径在新增 owner/证据/控制责任不成立时继续共存。<!-- claim:SF-2026-ARXIV-2605-17026:end -->

Books Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-17026:end -->

<!-- review:SF-2026-ARXIV-2605-17028:start -->
#### PARALLAX: Separating Genuine Hallucination Detection from Benchmark Construction Artifacts

问题与机制：We show, however, that much of this apparent progress does not survive scrutiny.

Evaluation contract：To measure what genuine detection capability remains once these artifacts are controlled, we conduct a large-scale evaluation spanning twenty-two detection methods, twelve open-source models spanning six architectural families, and six corpora.

Evidence locators：Method=`section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt)`；Evaluation=`Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only`；Counterevidence=`Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup`。

Trade-off / failure：新增 controller、metadata、verification、communication 或 runtime state 都带来成本；只在 exact-v1 披露 workload/evaluator 内成立，未披露的硬件、精度、长度、batch、并发、SLO、seed 与 artifact commit 为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-17028:start -->只支持 exact-v1 披露设置中的机制与结果；旧路径在新增 owner/证据/控制责任不成立时继续共存。<!-- claim:SF-2026-ARXIV-2605-17028:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-17028:end -->

<!-- review:SF-2026-ARXIV-2605-17034:start -->
#### Privacy Policy Enforcement Guardrails for Data-Sensitive Retrieval-Augmented Generation

问题与机制：Privacy Policy Enforcement Guardrails for Data-Sensitive Retrieval-Augmented Generation 提出的具体变化是：We introduce a Privacy Policy Enforcement (PPE) framework using dual one-class density estimators with fused text embeddings and a calibrated abstain region for out-of-distribution inputs. 摘要中的长期系统挑战为：RAG privacy enforcement must mediate retrieval and generation effects rather than rely on prompt policy。它可能改变 `PLATFORM-SECURITY` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“This methodology provides a robust stress-testing standard for any synthetic-data-trained classifier.”暂不作为最终证据。

Evaluation contract：This methodology provides a robust stress-testing standard for any synthetic-data-trained classifier.

Evidence locators：Method=`section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt)`；Evaluation=`Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only`；Counterevidence=`Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup`。

Trade-off / failure：新增 controller、metadata、verification、communication 或 runtime state 都带来成本；只在 exact-v1 披露 workload/evaluator 内成立，未披露的硬件、精度、长度、batch、并发、SLO、seed 与 artifact commit 为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-17034:start -->只支持 exact-v1 披露设置中的机制与结果；旧路径在新增 owner/证据/控制责任不成立时继续共存。<!-- claim:SF-2026-ARXIV-2605-17034:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-17034:end -->

<!-- review:SF-2026-ARXIV-2605-17062:start -->
#### The Range Shrinks, the Threat Remains: Re-evaluating LLM Package Hallucinations on the 2026 Frontier-Model Cohort

问题与机制：The Range Shrinks, the Threat Remains: Re-evaluating LLM Package Hallucinations on the 2026 Frontier-Model Cohort 提出的具体变化是：Across 199,845 paired Python and JavaScript prompts validated against PyPI and npm master lists, we measure overall hallucination rates between 4.62% (Claude Haiku 4.5) and 6.10% (GPT-5.4-mini) -- an order-of-magnitude compression of the inter-model spread observed by Spracklen, but not a retirement of the threat. 摘要中的长期系统挑战为：package hallucinations create a model-to-software-supply-chain effect path requiring independent resolution。它可能改变 `PLATFORM-SECURITY` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“We further document a Python-over-JavaScript hallucination asymmetry that inverts Spracklen's 2024 finding, identify a Haiku-below-Sonnet inversion within the Anthropic family, and observe a Jaccard-similarity peak between DeepSeek V3.2 and GPT-5.4-mini (J = 0.343) suggestive of shared training-data origins.”暂不作为最终证据。

Evaluation contract：We further document a Python-over-JavaScript hallucination asymmetry that inverts Spracklen's 2024 finding, identify a Haiku-below-Sonnet inversion within the Anthropic family, and observe a Jaccard-similarity peak between DeepSeek V3.2 and GPT-5.4-mini (J = 0.343) suggestive of shared training-data origins.

Evidence locators：Method=`section 4 Replication Methodology (§4 Replication Methodology)`；Evaluation=`section 5 Results (§5 model/package-registry comparisons)`；Counterevidence=`section 8 Limitations (§8 Limitations)`。

Trade-off / failure：新增 controller、metadata、verification、communication 或 runtime state 都带来成本；只在 exact-v1 披露 workload/evaluator 内成立，未披露的硬件、精度、长度、batch、并发、SLO、seed 与 artifact commit 为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-17062:start -->只支持 exact-v1 披露设置中的机制与结果；旧路径在新增 owner/证据/控制责任不成立时继续共存。<!-- claim:SF-2026-ARXIV-2605-17062:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-17062:end -->

<!-- review:SF-2026-ARXIV-2605-17076:start -->
#### S-Bus: Automatic Read-Set Reconstruction for Multi-Agent LLM State Coordination

问题与机制：S-Bus: Automatic Read-Set Reconstruction for Multi-Agent LLM State Coordination 提出的具体变化是：S-Bus is an HTTP middleware whose central mechanism, a server-side DeliveryLog, reconstructs each agent's read set at commit time from observed HTTP GET traffic. 摘要中的长期系统挑战为：observable-read isolation gives shared mutable multi-agent state an explicit consistency boundary。它可能改变 `AGENT-MULTI-AGENT` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“Source code, formal proofs, harness, annotation data: https://github.com/sajjadanwar0/sbus”暂不作为最终证据。

Evaluation contract：Source code, formal proofs, harness, annotation data: https://github.com/sajjadanwar0/sbus

Evidence locators：Method=`section VII-M (§VII-M)`；Evaluation=`Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only`；Counterevidence=`Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup`。

Trade-off / failure：新增 controller、metadata、verification、communication 或 runtime state 都带来成本；只在 exact-v1 披露 workload/evaluator 内成立，未披露的硬件、精度、长度、batch、并发、SLO、seed 与 artifact commit 为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-17076:start -->只支持 exact-v1 披露设置中的机制与结果；旧路径在新增 owner/证据/控制责任不成立时继续共存。<!-- claim:SF-2026-ARXIV-2605-17076:end -->

Books Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-17076:end -->

<!-- review:SF-2026-ARXIV-2605-17106:start -->
#### HyDRA: Hybrid Dynamic Routing Architecture for Heterogeneous LLM Pools

问题与机制：HyDRA: Hybrid Dynamic Routing Architecture for Heterogeneous LLM Pools 提出的具体变化是：We present HyDRA (Hybrid Dynamic Routing Architecture), a framework that predicts fine-grained, multi-dimensional capability requirements per query and matches them against configuration-defined model profiles via shortfall matching. 摘要中的长期系统挑战为：heterogeneous model pools and routing policy become decoupled deployable revisions。它可能改变 `INFER-SCHEDULING` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“Results generalize across LiveCodeBench, BigCodeBench, and tau-bench.”暂不作为最终证据。

Evaluation contract：HyDRA is deployed to all users in GitHub Copilot's VS Code Chat auto-mode and -- to our knowledge for the first time in the LLM routing literature -- demonstrates language-invariant routing across CJK, European, and other script families.

Evidence locators：Method=`section 8 (§8)`；Evaluation=`Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only`；Counterevidence=`Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup`。

Trade-off / failure：新增 controller、metadata、verification、communication 或 runtime state 都带来成本；只在 exact-v1 披露 workload/evaluator 内成立，未披露的硬件、精度、长度、batch、并发、SLO、seed 与 artifact commit 为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-17106:start -->只支持 exact-v1 披露设置中的机制与结果；旧路径在新增 owner/证据/控制责任不成立时继续共存。<!-- claim:SF-2026-ARXIV-2605-17106:end -->

Books Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-17106:end -->

<!-- review:SF-2026-ARXIV-2605-17113:start -->
#### The Point of No Return: Counterfactual Localization of Deceptive Commitment in Language-Model Reasoning

问题与机制：We introduce counterfactual localization: for each sentence prefix in a reasoning trace, we fix the prefix, resample continuations, and estimate the probability of a deceptive outcome.

Evaluation contract：Using this resource, we show that lexical cues for commitment prediction transfer poorly across environments, whereas attention-based transition features generalize out of distribution, suggesting that deceptive commitment is reflected in reusable changes in reasoning dynamics rather than surface form.

Evidence locators：Method=`section 3 Methods (§3 Methods)`；Evaluation=`section 5 Experiments (§5 Experiments)`；Counterevidence=`section 7 Discussion and Limitations (§7 Discussion and Limitations)`。

Trade-off / failure：新增 controller、metadata、verification、communication 或 runtime state 都带来成本；只在 exact-v1 披露 workload/evaluator 内成立，未披露的硬件、精度、长度、batch、并发、SLO、seed 与 artifact commit 为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-17113:start -->只支持 exact-v1 披露设置中的机制与结果；旧路径在新增 owner/证据/控制责任不成立时继续共存。<!-- claim:SF-2026-ARXIV-2605-17113:end -->

Books Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-17113:end -->

<!-- review:SF-2026-ARXIV-2605-17160:start -->
#### When Bits Break Recourse: Counterfactual-Faithful Quantization

问题与机制：We propose two metrics: Validity Drop (VD), which measures the fraction of full-precision recourse actions that no longer achieve the target outcome after quantization, and Counterfactual Recourse Gap (CRG), which measures the increase in minimal recourse cost under the quantized model.

Evaluation contract：Experiments on Adult, German Credit, and COMPAS show that standard QAT and mixed-precision baselines can preserve accuracy while substantially degrading recourse stability.

Evidence locators：Method=`section 3 Counterfactual-Faithful Quantization (§3 CFQ)`；Evaluation=`section 4 Experiments (§4 ADULT, GERMAN CREDIT and COMPAS)`；Counterevidence=`section 6 Limitations (§6 validity boundary)`。

Trade-off / failure：新增 controller、metadata、verification、communication 或 runtime state 都带来成本；只在 exact-v1 披露 workload/evaluator 内成立，未披露的硬件、精度、长度、batch、并发、SLO、seed 与 artifact commit 为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-17160:start -->只支持 exact-v1 披露设置中的机制与结果；旧路径在新增 owner/证据/控制责任不成立时继续共存。<!-- claim:SF-2026-ARXIV-2605-17160:end -->

Books Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-17160:end -->

<!-- review:SF-2026-ARXIV-2605-17164:start -->
#### Charon: A Unified and Fine-Grained Simulator for Large-Scale LLM Training and Inference

问题与机制：Charon: A Unified and Fine-Grained Simulator for Large-Scale LLM Training and Inference 提出的具体变化是：To address this, we introduce Charon, a unified, modular, and fine-grained simulator for accurately predicting LLM performance. 摘要中的长期系统挑战为：training and inference what-if simulation need a shared configuration identity and validation contract。它可能改变 `PLATFORM-EVALUATION-SYSTEM` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“In a practical inference deployment case, Charon discovered a configuration that improved system throughput over an engineering-tuned baseline, demonstrating its significant real-world value.”暂不作为最终证据。

Evaluation contract：Experiments show Charon achieves high accuracy across different models and configurations, with an overall prediction error consistently under 5.35%, and even under 3.74% for training with a large-scale GPU cluster.

Evidence locators：Method=`section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt)`；Evaluation=`Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only`；Counterevidence=`Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup`。

Trade-off / failure：新增 controller、metadata、verification、communication 或 runtime state 都带来成本；只在 exact-v1 披露 workload/evaluator 内成立，未披露的硬件、精度、长度、batch、并发、SLO、seed 与 artifact commit 为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-17164:start -->只支持 exact-v1 披露设置中的机制与结果；旧路径在新增 owner/证据/控制责任不成立时继续共存。<!-- claim:SF-2026-ARXIV-2605-17164:end -->

Books Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-17164:end -->

<!-- review:SF-2026-ARXIV-2605-17169:start -->
#### Responsible Agentic AI Requires Explicit Provenance

问题与机制：Agentic AI is rapidly proliferating across diverse real-world domains such as software engineering, yet public trust has not kept pace.

Evaluation contract：We position that what is missing is not better benchmark-level evaluation but $\textbf{explicit provenance}$ across the full agentic lifecycle, which is the only viable basis for making responsibility computable and actionable.

Evidence locators：Method=`section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt)`；Evaluation=`Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only`；Counterevidence=`Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup`。

Trade-off / failure：新增 controller、metadata、verification、communication 或 runtime state 都带来成本；只在 exact-v1 披露 workload/evaluator 内成立，未披露的硬件、精度、长度、batch、并发、SLO、seed 与 artifact commit 为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-17169:start -->只支持 exact-v1 披露设置中的机制与结果；旧路径在新增 owner/证据/控制责任不成立时继续共存。<!-- claim:SF-2026-ARXIV-2605-17169:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-17169:end -->

<!-- review:SF-2026-ARXIV-2605-17170:start -->
#### TriAxialKV: Toward Extreme Low-Precision KV-Cache Quantization for Agentic Inference Tasks

问题与机制：TriAxialKV: Toward Extreme Low-Precision KV-Cache Quantization for Agentic Inference Tasks 提出的具体变化是：To this end, we introduce TriAxialKV, a novel mixed-precision KV-cache quantization scheme that assigns each token a triaxial tag, calibrates per-tag sensitivity, and allocates INT2/INT4 bitwidths under a fixed memory budget. 摘要中的长期系统挑战为：agentic KV quantization must condition precision on role, modality and temporal lifecycle。它可能改变 `INFER-KV-CACHE` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“As a result, their context exhibits structure that can carry different importance along three key axes: temporal recency to the current turn, modality such as text or image tokens, and semantic role such as user queries, tool calls, observations, or reasoning.”暂不作为最终证据。

Evaluation contract：As a result, their context exhibits structure that can carry different importance along three key axes: temporal recency to the current turn, modality such as text or image tokens, and semantic role such as user queries, tool calls, observations, or…

Evidence locators：Method=`section 49 (§49)`；Evaluation=`Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only`；Counterevidence=`Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup`。

Trade-off / failure：新增 controller、metadata、verification、communication 或 runtime state 都带来成本；只在 exact-v1 披露 workload/evaluator 内成立，未披露的硬件、精度、长度、batch、并发、SLO、seed 与 artifact commit 为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-17170:start -->只支持 exact-v1 披露设置中的机制与结果；旧路径在新增 owner/证据/控制责任不成立时继续共存。<!-- claim:SF-2026-ARXIV-2605-17170:end -->

Books Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-17170:end -->

<!-- review:SF-2026-ARXIV-2605-17172:start -->
#### OpenJarvis: Personal AI, On Personal Devices

问题与机制：OpenJarvis: Personal AI, On Personal Devices 提出的具体变化是：We present OpenJarvis, an architecture that represents a personal AI system as a typed spec over five primitives: Intelligence, Engine, Agents, Tools &amp; Memory, and Learning. 摘要中的长期系统挑战为：personal AI splits sensitive local state, local execution and optional cloud escalation into typed boundaries。它可能改变 `AGENT-PLATFORM` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“They also reduce marginal API cost by ~800x and end-to-end latency by 4x.”暂不作为最终证据。

Evaluation contract：They also reduce marginal API cost by ~800x and end-to-end latency by 4x.

Evidence locators：Method=`section 3 Methods (§3 Methods)`；Evaluation=`section 3.2 Evaluation Metrics (§3.2 Evaluation Metrics)`；Counterevidence=`section 5 Discussion and Conclusion (§5 Discussion and Conclusion)`。

Trade-off / failure：新增 controller、metadata、verification、communication 或 runtime state 都带来成本；只在 exact-v1 披露 workload/evaluator 内成立，未披露的硬件、精度、长度、batch、并发、SLO、seed 与 artifact commit 为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-17172:start -->只支持 exact-v1 披露设置中的机制与结果；旧路径在新增 owner/证据/控制责任不成立时继续共存。<!-- claim:SF-2026-ARXIV-2605-17172:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-17172:end -->

<!-- review:SF-2026-ARXIV-2605-17173:start -->
#### Why Do Safety Guardrails Degrade Across Languages?

问题与机制：Why Do Safety Guardrails Degrade Across Languages? 提出的具体变化是：We introduce a latent variable model, a Multi-Group Item Response Theory (IRT) framework, that decouples language-agnostic safety robustness ($θ$), intrinsic prompt hardness ($β$), global language processing difficulty ($γ$), and a prompt-specific cross-lingual safety gap ($τ$). 摘要中的长期系统挑战为：multilingual safety evaluation must decompose the failure factors hidden by aggregate jailbreak rate。它可能改变 `PLATFORM-EVALUATION-SYSTEM` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“Our framework reveals concept-language vulnerabilities that aggregate metrics obscure, enabling fairer cross-lingual safety evaluation and targeted improvements in dataset construction.”暂不作为最终证据。

Evaluation contract：Our framework reveals concept-language vulnerabilities that aggregate metrics obscure, enabling fairer cross-lingual safety evaluation and targeted improvements in dataset construction.

Evidence locators：Method=`section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt)`；Evaluation=`Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only`；Counterevidence=`Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup`。

Trade-off / failure：新增 controller、metadata、verification、communication 或 runtime state 都带来成本；只在 exact-v1 披露 workload/evaluator 内成立，未披露的硬件、精度、长度、batch、并发、SLO、seed 与 artifact commit 为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-17173:start -->只支持 exact-v1 披露设置中的机制与结果；旧路径在新增 owner/证据/控制责任不成立时继续共存。<!-- claim:SF-2026-ARXIV-2605-17173:end -->

Books Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-17173:end -->

<!-- review:SF-2026-ARXIV-2605-17193:start -->
#### Multi-LLM Systems Exhibit Robust Semantic Collapse

问题与机制：旧假设是增加 Agent、模型异质性、讨论轮数或表面采样多样性能够持续扩大搜索空间；当各 Agent 的后续 Context 反复由同一闭环中的模型输出构成时，历史不再是独立证据，而会成为递归 conditioning state。exact-v1 在作者披露的 closed-loop text simulations 中把 lexical diversity、within-run semantic displacement 与 aligned cross-run diversity 分开测量，显示词汇继续增长时语义支持仍可收缩。

Evaluation contract：三种主要模型各进行三次 1,000-round triadic run，其余干预通常使用 200 rounds、每条件三次；十二类干预覆盖 temperature、output budget、prompt、retrieval packing、model mixing、uncensored variants、activation steering、GRPO、population size、framework 与 noise。论文报告 62 个 baseline comparisons 经 Bonferroni correction 后没有正且显著的 semantic-diversity 改善。该结论绑定作者选择的模型、closed-loop scaffold、embedding model、window statistics 与 run-level clustering。

Trade-off / failure：结果支持把“独立 evidence 与外部 renewal”作为 Multi-Agent admission 条件，而不是继续增加同源对话；但它不证明开放工具环境、外部人类/数据持续注入、不同任务拓扑或所有语义度量都会 collapse。Supplementary Note 3 明确回归不构成机制或因果证明，Supplementary Note 5 也把 recursive-channel 理论作为 heuristic guide；immutable code/data commit 为 Not Disclosed。

Evidence locators：Method=`PDF section Methods; Supplementary Note 1 §§1.1–1.8; Supplementary Notes 2–3 intervention definitions`；Evaluation=`PDF section Results: Semantic Collapse in Extended Open-Ended Simulations; Semantic Collapse Resists Intervention; Diagnosing Mechanisms of Semantic Collapse; Supplementary Note 3 §3.7`；Counterevidence=`PDF section Discussion; Supplementary Note 3 §3.7 non-causal regression boundary; Supplementary Note 5 heuristic-theory and predictive-regularity boundaries`；Artifact=`official exact-v1 PDF=https://arxiv.org/pdf/2605.17193v1; bytes=4076663; sha256=edde49ce22de86ac25ad4d676f9003afec5c11513bee35438ca8db965322abe7; immutable code/data commit Not Disclosed`。

<!-- claim:SF-2026-ARXIV-2605-17193:start -->exact-v1 只支持作者 closed-loop、text-only、多模型/多轮与所列 intervention protocol 下的 semantic contraction；不支持“所有 Multi-Agent 都必然退化”，也不证明 recursive-channel explanation 为因果机制。<!-- claim:SF-2026-ARXIV-2605-17193:end -->

Books Decision=`No Change — Existing Coverage`：Ch82 已明确拥有同源 Agent 的 correlated error、证据独立性、趋同风险、coordination tax 与 single-Agent / independent verifier fallback；该论文强化现有判断，但没有新增独立状态 owner 或控制机制。
<!-- review:SF-2026-ARXIV-2605-17193:end -->

<!-- review:SF-2026-ARXIV-2605-17222:start -->
#### Triple-Hoisted Baby-Step Giant-Step Linear Transformation over CKKS Homomorphic Encryption and Hardware Accelerator

问题与 changed constraint：CKKS 线性变换把 rotation 数量、off-chip traffic 与 FPGA permutation/data-path 共同暴露为隐私推理的硬件执行合同；收益不等于通用 GPU/模型加速。

机制与 ownership：Computations can be directly carried out over ciphertexts using homomorphic encryption (HE), which is indispensable for privacy-preserving cloud computing. owner=`PLATFORM-SECURITY`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17222v1 — §II-B BSGS Algorithm for HE-LT (frozen exact-v1 official HTML receipt)`；Evaluation=`arXiv:2605.17222v1 — §VI Experimental Results and Comparisons (frozen exact-v1 official HTML receipt)`。

Trade-off / failure：`Not Disclosed — no dedicated limitations heading; claim remains bounded to disclosed setup`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17222:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17222:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17222:end -->

<!-- review:SF-2026-ARXIV-2605-17234:start -->
#### Active Budget Allocation for Efficient Scaling Law Estimation via Surrogate-Guided Pruning

问题与 changed constraint：Scaling-law 实验预算从均匀采样演进为 successive-halving 与 surrogate-guided pruning；节省拟合成本的同时引入错误早停与 surrogate selection bias。

机制与 ownership：In addition to enabling a more systematic allocation of a given compute budget, our findings show that SH paired with surrogate models yields a set of learning curves that includes one with a lower loss-compute value than what naive uniform allocation or an SH-only approach can obtain. owner=`WORLDVIEW-SCALING-LAW`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17234v1 — §1 Introduction (frozen exact-v1 official HTML receipt)`；Evaluation=`arXiv:2605.17234v1 — §4 Experiments (frozen exact-v1 official HTML receipt)`。

Trade-off / failure：`Not Disclosed — no dedicated limitations heading; claim remains bounded to disclosed setup`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17234:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17234:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17234:end -->

<!-- review:SF-2026-ARXIV-2605-17242:start -->
#### From Runnable to Shippable: Multi-Agent Test-Driven Development for Generating Full-Stack Web Applications from Requirements

问题与 changed constraint：acceptance tests become pre-execution workflow state; browser-observed failures become typed repair evidence rather than terminal text

机制与 ownership：We present TDDev, a framework that automates this closed loop through three stages: (1) converting high-level requirements into structured acceptance tests before any code is written, (2) deploying the application and validating it through browser-based interaction simulation, and (3) translating browser-observed failures into structured repair reports for the coding agent. owner=`AGENT-WORKFLOW`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17242v1 — §3 Methodology (§3.1–§3.4) (official exact-v1 HTML)`；Evaluation=`arXiv:2605.17242v1 — §4 Experimental Setup; §5 Results (official exact-v1 HTML)`。

Trade-off / failure：`arXiv:2605.17242v1 — §6.4 Threats to Validity (official exact-v1 HTML)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17242:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17242:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17242:end -->

<!-- review:SF-2026-ARXIV-2605-17246:start -->
#### Fidelity Probes for Specification--Code Alignment

问题与 changed constraint：Specification–code alignment 由单一测试通过率扩展为 code-grounded fidelity probes、contradiction/coverage-gap 分解和 frozen held-out resampling；probe generator 仍不是完整语义 oracle。

机制与 ownership：We introduce fidelity probes: natural-language questions generated from a reference artifact with code-derived ground-truth answers, answered from a candidate specification. owner=`PLATFORM-EVALUATION-SYSTEM`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17246v1 — §3 The Behavioural Alignment Framework (frozen exact-v1 official HTML receipt)`；Evaluation=`arXiv:2605.17246v1 — §5 Empirical Evaluation on CardDemo (frozen exact-v1 official HTML receipt)`。

Trade-off / failure：`arXiv:2605.17246v1 — §6 Discussion and limitations (frozen exact-v1 official HTML receipt)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17246:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17246:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17246:end -->

<!-- review:SF-2026-ARXIV-2605-17260:start -->
#### LiteFrame: Efficient Vision Encoders Unlock Frame Scaling in Video LLMs

问题与 changed constraint：post-hoc visual-token reduction 会把瓶颈推回逐帧 vision encoder；compressed-token distillation 让 encoder 直接生成时空压缩表示，交换 teacher 成本、表示偏差和 frame coverage。

机制与 ownership：To address this, we introduce LiteFrame, a strong, yet highly efficient video encoder backbone for Video LLMs. owner=`MULTIMODAL-REPRESENTATION`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17260v1 — §4.1 Architecture: Spatio-temporal Token Compressive Encoding (frozen exact-v1 official HTML receipt)`；Evaluation=`arXiv:2605.17260v1 — §5 Experiments (frozen exact-v1 official HTML receipt)`。

Trade-off / failure：`Not Disclosed — no dedicated limitations heading; claim remains bounded to disclosed setup`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17260:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17260:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17260:end -->

<!-- review:SF-2026-ARXIV-2605-17268:start -->
#### Is VLA Reasoning Faithful? Probing Safety of Chain-of-Causation in Autonomous Driving Models

问题与 changed constraint：VLA 的自然语言 rationale 不能取得 trajectory safety authority；reasoning fidelity、entity/action consistency 与视觉扰动稳定性必须成为独立传感器并由安全控制器提交动作。

机制与 ownership：We present the first systematic study of faithfulness in Vision-Language-Action (VLA) driving models, analyzing 300 Alpamayo-R1-10B inferences across 100 diverse PhysicalAI-AV scenarios. owner=`MULTIMODAL-EMBODIED-VLA`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17268v1 — §4 Methodology (frozen exact-v1 official HTML receipt)`；Evaluation=`arXiv:2605.17268v1 — §5 Results (frozen exact-v1 official HTML receipt)`。

Trade-off / failure：`Not Disclosed — no dedicated limitations heading; claim remains bounded to disclosed setup`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17268:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17268:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17268:end -->

<!-- review:SF-2026-ARXIV-2605-17273:start -->
#### Position: State-of-the-Art Claims Require State-of-the-Art Evidence

问题与 changed constraint：SOTA claim 需要 effect size、consistency、uncertainty 与 task-level superiority 证据，平均分第一只证明 aggregate ranking，不证明广泛优越。

机制与 ownership：This requires no additional experiments, only honest reporting of what results actually show, enabling more precise and interpretable comparisons across models. owner=`PLATFORM-EVALUATION-SYSTEM`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17273v1 — §2.1 Statistical Comparison Methods (frozen exact-v1 official HTML receipt)`；Evaluation=`arXiv:2605.17273v1 — §4.1 Case Analysis: HELM MMLU (frozen exact-v1 official HTML receipt)`。

Trade-off / failure：`Not Disclosed — no dedicated limitations heading; claim remains bounded to disclosed setup`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17273:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17273:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17273:end -->

<!-- review:SF-2026-ARXIV-2605-17281:start -->
#### ContractBench: Can LLM Agents Preserve Observation Contracts?

问题与 changed constraint：工具 observation 中的 presigned URL、session token 与 OAuth state 是带 byte-integrity 和 expiry 的 contract；模型只能传递，不能自由改写或延迟复用。

机制与 ownership：We show that observation contract compliance (preserving the temporal validity and byte-level integrity) is an emergent, regression-prone capability: it is neither guaranteed by general tool-use ability nor consistently improved by larger or newer models. owner=`AGENT-TOOL-CALLING`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17281v1 — §1 Introduction (frozen exact-v1 official HTML receipt)`；Evaluation=`arXiv:2605.17281v1 — §3.2 Evaluation Protocol (frozen exact-v1 official HTML receipt)`。

Trade-off / failure：`Not Disclosed — no dedicated limitations heading; claim remains bounded to disclosed setup`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17281:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17281:end -->

Books Decision=`Integrate`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17281:end -->

<!-- review:SF-2026-ARXIV-2605-17288:start -->
#### When Efficiency Backfires: Cascading LLMs Trigger Cascade Failure under Adversarial Attack

问题与 changed constraint：模型 cascade 的轻量 front-end 与 escalation controller 扩大攻击面；攻击可同时破坏质量和成本目标，因此 route/admission 需绑定 adversarial evidence 与保守 fallback。

机制与 ownership：In this work, we present the first study demonstrating that LLM cascade systems are susceptible to targeted adversarial manipulation, which disrupts both performance objectives and the intended cost advantages of the cascade design. owner=`INFER-SCHEDULING`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17288v1 — §3.2 System Model (frozen exact-v1 official HTML receipt)`；Evaluation=`arXiv:2605.17288v1 — §6 Experiment (frozen exact-v1 official HTML receipt)`。

Trade-off / failure：`arXiv:2605.17288v1 — §7 Discussion (frozen exact-v1 official HTML receipt)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17288:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17288:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17288:end -->

<!-- review:SF-2026-ARXIV-2605-17289:start -->
#### LEAP: Learnable End-to-End Adaptive Pruning of Large Language Models

问题与 changed constraint：端到端 unstructured mask learning 把 pruning owner 从 layer-wise surrogate 移到全局 mask objective，但一次性 H100 训练成本和 kernel compatibility 不等于部署 speedup。

机制与 ownership：End-to-end alternatives such as MaskLLM and PATCH show that learnable masks can close this gap, but their categorical-over-patterns parameterization scales with the number of valid masks per row and does not port to the unstructured setting. owner=`INFER-TENSORRT-LLM`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17289v1 — §3 LEAP: Method (frozen exact-v1 official HTML receipt)`；Evaluation=`arXiv:2605.17289v1 — §4 Experiments (frozen exact-v1 official HTML receipt)`。

Trade-off / failure：`arXiv:2605.17289v1 — §5 Discussion and Limitations (frozen exact-v1 official HTML receipt)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17289:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17289:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17289:end -->

<!-- review:SF-2026-ARXIV-2605-17291:start -->
#### Step-wise Rubric Rewards for LLM Reasoning

问题与 changed constraint：final-answer reward 对中间步骤产生错误 credit；step-wise rubric attribution/normalization 改变 gradient ownership，但依赖 judge 与显式 step boundary。

机制与 ownership：Rubric-based methods such as Rubrics as Rewards (RaR) introduce finer-grained supervision by scoring rollouts against structured criteria, yet the rubric scores are still aggregated into a single scalar applied to the entire response, causing three weaknesses: loss of multi-criterion structure, uniform supervision of correct and incorrect steps, and reward hacking through unbounded self-correction. owner=`TRAIN-RLHF`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17291v1 — §3 Method (frozen exact-v1 official HTML receipt)`；Evaluation=`arXiv:2605.17291v1 — §2.2 Rubric-Based Evaluation and Rewards (frozen exact-v1 official HTML receipt)`。

Trade-off / failure：`arXiv:2605.17291v1 — §6 Limitations (frozen exact-v1 official HTML receipt)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17291:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17291:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17291:end -->

<!-- review:SF-2026-ARXIV-2605-17292:start -->
#### MetaCogAgent: A Metacognitive Multi-Agent LLM Framework with Self-Aware Task Delegation

问题与 changed constraint：delegation consumes a capability profile and confidence sensor, but self-reported confidence cannot own commit authority

机制与 ownership：Inspired by metacognition theory from cognitive science, we propose MetaCogAgent, a multi-agent LLM framework where each agent is equipped with a Metacognitive Self-Assessment Unit that evaluates task-capability alignment before execution. owner=`AGENT-MULTI-AGENT`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17292v1 — §III MetaCogAgent Framework (§III-B–§III-D) (official exact-v1 HTML)`；Evaluation=`arXiv:2605.17292v1 — §V Experiments (official exact-v1 HTML)`。

Trade-off / failure：`arXiv:2605.17292v1 — §VI Discussion; no dedicated limitations section (official exact-v1 HTML)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17292:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17292:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17292:end -->

<!-- review:SF-2026-ARXIV-2605-17301:start -->
#### ConflictRAG: Detecting and Resolving Knowledge Conflicts in Retrieval Augmented Generation

问题与 changed constraint：RAG 在生成前显式检测、分类并解决 retrieved-source conflict；source credibility 与 temporal/opinion policy 变成可审计状态，但 LLM judge 与合成冲突数据限制外推。

机制与 ownership：We present ConflictRAG, a conflict-aware RAG framework that detects, classifies, and resolves knowledge conflicts prior to answer generation. owner=`AGENT-RAG`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17301v1 — §III Methodology (frozen exact-v1 official HTML receipt)`；Evaluation=`arXiv:2605.17301v1 — §IV Experimental Setup (frozen exact-v1 official HTML receipt)`。

Trade-off / failure：`arXiv:2605.17301v1 — §V-G Limitations (frozen exact-v1 official HTML receipt)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17301:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17301:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17301:end -->

<!-- review:SF-2026-ARXIV-2605-17304:start -->
#### Compress the Context, Keep the Commitments: A Formal Framework for Verifiable LLM Context Compression

问题与 changed constraint：Context compression 的对象从 token 变为 typed, source-grounded commitment atoms；压缩必须验证 critical recall、conflict/equivalence 与 recoverability，并在不确定时回退 raw spans/更大 context。

机制与 ownership：We propose Context Codec, a commitment-level framework for compressing prompts and chat histories. owner=`AGENT-CONTEXT`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17304v1 — §3 Problem Formulation (frozen exact-v1 official HTML receipt)`；Evaluation=`Not Disclosed — no dedicated evaluation heading in the frozen exact-v1 receipt`。

Trade-off / failure：`Not Disclosed — no dedicated limitations heading; claim remains bounded to disclosed setup`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17304:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17304:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17304:end -->

<!-- review:SF-2026-ARXIV-2605-17305:start -->
#### CyberCorrect: A Cybernetic Framework for Closed-Loop Self-Correction in Large Language Models

问题与 changed constraint：self-correction is represented as detector-controller-stop state with overshoot and oscillation, not an unbounded retry loop

机制与 ownership：We propose CyberCorrect, a framework that formalizes LLM self-correction as a closed-loop control system grounded in cybernetic theory. owner=`AGENT-REFLECTION`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17305v1 — §III CyberCorrect Framework (§III-B–§III-D) (official exact-v1 HTML)`；Evaluation=`arXiv:2605.17305v1 — §V Experiments (official exact-v1 HTML)`。

Trade-off / failure：`arXiv:2605.17305v1 — §VI Discussion; no dedicated limitations section (official exact-v1 HTML)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17305:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17305:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17305:end -->

<!-- review:SF-2026-ARXIV-2605-17320:start -->
#### TClone: Low-Latency Forking of Live GUI Environments for Computer-Use Agents

问题与 changed constraint：Computer-use workspace 从一次性 sandbox 演进为 live save/fork/rollback/selective-commit；低延迟 branch 与 durable checkpoint 分权，同时引入 credential、GUI、external side-effect merge 边界。

机制与 ownership：We present TClone, a forkable personal workspace system for computer-use agents. owner=`AGENT-PLATFORM`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17320v1 — §4 TClone Design (frozen exact-v1 official HTML receipt)`；Evaluation=`arXiv:2605.17320v1 — §5 Evaluation (frozen exact-v1 official HTML receipt)`。

Trade-off / failure：`arXiv:2605.17320v1 — §2.3 Limitations of Existing Solutions (frozen exact-v1 official HTML receipt)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17320:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17320:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17320:end -->

<!-- review:SF-2026-ARXIV-2605-17324:start -->
#### ASPI: Seeking Ambiguity Clarification Amplifies Prompt Injection Vulnerability in LLM Agents

问题与 changed constraint：Clarification 是独立 agent state transition，可能把 prompt injection 从 tool-return path 扩展到后续 user-input path；clarify 不能自动提升输入 authority。

机制与 ownership：We introduce ASPI (Ambiguous-State Prompt Injection), a benchmark of 728 task-attack scenarios that isolates clarification as a distinct agent state and measures how this state transition affects vulnerability under controlled conditions. owner=`PLATFORM-SECURITY`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17324v1 — §5.1 Evaluation Design (frozen exact-v1 official HTML receipt)`；Evaluation=`arXiv:2605.17324v1 — §5 Evaluation (frozen exact-v1 official HTML receipt)`。

Trade-off / failure：`arXiv:2605.17324v1 — §7 Discussion (frozen exact-v1 official HTML receipt)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17324:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17324:end -->

Books Decision=`Integrate`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17324:end -->

<!-- review:SF-2026-ARXIV-2605-17329:start -->
#### LPG: Balancing Efficiency and Policy Reasoning in Latent Policy Guardrails

问题与 changed constraint：dynamic policy clauses are inference-time guardrail state; latent compression saves latency but remains a fallible sensor

机制与 ownership：We introduce Latent Policy Guardrail (LPG), a guardrail framework that learnssemantic latent deliberation over dynamic policies. owner=`PLATFORM-SECURITY`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17329v1 — §4 Method (§4.2–§4.6) (official exact-v1 HTML)`；Evaluation=`arXiv:2605.17329v1 — §5 Main Results; §6 Ablation (official exact-v1 HTML)`。

Trade-off / failure：`arXiv:2605.17329v1 — Appendix D Limitations and Broader Impacts (official exact-v1 HTML)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17329:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17329:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17329:end -->

<!-- review:SF-2026-ARXIV-2605-17348:start -->
#### Taming "Zombie'' Agents: A Markov State-Aware Framework for Resilient Multi-Agent Evolution

问题与 changed constraint：Active/Standby/Terminated is a recoverable agent lifecycle that avoids irreversible pruning after one bad round

机制与 ownership：In this paper, we propose AgentRevive, a Markov state-aware framework for resilient multi-agent evolution. owner=`AGENT-MULTI-AGENT`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17348v1 — §4 Methodology (§4.2–§4.3) (official exact-v1 HTML)`；Evaluation=`arXiv:2605.17348v1 — §5 Experiments (official exact-v1 HTML)`。

Trade-off / failure：`arXiv:2605.17348v1 — §6 Conclusion and robustness appendix; no dedicated limitations section (official exact-v1 HTML)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17348:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17348:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17348:end -->

<!-- review:SF-2026-ARXIV-2605-17360:start -->
#### Omni-DuplexEval: Evaluating Real-time Duplex Omni-modal Interaction

问题与 changed constraint：duplex evaluation makes response timing and content alignment joint evidence instead of scoring only a completed offline answer

机制与 ownership：To address this gap, we propose Omni-DuplexEval, a benchmark for systematically evaluating real-time duplex interaction. owner=`PLATFORM-EVALUATION-SYSTEM`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17360v1 — §3 Omni-DuplexEval (§3.2–§3.3) (official exact-v1 HTML)`；Evaluation=`arXiv:2605.17360v1 — §4 Experiments (official exact-v1 HTML)`。

Trade-off / failure：`arXiv:2605.17360v1 — Appendix D Limitations (official exact-v1 HTML)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17360:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17360:end -->

Books Decision=`Integrate`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17360:end -->

<!-- review:SF-2026-ARXIV-2605-17373:start -->
#### FML-bench: A Controlled Study of AI Research Agent Strategies from the Perspective of Search Dynamics

问题与 changed constraint：research-agent benchmarks must separate search policy from execution substrate and preserve process-level trajectory metrics

机制与 ownership：We propose FML-Bench, a benchmark of 18 fundamental ML research tasks across 10 domains that separates agent strategy from execution infrastructure and defines 12 process-level behavioral metrics. owner=`PLATFORM-EVALUATION-SYSTEM`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17373v1 — §3 FML-bench (§3.2–§3.4) (official exact-v1 HTML)`；Evaluation=`arXiv:2605.17373v1 — §4 Experiments; §5 Search-dynamics analysis (official exact-v1 HTML)`。

Trade-off / failure：`arXiv:2605.17373v1 — Appendix N Broader impacts; no dedicated limitations section (official exact-v1 HTML)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17373:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17373:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17373:end -->

<!-- review:SF-2026-ARXIV-2605-17380:start -->
#### ADR: An Agentic Detection System for Enterprise Agentic AI Security

问题与 changed constraint：agent security needs prompt/tool/causal-chain telemetry plus cheap triage and contextual escalation, not file events alone

机制与 ownership：We present the Agentic AI Detection and Response (ADR) system, the first large-scale, production-proven enterprise framework for securing AI agents operating through the Model Context Protocol (MCP). owner=`PLATFORM-SECURITY`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17380v1 — §3 ADR System Design (§3.1–§3.2) (official exact-v1 HTML)`；Evaluation=`arXiv:2605.17380v1 — §5 Evaluation; §6 Real-World Deployment (official exact-v1 HTML)`。

Trade-off / failure：`arXiv:2605.17380v1 — §7 Discussion; no dedicated limitations section (official exact-v1 HTML)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17380:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17380:end -->

Books Decision=`Integrate`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17380:end -->

<!-- review:SF-2026-ARXIV-2605-17415:start -->
#### IVF-TQ: Calibration-Free Streaming Vector Search via a Codebook-Free Residual Layer

问题与 changed constraint：streaming ANN requires an explicit coarse-index refresh owner and bounded stale-assignment fallback

机制与 ownership：Approximate nearest neighbor (ANN) indexes deployed against streaming corpora silently lose recall over weeks. owner=`AGENT-RAG`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17415v1 — §3 IVF-TQ (§3.1–§3.3) (official exact-v1 HTML)`；Evaluation=`arXiv:2605.17415v1 — §4 Streaming Experiments; §5 Million-Scale Evaluation (official exact-v1 HTML)`。

Trade-off / failure：`arXiv:2605.17415v1 — §7 Limitations (official exact-v1 HTML)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17415:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17415:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17415:end -->

<!-- review:SF-2026-ARXIV-2605-17439:start -->
#### DiagEval: Trajectory-Conditioned Diagnosis for Reliable Software Evaluation with GUI Agents

问题与 changed constraint：GUI-agent evaluation separates outcome scoring from failure localization and counterfactual diagnosis

机制与 ownership：We present DiagEval, a trajectory-conditioned diagnostic evaluation protocol for post-failure GUI-agent evaluation of interactive software. owner=`PLATFORM-EVALUATION-SYSTEM`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17439v1 — §4 DiagEval (§4.1–§4.4) (official exact-v1 HTML)`；Evaluation=`arXiv:2605.17439v1 — §5 Experiments (official exact-v1 HTML)`。

Trade-off / failure：`arXiv:2605.17439v1 — §6 Limitations (official exact-v1 HTML)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17439:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17439:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17439:end -->

<!-- review:SF-2026-ARXIV-2605-17453:start -->
#### Trust No Tool: Evaluating and Defending LLM Agents under Untrusted Tool Feedback

问题与 changed constraint：工具在探索期积累可信反馈、到隐藏状态满足时才毒化最终 action；final-action guard 必须对 trajectory-derived environment variables 做风险审查，单次 tool selection 不足。

机制与 ownership：To study this setting, we construct TRUST-Bench, a task-conditioned benchmark of 1,970 hidden-trigger tool-compromise episodes with matched safe controls, introduce an asymmetric penalty metric, GuardedJoint, to better reflect real deployment risk, and present VISTA-Guard, a backbone-agnostic framework for final-action risk scoring. owner=`AGENT-TOOL-CALLING`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17453v1 — §3 Method: VISTA-Guard under Untrusted Tool Feedback (frozen exact-v1 official HTML receipt)`；Evaluation=`arXiv:2605.17453v1 — §2 Threat Model, Benchmark, and Evaluation Lens (frozen exact-v1 official HTML receipt)`。

Trade-off / failure：`arXiv:2605.17453v1 — §5 Discussion (frozen exact-v1 official HTML receipt)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17453:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17453:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17453:end -->

<!-- review:SF-2026-ARXIV-2605-17467:start -->
#### VerifyMAS: Hypothesis Verification for Failure Attribution in LLM Multi-Agent Systems

问题与 changed constraint：multi-agent verification assigns claims and evidence to agents so disagreement is attributable rather than pooled

机制与 ownership：To address these challenges, we propose VerifyMAS, a hypothesis verification framework for agent failure attribution. owner=`AGENT-MULTI-AGENT`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17467v1 — §3 VerifyMAS (§3.1–§3.2) (official exact-v1 HTML)`；Evaluation=`arXiv:2605.17467v1 — §4 Main Experiments (official exact-v1 HTML)`。

Trade-off / failure：`arXiv:2605.17467v1 — §5 Discussion; no dedicated limitations section (official exact-v1 HTML)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17467:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17467:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17467:end -->

<!-- review:SF-2026-ARXIV-2605-17471:start -->
#### WinQ: Accelerating Quantization-Aware Training of Language Models Around Saddle Points

问题与 changed constraint：quantization-aware training changes loss geometry and convergence assumptions; deployment speedup still depends on compatible kernels

机制与 ownership：To mitigate these issues, we propose an algorithm called WinQ to accelerate QAT, which involves: (1) periodically resetting weights to the linear interpolation of full-precision and quantized weights, reducing the distance to the quantization grid and increasing eigenvalue magnitude, and (2) computing gradients of noise-injected weights to regularize the Hessian. owner=`TRAIN-PRETRAINING`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17471v1 — §3 Our Approach (§3.1–§3.2) (official exact-v1 HTML)`；Evaluation=`arXiv:2605.17471v1 — §4 Experiments (official exact-v1 HTML)`。

Trade-off / failure：`arXiv:2605.17471v1 — §5 Conclusion; no dedicated limitations section (official exact-v1 HTML)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17471:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17471:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17471:end -->

<!-- review:SF-2026-ARXIV-2605-17480:start -->
#### The Capability Paradox: How Smarter Auditors Make Multi-Agent Systems Less Secure

问题与 changed constraint：更强 Worker 可能以更确定语言把 semantic hijacking 传给 Manager；capability/certainty 不能替代 independent evidence，跨 Agent commit 需要来源与反证门。

机制与 ownership：Building on the mediation finding, we propose heterogeneous ensemble verification, which pairs Workers of asymmetric domain competence so their complementary vulnerabilities break the certainty-to-execution chain, reducing ASR from 52.8% to 2.0% with negligible benign-task impact. owner=`PLATFORM-SECURITY`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17480v1 — §3 Methodology (frozen exact-v1 official HTML receipt)`；Evaluation=`arXiv:2605.17480v1 — §4 Evaluation (frozen exact-v1 official HTML receipt)`。

Trade-off / failure：`arXiv:2605.17480v1 — §6 Limitations (frozen exact-v1 official HTML receipt)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17480:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17480:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17480:end -->

<!-- review:SF-2026-ARXIV-2605-17497:start -->
#### Self-Supervised On-Policy Distillation for Reasoning Language Models

问题与 changed constraint：teacher signals are generated on the learner's current rollout distribution, trading stale offline supervision for online sampling cost

机制与 ownership：We show that a mixed group contains a richer process signal: a correct completion is a self-generated witness of how the current policy can solve the problem, while a wrong completion provides on-policy prefixes where the policy needs correction. owner=`TRAIN-GRPO`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17497v1 — §3 Self-Supervised On-Policy Distillation (official exact-v1 HTML)`；Evaluation=`arXiv:2605.17497v1 — §4 Experiments (official exact-v1 HTML)`。

Trade-off / failure：`arXiv:2605.17497v1 — §5 Discussion; no dedicated limitations section (official exact-v1 HTML)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17497:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17497:end -->

Books Decision=`Integrate`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17497:end -->

<!-- review:SF-2026-ARXIV-2605-17508:start -->
#### BESplit: Bias-Compensated Split Federated Learning with Evidential Aggregation

问题与 changed constraint：split federated execution moves activation and optimizer state across a trust/network boundary but remains tied to the disclosed edge workload

机制与 ownership：Based on this insight, we propose BESplit, an architecture-aware framework that exploits the intrinsic structure of SFL to mitigate non-IID effects. owner=`TRAIN-DISTRIBUTED-TRAINING`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17508v1 — §4 Methodology (official exact-v1 HTML)`；Evaluation=`arXiv:2605.17508v1 — §5 Experiments (official exact-v1 HTML)`。

Trade-off / failure：`arXiv:2605.17508v1 — §6 Discussion (official exact-v1 HTML)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17508:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17508:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17508:end -->

<!-- review:SF-2026-ARXIV-2605-17522:start -->
#### RoboFlow4D: A Lightweight Flow World Model Toward Real-Time Flow-Guided Robotic Manipulation

问题与 changed constraint：closed-loop world-model evaluation must bind action conditioning, rollout state and downstream control outcome

机制与 ownership：To address these challenges, we introduce RoboFlow4D, a lightweight flow world model that unifies perception and planning by estimating temporal motion in physical 3D space. owner=`MULTIMODAL-WORLD-MODELS`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17522v1 — §3 Methodology (§3.2–§3.4) (official exact-v1 HTML)`；Evaluation=`arXiv:2605.17522v1 — §4 Experiments (official exact-v1 HTML)`。

Trade-off / failure：`arXiv:2605.17522v1 — §5 Conclusion; no dedicated limitations section (official exact-v1 HTML)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17522:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17522:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17522:end -->

<!-- review:SF-2026-ARXIV-2605-17554:start -->
#### Evaluating Deep Research Agents on Expert Consulting Work: A Benchmark with Verifiers, Rubrics, and Cognitive Traps

问题与 changed constraint：deep-research evaluation preserves search process, evidence use and final artifact as distinct measurement planes

机制与 ownership：We introduce a benchmark of 70 SME-authored management consulting prompts, each embedding cognitive traps that penalize surface-pattern reasoning. owner=`PLATFORM-EVALUATION-SYSTEM`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17554v1 — §3 Benchmark Design (§3.3–§3.4) (official exact-v1 HTML)`；Evaluation=`arXiv:2605.17554v1 — §4 Experiments (official exact-v1 HTML)`。

Trade-off / failure：`arXiv:2605.17554v1 — §5 Limitations (official exact-v1 HTML)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17554:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17554:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17554:end -->

<!-- review:SF-2026-ARXIV-2605-17558:start -->
#### Firefly: Illuminating Large-Scale Verified Tool-Call Data Generation from Real APIs

问题与 changed constraint：tool-call training data is admitted only after executable verification and typed failure closure

机制与 ownership：We present FireFly, a pipeline for generating verified tool-call data from real-world MCP servers. owner=`AGENT-TOOL-CALLING`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17558v1 — §3 Method (§3.1–§3.3) (official exact-v1 HTML)`；Evaluation=`arXiv:2605.17558v1 — §5 Experiments (official exact-v1 HTML)`。

Trade-off / failure：`arXiv:2605.17558v1 — §7 Limitations (official exact-v1 HTML)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17558:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17558:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17558:end -->

<!-- review:SF-2026-ARXIV-2605-17570:start -->
#### How Off-Policy Can GRPO Be? Mu-GRPO for Efficient LLM Reinforcement Learning

问题与 changed constraint：asynchronous RL must account for policy-version staleness in advantage updates rather than treating every rollout as current

机制与 ownership：We show that GRPO-style algorithms can tolerate substantially larger rollout staleness than previously assumed, and propose Mu-GRPO, an RL training framework that organizes training into a small number (e.g., four) of large sequential generation-optimization stages. owner=`TRAIN-GRPO`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17570v1 — §3 Diagnosing rollout staleness; §4 μ-GRPO (official exact-v1 HTML)`；Evaluation=`arXiv:2605.17570v1 — §5 Experiments (official exact-v1 HTML)`。

Trade-off / failure：`arXiv:2605.17570v1 — §6 Discussion; no dedicated limitations section (official exact-v1 HTML)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17570:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17570:end -->

Books Decision=`Integrate`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17570:end -->

<!-- review:SF-2026-ARXIV-2605-17590:start -->
#### Form and Function: Machine Unlearning as a Problem of Misaligned States

问题与 changed constraint：Machine unlearning 的目标不是只校正参数，而是对齐删除编辑后的 counterfactual optimizer state，包括 L-BFGS memory operator 与下一步 update direction。

机制与 ownership：We introduce state-aware metrics that separately measure parameter error, memory-operator error, combined state error, and update-direction error. owner=`TRAIN-DATA`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17590v1 — §4 Problem Setup (frozen exact-v1 official HTML receipt)`；Evaluation=`arXiv:2605.17590v1 — §5 Theoretical Results (frozen exact-v1 official HTML receipt)`。

Trade-off / failure：`arXiv:2605.17590v1 — §7 Discussion (frozen exact-v1 official HTML receipt)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17590:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17590:end -->

Books Decision=`Integrate`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17590:end -->

<!-- review:SF-2026-ARXIV-2605-17609:start -->
#### Adaptive Generate-Rank-Verify: Inference-Time Search with Costly Verification

问题与 changed constraint：test-time compute allocation jointly owns generation count, rank signal, verifier budget and stopping under an explicit monotonicity assumption

机制与 ownership：We formalize this setting using a learning-theoretic lens as generative active search: a cost-sensitive first-positive search problem in which a policy adaptively samples candidates from an unknown distribution, observes cheap scores, and pays for verifier labels until it finds a positive example. owner=`INFER-SCHEDULING`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17609v1 — §4 ADAP Adaptive Policy (official exact-v1 HTML)`；Evaluation=`arXiv:2605.17609v1 — §5 Experiments (official exact-v1 HTML)`。

Trade-off / failure：`arXiv:2605.17609v1 — §7 Limitations (official exact-v1 HTML)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17609:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17609:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17609:end -->

<!-- review:SF-2026-ARXIV-2605-17610:start -->
#### SafeLens: Deliberate and Efficient Video Guardrails with Fast-and-Slow Screening

问题与 changed constraint：fast/slow video moderation routes only uncertain temporal cases to deliberation while preserving a conservative safety fallback

机制与 ownership：We propose SafeLens, a video guardrail framework that introduces a fast-and-slow inference architecture for efficient and accurate content moderation with variable computational cost across inputs. owner=`PLATFORM-SECURITY`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17610v1 — §4 Data Curation; §5 SafeLens (official exact-v1 HTML)`；Evaluation=`arXiv:2605.17610v1 — §6 Experiments (official exact-v1 HTML)`。

Trade-off / failure：`arXiv:2605.17610v1 — Appendix A Limitations (official exact-v1 HTML)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17610:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17610:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17610:end -->

<!-- review:SF-2026-ARXIV-2605-17613:start -->
#### VeriCache: Turning Lossy KV Cache into Lossless LLM Inference

问题与 changed constraint：有损 KV 只作为 draft，full KV 被保留到慢层并拥有最终 verification/commit；换取 lossless output 的代价是 full-state tier、swap/prefetch 与验证失败回退。

机制与 ownership：We present VeriCache, the first inference framework that ensures the same output as full-KV-cache decoding but largely preserves the high decoding throughput of a range of KV cache compression algorithms. owner=`INFER-KV-CACHE`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17613v1 — §3 Motivation: Why Lossy KV Methods Fail (frozen exact-v1 official HTML receipt)`；Evaluation=`Not Disclosed — no dedicated evaluation heading in the frozen exact-v1 receipt`。

Trade-off / failure：`Not Disclosed — no dedicated limitations heading; claim remains bounded to disclosed setup`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17613:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17613:end -->

Books Decision=`Integrate`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17613:end -->

<!-- review:SF-2026-ARXIV-2605-17617:start -->
#### GraphMind: From Operational Traces to Self-Evolving Workflow Automation

问题与 changed constraint：operational traces become versioned workflow graphs whose online traversal and reinforcement need separate owners

机制与 ownership：We present GraphMind, a system that constructs, executes, and evolves action-centric workflow graphs with minimal human effort. owner=`AGENT-WORKFLOW`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17617v1 — §3 Offline Workflow Graph; §4 Online Traversal; §5 Reinforcement (official exact-v1 HTML)`；Evaluation=`arXiv:2605.17617v1 — §6 Evaluation; §7 Production Deployment (official exact-v1 HTML)`。

Trade-off / failure：`arXiv:2605.17617v1 — §8 Discussion (official exact-v1 HTML)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17617:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17617:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17617:end -->

<!-- review:SF-2026-ARXIV-2605-17625:start -->
#### Episodic-Semantic Memory Architecture for Long-Horizon Scientific Agents

问题与 changed constraint：episodic window and semantic consolidation are separate memory states; consolidation quality, contradiction and growth are explicit failure modes

机制与 ownership：As Large Language Models (LLMs) evolve into persistent scientific collaborators, context window saturation has emerged as a critical bottleneck. owner=`AGENT-MEMORY`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17625v1 — §3 Dual-Process Memory Architecture; §3.2 Episodic Window; §3.3 Semantic Consolidation (official exact-v1 HTML)`；Evaluation=`arXiv:2605.17625v1 — §4 Experimental Design; §5 Results (official exact-v1 HTML)`。

Trade-off / failure：`arXiv:2605.17625v1 — §6 Discussion and limitations (official exact-v1 HTML)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17625:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17625:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17625:end -->

<!-- review:SF-2026-ARXIV-2605-17634:start -->
#### AI Agents May Always Fall for Prompt Injections

问题与 changed constraint：Prompt injection 不可仅靠 data/instruction separation 完全解决；Contextual Integrity 显示 norm manipulation/mixed flows 的不可判定边界，最终 authority 必须由 capability policy/approval 持有。

机制与 ownership：Despite recent progress, we show that the prevailing defense paradigm (data-instruction separation) both fails to detect attacks that operate through contextual manipulation and degrades contextually appropriate behavior. owner=`PLATFORM-SECURITY`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17634v1 — §1 Introduction (frozen exact-v1 official HTML receipt)`；Evaluation=`arXiv:2605.17634v1 — §5.1 Attacking Context Parameters Inference and Norm Evaluation (frozen exact-v1 official HTML receipt)`。

Trade-off / failure：`arXiv:2605.17634v1 — §3 Limitations of Current Views on Prompt Injection (frozen exact-v1 official HTML receipt)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17634:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17634:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17634:end -->

<!-- review:SF-2026-ARXIV-2605-17641:start -->
#### Causal Intervention-Based Memory Selection for Long-Horizon LLM Agents

问题与 changed constraint：Memory selection 从 semantic similarity 演进为 controlled causal interventions；收益依赖 intervention/judge validity，计算成本和 distribution shift 要求保留普通 retrieval fallback。

机制与 ownership：We propose Causal Memory Intervention (CMI), a causal memory-selection technique that estimates how candidate memories affect the model's answer under controlled interventions, selecting memories that improve task performance while suppressing unstable, irrelevant, or harmful ones. owner=`AGENT-MEMORY`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17641v1 — §3 Proposed Framework (frozen exact-v1 official HTML receipt)`；Evaluation=`arXiv:2605.17641v1 — §5 Experimental Setup (frozen exact-v1 official HTML receipt)`。

Trade-off / failure：`Not Disclosed — no dedicated limitations heading; claim remains bounded to disclosed setup`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17641:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17641:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17641:end -->

<!-- review:SF-2026-ARXIV-2605-17659:start -->
#### Bug or Feature$^2$: Weight Drift, Activation Sparsity and Spikes

问题与 changed constraint：正偏激活与标准 loss 在初始化产生 negative weight drift，进而形成 activation sparsity/spikes；这是 optimizer–activation coupling，不是单纯数据性质或默认正则收益。

机制与 ownership：The design of modern neural architectures has converged through incremental empirical choices, yet the mechanisms governing their training dynamics remain only partially understood. owner=`TRAIN-PRETRAINING`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17659v1 — §1 Formal Illustration of Negative Weight Drift (frozen exact-v1 official HTML receipt)`；Evaluation=`arXiv:2605.17659v1 — §2 Empirical Results for Negative Weight Drift (frozen exact-v1 official HTML receipt)`。

Trade-off / failure：`Not Disclosed — no dedicated limitations heading; claim remains bounded to disclosed setup`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17659:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17659:end -->

Books Decision=`Integrate`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17659:end -->

<!-- review:SF-2026-ARXIV-2605-17672:start -->
#### Stop When Reasoning Converges: Semantic-Preserving Early Exit for Reasoning Models

问题与 changed constraint：Reasoning early exit 应检测 successive-step semantic convergence，而非只看 answer confidence；节省 token 的代价是 embedding/judge 开销与 premature-stop failure。

机制与 ownership：Building on this insight, we propose PUMA, a plug-and-play framework that combines a lightweight Redundancy Detector with answer-level verification. owner=`INFER-SCHEDULING`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17672v1 — §3 Methodology (frozen exact-v1 official HTML receipt)`；Evaluation=`arXiv:2605.17672v1 — §4 Experimental Setup (frozen exact-v1 official HTML receipt)`。

Trade-off / failure：`arXiv:2605.17672v1 — §6 Analysis and Discussion (frozen exact-v1 official HTML receipt)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17672:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17672:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17672:end -->

<!-- review:SF-2026-ARXIV-2605-17683:start -->
#### μ-ORCA: Optimizing Acceleration for Microsecond-Scale Deep Neural Network Inference on ACAP

问题与 changed constraint：microsecond inference requires overhead-aware execution planning across direct inter-layer links, synchronization and non-matmul operators

机制与 ownership：To address these problems, we propose μ-ORCA, a customized heterogeneous accelerator framework for ultra-low-latency model inference. owner=`INFER-TENSORRT-LLM`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17683v1 — §4 μ-ORCA Architecture and Implementation; §5 Performance Model and Design-Space Exploration (official exact-v1 HTML)`；Evaluation=`arXiv:2605.17683v1 — §6 Evaluation (official exact-v1 HTML)`。

Trade-off / failure：`arXiv:2605.17683v1 — §7 Conclusion; no dedicated limitations section (official exact-v1 HTML)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17683:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17683:end -->

Books Decision=`Integrate`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17683:end -->

<!-- review:SF-2026-ARXIV-2605-17707:start -->
#### Speed Kills: Exploring Confused Deputy Attacks Through Edge AI Accelerators

问题与 changed constraint：Edge AI accelerator 绕过 OS 语义隔离时可能成为 confused deputy；DMA/地址/权限验证必须进入 accelerator–driver contract，而不是只相信应用进程边界。

机制与 ownership：We propose an on-demand validation defense against CDA, and evaluation on the Gem5- salam simulator shows that it incurs minimal runtime overhead (i.e., ~15%). owner=`PLATFORM-SECURITY`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17707v1 — §VIII-B () Setup (frozen exact-v1 official HTML receipt)`；Evaluation=`arXiv:2605.17707v1 — §VIII-D2 Results (frozen exact-v1 official HTML receipt)`。

Trade-off / failure：`Not Disclosed — no dedicated limitations heading; claim remains bounded to disclosed setup`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17707:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17707:end -->

Books Decision=`Integrate`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17707:end -->

<!-- review:SF-2026-ARXIV-2605-17721:start -->
#### EXG: Self-Evolving Agents with Experience Graphs

问题与 changed constraint：Self-evolving Agent 把成功/失败经验组织为 online/offline experience graph；结构化复用提高可用性，同时带来 provenance、staleness、错误传播与 graph lifecycle 成本。

机制与 ownership：To address this limitation, we introduce EXG, an experience graph framework for self-evolving agents that explicitly organizes accumulated successes and failures into a structured, relational representation. owner=`AGENT-MEMORY`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17721v1 — §2 Experience Graph Design (frozen exact-v1 official HTML receipt)`；Evaluation=`arXiv:2605.17721v1 — §4 Experiments (frozen exact-v1 official HTML receipt)`。

Trade-off / failure：`Not Disclosed — no dedicated limitations heading; claim remains bounded to disclosed setup`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17721:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17721:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17721:end -->

<!-- review:SF-2026-ARXIV-2605-17734:start -->
#### Harnessing LLM Agents with Skill Programs

**问题与机制。** To bridge the gap, we introduce HASP(Harnessing LLM Agents with Skill Programs), a new framework that upgrades skills into executable Program Functions (PFs). 该 family 改变或挑战 `AGENT-PLATFORM` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3.1–3.3 Program Functions`；Evaluation=`§4.1–4.2 Experiments`；Limitations/Counterevidence=`Appendix A Limitations`。

<!-- claim:SF-2026-ARXIV-2605-17734:start -->Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-17734:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-17734:end -->

<!-- review:SF-2026-ARXIV-2605-17757:start -->
#### OSCAR: Offline Spectral Covariance-Aware Rotation for 2-bit KV Cache Quantization

**问题与机制。** We propose OSCAR, an Ultra-low-bit KV Cache quantization method that estimates attention-aware covariance structures offline and uses them to derive fixed rotations and clipping thresholds for quantization. 该 family 改变或挑战 `INFER-KV-CACHE` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3 OSCAR; §3.1–3.4 offline covariance-aware rotation and mixed K/V layout`；Evaluation=`§4 Experiments; §4.1–4.5 quality, memory and kernel latency`；Limitations/Counterevidence=`Appendix D Limitations`。

<!-- claim:SF-2026-ARXIV-2605-17757:start -->只支持 exact-v1 明确披露的模型、数据、硬件、精度、长度、并发与 evaluator；未披露字段为 Not Disclosed，不把模拟、单机或选定 benchmark 外推成生产保证。<!-- claim:SF-2026-ARXIV-2605-17757:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-17757:end -->

<!-- review:SF-2026-ARXIV-2605-17787:start -->
#### Revisiting the Adam-SGD Gap in LLM Pre-Training: The Role of Large Effective Learning Rates

**问题与机制。** Through empirical and theoretical analysis of LLM pre-training dynamics, we identify that training is characterized by small gradient norms and large weight-to-gradient ratios, an effect that becomes more pronounced with larger batch sizes typical in pre-training, necessitating such large effective learning rates. 该 family 改变或挑战 `TRAIN-PRETRAINING` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3 Training Dynamics; §4.1–4.2 clipping`；Evaluation=`Appendix B–C settings and ablations`；Limitations/Counterevidence=`§5 Conclusions; Appendix C.4 seeds`。

<!-- claim:SF-2026-ARXIV-2605-17787:start -->Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-17787:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-17787:end -->

<!-- review:SF-2026-ARXIV-2605-17821:start -->
#### TierCheck: Tiered Checkpointing for Fault Tolerance in Large Language Model Training

**问题与机制。** We propose TierCheck, a cluster-aware tiered checkpointing system that aligns storage placement with failure heterogeneity. 该 family 改变或挑战 `TRAIN-CHECKPOINT` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3 TierCheck Design; §3.1 save/retrieve/reclaim across local, peer and remote tiers`；Evaluation=`§5 Evaluation; failure frequency, checkpoint overhead and recovery`；Limitations/Counterevidence=`§7 Conclusion; no dedicated limitations section, production failure correlation Not Disclosed`。

<!-- claim:SF-2026-ARXIV-2605-17821:start -->只支持 exact-v1 明确披露的模型、数据、硬件、精度、长度、并发与 evaluator；未披露字段为 Not Disclosed，不把模拟、单机或选定 benchmark 外推成生产保证。<!-- claim:SF-2026-ARXIV-2605-17821:end -->

**Books Comparison。** 当前 checkpoint 章有完整/增量 checkpoint 与异步保存，但没有按 failure blast radius 把 local/peer/remote recovery tier 变成同一 durability policy；保留为写回增量。 Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-17821:end -->

<!-- review:SF-2026-ARXIV-2605-17830:start -->
#### Remembering More, Risking More: Longitudinal Safety Risks in Memory-Equipped LLM Agents

**问题与机制。** To isolate memory exposure from stream non-stationarity, we introduce a trigger-probe protocol that evaluates a fixed probe set against read-only memory snapshots at varying prefix lengths, together with a NullMemory counterfactual baseline for identifying memory-induced violations. 该 family 改变或挑战 `AGENT-MEMORY` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3.1–3.5 stateful setting and monitor`；Evaluation=`§4 protocol; §5 results`；Limitations/Counterevidence=`§6 Discussion and limitations`。

<!-- claim:SF-2026-ARXIV-2605-17830:start -->Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-17830:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-17830:end -->

<!-- review:SF-2026-ARXIV-2605-17842:start -->
#### SNLP: Layer-Parallel Inference via Structured Newton Corrections

**问题与机制。** We study whether this layerwise dependency can be relaxed by treating the hidden-state trace across layers as the solution of a nonlinear residual equation and solving it with parallel Newton-style updates. 该 family 改变或挑战 `INFER-TENSORRT-LLM` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3.2–3.5 Structured Newton Layer Parallelism`；Evaluation=`§5.1–5.3 experiments`；Limitations/Counterevidence=`§6 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-17842:start -->Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-17842:end -->

**Books Comparison。** 当前推理执行章覆盖 tensor/pipeline/kernel 并行，但没有把层序列改写为 residual root finding 后并行 correction 的实验分支；保留为受限机制。 Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-17842:end -->

<!-- review:SF-2026-ARXIV-2605-17849:start -->
#### Generating Pretraining Tokens from Organic Data for Data-Bound Scaling

**问题与机制。** In this paper, we introduce SynPro, a synthetic data generation framework that helps LLMs more thoroughly learn from limited organic data. 该 family 改变或挑战 `TRAIN-DATA` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3.1–3.3 model-aware synthesis`；Evaluation=`§4 experiments and analyses`；Limitations/Counterevidence=`§5 limitations`。

<!-- claim:SF-2026-ARXIV-2605-17849:start -->Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-17849:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-17849:end -->

<!-- review:SF-2026-ARXIV-2605-17862:start -->
#### $\boldsymbol{f}$-OPD: Stabilizing Long-Horizon On-Policy Distillation with Freshness-Aware Control

**问题与机制。** Building on this, we introduce a sample-level freshness score that quantifies the reliability of a buffered sample with respect to the on-policy objective. 该 family 改变或挑战 `TRAIN-RLHF` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3.1–3.3 drift decomposition; §4 freshness control`；Evaluation=`§5.1–5.4 experiments`；Limitations/Counterevidence=`§6 limitations`。

<!-- claim:SF-2026-ARXIV-2605-17862:start -->Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-17862:end -->

**Books Comparison。** 当前 post-training 章有 policy version/freshness，但未同时分解 rollout drift 与 supervision drift 并以 freshness controller 控制异步 OPD；保留为写回增量。 Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-17862:end -->

<!-- review:SF-2026-ARXIV-2605-17877:start -->
#### PAIR: Prefix-Aware Internal Reward Model for Multi-Turn Agent Optimization

**问题与机制。** Existing remedies such as running full rollouts to assign step-level advantages, calling external LLM judges at each step, or computing intrinsic rewards that require ground-truth answers at every evaluation introduce significant costs or practical constraints. 该 family 改变或挑战 `TRAIN-RLHF` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3 PAIR; prefix-aware dense reward construction and intervention`；Evaluation=`§4 Experiments; multi-turn agent optimization and ablations`；Limitations/Counterevidence=`Appendix J Limitations`。

<!-- claim:SF-2026-ARXIV-2605-17877:start -->只支持 exact-v1 明确披露的模型、数据、硬件、精度、长度、并发与 evaluator；未披露字段为 Not Disclosed，不把模拟、单机或选定 benchmark 外推成生产保证。<!-- claim:SF-2026-ARXIV-2605-17877:end -->

**Books Comparison。** 当前 RLHF 章讨论 outcome/step reward 与 verifier，但没有把不可控 prefix contamination 从当前 action 的 dense credit 中分离；保留为写回增量。 Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-17877:end -->

<!-- review:SF-2026-ARXIV-2605-17879:start -->
#### Guard: Scalable Straggler Detection and Node Health Management for Large-Scale Training

**问题与机制。** In this paper, we present Guard, a scalable system for detecting stragglers and ensuring node health in large-scale training clusters. 该 family 改变或挑战 `PLATFORM-MONITORING` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3–§6 Guard architecture; online monitor, offline node sweep and triage`；Evaluation=`§7 Evaluation; fail-slow detection, false positives and cluster overhead`；Limitations/Counterevidence=`§7–§8 claim boundary; no dedicated limitations section`。

<!-- claim:SF-2026-ARXIV-2605-17879:start -->只支持 exact-v1 明确披露的模型、数据、硬件、精度、长度、并发与 evaluator；未披露字段为 Not Disclosed，不把模拟、单机或选定 benchmark 外推成生产保证。<!-- claim:SF-2026-ARXIV-2605-17879:end -->

**Books Comparison。** 当前 monitoring/training 章节缺少在线低开销 fail-slow signal 与离线节点资格复验的分权闭环；保留为写回增量。 Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-17879:end -->

<!-- review:SF-2026-ARXIV-2605-17889:start -->
#### CoX-MoE: Coalesced Expert Execution for High-Throughput MoE Inference with AMX-Enabled CPU-GPU Co-Execution

**问题与机制。** The Mixture-of-Experts (MoE) architecture improves computational efficiency via sparse expert activation, but throughput-oriented inference faces substantial GPU memory pressure due to a significant parameter size and intermediate data. 该 family 改变或挑战 `INFER-TENSORRT-LLM` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3 Motivation; §4.1–4.2 orchestration`；Evaluation=`§5 evaluation`；Limitations/Counterevidence=`§6 discussion and limitations`。

<!-- claim:SF-2026-ARXIV-2605-17889:start -->Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-17889:end -->

**Books Comparison。** 当前 MoE execution 章有 expert offload/placement，但缺少 CPU-GPU coalesced expert execution 对 micro-batch 与中间态搬运的统一控制；保留为写回增量。 Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-17889:end -->

<!-- review:SF-2026-ARXIV-2605-17912:start -->
#### WorldArena 2.0: Extending Embodied World Model Benchmarking on Modality, Functionality and Platform

**问题与机制。** In this work, we introduce WorldArena 2.0, an expanded benchmark that systematically broadens embodied world model evaluation along three dimensions: modality, functionality, and platform. 该 family 改变或挑战 `PLATFORM-EVALUATION-SYSTEM` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3 WorldArena 2.0 benchmark axes and task construction`；Evaluation=`§4 Experiments across modality, functionality and platform`；Limitations/Counterevidence=`§5 Discussion/Conclusion; simulator and selected-model boundary`。

<!-- claim:SF-2026-ARXIV-2605-17912:start -->只支持 exact-v1 明确披露的模型、数据、硬件、精度、长度、并发与 evaluator；未披露字段为 Not Disclosed，不把模拟、单机或选定 benchmark 外推成生产保证。<!-- claim:SF-2026-ARXIV-2605-17912:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-17912:end -->

<!-- review:SF-2026-ARXIV-2605-17921:start -->
#### An Efficient Streaming Video Understanding Framework with Agentic Control

**问题与机制。** Rather than fixing these decisions upfront, we propose R3-Streaming (Remember, Respond, Reason), which formulates streaming video understanding as a cascaded control problem: for each query, the system compresses memory, judges response readiness, and routes computation sequentially, so that each downstream decision builds on progressively refined information states. 该 family 改变或挑战 `INFER-SCHEDULING` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3–§4 R3-Streaming cascaded memory, readiness and compute routing`；Evaluation=`§5 Experiments; latency/accuracy under streaming video workloads`；Limitations/Counterevidence=`§6 Conclusion; no production tail-SLO or failure-recovery evidence`。

<!-- claim:SF-2026-ARXIV-2605-17921:start -->只支持 exact-v1 明确披露的模型、数据、硬件、精度、长度、并发与 evaluator；未披露字段为 Not Disclosed，不把模拟、单机或选定 benchmark 外推成生产保证。<!-- claim:SF-2026-ARXIV-2605-17921:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-17921:end -->

<!-- review:SF-2026-ARXIV-2605-17923:start -->
#### AdaptiveLoad: Towards Efficient Video Diffusion Transformer Training

**问题与机制。** In video generation models, particularly world models, training large-scale video diffusion Transformers (such as DiT and MMDiT) poses significant computational challenges due to the extreme variance in sequence lengths within mixed-mode datasets. 该 family 改变或挑战 `TRAIN-DISTRIBUTED-TRAINING` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3 AdaptiveLoad; dual memory/compute constrained batch construction and fused execution`；Evaluation=`§4 Experiments on video diffusion training`；Limitations/Counterevidence=`§5 Conclusion/limitations; selected models and hardware only`。

<!-- claim:SF-2026-ARXIV-2605-17923:start -->只支持 exact-v1 明确披露的模型、数据、硬件、精度、长度、并发与 evaluator；未披露字段为 Not Disclosed，不把模拟、单机或选定 benchmark 外推成生产保证。<!-- claim:SF-2026-ARXIV-2605-17923:end -->

**Books Comparison。** 当前分布式训练章讨论 packed/variable-length 调度，但没有把 video-DiT sequence 的 memory 与 compute 双约束一起冻结为 batch contract；保留为写回增量。 Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-17923:end -->

<!-- review:SF-2026-ARXIV-2605-17932:start -->
#### Prompt Compression in Diffusion Large Language Models: Evaluating LLMLingua-2 on LLaDA

**问题与机制。** This study examines whether LLMLingua-2 transfers effectively to diffusion large language models (DLLMs), specifically LLaDA-8B-Instruct. 该 family 改变或挑战 `MULTIMODAL-GENERATIVE-PARADIGMS` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§III-A–C compression pipeline`；Evaluation=`§III-D; §IV-A–C`；Limitations/Counterevidence=`§V Discussion; §VII Future Work`。

<!-- claim:SF-2026-ARXIV-2605-17932:start -->Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-17932:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-17932:end -->

<!-- review:SF-2026-ARXIV-2605-17954:start -->
#### A More Word-like Image Tokenization for MLLMs

**问题与机制。** We propose a novel Disentangled Visual Tokenization (DiVT) that clusters patch embeddings into coherent semantic units, so each token corresponds to a distinct visual concept instead of a rigid grid cell. 该 family 改变或挑战 `MULTIMODAL-REPRESENTATION` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§2 motivation; §3.1–3.4 tokenization`；Evaluation=`§4.1–4.4 experiments`；Limitations/Counterevidence=`§5 limitations`。

<!-- claim:SF-2026-ARXIV-2605-17954:start -->Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-17954:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-17954:end -->

<!-- review:SF-2026-ARXIV-2605-17986:start -->
#### LivePI: More Realistic Benchmarking of Agents Against Indirect Prompt Injection

**问题与机制。** We introduce LivePI (Live Prompt Injection), a structured benchmark for IPI risk in a production-like but test-controlled environment. 该 family 改变或挑战 `PLATFORM-EVALUATION-SYSTEM` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3 Threat model and benchmark construction`；Evaluation=`§4–§5 evaluation and defense analysis across live interaction surfaces`；Limitations/Counterevidence=`§6 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-17986:start -->只支持 exact-v1 明确披露的模型、数据、硬件、精度、长度、并发与 evaluator；未披露字段为 Not Disclosed，不把模拟、单机或选定 benchmark 外推成生产保证。<!-- claim:SF-2026-ARXIV-2605-17986:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-17986:end -->

<!-- review:SF-2026-ARXIV-2605-17989:start -->
#### Predictive Prefetching for Retrieval-Augmented Generation

**问题与机制。** In this paper, we propose an advanced asynchronous retrieval framework that enables predictive prefetching aligned with evolving information needs. 该 family 改变或挑战 `AGENT-RAG` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3 Predictive prefetch controller and retrieval-generation overlap`；Evaluation=`§4 Evaluation; latency, retrieval usefulness and prediction error`；Limitations/Counterevidence=`§6 Limitations; stale/incorrect demand and workload boundary`。

<!-- claim:SF-2026-ARXIV-2605-17989:start -->只支持 exact-v1 明确披露的模型、数据、硬件、精度、长度、并发与 evaluator；未披露字段为 Not Disclosed，不把模拟、单机或选定 benchmark 外推成生产保证。<!-- claim:SF-2026-ARXIV-2605-17989:end -->

**Books Comparison。** 当前 RAG 章有同步/异步检索，却没有预测未来 information demand、允许误预测取消并绑定 freshness 的 prefetch control；保留为写回增量。 Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-17989:end -->

<!-- review:SF-2026-ARXIV-2605-17992:start -->
#### PipeANN-Filter: An Efficient Filtered Vector Search System on SSD

**问题与机制。** We propose PipeANN-Filter, an efficient filtered vector search system on SSD. 该 family 改变或挑战 `AGENT-RAG` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3 PipeANN-Filter superset traversal, post-verification and pipelined SSD IO`；Evaluation=`§4–§5 implementation and filtered-ANN evaluation`；Limitations/Counterevidence=`§6 Limitations; index/filter/update boundary`。

<!-- claim:SF-2026-ARXIV-2605-17992:start -->只支持 exact-v1 明确披露的模型、数据、硬件、精度、长度、并发与 evaluator；未披露字段为 Not Disclosed，不把模拟、单机或选定 benchmark 外推成生产保证。<!-- claim:SF-2026-ARXIV-2605-17992:end -->

**Books Comparison。** 当前 filtered ANN 已覆盖 query-aware routing，但没有 SSD superset traversal 与 top-k 后验证之间的 IO/recall contract；保留为写回增量。 Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-17992:end -->

<!-- review:SF-2026-ARXIV-2605-17998:start -->
#### Verify-Gated Completion as Admission Control in a Governed Multi-Agent Runtime: A Bounded Architecture Case Study

**问题与机制。** This preprint studies verify-gated completion as an admission-control pattern for governed multi-agent runtimes: agents may propose completion, but a read-only verifier decides whether the claim is admitted. 该 family 改变或挑战 `AGENT-WORKFLOW` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3–§8 read-only verifier, proposal/admission state and bounded completion protocol`；Evaluation=`§9–§10 architecture case study and failure injection`；Limitations/Counterevidence=`§12 Limitations; bounded case study, not a universal correctness proof`。

<!-- claim:SF-2026-ARXIV-2605-17998:start -->只支持 exact-v1 明确披露的模型、数据、硬件、精度、长度、并发与 evaluator；未披露字段为 Not Disclosed，不把模拟、单机或选定 benchmark 外推成生产保证。<!-- claim:SF-2026-ARXIV-2605-17998:end -->

**Books Comparison。** 当前 workflow 有 verifier/commit，但没有把 completion proposal 与只读 admission authority、bounded packet state 和 fail-closed recovery写成同一完成协议；保留为写回增量。 Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-17998:end -->

<!-- review:SF-2026-ARXIV-2605-18032:start -->
#### PROTEA: Offline Evaluation and Iterative Refinement for Multi-Agent LLM Workflows

**问题与机制。** We present PROTEA, a unified interface for offline, test-driven improvement of multi-agent workflows. 该 family 改变或挑战 `AGENT-WORKFLOW` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§2 architecture; §3.1–3.3 node diagnosis`；Evaluation=`§4.1–4.3 evaluation`；Limitations/Counterevidence=`§5 Conclusion`。

<!-- claim:SF-2026-ARXIV-2605-18032:start -->Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-18032:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-18032:end -->

<!-- review:SF-2026-ARXIV-2605-18041:start -->
#### OmniSelect: Dynamic Modality-Aware Token Compression for Efficient Omni-modal Large Language Models

**问题与机制。** To address this limitation, we propose $\textbf{OmniSelect}$, a training-free, modality-adaptive token pruning framework that dynamically selects appropriate compression strategies for multimodal inputs. 该 family 改变或挑战 `MULTIMODAL-REPRESENTATION` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3 OmniSelect modality-aware token-budget controller`；Evaluation=`§4 Experiments on audio-video OmniLLMs`；Limitations/Counterevidence=`§5 Limitations; model/task-local compression evidence`。

<!-- claim:SF-2026-ARXIV-2605-18041:start -->只支持 exact-v1 明确披露的模型、数据、硬件、精度、长度、并发与 evaluator；未披露字段为 Not Disclosed，不把模拟、单机或选定 benchmark 外推成生产保证。<!-- claim:SF-2026-ARXIV-2605-18041:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-18041:end -->

<!-- review:SF-2026-ARXIV-2605-18053:start -->
#### Protection Is (Nearly) All You Need: Structural Protection Dominates Scoring in Globally Capped KV Eviction

**问题与机制。** We study KV cache eviction under a shared globally capped decode-time harness. 该 family 改变或挑战 `INFER-KV-CACHE` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3–§7 globally capped KV eviction and structural boundary protection`；Evaluation=`§8–§9 evaluation across policies/models and cross-architecture challenge`；Limitations/Counterevidence=`§10.22 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-18053:start -->只支持 exact-v1 明确披露的模型、数据、硬件、精度、长度、并发与 evaluator；未披露字段为 Not Disclosed，不把模拟、单机或选定 benchmark 外推成生产保证。<!-- claim:SF-2026-ARXIV-2605-18053:end -->

**Books Comparison。** 当前 KV eviction 已覆盖 selector/quantizer/fallback，但没有把 prompt/modality boundary 的不可驱逐保护作为 global-cap 前的结构不变量；保留为写回增量。 Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-18053:end -->

<!-- review:SF-2026-ARXIV-2605-18067:start -->
#### PPAI: Enabling Personalized LLM Agent Interoperability for Collaborative Edge Intelligence

**问题与机制。** However, the ever-changing pool of agents and their interchangeable capacity introduce new challenges when it comes to matching queries to agents and balancing loads, compared with existing P2P systems. 该 family 改变或挑战 `AGENT-MULTI-AGENT` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§IV–VI agent scoring and serving game`；Evaluation=`§VIII implementation and experiments`；Limitations/Counterevidence=`§VII Discussion`。

<!-- claim:SF-2026-ARXIV-2605-18067:start -->Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-18067:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-18067:end -->

<!-- review:SF-2026-ARXIV-2605-18071:start -->
#### KVDrive: A Holistic Multi-Tier KV Cache Management System for Long-Context LLM Inference

**问题与机制。** We present KVDrive, a holistic multi-tier KV cache management system spanning GPU memory, host DRAM, and SSD. 该 family 改变或挑战 `INFER-KV-CACHE` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§4–§7 multi-tier KV design`；Evaluation=`§9.1–9.3 experiments`；Limitations/Counterevidence=`§10–§11 conclusion and future work`。

<!-- claim:SF-2026-ARXIV-2605-18071:start -->Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-18071:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-18071:end -->

<!-- review:SF-2026-ARXIV-2605-18106:start -->
#### Symmetry-Compatible Principle for Optimizer Design: Embeddings, LM Heads, SwiGLU MLPs, and MoE Routers

**问题与机制。** We address this disparity by introducing a symmetry-compatible principle for optimizer design: the gradient update rule should be equivariant under the symmetry group acting on the corresponding weight block. 该 family 改变或挑战 `TRAIN-PRETRAINING` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3–§5 symmetry-compatible optimizer design`；Evaluation=`§6 experiments`；Limitations/Counterevidence=`§1 Scope and limitations; §7 discussion`。

<!-- claim:SF-2026-ARXIV-2605-18106:start -->Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-18106:end -->

**Books Comparison。** 当前 optimizer 叙述未把 embedding/LM-head/SwiGLU/MoE-router 的参数对称性作为 optimizer state/action compatibility contract；保留为写回增量。 Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-18106:end -->

<!-- review:SF-2026-ARXIV-2605-18165:start -->
#### Elastic-dLLM: Position Preserving Context Compression and Augmentation of Diffusion LLMs

**问题与机制。** Guided by these findings, we propose position-preserving [MASK] token compression and terminal-aware augmentation. 该 family 改变或挑战 `MULTIMODAL-GENERATIVE-PARADIGMS` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3 mask state; §4.1–4.3 compression`；Evaluation=`§5.1–5.4 experiments`；Limitations/Counterevidence=`§6 limitations`。

<!-- claim:SF-2026-ARXIV-2605-18165:start -->Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-18165:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-18165:end -->

<!-- review:SF-2026-ARXIV-2605-18271:start -->
#### From Volume to Value: Preference-Aligned Memory Construction for On-Device RAG

**问题与机制。** We propose EPIC (Efficient Preference-aligned Index Construction), which focuses on user preferences as a compact and stable form of personal context and integrates them throughout the RAG pipeline. 该 family 改变或挑战 `AGENT-MEMORY` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`PDF pp.3–5 §3.1–3.3 memory construction`；Evaluation=`PDF §4–§5; device experiments`；Limitations/Counterevidence=`PDF §6 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-18271:start -->Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-18271:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-18271:end -->

<!-- review:SF-2026-ARXIV-2605-18401:start -->
#### SkillsVote: Lifecycle Governance of Agent Skills from Collection, Recommendation to Evolution

**问题与机制。** We present SkillsVote, a lifecycle-governance framework for Agent Skills across collection, recommendation, attribution, and evolution. 该 family 改变或挑战 `AGENT-PLATFORM` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3 SkillsVote collection, recommendation, validation and evolution lifecycle`；Evaluation=`§4 Experiments and lifecycle ablations`；Limitations/Counterevidence=`§5/Appendix limitations; ecosystem and environment sensitivity`。

<!-- claim:SF-2026-ARXIV-2605-18401:start -->只支持 exact-v1 明确披露的模型、数据、硬件、精度、长度、并发与 evaluator；未披露字段为 Not Disclosed，不把模拟、单机或选定 benchmark 外推成生产保证。<!-- claim:SF-2026-ARXIV-2605-18401:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-18401:end -->

<!-- review:SF-2026-ARXIV-2605-18414:start -->
#### Prompts Don't Protect: Architectural Enforcement via MCP Proxy for LLM Tool Access Control

**问题与机制。** We identify a critical gap: when unauthorized tools are visible in an agent's context, models select them in 48-68% of adversarial scenarios, even when explicitly instructed not to. 该 family 改变或挑战 `AGENT-MCP` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3 governed MCP proxy`；Evaluation=`§4–§5 benchmark and results`；Limitations/Counterevidence=`§6–§7 discussion and threat-model limits`。

<!-- claim:SF-2026-ARXIV-2605-18414:start -->Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-18414:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-18414:end -->

<!-- review:SF-2026-ARXIV-2605-18421:start -->
#### EvoMemBench: Benchmarking Agent Memory from a Self-Evolving Perspective

**问题与机制。** In this paper, we study agent memory from a self-evolving perspective and introduce EvoMemBench, a unified benchmark organized along two axes: memory scope (in-episode vs. 该 family 改变或挑战 `AGENT-MEMORY` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3–§4 EvoMemBench in/cross-episode and knowledge/execution axes`；Evaluation=`§5 Experiments across memory systems`；Limitations/Counterevidence=`§6 Conclusion; benchmark/model coverage boundary`。

<!-- claim:SF-2026-ARXIV-2605-18421:start -->只支持 exact-v1 明确披露的模型、数据、硬件、精度、长度、并发与 evaluator；未披露字段为 Not Disclosed，不把模拟、单机或选定 benchmark 外推成生产保证。<!-- claim:SF-2026-ARXIV-2605-18421:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-18421:end -->

<!-- review:SF-2026-ARXIV-2605-18498:start -->
#### DBES: A Systematic Benchmark and Metric Suite for Evaluating Expert Specialization in Large-Scale MoEs

**问题与机制。** We introduce DBES, a comprehensive diagnostic framework combining a multi-domain benchmark with five theoretically grounded metrics: Routing Specialization, Normalized Effective Rank, Domain Isolation, Routing Stiffness Score, and N-gram Expertise measures. 该 family 改变或挑战 `PLATFORM-EVALUATION-SYSTEM` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`PDF pp.3–5 §3 routing-specialization metrics`；Evaluation=`PDF pp.5–11 §4 experiments and intervention`；Limitations/Counterevidence=`PDF p.11 §4.3 intervention boundary; §5 Conclusion`。

<!-- claim:SF-2026-ARXIV-2605-18498:start -->Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-18498:end -->

**Books Comparison。** 当前 evaluation 章缺少将 MoE load balance 与 functional specialization 分开、并用干预验证而非只看 routing frequency 的契约；保留为写回增量。 Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-18498:end -->

<!-- review:SF-2026-ARXIV-2605-18565:start -->
#### MINTEval: Evaluating Memory under Multi-Target Interference in Long-Horizon Agent Systems

**问题与机制。** In this paper, we study how current memory-augmented agents perform in realistic, interference-heavy, long-horizon settings across diverse domains and question types. 该 family 改变或挑战 `AGENT-MEMORY` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3 MINTEval multi-target interference construction and update semantics`；Evaluation=`§4 Experiments; recall and aggregation under evolving memories`；Limitations/Counterevidence=`§5 Limitations; synthetic tasks and selected agents`。

<!-- claim:SF-2026-ARXIV-2605-18565:start -->只支持 exact-v1 明确披露的模型、数据、硬件、精度、长度、并发与 evaluator；未披露字段为 Not Disclosed，不把模拟、单机或选定 benchmark 外推成生产保证。<!-- claim:SF-2026-ARXIV-2605-18565:end -->

**Books Comparison。** 当前 memory 章覆盖版本与冲突，但没有把 multi-target interference、update history 与 aggregate reasoning 组合成一条验收轴；保留为写回增量。 Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-18565:end -->

<!-- review:SF-2026-ARXIV-2605-18583:start -->
#### Overeager Coding Agents: Measuring Out-of-Scope Actions on Benign Tasks

**问题与机制。** We present OverEager-Gen, a benchmark dedicated to overeager behavior on benign tasks. 该 family 改变或挑战 `PLATFORM-SECURITY` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3 benchmark, benign task scope and overeager-action taxonomy`；Evaluation=`§4 Experiments across coding agents`；Limitations/Counterevidence=`§5 Limitations; harness and observable-action boundary`。

<!-- claim:SF-2026-ARXIV-2605-18583:start -->只支持 exact-v1 明确披露的模型、数据、硬件、精度、长度、并发与 evaluator；未披露字段为 Not Disclosed，不把模拟、单机或选定 benchmark 外推成生产保证。<!-- claim:SF-2026-ARXIV-2605-18583:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-18583:end -->

<!-- review:SF-2026-ARXIV-2605-18607:start -->
#### Forecasting Downstream Performance of LLMs With Proxy Metrics

**问题与机制。** Instead, we propose to construct proxy metrics by aggregating token-level statistics, such as entropy, top-k accuracy, and expert token rank, from a candidate model's next token distribution over expert-written solutions. 该 family 改变或挑战 `PLATFORM-EVALUATION-SYSTEM` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3 proxy metrics`；Evaluation=`§4–§5 model/data ranking`；Limitations/Counterevidence=`§6 limitations`。

<!-- claim:SF-2026-ARXIV-2605-18607:start -->Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-18607:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-18607:end -->

<!-- review:SF-2026-ARXIV-2605-18652:start -->
#### MementoGUI: Learning Agentic Multimodal Memory Control for Long-Horizon GUI Agents

**问题与机制。** To address these limitations, we introduce \textbf{MementoGUI}, a plug-in agentic memory framework that equips MLLM-based GUI agents with \textbf{MementoCore}, a learned controller for online memory selection, compression, and retrieval. 该 family 改变或挑战 `AGENT-MEMORY` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3 MementoGUI multimodal memory controller and write/read policy`；Evaluation=`§4–§5 benchmark construction and experiments`；Limitations/Counterevidence=`§6 Limitations; GUI domain and selected backbones`。

<!-- claim:SF-2026-ARXIV-2605-18652:start -->只支持 exact-v1 明确披露的模型、数据、硬件、精度、长度、并发与 evaluator；未披露字段为 Not Disclosed，不把模拟、单机或选定 benchmark 外推成生产保证。<!-- claim:SF-2026-ARXIV-2605-18652:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-18652:end -->

<!-- review:SF-2026-ARXIV-2605-18693:start -->
#### SkillGenBench: Benchmarking Skill Generation Pipelines for LLM Agents

**问题与机制。** Existing benchmarks primarily evaluate the efficacy of given skills or the ability of agents to solve downstream tasks from raw context, but they do not isolate skill generation itself as the object of study. 该 family 改变或挑战 `AGENT-PLATFORM` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3.1–3.4 skill-generation artifact contract`；Evaluation=`§4.1–4.4 execution evaluation`；Limitations/Counterevidence=`§5 Conclusion; appendix sensitivity`。

<!-- claim:SF-2026-ARXIV-2605-18693:start -->Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-18693:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-18693:end -->

<!-- review:SF-2026-ARXIV-2605-18697:start -->
#### PopPy: Opportunistically Exploiting Parallelism in Python Compound AI Applications

**问题与机制。** To address this problem, we develop PopPy, a system that can uncover parallelization opportunities in Python applications that invoke these heavy external components, including those used in compound AI applications. 该 family 改变或挑战 `AGENT-WORKFLOW` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3–§6 PopPy compiler/runtime dependency discovery and external-call parallelism`；Evaluation=`§8 Evaluation; latency and semantic-equivalence checks`；Limitations/Counterevidence=`§10 Discussion; Python/compound-application boundary`。

<!-- claim:SF-2026-ARXIV-2605-18697:start -->只支持 exact-v1 明确披露的模型、数据、硬件、精度、长度、并发与 evaluator；未披露字段为 Not Disclosed，不把模拟、单机或选定 benchmark 外推成生产保证。<!-- claim:SF-2026-ARXIV-2605-18697:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-18697:end -->

<!-- review:SF-2026-ARXIV-2605-18703:start -->
#### EnvFactory: Scaling Tool-Use Agents via Executable Environments Synthesis and Robust RL

**问题与机制。** We introduce EnvFactory, a fully automated framework that addresses both challenges. 该 family 改变或挑战 `AGENT-WORKFLOW` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3–§4 executable-environment synthesis, verification and RL data path`；Evaluation=`§5 Evaluation of environment validity and agent training`；Limitations/Counterevidence=`§6 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-18703:start -->只支持 exact-v1 明确披露的模型、数据、硬件、精度、长度、并发与 evaluator；未披露字段为 Not Disclosed，不把模拟、单机或选定 benchmark 外推成生产保证。<!-- claim:SF-2026-ARXIV-2605-18703:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-18703:end -->

<!-- review:SF-2026-ARXIV-2605-18710:start -->
#### Mosaic: Towards Efficient Training of Multimodal Models with Spatial Resource Multiplexing

**问题与机制。** To improve GPU utilization and enable efficient MM training, we propose deploying MMs in a temporal-spatial multiplexing manner, allowing multiple MM modules to colocate on a GPU with well-controlled resource quotas. 该 family 改变或挑战 `TRAIN-DISTRIBUTED-TRAINING` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3 Mosaic spatial resource multiplexing, placement and performance model`；Evaluation=`§4 Evaluation across multimodal module mixtures`；Limitations/Counterevidence=`§5 Limitations; selected architectures/hardware`。

<!-- claim:SF-2026-ARXIV-2605-18710:start -->只支持 exact-v1 明确披露的模型、数据、硬件、精度、长度、并发与 evaluator；未披露字段为 Not Disclosed，不把模拟、单机或选定 benchmark 外推成生产保证。<!-- claim:SF-2026-ARXIV-2605-18710:end -->

**Books Comparison。** 当前 multimodal/distributed training 章缺少空间复用时 module placement、GPU share 与 interference budget 的联合 owner；保留为写回增量。 Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-18710:end -->

<!-- review:SF-2026-ARXIV-2605-18739:start -->
#### LongLive-2.0: An NVFP4 Parallel Infrastructure for Long Video Generation

**问题与机制。** We present LongLive-2.0, an NVFP4-based parallel infrastructure throughout the full training and inference workflow of long video generation, addressing speed and memory bottlenecks. 该 family 改变或挑战 `TRAIN-DISTRIBUTED-TRAINING` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3–§4 NVFP4 training/inference infrastructure and parallel layouts`；Evaluation=`§5 Evaluation on long-video generation`；Limitations/Counterevidence=`§6 Limitations; vendor precision and workload boundary`。

<!-- claim:SF-2026-ARXIV-2605-18739:start -->只支持 exact-v1 明确披露的模型、数据、硬件、精度、长度、并发与 evaluator；未披露字段为 Not Disclosed，不把模拟、单机或选定 benchmark 外推成生产保证。<!-- claim:SF-2026-ARXIV-2605-18739:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-18739:end -->

<!-- review:SF-2026-ARXIV-2605-18750:start -->
#### A Readiness-Driven Runtime for Pipeline-Parallel Training under Runtime Variability

**问题与机制。** We present Runtime-Readiness-First Pipeline (RRFP), a readiness-driven runtime for pipeline-parallel training. 该 family 改变或挑战 `TRAIN-PIPELINE-PARALLEL` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3 readiness-driven runtime and dependency state`；Evaluation=`§4–§5 implementation and evaluation under runtime variability`；Limitations/Counterevidence=`§6 Limitations; schedule/hardware/workload boundary`。

<!-- claim:SF-2026-ARXIV-2605-18750:start -->只支持 exact-v1 明确披露的模型、数据、硬件、精度、长度、并发与 evaluator；未披露字段为 Not Disclosed，不把模拟、单机或选定 benchmark 外推成生产保证。<!-- claim:SF-2026-ARXIV-2605-18750:end -->

**Books Comparison。** 当前 pipeline 章以 schedule 为主，但没有在运行时以真实 task readiness 取得 dispatch authority并保留静态 schedule fallback；保留为写回增量。 Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-18750:end -->

<!-- review:SF-2026-ARXIV-2605.16588:start -->
#### Policy Library CBF: Finite-Horizon Safety at Runtime via Parallel Rollouts

问题与约束：Safety-critical autonomy in unstructured environments poses significant challenges for online safety certification under evolving constraints.

机制与 ownership：We propose Policy Library Control Barrier Function~(PL-CBF), a runtime safety filter that evaluates a library of fallback policies via parallel finite-horizon rollouts, selects the least invasive safe mode, and enforces safety by solving a quadratic program that minimally modifies a nominal policy.

Evaluation contract：We propose Policy Library Control Barrier Function~(PL-CBF), a runtime safety filter that evaluates a library of fallback policies via parallel finite-horizon rollouts, selects the least invasive safe mode, and enforces safety by solving a quadratic program that minimally modifies a nominal policy.

Trade-off / failure：The mechanism described in `§IV Policy Library CBF` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `§VII Conclusion; no dedicated limitations heading` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605.16588:start -->`Policy Library CBF: Finite-Horizon Safety at Runtime via Parallel Rollouts` is supported only under the v1-disclosed workload and evaluator behind `§§V–VI theoretical and empirical evaluation`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605.16588:end -->

Books Decision=`No Change — Existing Coverage`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605.16588`。
<!-- review:SF-2026-ARXIV-2605.16588:end -->

<!-- review:SF-2026-ARXIV-2605.16622:start -->
#### Does Weight Decay Enhance Training Stability?

问题与约束：In modern deep learning, weight decay is often credited with "stabilizing" training dynamics, diverging from its classical role as a static regularization penalty.

机制与 ownership：We develop a mathematical framework that accurately models these phenomena and identify the global alignment of the parameter vector and the sharpness gradient as the mechanistic driver of the phase transition.

Evaluation contract：We show that weight decay robustly slows *progressive sharpening}.

Trade-off / failure：The mechanism described in `4 The Mechanism is Global Interaction` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `7 Limitations` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605.16622:start -->`Does Weight Decay Enhance Training Stability?` is supported only under the v1-disclosed workload and evaluator behind `3 Weight Decay Empirically Changes EoS Dynamics`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605.16622:end -->

Books Decision=`Integrate`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605.16622`。
<!-- review:SF-2026-ARXIV-2605.16622:end -->

<!-- review:SF-2026-ARXIV-2605.16647:start -->
#### Public-Decay Homomorphic State Space Models for Private Sequence Inference

问题与约束：Fully homomorphic encryption (FHE) changes sequence-model design because rotations, encrypted products, ciphertext materialization, multiplicative depth, and bootstrapping pressure can dominate ordinary neural-network costs.

机制与 ownership：This paper presents public-decay homomorphic state space models (HSSMs), recurrent/state-space blocks whose carried state is updated through ciphertext-plaintext public decay while ciphertext-ciphertext multiplication remains on a local write path.

Evaluation contract：The evaluated workflow separates client-side tokenization, frozen fastText lookup, projection, clipping, encryption, decryption, and thresholding from server-side encrypted evaluation over bounded projected features.

Trade-off / failure：The mechanism described in `3 Problem Formulation` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `8 Discussion and Limitations` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605.16647:start -->`Public-Decay Homomorphic State Space Models for Private Sequence Inference` is supported only under the v1-disclosed workload and evaluator behind `5 Complexity and Noise Analysis`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605.16647:end -->

Books Decision=`No Change — Existing Coverage`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605.16647`。
<!-- review:SF-2026-ARXIV-2605.16647:end -->

<!-- review:SF-ANNEAL-GOVERNED-SYMBOLIC-PATCHES:start -->
### ANNEAL: Adapting LLM Agents via Governed Symbolic Patch Learning

问题与旧路径：Agent adaptation can commit governed symbolic patches with explicit admission and rollback rather than silently mutating prompts or weights from experience. 旧方案在工作负载较小、状态可丢弃、风险低或边界固定时仍然合理。 exact-v1 的机制定位为 `arXiv:2605.16309v1 HTML, Method/Design section; abstract mechanism: We introduce ANNEAL, a neuro-symbolic agent that converts recurring failures into governed symbolic edits of a process knowledge graph without modifying foundation model weights.`。这改变的是可观测状态、控制 owner 或评价证据，而不是仅增加一个模型名称。

Evaluation contract：`arXiv:2605.16309v1 HTML, Experiments/Evaluation and ablation sections; abstract scope: Across four domains and 27 multi-seed runs, ANNEAL is the only evaluated system that commits persistent structural repairs--strong baselines such as ReAct and Reflexion achieve high episodic recovery…`。这里的作者实验只证明其披露模型、数据、硬件、精度和实现条件内的结果；未披露字段保持 Not Disclosed。 反证边界：`arXiv:2605.16309v1 HTML, Discussion/Limitations and threat-to-validity passages; no cross-workload generalization inferred`。Artifact：`arXiv:2605.16309v1 HTML, artifact/code statement; immutable event-time commit is Not Disclosed unless explicitly named`。 <!-- claim:SF-ANNEAL-GOVERNED-SYMBOLIC-PATCHES:start -->长期结论只保留为：Agent adaptation can commit governed symbolic patches with explicit admission and rollback rather than silently mutating prompts or weights from experience. 它不证明该实现跨 workload 普遍最优，也不能代替独立复现、fallback 与 rollback。<!-- claim:SF-ANNEAL-GOVERNED-SYMBOLIC-PATCHES:end -->
<!-- review:SF-ANNEAL-GOVERNED-SYMBOLIC-PATCHES:end -->

<!-- review:SF-FRE-RES-FREQUENCY-RESIDUAL-VIDEO-TOKEN-COMPRESSION-FOR-EFFICIENT-VIDEO-M:start -->
#### Fre-Res: Frequency-Residual Video Token Compression for Efficient Video MLLMs

问题与机制：We propose \textbf{Fre-Res}, a budget-adaptive dual-track video-token compression framework that separates these two forms of evidence.。状态 owner=`MULTIMODAL-REPRESENTATION`；机制改变的是该 owner 下的条件化 state/data/control 或 evaluation contract，而不是把论文名称当作长期结论。
Method locator：`arXiv:2605.16366v1 — §3 frequency-residual compression and spatial absorber — mechanism: We propose \textbf{Fre-Res}, a budget-adaptive dual-track video-token compression framework that separates these two forms of evidence.`；evaluation locator：`arXiv:2605.16366v1 — §4 short/long-video evaluation and ablations — disclosed evaluation scope only`；counterevidence/limitations：`arXiv:2605.16366v1 — §Limitations / Counterevidence — limitations: vision encoder, temporal-frequency assumptions and token budget — non-proof boundary retained`；artifact：`arXiv:2605.16366v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-FRE-RES-FREQUENCY-RESIDUAL-VIDEO-TOKEN-COMPRESSION-FOR-EFFICIENT-VIDEO-M:start -->证据只支持 exact-v1 披露的模型、数据、硬件、精度、长度、batch、并发、SLO 与 evaluator；未披露字段均为 Not Disclosed，作者 benchmark 不外推为通用结论。<!-- claim:SF-FRE-RES-FREQUENCY-RESIDUAL-VIDEO-TOKEN-COMPRESSION-FOR-EFFICIENT-VIDEO-M:end -->
旧方案在固定 workload、较低规模/风险或无需新增状态 owner 时仍成立；新机制获得更强控制或可观测性，同时引入分类器/控制器误差、额外状态、迁移成本或新的攻击面，需由 owner chapter 保留 fallback 与 coexistence。
<!-- review:SF-FRE-RES-FREQUENCY-RESIDUAL-VIDEO-TOKEN-COMPRESSION-FOR-EFFICIENT-VIDEO-M:end -->

<!-- review:SF-MIXING-TIMES-OF-GLAUBER-DYNAMICS-ON-MASKED-LANGUAGE-MODELS:start -->
#### Mixing Times of Glauber Dynamics on Masked Language Models

问题与机制：We first show that MLM conditionals are intrinsically incompatible: we introduce a rectangle test that certifies this incompatibility and empirically verify its prevalence across modern MLMs.。状态 owner=`MULTIMODAL-GENERATIVE-PARADIGMS`；机制改变的是该 owner 下的条件化 state/data/control 或 evaluation contract，而不是把论文名称当作长期结论。
Method locator：`arXiv:2605.16378v1 — §3 rectangle incompatibility test; §4–§5 mixing theory — mechanism: We first show that MLM conditionals are intrinsically incompatible: we introduce a rectangle test that certifies this incompatibility and empirically verify its prevalence across modern MLMs.`；evaluation locator：`arXiv:2605.16378v1 — §6 BERT/RoBERTa chain experiments — disclosed evaluation scope only`；counterevidence/limitations：`arXiv:2605.16378v1 — §7 limitations: loose bounds, classifier dependence and unknown stationary law — non-proof boundary retained`；artifact：`arXiv:2605.16378v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-MIXING-TIMES-OF-GLAUBER-DYNAMICS-ON-MASKED-LANGUAGE-MODELS:start -->证据只支持 exact-v1 披露的模型、数据、硬件、精度、长度、batch、并发、SLO 与 evaluator；未披露字段均为 Not Disclosed，作者 benchmark 不外推为通用结论。<!-- claim:SF-MIXING-TIMES-OF-GLAUBER-DYNAMICS-ON-MASKED-LANGUAGE-MODELS:end -->
旧方案在固定 workload、较低规模/风险或无需新增状态 owner 时仍成立；新机制获得更强控制或可观测性，同时引入分类器/控制器误差、额外状态、迁移成本或新的攻击面，需由 owner chapter 保留 fallback 与 coexistence。
<!-- review:SF-MIXING-TIMES-OF-GLAUBER-DYNAMICS-ON-MASKED-LANGUAGE-MODELS:end -->

<!-- review:SF-ORBISIM-WORLD-MODELS-AS-DIFFERENTIABLE-PHYSICS-ENGINES-FOR-EMBODIED-INTE:start -->
#### OrbiSim: World Models as Differentiable Physics Engines for Embodied Intelligence

问题与机制：We present OrbiSim, a novel robotic simulation paradigm that redefines world models as a fully differentiable physics engine for embodied intelligence.。机制 owner=`MULTIMODAL-WORLD-MODELS`。
全文定位：`arXiv:2605.16395v1 HTML — §3 OrbiSim persistent world-state simulator`；evaluation=`arXiv:2605.16395v1 — §4 interactive-world evaluation`；limitations/counterevidence=`arXiv:2605.16395v1 — §5 limitations: environment fidelity and action space`。
<!-- claim:SF-ORBISIM-WORLD-MODELS-AS-DIFFERENTIABLE-PHYSICS-ENGINES-FOR-EMBODIED-INTE:start -->证据只支持 exact-v1 披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨部署的一般优势，也不把作者 benchmark 变成生产承诺。<!-- claim:SF-ORBISIM-WORLD-MODELS-AS-DIFFERENTIABLE-PHYSICS-ENGINES-FOR-EMBODIED-INTE:end -->
Books Decision=`No Change — Existing Coverage`。旧方案在新增约束不存在、证据越界或 fallback 被触发时继续成立。
<!-- review:SF-ORBISIM-WORLD-MODELS-AS-DIFFERENTIABLE-PHYSICS-ENGINES-FOR-EMBODIED-INTE:end -->

<!-- review:SF-ORTH-DION-ELIMINATING-GEOMETRIC-MISMATCH-IN-DISTRIBUTED-LOW-RANK-SPECTRA:start -->
#### Orth-Dion: Eliminating Geometric Mismatch in Distributed Low-Rank Spectral Optimization

机制边界：We show that this gap is geometric: column normalization does not yield the rank-$r$ polar factor that Muon implicitly targets, so the resulting direction violates the dual-norm constraint of the low-rank spectral geometry, and the rate picks up…。Method/identity locator：`https://arxiv.org/html/2605.16341v1 §3 Geometric Mismatch; §4 Orth-Dion — mechanism: We show that this gap is geometric: column normalization does not yield the rank-$r$ polar factor that Muon implicitly targets, so the resulting direction violates the dual-norm constraint of the low-rank spectral geometry, and the rate picks up…`；evaluation locator：`https://arxiv.org/html/2605.16341v1 §5 Theory; §6 LLM Pretraining Experiments — disclosed evaluation scope only`；counterevidence/limitations：`https://arxiv.org/html/2605.16341v1 §7 Limitations and Adaptive-Rank Cost — no generalization beyond disclosed workload/model/evaluator`；artifact locator：`https://arxiv.org/html/2605.16341v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-ORTH-DION-ELIMINATING-GEOMETRIC-MISMATCH-IN-DISTRIBUTED-LOW-RANK-SPECTRA:start -->结论只适用于 exact-v1 披露的模型、数据、硬件、并发和 evaluator；未披露条件一律为 Not Disclosed，不把作者 benchmark 外推为通用 SLO。<!-- claim:SF-ORTH-DION-ELIMINATING-GEOMETRIC-MISMATCH-IN-DISTRIBUTED-LOW-RANK-SPECTRA:end -->
旧方案在固定 workload、低风险或无需跨层协调时仍成立；本证据只改变所列 owner 的条件化设计判断。
<!-- review:SF-ORTH-DION-ELIMINATING-GEOMETRIC-MISMATCH-IN-DISTRIBUTED-LOW-RANK-SPECTRA:end -->

<!-- review:SF-PROOF-CARRYING-CERTIFICATES-FOR-LLM-PIPELINES-A-TRUST-BOUNDARY-ARCHITECT:start -->
#### Proof-Carrying Certificates for LLM Pipelines: A Trust-Boundary Architecture

问题与机制：We present a framework for verifying the deterministic structured computations surrounding a large language model rather than the model itself, extending a Lean 4 trust-boundary architecture to the generic interfaces of modern LLM pipelines.。机制 owner=`PLATFORM-SECURITY`。
全文定位：`arXiv:2605.16407v1 HTML — §Method / System Design — Proof-Carrying Certificates for LLM Pipelines: A Trust-Boundary Architecture 的机制、状态 owner 与控制/数据流`；evaluation=`§Experiments / Evaluation — Proof-Carrying Certificates for LLM Pipelines: A Trust-Boundary Architecture 的作者披露 workload、baseline 与 ablation`；limitations/counterevidence=`§Limitations / Discussion — Proof-Carrying Certificates for LLM Pipelines: A Trust-Boundary Architecture 的适用范围、未证明项与 failure boundary`。
<!-- claim:SF-PROOF-CARRYING-CERTIFICATES-FOR-LLM-PIPELINES-A-TRUST-BOUNDARY-ARCHITECT:start -->只支持 exact-v1 披露的 workload、模型、硬件、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。该证据不证明跨模型/硬件/部署的一般优势。<!-- claim:SF-PROOF-CARRYING-CERTIFICATES-FOR-LLM-PIPELINES-A-TRUST-BOUNDARY-ARCHITECT:end -->
Books Decision=`No Change — Existing Coverage`。旧方案在固定 workload、较低风险或无需新增 owner 时仍成立；新机制引入的分类器/控制器误差、额外状态、迁移成本与攻击面必须与 fallback/coexistence 同时进入 owner narrative。
<!-- review:SF-PROOF-CARRYING-CERTIFICATES-FOR-LLM-PIPELINES-A-TRUST-BOUNDARY-ARCHITECT:end -->

<!-- review:SF-SELFPLAY-DECISION-CAPACITY-COLLAPSE:start -->
### A Structural Threshold in Decision Capacity Governs Collapse in Self-Play Reinforcement Learning

问题与旧路径：Self-play can collapse when policy decision capacity crosses an environment-dependent threshold; more optimization is not monotonic capability improvement. 旧方案在工作负载较小、状态可丢弃、风险低或边界固定时仍然合理。 exact-v1 的机制定位为 `arXiv:2605.16315v1 HTML, Method/Design section; abstract mechanism: We show that a threshold in decision capacity determines whether self-play reinforcement learning agents collapse under asymmetric rule perturbations.`。这改变的是可观测状态、控制 owner 或评价证据，而不是仅增加一个模型名称。

Evaluation contract：`arXiv:2605.16315v1 HTML, Experiments/Evaluation and ablation sections; abstract scope: Across poker variants, matrix games, a dice game, and multiple learning algorithms, eliminating all positive-reach contingent decisions causes rapid convergence to a deterministic exploitation attractor, a fixed point…`。这里的作者实验只证明其披露模型、数据、硬件、精度和实现条件内的结果；未披露字段保持 Not Disclosed。 反证边界：`arXiv:2605.16315v1 HTML, Discussion/Limitations and threat-to-validity passages; no cross-workload generalization inferred`。Artifact：`arXiv:2605.16315v1 HTML, artifact/code statement; immutable event-time commit is Not Disclosed unless explicitly named`。 <!-- claim:SF-SELFPLAY-DECISION-CAPACITY-COLLAPSE:start -->长期结论只保留为：Self-play can collapse when policy decision capacity crosses an environment-dependent threshold; more optimization is not monotonic capability improvement. 它不证明该实现跨 workload 普遍最优，也不能代替独立复现、fallback 与 rollback。<!-- claim:SF-SELFPLAY-DECISION-CAPACITY-COLLAPSE:end -->
<!-- review:SF-SELFPLAY-DECISION-CAPACITY-COLLAPSE:end -->

<!-- review:SF-SIGNMUON-SIGN-ORTHOGONALIZED-OPTIMIZER:start -->
### SignMuon: Communication-Efficient Distributed Muon Optimization

问题与旧路径：Sign-based orthogonalized updates are a bounded optimizer branch; they reinforce, but do not replace, the existing gradient-geometry and conditioning contract. 旧方案在工作负载较小、状态可丢弃、风险低或边界固定时仍然合理。 exact-v1 的机制定位为 `arXiv:2605.16311v1 HTML, Method/Design section; abstract mechanism: We propose Sign-Muon, a 1-bit, matrix-aware optimizer that combines majority-vote sign aggregation from signSGD with the polar-step framework of Muon.`。这改变的是可观测状态、控制 owner 或评价证据，而不是仅增加一个模型名称。

Evaluation contract：`arXiv:2605.16311v1 HTML, Experiments/Evaluation and ablation sections; abstract scope: With unimodal symmetric noise, majority vote across $M$ workers cuts the stochastic term by $1/\sqrt{M}$, matching signSGD.`。这里的作者实验只证明其披露模型、数据、硬件、精度和实现条件内的结果；未披露字段保持 Not Disclosed。 反证边界：`arXiv:2605.16311v1 HTML, Discussion/Limitations and threat-to-validity passages; no cross-workload generalization inferred`。Artifact：`arXiv:2605.16311v1 HTML, artifact/code statement; immutable event-time commit is Not Disclosed unless explicitly named`。 <!-- claim:SF-SIGNMUON-SIGN-ORTHOGONALIZED-OPTIMIZER:start -->长期结论只保留为：Sign-based orthogonalized updates are a bounded optimizer branch; they reinforce, but do not replace, the existing gradient-geometry and conditioning contract. 它不证明该实现跨 workload 普遍最优，也不能代替独立复现、fallback 与 rollback。<!-- claim:SF-SIGNMUON-SIGN-ORTHOGONALIZED-OPTIMIZER:end -->
<!-- review:SF-SIGNMUON-SIGN-ORTHOGONALIZED-OPTIMIZER:end -->

## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-16265 | exact-v1 evaluation for AgentWall: A Runtime Safety Layer for Local AI Agents | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | paper authors |
| SF-ANNEAL-GOVERNED-SYMBOLIC-PATCHES | exact-v1 disclosed workload for ANNEAL: Adapting LLM Agents via Governed Symbolic Patch Learning | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-SELFPLAY-DECISION-CAPACITY-COLLAPSE | exact-v1 disclosed workload for A Structural Threshold in Decision Capacity Governs Collapse in Self-Play Reinforcement Learning | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-SIGNMUON-SIGN-ORTHOGONALIZED-OPTIMIZER | exact-v1 disclosed workload for SignMuon: Communication-Efficient Distributed Muon Optimization | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-16265 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-16265 |
| SF-2026-ARXIV-2605-16346 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-16346 |
| SF-2026-ARXIV-2605-16360 | forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-16360 |
| SF-2026-ARXIV-2605-16436 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-16436 |
| SF-2026-ARXIV-2605-16439 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-16439 |
| SF-2026-ARXIV-2605-16508 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-16508 |
| SF-2026-ARXIV-2605-16565 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-16565 |
| SF-2026-ARXIV-2605-16604 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-16604 |
| SF-2026-ARXIV-2605-16616 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-16616 |
| SF-2026-ARXIV-2605-16626 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-16626 |
| SF-2026-ARXIV-2605-16630 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-16630 |
| SF-2026-ARXIV-2605-16637 | score_7_9 | selected | DA-20260519-01 | — | Score=9/9 且属于当日最高跨系统设计影响；有限叙事预算不替代其余 Source Review。 | analysis:DA-20260519-01 |
| SF-2026-ARXIV-2605-16650 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-16650 |
| SF-2026-ARXIV-2605-16704 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-16704 |
| SF-2026-ARXIV-2605-16712 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-16712 |
| SF-2026-ARXIV-2605-16725 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-16725 |
| SF-2026-ARXIV-2605-16745 | score_7_9;forced_review;potential_books_delta | selected | DA-20260519-02 | — | Score=9/9 且属于当日最高跨系统设计影响；有限叙事预算不替代其余 Source Review。 | analysis:DA-20260519-02 |
| SF-2026-ARXIV-2605-16746 | score_7_9 | selected | DA-20260519-03 | — | Score=9/9 且属于当日最高跨系统设计影响；有限叙事预算不替代其余 Source Review。 | analysis:DA-20260519-03 |
| SF-2026-ARXIV-2605-16776 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-16776 |
| SF-2026-ARXIV-2605-16786 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-16786 |
| SF-2026-ARXIV-2605-16787 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-16787 |
| SF-2026-ARXIV-2605-16790 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-16790 |
| SF-2026-ARXIV-2605-16819 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-16819 |
| SF-2026-ARXIV-2605-16826 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-16826 |
| SF-2026-ARXIV-2605-16839 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-16839 |
| SF-2026-ARXIV-2605-16867 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-16867 |
| SF-2026-ARXIV-2605-16928 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-16928 |
| SF-2026-ARXIV-2605-16976 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-16976 |
| SF-2026-ARXIV-2605-16986 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-16986 |
| SF-2026-ARXIV-2605-17003 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17003 |
| SF-2026-ARXIV-2605-17026 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17026 |
| SF-2026-ARXIV-2605-17028 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17028 |
| SF-2026-ARXIV-2605-17034 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17034 |
| SF-2026-ARXIV-2605-17062 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17062 |
| SF-2026-ARXIV-2605-17076 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17076 |
| SF-2026-ARXIV-2605-17106 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17106 |
| SF-2026-ARXIV-2605-17113 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17113 |
| SF-2026-ARXIV-2605-17160 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17160 |
| SF-2026-ARXIV-2605-17164 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17164 |
| SF-2026-ARXIV-2605-17169 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17169 |
| SF-2026-ARXIV-2605-17170 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17170 |
| SF-2026-ARXIV-2605-17172 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17172 |
| SF-2026-ARXIV-2605-17173 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17173 |
| SF-2026-ARXIV-2605-17193 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17193 |
| SF-2026-ARXIV-2605-17222 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17222 |
| SF-2026-ARXIV-2605-17234 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17234 |
| SF-2026-ARXIV-2605-17242 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17242 |
| SF-2026-ARXIV-2605-17246 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17246 |
| SF-2026-ARXIV-2605-17260 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17260 |
| SF-2026-ARXIV-2605-17268 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17268 |
| SF-2026-ARXIV-2605-17273 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17273 |
| SF-2026-ARXIV-2605-17281 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17281 |
| SF-2026-ARXIV-2605-17288 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17288 |
| SF-2026-ARXIV-2605-17289 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17289 |
| SF-2026-ARXIV-2605-17291 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17291 |
| SF-2026-ARXIV-2605-17292 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17292 |
| SF-2026-ARXIV-2605-17301 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17301 |
| SF-2026-ARXIV-2605-17304 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17304 |
| SF-2026-ARXIV-2605-17305 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17305 |
| SF-2026-ARXIV-2605-17320 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17320 |
| SF-2026-ARXIV-2605-17324 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17324 |
| SF-2026-ARXIV-2605-17329 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17329 |
| SF-2026-ARXIV-2605-17348 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17348 |
| SF-2026-ARXIV-2605-17360 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17360 |
| SF-2026-ARXIV-2605-17373 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17373 |
| SF-2026-ARXIV-2605-17380 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17380 |
| SF-2026-ARXIV-2605-17415 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17415 |
| SF-2026-ARXIV-2605-17439 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17439 |
| SF-2026-ARXIV-2605-17453 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17453 |
| SF-2026-ARXIV-2605-17467 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17467 |
| SF-2026-ARXIV-2605-17471 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17471 |
| SF-2026-ARXIV-2605-17480 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17480 |
| SF-2026-ARXIV-2605-17497 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17497 |
| SF-2026-ARXIV-2605-17508 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17508 |
| SF-2026-ARXIV-2605-17522 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17522 |
| SF-2026-ARXIV-2605-17554 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17554 |
| SF-2026-ARXIV-2605-17558 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17558 |
| SF-2026-ARXIV-2605-17570 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17570 |
| SF-2026-ARXIV-2605-17590 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17590 |
| SF-2026-ARXIV-2605-17609 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17609 |
| SF-2026-ARXIV-2605-17610 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17610 |
| SF-2026-ARXIV-2605-17613 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17613 |
| SF-2026-ARXIV-2605-17617 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17617 |
| SF-2026-ARXIV-2605-17625 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17625 |
| SF-2026-ARXIV-2605-17634 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17634 |
| SF-2026-ARXIV-2605-17641 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17641 |
| SF-2026-ARXIV-2605-17659 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17659 |
| SF-2026-ARXIV-2605-17672 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17672 |
| SF-2026-ARXIV-2605-17683 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17683 |
| SF-2026-ARXIV-2605-17707 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17707 |
| SF-2026-ARXIV-2605-17721 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17721 |
| SF-2026-ARXIV-2605-17734 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17734 |
| SF-2026-ARXIV-2605-17757 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17757 |
| SF-2026-ARXIV-2605-17787 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17787 |
| SF-2026-ARXIV-2605-17821 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17821 |
| SF-2026-ARXIV-2605-17830 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17830 |
| SF-2026-ARXIV-2605-17842 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17842 |
| SF-2026-ARXIV-2605-17849 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17849 |
| SF-2026-ARXIV-2605-17862 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17862 |
| SF-2026-ARXIV-2605-17877 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17877 |
| SF-2026-ARXIV-2605-17879 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17879 |
| SF-2026-ARXIV-2605-17889 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17889 |
| SF-2026-ARXIV-2605-17912 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17912 |
| SF-2026-ARXIV-2605-17921 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17921 |
| SF-2026-ARXIV-2605-17923 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17923 |
| SF-2026-ARXIV-2605-17932 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17932 |
| SF-2026-ARXIV-2605-17954 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17954 |
| SF-2026-ARXIV-2605-17986 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17986 |
| SF-2026-ARXIV-2605-17989 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17989 |
| SF-2026-ARXIV-2605-17992 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17992 |
| SF-2026-ARXIV-2605-17998 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-17998 |
| SF-2026-ARXIV-2605-18032 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-18032 |
| SF-2026-ARXIV-2605-18053 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-18053 |
| SF-2026-ARXIV-2605-18067 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-18067 |
| SF-2026-ARXIV-2605-18071 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-18071 |
| SF-2026-ARXIV-2605-18106 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-18106 |
| SF-2026-ARXIV-2605-18165 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-18165 |
| SF-2026-ARXIV-2605-18271 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-18271 |
| SF-2026-ARXIV-2605-18401 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-18401 |
| SF-2026-ARXIV-2605-18414 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-18414 |
| SF-2026-ARXIV-2605-18421 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-18421 |
| SF-2026-ARXIV-2605-18498 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-18498 |
| SF-2026-ARXIV-2605-18565 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-18565 |
| SF-2026-ARXIV-2605-18583 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-18583 |
| SF-2026-ARXIV-2605-18607 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-18607 |
| SF-2026-ARXIV-2605-18652 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-18652 |
| SF-2026-ARXIV-2605-18693 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-18693 |
| SF-2026-ARXIV-2605-18697 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-18697 |
| SF-2026-ARXIV-2605-18703 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-18703 |
| SF-2026-ARXIV-2605-18710 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-18710 |
| SF-2026-ARXIV-2605-18739 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-18739 |
| SF-2026-ARXIV-2605-18750 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-18750 |
| SF-2026-ARXIV-2605.16588 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605.16588 |
| SF-2026-ARXIV-2605.16622 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605.16622 |
| SF-2026-ARXIV-2605.16647 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605.16647 |
| SF-ANNEAL-GOVERNED-SYMBOLIC-PATCHES | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-ANNEAL-GOVERNED-SYMBOLIC-PATCHES |
| SF-ORBISIM-WORLD-MODELS-AS-DIFFERENTIABLE-PHYSICS-ENGINES-FOR-EMBODIED-INTE | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-ORBISIM-WORLD-MODELS-AS-DIFFERENTIABLE-PHYSICS-ENGINES-FOR-EMBODIED-INTE |
| SF-ORTH-DION-ELIMINATING-GEOMETRIC-MISMATCH-IN-DISTRIBUTED-LOW-RANK-SPECTRA | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-ORTH-DION-ELIMINATING-GEOMETRIC-MISMATCH-IN-DISTRIBUTED-LOW-RANK-SPECTRA |
| SF-PROOF-CARRYING-CERTIFICATES-FOR-LLM-PIPELINES-A-TRUST-BOUNDARY-ARCHITECT | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-PROOF-CARRYING-CERTIFICATES-FOR-LLM-PIPELINES-A-TRUST-BOUNDARY-ARCHITECT |
| SF-SELFPLAY-DECISION-CAPACITY-COLLAPSE | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-SELFPLAY-DECISION-CAPACITY-COLLAPSE |

<!-- analysis-decision:SF-2026-ARXIV-2605-16265:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-16265:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-16346:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-16346:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-16360:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-16360:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-16436:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-16436:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-16439:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-16439:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-16508:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-16508:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-16565:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-16565:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-16604:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-16604:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-16616:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-16616:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-16626:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-16626:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-16630:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-16630:end -->

<!-- analysis:DA-20260519-01:start -->
### Deep Analysis — SF-2026-ARXIV-2605-16637

该 family 的 Score V2=9/9；Source Review 已闭合问题、旧路径、机制 owner、evaluation boundary、trade-off 与共存条件。Deep Analysis 只提升叙事优先级，不改变 Evidence Gate。
<!-- analysis:DA-20260519-01:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-16650:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-16650:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-16704:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-16704:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-16712:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-16712:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-16725:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-16725:end -->

<!-- analysis:DA-20260519-02:start -->
### Deep Analysis — SF-2026-ARXIV-2605-16745

该 family 的 Score V2=9/9；Source Review 已闭合问题、旧路径、机制 owner、evaluation boundary、trade-off 与共存条件。Deep Analysis 只提升叙事优先级，不改变 Evidence Gate。
<!-- analysis:DA-20260519-02:end -->

<!-- analysis:DA-20260519-03:start -->
### Deep Analysis — SF-2026-ARXIV-2605-16746

该 family 的 Score V2=9/9；Source Review 已闭合问题、旧路径、机制 owner、evaluation boundary、trade-off 与共存条件。Deep Analysis 只提升叙事优先级，不改变 Evidence Gate。
<!-- analysis:DA-20260519-03:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-16776:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-16776:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-16786:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-16786:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-16787:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-16787:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-16790:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-16790:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-16819:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-16819:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-16826:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-16826:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-16839:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-16839:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-16867:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-16867:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-16928:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-16928:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-16976:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-16976:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-16986:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-16986:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17003:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17003:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17026:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17026:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17028:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17028:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17034:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17034:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17062:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17062:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17076:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17076:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17106:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17106:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17113:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17113:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17160:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17160:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17164:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17164:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17169:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17169:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17170:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17170:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17172:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17172:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17173:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17173:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17193:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17193:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17222:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17222:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17234:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17234:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17242:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17242:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17246:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17246:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17260:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17260:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17268:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17268:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17273:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17273:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17281:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17281:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17288:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17288:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17289:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17289:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17291:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17291:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17292:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17292:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17301:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17301:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17304:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17304:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17305:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17305:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17320:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17320:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17324:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17324:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17329:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17329:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17348:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17348:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17360:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17360:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17373:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17373:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17380:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17380:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17415:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17415:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17439:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17439:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17453:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17453:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17467:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17467:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17471:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17471:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17480:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17480:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17497:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17497:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17508:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17508:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17522:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17522:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17554:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17554:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17558:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17558:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17570:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17570:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17590:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17590:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17609:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17609:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17610:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17610:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17613:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17613:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17617:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17617:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17625:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17625:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17634:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17634:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17641:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17641:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17659:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17659:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17672:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17672:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17683:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17683:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17707:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17707:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17721:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17721:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17734:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17734:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17757:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17757:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17787:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17787:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17821:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17821:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17830:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17830:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17842:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17842:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17849:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17849:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17862:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17862:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17877:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17877:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17879:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17879:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17889:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17889:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17912:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17912:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17921:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17921:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17923:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17923:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17932:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17932:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17954:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17954:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17986:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17986:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17989:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17989:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17992:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17992:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-17998:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17998:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-18032:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-18032:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-18053:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-18053:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-18067:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-18067:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-18071:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-18071:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-18106:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-18106:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-18165:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-18165:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-18271:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-18271:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-18401:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-18401:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-18414:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-18414:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-18421:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-18421:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-18498:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-18498:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-18565:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-18565:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-18583:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-18583:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-18607:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-18607:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-18652:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-18652:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-18693:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-18693:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-18697:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-18697:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-18703:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-18703:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-18710:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-18710:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-18739:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-18739:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-18750:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-18750:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605.16588:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605.16588:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605.16622:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605.16622:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605.16647:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605.16647:end -->

<!-- analysis-decision:SF-ANNEAL-GOVERNED-SYMBOLIC-PATCHES:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-ANNEAL-GOVERNED-SYMBOLIC-PATCHES:end -->

<!-- analysis-decision:SF-ORBISIM-WORLD-MODELS-AS-DIFFERENTIABLE-PHYSICS-ENGINES-FOR-EMBODIED-INTE:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-ORBISIM-WORLD-MODELS-AS-DIFFERENTIABLE-PHYSICS-ENGINES-FOR-EMBODIED-INTE:end -->

<!-- analysis-decision:SF-ORTH-DION-ELIMINATING-GEOMETRIC-MISMATCH-IN-DISTRIBUTED-LOW-RANK-SPECTRA:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-ORTH-DION-ELIMINATING-GEOMETRIC-MISMATCH-IN-DISTRIBUTED-LOW-RANK-SPECTRA:end -->

<!-- analysis-decision:SF-PROOF-CARRYING-CERTIFICATES-FOR-LLM-PIPELINES-A-TRUST-BOUNDARY-ARCHITECT:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-PROOF-CARRYING-CERTIFICATES-FOR-LLM-PIPELINES-A-TRUST-BOUNDARY-ARCHITECT:end -->

<!-- analysis-decision:SF-SELFPLAY-DECISION-CAPACITY-COLLAPSE:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-SELFPLAY-DECISION-CAPACITY-COLLAPSE:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-16265 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L29 (H2: 生命周期威胁) | books/part-06-ai-infrastructure/71-multi-tenant.md#L10 (H2: 本章要回答的问题); books/part-06-ai-infrastructure/73-production-best-practice.md#L10 (H2: 本章要回答的问题) | existing:SF-2026-ARXIV-2605-16265 | delta:SF-2026-ARXIV-2605-16265 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16265 |
| SF-2026-ARXIV-2605-16343 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | books/part-05-inference-system/48-speculative-decoding.md#chapter-48; books/part-05-inference-system/50-vllm.md#chapter-50 | existing:SF-2026-ARXIV-2605-16343 | delta:SF-2026-ARXIV-2605-16343 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16343 |
| SF-2026-ARXIV-2605-16346 | AGENT-MULTI-AGENT | books/part-04-training-system/33-grpo.md#chapter-33 | books/part-04-training-system/32-ppo.md#chapter-32; books/part-04-training-system/34-dpo.md#chapter-34 | existing:SF-2026-ARXIV-2605-16346 | delta:SF-2026-ARXIV-2605-16346 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16346 |
| SF-2026-ARXIV-2605-16354 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-16354 | delta:SF-2026-ARXIV-2605-16354 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16354 |
| SF-2026-ARXIV-2605-16359 | MULTIMODAL-REPRESENTATION | books/part-03-multimodal-world-models/23-multimodal-representation.md#chapter-23 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24 | existing:SF-2026-ARXIV-2605-16359 | delta:SF-2026-ARXIV-2605-16359 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16359 |
| SF-2026-ARXIV-2605-16360 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#chapter-45 | books/part-05-inference-system/44-decode.md#chapter-44; books/part-05-inference-system/46-continuous-batching.md#chapter-46 | existing:SF-2026-ARXIV-2605-16360 | delta:SF-2026-ARXIV-2605-16360 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-16360 |
| SF-2026-ARXIV-2605-16436 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-16436 | delta:SF-2026-ARXIV-2605-16436 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16436 |
| SF-2026-ARXIV-2605-16439 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#chapter-45 | books/part-05-inference-system/44-decode.md#chapter-44; books/part-05-inference-system/46-continuous-batching.md#chapter-46 | existing:SF-2026-ARXIV-2605-16439 | delta:SF-2026-ARXIV-2605-16439 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16439 |
| SF-2026-ARXIV-2605-16508 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83;books/part-07-agent/README.md#knowledge-tree | existing:SF-2026-ARXIV-2605-16508 | delta:SF-2026-ARXIV-2605-16508 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16508 |
| SF-2026-ARXIV-2605-16565 | AGENT-PLANNING | books/part-07-agent/79-planning.md#chapter-79 | books/part-07-agent/78-tool-calling.md#chapter-78;books/part-07-agent/80-reflection.md#chapter-80 | existing:SF-2026-ARXIV-2605-16565 | delta:SF-2026-ARXIV-2605-16565 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16565 |
| SF-2026-ARXIV-2605-16604 | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#chapter-78 | books/part-07-agent/77-memory.md#chapter-77;books/part-07-agent/79-planning.md#chapter-79 | existing:SF-2026-ARXIV-2605-16604 | delta:SF-2026-ARXIV-2605-16604 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16604 |
| SF-2026-ARXIV-2605-16616 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-16616 | delta:SF-2026-ARXIV-2605-16616 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16616 |
| SF-2026-ARXIV-2605-16626 | PLATFORM-MONITORING | books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66;books/part-06-ai-infrastructure/68-logging.md#chapter-68 | existing:SF-2026-ARXIV-2605-16626 | delta:SF-2026-ARXIV-2605-16626 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16626 |
| SF-2026-ARXIV-2605-16630 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-16630 | delta:SF-2026-ARXIV-2605-16630 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16630 |
| SF-2026-ARXIV-2605-16637 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#chapter-56 | books/part-05-inference-system/55-pd-disaggregation.md#chapter-55;books/part-05-inference-system/README.md#knowledge-tree | existing:SF-2026-ARXIV-2605-16637 | delta:SF-2026-ARXIV-2605-16637 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16637 |
| SF-2026-ARXIV-2605-16650 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-16650 | delta:SF-2026-ARXIV-2605-16650 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16650 |
| SF-2026-ARXIV-2605-16704 | TRAIN-DATA | books/part-04-training-system/27-data.md#chapter-27 | books/part-04-training-system/28-pretraining.md#chapter-28 | existing:SF-2026-ARXIV-2605-16704 | delta:SF-2026-ARXIV-2605-16704 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16704 |
| SF-2026-ARXIV-2605-16712 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76;books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-16712 | delta:SF-2026-ARXIV-2605-16712 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-16712 |
| SF-2026-ARXIV-2605-16725 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24;books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | existing:SF-2026-ARXIV-2605-16725 | delta:SF-2026-ARXIV-2605-16725 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16725 |
| SF-2026-ARXIV-2605-16745 | MULTIMODAL-REPRESENTATION | books/part-03-multimodal-world-models/23-multimodal-representation.md#chapter-23 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24 | existing:SF-2026-ARXIV-2605-16745 | delta:SF-2026-ARXIV-2605-16745 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-16745 |
| SF-2026-ARXIV-2605-16746 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76; books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-16746 | delta:SF-2026-ARXIV-2605-16746 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16746 |
| SF-2026-ARXIV-2605-16776 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-16776 | delta:SF-2026-ARXIV-2605-16776 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-16776 |
| SF-2026-ARXIV-2605-16786 | INFER-SPECULATIVE-DECODING | books/part-05-inference-system/48-speculative-decoding.md#chapter-48 | books/part-05-inference-system/47-pagedattention.md#chapter-47; books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | existing:SF-2026-ARXIV-2605-16786 | delta:SF-2026-ARXIV-2605-16786 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-16786 |
| SF-2026-ARXIV-2605-16787 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#chapter-33 | books/part-04-training-system/32-ppo.md#chapter-32; books/part-04-training-system/34-dpo.md#chapter-34 | existing:SF-2026-ARXIV-2605-16787 | delta:SF-2026-ARXIV-2605-16787 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-16787 |
| SF-2026-ARXIV-2605-16790 | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#chapter-78 | books/part-07-agent/77-memory.md#chapter-77; books/part-07-agent/79-planning.md#chapter-79 | existing:SF-2026-ARXIV-2605-16790 | delta:SF-2026-ARXIV-2605-16790 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-16790 |
| SF-2026-ARXIV-2605-16819 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-16819 | delta:SF-2026-ARXIV-2605-16819 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-16819 |
| SF-2026-ARXIV-2605-16826 | TRAIN-PRETRAINING | books/part-04-training-system/28-pretraining.md#chapter-28 | books/part-04-training-system/27-data.md#chapter-27; books/part-04-training-system/29-sft.md#chapter-29 | existing:SF-2026-ARXIV-2605-16826 | delta:SF-2026-ARXIV-2605-16826 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-16826 |
| SF-2026-ARXIV-2605-16839 | INFER-PREFILL | books/part-05-inference-system/43-prefill.md#chapter-43 | books/part-05-inference-system/42-what-happens-during-inference.md#chapter-42; books/part-05-inference-system/44-decode.md#chapter-44 | existing:SF-2026-ARXIV-2605-16839 | delta:SF-2026-ARXIV-2605-16839 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-16839 |
| SF-2026-ARXIV-2605-16867 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#chapter-56 | books/part-05-inference-system/55-pd-disaggregation.md#chapter-55 | existing:SF-2026-ARXIV-2605-16867 | delta:SF-2026-ARXIV-2605-16867 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16867 |
| SF-2026-ARXIV-2605-16928 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#chapter-45 | books/part-05-inference-system/44-decode.md#chapter-44; books/part-05-inference-system/46-continuous-batching.md#chapter-46 | existing:SF-2026-ARXIV-2605-16928 | delta:SF-2026-ARXIV-2605-16928 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-16928 |
| SF-2026-ARXIV-2605-16976 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-16976 | delta:SF-2026-ARXIV-2605-16976 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-16976 |
| SF-2026-ARXIV-2605-16986 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-16986 | delta:SF-2026-ARXIV-2605-16986 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16986 |
| SF-2026-ARXIV-2605-17003 | TRAIN-DATA | books/part-04-training-system/27-data.md#chapter-27 | books/part-04-training-system/28-pretraining.md#chapter-28 | existing:SF-2026-ARXIV-2605-17003 | delta:SF-2026-ARXIV-2605-17003 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-17003 |
| SF-2026-ARXIV-2605-17026 | TRAIN-DATA | books/part-04-training-system/27-data.md#chapter-27 | books/part-04-training-system/28-pretraining.md#chapter-28 | existing:SF-2026-ARXIV-2605-17026 | delta:SF-2026-ARXIV-2605-17026 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-17026 |
| SF-2026-ARXIV-2605-17028 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-17028 | delta:SF-2026-ARXIV-2605-17028 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17028 |
| SF-2026-ARXIV-2605-17034 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-17034 | delta:SF-2026-ARXIV-2605-17034 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17034 |
| SF-2026-ARXIV-2605-17062 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-17062 | delta:SF-2026-ARXIV-2605-17062 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17062 |
| SF-2026-ARXIV-2605-17076 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#chapter-82 | books/part-07-agent/81-workflow.md#chapter-81; books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-17076 | delta:SF-2026-ARXIV-2605-17076 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-17076 |
| SF-2026-ARXIV-2605-17106 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#chapter-56 | books/part-05-inference-system/55-pd-disaggregation.md#chapter-55 | existing:SF-2026-ARXIV-2605-17106 | delta:SF-2026-ARXIV-2605-17106 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-17106 |
| SF-2026-ARXIV-2605-17113 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-17113 | delta:SF-2026-ARXIV-2605-17113 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-17113 |
| SF-2026-ARXIV-2605-17160 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | books/part-05-inference-system/48-speculative-decoding.md#chapter-48; books/part-05-inference-system/50-vllm.md#chapter-50 | existing:SF-2026-ARXIV-2605-17160 | delta:SF-2026-ARXIV-2605-17160 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-17160 |
| SF-2026-ARXIV-2605-17164 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-17164 | delta:SF-2026-ARXIV-2605-17164 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-17164 |
| SF-2026-ARXIV-2605-17169 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-17169 | delta:SF-2026-ARXIV-2605-17169 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17169 |
| SF-2026-ARXIV-2605-17170 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#chapter-45 | books/part-05-inference-system/44-decode.md#chapter-44; books/part-05-inference-system/46-continuous-batching.md#chapter-46 | existing:SF-2026-ARXIV-2605-17170 | delta:SF-2026-ARXIV-2605-17170 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-17170 |
| SF-2026-ARXIV-2605-17172 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-17172 | delta:SF-2026-ARXIV-2605-17172 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17172 |
| SF-2026-ARXIV-2605-17173 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-17173 | delta:SF-2026-ARXIV-2605-17173 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-17173 |
| SF-2026-ARXIV-2605-17193 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#chapter-82 | books/part-07-agent/81-workflow.md#chapter-81; books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-17193 | delta:SF-2026-ARXIV-2605-17193 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17193 |
| SF-2026-ARXIV-2605-17222 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-17222 | delta:SF-2026-ARXIV-2605-17222 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17222 |
| SF-2026-ARXIV-2605-17234 | WORLDVIEW-SCALING-LAW | books/part-01-worldview/07-scaling-law.md#chapter-7 | books/part-01-worldview/06-why-transformer-changed-the-world.md#chapter-6; books/part-01-worldview/08-why-llms-show-intelligence.md#chapter-8 | existing:SF-2026-ARXIV-2605-17234 | delta:SF-2026-ARXIV-2605-17234 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17234 |
| SF-2026-ARXIV-2605-17242 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#chapter-81 | books/part-07-agent/80-reflection.md#chapter-80; books/part-07-agent/82-multi-agent.md#chapter-82 | existing:SF-2026-ARXIV-2605-17242 | delta:SF-2026-ARXIV-2605-17242 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17242 |
| SF-2026-ARXIV-2605-17246 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-17246 | delta:SF-2026-ARXIV-2605-17246 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17246 |
| SF-2026-ARXIV-2605-17260 | MULTIMODAL-REPRESENTATION | books/part-03-multimodal-world-models/23-multimodal-representation.md#chapter-23 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24 | existing:SF-2026-ARXIV-2605-17260 | delta:SF-2026-ARXIV-2605-17260 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17260 |
| SF-2026-ARXIV-2605-17268 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | existing:SF-2026-ARXIV-2605-17268 | delta:SF-2026-ARXIV-2605-17268 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17268 |
| SF-2026-ARXIV-2605-17273 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-17273 | delta:SF-2026-ARXIV-2605-17273 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17273 |
| SF-2026-ARXIV-2605-17281 | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#chapter-78 | books/part-07-agent/77-memory.md#chapter-77; books/part-07-agent/79-planning.md#chapter-79 | existing:SF-2026-ARXIV-2605-17281 | delta:SF-2026-ARXIV-2605-17281 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-17281 |
| SF-2026-ARXIV-2605-17288 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#chapter-56 | books/part-05-inference-system/55-pd-disaggregation.md#chapter-55 | existing:SF-2026-ARXIV-2605-17288 | delta:SF-2026-ARXIV-2605-17288 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17288 |
| SF-2026-ARXIV-2605-17289 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | books/part-05-inference-system/48-speculative-decoding.md#chapter-48; books/part-05-inference-system/50-vllm.md#chapter-50 | existing:SF-2026-ARXIV-2605-17289 | delta:SF-2026-ARXIV-2605-17289 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17289 |
| SF-2026-ARXIV-2605-17291 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#chapter-31 | books/part-04-training-system/30-lora.md#chapter-30; books/part-04-training-system/32-ppo.md#chapter-32 | existing:SF-2026-ARXIV-2605-17291 | delta:SF-2026-ARXIV-2605-17291 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17291 |
| SF-2026-ARXIV-2605-17292 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#chapter-82 | books/part-07-agent/81-workflow.md#chapter-81; books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-17292 | delta:SF-2026-ARXIV-2605-17292 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17292 |
| SF-2026-ARXIV-2605-17301 | AGENT-RAG | books/part-07-agent/76-rag.md#chapter-76 | books/part-07-agent/75-context.md#chapter-75; books/part-07-agent/77-memory.md#chapter-77 | existing:SF-2026-ARXIV-2605-17301 | delta:SF-2026-ARXIV-2605-17301 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17301 |
| SF-2026-ARXIV-2605-17304 | AGENT-CONTEXT | books/part-07-agent/75-context.md#chapter-75 | books/part-07-agent/74-prompt.md#chapter-74; books/part-07-agent/76-rag.md#chapter-76 | existing:SF-2026-ARXIV-2605-17304 | delta:SF-2026-ARXIV-2605-17304 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17304 |
| SF-2026-ARXIV-2605-17305 | AGENT-REFLECTION | books/part-07-agent/80-reflection.md#chapter-80 | books/part-07-agent/79-planning.md#chapter-79; books/part-07-agent/81-workflow.md#chapter-81 | existing:SF-2026-ARXIV-2605-17305 | delta:SF-2026-ARXIV-2605-17305 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17305 |
| SF-2026-ARXIV-2605-17320 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-17320 | delta:SF-2026-ARXIV-2605-17320 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17320 |
| SF-2026-ARXIV-2605-17324 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-17324 | delta:SF-2026-ARXIV-2605-17324 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-17324 |
| SF-2026-ARXIV-2605-17329 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-17329 | delta:SF-2026-ARXIV-2605-17329 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17329 |
| SF-2026-ARXIV-2605-17348 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#chapter-82 | books/part-07-agent/81-workflow.md#chapter-81; books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-17348 | delta:SF-2026-ARXIV-2605-17348 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17348 |
| SF-2026-ARXIV-2605-17360 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-17360 | delta:SF-2026-ARXIV-2605-17360 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-17360 |
| SF-2026-ARXIV-2605-17373 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-17373 | delta:SF-2026-ARXIV-2605-17373 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17373 |
| SF-2026-ARXIV-2605-17380 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-17380 | delta:SF-2026-ARXIV-2605-17380 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-17380 |
| SF-2026-ARXIV-2605-17415 | AGENT-RAG | books/part-07-agent/76-rag.md#chapter-76 | books/part-07-agent/75-context.md#chapter-75; books/part-07-agent/77-memory.md#chapter-77 | existing:SF-2026-ARXIV-2605-17415 | delta:SF-2026-ARXIV-2605-17415 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17415 |
| SF-2026-ARXIV-2605-17439 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-17439 | delta:SF-2026-ARXIV-2605-17439 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17439 |
| SF-2026-ARXIV-2605-17453 | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#chapter-78 | books/part-07-agent/77-memory.md#chapter-77; books/part-07-agent/79-planning.md#chapter-79 | existing:SF-2026-ARXIV-2605-17453 | delta:SF-2026-ARXIV-2605-17453 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17453 |
| SF-2026-ARXIV-2605-17467 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#chapter-82 | books/part-07-agent/81-workflow.md#chapter-81; books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-17467 | delta:SF-2026-ARXIV-2605-17467 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17467 |
| SF-2026-ARXIV-2605-17471 | TRAIN-PRETRAINING | books/part-04-training-system/28-pretraining.md#chapter-28 | books/part-04-training-system/27-data.md#chapter-27; books/part-04-training-system/29-sft.md#chapter-29 | existing:SF-2026-ARXIV-2605-17471 | delta:SF-2026-ARXIV-2605-17471 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17471 |
| SF-2026-ARXIV-2605-17480 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-17480 | delta:SF-2026-ARXIV-2605-17480 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17480 |
| SF-2026-ARXIV-2605-17497 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#chapter-33 | books/part-04-training-system/32-ppo.md#chapter-32; books/part-04-training-system/34-dpo.md#chapter-34 | existing:SF-2026-ARXIV-2605-17497 | delta:SF-2026-ARXIV-2605-17497 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-17497 |
| SF-2026-ARXIV-2605-17508 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#chapter-36 | books/part-04-training-system/35-checkpoint.md#chapter-35; books/part-04-training-system/37-tensor-parallel.md#chapter-37 | existing:SF-2026-ARXIV-2605-17508 | delta:SF-2026-ARXIV-2605-17508 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17508 |
| SF-2026-ARXIV-2605-17522 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24; books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | existing:SF-2026-ARXIV-2605-17522 | delta:SF-2026-ARXIV-2605-17522 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17522 |
| SF-2026-ARXIV-2605-17554 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-17554 | delta:SF-2026-ARXIV-2605-17554 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17554 |
| SF-2026-ARXIV-2605-17558 | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#chapter-78 | books/part-07-agent/77-memory.md#chapter-77; books/part-07-agent/79-planning.md#chapter-79 | existing:SF-2026-ARXIV-2605-17558 | delta:SF-2026-ARXIV-2605-17558 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17558 |
| SF-2026-ARXIV-2605-17570 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#chapter-33 | books/part-04-training-system/32-ppo.md#chapter-32; books/part-04-training-system/34-dpo.md#chapter-34 | existing:SF-2026-ARXIV-2605-17570 | delta:SF-2026-ARXIV-2605-17570 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-17570 |
| SF-2026-ARXIV-2605-17590 | TRAIN-DATA | books/part-04-training-system/27-data.md#chapter-27 | books/part-04-training-system/28-pretraining.md#chapter-28 | existing:SF-2026-ARXIV-2605-17590 | delta:SF-2026-ARXIV-2605-17590 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-17590 |
| SF-2026-ARXIV-2605-17609 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#chapter-56 | books/part-05-inference-system/55-pd-disaggregation.md#chapter-55 | existing:SF-2026-ARXIV-2605-17609 | delta:SF-2026-ARXIV-2605-17609 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17609 |
| SF-2026-ARXIV-2605-17610 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-17610 | delta:SF-2026-ARXIV-2605-17610 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17610 |
| SF-2026-ARXIV-2605-17613 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#chapter-45 | books/part-05-inference-system/44-decode.md#chapter-44; books/part-05-inference-system/46-continuous-batching.md#chapter-46 | existing:SF-2026-ARXIV-2605-17613 | delta:SF-2026-ARXIV-2605-17613 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-17613 |
| SF-2026-ARXIV-2605-17617 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#chapter-81 | books/part-07-agent/80-reflection.md#chapter-80; books/part-07-agent/82-multi-agent.md#chapter-82 | existing:SF-2026-ARXIV-2605-17617 | delta:SF-2026-ARXIV-2605-17617 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17617 |
| SF-2026-ARXIV-2605-17625 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76; books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-17625 | delta:SF-2026-ARXIV-2605-17625 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17625 |
| SF-2026-ARXIV-2605-17634 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-17634 | delta:SF-2026-ARXIV-2605-17634 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17634 |
| SF-2026-ARXIV-2605-17641 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76; books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-17641 | delta:SF-2026-ARXIV-2605-17641 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17641 |
| SF-2026-ARXIV-2605-17659 | TRAIN-PRETRAINING | books/part-04-training-system/28-pretraining.md#chapter-28 | books/part-04-training-system/27-data.md#chapter-27; books/part-04-training-system/29-sft.md#chapter-29 | existing:SF-2026-ARXIV-2605-17659 | delta:SF-2026-ARXIV-2605-17659 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-17659 |
| SF-2026-ARXIV-2605-17672 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#chapter-56 | books/part-05-inference-system/55-pd-disaggregation.md#chapter-55 | existing:SF-2026-ARXIV-2605-17672 | delta:SF-2026-ARXIV-2605-17672 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17672 |
| SF-2026-ARXIV-2605-17683 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | books/part-05-inference-system/48-speculative-decoding.md#chapter-48; books/part-05-inference-system/50-vllm.md#chapter-50 | existing:SF-2026-ARXIV-2605-17683 | delta:SF-2026-ARXIV-2605-17683 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-17683 |
| SF-2026-ARXIV-2605-17707 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-17707 | delta:SF-2026-ARXIV-2605-17707 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-17707 |
| SF-2026-ARXIV-2605-17721 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76; books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-17721 | delta:SF-2026-ARXIV-2605-17721 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17721 |
| SF-2026-ARXIV-2605-17734 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-17734 | delta:SF-2026-ARXIV-2605-17734 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17734 |
| SF-2026-ARXIV-2605-17757 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#chapter-45 | books/part-05-inference-system/44-decode.md#chapter-44;books/part-05-inference-system/46-continuous-batching.md#chapter-46 | existing:SF-2026-ARXIV-2605-17757 | delta:SF-2026-ARXIV-2605-17757 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17757 |
| SF-2026-ARXIV-2605-17787 | TRAIN-PRETRAINING | books/part-04-training-system/28-pretraining.md#chapter-28 | books/part-04-training-system/27-data.md#chapter-27;books/part-04-training-system/29-sft.md#chapter-29 | existing:SF-2026-ARXIV-2605-17787 | delta:SF-2026-ARXIV-2605-17787 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17787 |
| SF-2026-ARXIV-2605-17821 | TRAIN-CHECKPOINT | books/part-04-training-system/35-checkpoint.md#chapter-35 | books/part-04-training-system/34-dpo.md#chapter-34;books/part-04-training-system/36-distributed-training.md#chapter-36 | existing:SF-2026-ARXIV-2605-17821 | delta:SF-2026-ARXIV-2605-17821 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-17821 |
| SF-2026-ARXIV-2605-17830 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76;books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-17830 | delta:SF-2026-ARXIV-2605-17830 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17830 |
| SF-2026-ARXIV-2605-17842 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | books/part-05-inference-system/48-speculative-decoding.md#chapter-48;books/part-05-inference-system/50-vllm.md#chapter-50 | existing:SF-2026-ARXIV-2605-17842 | delta:SF-2026-ARXIV-2605-17842 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-17842 |
| SF-2026-ARXIV-2605-17849 | TRAIN-DATA | books/part-04-training-system/27-data.md#chapter-27 | books/part-04-training-system/28-pretraining.md#chapter-28 | existing:SF-2026-ARXIV-2605-17849 | delta:SF-2026-ARXIV-2605-17849 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17849 |
| SF-2026-ARXIV-2605-17862 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#chapter-31 | books/part-04-training-system/30-lora.md#chapter-30;books/part-04-training-system/32-ppo.md#chapter-32 | existing:SF-2026-ARXIV-2605-17862 | delta:SF-2026-ARXIV-2605-17862 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-17862 |
| SF-2026-ARXIV-2605-17877 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#chapter-31 | books/part-04-training-system/30-lora.md#chapter-30;books/part-04-training-system/32-ppo.md#chapter-32 | existing:SF-2026-ARXIV-2605-17877 | delta:SF-2026-ARXIV-2605-17877 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-17877 |
| SF-2026-ARXIV-2605-17879 | PLATFORM-MONITORING | books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66;books/part-06-ai-infrastructure/68-logging.md#chapter-68 | existing:SF-2026-ARXIV-2605-17879 | delta:SF-2026-ARXIV-2605-17879 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-17879 |
| SF-2026-ARXIV-2605-17889 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | books/part-05-inference-system/48-speculative-decoding.md#chapter-48;books/part-05-inference-system/50-vllm.md#chapter-50 | existing:SF-2026-ARXIV-2605-17889 | delta:SF-2026-ARXIV-2605-17889 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-17889 |
| SF-2026-ARXIV-2605-17912 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-17912 | delta:SF-2026-ARXIV-2605-17912 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17912 |
| SF-2026-ARXIV-2605-17921 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#chapter-56 | books/part-05-inference-system/55-pd-disaggregation.md#chapter-55 | existing:SF-2026-ARXIV-2605-17921 | delta:SF-2026-ARXIV-2605-17921 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17921 |
| SF-2026-ARXIV-2605-17923 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#chapter-36 | books/part-04-training-system/35-checkpoint.md#chapter-35;books/part-04-training-system/37-tensor-parallel.md#chapter-37 | existing:SF-2026-ARXIV-2605-17923 | delta:SF-2026-ARXIV-2605-17923 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-17923 |
| SF-2026-ARXIV-2605-17932 | MULTIMODAL-GENERATIVE-PARADIGMS | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24 | books/part-03-multimodal-world-models/23-multimodal-representation.md#chapter-23;books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | existing:SF-2026-ARXIV-2605-17932 | delta:SF-2026-ARXIV-2605-17932 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17932 |
| SF-2026-ARXIV-2605-17954 | MULTIMODAL-REPRESENTATION | books/part-03-multimodal-world-models/23-multimodal-representation.md#chapter-23 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24 | existing:SF-2026-ARXIV-2605-17954 | delta:SF-2026-ARXIV-2605-17954 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17954 |
| SF-2026-ARXIV-2605-17986 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-17986 | delta:SF-2026-ARXIV-2605-17986 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17986 |
| SF-2026-ARXIV-2605-17989 | AGENT-RAG | books/part-07-agent/76-rag.md#chapter-76 | books/part-07-agent/75-context.md#chapter-75;books/part-07-agent/77-memory.md#chapter-77 | existing:SF-2026-ARXIV-2605-17989 | delta:SF-2026-ARXIV-2605-17989 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-17989 |
| SF-2026-ARXIV-2605-17992 | AGENT-RAG | books/part-07-agent/76-rag.md#chapter-76 | books/part-07-agent/75-context.md#chapter-75;books/part-07-agent/77-memory.md#chapter-77 | existing:SF-2026-ARXIV-2605-17992 | delta:SF-2026-ARXIV-2605-17992 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-17992 |
| SF-2026-ARXIV-2605-17998 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#chapter-81 | books/part-07-agent/80-reflection.md#chapter-80;books/part-07-agent/82-multi-agent.md#chapter-82 | existing:SF-2026-ARXIV-2605-17998 | delta:SF-2026-ARXIV-2605-17998 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-17998 |
| SF-2026-ARXIV-2605-18032 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#chapter-81 | books/part-07-agent/80-reflection.md#chapter-80;books/part-07-agent/82-multi-agent.md#chapter-82 | existing:SF-2026-ARXIV-2605-18032 | delta:SF-2026-ARXIV-2605-18032 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18032 |
| SF-2026-ARXIV-2605-18041 | MULTIMODAL-REPRESENTATION | books/part-03-multimodal-world-models/23-multimodal-representation.md#chapter-23 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24 | existing:SF-2026-ARXIV-2605-18041 | delta:SF-2026-ARXIV-2605-18041 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18041 |
| SF-2026-ARXIV-2605-18053 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#chapter-45 | books/part-05-inference-system/44-decode.md#chapter-44;books/part-05-inference-system/46-continuous-batching.md#chapter-46 | existing:SF-2026-ARXIV-2605-18053 | delta:SF-2026-ARXIV-2605-18053 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-18053 |
| SF-2026-ARXIV-2605-18067 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#chapter-82 | books/part-07-agent/81-workflow.md#chapter-81;books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-18067 | delta:SF-2026-ARXIV-2605-18067 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18067 |
| SF-2026-ARXIV-2605-18071 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#chapter-45 | books/part-05-inference-system/44-decode.md#chapter-44;books/part-05-inference-system/46-continuous-batching.md#chapter-46 | existing:SF-2026-ARXIV-2605-18071 | delta:SF-2026-ARXIV-2605-18071 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18071 |
| SF-2026-ARXIV-2605-18106 | TRAIN-PRETRAINING | books/part-04-training-system/28-pretraining.md#chapter-28 | books/part-04-training-system/27-data.md#chapter-27;books/part-04-training-system/29-sft.md#chapter-29 | existing:SF-2026-ARXIV-2605-18106 | delta:SF-2026-ARXIV-2605-18106 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-18106 |
| SF-2026-ARXIV-2605-18165 | MULTIMODAL-GENERATIVE-PARADIGMS | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24 | books/part-03-multimodal-world-models/23-multimodal-representation.md#chapter-23;books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | existing:SF-2026-ARXIV-2605-18165 | delta:SF-2026-ARXIV-2605-18165 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18165 |
| SF-2026-ARXIV-2605-18271 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76;books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-18271 | delta:SF-2026-ARXIV-2605-18271 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18271 |
| SF-2026-ARXIV-2605-18401 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-18401 | delta:SF-2026-ARXIV-2605-18401 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18401 |
| SF-2026-ARXIV-2605-18414 | AGENT-MCP | books/part-07-agent/83-mcp.md#chapter-83 | books/part-07-agent/82-multi-agent.md#chapter-82;books/part-07-agent/84-agent-platform.md#chapter-84 | existing:SF-2026-ARXIV-2605-18414 | delta:SF-2026-ARXIV-2605-18414 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18414 |
| SF-2026-ARXIV-2605-18421 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76;books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-18421 | delta:SF-2026-ARXIV-2605-18421 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18421 |
| SF-2026-ARXIV-2605-18498 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-18498 | delta:SF-2026-ARXIV-2605-18498 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-18498 |
| SF-2026-ARXIV-2605-18565 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76;books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-18565 | delta:SF-2026-ARXIV-2605-18565 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-18565 |
| SF-2026-ARXIV-2605-18583 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-18583 | delta:SF-2026-ARXIV-2605-18583 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18583 |
| SF-2026-ARXIV-2605-18607 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-18607 | delta:SF-2026-ARXIV-2605-18607 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18607 |
| SF-2026-ARXIV-2605-18652 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76;books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-18652 | delta:SF-2026-ARXIV-2605-18652 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18652 |
| SF-2026-ARXIV-2605-18693 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-18693 | delta:SF-2026-ARXIV-2605-18693 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18693 |
| SF-2026-ARXIV-2605-18697 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#chapter-81 | books/part-07-agent/80-reflection.md#chapter-80;books/part-07-agent/82-multi-agent.md#chapter-82 | existing:SF-2026-ARXIV-2605-18697 | delta:SF-2026-ARXIV-2605-18697 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18697 |
| SF-2026-ARXIV-2605-18703 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#chapter-81 | books/part-07-agent/80-reflection.md#chapter-80;books/part-07-agent/82-multi-agent.md#chapter-82 | existing:SF-2026-ARXIV-2605-18703 | delta:SF-2026-ARXIV-2605-18703 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18703 |
| SF-2026-ARXIV-2605-18710 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#chapter-36 | books/part-04-training-system/35-checkpoint.md#chapter-35;books/part-04-training-system/37-tensor-parallel.md#chapter-37 | existing:SF-2026-ARXIV-2605-18710 | delta:SF-2026-ARXIV-2605-18710 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-18710 |
| SF-2026-ARXIV-2605-18739 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#chapter-36 | books/part-04-training-system/35-checkpoint.md#chapter-35;books/part-04-training-system/37-tensor-parallel.md#chapter-37 | existing:SF-2026-ARXIV-2605-18739 | delta:SF-2026-ARXIV-2605-18739 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18739 |
| SF-2026-ARXIV-2605-18750 | TRAIN-PIPELINE-PARALLEL | books/part-04-training-system/38-pipeline-parallel.md#chapter-38 | books/part-04-training-system/37-tensor-parallel.md#chapter-37;books/part-04-training-system/39-zero.md#chapter-39 | existing:SF-2026-ARXIV-2605-18750 | delta:SF-2026-ARXIV-2605-18750 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-18750 |
| SF-2026-ARXIV-2605.16588 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25;books/part-03-multimodal-world-models/README.md#knowledge-tree | existing:SF-2026-ARXIV-2605.16588 | delta:SF-2026-ARXIV-2605.16588 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605.16588 |
| SF-2026-ARXIV-2605.16622 | TRAIN-PRETRAINING | books/part-04-training-system/28-pretraining.md#chapter-28 | books/part-04-training-system/27-data.md#chapter-27;books/part-04-training-system/29-sft.md#chapter-29 | existing:SF-2026-ARXIV-2605.16622 | delta:SF-2026-ARXIV-2605.16622 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605.16622 |
| SF-2026-ARXIV-2605.16647 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605.16647 | delta:SF-2026-ARXIV-2605.16647 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605.16647 |
| SF-ANNEAL-GOVERNED-SYMBOLIC-PATCHES | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76; books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-ANNEAL-GOVERNED-SYMBOLIC-PATCHES | delta:SF-ANNEAL-GOVERNED-SYMBOLIC-PATCHES | Layering / Dependency | No Change — Existing Coverage | books-review:SF-ANNEAL-GOVERNED-SYMBOLIC-PATCHES |
| SF-FRE-RES-FREQUENCY-RESIDUAL-VIDEO-TOKEN-COMPRESSION-FOR-EFFICIENT-VIDEO-M | MULTIMODAL-REPRESENTATION | books/part-03-multimodal-world-models/23-multimodal-representation.md#chapter-23 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24 | existing:SF-FRE-RES-FREQUENCY-RESIDUAL-VIDEO-TOKEN-COMPRESSION-FOR-EFFICIENT-VIDEO-M | delta:SF-FRE-RES-FREQUENCY-RESIDUAL-VIDEO-TOKEN-COMPRESSION-FOR-EFFICIENT-VIDEO-M | Direct Evolution | No Change — Existing Coverage | books-review:SF-FRE-RES-FREQUENCY-RESIDUAL-VIDEO-TOKEN-COMPRESSION-FOR-EFFICIENT-VIDEO-M |
| SF-MIXING-TIMES-OF-GLAUBER-DYNAMICS-ON-MASKED-LANGUAGE-MODELS | MULTIMODAL-GENERATIVE-PARADIGMS | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24 | books/part-03-multimodal-world-models/23-multimodal-representation.md#chapter-23; books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | existing:SF-MIXING-TIMES-OF-GLAUBER-DYNAMICS-ON-MASKED-LANGUAGE-MODELS | delta:SF-MIXING-TIMES-OF-GLAUBER-DYNAMICS-ON-MASKED-LANGUAGE-MODELS | Direct Evolution | No Change — Existing Coverage | books-review:SF-MIXING-TIMES-OF-GLAUBER-DYNAMICS-ON-MASKED-LANGUAGE-MODELS |
| SF-ORBISIM-WORLD-MODELS-AS-DIFFERENTIABLE-PHYSICS-ENGINES-FOR-EMBODIED-INTE | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24; books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | existing:SF-ORBISIM-WORLD-MODELS-AS-DIFFERENTIABLE-PHYSICS-ENGINES-FOR-EMBODIED-INTE | delta:SF-ORBISIM-WORLD-MODELS-AS-DIFFERENTIABLE-PHYSICS-ENGINES-FOR-EMBODIED-INTE | Direct Evolution | No Change — Existing Coverage | books-review:SF-ORBISIM-WORLD-MODELS-AS-DIFFERENTIABLE-PHYSICS-ENGINES-FOR-EMBODIED-INTE |
| SF-ORTH-DION-ELIMINATING-GEOMETRIC-MISMATCH-IN-DISTRIBUTED-LOW-RANK-SPECTRA | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#chapter-36 | books/part-04-training-system/35-checkpoint.md#chapter-35; books/part-04-training-system/37-tensor-parallel.md#chapter-37 | existing:SF-ORTH-DION-ELIMINATING-GEOMETRIC-MISMATCH-IN-DISTRIBUTED-LOW-RANK-SPECTRA | delta:SF-ORTH-DION-ELIMINATING-GEOMETRIC-MISMATCH-IN-DISTRIBUTED-LOW-RANK-SPECTRA | Direct Evolution | No Change — Existing Coverage | books-review:SF-ORTH-DION-ELIMINATING-GEOMETRIC-MISMATCH-IN-DISTRIBUTED-LOW-RANK-SPECTRA |
| SF-PROOF-CARRYING-CERTIFICATES-FOR-LLM-PIPELINES-A-TRUST-BOUNDARY-ARCHITECT | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-PROOF-CARRYING-CERTIFICATES-FOR-LLM-PIPELINES-A-TRUST-BOUNDARY-ARCHITECT | delta:SF-PROOF-CARRYING-CERTIFICATES-FOR-LLM-PIPELINES-A-TRUST-BOUNDARY-ARCHITECT | Direct Evolution | No Change — Existing Coverage | books-review:SF-PROOF-CARRYING-CERTIFICATES-FOR-LLM-PIPELINES-A-TRUST-BOUNDARY-ARCHITECT |
| SF-SELFPLAY-DECISION-CAPACITY-COLLAPSE | TRAIN-PPO | books/part-04-training-system/32-ppo.md#chapter-32 | books/part-04-training-system/31-rlhf.md#chapter-31; books/part-04-training-system/33-grpo.md#chapter-33 | existing:SF-SELFPLAY-DECISION-CAPACITY-COLLAPSE | delta:SF-SELFPLAY-DECISION-CAPACITY-COLLAPSE | Layering / Dependency | No Change — Existing Coverage | books-review:SF-SELFPLAY-DECISION-CAPACITY-COLLAPSE |
| SF-SIGNMUON-SIGN-ORTHOGONALIZED-OPTIMIZER | TRAIN-PRETRAINING | books/part-04-training-system/28-pretraining.md#chapter-28 | books/part-04-training-system/27-data.md#chapter-27; books/part-04-training-system/29-sft.md#chapter-29 | existing:SF-SIGNMUON-SIGN-ORTHOGONALIZED-OPTIMIZER | delta:SF-SIGNMUON-SIGN-ORTHOGONALIZED-OPTIMIZER | Layering / Dependency | No Change — Existing Coverage | books-review:SF-SIGNMUON-SIGN-ORTHOGONALIZED-OPTIMIZER |

<!-- books-review:SF-2026-ARXIV-2605-16265:start -->
<!-- existing:SF-2026-ARXIV-2605-16265:start -->对读 `books/part-06-ai-infrastructure/72-security.md#L29 (H2: 生命周期威胁)` 及相邻章节后，现有命题为：本章的核心判断是：**AI security 是贯穿 capability production、delivery 与 action 的风险管理。平台必须识别资产、主体、数据流和信任转换，并用 provenance、least privilege、isolation、validation 与 audit 建立纵深防御。** 目标小节已经拥有该 family 所需的长期 owner 与旧路径/约束边界。<!-- existing:SF-2026-ARXIV-2605-16265:end -->
<!-- delta:SF-2026-ARXIV-2605-16265:start -->Exact-v1 的 source-specific delta 是：We present the design, architecture, threat model, and policy model of AgentWall, and demonstrate 92.9% policy enforcement accuracy with sub-millisecond overhead across 14 benchmark tests. 其证据边界为：Evidence is author-reported exact-v1 mechanism/evaluation evidence. It does not establish cross-model, cross-hardware, cross-workload or production generality unless those conditions are explicitly named above. 该实现或实验没有改变当前章节已经成立的长期机制，不把作者 benchmark 外推为通用结论。<!-- delta:SF-2026-ARXIV-2605-16265:end -->
Decision: `No Change — Existing Coverage`; reviewer=fresh-context:apr-may-books-20260903。
<!-- books-review:SF-2026-ARXIV-2605-16265:end -->

<!-- books-review:SF-2026-ARXIV-2605-16343:start -->
<!-- existing:SF-2026-ARXIV-2605-16343:start -->已读取 `books/part-05-inference-system/49-tensorrt-llm.md` 及同 Part 前后相邻章节；当前主线已覆盖execution plan、kernel/quantization contract、精度边界与 fallback。本 family 的 exact-v1 增量为“`LoopQ: Quantization for Recursive Transformers` 通过“We present the first systematic study of quantization in LoopLMs and identify three challenges: distribution shift across roles, state reuse across loop transitions, and recursive error accumulation.”改变 infer tensorrt llm 的可观察机制或决策边界；exact-v1 的证明范围限于“Experiments across seven benchmarks show that, under W4A4 quantization, LoopQ improves average downstream accuracy by 68.8% and reduces average perplexity by 87.7% compared with the strongest static PTQ baseline.”，不能外推到未披露 workload、model、hardware、precision、evaluator 或 SLO”，它没有改变现有 owner、控制权或共存边界，因此作为受限案例留在 Daily。<!-- existing:SF-2026-ARXIV-2605-16343:end -->
<!-- delta:SF-2026-ARXIV-2605-16343:start -->`LoopQ: Quantization for Recursive Transformers` 通过“We present the first systematic study of quantization in LoopLMs and identify three challenges: distribution shift across roles, state reuse across loop transitions, and recursive error accumulation.”改变 infer tensorrt llm 的可观察机制或决策边界；exact-v1 的证明范围限于“Experiments across seven benchmarks show that, under W4A4 quantization, LoopQ improves average downstream accuracy by 68.8% and reduces average perplexity by 87.7% compared with the strongest static PTQ baseline.”，不能外推到未披露 workload、model、hardware、precision、evaluator 或 SLO<!-- delta:SF-2026-ARXIV-2605-16343:end --> Decision: `No Change — Existing Coverage`。author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-16343:end -->

<!-- books-review:SF-2026-ARXIV-2605-16346:start -->
<!-- existing:SF-2026-ARXIV-2605-16346:start -->已读取 `books/part-04-training-system/33-grpo.md` 及同 Part 前后相邻章节；当前主线已覆盖sequence reward、token credit、group/batch composition 与 verifier 约束。本 family 的 exact-v1 增量为“`PropGuard: Safeguarding LLM-MAS via Propagation-Aware Exploration and Remediation` 通过“We propose PropGuard, a propagation-aware framework for safeguarding LLM-MAS.”改变 train grpo 的可观察机制或决策边界；exact-v1 的证明范围限于“Experiments across four communication architectures and five attack settings demonstrate that PropGuard consistently lowers attack success while maintaining high task-level defense success, achieving a favorable effectiveness--efficiency trade-off.”，不能外推到未披露 workload、model、hardware、precision、evaluator 或 SLO”，它没有改变现有 owner、控制权或共存边界，因此作为受限案例留在 Daily。<!-- existing:SF-2026-ARXIV-2605-16346:end -->
<!-- delta:SF-2026-ARXIV-2605-16346:start -->`PropGuard: Safeguarding LLM-MAS via Propagation-Aware Exploration and Remediation` 通过“We propose PropGuard, a propagation-aware framework for safeguarding LLM-MAS.”改变 train grpo 的可观察机制或决策边界；exact-v1 的证明范围限于“Experiments across four communication architectures and five attack settings demonstrate that PropGuard consistently lowers attack success while maintaining high task-level defense success, achieving a favorable effectiveness--efficiency trade-off.”，不能外推到未披露 workload、model、hardware、precision、evaluator 或 SLO<!-- delta:SF-2026-ARXIV-2605-16346:end --> Decision: `No Change — Existing Coverage`。author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-16346:end -->

<!-- books-review:SF-2026-ARXIV-2605-16354:start -->
<!-- existing:SF-2026-ARXIV-2605-16354:start -->已读取 `books/part-06-ai-infrastructure/72-security.md` 及同 Part 前后相邻章节；当前主线已覆盖typed capability、trust boundary、policy enforcement 与 least-privilege action commit。但正文尚未明确承载本 family 的增量边界：`Augmenting Human Evaluation with LLM Judges: How Many Human Reviews Do You Need?` 通过“We propose to use a doubly robust estimator from the missing data literature, which takes advantage of the robustness property against the prediction model, since the missingness model is known by design.”改变 platform security 的可观察机制或决策边界；exact-v1 的证明范围限于“This paper (1) shifts the role of the LLM judge from substitutive to auxiliary, and (2) formulates the LLM-as-a-judge paradigm as one of augmenting human evaluation through a two-stage sampling design, where LLM evaluations…”，不能外推到未披露 workload、model、hardware、precision、evaluator 或 SLO。<!-- existing:SF-2026-ARXIV-2605-16354:end -->
<!-- delta:SF-2026-ARXIV-2605-16354:start -->`Augmenting Human Evaluation with LLM Judges: How Many Human Reviews Do You Need?` 通过“We propose to use a doubly robust estimator from the missing data literature, which takes advantage of the robustness property against the prediction model, since the missingness model is known by design.”改变 platform security 的可观察机制或决策边界；exact-v1 的证明范围限于“This paper (1) shifts the role of the LLM judge from substitutive to auxiliary, and (2) formulates the LLM-as-a-judge paradigm as one of augmenting human evaluation through a two-stage sampling design, where LLM evaluations…”，不能外推到未披露 workload、model、hardware、precision、evaluator 或 SLO<!-- delta:SF-2026-ARXIV-2605-16354:end --> Decision: `No Change — Existing Coverage`。author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-16354:end -->

<!-- books-review:SF-2026-ARXIV-2605-16359:start -->
<!-- existing:SF-2026-ARXIV-2605-16359:start -->已读取 `books/part-03-multimodal-world-models/23-multimodal-representation.md` 及同 Part 前后相邻章节；当前主线已覆盖modality token identity、fusion、coverage 与 provenance。本 family 的 exact-v1 增量为“视觉 token pruning 应作为 task-conditioned evidence search，预算分配需同时保留局部相关性与 coverage recovery”，它没有改变现有 owner、控制权或共存边界，因此作为受限案例留在 Daily。<!-- existing:SF-2026-ARXIV-2605-16359:end -->
<!-- delta:SF-2026-ARXIV-2605-16359:start -->视觉 token pruning 应作为 task-conditioned evidence search，预算分配需同时保留局部相关性与 coverage recovery<!-- delta:SF-2026-ARXIV-2605-16359:end --> Decision: `No Change — Existing Coverage`。author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-16359:end -->

<!-- books-review:SF-2026-ARXIV-2605-16360:start -->
<!-- existing:SF-2026-ARXIV-2605-16360:start -->已读取 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 及同 Part 前后相邻章节；当前主线已覆盖KV identity、生命周期、容量、eviction quality 与 correctness fallback。但正文尚未明确承载本 family 的增量边界：高精度 KV importance scoring 可异步交给同 family 小模型 proxy，但会增加 prefill 峰值显存并受 intra-family transfer 约束。<!-- existing:SF-2026-ARXIV-2605-16360:end -->
<!-- delta:SF-2026-ARXIV-2605-16360:start -->高精度 KV importance scoring 可异步交给同 family 小模型 proxy，但会增加 prefill 峰值显存并受 intra-family transfer 约束<!-- delta:SF-2026-ARXIV-2605-16360:end --> Decision: `Integrate`。author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-16360:end -->

<!-- books-review:SF-2026-ARXIV-2605-16436:start -->
<!-- existing:SF-2026-ARXIV-2605-16436:start -->已读取 `books/part-06-ai-infrastructure/72-security.md` 及相邻章节；当前主线已覆盖identity、typed capability、least privilege、policy mediation、effect boundary 与 audit。本 family 的增量“Agentic AI 降低高拟真攻击的边际成本，使 rate limit、identity proof 与 human vigilance 的旧经济假设失效；position analysis 不证明具体控制已有效”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`45cdedd789e1517c5cd110897cbfaf39b57453fe2bc94b9bc64d72ffa4612bb3`；相邻章节=`books/part-06-ai-infrastructure/71-multi-tenant.md, books/part-06-ai-infrastructure/73-production-best-practice.md`。<!-- existing:SF-2026-ARXIV-2605-16436:end -->
<!-- delta:SF-2026-ARXIV-2605-16436:start -->Agentic AI 降低高拟真攻击的边际成本，使 rate limit、identity proof 与 human vigilance 的旧经济假设失效；position analysis 不证明具体控制已有效<!-- delta:SF-2026-ARXIV-2605-16436:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-16436:end -->

<!-- books-review:SF-2026-ARXIV-2605-16439:start -->
<!-- existing:SF-2026-ARXIV-2605-16439:start -->已读取 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 及相邻章节；当前主线已覆盖KV identity、residency、compression/eviction quality、rollback 与 workload-bound correctness。本 family 的增量“VLM KV compression 应利用视觉与文本 token 的非对称冗余并按序列阶段保留信息；局部压缩收益不能外推到任意模态、长度或 backend”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`eb1d588cb78640e5a75ba6759724e661d8aae6d976d9bebe394627c4148707db`；相邻章节=`books/part-05-inference-system/44-decode.md, books/part-05-inference-system/46-continuous-batching.md`。<!-- existing:SF-2026-ARXIV-2605-16439:end -->
<!-- delta:SF-2026-ARXIV-2605-16439:start -->VLM KV compression 应利用视觉与文本 token 的非对称冗余并按序列阶段保留信息；局部压缩收益不能外推到任意模态、长度或 backend<!-- delta:SF-2026-ARXIV-2605-16439:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-16439:end -->

<!-- books-review:SF-2026-ARXIV-2605-16508:start -->
<!-- existing:SF-2026-ARXIV-2605-16508:start -->Ch84 already models skill-library competence, selection, transfer, interference and lifecycle; the scaling law is supporting evidence, not a new contract.<!-- existing:SF-2026-ARXIV-2605-16508:end -->
<!-- delta:SF-2026-ARXIV-2605-16508:start -->Ch84 already models skill-library competence, selection, transfer, interference and lifecycle; the scaling law is supporting evidence, not a new contract.<!-- delta:SF-2026-ARXIV-2605-16508:end --> Final decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-16508:end -->

<!-- books-review:SF-2026-ARXIV-2605-16565:start -->
<!-- existing:SF-2026-ARXIV-2605-16565:start -->Ch79 and Ch56 already own speculative action planning, validation, commit and rollback under latency/cost budgets.<!-- existing:SF-2026-ARXIV-2605-16565:end -->
<!-- delta:SF-2026-ARXIV-2605-16565:start -->Ch79 and Ch56 already own speculative action planning, validation, commit and rollback under latency/cost budgets.<!-- delta:SF-2026-ARXIV-2605-16565:end --> Final decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-16565:end -->

<!-- books-review:SF-2026-ARXIV-2605-16604:start -->
<!-- existing:SF-2026-ARXIV-2605-16604:start -->Ch56 already admits/escalates work by uncertainty, evidence value, cost and SLO, with a bounded fallback to stronger execution.<!-- existing:SF-2026-ARXIV-2605-16604:end -->
<!-- delta:SF-2026-ARXIV-2605-16604:start -->Ch56 already admits/escalates work by uncertainty, evidence value, cost and SLO, with a bounded fallback to stronger execution.<!-- delta:SF-2026-ARXIV-2605-16604:end --> Final decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-16604:end -->

<!-- books-review:SF-2026-ARXIV-2605-16616:start -->
<!-- existing:SF-2026-ARXIV-2605-16616:start -->Ch66 already requires immutable task, environment, code, artifact and evaluator identity for reproducible autonomous-research evidence.<!-- existing:SF-2026-ARXIV-2605-16616:end -->
<!-- delta:SF-2026-ARXIV-2605-16616:start -->Ch66 already requires immutable task, environment, code, artifact and evaluator identity for reproducible autonomous-research evidence.<!-- delta:SF-2026-ARXIV-2605-16616:end --> Final decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-16616:end -->

<!-- books-review:SF-2026-ARXIV-2605-16626:start -->
<!-- existing:SF-2026-ARXIV-2605-16626:start -->Ch67 and Ch72 already treat adaptive monitor evasion, blind spots and false-negative measurement as part of the security evidence contract.<!-- existing:SF-2026-ARXIV-2605-16626:end -->
<!-- delta:SF-2026-ARXIV-2605-16626:start -->Ch67 and Ch72 already treat adaptive monitor evasion, blind spots and false-negative measurement as part of the security evidence contract.<!-- delta:SF-2026-ARXIV-2605-16626:end --> Final decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-16626:end -->

<!-- books-review:SF-2026-ARXIV-2605-16630:start -->
<!-- existing:SF-2026-ARXIV-2605-16630:start -->Ch72 already binds disclosure to task intent, data flow, access scope, local/cloud trust boundary and least-privilege release.<!-- existing:SF-2026-ARXIV-2605-16630:end -->
<!-- delta:SF-2026-ARXIV-2605-16630:start -->Ch72 already binds disclosure to task intent, data flow, access scope, local/cloud trust boundary and least-privilege release.<!-- delta:SF-2026-ARXIV-2605-16630:end --> Final decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-16630:end -->

<!-- books-review:SF-2026-ARXIV-2605-16637:start -->
<!-- existing:SF-2026-ARXIV-2605-16637:start -->Ch56 already owns online workflow DAGs, heterogeneous placement, critical-path scheduling, queue pressure and SLO-aware fallback.<!-- existing:SF-2026-ARXIV-2605-16637:end -->
<!-- delta:SF-2026-ARXIV-2605-16637:start -->Ch56 already owns online workflow DAGs, heterogeneous placement, critical-path scheduling, queue pressure and SLO-aware fallback.<!-- delta:SF-2026-ARXIV-2605-16637:end --> Final decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-16637:end -->

<!-- books-review:SF-2026-ARXIV-2605-16650:start -->
<!-- existing:SF-2026-ARXIV-2605-16650:start -->Ch66 and Ch77 already evaluate stateful dialogue through incremental state identity, provenance, contradiction handling and longitudinal effects.<!-- existing:SF-2026-ARXIV-2605-16650:end -->
<!-- delta:SF-2026-ARXIV-2605-16650:start -->Ch66 and Ch77 already evaluate stateful dialogue through incremental state identity, provenance, contradiction handling and longitudinal effects.<!-- delta:SF-2026-ARXIV-2605-16650:end --> Final decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-16650:end -->

<!-- books-review:SF-2026-ARXIV-2605-16704:start -->
<!-- existing:SF-2026-ARXIV-2605-16704:start -->Ch27 already treats dataset value as a set-level gradient-space diversity/quality allocation problem rather than additive example scores.<!-- existing:SF-2026-ARXIV-2605-16704:end -->
<!-- delta:SF-2026-ARXIV-2605-16704:start -->Ch27 already treats dataset value as a set-level gradient-space diversity/quality allocation problem rather than additive example scores.<!-- delta:SF-2026-ARXIV-2605-16704:end --> Final decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-16704:end -->

<!-- books-review:SF-2026-ARXIV-2605-16712:start -->
<!-- existing:SF-2026-ARXIV-2605-16712:start -->`books/part-07-agent/77-memory.md` contains the surrounding principle but not the exact control/evidence delta below; adjacent chapters do not own it.<!-- existing:SF-2026-ARXIV-2605-16712:end -->
<!-- delta:SF-2026-ARXIV-2605-16712:start -->Retrieved personal facts must not automatically become behavioral commitments; activation, validation and realization need a bounded-commitment authority distinct from recall ownership.<!-- delta:SF-2026-ARXIV-2605-16712:end --> Final decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-16712:end -->

<!-- books-review:SF-2026-ARXIV-2605-16725:start -->
<!-- existing:SF-2026-ARXIV-2605-16725:start -->Ch25 already requires persistent, revisable and executable world state updated by failed predictions and targeted exploration.<!-- existing:SF-2026-ARXIV-2605-16725:end -->
<!-- delta:SF-2026-ARXIV-2605-16725:start -->Ch25 already requires persistent, revisable and executable world state updated by failed predictions and targeted exploration.<!-- delta:SF-2026-ARXIV-2605-16725:end --> Final decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-16725:end -->

<!-- books-review:SF-2026-ARXIV-2605-16745:start -->
<!-- existing:SF-2026-ARXIV-2605-16745:start -->已逐章读取 `books/part-03-multimodal-world-models/23-multimodal-representation.md` 与相邻章节 ['books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md']；当前正文拥有 surrounding principle，但尚未显式承载 `EVA01: Unified Native 3D Understanding and Generation via Mixture-of-Transformers` 改变的 state/data/control/evidence boundary。 owner_sha256=cde0ccfed7241f74e706727568f977cfe98384d75b2483b4c57eedc44fa486c4。<!-- existing:SF-2026-ARXIV-2605-16745:end -->
<!-- delta:SF-2026-ARXIV-2605-16745:start -->EVA01: Unified Native 3D Understanding and Generation via Mixture-of-Transformers 提出的具体变化是：We introduce EVA01, a unified framework that extends the modality boundary of MLLMs to natively incorporate 3D mesh understanding, generation, and context-aware editing. 摘要中的长期系统挑战为：native 3D tokens join understanding and generation rather than remaining a stateless reconstruction sidecar。它可能改变 `MULTIMODAL-REPRESENTATION` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“Results show that EVA01 achieves state-of-the-art native text-to-3D generation fidelity and unlocks robust long-context multi-turn geometric editing with identity preservation, a capability fundamentally inaccessible to stateless reconstruction pipelines.”暂不作为最终证据。<!-- delta:SF-2026-ARXIV-2605-16745:end --> Decision=`Integrate`；non-author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-16745:end -->

<!-- books-review:SF-2026-ARXIV-2605-16746:start -->
<!-- existing:SF-2026-ARXIV-2605-16746:start -->`books/part-07-agent/77-memory.md` 已以更一般的 `AGENT-MEMORY` 演进链承载该问题的 owner、commit/evidence boundary、failure fallback 与旧路径共存；本 family 只增加受限实现或 benchmark evidence。 owner_sha256=ac3bf5ab49bb87bcf3f0cfa1da47486caeb35e9d451251f91c67caf3bc9de6d7。<!-- existing:SF-2026-ARXIV-2605-16746:end -->
<!-- delta:SF-2026-ARXIV-2605-16746:start -->State Contamination in Memory-Augmented LLM Agents 提出的具体变化是：To measure this hidden influence, we introduce the sub-threshold propagation gap (SPG), which quantifies downstream behavioral differences conditioned on memory states that a deployed monitor would classify as safe. 摘要中的长期系统挑战为：persistent memory becomes a cross-turn attack surface whose writes and reuse require separate authority。它可能改变 `AGENT-MEMORY` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“These results suggest that safety in memory-augmented agents should be treated as a state-control problem over evolving context, with sanitization applied before unsafe information is compressed into persistent memory.”暂不作为最终证据。<!-- delta:SF-2026-ARXIV-2605-16746:end --> Decision=`No Change — Existing Coverage`；non-author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-16746:end -->

<!-- books-review:SF-2026-ARXIV-2605-16776:start -->
<!-- existing:SF-2026-ARXIV-2605-16776:start -->已逐章读取 `books/part-06-ai-infrastructure/72-security.md` 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；当前正文拥有 surrounding principle，但尚未显式承载 `Distinguishable Deletion: Unifying Knowledge Erasure and Refusal for Large Language Model Unlearning` 改变的 state/data/control/evidence boundary。 owner_sha256=b4a3cdb8a1a37d72b85afa4def5d2fd3756d9432a2a7ddd0c60732f5bdbf9c1d。<!-- existing:SF-2026-ARXIV-2605-16776:end -->
<!-- delta:SF-2026-ARXIV-2605-16776:start -->Distinguishable Deletion: Unifying Knowledge Erasure and Refusal for Large Language Model Unlearning 提出的具体变化是：To address these issues, we propose Distinguishable Deletion ($\mathrm{D^2}$), a paradigm that restricts the response distribution in the latent representation rather than specific tokens to erase undesirable knowledge, while distinguishing it from retained knowledge, enabling a refusal mechanism to handle unlearned inputs safely and coherently. 摘要中的长期系统挑战为：unlearning must distinguish parameter erasure from inference-time refusal and verify both contracts。它可能改变 `PLATFORM-SECURITY` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“Extensive experiments demonstrate that EUA significantly outperforms previous methods, indicating the superiority of $\mathrm{D^2}$.”暂不作为最终证据。<!-- delta:SF-2026-ARXIV-2605-16776:end --> Decision=`Integrate`；non-author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-16776:end -->

<!-- books-review:SF-2026-ARXIV-2605-16786:start -->
<!-- existing:SF-2026-ARXIV-2605-16786:start -->已逐章读取 `books/part-05-inference-system/48-speculative-decoding.md` 与相邻章节 ['books/part-05-inference-system/47-pagedattention.md', 'books/part-05-inference-system/49-tensorrt-llm.md']；当前正文拥有 surrounding principle，但尚未显式承载 `Lever: Speculative LLM Inference on Smartphones` 改变的 state/data/control/evidence boundary。 owner_sha256=6e03731cbbf82d3455fb4df123c710eee96e98d84d4c80680ad56e47c9b84dc3。<!-- existing:SF-2026-ARXIV-2605-16786:end -->
<!-- delta:SF-2026-ARXIV-2605-16786:start -->Lever: Speculative LLM Inference on Smartphones 提出的具体变化是：We present Lever, an end-to-end system for efficient flash-backed LLM inference on smartphones. 摘要中的长期系统挑战为：flash-backed mobile inference changes the draft/verify cost model and state-placement boundary。它可能改变 `INFER-SPECULATIVE-DECODING` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“We observe that speculative decoding is a natural fit for this setting: a small draft model can remain in DRAM, while a larger flash-resident target model verifies multiple candidate tokens per invocation.”暂不作为最终证据。<!-- delta:SF-2026-ARXIV-2605-16786:end --> Decision=`Integrate`；non-author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-16786:end -->

<!-- books-review:SF-2026-ARXIV-2605-16787:start -->
<!-- existing:SF-2026-ARXIV-2605-16787:start -->已逐章读取 `books/part-04-training-system/33-grpo.md` 与相邻章节 ['books/part-04-training-system/32-ppo.md', 'books/part-04-training-system/34-dpo.md']；当前正文拥有 surrounding principle，但尚未显式承载 `The Unlearnability Phenomenon in RLVR for Language Models` 改变的 state/data/control/evidence boundary。 owner_sha256=c75d66bc18a9221e70da0fc29018962765e69241af2ce0959becf0ab5f8e49a8。<!-- existing:SF-2026-ARXIV-2605-16787:end -->
<!-- delta:SF-2026-ARXIV-2605-16787:start -->The Unlearnability Phenomenon in RLVR for Language Models 提出的具体变化是：Reinforcement Learning with Verifiable Reward (RLVR) has proven effective in improving Large Language Model's (LLM) reasoning ability. 摘要中的长期系统挑战为：RLVR admission must recognize examples with no useful policy-gradient direction rather than treating all verified rewards alike。它可能改变 `TRAIN-GRPO` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“With cross-example gradient analysis, we show that unlearnable examples have fundamental representation issue, characterized by low gradient similarity with the rest of the examples and ungeneralizable reasoning patterns.”暂不作为最终证据。<!-- delta:SF-2026-ARXIV-2605-16787:end --> Decision=`Integrate`；non-author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-16787:end -->

<!-- books-review:SF-2026-ARXIV-2605-16790:start -->
<!-- existing:SF-2026-ARXIV-2605-16790:start -->已逐章读取 `books/part-07-agent/78-tool-calling.md` 与相邻章节 ['books/part-07-agent/77-memory.md', 'books/part-07-agent/79-planning.md']；当前正文拥有 surrounding principle，但尚未显式承载 `TIER: Trajectory-Invariant Execution Rewards for Multi-Step Tool Composition` 改变的 state/data/control/evidence boundary。 owner_sha256=73f2708a56d1c3852ff08cba8240fd7021f192a4778636a241608de26bbbb2e4。<!-- existing:SF-2026-ARXIV-2605-16790:end -->
<!-- delta:SF-2026-ARXIV-2605-16790:start -->TIER: Trajectory-Invariant Execution Rewards for Multi-Step Tool Composition 提出的具体变化是：We propose TIER: Trajectory-Invariant Execution Rewards, a reward framework that derives supervision directly from function schemas and runtime execution, rather than from reference trajectories. 摘要中的长期系统挑战为：tool-composition reward moves from reference trajectories to invariant execution-state evidence。它可能改变 `AGENT-TOOL-CALLING` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“Ablation studies confirm that all reward components are necessary, highlighting the importance of multi-level supervision for compositional reasoning.”暂不作为最终证据。<!-- delta:SF-2026-ARXIV-2605-16790:end --> Decision=`Integrate`；non-author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-16790:end -->

<!-- books-review:SF-2026-ARXIV-2605-16819:start -->
<!-- existing:SF-2026-ARXIV-2605-16819:start -->已逐章读取 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前正文拥有 surrounding principle，但尚未显式承载 `AgentKernelArena: Generalization-Aware Benchmarking of GPU Kernel Optimization Agents` 改变的 state/data/control/evidence boundary。 owner_sha256=089fc06685d0e6238733d8b293222afd04aeacd6d35cf016f2c21fe13c9e8ef1。<!-- existing:SF-2026-ARXIV-2605-16819:end -->
<!-- delta:SF-2026-ARXIV-2605-16819:start -->AgentKernelArena: Generalization-Aware Benchmarking of GPU Kernel Optimization Agents 提出的具体变化是：We present AgentKernelArena, an open-source benchmark for measuring AI coding agents on GPU kernel optimization. 摘要中的长期系统挑战为：agent evaluation must freeze workflow state, hidden task contract, runtime receipts and unseen-shape generalization。它可能改变 `PLATFORM-EVALUATION-SYSTEM` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“AgentKernelArena is designed as a modular, extensible framework for rigorous evaluation of agentic GPU kernel optimization across agents, tasks, and hardware targets.”暂不作为最终证据。<!-- delta:SF-2026-ARXIV-2605-16819:end --> Decision=`Integrate`；non-author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-16819:end -->

<!-- books-review:SF-2026-ARXIV-2605-16826:start -->
<!-- existing:SF-2026-ARXIV-2605-16826:start -->已逐章读取 `books/part-04-training-system/28-pretraining.md` 与相邻章节 ['books/part-04-training-system/27-data.md', 'books/part-04-training-system/29-sft.md']；当前正文拥有 surrounding principle，但尚未显式承载 `Decoupling KL and Trajectories: A Unified Perspective for SFT, DAgger, Offline RL, and OPD in LLM Distillation` 改变的 state/data/control/evidence boundary。 owner_sha256=0eca9f709aa5037490fd8ccf36118c63b0a7a18c7abb5e68100e8b89473faf65。<!-- existing:SF-2026-ARXIV-2605-16826:end -->
<!-- delta:SF-2026-ARXIV-2605-16826:start -->Decoupling KL and Trajectories: A Unified Perspective for SFT, DAgger, Offline RL, and OPD in LLM Distillation 提出的具体变化是：Motivated by these findings, we propose KL mixing and an entropy-gated length curriculum. 摘要中的长期系统挑战为：distillation outcomes depend separately on prefix provenance and KL direction, changing the training contract。它可能改变 `TRAIN-PRETRAINING` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“Our results provide a framework and practical methods for designing reasoning distillation objectives that balance accuracy, diversity, compute, and RL behavior.”暂不作为最终证据。<!-- delta:SF-2026-ARXIV-2605-16826:end --> Decision=`Integrate`；non-author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-16826:end -->

<!-- books-review:SF-2026-ARXIV-2605-16839:start -->
<!-- existing:SF-2026-ARXIV-2605-16839:start -->已逐章读取 `books/part-05-inference-system/43-prefill.md` 与相邻章节 ['books/part-05-inference-system/42-what-happens-during-inference.md', 'books/part-05-inference-system/44-decode.md']；当前正文拥有 surrounding principle，但尚未显式承载 `CompactAttention: Accelerating Chunked Prefill with Block-Union KV Selection` 改变的 state/data/control/evidence boundary。 owner_sha256=dc847cff021d99b03c0e59549275c3564437e632f8614a227ef9be66a999076d。<!-- existing:SF-2026-ARXIV-2605-16839:end -->
<!-- delta:SF-2026-ARXIV-2605-16839:start -->CompactAttention: Accelerating Chunked Prefill with Block-Union KV Selection 提出的具体变化是：To address these limitations, we propose CompactAttention, a chunked-prefill attention mechanism based on Block-Union KV Selection. 摘要中的长期系统挑战为：chunked prefill reuses a union of selected KV blocks while preserving the dense attention owner。它可能改变 `INFER-PREFILL` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“On LLaMA-3.1-8B-Instruct, CompactAttention maintains accuracy close to dense attention on the RULER benchmark while delivering up to 2.72$\times$ attention speedup at 128K context length under chunked prefill.”暂不作为最终证据。<!-- delta:SF-2026-ARXIV-2605-16839:end --> Decision=`Integrate`；non-author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-16839:end -->

<!-- books-review:SF-2026-ARXIV-2605-16867:start -->
<!-- existing:SF-2026-ARXIV-2605-16867:start -->`books/part-05-inference-system/56-inference-scheduling.md` 已以更一般的 `INFER-SCHEDULING` 演进链承载该问题的 owner、commit/evidence boundary、failure fallback 与旧路径共存；本 family 只增加受限实现或 benchmark evidence。 owner_sha256=1e3e8c3dff17a6bd79b65130176926b9f10cb1e2ff5bf3e042d4ccee6c302280。<!-- existing:SF-2026-ARXIV-2605-16867:end -->
<!-- delta:SF-2026-ARXIV-2605-16867:start -->In this paper, we propose GoodServe, a goodput-optimized serving system for agentic inferences over heterogeneous resources.<!-- delta:SF-2026-ARXIV-2605-16867:end --> Decision=`No Change — Existing Coverage`；non-author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-16867:end -->

<!-- books-review:SF-2026-ARXIV-2605-16928:start -->
<!-- existing:SF-2026-ARXIV-2605-16928:start -->已逐章读取 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 与相邻章节 ['books/part-05-inference-system/44-decode.md', 'books/part-05-inference-system/46-continuous-batching.md']；当前正文拥有 surrounding principle，但尚未显式承载 `Full Attention Strikes Back: Transferring Full Attention into Sparse within Hundred Training Steps` 改变的 state/data/control/evidence boundary。 owner_sha256=94425d5fe4db0238e99350a5a0299edb408dcffcdb7b32453c76854a9dbc8e86。<!-- existing:SF-2026-ARXIV-2605-16928:end -->
<!-- delta:SF-2026-ARXIV-2605-16928:start -->Full Attention Strikes Back: Transferring Full Attention into Sparse within Hundred Training Steps 提出的具体变化是：Based on these insights, we propose RTPurbo, which retains the full KV cache only for retrieval heads and introduces a lightweight token indexer for sparse attention. 摘要中的长期系统挑战为：head-aware dense-to-sparse post-training separates candidate routing from exact attention。它可能改变 `INFER-KV-CACHE` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“These results suggest that strong sparse inference can be obtained from standard full-attention training without expensive native sparse pretraining.”暂不作为最终证据。<!-- delta:SF-2026-ARXIV-2605-16928:end --> Decision=`Integrate`；non-author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-16928:end -->

<!-- books-review:SF-2026-ARXIV-2605-16976:start -->
<!-- existing:SF-2026-ARXIV-2605-16976:start -->已逐章读取 `books/part-06-ai-infrastructure/72-security.md` 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；当前正文拥有 surrounding principle，但尚未显式承载 `Securing LLM Agents Need Intent-to-Execution Integrity` 改变的 state/data/control/evidence boundary。 owner_sha256=b4a3cdb8a1a37d72b85afa4def5d2fd3756d9432a2a7ddd0c60732f5bdbf9c1d。<!-- existing:SF-2026-ARXIV-2605-16976:end -->
<!-- delta:SF-2026-ARXIV-2605-16976:start -->Drawing on this analogy, we identify two fundamental problem sources -- untrusted data ingestion and untrusted tool execution -- and derive four integrity properties that must hold simultaneously: \emph{Tool Integrity}, \emph{Instruction Integrity}, \emph{Judgment Integrity}, and \emph{Data Flow Integrity}.<!-- delta:SF-2026-ARXIV-2605-16976:end --> Decision=`Integrate`；non-author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-16976:end -->

<!-- books-review:SF-2026-ARXIV-2605-16986:start -->
<!-- existing:SF-2026-ARXIV-2605-16986:start -->`books/part-07-agent/84-agent-platform.md` 已以更一般的 `AGENT-PLATFORM` 演进链承载该问题的 owner、commit/evidence boundary、failure fallback 与旧路径共存；本 family 只增加受限实现或 benchmark evidence。 owner_sha256=c90613b1e2cab33b382c0cff6ae0226e44b2d66b051e12a15174eae9c5fc6cdc。<!-- existing:SF-2026-ARXIV-2605-16986:end -->
<!-- delta:SF-2026-ARXIV-2605-16986:start -->Skills on the Fly: Test-Time Adaptive Skill Synthesis for LLM Agents 提出的具体变化是：We call this challenge test-time compute-to-capability conversion and propose SkillTTA, which retrieves task-relevant training trajectories and synthesizes a temporary skill conditioned on the visible target context for a solver with fixed parameters. 摘要中的长期系统挑战为：test-time skill synthesis creates ephemeral executable state that needs admission, expiry and rollback。它可能改变 `AGENT-PLATFORM` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“Across ALFWorld, SpreadsheetBench, BigCodeBench, and WebShop, SkillTTA outperforms state-of-the-art reuse and optimization baselines.”暂不作为最终证据。<!-- delta:SF-2026-ARXIV-2605-16986:end --> Decision=`No Change — Existing Coverage`；non-author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-16986:end -->

<!-- books-review:SF-2026-ARXIV-2605-17003:start -->
<!-- existing:SF-2026-ARXIV-2605-17003:start -->已逐章读取 `books/part-04-training-system/27-data.md` 与相邻章节 ['books/part-04-training-system/28-pretraining.md']；当前正文拥有 surrounding principle，但尚未显式承载 `Learning-Zone Energy: Online Data Selection for Efficient RL Post-Training` 改变的 state/data/control/evidence boundary。 owner_sha256=9e54b8820f3288dddf939ad59b0cfec8944d21573c4b03a10227688eb11a5ef1。<!-- existing:SF-2026-ARXIV-2605-17003:end -->
<!-- delta:SF-2026-ARXIV-2605-17003:start -->Learning-Zone Energy: Online Data Selection for Efficient RL Post-Training 提出的具体变化是：To address this fundamental inefficiency, we propose Learning-Zone Energy (LZE), a theoretically grounded, fully online data selection framework that concentrates computation on the model's active learning frontier. 摘要中的长期系统挑战为：online RL data selection becomes a control loop over current policy frontier rather than a static dataset。它可能改变 `TRAIN-DATA` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“Our code is available at https://github.com/Stellaris167/LZE.”暂不作为最终证据。<!-- delta:SF-2026-ARXIV-2605-17003:end --> Decision=`Integrate`；non-author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17003:end -->

<!-- books-review:SF-2026-ARXIV-2605-17026:start -->
<!-- existing:SF-2026-ARXIV-2605-17026:start -->已逐章读取 `books/part-04-training-system/27-data.md` 与相邻章节 ['books/part-04-training-system/28-pretraining.md']；当前正文拥有 surrounding principle，但尚未显式承载 `Why Do Reasoning Models Lose Coverage? The Role of Data and Forks in the Road` 改变的 state/data/control/evidence boundary。 owner_sha256=9e54b8820f3288dddf939ad59b0cfec8944d21573c4b03a10227688eb11a5ef1。<!-- existing:SF-2026-ARXIV-2605-17026:end -->
<!-- delta:SF-2026-ARXIV-2605-17026:start -->While these methods reliably improve pass@1 accuracy, prior works have observed that they show a coverage shrinkage behavior, where pass@k degrades relative to the base model.<!-- delta:SF-2026-ARXIV-2605-17026:end --> Decision=`Integrate`；non-author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17026:end -->

<!-- books-review:SF-2026-ARXIV-2605-17028:start -->
<!-- existing:SF-2026-ARXIV-2605-17028:start -->`books/part-06-ai-infrastructure/66-evaluation-system.md` 已以更一般的 `PLATFORM-EVALUATION-SYSTEM` 演进链承载该问题的 owner、commit/evidence boundary、failure fallback 与旧路径共存；本 family 只增加受限实现或 benchmark evidence。 owner_sha256=089fc06685d0e6238733d8b293222afd04aeacd6d35cf016f2c21fe13c9e8ef1。<!-- existing:SF-2026-ARXIV-2605-17028:end -->
<!-- delta:SF-2026-ARXIV-2605-17028:start -->We show, however, that much of this apparent progress does not survive scrutiny.<!-- delta:SF-2026-ARXIV-2605-17028:end --> Decision=`No Change — Existing Coverage`；non-author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17028:end -->

<!-- books-review:SF-2026-ARXIV-2605-17034:start -->
<!-- existing:SF-2026-ARXIV-2605-17034:start -->`books/part-06-ai-infrastructure/72-security.md` 已以更一般的 `PLATFORM-SECURITY` 演进链承载该问题的 owner、commit/evidence boundary、failure fallback 与旧路径共存；本 family 只增加受限实现或 benchmark evidence。 owner_sha256=b4a3cdb8a1a37d72b85afa4def5d2fd3756d9432a2a7ddd0c60732f5bdbf9c1d。<!-- existing:SF-2026-ARXIV-2605-17034:end -->
<!-- delta:SF-2026-ARXIV-2605-17034:start -->Privacy Policy Enforcement Guardrails for Data-Sensitive Retrieval-Augmented Generation 提出的具体变化是：We introduce a Privacy Policy Enforcement (PPE) framework using dual one-class density estimators with fused text embeddings and a calibrated abstain region for out-of-distribution inputs. 摘要中的长期系统挑战为：RAG privacy enforcement must mediate retrieval and generation effects rather than rely on prompt policy。它可能改变 `PLATFORM-SECURITY` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“This methodology provides a robust stress-testing standard for any synthetic-data-trained classifier.”暂不作为最终证据。<!-- delta:SF-2026-ARXIV-2605-17034:end --> Decision=`No Change — Existing Coverage`；non-author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17034:end -->

<!-- books-review:SF-2026-ARXIV-2605-17062:start -->
<!-- existing:SF-2026-ARXIV-2605-17062:start -->`books/part-06-ai-infrastructure/72-security.md` 已以更一般的 `PLATFORM-SECURITY` 演进链承载该问题的 owner、commit/evidence boundary、failure fallback 与旧路径共存；本 family 只增加受限实现或 benchmark evidence。 owner_sha256=b4a3cdb8a1a37d72b85afa4def5d2fd3756d9432a2a7ddd0c60732f5bdbf9c1d。<!-- existing:SF-2026-ARXIV-2605-17062:end -->
<!-- delta:SF-2026-ARXIV-2605-17062:start -->The Range Shrinks, the Threat Remains: Re-evaluating LLM Package Hallucinations on the 2026 Frontier-Model Cohort 提出的具体变化是：Across 199,845 paired Python and JavaScript prompts validated against PyPI and npm master lists, we measure overall hallucination rates between 4.62% (Claude Haiku 4.5) and 6.10% (GPT-5.4-mini) -- an order-of-magnitude compression of the inter-model spread observed by Spracklen, but not a retirement of the threat. 摘要中的长期系统挑战为：package hallucinations create a model-to-software-supply-chain effect path requiring independent resolution。它可能改变 `PLATFORM-SECURITY` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“We further document a Python-over-JavaScript hallucination asymmetry that inverts Spracklen's 2024 finding, identify a Haiku-below-Sonnet inversion within the Anthropic family, and observe a Jaccard-similarity peak between DeepSeek V3.2 and GPT-5.4-mini (J = 0.343) suggestive of shared training-data origins.”暂不作为最终证据。<!-- delta:SF-2026-ARXIV-2605-17062:end --> Decision=`No Change — Existing Coverage`；non-author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17062:end -->

<!-- books-review:SF-2026-ARXIV-2605-17076:start -->
<!-- existing:SF-2026-ARXIV-2605-17076:start -->已逐章读取 `books/part-07-agent/82-multi-agent.md` 与相邻章节 ['books/part-07-agent/81-workflow.md', 'books/part-07-agent/83-mcp.md']；当前正文拥有 surrounding principle，但尚未显式承载 `S-Bus: Automatic Read-Set Reconstruction for Multi-Agent LLM State Coordination` 改变的 state/data/control/evidence boundary。 owner_sha256=948a0d2dac39b1e241adb0b692a057f0b8ef5411dda794e210d733cba06fa3d3。<!-- existing:SF-2026-ARXIV-2605-17076:end -->
<!-- delta:SF-2026-ARXIV-2605-17076:start -->S-Bus: Automatic Read-Set Reconstruction for Multi-Agent LLM State Coordination 提出的具体变化是：S-Bus is an HTTP middleware whose central mechanism, a server-side DeliveryLog, reconstructs each agent's read set at commit time from observed HTTP GET traffic. 摘要中的长期系统挑战为：observable-read isolation gives shared mutable multi-agent state an explicit consistency boundary。它可能改变 `AGENT-MULTI-AGENT` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“Source code, formal proofs, harness, annotation data: https://github.com/sajjadanwar0/sbus”暂不作为最终证据。<!-- delta:SF-2026-ARXIV-2605-17076:end --> Decision=`Integrate`；non-author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17076:end -->

<!-- books-review:SF-2026-ARXIV-2605-17106:start -->
<!-- existing:SF-2026-ARXIV-2605-17106:start -->已逐章读取 `books/part-05-inference-system/56-inference-scheduling.md` 与相邻章节 ['books/part-05-inference-system/55-pd-disaggregation.md']；当前正文拥有 surrounding principle，但尚未显式承载 `HyDRA: Hybrid Dynamic Routing Architecture for Heterogeneous LLM Pools` 改变的 state/data/control/evidence boundary。 owner_sha256=1e3e8c3dff17a6bd79b65130176926b9f10cb1e2ff5bf3e042d4ccee6c302280。<!-- existing:SF-2026-ARXIV-2605-17106:end -->
<!-- delta:SF-2026-ARXIV-2605-17106:start -->HyDRA: Hybrid Dynamic Routing Architecture for Heterogeneous LLM Pools 提出的具体变化是：We present HyDRA (Hybrid Dynamic Routing Architecture), a framework that predicts fine-grained, multi-dimensional capability requirements per query and matches them against configuration-defined model profiles via shortfall matching. 摘要中的长期系统挑战为：heterogeneous model pools and routing policy become decoupled deployable revisions。它可能改变 `INFER-SCHEDULING` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“Results generalize across LiveCodeBench, BigCodeBench, and tau-bench.”暂不作为最终证据。<!-- delta:SF-2026-ARXIV-2605-17106:end --> Decision=`Integrate`；non-author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17106:end -->

<!-- books-review:SF-2026-ARXIV-2605-17113:start -->
<!-- existing:SF-2026-ARXIV-2605-17113:start -->已逐章读取 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前正文拥有 surrounding principle，但尚未显式承载 `The Point of No Return: Counterfactual Localization of Deceptive Commitment in Language-Model Reasoning` 改变的 state/data/control/evidence boundary。 owner_sha256=089fc06685d0e6238733d8b293222afd04aeacd6d35cf016f2c21fe13c9e8ef1。<!-- existing:SF-2026-ARXIV-2605-17113:end -->
<!-- delta:SF-2026-ARXIV-2605-17113:start -->We introduce counterfactual localization: for each sentence prefix in a reasoning trace, we fix the prefix, resample continuations, and estimate the probability of a deceptive outcome.<!-- delta:SF-2026-ARXIV-2605-17113:end --> Decision=`Integrate`；non-author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17113:end -->

<!-- books-review:SF-2026-ARXIV-2605-17160:start -->
<!-- existing:SF-2026-ARXIV-2605-17160:start -->已逐章读取 `books/part-05-inference-system/49-tensorrt-llm.md` 与相邻章节 ['books/part-05-inference-system/48-speculative-decoding.md', 'books/part-05-inference-system/50-vllm.md']；当前正文拥有 surrounding principle，但尚未显式承载 `When Bits Break Recourse: Counterfactual-Faithful Quantization` 改变的 state/data/control/evidence boundary。 owner_sha256=8ee7425b911361c8e1e632272a759a2ae9eb63723aeb30c1237bc304ce07fb7b。<!-- existing:SF-2026-ARXIV-2605-17160:end -->
<!-- delta:SF-2026-ARXIV-2605-17160:start -->We propose two metrics: Validity Drop (VD), which measures the fraction of full-precision recourse actions that no longer achieve the target outcome after quantization, and Counterfactual Recourse Gap (CRG), which measures the increase in minimal recourse cost under the quantized model.<!-- delta:SF-2026-ARXIV-2605-17160:end --> Decision=`Integrate`；non-author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17160:end -->

<!-- books-review:SF-2026-ARXIV-2605-17164:start -->
<!-- existing:SF-2026-ARXIV-2605-17164:start -->已逐章读取 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前正文拥有 surrounding principle，但尚未显式承载 `Charon: A Unified and Fine-Grained Simulator for Large-Scale LLM Training and Inference` 改变的 state/data/control/evidence boundary。 owner_sha256=089fc06685d0e6238733d8b293222afd04aeacd6d35cf016f2c21fe13c9e8ef1。<!-- existing:SF-2026-ARXIV-2605-17164:end -->
<!-- delta:SF-2026-ARXIV-2605-17164:start -->Charon: A Unified and Fine-Grained Simulator for Large-Scale LLM Training and Inference 提出的具体变化是：To address this, we introduce Charon, a unified, modular, and fine-grained simulator for accurately predicting LLM performance. 摘要中的长期系统挑战为：training and inference what-if simulation need a shared configuration identity and validation contract。它可能改变 `PLATFORM-EVALUATION-SYSTEM` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“In a practical inference deployment case, Charon discovered a configuration that improved system throughput over an engineering-tuned baseline, demonstrating its significant real-world value.”暂不作为最终证据。<!-- delta:SF-2026-ARXIV-2605-17164:end --> Decision=`Integrate`；non-author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17164:end -->

<!-- books-review:SF-2026-ARXIV-2605-17169:start -->
<!-- existing:SF-2026-ARXIV-2605-17169:start -->`books/part-07-agent/84-agent-platform.md` 已以更一般的 `AGENT-PLATFORM` 演进链承载该问题的 owner、commit/evidence boundary、failure fallback 与旧路径共存；本 family 只增加受限实现或 benchmark evidence。 owner_sha256=c90613b1e2cab33b382c0cff6ae0226e44b2d66b051e12a15174eae9c5fc6cdc。<!-- existing:SF-2026-ARXIV-2605-17169:end -->
<!-- delta:SF-2026-ARXIV-2605-17169:start -->Agentic AI is rapidly proliferating across diverse real-world domains such as software engineering, yet public trust has not kept pace.<!-- delta:SF-2026-ARXIV-2605-17169:end --> Decision=`No Change — Existing Coverage`；non-author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17169:end -->

<!-- books-review:SF-2026-ARXIV-2605-17170:start -->
<!-- existing:SF-2026-ARXIV-2605-17170:start -->已逐章读取 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 与相邻章节 ['books/part-05-inference-system/44-decode.md', 'books/part-05-inference-system/46-continuous-batching.md']；当前正文拥有 surrounding principle，但尚未显式承载 `TriAxialKV: Toward Extreme Low-Precision KV-Cache Quantization for Agentic Inference Tasks` 改变的 state/data/control/evidence boundary。 owner_sha256=94425d5fe4db0238e99350a5a0299edb408dcffcdb7b32453c76854a9dbc8e86。<!-- existing:SF-2026-ARXIV-2605-17170:end -->
<!-- delta:SF-2026-ARXIV-2605-17170:start -->TriAxialKV: Toward Extreme Low-Precision KV-Cache Quantization for Agentic Inference Tasks 提出的具体变化是：To this end, we introduce TriAxialKV, a novel mixed-precision KV-cache quantization scheme that assigns each token a triaxial tag, calibrates per-tag sensitivity, and allocates INT2/INT4 bitwidths under a fixed memory budget. 摘要中的长期系统挑战为：agentic KV quantization must condition precision on role, modality and temporal lifecycle。它可能改变 `INFER-KV-CACHE` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“As a result, their context exhibits structure that can carry different importance along three key axes: temporal recency to the current turn, modality such as text or image tokens, and semantic role such as user queries, tool calls, observations, or reasoning.”暂不作为最终证据。<!-- delta:SF-2026-ARXIV-2605-17170:end --> Decision=`Integrate`；non-author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17170:end -->

<!-- books-review:SF-2026-ARXIV-2605-17172:start -->
<!-- existing:SF-2026-ARXIV-2605-17172:start -->`books/part-07-agent/84-agent-platform.md` 已以更一般的 `AGENT-PLATFORM` 演进链承载该问题的 owner、commit/evidence boundary、failure fallback 与旧路径共存；本 family 只增加受限实现或 benchmark evidence。 owner_sha256=c90613b1e2cab33b382c0cff6ae0226e44b2d66b051e12a15174eae9c5fc6cdc。<!-- existing:SF-2026-ARXIV-2605-17172:end -->
<!-- delta:SF-2026-ARXIV-2605-17172:start -->OpenJarvis: Personal AI, On Personal Devices 提出的具体变化是：We present OpenJarvis, an architecture that represents a personal AI system as a typed spec over five primitives: Intelligence, Engine, Agents, Tools &amp; Memory, and Learning. 摘要中的长期系统挑战为：personal AI splits sensitive local state, local execution and optional cloud escalation into typed boundaries。它可能改变 `AGENT-PLATFORM` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“They also reduce marginal API cost by ~800x and end-to-end latency by 4x.”暂不作为最终证据。<!-- delta:SF-2026-ARXIV-2605-17172:end --> Decision=`No Change — Existing Coverage`；non-author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17172:end -->

<!-- books-review:SF-2026-ARXIV-2605-17173:start -->
<!-- existing:SF-2026-ARXIV-2605-17173:start -->已逐章读取 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前正文拥有 surrounding principle，但尚未显式承载 `Why Do Safety Guardrails Degrade Across Languages?` 改变的 state/data/control/evidence boundary。 owner_sha256=089fc06685d0e6238733d8b293222afd04aeacd6d35cf016f2c21fe13c9e8ef1。<!-- existing:SF-2026-ARXIV-2605-17173:end -->
<!-- delta:SF-2026-ARXIV-2605-17173:start -->Why Do Safety Guardrails Degrade Across Languages? 提出的具体变化是：We introduce a latent variable model, a Multi-Group Item Response Theory (IRT) framework, that decouples language-agnostic safety robustness ($θ$), intrinsic prompt hardness ($β$), global language processing difficulty ($γ$), and a prompt-specific cross-lingual safety gap ($τ$). 摘要中的长期系统挑战为：multilingual safety evaluation must decompose the failure factors hidden by aggregate jailbreak rate。它可能改变 `PLATFORM-EVALUATION-SYSTEM` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“Our framework reveals concept-language vulnerabilities that aggregate metrics obscure, enabling fairer cross-lingual safety evaluation and targeted improvements in dataset construction.”暂不作为最终证据。<!-- delta:SF-2026-ARXIV-2605-17173:end --> Decision=`Integrate`；non-author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17173:end -->

<!-- books-review:SF-2026-ARXIV-2605-17193:start -->
<!-- existing:SF-2026-ARXIV-2605-17193:start -->Ch82 已说明 same-model/context agents 共享 correlated error，只有独立 evidence、可验证接口或真实责任分解才可能产生增量；正文还保留趋同、coordination tax、single-Agent、independent proposals、deterministic verifier 与人工 adjudication fallback。Ch81 只拥有 durable workflow state，Ch83 只拥有 protocol interoperability。<!-- existing:SF-2026-ARXIV-2605-17193:end -->
<!-- delta:SF-2026-ARXIV-2605-17193:start -->exact-v1 在作者 closed-loop text simulations 中提供纵向 evidence：词汇变化可继续增长而语义支持收缩，十二类已测 surface/deep intervention 在 Bonferroni correction 后没有显著提升；但 regression 非 causal，recursive-channel theory 是 heuristic，且未覆盖外部 evidence renewal。<!-- delta:SF-2026-ARXIV-2605-17193:end --> Decision=`No Change — Existing Coverage`；无需新增 Books queue 或重复正文。
<!-- books-review:SF-2026-ARXIV-2605-17193:end -->

<!-- books-review:SF-2026-ARXIV-2605-17222:start -->
<!-- existing:SF-2026-ARXIV-2605-17222:start -->独立 reviewer 顺读 `books/part-06-ai-infrastructure/72-security.md` 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=b4a3cdb8a1a37d72b85afa4def5d2fd3756d9432a2a7ddd0c60732f5bdbf9c1d。<!-- existing:SF-2026-ARXIV-2605-17222:end -->
<!-- delta:SF-2026-ARXIV-2605-17222:start -->CKKS 线性变换把 rotation 数量、off-chip traffic 与 FPGA permutation/data-path 共同暴露为隐私推理的硬件执行合同；收益不等于通用 GPU/模型加速。<!-- delta:SF-2026-ARXIV-2605-17222:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17222:end -->

<!-- books-review:SF-2026-ARXIV-2605-17234:start -->
<!-- existing:SF-2026-ARXIV-2605-17234:start -->独立 reviewer 顺读 `books/part-01-worldview/07-scaling-law.md` 与相邻章节 ['books/part-01-worldview/06-why-transformer-changed-the-world.md', 'books/part-01-worldview/08-why-llms-show-intelligence.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=e0c3271fd260faf72be338e83ba9a9e394be267b033f70d14914934a4d51801a。<!-- existing:SF-2026-ARXIV-2605-17234:end -->
<!-- delta:SF-2026-ARXIV-2605-17234:start -->Scaling-law 实验预算从均匀采样演进为 successive-halving 与 surrogate-guided pruning；节省拟合成本的同时引入错误早停与 surrogate selection bias。<!-- delta:SF-2026-ARXIV-2605-17234:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17234:end -->

<!-- books-review:SF-2026-ARXIV-2605-17242:start -->
<!-- existing:SF-2026-ARXIV-2605-17242:start -->独立 reviewer 顺读 `books/part-07-agent/81-workflow.md` 与相邻章节 ['books/part-07-agent/80-reflection.md', 'books/part-07-agent/82-multi-agent.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=6e71a861a0983658675a17c274f4899af49cf05cf91646a8a52289bd724fd6ab。<!-- existing:SF-2026-ARXIV-2605-17242:end -->
<!-- delta:SF-2026-ARXIV-2605-17242:start -->acceptance tests become pre-execution workflow state; browser-observed failures become typed repair evidence rather than terminal text<!-- delta:SF-2026-ARXIV-2605-17242:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17242:end -->

<!-- books-review:SF-2026-ARXIV-2605-17246:start -->
<!-- existing:SF-2026-ARXIV-2605-17246:start -->独立 reviewer 顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=6ef373ceb7416023b9a2ee18a9a6b6b920f2219bb2dae08748e4a6adc5a1febc。<!-- existing:SF-2026-ARXIV-2605-17246:end -->
<!-- delta:SF-2026-ARXIV-2605-17246:start -->Specification–code alignment 由单一测试通过率扩展为 code-grounded fidelity probes、contradiction/coverage-gap 分解和 frozen held-out resampling；probe generator 仍不是完整语义 oracle。<!-- delta:SF-2026-ARXIV-2605-17246:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17246:end -->

<!-- books-review:SF-2026-ARXIV-2605-17260:start -->
<!-- existing:SF-2026-ARXIV-2605-17260:start -->独立 reviewer 顺读 `books/part-03-multimodal-world-models/23-multimodal-representation.md` 与相邻章节 ['books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=cde0ccfed7241f74e706727568f977cfe98384d75b2483b4c57eedc44fa486c4。<!-- existing:SF-2026-ARXIV-2605-17260:end -->
<!-- delta:SF-2026-ARXIV-2605-17260:start -->post-hoc visual-token reduction 会把瓶颈推回逐帧 vision encoder；compressed-token distillation 让 encoder 直接生成时空压缩表示，交换 teacher 成本、表示偏差和 frame coverage。<!-- delta:SF-2026-ARXIV-2605-17260:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17260:end -->

<!-- books-review:SF-2026-ARXIV-2605-17268:start -->
<!-- existing:SF-2026-ARXIV-2605-17268:start -->独立 reviewer 顺读 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 与相邻章节 ['books/part-03-multimodal-world-models/25-multimodal-world-models.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=42393275c6844463595681634a612f8895ae52a56bd78a817077a56b26e65038。<!-- existing:SF-2026-ARXIV-2605-17268:end -->
<!-- delta:SF-2026-ARXIV-2605-17268:start -->VLA 的自然语言 rationale 不能取得 trajectory safety authority；reasoning fidelity、entity/action consistency 与视觉扰动稳定性必须成为独立传感器并由安全控制器提交动作。<!-- delta:SF-2026-ARXIV-2605-17268:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17268:end -->

<!-- books-review:SF-2026-ARXIV-2605-17273:start -->
<!-- existing:SF-2026-ARXIV-2605-17273:start -->独立 reviewer 顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=6ef373ceb7416023b9a2ee18a9a6b6b920f2219bb2dae08748e4a6adc5a1febc。<!-- existing:SF-2026-ARXIV-2605-17273:end -->
<!-- delta:SF-2026-ARXIV-2605-17273:start -->SOTA claim 需要 effect size、consistency、uncertainty 与 task-level superiority 证据，平均分第一只证明 aggregate ranking，不证明广泛优越。<!-- delta:SF-2026-ARXIV-2605-17273:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17273:end -->

<!-- books-review:SF-2026-ARXIV-2605-17281:start -->
<!-- existing:SF-2026-ARXIV-2605-17281:start -->独立 reviewer 顺读 `books/part-07-agent/78-tool-calling.md` 与相邻章节 ['books/part-07-agent/77-memory.md', 'books/part-07-agent/79-planning.md']。当前正文已覆盖一般机制；本项仍留下不可被现有论证替代的状态/控制/证据增量。 owner_sha256=c0020f56aeee2c8008004dd34f27ed47f49f190f17a43909a885ce972a2a41d4。<!-- existing:SF-2026-ARXIV-2605-17281:end -->
<!-- delta:SF-2026-ARXIV-2605-17281:start -->工具 observation 中的 presigned URL、session token 与 OAuth state 是带 byte-integrity 和 expiry 的 contract；模型只能传递，不能自由改写或延迟复用。<!-- delta:SF-2026-ARXIV-2605-17281:end --> Decision=`Integrate`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17281:end -->

<!-- books-review:SF-2026-ARXIV-2605-17288:start -->
<!-- existing:SF-2026-ARXIV-2605-17288:start -->独立 reviewer 顺读 `books/part-05-inference-system/56-inference-scheduling.md` 与相邻章节 ['books/part-05-inference-system/55-pd-disaggregation.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=1e3e8c3dff17a6bd79b65130176926b9f10cb1e2ff5bf3e042d4ccee6c302280。<!-- existing:SF-2026-ARXIV-2605-17288:end -->
<!-- delta:SF-2026-ARXIV-2605-17288:start -->模型 cascade 的轻量 front-end 与 escalation controller 扩大攻击面；攻击可同时破坏质量和成本目标，因此 route/admission 需绑定 adversarial evidence 与保守 fallback。<!-- delta:SF-2026-ARXIV-2605-17288:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17288:end -->

<!-- books-review:SF-2026-ARXIV-2605-17289:start -->
<!-- existing:SF-2026-ARXIV-2605-17289:start -->独立 reviewer 顺读 `books/part-05-inference-system/49-tensorrt-llm.md` 与相邻章节 ['books/part-05-inference-system/48-speculative-decoding.md', 'books/part-05-inference-system/50-vllm.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=8ee7425b911361c8e1e632272a759a2ae9eb63723aeb30c1237bc304ce07fb7b。<!-- existing:SF-2026-ARXIV-2605-17289:end -->
<!-- delta:SF-2026-ARXIV-2605-17289:start -->端到端 unstructured mask learning 把 pruning owner 从 layer-wise surrogate 移到全局 mask objective，但一次性 H100 训练成本和 kernel compatibility 不等于部署 speedup。<!-- delta:SF-2026-ARXIV-2605-17289:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17289:end -->

<!-- books-review:SF-2026-ARXIV-2605-17291:start -->
<!-- existing:SF-2026-ARXIV-2605-17291:start -->独立 reviewer 顺读 `books/part-04-training-system/31-rlhf.md` 与相邻章节 ['books/part-04-training-system/30-lora.md', 'books/part-04-training-system/32-ppo.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=f89604163f74332678caef15a44cb856c58d35237798871d9009db06389a44be。<!-- existing:SF-2026-ARXIV-2605-17291:end -->
<!-- delta:SF-2026-ARXIV-2605-17291:start -->final-answer reward 对中间步骤产生错误 credit；step-wise rubric attribution/normalization 改变 gradient ownership，但依赖 judge 与显式 step boundary。<!-- delta:SF-2026-ARXIV-2605-17291:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17291:end -->

<!-- books-review:SF-2026-ARXIV-2605-17292:start -->
<!-- existing:SF-2026-ARXIV-2605-17292:start -->独立 reviewer 顺读 `books/part-07-agent/82-multi-agent.md` 与相邻章节 ['books/part-07-agent/81-workflow.md', 'books/part-07-agent/83-mcp.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=948a0d2dac39b1e241adb0b692a057f0b8ef5411dda794e210d733cba06fa3d3。<!-- existing:SF-2026-ARXIV-2605-17292:end -->
<!-- delta:SF-2026-ARXIV-2605-17292:start -->delegation consumes a capability profile and confidence sensor, but self-reported confidence cannot own commit authority<!-- delta:SF-2026-ARXIV-2605-17292:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17292:end -->

<!-- books-review:SF-2026-ARXIV-2605-17301:start -->
<!-- existing:SF-2026-ARXIV-2605-17301:start -->独立 reviewer 顺读 `books/part-07-agent/76-rag.md` 与相邻章节 ['books/part-07-agent/75-context.md', 'books/part-07-agent/77-memory.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=3986f4307ffd57af8ace87d5c720982b992e07f247a91b16d73a39d83a8917a2。<!-- existing:SF-2026-ARXIV-2605-17301:end -->
<!-- delta:SF-2026-ARXIV-2605-17301:start -->RAG 在生成前显式检测、分类并解决 retrieved-source conflict；source credibility 与 temporal/opinion policy 变成可审计状态，但 LLM judge 与合成冲突数据限制外推。<!-- delta:SF-2026-ARXIV-2605-17301:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17301:end -->

<!-- books-review:SF-2026-ARXIV-2605-17304:start -->
<!-- existing:SF-2026-ARXIV-2605-17304:start -->独立 reviewer 顺读 `books/part-07-agent/75-context.md` 与相邻章节 ['books/part-07-agent/74-prompt.md', 'books/part-07-agent/76-rag.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=dcfe0b447383d99f4a06e25113b952af345025eaccbae7b73223e12444fe9ba6。<!-- existing:SF-2026-ARXIV-2605-17304:end -->
<!-- delta:SF-2026-ARXIV-2605-17304:start -->Context compression 的对象从 token 变为 typed, source-grounded commitment atoms；压缩必须验证 critical recall、conflict/equivalence 与 recoverability，并在不确定时回退 raw spans/更大 context。<!-- delta:SF-2026-ARXIV-2605-17304:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17304:end -->

<!-- books-review:SF-2026-ARXIV-2605-17305:start -->
<!-- existing:SF-2026-ARXIV-2605-17305:start -->独立 reviewer 顺读 `books/part-07-agent/80-reflection.md` 与相邻章节 ['books/part-07-agent/79-planning.md', 'books/part-07-agent/81-workflow.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=c1293a34a41ce0c0ee8d27ebdb10d68cada38430db2d77545ddb7873abd6fe08。<!-- existing:SF-2026-ARXIV-2605-17305:end -->
<!-- delta:SF-2026-ARXIV-2605-17305:start -->self-correction is represented as detector-controller-stop state with overshoot and oscillation, not an unbounded retry loop<!-- delta:SF-2026-ARXIV-2605-17305:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17305:end -->

<!-- books-review:SF-2026-ARXIV-2605-17320:start -->
<!-- existing:SF-2026-ARXIV-2605-17320:start -->独立 reviewer 顺读 `books/part-07-agent/84-agent-platform.md` 与相邻章节 ['books/part-07-agent/83-mcp.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=c90613b1e2cab33b382c0cff6ae0226e44b2d66b051e12a15174eae9c5fc6cdc。<!-- existing:SF-2026-ARXIV-2605-17320:end -->
<!-- delta:SF-2026-ARXIV-2605-17320:start -->Computer-use workspace 从一次性 sandbox 演进为 live save/fork/rollback/selective-commit；低延迟 branch 与 durable checkpoint 分权，同时引入 credential、GUI、external side-effect merge 边界。<!-- delta:SF-2026-ARXIV-2605-17320:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17320:end -->

<!-- books-review:SF-2026-ARXIV-2605-17324:start -->
<!-- existing:SF-2026-ARXIV-2605-17324:start -->独立 reviewer 顺读 `books/part-06-ai-infrastructure/72-security.md` 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']。当前正文已覆盖一般机制；本项仍留下不可被现有论证替代的状态/控制/证据增量。 owner_sha256=b4a3cdb8a1a37d72b85afa4def5d2fd3756d9432a2a7ddd0c60732f5bdbf9c1d。<!-- existing:SF-2026-ARXIV-2605-17324:end -->
<!-- delta:SF-2026-ARXIV-2605-17324:start -->Clarification 是独立 agent state transition，可能把 prompt injection 从 tool-return path 扩展到后续 user-input path；clarify 不能自动提升输入 authority。<!-- delta:SF-2026-ARXIV-2605-17324:end --> Decision=`Integrate`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17324:end -->

<!-- books-review:SF-2026-ARXIV-2605-17329:start -->
<!-- existing:SF-2026-ARXIV-2605-17329:start -->独立 reviewer 顺读 `books/part-06-ai-infrastructure/72-security.md` 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=b4a3cdb8a1a37d72b85afa4def5d2fd3756d9432a2a7ddd0c60732f5bdbf9c1d。<!-- existing:SF-2026-ARXIV-2605-17329:end -->
<!-- delta:SF-2026-ARXIV-2605-17329:start -->dynamic policy clauses are inference-time guardrail state; latent compression saves latency but remains a fallible sensor<!-- delta:SF-2026-ARXIV-2605-17329:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17329:end -->

<!-- books-review:SF-2026-ARXIV-2605-17348:start -->
<!-- existing:SF-2026-ARXIV-2605-17348:start -->独立 reviewer 顺读 `books/part-07-agent/82-multi-agent.md` 与相邻章节 ['books/part-07-agent/81-workflow.md', 'books/part-07-agent/83-mcp.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=948a0d2dac39b1e241adb0b692a057f0b8ef5411dda794e210d733cba06fa3d3。<!-- existing:SF-2026-ARXIV-2605-17348:end -->
<!-- delta:SF-2026-ARXIV-2605-17348:start -->Active/Standby/Terminated is a recoverable agent lifecycle that avoids irreversible pruning after one bad round<!-- delta:SF-2026-ARXIV-2605-17348:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17348:end -->

<!-- books-review:SF-2026-ARXIV-2605-17360:start -->
<!-- existing:SF-2026-ARXIV-2605-17360:start -->独立 reviewer 顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']。当前正文已覆盖一般机制；本项仍留下不可被现有论证替代的状态/控制/证据增量。 owner_sha256=6ef373ceb7416023b9a2ee18a9a6b6b920f2219bb2dae08748e4a6adc5a1febc。<!-- existing:SF-2026-ARXIV-2605-17360:end -->
<!-- delta:SF-2026-ARXIV-2605-17360:start -->duplex evaluation makes response timing and content alignment joint evidence instead of scoring only a completed offline answer<!-- delta:SF-2026-ARXIV-2605-17360:end --> Decision=`Integrate`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17360:end -->

<!-- books-review:SF-2026-ARXIV-2605-17373:start -->
<!-- existing:SF-2026-ARXIV-2605-17373:start -->独立 reviewer 顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=6ef373ceb7416023b9a2ee18a9a6b6b920f2219bb2dae08748e4a6adc5a1febc。<!-- existing:SF-2026-ARXIV-2605-17373:end -->
<!-- delta:SF-2026-ARXIV-2605-17373:start -->research-agent benchmarks must separate search policy from execution substrate and preserve process-level trajectory metrics<!-- delta:SF-2026-ARXIV-2605-17373:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17373:end -->

<!-- books-review:SF-2026-ARXIV-2605-17380:start -->
<!-- existing:SF-2026-ARXIV-2605-17380:start -->独立 reviewer 顺读 `books/part-06-ai-infrastructure/72-security.md` 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']。当前正文已覆盖一般机制；本项仍留下不可被现有论证替代的状态/控制/证据增量。 owner_sha256=b4a3cdb8a1a37d72b85afa4def5d2fd3756d9432a2a7ddd0c60732f5bdbf9c1d。<!-- existing:SF-2026-ARXIV-2605-17380:end -->
<!-- delta:SF-2026-ARXIV-2605-17380:start -->agent security needs prompt/tool/causal-chain telemetry plus cheap triage and contextual escalation, not file events alone<!-- delta:SF-2026-ARXIV-2605-17380:end --> Decision=`Integrate`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17380:end -->

<!-- books-review:SF-2026-ARXIV-2605-17415:start -->
<!-- existing:SF-2026-ARXIV-2605-17415:start -->独立 reviewer 顺读 `books/part-07-agent/76-rag.md` 与相邻章节 ['books/part-07-agent/75-context.md', 'books/part-07-agent/77-memory.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=3986f4307ffd57af8ace87d5c720982b992e07f247a91b16d73a39d83a8917a2。<!-- existing:SF-2026-ARXIV-2605-17415:end -->
<!-- delta:SF-2026-ARXIV-2605-17415:start -->streaming ANN requires an explicit coarse-index refresh owner and bounded stale-assignment fallback<!-- delta:SF-2026-ARXIV-2605-17415:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17415:end -->

<!-- books-review:SF-2026-ARXIV-2605-17439:start -->
<!-- existing:SF-2026-ARXIV-2605-17439:start -->独立 reviewer 顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=6ef373ceb7416023b9a2ee18a9a6b6b920f2219bb2dae08748e4a6adc5a1febc。<!-- existing:SF-2026-ARXIV-2605-17439:end -->
<!-- delta:SF-2026-ARXIV-2605-17439:start -->GUI-agent evaluation separates outcome scoring from failure localization and counterfactual diagnosis<!-- delta:SF-2026-ARXIV-2605-17439:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17439:end -->

<!-- books-review:SF-2026-ARXIV-2605-17453:start -->
<!-- existing:SF-2026-ARXIV-2605-17453:start -->独立 reviewer 顺读 `books/part-07-agent/78-tool-calling.md` 与相邻章节 ['books/part-07-agent/77-memory.md', 'books/part-07-agent/79-planning.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=c0020f56aeee2c8008004dd34f27ed47f49f190f17a43909a885ce972a2a41d4。<!-- existing:SF-2026-ARXIV-2605-17453:end -->
<!-- delta:SF-2026-ARXIV-2605-17453:start -->工具在探索期积累可信反馈、到隐藏状态满足时才毒化最终 action；final-action guard 必须对 trajectory-derived environment variables 做风险审查，单次 tool selection 不足。<!-- delta:SF-2026-ARXIV-2605-17453:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17453:end -->

<!-- books-review:SF-2026-ARXIV-2605-17467:start -->
<!-- existing:SF-2026-ARXIV-2605-17467:start -->独立 reviewer 顺读 `books/part-07-agent/82-multi-agent.md` 与相邻章节 ['books/part-07-agent/81-workflow.md', 'books/part-07-agent/83-mcp.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=948a0d2dac39b1e241adb0b692a057f0b8ef5411dda794e210d733cba06fa3d3。<!-- existing:SF-2026-ARXIV-2605-17467:end -->
<!-- delta:SF-2026-ARXIV-2605-17467:start -->multi-agent verification assigns claims and evidence to agents so disagreement is attributable rather than pooled<!-- delta:SF-2026-ARXIV-2605-17467:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17467:end -->

<!-- books-review:SF-2026-ARXIV-2605-17471:start -->
<!-- existing:SF-2026-ARXIV-2605-17471:start -->独立 reviewer 顺读 `books/part-04-training-system/28-pretraining.md` 与相邻章节 ['books/part-04-training-system/27-data.md', 'books/part-04-training-system/29-sft.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=0eca9f709aa5037490fd8ccf36118c63b0a7a18c7abb5e68100e8b89473faf65。<!-- existing:SF-2026-ARXIV-2605-17471:end -->
<!-- delta:SF-2026-ARXIV-2605-17471:start -->quantization-aware training changes loss geometry and convergence assumptions; deployment speedup still depends on compatible kernels<!-- delta:SF-2026-ARXIV-2605-17471:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17471:end -->

<!-- books-review:SF-2026-ARXIV-2605-17480:start -->
<!-- existing:SF-2026-ARXIV-2605-17480:start -->独立 reviewer 顺读 `books/part-06-ai-infrastructure/72-security.md` 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=b4a3cdb8a1a37d72b85afa4def5d2fd3756d9432a2a7ddd0c60732f5bdbf9c1d。<!-- existing:SF-2026-ARXIV-2605-17480:end -->
<!-- delta:SF-2026-ARXIV-2605-17480:start -->更强 Worker 可能以更确定语言把 semantic hijacking 传给 Manager；capability/certainty 不能替代 independent evidence，跨 Agent commit 需要来源与反证门。<!-- delta:SF-2026-ARXIV-2605-17480:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17480:end -->

<!-- books-review:SF-2026-ARXIV-2605-17497:start -->
<!-- existing:SF-2026-ARXIV-2605-17497:start -->独立 reviewer 顺读 `books/part-04-training-system/33-grpo.md` 与相邻章节 ['books/part-04-training-system/32-ppo.md', 'books/part-04-training-system/34-dpo.md']。当前正文已覆盖一般机制；本项仍留下不可被现有论证替代的状态/控制/证据增量。 owner_sha256=c75d66bc18a9221e70da0fc29018962765e69241af2ce0959becf0ab5f8e49a8。<!-- existing:SF-2026-ARXIV-2605-17497:end -->
<!-- delta:SF-2026-ARXIV-2605-17497:start -->teacher signals are generated on the learner's current rollout distribution, trading stale offline supervision for online sampling cost<!-- delta:SF-2026-ARXIV-2605-17497:end --> Decision=`Integrate`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17497:end -->

<!-- books-review:SF-2026-ARXIV-2605-17508:start -->
<!-- existing:SF-2026-ARXIV-2605-17508:start -->独立 reviewer 顺读 `books/part-04-training-system/36-distributed-training.md` 与相邻章节 ['books/part-04-training-system/35-checkpoint.md', 'books/part-04-training-system/37-tensor-parallel.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=c940481ca012303f984917615764a048e4a6742978fcb826524402093905481b。<!-- existing:SF-2026-ARXIV-2605-17508:end -->
<!-- delta:SF-2026-ARXIV-2605-17508:start -->split federated execution moves activation and optimizer state across a trust/network boundary but remains tied to the disclosed edge workload<!-- delta:SF-2026-ARXIV-2605-17508:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17508:end -->

<!-- books-review:SF-2026-ARXIV-2605-17522:start -->
<!-- existing:SF-2026-ARXIV-2605-17522:start -->独立 reviewer 顺读 `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 与相邻章节 ['books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md', 'books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=e3eb726b0a302cf0dd2994ec6c50e1f6615e7bfee81edf9ca9bdbff7c78a6325。<!-- existing:SF-2026-ARXIV-2605-17522:end -->
<!-- delta:SF-2026-ARXIV-2605-17522:start -->closed-loop world-model evaluation must bind action conditioning, rollout state and downstream control outcome<!-- delta:SF-2026-ARXIV-2605-17522:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17522:end -->

<!-- books-review:SF-2026-ARXIV-2605-17554:start -->
<!-- existing:SF-2026-ARXIV-2605-17554:start -->独立 reviewer 顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=6ef373ceb7416023b9a2ee18a9a6b6b920f2219bb2dae08748e4a6adc5a1febc。<!-- existing:SF-2026-ARXIV-2605-17554:end -->
<!-- delta:SF-2026-ARXIV-2605-17554:start -->deep-research evaluation preserves search process, evidence use and final artifact as distinct measurement planes<!-- delta:SF-2026-ARXIV-2605-17554:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17554:end -->

<!-- books-review:SF-2026-ARXIV-2605-17558:start -->
<!-- existing:SF-2026-ARXIV-2605-17558:start -->独立 reviewer 顺读 `books/part-07-agent/78-tool-calling.md` 与相邻章节 ['books/part-07-agent/77-memory.md', 'books/part-07-agent/79-planning.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=c0020f56aeee2c8008004dd34f27ed47f49f190f17a43909a885ce972a2a41d4。<!-- existing:SF-2026-ARXIV-2605-17558:end -->
<!-- delta:SF-2026-ARXIV-2605-17558:start -->tool-call training data is admitted only after executable verification and typed failure closure<!-- delta:SF-2026-ARXIV-2605-17558:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17558:end -->

<!-- books-review:SF-2026-ARXIV-2605-17570:start -->
<!-- existing:SF-2026-ARXIV-2605-17570:start -->独立 reviewer 顺读 `books/part-04-training-system/33-grpo.md` 与相邻章节 ['books/part-04-training-system/32-ppo.md', 'books/part-04-training-system/34-dpo.md']。当前正文已覆盖一般机制；本项仍留下不可被现有论证替代的状态/控制/证据增量。 owner_sha256=c75d66bc18a9221e70da0fc29018962765e69241af2ce0959becf0ab5f8e49a8。<!-- existing:SF-2026-ARXIV-2605-17570:end -->
<!-- delta:SF-2026-ARXIV-2605-17570:start -->asynchronous RL must account for policy-version staleness in advantage updates rather than treating every rollout as current<!-- delta:SF-2026-ARXIV-2605-17570:end --> Decision=`Integrate`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17570:end -->

<!-- books-review:SF-2026-ARXIV-2605-17590:start -->
<!-- existing:SF-2026-ARXIV-2605-17590:start -->独立 reviewer 顺读 `books/part-04-training-system/27-data.md` 与相邻章节 ['books/part-04-training-system/28-pretraining.md']。当前正文已覆盖一般机制；本项仍留下不可被现有论证替代的状态/控制/证据增量。 owner_sha256=8e594c3827c4a7778945dbe71f0c1af1ca4089918dcd0c8998ff54d98ac664a1。<!-- existing:SF-2026-ARXIV-2605-17590:end -->
<!-- delta:SF-2026-ARXIV-2605-17590:start -->Machine unlearning 的目标不是只校正参数，而是对齐删除编辑后的 counterfactual optimizer state，包括 L-BFGS memory operator 与下一步 update direction。<!-- delta:SF-2026-ARXIV-2605-17590:end --> Decision=`Integrate`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17590:end -->

<!-- books-review:SF-2026-ARXIV-2605-17609:start -->
<!-- existing:SF-2026-ARXIV-2605-17609:start -->独立 reviewer 顺读 `books/part-05-inference-system/56-inference-scheduling.md` 与相邻章节 ['books/part-05-inference-system/55-pd-disaggregation.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=1e3e8c3dff17a6bd79b65130176926b9f10cb1e2ff5bf3e042d4ccee6c302280。<!-- existing:SF-2026-ARXIV-2605-17609:end -->
<!-- delta:SF-2026-ARXIV-2605-17609:start -->test-time compute allocation jointly owns generation count, rank signal, verifier budget and stopping under an explicit monotonicity assumption<!-- delta:SF-2026-ARXIV-2605-17609:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17609:end -->

<!-- books-review:SF-2026-ARXIV-2605-17610:start -->
<!-- existing:SF-2026-ARXIV-2605-17610:start -->独立 reviewer 顺读 `books/part-06-ai-infrastructure/72-security.md` 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=b4a3cdb8a1a37d72b85afa4def5d2fd3756d9432a2a7ddd0c60732f5bdbf9c1d。<!-- existing:SF-2026-ARXIV-2605-17610:end -->
<!-- delta:SF-2026-ARXIV-2605-17610:start -->fast/slow video moderation routes only uncertain temporal cases to deliberation while preserving a conservative safety fallback<!-- delta:SF-2026-ARXIV-2605-17610:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17610:end -->

<!-- books-review:SF-2026-ARXIV-2605-17613:start -->
<!-- existing:SF-2026-ARXIV-2605-17613:start -->独立 reviewer 顺读 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 与相邻章节 ['books/part-05-inference-system/44-decode.md', 'books/part-05-inference-system/46-continuous-batching.md']。当前正文已覆盖一般机制；本项仍留下不可被现有论证替代的状态/控制/证据增量。 owner_sha256=94425d5fe4db0238e99350a5a0299edb408dcffcdb7b32453c76854a9dbc8e86。<!-- existing:SF-2026-ARXIV-2605-17613:end -->
<!-- delta:SF-2026-ARXIV-2605-17613:start -->有损 KV 只作为 draft，full KV 被保留到慢层并拥有最终 verification/commit；换取 lossless output 的代价是 full-state tier、swap/prefetch 与验证失败回退。<!-- delta:SF-2026-ARXIV-2605-17613:end --> Decision=`Integrate`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17613:end -->

<!-- books-review:SF-2026-ARXIV-2605-17617:start -->
<!-- existing:SF-2026-ARXIV-2605-17617:start -->独立 reviewer 顺读 `books/part-07-agent/81-workflow.md` 与相邻章节 ['books/part-07-agent/80-reflection.md', 'books/part-07-agent/82-multi-agent.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=6e71a861a0983658675a17c274f4899af49cf05cf91646a8a52289bd724fd6ab。<!-- existing:SF-2026-ARXIV-2605-17617:end -->
<!-- delta:SF-2026-ARXIV-2605-17617:start -->operational traces become versioned workflow graphs whose online traversal and reinforcement need separate owners<!-- delta:SF-2026-ARXIV-2605-17617:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17617:end -->

<!-- books-review:SF-2026-ARXIV-2605-17625:start -->
<!-- existing:SF-2026-ARXIV-2605-17625:start -->独立 reviewer 顺读 `books/part-07-agent/77-memory.md` 与相邻章节 ['books/part-07-agent/76-rag.md', 'books/part-07-agent/78-tool-calling.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=c6d90ee41a0332b99f4f0a78dc25c6253eb7c7cb12b4bb3769360926879e8751。<!-- existing:SF-2026-ARXIV-2605-17625:end -->
<!-- delta:SF-2026-ARXIV-2605-17625:start -->episodic window and semantic consolidation are separate memory states; consolidation quality, contradiction and growth are explicit failure modes<!-- delta:SF-2026-ARXIV-2605-17625:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17625:end -->

<!-- books-review:SF-2026-ARXIV-2605-17634:start -->
<!-- existing:SF-2026-ARXIV-2605-17634:start -->独立 reviewer 顺读 `books/part-06-ai-infrastructure/72-security.md` 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=b4a3cdb8a1a37d72b85afa4def5d2fd3756d9432a2a7ddd0c60732f5bdbf9c1d。<!-- existing:SF-2026-ARXIV-2605-17634:end -->
<!-- delta:SF-2026-ARXIV-2605-17634:start -->Prompt injection 不可仅靠 data/instruction separation 完全解决；Contextual Integrity 显示 norm manipulation/mixed flows 的不可判定边界，最终 authority 必须由 capability policy/approval 持有。<!-- delta:SF-2026-ARXIV-2605-17634:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17634:end -->

<!-- books-review:SF-2026-ARXIV-2605-17641:start -->
<!-- existing:SF-2026-ARXIV-2605-17641:start -->独立 reviewer 顺读 `books/part-07-agent/77-memory.md` 与相邻章节 ['books/part-07-agent/76-rag.md', 'books/part-07-agent/78-tool-calling.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=c6d90ee41a0332b99f4f0a78dc25c6253eb7c7cb12b4bb3769360926879e8751。<!-- existing:SF-2026-ARXIV-2605-17641:end -->
<!-- delta:SF-2026-ARXIV-2605-17641:start -->Memory selection 从 semantic similarity 演进为 controlled causal interventions；收益依赖 intervention/judge validity，计算成本和 distribution shift 要求保留普通 retrieval fallback。<!-- delta:SF-2026-ARXIV-2605-17641:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17641:end -->

<!-- books-review:SF-2026-ARXIV-2605-17659:start -->
<!-- existing:SF-2026-ARXIV-2605-17659:start -->独立 reviewer 顺读 `books/part-04-training-system/28-pretraining.md` 与相邻章节 ['books/part-04-training-system/27-data.md', 'books/part-04-training-system/29-sft.md']。当前正文已覆盖一般机制；本项仍留下不可被现有论证替代的状态/控制/证据增量。 owner_sha256=0eca9f709aa5037490fd8ccf36118c63b0a7a18c7abb5e68100e8b89473faf65。<!-- existing:SF-2026-ARXIV-2605-17659:end -->
<!-- delta:SF-2026-ARXIV-2605-17659:start -->正偏激活与标准 loss 在初始化产生 negative weight drift，进而形成 activation sparsity/spikes；这是 optimizer–activation coupling，不是单纯数据性质或默认正则收益。<!-- delta:SF-2026-ARXIV-2605-17659:end --> Decision=`Integrate`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17659:end -->

<!-- books-review:SF-2026-ARXIV-2605-17672:start -->
<!-- existing:SF-2026-ARXIV-2605-17672:start -->独立 reviewer 顺读 `books/part-05-inference-system/56-inference-scheduling.md` 与相邻章节 ['books/part-05-inference-system/55-pd-disaggregation.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=1e3e8c3dff17a6bd79b65130176926b9f10cb1e2ff5bf3e042d4ccee6c302280。<!-- existing:SF-2026-ARXIV-2605-17672:end -->
<!-- delta:SF-2026-ARXIV-2605-17672:start -->Reasoning early exit 应检测 successive-step semantic convergence，而非只看 answer confidence；节省 token 的代价是 embedding/judge 开销与 premature-stop failure。<!-- delta:SF-2026-ARXIV-2605-17672:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17672:end -->

<!-- books-review:SF-2026-ARXIV-2605-17683:start -->
<!-- existing:SF-2026-ARXIV-2605-17683:start -->独立 reviewer 顺读 `books/part-05-inference-system/49-tensorrt-llm.md` 与相邻章节 ['books/part-05-inference-system/48-speculative-decoding.md', 'books/part-05-inference-system/50-vllm.md']。当前正文已覆盖一般机制；本项仍留下不可被现有论证替代的状态/控制/证据增量。 owner_sha256=8ee7425b911361c8e1e632272a759a2ae9eb63723aeb30c1237bc304ce07fb7b。<!-- existing:SF-2026-ARXIV-2605-17683:end -->
<!-- delta:SF-2026-ARXIV-2605-17683:start -->microsecond inference requires overhead-aware execution planning across direct inter-layer links, synchronization and non-matmul operators<!-- delta:SF-2026-ARXIV-2605-17683:end --> Decision=`Integrate`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17683:end -->

<!-- books-review:SF-2026-ARXIV-2605-17707:start -->
<!-- existing:SF-2026-ARXIV-2605-17707:start -->独立 reviewer 顺读 `books/part-06-ai-infrastructure/72-security.md` 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']。当前正文已覆盖一般机制；本项仍留下不可被现有论证替代的状态/控制/证据增量。 owner_sha256=b4a3cdb8a1a37d72b85afa4def5d2fd3756d9432a2a7ddd0c60732f5bdbf9c1d。<!-- existing:SF-2026-ARXIV-2605-17707:end -->
<!-- delta:SF-2026-ARXIV-2605-17707:start -->Edge AI accelerator 绕过 OS 语义隔离时可能成为 confused deputy；DMA/地址/权限验证必须进入 accelerator–driver contract，而不是只相信应用进程边界。<!-- delta:SF-2026-ARXIV-2605-17707:end --> Decision=`Integrate`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17707:end -->

<!-- books-review:SF-2026-ARXIV-2605-17721:start -->
<!-- existing:SF-2026-ARXIV-2605-17721:start -->独立 reviewer 顺读 `books/part-07-agent/77-memory.md` 与相邻章节 ['books/part-07-agent/76-rag.md', 'books/part-07-agent/78-tool-calling.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=c6d90ee41a0332b99f4f0a78dc25c6253eb7c7cb12b4bb3769360926879e8751。<!-- existing:SF-2026-ARXIV-2605-17721:end -->
<!-- delta:SF-2026-ARXIV-2605-17721:start -->Self-evolving Agent 把成功/失败经验组织为 online/offline experience graph；结构化复用提高可用性，同时带来 provenance、staleness、错误传播与 graph lifecycle 成本。<!-- delta:SF-2026-ARXIV-2605-17721:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17721:end -->

<!-- books-review:SF-2026-ARXIV-2605-17734:start -->
<!-- existing:SF-2026-ARXIV-2605-17734:start -->已顺读 `books/part-07-agent/84-agent-platform.md` 与相邻章节 ['books/part-07-agent/83-mcp.md']；正文主线 headings=['本章要回答的问题', 'Agent 改变了平台的控制对象', 'Serving 结束不等于 Agent 任务结束', 'Agent Definition 与 Run Identity', '可复用 Skill 不是一个 Prompt 文件', '从 Skill Catalog 到 Competence-aware Orchestration', '从 Trajectory 到 Skill 是一次受治理的 Compilation', 'Skill Compiler 必须绑定 Target Profile，而不是只绑定模型名', 'Self-evolution Admission 需要 Anytime-valid Acceptor', 'Workspace 是长期行动的隔离单元']。<!-- existing:SF-2026-ARXIV-2605-17734:end -->
<!-- delta:SF-2026-ARXIV-2605-17734:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-17734:end -->
<!-- books-review:SF-2026-ARXIV-2605-17734:end -->

<!-- books-review:SF-2026-ARXIV-2605-17757:start -->
<!-- existing:SF-2026-ARXIV-2605-17757:start -->已顺读 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 与相邻章节 ['books/part-05-inference-system/44-decode.md', 'books/part-05-inference-system/46-continuous-batching.md']；正文主线 headings=['本章要回答的问题', '如果完全不缓存', '为什么缓存 K/V 而不是 Query', '逻辑 Shape 与容量公式', '一个容量小例子', 'KV Cache 的生命周期', 'Segmented Execution 必须在训练与推理共享同一语义', 'Prefix reuse', 'KV 从生成私有状态演进为受约束的下游读出接口', 'Structured knowledge 只有进入 physical access plan 才改变 KV 成本']。<!-- existing:SF-2026-ARXIV-2605-17757:end -->
<!-- delta:SF-2026-ARXIV-2605-17757:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-17757:end -->
<!-- books-review:SF-2026-ARXIV-2605-17757:end -->

<!-- books-review:SF-2026-ARXIV-2605-17787:start -->
<!-- existing:SF-2026-ARXIV-2605-17787:start -->已顺读 `books/part-04-training-system/28-pretraining.md` 与相邻章节 ['books/part-04-training-system/27-data.md', 'books/part-04-training-system/29-sft.md']；正文主线 headings=['本章要回答的问题', '从随机参数开始会发生什么', 'Next-token objective', '一个 token loss 小例子', 'Perplexity 能回答什么', '一次 training step 的状态流', 'Residual Path 也可以成为随 Depth 与 Time 演化的训练状态', 'Optimizer 不是与参数化无关的旋钮', 'Optimizer State Allocation 也应服从参数角色', 'Batch、tokens 与 optimizer steps 不是同一计量']。<!-- existing:SF-2026-ARXIV-2605-17787:end -->
<!-- delta:SF-2026-ARXIV-2605-17787:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-17787:end -->
<!-- books-review:SF-2026-ARXIV-2605-17787:end -->

<!-- books-review:SF-2026-ARXIV-2605-17821:start -->
<!-- existing:SF-2026-ARXIV-2605-17821:start -->已顺读 `books/part-04-training-system/35-checkpoint.md` 与相邻章节 ['books/part-04-training-system/34-dpo.md', 'books/part-04-training-system/36-distributed-training.md']；正文主线 headings=['本章要回答的问题', '为什么只保存 Weights 不够', '一个完整训练状态清单', 'Checkpoint Size 为什么远大于模型文件', '一致性首先是 Step 边界', 'Checkpoint 应像事务一样提交', '分布式 Sharded Checkpoint', 'Resharding 为什么比 Load 更难', 'Data Cursor 为什么必须保存', 'RNG State 为什么影响可复现性']。<!-- existing:SF-2026-ARXIV-2605-17821:end -->
<!-- delta:SF-2026-ARXIV-2605-17821:start -->当前 checkpoint 章有完整/增量 checkpoint 与异步保存，但没有按 failure blast radius 把 local/peer/remote recovery tier 变成同一 durability policy；保留为写回增量。<!-- delta:SF-2026-ARXIV-2605-17821:end -->
<!-- books-review:SF-2026-ARXIV-2605-17821:end -->

<!-- books-review:SF-2026-ARXIV-2605-17830:start -->
<!-- existing:SF-2026-ARXIV-2605-17830:start -->已顺读 `books/part-07-agent/77-memory.md` 与相邻章节 ['books/part-07-agent/76-rag.md', 'books/part-07-agent/78-tool-calling.md']；正文主线 headings=['本章要回答的问题', 'Context 与 Memory 的状态边界', 'Memory 类型是用途，不只是存储介质', 'Memory Write 是高风险决策', 'Write / Hold 不足以定义下一状态', '从 Outcome Reward 到 Content-level Credit：归因只能约束写入，不能成为真值', 'Memory Read 是受约束检索', '从按需读取到选择性主动干预', '从一次 Top-k 检索到有预算的关联回忆', 'Fact State 与 Retrieval-policy State 必须分离']。<!-- existing:SF-2026-ARXIV-2605-17830:end -->
<!-- delta:SF-2026-ARXIV-2605-17830:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-17830:end -->
<!-- books-review:SF-2026-ARXIV-2605-17830:end -->

<!-- books-review:SF-2026-ARXIV-2605-17842:start -->
<!-- existing:SF-2026-ARXIV-2605-17842:start -->已顺读 `books/part-05-inference-system/49-tensorrt-llm.md` 与相邻章节 ['books/part-05-inference-system/48-speculative-decoding.md', 'books/part-05-inference-system/50-vllm.md']；正文主线 headings=['本章要回答的问题', '从计算图开始', '三类基础优化', 'Execution Plan 可以修订，但只能在安全边界 Commit', '异步工作不必永久绑定固定 Physical Core', '从粗粒度 Offload 到负载观测的 Tensor Placement', 'Backend Choice 必须携带 Previous-backend State', 'Accelerator Readiness 是 Phase × Shape × Offload × Host-control Contract', '从 Linear 语义到 GEMM 执行', '两种稀疏性必须共享地址合同，却不必共享 Kernel']。<!-- existing:SF-2026-ARXIV-2605-17842:end -->
<!-- delta:SF-2026-ARXIV-2605-17842:start -->当前推理执行章覆盖 tensor/pipeline/kernel 并行，但没有把层序列改写为 residual root finding 后并行 correction 的实验分支；保留为受限机制。<!-- delta:SF-2026-ARXIV-2605-17842:end -->
<!-- books-review:SF-2026-ARXIV-2605-17842:end -->

<!-- books-review:SF-2026-ARXIV-2605-17849:start -->
<!-- existing:SF-2026-ARXIV-2605-17849:start -->已顺读 `books/part-04-training-system/27-data.md` 与相邻章节 ['books/part-04-training-system/28-pretraining.md']；正文主线 headings=['本章要回答的问题', 'Part IV 的能力生产链', '先从“把互联网都抓下来”开始', 'Collection protocol 为什么先于 Filtering 定义数据', '数据分布就是优化权重', '静态 Mixture 到版本化 Data Control Plane', '一个三域配比小例子', 'Data tags 也可能训练一条隐式控制策略', 'Quality filtering 在过滤什么', 'Synthetic data：从“先生成再打分”到 Specification Compilation']。<!-- existing:SF-2026-ARXIV-2605-17849:end -->
<!-- delta:SF-2026-ARXIV-2605-17849:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-17849:end -->
<!-- books-review:SF-2026-ARXIV-2605-17849:end -->

<!-- books-review:SF-2026-ARXIV-2605-17862:start -->
<!-- existing:SF-2026-ARXIV-2605-17862:start -->已顺读 `books/part-04-training-system/31-rlhf.md` 与相邻章节 ['books/part-04-training-system/30-lora.md', 'books/part-04-training-system/32-ppo.md']；正文主线 headings=['本章要回答的问题', 'Demonstration 为什么不足以表达偏好', 'RLHF 的完整 pipeline', 'Reward Model 怎样学习相对判断', '一个 preference score 小例子', 'Preference data 的难点不只是数量', '从 Reward 到 Policy objective', '改变输出分布是目标，不是无副作用的偏好标签', "Reward hacking 与 Goodhart's Law", 'Sequence reward 与 token updates 的错位']。<!-- existing:SF-2026-ARXIV-2605-17862:end -->
<!-- delta:SF-2026-ARXIV-2605-17862:start -->当前 post-training 章有 policy version/freshness，但未同时分解 rollout drift 与 supervision drift 并以 freshness controller 控制异步 OPD；保留为写回增量。<!-- delta:SF-2026-ARXIV-2605-17862:end -->
<!-- books-review:SF-2026-ARXIV-2605-17862:end -->

<!-- books-review:SF-2026-ARXIV-2605-17877:start -->
<!-- existing:SF-2026-ARXIV-2605-17877:start -->已顺读 `books/part-04-training-system/31-rlhf.md` 与相邻章节 ['books/part-04-training-system/30-lora.md', 'books/part-04-training-system/32-ppo.md']；正文主线 headings=['本章要回答的问题', 'Demonstration 为什么不足以表达偏好', 'RLHF 的完整 pipeline', 'Reward Model 怎样学习相对判断', '一个 preference score 小例子', 'Preference data 的难点不只是数量', '从 Reward 到 Policy objective', '改变输出分布是目标，不是无副作用的偏好标签', "Reward hacking 与 Goodhart's Law", 'Sequence reward 与 token updates 的错位']。<!-- existing:SF-2026-ARXIV-2605-17877:end -->
<!-- delta:SF-2026-ARXIV-2605-17877:start -->当前 RLHF 章讨论 outcome/step reward 与 verifier，但没有把不可控 prefix contamination 从当前 action 的 dense credit 中分离；保留为写回增量。<!-- delta:SF-2026-ARXIV-2605-17877:end -->
<!-- books-review:SF-2026-ARXIV-2605-17877:end -->

<!-- books-review:SF-2026-ARXIV-2605-17879:start -->
<!-- existing:SF-2026-ARXIV-2605-17879:start -->已顺读 `books/part-06-ai-infrastructure/67-monitoring.md` 与相邻章节 ['books/part-06-ai-infrastructure/66-evaluation-system.md', 'books/part-06-ai-infrastructure/68-logging.md']；正文主线 headings=['本章要回答的问题', '先定义目标，再选择可测信号', 'Context generator 是 pre-failure sensor identity 的一部分', 'Review notes', '四层指标', 'Autonomy 不是一个纯模型指标', '从单次 Query 指标到 Session-level Search Trajectory Sensor', 'Rate、Errors、Duration 与 Saturation', '从 Error Counter 到 Layer × Detectability Failure Coordinate', '平均值为什么危险']。<!-- existing:SF-2026-ARXIV-2605-17879:end -->
<!-- delta:SF-2026-ARXIV-2605-17879:start -->当前 monitoring/training 章节缺少在线低开销 fail-slow signal 与离线节点资格复验的分权闭环；保留为写回增量。<!-- delta:SF-2026-ARXIV-2605-17879:end -->
<!-- books-review:SF-2026-ARXIV-2605-17879:end -->

<!-- books-review:SF-2026-ARXIV-2605-17889:start -->
<!-- existing:SF-2026-ARXIV-2605-17889:start -->已顺读 `books/part-05-inference-system/49-tensorrt-llm.md` 与相邻章节 ['books/part-05-inference-system/48-speculative-decoding.md', 'books/part-05-inference-system/50-vllm.md']；正文主线 headings=['本章要回答的问题', '从计算图开始', '三类基础优化', 'Execution Plan 可以修订，但只能在安全边界 Commit', '异步工作不必永久绑定固定 Physical Core', '从粗粒度 Offload 到负载观测的 Tensor Placement', 'Backend Choice 必须携带 Previous-backend State', 'Accelerator Readiness 是 Phase × Shape × Offload × Host-control Contract', '从 Linear 语义到 GEMM 执行', '两种稀疏性必须共享地址合同，却不必共享 Kernel']。<!-- existing:SF-2026-ARXIV-2605-17889:end -->
<!-- delta:SF-2026-ARXIV-2605-17889:start -->当前 MoE execution 章有 expert offload/placement，但缺少 CPU-GPU coalesced expert execution 对 micro-batch 与中间态搬运的统一控制；保留为写回增量。<!-- delta:SF-2026-ARXIV-2605-17889:end -->
<!-- books-review:SF-2026-ARXIV-2605-17889:end -->

<!-- books-review:SF-2026-ARXIV-2605-17912:start -->
<!-- existing:SF-2026-ARXIV-2605-17912:start -->已顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；正文主线 headings=['本章要回答的问题', '为什么“选一个分数”不是评估系统', 'HTTP 成功只是质量判断的第一道门', '从目标到证据，而不是从指标到目标', '第一个不变量：评估声明必须绑定完整对象', 'Evaluation Identity 必须包含 Harness 与 Environment', '第二个不变量：评估结论总是相对于分布', '平均值、切片与不确定性', '评估对象有四个层次', 'Model Evaluation']。<!-- existing:SF-2026-ARXIV-2605-17912:end -->
<!-- delta:SF-2026-ARXIV-2605-17912:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-17912:end -->
<!-- books-review:SF-2026-ARXIV-2605-17912:end -->

<!-- books-review:SF-2026-ARXIV-2605-17921:start -->
<!-- existing:SF-2026-ARXIV-2605-17921:start -->已顺读 `books/part-05-inference-system/56-inference-scheduling.md` 与相邻章节 ['books/part-05-inference-system/55-pd-disaggregation.md']；正文主线 headings=['本章要回答的问题', '调度对象从 request 变成 token state', '目标函数不止吞吐', 'SLO-aware Admission', '当前能放下，不等于未来可完成', '不确定输出长度下的 Future-state Reservation', '连续 Edge Inference 需要跨窗口携带 Violation-risk Budget', '从队列启发式到时间耦合的资源影子价格', 'Reasoning Budget 必须进入调度与评估身份', 'Inference-time Process Guidance 也是可调度资源']。<!-- existing:SF-2026-ARXIV-2605-17921:end -->
<!-- delta:SF-2026-ARXIV-2605-17921:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-17921:end -->
<!-- books-review:SF-2026-ARXIV-2605-17921:end -->

<!-- books-review:SF-2026-ARXIV-2605-17923:start -->
<!-- existing:SF-2026-ARXIV-2605-17923:start -->已顺读 `books/part-04-training-system/36-distributed-training.md` 与相邻章节 ['books/part-04-training-system/35-checkpoint.md', 'books/part-04-training-system/37-tensor-parallel.md']；正文主线 headings=['本章要回答的问题', '单卡为什么会失败', '从本机协作到分布式执行', '先分清五个通信层次', 'Collective 是群体语义，不是一种算法', '用 Alpha-Beta 模型建立下界直觉', 'Ring、Tree 与 Butterfly 在优化什么', 'MPI、NCCL、UCX、UCC 与 NIXL 的边界', 'Collective 进入计算图后，Completion 也成为 Autograd 语义', '从 Collective Call 到 Kernel 内 Remote Memory']。<!-- existing:SF-2026-ARXIV-2605-17923:end -->
<!-- delta:SF-2026-ARXIV-2605-17923:start -->当前分布式训练章讨论 packed/variable-length 调度，但没有把 video-DiT sequence 的 memory 与 compute 双约束一起冻结为 batch contract；保留为写回增量。<!-- delta:SF-2026-ARXIV-2605-17923:end -->
<!-- books-review:SF-2026-ARXIV-2605-17923:end -->

<!-- books-review:SF-2026-ARXIV-2605-17932:start -->
<!-- existing:SF-2026-ARXIV-2605-17932:start -->已顺读 `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md` 与相邻章节 ['books/part-03-multimodal-world-models/23-multimodal-representation.md', 'books/part-03-multimodal-world-models/25-multimodal-world-models.md']；正文主线 headings=['本章要回答的问题', '从一个共同问题开始', '为什么 Autoregressive 是合理起点', 'Diffusion：用迭代修正换并行状态更新', 'Masked generation：未知位置与已知位置', 'Editable tokens 与 commit boundary', 'Self-revision：并行位置必须在 Commit 前保持可撤销', '生成 Workflow 也可以被训练进 Intermediate State', 'Block Diffusion：局部自回归与块内并行', 'Draft、Verify 与 Correct 不是同一件事']。<!-- existing:SF-2026-ARXIV-2605-17932:end -->
<!-- delta:SF-2026-ARXIV-2605-17932:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-17932:end -->
<!-- books-review:SF-2026-ARXIV-2605-17932:end -->

<!-- books-review:SF-2026-ARXIV-2605-17954:start -->
<!-- existing:SF-2026-ARXIV-2605-17954:start -->已顺读 `books/part-03-multimodal-world-models/23-multimodal-representation.md` 与相邻章节 ['books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md']；正文主线 headings=['本章要回答的问题', '为什么文本 token 的经验不能直接复制', '一个思想实验：同样是 256 个 token', '表示演进：从专用特征到统一协议', '阶段一：手工特征与专用模型', '阶段二：modality-specific encoder + projector', '阶段三：共享 token space', '阶段四：native multimodal representation', '连续表示、离散表示与混合表示', '连续表示']。<!-- existing:SF-2026-ARXIV-2605-17954:end -->
<!-- delta:SF-2026-ARXIV-2605-17954:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-17954:end -->
<!-- books-review:SF-2026-ARXIV-2605-17954:end -->

<!-- books-review:SF-2026-ARXIV-2605-17986:start -->
<!-- existing:SF-2026-ARXIV-2605-17986:start -->已顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；正文主线 headings=['本章要回答的问题', '为什么“选一个分数”不是评估系统', 'HTTP 成功只是质量判断的第一道门', '从目标到证据，而不是从指标到目标', '第一个不变量：评估声明必须绑定完整对象', 'Evaluation Identity 必须包含 Harness 与 Environment', '第二个不变量：评估结论总是相对于分布', '平均值、切片与不确定性', '评估对象有四个层次', 'Model Evaluation']。<!-- existing:SF-2026-ARXIV-2605-17986:end -->
<!-- delta:SF-2026-ARXIV-2605-17986:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-17986:end -->
<!-- books-review:SF-2026-ARXIV-2605-17986:end -->

<!-- books-review:SF-2026-ARXIV-2605-17989:start -->
<!-- existing:SF-2026-ARXIV-2605-17989:start -->已顺读 `books/part-07-agent/76-rag.md` 与相邻章节 ['books/part-07-agent/75-context.md', 'books/part-07-agent/77-memory.md']；正文主线 headings=['本章要回答的问题', '参数化知识的边界', 'Offline Ingestion 不是预处理细节', 'Online Retrieval Pipeline', 'Tenant Filter 必须在检索内核中前置执行', 'Retrieval 的基本度量', 'Chunking 是信息边界设计', 'Reranking 与 Context Packing', 'Relevance 不等于 Sufficient Context', 'Agentic Retrieval：Relevance 也可以是执行先验']。<!-- existing:SF-2026-ARXIV-2605-17989:end -->
<!-- delta:SF-2026-ARXIV-2605-17989:start -->当前 RAG 章有同步/异步检索，却没有预测未来 information demand、允许误预测取消并绑定 freshness 的 prefetch control；保留为写回增量。<!-- delta:SF-2026-ARXIV-2605-17989:end -->
<!-- books-review:SF-2026-ARXIV-2605-17989:end -->

<!-- books-review:SF-2026-ARXIV-2605-17992:start -->
<!-- existing:SF-2026-ARXIV-2605-17992:start -->已顺读 `books/part-07-agent/76-rag.md` 与相邻章节 ['books/part-07-agent/75-context.md', 'books/part-07-agent/77-memory.md']；正文主线 headings=['本章要回答的问题', '参数化知识的边界', 'Offline Ingestion 不是预处理细节', 'Online Retrieval Pipeline', 'Tenant Filter 必须在检索内核中前置执行', 'Retrieval 的基本度量', 'Chunking 是信息边界设计', 'Reranking 与 Context Packing', 'Relevance 不等于 Sufficient Context', 'Agentic Retrieval：Relevance 也可以是执行先验']。<!-- existing:SF-2026-ARXIV-2605-17992:end -->
<!-- delta:SF-2026-ARXIV-2605-17992:start -->当前 filtered ANN 已覆盖 query-aware routing，但没有 SSD superset traversal 与 top-k 后验证之间的 IO/recall contract；保留为写回增量。<!-- delta:SF-2026-ARXIV-2605-17992:end -->
<!-- books-review:SF-2026-ARXIV-2605-17992:end -->

<!-- books-review:SF-2026-ARXIV-2605-17998:start -->
<!-- existing:SF-2026-ARXIV-2605-17998:start -->已顺读 `books/part-07-agent/81-workflow.md` 与相邻章节 ['books/part-07-agent/80-reflection.md', 'books/part-07-agent/82-multi-agent.md']；正文主线 headings=['本章要回答的问题', '一个循环为什么不够', 'State Machine 是基本模型', 'Failure attribution、perception routing 与 sticky state ownership', 'Review notes', '从“对象已保存”到“状态已激活”', 'Deterministic Spine，Agentic Nodes', '从一次性脚本到平台拥有的可编辑 DAG', 'Template、Realized Graph 与 Trace 不是同一个对象', 'Offline World 是可验证的数据工厂，不是 Live Workflow 的替身']。<!-- existing:SF-2026-ARXIV-2605-17998:end -->
<!-- delta:SF-2026-ARXIV-2605-17998:start -->当前 workflow 有 verifier/commit，但没有把 completion proposal 与只读 admission authority、bounded packet state 和 fail-closed recovery写成同一完成协议；保留为写回增量。<!-- delta:SF-2026-ARXIV-2605-17998:end -->
<!-- books-review:SF-2026-ARXIV-2605-17998:end -->

<!-- books-review:SF-2026-ARXIV-2605-18032:start -->
<!-- existing:SF-2026-ARXIV-2605-18032:start -->已顺读 `books/part-07-agent/81-workflow.md` 与相邻章节 ['books/part-07-agent/80-reflection.md', 'books/part-07-agent/82-multi-agent.md']；正文主线 headings=['本章要回答的问题', '一个循环为什么不够', 'State Machine 是基本模型', 'Failure attribution、perception routing 与 sticky state ownership', 'Review notes', '从“对象已保存”到“状态已激活”', 'Deterministic Spine，Agentic Nodes', '从一次性脚本到平台拥有的可编辑 DAG', 'Template、Realized Graph 与 Trace 不是同一个对象', 'Offline World 是可验证的数据工厂，不是 Live Workflow 的替身']。<!-- existing:SF-2026-ARXIV-2605-18032:end -->
<!-- delta:SF-2026-ARXIV-2605-18032:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-18032:end -->
<!-- books-review:SF-2026-ARXIV-2605-18032:end -->

<!-- books-review:SF-2026-ARXIV-2605-18041:start -->
<!-- existing:SF-2026-ARXIV-2605-18041:start -->已顺读 `books/part-03-multimodal-world-models/23-multimodal-representation.md` 与相邻章节 ['books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md']；正文主线 headings=['本章要回答的问题', '为什么文本 token 的经验不能直接复制', '一个思想实验：同样是 256 个 token', '表示演进：从专用特征到统一协议', '阶段一：手工特征与专用模型', '阶段二：modality-specific encoder + projector', '阶段三：共享 token space', '阶段四：native multimodal representation', '连续表示、离散表示与混合表示', '连续表示']。<!-- existing:SF-2026-ARXIV-2605-18041:end -->
<!-- delta:SF-2026-ARXIV-2605-18041:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-18041:end -->
<!-- books-review:SF-2026-ARXIV-2605-18041:end -->

<!-- books-review:SF-2026-ARXIV-2605-18053:start -->
<!-- existing:SF-2026-ARXIV-2605-18053:start -->已顺读 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 与相邻章节 ['books/part-05-inference-system/44-decode.md', 'books/part-05-inference-system/46-continuous-batching.md']；正文主线 headings=['本章要回答的问题', '如果完全不缓存', '为什么缓存 K/V 而不是 Query', '逻辑 Shape 与容量公式', '一个容量小例子', 'KV Cache 的生命周期', 'Segmented Execution 必须在训练与推理共享同一语义', 'Prefix reuse', 'KV 从生成私有状态演进为受约束的下游读出接口', 'Structured knowledge 只有进入 physical access plan 才改变 KV 成本']。<!-- existing:SF-2026-ARXIV-2605-18053:end -->
<!-- delta:SF-2026-ARXIV-2605-18053:start -->当前 KV eviction 已覆盖 selector/quantizer/fallback，但没有把 prompt/modality boundary 的不可驱逐保护作为 global-cap 前的结构不变量；保留为写回增量。<!-- delta:SF-2026-ARXIV-2605-18053:end -->
<!-- books-review:SF-2026-ARXIV-2605-18053:end -->

<!-- books-review:SF-2026-ARXIV-2605-18067:start -->
<!-- existing:SF-2026-ARXIV-2605-18067:start -->已顺读 `books/part-07-agent/82-multi-agent.md` 与相邻章节 ['books/part-07-agent/81-workflow.md', 'books/part-07-agent/83-mcp.md']；正文主线 headings=['本章要回答的问题', '先建立单 Agent Baseline', '扩展 Agent 数量之前，先测量 Coordination Tax', '什么时候分解有意义', '典型拓扑', 'Topology 从部署前选择演进到运行时有界修复', '通信可以压缩成 latent，但 contract 不能一起消失', 'Behavioral belief 不等于 authenticated identity', 'Message 不是 State', 'Pairwise coupling 不能外推 group dynamics']。<!-- existing:SF-2026-ARXIV-2605-18067:end -->
<!-- delta:SF-2026-ARXIV-2605-18067:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-18067:end -->
<!-- books-review:SF-2026-ARXIV-2605-18067:end -->

<!-- books-review:SF-2026-ARXIV-2605-18071:start -->
<!-- existing:SF-2026-ARXIV-2605-18071:start -->已顺读 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 与相邻章节 ['books/part-05-inference-system/44-decode.md', 'books/part-05-inference-system/46-continuous-batching.md']；正文主线 headings=['本章要回答的问题', '如果完全不缓存', '为什么缓存 K/V 而不是 Query', '逻辑 Shape 与容量公式', '一个容量小例子', 'KV Cache 的生命周期', 'Segmented Execution 必须在训练与推理共享同一语义', 'Prefix reuse', 'KV 从生成私有状态演进为受约束的下游读出接口', 'Structured knowledge 只有进入 physical access plan 才改变 KV 成本']。<!-- existing:SF-2026-ARXIV-2605-18071:end -->
<!-- delta:SF-2026-ARXIV-2605-18071:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-18071:end -->
<!-- books-review:SF-2026-ARXIV-2605-18071:end -->

<!-- books-review:SF-2026-ARXIV-2605-18106:start -->
<!-- existing:SF-2026-ARXIV-2605-18106:start -->已顺读 `books/part-04-training-system/28-pretraining.md` 与相邻章节 ['books/part-04-training-system/27-data.md', 'books/part-04-training-system/29-sft.md']；正文主线 headings=['本章要回答的问题', '从随机参数开始会发生什么', 'Next-token objective', '一个 token loss 小例子', 'Perplexity 能回答什么', '一次 training step 的状态流', 'Residual Path 也可以成为随 Depth 与 Time 演化的训练状态', 'Optimizer 不是与参数化无关的旋钮', 'Optimizer State Allocation 也应服从参数角色', 'Batch、tokens 与 optimizer steps 不是同一计量']。<!-- existing:SF-2026-ARXIV-2605-18106:end -->
<!-- delta:SF-2026-ARXIV-2605-18106:start -->当前 optimizer 叙述未把 embedding/LM-head/SwiGLU/MoE-router 的参数对称性作为 optimizer state/action compatibility contract；保留为写回增量。<!-- delta:SF-2026-ARXIV-2605-18106:end -->
<!-- books-review:SF-2026-ARXIV-2605-18106:end -->

<!-- books-review:SF-2026-ARXIV-2605-18165:start -->
<!-- existing:SF-2026-ARXIV-2605-18165:start -->已顺读 `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md` 与相邻章节 ['books/part-03-multimodal-world-models/23-multimodal-representation.md', 'books/part-03-multimodal-world-models/25-multimodal-world-models.md']；正文主线 headings=['本章要回答的问题', '从一个共同问题开始', '为什么 Autoregressive 是合理起点', 'Diffusion：用迭代修正换并行状态更新', 'Masked generation：未知位置与已知位置', 'Editable tokens 与 commit boundary', 'Self-revision：并行位置必须在 Commit 前保持可撤销', '生成 Workflow 也可以被训练进 Intermediate State', 'Block Diffusion：局部自回归与块内并行', 'Draft、Verify 与 Correct 不是同一件事']。<!-- existing:SF-2026-ARXIV-2605-18165:end -->
<!-- delta:SF-2026-ARXIV-2605-18165:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-18165:end -->
<!-- books-review:SF-2026-ARXIV-2605-18165:end -->

<!-- books-review:SF-2026-ARXIV-2605-18271:start -->
<!-- existing:SF-2026-ARXIV-2605-18271:start -->已顺读 `books/part-07-agent/77-memory.md` 与相邻章节 ['books/part-07-agent/76-rag.md', 'books/part-07-agent/78-tool-calling.md']；正文主线 headings=['本章要回答的问题', 'Context 与 Memory 的状态边界', 'Memory 类型是用途，不只是存储介质', 'Memory Write 是高风险决策', 'Write / Hold 不足以定义下一状态', '从 Outcome Reward 到 Content-level Credit：归因只能约束写入，不能成为真值', 'Memory Read 是受约束检索', '从按需读取到选择性主动干预', '从一次 Top-k 检索到有预算的关联回忆', 'Fact State 与 Retrieval-policy State 必须分离']。<!-- existing:SF-2026-ARXIV-2605-18271:end -->
<!-- delta:SF-2026-ARXIV-2605-18271:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-18271:end -->
<!-- books-review:SF-2026-ARXIV-2605-18271:end -->

<!-- books-review:SF-2026-ARXIV-2605-18401:start -->
<!-- existing:SF-2026-ARXIV-2605-18401:start -->已顺读 `books/part-07-agent/84-agent-platform.md` 与相邻章节 ['books/part-07-agent/83-mcp.md']；正文主线 headings=['本章要回答的问题', 'Agent 改变了平台的控制对象', 'Serving 结束不等于 Agent 任务结束', 'Agent Definition 与 Run Identity', '可复用 Skill 不是一个 Prompt 文件', '从 Skill Catalog 到 Competence-aware Orchestration', '从 Trajectory 到 Skill 是一次受治理的 Compilation', 'Skill Compiler 必须绑定 Target Profile，而不是只绑定模型名', 'Self-evolution Admission 需要 Anytime-valid Acceptor', 'Workspace 是长期行动的隔离单元']。<!-- existing:SF-2026-ARXIV-2605-18401:end -->
<!-- delta:SF-2026-ARXIV-2605-18401:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-18401:end -->
<!-- books-review:SF-2026-ARXIV-2605-18401:end -->

<!-- books-review:SF-2026-ARXIV-2605-18414:start -->
<!-- existing:SF-2026-ARXIV-2605-18414:start -->已顺读 `books/part-07-agent/83-mcp.md` 与相邻章节 ['books/part-07-agent/82-multi-agent.md', 'books/part-07-agent/84-agent-platform.md']；正文主线 headings=['本章要回答的问题', '为什么需要协议层', 'Host、Client、Server', 'Data Layer 与 Transport Layer', 'Server Primitives', 'Lifecycle 与 Version Contract', 'Update 2026-07-29 — 从连接会话到显式请求契约', 'MCP 不等于 Tool Authorization', 'Sampling、Elicitation 与递归能力', 'MCP 与 Workflow/Multi-Agent 的边界']。<!-- existing:SF-2026-ARXIV-2605-18414:end -->
<!-- delta:SF-2026-ARXIV-2605-18414:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-18414:end -->
<!-- books-review:SF-2026-ARXIV-2605-18414:end -->

<!-- books-review:SF-2026-ARXIV-2605-18421:start -->
<!-- existing:SF-2026-ARXIV-2605-18421:start -->已顺读 `books/part-07-agent/77-memory.md` 与相邻章节 ['books/part-07-agent/76-rag.md', 'books/part-07-agent/78-tool-calling.md']；正文主线 headings=['本章要回答的问题', 'Context 与 Memory 的状态边界', 'Memory 类型是用途，不只是存储介质', 'Memory Write 是高风险决策', 'Write / Hold 不足以定义下一状态', '从 Outcome Reward 到 Content-level Credit：归因只能约束写入，不能成为真值', 'Memory Read 是受约束检索', '从按需读取到选择性主动干预', '从一次 Top-k 检索到有预算的关联回忆', 'Fact State 与 Retrieval-policy State 必须分离']。<!-- existing:SF-2026-ARXIV-2605-18421:end -->
<!-- delta:SF-2026-ARXIV-2605-18421:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-18421:end -->
<!-- books-review:SF-2026-ARXIV-2605-18421:end -->

<!-- books-review:SF-2026-ARXIV-2605-18498:start -->
<!-- existing:SF-2026-ARXIV-2605-18498:start -->已顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；正文主线 headings=['本章要回答的问题', '为什么“选一个分数”不是评估系统', 'HTTP 成功只是质量判断的第一道门', '从目标到证据，而不是从指标到目标', '第一个不变量：评估声明必须绑定完整对象', 'Evaluation Identity 必须包含 Harness 与 Environment', '第二个不变量：评估结论总是相对于分布', '平均值、切片与不确定性', '评估对象有四个层次', 'Model Evaluation']。<!-- existing:SF-2026-ARXIV-2605-18498:end -->
<!-- delta:SF-2026-ARXIV-2605-18498:start -->当前 evaluation 章缺少将 MoE load balance 与 functional specialization 分开、并用干预验证而非只看 routing frequency 的契约；保留为写回增量。<!-- delta:SF-2026-ARXIV-2605-18498:end -->
<!-- books-review:SF-2026-ARXIV-2605-18498:end -->

<!-- books-review:SF-2026-ARXIV-2605-18565:start -->
<!-- existing:SF-2026-ARXIV-2605-18565:start -->已顺读 `books/part-07-agent/77-memory.md` 与相邻章节 ['books/part-07-agent/76-rag.md', 'books/part-07-agent/78-tool-calling.md']；正文主线 headings=['本章要回答的问题', 'Context 与 Memory 的状态边界', 'Memory 类型是用途，不只是存储介质', 'Memory Write 是高风险决策', 'Write / Hold 不足以定义下一状态', '从 Outcome Reward 到 Content-level Credit：归因只能约束写入，不能成为真值', 'Memory Read 是受约束检索', '从按需读取到选择性主动干预', '从一次 Top-k 检索到有预算的关联回忆', 'Fact State 与 Retrieval-policy State 必须分离']。<!-- existing:SF-2026-ARXIV-2605-18565:end -->
<!-- delta:SF-2026-ARXIV-2605-18565:start -->当前 memory 章覆盖版本与冲突，但没有把 multi-target interference、update history 与 aggregate reasoning 组合成一条验收轴；保留为写回增量。<!-- delta:SF-2026-ARXIV-2605-18565:end -->
<!-- books-review:SF-2026-ARXIV-2605-18565:end -->

<!-- books-review:SF-2026-ARXIV-2605-18583:start -->
<!-- existing:SF-2026-ARXIV-2605-18583:start -->已顺读 `books/part-06-ai-infrastructure/72-security.md` 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；正文主线 headings=['本章要回答的问题', '从资产与信任边界开始', '生命周期威胁', '隐私检测是 Policy-bound Sensor，不是安全判决', '从独立 Span 到关系感知的本地 Sanitization', 'Differential Privacy 先定义被保护对象，再选择机制', 'Privacy Accountant 必须与真实实现同构', 'Capability Access Control 可以前移到训练状态', 'Policy-as-Data：可更新规则与模型判断必须分开版本化', '从“文本是否恶意”到“谁获得了行为控制权”']。<!-- existing:SF-2026-ARXIV-2605-18583:end -->
<!-- delta:SF-2026-ARXIV-2605-18583:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-18583:end -->
<!-- books-review:SF-2026-ARXIV-2605-18583:end -->

<!-- books-review:SF-2026-ARXIV-2605-18607:start -->
<!-- existing:SF-2026-ARXIV-2605-18607:start -->已顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；正文主线 headings=['本章要回答的问题', '为什么“选一个分数”不是评估系统', 'HTTP 成功只是质量判断的第一道门', '从目标到证据，而不是从指标到目标', '第一个不变量：评估声明必须绑定完整对象', 'Evaluation Identity 必须包含 Harness 与 Environment', '第二个不变量：评估结论总是相对于分布', '平均值、切片与不确定性', '评估对象有四个层次', 'Model Evaluation']。<!-- existing:SF-2026-ARXIV-2605-18607:end -->
<!-- delta:SF-2026-ARXIV-2605-18607:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-18607:end -->
<!-- books-review:SF-2026-ARXIV-2605-18607:end -->

<!-- books-review:SF-2026-ARXIV-2605-18652:start -->
<!-- existing:SF-2026-ARXIV-2605-18652:start -->已顺读 `books/part-07-agent/77-memory.md` 与相邻章节 ['books/part-07-agent/76-rag.md', 'books/part-07-agent/78-tool-calling.md']；正文主线 headings=['本章要回答的问题', 'Context 与 Memory 的状态边界', 'Memory 类型是用途，不只是存储介质', 'Memory Write 是高风险决策', 'Write / Hold 不足以定义下一状态', '从 Outcome Reward 到 Content-level Credit：归因只能约束写入，不能成为真值', 'Memory Read 是受约束检索', '从按需读取到选择性主动干预', '从一次 Top-k 检索到有预算的关联回忆', 'Fact State 与 Retrieval-policy State 必须分离']。<!-- existing:SF-2026-ARXIV-2605-18652:end -->
<!-- delta:SF-2026-ARXIV-2605-18652:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-18652:end -->
<!-- books-review:SF-2026-ARXIV-2605-18652:end -->

<!-- books-review:SF-2026-ARXIV-2605-18693:start -->
<!-- existing:SF-2026-ARXIV-2605-18693:start -->已顺读 `books/part-07-agent/84-agent-platform.md` 与相邻章节 ['books/part-07-agent/83-mcp.md']；正文主线 headings=['本章要回答的问题', 'Agent 改变了平台的控制对象', 'Serving 结束不等于 Agent 任务结束', 'Agent Definition 与 Run Identity', '可复用 Skill 不是一个 Prompt 文件', '从 Skill Catalog 到 Competence-aware Orchestration', '从 Trajectory 到 Skill 是一次受治理的 Compilation', 'Skill Compiler 必须绑定 Target Profile，而不是只绑定模型名', 'Self-evolution Admission 需要 Anytime-valid Acceptor', 'Workspace 是长期行动的隔离单元']。<!-- existing:SF-2026-ARXIV-2605-18693:end -->
<!-- delta:SF-2026-ARXIV-2605-18693:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-18693:end -->
<!-- books-review:SF-2026-ARXIV-2605-18693:end -->

<!-- books-review:SF-2026-ARXIV-2605-18697:start -->
<!-- existing:SF-2026-ARXIV-2605-18697:start -->已顺读 `books/part-07-agent/81-workflow.md` 与相邻章节 ['books/part-07-agent/80-reflection.md', 'books/part-07-agent/82-multi-agent.md']；正文主线 headings=['本章要回答的问题', '一个循环为什么不够', 'State Machine 是基本模型', 'Failure attribution、perception routing 与 sticky state ownership', 'Review notes', '从“对象已保存”到“状态已激活”', 'Deterministic Spine，Agentic Nodes', '从一次性脚本到平台拥有的可编辑 DAG', 'Template、Realized Graph 与 Trace 不是同一个对象', 'Offline World 是可验证的数据工厂，不是 Live Workflow 的替身']。<!-- existing:SF-2026-ARXIV-2605-18697:end -->
<!-- delta:SF-2026-ARXIV-2605-18697:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-18697:end -->
<!-- books-review:SF-2026-ARXIV-2605-18697:end -->

<!-- books-review:SF-2026-ARXIV-2605-18703:start -->
<!-- existing:SF-2026-ARXIV-2605-18703:start -->已顺读 `books/part-07-agent/81-workflow.md` 与相邻章节 ['books/part-07-agent/80-reflection.md', 'books/part-07-agent/82-multi-agent.md']；正文主线 headings=['本章要回答的问题', '一个循环为什么不够', 'State Machine 是基本模型', 'Failure attribution、perception routing 与 sticky state ownership', 'Review notes', '从“对象已保存”到“状态已激活”', 'Deterministic Spine，Agentic Nodes', '从一次性脚本到平台拥有的可编辑 DAG', 'Template、Realized Graph 与 Trace 不是同一个对象', 'Offline World 是可验证的数据工厂，不是 Live Workflow 的替身']。<!-- existing:SF-2026-ARXIV-2605-18703:end -->
<!-- delta:SF-2026-ARXIV-2605-18703:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-18703:end -->
<!-- books-review:SF-2026-ARXIV-2605-18703:end -->

<!-- books-review:SF-2026-ARXIV-2605-18710:start -->
<!-- existing:SF-2026-ARXIV-2605-18710:start -->已顺读 `books/part-04-training-system/36-distributed-training.md` 与相邻章节 ['books/part-04-training-system/35-checkpoint.md', 'books/part-04-training-system/37-tensor-parallel.md']；正文主线 headings=['本章要回答的问题', '单卡为什么会失败', '从本机协作到分布式执行', '先分清五个通信层次', 'Collective 是群体语义，不是一种算法', '用 Alpha-Beta 模型建立下界直觉', 'Ring、Tree 与 Butterfly 在优化什么', 'MPI、NCCL、UCX、UCC 与 NIXL 的边界', 'Collective 进入计算图后，Completion 也成为 Autograd 语义', '从 Collective Call 到 Kernel 内 Remote Memory']。<!-- existing:SF-2026-ARXIV-2605-18710:end -->
<!-- delta:SF-2026-ARXIV-2605-18710:start -->当前 multimodal/distributed training 章缺少空间复用时 module placement、GPU share 与 interference budget 的联合 owner；保留为写回增量。<!-- delta:SF-2026-ARXIV-2605-18710:end -->
<!-- books-review:SF-2026-ARXIV-2605-18710:end -->

<!-- books-review:SF-2026-ARXIV-2605-18739:start -->
<!-- existing:SF-2026-ARXIV-2605-18739:start -->已顺读 `books/part-04-training-system/36-distributed-training.md` 与相邻章节 ['books/part-04-training-system/35-checkpoint.md', 'books/part-04-training-system/37-tensor-parallel.md']；正文主线 headings=['本章要回答的问题', '单卡为什么会失败', '从本机协作到分布式执行', '先分清五个通信层次', 'Collective 是群体语义，不是一种算法', '用 Alpha-Beta 模型建立下界直觉', 'Ring、Tree 与 Butterfly 在优化什么', 'MPI、NCCL、UCX、UCC 与 NIXL 的边界', 'Collective 进入计算图后，Completion 也成为 Autograd 语义', '从 Collective Call 到 Kernel 内 Remote Memory']。<!-- existing:SF-2026-ARXIV-2605-18739:end -->
<!-- delta:SF-2026-ARXIV-2605-18739:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-18739:end -->
<!-- books-review:SF-2026-ARXIV-2605-18739:end -->

<!-- books-review:SF-2026-ARXIV-2605-18750:start -->
<!-- existing:SF-2026-ARXIV-2605-18750:start -->已顺读 `books/part-04-training-system/38-pipeline-parallel.md` 与相邻章节 ['books/part-04-training-system/37-tensor-parallel.md', 'books/part-04-training-system/39-zero.md']；正文主线 headings=['本章要回答的问题', '只有 Layer Partition 会发生什么', 'Micro-batch 怎样填充 Pipeline', 'Bubble 从哪里来', 'GPipe：先 Forward，再 Backward', '1F1B：缩短 Activation Lifetime', '异步 Pipeline：去掉 Bubble 会把成本移到参数版本', 'Interleaving 为什么引入 Virtual Stages', 'Boundary Communication 在传什么', 'Stage Balance 比平均 Layer 数更重要']。<!-- existing:SF-2026-ARXIV-2605-18750:end -->
<!-- delta:SF-2026-ARXIV-2605-18750:start -->当前 pipeline 章以 schedule 为主，但没有在运行时以真实 task readiness 取得 dispatch authority并保留静态 schedule fallback；保留为写回增量。<!-- delta:SF-2026-ARXIV-2605-18750:end -->
<!-- books-review:SF-2026-ARXIV-2605-18750:end -->

<!-- books-review:SF-2026-ARXIV-2605.16588:start -->
<!-- existing:SF-2026-ARXIV-2605.16588:start -->Ch26 already includes stronger runtime-assurance separation between nominal controller, safety admission and verified fallback under physical evidence.<!-- existing:SF-2026-ARXIV-2605.16588:end -->
<!-- delta:SF-2026-ARXIV-2605.16588:start -->Ch26 already includes stronger runtime-assurance separation between nominal controller, safety admission and verified fallback under physical evidence.<!-- delta:SF-2026-ARXIV-2605.16588:end --> Final decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605.16588:end -->

<!-- books-review:SF-2026-ARXIV-2605.16622:start -->
<!-- existing:SF-2026-ARXIV-2605.16622:start -->`books/part-04-training-system/28-pretraining.md` contains the surrounding principle but not the exact control/evidence delta below; adjacent chapters do not own it.<!-- existing:SF-2026-ARXIV-2605.16622:end -->
<!-- delta:SF-2026-ARXIV-2605.16622:start -->Weight decay changes progressive sharpening through global parameter interaction rather than simple local friction, refining Ch28's stability/EoS mechanism and architecture-dependent boundary.<!-- delta:SF-2026-ARXIV-2605.16622:end --> Final decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605.16622:end -->

<!-- books-review:SF-2026-ARXIV-2605.16647:start -->
<!-- existing:SF-2026-ARXIV-2605.16647:start -->Ch72 already carries encrypted state-space inference, public-parameter constraints, ciphertext depth/noise and FHE fallback boundaries.<!-- existing:SF-2026-ARXIV-2605.16647:end -->
<!-- delta:SF-2026-ARXIV-2605.16647:start -->Ch72 already carries encrypted state-space inference, public-parameter constraints, ciphertext depth/noise and FHE fallback boundaries.<!-- delta:SF-2026-ARXIV-2605.16647:end --> Final decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605.16647:end -->

<!-- books-review:SF-ANNEAL-GOVERNED-SYMBOLIC-PATCHES:start -->
<!-- existing:SF-ANNEAL-GOVERNED-SYMBOLIC-PATCHES:start -->The current owner already states the durable mechanism boundary; this paper is a bounded supporting case and would duplicate the chapter spine.<!-- existing:SF-ANNEAL-GOVERNED-SYMBOLIC-PATCHES:end --> <!-- delta:SF-ANNEAL-GOVERNED-SYMBOLIC-PATCHES:start -->Agent adaptation can commit governed symbolic patches with explicit admission and rollback rather than silently mutating prompts or weights from experience.<!-- delta:SF-ANNEAL-GOVERNED-SYMBOLIC-PATCHES:end --> Decision remains `No Change — Existing Coverage`. Shared Books were not modified in this author lane.
<!-- books-review:SF-ANNEAL-GOVERNED-SYMBOLIC-PATCHES:end -->

<!-- books-review:SF-FRE-RES-FREQUENCY-RESIDUAL-VIDEO-TOKEN-COMPRESSION-FOR-EFFICIENT-VIDEO-M:start -->
<!-- existing:SF-FRE-RES-FREQUENCY-RESIDUAL-VIDEO-TOKEN-COMPRESSION-FOR-EFFICIENT-VIDEO-M:start -->已读取 `books/part-03-multimodal-world-models/23-multimodal-representation.md` 及相邻章节 ['books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md']；当前 owner 已覆盖 `MULTIMODAL-REPRESENTATION` 的基础契约，直接机制词命中 ['residual', 'compression']。本比较只判断正文现有命题，不把 Review notes/标题命中当作已整合。<!-- existing:SF-FRE-RES-FREQUENCY-RESIDUAL-VIDEO-TOKEN-COMPRESSION-FOR-EFFICIENT-VIDEO-M:end -->
<!-- delta:SF-FRE-RES-FREQUENCY-RESIDUAL-VIDEO-TOKEN-COMPRESSION-FOR-EFFICIENT-VIDEO-M:start -->We propose \textbf{Fre-Res}, a budget-adaptive dual-track video-token compression framework that separates these two forms of evidence.<!-- delta:SF-FRE-RES-FREQUENCY-RESIDUAL-VIDEO-TOKEN-COMPRESSION-FOR-EFFICIENT-VIDEO-M:end --> Decision=`No Change — Existing Coverage`；本 author lane 未修改共享 Books。
<!-- books-review:SF-FRE-RES-FREQUENCY-RESIDUAL-VIDEO-TOKEN-COMPRESSION-FOR-EFFICIENT-VIDEO-M:end -->

<!-- books-review:SF-MIXING-TIMES-OF-GLAUBER-DYNAMICS-ON-MASKED-LANGUAGE-MODELS:start -->
<!-- existing:SF-MIXING-TIMES-OF-GLAUBER-DYNAMICS-ON-MASKED-LANGUAGE-MODELS:start -->已读取 `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md` 及相邻章节 ['books/part-03-multimodal-world-models/23-multimodal-representation.md', 'books/part-03-multimodal-world-models/25-multimodal-world-models.md']；当前 owner 已覆盖 `MULTIMODAL-GENERATIVE-PARADIGMS` 的基础契约，直接机制词命中 ['masked', 'language', 'models']。本比较只判断正文现有命题，不把 Review notes/标题命中当作已整合。<!-- existing:SF-MIXING-TIMES-OF-GLAUBER-DYNAMICS-ON-MASKED-LANGUAGE-MODELS:end -->
<!-- delta:SF-MIXING-TIMES-OF-GLAUBER-DYNAMICS-ON-MASKED-LANGUAGE-MODELS:start -->We first show that MLM conditionals are intrinsically incompatible: we introduce a rectangle test that certifies this incompatibility and empirically verify its prevalence across modern MLMs.<!-- delta:SF-MIXING-TIMES-OF-GLAUBER-DYNAMICS-ON-MASKED-LANGUAGE-MODELS:end --> Decision=`No Change — Existing Coverage`；本 author lane 未修改共享 Books。
<!-- books-review:SF-MIXING-TIMES-OF-GLAUBER-DYNAMICS-ON-MASKED-LANGUAGE-MODELS:end -->

<!-- books-review:SF-ORBISIM-WORLD-MODELS-AS-DIFFERENTIABLE-PHYSICS-ENGINES-FOR-EMBODIED-INTE:start -->
<!-- existing:SF-ORBISIM-WORLD-MODELS-AS-DIFFERENTIABLE-PHYSICS-ENGINES-FOR-EMBODIED-INTE:start -->`books/part-03-multimodal-world-models/25-multimodal-world-models.md` 已以更一般的 MULTIMODAL-WORLD-MODELS 演进链承载 `OrbiSim: World Models as Differentiable Physics Engines for Embodied Intelligence` 的问题：owner、commit/evidence boundary、失败回退与旧路径共存已经显式化；该 exact-v1 只增加受限实现或 benchmark evidence。<!-- existing:SF-ORBISIM-WORLD-MODELS-AS-DIFFERENTIABLE-PHYSICS-ENGINES-FOR-EMBODIED-INTE:end -->
<!-- delta:SF-ORBISIM-WORLD-MODELS-AS-DIFFERENTIABLE-PHYSICS-ENGINES-FOR-EMBODIED-INTE:start -->We present OrbiSim, a novel robotic simulation paradigm that redefines world models as a fully differentiable physics engine for embodied intelligence.<!-- delta:SF-ORBISIM-WORLD-MODELS-AS-DIFFERENTIABLE-PHYSICS-ENGINES-FOR-EMBODIED-INTE:end --> Final prewrite decision=`No Change — Existing Coverage`。Integrate 只进入 date-local queue；本 reviewer 未修改共享 Books。
<!-- books-review:SF-ORBISIM-WORLD-MODELS-AS-DIFFERENTIABLE-PHYSICS-ENGINES-FOR-EMBODIED-INTE:end -->

<!-- books-review:SF-ORTH-DION-ELIMINATING-GEOMETRIC-MISMATCH-IN-DISTRIBUTED-LOW-RANK-SPECTRA:start -->
<!-- existing:SF-ORTH-DION-ELIMINATING-GEOMETRIC-MISMATCH-IN-DISTRIBUTED-LOW-RANK-SPECTRA:start -->fresh-context current-books challenge 已读取 `books/part-04-training-system/36-distributed-training.md` 及相邻章节 `books/part-04-training-system/35-checkpoint.md`, `books/part-04-training-system/37-tensor-parallel.md`；canonical owner=`TRAIN-DISTRIBUTED-TRAINING`。`Orth-Dion: Eliminating Geometric Mismatch in Distributed Low-Rank Spectral Optimization` 的 exact-v1 机制为：We show that this gap is geometric: column normalization does not yield the rank-$r$ polar factor that Muon implicitly targets, so the resulting direction violates the dual-norm constraint of the low-rank spectral geometry, and the rate picks up…。重读 current owner+adjacent 后，the body already owns fault observation/recovery and runtime parallelism transition with topology, optimizer/checkpoint state and rollback；该论文提供受限案例或局部实现，但没有再改变长期 state/data/control owner、evaluation/release contract 或 fallback/coexistence。<!-- existing:SF-ORTH-DION-ELIMINATING-GEOMETRIC-MISMATCH-IN-DISTRIBUTED-LOW-RANK-SPECTRA:end -->
<!-- delta:SF-ORTH-DION-ELIMINATING-GEOMETRIC-MISMATCH-IN-DISTRIBUTED-LOW-RANK-SPECTRA:start -->We show that this gap is geometric: column normalization does not yield the rank-$r$ polar factor that Muon implicitly targets, so the resulting direction violates the dual-norm constraint of the low-rank spectral geometry, and the rate picks up…<!-- delta:SF-ORTH-DION-ELIMINATING-GEOMETRIC-MISMATCH-IN-DISTRIBUTED-LOW-RANK-SPECTRA:end --> Decision=`No Change — Existing Coverage`；本轮仅同步 date-local 结构化真值，未修改共享 Books。
<!-- books-review:SF-ORTH-DION-ELIMINATING-GEOMETRIC-MISMATCH-IN-DISTRIBUTED-LOW-RANK-SPECTRA:end -->

<!-- books-review:SF-PROOF-CARRYING-CERTIFICATES-FOR-LLM-PIPELINES-A-TRUST-BOUNDARY-ARCHITECT:start -->
<!-- existing:SF-PROOF-CARRYING-CERTIFICATES-FOR-LLM-PIPELINES-A-TRUST-BOUNDARY-ARCHITECT:start -->已读取 `books/part-06-ai-infrastructure/72-security.md` 及相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；owner 当前主干包含 ['本章要回答的问题', '从资产与信任边界开始', '生命周期威胁', '隐私检测是 Policy-bound Sensor，不是安全判决', '从独立 Span 到关系感知的本地 Sanitization', 'Differential Privacy 先定义被保护对象，再选择机制', 'Capability Access Control 可以前移到训练状态', 'Policy-as-Data：可更新规则与模型判断必须分开版本化']。仅正文命题用于比较，Review notes 不视为整合。<!-- existing:SF-PROOF-CARRYING-CERTIFICATES-FOR-LLM-PIPELINES-A-TRUST-BOUNDARY-ARCHITECT:end -->
<!-- delta:SF-PROOF-CARRYING-CERTIFICATES-FOR-LLM-PIPELINES-A-TRUST-BOUNDARY-ARCHITECT:start -->We present a framework for verifying the deterministic structured computations surrounding a large language model rather than the model itself, extending a Lean 4 trust-boundary architecture to the generic interfaces of modern LLM pipelines.<!-- delta:SF-PROOF-CARRYING-CERTIFICATES-FOR-LLM-PIPELINES-A-TRUST-BOUNDARY-ARCHITECT:end --> Independent decision=`No Change — Existing Coverage`；prewrite challenge 已通过，不写共享 Books。
<!-- books-review:SF-PROOF-CARRYING-CERTIFICATES-FOR-LLM-PIPELINES-A-TRUST-BOUNDARY-ARCHITECT:end -->

<!-- books-review:SF-SELFPLAY-DECISION-CAPACITY-COLLAPSE:start -->
<!-- existing:SF-SELFPLAY-DECISION-CAPACITY-COLLAPSE:start -->The current owner already states the durable mechanism boundary; this paper is a bounded supporting case and would duplicate the chapter spine.<!-- existing:SF-SELFPLAY-DECISION-CAPACITY-COLLAPSE:end --> <!-- delta:SF-SELFPLAY-DECISION-CAPACITY-COLLAPSE:start -->Self-play can collapse when policy decision capacity crosses an environment-dependent threshold; more optimization is not monotonic capability improvement.<!-- delta:SF-SELFPLAY-DECISION-CAPACITY-COLLAPSE:end --> Decision remains `No Change — Existing Coverage`. Shared Books were not modified in this author lane.
<!-- books-review:SF-SELFPLAY-DECISION-CAPACITY-COLLAPSE:end -->

<!-- books-review:SF-SIGNMUON-SIGN-ORTHOGONALIZED-OPTIMIZER:start -->
<!-- existing:SF-SIGNMUON-SIGN-ORTHOGONALIZED-OPTIMIZER:start -->The current owner already states the durable mechanism boundary; this paper is a bounded supporting case and would duplicate the chapter spine.<!-- existing:SF-SIGNMUON-SIGN-ORTHOGONALIZED-OPTIMIZER:end --> <!-- delta:SF-SIGNMUON-SIGN-ORTHOGONALIZED-OPTIMIZER:start -->Sign-based orthogonalized updates are a bounded optimizer branch; they reinforce, but do not replace, the existing gradient-geometry and conditioning contract.<!-- delta:SF-SIGNMUON-SIGN-ORTHOGONALIZED-OPTIMIZER:end --> Decision remains `No Change — Existing Coverage`. Shared Books were not modified in this author lane.
<!-- books-review:SF-SIGNMUON-SIGN-ORTHOGONALIZED-OPTIMIZER:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260519-COVERAGE | fresh-context:owner-replay-20260903 | coverage | coverage:SRC-ARXIV:20260519 | none | raw/retained/closure/withdrawn conservation and initial-created owner mapping independently recounted | passed |
| SA-20260519-EVIDENCE | fresh-context:owner-replay-20260903 | evidence | validator:review-completion-v1 | none | every frozen family has a completed exact-version receipt; blocked=0 | passed |
| SA-20260519-SELECTION | fresh-context:owner-replay-20260903 | deep_analysis_selection | validator:deep-analysis-selection-v1 | none | eligible=140；selected=3；all others retain completed reviews | passed |
| SA-20260519-BOOKS | fresh-context:apr-may-books-20260903 | books | validator:books-comparison-v1 | none | — | passed |

## 8. Ignored Noise

- Pre-denominator closures=1201；逐 family 理由保存在 owner receipt。
- Withdrawn=0；只保留审计 closure，不进入候选、评分、Review 或 Books。
- `updated` / current OAI datestamp 的 revision 噪声不拥有 Daily。

## 9. Recommended Action

本日全部 Gate 已闭合，无进一步动作。

## 10. Repository Changes

- Owner receipt（本阶段只读）：`papers/2026/05/_sources/arxiv-owner-replay-20260903/20260519/arxiv-owner-receipt.json`
- Canonical ledger（Books terminal state）：`papers/2026/05/_sources/arxiv-owner-replay-20260903/20260519/canonical-ledger.json`
- Books queue（fresh-context decision）：`papers/2026/05/_sources/arxiv-owner-replay-20260903/BOOKS_WRITEBACK_QUEUE.json`
- Superseded report：`papers/2026/05/_sources/arxiv-owner-replay-20260903/legacy-reports-before-created-owner-reconciliation/2026-05-19.md`
- Books body: no change for the recovered families on this date.

## 11. Open Questions

- 无。

## 12. Sources

- [DataCite REST API](https://api.datacite.org/dois) — initial `created` owner-day proxy；`updated` 只作 revision provenance。
- [arXiv OAI](https://export.arxiv.org/oai2) — identity/date corroboration；current datestamp 不拥有 first-public day。
- [arXiv](https://arxiv.org/) — exact-v1 abstract、HTML/PDF 与 version history。

## 13. Final Status

Completion Status: Complete; Coverage: Closed; Evidence: Passed; Books: Passed; unresolved findings=0
