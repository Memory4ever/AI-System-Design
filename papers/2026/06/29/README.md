# Daily Research — 2026-06-29

**Research Date:** 2026-06-29

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-06-28 09:00:00 ～ 2026-06-29 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；全量枚举与语义筛选冻结候选分母，技术 claim 回到 exact-version primary evidence 与事件时 artifact receipt

**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed，fresh-context Semantic Audit 状态见第 7 节

## Executive Summary

北京时间窗口 [2026-06-28 09:00, 2026-06-29 09:00) 枚举 262 个注册 identity；fresh freeze 为 86 retained + 176 family-specific closures。86/86 exact-v1 Evidence、full-frontier Selection 与 post-write Books audit 已完成。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-06-29 |
| Window End | 2026-06-29 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | daily-v2.1:2026-06-29:3f607817d0a16d2b |
| Denominator Frozen At | 2026-08-29T22:30:00+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-06-28T09:00:00+08:00 | 2026-06-29T09:00:00+08:00 | 2026-08-29T22:30:00+08:00 | frozen DataCite prefix snapshots; exact UTC window; all registered categories | checked | 262 | SF-2026-ARXIV-2606-29142; SF-2026-ARXIV-2606-29150; SF-2026-ARXIV-2606-29151; SF-2026-ARXIV-2606-29158; SF-2026-ARXIV-2606-29159; SF-2026-ARXIV-2606-29171; SF-2026-ARXIV-2606-29176; SF-2026-ARXIV-2606-29178; SF-2026-ARXIV-2606-29182; SF-2026-ARXIV-2606-29184; SF-2026-ARXIV-2606-29193; SF-2026-ARXIV-2606-29194; SF-2026-ARXIV-2606-29196; SF-2026-ARXIV-2606-29207; SF-2026-ARXIV-2606-29215; SF-2026-ARXIV-2606-29222; SF-2026-ARXIV-2606-29223; SF-2026-ARXIV-2606-29225; SF-2026-ARXIV-2606-29228; SF-2026-ARXIV-2606-29237; SF-2026-ARXIV-2606-29238; SF-2026-ARXIV-2606-29239; SF-2026-ARXIV-2606-29251; SF-2026-ARXIV-2606-29270; SF-2026-ARXIV-2606-29275; SF-2026-ARXIV-2606-29278; SF-2026-ARXIV-2606-29279; SF-2026-ARXIV-2606-29280; SF-2026-ARXIV-2606-29282; SF-2026-ARXIV-2606-29296; SF-2026-ARXIV-2606-29315; SF-2026-ARXIV-2606-29328; SF-2026-ARXIV-2606-29337; SF-2026-ARXIV-2606-29340; SF-2026-ARXIV-2606-29350; SF-2026-ARXIV-2606-29354; SF-2026-ARXIV-2606-29366; SF-2026-ARXIV-2606-29377; SF-2026-ARXIV-2606-29399; SF-2026-ARXIV-2606-29403; SF-2026-ARXIV-2606-29424; SF-2026-ARXIV-2606-29425; SF-2026-ARXIV-2606-29441; SF-2026-ARXIV-2606-29445; SF-2026-ARXIV-2606-29472; SF-2026-ARXIV-2606-29476; SF-2026-ARXIV-2606-29481; SF-2026-ARXIV-2606-29490; SF-2026-ARXIV-2606-29493; SF-2026-ARXIV-2606-29501; SF-2026-ARXIV-2606-29502; SF-2026-ARXIV-2606-29506; SF-2026-ARXIV-2606-29520; SF-2026-ARXIV-2606-29522; SF-2026-ARXIV-2606-29526; SF-2026-ARXIV-2606-29532; SF-2026-ARXIV-2606-29537; SF-2026-ARXIV-2606-29538; SF-2026-ARXIV-2606-29541; SF-2026-ARXIV-2606-29544; SF-2026-ARXIV-2606-29554; SF-2026-ARXIV-2606-29563; SF-2026-ARXIV-2606-29565; SF-2026-ARXIV-2606-29567; SF-2026-ARXIV-2606-29571; SF-2026-ARXIV-2606-29573; SF-2026-ARXIV-2606-29580; SF-2026-ARXIV-2606-29581; SF-2026-ARXIV-2606-29592; SF-2026-ARXIV-2606-29601; SF-2026-ARXIV-2606-29602; SF-2026-ARXIV-2606-29604; SF-2026-ARXIV-2606-29605; SF-2026-ARXIV-2606-29623; SF-2026-ARXIV-2606-29629; SF-2026-ARXIV-2606-29645; SF-2026-ARXIV-2606-29646; SF-2026-ARXIV-2606-29648; SF-2026-ARXIV-2606-29649; SF-2026-ARXIV-2606-29652; SF-2026-ARXIV-2606-29654; SF-2026-ARXIV-2606-29657; SF-2026-ARXIV-2606-29661; SF-2026-ARXIV-2606-29679; SF-2026-ARXIV-2606-30686; SF-2026-ARXIV-2606-30689 | snapshots=32,040 records; pages=40; final_cursor=end | 2026-06-29T01:00:00Z | ../_sources/daily-20260629/screening-ledger.json; ../_sources/daily-20260629/denominator-full-semantic-audit-v1.tsv; coverage:SRC-ARXIV:20260629 | — |

<!-- coverage:SRC-ARXIV:20260629:start -->
Fresh reconciliation: 262 = 86 + 176; Core 184=76+108; keyword 26=8+18; route-negative 52=2+50. Fresh-context audit checked all 85 first-freeze retained and all 177 first-freeze closures, including 52/52 route-negative identities; one false negative (2606.29328) was reinstated and the denominator re-froze at 86/176.
<!-- coverage:SRC-ARXIV:20260629:end -->

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-29142 | arXiv:2606.29142v1 | paper-v1:2606.29142 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29142 | self | — | new_in_window | PLATFORM-SECURITY | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-29150 | arXiv:2606.29150v1 | paper-v1:2606.29150 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29150 | self | — | new_in_window | INFER-DECODE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29150 | yes |
| SF-2026-ARXIV-2606-29151 | arXiv:2606.29151v1 | paper-v1:2606.29151 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29151 | self | — | new_in_window | AGENT-RAG | Integrate | books-review:SF-2026-ARXIV-2606-29151 | yes |
| SF-2026-ARXIV-2606-29158 | arXiv:2606.29158v1 | paper-v1:2606.29158 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29158 | self | — | new_in_window | TRAIN-PRETRAINING | Integrate | books-review:SF-2026-ARXIV-2606-29158 | yes |
| SF-2026-ARXIV-2606-29159 | arXiv:2606.29159v1 | paper-v1:2606.29159 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29159 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29159 | yes |
| SF-2026-ARXIV-2606-29171 | arXiv:2606.29171v1 | paper-v1:2606.29171 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29171 | self | — | new_in_window | TRAIN-DATA | Integrate | books-review:SF-2026-ARXIV-2606-29171 | yes |
| SF-2026-ARXIV-2606-29176 | arXiv:2606.29176v1 | paper-v1:2606.29176 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29176 | self | — | new_in_window | TRAIN-PRETRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29176 | yes |
| SF-2026-ARXIV-2606-29178 | arXiv:2606.29178v1 | paper-v1:2606.29178 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29178 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29178 | yes |
| SF-2026-ARXIV-2606-29182 | arXiv:2606.29182v1 | paper-v1:2606.29182 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29182 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29182 | yes |
| SF-2026-ARXIV-2606-29184 | arXiv:2606.29184v1 | paper-v1:2606.29184 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29184 | self | — | new_in_window | TRAIN-LORA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29184 | yes |
| SF-2026-ARXIV-2606-29193 | arXiv:2606.29193v1 | paper-v1:2606.29193 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29193 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29193 | yes |
| SF-2026-ARXIV-2606-29194 | arXiv:2606.29194v1 | paper-v1:2606.29194 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29194 | self | — | new_in_window | AGENT-MULTI-AGENT | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-29196 | arXiv:2606.29196v1 | paper-v1:2606.29196 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29196 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2606-29196 | yes |
| SF-2026-ARXIV-2606-29207 | arXiv:2606.29207v1 | paper-v1:2606.29207 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29207 | self | — | new_in_window | INFER-DECODE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29207 | yes |
| SF-2026-ARXIV-2606-29215 | arXiv:2606.29215v1 | paper-v1:2606.29215 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29215 | self | — | new_in_window | INFER-DECODE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29215 | yes |
| SF-2026-ARXIV-2606-29222 | arXiv:2606.29222v1 | paper-v1:2606.29222 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29222 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29222 | yes |
| SF-2026-ARXIV-2606-29223 | arXiv:2606.29223v1 | paper-v1:2606.29223 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29223 | self | — | new_in_window | INFER-DECODE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29223 | yes |
| SF-2026-ARXIV-2606-29225 | arXiv:2606.29225v1 | paper-v1:2606.29225 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29225 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29225 | yes |
| SF-2026-ARXIV-2606-29228 | arXiv:2606.29228v1 | paper-v1:2606.29228 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29228 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29228 | yes |
| SF-2026-ARXIV-2606-29237 | arXiv:2606.29237v1 | paper-v1:2606.29237 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29237 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29237 | yes |
| SF-2026-ARXIV-2606-29238 | arXiv:2606.29238v1 | paper-v1:2606.29238 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29238 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29238 | yes |
| SF-2026-ARXIV-2606-29239 | arXiv:2606.29239v1 | paper-v1:2606.29239 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29239 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29239 | yes |
| SF-2026-ARXIV-2606-29251 | arXiv:2606.29251v1 | paper-v1:2606.29251 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29251 | self | — | new_in_window | AGENT-CONTEXT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29251 | yes |
| SF-2026-ARXIV-2606-29270 | arXiv:2606.29270v1 | paper-v1:2606.29270 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29270 | self | — | new_in_window | AGENT-MULTI-AGENT | Integrate | books-review:SF-2026-ARXIV-2606-29270 | yes |
| SF-2026-ARXIV-2606-29275 | arXiv:2606.29275v1 | paper-v1:2606.29275 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29275 | self | — | new_in_window | INFER-DECODE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29275 | yes |
| SF-2026-ARXIV-2606-29278 | arXiv:2606.29278v1 | paper-v1:2606.29278 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29278 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29278 | yes |
| SF-2026-ARXIV-2606-29279 | arXiv:2606.29279v1 | paper-v1:2606.29279 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29279 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29279 | yes |
| SF-2026-ARXIV-2606-29280 | arXiv:2606.29280v1 | paper-v1:2606.29280 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29280 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29280 | yes |
| SF-2026-ARXIV-2606-29282 | arXiv:2606.29282v1 | paper-v1:2606.29282 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29282 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29282 | yes |
| SF-2026-ARXIV-2606-29296 | arXiv:2606.29296v1 | paper-v1:2606.29296 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29296 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29296 | yes |
| SF-2026-ARXIV-2606-29315 | arXiv:2606.29315v1 | paper-v1:2606.29315 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29315 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29315 | yes |
| SF-2026-ARXIV-2606-29328 | arXiv:2606.29328v1 | paper-v1:2606.29328 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29328 | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29328 | yes |
| SF-2026-ARXIV-2606-29337 | arXiv:2606.29337v1 | paper-v1:2606.29337 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29337 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29337 | yes |
| SF-2026-ARXIV-2606-29340 | arXiv:2606.29340v1 | paper-v1:2606.29340 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29340 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29340 | yes |
| SF-2026-ARXIV-2606-29350 | arXiv:2606.29350v1 | paper-v1:2606.29350 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29350 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29350 | yes |
| SF-2026-ARXIV-2606-29354 | arXiv:2606.29354v1 | paper-v1:2606.29354 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29354 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29354 | yes |
| SF-2026-ARXIV-2606-29366 | arXiv:2606.29366v1 | paper-v1:2606.29366 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29366 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29366 | yes |
| SF-2026-ARXIV-2606-29377 | arXiv:2606.29377v1 | paper-v1:2606.29377 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29377 | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29377 | yes |
| SF-2026-ARXIV-2606-29399 | arXiv:2606.29399v1 | paper-v1:2606.29399 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29399 | self | — | new_in_window | AGENT-RAG | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-29403 | arXiv:2606.29403v1 | paper-v1:2606.29403 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29403 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29403 | yes |
| SF-2026-ARXIV-2606-29424 | arXiv:2606.29424v1 | paper-v1:2606.29424 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29424 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29424 | yes |
| SF-2026-ARXIV-2606-29425 | arXiv:2606.29425v1 | paper-v1:2606.29425 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29425 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29425 | yes |
| SF-2026-ARXIV-2606-29441 | arXiv:2606.29441v1 | paper-v1:2606.29441 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29441 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29441 | yes |
| SF-2026-ARXIV-2606-29445 | arXiv:2606.29445v1 | paper-v1:2606.29445 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29445 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29445 | yes |
| SF-2026-ARXIV-2606-29472 | arXiv:2606.29472v1 | paper-v1:2606.29472 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29472 | self | — | new_in_window | AGENT-PLATFORM | Integrate | books-review:SF-2026-ARXIV-2606-29472 | yes |
| SF-2026-ARXIV-2606-29476 | arXiv:2606.29476v1 | paper-v1:2606.29476 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29476 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29476 | yes |
| SF-2026-ARXIV-2606-29481 | arXiv:2606.29481v1 | paper-v1:2606.29481 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29481 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29481 | yes |
| SF-2026-ARXIV-2606-29490 | arXiv:2606.29490v1 | paper-v1:2606.29490 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29490 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29490 | yes |
| SF-2026-ARXIV-2606-29493 | arXiv:2606.29493v1 | paper-v1:2606.29493 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29493 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29493 | yes |
| SF-2026-ARXIV-2606-29501 | arXiv:2606.29501v1 | paper-v1:2606.29501 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29501 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29501 | yes |
| SF-2026-ARXIV-2606-29502 | arXiv:2606.29502v1 | paper-v1:2606.29502 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29502 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29502 | yes |
| SF-2026-ARXIV-2606-29506 | arXiv:2606.29506v1 | paper-v1:2606.29506 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29506 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29506 | yes |
| SF-2026-ARXIV-2606-29520 | arXiv:2606.29520v1 | paper-v1:2606.29520 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29520 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29520 | yes |
| SF-2026-ARXIV-2606-29522 | arXiv:2606.29522v1 | paper-v1:2606.29522 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29522 | self | — | new_in_window | AGENT-CONTEXT | Integrate | books-review:SF-2026-ARXIV-2606-29522 | yes |
| SF-2026-ARXIV-2606-29526 | arXiv:2606.29526v1 | paper-v1:2606.29526 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29526 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29526 | yes |
| SF-2026-ARXIV-2606-29532 | arXiv:2606.29532v1 | paper-v1:2606.29532 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29532 | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29532 | yes |
| SF-2026-ARXIV-2606-29537 | arXiv:2606.29537v1 | paper-v1:2606.29537 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29537 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29537 | yes |
| SF-2026-ARXIV-2606-29538 | arXiv:2606.29538v1 | paper-v1:2606.29538 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29538 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29538 | yes |
| SF-2026-ARXIV-2606-29541 | arXiv:2606.29541v1 | paper-v1:2606.29541 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29541 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29541 | yes |
| SF-2026-ARXIV-2606-29544 | arXiv:2606.29544v1 | paper-v1:2606.29544 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29544 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29544 | yes |
| SF-2026-ARXIV-2606-29554 | arXiv:2606.29554v1 | paper-v1:2606.29554 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29554 | self | — | new_in_window | TRAIN-PRETRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29554 | yes |
| SF-2026-ARXIV-2606-29563 | arXiv:2606.29563v1 | paper-v1:2606.29563 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29563 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29563 | yes |
| SF-2026-ARXIV-2606-29565 | arXiv:2606.29565v1 | paper-v1:2606.29565 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29565 | self | — | new_in_window | INFER-REQUEST-LIFECYCLE | Integrate | books-review:SF-2026-ARXIV-2606-29565 | yes |
| SF-2026-ARXIV-2606-29567 | arXiv:2606.29567v1 | paper-v1:2606.29567 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29567 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29567 | yes |
| SF-2026-ARXIV-2606-29571 | arXiv:2606.29571v1 | paper-v1:2606.29571 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29571 | self | — | new_in_window | AGENT-RAG | Integrate | books-review:SF-2026-ARXIV-2606-29571 | yes |
| SF-2026-ARXIV-2606-29573 | arXiv:2606.29573v1 | paper-v1:2606.29573 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29573 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29573 | yes |
| SF-2026-ARXIV-2606-29580 | arXiv:2606.29580v1 | paper-v1:2606.29580 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29580 | self | — | new_in_window | AGENT-RAG | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-29581 | arXiv:2606.29581v1 | paper-v1:2606.29581 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29581 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-29581 | yes |
| SF-2026-ARXIV-2606-29592 | arXiv:2606.29592v1 | paper-v1:2606.29592 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29592 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-29601 | arXiv:2606.29601v1 | paper-v1:2606.29601 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29601 | self | — | new_in_window | AGENT-MULTI-AGENT | Integrate | books-review:SF-2026-ARXIV-2606-29601 | yes |
| SF-2026-ARXIV-2606-29602 | arXiv:2606.29602v1 | paper-v1:2606.29602 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29602 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29602 | yes |
| SF-2026-ARXIV-2606-29604 | arXiv:2606.29604v1 | paper-v1:2606.29604 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29604 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29604 | yes |
| SF-2026-ARXIV-2606-29605 | arXiv:2606.29605v1 | paper-v1:2606.29605 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29605 | self | — | new_in_window | TRAIN-DATA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29605 | yes |
| SF-2026-ARXIV-2606-29623 | arXiv:2606.29623v1 | paper-v1:2606.29623 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29623 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2606-29623 | yes |
| SF-2026-ARXIV-2606-29629 | arXiv:2606.29629v1 | paper-v1:2606.29629 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29629 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29629 | yes |
| SF-2026-ARXIV-2606-29645 | arXiv:2606.29645v1 | paper-v1:2606.29645 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29645 | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29645 | yes |
| SF-2026-ARXIV-2606-29646 | arXiv:2606.29646v1 | paper-v1:2606.29646 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29646 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29646 | yes |
| SF-2026-ARXIV-2606-29648 | arXiv:2606.29648v1 | paper-v1:2606.29648 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29648 | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29648 | yes |
| SF-2026-ARXIV-2606-29649 | arXiv:2606.29649v1 | paper-v1:2606.29649 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29649 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29649 | yes |
| SF-2026-ARXIV-2606-29652 | arXiv:2606.29652v1 | paper-v1:2606.29652 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29652 | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29652 | yes |
| SF-2026-ARXIV-2606-29654 | arXiv:2606.29654v1 | paper-v1:2606.29654 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29654 | self | — | new_in_window | AGENT-MULTI-AGENT | Integrate | books-review:SF-2026-ARXIV-2606-29654 | yes |
| SF-2026-ARXIV-2606-29657 | arXiv:2606.29657v1 | paper-v1:2606.29657 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29657 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29657 | yes |
| SF-2026-ARXIV-2606-29661 | arXiv:2606.29661v1 | paper-v1:2606.29661 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29661 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29661 | yes |
| SF-2026-ARXIV-2606-29679 | arXiv:2606.29679v1 | paper-v1:2606.29679 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29679 | self | — | new_in_window | PLATFORM-MONITORING | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-30686 | arXiv:2606.30686v1 | paper-v1:2606.30686 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-30686 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-30686 | yes |
| SF-2026-ARXIV-2606-30689 | arXiv:2606.30689v1 | paper-v1:2606.30689 | 2026-W26 | 2026-06-28 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-30689 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-30689 | yes |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-29142 | RP-8a6f37eec6feed9d | deep | arXiv:2606.29142v1 | SRC-ARXIV@arXiv:2606.29142v1 | https://arxiv.org/pdf/2606.29142v1 — §III Threat Model Under Regulatory Constraint; IV Architectural Patterns Observed in Production | https://arxiv.org/pdf/2606.29142v1 — §IV Architectural Patterns Observed in Production; V Negative Results and Open Problems | https://arxiv.org/pdf/2606.29142v1 — §V Negative Results and Open Problems; VI Generalization Beyond Finance | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29142 | complete |
| SF-2026-ARXIV-2606-29150 | RP-609a0ae03aebf30c | deep | arXiv:2606.29150v1 | SRC-ARXIV@arXiv:2606.29150v1 | https://arxiv.org/html/2606.29150v1 — §2.1 The flow reasoning model framework; 2.2 Learning to Self-Refine at Inference Time | https://arxiv.org/html/2606.29150v1 — §4 Experiments; G Experimental setup and hyperparameters | https://arxiv.org/html/2606.29150v1 — §6 Discussion; B Test-time scaling: coverage, selection, and sampling-step baselines | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29150 | complete |
| SF-2026-ARXIV-2606-29151 | RP-c18b9eeafc5cc1c1 | deep | arXiv:2606.29151v1 | SRC-ARXIV@arXiv:2606.29151v1 | https://arxiv.org/html/2606.29151v1 — §2.2 System Architecture; 4 Logical Planner; 5 Physical Planner | https://arxiv.org/html/2606.29151v1 — §7 Experiments; 7.1 Experimental Setup | https://arxiv.org/html/2606.29151v1 — §6.3 Robustness; G Validation Set Noise | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29151 | complete |
| SF-2026-ARXIV-2606-29158 | RP-21cf727a5f0fb417 | deep | arXiv:2606.29158v1 | SRC-ARXIV@arXiv:2606.29158v1 | https://arxiv.org/html/2606.29158v1 — §3 Power Laws for Optimal Learning Rates; 6 Explaining Nonlinear Scaling via Implicit Effective Learning Rate Schedule | https://arxiv.org/html/2606.29158v1 — §4 Experiment Design; 5 Main Results | https://arxiv.org/html/2606.29158v1 — §7 Conclusions and Limitations | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29158 | complete |
| SF-2026-ARXIV-2606-29159 | RP-5b74f6528b3000e9 | deep | arXiv:2606.29159v1 | SRC-ARXIV@arXiv:2606.29159v1 | https://arxiv.org/html/2606.29159v1 — §Root-cause-analysis methods on offline benchmarks; reporting-protocol formulation | https://arxiv.org/html/2606.29159v1 — §Benchmark validity and leaderboard instability in ML; system-specific results | https://arxiv.org/html/2606.29159v1 — §6 Discussion, Limitations, and Recommendations | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29159 | complete |
| SF-2026-ARXIV-2606-29171 | RP-d7ff67d6b00399cd | deep | arXiv:2606.29171v1 | SRC-ARXIV@arXiv:2606.29171v1 | https://arxiv.org/html/2606.29171v1 — §3 Symbolic Mechanistic Data Attribution Framework; 3.2 Symbolic Policy Model; 3.3 Influence Computation | https://arxiv.org/html/2606.29171v1 — §4 Experimental Setup; 5 Results | https://arxiv.org/html/2606.29171v1 — §6 Discussion; Symbolic model fidelity and scope; First-order approximation | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29171 | complete |
| SF-2026-ARXIV-2606-29176 | RP-c0063cf1f3ba01c1 | deep | arXiv:2606.29176v1 | SRC-ARXIV@arXiv:2606.29176v1 | https://arxiv.org/html/2606.29176v1 — §Dead-Direction Conditioners; matching the gauge to the architecture | https://arxiv.org/html/2606.29176v1 — §5 Experiments; 5.1 Reading the rate at language-model scale | https://arxiv.org/html/2606.29176v1 — §5.10 Scope and limitations | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29176 | complete |
| SF-2026-ARXIV-2606-29178 | RP-ff09a68509239c76 | deep | arXiv:2606.29178v1 | SRC-ARXIV@arXiv:2606.29178v1 | https://arxiv.org/html/2606.29178v1 — §3 Method; selective memory retention controller | https://arxiv.org/html/2606.29178v1 — §4 Experiments | https://arxiv.org/html/2606.29178v1 — §6 Discussion and Limitations | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29178 | complete |
| SF-2026-ARXIV-2606-29182 | RP-8c7f0d241de2e90a | deep | arXiv:2606.29182v1 | SRC-ARXIV@arXiv:2606.29182v1 | https://arxiv.org/html/2606.29182v1 — §3.1.1 In-Context Memory; continual belief-update mechanism | https://arxiv.org/html/2606.29182v1 — §3.1.2 Evaluation: Reducing Surprisal Under Non-Stationary Beliefs | https://arxiv.org/html/2606.29182v1 — §6 Limitations | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29182 | complete |
| SF-2026-ARXIV-2606-29184 | RP-9c5a65bfa597b647 | deep | arXiv:2606.29184v1 | SRC-ARXIV@arXiv:2606.29184v1 | https://arxiv.org/html/2606.29184v1 — §IV BaRA: Bayesian Adaptive Rank Allocation | https://arxiv.org/html/2606.29184v1 — §VI Experiments | https://arxiv.org/html/2606.29184v1 — §III-C Limitations of Bayesian LoRA Methods | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29184 | complete |
| SF-2026-ARXIV-2606-29193 | RP-62de3af2063e9341 | deep | arXiv:2606.29193v1 | SRC-ARXIV@arXiv:2606.29193v1 | https://arxiv.org/html/2606.29193v1 — §3 Design Principles; microservice-agent evaluation harness | https://arxiv.org/html/2606.29193v1 — §4 Evaluation; 4.4 Evaluation Metric | https://arxiv.org/html/2606.29193v1 — §6 Discussion | https://www.aiops.cn/gitlab/aiops-live-benchmark/agenticopseval. | claim:SF-2026-ARXIV-2606-29193 | complete |
| SF-2026-ARXIV-2606-29194 | RP-c585576eaf1a2c03 | deep | arXiv:2606.29194v1 | SRC-ARXIV@arXiv:2606.29194v1 | https://arxiv.org/html/2606.29194v1 — §Sealed-joint multi-agent search protocol; merge and isolation mechanism | https://arxiv.org/html/2606.29194v1 — §Statistical inference and out-of-sample evaluation | https://arxiv.org/html/2606.29194v1 — §6 Discussion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29194 | complete |
| SF-2026-ARXIV-2606-29196 | RP-7edc076758df6d38 | deep | arXiv:2606.29196v1 | SRC-ARXIV@arXiv:2606.29196v1 | https://arxiv.org/html/2606.29196v1 — §2 Evaluation-Awareness Representations; scale-dependent probe construction | https://arxiv.org/html/2606.29196v1 — §3 Experimental Setup; 4 Results | https://arxiv.org/html/2606.29196v1 — §5 Discussion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29196 | complete |
| SF-2026-ARXIV-2606-29207 | RP-e454caec3c98395e | deep | arXiv:2606.29207v1 | SRC-ARXIV@arXiv:2606.29207v1 | https://arxiv.org/html/2606.29207v1 — §3 System Overview; KernelFlume generation and verification pipeline | https://arxiv.org/html/2606.29207v1 — §6 Evaluation | https://arxiv.org/html/2606.29207v1 — §2.4 Limitations of Existing Elastic Scaling | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29207 | complete |
| SF-2026-ARXIV-2606-29215 | RP-e1705dedb6a9c2fd | deep | arXiv:2606.29215v1 | SRC-ARXIV@arXiv:2606.29215v1 | https://arxiv.org/html/2606.29215v1 — §3 Methodology; multi-block diffusion language-model decoding | https://arxiv.org/html/2606.29215v1 — §4 Experiments | https://arxiv.org/html/2606.29215v1 — §5 Conclusion and stated speed-quality scope | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29215 | complete |
| SF-2026-ARXIV-2606-29222 | RP-c824d391e225c04b | deep | arXiv:2606.29222v1 | SRC-ARXIV@arXiv:2606.29222v1 | https://arxiv.org/html/2606.29222v1 — §III Contextual-Memory Architecture; memory-conditioned robot control | https://arxiv.org/html/2606.29222v1 — §V Experiments | https://arxiv.org/html/2606.29222v1 — §VI Conclusion and deployment scope | https://github.com/BBD00/core_planner. | claim:SF-2026-ARXIV-2606-29222 | complete |
| SF-2026-ARXIV-2606-29223 | RP-2bc35c4f8ee33ba4 | deep | arXiv:2606.29223v1 | SRC-ARXIV@arXiv:2606.29223v1 | https://arxiv.org/html/2606.29223v1 — §3 Method; depth-exploration controller | https://arxiv.org/html/2606.29223v1 — §4 Experiment | https://arxiv.org/html/2606.29223v1 — §E Limitations and discussion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29223 | complete |
| SF-2026-ARXIV-2606-29225 | RP-665169d00e911e7e | deep | arXiv:2606.29225v1 | SRC-ARXIV@arXiv:2606.29225v1 | https://arxiv.org/html/2606.29225v1 — §3 Method; PolicyGuard pre-commit policy gate | https://arxiv.org/html/2606.29225v1 — §4 Experiments | https://arxiv.org/html/2606.29225v1 — §Discussion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29225 | complete |
| SF-2026-ARXIV-2606-29228 | RP-e43a9c98d9a755f5 | deep | arXiv:2606.29228v1 | SRC-ARXIV@arXiv:2606.29228v1 | https://arxiv.org/html/2606.29228v1 — §3 Evaluation Inconsistency in Diffusion Large Language Models | https://arxiv.org/html/2606.29228v1 — §3 Evaluation Inconsistency; 4 Experiments | https://arxiv.org/html/2606.29228v1 — §5 Discussion; speed-quality trade-off counterevidence | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29228 | complete |
| SF-2026-ARXIV-2606-29237 | RP-31917d2ace09184f | deep | arXiv:2606.29237v1 | SRC-ARXIV@arXiv:2606.29237v1 | https://arxiv.org/html/2606.29237v1 — §III Methodology; motion-permanence world state | https://arxiv.org/html/2606.29237v1 — §IV Experiments | https://arxiv.org/html/2606.29237v1 — §V Limitations and Future Work | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29237 | complete |
| SF-2026-ARXIV-2606-29238 | RP-4e6c956d1a2a472e | deep | arXiv:2606.29238v1 | SRC-ARXIV@arXiv:2606.29238v1 | https://arxiv.org/html/2606.29238v1 — §2.1 MDP Formulation for Text Generation; GRPO analysis | https://arxiv.org/html/2606.29238v1 — §7 Experiments | https://arxiv.org/html/2606.29238v1 — §6 Multi-Turn Limitation | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29238 | complete |
| SF-2026-ARXIV-2606-29239 | RP-555ae4fea3e0e6e0 | deep | arXiv:2606.29239v1 | SRC-ARXIV@arXiv:2606.29239v1 | https://arxiv.org/html/2606.29239v1 — §4.1 Differentiable Rounding Framework; QuantGuard calibration | https://arxiv.org/html/2606.29239v1 — §3.2 Empirical Motivation: The Role of Rounding Errors in LLM Quantization | https://arxiv.org/html/2606.29239v1 — §3.1 Threat Model | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29239 | complete |
| SF-2026-ARXIV-2606-29251 | RP-ddc11dbdabac40d3 | deep | arXiv:2606.29251v1 | SRC-ARXIV@arXiv:2606.29251v1 | https://arxiv.org/html/2606.29251v1 — §3.1 Problem Formulation; compression-fidelity decomposition | https://arxiv.org/html/2606.29251v1 — §4 Experiments | https://arxiv.org/html/2606.29251v1 — §7 Limitations | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29251 | complete |
| SF-2026-ARXIV-2606-29270 | RP-9f92eb0ba8a818d5 | deep | arXiv:2606.29270v1 | SRC-ARXIV@arXiv:2606.29270v1 | https://arxiv.org/html/2606.29270v1 — §3 Our Method; 3.3 The Debate Fingerprint; 3.4 Cure Phase: Meta-Classifier and Threshold Strategy | https://arxiv.org/html/2606.29270v1 — §4 Experiments and Results; 4.1 Datasets and Debate Configuration; 5.5 Multi-Seed Stability | https://arxiv.org/html/2606.29270v1 — §6.2 Limitations | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29270 | complete |
| SF-2026-ARXIV-2606-29275 | RP-637f46dec5e9e6a5 | deep | arXiv:2606.29275v1 | SRC-ARXIV@arXiv:2606.29275v1 | https://arxiv.org/html/2606.29275v1 — §3 Methodology: Adaptive Block Diffusion | https://arxiv.org/html/2606.29275v1 — §5 Experiments | https://arxiv.org/html/2606.29275v1 — §4.4 Limitation of Block Diffusion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29275 | complete |
| SF-2026-ARXIV-2606-29278 | RP-cc38cf459a9073a3 | deep | arXiv:2606.29278v1 | SRC-ARXIV@arXiv:2606.29278v1 | https://arxiv.org/html/2606.29278v1 — §3 Benchmark Design; complexity-ceiling protocol | https://arxiv.org/html/2606.29278v1 — §Trace-level evaluation and structural uncertainty | https://arxiv.org/html/2606.29278v1 — §5 Discussion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29278 | complete |
| SF-2026-ARXIV-2606-29279 | RP-aa1fcf87be4ff47c | deep | arXiv:2606.29279v1 | SRC-ARXIV@arXiv:2606.29279v1 | https://arxiv.org/html/2606.29279v1 — §Agent memory and compression; hearsay-provenance mechanism | https://arxiv.org/html/2606.29279v1 — §3 Results | https://arxiv.org/html/2606.29279v1 — §Conclusion and source-provenance scope | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29279 | complete |
| SF-2026-ARXIV-2606-29280 | RP-818794d350b7867b | deep | arXiv:2606.29280v1 | SRC-ARXIV@arXiv:2606.29280v1 | https://arxiv.org/html/2606.29280v1 — §3 System Architecture; high-stakes escalation pipeline | https://arxiv.org/html/2606.29280v1 — §Evaluation methodology and outcome study | https://arxiv.org/html/2606.29280v1 — §2.4 Machine Learning for Student Outcome Prediction: Benchmarks and Limits | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29280 | complete |
| SF-2026-ARXIV-2606-29282 | RP-6e3e08ce41c7f948 | deep | arXiv:2606.29282v1 | SRC-ARXIV@arXiv:2606.29282v1 | https://arxiv.org/html/2606.29282v1 — §4 Methodology; concept-erasure and reactivation tests | https://arxiv.org/html/2606.29282v1 — §5 Experiments | https://arxiv.org/html/2606.29282v1 — §B Discussion on MACE Adaptation | https://github.com/coziiizz/ScaleErasure. | claim:SF-2026-ARXIV-2606-29282 | complete |
| SF-2026-ARXIV-2606-29296 | RP-54ca1ff0ae3285fe | deep | arXiv:2606.29296v1 | SRC-ARXIV@arXiv:2606.29296v1 | https://arxiv.org/html/2606.29296v1 — §4 Method: The PASS Middleware | https://arxiv.org/html/2606.29296v1 — §Empirical scope; evaluation protocol | https://arxiv.org/html/2606.29296v1 — §6 Discussion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29296 | complete |
| SF-2026-ARXIV-2606-29315 | RP-2db564eff9a713e0 | deep | arXiv:2606.29315v1 | SRC-ARXIV@arXiv:2606.29315v1 | https://arxiv.org/pdf/2606.29315v1 — §3 Hierarchical Experimentalist Agents; actor, evolver, retriever and skill bank | https://arxiv.org/pdf/2606.29315v1 — §4 Experiments and Results on Interphyre | https://arxiv.org/pdf/2606.29315v1 — §A.5 Design Principles; domain-agnostic inputs and simulator-only evidence boundary | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29315 | complete |
| SF-2026-ARXIV-2606-29328 | RP-eaf6d5f2ca6d1935 | deep | arXiv:2606.29328v1 | SRC-ARXIV@arXiv:2606.29328v1 | https://arxiv.org/html/2606.29328v1 — §III Problem Formulation; III-B The Single-Point Coverage Barrier; IV Method | https://arxiv.org/html/2606.29328v1 — §V Experiments; V-A Experimental Settings; V-D Full-Wikipedia Test; V-J Context-Budget Robustness | https://arxiv.org/html/2606.29328v1 — §VI Conclusion; V-K Generalization Across Sub-query Generators | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29328 | complete |
| SF-2026-ARXIV-2606-29337 | RP-5c513869ecc173ab | deep | arXiv:2606.29337v1 | SRC-ARXIV@arXiv:2606.29337v1 | https://arxiv.org/html/2606.29337v1 — §III Method; W4A4 quantization path | https://arxiv.org/html/2606.29337v1 — §IV Evaluation and Results | https://arxiv.org/html/2606.29337v1 — §IV-B Discussion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29337 | complete |
| SF-2026-ARXIV-2606-29340 | RP-a8882e022967aad1 | deep | arXiv:2606.29340v1 | SRC-ARXIV@arXiv:2606.29340v1 | https://arxiv.org/html/2606.29340v1 — §Method; off-policy sample-distribution controller | https://arxiv.org/html/2606.29340v1 — §Experiments | https://arxiv.org/html/2606.29340v1 — §Discussion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29340 | complete |
| SF-2026-ARXIV-2606-29350 | RP-3fa9cb3aa8222359 | deep | arXiv:2606.29350v1 | SRC-ARXIV@arXiv:2606.29350v1 | https://arxiv.org/html/2606.29350v1 — §III Method; visual-token merging for VLA | https://arxiv.org/html/2606.29350v1 — §IV Experiments | https://arxiv.org/html/2606.29350v1 — §V Conclusion and Discussion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29350 | complete |
| SF-2026-ARXIV-2606-29354 | RP-ab160dfde90f8b0a | deep | arXiv:2606.29354v1 | SRC-ARXIV@arXiv:2606.29354v1 | https://arxiv.org/html/2606.29354v1 — §2 Methodology; symbolic communication protocol | https://arxiv.org/html/2606.29354v1 — §4 Experiments | https://arxiv.org/html/2606.29354v1 — §5 Conclusion and Limitations | https://github.com/pzqpzq/LSF_MDia | claim:SF-2026-ARXIV-2606-29354 | complete |
| SF-2026-ARXIV-2606-29366 | RP-3267246ddae6e272 | deep | arXiv:2606.29366v1 | SRC-ARXIV@arXiv:2606.29366v1 | https://arxiv.org/html/2606.29366v1 — §Solver-verified LLM workflow; formal verification path | https://arxiv.org/html/2606.29366v1 — §6 Computational Evaluation | https://arxiv.org/html/2606.29366v1 — §Conclusion and solver-coverage boundary | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29366 | complete |
| SF-2026-ARXIV-2606-29377 | RP-88fa766caf8ae12f | deep | arXiv:2606.29377v1 | SRC-ARXIV@arXiv:2606.29377v1 | https://arxiv.org/html/2606.29377v1 — §2 Methodology; retrieval-failure repair loop | https://arxiv.org/html/2606.29377v1 — §3 Experiments | https://arxiv.org/html/2606.29377v1 — §Conclusion and evaluated-query scope | https://github.com/CyberScienceLab/D2R-RAG/. | claim:SF-2026-ARXIV-2606-29377 | complete |
| SF-2026-ARXIV-2606-29399 | RP-62d75df8b05d22f4 | deep | arXiv:2606.29399v1 | SRC-ARXIV@arXiv:2606.29399v1 | https://arxiv.org/html/2606.29399v1 — §3 Method; multimodal document-RAG planning | https://arxiv.org/html/2606.29399v1 — §Experiments and multimodal document evaluation | https://arxiv.org/html/2606.29399v1 — §7 Limitations | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29399 | complete |
| SF-2026-ARXIV-2606-29403 | RP-1b83e47112eb3841 | deep | arXiv:2606.29403v1 | SRC-ARXIV@arXiv:2606.29403v1 | https://arxiv.org/html/2606.29403v1 — §Conformal failure mode and design knob; calibration method | https://arxiv.org/html/2606.29403v1 — §4 Experiments | https://arxiv.org/html/2606.29403v1 — §Conclusion and exchangeability boundary | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29403 | complete |
| SF-2026-ARXIV-2606-29424 | RP-f56f728db4709827 | deep | arXiv:2606.29424v1 | SRC-ARXIV@arXiv:2606.29424v1 | https://arxiv.org/html/2606.29424v1 — §2.1 Problem Formulation; EntroRouter | https://arxiv.org/html/2606.29424v1 — §4 Experiments | https://arxiv.org/html/2606.29424v1 — §5 Discussion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29424 | complete |
| SF-2026-ARXIV-2606-29425 | RP-ca573317f519e527 | deep | arXiv:2606.29425v1 | SRC-ARXIV@arXiv:2606.29425v1 | https://arxiv.org/html/2606.29425v1 — §3.1 Model Architecture; mixture-of-debaters routing | https://arxiv.org/html/2606.29425v1 — §4 Experiments | https://arxiv.org/html/2606.29425v1 — §Conclusion and tested-debater scope | https://github.com/YongLD/MoD. | claim:SF-2026-ARXIV-2606-29425 | complete |
| SF-2026-ARXIV-2606-29441 | RP-5cede91b8324a308 | deep | arXiv:2606.29441v1 | SRC-ARXIV@arXiv:2606.29441v1 | https://arxiv.org/html/2606.29441v1 — §Activation-defense mechanism and intervention pipeline | https://arxiv.org/html/2606.29441v1 — §4 Experimental Setup; 5.1 No Single-Mechanism Paradigm Dominates | https://arxiv.org/html/2606.29441v1 — §6 Discussion and Limitations | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29441 | complete |
| SF-2026-ARXIV-2606-29445 | RP-4703ffdf106800f9 | deep | arXiv:2606.29445v1 | SRC-ARXIV@arXiv:2606.29445v1 | https://arxiv.org/html/2606.29445v1 — §3 Method; long-video GUI-agent observation/evaluation | https://arxiv.org/html/2606.29445v1 — §4 Experiments | https://arxiv.org/html/2606.29445v1 — §Conclusion and benchmark-domain scope | https://github.com/VG-GUI-TASKER/VG-GUI-TASKER. | claim:SF-2026-ARXIV-2606-29445 | complete |
| SF-2026-ARXIV-2606-29472 | RP-f734b1ee4374de1e | deep | arXiv:2606.29472v1 | SRC-ARXIV@arXiv:2606.29472v1 | https://arxiv.org/pdf/2606.29472v1 — §3 Agent-Computer Observation Interface: gated keyframes, audio transcription and persistent narration | https://arxiv.org/pdf/2606.29472v1 — §4 DynaCU-Bench design; 5 Main results and ablations | https://arxiv.org/pdf/2606.29472v1 — §5 per-model component ablation: keyframe regression through image-token dilution | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29472 | complete |
| SF-2026-ARXIV-2606-29476 | RP-fadcaac41b9b7d92 | deep | arXiv:2606.29476v1 | SRC-ARXIV@arXiv:2606.29476v1 | https://arxiv.org/html/2606.29476v1 — §3 The CRAFT Method | https://arxiv.org/html/2606.29476v1 — §5 Experiments | https://arxiv.org/html/2606.29476v1 — §7 Discussion and Limitations | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29476 | complete |
| SF-2026-ARXIV-2606-29481 | RP-73031fa2f7536185 | deep | arXiv:2606.29481v1 | SRC-ARXIV@arXiv:2606.29481v1 | https://arxiv.org/html/2606.29481v1 — §2 Methodology; HIPPO update policy | https://arxiv.org/html/2606.29481v1 — §3 Experimental Setup | https://arxiv.org/html/2606.29481v1 — §2.2 Direct KL Optimization and Its Limitations | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29481 | complete |
| SF-2026-ARXIV-2606-29490 | RP-159d3c81ea76f992 | deep | arXiv:2606.29490v1 | SRC-ARXIV@arXiv:2606.29490v1 | https://arxiv.org/html/2606.29490v1 — §1.1 Supplemental Methods; confidence-commitment calibration | https://arxiv.org/html/2606.29490v1 — §1.2 Supplemental Results | https://arxiv.org/html/2606.29490v1 — §Conclusion and evaluated-distribution scope | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29490 | complete |
| SF-2026-ARXIV-2606-29493 | RP-d267ebdec6d59db2 | deep | arXiv:2606.29493v1 | SRC-ARXIV@arXiv:2606.29493v1 | https://arxiv.org/html/2606.29493v1 — §Detection framework; formal benchmark audit protocol | https://arxiv.org/html/2606.29493v1 — §2 What Formal Benchmarking Certifies (and What It Does Not) | https://arxiv.org/html/2606.29493v1 — §7 Limitations | https://github.com/Shashi456/atp-checkers. | claim:SF-2026-ARXIV-2606-29493 | complete |
| SF-2026-ARXIV-2606-29501 | RP-72d76d92a2d24dae | deep | arXiv:2606.29501v1 | SRC-ARXIV@arXiv:2606.29501v1 | https://arxiv.org/html/2606.29501v1 — §3 Methodology; action-conditioned world-model rollout | https://arxiv.org/html/2606.29501v1 — §4 Experiments | https://arxiv.org/html/2606.29501v1 — §4.5 Ablations and discussions | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29501 | complete |
| SF-2026-ARXIV-2606-29502 | RP-6cef183dfa5e83f4 | deep | arXiv:2606.29502v1 | SRC-ARXIV@arXiv:2606.29502v1 | https://arxiv.org/html/2606.29502v1 — §4 Method: UCOB; skill discovery and composition | https://arxiv.org/html/2606.29502v1 — §6 Experiments | https://arxiv.org/html/2606.29502v1 — §Conclusion and evaluated-environment boundary | https://github.com/TU2021/UCOB. | claim:SF-2026-ARXIV-2606-29502 | complete |
| SF-2026-ARXIV-2606-29506 | RP-d3a1efee80279c53 | deep | arXiv:2606.29506v1 | SRC-ARXIV@arXiv:2606.29506v1 | https://arxiv.org/html/2606.29506v1 — §Cross-dataset audit design and grouped-split protocol | https://arxiv.org/html/2606.29506v1 — §IV Results | https://arxiv.org/html/2606.29506v1 — §VII Discussion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29506 | complete |
| SF-2026-ARXIV-2606-29520 | RP-a10a115a38cec145 | deep | arXiv:2606.29520v1 | SRC-ARXIV@arXiv:2606.29520v1 | https://arxiv.org/html/2606.29520v1 — §SAKE evaluation decomposition and safety-knowledge tests | https://arxiv.org/html/2606.29520v1 — §Benchmark construction and evaluation | https://arxiv.org/html/2606.29520v1 — §7 Threats to Validity | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29520 | complete |
| SF-2026-ARXIV-2606-29522 | RP-65901f07c59f5abc | deep | arXiv:2606.29522v1 | SRC-ARXIV@arXiv:2606.29522v1 | https://arxiv.org/html/2606.29522v1 — §6 Mechanism and alignment interpretation; scratchpad intervention | https://arxiv.org/html/2606.29522v1 — §5 Results | https://arxiv.org/html/2606.29522v1 — §Conclusion and intervention-identifiability scope | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29522 | complete |
| SF-2026-ARXIV-2606-29526 | RP-9e4f6c402d13d91d | deep | arXiv:2606.29526v1 | SRC-ARXIV@arXiv:2606.29526v1 | https://arxiv.org/html/2606.29526v1 — §Monotonic Inference Policy objective and training-policy analysis | https://arxiv.org/html/2606.29526v1 — §5 Experiments | https://arxiv.org/html/2606.29526v1 — §Limitations | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29526 | complete |
| SF-2026-ARXIV-2606-29532 | RP-c331f6b3dbebb328 | deep | arXiv:2606.29532v1 | SRC-ARXIV@arXiv:2606.29532v1 | https://arxiv.org/html/2606.29532v1 — §Semantic-join planning and verification method | https://arxiv.org/html/2606.29532v1 — §4 Evaluation | https://arxiv.org/html/2606.29532v1 — §Conclusion and evaluated-database scope | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29532 | complete |
| SF-2026-ARXIV-2606-29537 | RP-9480043860a2a363 | deep | arXiv:2606.29537v1 | SRC-ARXIV@arXiv:2606.29537v1 | https://arxiv.org/html/2606.29537v1 — §2.1 Task Design and Construction; OSWorld 2.0 environment | https://arxiv.org/html/2606.29537v1 — §2 OSWorld 2.0 Benchmark; evaluation protocol | https://arxiv.org/html/2606.29537v1 — §6 Limitations | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29537 | complete |
| SF-2026-ARXIV-2606-29538 | RP-9d8177552f19af12 | deep | arXiv:2606.29538v1 | SRC-ARXIV@arXiv:2606.29538v1 | https://arxiv.org/html/2606.29538v1 — §3 Method; Resource2Skill discovery and compilation | https://arxiv.org/html/2606.29538v1 — §4 Experiments | https://arxiv.org/html/2606.29538v1 — §M Limitations | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29538 | complete |
| SF-2026-ARXIV-2606-29541 | RP-7e1bfd70b6d7fbe7 | deep | arXiv:2606.29541v1 | SRC-ARXIV@arXiv:2606.29541v1 | https://arxiv.org/html/2606.29541v1 — §3 Mechanism: Role-Label-Conditioned Routing | https://arxiv.org/html/2606.29541v1 — §5 Experiments | https://arxiv.org/html/2606.29541v1 — §6 Discussion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29541 | complete |
| SF-2026-ARXIV-2606-29544 | RP-5f64c3f6d2057550 | deep | arXiv:2606.29544v1 | SRC-ARXIV@arXiv:2606.29544v1 | https://arxiv.org/html/2606.29544v1 — §2 Method; production robustness protocol | https://arxiv.org/html/2606.29544v1 — §3 Results | https://arxiv.org/html/2606.29544v1 — §Conclusion and tested-shift boundary | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29544 | complete |
| SF-2026-ARXIV-2606-29554 | RP-83192e77e1afc5ac | deep | arXiv:2606.29554v1 | SRC-ARXIV@arXiv:2606.29554v1 | https://arxiv.org/html/2606.29554v1 — §Optimizer-shuffle exponent and mechanism | https://arxiv.org/html/2606.29554v1 — §5 Empirical evidence | https://arxiv.org/html/2606.29554v1 — §7 Discussion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29554 | complete |
| SF-2026-ARXIV-2606-29563 | RP-8d93eea7e0df738f | deep | arXiv:2606.29563v1 | SRC-ARXIV@arXiv:2606.29563v1 | https://arxiv.org/html/2606.29563v1 — §3 Coverage Hypothesis for KV-Cache Eviction; 4 KV Cache Eviction with Coverage | https://arxiv.org/html/2606.29563v1 — §5 Experiments; 5.1 Experimental setup | https://arxiv.org/html/2606.29563v1 — §5.3 Discussion; 5.3.5 Computational Complexity | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29563 | complete |
| SF-2026-ARXIV-2606-29565 | RP-4ac5a15d121d6d0f | deep | arXiv:2606.29565v1 | SRC-ARXIV@arXiv:2606.29565v1 | https://arxiv.org/html/2606.29565v1 — §2 Problem Formulation; speculative pre-positioning state machine | https://arxiv.org/html/2606.29565v1 — §4 Experimental Setup; 5 Evaluation | https://arxiv.org/html/2606.29565v1 — §6 Discussion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29565 | complete |
| SF-2026-ARXIV-2606-29567 | RP-803df0d78ddcc81a | deep | arXiv:2606.29567v1 | SRC-ARXIV@arXiv:2606.29567v1 | https://arxiv.org/html/2606.29567v1 — §3 System Design; SurrogateShield and ShadowMap | https://arxiv.org/html/2606.29567v1 — §4 Evaluation Methodology | https://arxiv.org/html/2606.29567v1 — §6 Discussion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29567 | complete |
| SF-2026-ARXIV-2606-29571 | RP-31d483c83ac73494 | deep | arXiv:2606.29571v1 | SRC-ARXIV@arXiv:2606.29571v1 | https://arxiv.org/html/2606.29571v1 — §3.4 Geometry measures; 4.3 The cause: a few crowded directions; 4.4 Mechanism and consequences | https://arxiv.org/html/2606.29571v1 — §3.1 Encoders; 3.3 Datasets; 3.5 Scoring | https://arxiv.org/html/2606.29571v1 — §6 Limitations | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29571 | complete |
| SF-2026-ARXIV-2606-29573 | RP-62cf4d2ea072222d | deep | arXiv:2606.29573v1 | SRC-ARXIV@arXiv:2606.29573v1 | https://arxiv.org/html/2606.29573v1 — §GranFact hierarchy-aware evaluation and reliability-prioritized preference optimization | https://arxiv.org/html/2606.29573v1 — §2.1 MLLM Benchmarks; experiments | https://arxiv.org/html/2606.29573v1 — §Conclusion and expert-verified benchmark scope | https://github.com/WeiWu2025/GranFact | claim:SF-2026-ARXIV-2606-29573 | complete |
| SF-2026-ARXIV-2606-29580 | RP-ee0cb1445098ef3c | deep | arXiv:2606.29580v1 | SRC-ARXIV@arXiv:2606.29580v1 | https://arxiv.org/pdf/2606.29580v1 — §2 On-device RAG system; 3 corpus and deployed configuration | https://arxiv.org/pdf/2606.29580v1 — §4 Evaluation Methodology; Sections 5-8 component results | https://arxiv.org/pdf/2606.29580v1 — §9 Discussion; 10 Limitations and Future Work | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29580 | complete |
| SF-2026-ARXIV-2606-29581 | RP-dbb67845d6131a66 | deep | arXiv:2606.29581v1 | SRC-ARXIV@arXiv:2606.29581v1 | https://arxiv.org/html/2606.29581v1 — §3 Methodology; quantization-temperature factorial design | https://arxiv.org/html/2606.29581v1 — §3.1 Experimental Design; 4 Results | https://arxiv.org/html/2606.29581v1 — §5 Discussion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29581 | complete |
| SF-2026-ARXIV-2606-29592 | RP-842dcdabcceb47cb | deep | arXiv:2606.29592v1 | SRC-ARXIV@arXiv:2606.29592v1 | https://arxiv.org/html/2606.29592v1 — §3 Method; perception-navigation-planning decomposition | https://arxiv.org/html/2606.29592v1 — §4 Experiments | https://arxiv.org/html/2606.29592v1 — §5 Limitations | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29592 | complete |
| SF-2026-ARXIV-2606-29601 | RP-c4028da799f220c5 | deep | arXiv:2606.29601v1 | SRC-ARXIV@arXiv:2606.29601v1 | https://arxiv.org/html/2606.29601v1 — §Approach; sayso, nono and nogo protocol semantics | https://arxiv.org/html/2606.29601v1 — §6.2 Empirical Results; safety and liveness procedures | https://arxiv.org/html/2606.29601v1 — §7 Discussion: Conclusion and Perspectives | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29601 | complete |
| SF-2026-ARXIV-2606-29602 | RP-86fc907325d11bbd | deep | arXiv:2606.29602v1 | SRC-ARXIV@arXiv:2606.29602v1 | https://arxiv.org/html/2606.29602v1 — §III Methodology; multilingual and obfuscated prompt-injection matrix | https://arxiv.org/html/2606.29602v1 — §II-D Empirical Evaluations of LLM Safety; IV Results | https://arxiv.org/html/2606.29602v1 — §V Discussion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29602 | complete |
| SF-2026-ARXIV-2606-29604 | RP-c24b61c272a7c0fb | deep | arXiv:2606.29604v1 | SRC-ARXIV@arXiv:2606.29604v1 | https://arxiv.org/html/2606.29604v1 — §3 Method; Causal Perturbative Elicitation | https://arxiv.org/html/2606.29604v1 — §Experimental setup; latent-behavior evaluation | https://arxiv.org/html/2606.29604v1 — §Conclusion and model-organism scope | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29604 | complete |
| SF-2026-ARXIV-2606-29605 | RP-fd558e45f22b4df7 | deep | arXiv:2606.29605v1 | SRC-ARXIV@arXiv:2606.29605v1 | https://arxiv.org/html/2606.29605v1 — §2.2 Two distinct redundancy mechanisms; provenance decomposition | https://arxiv.org/html/2606.29605v1 — §2 Results; downstream equal-token adaptation test | https://arxiv.org/html/2606.29605v1 — §3 Discussion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29605 | complete |
| SF-2026-ARXIV-2606-29623 | RP-2b07f6eeb9f88278 | deep | arXiv:2606.29623v1 | SRC-ARXIV@arXiv:2606.29623v1 | https://arxiv.org/html/2606.29623v1 — §3 Data-Driven Subset Simulation; 4 Theoretical Guarantees; C Martingale Theory for SCARCE | https://arxiv.org/html/2606.29623v1 — §5.1 Experiment Setup; 6.1 Experiment Setup; 6.2 Simulation Results | https://arxiv.org/html/2606.29623v1 — §7 Conclusion, Limitations, and Extensions; E LLM Transfer Challenges | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29623 | complete |
| SF-2026-ARXIV-2606-29629 | RP-c3a3356401bb627f | deep | arXiv:2606.29629v1 | SRC-ARXIV@arXiv:2606.29629v1 | https://arxiv.org/pdf/2606.29629v1 — §III Tri-serve software DVFS controller: stall-, arithmetic-intensity-, and thermal-aware policies | https://arxiv.org/pdf/2606.29629v1 — §II-C1 Frequency-locked Roofline Benchmarking; IV Evaluation | https://arxiv.org/pdf/2606.29629v1 — §V Conclusion; evaluated Qwen-Omni/GPU-cluster boundary | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29629 | complete |
| SF-2026-ARXIV-2606-29645 | RP-302b8f9667ba430b | deep | arXiv:2606.29645v1 | SRC-ARXIV@arXiv:2606.29645v1 | https://arxiv.org/html/2606.29645v1 — §3 Method; RAG enrichment decomposition | https://arxiv.org/html/2606.29645v1 — §3.2 Experimental Design; results across six benchmarks | https://arxiv.org/html/2606.29645v1 — §6.1 Limitations | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29645 | complete |
| SF-2026-ARXIV-2606-29646 | RP-8e9a570761890c3e | deep | arXiv:2606.29646v1 | SRC-ARXIV@arXiv:2606.29646v1 | https://arxiv.org/html/2606.29646v1 — §2 Methodology; weight/residual fuzzing and proxy selection | https://arxiv.org/html/2606.29646v1 — §3 Results | https://arxiv.org/html/2606.29646v1 — §4 Discussion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29646 | complete |
| SF-2026-ARXIV-2606-29648 | RP-d6eca3212b85931c | deep | arXiv:2606.29648v1 | SRC-ARXIV@arXiv:2606.29648v1 | https://arxiv.org/html/2606.29648v1 — §Failure-driven retriever evolution and meta-agent rewrite loop | https://arxiv.org/html/2606.29648v1 — §4 Experiments | https://arxiv.org/html/2606.29648v1 — §A Limitations | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29648 | complete |
| SF-2026-ARXIV-2606-29649 | RP-869b44ae5adf7ed9 | deep | arXiv:2606.29649v1 | SRC-ARXIV@arXiv:2606.29649v1 | https://arxiv.org/html/2606.29649v1 — §3 Methodology; resolution/construction/language attack grid | https://arxiv.org/html/2606.29649v1 — §3.2 VLM Evaluation | https://arxiv.org/html/2606.29649v1 — §5 Discussion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29649 | complete |
| SF-2026-ARXIV-2606-29652 | RP-e043c6ba71f87521 | deep | arXiv:2606.29652v1 | SRC-ARXIV@arXiv:2606.29652v1 | https://arxiv.org/html/2606.29652v1 — §Local-first IR architecture and on-device index/inference design | https://arxiv.org/html/2606.29652v1 — §4.1 Experimental Setup; five benchmarks and 1K-1M documents | https://arxiv.org/html/2606.29652v1 — §4.11 Limitations | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29652 | complete |
| SF-2026-ARXIV-2606-29654 | RP-ec2db999a138526f | deep | arXiv:2606.29654v1 | SRC-ARXIV@arXiv:2606.29654v1 | https://arxiv.org/html/2606.29654v1 — §3 Method; Offline: calibration; Online: k-NN lookup; Stopping rule | https://arxiv.org/html/2606.29654v1 — §6 Experiments; Benchmarks; Difficulty-normalized deployment budgets; 6.1 Main results | https://arxiv.org/html/2606.29654v1 — §7 Discussion and Limitations; H Detailed Assumption Diagnostics; N Failure-case decomposition | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29654 | complete |
| SF-2026-ARXIV-2606-29657 | RP-ac89750a96b9e5d8 | deep | arXiv:2606.29657v1 | SRC-ARXIV@arXiv:2606.29657v1 | https://arxiv.org/html/2606.29657v1 — §Posterior-seeking Predictor, epistemic contextualization and guarded scaffolding | https://arxiv.org/html/2606.29657v1 — §Formal safety argument and falsifiability analysis | https://arxiv.org/html/2606.29657v1 — §5.4.2 Falsifiability, Scope, and Requirements for a Concrete Design | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29657 | complete |
| SF-2026-ARXIV-2606-29661 | RP-d9e00f98554b2742 | deep | arXiv:2606.29661v1 | SRC-ARXIV@arXiv:2606.29661v1 | https://arxiv.org/html/2606.29661v1 — §4 Methods; quality-diversity ensemble construction | https://arxiv.org/html/2606.29661v1 — §5 Results | https://arxiv.org/html/2606.29661v1 — §6 Discussion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29661 | complete |
| SF-2026-ARXIV-2606-29679 | RP-afbb2a64cdcc9f43 | deep | arXiv:2606.29679v1 | SRC-ARXIV@arXiv:2606.29679v1 | https://arxiv.org/html/2606.29679v1 — §3.6 Applying I-BBS Algorithm 1 to M(t): dimension inference and operative regimes | https://arxiv.org/html/2606.29679v1 — §4 Experiments | https://arxiv.org/html/2606.29679v1 — §6 Discussion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29679 | complete |
| SF-2026-ARXIV-2606-30686 | RP-c655f884e7729c50 | deep | arXiv:2606.30686v1 | SRC-ARXIV@arXiv:2606.30686v1 | https://arxiv.org/html/2606.30686v1 — §2 Decomposing VLA Policies; 4 Systemic Consequences | https://arxiv.org/html/2606.30686v1 — §3.2 Three Levels of Non-Identifiability in Current Evaluation | https://arxiv.org/html/2606.30686v1 — §Conclusion and proposed controlled-variation scope | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-30686 | complete |
| SF-2026-ARXIV-2606-30689 | RP-61936b0d3dba74db | deep | arXiv:2606.30689v1 | SRC-ARXIV@arXiv:2606.30689v1 | https://arxiv.org/html/2606.30689v1 — §Citation-enforced SDD design; 4.4 Hallucination Injection Protocol | https://arxiv.org/html/2606.30689v1 — §4 Experimental Design; cross-model results | https://arxiv.org/html/2606.30689v1 — §7 Discussion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-30689 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2606-29142:start -->
### 2606.29142 — Agent Security Meets Regulatory Reality -- A Practitioner Systematization of Autonomous-Agent Threats and Controls in Regulated Financial Systems

**问题与现有正文缺口。** Large language model agents are entering regulated financial systems, yet the security literature characterizing their attack surface is almost entirely laboratory-based, and the practitioner guidance on regulated deployment is neither peer-reviewed nor connected to a formal threat model. 逐段重读 owner 与相邻章后确认：当前章已把模型 sensor、policy/authorization 与 effect-time commit 分开，并拥有 fail-closed fallback。

**机制、状态、控制流与取舍。** 把受监管金融 Agent 的模型、工具、审计证据与人工授权绑定为部署控制面。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 把受监管金融 Agent 的模型、工具、审计证据与人工授权绑定为部署控制面。《Agent Security Meets Regulatory Reality -- A Practitioner Systematization of Autonomous-Agent Threats and Controls in Regulated Financial Systems》的正证据锚定 `IV Architectural Patterns Observed in Production; V Negative Results and Open Problems`；`V Negative Results and Open Problems; VI Generalization Beyond Finance` 没有建立跨 threat distribution、attacker adaptation 与 effect-time authorization 的防护承诺。因此该证据只能修正当前判断，超界时 `PLATFORM-SECURITY` 必须拒绝 effect commit 并转 sandbox/人工。

<!-- claim:SF-2026-ARXIV-2606-29142:start -->
Claim boundary：仅 `arXiv:2606.29142v1`；未证明边界定位 `https://arxiv.org/pdf/2606.29142v1 — §V Negative Results and Open Problems; VI Generalization Beyond Finance`。
<!-- claim:SF-2026-ARXIV-2606-29142:end -->
<!-- review:SF-2026-ARXIV-2606-29142:end -->

<!-- review:SF-2026-ARXIV-2606-29150:start -->
### 2606.29150 — Flow Reasoning Models: Scaling Reasoning Through Iterative Self-Refinement

**问题与现有正文缺口。** Discrete flow models have recently shown promising performance on few-step text generation; however, when naively applied to structured reasoning tasks such as Sudoku and Zebra puzzles, they converge confidently to incorrect answers (solving only $\sim$36% of Sudoku puzzles). 逐段重读 owner 与相邻章后确认：当前章已拥有 request-local decode/refinement state、停止条件与受验证执行路径。

**机制、状态、控制流与取舍。** 把 flow reasoning 的中间状态、自验证与 test-time compute 变成推理时控制路径。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 把 flow reasoning 的中间状态、自验证与 test-time compute 变成推理时控制路径。《Flow Reasoning Models: Scaling Reasoning Through Iterative Self-Refinement》的正证据锚定 `4 Experiments; G Experimental setup and hyperparameters`；`6 Discussion; B Test-time scaling: coverage, selection, and sampling-step baselines` 没有建立跨 model、request shape、quality target 与 serving engine 的延迟-质量合同。因此该证据只能修正当前判断，超界时 `INFER-DECODE` 必须恢复已验证的普通 decode/refinement path。

<!-- claim:SF-2026-ARXIV-2606-29150:start -->
Claim boundary：仅 `arXiv:2606.29150v1`；未证明边界定位 `https://arxiv.org/html/2606.29150v1 — §6 Discussion; B Test-time scaling: coverage, selection, and sampling-step baselines`。
<!-- claim:SF-2026-ARXIV-2606-29150:end -->
<!-- review:SF-2026-ARXIV-2606-29150:end -->

<!-- review:SF-2026-ARXIV-2606-29151:start -->
### 2606.29151 — CADENZA: Compiling Natural-Language Intent into Task-Specific Operator DAGs for Semantic Query Processing

**问题与现有正文缺口。** Semantic query processing engines (SQPEs) extend relational query processing with semantic operators that are executed via model inference over unstructured data. 逐段重读 owner 与相邻章后确认：现有 RAG 正文有 typed query plan 与固定/校准检索回退，但没有把自然语言 semantic operator 编译为可重写 logical DAG、再由 physical planner 联合提交 backend/router/threshold 的计划对象。

**机制、状态、控制流与取舍。** 旧 RAG 路径把自然语言直接送入固定 retriever；CADENZA 先编译 task-specific operator DAG，再由 logical rewrite 与 physical planner 按 quality/latency/cost 选择 backend。RAG owner 持有 DAG、operator identity 与 plan commit；统计或 backend profile 漂移时回退固定检索计划。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 只证明 SemBench 上 intent-specific operator DAG 与异构 backend 的 quality/latency/cost 计划选择；未证明跨 operator 的联合最优、teacher-noise 之外的 label shift，或 Azure/API 与本地模型间可移植性。失配时固定到已校准 retrieval plan。

<!-- claim:SF-2026-ARXIV-2606-29151:start -->
Claim boundary：仅 `arXiv:2606.29151v1`；未证明边界定位 `https://arxiv.org/html/2606.29151v1 — §6.3 Robustness; G Validation Set Noise`。
<!-- claim:SF-2026-ARXIV-2606-29151:end -->
<!-- review:SF-2026-ARXIV-2606-29151:end -->

<!-- review:SF-2026-ARXIV-2606-29158:start -->
### 2606.29158 — On the Nonlinearity of Learning Rate Scaling for LLM Training

**问题与现有正文缺口。** Learning-rate transfer can reduce the cost of training large language models: instead of sweeping learning rates at target scale, practitioners extrapolate from smaller runs. 逐段重读 owner 与相邻章后确认：现有 Pretraining 正文分离 optimizer、schedule、batch/tokens 与 scaling identity，但没有记录普通 LR 对 model/data scale 的非线性以及 effective LR 与 D-axis 外推的不同可靠域。

**机制、状态、控制流与取舍。** 固定比例或单变量外推学习率会把 width、depth、token budget 与 schedule 的非线性交互折叠掉；训练控制面应把这些轴和 optimizer/schedule revision 一起冻结后再外推。额外 sweep 提高成本，超出已测尺度时回退邻近规模校准而非沿幂律盲推。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 只覆盖 GPT-2-style 22M-707M、FineWeb 5B-100B tokens、WSD 与 AdamW/AdamH；论文明确显示 log-linear LR 仅局部成立，不能外推到其他架构、optimizer 或更大规模。超界时重新 sweep 邻近尺度。

<!-- claim:SF-2026-ARXIV-2606-29158:start -->
Claim boundary：仅 `arXiv:2606.29158v1`；未证明边界定位 `https://arxiv.org/html/2606.29158v1 — §7 Conclusions and Limitations`。
<!-- claim:SF-2026-ARXIV-2606-29158:end -->
<!-- review:SF-2026-ARXIV-2606-29158:end -->

<!-- review:SF-2026-ARXIV-2606-29159:start -->
### 2606.29159 — Pooled Leaderboards Hide System-Specific Winners: A Reporting-Protocol Audit of Offline Root-Cause Analysis Benchmarks

**问题与现有正文缺口。** Offline root-cause-analysis (RCA) benchmarks commonly rank methods by a single pooled top-1 accuracy across multiple subsystems, and engineers often read the pooled winner as a recommendation for their own subsystem. 逐段重读 owner 与相邻章后确认：当前章已把 dataset/model/evaluator/metric/release 分权，并要求 slice、校准、污染与反例证据。

**机制、状态、控制流与取舍。** 揭示 pooled leaderboard 会掩盖 RCA 子任务差异，改变评测聚合合同。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 揭示 pooled leaderboard 会掩盖 RCA 子任务差异，改变评测聚合合同。《Pooled Leaderboards Hide System-Specific Winners: A Reporting-Protocol Audit of Offline Root-Cause Analysis Benchmarks》的正证据锚定 `Benchmark validity and leaderboard instability in ML; system-specific results`；`6 Discussion, Limitations, and Recommendations` 没有建立跨 dataset/model/evaluator revision 的 release acceptance 或生产 SLO。因此该证据只能修正当前判断，超界时 `PLATFORM-EVALUATION-SYSTEM` 必须保持 release Gate Open 并恢复完整分层评测。

<!-- claim:SF-2026-ARXIV-2606-29159:start -->
Claim boundary：仅 `arXiv:2606.29159v1`；未证明边界定位 `https://arxiv.org/html/2606.29159v1 — §6 Discussion, Limitations, and Recommendations`。
<!-- claim:SF-2026-ARXIV-2606-29159:end -->
<!-- review:SF-2026-ARXIV-2606-29159:end -->

<!-- review:SF-2026-ARXIV-2606-29171:start -->
### 2606.29171 — Symbolic Mechanistic Data Attribution: Tracing Training Influence to Learned Behavioral Policies

**问题与现有正文缺口。** While existing data attribution methods can identify which training examples build specific mechanistic circuits, they cannot explain how training data shapes the high-level behavioral decisions a model learns to make. 逐段重读 owner 与相邻章后确认：现有 Data 正文拥有 lineage、dedup、contamination 与删除证据，却缺少从训练 pair 经 SAE feature 归因到 learned behavioral policy 的中间可审计层。

**机制、状态、控制流与取舍。** 普通 sample lineage 只能回答数据来自哪里；symbolic mechanistic attribution 进一步把样本影响连接到可解释 behavioral policy，使数据 owner 能把选择、删除或复核请求落到行为证据链。归因仍是模型化证据，符号解释不稳定时保留原数据并回退重训/对照实验。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 只在 Llama-3.2-3B-Instruct refusal proxy、特定 SAE 与 200 个 SFT pair 上验证一阶符号归因；feature label、Ridge fidelity 与 first-order approximation 不等于真实删除/重训因果。保留原样本与重训对照。

<!-- claim:SF-2026-ARXIV-2606-29171:start -->
Claim boundary：仅 `arXiv:2606.29171v1`；未证明边界定位 `https://arxiv.org/html/2606.29171v1 — §6 Discussion; Symbolic model fidelity and scope; First-order approximation`。
<!-- claim:SF-2026-ARXIV-2606-29171:end -->
<!-- review:SF-2026-ARXIV-2606-29171:end -->

<!-- review:SF-2026-ARXIV-2606-29176:start -->
### 2606.29176 — Dead-Direction Conditioners: Gauge-Equivariant Preconditioning for Deep Networks

**问题与现有正文缺口。** A deep network's loss is invariant to continuous symmetries of its parameters: the logit shift, the ReLU rescaling, the LayerNorm scale, the per-head attention rotation. 逐段重读 owner 与相邻章后确认：当前章已把 optimizer、schedule、batch/tokens 与 scaling identity 分开；新证据只有改变外推或控制合同才可追加。

**机制、状态、控制流与取舍。** 改变优化器更新的去偏与稳定性路径，并要求按训练阶段校准。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 改变优化器更新的去偏与稳定性路径，并要求按训练阶段校准。《Dead-Direction Conditioners: Gauge-Equivariant Preconditioning for Deep Networks》的正证据锚定 `5 Experiments; 5.1 Reading the rate at language-model scale`；`5.10 Scope and limitations` 没有建立跨 architecture、optimizer、token budget 与更大训练尺度的可迁移性。因此该证据只能修正当前判断，超界时 `TRAIN-PRETRAINING` 必须恢复邻近规模 sweep 与已验证 schedule。

<!-- claim:SF-2026-ARXIV-2606-29176:start -->
Claim boundary：仅 `arXiv:2606.29176v1`；未证明边界定位 `https://arxiv.org/html/2606.29176v1 — §5.10 Scope and limitations`。
<!-- claim:SF-2026-ARXIV-2606-29176:end -->
<!-- review:SF-2026-ARXIV-2606-29176:end -->

<!-- review:SF-2026-ARXIV-2606-29178:start -->
### 2606.29178 — Selective Memory Retention for Long-Horizon LLM Agents

**问题与现有正文缺口。** When does retention matter for memory-augmented LLM agents? 逐段重读 owner 与相邻章后确认：当前章已拥有 admission/retention/forgetting、provenance、transaction 与 raw evidence fallback。

**机制、状态、控制流与取舍。** 把长期记忆的写入、保留与遗忘门控变成显式持久状态迁移。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 把长期记忆的写入、保留与遗忘门控变成显式持久状态迁移。《Selective Memory Retention for Long-Horizon LLM Agents》的正证据锚定 `4 Experiments`；`6 Discussion and Limitations` 没有建立跨 workload、write policy、retention horizon 与 provenance shift 的记忆收益。因此该证据只能修正当前判断，超界时 `AGENT-MEMORY` 必须拒绝写入并保留旧 memory revision。

<!-- claim:SF-2026-ARXIV-2606-29178:start -->
Claim boundary：仅 `arXiv:2606.29178v1`；未证明边界定位 `https://arxiv.org/html/2606.29178v1 — §6 Discussion and Limitations`。
<!-- claim:SF-2026-ARXIV-2606-29178:end -->
<!-- review:SF-2026-ARXIV-2606-29178:end -->

<!-- review:SF-2026-ARXIV-2606-29182:start -->
### 2606.29182 — Evidence-Informed LLM Beliefs for Continual Scientific Discovery

**问题与现有正文缺口。** Open-ended scientific discovery with large language models (LLMs) increasingly operates as a long-horizon loop of hypothesis search and verification, where a reward signal guides which hypotheses to test next. 逐段重读 owner 与相邻章后确认：当前章已拥有 versioned state machine、DAG、evaluator-driven search、replay 与 compensation。

**机制、状态、控制流与取舍。** 让科学发现 Agent 的信念状态、实验动作与反证更新形成可追踪闭环。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 让科学发现 Agent 的信念状态、实验动作与反证更新形成可追踪闭环。《Evidence-Informed LLM Beliefs for Continual Scientific Discovery》的正证据锚定 `3.1.2 Evaluation: Reducing Surprisal Under Non-Stationary Beliefs`；`6 Limitations` 没有建立跨 environment、tool semantics、checkpoint 与 compensation path 的可复算性。因此该证据只能修正当前判断，超界时 `AGENT-WORKFLOW` 必须停在可恢复 checkpoint 并执行 compensation。

<!-- claim:SF-2026-ARXIV-2606-29182:start -->
Claim boundary：仅 `arXiv:2606.29182v1`；未证明边界定位 `https://arxiv.org/html/2606.29182v1 — §6 Limitations`。
<!-- claim:SF-2026-ARXIV-2606-29182:end -->
<!-- review:SF-2026-ARXIV-2606-29182:end -->

<!-- review:SF-2026-ARXIV-2606-29184:start -->
### 2606.29184 — BaRA: Bayesian Adaptive Rank Allocation for Parameter-Efficient Fine-Tuning

**问题与现有正文缺口。** While Low-rank adaptation (LoRA) enables highly efficient fine-tuning by constraining task-specific updates to fixed low-rank subspaces, this rigid design limits representational flexibility and often results in overconfident predictions and miscalibrated uncertainty, especially in low-data regimes. 逐段重读 owner 与相邻章后确认：当前章已把 rank、target modules、adapter identity 与 merge/serve 边界版本化。

**机制、状态、控制流与取舍。** 把适配器秩分配与层级预算绑定为可动态选择的训练状态。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 把适配器秩分配与层级预算绑定为可动态选择的训练状态。《BaRA: Bayesian Adaptive Rank Allocation for Parameter-Efficient Fine-Tuning》的正证据锚定 `VI Experiments`；`III-C Limitations of Bayesian LoRA Methods` 没有建立跨 backbone、target module、rank budget 与 merge/serve path 的稳定性。因此该证据只能修正当前判断，超界时 `TRAIN-LORA` 必须恢复固定 rank/target-module adapter。

<!-- claim:SF-2026-ARXIV-2606-29184:start -->
Claim boundary：仅 `arXiv:2606.29184v1`；未证明边界定位 `https://arxiv.org/html/2606.29184v1 — §III-C Limitations of Bayesian LoRA Methods`。
<!-- claim:SF-2026-ARXIV-2606-29184:end -->
<!-- review:SF-2026-ARXIV-2606-29184:end -->

<!-- review:SF-2026-ARXIV-2606-29193:start -->
### 2606.29193 — A Multi-Dataset Benchmark for Evaluating LLM Agents in Microservice Failure Diagnosis

**问题与现有正文缺口。** LLM-based agents are reshaping microservice operations into AgentOps, where benchmarks are key to evaluating failure diagnosis over multimodal observability data. 逐段重读 owner 与相邻章后确认：当前章已把 dataset/model/evaluator/metric/release 分权，并要求 slice、校准、污染与反例证据。

**机制、状态、控制流与取舍。** 把微服务 Agent 的任务、环境、副作用和故障恢复纳入发布评测。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 把微服务 Agent 的任务、环境、副作用和故障恢复纳入发布评测。《A Multi-Dataset Benchmark for Evaluating LLM Agents in Microservice Failure Diagnosis》的正证据锚定 `4 Evaluation; 4.4 Evaluation Metric`；`6 Discussion` 没有建立跨 dataset/model/evaluator revision 的 release acceptance 或生产 SLO。因此该证据只能修正当前判断，超界时 `PLATFORM-EVALUATION-SYSTEM` 必须保持 release Gate Open 并恢复完整分层评测。

<!-- claim:SF-2026-ARXIV-2606-29193:start -->
Claim boundary：仅 `arXiv:2606.29193v1`；未证明边界定位 `https://arxiv.org/html/2606.29193v1 — §6 Discussion`。
<!-- claim:SF-2026-ARXIV-2606-29193:end -->
<!-- review:SF-2026-ARXIV-2606-29193:end -->

<!-- review:SF-2026-ARXIV-2606-29194:start -->
### 2606.29194 — AI Trading's Alpha Singularity: Emergent Market Reasoning through Agent-to-Agent Self-Evolution

**问题与现有正文缺口。** Automated alpha mining holds the scoring function fixed and varies the search algorithm over it. 逐段重读 owner 与相邻章后确认：当前章已拥有 topology、message/state、aggregation、delegation、independent verification 与 coordination tax。

**机制、状态、控制流与取舍。** 把多 Agent 搜索的共享状态、隔离边界与合并控制显式化。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 把多 Agent 搜索的共享状态、隔离边界与合并控制显式化。《AI Trading's Alpha Singularity: Emergent Market Reasoning through Agent-to-Agent Self-Evolution》的正证据锚定 `Statistical inference and out-of-sample evaluation`；`6 Discussion` 没有建立跨 agent population、message protocol、error correlation 与 coordination load 的聚合收益。因此该证据只能修正当前判断，超界时 `AGENT-MULTI-AGENT` 必须恢复单 Agent/串行协调与人工仲裁。

<!-- claim:SF-2026-ARXIV-2606-29194:start -->
Claim boundary：仅 `arXiv:2606.29194v1`；未证明边界定位 `https://arxiv.org/html/2606.29194v1 — §6 Discussion`。
<!-- claim:SF-2026-ARXIV-2606-29194:end -->
<!-- review:SF-2026-ARXIV-2606-29194:end -->

<!-- review:SF-2026-ARXIV-2606-29196:start -->
### 2606.29196 — Representational Depth of Evaluation Awareness Shifts With Scale in Open-Weight Language Models

**问题与现有正文缺口。** Do language models know when they are being tested? 逐段重读 owner 与相邻章后确认：现有 Evaluation 正文管理 dataset/model/evaluator/metric/release 分权，却未把模型识别 evaluation context 的内部 signal 作为 benchmark 污染诊断，并限制其只能触发额外评测。

**机制、状态、控制流与取舍。** 能力评测不能假设模型对 evaluation context 无感；evaluation-awareness probe 必须作为 contamination sensor，按模型尺度和表示深度版本化，并在异常时阻止 pooled score 直接取得 release authority。Probe 迁移失败时回退 blind/held-out protocol 与外部 outcome。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** SAD 上的线性可恢复性只是一种 operational evaluation-awareness signal；white-box AUROC 与黑盒行为会分离，且 Qwen/Gemma 的深度迁移不构成跨 family scaling law。异常只触发额外 held-out evaluation，不授予直接拒绝权。

<!-- claim:SF-2026-ARXIV-2606-29196:start -->
Claim boundary：仅 `arXiv:2606.29196v1`；未证明边界定位 `https://arxiv.org/html/2606.29196v1 — §5 Discussion`。
<!-- claim:SF-2026-ARXIV-2606-29196:end -->
<!-- review:SF-2026-ARXIV-2606-29196:end -->

<!-- review:SF-2026-ARXIV-2606-29207:start -->
### 2606.29207 — KernelFlume: Elastic Core-Attention Scaling for Agentic Long-Context Decoding

**问题与现有正文缺口。** LLM serving is increasingly dominated by long and dynamic decode workloads from agents, reasoning models, and extended conversations. 逐段重读 owner 与相邻章后确认：当前章已拥有 request-local decode/refinement state、停止条件与受验证执行路径。

**机制、状态、控制流与取舍。** 把 kernel 生成、校验、选择与回退组成可执行的推理内核控制流。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 把 kernel 生成、校验、选择与回退组成可执行的推理内核控制流。《KernelFlume: Elastic Core-Attention Scaling for Agentic Long-Context Decoding》的正证据锚定 `6 Evaluation`；`2.4 Limitations of Existing Elastic Scaling` 没有建立跨 model、request shape、quality target 与 serving engine 的延迟-质量合同。因此该证据只能修正当前判断，超界时 `INFER-DECODE` 必须恢复已验证的普通 decode/refinement path。

<!-- claim:SF-2026-ARXIV-2606-29207:start -->
Claim boundary：仅 `arXiv:2606.29207v1`；未证明边界定位 `https://arxiv.org/html/2606.29207v1 — §2.4 Limitations of Existing Elastic Scaling`。
<!-- claim:SF-2026-ARXIV-2606-29207:end -->
<!-- review:SF-2026-ARXIV-2606-29207:end -->

<!-- review:SF-2026-ARXIV-2606-29215:start -->
### 2606.29215 — Multi-Block Diffusion Language Models

**问题与现有正文缺口。** Block Diffusion Language Models (BD-LMs) improve diffusion-based text generation with KV caching and flexible-length generation. 逐段重读 owner 与相邻章后确认：当前章已拥有 request-local decode/refinement state、停止条件与受验证执行路径。

**机制、状态、控制流与取舍。** 把 discrete diffusion 的多块并行解码、校验与质量退化边界显式化。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 把 discrete diffusion 的多块并行解码、校验与质量退化边界显式化。《Multi-Block Diffusion Language Models》的正证据锚定 `4 Experiments`；`5 Conclusion and stated speed-quality scope` 没有建立跨 model、request shape、quality target 与 serving engine 的延迟-质量合同。因此该证据只能修正当前判断，超界时 `INFER-DECODE` 必须恢复已验证的普通 decode/refinement path。

<!-- claim:SF-2026-ARXIV-2606-29215:start -->
Claim boundary：仅 `arXiv:2606.29215v1`；未证明边界定位 `https://arxiv.org/html/2606.29215v1 — §5 Conclusion and stated speed-quality scope`。
<!-- claim:SF-2026-ARXIV-2606-29215:end -->
<!-- review:SF-2026-ARXIV-2606-29215:end -->

<!-- review:SF-2026-ARXIV-2606-29222:start -->
### 2606.29222 — CORE Planner: Contextual-memory Oriented Reinforcement-learning in Unknown Environments for Robot Navigation

**问题与现有正文缺口。** Autonomous navigation in unknown environments requires a robot to efficiently reach a predefined goal while exploring without prior maps. 逐段重读 owner 与相邻章后确认：当前章已把 observation/action identity、latency、closed-loop outcome 与保守接管绑定。

**机制、状态、控制流与取舍。** 把机器人情境记忆接入感知到动作的闭环状态。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 把机器人情境记忆接入感知到动作的闭环状态。《CORE Planner: Contextual-memory Oriented Reinforcement-learning in Unknown Environments for Robot Navigation》的正证据锚定 `V Experiments`；`VI Conclusion and deployment scope` 没有建立跨 embodiment、sensor、latency 与闭环干预的动作成功率。因此该证据只能修正当前判断，超界时 `MULTIMODAL-EMBODIED-VLA` 必须拒绝物理提交并交回保守 controller。

<!-- claim:SF-2026-ARXIV-2606-29222:start -->
Claim boundary：仅 `arXiv:2606.29222v1`；未证明边界定位 `https://arxiv.org/html/2606.29222v1 — §VI Conclusion and deployment scope`。
<!-- claim:SF-2026-ARXIV-2606-29222:end -->
<!-- review:SF-2026-ARXIV-2606-29222:end -->

<!-- review:SF-2026-ARXIV-2606-29223:start -->
### 2606.29223 — Depth Exploration for LLM Decoding

**问题与现有正文缺口。** Autoregressive LLM decoding evaluates every generated token through the full layer stack, even though many tokens become predictable at intermediate depths. 逐段重读 owner 与相邻章后确认：当前章已拥有 request-local decode/refinement state、停止条件与受验证执行路径。

**机制、状态、控制流与取舍。** 把推理深度按样本难度分配，并保留固定深度回退。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 把推理深度按样本难度分配，并保留固定深度回退。《Depth Exploration for LLM Decoding》的正证据锚定 `4 Experiment`；`E Limitations and discussion` 没有建立跨 model、request shape、quality target 与 serving engine 的延迟-质量合同。因此该证据只能修正当前判断，超界时 `INFER-DECODE` 必须恢复已验证的普通 decode/refinement path。

<!-- claim:SF-2026-ARXIV-2606-29223:start -->
Claim boundary：仅 `arXiv:2606.29223v1`；未证明边界定位 `https://arxiv.org/html/2606.29223v1 — §E Limitations and discussion`。
<!-- claim:SF-2026-ARXIV-2606-29223:end -->
<!-- review:SF-2026-ARXIV-2606-29223:end -->

<!-- review:SF-2026-ARXIV-2606-29225:start -->
### 2606.29225 — PolicyGuard: A Dialogue-Grounded Sub-Agent Verifier for Policy Adherence in LLM Agents

**问题与现有正文缺口。** LLM agents handle user requests on behalf of organizations through tool calls and must follow the company policies stated in their system prompts. 逐段重读 owner 与相邻章后确认：当前章已把模型 sensor、policy/authorization 与 effect-time commit 分开，并拥有 fail-closed fallback。

**机制、状态、控制流与取舍。** 把 Agent policy 判定置于工具副作用提交前并定义 fail-closed 路径。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 把 Agent policy 判定置于工具副作用提交前并定义 fail-closed 路径。《PolicyGuard: A Dialogue-Grounded Sub-Agent Verifier for Policy Adherence in LLM Agents》的正证据锚定 `4 Experiments`；`Discussion` 没有建立跨 threat distribution、attacker adaptation 与 effect-time authorization 的防护承诺。因此该证据只能修正当前判断，超界时 `PLATFORM-SECURITY` 必须拒绝 effect commit 并转 sandbox/人工。

<!-- claim:SF-2026-ARXIV-2606-29225:start -->
Claim boundary：仅 `arXiv:2606.29225v1`；未证明边界定位 `https://arxiv.org/html/2606.29225v1 — §Discussion`。
<!-- claim:SF-2026-ARXIV-2606-29225:end -->
<!-- review:SF-2026-ARXIV-2606-29225:end -->

<!-- review:SF-2026-ARXIV-2606-29228:start -->
### 2606.29228 — Understanding Evaluation Illusion in Diffusion Large Language Models

**问题与现有正文缺口。** Despite the capability of parallel decoding, diffusion large language models (dLLMs) require many denoising steps to maintain generation quality, motivating recent research on efficient decoding strategies. 逐段重读 owner 与相邻章后确认：当前章已把 dataset/model/evaluator/metric/release 分权，并要求 slice、校准、污染与反例证据。

**机制、状态、控制流与取舍。** 揭示 DLM 评测中的表面提升与实际生成能力分离。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 揭示 DLM 评测中的表面提升与实际生成能力分离。《Understanding Evaluation Illusion in Diffusion Large Language Models》的正证据锚定 `3 Evaluation Inconsistency; 4 Experiments`；`5 Discussion; speed-quality trade-off counterevidence` 没有建立跨 dataset/model/evaluator revision 的 release acceptance 或生产 SLO。因此该证据只能修正当前判断，超界时 `PLATFORM-EVALUATION-SYSTEM` 必须保持 release Gate Open 并恢复完整分层评测。

<!-- claim:SF-2026-ARXIV-2606-29228:start -->
Claim boundary：仅 `arXiv:2606.29228v1`；未证明边界定位 `https://arxiv.org/html/2606.29228v1 — §5 Discussion; speed-quality trade-off counterevidence`。
<!-- claim:SF-2026-ARXIV-2606-29228:end -->
<!-- review:SF-2026-ARXIV-2606-29228:end -->

<!-- review:SF-2026-ARXIV-2606-29237:start -->
### 2606.29237 — MoPe: Motion Permanence for Robust Monocular Gaussian Mapping in Dynamic Environments

**问题与现有正文缺口。** Robust robot autonomy depends on scene representations that remain stable enough to support localization, navigation, and downstream decision making in dynamic environments. 逐段重读 owner 与相邻章后确认：当前章已区分 action-conditioned transition、persistent state、rollout 与 physical commit。

**机制、状态、控制流与取舍。** 把运动持续性作为世界模型 rollout 的可测状态而非单帧视觉指标。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 把运动持续性作为世界模型 rollout 的可测状态而非单帧视觉指标。《MoPe: Motion Permanence for Robust Monocular Gaussian Mapping in Dynamic Environments》的正证据锚定 `IV Experiments`；`V Limitations and Future Work` 没有建立跨 environment、observation dynamics 与 physical commit 的 rollout fidelity。因此该证据只能修正当前判断，超界时 `MULTIMODAL-WORLD-MODELS` 必须停止 imagined rollout 并请求真实 observation。

<!-- claim:SF-2026-ARXIV-2606-29237:start -->
Claim boundary：仅 `arXiv:2606.29237v1`；未证明边界定位 `https://arxiv.org/html/2606.29237v1 — §V Limitations and Future Work`。
<!-- claim:SF-2026-ARXIV-2606-29237:end -->
<!-- review:SF-2026-ARXIV-2606-29237:end -->

<!-- review:SF-2026-ARXIV-2606-29238:start -->
### 2606.29238 — On the Policy Gradient Foundations of Group Relative Policy Optimization: Credit Assignment, Gradient Sparsity, and Rank Collapse

**问题与现有正文缺口。** Group Relative Policy Optimization (GRPO) eliminates the learned critic in PPO by using the mean reward of grouped rollouts as a baseline. 逐段重读 owner 与相邻章后确认：当前章已把 terminal reward 拆为 typed trajectory credit，并记录 verifier、policy freshness 与 off-policy 边界。

**机制、状态、控制流与取舍。** 给 GRPO 更新的稳定域与偏差来源建立理论边界。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 给 GRPO 更新的稳定域与偏差来源建立理论边界。《On the Policy Gradient Foundations of Group Relative Policy Optimization: Credit Assignment, Gradient Sparsity, and Rank Collapse》的正证据锚定 `7 Experiments`；`6 Multi-Turn Limitation` 没有建立跨 reward/verifier、policy freshness 与分布漂移的 on-policy 有效性。因此该证据只能修正当前判断，超界时 `TRAIN-GRPO` 必须恢复 on-policy terminal/verifier baseline。

<!-- claim:SF-2026-ARXIV-2606-29238:start -->
Claim boundary：仅 `arXiv:2606.29238v1`；未证明边界定位 `https://arxiv.org/html/2606.29238v1 — §6 Multi-Turn Limitation`。
<!-- claim:SF-2026-ARXIV-2606-29238:end -->
<!-- review:SF-2026-ARXIV-2606-29238:end -->

<!-- review:SF-2026-ARXIV-2606-29239:start -->
### 2606.29239 — Breaking the Rounding Trap: Securing LLMs against Quantization-Conditioned Backdoors

**问题与现有正文缺口。** Model quantization is a key technique for reducing storage and inference costs when deploying large language models in practice. 逐段重读 owner 与相邻章后确认：当前章已把模型 sensor、policy/authorization 与 effect-time commit 分开，并拥有 fail-closed fallback。

**机制、状态、控制流与取舍。** 把量化后安全回归纳入部署校准与发布 gate。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 把量化后安全回归纳入部署校准与发布 gate。《Breaking the Rounding Trap: Securing LLMs against Quantization-Conditioned Backdoors》的正证据锚定 `3.2 Empirical Motivation: The Role of Rounding Errors in LLM Quantization`；`3.1 Threat Model` 没有建立跨 threat distribution、attacker adaptation 与 effect-time authorization 的防护承诺。因此该证据只能修正当前判断，超界时 `PLATFORM-SECURITY` 必须拒绝 effect commit 并转 sandbox/人工。

<!-- claim:SF-2026-ARXIV-2606-29239:start -->
Claim boundary：仅 `arXiv:2606.29239v1`；未证明边界定位 `https://arxiv.org/html/2606.29239v1 — §3.1 Threat Model`。
<!-- claim:SF-2026-ARXIV-2606-29239:end -->
<!-- review:SF-2026-ARXIV-2606-29239:end -->

<!-- review:SF-2026-ARXIV-2606-29251:start -->
### 2606.29251 — When Summaries Distort Decisions: Information Fidelity in LLM-Compressed Financial Analysis

**问题与现有正文缺口。** Financial decision-makers face more information than they can directly inspect, making context compression necessary. 逐段重读 owner 与相邻章后确认：当前章已把 raw evidence、derived view、compression fidelity 与可恢复 bookkeeping 分开。

**机制、状态、控制流与取舍。** 把上下文压缩的事实保真、推理可用性与预算绑定为控制合同。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 把上下文压缩的事实保真、推理可用性与预算绑定为控制合同。《When Summaries Distort Decisions: Information Fidelity in LLM-Compressed Financial Analysis》的正证据锚定 `4 Experiments`；`7 Limitations` 没有建立跨 task、compression policy 与 evidence loss 的决策保真。因此该证据只能修正当前判断，超界时 `AGENT-CONTEXT` 必须恢复 hash-addressed raw evidence。

<!-- claim:SF-2026-ARXIV-2606-29251:start -->
Claim boundary：仅 `arXiv:2606.29251v1`；未证明边界定位 `https://arxiv.org/html/2606.29251v1 — §7 Limitations`。
<!-- claim:SF-2026-ARXIV-2606-29251:end -->
<!-- review:SF-2026-ARXIV-2606-29251:end -->

<!-- review:SF-2026-ARXIV-2606-29270:start -->
### 2606.29270 — Minority Sentinel: When to Overturn Majority Voting in Multi-Agent LLM Debates

**问题与现有正文缺口。** Multi-Agent Debate (MAD) with Majority Voting is a dominant paradigm for improving LLM reasoning, yet its effectiveness rests on the Condorcet Jury Theorem's assumption of independent errors. 逐段重读 owner 与相邻章后确认：现有 Multi-Agent 正文有 aggregation 与 independent verification，但缺少在多数错误相关时保存 minority evidence、以预校准 Flip Precision 决定是否推翻 majority commit 的协议状态。

**机制、状态、控制流与取舍。** 多数投票不再自动提交；aggregation owner 保存 minority-sentinel evidence、override criterion 与最终 commit receipt，只在少数意见显示独立且校准的反证时推翻多数。相关错误或 sentinel 失准时回退独立 verifier/人工，而不是继续增加同源 Agent。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 只证明三异构 Agent、两轮、六 benchmark 的 debate-log classifier 能在已测阈值上安全翻转；共享训练导致的相关错误、换模型和换协议都可能破坏 81.2% Flip Precision。失配时不翻转并交给独立 verifier/人工。

<!-- claim:SF-2026-ARXIV-2606-29270:start -->
Claim boundary：仅 `arXiv:2606.29270v1`；未证明边界定位 `https://arxiv.org/html/2606.29270v1 — §6.2 Limitations`。
<!-- claim:SF-2026-ARXIV-2606-29270:end -->
<!-- review:SF-2026-ARXIV-2606-29270:end -->

<!-- review:SF-2026-ARXIV-2606-29275:start -->
### 2606.29275 — Adaptive Block Diffusion: Resolving Training-Inference Mismatch in Diffusion Language Models

**问题与现有正文缺口。** Diffusion Language Models (DLMs) are typically trained under fixed context structures, restricting denoising to predetermined token subsets. 逐段重读 owner 与相邻章后确认：当前章已拥有 request-local decode/refinement state、停止条件与受验证执行路径。

**机制、状态、控制流与取舍。** 按置信度动态分配离散扩散步数并定义失败回退。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 按置信度动态分配离散扩散步数并定义失败回退。《Adaptive Block Diffusion: Resolving Training-Inference Mismatch in Diffusion Language Models》的正证据锚定 `5 Experiments`；`4.4 Limitation of Block Diffusion` 没有建立跨 model、request shape、quality target 与 serving engine 的延迟-质量合同。因此该证据只能修正当前判断，超界时 `INFER-DECODE` 必须恢复已验证的普通 decode/refinement path。

<!-- claim:SF-2026-ARXIV-2606-29275:start -->
Claim boundary：仅 `arXiv:2606.29275v1`；未证明边界定位 `https://arxiv.org/html/2606.29275v1 — §4.4 Limitation of Block Diffusion`。
<!-- claim:SF-2026-ARXIV-2606-29275:end -->
<!-- review:SF-2026-ARXIV-2606-29275:end -->

<!-- review:SF-2026-ARXIV-2606-29278:start -->
### 2606.29278 — The Complexity Ceiling Benchmark: A Multi-Domain Evaluation of Sequential Reasoning Under Depth Scaling

**问题与现有正文缺口。** We introduce the Complexity Ceiling Benchmark (CCB), a controlled evaluation of how language-model reasoning decays as the number of required sequential steps grows. 逐段重读 owner 与相邻章后确认：当前章已把 dataset/model/evaluator/metric/release 分权，并要求 slice、校准、污染与反例证据。

**机制、状态、控制流与取舍。** 把推理复杂度上限与 benchmark 饱和分开，形成停止判断。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 把推理复杂度上限与 benchmark 饱和分开，形成停止判断。《The Complexity Ceiling Benchmark: A Multi-Domain Evaluation of Sequential Reasoning Under Depth Scaling》的正证据锚定 `Trace-level evaluation and structural uncertainty`；`5 Discussion` 没有建立跨 dataset/model/evaluator revision 的 release acceptance 或生产 SLO。因此该证据只能修正当前判断，超界时 `PLATFORM-EVALUATION-SYSTEM` 必须保持 release Gate Open 并恢复完整分层评测。

<!-- claim:SF-2026-ARXIV-2606-29278:start -->
Claim boundary：仅 `arXiv:2606.29278v1`；未证明边界定位 `https://arxiv.org/html/2606.29278v1 — §5 Discussion`。
<!-- claim:SF-2026-ARXIV-2606-29278:end -->
<!-- review:SF-2026-ARXIV-2606-29278:end -->

<!-- review:SF-2026-ARXIV-2606-29279:start -->
### 2606.29279 — Manufactured Confidence: How Memory Consolidation Turns Hearsay into Confident Facts

**问题与现有正文缺口。** LLM agents carry conclusions across steps and sessions in compressed memory, and memory products (e.g., mem0, LangMem) rewrite conversation into stored "facts" that later steps trust. 逐段重读 owner 与相邻章后确认：当前章已拥有 admission/retention/forgetting、provenance、transaction 与 raw evidence fallback。

**机制、状态、控制流与取舍。** 把记忆中的转述污染与一手证据 provenance 分开。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 把记忆中的转述污染与一手证据 provenance 分开。《Manufactured Confidence: How Memory Consolidation Turns Hearsay into Confident Facts》的正证据锚定 `3 Results`；`Conclusion and source-provenance scope` 没有建立跨 workload、write policy、retention horizon 与 provenance shift 的记忆收益。因此该证据只能修正当前判断，超界时 `AGENT-MEMORY` 必须拒绝写入并保留旧 memory revision。

<!-- claim:SF-2026-ARXIV-2606-29279:start -->
Claim boundary：仅 `arXiv:2606.29279v1`；未证明边界定位 `https://arxiv.org/html/2606.29279v1 — §Conclusion and source-provenance scope`。
<!-- claim:SF-2026-ARXIV-2606-29279:end -->
<!-- review:SF-2026-ARXIV-2606-29279:end -->

<!-- review:SF-2026-ARXIV-2606-29280:start -->
### 2606.29280 — Deterministic Decisions for High-Stakes AI. A Zero-Egress Pipeline with the Deployability of RAG and the Accuracy of Machine Learning

**问题与现有正文缺口。** We identify intervention bias as a previously unquantified failure mode of zero-shot large-language-model (LLM) educational advisory agents: without task-specific training, they recommend action when a hindsight-optimal oracle policy mandates inaction. 逐段重读 owner 与相邻章后确认：当前章已把 dataset/model/evaluator/metric/release 分权，并要求 slice、校准、污染与反例证据。

**机制、状态、控制流与取舍。** 把高风险 pipeline 的阶段性不确定性、升级与拒答纳入验收。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 把高风险 pipeline 的阶段性不确定性、升级与拒答纳入验收。《Deterministic Decisions for High-Stakes AI. A Zero-Egress Pipeline with the Deployability of RAG and the Accuracy of Machine Learning》的正证据锚定 `Evaluation methodology and outcome study`；`2.4 Machine Learning for Student Outcome Prediction: Benchmarks and Limits` 没有建立跨 dataset/model/evaluator revision 的 release acceptance 或生产 SLO。因此该证据只能修正当前判断，超界时 `PLATFORM-EVALUATION-SYSTEM` 必须保持 release Gate Open 并恢复完整分层评测。

<!-- claim:SF-2026-ARXIV-2606-29280:start -->
Claim boundary：仅 `arXiv:2606.29280v1`；未证明边界定位 `https://arxiv.org/html/2606.29280v1 — §2.4 Machine Learning for Student Outcome Prediction: Benchmarks and Limits`。
<!-- claim:SF-2026-ARXIV-2606-29280:end -->
<!-- review:SF-2026-ARXIV-2606-29280:end -->

<!-- review:SF-2026-ARXIV-2606-29282:start -->
### 2606.29282 — ScaleErasure: Inference-Time Minimal Intervention for Precise Concept Erasure in Next-Scale Autoregressive Image Generation

**问题与现有正文缺口。** Concept erasure aims to prevent image generative models from producing unsafe content while preserving their general generative capability. 逐段重读 owner 与相邻章后确认：当前章已把模型 sensor、policy/authorization 与 effect-time commit 分开，并拥有 fail-closed fallback。

**机制、状态、控制流与取舍。** 把概念擦除的残留行为与再激活纳入安全发布证据。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 把概念擦除的残留行为与再激活纳入安全发布证据。《ScaleErasure: Inference-Time Minimal Intervention for Precise Concept Erasure in Next-Scale Autoregressive Image Generation》的正证据锚定 `5 Experiments`；`B Discussion on MACE Adaptation` 没有建立跨 threat distribution、attacker adaptation 与 effect-time authorization 的防护承诺。因此该证据只能修正当前判断，超界时 `PLATFORM-SECURITY` 必须拒绝 effect commit 并转 sandbox/人工。

<!-- claim:SF-2026-ARXIV-2606-29282:start -->
Claim boundary：仅 `arXiv:2606.29282v1`；未证明边界定位 `https://arxiv.org/html/2606.29282v1 — §B Discussion on MACE Adaptation`。
<!-- claim:SF-2026-ARXIV-2606-29282:end -->
<!-- review:SF-2026-ARXIV-2606-29282:end -->

<!-- review:SF-2026-ARXIV-2606-29296:start -->
### 2606.29296 — Process Advantage Signal Shaping: A Paradigm-Agnostic Middleware for Process-Supervised RL in LLM Reasoners

**问题与现有正文缺口。** Group Relative Policy Optimization (GRPO) is a default recipe for process-supervised reinforcement learning of LLM reasoners, and dense process supervision -- via learned process reward models (PRMs) or on-policy-distillation KL signals -- is a common way to densify its otherwise weak outcome reward. 逐段重读 owner 与相邻章后确认：当前章已把 terminal reward 拆为 typed trajectory credit，并记录 verifier、policy freshness 与 off-policy 边界。

**机制、状态、控制流与取舍。** 把策略更新的通过条件与样本级失败信号结合，改变 reward gate。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 把策略更新的通过条件与样本级失败信号结合，改变 reward gate。《Process Advantage Signal Shaping: A Paradigm-Agnostic Middleware for Process-Supervised RL in LLM Reasoners》的正证据锚定 `Empirical scope; evaluation protocol`；`6 Discussion` 没有建立跨 reward/verifier、policy freshness 与分布漂移的 on-policy 有效性。因此该证据只能修正当前判断，超界时 `TRAIN-GRPO` 必须恢复 on-policy terminal/verifier baseline。

<!-- claim:SF-2026-ARXIV-2606-29296:start -->
Claim boundary：仅 `arXiv:2606.29296v1`；未证明边界定位 `https://arxiv.org/html/2606.29296v1 — §6 Discussion`。
<!-- claim:SF-2026-ARXIV-2606-29296:end -->
<!-- review:SF-2026-ARXIV-2606-29296:end -->

<!-- review:SF-2026-ARXIV-2606-29315:start -->
### 2606.29315 — Hierarchical Experimentalist Agents

**问题与现有正文缺口。** Large language models (LLMs) are increasingly used to take actions in the real world and support human decision-making, yet most agents rely on parametric knowledge, fixed post-training data, retrieval, or search. 逐段重读 owner 与相邻章后确认：当前章已拥有 versioned state machine、DAG、evaluator-driven search、replay 与 compensation。

**机制、状态、控制流与取舍。** 把实验设计、工具执行、观测与假设修订组织成可复算工作流。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 把实验设计、工具执行、观测与假设修订组织成可复算工作流。《Hierarchical Experimentalist Agents》的正证据锚定 `4 Experiments and Results on Interphyre`；`A.5 Design Principles; domain-agnostic inputs and simulator-only evidence boundary` 没有建立跨 environment、tool semantics、checkpoint 与 compensation path 的可复算性。因此该证据只能修正当前判断，超界时 `AGENT-WORKFLOW` 必须停在可恢复 checkpoint 并执行 compensation。

<!-- claim:SF-2026-ARXIV-2606-29315:start -->
Claim boundary：仅 `arXiv:2606.29315v1`；未证明边界定位 `https://arxiv.org/pdf/2606.29315v1 — §A.5 Design Principles; domain-agnostic inputs and simulator-only evidence boundary`。
<!-- claim:SF-2026-ARXIV-2606-29315:end -->
<!-- review:SF-2026-ARXIV-2606-29315:end -->

<!-- review:SF-2026-ARXIV-2606-29328:start -->
### 2606.29328 — Covering the Unseen: Information Demand Coverage Optimization for Retrieval-Augmented Generation

**问题与现有正文缺口。** Retrieval-augmented generation (RAG) typically treats context selection as ranking chunks against a single query embedding. 逐段重读 owner 与相邻章后确认：当前章已拥有 typed query plan、router、metric/index identity、evidence sufficiency 与失败回退。

**机制、状态、控制流与取舍。** 把 RAG context selection 从单点相关性排序改为多维 information-demand coverage，并持有 sub-query 权重、set coverage 与 context-budget 状态。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 只证明六个 open-domain QA benchmark 上，把 K=200 candidate 的 k-context selection 改成多维 demand coverage 可改善 EM；理论 non-coverability 仅约束 query-proximity-monotone scorer，不直接约束 cross-encoder。sub-query drift、OT surrogate 成本或 corpus shift 失控时回退已校准 top-k/MMR。

<!-- claim:SF-2026-ARXIV-2606-29328:start -->
Claim boundary：仅 `arXiv:2606.29328v1`；未证明边界定位 `https://arxiv.org/html/2606.29328v1 — §VI Conclusion; V-K Generalization Across Sub-query Generators`。
<!-- claim:SF-2026-ARXIV-2606-29328:end -->
<!-- review:SF-2026-ARXIV-2606-29328:end -->

<!-- review:SF-2026-ARXIV-2606-29337:start -->
### 2606.29337 — W4A4 Quantization for Inference on Wan2.2-I2V-A14B

**问题与现有正文缺口。** We summarize our submission to Sub-Challenge 1: W4A4 Quantization for Inference (HiF4 / MXFP4) of the ICME 2026 Low-Bit-width Large-Model Quantization Challenge. 逐段重读 owner 与相邻章后确认：当前章已要求 graph/kernel/precision/hardware 共同形成 execution plan，并由 validator 而非生成器提交。

**机制、状态、控制流与取舍。** 给 W4A4 量化的校准、kernel 与质量回退建立部署边界。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 给 W4A4 量化的校准、kernel 与质量回退建立部署边界。《W4A4 Quantization for Inference on Wan2.2-I2V-A14B》的正证据锚定 `IV Evaluation and Results`；`IV-B Discussion` 没有建立跨 kernel、hardware、precision 与 graph revision 的执行计划可移植性。因此该证据只能修正当前判断，超界时 `INFER-TENSORRT-LLM` 必须恢复已验收 kernel/precision plan。

<!-- claim:SF-2026-ARXIV-2606-29337:start -->
Claim boundary：仅 `arXiv:2606.29337v1`；未证明边界定位 `https://arxiv.org/html/2606.29337v1 — §IV-B Discussion`。
<!-- claim:SF-2026-ARXIV-2606-29337:end -->
<!-- review:SF-2026-ARXIV-2606-29337:end -->

<!-- review:SF-2026-ARXIV-2606-29340:start -->
### 2606.29340 — PHF: Privileged Hidden Flow for On-Policy Self-Distillation

**问题与现有正文缺口。** On-policy self-distillation (OPSD) trains a reasoning model on rollouts sampled from its own policy by matching a privileged teacher that also sees verified reference solutions. 逐段重读 owner 与相邻章后确认：当前章已把 terminal reward 拆为 typed trajectory credit，并记录 verifier、policy freshness 与 off-policy 边界。

**机制、状态、控制流与取舍。** 把 off-policy 样本选择与策略漂移控制纳入训练状态。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 把 off-policy 样本选择与策略漂移控制纳入训练状态。《PHF: Privileged Hidden Flow for On-Policy Self-Distillation》的正证据锚定 `Experiments`；`Discussion` 没有建立跨 reward/verifier、policy freshness 与分布漂移的 on-policy 有效性。因此该证据只能修正当前判断，超界时 `TRAIN-GRPO` 必须恢复 on-policy terminal/verifier baseline。

<!-- claim:SF-2026-ARXIV-2606-29340:start -->
Claim boundary：仅 `arXiv:2606.29340v1`；未证明边界定位 `https://arxiv.org/html/2606.29340v1 — §Discussion`。
<!-- claim:SF-2026-ARXIV-2606-29340:end -->
<!-- review:SF-2026-ARXIV-2606-29340:end -->

<!-- review:SF-2026-ARXIV-2606-29350:start -->
### 2606.29350 — Fast Enough to Act: Spatio-Temporal Visual Token Merging for Low-Latency Robotic VLMs and VLAs

**问题与现有正文缺口。** Vision-language models and vision-language action models endow the robot with unprecedented capabilities. 逐段重读 owner 与相邻章后确认：当前章已把 observation/action identity、latency、closed-loop outcome 与保守接管绑定。

**机制、状态、控制流与取舍。** 把 VLA 视觉 token 合并与动作成功、延迟和回退共同校准。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 把 VLA 视觉 token 合并与动作成功、延迟和回退共同校准。《Fast Enough to Act: Spatio-Temporal Visual Token Merging for Low-Latency Robotic VLMs and VLAs》的正证据锚定 `IV Experiments`；`V Conclusion and Discussion` 没有建立跨 embodiment、sensor、latency 与闭环干预的动作成功率。因此该证据只能修正当前判断，超界时 `MULTIMODAL-EMBODIED-VLA` 必须拒绝物理提交并交回保守 controller。

<!-- claim:SF-2026-ARXIV-2606-29350:start -->
Claim boundary：仅 `arXiv:2606.29350v1`；未证明边界定位 `https://arxiv.org/html/2606.29350v1 — §V Conclusion and Discussion`。
<!-- claim:SF-2026-ARXIV-2606-29350:end -->
<!-- review:SF-2026-ARXIV-2606-29350:end -->

<!-- review:SF-2026-ARXIV-2606-29354:start -->
### 2606.29354 — When LLMs Develop Languages: Symbolic Communication for Efficient Multi-Agent Reasoning

**问题与现有正文缺口。** Chain-of-Thought (CoT) improves large language models (LLMs) on difficult reasoning tasks, but it often incurs long natural-language rationales that are poorly aligned with efficient machine reasoning. 逐段重读 owner 与相邻章后确认：当前章已拥有 topology、message/state、aggregation、delegation、independent verification 与 coordination tax。

**机制、状态、控制流与取舍。** 把符号消息协议作为多 Agent 共享状态而非自由文本旁路。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 把符号消息协议作为多 Agent 共享状态而非自由文本旁路。《When LLMs Develop Languages: Symbolic Communication for Efficient Multi-Agent Reasoning》的正证据锚定 `4 Experiments`；`5 Conclusion and Limitations` 没有建立跨 agent population、message protocol、error correlation 与 coordination load 的聚合收益。因此该证据只能修正当前判断，超界时 `AGENT-MULTI-AGENT` 必须恢复单 Agent/串行协调与人工仲裁。

<!-- claim:SF-2026-ARXIV-2606-29354:start -->
Claim boundary：仅 `arXiv:2606.29354v1`；未证明边界定位 `https://arxiv.org/html/2606.29354v1 — §5 Conclusion and Limitations`。
<!-- claim:SF-2026-ARXIV-2606-29354:end -->
<!-- review:SF-2026-ARXIV-2606-29354:end -->

<!-- review:SF-2026-ARXIV-2606-29366:start -->
### 2606.29366 — Solver-Verified Formulation Generation and Selection for Multi-Warehouse Inventory Allocation Using Large Language Models

**问题与现有正文缺口。** Balance-oriented multi-warehouse inventory allocation is a recurring decision problem in large-scale e-commerce supply chains, in which a fixed replenishment quantity is distributed across warehouses to balance post-allocation inventory coverage while accounting for demand forecasts and heterogeneous allocation constraints. 逐段重读 owner 与相邻章后确认：当前章已拥有 versioned state machine、DAG、evaluator-driven search、replay 与 compensation。

**机制、状态、控制流与取舍。** 把 LLM 建议置于 solver 验证与可执行证据之后。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 把 LLM 建议置于 solver 验证与可执行证据之后。《Solver-Verified Formulation Generation and Selection for Multi-Warehouse Inventory Allocation Using Large Language Models》的正证据锚定 `6 Computational Evaluation`；`Conclusion and solver-coverage boundary` 没有建立跨 environment、tool semantics、checkpoint 与 compensation path 的可复算性。因此该证据只能修正当前判断，超界时 `AGENT-WORKFLOW` 必须停在可恢复 checkpoint 并执行 compensation。

<!-- claim:SF-2026-ARXIV-2606-29366:start -->
Claim boundary：仅 `arXiv:2606.29366v1`；未证明边界定位 `https://arxiv.org/html/2606.29366v1 — §Conclusion and solver-coverage boundary`。
<!-- claim:SF-2026-ARXIV-2606-29366:end -->
<!-- review:SF-2026-ARXIV-2606-29366:end -->

<!-- review:SF-2026-ARXIV-2606-29377:start -->
### 2606.29377 — Diagnosing and Repairing Factual Errors in RAG under Budget Constraints

**问题与现有正文缺口。** Retrieval-Augmented Generation (RAG) improves the factuality of large language models by grounding responses in external evidence, yet real-world deployments remain fragile. 逐段重读 owner 与相邻章后确认：当前章已拥有 typed query plan、router、metric/index identity、evidence sufficiency 与失败回退。

**机制、状态、控制流与取舍。** 把检索失败诊断、查询修复与证据重取变成循环控制。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 把检索失败诊断、查询修复与证据重取变成循环控制。《Diagnosing and Repairing Factual Errors in RAG under Budget Constraints》的正证据锚定 `3 Experiments`；`Conclusion and evaluated-query scope` 没有建立跨 corpus、query distribution、retriever/index revision 与生成器的检索收益。因此该证据只能修正当前判断，超界时 `AGENT-RAG` 必须恢复固定、已校准的 retrieval plan。

<!-- claim:SF-2026-ARXIV-2606-29377:start -->
Claim boundary：仅 `arXiv:2606.29377v1`；未证明边界定位 `https://arxiv.org/html/2606.29377v1 — §Conclusion and evaluated-query scope`。
<!-- claim:SF-2026-ARXIV-2606-29377:end -->
<!-- review:SF-2026-ARXIV-2606-29377:end -->

<!-- review:SF-2026-ARXIV-2606-29399:start -->
### 2606.29399 — LLM-Guided Planning for Multi-hop Reasoning over Multimodal Nuclear Regulatory Documents

**问题与现有正文缺口。** Reviewing nuclear regulatory documents requires multi-hop reasoning across tens of thousands of pages, where judgments depend on evidence assembled across multiple chapters. 逐段重读 owner 与相邻章后确认：当前章已拥有 typed query plan、router、metric/index identity、evidence sufficiency 与失败回退。

**机制、状态、控制流与取舍。** 把多模态文档索引、跨页证据与推理计划联结。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 把多模态文档索引、跨页证据与推理计划联结。《LLM-Guided Planning for Multi-hop Reasoning over Multimodal Nuclear Regulatory Documents》的正证据锚定 `Experiments and multimodal document evaluation`；`7 Limitations` 没有建立跨 corpus、query distribution、retriever/index revision 与生成器的检索收益。因此该证据只能修正当前判断，超界时 `AGENT-RAG` 必须恢复固定、已校准的 retrieval plan。

<!-- claim:SF-2026-ARXIV-2606-29399:start -->
Claim boundary：仅 `arXiv:2606.29399v1`；未证明边界定位 `https://arxiv.org/html/2606.29399v1 — §7 Limitations`。
<!-- claim:SF-2026-ARXIV-2606-29399:end -->
<!-- review:SF-2026-ARXIV-2606-29399:end -->

<!-- review:SF-2026-ARXIV-2606-29403:start -->
### 2606.29403 — Self-Organized Conformal Prediction: Reducing Regional Coverage Gaps with Unsupervised Group Discovery

**问题与现有正文缺口。** Conformal prediction guarantees marginal coverage, but pooled calibration averages over heterogeneous regions and can mask regional undercoverage in safety-critical subgroups. 逐段重读 owner 与相邻章后确认：当前章已把 dataset/model/evaluator/metric/release 分权，并要求 slice、校准、污染与反例证据。

**机制、状态、控制流与取舍。** 把 conformal coverage 与拒答/发布阈值绑定。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 把 conformal coverage 与拒答/发布阈值绑定。《Self-Organized Conformal Prediction: Reducing Regional Coverage Gaps with Unsupervised Group Discovery》的正证据锚定 `4 Experiments`；`Conclusion and exchangeability boundary` 没有建立跨 dataset/model/evaluator revision 的 release acceptance 或生产 SLO。因此该证据只能修正当前判断，超界时 `PLATFORM-EVALUATION-SYSTEM` 必须保持 release Gate Open 并恢复完整分层评测。

<!-- claim:SF-2026-ARXIV-2606-29403:start -->
Claim boundary：仅 `arXiv:2606.29403v1`；未证明边界定位 `https://arxiv.org/html/2606.29403v1 — §Conclusion and exchangeability boundary`。
<!-- claim:SF-2026-ARXIV-2606-29403:end -->
<!-- review:SF-2026-ARXIV-2606-29403:end -->

<!-- review:SF-2026-ARXIV-2606-29424:start -->
### 2606.29424 — EntroRouter: Learning Efficient Model Routing via Entropy Regulation

**问题与现有正文缺口。** Model routing balances solution accuracy and computational cost by selecting among models of varying capabilities. 逐段重读 owner 与相邻章后确认：当前章已把 routing、placement、energy/thermal、SLO 与 topology state 纳入调度控制。

**机制、状态、控制流与取舍。** 让 router 持有请求熵、专家选择与负载降级状态。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 让 router 持有请求熵、专家选择与负载降级状态。《EntroRouter: Learning Efficient Model Routing via Entropy Regulation》的正证据锚定 `4 Experiments`；`5 Discussion` 没有建立跨 topology、并发负载、thermal state 与 SLO 的调度收益。因此该证据只能修正当前判断，超界时 `INFER-SCHEDULING` 必须恢复静态 placement 与保守 SLO headroom。

<!-- claim:SF-2026-ARXIV-2606-29424:start -->
Claim boundary：仅 `arXiv:2606.29424v1`；未证明边界定位 `https://arxiv.org/html/2606.29424v1 — §5 Discussion`。
<!-- claim:SF-2026-ARXIV-2606-29424:end -->
<!-- review:SF-2026-ARXIV-2606-29424:end -->

<!-- review:SF-2026-ARXIV-2606-29425:start -->
### 2606.29425 — Mixture of Debaters: Learn to Debate at Architectural Level in Multi-Agent Reasoning

**问题与现有正文缺口。** Existing multi-agent debate frameworks suffer from two critical limitations: they rely on static architectures where agent roles and coordination patterns are fixed at design time, and they require instantiating multiple model copies, incurring substantial computational overhead. 逐段重读 owner 与相邻章后确认：当前章已拥有 topology、message/state、aggregation、delegation、independent verification 与 coordination tax。

**机制、状态、控制流与取舍。** 把辩论者选择与聚合权重变成可校准协调状态。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 把辩论者选择与聚合权重变成可校准协调状态。《Mixture of Debaters: Learn to Debate at Architectural Level in Multi-Agent Reasoning》的正证据锚定 `4 Experiments`；`Conclusion and tested-debater scope` 没有建立跨 agent population、message protocol、error correlation 与 coordination load 的聚合收益。因此该证据只能修正当前判断，超界时 `AGENT-MULTI-AGENT` 必须恢复单 Agent/串行协调与人工仲裁。

<!-- claim:SF-2026-ARXIV-2606-29425:start -->
Claim boundary：仅 `arXiv:2606.29425v1`；未证明边界定位 `https://arxiv.org/html/2606.29425v1 — §Conclusion and tested-debater scope`。
<!-- claim:SF-2026-ARXIV-2606-29425:end -->
<!-- review:SF-2026-ARXIV-2606-29425:end -->

<!-- review:SF-2026-ARXIV-2606-29441:start -->
### 2606.29441 — Closing the Activation-Cone Blind Spot: Response-Time Probing and Unified Defense

**问题与现有正文缺口。** Inference-time safety methods for large language models have proliferated, yet no systematic comparison exists. 逐段重读 owner 与相邻章后确认：当前章已把模型 sensor、policy/authorization 与 effect-time commit 分开，并拥有 fail-closed fallback。

**机制、状态、控制流与取舍。** 把 activation defense 的检测、干预与失效边界置于运行时控制面。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 把 activation defense 的检测、干预与失效边界置于运行时控制面。《Closing the Activation-Cone Blind Spot: Response-Time Probing and Unified Defense》的正证据锚定 `4 Experimental Setup; 5.1 No Single-Mechanism Paradigm Dominates`；`6 Discussion and Limitations` 没有建立跨 threat distribution、attacker adaptation 与 effect-time authorization 的防护承诺。因此该证据只能修正当前判断，超界时 `PLATFORM-SECURITY` 必须拒绝 effect commit 并转 sandbox/人工。

<!-- claim:SF-2026-ARXIV-2606-29441:start -->
Claim boundary：仅 `arXiv:2606.29441v1`；未证明边界定位 `https://arxiv.org/html/2606.29441v1 — §6 Discussion and Limitations`。
<!-- claim:SF-2026-ARXIV-2606-29441:end -->
<!-- review:SF-2026-ARXIV-2606-29441:end -->

<!-- review:SF-2026-ARXIV-2606-29445:start -->
### 2606.29445 — Bridging VideoQA and Video-Guided Agentic Tasks via Generalized Keyframe Extraction

**问题与现有正文缺口。** Video understanding is a fundamental capability for multimodal intelligence, and recent Multimodal Large Language Models (MLLMs) have achieved remarkable performance on Video Question Answering (VideoQA) benchmarks. 逐段重读 owner 与相邻章后确认：当前章已把 dataset/model/evaluator/metric/release 分权，并要求 slice、校准、污染与反例证据。

**机制、状态、控制流与取舍。** 把视频 GUI Agent 的长程观测与操作副作用纳入端到端评测。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 把视频 GUI Agent 的长程观测与操作副作用纳入端到端评测。《Bridging VideoQA and Video-Guided Agentic Tasks via Generalized Keyframe Extraction》的正证据锚定 `4 Experiments`；`Conclusion and benchmark-domain scope` 没有建立跨 dataset/model/evaluator revision 的 release acceptance 或生产 SLO。因此该证据只能修正当前判断，超界时 `PLATFORM-EVALUATION-SYSTEM` 必须保持 release Gate Open 并恢复完整分层评测。

<!-- claim:SF-2026-ARXIV-2606-29445:start -->
Claim boundary：仅 `arXiv:2606.29445v1`；未证明边界定位 `https://arxiv.org/html/2606.29445v1 — §Conclusion and benchmark-domain scope`。
<!-- claim:SF-2026-ARXIV-2606-29445:end -->
<!-- review:SF-2026-ARXIV-2606-29445:end -->

<!-- review:SF-2026-ARXIV-2606-29472:start -->
### 2606.29472 — Agent-Computer Observation Interfaces Enable Dynamic Computer Use

**问题与现有正文缺口。** SWE-agent established the action interface as an underexplored design axis for software-engineering agents; we make the analogous case for the observation interface in computer-use (CU) agents. 逐段重读 owner 与相邻章后确认：现有 Agent Platform 正文有 observation/action history 与 replay，却没有把连续 gated capture、audio transcript、persistent narration 与离散动作解耦成版本化 observation interface。

**机制、状态、控制流与取舍。** Computer-use 平台需要把 gated keyframe、audio transcript、persistent narration 与动作回执定义为版本化 observation interface，而不是让模型任意读取连续桌面流。接口 owner 管理 capture/retention 与 action-state identity；视觉 token 稀释或漏帧时回退高保真 capture/人工确认。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 只覆盖 DynaCU-Bench 浏览器任务与已测 CU models；Gemini 3 Flash 上 keyframe image-token dilution 已构成反例，因此 AOI 不是固定 bundle，也未证明桌面 OS、权限副作用或持续会议场景安全。退回高保真 capture 与人工确认。

<!-- claim:SF-2026-ARXIV-2606-29472:start -->
Claim boundary：仅 `arXiv:2606.29472v1`；未证明边界定位 `https://arxiv.org/pdf/2606.29472v1 — §5 per-model component ablation: keyframe regression through image-token dilution`。
<!-- claim:SF-2026-ARXIV-2606-29472:end -->
<!-- review:SF-2026-ARXIV-2606-29472:end -->

<!-- review:SF-2026-ARXIV-2606-29476:start -->
### 2606.29476 — CRAFT: Counterfactual Credit Assignment from Free Sibling Rollouts for Self-Distilled Agentic Reinforcement Learning

**问题与现有正文缺口。** Self-distilled agentic reinforcement learning augments trajectory-level reward with a token-level distillation loss, using as its teacher the same policy conditioned on privileged context. 逐段重读 owner 与相邻章后确认：当前章已把 terminal reward 拆为 typed trajectory credit，并记录 verifier、policy freshness 与 off-policy 边界。

**机制、状态、控制流与取舍。** 把 reward 构造与可验证约束结合并保留失败样本。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 把 reward 构造与可验证约束结合并保留失败样本。《CRAFT: Counterfactual Credit Assignment from Free Sibling Rollouts for Self-Distilled Agentic Reinforcement Learning》的正证据锚定 `5 Experiments`；`7 Discussion and Limitations` 没有建立跨 reward/verifier、policy freshness 与分布漂移的 on-policy 有效性。因此该证据只能修正当前判断，超界时 `TRAIN-GRPO` 必须恢复 on-policy terminal/verifier baseline。

<!-- claim:SF-2026-ARXIV-2606-29476:start -->
Claim boundary：仅 `arXiv:2606.29476v1`；未证明边界定位 `https://arxiv.org/html/2606.29476v1 — §7 Discussion and Limitations`。
<!-- claim:SF-2026-ARXIV-2606-29476:end -->
<!-- review:SF-2026-ARXIV-2606-29476:end -->

<!-- review:SF-2026-ARXIV-2606-29481:start -->
### 2606.29481 — To Reason or to Fabricate: Reasoning Without Shortcuts via Hint-Anchored Pairwise Aggregation

**问题与现有正文缺口。** While reinforcement learning (RL) significantly enhances LLM reasoning, its efficacy is severely undermined by Pre-RL data overlap, where RL datasets overlap with pretraining or SFT corpora, causing models to exploit shortcuts by memorizing correct answers and fabricating post-hoc reasoning. 逐段重读 owner 与相邻章后确认：当前章已把 terminal reward 拆为 typed trajectory credit，并记录 verifier、policy freshness 与 off-policy 边界。

**机制、状态、控制流与取舍。** 按难度与策略状态控制 rollout 采样和更新。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 按难度与策略状态控制 rollout 采样和更新。《To Reason or to Fabricate: Reasoning Without Shortcuts via Hint-Anchored Pairwise Aggregation》的正证据锚定 `3 Experimental Setup`；`2.2 Direct KL Optimization and Its Limitations` 没有建立跨 reward/verifier、policy freshness 与分布漂移的 on-policy 有效性。因此该证据只能修正当前判断，超界时 `TRAIN-GRPO` 必须恢复 on-policy terminal/verifier baseline。

<!-- claim:SF-2026-ARXIV-2606-29481:start -->
Claim boundary：仅 `arXiv:2606.29481v1`；未证明边界定位 `https://arxiv.org/html/2606.29481v1 — §2.2 Direct KL Optimization and Its Limitations`。
<!-- claim:SF-2026-ARXIV-2606-29481:end -->
<!-- review:SF-2026-ARXIV-2606-29481:end -->

<!-- review:SF-2026-ARXIV-2606-29490:start -->
### 2606.29490 — Reported Confidence in LLMs Tracks Commitment More Than Correctness

**问题与现有正文缺口。** Confidence is an estimate of the probability that a chosen answer is correct. 逐段重读 owner 与相邻章后确认：当前章已把 dataset/model/evaluator/metric/release 分权，并要求 slice、校准、污染与反例证据。

**机制、状态、控制流与取舍。** 把置信承诺、校准误差与拒答决策绑定。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 把置信承诺、校准误差与拒答决策绑定。《Reported Confidence in LLMs Tracks Commitment More Than Correctness》的正证据锚定 `1.2 Supplemental Results`；`Conclusion and evaluated-distribution scope` 没有建立跨 dataset/model/evaluator revision 的 release acceptance 或生产 SLO。因此该证据只能修正当前判断，超界时 `PLATFORM-EVALUATION-SYSTEM` 必须保持 release Gate Open 并恢复完整分层评测。

<!-- claim:SF-2026-ARXIV-2606-29490:start -->
Claim boundary：仅 `arXiv:2606.29490v1`；未证明边界定位 `https://arxiv.org/html/2606.29490v1 — §Conclusion and evaluated-distribution scope`。
<!-- claim:SF-2026-ARXIV-2606-29490:end -->
<!-- review:SF-2026-ARXIV-2606-29490:end -->

<!-- review:SF-2026-ARXIV-2606-29493:start -->
### 2606.29493 — Faults in Our Formal Benchmarking: Dataset Defects and Evaluation Failures in Lean Theorem Proving

**问题与现有正文缺口。** Benchmarks for LLM-assisted theorem proving in Lean are often treated as intrinsically reliable because every solved instance comes with a machine-checked proof. 逐段重读 owner 与相邻章后确认：当前章已把 dataset/model/evaluator/metric/release 分权，并要求 slice、校准、污染与反例证据。

**机制、状态、控制流与取舍。** 把形式化 benchmark 的语义正确与语法通过分层审计。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 把形式化 benchmark 的语义正确与语法通过分层审计。《Faults in Our Formal Benchmarking: Dataset Defects and Evaluation Failures in Lean Theorem Proving》的正证据锚定 `2 What Formal Benchmarking Certifies (and What It Does Not)`；`7 Limitations` 没有建立跨 dataset/model/evaluator revision 的 release acceptance 或生产 SLO。因此该证据只能修正当前判断，超界时 `PLATFORM-EVALUATION-SYSTEM` 必须保持 release Gate Open 并恢复完整分层评测。

<!-- claim:SF-2026-ARXIV-2606-29493:start -->
Claim boundary：仅 `arXiv:2606.29493v1`；未证明边界定位 `https://arxiv.org/html/2606.29493v1 — §7 Limitations`。
<!-- claim:SF-2026-ARXIV-2606-29493:end -->
<!-- review:SF-2026-ARXIV-2606-29493:end -->

<!-- review:SF-2026-ARXIV-2606-29501:start -->
### 2606.29501 — Learning Transferable Dynamics Priors from Action to World Modeling

**问题与现有正文缺口。** We study action-conditioned world modeling as a scalable way to learn transferable dynamics priors for robot learning. 逐段重读 owner 与相邻章后确认：当前章已区分 action-conditioned transition、persistent state、rollout 与 physical commit。

**机制、状态、控制流与取舍。** 把 action-conditioned rollout 与可干预世界状态联结。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 把 action-conditioned rollout 与可干预世界状态联结。《Learning Transferable Dynamics Priors from Action to World Modeling》的正证据锚定 `4 Experiments`；`4.5 Ablations and discussions` 没有建立跨 environment、observation dynamics 与 physical commit 的 rollout fidelity。因此该证据只能修正当前判断，超界时 `MULTIMODAL-WORLD-MODELS` 必须停止 imagined rollout 并请求真实 observation。

<!-- claim:SF-2026-ARXIV-2606-29501:start -->
Claim boundary：仅 `arXiv:2606.29501v1`；未证明边界定位 `https://arxiv.org/html/2606.29501v1 — §4.5 Ablations and discussions`。
<!-- claim:SF-2026-ARXIV-2606-29501:end -->
<!-- review:SF-2026-ARXIV-2606-29501:end -->

<!-- review:SF-2026-ARXIV-2606-29502:start -->
### 2606.29502 — UCOB: Learning to Utilize and Evolve Agentic Skills via Credit-Aware On-Policy Bidirectional Self-Distillation

**问题与现有正文缺口。** Skill memories can improve agentic reinforcement learning by reusing past experience as textual guidance, but retrieved skills are not oracular: they may help in one state while misleading the same policy in another. 逐段重读 owner 与相邻章后确认：当前章已拥有 admission/retention/forgetting、provenance、transaction 与 raw evidence fallback。

**机制、状态、控制流与取舍。** 把技能发现、组合与持久化变成可更新 Agent 状态。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 把技能发现、组合与持久化变成可更新 Agent 状态。《UCOB: Learning to Utilize and Evolve Agentic Skills via Credit-Aware On-Policy Bidirectional Self-Distillation》的正证据锚定 `6 Experiments`；`Conclusion and evaluated-environment boundary` 没有建立跨 workload、write policy、retention horizon 与 provenance shift 的记忆收益。因此该证据只能修正当前判断，超界时 `AGENT-MEMORY` 必须拒绝写入并保留旧 memory revision。

<!-- claim:SF-2026-ARXIV-2606-29502:start -->
Claim boundary：仅 `arXiv:2606.29502v1`；未证明边界定位 `https://arxiv.org/html/2606.29502v1 — §Conclusion and evaluated-environment boundary`。
<!-- claim:SF-2026-ARXIV-2606-29502:end -->
<!-- review:SF-2026-ARXIV-2606-29502:end -->

<!-- review:SF-2026-ARXIV-2606-29506:start -->
### 2606.29506 — Benchmark AUC Is Not Deployable Reliability: A Cross-Dataset Audit of Off-the-Shelf Features for Surveillance Video Anomaly Detection

**问题与现有正文缺口。** Automated "suspicious behavior" flagging is a headline promise of AI surveillance, and the field reports high frame-level ROC-AUC on standard video anomaly detection benchmarks. 逐段重读 owner 与相邻章后确认：当前章已把 dataset/model/evaluator/metric/release 分权，并要求 slice、校准、污染与反例证据。

**机制、状态、控制流与取舍。** 揭示跨数据集切分污染并改变 benchmark release contract。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 揭示跨数据集切分污染并改变 benchmark release contract。《Benchmark AUC Is Not Deployable Reliability: A Cross-Dataset Audit of Off-the-Shelf Features for Surveillance Video Anomaly Detection》的正证据锚定 `IV Results`；`VII Discussion` 没有建立跨 dataset/model/evaluator revision 的 release acceptance 或生产 SLO。因此该证据只能修正当前判断，超界时 `PLATFORM-EVALUATION-SYSTEM` 必须保持 release Gate Open 并恢复完整分层评测。

<!-- claim:SF-2026-ARXIV-2606-29506:start -->
Claim boundary：仅 `arXiv:2606.29506v1`；未证明边界定位 `https://arxiv.org/html/2606.29506v1 — §VII Discussion`。
<!-- claim:SF-2026-ARXIV-2606-29506:end -->
<!-- review:SF-2026-ARXIV-2606-29506:end -->

<!-- review:SF-2026-ARXIV-2606-29520:start -->
### 2606.29520 — SAKE: Software Architectural Knowledge Evaluation Benchmark for Large Language Models

**问题与现有正文缺口。** Large Language Models (LLMs) are increasingly used as assistants across the software development lifecycle, yet their ability to reason about software architecture remains largely unmeasured. 逐段重读 owner 与相邻章后确认：当前章已把 dataset/model/evaluator/metric/release 分权，并要求 slice、校准、污染与反例证据。

**机制、状态、控制流与取舍。** 把安全知识、执行与拒答分层测量。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 把安全知识、执行与拒答分层测量。《SAKE: Software Architectural Knowledge Evaluation Benchmark for Large Language Models》的正证据锚定 `Benchmark construction and evaluation`；`7 Threats to Validity` 没有建立跨 dataset/model/evaluator revision 的 release acceptance 或生产 SLO。因此该证据只能修正当前判断，超界时 `PLATFORM-EVALUATION-SYSTEM` 必须保持 release Gate Open 并恢复完整分层评测。

<!-- claim:SF-2026-ARXIV-2606-29520:start -->
Claim boundary：仅 `arXiv:2606.29520v1`；未证明边界定位 `https://arxiv.org/html/2606.29520v1 — §7 Threats to Validity`。
<!-- claim:SF-2026-ARXIV-2606-29520:end -->
<!-- review:SF-2026-ARXIV-2606-29520:end -->

<!-- review:SF-2026-ARXIV-2606-29522:start -->
### 2606.29522 — Do Models Read What They Write? Causal Registers in Scratchpad Reasoning

**问题与现有正文缺口。** A central hope behind process supervision is that models can expose intermediate variables that matter for their later behavior. 逐段重读 owner 与相邻章后确认：现有 Context 正文区分 raw evidence、derived view 与 compression fidelity，但没有验证 scratchpad register 是否被后续计算因果读取的 intervention contract。

**机制、状态、控制流与取舍。** Scratchpad 不能仅按可见文本保存；因果干预结果应把其中哪些 register 实际驱动后续输出记录成 request-local diagnostic state。该 probe 只拥有观测/路由权，干预不稳定时回退原始 scratchpad 与外部 verifier，不能据此删除未被识别的约束。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 只在 Q8/D8 合成 transition task、Qwen2.5-Coder-7B 与 Mistral-7B-v0.3 上证明特定 written state 被因果读取；显式 scratchpad 的其他 token、自然语言推理和真实 Agent memory 均未被证明忠实。probe 不稳定时保留原文本与外部 verifier。

<!-- claim:SF-2026-ARXIV-2606-29522:start -->
Claim boundary：仅 `arXiv:2606.29522v1`；未证明边界定位 `https://arxiv.org/html/2606.29522v1 — §Conclusion and intervention-identifiability scope`。
<!-- claim:SF-2026-ARXIV-2606-29522:end -->
<!-- review:SF-2026-ARXIV-2606-29522:end -->

<!-- review:SF-2026-ARXIV-2606-29526:start -->
### 2606.29526 — The Mirage of Optimizing Training Policies: Monotonic Inference Policies as the Real Objective for LLM Reinforcement Learning

**问题与现有正文缺口。** Reinforcement learning (RL) has gained growing attention in large language model (LLM) post-training, yet RL training remains fragile and can suffer from instability or collapse. 逐段重读 owner 与相邻章后确认：当前章已把 terminal reward 拆为 typed trajectory credit，并记录 verifier、policy freshness 与 off-policy 边界。

**机制、状态、控制流与取舍。** 把多阶段策略改进与验证门控组织成训练控制流。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 把多阶段策略改进与验证门控组织成训练控制流。《The Mirage of Optimizing Training Policies: Monotonic Inference Policies as the Real Objective for LLM Reinforcement Learning》的正证据锚定 `5 Experiments`；`Limitations` 没有建立跨 reward/verifier、policy freshness 与分布漂移的 on-policy 有效性。因此该证据只能修正当前判断，超界时 `TRAIN-GRPO` 必须恢复 on-policy terminal/verifier baseline。

<!-- claim:SF-2026-ARXIV-2606-29526:start -->
Claim boundary：仅 `arXiv:2606.29526v1`；未证明边界定位 `https://arxiv.org/html/2606.29526v1 — §Limitations`。
<!-- claim:SF-2026-ARXIV-2606-29526:end -->
<!-- review:SF-2026-ARXIV-2606-29526:end -->

<!-- review:SF-2026-ARXIV-2606-29532:start -->
### 2606.29532 — SemJoin: Semantic Join Optimization

**问题与现有正文缺口。** Integrating unstructured data into relational database systems is increasingly important as demand grows for natural language querying and analysis. 逐段重读 owner 与相邻章后确认：当前章已拥有 typed query plan、router、metric/index identity、evidence sufficiency 与失败回退。

**机制、状态、控制流与取舍。** 把语义 join 的候选生成、验证与代价纳入查询计划。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 把语义 join 的候选生成、验证与代价纳入查询计划。《SemJoin: Semantic Join Optimization》的正证据锚定 `4 Evaluation`；`Conclusion and evaluated-database scope` 没有建立跨 corpus、query distribution、retriever/index revision 与生成器的检索收益。因此该证据只能修正当前判断，超界时 `AGENT-RAG` 必须恢复固定、已校准的 retrieval plan。

<!-- claim:SF-2026-ARXIV-2606-29532:start -->
Claim boundary：仅 `arXiv:2606.29532v1`；未证明边界定位 `https://arxiv.org/html/2606.29532v1 — §Conclusion and evaluated-database scope`。
<!-- claim:SF-2026-ARXIV-2606-29532:end -->
<!-- review:SF-2026-ARXIV-2606-29532:end -->

<!-- review:SF-2026-ARXIV-2606-29537:start -->
### 2606.29537 — OSWorld 2.0: Benchmarking Computer Use Agents on Long-Horizon Real-World Tasks

**问题与现有正文缺口。** Existing computer-use benchmarks fail to capture the realism, complexity, and long-horizon demands of real-world computer use, limiting their ability to reveal the limitations of frontier agents. 逐段重读 owner 与相邻章后确认：当前章已把 dataset/model/evaluator/metric/release 分权，并要求 slice、校准、污染与反例证据。

**机制、状态、控制流与取舍。** 把 OSWorld 环境、任务与判定器升级为版本化 release contract。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 把 OSWorld 环境、任务与判定器升级为版本化 release contract。《OSWorld 2.0: Benchmarking Computer Use Agents on Long-Horizon Real-World Tasks》的正证据锚定 `2 OSWorld 2.0 Benchmark; evaluation protocol`；`6 Limitations` 没有建立跨 dataset/model/evaluator revision 的 release acceptance 或生产 SLO。因此该证据只能修正当前判断，超界时 `PLATFORM-EVALUATION-SYSTEM` 必须保持 release Gate Open 并恢复完整分层评测。

<!-- claim:SF-2026-ARXIV-2606-29537:start -->
Claim boundary：仅 `arXiv:2606.29537v1`；未证明边界定位 `https://arxiv.org/html/2606.29537v1 — §6 Limitations`。
<!-- claim:SF-2026-ARXIV-2606-29537:end -->
<!-- review:SF-2026-ARXIV-2606-29537:end -->

<!-- review:SF-2026-ARXIV-2606-29538:start -->
### 2606.29538 — RESOURCE2SKILL: Distilling Executable Agent Skills from Human-Created Multimodal Resources

**问题与现有正文缺口。** Skills are a useful abstraction for software agents, turning human and agent experience into reusable procedural knowledge. 逐段重读 owner 与相邻章后确认：当前章已拥有 versioned state machine、DAG、evaluator-driven search、replay 与 compensation。

**机制、状态、控制流与取舍。** 把资源发现转成可执行 skill，并保留权限与失败边界。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 把资源发现转成可执行 skill，并保留权限与失败边界。《RESOURCE2SKILL: Distilling Executable Agent Skills from Human-Created Multimodal Resources》的正证据锚定 `4 Experiments`；`M Limitations` 没有建立跨 environment、tool semantics、checkpoint 与 compensation path 的可复算性。因此该证据只能修正当前判断，超界时 `AGENT-WORKFLOW` 必须停在可恢复 checkpoint 并执行 compensation。

<!-- claim:SF-2026-ARXIV-2606-29538:start -->
Claim boundary：仅 `arXiv:2606.29538v1`；未证明边界定位 `https://arxiv.org/html/2606.29538v1 — §M Limitations`。
<!-- claim:SF-2026-ARXIV-2606-29538:end -->
<!-- review:SF-2026-ARXIV-2606-29538:end -->

<!-- review:SF-2026-ARXIV-2606-29541:start -->
### 2606.29541 — Learned Coordination Conventions in Cooperative MARL: Measuring the Translation Gap Between Theory-Informed Roles and Learned Routing

**问题与现有正文缺口。** Role-semantic assignments provide priors over how heterogeneous agents may coordinate, but cooperative MARL systems instead settle on conventions through decentralized, non-stationary learning, with no guarantee that the resulting structure matches those priors. 逐段重读 owner 与相邻章后确认：当前章已拥有 topology、message/state、aggregation、delegation、independent verification 与 coordination tax。

**机制、状态、控制流与取舍。** 把 MARL 协调的共享意图与通信失效纳入状态。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 把 MARL 协调的共享意图与通信失效纳入状态。《Learned Coordination Conventions in Cooperative MARL: Measuring the Translation Gap Between Theory-Informed Roles and Learned Routing》的正证据锚定 `5 Experiments`；`6 Discussion` 没有建立跨 agent population、message protocol、error correlation 与 coordination load 的聚合收益。因此该证据只能修正当前判断，超界时 `AGENT-MULTI-AGENT` 必须恢复单 Agent/串行协调与人工仲裁。

<!-- claim:SF-2026-ARXIV-2606-29541:start -->
Claim boundary：仅 `arXiv:2606.29541v1`；未证明边界定位 `https://arxiv.org/html/2606.29541v1 — §6 Discussion`。
<!-- claim:SF-2026-ARXIV-2606-29541:end -->
<!-- review:SF-2026-ARXIV-2606-29541:end -->

<!-- review:SF-2026-ARXIV-2606-29544:start -->
### 2606.29544 — Proteus: Automated Adversarial Robustness Testing for Audio Deepfake Detectors

**问题与现有正文缺口。** We present Proteus, a framework developed at Resemble AI for automated robustness testing of our audio deepfake detection system. 逐段重读 owner 与相邻章后确认：当前章已把模型 sensor、policy/authorization 与 effect-time commit 分开，并拥有 fail-closed fallback。

**机制、状态、控制流与取舍。** 把生产分布漂移、攻击与回退纳入鲁棒性发布证据。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 把生产分布漂移、攻击与回退纳入鲁棒性发布证据。《Proteus: Automated Adversarial Robustness Testing for Audio Deepfake Detectors》的正证据锚定 `3 Results`；`Conclusion and tested-shift boundary` 没有建立跨 threat distribution、attacker adaptation 与 effect-time authorization 的防护承诺。因此该证据只能修正当前判断，超界时 `PLATFORM-SECURITY` 必须拒绝 effect commit 并转 sandbox/人工。

<!-- claim:SF-2026-ARXIV-2606-29544:start -->
Claim boundary：仅 `arXiv:2606.29544v1`；未证明边界定位 `https://arxiv.org/html/2606.29544v1 — §Conclusion and tested-shift boundary`。
<!-- claim:SF-2026-ARXIV-2606-29544:end -->
<!-- review:SF-2026-ARXIV-2606-29544:end -->

<!-- review:SF-2026-ARXIV-2606-29554:start -->
### 2606.29554 — Optimizer Memory Makes Shuffle Order a First-Order Source of Fine-Tuning Noise

**问题与现有正文缺口。** Shuffle order can be a larger source of fine-tuning noise than a memoryless analysis predicts: fixed-clock optimizer memory makes local equal-multiset contrasts first order in the learning rate rather than second order, and the resulting order channel can be large enough for a single seed to flip a close A/B comparison. 逐段重读 owner 与相邻章后确认：当前章已把 optimizer、schedule、batch/tokens 与 scaling identity 分开；新证据只有改变外推或控制合同才可追加。

**机制、状态、控制流与取舍。** 揭示数据 shuffle 与 optimizer state 的耦合，改变复现合同。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 揭示数据 shuffle 与 optimizer state 的耦合，改变复现合同。《Optimizer Memory Makes Shuffle Order a First-Order Source of Fine-Tuning Noise》的正证据锚定 `5 Empirical evidence`；`7 Discussion` 没有建立跨 architecture、optimizer、token budget 与更大训练尺度的可迁移性。因此该证据只能修正当前判断，超界时 `TRAIN-PRETRAINING` 必须恢复邻近规模 sweep 与已验证 schedule。

<!-- claim:SF-2026-ARXIV-2606-29554:start -->
Claim boundary：仅 `arXiv:2606.29554v1`；未证明边界定位 `https://arxiv.org/html/2606.29554v1 — §7 Discussion`。
<!-- claim:SF-2026-ARXIV-2606-29554:end -->
<!-- review:SF-2026-ARXIV-2606-29554:end -->

<!-- review:SF-2026-ARXIV-2606-29563:start -->
### 2606.29563 — Coverage-Driven KV Cache Eviction for Efficient and Improved Inference of LLM

**问题与现有正文缺口。** Large language models (LLMs) excel at complex tasks like question answering and summarization, thanks to their ability to handle long-context inputs. 逐段重读 owner 与相邻章后确认：当前章已拥有 workload-aware eviction、风险门、可恢复 recall 与完整缓存回退。

**机制、状态、控制流与取舍。** 用跨头跨层 coverage 状态驱动 KV 驱逐并保留完整缓存回退。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 用跨头跨层 coverage 状态驱动 KV 驱逐并保留完整缓存回退。《Coverage-Driven KV Cache Eviction for Efficient and Improved Inference of LLM》的正证据锚定 `5 Experiments; 5.1 Experimental setup`；`5.3 Discussion; 5.3.5 Computational Complexity` 没有建立跨 attention pattern、context length 与 workload shift 的 eviction 安全性。因此该证据只能修正当前判断，超界时 `INFER-KV-CACHE` 必须恢复完整 KV 或保守 eviction。

<!-- claim:SF-2026-ARXIV-2606-29563:start -->
Claim boundary：仅 `arXiv:2606.29563v1`；未证明边界定位 `https://arxiv.org/html/2606.29563v1 — §5.3 Discussion; 5.3.5 Computational Complexity`。
<!-- claim:SF-2026-ARXIV-2606-29563:end -->
<!-- review:SF-2026-ARXIV-2606-29563:end -->

<!-- review:SF-2026-ARXIV-2606-29565:start -->
### 2606.29565 — Speculative Pre-Positioning: Decoding Stateful Sessions to the Next Decision Point Off the Critical Path

**问题与现有正文缺口。** A stateless inference server (vLLM, SGLang, TensorRT-LLM) idles between requests while the accelerator waits; a stateful session reclaims that idle time. 逐段重读 owner 与相邻章后确认：现有 request state machine 到 RELEASED 为止，没有持有跨请求 idle-window speculative state、base-state identity、confidence gate 与 mutation invalidation。

**机制、状态、控制流与取舍。** 有状态会话的 idle time 可用于推演到下个 decision point；request lifecycle owner 保存 speculative state、acceptance confidence 与 base-state identity，命中后才原子提交。False accept、用户输入或 state drift 立即作废预推进并回退正常 decode。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 只在 LayerScale 专有 engine、单 H100、70B-class 4-bit target 上测得 capability-gated fast path；8B BF16 不触发 gate，且大量收益为测量常数上的闭式推导。任何 state mutation 或置信漂移都必须 invalidate 并恢复普通 decode。

<!-- claim:SF-2026-ARXIV-2606-29565:start -->
Claim boundary：仅 `arXiv:2606.29565v1`；未证明边界定位 `https://arxiv.org/html/2606.29565v1 — §6 Discussion`。
<!-- claim:SF-2026-ARXIV-2606-29565:end -->
<!-- review:SF-2026-ARXIV-2606-29565:end -->

<!-- review:SF-2026-ARXIV-2606-29567:start -->
### 2606.29567 — SurrogateShield: Beyond Redaction for High-Utility, Privacy-Preserving LLM Interactions

**问题与现有正文缺口。** LLM-based assistants transmit user queries verbatim to third-party API endpoints that lie outside the user's audit or control. 逐段重读 owner 与相邻章后确认：当前章已把模型 sensor、policy/authorization 与 effect-time commit 分开，并拥有 fail-closed fallback。

**机制、状态、控制流与取舍。** 把 PII 替身生成、加密映射与还原置于本地代理控制面。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 把 PII 替身生成、加密映射与还原置于本地代理控制面。《SurrogateShield: Beyond Redaction for High-Utility, Privacy-Preserving LLM Interactions》的正证据锚定 `4 Evaluation Methodology`；`6 Discussion` 没有建立跨 threat distribution、attacker adaptation 与 effect-time authorization 的防护承诺。因此该证据只能修正当前判断，超界时 `PLATFORM-SECURITY` 必须拒绝 effect commit 并转 sandbox/人工。

<!-- claim:SF-2026-ARXIV-2606-29567:start -->
Claim boundary：仅 `arXiv:2606.29567v1`；未证明边界定位 `https://arxiv.org/html/2606.29567v1 — §6 Discussion`。
<!-- claim:SF-2026-ARXIV-2606-29567:end -->
<!-- review:SF-2026-ARXIV-2606-29567:end -->

<!-- review:SF-2026-ARXIV-2606-29571:start -->
### 2606.29571 — Anisotropy Decides Cosine vs. Rank Metrics for Text Embeddings

**问题与现有正文缺口。** The standard way to compare two text embeddings is cosine similarity. 逐段重读 owner 与相邻章后确认：现有 RAG 正文版本化 metric/index identity，但没有把 encoder anisotropy 变成上线前 cosine-versus-rank/L1 的 metric selection diagnostic。

**机制、状态、控制流与取舍。** Embedding distance 不应固定为 cosine；retrieval owner 先测 anisotropy，再在同一 corpus/query revision 上选择 cosine、rank 或 L1 类 metric，并把 metric 写入 index identity。诊断漂移或收益不稳时回退已校准 cosine/混合检索。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 只比较 19 个 parameter-free metric、19 encoder 与七个静态数据集；0.01 crowded split、dominant-direction removal 和相关性未证明在线 corpus 漂移下的因果门槛，也未覆盖 learned metric。收益消失时恢复已校准 cosine/混合检索。

<!-- claim:SF-2026-ARXIV-2606-29571:start -->
Claim boundary：仅 `arXiv:2606.29571v1`；未证明边界定位 `https://arxiv.org/html/2606.29571v1 — §6 Limitations`。
<!-- claim:SF-2026-ARXIV-2606-29571:end -->
<!-- review:SF-2026-ARXIV-2606-29571:end -->

<!-- review:SF-2026-ARXIV-2606-29573:start -->
### 2606.29573 — Reliability-Prioritized Fine-Grained Generation in Multimodal Large

**问题与现有正文缺口。** Multimodal large language models (MLLMs) are increasingly expected to generate fine-grained descriptions of visual content. 逐段重读 owner 与相邻章后确认：当前章已把 dataset/model/evaluator/metric/release 分权，并要求 slice、校准、污染与反例证据。

**机制、状态、控制流与取舍。** 把多模态生成粒度与可靠性共同纳入发布阈值。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 把多模态生成粒度与可靠性共同纳入发布阈值。《Reliability-Prioritized Fine-Grained Generation in Multimodal Large》的正证据锚定 `2.1 MLLM Benchmarks; experiments`；`Conclusion and expert-verified benchmark scope` 没有建立跨 dataset/model/evaluator revision 的 release acceptance 或生产 SLO。因此该证据只能修正当前判断，超界时 `PLATFORM-EVALUATION-SYSTEM` 必须保持 release Gate Open 并恢复完整分层评测。

<!-- claim:SF-2026-ARXIV-2606-29573:start -->
Claim boundary：仅 `arXiv:2606.29573v1`；未证明边界定位 `https://arxiv.org/html/2606.29573v1 — §Conclusion and expert-verified benchmark scope`。
<!-- claim:SF-2026-ARXIV-2606-29573:end -->
<!-- review:SF-2026-ARXIV-2606-29573:end -->

<!-- review:SF-2026-ARXIV-2606-29580:start -->
### 2606.29580 — MAM-AI: An On-Device Medical Retrieval-Augmented Generation System for Nurses and Midwives in Zanzibar

**问题与现有正文缺口。** Maternal and newborn mortality remain among the highest in sub-Saharan Africa, where midwifery care is often delivered by nurses who lack midwifery training to international standards, and consulting authoritative guidance at the point of care is hard: the guidelines are long and connectivity is intermittent. 逐段重读 owner 与相邻章后确认：当前章已拥有 typed query plan、router、metric/index identity、evidence sufficiency 与失败回退。

**机制、状态、控制流与取舍。** 把离线索引、设备内生成、citation 与语料缺口串成端侧 RAG 合同。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 把离线索引、设备内生成、citation 与语料缺口串成端侧 RAG 合同。《MAM-AI: An On-Device Medical Retrieval-Augmented Generation System for Nurses and Midwives in Zanzibar》的正证据锚定 `4 Evaluation Methodology; Sections 5-8 component results`；`9 Discussion; 10 Limitations and Future Work` 没有建立跨 corpus、query distribution、retriever/index revision 与生成器的检索收益。因此该证据只能修正当前判断，超界时 `AGENT-RAG` 必须恢复固定、已校准的 retrieval plan。

<!-- claim:SF-2026-ARXIV-2606-29580:start -->
Claim boundary：仅 `arXiv:2606.29580v1`；未证明边界定位 `https://arxiv.org/pdf/2606.29580v1 — §9 Discussion; 10 Limitations and Future Work`。
<!-- claim:SF-2026-ARXIV-2606-29580:end -->
<!-- review:SF-2026-ARXIV-2606-29580:end -->

<!-- review:SF-2026-ARXIV-2606-29581:start -->
### 2606.29581 — The Joint Effect of Quantization and Sampling Temperature on LLM Safety Alignment: A Factorial Analysis

**问题与现有正文缺口。** Modern LLM deployments often combine quantization with higher sampling temperatures to reduce cost, latency, or repetition, yet safety evaluations usually treat these as fixed implementation details. 逐段重读 owner 与相邻章后确认：现有 Security 正文有 threat matrix 与 fail-closed release，但未把 quantization precision、sampling temperature、multi-sample stability 与多 benchmark safety slice 联合成同一 release identity。

**机制、状态、控制流与取舍。** 量化验收与 sampling temperature 不能分开：security release matrix 必须联合保存 model/quantization/sampler/multi-sample identity，并在多个 safety benchmark 上检查交互失稳。任一切片回归时回退已验收 precision/decoding 配置，而不是只恢复 greedy 单次测试。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 当前 official exact-v1 的 Abstract 与 §3 一致披露 9 models、161 configurations、AdvBench+XSTest 与约 322k responses；证据只覆盖以 Pile validation calibration 的 AWQ INT4/GPTQ INT8、2B–8B 模型与静态 AdvBench，未证明 NF4/GGUF/对抗式 calibration、>70B、adaptive jailbreak/prompt injection 或 judge 完美可靠。任一切片回归即恢复已验收 precision/sampler。

<!-- claim:SF-2026-ARXIV-2606-29581:start -->
Claim boundary：仅 `arXiv:2606.29581v1`；未证明边界定位 `https://arxiv.org/html/2606.29581v1 — §5 Discussion`。
<!-- claim:SF-2026-ARXIV-2606-29581:end -->
<!-- review:SF-2026-ARXIV-2606-29581:end -->

<!-- review:SF-2026-ARXIV-2606-29592:start -->
### 2606.29592 — STEMGym: Benchmarking Sequential Decision-Making under Dose Budgets in Autonomous Electron Microscopy

**问题与现有正文缺口。** A central premise of autonomous scientific imaging is that smarter navigation, whether Bayesian, RL-based, or otherwise adaptive, is the principal lever for sample-efficient acquisition. 逐段重读 owner 与相邻章后确认：当前章已把 dataset/model/evaluator/metric/release 分权，并要求 slice、校准、污染与反例证据。

**机制、状态、控制流与取舍。** 把 perception、navigation、planning 与剂量预算解耦评测。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 把 perception、navigation、planning 与剂量预算解耦评测。《STEMGym: Benchmarking Sequential Decision-Making under Dose Budgets in Autonomous Electron Microscopy》的正证据锚定 `4 Experiments`；`5 Limitations` 没有建立跨 dataset/model/evaluator revision 的 release acceptance 或生产 SLO。因此该证据只能修正当前判断，超界时 `PLATFORM-EVALUATION-SYSTEM` 必须保持 release Gate Open 并恢复完整分层评测。

<!-- claim:SF-2026-ARXIV-2606-29592:start -->
Claim boundary：仅 `arXiv:2606.29592v1`；未证明边界定位 `https://arxiv.org/html/2606.29592v1 — §5 Limitations`。
<!-- claim:SF-2026-ARXIV-2606-29592:end -->
<!-- review:SF-2026-ARXIV-2606-29592:end -->

<!-- review:SF-2026-ARXIV-2606-29601:start -->
### 2606.29601 — Langshaw: Declarative Interaction Protocols Based on Sayso and Conflict

**问题与现有正文缺口。** Current languages for specifying multiagent protocols either over-constrain protocol enactments or complicate capturing their meanings. 逐段重读 owner 与相邻章后确认：现有 Multi-Agent 正文有 topology、message state 与 delegation，却没有把 attribute sayso、action nono/nogo 编译为可做 safety/liveness 检查的异步协议。

**机制、状态、控制流与取舍。** 异步多 Agent 协议应把 attribute-setting priority、action conflict 与禁止组合编译为 sayso/nono/nogo 等声明式状态，再由协议 runtime 决定可提交 transition。规则冲突或编译覆盖不足时回退串行 coordinator/人工仲裁。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 只验证有限 Langshaw examples 到 BSPL tableau 的 safety/liveness 与编译时间；未证明开放网络中的 delivery、identity、Byzantine role 或工具副作用。协议编译/验证超界时回到串行 coordinator 与人工仲裁。

<!-- claim:SF-2026-ARXIV-2606-29601:start -->
Claim boundary：仅 `arXiv:2606.29601v1`；未证明边界定位 `https://arxiv.org/html/2606.29601v1 — §7 Discussion: Conclusion and Perspectives`。
<!-- claim:SF-2026-ARXIV-2606-29601:end -->
<!-- review:SF-2026-ARXIV-2606-29601:end -->

<!-- review:SF-2026-ARXIV-2606-29602:start -->
### 2606.29602 — An Empirical Evaluation of Prompt Injection Vulnerabilities in Large Language Models Across Multilingual and Obfuscated Attack Scenarios

**问题与现有正文缺口。** Large Language Models (LLMs) have rapidly evolved, transforming industries by automating complex tasks and generating human-like content. 逐段重读 owner 与相邻章后确认：当前章已把模型 sensor、policy/authorization 与 effect-time commit 分开，并拥有 fail-closed fallback。

**机制、状态、控制流与取舍。** 把多语言、编码与多阶段 prompt injection 纳入威胁矩阵。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 把多语言、编码与多阶段 prompt injection 纳入威胁矩阵。《An Empirical Evaluation of Prompt Injection Vulnerabilities in Large Language Models Across Multilingual and Obfuscated Attack Scenarios》的正证据锚定 `II-D Empirical Evaluations of LLM Safety; IV Results`；`V Discussion` 没有建立跨 threat distribution、attacker adaptation 与 effect-time authorization 的防护承诺。因此该证据只能修正当前判断，超界时 `PLATFORM-SECURITY` 必须拒绝 effect commit 并转 sandbox/人工。

<!-- claim:SF-2026-ARXIV-2606-29602:start -->
Claim boundary：仅 `arXiv:2606.29602v1`；未证明边界定位 `https://arxiv.org/html/2606.29602v1 — §V Discussion`。
<!-- claim:SF-2026-ARXIV-2606-29602:end -->
<!-- review:SF-2026-ARXIV-2606-29602:end -->

<!-- review:SF-2026-ARXIV-2606-29604:start -->
### 2606.29604 — Mechanistically Eliciting Latent Behaviors in Language Models

**问题与现有正文缺口。** We aim to discover diverse, generalizable perturbations of LLM internals that can surface hidden behavioral modes. 逐段重读 owner 与相邻章后确认：当前章已把模型 sensor、policy/authorization 与 effect-time commit 分开，并拥有 fail-closed fallback。

**机制、状态、控制流与取舍。** 把权重/激活扰动用于潜在行为发现并定义代理选择边界。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 把权重/激活扰动用于潜在行为发现并定义代理选择边界。《Mechanistically Eliciting Latent Behaviors in Language Models》的正证据锚定 `Experimental setup; latent-behavior evaluation`；`Conclusion and model-organism scope` 没有建立跨 threat distribution、attacker adaptation 与 effect-time authorization 的防护承诺。因此该证据只能修正当前判断，超界时 `PLATFORM-SECURITY` 必须拒绝 effect commit 并转 sandbox/人工。

<!-- claim:SF-2026-ARXIV-2606-29604:start -->
Claim boundary：仅 `arXiv:2606.29604v1`；未证明边界定位 `https://arxiv.org/html/2606.29604v1 — §Conclusion and model-organism scope`。
<!-- claim:SF-2026-ARXIV-2606-29604:end -->
<!-- review:SF-2026-ARXIV-2606-29604:end -->

<!-- review:SF-2026-ARXIV-2606-29605:start -->
### 2606.29605 — How much of an LLM-generated clinical corpus is actually new? A production-scale measurement of content redundancy for provenance classification

**问题与现有正文缺口。** Clinical machine learning increasingly relies on training corpora generated by large language models (LLMs) rather than annotated by clinicians, and such corpora are described and reused largely on the basis of their reported scale. 逐段重读 owner 与相邻章后确认：当前章已拥有 provenance、dedup、contamination 与 typed lineage；单一归因或语料案例不自动形成新命题。

**机制、状态、控制流与取舍。** 把生成语料的 provenance、复制与跨记录冗余转成训练前数据控制状态。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 把生成语料的 provenance、复制与跨记录冗余转成训练前数据控制状态。《How much of an LLM-generated clinical corpus is actually new? A production-scale measurement of content redundancy for provenance classification》的正证据锚定 `2 Results; downstream equal-token adaptation test`；`3 Discussion` 没有建立跨 corpus、训练阶段与真实删除/重训操作的因果有效性。因此该证据只能修正当前判断，超界时 `TRAIN-DATA` 必须保留原样本、lineage 与重训对照。

<!-- claim:SF-2026-ARXIV-2606-29605:start -->
Claim boundary：仅 `arXiv:2606.29605v1`；未证明边界定位 `https://arxiv.org/html/2606.29605v1 — §3 Discussion`。
<!-- claim:SF-2026-ARXIV-2606-29605:end -->
<!-- review:SF-2026-ARXIV-2606-29605:end -->

<!-- review:SF-2026-ARXIV-2606-29623:start -->
### 2606.29623 — SCARCE: Scalable Cascade Analysis for Rare-event Characterisation via Embeddings

**问题与现有正文缺口。** Rare events govern the safety profile of modern AI systems, yet their probabilities are extremely difficult to estimate: direct Monte Carlo requires prohibitive sample budgets. 逐段重读 owner 与相邻章后确认：现有 Evaluation 正文要求 slice、校准与反例，但缺少在零失败观测下以 adaptive rare-event cascade、ruler revision 与 anytime-valid upper envelope持有风险证据。

**机制、状态、控制流与取舍。** 高风险 release 不能用普通 Monte Carlo 的零观察失败推断安全；SCARCE 类 cascade 将 rare-event region、latent ruler、停止条件与概率上界保存为验收证据。Ruler/分布假设失效时恢复更保守采样或保持 Gate Open。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** MNIST 与 Llama-Guard hidden-state jailbreak fleet 只验证经校准 ruler 的 rare-event estimate；论文明确指出 behavioral fleet 约 2,000 variants 仍不足、Mahalanobis ruler 可结构性失效，跨 corpus 必须重新校准。否则 Gate 保持 Open。

<!-- claim:SF-2026-ARXIV-2606-29623:start -->
Claim boundary：仅 `arXiv:2606.29623v1`；未证明边界定位 `https://arxiv.org/html/2606.29623v1 — §7 Conclusion, Limitations, and Extensions; E LLM Transfer Challenges`。
<!-- claim:SF-2026-ARXIV-2606-29623:end -->
<!-- review:SF-2026-ARXIV-2606-29623:end -->

<!-- review:SF-2026-ARXIV-2606-29629:start -->
### 2606.29629 — Energy-Efficient Multimodal Inference Serving with Tri-serve

**问题与现有正文缺口。** Multimodal model inference creates substantial energy demand with growing performance requirements. 逐段重读 owner 与相邻章后确认：当前章已把 routing、placement、energy/thermal、SLO 与 topology state 纳入调度控制。

**机制、状态、控制流与取舍。** 让软件 DVFS controller 持有多模态 serving 阶段、功耗与热状态。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 让软件 DVFS controller 持有多模态 serving 阶段、功耗与热状态。《Energy-Efficient Multimodal Inference Serving with Tri-serve》的正证据锚定 `II-C1 Frequency-locked Roofline Benchmarking; IV Evaluation`；`V Conclusion; evaluated Qwen-Omni/GPU-cluster boundary` 没有建立跨 topology、并发负载、thermal state 与 SLO 的调度收益。因此该证据只能修正当前判断，超界时 `INFER-SCHEDULING` 必须恢复静态 placement 与保守 SLO headroom。

<!-- claim:SF-2026-ARXIV-2606-29629:start -->
Claim boundary：仅 `arXiv:2606.29629v1`；未证明边界定位 `https://arxiv.org/pdf/2606.29629v1 — §V Conclusion; evaluated Qwen-Omni/GPU-cluster boundary`。
<!-- claim:SF-2026-ARXIV-2606-29629:end -->
<!-- review:SF-2026-ARXIV-2606-29629:end -->

<!-- review:SF-2026-ARXIV-2606-29645:start -->
### 2606.29645 — Metadata, Structure, or Strategy? A Decomposition of RAG Context Enrichment

**问题与现有正文缺口。** Retrieval-augmented generation (RAG) systems increasingly enrich retrieved passages by attaching quality metadata, structuring them into explicit records, and adopting multi-hop retrieval strategies that accumulate evidence across steps. 逐段重读 owner 与相邻章后确认：当前章已拥有 typed query plan、router、metric/index identity、evidence sufficiency 与失败回退。

**机制、状态、控制流与取舍。** 把 metadata、结构与 multi-hop strategy 分解为可单独验收的 RAG 控制变量。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 把 metadata、结构与 multi-hop strategy 分解为可单独验收的 RAG 控制变量。《Metadata, Structure, or Strategy? A Decomposition of RAG Context Enrichment》的正证据锚定 `3.2 Experimental Design; results across six benchmarks`；`6.1 Limitations` 没有建立跨 corpus、query distribution、retriever/index revision 与生成器的检索收益。因此该证据只能修正当前判断，超界时 `AGENT-RAG` 必须恢复固定、已校准的 retrieval plan。

<!-- claim:SF-2026-ARXIV-2606-29645:start -->
Claim boundary：仅 `arXiv:2606.29645v1`；未证明边界定位 `https://arxiv.org/html/2606.29645v1 — §6.1 Limitations`。
<!-- claim:SF-2026-ARXIV-2606-29645:end -->
<!-- review:SF-2026-ARXIV-2606-29645:end -->

<!-- review:SF-2026-ARXIV-2606-29646:start -->
### 2606.29646 — Fuzzing Large Language Models to Elicit Hidden Behaviours

**问题与现有正文缺口。** Sleeper agents are the canonical model organism of deception: models trained to behave normally but to emit an unsafe behaviour on a specific trigger. 逐段重读 owner 与相邻章后确认：当前章已把模型 sensor、policy/authorization 与 effect-time commit 分开，并拥有 fail-closed fallback。

**机制、状态、控制流与取舍。** 把 sleeper behavior elicitation 的 fuzzing、代理调参与 oracle 边界分开。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 把 sleeper behavior elicitation 的 fuzzing、代理调参与 oracle 边界分开。《Fuzzing Large Language Models to Elicit Hidden Behaviours》的正证据锚定 `3 Results`；`4 Discussion` 没有建立跨 threat distribution、attacker adaptation 与 effect-time authorization 的防护承诺。因此该证据只能修正当前判断，超界时 `PLATFORM-SECURITY` 必须拒绝 effect commit 并转 sandbox/人工。

<!-- claim:SF-2026-ARXIV-2606-29646:start -->
Claim boundary：仅 `arXiv:2606.29646v1`；未证明边界定位 `https://arxiv.org/html/2606.29646v1 — §4 Discussion`。
<!-- claim:SF-2026-ARXIV-2606-29646:end -->
<!-- review:SF-2026-ARXIV-2606-29646:end -->

<!-- review:SF-2026-ARXIV-2606-29648:start -->
### 2606.29648 — Hybrid Retriever Evolution for Multimodal Document Reasoning Agents

**问题与现有正文缺口。** Different retrievers, including lexical, semantic, and multimodal approaches, provide highly complementary strengths for multimodal document understanding, yet most systems combine them through fixed pipelines that cannot adapt to the demands of individual reasoning steps. 逐段重读 owner 与相邻章后确认：当前章已拥有 typed query plan、router、metric/index identity、evidence sufficiency 与失败回退。

**机制、状态、控制流与取舍。** 让 meta-agent 从失败轨迹重写多检索器编排策略。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 让 meta-agent 从失败轨迹重写多检索器编排策略。《Hybrid Retriever Evolution for Multimodal Document Reasoning Agents》的正证据锚定 `4 Experiments`；`A Limitations` 没有建立跨 corpus、query distribution、retriever/index revision 与生成器的检索收益。因此该证据只能修正当前判断，超界时 `AGENT-RAG` 必须恢复固定、已校准的 retrieval plan。

<!-- claim:SF-2026-ARXIV-2606-29648:start -->
Claim boundary：仅 `arXiv:2606.29648v1`；未证明边界定位 `https://arxiv.org/html/2606.29648v1 — §A Limitations`。
<!-- claim:SF-2026-ARXIV-2606-29648:end -->
<!-- review:SF-2026-ARXIV-2606-29648:end -->

<!-- review:SF-2026-ARXIV-2606-29649:start -->
### 2606.29649 — Resolution Thresholds in VLM Detection of Harmful ASCII Art Across Construction Modes and Languages

**问题与现有正文缺口。** Large Vision-Language Models (VLMs) are increasingly deployed as content moderation tools, yet they remain vulnerable to jailbreak attacks in which harmful text is visually encoded as ASCII art. 逐段重读 owner 与相邻章后确认：当前章已把模型 sensor、policy/authorization 与 effect-time commit 分开，并拥有 fail-closed fallback。

**机制、状态、控制流与取舍。** 把分辨率、字符构造与语言纳入 VLM moderation 威胁面。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 把分辨率、字符构造与语言纳入 VLM moderation 威胁面。《Resolution Thresholds in VLM Detection of Harmful ASCII Art Across Construction Modes and Languages》的正证据锚定 `3.2 VLM Evaluation`；`5 Discussion` 没有建立跨 threat distribution、attacker adaptation 与 effect-time authorization 的防护承诺。因此该证据只能修正当前判断，超界时 `PLATFORM-SECURITY` 必须拒绝 effect commit 并转 sandbox/人工。

<!-- claim:SF-2026-ARXIV-2606-29649:start -->
Claim boundary：仅 `arXiv:2606.29649v1`；未证明边界定位 `https://arxiv.org/html/2606.29649v1 — §5 Discussion`。
<!-- claim:SF-2026-ARXIV-2606-29649:end -->
<!-- review:SF-2026-ARXIV-2606-29649:end -->

<!-- review:SF-2026-ARXIV-2606-29652:start -->
### 2606.29652 — As We May Search

**问题与现有正文缺口。** The sensitive information in personal documents, legal files, and medical records is among the most valuable things to search, yet current retrieval-augmented generation systems still require sending content to remote servers. 逐段重读 owner 与相邻章后确认：当前章已拥有 typed query plan、router、metric/index identity、evidence sufficiency 与失败回退。

**机制、状态、控制流与取舍。** 把索引、模型与推理默认置于用户设备，并把远端服务降为可选路径。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 把索引、模型与推理默认置于用户设备，并把远端服务降为可选路径。《As We May Search》的正证据锚定 `4.1 Experimental Setup; five benchmarks and 1K-1M documents`；`4.11 Limitations` 没有建立跨 corpus、query distribution、retriever/index revision 与生成器的检索收益。因此该证据只能修正当前判断，超界时 `AGENT-RAG` 必须恢复固定、已校准的 retrieval plan。

<!-- claim:SF-2026-ARXIV-2606-29652:start -->
Claim boundary：仅 `arXiv:2606.29652v1`；未证明边界定位 `https://arxiv.org/html/2606.29652v1 — §4.11 Limitations`。
<!-- claim:SF-2026-ARXIV-2606-29652:end -->
<!-- review:SF-2026-ARXIV-2606-29652:end -->

<!-- review:SF-2026-ARXIV-2606-29654:start -->
### 2606.29654 — Budgeted Act-or-Defer Multi-Agent LLM Deliberation with Local Reliability Bounds

**问题与现有正文缺口。** Multi-agent deliberation among LLMs can improve reasoning, but deployment requires deciding when the current answer is reliable enough to act on and when it should be escalated to human review. 逐段重读 owner 与相邻章后确认：现有 Multi-Agent 正文有 verifier 与 coordination tax，却没有在部署前将 wrong-action budget 分解为校准失败、残余行动风险和 representation gap，并据 local lower bound 决定 act/defer。

**机制、状态、控制流与取舍。** 多 Agent deliberation 的 automation 权由预先声明的 wrong-action budget 和 local reliability lower bound 决定；controller 记录 act/defer 与预算消耗，低于下界即升级或拒答。校准失效时回退全 defer/人工，不用事后挑阈值美化覆盖率。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 保证依赖 local bias envelope、representation-gap bound 与 calibration split，并非 distribution-free；六个选择题 benchmark 与训练期 difficulty-normalized budget 未证明开放式任务或分布漂移。诊断失败时全 defer/人工。

<!-- claim:SF-2026-ARXIV-2606-29654:start -->
Claim boundary：仅 `arXiv:2606.29654v1`；未证明边界定位 `https://arxiv.org/html/2606.29654v1 — §7 Discussion and Limitations; H Detailed Assumption Diagnostics; N Failure-case decomposition`。
<!-- claim:SF-2026-ARXIV-2606-29654:end -->
<!-- review:SF-2026-ARXIV-2606-29654:end -->

<!-- review:SF-2026-ARXIV-2606-29657:start -->
### 2606.29657 — Safety from Honesty in a Disinterested AI Predictor

**问题与现有正文缺口。** As AI systems become more capable, training procedures that optimize for downstream outcomes risk introducing implicit agency: goal-directed behavior that designers never specified. 逐段重读 owner 与相邻章后确认：当前章已把模型 sensor、policy/authorization 与 effect-time commit 分开，并拥有 fail-closed fallback。

**机制、状态、控制流与取舍。** 把预测器训练与下游行动奖励隔离，并把 agency 留给受约束 scaffolding。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 把预测器训练与下游行动奖励隔离，并把 agency 留给受约束 scaffolding。《Safety from Honesty in a Disinterested AI Predictor》的正证据锚定 `Formal safety argument and falsifiability analysis`；`5.4.2 Falsifiability, Scope, and Requirements for a Concrete Design` 没有建立跨 threat distribution、attacker adaptation 与 effect-time authorization 的防护承诺。因此该证据只能修正当前判断，超界时 `PLATFORM-SECURITY` 必须拒绝 effect commit 并转 sandbox/人工。

<!-- claim:SF-2026-ARXIV-2606-29657:start -->
Claim boundary：仅 `arXiv:2606.29657v1`；未证明边界定位 `https://arxiv.org/html/2606.29657v1 — §5.4.2 Falsifiability, Scope, and Requirements for a Concrete Design`。
<!-- claim:SF-2026-ARXIV-2606-29657:end -->
<!-- review:SF-2026-ARXIV-2606-29657:end -->

<!-- review:SF-2026-ARXIV-2606-29661:start -->
### 2606.29661 — Diversity is the Strength of the AI Crowd

**问题与现有正文缺口。** Top AI forecasting systems are approaching superforecaster-level accuracy on future world events, but still rely primarily on off-the-shelf LLMs combined with forecasting-specific context gathering and scaffolding. 逐段重读 owner 与相邻章后确认：当前章已拥有 topology、message/state、aggregation、delegation、independent verification 与 coordination tax。

**机制、状态、控制流与取舍。** 让 ensemble controller 同时优化预测质量与跨模型错误多样性。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 让 ensemble controller 同时优化预测质量与跨模型错误多样性。《Diversity is the Strength of the AI Crowd》的正证据锚定 `5 Results`；`6 Discussion` 没有建立跨 agent population、message protocol、error correlation 与 coordination load 的聚合收益。因此该证据只能修正当前判断，超界时 `AGENT-MULTI-AGENT` 必须恢复单 Agent/串行协调与人工仲裁。

<!-- claim:SF-2026-ARXIV-2606-29661:start -->
Claim boundary：仅 `arXiv:2606.29661v1`；未证明边界定位 `https://arxiv.org/html/2606.29661v1 — §6 Discussion`。
<!-- claim:SF-2026-ARXIV-2606-29661:end -->
<!-- review:SF-2026-ARXIV-2606-29661:end -->

<!-- review:SF-2026-ARXIV-2606-29679:start -->
### 2606.29679 — Learning as Observable Matrix Dynamics: Diffusive Relaxations versus Phase Transitions

**问题与现有正文缺口。** Observable Matrix Dynamics (OMD) is a diagnostic framework that probes the dynamics of high-dimensional internal representations of inputs by a neural network via a fixed-size $N \times N$ distance matrix $M(t)$ on a held set of $N$ inputs. 逐段重读 owner 与相邻章后确认：当前章已区分 observe-only sensor、SLO authority、drift 与告警副作用。

**机制、状态、控制流与取舍。** 用表示距离矩阵轨迹监测训练相变，而非只观察标量 loss。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 用表示距离矩阵轨迹监测训练相变，而非只观察标量 loss。《Learning as Observable Matrix Dynamics: Diffusive Relaxations versus Phase Transitions》的正证据锚定 `4 Experiments`；`6 Discussion` 没有建立跨 workload、signal drift 与告警副作用的生产检测率。因此该证据只能修正当前判断，超界时 `PLATFORM-MONITORING` 必须只保留 observe-only 告警并请求重新校准。

<!-- claim:SF-2026-ARXIV-2606-29679:start -->
Claim boundary：仅 `arXiv:2606.29679v1`；未证明边界定位 `https://arxiv.org/html/2606.29679v1 — §6 Discussion`。
<!-- claim:SF-2026-ARXIV-2606-29679:end -->
<!-- review:SF-2026-ARXIV-2606-29679:end -->

<!-- review:SF-2026-ARXIV-2606-30686:start -->
### 2606.30686 — Position: Vision-Language-Action Models Cannot Be Verified to Perform Physical Reasoning

**问题与现有正文缺口。** Vision-Language-Action (VLA) systems, built on pretrained vision-language models (VLMs), have shown rapidly improving performance on robot manipulation benchmarks. 逐段重读 owner 与相邻章后确认：当前章已把 dataset/model/evaluator/metric/release 分权，并要求 slice、校准、污染与反例证据。

**机制、状态、控制流与取舍。** 把 VLA 的语义匹配与物理动作泛化拆成可识别因果评测。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 把 VLA 的语义匹配与物理动作泛化拆成可识别因果评测。《Position: Vision-Language-Action Models Cannot Be Verified to Perform Physical Reasoning》的正证据锚定 `3.2 Three Levels of Non-Identifiability in Current Evaluation`；`Conclusion and proposed controlled-variation scope` 没有建立跨 dataset/model/evaluator revision 的 release acceptance 或生产 SLO。因此该证据只能修正当前判断，超界时 `PLATFORM-EVALUATION-SYSTEM` 必须保持 release Gate Open 并恢复完整分层评测。

<!-- claim:SF-2026-ARXIV-2606-30686:start -->
Claim boundary：仅 `arXiv:2606.30686v1`；未证明边界定位 `https://arxiv.org/html/2606.30686v1 — §Conclusion and proposed controlled-variation scope`。
<!-- claim:SF-2026-ARXIV-2606-30686:end -->
<!-- review:SF-2026-ARXIV-2606-30686:end -->

<!-- review:SF-2026-ARXIV-2606-30689:start -->
### 2606.30689 — Citation Discipline in Spec-Driven Development: A Cross-Model Empirical Study of Output Determinism and Automated Hallucination Detection in LLM-Generated Code

**问题与现有正文缺口。** Spec-Driven Development (SDD) frameworks guide Large Language Model (LLM)-powered code generation through formal specifications, yet they differ fundamentally in how they enforce traceability between requirements and generated code. 逐段重读 owner 与相邻章后确认：当前章已拥有 versioned state machine、DAG、evaluator-driven search、replay 与 compensation。

**机制、状态、控制流与取舍。** 把逐行需求 citation 变成可自动检测幻觉的 provenance 合同。 该路径新增论文所述的校准/状态维护或执行成本，不能由 headline result 抵消。

**Failure、fallback 与共存。** 把逐行需求 citation 变成可自动检测幻觉的 provenance 合同。《Citation Discipline in Spec-Driven Development: A Cross-Model Empirical Study of Output Determinism and Automated Hallucination Detection in LLM-Generated Code》的正证据锚定 `4 Experimental Design; cross-model results`；`7 Discussion` 没有建立跨 environment、tool semantics、checkpoint 与 compensation path 的可复算性。因此该证据只能修正当前判断，超界时 `AGENT-WORKFLOW` 必须停在可恢复 checkpoint 并执行 compensation。

<!-- claim:SF-2026-ARXIV-2606-30689:start -->
Claim boundary：仅 `arXiv:2606.30689v1`；未证明边界定位 `https://arxiv.org/html/2606.30689v1 — §7 Discussion`。
<!-- claim:SF-2026-ARXIV-2606-30689:end -->
<!-- review:SF-2026-ARXIV-2606-30689:end -->

## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-29142 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-29150 | Discrete flow models have recently shown promising performance on few-step text generation; however, when naively applied to structured reasoning tasks such as Sudoku and Zebra puzzles, they converge confidently to incorrect answers (solving only $\sim$36% of Sudoku puzzles). | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | These changes substantially improve the base model's efficiency, letting it reach $99.2\%$ on Sudoku in just $7$ forward passes, over $8\times$ fewer than the strongest matched masked-diffusion baseline we compare needs for the same accuracy. |
| SF-2026-ARXIV-2606-29151 | SemBench: Movie (10 queries), Wildlife (11), MMQA (10), Cars (14), and E-Commerce semantic-query scenarios | GPT-4.1 planner; GPT-4.1-mini adaptive bypass; gpt-audio-mini; heterogeneous symbolic, specialized, general-purpose, and composite backends | 2 x NVIDIA RTX 3090 24GB; 64-core Intel Xeon; 512GB RAM; Azure Foundry APIs | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | 24-hour per-query timeout | Quality in [0,1] via relative error, F1, Spearman rho, or ARI by scenario; latency in seconds; cost in USD; three repeats with geometric mean |
| SF-2026-ARXIV-2606-29158 | FineWeb-100B; 5B-100B training tokens in 2.5B-token increments; held-out 707M model tested at 50B-100B tokens | GPT-2-style dense models from 22M to 707M parameters; AdamW and AdamH experiments | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | 0.52M tokens per batch | Not Disclosed | Not Disclosed | Validation loss, out-of-distribution R-squared, and extra compute ratio under compute-constrained extrapolation |
| SF-2026-ARXIV-2606-29159 | Offline root-cause-analysis (RCA) benchmarks commonly rank methods by a single pooled top-1 accuracy across multiple subsystems, and engineers often read the pooled winner as a recommendation for their own subsystem. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | To keep pairwise comparisons on identical cases, the main analysis retains four methods or comparators with complete coverage: BARO, a CD-1min adapter, max-$/Z/$, and per-service alert-count. |
| SF-2026-ARXIV-2606-29171 | 11,000 refusal-policy prompts across harmful, harmless, harmful-natural, harmful-balanced, and three 2,000-prompt consistency splits; 200 SFT training pairs attributed | Llama-3.2-3B-Instruct; sparse autoencoder with k=40 active features per token; GPT-5.4-mini feature labels | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Two independent researchers; mean feature-label score 0.76/1 and Cohen kappa 0.648 on n=25; Ridge fidelity and attribution-stability analyses |
| SF-2026-ARXIV-2606-29176 | On a language model trained past the point of fit, DDCAdam resists the over-training collapse AdamW falls into, holding a validation-train loss gap of 0.67 against 5.88, and reads the dead-direction rate in 32 of 65 layer-by-observable cells where AdamW reads it in 7. | grok | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-29178 | Under a controlled noisy-write stress (75% synthetic distractors), unbounded memory and FIFO-K50 degrade on Precision@5 (20.2% to 12.4% and 15.8% to 3.8%) while TraceRetain-CEM is essentially unchanged (16.9% to 16.6%) and preserves 97/100 task success. | gpt-5-mini | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | The mechanism: unbounded memory has the highest mean similarity (0.87) but lowest precision, indicating failed distractors close to the query in embedding space. |
| SF-2026-ARXIV-2606-29182 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-29184 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-29193 | We address this gap by introducing two large-scale datasets (AIOps2025 and RCA100) under a reasoning-process evaluation paradigm that assesses agentic diagnostic capability along three dimensions: Localization (where the fault occurs), Identification (what type of fault it is), and Reason (whether the reasoning trace is grounded in relevant evidence). | Not Disclosed | A100 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Beyond scale and coverage, the datasets have been carefully labelled by domain experts and validated through large-scale competitions, supporting more than 6,000 participating teams. |
| SF-2026-ARXIV-2606-29194 | We run Agora for 100 rounds on CSI 1000 and evaluate on a 91-day 2026 holdout sealed from all LLM inputs. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-29196 | 203 Jordine evaluation/deployment prompt pairs for probe construction; SAD stages_oversight split for evaluation; ROUGE-L and perplexity-ratio contamination diagnostics | 11 open-weight checkpoints: Qwen2.5 0.5B/1.5B/3B/7B/14B/32B, Gemma2 2B/9B/27B, Llama3.2 1B/3B | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Layer-wise probe AUROC, peak relative layer depth, black-box behavioral classification, ROUGE-L completion, and perplexity-ratio diagnostics |
| SF-2026-ARXIV-2606-29207 | On real GPU testbeds (intra-node A6000 and cross-node H100), under a dynamic long-context agentic workload serving Llama-3.1-8B, KernelFlume sustains flat p99 TPOTs of ~74 ms on A6000 and ~34 ms on H100, while lowering cost per million output tokens by up to 32% and 61%, respectively, relative to full-instance elastic scaling with ServerlessLLM, a state-of-the-art instance-startup method. | Llama-3.1-8B | H100 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-29215 | Empirically, MBD-LLaDA2-Mini increases average Tokens Per Forward pass (TPF) from 3.47 to 6.19 and improves average accuracy from 79.95% to 81.03%; when combined with DMax, MBD-LLaDA2-Mini-DMax reaches an average TPF of 9.34 with only a 1.02% accuracy drop on math and code benchmarks. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Empirically, MBD-LLaDA2-Mini increases average Tokens Per Forward pass (TPF) from 3.47 to 6.19 and improves average accuracy from 79.95% to 81.03%; when combined with DMax, MBD-LLaDA2-Mini-DMax reaches an average TPF of 9.34 with only a 1.02% accuracy drop on math and code benchmarks. |
| SF-2026-ARXIV-2606-29222 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-29223 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-29225 | On tau^2-BENCH airline across three vendors (GPT-5.4, Claude Sonnet 4.6, Gemini 2.5 Pro) with four trials per setting, POLICYGUARD improves PASS4 by +12.0 / +6.0 / +12.0 pp. | GPT-5.4 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-29228 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-29237 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-29238 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-29239 | We conduct systematic experiments on six mainstream LLMs (including the LLaMA-3 and Qwen2.5-Coder) using three quantization precisions (INT8, FP4, and NF4) across three representative scenarios: vulnerable code generation, content injection, and over-refusal. | LLaMA-3 and Qwen2.5 | Not Disclosed | INT8 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-29251 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-29270 | 1,754 questions over six benchmarks; three heterogeneous agents and two debate rounds; 20 random-seed trials | GPT-4o-mini, Gemini-2.0-Flash, Claude Haiku 4.5; LightGBM meta-classifier; GPT-4o semantic-audit judge at temperature 0 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Flip Precision, Net Gain, minority-truth recovery, per-dataset performance, and 20-seed stability |
| SF-2026-ARXIV-2606-29275 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-29278 | CCB fixes the semantic content of a task and varies only its depth N in {5,...,50} across three structurally distinct regimes: grounded spatial state-tracking, abstract symbolic pointer manipulation, and transitive relational inference. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Forced verbose state-tracking does not move the ceiling (McNemar p=1.000), and the mean step at which reasoning first diverges, k*, predicts within-domain accuracy better than parameter count. |
| SF-2026-ARXIV-2606-29279 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-29280 | In a six-arm ablation on the Open University Learning Analytics Dataset (N=800 students, four temporal cutoffs), at day 56 -- when the oracle designates 70.1% of students as needing no intervention -- zero-shot GPT-4o recommends action for 73%, a 43 percentage-point false-positive rate. | GPT-4o recommends action | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | The DT reaches macro-F1 0.79 (macro-recall 0.85) across all five action classes, predicting even the rare load-reduction action without collapsing, at a 0% action flip rate and sub-5 ms CPU decision latency. |
| SF-2026-ARXIV-2606-29282 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-29296 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | In every regime PASS delivers a consistent pass@1 gain over the corresponding GRPO baseline. |
| SF-2026-ARXIV-2606-29315 | To evaluate active experimentation, we introduce Interphyre, a tool-calling benchmark built on the PHYRE 2D procedural physics environment, where agents propose interventions and test hypotheses through simulation APIs. | Claude Sonnet 4.6 achieves | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Moreover, using only skills learned from easier levels and transferred without active experimentation, HExA achieves 44% success, demonstrating the reusability and generalization of its learned skills. |
| SF-2026-ARXIV-2606-29328 | Six open-domain QA benchmarks and six retrieval methods; candidate recall K=200 and selected context k=5 in the standard setup; full-Wikipedia no-gold-injection and context-budget robustness tests | Dense retrievers plus context-selection baselines including cosine top-k, MMR, DPP, BGE-Reranker, SMART-RAG, and AdaGReS; multiple sub-query generators | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Exact Match, Recall@200, demand-dimension coverage, context redundancy, ablations, and stability across context budgets and sub-query generators |
| SF-2026-ARXIV-2606-29337 | We summarize our submission to Sub-Challenge 1: W4A4 Quantization for Inference (HiF4 / MXFP4) of the ICME 2026 Low-Bit-width Large-Model Quantization Challenge. | Not Disclosed | Not Disclosed | W4A4 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Calibration on representative OpenS2V-5M batches identifies heavy-tailed activation channels; smoothing rebalances dynamic range before W4A4 rounding; and a dual-branch GEMM preserves outlier columns in higher precision while the bulk of channels use strict W4A4. |
| SF-2026-ARXIV-2606-29340 | Not Disclosed | Qwen | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-29350 | In the Video Question Answering task on the mainstream VLM, Qwen2.5-VL, ST-Merge achieves a 2$\times$ inference speedup with only a tiny 1\% loss in precision. | Qwen | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | When deployed on the $π_{0.5}$ VLA policy, ST-Merge achieves an 8.3$\times$ speedup at 1024 $\times$ 1024 resolution and matches the baseline success rate at this high-resolution setting. |
| SF-2026-ARXIV-2606-29354 | Across challenging benchmarks, CLSR reduces latency-oriented generated token completion by $3\sim 6\times$ compared to standard CoT while maintaining accuracy. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Across challenging benchmarks, CLSR reduces latency-oriented generated token completion by $3\sim 6\times$ compared to standard CoT while maintaining accuracy. |
| SF-2026-ARXIV-2606-29366 | Experimental results on 29 production evaluation batches from JD.com show that the best single OR formulation improves allocation accuracy by 3.4 percentage points over the incumbent approach, while the full ORLA framework achieves a 4.5 percentage-point overall improvement and improves allocation accuracy in 26 of the 29 evaluation batches. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Experimental results on 29 production evaluation batches from JD.com show that the best single OR formulation improves allocation accuracy by 3.4 percentage points over the incumbent approach, while the full ORLA framework achieves a 4.5 percentage-point overall improvement and improves allocation accuracy in 26 of the 29 evaluation batches. |
| SF-2026-ARXIV-2606-29377 | We propose D2R-RAG (Diagnose-to-Repair RAG), a model-agnostic and resource-aware framework that combines lightweight failure diagnosis with adaptive repair. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Experiments on FEVER and HotpotQA show that D2R-RAG improves reliability over recent baselines and achieves better accuracy--efficiency trade-offs across multiple compute budgets. |
| SF-2026-ARXIV-2606-29399 | On a 200-question benchmark over NuScale Final Safety Analysis Report (FSAR) documents, the system reaches 81.5% accuracy with a RAGAS Faithfulness of 0.93. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Edge inference adds 2.8x cost without raising accuracy; we retain it as a traceability module. |
| SF-2026-ARXIV-2606-29403 | On eight regression and classification benchmarks, SO-SCP reduces the weighted regional coverage gap on $7/8$ datasets (mean paired change $-7.1\%$) for a mean prediction-set size increase of $6.2\%$, with negligible overhead on the largest six datasets; SO-CQR yields smaller gains, since quantile regression already absorbs much of the heterogeneity. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | On eight regression and classification benchmarks, SO-SCP reduces the weighted regional coverage gap on $7/8$ datasets (mean paired change $-7.1\%$) for a mean prediction-set size increase of $6.2\%$, with negligible overhead on the largest six datasets; SO-CQR yields smaller gains, since quantile regression already absorbs much of the heterogeneity. |
| SF-2026-ARXIV-2606-29424 | Extensive experiments demonstrate that EntroRouter retains 98.3% of the strongest expert's accuracy while reducing computational costs by 48.25%. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Extensive experiments demonstrate that EntroRouter retains 98.3% of the strongest expert's accuracy while reducing computational costs by 48.25%. |
| SF-2026-ARXIV-2606-29425 | Extensive experiments on multimodal benchmarks demonstrate that MoD outperforms both single-model baselines and conventional multi-agent systems, achieving superior accuracy with 3.7x lower latency and 87% reduction in token consumption.The source code can be accessed at https://github.com/YongLD/MoD. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Extensive experiments on multimodal benchmarks demonstrate that MoD outperforms both single-model baselines and conventional multi-agent systems, achieving superior accuracy with 3.7x lower latency and 87% reduction in token consumption.The source code can be accessed at https://github.com/YongLD/MoD. |
| SF-2026-ARXIV-2606-29441 | We evaluate five defense paradigms (no defense, static steering, CAST, AlphaSteer, probe-gated) across seven instruction-tuned models (7-31B) and five attack types (GCG, AutoDAN, DeepInception, prefilling, intent laundering). | Llama Guard 3. Cross | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Composing the response-halt with AlphaSteer's null-space steering gives an orthogonal split (the halt catches prefilling, AlphaSteer catches semantic attacks), reaching defense success 0.983 on Mistral and 0.994 on Llama and dominating both components. |
| SF-2026-ARXIV-2606-29445 | Experimental results demonstrate that TASKER achieves significant performance improvements on both VideoQA and video-guided agentic task benchmarks, outperforming the best baseline by 2.0% on the EgoSchema fullset and 1.8% on the NExT-QA dataset, respectively. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-29472 | DynaCU-Bench: 100 dynamic browser tasks plus 50 static-control tasks, including spoken-content tasks | Computer-use models from 7B to frontier scale; Gemini 3 Flash component ablation | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Task success against periodic-screenshot baselines; per-model ablations of keyframes, audio transcription, and persistent visual narration |
| SF-2026-ARXIV-2606-29476 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-29481 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-29490 | Not Disclosed | Gemma 3 and 4 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-29493 | We audit five widely used Lean theorem-proving benchmarks and their forks, using corpus-scale static checkers to surface 4,833 findings, including 398 mechanically certified issues such as counterexamples, vacuous theorems, and unsound axioms. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-29501 | Concretely, we pretrain a multi-view interactive base diffusion world model, A2World, on large-scale robot manipulation data with real action annotations. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-29502 | Experiments on agentic tasks, including ALFWorld, WebShop, and Search-QA, show that UCOB outperforms skill-free RL, skill-memory baselines, and self-distillation methods across model scales, with up to 23.5 and 18.0 point gains over SOTA baselines on ALFWorld and WebShop. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-29506 | We build an unsupervised normality model from the all-normal training frames of one dataset, using frozen off-the-shelf embeddings (CLIP, DINOv2, ResNet-50, EfficientNet-B0) and a nearest-neighbour distance, and score the test frames of the same and of other datasets. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | The strongest backbone makes this worse, not better: DINOv2 has the best same-dataset AUC (up to 0.901 on Ped2) and the largest cross-dataset drop. |
| SF-2026-ARXIV-2606-29520 | We evaluate 11 proprietary and open-weight models in zero-shot and five-shot settings. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-29522 | Q8 and D8 eight-state transition tasks; n=400 held-out discriminating items per metric per split; n=600 per layer for decodability | Qwen2.5-Coder-7B primary; Mistral-7B-v0.3 replication; LoRA rank 16 and alpha 32 | Not Disclosed | Not Disclosed | Maximum sequence length 256 tokens | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Edited-state agreement, move-specific and conflicting-continuation selectivity, circuit localization, exact-prefix coverage, and 95% item-level bootstrap intervals |
| SF-2026-ARXIV-2606-29526 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-29532 | This dynamic routing proves decisive: it outperforms adaptive block join (ABJ) by 20-33 F1 points across all datasets while consuming fewer tokens on two of the three, and achieves higher F1 scores than featurized-decomposition join (FDJ) at one to two orders of magnitude lower token cost. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | This dynamic routing proves decisive: it outperforms adaptive block join (ABJ) by 20-33 F1 points across all datasets while consuming fewer tokens on two of the three, and achieves higher F1 scores than featurized-decomposition join (FDJ) at one to two orders of magnitude lower token cost. |
| SF-2026-ARXIV-2606-29537 | We introduce OSWorld 2.0, a benchmark of 108 long-horizon computer-use workflows across everyday and professional tasks, designed to capture complex and challenging real-world phenomena. | Claude Opus 4.7 using | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | OSWorld 2.0 targets challenge phenomena that are common in real workflows yet underrepresented in prior benchmarks, spanning interaction-design challenges such as streaming interaction and dynamic environments, as well as agent-pattern challenges such as cross-source reasoning, implicit-state inference, and visual-spatial precision. |
| SF-2026-ARXIV-2606-29538 | Across seven practical authoring domains, RESOURCE2SKILL improves average overall score by +11.9 percentage points over no-skill agents and outperforms strong harness baselines in 26 of 28 main-aggregate model-domain cells. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-29541 | A 5-seed re-evaluation shows partial alignment between learned conventions and designer-specified priors while revealing where small-n noise can manufacture apparent strategic divergence. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-29544 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-29554 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-29563 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-29565 | Stateful streaming and tool-calling session traces; measured prefill, entry decode, fast path, confidence-gate precision, and cross-request hit rate | 70B-class target model; 8B BF16 capability-control model | Single NVIDIA H100 (tensor parallelism 1) | 4-bit target model; BF16 8B control | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Measured prefill slope 0.843 ms/token; fast-path latency, decode latency, selective-prediction risk-coverage, hit rate, and closed-form net benefit |
| SF-2026-ARXIV-2606-29567 | Evaluations on a 1,124-query corpus demonstrate that the cascade reliably detects PII, achieving an overall F1 score of 98.87%. | BERT | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Evaluations on a 1,124-query corpus demonstrate that the cascade reliably detects PII, achieving an overall F1 score of 98.87%. |
| SF-2026-ARXIV-2606-29571 | 19 parameter-free metrics x 19 encoders x seven datasets: STS-B, SICK-R, STS16, Quora, PAWS, SNLI, and MultiNLI | 19 encoders from all-MiniLM and BERT/GPT-2 through E5-Mistral-7B, SFR-Embedding-Mistral, Qwen2.5-7B, and Mistral-7B | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Spearman correlation on all datasets; ROC-AUC and PR-AUC on binary-label datasets; calibration MSE/ECE; Wilcoxon, Mann-Whitney, bootstrap, and leave-one-out tests |
| SF-2026-ARXIV-2606-29573 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-29580 | We present MAM-AI, a medical question-answering assistant for nurse-midwives in Zanzibar that runs entirely on a commodity Android device: a question is embedded (EmbeddingGemma, 300M) and matched against a curated corpus of 87 guideline documents (63,650 passages), then answered with citations by a 4B int4 generator (Gemma 4 E4B), fully offline, with no query leaving the device. | Gemma | commodity Android device | int4 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | The small generator is what remains in doubt: adding retrieved context does not improve its answers, and at 4B it cannot be both helpful and safe at once -- of two same-size candidates, the more helpful one commits genuine dangerous errors, so we deploy the other, which is about twice as faithful to its sources (as faithful as a frontier model), and recover its helpfulness with a redesigned prompt that cuts deflection from 33% to 3%. |
| SF-2026-ARXIV-2606-29581 | 200 AdvBench harmful prompts plus 200 XSTest benign prompts; five independent samples per prompt; 161 evaluated model-precision-temperature configurations (~322,000 responses) | Llama-3.1-8B-Instruct; Llama-3.2-3B-Instruct; Qwen3-4B; Qwen3-8B; Mistral-7B-Instruct-v0.3; OLMo-2-7B-Instruct; Granite-3.1-2B-Instruct; Granite-3.1-8B-Instruct; SmolLM3-3B | 2 x NVIDIA RTX 6000 Pro 96GB workstation; vLLM v0.20.0 with enforce_eager=True | FP16, GPTQ INT8, and AWQ INT4 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Six-judge safety ensemble; refusal rate, attack success rate, Safety Stability Index, Decision Flip Rate, over-refusal, and Compound Degradation Index |
| SF-2026-ARXIV-2606-29592 | We introduce STEMGym, an open-source Gymnasium benchmark of 15 physics-simulated STEM worlds spanning five materials, three difficulty levels, and four characterisation tasks, scored by the Dose-Efficiency Curve area (DEC-AUC), a single scalar capturing the information-vs-dose Pareto frontier. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Across 33 agent configurations under realistic dose budgets, the dominant determinant of dose efficiency is the analyst (perception) pipeline, not the navigator: pairing a trained CNN analyst with naïve raster scanning raises DEC-AUC by 5.5x over a CNN-free raster baseline (0.287 vs.\ 0.052), while substituting Bayesian or adaptive finite-state-machine navigation for raster yields no statistically significant further gain. |
| SF-2026-ARXIV-2606-29601 | Thirteen Langshaw protocol examples; liveness and safety verification averaged over 10 runs | Not Disclosed | ASUS Zenbook S13; AMD Ryzen 7 6800U; 16GB LPDDR5; Linux | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Tableau nodes, branches, verification time in milliseconds, safety verdict, and liveness verdict |
| SF-2026-ARXIV-2606-29602 | Not Disclosed | DeepSeek | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-29604 | For instance, CPE performs similarly to matched-wall-clock-time GRPO on the Countdown task for Qwen3-8B (85% vs 87%), demonstrating that CPE can efficiently elicit complex multi-token behaviors. | Qwen | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-29605 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-29623 | MNIST misclassification with 1,000,000 perturbations per seed; PAIR-style and GCG-style LLM jailbreak corpora with 20,000 and 200,000-sample runs | Llama-Guard-3-8B hidden states for LLM jailbreak estimation | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Mean absolute error, mean relative error, bootstrap relative half-width, GCG transfer error, ruler-ranking Spearman rho, and anytime-valid upper envelope |
| SF-2026-ARXIV-2606-29629 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | We show that Tri-serve achieves 22% energy efficiency improvement with no latency or throughput impacts. |
| SF-2026-ARXIV-2606-29645 | We isolate each factor in a controlled experiment across six benchmarks, four models from three families, and five enrichment levels, totaling over 24,000 evaluated responses. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | When metadata and retrieval strategy are aligned with model capabilities, a smaller model outperforms a frontier model by 19 F1 points. |
| SF-2026-ARXIV-2606-29646 | On 6 backdoored models (7B-13B) we compare both forms of fuzzing head-to-head against temperature-sampling baselines. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-29648 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-29649 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-29652 | This paper makes four contributions: (1) a framework organizing retrieval architectures along three dimensions: privacy and control, capability, and accessibility, (2) experiments on consumer hardware across five benchmarks, scaling from 1K to 1M documents with dense retrieval, BM25, and hybrid fusion. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Dense retrieval keeps over 91% nDCG@10 up to 100K documents, with approximate HNSW indexes extending this to 1M with only 2% quality loss; a 7B local language model reaches within 4 points of a cloud baseline on answer quality, (3) competing perspectives for and against local-first IR, informed by experimental evidence, and (4) a research agenda identifying open problems. |
| SF-2026-ARXIV-2606-29654 | Six multiple-choice benchmarks: MMLU-Pro n=8,312; LogiQA n=8,678; ARC-Challenge n=2,590; BBH n=2,395; MuSR n=756; GPQA n=546 | N LLM agents debating for at most T rounds; exact agent-model identities are in Appendix O reproducibility details | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Pre-declared wrong-action budget beta, evaluated as normalized budget usage WA/beta | Wrong actions, normalized budget usage, automation rate, acted-on accuracy, local-reliability diagnostics, and nine-baseline comparison |
| SF-2026-ARXIV-2606-29657 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-29661 | Instead, the strongest ensembles combine accurate but diverse forecasters, with models such as \model{Grok 4} contributing disproportionately because their predictions are less correlated with other frontier LLMs. | Grok 4 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-29679 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-30686 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-30689 | Our pre-registered analysis reveals a consistent, cross-model replicated trade-off: the uncited condition produces significantly higher determinism than the cited condition (Claude: $d=-0.76$, $p=0.003$; GLM: $d=-0.72$, $p&lt;0.001$), while only the cited condition enables automated hallucination detection (TDR: Claude 86.4%, GLM 88.0%, vs 0% for all alternatives, FPR=0% across both studies). | Claude Sonnet 4.6 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-29142 | score_7_9 | not_selected | — | — | 未入选长叙事：把受监管金融 Agent 的模型、工具、审计证据与人工授权绑定为部署控制面。《Agent Security Meets Regulatory Reality -- A Practitioner Systematization of Autonomous-Agent Threats and Controls in Regulated Financial Systems》的正证据锚定 `IV Architectural Patterns Observed in Production; V Negative Results and Open Problems`；`V Negative Results and Open Problems; VI Generalization Beyond Finance` 没有建立跨 threat distribution、attacker adaptation 与 effect-time authorization 的防护承诺。因此该证据只能修正当前判断，超界时 `PLATFORM-SECURITY` 必须拒绝 effect commit 并转 sandbox/人工。 | analysis-decision:SF-2026-ARXIV-2606-29142 |
| SF-2026-ARXIV-2606-29150 | score_7_9 | not_selected | — | — | 未入选长叙事：把 flow reasoning 的中间状态、自验证与 test-time compute 变成推理时控制路径。《Flow Reasoning Models: Scaling Reasoning Through Iterative Self-Refinement》的正证据锚定 `4 Experiments; G Experimental setup and hyperparameters`；`6 Discussion; B Test-time scaling: coverage, selection, and sampling-step baselines` 没有建立跨 model、request shape、quality target 与 serving engine 的延迟-质量合同。因此该证据只能修正当前判断，超界时 `INFER-DECODE` 必须恢复已验证的普通 decode/refinement path。 | analysis-decision:SF-2026-ARXIV-2606-29150 |
| SF-2026-ARXIV-2606-29151 | score_7_9; potential_books_delta | selected | DA-20260629-2606-29151 | — | 入选：只证明 SemBench 上 intent-specific operator DAG 与异构 backend 的 quality/latency/cost 计划选择；未证明跨 operator 的联合最优、teacher-noise 之外的 label shift，或 Azure/API 与本地模型间可移植性。失配时固定到已校准 retrieval plan。 | analysis:DA-20260629-2606-29151 |
| SF-2026-ARXIV-2606-29158 | score_7_9; potential_books_delta | not_selected | — | — | 未入选长叙事：只覆盖 GPT-2-style 22M-707M、FineWeb 5B-100B tokens、WSD 与 AdamW/AdamH；论文明确显示 log-linear LR 仅局部成立，不能外推到其他架构、optimizer 或更大规模。超界时重新 sweep 邻近尺度。 | analysis-decision:SF-2026-ARXIV-2606-29158 |
| SF-2026-ARXIV-2606-29159 | score_7_9 | not_selected | — | — | 未入选长叙事：揭示 pooled leaderboard 会掩盖 RCA 子任务差异，改变评测聚合合同。《Pooled Leaderboards Hide System-Specific Winners: A Reporting-Protocol Audit of Offline Root-Cause Analysis Benchmarks》的正证据锚定 `Benchmark validity and leaderboard instability in ML; system-specific results`；`6 Discussion, Limitations, and Recommendations` 没有建立跨 dataset/model/evaluator revision 的 release acceptance 或生产 SLO。因此该证据只能修正当前判断，超界时 `PLATFORM-EVALUATION-SYSTEM` 必须保持 release Gate Open 并恢复完整分层评测。 | analysis-decision:SF-2026-ARXIV-2606-29159 |
| SF-2026-ARXIV-2606-29171 | score_7_9; potential_books_delta | not_selected | — | — | 未入选长叙事：只在 Llama-3.2-3B-Instruct refusal proxy、特定 SAE 与 200 个 SFT pair 上验证一阶符号归因；feature label、Ridge fidelity 与 first-order approximation 不等于真实删除/重训因果。保留原样本与重训对照。 | analysis-decision:SF-2026-ARXIV-2606-29171 |
| SF-2026-ARXIV-2606-29176 | score_7_9 | not_selected | — | — | 未入选长叙事：改变优化器更新的去偏与稳定性路径，并要求按训练阶段校准。《Dead-Direction Conditioners: Gauge-Equivariant Preconditioning for Deep Networks》的正证据锚定 `5 Experiments; 5.1 Reading the rate at language-model scale`；`5.10 Scope and limitations` 没有建立跨 architecture、optimizer、token budget 与更大训练尺度的可迁移性。因此该证据只能修正当前判断，超界时 `TRAIN-PRETRAINING` 必须恢复邻近规模 sweep 与已验证 schedule。 | analysis-decision:SF-2026-ARXIV-2606-29176 |
| SF-2026-ARXIV-2606-29178 | score_7_9 | not_selected | — | — | 未入选长叙事：把长期记忆的写入、保留与遗忘门控变成显式持久状态迁移。《Selective Memory Retention for Long-Horizon LLM Agents》的正证据锚定 `4 Experiments`；`6 Discussion and Limitations` 没有建立跨 workload、write policy、retention horizon 与 provenance shift 的记忆收益。因此该证据只能修正当前判断，超界时 `AGENT-MEMORY` 必须拒绝写入并保留旧 memory revision。 | analysis-decision:SF-2026-ARXIV-2606-29178 |
| SF-2026-ARXIV-2606-29182 | score_7_9 | not_selected | — | — | 未入选长叙事：让科学发现 Agent 的信念状态、实验动作与反证更新形成可追踪闭环。《Evidence-Informed LLM Beliefs for Continual Scientific Discovery》的正证据锚定 `3.1.2 Evaluation: Reducing Surprisal Under Non-Stationary Beliefs`；`6 Limitations` 没有建立跨 environment、tool semantics、checkpoint 与 compensation path 的可复算性。因此该证据只能修正当前判断，超界时 `AGENT-WORKFLOW` 必须停在可恢复 checkpoint 并执行 compensation。 | analysis-decision:SF-2026-ARXIV-2606-29182 |
| SF-2026-ARXIV-2606-29184 | score_7_9 | not_selected | — | — | 未入选长叙事：把适配器秩分配与层级预算绑定为可动态选择的训练状态。《BaRA: Bayesian Adaptive Rank Allocation for Parameter-Efficient Fine-Tuning》的正证据锚定 `VI Experiments`；`III-C Limitations of Bayesian LoRA Methods` 没有建立跨 backbone、target module、rank budget 与 merge/serve path 的稳定性。因此该证据只能修正当前判断，超界时 `TRAIN-LORA` 必须恢复固定 rank/target-module adapter。 | analysis-decision:SF-2026-ARXIV-2606-29184 |
| SF-2026-ARXIV-2606-29193 | score_7_9 | not_selected | — | — | 未入选长叙事：把微服务 Agent 的任务、环境、副作用和故障恢复纳入发布评测。《A Multi-Dataset Benchmark for Evaluating LLM Agents in Microservice Failure Diagnosis》的正证据锚定 `4 Evaluation; 4.4 Evaluation Metric`；`6 Discussion` 没有建立跨 dataset/model/evaluator revision 的 release acceptance 或生产 SLO。因此该证据只能修正当前判断，超界时 `PLATFORM-EVALUATION-SYSTEM` 必须保持 release Gate Open 并恢复完整分层评测。 | analysis-decision:SF-2026-ARXIV-2606-29193 |
| SF-2026-ARXIV-2606-29194 | score_7_9 | not_selected | — | — | 未入选长叙事：把多 Agent 搜索的共享状态、隔离边界与合并控制显式化。《AI Trading's Alpha Singularity: Emergent Market Reasoning through Agent-to-Agent Self-Evolution》的正证据锚定 `Statistical inference and out-of-sample evaluation`；`6 Discussion` 没有建立跨 agent population、message protocol、error correlation 与 coordination load 的聚合收益。因此该证据只能修正当前判断，超界时 `AGENT-MULTI-AGENT` 必须恢复单 Agent/串行协调与人工仲裁。 | analysis-decision:SF-2026-ARXIV-2606-29194 |
| SF-2026-ARXIV-2606-29196 | score_7_9; potential_books_delta | not_selected | — | — | 未入选长叙事：SAD 上的线性可恢复性只是一种 operational evaluation-awareness signal；white-box AUROC 与黑盒行为会分离，且 Qwen/Gemma 的深度迁移不构成跨 family scaling law。异常只触发额外 held-out evaluation，不授予直接拒绝权。 | analysis-decision:SF-2026-ARXIV-2606-29196 |
| SF-2026-ARXIV-2606-29207 | score_7_9 | not_selected | — | — | 未入选长叙事：把 kernel 生成、校验、选择与回退组成可执行的推理内核控制流。《KernelFlume: Elastic Core-Attention Scaling for Agentic Long-Context Decoding》的正证据锚定 `6 Evaluation`；`2.4 Limitations of Existing Elastic Scaling` 没有建立跨 model、request shape、quality target 与 serving engine 的延迟-质量合同。因此该证据只能修正当前判断，超界时 `INFER-DECODE` 必须恢复已验证的普通 decode/refinement path。 | analysis-decision:SF-2026-ARXIV-2606-29207 |
| SF-2026-ARXIV-2606-29215 | score_7_9 | not_selected | — | — | 未入选长叙事：把 discrete diffusion 的多块并行解码、校验与质量退化边界显式化。《Multi-Block Diffusion Language Models》的正证据锚定 `4 Experiments`；`5 Conclusion and stated speed-quality scope` 没有建立跨 model、request shape、quality target 与 serving engine 的延迟-质量合同。因此该证据只能修正当前判断，超界时 `INFER-DECODE` 必须恢复已验证的普通 decode/refinement path。 | analysis-decision:SF-2026-ARXIV-2606-29215 |
| SF-2026-ARXIV-2606-29222 | score_7_9 | not_selected | — | — | 未入选长叙事：把机器人情境记忆接入感知到动作的闭环状态。《CORE Planner: Contextual-memory Oriented Reinforcement-learning in Unknown Environments for Robot Navigation》的正证据锚定 `V Experiments`；`VI Conclusion and deployment scope` 没有建立跨 embodiment、sensor、latency 与闭环干预的动作成功率。因此该证据只能修正当前判断，超界时 `MULTIMODAL-EMBODIED-VLA` 必须拒绝物理提交并交回保守 controller。 | analysis-decision:SF-2026-ARXIV-2606-29222 |
| SF-2026-ARXIV-2606-29223 | score_7_9 | not_selected | — | — | 未入选长叙事：把推理深度按样本难度分配，并保留固定深度回退。《Depth Exploration for LLM Decoding》的正证据锚定 `4 Experiment`；`E Limitations and discussion` 没有建立跨 model、request shape、quality target 与 serving engine 的延迟-质量合同。因此该证据只能修正当前判断，超界时 `INFER-DECODE` 必须恢复已验证的普通 decode/refinement path。 | analysis-decision:SF-2026-ARXIV-2606-29223 |
| SF-2026-ARXIV-2606-29225 | score_7_9 | not_selected | — | — | 未入选长叙事：把 Agent policy 判定置于工具副作用提交前并定义 fail-closed 路径。《PolicyGuard: A Dialogue-Grounded Sub-Agent Verifier for Policy Adherence in LLM Agents》的正证据锚定 `4 Experiments`；`Discussion` 没有建立跨 threat distribution、attacker adaptation 与 effect-time authorization 的防护承诺。因此该证据只能修正当前判断，超界时 `PLATFORM-SECURITY` 必须拒绝 effect commit 并转 sandbox/人工。 | analysis-decision:SF-2026-ARXIV-2606-29225 |
| SF-2026-ARXIV-2606-29228 | score_7_9 | not_selected | — | — | 未入选长叙事：揭示 DLM 评测中的表面提升与实际生成能力分离。《Understanding Evaluation Illusion in Diffusion Large Language Models》的正证据锚定 `3 Evaluation Inconsistency; 4 Experiments`；`5 Discussion; speed-quality trade-off counterevidence` 没有建立跨 dataset/model/evaluator revision 的 release acceptance 或生产 SLO。因此该证据只能修正当前判断，超界时 `PLATFORM-EVALUATION-SYSTEM` 必须保持 release Gate Open 并恢复完整分层评测。 | analysis-decision:SF-2026-ARXIV-2606-29228 |
| SF-2026-ARXIV-2606-29237 | score_7_9 | not_selected | — | — | 未入选长叙事：把运动持续性作为世界模型 rollout 的可测状态而非单帧视觉指标。《MoPe: Motion Permanence for Robust Monocular Gaussian Mapping in Dynamic Environments》的正证据锚定 `IV Experiments`；`V Limitations and Future Work` 没有建立跨 environment、observation dynamics 与 physical commit 的 rollout fidelity。因此该证据只能修正当前判断，超界时 `MULTIMODAL-WORLD-MODELS` 必须停止 imagined rollout 并请求真实 observation。 | analysis-decision:SF-2026-ARXIV-2606-29237 |
| SF-2026-ARXIV-2606-29238 | score_7_9 | not_selected | — | — | 未入选长叙事：给 GRPO 更新的稳定域与偏差来源建立理论边界。《On the Policy Gradient Foundations of Group Relative Policy Optimization: Credit Assignment, Gradient Sparsity, and Rank Collapse》的正证据锚定 `7 Experiments`；`6 Multi-Turn Limitation` 没有建立跨 reward/verifier、policy freshness 与分布漂移的 on-policy 有效性。因此该证据只能修正当前判断，超界时 `TRAIN-GRPO` 必须恢复 on-policy terminal/verifier baseline。 | analysis-decision:SF-2026-ARXIV-2606-29238 |
| SF-2026-ARXIV-2606-29239 | score_7_9 | not_selected | — | — | 未入选长叙事：把量化后安全回归纳入部署校准与发布 gate。《Breaking the Rounding Trap: Securing LLMs against Quantization-Conditioned Backdoors》的正证据锚定 `3.2 Empirical Motivation: The Role of Rounding Errors in LLM Quantization`；`3.1 Threat Model` 没有建立跨 threat distribution、attacker adaptation 与 effect-time authorization 的防护承诺。因此该证据只能修正当前判断，超界时 `PLATFORM-SECURITY` 必须拒绝 effect commit 并转 sandbox/人工。 | analysis-decision:SF-2026-ARXIV-2606-29239 |
| SF-2026-ARXIV-2606-29251 | score_7_9 | not_selected | — | — | 未入选长叙事：把上下文压缩的事实保真、推理可用性与预算绑定为控制合同。《When Summaries Distort Decisions: Information Fidelity in LLM-Compressed Financial Analysis》的正证据锚定 `4 Experiments`；`7 Limitations` 没有建立跨 task、compression policy 与 evidence loss 的决策保真。因此该证据只能修正当前判断，超界时 `AGENT-CONTEXT` 必须恢复 hash-addressed raw evidence。 | analysis-decision:SF-2026-ARXIV-2606-29251 |
| SF-2026-ARXIV-2606-29270 | score_7_9; potential_books_delta | not_selected | — | — | 未入选长叙事：只证明三异构 Agent、两轮、六 benchmark 的 debate-log classifier 能在已测阈值上安全翻转；共享训练导致的相关错误、换模型和换协议都可能破坏 81.2% Flip Precision。失配时不翻转并交给独立 verifier/人工。 | analysis-decision:SF-2026-ARXIV-2606-29270 |
| SF-2026-ARXIV-2606-29275 | score_7_9 | not_selected | — | — | 未入选长叙事：按置信度动态分配离散扩散步数并定义失败回退。《Adaptive Block Diffusion: Resolving Training-Inference Mismatch in Diffusion Language Models》的正证据锚定 `5 Experiments`；`4.4 Limitation of Block Diffusion` 没有建立跨 model、request shape、quality target 与 serving engine 的延迟-质量合同。因此该证据只能修正当前判断，超界时 `INFER-DECODE` 必须恢复已验证的普通 decode/refinement path。 | analysis-decision:SF-2026-ARXIV-2606-29275 |
| SF-2026-ARXIV-2606-29278 | score_7_9 | not_selected | — | — | 未入选长叙事：把推理复杂度上限与 benchmark 饱和分开，形成停止判断。《The Complexity Ceiling Benchmark: A Multi-Domain Evaluation of Sequential Reasoning Under Depth Scaling》的正证据锚定 `Trace-level evaluation and structural uncertainty`；`5 Discussion` 没有建立跨 dataset/model/evaluator revision 的 release acceptance 或生产 SLO。因此该证据只能修正当前判断，超界时 `PLATFORM-EVALUATION-SYSTEM` 必须保持 release Gate Open 并恢复完整分层评测。 | analysis-decision:SF-2026-ARXIV-2606-29278 |
| SF-2026-ARXIV-2606-29279 | score_7_9 | not_selected | — | — | 未入选长叙事：把记忆中的转述污染与一手证据 provenance 分开。《Manufactured Confidence: How Memory Consolidation Turns Hearsay into Confident Facts》的正证据锚定 `3 Results`；`Conclusion and source-provenance scope` 没有建立跨 workload、write policy、retention horizon 与 provenance shift 的记忆收益。因此该证据只能修正当前判断，超界时 `AGENT-MEMORY` 必须拒绝写入并保留旧 memory revision。 | analysis-decision:SF-2026-ARXIV-2606-29279 |
| SF-2026-ARXIV-2606-29280 | score_7_9 | not_selected | — | — | 未入选长叙事：把高风险 pipeline 的阶段性不确定性、升级与拒答纳入验收。《Deterministic Decisions for High-Stakes AI. A Zero-Egress Pipeline with the Deployability of RAG and the Accuracy of Machine Learning》的正证据锚定 `Evaluation methodology and outcome study`；`2.4 Machine Learning for Student Outcome Prediction: Benchmarks and Limits` 没有建立跨 dataset/model/evaluator revision 的 release acceptance 或生产 SLO。因此该证据只能修正当前判断，超界时 `PLATFORM-EVALUATION-SYSTEM` 必须保持 release Gate Open 并恢复完整分层评测。 | analysis-decision:SF-2026-ARXIV-2606-29280 |
| SF-2026-ARXIV-2606-29282 | score_7_9 | not_selected | — | — | 未入选长叙事：把概念擦除的残留行为与再激活纳入安全发布证据。《ScaleErasure: Inference-Time Minimal Intervention for Precise Concept Erasure in Next-Scale Autoregressive Image Generation》的正证据锚定 `5 Experiments`；`B Discussion on MACE Adaptation` 没有建立跨 threat distribution、attacker adaptation 与 effect-time authorization 的防护承诺。因此该证据只能修正当前判断，超界时 `PLATFORM-SECURITY` 必须拒绝 effect commit 并转 sandbox/人工。 | analysis-decision:SF-2026-ARXIV-2606-29282 |
| SF-2026-ARXIV-2606-29296 | score_7_9 | not_selected | — | — | 未入选长叙事：把策略更新的通过条件与样本级失败信号结合，改变 reward gate。《Process Advantage Signal Shaping: A Paradigm-Agnostic Middleware for Process-Supervised RL in LLM Reasoners》的正证据锚定 `Empirical scope; evaluation protocol`；`6 Discussion` 没有建立跨 reward/verifier、policy freshness 与分布漂移的 on-policy 有效性。因此该证据只能修正当前判断，超界时 `TRAIN-GRPO` 必须恢复 on-policy terminal/verifier baseline。 | analysis-decision:SF-2026-ARXIV-2606-29296 |
| SF-2026-ARXIV-2606-29315 | score_7_9 | not_selected | — | — | 未入选长叙事：把实验设计、工具执行、观测与假设修订组织成可复算工作流。《Hierarchical Experimentalist Agents》的正证据锚定 `4 Experiments and Results on Interphyre`；`A.5 Design Principles; domain-agnostic inputs and simulator-only evidence boundary` 没有建立跨 environment、tool semantics、checkpoint 与 compensation path 的可复算性。因此该证据只能修正当前判断，超界时 `AGENT-WORKFLOW` 必须停在可恢复 checkpoint 并执行 compensation。 | analysis-decision:SF-2026-ARXIV-2606-29315 |
| SF-2026-ARXIV-2606-29328 | score_7_9 | not_selected | — | — | 未入选长叙事：只证明六个 open-domain QA benchmark 上，把 K=200 candidate 的 k-context selection 改成多维 demand coverage 可改善 EM；理论 non-coverability 仅约束 query-proximity-monotone scorer，不直接约束 cross-encoder。sub-query drift、OT surrogate 成本或 corpus shift 失控时回退已校准 top-k/MMR。 | analysis-decision:SF-2026-ARXIV-2606-29328 |
| SF-2026-ARXIV-2606-29337 | score_7_9 | not_selected | — | — | 未入选长叙事：给 W4A4 量化的校准、kernel 与质量回退建立部署边界。《W4A4 Quantization for Inference on Wan2.2-I2V-A14B》的正证据锚定 `IV Evaluation and Results`；`IV-B Discussion` 没有建立跨 kernel、hardware、precision 与 graph revision 的执行计划可移植性。因此该证据只能修正当前判断，超界时 `INFER-TENSORRT-LLM` 必须恢复已验收 kernel/precision plan。 | analysis-decision:SF-2026-ARXIV-2606-29337 |
| SF-2026-ARXIV-2606-29340 | score_7_9 | not_selected | — | — | 未入选长叙事：把 off-policy 样本选择与策略漂移控制纳入训练状态。《PHF: Privileged Hidden Flow for On-Policy Self-Distillation》的正证据锚定 `Experiments`；`Discussion` 没有建立跨 reward/verifier、policy freshness 与分布漂移的 on-policy 有效性。因此该证据只能修正当前判断，超界时 `TRAIN-GRPO` 必须恢复 on-policy terminal/verifier baseline。 | analysis-decision:SF-2026-ARXIV-2606-29340 |
| SF-2026-ARXIV-2606-29350 | score_7_9 | not_selected | — | — | 未入选长叙事：把 VLA 视觉 token 合并与动作成功、延迟和回退共同校准。《Fast Enough to Act: Spatio-Temporal Visual Token Merging for Low-Latency Robotic VLMs and VLAs》的正证据锚定 `IV Experiments`；`V Conclusion and Discussion` 没有建立跨 embodiment、sensor、latency 与闭环干预的动作成功率。因此该证据只能修正当前判断，超界时 `MULTIMODAL-EMBODIED-VLA` 必须拒绝物理提交并交回保守 controller。 | analysis-decision:SF-2026-ARXIV-2606-29350 |
| SF-2026-ARXIV-2606-29354 | score_7_9 | not_selected | — | — | 未入选长叙事：把符号消息协议作为多 Agent 共享状态而非自由文本旁路。《When LLMs Develop Languages: Symbolic Communication for Efficient Multi-Agent Reasoning》的正证据锚定 `4 Experiments`；`5 Conclusion and Limitations` 没有建立跨 agent population、message protocol、error correlation 与 coordination load 的聚合收益。因此该证据只能修正当前判断，超界时 `AGENT-MULTI-AGENT` 必须恢复单 Agent/串行协调与人工仲裁。 | analysis-decision:SF-2026-ARXIV-2606-29354 |
| SF-2026-ARXIV-2606-29366 | score_7_9 | not_selected | — | — | 未入选长叙事：把 LLM 建议置于 solver 验证与可执行证据之后。《Solver-Verified Formulation Generation and Selection for Multi-Warehouse Inventory Allocation Using Large Language Models》的正证据锚定 `6 Computational Evaluation`；`Conclusion and solver-coverage boundary` 没有建立跨 environment、tool semantics、checkpoint 与 compensation path 的可复算性。因此该证据只能修正当前判断，超界时 `AGENT-WORKFLOW` 必须停在可恢复 checkpoint 并执行 compensation。 | analysis-decision:SF-2026-ARXIV-2606-29366 |
| SF-2026-ARXIV-2606-29377 | score_7_9 | not_selected | — | — | 未入选长叙事：把检索失败诊断、查询修复与证据重取变成循环控制。《Diagnosing and Repairing Factual Errors in RAG under Budget Constraints》的正证据锚定 `3 Experiments`；`Conclusion and evaluated-query scope` 没有建立跨 corpus、query distribution、retriever/index revision 与生成器的检索收益。因此该证据只能修正当前判断，超界时 `AGENT-RAG` 必须恢复固定、已校准的 retrieval plan。 | analysis-decision:SF-2026-ARXIV-2606-29377 |
| SF-2026-ARXIV-2606-29399 | score_7_9 | not_selected | — | — | 未入选长叙事：把多模态文档索引、跨页证据与推理计划联结。《LLM-Guided Planning for Multi-hop Reasoning over Multimodal Nuclear Regulatory Documents》的正证据锚定 `Experiments and multimodal document evaluation`；`7 Limitations` 没有建立跨 corpus、query distribution、retriever/index revision 与生成器的检索收益。因此该证据只能修正当前判断，超界时 `AGENT-RAG` 必须恢复固定、已校准的 retrieval plan。 | analysis-decision:SF-2026-ARXIV-2606-29399 |
| SF-2026-ARXIV-2606-29403 | score_7_9 | not_selected | — | — | 未入选长叙事：把 conformal coverage 与拒答/发布阈值绑定。《Self-Organized Conformal Prediction: Reducing Regional Coverage Gaps with Unsupervised Group Discovery》的正证据锚定 `4 Experiments`；`Conclusion and exchangeability boundary` 没有建立跨 dataset/model/evaluator revision 的 release acceptance 或生产 SLO。因此该证据只能修正当前判断，超界时 `PLATFORM-EVALUATION-SYSTEM` 必须保持 release Gate Open 并恢复完整分层评测。 | analysis-decision:SF-2026-ARXIV-2606-29403 |
| SF-2026-ARXIV-2606-29424 | score_7_9 | not_selected | — | — | 未入选长叙事：让 router 持有请求熵、专家选择与负载降级状态。《EntroRouter: Learning Efficient Model Routing via Entropy Regulation》的正证据锚定 `4 Experiments`；`5 Discussion` 没有建立跨 topology、并发负载、thermal state 与 SLO 的调度收益。因此该证据只能修正当前判断，超界时 `INFER-SCHEDULING` 必须恢复静态 placement 与保守 SLO headroom。 | analysis-decision:SF-2026-ARXIV-2606-29424 |
| SF-2026-ARXIV-2606-29425 | score_7_9 | not_selected | — | — | 未入选长叙事：把辩论者选择与聚合权重变成可校准协调状态。《Mixture of Debaters: Learn to Debate at Architectural Level in Multi-Agent Reasoning》的正证据锚定 `4 Experiments`；`Conclusion and tested-debater scope` 没有建立跨 agent population、message protocol、error correlation 与 coordination load 的聚合收益。因此该证据只能修正当前判断，超界时 `AGENT-MULTI-AGENT` 必须恢复单 Agent/串行协调与人工仲裁。 | analysis-decision:SF-2026-ARXIV-2606-29425 |
| SF-2026-ARXIV-2606-29441 | score_7_9 | not_selected | — | — | 未入选长叙事：把 activation defense 的检测、干预与失效边界置于运行时控制面。《Closing the Activation-Cone Blind Spot: Response-Time Probing and Unified Defense》的正证据锚定 `4 Experimental Setup; 5.1 No Single-Mechanism Paradigm Dominates`；`6 Discussion and Limitations` 没有建立跨 threat distribution、attacker adaptation 与 effect-time authorization 的防护承诺。因此该证据只能修正当前判断，超界时 `PLATFORM-SECURITY` 必须拒绝 effect commit 并转 sandbox/人工。 | analysis-decision:SF-2026-ARXIV-2606-29441 |
| SF-2026-ARXIV-2606-29445 | score_7_9 | not_selected | — | — | 未入选长叙事：把视频 GUI Agent 的长程观测与操作副作用纳入端到端评测。《Bridging VideoQA and Video-Guided Agentic Tasks via Generalized Keyframe Extraction》的正证据锚定 `4 Experiments`；`Conclusion and benchmark-domain scope` 没有建立跨 dataset/model/evaluator revision 的 release acceptance 或生产 SLO。因此该证据只能修正当前判断，超界时 `PLATFORM-EVALUATION-SYSTEM` 必须保持 release Gate Open 并恢复完整分层评测。 | analysis-decision:SF-2026-ARXIV-2606-29445 |
| SF-2026-ARXIV-2606-29472 | score_7_9; potential_books_delta | not_selected | — | — | 未入选长叙事：只覆盖 DynaCU-Bench 浏览器任务与已测 CU models；Gemini 3 Flash 上 keyframe image-token dilution 已构成反例，因此 AOI 不是固定 bundle，也未证明桌面 OS、权限副作用或持续会议场景安全。退回高保真 capture 与人工确认。 | analysis-decision:SF-2026-ARXIV-2606-29472 |
| SF-2026-ARXIV-2606-29476 | score_7_9 | not_selected | — | — | 未入选长叙事：把 reward 构造与可验证约束结合并保留失败样本。《CRAFT: Counterfactual Credit Assignment from Free Sibling Rollouts for Self-Distilled Agentic Reinforcement Learning》的正证据锚定 `5 Experiments`；`7 Discussion and Limitations` 没有建立跨 reward/verifier、policy freshness 与分布漂移的 on-policy 有效性。因此该证据只能修正当前判断，超界时 `TRAIN-GRPO` 必须恢复 on-policy terminal/verifier baseline。 | analysis-decision:SF-2026-ARXIV-2606-29476 |
| SF-2026-ARXIV-2606-29481 | score_7_9 | not_selected | — | — | 未入选长叙事：按难度与策略状态控制 rollout 采样和更新。《To Reason or to Fabricate: Reasoning Without Shortcuts via Hint-Anchored Pairwise Aggregation》的正证据锚定 `3 Experimental Setup`；`2.2 Direct KL Optimization and Its Limitations` 没有建立跨 reward/verifier、policy freshness 与分布漂移的 on-policy 有效性。因此该证据只能修正当前判断，超界时 `TRAIN-GRPO` 必须恢复 on-policy terminal/verifier baseline。 | analysis-decision:SF-2026-ARXIV-2606-29481 |
| SF-2026-ARXIV-2606-29490 | score_7_9 | not_selected | — | — | 未入选长叙事：把置信承诺、校准误差与拒答决策绑定。《Reported Confidence in LLMs Tracks Commitment More Than Correctness》的正证据锚定 `1.2 Supplemental Results`；`Conclusion and evaluated-distribution scope` 没有建立跨 dataset/model/evaluator revision 的 release acceptance 或生产 SLO。因此该证据只能修正当前判断，超界时 `PLATFORM-EVALUATION-SYSTEM` 必须保持 release Gate Open 并恢复完整分层评测。 | analysis-decision:SF-2026-ARXIV-2606-29490 |
| SF-2026-ARXIV-2606-29493 | score_7_9 | not_selected | — | — | 未入选长叙事：把形式化 benchmark 的语义正确与语法通过分层审计。《Faults in Our Formal Benchmarking: Dataset Defects and Evaluation Failures in Lean Theorem Proving》的正证据锚定 `2 What Formal Benchmarking Certifies (and What It Does Not)`；`7 Limitations` 没有建立跨 dataset/model/evaluator revision 的 release acceptance 或生产 SLO。因此该证据只能修正当前判断，超界时 `PLATFORM-EVALUATION-SYSTEM` 必须保持 release Gate Open 并恢复完整分层评测。 | analysis-decision:SF-2026-ARXIV-2606-29493 |
| SF-2026-ARXIV-2606-29501 | score_7_9 | not_selected | — | — | 未入选长叙事：把 action-conditioned rollout 与可干预世界状态联结。《Learning Transferable Dynamics Priors from Action to World Modeling》的正证据锚定 `4 Experiments`；`4.5 Ablations and discussions` 没有建立跨 environment、observation dynamics 与 physical commit 的 rollout fidelity。因此该证据只能修正当前判断，超界时 `MULTIMODAL-WORLD-MODELS` 必须停止 imagined rollout 并请求真实 observation。 | analysis-decision:SF-2026-ARXIV-2606-29501 |
| SF-2026-ARXIV-2606-29502 | score_7_9 | not_selected | — | — | 未入选长叙事：把技能发现、组合与持久化变成可更新 Agent 状态。《UCOB: Learning to Utilize and Evolve Agentic Skills via Credit-Aware On-Policy Bidirectional Self-Distillation》的正证据锚定 `6 Experiments`；`Conclusion and evaluated-environment boundary` 没有建立跨 workload、write policy、retention horizon 与 provenance shift 的记忆收益。因此该证据只能修正当前判断，超界时 `AGENT-MEMORY` 必须拒绝写入并保留旧 memory revision。 | analysis-decision:SF-2026-ARXIV-2606-29502 |
| SF-2026-ARXIV-2606-29506 | score_7_9 | not_selected | — | — | 未入选长叙事：揭示跨数据集切分污染并改变 benchmark release contract。《Benchmark AUC Is Not Deployable Reliability: A Cross-Dataset Audit of Off-the-Shelf Features for Surveillance Video Anomaly Detection》的正证据锚定 `IV Results`；`VII Discussion` 没有建立跨 dataset/model/evaluator revision 的 release acceptance 或生产 SLO。因此该证据只能修正当前判断，超界时 `PLATFORM-EVALUATION-SYSTEM` 必须保持 release Gate Open 并恢复完整分层评测。 | analysis-decision:SF-2026-ARXIV-2606-29506 |
| SF-2026-ARXIV-2606-29520 | score_7_9 | not_selected | — | — | 未入选长叙事：把安全知识、执行与拒答分层测量。《SAKE: Software Architectural Knowledge Evaluation Benchmark for Large Language Models》的正证据锚定 `Benchmark construction and evaluation`；`7 Threats to Validity` 没有建立跨 dataset/model/evaluator revision 的 release acceptance 或生产 SLO。因此该证据只能修正当前判断，超界时 `PLATFORM-EVALUATION-SYSTEM` 必须保持 release Gate Open 并恢复完整分层评测。 | analysis-decision:SF-2026-ARXIV-2606-29520 |
| SF-2026-ARXIV-2606-29522 | score_7_9; potential_books_delta | not_selected | — | — | 未入选长叙事：只在 Q8/D8 合成 transition task、Qwen2.5-Coder-7B 与 Mistral-7B-v0.3 上证明特定 written state 被因果读取；显式 scratchpad 的其他 token、自然语言推理和真实 Agent memory 均未被证明忠实。probe 不稳定时保留原文本与外部 verifier。 | analysis-decision:SF-2026-ARXIV-2606-29522 |
| SF-2026-ARXIV-2606-29526 | score_7_9 | not_selected | — | — | 未入选长叙事：把多阶段策略改进与验证门控组织成训练控制流。《The Mirage of Optimizing Training Policies: Monotonic Inference Policies as the Real Objective for LLM Reinforcement Learning》的正证据锚定 `5 Experiments`；`Limitations` 没有建立跨 reward/verifier、policy freshness 与分布漂移的 on-policy 有效性。因此该证据只能修正当前判断，超界时 `TRAIN-GRPO` 必须恢复 on-policy terminal/verifier baseline。 | analysis-decision:SF-2026-ARXIV-2606-29526 |
| SF-2026-ARXIV-2606-29532 | score_7_9 | not_selected | — | — | 未入选长叙事：把语义 join 的候选生成、验证与代价纳入查询计划。《SemJoin: Semantic Join Optimization》的正证据锚定 `4 Evaluation`；`Conclusion and evaluated-database scope` 没有建立跨 corpus、query distribution、retriever/index revision 与生成器的检索收益。因此该证据只能修正当前判断，超界时 `AGENT-RAG` 必须恢复固定、已校准的 retrieval plan。 | analysis-decision:SF-2026-ARXIV-2606-29532 |
| SF-2026-ARXIV-2606-29537 | score_7_9 | not_selected | — | — | 未入选长叙事：把 OSWorld 环境、任务与判定器升级为版本化 release contract。《OSWorld 2.0: Benchmarking Computer Use Agents on Long-Horizon Real-World Tasks》的正证据锚定 `2 OSWorld 2.0 Benchmark; evaluation protocol`；`6 Limitations` 没有建立跨 dataset/model/evaluator revision 的 release acceptance 或生产 SLO。因此该证据只能修正当前判断，超界时 `PLATFORM-EVALUATION-SYSTEM` 必须保持 release Gate Open 并恢复完整分层评测。 | analysis-decision:SF-2026-ARXIV-2606-29537 |
| SF-2026-ARXIV-2606-29538 | score_7_9 | not_selected | — | — | 未入选长叙事：把资源发现转成可执行 skill，并保留权限与失败边界。《RESOURCE2SKILL: Distilling Executable Agent Skills from Human-Created Multimodal Resources》的正证据锚定 `4 Experiments`；`M Limitations` 没有建立跨 environment、tool semantics、checkpoint 与 compensation path 的可复算性。因此该证据只能修正当前判断，超界时 `AGENT-WORKFLOW` 必须停在可恢复 checkpoint 并执行 compensation。 | analysis-decision:SF-2026-ARXIV-2606-29538 |
| SF-2026-ARXIV-2606-29541 | score_7_9 | not_selected | — | — | 未入选长叙事：把 MARL 协调的共享意图与通信失效纳入状态。《Learned Coordination Conventions in Cooperative MARL: Measuring the Translation Gap Between Theory-Informed Roles and Learned Routing》的正证据锚定 `5 Experiments`；`6 Discussion` 没有建立跨 agent population、message protocol、error correlation 与 coordination load 的聚合收益。因此该证据只能修正当前判断，超界时 `AGENT-MULTI-AGENT` 必须恢复单 Agent/串行协调与人工仲裁。 | analysis-decision:SF-2026-ARXIV-2606-29541 |
| SF-2026-ARXIV-2606-29544 | score_7_9 | not_selected | — | — | 未入选长叙事：把生产分布漂移、攻击与回退纳入鲁棒性发布证据。《Proteus: Automated Adversarial Robustness Testing for Audio Deepfake Detectors》的正证据锚定 `3 Results`；`Conclusion and tested-shift boundary` 没有建立跨 threat distribution、attacker adaptation 与 effect-time authorization 的防护承诺。因此该证据只能修正当前判断，超界时 `PLATFORM-SECURITY` 必须拒绝 effect commit 并转 sandbox/人工。 | analysis-decision:SF-2026-ARXIV-2606-29544 |
| SF-2026-ARXIV-2606-29554 | score_7_9 | not_selected | — | — | 未入选长叙事：揭示数据 shuffle 与 optimizer state 的耦合，改变复现合同。《Optimizer Memory Makes Shuffle Order a First-Order Source of Fine-Tuning Noise》的正证据锚定 `5 Empirical evidence`；`7 Discussion` 没有建立跨 architecture、optimizer、token budget 与更大训练尺度的可迁移性。因此该证据只能修正当前判断，超界时 `TRAIN-PRETRAINING` 必须恢复邻近规模 sweep 与已验证 schedule。 | analysis-decision:SF-2026-ARXIV-2606-29554 |
| SF-2026-ARXIV-2606-29563 | score_7_9 | not_selected | — | — | 未入选长叙事：用跨头跨层 coverage 状态驱动 KV 驱逐并保留完整缓存回退。《Coverage-Driven KV Cache Eviction for Efficient and Improved Inference of LLM》的正证据锚定 `5 Experiments; 5.1 Experimental setup`；`5.3 Discussion; 5.3.5 Computational Complexity` 没有建立跨 attention pattern、context length 与 workload shift 的 eviction 安全性。因此该证据只能修正当前判断，超界时 `INFER-KV-CACHE` 必须恢复完整 KV 或保守 eviction。 | analysis-decision:SF-2026-ARXIV-2606-29563 |
| SF-2026-ARXIV-2606-29565 | score_7_9; potential_books_delta | selected | DA-20260629-2606-29565 | — | 入选：只在 LayerScale 专有 engine、单 H100、70B-class 4-bit target 上测得 capability-gated fast path；8B BF16 不触发 gate，且大量收益为测量常数上的闭式推导。任何 state mutation 或置信漂移都必须 invalidate 并恢复普通 decode。 | analysis:DA-20260629-2606-29565 |
| SF-2026-ARXIV-2606-29567 | score_7_9 | not_selected | — | — | 未入选长叙事：把 PII 替身生成、加密映射与还原置于本地代理控制面。《SurrogateShield: Beyond Redaction for High-Utility, Privacy-Preserving LLM Interactions》的正证据锚定 `4 Evaluation Methodology`；`6 Discussion` 没有建立跨 threat distribution、attacker adaptation 与 effect-time authorization 的防护承诺。因此该证据只能修正当前判断，超界时 `PLATFORM-SECURITY` 必须拒绝 effect commit 并转 sandbox/人工。 | analysis-decision:SF-2026-ARXIV-2606-29567 |
| SF-2026-ARXIV-2606-29571 | score_7_9; potential_books_delta | not_selected | — | — | 未入选长叙事：只比较 19 个 parameter-free metric、19 encoder 与七个静态数据集；0.01 crowded split、dominant-direction removal 和相关性未证明在线 corpus 漂移下的因果门槛，也未覆盖 learned metric。收益消失时恢复已校准 cosine/混合检索。 | analysis-decision:SF-2026-ARXIV-2606-29571 |
| SF-2026-ARXIV-2606-29573 | score_7_9 | not_selected | — | — | 未入选长叙事：把多模态生成粒度与可靠性共同纳入发布阈值。《Reliability-Prioritized Fine-Grained Generation in Multimodal Large》的正证据锚定 `2.1 MLLM Benchmarks; experiments`；`Conclusion and expert-verified benchmark scope` 没有建立跨 dataset/model/evaluator revision 的 release acceptance 或生产 SLO。因此该证据只能修正当前判断，超界时 `PLATFORM-EVALUATION-SYSTEM` 必须保持 release Gate Open 并恢复完整分层评测。 | analysis-decision:SF-2026-ARXIV-2606-29573 |
| SF-2026-ARXIV-2606-29580 | score_7_9 | not_selected | — | — | 未入选长叙事：把离线索引、设备内生成、citation 与语料缺口串成端侧 RAG 合同。《MAM-AI: An On-Device Medical Retrieval-Augmented Generation System for Nurses and Midwives in Zanzibar》的正证据锚定 `4 Evaluation Methodology; Sections 5-8 component results`；`9 Discussion; 10 Limitations and Future Work` 没有建立跨 corpus、query distribution、retriever/index revision 与生成器的检索收益。因此该证据只能修正当前判断，超界时 `AGENT-RAG` 必须恢复固定、已校准的 retrieval plan。 | analysis-decision:SF-2026-ARXIV-2606-29580 |
| SF-2026-ARXIV-2606-29581 | score_7_9; potential_books_delta | not_selected | — | — | 未入选长叙事：当前 official exact-v1 的 Abstract 与 §3 一致披露 9 models、161 configurations、AdvBench+XSTest 与约 322k responses；证据只覆盖以 Pile validation calibration 的 AWQ INT4/GPTQ INT8、2B–8B 模型与静态 AdvBench，未证明 NF4/GGUF/对抗式 calibration、>70B、adaptive jailbreak/prompt injection 或 judge 完美可靠。任一切片回归即恢复已验收 precision/sampler。 | analysis-decision:SF-2026-ARXIV-2606-29581 |
| SF-2026-ARXIV-2606-29592 | score_7_9 | not_selected | — | — | 未入选长叙事：把 perception、navigation、planning 与剂量预算解耦评测。《STEMGym: Benchmarking Sequential Decision-Making under Dose Budgets in Autonomous Electron Microscopy》的正证据锚定 `4 Experiments`；`5 Limitations` 没有建立跨 dataset/model/evaluator revision 的 release acceptance 或生产 SLO。因此该证据只能修正当前判断，超界时 `PLATFORM-EVALUATION-SYSTEM` 必须保持 release Gate Open 并恢复完整分层评测。 | analysis-decision:SF-2026-ARXIV-2606-29592 |
| SF-2026-ARXIV-2606-29601 | score_7_9; potential_books_delta | not_selected | — | — | 未入选长叙事：只验证有限 Langshaw examples 到 BSPL tableau 的 safety/liveness 与编译时间；未证明开放网络中的 delivery、identity、Byzantine role 或工具副作用。协议编译/验证超界时回到串行 coordinator 与人工仲裁。 | analysis-decision:SF-2026-ARXIV-2606-29601 |
| SF-2026-ARXIV-2606-29602 | score_7_9 | not_selected | — | — | 未入选长叙事：把多语言、编码与多阶段 prompt injection 纳入威胁矩阵。《An Empirical Evaluation of Prompt Injection Vulnerabilities in Large Language Models Across Multilingual and Obfuscated Attack Scenarios》的正证据锚定 `II-D Empirical Evaluations of LLM Safety; IV Results`；`V Discussion` 没有建立跨 threat distribution、attacker adaptation 与 effect-time authorization 的防护承诺。因此该证据只能修正当前判断，超界时 `PLATFORM-SECURITY` 必须拒绝 effect commit 并转 sandbox/人工。 | analysis-decision:SF-2026-ARXIV-2606-29602 |
| SF-2026-ARXIV-2606-29604 | score_7_9 | not_selected | — | — | 未入选长叙事：把权重/激活扰动用于潜在行为发现并定义代理选择边界。《Mechanistically Eliciting Latent Behaviors in Language Models》的正证据锚定 `Experimental setup; latent-behavior evaluation`；`Conclusion and model-organism scope` 没有建立跨 threat distribution、attacker adaptation 与 effect-time authorization 的防护承诺。因此该证据只能修正当前判断，超界时 `PLATFORM-SECURITY` 必须拒绝 effect commit 并转 sandbox/人工。 | analysis-decision:SF-2026-ARXIV-2606-29604 |
| SF-2026-ARXIV-2606-29605 | score_7_9 | not_selected | — | — | 未入选长叙事：把生成语料的 provenance、复制与跨记录冗余转成训练前数据控制状态。《How much of an LLM-generated clinical corpus is actually new? A production-scale measurement of content redundancy for provenance classification》的正证据锚定 `2 Results; downstream equal-token adaptation test`；`3 Discussion` 没有建立跨 corpus、训练阶段与真实删除/重训操作的因果有效性。因此该证据只能修正当前判断，超界时 `TRAIN-DATA` 必须保留原样本、lineage 与重训对照。 | analysis-decision:SF-2026-ARXIV-2606-29605 |
| SF-2026-ARXIV-2606-29623 | score_7_9; potential_books_delta | not_selected | — | — | 未入选长叙事：MNIST 与 Llama-Guard hidden-state jailbreak fleet 只验证经校准 ruler 的 rare-event estimate；论文明确指出 behavioral fleet 约 2,000 variants 仍不足、Mahalanobis ruler 可结构性失效，跨 corpus 必须重新校准。否则 Gate 保持 Open。 | analysis-decision:SF-2026-ARXIV-2606-29623 |
| SF-2026-ARXIV-2606-29629 | score_7_9 | not_selected | — | — | 未入选长叙事：让软件 DVFS controller 持有多模态 serving 阶段、功耗与热状态。《Energy-Efficient Multimodal Inference Serving with Tri-serve》的正证据锚定 `II-C1 Frequency-locked Roofline Benchmarking; IV Evaluation`；`V Conclusion; evaluated Qwen-Omni/GPU-cluster boundary` 没有建立跨 topology、并发负载、thermal state 与 SLO 的调度收益。因此该证据只能修正当前判断，超界时 `INFER-SCHEDULING` 必须恢复静态 placement 与保守 SLO headroom。 | analysis-decision:SF-2026-ARXIV-2606-29629 |
| SF-2026-ARXIV-2606-29645 | score_7_9 | not_selected | — | — | 未入选长叙事：把 metadata、结构与 multi-hop strategy 分解为可单独验收的 RAG 控制变量。《Metadata, Structure, or Strategy? A Decomposition of RAG Context Enrichment》的正证据锚定 `3.2 Experimental Design; results across six benchmarks`；`6.1 Limitations` 没有建立跨 corpus、query distribution、retriever/index revision 与生成器的检索收益。因此该证据只能修正当前判断，超界时 `AGENT-RAG` 必须恢复固定、已校准的 retrieval plan。 | analysis-decision:SF-2026-ARXIV-2606-29645 |
| SF-2026-ARXIV-2606-29646 | score_7_9 | not_selected | — | — | 未入选长叙事：把 sleeper behavior elicitation 的 fuzzing、代理调参与 oracle 边界分开。《Fuzzing Large Language Models to Elicit Hidden Behaviours》的正证据锚定 `3 Results`；`4 Discussion` 没有建立跨 threat distribution、attacker adaptation 与 effect-time authorization 的防护承诺。因此该证据只能修正当前判断，超界时 `PLATFORM-SECURITY` 必须拒绝 effect commit 并转 sandbox/人工。 | analysis-decision:SF-2026-ARXIV-2606-29646 |
| SF-2026-ARXIV-2606-29648 | score_7_9 | not_selected | — | — | 未入选长叙事：让 meta-agent 从失败轨迹重写多检索器编排策略。《Hybrid Retriever Evolution for Multimodal Document Reasoning Agents》的正证据锚定 `4 Experiments`；`A Limitations` 没有建立跨 corpus、query distribution、retriever/index revision 与生成器的检索收益。因此该证据只能修正当前判断，超界时 `AGENT-RAG` 必须恢复固定、已校准的 retrieval plan。 | analysis-decision:SF-2026-ARXIV-2606-29648 |
| SF-2026-ARXIV-2606-29649 | score_7_9 | not_selected | — | — | 未入选长叙事：把分辨率、字符构造与语言纳入 VLM moderation 威胁面。《Resolution Thresholds in VLM Detection of Harmful ASCII Art Across Construction Modes and Languages》的正证据锚定 `3.2 VLM Evaluation`；`5 Discussion` 没有建立跨 threat distribution、attacker adaptation 与 effect-time authorization 的防护承诺。因此该证据只能修正当前判断，超界时 `PLATFORM-SECURITY` 必须拒绝 effect commit 并转 sandbox/人工。 | analysis-decision:SF-2026-ARXIV-2606-29649 |
| SF-2026-ARXIV-2606-29652 | score_7_9 | not_selected | — | — | 未入选长叙事：把索引、模型与推理默认置于用户设备，并把远端服务降为可选路径。《As We May Search》的正证据锚定 `4.1 Experimental Setup; five benchmarks and 1K-1M documents`；`4.11 Limitations` 没有建立跨 corpus、query distribution、retriever/index revision 与生成器的检索收益。因此该证据只能修正当前判断，超界时 `AGENT-RAG` 必须恢复固定、已校准的 retrieval plan。 | analysis-decision:SF-2026-ARXIV-2606-29652 |
| SF-2026-ARXIV-2606-29654 | score_7_9; potential_books_delta | selected | DA-20260629-2606-29654 | — | 入选：保证依赖 local bias envelope、representation-gap bound 与 calibration split，并非 distribution-free；六个选择题 benchmark 与训练期 difficulty-normalized budget 未证明开放式任务或分布漂移。诊断失败时全 defer/人工。 | analysis:DA-20260629-2606-29654 |
| SF-2026-ARXIV-2606-29657 | score_7_9 | not_selected | — | — | 未入选长叙事：把预测器训练与下游行动奖励隔离，并把 agency 留给受约束 scaffolding。《Safety from Honesty in a Disinterested AI Predictor》的正证据锚定 `Formal safety argument and falsifiability analysis`；`5.4.2 Falsifiability, Scope, and Requirements for a Concrete Design` 没有建立跨 threat distribution、attacker adaptation 与 effect-time authorization 的防护承诺。因此该证据只能修正当前判断，超界时 `PLATFORM-SECURITY` 必须拒绝 effect commit 并转 sandbox/人工。 | analysis-decision:SF-2026-ARXIV-2606-29657 |
| SF-2026-ARXIV-2606-29661 | score_7_9 | not_selected | — | — | 未入选长叙事：让 ensemble controller 同时优化预测质量与跨模型错误多样性。《Diversity is the Strength of the AI Crowd》的正证据锚定 `5 Results`；`6 Discussion` 没有建立跨 agent population、message protocol、error correlation 与 coordination load 的聚合收益。因此该证据只能修正当前判断，超界时 `AGENT-MULTI-AGENT` 必须恢复单 Agent/串行协调与人工仲裁。 | analysis-decision:SF-2026-ARXIV-2606-29661 |
| SF-2026-ARXIV-2606-29679 | score_7_9 | not_selected | — | — | 未入选长叙事：用表示距离矩阵轨迹监测训练相变，而非只观察标量 loss。《Learning as Observable Matrix Dynamics: Diffusive Relaxations versus Phase Transitions》的正证据锚定 `4 Experiments`；`6 Discussion` 没有建立跨 workload、signal drift 与告警副作用的生产检测率。因此该证据只能修正当前判断，超界时 `PLATFORM-MONITORING` 必须只保留 observe-only 告警并请求重新校准。 | analysis-decision:SF-2026-ARXIV-2606-29679 |
| SF-2026-ARXIV-2606-30686 | score_7_9 | not_selected | — | — | 未入选长叙事：把 VLA 的语义匹配与物理动作泛化拆成可识别因果评测。《Position: Vision-Language-Action Models Cannot Be Verified to Perform Physical Reasoning》的正证据锚定 `3.2 Three Levels of Non-Identifiability in Current Evaluation`；`Conclusion and proposed controlled-variation scope` 没有建立跨 dataset/model/evaluator revision 的 release acceptance 或生产 SLO。因此该证据只能修正当前判断，超界时 `PLATFORM-EVALUATION-SYSTEM` 必须保持 release Gate Open 并恢复完整分层评测。 | analysis-decision:SF-2026-ARXIV-2606-30686 |
| SF-2026-ARXIV-2606-30689 | score_7_9 | not_selected | — | — | 未入选长叙事：把逐行需求 citation 变成可自动检测幻觉的 provenance 合同。《Citation Discipline in Spec-Driven Development: A Cross-Model Empirical Study of Output Determinism and Automated Hallucination Detection in LLM-Generated Code》的正证据锚定 `4 Experimental Design; cross-model results`；`7 Discussion` 没有建立跨 environment、tool semantics、checkpoint 与 compensation path 的可复算性。因此该证据只能修正当前判断，超界时 `AGENT-WORKFLOW` 必须停在可恢复 checkpoint 并执行 compensation。 | analysis-decision:SF-2026-ARXIV-2606-30689 |

<!-- analysis-decision:SF-2026-ARXIV-2606-29142:start -->
未入选长叙事：把受监管金融 Agent 的模型、工具、审计证据与人工授权绑定为部署控制面。《Agent Security Meets Regulatory Reality -- A Practitioner Systematization of Autonomous-Agent Threats and Controls in Regulated Financial Systems》的正证据锚定 `IV Architectural Patterns Observed in Production; V Negative Results and Open Problems`；`V Negative Results and Open Problems; VI Generalization Beyond Finance` 没有建立跨 threat distribution、attacker adaptation 与 effect-time authorization 的防护承诺。因此该证据只能修正当前判断，超界时 `PLATFORM-SECURITY` 必须拒绝 effect commit 并转 sandbox/人工。
<!-- analysis-decision:SF-2026-ARXIV-2606-29142:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29150:start -->
未入选长叙事：把 flow reasoning 的中间状态、自验证与 test-time compute 变成推理时控制路径。《Flow Reasoning Models: Scaling Reasoning Through Iterative Self-Refinement》的正证据锚定 `4 Experiments; G Experimental setup and hyperparameters`；`6 Discussion; B Test-time scaling: coverage, selection, and sampling-step baselines` 没有建立跨 model、request shape、quality target 与 serving engine 的延迟-质量合同。因此该证据只能修正当前判断，超界时 `INFER-DECODE` 必须恢复已验证的普通 decode/refinement path。
<!-- analysis-decision:SF-2026-ARXIV-2606-29150:end -->

<!-- analysis:DA-20260629-2606-29151:start -->
入选：只证明 SemBench 上 intent-specific operator DAG 与异构 backend 的 quality/latency/cost 计划选择；未证明跨 operator 的联合最优、teacher-noise 之外的 label shift，或 Azure/API 与本地模型间可移植性。失配时固定到已校准 retrieval plan。
<!-- analysis:DA-20260629-2606-29151:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29158:start -->
未入选长叙事：只覆盖 GPT-2-style 22M-707M、FineWeb 5B-100B tokens、WSD 与 AdamW/AdamH；论文明确显示 log-linear LR 仅局部成立，不能外推到其他架构、optimizer 或更大规模。超界时重新 sweep 邻近尺度。
<!-- analysis-decision:SF-2026-ARXIV-2606-29158:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29159:start -->
未入选长叙事：揭示 pooled leaderboard 会掩盖 RCA 子任务差异，改变评测聚合合同。《Pooled Leaderboards Hide System-Specific Winners: A Reporting-Protocol Audit of Offline Root-Cause Analysis Benchmarks》的正证据锚定 `Benchmark validity and leaderboard instability in ML; system-specific results`；`6 Discussion, Limitations, and Recommendations` 没有建立跨 dataset/model/evaluator revision 的 release acceptance 或生产 SLO。因此该证据只能修正当前判断，超界时 `PLATFORM-EVALUATION-SYSTEM` 必须保持 release Gate Open 并恢复完整分层评测。
<!-- analysis-decision:SF-2026-ARXIV-2606-29159:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29171:start -->
未入选长叙事：只在 Llama-3.2-3B-Instruct refusal proxy、特定 SAE 与 200 个 SFT pair 上验证一阶符号归因；feature label、Ridge fidelity 与 first-order approximation 不等于真实删除/重训因果。保留原样本与重训对照。
<!-- analysis-decision:SF-2026-ARXIV-2606-29171:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29176:start -->
未入选长叙事：改变优化器更新的去偏与稳定性路径，并要求按训练阶段校准。《Dead-Direction Conditioners: Gauge-Equivariant Preconditioning for Deep Networks》的正证据锚定 `5 Experiments; 5.1 Reading the rate at language-model scale`；`5.10 Scope and limitations` 没有建立跨 architecture、optimizer、token budget 与更大训练尺度的可迁移性。因此该证据只能修正当前判断，超界时 `TRAIN-PRETRAINING` 必须恢复邻近规模 sweep 与已验证 schedule。
<!-- analysis-decision:SF-2026-ARXIV-2606-29176:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29178:start -->
未入选长叙事：把长期记忆的写入、保留与遗忘门控变成显式持久状态迁移。《Selective Memory Retention for Long-Horizon LLM Agents》的正证据锚定 `4 Experiments`；`6 Discussion and Limitations` 没有建立跨 workload、write policy、retention horizon 与 provenance shift 的记忆收益。因此该证据只能修正当前判断，超界时 `AGENT-MEMORY` 必须拒绝写入并保留旧 memory revision。
<!-- analysis-decision:SF-2026-ARXIV-2606-29178:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29182:start -->
未入选长叙事：让科学发现 Agent 的信念状态、实验动作与反证更新形成可追踪闭环。《Evidence-Informed LLM Beliefs for Continual Scientific Discovery》的正证据锚定 `3.1.2 Evaluation: Reducing Surprisal Under Non-Stationary Beliefs`；`6 Limitations` 没有建立跨 environment、tool semantics、checkpoint 与 compensation path 的可复算性。因此该证据只能修正当前判断，超界时 `AGENT-WORKFLOW` 必须停在可恢复 checkpoint 并执行 compensation。
<!-- analysis-decision:SF-2026-ARXIV-2606-29182:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29184:start -->
未入选长叙事：把适配器秩分配与层级预算绑定为可动态选择的训练状态。《BaRA: Bayesian Adaptive Rank Allocation for Parameter-Efficient Fine-Tuning》的正证据锚定 `VI Experiments`；`III-C Limitations of Bayesian LoRA Methods` 没有建立跨 backbone、target module、rank budget 与 merge/serve path 的稳定性。因此该证据只能修正当前判断，超界时 `TRAIN-LORA` 必须恢复固定 rank/target-module adapter。
<!-- analysis-decision:SF-2026-ARXIV-2606-29184:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29193:start -->
未入选长叙事：把微服务 Agent 的任务、环境、副作用和故障恢复纳入发布评测。《A Multi-Dataset Benchmark for Evaluating LLM Agents in Microservice Failure Diagnosis》的正证据锚定 `4 Evaluation; 4.4 Evaluation Metric`；`6 Discussion` 没有建立跨 dataset/model/evaluator revision 的 release acceptance 或生产 SLO。因此该证据只能修正当前判断，超界时 `PLATFORM-EVALUATION-SYSTEM` 必须保持 release Gate Open 并恢复完整分层评测。
<!-- analysis-decision:SF-2026-ARXIV-2606-29193:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29194:start -->
未入选长叙事：把多 Agent 搜索的共享状态、隔离边界与合并控制显式化。《AI Trading's Alpha Singularity: Emergent Market Reasoning through Agent-to-Agent Self-Evolution》的正证据锚定 `Statistical inference and out-of-sample evaluation`；`6 Discussion` 没有建立跨 agent population、message protocol、error correlation 与 coordination load 的聚合收益。因此该证据只能修正当前判断，超界时 `AGENT-MULTI-AGENT` 必须恢复单 Agent/串行协调与人工仲裁。
<!-- analysis-decision:SF-2026-ARXIV-2606-29194:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29196:start -->
未入选长叙事：SAD 上的线性可恢复性只是一种 operational evaluation-awareness signal；white-box AUROC 与黑盒行为会分离，且 Qwen/Gemma 的深度迁移不构成跨 family scaling law。异常只触发额外 held-out evaluation，不授予直接拒绝权。
<!-- analysis-decision:SF-2026-ARXIV-2606-29196:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29207:start -->
未入选长叙事：把 kernel 生成、校验、选择与回退组成可执行的推理内核控制流。《KernelFlume: Elastic Core-Attention Scaling for Agentic Long-Context Decoding》的正证据锚定 `6 Evaluation`；`2.4 Limitations of Existing Elastic Scaling` 没有建立跨 model、request shape、quality target 与 serving engine 的延迟-质量合同。因此该证据只能修正当前判断，超界时 `INFER-DECODE` 必须恢复已验证的普通 decode/refinement path。
<!-- analysis-decision:SF-2026-ARXIV-2606-29207:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29215:start -->
未入选长叙事：把 discrete diffusion 的多块并行解码、校验与质量退化边界显式化。《Multi-Block Diffusion Language Models》的正证据锚定 `4 Experiments`；`5 Conclusion and stated speed-quality scope` 没有建立跨 model、request shape、quality target 与 serving engine 的延迟-质量合同。因此该证据只能修正当前判断，超界时 `INFER-DECODE` 必须恢复已验证的普通 decode/refinement path。
<!-- analysis-decision:SF-2026-ARXIV-2606-29215:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29222:start -->
未入选长叙事：把机器人情境记忆接入感知到动作的闭环状态。《CORE Planner: Contextual-memory Oriented Reinforcement-learning in Unknown Environments for Robot Navigation》的正证据锚定 `V Experiments`；`VI Conclusion and deployment scope` 没有建立跨 embodiment、sensor、latency 与闭环干预的动作成功率。因此该证据只能修正当前判断，超界时 `MULTIMODAL-EMBODIED-VLA` 必须拒绝物理提交并交回保守 controller。
<!-- analysis-decision:SF-2026-ARXIV-2606-29222:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29223:start -->
未入选长叙事：把推理深度按样本难度分配，并保留固定深度回退。《Depth Exploration for LLM Decoding》的正证据锚定 `4 Experiment`；`E Limitations and discussion` 没有建立跨 model、request shape、quality target 与 serving engine 的延迟-质量合同。因此该证据只能修正当前判断，超界时 `INFER-DECODE` 必须恢复已验证的普通 decode/refinement path。
<!-- analysis-decision:SF-2026-ARXIV-2606-29223:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29225:start -->
未入选长叙事：把 Agent policy 判定置于工具副作用提交前并定义 fail-closed 路径。《PolicyGuard: A Dialogue-Grounded Sub-Agent Verifier for Policy Adherence in LLM Agents》的正证据锚定 `4 Experiments`；`Discussion` 没有建立跨 threat distribution、attacker adaptation 与 effect-time authorization 的防护承诺。因此该证据只能修正当前判断，超界时 `PLATFORM-SECURITY` 必须拒绝 effect commit 并转 sandbox/人工。
<!-- analysis-decision:SF-2026-ARXIV-2606-29225:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29228:start -->
未入选长叙事：揭示 DLM 评测中的表面提升与实际生成能力分离。《Understanding Evaluation Illusion in Diffusion Large Language Models》的正证据锚定 `3 Evaluation Inconsistency; 4 Experiments`；`5 Discussion; speed-quality trade-off counterevidence` 没有建立跨 dataset/model/evaluator revision 的 release acceptance 或生产 SLO。因此该证据只能修正当前判断，超界时 `PLATFORM-EVALUATION-SYSTEM` 必须保持 release Gate Open 并恢复完整分层评测。
<!-- analysis-decision:SF-2026-ARXIV-2606-29228:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29237:start -->
未入选长叙事：把运动持续性作为世界模型 rollout 的可测状态而非单帧视觉指标。《MoPe: Motion Permanence for Robust Monocular Gaussian Mapping in Dynamic Environments》的正证据锚定 `IV Experiments`；`V Limitations and Future Work` 没有建立跨 environment、observation dynamics 与 physical commit 的 rollout fidelity。因此该证据只能修正当前判断，超界时 `MULTIMODAL-WORLD-MODELS` 必须停止 imagined rollout 并请求真实 observation。
<!-- analysis-decision:SF-2026-ARXIV-2606-29237:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29238:start -->
未入选长叙事：给 GRPO 更新的稳定域与偏差来源建立理论边界。《On the Policy Gradient Foundations of Group Relative Policy Optimization: Credit Assignment, Gradient Sparsity, and Rank Collapse》的正证据锚定 `7 Experiments`；`6 Multi-Turn Limitation` 没有建立跨 reward/verifier、policy freshness 与分布漂移的 on-policy 有效性。因此该证据只能修正当前判断，超界时 `TRAIN-GRPO` 必须恢复 on-policy terminal/verifier baseline。
<!-- analysis-decision:SF-2026-ARXIV-2606-29238:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29239:start -->
未入选长叙事：把量化后安全回归纳入部署校准与发布 gate。《Breaking the Rounding Trap: Securing LLMs against Quantization-Conditioned Backdoors》的正证据锚定 `3.2 Empirical Motivation: The Role of Rounding Errors in LLM Quantization`；`3.1 Threat Model` 没有建立跨 threat distribution、attacker adaptation 与 effect-time authorization 的防护承诺。因此该证据只能修正当前判断，超界时 `PLATFORM-SECURITY` 必须拒绝 effect commit 并转 sandbox/人工。
<!-- analysis-decision:SF-2026-ARXIV-2606-29239:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29251:start -->
未入选长叙事：把上下文压缩的事实保真、推理可用性与预算绑定为控制合同。《When Summaries Distort Decisions: Information Fidelity in LLM-Compressed Financial Analysis》的正证据锚定 `4 Experiments`；`7 Limitations` 没有建立跨 task、compression policy 与 evidence loss 的决策保真。因此该证据只能修正当前判断，超界时 `AGENT-CONTEXT` 必须恢复 hash-addressed raw evidence。
<!-- analysis-decision:SF-2026-ARXIV-2606-29251:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29270:start -->
未入选长叙事：只证明三异构 Agent、两轮、六 benchmark 的 debate-log classifier 能在已测阈值上安全翻转；共享训练导致的相关错误、换模型和换协议都可能破坏 81.2% Flip Precision。失配时不翻转并交给独立 verifier/人工。
<!-- analysis-decision:SF-2026-ARXIV-2606-29270:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29275:start -->
未入选长叙事：按置信度动态分配离散扩散步数并定义失败回退。《Adaptive Block Diffusion: Resolving Training-Inference Mismatch in Diffusion Language Models》的正证据锚定 `5 Experiments`；`4.4 Limitation of Block Diffusion` 没有建立跨 model、request shape、quality target 与 serving engine 的延迟-质量合同。因此该证据只能修正当前判断，超界时 `INFER-DECODE` 必须恢复已验证的普通 decode/refinement path。
<!-- analysis-decision:SF-2026-ARXIV-2606-29275:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29278:start -->
未入选长叙事：把推理复杂度上限与 benchmark 饱和分开，形成停止判断。《The Complexity Ceiling Benchmark: A Multi-Domain Evaluation of Sequential Reasoning Under Depth Scaling》的正证据锚定 `Trace-level evaluation and structural uncertainty`；`5 Discussion` 没有建立跨 dataset/model/evaluator revision 的 release acceptance 或生产 SLO。因此该证据只能修正当前判断，超界时 `PLATFORM-EVALUATION-SYSTEM` 必须保持 release Gate Open 并恢复完整分层评测。
<!-- analysis-decision:SF-2026-ARXIV-2606-29278:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29279:start -->
未入选长叙事：把记忆中的转述污染与一手证据 provenance 分开。《Manufactured Confidence: How Memory Consolidation Turns Hearsay into Confident Facts》的正证据锚定 `3 Results`；`Conclusion and source-provenance scope` 没有建立跨 workload、write policy、retention horizon 与 provenance shift 的记忆收益。因此该证据只能修正当前判断，超界时 `AGENT-MEMORY` 必须拒绝写入并保留旧 memory revision。
<!-- analysis-decision:SF-2026-ARXIV-2606-29279:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29280:start -->
未入选长叙事：把高风险 pipeline 的阶段性不确定性、升级与拒答纳入验收。《Deterministic Decisions for High-Stakes AI. A Zero-Egress Pipeline with the Deployability of RAG and the Accuracy of Machine Learning》的正证据锚定 `Evaluation methodology and outcome study`；`2.4 Machine Learning for Student Outcome Prediction: Benchmarks and Limits` 没有建立跨 dataset/model/evaluator revision 的 release acceptance 或生产 SLO。因此该证据只能修正当前判断，超界时 `PLATFORM-EVALUATION-SYSTEM` 必须保持 release Gate Open 并恢复完整分层评测。
<!-- analysis-decision:SF-2026-ARXIV-2606-29280:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29282:start -->
未入选长叙事：把概念擦除的残留行为与再激活纳入安全发布证据。《ScaleErasure: Inference-Time Minimal Intervention for Precise Concept Erasure in Next-Scale Autoregressive Image Generation》的正证据锚定 `5 Experiments`；`B Discussion on MACE Adaptation` 没有建立跨 threat distribution、attacker adaptation 与 effect-time authorization 的防护承诺。因此该证据只能修正当前判断，超界时 `PLATFORM-SECURITY` 必须拒绝 effect commit 并转 sandbox/人工。
<!-- analysis-decision:SF-2026-ARXIV-2606-29282:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29296:start -->
未入选长叙事：把策略更新的通过条件与样本级失败信号结合，改变 reward gate。《Process Advantage Signal Shaping: A Paradigm-Agnostic Middleware for Process-Supervised RL in LLM Reasoners》的正证据锚定 `Empirical scope; evaluation protocol`；`6 Discussion` 没有建立跨 reward/verifier、policy freshness 与分布漂移的 on-policy 有效性。因此该证据只能修正当前判断，超界时 `TRAIN-GRPO` 必须恢复 on-policy terminal/verifier baseline。
<!-- analysis-decision:SF-2026-ARXIV-2606-29296:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29315:start -->
未入选长叙事：把实验设计、工具执行、观测与假设修订组织成可复算工作流。《Hierarchical Experimentalist Agents》的正证据锚定 `4 Experiments and Results on Interphyre`；`A.5 Design Principles; domain-agnostic inputs and simulator-only evidence boundary` 没有建立跨 environment、tool semantics、checkpoint 与 compensation path 的可复算性。因此该证据只能修正当前判断，超界时 `AGENT-WORKFLOW` 必须停在可恢复 checkpoint 并执行 compensation。
<!-- analysis-decision:SF-2026-ARXIV-2606-29315:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29328:start -->
未入选长叙事：只证明六个 open-domain QA benchmark 上，把 K=200 candidate 的 k-context selection 改成多维 demand coverage 可改善 EM；理论 non-coverability 仅约束 query-proximity-monotone scorer，不直接约束 cross-encoder。sub-query drift、OT surrogate 成本或 corpus shift 失控时回退已校准 top-k/MMR。
<!-- analysis-decision:SF-2026-ARXIV-2606-29328:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29337:start -->
未入选长叙事：给 W4A4 量化的校准、kernel 与质量回退建立部署边界。《W4A4 Quantization for Inference on Wan2.2-I2V-A14B》的正证据锚定 `IV Evaluation and Results`；`IV-B Discussion` 没有建立跨 kernel、hardware、precision 与 graph revision 的执行计划可移植性。因此该证据只能修正当前判断，超界时 `INFER-TENSORRT-LLM` 必须恢复已验收 kernel/precision plan。
<!-- analysis-decision:SF-2026-ARXIV-2606-29337:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29340:start -->
未入选长叙事：把 off-policy 样本选择与策略漂移控制纳入训练状态。《PHF: Privileged Hidden Flow for On-Policy Self-Distillation》的正证据锚定 `Experiments`；`Discussion` 没有建立跨 reward/verifier、policy freshness 与分布漂移的 on-policy 有效性。因此该证据只能修正当前判断，超界时 `TRAIN-GRPO` 必须恢复 on-policy terminal/verifier baseline。
<!-- analysis-decision:SF-2026-ARXIV-2606-29340:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29350:start -->
未入选长叙事：把 VLA 视觉 token 合并与动作成功、延迟和回退共同校准。《Fast Enough to Act: Spatio-Temporal Visual Token Merging for Low-Latency Robotic VLMs and VLAs》的正证据锚定 `IV Experiments`；`V Conclusion and Discussion` 没有建立跨 embodiment、sensor、latency 与闭环干预的动作成功率。因此该证据只能修正当前判断，超界时 `MULTIMODAL-EMBODIED-VLA` 必须拒绝物理提交并交回保守 controller。
<!-- analysis-decision:SF-2026-ARXIV-2606-29350:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29354:start -->
未入选长叙事：把符号消息协议作为多 Agent 共享状态而非自由文本旁路。《When LLMs Develop Languages: Symbolic Communication for Efficient Multi-Agent Reasoning》的正证据锚定 `4 Experiments`；`5 Conclusion and Limitations` 没有建立跨 agent population、message protocol、error correlation 与 coordination load 的聚合收益。因此该证据只能修正当前判断，超界时 `AGENT-MULTI-AGENT` 必须恢复单 Agent/串行协调与人工仲裁。
<!-- analysis-decision:SF-2026-ARXIV-2606-29354:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29366:start -->
未入选长叙事：把 LLM 建议置于 solver 验证与可执行证据之后。《Solver-Verified Formulation Generation and Selection for Multi-Warehouse Inventory Allocation Using Large Language Models》的正证据锚定 `6 Computational Evaluation`；`Conclusion and solver-coverage boundary` 没有建立跨 environment、tool semantics、checkpoint 与 compensation path 的可复算性。因此该证据只能修正当前判断，超界时 `AGENT-WORKFLOW` 必须停在可恢复 checkpoint 并执行 compensation。
<!-- analysis-decision:SF-2026-ARXIV-2606-29366:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29377:start -->
未入选长叙事：把检索失败诊断、查询修复与证据重取变成循环控制。《Diagnosing and Repairing Factual Errors in RAG under Budget Constraints》的正证据锚定 `3 Experiments`；`Conclusion and evaluated-query scope` 没有建立跨 corpus、query distribution、retriever/index revision 与生成器的检索收益。因此该证据只能修正当前判断，超界时 `AGENT-RAG` 必须恢复固定、已校准的 retrieval plan。
<!-- analysis-decision:SF-2026-ARXIV-2606-29377:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29399:start -->
未入选长叙事：把多模态文档索引、跨页证据与推理计划联结。《LLM-Guided Planning for Multi-hop Reasoning over Multimodal Nuclear Regulatory Documents》的正证据锚定 `Experiments and multimodal document evaluation`；`7 Limitations` 没有建立跨 corpus、query distribution、retriever/index revision 与生成器的检索收益。因此该证据只能修正当前判断，超界时 `AGENT-RAG` 必须恢复固定、已校准的 retrieval plan。
<!-- analysis-decision:SF-2026-ARXIV-2606-29399:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29403:start -->
未入选长叙事：把 conformal coverage 与拒答/发布阈值绑定。《Self-Organized Conformal Prediction: Reducing Regional Coverage Gaps with Unsupervised Group Discovery》的正证据锚定 `4 Experiments`；`Conclusion and exchangeability boundary` 没有建立跨 dataset/model/evaluator revision 的 release acceptance 或生产 SLO。因此该证据只能修正当前判断，超界时 `PLATFORM-EVALUATION-SYSTEM` 必须保持 release Gate Open 并恢复完整分层评测。
<!-- analysis-decision:SF-2026-ARXIV-2606-29403:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29424:start -->
未入选长叙事：让 router 持有请求熵、专家选择与负载降级状态。《EntroRouter: Learning Efficient Model Routing via Entropy Regulation》的正证据锚定 `4 Experiments`；`5 Discussion` 没有建立跨 topology、并发负载、thermal state 与 SLO 的调度收益。因此该证据只能修正当前判断，超界时 `INFER-SCHEDULING` 必须恢复静态 placement 与保守 SLO headroom。
<!-- analysis-decision:SF-2026-ARXIV-2606-29424:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29425:start -->
未入选长叙事：把辩论者选择与聚合权重变成可校准协调状态。《Mixture of Debaters: Learn to Debate at Architectural Level in Multi-Agent Reasoning》的正证据锚定 `4 Experiments`；`Conclusion and tested-debater scope` 没有建立跨 agent population、message protocol、error correlation 与 coordination load 的聚合收益。因此该证据只能修正当前判断，超界时 `AGENT-MULTI-AGENT` 必须恢复单 Agent/串行协调与人工仲裁。
<!-- analysis-decision:SF-2026-ARXIV-2606-29425:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29441:start -->
未入选长叙事：把 activation defense 的检测、干预与失效边界置于运行时控制面。《Closing the Activation-Cone Blind Spot: Response-Time Probing and Unified Defense》的正证据锚定 `4 Experimental Setup; 5.1 No Single-Mechanism Paradigm Dominates`；`6 Discussion and Limitations` 没有建立跨 threat distribution、attacker adaptation 与 effect-time authorization 的防护承诺。因此该证据只能修正当前判断，超界时 `PLATFORM-SECURITY` 必须拒绝 effect commit 并转 sandbox/人工。
<!-- analysis-decision:SF-2026-ARXIV-2606-29441:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29445:start -->
未入选长叙事：把视频 GUI Agent 的长程观测与操作副作用纳入端到端评测。《Bridging VideoQA and Video-Guided Agentic Tasks via Generalized Keyframe Extraction》的正证据锚定 `4 Experiments`；`Conclusion and benchmark-domain scope` 没有建立跨 dataset/model/evaluator revision 的 release acceptance 或生产 SLO。因此该证据只能修正当前判断，超界时 `PLATFORM-EVALUATION-SYSTEM` 必须保持 release Gate Open 并恢复完整分层评测。
<!-- analysis-decision:SF-2026-ARXIV-2606-29445:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29472:start -->
未入选长叙事：只覆盖 DynaCU-Bench 浏览器任务与已测 CU models；Gemini 3 Flash 上 keyframe image-token dilution 已构成反例，因此 AOI 不是固定 bundle，也未证明桌面 OS、权限副作用或持续会议场景安全。退回高保真 capture 与人工确认。
<!-- analysis-decision:SF-2026-ARXIV-2606-29472:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29476:start -->
未入选长叙事：把 reward 构造与可验证约束结合并保留失败样本。《CRAFT: Counterfactual Credit Assignment from Free Sibling Rollouts for Self-Distilled Agentic Reinforcement Learning》的正证据锚定 `5 Experiments`；`7 Discussion and Limitations` 没有建立跨 reward/verifier、policy freshness 与分布漂移的 on-policy 有效性。因此该证据只能修正当前判断，超界时 `TRAIN-GRPO` 必须恢复 on-policy terminal/verifier baseline。
<!-- analysis-decision:SF-2026-ARXIV-2606-29476:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29481:start -->
未入选长叙事：按难度与策略状态控制 rollout 采样和更新。《To Reason or to Fabricate: Reasoning Without Shortcuts via Hint-Anchored Pairwise Aggregation》的正证据锚定 `3 Experimental Setup`；`2.2 Direct KL Optimization and Its Limitations` 没有建立跨 reward/verifier、policy freshness 与分布漂移的 on-policy 有效性。因此该证据只能修正当前判断，超界时 `TRAIN-GRPO` 必须恢复 on-policy terminal/verifier baseline。
<!-- analysis-decision:SF-2026-ARXIV-2606-29481:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29490:start -->
未入选长叙事：把置信承诺、校准误差与拒答决策绑定。《Reported Confidence in LLMs Tracks Commitment More Than Correctness》的正证据锚定 `1.2 Supplemental Results`；`Conclusion and evaluated-distribution scope` 没有建立跨 dataset/model/evaluator revision 的 release acceptance 或生产 SLO。因此该证据只能修正当前判断，超界时 `PLATFORM-EVALUATION-SYSTEM` 必须保持 release Gate Open 并恢复完整分层评测。
<!-- analysis-decision:SF-2026-ARXIV-2606-29490:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29493:start -->
未入选长叙事：把形式化 benchmark 的语义正确与语法通过分层审计。《Faults in Our Formal Benchmarking: Dataset Defects and Evaluation Failures in Lean Theorem Proving》的正证据锚定 `2 What Formal Benchmarking Certifies (and What It Does Not)`；`7 Limitations` 没有建立跨 dataset/model/evaluator revision 的 release acceptance 或生产 SLO。因此该证据只能修正当前判断，超界时 `PLATFORM-EVALUATION-SYSTEM` 必须保持 release Gate Open 并恢复完整分层评测。
<!-- analysis-decision:SF-2026-ARXIV-2606-29493:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29501:start -->
未入选长叙事：把 action-conditioned rollout 与可干预世界状态联结。《Learning Transferable Dynamics Priors from Action to World Modeling》的正证据锚定 `4 Experiments`；`4.5 Ablations and discussions` 没有建立跨 environment、observation dynamics 与 physical commit 的 rollout fidelity。因此该证据只能修正当前判断，超界时 `MULTIMODAL-WORLD-MODELS` 必须停止 imagined rollout 并请求真实 observation。
<!-- analysis-decision:SF-2026-ARXIV-2606-29501:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29502:start -->
未入选长叙事：把技能发现、组合与持久化变成可更新 Agent 状态。《UCOB: Learning to Utilize and Evolve Agentic Skills via Credit-Aware On-Policy Bidirectional Self-Distillation》的正证据锚定 `6 Experiments`；`Conclusion and evaluated-environment boundary` 没有建立跨 workload、write policy、retention horizon 与 provenance shift 的记忆收益。因此该证据只能修正当前判断，超界时 `AGENT-MEMORY` 必须拒绝写入并保留旧 memory revision。
<!-- analysis-decision:SF-2026-ARXIV-2606-29502:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29506:start -->
未入选长叙事：揭示跨数据集切分污染并改变 benchmark release contract。《Benchmark AUC Is Not Deployable Reliability: A Cross-Dataset Audit of Off-the-Shelf Features for Surveillance Video Anomaly Detection》的正证据锚定 `IV Results`；`VII Discussion` 没有建立跨 dataset/model/evaluator revision 的 release acceptance 或生产 SLO。因此该证据只能修正当前判断，超界时 `PLATFORM-EVALUATION-SYSTEM` 必须保持 release Gate Open 并恢复完整分层评测。
<!-- analysis-decision:SF-2026-ARXIV-2606-29506:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29520:start -->
未入选长叙事：把安全知识、执行与拒答分层测量。《SAKE: Software Architectural Knowledge Evaluation Benchmark for Large Language Models》的正证据锚定 `Benchmark construction and evaluation`；`7 Threats to Validity` 没有建立跨 dataset/model/evaluator revision 的 release acceptance 或生产 SLO。因此该证据只能修正当前判断，超界时 `PLATFORM-EVALUATION-SYSTEM` 必须保持 release Gate Open 并恢复完整分层评测。
<!-- analysis-decision:SF-2026-ARXIV-2606-29520:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29522:start -->
未入选长叙事：只在 Q8/D8 合成 transition task、Qwen2.5-Coder-7B 与 Mistral-7B-v0.3 上证明特定 written state 被因果读取；显式 scratchpad 的其他 token、自然语言推理和真实 Agent memory 均未被证明忠实。probe 不稳定时保留原文本与外部 verifier。
<!-- analysis-decision:SF-2026-ARXIV-2606-29522:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29526:start -->
未入选长叙事：把多阶段策略改进与验证门控组织成训练控制流。《The Mirage of Optimizing Training Policies: Monotonic Inference Policies as the Real Objective for LLM Reinforcement Learning》的正证据锚定 `5 Experiments`；`Limitations` 没有建立跨 reward/verifier、policy freshness 与分布漂移的 on-policy 有效性。因此该证据只能修正当前判断，超界时 `TRAIN-GRPO` 必须恢复 on-policy terminal/verifier baseline。
<!-- analysis-decision:SF-2026-ARXIV-2606-29526:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29532:start -->
未入选长叙事：把语义 join 的候选生成、验证与代价纳入查询计划。《SemJoin: Semantic Join Optimization》的正证据锚定 `4 Evaluation`；`Conclusion and evaluated-database scope` 没有建立跨 corpus、query distribution、retriever/index revision 与生成器的检索收益。因此该证据只能修正当前判断，超界时 `AGENT-RAG` 必须恢复固定、已校准的 retrieval plan。
<!-- analysis-decision:SF-2026-ARXIV-2606-29532:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29537:start -->
未入选长叙事：把 OSWorld 环境、任务与判定器升级为版本化 release contract。《OSWorld 2.0: Benchmarking Computer Use Agents on Long-Horizon Real-World Tasks》的正证据锚定 `2 OSWorld 2.0 Benchmark; evaluation protocol`；`6 Limitations` 没有建立跨 dataset/model/evaluator revision 的 release acceptance 或生产 SLO。因此该证据只能修正当前判断，超界时 `PLATFORM-EVALUATION-SYSTEM` 必须保持 release Gate Open 并恢复完整分层评测。
<!-- analysis-decision:SF-2026-ARXIV-2606-29537:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29538:start -->
未入选长叙事：把资源发现转成可执行 skill，并保留权限与失败边界。《RESOURCE2SKILL: Distilling Executable Agent Skills from Human-Created Multimodal Resources》的正证据锚定 `4 Experiments`；`M Limitations` 没有建立跨 environment、tool semantics、checkpoint 与 compensation path 的可复算性。因此该证据只能修正当前判断，超界时 `AGENT-WORKFLOW` 必须停在可恢复 checkpoint 并执行 compensation。
<!-- analysis-decision:SF-2026-ARXIV-2606-29538:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29541:start -->
未入选长叙事：把 MARL 协调的共享意图与通信失效纳入状态。《Learned Coordination Conventions in Cooperative MARL: Measuring the Translation Gap Between Theory-Informed Roles and Learned Routing》的正证据锚定 `5 Experiments`；`6 Discussion` 没有建立跨 agent population、message protocol、error correlation 与 coordination load 的聚合收益。因此该证据只能修正当前判断，超界时 `AGENT-MULTI-AGENT` 必须恢复单 Agent/串行协调与人工仲裁。
<!-- analysis-decision:SF-2026-ARXIV-2606-29541:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29544:start -->
未入选长叙事：把生产分布漂移、攻击与回退纳入鲁棒性发布证据。《Proteus: Automated Adversarial Robustness Testing for Audio Deepfake Detectors》的正证据锚定 `3 Results`；`Conclusion and tested-shift boundary` 没有建立跨 threat distribution、attacker adaptation 与 effect-time authorization 的防护承诺。因此该证据只能修正当前判断，超界时 `PLATFORM-SECURITY` 必须拒绝 effect commit 并转 sandbox/人工。
<!-- analysis-decision:SF-2026-ARXIV-2606-29544:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29554:start -->
未入选长叙事：揭示数据 shuffle 与 optimizer state 的耦合，改变复现合同。《Optimizer Memory Makes Shuffle Order a First-Order Source of Fine-Tuning Noise》的正证据锚定 `5 Empirical evidence`；`7 Discussion` 没有建立跨 architecture、optimizer、token budget 与更大训练尺度的可迁移性。因此该证据只能修正当前判断，超界时 `TRAIN-PRETRAINING` 必须恢复邻近规模 sweep 与已验证 schedule。
<!-- analysis-decision:SF-2026-ARXIV-2606-29554:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29563:start -->
未入选长叙事：用跨头跨层 coverage 状态驱动 KV 驱逐并保留完整缓存回退。《Coverage-Driven KV Cache Eviction for Efficient and Improved Inference of LLM》的正证据锚定 `5 Experiments; 5.1 Experimental setup`；`5.3 Discussion; 5.3.5 Computational Complexity` 没有建立跨 attention pattern、context length 与 workload shift 的 eviction 安全性。因此该证据只能修正当前判断，超界时 `INFER-KV-CACHE` 必须恢复完整 KV 或保守 eviction。
<!-- analysis-decision:SF-2026-ARXIV-2606-29563:end -->

<!-- analysis:DA-20260629-2606-29565:start -->
入选：只在 LayerScale 专有 engine、单 H100、70B-class 4-bit target 上测得 capability-gated fast path；8B BF16 不触发 gate，且大量收益为测量常数上的闭式推导。任何 state mutation 或置信漂移都必须 invalidate 并恢复普通 decode。
<!-- analysis:DA-20260629-2606-29565:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29567:start -->
未入选长叙事：把 PII 替身生成、加密映射与还原置于本地代理控制面。《SurrogateShield: Beyond Redaction for High-Utility, Privacy-Preserving LLM Interactions》的正证据锚定 `4 Evaluation Methodology`；`6 Discussion` 没有建立跨 threat distribution、attacker adaptation 与 effect-time authorization 的防护承诺。因此该证据只能修正当前判断，超界时 `PLATFORM-SECURITY` 必须拒绝 effect commit 并转 sandbox/人工。
<!-- analysis-decision:SF-2026-ARXIV-2606-29567:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29571:start -->
未入选长叙事：只比较 19 个 parameter-free metric、19 encoder 与七个静态数据集；0.01 crowded split、dominant-direction removal 和相关性未证明在线 corpus 漂移下的因果门槛，也未覆盖 learned metric。收益消失时恢复已校准 cosine/混合检索。
<!-- analysis-decision:SF-2026-ARXIV-2606-29571:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29573:start -->
未入选长叙事：把多模态生成粒度与可靠性共同纳入发布阈值。《Reliability-Prioritized Fine-Grained Generation in Multimodal Large》的正证据锚定 `2.1 MLLM Benchmarks; experiments`；`Conclusion and expert-verified benchmark scope` 没有建立跨 dataset/model/evaluator revision 的 release acceptance 或生产 SLO。因此该证据只能修正当前判断，超界时 `PLATFORM-EVALUATION-SYSTEM` 必须保持 release Gate Open 并恢复完整分层评测。
<!-- analysis-decision:SF-2026-ARXIV-2606-29573:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29580:start -->
未入选长叙事：把离线索引、设备内生成、citation 与语料缺口串成端侧 RAG 合同。《MAM-AI: An On-Device Medical Retrieval-Augmented Generation System for Nurses and Midwives in Zanzibar》的正证据锚定 `4 Evaluation Methodology; Sections 5-8 component results`；`9 Discussion; 10 Limitations and Future Work` 没有建立跨 corpus、query distribution、retriever/index revision 与生成器的检索收益。因此该证据只能修正当前判断，超界时 `AGENT-RAG` 必须恢复固定、已校准的 retrieval plan。
<!-- analysis-decision:SF-2026-ARXIV-2606-29580:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29581:start -->
未入选长叙事：当前 official exact-v1 的 Abstract 与 §3 一致披露 9 models、161 configurations、AdvBench+XSTest 与约 322k responses；证据只覆盖以 Pile validation calibration 的 AWQ INT4/GPTQ INT8、2B–8B 模型与静态 AdvBench，未证明 NF4/GGUF/对抗式 calibration、>70B、adaptive jailbreak/prompt injection 或 judge 完美可靠。任一切片回归即恢复已验收 precision/sampler。
<!-- analysis-decision:SF-2026-ARXIV-2606-29581:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29592:start -->
未入选长叙事：把 perception、navigation、planning 与剂量预算解耦评测。《STEMGym: Benchmarking Sequential Decision-Making under Dose Budgets in Autonomous Electron Microscopy》的正证据锚定 `4 Experiments`；`5 Limitations` 没有建立跨 dataset/model/evaluator revision 的 release acceptance 或生产 SLO。因此该证据只能修正当前判断，超界时 `PLATFORM-EVALUATION-SYSTEM` 必须保持 release Gate Open 并恢复完整分层评测。
<!-- analysis-decision:SF-2026-ARXIV-2606-29592:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29601:start -->
未入选长叙事：只验证有限 Langshaw examples 到 BSPL tableau 的 safety/liveness 与编译时间；未证明开放网络中的 delivery、identity、Byzantine role 或工具副作用。协议编译/验证超界时回到串行 coordinator 与人工仲裁。
<!-- analysis-decision:SF-2026-ARXIV-2606-29601:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29602:start -->
未入选长叙事：把多语言、编码与多阶段 prompt injection 纳入威胁矩阵。《An Empirical Evaluation of Prompt Injection Vulnerabilities in Large Language Models Across Multilingual and Obfuscated Attack Scenarios》的正证据锚定 `II-D Empirical Evaluations of LLM Safety; IV Results`；`V Discussion` 没有建立跨 threat distribution、attacker adaptation 与 effect-time authorization 的防护承诺。因此该证据只能修正当前判断，超界时 `PLATFORM-SECURITY` 必须拒绝 effect commit 并转 sandbox/人工。
<!-- analysis-decision:SF-2026-ARXIV-2606-29602:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29604:start -->
未入选长叙事：把权重/激活扰动用于潜在行为发现并定义代理选择边界。《Mechanistically Eliciting Latent Behaviors in Language Models》的正证据锚定 `Experimental setup; latent-behavior evaluation`；`Conclusion and model-organism scope` 没有建立跨 threat distribution、attacker adaptation 与 effect-time authorization 的防护承诺。因此该证据只能修正当前判断，超界时 `PLATFORM-SECURITY` 必须拒绝 effect commit 并转 sandbox/人工。
<!-- analysis-decision:SF-2026-ARXIV-2606-29604:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29605:start -->
未入选长叙事：把生成语料的 provenance、复制与跨记录冗余转成训练前数据控制状态。《How much of an LLM-generated clinical corpus is actually new? A production-scale measurement of content redundancy for provenance classification》的正证据锚定 `2 Results; downstream equal-token adaptation test`；`3 Discussion` 没有建立跨 corpus、训练阶段与真实删除/重训操作的因果有效性。因此该证据只能修正当前判断，超界时 `TRAIN-DATA` 必须保留原样本、lineage 与重训对照。
<!-- analysis-decision:SF-2026-ARXIV-2606-29605:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29623:start -->
未入选长叙事：MNIST 与 Llama-Guard hidden-state jailbreak fleet 只验证经校准 ruler 的 rare-event estimate；论文明确指出 behavioral fleet 约 2,000 variants 仍不足、Mahalanobis ruler 可结构性失效，跨 corpus 必须重新校准。否则 Gate 保持 Open。
<!-- analysis-decision:SF-2026-ARXIV-2606-29623:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29629:start -->
未入选长叙事：让软件 DVFS controller 持有多模态 serving 阶段、功耗与热状态。《Energy-Efficient Multimodal Inference Serving with Tri-serve》的正证据锚定 `II-C1 Frequency-locked Roofline Benchmarking; IV Evaluation`；`V Conclusion; evaluated Qwen-Omni/GPU-cluster boundary` 没有建立跨 topology、并发负载、thermal state 与 SLO 的调度收益。因此该证据只能修正当前判断，超界时 `INFER-SCHEDULING` 必须恢复静态 placement 与保守 SLO headroom。
<!-- analysis-decision:SF-2026-ARXIV-2606-29629:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29645:start -->
未入选长叙事：把 metadata、结构与 multi-hop strategy 分解为可单独验收的 RAG 控制变量。《Metadata, Structure, or Strategy? A Decomposition of RAG Context Enrichment》的正证据锚定 `3.2 Experimental Design; results across six benchmarks`；`6.1 Limitations` 没有建立跨 corpus、query distribution、retriever/index revision 与生成器的检索收益。因此该证据只能修正当前判断，超界时 `AGENT-RAG` 必须恢复固定、已校准的 retrieval plan。
<!-- analysis-decision:SF-2026-ARXIV-2606-29645:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29646:start -->
未入选长叙事：把 sleeper behavior elicitation 的 fuzzing、代理调参与 oracle 边界分开。《Fuzzing Large Language Models to Elicit Hidden Behaviours》的正证据锚定 `3 Results`；`4 Discussion` 没有建立跨 threat distribution、attacker adaptation 与 effect-time authorization 的防护承诺。因此该证据只能修正当前判断，超界时 `PLATFORM-SECURITY` 必须拒绝 effect commit 并转 sandbox/人工。
<!-- analysis-decision:SF-2026-ARXIV-2606-29646:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29648:start -->
未入选长叙事：让 meta-agent 从失败轨迹重写多检索器编排策略。《Hybrid Retriever Evolution for Multimodal Document Reasoning Agents》的正证据锚定 `4 Experiments`；`A Limitations` 没有建立跨 corpus、query distribution、retriever/index revision 与生成器的检索收益。因此该证据只能修正当前判断，超界时 `AGENT-RAG` 必须恢复固定、已校准的 retrieval plan。
<!-- analysis-decision:SF-2026-ARXIV-2606-29648:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29649:start -->
未入选长叙事：把分辨率、字符构造与语言纳入 VLM moderation 威胁面。《Resolution Thresholds in VLM Detection of Harmful ASCII Art Across Construction Modes and Languages》的正证据锚定 `3.2 VLM Evaluation`；`5 Discussion` 没有建立跨 threat distribution、attacker adaptation 与 effect-time authorization 的防护承诺。因此该证据只能修正当前判断，超界时 `PLATFORM-SECURITY` 必须拒绝 effect commit 并转 sandbox/人工。
<!-- analysis-decision:SF-2026-ARXIV-2606-29649:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29652:start -->
未入选长叙事：把索引、模型与推理默认置于用户设备，并把远端服务降为可选路径。《As We May Search》的正证据锚定 `4.1 Experimental Setup; five benchmarks and 1K-1M documents`；`4.11 Limitations` 没有建立跨 corpus、query distribution、retriever/index revision 与生成器的检索收益。因此该证据只能修正当前判断，超界时 `AGENT-RAG` 必须恢复固定、已校准的 retrieval plan。
<!-- analysis-decision:SF-2026-ARXIV-2606-29652:end -->

<!-- analysis:DA-20260629-2606-29654:start -->
入选：保证依赖 local bias envelope、representation-gap bound 与 calibration split，并非 distribution-free；六个选择题 benchmark 与训练期 difficulty-normalized budget 未证明开放式任务或分布漂移。诊断失败时全 defer/人工。
<!-- analysis:DA-20260629-2606-29654:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29657:start -->
未入选长叙事：把预测器训练与下游行动奖励隔离，并把 agency 留给受约束 scaffolding。《Safety from Honesty in a Disinterested AI Predictor》的正证据锚定 `Formal safety argument and falsifiability analysis`；`5.4.2 Falsifiability, Scope, and Requirements for a Concrete Design` 没有建立跨 threat distribution、attacker adaptation 与 effect-time authorization 的防护承诺。因此该证据只能修正当前判断，超界时 `PLATFORM-SECURITY` 必须拒绝 effect commit 并转 sandbox/人工。
<!-- analysis-decision:SF-2026-ARXIV-2606-29657:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29661:start -->
未入选长叙事：让 ensemble controller 同时优化预测质量与跨模型错误多样性。《Diversity is the Strength of the AI Crowd》的正证据锚定 `5 Results`；`6 Discussion` 没有建立跨 agent population、message protocol、error correlation 与 coordination load 的聚合收益。因此该证据只能修正当前判断，超界时 `AGENT-MULTI-AGENT` 必须恢复单 Agent/串行协调与人工仲裁。
<!-- analysis-decision:SF-2026-ARXIV-2606-29661:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29679:start -->
未入选长叙事：用表示距离矩阵轨迹监测训练相变，而非只观察标量 loss。《Learning as Observable Matrix Dynamics: Diffusive Relaxations versus Phase Transitions》的正证据锚定 `4 Experiments`；`6 Discussion` 没有建立跨 workload、signal drift 与告警副作用的生产检测率。因此该证据只能修正当前判断，超界时 `PLATFORM-MONITORING` 必须只保留 observe-only 告警并请求重新校准。
<!-- analysis-decision:SF-2026-ARXIV-2606-29679:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-30686:start -->
未入选长叙事：把 VLA 的语义匹配与物理动作泛化拆成可识别因果评测。《Position: Vision-Language-Action Models Cannot Be Verified to Perform Physical Reasoning》的正证据锚定 `3.2 Three Levels of Non-Identifiability in Current Evaluation`；`Conclusion and proposed controlled-variation scope` 没有建立跨 dataset/model/evaluator revision 的 release acceptance 或生产 SLO。因此该证据只能修正当前判断，超界时 `PLATFORM-EVALUATION-SYSTEM` 必须保持 release Gate Open 并恢复完整分层评测。
<!-- analysis-decision:SF-2026-ARXIV-2606-30686:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-30689:start -->
未入选长叙事：把逐行需求 citation 变成可自动检测幻觉的 provenance 合同。《Citation Discipline in Spec-Driven Development: A Cross-Model Empirical Study of Output Determinism and Automated Hallucination Detection in LLM-Generated Code》的正证据锚定 `4 Experimental Design; cross-model results`；`7 Discussion` 没有建立跨 environment、tool semantics、checkpoint 与 compensation path 的可复算性。因此该证据只能修正当前判断，超界时 `AGENT-WORKFLOW` 必须停在可恢复 checkpoint 并执行 compensation。
<!-- analysis-decision:SF-2026-ARXIV-2606-30689:end -->

### DA-20260629-2606-29151
CADENZA 将 semantic query 的 task-specific operator DAG、逻辑重写、异构 backend routing 与 quality-latency-cost 共同纳入 query planner。

### DA-20260629-2606-29565
Speculative pre-positioning 把 stateful session 的空闲期变成跨请求预推进窗口，同时要求 confidence gate 管理 false accept。

### DA-20260629-2606-29654
Budgeted act-or-defer 将 wrong-action budget 变成多 Agent deliberation 的前置运行点，而不是事后阈值搜索。

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-29150 | INFER-DECODE | books/part-05-inference-system/44-decode.md#L31 | books/part-05-inference-system/43-prefill.md#L297 | existing:SF-2026-ARXIV-2606-29150 | delta:SF-2026-ARXIV-2606-29150 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29150 |
| SF-2026-ARXIV-2606-29151 | AGENT-RAG | books/part-07-agent/76-rag.md#L51 | books/part-07-agent/77-memory.md#L1017 | existing:SF-2026-ARXIV-2606-29151 | delta:SF-2026-ARXIV-2606-29151 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-29151 |
| SF-2026-ARXIV-2606-29158 | TRAIN-PRETRAINING | books/part-04-training-system/28-pretraining.md#L263 | books/part-04-training-system/27-data.md#L591 | existing:SF-2026-ARXIV-2606-29158 | delta:SF-2026-ARXIV-2606-29158 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-29158 |
| SF-2026-ARXIV-2606-29159 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L193 | books/part-06-ai-infrastructure/59-model-registry.md#L144 | existing:SF-2026-ARXIV-2606-29159 | delta:SF-2026-ARXIV-2606-29159 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29159 |
| SF-2026-ARXIV-2606-29171 | TRAIN-DATA | books/part-04-training-system/27-data.md#L484 | books/part-04-training-system/28-pretraining.md#L702 | existing:SF-2026-ARXIV-2606-29171 | delta:SF-2026-ARXIV-2606-29171 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-29171 |
| SF-2026-ARXIV-2606-29176 | TRAIN-PRETRAINING | books/part-04-training-system/28-pretraining.md#L263 | books/part-04-training-system/27-data.md#L591 | existing:SF-2026-ARXIV-2606-29176 | delta:SF-2026-ARXIV-2606-29176 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29176 |
| SF-2026-ARXIV-2606-29178 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L46 | books/part-07-agent/76-rag.md#L393 | existing:SF-2026-ARXIV-2606-29178 | delta:SF-2026-ARXIV-2606-29178 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29178 |
| SF-2026-ARXIV-2606-29182 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#L36 | books/part-07-agent/78-tool-calling.md#L301 | existing:SF-2026-ARXIV-2606-29182 | delta:SF-2026-ARXIV-2606-29182 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29182 |
| SF-2026-ARXIV-2606-29184 | TRAIN-LORA | books/part-04-training-system/30-lora.md#L145 | books/part-04-training-system/29-sft.md#L494 | existing:SF-2026-ARXIV-2606-29184 | delta:SF-2026-ARXIV-2606-29184 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29184 |
| SF-2026-ARXIV-2606-29193 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L193 | books/part-06-ai-infrastructure/59-model-registry.md#L144 | existing:SF-2026-ARXIV-2606-29193 | delta:SF-2026-ARXIV-2606-29193 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29193 |
| SF-2026-ARXIV-2606-29196 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L193 | books/part-06-ai-infrastructure/59-model-registry.md#L144 | existing:SF-2026-ARXIV-2606-29196 | delta:SF-2026-ARXIV-2606-29196 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-29196 |
| SF-2026-ARXIV-2606-29207 | INFER-DECODE | books/part-05-inference-system/44-decode.md#L31 | books/part-05-inference-system/43-prefill.md#L297 | existing:SF-2026-ARXIV-2606-29207 | delta:SF-2026-ARXIV-2606-29207 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29207 |
| SF-2026-ARXIV-2606-29215 | INFER-DECODE | books/part-05-inference-system/44-decode.md#L31 | books/part-05-inference-system/43-prefill.md#L297 | existing:SF-2026-ARXIV-2606-29215 | delta:SF-2026-ARXIV-2606-29215 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29215 |
| SF-2026-ARXIV-2606-29222 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L171 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L514 | existing:SF-2026-ARXIV-2606-29222 | delta:SF-2026-ARXIV-2606-29222 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29222 |
| SF-2026-ARXIV-2606-29223 | INFER-DECODE | books/part-05-inference-system/44-decode.md#L31 | books/part-05-inference-system/43-prefill.md#L297 | existing:SF-2026-ARXIV-2606-29223 | delta:SF-2026-ARXIV-2606-29223 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29223 |
| SF-2026-ARXIV-2606-29225 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L418 | books/part-06-ai-infrastructure/71-multi-tenant.md#L120 | existing:SF-2026-ARXIV-2606-29225 | delta:SF-2026-ARXIV-2606-29225 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29225 |
| SF-2026-ARXIV-2606-29228 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L193 | books/part-06-ai-infrastructure/59-model-registry.md#L144 | existing:SF-2026-ARXIV-2606-29228 | delta:SF-2026-ARXIV-2606-29228 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29228 |
| SF-2026-ARXIV-2606-29237 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L189 | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L483 | existing:SF-2026-ARXIV-2606-29237 | delta:SF-2026-ARXIV-2606-29237 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29237 |
| SF-2026-ARXIV-2606-29238 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#L879 | books/part-04-training-system/32-ppo.md#L342 | existing:SF-2026-ARXIV-2606-29238 | delta:SF-2026-ARXIV-2606-29238 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29238 |
| SF-2026-ARXIV-2606-29239 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L418 | books/part-06-ai-infrastructure/71-multi-tenant.md#L120 | existing:SF-2026-ARXIV-2606-29239 | delta:SF-2026-ARXIV-2606-29239 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29239 |
| SF-2026-ARXIV-2606-29251 | AGENT-CONTEXT | books/part-07-agent/75-context.md#L16 | books/part-07-agent/74-prompt.md#L187 | existing:SF-2026-ARXIV-2606-29251 | delta:SF-2026-ARXIV-2606-29251 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29251 |
| SF-2026-ARXIV-2606-29270 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#L380 | books/part-07-agent/81-workflow.md#L702 | existing:SF-2026-ARXIV-2606-29270 | delta:SF-2026-ARXIV-2606-29270 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-29270 |
| SF-2026-ARXIV-2606-29275 | INFER-DECODE | books/part-05-inference-system/44-decode.md#L31 | books/part-05-inference-system/43-prefill.md#L297 | existing:SF-2026-ARXIV-2606-29275 | delta:SF-2026-ARXIV-2606-29275 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29275 |
| SF-2026-ARXIV-2606-29278 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L193 | books/part-06-ai-infrastructure/59-model-registry.md#L144 | existing:SF-2026-ARXIV-2606-29278 | delta:SF-2026-ARXIV-2606-29278 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29278 |
| SF-2026-ARXIV-2606-29279 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L46 | books/part-07-agent/76-rag.md#L393 | existing:SF-2026-ARXIV-2606-29279 | delta:SF-2026-ARXIV-2606-29279 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29279 |
| SF-2026-ARXIV-2606-29280 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L193 | books/part-06-ai-infrastructure/59-model-registry.md#L144 | existing:SF-2026-ARXIV-2606-29280 | delta:SF-2026-ARXIV-2606-29280 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29280 |
| SF-2026-ARXIV-2606-29282 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L418 | books/part-06-ai-infrastructure/71-multi-tenant.md#L120 | existing:SF-2026-ARXIV-2606-29282 | delta:SF-2026-ARXIV-2606-29282 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29282 |
| SF-2026-ARXIV-2606-29296 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#L879 | books/part-04-training-system/32-ppo.md#L342 | existing:SF-2026-ARXIV-2606-29296 | delta:SF-2026-ARXIV-2606-29296 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29296 |
| SF-2026-ARXIV-2606-29315 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#L36 | books/part-07-agent/78-tool-calling.md#L301 | existing:SF-2026-ARXIV-2606-29315 | delta:SF-2026-ARXIV-2606-29315 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29315 |
| SF-2026-ARXIV-2606-29328 | AGENT-RAG | books/part-07-agent/76-rag.md#L51 | books/part-07-agent/77-memory.md#L1017 | existing:SF-2026-ARXIV-2606-29328 | delta:SF-2026-ARXIV-2606-29328 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29328 |
| SF-2026-ARXIV-2606-29337 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#L394 | books/part-05-inference-system/48-speculative-decoding.md#L597 | existing:SF-2026-ARXIV-2606-29337 | delta:SF-2026-ARXIV-2606-29337 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29337 |
| SF-2026-ARXIV-2606-29340 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#L879 | books/part-04-training-system/32-ppo.md#L342 | existing:SF-2026-ARXIV-2606-29340 | delta:SF-2026-ARXIV-2606-29340 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29340 |
| SF-2026-ARXIV-2606-29350 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L171 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L514 | existing:SF-2026-ARXIV-2606-29350 | delta:SF-2026-ARXIV-2606-29350 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29350 |
| SF-2026-ARXIV-2606-29354 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#L380 | books/part-07-agent/81-workflow.md#L702 | existing:SF-2026-ARXIV-2606-29354 | delta:SF-2026-ARXIV-2606-29354 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29354 |
| SF-2026-ARXIV-2606-29366 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#L36 | books/part-07-agent/78-tool-calling.md#L301 | existing:SF-2026-ARXIV-2606-29366 | delta:SF-2026-ARXIV-2606-29366 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29366 |
| SF-2026-ARXIV-2606-29377 | AGENT-RAG | books/part-07-agent/76-rag.md#L51 | books/part-07-agent/77-memory.md#L1017 | existing:SF-2026-ARXIV-2606-29377 | delta:SF-2026-ARXIV-2606-29377 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29377 |
| SF-2026-ARXIV-2606-29403 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L193 | books/part-06-ai-infrastructure/59-model-registry.md#L144 | existing:SF-2026-ARXIV-2606-29403 | delta:SF-2026-ARXIV-2606-29403 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29403 |
| SF-2026-ARXIV-2606-29424 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#L183 | books/part-05-inference-system/46-continuous-batching.md#L216 | existing:SF-2026-ARXIV-2606-29424 | delta:SF-2026-ARXIV-2606-29424 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29424 |
| SF-2026-ARXIV-2606-29425 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#L380 | books/part-07-agent/81-workflow.md#L702 | existing:SF-2026-ARXIV-2606-29425 | delta:SF-2026-ARXIV-2606-29425 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29425 |
| SF-2026-ARXIV-2606-29441 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L418 | books/part-06-ai-infrastructure/71-multi-tenant.md#L120 | existing:SF-2026-ARXIV-2606-29441 | delta:SF-2026-ARXIV-2606-29441 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29441 |
| SF-2026-ARXIV-2606-29445 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L193 | books/part-06-ai-infrastructure/59-model-registry.md#L144 | existing:SF-2026-ARXIV-2606-29445 | delta:SF-2026-ARXIV-2606-29445 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29445 |
| SF-2026-ARXIV-2606-29472 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#L399 | books/part-07-agent/83-mcp.md#L229 | existing:SF-2026-ARXIV-2606-29472 | delta:SF-2026-ARXIV-2606-29472 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-29472 |
| SF-2026-ARXIV-2606-29476 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#L879 | books/part-04-training-system/32-ppo.md#L342 | existing:SF-2026-ARXIV-2606-29476 | delta:SF-2026-ARXIV-2606-29476 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29476 |
| SF-2026-ARXIV-2606-29481 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#L879 | books/part-04-training-system/32-ppo.md#L342 | existing:SF-2026-ARXIV-2606-29481 | delta:SF-2026-ARXIV-2606-29481 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29481 |
| SF-2026-ARXIV-2606-29490 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L193 | books/part-06-ai-infrastructure/59-model-registry.md#L144 | existing:SF-2026-ARXIV-2606-29490 | delta:SF-2026-ARXIV-2606-29490 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29490 |
| SF-2026-ARXIV-2606-29493 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L193 | books/part-06-ai-infrastructure/59-model-registry.md#L144 | existing:SF-2026-ARXIV-2606-29493 | delta:SF-2026-ARXIV-2606-29493 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29493 |
| SF-2026-ARXIV-2606-29501 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L189 | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L483 | existing:SF-2026-ARXIV-2606-29501 | delta:SF-2026-ARXIV-2606-29501 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29501 |
| SF-2026-ARXIV-2606-29502 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L46 | books/part-07-agent/76-rag.md#L393 | existing:SF-2026-ARXIV-2606-29502 | delta:SF-2026-ARXIV-2606-29502 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29502 |
| SF-2026-ARXIV-2606-29506 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L193 | books/part-06-ai-infrastructure/59-model-registry.md#L144 | existing:SF-2026-ARXIV-2606-29506 | delta:SF-2026-ARXIV-2606-29506 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29506 |
| SF-2026-ARXIV-2606-29520 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L193 | books/part-06-ai-infrastructure/59-model-registry.md#L144 | existing:SF-2026-ARXIV-2606-29520 | delta:SF-2026-ARXIV-2606-29520 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29520 |
| SF-2026-ARXIV-2606-29522 | AGENT-CONTEXT | books/part-07-agent/75-context.md#L16 | books/part-07-agent/74-prompt.md#L187 | existing:SF-2026-ARXIV-2606-29522 | delta:SF-2026-ARXIV-2606-29522 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-29522 |
| SF-2026-ARXIV-2606-29526 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#L879 | books/part-04-training-system/32-ppo.md#L342 | existing:SF-2026-ARXIV-2606-29526 | delta:SF-2026-ARXIV-2606-29526 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29526 |
| SF-2026-ARXIV-2606-29532 | AGENT-RAG | books/part-07-agent/76-rag.md#L51 | books/part-07-agent/77-memory.md#L1017 | existing:SF-2026-ARXIV-2606-29532 | delta:SF-2026-ARXIV-2606-29532 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29532 |
| SF-2026-ARXIV-2606-29537 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L193 | books/part-06-ai-infrastructure/59-model-registry.md#L144 | existing:SF-2026-ARXIV-2606-29537 | delta:SF-2026-ARXIV-2606-29537 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29537 |
| SF-2026-ARXIV-2606-29538 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#L36 | books/part-07-agent/78-tool-calling.md#L301 | existing:SF-2026-ARXIV-2606-29538 | delta:SF-2026-ARXIV-2606-29538 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29538 |
| SF-2026-ARXIV-2606-29541 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#L380 | books/part-07-agent/81-workflow.md#L702 | existing:SF-2026-ARXIV-2606-29541 | delta:SF-2026-ARXIV-2606-29541 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29541 |
| SF-2026-ARXIV-2606-29544 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L418 | books/part-06-ai-infrastructure/71-multi-tenant.md#L120 | existing:SF-2026-ARXIV-2606-29544 | delta:SF-2026-ARXIV-2606-29544 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29544 |
| SF-2026-ARXIV-2606-29554 | TRAIN-PRETRAINING | books/part-04-training-system/28-pretraining.md#L263 | books/part-04-training-system/27-data.md#L591 | existing:SF-2026-ARXIV-2606-29554 | delta:SF-2026-ARXIV-2606-29554 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29554 |
| SF-2026-ARXIV-2606-29563 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L222 | books/part-05-inference-system/44-decode.md#L222 | existing:SF-2026-ARXIV-2606-29563 | delta:SF-2026-ARXIV-2606-29563 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29563 |
| SF-2026-ARXIV-2606-29565 | INFER-REQUEST-LIFECYCLE | books/part-05-inference-system/42-what-happens-during-inference.md#L80 | books/part-05-inference-system/43-prefill.md#L297 | existing:SF-2026-ARXIV-2606-29565 | delta:SF-2026-ARXIV-2606-29565 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-29565 |
| SF-2026-ARXIV-2606-29567 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L418 | books/part-06-ai-infrastructure/71-multi-tenant.md#L120 | existing:SF-2026-ARXIV-2606-29567 | delta:SF-2026-ARXIV-2606-29567 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29567 |
| SF-2026-ARXIV-2606-29571 | AGENT-RAG | books/part-07-agent/76-rag.md#L51 | books/part-07-agent/77-memory.md#L1017 | existing:SF-2026-ARXIV-2606-29571 | delta:SF-2026-ARXIV-2606-29571 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-29571 |
| SF-2026-ARXIV-2606-29573 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L193 | books/part-06-ai-infrastructure/59-model-registry.md#L144 | existing:SF-2026-ARXIV-2606-29573 | delta:SF-2026-ARXIV-2606-29573 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29573 |
| SF-2026-ARXIV-2606-29581 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L418 | books/part-06-ai-infrastructure/71-multi-tenant.md#L120 | existing:SF-2026-ARXIV-2606-29581 | delta:SF-2026-ARXIV-2606-29581 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-29581 |
| SF-2026-ARXIV-2606-29601 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#L380 | books/part-07-agent/81-workflow.md#L702 | existing:SF-2026-ARXIV-2606-29601 | delta:SF-2026-ARXIV-2606-29601 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-29601 |
| SF-2026-ARXIV-2606-29602 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L418 | books/part-06-ai-infrastructure/71-multi-tenant.md#L120 | existing:SF-2026-ARXIV-2606-29602 | delta:SF-2026-ARXIV-2606-29602 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29602 |
| SF-2026-ARXIV-2606-29604 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L418 | books/part-06-ai-infrastructure/71-multi-tenant.md#L120 | existing:SF-2026-ARXIV-2606-29604 | delta:SF-2026-ARXIV-2606-29604 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29604 |
| SF-2026-ARXIV-2606-29605 | TRAIN-DATA | books/part-04-training-system/27-data.md#L484 | books/part-04-training-system/28-pretraining.md#L702 | existing:SF-2026-ARXIV-2606-29605 | delta:SF-2026-ARXIV-2606-29605 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29605 |
| SF-2026-ARXIV-2606-29623 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L193 | books/part-06-ai-infrastructure/59-model-registry.md#L144 | existing:SF-2026-ARXIV-2606-29623 | delta:SF-2026-ARXIV-2606-29623 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-29623 |
| SF-2026-ARXIV-2606-29629 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#L183 | books/part-05-inference-system/46-continuous-batching.md#L216 | existing:SF-2026-ARXIV-2606-29629 | delta:SF-2026-ARXIV-2606-29629 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29629 |
| SF-2026-ARXIV-2606-29645 | AGENT-RAG | books/part-07-agent/76-rag.md#L51 | books/part-07-agent/77-memory.md#L1017 | existing:SF-2026-ARXIV-2606-29645 | delta:SF-2026-ARXIV-2606-29645 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29645 |
| SF-2026-ARXIV-2606-29646 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L418 | books/part-06-ai-infrastructure/71-multi-tenant.md#L120 | existing:SF-2026-ARXIV-2606-29646 | delta:SF-2026-ARXIV-2606-29646 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29646 |
| SF-2026-ARXIV-2606-29648 | AGENT-RAG | books/part-07-agent/76-rag.md#L51 | books/part-07-agent/77-memory.md#L1017 | existing:SF-2026-ARXIV-2606-29648 | delta:SF-2026-ARXIV-2606-29648 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29648 |
| SF-2026-ARXIV-2606-29649 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L418 | books/part-06-ai-infrastructure/71-multi-tenant.md#L120 | existing:SF-2026-ARXIV-2606-29649 | delta:SF-2026-ARXIV-2606-29649 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29649 |
| SF-2026-ARXIV-2606-29652 | AGENT-RAG | books/part-07-agent/76-rag.md#L51 | books/part-07-agent/77-memory.md#L1017 | existing:SF-2026-ARXIV-2606-29652 | delta:SF-2026-ARXIV-2606-29652 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29652 |
| SF-2026-ARXIV-2606-29654 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#L380 | books/part-07-agent/81-workflow.md#L702 | existing:SF-2026-ARXIV-2606-29654 | delta:SF-2026-ARXIV-2606-29654 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-29654 |
| SF-2026-ARXIV-2606-29657 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L418 | books/part-06-ai-infrastructure/71-multi-tenant.md#L120 | existing:SF-2026-ARXIV-2606-29657 | delta:SF-2026-ARXIV-2606-29657 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29657 |
| SF-2026-ARXIV-2606-29661 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#L380 | books/part-07-agent/81-workflow.md#L702 | existing:SF-2026-ARXIV-2606-29661 | delta:SF-2026-ARXIV-2606-29661 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29661 |
| SF-2026-ARXIV-2606-30686 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L193 | books/part-06-ai-infrastructure/59-model-registry.md#L144 | existing:SF-2026-ARXIV-2606-30686 | delta:SF-2026-ARXIV-2606-30686 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-30686 |
| SF-2026-ARXIV-2606-30689 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#L36 | books/part-07-agent/78-tool-calling.md#L301 | existing:SF-2026-ARXIV-2606-30689 | delta:SF-2026-ARXIV-2606-30689 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-30689 |

<!-- existing:SF-2026-ARXIV-2606-29150:start -->
当前章已拥有 request-local decode/refinement state、停止条件与受验证执行路径。
<!-- existing:SF-2026-ARXIV-2606-29150:end -->
<!-- delta:SF-2026-ARXIV-2606-29150:start -->
把 flow reasoning 的中间状态、自验证与 test-time compute 变成推理时控制路径。
<!-- delta:SF-2026-ARXIV-2606-29150:end -->
<!-- books-review:SF-2026-ARXIV-2606-29150:start -->
已重读 `books/part-05-inference-system/44-decode.md#L31` 与相邻章 `books/part-05-inference-system/43-prefill.md#L297`；决定 `No Change — Existing Coverage`。把 flow reasoning 的中间状态、自验证与 test-time compute 变成推理时控制路径。《Flow Reasoning Models: Scaling Reasoning Through Iterative Self-Refinement》的正证据锚定 `4 Experiments; G Experimental setup and hyperparameters`；`6 Discussion; B Test-time scaling: coverage, selection, and sampling-step baselines` 没有建立跨 model、request shape、quality target 与 serving engine 的延迟-质量合同。因此该证据只能修正当前判断，超界时 `INFER-DECODE` 必须恢复已验证的普通 decode/refinement path。
<!-- books-review:SF-2026-ARXIV-2606-29150:end -->

<!-- existing:SF-2026-ARXIV-2606-29151:start -->
当前章已拥有 typed query plan、router、metric/index identity、evidence sufficiency 与失败回退。
<!-- existing:SF-2026-ARXIV-2606-29151:end -->
<!-- delta:SF-2026-ARXIV-2606-29151:start -->
旧 RAG 路径把自然语言直接送入固定 retriever；CADENZA 先编译 task-specific operator DAG，再由 logical rewrite 与 physical planner 按 quality/latency/cost 选择 backend。RAG owner 持有 DAG、operator identity 与 plan commit；统计或 backend profile 漂移时回退固定检索计划。
<!-- delta:SF-2026-ARXIV-2606-29151:end -->
<!-- books-review:SF-2026-ARXIV-2606-29151:start -->
已重读 `books/part-07-agent/76-rag.md#L51` 与相邻章 `books/part-07-agent/77-memory.md#L1017`；决定 `Integrate`。只证明 SemBench 上 intent-specific operator DAG 与异构 backend 的 quality/latency/cost 计划选择；未证明跨 operator 的联合最优、teacher-noise 之外的 label shift，或 Azure/API 与本地模型间可移植性。失配时固定到已校准 retrieval plan。
<!-- books-review:SF-2026-ARXIV-2606-29151:end -->

<!-- existing:SF-2026-ARXIV-2606-29158:start -->
当前章已把 optimizer、schedule、batch/tokens 与 scaling identity 分开；新证据只有改变外推或控制合同才可追加。
<!-- existing:SF-2026-ARXIV-2606-29158:end -->
<!-- delta:SF-2026-ARXIV-2606-29158:start -->
固定比例或单变量外推学习率会把 width、depth、token budget 与 schedule 的非线性交互折叠掉；训练控制面应把这些轴和 optimizer/schedule revision 一起冻结后再外推。额外 sweep 提高成本，超出已测尺度时回退邻近规模校准而非沿幂律盲推。
<!-- delta:SF-2026-ARXIV-2606-29158:end -->
<!-- books-review:SF-2026-ARXIV-2606-29158:start -->
已重读 `books/part-04-training-system/28-pretraining.md#L263` 与相邻章 `books/part-04-training-system/27-data.md#L591`；决定 `Integrate`。只覆盖 GPT-2-style 22M-707M、FineWeb 5B-100B tokens、WSD 与 AdamW/AdamH；论文明确显示 log-linear LR 仅局部成立，不能外推到其他架构、optimizer 或更大规模。超界时重新 sweep 邻近尺度。
<!-- books-review:SF-2026-ARXIV-2606-29158:end -->

<!-- existing:SF-2026-ARXIV-2606-29159:start -->
当前章已把 dataset/model/evaluator/metric/release 分权，并要求 slice、校准、污染与反例证据。
<!-- existing:SF-2026-ARXIV-2606-29159:end -->
<!-- delta:SF-2026-ARXIV-2606-29159:start -->
揭示 pooled leaderboard 会掩盖 RCA 子任务差异，改变评测聚合合同。
<!-- delta:SF-2026-ARXIV-2606-29159:end -->
<!-- books-review:SF-2026-ARXIV-2606-29159:start -->
已重读 `books/part-06-ai-infrastructure/66-evaluation-system.md#L193` 与相邻章 `books/part-06-ai-infrastructure/59-model-registry.md#L144`；决定 `No Change — Existing Coverage`。揭示 pooled leaderboard 会掩盖 RCA 子任务差异，改变评测聚合合同。《Pooled Leaderboards Hide System-Specific Winners: A Reporting-Protocol Audit of Offline Root-Cause Analysis Benchmarks》的正证据锚定 `Benchmark validity and leaderboard instability in ML; system-specific results`；`6 Discussion, Limitations, and Recommendations` 没有建立跨 dataset/model/evaluator revision 的 release acceptance 或生产 SLO。因此该证据只能修正当前判断，超界时 `PLATFORM-EVALUATION-SYSTEM` 必须保持 release Gate Open 并恢复完整分层评测。
<!-- books-review:SF-2026-ARXIV-2606-29159:end -->

<!-- existing:SF-2026-ARXIV-2606-29171:start -->
当前章已拥有 provenance、dedup、contamination 与 typed lineage；单一归因或语料案例不自动形成新命题。
<!-- existing:SF-2026-ARXIV-2606-29171:end -->
<!-- delta:SF-2026-ARXIV-2606-29171:start -->
普通 sample lineage 只能回答数据来自哪里；symbolic mechanistic attribution 进一步把样本影响连接到可解释 behavioral policy，使数据 owner 能把选择、删除或复核请求落到行为证据链。归因仍是模型化证据，符号解释不稳定时保留原数据并回退重训/对照实验。
<!-- delta:SF-2026-ARXIV-2606-29171:end -->
<!-- books-review:SF-2026-ARXIV-2606-29171:start -->
已重读 `books/part-04-training-system/27-data.md#L484` 与相邻章 `books/part-04-training-system/28-pretraining.md#L702`；决定 `Integrate`。只在 Llama-3.2-3B-Instruct refusal proxy、特定 SAE 与 200 个 SFT pair 上验证一阶符号归因；feature label、Ridge fidelity 与 first-order approximation 不等于真实删除/重训因果。保留原样本与重训对照。
<!-- books-review:SF-2026-ARXIV-2606-29171:end -->

<!-- existing:SF-2026-ARXIV-2606-29176:start -->
当前章已把 optimizer、schedule、batch/tokens 与 scaling identity 分开；新证据只有改变外推或控制合同才可追加。
<!-- existing:SF-2026-ARXIV-2606-29176:end -->
<!-- delta:SF-2026-ARXIV-2606-29176:start -->
改变优化器更新的去偏与稳定性路径，并要求按训练阶段校准。
<!-- delta:SF-2026-ARXIV-2606-29176:end -->
<!-- books-review:SF-2026-ARXIV-2606-29176:start -->
已重读 `books/part-04-training-system/28-pretraining.md#L263` 与相邻章 `books/part-04-training-system/27-data.md#L591`；决定 `No Change — Existing Coverage`。改变优化器更新的去偏与稳定性路径，并要求按训练阶段校准。《Dead-Direction Conditioners: Gauge-Equivariant Preconditioning for Deep Networks》的正证据锚定 `5 Experiments; 5.1 Reading the rate at language-model scale`；`5.10 Scope and limitations` 没有建立跨 architecture、optimizer、token budget 与更大训练尺度的可迁移性。因此该证据只能修正当前判断，超界时 `TRAIN-PRETRAINING` 必须恢复邻近规模 sweep 与已验证 schedule。
<!-- books-review:SF-2026-ARXIV-2606-29176:end -->

<!-- existing:SF-2026-ARXIV-2606-29178:start -->
当前章已拥有 admission/retention/forgetting、provenance、transaction 与 raw evidence fallback。
<!-- existing:SF-2026-ARXIV-2606-29178:end -->
<!-- delta:SF-2026-ARXIV-2606-29178:start -->
把长期记忆的写入、保留与遗忘门控变成显式持久状态迁移。
<!-- delta:SF-2026-ARXIV-2606-29178:end -->
<!-- books-review:SF-2026-ARXIV-2606-29178:start -->
已重读 `books/part-07-agent/77-memory.md#L46` 与相邻章 `books/part-07-agent/76-rag.md#L393`；决定 `No Change — Existing Coverage`。把长期记忆的写入、保留与遗忘门控变成显式持久状态迁移。《Selective Memory Retention for Long-Horizon LLM Agents》的正证据锚定 `4 Experiments`；`6 Discussion and Limitations` 没有建立跨 workload、write policy、retention horizon 与 provenance shift 的记忆收益。因此该证据只能修正当前判断，超界时 `AGENT-MEMORY` 必须拒绝写入并保留旧 memory revision。
<!-- books-review:SF-2026-ARXIV-2606-29178:end -->

<!-- existing:SF-2026-ARXIV-2606-29182:start -->
当前章已拥有 versioned state machine、DAG、evaluator-driven search、replay 与 compensation。
<!-- existing:SF-2026-ARXIV-2606-29182:end -->
<!-- delta:SF-2026-ARXIV-2606-29182:start -->
让科学发现 Agent 的信念状态、实验动作与反证更新形成可追踪闭环。
<!-- delta:SF-2026-ARXIV-2606-29182:end -->
<!-- books-review:SF-2026-ARXIV-2606-29182:start -->
已重读 `books/part-07-agent/81-workflow.md#L36` 与相邻章 `books/part-07-agent/78-tool-calling.md#L301`；决定 `No Change — Existing Coverage`。让科学发现 Agent 的信念状态、实验动作与反证更新形成可追踪闭环。《Evidence-Informed LLM Beliefs for Continual Scientific Discovery》的正证据锚定 `3.1.2 Evaluation: Reducing Surprisal Under Non-Stationary Beliefs`；`6 Limitations` 没有建立跨 environment、tool semantics、checkpoint 与 compensation path 的可复算性。因此该证据只能修正当前判断，超界时 `AGENT-WORKFLOW` 必须停在可恢复 checkpoint 并执行 compensation。
<!-- books-review:SF-2026-ARXIV-2606-29182:end -->

<!-- existing:SF-2026-ARXIV-2606-29184:start -->
当前章已把 rank、target modules、adapter identity 与 merge/serve 边界版本化。
<!-- existing:SF-2026-ARXIV-2606-29184:end -->
<!-- delta:SF-2026-ARXIV-2606-29184:start -->
把适配器秩分配与层级预算绑定为可动态选择的训练状态。
<!-- delta:SF-2026-ARXIV-2606-29184:end -->
<!-- books-review:SF-2026-ARXIV-2606-29184:start -->
已重读 `books/part-04-training-system/30-lora.md#L145` 与相邻章 `books/part-04-training-system/29-sft.md#L494`；决定 `No Change — Existing Coverage`。把适配器秩分配与层级预算绑定为可动态选择的训练状态。《BaRA: Bayesian Adaptive Rank Allocation for Parameter-Efficient Fine-Tuning》的正证据锚定 `VI Experiments`；`III-C Limitations of Bayesian LoRA Methods` 没有建立跨 backbone、target module、rank budget 与 merge/serve path 的稳定性。因此该证据只能修正当前判断，超界时 `TRAIN-LORA` 必须恢复固定 rank/target-module adapter。
<!-- books-review:SF-2026-ARXIV-2606-29184:end -->

<!-- existing:SF-2026-ARXIV-2606-29193:start -->
当前章已把 dataset/model/evaluator/metric/release 分权，并要求 slice、校准、污染与反例证据。
<!-- existing:SF-2026-ARXIV-2606-29193:end -->
<!-- delta:SF-2026-ARXIV-2606-29193:start -->
把微服务 Agent 的任务、环境、副作用和故障恢复纳入发布评测。
<!-- delta:SF-2026-ARXIV-2606-29193:end -->
<!-- books-review:SF-2026-ARXIV-2606-29193:start -->
已重读 `books/part-06-ai-infrastructure/66-evaluation-system.md#L193` 与相邻章 `books/part-06-ai-infrastructure/59-model-registry.md#L144`；决定 `No Change — Existing Coverage`。把微服务 Agent 的任务、环境、副作用和故障恢复纳入发布评测。《A Multi-Dataset Benchmark for Evaluating LLM Agents in Microservice Failure Diagnosis》的正证据锚定 `4 Evaluation; 4.4 Evaluation Metric`；`6 Discussion` 没有建立跨 dataset/model/evaluator revision 的 release acceptance 或生产 SLO。因此该证据只能修正当前判断，超界时 `PLATFORM-EVALUATION-SYSTEM` 必须保持 release Gate Open 并恢复完整分层评测。
<!-- books-review:SF-2026-ARXIV-2606-29193:end -->

<!-- existing:SF-2026-ARXIV-2606-29196:start -->
当前章已把 dataset/model/evaluator/metric/release 分权，并要求 slice、校准、污染与反例证据。
<!-- existing:SF-2026-ARXIV-2606-29196:end -->
<!-- delta:SF-2026-ARXIV-2606-29196:start -->
能力评测不能假设模型对 evaluation context 无感；evaluation-awareness probe 必须作为 contamination sensor，按模型尺度和表示深度版本化，并在异常时阻止 pooled score 直接取得 release authority。Probe 迁移失败时回退 blind/held-out protocol 与外部 outcome。
<!-- delta:SF-2026-ARXIV-2606-29196:end -->
<!-- books-review:SF-2026-ARXIV-2606-29196:start -->
已重读 `books/part-06-ai-infrastructure/66-evaluation-system.md#L193` 与相邻章 `books/part-06-ai-infrastructure/59-model-registry.md#L144`；决定 `Integrate`。SAD 上的线性可恢复性只是一种 operational evaluation-awareness signal；white-box AUROC 与黑盒行为会分离，且 Qwen/Gemma 的深度迁移不构成跨 family scaling law。异常只触发额外 held-out evaluation，不授予直接拒绝权。
<!-- books-review:SF-2026-ARXIV-2606-29196:end -->

<!-- existing:SF-2026-ARXIV-2606-29207:start -->
当前章已拥有 request-local decode/refinement state、停止条件与受验证执行路径。
<!-- existing:SF-2026-ARXIV-2606-29207:end -->
<!-- delta:SF-2026-ARXIV-2606-29207:start -->
把 kernel 生成、校验、选择与回退组成可执行的推理内核控制流。
<!-- delta:SF-2026-ARXIV-2606-29207:end -->
<!-- books-review:SF-2026-ARXIV-2606-29207:start -->
已重读 `books/part-05-inference-system/44-decode.md#L31` 与相邻章 `books/part-05-inference-system/43-prefill.md#L297`；决定 `No Change — Existing Coverage`。把 kernel 生成、校验、选择与回退组成可执行的推理内核控制流。《KernelFlume: Elastic Core-Attention Scaling for Agentic Long-Context Decoding》的正证据锚定 `6 Evaluation`；`2.4 Limitations of Existing Elastic Scaling` 没有建立跨 model、request shape、quality target 与 serving engine 的延迟-质量合同。因此该证据只能修正当前判断，超界时 `INFER-DECODE` 必须恢复已验证的普通 decode/refinement path。
<!-- books-review:SF-2026-ARXIV-2606-29207:end -->

<!-- existing:SF-2026-ARXIV-2606-29215:start -->
当前章已拥有 request-local decode/refinement state、停止条件与受验证执行路径。
<!-- existing:SF-2026-ARXIV-2606-29215:end -->
<!-- delta:SF-2026-ARXIV-2606-29215:start -->
把 discrete diffusion 的多块并行解码、校验与质量退化边界显式化。
<!-- delta:SF-2026-ARXIV-2606-29215:end -->
<!-- books-review:SF-2026-ARXIV-2606-29215:start -->
已重读 `books/part-05-inference-system/44-decode.md#L31` 与相邻章 `books/part-05-inference-system/43-prefill.md#L297`；决定 `No Change — Existing Coverage`。把 discrete diffusion 的多块并行解码、校验与质量退化边界显式化。《Multi-Block Diffusion Language Models》的正证据锚定 `4 Experiments`；`5 Conclusion and stated speed-quality scope` 没有建立跨 model、request shape、quality target 与 serving engine 的延迟-质量合同。因此该证据只能修正当前判断，超界时 `INFER-DECODE` 必须恢复已验证的普通 decode/refinement path。
<!-- books-review:SF-2026-ARXIV-2606-29215:end -->

<!-- existing:SF-2026-ARXIV-2606-29222:start -->
当前章已把 observation/action identity、latency、closed-loop outcome 与保守接管绑定。
<!-- existing:SF-2026-ARXIV-2606-29222:end -->
<!-- delta:SF-2026-ARXIV-2606-29222:start -->
把机器人情境记忆接入感知到动作的闭环状态。
<!-- delta:SF-2026-ARXIV-2606-29222:end -->
<!-- books-review:SF-2026-ARXIV-2606-29222:start -->
已重读 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L171` 与相邻章 `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L514`；决定 `No Change — Existing Coverage`。把机器人情境记忆接入感知到动作的闭环状态。《CORE Planner: Contextual-memory Oriented Reinforcement-learning in Unknown Environments for Robot Navigation》的正证据锚定 `V Experiments`；`VI Conclusion and deployment scope` 没有建立跨 embodiment、sensor、latency 与闭环干预的动作成功率。因此该证据只能修正当前判断，超界时 `MULTIMODAL-EMBODIED-VLA` 必须拒绝物理提交并交回保守 controller。
<!-- books-review:SF-2026-ARXIV-2606-29222:end -->

<!-- existing:SF-2026-ARXIV-2606-29223:start -->
当前章已拥有 request-local decode/refinement state、停止条件与受验证执行路径。
<!-- existing:SF-2026-ARXIV-2606-29223:end -->
<!-- delta:SF-2026-ARXIV-2606-29223:start -->
把推理深度按样本难度分配，并保留固定深度回退。
<!-- delta:SF-2026-ARXIV-2606-29223:end -->
<!-- books-review:SF-2026-ARXIV-2606-29223:start -->
已重读 `books/part-05-inference-system/44-decode.md#L31` 与相邻章 `books/part-05-inference-system/43-prefill.md#L297`；决定 `No Change — Existing Coverage`。把推理深度按样本难度分配，并保留固定深度回退。《Depth Exploration for LLM Decoding》的正证据锚定 `4 Experiment`；`E Limitations and discussion` 没有建立跨 model、request shape、quality target 与 serving engine 的延迟-质量合同。因此该证据只能修正当前判断，超界时 `INFER-DECODE` 必须恢复已验证的普通 decode/refinement path。
<!-- books-review:SF-2026-ARXIV-2606-29223:end -->

<!-- existing:SF-2026-ARXIV-2606-29225:start -->
当前章已把模型 sensor、policy/authorization 与 effect-time commit 分开，并拥有 fail-closed fallback。
<!-- existing:SF-2026-ARXIV-2606-29225:end -->
<!-- delta:SF-2026-ARXIV-2606-29225:start -->
把 Agent policy 判定置于工具副作用提交前并定义 fail-closed 路径。
<!-- delta:SF-2026-ARXIV-2606-29225:end -->
<!-- books-review:SF-2026-ARXIV-2606-29225:start -->
已重读 `books/part-06-ai-infrastructure/72-security.md#L418` 与相邻章 `books/part-06-ai-infrastructure/71-multi-tenant.md#L120`；决定 `No Change — Existing Coverage`。把 Agent policy 判定置于工具副作用提交前并定义 fail-closed 路径。《PolicyGuard: A Dialogue-Grounded Sub-Agent Verifier for Policy Adherence in LLM Agents》的正证据锚定 `4 Experiments`；`Discussion` 没有建立跨 threat distribution、attacker adaptation 与 effect-time authorization 的防护承诺。因此该证据只能修正当前判断，超界时 `PLATFORM-SECURITY` 必须拒绝 effect commit 并转 sandbox/人工。
<!-- books-review:SF-2026-ARXIV-2606-29225:end -->

<!-- existing:SF-2026-ARXIV-2606-29228:start -->
当前章已把 dataset/model/evaluator/metric/release 分权，并要求 slice、校准、污染与反例证据。
<!-- existing:SF-2026-ARXIV-2606-29228:end -->
<!-- delta:SF-2026-ARXIV-2606-29228:start -->
揭示 DLM 评测中的表面提升与实际生成能力分离。
<!-- delta:SF-2026-ARXIV-2606-29228:end -->
<!-- books-review:SF-2026-ARXIV-2606-29228:start -->
已重读 `books/part-06-ai-infrastructure/66-evaluation-system.md#L193` 与相邻章 `books/part-06-ai-infrastructure/59-model-registry.md#L144`；决定 `No Change — Existing Coverage`。揭示 DLM 评测中的表面提升与实际生成能力分离。《Understanding Evaluation Illusion in Diffusion Large Language Models》的正证据锚定 `3 Evaluation Inconsistency; 4 Experiments`；`5 Discussion; speed-quality trade-off counterevidence` 没有建立跨 dataset/model/evaluator revision 的 release acceptance 或生产 SLO。因此该证据只能修正当前判断，超界时 `PLATFORM-EVALUATION-SYSTEM` 必须保持 release Gate Open 并恢复完整分层评测。
<!-- books-review:SF-2026-ARXIV-2606-29228:end -->

<!-- existing:SF-2026-ARXIV-2606-29237:start -->
当前章已区分 action-conditioned transition、persistent state、rollout 与 physical commit。
<!-- existing:SF-2026-ARXIV-2606-29237:end -->
<!-- delta:SF-2026-ARXIV-2606-29237:start -->
把运动持续性作为世界模型 rollout 的可测状态而非单帧视觉指标。
<!-- delta:SF-2026-ARXIV-2606-29237:end -->
<!-- books-review:SF-2026-ARXIV-2606-29237:start -->
已重读 `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L189` 与相邻章 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L483`；决定 `No Change — Existing Coverage`。把运动持续性作为世界模型 rollout 的可测状态而非单帧视觉指标。《MoPe: Motion Permanence for Robust Monocular Gaussian Mapping in Dynamic Environments》的正证据锚定 `IV Experiments`；`V Limitations and Future Work` 没有建立跨 environment、observation dynamics 与 physical commit 的 rollout fidelity。因此该证据只能修正当前判断，超界时 `MULTIMODAL-WORLD-MODELS` 必须停止 imagined rollout 并请求真实 observation。
<!-- books-review:SF-2026-ARXIV-2606-29237:end -->

<!-- existing:SF-2026-ARXIV-2606-29238:start -->
当前章已把 terminal reward 拆为 typed trajectory credit，并记录 verifier、policy freshness 与 off-policy 边界。
<!-- existing:SF-2026-ARXIV-2606-29238:end -->
<!-- delta:SF-2026-ARXIV-2606-29238:start -->
给 GRPO 更新的稳定域与偏差来源建立理论边界。
<!-- delta:SF-2026-ARXIV-2606-29238:end -->
<!-- books-review:SF-2026-ARXIV-2606-29238:start -->
已重读 `books/part-04-training-system/33-grpo.md#L879` 与相邻章 `books/part-04-training-system/32-ppo.md#L342`；决定 `No Change — Existing Coverage`。给 GRPO 更新的稳定域与偏差来源建立理论边界。《On the Policy Gradient Foundations of Group Relative Policy Optimization: Credit Assignment, Gradient Sparsity, and Rank Collapse》的正证据锚定 `7 Experiments`；`6 Multi-Turn Limitation` 没有建立跨 reward/verifier、policy freshness 与分布漂移的 on-policy 有效性。因此该证据只能修正当前判断，超界时 `TRAIN-GRPO` 必须恢复 on-policy terminal/verifier baseline。
<!-- books-review:SF-2026-ARXIV-2606-29238:end -->

<!-- existing:SF-2026-ARXIV-2606-29239:start -->
当前章已把模型 sensor、policy/authorization 与 effect-time commit 分开，并拥有 fail-closed fallback。
<!-- existing:SF-2026-ARXIV-2606-29239:end -->
<!-- delta:SF-2026-ARXIV-2606-29239:start -->
把量化后安全回归纳入部署校准与发布 gate。
<!-- delta:SF-2026-ARXIV-2606-29239:end -->
<!-- books-review:SF-2026-ARXIV-2606-29239:start -->
已重读 `books/part-06-ai-infrastructure/72-security.md#L418` 与相邻章 `books/part-06-ai-infrastructure/71-multi-tenant.md#L120`；决定 `No Change — Existing Coverage`。把量化后安全回归纳入部署校准与发布 gate。《Breaking the Rounding Trap: Securing LLMs against Quantization-Conditioned Backdoors》的正证据锚定 `3.2 Empirical Motivation: The Role of Rounding Errors in LLM Quantization`；`3.1 Threat Model` 没有建立跨 threat distribution、attacker adaptation 与 effect-time authorization 的防护承诺。因此该证据只能修正当前判断，超界时 `PLATFORM-SECURITY` 必须拒绝 effect commit 并转 sandbox/人工。
<!-- books-review:SF-2026-ARXIV-2606-29239:end -->

<!-- existing:SF-2026-ARXIV-2606-29251:start -->
当前章已把 raw evidence、derived view、compression fidelity 与可恢复 bookkeeping 分开。
<!-- existing:SF-2026-ARXIV-2606-29251:end -->
<!-- delta:SF-2026-ARXIV-2606-29251:start -->
把上下文压缩的事实保真、推理可用性与预算绑定为控制合同。
<!-- delta:SF-2026-ARXIV-2606-29251:end -->
<!-- books-review:SF-2026-ARXIV-2606-29251:start -->
已重读 `books/part-07-agent/75-context.md#L16` 与相邻章 `books/part-07-agent/74-prompt.md#L187`；决定 `No Change — Existing Coverage`。把上下文压缩的事实保真、推理可用性与预算绑定为控制合同。《When Summaries Distort Decisions: Information Fidelity in LLM-Compressed Financial Analysis》的正证据锚定 `4 Experiments`；`7 Limitations` 没有建立跨 task、compression policy 与 evidence loss 的决策保真。因此该证据只能修正当前判断，超界时 `AGENT-CONTEXT` 必须恢复 hash-addressed raw evidence。
<!-- books-review:SF-2026-ARXIV-2606-29251:end -->

<!-- existing:SF-2026-ARXIV-2606-29270:start -->
当前章已拥有 topology、message/state、aggregation、delegation、independent verification 与 coordination tax。
<!-- existing:SF-2026-ARXIV-2606-29270:end -->
<!-- delta:SF-2026-ARXIV-2606-29270:start -->
多数投票不再自动提交；aggregation owner 保存 minority-sentinel evidence、override criterion 与最终 commit receipt，只在少数意见显示独立且校准的反证时推翻多数。相关错误或 sentinel 失准时回退独立 verifier/人工，而不是继续增加同源 Agent。
<!-- delta:SF-2026-ARXIV-2606-29270:end -->
<!-- books-review:SF-2026-ARXIV-2606-29270:start -->
已重读 `books/part-07-agent/82-multi-agent.md#L380` 与相邻章 `books/part-07-agent/81-workflow.md#L702`；决定 `Integrate`。只证明三异构 Agent、两轮、六 benchmark 的 debate-log classifier 能在已测阈值上安全翻转；共享训练导致的相关错误、换模型和换协议都可能破坏 81.2% Flip Precision。失配时不翻转并交给独立 verifier/人工。
<!-- books-review:SF-2026-ARXIV-2606-29270:end -->

<!-- existing:SF-2026-ARXIV-2606-29275:start -->
当前章已拥有 request-local decode/refinement state、停止条件与受验证执行路径。
<!-- existing:SF-2026-ARXIV-2606-29275:end -->
<!-- delta:SF-2026-ARXIV-2606-29275:start -->
按置信度动态分配离散扩散步数并定义失败回退。
<!-- delta:SF-2026-ARXIV-2606-29275:end -->
<!-- books-review:SF-2026-ARXIV-2606-29275:start -->
已重读 `books/part-05-inference-system/44-decode.md#L31` 与相邻章 `books/part-05-inference-system/43-prefill.md#L297`；决定 `No Change — Existing Coverage`。按置信度动态分配离散扩散步数并定义失败回退。《Adaptive Block Diffusion: Resolving Training-Inference Mismatch in Diffusion Language Models》的正证据锚定 `5 Experiments`；`4.4 Limitation of Block Diffusion` 没有建立跨 model、request shape、quality target 与 serving engine 的延迟-质量合同。因此该证据只能修正当前判断，超界时 `INFER-DECODE` 必须恢复已验证的普通 decode/refinement path。
<!-- books-review:SF-2026-ARXIV-2606-29275:end -->

<!-- existing:SF-2026-ARXIV-2606-29278:start -->
当前章已把 dataset/model/evaluator/metric/release 分权，并要求 slice、校准、污染与反例证据。
<!-- existing:SF-2026-ARXIV-2606-29278:end -->
<!-- delta:SF-2026-ARXIV-2606-29278:start -->
把推理复杂度上限与 benchmark 饱和分开，形成停止判断。
<!-- delta:SF-2026-ARXIV-2606-29278:end -->
<!-- books-review:SF-2026-ARXIV-2606-29278:start -->
已重读 `books/part-06-ai-infrastructure/66-evaluation-system.md#L193` 与相邻章 `books/part-06-ai-infrastructure/59-model-registry.md#L144`；决定 `No Change — Existing Coverage`。把推理复杂度上限与 benchmark 饱和分开，形成停止判断。《The Complexity Ceiling Benchmark: A Multi-Domain Evaluation of Sequential Reasoning Under Depth Scaling》的正证据锚定 `Trace-level evaluation and structural uncertainty`；`5 Discussion` 没有建立跨 dataset/model/evaluator revision 的 release acceptance 或生产 SLO。因此该证据只能修正当前判断，超界时 `PLATFORM-EVALUATION-SYSTEM` 必须保持 release Gate Open 并恢复完整分层评测。
<!-- books-review:SF-2026-ARXIV-2606-29278:end -->

<!-- existing:SF-2026-ARXIV-2606-29279:start -->
当前章已拥有 admission/retention/forgetting、provenance、transaction 与 raw evidence fallback。
<!-- existing:SF-2026-ARXIV-2606-29279:end -->
<!-- delta:SF-2026-ARXIV-2606-29279:start -->
把记忆中的转述污染与一手证据 provenance 分开。
<!-- delta:SF-2026-ARXIV-2606-29279:end -->
<!-- books-review:SF-2026-ARXIV-2606-29279:start -->
已重读 `books/part-07-agent/77-memory.md#L46` 与相邻章 `books/part-07-agent/76-rag.md#L393`；决定 `No Change — Existing Coverage`。把记忆中的转述污染与一手证据 provenance 分开。《Manufactured Confidence: How Memory Consolidation Turns Hearsay into Confident Facts》的正证据锚定 `3 Results`；`Conclusion and source-provenance scope` 没有建立跨 workload、write policy、retention horizon 与 provenance shift 的记忆收益。因此该证据只能修正当前判断，超界时 `AGENT-MEMORY` 必须拒绝写入并保留旧 memory revision。
<!-- books-review:SF-2026-ARXIV-2606-29279:end -->

<!-- existing:SF-2026-ARXIV-2606-29280:start -->
当前章已把 dataset/model/evaluator/metric/release 分权，并要求 slice、校准、污染与反例证据。
<!-- existing:SF-2026-ARXIV-2606-29280:end -->
<!-- delta:SF-2026-ARXIV-2606-29280:start -->
把高风险 pipeline 的阶段性不确定性、升级与拒答纳入验收。
<!-- delta:SF-2026-ARXIV-2606-29280:end -->
<!-- books-review:SF-2026-ARXIV-2606-29280:start -->
已重读 `books/part-06-ai-infrastructure/66-evaluation-system.md#L193` 与相邻章 `books/part-06-ai-infrastructure/59-model-registry.md#L144`；决定 `No Change — Existing Coverage`。把高风险 pipeline 的阶段性不确定性、升级与拒答纳入验收。《Deterministic Decisions for High-Stakes AI. A Zero-Egress Pipeline with the Deployability of RAG and the Accuracy of Machine Learning》的正证据锚定 `Evaluation methodology and outcome study`；`2.4 Machine Learning for Student Outcome Prediction: Benchmarks and Limits` 没有建立跨 dataset/model/evaluator revision 的 release acceptance 或生产 SLO。因此该证据只能修正当前判断，超界时 `PLATFORM-EVALUATION-SYSTEM` 必须保持 release Gate Open 并恢复完整分层评测。
<!-- books-review:SF-2026-ARXIV-2606-29280:end -->

<!-- existing:SF-2026-ARXIV-2606-29282:start -->
当前章已把模型 sensor、policy/authorization 与 effect-time commit 分开，并拥有 fail-closed fallback。
<!-- existing:SF-2026-ARXIV-2606-29282:end -->
<!-- delta:SF-2026-ARXIV-2606-29282:start -->
把概念擦除的残留行为与再激活纳入安全发布证据。
<!-- delta:SF-2026-ARXIV-2606-29282:end -->
<!-- books-review:SF-2026-ARXIV-2606-29282:start -->
已重读 `books/part-06-ai-infrastructure/72-security.md#L418` 与相邻章 `books/part-06-ai-infrastructure/71-multi-tenant.md#L120`；决定 `No Change — Existing Coverage`。把概念擦除的残留行为与再激活纳入安全发布证据。《ScaleErasure: Inference-Time Minimal Intervention for Precise Concept Erasure in Next-Scale Autoregressive Image Generation》的正证据锚定 `5 Experiments`；`B Discussion on MACE Adaptation` 没有建立跨 threat distribution、attacker adaptation 与 effect-time authorization 的防护承诺。因此该证据只能修正当前判断，超界时 `PLATFORM-SECURITY` 必须拒绝 effect commit 并转 sandbox/人工。
<!-- books-review:SF-2026-ARXIV-2606-29282:end -->

<!-- existing:SF-2026-ARXIV-2606-29296:start -->
当前章已把 terminal reward 拆为 typed trajectory credit，并记录 verifier、policy freshness 与 off-policy 边界。
<!-- existing:SF-2026-ARXIV-2606-29296:end -->
<!-- delta:SF-2026-ARXIV-2606-29296:start -->
把策略更新的通过条件与样本级失败信号结合，改变 reward gate。
<!-- delta:SF-2026-ARXIV-2606-29296:end -->
<!-- books-review:SF-2026-ARXIV-2606-29296:start -->
已重读 `books/part-04-training-system/33-grpo.md#L879` 与相邻章 `books/part-04-training-system/32-ppo.md#L342`；决定 `No Change — Existing Coverage`。把策略更新的通过条件与样本级失败信号结合，改变 reward gate。《Process Advantage Signal Shaping: A Paradigm-Agnostic Middleware for Process-Supervised RL in LLM Reasoners》的正证据锚定 `Empirical scope; evaluation protocol`；`6 Discussion` 没有建立跨 reward/verifier、policy freshness 与分布漂移的 on-policy 有效性。因此该证据只能修正当前判断，超界时 `TRAIN-GRPO` 必须恢复 on-policy terminal/verifier baseline。
<!-- books-review:SF-2026-ARXIV-2606-29296:end -->

<!-- existing:SF-2026-ARXIV-2606-29315:start -->
当前章已拥有 versioned state machine、DAG、evaluator-driven search、replay 与 compensation。
<!-- existing:SF-2026-ARXIV-2606-29315:end -->
<!-- delta:SF-2026-ARXIV-2606-29315:start -->
把实验设计、工具执行、观测与假设修订组织成可复算工作流。
<!-- delta:SF-2026-ARXIV-2606-29315:end -->
<!-- books-review:SF-2026-ARXIV-2606-29315:start -->
已重读 `books/part-07-agent/81-workflow.md#L36` 与相邻章 `books/part-07-agent/78-tool-calling.md#L301`；决定 `No Change — Existing Coverage`。把实验设计、工具执行、观测与假设修订组织成可复算工作流。《Hierarchical Experimentalist Agents》的正证据锚定 `4 Experiments and Results on Interphyre`；`A.5 Design Principles; domain-agnostic inputs and simulator-only evidence boundary` 没有建立跨 environment、tool semantics、checkpoint 与 compensation path 的可复算性。因此该证据只能修正当前判断，超界时 `AGENT-WORKFLOW` 必须停在可恢复 checkpoint 并执行 compensation。
<!-- books-review:SF-2026-ARXIV-2606-29315:end -->

<!-- existing:SF-2026-ARXIV-2606-29328:start -->
当前章已拥有 typed query plan、router、metric/index identity、evidence sufficiency 与失败回退。
<!-- existing:SF-2026-ARXIV-2606-29328:end -->
<!-- delta:SF-2026-ARXIV-2606-29328:start -->
把 RAG context selection 从单点相关性排序改为多维 information-demand coverage，并持有 sub-query 权重、set coverage 与 context-budget 状态。
<!-- delta:SF-2026-ARXIV-2606-29328:end -->
<!-- books-review:SF-2026-ARXIV-2606-29328:start -->
已重读 `books/part-07-agent/76-rag.md#L51` 与相邻章 `books/part-07-agent/77-memory.md#L1017`；决定 `No Change — Existing Coverage`。只证明六个 open-domain QA benchmark 上，把 K=200 candidate 的 k-context selection 改成多维 demand coverage 可改善 EM；理论 non-coverability 仅约束 query-proximity-monotone scorer，不直接约束 cross-encoder。sub-query drift、OT surrogate 成本或 corpus shift 失控时回退已校准 top-k/MMR。
<!-- books-review:SF-2026-ARXIV-2606-29328:end -->

<!-- existing:SF-2026-ARXIV-2606-29337:start -->
当前章已要求 graph/kernel/precision/hardware 共同形成 execution plan，并由 validator 而非生成器提交。
<!-- existing:SF-2026-ARXIV-2606-29337:end -->
<!-- delta:SF-2026-ARXIV-2606-29337:start -->
给 W4A4 量化的校准、kernel 与质量回退建立部署边界。
<!-- delta:SF-2026-ARXIV-2606-29337:end -->
<!-- books-review:SF-2026-ARXIV-2606-29337:start -->
已重读 `books/part-05-inference-system/49-tensorrt-llm.md#L394` 与相邻章 `books/part-05-inference-system/48-speculative-decoding.md#L597`；决定 `No Change — Existing Coverage`。给 W4A4 量化的校准、kernel 与质量回退建立部署边界。《W4A4 Quantization for Inference on Wan2.2-I2V-A14B》的正证据锚定 `IV Evaluation and Results`；`IV-B Discussion` 没有建立跨 kernel、hardware、precision 与 graph revision 的执行计划可移植性。因此该证据只能修正当前判断，超界时 `INFER-TENSORRT-LLM` 必须恢复已验收 kernel/precision plan。
<!-- books-review:SF-2026-ARXIV-2606-29337:end -->

<!-- existing:SF-2026-ARXIV-2606-29340:start -->
当前章已把 terminal reward 拆为 typed trajectory credit，并记录 verifier、policy freshness 与 off-policy 边界。
<!-- existing:SF-2026-ARXIV-2606-29340:end -->
<!-- delta:SF-2026-ARXIV-2606-29340:start -->
把 off-policy 样本选择与策略漂移控制纳入训练状态。
<!-- delta:SF-2026-ARXIV-2606-29340:end -->
<!-- books-review:SF-2026-ARXIV-2606-29340:start -->
已重读 `books/part-04-training-system/33-grpo.md#L879` 与相邻章 `books/part-04-training-system/32-ppo.md#L342`；决定 `No Change — Existing Coverage`。把 off-policy 样本选择与策略漂移控制纳入训练状态。《PHF: Privileged Hidden Flow for On-Policy Self-Distillation》的正证据锚定 `Experiments`；`Discussion` 没有建立跨 reward/verifier、policy freshness 与分布漂移的 on-policy 有效性。因此该证据只能修正当前判断，超界时 `TRAIN-GRPO` 必须恢复 on-policy terminal/verifier baseline。
<!-- books-review:SF-2026-ARXIV-2606-29340:end -->

<!-- existing:SF-2026-ARXIV-2606-29350:start -->
当前章已把 observation/action identity、latency、closed-loop outcome 与保守接管绑定。
<!-- existing:SF-2026-ARXIV-2606-29350:end -->
<!-- delta:SF-2026-ARXIV-2606-29350:start -->
把 VLA 视觉 token 合并与动作成功、延迟和回退共同校准。
<!-- delta:SF-2026-ARXIV-2606-29350:end -->
<!-- books-review:SF-2026-ARXIV-2606-29350:start -->
已重读 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L171` 与相邻章 `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L514`；决定 `No Change — Existing Coverage`。把 VLA 视觉 token 合并与动作成功、延迟和回退共同校准。《Fast Enough to Act: Spatio-Temporal Visual Token Merging for Low-Latency Robotic VLMs and VLAs》的正证据锚定 `IV Experiments`；`V Conclusion and Discussion` 没有建立跨 embodiment、sensor、latency 与闭环干预的动作成功率。因此该证据只能修正当前判断，超界时 `MULTIMODAL-EMBODIED-VLA` 必须拒绝物理提交并交回保守 controller。
<!-- books-review:SF-2026-ARXIV-2606-29350:end -->

<!-- existing:SF-2026-ARXIV-2606-29354:start -->
当前章已拥有 topology、message/state、aggregation、delegation、independent verification 与 coordination tax。
<!-- existing:SF-2026-ARXIV-2606-29354:end -->
<!-- delta:SF-2026-ARXIV-2606-29354:start -->
把符号消息协议作为多 Agent 共享状态而非自由文本旁路。
<!-- delta:SF-2026-ARXIV-2606-29354:end -->
<!-- books-review:SF-2026-ARXIV-2606-29354:start -->
已重读 `books/part-07-agent/82-multi-agent.md#L380` 与相邻章 `books/part-07-agent/81-workflow.md#L702`；决定 `No Change — Existing Coverage`。把符号消息协议作为多 Agent 共享状态而非自由文本旁路。《When LLMs Develop Languages: Symbolic Communication for Efficient Multi-Agent Reasoning》的正证据锚定 `4 Experiments`；`5 Conclusion and Limitations` 没有建立跨 agent population、message protocol、error correlation 与 coordination load 的聚合收益。因此该证据只能修正当前判断，超界时 `AGENT-MULTI-AGENT` 必须恢复单 Agent/串行协调与人工仲裁。
<!-- books-review:SF-2026-ARXIV-2606-29354:end -->

<!-- existing:SF-2026-ARXIV-2606-29366:start -->
当前章已拥有 versioned state machine、DAG、evaluator-driven search、replay 与 compensation。
<!-- existing:SF-2026-ARXIV-2606-29366:end -->
<!-- delta:SF-2026-ARXIV-2606-29366:start -->
把 LLM 建议置于 solver 验证与可执行证据之后。
<!-- delta:SF-2026-ARXIV-2606-29366:end -->
<!-- books-review:SF-2026-ARXIV-2606-29366:start -->
已重读 `books/part-07-agent/81-workflow.md#L36` 与相邻章 `books/part-07-agent/78-tool-calling.md#L301`；决定 `No Change — Existing Coverage`。把 LLM 建议置于 solver 验证与可执行证据之后。《Solver-Verified Formulation Generation and Selection for Multi-Warehouse Inventory Allocation Using Large Language Models》的正证据锚定 `6 Computational Evaluation`；`Conclusion and solver-coverage boundary` 没有建立跨 environment、tool semantics、checkpoint 与 compensation path 的可复算性。因此该证据只能修正当前判断，超界时 `AGENT-WORKFLOW` 必须停在可恢复 checkpoint 并执行 compensation。
<!-- books-review:SF-2026-ARXIV-2606-29366:end -->

<!-- existing:SF-2026-ARXIV-2606-29377:start -->
当前章已拥有 typed query plan、router、metric/index identity、evidence sufficiency 与失败回退。
<!-- existing:SF-2026-ARXIV-2606-29377:end -->
<!-- delta:SF-2026-ARXIV-2606-29377:start -->
把检索失败诊断、查询修复与证据重取变成循环控制。
<!-- delta:SF-2026-ARXIV-2606-29377:end -->
<!-- books-review:SF-2026-ARXIV-2606-29377:start -->
已重读 `books/part-07-agent/76-rag.md#L51` 与相邻章 `books/part-07-agent/77-memory.md#L1017`；决定 `No Change — Existing Coverage`。把检索失败诊断、查询修复与证据重取变成循环控制。《Diagnosing and Repairing Factual Errors in RAG under Budget Constraints》的正证据锚定 `3 Experiments`；`Conclusion and evaluated-query scope` 没有建立跨 corpus、query distribution、retriever/index revision 与生成器的检索收益。因此该证据只能修正当前判断，超界时 `AGENT-RAG` 必须恢复固定、已校准的 retrieval plan。
<!-- books-review:SF-2026-ARXIV-2606-29377:end -->

<!-- existing:SF-2026-ARXIV-2606-29403:start -->
当前章已把 dataset/model/evaluator/metric/release 分权，并要求 slice、校准、污染与反例证据。
<!-- existing:SF-2026-ARXIV-2606-29403:end -->
<!-- delta:SF-2026-ARXIV-2606-29403:start -->
把 conformal coverage 与拒答/发布阈值绑定。
<!-- delta:SF-2026-ARXIV-2606-29403:end -->
<!-- books-review:SF-2026-ARXIV-2606-29403:start -->
已重读 `books/part-06-ai-infrastructure/66-evaluation-system.md#L193` 与相邻章 `books/part-06-ai-infrastructure/59-model-registry.md#L144`；决定 `No Change — Existing Coverage`。把 conformal coverage 与拒答/发布阈值绑定。《Self-Organized Conformal Prediction: Reducing Regional Coverage Gaps with Unsupervised Group Discovery》的正证据锚定 `4 Experiments`；`Conclusion and exchangeability boundary` 没有建立跨 dataset/model/evaluator revision 的 release acceptance 或生产 SLO。因此该证据只能修正当前判断，超界时 `PLATFORM-EVALUATION-SYSTEM` 必须保持 release Gate Open 并恢复完整分层评测。
<!-- books-review:SF-2026-ARXIV-2606-29403:end -->

<!-- existing:SF-2026-ARXIV-2606-29424:start -->
当前章已把 routing、placement、energy/thermal、SLO 与 topology state 纳入调度控制。
<!-- existing:SF-2026-ARXIV-2606-29424:end -->
<!-- delta:SF-2026-ARXIV-2606-29424:start -->
让 router 持有请求熵、专家选择与负载降级状态。
<!-- delta:SF-2026-ARXIV-2606-29424:end -->
<!-- books-review:SF-2026-ARXIV-2606-29424:start -->
已重读 `books/part-05-inference-system/56-inference-scheduling.md#L183` 与相邻章 `books/part-05-inference-system/46-continuous-batching.md#L216`；决定 `No Change — Existing Coverage`。让 router 持有请求熵、专家选择与负载降级状态。《EntroRouter: Learning Efficient Model Routing via Entropy Regulation》的正证据锚定 `4 Experiments`；`5 Discussion` 没有建立跨 topology、并发负载、thermal state 与 SLO 的调度收益。因此该证据只能修正当前判断，超界时 `INFER-SCHEDULING` 必须恢复静态 placement 与保守 SLO headroom。
<!-- books-review:SF-2026-ARXIV-2606-29424:end -->

<!-- existing:SF-2026-ARXIV-2606-29425:start -->
当前章已拥有 topology、message/state、aggregation、delegation、independent verification 与 coordination tax。
<!-- existing:SF-2026-ARXIV-2606-29425:end -->
<!-- delta:SF-2026-ARXIV-2606-29425:start -->
把辩论者选择与聚合权重变成可校准协调状态。
<!-- delta:SF-2026-ARXIV-2606-29425:end -->
<!-- books-review:SF-2026-ARXIV-2606-29425:start -->
已重读 `books/part-07-agent/82-multi-agent.md#L380` 与相邻章 `books/part-07-agent/81-workflow.md#L702`；决定 `No Change — Existing Coverage`。把辩论者选择与聚合权重变成可校准协调状态。《Mixture of Debaters: Learn to Debate at Architectural Level in Multi-Agent Reasoning》的正证据锚定 `4 Experiments`；`Conclusion and tested-debater scope` 没有建立跨 agent population、message protocol、error correlation 与 coordination load 的聚合收益。因此该证据只能修正当前判断，超界时 `AGENT-MULTI-AGENT` 必须恢复单 Agent/串行协调与人工仲裁。
<!-- books-review:SF-2026-ARXIV-2606-29425:end -->

<!-- existing:SF-2026-ARXIV-2606-29441:start -->
当前章已把模型 sensor、policy/authorization 与 effect-time commit 分开，并拥有 fail-closed fallback。
<!-- existing:SF-2026-ARXIV-2606-29441:end -->
<!-- delta:SF-2026-ARXIV-2606-29441:start -->
把 activation defense 的检测、干预与失效边界置于运行时控制面。
<!-- delta:SF-2026-ARXIV-2606-29441:end -->
<!-- books-review:SF-2026-ARXIV-2606-29441:start -->
已重读 `books/part-06-ai-infrastructure/72-security.md#L418` 与相邻章 `books/part-06-ai-infrastructure/71-multi-tenant.md#L120`；决定 `No Change — Existing Coverage`。把 activation defense 的检测、干预与失效边界置于运行时控制面。《Closing the Activation-Cone Blind Spot: Response-Time Probing and Unified Defense》的正证据锚定 `4 Experimental Setup; 5.1 No Single-Mechanism Paradigm Dominates`；`6 Discussion and Limitations` 没有建立跨 threat distribution、attacker adaptation 与 effect-time authorization 的防护承诺。因此该证据只能修正当前判断，超界时 `PLATFORM-SECURITY` 必须拒绝 effect commit 并转 sandbox/人工。
<!-- books-review:SF-2026-ARXIV-2606-29441:end -->

<!-- existing:SF-2026-ARXIV-2606-29445:start -->
当前章已把 dataset/model/evaluator/metric/release 分权，并要求 slice、校准、污染与反例证据。
<!-- existing:SF-2026-ARXIV-2606-29445:end -->
<!-- delta:SF-2026-ARXIV-2606-29445:start -->
把视频 GUI Agent 的长程观测与操作副作用纳入端到端评测。
<!-- delta:SF-2026-ARXIV-2606-29445:end -->
<!-- books-review:SF-2026-ARXIV-2606-29445:start -->
已重读 `books/part-06-ai-infrastructure/66-evaluation-system.md#L193` 与相邻章 `books/part-06-ai-infrastructure/59-model-registry.md#L144`；决定 `No Change — Existing Coverage`。把视频 GUI Agent 的长程观测与操作副作用纳入端到端评测。《Bridging VideoQA and Video-Guided Agentic Tasks via Generalized Keyframe Extraction》的正证据锚定 `4 Experiments`；`Conclusion and benchmark-domain scope` 没有建立跨 dataset/model/evaluator revision 的 release acceptance 或生产 SLO。因此该证据只能修正当前判断，超界时 `PLATFORM-EVALUATION-SYSTEM` 必须保持 release Gate Open 并恢复完整分层评测。
<!-- books-review:SF-2026-ARXIV-2606-29445:end -->

<!-- existing:SF-2026-ARXIV-2606-29472:start -->
当前章已拥有 run identity、event/observation history、policy、trajectory evaluation 与 replay。
<!-- existing:SF-2026-ARXIV-2606-29472:end -->
<!-- delta:SF-2026-ARXIV-2606-29472:start -->
Computer-use 平台需要把 gated keyframe、audio transcript、persistent narration 与动作回执定义为版本化 observation interface，而不是让模型任意读取连续桌面流。接口 owner 管理 capture/retention 与 action-state identity；视觉 token 稀释或漏帧时回退高保真 capture/人工确认。
<!-- delta:SF-2026-ARXIV-2606-29472:end -->
<!-- books-review:SF-2026-ARXIV-2606-29472:start -->
已重读 `books/part-07-agent/84-agent-platform.md#L399` 与相邻章 `books/part-07-agent/83-mcp.md#L229`；决定 `Integrate`。只覆盖 DynaCU-Bench 浏览器任务与已测 CU models；Gemini 3 Flash 上 keyframe image-token dilution 已构成反例，因此 AOI 不是固定 bundle，也未证明桌面 OS、权限副作用或持续会议场景安全。退回高保真 capture 与人工确认。
<!-- books-review:SF-2026-ARXIV-2606-29472:end -->

<!-- existing:SF-2026-ARXIV-2606-29476:start -->
当前章已把 terminal reward 拆为 typed trajectory credit，并记录 verifier、policy freshness 与 off-policy 边界。
<!-- existing:SF-2026-ARXIV-2606-29476:end -->
<!-- delta:SF-2026-ARXIV-2606-29476:start -->
把 reward 构造与可验证约束结合并保留失败样本。
<!-- delta:SF-2026-ARXIV-2606-29476:end -->
<!-- books-review:SF-2026-ARXIV-2606-29476:start -->
已重读 `books/part-04-training-system/33-grpo.md#L879` 与相邻章 `books/part-04-training-system/32-ppo.md#L342`；决定 `No Change — Existing Coverage`。把 reward 构造与可验证约束结合并保留失败样本。《CRAFT: Counterfactual Credit Assignment from Free Sibling Rollouts for Self-Distilled Agentic Reinforcement Learning》的正证据锚定 `5 Experiments`；`7 Discussion and Limitations` 没有建立跨 reward/verifier、policy freshness 与分布漂移的 on-policy 有效性。因此该证据只能修正当前判断，超界时 `TRAIN-GRPO` 必须恢复 on-policy terminal/verifier baseline。
<!-- books-review:SF-2026-ARXIV-2606-29476:end -->

<!-- existing:SF-2026-ARXIV-2606-29481:start -->
当前章已把 terminal reward 拆为 typed trajectory credit，并记录 verifier、policy freshness 与 off-policy 边界。
<!-- existing:SF-2026-ARXIV-2606-29481:end -->
<!-- delta:SF-2026-ARXIV-2606-29481:start -->
按难度与策略状态控制 rollout 采样和更新。
<!-- delta:SF-2026-ARXIV-2606-29481:end -->
<!-- books-review:SF-2026-ARXIV-2606-29481:start -->
已重读 `books/part-04-training-system/33-grpo.md#L879` 与相邻章 `books/part-04-training-system/32-ppo.md#L342`；决定 `No Change — Existing Coverage`。按难度与策略状态控制 rollout 采样和更新。《To Reason or to Fabricate: Reasoning Without Shortcuts via Hint-Anchored Pairwise Aggregation》的正证据锚定 `3 Experimental Setup`；`2.2 Direct KL Optimization and Its Limitations` 没有建立跨 reward/verifier、policy freshness 与分布漂移的 on-policy 有效性。因此该证据只能修正当前判断，超界时 `TRAIN-GRPO` 必须恢复 on-policy terminal/verifier baseline。
<!-- books-review:SF-2026-ARXIV-2606-29481:end -->

<!-- existing:SF-2026-ARXIV-2606-29490:start -->
当前章已把 dataset/model/evaluator/metric/release 分权，并要求 slice、校准、污染与反例证据。
<!-- existing:SF-2026-ARXIV-2606-29490:end -->
<!-- delta:SF-2026-ARXIV-2606-29490:start -->
把置信承诺、校准误差与拒答决策绑定。
<!-- delta:SF-2026-ARXIV-2606-29490:end -->
<!-- books-review:SF-2026-ARXIV-2606-29490:start -->
已重读 `books/part-06-ai-infrastructure/66-evaluation-system.md#L193` 与相邻章 `books/part-06-ai-infrastructure/59-model-registry.md#L144`；决定 `No Change — Existing Coverage`。把置信承诺、校准误差与拒答决策绑定。《Reported Confidence in LLMs Tracks Commitment More Than Correctness》的正证据锚定 `1.2 Supplemental Results`；`Conclusion and evaluated-distribution scope` 没有建立跨 dataset/model/evaluator revision 的 release acceptance 或生产 SLO。因此该证据只能修正当前判断，超界时 `PLATFORM-EVALUATION-SYSTEM` 必须保持 release Gate Open 并恢复完整分层评测。
<!-- books-review:SF-2026-ARXIV-2606-29490:end -->

<!-- existing:SF-2026-ARXIV-2606-29493:start -->
当前章已把 dataset/model/evaluator/metric/release 分权，并要求 slice、校准、污染与反例证据。
<!-- existing:SF-2026-ARXIV-2606-29493:end -->
<!-- delta:SF-2026-ARXIV-2606-29493:start -->
把形式化 benchmark 的语义正确与语法通过分层审计。
<!-- delta:SF-2026-ARXIV-2606-29493:end -->
<!-- books-review:SF-2026-ARXIV-2606-29493:start -->
已重读 `books/part-06-ai-infrastructure/66-evaluation-system.md#L193` 与相邻章 `books/part-06-ai-infrastructure/59-model-registry.md#L144`；决定 `No Change — Existing Coverage`。把形式化 benchmark 的语义正确与语法通过分层审计。《Faults in Our Formal Benchmarking: Dataset Defects and Evaluation Failures in Lean Theorem Proving》的正证据锚定 `2 What Formal Benchmarking Certifies (and What It Does Not)`；`7 Limitations` 没有建立跨 dataset/model/evaluator revision 的 release acceptance 或生产 SLO。因此该证据只能修正当前判断，超界时 `PLATFORM-EVALUATION-SYSTEM` 必须保持 release Gate Open 并恢复完整分层评测。
<!-- books-review:SF-2026-ARXIV-2606-29493:end -->

<!-- existing:SF-2026-ARXIV-2606-29501:start -->
当前章已区分 action-conditioned transition、persistent state、rollout 与 physical commit。
<!-- existing:SF-2026-ARXIV-2606-29501:end -->
<!-- delta:SF-2026-ARXIV-2606-29501:start -->
把 action-conditioned rollout 与可干预世界状态联结。
<!-- delta:SF-2026-ARXIV-2606-29501:end -->
<!-- books-review:SF-2026-ARXIV-2606-29501:start -->
已重读 `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L189` 与相邻章 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L483`；决定 `No Change — Existing Coverage`。把 action-conditioned rollout 与可干预世界状态联结。《Learning Transferable Dynamics Priors from Action to World Modeling》的正证据锚定 `4 Experiments`；`4.5 Ablations and discussions` 没有建立跨 environment、observation dynamics 与 physical commit 的 rollout fidelity。因此该证据只能修正当前判断，超界时 `MULTIMODAL-WORLD-MODELS` 必须停止 imagined rollout 并请求真实 observation。
<!-- books-review:SF-2026-ARXIV-2606-29501:end -->

<!-- existing:SF-2026-ARXIV-2606-29502:start -->
当前章已拥有 admission/retention/forgetting、provenance、transaction 与 raw evidence fallback。
<!-- existing:SF-2026-ARXIV-2606-29502:end -->
<!-- delta:SF-2026-ARXIV-2606-29502:start -->
把技能发现、组合与持久化变成可更新 Agent 状态。
<!-- delta:SF-2026-ARXIV-2606-29502:end -->
<!-- books-review:SF-2026-ARXIV-2606-29502:start -->
已重读 `books/part-07-agent/77-memory.md#L46` 与相邻章 `books/part-07-agent/76-rag.md#L393`；决定 `No Change — Existing Coverage`。把技能发现、组合与持久化变成可更新 Agent 状态。《UCOB: Learning to Utilize and Evolve Agentic Skills via Credit-Aware On-Policy Bidirectional Self-Distillation》的正证据锚定 `6 Experiments`；`Conclusion and evaluated-environment boundary` 没有建立跨 workload、write policy、retention horizon 与 provenance shift 的记忆收益。因此该证据只能修正当前判断，超界时 `AGENT-MEMORY` 必须拒绝写入并保留旧 memory revision。
<!-- books-review:SF-2026-ARXIV-2606-29502:end -->

<!-- existing:SF-2026-ARXIV-2606-29506:start -->
当前章已把 dataset/model/evaluator/metric/release 分权，并要求 slice、校准、污染与反例证据。
<!-- existing:SF-2026-ARXIV-2606-29506:end -->
<!-- delta:SF-2026-ARXIV-2606-29506:start -->
揭示跨数据集切分污染并改变 benchmark release contract。
<!-- delta:SF-2026-ARXIV-2606-29506:end -->
<!-- books-review:SF-2026-ARXIV-2606-29506:start -->
已重读 `books/part-06-ai-infrastructure/66-evaluation-system.md#L193` 与相邻章 `books/part-06-ai-infrastructure/59-model-registry.md#L144`；决定 `No Change — Existing Coverage`。揭示跨数据集切分污染并改变 benchmark release contract。《Benchmark AUC Is Not Deployable Reliability: A Cross-Dataset Audit of Off-the-Shelf Features for Surveillance Video Anomaly Detection》的正证据锚定 `IV Results`；`VII Discussion` 没有建立跨 dataset/model/evaluator revision 的 release acceptance 或生产 SLO。因此该证据只能修正当前判断，超界时 `PLATFORM-EVALUATION-SYSTEM` 必须保持 release Gate Open 并恢复完整分层评测。
<!-- books-review:SF-2026-ARXIV-2606-29506:end -->

<!-- existing:SF-2026-ARXIV-2606-29520:start -->
当前章已把 dataset/model/evaluator/metric/release 分权，并要求 slice、校准、污染与反例证据。
<!-- existing:SF-2026-ARXIV-2606-29520:end -->
<!-- delta:SF-2026-ARXIV-2606-29520:start -->
把安全知识、执行与拒答分层测量。
<!-- delta:SF-2026-ARXIV-2606-29520:end -->
<!-- books-review:SF-2026-ARXIV-2606-29520:start -->
已重读 `books/part-06-ai-infrastructure/66-evaluation-system.md#L193` 与相邻章 `books/part-06-ai-infrastructure/59-model-registry.md#L144`；决定 `No Change — Existing Coverage`。把安全知识、执行与拒答分层测量。《SAKE: Software Architectural Knowledge Evaluation Benchmark for Large Language Models》的正证据锚定 `Benchmark construction and evaluation`；`7 Threats to Validity` 没有建立跨 dataset/model/evaluator revision 的 release acceptance 或生产 SLO。因此该证据只能修正当前判断，超界时 `PLATFORM-EVALUATION-SYSTEM` 必须保持 release Gate Open 并恢复完整分层评测。
<!-- books-review:SF-2026-ARXIV-2606-29520:end -->

<!-- existing:SF-2026-ARXIV-2606-29522:start -->
当前章已把 raw evidence、derived view、compression fidelity 与可恢复 bookkeeping 分开。
<!-- existing:SF-2026-ARXIV-2606-29522:end -->
<!-- delta:SF-2026-ARXIV-2606-29522:start -->
Scratchpad 不能仅按可见文本保存；因果干预结果应把其中哪些 register 实际驱动后续输出记录成 request-local diagnostic state。该 probe 只拥有观测/路由权，干预不稳定时回退原始 scratchpad 与外部 verifier，不能据此删除未被识别的约束。
<!-- delta:SF-2026-ARXIV-2606-29522:end -->
<!-- books-review:SF-2026-ARXIV-2606-29522:start -->
已重读 `books/part-07-agent/75-context.md#L16` 与相邻章 `books/part-07-agent/74-prompt.md#L187`；决定 `Integrate`。只在 Q8/D8 合成 transition task、Qwen2.5-Coder-7B 与 Mistral-7B-v0.3 上证明特定 written state 被因果读取；显式 scratchpad 的其他 token、自然语言推理和真实 Agent memory 均未被证明忠实。probe 不稳定时保留原文本与外部 verifier。
<!-- books-review:SF-2026-ARXIV-2606-29522:end -->

<!-- existing:SF-2026-ARXIV-2606-29526:start -->
当前章已把 terminal reward 拆为 typed trajectory credit，并记录 verifier、policy freshness 与 off-policy 边界。
<!-- existing:SF-2026-ARXIV-2606-29526:end -->
<!-- delta:SF-2026-ARXIV-2606-29526:start -->
把多阶段策略改进与验证门控组织成训练控制流。
<!-- delta:SF-2026-ARXIV-2606-29526:end -->
<!-- books-review:SF-2026-ARXIV-2606-29526:start -->
已重读 `books/part-04-training-system/33-grpo.md#L879` 与相邻章 `books/part-04-training-system/32-ppo.md#L342`；决定 `No Change — Existing Coverage`。把多阶段策略改进与验证门控组织成训练控制流。《The Mirage of Optimizing Training Policies: Monotonic Inference Policies as the Real Objective for LLM Reinforcement Learning》的正证据锚定 `5 Experiments`；`Limitations` 没有建立跨 reward/verifier、policy freshness 与分布漂移的 on-policy 有效性。因此该证据只能修正当前判断，超界时 `TRAIN-GRPO` 必须恢复 on-policy terminal/verifier baseline。
<!-- books-review:SF-2026-ARXIV-2606-29526:end -->

<!-- existing:SF-2026-ARXIV-2606-29532:start -->
当前章已拥有 typed query plan、router、metric/index identity、evidence sufficiency 与失败回退。
<!-- existing:SF-2026-ARXIV-2606-29532:end -->
<!-- delta:SF-2026-ARXIV-2606-29532:start -->
把语义 join 的候选生成、验证与代价纳入查询计划。
<!-- delta:SF-2026-ARXIV-2606-29532:end -->
<!-- books-review:SF-2026-ARXIV-2606-29532:start -->
已重读 `books/part-07-agent/76-rag.md#L51` 与相邻章 `books/part-07-agent/77-memory.md#L1017`；决定 `No Change — Existing Coverage`。把语义 join 的候选生成、验证与代价纳入查询计划。《SemJoin: Semantic Join Optimization》的正证据锚定 `4 Evaluation`；`Conclusion and evaluated-database scope` 没有建立跨 corpus、query distribution、retriever/index revision 与生成器的检索收益。因此该证据只能修正当前判断，超界时 `AGENT-RAG` 必须恢复固定、已校准的 retrieval plan。
<!-- books-review:SF-2026-ARXIV-2606-29532:end -->

<!-- existing:SF-2026-ARXIV-2606-29537:start -->
当前章已把 dataset/model/evaluator/metric/release 分权，并要求 slice、校准、污染与反例证据。
<!-- existing:SF-2026-ARXIV-2606-29537:end -->
<!-- delta:SF-2026-ARXIV-2606-29537:start -->
把 OSWorld 环境、任务与判定器升级为版本化 release contract。
<!-- delta:SF-2026-ARXIV-2606-29537:end -->
<!-- books-review:SF-2026-ARXIV-2606-29537:start -->
已重读 `books/part-06-ai-infrastructure/66-evaluation-system.md#L193` 与相邻章 `books/part-06-ai-infrastructure/59-model-registry.md#L144`；决定 `No Change — Existing Coverage`。把 OSWorld 环境、任务与判定器升级为版本化 release contract。《OSWorld 2.0: Benchmarking Computer Use Agents on Long-Horizon Real-World Tasks》的正证据锚定 `2 OSWorld 2.0 Benchmark; evaluation protocol`；`6 Limitations` 没有建立跨 dataset/model/evaluator revision 的 release acceptance 或生产 SLO。因此该证据只能修正当前判断，超界时 `PLATFORM-EVALUATION-SYSTEM` 必须保持 release Gate Open 并恢复完整分层评测。
<!-- books-review:SF-2026-ARXIV-2606-29537:end -->

<!-- existing:SF-2026-ARXIV-2606-29538:start -->
当前章已拥有 versioned state machine、DAG、evaluator-driven search、replay 与 compensation。
<!-- existing:SF-2026-ARXIV-2606-29538:end -->
<!-- delta:SF-2026-ARXIV-2606-29538:start -->
把资源发现转成可执行 skill，并保留权限与失败边界。
<!-- delta:SF-2026-ARXIV-2606-29538:end -->
<!-- books-review:SF-2026-ARXIV-2606-29538:start -->
已重读 `books/part-07-agent/81-workflow.md#L36` 与相邻章 `books/part-07-agent/78-tool-calling.md#L301`；决定 `No Change — Existing Coverage`。把资源发现转成可执行 skill，并保留权限与失败边界。《RESOURCE2SKILL: Distilling Executable Agent Skills from Human-Created Multimodal Resources》的正证据锚定 `4 Experiments`；`M Limitations` 没有建立跨 environment、tool semantics、checkpoint 与 compensation path 的可复算性。因此该证据只能修正当前判断，超界时 `AGENT-WORKFLOW` 必须停在可恢复 checkpoint 并执行 compensation。
<!-- books-review:SF-2026-ARXIV-2606-29538:end -->

<!-- existing:SF-2026-ARXIV-2606-29541:start -->
当前章已拥有 topology、message/state、aggregation、delegation、independent verification 与 coordination tax。
<!-- existing:SF-2026-ARXIV-2606-29541:end -->
<!-- delta:SF-2026-ARXIV-2606-29541:start -->
把 MARL 协调的共享意图与通信失效纳入状态。
<!-- delta:SF-2026-ARXIV-2606-29541:end -->
<!-- books-review:SF-2026-ARXIV-2606-29541:start -->
已重读 `books/part-07-agent/82-multi-agent.md#L380` 与相邻章 `books/part-07-agent/81-workflow.md#L702`；决定 `No Change — Existing Coverage`。把 MARL 协调的共享意图与通信失效纳入状态。《Learned Coordination Conventions in Cooperative MARL: Measuring the Translation Gap Between Theory-Informed Roles and Learned Routing》的正证据锚定 `5 Experiments`；`6 Discussion` 没有建立跨 agent population、message protocol、error correlation 与 coordination load 的聚合收益。因此该证据只能修正当前判断，超界时 `AGENT-MULTI-AGENT` 必须恢复单 Agent/串行协调与人工仲裁。
<!-- books-review:SF-2026-ARXIV-2606-29541:end -->

<!-- existing:SF-2026-ARXIV-2606-29544:start -->
当前章已把模型 sensor、policy/authorization 与 effect-time commit 分开，并拥有 fail-closed fallback。
<!-- existing:SF-2026-ARXIV-2606-29544:end -->
<!-- delta:SF-2026-ARXIV-2606-29544:start -->
把生产分布漂移、攻击与回退纳入鲁棒性发布证据。
<!-- delta:SF-2026-ARXIV-2606-29544:end -->
<!-- books-review:SF-2026-ARXIV-2606-29544:start -->
已重读 `books/part-06-ai-infrastructure/72-security.md#L418` 与相邻章 `books/part-06-ai-infrastructure/71-multi-tenant.md#L120`；决定 `No Change — Existing Coverage`。把生产分布漂移、攻击与回退纳入鲁棒性发布证据。《Proteus: Automated Adversarial Robustness Testing for Audio Deepfake Detectors》的正证据锚定 `3 Results`；`Conclusion and tested-shift boundary` 没有建立跨 threat distribution、attacker adaptation 与 effect-time authorization 的防护承诺。因此该证据只能修正当前判断，超界时 `PLATFORM-SECURITY` 必须拒绝 effect commit 并转 sandbox/人工。
<!-- books-review:SF-2026-ARXIV-2606-29544:end -->

<!-- existing:SF-2026-ARXIV-2606-29554:start -->
当前章已把 optimizer、schedule、batch/tokens 与 scaling identity 分开；新证据只有改变外推或控制合同才可追加。
<!-- existing:SF-2026-ARXIV-2606-29554:end -->
<!-- delta:SF-2026-ARXIV-2606-29554:start -->
揭示数据 shuffle 与 optimizer state 的耦合，改变复现合同。
<!-- delta:SF-2026-ARXIV-2606-29554:end -->
<!-- books-review:SF-2026-ARXIV-2606-29554:start -->
已重读 `books/part-04-training-system/28-pretraining.md#L263` 与相邻章 `books/part-04-training-system/27-data.md#L591`；决定 `No Change — Existing Coverage`。揭示数据 shuffle 与 optimizer state 的耦合，改变复现合同。《Optimizer Memory Makes Shuffle Order a First-Order Source of Fine-Tuning Noise》的正证据锚定 `5 Empirical evidence`；`7 Discussion` 没有建立跨 architecture、optimizer、token budget 与更大训练尺度的可迁移性。因此该证据只能修正当前判断，超界时 `TRAIN-PRETRAINING` 必须恢复邻近规模 sweep 与已验证 schedule。
<!-- books-review:SF-2026-ARXIV-2606-29554:end -->

<!-- existing:SF-2026-ARXIV-2606-29563:start -->
当前章已拥有 workload-aware eviction、风险门、可恢复 recall 与完整缓存回退。
<!-- existing:SF-2026-ARXIV-2606-29563:end -->
<!-- delta:SF-2026-ARXIV-2606-29563:start -->
用跨头跨层 coverage 状态驱动 KV 驱逐并保留完整缓存回退。
<!-- delta:SF-2026-ARXIV-2606-29563:end -->
<!-- books-review:SF-2026-ARXIV-2606-29563:start -->
已重读 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L222` 与相邻章 `books/part-05-inference-system/44-decode.md#L222`；决定 `No Change — Existing Coverage`。用跨头跨层 coverage 状态驱动 KV 驱逐并保留完整缓存回退。《Coverage-Driven KV Cache Eviction for Efficient and Improved Inference of LLM》的正证据锚定 `5 Experiments; 5.1 Experimental setup`；`5.3 Discussion; 5.3.5 Computational Complexity` 没有建立跨 attention pattern、context length 与 workload shift 的 eviction 安全性。因此该证据只能修正当前判断，超界时 `INFER-KV-CACHE` 必须恢复完整 KV 或保守 eviction。
<!-- books-review:SF-2026-ARXIV-2606-29563:end -->

<!-- existing:SF-2026-ARXIV-2606-29565:start -->
当前章已定义 ARRIVED 到 RELEASED 的请求状态机，但尚未拥有跨请求 idle-time speculative state。
<!-- existing:SF-2026-ARXIV-2606-29565:end -->
<!-- delta:SF-2026-ARXIV-2606-29565:start -->
有状态会话的 idle time 可用于推演到下个 decision point；request lifecycle owner 保存 speculative state、acceptance confidence 与 base-state identity，命中后才原子提交。False accept、用户输入或 state drift 立即作废预推进并回退正常 decode。
<!-- delta:SF-2026-ARXIV-2606-29565:end -->
<!-- books-review:SF-2026-ARXIV-2606-29565:start -->
已重读 `books/part-05-inference-system/42-what-happens-during-inference.md#L80` 与相邻章 `books/part-05-inference-system/43-prefill.md#L297`；决定 `Integrate`。只在 LayerScale 专有 engine、单 H100、70B-class 4-bit target 上测得 capability-gated fast path；8B BF16 不触发 gate，且大量收益为测量常数上的闭式推导。任何 state mutation 或置信漂移都必须 invalidate 并恢复普通 decode。
<!-- books-review:SF-2026-ARXIV-2606-29565:end -->

<!-- existing:SF-2026-ARXIV-2606-29567:start -->
当前章已把模型 sensor、policy/authorization 与 effect-time commit 分开，并拥有 fail-closed fallback。
<!-- existing:SF-2026-ARXIV-2606-29567:end -->
<!-- delta:SF-2026-ARXIV-2606-29567:start -->
把 PII 替身生成、加密映射与还原置于本地代理控制面。
<!-- delta:SF-2026-ARXIV-2606-29567:end -->
<!-- books-review:SF-2026-ARXIV-2606-29567:start -->
已重读 `books/part-06-ai-infrastructure/72-security.md#L418` 与相邻章 `books/part-06-ai-infrastructure/71-multi-tenant.md#L120`；决定 `No Change — Existing Coverage`。把 PII 替身生成、加密映射与还原置于本地代理控制面。《SurrogateShield: Beyond Redaction for High-Utility, Privacy-Preserving LLM Interactions》的正证据锚定 `4 Evaluation Methodology`；`6 Discussion` 没有建立跨 threat distribution、attacker adaptation 与 effect-time authorization 的防护承诺。因此该证据只能修正当前判断，超界时 `PLATFORM-SECURITY` 必须拒绝 effect commit 并转 sandbox/人工。
<!-- books-review:SF-2026-ARXIV-2606-29567:end -->

<!-- existing:SF-2026-ARXIV-2606-29571:start -->
当前章已拥有 typed query plan、router、metric/index identity、evidence sufficiency 与失败回退。
<!-- existing:SF-2026-ARXIV-2606-29571:end -->
<!-- delta:SF-2026-ARXIV-2606-29571:start -->
Embedding distance 不应固定为 cosine；retrieval owner 先测 anisotropy，再在同一 corpus/query revision 上选择 cosine、rank 或 L1 类 metric，并把 metric 写入 index identity。诊断漂移或收益不稳时回退已校准 cosine/混合检索。
<!-- delta:SF-2026-ARXIV-2606-29571:end -->
<!-- books-review:SF-2026-ARXIV-2606-29571:start -->
已重读 `books/part-07-agent/76-rag.md#L51` 与相邻章 `books/part-07-agent/77-memory.md#L1017`；决定 `Integrate`。只比较 19 个 parameter-free metric、19 encoder 与七个静态数据集；0.01 crowded split、dominant-direction removal 和相关性未证明在线 corpus 漂移下的因果门槛，也未覆盖 learned metric。收益消失时恢复已校准 cosine/混合检索。
<!-- books-review:SF-2026-ARXIV-2606-29571:end -->

<!-- existing:SF-2026-ARXIV-2606-29573:start -->
当前章已把 dataset/model/evaluator/metric/release 分权，并要求 slice、校准、污染与反例证据。
<!-- existing:SF-2026-ARXIV-2606-29573:end -->
<!-- delta:SF-2026-ARXIV-2606-29573:start -->
把多模态生成粒度与可靠性共同纳入发布阈值。
<!-- delta:SF-2026-ARXIV-2606-29573:end -->
<!-- books-review:SF-2026-ARXIV-2606-29573:start -->
已重读 `books/part-06-ai-infrastructure/66-evaluation-system.md#L193` 与相邻章 `books/part-06-ai-infrastructure/59-model-registry.md#L144`；决定 `No Change — Existing Coverage`。把多模态生成粒度与可靠性共同纳入发布阈值。《Reliability-Prioritized Fine-Grained Generation in Multimodal Large》的正证据锚定 `2.1 MLLM Benchmarks; experiments`；`Conclusion and expert-verified benchmark scope` 没有建立跨 dataset/model/evaluator revision 的 release acceptance 或生产 SLO。因此该证据只能修正当前判断，超界时 `PLATFORM-EVALUATION-SYSTEM` 必须保持 release Gate Open 并恢复完整分层评测。
<!-- books-review:SF-2026-ARXIV-2606-29573:end -->

<!-- existing:SF-2026-ARXIV-2606-29581:start -->
当前章已把模型 sensor、policy/authorization 与 effect-time commit 分开，并拥有 fail-closed fallback。
<!-- existing:SF-2026-ARXIV-2606-29581:end -->
<!-- delta:SF-2026-ARXIV-2606-29581:start -->
量化验收与 sampling temperature 不能分开：security release matrix 必须联合保存 model/quantization/sampler/multi-sample identity，并在多个 safety benchmark 上检查交互失稳。任一切片回归时回退已验收 precision/decoding 配置，而不是只恢复 greedy 单次测试。
<!-- delta:SF-2026-ARXIV-2606-29581:end -->
<!-- books-review:SF-2026-ARXIV-2606-29581:start -->
已重读 `books/part-06-ai-infrastructure/72-security.md#L418` 与相邻章 `books/part-06-ai-infrastructure/71-multi-tenant.md#L120`；决定 `Integrate`。当前 official exact-v1 的 Abstract 与 §3 一致披露 9 models、161 configurations、AdvBench+XSTest 与约 322k responses；证据只覆盖以 Pile validation calibration 的 AWQ INT4/GPTQ INT8、2B–8B 模型与静态 AdvBench，未证明 NF4/GGUF/对抗式 calibration、>70B、adaptive jailbreak/prompt injection 或 judge 完美可靠。任一切片回归即恢复已验收 precision/sampler。
<!-- books-review:SF-2026-ARXIV-2606-29581:end -->

<!-- existing:SF-2026-ARXIV-2606-29601:start -->
当前章已拥有 topology、message/state、aggregation、delegation、independent verification 与 coordination tax。
<!-- existing:SF-2026-ARXIV-2606-29601:end -->
<!-- delta:SF-2026-ARXIV-2606-29601:start -->
异步多 Agent 协议应把 attribute-setting priority、action conflict 与禁止组合编译为 sayso/nono/nogo 等声明式状态，再由协议 runtime 决定可提交 transition。规则冲突或编译覆盖不足时回退串行 coordinator/人工仲裁。
<!-- delta:SF-2026-ARXIV-2606-29601:end -->
<!-- books-review:SF-2026-ARXIV-2606-29601:start -->
已重读 `books/part-07-agent/82-multi-agent.md#L380` 与相邻章 `books/part-07-agent/81-workflow.md#L702`；决定 `Integrate`。只验证有限 Langshaw examples 到 BSPL tableau 的 safety/liveness 与编译时间；未证明开放网络中的 delivery、identity、Byzantine role 或工具副作用。协议编译/验证超界时回到串行 coordinator 与人工仲裁。
<!-- books-review:SF-2026-ARXIV-2606-29601:end -->

<!-- existing:SF-2026-ARXIV-2606-29602:start -->
当前章已把模型 sensor、policy/authorization 与 effect-time commit 分开，并拥有 fail-closed fallback。
<!-- existing:SF-2026-ARXIV-2606-29602:end -->
<!-- delta:SF-2026-ARXIV-2606-29602:start -->
把多语言、编码与多阶段 prompt injection 纳入威胁矩阵。
<!-- delta:SF-2026-ARXIV-2606-29602:end -->
<!-- books-review:SF-2026-ARXIV-2606-29602:start -->
已重读 `books/part-06-ai-infrastructure/72-security.md#L418` 与相邻章 `books/part-06-ai-infrastructure/71-multi-tenant.md#L120`；决定 `No Change — Existing Coverage`。把多语言、编码与多阶段 prompt injection 纳入威胁矩阵。《An Empirical Evaluation of Prompt Injection Vulnerabilities in Large Language Models Across Multilingual and Obfuscated Attack Scenarios》的正证据锚定 `II-D Empirical Evaluations of LLM Safety; IV Results`；`V Discussion` 没有建立跨 threat distribution、attacker adaptation 与 effect-time authorization 的防护承诺。因此该证据只能修正当前判断，超界时 `PLATFORM-SECURITY` 必须拒绝 effect commit 并转 sandbox/人工。
<!-- books-review:SF-2026-ARXIV-2606-29602:end -->

<!-- existing:SF-2026-ARXIV-2606-29604:start -->
当前章已把模型 sensor、policy/authorization 与 effect-time commit 分开，并拥有 fail-closed fallback。
<!-- existing:SF-2026-ARXIV-2606-29604:end -->
<!-- delta:SF-2026-ARXIV-2606-29604:start -->
把权重/激活扰动用于潜在行为发现并定义代理选择边界。
<!-- delta:SF-2026-ARXIV-2606-29604:end -->
<!-- books-review:SF-2026-ARXIV-2606-29604:start -->
已重读 `books/part-06-ai-infrastructure/72-security.md#L418` 与相邻章 `books/part-06-ai-infrastructure/71-multi-tenant.md#L120`；决定 `No Change — Existing Coverage`。把权重/激活扰动用于潜在行为发现并定义代理选择边界。《Mechanistically Eliciting Latent Behaviors in Language Models》的正证据锚定 `Experimental setup; latent-behavior evaluation`；`Conclusion and model-organism scope` 没有建立跨 threat distribution、attacker adaptation 与 effect-time authorization 的防护承诺。因此该证据只能修正当前判断，超界时 `PLATFORM-SECURITY` 必须拒绝 effect commit 并转 sandbox/人工。
<!-- books-review:SF-2026-ARXIV-2606-29604:end -->

<!-- existing:SF-2026-ARXIV-2606-29605:start -->
当前章已拥有 provenance、dedup、contamination 与 typed lineage；单一归因或语料案例不自动形成新命题。
<!-- existing:SF-2026-ARXIV-2606-29605:end -->
<!-- delta:SF-2026-ARXIV-2606-29605:start -->
把生成语料的 provenance、复制与跨记录冗余转成训练前数据控制状态。
<!-- delta:SF-2026-ARXIV-2606-29605:end -->
<!-- books-review:SF-2026-ARXIV-2606-29605:start -->
已重读 `books/part-04-training-system/27-data.md#L484` 与相邻章 `books/part-04-training-system/28-pretraining.md#L702`；决定 `No Change — Existing Coverage`。把生成语料的 provenance、复制与跨记录冗余转成训练前数据控制状态。《How much of an LLM-generated clinical corpus is actually new? A production-scale measurement of content redundancy for provenance classification》的正证据锚定 `2 Results; downstream equal-token adaptation test`；`3 Discussion` 没有建立跨 corpus、训练阶段与真实删除/重训操作的因果有效性。因此该证据只能修正当前判断，超界时 `TRAIN-DATA` 必须保留原样本、lineage 与重训对照。
<!-- books-review:SF-2026-ARXIV-2606-29605:end -->

<!-- existing:SF-2026-ARXIV-2606-29623:start -->
当前章已把 dataset/model/evaluator/metric/release 分权，并要求 slice、校准、污染与反例证据。
<!-- existing:SF-2026-ARXIV-2606-29623:end -->
<!-- delta:SF-2026-ARXIV-2606-29623:start -->
高风险 release 不能用普通 Monte Carlo 的零观察失败推断安全；SCARCE 类 cascade 将 rare-event region、latent ruler、停止条件与概率上界保存为验收证据。Ruler/分布假设失效时恢复更保守采样或保持 Gate Open。
<!-- delta:SF-2026-ARXIV-2606-29623:end -->
<!-- books-review:SF-2026-ARXIV-2606-29623:start -->
已重读 `books/part-06-ai-infrastructure/66-evaluation-system.md#L193` 与相邻章 `books/part-06-ai-infrastructure/59-model-registry.md#L144`；决定 `Integrate`。MNIST 与 Llama-Guard hidden-state jailbreak fleet 只验证经校准 ruler 的 rare-event estimate；论文明确指出 behavioral fleet 约 2,000 variants 仍不足、Mahalanobis ruler 可结构性失效，跨 corpus 必须重新校准。否则 Gate 保持 Open。
<!-- books-review:SF-2026-ARXIV-2606-29623:end -->

<!-- existing:SF-2026-ARXIV-2606-29629:start -->
当前章已把 routing、placement、energy/thermal、SLO 与 topology state 纳入调度控制。
<!-- existing:SF-2026-ARXIV-2606-29629:end -->
<!-- delta:SF-2026-ARXIV-2606-29629:start -->
让软件 DVFS controller 持有多模态 serving 阶段、功耗与热状态。
<!-- delta:SF-2026-ARXIV-2606-29629:end -->
<!-- books-review:SF-2026-ARXIV-2606-29629:start -->
已重读 `books/part-05-inference-system/56-inference-scheduling.md#L183` 与相邻章 `books/part-05-inference-system/46-continuous-batching.md#L216`；决定 `No Change — Existing Coverage`。让软件 DVFS controller 持有多模态 serving 阶段、功耗与热状态。《Energy-Efficient Multimodal Inference Serving with Tri-serve》的正证据锚定 `II-C1 Frequency-locked Roofline Benchmarking; IV Evaluation`；`V Conclusion; evaluated Qwen-Omni/GPU-cluster boundary` 没有建立跨 topology、并发负载、thermal state 与 SLO 的调度收益。因此该证据只能修正当前判断，超界时 `INFER-SCHEDULING` 必须恢复静态 placement 与保守 SLO headroom。
<!-- books-review:SF-2026-ARXIV-2606-29629:end -->

<!-- existing:SF-2026-ARXIV-2606-29645:start -->
当前章已拥有 typed query plan、router、metric/index identity、evidence sufficiency 与失败回退。
<!-- existing:SF-2026-ARXIV-2606-29645:end -->
<!-- delta:SF-2026-ARXIV-2606-29645:start -->
把 metadata、结构与 multi-hop strategy 分解为可单独验收的 RAG 控制变量。
<!-- delta:SF-2026-ARXIV-2606-29645:end -->
<!-- books-review:SF-2026-ARXIV-2606-29645:start -->
已重读 `books/part-07-agent/76-rag.md#L51` 与相邻章 `books/part-07-agent/77-memory.md#L1017`；决定 `No Change — Existing Coverage`。把 metadata、结构与 multi-hop strategy 分解为可单独验收的 RAG 控制变量。《Metadata, Structure, or Strategy? A Decomposition of RAG Context Enrichment》的正证据锚定 `3.2 Experimental Design; results across six benchmarks`；`6.1 Limitations` 没有建立跨 corpus、query distribution、retriever/index revision 与生成器的检索收益。因此该证据只能修正当前判断，超界时 `AGENT-RAG` 必须恢复固定、已校准的 retrieval plan。
<!-- books-review:SF-2026-ARXIV-2606-29645:end -->

<!-- existing:SF-2026-ARXIV-2606-29646:start -->
当前章已把模型 sensor、policy/authorization 与 effect-time commit 分开，并拥有 fail-closed fallback。
<!-- existing:SF-2026-ARXIV-2606-29646:end -->
<!-- delta:SF-2026-ARXIV-2606-29646:start -->
把 sleeper behavior elicitation 的 fuzzing、代理调参与 oracle 边界分开。
<!-- delta:SF-2026-ARXIV-2606-29646:end -->
<!-- books-review:SF-2026-ARXIV-2606-29646:start -->
已重读 `books/part-06-ai-infrastructure/72-security.md#L418` 与相邻章 `books/part-06-ai-infrastructure/71-multi-tenant.md#L120`；决定 `No Change — Existing Coverage`。把 sleeper behavior elicitation 的 fuzzing、代理调参与 oracle 边界分开。《Fuzzing Large Language Models to Elicit Hidden Behaviours》的正证据锚定 `3 Results`；`4 Discussion` 没有建立跨 threat distribution、attacker adaptation 与 effect-time authorization 的防护承诺。因此该证据只能修正当前判断，超界时 `PLATFORM-SECURITY` 必须拒绝 effect commit 并转 sandbox/人工。
<!-- books-review:SF-2026-ARXIV-2606-29646:end -->

<!-- existing:SF-2026-ARXIV-2606-29648:start -->
当前章已拥有 typed query plan、router、metric/index identity、evidence sufficiency 与失败回退。
<!-- existing:SF-2026-ARXIV-2606-29648:end -->
<!-- delta:SF-2026-ARXIV-2606-29648:start -->
让 meta-agent 从失败轨迹重写多检索器编排策略。
<!-- delta:SF-2026-ARXIV-2606-29648:end -->
<!-- books-review:SF-2026-ARXIV-2606-29648:start -->
已重读 `books/part-07-agent/76-rag.md#L51` 与相邻章 `books/part-07-agent/77-memory.md#L1017`；决定 `No Change — Existing Coverage`。让 meta-agent 从失败轨迹重写多检索器编排策略。《Hybrid Retriever Evolution for Multimodal Document Reasoning Agents》的正证据锚定 `4 Experiments`；`A Limitations` 没有建立跨 corpus、query distribution、retriever/index revision 与生成器的检索收益。因此该证据只能修正当前判断，超界时 `AGENT-RAG` 必须恢复固定、已校准的 retrieval plan。
<!-- books-review:SF-2026-ARXIV-2606-29648:end -->

<!-- existing:SF-2026-ARXIV-2606-29649:start -->
当前章已把模型 sensor、policy/authorization 与 effect-time commit 分开，并拥有 fail-closed fallback。
<!-- existing:SF-2026-ARXIV-2606-29649:end -->
<!-- delta:SF-2026-ARXIV-2606-29649:start -->
把分辨率、字符构造与语言纳入 VLM moderation 威胁面。
<!-- delta:SF-2026-ARXIV-2606-29649:end -->
<!-- books-review:SF-2026-ARXIV-2606-29649:start -->
已重读 `books/part-06-ai-infrastructure/72-security.md#L418` 与相邻章 `books/part-06-ai-infrastructure/71-multi-tenant.md#L120`；决定 `No Change — Existing Coverage`。把分辨率、字符构造与语言纳入 VLM moderation 威胁面。《Resolution Thresholds in VLM Detection of Harmful ASCII Art Across Construction Modes and Languages》的正证据锚定 `3.2 VLM Evaluation`；`5 Discussion` 没有建立跨 threat distribution、attacker adaptation 与 effect-time authorization 的防护承诺。因此该证据只能修正当前判断，超界时 `PLATFORM-SECURITY` 必须拒绝 effect commit 并转 sandbox/人工。
<!-- books-review:SF-2026-ARXIV-2606-29649:end -->

<!-- existing:SF-2026-ARXIV-2606-29652:start -->
当前章已拥有 typed query plan、router、metric/index identity、evidence sufficiency 与失败回退。
<!-- existing:SF-2026-ARXIV-2606-29652:end -->
<!-- delta:SF-2026-ARXIV-2606-29652:start -->
把索引、模型与推理默认置于用户设备，并把远端服务降为可选路径。
<!-- delta:SF-2026-ARXIV-2606-29652:end -->
<!-- books-review:SF-2026-ARXIV-2606-29652:start -->
已重读 `books/part-07-agent/76-rag.md#L51` 与相邻章 `books/part-07-agent/77-memory.md#L1017`；决定 `No Change — Existing Coverage`。把索引、模型与推理默认置于用户设备，并把远端服务降为可选路径。《As We May Search》的正证据锚定 `4.1 Experimental Setup; five benchmarks and 1K-1M documents`；`4.11 Limitations` 没有建立跨 corpus、query distribution、retriever/index revision 与生成器的检索收益。因此该证据只能修正当前判断，超界时 `AGENT-RAG` 必须恢复固定、已校准的 retrieval plan。
<!-- books-review:SF-2026-ARXIV-2606-29652:end -->

<!-- existing:SF-2026-ARXIV-2606-29654:start -->
当前章已拥有 topology、message/state、aggregation、delegation、independent verification 与 coordination tax。
<!-- existing:SF-2026-ARXIV-2606-29654:end -->
<!-- delta:SF-2026-ARXIV-2606-29654:start -->
多 Agent deliberation 的 automation 权由预先声明的 wrong-action budget 和 local reliability lower bound 决定；controller 记录 act/defer 与预算消耗，低于下界即升级或拒答。校准失效时回退全 defer/人工，不用事后挑阈值美化覆盖率。
<!-- delta:SF-2026-ARXIV-2606-29654:end -->
<!-- books-review:SF-2026-ARXIV-2606-29654:start -->
已重读 `books/part-07-agent/82-multi-agent.md#L380` 与相邻章 `books/part-07-agent/81-workflow.md#L702`；决定 `Integrate`。保证依赖 local bias envelope、representation-gap bound 与 calibration split，并非 distribution-free；六个选择题 benchmark 与训练期 difficulty-normalized budget 未证明开放式任务或分布漂移。诊断失败时全 defer/人工。
<!-- books-review:SF-2026-ARXIV-2606-29654:end -->

<!-- existing:SF-2026-ARXIV-2606-29657:start -->
当前章已把模型 sensor、policy/authorization 与 effect-time commit 分开，并拥有 fail-closed fallback。
<!-- existing:SF-2026-ARXIV-2606-29657:end -->
<!-- delta:SF-2026-ARXIV-2606-29657:start -->
把预测器训练与下游行动奖励隔离，并把 agency 留给受约束 scaffolding。
<!-- delta:SF-2026-ARXIV-2606-29657:end -->
<!-- books-review:SF-2026-ARXIV-2606-29657:start -->
已重读 `books/part-06-ai-infrastructure/72-security.md#L418` 与相邻章 `books/part-06-ai-infrastructure/71-multi-tenant.md#L120`；决定 `No Change — Existing Coverage`。把预测器训练与下游行动奖励隔离，并把 agency 留给受约束 scaffolding。《Safety from Honesty in a Disinterested AI Predictor》的正证据锚定 `Formal safety argument and falsifiability analysis`；`5.4.2 Falsifiability, Scope, and Requirements for a Concrete Design` 没有建立跨 threat distribution、attacker adaptation 与 effect-time authorization 的防护承诺。因此该证据只能修正当前判断，超界时 `PLATFORM-SECURITY` 必须拒绝 effect commit 并转 sandbox/人工。
<!-- books-review:SF-2026-ARXIV-2606-29657:end -->

<!-- existing:SF-2026-ARXIV-2606-29661:start -->
当前章已拥有 topology、message/state、aggregation、delegation、independent verification 与 coordination tax。
<!-- existing:SF-2026-ARXIV-2606-29661:end -->
<!-- delta:SF-2026-ARXIV-2606-29661:start -->
让 ensemble controller 同时优化预测质量与跨模型错误多样性。
<!-- delta:SF-2026-ARXIV-2606-29661:end -->
<!-- books-review:SF-2026-ARXIV-2606-29661:start -->
已重读 `books/part-07-agent/82-multi-agent.md#L380` 与相邻章 `books/part-07-agent/81-workflow.md#L702`；决定 `No Change — Existing Coverage`。让 ensemble controller 同时优化预测质量与跨模型错误多样性。《Diversity is the Strength of the AI Crowd》的正证据锚定 `5 Results`；`6 Discussion` 没有建立跨 agent population、message protocol、error correlation 与 coordination load 的聚合收益。因此该证据只能修正当前判断，超界时 `AGENT-MULTI-AGENT` 必须恢复单 Agent/串行协调与人工仲裁。
<!-- books-review:SF-2026-ARXIV-2606-29661:end -->

<!-- existing:SF-2026-ARXIV-2606-30686:start -->
当前章已把 dataset/model/evaluator/metric/release 分权，并要求 slice、校准、污染与反例证据。
<!-- existing:SF-2026-ARXIV-2606-30686:end -->
<!-- delta:SF-2026-ARXIV-2606-30686:start -->
把 VLA 的语义匹配与物理动作泛化拆成可识别因果评测。
<!-- delta:SF-2026-ARXIV-2606-30686:end -->
<!-- books-review:SF-2026-ARXIV-2606-30686:start -->
已重读 `books/part-06-ai-infrastructure/66-evaluation-system.md#L193` 与相邻章 `books/part-06-ai-infrastructure/59-model-registry.md#L144`；决定 `No Change — Existing Coverage`。把 VLA 的语义匹配与物理动作泛化拆成可识别因果评测。《Position: Vision-Language-Action Models Cannot Be Verified to Perform Physical Reasoning》的正证据锚定 `3.2 Three Levels of Non-Identifiability in Current Evaluation`；`Conclusion and proposed controlled-variation scope` 没有建立跨 dataset/model/evaluator revision 的 release acceptance 或生产 SLO。因此该证据只能修正当前判断，超界时 `PLATFORM-EVALUATION-SYSTEM` 必须保持 release Gate Open 并恢复完整分层评测。
<!-- books-review:SF-2026-ARXIV-2606-30686:end -->

<!-- existing:SF-2026-ARXIV-2606-30689:start -->
当前章已拥有 versioned state machine、DAG、evaluator-driven search、replay 与 compensation。
<!-- existing:SF-2026-ARXIV-2606-30689:end -->
<!-- delta:SF-2026-ARXIV-2606-30689:start -->
把逐行需求 citation 变成可自动检测幻觉的 provenance 合同。
<!-- delta:SF-2026-ARXIV-2606-30689:end -->
<!-- books-review:SF-2026-ARXIV-2606-30689:start -->
已重读 `books/part-07-agent/81-workflow.md#L36` 与相邻章 `books/part-07-agent/78-tool-calling.md#L301`；决定 `No Change — Existing Coverage`。把逐行需求 citation 变成可自动检测幻觉的 provenance 合同。《Citation Discipline in Spec-Driven Development: A Cross-Model Empirical Study of Output Determinism and Automated Hallucination Detection in LLM-Generated Code》的正证据锚定 `4 Experimental Design; cross-model results`；`7 Discussion` 没有建立跨 environment、tool semantics、checkpoint 与 compensation path 的可复算性。因此该证据只能修正当前判断，超界时 `AGENT-WORKFLOW` 必须停在可恢复 checkpoint 并执行 compensation。
<!-- books-review:SF-2026-ARXIV-2606-30689:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260629-COVERAGE-V1 | fresh-context:jun29-denominator-fresh-v2 | coverage | coverage:SRC-ARXIV:20260629 | none | 262/262 checked; prior FN 2606.29328 resolved; final freeze 86/176; 52/52 route-negative checked | passed |
| SA-20260629-EVIDENCE-V1 | fresh-context:jun29-postwrite-v1 | evidence | review:SF-2026-ARXIV-2606-29142; review:SF-2026-ARXIV-2606-29150; review:SF-2026-ARXIV-2606-29151; review:SF-2026-ARXIV-2606-29158; review:SF-2026-ARXIV-2606-29159; review:SF-2026-ARXIV-2606-29171; review:SF-2026-ARXIV-2606-29176; review:SF-2026-ARXIV-2606-29178; review:SF-2026-ARXIV-2606-29182; review:SF-2026-ARXIV-2606-29184; review:SF-2026-ARXIV-2606-29193; review:SF-2026-ARXIV-2606-29194; review:SF-2026-ARXIV-2606-29196; review:SF-2026-ARXIV-2606-29207; review:SF-2026-ARXIV-2606-29215; review:SF-2026-ARXIV-2606-29222; review:SF-2026-ARXIV-2606-29223; review:SF-2026-ARXIV-2606-29225; review:SF-2026-ARXIV-2606-29228; review:SF-2026-ARXIV-2606-29237; review:SF-2026-ARXIV-2606-29238; review:SF-2026-ARXIV-2606-29239; review:SF-2026-ARXIV-2606-29251; review:SF-2026-ARXIV-2606-29270; review:SF-2026-ARXIV-2606-29275; review:SF-2026-ARXIV-2606-29278; review:SF-2026-ARXIV-2606-29279; review:SF-2026-ARXIV-2606-29280; review:SF-2026-ARXIV-2606-29282; review:SF-2026-ARXIV-2606-29296; review:SF-2026-ARXIV-2606-29315; review:SF-2026-ARXIV-2606-29328; review:SF-2026-ARXIV-2606-29337; review:SF-2026-ARXIV-2606-29340; review:SF-2026-ARXIV-2606-29350; review:SF-2026-ARXIV-2606-29354; review:SF-2026-ARXIV-2606-29366; review:SF-2026-ARXIV-2606-29377; review:SF-2026-ARXIV-2606-29399; review:SF-2026-ARXIV-2606-29403; review:SF-2026-ARXIV-2606-29424; review:SF-2026-ARXIV-2606-29425; review:SF-2026-ARXIV-2606-29441; review:SF-2026-ARXIV-2606-29445; review:SF-2026-ARXIV-2606-29472; review:SF-2026-ARXIV-2606-29476; review:SF-2026-ARXIV-2606-29481; review:SF-2026-ARXIV-2606-29490; review:SF-2026-ARXIV-2606-29493; review:SF-2026-ARXIV-2606-29501; review:SF-2026-ARXIV-2606-29502; review:SF-2026-ARXIV-2606-29506; review:SF-2026-ARXIV-2606-29520; review:SF-2026-ARXIV-2606-29522; review:SF-2026-ARXIV-2606-29526; review:SF-2026-ARXIV-2606-29532; review:SF-2026-ARXIV-2606-29537; review:SF-2026-ARXIV-2606-29538; review:SF-2026-ARXIV-2606-29541; review:SF-2026-ARXIV-2606-29544; review:SF-2026-ARXIV-2606-29554; review:SF-2026-ARXIV-2606-29563; review:SF-2026-ARXIV-2606-29565; review:SF-2026-ARXIV-2606-29567; review:SF-2026-ARXIV-2606-29571; review:SF-2026-ARXIV-2606-29573; review:SF-2026-ARXIV-2606-29580; review:SF-2026-ARXIV-2606-29581; review:SF-2026-ARXIV-2606-29592; review:SF-2026-ARXIV-2606-29601; review:SF-2026-ARXIV-2606-29602; review:SF-2026-ARXIV-2606-29604; review:SF-2026-ARXIV-2606-29605; review:SF-2026-ARXIV-2606-29623; review:SF-2026-ARXIV-2606-29629; review:SF-2026-ARXIV-2606-29645; review:SF-2026-ARXIV-2606-29646; review:SF-2026-ARXIV-2606-29648; review:SF-2026-ARXIV-2606-29649; review:SF-2026-ARXIV-2606-29652; review:SF-2026-ARXIV-2606-29654; review:SF-2026-ARXIV-2606-29657; review:SF-2026-ARXIV-2606-29661; review:SF-2026-ARXIV-2606-29679; review:SF-2026-ARXIV-2606-30686; review:SF-2026-ARXIV-2606-30689 | none | 86/86 exact-v1 locator, benchmark and source-specific boundary checks passed | passed |
| SA-20260629-SELECTION-V1 | fresh-context:jun29-postwrite-v1 | deep_analysis_selection | analysis-decision:SF-2026-ARXIV-2606-29142; analysis-decision:SF-2026-ARXIV-2606-29150; analysis:DA-20260629-2606-29151; analysis-decision:SF-2026-ARXIV-2606-29158; analysis-decision:SF-2026-ARXIV-2606-29159; analysis-decision:SF-2026-ARXIV-2606-29171; analysis-decision:SF-2026-ARXIV-2606-29176; analysis-decision:SF-2026-ARXIV-2606-29178; analysis-decision:SF-2026-ARXIV-2606-29182; analysis-decision:SF-2026-ARXIV-2606-29184; analysis-decision:SF-2026-ARXIV-2606-29193; analysis-decision:SF-2026-ARXIV-2606-29194; analysis-decision:SF-2026-ARXIV-2606-29196; analysis-decision:SF-2026-ARXIV-2606-29207; analysis-decision:SF-2026-ARXIV-2606-29215; analysis-decision:SF-2026-ARXIV-2606-29222; analysis-decision:SF-2026-ARXIV-2606-29223; analysis-decision:SF-2026-ARXIV-2606-29225; analysis-decision:SF-2026-ARXIV-2606-29228; analysis-decision:SF-2026-ARXIV-2606-29237; analysis-decision:SF-2026-ARXIV-2606-29238; analysis-decision:SF-2026-ARXIV-2606-29239; analysis-decision:SF-2026-ARXIV-2606-29251; analysis-decision:SF-2026-ARXIV-2606-29270; analysis-decision:SF-2026-ARXIV-2606-29275; analysis-decision:SF-2026-ARXIV-2606-29278; analysis-decision:SF-2026-ARXIV-2606-29279; analysis-decision:SF-2026-ARXIV-2606-29280; analysis-decision:SF-2026-ARXIV-2606-29282; analysis-decision:SF-2026-ARXIV-2606-29296; analysis-decision:SF-2026-ARXIV-2606-29315; analysis-decision:SF-2026-ARXIV-2606-29328; analysis-decision:SF-2026-ARXIV-2606-29337; analysis-decision:SF-2026-ARXIV-2606-29340; analysis-decision:SF-2026-ARXIV-2606-29350; analysis-decision:SF-2026-ARXIV-2606-29354; analysis-decision:SF-2026-ARXIV-2606-29366; analysis-decision:SF-2026-ARXIV-2606-29377; analysis-decision:SF-2026-ARXIV-2606-29399; analysis-decision:SF-2026-ARXIV-2606-29403; analysis-decision:SF-2026-ARXIV-2606-29424; analysis-decision:SF-2026-ARXIV-2606-29425; analysis-decision:SF-2026-ARXIV-2606-29441; analysis-decision:SF-2026-ARXIV-2606-29445; analysis-decision:SF-2026-ARXIV-2606-29472; analysis-decision:SF-2026-ARXIV-2606-29476; analysis-decision:SF-2026-ARXIV-2606-29481; analysis-decision:SF-2026-ARXIV-2606-29490; analysis-decision:SF-2026-ARXIV-2606-29493; analysis-decision:SF-2026-ARXIV-2606-29501; analysis-decision:SF-2026-ARXIV-2606-29502; analysis-decision:SF-2026-ARXIV-2606-29506; analysis-decision:SF-2026-ARXIV-2606-29520; analysis-decision:SF-2026-ARXIV-2606-29522; analysis-decision:SF-2026-ARXIV-2606-29526; analysis-decision:SF-2026-ARXIV-2606-29532; analysis-decision:SF-2026-ARXIV-2606-29537; analysis-decision:SF-2026-ARXIV-2606-29538; analysis-decision:SF-2026-ARXIV-2606-29541; analysis-decision:SF-2026-ARXIV-2606-29544; analysis-decision:SF-2026-ARXIV-2606-29554; analysis-decision:SF-2026-ARXIV-2606-29563; analysis:DA-20260629-2606-29565; analysis-decision:SF-2026-ARXIV-2606-29567; analysis-decision:SF-2026-ARXIV-2606-29571; analysis-decision:SF-2026-ARXIV-2606-29573; analysis-decision:SF-2026-ARXIV-2606-29580; analysis-decision:SF-2026-ARXIV-2606-29581; analysis-decision:SF-2026-ARXIV-2606-29592; analysis-decision:SF-2026-ARXIV-2606-29601; analysis-decision:SF-2026-ARXIV-2606-29602; analysis-decision:SF-2026-ARXIV-2606-29604; analysis-decision:SF-2026-ARXIV-2606-29605; analysis-decision:SF-2026-ARXIV-2606-29623; analysis-decision:SF-2026-ARXIV-2606-29629; analysis-decision:SF-2026-ARXIV-2606-29645; analysis-decision:SF-2026-ARXIV-2606-29646; analysis-decision:SF-2026-ARXIV-2606-29648; analysis-decision:SF-2026-ARXIV-2606-29649; analysis-decision:SF-2026-ARXIV-2606-29652; analysis:DA-20260629-2606-29654; analysis-decision:SF-2026-ARXIV-2606-29657; analysis-decision:SF-2026-ARXIV-2606-29661; analysis-decision:SF-2026-ARXIV-2606-29679; analysis-decision:SF-2026-ARXIV-2606-30686; analysis-decision:SF-2026-ARXIV-2606-30689 | none | 86/86 full frontier checked; three winners frozen | passed |
| SA-20260629-BOOKS-POSTWRITE-V1 | fresh-context:jun29-postwrite-v1 | books | review:SF-2026-ARXIV-2606-29142; books-review:SF-2026-ARXIV-2606-29150; books-review:SF-2026-ARXIV-2606-29151; books-review:SF-2026-ARXIV-2606-29158; books-review:SF-2026-ARXIV-2606-29159; books-review:SF-2026-ARXIV-2606-29171; books-review:SF-2026-ARXIV-2606-29176; books-review:SF-2026-ARXIV-2606-29178; books-review:SF-2026-ARXIV-2606-29182; books-review:SF-2026-ARXIV-2606-29184; books-review:SF-2026-ARXIV-2606-29193; review:SF-2026-ARXIV-2606-29194; books-review:SF-2026-ARXIV-2606-29196; books-review:SF-2026-ARXIV-2606-29207; books-review:SF-2026-ARXIV-2606-29215; books-review:SF-2026-ARXIV-2606-29222; books-review:SF-2026-ARXIV-2606-29223; books-review:SF-2026-ARXIV-2606-29225; books-review:SF-2026-ARXIV-2606-29228; books-review:SF-2026-ARXIV-2606-29237; books-review:SF-2026-ARXIV-2606-29238; books-review:SF-2026-ARXIV-2606-29239; books-review:SF-2026-ARXIV-2606-29251; books-review:SF-2026-ARXIV-2606-29270; books-review:SF-2026-ARXIV-2606-29275; books-review:SF-2026-ARXIV-2606-29278; books-review:SF-2026-ARXIV-2606-29279; books-review:SF-2026-ARXIV-2606-29280; books-review:SF-2026-ARXIV-2606-29282; books-review:SF-2026-ARXIV-2606-29296; books-review:SF-2026-ARXIV-2606-29315; books-review:SF-2026-ARXIV-2606-29328; books-review:SF-2026-ARXIV-2606-29337; books-review:SF-2026-ARXIV-2606-29340; books-review:SF-2026-ARXIV-2606-29350; books-review:SF-2026-ARXIV-2606-29354; books-review:SF-2026-ARXIV-2606-29366; books-review:SF-2026-ARXIV-2606-29377; review:SF-2026-ARXIV-2606-29399; books-review:SF-2026-ARXIV-2606-29403; books-review:SF-2026-ARXIV-2606-29424; books-review:SF-2026-ARXIV-2606-29425; books-review:SF-2026-ARXIV-2606-29441; books-review:SF-2026-ARXIV-2606-29445; books-review:SF-2026-ARXIV-2606-29472; books-review:SF-2026-ARXIV-2606-29476; books-review:SF-2026-ARXIV-2606-29481; books-review:SF-2026-ARXIV-2606-29490; books-review:SF-2026-ARXIV-2606-29493; books-review:SF-2026-ARXIV-2606-29501; books-review:SF-2026-ARXIV-2606-29502; books-review:SF-2026-ARXIV-2606-29506; books-review:SF-2026-ARXIV-2606-29520; books-review:SF-2026-ARXIV-2606-29522; books-review:SF-2026-ARXIV-2606-29526; books-review:SF-2026-ARXIV-2606-29532; books-review:SF-2026-ARXIV-2606-29537; books-review:SF-2026-ARXIV-2606-29538; books-review:SF-2026-ARXIV-2606-29541; books-review:SF-2026-ARXIV-2606-29544; books-review:SF-2026-ARXIV-2606-29554; books-review:SF-2026-ARXIV-2606-29563; books-review:SF-2026-ARXIV-2606-29565; books-review:SF-2026-ARXIV-2606-29567; books-review:SF-2026-ARXIV-2606-29571; books-review:SF-2026-ARXIV-2606-29573; review:SF-2026-ARXIV-2606-29580; books-review:SF-2026-ARXIV-2606-29581; review:SF-2026-ARXIV-2606-29592; books-review:SF-2026-ARXIV-2606-29601; books-review:SF-2026-ARXIV-2606-29602; books-review:SF-2026-ARXIV-2606-29604; books-review:SF-2026-ARXIV-2606-29605; books-review:SF-2026-ARXIV-2606-29623; books-review:SF-2026-ARXIV-2606-29629; books-review:SF-2026-ARXIV-2606-29645; books-review:SF-2026-ARXIV-2606-29646; books-review:SF-2026-ARXIV-2606-29648; books-review:SF-2026-ARXIV-2606-29649; books-review:SF-2026-ARXIV-2606-29652; books-review:SF-2026-ARXIV-2606-29654; books-review:SF-2026-ARXIV-2606-29657; books-review:SF-2026-ARXIV-2606-29661; review:SF-2026-ARXIV-2606-29679; books-review:SF-2026-ARXIV-2606-30686; books-review:SF-2026-ARXIV-2606-30689 | none | 13/13 Integrate body+Review markers unique in 9 owners; 73 non-Integrate families absent | passed |

## 8. Ignored Noise

候选分母外 identity 已在 full-population semantic screening ledger 中按 family-specific 理由关闭；Coverage Receipt 与 source packet 保留 raw、retained、closure 和 route-negative 账目，正文不重复展开低耐久度或越界项目。

### Materials and Access

- 86/86 exact-v1 primary full texts resolved; five PDF fallbacks; later versions used=0.

## 9. Recommended Action

- Fresh prewrite disposition: 13 Integrate / 67 No Change / 6 Weekly Only across 9 write owners.
- Under the exclusive write lock, 13 Integrate families were merged into 9 owner files; 67 No Change and 6 Weekly Only families remain absent.

## 10. Repository Changes

- Updated the date-local Daily/source packet/scripts and the nine approved Books owner files; LEARNING_STATE was not changed.

## 11. Open Questions

- Coverage audit complete: 0 FP in the 85 first-freeze retained; 1 FN in the 177 closures (2606.29328) reinstated; final denominator 86/176.
- None; 86/86 post-write fresh audit found zero unresolved finding.

## 12. Sources

- [Agent Security Meets Regulatory Reality -- A Practitioner Systematization of Autonomous-Agent Threats and Controls in Regulated Financial Systems](https://arxiv.org/abs/2606.29142v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [Flow Reasoning Models: Scaling Reasoning Through Iterative Self-Refinement](https://arxiv.org/abs/2606.29150v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [CADENZA: Compiling Natural-Language Intent into Task-Specific Operator DAGs for Semantic Query Processing](https://arxiv.org/abs/2606.29151v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [On the Nonlinearity of Learning Rate Scaling for LLM Training](https://arxiv.org/abs/2606.29158v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [Pooled Leaderboards Hide System-Specific Winners: A Reporting-Protocol Audit of Offline Root-Cause Analysis Benchmarks](https://arxiv.org/abs/2606.29159v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [Symbolic Mechanistic Data Attribution: Tracing Training Influence to Learned Behavioral Policies](https://arxiv.org/abs/2606.29171v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [Dead-Direction Conditioners: Gauge-Equivariant Preconditioning for Deep Networks](https://arxiv.org/abs/2606.29176v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [Selective Memory Retention for Long-Horizon LLM Agents](https://arxiv.org/abs/2606.29178v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [Evidence-Informed LLM Beliefs for Continual Scientific Discovery](https://arxiv.org/abs/2606.29182v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [BaRA: Bayesian Adaptive Rank Allocation for Parameter-Efficient Fine-Tuning](https://arxiv.org/abs/2606.29184v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [A Multi-Dataset Benchmark for Evaluating LLM Agents in Microservice Failure Diagnosis](https://arxiv.org/abs/2606.29193v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [AI Trading's Alpha Singularity: Emergent Market Reasoning through Agent-to-Agent Self-Evolution](https://arxiv.org/abs/2606.29194v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [Representational Depth of Evaluation Awareness Shifts With Scale in Open-Weight Language Models](https://arxiv.org/abs/2606.29196v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [KernelFlume: Elastic Core-Attention Scaling for Agentic Long-Context Decoding](https://arxiv.org/abs/2606.29207v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [Multi-Block Diffusion Language Models](https://arxiv.org/abs/2606.29215v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [CORE Planner: Contextual-memory Oriented Reinforcement-learning in Unknown Environments for Robot Navigation](https://arxiv.org/abs/2606.29222v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [Depth Exploration for LLM Decoding](https://arxiv.org/abs/2606.29223v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [PolicyGuard: A Dialogue-Grounded Sub-Agent Verifier for Policy Adherence in LLM Agents](https://arxiv.org/abs/2606.29225v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [Understanding Evaluation Illusion in Diffusion Large Language Models](https://arxiv.org/abs/2606.29228v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [MoPe: Motion Permanence for Robust Monocular Gaussian Mapping in Dynamic Environments](https://arxiv.org/abs/2606.29237v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [On the Policy Gradient Foundations of Group Relative Policy Optimization: Credit Assignment, Gradient Sparsity, and Rank Collapse](https://arxiv.org/abs/2606.29238v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [Breaking the Rounding Trap: Securing LLMs against Quantization-Conditioned Backdoors](https://arxiv.org/abs/2606.29239v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [When Summaries Distort Decisions: Information Fidelity in LLM-Compressed Financial Analysis](https://arxiv.org/abs/2606.29251v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [Minority Sentinel: When to Overturn Majority Voting in Multi-Agent LLM Debates](https://arxiv.org/abs/2606.29270v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [Adaptive Block Diffusion: Resolving Training-Inference Mismatch in Diffusion Language Models](https://arxiv.org/abs/2606.29275v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [The Complexity Ceiling Benchmark: A Multi-Domain Evaluation of Sequential Reasoning Under Depth Scaling](https://arxiv.org/abs/2606.29278v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [Manufactured Confidence: How Memory Consolidation Turns Hearsay into Confident Facts](https://arxiv.org/abs/2606.29279v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [Deterministic Decisions for High-Stakes AI. A Zero-Egress Pipeline with the Deployability of RAG and the Accuracy of Machine Learning](https://arxiv.org/abs/2606.29280v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [ScaleErasure: Inference-Time Minimal Intervention for Precise Concept Erasure in Next-Scale Autoregressive Image Generation](https://arxiv.org/abs/2606.29282v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [Process Advantage Signal Shaping: A Paradigm-Agnostic Middleware for Process-Supervised RL in LLM Reasoners](https://arxiv.org/abs/2606.29296v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [Hierarchical Experimentalist Agents](https://arxiv.org/abs/2606.29315v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [Covering the Unseen: Information Demand Coverage Optimization for Retrieval-Augmented Generation](https://arxiv.org/abs/2606.29328v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [W4A4 Quantization for Inference on Wan2.2-I2V-A14B](https://arxiv.org/abs/2606.29337v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [PHF: Privileged Hidden Flow for On-Policy Self-Distillation](https://arxiv.org/abs/2606.29340v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [Fast Enough to Act: Spatio-Temporal Visual Token Merging for Low-Latency Robotic VLMs and VLAs](https://arxiv.org/abs/2606.29350v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [When LLMs Develop Languages: Symbolic Communication for Efficient Multi-Agent Reasoning](https://arxiv.org/abs/2606.29354v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [Solver-Verified Formulation Generation and Selection for Multi-Warehouse Inventory Allocation Using Large Language Models](https://arxiv.org/abs/2606.29366v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [Diagnosing and Repairing Factual Errors in RAG under Budget Constraints](https://arxiv.org/abs/2606.29377v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [LLM-Guided Planning for Multi-hop Reasoning over Multimodal Nuclear Regulatory Documents](https://arxiv.org/abs/2606.29399v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [Self-Organized Conformal Prediction: Reducing Regional Coverage Gaps with Unsupervised Group Discovery](https://arxiv.org/abs/2606.29403v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [EntroRouter: Learning Efficient Model Routing via Entropy Regulation](https://arxiv.org/abs/2606.29424v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [Mixture of Debaters: Learn to Debate at Architectural Level in Multi-Agent Reasoning](https://arxiv.org/abs/2606.29425v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [Closing the Activation-Cone Blind Spot: Response-Time Probing and Unified Defense](https://arxiv.org/abs/2606.29441v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [Bridging VideoQA and Video-Guided Agentic Tasks via Generalized Keyframe Extraction](https://arxiv.org/abs/2606.29445v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [Agent-Computer Observation Interfaces Enable Dynamic Computer Use](https://arxiv.org/abs/2606.29472v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [CRAFT: Counterfactual Credit Assignment from Free Sibling Rollouts for Self-Distilled Agentic Reinforcement Learning](https://arxiv.org/abs/2606.29476v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [To Reason or to Fabricate: Reasoning Without Shortcuts via Hint-Anchored Pairwise Aggregation](https://arxiv.org/abs/2606.29481v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [Reported Confidence in LLMs Tracks Commitment More Than Correctness](https://arxiv.org/abs/2606.29490v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [Faults in Our Formal Benchmarking: Dataset Defects and Evaluation Failures in Lean Theorem Proving](https://arxiv.org/abs/2606.29493v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [Learning Transferable Dynamics Priors from Action to World Modeling](https://arxiv.org/abs/2606.29501v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [UCOB: Learning to Utilize and Evolve Agentic Skills via Credit-Aware On-Policy Bidirectional Self-Distillation](https://arxiv.org/abs/2606.29502v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [Benchmark AUC Is Not Deployable Reliability: A Cross-Dataset Audit of Off-the-Shelf Features for Surveillance Video Anomaly Detection](https://arxiv.org/abs/2606.29506v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [SAKE: Software Architectural Knowledge Evaluation Benchmark for Large Language Models](https://arxiv.org/abs/2606.29520v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [Do Models Read What They Write? Causal Registers in Scratchpad Reasoning](https://arxiv.org/abs/2606.29522v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [The Mirage of Optimizing Training Policies: Monotonic Inference Policies as the Real Objective for LLM Reinforcement Learning](https://arxiv.org/abs/2606.29526v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [SemJoin: Semantic Join Optimization](https://arxiv.org/abs/2606.29532v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [OSWorld 2.0: Benchmarking Computer Use Agents on Long-Horizon Real-World Tasks](https://arxiv.org/abs/2606.29537v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [RESOURCE2SKILL: Distilling Executable Agent Skills from Human-Created Multimodal Resources](https://arxiv.org/abs/2606.29538v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [Learned Coordination Conventions in Cooperative MARL: Measuring the Translation Gap Between Theory-Informed Roles and Learned Routing](https://arxiv.org/abs/2606.29541v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [Proteus: Automated Adversarial Robustness Testing for Audio Deepfake Detectors](https://arxiv.org/abs/2606.29544v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [Optimizer Memory Makes Shuffle Order a First-Order Source of Fine-Tuning Noise](https://arxiv.org/abs/2606.29554v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [Coverage-Driven KV Cache Eviction for Efficient and Improved Inference of LLM](https://arxiv.org/abs/2606.29563v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [Speculative Pre-Positioning: Decoding Stateful Sessions to the Next Decision Point Off the Critical Path](https://arxiv.org/abs/2606.29565v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [SurrogateShield: Beyond Redaction for High-Utility, Privacy-Preserving LLM Interactions](https://arxiv.org/abs/2606.29567v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [Anisotropy Decides Cosine vs. Rank Metrics for Text Embeddings](https://arxiv.org/abs/2606.29571v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [Reliability-Prioritized Fine-Grained Generation in Multimodal Large](https://arxiv.org/abs/2606.29573v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [MAM-AI: An On-Device Medical Retrieval-Augmented Generation System for Nurses and Midwives in Zanzibar](https://arxiv.org/abs/2606.29580v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [The Joint Effect of Quantization and Sampling Temperature on LLM Safety Alignment: A Factorial Analysis](https://arxiv.org/abs/2606.29581v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [STEMGym: Benchmarking Sequential Decision-Making under Dose Budgets in Autonomous Electron Microscopy](https://arxiv.org/abs/2606.29592v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [Langshaw: Declarative Interaction Protocols Based on Sayso and Conflict](https://arxiv.org/abs/2606.29601v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [An Empirical Evaluation of Prompt Injection Vulnerabilities in Large Language Models Across Multilingual and Obfuscated Attack Scenarios](https://arxiv.org/abs/2606.29602v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [Mechanistically Eliciting Latent Behaviors in Language Models](https://arxiv.org/abs/2606.29604v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [How much of an LLM-generated clinical corpus is actually new? A production-scale measurement of content redundancy for provenance classification](https://arxiv.org/abs/2606.29605v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [SCARCE: Scalable Cascade Analysis for Rare-event Characterisation via Embeddings](https://arxiv.org/abs/2606.29623v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [Energy-Efficient Multimodal Inference Serving with Tri-serve](https://arxiv.org/abs/2606.29629v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [Metadata, Structure, or Strategy? A Decomposition of RAG Context Enrichment](https://arxiv.org/abs/2606.29645v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [Fuzzing Large Language Models to Elicit Hidden Behaviours](https://arxiv.org/abs/2606.29646v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [Hybrid Retriever Evolution for Multimodal Document Reasoning Agents](https://arxiv.org/abs/2606.29648v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [Resolution Thresholds in VLM Detection of Harmful ASCII Art Across Construction Modes and Languages](https://arxiv.org/abs/2606.29649v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [As We May Search](https://arxiv.org/abs/2606.29652v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [Budgeted Act-or-Defer Multi-Agent LLM Deliberation with Local Reliability Bounds](https://arxiv.org/abs/2606.29654v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [Safety from Honesty in a Disinterested AI Predictor](https://arxiv.org/abs/2606.29657v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [Diversity is the Strength of the AI Crowd](https://arxiv.org/abs/2606.29661v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [Learning as Observable Matrix Dynamics: Diffusive Relaxations versus Phase Transitions](https://arxiv.org/abs/2606.29679v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [Position: Vision-Language-Action Models Cannot Be Verified to Perform Physical Reasoning](https://arxiv.org/abs/2606.30686v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [Citation Discipline in Spec-Driven Development: A Cross-Model Empirical Study of Output Determinism and Automated Hallucination Detection in LLM-Generated Code](https://arxiv.org/abs/2606.30689v1) — first-public（Asia/Shanghai）：2026-06-28；accessed：2026-08-29
- [Research Sources Registry](../../../../docs/RESEARCH_SOURCES.md) — source roles、cadence 与 evidence scope 的权威注册表

## 13. Final Status

Daily V2.1 的 Coverage=Closed、Evidence=Passed、Books=Passed；Completion Status=Complete。机器校验只证明接口一致，语义结论仍由第 7 节记录的 fresh-context audit 承担。

State Truth: Completion=Complete；Coverage=Closed；Evidence=Passed；Books=Passed；Unresolved Findings=0。
