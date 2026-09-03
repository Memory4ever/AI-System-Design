# Daily Research — 2026-05-26

**Research Date:** 2026-05-26

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-05-25 09:00:00 ～ 2026-05-26 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Historical Daily Independent Full Replay

**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed；initial-created owner replay 与 exact-v1 Evidence Review 已完成。

## Executive Summary

本次独立重放枚举并逐项闭合 1208 个注册 arXiv identity，冻结 170 个 Source Family；pre-denominator closure=1038，withdrawn pre-denominator=0。111 个旧候选被迁回正确 owner day，4 个漏检 family 已恢复 exact-v1 全文并完成 Source Review。

DataCite `created` 仅作为 initial DOI registration 的 owner-day proxy；`updated`、v1 Updated 与 current OAI datestamp 只记录 revision provenance，不决定 first-public owner。机制结论只绑定 exact-v1 正文。 本日所有 Books disposition 已有终态。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-05-26 |
| Window End | 2026-05-26 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | DEN-20260526-CREATED-20261125c20fcf8f |
| Denominator Frozen At | 2026-09-03T12:36:05+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-05-25T09:00:00+08:00 | 2026-05-26T09:00:00+08:00 | 2026-09-03T12:36:05+08:00 | DataCite prefix 10.48550 initial created-day inventory + registered arXiv categories + exact-v1 identity/body | checked | 1208 | SF-2026-ARXIV-2605-23911;SF-2026-ARXIV-2605-23918;SF-2026-ARXIV-2605-23935;SF-2026-ARXIV-2605-23945;SF-2026-ARXIV-2605-23951;SF-2026-ARXIV-2605-23956;SF-2026-ARXIV-2605-23986;SF-2026-ARXIV-2605-23988;SF-2026-ARXIV-2605-23993;SF-2026-ARXIV-2605-24004;SF-2026-ARXIV-2605-24006;SF-2026-ARXIV-2605-24022;SF-2026-ARXIV-2605-24036;SF-2026-ARXIV-2605-24042;SF-2026-ARXIV-2605-24044;SF-2026-ARXIV-2605-24050;SF-2026-ARXIV-2605-24060;SF-2026-ARXIV-2605-24069;SF-2026-ARXIV-2605-24117;SF-2026-ARXIV-2605-24134;SF-2026-ARXIV-2605-24154;SF-2026-ARXIV-2605-24168;SF-2026-ARXIV-2605-24183;SF-2026-ARXIV-2605-24197;SF-2026-ARXIV-2605-24202;SF-2026-ARXIV-2605-24213;SF-2026-ARXIV-2605-24216;SF-2026-ARXIV-2605-24217;SF-2026-ARXIV-2605-24219;SF-2026-ARXIV-2605-24220;SF-2026-ARXIV-2605-24229;SF-2026-ARXIV-2605-24245;SF-2026-ARXIV-2605-24247;SF-2026-ARXIV-2605-24248;SF-2026-ARXIV-2605-24259;SF-2026-ARXIV-2605-24279;SF-2026-ARXIV-2605-24286;SF-2026-ARXIV-2605-24299;SF-2026-ARXIV-2605-24309;SF-2026-ARXIV-2605-24312;SF-2026-ARXIV-2605-24326;SF-2026-ARXIV-2605-24391;SF-2026-ARXIV-2605-24420;SF-2026-ARXIV-2605-24421;SF-2026-ARXIV-2605-24425;SF-2026-ARXIV-2605-24426;SF-2026-ARXIV-2605-24461;SF-2026-ARXIV-2605-24468;SF-2026-ARXIV-2605-24517;SF-2026-ARXIV-2605-24547;SF-2026-ARXIV-2605-24558;SF-2026-ARXIV-2605-24579;SF-2026-ARXIV-2605-24583;SF-2026-ARXIV-2605-24598;SF-2026-ARXIV-2605-24614;SF-2026-ARXIV-2605-24619;SF-2026-ARXIV-2605-24657;SF-2026-ARXIV-2605-24659;SF-2026-ARXIV-2605-24660;SF-2026-ARXIV-2605-24661;SF-2026-ARXIV-2605-24662;SF-2026-ARXIV-2605-24667;SF-2026-ARXIV-2605-24683;SF-2026-ARXIV-2605-24697;SF-2026-ARXIV-2605-24709;SF-2026-ARXIV-2605-24727;SF-2026-ARXIV-2605-24728;SF-2026-ARXIV-2605-24733;SF-2026-ARXIV-2605-24737;SF-2026-ARXIV-2605-24743;SF-2026-ARXIV-2605-24749;SF-2026-ARXIV-2605-24756;SF-2026-ARXIV-2605-24770;SF-2026-ARXIV-2605-24775;SF-2026-ARXIV-2605-24785;SF-2026-ARXIV-2605-24786;SF-2026-ARXIV-2605-24793;SF-2026-ARXIV-2605-24817;SF-2026-ARXIV-2605-24818;SF-2026-ARXIV-2605-24823;SF-2026-ARXIV-2605-24832;SF-2026-ARXIV-2605-24870;SF-2026-ARXIV-2605-24879;SF-2026-ARXIV-2605-24883;SF-2026-ARXIV-2605-24892;SF-2026-ARXIV-2605-24914;SF-2026-ARXIV-2605-24922;SF-2026-ARXIV-2605-24930;SF-2026-ARXIV-2605-24941;SF-2026-ARXIV-2605-24973;SF-2026-ARXIV-2605-25002;SF-2026-ARXIV-2605-25052;SF-2026-ARXIV-2605-25073;SF-2026-ARXIV-2605-25077;SF-2026-ARXIV-2605-25085;SF-2026-ARXIV-2605-25092;SF-2026-ARXIV-2605-25133;SF-2026-ARXIV-2605-25160;SF-2026-ARXIV-2605-25188;SF-2026-ARXIV-2605-25189;SF-2026-ARXIV-2605-25233;SF-2026-ARXIV-2605-25240;SF-2026-ARXIV-2605-25244;SF-2026-ARXIV-2605-25247;SF-2026-ARXIV-2605-25252;SF-2026-ARXIV-2605-25272;SF-2026-ARXIV-2605-25284;SF-2026-ARXIV-2605-25292;SF-2026-ARXIV-2605-25298;SF-2026-ARXIV-2605-25310;SF-2026-ARXIV-2605-25313;SF-2026-ARXIV-2605-25338;SF-2026-ARXIV-2605-25375;SF-2026-ARXIV-2605-25376;SF-2026-ARXIV-2605-25379;SF-2026-ARXIV-2605-25389;SF-2026-ARXIV-2605-25421;SF-2026-ARXIV-2605-25422;SF-2026-ARXIV-2605-25424;SF-2026-ARXIV-2605-25430;SF-2026-ARXIV-2605-25451;SF-2026-ARXIV-2605-25475;SF-2026-ARXIV-2605-25492;SF-2026-ARXIV-2605-25507;SF-2026-ARXIV-2605-25521;SF-2026-ARXIV-2605-25535;SF-2026-ARXIV-2605-25537;SF-2026-ARXIV-2605-25547;SF-2026-ARXIV-2605-25550;SF-2026-ARXIV-2605-25621;SF-2026-ARXIV-2605-25624;SF-2026-ARXIV-2605-25632;SF-2026-ARXIV-2605-25641;SF-2026-ARXIV-2605-25653;SF-2026-ARXIV-2605-25655;SF-2026-ARXIV-2605-25673;SF-2026-ARXIV-2605-25674;SF-2026-ARXIV-2605-25682;SF-2026-ARXIV-2605-25698;SF-2026-ARXIV-2605-25707;SF-2026-ARXIV-2605-25716;SF-2026-ARXIV-2605-25745;SF-2026-ARXIV-2605-25746;SF-2026-ARXIV-2605-25798;SF-2026-ARXIV-2605-25815;SF-2026-ARXIV-2605-25819;SF-2026-ARXIV-2605-25820;SF-2026-ARXIV-2605-25831;SF-2026-ARXIV-2605-25854;SF-2026-ARXIV-2605-25869;SF-2026-ARXIV-2605-25874;SF-2026-ARXIV-2605-25889;SF-2026-ARXIV-2605-25893;SF-2026-ARXIV-2605-25966;SF-2026-ARXIV-2605-25971;SF-2026-ARXIV-2605-25988;SF-2026-ARXIV-2605-25997;SF-2026-ARXIV-2605-26029;SF-2026-ARXIV-2605-26037;SF-2026-ARXIV-2605-26045;SF-2026-ARXIV-2605-26046;SF-2026-ARXIV-2605-26047;SF-2026-ARXIV-2605-26079;SF-2026-ARXIV-2605-26110;SF-2026-ARXIV-2605-26112;SF-2026-ARXIV-2605-26114;SF-AERIC-ANTICIPATORY-HIDDEN-STATE-MONITORING-FOR-IMPLICIT-HARMFUL-DIALOGUE;SF-FAITHFUL-OR-FABRICATED-A-CAUSAL-FRAMEWORK-FOR-RATIONALIZATION-BIAS-IN-LL;SF-LGMT-LOGIC-GROUNDED-METAMORPHIC-TESTING-FOR-EVALUATING-THE-REASONING-REL;SF-STOP-COMPARING-LLM-AGENTS-WITHOUT-DISCLOSING-THE-HARNESS | created-day pages=closed; OAI category sets=closed; direct same-day OAI=931 | 2026-05-26T09:00:00+08:00 | coverage:SRC-ARXIV:20260526 | — |

<!-- coverage:SRC-ARXIV:20260526:start -->全量 raw inventory=1208；每个 identity 均具有 retained、family-specific closure 或 withdrawn terminal closure。候选 owner 由 initial DataCite created、arXiv ID month、v1 history 与 announcement cadence 共同约束；冲突不由 updated 字段覆盖。<!-- coverage:SRC-ARXIV:20260526:end -->

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
| SF-2026-ARXIV-2605-23911 | arXiv:2605.23911v1 | paper-v1:2605.23911 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-23911 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23911 | yes |
| SF-2026-ARXIV-2605-23918 | arXiv:2605.23918v1 | paper-v1:2605.23918 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 2 | 3 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-23918 | self | — | new_in_window | PLATFORM-COST | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23918 | yes |
| SF-2026-ARXIV-2605-23935 | arXiv:2605.23935v1 | paper-v1:2605.23935 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-23935 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23935 | yes |
| SF-2026-ARXIV-2605-23945 | arXiv:2605.23945v1 | paper-v1:2605.23945 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-23945 | self | — | new_in_window | TRAIN-TENSOR-PARALLEL | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23945 | yes |
| SF-2026-ARXIV-2605-23951 | arXiv:2605.23951v1 | paper-v1:2605.23951 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-23951 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23951 | no |
| SF-2026-ARXIV-2605-23956 | arXiv:2605.23956v1 | paper-v1:2605.23956 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-23956 | self | — | new_in_window | WORLDVIEW-SYSTEM-EVOLUTION | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23956 | no |
| SF-2026-ARXIV-2605-23986 | arXiv:2605.23986v1 | paper-v1:2605.23986 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-23986 | self | — | new_in_window | AGENT-MEMORY | Integrate | books-review:SF-2026-ARXIV-2605-23986 | no |
| SF-2026-ARXIV-2605-23988 | arXiv:2605.23988v1 | paper-v1:2605.23988 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-23988 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Integrate | books-review:SF-2026-ARXIV-2605-23988 | no |
| SF-2026-ARXIV-2605-23993 | arXiv:2605.23993v1 | paper-v1:2605.23993 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-23993 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23993 | no |
| SF-2026-ARXIV-2605-24004 | arXiv:2605.24004v1 | paper-v1:2605.24004 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24004 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Integrate | books-review:SF-2026-ARXIV-2605-24004 | no |
| SF-2026-ARXIV-2605-24006 | arXiv:2605.24006v1 | paper-v1:2605.24006 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24006 | self | — | new_in_window | TRAIN-PIPELINE-PARALLEL | Integrate | books-review:SF-2026-ARXIV-2605-24006 | no |
| SF-2026-ARXIV-2605-24022 | arXiv:2605.24022v1 | paper-v1:2605.24022 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24022 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24022 | no |
| SF-2026-ARXIV-2605-24036 | arXiv:2605.24036v1 | paper-v1:2605.24036 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24036 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24036 | no |
| SF-2026-ARXIV-2605-24042 | arXiv:2605.24042v1 | paper-v1:2605.24042 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24042 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2605-24042 | no |
| SF-2026-ARXIV-2605-24044 | arXiv:2605.24044v1 | paper-v1:2605.24044 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24044 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24044 | no |
| SF-2026-ARXIV-2605-24050 | arXiv:2605.24050v1 | paper-v1:2605.24050 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24050 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24050 | no |
| SF-2026-ARXIV-2605-24060 | arXiv:2605.24060v1 | paper-v1:2605.24060 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24060 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24060 | no |
| SF-2026-ARXIV-2605-24069 | arXiv:2605.24069v1 | paper-v1:2605.24069 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24069 | self | — | new_in_window | AGENT-MCP | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24069 | no |
| SF-2026-ARXIV-2605-24117 | arXiv:2605.24117v1 | paper-v1:2605.24117 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24117 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24117 | no |
| SF-2026-ARXIV-2605-24134 | arXiv:2605.24134v1 | paper-v1:2605.24134 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24134 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24134 | no |
| SF-2026-ARXIV-2605-24154 | arXiv:2605.24154v1 | paper-v1:2605.24154 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24154 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24154 | no |
| SF-2026-ARXIV-2605-24168 | arXiv:2605.24168v1 | paper-v1:2605.24168 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24168 | self | — | new_in_window | AGENT-CONTEXT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24168 | no |
| SF-2026-ARXIV-2605-24183 | arXiv:2605.24183v1 | paper-v1:2605.24183 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24183 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24183 | no |
| SF-2026-ARXIV-2605-24197 | arXiv:2605.24197v1 | paper-v1:2605.24197 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24197 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24197 | no |
| SF-2026-ARXIV-2605-24202 | arXiv:2605.24202v1 | paper-v1:2605.24202 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24202 | self | — | new_in_window | TRAIN-RLHF | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24202 | no |
| SF-2026-ARXIV-2605-24213 | arXiv:2605.24213v1 | paper-v1:2605.24213 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24213 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24213 | no |
| SF-2026-ARXIV-2605-24216 | arXiv:2605.24216v1 | paper-v1:2605.24216 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24216 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24216 | no |
| SF-2026-ARXIV-2605-24217 | arXiv:2605.24217v1 | paper-v1:2605.24217 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24217 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2605-24217 | no |
| SF-2026-ARXIV-2605-24219 | arXiv:2605.24219v1 | paper-v1:2605.24219 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24219 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24219 | no |
| SF-2026-ARXIV-2605-24220 | arXiv:2605.24220v1 | paper-v1:2605.24220 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24220 | self | — | new_in_window | TRAIN-RLHF | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24220 | no |
| SF-2026-ARXIV-2605-24229 | arXiv:2605.24229v1 | paper-v1:2605.24229 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24229 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2605-24229 | no |
| SF-2026-ARXIV-2605-24245 | arXiv:2605.24245v1 | paper-v1:2605.24245 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24245 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24245 | no |
| SF-2026-ARXIV-2605-24247 | arXiv:2605.24247v1 | paper-v1:2605.24247 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24247 | self | — | new_in_window | TRAIN-DATA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24247 | no |
| SF-2026-ARXIV-2605-24248 | arXiv:2605.24248v1 | paper-v1:2605.24248 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24248 | self | — | new_in_window | AGENT-MCP | Integrate | books-review:SF-2026-ARXIV-2605-24248 | no |
| SF-2026-ARXIV-2605-24259 | arXiv:2605.24259v1 | paper-v1:2605.24259 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24259 | self | — | new_in_window | INFER-KV-CACHE | Integrate | books-review:SF-2026-ARXIV-2605-24259 | no |
| SF-2026-ARXIV-2605-24279 | arXiv:2605.24279v1 | paper-v1:2605.24279 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24279 | self | — | new_in_window | AGENT-CONTEXT | Integrate | books-review:SF-2026-ARXIV-2605-24279 | no |
| SF-2026-ARXIV-2605-24286 | arXiv:2605.24286v1 | paper-v1:2605.24286 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24286 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24286 | no |
| SF-2026-ARXIV-2605-24299 | arXiv:2605.24299v1 | paper-v1:2605.24299 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24299 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24299 | no |
| SF-2026-ARXIV-2605-24309 | arXiv:2605.24309v1 | paper-v1:2605.24309 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24309 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24309 | no |
| SF-2026-ARXIV-2605-24312 | arXiv:2605.24312v1 | paper-v1:2605.24312 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24312 | self | — | new_in_window | AGENT-RAG | Integrate | books-review:SF-2026-ARXIV-2605-24312 | no |
| SF-2026-ARXIV-2605-24326 | arXiv:2605.24326v1 | paper-v1:2605.24326 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24326 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24326 | no |
| SF-2026-ARXIV-2605-24391 | arXiv:2605.24391v1 | paper-v1:2605.24391 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24391 | self | — | new_in_window | INFER-TENSORRT-LLM | Integrate | books-review:SF-2026-ARXIV-2605-24391 | no |
| SF-2026-ARXIV-2605-24420 | arXiv:2605.24420v1 | paper-v1:2605.24420 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24420 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2605-24420 | no |
| SF-2026-ARXIV-2605-24421 | arXiv:2605.24421v1 | paper-v1:2605.24421 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24421 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2605-24421 | no |
| SF-2026-ARXIV-2605-24425 | arXiv:2605.24425v1 | paper-v1:2605.24425 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24425 | self | — | new_in_window | MODEL-TRANSFORMER-LAYER | Integrate | books-review:SF-2026-ARXIV-2605-24425 | no |
| SF-2026-ARXIV-2605-24426 | arXiv:2605.24426v1 | paper-v1:2605.24426 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24426 | self | — | new_in_window | TRAIN-RLHF | Integrate | books-review:SF-2026-ARXIV-2605-24426 | no |
| SF-2026-ARXIV-2605-24461 | arXiv:2605.24461v1 | paper-v1:2605.24461 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24461 | self | — | new_in_window | PLATFORM-GPU-SCHEDULER | Integrate | books-review:SF-2026-ARXIV-2605-24461 | no |
| SF-2026-ARXIV-2605-24468 | arXiv:2605.24468v1 | paper-v1:2605.24468 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24468 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24468 | no |
| SF-2026-ARXIV-2605-24517 | arXiv:2605.24517v1 | paper-v1:2605.24517 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24517 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24517 | no |
| SF-2026-ARXIV-2605-24547 | arXiv:2605.24547v1 | paper-v1:2605.24547 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24547 | self | — | new_in_window | TRAIN-RLHF | Integrate | books-review:SF-2026-ARXIV-2605-24547 | no |
| SF-2026-ARXIV-2605-24558 | arXiv:2605.24558v1 | paper-v1:2605.24558 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24558 | self | — | new_in_window | TRAIN-DATA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24558 | no |
| SF-2026-ARXIV-2605-24579 | arXiv:2605.24579v1 | paper-v1:2605.24579 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24579 | self | — | new_in_window | AGENT-MEMORY | Integrate | books-review:SF-2026-ARXIV-2605-24579 | no |
| SF-2026-ARXIV-2605-24583 | arXiv:2605.24583v1 | paper-v1:2605.24583 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24583 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2605-24583 | no |
| SF-2026-ARXIV-2605-24598 | arXiv:2605.24598v1 | paper-v1:2605.24598 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24598 | self | — | new_in_window | AGENT-MULTI-AGENT | Integrate | books-review:SF-2026-ARXIV-2605-24598 | no |
| SF-2026-ARXIV-2605-24614 | arXiv:2605.24614v1 | paper-v1:2605.24614 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24614 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24614 | no |
| SF-2026-ARXIV-2605-24619 | arXiv:2605.24619v1 | paper-v1:2605.24619 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24619 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24619 | no |
| SF-2026-ARXIV-2605-24657 | arXiv:2605.24657v1 | paper-v1:2605.24657 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24657 | self | — | new_in_window | AGENT-CONTEXT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24657 | no |
| SF-2026-ARXIV-2605-24659 | arXiv:2605.24659v1 | paper-v1:2605.24659 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24659 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24659 | no |
| SF-2026-ARXIV-2605-24660 | arXiv:2605.24660v1 | paper-v1:2605.24660 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24660 | self | — | new_in_window | AGENT-TOOL-CALLING | Integrate | books-review:SF-2026-ARXIV-2605-24660 | no |
| SF-2026-ARXIV-2605-24661 | arXiv:2605.24661v1 | paper-v1:2605.24661 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24661 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24661 | no |
| SF-2026-ARXIV-2605-24662 | arXiv:2605.24662v1 | paper-v1:2605.24662 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24662 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24662 | no |
| SF-2026-ARXIV-2605-24667 | arXiv:2605.24667v1 | paper-v1:2605.24667 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24667 | self | — | new_in_window | TRAIN-PRETRAINING | Integrate | books-review:SF-2026-ARXIV-2605-24667 | no |
| SF-2026-ARXIV-2605-24683 | arXiv:2605.24683v1 | paper-v1:2605.24683 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24683 | self | — | new_in_window | PLATFORM-MONITORING | Integrate | books-review:SF-2026-ARXIV-2605-24683 | no |
| SF-2026-ARXIV-2605-24697 | arXiv:2605.24697v1 | paper-v1:2605.24697 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24697 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | Integrate | books-review:SF-2026-ARXIV-2605-24697 | no |
| SF-2026-ARXIV-2605-24709 | arXiv:2605.24709v1 | paper-v1:2605.24709 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24709 | self | — | new_in_window | TRAIN-RLHF | Integrate | books-review:SF-2026-ARXIV-2605-24709 | no |
| SF-2026-ARXIV-2605-24727 | arXiv:2605.24727v1 | paper-v1:2605.24727 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24727 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2605-24727 | no |
| SF-2026-ARXIV-2605-24728 | arXiv:2605.24728v1 | paper-v1:2605.24728 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24728 | self | — | new_in_window | — | Structural Candidate | books-review:SF-2026-ARXIV-2605-24728 | no |
| SF-2026-ARXIV-2605-24733 | arXiv:2605.24733v1 | paper-v1:2605.24733 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24733 | self | — | new_in_window | AGENT-REFLECTION | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24733 | no |
| SF-2026-ARXIV-2605-24737 | arXiv:2605.24737v1 | paper-v1:2605.24737 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24737 | self | — | new_in_window | PLATFORM-MONITORING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24737 | no |
| SF-2026-ARXIV-2605-24743 | arXiv:2605.24743v1 | paper-v1:2605.24743 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24743 | self | — | new_in_window | TRAIN-DATA | Integrate | books-review:SF-2026-ARXIV-2605-24743 | no |
| SF-2026-ARXIV-2605-24749 | arXiv:2605.24749v1 | paper-v1:2605.24749 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24749 | self | — | new_in_window | TRAIN-RLHF | Integrate | books-review:SF-2026-ARXIV-2605-24749 | no |
| SF-2026-ARXIV-2605-24756 | arXiv:2605.24756v1 | paper-v1:2605.24756 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24756 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2605-24756 | no |
| SF-2026-ARXIV-2605-24770 | arXiv:2605.24770v1 | paper-v1:2605.24770 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24770 | self | — | new_in_window | TRAIN-PRETRAINING | Integrate | books-review:SF-2026-ARXIV-2605-24770 | no |
| SF-2026-ARXIV-2605-24775 | arXiv:2605.24775v1 | paper-v1:2605.24775 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24775 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24775 | no |
| SF-2026-ARXIV-2605-24785 | arXiv:2605.24785v1 | paper-v1:2605.24785 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24785 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24785 | no |
| SF-2026-ARXIV-2605-24786 | arXiv:2605.24786v1 | paper-v1:2605.24786 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24786 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24786 | no |
| SF-2026-ARXIV-2605-24793 | arXiv:2605.24793v1 | paper-v1:2605.24793 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24793 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | Integrate | books-review:SF-2026-ARXIV-2605-24793 | no |
| SF-2026-ARXIV-2605-24817 | arXiv:2605.24817v1 | paper-v1:2605.24817 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24817 | self | — | new_in_window | PLATFORM-MONITORING | Integrate | books-review:SF-2026-ARXIV-2605-24817 | no |
| SF-2026-ARXIV-2605-24818 | arXiv:2605.24818v1 | paper-v1:2605.24818 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24818 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2605-24818 | no |
| SF-2026-ARXIV-2605-24823 | arXiv:2605.24823v1 | paper-v1:2605.24823 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24823 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24823 | no |
| SF-2026-ARXIV-2605-24832 | arXiv:2605.24832v1 | paper-v1:2605.24832 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24832 | self | — | new_in_window | INFER-TENSORRT-LLM | Integrate | books-review:SF-2026-ARXIV-2605-24832 | no |
| SF-2026-ARXIV-2605-24870 | arXiv:2605.24870v1 | paper-v1:2605.24870 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24870 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | Integrate | books-review:SF-2026-ARXIV-2605-24870 | no |
| SF-2026-ARXIV-2605-24879 | arXiv:2605.24879v1 | paper-v1:2605.24879 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24879 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2605-24879 | no |
| SF-2026-ARXIV-2605-24883 | arXiv:2605.24883v1 | paper-v1:2605.24883 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24883 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2605-24883 | no |
| SF-2026-ARXIV-2605-24892 | arXiv:2605.24892v1 | paper-v1:2605.24892 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24892 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24892 | no |
| SF-2026-ARXIV-2605-24914 | arXiv:2605.24914v1 | paper-v1:2605.24914 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24914 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24914 | no |
| SF-2026-ARXIV-2605-24922 | arXiv:2605.24922v1 | paper-v1:2605.24922 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24922 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Integrate | books-review:SF-2026-ARXIV-2605-24922 | no |
| SF-2026-ARXIV-2605-24930 | arXiv:2605.24930v1 | paper-v1:2605.24930 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24930 | self | — | new_in_window | MODEL-LONG-CONTEXT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24930 | no |
| SF-2026-ARXIV-2605-24941 | arXiv:2605.24941v1 | paper-v1:2605.24941 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24941 | self | — | new_in_window | AGENT-TOOL-CALLING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24941 | no |
| SF-2026-ARXIV-2605-24973 | arXiv:2605.24973v1 | paper-v1:2605.24973 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24973 | self | — | new_in_window | AGENT-RAG | Integrate | books-review:SF-2026-ARXIV-2605-24973 | no |
| SF-2026-ARXIV-2605-25002 | arXiv:2605.25002v1 | paper-v1:2605.25002 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-25002 | self | — | new_in_window | AGENT-MEMORY | Integrate | books-review:SF-2026-ARXIV-2605-25002 | no |
| SF-2026-ARXIV-2605-25052 | arXiv:2605.25052v1 | paper-v1:2605.25052 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-25052 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25052 | no |
| SF-2026-ARXIV-2605-25073 | arXiv:2605.25073v1 | paper-v1:2605.25073 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-25073 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25073 | no |
| SF-2026-ARXIV-2605-25077 | arXiv:2605.25077v1 | paper-v1:2605.25077 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-25077 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25077 | no |
| SF-2026-ARXIV-2605-25085 | arXiv:2605.25085v1 | paper-v1:2605.25085 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-25085 | self | — | new_in_window | INFER-KV-CACHE | Integrate | books-review:SF-2026-ARXIV-2605-25085 | no |
| SF-2026-ARXIV-2605-25092 | arXiv:2605.25092v1 | paper-v1:2605.25092 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-25092 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25092 | no |
| SF-2026-ARXIV-2605-25133 | arXiv:2605.25133v1 | paper-v1:2605.25133 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-25133 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25133 | no |
| SF-2026-ARXIV-2605-25160 | arXiv:2605.25160v1 | paper-v1:2605.25160 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-25160 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25160 | no |
| SF-2026-ARXIV-2605-25188 | arXiv:2605.25188v1 | paper-v1:2605.25188 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-25188 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25188 | no |
| SF-2026-ARXIV-2605-25189 | arXiv:2605.25189v1 | paper-v1:2605.25189 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-25189 | self | — | new_in_window | TRAIN-RLHF | Integrate | books-review:SF-2026-ARXIV-2605-25189 | no |
| SF-2026-ARXIV-2605-25233 | arXiv:2605.25233v1 | paper-v1:2605.25233 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-25233 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25233 | no |
| SF-2026-ARXIV-2605-25240 | arXiv:2605.25240v1 | paper-v1:2605.25240 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-25240 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2605-25240 | no |
| SF-2026-ARXIV-2605-25244 | arXiv:2605.25244v1 | paper-v1:2605.25244 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-25244 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25244 | no |
| SF-2026-ARXIV-2605-25247 | arXiv:2605.25247v1 | paper-v1:2605.25247 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-25247 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25247 | no |
| SF-2026-ARXIV-2605-25252 | arXiv:2605.25252v1 | paper-v1:2605.25252 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-25252 | self | — | new_in_window | TRAIN-RLHF | Integrate | books-review:SF-2026-ARXIV-2605-25252 | no |
| SF-2026-ARXIV-2605-25272 | arXiv:2605.25272v1 | paper-v1:2605.25272 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-25272 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2605-25272 | no |
| SF-2026-ARXIV-2605-25284 | arXiv:2605.25284v1 | paper-v1:2605.25284 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-25284 | self | — | new_in_window | AGENT-PLANNING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25284 | no |
| SF-2026-ARXIV-2605-25292 | arXiv:2605.25292v1 | paper-v1:2605.25292 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-25292 | self | — | new_in_window | PLATFORM-GPU-SCHEDULER | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25292 | no |
| SF-2026-ARXIV-2605-25298 | arXiv:2605.25298v1 | paper-v1:2605.25298 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-25298 | self | — | new_in_window | PLATFORM-MONITORING | Integrate | books-review:SF-2026-ARXIV-2605-25298 | no |
| SF-2026-ARXIV-2605-25310 | arXiv:2605.25310v1 | paper-v1:2605.25310 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 2 | 2 | 1 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2605-25310 | self | — | new_in_window | AGENT-TOOL-CALLING | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2605-25313 | arXiv:2605.25313v1 | paper-v1:2605.25313 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-25313 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25313 | no |
| SF-2026-ARXIV-2605-25338 | arXiv:2605.25338v1 | paper-v1:2605.25338 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-25338 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25338 | no |
| SF-2026-ARXIV-2605-25375 | arXiv:2605.25375v1 | paper-v1:2605.25375 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-25375 | self | — | new_in_window | TRAIN-PIPELINE-PARALLEL | Integrate | books-review:SF-2026-ARXIV-2605-25375 | no |
| SF-2026-ARXIV-2605-25376 | arXiv:2605.25376v1 | paper-v1:2605.25376 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-25376 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25376 | no |
| SF-2026-ARXIV-2605-25379 | arXiv:2605.25379v1 | paper-v1:2605.25379 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-25379 | self | — | new_in_window | AGENT-RAG | Integrate | books-review:SF-2026-ARXIV-2605-25379 | no |
| SF-2026-ARXIV-2605-25389 | arXiv:2605.25389v1 | paper-v1:2605.25389 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-25389 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25389 | no |
| SF-2026-ARXIV-2605-25421 | arXiv:2605.25421v1 | paper-v1:2605.25421 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-25421 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25421 | no |
| SF-2026-ARXIV-2605-25422 | arXiv:2605.25422v1 | paper-v1:2605.25422 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-25422 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25422 | no |
| SF-2026-ARXIV-2605-25424 | arXiv:2605.25424v1 | paper-v1:2605.25424 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-25424 | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-2026-ARXIV-2605-25424 | no |
| SF-2026-ARXIV-2605-25430 | arXiv:2605.25430v1 | paper-v1:2605.25430 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-25430 | self | — | new_in_window | AGENT-PLATFORM | Integrate | books-review:SF-2026-ARXIV-2605-25430 | no |
| SF-2026-ARXIV-2605-25451 | arXiv:2605.25451v1 | paper-v1:2605.25451 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-25451 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25451 | no |
| SF-2026-ARXIV-2605-25475 | arXiv:2605.25475v1 | paper-v1:2605.25475 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-25475 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25475 | no |
| SF-2026-ARXIV-2605-25492 | arXiv:2605.25492v1 | paper-v1:2605.25492 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-25492 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2605-25492 | no |
| SF-2026-ARXIV-2605-25507 | arXiv:2605.25507v1 | paper-v1:2605.25507 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-25507 | self | — | new_in_window | TRAIN-PPO | Integrate | books-review:SF-2026-ARXIV-2605-25507 | no |
| SF-2026-ARXIV-2605-25521 | arXiv:2605.25521v1 | paper-v1:2605.25521 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-25521 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25521 | no |
| SF-2026-ARXIV-2605-25535 | arXiv:2605.25535v1 | paper-v1:2605.25535 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-25535 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25535 | no |
| SF-2026-ARXIV-2605-25537 | arXiv:2605.25537v1 | paper-v1:2605.25537 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-25537 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25537 | no |
| SF-2026-ARXIV-2605-25547 | arXiv:2605.25547v1 | paper-v1:2605.25547 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-25547 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25547 | no |
| SF-2026-ARXIV-2605-25550 | arXiv:2605.25550v1 | paper-v1:2605.25550 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-25550 | self | — | new_in_window | INFER-PD-DISAGGREGATION | Integrate | books-review:SF-2026-ARXIV-2605-25550 | no |
| SF-2026-ARXIV-2605-25621 | arXiv:2605.25621v1 | paper-v1:2605.25621 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-25621 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25621 | no |
| SF-2026-ARXIV-2605-25624 | arXiv:2605.25624v1 | paper-v1:2605.25624 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-25624 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25624 | no |
| SF-2026-ARXIV-2605-25632 | arXiv:2605.25632v1 | paper-v1:2605.25632 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-25632 | self | — | new_in_window | AGENT-TOOL-CALLING | Integrate | books-review:SF-2026-ARXIV-2605-25632 | no |
| SF-2026-ARXIV-2605-25641 | arXiv:2605.25641v1 | paper-v1:2605.25641 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-25641 | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25641 | no |
| SF-2026-ARXIV-2605-25653 | arXiv:2605.25653v1 | paper-v1:2605.25653 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-25653 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25653 | no |
| SF-2026-ARXIV-2605-25655 | arXiv:2605.25655v1 | paper-v1:2605.25655 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-25655 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25655 | no |
| SF-2026-ARXIV-2605-25673 | arXiv:2605.25673v1 | paper-v1:2605.25673 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-25673 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2605-25673 | no |
| SF-2026-ARXIV-2605-25674 | arXiv:2605.25674v1 | paper-v1:2605.25674 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-25674 | self | — | new_in_window | PLATFORM-MONITORING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25674 | no |
| SF-2026-ARXIV-2605-25682 | arXiv:2605.25682v1 | paper-v1:2605.25682 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-25682 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25682 | no |
| SF-2026-ARXIV-2605-25698 | arXiv:2605.25698v1 | paper-v1:2605.25698 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-25698 | self | — | new_in_window | TRAIN-DATA | Integrate | books-review:SF-2026-ARXIV-2605-25698 | no |
| SF-2026-ARXIV-2605-25707 | arXiv:2605.25707v1 | paper-v1:2605.25707 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-25707 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25707 | no |
| SF-2026-ARXIV-2605-25716 | arXiv:2605.25716v1 | paper-v1:2605.25716 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-25716 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25716 | no |
| SF-2026-ARXIV-2605-25745 | arXiv:2605.25745v1 | paper-v1:2605.25745 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-25745 | self | — | new_in_window | MODEL-DECODER-ONLY | Integrate | books-review:SF-2026-ARXIV-2605-25745 | no |
| SF-2026-ARXIV-2605-25746 | arXiv:2605.25746v1 | paper-v1:2605.25746 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-25746 | self | — | new_in_window | AGENT-MULTI-AGENT | Integrate | books-review:SF-2026-ARXIV-2605-25746 | no |
| SF-2026-ARXIV-2605-25798 | arXiv:2605.25798v1 | paper-v1:2605.25798 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-25798 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25798 | no |
| SF-2026-ARXIV-2605-25815 | arXiv:2605.25815v1 | paper-v1:2605.25815 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-25815 | self | — | new_in_window | AGENT-PLATFORM | Integrate | books-review:SF-2026-ARXIV-2605-25815 | no |
| SF-2026-ARXIV-2605-25819 | arXiv:2605.25819v1 | paper-v1:2605.25819 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-25819 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2605-25819 | no |
| SF-2026-ARXIV-2605-25820 | arXiv:2605.25820v1 | paper-v1:2605.25820 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-25820 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25820 | no |
| SF-2026-ARXIV-2605-25831 | arXiv:2605.25831v1 | paper-v1:2605.25831 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-25831 | self | — | new_in_window | AGENT-REFLECTION | Integrate | books-review:SF-2026-ARXIV-2605-25831 | no |
| SF-2026-ARXIV-2605-25854 | arXiv:2605.25854v1 | paper-v1:2605.25854 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-25854 | self | — | new_in_window | PLATFORM-COST | Integrate | books-review:SF-2026-ARXIV-2605-25854 | no |
| SF-2026-ARXIV-2605-25869 | arXiv:2605.25869v1 | paper-v1:2605.25869 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-25869 | self | — | new_in_window | AGENT-MEMORY | Integrate | books-review:SF-2026-ARXIV-2605-25869 | no |
| SF-2026-ARXIV-2605-25874 | arXiv:2605.25874v1 | paper-v1:2605.25874 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-25874 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25874 | no |
| SF-2026-ARXIV-2605-25889 | arXiv:2605.25889v1 | paper-v1:2605.25889 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-25889 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Integrate | books-review:SF-2026-ARXIV-2605-25889 | no |
| SF-2026-ARXIV-2605-25893 | arXiv:2605.25893v1 | paper-v1:2605.25893 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-25893 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2605-25893 | no |
| SF-2026-ARXIV-2605-25966 | arXiv:2605.25966v1 | paper-v1:2605.25966 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-25966 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25966 | no |
| SF-2026-ARXIV-2605-25971 | arXiv:2605.25971v1 | paper-v1:2605.25971 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-25971 | self | — | new_in_window | AGENT-PLATFORM | Integrate | books-review:SF-2026-ARXIV-2605-25971 | no |
| SF-2026-ARXIV-2605-25988 | arXiv:2605.25988v1 | paper-v1:2605.25988 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-25988 | self | — | new_in_window | AGENT-RAG | Integrate | books-review:SF-2026-ARXIV-2605-25988 | no |
| SF-2026-ARXIV-2605-25997 | arXiv:2605.25997v1 | paper-v1:2605.25997 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-25997 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2605-25997 | no |
| SF-2026-ARXIV-2605-26029 | arXiv:2605.26029v1 | paper-v1:2605.26029 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-26029 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26029 | no |
| SF-2026-ARXIV-2605-26037 | arXiv:2605.26037v1 | paper-v1:2605.26037 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-26037 | self | — | new_in_window | TRAIN-GRPO | Integrate | books-review:SF-2026-ARXIV-2605-26037 | no |
| SF-2026-ARXIV-2605-26045 | arXiv:2605.26045v1 | paper-v1:2605.26045 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-26045 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2605-26045 | no |
| SF-2026-ARXIV-2605-26046 | arXiv:2605.26046v1 | paper-v1:2605.26046 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-26046 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26046 | no |
| SF-2026-ARXIV-2605-26047 | arXiv:2605.26047v1 | paper-v1:2605.26047 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-26047 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2605-26047 | no |
| SF-2026-ARXIV-2605-26079 | arXiv:2605.26079v1 | paper-v1:2605.26079 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-26079 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26079 | no |
| SF-2026-ARXIV-2605-26110 | arXiv:2605.26110v1 | paper-v1:2605.26110 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-26110 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26110 | no |
| SF-2026-ARXIV-2605-26112 | arXiv:2605.26112v1 | paper-v1:2605.26112 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-26112 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26112 | no |
| SF-2026-ARXIV-2605-26114 | arXiv:2605.26114v1 | paper-v1:2605.26114 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-26114 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26114 | no |
| SF-AERIC-ANTICIPATORY-HIDDEN-STATE-MONITORING-FOR-IMPLICIT-HARMFUL-DIALOGUE | arXiv:2605.23974v1 | paper-v1:2605.23974 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-AERIC-ANTICIPATORY-HIDDEN-STATE-MONITORING-FOR-IMPLICIT-HARMFUL-DIALOGUE | self | — | new_in_window | PLATFORM-MONITORING | Integrate | books-review:SF-AERIC-ANTICIPATORY-HIDDEN-STATE-MONITORING-FOR-IMPLICIT-HARMFUL-DIALOGUE | no |
| SF-FAITHFUL-OR-FABRICATED-A-CAUSAL-FRAMEWORK-FOR-RATIONALIZATION-BIAS-IN-LL | arXiv:2605.23970v1 | paper-v1:2605.23970 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-FAITHFUL-OR-FABRICATED-A-CAUSAL-FRAMEWORK-FOR-RATIONALIZATION-BIAS-IN-LL | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-FAITHFUL-OR-FABRICATED-A-CAUSAL-FRAMEWORK-FOR-RATIONALIZATION-BIAS-IN-LL | no |
| SF-LGMT-LOGIC-GROUNDED-METAMORPHIC-TESTING-FOR-EVALUATING-THE-REASONING-REL | arXiv:2605.23965v1 | paper-v1:2605.23965 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-LGMT-LOGIC-GROUNDED-METAMORPHIC-TESTING-FOR-EVALUATING-THE-REASONING-REL | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-LGMT-LOGIC-GROUNDED-METAMORPHIC-TESTING-FOR-EVALUATING-THE-REASONING-REL | no |
| SF-STOP-COMPARING-LLM-AGENTS-WITHOUT-DISCLOSING-THE-HARNESS | arXiv:2605.23950v1 | paper-v1:2605.23950 | 2026-W22 | 2026-05-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-STOP-COMPARING-LLM-AGENTS-WITHOUT-DISCLOSING-THE-HARNESS | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-STOP-COMPARING-LLM-AGENTS-WITHOUT-DISCLOSING-THE-HARNESS | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-23911 | RP-e4f64588fd34964d | deep | arXiv:2605.23911v1 | SRC-ARXIV@arXiv:2605.23911v1 | https://arxiv.org/html/2605.23911v1#S2 | https://arxiv.org/html/2605.23911v1#S4 | https://arxiv.org/html/2605.23911v1#S6 | Not Disclosed — exact-v1 review found no versioned public artifact contract | claim:SF-2026-ARXIV-2605-23911 | complete |
| SF-2026-ARXIV-2605-23918 | RP-d810505bda471106 | deep | arXiv:2605.23918v1 | SRC-ARXIV@arXiv:2605.23918v1 | https://arxiv.org/html/2605.23918v1#S2 | https://arxiv.org/html/2605.23918v1#S4 | https://arxiv.org/html/2605.23918v1#S6 | Not Disclosed — exact-v1 review found no versioned public artifact contract | claim:SF-2026-ARXIV-2605-23918 | complete |
| SF-2026-ARXIV-2605-23935 | RP-2ecfb04410958793 | deep | arXiv:2605.23935v1 | SRC-ARXIV@arXiv:2605.23935v1 | https://arxiv.org/html/2605.23935v1#S2 | https://arxiv.org/html/2605.23935v1#S4 | https://arxiv.org/html/2605.23935v1#S6 | Not Disclosed — exact-v1 review found no versioned public artifact contract | claim:SF-2026-ARXIV-2605-23935 | complete |
| SF-2026-ARXIV-2605-23945 | RP-e9fd079d52d14105 | deep | arXiv:2605.23945v1 | SRC-ARXIV@arXiv:2605.23945v1 | https://arxiv.org/html/2605.23945v1 — § exact-v1 reviewer locator: §3 predictor-guided TP reconfiguration; §4 KV migration/recompute and weight reshard（全文读取 ref=turn11936view7） | https://arxiv.org/html/2605.23945v1 — § exact-v1 reviewer locator: §5 A40/H100 testbeds, Llama/Qwen with VeRL/SGLang（全文读取 ref=turn11936view7） | https://arxiv.org/html/2605.23945v1 — § exact-v1 reviewer locator: No dedicated limitations section; 8–16 GPU testbeds, offline profiles and synchronous pipelines do not establish fleet-scale stability or arbitrary topology gains.（全文读取 ref=turn11936view7） | Not Disclosed — exact v1 does not bind the claim to an immutable public experiment commit. | claim:SF-2026-ARXIV-2605-23945 | complete |
| SF-2026-ARXIV-2605-23951 | RP-8d7f744bbf216f42 | deep | arXiv:2605.23951v1 | SRC-ARXIV@arXiv:2605.23951v1 | https://arxiv.org/html/2605.23951v1 §3 Semantics; §4–§6 Three Verification Layers — mechanism: We give a precise semantics for skill behaviour faithful to how a skill is consumed by an LLM-driven runtime (a deterministic script-side reachable through a non-deterministic LLM-side), state the verification problem as a capability-containment property over that semantics, and present three composable methods that together raise… | https://arxiv.org/html/2605.23951v1 §8 Bundle Re-checker; §10 Threat Coverage — disclosed scope: The companion paper introduced a four-level verification lattice on agent-skill manifests (unverified, declared, tested, formal) and left the top level aspirational. This paper closes that gap. We give a precise semantics for skill behaviour faithful to how a skill is consumed by an LLM-driven runtime (a… | https://arxiv.org/html/2605.23951v1 §11 Scope and Residual LLM Refusal Boundary — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO | https://arxiv.org/html/2605.23951v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-23951 | complete |
| SF-2026-ARXIV-2605-23956 | RP-7714ccd432351b7e | deep | arXiv:2605.23956v1 | SRC-ARXIV@arXiv:2605.23956v1 | arXiv:2605.23956v1 §2 typed pipeline graph, type-dispatched distances, sensitivity matrix and loop bifurcation — We introduce QUIVER, a formal framework for measuring perturbation propagation in graph-structured LLM pipelines. | arXiv:2605.23956v1 §2.5 evaluation principles and estimation; framework case analyses | Not Disclosed — exact-v1 body was reviewed, but no stable numbered Limitations/Counterevidence fragment was exposed; reviewer boundary: arXiv:2605.23956v1 No controlled production validation; the formal model depends on chosen distance metrics and perturbation distributions | Not Disclosed — no immutable public artifact was identified in the reviewed exact-v1 body | claim:SF-2026-ARXIV-2605-23956 | complete |
| SF-2026-ARXIV-2605-23986 | RP-40ee91c88e737a85 | deep | arXiv:2605.23986v1 | SRC-ARXIV@arXiv:2605.23986v1 | section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt) | Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only | Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup | papers/2026/05/_sources/daily-20260517/exact-review-batch-f.txt#sha256=b5d6a0a2fd67c424c789e8fdee75b6523c7473081588f5eee6a221ecc4fafaff; exact-v1 URL=https://arxiv.org/html/2605.23986v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-23986 | complete |
| SF-2026-ARXIV-2605-23988 | RP-fc4f8fb00f24ce39 | deep | arXiv:2605.23988v1 | SRC-ARXIV@arXiv:2605.23988v1 | arXiv:2605.23988v1 — §II Architecture and Workflow; §III Token Compression (official exact-v1 HTML) | arXiv:2605.23988v1 — §VI Experiments (official exact-v1 HTML) | arXiv:2605.23988v1 — §VII Conclusion; no dedicated limitations section (official exact-v1 HTML) | exact-v1 URL=https://arxiv.org/html/2605.23988v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-23988 | complete |
| SF-2026-ARXIV-2605-23993 | RP-2aa525f1ee506fca | deep | arXiv:2605.23993v1 | SRC-ARXIV@arXiv:2605.23993v1 | arXiv:2605.23993v1 — §3 Diffusion-Forcing Interface and Experimental Substrate (official exact-v1 HTML) | arXiv:2605.23993v1 — §4 Findings (official exact-v1 HTML) | arXiv:2605.23993v1 — §5 Conclusion; no dedicated limitations section (official exact-v1 HTML) | exact-v1 URL=https://arxiv.org/html/2605.23993v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-23993 | complete |
| SF-2026-ARXIV-2605-24004 | RP-d1801b370072c775 | deep | arXiv:2605.24004v1 | SRC-ARXIV@arXiv:2605.24004v1 | arXiv:2605.24004v1 HTML — §III Reason–Imagine–Act world-model verification loop | arXiv:2605.24004v1 HTML — §IV CARLA closed-loop evaluation | arXiv:2605.24004v1 HTML — §V Conclusion; simulator and discrete-action-template boundary | https://arxiv.org/html/2605.24004v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-24004 | complete |
| SF-2026-ARXIV-2605-24006 | RP-a25cb3acf89adb37 | deep | arXiv:2605.24006v1 | SRC-ARXIV@arXiv:2605.24006v1 | arXiv:2605.24006v1 HTML — §III tabular schedule abstraction | arXiv:2605.24006v1 HTML — §IV communication-aware schedule experiments | arXiv:2605.24006v1 HTML — §V Conclusion and simulator boundary | https://arxiv.org/html/2605.24006v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-24006 | complete |
| SF-2026-ARXIV-2605-24022 | RP-b37dab8934926779 | deep | arXiv:2605.24022v1 | SRC-ARXIV@arXiv:2605.24022v1 | arXiv:2605.24022v1 HTML — §3 CacheTune Adaptive KV Reuse | arXiv:2605.24022v1 HTML — §5 Evaluation | arXiv:2605.24022v1 HTML — §5.5 Limitations; §6 Conclusion | https://arxiv.org/html/2605.24022v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-24022 | complete |
| SF-2026-ARXIV-2605-24036 | RP-6ab37dfed97a447d | deep | arXiv:2605.24036v1 | SRC-ARXIV@arXiv:2605.24036v1 | arXiv:2605.24036v1 HTML — §4 Intent-Driven Computational Model | arXiv:2605.24036v1 HTML — §8 Worked Governance Semantics | arXiv:2605.24036v1 HTML — §10 Limitations and Scope | https://arxiv.org/html/2605.24036v1; sha256:1eec7ae37f60c2236eeed917aec705e4224a2a0d518f318bc6a604a15c121a41 | claim:SF-2026-ARXIV-2605-24036 | complete |
| SF-2026-ARXIV-2605-24042 | RP-21bf9757b1a572fe | deep | arXiv:2605.24042v1 | SRC-ARXIV@arXiv:2605.24042v1 | arXiv:2605.24042v1 HTML — §3 Hidden-State Privacy Feasibility Regions | arXiv:2605.24042v1 HTML — §7–§8 Experimental Tests | arXiv:2605.24042v1 HTML — §9 Limitations and Future Questions | https://arxiv.org/html/2605.24042v1; sha256:570f86970a0df097c2ce9229704f9a83c3ae36eabf0b4361316eccbc058ae683 | claim:SF-2026-ARXIV-2605-24042 | complete |
| SF-2026-ARXIV-2605-24044 | RP-18f082e2b4a819b8 | deep | arXiv:2605.24044v1 | SRC-ARXIV@arXiv:2605.24044v1 | arXiv:2605.24044v1 HTML — §2.2 Challenges due to the MIMONet Architecture; §3 System Model and Problem Formulation; §3.4 Problem Formulation | arXiv:2605.24044v1 HTML — §5 Evaluation; §5.1 Experimental Setups; §5.5 Overhead Analysis | arXiv:2605.24044v1 HTML — §7 Discussion; §9 Conclusion | https://arxiv.org/html/2605.24044v1; sha256:d6cd3302598aa903e9c7200f7f725ca3747ced003157d0aecd07e5b6d92fc7de | claim:SF-2026-ARXIV-2605-24044 | complete |
| SF-2026-ARXIV-2605-24050 | RP-3d02110946596891 | deep | arXiv:2605.24050v1 | SRC-ARXIV@arXiv:2605.24050v1 | arXiv:2605.24050v1 HTML — §3 Skill-Shadowing Mechanism and Library Expansion Protocol | arXiv:2605.24050v1 HTML — §4 Evaluation | arXiv:2605.24050v1 HTML — §5 Conclusion and tested-library/model boundary | https://arxiv.org/html/2605.24050v1; sha256:bcb4f4766c6e6987b1c569b560bb4c19636dcab9eb9125d98e3ba5c8c5450002 | claim:SF-2026-ARXIV-2605-24050 | complete |
| SF-2026-ARXIV-2605-24060 | RP-53ca81da553bf549 | deep | arXiv:2605.24060v1 | SRC-ARXIV@arXiv:2605.24060v1 | https://arxiv.org/html/2605.24060v1 — §3 memory benchmark scoring-target intervention | https://arxiv.org/html/2605.24060v1 — §4–§5 controlled benchmark evaluation | https://arxiv.org/html/2605.24060v1 — §7 Limitations; tested-memory systems and tasks | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24060 | complete |
| SF-2026-ARXIV-2605-24069 | RP-edfc3e1a0860e2d4 | deep | arXiv:2605.24069v1 | SRC-ARXIV@arXiv:2605.24069v1 | https://arxiv.org/html/2605.24069v1 — §3 MCP Poisoning Threat Model and Benchmark | https://arxiv.org/html/2605.24069v1 — §4 Evaluation | https://arxiv.org/html/2605.24069v1 — §5 Limitations and manual/registry boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24069 | complete |
| SF-2026-ARXIV-2605-24117 | RP-1945ab82f7d8942d | deep | arXiv:2605.24117v1 | SRC-ARXIV@arXiv:2605.24117v1 | https://arxiv.org/html/2605.24117v1 — §3 SkillEvolBench lifecycle/evolution protocol | https://arxiv.org/html/2605.24117v1 — §4–§5 benchmark protocol and experiments | https://arxiv.org/html/2605.24117v1 — §6 Discussion; benchmark coverage does not prove deployment safety | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24117 | complete |
| SF-2026-ARXIV-2605-24134 | RP-e60e94ab77294bb7 | deep | arXiv:2605.24134v1 | SRC-ARXIV@arXiv:2605.24134v1 | https://arxiv.org/html/2605.24134v1 — §3 ProofAgent Harness Architecture | https://arxiv.org/html/2605.24134v1 — §5 Adversarial Agent Evaluation | https://arxiv.org/html/2605.24134v1 — §6 Limitations and proof-domain boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24134 | complete |
| SF-2026-ARXIV-2605-24154 | RP-e0c811bb34fd8177 | deep | arXiv:2605.24154v1 | SRC-ARXIV@arXiv:2605.24154v1 | https://arxiv.org/html/2605.24154v1 — §3 Palette Authorized Safety-Relaxation Modules | https://arxiv.org/html/2605.24154v1 — §5 Safety/Utility Evaluation | https://arxiv.org/html/2605.24154v1 — §6 Limitations and authorization boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24154 | complete |
| SF-2026-ARXIV-2605-24168 | RP-7d918c661cf20669 | deep | arXiv:2605.24168v1 | SRC-ARXIV@arXiv:2605.24168v1 | https://arxiv.org/html/2605.24168v1 — §3 Inference-Time Context-Sparsity Analysis | https://arxiv.org/html/2605.24168v1 — §4 Evaluation | https://arxiv.org/html/2605.24168v1 — §5 Discussion and model/task boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24168 | complete |
| SF-2026-ARXIV-2605-24183 | RP-c3fa6cd87b633384 | deep | arXiv:2605.24183v1 | SRC-ARXIV@arXiv:2605.24183v1 | https://arxiv.org/html/2605.24183v1 — §2–§3 AvalancheBench latent-world recovery protocol | https://arxiv.org/html/2605.24183v1 — §4 early experiments | https://arxiv.org/html/2605.24183v1 — §5 Limitations; synthetic/latent-world scope | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24183 | complete |
| SF-2026-ARXIV-2605-24197 | RP-7014a32fa7fb0410 | deep | arXiv:2605.24197v1 | SRC-ARXIV@arXiv:2605.24197v1 | https://arxiv.org/html/2605.24197v1 — §3 formulation; §4 evidence-attribution mechanism | https://arxiv.org/html/2605.24197v1 — §5 experiments | https://arxiv.org/html/2605.24197v1 — Appendix B Limitations; simulated-agent and attribution boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24197 | complete |
| SF-2026-ARXIV-2605-24202 | RP-4930f30a517dca9e | deep | arXiv:2605.24202v1 | SRC-ARXIV@arXiv:2605.24202v1 | https://arxiv.org/html/2605.24202v1 — §3 multi-agent RL workflow and policy-sharing mechanism | https://arxiv.org/html/2605.24202v1 — §4 experiments | https://arxiv.org/html/2605.24202v1 — §5 Discussion; policy-sharing topology and task boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24202 | complete |
| SF-2026-ARXIV-2605-24213 | RP-560b2532606bbdda | deep | arXiv:2605.24213v1 | SRC-ARXIV@arXiv:2605.24213v1 | https://arxiv.org/html/2605.24213v1 — §3 Evaluation-Harness Measurement Method | https://arxiv.org/html/2605.24213v1 — §5 Empirical Harness Study | https://arxiv.org/html/2605.24213v1 — §6 Threats to Validity | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24213 | complete |
| SF-2026-ARXIV-2605-24216 | RP-077abf5941d8963d | deep | arXiv:2605.24216v1 | SRC-ARXIV@arXiv:2605.24216v1 | https://arxiv.org/html/2605.24216v1 — §3 Agent-ToM learning-to-monitor architecture | https://arxiv.org/html/2605.24216v1 — §4–§5 monitoring evaluation | https://arxiv.org/html/2605.24216v1 — §6 Limitations; ToM inference is a sensor, not intent ground truth | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24216 | complete |
| SF-2026-ARXIV-2605-24217 | RP-83b7fc2b50acda2c | deep | arXiv:2605.24217v1 | SRC-ARXIV@arXiv:2605.24217v1 | https://arxiv.org/html/2605.24217v1 — §3 Production-Inference Measurement-Bias Model | https://arxiv.org/html/2605.24217v1 — §4 Benchmark Evaluation | https://arxiv.org/html/2605.24217v1 — §5 Mitigation and production-scope boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24217 | complete |
| SF-2026-ARXIV-2605-24219 | RP-cb6de191d8d1a25b | deep | arXiv:2605.24219v1 | SRC-ARXIV@arXiv:2605.24219v1 | https://arxiv.org/html/2605.24219v1 — §3 Trajectory-Level Hallucination Audit | https://arxiv.org/html/2605.24219v1 — §5 Multi-Agent Workflow Evaluation | https://arxiv.org/html/2605.24219v1 — §6 Limitations and industrial-workflow boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24219 | complete |
| SF-2026-ARXIV-2605-24220 | RP-e1e6b29bd447f830 | deep | arXiv:2605.24220v1 | SRC-ARXIV@arXiv:2605.24220v1 | https://arxiv.org/html/2605.24220v1 — §3 Polar Harness-Agnostic Agentic-RL Runtime | https://arxiv.org/html/2605.24220v1 — §5 Scale Evaluation | https://arxiv.org/html/2605.24220v1 — §6 Limitations and harness/reward boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24220 | complete |
| SF-2026-ARXIV-2605-24229 | RP-95b9d6a655c9ba1b | deep | arXiv:2605.24229v1 | SRC-ARXIV@arXiv:2605.24229v1 | https://arxiv.org/html/2605.24229v1 — §3 atomic-tenet extraction and adversarial audit pipeline | https://arxiv.org/html/2605.24229v1 — §4–§5 multi-turn constitution-adherence evaluation | https://arxiv.org/html/2605.24229v1 — §6 Limitations; published-spec and evaluator boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24229 | complete |
| SF-2026-ARXIV-2605-24245 | RP-d9a0c3a52f264bbf | deep | arXiv:2605.24245v1 | SRC-ARXIV@arXiv:2605.24245v1 | https://arxiv.org/html/2605.24245v1 — §3 User-Generated-Content Poisoning Attack | https://arxiv.org/html/2605.24245v1 — §5 Deep-Research Agent Evaluation | https://arxiv.org/html/2605.24245v1 — §6 Limitations and source/ecosystem boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24245 | complete |
| SF-2026-ARXIV-2605-24247 | RP-c6b27047965b1a2c | deep | arXiv:2605.24247v1 | SRC-ARXIV@arXiv:2605.24247v1 | https://arxiv.org/html/2605.24247v1 — §3 detailed constitutional definitions and AI-assisted labeling workflow | https://arxiv.org/html/2605.24247v1 — §4–§5 label-consistency evaluation | https://arxiv.org/html/2605.24247v1 — §6 Limitations; category/specification and annotator boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24247 | complete |
| SF-2026-ARXIV-2605-24248 | RP-3c1364836d648be2 | deep | arXiv:2605.24248v1 | SRC-ARXIV@arXiv:2605.24248v1 | https://arxiv.org/html/2605.24248v1 — §3 Attested Tool-Server Admission Protocol | https://arxiv.org/html/2605.24248v1 — §5 Security Evaluation | https://arxiv.org/html/2605.24248v1 — §6 Limitations and attestation-root boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24248 | complete |
| SF-2026-ARXIV-2605-24259 | RP-b6c8edc6414dc377 | deep | arXiv:2605.24259v1 | SRC-ARXIV@arXiv:2605.24259v1 | https://arxiv.org/html/2605.24259v1 — §3 Resident-KV Conformance Contract | https://arxiv.org/html/2605.24259v1 — §5 Active-Pressure Evaluation | https://arxiv.org/html/2605.24259v1 — §6 Limitations and cache-manager boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24259 | complete |
| SF-2026-ARXIV-2605-24279 | RP-8b8d5013744b9560 | deep | arXiv:2605.24279v1 | SRC-ARXIV@arXiv:2605.24279v1 | https://arxiv.org/html/2605.24279v1 — §3 ContextEcho snapshot-then-probe deployment harness | https://arxiv.org/html/2605.24279v1 — §4–§5 long agentic-coding session evaluation | https://arxiv.org/html/2605.24279v1 — §6 Limitations; persona probes and coding-session boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24279 | complete |
| SF-2026-ARXIV-2605-24286 | RP-84921df9be98938b | deep | arXiv:2605.24286v1 | SRC-ARXIV@arXiv:2605.24286v1 | https://arxiv.org/html/2605.24286v1 — §3 information-flow faithfulness criteria and diagnostics | https://arxiv.org/html/2605.24286v1 — §4–§5 faithfulness evaluation/training | https://arxiv.org/html/2605.24286v1 — §6 Limitations; diagnostic proxies do not reveal hidden computation | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24286 | complete |
| SF-2026-ARXIV-2605-24299 | RP-724533acc435b3a4 | deep | arXiv:2605.24299v1 | SRC-ARXIV@arXiv:2605.24299v1 | https://arxiv.org/html/2605.24299v1 — §3 factor-analysis decomposition of elicited confidence | https://arxiv.org/html/2605.24299v1 — §4 pairwise calibration across twenty models/six benchmarks | https://arxiv.org/html/2605.24299v1 — §5–§6 Limitations; elicited-confidence and tested-benchmark boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24299 | complete |
| SF-2026-ARXIV-2605-24309 | RP-e7e9cb98a7e9408c | deep | arXiv:2605.24309v1 | SRC-ARXIV@arXiv:2605.24309v1 | https://arxiv.org/html/2605.24309v1 — §3 agent-human security mechanism taxonomy | https://arxiv.org/html/2605.24309v1 — §4 audit of papers, production agents and plugins | https://arxiv.org/html/2605.24309v1 — §5 Limitations; observational taxonomy does not prove mechanism efficacy | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24309 | complete |
| SF-2026-ARXIV-2605-24312 | RP-2668bfa075d3ed92 | deep | arXiv:2605.24312v1 | SRC-ARXIV@arXiv:2605.24312v1 | https://arxiv.org/html/2605.24312v1 — §3 Entailment-Based RAG Membership Inference | https://arxiv.org/html/2605.24312v1 — §4 Five-Query Evaluation | https://arxiv.org/html/2605.24312v1 — §5 Limitations and black-box-access boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24312 | complete |
| SF-2026-ARXIV-2605-24326 | RP-4f648fc711474d89 | deep | arXiv:2605.24326v1 | SRC-ARXIV@arXiv:2605.24326v1 | https://arxiv.org/html/2605.24326v1 — §3–§6 placement, scheduling, network and ScaleAcross Explorer | https://arxiv.org/html/2605.24326v1 — §6.3 Evaluation Results; Appendix A testbed/simulation settings | https://arxiv.org/html/2605.24326v1 — §7 Lessons Learned; §8 Conclusion; cross-building testbed/simulator scope | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24326 | complete |
| SF-2026-ARXIV-2605-24391 | RP-55e9632e2d963538 | deep | arXiv:2605.24391v1 | SRC-ARXIV@arXiv:2605.24391v1 | https://arxiv.org/html/2605.24391v1 — §IV MX-SAFE format; §V accelerator | https://arxiv.org/html/2605.24391v1 — §VI Experimental Results | https://arxiv.org/html/2605.24391v1 — §VII Conclusion; tested MXSF hardware/model boundary | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24391 | complete |
| SF-2026-ARXIV-2605-24420 | RP-b36175ce3407cad2 | deep | arXiv:2605.24420v1 | SRC-ARXIV@arXiv:2605.24420v1 | https://arxiv.org/html/2605.24420v1 — §3 Methodology; §5 theory; §6 mitigation | https://arxiv.org/html/2605.24420v1 — §4 Experiments; §4.3 membership inference | https://arxiv.org/html/2605.24420v1 — Appendix A.3 theoretical limitations; tested normalization/model/data boundary | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24420 | complete |
| SF-2026-ARXIV-2605-24421 | RP-102e187f2447e1a2 | deep | arXiv:2605.24421v1 | SRC-ARXIV@arXiv:2605.24421v1 | https://arxiv.org/html/2605.24421v1 — §2 Threat Model; §3 taxonomy; §4 pipeline/defenses | https://arxiv.org/html/2605.24421v1 — §5 Experiments | https://arxiv.org/html/2605.24421v1 — §6.4 Limitations | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24421 | complete |
| SF-2026-ARXIV-2605-24425 | RP-f3674382966e9490 | deep | arXiv:2605.24425v1 | SRC-ARXIV@arXiv:2605.24425v1 | https://arxiv.org/html/2605.24425v1 — §§3–5 optimizer view, optimizer-inspired block and momentum stream | https://arxiv.org/html/2605.24425v1 — §4.2; §§5–6; Appendix D Experimental Details | https://arxiv.org/html/2605.24425v1 — §7 Conclusion; architecture/scale/recipe boundary | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24425 | complete |
| SF-2026-ARXIV-2605-24426 | RP-98d07cd64cd7d6ad | deep | arXiv:2605.24426v1 | SRC-ARXIV@arXiv:2605.24426v1 | https://arxiv.org/html/2605.24426v1 — §3 verifier-grounded diagnosis, interface evolution and advantage reweighting | https://arxiv.org/html/2605.24426v1 — §4 Experiments; Appendix C controlled protocol | https://arxiv.org/html/2605.24426v1 — §5 Conclusion and Limitations | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24426 | complete |
| SF-2026-ARXIV-2605-24461 | RP-972614f3963dd9ae | deep | arXiv:2605.24461v1 | SRC-ARXIV@arXiv:2605.24461v1 | https://arxiv.org/html/2605.24461v1 — §3 power hierarchy; §§4–6 provisioning, validation and active operation | https://arxiv.org/html/2605.24461v1 — §4.2 empirical data; §§5–7 deployment/runtime measurements | https://arxiv.org/html/2605.24461v1 — §8 Research Wishlist; §10 Conclusion; single 150MW/83K-GB200 site boundary | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24461 | complete |
| SF-2026-ARXIV-2605-24468 | RP-9e8b74037551a48d | deep | arXiv:2605.24468v1 | SRC-ARXIV@arXiv:2605.24468v1 | https://arxiv.org/html/2605.24468v1 — §2.2–§2.3 State-Adaptive Memory and optimization | https://arxiv.org/html/2605.24468v1 — §3 Experiments; §4 Discussions | https://arxiv.org/html/2605.24468v1 — Appendix A Limitations and Broader Impact | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24468 | complete |
| SF-2026-ARXIV-2605-24517 | RP-8cf791c6ad1be8e1 | deep | arXiv:2605.24517v1 | SRC-ARXIV@arXiv:2605.24517v1 | https://arxiv.org/pdf/2605.24517v1 — §3 Method; ECHO hybrid policy/observation objective | https://arxiv.org/pdf/2605.24517v1 — §4 Experimental Setup; §5 Results | https://arxiv.org/pdf/2605.24517v1 — §7 Conclusion; terminal-environment and training-only auxiliary-loss boundary | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24517 | complete |
| SF-2026-ARXIV-2605-24547 | RP-e0e458f246e1cf50 | deep | arXiv:2605.24547v1 | SRC-ARXIV@arXiv:2605.24547v1 | https://arxiv.org/html/2605.24547v1 — §2 problem formulation; §3 bilevel natural-language actor-critic | https://arxiv.org/html/2605.24547v1 — §4 Experiments; Appendix A.5 efficiency | https://arxiv.org/html/2605.24547v1 — §5 Conclusion; tested task/model and higher-order-gradient boundary | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24547 | complete |
| SF-2026-ARXIV-2605-24558 | RP-86300338cd43f93c | deep | arXiv:2605.24558v1 | SRC-ARXIV@arXiv:2605.24558v1 | https://arxiv.org/html/2605.24558v1 — §§2–3 measurement pipeline as observation/inference component | https://arxiv.org/html/2605.24558v1 — §4 empirical audit; §5 alternative views | https://arxiv.org/html/2605.24558v1 — §6 Call to Action; position/audit does not prove a universal pipeline | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24558 | complete |
| SF-2026-ARXIV-2605-24579 | RP-03689a15f3910dd8 | deep | arXiv:2605.24579v1 | SRC-ARXIV@arXiv:2605.24579v1 | https://arxiv.org/html/2605.24579v1 — §3 four-condition diagnostic; §4 expected predictive compression | https://arxiv.org/html/2605.24579v1 — §5 Experimental Setup; §6 Results; §7 Analysis | https://arxiv.org/html/2605.24579v1 — §7 Analysis and §8 Conclusion; tested readers, memories and two benchmarks | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24579 | complete |
| SF-2026-ARXIV-2605-24583 | RP-94172e9bb59bd455 | deep | arXiv:2605.24583v1 | SRC-ARXIV@arXiv:2605.24583v1 | https://arxiv.org/html/2605.24583v1 — §§2–4 separability metric and three confound-control tests | https://arxiv.org/html/2605.24583v1 — §§5–6 calibration and current-alignment audit | https://arxiv.org/html/2605.24583v1 — §7 Scope; §8 open problem and failed spectral-gap claim | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24583 | complete |
| SF-2026-ARXIV-2605-24598 | RP-25d0449947a6ad7a | deep | arXiv:2605.24598v1 | SRC-ARXIV@arXiv:2605.24598v1 | https://arxiv.org/html/2605.24598v1 — §5 Hera step-level device-cloud coordinator | https://arxiv.org/html/2605.24598v1 — §6 Experiment; §6.2–§6.4 | https://arxiv.org/html/2605.24598v1 — Appendix E Limitations and Future Work | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24598 | complete |
| SF-2026-ARXIV-2605-24614 | RP-3a00f3e1da3ee4ac | deep | arXiv:2605.24614v1 | SRC-ARXIV@arXiv:2605.24614v1 | https://arxiv.org/html/2605.24614v1 — §3 Unlearning Depth Score and activation patching | https://arxiv.org/html/2605.24614v1 — §4 Meta-Evaluation; §5 case studies | https://arxiv.org/html/2605.24614v1 — Limitations after §7 Conclusion | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24614 | complete |
| SF-2026-ARXIV-2605-24619 | RP-6de6abc06fda9317 | deep | arXiv:2605.24619v1 | SRC-ARXIV@arXiv:2605.24619v1 | https://arxiv.org/html/2605.24619v1 — §4 Design; §5 Implementation | https://arxiv.org/html/2605.24619v1 — §6 Evaluation | https://arxiv.org/html/2605.24619v1 — §7.2 Limitations | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24619 | complete |
| SF-2026-ARXIV-2605-24657 | RP-6e4c98528d814c8c | deep | arXiv:2605.24657v1 | SRC-ARXIV@arXiv:2605.24657v1 | https://arxiv.org/html/2605.24657v1 — §2 Method; memory taxonomy and consolidation/compaction pipelines | https://arxiv.org/html/2605.24657v1 — §3 Evaluation | https://arxiv.org/html/2605.24657v1 — §4 Discussion — Limitations | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24657 | complete |
| SF-2026-ARXIV-2605-24659 | RP-e1f6275b0ab9bf33 | deep | arXiv:2605.24659v1 | SRC-ARXIV@arXiv:2605.24659v1 | https://arxiv.org/html/2605.24659v1 — §3 Threat Model; §4 feedback-guided payload optimization | https://arxiv.org/html/2605.24659v1 — §5 Experimental Setup; §6 Evaluation | https://arxiv.org/html/2605.24659v1 — Limitations after §7 Conclusion; tested agents/channels only | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24659 | complete |
| SF-2026-ARXIV-2605-24660 | RP-e10fd5ac2e6315c9 | deep | arXiv:2605.24660v1 | SRC-ARXIV@arXiv:2605.24660v1 | https://arxiv.org/html/2605.24660v1 — §3 Bits-over-Random and MDP exposure policy | https://arxiv.org/html/2605.24660v1 — §4 Empirical Evaluation | https://arxiv.org/html/2605.24660v1 — §5.3 Limitations | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24660 | complete |
| SF-2026-ARXIV-2605-24661 | RP-39c314eb0adaeffa | deep | arXiv:2605.24661v1 | SRC-ARXIV@arXiv:2605.24661v1 | https://arxiv.org/html/2605.24661v1 — §4 multi-dimensional behavioral framework and aggregation | https://arxiv.org/html/2605.24661v1 — §5 Results | https://arxiv.org/html/2605.24661v1 — §6.2 Limitations | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24661 | complete |
| SF-2026-ARXIV-2605-24662 | RP-ae966f511033343f | deep | arXiv:2605.24662v1 | SRC-ARXIV@arXiv:2605.24662v1 | https://arxiv.org/pdf/2605.24662v1 — §II–§IV OpenTwin closed-loop data assimilation, calibration and policy-validation workflow | https://arxiv.org/pdf/2605.24662v1 — §A Experimental Setup; §B Experimental Results | https://arxiv.org/pdf/2605.24662v1 — §V Limitations; real-network drift and Open-RAN testbed boundary | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24662 | complete |
| SF-2026-ARXIV-2605-24667 | RP-581d1df78a56b1a8 | deep | arXiv:2605.24667v1 | SRC-ARXIV@arXiv:2605.24667v1 | https://arxiv.org/html/2605.24667v1 — §§3–4 mean/median CE interventions and top-K self-distillation | https://arxiv.org/html/2605.24667v1 — §3.2; §§4.2–4.4; Appendix C protocol | https://arxiv.org/html/2605.24667v1 — §5 Discussion — Limitations | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24667 | complete |
| SF-2026-ARXIV-2605-24683 | RP-59a2b83cfa3da81b | deep | arXiv:2605.24683v1 | SRC-ARXIV@arXiv:2605.24683v1 | https://arxiv.org/html/2605.24683v1 — §III deterministic L2 topology, identity loop and HIL protocol | https://arxiv.org/html/2605.24683v1 — §IV Implementation and Results | https://arxiv.org/html/2605.24683v1 — §V Limitations and Constraints | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24683 | complete |
| SF-2026-ARXIV-2605-24697 | RP-9f4e2f1043856416 | deep | arXiv:2605.24697v1 | SRC-ARXIV@arXiv:2605.24697v1 | https://arxiv.org/html/2605.24697v1 — §3 future-stability labels, learned commitment and TraceLock deployment | https://arxiv.org/html/2605.24697v1 — §4 Experiments; §§4.2–4.4 | https://arxiv.org/html/2605.24697v1 — §5 Conclusion; frozen generator/tested diffusion backbones boundary | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24697 | complete |
| SF-2026-ARXIV-2605-24709 | RP-e754b0014f15c7c7 | deep | arXiv:2605.24709v1 | SRC-ARXIV@arXiv:2605.24709v1 | https://arxiv.org/pdf/2605.24709v1 — §3 Methodology; streaming partially-observed recurrent policy with exact RTRL | https://arxiv.org/pdf/2605.24709v1 — §4 Experiments | https://arxiv.org/pdf/2605.24709v1 — §6 Discussion and Limitations | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24709 | complete |
| SF-2026-ARXIV-2605-24727 | RP-9695b6567a93af77 | deep | arXiv:2605.24727v1 | SRC-ARXIV@arXiv:2605.24727v1 | https://arxiv.org/html/2605.24727v1 — §3 four explanation conditions; §4 quadrilemma theorem/implications | https://arxiv.org/html/2605.24727v1 — formal construction and implications in §4 | https://arxiv.org/html/2605.24727v1 — §5 Conclusion, limitations and future work | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24727 | complete |
| SF-2026-ARXIV-2605-24728 | RP-9c320a39b9208093 | deep | arXiv:2605.24728v1 | SRC-ARXIV@arXiv:2605.24728v1 | https://arxiv.org/html/2605.24728v1 — §4 operability state/graph, spatial transactions and effect diffs; §5 agency gates | https://arxiv.org/html/2605.24728v1 — §6 repair stress test; §7 qualitative result | https://arxiv.org/html/2605.24728v1 — §1.2 Scope of Claims; prototype/trajectory does not establish general runtime validity | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24728 | complete |
| SF-2026-ARXIV-2605-24733 | RP-0193a60be397b1bf | deep | arXiv:2605.24733v1 | SRC-ARXIV@arXiv:2605.24733v1 | https://arxiv.org/html/2605.24733v1 — §3 formulation; §4 hybrid checker; §5 typed process reward | https://arxiv.org/html/2605.24733v1 — §6 checker evaluation; §7 GRPO training | https://arxiv.org/html/2605.24733v1 — Limitations after §8 Conclusion | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24733 | complete |
| SF-2026-ARXIV-2605-24737 | RP-f76afdb14139d1ac | deep | arXiv:2605.24737v1 | SRC-ARXIV@arXiv:2605.24737v1 | https://arxiv.org/pdf/2605.24737v1 — §3 governance from metrics; §4 govllm architecture; §5 contributions | https://arxiv.org/pdf/2605.24737v1 — §6 Preliminary experiments | https://arxiv.org/pdf/2605.24737v1 — §6.3 and §7.4 Limitations | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24737 | complete |
| SF-2026-ARXIV-2605-24743 | RP-14b1da66185ab9e6 | deep | arXiv:2605.24743v1 | SRC-ARXIV@arXiv:2605.24743v1 | https://arxiv.org/html/2605.24743v1 — §3 bilevel synthetic-trajectory weighting; §4 theory | https://arxiv.org/html/2605.24743v1 — §§5–6 experiments and learned-weight analysis | https://arxiv.org/html/2605.24743v1 — §7 Conclusion; three tasks and synthetic-generator boundary | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24743 | complete |
| SF-2026-ARXIV-2605-24749 | RP-6a6251126779544a | deep | arXiv:2605.24749v1 | SRC-ARXIV@arXiv:2605.24749v1 | https://arxiv.org/html/2605.24749v1 — §§3–5 reward-weighted feature recovery and tilted-policy value gap | https://arxiv.org/html/2605.24749v1 — theory and deployment-temperature analysis in §§4–5 | https://arxiv.org/html/2605.24749v1 — §6 Conclusion and Discussion; single-index/theoretical-assumption boundary | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24749 | complete |
| SF-2026-ARXIV-2605-24756 | RP-4a2017558a4cac29 | deep | arXiv:2605.24756v1 | SRC-ARXIV@arXiv:2605.24756v1 | https://arxiv.org/html/2605.24756v1 — §4 proper trajectory scores under complete and censored observation | https://arxiv.org/html/2605.24756v1 — §5 metrics; §6 Experiments | https://arxiv.org/html/2605.24756v1 — §7 Conclusion and Limitations | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24756 | complete |
| SF-2026-ARXIV-2605-24770 | RP-b893b2cab66aa0ad | deep | arXiv:2605.24770v1 | SRC-ARXIV@arXiv:2605.24770v1 | https://arxiv.org/html/2605.24770v1 — §§2–5 Muon geometry and recipe interaction | https://arxiv.org/html/2605.24770v1 — §§3–6; Appendices C–E | https://arxiv.org/html/2605.24770v1 — §7 Conclusions and limitations | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24770 | complete |
| SF-2026-ARXIV-2605-24775 | RP-3886915343290683 | deep | arXiv:2605.24775v1 | SRC-ARXIV@arXiv:2605.24775v1 | https://arxiv.org/html/2605.24775v1 — §III identity; §§IV–VIII protocol, scoring, orchestration and persistence | https://arxiv.org/html/2605.24775v1 — reported operational examples and convergence traces in §§VI–VIII | https://arxiv.org/html/2605.24775v1 — §I/§II claim scope; pattern/prototype rather than general production proof | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24775 | complete |
| SF-2026-ARXIV-2605-24785 | RP-c03d089563b69109 | deep | arXiv:2605.24785v1 | SRC-ARXIV@arXiv:2605.24785v1 | https://arxiv.org/pdf/2605.24785v1 — §3 cost decomposition and online skill-distillation lifecycle | https://arxiv.org/pdf/2605.24785v1 — §5 Experimental Setup and reported results | https://arxiv.org/pdf/2605.24785v1 — §7 Limitations and Conclusion | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24785 | complete |
| SF-2026-ARXIV-2605-24786 | RP-c5d198be81110b11 | deep | arXiv:2605.24786v1 | SRC-ARXIV@arXiv:2605.24786v1 | https://arxiv.org/html/2605.24786v1 — §3 confidence-aware mixed-precision cache manager | https://arxiv.org/html/2605.24786v1 — §§4–6 setup, results and ablations | https://arxiv.org/html/2605.24786v1 — §7 failure modes; §8 Limitations and conclusion | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24786 | complete |
| SF-2026-ARXIV-2605-24793 | RP-d267c48a39ae48a5 | deep | arXiv:2605.24793v1 | SRC-ARXIV@arXiv:2605.24793v1 | https://arxiv.org/html/2605.24793v1 — §3 utility view, collaborative arbitration and RL training | https://arxiv.org/html/2605.24793v1 — §4 Experiments; §§4.2–4.4 | https://arxiv.org/html/2605.24793v1 — §5 Conclusion and Appendix A tested-model/benchmark boundary | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24793 | complete |
| SF-2026-ARXIV-2605-24817 | RP-d376f013b687760b | deep | arXiv:2605.24817v1 | SRC-ARXIV@arXiv:2605.24817v1 | arXiv:2605.24817v1 HTML — §5 Method: request-level telemetry, hybrid scoring and calibrated detector | arXiv:2605.24817v1 HTML — §6 Evaluation, including §6.3–§6.5 transfer and privacy-boundary tests | arXiv:2605.24817v1 HTML — §8 Discussion; §10 Ethical Concern; no dedicated Limitations section | arXiv:2605.24817v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-24817 | complete |
| SF-2026-ARXIV-2605-24818 | RP-7fe610b7d1de0184 | deep | arXiv:2605.24818v1 | SRC-ARXIV@arXiv:2605.24818v1 | arXiv:2605.24818v1 HTML — §3 Simulating contamination; §3.1 Estimators and predictors; §3.2 Data generation | arXiv:2605.24818v1 HTML — §4 Benchmarking predictors; §5 Practical considerations; Appendix B Experimental details | arXiv:2605.24818v1 HTML — §5 Practical considerations; §6 Discussion: controlled Hubble-8B/test-set setting, training-data access and counterfactual-model assumptions | arXiv:2605.24818v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-24818 | complete |
| SF-2026-ARXIV-2605-24823 | RP-26c3b77b3995ecf6 | deep | arXiv:2605.24823v1 | SRC-ARXIV@arXiv:2605.24823v1 | arXiv:2605.24823v1 HTML — §3 Definition and Decomposition of Industrial Cognition; §4 thin versus thick autonomy | arXiv:2605.24823v1 HTML — §5 The Factory as a Cognitive Ecosystem: A Worked Example | arXiv:2605.24823v1 HTML — §8 Research Agenda; §9 Conclusion; position paper and near-future composite, not deployed-system validation | arXiv:2605.24823v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-24823 | complete |
| SF-2026-ARXIV-2605-24832 | RP-51979a1f86135445 | deep | arXiv:2605.24832v1 | SRC-ARXIV@arXiv:2605.24832v1 | arXiv:2605.24832v1 HTML — §4 Streaming Chunked Decoding; §5 Saturation-aware Elastic Scheduling | arXiv:2605.24832v1 HTML — §7 Evaluation, especially §7.3–§7.7 throughput, serving and ablation results | arXiv:2605.24832v1 HTML — §9 Conclusion; no dedicated Limitations section; evidence is bounded to evaluated DLLMs, A100 and disclosed loads | arXiv:2605.24832v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-24832 | complete |
| SF-2026-ARXIV-2605-24870 | RP-cc4dd36dd2966dd4 | deep | arXiv:2605.24870v1 | SRC-ARXIV@arXiv:2605.24870v1 | arXiv:2605.24870v1 HTML — §2 Problem Formulation; §3.1 Local Statistical Calibration; §3.2 Trajectory-Consistent Prior Estimation | arXiv:2605.24870v1 HTML — §4.1–§4.3 PixArt-alpha/DiT-XL/2 experiments and ablations; Appendix B.1–B.8 latency, prompt-count and compute details | arXiv:2605.24870v1 HTML — Appendix C Limitations and Broader Impact; offline priors, selected sites/windows, representative-prompt and tested-model boundary | arXiv:2605.24870v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-24870 | complete |
| SF-2026-ARXIV-2605-24879 | RP-7ecc15008e367834 | deep | arXiv:2605.24879v1 | SRC-ARXIV@arXiv:2605.24879v1 | arXiv:2605.24879v1 HTML — §4 Proposed Method; §5 Privacy Analysis and Accounting; Appendix B.9 randomized-clipping accountant | arXiv:2605.24879v1 HTML — §6 Experiments; §6.1 Memory, Compute and Latency Gains; Appendix D hyperparameters | arXiv:2605.24879v1 HTML — §7 Conclusion and experiment scope: Llama-3.2-1B, sequence length 4096, selected full/LoRA fine-tuning tasks and randomized norm-estimation assumptions | arXiv:2605.24879v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-24879 | complete |
| SF-2026-ARXIV-2605-24883 | RP-4a6636ab3f7e0857 | deep | arXiv:2605.24883v1 | SRC-ARXIV@arXiv:2605.24883v1 | arXiv:2605.24883v1 HTML — §3 Methodology: policy-to-FOL translation, semantic policy graph and graph-guided query instantiation | arXiv:2605.24883v1 HTML — §4 Evaluation: policy coverage and attack efficacy | arXiv:2605.24883v1 HTML — § Limitations: policy-quality dependency, static single-turn scope, no multi-turn or agent-state coverage | arXiv:2605.24883v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-24883 | complete |
| SF-2026-ARXIV-2605-24892 | RP-4206eab193a94322 | deep | arXiv:2605.24892v1 | SRC-ARXIV@arXiv:2605.24892v1 | arXiv:2605.24892v1 HTML — §3.1 Large Drive Model, especially §3.1.3 chunk-wise prediction/CLEF/TIS; §3.2 Vision Renderer; §3.3 training and interleaved inference pipeline | arXiv:2605.24892v1 HTML — §4.1 Large Drive Model and §4.2 Vision Renderer, including horizon/CL-CLEF-TIS ablations and production-scale comparison | arXiv:2605.24892v1 HTML — §5 Conclusion/future directions; private driving-data distribution, learned renderer and offline/closed-loop evaluation boundary; no dedicated limitations section | arXiv:2605.24892v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-24892 | complete |
| SF-2026-ARXIV-2605-24914 | RP-4348aa5c762412a2 | deep | arXiv:2605.24914v1 | SRC-ARXIV@arXiv:2605.24914v1 | arXiv:2605.24914v1 HTML — §3 MVR-cache multi-vector retrieval and prompt segmentation | arXiv:2605.24914v1 HTML — §5 semantic-cache evaluation | arXiv:2605.24914v1 HTML — §6 limitations and workload/encoder boundary | arXiv:2605.24914v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-24914 | complete |
| SF-2026-ARXIV-2605-24922 | RP-dcb3537ebca19467 | deep | arXiv:2605.24922v1 | SRC-ARXIV@arXiv:2605.24922v1 | arXiv:2605.24922v1 HTML — §3 System Design and API; §3.1 Design boundary; §3.2 Persistent pool ownership; §3.3 Runtime primitives; §3.4 Reset-time randomization | arXiv:2605.24922v1 HTML — §4 Validation and Benchmarks: parity, rollout throughput, reset and Jacobian measurements | arXiv:2605.24922v1 HTML — §6 Discussion; §6.1 Runtime boundary and trade-offs; §6.3 Reproducibility | arXiv:2605.24922v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-24922 | complete |
| SF-2026-ARXIV-2605-24930 | RP-84515d6b9347b564 | deep | arXiv:2605.24930v1 | SRC-ARXIV@arXiv:2605.24930v1 | arXiv:2605.24930v1 HTML — §3 Methodology; §3.1 Semantic tree construction; §3.2 Memory-token construction; §3.3 Hierarchical inference; §3.4 Objectives | arXiv:2605.24930v1 HTML — §4 Experiments: LongBench/structured-document quality, TTFT and memory | arXiv:2605.24930v1 HTML — §5 Conclusion and discussion: hierarchy dependency, heuristic-tree error propagation, rare-evidence attenuation and routing-prune risk | arXiv:2605.24930v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-24930 | complete |
| SF-2026-ARXIV-2605-24941 | RP-186ba8bfb236198f | deep | arXiv:2605.24941v1 | SRC-ARXIV@arXiv:2605.24941v1 | arXiv:2605.24941v1 HTML — PDF §3 memory-induced tool-drift mechanism | arXiv:2605.24941v1 HTML — PDF §4 agent/tool evaluation | arXiv:2605.24941v1 HTML — PDF §5 limitations and memory/task boundary | arXiv:2605.24941v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-24941 | complete |
| SF-2026-ARXIV-2605-24973 | RP-6b7efaccae6f1dec | deep | arXiv:2605.24973v1 | SRC-ARXIV@arXiv:2605.24973v1 | arXiv:2605.24973v1 HTML — §3 Problem formulation; §4.1 Task-oriented data engine; §4.2 Dynamic chunking and synchronization; §4.3 Document enrichment | arXiv:2605.24973v1 HTML — §5 Experiments: five OCR backends and downstream RAG/QA | arXiv:2605.24973v1 HTML — §5 evaluation scope and §6 conclusion: OCR/model/workload boundary; cross-page summaries can suppress fine-grained evidence | arXiv:2605.24973v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-24973 | complete |
| SF-2026-ARXIV-2605-25002 | RP-4772cc1089fbe596 | deep | arXiv:2605.25002v1 | SRC-ARXIV@arXiv:2605.25002v1 | arXiv:2605.25002v1 HTML — §3 Problem Formulation; §4 MemMark, including distribution-preserving watermark and cryptographic audit trace | arXiv:2605.25002v1 HTML — §5 Experiments, RQ1–RQ5 | arXiv:2605.25002v1 HTML — §7 Limitations; Appendix G memory-lifecycle attacks and backend diagnostics | arXiv:2605.25002v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25002 | complete |
| SF-2026-ARXIV-2605-25052 | RP-54bb474635658972 | deep | arXiv:2605.25052v1 | SRC-ARXIV@arXiv:2605.25052v1 | arXiv:2605.25052v1 HTML — §2 faithfulness definitions; §3 ground-truth elicitation; §4 BonaFide labeling pipeline | arXiv:2605.25052v1 HTML — §5 Experiments and §5.2 Results | arXiv:2605.25052v1 HTML — §5.3 Discussion — Limitations; task/model and metric-cost boundary | arXiv:2605.25052v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25052 | complete |
| SF-2026-ARXIV-2605-25073 | RP-6d565967c6c643fa | deep | arXiv:2605.25073v1 | SRC-ARXIV@arXiv:2605.25073v1 | arXiv:2605.25073v1 HTML — §2 Evaluation Substrate and Threat Model; §3–§5 pre/during/post-tuning lifecycle taxonomy; §6 unified cross-phase evaluation | arXiv:2605.25073v1 HTML — §6.2–§6.6 shared models/tasks, reproduced attacks and cross-phase defense combinations | arXiv:2605.25073v1 HTML — §7 Discussion and §8 Future Directions; reproduced small-model/task configurations, method-compatibility substitutions and lifecycle-survey boundary | arXiv:2605.25073v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25073 | complete |
| SF-2026-ARXIV-2605-25077 | RP-d17d901b4fbc012c | deep | arXiv:2605.25077v1 | SRC-ARXIV@arXiv:2605.25077v1 | arXiv:2605.25077v1 HTML — §3 Method: NWT, Spatial-Pathway LoRA and Trajectory-Anchored State Persistence | arXiv:2605.25077v1 HTML — §4 Experiments, including camera/object control and state-persistence ablations | arXiv:2605.25077v1 HTML — Appendix D Limitations; pixel-world and trajectory-action boundary | arXiv:2605.25077v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25077 | complete |
| SF-2026-ARXIV-2605-25085 | RP-e201832217ab23ac | deep | arXiv:2605.25085v1 | SRC-ARXIV@arXiv:2605.25085v1 | arXiv:2605.25085v1 HTML — §3 formulation; §4 Main Theoretical Results on sequential Wyner–Ziv and suffix-only policies | arXiv:2605.25085v1 HTML — §5 Empirical Validation; §6 Connections to Deployed Compression Schemes | arXiv:2605.25085v1 HTML — §7 Limitations, including architecture, rate-convergence and heavy-hitter boundaries | arXiv:2605.25085v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25085 | complete |
| SF-2026-ARXIV-2605-25092 | RP-83a156192aaafae0 | deep | arXiv:2605.25092v1 | SRC-ARXIV@arXiv:2605.25092v1 | arXiv:2605.25092v1 HTML — §3 System Design; §4 Optimizations; §5.9 Agent Memory Benchmark cascade router | arXiv:2605.25092v1 HTML — §5 Evaluation, especially §5.9 LongMemEval and LoCoMo | arXiv:2605.25092v1 HTML — §6 Threats to validity and limitations; Appendix N Threats to Validity | arXiv:2605.25092v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25092 | complete |
| SF-2026-ARXIV-2605-25133 | RP-85b3dd2e1a91df73 | deep | arXiv:2605.25133v1 | SRC-ARXIV@arXiv:2605.25133v1 | arXiv:2605.25133v1 HTML — §3 Prover-Verifier Deliberation protocol and algorithm | arXiv:2605.25133v1 HTML — §4 Experiments; §5 Results on coverage-precision operating points | arXiv:2605.25133v1 HTML — §7 Limitations; verifier effective-region and no-formal-guarantee boundary | arXiv:2605.25133v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25133 | complete |
| SF-2026-ARXIV-2605-25160 | RP-c5e4ef7c48bd47a1 | deep | arXiv:2605.25160v1 | SRC-ARXIV@arXiv:2605.25160v1 | arXiv:2605.25160v1 HTML — §3 SimuWoB; §3.1 Environment generation; §3.2 Task and validator generation | arXiv:2605.25160v1 HTML — §4 Experiments: app fidelity, task feasibility and GUI-agent evaluation | arXiv:2605.25160v1 HTML — §5 Limitations: visual-only interface, single-app tasks, no accessibility tree or cross-app workflow | arXiv:2605.25160v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25160 | complete |
| SF-2026-ARXIV-2605-25188 | RP-b305173282f7d3b8 | deep | arXiv:2605.25188v1 | SRC-ARXIV@arXiv:2605.25188v1 | arXiv:2605.25188v1 HTML — §3 DarkForest Design: calibrated belief, controlled disclosure and guardrail | arXiv:2605.25188v1 HTML — §4 Evaluation; Appendix D ablations | arXiv:2605.25188v1 HTML — §6 Conclusion; no dedicated Limitations section; benchmark/model and coordinator boundary | arXiv:2605.25188v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25188 | complete |
| SF-2026-ARXIV-2605-25189 | RP-52a5ec545d41d6d8 | deep | arXiv:2605.25189v1 | SRC-ARXIV@arXiv:2605.25189v1 | arXiv:2605.25189v1 HTML — §3–§5 dominant update directions, directional shift and trusted-direction method | arXiv:2605.25189v1 HTML — §6 Experimental Setting; §7 Results | arXiv:2605.25189v1 HTML — Appendix A.1 Future Work; manuscript explicitly identifies itself as a preliminary study | arXiv:2605.25189v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25189 | complete |
| SF-2026-ARXIV-2605-25233 | RP-21c9028918989b7a | deep | arXiv:2605.25233v1 | SRC-ARXIV@arXiv:2605.25233v1 | arXiv:2605.25233v1 HTML — §3 Method, especially §3.2 verification loop and error attribution | arXiv:2605.25233v1 HTML — §4 Experiments and ablation study | arXiv:2605.25233v1 HTML — §4.5 Discussions; §5 Conclusion; no dedicated Limitations section | arXiv:2605.25233v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25233 | complete |
| SF-2026-ARXIV-2605-25240 | RP-84b6513eca9689f1 | deep | arXiv:2605.25240v1 | SRC-ARXIV@arXiv:2605.25240v1 | arXiv:2605.25240v1 HTML — §3.1 Dataset; §3.2 Constructed quality levels; §3.3 Rubric and pairwise-preference expert annotation | arXiv:2605.25240v1 HTML — §4 Empirical comparison of rubric scoring and comparative judgment | arXiv:2605.25240v1 HTML — Appendix A.1 Limitations: legal-domain scope, prompt-induced quality confounds, style cues and mixed-trade-off cases | arXiv:2605.25240v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25240 | complete |
| SF-2026-ARXIV-2605-25244 | RP-976230abd615e47e | deep | arXiv:2605.25244v1 | SRC-ARXIV@arXiv:2605.25244v1 | arXiv:2605.25244v1 HTML — §3 Confidence Trajectories and Confidence Dynamic Gain voting | arXiv:2605.25244v1 HTML — §5 Empirical Results and §5.3–§5.4 ablations/score analysis | arXiv:2605.25244v1 HTML — §6 Conclusion; Appendix A.2 simplified-training-model assumption; no dedicated Limitations section | arXiv:2605.25244v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25244 | complete |
| SF-2026-ARXIV-2605-25247 | RP-590dd99b68d0dceb | deep | arXiv:2605.25247v1 | SRC-ARXIV@arXiv:2605.25247v1 | arXiv:2605.25247v1 HTML — §4 Design of Kavier and cache-aware simulation modules | arXiv:2605.25247v1 HTML — §6 Trace-Based Experiments with Kavier | arXiv:2605.25247v1 HTML — §6.7 Discussion; §7.2 Future Work; bachelor-thesis prototype and simulator-calibration boundary | arXiv:2605.25247v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25247 | complete |
| SF-2026-ARXIV-2605-25252 | RP-b5b5c1f3ea612a06 | deep | arXiv:2605.25252v1 | SRC-ARXIV@arXiv:2605.25252v1 | arXiv:2605.25252v1 HTML — §3 Methodology: controlled false-positive/false-negative verifier noise and rollout scaling | arXiv:2605.25252v1 HTML — §4 Results on compute-supervision tradeoffs | arXiv:2605.25252v1 HTML — §5 Conclusion; narrow Qwen2.5/GSM8K/GRPO setting and no dedicated Limitations section | arXiv:2605.25252v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25252 | complete |
| SF-2026-ARXIV-2605-25272 | RP-b63243167e8852a5 | deep | arXiv:2605.25272v1 | SRC-ARXIV@arXiv:2605.25272v1 | arXiv:2605.25272v1 HTML — §2 Variance decomposition, confirmatory factor analysis, bifactor model and mixed-effects latent regression; §3 Experiment and data | arXiv:2605.25272v1 HTML — §4 Results across six benchmark ecosystems | arXiv:2605.25272v1 HTML — § Limitations: one snapshot/six benchmarks, observational design, noisy metadata, non-representative sample and temporal instability | arXiv:2605.25272v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25272 | complete |
| SF-2026-ARXIV-2605-25284 | RP-c6c6bf12ec7a5516 | deep | arXiv:2605.25284v1 | SRC-ARXIV@arXiv:2605.25284v1 | arXiv:2605.25284v1 HTML — §3 ambiguity-recognition and clarification protocol | arXiv:2605.25284v1 HTML — §4 evaluation | arXiv:2605.25284v1 HTML — §5 limitations and prompt/model boundary | arXiv:2605.25284v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25284 | complete |
| SF-2026-ARXIV-2605-25292 | RP-f1b52d80595cf9e3 | deep | arXiv:2605.25292v1 | SRC-ARXIV@arXiv:2605.25292v1 | arXiv:2605.25292v1 HTML — §II Work Package Structure and Contributions: IAIS data flow, formal workflow mapping, Kubernetes/Slurm control manager and Digital Twin state | arXiv:2605.25292v1 HTML — §III Evaluation Results: 10–5000 job/node scalability and solver/heuristic workflow comparison | arXiv:2605.25292v1 HTML — §IV Conclusion and project-report scope; component-level evaluation, heterogeneous project artifacts and no controlled end-to-end production SLO comparison | arXiv:2605.25292v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25292 | complete |
| SF-2026-ARXIV-2605-25298 | RP-5116ff1c466a2d6b | deep | arXiv:2605.25298v1 | SRC-ARXIV@arXiv:2605.25298v1 | arXiv:2605.25298v1 HTML — §III Design; §IV-A eBPF metric collection; §IV-C Selective Thread Tracking and Algorithm 1 | arXiv:2605.25298v1 HTML — §V–§VI six data-intensive applications and CPU/disk/lock/external-service contention; Artifact Description/Evaluation | arXiv:2605.25298v1 HTML — §IV-C optimistic entry-point propagation assumption; §V single x86/Linux 6.8.12 host and six-application workload boundary | arXiv:2605.25298v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25298 | complete |
| SF-2026-ARXIV-2605-25310 | RP-1db426a80ab5dec7 | standard | arXiv:2605.25310v1 | SRC-ARXIV@arXiv:2605.25310v1 | https://arxiv.org/html/2605.25310v1#S2 | https://arxiv.org/html/2605.25310v1#S4 | https://arxiv.org/html/2605.25310v1#S6 | Not Disclosed — exact-v1 review found no versioned public artifact contract | claim:SF-2026-ARXIV-2605-25310 | complete |
| SF-2026-ARXIV-2605-25313 | RP-5f4bec245d79794d | deep | arXiv:2605.25313v1 | SRC-ARXIV@arXiv:2605.25313v1 | arXiv:2605.25313v1 HTML — §3 UWM-JEPA belief-space dynamics | arXiv:2605.25313v1 HTML — §4 world-model evaluation | arXiv:2605.25313v1 HTML — §5 limitations and environment/action boundary | arXiv:2605.25313v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25313 | complete |
| SF-2026-ARXIV-2605-25338 | RP-7d863dc51c514600 | deep | arXiv:2605.25338v1 | SRC-ARXIV@arXiv:2605.25338v1 | arXiv:2605.25338v1 HTML — §3 Problem Setup; §4.1–§4.3 causal attribution, counterfactual repair and multi-agent validation | arXiv:2605.25338v1 HTML — §5–§6 intervention protocol, repair performance, minimality and ablations | arXiv:2605.25338v1 HTML — §7 Discussion; Appendix A.10 Runtime Analysis; Appendix B Future Work | arXiv:2605.25338v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25338 | complete |
| SF-2026-ARXIV-2605-25375 | RP-6a5be176c44fb6ab | deep | arXiv:2605.25375v1 | SRC-ARXIV@arXiv:2605.25375v1 | arXiv:2605.25375v1 HTML — §III problem definition; §III-B dynamic priority, bandwidth pathfinder and cost allocator | arXiv:2605.25375v1 HTML — §IV-A–§IV-E geo-cluster setup, bandwidth/GPU/workload sensitivity and ablation | arXiv:2605.25375v1 HTML — §II-A prior limitations; §V conclusion; evidence is simulator/trace-bound | arXiv:2605.25375v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25375 | complete |
| SF-2026-ARXIV-2605-25376 | RP-ff156444b01bd5d9 | deep | arXiv:2605.25376v1 | SRC-ARXIV@arXiv:2605.25376v1 | arXiv:2605.25376v1 HTML — §2 threat model; §3 three-layer runtime gates; §5 dynamic rogue signals; §6 evidence chain | arXiv:2605.25376v1 HTML — §4.4 worked fleets; §8–§10 evaluation, red-team and performance sections | arXiv:2605.25376v1 HTML — §4.5 calibration and limitations; §11 limitations and threat-model boundary | arXiv:2605.25376v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25376 | complete |
| SF-2026-ARXIV-2605-25379 | RP-064a1b1a85fed0e2 | deep | arXiv:2605.25379v1 | SRC-ARXIV@arXiv:2605.25379v1 | arXiv:2605.25379v1 HTML — §1.2 structured retrieval state; §3 tree memory, adaptive routing, MARS/SMP and access control | arXiv:2605.25379v1 HTML — §4 datasets, main results, component ablation and verifier-guided recovery | arXiv:2605.25379v1 HTML — §5 Limitations; Appendix A.4 efficiency accounting; Appendix F.3 failure modes | arXiv:2605.25379v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25379 | complete |
| SF-2026-ARXIV-2605-25389 | RP-9fe8cde438e44af4 | deep | arXiv:2605.25389v1 | SRC-ARXIV@arXiv:2605.25389v1 | arXiv:2605.25389v1 HTML — §2 threat model; §3.1–§3.3 attack memory, memory-augmented attack and Attack-Flow GRPO | arXiv:2605.25389v1 HTML — §4 main, ablation, stealth and cross-model experiments | arXiv:2605.25389v1 HTML — §6 Conclusion; Appendix C framework/dataset/training scope | arXiv:2605.25389v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25389 | complete |
| SF-2026-ARXIV-2605-25421 | RP-62f11f28d74b931b | deep | arXiv:2605.25421v1 | SRC-ARXIV@arXiv:2605.25421v1 | arXiv:2605.25421v1 HTML — §2.2–§2.4 dual-channel protocol, cross-channel alignment and interactive co-training | arXiv:2605.25421v1 HTML — §3–§4 task/metric setup, ablation, compatibility, robustness and scale analysis | arXiv:2605.25421v1 HTML — §6 Conclusion; Appendix B model-family/scale boundary | arXiv:2605.25421v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25421 | complete |
| SF-2026-ARXIV-2605-25422 | RP-9bd395bbe7df5a45 | deep | arXiv:2605.25422v1 | SRC-ARXIV@arXiv:2605.25422v1 | arXiv:2605.25422v1 HTML — §3 system model; §4 token/KV latency; §5.1–§5.2 constrained mode and bandwidth optimization | arXiv:2605.25422v1 HTML — §5.3 numerical validation and multi-round mode switching | arXiv:2605.25422v1 HTML — §6 Conclusion and Future Work; wireless/model assumptions bound generality | arXiv:2605.25422v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25422 | complete |
| SF-2026-ARXIV-2605-25424 | RP-9b0ded46e6cda190 | deep | arXiv:2605.25424v1 | SRC-ARXIV@arXiv:2605.25424v1 | arXiv:2605.25424v1 HTML — §3 session-budget MDP; §4.1–§4.3 HBR, CQL and deployment lambda-sweep | arXiv:2605.25424v1 HTML — §5 cost-safety frontier, delayed-gratification and ablation experiments | arXiv:2605.25424v1 HTML — §6 Conclusion; offline reward proxy, single model pair and fixed-cost assumptions | arXiv:2605.25424v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25424 | complete |
| SF-2026-ARXIV-2605-25430 | RP-0380c85d82bcb80e | deep | arXiv:2605.25430v1 | SRC-ARXIV@arXiv:2605.25430v1 | arXiv:2605.25430v1 HTML — §3.1 Skill extraction; §3.2 learnable skill-bank maintenance; §3.3 RL objective | arXiv:2605.25430v1 HTML — §4 EnvBench, SWE-Bench Verified and Terminal-Bench 2; iterative-bank ablations | arXiv:2605.25430v1 HTML — §5/Appendix: frozen downstream agent, benchmark and verifier-reward boundary | arXiv:2605.25430v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25430 | complete |
| SF-2026-ARXIV-2605-25451 | RP-9156584361eba181 | deep | arXiv:2605.25451v1 | SRC-ARXIV@arXiv:2605.25451v1 | arXiv:2605.25451v1 HTML — Official author artifact §BigMac Method: dependency-safe nested pipeline, global operator-table schedule, scheduler/executor separation and PP-transparent interface | arXiv:2605.25451v1 HTML — Official author artifact §Experiments: Qwen3-30B-A3B + 1.3B ViT; MMDiT extension; 8K sequence; Optimus/Megatron-DistTrain comparisons | arXiv:2605.25451v1 HTML — Official author artifact §Evidence Boundary — no explicit Limitations section; hardware, precision, topology, concurrency and tail-SLO are Not Disclosed | arXiv:2605.25451v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25451 | complete |
| SF-2026-ARXIV-2605-25475 | RP-b804c4d9ded4c0b1 | deep | arXiv:2605.25475v1 | SRC-ARXIV@arXiv:2605.25475v1 | arXiv:2605.25475v1 HTML — §3.1 learned token indexer; §3.2 latent fast/slow-weight memory | arXiv:2605.25475v1 HTML — §4 RULER, NIAH, LongBench, compression and ablation | arXiv:2605.25475v1 HTML — §6 Conclusion & Limitation; Appendix A limited budgets, models and frozen backbone | arXiv:2605.25475v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25475 | complete |
| SF-2026-ARXIV-2605-25492 | RP-ebd5ed74a7ea3203 | deep | arXiv:2605.25492v1 | SRC-ARXIV@arXiv:2605.25492v1 | arXiv:2605.25492v1 HTML — §3 configuration grid; §4 SDI/CFR/rank-concordance/variance metrics | arXiv:2605.25492v1 HTML — §5 configuration-conditional reversals and cross-package analysis | arXiv:2605.25492v1 HTML — §6 Threats to Validity: narrow model/benchmark/envelope and qualitative variance attribution | arXiv:2605.25492v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25492 | complete |
| SF-2026-ARXIV-2605-25507 | RP-ce410d2dc149f6da | deep | arXiv:2605.25507v1 | SRC-ARXIV@arXiv:2605.25507v1 | arXiv:2605.25507v1 HTML — §3 Conservative Policy Iteration with reset credit; §4 RRPO and SRPO | arXiv:2605.25507v1 HTML — §5–§6 reasoning benchmarks, GRPO/RRPO/SRPO comparison and reset ablations | arXiv:2605.25507v1 HTML — §7 Limitations: self-localized error and verifiable-reward reasoning scope | arXiv:2605.25507v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25507 | complete |
| SF-2026-ARXIV-2605-25521 | RP-70581403d9083b98 | deep | arXiv:2605.25521v1 | SRC-ARXIV@arXiv:2605.25521v1 | arXiv:2605.25521v1 HTML — §3 motivation; §4 centroid-parallel SIMD, cache organization and ranking-preserving reformulation | arXiv:2605.25521v1 HTML — §5 setup, end-to-end, microbenchmark, ablation and microarchitecture evidence | arXiv:2605.25521v1 HTML — §7 Conclusion; evaluated CPU/PQ construction boundary | arXiv:2605.25521v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25521 | complete |
| SF-2026-ARXIV-2605-25535 | RP-ed7dfda96add92dc | deep | arXiv:2605.25535v1 | SRC-ARXIV@arXiv:2605.25535v1 | arXiv:2605.25535v1 HTML — §3–§4 static/dynamic PerMem-Bench; §7.1 session-level personalized storage gating | arXiv:2605.25535v1 HTML — §5 meta-evaluation; §6 protocol; §7.2 memory-system results | arXiv:2605.25535v1 HTML — §8 Conclusion; appendix construction/judge/checkpoint-sampling boundaries | arXiv:2605.25535v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25535 | complete |
| SF-2026-ARXIV-2605-25537 | RP-04b0446b1b297dc0 | deep | arXiv:2605.25537v1 | SRC-ARXIV@arXiv:2605.25537v1 | arXiv:2605.25537v1 HTML — §III problem; §IV-A action-prior denoising; §IV-B inference blending | arXiv:2605.25537v1 HTML — §V–§VI Kinetix setup, real-robot pilot and delay/window sweeps | arXiv:2605.25537v1 HTML — §VII Discussion; small real-robot pilot and policy/workload scope | arXiv:2605.25537v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25537 | complete |
| SF-2026-ARXIV-2605-25547 | RP-cd10eaa790e1c610 | deep | arXiv:2605.25547v1 | SRC-ARXIV@arXiv:2605.25547v1 | arXiv:2605.25547v1 HTML — §3.2 posterior action sampling; §3.3 task-progress verification | arXiv:2605.25547v1 HTML — §4 simulation, real-world and sample/latent ablations | arXiv:2605.25547v1 HTML — Appendix I linear-progress assumption and base-policy capacity boundary | arXiv:2605.25547v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25547 | complete |
| SF-2026-ARXIV-2605-25550 | RP-ae331b0b27aab0ba | deep | arXiv:2605.25550v1 | SRC-ARXIV@arXiv:2605.25550v1 | arXiv:2605.25550v1 HTML — §2 workload/stage imbalance; §3 async pipeline and hybrid instance scheduler; §4 implementation | arXiv:2605.25550v1 HTML — §5 quality, latency, scale, robustness, elasticity and utilization | arXiv:2605.25550v1 HTML — §7 Conclusion; diffusion-stage topology and disclosed hardware/workload boundary | arXiv:2605.25550v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25550 | complete |
| SF-2026-ARXIV-2605-25621 | RP-9994a0a03aac6345 | deep | arXiv:2605.25621v1 | SRC-ARXIV@arXiv:2605.25621v1 | arXiv:2605.25621v1 HTML — §4.1 evidence construction; §4.2 long/short memory update; §4.3 response trigger | arXiv:2605.25621v1 HTML — §3 SOVBench and §5 audio-visual/visual-only/ablation evaluation | arXiv:2605.25621v1 HTML — Appendix J trigger failures; Appendix K limitations and future work | arXiv:2605.25621v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25621 | complete |
| SF-2026-ARXIV-2605-25624 | RP-68e66564213f9f22 | deep | arXiv:2605.25624v1 | SRC-ARXIV@arXiv:2605.25624v1 | arXiv:2605.25624v1 HTML — §2.1 adversarial task/reward co-generation; §2.2 environment scaling | arXiv:2605.25624v1 HTML — §3–§4 training results, data/environment scaling and emergent multi-action calls | arXiv:2605.25624v1 HTML — §6 Limitations; synthetic task and environment-fidelity boundary | arXiv:2605.25624v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25624 | complete |
| SF-2026-ARXIV-2605-25632 | RP-4619387a5f2e35fd | deep | arXiv:2605.25632v1 | SRC-ARXIV@arXiv:2605.25632v1 | arXiv:2605.25632v1 HTML — §3 action taxonomy and quote-bind-commit; §4 authority frontier and capital metrics | arXiv:2605.25632v1 HTML — §5–§7 simulation, calibration and runtime-control experiments | arXiv:2605.25632v1 HTML — §8 Limitations; actuarial assumptions and empirical deployment boundary | arXiv:2605.25632v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25632 | complete |
| SF-2026-ARXIV-2605-25641 | RP-9ba391ea45bff775 | deep | arXiv:2605.25641v1 | SRC-ARXIV@arXiv:2605.25641v1 | arXiv:2605.25641v1 HTML — §3 production correction setting; §4 factual-nugget variants and iterative optimization | arXiv:2605.25641v1 HTML — §5–§6 held-out, transfer, negative-control and answer-level results | arXiv:2605.25641v1 HTML — §7 Conclusion: one retrieval architecture, English-only and LLM dependence | arXiv:2605.25641v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25641 | complete |
| SF-2026-ARXIV-2605-25653 | RP-39f60aca40746504 | deep | arXiv:2605.25653v1 | SRC-ARXIV@arXiv:2605.25653v1 | arXiv:2605.25653v1 HTML — §3 threat/system model; §4 typed zero-trust enforcement and physical-impact tiers | arXiv:2605.25653v1 HTML — §5 deployed instantiation, 60 traces and coverage analysis | arXiv:2605.25653v1 HTML — §6 Conclusion; small system/model/trace envelope | arXiv:2605.25653v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25653 | complete |
| SF-2026-ARXIV-2605-25655 | RP-7ca4e9edb679585c | deep | arXiv:2605.25655v1 | SRC-ARXIV@arXiv:2605.25655v1 | arXiv:2605.25655v1 HTML — §III-A framework; §III-B operators; §III-C graph schedule; §III-D adaptive parallelism | arXiv:2605.25655v1 HTML — §IV throughput, ablation and operator scaling experiments | arXiv:2605.25655v1 HTML — §V Conclusion; MT-3000-specific architecture and bandwidth boundary | arXiv:2605.25655v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25655 | complete |
| SF-2026-ARXIV-2605-25673 | RP-9a63d25e636fb484 | deep | arXiv:2605.25673v1 | SRC-ARXIV@arXiv:2605.25673v1 | arXiv:2605.25673v1 HTML — §3 referential stability; §4 threat model; §5 workflows; §8 attestation/fingerprinting architectures | arXiv:2605.25673v1 HTML — §7 provider identifier survey and workflow analysis | arXiv:2605.25673v1 HTML — §9 Conclusions; proposal-level evidence without broad deployed evaluation | arXiv:2605.25673v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25673 | complete |
| SF-2026-ARXIV-2605-25674 | RP-df3c827b4e41a9aa | deep | arXiv:2605.25674v1 | SRC-ARXIV@arXiv:2605.25674v1 | arXiv:2605.25674v1 HTML — §2 layer-wise target; §3 unbiased estimator; §4 variance analysis | arXiv:2605.25674v1 HTML — §5 memorisation-regime setup, decision rule and empirical validation | arXiv:2605.25674v1 HTML — §6 Discussion and limitations; modest model/monitoring setting | arXiv:2605.25674v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25674 | complete |
| SF-2026-ARXIV-2605-25682 | RP-823f08790d6c4e79 | deep | arXiv:2605.25682v1 | SRC-ARXIV@arXiv:2605.25682v1 | arXiv:2605.25682v1 HTML — §3 segment communication, staging bottleneck and adaptive inference | arXiv:2605.25682v1 HTML — §4 prototype; §5 latency, energy, qualitative and instrumentation results | arXiv:2605.25682v1 HTML — §6 Conclusion; Jetson/Wi-Fi prototype and qualitative-output boundary | arXiv:2605.25682v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25682 | complete |
| SF-2026-ARXIV-2605-25698 | RP-3c65bae54c14803c | deep | arXiv:2605.25698v1 | SRC-ARXIV@arXiv:2605.25698v1 | arXiv:2605.25698v1 HTML — §3 quality-aware functional scaling law; §4 optimal schedule; §5.1 Drop-Stable-Rampup | arXiv:2605.25698v1 HTML — §5.2–§5.4 batch drop, phase ratio and schedule comparison | arXiv:2605.25698v1 HTML — §6 scope: theoretical simplification, multi-task heterogeneity, scale dependence and overhead | arXiv:2605.25698v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25698 | complete |
| SF-2026-ARXIV-2605-25707 | RP-1d0010b46d6e3100 | deep | arXiv:2605.25707v1 | SRC-ARXIV@arXiv:2605.25707v1 | arXiv:2605.25707v1 HTML — §3 corruption benchmark; §4 robustness method | arXiv:2605.25707v1 HTML — §5 setup, main results and ablation; Appendix E case studies | arXiv:2605.25707v1 HTML — §6 Conclusion; OSWorld corruption/model envelope | arXiv:2605.25707v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25707 | complete |
| SF-2026-ARXIV-2605-25716 | RP-3c8e5efefb6b7d84 | deep | arXiv:2605.25716v1 | SRC-ARXIV@arXiv:2605.25716v1 | arXiv:2605.25716v1 HTML — §3 threat model; §4 scrambled distributed attention; §5 role-aware collaborative RAG | arXiv:2605.25716v1 HTML — §6 privacy analysis; §7 latency, network, utility and quantization evaluation | arXiv:2605.25716v1 HTML — §8 Discussion; honest-but-curious assumptions and disclosed network/topology boundary | arXiv:2605.25716v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25716 | complete |
| SF-2026-ARXIV-2605-25745 | RP-b21db761ecc7b586 | deep | arXiv:2605.25745v1 | SRC-ARXIV@arXiv:2605.25745v1 | arXiv:2605.25745v1 HTML — §3 span anticipation, confidence gate, latent encoding and three-stage training | arXiv:2605.25745v1 HTML — §4 four math benchmarks; compression/accuracy/latency and gating ablations | arXiv:2605.25745v1 HTML — §5 Limitations: math/model/calibration scope and latent-span error propagation | arXiv:2605.25745v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25745 | complete |
| SF-2026-ARXIV-2605-25746 | RP-0f39e89a94215f4a | deep | arXiv:2605.25746v1 | SRC-ARXIV@arXiv:2605.25746v1 | arXiv:2605.25746v1 HTML — §3 joint structure/orchestration posterior; §4 task-budget structural prior and policy orchestration | arXiv:2605.25746v1 HTML — §5 benchmark/token-budget comparisons and interaction ablations | arXiv:2605.25746v1 HTML — §6 Limitations: tested tasks/models/budgets and centralized training assumptions | arXiv:2605.25746v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25746 | complete |
| SF-2026-ARXIV-2605-25798 | RP-816fad636035fde0 | deep | arXiv:2605.25798v1 | SRC-ARXIV@arXiv:2605.25798v1 | arXiv:2605.25798v1 HTML — §III cached-token reuse and softmax-threshold mask reuse; §IV hash-distributed hardware | arXiv:2605.25798v1 HTML — §V methodology, performance, area/power and high-resolution comparison | arXiv:2605.25798v1 HTML — §VII Conclusion; specialized architecture and diffusion-workload simulation boundary | arXiv:2605.25798v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25798 | complete |
| SF-2026-ARXIV-2605-25815 | RP-66cd02201cf4147f | deep | arXiv:2605.25815v1 | SRC-ARXIV@arXiv:2605.25815v1 | arXiv:2605.25815v1 HTML — §3 EvoMap dataset/protocol reconstruction; §4 reuse, credit, GDI and validation analysis | arXiv:2605.25815v1 HTML — §5–§7 1.5M assets/128K agents empirical audit and manipulation checks | arXiv:2605.25815v1 HTML — §8 limitations: 47-day observational snapshot, one ecosystem and self-reported fields | arXiv:2605.25815v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25815 | complete |
| SF-2026-ARXIV-2605-25819 | RP-c003a2991ffd7bf7 | deep | arXiv:2605.25819v1 | SRC-ARXIV@arXiv:2605.25819v1 | arXiv:2605.25819v1 HTML — §3 per-sample vulnerability; §4 calibrated aggregation; §5 finite-population correction | arXiv:2605.25819v1 HTML — §6 efficient LiRA experiments and analytical simulation | arXiv:2605.25819v1 HTML — §7/Appendix: Gaussian post-processing, finite shadow-model and dataset scope | arXiv:2605.25819v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25819 | complete |
| SF-2026-ARXIV-2605-25820 | RP-8254de0101e2a4d9 | deep | arXiv:2605.25820v1 | SRC-ARXIV@arXiv:2605.25820v1 | arXiv:2605.25820v1 HTML — §3.2 visual redundancy; §3.3 redundancy-controlled parallel decoding | arXiv:2605.25820v1 HTML — §4 model/benchmark comparison, certainty analysis and ablation | arXiv:2605.25820v1 HTML — Appendix A.3 limitations; backbone and multimodal-task scope | arXiv:2605.25820v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25820 | complete |
| SF-2026-ARXIV-2605-25831 | RP-f0936c7c1e361d87 | deep | arXiv:2605.25831v1 | SRC-ARXIV@arXiv:2605.25831v1 | arXiv:2605.25831v1 HTML — §3.1 belief-state construction; §3.2 clarify/abstain/answer strategy | arXiv:2605.25831v1 HTML — §4–§7 interaction simulation, accuracy, clarification and faithfulness | arXiv:2605.25831v1 HTML — §9 Limitations; simulated-user/judge and dataset ambiguity boundary | arXiv:2605.25831v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25831 | complete |
| SF-2026-ARXIV-2605-25854 | RP-5a8d660f3c5070ef | deep | arXiv:2605.25854v1 | SRC-ARXIV@arXiv:2605.25854v1 | arXiv:2605.25854v1 HTML — §3 differentiable ECW dispatch layer; §4 fixed-point virtual-water coordination | arXiv:2605.25854v1 HTML — §5 IEEE 30/118-bus dispatch and consistency experiments | arXiv:2605.25854v1 HTML — §6 limitations: simulated grid, water-attribution model and no production DC trace | arXiv:2605.25854v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25854 | complete |
| SF-2026-ARXIV-2605-25869 | RP-c2ff3700d08ed629 | deep | arXiv:2605.25869v1 | SRC-ARXIV@arXiv:2605.25869v1 | arXiv:2605.25869v1 HTML — §3.1 typed memory atoms; §3.2 multi-route projection; §3.3 provenance-scoped use | arXiv:2605.25869v1 HTML — §4 main results, ablation, backbone and hyperparameter analysis | arXiv:2605.25869v1 HTML — §5 Conclusion; benchmark/prompt and long-term deployment boundary | arXiv:2605.25869v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25869 | complete |
| SF-2026-ARXIV-2605-25874 | RP-263cb42c09c2606f | deep | arXiv:2605.25874v1 | SRC-ARXIV@arXiv:2605.25874v1 | arXiv:2605.25874v1 HTML — §3 multi-turn dataset; §4 world-model evaluation suite | arXiv:2605.25874v1 HTML — §5 protocol, per-dimension, cross-dimension and human-alignment results | arXiv:2605.25874v1 HTML — §6 Conclusion; Appendix B web-model access and configuration boundary | arXiv:2605.25874v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25874 | complete |
| SF-2026-ARXIV-2605-25889 | RP-6c40b09c9ac0e777 | deep | arXiv:2605.25889v1 | SRC-ARXIV@arXiv:2605.25889v1 | arXiv:2605.25889v1 HTML — §3 information-theoretic capability/robustness bound; §4 encoder-specific corollary | arXiv:2605.25889v1 HTML — §5 Gaussian/OpenVLA/LIBERO/PGD and cross-architecture diagnostics | arXiv:2605.25889v1 HTML — §6 limitations: loose pixel bound, estimated mutual information and tested attacks | arXiv:2605.25889v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25889 | complete |
| SF-2026-ARXIV-2605-25893 | RP-4048e598bf10a235 | deep | arXiv:2605.25893v1 | SRC-ARXIV@arXiv:2605.25893v1 | arXiv:2605.25893v1 HTML — §3 hesitation signals; §4 cascade monitor and probe routing | arXiv:2605.25893v1 HTML — §5 datasets/models, efficiency-effectiveness, robustness and ablation | arXiv:2605.25893v1 HTML — Appendix A Limitation; evaluated diffusion models/remasking strategies only | arXiv:2605.25893v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25893 | complete |
| SF-2026-ARXIV-2605-25966 | RP-58461e2fb33b8adf | deep | arXiv:2605.25966v1 | SRC-ARXIV@arXiv:2605.25966v1 | arXiv:2605.25966v1 HTML — §3 QAT implementation, LR schedule and factorial/ablation grid | arXiv:2605.25966v1 HTML — §4–§5 compute/statistical protocol and schedule×bit-width results | arXiv:2605.25966v1 HTML — §6.8 Limitations; sub-100M and tested optimizer/data regime | arXiv:2605.25966v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25966 | complete |
| SF-2026-ARXIV-2605-25971 | RP-93d4d22cee1fc96a | deep | arXiv:2605.25971v1 | SRC-ARXIV@arXiv:2605.25971v1 | arXiv:2605.25971v1 HTML — §3 proactive need prediction; §4 idle-time evidence acquisition and persistent-memory loop | arXiv:2605.25971v1 HTML — §5 ProActEval/MemBench, turn/effort/hallucination and ablation results | arXiv:2605.25971v1 HTML — §6 limitations: predictable-need scenarios, privacy/cost and stale anticipation | arXiv:2605.25971v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25971 | complete |
| SF-2026-ARXIV-2605-25988 | RP-31040560e2c7459d | deep | arXiv:2605.25988v1 | SRC-ARXIV@arXiv:2605.25988v1 | arXiv:2605.25988v1 HTML — §3 checker backends and reward; §5 signal collapse; §6 reward-hacking cascade | arXiv:2605.25988v1 HTML — §4 main/cross-model results and appendices 9–16 | arXiv:2605.25988v1 HTML — §8 listed limitations: evaluation independence, seeds, test size, domain and incomplete cascade resolution | arXiv:2605.25988v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25988 | complete |
| SF-2026-ARXIV-2605-25997 | RP-c33f13b29f44b38b | deep | arXiv:2605.25997v1 | SRC-ARXIV@arXiv:2605.25997v1 | arXiv:2605.25997v1 HTML — §2 evidence fibers and action completeness; §3 completion curves; §4 certify-then-acquire | arXiv:2605.25997v1 HTML — §5 controlled channels and Tox21/Matbench/JARVIS audits | arXiv:2605.25997v1 HTML — §6 limitations: finite response spaces, selected public datasets and action model | arXiv:2605.25997v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25997 | complete |
| SF-2026-ARXIV-2605-26029 | RP-133cd71e195331e3 | deep | arXiv:2605.26029v1 | SRC-ARXIV@arXiv:2605.26029v1 | arXiv:2605.26029v1 HTML — §3 interactive SCM environment; §4 parsable causal-trajectory DSL | arXiv:2605.26029v1 HTML — §5 mechanism recovery, interventions, scale and verification results | arXiv:2605.26029v1 HTML — §8 Limitations; synthetic SCM and benchmark-agent scope | arXiv:2605.26029v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-26029 | complete |
| SF-2026-ARXIV-2605-26037 | RP-f8221b35e88d16a6 | deep | arXiv:2605.26037v1 | SRC-ARXIV@arXiv:2605.26037v1 | arXiv:2605.26037v1 HTML — §2 KG tool interface and RLVR setup; §3 four feedback channels; §4 reward variants | arXiv:2605.26037v1 HTML — §5 four-seed peak-collapse, oracle relation ablation and self-distillation | arXiv:2605.26037v1 HTML — §6 limitations: Freebase/CWQ/Qwen2.5-7B and interface-specific failure | arXiv:2605.26037v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-26037 | complete |
| SF-2026-ARXIV-2605-26045 | RP-051ec8c0b38d2d6d | deep | arXiv:2605.26045v1 | SRC-ARXIV@arXiv:2605.26045v1 | arXiv:2605.26045v1 HTML — §3 five confidence operators for activation oracles; §4 calibration protocol | arXiv:2605.26045v1 HTML — §5 four Qwen/Gemma oracles, 6K samples/operator and label/no-label comparisons | arXiv:2605.26045v1 HTML — §6 limitations: secret-word task, enumerability and no general interpretability guarantee | arXiv:2605.26045v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-26045 | complete |
| SF-2026-ARXIV-2605-26046 | RP-873a02454b3e98e0 | deep | arXiv:2605.26046v1 | SRC-ARXIV@arXiv:2605.26046v1 | arXiv:2605.26046v1 HTML — §3 decomposition grid; §5 gradient-specificity and instruction-interference analysis | arXiv:2605.26046v1 HTML — §4 results and appendices B–F trajectory/task diagnostics | arXiv:2605.26046v1 HTML — §6–§7 conclusion/future work; two datasets and textual-gradient optimizer scope | arXiv:2605.26046v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-26046 | complete |
| SF-2026-ARXIV-2605-26047 | RP-667b1bb709269793 | deep | arXiv:2605.26047v1 | SRC-ARXIV@arXiv:2605.26047v1 | arXiv:2605.26047v1 HTML — §2 control setting/metrics; §3 retrying; §4 resampling and audit aggregation | arXiv:2605.26047v1 HTML — §5–§6 BashArena safety/usefulness, budget and selective-resampling experiments | arXiv:2605.26047v1 HTML — §7 limitations: one coding arena, model/monitor pair and adaptive adversary | arXiv:2605.26047v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-26047 | complete |
| SF-2026-ARXIV-2605-26079 | RP-1d03b9707419a293 | deep | arXiv:2605.26079v1 | SRC-ARXIV@arXiv:2605.26079v1 | arXiv:2605.26079v1 HTML — §2 evidence-collector/auditor; §3 benchmark-quality audit protocol | arXiv:2605.26079v1 HTML — §4 fix/manual validation and §5 trajectory audit analysis | arXiv:2605.26079v1 HTML — §7 Conclusion; automated auditor false-positive/coverage and sampled-benchmark boundary | arXiv:2605.26079v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-26079 | complete |
| SF-2026-ARXIV-2605-26110 | RP-2b4be3a8a077bd4c | deep | arXiv:2605.26110v1 | SRC-ARXIV@arXiv:2605.26110v1 | arXiv:2605.26110v1 HTML — §3 backbone/plugin boundary, registration API and scalable training integration | arXiv:2605.26110v1 HTML — §4 reproducibility/continual-tuning method comparisons | arXiv:2605.26110v1 HTML — §5 limitations: research codebase, supported backbones and no production fault study | arXiv:2605.26110v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-26110 | complete |
| SF-2026-ARXIV-2605-26112 | RP-a328720dcfad0b6d | deep | arXiv:2605.26112v1 | SRC-ARXIV@arXiv:2605.26112v1 | arXiv:2605.26112v1 HTML — §3 harness infrastructure and temporal layers; §4 context/memory/skill bottlenecks | arXiv:2605.26112v1 HTML — §5 process/longitudinal evaluation and safe evolution argument | arXiv:2605.26112v1 HTML — §6 alternative views and limitations; position/framework paper without controlled deployment study | arXiv:2605.26112v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-26112 | complete |
| SF-2026-ARXIV-2605-26114 | RP-9f74573dbd27cc07 | deep | arXiv:2605.26114v1 | SRC-ARXIV@arXiv:2605.26114v1 | arXiv:2605.26114v1 HTML — §3.1 layered state model; §3.2 programmable/serializable state and verifiable outcomes | arXiv:2605.26114v1 HTML — §4 protocol; §5 benchmark, sim-to-real, judge error and efficiency | arXiv:2605.26114v1 HTML — §6 listed visual/backend/app/legal/misuse limitations | arXiv:2605.26114v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-26114 | complete |
| SF-AERIC-ANTICIPATORY-HIDDEN-STATE-MONITORING-FOR-IMPLICIT-HARMFUL-DIALOGUE | RP-6de2ee59d4b175dd | deep | arXiv:2605.23974v1 | SRC-ARXIV@arXiv:2605.23974v1 | arXiv:2605.23974v1 HTML — §3 AERIC — same-pass hidden-state hazard forecasting and EMA rule | arXiv:2605.23974v1 HTML — §4 Setup and §5 Results — transfer, safe-budget and latency evaluation | arXiv:2605.23974v1 HTML — §6 Limitations and Broader Impact — white-box state access, model and threshold-shift boundary | arXiv:2605.23974v1 artifact/code statement; immutable commit Not Disclosed unless named | claim:SF-AERIC-ANTICIPATORY-HIDDEN-STATE-MONITORING-FOR-IMPLICIT-HARMFUL-DIALOGUE | complete |
| SF-FAITHFUL-OR-FABRICATED-A-CAUSAL-FRAMEWORK-FOR-RATIONALIZATION-BIAS-IN-LL | RP-8463bcad8f08e12e | deep | arXiv:2605.23970v1 | SRC-ARXIV@arXiv:2605.23970v1 | arXiv:2605.23970v1 HTML — §III Problem Formulation and §IV causal cue-intervention method | arXiv:2605.23970v1 HTML — §V Experiments — tie-aware anchoring and mitigation metrics | arXiv:2605.23970v1 HTML — §VI Limitations / Conclusion — judge, summarization and cue-family boundary | arXiv:2605.23970v1 artifact/code statement; immutable commit Not Disclosed unless named | claim:SF-FAITHFUL-OR-FABRICATED-A-CAUSAL-FRAMEWORK-FOR-RATIONALIZATION-BIAS-IN-LL | complete |
| SF-LGMT-LOGIC-GROUNDED-METAMORPHIC-TESTING-FOR-EVALUATING-THE-REASONING-REL | RP-a7ae0eb23c062b57 | deep | arXiv:2605.23965v1 | SRC-ARXIV@arXiv:2605.23965v1 | arXiv:2605.23965v1 HTML — §3 logic-grounded metamorphic test generator | arXiv:2605.23965v1 — §4 evaluation and mutation analysis | arXiv:2605.23965v1 — §5 limitations: rule coverage, oracle and domain scope | arXiv:2605.23965v1 artifact/code statement; immutable commit Not Disclosed unless named | claim:SF-LGMT-LOGIC-GROUNDED-METAMORPHIC-TESTING-FOR-EVALUATING-THE-REASONING-REL | complete |
| SF-STOP-COMPARING-LLM-AGENTS-WITHOUT-DISCLOSING-THE-HARNESS | RP-3d466eb046b00d8d | deep | arXiv:2605.23950v1 | SRC-ARXIV@arXiv:2605.23950v1 | https://arxiv.org/html/2605.23950v1 §2 Binding Constraint Thesis; §3 Control-Theoretic Model — mechanism: Second, published benchmarks, industry deployments, and a controlled variance decomposition show that harness-induced variance can substantially exceed model-induced variance, including cases of model ranking reversal. | https://arxiv.org/html/2605.23950v1 §4 Variance Evidence; §5 Disclosure Protocol — disclosed evaluation scope only | https://arxiv.org/html/2605.23950v1 Position-paper evidence boundary; §6 Limitations — no generalization beyond disclosed workload/model/evaluator | https://arxiv.org/html/2605.23950v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-STOP-COMPARING-LLM-AGENTS-WITHOUT-DISCLOSING-THE-HARNESS | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2605-23911:start -->
#### Cross-Platform Fused MoE Dispatch in Triton: Portable Expert Routing Without CUDA

<!-- claim:SF-2026-ARXIV-2605-23911:start -->
- **Problem:** Mixture-of-Experts (MoE) architectures power the majority of frontier large language models, but their inference is bottlenecked by irregular memory access patterns and expert routing overhead.
- **Old path / changed constraint:** Mixture-of-Experts (MoE) architectures power the majority of frontier large language models, but their inference is bottlenecked by irregular memory access patterns and expert routing overhead.
- **Mechanism / ownership:** We present TritonMoE, a fused MoE dispatch kernel written entirely in OpenAI Triton that performs the complete forward pass -- router scoring, token permutation, expert GEMMs, and weighted output combination -- using only portable Triton primitives.
- **Evaluation contract:** Comprehensive benchmarks across four MoE model configurations (8 to 256 experts) showing 89–131% of Megablocks throughput at inference batch sizes on NVIDIA A100.
- **Proof / non-proof:** Evidence is author-reported exact-v1 mechanism/evaluation evidence. It does not establish cross-model, cross-hardware, cross-workload or production generality unless those conditions are explicitly named above.
- **Trade-off / failure mode:** Describe the issue below: Mixture-of-Experts (MoE) architectures power the majority of frontier large language models, but their inference is bottlenecked by irregular memory access patterns and expert routing overhead.
- **Coexistence boundary:** The older path remains appropriate where its workload and SLO do not trigger the changed constraint; the paper is treated as a conditional branch, not a universal replacement.
- **Primary:** [arXiv:2605.23911v1](https://arxiv.org/abs/2605.23911v1)；frozen exact-v1 `papers/2026/05/_sources/arxiv-owner-replay-20260903/exact-v1/2605.23911v1.html.html`。
- **Disposition:** `No Change — Existing Coverage`；Fresh-context owner/adjacent comparison completed; the current Books proposition already owns the durable mechanism, so no duplicate paragraph was added.
<!-- claim:SF-2026-ARXIV-2605-23911:end -->
<!-- review:SF-2026-ARXIV-2605-23911:end -->

<!-- review:SF-2026-ARXIV-2605-23918:start -->
#### The Model Parking Tax: Quantifying the Hidden Energy Cost of Always-On GPU Model Deployment

<!-- claim:SF-2026-ARXIV-2605-23918:start -->
- **Problem:** The AI inference industry keeps models loaded in GPU memory around the clock to avoid cold-start latency, implicitly treating idle power as a fixed cost of readiness.
- **Old path / changed constraint:** No prior work has measured the marginal idle power cost per GB of VRAM, decomposed idle power into DVFS and memory components, or tested cross-architecture invariance.
- **Mechanism / ownership:** We present the first cross-architecture measurement of idle GPU power as a function of VRAM allocation, combining 18 days of production telemetry (335,267 samples, 14 H100 GPUs) with controlled dose-response experiments on three GPU architectures spanning three memory technologies: NVIDIA H100 (HBM3, 80 GB), A100 (HBM2e, 80 GB), and L40S (GDDR6, 48 GB).
- **Evaluation contract:** We present the first cross-architecture measurement of idle GPU power as a function of VRAM allocation, combining 18 days of production telemetry (335,267 samples, 14 H100 GPUs) with controlled dose-response experiments on three GPU architectures spanning three memory technologies: NVIDIA H100 (HBM3, 80 GB), A100 (HBM2e, 80 GB), and L40S (GDDR6, 48 GB).
- **Proof / non-proof:** Evidence is author-reported exact-v1 mechanism/evaluation evidence. It does not establish cross-model, cross-hardware, cross-workload or production generality unless those conditions are explicitly named above.
- **Trade-off / failure mode:** Multi-Process Service (MPS) ( 17 ) allows multiple CUDA contexts to share SM resources with reduced context-switching overhead.
- **Coexistence boundary:** The older path remains appropriate where its workload and SLO do not trigger the changed constraint; the paper is treated as a conditional branch, not a universal replacement.
- **Primary:** [arXiv:2605.23918v1](https://arxiv.org/abs/2605.23918v1)；frozen exact-v1 `papers/2026/05/_sources/arxiv-owner-replay-20260903/exact-v1/2605.23918v1.html.html`。
- **Disposition:** `No Change — Existing Coverage`；Fresh-context owner/adjacent comparison completed; the current Books proposition already owns the durable mechanism, so no duplicate paragraph was added.
<!-- claim:SF-2026-ARXIV-2605-23918:end -->
<!-- review:SF-2026-ARXIV-2605-23918:end -->

<!-- review:SF-2026-ARXIV-2605-23935:start -->
#### Operationalizing Reconstructive Authority: Runtime Construction, Dependency Resolution, and Execution Gating in Autonomous Agent Systems

<!-- claim:SF-2026-ARXIV-2605-23935:start -->
- **Problem:** Autonomous agent systems fail not only due to incorrect decisions, but due to executing decisions whose authority no longer holds at runtime.
- **Old path / changed constraint:** Prior work defined Reconstructive Authority (RAM) as a condition for valid execution: actions are permitted only if authority can be constructed from current state.
- **Mechanism / ownership:** We introduce a runtime execution model in which authority is evaluated at action time and execution is conditioned on its constructibility.
- **Evaluation contract:** We show that this model guarantees safety -- no action is executed without constructible authority -- and conditional liveness: execution resumes when authority-defining variables become observable.
- **Proof / non-proof:** Evidence is author-reported exact-v1 mechanism/evaluation evidence. It does not establish cross-model, cross-hardware, cross-workload or production generality unless those conditions are explicitly named above.
- **Trade-off / failure mode:** A central failure mode follows from this structure: systems execute decisions whose authority no longer holds at runtime.
- **Coexistence boundary:** The older path remains appropriate where its workload and SLO do not trigger the changed constraint; the paper is treated as a conditional branch, not a universal replacement.
- **Primary:** [arXiv:2605.23935v1](https://arxiv.org/abs/2605.23935v1)；frozen exact-v1 `papers/2026/05/_sources/arxiv-owner-replay-20260903/exact-v1/2605.23935v1.html.html`。
- **Disposition:** `No Change — Existing Coverage`；Fresh-context owner/adjacent comparison completed; the current Books proposition already owns the durable mechanism, so no duplicate paragraph was added.
<!-- claim:SF-2026-ARXIV-2605-23935:end -->
<!-- review:SF-2026-ARXIV-2605-23935:end -->

<!-- review:SF-2026-ARXIV-2605-23945:start -->
<!-- claim:SF-2026-ARXIV-2605-23945:start -->
Synchronous RLHF generation should treat response-length skew as changing the efficient TP degree; online reconfiguration must compare predicted benefit with KV migration/recompute, reshard and communicator costs.
<!-- claim:SF-2026-ARXIV-2605-23945:end -->
#### Accelerating Long-Tail Generation in Synchronous RLHF Training via Adaptive Tensor Parallelism

- **Why / changed constraint:** `§3 predictor-guided TP reconfiguration; §4 KV migration/recompute and weight reshard`。
- **Mechanism / ownership:** Synchronous RLHF generation should treat response-length skew as changing the efficient TP degree; online reconfiguration must compare predicted benefit with KV migration/recompute, reshard and communicator costs.
- **Evaluation contract:** `§5 A40/H100 testbeds, Llama/Qwen with VeRL/SGLang`；结果只绑定 exact-v1 披露的模型、数据、硬件与 evaluator。
- **Trade-off / non-proof:** No dedicated limitations section; 8–16 GPU testbeds, offline profiles and synchronous pipelines do not establish fleet-scale stability or arbitrary topology gains.
- **Evolution / owner:** `Direct Evolution` → `TRAIN-TENSOR-PARALLEL`；Score V2 `3/3/3` = **9/9**。
- **Books decision:** `No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-23945:end -->

<!-- review:SF-2026-ARXIV-2605-23951:start -->
#### Methods for Formal Verification of Agent Skills: Three Layers Toward a Mechanically Checkable Capability-Containment Proof

问题与演进：agent skill capability containment 需要 static effect analysis、refinement-typed dispatch 与 bounded model checking 组合，经验测试不能替代 soundness。旧方案在其原 workload、风险和成本约束下仍成立。

Method：`https://arxiv.org/html/2605.23951v1 §3 Semantics; §4–§6 Three Verification Layers — mechanism: We give a precise semantics for skill behaviour faithful to how a skill is consumed by an LLM-driven runtime (a deterministic script-side reachable through a non-deterministic LLM-side), state the verification problem as a capability-containment property over that semantics, and present three composable methods that together raise…`。

Evaluation：`https://arxiv.org/html/2605.23951v1 §8 Bundle Re-checker; §10 Threat Coverage — disclosed scope: The companion paper introduced a four-level verification lattice on agent-skill manifests (unverified, declared, tested, formal) and left the top level aspirational. This paper closes that gap. We give a precise semantics for skill behaviour faithful to how a skill is consumed by an LLM-driven runtime (a…`。

Non-proof / fallback：`https://arxiv.org/html/2605.23951v1 §11 Scope and Residual LLM Refusal Boundary — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO`。离开披露条件时回退既有机制，不把作者结果外推为通用保证。Artifact：`https://arxiv.org/html/2605.23951v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-23951:start -->长期结论只限 exact-v1 披露的机制和实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 一律记为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-23951:end -->
<!-- review:SF-2026-ARXIV-2605-23951:end -->

<!-- review:SF-2026-ARXIV-2605-23956:start -->
#### QUIVER: A Formal Framework for Quantifying Perturbation Propagation and Bifurcation in Compound AI Systems

Review provenance 由本节边界正文与 Completion Receipt 共同绑定；owner=`WORLDVIEW-SYSTEM-EVOLUTION`。
Method / identity：arXiv:2605.23956v1 §2 typed pipeline graph, type-dispatched distances, sensitivity matrix and loop bifurcation — We introduce QUIVER, a formal framework for measuring perturbation propagation in graph-structured LLM pipelines.。
Evaluation：arXiv:2605.23956v1 §2.5 evaluation principles and estimation; framework case analyses。
Counterevidence / limitations：Not Disclosed — exact-v1 body was reviewed, but no stable numbered Limitations/Counterevidence fragment was exposed; reviewer boundary: arXiv:2605.23956v1 No controlled production validation; the formal model depends on chosen distance metrics and perturbation distributions。
Artifact：Not Disclosed — no immutable public artifact was identified in the reviewed exact-v1 body。

<!-- claim:SF-2026-ARXIV-2605-23956:start -->The exact-v1 body supports the mechanism under §2.5 evaluation principles and estimation; framework case analyses. Counterevidence/scope was checked at No controlled production validation; the formal model depends on chosen distance metrics and perturbation distributions. It does not prove that “QUIVER: A Formal Framework for Quantifying Perturbation Propagation and Bifurcation in Compound AI Systems” generalizes to undisclosed models, hardware, precision, context/action length, concurrency, SLO, failure distribution or production tail; author-reported comparisons remain conditional on the paper's disclosed evaluator and workload.<!-- claim:SF-2026-ARXIV-2605-23956:end -->

Disposition=`No Change — Existing Coverage`；该结论来自独立 exact-v1 与 current owner+adjacent comparison，不由 validator 代签。
<!-- review:SF-2026-ARXIV-2605-23956:end -->

<!-- review:SF-2026-ARXIV-2605-23986:start -->
#### MemForest: An Efficient Agent Memory System with Hierarchical Temporal Indexing

问题与机制：MemForest: An Efficient Agent Memory System with Hierarchical Temporal Indexing 提出的具体变化是：To address these challenges, we present MemForest, a memory framework that reformulates agent memory as a write-efficient temporal data-management problem. 摘要中的长期系统挑战为：hierarchical temporal indexing removes state-dependent generation from the memory write critical path。它可能改变 `AGENT-MEMORY` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“These results show that MemForest reduces memory-freshness latency while retaining strong answer quality.”暂不作为最终证据。

Evaluation contract：These results show that MemForest reduces memory-freshness latency while retaining strong answer quality.

Evidence locators：Method=`section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt)`；Evaluation=`Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only`；Counterevidence=`Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup`。

Trade-off / failure：新增 controller、metadata、verification、communication 或 runtime state 都带来成本；只在 exact-v1 披露 workload/evaluator 内成立，未披露的硬件、精度、长度、batch、并发、SLO、seed 与 artifact commit 为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-23986:start -->只支持 exact-v1 披露设置中的机制与结果；旧路径在新增 owner/证据/控制责任不成立时继续共存。<!-- claim:SF-2026-ARXIV-2605-23986:end -->

Books Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-23986:end -->

<!-- review:SF-2026-ARXIV-2605-23988:start -->
#### TSFLora: Token-Compressed Split Fine-Tuning for Wireless Edge Networks

问题与 changed constraint：split fine-tuning compresses activation tokens before transmission, coupling accuracy, uplink traffic, server compute and frozen-backbone identity

机制与 ownership：Experiments on ViT models over CIFAR-10, CIFAR-100, and TinyImageNet show that TSFLora achieves up to \textbf{6.8$\times$} communication reduction and \textbf{41\%} memory saving while maintaining competitive accuracy. owner=`TRAIN-DISTRIBUTED-TRAINING`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.23988v1 — §II Architecture and Workflow; §III Token Compression (official exact-v1 HTML)`；Evaluation=`arXiv:2605.23988v1 — §VI Experiments (official exact-v1 HTML)`。

Trade-off / failure：`arXiv:2605.23988v1 — §VII Conclusion; no dedicated limitations section (official exact-v1 HTML)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-23988:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-23988:end -->

Books Decision=`Integrate`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-23988:end -->

<!-- review:SF-2026-ARXIV-2605-23993:start -->
#### Nano World Models: A Minimalist Implementation of Future Video Prediction

问题与 changed constraint：a reproducible world-model substrate versions objective, action conditioning, latent state, rollout and evaluation rather than comparing entangled codebases

机制与 ownership：We introduce Nano World Models, a minimalist codebase for future video prediction centered around diffusion forcing. owner=`MULTIMODAL-WORLD-MODELS`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.23993v1 — §3 Diffusion-Forcing Interface and Experimental Substrate (official exact-v1 HTML)`；Evaluation=`arXiv:2605.23993v1 — §4 Findings (official exact-v1 HTML)`。

Trade-off / failure：`arXiv:2605.23993v1 — §5 Conclusion; no dedicated limitations section (official exact-v1 HTML)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-23993:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-23993:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-23993:end -->

<!-- review:SF-2026-ARXIV-2605-24004:start -->
#### Reason--Imagine--Act: Closed-Loop LLM Decision Making with World Models for Autonomous Driving

**问题与机制。** We propose Reason--Imagine--Act (RIA), a closed-loop framework that couples an LLM reasoner with an action-conditioned world model for online safety verification. 系统 owner=`MULTIMODAL-EMBODIED-VLA`。

**Exact-v1。** Method=`§III Reason–Imagine–Act world-model verification loop`；Evaluation=`§IV CARLA closed-loop evaluation`；Limitations/Counterevidence=`§V Conclusion; simulator and discrete-action-template boundary`。

<!-- claim:SF-2026-ARXIV-2605-24004:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-24004:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-24004:end -->

<!-- review:SF-2026-ARXIV-2605-24006:start -->
#### A Tabular Schedule Abstraction for Communication-Aware Evaluation of Pipeline-Parallel LLM Training

**问题与机制。** In this work, we introduce a tabular schedule abstraction and a unified multi-abstraction methodology that connects formula-based reasoning, idealized schedule tables, and communication-aware execution simulation. 系统 owner=`TRAIN-PIPELINE-PARALLEL`。

**Exact-v1。** Method=`§III tabular schedule abstraction`；Evaluation=`§IV communication-aware schedule experiments`；Limitations/Counterevidence=`§V Conclusion and simulator boundary`。

<!-- claim:SF-2026-ARXIV-2605-24006:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-24006:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-24006:end -->

<!-- review:SF-2026-ARXIV-2605-24022:start -->
#### Adaptive KV Cache Reuse for Fast Long-Context LLM Serving

**问题与机制。** Evaluations on mainstream LLMs and long-context tasks show that CacheTune achieves 3.72x-4.86x TTFT speedup and 3.93x-6.21x higher throughput while maintaining generation quality close to full recompute. 系统 owner=`INFER-KV-CACHE`。

**Exact-v1。** Method=`§3 CacheTune Adaptive KV Reuse`；Evaluation=`§5 Evaluation`；Limitations/Counterevidence=`§5.5 Limitations; §6 Conclusion`。

<!-- claim:SF-2026-ARXIV-2605-24022:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-24022:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-24022:end -->

<!-- review:SF-2026-ARXIV-2605-24036:start -->
#### Intent-Driven Computing: A Computational Model for Governed Autonomous Systems

**问题与机制。** Programming languages assume programs directly execute effects. Programming languages assume programs directly execute effects. 系统 owner=`AGENT-PLATFORM`。

**Exact-v1。** Method=`§4 Intent-Driven Computational Model`；Evaluation=`§8 Worked Governance Semantics`；Limitations/Counterevidence=`§10 Limitations and Scope`；正文 sha256=`1eec7ae37f60c2236eeed917aec705e4224a2a0d518f318bc6a604a15c121a41`。

<!-- claim:SF-2026-ARXIV-2605-24036:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-24036:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-24036:end -->

<!-- review:SF-2026-ARXIV-2605-24042:start -->
#### Hidden-State Privacy Has an Empty Middle

**问题与机制。** Of $1{,}536$ Gaussian release covariances we tested for single-layer hidden-state privacy, zero achieve both moderate utility and moderate privacy against an adaptive retrieval attacker. These results reframe hidden-state release from mechanism-design within the Gaussian class to architecture or release co-design. 系统 owner=`PLATFORM-SECURITY`。

**Exact-v1。** Method=`§3 Hidden-State Privacy Feasibility Regions`；Evaluation=`§7–§8 Experimental Tests`；Limitations/Counterevidence=`§9 Limitations and Future Questions`；正文 sha256=`570f86970a0df097c2ce9229704f9a83c3ae36eabf0b4361316eccbc058ae683`。

<!-- claim:SF-2026-ARXIV-2605-24042:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-24042:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-24042:end -->

<!-- review:SF-2026-ARXIV-2605-24044:start -->
#### RED: Adaptive Real-Time DAG Scheduling for Robotic Inference under Environmental Dynamics

**问题与机制。** Robots deployed in dynamic environments must contend with environment-driven changes that reshape computation at runtime: new tasks may appear, precedence relations can shift, and overall workload structure evolves, all of which degrade performance, especially when multi-task inference is required under tight resource and real-time budgets. We present RED, a real-time scheduling framework for multi-task deep neural network workloads on resource-constrained robotic platforms that adapts to Robotic Environmental Dynamics (RED) while preserving end-to-end timing guarantees under modeling assumptions. 系统 owner=`INFER-SCHEDULING`。

**Exact-v1。** Method=`§2.2 Challenges due to the MIMONet Architecture; §3 System Model and Problem Formulation; §3.4 Problem Formulation`；Evaluation=`§5 Evaluation; §5.1 Experimental Setups; §5.5 Overhead Analysis`；Limitations/Counterevidence=`§7 Discussion; §9 Conclusion`；正文 sha256=`d6cd3302598aa903e9c7200f7f725ca3747ced003157d0aecd07e5b6d92fc7de`。

<!-- claim:SF-2026-ARXIV-2605-24044:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-24044:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-24044:end -->

<!-- review:SF-2026-ARXIV-2605-24050:start -->
#### More Skills, Worse Agents? Skill Shadowing Degrades Performance When Expanding Skill Libraries

**问题与机制。** Skill libraries allow LLM agents to load task-specific instructions on demand, letting non-expert users solve domain-specific tasks through natural language without knowing which skills exist or how they work. Moreover, we propose to decompose the pass rate drop by conditioning on the skill(s) invocation -- which skills the agent selects during a trajectory -- into two effects: \emph{skill shadowing}, where the agent selects wrong skills more often as the library expands, and \emph{context overhead}, where the enlarged context degrades execution even when selection is correct. 系统 owner=`AGENT-PLATFORM`。

**Exact-v1。** Method=`§3 Skill-Shadowing Mechanism and Library Expansion Protocol`；Evaluation=`§4 Evaluation`；Limitations/Counterevidence=`§5 Conclusion and tested-library/model boundary`；正文 sha256=`bcb4f4766c6e6987b1c569b560bb4c19636dcab9eb9125d98e3ba5c8c5450002`。

<!-- claim:SF-2026-ARXIV-2605-24050:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-24050:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-24050:end -->

<!-- review:SF-2026-ARXIV-2605-24060:start -->
#### Same Ranking, Different Winner: How Scoring Targets Shape LLM Memory Benchmarks

**问题与机制。** We show that this scoring-target choice is often left implicit and can materially change benchmark conclusions. owner=`PLATFORM-EVALUATION-SYSTEM`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§3 memory benchmark scoring-target intervention`；Evaluation=`§4–§5 controlled benchmark evaluation`；Limitations/Counterevidence=`§7 Limitations; tested-memory systems and tasks`。

<!-- claim:SF-2026-ARXIV-2605-24060:start -->Same Ranking, Different Winner: How Scoring Targets Shape LLM Memory Benchmarks only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-24060:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24060:end -->

<!-- review:SF-2026-ARXIV-2605-24069:start -->
#### When the Manual Lies: A Realistic Benchmark to Evaluate MCP Poisoning Attacks for LLM Agents

**问题与机制。** To rigorously and systematically evaluate this emerging threat, we introduce the MCP-TDP Security Benchmark. owner=`AGENT-MCP`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 MCP Poisoning Threat Model and Benchmark`；Evaluation=`§4 Evaluation`；Limitations/Counterevidence=`§5 Limitations and manual/registry boundary`。

<!-- claim:SF-2026-ARXIV-2605-24069:start -->When the Manual Lies: A Realistic Benchmark to Evaluate MCP Poisoning Attacks for LLM Agents only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-24069:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24069:end -->

<!-- review:SF-2026-ARXIV-2605-24117:start -->
#### SkillEvolBench: Benchmarking the Evolution from Episodic Experience to Procedural Skills

**问题与机制。** We introduce SkillEvolBench, a diagnostic benchmark for evaluating this step from experience reuse to skill formation. owner=`AGENT-PLATFORM`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§3 SkillEvolBench lifecycle/evolution protocol`；Evaluation=`§4–§5 benchmark protocol and experiments`；Limitations/Counterevidence=`§6 Discussion; benchmark coverage does not prove deployment safety`。

<!-- claim:SF-2026-ARXIV-2605-24117:start -->SkillEvolBench: Benchmarking the Evolution from Episodic Experience to Procedural Skills only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-24117:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24117:end -->

<!-- review:SF-2026-ARXIV-2605-24134:start -->
#### ProofAgent Harness: Open Infrastructure for Adversarial Evaluation of AI Agents

**问题与机制。** We introduce ProofAgent Harness, open infrastructure for scalable, auditable, and adversarial AI agent evaluation. owner=`PLATFORM-EVALUATION-SYSTEM`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 ProofAgent Harness Architecture`；Evaluation=`§5 Adversarial Agent Evaluation`；Limitations/Counterevidence=`§6 Limitations and proof-domain boundary`。

<!-- claim:SF-2026-ARXIV-2605-24134:start -->ProofAgent Harness: Open Infrastructure for Adversarial Evaluation of AI Agents only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-24134:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24134:end -->

<!-- review:SF-2026-ARXIV-2605-24154:start -->
#### Palette: A Modular, Controllable, and Efficient Framework for On-demand Authorized Safety Alignment Relaxation in LLMs

**问题与机制。** To this end, we propose \textsc{Palette}, a modular, controllable, and efficient framework that selectively relaxes refusal behavior on authorized target domains while preserving standard safety elsewhere. owner=`PLATFORM-SECURITY`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 Palette Authorized Safety-Relaxation Modules`；Evaluation=`§5 Safety/Utility Evaluation`；Limitations/Counterevidence=`§6 Limitations and authorization boundary`。

<!-- claim:SF-2026-ARXIV-2605-24154:start -->Palette: A Modular, Controllable, and Efficient Framework for On-demand Authorized Safety Alignment Relaxation in LLMs only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-24154:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24154:end -->

<!-- review:SF-2026-ARXIV-2605-24168:start -->
#### Inference Time Context Sparsity: Illusion or Opportunity?

**问题与机制。** Second, we perform an extensive study of sparsity in LLMs spanning 20 models across five model families, varying context lengths, and different sparsity levels. owner=`AGENT-CONTEXT`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 Inference-Time Context-Sparsity Analysis`；Evaluation=`§4 Evaluation`；Limitations/Counterevidence=`§5 Discussion and model/task boundary`。

<!-- claim:SF-2026-ARXIV-2605-24168:start -->Inference Time Context Sparsity: Illusion or Opportunity? only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-24168:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24168:end -->

<!-- review:SF-2026-ARXIV-2605-24183:start -->
#### AvalancheBench: Evaluating Enterprise Data Agents Through Latent World Recovery

**问题与机制。** We introduce AvalancheBench, a benchmark for evaluating enterprise data agents through \emph{latent world recovery}. owner=`PLATFORM-EVALUATION-SYSTEM`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§2–§3 AvalancheBench latent-world recovery protocol`；Evaluation=`§4 early experiments`；Limitations/Counterevidence=`§5 Limitations; synthetic/latent-world scope`。

<!-- claim:SF-2026-ARXIV-2605-24183:start -->AvalancheBench: Evaluating Enterprise Data Agents Through Latent World Recovery only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-24183:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24183:end -->

<!-- review:SF-2026-ARXIV-2605-24197:start -->
#### A Sober Look at Agentic Misalignment in Automated Workflows

**问题与机制。** We study a class of emergent misalignment in multi-agent systems (MAS), with a focus on automated workflows, which we refer to agentic misalignment. owner=`AGENT-MULTI-AGENT`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§3 formulation; §4 evidence-attribution mechanism`；Evaluation=`§5 experiments`；Limitations/Counterevidence=`Appendix B Limitations; simulated-agent and attribution boundary`。

<!-- claim:SF-2026-ARXIV-2605-24197:start -->A Sober Look at Agentic Misalignment in Automated Workflows only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-24197:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24197:end -->

<!-- review:SF-2026-ARXIV-2605-24202:start -->
#### When Does Multi-Agent RL Improve LLM Workflows? Workflow, Scale, and Policy-Sharing Tradeoffs

**问题与机制。** We study when end-to-end RL training of multi-agent LLM workflows improves over their base models, comparing Shared-Policy training, where all roles update one policy, with Isolated-Policy training, where each role has its own parameters. owner=`TRAIN-RLHF`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§3 multi-agent RL workflow and policy-sharing mechanism`；Evaluation=`§4 experiments`；Limitations/Counterevidence=`§5 Discussion; policy-sharing topology and task boundary`。

<!-- claim:SF-2026-ARXIV-2605-24202:start -->When Does Multi-Agent RL Improve LLM Workflows? Workflow, Scale, and Policy-Sharing Tradeoffs only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-24202:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24202:end -->

<!-- review:SF-2026-ARXIV-2605-24213:start -->
#### Towards Evaluation Engineering: An Empirical Study of ML Evaluation Harnesses in the Wild

**问题与机制。** We present an empirical study of 57 evaluation harnesses, deriving a five-stage harness model and classifying 16,560 issues by workflow stage and root cause. owner=`PLATFORM-EVALUATION-SYSTEM`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 Evaluation-Harness Measurement Method`；Evaluation=`§5 Empirical Harness Study`；Limitations/Counterevidence=`§6 Threats to Validity`。

<!-- claim:SF-2026-ARXIV-2605-24213:start -->Towards Evaluation Engineering: An Empirical Study of ML Evaluation Harnesses in the Wild only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-24213:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24213:end -->

<!-- review:SF-2026-ARXIV-2605-24216:start -->
#### Agent-ToM: Learning to Monitor Autonomous LLM Agents via Theory-of-Mind Reasoning

**问题与机制。** We propose \textbf{Agent-ToM}, a learning-to-monitor framework grounded in Theory-of-Mind (ToM) reasoning for security analysis of autonomous agents. owner=`PLATFORM-SECURITY`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§3 Agent-ToM learning-to-monitor architecture`；Evaluation=`§4–§5 monitoring evaluation`；Limitations/Counterevidence=`§6 Limitations; ToM inference is a sensor, not intent ground truth`。

<!-- claim:SF-2026-ARXIV-2605-24216:start -->Agent-ToM: Learning to Monitor Autonomous LLM Agents via Theory-of-Mind Reasoning only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-24216:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24216:end -->

<!-- review:SF-2026-ARXIV-2605-24217:start -->
#### Identifying and Mitigating Systemic Measurement Bias in Production LLM Inference Benchmarks

**问题与机制。** We demonstrate that widely used benchmarking utilities rely on single-process, asyncio-driven architectures that introduce fundamental client-side queuing bottlenecks under high concurrency. owner=`PLATFORM-EVALUATION-SYSTEM`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 Production-Inference Measurement-Bias Model`；Evaluation=`§4 Benchmark Evaluation`；Limitations/Counterevidence=`§5 Mitigation and production-scope boundary`。

<!-- claim:SF-2026-ARXIV-2605-24217:start -->Identifying and Mitigating Systemic Measurement Bias in Production LLM Inference Benchmarks only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-24217:end -->

Books Decision=`Integrate`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24217:end -->

<!-- review:SF-2026-ARXIV-2605-24219:start -->
#### Beyond Final Answers: Auditing Trajectory-Level Hallucinations in Multi-Agent Industrial Workflows

**问题与机制。** We present Trajel, a dataset and evaluation framework for auditing trajectory-level hallucinations in multi-agent industrial workflows. owner=`PLATFORM-EVALUATION-SYSTEM`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 Trajectory-Level Hallucination Audit`；Evaluation=`§5 Multi-Agent Workflow Evaluation`；Limitations/Counterevidence=`§6 Limitations and industrial-workflow boundary`。

<!-- claim:SF-2026-ARXIV-2605-24219:start -->Beyond Final Answers: Auditing Trajectory-Level Hallucinations in Multi-Agent Industrial Workflows only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-24219:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24219:end -->

<!-- review:SF-2026-ARXIV-2605-24220:start -->
#### Polar: Agentic RL on Any Harness at Scale

**问题与机制。** This decoupled design makes Polar agnostic to agent harnesses, training infrastructure, and RL algorithms while improving compute utilization for long-running agent workloads. owner=`TRAIN-RLHF`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 Polar Harness-Agnostic Agentic-RL Runtime`；Evaluation=`§5 Scale Evaluation`；Limitations/Counterevidence=`§6 Limitations and harness/reward boundary`。

<!-- claim:SF-2026-ARXIV-2605-24220:start -->Polar: Agentic RL on Any Harness at Scale only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-24220:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24220:end -->

<!-- review:SF-2026-ARXIV-2605-24229:start -->
#### How Well Do Models Follow Their Constitutions?

**问题与机制。** We propose a multi-method audit pipeline that treats each lab's published specification as an auditable target: it decomposes the specification into atomic testable tenets (205 for Anthropic, 197 for OpenAI), generates multi-turn adversarial scenarios with the Petri auditing agent (Anthropic, 2025b), runs a modified SURF-style rubric search (Murray et al., 2026) to catch shallow single-turn failures Petri misses, validates flagged transcripts against the relevant specification, and compares the findings against the lab's own published system card. owner=`PLATFORM-EVALUATION-SYSTEM`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§3 atomic-tenet extraction and adversarial audit pipeline`；Evaluation=`§4–§5 multi-turn constitution-adherence evaluation`；Limitations/Counterevidence=`§6 Limitations; published-spec and evaluator boundary`。

<!-- claim:SF-2026-ARXIV-2605-24229:start -->How Well Do Models Follow Their Constitutions? only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-24229:end -->

Books Decision=`Integrate`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24229:end -->

<!-- review:SF-2026-ARXIV-2605-24245:start -->
#### Deep-Research Agents Can Be Poisoned via User-Generated Content

**问题与机制。** We show that for many common search topics, they repeatedly retrieve the same user-generated content (UGC) pages from platforms such as Reddit and Wikipedia. owner=`PLATFORM-SECURITY`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 User-Generated-Content Poisoning Attack`；Evaluation=`§5 Deep-Research Agent Evaluation`；Limitations/Counterevidence=`§6 Limitations and source/ecosystem boundary`。

<!-- claim:SF-2026-ARXIV-2605-24245:start -->Deep-Research Agents Can Be Poisoned via User-Generated Content only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-24245:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24245:end -->

<!-- review:SF-2026-ARXIV-2605-24247:start -->
#### Improving Labeling Consistency with Detailed Constitutional Definitions and AI-Driven Evaluation

**问题与机制。** We propose and demonstrate the efficacy of an AI-driven workflow in which AI helps write a per-category constitution that defines the label in enough detail to cover edge cases, and a frontier LLM interprets it on each input to produce the golden label more consistently and accurately than humans reading the same document. owner=`TRAIN-DATA`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§3 detailed constitutional definitions and AI-assisted labeling workflow`；Evaluation=`§4–§5 label-consistency evaluation`；Limitations/Counterevidence=`§6 Limitations; category/specification and annotator boundary`。

<!-- claim:SF-2026-ARXIV-2605-24247:start -->Improving Labeling Consistency with Detailed Constitutional Definitions and AI-Driven Evaluation only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-24247:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24247:end -->

<!-- review:SF-2026-ARXIV-2605-24248:start -->
#### Attested Tool-Server Admission: A Security Extension to the Model Context Protocol

**问题与机制。** We give the wire format, the verification algorithm, a security analysis, and an LLM-driven adversarial evaluation; we then state the design in normative Request-for-Comments (RFC 2119) form -- schema, verification rules, error registry, well-known registration, and machine-checkable conformance vectors -- so it can be adopted as an MCP addendum rather than reinvented. owner=`AGENT-MCP`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 Attested Tool-Server Admission Protocol`；Evaluation=`§5 Security Evaluation`；Limitations/Counterevidence=`§6 Limitations and attestation-root boundary`。

<!-- claim:SF-2026-ARXIV-2605-24248:start -->Attested Tool-Server Admission: A Security Extension to the Model Context Protocol only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-24248:end -->

Books Decision=`Integrate`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24248:end -->

<!-- review:SF-2026-ARXIV-2605-24259:start -->
#### Resident KV Claims: A Conformance Contract for Future Reuse under Active KV Pressure

**问题与机制。** We introduce resident KV claims, a conformance contract that binds future-reuse intent to a materialization predicate, lifecycle state, active/resident feasibility outcome, and claim-level telemetry. owner=`INFER-KV-CACHE`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 Resident-KV Conformance Contract`；Evaluation=`§5 Active-Pressure Evaluation`；Limitations/Counterevidence=`§6 Limitations and cache-manager boundary`。

<!-- claim:SF-2026-ARXIV-2605-24259:start -->Resident KV Claims: A Conformance Contract for Future Reuse under Active KV Pressure only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-24259:end -->

Books Decision=`Integrate`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24259:end -->

<!-- review:SF-2026-ARXIV-2605-24279:start -->
#### ContextEcho: A Benchmark for Persona Drift in Long Agentic-Coding Sessions

**问题与机制。** We introduce ContextEcho, a benchmark and reusable harness for measuring persona drift at deployment scale. owner=`AGENT-CONTEXT`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§3 ContextEcho snapshot-then-probe deployment harness`；Evaluation=`§4–§5 long agentic-coding session evaluation`；Limitations/Counterevidence=`§6 Limitations; persona probes and coding-session boundary`。

<!-- claim:SF-2026-ARXIV-2605-24279:start -->ContextEcho: A Benchmark for Persona Drift in Long Agentic-Coding Sessions only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-24279:end -->

Books Decision=`Integrate`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24279:end -->

<!-- review:SF-2026-ARXIV-2605-24286:start -->
#### Faithfulness as Information Flow: Evaluating and Training Faithful Chain-of-Thought Reasoning

**问题与机制。** We study CoT faithfulness through a structural information-flow perspective: faithful reasoning should route answer-relevant information through the mediated path from prompt to CoT to answer, rather than through a direct prompt-to-answer shortcut. owner=`PLATFORM-EVALUATION-SYSTEM`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§3 information-flow faithfulness criteria and diagnostics`；Evaluation=`§4–§5 faithfulness evaluation/training`；Limitations/Counterevidence=`§6 Limitations; diagnostic proxies do not reveal hidden computation`。

<!-- claim:SF-2026-ARXIV-2605-24286:start -->Faithfulness as Information Flow: Evaluating and Training Faithful Chain-of-Thought Reasoning only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-24286:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24286:end -->

<!-- review:SF-2026-ARXIV-2605-24299:start -->
#### LLMs Show No Signs Of Individuated Metacognition

**问题与机制。** Confidence-weighted routing, selective abstention, and ensemble weighting all assume that a model's stated confidence is informative about its capability on the question being asked. owner=`PLATFORM-EVALUATION-SYSTEM`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§3 factor-analysis decomposition of elicited confidence`；Evaluation=`§4 pairwise calibration across twenty models/six benchmarks`；Limitations/Counterevidence=`§5–§6 Limitations; elicited-confidence and tested-benchmark boundary`。

<!-- claim:SF-2026-ARXIV-2605-24299:start -->LLMs Show No Signs Of Individuated Metacognition only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-24299:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24299:end -->

<!-- review:SF-2026-ARXIV-2605-24309:start -->
#### Reframing LLM Agent Security as an Agent-Human Interaction Problem

**问题与机制。** Third, we propose a three-direction research agenda and call for AHI security to be recognized as a first-class research citizen, one that demands its own design principles, evaluation methods, and theoretical foundations. owner=`PLATFORM-SECURITY`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§3 agent-human security mechanism taxonomy`；Evaluation=`§4 audit of papers, production agents and plugins`；Limitations/Counterevidence=`§5 Limitations; observational taxonomy does not prove mechanism efficacy`。

<!-- claim:SF-2026-ARXIV-2605-24309:start -->Reframing LLM Agent Security as an Agent-Human Interaction Problem only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-24309:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24309:end -->

<!-- review:SF-2026-ARXIV-2605-24312:start -->
#### Five Queries Are Enough: Query-Efficient and Surrogate-Free Membership Inference Attacks on RAG via Entailment

**问题与机制。** However, this design introduces a new privacy risk: model outputs may signal the presence of specific documents in the retrieval corpus, enabling membership inference attacks (MIAs) that leak sensitive information. owner=`AGENT-RAG`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 Entailment-Based RAG Membership Inference`；Evaluation=`§4 Five-Query Evaluation`；Limitations/Counterevidence=`§5 Limitations and black-box-access boundary`。

<!-- claim:SF-2026-ARXIV-2605-24312:start -->Five Queries Are Enough: Query-Efficient and Surrogate-Free Membership Inference Attacks on RAG via Entailment only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-24312:end -->

Books Decision=`Integrate`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24312:end -->

<!-- review:SF-2026-ARXIV-2605-24326:start -->
#### ScaleAcross Explorer: Exploring Communication Optimization for Scale-Across AI Model Training

**问题与机制。** As infrastructure expands, the system design space becomes increasingly intricate, encompassing new model architectures, hardware heterogeneity, and evolving communication patterns. owner=`TRAIN-DISTRIBUTED-TRAINING`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3–§6 placement, scheduling, network and ScaleAcross Explorer`；Evaluation=`§6.3 Evaluation Results; Appendix A testbed/simulation settings`；Limitations/Counterevidence=`§7 Lessons Learned; §8 Conclusion; cross-building testbed/simulator scope`。

<!-- claim:SF-2026-ARXIV-2605-24326:start -->ScaleAcross Explorer: Exploring Communication Optimization for Scale-Across AI Model Training only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24326:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24326:end -->

<!-- review:SF-2026-ARXIV-2605-24391:start -->
#### MX-SAFE: Versatile Inference- and Training-Proof Microscaling Format with On-the-Fly Exponent and Mantissa Bit Allocation

**问题与机制。** In this work, we present a versatile MXFP format, called MX-SAFE (MXSF in short), that adaptively uses two modes, i.e., a wider mantissa mode (FP8 E2M5) and a subnormal FP mode (FP5 E3M2), to support both training and direct-cast inference. owner=`INFER-TENSORRT-LLM`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§IV MX-SAFE format; §V accelerator`；Evaluation=`§VI Experimental Results`；Limitations/Counterevidence=`§VII Conclusion; tested MXSF hardware/model boundary`。

<!-- claim:SF-2026-ARXIV-2605-24391:start -->MX-SAFE: Versatile Inference- and Training-Proof Microscaling Format with On-the-Fly Exponent and Mantissa Bit Allocation only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24391:end -->

Books Decision=`Integrate`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24391:end -->

<!-- review:SF-2026-ARXIV-2605-24420:start -->
#### Batch Normalization Amplifies Memorization and Privacy Risks

**问题与机制。** We conduct an extensive empirical study using three complementary approaches: (i) unintended memorization of out-of-distribution training samples, (ii) per-sample influence measured via gradient norms, and (iii) susceptibility to membership inference attacks (MIA). owner=`PLATFORM-SECURITY`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§3 Methodology; §5 theory; §6 mitigation`；Evaluation=`§4 Experiments; §4.3 membership inference`；Limitations/Counterevidence=`Appendix A.3 theoretical limitations; tested normalization/model/data boundary`。

<!-- claim:SF-2026-ARXIV-2605-24420:start -->Batch Normalization Amplifies Memorization and Privacy Risks only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24420:end -->

Books Decision=`Integrate`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24420:end -->

<!-- review:SF-2026-ARXIV-2605-24421:start -->
#### Poisoning the Watchtower: Prompt Injection Attacks Against LLM-Augmented Security Operations Through Adversarial Log Content

**问题与机制。** We study a structural failure mode of this design: many log fields are attacker controlled. owner=`PLATFORM-SECURITY`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§2 Threat Model; §3 taxonomy; §4 pipeline/defenses`；Evaluation=`§5 Experiments`；Limitations/Counterevidence=`§6.4 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-24421:start -->Poisoning the Watchtower: Prompt Injection Attacks Against LLM-Augmented Security Operations Through Adversarial Log Content only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24421:end -->

Books Decision=`Integrate`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24421:end -->

<!-- review:SF-2026-ARXIV-2605-24425:start -->
#### Momentum Streams for Optimizer-Inspired Transformers

**问题与机制。** A controlled ablation and supporting theory show that momentum, not preconditioning, is the main source of the gain. owner=`MODEL-TRANSFORMER-LAYER`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§§3–5 optimizer view, optimizer-inspired block and momentum stream`；Evaluation=`§4.2; §§5–6; Appendix D Experimental Details`；Limitations/Counterevidence=`§7 Conclusion; architecture/scale/recipe boundary`。

<!-- claim:SF-2026-ARXIV-2605-24425:start -->Momentum Streams for Optimizer-Inspired Transformers only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24425:end -->

Books Decision=`Integrate`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24425:end -->

<!-- review:SF-2026-ARXIV-2605-24426:start -->
#### SEAL: Synergistic Co-Evolution of Agents and Learning Environments

**问题与机制。** We identify this structural gap as \emph{Agent-Environment Misalignment}: the agent's capability frontier changes during training, while the environment that provides supervision remains static or only weakly coupled to the agent's revealed failures. owner=`TRAIN-RLHF`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§3 verifier-grounded diagnosis, interface evolution and advantage reweighting`；Evaluation=`§4 Experiments; Appendix C controlled protocol`；Limitations/Counterevidence=`§5 Conclusion and Limitations`。

<!-- claim:SF-2026-ARXIV-2605-24426:start -->SEAL: Synergistic Co-Evolution of Agents and Learning Environments only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24426:end -->

Books Decision=`Integrate`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24426:end -->

<!-- review:SF-2026-ARXIV-2605-24461:start -->
#### Provisioning to Runtime Optimization of a 100 MW-Scale AI Cluster

**问题与机制。** We present detailed power measurements for a 150 MW datacenter hosting a cluster of 83K GB200 GPUs. owner=`PLATFORM-GPU-SCHEDULER`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 power hierarchy; §§4–6 provisioning, validation and active operation`；Evaluation=`§4.2 empirical data; §§5–7 deployment/runtime measurements`；Limitations/Counterevidence=`§8 Research Wishlist; §10 Conclusion; single 150MW/83K-GB200 site boundary`。

<!-- claim:SF-2026-ARXIV-2605-24461:start -->Provisioning to Runtime Optimization of a 100 MW-Scale AI Cluster only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24461:end -->

Books Decision=`Integrate`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24461:end -->

<!-- review:SF-2026-ARXIV-2605-24468:start -->
#### SAM: State-Adaptive Memory for Long-Horizon Reasoning Agent

**问题与机制。** To this end, we propose State-Adaptive Memory~(SAM), a standalone framework that consolidates ongoing interaction into compact memory cues while preserving raw trajectory pages for intent-driven recall. owner=`AGENT-MEMORY`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§2.2–§2.3 State-Adaptive Memory and optimization`；Evaluation=`§3 Experiments; §4 Discussions`；Limitations/Counterevidence=`Appendix A Limitations and Broader Impact`。

<!-- claim:SF-2026-ARXIV-2605-24468:start -->SAM: State-Adaptive Memory for Long-Horizon Reasoning Agent only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24468:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24468:end -->

<!-- review:SF-2026-ARXIV-2605-24517:start -->
#### ECHO: Terminal Agents Learn World Models for Free

**问题与机制。** We introduce ECHO (Environment Cross-entropy Hybrid Objective), a hybrid objective that combines the standard policy-gradient loss on action tokens with an auxiliary loss that trains the policy to predict environment observation tokens resulting from its own actions. owner=`MULTIMODAL-WORLD-MODELS`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 Method; ECHO hybrid policy/observation objective`；Evaluation=`§4 Experimental Setup; §5 Results`；Limitations/Counterevidence=`§7 Conclusion; terminal-environment and training-only auxiliary-loss boundary`。

<!-- claim:SF-2026-ARXIV-2605-24517:start -->ECHO: Terminal Agents Learn World Models for Free only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24517:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24517:end -->

<!-- review:SF-2026-ARXIV-2605-24547:start -->
#### RL with Learnable Textual Feedback: A Bilevel Approach

**问题与机制。** We formalize this coupling as a Stackelberg bilevel program and derive Bilevel Natural Language Actor-Critic (Bi-NAC), which jointly trains a critic to generate reward-improving feedback and an actor to exploit it. owner=`TRAIN-RLHF`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§2 problem formulation; §3 bilevel natural-language actor-critic`；Evaluation=`§4 Experiments; Appendix A.5 efficiency`；Limitations/Counterevidence=`§5 Conclusion; tested task/model and higher-order-gradient boundary`。

<!-- claim:SF-2026-ARXIV-2605-24547:start -->RL with Learnable Textual Feedback: A Bilevel Approach only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24547:end -->

Books Decision=`Integrate`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24547:end -->

<!-- review:SF-2026-ARXIV-2605-24558:start -->
#### Position: AI for Science Should Treat Measurement-to-Dataset Pipelines as Inference Components

**问题与机制。** \textbf{We argue that these measurement-to-dataset pipelines are inference components: treating their outputs as ``given data'' freezes an observation model and obscures uncertainty over feasible pipeline choices.} We identify three failure modes arising from this ``frozen lens'': \textbf{(C1) hidden hypothesis space}, where the released dataset does not specify the pipeline configuration or its validity conditions; \textbf{(C2) uncertified transportability}, where a pipeline may be documented but its regime of validity is untested, so failures under distribution shift cannot be adjudicated; \textbf{(C3) ungoverned multiplicity}, where many defensible pipelines exist and dispersion is real but not propagated into uncertainty-aware evidence. owner=`TRAIN-DATA`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§§2–3 measurement pipeline as observation/inference component`；Evaluation=`§4 empirical audit; §5 alternative views`；Limitations/Counterevidence=`§6 Call to Action; position/audit does not prove a universal pipeline`。

<!-- claim:SF-2026-ARXIV-2605-24558:start -->Position: AI for Science Should Treat Measurement-to-Dataset Pipelines as Inference Components only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24558:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24558:end -->

<!-- review:SF-2026-ARXIV-2605-24579:start -->
#### WhenLoss: Diagnosing Write and Retrieval Bottlenecks in Long-Context Memory Systems

**问题与机制。** We introduce a four-condition diagnostic protocol that evaluates a fixed reader under truncated full context (TFC), oracle evidence (OE), complete stored memory (CSM), and retrieved memory (RM). owner=`AGENT-MEMORY`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 four-condition diagnostic; §4 expected predictive compression`；Evaluation=`§5 Experimental Setup; §6 Results; §7 Analysis`；Limitations/Counterevidence=`§7 Analysis and §8 Conclusion; tested readers, memories and two benchmarks`。

<!-- claim:SF-2026-ARXIV-2605-24579:start -->WhenLoss: Diagnosing Write and Retrieval Bottlenecks in Long-Context Memory Systems only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24579:end -->

Books Decision=`Integrate`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24579:end -->

<!-- review:SF-2026-ARXIV-2605-24583:start -->
#### Measuring Alignment-Induced Activation Shifts Correctly: A Template-Controlled Difference-in-Differences Protocol

**问题与机制。** We show the obvious way to form this matrix is confounded. owner=`PLATFORM-EVALUATION-SYSTEM`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§§2–4 separability metric and three confound-control tests`；Evaluation=`§§5–6 calibration and current-alignment audit`；Limitations/Counterevidence=`§7 Scope; §8 open problem and failed spectral-gap claim`。

<!-- claim:SF-2026-ARXIV-2605-24583:start -->Measuring Alignment-Induced Activation Shifts Correctly: A Template-Controlled Difference-in-Differences Protocol only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24583:end -->

Books Decision=`Integrate`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24583:end -->

<!-- review:SF-2026-ARXIV-2605-24598:start -->
#### Hera: Learning Long-Horizon Coordination for Device-Cloud Collaborative LLM Agents

**问题与机制。** To address this issue, we present Hera, a step-level device--cloud LLM agent coordinator for long-horizon tasks achieving a strong performance--cost Pareto frontier. owner=`AGENT-MULTI-AGENT`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§5 Hera step-level device-cloud coordinator`；Evaluation=`§6 Experiment; §6.2–§6.4`；Limitations/Counterevidence=`Appendix E Limitations and Future Work`。

<!-- claim:SF-2026-ARXIV-2605-24598:start -->Hera: Learning Long-Horizon Coordination for Device-Cloud Collaborative LLM Agents only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24598:end -->

Books Decision=`Integrate`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24598:end -->

<!-- review:SF-2026-ARXIV-2605-24614:start -->
#### Measuring the Depth of LLM Unlearning via Activation Patching

**问题与机制。** To address these limitations, we propose the Unlearning Depth Score (UDS), a metric that quantifies the mechanistic depth of unlearning via activation patching. owner=`PLATFORM-EVALUATION-SYSTEM`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§3 Unlearning Depth Score and activation patching`；Evaluation=`§4 Meta-Evaluation; §5 case studies`；Limitations/Counterevidence=`Limitations after §7 Conclusion`。

<!-- claim:SF-2026-ARXIV-2605-24614:start -->Measuring the Depth of LLM Unlearning via Activation Patching only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24614:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24614:end -->

<!-- review:SF-2026-ARXIV-2605-24619:start -->
#### Synthesizing Inductive Invariants for Distributed Protocols via IC3 and Large Language Models

**问题与机制。** We present IC3Syn, a neuro-symbolic framework that synthesizes inductive invariants by executing an IC3-style process over TLA+ states with the assistance of Large Language Models (LLMs). owner=`AGENT-PLATFORM`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§4 Design; §5 Implementation`；Evaluation=`§6 Evaluation`；Limitations/Counterevidence=`§7.2 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-24619:start -->Synthesizing Inductive Invariants for Distributed Protocols via IC3 and Large Language Models only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24619:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24619:end -->

<!-- review:SF-2026-ARXIV-2605-24657:start -->
#### Beyond Inference-Only Deployment: Comparing Weight-Based Consolidation Against Cascading Compaction

**问题与机制。** Major LLM platforms deploy models in an inference-only configuration: the model serves requests but never updates per-user weights. owner=`AGENT-CONTEXT`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§2 Method; memory taxonomy and consolidation/compaction pipelines`；Evaluation=`§3 Evaluation`；Limitations/Counterevidence=`§4 Discussion — Limitations`。

<!-- claim:SF-2026-ARXIV-2605-24657:start -->Beyond Inference-Only Deployment: Comparing Weight-Based Consolidation Against Cascading Compaction only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24657:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24657:end -->

<!-- review:SF-2026-ARXIV-2605-24659:start -->
#### IterInject: Indirect Prompt Injection Against LLM Agents via Feedback-Guided Iterative Optimization

**问题与机制。** We introduce \oursys, a feedback-guided iterative framework that closes the loop between injection, diagnosis, and refinement: a rule-based diagnoser produces structured outcome labels with behavioral descriptions, and an LLM-based optimizer refines payloads conditioned on the full optimization history. owner=`PLATFORM-SECURITY`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 Threat Model; §4 feedback-guided payload optimization`；Evaluation=`§5 Experimental Setup; §6 Evaluation`；Limitations/Counterevidence=`Limitations after §7 Conclusion; tested agents/channels only`。

<!-- claim:SF-2026-ARXIV-2605-24659:start -->IterInject: Indirect Prompt Injection Against LLM Agents via Feedback-Guided Iterative Optimization only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24659:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24659:end -->

<!-- review:SF-2026-ARXIV-2605-24660:start -->
#### How Many Tools Should an LLM Agent See? A Chance-Corrected Answer

**问题与机制。** Before an LLM agent can use a tool, a retrieval system must decide which candidate tools to show to the agent. owner=`AGENT-TOOL-CALLING`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 Bits-over-Random and MDP exposure policy`；Evaluation=`§4 Empirical Evaluation`；Limitations/Counterevidence=`§5.3 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-24660:start -->How Many Tools Should an LLM Agent See? A Chance-Corrected Answer only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24660:end -->

Books Decision=`Integrate`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24660:end -->

<!-- review:SF-2026-ARXIV-2605-24661:start -->
#### Measuring Reasoning Quality in LLMs: A Multi-Dimensional Behavioral Framework

**问题与机制。** Despite remarkable progress on reasoning benchmarks, current LLM evaluation practice remains anchored to final-answer correctness, providing limited insight into how models reason, how reliably they behave under contextual variation, or how efficiently they reach conclusions. owner=`PLATFORM-EVALUATION-SYSTEM`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§4 multi-dimensional behavioral framework and aggregation`；Evaluation=`§5 Results`；Limitations/Counterevidence=`§6.2 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-24661:start -->Measuring Reasoning Quality in LLMs: A Multi-Dimensional Behavioral Framework only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24661:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24661:end -->

<!-- review:SF-2026-ARXIV-2605-24662:start -->
#### OpenTwin: Closed-Loop Digital Twins for Trustworthy Policy Deployment in Open RAN

**问题与机制。** To fill this gap, we present OpenTwin, a closed-loop framework that learns the simulator configuration reproducing an operating deployment streamed measurements, certifies the resulting DT by re-simulation, calibrates it online, and evaluates each xApp action before it executes on the physical network. owner=`PLATFORM-EVALUATION-SYSTEM`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§II–§IV OpenTwin closed-loop data assimilation, calibration and policy-validation workflow`；Evaluation=`§A Experimental Setup; §B Experimental Results`；Limitations/Counterevidence=`§V Limitations; real-network drift and Open-RAN testbed boundary`。

<!-- claim:SF-2026-ARXIV-2605-24662:start -->OpenTwin: Closed-Loop Digital Twins for Trustworthy Policy Deployment in Open RAN only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24662:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24662:end -->

<!-- review:SF-2026-ARXIV-2605-24667:start -->
#### When Mean CE Fails: Median CE Can Better Track Language Model Quality

**问题与机制。** Mean cross-entropy is the standard validation metric for language models, but it can fail to track model quality during training. owner=`TRAIN-PRETRAINING`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§§3–4 mean/median CE interventions and top-K self-distillation`；Evaluation=`§3.2; §§4.2–4.4; Appendix C protocol`；Limitations/Counterevidence=`§5 Discussion — Limitations`。

<!-- claim:SF-2026-ARXIV-2605-24667:start -->When Mean CE Fails: Median CE Can Better Track Language Model Quality only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24667:end -->

Books Decision=`Integrate`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24667:end -->

<!-- review:SF-2026-ARXIV-2605-24683:start -->
#### B.O.D.Y.: Beyond-Overlay Deterministic topologY -- A Layer-2 Declarative Ground Truth for AIOps Pipelines under Fragmented Administrative Boundaries

**问题与机制。** Modern AIOps environments operating within multi-campus institutional infrastructures suffer acutely from topological drift and black-box unmanaged physical network segments. owner=`PLATFORM-MONITORING`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§III deterministic L2 topology, identity loop and HIL protocol`；Evaluation=`§IV Implementation and Results`；Limitations/Counterevidence=`§V Limitations and Constraints`。

<!-- claim:SF-2026-ARXIV-2605-24683:start -->B.O.D.Y.: Beyond-Overlay Deterministic topologY -- A Layer-2 Declarative Ground Truth for AIOps Pipelines under Fragmented Administrative Boundaries only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24683:end -->

Books Decision=`Integrate`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24683:end -->

<!-- review:SF-2026-ARXIV-2605-24697:start -->
#### The Path Matters: Learning a Token-Commitment Policy for Diffusion Language Models

**问题与机制。** We introduce TraceLock, a lightweight plug-in controller that instantiates this policy for a frozen diffusion language model. owner=`MULTIMODAL-GENERATIVE-PARADIGMS`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§3 future-stability labels, learned commitment and TraceLock deployment`；Evaluation=`§4 Experiments; §§4.2–4.4`；Limitations/Counterevidence=`§5 Conclusion; frozen generator/tested diffusion backbones boundary`。

<!-- claim:SF-2026-ARXIV-2605-24697:start -->The Path Matters: Learning a Token-Commitment Policy for Diffusion Language Models only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24697:end -->

Books Decision=`Integrate`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24697:end -->

<!-- review:SF-2026-ARXIV-2605-24709:start -->
#### Streaming Reinforcement Learning under Partial Observability with Real-Time Recurrent Learning

**问题与机制。** We close this gap using recurrent trace units, a diagonal recurrent architecture that enables exact RTRL with linear time and memory complexity in the parameter count, and show that they integrate cleanly into existing streaming algorithms across both discrete and continuous control. owner=`TRAIN-RLHF`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§3 Methodology; streaming partially-observed recurrent policy with exact RTRL`；Evaluation=`§4 Experiments`；Limitations/Counterevidence=`§6 Discussion and Limitations`。

<!-- claim:SF-2026-ARXIV-2605-24709:start -->Streaming Reinforcement Learning under Partial Observability with Real-Time Recurrent Learning only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24709:end -->

Books Decision=`Integrate`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24709:end -->

<!-- review:SF-2026-ARXIV-2605-24727:start -->
#### Fundamental Limitation in Explaining AI

**问题与机制。** In this paper, we mathematically prove a fundamental quadrilemma in explaining AI, stating that AI and its explanation cannot satisfy the following four conditions simultaneously: 1) the complexity of the operation environment, 2) the goodness of the AI's performance, 3) the interpretability of the AI's explanation, and 4) the complete faithfulness of the AI's explanation. owner=`PLATFORM-EVALUATION-SYSTEM`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§3 four explanation conditions; §4 quadrilemma theorem/implications`；Evaluation=`formal construction and implications in §4`；Limitations/Counterevidence=`§5 Conclusion, limitations and future work`。

<!-- claim:SF-2026-ARXIV-2605-24727:start -->Fundamental Limitation in Explaining AI only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24727:end -->

Books Decision=`Integrate`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24727:end -->

<!-- review:SF-2026-ARXIV-2605-24728:start -->
#### Hylos: Operability Contracts for Model-Native Spatial Intelligence

**问题与机制。** A generated object or environment becomes useful to an agent only when the system can identify its entities, frames, surfaces, constraints, provenance, admissible actions, expected effects, and validation failures. owner=`MULTIMODAL-EMBODIED-VLA`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§4 operability state/graph, spatial transactions and effect diffs; §5 agency gates`；Evaluation=`§6 repair stress test; §7 qualitative result`；Limitations/Counterevidence=`§1.2 Scope of Claims; prototype/trajectory does not establish general runtime validity`。

<!-- claim:SF-2026-ARXIV-2605-24728:start -->Hylos: Operability Contracts for Model-Native Spatial Intelligence only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24728:end -->

Books Decision=`Structural Candidate`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24728:end -->

<!-- review:SF-2026-ARXIV-2605-24733:start -->
#### StepGap: A Hybrid NLI-LLM Checker for Step-Level Evidence-Gap Detectionin Multi-Hop Question Answering

**问题与机制。** We present \textbf{StepGap}, a hybrid NLI-LLM decision tree that detects step-level evidence gaps in multi-hop QA and emits one of three typed labels: \textsc{Contradicted Claim} (CC), \textsc{Irrelevant Evidence} (IE), or \textsc{Missing Bridge} (MB), each tied to a concrete repair action. owner=`AGENT-REFLECTION`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 formulation; §4 hybrid checker; §5 typed process reward`；Evaluation=`§6 checker evaluation; §7 GRPO training`；Limitations/Counterevidence=`Limitations after §8 Conclusion`。

<!-- claim:SF-2026-ARXIV-2605-24733:start -->StepGap: A Hybrid NLI-LLM Checker for Step-Level Evidence-Gap Detectionin Multi-Hop Question Answering only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24733:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24733:end -->

<!-- review:SF-2026-ARXIV-2605-24737:start -->
#### Who judges the judges? Governance from metrics: a runtime framework for continuous LLM compliance monitoring

**问题与机制。** Current approaches to AI compliance treat conformity as a binary, audit-time verdict rather than a continuous, measurable property of production systems. owner=`PLATFORM-MONITORING`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 governance from metrics; §4 govllm architecture; §5 contributions`；Evaluation=`§6 Preliminary experiments`；Limitations/Counterevidence=`§6.3 and §7.4 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-24737:start -->Who judges the judges? Governance from metrics: a runtime framework for continuous LLM compliance monitoring only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24737:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24737:end -->

<!-- review:SF-2026-ARXIV-2605-24743:start -->
#### Bilevel Optimization of Synthetic Trajectories for Multi-Turn LLM Fine-Tuning

**问题与机制。** We propose BOOST, a bilevel optimization framework where the inner level trains the LLM on reweighted data and the outer level trains a lightweight reweighting head on held-out real validation tasks, assigning continuous trajectory-level weights without requiring an external judge. owner=`TRAIN-DATA`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§3 bilevel synthetic-trajectory weighting; §4 theory`；Evaluation=`§§5–6 experiments and learned-weight analysis`；Limitations/Counterevidence=`§7 Conclusion; three tasks and synthetic-generator boundary`。

<!-- claim:SF-2026-ARXIV-2605-24743:start -->Bilevel Optimization of Synthetic Trajectories for Multi-Turn LLM Fine-Tuning only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24743:end -->

Books Decision=`Integrate`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24743:end -->

<!-- review:SF-2026-ARXIV-2605-24749:start -->
#### How Neural Reward Models Learn Features for Policy Optimization: A Single-Index Analysis

**问题与机制。** We study this feedback in a Gaussian single-index model with $r^*(x) = σ^*(\langle θ^*, x\rangle)$ and $x \sim N(0, I_d)$. owner=`TRAIN-RLHF`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§§3–5 reward-weighted feature recovery and tilted-policy value gap`；Evaluation=`theory and deployment-temperature analysis in §§4–5`；Limitations/Counterevidence=`§6 Conclusion and Discussion; single-index/theoretical-assumption boundary`。

<!-- claim:SF-2026-ARXIV-2605-24749:start -->How Neural Reward Models Learn Features for Policy Optimization: A Single-Index Analysis only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24749:end -->

Books Decision=`Integrate`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24749:end -->

<!-- review:SF-2026-ARXIV-2605-24756:start -->
#### Proper Scoring Rules for Agentic Uncertainty Quantification

**问题与机制。** Building on prequential proper scoring, we introduce the Trajectory Proper Score (TPS), a predictor-agnostic family of strictly proper trajectory-level scoring rules for any per-step uncertainty signal calibrated into a probability of eventual success. owner=`PLATFORM-EVALUATION-SYSTEM`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§4 proper trajectory scores under complete and censored observation`；Evaluation=`§5 metrics; §6 Experiments`；Limitations/Counterevidence=`§7 Conclusion and Limitations`。

<!-- claim:SF-2026-ARXIV-2605-24756:start -->Proper Scoring Rules for Agentic Uncertainty Quantification only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24756:end -->

Books Decision=`Integrate`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24756:end -->

<!-- review:SF-2026-ARXIV-2605-24770:start -->
#### Muon in Vision Transformers: Optimizer-Recipe Interactions and Gradient Spectra

**问题与机制。** We study Muon for ViT training, largely on ImageNet-100 and Pl@ntNet-300K, comparing against AdamW under standard vision recipes involving mixup, cutmix, smoothing, and random augmentation and erasing. owner=`TRAIN-PRETRAINING`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§§2–5 Muon geometry and recipe interaction`；Evaluation=`§§3–6; Appendices C–E`；Limitations/Counterevidence=`§7 Conclusions and limitations`。

<!-- claim:SF-2026-ARXIV-2605-24770:start -->Muon in Vision Transformers: Optimizer-Recipe Interactions and Gradient Spectra only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24770:end -->

Books Decision=`Integrate`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24770:end -->

<!-- review:SF-2026-ARXIV-2605-24775:start -->
#### PRIMA: Operational Patterns for Resilient Multi-Agent Research with Verifiable Identity and Convergent Feedback

**问题与机制。** We present PRIMA, whose primary contributions are three operational patterns for surviving these failure modes: (1) a resilience-and-recovery layer that detects upstream rate-limit signals, persists a typed pause record to disk, and resumes long-running runs without re-executing converged work even across process restarts; (2) a sub-agent operating discipline encoding task-fidelity, tool-use, revision, and inter-step context-boundary norms as a structural prompt layer; (3) a multi-phase application pattern for structured engineering deliverables pairing orthogonal draft steps with an explicit cross-document harmonization pass before final synthesis. owner=`AGENT-MULTI-AGENT`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§III identity; §§IV–VIII protocol, scoring, orchestration and persistence`；Evaluation=`reported operational examples and convergence traces in §§VI–VIII`；Limitations/Counterevidence=`§I/§II claim scope; pattern/prototype rather than general production proof`。

<!-- claim:SF-2026-ARXIV-2605-24775:start -->PRIMA: Operational Patterns for Resilient Multi-Agent Research with Verifiable Identity and Convergent Feedback only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24775:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24775:end -->

<!-- review:SF-2026-ARXIV-2605-24785:start -->
#### PANDO: Efficient Multimodal AI Agents via Online Skill Distillation

**问题与机制。** We first analyze trajectories from VisualWebArena and identify three recurring sources of inefficiency: repeat-action loops, hidden discovery costs, and low prompt-cache reuse. owner=`AGENT-PLATFORM`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 cost decomposition and online skill-distillation lifecycle`；Evaluation=`§5 Experimental Setup and reported results`；Limitations/Counterevidence=`§7 Limitations and Conclusion`。

<!-- claim:SF-2026-ARXIV-2605-24785:start -->PANDO: Efficient Multimodal AI Agents via Online Skill Distillation only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24785:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24785:end -->

<!-- review:SF-2026-ARXIV-2605-24786:start -->
#### CONF-KV: Confidence-Aware KV Cache Eviction with Mixed-Precision Storage for Long-Horizon LLM

**问题与机制。** We introduce CONF-KV, a KV-cache manager that converts the next-token distribution into a scalar confidence score and uses it to choose the per-step cache budget, retaining more context when the model is uncertain and pruning aggressively when it is confident. owner=`INFER-KV-CACHE`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 confidence-aware mixed-precision cache manager`；Evaluation=`§§4–6 setup, results and ablations`；Limitations/Counterevidence=`§7 failure modes; §8 Limitations and conclusion`。

<!-- claim:SF-2026-ARXIV-2605-24786:start -->CONF-KV: Confidence-Aware KV Cache Eviction with Mixed-Precision Storage for Long-Horizon LLM only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24786:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24786:end -->

<!-- review:SF-2026-ARXIV-2605-24793:start -->
#### Beyond the Target: From Imitation to Collaboration in Speculative Decoding

**问题与机制。** Speculative decoding (SPD) accelerates large language model (LLM) inference by letting a smaller draft model propose multiple future tokens that are verified in parallel by a larger target model. owner=`INFER-SPECULATIVE-DECODING`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 utility view, collaborative arbitration and RL training`；Evaluation=`§4 Experiments; §§4.2–4.4`；Limitations/Counterevidence=`§5 Conclusion and Appendix A tested-model/benchmark boundary`。

<!-- claim:SF-2026-ARXIV-2605-24793:start -->Beyond the Target: From Imitation to Collaboration in Speculative Decoding only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24793:end -->

Books Decision=`Integrate`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24793:end -->

<!-- review:SF-2026-ARXIV-2605-24817:start -->
#### RouteScan: A Non-Intrusive Approach to Auditing MoE LLMs Safety via Expert Routing Telemetry

**问题与机制。** Inspired by this observation, we propose RouteScan, a non-intrusive auditing framework for detecting harmful behaviors through such routing-induced GPU telemetry. 系统 owner=`PLATFORM-MONITORING`。

**Exact-v1 路径。** Method=`§5 Method: request-level telemetry, hybrid scoring and calibrated detector`；Evaluation=`§6 Evaluation, including §6.3–§6.5 transfer and privacy-boundary tests`；Limitations/Counterevidence=`§8 Discussion; §10 Ethical Concern; no dedicated Limitations section`。

<!-- claim:SF-2026-ARXIV-2605-24817:start -->RouteScan: A Non-Intrusive Approach to Auditing MoE LLMs Safety via Expert Routing Telemetry 的 exact-v1 只支持该文披露机制：Inspired by this observation, we propose RouteScan, a non-intrusive auditing framework for detecting harmful behaviors through such routing-induced GPU telemetry. 其未证明边界由 `§8 Discussion; §10 Ethical Concern; no dedicated Limitations section` 限定；不能把该受限结果外推为跨模型、跨硬件、跨 workload 或生产 SLO 的通用优势。<!-- claim:SF-2026-ARXIV-2605-24817:end -->

Books Decision=`Integrate`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-24817:end -->

<!-- review:SF-2026-ARXIV-2605-24818:start -->
#### Spiking the training data to correct for test set contamination

**问题与机制。** 在已知比例主动注入 benchmark 样本并拟合 contamination-response curve，把污染校正从事后猜测变成带干预记录的 evaluation protocol。 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1 路径。** Method=`§3 Simulating contamination; §3.1 Estimators and predictors; §3.2 Data generation`；Evaluation=`§4 Benchmarking predictors; §5 Practical considerations; Appendix B Experimental details`；Limitations/Counterevidence=`§5 Practical considerations; §6 Discussion: controlled Hubble-8B/test-set setting, training-data access and counterfactual-model assumptions`。

<!-- claim:SF-2026-ARXIV-2605-24818:start -->只证明论文披露的 Hubble-8B、五类 benchmark 与模拟污染设置；需要训练数据写权限和未污染 counterfactual 假设，不能外推成任意闭源模型的通用校正器。<!-- claim:SF-2026-ARXIV-2605-24818:end -->

Books Decision=`Integrate`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-24818:end -->

<!-- review:SF-2026-ARXIV-2605-24823:start -->
#### Agent Manufacturing: Foundation-Model Agents as First-Class Industrial Entities

**问题与机制。** Manufacturing has passed through four widely recognized paradigms - mechanization, electrification, programmable automation, and Smart Manufacturing - each defined by the kind of work it shifted from humans to machines. 系统 owner=`AGENT-PLATFORM`。

**Exact-v1 路径。** Method=`§3 Definition and Decomposition of Industrial Cognition; §4 thin versus thick autonomy`；Evaluation=`§5 The Factory as a Cognitive Ecosystem: A Worked Example`；Limitations/Counterevidence=`§8 Research Agenda; §9 Conclusion; position paper and near-future composite, not deployed-system validation`。

<!-- claim:SF-2026-ARXIV-2605-24823:start -->Agent Manufacturing: Foundation-Model Agents as First-Class Industrial Entities 的 exact-v1 只支持该文披露机制：Manufacturing has passed through four widely recognized paradigms - mechanization, electrification, programmable automation, and Smart Manufacturing - each defined by the kind of work it shifted from humans to machines. 其未证明边界由 `§8 Research Agenda; §9 Conclusion; position paper and near-future composite, not deployed-system validation` 限定；不能把该受限结果外推为跨模型、跨硬件、跨 workload 或生产 SLO 的通用优势。<!-- claim:SF-2026-ARXIV-2605-24823:end -->

Books Decision=`No Change — Existing Coverage`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-24823:end -->

<!-- review:SF-2026-ARXIV-2605-24832:start -->
#### Optimus: Elastic Decoding for Efficient Diffusion LLM Serving

**问题与机制。** We present Optimus, a serving system that enables elastic decoding for diffusion LLMs by dynamically adapting decoding granularity to runtime load. 系统 owner=`INFER-TENSORRT-LLM`。

**Exact-v1 路径。** Method=`§4 Streaming Chunked Decoding; §5 Saturation-aware Elastic Scheduling`；Evaluation=`§7 Evaluation, especially §7.3–§7.7 throughput, serving and ablation results`；Limitations/Counterevidence=`§9 Conclusion; no dedicated Limitations section; evidence is bounded to evaluated DLLMs, A100 and disclosed loads`。

<!-- claim:SF-2026-ARXIV-2605-24832:start -->Optimus: Elastic Decoding for Efficient Diffusion LLM Serving 的 exact-v1 只支持该文披露机制：We present Optimus, a serving system that enables elastic decoding for diffusion LLMs by dynamically adapting decoding granularity to runtime load. 其未证明边界由 `§9 Conclusion; no dedicated Limitations section; evidence is bounded to evaluated DLLMs, A100 and disclosed loads` 限定；不能把该受限结果外推为跨模型、跨硬件、跨 workload 或生产 SLO 的通用优势。<!-- claim:SF-2026-ARXIV-2605-24832:end -->

Books Decision=`Integrate`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-24832:end -->

<!-- review:SF-2026-ARXIV-2605-24870:start -->
#### Trajectory-Consistent Calibration for Cache-Accelerated Diffusion Models

**问题与机制。** 把 diffusion cache 的误差从单点 representation mismatch 扩展为会被先前校准继续改写的 trajectory state，并沿 corrected history 逐步拟合 site-local calibration prior。 系统 owner=`MULTIMODAL-GENERATIVE-PARADIGMS`。

**Exact-v1 路径。** Method=`§2 Problem Formulation; §3.1 Local Statistical Calibration; §3.2 Trajectory-Consistent Prior Estimation`；Evaluation=`§4.1–§4.3 PixArt-alpha/DiT-XL/2 experiments and ablations; Appendix B.1–B.8 latency, prompt-count and compute details`；Limitations/Counterevidence=`Appendix C Limitations and Broader Impact; offline priors, selected sites/windows, representative-prompt and tested-model boundary`。

<!-- claim:SF-2026-ARXIV-2605-24870:start -->只验证 PixArt-alpha、DiT-XL/2、FORA/ToCa/L2C 与披露的离线 prior、采样步数和 H800 路径；prior 漂移、未测 cache policy、在线并发与分布外 prompt 不受该结果保证，失配时应回退 base cache 或 full computation。<!-- claim:SF-2026-ARXIV-2605-24870:end -->

Books Decision=`Integrate`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-24870:end -->

<!-- review:SF-2026-ARXIV-2605-24879:start -->
#### Efficient DP-SGD for LLMs with Randomized Clipping

**问题与机制。** 用 Hutchinson/Hutch++ 随机 trace estimation 近似 per-sample gradient norm，把 DP clipping 的显存复杂度从显式 T×T 或 d×d 中间量改为受投影维度控制的 estimator，并为随机 clipping 单独建立 privacy accountant。 系统 owner=`PLATFORM-SECURITY`。

**Exact-v1 路径。** Method=`§4 Proposed Method; §5 Privacy Analysis and Accounting; Appendix B.9 randomized-clipping accountant`；Evaluation=`§6 Experiments; §6.1 Memory, Compute and Latency Gains; Appendix D hyperparameters`；Limitations/Counterevidence=`§7 Conclusion and experiment scope: Llama-3.2-1B, sequence length 4096, selected full/LoRA fine-tuning tasks and randomized norm-estimation assumptions`。

<!-- claim:SF-2026-ARXIV-2605-24879:start -->形式保证依赖论文的随机 clipping mechanism 与 accountant 被原样实现；实验只覆盖 Llama-3.2-1B、固定 4096 长度和三类任务，未证明大模型、分布式 microbatch、任意 epsilon 或任意投影维度下同时保持 utility 与成本优势。<!-- claim:SF-2026-ARXIV-2605-24879:end -->

Books Decision=`Integrate`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-24879:end -->

<!-- review:SF-2026-ARXIV-2605-24883:start -->
#### Inverting the Shield: Systematically Generating Safety Tests from Policy Specifications

**问题与机制。** 把自然语言 safety policy 编译为形式化谓词和语义图，再从未覆盖路径生成可追踪测试，使 policy revision、test identity 与 coverage evidence 成为同一评估对象。 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1 路径。** Method=`§3 Methodology: policy-to-FOL translation, semantic policy graph and graph-guided query instantiation`；Evaluation=`§4 Evaluation: policy coverage and attack efficacy`；Limitations/Counterevidence=`§ Limitations: policy-quality dependency, static single-turn scope, no multi-turn or agent-state coverage`。

<!-- claim:SF-2026-ARXIV-2605-24883:start -->垃圾输入 policy 会直接产生错误测试；exact-v1 只覆盖静态单轮交互，未证明多轮 Agent state、生产 policy 漂移或自动生成测试的完备性。<!-- claim:SF-2026-ARXIV-2605-24883:end -->

Books Decision=`Integrate`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-24883:end -->

<!-- review:SF-2026-ARXIV-2605-24892:start -->
#### X-Foresight: A Joint Vision-Action Causal Forecasting Network via Predictive World Modeling

**问题与机制。** 把低熵相邻帧预测改成跨语义时间块的自回归 future-state 预测：块内保留稠密瞬时动态、块间保留稀疏长程因果，并把 action/latent prediction 与多视角 renderer 分责。 系统 owner=`MULTIMODAL-WORLD-MODELS`。

**Exact-v1 路径。** Method=`§3.1 Large Drive Model, especially §3.1.3 chunk-wise prediction/CLEF/TIS; §3.2 Vision Renderer; §3.3 training and interleaved inference pipeline`；Evaluation=`§4.1 Large Drive Model and §4.2 Vision Renderer, including horizon/CL-CLEF-TIS ablations and production-scale comparison`；Limitations/Counterevidence=`§5 Conclusion/future directions; private driving-data distribution, learned renderer and offline/closed-loop evaluation boundary; no dedicated limitations section`。

<!-- claim:SF-2026-ARXIV-2605-24892:start -->证据绑定作者私有驾驶数据、4 Hz 七相机 rollout、learned renderer 与披露的闭环设置；视觉一致性和 planning gain 不证明真实道路安全、因果识别或跨 embodiment 泛化。Ch25 已有 transition-token/reasoner/renderer 分责和多时间尺度状态边界，故不重复写入。<!-- claim:SF-2026-ARXIV-2605-24892:end -->

Books Decision=`No Change — Existing Coverage`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-24892:end -->

<!-- review:SF-2026-ARXIV-2605-24914:start -->
#### MVR-cache: Optimizing Semantic Caching via Multi-Vector Retrieval and Learned Prompt Segmentation

**问题与机制。** To reduce LLM costs and latency, semantic caching systems must accurately identify when a new prompt matches a cached one. 系统 owner=`INFER-KV-CACHE`。

**Exact-v1 路径。** Method=`§3 MVR-cache multi-vector retrieval and prompt segmentation`；Evaluation=`§5 semantic-cache evaluation`；Limitations/Counterevidence=`§6 limitations and workload/encoder boundary`。

<!-- claim:SF-2026-ARXIV-2605-24914:start -->MVR-cache: Optimizing Semantic Caching via Multi-Vector Retrieval and Learned Prompt Segmentation 的 exact-v1 只支持该文披露机制：To reduce LLM costs and latency, semantic caching systems must accurately identify when a new prompt matches a cached one. 其未证明边界由 `§6 limitations and workload/encoder boundary` 限定；不能把该受限结果外推为跨模型、跨硬件、跨 workload 或生产 SLO 的通用优势。<!-- claim:SF-2026-ARXIV-2605-24914:end -->

Books Decision=`No Change — Existing Coverage`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-24914:end -->

<!-- review:SF-2026-ARXIV-2605-24922:start -->
#### MuJoCoUni:Persistent Batched Runtime Primitives for MuJoCo

**问题与机制。** 把 stateless rollout 调用提升为 executor-owned persistent environment pool，使 per-environment model/data、reset、step 与 Jacobian state 在 batched robot-learning loop 中保持可寻址。 系统 owner=`MULTIMODAL-EMBODIED-VLA`。

**Exact-v1 路径。** Method=`§3 System Design and API; §3.1 Design boundary; §3.2 Persistent pool ownership; §3.3 Runtime primitives; §3.4 Reset-time randomization`；Evaluation=`§4 Validation and Benchmarks: parity, rollout throughput, reset and Jacobian measurements`；Limitations/Counterevidence=`§6 Discussion; §6.1 Runtime boundary and trade-offs; §6.3 Reproducibility`。

<!-- claim:SF-2026-ARXIV-2605-24922:start -->证据绑定 MuJoCo 与论文测试硬件/任务；persistent pool 增加生命周期、隔离和复现责任，未证明真实机器人、分布式故障或硬实时控制语义。<!-- claim:SF-2026-ARXIV-2605-24922:end -->

Books Decision=`Integrate`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-24922:end -->

<!-- review:SF-2026-ARXIV-2605-24930:start -->
#### H$^{2}$MT: Semantic Hierarchy-Aware Hierarchical Memory Transformer

**问题与机制。** 先把长文档组织成语义树，再用层级 memory tokens 与 query-aware routing 在粗摘要和细粒度节点间分配注意力预算。 系统 owner=`MODEL-LONG-CONTEXT`。

**Exact-v1 路径。** Method=`§3 Methodology; §3.1 Semantic tree construction; §3.2 Memory-token construction; §3.3 Hierarchical inference; §3.4 Objectives`；Evaluation=`§4 Experiments: LongBench/structured-document quality, TTFT and memory`；Limitations/Counterevidence=`§5 Conclusion and discussion: hierarchy dependency, heuristic-tree error propagation, rare-evidence attenuation and routing-prune risk`。

<!-- claim:SF-2026-ARXIV-2605-24930:start -->收益依赖可恢复的文档层级；错误树和过度压缩会丢失稀有证据。当前 Ch22 已拥有 query-aware hierarchical selection、coarse summary 与 dense fallback，因此不重复写入。<!-- claim:SF-2026-ARXIV-2605-24930:end -->

Books Decision=`No Change — Existing Coverage`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-24930:end -->

<!-- review:SF-2026-ARXIV-2605-24941:start -->
#### Memory-Induced Tool-Drift in LLM Agents

**问题与机制。** We study a previously unexamined failure of this combination: when personality-driven biases stored in memory (cost-consciousness, impatience, risk tolerance, etc.) silently affect tool calls in contexts where they are not applicable. 系统 owner=`AGENT-TOOL-CALLING`。

**Exact-v1 路径。** Method=`PDF §3 memory-induced tool-drift mechanism`；Evaluation=`PDF §4 agent/tool evaluation`；Limitations/Counterevidence=`PDF §5 limitations and memory/task boundary`。

<!-- claim:SF-2026-ARXIV-2605-24941:start -->Memory-Induced Tool-Drift in LLM Agents 的 exact-v1 只支持该文披露机制：We study a previously unexamined failure of this combination: when personality-driven biases stored in memory (cost-consciousness, impatience, risk tolerance, etc.) silently affect tool calls in contexts where they are not applicable. 其未证明边界由 `PDF §5 limitations and memory/task boundary` 限定；不能把该受限结果外推为跨模型、跨硬件、跨 workload 或生产 SLO 的通用优势。<!-- claim:SF-2026-ARXIV-2605-24941:end -->

Books Decision=`No Change — Existing Coverage`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-24941:end -->

<!-- review:SF-2026-ARXIV-2605-24973:start -->
#### MinerU-Popo: Universal Post-Processing Model for Structured Document Parsing

**问题与机制。** 在 page OCR 之后增加 document-level state owner，跨页合并段落/表格并同步 chunk 与结构索引，使 ingestion 输出可被 RAG 以同一 document revision 消费。 系统 owner=`AGENT-RAG`。

**Exact-v1 路径。** Method=`§3 Problem formulation; §4.1 Task-oriented data engine; §4.2 Dynamic chunking and synchronization; §4.3 Document enrichment`；Evaluation=`§5 Experiments: five OCR backends and downstream RAG/QA`；Limitations/Counterevidence=`§5 evaluation scope and §6 conclusion: OCR/model/workload boundary; cross-page summaries can suppress fine-grained evidence`。

<!-- claim:SF-2026-ARXIV-2605-24973:start -->作者结果绑定披露的 OCR/VLM、H200 与文档集合；跨页修复可能合并错误或隐藏细粒度 locator，不能替代原页、region provenance 与独立 evidence check。<!-- claim:SF-2026-ARXIV-2605-24973:end -->

Books Decision=`Integrate`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-24973:end -->

<!-- review:SF-2026-ARXIV-2605-25002:start -->
#### MemMark: State-Evolution Attribution Watermarking for Agent Long-Term Memory Systems

**问题与机制。** We propose MemMark, a state-evolution attribution watermark that embeds an owner-controlled signal into latent memory-write decisions. 系统 owner=`AGENT-MEMORY`。

**Exact-v1 路径。** Method=`§3 Problem Formulation; §4 MemMark, including distribution-preserving watermark and cryptographic audit trace`；Evaluation=`§5 Experiments, RQ1–RQ5`；Limitations/Counterevidence=`§7 Limitations; Appendix G memory-lifecycle attacks and backend diagnostics`。

<!-- claim:SF-2026-ARXIV-2605-25002:start -->MemMark: State-Evolution Attribution Watermarking for Agent Long-Term Memory Systems 的 exact-v1 只支持该文披露机制：We propose MemMark, a state-evolution attribution watermark that embeds an owner-controlled signal into latent memory-write decisions. 其未证明边界由 `§7 Limitations; Appendix G memory-lifecycle attacks and backend diagnostics` 限定；不能把该受限结果外推为跨模型、跨硬件、跨 workload 或生产 SLO 的通用优势。<!-- claim:SF-2026-ARXIV-2605-25002:end -->

Books Decision=`Integrate`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-25002:end -->

<!-- review:SF-2026-ARXIV-2605-25052:start -->
#### Faithfulness Metrics Don't Measure Faithfulness: A Meta-Evaluation with Ground Truth

**问题与机制。** Building on this methodology, we present BonaFide, a benchmark of 3,066 labeled CoTs across 13 tasks and 10 models, and use it to conduct the first systematic evaluation of prominent faithfulness metrics. 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1 路径。** Method=`§2 faithfulness definitions; §3 ground-truth elicitation; §4 BonaFide labeling pipeline`；Evaluation=`§5 Experiments and §5.2 Results`；Limitations/Counterevidence=`§5.3 Discussion — Limitations; task/model and metric-cost boundary`。

<!-- claim:SF-2026-ARXIV-2605-25052:start -->Faithfulness Metrics Don't Measure Faithfulness: A Meta-Evaluation with Ground Truth 的 exact-v1 只支持该文披露机制：Building on this methodology, we present BonaFide, a benchmark of 3,066 labeled CoTs across 13 tasks and 10 models, and use it to conduct the first systematic evaluation of prominent faithfulness metrics. 其未证明边界由 `§5.3 Discussion — Limitations; task/model and metric-cost boundary` 限定；不能把该受限结果外推为跨模型、跨硬件、跨 workload 或生产 SLO 的通用优势。<!-- claim:SF-2026-ARXIV-2605-25052:end -->

Books Decision=`No Change — Existing Coverage`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-25052:end -->

<!-- review:SF-2026-ARXIV-2605-25073:start -->
#### Security in the Fine-Tuning Lifecycle of Large Language Models: Threats, Defenses,Evaluation, and Future Directions

**问题与机制。** 把 fine-tuning attack surface 按 pre-tuning input/supply chain、during-tuning optimizer/update 与 post-tuning adapter/artifact 三个 intervention phase 组织，并用同一基座和协议检查跨 phase 防御组合。 系统 owner=`PLATFORM-SECURITY`。

**Exact-v1 路径。** Method=`§2 Evaluation Substrate and Threat Model; §3–§5 pre/during/post-tuning lifecycle taxonomy; §6 unified cross-phase evaluation`；Evaluation=`§6.2–§6.6 shared models/tasks, reproduced attacks and cross-phase defense combinations`；Limitations/Counterevidence=`§7 Discussion and §8 Future Directions; reproduced small-model/task configurations, method-compatibility substitutions and lifecycle-survey boundary`。

<!-- claim:SF-2026-ARXIV-2605-25073:start -->survey taxonomy 与复现实验只能支持披露的 Llama/Qwen 1B–4B、SST-2/AGNews/agent subsets 和选定 attack-defense pairs；不能证明未复现方法、生产 adapter registry 或 RLHF/DPO 路径已被覆盖。Ch72 已拥有 data→update→artifact→runtime 的安全与 release contract，故不重复写入。<!-- claim:SF-2026-ARXIV-2605-25073:end -->

Books Decision=`No Change — Existing Coverage`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-25073:end -->

<!-- review:SF-2026-ARXIV-2605-25077:start -->
#### WorldCraft: From Camera Navigation to Object Manipulation in Interactive Video World Models

**问题与机制。** We present WorldCraft, a framework that expands interactive video world models from camera navigation to object-level trajectory actions. 系统 owner=`MULTIMODAL-WORLD-MODELS`。

**Exact-v1 路径。** Method=`§3 Method: NWT, Spatial-Pathway LoRA and Trajectory-Anchored State Persistence`；Evaluation=`§4 Experiments, including camera/object control and state-persistence ablations`；Limitations/Counterevidence=`Appendix D Limitations; pixel-world and trajectory-action boundary`。

<!-- claim:SF-2026-ARXIV-2605-25077:start -->WorldCraft: From Camera Navigation to Object Manipulation in Interactive Video World Models 的 exact-v1 只支持该文披露机制：We present WorldCraft, a framework that expands interactive video world models from camera navigation to object-level trajectory actions. 其未证明边界由 `Appendix D Limitations; pixel-world and trajectory-action boundary` 限定；不能把该受限结果外推为跨模型、跨硬件、跨 workload 或生产 SLO 的通用优势。<!-- claim:SF-2026-ARXIV-2605-25077:end -->

Books Decision=`No Change — Existing Coverage`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-25077:end -->

<!-- review:SF-2026-ARXIV-2605-25085:start -->
#### Polynomial Context-Truncation Sensitivity in Autoregressive Language Models: Sequential Wyner-Ziv Bounds for KV Cache Compression

**问题与机制。** We study the rate-distortion limits of online KV cache compression in autoregressive language models, formulating it as sequential Wyner-Ziv source coding on the filtration induced by the model, with the next-step query as decoder side information. 系统 owner=`INFER-KV-CACHE`。

**Exact-v1 路径。** Method=`§3 formulation; §4 Main Theoretical Results on sequential Wyner–Ziv and suffix-only policies`；Evaluation=`§5 Empirical Validation; §6 Connections to Deployed Compression Schemes`；Limitations/Counterevidence=`§7 Limitations, including architecture, rate-convergence and heavy-hitter boundaries`。

<!-- claim:SF-2026-ARXIV-2605-25085:start -->Polynomial Context-Truncation Sensitivity in Autoregressive Language Models: Sequential Wyner-Ziv Bounds for KV Cache Compression 的 exact-v1 只支持该文披露机制：We study the rate-distortion limits of online KV cache compression in autoregressive language models, formulating it as sequential Wyner-Ziv source coding on the filtration induced by the model, with the next-step query as decoder side information. 其未证明边界由 `§7 Limitations, including architecture, rate-convergence and heavy-hitter boundaries` 限定；不能把该受限结果外推为跨模型、跨硬件、跨 workload 或生产 SLO 的通用优势。<!-- claim:SF-2026-ARXIV-2605-25085:end -->

Books Decision=`Integrate`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-25085:end -->

<!-- review:SF-2026-ARXIV-2605-25092:start -->
#### AgentIR: A Workload-Adaptive Cascade Retrieval Substrate for Long-Term Conversational Memory

**问题与机制。** Long-term conversational memory is a retrieval workload classical IR was not built for: the index grows during the query stream, query types shift intra-session, and the latency budget per retrieval is sub-10 ms. 系统 owner=`AGENT-MEMORY`。

**Exact-v1 路径。** Method=`§3 System Design; §4 Optimizations; §5.9 Agent Memory Benchmark cascade router`；Evaluation=`§5 Evaluation, especially §5.9 LongMemEval and LoCoMo`；Limitations/Counterevidence=`§6 Threats to validity and limitations; Appendix N Threats to Validity`。

<!-- claim:SF-2026-ARXIV-2605-25092:start -->AgentIR: A Workload-Adaptive Cascade Retrieval Substrate for Long-Term Conversational Memory 的 exact-v1 只支持该文披露机制：Long-term conversational memory is a retrieval workload classical IR was not built for: the index grows during the query stream, query types shift intra-session, and the latency budget per retrieval is sub-10 ms. 其未证明边界由 `§6 Threats to validity and limitations; Appendix N Threats to Validity` 限定；不能把该受限结果外推为跨模型、跨硬件、跨 workload 或生产 SLO 的通用优势。<!-- claim:SF-2026-ARXIV-2605-25092:end -->

Books Decision=`No Change — Existing Coverage`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-25092:end -->

<!-- review:SF-2026-ARXIV-2605-25133:start -->
#### Trust but Verify: Prover-Verifier Deliberation for Selective LLM Prediction

**问题与机制。** We introduce prover-verifier deliberation (PVD), an inference-time protocol grounded in interactive proof theory, as a mechanism for selective prediction: the protocol produces both an answer and a structured confidence verdict, allowing a system to report high-confidence answers while abstaining on uncertain cases. 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1 路径。** Method=`§3 Prover-Verifier Deliberation protocol and algorithm`；Evaluation=`§4 Experiments; §5 Results on coverage-precision operating points`；Limitations/Counterevidence=`§7 Limitations; verifier effective-region and no-formal-guarantee boundary`。

<!-- claim:SF-2026-ARXIV-2605-25133:start -->Trust but Verify: Prover-Verifier Deliberation for Selective LLM Prediction 的 exact-v1 只支持该文披露机制：We introduce prover-verifier deliberation (PVD), an inference-time protocol grounded in interactive proof theory, as a mechanism for selective prediction: the protocol produces both an answer and a structured confidence verdict, allowing a system to report high-confidence answers while abstaining on uncertain cases. 其未证明边界由 `§7 Limitations; verifier effective-region and no-formal-guarantee boundary` 限定；不能把该受限结果外推为跨模型、跨硬件、跨 workload 或生产 SLO 的通用优势。<!-- claim:SF-2026-ARXIV-2605-25133:end -->

Books Decision=`No Change — Existing Coverage`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-25133:end -->

<!-- review:SF-2026-ARXIV-2605-25160:start -->
#### SimuWoB: Simulating Real-World Mobile Apps for Fast and Faithful GUI Agent Benchmarking

**问题与机制。** 由 coding agent 合成可执行 mobile-app simulator，再独立生成 task 与 state validator，把 GUI agent benchmark 的 environment 和 outcome evidence 版本化。 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1 路径。** Method=`§3 SimuWoB; §3.1 Environment generation; §3.2 Task and validator generation`；Evaluation=`§4 Experiments: app fidelity, task feasibility and GUI-agent evaluation`；Limitations/Counterevidence=`§5 Limitations: visual-only interface, single-app tasks, no accessibility tree or cross-app workflow`。

<!-- claim:SF-2026-ARXIV-2605-25160:start -->只覆盖视觉单应用 simulator；不等于真实 backend、跨应用状态或 accessibility-tree 行为。当前 Ch66/Ch81 已明确 environment generation、task constraint、validator 与 durable marker 分责，故不重复写入。<!-- claim:SF-2026-ARXIV-2605-25160:end -->

Books Decision=`No Change — Existing Coverage`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-25160:end -->

<!-- review:SF-2026-ARXIV-2605-25188:start -->
#### DarkForest: Less Talk, Higher Accuracy for Multi-Agent LLMs

**问题与机制。** Multi-agent LLM systems improve reasoning by combining outputs from multiple agents, but interaction-heavy methods can introduce error propagation and high communication overhead. 系统 owner=`AGENT-MULTI-AGENT`。

**Exact-v1 路径。** Method=`§3 DarkForest Design: calibrated belief, controlled disclosure and guardrail`；Evaluation=`§4 Evaluation; Appendix D ablations`；Limitations/Counterevidence=`§6 Conclusion; no dedicated Limitations section; benchmark/model and coordinator boundary`。

<!-- claim:SF-2026-ARXIV-2605-25188:start -->DarkForest: Less Talk, Higher Accuracy for Multi-Agent LLMs 的 exact-v1 只支持该文披露机制：Multi-agent LLM systems improve reasoning by combining outputs from multiple agents, but interaction-heavy methods can introduce error propagation and high communication overhead. 其未证明边界由 `§6 Conclusion; no dedicated Limitations section; benchmark/model and coordinator boundary` 限定；不能把该受限结果外推为跨模型、跨硬件、跨 workload 或生产 SLO 的通用优势。<!-- claim:SF-2026-ARXIV-2605-25188:end -->

Books Decision=`No Change — Existing Coverage`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-25188:end -->

<!-- review:SF-2026-ARXIV-2605-25189:start -->
#### Directional Alignment Mitigates Reward Hacking in Reinforcement Learning for Language Models

**问题与机制。** We study this failure mode through the geometry of reinforcement learning updates in language models and argue that hacking emerges when optimization drifts away from a stable low-dimensional learning trajectory. 系统 owner=`TRAIN-RLHF`。

**Exact-v1 路径。** Method=`§3–§5 dominant update directions, directional shift and trusted-direction method`；Evaluation=`§6 Experimental Setting; §7 Results`；Limitations/Counterevidence=`Appendix A.1 Future Work; manuscript explicitly identifies itself as a preliminary study`。

<!-- claim:SF-2026-ARXIV-2605-25189:start -->Directional Alignment Mitigates Reward Hacking in Reinforcement Learning for Language Models 的 exact-v1 只支持该文披露机制：We study this failure mode through the geometry of reinforcement learning updates in language models and argue that hacking emerges when optimization drifts away from a stable low-dimensional learning trajectory. 其未证明边界由 `Appendix A.1 Future Work; manuscript explicitly identifies itself as a preliminary study` 限定；不能把该受限结果外推为跨模型、跨硬件、跨 workload 或生产 SLO 的通用优势。<!-- claim:SF-2026-ARXIV-2605-25189:end -->

Books Decision=`Integrate`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-25189:end -->

<!-- review:SF-2026-ARXIV-2605-25233:start -->
#### Meta-Agent: From Task Descriptions to Verified Multi-Agent Systems

**问题与机制。** We present Meta-Agent, a two-phase framework that automatically constructs and executes specialized multi-agent systems from natural-language task descriptions. 系统 owner=`AGENT-MULTI-AGENT`。

**Exact-v1 路径。** Method=`§3 Method, especially §3.2 verification loop and error attribution`；Evaluation=`§4 Experiments and ablation study`；Limitations/Counterevidence=`§4.5 Discussions; §5 Conclusion; no dedicated Limitations section`。

<!-- claim:SF-2026-ARXIV-2605-25233:start -->Meta-Agent: From Task Descriptions to Verified Multi-Agent Systems 的 exact-v1 只支持该文披露机制：We present Meta-Agent, a two-phase framework that automatically constructs and executes specialized multi-agent systems from natural-language task descriptions. 其未证明边界由 `§4.5 Discussions; §5 Conclusion; no dedicated Limitations section` 限定；不能把该受限结果外推为跨模型、跨硬件、跨 workload 或生产 SLO 的通用优势。<!-- claim:SF-2026-ARXIV-2605-25233:end -->

Books Decision=`No Change — Existing Coverage`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-25233:end -->

<!-- review:SF-2026-ARXIV-2605-25240:start -->
#### JudgmentBench: Comparing Rubric and Preference Evaluation for Quality Assessment

**问题与机制。** 把 rubric score 与 pairwise preference 作为不同 measurement operators，在同一受控质量阶梯上比较各自一致性与区分力，而不是默认二者可互换。 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1 路径。** Method=`§3.1 Dataset; §3.2 Constructed quality levels; §3.3 Rubric and pairwise-preference expert annotation`；Evaluation=`§4 Empirical comparison of rubric scoring and comparative judgment`；Limitations/Counterevidence=`Appendix A.1 Limitations: legal-domain scope, prompt-induced quality confounds, style cues and mixed-trade-off cases`。

<!-- claim:SF-2026-ARXIV-2605-25240:start -->证据主要来自法律文本和 prompt 构造的质量层级，质量与表达风格可能共变；不能据此规定所有 evaluator 都应采用同一判断形式。<!-- claim:SF-2026-ARXIV-2605-25240:end -->

Books Decision=`Integrate`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-25240:end -->

<!-- review:SF-2026-ARXIV-2605-25244:start -->
#### Inference Time Optimization with Confidence Dynamics

**问题与机制。** In this paper, we investigate the dynamics of confidence along reasoning trajectories and for first time reveal a surprising and unique pattern: correct answer traces tend to exhibit confidence improvement over time (positive confidence gain), while incorrect traces show attenuated or declining confidence as reasoning proceeds. 系统 owner=`INFER-SCHEDULING`。

**Exact-v1 路径。** Method=`§3 Confidence Trajectories and Confidence Dynamic Gain voting`；Evaluation=`§5 Empirical Results and §5.3–§5.4 ablations/score analysis`；Limitations/Counterevidence=`§6 Conclusion; Appendix A.2 simplified-training-model assumption; no dedicated Limitations section`。

<!-- claim:SF-2026-ARXIV-2605-25244:start -->Inference Time Optimization with Confidence Dynamics 的 exact-v1 只支持该文披露机制：In this paper, we investigate the dynamics of confidence along reasoning trajectories and for first time reveal a surprising and unique pattern: correct answer traces tend to exhibit confidence improvement over time (positive confidence gain), while incorrect traces show attenuated or declining confidence as reasoning proceeds. 其未证明边界由 `§6 Conclusion; Appendix A.2 simplified-training-model assumption; no dedicated Limitations section` 限定；不能把该受限结果外推为跨模型、跨硬件、跨 workload 或生产 SLO 的通用优势。<!-- claim:SF-2026-ARXIV-2605-25244:end -->

Books Decision=`No Change — Existing Coverage`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-25244:end -->

<!-- review:SF-2026-ARXIV-2605-25247:start -->
#### Kavier: Exploring Performance, Sustainability, and Efficiency of LLM Ecosystems under Inference through Cache-Aware Discrete-Event Simulation

**问题与机制。** To improve the design and operation of LLM ecosystems, we envision simulators and simulation-based digital twins becoming primary decision-making tools. 系统 owner=`INFER-SCHEDULING`。

**Exact-v1 路径。** Method=`§4 Design of Kavier and cache-aware simulation modules`；Evaluation=`§6 Trace-Based Experiments with Kavier`；Limitations/Counterevidence=`§6.7 Discussion; §7.2 Future Work; bachelor-thesis prototype and simulator-calibration boundary`。

<!-- claim:SF-2026-ARXIV-2605-25247:start -->Kavier: Exploring Performance, Sustainability, and Efficiency of LLM Ecosystems under Inference through Cache-Aware Discrete-Event Simulation 的 exact-v1 只支持该文披露机制：To improve the design and operation of LLM ecosystems, we envision simulators and simulation-based digital twins becoming primary decision-making tools. 其未证明边界由 `§6.7 Discussion; §7.2 Future Work; bachelor-thesis prototype and simulator-calibration boundary` 限定；不能把该受限结果外推为跨模型、跨硬件、跨 workload 或生产 SLO 的通用优势。<!-- claim:SF-2026-ARXIV-2605-25247:end -->

Books Decision=`No Change — Existing Coverage`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-25247:end -->

<!-- review:SF-2026-ARXIV-2605-25252:start -->
#### Quantifying Empirical Compute-Supervision Tradeoffs in RLVR

**问题与机制。** Reinforcement learning with verifiable rewards (RLVR) has become a standard paradigm for post-training language models, but in practice, verifiers are rarely perfect. 系统 owner=`TRAIN-RLHF`。

**Exact-v1 路径。** Method=`§3 Methodology: controlled false-positive/false-negative verifier noise and rollout scaling`；Evaluation=`§4 Results on compute-supervision tradeoffs`；Limitations/Counterevidence=`§5 Conclusion; narrow Qwen2.5/GSM8K/GRPO setting and no dedicated Limitations section`。

<!-- claim:SF-2026-ARXIV-2605-25252:start -->Quantifying Empirical Compute-Supervision Tradeoffs in RLVR 的 exact-v1 只支持该文披露机制：Reinforcement learning with verifiable rewards (RLVR) has become a standard paradigm for post-training language models, but in practice, verifiers are rarely perfect. 其未证明边界由 `§5 Conclusion; narrow Qwen2.5/GSM8K/GRPO setting and no dedicated Limitations section` 限定；不能把该受限结果外推为跨模型、跨硬件、跨 workload 或生产 SLO 的通用优势。<!-- claim:SF-2026-ARXIV-2605-25252:end -->

Books Decision=`Integrate`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-25252:end -->

<!-- review:SF-2026-ARXIV-2605-25272:start -->
#### AI Cartography: Mapping the Latent Landscape of AI Benchmark Ecosystems

**问题与机制。** 用 latent measurement model 分解 benchmark 共同因子与 task-specific variance，使 release evidence 能区分能力构念、数据生态和 leaderboard 聚合造成的相关性。 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1 路径。** Method=`§2 Variance decomposition, confirmatory factor analysis, bifactor model and mixed-effects latent regression; §3 Experiment and data`；Evaluation=`§4 Results across six benchmark ecosystems`；Limitations/Counterevidence=`§ Limitations: one snapshot/six benchmarks, observational design, noisy metadata, non-representative sample and temporal instability`。

<!-- claim:SF-2026-ARXIV-2605-25272:start -->只是一轮六 benchmark 的观察性快照；latent factor 不是能力本体，也不证明因果。模型、数据与提交策略变化后必须重新拟合而不能复用旧 factor。<!-- claim:SF-2026-ARXIV-2605-25272:end -->

Books Decision=`Integrate`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-25272:end -->

<!-- review:SF-2026-ARXIV-2605-25284:start -->
#### Knowing but Not Showing: LLMs Recognize Ambiguity but Rarely Ask Clarifying Questions

**问题与机制。** To study these abilities, we evaluate models on ambiguous, unambiguous, and disambiguated questions in three settings: standard question answering, explicit ambiguity judgment, and behavioral analysis, where a judge model classifies responses as direct answers, refusals, or clarifying questions. 系统 owner=`AGENT-PLANNING`。

**Exact-v1 路径。** Method=`§3 ambiguity-recognition and clarification protocol`；Evaluation=`§4 evaluation`；Limitations/Counterevidence=`§5 limitations and prompt/model boundary`。

<!-- claim:SF-2026-ARXIV-2605-25284:start -->Knowing but Not Showing: LLMs Recognize Ambiguity but Rarely Ask Clarifying Questions 的 exact-v1 只支持该文披露机制：To study these abilities, we evaluate models on ambiguous, unambiguous, and disambiguated questions in three settings: standard question answering, explicit ambiguity judgment, and behavioral analysis, where a judge model classifies responses as direct answers, refusals, or clarifying questions. 其未证明边界由 `§5 limitations and prompt/model boundary` 限定；不能把该受限结果外推为跨模型、跨硬件、跨 workload 或生产 SLO 的通用优势。<!-- claim:SF-2026-ARXIV-2605-25284:end -->

Books Decision=`No Change — Existing Coverage`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-25284:end -->

<!-- review:SF-2026-ARXIV-2605-25292:start -->
#### DECICE: AI-Driven Scheduling and Digital Twin Integration for the Cloud-HPC-Edge Compute Continuum

**问题与机制。** 让 scheduler 消费由 Digital Twin 维护的 node power/carbon/anomaly state，并把 heterogeneous workflow 先转成正式 dependency/resource model，再输出 Kubernetes/Slurm placement。 系统 owner=`PLATFORM-GPU-SCHEDULER`。

**Exact-v1 路径。** Method=`§II Work Package Structure and Contributions: IAIS data flow, formal workflow mapping, Kubernetes/Slurm control manager and Digital Twin state`；Evaluation=`§III Evaluation Results: 10–5000 job/node scalability and solver/heuristic workflow comparison`；Limitations/Counterevidence=`§IV Conclusion and project-report scope; component-level evaluation, heterogeneous project artifacts and no controlled end-to-end production SLO comparison`。

<!-- claim:SF-2026-ARXIV-2605-25292:start -->论文是 DECICE 项目架构与组件结果汇总；5000×5000 scalability、solver runtime 和 production-like use cases 不是同一 end-to-end SLO 实验，也未证明 RNN/RL 优于所有启发式。Ch63–65 已覆盖 state-aware placement、carbon/energy signal、workflow dependency 与 Slurm/Kubernetes 边界，故不重复写入。<!-- claim:SF-2026-ARXIV-2605-25292:end -->

Books Decision=`No Change — Existing Coverage`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-25292:end -->

<!-- review:SF-2026-ARXIV-2605-25298:start -->
#### Beyond Thread States: Diagnosing Performance Degradation with eBPF and Thread Dynamics

**问题与机制。** 从 thread-state 时间占比继续下钻到带 backing-resource identity 的 futex/pipe/socket/VFS/block-I/O dependency graph，并从 request entry thread 反向追踪 contention propagation。 系统 owner=`PLATFORM-MONITORING`。

**Exact-v1 路径。** Method=`§III Design; §IV-A eBPF metric collection; §IV-C Selective Thread Tracking and Algorithm 1`；Evaluation=`§V–§VI six data-intensive applications and CPU/disk/lock/external-service contention; Artifact Description/Evaluation`；Limitations/Counterevidence=`§IV-C optimistic entry-point propagation assumption; §V single x86/Linux 6.8.12 host and six-application workload boundary`。

<!-- claim:SF-2026-ARXIV-2605-25298:start -->选择性算法假设 degradation 能传播到可识别 entry thread；证据绑定单机 x86/Linux 6.8.12、六类应用与人工注入 contention，不能证明跨 kernel、GPU collective、容器隔离或无 socket entry 的训练作业同样可诊断。<!-- claim:SF-2026-ARXIV-2605-25298:end -->

Books Decision=`Integrate`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-25298:end -->

<!-- review:SF-2026-ARXIV-2605-25310:start -->
#### Tool-Call Dependency Structure is Linearly Decodable in LLM Agent Residual Streams

<!-- claim:SF-2026-ARXIV-2605-25310:start -->
- **Problem:** Tool-using LLM agents produce trajectories whose calls form a directed dependency graph: earlier tool outputs supply arguments to later calls.
- **Old path / changed constraint:** However, the structural-probe literature has not engaged with a setting now central to deployed LLM systems: tool-using agents that interleave model generation with external function calls ( Schick et al., 2023 ; Yao et al., 2023 ; Yao et al., 2024 ) .
- **Mechanism / ownership:** 研究从 agent 每次 assistant decode boundary 的 residual stream 读取表示，用低容量 edge probe 预测先前 tool output 是否为后续 tool call 提供参数，从而重建调用依赖 DAG 及其 transitive closure；random-label control、positional baseline、value/structure perturbation 与跨层 patching 用于区分记忆、位置和拓扑信号。
- **Evaluation contract:** 主实验在 Qwen3-32B 与 τ-bench retail 上记录 65 个表示层，并在 TaskBench、BFCL、ComplexFuncBench、ToolHop 检查跨域调制；部分 activation-patching 表示传播结果在 Llama-3.3-70B 复现。interactive multi-hop 中 residual 带来非位置贡献，而 single-shot 或位置已足够时该贡献衰减。
- **Proof / non-proof:** Evidence is author-reported exact-v1 mechanism/evaluation evidence. It does not establish cross-model, cross-hardware, cross-workload or production generality unless those conditions are explicitly named above.
- **Trade-off / failure mode:** 线性可解码证明 residual 中存在相关结构，不证明 agent 使用该结构控制动作；patching 改变后续 probe readout，却没有改变实际 tool call。高幅 value perturbation、跨域行为充分干预和长时序控制仍未验证，且部分 benchmark 的位置 baseline 已很强；因此不能把 probe AUROC 当成可靠规划或因果控制能力。
- **Coexistence boundary:** The older path remains appropriate where its workload and SLO do not trigger the changed constraint; the paper is treated as a conditional branch, not a universal replacement.
- **Primary:** [arXiv:2605.25310v1](https://arxiv.org/abs/2605.25310v1)；frozen exact-v1 `papers/2026/05/_sources/arxiv-owner-replay-20260903/exact-v1/2605.25310v1.html.html`。
- **Disposition:** `Weekly Only — Context`；Residual-stream decodability is a bounded model probe: it does not transfer dependency truth or execution authority from the runtime to the model.
<!-- claim:SF-2026-ARXIV-2605-25310:end -->
<!-- review:SF-2026-ARXIV-2605-25310:end -->

<!-- review:SF-2026-ARXIV-2605-25313:start -->
#### UWM-JEPA: Predictive World Models That Imagine in Belief Space

**问题与机制。** We introduce the Unitary World Model JEPA (UWM-JEPA), a JEPA world model with a density-matrix latent on a joint system-environment space and a learned unitary predictor. 系统 owner=`MULTIMODAL-WORLD-MODELS`。

**Exact-v1 路径。** Method=`§3 UWM-JEPA belief-space dynamics`；Evaluation=`§4 world-model evaluation`；Limitations/Counterevidence=`§5 limitations and environment/action boundary`。

<!-- claim:SF-2026-ARXIV-2605-25313:start -->UWM-JEPA: Predictive World Models That Imagine in Belief Space 的 exact-v1 只支持该文披露机制：We introduce the Unitary World Model JEPA (UWM-JEPA), a JEPA world model with a density-matrix latent on a joint system-environment space and a learned unitary predictor. 其未证明边界由 `§5 limitations and environment/action boundary` 限定；不能把该受限结果外推为跨模型、跨硬件、跨 workload 或生产 SLO 的通用优势。<!-- claim:SF-2026-ARXIV-2605-25313:end -->

Books Decision=`No Change — Existing Coverage`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-25313:end -->

<!-- review:SF-2026-ARXIV-2605-25338:start -->
#### CausalFlow: Causal Attribution and Counterfactual Repair for LLM Agent Failures

**问题与机制。** We introduce CausalFlow, an interventional framework that converts failed agent traces into minimal counterfactual repairs and reusable supervision. 该证据的系统 owner 定位为 `AGENT-PLATFORM`。

**Exact-v1 路径。** Method=`§3 Problem Setup; §4.1–§4.3 causal attribution, counterfactual repair and multi-agent validation`；Evaluation=`§5–§6 intervention protocol, repair performance, minimality and ablations`；Limitations/Counterevidence=`§7 Discussion; Appendix A.10 Runtime Analysis; Appendix B Future Work`。

<!-- claim:SF-2026-ARXIV-2605-25338:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-25338:end -->

Books Decision=`No Change — Existing Coverage`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-25338:end -->

<!-- review:SF-2026-ARXIV-2605-25375:start -->
#### Bandwidth-Aware and Cost-Efficient Pipeline Parallel Scheduling in Geo-Distributed LLM Training

**问题与机制。** To this end, we propose BACE-Pipe, a bandwidth-aware and cost-efficient pipeline scheduling framework for LLM training across geo-distributed clusters. 该证据的系统 owner 定位为 `TRAIN-PIPELINE-PARALLEL`。

**Exact-v1 路径。** Method=`§III problem definition; §III-B dynamic priority, bandwidth pathfinder and cost allocator`；Evaluation=`§IV-A–§IV-E geo-cluster setup, bandwidth/GPU/workload sensitivity and ablation`；Limitations/Counterevidence=`§II-A prior limitations; §V conclusion; evidence is simulator/trace-bound`。

<!-- claim:SF-2026-ARXIV-2605-25375:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-25375:end -->

Books Decision=`Integrate`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-25375:end -->

<!-- review:SF-2026-ARXIV-2605-25376:start -->
#### KYA: A Framework-Agnostic Trust Layer for Autonomous Systems with Verifiable Provenance and Hierarchical Policy Composition

**问题与机制。** KYA (Know Your Agents) is an open-source, framework-agnostic trust and governance layer for autonomous systems, composed of five primitives: (1) a four-gate inbound apply pipeline; (2) an only-tighten composition algebra over a three-channel multi-tenant hierarchy; (3) KYP (Know Your Principal), a schema-level unification of trust scoring across human users, AI agents, and service accounts; (4) auditable interaction-multiplier amplification over an AIVSS-shaped additive baseline; and (5) two-axis delegation attribution: a static premium for risky delegates and a runtime debit for actual delegate misbehavior in multi-agent fan-out. 该证据的系统 owner 定位为 `PLATFORM-SECURITY`。

**Exact-v1 路径。** Method=`§2 threat model; §3 three-layer runtime gates; §5 dynamic rogue signals; §6 evidence chain`；Evaluation=`§4.4 worked fleets; §8–§10 evaluation, red-team and performance sections`；Limitations/Counterevidence=`§4.5 calibration and limitations; §11 limitations and threat-model boundary`。

<!-- claim:SF-2026-ARXIV-2605-25376:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-25376:end -->

Books Decision=`No Change — Existing Coverage`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-25376:end -->

<!-- review:SF-2026-ARXIV-2605-25379:start -->
#### StateRAG: Typed State Contracts for Complex Retrieval-Augmented Generation

**问题与机制。** We introduce StateRAG, which represents retrieval control as a typed state external to the final reader. 该证据的系统 owner 定位为 `AGENT-RAG`。

**Exact-v1 路径。** Method=`§1.2 structured retrieval state; §3 tree memory, adaptive routing, MARS/SMP and access control`；Evaluation=`§4 datasets, main results, component ablation and verifier-guided recovery`；Limitations/Counterevidence=`§5 Limitations; Appendix A.4 efficiency accounting; Appendix F.3 failure modes`。

<!-- claim:SF-2026-ARXIV-2605-25379:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-25379:end -->

Books Decision=`Integrate`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-25379:end -->

<!-- review:SF-2026-ARXIV-2605-25389:start -->
#### Evo-Attacker: Memory-Augmented Reinforcement Learning for Long-Horizon Tool Attacks on LLM-MAS

**问题与机制。** While Large Language Model-based Multi-Agent Systems (LLM-MAS) demonstrate remarkable capabilities in solving complex tasks by orchestrating specialized agents and external tools, the implicit trust in tool outputs creates a critical attack surface. 该证据的系统 owner 定位为 `PLATFORM-SECURITY`。

**Exact-v1 路径。** Method=`§2 threat model; §3.1–§3.3 attack memory, memory-augmented attack and Attack-Flow GRPO`；Evaluation=`§4 main, ablation, stealth and cross-model experiments`；Limitations/Counterevidence=`§6 Conclusion; Appendix C framework/dataset/training scope`。

<!-- claim:SF-2026-ARXIV-2605-25389:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-25389:end -->

Books Decision=`No Change — Existing Coverage`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-25389:end -->

<!-- review:SF-2026-ARXIV-2605-25421:start -->
#### HyLaT: Efficient Multi-Agent Communication via Hybrid Latent-Text Protocol

**问题与机制。** Communication protocol design is a central challenge in large language model-based multi-agent systems. 该证据的系统 owner 定位为 `AGENT-MULTI-AGENT`。

**Exact-v1 路径。** Method=`§2.2–§2.4 dual-channel protocol, cross-channel alignment and interactive co-training`；Evaluation=`§3–§4 task/metric setup, ablation, compatibility, robustness and scale analysis`；Limitations/Counterevidence=`§6 Conclusion; Appendix B model-family/scale boundary`。

<!-- claim:SF-2026-ARXIV-2605-25421:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-25421:end -->

Books Decision=`No Change — Existing Coverage`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-25421:end -->

<!-- review:SF-2026-ARXIV-2605-25422:start -->
#### A Token/KV-Cache Communication Media Selection and Resource Allocation Strategy for Multi-Agent Collaboration

**问题与机制。** To address this, we propose a joint design that integrates communication-media selection with wireless resource allocation. 该证据的系统 owner 定位为 `AGENT-MULTI-AGENT`。

**Exact-v1 路径。** Method=`§3 system model; §4 token/KV latency; §5.1–§5.2 constrained mode and bandwidth optimization`；Evaluation=`§5.3 numerical validation and multi-round mode switching`；Limitations/Counterevidence=`§6 Conclusion and Future Work; wireless/model assumptions bound generality`。

<!-- claim:SF-2026-ARXIV-2605-25422:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-25422:end -->

Books Decision=`No Change — Existing Coverage`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-25422:end -->

<!-- review:SF-2026-ARXIV-2605-25424:start -->
#### SeqRoute: Global Budget-Aware Sequential LLM Routing via Offline Reinforcement Learning

**问题与机制。** We introduce SeqRoute, a framework that formulates multi-turn routing as a finite-horizon Markov Decision Process and solves it via offline reinforcement learning. 该证据的系统 owner 定位为 `INFER-SCHEDULING`。

**Exact-v1 路径。** Method=`§3 session-budget MDP; §4.1–§4.3 HBR, CQL and deployment lambda-sweep`；Evaluation=`§5 cost-safety frontier, delayed-gratification and ablation experiments`；Limitations/Counterevidence=`§6 Conclusion; offline reward proxy, single model pair and fixed-cost assumptions`。

<!-- claim:SF-2026-ARXIV-2605-25424:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-25424:end -->

Books Decision=`Integrate`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-25424:end -->

<!-- review:SF-2026-ARXIV-2605-25430:start -->
#### CODESKILL: Learning Self-Evolving Skills for Coding Agents

**问题与机制。** We propose CODESKILL, an LLM-based framework that reformulates skill extraction and skill-bank maintenance as a learnable management policy. 该证据的系统 owner 定位为 `AGENT-PLATFORM`。

**Exact-v1 路径。** Method=`§3.1 Skill extraction; §3.2 learnable skill-bank maintenance; §3.3 RL objective`；Evaluation=`§4 EnvBench, SWE-Bench Verified and Terminal-Bench 2; iterative-bank ablations`；Limitations/Counterevidence=`§5/Appendix: frozen downstream agent, benchmark and verifier-reward boundary`。

<!-- claim:SF-2026-ARXIV-2605-25430:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-25430:end -->

Books Decision=`Integrate`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-25430:end -->

<!-- review:SF-2026-ARXIV-2605-25451:start -->
#### BigMac: Breaking the Pareto Frontier of Compute and Memory in Multimodal LLM Training

**问题与机制。** We present BigMac, a new training pipeline for multimodal LLMs. 该证据的系统 owner 定位为 `TRAIN-DISTRIBUTED-TRAINING`。

**Exact-v1 路径。** Method=`Official author artifact §BigMac Method: dependency-safe nested pipeline, global operator-table schedule, scheduler/executor separation and PP-transparent interface`；Evaluation=`Official author artifact §Experiments: Qwen3-30B-A3B + 1.3B ViT; MMDiT extension; 8K sequence; Optimus/Megatron-DistTrain comparisons`；Limitations/Counterevidence=`Official author artifact §Evidence Boundary — no explicit Limitations section; hardware, precision, topology, concurrency and tail-SLO are Not Disclosed`。

<!-- claim:SF-2026-ARXIV-2605-25451:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-25451:end -->

Books Decision=`No Change — Existing Coverage`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-25451:end -->

<!-- review:SF-2026-ARXIV-2605-25475:start -->
#### IndexMem: Learned KV-Cache Eviction with Latent Memory for Long-Context LLM Inference

**问题与机制。** In this work, we introduce a learnable indexer that predicts KV importance, enabling more accurate retention of critical tokens. 该证据的系统 owner 定位为 `INFER-KV-CACHE`。

**Exact-v1 路径。** Method=`§3.1 learned token indexer; §3.2 latent fast/slow-weight memory`；Evaluation=`§4 RULER, NIAH, LongBench, compression and ablation`；Limitations/Counterevidence=`§6 Conclusion & Limitation; Appendix A limited budgets, models and frozen backbone`。

<!-- claim:SF-2026-ARXIV-2605-25475:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-25475:end -->

Books Decision=`No Change — Existing Coverage`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-25475:end -->

<!-- review:SF-2026-ARXIV-2605-25492:start -->
#### SafetyRepro: Configuration-Conditional Rank Instability on Alignment Benchmarks

**问题与机制。** Pairwise model comparisons drawn from foundation-model benchmarks ("A is safer than B") are read as quantitative verdicts but hinge on harness choices benchmark papers under-specify. 该证据的系统 owner 定位为 `PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1 路径。** Method=`§3 configuration grid; §4 SDI/CFR/rank-concordance/variance metrics`；Evaluation=`§5 configuration-conditional reversals and cross-package analysis`；Limitations/Counterevidence=`§6 Threats to Validity: narrow model/benchmark/envelope and qualitative variance attribution`。

<!-- claim:SF-2026-ARXIV-2605-25492:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-25492:end -->

Books Decision=`Integrate`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-25492:end -->

<!-- review:SF-2026-ARXIV-2605-25507:start -->
#### Credit Assignment with Resets in Language Model Reasoning

**问题与机制。** We propose two such methods: Random-Reset Policy Optimization (RRPO), where reset states are drawn randomly from reasoning steps, and Self-Reset Policy Optimization (SRPO), where the model self-localizes the erroneous step in an incorrect trajectory and resets there. 该证据的系统 owner 定位为 `TRAIN-PPO`。

**Exact-v1 路径。** Method=`§3 Conservative Policy Iteration with reset credit; §4 RRPO and SRPO`；Evaluation=`§5–§6 reasoning benchmarks, GRPO/RRPO/SRPO comparison and reset ablations`；Limitations/Counterevidence=`§7 Limitations: self-localized error and verifiable-reward reasoning scope`。

<!-- claim:SF-2026-ARXIV-2605-25507:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-25507:end -->

Books Decision=`Integrate`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-25507:end -->

<!-- review:SF-2026-ARXIV-2605-25521:start -->
#### CS-PQ: Cache-Friendly SIMD Product Quantization for Large-Scale ANNS Index Construction

**问题与机制。** Although CPU-based solutions are prevalent, they are essentially general-purpose designs that fail to capture the intrinsic characteristics of PQ construction.In this paper, we propose CS-PQ, a Cache-friendly, SIMD-optimized PQ framework based on modern CPUs. 该证据的系统 owner 定位为 `INFER-TENSORRT-LLM`。

**Exact-v1 路径。** Method=`§3 motivation; §4 centroid-parallel SIMD, cache organization and ranking-preserving reformulation`；Evaluation=`§5 setup, end-to-end, microbenchmark, ablation and microarchitecture evidence`；Limitations/Counterevidence=`§7 Conclusion; evaluated CPU/PQ construction boundary`。

<!-- claim:SF-2026-ARXIV-2605-25521:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-25521:end -->

Books Decision=`No Change — Existing Coverage`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-25521:end -->

<!-- review:SF-2026-ARXIV-2605-25535:start -->
#### Personalize-then-Store: Benchmarking and Learning Personalized Memory for Long-horizon Agents

**问题与机制。** We introduce PerMemBench, the first benchmark for evaluating personalized memory systems, featuring multi year, multi domain interaction histories across diverse user personas. 该证据的系统 owner 定位为 `AGENT-MEMORY`。

**Exact-v1 路径。** Method=`§3–§4 static/dynamic PerMem-Bench; §7.1 session-level personalized storage gating`；Evaluation=`§5 meta-evaluation; §6 protocol; §7.2 memory-system results`；Limitations/Counterevidence=`§8 Conclusion; appendix construction/judge/checkpoint-sampling boundaries`。

<!-- claim:SF-2026-ARXIV-2605-25535:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-25535:end -->

Books Decision=`No Change — Existing Coverage`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-25535:end -->

<!-- review:SF-2026-ARXIV-2605-25537:start -->
#### Action-Prior Denoising for Smooth Real-Time Chunking

**问题与机制。** We propose Soft RTC, a training-time RTC generalization based on action-prior denoising. 该证据的系统 owner 定位为 `MULTIMODAL-EMBODIED-VLA`。

**Exact-v1 路径。** Method=`§III problem; §IV-A action-prior denoising; §IV-B inference blending`；Evaluation=`§V–§VI Kinetix setup, real-robot pilot and delay/window sweeps`；Limitations/Counterevidence=`§VII Discussion; small real-robot pilot and policy/workload scope`。

<!-- claim:SF-2026-ARXIV-2605-25537:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-25537:end -->

Books Decision=`No Change — Existing Coverage`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-25537:end -->

<!-- review:SF-2026-ARXIV-2605-25547:start -->
#### TapSampling: Inference-Time Sampling with a Task-Progress-Understanding Verifier for Robotic Manipulation

**问题与机制。** In this paper, we propose \textbf{TapSampling}, a plug-and-play framework for inference-time sampling. 该证据的系统 owner 定位为 `MULTIMODAL-EMBODIED-VLA`。

**Exact-v1 路径。** Method=`§3.2 posterior action sampling; §3.3 task-progress verification`；Evaluation=`§4 simulation, real-world and sample/latent ablations`；Limitations/Counterevidence=`Appendix I linear-progress assumption and base-policy capacity boundary`。

<!-- claim:SF-2026-ARXIV-2605-25547:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-25547:end -->

Books Decision=`No Change — Existing Coverage`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-25547:end -->

<!-- review:SF-2026-ARXIV-2605-25550:start -->
#### DisagFusion: Asynchronous Pipeline Parallelism and Elastic Scheduling for Disaggregated Diffusion Serving

**问题与机制。** Diffusion-based generation is increasingly powering production content pipelines; however, deploying these models at scale remains a significant challenge. 该证据的系统 owner 定位为 `INFER-PD-DISAGGREGATION`。

**Exact-v1 路径。** Method=`§2 workload/stage imbalance; §3 async pipeline and hybrid instance scheduler; §4 implementation`；Evaluation=`§5 quality, latency, scale, robustness, elasticity and utilization`；Limitations/Counterevidence=`§7 Conclusion; diffusion-stage topology and disclosed hardware/workload boundary`。

<!-- claim:SF-2026-ARXIV-2605-25550:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-25550:end -->

Books Decision=`Integrate`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-25550:end -->

<!-- review:SF-2026-ARXIV-2605-25621:start -->
#### StreamOV: Streaming Omni-Video Understanding via Evidence-Guided Memory and Response Triggering

**问题与机制。** To bridge these gaps, we propose StreamOV, a novel Streaming Omni-Video understanding framework for efficient online audio-visual reasoning with bounded memory and proactive response triggering. 该证据的系统 owner 定位为 `MULTIMODAL-GENERATIVE-PARADIGMS`。

**Exact-v1 路径。** Method=`§4.1 evidence construction; §4.2 long/short memory update; §4.3 response trigger`；Evaluation=`§3 SOVBench and §5 audio-visual/visual-only/ablation evaluation`；Limitations/Counterevidence=`Appendix J trigger failures; Appendix K limitations and future work`。

<!-- claim:SF-2026-ARXIV-2605-25621:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-25621:end -->

Books Decision=`No Change — Existing Coverage`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-25621:end -->

<!-- review:SF-2026-ARXIV-2605-25624:start -->
#### CUA-Gym: Scaling Verifiable Training Environments and Tasks for Computer-Use Agents

**问题与机制。** We present CUA-Gym, a scalable pipeline that co-generates task instructions, environment states, and reward functions. 该证据的系统 owner 定位为 `AGENT-PLATFORM`。

**Exact-v1 路径。** Method=`§2.1 adversarial task/reward co-generation; §2.2 environment scaling`；Evaluation=`§3–§4 training results, data/environment scaling and emergent multi-action calls`；Limitations/Counterevidence=`§6 Limitations; synthetic task and environment-fidelity boundary`。

<!-- claim:SF-2026-ARXIV-2605-25624:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-25624:end -->

Books Decision=`No Change — Existing Coverage`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-25624:end -->

<!-- review:SF-2026-ARXIV-2605-25632:start -->
#### Insuring Every Action: An Authority Frontier Framework for Runtime Actuarial Control of Autonomous AI Agents

**问题与机制。** We propose the Actuarial Action Interface (AAI), a deterministic runtime contract that prices each such action against a contractually fixed safe default under a time-consistent risk mapping, and gates execution against a per-boundary reserve capital budget. 该证据的系统 owner 定位为 `AGENT-TOOL-CALLING`。

**Exact-v1 路径。** Method=`§3 action taxonomy and quote-bind-commit; §4 authority frontier and capital metrics`；Evaluation=`§5–§7 simulation, calibration and runtime-control experiments`；Limitations/Counterevidence=`§8 Limitations; actuarial assumptions and empirical deployment boundary`。

<!-- claim:SF-2026-ARXIV-2605-25632:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-25632:end -->

Books Decision=`Integrate`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-25632:end -->

<!-- review:SF-2026-ARXIV-2605-25641:start -->
#### Iterate Until Retrieved: Factual Nugget Optimization for Discoverable Continual Corrections in Agentic RAG

**问题与机制。** We identify these instances and convert them into compact knowledge-base entries, which we call factual nuggets. 该证据的系统 owner 定位为 `AGENT-RAG`。

**Exact-v1 路径。** Method=`§3 production correction setting; §4 factual-nugget variants and iterative optimization`；Evaluation=`§5–§6 held-out, transfer, negative-control and answer-level results`；Limitations/Counterevidence=`§7 Conclusion: one retrieval architecture, English-only and LLM dependence`。

<!-- claim:SF-2026-ARXIV-2605-25641:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-25641:end -->

Books Decision=`No Change — Existing Coverage`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-25641:end -->

<!-- review:SF-2026-ARXIV-2605-25653:start -->
#### When Agents Control Robots: A Zero Trust Policy Model for Agentic Cyber-Physical Systems

**问题与机制。** We analyse this threat landscape through Cobot-Claw, a deployed four-agent system for UR3e robotic arm control, and identify five attack classes specific to agentic cyber-physical systems. 该证据的系统 owner 定位为 `PLATFORM-SECURITY`。

**Exact-v1 路径。** Method=`§3 threat/system model; §4 typed zero-trust enforcement and physical-impact tiers`；Evaluation=`§5 deployed instantiation, 60 traces and coverage analysis`；Limitations/Counterevidence=`§6 Conclusion; small system/model/trace envelope`。

<!-- claim:SF-2026-ARXIV-2605-25653:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-25653:end -->

Books Decision=`No Change — Existing Coverage`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-25653:end -->

<!-- review:SF-2026-ARXIV-2605-25655:start -->
#### Bandwidth-Aware LLM Inference on Heterogeneous Many-Core Supercomputers

**问题与机制。** To address this problem, we propose THInfer, a hardware-aware inference framework that maximizes data locality under bandwidth-constrained conditions through hardware-software co-design and parallel strategy optimization. 该证据的系统 owner 定位为 `INFER-SCHEDULING`。

**Exact-v1 路径。** Method=`§III-A framework; §III-B operators; §III-C graph schedule; §III-D adaptive parallelism`；Evaluation=`§IV throughput, ablation and operator scaling experiments`；Limitations/Counterevidence=`§V Conclusion; MT-3000-specific architecture and bandwidth boundary`。

<!-- claim:SF-2026-ARXIV-2605-25655:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-25655:end -->

Books Decision=`No Change — Existing Coverage`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-25655:end -->

<!-- review:SF-2026-ARXIV-2605-25673:start -->
#### Referential Security as a New Paradigm for AI Evaluations

**问题与机制。** To resolve this, we propose referential security as a new paradigm for AI evaluation. 该证据的系统 owner 定位为 `PLATFORM-SECURITY`。

**Exact-v1 路径。** Method=`§3 referential stability; §4 threat model; §5 workflows; §8 attestation/fingerprinting architectures`；Evaluation=`§7 provider identifier survey and workflow analysis`；Limitations/Counterevidence=`§9 Conclusions; proposal-level evidence without broad deployed evaluation`。

<!-- claim:SF-2026-ARXIV-2605-25673:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-25673:end -->

Books Decision=`Integrate`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-25673:end -->

<!-- review:SF-2026-ARXIV-2605-25674:start -->
#### Stochastic Estimation of the Layer-wise Hessian Trace for Monitoring Neural-network Training

**问题与机制。** We present a stochastic estimator of the trace of the diagonal blocks of the Hessian matrix of the empirical risk of a neural network. 该证据的系统 owner 定位为 `PLATFORM-MONITORING`。

**Exact-v1 路径。** Method=`§2 layer-wise target; §3 unbiased estimator; §4 variance analysis`；Evaluation=`§5 memorisation-regime setup, decision rule and empirical validation`；Limitations/Counterevidence=`§6 Discussion and limitations; modest model/monitoring setting`。

<!-- claim:SF-2026-ARXIV-2605-25674:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-25674:end -->

Books Decision=`No Change — Existing Coverage`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-25674:end -->

<!-- review:SF-2026-ARXIV-2605-25682:start -->
#### Profiling-Driven Adaptive Distributed Transformer Inference on Embedded Edge Deployment

**问题与机制。** We present a hardware prototype study on NVIDIA Jetson Orin Nano devices connected over WiFi. 该证据的系统 owner 定位为 `INFER-SCHEDULING`。

**Exact-v1 路径。** Method=`§3 segment communication, staging bottleneck and adaptive inference`；Evaluation=`§4 prototype; §5 latency, energy, qualitative and instrumentation results`；Limitations/Counterevidence=`§6 Conclusion; Jetson/Wi-Fi prototype and qualitative-output boundary`。

<!-- claim:SF-2026-ARXIV-2605-25682:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-25682:end -->

Books Decision=`No Change — Existing Coverage`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-25682:end -->

<!-- review:SF-2026-ARXIV-2605-25698:start -->
#### How Should LLMs Consume High-Quality Data? Optimal Data Scheduling via Quality-Aware Functional Scaling Laws

**问题与机制。** Motivated by the theoretical structure, we propose Drop-Stable-Rampup for LLM midtraining: drop the batch size at the quality transition, keep it low to accumulate signal, then ramp up to suppress noise. 该证据的系统 owner 定位为 `TRAIN-DATA`。

**Exact-v1 路径。** Method=`§3 quality-aware functional scaling law; §4 optimal schedule; §5.1 Drop-Stable-Rampup`；Evaluation=`§5.2–§5.4 batch drop, phase ratio and schedule comparison`；Limitations/Counterevidence=`§6 scope: theoretical simplification, multi-task heterogeneity, scale dependence and overhead`。

<!-- claim:SF-2026-ARXIV-2605-25698:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-25698:end -->

Books Decision=`Integrate`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-25698:end -->

<!-- review:SF-2026-ARXIV-2605-25707:start -->
#### AgentHijack: Benchmarking Computer Use Agent Robustness to Common Environment Corruptions

**问题与机制。** We introduce AgentHijack, a benchmark designed to evaluate the robustness of computer-use agents under common corruptions, where the uncertainties in dynamic environment disrupt the execution flow without direct adversarial intent. 该证据的系统 owner 定位为 `PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1 路径。** Method=`§3 corruption benchmark; §4 robustness method`；Evaluation=`§5 setup, main results and ablation; Appendix E case studies`；Limitations/Counterevidence=`§6 Conclusion; OSWorld corruption/model envelope`。

<!-- claim:SF-2026-ARXIV-2605-25707:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-25707:end -->

Books Decision=`No Change — Existing Coverage`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-25707:end -->

<!-- review:SF-2026-ARXIV-2605-25716:start -->
#### An Efficient and Privacy-Preserving Architecture for Cross-Institutional Collaborative RAG

**问题与机制。** To address this challenge, we present FedRAG, a high-throughput, privacy-preserving federated RAG framework. 该证据的系统 owner 定位为 `PLATFORM-SECURITY`。

**Exact-v1 路径。** Method=`§3 threat model; §4 scrambled distributed attention; §5 role-aware collaborative RAG`；Evaluation=`§6 privacy analysis; §7 latency, network, utility and quantization evaluation`；Limitations/Counterevidence=`§8 Discussion; honest-but-curious assumptions and disclosed network/topology boundary`。

<!-- claim:SF-2026-ARXIV-2605-25716:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-25716:end -->

Books Decision=`No Change — Existing Coverage`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-25716:end -->

<!-- review:SF-2026-ARXIV-2605-25745:start -->
#### Selective Latent Thinking: Adaptive Compression of LLM Reasoning Chains

**问题与机制。** In this work, we propose Selective Latent Thinking (SLT), a framework that selectively compresses redundant reasoning spans into latent representations while preserving precision-critical spans as explicit CoT within the same reasoning trajectory. 该证据改变的是 reasoning representation 的选择与可观测性边界，系统 owner 定位为 `MODEL-DECODER-ONLY`；它不是 speculative verification、rollback 或 commit protocol。

**Exact-v1 路径。** Method=`§3 span anticipation, confidence gate, latent encoding and three-stage training`；Evaluation=`§4 four math benchmarks; compression/accuracy/latency and gating ablations`；Limitations/Counterevidence=`§5 Limitations: math/model/calibration scope and latent-span error propagation`。

<!-- claim:SF-2026-ARXIV-2605-25745:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-25745:end -->

Books Decision=`Integrate`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-25745:end -->

<!-- review:SF-2026-ARXIV-2605-25746:start -->
#### Multi-Agent Coordination Adaptation via Structure-Guided Orchestration

**问题与机制。** We introduce MACA, an automated coordination framework that learns a task- and budget-conditioned structural prior over agent participation and interactions. 该证据的系统 owner 定位为 `AGENT-MULTI-AGENT`。

**Exact-v1 路径。** Method=`§3 joint structure/orchestration posterior; §4 task-budget structural prior and policy orchestration`；Evaluation=`§5 benchmark/token-budget comparisons and interaction ablations`；Limitations/Counterevidence=`§6 Limitations: tested tasks/models/budgets and centralized training assumptions`。

<!-- claim:SF-2026-ARXIV-2605-25746:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-25746:end -->

Books Decision=`Integrate`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-25746:end -->

<!-- review:SF-2026-ARXIV-2605-25798:start -->
#### DiSC: Resolution-Scalable Acceleration of Diffusion Models by Exploiting Sparsity and Cached Token Reuse with Hash-based Distribution

**问题与机制。** In this paper, we propose DiSC, a resolution-scalable, sparsity-aware hardware accelerator. 该证据的系统 owner 定位为 `INFER-TENSORRT-LLM`。

**Exact-v1 路径。** Method=`§III cached-token reuse and softmax-threshold mask reuse; §IV hash-distributed hardware`；Evaluation=`§V methodology, performance, area/power and high-resolution comparison`；Limitations/Counterevidence=`§VII Conclusion; specialized architecture and diffusion-workload simulation boundary`。

<!-- claim:SF-2026-ARXIV-2605-25798:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-25798:end -->

Books Decision=`No Change — Existing Coverage`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-25798:end -->

<!-- review:SF-2026-ARXIV-2605-25815:start -->
#### Behind EvoMap: Characterizing a Self-Evolving Agent-to-Agent Collaboration Network

**问题与机制。** We present the first large-scale empirical study of EvoMap, a prominent A2A collaboration network. 该证据的系统 owner 定位为 `AGENT-PLATFORM`。

**Exact-v1 路径。** Method=`§3 EvoMap dataset/protocol reconstruction; §4 reuse, credit, GDI and validation analysis`；Evaluation=`§5–§7 1.5M assets/128K agents empirical audit and manipulation checks`；Limitations/Counterevidence=`§8 limitations: 47-day observational snapshot, one ecosystem and self-reported fields`。

<!-- claim:SF-2026-ARXIV-2605-25815:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-25815:end -->

Books Decision=`Integrate`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-25815:end -->

<!-- review:SF-2026-ARXIV-2605-25819:start -->
#### On Reliability of Efficient Membership Inference Vulnerability Evaluation

**问题与机制。** We demonstrate two key weaknesses in this efficient MIA evaluation pipeline. 该证据的系统 owner 定位为 `PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1 路径。** Method=`§3 per-sample vulnerability; §4 calibrated aggregation; §5 finite-population correction`；Evaluation=`§6 efficient LiRA experiments and analytical simulation`；Limitations/Counterevidence=`§7/Appendix: Gaussian post-processing, finite shadow-model and dataset scope`。

<!-- claim:SF-2026-ARXIV-2605-25819:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-25819:end -->

Books Decision=`Integrate`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-25819:end -->

<!-- review:SF-2026-ARXIV-2605-25820:start -->
#### Visual-Redundancy-Controlled Parallel Decoding for Diffusion-Based Multimodal Large Language Models

**问题与机制。** We identify a step-level limitation of this strategy in multimodal settings: high-confidence tokens selected in the same step can rely on overlapping visual grounding, introducing visual redundancy among the committed tokens and leaving less complementary visual grounding available for later decoding. 该证据的系统 owner 定位为 `MULTIMODAL-GENERATIVE-PARADIGMS`。

**Exact-v1 路径。** Method=`§3.2 visual redundancy; §3.3 redundancy-controlled parallel decoding`；Evaluation=`§4 model/benchmark comparison, certainty analysis and ablation`；Limitations/Counterevidence=`Appendix A.3 limitations; backbone and multimodal-task scope`。

<!-- claim:SF-2026-ARXIV-2605-25820:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-25820:end -->

Books Decision=`No Change — Existing Coverage`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-25820:end -->

<!-- review:SF-2026-ARXIV-2605-25831:start -->
#### Clarify, Abstain or Answer? Strategising in Conversation with Belief-Augmented Generation

**问题与机制。** We propose Belief-Augmented Generation (BAG): grounding LLMs in their own belief state via the prompt and letting them reason over these K samples to decide on a conversational strategy: answer, clarify, or abstain. 该证据的系统 owner 定位为 `AGENT-REFLECTION`。

**Exact-v1 路径。** Method=`§3.1 belief-state construction; §3.2 clarify/abstain/answer strategy`；Evaluation=`§4–§7 interaction simulation, accuracy, clarification and faithfulness`；Limitations/Counterevidence=`§9 Limitations; simulated-user/judge and dataset ambiguity boundary`。

<!-- claim:SF-2026-ARXIV-2605-25831:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-25831:end -->

Books Decision=`Integrate`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-25831:end -->

<!-- review:SF-2026-ARXIV-2605-25854:start -->
#### From Accounting to Coordination: A Virtual Water-Aware Electricity-Computation-Water Nexus Framework for Data Center Dispatch

**问题与机制。** Case studies on the IEEE 30-bus and 118-bus test systems demonstrate reliable convergence, exact power-water consistency, and reductions of approximately 3-5% in generation-related freshwater withdrawals under water-constrained conditions. 该证据的系统 owner 定位为 `PLATFORM-COST`。

**Exact-v1 路径。** Method=`§3 differentiable ECW dispatch layer; §4 fixed-point virtual-water coordination`；Evaluation=`§5 IEEE 30/118-bus dispatch and consistency experiments`；Limitations/Counterevidence=`§6 limitations: simulated grid, water-attribution model and no production DC trace`。

<!-- claim:SF-2026-ARXIV-2605-25854:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-25854:end -->

Books Decision=`Integrate`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-25854:end -->

<!-- review:SF-2026-ARXIV-2605-25869:start -->
#### Mitigating Provenance-Role Collapse in Long-Term Agents via Typed Memory Representation

**问题与机制。** To resolve this cognitive vulnerability at the architectural level, we propose MemIR, a typed Memory Intermediate Representation that operationalizes source monitoring as a structural constraint. 该证据的系统 owner 定位为 `AGENT-MEMORY`。

**Exact-v1 路径。** Method=`§3.1 typed memory atoms; §3.2 multi-route projection; §3.3 provenance-scoped use`；Evaluation=`§4 main results, ablation, backbone and hyperparameter analysis`；Limitations/Counterevidence=`§5 Conclusion; benchmark/prompt and long-term deployment boundary`。

<!-- claim:SF-2026-ARXIV-2605-25869:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-25869:end -->

Books Decision=`Integrate`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-25869:end -->

<!-- review:SF-2026-ARXIV-2605-25874:start -->
#### WBench: A Comprehensive Multi-turn Benchmark for Interactive Video World Model Evaluation

**问题与机制。** To fill this gap, we introduce WBench, a comprehensive multi-turn benchmark for interactive world model evaluation along five dimensions, namely video quality, setting adherence, interaction adherence, consistency, and physics compliance. 该证据的系统 owner 定位为 `MULTIMODAL-WORLD-MODELS`。

**Exact-v1 路径。** Method=`§3 multi-turn dataset; §4 world-model evaluation suite`；Evaluation=`§5 protocol, per-dimension, cross-dimension and human-alignment results`；Limitations/Counterevidence=`§6 Conclusion; Appendix B web-model access and configuration boundary`。

<!-- claim:SF-2026-ARXIV-2605-25874:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-25874:end -->

Books Decision=`No Change — Existing Coverage`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-25874:end -->

<!-- review:SF-2026-ARXIV-2605-25889:start -->
#### Capability and Robustness Cannot Both Be Free: An Information-Theoretic Bound for Vision-Language-Action Models

**问题与机制。** Vision-Language-Action (VLA) models reach high success rates on clean inputs but collapse under small adversarial perturbations: a $16/255$ PGD attack drops OpenVLA-7B's LIBERO success from $95\%$ to under $5\%$. 该证据的系统 owner 定位为 `MULTIMODAL-EMBODIED-VLA`。

**Exact-v1 路径。** Method=`§3 information-theoretic capability/robustness bound; §4 encoder-specific corollary`；Evaluation=`§5 Gaussian/OpenVLA/LIBERO/PGD and cross-architecture diagnostics`；Limitations/Counterevidence=`§6 limitations: loose pixel bound, estimated mutual information and tested attacks`。

<!-- claim:SF-2026-ARXIV-2605-25889:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-25889:end -->

Books Decision=`Integrate`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-25889:end -->

<!-- review:SF-2026-ARXIV-2605-25893:start -->
#### $D^2$-Monitor: Dynamic Safety Monitoring for Diffusion LLMs via Hesitation-Aware Routing

**问题与机制。** Motivated by the suitability of lightweight probes for always-on monitoring, we analyze which trajectory-level signals best indicate when such probes are likely to struggle. 该证据的系统 owner 定位为 `PLATFORM-SECURITY`。

**Exact-v1 路径。** Method=`§3 hesitation signals; §4 cascade monitor and probe routing`；Evaluation=`§5 datasets/models, efficiency-effectiveness, robustness and ablation`；Limitations/Counterevidence=`Appendix A Limitation; evaluated diffusion models/remasking strategies only`。

<!-- claim:SF-2026-ARXIV-2605-25893:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-25893:end -->

Books Decision=`Integrate`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-25893:end -->

<!-- review:SF-2026-ARXIV-2605-25966:start -->
#### Mapping the Schedule x Bit-Width Boundary in Sub-100M Quantisation-Aware Training

**问题与机制。** We test whether the optimal learning-rate schedule depends on bit-width during from-initialisation quantisation-aware training (QAT) for sub-100M decoder language models. 该证据的系统 owner 定位为 `INFER-TENSORRT-LLM`。

**Exact-v1 路径。** Method=`§3 QAT implementation, LR schedule and factorial/ablation grid`；Evaluation=`§4–§5 compute/statistical protocol and schedule×bit-width results`；Limitations/Counterevidence=`§6.8 Limitations; sub-100M and tested optimizer/data regime`。

<!-- claim:SF-2026-ARXIV-2605-25966:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-25966:end -->

Books Decision=`No Change — Existing Coverage`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-25966:end -->

<!-- review:SF-2026-ARXIV-2605-25971:start -->
#### Anticipate and Learn: Unleashing Idle-Time Compute in Proactive Agents

**问题与机制。** While AI agents demonstrate remarkable capabilities in reasoning and tool use, they remain fundamentally reactive: they compute responses only after explicit user prompts. 该证据的系统 owner 定位为 `AGENT-PLATFORM`。

**Exact-v1 路径。** Method=`§3 proactive need prediction; §4 idle-time evidence acquisition and persistent-memory loop`；Evaluation=`§5 ProActEval/MemBench, turn/effort/hallucination and ablation results`；Limitations/Counterevidence=`§6 limitations: predictable-need scenarios, privacy/cost and stale anticipation`。

<!-- claim:SF-2026-ARXIV-2605-25971:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-25971:end -->

Books Decision=`Integrate`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-25971:end -->

<!-- review:SF-2026-ARXIV-2605-25988:start -->
#### What Makes a Medical Checker Trainable? Diagnosing Signal Collapse and Reward Hacking in Checker-Guided RAG for Biomedical QA

**问题与机制。** Medical RAG needs evidence-grounded claims, so plugging a claim-level NLI checker into retrieval-augmented RL is intuitive. 该证据的系统 owner 定位为 `AGENT-RAG`。

**Exact-v1 路径。** Method=`§3 checker backends and reward; §5 signal collapse; §6 reward-hacking cascade`；Evaluation=`§4 main/cross-model results and appendices 9–16`；Limitations/Counterevidence=`§8 listed limitations: evaluation independence, seeds, test size, domain and incomplete cascade resolution`。

<!-- claim:SF-2026-ARXIV-2605-25988:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-25988:end -->

Books Decision=`Integrate`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-25988:end -->

<!-- review:SF-2026-ARXIV-2605-25997:start -->
#### Deployment-complete benchmarking

**问题与机制。** We introduce deployment-complete benchmarking, which tests whether benchmark evidence determines a deployment action. 该证据的系统 owner 定位为 `PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1 路径。** Method=`§2 evidence fibers and action completeness; §3 completion curves; §4 certify-then-acquire`；Evaluation=`§5 controlled channels and Tox21/Matbench/JARVIS audits`；Limitations/Counterevidence=`§6 limitations: finite response spaces, selected public datasets and action model`。

<!-- claim:SF-2026-ARXIV-2605-25997:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-25997:end -->

Books Decision=`Integrate`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-25997:end -->

<!-- review:SF-2026-ARXIV-2605-26029:start -->
#### CausaLab: A Scalable Environment for Interactive Causal Discovery Toward AI Scientists

**问题与机制。** We introduce CausaLab, a scalable environment for evaluating interactive causal discovery by LLM agents. 该证据的系统 owner 定位为 `AGENT-WORKFLOW`。

**Exact-v1 路径。** Method=`§3 interactive SCM environment; §4 parsable causal-trajectory DSL`；Evaluation=`§5 mechanism recovery, interventions, scale and verification results`；Limitations/Counterevidence=`§8 Limitations; synthetic SCM and benchmark-agent scope`。

<!-- claim:SF-2026-ARXIV-2605-26029:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-26029:end -->

Books Decision=`No Change — Existing Coverage`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-26029:end -->

<!-- review:SF-2026-ARXIV-2605-26037:start -->
#### Peak-Then-Collapse and the Four Interface Channels of Knowledge-Graph Tool Use

**问题与机制。** We test the standard RLVR tool-use recipe -- GRPO on Qwen2.5-7B-Instruct -- on a deliberately minimal knowledge-graph tool API: four Freebase navigation verbs over Complex WebQuestions. 该证据的系统 owner 定位为 `TRAIN-GRPO`。

**Exact-v1 路径。** Method=`§2 KG tool interface and RLVR setup; §3 four feedback channels; §4 reward variants`；Evaluation=`§5 four-seed peak-collapse, oracle relation ablation and self-distillation`；Limitations/Counterevidence=`§6 limitations: Freebase/CWQ/Qwen2.5-7B and interface-specific failure`。

<!-- claim:SF-2026-ARXIV-2605-26037:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-26037:end -->

Books Decision=`Integrate`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-26037:end -->

<!-- review:SF-2026-ARXIV-2605-26045:start -->
#### Confidence and Calibration of Activation Oracles for Reliable Interpretation of Language Model Internals

**问题与机制。** An activation oracle is a language model trained to read another model's internal activations and describe them in natural language, for example to name a secret word the other model was trained to hide. 该证据的系统 owner 定位为 `PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1 路径。** Method=`§3 five confidence operators for activation oracles; §4 calibration protocol`；Evaluation=`§5 four Qwen/Gemma oracles, 6K samples/operator and label/no-label comparisons`；Limitations/Counterevidence=`§6 limitations: secret-word task, enumerability and no general interpretability guarantee`。

<!-- claim:SF-2026-ARXIV-2605-26045:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-26045:end -->

Books Decision=`Integrate`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-26045:end -->

<!-- review:SF-2026-ARXIV-2605-26046:start -->
#### When Gradients Collide: Failure Modes of Multi-Objective Prompt Optimization for LLM Judges

**问题与机制。** These results identify two separable failure modes: optimization-time gradient dilution and inference-time instruction interference, which together constrain the design space for multi-objective judge optimization using textual feedback. 该证据的系统 owner 定位为 `PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1 路径。** Method=`§3 decomposition grid; §5 gradient-specificity and instruction-interference analysis`；Evaluation=`§4 results and appendices B–F trajectory/task diagnostics`；Limitations/Counterevidence=`§6–§7 conclusion/future work; two datasets and textual-gradient optimizer scope`。

<!-- claim:SF-2026-ARXIV-2605-26046:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-26046:end -->

Books Decision=`No Change — Existing Coverage`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-26046:end -->

<!-- review:SF-2026-ARXIV-2605-26047:start -->
#### Retrying vs Resampling in AI Control

**问题与机制。** We study retrying from an AI control perspective, which treats the model as potentially adversarial. 该证据的系统 owner 定位为 `PLATFORM-SECURITY`。

**Exact-v1 路径。** Method=`§2 control setting/metrics; §3 retrying; §4 resampling and audit aggregation`；Evaluation=`§5–§6 BashArena safety/usefulness, budget and selective-resampling experiments`；Limitations/Counterevidence=`§7 limitations: one coding arena, model/monitor pair and adaptive adversary`。

<!-- claim:SF-2026-ARXIV-2605-26047:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-26047:end -->

Books Decision=`Integrate`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-26047:end -->

<!-- review:SF-2026-ARXIV-2605-26079:start -->
#### Automated Benchmark Auditing for AI Agents and Large Language Models

**问题与机制。** We introduce Auto Benchmark Audit (ABA), an agentic framework that systematically audits individual benchmark tasks, uncovering issues such as hidden environment dependencies, specification gaps, and limited grading logic. 该证据的系统 owner 定位为 `PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1 路径。** Method=`§2 evidence-collector/auditor; §3 benchmark-quality audit protocol`；Evaluation=`§4 fix/manual validation and §5 trajectory audit analysis`；Limitations/Counterevidence=`§7 Conclusion; automated auditor false-positive/coverage and sampled-benchmark boundary`。

<!-- claim:SF-2026-ARXIV-2605-26079:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-26079:end -->

Books Decision=`No Change — Existing Coverage`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-26079:end -->

<!-- review:SF-2026-ARXIV-2605-26110:start -->
#### Prism: A Plug-in Reproducible Infrastructure for Scalable Multimodal Continual Instruction Tuning

**问题与机制。** To address this, we introduce Prism, a plug-in reproducible codebase specifically designed for scalable MCIT research. 该证据的系统 owner 定位为 `TRAIN-DISTRIBUTED-TRAINING`。

**Exact-v1 路径。** Method=`§3 backbone/plugin boundary, registration API and scalable training integration`；Evaluation=`§4 reproducibility/continual-tuning method comparisons`；Limitations/Counterevidence=`§5 limitations: research codebase, supported backbones and no production fault study`。

<!-- claim:SF-2026-ARXIV-2605-26110:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-26110:end -->

Books Decision=`No Change — Existing Coverage`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-26110:end -->

<!-- review:SF-2026-ARXIV-2605-26112:start -->
#### From Model Scaling to System Scaling: Scaling the Harness in Agentic AI

**问题与机制。** This paper studies the next major bottleneck in agentic AI as system scaling, not only model scaling: the design of auditable, persistent, modular, and verifiable architectures around foundation models. 该证据的系统 owner 定位为 `AGENT-PLATFORM`。

**Exact-v1 路径。** Method=`§3 harness infrastructure and temporal layers; §4 context/memory/skill bottlenecks`；Evaluation=`§5 process/longitudinal evaluation and safe evolution argument`；Limitations/Counterevidence=`§6 alternative views and limitations; position/framework paper without controlled deployment study`。

<!-- claim:SF-2026-ARXIV-2605-26112:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-26112:end -->

Books Decision=`No Change — Existing Coverage`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-26112:end -->

<!-- review:SF-2026-ARXIV-2605-26114:start -->
#### MobileGym: A Verifiable and Highly Parallel Simulation Platform for Mobile GUI Agent Research

**问题与机制。** We present MobileGym, a browser-hosted, lightweight, fully controllable environment for everyday mobile use, targeting interaction fidelity without replicating proprietary backends. 该证据的系统 owner 定位为 `AGENT-PLATFORM`。

**Exact-v1 路径。** Method=`§3.1 layered state model; §3.2 programmable/serializable state and verifiable outcomes`；Evaluation=`§4 protocol; §5 benchmark, sim-to-real, judge error and efficiency`；Limitations/Counterevidence=`§6 listed visual/backend/app/legal/misuse limitations`。

<!-- claim:SF-2026-ARXIV-2605-26114:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-26114:end -->

Books Decision=`No Change — Existing Coverage`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-26114:end -->

<!-- review:SF-AERIC-ANTICIPATORY-HIDDEN-STATE-MONITORING-FOR-IMPLICIT-HARMFUL-DIALOGUE:start -->
#### AERIC: Anticipatory Hidden-State Monitoring for Implicit Harmful Dialogue

问题与机制：We study anticipatory same-pass monitoring, where a safety monitor may read hidden states produced during ordinary decoding but may not invoke an additional forward pass through the base model.。机制 owner=`PLATFORM-MONITORING`。
全文定位：`arXiv:2605.23974v1 HTML — §3 AERIC — same-pass hidden-state hazard forecasting and EMA rule`；evaluation=`§4 Setup and §5 Results — transfer, safe-budget and latency evaluation`；limitations/counterevidence=`§6 Limitations and Broader Impact — white-box state access, model and threshold-shift boundary`。
<!-- claim:SF-AERIC-ANTICIPATORY-HIDDEN-STATE-MONITORING-FOR-IMPLICIT-HARMFUL-DIALOGUE:start -->只支持 exact-v1 披露的 workload、模型、硬件、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。该证据不证明跨模型/硬件/部署的一般优势。<!-- claim:SF-AERIC-ANTICIPATORY-HIDDEN-STATE-MONITORING-FOR-IMPLICIT-HARMFUL-DIALOGUE:end -->
Books Decision=`Integrate`。旧方案在固定 workload、较低风险或无需新增 owner 时仍成立；新机制引入的分类器/控制器误差、额外状态、迁移成本与攻击面必须与 fallback/coexistence 同时进入 owner narrative。
<!-- review:SF-AERIC-ANTICIPATORY-HIDDEN-STATE-MONITORING-FOR-IMPLICIT-HARMFUL-DIALOGUE:end -->

<!-- review:SF-FAITHFUL-OR-FABRICATED-A-CAUSAL-FRAMEWORK-FOR-RATIONALIZATION-BIAS-IN-LL:start -->
#### Faithful or Fabricated? A Causal Framework for Rationalization Bias in LLM Judges

问题与机制：We introduce a suite of cue interventions (Blind, Truth, Flip, Placebo, Reveal-After) and tie-aware metrics that quantify outcome anchoring and rationale anchoring, including label-aligned rhetoric and explanation drift, alongside consistency and stereotype-intrusion checks.。机制 owner=`PLATFORM-EVALUATION-SYSTEM`。
全文定位：`arXiv:2605.23970v1 HTML — §III Problem Formulation and §IV causal cue-intervention method`；evaluation=`§V Experiments — tie-aware anchoring and mitigation metrics`；limitations/counterevidence=`§VI Limitations / Conclusion — judge, summarization and cue-family boundary`。
<!-- claim:SF-FAITHFUL-OR-FABRICATED-A-CAUSAL-FRAMEWORK-FOR-RATIONALIZATION-BIAS-IN-LL:start -->只支持 exact-v1 披露的 workload、模型、硬件、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。该证据不证明跨模型/硬件/部署的一般优势。<!-- claim:SF-FAITHFUL-OR-FABRICATED-A-CAUSAL-FRAMEWORK-FOR-RATIONALIZATION-BIAS-IN-LL:end -->
Books Decision=`Integrate`。旧方案在固定 workload、较低风险或无需新增 owner 时仍成立；新机制引入的分类器/控制器误差、额外状态、迁移成本与攻击面必须与 fallback/coexistence 同时进入 owner narrative。
<!-- review:SF-FAITHFUL-OR-FABRICATED-A-CAUSAL-FRAMEWORK-FOR-RATIONALIZATION-BIAS-IN-LL:end -->

<!-- review:SF-LGMT-LOGIC-GROUNDED-METAMORPHIC-TESTING-FOR-EVALUATING-THE-REASONING-REL:start -->
#### LGMT: Logic-Grounded Metamorphic Testing for Evaluating the Reasoning Reliability of LLMs

问题与机制：We propose LGMT (Logic-Grounded Metamorphic Testing), an oracle-free framework that leverages first-order logic (FOL) to evaluate LLM reasoning.。机制 owner=`PLATFORM-EVALUATION-SYSTEM`。
全文定位：`arXiv:2605.23965v1 HTML — §3 logic-grounded metamorphic test generator`；evaluation=`arXiv:2605.23965v1 — §4 evaluation and mutation analysis`；limitations/counterevidence=`arXiv:2605.23965v1 — §5 limitations: rule coverage, oracle and domain scope`。
<!-- claim:SF-LGMT-LOGIC-GROUNDED-METAMORPHIC-TESTING-FOR-EVALUATING-THE-REASONING-REL:start -->证据只支持 exact-v1 披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨部署的一般优势，也不把作者 benchmark 变成生产承诺。<!-- claim:SF-LGMT-LOGIC-GROUNDED-METAMORPHIC-TESTING-FOR-EVALUATING-THE-REASONING-REL:end -->
Books Decision=`No Change — Existing Coverage`。旧方案在新增约束不存在、证据越界或 fallback 被触发时继续成立。
<!-- review:SF-LGMT-LOGIC-GROUNDED-METAMORPHIC-TESTING-FOR-EVALUATING-THE-REASONING-REL:end -->

<!-- review:SF-STOP-COMPARING-LLM-AGENTS-WITHOUT-DISCLOSING-THE-HARNESS:start -->
#### Stop Comparing LLM Agents Without Disclosing the Harness

机制边界：Second, published benchmarks, industry deployments, and a controlled variance decomposition show that harness-induced variance can substantially exceed model-induced variance, including cases of model ranking reversal.。Method/identity locator：`https://arxiv.org/html/2605.23950v1 §2 Binding Constraint Thesis; §3 Control-Theoretic Model — mechanism: Second, published benchmarks, industry deployments, and a controlled variance decomposition show that harness-induced variance can substantially exceed model-induced variance, including cases of model ranking reversal.`；evaluation locator：`https://arxiv.org/html/2605.23950v1 §4 Variance Evidence; §5 Disclosure Protocol — disclosed evaluation scope only`；counterevidence/limitations：`https://arxiv.org/html/2605.23950v1 Position-paper evidence boundary; §6 Limitations — no generalization beyond disclosed workload/model/evaluator`；artifact locator：`https://arxiv.org/html/2605.23950v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-STOP-COMPARING-LLM-AGENTS-WITHOUT-DISCLOSING-THE-HARNESS:start -->结论只适用于 exact-v1 披露的模型、数据、硬件、并发和 evaluator；未披露条件一律为 Not Disclosed，不把作者 benchmark 外推为通用 SLO。<!-- claim:SF-STOP-COMPARING-LLM-AGENTS-WITHOUT-DISCLOSING-THE-HARNESS:end -->
旧方案在固定 workload、低风险或无需跨层协调时仍成立；本证据只改变所列 owner 的条件化设计判断。
<!-- review:SF-STOP-COMPARING-LLM-AGENTS-WITHOUT-DISCLOSING-THE-HARNESS:end -->

## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-23911 | exact-v1 evaluation for Cross-Platform Fused MoE Dispatch in Triton: Portable Expert Routing Without CUDA | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | paper authors |
| SF-2026-ARXIV-2605-23918 | exact-v1 evaluation for The Model Parking Tax: Quantifying the Hidden Energy Cost of Always-On GPU Model Deployment | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | paper authors |
| SF-2026-ARXIV-2605-23935 | exact-v1 evaluation for Operationalizing Reconstructive Authority: Runtime Construction, Dependency Resolution, and Execution Gating in Autonomous Agent Systems | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | paper authors |
| SF-2026-ARXIV-2605-23945 | §5 A40/H100 testbeds, Llama/Qwen with VeRL/SGLang | Not Disclosed in exact-v1; no inference made | Not Disclosed in exact-v1; no inference made | Not Disclosed in exact-v1; no inference made | Not Disclosed in exact-v1; no inference made | Not Disclosed in exact-v1; no inference made | Not Disclosed in exact-v1; no inference made | Not Disclosed in exact-v1; no inference made | Not Disclosed in exact-v1; no inference made | exact-v1 author evaluator described in §5 A40/H100 testbeds, Llama/Qwen with VeRL/SGLang |
| SF-2026-ARXIV-2605-25310 | exact-v1 evaluation for Tool-Call Dependency Structure is Linearly Decodable in LLM Agent Residual Streams | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | paper authors |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-23911 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-23911 |
| SF-2026-ARXIV-2605-23918 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-23918 |
| SF-2026-ARXIV-2605-23935 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-23935 |
| SF-2026-ARXIV-2605-23945 | score_7_9 | selected | DA-20260526-01 | — | Score=9/9 且属于当日最高跨系统设计影响；有限叙事预算不替代其余 Source Review。 | analysis:DA-20260526-01 |
| SF-2026-ARXIV-2605-23951 | score_7_9 | selected | DA-20260526-02 | — | Score=9/9 且属于当日最高跨系统设计影响；有限叙事预算不替代其余 Source Review。 | analysis:DA-20260526-02 |
| SF-2026-ARXIV-2605-23956 | score_7_9 | selected | DA-20260526-03 | — | Score=9/9 且属于当日最高跨系统设计影响；有限叙事预算不替代其余 Source Review。 | analysis:DA-20260526-03 |
| SF-2026-ARXIV-2605-23986 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-23986 |
| SF-2026-ARXIV-2605-23988 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-23988 |
| SF-2026-ARXIV-2605-23993 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-23993 |
| SF-2026-ARXIV-2605-24004 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24004 |
| SF-2026-ARXIV-2605-24006 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24006 |
| SF-2026-ARXIV-2605-24022 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24022 |
| SF-2026-ARXIV-2605-24036 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24036 |
| SF-2026-ARXIV-2605-24042 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24042 |
| SF-2026-ARXIV-2605-24044 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24044 |
| SF-2026-ARXIV-2605-24050 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24050 |
| SF-2026-ARXIV-2605-24060 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24060 |
| SF-2026-ARXIV-2605-24069 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24069 |
| SF-2026-ARXIV-2605-24117 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24117 |
| SF-2026-ARXIV-2605-24134 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24134 |
| SF-2026-ARXIV-2605-24154 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24154 |
| SF-2026-ARXIV-2605-24168 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24168 |
| SF-2026-ARXIV-2605-24183 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24183 |
| SF-2026-ARXIV-2605-24197 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24197 |
| SF-2026-ARXIV-2605-24202 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24202 |
| SF-2026-ARXIV-2605-24213 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24213 |
| SF-2026-ARXIV-2605-24216 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24216 |
| SF-2026-ARXIV-2605-24217 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24217 |
| SF-2026-ARXIV-2605-24219 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24219 |
| SF-2026-ARXIV-2605-24220 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24220 |
| SF-2026-ARXIV-2605-24229 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24229 |
| SF-2026-ARXIV-2605-24245 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24245 |
| SF-2026-ARXIV-2605-24247 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24247 |
| SF-2026-ARXIV-2605-24248 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24248 |
| SF-2026-ARXIV-2605-24259 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24259 |
| SF-2026-ARXIV-2605-24279 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24279 |
| SF-2026-ARXIV-2605-24286 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24286 |
| SF-2026-ARXIV-2605-24299 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24299 |
| SF-2026-ARXIV-2605-24309 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24309 |
| SF-2026-ARXIV-2605-24312 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24312 |
| SF-2026-ARXIV-2605-24326 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24326 |
| SF-2026-ARXIV-2605-24391 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24391 |
| SF-2026-ARXIV-2605-24420 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24420 |
| SF-2026-ARXIV-2605-24421 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24421 |
| SF-2026-ARXIV-2605-24425 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24425 |
| SF-2026-ARXIV-2605-24426 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24426 |
| SF-2026-ARXIV-2605-24461 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24461 |
| SF-2026-ARXIV-2605-24468 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24468 |
| SF-2026-ARXIV-2605-24517 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24517 |
| SF-2026-ARXIV-2605-24547 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24547 |
| SF-2026-ARXIV-2605-24558 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24558 |
| SF-2026-ARXIV-2605-24579 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24579 |
| SF-2026-ARXIV-2605-24583 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24583 |
| SF-2026-ARXIV-2605-24598 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24598 |
| SF-2026-ARXIV-2605-24614 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24614 |
| SF-2026-ARXIV-2605-24619 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24619 |
| SF-2026-ARXIV-2605-24657 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24657 |
| SF-2026-ARXIV-2605-24659 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24659 |
| SF-2026-ARXIV-2605-24660 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24660 |
| SF-2026-ARXIV-2605-24661 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24661 |
| SF-2026-ARXIV-2605-24662 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24662 |
| SF-2026-ARXIV-2605-24667 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24667 |
| SF-2026-ARXIV-2605-24683 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24683 |
| SF-2026-ARXIV-2605-24697 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24697 |
| SF-2026-ARXIV-2605-24709 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24709 |
| SF-2026-ARXIV-2605-24727 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24727 |
| SF-2026-ARXIV-2605-24728 | score_7_9;forced_review;potential_structural_gap | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24728 |
| SF-2026-ARXIV-2605-24733 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24733 |
| SF-2026-ARXIV-2605-24737 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24737 |
| SF-2026-ARXIV-2605-24743 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24743 |
| SF-2026-ARXIV-2605-24749 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24749 |
| SF-2026-ARXIV-2605-24756 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24756 |
| SF-2026-ARXIV-2605-24770 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24770 |
| SF-2026-ARXIV-2605-24775 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24775 |
| SF-2026-ARXIV-2605-24785 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24785 |
| SF-2026-ARXIV-2605-24786 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24786 |
| SF-2026-ARXIV-2605-24793 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24793 |
| SF-2026-ARXIV-2605-24817 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24817 |
| SF-2026-ARXIV-2605-24818 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24818 |
| SF-2026-ARXIV-2605-24823 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24823 |
| SF-2026-ARXIV-2605-24832 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24832 |
| SF-2026-ARXIV-2605-24870 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24870 |
| SF-2026-ARXIV-2605-24879 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24879 |
| SF-2026-ARXIV-2605-24883 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24883 |
| SF-2026-ARXIV-2605-24892 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24892 |
| SF-2026-ARXIV-2605-24914 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24914 |
| SF-2026-ARXIV-2605-24922 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24922 |
| SF-2026-ARXIV-2605-24930 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24930 |
| SF-2026-ARXIV-2605-24941 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24941 |
| SF-2026-ARXIV-2605-24973 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-24973 |
| SF-2026-ARXIV-2605-25002 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-25002 |
| SF-2026-ARXIV-2605-25052 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-25052 |
| SF-2026-ARXIV-2605-25073 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-25073 |
| SF-2026-ARXIV-2605-25077 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-25077 |
| SF-2026-ARXIV-2605-25085 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-25085 |
| SF-2026-ARXIV-2605-25092 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-25092 |
| SF-2026-ARXIV-2605-25133 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-25133 |
| SF-2026-ARXIV-2605-25160 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-25160 |
| SF-2026-ARXIV-2605-25188 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-25188 |
| SF-2026-ARXIV-2605-25189 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-25189 |
| SF-2026-ARXIV-2605-25233 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-25233 |
| SF-2026-ARXIV-2605-25240 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-25240 |
| SF-2026-ARXIV-2605-25244 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-25244 |
| SF-2026-ARXIV-2605-25247 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-25247 |
| SF-2026-ARXIV-2605-25252 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-25252 |
| SF-2026-ARXIV-2605-25272 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-25272 |
| SF-2026-ARXIV-2605-25284 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-25284 |
| SF-2026-ARXIV-2605-25292 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-25292 |
| SF-2026-ARXIV-2605-25298 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-25298 |
| SF-2026-ARXIV-2605-25313 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-25313 |
| SF-2026-ARXIV-2605-25338 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-25338 |
| SF-2026-ARXIV-2605-25375 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-25375 |
| SF-2026-ARXIV-2605-25376 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-25376 |
| SF-2026-ARXIV-2605-25379 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-25379 |
| SF-2026-ARXIV-2605-25389 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-25389 |
| SF-2026-ARXIV-2605-25421 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-25421 |
| SF-2026-ARXIV-2605-25422 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-25422 |
| SF-2026-ARXIV-2605-25424 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-25424 |
| SF-2026-ARXIV-2605-25430 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-25430 |
| SF-2026-ARXIV-2605-25451 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-25451 |
| SF-2026-ARXIV-2605-25475 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-25475 |
| SF-2026-ARXIV-2605-25492 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-25492 |
| SF-2026-ARXIV-2605-25507 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-25507 |
| SF-2026-ARXIV-2605-25521 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-25521 |
| SF-2026-ARXIV-2605-25535 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-25535 |
| SF-2026-ARXIV-2605-25537 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-25537 |
| SF-2026-ARXIV-2605-25547 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-25547 |
| SF-2026-ARXIV-2605-25550 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-25550 |
| SF-2026-ARXIV-2605-25621 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-25621 |
| SF-2026-ARXIV-2605-25624 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-25624 |
| SF-2026-ARXIV-2605-25632 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-25632 |
| SF-2026-ARXIV-2605-25641 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-25641 |
| SF-2026-ARXIV-2605-25653 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-25653 |
| SF-2026-ARXIV-2605-25655 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-25655 |
| SF-2026-ARXIV-2605-25673 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-25673 |
| SF-2026-ARXIV-2605-25674 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-25674 |
| SF-2026-ARXIV-2605-25682 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-25682 |
| SF-2026-ARXIV-2605-25698 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-25698 |
| SF-2026-ARXIV-2605-25707 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-25707 |
| SF-2026-ARXIV-2605-25716 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-25716 |
| SF-2026-ARXIV-2605-25745 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-25745 |
| SF-2026-ARXIV-2605-25746 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-25746 |
| SF-2026-ARXIV-2605-25798 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-25798 |
| SF-2026-ARXIV-2605-25815 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-25815 |
| SF-2026-ARXIV-2605-25819 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-25819 |
| SF-2026-ARXIV-2605-25820 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-25820 |
| SF-2026-ARXIV-2605-25831 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-25831 |
| SF-2026-ARXIV-2605-25854 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-25854 |
| SF-2026-ARXIV-2605-25869 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-25869 |
| SF-2026-ARXIV-2605-25874 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-25874 |
| SF-2026-ARXIV-2605-25889 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-25889 |
| SF-2026-ARXIV-2605-25893 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-25893 |
| SF-2026-ARXIV-2605-25966 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-25966 |
| SF-2026-ARXIV-2605-25971 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-25971 |
| SF-2026-ARXIV-2605-25988 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-25988 |
| SF-2026-ARXIV-2605-25997 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-25997 |
| SF-2026-ARXIV-2605-26029 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-26029 |
| SF-2026-ARXIV-2605-26037 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-26037 |
| SF-2026-ARXIV-2605-26045 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-26045 |
| SF-2026-ARXIV-2605-26046 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-26046 |
| SF-2026-ARXIV-2605-26047 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-26047 |
| SF-2026-ARXIV-2605-26079 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-26079 |
| SF-2026-ARXIV-2605-26110 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-26110 |
| SF-2026-ARXIV-2605-26112 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-26112 |
| SF-2026-ARXIV-2605-26114 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-26114 |
| SF-AERIC-ANTICIPATORY-HIDDEN-STATE-MONITORING-FOR-IMPLICIT-HARMFUL-DIALOGUE | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-AERIC-ANTICIPATORY-HIDDEN-STATE-MONITORING-FOR-IMPLICIT-HARMFUL-DIALOGUE |
| SF-FAITHFUL-OR-FABRICATED-A-CAUSAL-FRAMEWORK-FOR-RATIONALIZATION-BIAS-IN-LL | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-FAITHFUL-OR-FABRICATED-A-CAUSAL-FRAMEWORK-FOR-RATIONALIZATION-BIAS-IN-LL |
| SF-LGMT-LOGIC-GROUNDED-METAMORPHIC-TESTING-FOR-EVALUATING-THE-REASONING-REL | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-LGMT-LOGIC-GROUNDED-METAMORPHIC-TESTING-FOR-EVALUATING-THE-REASONING-REL |
| SF-STOP-COMPARING-LLM-AGENTS-WITHOUT-DISCLOSING-THE-HARNESS | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-STOP-COMPARING-LLM-AGENTS-WITHOUT-DISCLOSING-THE-HARNESS |

<!-- analysis-decision:SF-2026-ARXIV-2605-23911:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-23911:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-23918:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-23918:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-23935:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-23935:end -->

<!-- analysis:DA-20260526-01:start -->
### Deep Analysis — SF-2026-ARXIV-2605-23945

该 family 的 Score V2=9/9；Source Review 已闭合问题、旧路径、机制 owner、evaluation boundary、trade-off 与共存条件。Deep Analysis 只提升叙事优先级，不改变 Evidence Gate。
<!-- analysis:DA-20260526-01:end -->

<!-- analysis:DA-20260526-02:start -->
### Deep Analysis — SF-2026-ARXIV-2605-23951

该 family 的 Score V2=9/9；Source Review 已闭合问题、旧路径、机制 owner、evaluation boundary、trade-off 与共存条件。Deep Analysis 只提升叙事优先级，不改变 Evidence Gate。
<!-- analysis:DA-20260526-02:end -->

<!-- analysis:DA-20260526-03:start -->
### Deep Analysis — SF-2026-ARXIV-2605-23956

该 family 的 Score V2=9/9；Source Review 已闭合问题、旧路径、机制 owner、evaluation boundary、trade-off 与共存条件。Deep Analysis 只提升叙事优先级，不改变 Evidence Gate。
<!-- analysis:DA-20260526-03:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-23986:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-23986:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-23988:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-23988:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-23993:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-23993:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24004:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24004:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24006:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24006:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24022:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24022:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24036:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24036:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24042:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24042:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24044:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24044:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24050:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24050:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24060:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24060:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24069:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24069:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24117:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24117:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24134:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24134:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24154:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24154:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24168:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24168:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24183:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24183:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24197:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24197:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24202:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24202:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24213:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24213:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24216:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24216:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24217:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24217:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24219:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24219:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24220:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24220:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24229:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24229:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24245:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24245:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24247:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24247:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24248:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24248:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24259:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24259:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24279:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24279:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24286:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24286:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24299:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24299:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24309:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24309:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24312:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24312:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24326:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24326:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24391:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24391:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24420:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24420:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24421:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24421:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24425:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24425:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24426:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24426:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24461:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24461:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24468:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24468:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24517:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24517:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24547:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24547:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24558:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24558:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24579:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24579:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24583:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24583:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24598:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24598:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24614:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24614:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24619:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24619:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24657:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24657:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24659:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24659:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24660:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24660:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24661:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24661:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24662:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24662:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24667:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24667:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24683:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24683:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24697:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24697:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24709:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24709:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24727:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24727:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24728:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24728:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24733:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24733:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24737:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24737:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24743:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24743:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24749:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24749:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24756:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24756:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24770:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24770:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24775:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24775:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24785:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24785:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24786:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24786:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24793:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24793:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24817:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24817:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24818:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24818:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24823:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24823:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24832:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24832:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24870:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24870:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24879:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24879:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24883:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24883:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24892:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24892:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24914:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24914:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24922:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24922:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24930:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24930:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24941:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24941:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-24973:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-24973:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-25002:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-25002:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-25052:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-25052:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-25073:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-25073:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-25077:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-25077:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-25085:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-25085:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-25092:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-25092:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-25133:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-25133:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-25160:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-25160:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-25188:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-25188:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-25189:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-25189:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-25233:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-25233:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-25240:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-25240:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-25244:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-25244:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-25247:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-25247:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-25252:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-25252:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-25272:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-25272:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-25284:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-25284:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-25292:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-25292:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-25298:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-25298:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-25313:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-25313:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-25338:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-25338:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-25375:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-25375:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-25376:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-25376:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-25379:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-25379:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-25389:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-25389:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-25421:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-25421:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-25422:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-25422:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-25424:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-25424:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-25430:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-25430:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-25451:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-25451:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-25475:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-25475:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-25492:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-25492:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-25507:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-25507:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-25521:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-25521:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-25535:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-25535:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-25537:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-25537:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-25547:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-25547:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-25550:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-25550:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-25621:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-25621:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-25624:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-25624:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-25632:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-25632:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-25641:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-25641:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-25653:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-25653:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-25655:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-25655:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-25673:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-25673:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-25674:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-25674:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-25682:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-25682:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-25698:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-25698:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-25707:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-25707:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-25716:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-25716:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-25745:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-25745:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-25746:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-25746:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-25798:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-25798:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-25815:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-25815:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-25819:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-25819:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-25820:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-25820:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-25831:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-25831:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-25854:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-25854:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-25869:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-25869:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-25874:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-25874:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-25889:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-25889:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-25893:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-25893:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-25966:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-25966:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-25971:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-25971:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-25988:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-25988:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-25997:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-25997:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-26029:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-26029:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-26037:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-26037:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-26045:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-26045:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-26046:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-26046:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-26047:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-26047:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-26079:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-26079:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-26110:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-26110:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-26112:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-26112:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-26114:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-26114:end -->

<!-- analysis-decision:SF-AERIC-ANTICIPATORY-HIDDEN-STATE-MONITORING-FOR-IMPLICIT-HARMFUL-DIALOGUE:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-AERIC-ANTICIPATORY-HIDDEN-STATE-MONITORING-FOR-IMPLICIT-HARMFUL-DIALOGUE:end -->

<!-- analysis-decision:SF-FAITHFUL-OR-FABRICATED-A-CAUSAL-FRAMEWORK-FOR-RATIONALIZATION-BIAS-IN-LL:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-FAITHFUL-OR-FABRICATED-A-CAUSAL-FRAMEWORK-FOR-RATIONALIZATION-BIAS-IN-LL:end -->

<!-- analysis-decision:SF-LGMT-LOGIC-GROUNDED-METAMORPHIC-TESTING-FOR-EVALUATING-THE-REASONING-REL:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-LGMT-LOGIC-GROUNDED-METAMORPHIC-TESTING-FOR-EVALUATING-THE-REASONING-REL:end -->

<!-- analysis-decision:SF-STOP-COMPARING-LLM-AGENTS-WITHOUT-DISCLOSING-THE-HARNESS:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-STOP-COMPARING-LLM-AGENTS-WITHOUT-DISCLOSING-THE-HARNESS:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-23911 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#L53 (H3: Execution Plan 可以修订，但只能在安全边界 Commit) | books/part-05-inference-system/48-speculative-decoding.md#L10 (H2: 本章要回答的问题); books/part-05-inference-system/50-vllm.md#L10 (H2: 本章要回答的问题) | existing:SF-2026-ARXIV-2605-23911 | delta:SF-2026-ARXIV-2605-23911 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23911 |
| SF-2026-ARXIV-2605-23918 | PLATFORM-COST | books/part-06-ai-infrastructure/70-cost.md#L16 (H2: 资源时间是共同底座) | books/part-06-ai-infrastructure/69-trace.md#L10 (H2: 本章要回答的问题); books/part-06-ai-infrastructure/71-multi-tenant.md#L10 (H2: 本章要回答的问题) | existing:SF-2026-ARXIV-2605-23918 | delta:SF-2026-ARXIV-2605-23918 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23918 |
| SF-2026-ARXIV-2605-23935 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L29 (H2: 生命周期威胁) | books/part-06-ai-infrastructure/71-multi-tenant.md#L10 (H2: 本章要回答的问题); books/part-06-ai-infrastructure/73-production-best-practice.md#L10 (H2: 本章要回答的问题) | existing:SF-2026-ARXIV-2605-23935 | delta:SF-2026-ARXIV-2605-23935 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23935 |
| SF-2026-ARXIV-2605-23945 | TRAIN-TENSOR-PARALLEL | books/part-04-training-system/37-tensor-parallel.md#L1 | books/part-04-training-system/36-distributed-training.md#L1; books/part-04-training-system/38-pipeline-parallel.md#L1 | existing:SF-2026-ARXIV-2605-23945 | delta:SF-2026-ARXIV-2605-23945 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23945 |
| SF-2026-ARXIV-2605-23951 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-23951 | delta:SF-2026-ARXIV-2605-23951 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23951 |
| SF-2026-ARXIV-2605-23956 | WORLDVIEW-SYSTEM-EVOLUTION | books/part-01-worldview/09-ai-system-evolution.md#chapter-09 | books/part-01-worldview/08-why-llms-show-intelligence.md#chapter-08; books/part-01-worldview/10-future-of-ai.md#chapter-10 | existing:SF-2026-ARXIV-2605-23956 | delta:SF-2026-ARXIV-2605-23956 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23956 |
| SF-2026-ARXIV-2605-23986 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76; books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-23986 | delta:SF-2026-ARXIV-2605-23986 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-23986 |
| SF-2026-ARXIV-2605-23988 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#chapter-36 | books/part-04-training-system/35-checkpoint.md#chapter-35; books/part-04-training-system/37-tensor-parallel.md#chapter-37 | existing:SF-2026-ARXIV-2605-23988 | delta:SF-2026-ARXIV-2605-23988 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-23988 |
| SF-2026-ARXIV-2605-23993 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24; books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | existing:SF-2026-ARXIV-2605-23993 | delta:SF-2026-ARXIV-2605-23993 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23993 |
| SF-2026-ARXIV-2605-24004 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | existing:SF-2026-ARXIV-2605-24004 | delta:SF-2026-ARXIV-2605-24004 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24004 |
| SF-2026-ARXIV-2605-24006 | TRAIN-PIPELINE-PARALLEL | books/part-04-training-system/38-pipeline-parallel.md#chapter-38 | books/part-04-training-system/37-tensor-parallel.md#chapter-37;books/part-04-training-system/39-zero.md#chapter-39 | existing:SF-2026-ARXIV-2605-24006 | delta:SF-2026-ARXIV-2605-24006 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24006 |
| SF-2026-ARXIV-2605-24022 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#chapter-45 | books/part-05-inference-system/44-decode.md#chapter-44;books/part-05-inference-system/46-continuous-batching.md#chapter-46 | existing:SF-2026-ARXIV-2605-24022 | delta:SF-2026-ARXIV-2605-24022 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24022 |
| SF-2026-ARXIV-2605-24036 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-24036 | delta:SF-2026-ARXIV-2605-24036 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24036 |
| SF-2026-ARXIV-2605-24042 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-24042 | delta:SF-2026-ARXIV-2605-24042 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24042 |
| SF-2026-ARXIV-2605-24044 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#chapter-56 | books/part-05-inference-system/55-pd-disaggregation.md#chapter-55 | existing:SF-2026-ARXIV-2605-24044 | delta:SF-2026-ARXIV-2605-24044 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24044 |
| SF-2026-ARXIV-2605-24050 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-24050 | delta:SF-2026-ARXIV-2605-24050 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24050 |
| SF-2026-ARXIV-2605-24060 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-24060 | delta:SF-2026-ARXIV-2605-24060 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24060 |
| SF-2026-ARXIV-2605-24069 | AGENT-MCP | books/part-07-agent/83-mcp.md#chapter-83 | books/part-07-agent/82-multi-agent.md#chapter-82;books/part-07-agent/84-agent-platform.md#chapter-84 | existing:SF-2026-ARXIV-2605-24069 | delta:SF-2026-ARXIV-2605-24069 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24069 |
| SF-2026-ARXIV-2605-24117 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-24117 | delta:SF-2026-ARXIV-2605-24117 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24117 |
| SF-2026-ARXIV-2605-24134 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-24134 | delta:SF-2026-ARXIV-2605-24134 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24134 |
| SF-2026-ARXIV-2605-24154 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-24154 | delta:SF-2026-ARXIV-2605-24154 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24154 |
| SF-2026-ARXIV-2605-24168 | AGENT-CONTEXT | books/part-07-agent/75-context.md#chapter-75 | books/part-07-agent/74-prompt.md#chapter-74;books/part-07-agent/76-rag.md#chapter-76 | existing:SF-2026-ARXIV-2605-24168 | delta:SF-2026-ARXIV-2605-24168 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24168 |
| SF-2026-ARXIV-2605-24183 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-24183 | delta:SF-2026-ARXIV-2605-24183 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24183 |
| SF-2026-ARXIV-2605-24197 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#chapter-82 | books/part-07-agent/81-workflow.md#chapter-81;books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-24197 | delta:SF-2026-ARXIV-2605-24197 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24197 |
| SF-2026-ARXIV-2605-24202 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#chapter-31 | books/part-04-training-system/30-lora.md#chapter-30;books/part-04-training-system/32-ppo.md#chapter-32 | existing:SF-2026-ARXIV-2605-24202 | delta:SF-2026-ARXIV-2605-24202 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24202 |
| SF-2026-ARXIV-2605-24213 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-24213 | delta:SF-2026-ARXIV-2605-24213 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24213 |
| SF-2026-ARXIV-2605-24216 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-24216 | delta:SF-2026-ARXIV-2605-24216 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24216 |
| SF-2026-ARXIV-2605-24217 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-24217 | delta:SF-2026-ARXIV-2605-24217 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24217 |
| SF-2026-ARXIV-2605-24219 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-24219 | delta:SF-2026-ARXIV-2605-24219 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24219 |
| SF-2026-ARXIV-2605-24220 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#chapter-31 | books/part-04-training-system/30-lora.md#chapter-30;books/part-04-training-system/32-ppo.md#chapter-32 | existing:SF-2026-ARXIV-2605-24220 | delta:SF-2026-ARXIV-2605-24220 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24220 |
| SF-2026-ARXIV-2605-24229 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-24229 | delta:SF-2026-ARXIV-2605-24229 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24229 |
| SF-2026-ARXIV-2605-24245 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-24245 | delta:SF-2026-ARXIV-2605-24245 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24245 |
| SF-2026-ARXIV-2605-24247 | TRAIN-DATA | books/part-04-training-system/27-data.md#chapter-27 | books/part-04-training-system/28-pretraining.md#chapter-28 | existing:SF-2026-ARXIV-2605-24247 | delta:SF-2026-ARXIV-2605-24247 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24247 |
| SF-2026-ARXIV-2605-24248 | AGENT-MCP | books/part-07-agent/83-mcp.md#chapter-83 | books/part-07-agent/82-multi-agent.md#chapter-82;books/part-07-agent/84-agent-platform.md#chapter-84 | existing:SF-2026-ARXIV-2605-24248 | delta:SF-2026-ARXIV-2605-24248 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24248 |
| SF-2026-ARXIV-2605-24259 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#chapter-45 | books/part-05-inference-system/44-decode.md#chapter-44;books/part-05-inference-system/46-continuous-batching.md#chapter-46 | existing:SF-2026-ARXIV-2605-24259 | delta:SF-2026-ARXIV-2605-24259 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24259 |
| SF-2026-ARXIV-2605-24279 | AGENT-CONTEXT | books/part-07-agent/75-context.md#chapter-75 | books/part-07-agent/74-prompt.md#chapter-74;books/part-07-agent/76-rag.md#chapter-76 | existing:SF-2026-ARXIV-2605-24279 | delta:SF-2026-ARXIV-2605-24279 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24279 |
| SF-2026-ARXIV-2605-24286 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-24286 | delta:SF-2026-ARXIV-2605-24286 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24286 |
| SF-2026-ARXIV-2605-24299 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-24299 | delta:SF-2026-ARXIV-2605-24299 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24299 |
| SF-2026-ARXIV-2605-24309 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-24309 | delta:SF-2026-ARXIV-2605-24309 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24309 |
| SF-2026-ARXIV-2605-24312 | AGENT-RAG | books/part-07-agent/76-rag.md#chapter-76 | books/part-07-agent/75-context.md#chapter-75;books/part-07-agent/77-memory.md#chapter-77 | existing:SF-2026-ARXIV-2605-24312 | delta:SF-2026-ARXIV-2605-24312 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24312 |
| SF-2026-ARXIV-2605-24326 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#chapter-36 | books/part-04-training-system/35-checkpoint.md#chapter-35;books/part-04-training-system/37-tensor-parallel.md#chapter-37 | existing:SF-2026-ARXIV-2605-24326 | delta:SF-2026-ARXIV-2605-24326 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24326 |
| SF-2026-ARXIV-2605-24391 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | books/part-05-inference-system/48-speculative-decoding.md#chapter-48;books/part-05-inference-system/50-vllm.md#chapter-50 | existing:SF-2026-ARXIV-2605-24391 | delta:SF-2026-ARXIV-2605-24391 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24391 |
| SF-2026-ARXIV-2605-24420 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-24420 | delta:SF-2026-ARXIV-2605-24420 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24420 |
| SF-2026-ARXIV-2605-24421 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-24421 | delta:SF-2026-ARXIV-2605-24421 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24421 |
| SF-2026-ARXIV-2605-24425 | MODEL-TRANSFORMER-LAYER | books/part-02-model/17-transformer-layer.md#chapter-17 | books/part-02-model/16-feed-forward-mlp.md#chapter-16;books/part-02-model/18-decoder-only.md#chapter-18 | existing:SF-2026-ARXIV-2605-24425 | delta:SF-2026-ARXIV-2605-24425 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24425 |
| SF-2026-ARXIV-2605-24426 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#chapter-31 | books/part-04-training-system/30-lora.md#chapter-30;books/part-04-training-system/32-ppo.md#chapter-32 | existing:SF-2026-ARXIV-2605-24426 | delta:SF-2026-ARXIV-2605-24426 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24426 |
| SF-2026-ARXIV-2605-24461 | PLATFORM-GPU-SCHEDULER | books/part-06-ai-infrastructure/63-gpu-scheduler.md#chapter-63 | books/part-06-ai-infrastructure/62-gateway.md#chapter-62;books/part-06-ai-infrastructure/64-volcano.md#chapter-64 | existing:SF-2026-ARXIV-2605-24461 | delta:SF-2026-ARXIV-2605-24461 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24461 |
| SF-2026-ARXIV-2605-24468 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76;books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-24468 | delta:SF-2026-ARXIV-2605-24468 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24468 |
| SF-2026-ARXIV-2605-24517 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24;books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | existing:SF-2026-ARXIV-2605-24517 | delta:SF-2026-ARXIV-2605-24517 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24517 |
| SF-2026-ARXIV-2605-24547 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#chapter-31 | books/part-04-training-system/30-lora.md#chapter-30;books/part-04-training-system/32-ppo.md#chapter-32 | existing:SF-2026-ARXIV-2605-24547 | delta:SF-2026-ARXIV-2605-24547 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24547 |
| SF-2026-ARXIV-2605-24558 | TRAIN-DATA | books/part-04-training-system/27-data.md#chapter-27 | books/part-04-training-system/28-pretraining.md#chapter-28 | existing:SF-2026-ARXIV-2605-24558 | delta:SF-2026-ARXIV-2605-24558 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24558 |
| SF-2026-ARXIV-2605-24579 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76;books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-24579 | delta:SF-2026-ARXIV-2605-24579 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24579 |
| SF-2026-ARXIV-2605-24583 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-24583 | delta:SF-2026-ARXIV-2605-24583 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24583 |
| SF-2026-ARXIV-2605-24598 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#chapter-82 | books/part-07-agent/81-workflow.md#chapter-81;books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-24598 | delta:SF-2026-ARXIV-2605-24598 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24598 |
| SF-2026-ARXIV-2605-24614 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-24614 | delta:SF-2026-ARXIV-2605-24614 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24614 |
| SF-2026-ARXIV-2605-24619 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-24619 | delta:SF-2026-ARXIV-2605-24619 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24619 |
| SF-2026-ARXIV-2605-24657 | AGENT-CONTEXT | books/part-07-agent/75-context.md#chapter-75 | books/part-07-agent/74-prompt.md#chapter-74;books/part-07-agent/76-rag.md#chapter-76 | existing:SF-2026-ARXIV-2605-24657 | delta:SF-2026-ARXIV-2605-24657 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24657 |
| SF-2026-ARXIV-2605-24659 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-24659 | delta:SF-2026-ARXIV-2605-24659 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24659 |
| SF-2026-ARXIV-2605-24660 | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#chapter-78 | books/part-07-agent/77-memory.md#chapter-77;books/part-07-agent/79-planning.md#chapter-79 | existing:SF-2026-ARXIV-2605-24660 | delta:SF-2026-ARXIV-2605-24660 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24660 |
| SF-2026-ARXIV-2605-24661 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-24661 | delta:SF-2026-ARXIV-2605-24661 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24661 |
| SF-2026-ARXIV-2605-24662 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-24662 | delta:SF-2026-ARXIV-2605-24662 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24662 |
| SF-2026-ARXIV-2605-24667 | TRAIN-PRETRAINING | books/part-04-training-system/28-pretraining.md#chapter-28 | books/part-04-training-system/27-data.md#chapter-27;books/part-04-training-system/29-sft.md#chapter-29 | existing:SF-2026-ARXIV-2605-24667 | delta:SF-2026-ARXIV-2605-24667 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24667 |
| SF-2026-ARXIV-2605-24683 | PLATFORM-MONITORING | books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66;books/part-06-ai-infrastructure/68-logging.md#chapter-68 | existing:SF-2026-ARXIV-2605-24683 | delta:SF-2026-ARXIV-2605-24683 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24683 |
| SF-2026-ARXIV-2605-24697 | MULTIMODAL-GENERATIVE-PARADIGMS | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24 | books/part-03-multimodal-world-models/23-multimodal-representation.md#chapter-23;books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | existing:SF-2026-ARXIV-2605-24697 | delta:SF-2026-ARXIV-2605-24697 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24697 |
| SF-2026-ARXIV-2605-24709 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#chapter-31 | books/part-04-training-system/30-lora.md#chapter-30;books/part-04-training-system/32-ppo.md#chapter-32 | existing:SF-2026-ARXIV-2605-24709 | delta:SF-2026-ARXIV-2605-24709 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24709 |
| SF-2026-ARXIV-2605-24727 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-24727 | delta:SF-2026-ARXIV-2605-24727 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24727 |
| SF-2026-ARXIV-2605-24728 | considered:MULTIMODAL-EMBODIED-VLA,AGENT-WORKFLOW | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | existing:SF-2026-ARXIV-2605-24728 | delta:SF-2026-ARXIV-2605-24728 | Layering / Dependency | Structural Candidate | books-review:SF-2026-ARXIV-2605-24728 |
| SF-2026-ARXIV-2605-24733 | AGENT-REFLECTION | books/part-07-agent/80-reflection.md#chapter-80 | books/part-07-agent/79-planning.md#chapter-79;books/part-07-agent/81-workflow.md#chapter-81 | existing:SF-2026-ARXIV-2605-24733 | delta:SF-2026-ARXIV-2605-24733 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24733 |
| SF-2026-ARXIV-2605-24737 | PLATFORM-MONITORING | books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66;books/part-06-ai-infrastructure/68-logging.md#chapter-68 | existing:SF-2026-ARXIV-2605-24737 | delta:SF-2026-ARXIV-2605-24737 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24737 |
| SF-2026-ARXIV-2605-24743 | TRAIN-DATA | books/part-04-training-system/27-data.md#chapter-27 | books/part-04-training-system/28-pretraining.md#chapter-28 | existing:SF-2026-ARXIV-2605-24743 | delta:SF-2026-ARXIV-2605-24743 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24743 |
| SF-2026-ARXIV-2605-24749 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#chapter-31 | books/part-04-training-system/30-lora.md#chapter-30;books/part-04-training-system/32-ppo.md#chapter-32 | existing:SF-2026-ARXIV-2605-24749 | delta:SF-2026-ARXIV-2605-24749 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24749 |
| SF-2026-ARXIV-2605-24756 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-24756 | delta:SF-2026-ARXIV-2605-24756 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24756 |
| SF-2026-ARXIV-2605-24770 | TRAIN-PRETRAINING | books/part-04-training-system/28-pretraining.md#chapter-28 | books/part-04-training-system/27-data.md#chapter-27;books/part-04-training-system/29-sft.md#chapter-29 | existing:SF-2026-ARXIV-2605-24770 | delta:SF-2026-ARXIV-2605-24770 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24770 |
| SF-2026-ARXIV-2605-24775 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#chapter-82 | books/part-07-agent/81-workflow.md#chapter-81;books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-24775 | delta:SF-2026-ARXIV-2605-24775 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24775 |
| SF-2026-ARXIV-2605-24785 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-24785 | delta:SF-2026-ARXIV-2605-24785 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24785 |
| SF-2026-ARXIV-2605-24786 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#chapter-45 | books/part-05-inference-system/44-decode.md#chapter-44;books/part-05-inference-system/46-continuous-batching.md#chapter-46 | existing:SF-2026-ARXIV-2605-24786 | delta:SF-2026-ARXIV-2605-24786 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24786 |
| SF-2026-ARXIV-2605-24793 | INFER-SPECULATIVE-DECODING | books/part-05-inference-system/48-speculative-decoding.md#chapter-48 | books/part-05-inference-system/47-pagedattention.md#chapter-47;books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | existing:SF-2026-ARXIV-2605-24793 | delta:SF-2026-ARXIV-2605-24793 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24793 |
| SF-2026-ARXIV-2605-24817 | PLATFORM-MONITORING | books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66;books/part-06-ai-infrastructure/68-logging.md#chapter-68 | existing:SF-2026-ARXIV-2605-24817 | delta:SF-2026-ARXIV-2605-24817 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24817 |
| SF-2026-ARXIV-2605-24818 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-24818 | delta:SF-2026-ARXIV-2605-24818 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24818 |
| SF-2026-ARXIV-2605-24823 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83;books/part-07-agent/README.md#knowledge-tree | existing:SF-2026-ARXIV-2605-24823 | delta:SF-2026-ARXIV-2605-24823 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24823 |
| SF-2026-ARXIV-2605-24832 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | books/part-05-inference-system/48-speculative-decoding.md#chapter-48;books/part-05-inference-system/50-vllm.md#chapter-50 | existing:SF-2026-ARXIV-2605-24832 | delta:SF-2026-ARXIV-2605-24832 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24832 |
| SF-2026-ARXIV-2605-24870 | MULTIMODAL-GENERATIVE-PARADIGMS | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24 | books/part-03-multimodal-world-models/23-multimodal-representation.md#chapter-23;books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | existing:SF-2026-ARXIV-2605-24870 | delta:SF-2026-ARXIV-2605-24870 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24870 |
| SF-2026-ARXIV-2605-24879 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-24879 | delta:SF-2026-ARXIV-2605-24879 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24879 |
| SF-2026-ARXIV-2605-24883 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-24883 | delta:SF-2026-ARXIV-2605-24883 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24883 |
| SF-2026-ARXIV-2605-24892 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24;books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | existing:SF-2026-ARXIV-2605-24892 | delta:SF-2026-ARXIV-2605-24892 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24892 |
| SF-2026-ARXIV-2605-24914 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#chapter-45 | books/part-05-inference-system/44-decode.md#chapter-44;books/part-05-inference-system/46-continuous-batching.md#chapter-46 | existing:SF-2026-ARXIV-2605-24914 | delta:SF-2026-ARXIV-2605-24914 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24914 |
| SF-2026-ARXIV-2605-24922 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25;books/part-03-multimodal-world-models/README.md#knowledge-tree | existing:SF-2026-ARXIV-2605-24922 | delta:SF-2026-ARXIV-2605-24922 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24922 |
| SF-2026-ARXIV-2605-24930 | MODEL-LONG-CONTEXT | books/part-02-model/22-long-context.md#chapter-22 | books/part-02-model/21-moe.md#chapter-21;books/part-03-multimodal-world-models/README.md#knowledge-tree | existing:SF-2026-ARXIV-2605-24930 | delta:SF-2026-ARXIV-2605-24930 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24930 |
| SF-2026-ARXIV-2605-24941 | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#chapter-78 | books/part-07-agent/77-memory.md#chapter-77;books/part-07-agent/79-planning.md#chapter-79 | existing:SF-2026-ARXIV-2605-24941 | delta:SF-2026-ARXIV-2605-24941 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24941 |
| SF-2026-ARXIV-2605-24973 | AGENT-RAG | books/part-07-agent/76-rag.md#chapter-76 | books/part-07-agent/75-context.md#chapter-75;books/part-07-agent/77-memory.md#chapter-77 | existing:SF-2026-ARXIV-2605-24973 | delta:SF-2026-ARXIV-2605-24973 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24973 |
| SF-2026-ARXIV-2605-25002 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76;books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-25002 | delta:SF-2026-ARXIV-2605-25002 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-25002 |
| SF-2026-ARXIV-2605-25052 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-25052 | delta:SF-2026-ARXIV-2605-25052 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25052 |
| SF-2026-ARXIV-2605-25073 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-25073 | delta:SF-2026-ARXIV-2605-25073 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25073 |
| SF-2026-ARXIV-2605-25077 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24;books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | existing:SF-2026-ARXIV-2605-25077 | delta:SF-2026-ARXIV-2605-25077 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25077 |
| SF-2026-ARXIV-2605-25085 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#chapter-45 | books/part-05-inference-system/44-decode.md#chapter-44;books/part-05-inference-system/46-continuous-batching.md#chapter-46 | existing:SF-2026-ARXIV-2605-25085 | delta:SF-2026-ARXIV-2605-25085 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-25085 |
| SF-2026-ARXIV-2605-25092 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76;books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-25092 | delta:SF-2026-ARXIV-2605-25092 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25092 |
| SF-2026-ARXIV-2605-25133 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-25133 | delta:SF-2026-ARXIV-2605-25133 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25133 |
| SF-2026-ARXIV-2605-25160 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-25160 | delta:SF-2026-ARXIV-2605-25160 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25160 |
| SF-2026-ARXIV-2605-25188 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#chapter-82 | books/part-07-agent/81-workflow.md#chapter-81;books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-25188 | delta:SF-2026-ARXIV-2605-25188 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25188 |
| SF-2026-ARXIV-2605-25189 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#chapter-31 | books/part-04-training-system/30-lora.md#chapter-30;books/part-04-training-system/32-ppo.md#chapter-32 | existing:SF-2026-ARXIV-2605-25189 | delta:SF-2026-ARXIV-2605-25189 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-25189 |
| SF-2026-ARXIV-2605-25233 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#chapter-82 | books/part-07-agent/81-workflow.md#chapter-81;books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-25233 | delta:SF-2026-ARXIV-2605-25233 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25233 |
| SF-2026-ARXIV-2605-25240 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-25240 | delta:SF-2026-ARXIV-2605-25240 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-25240 |
| SF-2026-ARXIV-2605-25244 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#chapter-56 | books/part-05-inference-system/55-pd-disaggregation.md#chapter-55;books/part-05-inference-system/README.md#knowledge-tree | existing:SF-2026-ARXIV-2605-25244 | delta:SF-2026-ARXIV-2605-25244 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25244 |
| SF-2026-ARXIV-2605-25247 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#chapter-56 | books/part-05-inference-system/55-pd-disaggregation.md#chapter-55;books/part-05-inference-system/README.md#knowledge-tree | existing:SF-2026-ARXIV-2605-25247 | delta:SF-2026-ARXIV-2605-25247 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25247 |
| SF-2026-ARXIV-2605-25252 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#chapter-31 | books/part-04-training-system/30-lora.md#chapter-30;books/part-04-training-system/32-ppo.md#chapter-32 | existing:SF-2026-ARXIV-2605-25252 | delta:SF-2026-ARXIV-2605-25252 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-25252 |
| SF-2026-ARXIV-2605-25272 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-25272 | delta:SF-2026-ARXIV-2605-25272 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-25272 |
| SF-2026-ARXIV-2605-25284 | AGENT-PLANNING | books/part-07-agent/79-planning.md#chapter-79 | books/part-07-agent/78-tool-calling.md#chapter-78;books/part-07-agent/80-reflection.md#chapter-80 | existing:SF-2026-ARXIV-2605-25284 | delta:SF-2026-ARXIV-2605-25284 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25284 |
| SF-2026-ARXIV-2605-25292 | PLATFORM-GPU-SCHEDULER | books/part-06-ai-infrastructure/63-gpu-scheduler.md#chapter-63 | books/part-06-ai-infrastructure/62-gateway.md#chapter-62;books/part-06-ai-infrastructure/64-volcano.md#chapter-64 | existing:SF-2026-ARXIV-2605-25292 | delta:SF-2026-ARXIV-2605-25292 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25292 |
| SF-2026-ARXIV-2605-25298 | PLATFORM-MONITORING | books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66;books/part-06-ai-infrastructure/68-logging.md#chapter-68 | existing:SF-2026-ARXIV-2605-25298 | delta:SF-2026-ARXIV-2605-25298 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-25298 |
| SF-2026-ARXIV-2605-25313 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24;books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | existing:SF-2026-ARXIV-2605-25313 | delta:SF-2026-ARXIV-2605-25313 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25313 |
| SF-2026-ARXIV-2605-25338 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83;books/part-07-agent/README.md#knowledge-tree | existing:SF-2026-ARXIV-2605-25338 | delta:SF-2026-ARXIV-2605-25338 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25338 |
| SF-2026-ARXIV-2605-25375 | TRAIN-PIPELINE-PARALLEL | books/part-04-training-system/38-pipeline-parallel.md#chapter-38 | books/part-04-training-system/37-tensor-parallel.md#chapter-37;books/part-04-training-system/39-zero.md#chapter-39 | existing:SF-2026-ARXIV-2605-25375 | delta:SF-2026-ARXIV-2605-25375 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-25375 |
| SF-2026-ARXIV-2605-25376 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-25376 | delta:SF-2026-ARXIV-2605-25376 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25376 |
| SF-2026-ARXIV-2605-25379 | AGENT-RAG | books/part-07-agent/76-rag.md#chapter-76 | books/part-07-agent/75-context.md#chapter-75;books/part-07-agent/77-memory.md#chapter-77 | existing:SF-2026-ARXIV-2605-25379 | delta:SF-2026-ARXIV-2605-25379 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-25379 |
| SF-2026-ARXIV-2605-25389 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-25389 | delta:SF-2026-ARXIV-2605-25389 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25389 |
| SF-2026-ARXIV-2605-25421 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#chapter-82 | books/part-07-agent/81-workflow.md#chapter-81;books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-25421 | delta:SF-2026-ARXIV-2605-25421 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25421 |
| SF-2026-ARXIV-2605-25422 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#chapter-82 | books/part-07-agent/81-workflow.md#chapter-81;books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-25422 | delta:SF-2026-ARXIV-2605-25422 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25422 |
| SF-2026-ARXIV-2605-25424 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#chapter-56 | books/part-05-inference-system/55-pd-disaggregation.md#chapter-55;books/part-05-inference-system/README.md#knowledge-tree | existing:SF-2026-ARXIV-2605-25424 | delta:SF-2026-ARXIV-2605-25424 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-25424 |
| SF-2026-ARXIV-2605-25430 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83;books/part-07-agent/README.md#knowledge-tree | existing:SF-2026-ARXIV-2605-25430 | delta:SF-2026-ARXIV-2605-25430 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-25430 |
| SF-2026-ARXIV-2605-25451 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#chapter-36 | books/part-04-training-system/35-checkpoint.md#chapter-35;books/part-04-training-system/37-tensor-parallel.md#chapter-37 | existing:SF-2026-ARXIV-2605-25451 | delta:SF-2026-ARXIV-2605-25451 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25451 |
| SF-2026-ARXIV-2605-25475 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#chapter-45 | books/part-05-inference-system/44-decode.md#chapter-44;books/part-05-inference-system/46-continuous-batching.md#chapter-46 | existing:SF-2026-ARXIV-2605-25475 | delta:SF-2026-ARXIV-2605-25475 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25475 |
| SF-2026-ARXIV-2605-25492 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-25492 | delta:SF-2026-ARXIV-2605-25492 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-25492 |
| SF-2026-ARXIV-2605-25507 | TRAIN-PPO | books/part-04-training-system/32-ppo.md#chapter-32 | books/part-04-training-system/31-rlhf.md#chapter-31;books/part-04-training-system/33-grpo.md#chapter-33 | existing:SF-2026-ARXIV-2605-25507 | delta:SF-2026-ARXIV-2605-25507 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-25507 |
| SF-2026-ARXIV-2605-25521 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | books/part-05-inference-system/48-speculative-decoding.md#chapter-48;books/part-05-inference-system/50-vllm.md#chapter-50 | existing:SF-2026-ARXIV-2605-25521 | delta:SF-2026-ARXIV-2605-25521 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25521 |
| SF-2026-ARXIV-2605-25535 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76;books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-25535 | delta:SF-2026-ARXIV-2605-25535 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25535 |
| SF-2026-ARXIV-2605-25537 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25;books/part-03-multimodal-world-models/README.md#knowledge-tree | existing:SF-2026-ARXIV-2605-25537 | delta:SF-2026-ARXIV-2605-25537 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25537 |
| SF-2026-ARXIV-2605-25547 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25;books/part-03-multimodal-world-models/README.md#knowledge-tree | existing:SF-2026-ARXIV-2605-25547 | delta:SF-2026-ARXIV-2605-25547 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25547 |
| SF-2026-ARXIV-2605-25550 | INFER-PD-DISAGGREGATION | books/part-05-inference-system/55-pd-disaggregation.md#chapter-55 | books/part-05-inference-system/54-gpu-memory.md#chapter-54;books/part-05-inference-system/56-inference-scheduling.md#chapter-56 | existing:SF-2026-ARXIV-2605-25550 | delta:SF-2026-ARXIV-2605-25550 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-25550 |
| SF-2026-ARXIV-2605-25621 | MULTIMODAL-GENERATIVE-PARADIGMS | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24 | books/part-03-multimodal-world-models/23-multimodal-representation.md#chapter-23;books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | existing:SF-2026-ARXIV-2605-25621 | delta:SF-2026-ARXIV-2605-25621 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25621 |
| SF-2026-ARXIV-2605-25624 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83;books/part-07-agent/README.md#knowledge-tree | existing:SF-2026-ARXIV-2605-25624 | delta:SF-2026-ARXIV-2605-25624 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25624 |
| SF-2026-ARXIV-2605-25632 | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#chapter-78 | books/part-07-agent/77-memory.md#chapter-77;books/part-07-agent/79-planning.md#chapter-79 | existing:SF-2026-ARXIV-2605-25632 | delta:SF-2026-ARXIV-2605-25632 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-25632 |
| SF-2026-ARXIV-2605-25641 | AGENT-RAG | books/part-07-agent/76-rag.md#chapter-76 | books/part-07-agent/75-context.md#chapter-75;books/part-07-agent/77-memory.md#chapter-77 | existing:SF-2026-ARXIV-2605-25641 | delta:SF-2026-ARXIV-2605-25641 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25641 |
| SF-2026-ARXIV-2605-25653 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-25653 | delta:SF-2026-ARXIV-2605-25653 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25653 |
| SF-2026-ARXIV-2605-25655 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#chapter-56 | books/part-05-inference-system/55-pd-disaggregation.md#chapter-55;books/part-05-inference-system/README.md#knowledge-tree | existing:SF-2026-ARXIV-2605-25655 | delta:SF-2026-ARXIV-2605-25655 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25655 |
| SF-2026-ARXIV-2605-25673 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-25673 | delta:SF-2026-ARXIV-2605-25673 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-25673 |
| SF-2026-ARXIV-2605-25674 | PLATFORM-MONITORING | books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66;books/part-06-ai-infrastructure/68-logging.md#chapter-68 | existing:SF-2026-ARXIV-2605-25674 | delta:SF-2026-ARXIV-2605-25674 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25674 |
| SF-2026-ARXIV-2605-25682 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#chapter-56 | books/part-05-inference-system/55-pd-disaggregation.md#chapter-55;books/part-05-inference-system/README.md#knowledge-tree | existing:SF-2026-ARXIV-2605-25682 | delta:SF-2026-ARXIV-2605-25682 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25682 |
| SF-2026-ARXIV-2605-25698 | TRAIN-DATA | books/part-04-training-system/27-data.md#chapter-27 | books/part-04-training-system/28-pretraining.md#chapter-28 | existing:SF-2026-ARXIV-2605-25698 | delta:SF-2026-ARXIV-2605-25698 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-25698 |
| SF-2026-ARXIV-2605-25707 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-25707 | delta:SF-2026-ARXIV-2605-25707 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25707 |
| SF-2026-ARXIV-2605-25716 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-25716 | delta:SF-2026-ARXIV-2605-25716 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25716 |
| SF-2026-ARXIV-2605-25745 | MODEL-DECODER-ONLY | books/part-02-model/18-decoder-only.md#chapter-18 | books/part-02-model/17-transformer-layer.md#chapter-17;books/part-02-model/19-kv-cache.md#chapter-19 | existing:SF-2026-ARXIV-2605-25745 | delta:SF-2026-ARXIV-2605-25745 | Alternative Branch | Integrate | books-review:SF-2026-ARXIV-2605-25745 |
| SF-2026-ARXIV-2605-25746 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#chapter-82 | books/part-07-agent/81-workflow.md#chapter-81;books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-25746 | delta:SF-2026-ARXIV-2605-25746 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-25746 |
| SF-2026-ARXIV-2605-25798 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | books/part-05-inference-system/48-speculative-decoding.md#chapter-48;books/part-05-inference-system/50-vllm.md#chapter-50 | existing:SF-2026-ARXIV-2605-25798 | delta:SF-2026-ARXIV-2605-25798 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25798 |
| SF-2026-ARXIV-2605-25815 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83;books/part-07-agent/README.md#knowledge-tree | existing:SF-2026-ARXIV-2605-25815 | delta:SF-2026-ARXIV-2605-25815 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-25815 |
| SF-2026-ARXIV-2605-25819 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-25819 | delta:SF-2026-ARXIV-2605-25819 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-25819 |
| SF-2026-ARXIV-2605-25820 | MULTIMODAL-GENERATIVE-PARADIGMS | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24 | books/part-03-multimodal-world-models/23-multimodal-representation.md#chapter-23;books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | existing:SF-2026-ARXIV-2605-25820 | delta:SF-2026-ARXIV-2605-25820 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25820 |
| SF-2026-ARXIV-2605-25831 | AGENT-REFLECTION | books/part-07-agent/80-reflection.md#chapter-80 | books/part-07-agent/79-planning.md#chapter-79;books/part-07-agent/81-workflow.md#chapter-81 | existing:SF-2026-ARXIV-2605-25831 | delta:SF-2026-ARXIV-2605-25831 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-25831 |
| SF-2026-ARXIV-2605-25854 | PLATFORM-COST | books/part-06-ai-infrastructure/70-cost.md#chapter-70 | books/part-06-ai-infrastructure/69-trace.md#chapter-69;books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71 | existing:SF-2026-ARXIV-2605-25854 | delta:SF-2026-ARXIV-2605-25854 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-25854 |
| SF-2026-ARXIV-2605-25869 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76;books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-25869 | delta:SF-2026-ARXIV-2605-25869 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-25869 |
| SF-2026-ARXIV-2605-25874 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24;books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | existing:SF-2026-ARXIV-2605-25874 | delta:SF-2026-ARXIV-2605-25874 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25874 |
| SF-2026-ARXIV-2605-25889 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25;books/part-03-multimodal-world-models/README.md#knowledge-tree | existing:SF-2026-ARXIV-2605-25889 | delta:SF-2026-ARXIV-2605-25889 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-25889 |
| SF-2026-ARXIV-2605-25893 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-25893 | delta:SF-2026-ARXIV-2605-25893 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-25893 |
| SF-2026-ARXIV-2605-25966 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | books/part-05-inference-system/48-speculative-decoding.md#chapter-48;books/part-05-inference-system/50-vllm.md#chapter-50 | existing:SF-2026-ARXIV-2605-25966 | delta:SF-2026-ARXIV-2605-25966 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25966 |
| SF-2026-ARXIV-2605-25971 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83;books/part-07-agent/README.md#knowledge-tree | existing:SF-2026-ARXIV-2605-25971 | delta:SF-2026-ARXIV-2605-25971 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-25971 |
| SF-2026-ARXIV-2605-25988 | AGENT-RAG | books/part-07-agent/76-rag.md#chapter-76 | books/part-07-agent/75-context.md#chapter-75;books/part-07-agent/77-memory.md#chapter-77 | existing:SF-2026-ARXIV-2605-25988 | delta:SF-2026-ARXIV-2605-25988 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-25988 |
| SF-2026-ARXIV-2605-25997 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-25997 | delta:SF-2026-ARXIV-2605-25997 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-25997 |
| SF-2026-ARXIV-2605-26029 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#chapter-81 | books/part-07-agent/80-reflection.md#chapter-80;books/part-07-agent/82-multi-agent.md#chapter-82 | existing:SF-2026-ARXIV-2605-26029 | delta:SF-2026-ARXIV-2605-26029 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26029 |
| SF-2026-ARXIV-2605-26037 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#chapter-33 | books/part-04-training-system/32-ppo.md#chapter-32;books/part-04-training-system/34-dpo.md#chapter-34 | existing:SF-2026-ARXIV-2605-26037 | delta:SF-2026-ARXIV-2605-26037 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-26037 |
| SF-2026-ARXIV-2605-26045 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-26045 | delta:SF-2026-ARXIV-2605-26045 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-26045 |
| SF-2026-ARXIV-2605-26046 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-26046 | delta:SF-2026-ARXIV-2605-26046 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26046 |
| SF-2026-ARXIV-2605-26047 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-26047 | delta:SF-2026-ARXIV-2605-26047 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-26047 |
| SF-2026-ARXIV-2605-26079 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-26079 | delta:SF-2026-ARXIV-2605-26079 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26079 |
| SF-2026-ARXIV-2605-26110 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#chapter-36 | books/part-04-training-system/35-checkpoint.md#chapter-35;books/part-04-training-system/37-tensor-parallel.md#chapter-37 | existing:SF-2026-ARXIV-2605-26110 | delta:SF-2026-ARXIV-2605-26110 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26110 |
| SF-2026-ARXIV-2605-26112 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83;books/part-07-agent/README.md#knowledge-tree | existing:SF-2026-ARXIV-2605-26112 | delta:SF-2026-ARXIV-2605-26112 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26112 |
| SF-2026-ARXIV-2605-26114 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83;books/part-07-agent/README.md#knowledge-tree | existing:SF-2026-ARXIV-2605-26114 | delta:SF-2026-ARXIV-2605-26114 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26114 |
| SF-AERIC-ANTICIPATORY-HIDDEN-STATE-MONITORING-FOR-IMPLICIT-HARMFUL-DIALOGUE | PLATFORM-MONITORING | books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66; books/part-06-ai-infrastructure/68-logging.md#chapter-68 | existing:SF-AERIC-ANTICIPATORY-HIDDEN-STATE-MONITORING-FOR-IMPLICIT-HARMFUL-DIALOGUE | delta:SF-AERIC-ANTICIPATORY-HIDDEN-STATE-MONITORING-FOR-IMPLICIT-HARMFUL-DIALOGUE | Direct Evolution | Integrate | books-review:SF-AERIC-ANTICIPATORY-HIDDEN-STATE-MONITORING-FOR-IMPLICIT-HARMFUL-DIALOGUE |
| SF-FAITHFUL-OR-FABRICATED-A-CAUSAL-FRAMEWORK-FOR-RATIONALIZATION-BIAS-IN-LL | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-FAITHFUL-OR-FABRICATED-A-CAUSAL-FRAMEWORK-FOR-RATIONALIZATION-BIAS-IN-LL | delta:SF-FAITHFUL-OR-FABRICATED-A-CAUSAL-FRAMEWORK-FOR-RATIONALIZATION-BIAS-IN-LL | Direct Evolution | Integrate | books-review:SF-FAITHFUL-OR-FABRICATED-A-CAUSAL-FRAMEWORK-FOR-RATIONALIZATION-BIAS-IN-LL |
| SF-LGMT-LOGIC-GROUNDED-METAMORPHIC-TESTING-FOR-EVALUATING-THE-REASONING-REL | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-LGMT-LOGIC-GROUNDED-METAMORPHIC-TESTING-FOR-EVALUATING-THE-REASONING-REL | delta:SF-LGMT-LOGIC-GROUNDED-METAMORPHIC-TESTING-FOR-EVALUATING-THE-REASONING-REL | Direct Evolution | No Change — Existing Coverage | books-review:SF-LGMT-LOGIC-GROUNDED-METAMORPHIC-TESTING-FOR-EVALUATING-THE-REASONING-REL |
| SF-STOP-COMPARING-LLM-AGENTS-WITHOUT-DISCLOSING-THE-HARNESS | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-STOP-COMPARING-LLM-AGENTS-WITHOUT-DISCLOSING-THE-HARNESS | delta:SF-STOP-COMPARING-LLM-AGENTS-WITHOUT-DISCLOSING-THE-HARNESS | Direct Evolution | No Change — Existing Coverage | books-review:SF-STOP-COMPARING-LLM-AGENTS-WITHOUT-DISCLOSING-THE-HARNESS |

<!-- books-review:SF-2026-ARXIV-2605-23911:start -->
<!-- existing:SF-2026-ARXIV-2605-23911:start -->对读 `books/part-05-inference-system/49-tensorrt-llm.md#L53 (H3: Execution Plan 可以修订，但只能在安全边界 Commit)` 及相邻章节后，现有命题为：本章的核心判断是：**TensorRT-LLM 的核心不是改变模型语义，而是把经过验证的模型资产转换为面向 NVIDIA GPU 的执行计划，并用专用 kernels、quantization、KV management 与 runtime scheduling 交付它。** 目标小节已经拥有该 family 所需的长期 owner 与旧路径/约束边界。<!-- existing:SF-2026-ARXIV-2605-23911:end -->
<!-- delta:SF-2026-ARXIV-2605-23911:start -->Exact-v1 的 source-specific delta 是：We present TritonMoE, a fused MoE dispatch kernel written entirely in OpenAI Triton that performs the complete forward pass -- router scoring, token permutation, expert GEMMs, and weighted output combination -- using only portable Triton primitives. 其证据边界为：Evidence is author-reported exact-v1 mechanism/evaluation evidence. It does not establish cross-model, cross-hardware, cross-workload or production generality unless those conditions are explicitly named above. 该实现或实验没有改变当前章节已经成立的长期机制，不把作者 benchmark 外推为通用结论。<!-- delta:SF-2026-ARXIV-2605-23911:end -->
Decision: `No Change — Existing Coverage`; reviewer=fresh-context:apr-may-books-20260903。
<!-- books-review:SF-2026-ARXIV-2605-23911:end -->

<!-- books-review:SF-2026-ARXIV-2605-23918:start -->
<!-- existing:SF-2026-ARXIV-2605-23918:start -->对读 `books/part-06-ai-infrastructure/70-cost.md#L16 (H2: 资源时间是共同底座)` 及相邻章节后，现有命题为：本章的核心判断是：**AI cost 是资源在时间上的占用与机会成本，必须在质量、可靠性和 SLO 约束下按可归属结果计算；脱离 outcome 的利用率或单价会驱动错误优化。** 目标小节已经拥有该 family 所需的长期 owner 与旧路径/约束边界。<!-- existing:SF-2026-ARXIV-2605-23918:end -->
<!-- delta:SF-2026-ARXIV-2605-23918:start -->Exact-v1 的 source-specific delta 是：We present the first cross-architecture measurement of idle GPU power as a function of VRAM allocation, combining 18 days of production telemetry (335,267 samples, 14 H100 GPUs) with controlled dose-response experiments on three GPU architectures spanning three memory technologies: NVIDIA H100 (HBM3, 80 GB), A100 (HBM2e, 80 GB), and L40S (GDDR6, 48 GB). 其证据边界为：Evidence is author-reported exact-v1 mechanism/evaluation evidence. It does not establish cross-model, cross-hardware, cross-workload or production generality unless those conditions are explicitly named above. 该实现或实验没有改变当前章节已经成立的长期机制，不把作者 benchmark 外推为通用结论。<!-- delta:SF-2026-ARXIV-2605-23918:end -->
Decision: `No Change — Existing Coverage`; reviewer=fresh-context:apr-may-books-20260903。
<!-- books-review:SF-2026-ARXIV-2605-23918:end -->

<!-- books-review:SF-2026-ARXIV-2605-23935:start -->
<!-- existing:SF-2026-ARXIV-2605-23935:start -->对读 `books/part-06-ai-infrastructure/72-security.md#L29 (H2: 生命周期威胁)` 及相邻章节后，现有命题为：本章的核心判断是：**AI security 是贯穿 capability production、delivery 与 action 的风险管理。平台必须识别资产、主体、数据流和信任转换，并用 provenance、least privilege、isolation、validation 与 audit 建立纵深防御。** 目标小节已经拥有该 family 所需的长期 owner 与旧路径/约束边界。<!-- existing:SF-2026-ARXIV-2605-23935:end -->
<!-- delta:SF-2026-ARXIV-2605-23935:start -->Exact-v1 的 source-specific delta 是：We introduce a runtime execution model in which authority is evaluated at action time and execution is conditioned on its constructibility. 其证据边界为：Evidence is author-reported exact-v1 mechanism/evaluation evidence. It does not establish cross-model, cross-hardware, cross-workload or production generality unless those conditions are explicitly named above. 该实现或实验没有改变当前章节已经成立的长期机制，不把作者 benchmark 外推为通用结论。<!-- delta:SF-2026-ARXIV-2605-23935:end -->
Decision: `No Change — Existing Coverage`; reviewer=fresh-context:apr-may-books-20260903。
<!-- books-review:SF-2026-ARXIV-2605-23935:end -->

<!-- books-review:SF-2026-ARXIV-2605-23945:start --><!-- existing:SF-2026-ARXIV-2605-23945:start -->对读 `books/part-04-training-system/37-tensor-parallel.md` 与相邻 `Ch31/Ch41` 后，现有命题为：本章的核心判断是：**Tensor Parallel 选择代数上可分解的 operator 维度，用局部 GEMM 与必要 collective 共同实现原算子。**它降低每卡 layer 参数与计算，代价是把通信放进每层 forward/backward 的关键路径。第 36 章定义 collective semantics、algorithm 与 topology 的公共语言；本章只回答 TP 怎样消费 AllReduce、AllGather 与 ReduceScatter 来恢复 operator 语义。<!-- existing:SF-2026-ARXIV-2605-23945:end --><!-- delta:SF-2026-ARXIV-2605-23945:start -->新增 evidence delta：Synchronous RLHF generation should treat response-length skew as changing the efficient TP degree; online reconfiguration must compare predicted benefit with KV migration/recompute, reshard and communicator costs. 该 evidence 未改变现有长期命题，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2605-23945:end --><!-- books-review:SF-2026-ARXIV-2605-23945:end -->

<!-- books-review:SF-2026-ARXIV-2605-23951:start -->
<!-- existing:SF-2026-ARXIV-2605-23951:start -->已读取 `books/part-07-agent/84-agent-platform.md` 及同 Part 前后相邻章节；当前主线已覆盖skill/tool artifact 的身份、版本、admission、drift 与 capability containment。本 family 的 exact-v1 增量为“agent skill capability containment 需要 static effect analysis、refinement-typed dispatch 与 bounded model checking 组合，经验测试不能替代 soundness”，它没有改变现有 owner、控制权或共存边界，因此作为受限案例留在 Daily。<!-- existing:SF-2026-ARXIV-2605-23951:end -->
<!-- delta:SF-2026-ARXIV-2605-23951:start -->agent skill capability containment 需要 static effect analysis、refinement-typed dispatch 与 bounded model checking 组合，经验测试不能替代 soundness<!-- delta:SF-2026-ARXIV-2605-23951:end --> Decision: `No Change — Existing Coverage`。author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-23951:end -->

<!-- books-review:SF-2026-ARXIV-2605-23956:start -->
<!-- existing:SF-2026-ARXIV-2605-23956:start -->已读取 current owner `books/part-01-worldview/09-ai-system-evolution.md` 与相邻章节 `['books/part-01-worldview/08-why-llms-show-intelligence.md', 'books/part-01-worldview/10-future-of-ai.md']`，并只比较首个 `## Review notes` 之前的正文演进链；owner outline：## 本章要回答的问题 → ## 系统考古不是寻找相似名词 → ## 第一阶段：单机实验解决可行性 → ## 第二阶段：Pipeline 解决可复现生产 → ## 第三阶段：分布式训练解决规模约束 → ## 第四阶段：在线 Serving 解决能力交付 → ## 第五阶段：LLM Runtime 管理 token 与状态 → ## 第六阶段：平台治理解决跨团队控制 → ## 第七阶段：Agent Runtime 管理行动闭环 → ## MLOps、LLMOps 与 AgentOps 的边界 → ## 一条统一的演化逻辑 → ## 五条横向约束怎样穿过七个阶段 → ## 控制闭环是系统成熟的共同标志 → ## 本章在知识树中的位置。<!-- existing:SF-2026-ARXIV-2605-23956:end -->
<!-- delta:SF-2026-ARXIV-2605-23956:start -->Ch9/Ch66 已拥有 typed pipeline stages、feedback/error propagation 与 evaluation evidence；QUIVER 是分析框架分支。<!-- delta:SF-2026-ARXIV-2605-23956:end --> Decision=`No Change — Existing Coverage`；shared Books writeback 与独立 post-write audit 见 `books-post-write-semantic-audit.json`。
<!-- books-review:SF-2026-ARXIV-2605-23956:end -->

<!-- books-review:SF-2026-ARXIV-2605-23986:start -->
<!-- existing:SF-2026-ARXIV-2605-23986:start -->已逐章读取 `books/part-07-agent/77-memory.md` 与相邻章节 ['books/part-07-agent/76-rag.md', 'books/part-07-agent/78-tool-calling.md']；当前正文拥有 surrounding principle，但尚未显式承载 `MemForest: An Efficient Agent Memory System with Hierarchical Temporal Indexing` 改变的 state/data/control/evidence boundary。 owner_sha256=ac3bf5ab49bb87bcf3f0cfa1da47486caeb35e9d451251f91c67caf3bc9de6d7。<!-- existing:SF-2026-ARXIV-2605-23986:end -->
<!-- delta:SF-2026-ARXIV-2605-23986:start -->MemForest: An Efficient Agent Memory System with Hierarchical Temporal Indexing 提出的具体变化是：To address these challenges, we present MemForest, a memory framework that reformulates agent memory as a write-efficient temporal data-management problem. 摘要中的长期系统挑战为：hierarchical temporal indexing removes state-dependent generation from the memory write critical path。它可能改变 `AGENT-MEMORY` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“These results show that MemForest reduces memory-freshness latency while retaining strong answer quality.”暂不作为最终证据。<!-- delta:SF-2026-ARXIV-2605-23986:end --> Decision=`Integrate`；non-author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-23986:end -->

<!-- books-review:SF-2026-ARXIV-2605-23988:start -->
<!-- existing:SF-2026-ARXIV-2605-23988:start -->独立 reviewer 顺读 `books/part-04-training-system/36-distributed-training.md` 与相邻章节 ['books/part-04-training-system/35-checkpoint.md', 'books/part-04-training-system/37-tensor-parallel.md']。当前正文已覆盖一般机制；本项仍留下不可被现有论证替代的状态/控制/证据增量。 owner_sha256=c940481ca012303f984917615764a048e4a6742978fcb826524402093905481b。<!-- existing:SF-2026-ARXIV-2605-23988:end -->
<!-- delta:SF-2026-ARXIV-2605-23988:start -->split fine-tuning compresses activation tokens before transmission, coupling accuracy, uplink traffic, server compute and frozen-backbone identity<!-- delta:SF-2026-ARXIV-2605-23988:end --> Decision=`Integrate`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-23988:end -->

<!-- books-review:SF-2026-ARXIV-2605-23993:start -->
<!-- existing:SF-2026-ARXIV-2605-23993:start -->独立 reviewer 顺读 `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 与相邻章节 ['books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md', 'books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=e3eb726b0a302cf0dd2994ec6c50e1f6615e7bfee81edf9ca9bdbff7c78a6325。<!-- existing:SF-2026-ARXIV-2605-23993:end -->
<!-- delta:SF-2026-ARXIV-2605-23993:start -->a reproducible world-model substrate versions objective, action conditioning, latent state, rollout and evaluation rather than comparing entangled codebases<!-- delta:SF-2026-ARXIV-2605-23993:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-23993:end -->

<!-- books-review:SF-2026-ARXIV-2605-24004:start -->
<!-- existing:SF-2026-ARXIV-2605-24004:start -->已顺读 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 与相邻章节 ['books/part-03-multimodal-world-models/25-multimodal-world-models.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-24004:end -->
<!-- delta:SF-2026-ARXIV-2605-24004:start -->We propose Reason--Imagine--Act (RIA), a closed-loop framework that couples an LLM reasoner with an action-conditioned world model for online safety verification.<!-- delta:SF-2026-ARXIV-2605-24004:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-24004:end -->

<!-- books-review:SF-2026-ARXIV-2605-24006:start -->
<!-- existing:SF-2026-ARXIV-2605-24006:start -->已顺读 `books/part-04-training-system/38-pipeline-parallel.md` 与相邻章节 ['books/part-04-training-system/37-tensor-parallel.md', 'books/part-04-training-system/39-zero.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-24006:end -->
<!-- delta:SF-2026-ARXIV-2605-24006:start -->In this work, we introduce a tabular schedule abstraction and a unified multi-abstraction methodology that connects formula-based reasoning, idealized schedule tables, and communication-aware execution simulation.<!-- delta:SF-2026-ARXIV-2605-24006:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-24006:end -->

<!-- books-review:SF-2026-ARXIV-2605-24022:start -->
<!-- existing:SF-2026-ARXIV-2605-24022:start -->已顺读 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 与相邻章节 ['books/part-05-inference-system/44-decode.md', 'books/part-05-inference-system/46-continuous-batching.md']。第45章已覆盖 sparse selection、tiering、prefetch、eviction、reuse identity、误差预算与 exact recompute fallback。`Adaptive KV Cache Reuse for Fast Long-Context LLM Serving` 的 source-specific 机制是：Evaluations on mainstream LLMs and long-context tasks show that CacheTune achieves 3.72x-4.86x TTFT speedup and 3.93x-6.21x higher throughput while maintaining generation quality close to full recompute.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-24022:end -->
<!-- delta:SF-2026-ARXIV-2605-24022:start -->Evaluations on mainstream LLMs and long-context tasks show that CacheTune achieves 3.72x-4.86x TTFT speedup and 3.93x-6.21x higher throughput while maintaining generation quality close to full recompute.<!-- delta:SF-2026-ARXIV-2605-24022:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-24022:end -->

<!-- existing:SF-2026-ARXIV-2605-24036:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', 'Agent 改变了平台的控制对象', 'Serving 结束不等于 Agent 任务结束', 'Agent Definition 与 Run Identity', '可编程 Skill 需要输入、状态与副作用契约', '可复用 Skill 不是一个 Prompt 文件', '从 Skill Catalog 到 Competence-aware Orchestration', '从 Trajectory 到 Skill 是一次受治理的 Compilation', 'Skill Compiler 必须绑定 Target Profile，而不是只绑定模型名', 'Self-evolution Admission 需要 Anytime-valid Acceptor', 'Workspace 是长期行动的隔离单元', '三个平面', 'Agent Runtime State Machine', 'Scheduling 不只是 GPU']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-24036:end -->
<!-- delta:SF-2026-ARXIV-2605-24036:start -->Programming languages assume programs directly execute effects.<!-- delta:SF-2026-ARXIV-2605-24036:end -->
<!-- books-review:SF-2026-ARXIV-2605-24036:start -->owner=`AGENT-PLATFORM`；decision=`No Change — Existing Coverage`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-24036:end -->

<!-- existing:SF-2026-ARXIV-2605-24042:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', '从资产与信任边界开始', '生命周期威胁', '隐私检测是 Policy-bound Sensor，不是安全判决', '从独立 Span 到关系感知的本地 Sanitization', 'Differential Privacy 先定义被保护对象，再选择机制', 'Privacy Accountant 必须与真实实现同构', 'Capability Access Control 可以前移到训练状态', 'Policy-as-Data：可更新规则与模型判断必须分开版本化', '从“文本是否恶意”到“谁获得了行为控制权”', '多 Agent Cascade 需要跨 Channel 的 Influence Graph', 'Safety Evaluation 的单位是 Run，不只是 Prompt', 'Security Agent 的评估必须绑定 Tool Trace 与 Deterministic Predicate', 'Containment 不能只看最终是否发生攻击']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-24042:end -->
<!-- delta:SF-2026-ARXIV-2605-24042:start -->hidden-state release 的 privacy/utility 不是连续可调的天然中间地带：若中间状态保留任务信息就可能保留敏感信息；release owner 必须选择 architecture co-design、受限接口或不发布，而不能只调高噪声后宣称安全。<!-- delta:SF-2026-ARXIV-2605-24042:end -->
<!-- books-review:SF-2026-ARXIV-2605-24042:start -->owner=`PLATFORM-SECURITY`；decision=`Integrate`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-24042:end -->

<!-- existing:SF-2026-ARXIV-2605-24044:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', '调度对象从 request 变成 token state', '目标函数不止吞吐', 'SLO-aware Admission', '当前能放下，不等于未来可完成', '不确定输出长度下的 Future-state Reservation', '连续 Edge Inference 需要跨窗口携带 Violation-risk Budget', '从队列启发式到时间耦合的资源影子价格', 'Reasoning Budget 必须进入调度与评估身份', 'Inference-time Process Guidance 也是可调度资源', 'Iteration Scheduling', 'Physical AI 把 Execution Horizon 变成调度状态', 'Routing、Placement 与 Autoscaling', 'Heterogeneous Offload 必须同时预算 Preemption 与 State Transfer']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-24044:end -->
<!-- delta:SF-2026-ARXIV-2605-24044:start -->We present RED, a real-time scheduling framework for multi-task deep neural network workloads on resource-constrained robotic platforms that adapts to Robotic Environmental Dynamics (RED) while preserving end-to-end timing guarantees under modeling assumptions.<!-- delta:SF-2026-ARXIV-2605-24044:end -->
<!-- books-review:SF-2026-ARXIV-2605-24044:start -->owner=`INFER-SCHEDULING`；decision=`No Change — Existing Coverage`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-24044:end -->

<!-- existing:SF-2026-ARXIV-2605-24050:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', 'Agent 改变了平台的控制对象', 'Serving 结束不等于 Agent 任务结束', 'Agent Definition 与 Run Identity', '可编程 Skill 需要输入、状态与副作用契约', '可复用 Skill 不是一个 Prompt 文件', '从 Skill Catalog 到 Competence-aware Orchestration', '从 Trajectory 到 Skill 是一次受治理的 Compilation', 'Skill Compiler 必须绑定 Target Profile，而不是只绑定模型名', 'Self-evolution Admission 需要 Anytime-valid Acceptor', 'Workspace 是长期行动的隔离单元', '三个平面', 'Agent Runtime State Machine', 'Scheduling 不只是 GPU']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-24050:end -->
<!-- delta:SF-2026-ARXIV-2605-24050:start -->Moreover, we propose to decompose the pass rate drop by conditioning on the skill(s) invocation -- which skills the agent selects during a trajectory -- into two effects: \emph{skill shadowing}, where the agent selects wrong skills more often as the library expands, and \emph{context overhead}, where the enlarged context degrades execution even when selection is correct.<!-- delta:SF-2026-ARXIV-2605-24050:end -->
<!-- books-review:SF-2026-ARXIV-2605-24050:start -->owner=`AGENT-PLATFORM`；decision=`No Change — Existing Coverage`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-24050:end -->

<!-- books-review:SF-2026-ARXIV-2605-24060:start -->
<!-- existing:SF-2026-ARXIV-2605-24060:start -->正文已覆盖 Evaluation Identity、trajectory、judge budget、confidence/calibration、policy-bound sensor 与 evidence/release gate。 本 family 的具体机制 `We show that this scoring-target choice is often left implicit and can materially change benchmark conclusions.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-24060:end -->
<!-- delta:SF-2026-ARXIV-2605-24060:start -->We show that this scoring-target choice is often left implicit and can materially change benchmark conclusions.<!-- delta:SF-2026-ARXIV-2605-24060:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=2d996d80d292f4f17ab2ef9ecd57033f53ee34128f8ddad48df2fcce7e1c1f9d。
<!-- books-review:SF-2026-ARXIV-2605-24060:end -->

<!-- books-review:SF-2026-ARXIV-2605-24069:start -->
<!-- existing:SF-2026-ARXIV-2605-24069:start -->正文已覆盖 protocol/authorization boundary、tool-set admission、information flow、effect-time authorization 与 provenance。 本 family 的具体机制 `To rigorously and systematically evaluate this emerging threat, we introduce the MCP-TDP Security Benchmark.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-24069:end -->
<!-- delta:SF-2026-ARXIV-2605-24069:start -->To rigorously and systematically evaluate this emerging threat, we introduce the MCP-TDP Security Benchmark.<!-- delta:SF-2026-ARXIV-2605-24069:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=49fbcf4975553049fa6fbcf81baf5b91d04ff47dd5faa14191df42827025fc76。
<!-- books-review:SF-2026-ARXIV-2605-24069:end -->

<!-- books-review:SF-2026-ARXIV-2605-24117:start -->
<!-- existing:SF-2026-ARXIV-2605-24117:start -->正文已覆盖 Skill lifecycle、self-evolution admission、artifact identity 与 drift retirement。 本 family 的具体机制 `We introduce SkillEvolBench, a diagnostic benchmark for evaluating this step from experience reuse to skill formation.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-24117:end -->
<!-- delta:SF-2026-ARXIV-2605-24117:start -->We introduce SkillEvolBench, a diagnostic benchmark for evaluating this step from experience reuse to skill formation.<!-- delta:SF-2026-ARXIV-2605-24117:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=6980a9cf747990532ed9860f9f29811513be4f712acea90972df70247cbc3360。
<!-- books-review:SF-2026-ARXIV-2605-24117:end -->

<!-- books-review:SF-2026-ARXIV-2605-24134:start -->
<!-- existing:SF-2026-ARXIV-2605-24134:start -->正文已覆盖 Evaluation Identity、trajectory、judge budget、confidence/calibration、policy-bound sensor 与 evidence/release gate。 本 family 的具体机制 `We introduce ProofAgent Harness, open infrastructure for scalable, auditable, and adversarial AI agent evaluation.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-24134:end -->
<!-- delta:SF-2026-ARXIV-2605-24134:start -->We introduce ProofAgent Harness, open infrastructure for scalable, auditable, and adversarial AI agent evaluation.<!-- delta:SF-2026-ARXIV-2605-24134:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=2d996d80d292f4f17ab2ef9ecd57033f53ee34128f8ddad48df2fcce7e1c1f9d。
<!-- books-review:SF-2026-ARXIV-2605-24134:end -->

<!-- books-review:SF-2026-ARXIV-2605-24154:start -->
<!-- existing:SF-2026-ARXIV-2605-24154:start -->正文已覆盖 policy-bound sensor、supply-chain、prompt/tool authority、shared-state privacy 与 human approval；只有改变边界对象或 admission 权限的证据才需追加。 本 family 的具体机制 `To this end, we propose \textsc{Palette}, a modular, controllable, and efficient framework that selectively relaxes refusal behavior on authorized target domains while preserving standard safety elsewhere.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-24154:end -->
<!-- delta:SF-2026-ARXIV-2605-24154:start -->To this end, we propose \textsc{Palette}, a modular, controllable, and efficient framework that selectively relaxes refusal behavior on authorized target domains while preserving standard safety elsewhere.<!-- delta:SF-2026-ARXIV-2605-24154:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=40095d409cb4bf91595d96c61e60d528b79b073488677723402dd3c23057bb9f。
<!-- books-review:SF-2026-ARXIV-2605-24154:end -->

<!-- books-review:SF-2026-ARXIV-2605-24168:start -->
<!-- existing:SF-2026-ARXIV-2605-24168:start -->正文已覆盖 context assembly、compression loss、identity、policy integrity 与 long-session state。 本 family 的具体机制 `Second, we perform an extensive study of sparsity in LLMs spanning 20 models across five model families, varying context lengths, and different sparsity levels.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-24168:end -->
<!-- delta:SF-2026-ARXIV-2605-24168:start -->Second, we perform an extensive study of sparsity in LLMs spanning 20 models across five model families, varying context lengths, and different sparsity levels.<!-- delta:SF-2026-ARXIV-2605-24168:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=55db3e124881a0bcde65d0587c9c31fa32ada720f92e5a0fc530cbb77952a53d。
<!-- books-review:SF-2026-ARXIV-2605-24168:end -->

<!-- books-review:SF-2026-ARXIV-2605-24183:start -->
<!-- existing:SF-2026-ARXIV-2605-24183:start -->正文已覆盖 Evaluation Identity、trajectory、judge budget、confidence/calibration、policy-bound sensor 与 evidence/release gate。 本 family 的具体机制 `We introduce AvalancheBench, a benchmark for evaluating enterprise data agents through \emph{latent world recovery}.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-24183:end -->
<!-- delta:SF-2026-ARXIV-2605-24183:start -->We introduce AvalancheBench, a benchmark for evaluating enterprise data agents through \emph{latent world recovery}.<!-- delta:SF-2026-ARXIV-2605-24183:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=2d996d80d292f4f17ab2ef9ecd57033f53ee34128f8ddad48df2fcce7e1c1f9d。
<!-- books-review:SF-2026-ARXIV-2605-24183:end -->

<!-- books-review:SF-2026-ARXIV-2605-24197:start -->
<!-- existing:SF-2026-ARXIV-2605-24197:start -->正文已覆盖 coordination state、identity/delegation、shared-state commit、verification 与 topology cost。 本 family 的具体机制 `We study a class of emergent misalignment in multi-agent systems (MAS), with a focus on automated workflows, which we refer to agentic misalignment.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-24197:end -->
<!-- delta:SF-2026-ARXIV-2605-24197:start -->We study a class of emergent misalignment in multi-agent systems (MAS), with a focus on automated workflows, which we refer to agentic misalignment.<!-- delta:SF-2026-ARXIV-2605-24197:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=790fbd7fa453181af6ae4c0885cecf49590beecc162a4d9b3a8ea9f8823d0fd3。
<!-- books-review:SF-2026-ARXIV-2605-24197:end -->

<!-- books-review:SF-2026-ARXIV-2605-24202:start -->
<!-- existing:SF-2026-ARXIV-2605-24202:start -->正文已覆盖 rubric/reward ownership、on-policy freshness、teacher/evidence boundary 与 trajectory credit。 本 family 的具体机制 `We study when end-to-end RL training of multi-agent LLM workflows improves over their base models, comparing Shared-Policy training, where all roles update one policy, with Isolated-Policy training, where each role has its own parameters.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-24202:end -->
<!-- delta:SF-2026-ARXIV-2605-24202:start -->We study when end-to-end RL training of multi-agent LLM workflows improves over their base models, comparing Shared-Policy training, where all roles update one policy, with Isolated-Policy training, where each role has its own parameters.<!-- delta:SF-2026-ARXIV-2605-24202:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=1399c1280771b79bb05afde8ddf4551654c2f7ab47c9654a799131a117ca3e09。
<!-- books-review:SF-2026-ARXIV-2605-24202:end -->

<!-- books-review:SF-2026-ARXIV-2605-24213:start -->
<!-- existing:SF-2026-ARXIV-2605-24213:start -->正文已覆盖 Evaluation Identity、trajectory、judge budget、confidence/calibration、policy-bound sensor 与 evidence/release gate。 本 family 的具体机制 `We present an empirical study of 57 evaluation harnesses, deriving a five-stage harness model and classifying 16,560 issues by workflow stage and root cause.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-24213:end -->
<!-- delta:SF-2026-ARXIV-2605-24213:start -->We present an empirical study of 57 evaluation harnesses, deriving a five-stage harness model and classifying 16,560 issues by workflow stage and root cause.<!-- delta:SF-2026-ARXIV-2605-24213:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=2d996d80d292f4f17ab2ef9ecd57033f53ee34128f8ddad48df2fcce7e1c1f9d。
<!-- books-review:SF-2026-ARXIV-2605-24213:end -->

<!-- books-review:SF-2026-ARXIV-2605-24216:start -->
<!-- existing:SF-2026-ARXIV-2605-24216:start -->正文已覆盖 policy-bound sensor、supply-chain、prompt/tool authority、shared-state privacy 与 human approval；只有改变边界对象或 admission 权限的证据才需追加。 本 family 的具体机制 `We propose \textbf{Agent-ToM}, a learning-to-monitor framework grounded in Theory-of-Mind (ToM) reasoning for security analysis of autonomous agents.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-24216:end -->
<!-- delta:SF-2026-ARXIV-2605-24216:start -->We propose \textbf{Agent-ToM}, a learning-to-monitor framework grounded in Theory-of-Mind (ToM) reasoning for security analysis of autonomous agents.<!-- delta:SF-2026-ARXIV-2605-24216:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=40095d409cb4bf91595d96c61e60d528b79b073488677723402dd3c23057bb9f。
<!-- books-review:SF-2026-ARXIV-2605-24216:end -->

<!-- books-review:SF-2026-ARXIV-2605-24217:start -->
<!-- existing:SF-2026-ARXIV-2605-24217:start -->现有 Evaluation 章尚未把 benchmark client 自身的单进程排队偏差纳入 TTFT/TPOT measurement identity。<!-- existing:SF-2026-ARXIV-2605-24217:end -->
<!-- delta:SF-2026-ARXIV-2605-24217:start -->We demonstrate that widely used benchmarking utilities rely on single-process, asyncio-driven architectures that introduce fundamental client-side queuing bottlenecks under high concurrency.<!-- delta:SF-2026-ARXIV-2605-24217:end --> Independent decision=`Integrate`；owner_sha256=2d996d80d292f4f17ab2ef9ecd57033f53ee34128f8ddad48df2fcce7e1c1f9d。
<!-- books-review:SF-2026-ARXIV-2605-24217:end -->

<!-- books-review:SF-2026-ARXIV-2605-24219:start -->
<!-- existing:SF-2026-ARXIV-2605-24219:start -->正文已覆盖 Evaluation Identity、trajectory、judge budget、confidence/calibration、policy-bound sensor 与 evidence/release gate。 本 family 的具体机制 `We present Trajel, a dataset and evaluation framework for auditing trajectory-level hallucinations in multi-agent industrial workflows.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-24219:end -->
<!-- delta:SF-2026-ARXIV-2605-24219:start -->We present Trajel, a dataset and evaluation framework for auditing trajectory-level hallucinations in multi-agent industrial workflows.<!-- delta:SF-2026-ARXIV-2605-24219:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=2d996d80d292f4f17ab2ef9ecd57033f53ee34128f8ddad48df2fcce7e1c1f9d。
<!-- books-review:SF-2026-ARXIV-2605-24219:end -->

<!-- books-review:SF-2026-ARXIV-2605-24220:start -->
<!-- existing:SF-2026-ARXIV-2605-24220:start -->正文已覆盖 rubric/reward ownership、on-policy freshness、teacher/evidence boundary 与 trajectory credit。 本 family 的具体机制 `This decoupled design makes Polar agnostic to agent harnesses, training infrastructure, and RL algorithms while improving compute utilization for long-running agent workloads.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-24220:end -->
<!-- delta:SF-2026-ARXIV-2605-24220:start -->This decoupled design makes Polar agnostic to agent harnesses, training infrastructure, and RL algorithms while improving compute utilization for long-running agent workloads.<!-- delta:SF-2026-ARXIV-2605-24220:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=1399c1280771b79bb05afde8ddf4551654c2f7ab47c9654a799131a117ca3e09。
<!-- books-review:SF-2026-ARXIV-2605-24220:end -->

<!-- books-review:SF-2026-ARXIV-2605-24229:start -->
<!-- existing:SF-2026-ARXIV-2605-24229:start -->现有 Evaluation 章缺少将长篇 policy/constitution 分解为 versioned atomic tenets，并在多轮对抗压力下审计 adherence 的闭环。<!-- existing:SF-2026-ARXIV-2605-24229:end -->
<!-- delta:SF-2026-ARXIV-2605-24229:start -->We propose a multi-method audit pipeline that treats each lab's published specification as an auditable target: it decomposes the specification into atomic testable tenets (205 for Anthropic, 197 for OpenAI), generates multi-turn adversarial scenarios with the Petri auditing agent (Anthropic, 2025b), runs a modified SURF-style rubric search (Murray et al., 2026) to catch shallow single-turn failures Petri misses, validates flagged transcripts against the relevant specification, and compares the findings against the lab's own published system card.<!-- delta:SF-2026-ARXIV-2605-24229:end --> Independent decision=`Integrate`；owner_sha256=2d996d80d292f4f17ab2ef9ecd57033f53ee34128f8ddad48df2fcce7e1c1f9d。
<!-- books-review:SF-2026-ARXIV-2605-24229:end -->

<!-- books-review:SF-2026-ARXIV-2605-24245:start -->
<!-- existing:SF-2026-ARXIV-2605-24245:start -->正文已覆盖 policy-bound sensor、supply-chain、prompt/tool authority、shared-state privacy 与 human approval；只有改变边界对象或 admission 权限的证据才需追加。 本 family 的具体机制 `We show that for many common search topics, they repeatedly retrieve the same user-generated content (UGC) pages from platforms such as Reddit and Wikipedia.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-24245:end -->
<!-- delta:SF-2026-ARXIV-2605-24245:start -->We show that for many common search topics, they repeatedly retrieve the same user-generated content (UGC) pages from platforms such as Reddit and Wikipedia.<!-- delta:SF-2026-ARXIV-2605-24245:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=40095d409cb4bf91595d96c61e60d528b79b073488677723402dd3c23057bb9f。
<!-- books-review:SF-2026-ARXIV-2605-24245:end -->

<!-- books-review:SF-2026-ARXIV-2605-24247:start -->
<!-- existing:SF-2026-ARXIV-2605-24247:start -->正文已覆盖 data lineage、poisoning/contamination、specification compilation 与 golden-data governance。 本 family 的具体机制 `We propose and demonstrate the efficacy of an AI-driven workflow in which AI helps write a per-category constitution that defines the label in enough detail to cover edge cases, and a frontier LLM interprets it on each input to produce the golden label more consistently and accurately than humans reading the same document.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-24247:end -->
<!-- delta:SF-2026-ARXIV-2605-24247:start -->We propose and demonstrate the efficacy of an AI-driven workflow in which AI helps write a per-category constitution that defines the label in enough detail to cover edge cases, and a frontier LLM interprets it on each input to produce the golden label more consistently and accurately than humans reading the same document.<!-- delta:SF-2026-ARXIV-2605-24247:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=6a791d1111cd7019627ea79d0c2c9be8cc4ca30ec72dbb295553428a5250f5c1。
<!-- books-review:SF-2026-ARXIV-2605-24247:end -->

<!-- books-review:SF-2026-ARXIV-2605-24248:start -->
<!-- existing:SF-2026-ARXIV-2605-24248:start -->现有 MCP 章说明 authorization 不等于 trust，但未给出 server identity、tool allowlist、sensitivity 与 attestation root 的 admission contract。<!-- existing:SF-2026-ARXIV-2605-24248:end -->
<!-- delta:SF-2026-ARXIV-2605-24248:start -->We give the wire format, the verification algorithm, a security analysis, and an LLM-driven adversarial evaluation; we then state the design in normative Request-for-Comments (RFC 2119) form -- schema, verification rules, error registry, well-known registration, and machine-checkable conformance vectors -- so it can be adopted as an MCP addendum rather than reinvented.<!-- delta:SF-2026-ARXIV-2605-24248:end --> Independent decision=`Integrate`；owner_sha256=49fbcf4975553049fa6fbcf81baf5b91d04ff47dd5faa14191df42827025fc76。
<!-- books-review:SF-2026-ARXIV-2605-24248:end -->

<!-- books-review:SF-2026-ARXIV-2605-24259:start -->
<!-- existing:SF-2026-ARXIV-2605-24259:start -->现有 KV lifecycle 没有把 future-reuse intent、materialization predicate、active/resident feasibility 与 telemetry 合成可移植 conformance claim。<!-- existing:SF-2026-ARXIV-2605-24259:end -->
<!-- delta:SF-2026-ARXIV-2605-24259:start -->We introduce resident KV claims, a conformance contract that binds future-reuse intent to a materialization predicate, lifecycle state, active/resident feasibility outcome, and claim-level telemetry.<!-- delta:SF-2026-ARXIV-2605-24259:end --> Independent decision=`Integrate`；owner_sha256=322a087f0629a6acc48fc085f83172b753f8fa38a54f182e7b9d5f8d36b02348。
<!-- books-review:SF-2026-ARXIV-2605-24259:end -->

<!-- books-review:SF-2026-ARXIV-2605-24279:start -->
<!-- existing:SF-2026-ARXIV-2605-24279:start -->现有 Context 章没有把长会话 compaction 后的 persona/role drift 作为可 fork、可重放的 deployment-state evaluation。<!-- existing:SF-2026-ARXIV-2605-24279:end -->
<!-- delta:SF-2026-ARXIV-2605-24279:start -->We introduce ContextEcho, a benchmark and reusable harness for measuring persona drift at deployment scale.<!-- delta:SF-2026-ARXIV-2605-24279:end --> Independent decision=`Integrate`；owner_sha256=55db3e124881a0bcde65d0587c9c31fa32ada720f92e5a0fc530cbb77952a53d。
<!-- books-review:SF-2026-ARXIV-2605-24279:end -->

<!-- books-review:SF-2026-ARXIV-2605-24286:start -->
<!-- existing:SF-2026-ARXIV-2605-24286:start -->正文已覆盖 Evaluation Identity、trajectory、judge budget、confidence/calibration、policy-bound sensor 与 evidence/release gate。 本 family 的具体机制 `We study CoT faithfulness through a structural information-flow perspective: faithful reasoning should route answer-relevant information through the mediated path from prompt to CoT to answer, rather than through a direct prompt-to-answer shortcut.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-24286:end -->
<!-- delta:SF-2026-ARXIV-2605-24286:start -->We study CoT faithfulness through a structural information-flow perspective: faithful reasoning should route answer-relevant information through the mediated path from prompt to CoT to answer, rather than through a direct prompt-to-answer shortcut.<!-- delta:SF-2026-ARXIV-2605-24286:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=2d996d80d292f4f17ab2ef9ecd57033f53ee34128f8ddad48df2fcce7e1c1f9d。
<!-- books-review:SF-2026-ARXIV-2605-24286:end -->

<!-- books-review:SF-2026-ARXIV-2605-24299:start -->
<!-- existing:SF-2026-ARXIV-2605-24299:start -->正文已覆盖 Evaluation Identity、trajectory、judge budget、confidence/calibration、policy-bound sensor 与 evidence/release gate。 本 family 的具体机制 `Confidence-weighted routing, selective abstention, and ensemble weighting all assume that a model's stated confidence is informative about its capability on the question being asked.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-24299:end -->
<!-- delta:SF-2026-ARXIV-2605-24299:start -->Confidence-weighted routing, selective abstention, and ensemble weighting all assume that a model's stated confidence is informative about its capability on the question being asked.<!-- delta:SF-2026-ARXIV-2605-24299:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=2d996d80d292f4f17ab2ef9ecd57033f53ee34128f8ddad48df2fcce7e1c1f9d。
<!-- books-review:SF-2026-ARXIV-2605-24299:end -->

<!-- books-review:SF-2026-ARXIV-2605-24309:start -->
<!-- existing:SF-2026-ARXIV-2605-24309:start -->正文已覆盖 policy-bound sensor、supply-chain、prompt/tool authority、shared-state privacy 与 human approval；只有改变边界对象或 admission 权限的证据才需追加。 本 family 的具体机制 `Third, we propose a three-direction research agenda and call for AHI security to be recognized as a first-class research citizen, one that demands its own design principles, evaluation methods, and theoretical foundations.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-24309:end -->
<!-- delta:SF-2026-ARXIV-2605-24309:start -->Third, we propose a three-direction research agenda and call for AHI security to be recognized as a first-class research citizen, one that demands its own design principles, evaluation methods, and theoretical foundations.<!-- delta:SF-2026-ARXIV-2605-24309:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=40095d409cb4bf91595d96c61e60d528b79b073488677723402dd3c23057bb9f。
<!-- books-review:SF-2026-ARXIV-2605-24309:end -->

<!-- books-review:SF-2026-ARXIV-2605-24312:start -->
<!-- existing:SF-2026-ARXIV-2605-24312:start -->现有 RAG 安全叙述未明确输出蕴含信号可在低查询预算下泄露 corpus membership。<!-- existing:SF-2026-ARXIV-2605-24312:end -->
<!-- delta:SF-2026-ARXIV-2605-24312:start -->However, this design introduces a new privacy risk: model outputs may signal the presence of specific documents in the retrieval corpus, enabling membership inference attacks (MIAs) that leak sensitive information.<!-- delta:SF-2026-ARXIV-2605-24312:end --> Independent decision=`Integrate`；owner_sha256=3011c1f900fd57c3767efb22ef3cd9b180fd95ace4e1c157c325d229ff114c83。
<!-- books-review:SF-2026-ARXIV-2605-24312:end -->

<!-- books-review:SF-2026-ARXIV-2605-24326:start -->
<!-- existing:SF-2026-ARXIV-2605-24326:start -->现有章节已覆盖 topology-aware placement、collective/parallelism co-design、异构网络 profile、simulation 与 fallback；ScaleAcross 属于同一机制的跨楼宇实例。<!-- existing:SF-2026-ARXIV-2605-24326:end -->
<!-- delta:SF-2026-ARXIV-2605-24326:start -->As infrastructure expands, the system design space becomes increasingly intricate, encompassing new model architectures, hardware heterogeneity, and evolving communication patterns.<!-- delta:SF-2026-ARXIV-2605-24326:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=4f93d876e7023721408d2cb9a84c868ecf7049796c99bb18d430ffb936337560。
<!-- books-review:SF-2026-ARXIV-2605-24326:end -->

<!-- books-review:SF-2026-ARXIV-2605-24391:start -->
<!-- existing:SF-2026-ARXIV-2605-24391:start -->现有执行计划覆盖 bit-exact format，却未表达同一 microscaling block 在 training/direct-cast inference 间按 exponent/mantissa mode 切换的格式与硬件共同身份。<!-- existing:SF-2026-ARXIV-2605-24391:end -->
<!-- delta:SF-2026-ARXIV-2605-24391:start -->In this work, we present a versatile MXFP format, called MX-SAFE (MXSF in short), that adaptively uses two modes, i.e., a wider mantissa mode (FP8 E2M5) and a subnormal FP mode (FP5 E3M2), to support both training and direct-cast inference.<!-- delta:SF-2026-ARXIV-2605-24391:end --> Independent decision=`Integrate`；owner_sha256=86a67912e98da1110924056b16139a49e3854f707c8d56e04448ce75d12c6950。
<!-- books-review:SF-2026-ARXIV-2605-24391:end -->

<!-- books-review:SF-2026-ARXIV-2605-24420:start -->
<!-- existing:SF-2026-ARXIV-2605-24420:start -->现有 privacy 章没有把 BatchNorm cross-sample statistics 作为 memorization 与 membership inference 的训练态共享通道。<!-- existing:SF-2026-ARXIV-2605-24420:end -->
<!-- delta:SF-2026-ARXIV-2605-24420:start -->We conduct an extensive empirical study using three complementary approaches: (i) unintended memorization of out-of-distribution training samples, (ii) per-sample influence measured via gradient norms, and (iii) susceptibility to membership inference attacks (MIA).<!-- delta:SF-2026-ARXIV-2605-24420:end --> Independent decision=`Integrate`；owner_sha256=ef7882199869af53c1d9715b6343b35023fff4e4a578647be098c6dbdd21cf0e。
<!-- books-review:SF-2026-ARXIV-2605-24420:end -->

<!-- books-review:SF-2026-ARXIV-2605-24421:start -->
<!-- existing:SF-2026-ARXIV-2605-24421:start -->现有 prompt-injection 边界没有把 attacker-controlled log field 明确视为安全分析链路的 untrusted instruction substrate。<!-- existing:SF-2026-ARXIV-2605-24421:end -->
<!-- delta:SF-2026-ARXIV-2605-24421:start -->We study a structural failure mode of this design: many log fields are attacker controlled.<!-- delta:SF-2026-ARXIV-2605-24421:end --> Independent decision=`Integrate`；owner_sha256=ef7882199869af53c1d9715b6343b35023fff4e4a578647be098c6dbdd21cf0e。
<!-- books-review:SF-2026-ARXIV-2605-24421:end -->

<!-- books-review:SF-2026-ARXIV-2605-24425:start -->
<!-- existing:SF-2026-ARXIV-2605-24425:start -->现有 Transformer Layer 把 residual stream 当 activation carrier，未表达跨层 momentum state 如何改变深度方向更新以及与 preconditioning 分工。<!-- existing:SF-2026-ARXIV-2605-24425:end -->
<!-- delta:SF-2026-ARXIV-2605-24425:start -->A controlled ablation and supporting theory show that momentum, not preconditioning, is the main source of the gain.<!-- delta:SF-2026-ARXIV-2605-24425:end --> Independent decision=`Integrate`；owner_sha256=c03328e1ab575411f62dbdf61f64d8559082b96df8e231b5b3795adde2a69a15。
<!-- books-review:SF-2026-ARXIV-2605-24425:end -->

<!-- books-review:SF-2026-ARXIV-2605-24426:start -->
<!-- existing:SF-2026-ARXIV-2605-24426:start -->现有 RLHF 将 environment/interface 多视作固定 rollout 条件；缺少 verifier diagnosis 驱动 learning interface 与 policy 同步演进的双 owner 闭环。<!-- existing:SF-2026-ARXIV-2605-24426:end -->
<!-- delta:SF-2026-ARXIV-2605-24426:start -->We identify this structural gap as \emph{Agent-Environment Misalignment}: the agent's capability frontier changes during training, while the environment that provides supervision remains static or only weakly coupled to the agent's revealed failures.<!-- delta:SF-2026-ARXIV-2605-24426:end --> Independent decision=`Integrate`；owner_sha256=df76cc355aa8203c222d08d5ef206aedc1549bbadcbf2b404d0b341eac4694e8。
<!-- books-review:SF-2026-ARXIV-2605-24426:end -->

<!-- books-review:SF-2026-ARXIV-2605-24461:start -->
<!-- existing:SF-2026-ARXIV-2605-24461:start -->现有 scheduler 讨论 power-aware admission，但未贯通 design provisioning、rack validation、operational cap 与 runtime power swing 的责任交接。<!-- existing:SF-2026-ARXIV-2605-24461:end -->
<!-- delta:SF-2026-ARXIV-2605-24461:start -->We present detailed power measurements for a 150 MW datacenter hosting a cluster of 83K GB200 GPUs.<!-- delta:SF-2026-ARXIV-2605-24461:end --> Independent decision=`Integrate`；owner_sha256=f44097493dfbe426ed1dadf2e27d3f87e14068d7f9d96027f8fa7c8a51511b45。
<!-- books-review:SF-2026-ARXIV-2605-24461:end -->

<!-- books-review:SF-2026-ARXIV-2605-24468:start -->
<!-- existing:SF-2026-ARXIV-2605-24468:start -->现有章节已经由 raw immutable trajectory、derived cue、write/read policy、provenance 和 rollback 构成同一 memory lifecycle；SAM 未改变该 owner。<!-- existing:SF-2026-ARXIV-2605-24468:end -->
<!-- delta:SF-2026-ARXIV-2605-24468:start -->To this end, we propose State-Adaptive Memory~(SAM), a standalone framework that consolidates ongoing interaction into compact memory cues while preserving raw trajectory pages for intent-driven recall.<!-- delta:SF-2026-ARXIV-2605-24468:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=859029c176f33208548742c32d8bbd45836601858f6f8205cf7227795a2a6f51。
<!-- books-review:SF-2026-ARXIV-2605-24468:end -->

<!-- books-review:SF-2026-ARXIV-2605-24517:start -->
<!-- existing:SF-2026-ARXIV-2605-24517:start -->现有章节已明确 training-only observation/world-token auxiliary supervision 不等于 runtime world state；ECHO 是该边界内案例。<!-- existing:SF-2026-ARXIV-2605-24517:end -->
<!-- delta:SF-2026-ARXIV-2605-24517:start -->We introduce ECHO (Environment Cross-entropy Hybrid Objective), a hybrid objective that combines the standard policy-gradient loss on action tokens with an auxiliary loss that trains the policy to predict environment observation tokens resulting from its own actions.<!-- delta:SF-2026-ARXIV-2605-24517:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=8eba6188ba7b28ccead4779988e06a1e42eb7c8b638cc8e8319281251ae3446e。
<!-- books-review:SF-2026-ARXIV-2605-24517:end -->

<!-- books-review:SF-2026-ARXIV-2605-24547:start -->
<!-- existing:SF-2026-ARXIV-2605-24547:start -->现有 textual feedback 是静态 rubric/critic artifact；缺少以 policy return 为上层目标反向学习 feedback generator 的 bilevel control loop。<!-- existing:SF-2026-ARXIV-2605-24547:end -->
<!-- delta:SF-2026-ARXIV-2605-24547:start -->We formalize this coupling as a Stackelberg bilevel program and derive Bilevel Natural Language Actor-Critic (Bi-NAC), which jointly trains a critic to generate reward-improving feedback and an actor to exploit it.<!-- delta:SF-2026-ARXIV-2605-24547:end --> Independent decision=`Integrate`；owner_sha256=df76cc355aa8203c222d08d5ef206aedc1549bbadcbf2b404d0b341eac4694e8。
<!-- books-review:SF-2026-ARXIV-2605-24547:end -->

<!-- books-review:SF-2026-ARXIV-2605-24558:start -->
<!-- existing:SF-2026-ARXIV-2605-24558:start -->现有 Data 章已把 observation/measurement pipeline、schema/provenance 与 transformation version 纳入 dataset identity；position paper 未给出新的可验证接口。<!-- existing:SF-2026-ARXIV-2605-24558:end -->
<!-- delta:SF-2026-ARXIV-2605-24558:start -->\textbf{We argue that these measurement-to-dataset pipelines are inference components: treating their outputs as ``given data'' freezes an observation model and obscures uncertainty over feasible pipeline choices.} We identify three failure modes arising from this ``frozen lens'': \textbf{(C1) hidden hypothesis space}, where the released dataset does not specify the pipeline configuration or its validity conditions; \textbf{(C2) uncertified transportability}, where a pipeline may be documented but its regime of validity is untested, so failures under distribution shift cannot be adjudicated; \textbf{(C3) ungoverned multiplicity}, where many defensible pipelines exist and dispersion is real but not propagated into uncertainty-aware evidence.<!-- delta:SF-2026-ARXIV-2605-24558:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=0e382b1714d3c389d41845aaad046f5179c117a50d6c613102efed4b564f3755。
<!-- books-review:SF-2026-ARXIV-2605-24558:end -->

<!-- books-review:SF-2026-ARXIV-2605-24579:start -->
<!-- existing:SF-2026-ARXIV-2605-24579:start -->现有 Memory 章有 write/read 分离，却没有以 TFC/OE/CSM/RM 四个干预条件区分 reader ceiling、write loss 与 retrieval loss。<!-- existing:SF-2026-ARXIV-2605-24579:end -->
<!-- delta:SF-2026-ARXIV-2605-24579:start -->We introduce a four-condition diagnostic protocol that evaluates a fixed reader under truncated full context (TFC), oracle evidence (OE), complete stored memory (CSM), and retrieved memory (RM).<!-- delta:SF-2026-ARXIV-2605-24579:end --> Independent decision=`Integrate`；owner_sha256=859029c176f33208548742c32d8bbd45836601858f6f8205cf7227795a2a6f51。
<!-- books-review:SF-2026-ARXIV-2605-24579:end -->

<!-- books-review:SF-2026-ARXIV-2605-24583:start -->
<!-- existing:SF-2026-ARXIV-2605-24583:start -->现有 alignment evaluation 未把 prompt/template confound、mean-direction shift、effective-rank proxy 与 causal ablation 组织成可反驳的 activation audit。<!-- existing:SF-2026-ARXIV-2605-24583:end -->
<!-- delta:SF-2026-ARXIV-2605-24583:start -->We show the obvious way to form this matrix is confounded.<!-- delta:SF-2026-ARXIV-2605-24583:end --> Independent decision=`Integrate`；owner_sha256=ec7aa353d8c12a45a4efc02c1ff1a58c3e703f2e4ef5a2f308e43eb9e88be10e。
<!-- books-review:SF-2026-ARXIV-2605-24583:end -->

<!-- books-review:SF-2026-ARXIV-2605-24598:start -->
<!-- existing:SF-2026-ARXIV-2605-24598:start -->现有多 Agent 协调未覆盖 device/cloud step-level routing 在任务历史、成功概率、网络开销与 cost budget 下的可学习控制状态。<!-- existing:SF-2026-ARXIV-2605-24598:end -->
<!-- delta:SF-2026-ARXIV-2605-24598:start -->To address this issue, we present Hera, a step-level device--cloud LLM agent coordinator for long-horizon tasks achieving a strong performance--cost Pareto frontier.<!-- delta:SF-2026-ARXIV-2605-24598:end --> Independent decision=`Integrate`；owner_sha256=48b45443639518cec718da5a162973b920b5de48c6fb030e443c51b41e37000a。
<!-- books-review:SF-2026-ARXIV-2605-24598:end -->

<!-- books-review:SF-2026-ARXIV-2605-24614:start -->
<!-- existing:SF-2026-ARXIV-2605-24614:start -->现有 Evaluation 已覆盖 unlearning counterfactual/activation audit、多维 score、simulator feedback loop 与 release gate；对应 family 是已覆盖受限实例。<!-- existing:SF-2026-ARXIV-2605-24614:end -->
<!-- delta:SF-2026-ARXIV-2605-24614:start -->To address these limitations, we propose the Unlearning Depth Score (UDS), a metric that quantifies the mechanistic depth of unlearning via activation patching.<!-- delta:SF-2026-ARXIV-2605-24614:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=ec7aa353d8c12a45a4efc02c1ff1a58c3e703f2e4ef5a2f308e43eb9e88be10e。
<!-- books-review:SF-2026-ARXIV-2605-24614:end -->

<!-- books-review:SF-2026-ARXIV-2605-24619:start -->
<!-- existing:SF-2026-ARXIV-2605-24619:start -->现有章节已把 LLM proposal 与 deterministic/formal verifier 的 authority 分离；IC3Syn 未改变 commit owner。<!-- existing:SF-2026-ARXIV-2605-24619:end -->
<!-- delta:SF-2026-ARXIV-2605-24619:start -->We present IC3Syn, a neuro-symbolic framework that synthesizes inductive invariants by executing an IC3-style process over TLA+ states with the assistance of Large Language Models (LLMs).<!-- delta:SF-2026-ARXIV-2605-24619:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=fb79e1d1dc0522d217986d7a6df65191484bbc5d4ad827f59cbc2fbf9a80ba11。
<!-- books-review:SF-2026-ARXIV-2605-24619:end -->

<!-- books-review:SF-2026-ARXIV-2605-24657:start -->
<!-- existing:SF-2026-ARXIV-2605-24657:start -->现有 Context/Memory 已比较 compaction 与 durable learned state，并绑定 base/model revision；该 consolidation 实验未改变 owner。<!-- existing:SF-2026-ARXIV-2605-24657:end -->
<!-- delta:SF-2026-ARXIV-2605-24657:start -->Major LLM platforms deploy models in an inference-only configuration: the model serves requests but never updates per-user weights.<!-- delta:SF-2026-ARXIV-2605-24657:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=55db3e124881a0bcde65d0587c9c31fa32ada720f92e5a0fc530cbb77952a53d。
<!-- books-review:SF-2026-ARXIV-2605-24657:end -->

<!-- books-review:SF-2026-ARXIV-2605-24659:start -->
<!-- existing:SF-2026-ARXIV-2605-24659:start -->现有章节已覆盖 indirect injection、adaptive adversary、tool/output boundary 与 defense-in-depth；IterInject 是攻击搜索增强，不是新的生产防御契约。<!-- existing:SF-2026-ARXIV-2605-24659:end -->
<!-- delta:SF-2026-ARXIV-2605-24659:start -->We introduce \oursys, a feedback-guided iterative framework that closes the loop between injection, diagnosis, and refinement: a rule-based diagnoser produces structured outcome labels with behavioral descriptions, and an LLM-based optimizer refines payloads conditioned on the full optimization history.<!-- delta:SF-2026-ARXIV-2605-24659:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=ef7882199869af53c1d9715b6343b35023fff4e4a578647be098c6dbdd21cf0e。
<!-- books-review:SF-2026-ARXIV-2605-24659:end -->

<!-- books-review:SF-2026-ARXIV-2605-24660:start -->
<!-- existing:SF-2026-ARXIV-2605-24660:start -->现有 tool shortlist 没有用 chance-corrected information gain 把 candidate-set size 与 random baseline 从 tool exposure reward 中扣除。<!-- existing:SF-2026-ARXIV-2605-24660:end -->
<!-- delta:SF-2026-ARXIV-2605-24660:start -->Before an LLM agent can use a tool, a retrieval system must decide which candidate tools to show to the agent.<!-- delta:SF-2026-ARXIV-2605-24660:end --> Independent decision=`Integrate`；owner_sha256=3deca1b35edccc646c1982cea7dd44ce99b94d42a6052e4a581d9ef9007f2bf9。
<!-- books-review:SF-2026-ARXIV-2605-24660:end -->

<!-- books-review:SF-2026-ARXIV-2605-24661:start -->
<!-- existing:SF-2026-ARXIV-2605-24661:start -->现有 Evaluation 已覆盖 unlearning counterfactual/activation audit、多维 score、simulator feedback loop 与 release gate；对应 family 是已覆盖受限实例。<!-- existing:SF-2026-ARXIV-2605-24661:end -->
<!-- delta:SF-2026-ARXIV-2605-24661:start -->Despite remarkable progress on reasoning benchmarks, current LLM evaluation practice remains anchored to final-answer correctness, providing limited insight into how models reason, how reliably they behave under contextual variation, or how efficiently they reach conclusions.<!-- delta:SF-2026-ARXIV-2605-24661:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=ec7aa353d8c12a45a4efc02c1ff1a58c3e703f2e4ef5a2f308e43eb9e88be10e。
<!-- books-review:SF-2026-ARXIV-2605-24661:end -->

<!-- books-review:SF-2026-ARXIV-2605-24662:start -->
<!-- existing:SF-2026-ARXIV-2605-24662:start -->现有 Evaluation 已覆盖 unlearning counterfactual/activation audit、多维 score、simulator feedback loop 与 release gate；对应 family 是已覆盖受限实例。<!-- existing:SF-2026-ARXIV-2605-24662:end -->
<!-- delta:SF-2026-ARXIV-2605-24662:start -->To fill this gap, we present OpenTwin, a closed-loop framework that learns the simulator configuration reproducing an operating deployment streamed measurements, certifies the resulting DT by re-simulation, calibrates it online, and evaluates each xApp action before it executes on the physical network.<!-- delta:SF-2026-ARXIV-2605-24662:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=ec7aa353d8c12a45a4efc02c1ff1a58c3e703f2e4ef5a2f308e43eb9e88be10e。
<!-- books-review:SF-2026-ARXIV-2605-24662:end -->

<!-- books-review:SF-2026-ARXIV-2605-24667:start -->
<!-- existing:SF-2026-ARXIV-2605-24667:start -->现有 pretraining 以 mean CE 为主，没有记录 heavy-tail token loss 下 median CE/mean CE 与 downstream quality 的 concordance regime。<!-- existing:SF-2026-ARXIV-2605-24667:end -->
<!-- delta:SF-2026-ARXIV-2605-24667:start -->Mean cross-entropy is the standard validation metric for language models, but it can fail to track model quality during training.<!-- delta:SF-2026-ARXIV-2605-24667:end --> Independent decision=`Integrate`；owner_sha256=7ed3a8bde8bbf14b9d742176e34c931da3630528bbad900256f07bdc2df3e9c7。
<!-- books-review:SF-2026-ARXIV-2605-24667:end -->

<!-- books-review:SF-2026-ARXIV-2605-24683:start -->
<!-- existing:SF-2026-ARXIV-2605-24683:start -->现有 monitoring 假设 topology/asset identity 可得；缺少 fragmented admin domain 下 deterministic L2 ground truth、integrity loop 与 HIL admission。<!-- existing:SF-2026-ARXIV-2605-24683:end -->
<!-- delta:SF-2026-ARXIV-2605-24683:start -->Modern AIOps environments operating within multi-campus institutional infrastructures suffer acutely from topological drift and black-box unmanaged physical network segments.<!-- delta:SF-2026-ARXIV-2605-24683:end --> Independent decision=`Integrate`；owner_sha256=b61889e5ef350937dfc6eaff0029815bd5239105a48de2145e51210c0673919a。
<!-- books-review:SF-2026-ARXIV-2605-24683:end -->

<!-- books-review:SF-2026-ARXIV-2605-24697:start -->
<!-- existing:SF-2026-ARXIV-2605-24697:start -->现有 diffusion commit 比较 confidence/block schedule，未包含从 future stability trace 学习 token-local commitment policy 与动态 threshold 的分支。<!-- existing:SF-2026-ARXIV-2605-24697:end -->
<!-- delta:SF-2026-ARXIV-2605-24697:start -->We introduce TraceLock, a lightweight plug-in controller that instantiates this policy for a frozen diffusion language model.<!-- delta:SF-2026-ARXIV-2605-24697:end --> Independent decision=`Integrate`；owner_sha256=82d67a82821a384369ee36c24794db1b14bdfd6d538877525c38e9420761df30。
<!-- books-review:SF-2026-ARXIV-2605-24697:end -->

<!-- books-review:SF-2026-ARXIV-2605-24709:start -->
<!-- existing:SF-2026-ARXIV-2605-24709:start -->现有 RL loop 多按完整 trajectory 更新；缺少 partial observation 下 recurrent hidden/eligibility state 的 per-step exact online update ownership。<!-- existing:SF-2026-ARXIV-2605-24709:end -->
<!-- delta:SF-2026-ARXIV-2605-24709:start -->We close this gap using recurrent trace units, a diagonal recurrent architecture that enables exact RTRL with linear time and memory complexity in the parameter count, and show that they integrate cleanly into existing streaming algorithms across both discrete and continuous control.<!-- delta:SF-2026-ARXIV-2605-24709:end --> Independent decision=`Integrate`；owner_sha256=df76cc355aa8203c222d08d5ef206aedc1549bbadcbf2b404d0b341eac4694e8。
<!-- books-review:SF-2026-ARXIV-2605-24709:end -->

<!-- books-review:SF-2026-ARXIV-2605-24727:start -->
<!-- existing:SF-2026-ARXIV-2605-24727:start -->现有 explainability/evidence 章节未显式给出 fidelity、completeness、human comprehensibility 与 universal applicability 不可同时保证的 claim boundary。<!-- existing:SF-2026-ARXIV-2605-24727:end -->
<!-- delta:SF-2026-ARXIV-2605-24727:start -->In this paper, we mathematically prove a fundamental quadrilemma in explaining AI, stating that AI and its explanation cannot satisfy the following four conditions simultaneously: 1) the complexity of the operation environment, 2) the goodness of the AI's performance, 3) the interpretability of the AI's explanation, and 4) the complete faithfulness of the AI's explanation.<!-- delta:SF-2026-ARXIV-2605-24727:end --> Independent decision=`Integrate`；owner_sha256=ec7aa353d8c12a45a4efc02c1ff1a58c3e703f2e4ef5a2f308e43eb9e88be10e。
<!-- books-review:SF-2026-ARXIV-2605-24727:end -->

<!-- books-review:SF-2026-ARXIV-2605-24728:start -->
<!-- existing:SF-2026-ARXIV-2605-24728:start -->当前 owner 与相邻章节已覆盖同一长期 mechanism、identity、trade-off 与 fallback；该 exact-v1 仅提供受限实例。<!-- existing:SF-2026-ARXIV-2605-24728:end -->
<!-- delta:SF-2026-ARXIV-2605-24728:start -->A generated object or environment becomes useful to an agent only when the system can identify its entities, frames, surfaces, constraints, provenance, admissible actions, expected effects, and validation failures.<!-- delta:SF-2026-ARXIV-2605-24728:end --> Independent decision=`Structural Candidate`；owner_sha256=a78e439d8d301c686575bc38f307852352bf950dc9a3066df7fa01fb6734131b。
<!-- books-review:SF-2026-ARXIV-2605-24728:end -->

<!-- books-review:SF-2026-ARXIV-2605-24733:start -->
<!-- existing:SF-2026-ARXIV-2605-24733:start -->现有章节已经以 evidence gap、typed verification failure 与 selective rerun 组织 reflection；StepGap 是 NLI/LLM 实现实例。<!-- existing:SF-2026-ARXIV-2605-24733:end -->
<!-- delta:SF-2026-ARXIV-2605-24733:start -->We present \textbf{StepGap}, a hybrid NLI-LLM decision tree that detects step-level evidence gaps in multi-hop QA and emits one of three typed labels: \textsc{Contradicted Claim} (CC), \textsc{Irrelevant Evidence} (IE), or \textsc{Missing Bridge} (MB), each tied to a concrete repair action.<!-- delta:SF-2026-ARXIV-2605-24733:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=c1293a34a41ce0c0ee8d27ebdb10d68cada38430db2d77545ddb7873abd6fe08。
<!-- books-review:SF-2026-ARXIV-2605-24733:end -->

<!-- books-review:SF-2026-ARXIV-2605-24737:start -->
<!-- existing:SF-2026-ARXIV-2605-24737:start -->现有 monitoring 已覆盖 policy-bound sensor、versioned metric、continuous compliance 与 unknown propagation；govllm 未改变 owner。<!-- existing:SF-2026-ARXIV-2605-24737:end -->
<!-- delta:SF-2026-ARXIV-2605-24737:start -->Current approaches to AI compliance treat conformity as a binary, audit-time verdict rather than a continuous, measurable property of production systems.<!-- delta:SF-2026-ARXIV-2605-24737:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=b61889e5ef350937dfc6eaff0029815bd5239105a48de2145e51210c0673919a。
<!-- books-review:SF-2026-ARXIV-2605-24737:end -->

<!-- books-review:SF-2026-ARXIV-2605-24743:start -->
<!-- existing:SF-2026-ARXIV-2605-24743:start -->现有 synthetic-data admission 未表达由 held-out real trajectory loss 反向拥有每条 multi-turn synthetic trajectory weight 的 bilevel选择。<!-- existing:SF-2026-ARXIV-2605-24743:end -->
<!-- delta:SF-2026-ARXIV-2605-24743:start -->We propose BOOST, a bilevel optimization framework where the inner level trains the LLM on reweighted data and the outer level trains a lightweight reweighting head on held-out real validation tasks, assigning continuous trajectory-level weights without requiring an external judge.<!-- delta:SF-2026-ARXIV-2605-24743:end --> Independent decision=`Integrate`；owner_sha256=0e382b1714d3c389d41845aaad046f5179c117a50d6c613102efed4b564f3755。
<!-- books-review:SF-2026-ARXIV-2605-24743:end -->

<!-- books-review:SF-2026-ARXIV-2605-24749:start -->
<!-- existing:SF-2026-ARXIV-2605-24749:start -->现有 reward model 评价未把 training distribution 的 prediction error 与 reward-tilted deployment distribution 的 policy value gap分开。<!-- existing:SF-2026-ARXIV-2605-24749:end -->
<!-- delta:SF-2026-ARXIV-2605-24749:start -->We study this feedback in a Gaussian single-index model with $r^*(x) = σ^*(\langle θ^*, x\rangle)$ and $x \sim N(0, I_d)$.<!-- delta:SF-2026-ARXIV-2605-24749:end --> Independent decision=`Integrate`；owner_sha256=df76cc355aa8203c222d08d5ef206aedc1549bbadcbf2b404d0b341eac4694e8。
<!-- books-review:SF-2026-ARXIV-2605-24749:end -->

<!-- books-review:SF-2026-ARXIV-2605-24756:start -->
<!-- existing:SF-2026-ARXIV-2605-24756:start -->现有 proper scoring 主要针对 outcome/confidence；缺少带 early termination/censoring 的整条 agent trajectory 的严格 proper score。<!-- existing:SF-2026-ARXIV-2605-24756:end -->
<!-- delta:SF-2026-ARXIV-2605-24756:start -->Building on prequential proper scoring, we introduce the Trajectory Proper Score (TPS), a predictor-agnostic family of strictly proper trajectory-level scoring rules for any per-step uncertainty signal calibrated into a probability of eventual success.<!-- delta:SF-2026-ARXIV-2605-24756:end --> Independent decision=`Integrate`；owner_sha256=ec7aa353d8c12a45a4efc02c1ff1a58c3e703f2e4ef5a2f308e43eb9e88be10e。
<!-- books-review:SF-2026-ARXIV-2605-24756:end -->

<!-- books-review:SF-2026-ARXIV-2605-24770:start -->
<!-- existing:SF-2026-ARXIV-2605-24770:start -->现有 Muon 机制讨论 update geometry，但未把 augmentation/mixing/smoothing recipe 与 gradient spectrum 共同纳入 optimizer recipe identity。<!-- existing:SF-2026-ARXIV-2605-24770:end -->
<!-- delta:SF-2026-ARXIV-2605-24770:start -->We study Muon for ViT training, largely on ImageNet-100 and Pl@ntNet-300K, comparing against AdamW under standard vision recipes involving mixup, cutmix, smoothing, and random augmentation and erasing.<!-- delta:SF-2026-ARXIV-2605-24770:end --> Independent decision=`Integrate`；owner_sha256=7ed3a8bde8bbf14b9d742176e34c931da3630528bbad900256f07bdc2df3e9c7。
<!-- books-review:SF-2026-ARXIV-2605-24770:end -->

<!-- books-review:SF-2026-ARXIV-2605-24775:start -->
<!-- existing:SF-2026-ARXIV-2605-24775:start -->现有章节已覆盖 verifiable identity、delegation、convergence feedback、append-only state 与 branch/merge；PRIMA 是同构 pattern bundle。<!-- existing:SF-2026-ARXIV-2605-24775:end -->
<!-- delta:SF-2026-ARXIV-2605-24775:start -->We present PRIMA, whose primary contributions are three operational patterns for surviving these failure modes: (1) a resilience-and-recovery layer that detects upstream rate-limit signals, persists a typed pause record to disk, and resumes long-running runs without re-executing converged work even across process restarts; (2) a sub-agent operating discipline encoding task-fidelity, tool-use, revision, and inter-step context-boundary norms as a structural prompt layer; (3) a multi-phase application pattern for structured engineering deliverables pairing orthogonal draft steps with an explicit cross-document harmonization pass before final synthesis.<!-- delta:SF-2026-ARXIV-2605-24775:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=48b45443639518cec718da5a162973b920b5de48c6fb030e443c51b41e37000a。
<!-- books-review:SF-2026-ARXIV-2605-24775:end -->

<!-- books-review:SF-2026-ARXIV-2605-24785:start -->
<!-- existing:SF-2026-ARXIV-2605-24785:start -->现有 Agent Platform 已拥有 skill distillation、promotion、drift、rollback 与 lifecycle evidence；PANDO 的 web-agent实验不改变该 contract。<!-- existing:SF-2026-ARXIV-2605-24785:end -->
<!-- delta:SF-2026-ARXIV-2605-24785:start -->We first analyze trajectories from VisualWebArena and identify three recurring sources of inefficiency: repeat-action loops, hidden discovery costs, and low prompt-cache reuse.<!-- delta:SF-2026-ARXIV-2605-24785:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=fb79e1d1dc0522d217986d7a6df65191484bbc5d4ad827f59cbc2fbf9a80ba11。
<!-- books-review:SF-2026-ARXIV-2605-24785:end -->

<!-- books-review:SF-2026-ARXIV-2605-24786:start -->
<!-- existing:SF-2026-ARXIV-2605-24786:start -->现有 KV 章已拥有 confidence-aware mixed precision、budget/eviction、estimator drift 和 FullKV fallback；CONF-KV 属已覆盖分支。<!-- existing:SF-2026-ARXIV-2605-24786:end -->
<!-- delta:SF-2026-ARXIV-2605-24786:start -->We introduce CONF-KV, a KV-cache manager that converts the next-token distribution into a scalar confidence score and uses it to choose the per-step cache budget, retaining more context when the model is uncertain and pruning aggressively when it is confident.<!-- delta:SF-2026-ARXIV-2605-24786:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=322a087f0629a6acc48fc085f83172b753f8fa38a54f182e7b9d5f8d36b02348。
<!-- books-review:SF-2026-ARXIV-2605-24786:end -->

<!-- books-review:SF-2026-ARXIV-2605-24793:start -->
<!-- existing:SF-2026-ARXIV-2605-24793:start -->现有 speculation 以 target exactness 为 commit contract；缺少 draft 可能优于 target 时由 utility-aware arbitrator 拥有非 exact commit 的 alternative branch。<!-- existing:SF-2026-ARXIV-2605-24793:end -->
<!-- delta:SF-2026-ARXIV-2605-24793:start -->Speculative decoding (SPD) accelerates large language model (LLM) inference by letting a smaller draft model propose multiple future tokens that are verified in parallel by a larger target model.<!-- delta:SF-2026-ARXIV-2605-24793:end --> Independent decision=`Integrate`；owner_sha256=63abd49ea9f1fc8cb365512ea7b41f59d786879ec3603ab77545700307a29ce8。
<!-- books-review:SF-2026-ARXIV-2605-24793:end -->

<!-- books-review:SF-2026-ARXIV-2605-24817:start -->
<!-- existing:SF-2026-ARXIV-2605-24817:start -->已顺读 `books/part-06-ai-infrastructure/67-monitoring.md` 及相邻章节 ['books/part-06-ai-infrastructure/66-evaluation-system.md', 'books/part-06-ai-infrastructure/68-logging.md']；当前主干=['本章要回答的问题', '先定义目标，再选择可测信号', 'Context generator 是 pre-failure sensor identity 的一部分', 'Review notes', '四层指标', 'Autonomy 不是一个纯模型指标', '从单次 Query 指标到 Session-level Search Trajectory Sensor', 'Rate、Errors、Duration 与 Saturation']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-24817:end -->
<!-- delta:SF-2026-ARXIV-2605-24817:start -->Inspired by this observation, we propose RouteScan, a non-intrusive auditing framework for detecting harmful behaviors through such routing-induced GPU telemetry.<!-- delta:SF-2026-ARXIV-2605-24817:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-24817:end -->

<!-- books-review:SF-2026-ARXIV-2605-24818:start -->
<!-- existing:SF-2026-ARXIV-2605-24818:start -->Ch27/Ch66 已有 contamination identity、decontamination 与 release evidence，但没有用主动已知污染率拟合 score-correction curve。<!-- existing:SF-2026-ARXIV-2605-24818:end -->
<!-- delta:SF-2026-ARXIV-2605-24818:start -->在已知比例主动注入 benchmark 样本并拟合 contamination-response curve，把污染校正从事后猜测变成带干预记录的 evaluation protocol。<!-- delta:SF-2026-ARXIV-2605-24818:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-24818:end -->

<!-- books-review:SF-2026-ARXIV-2605-24823:start -->
<!-- existing:SF-2026-ARXIV-2605-24823:start -->已顺读 `books/part-07-agent/84-agent-platform.md` 及相邻章节 ['books/part-07-agent/83-mcp.md', 'books/part-07-agent/README.md']；当前主干=['本章要回答的问题', 'Agent 改变了平台的控制对象', 'Serving 结束不等于 Agent 任务结束', 'Agent Definition 与 Run Identity', '可复用 Skill 不是一个 Prompt 文件', '从 Skill Catalog 到 Competence-aware Orchestration', '从 Trajectory 到 Skill 是一次受治理的 Compilation', 'Skill Compiler 必须绑定 Target Profile，而不是只绑定模型名']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-24823:end -->
<!-- delta:SF-2026-ARXIV-2605-24823:start -->Manufacturing has passed through four widely recognized paradigms - mechanization, electrification, programmable automation, and Smart Manufacturing - each defined by the kind of work it shifted from humans to machines.<!-- delta:SF-2026-ARXIV-2605-24823:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-24823:end -->

<!-- books-review:SF-2026-ARXIV-2605-24832:start -->
<!-- existing:SF-2026-ARXIV-2605-24832:start -->已顺读 `books/part-05-inference-system/49-tensorrt-llm.md` 及相邻章节 ['books/part-05-inference-system/48-speculative-decoding.md', 'books/part-05-inference-system/50-vllm.md']；当前主干=['本章要回答的问题', '从计算图开始', '三类基础优化', 'Execution Plan 可以修订，但只能在安全边界 Commit', '异步工作不必永久绑定固定 Physical Core', '从粗粒度 Offload 到负载观测的 Tensor Placement', 'Backend Choice 必须携带 Previous-backend State', 'Accelerator Readiness 是 Phase × Shape × Offload × Host-control Contract']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-24832:end -->
<!-- delta:SF-2026-ARXIV-2605-24832:start -->We present Optimus, a serving system that enables elastic decoding for diffusion LLMs by dynamically adapting decoding granularity to runtime load.<!-- delta:SF-2026-ARXIV-2605-24832:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-24832:end -->

<!-- books-review:SF-2026-ARXIV-2605-24870:start -->
<!-- existing:SF-2026-ARXIV-2605-24870:start -->Ch24 已有 sensitivity/error-budget cache 与 recompute fallback，但没有把 calibration prior 绑定到被先前 correction 改写后的 denoising trajectory。<!-- existing:SF-2026-ARXIV-2605-24870:end -->
<!-- delta:SF-2026-ARXIV-2605-24870:start -->把 diffusion cache 的误差从单点 representation mismatch 扩展为会被先前校准继续改写的 trajectory state，并沿 corrected history 逐步拟合 site-local calibration prior。<!-- delta:SF-2026-ARXIV-2605-24870:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-24870:end -->

<!-- books-review:SF-2026-ARXIV-2605-24879:start -->
<!-- existing:SF-2026-ARXIV-2605-24879:start -->Ch72 已要求 DP sampling/clipping/noise/accounting 实现等价，却没有覆盖 randomized norm estimator 改变 clipping mechanism 后必须配套重建 accountant 与资源合同。<!-- existing:SF-2026-ARXIV-2605-24879:end -->
<!-- delta:SF-2026-ARXIV-2605-24879:start -->用 Hutchinson/Hutch++ 随机 trace estimation 近似 per-sample gradient norm，把 DP clipping 的显存复杂度从显式 T×T 或 d×d 中间量改为受投影维度控制的 estimator，并为随机 clipping 单独建立 privacy accountant。<!-- delta:SF-2026-ARXIV-2605-24879:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-24879:end -->

<!-- books-review:SF-2026-ARXIV-2605-24883:start -->
<!-- existing:SF-2026-ARXIV-2605-24883:start -->Ch66/Ch72 已有 red-team、policy revision 与独立 guard，但没有从 policy predicate graph 生成 coverage-traceable tests。<!-- existing:SF-2026-ARXIV-2605-24883:end -->
<!-- delta:SF-2026-ARXIV-2605-24883:start -->把自然语言 safety policy 编译为形式化谓词和语义图，再从未覆盖路径生成可追踪测试，使 policy revision、test identity 与 coverage evidence 成为同一评估对象。<!-- delta:SF-2026-ARXIV-2605-24883:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-24883:end -->

<!-- books-review:SF-2026-ARXIV-2605-24892:start -->
<!-- existing:SF-2026-ARXIV-2605-24892:start -->Ch25 已有 transition-token reasoner、appearance renderer、多时间尺度状态和 closed-loop evidence boundary。<!-- existing:SF-2026-ARXIV-2605-24892:end -->
<!-- delta:SF-2026-ARXIV-2605-24892:start -->把低熵相邻帧预测改成跨语义时间块的自回归 future-state 预测：块内保留稠密瞬时动态、块间保留稀疏长程因果，并把 action/latent prediction 与多视角 renderer 分责。<!-- delta:SF-2026-ARXIV-2605-24892:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-24892:end -->

<!-- books-review:SF-2026-ARXIV-2605-24914:start -->
<!-- existing:SF-2026-ARXIV-2605-24914:start -->已顺读 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 及相邻章节 ['books/part-05-inference-system/44-decode.md', 'books/part-05-inference-system/46-continuous-batching.md']；当前主干=['本章要回答的问题', '如果完全不缓存', '为什么缓存 K/V 而不是 Query', '逻辑 Shape 与容量公式', '一个容量小例子', 'KV Cache 的生命周期', 'Segmented Execution 必须在训练与推理共享同一语义', 'Prefix reuse']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-24914:end -->
<!-- delta:SF-2026-ARXIV-2605-24914:start -->To reduce LLM costs and latency, semantic caching systems must accurately identify when a new prompt matches a cached one.<!-- delta:SF-2026-ARXIV-2605-24914:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-24914:end -->

<!-- books-review:SF-2026-ARXIV-2605-24922:start -->
<!-- existing:SF-2026-ARXIV-2605-24922:start -->Ch25/Ch26 已有 simulator/observed-state authority 与 rollback，但没有 executor-owned per-environment persistent batched runtime lifecycle。<!-- existing:SF-2026-ARXIV-2605-24922:end -->
<!-- delta:SF-2026-ARXIV-2605-24922:start -->把 stateless rollout 调用提升为 executor-owned persistent environment pool，使 per-environment model/data、reset、step 与 Jacobian state 在 batched robot-learning loop 中保持可寻址。<!-- delta:SF-2026-ARXIV-2605-24922:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-24922:end -->

<!-- books-review:SF-2026-ARXIV-2605-24930:start -->
<!-- existing:SF-2026-ARXIV-2605-24930:start -->Ch22 已有 coarse global summary、query-aware hierarchical sparse selection、selector miss 与 dense fallback。<!-- existing:SF-2026-ARXIV-2605-24930:end -->
<!-- delta:SF-2026-ARXIV-2605-24930:start -->先把长文档组织成语义树，再用层级 memory tokens 与 query-aware routing 在粗摘要和细粒度节点间分配注意力预算。<!-- delta:SF-2026-ARXIV-2605-24930:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-24930:end -->

<!-- books-review:SF-2026-ARXIV-2605-24941:start -->
<!-- existing:SF-2026-ARXIV-2605-24941:start -->已顺读 `books/part-07-agent/78-tool-calling.md` 及相邻章节 ['books/part-07-agent/77-memory.md', 'books/part-07-agent/79-planning.md']；当前主干=['本章要回答的问题', '从生成文本到环境转移', 'Tool Contract', '模型输出只是 Proposal', '编译器反馈可以前移，但仍是受限 Authority', 'Tool Discovery 与选择', 'Interface Granularity：不是 Tool 越多越有能力', 'Agent-friendly Tool 不等于把 CLI 包一层']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-24941:end -->
<!-- delta:SF-2026-ARXIV-2605-24941:start -->We study a previously unexamined failure of this combination: when personality-driven biases stored in memory (cost-consciousness, impatience, risk tolerance, etc.) silently affect tool calls in contexts where they are not applicable.<!-- delta:SF-2026-ARXIV-2605-24941:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-24941:end -->

<!-- books-review:SF-2026-ARXIV-2605-24973:start -->
<!-- existing:SF-2026-ARXIV-2605-24973:start -->Ch76 已有 document/page/region provenance 与 ingestion identity，但没有跨页结构修复、chunk synchronization 及原页 fallback 的同一 lifecycle。<!-- existing:SF-2026-ARXIV-2605-24973:end -->
<!-- delta:SF-2026-ARXIV-2605-24973:start -->在 page OCR 之后增加 document-level state owner，跨页合并段落/表格并同步 chunk 与结构索引，使 ingestion 输出可被 RAG 以同一 document revision 消费。<!-- delta:SF-2026-ARXIV-2605-24973:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-24973:end -->

<!-- books-review:SF-2026-ARXIV-2605-25002:start -->
<!-- existing:SF-2026-ARXIV-2605-25002:start -->已顺读 `books/part-07-agent/77-memory.md` 及相邻章节 ['books/part-07-agent/76-rag.md', 'books/part-07-agent/78-tool-calling.md']；当前主干=['本章要回答的问题', 'Context 与 Memory 的状态边界', 'Memory 类型是用途，不只是存储介质', 'Memory Write 是高风险决策', 'Write / Hold 不足以定义下一状态', '从 Outcome Reward 到 Content-level Credit：归因只能约束写入，不能成为真值', 'Memory Read 是受约束检索', '从按需读取到选择性主动干预']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25002:end -->
<!-- delta:SF-2026-ARXIV-2605-25002:start -->We propose MemMark, a state-evolution attribution watermark that embeds an owner-controlled signal into latent memory-write decisions.<!-- delta:SF-2026-ARXIV-2605-25002:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-25002:end -->

<!-- books-review:SF-2026-ARXIV-2605-25052:start -->
<!-- existing:SF-2026-ARXIV-2605-25052:start -->已顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 及相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前主干=['本章要回答的问题', '为什么“选一个分数”不是评估系统', 'HTTP 成功只是质量判断的第一道门', '从目标到证据，而不是从指标到目标', '第一个不变量：评估声明必须绑定完整对象', 'Evaluation Identity 必须包含 Harness 与 Environment', '第二个不变量：评估结论总是相对于分布', '平均值、切片与不确定性']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25052:end -->
<!-- delta:SF-2026-ARXIV-2605-25052:start -->Building on this methodology, we present BonaFide, a benchmark of 3,066 labeled CoTs across 13 tasks and 10 models, and use it to conduct the first systematic evaluation of prominent faithfulness metrics.<!-- delta:SF-2026-ARXIV-2605-25052:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-25052:end -->

<!-- books-review:SF-2026-ARXIV-2605-25073:start -->
<!-- existing:SF-2026-ARXIV-2605-25073:start -->Ch72 已沿 data/supply-chain、training update、adapter artifact、runtime monitor 与 release Gate 组织 fine-tuning security lifecycle。<!-- existing:SF-2026-ARXIV-2605-25073:end -->
<!-- delta:SF-2026-ARXIV-2605-25073:start -->把 fine-tuning attack surface 按 pre-tuning input/supply chain、during-tuning optimizer/update 与 post-tuning adapter/artifact 三个 intervention phase 组织，并用同一基座和协议检查跨 phase 防御组合。<!-- delta:SF-2026-ARXIV-2605-25073:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-25073:end -->

<!-- books-review:SF-2026-ARXIV-2605-25077:start -->
<!-- existing:SF-2026-ARXIV-2605-25077:start -->已顺读 `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 及相邻章节 ['books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md', 'books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md']；当前主干=['本章要回答的问题', '从三个容易混淆的对象开始', 'Video generation', 'Predictive environment model', 'Controllable world model', '在谈 State 之前，先声明预测 Channel', '为什么旧的 Simulator 仍然合理', '演进路线']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25077:end -->
<!-- delta:SF-2026-ARXIV-2605-25077:start -->We present WorldCraft, a framework that expands interactive video world models from camera navigation to object-level trajectory actions.<!-- delta:SF-2026-ARXIV-2605-25077:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-25077:end -->

<!-- books-review:SF-2026-ARXIV-2605-25085:start -->
<!-- existing:SF-2026-ARXIV-2605-25085:start -->已顺读 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 及相邻章节 ['books/part-05-inference-system/44-decode.md', 'books/part-05-inference-system/46-continuous-batching.md']；当前主干=['本章要回答的问题', '如果完全不缓存', '为什么缓存 K/V 而不是 Query', '逻辑 Shape 与容量公式', '一个容量小例子', 'KV Cache 的生命周期', 'Segmented Execution 必须在训练与推理共享同一语义', 'Prefix reuse']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25085:end -->
<!-- delta:SF-2026-ARXIV-2605-25085:start -->We study the rate-distortion limits of online KV cache compression in autoregressive language models, formulating it as sequential Wyner-Ziv source coding on the filtration induced by the model, with the next-step query as decoder side information.<!-- delta:SF-2026-ARXIV-2605-25085:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-25085:end -->

<!-- books-review:SF-2026-ARXIV-2605-25092:start -->
<!-- existing:SF-2026-ARXIV-2605-25092:start -->已顺读 `books/part-07-agent/77-memory.md` 及相邻章节 ['books/part-07-agent/76-rag.md', 'books/part-07-agent/78-tool-calling.md']；当前主干=['本章要回答的问题', 'Context 与 Memory 的状态边界', 'Memory 类型是用途，不只是存储介质', 'Memory Write 是高风险决策', 'Write / Hold 不足以定义下一状态', '从 Outcome Reward 到 Content-level Credit：归因只能约束写入，不能成为真值', 'Memory Read 是受约束检索', '从按需读取到选择性主动干预']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25092:end -->
<!-- delta:SF-2026-ARXIV-2605-25092:start -->Long-term conversational memory is a retrieval workload classical IR was not built for: the index grows during the query stream, query types shift intra-session, and the latency budget per retrieval is sub-10 ms.<!-- delta:SF-2026-ARXIV-2605-25092:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-25092:end -->

<!-- books-review:SF-2026-ARXIV-2605-25133:start -->
<!-- existing:SF-2026-ARXIV-2605-25133:start -->已顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 及相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前主干=['本章要回答的问题', '为什么“选一个分数”不是评估系统', 'HTTP 成功只是质量判断的第一道门', '从目标到证据，而不是从指标到目标', '第一个不变量：评估声明必须绑定完整对象', 'Evaluation Identity 必须包含 Harness 与 Environment', '第二个不变量：评估结论总是相对于分布', '平均值、切片与不确定性']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25133:end -->
<!-- delta:SF-2026-ARXIV-2605-25133:start -->We introduce prover-verifier deliberation (PVD), an inference-time protocol grounded in interactive proof theory, as a mechanism for selective prediction: the protocol produces both an answer and a structured confidence verdict, allowing a system to report high-confidence answers while abstaining on uncertain cases.<!-- delta:SF-2026-ARXIV-2605-25133:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-25133:end -->

<!-- books-review:SF-2026-ARXIV-2605-25160:start -->
<!-- existing:SF-2026-ARXIV-2605-25160:start -->Ch66/Ch81 已把 generated environment、task constraint、validator、marker 与真实 backend authority 分开。<!-- existing:SF-2026-ARXIV-2605-25160:end -->
<!-- delta:SF-2026-ARXIV-2605-25160:start -->由 coding agent 合成可执行 mobile-app simulator，再独立生成 task 与 state validator，把 GUI agent benchmark 的 environment 和 outcome evidence 版本化。<!-- delta:SF-2026-ARXIV-2605-25160:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-25160:end -->

<!-- books-review:SF-2026-ARXIV-2605-25188:start -->
<!-- existing:SF-2026-ARXIV-2605-25188:start -->已顺读 `books/part-07-agent/82-multi-agent.md` 及相邻章节 ['books/part-07-agent/81-workflow.md', 'books/part-07-agent/83-mcp.md']；当前主干=['本章要回答的问题', '先建立单 Agent Baseline', '扩展 Agent 数量之前，先测量 Coordination Tax', '什么时候分解有意义', '典型拓扑', 'Topology 从部署前选择演进到运行时有界修复', '通信可以压缩成 latent，但 contract 不能一起消失', 'Behavioral belief 不等于 authenticated identity']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25188:end -->
<!-- delta:SF-2026-ARXIV-2605-25188:start -->Multi-agent LLM systems improve reasoning by combining outputs from multiple agents, but interaction-heavy methods can introduce error propagation and high communication overhead.<!-- delta:SF-2026-ARXIV-2605-25188:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-25188:end -->

<!-- books-review:SF-2026-ARXIV-2605-25189:start -->
<!-- existing:SF-2026-ARXIV-2605-25189:start -->已顺读 `books/part-04-training-system/31-rlhf.md` 及相邻章节 ['books/part-04-training-system/30-lora.md', 'books/part-04-training-system/32-ppo.md']；当前主干=['本章要回答的问题', 'Demonstration 为什么不足以表达偏好', 'RLHF 的完整 pipeline', 'Reward Model 怎样学习相对判断', '一个 preference score 小例子', 'Preference data 的难点不只是数量', '从 Reward 到 Policy objective', '改变输出分布是目标，不是无副作用的偏好标签']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25189:end -->
<!-- delta:SF-2026-ARXIV-2605-25189:start -->We study this failure mode through the geometry of reinforcement learning updates in language models and argue that hacking emerges when optimization drifts away from a stable low-dimensional learning trajectory.<!-- delta:SF-2026-ARXIV-2605-25189:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-25189:end -->

<!-- books-review:SF-2026-ARXIV-2605-25233:start -->
<!-- existing:SF-2026-ARXIV-2605-25233:start -->已顺读 `books/part-07-agent/82-multi-agent.md` 及相邻章节 ['books/part-07-agent/81-workflow.md', 'books/part-07-agent/83-mcp.md']；当前主干=['本章要回答的问题', '先建立单 Agent Baseline', '扩展 Agent 数量之前，先测量 Coordination Tax', '什么时候分解有意义', '典型拓扑', 'Topology 从部署前选择演进到运行时有界修复', '通信可以压缩成 latent，但 contract 不能一起消失', 'Behavioral belief 不等于 authenticated identity']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25233:end -->
<!-- delta:SF-2026-ARXIV-2605-25233:start -->We present Meta-Agent, a two-phase framework that automatically constructs and executes specialized multi-agent systems from natural-language task descriptions.<!-- delta:SF-2026-ARXIV-2605-25233:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-25233:end -->

<!-- books-review:SF-2026-ARXIV-2605-25240:start -->
<!-- existing:SF-2026-ARXIV-2605-25240:start -->Ch66 已比较 judge/metric 风险，但没有把 rubric 与 pairwise preference 作为不同 measurement operator 做受控同台选择。<!-- existing:SF-2026-ARXIV-2605-25240:end -->
<!-- delta:SF-2026-ARXIV-2605-25240:start -->把 rubric score 与 pairwise preference 作为不同 measurement operators，在同一受控质量阶梯上比较各自一致性与区分力，而不是默认二者可互换。<!-- delta:SF-2026-ARXIV-2605-25240:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-25240:end -->

<!-- books-review:SF-2026-ARXIV-2605-25244:start -->
<!-- existing:SF-2026-ARXIV-2605-25244:start -->已顺读 `books/part-05-inference-system/56-inference-scheduling.md` 及相邻章节 ['books/part-05-inference-system/55-pd-disaggregation.md', 'books/part-05-inference-system/README.md']；当前主干=['本章要回答的问题', '调度对象从 request 变成 token state', '目标函数不止吞吐', 'SLO-aware Admission', '当前能放下，不等于未来可完成', '不确定输出长度下的 Future-state Reservation', '连续 Edge Inference 需要跨窗口携带 Violation-risk Budget', '从队列启发式到时间耦合的资源影子价格']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25244:end -->
<!-- delta:SF-2026-ARXIV-2605-25244:start -->In this paper, we investigate the dynamics of confidence along reasoning trajectories and for first time reveal a surprising and unique pattern: correct answer traces tend to exhibit confidence improvement over time (positive confidence gain), while incorrect traces show attenuated or declining confidence as reasoning proceeds.<!-- delta:SF-2026-ARXIV-2605-25244:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-25244:end -->

<!-- books-review:SF-2026-ARXIV-2605-25247:start -->
<!-- existing:SF-2026-ARXIV-2605-25247:start -->已顺读 `books/part-05-inference-system/56-inference-scheduling.md` 及相邻章节 ['books/part-05-inference-system/55-pd-disaggregation.md', 'books/part-05-inference-system/README.md']；当前主干=['本章要回答的问题', '调度对象从 request 变成 token state', '目标函数不止吞吐', 'SLO-aware Admission', '当前能放下，不等于未来可完成', '不确定输出长度下的 Future-state Reservation', '连续 Edge Inference 需要跨窗口携带 Violation-risk Budget', '从队列启发式到时间耦合的资源影子价格']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25247:end -->
<!-- delta:SF-2026-ARXIV-2605-25247:start -->To improve the design and operation of LLM ecosystems, we envision simulators and simulation-based digital twins becoming primary decision-making tools.<!-- delta:SF-2026-ARXIV-2605-25247:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-25247:end -->

<!-- books-review:SF-2026-ARXIV-2605-25252:start -->
<!-- existing:SF-2026-ARXIV-2605-25252:start -->已顺读 `books/part-04-training-system/31-rlhf.md` 及相邻章节 ['books/part-04-training-system/30-lora.md', 'books/part-04-training-system/32-ppo.md']；当前主干=['本章要回答的问题', 'Demonstration 为什么不足以表达偏好', 'RLHF 的完整 pipeline', 'Reward Model 怎样学习相对判断', '一个 preference score 小例子', 'Preference data 的难点不只是数量', '从 Reward 到 Policy objective', '改变输出分布是目标，不是无副作用的偏好标签']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25252:end -->
<!-- delta:SF-2026-ARXIV-2605-25252:start -->Reinforcement learning with verifiable rewards (RLVR) has become a standard paradigm for post-training language models, but in practice, verifiers are rarely perfect.<!-- delta:SF-2026-ARXIV-2605-25252:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-25252:end -->

<!-- books-review:SF-2026-ARXIV-2605-25272:start -->
<!-- existing:SF-2026-ARXIV-2605-25272:start -->Ch66 已要求 construct validity 和 slice/uncertainty，但没有用 latent measurement model 分离共同构念与 benchmark-specific variance。<!-- existing:SF-2026-ARXIV-2605-25272:end -->
<!-- delta:SF-2026-ARXIV-2605-25272:start -->用 latent measurement model 分解 benchmark 共同因子与 task-specific variance，使 release evidence 能区分能力构念、数据生态和 leaderboard 聚合造成的相关性。<!-- delta:SF-2026-ARXIV-2605-25272:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-25272:end -->

<!-- books-review:SF-2026-ARXIV-2605-25284:start -->
<!-- existing:SF-2026-ARXIV-2605-25284:start -->已顺读 `books/part-07-agent/79-planning.md` 及相邻章节 ['books/part-07-agent/78-tool-calling.md', 'books/part-07-agent/80-reflection.md']；当前主干=['本章要回答的问题', 'Plan 不是解释文本', '从目标到状态图', 'Decomposition 的价值与代价', '依赖、并行与 Critical Path', 'Subtask Parallelism 与 Trial Parallelism 解决的不是同一个等待', 'Replanning 的触发条件', 'Search-based Planning 的边界']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25284:end -->
<!-- delta:SF-2026-ARXIV-2605-25284:start -->To study these abilities, we evaluate models on ambiguous, unambiguous, and disambiguated questions in three settings: standard question answering, explicit ambiguity judgment, and behavioral analysis, where a judge model classifies responses as direct answers, refusals, or clarifying questions.<!-- delta:SF-2026-ARXIV-2605-25284:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-25284:end -->

<!-- books-review:SF-2026-ARXIV-2605-25292:start -->
<!-- existing:SF-2026-ARXIV-2605-25292:start -->Ch63–65 已让 dependency、resource/topology、energy/carbon/telemetry state 进入 Kubernetes/Slurm placement owner，并保留 heuristic fallback。<!-- existing:SF-2026-ARXIV-2605-25292:end -->
<!-- delta:SF-2026-ARXIV-2605-25292:start -->让 scheduler 消费由 Digital Twin 维护的 node power/carbon/anomaly state，并把 heterogeneous workflow 先转成正式 dependency/resource model，再输出 Kubernetes/Slurm placement。<!-- delta:SF-2026-ARXIV-2605-25292:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-25292:end -->

<!-- books-review:SF-2026-ARXIV-2605-25298:start -->
<!-- existing:SF-2026-ARXIV-2605-25298:start -->Ch67/69 已区分 metrics 与 trace/dependency graph，但没有从 request entry thread 沿 backing-resource identity 追踪 kernel-level contention propagation。<!-- existing:SF-2026-ARXIV-2605-25298:end -->
<!-- delta:SF-2026-ARXIV-2605-25298:start -->从 thread-state 时间占比继续下钻到带 backing-resource identity 的 futex/pipe/socket/VFS/block-I/O dependency graph，并从 request entry thread 反向追踪 contention propagation。<!-- delta:SF-2026-ARXIV-2605-25298:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-25298:end -->

<!-- books-review:SF-2026-ARXIV-2605-25313:start -->
<!-- existing:SF-2026-ARXIV-2605-25313:start -->已顺读 `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 及相邻章节 ['books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md', 'books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md']；当前主干=['本章要回答的问题', '从三个容易混淆的对象开始', 'Video generation', 'Predictive environment model', 'Controllable world model', '在谈 State 之前，先声明预测 Channel', '为什么旧的 Simulator 仍然合理', '演进路线']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25313:end -->
<!-- delta:SF-2026-ARXIV-2605-25313:start -->We introduce the Unitary World Model JEPA (UWM-JEPA), a JEPA world model with a density-matrix latent on a joint system-environment space and a learned unitary predictor.<!-- delta:SF-2026-ARXIV-2605-25313:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-25313:end -->

<!-- books-review:SF-2026-ARXIV-2605-25338:start -->
<!-- existing:SF-2026-ARXIV-2605-25338:start -->已顺读 `books/part-07-agent/84-agent-platform.md` 及相邻章节 ['books/part-07-agent/83-mcp.md', 'books/part-07-agent/README.md']；当前主干=['本章要回答的问题', 'Agent 改变了平台的控制对象', 'Serving 结束不等于 Agent 任务结束', 'Agent Definition 与 Run Identity', '可编程 Skill 需要输入、状态与副作用契约', '可复用 Skill 不是一个 Prompt 文件', '从 Skill Catalog 到 Competence-aware Orchestration', '从 Trajectory 到 Skill 是一次受治理的 Compilation']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25338:end -->
<!-- delta:SF-2026-ARXIV-2605-25338:start -->We introduce CausalFlow, an interventional framework that converts failed agent traces into minimal counterfactual repairs and reusable supervision.<!-- delta:SF-2026-ARXIV-2605-25338:end --> Author decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-25338:end -->

<!-- books-review:SF-2026-ARXIV-2605-25375:start -->
<!-- existing:SF-2026-ARXIV-2605-25375:start -->已顺读 `books/part-04-training-system/38-pipeline-parallel.md` 及相邻章节 ['books/part-04-training-system/37-tensor-parallel.md', 'books/part-04-training-system/39-zero.md']；当前主干=['本章要回答的问题', '只有 Layer Partition 会发生什么', 'Micro-batch 怎样填充 Pipeline', 'Bubble 从哪里来', 'GPipe：先 Forward，再 Backward', '1F1B：缩短 Activation Lifetime', '异步 Pipeline：去掉 Bubble 会把成本移到参数版本', 'Runtime Variability 下由 Readiness 取得 Dispatch Authority']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25375:end -->
<!-- delta:SF-2026-ARXIV-2605-25375:start -->To this end, we propose BACE-Pipe, a bandwidth-aware and cost-efficient pipeline scheduling framework for LLM training across geo-distributed clusters.<!-- delta:SF-2026-ARXIV-2605-25375:end --> Author decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-25375:end -->

<!-- books-review:SF-2026-ARXIV-2605-25376:start -->
<!-- existing:SF-2026-ARXIV-2605-25376:start -->已顺读 `books/part-06-ai-infrastructure/72-security.md` 及相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；当前主干=['本章要回答的问题', '从资产与信任边界开始', '生命周期威胁', '隐私检测是 Policy-bound Sensor，不是安全判决', '从独立 Span 到关系感知的本地 Sanitization', 'Differential Privacy 先定义被保护对象，再选择机制', 'Privacy Accountant 必须与真实实现同构', 'Hidden State Release 不天然位于 Privacy 与 Utility 的中间地带']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25376:end -->
<!-- delta:SF-2026-ARXIV-2605-25376:start -->KYA (Know Your Agents) is an open-source, framework-agnostic trust and governance layer for autonomous systems, composed of five primitives: (1) a four-gate inbound apply pipeline; (2) an only-tighten composition algebra over a three-channel multi-tenant hierarchy; (3) KYP (Know Your Principal), a schema-level unification of trust scoring across human users, AI agents, and service accounts; (4) auditable interaction-multiplier amplification over an AIVSS-shaped additive baseline; and (5) two-axis delegation attribution: a static premium for risky delegates and a runtime debit for actual delegate misbehavior in multi-agent fan-out.<!-- delta:SF-2026-ARXIV-2605-25376:end --> Author decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-25376:end -->

<!-- books-review:SF-2026-ARXIV-2605-25379:start -->
<!-- existing:SF-2026-ARXIV-2605-25379:start -->已顺读 `books/part-07-agent/76-rag.md` 及相邻章节 ['books/part-07-agent/75-context.md', 'books/part-07-agent/77-memory.md']；当前主干=['本章要回答的问题', '参数化知识的边界', 'Offline Ingestion 不是预处理细节', 'Online Retrieval Pipeline', 'Tenant Filter 必须在检索内核中前置执行', 'Retrieval 可以预测未来需求，但必须允许取消与过期', 'SSD Filtered ANN 要把 Superset Traversal 与最终验证分开', 'Index Update 可以借用 Search I/O Stall，但不能借走 Freshness Authority']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25379:end -->
<!-- delta:SF-2026-ARXIV-2605-25379:start -->We introduce StateRAG, which represents retrieval control as a typed state external to the final reader.<!-- delta:SF-2026-ARXIV-2605-25379:end --> Author decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-25379:end -->

<!-- books-review:SF-2026-ARXIV-2605-25389:start -->
<!-- existing:SF-2026-ARXIV-2605-25389:start -->已顺读 `books/part-06-ai-infrastructure/72-security.md` 及相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；当前主干=['本章要回答的问题', '从资产与信任边界开始', '生命周期威胁', '隐私检测是 Policy-bound Sensor，不是安全判决', '从独立 Span 到关系感知的本地 Sanitization', 'Differential Privacy 先定义被保护对象，再选择机制', 'Privacy Accountant 必须与真实实现同构', 'Hidden State Release 不天然位于 Privacy 与 Utility 的中间地带']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25389:end -->
<!-- delta:SF-2026-ARXIV-2605-25389:start -->While Large Language Model-based Multi-Agent Systems (LLM-MAS) demonstrate remarkable capabilities in solving complex tasks by orchestrating specialized agents and external tools, the implicit trust in tool outputs creates a critical attack surface.<!-- delta:SF-2026-ARXIV-2605-25389:end --> Author decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-25389:end -->

<!-- books-review:SF-2026-ARXIV-2605-25421:start -->
<!-- existing:SF-2026-ARXIV-2605-25421:start -->已顺读 `books/part-07-agent/82-multi-agent.md` 及相邻章节 ['books/part-07-agent/81-workflow.md', 'books/part-07-agent/83-mcp.md']；当前主干=['本章要回答的问题', '先建立单 Agent Baseline', '扩展 Agent 数量之前，先测量 Coordination Tax', 'Agent 数量应由边际信息价值分配，而不是固定扩容', '什么时候分解有意义', '典型拓扑', 'Topology 从部署前选择演进到运行时有界修复', '通信可以压缩成 latent，但 contract 不能一起消失']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25421:end -->
<!-- delta:SF-2026-ARXIV-2605-25421:start -->Communication protocol design is a central challenge in large language model-based multi-agent systems.<!-- delta:SF-2026-ARXIV-2605-25421:end --> Author decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-25421:end -->

<!-- books-review:SF-2026-ARXIV-2605-25422:start -->
<!-- existing:SF-2026-ARXIV-2605-25422:start -->已顺读 `books/part-07-agent/82-multi-agent.md` 及相邻章节 ['books/part-07-agent/81-workflow.md', 'books/part-07-agent/83-mcp.md']；当前主干=['本章要回答的问题', '先建立单 Agent Baseline', '扩展 Agent 数量之前，先测量 Coordination Tax', 'Agent 数量应由边际信息价值分配，而不是固定扩容', '什么时候分解有意义', '典型拓扑', 'Topology 从部署前选择演进到运行时有界修复', '通信可以压缩成 latent，但 contract 不能一起消失']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25422:end -->
<!-- delta:SF-2026-ARXIV-2605-25422:start -->To address this, we propose a joint design that integrates communication-media selection with wireless resource allocation.<!-- delta:SF-2026-ARXIV-2605-25422:end --> Author decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-25422:end -->

<!-- books-review:SF-2026-ARXIV-2605-25424:start -->
<!-- existing:SF-2026-ARXIV-2605-25424:start -->已顺读 `books/part-05-inference-system/56-inference-scheduling.md` 及相邻章节 ['books/part-05-inference-system/55-pd-disaggregation.md', 'books/part-05-inference-system/README.md']；当前主干=['本章要回答的问题', '调度对象从 request 变成 token state', '目标函数不止吞吐', 'SLO-aware Admission', '当前能放下，不等于未来可完成', '不确定输出长度下的 Future-state Reservation', '连续 Edge Inference 需要跨窗口携带 Violation-risk Budget', '从队列启发式到时间耦合的资源影子价格']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25424:end -->
<!-- delta:SF-2026-ARXIV-2605-25424:start -->We introduce SeqRoute, a framework that formulates multi-turn routing as a finite-horizon Markov Decision Process and solves it via offline reinforcement learning.<!-- delta:SF-2026-ARXIV-2605-25424:end --> Author decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-25424:end -->

<!-- books-review:SF-2026-ARXIV-2605-25430:start -->
<!-- existing:SF-2026-ARXIV-2605-25430:start -->已顺读 `books/part-07-agent/84-agent-platform.md` 及相邻章节 ['books/part-07-agent/83-mcp.md', 'books/part-07-agent/README.md']；当前主干=['本章要回答的问题', 'Agent 改变了平台的控制对象', 'Serving 结束不等于 Agent 任务结束', 'Agent Definition 与 Run Identity', '可编程 Skill 需要输入、状态与副作用契约', '可复用 Skill 不是一个 Prompt 文件', '从 Skill Catalog 到 Competence-aware Orchestration', '从 Trajectory 到 Skill 是一次受治理的 Compilation']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25430:end -->
<!-- delta:SF-2026-ARXIV-2605-25430:start -->We propose CODESKILL, an LLM-based framework that reformulates skill extraction and skill-bank maintenance as a learnable management policy.<!-- delta:SF-2026-ARXIV-2605-25430:end --> Author decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-25430:end -->

<!-- books-review:SF-2026-ARXIV-2605-25451:start -->
<!-- existing:SF-2026-ARXIV-2605-25451:start -->已顺读 `books/part-04-training-system/36-distributed-training.md` 及相邻章节 ['books/part-04-training-system/35-checkpoint.md', 'books/part-04-training-system/37-tensor-parallel.md']；当前主干=['本章要回答的问题', '单卡为什么会失败', '从本机协作到分布式执行', '先分清五个通信层次', 'Collective 是群体语义，不是一种算法', '用 Alpha-Beta 模型建立下界直觉', 'Ring、Tree 与 Butterfly 在优化什么', 'MPI、NCCL、UCX、UCC 与 NIXL 的边界']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25451:end -->
<!-- delta:SF-2026-ARXIV-2605-25451:start -->We present BigMac, a new training pipeline for multimodal LLMs.<!-- delta:SF-2026-ARXIV-2605-25451:end --> Author decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-25451:end -->

<!-- books-review:SF-2026-ARXIV-2605-25475:start -->
<!-- existing:SF-2026-ARXIV-2605-25475:start -->已顺读 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 及相邻章节 ['books/part-05-inference-system/44-decode.md', 'books/part-05-inference-system/46-continuous-batching.md']；当前主干=['本章要回答的问题', '如果完全不缓存', '为什么缓存 K/V 而不是 Query', '逻辑 Shape 与容量公式', '一个容量小例子', 'KV Cache 的生命周期', 'Segmented Execution 必须在训练与推理共享同一语义', 'Prefix reuse']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25475:end -->
<!-- delta:SF-2026-ARXIV-2605-25475:start -->In this work, we introduce a learnable indexer that predicts KV importance, enabling more accurate retention of critical tokens.<!-- delta:SF-2026-ARXIV-2605-25475:end --> Author decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-25475:end -->

<!-- books-review:SF-2026-ARXIV-2605-25492:start -->
<!-- existing:SF-2026-ARXIV-2605-25492:start -->已顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 及相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前主干=['本章要回答的问题', '为什么“选一个分数”不是评估系统', 'HTTP 成功只是质量判断的第一道门', '从目标到证据，而不是从指标到目标', '第一个不变量：评估声明必须绑定完整对象', 'Evaluation Identity 必须包含 Harness 与 Environment', 'Backend 是 Evaluation Identity 的一部分', '第二个不变量：评估结论总是相对于分布']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25492:end -->
<!-- delta:SF-2026-ARXIV-2605-25492:start -->Pairwise model comparisons drawn from foundation-model benchmarks ("A is safer than B") are read as quantitative verdicts but hinge on harness choices benchmark papers under-specify.<!-- delta:SF-2026-ARXIV-2605-25492:end --> Author decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-25492:end -->

<!-- books-review:SF-2026-ARXIV-2605-25507:start -->
<!-- existing:SF-2026-ARXIV-2605-25507:start -->已顺读 `books/part-04-training-system/32-ppo.md` 及相邻章节 ['books/part-04-training-system/31-rlhf.md', 'books/part-04-training-system/33-grpo.md']；当前主干=['本章要回答的问题', '把语言生成写成策略过程', '最直接的 Policy Gradient', 'Value、Return 与 Advantage', 'Baseline Granularity 是 Rollout Cost 与 Attribution Fidelity 的交换', 'Critic 稳定性是一个联合合同', '当 Temporal Credit 不足：Counterfactual Credit 是有条件分支', '为什么需要旧策略概率']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25507:end -->
<!-- delta:SF-2026-ARXIV-2605-25507:start -->We propose two such methods: Random-Reset Policy Optimization (RRPO), where reset states are drawn randomly from reasoning steps, and Self-Reset Policy Optimization (SRPO), where the model self-localizes the erroneous step in an incorrect trajectory and resets there.<!-- delta:SF-2026-ARXIV-2605-25507:end --> Author decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-25507:end -->

<!-- books-review:SF-2026-ARXIV-2605-25521:start -->
<!-- existing:SF-2026-ARXIV-2605-25521:start -->已顺读 `books/part-05-inference-system/49-tensorrt-llm.md` 及相邻章节 ['books/part-05-inference-system/48-speculative-decoding.md', 'books/part-05-inference-system/50-vllm.md']；当前主干=['本章要回答的问题', '从计算图开始', '三类基础优化', 'Execution Plan 可以修订，但只能在安全边界 Commit', '异步工作不必永久绑定固定 Physical Core', '从粗粒度 Offload 到负载观测的 Tensor Placement', 'Backend Choice 必须携带 Previous-backend State', 'Accelerator Readiness 是 Phase × Shape × Offload × Host-control Contract']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25521:end -->
<!-- delta:SF-2026-ARXIV-2605-25521:start -->Although CPU-based solutions are prevalent, they are essentially general-purpose designs that fail to capture the intrinsic characteristics of PQ construction.In this paper, we propose CS-PQ, a Cache-friendly, SIMD-optimized PQ framework based on modern CPUs.<!-- delta:SF-2026-ARXIV-2605-25521:end --> Author decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-25521:end -->

<!-- books-review:SF-2026-ARXIV-2605-25535:start -->
<!-- existing:SF-2026-ARXIV-2605-25535:start -->已顺读 `books/part-07-agent/77-memory.md` 及相邻章节 ['books/part-07-agent/76-rag.md', 'books/part-07-agent/78-tool-calling.md']；当前主干=['本章要回答的问题', 'Context 与 Memory 的状态边界', 'Memory 类型是用途，不只是存储介质', 'Memory Write 是高风险决策', 'Write / Hold 不足以定义下一状态', '从 Outcome Reward 到 Content-level Credit：归因只能约束写入，不能成为真值', 'Memory Read 是受约束检索', '从按需读取到选择性主动干预']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25535:end -->
<!-- delta:SF-2026-ARXIV-2605-25535:start -->We introduce PerMemBench, the first benchmark for evaluating personalized memory systems, featuring multi year, multi domain interaction histories across diverse user personas.<!-- delta:SF-2026-ARXIV-2605-25535:end --> Author decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-25535:end -->

<!-- books-review:SF-2026-ARXIV-2605-25537:start -->
<!-- existing:SF-2026-ARXIV-2605-25537:start -->已顺读 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 及相邻章节 ['books/part-03-multimodal-world-models/25-multimodal-world-models.md', 'books/part-03-multimodal-world-models/README.md']；当前主干=['本章要回答的问题', '约束为何从 VLM 到 VLA 发生变化', '坐标系归一化是 Representation 到 Action Schema 的桥', '闭环主干', '从模块化机器人到 VLA', '传统模块化系统', 'VLM-conditioned controller', 'VLA policy']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25537:end -->
<!-- delta:SF-2026-ARXIV-2605-25537:start -->We propose Soft RTC, a training-time RTC generalization based on action-prior denoising.<!-- delta:SF-2026-ARXIV-2605-25537:end --> Author decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-25537:end -->

<!-- books-review:SF-2026-ARXIV-2605-25547:start -->
<!-- existing:SF-2026-ARXIV-2605-25547:start -->已顺读 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 及相邻章节 ['books/part-03-multimodal-world-models/25-multimodal-world-models.md', 'books/part-03-multimodal-world-models/README.md']；当前主干=['本章要回答的问题', '约束为何从 VLM 到 VLA 发生变化', '坐标系归一化是 Representation 到 Action Schema 的桥', '闭环主干', '从模块化机器人到 VLA', '传统模块化系统', 'VLM-conditioned controller', 'VLA policy']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25547:end -->
<!-- delta:SF-2026-ARXIV-2605-25547:start -->In this paper, we propose \textbf{TapSampling}, a plug-and-play framework for inference-time sampling.<!-- delta:SF-2026-ARXIV-2605-25547:end --> Author decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-25547:end -->

<!-- books-review:SF-2026-ARXIV-2605-25550:start -->
<!-- existing:SF-2026-ARXIV-2605-25550:start -->已顺读 `books/part-05-inference-system/55-pd-disaggregation.md` 及相邻章节 ['books/part-05-inference-system/54-gpu-memory.md', 'books/part-05-inference-system/56-inference-scheduling.md']；当前主干=['本章要回答的问题', '两种阶段，两种节奏', '分离之后发生什么', '新问题：KV 怎么移动', 'Transfer Cost 下界', '从 Full Transfer 到 Demand-corrected Selective Transfer', '从共享链路调度到物理 Traffic-class Isolation', '从完整到达再执行到 Progressive Verified Handoff']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25550:end -->
<!-- delta:SF-2026-ARXIV-2605-25550:start -->Diffusion-based generation is increasingly powering production content pipelines; however, deploying these models at scale remains a significant challenge.<!-- delta:SF-2026-ARXIV-2605-25550:end --> Author decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-25550:end -->

<!-- books-review:SF-2026-ARXIV-2605-25621:start -->
<!-- existing:SF-2026-ARXIV-2605-25621:start -->已顺读 `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md` 及相邻章节 ['books/part-03-multimodal-world-models/23-multimodal-representation.md', 'books/part-03-multimodal-world-models/25-multimodal-world-models.md']；当前主干=['本章要回答的问题', '从一个共同问题开始', '为什么 Autoregressive 是合理起点', 'Diffusion：用迭代修正换并行状态更新', 'Masked generation：未知位置与已知位置', 'Editable tokens 与 commit boundary', 'Self-revision：并行位置必须在 Commit 前保持可撤销', '生成 Workflow 也可以被训练进 Intermediate State']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25621:end -->
<!-- delta:SF-2026-ARXIV-2605-25621:start -->To bridge these gaps, we propose StreamOV, a novel Streaming Omni-Video understanding framework for efficient online audio-visual reasoning with bounded memory and proactive response triggering.<!-- delta:SF-2026-ARXIV-2605-25621:end --> Author decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-25621:end -->

<!-- books-review:SF-2026-ARXIV-2605-25624:start -->
<!-- existing:SF-2026-ARXIV-2605-25624:start -->已顺读 `books/part-07-agent/84-agent-platform.md` 及相邻章节 ['books/part-07-agent/83-mcp.md', 'books/part-07-agent/README.md']；当前主干=['本章要回答的问题', 'Agent 改变了平台的控制对象', 'Serving 结束不等于 Agent 任务结束', 'Agent Definition 与 Run Identity', '可编程 Skill 需要输入、状态与副作用契约', '可复用 Skill 不是一个 Prompt 文件', '从 Skill Catalog 到 Competence-aware Orchestration', '从 Trajectory 到 Skill 是一次受治理的 Compilation']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25624:end -->
<!-- delta:SF-2026-ARXIV-2605-25624:start -->We present CUA-Gym, a scalable pipeline that co-generates task instructions, environment states, and reward functions.<!-- delta:SF-2026-ARXIV-2605-25624:end --> Author decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-25624:end -->

<!-- books-review:SF-2026-ARXIV-2605-25632:start -->
<!-- existing:SF-2026-ARXIV-2605-25632:start -->已顺读 `books/part-07-agent/78-tool-calling.md` 及相邻章节 ['books/part-07-agent/77-memory.md', 'books/part-07-agent/79-planning.md']；当前主干=['本章要回答的问题', '从生成文本到环境转移', 'Tool Contract', '模型输出只是 Proposal', '编译器反馈可以前移，但仍是受限 Authority', 'Tool Discovery 与选择', '同功能 Provider 的选择属于运行时路由，不属于模型授权', 'Interface Granularity：不是 Tool 越多越有能力']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25632:end -->
<!-- delta:SF-2026-ARXIV-2605-25632:start -->We propose the Actuarial Action Interface (AAI), a deterministic runtime contract that prices each such action against a contractually fixed safe default under a time-consistent risk mapping, and gates execution against a per-boundary reserve capital budget.<!-- delta:SF-2026-ARXIV-2605-25632:end --> Author decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-25632:end -->

<!-- books-review:SF-2026-ARXIV-2605-25641:start -->
<!-- existing:SF-2026-ARXIV-2605-25641:start -->已顺读 `books/part-07-agent/76-rag.md` 及相邻章节 ['books/part-07-agent/75-context.md', 'books/part-07-agent/77-memory.md']；当前主干=['本章要回答的问题', '参数化知识的边界', 'Offline Ingestion 不是预处理细节', 'Online Retrieval Pipeline', 'Tenant Filter 必须在检索内核中前置执行', 'Retrieval 可以预测未来需求，但必须允许取消与过期', 'SSD Filtered ANN 要把 Superset Traversal 与最终验证分开', 'Index Update 可以借用 Search I/O Stall，但不能借走 Freshness Authority']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25641:end -->
<!-- delta:SF-2026-ARXIV-2605-25641:start -->We identify these instances and convert them into compact knowledge-base entries, which we call factual nuggets.<!-- delta:SF-2026-ARXIV-2605-25641:end --> Author decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-25641:end -->

<!-- books-review:SF-2026-ARXIV-2605-25653:start -->
<!-- existing:SF-2026-ARXIV-2605-25653:start -->已顺读 `books/part-06-ai-infrastructure/72-security.md` 及相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；当前主干=['本章要回答的问题', '从资产与信任边界开始', '生命周期威胁', '隐私检测是 Policy-bound Sensor，不是安全判决', '从独立 Span 到关系感知的本地 Sanitization', 'Differential Privacy 先定义被保护对象，再选择机制', 'Privacy Accountant 必须与真实实现同构', 'Hidden State Release 不天然位于 Privacy 与 Utility 的中间地带']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25653:end -->
<!-- delta:SF-2026-ARXIV-2605-25653:start -->We analyse this threat landscape through Cobot-Claw, a deployed four-agent system for UR3e robotic arm control, and identify five attack classes specific to agentic cyber-physical systems.<!-- delta:SF-2026-ARXIV-2605-25653:end --> Author decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-25653:end -->

<!-- books-review:SF-2026-ARXIV-2605-25655:start -->
<!-- existing:SF-2026-ARXIV-2605-25655:start -->已顺读 `books/part-05-inference-system/56-inference-scheduling.md` 及相邻章节 ['books/part-05-inference-system/55-pd-disaggregation.md', 'books/part-05-inference-system/README.md']；当前主干=['本章要回答的问题', '调度对象从 request 变成 token state', '目标函数不止吞吐', 'SLO-aware Admission', '当前能放下，不等于未来可完成', '不确定输出长度下的 Future-state Reservation', '连续 Edge Inference 需要跨窗口携带 Violation-risk Budget', '从队列启发式到时间耦合的资源影子价格']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25655:end -->
<!-- delta:SF-2026-ARXIV-2605-25655:start -->To address this problem, we propose THInfer, a hardware-aware inference framework that maximizes data locality under bandwidth-constrained conditions through hardware-software co-design and parallel strategy optimization.<!-- delta:SF-2026-ARXIV-2605-25655:end --> Author decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-25655:end -->

<!-- books-review:SF-2026-ARXIV-2605-25673:start -->
<!-- existing:SF-2026-ARXIV-2605-25673:start -->已顺读 `books/part-06-ai-infrastructure/72-security.md` 及相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；当前主干=['本章要回答的问题', '从资产与信任边界开始', '生命周期威胁', '隐私检测是 Policy-bound Sensor，不是安全判决', '从独立 Span 到关系感知的本地 Sanitization', 'Differential Privacy 先定义被保护对象，再选择机制', 'Privacy Accountant 必须与真实实现同构', 'Hidden State Release 不天然位于 Privacy 与 Utility 的中间地带']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25673:end -->
<!-- delta:SF-2026-ARXIV-2605-25673:start -->To resolve this, we propose referential security as a new paradigm for AI evaluation.<!-- delta:SF-2026-ARXIV-2605-25673:end --> Author decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-25673:end -->

<!-- books-review:SF-2026-ARXIV-2605-25674:start -->
<!-- existing:SF-2026-ARXIV-2605-25674:start -->已顺读 `books/part-06-ai-infrastructure/67-monitoring.md` 及相邻章节 ['books/part-06-ai-infrastructure/66-evaluation-system.md', 'books/part-06-ai-infrastructure/68-logging.md']；当前主干=['本章要回答的问题', '先定义目标，再选择可测信号', 'Context generator 是 pre-failure sensor identity 的一部分', 'Review notes', '四层指标', '从 GPU Busy 到 Counter-derived Progress Sensor', 'Autonomy 不是一个纯模型指标', '从单次 Query 指标到 Session-level Search Trajectory Sensor']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25674:end -->
<!-- delta:SF-2026-ARXIV-2605-25674:start -->We present a stochastic estimator of the trace of the diagonal blocks of the Hessian matrix of the empirical risk of a neural network.<!-- delta:SF-2026-ARXIV-2605-25674:end --> Author decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-25674:end -->

<!-- books-review:SF-2026-ARXIV-2605-25682:start -->
<!-- existing:SF-2026-ARXIV-2605-25682:start -->已顺读 `books/part-05-inference-system/56-inference-scheduling.md` 及相邻章节 ['books/part-05-inference-system/55-pd-disaggregation.md', 'books/part-05-inference-system/README.md']；当前主干=['本章要回答的问题', '调度对象从 request 变成 token state', '目标函数不止吞吐', 'SLO-aware Admission', '当前能放下，不等于未来可完成', '不确定输出长度下的 Future-state Reservation', '连续 Edge Inference 需要跨窗口携带 Violation-risk Budget', '从队列启发式到时间耦合的资源影子价格']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25682:end -->
<!-- delta:SF-2026-ARXIV-2605-25682:start -->We present a hardware prototype study on NVIDIA Jetson Orin Nano devices connected over WiFi.<!-- delta:SF-2026-ARXIV-2605-25682:end --> Author decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-25682:end -->

<!-- books-review:SF-2026-ARXIV-2605-25698:start -->
<!-- existing:SF-2026-ARXIV-2605-25698:start -->已顺读 `books/part-04-training-system/27-data.md` 及相邻章节 ['books/part-04-training-system/28-pretraining.md']；当前主干=['本章要回答的问题', 'Part IV 的能力生产链', '先从“把互联网都抓下来”开始', 'Collection protocol 为什么先于 Filtering 定义数据', '数据分布就是优化权重', 'Data Reuse 改变的是 Layer-wise Growth，不只是 Epoch 计数', '静态 Mixture 到版本化 Data Control Plane', '一个三域配比小例子']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25698:end -->
<!-- delta:SF-2026-ARXIV-2605-25698:start -->Motivated by the theoretical structure, we propose Drop-Stable-Rampup for LLM midtraining: drop the batch size at the quality transition, keep it low to accumulate signal, then ramp up to suppress noise.<!-- delta:SF-2026-ARXIV-2605-25698:end --> Author decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-25698:end -->

<!-- books-review:SF-2026-ARXIV-2605-25707:start -->
<!-- existing:SF-2026-ARXIV-2605-25707:start -->已顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 及相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前主干=['本章要回答的问题', '为什么“选一个分数”不是评估系统', 'HTTP 成功只是质量判断的第一道门', '从目标到证据，而不是从指标到目标', '第一个不变量：评估声明必须绑定完整对象', 'Evaluation Identity 必须包含 Harness 与 Environment', 'Backend 是 Evaluation Identity 的一部分', '第二个不变量：评估结论总是相对于分布']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25707:end -->
<!-- delta:SF-2026-ARXIV-2605-25707:start -->We introduce AgentHijack, a benchmark designed to evaluate the robustness of computer-use agents under common corruptions, where the uncertainties in dynamic environment disrupt the execution flow without direct adversarial intent.<!-- delta:SF-2026-ARXIV-2605-25707:end --> Author decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-25707:end -->

<!-- books-review:SF-2026-ARXIV-2605-25716:start -->
<!-- existing:SF-2026-ARXIV-2605-25716:start -->已顺读 `books/part-06-ai-infrastructure/72-security.md` 及相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；当前主干=['本章要回答的问题', '从资产与信任边界开始', '生命周期威胁', '隐私检测是 Policy-bound Sensor，不是安全判决', '从独立 Span 到关系感知的本地 Sanitization', 'Differential Privacy 先定义被保护对象，再选择机制', 'Privacy Accountant 必须与真实实现同构', 'Hidden State Release 不天然位于 Privacy 与 Utility 的中间地带']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25716:end -->
<!-- delta:SF-2026-ARXIV-2605-25716:start -->To address this challenge, we present FedRAG, a high-throughput, privacy-preserving federated RAG framework.<!-- delta:SF-2026-ARXIV-2605-25716:end --> Author decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-25716:end -->

<!-- books-review:SF-2026-ARXIV-2605-25745:start -->
<!-- existing:SF-2026-ARXIV-2605-25745:start -->已顺读 `books/part-02-model/18-decoder-only.md` 及相邻章节 ['books/part-02-model/17-transformer-layer.md', 'books/part-02-model/19-kv-cache.md']；现有主干已经区分显式 CoT 与 latent reasoning，但尚未覆盖同一 trajectory 内按 span anticipation 与 confidence 选择表示的中间分支。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25745:end -->
<!-- delta:SF-2026-ARXIV-2605-25745:start -->In this work, we propose Selective Latent Thinking (SLT), a framework that selectively compresses redundant reasoning spans into latent representations while preserving precision-critical spans as explicit CoT within the same reasoning trajectory.<!-- delta:SF-2026-ARXIV-2605-25745:end --> Author decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-25745:end -->

<!-- books-review:SF-2026-ARXIV-2605-25746:start -->
<!-- existing:SF-2026-ARXIV-2605-25746:start -->已顺读 `books/part-07-agent/82-multi-agent.md` 及相邻章节 ['books/part-07-agent/81-workflow.md', 'books/part-07-agent/83-mcp.md']；当前主干=['本章要回答的问题', '先建立单 Agent Baseline', '扩展 Agent 数量之前，先测量 Coordination Tax', 'Agent 数量应由边际信息价值分配，而不是固定扩容', '什么时候分解有意义', '典型拓扑', 'Topology 从部署前选择演进到运行时有界修复', '通信可以压缩成 latent，但 contract 不能一起消失']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25746:end -->
<!-- delta:SF-2026-ARXIV-2605-25746:start -->We introduce MACA, an automated coordination framework that learns a task- and budget-conditioned structural prior over agent participation and interactions.<!-- delta:SF-2026-ARXIV-2605-25746:end --> Author decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-25746:end -->

<!-- books-review:SF-2026-ARXIV-2605-25798:start -->
<!-- existing:SF-2026-ARXIV-2605-25798:start -->已顺读 `books/part-05-inference-system/49-tensorrt-llm.md` 及相邻章节 ['books/part-05-inference-system/48-speculative-decoding.md', 'books/part-05-inference-system/50-vllm.md']；当前主干=['本章要回答的问题', '从计算图开始', '三类基础优化', 'Execution Plan 可以修订，但只能在安全边界 Commit', '异步工作不必永久绑定固定 Physical Core', '从粗粒度 Offload 到负载观测的 Tensor Placement', 'Backend Choice 必须携带 Previous-backend State', 'Accelerator Readiness 是 Phase × Shape × Offload × Host-control Contract']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25798:end -->
<!-- delta:SF-2026-ARXIV-2605-25798:start -->In this paper, we propose DiSC, a resolution-scalable, sparsity-aware hardware accelerator.<!-- delta:SF-2026-ARXIV-2605-25798:end --> Author decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-25798:end -->

<!-- books-review:SF-2026-ARXIV-2605-25815:start -->
<!-- existing:SF-2026-ARXIV-2605-25815:start -->已顺读 `books/part-07-agent/84-agent-platform.md` 及相邻章节 ['books/part-07-agent/83-mcp.md', 'books/part-07-agent/README.md']；当前主干=['本章要回答的问题', 'Agent 改变了平台的控制对象', 'Serving 结束不等于 Agent 任务结束', 'Agent Definition 与 Run Identity', '可编程 Skill 需要输入、状态与副作用契约', '可复用 Skill 不是一个 Prompt 文件', '从 Skill Catalog 到 Competence-aware Orchestration', '从 Trajectory 到 Skill 是一次受治理的 Compilation']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25815:end -->
<!-- delta:SF-2026-ARXIV-2605-25815:start -->We present the first large-scale empirical study of EvoMap, a prominent A2A collaboration network.<!-- delta:SF-2026-ARXIV-2605-25815:end --> Author decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-25815:end -->

<!-- books-review:SF-2026-ARXIV-2605-25819:start -->
<!-- existing:SF-2026-ARXIV-2605-25819:start -->已顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 及相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前主干=['本章要回答的问题', '为什么“选一个分数”不是评估系统', 'HTTP 成功只是质量判断的第一道门', '从目标到证据，而不是从指标到目标', '第一个不变量：评估声明必须绑定完整对象', 'Evaluation Identity 必须包含 Harness 与 Environment', 'Backend 是 Evaluation Identity 的一部分', '第二个不变量：评估结论总是相对于分布']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25819:end -->
<!-- delta:SF-2026-ARXIV-2605-25819:start -->We demonstrate two key weaknesses in this efficient MIA evaluation pipeline.<!-- delta:SF-2026-ARXIV-2605-25819:end --> Author decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-25819:end -->

<!-- books-review:SF-2026-ARXIV-2605-25820:start -->
<!-- existing:SF-2026-ARXIV-2605-25820:start -->已顺读 `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md` 及相邻章节 ['books/part-03-multimodal-world-models/23-multimodal-representation.md', 'books/part-03-multimodal-world-models/25-multimodal-world-models.md']；当前主干=['本章要回答的问题', '从一个共同问题开始', '为什么 Autoregressive 是合理起点', 'Diffusion：用迭代修正换并行状态更新', 'Masked generation：未知位置与已知位置', 'Editable tokens 与 commit boundary', 'Self-revision：并行位置必须在 Commit 前保持可撤销', '生成 Workflow 也可以被训练进 Intermediate State']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25820:end -->
<!-- delta:SF-2026-ARXIV-2605-25820:start -->We identify a step-level limitation of this strategy in multimodal settings: high-confidence tokens selected in the same step can rely on overlapping visual grounding, introducing visual redundancy among the committed tokens and leaving less complementary visual grounding available for later decoding.<!-- delta:SF-2026-ARXIV-2605-25820:end --> Author decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-25820:end -->

<!-- books-review:SF-2026-ARXIV-2605-25831:start -->
<!-- existing:SF-2026-ARXIV-2605-25831:start -->已顺读 `books/part-07-agent/80-reflection.md` 及相邻章节 ['books/part-07-agent/79-planning.md', 'books/part-07-agent/81-workflow.md']；当前主干=['本章要回答的问题', '基本循环', 'Feedback 来源决定价值', 'Reflection 应输出可执行诊断', 'Verification-centric Reflection：先定位 Evidence Gap，再决定重跑什么', '从固定 Reflection Prompt 到 Learned Adaptation Policy', '从“结果失败”到“最早可修复偏离”', '反思对象要分开']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25831:end -->
<!-- delta:SF-2026-ARXIV-2605-25831:start -->We propose Belief-Augmented Generation (BAG): grounding LLMs in their own belief state via the prompt and letting them reason over these K samples to decide on a conversational strategy: answer, clarify, or abstain.<!-- delta:SF-2026-ARXIV-2605-25831:end --> Author decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-25831:end -->

<!-- books-review:SF-2026-ARXIV-2605-25854:start -->
<!-- existing:SF-2026-ARXIV-2605-25854:start -->已顺读 `books/part-06-ai-infrastructure/70-cost.md` 及相邻章节 ['books/part-06-ai-infrastructure/69-trace.md', 'books/part-06-ai-infrastructure/71-multi-tenant.md']；当前主干=['本章要回答的问题', '资源时间是共同底座', '训练成本', 'Adaptation 不是单一路径，而是受预算约束的组合决策', '推理成本', 'Agent Trajectory 的 Token 数必须折算为 State-dependent Work', 'Agent 能耗的分母应是 Successful Goal', 'Agent 的持久化 Footprint 也是成本']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25854:end -->
<!-- delta:SF-2026-ARXIV-2605-25854:start -->Case studies on the IEEE 30-bus and 118-bus test systems demonstrate reliable convergence, exact power-water consistency, and reductions of approximately 3-5% in generation-related freshwater withdrawals under water-constrained conditions.<!-- delta:SF-2026-ARXIV-2605-25854:end --> Author decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-25854:end -->

<!-- books-review:SF-2026-ARXIV-2605-25869:start -->
<!-- existing:SF-2026-ARXIV-2605-25869:start -->已顺读 `books/part-07-agent/77-memory.md` 及相邻章节 ['books/part-07-agent/76-rag.md', 'books/part-07-agent/78-tool-calling.md']；当前主干=['本章要回答的问题', 'Context 与 Memory 的状态边界', 'Memory 类型是用途，不只是存储介质', 'Memory Write 是高风险决策', 'Write / Hold 不足以定义下一状态', '从 Outcome Reward 到 Content-level Credit：归因只能约束写入，不能成为真值', 'Memory Read 是受约束检索', '从按需读取到选择性主动干预']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25869:end -->
<!-- delta:SF-2026-ARXIV-2605-25869:start -->To resolve this cognitive vulnerability at the architectural level, we propose MemIR, a typed Memory Intermediate Representation that operationalizes source monitoring as a structural constraint.<!-- delta:SF-2026-ARXIV-2605-25869:end --> Author decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-25869:end -->

<!-- books-review:SF-2026-ARXIV-2605-25874:start -->
<!-- existing:SF-2026-ARXIV-2605-25874:start -->已顺读 `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 及相邻章节 ['books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md', 'books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md']；当前主干=['本章要回答的问题', '从三个容易混淆的对象开始', 'Video generation', 'Predictive environment model', 'Controllable world model', '在谈 State 之前，先声明预测 Channel', '为什么旧的 Simulator 仍然合理', '演进路线']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25874:end -->
<!-- delta:SF-2026-ARXIV-2605-25874:start -->To fill this gap, we introduce WBench, a comprehensive multi-turn benchmark for interactive world model evaluation along five dimensions, namely video quality, setting adherence, interaction adherence, consistency, and physics compliance.<!-- delta:SF-2026-ARXIV-2605-25874:end --> Author decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-25874:end -->

<!-- books-review:SF-2026-ARXIV-2605-25889:start -->
<!-- existing:SF-2026-ARXIV-2605-25889:start -->已顺读 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 及相邻章节 ['books/part-03-multimodal-world-models/25-multimodal-world-models.md', 'books/part-03-multimodal-world-models/README.md']；当前主干=['本章要回答的问题', '约束为何从 VLM 到 VLA 发生变化', '坐标系归一化是 Representation 到 Action Schema 的桥', '闭环主干', '从模块化机器人到 VLA', '传统模块化系统', 'VLM-conditioned controller', 'VLA policy']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25889:end -->
<!-- delta:SF-2026-ARXIV-2605-25889:start -->Vision-Language-Action (VLA) models reach high success rates on clean inputs but collapse under small adversarial perturbations: a $16/255$ PGD attack drops OpenVLA-7B's LIBERO success from $95\%$ to under $5\%$.<!-- delta:SF-2026-ARXIV-2605-25889:end --> Author decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-25889:end -->

<!-- books-review:SF-2026-ARXIV-2605-25893:start -->
<!-- existing:SF-2026-ARXIV-2605-25893:start -->已顺读 `books/part-06-ai-infrastructure/72-security.md` 及相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；当前主干=['本章要回答的问题', '从资产与信任边界开始', '生命周期威胁', '隐私检测是 Policy-bound Sensor，不是安全判决', '从独立 Span 到关系感知的本地 Sanitization', 'Differential Privacy 先定义被保护对象，再选择机制', 'Privacy Accountant 必须与真实实现同构', 'Hidden State Release 不天然位于 Privacy 与 Utility 的中间地带']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25893:end -->
<!-- delta:SF-2026-ARXIV-2605-25893:start -->Motivated by the suitability of lightweight probes for always-on monitoring, we analyze which trajectory-level signals best indicate when such probes are likely to struggle.<!-- delta:SF-2026-ARXIV-2605-25893:end --> Author decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-25893:end -->

<!-- books-review:SF-2026-ARXIV-2605-25966:start -->
<!-- existing:SF-2026-ARXIV-2605-25966:start -->已顺读 `books/part-05-inference-system/49-tensorrt-llm.md` 及相邻章节 ['books/part-05-inference-system/48-speculative-decoding.md', 'books/part-05-inference-system/50-vllm.md']；当前主干=['本章要回答的问题', '从计算图开始', '三类基础优化', 'Execution Plan 可以修订，但只能在安全边界 Commit', '异步工作不必永久绑定固定 Physical Core', '从粗粒度 Offload 到负载观测的 Tensor Placement', 'Backend Choice 必须携带 Previous-backend State', 'Accelerator Readiness 是 Phase × Shape × Offload × Host-control Contract']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25966:end -->
<!-- delta:SF-2026-ARXIV-2605-25966:start -->We test whether the optimal learning-rate schedule depends on bit-width during from-initialisation quantisation-aware training (QAT) for sub-100M decoder language models.<!-- delta:SF-2026-ARXIV-2605-25966:end --> Author decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-25966:end -->

<!-- books-review:SF-2026-ARXIV-2605-25971:start -->
<!-- existing:SF-2026-ARXIV-2605-25971:start -->已顺读 `books/part-07-agent/84-agent-platform.md` 及相邻章节 ['books/part-07-agent/83-mcp.md', 'books/part-07-agent/README.md']；当前主干=['本章要回答的问题', 'Agent 改变了平台的控制对象', 'Serving 结束不等于 Agent 任务结束', 'Agent Definition 与 Run Identity', '可编程 Skill 需要输入、状态与副作用契约', '可复用 Skill 不是一个 Prompt 文件', '从 Skill Catalog 到 Competence-aware Orchestration', '从 Trajectory 到 Skill 是一次受治理的 Compilation']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25971:end -->
<!-- delta:SF-2026-ARXIV-2605-25971:start -->While AI agents demonstrate remarkable capabilities in reasoning and tool use, they remain fundamentally reactive: they compute responses only after explicit user prompts.<!-- delta:SF-2026-ARXIV-2605-25971:end --> Author decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-25971:end -->

<!-- books-review:SF-2026-ARXIV-2605-25988:start -->
<!-- existing:SF-2026-ARXIV-2605-25988:start -->已顺读 `books/part-07-agent/76-rag.md` 及相邻章节 ['books/part-07-agent/75-context.md', 'books/part-07-agent/77-memory.md']；当前主干=['本章要回答的问题', '参数化知识的边界', 'Offline Ingestion 不是预处理细节', 'Online Retrieval Pipeline', 'Tenant Filter 必须在检索内核中前置执行', 'Retrieval 可以预测未来需求，但必须允许取消与过期', 'SSD Filtered ANN 要把 Superset Traversal 与最终验证分开', 'Index Update 可以借用 Search I/O Stall，但不能借走 Freshness Authority']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25988:end -->
<!-- delta:SF-2026-ARXIV-2605-25988:start -->Medical RAG needs evidence-grounded claims, so plugging a claim-level NLI checker into retrieval-augmented RL is intuitive.<!-- delta:SF-2026-ARXIV-2605-25988:end --> Author decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-25988:end -->

<!-- books-review:SF-2026-ARXIV-2605-25997:start -->
<!-- existing:SF-2026-ARXIV-2605-25997:start -->已顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 及相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前主干=['本章要回答的问题', '为什么“选一个分数”不是评估系统', 'HTTP 成功只是质量判断的第一道门', '从目标到证据，而不是从指标到目标', '第一个不变量：评估声明必须绑定完整对象', 'Evaluation Identity 必须包含 Harness 与 Environment', 'Backend 是 Evaluation Identity 的一部分', '第二个不变量：评估结论总是相对于分布']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25997:end -->
<!-- delta:SF-2026-ARXIV-2605-25997:start -->We introduce deployment-complete benchmarking, which tests whether benchmark evidence determines a deployment action.<!-- delta:SF-2026-ARXIV-2605-25997:end --> Author decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-25997:end -->

<!-- books-review:SF-2026-ARXIV-2605-26029:start -->
<!-- existing:SF-2026-ARXIV-2605-26029:start -->已顺读 `books/part-07-agent/81-workflow.md` 及相邻章节 ['books/part-07-agent/80-reflection.md', 'books/part-07-agent/82-multi-agent.md']；当前主干=['本章要回答的问题', '一个循环为什么不够', 'State Machine 是基本模型', 'Failure attribution、perception routing 与 sticky state ownership', 'Review notes', '从“对象已保存”到“状态已激活”', 'Task State Alignment 是每次 Dispatch 的前置条件', 'Deterministic Spine，Agentic Nodes']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-26029:end -->
<!-- delta:SF-2026-ARXIV-2605-26029:start -->We introduce CausaLab, a scalable environment for evaluating interactive causal discovery by LLM agents.<!-- delta:SF-2026-ARXIV-2605-26029:end --> Author decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-26029:end -->

<!-- books-review:SF-2026-ARXIV-2605-26037:start -->
<!-- existing:SF-2026-ARXIV-2605-26037:start -->已顺读 `books/part-04-training-system/33-grpo.md` 及相邻章节 ['books/part-04-training-system/32-ppo.md', 'books/part-04-training-system/34-dpo.md']；当前主干=['本章要回答的问题', '为什么移除 Critic 会有吸引力', '同 Prompt 生成一组 Responses', 'Group-relative advantage', '一个三样本小例子', 'GRPO 的 clipped objective', '正负 Advantage 不必共享同一 Clipping Contract', 'Sequence Reward 怎样作用到 Tokens']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-26037:end -->
<!-- delta:SF-2026-ARXIV-2605-26037:start -->We test the standard RLVR tool-use recipe -- GRPO on Qwen2.5-7B-Instruct -- on a deliberately minimal knowledge-graph tool API: four Freebase navigation verbs over Complex WebQuestions.<!-- delta:SF-2026-ARXIV-2605-26037:end --> Author decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-26037:end -->

<!-- books-review:SF-2026-ARXIV-2605-26045:start -->
<!-- existing:SF-2026-ARXIV-2605-26045:start -->已顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 及相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前主干=['本章要回答的问题', '为什么“选一个分数”不是评估系统', 'HTTP 成功只是质量判断的第一道门', '从目标到证据，而不是从指标到目标', '第一个不变量：评估声明必须绑定完整对象', 'Evaluation Identity 必须包含 Harness 与 Environment', 'Backend 是 Evaluation Identity 的一部分', '第二个不变量：评估结论总是相对于分布']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-26045:end -->
<!-- delta:SF-2026-ARXIV-2605-26045:start -->An activation oracle is a language model trained to read another model's internal activations and describe them in natural language, for example to name a secret word the other model was trained to hide.<!-- delta:SF-2026-ARXIV-2605-26045:end --> Author decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-26045:end -->

<!-- books-review:SF-2026-ARXIV-2605-26046:start -->
<!-- existing:SF-2026-ARXIV-2605-26046:start -->已顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 及相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前主干=['本章要回答的问题', '为什么“选一个分数”不是评估系统', 'HTTP 成功只是质量判断的第一道门', '从目标到证据，而不是从指标到目标', '第一个不变量：评估声明必须绑定完整对象', 'Evaluation Identity 必须包含 Harness 与 Environment', 'Backend 是 Evaluation Identity 的一部分', '第二个不变量：评估结论总是相对于分布']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-26046:end -->
<!-- delta:SF-2026-ARXIV-2605-26046:start -->These results identify two separable failure modes: optimization-time gradient dilution and inference-time instruction interference, which together constrain the design space for multi-objective judge optimization using textual feedback.<!-- delta:SF-2026-ARXIV-2605-26046:end --> Author decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-26046:end -->

<!-- books-review:SF-2026-ARXIV-2605-26047:start -->
<!-- existing:SF-2026-ARXIV-2605-26047:start -->已顺读 `books/part-06-ai-infrastructure/72-security.md` 及相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；当前主干=['本章要回答的问题', '从资产与信任边界开始', '生命周期威胁', '隐私检测是 Policy-bound Sensor，不是安全判决', '从独立 Span 到关系感知的本地 Sanitization', 'Differential Privacy 先定义被保护对象，再选择机制', 'Privacy Accountant 必须与真实实现同构', 'Hidden State Release 不天然位于 Privacy 与 Utility 的中间地带']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-26047:end -->
<!-- delta:SF-2026-ARXIV-2605-26047:start -->We study retrying from an AI control perspective, which treats the model as potentially adversarial.<!-- delta:SF-2026-ARXIV-2605-26047:end --> Author decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-26047:end -->

<!-- books-review:SF-2026-ARXIV-2605-26079:start -->
<!-- existing:SF-2026-ARXIV-2605-26079:start -->已顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 及相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前主干=['本章要回答的问题', '为什么“选一个分数”不是评估系统', 'HTTP 成功只是质量判断的第一道门', '从目标到证据，而不是从指标到目标', '第一个不变量：评估声明必须绑定完整对象', 'Evaluation Identity 必须包含 Harness 与 Environment', 'Backend 是 Evaluation Identity 的一部分', '第二个不变量：评估结论总是相对于分布']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-26079:end -->
<!-- delta:SF-2026-ARXIV-2605-26079:start -->We introduce Auto Benchmark Audit (ABA), an agentic framework that systematically audits individual benchmark tasks, uncovering issues such as hidden environment dependencies, specification gaps, and limited grading logic.<!-- delta:SF-2026-ARXIV-2605-26079:end --> Author decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-26079:end -->

<!-- books-review:SF-2026-ARXIV-2605-26110:start -->
<!-- existing:SF-2026-ARXIV-2605-26110:start -->已顺读 `books/part-04-training-system/36-distributed-training.md` 及相邻章节 ['books/part-04-training-system/35-checkpoint.md', 'books/part-04-training-system/37-tensor-parallel.md']；当前主干=['本章要回答的问题', '单卡为什么会失败', '从本机协作到分布式执行', '先分清五个通信层次', 'Collective 是群体语义，不是一种算法', '用 Alpha-Beta 模型建立下界直觉', 'Ring、Tree 与 Butterfly 在优化什么', 'MPI、NCCL、UCX、UCC 与 NIXL 的边界']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-26110:end -->
<!-- delta:SF-2026-ARXIV-2605-26110:start -->To address this, we introduce Prism, a plug-in reproducible codebase specifically designed for scalable MCIT research.<!-- delta:SF-2026-ARXIV-2605-26110:end --> Author decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-26110:end -->

<!-- books-review:SF-2026-ARXIV-2605-26112:start -->
<!-- existing:SF-2026-ARXIV-2605-26112:start -->已顺读 `books/part-07-agent/84-agent-platform.md` 及相邻章节 ['books/part-07-agent/83-mcp.md', 'books/part-07-agent/README.md']；当前主干=['本章要回答的问题', 'Agent 改变了平台的控制对象', 'Serving 结束不等于 Agent 任务结束', 'Agent Definition 与 Run Identity', '可编程 Skill 需要输入、状态与副作用契约', '可复用 Skill 不是一个 Prompt 文件', '从 Skill Catalog 到 Competence-aware Orchestration', '从 Trajectory 到 Skill 是一次受治理的 Compilation']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-26112:end -->
<!-- delta:SF-2026-ARXIV-2605-26112:start -->This paper studies the next major bottleneck in agentic AI as system scaling, not only model scaling: the design of auditable, persistent, modular, and verifiable architectures around foundation models.<!-- delta:SF-2026-ARXIV-2605-26112:end --> Author decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-26112:end -->

<!-- books-review:SF-2026-ARXIV-2605-26114:start -->
<!-- existing:SF-2026-ARXIV-2605-26114:start -->已顺读 `books/part-07-agent/84-agent-platform.md` 及相邻章节 ['books/part-07-agent/83-mcp.md', 'books/part-07-agent/README.md']；当前主干=['本章要回答的问题', 'Agent 改变了平台的控制对象', 'Serving 结束不等于 Agent 任务结束', 'Agent Definition 与 Run Identity', '可编程 Skill 需要输入、状态与副作用契约', '可复用 Skill 不是一个 Prompt 文件', '从 Skill Catalog 到 Competence-aware Orchestration', '从 Trajectory 到 Skill 是一次受治理的 Compilation']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-26114:end -->
<!-- delta:SF-2026-ARXIV-2605-26114:start -->We present MobileGym, a browser-hosted, lightweight, fully controllable environment for everyday mobile use, targeting interaction fidelity without replicating proprietary backends.<!-- delta:SF-2026-ARXIV-2605-26114:end --> Author decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-26114:end -->

<!-- books-review:SF-AERIC-ANTICIPATORY-HIDDEN-STATE-MONITORING-FOR-IMPLICIT-HARMFUL-DIALOGUE:start -->
<!-- existing:SF-AERIC-ANTICIPATORY-HIDDEN-STATE-MONITORING-FOR-IMPLICIT-HARMFUL-DIALOGUE:start -->已读取 `books/part-06-ai-infrastructure/67-monitoring.md` 及相邻章节 ['books/part-06-ai-infrastructure/66-evaluation-system.md', 'books/part-06-ai-infrastructure/68-logging.md']；owner 当前主干包含 ['本章要回答的问题', '先定义目标，再选择可测信号', 'Context generator 是 pre-failure sensor identity 的一部分', 'Review notes', '四层指标', 'Autonomy 不是一个纯模型指标', '从单次 Query 指标到 Session-level Search Trajectory Sensor', 'Rate、Errors、Duration 与 Saturation']。仅正文命题用于比较，Review notes 不视为整合。<!-- existing:SF-AERIC-ANTICIPATORY-HIDDEN-STATE-MONITORING-FOR-IMPLICIT-HARMFUL-DIALOGUE:end -->
<!-- delta:SF-AERIC-ANTICIPATORY-HIDDEN-STATE-MONITORING-FOR-IMPLICIT-HARMFUL-DIALOGUE:start -->We study anticipatory same-pass monitoring, where a safety monitor may read hidden states produced during ordinary decoding but may not invoke an additional forward pass through the base model.<!-- delta:SF-AERIC-ANTICIPATORY-HIDDEN-STATE-MONITORING-FOR-IMPLICIT-HARMFUL-DIALOGUE:end --> Independent decision=`Integrate`；prewrite challenge 已通过，不写共享 Books。
<!-- books-review:SF-AERIC-ANTICIPATORY-HIDDEN-STATE-MONITORING-FOR-IMPLICIT-HARMFUL-DIALOGUE:end -->

<!-- books-review:SF-FAITHFUL-OR-FABRICATED-A-CAUSAL-FRAMEWORK-FOR-RATIONALIZATION-BIAS-IN-LL:start -->
<!-- existing:SF-FAITHFUL-OR-FABRICATED-A-CAUSAL-FRAMEWORK-FOR-RATIONALIZATION-BIAS-IN-LL:start -->已读取 `books/part-06-ai-infrastructure/66-evaluation-system.md` 及相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；owner 当前主干包含 ['本章要回答的问题', '为什么“选一个分数”不是评估系统', 'HTTP 成功只是质量判断的第一道门', '从目标到证据，而不是从指标到目标', '第一个不变量：评估声明必须绑定完整对象', 'Evaluation Identity 必须包含 Harness 与 Environment', '第二个不变量：评估结论总是相对于分布', '平均值、切片与不确定性']。仅正文命题用于比较，Review notes 不视为整合。<!-- existing:SF-FAITHFUL-OR-FABRICATED-A-CAUSAL-FRAMEWORK-FOR-RATIONALIZATION-BIAS-IN-LL:end -->
<!-- delta:SF-FAITHFUL-OR-FABRICATED-A-CAUSAL-FRAMEWORK-FOR-RATIONALIZATION-BIAS-IN-LL:start -->We introduce a suite of cue interventions (Blind, Truth, Flip, Placebo, Reveal-After) and tie-aware metrics that quantify outcome anchoring and rationale anchoring, including label-aligned rhetoric and explanation drift, alongside consistency and stereotype-intrusion checks.<!-- delta:SF-FAITHFUL-OR-FABRICATED-A-CAUSAL-FRAMEWORK-FOR-RATIONALIZATION-BIAS-IN-LL:end --> Independent decision=`Integrate`；prewrite challenge 已通过，不写共享 Books。
<!-- books-review:SF-FAITHFUL-OR-FABRICATED-A-CAUSAL-FRAMEWORK-FOR-RATIONALIZATION-BIAS-IN-LL:end -->

<!-- books-review:SF-LGMT-LOGIC-GROUNDED-METAMORPHIC-TESTING-FOR-EVALUATING-THE-REASONING-REL:start -->
<!-- existing:SF-LGMT-LOGIC-GROUNDED-METAMORPHIC-TESTING-FOR-EVALUATING-THE-REASONING-REL:start -->`books/part-06-ai-infrastructure/66-evaluation-system.md` 已以更一般的 PLATFORM-EVALUATION-SYSTEM 演进链承载 `LGMT: Logic-Grounded Metamorphic Testing for Evaluating the Reasoning Reliability of LLMs` 的问题：owner、commit/evidence boundary、失败回退与旧路径共存已经显式化；该 exact-v1 只增加受限实现或 benchmark evidence。<!-- existing:SF-LGMT-LOGIC-GROUNDED-METAMORPHIC-TESTING-FOR-EVALUATING-THE-REASONING-REL:end -->
<!-- delta:SF-LGMT-LOGIC-GROUNDED-METAMORPHIC-TESTING-FOR-EVALUATING-THE-REASONING-REL:start -->We propose LGMT (Logic-Grounded Metamorphic Testing), an oracle-free framework that leverages first-order logic (FOL) to evaluate LLM reasoning.<!-- delta:SF-LGMT-LOGIC-GROUNDED-METAMORPHIC-TESTING-FOR-EVALUATING-THE-REASONING-REL:end --> Final prewrite decision=`No Change — Existing Coverage`。Integrate 只进入 date-local queue；本 reviewer 未修改共享 Books。
<!-- books-review:SF-LGMT-LOGIC-GROUNDED-METAMORPHIC-TESTING-FOR-EVALUATING-THE-REASONING-REL:end -->

<!-- books-review:SF-STOP-COMPARING-LLM-AGENTS-WITHOUT-DISCLOSING-THE-HARNESS:start -->
<!-- existing:SF-STOP-COMPARING-LLM-AGENTS-WITHOUT-DISCLOSING-THE-HARNESS:start -->fresh-context current-books challenge 已读取 `books/part-06-ai-infrastructure/66-evaluation-system.md` 及相邻章节 `books/part-06-ai-infrastructure/65-kai-scheduler.md`, `books/part-06-ai-infrastructure/67-monitoring.md`；canonical owner=`PLATFORM-EVALUATION-SYSTEM`。`Stop Comparing LLM Agents Without Disclosing the Harness` 的 exact-v1 机制为：Second, published benchmarks, industry deployments, and a controlled variance decomposition show that harness-induced variance can substantially exceed model-induced variance, including cases of model ranking reversal.。重读 current owner+adjacent 后，the current body already owns model×harness×environment×scorer identity, paired perturbation, sequential/anytime-valid evidence, effort/cost, claim attribution and release authority；该论文提供受限案例或局部实现，但没有再改变长期 state/data/control owner、evaluation/release contract 或 fallback/coexistence。<!-- existing:SF-STOP-COMPARING-LLM-AGENTS-WITHOUT-DISCLOSING-THE-HARNESS:end -->
<!-- delta:SF-STOP-COMPARING-LLM-AGENTS-WITHOUT-DISCLOSING-THE-HARNESS:start -->Second, published benchmarks, industry deployments, and a controlled variance decomposition show that harness-induced variance can substantially exceed model-induced variance, including cases of model ranking reversal.<!-- delta:SF-STOP-COMPARING-LLM-AGENTS-WITHOUT-DISCLOSING-THE-HARNESS:end --> Decision=`No Change — Existing Coverage`；本轮仅同步 date-local 结构化真值，未修改共享 Books。
<!-- books-review:SF-STOP-COMPARING-LLM-AGENTS-WITHOUT-DISCLOSING-THE-HARNESS:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260526-COVERAGE | fresh-context:owner-replay-20260903 | coverage | coverage:SRC-ARXIV:20260526 | none | raw/retained/closure/withdrawn conservation and initial-created owner mapping independently recounted | passed |
| SA-20260526-EVIDENCE | fresh-context:owner-replay-20260903 | evidence | validator:review-completion-v1 | none | every frozen family has a completed exact-version receipt; blocked=0 | passed |
| SA-20260526-SELECTION | fresh-context:owner-replay-20260903 | deep_analysis_selection | validator:deep-analysis-selection-v1 | none | eligible=169；selected=3；all others retain completed reviews | passed |
| SA-20260526-BOOKS | fresh-context:apr-may-books-20260903 | books | validator:books-comparison-v1;review:SF-2026-ARXIV-2605-25310 | none | — | passed |

## 8. Ignored Noise

- Pre-denominator closures=1038；逐 family 理由保存在 owner receipt。
- Withdrawn=0；只保留审计 closure，不进入候选、评分、Review 或 Books。
- `updated` / current OAI datestamp 的 revision 噪声不拥有 Daily。

## 9. Recommended Action

本日全部 Gate 已闭合，无进一步动作。

## 10. Repository Changes

- Owner receipt（本阶段只读）：`papers/2026/05/_sources/arxiv-owner-replay-20260903/20260526/arxiv-owner-receipt.json`
- Canonical ledger（Books terminal state）：`papers/2026/05/_sources/arxiv-owner-replay-20260903/20260526/canonical-ledger.json`
- Books queue（fresh-context decision）：`papers/2026/05/_sources/arxiv-owner-replay-20260903/BOOKS_WRITEBACK_QUEUE.json`
- Superseded report：`papers/2026/05/_sources/arxiv-owner-replay-20260903/legacy-reports-before-created-owner-reconciliation/2026-05-26.md`
- Books body: no change for the recovered families on this date.

## 11. Open Questions

- 无。

## 12. Sources

- [DataCite REST API](https://api.datacite.org/dois) — initial `created` owner-day proxy；`updated` 只作 revision provenance。
- [arXiv OAI](https://export.arxiv.org/oai2) — identity/date corroboration；current datestamp 不拥有 first-public day。
- [arXiv](https://arxiv.org/) — exact-v1 abstract、HTML/PDF 与 version history。

## 13. Final Status

Completion Status: Complete; Coverage: Closed; Evidence: Passed; Books: Passed; unresolved findings=0
