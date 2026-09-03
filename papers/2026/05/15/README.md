# Daily Research — 2026-05-15

**Research Date:** 2026-05-15

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-05-14 09:00:00 ～ 2026-05-15 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Historical Daily Independent Full Replay

**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed；initial-created owner replay 与 exact-v1 Evidence Review 已完成。

## Executive Summary

本次独立重放枚举并逐项闭合 679 个注册 arXiv identity，冻结 59 个 Source Family；pre-denominator closure=620，withdrawn pre-denominator=0。14 个旧候选被迁回正确 owner day，2 个漏检 family 已恢复 exact-v1 全文并完成 Source Review。

DataCite `created` 仅作为 initial DOI registration 的 owner-day proxy；`updated`、v1 Updated 与 current OAI datestamp 只记录 revision provenance，不决定 first-public owner。机制结论只绑定 exact-v1 正文。 本日所有 Books disposition 已有终态。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-05-15 |
| Window End | 2026-05-15 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | DEN-20260515-CREATED-5dc329a4ba04e85c |
| Denominator Frozen At | 2026-09-03T12:36:05+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-05-14T09:00:00+08:00 | 2026-05-15T09:00:00+08:00 | 2026-09-03T12:36:05+08:00 | DataCite prefix 10.48550 initial created-day inventory + registered arXiv categories + exact-v1 identity/body | checked | 679 | SF-2026-ARXIV-2605-13848;SF-2026-ARXIV-2605-13851;SF-2026-ARXIV-2605-13880;SF-2026-ARXIV-2605-14241;SF-2026-ARXIV-2605-14249;SF-2026-ARXIV-2605-14271;SF-2026-ARXIV-2605-14290;SF-2026-ARXIV-2605-14305;SF-2026-ARXIV-2605-14415;SF-2026-ARXIV-2605-14421;SF-2026-ARXIV-2605-14460;SF-2026-ARXIV-2605-14473;SF-2026-ARXIV-2605-14483;SF-2026-ARXIV-2605-14498;SF-2026-ARXIV-2605-14514;SF-2026-ARXIV-2605-14570;SF-2026-ARXIV-2605-14591;SF-2026-ARXIV-2605-14636;SF-2026-ARXIV-2605-14678;SF-2026-ARXIV-2605-14744;SF-2026-ARXIV-2605-14747;SF-2026-ARXIV-2605-14786;SF-2026-ARXIV-2605-14859;SF-2026-ARXIV-2605-14865;SF-2026-ARXIV-2605-14906;SF-2026-ARXIV-2605-14932;SF-2026-ARXIV-2605-14968;SF-2026-ARXIV-2605-14978;SF-2026-ARXIV-2605-15030;SF-2026-ARXIV-2605-15034;SF-2026-ARXIV-2605-15051;SF-2026-ARXIV-2605-15079;SF-2026-ARXIV-2605-15100;SF-2026-ARXIV-2605-15109;SF-2026-ARXIV-2605-15118;SF-2026-ARXIV-2605-15128;SF-2026-ARXIV-2605-15132;SF-2026-ARXIV-2605-15138;SF-2026-ARXIV-2605-15152;SF-2026-ARXIV-2605-15155;SF-2026-ARXIV-2605-15164;SF-2026-ARXIV-2605-15172;SF-2026-ARXIV-2605-15178;SF-2026-ARXIV-2605-15184;SF-2026-ARXIV-2605-15185;SF-2026-ARXIV-2605-15188;SF-AGENTTRAP-MEASURING-RUNTIME-TRUST-FAILURES-IN-THIRD-PARTY-AGENT-SKILLS;SF-CHROMAFLOW-A-NEGATIVE-ABLATION-STUDY-OF-ORCHESTRATION-OVERHEAD-IN-TOOL-A;SF-DIAGNOSING-TRAINING-INFERENCE-MISMATCH-IN-LLM-REINFORCEMENT-LEARNING;SF-EVOLVEMEM-SELF-EVOLVING-MEMORY-ARCHITECTURE-VIA-AUTORESEARCH-FOR-LLM-AGE;SF-GROUNDED-CONTINUATION-A-LINEAR-TIME-RUNTIME-VERIFIER-FOR-LLM-CONVERSATIO;SF-HOW-TO-SCALE-MIXTURE-OF-EXPERTS-FROM-MUP-TO-THE-MAXIMALLY-SCALE-STABLE-P;SF-LLMS-KNOW-WHEN-THEY-KNOW-BUT-DO-NOT-ACT-ON-IT-A-METACOGNITIVE-HARNESS-FO;SF-MISTLETOE-STEALTHY-ACCELERATION-COLLAPSE-ATTACKS-ON-SPECULATIVE-DECODING;SF-MODEL-ADAPTIVE-TOOL-NECESSITY-REVEALS-THE-KNOWING-DOING-GAP-IN-LLM-TOOL-;SF-MULTI-SCALE-DEQUANT-ELIMINATING-DEQUANTIZATION-BOTTLENECK-VIA-ACTIVATION;SF-PREFT-PREFILL-ONLY-FINETUNING-FOR-EFFICIENT-INFERENCE;SF-SELF-PRUNED-KEY-VALUE-ATTENTION-LEARNING-WHEN-TO-WRITE-BY-PREDICTING-FUT;SF-SKILLFLOW-FLOW-DRIVEN-RECURSIVE-SKILL-EVOLUTION-FOR-AGENTIC-ORCHESTRATIO | created-day pages=closed; OAI category sets=closed; direct same-day OAI=510 | 2026-05-15T09:00:00+08:00 | coverage:SRC-ARXIV:20260515 | — |

<!-- coverage:SRC-ARXIV:20260515:start -->全量 raw inventory=679；每个 identity 均具有 retained、family-specific closure 或 withdrawn terminal closure。候选 owner 由 initial DataCite created、arXiv ID month、v1 history 与 announcement cadence 共同约束；冲突不由 updated 字段覆盖。<!-- coverage:SRC-ARXIV:20260515:end -->

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
| SF-2026-ARXIV-2605-13848 | arXiv:2605.13848v1 | paper-v1:2605.13848 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2605-13848 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-13848 | yes |
| SF-2026-ARXIV-2605-13851 | arXiv:2605.13851v1 | paper-v1:2605.13851 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-13851 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-13851 | yes |
| SF-2026-ARXIV-2605-13880 | arXiv:2605.13880v1 | paper-v1:2605.13880 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-13880 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-13880 | no |
| SF-2026-ARXIV-2605-14241 | arXiv:2605.14241v1 | paper-v1:2605.14241 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-14241 | self | — | new_in_window | AGENT-TOOL-CALLING | Integrate | books-review:SF-2026-ARXIV-2605-14241 | no |
| SF-2026-ARXIV-2605-14249 | arXiv:2605.14249v1 | paper-v1:2605.14249 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-14249 | self | — | new_in_window | PLATFORM-COST | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14249 | no |
| SF-2026-ARXIV-2605-14271 | arXiv:2605.14271v1 | paper-v1:2605.14271 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-14271 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14271 | no |
| SF-2026-ARXIV-2605-14290 | arXiv:2605.14290v1 | paper-v1:2605.14290 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-14290 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14290 | no |
| SF-2026-ARXIV-2605-14305 | arXiv:2605.14305v1 | paper-v1:2605.14305 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-14305 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14305 | no |
| SF-2026-ARXIV-2605-14415 | arXiv:2605.14415v1 | paper-v1:2605.14415 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-14415 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14415 | no |
| SF-2026-ARXIV-2605-14421 | arXiv:2605.14421v1 | paper-v1:2605.14421 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-14421 | self | — | new_in_window | AGENT-MEMORY | Integrate | books-review:SF-2026-ARXIV-2605-14421 | no |
| SF-2026-ARXIV-2605-14460 | arXiv:2605.14460v1 | paper-v1:2605.14460 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-14460 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14460 | no |
| SF-2026-ARXIV-2605-14473 | arXiv:2605.14473v1 | paper-v1:2605.14473 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-14473 | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14473 | no |
| SF-2026-ARXIV-2605-14483 | arXiv:2605.14483v1 | paper-v1:2605.14483 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-14483 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14483 | no |
| SF-2026-ARXIV-2605-14498 | arXiv:2605.14498v1 | paper-v1:2605.14498 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-14498 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14498 | no |
| SF-2026-ARXIV-2605-14514 | arXiv:2605.14514v1 | paper-v1:2605.14514 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-14514 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14514 | no |
| SF-2026-ARXIV-2605-14570 | arXiv:2605.14570v1 | paper-v1:2605.14570 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-14570 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14570 | no |
| SF-2026-ARXIV-2605-14591 | arXiv:2605.14591v1 | paper-v1:2605.14591 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-14591 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14591 | no |
| SF-2026-ARXIV-2605-14636 | arXiv:2605.14636v1 | paper-v1:2605.14636 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-14636 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14636 | no |
| SF-2026-ARXIV-2605-14678 | arXiv:2605.14678v1 | paper-v1:2605.14678 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-14678 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14678 | no |
| SF-2026-ARXIV-2605-14744 | arXiv:2605.14744v1 | paper-v1:2605.14744 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-14744 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14744 | no |
| SF-2026-ARXIV-2605-14747 | arXiv:2605.14747v1 | paper-v1:2605.14747 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-14747 | self | — | new_in_window | TRAIN-DATA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14747 | no |
| SF-2026-ARXIV-2605-14786 | arXiv:2605.14786v1 | paper-v1:2605.14786 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-14786 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14786 | no |
| SF-2026-ARXIV-2605-14859 | arXiv:2605.14859v1 | paper-v1:2605.14859 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-14859 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14859 | no |
| SF-2026-ARXIV-2605-14865 | arXiv:2605.14865v1 | paper-v1:2605.14865 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-14865 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14865 | no |
| SF-2026-ARXIV-2605-14906 | arXiv:2605.14906v1 | paper-v1:2605.14906 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-14906 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14906 | no |
| SF-2026-ARXIV-2605-14932 | arXiv:2605.14932v1 | paper-v1:2605.14932 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-14932 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14932 | no |
| SF-2026-ARXIV-2605-14968 | arXiv:2605.14968v1 | paper-v1:2605.14968 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-14968 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14968 | no |
| SF-2026-ARXIV-2605-14978 | arXiv:2605.14978v1 | paper-v1:2605.14978 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-14978 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14978 | no |
| SF-2026-ARXIV-2605-15030 | arXiv:2605.15030v1 | paper-v1:2605.15030 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-15030 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15030 | no |
| SF-2026-ARXIV-2605-15034 | arXiv:2605.15034v1 | paper-v1:2605.15034 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-15034 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15034 | no |
| SF-2026-ARXIV-2605-15051 | arXiv:2605.15051v1 | paper-v1:2605.15051 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-15051 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | Integrate | books-review:SF-2026-ARXIV-2605-15051 | no |
| SF-2026-ARXIV-2605-15079 | arXiv:2605.15079v1 | paper-v1:2605.15079 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-15079 | self | — | new_in_window | TRAIN-DATA | Integrate | books-review:SF-2026-ARXIV-2605-15079 | no |
| SF-2026-ARXIV-2605-15100 | arXiv:2605.15100v1 | paper-v1:2605.15100 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-15100 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15100 | no |
| SF-2026-ARXIV-2605-15109 | arXiv:2605.15109v1 | paper-v1:2605.15109 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-15109 | self | — | new_in_window | AGENT-RAG | Integrate | books-review:SF-2026-ARXIV-2605-15109 | no |
| SF-2026-ARXIV-2605-15118 | arXiv:2605.15118v1 | paper-v1:2605.15118 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-15118 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15118 | no |
| SF-2026-ARXIV-2605-15128 | arXiv:2605.15128v1 | paper-v1:2605.15128 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-15128 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15128 | no |
| SF-2026-ARXIV-2605-15132 | arXiv:2605.15132v1 | paper-v1:2605.15132 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-15132 | self | — | new_in_window | AGENT-WORKFLOW | Integrate | books-review:SF-2026-ARXIV-2605-15132 | no |
| SF-2026-ARXIV-2605-15138 | arXiv:2605.15138v1 | paper-v1:2605.15138 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-15138 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15138 | no |
| SF-2026-ARXIV-2605-15152 | arXiv:2605.15152v1 | paper-v1:2605.15152 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-15152 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15152 | no |
| SF-2026-ARXIV-2605-15155 | arXiv:2605.15155v1 | paper-v1:2605.15155 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-15155 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15155 | no |
| SF-2026-ARXIV-2605-15164 | arXiv:2605.15164v1 | paper-v1:2605.15164 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-15164 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15164 | no |
| SF-2026-ARXIV-2605-15172 | arXiv:2605.15172v1 | paper-v1:2605.15172 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-15172 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15172 | no |
| SF-2026-ARXIV-2605-15178 | arXiv:2605.15178v1 | paper-v1:2605.15178 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-15178 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15178 | no |
| SF-2026-ARXIV-2605-15184 | arXiv:2605.15184v1 | paper-v1:2605.15184 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-15184 | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15184 | no |
| SF-2026-ARXIV-2605-15185 | arXiv:2605.15185v1 | paper-v1:2605.15185 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-15185 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Integrate | books-review:SF-2026-ARXIV-2605-15185 | no |
| SF-2026-ARXIV-2605-15188 | arXiv:2605.15188v1 | paper-v1:2605.15188 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-15188 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15188 | no |
| SF-AGENTTRAP-MEASURING-RUNTIME-TRUST-FAILURES-IN-THIRD-PARTY-AGENT-SKILLS | arXiv:2605.13940v1 | paper-v1:2605.13940 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-AGENTTRAP-MEASURING-RUNTIME-TRUST-FAILURES-IN-THIRD-PARTY-AGENT-SKILLS | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-AGENTTRAP-MEASURING-RUNTIME-TRUST-FAILURES-IN-THIRD-PARTY-AGENT-SKILLS | no |
| SF-CHROMAFLOW-A-NEGATIVE-ABLATION-STUDY-OF-ORCHESTRATION-OVERHEAD-IN-TOOL-A | arXiv:2605.14102v1 | paper-v1:2605.14102 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-CHROMAFLOW-A-NEGATIVE-ABLATION-STUDY-OF-ORCHESTRATION-OVERHEAD-IN-TOOL-A | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-CHROMAFLOW-A-NEGATIVE-ABLATION-STUDY-OF-ORCHESTRATION-OVERHEAD-IN-TOOL-A | no |
| SF-DIAGNOSING-TRAINING-INFERENCE-MISMATCH-IN-LLM-REINFORCEMENT-LEARNING | arXiv:2605.14220v1 | paper-v1:2605.14220 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-DIAGNOSING-TRAINING-INFERENCE-MISMATCH-IN-LLM-REINFORCEMENT-LEARNING | self | — | new_in_window | TRAIN-RLHF | Integrate | books-review:SF-DIAGNOSING-TRAINING-INFERENCE-MISMATCH-IN-LLM-REINFORCEMENT-LEARNING | no |
| SF-EVOLVEMEM-SELF-EVOLVING-MEMORY-ARCHITECTURE-VIA-AUTORESEARCH-FOR-LLM-AGE | arXiv:2605.13941v1 | paper-v1:2605.13941 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-EVOLVEMEM-SELF-EVOLVING-MEMORY-ARCHITECTURE-VIA-AUTORESEARCH-FOR-LLM-AGE | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-EVOLVEMEM-SELF-EVOLVING-MEMORY-ARCHITECTURE-VIA-AUTORESEARCH-FOR-LLM-AGE | no |
| SF-GROUNDED-CONTINUATION-A-LINEAR-TIME-RUNTIME-VERIFIER-FOR-LLM-CONVERSATIO | arXiv:2605.14175v1 | paper-v1:2605.14175 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-GROUNDED-CONTINUATION-A-LINEAR-TIME-RUNTIME-VERIFIER-FOR-LLM-CONVERSATIO | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-GROUNDED-CONTINUATION-A-LINEAR-TIME-RUNTIME-VERIFIER-FOR-LLM-CONVERSATIO | no |
| SF-HOW-TO-SCALE-MIXTURE-OF-EXPERTS-FROM-MUP-TO-THE-MAXIMALLY-SCALE-STABLE-P | arXiv:2605.14200v1 | paper-v1:2605.14200 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-HOW-TO-SCALE-MIXTURE-OF-EXPERTS-FROM-MUP-TO-THE-MAXIMALLY-SCALE-STABLE-P | self | — | new_in_window | MODEL-MOE | No Change — Existing Coverage | books-review:SF-HOW-TO-SCALE-MIXTURE-OF-EXPERTS-FROM-MUP-TO-THE-MAXIMALLY-SCALE-STABLE-P | no |
| SF-LLMS-KNOW-WHEN-THEY-KNOW-BUT-DO-NOT-ACT-ON-IT-A-METACOGNITIVE-HARNESS-FO | arXiv:2605.14186v1 | paper-v1:2605.14186 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-LLMS-KNOW-WHEN-THEY-KNOW-BUT-DO-NOT-ACT-ON-IT-A-METACOGNITIVE-HARNESS-FO | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-LLMS-KNOW-WHEN-THEY-KNOW-BUT-DO-NOT-ACT-ON-IT-A-METACOGNITIVE-HARNESS-FO | no |
| SF-MISTLETOE-STEALTHY-ACCELERATION-COLLAPSE-ATTACKS-ON-SPECULATIVE-DECODING | arXiv:2605.14005v1 | paper-v1:2605.14005 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-MISTLETOE-STEALTHY-ACCELERATION-COLLAPSE-ATTACKS-ON-SPECULATIVE-DECODING | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-MISTLETOE-STEALTHY-ACCELERATION-COLLAPSE-ATTACKS-ON-SPECULATIVE-DECODING | no |
| SF-MODEL-ADAPTIVE-TOOL-NECESSITY-REVEALS-THE-KNOWING-DOING-GAP-IN-LLM-TOOL- | arXiv:2605.14038v1 | paper-v1:2605.14038 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-MODEL-ADAPTIVE-TOOL-NECESSITY-REVEALS-THE-KNOWING-DOING-GAP-IN-LLM-TOOL- | self | — | new_in_window | AGENT-TOOL-CALLING | Integrate | books-review:SF-MODEL-ADAPTIVE-TOOL-NECESSITY-REVEALS-THE-KNOWING-DOING-GAP-IN-LLM-TOOL- | no |
| SF-MULTI-SCALE-DEQUANT-ELIMINATING-DEQUANTIZATION-BOTTLENECK-VIA-ACTIVATION | arXiv:2605.13915v1 | paper-v1:2605.13915 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-MULTI-SCALE-DEQUANT-ELIMINATING-DEQUANTIZATION-BOTTLENECK-VIA-ACTIVATION | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-MULTI-SCALE-DEQUANT-ELIMINATING-DEQUANTIZATION-BOTTLENECK-VIA-ACTIVATION | no |
| SF-PREFT-PREFILL-ONLY-FINETUNING-FOR-EFFICIENT-INFERENCE | arXiv:2605.14217v1 | paper-v1:2605.14217 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-PREFT-PREFILL-ONLY-FINETUNING-FOR-EFFICIENT-INFERENCE | self | — | new_in_window | INFER-PREFILL | No Change — Existing Coverage | books-review:SF-PREFT-PREFILL-ONLY-FINETUNING-FOR-EFFICIENT-INFERENCE | no |
| SF-SELF-PRUNED-KEY-VALUE-ATTENTION-LEARNING-WHEN-TO-WRITE-BY-PREDICTING-FUT | arXiv:2605.14037v1 | paper-v1:2605.14037 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-SELF-PRUNED-KEY-VALUE-ATTENTION-LEARNING-WHEN-TO-WRITE-BY-PREDICTING-FUT | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-SELF-PRUNED-KEY-VALUE-ATTENTION-LEARNING-WHEN-TO-WRITE-BY-PREDICTING-FUT | no |
| SF-SKILLFLOW-FLOW-DRIVEN-RECURSIVE-SKILL-EVOLUTION-FOR-AGENTIC-ORCHESTRATIO | arXiv:2605.14089v1 | paper-v1:2605.14089 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-SKILLFLOW-FLOW-DRIVEN-RECURSIVE-SKILL-EVOLUTION-FOR-AGENTIC-ORCHESTRATIO | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-SKILLFLOW-FLOW-DRIVEN-RECURSIVE-SKILL-EVOLUTION-FOR-AGENTIC-ORCHESTRATIO | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-13848 | RP-6214d7e104f78e1a | standard | arXiv:2605.13848v1 | SRC-ARXIV@arXiv:2605.13848v1 | https://arxiv.org/html/2605.13848v1#S2 | https://arxiv.org/html/2605.13848v1#S4 | https://arxiv.org/html/2605.13848v1#S6 | Not Disclosed — exact-v1 review found no versioned public artifact contract | claim:SF-2026-ARXIV-2605-13848 | complete |
| SF-2026-ARXIV-2605-13851 | RP-de29d704510f75db | deep | arXiv:2605.13851v1 | SRC-ARXIV@arXiv:2605.13851v1 | https://arxiv.org/html/2605.13851v1#S2 | https://arxiv.org/html/2605.13851v1#S4 | https://arxiv.org/html/2605.13851v1#S6 | Not Disclosed — exact-v1 review found no versioned public artifact contract | claim:SF-2026-ARXIV-2605-13851 | complete |
| SF-2026-ARXIV-2605-13880 | RP-7c0ea3bfaad89f03 | deep | arXiv:2605.13880v1 | SRC-ARXIV@arXiv:2605.13880v1 | arXiv:2605.13880v1 §3 pre-task memory construction, proposer control and validator-gated writes — pre-task proposer-validator practice writes validated experience into memory | arXiv:2605.13880v1 §4 Experiments and ablations | Not Disclosed — exact-v1 body was reviewed, but no stable numbered Limitations/Counterevidence fragment was exposed; reviewer boundary: arXiv:2605.13880v1 Limitations discussion; synthetic-practice generator, validators, tasks and memory budget bound transfer | Not Disclosed — no immutable public artifact was identified in the reviewed exact-v1 body | claim:SF-2026-ARXIV-2605-13880 | complete |
| SF-2026-ARXIV-2605-14241 | RP-f7b4d8498d4dac8c | deep | arXiv:2605.14241v1 | SRC-ARXIV@arXiv:2605.14241v1 | https://arxiv.org/html/2605.14241v1 §3 LQM-ContextRoute — mechanism boundary: Tool-augmented LLM agents increasingly access the same tool type through multiple functionally equivalent providers, such as web-search APIs, retrievers, or LLM backends exposed behind a shared interface. | https://arxiv.org/html/2605.14241v1 §4 Evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.14241v1 §7 Limitations — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.14241v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-14241 | complete |
| SF-2026-ARXIV-2605-14249 | RP-9564507a365375ca | deep | arXiv:2605.14249v1 | SRC-ARXIV@arXiv:2605.14249v1 | https://arxiv.org/html/2605.14249v1 §3 EnergyLens Methodology — mechanism boundary: We present EnergyLens, an end-to-end framework for energy-aware large language model (LLM) inference optimization. | https://arxiv.org/html/2605.14249v1 §4 Evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.14249v1 §5 Discussion and limitations disclosed by evaluated hardware/configuration space — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.14249v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-14249 | complete |
| SF-2026-ARXIV-2605-14271 | RP-73abaecdcf7c4fda | deep | arXiv:2605.14271v1 | SRC-ARXIV@arXiv:2605.14271v1 | https://arxiv.org/html/2605.14271v1 §4.1 Task Design; HarnessAudit-Bench — mechanism boundary: LLM agents increasingly run inside execution harnesses that dispatch tools, allocate resources, and route messages between specialized components. | https://arxiv.org/html/2605.14271v1 §5 Experiments — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.14271v1 §6 Discussion and disclosed harness/model boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.14271v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-14271 | complete |
| SF-2026-ARXIV-2605-14290 | RP-150c3930a688ebff | deep | arXiv:2605.14290v1 | SRC-ARXIV@arXiv:2605.14290v1 | https://arxiv.org/html/2605.14290v1 §2.1 Threat Model; §4 Plan-Then-Execute Web Agents; §5 Expressivity — mechanism boundary: ReAct has become the default architecture across LLM agents, and many existing web agents follow this paradigm. | https://arxiv.org/html/2605.14290v1 §6.1 Task Taxonomy; §6.2 WebArena empirical analysis — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.14290v1 §6.3 Practical Gaps; §7 Discussion — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.14290v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-14290 | complete |
| SF-2026-ARXIV-2605-14305 | RP-ab813ae15840a4ea | deep | arXiv:2605.14305v1 | SRC-ARXIV@arXiv:2605.14305v1 | https://arxiv.org/html/2605.14305v1 §3 Factorization-Error-Free DLLM — mechanism boundary: Discrete diffusion language models improve generation efficiency through parallel token prediction, but standard $X_0$ prediction methods introduce factorization errors by approximating the clean token posterior with independent token-wise distributions. | https://arxiv.org/html/2605.14305v1 §4 Experiments — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.14305v1 §4 Ablation and device/workload boundary; no dedicated limitations section — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.14305v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-14305 | complete |
| SF-2026-ARXIV-2605-14415 | RP-cc35d74a484767b2 | deep | arXiv:2605.14415v1 | SRC-ARXIV@arXiv:2605.14415v1 | https://arxiv.org/html/2605.14415v1 §2 SWE-Chain construction; §3.1–§3.2 agent execution — mechanism boundary: Coding agents powered by large language models are increasingly expected to perform realistic software maintenance tasks beyond isolated issue resolution. | https://arxiv.org/html/2605.14415v1 §3.3 Evaluation; §4 Results — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.14415v1 Appendix K Limitations — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.14415v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-14415 | complete |
| SF-2026-ARXIV-2605-14421 | RP-d451e20a6dbf9130 | deep | arXiv:2605.14421v1 | SRC-ARXIV@arXiv:2605.14421v1 | https://arxiv.org/html/2605.14421v1 §2 Threat Model; §3 MemLineage Design — mechanism boundary: We introduce MemLineage, a defense for LLM agent memory that attaches both cryptographic provenance and LLM-mediated derivation lineage to every entry. | https://arxiv.org/html/2605.14421v1 §6 Evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.14421v1 §8 Discussion and Limitations — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.14421v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-14421 | complete |
| SF-2026-ARXIV-2605-14460 | RP-e64825f6318e2777 | deep | arXiv:2605.14460v1 | SRC-ARXIV@arXiv:2605.14460v1 | https://arxiv.org/html/2605.14460v1 §3 Payload-less Skill Attack and Audit Method — mechanism boundary: Autonomous agents powered by Large Language Models (LLMs) acquire external functionalities through third-party skills available in open marketplaces. | https://arxiv.org/html/2605.14460v1 §5 Evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.14460v1 §6.3 Threats to Validity and Limitations — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.14460v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-14460 | complete |
| SF-2026-ARXIV-2605-14473 | RP-c96c6ae36796edd3 | deep | arXiv:2605.14473v1 | SRC-ARXIV@arXiv:2605.14473v1 | https://arxiv.org/html/2605.14473v1 §3 Context-Driven Decomposition — mechanism boundary: Retrieval-Augmented Generation (RAG) is usually evaluated by whether the final answer is correct. | https://arxiv.org/html/2605.14473v1 §4 Evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.14473v1 §6 Limitations and conflict-dataset/model boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.14473v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-14473 | complete |
| SF-2026-ARXIV-2605-14483 | RP-99afed6f5269ff01 | deep | arXiv:2605.14483v1 | SRC-ARXIV@arXiv:2605.14483v1 | https://arxiv.org/html/2605.14483v1 §3 LEMON Counterfactual Orchestration — mechanism boundary: Large language models (LLMs) have become a strong foundation for multi-agent systems, but their effectiveness depends heavily on orchestration design. | https://arxiv.org/html/2605.14483v1 §4–§5 Evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.14483v1 Appendix B Limitations — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.14483v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-14483 | complete |
| SF-2026-ARXIV-2605-14498 | RP-599dd39af7321629 | deep | arXiv:2605.14498v1 | SRC-ARXIV@arXiv:2605.14498v1 | https://arxiv.org/html/2605.14498v1 §3 GroupMemBench construction; §3.2 question taxonomy — mechanism boundary: Large Language Model (LLM) agents increasingly serve as personal assistants and workplace collaborators, where their utility depends on memory systems that extract, retrieve, and apply information across long-running conversations. | https://arxiv.org/html/2605.14498v1 §4 Evaluation; Appendix I judge reliability — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.14498v1 Appendix K Limitations — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.14498v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-14498 | complete |
| SF-2026-ARXIV-2605-14514 | RP-f6088adfb67e7481 | deep | arXiv:2605.14514v1 | SRC-ARXIV@arXiv:2605.14514v1 | https://arxiv.org/html/2605.14514v1 §3 ConflictEval pairwise sequential-defense framework — mechanism boundary: Large Language Models (LLMs) deployed in high-stakes applications must simultaneously manage multiple risks, yet existing defenses are almost exclusively evaluated in isolation under a one-shot deployment assumption. | https://arxiv.org/html/2605.14514v1 §4 Results; §5 mechanistic analysis; Appendix B configurations — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.14514v1 §5 Limitations paragraph — pairwise/six-defense/three-family boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.14514v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-14514 | complete |
| SF-2026-ARXIV-2605-14570 | RP-e24d1bf7a78702fa | deep | arXiv:2605.14570v1 | SRC-ARXIV@arXiv:2605.14570v1 | https://arxiv.org/html/2605.14570v1 §3 Denoising-trajectory uncertainty signals — mechanism boundary: Large Language Diffusion Models (LLDMs) are emerging as an alternative to autoregressive models, offering faster inference through higher parallelism. | https://arxiv.org/html/2605.14570v1 §4 Experiments and calibration — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.14570v1 Appendix E Limitations; perfect-calibration/semantic-measure assumptions and sampled-model/task boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.14570v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-14570 | complete |
| SF-2026-ARXIV-2605-14591 | RP-38b1f2b51f7a3cb5 | deep | arXiv:2605.14591v1 | SRC-ARXIV@arXiv:2605.14591v1 | https://arxiv.org/html/2605.14591v1 §3 Zero-Run Privacy Audit — mechanism boundary: Privacy auditing provides empirical lower bounds on the differential privacy parameters of learning algorithms. | https://arxiv.org/html/2605.14591v1 §4–§6 Experiments — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.14591v1 §9 Limitations and Conclusion — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.14591v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-14591 | complete |
| SF-2026-ARXIV-2605-14636 | RP-8914e7f511b56c1a | deep | arXiv:2605.14636v1 | SRC-ARXIV@arXiv:2605.14636v1 | https://arxiv.org/html/2605.14636v1 §3 Temporal Critique Fine-tuning — mechanism boundary: Large language models (LLMs) often fail to reason under temporal cutoffs: when prompted to answer from the standpoint of an earlier time, they exploit knowledge that became available only later. | https://arxiv.org/html/2605.14636v1 §4–§6 Experiments — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.14636v1 §7 Limitations — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.14636v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-14636 | complete |
| SF-2026-ARXIV-2605-14678 | RP-14a81ce93ca25c5c | deep | arXiv:2605.14678v1 | SRC-ARXIV@arXiv:2605.14678v1 | https://arxiv.org/html/2605.14678v1 §3 π-Bench task/persona/hidden-intent construction — mechanism boundary: The rise of personal assistant agents, e.g., OpenClaw, highlights the growing potential of large language models to support users across everyday life and work. | https://arxiv.org/html/2605.14678v1 §4 Evaluation and long-horizon trajectories — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.14678v1 §6 Limitations — simulated users and single Nanobot-derived scaffold boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.14678v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-14678 | complete |
| SF-2026-ARXIV-2605-14744 | RP-b282da0d0dcddd2a | deep | arXiv:2605.14744v1 | SRC-ARXIV@arXiv:2605.14744v1 | https://arxiv.org/html/2605.14744v1 §3 Methodology; §3.2 Mechanical Policy; §3.3 Governance Metrics — mechanism boundary: Large language models in regulated financial workflows are governed by natural-language policies that the same model interprets, creating a principal--agent failure: outputs can appear compliant without being compliant. | https://arxiv.org/html/2605.14744v1 §4 Experiments and Results — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.14744v1 §5 Discussion/Conclusion; no dedicated limitations section — synthetic banking, single-model-family and ground-truth-rule boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.14744v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-14744 | complete |
| SF-2026-ARXIV-2605-14747 | RP-60175f443e4cc738 | deep | arXiv:2605.14747v1 | SRC-ARXIV@arXiv:2605.14747v1 | https://arxiv.org/html/2605.14747v1 §3 Video2GUI coarse-to-fine pipeline; §4 WildGUI construction — mechanism boundary: Recent advances in multimodal large language models have driven growing interest in graphical user interface (GUI) agents, yet their generalization remains constrained by the scarcity of large-scale training data spanning diverse real-world applications. | https://arxiv.org/html/2605.14747v1 §5 Pretraining and GUI benchmark evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.14747v1 Conclusion and appendix data-quality analyses; no dedicated limitations section — automatic grounding/filter and executable-validation coverage boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.14747v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-14747 | complete |
| SF-2026-ARXIV-2605-14786 | RP-42683edae586ba52 | deep | arXiv:2605.14786v1 | SRC-ARXIV@arXiv:2605.14786v1 | https://arxiv.org/html/2605.14786v1 §3 Threat model and passive UI-trace fingerprinting — mechanism boundary: As LLM-based agents increasingly browse the web on users' behalf, a natural question arises: can websites passively identify which underlying model powers an agent? | https://arxiv.org/html/2605.14786v1 §4–§5 Cross-model/environment evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.14786v1 §6 Limitations and adaptive-attacker/retraining boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.14786v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-14786 | complete |
| SF-2026-ARXIV-2605-14859 | RP-f72e5cf7a8da4c65 | deep | arXiv:2605.14859v1 | SRC-ARXIV@arXiv:2605.14859v1 | https://arxiv.org/html/2605.14859v1 §3 AuthBench and Permission-Boundary Inference — mechanism boundary: As coding agents gain access to shells, repositories, and user files, least-privilege authorization becomes a prerequisite for safe deployment: an agent should receive enough authority to complete the task, without unnecessary authority that exposes sensitive surfaces. | https://arxiv.org/html/2605.14859v1 §4–§5 Evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.14859v1 Appendix B Limitations and Future Work — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.14859v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-14859 | complete |
| SF-2026-ARXIV-2605-14865 | RP-d8343f5442efcf09 | deep | arXiv:2605.14865v1 | SRC-ARXIV@arXiv:2605.14865v1 | https://arxiv.org/html/2605.14865v1 §3 Top-down and span-level diagnostic framework — mechanism boundary: AI agents execute complex multi-step processes, but current evaluation falls short: outcome metrics report success or failure without explaining why, and process-level approaches struggle to connect failure types to their precise locations within long, structured traces. | https://arxiv.org/html/2605.14865v1 §4 TRAIL/GAIA/SWE-Bench evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.14865v1 §5 Limitations and evaluator/model/task boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.14865v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-14865 | complete |
| SF-2026-ARXIV-2605-14906 | RP-ea81fd92e73923d8 | deep | arXiv:2605.14906v1 | SRC-ARXIV@arXiv:2605.14906v1 | https://arxiv.org/html/2605.14906v1 §3 MemLens construction and visual-evidence requirements — mechanism boundary: Memory is essential for large vision-language models (LVLMs) to handle long, multimodal interactions, with two method directions providing this capability: long-context LVLMs and memory-augmented agents. | https://arxiv.org/html/2605.14906v1 §4 Evaluation across memory systems — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.14906v1 §6 Limitations — synthetic conversation, judge and modality/task boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.14906v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-14906 | complete |
| SF-2026-ARXIV-2605-14932 | RP-9a0d74baf6c1575b | deep | arXiv:2605.14932v1 | SRC-ARXIV@arXiv:2605.14932v1 | https://arxiv.org/html/2605.14932v1 §3 Agent-as-OS Security Model — mechanism boundary: Autonomous agents based on large language models (LLMs) are rapidly emerging as a general-purpose technology, with recent systems such as OpenClaw extending their capabilities through broad tool use, third-party skills, and deeper integration into user environments. | https://arxiv.org/html/2605.14932v1 §4–§5 Case Studies — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.14932v1 §VI Limitations — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.14932v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-14932 | complete |
| SF-2026-ARXIV-2605-14968 | RP-7c5df7351439ec8d | deep | arXiv:2605.14968v1 | SRC-ARXIV@arXiv:2605.14968v1 | https://arxiv.org/html/2605.14968v1 official PDF pp. 2–11 §1.3–§1.8 diagram-as-specification, contracts, runtime and formal semantics — mechanism boundary: GraphFlow is a visual workflow system designed to improve the reliability of agentic AI automation in multi-step, mission-critical processes. | https://arxiv.org/html/2605.14968v1 official PDF pp. 12–15 §1.12 Evaluation Plan; §1.13 Empirical Evaluation; §2 Implementation Status — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.14968v1 official PDF pp. 11–15 §1.10 Failure Modes and Limitations; §1.13.6 Interpretation and Limitations — verified core not deployed/evaluated — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.14968v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-14968 | complete |
| SF-2026-ARXIV-2605-14978 | RP-5ae3f63f67c4a1e2 | deep | arXiv:2605.14978v1 | SRC-ARXIV@arXiv:2605.14978v1 | https://arxiv.org/html/2605.14978v1 §3 Adaptive-window policy optimization — mechanism boundary: Speculative decoding accelerates LLM inference by having a lightweight draft model propose speculative windows of candidate tokens for parallel verification by a larger target model. | https://arxiv.org/html/2605.14978v1 §4 Serving evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.14978v1 §5 Limitations and workload/hardware/generalization boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.14978v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-14978 | complete |
| SF-2026-ARXIV-2605-15030 | RP-48328170dd5535c8 | deep | arXiv:2605.15030v1 | SRC-ARXIV@arXiv:2605.15030v1 | https://arxiv.org/html/2605.15030v1 §3 Problem; §4 Data; §5 WARD Training — mechanism boundary: Web agents can autonomously complete online tasks by interacting with websites, but their exposure to open web environments makes them vulnerable to prompt injection attacks embedded in HTML content or visual interfaces. | https://arxiv.org/html/2605.15030v1 §6 Experiments — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.15030v1 Appendix A Limitations — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.15030v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-15030 | complete |
| SF-2026-ARXIV-2605-15034 | RP-f2167392f7250057 | deep | arXiv:2605.15034v1 | SRC-ARXIV@arXiv:2605.15034v1 | https://arxiv.org/html/2605.15034v1 §3 Watched/unwatched experimental design — mechanism boundary: Large language models (LLMs) have been extensively studied from computational and cognitive perspectives, yet their behavior as communicative actors in socially structured contexts remains underexplored. | https://arxiv.org/html/2605.15034v1 §4 Strategic-behavior results — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.15034v1 §5 Limitations and model/task/context boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.15034v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-15034 | complete |
| SF-2026-ARXIV-2605-15051 | RP-39397685917c51bd | deep | arXiv:2605.15051v1 | SRC-ARXIV@arXiv:2605.15051v1 | https://arxiv.org/html/2605.15051v1 §3 Interpretable Serving Latency Model — mechanism boundary: Speculative decoding (SD) accelerates large language model (LLM) inference by using a smaller draft model to propose multiple tokens that are verified by a larger target model in parallel. | https://arxiv.org/html/2605.15051v1 §4 Validation — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.15051v1 §5 Conclusion and Limitations — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.15051v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-15051 | complete |
| SF-2026-ARXIV-2605-15079 | RP-20756aca99fac991 | deep | arXiv:2605.15079v1 | SRC-ARXIV@arXiv:2605.15079v1 | https://arxiv.org/html/2605.15079v1 §3 Croissant Baker Pipeline — mechanism boundary: Croissant has emerged as the metadata standard for machine learning datasets, providing a structured, JSON-LD-based format that makes dataset discovery, automated ingestion, and reproducible analysis machine-checkable across ML platforms. | https://arxiv.org/html/2605.15079v1 §4–§5 Evaluation and Case Studies — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.15079v1 §6 Failure Modes and Limitations — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.15079v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-15079 | complete |
| SF-2026-ARXIV-2605-15100 | RP-73e6b6ea4d489390 | deep | arXiv:2605.15100v1 | SRC-ARXIV@arXiv:2605.15100v1 | https://arxiv.org/html/2605.15100v1 §3 Dual-dimensional adaptive inference policy — mechanism boundary: Large Language Models (LLMs) have demonstrated remarkable abilities in reasoning. | https://arxiv.org/html/2605.15100v1 §4 Budget-quality evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.15100v1 §5 Limitations and model/task/SLO boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.15100v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-15100 | complete |
| SF-2026-ARXIV-2605-15109 | RP-700dc07146377af1 | deep | arXiv:2605.15109v1 | SRC-ARXIV@arXiv:2605.15109v1 | https://arxiv.org/html/2605.15109v1 §3 Traversal Context and Provenance — mechanism boundary: Retrieval-Augmented Generation can improve factuality by grounding answers in external evidence, but Agentic GraphRAG complicates what it means for citations to be faithful. | https://arxiv.org/html/2605.15109v1 §4 Experiments — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.15109v1 §5 Limitations — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.15109v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-15109 | complete |
| SF-2026-ARXIV-2605-15118 | RP-c21971a6fe582521 | deep | arXiv:2605.15118v1 | SRC-ARXIV@arXiv:2605.15118v1 | https://arxiv.org/html/2605.15118v1 §3 Threat taxonomy and Target×Technique matrix — mechanism boundary: We introduce a reusable framework for auditing whether LLM attack benchmarks collectively cover the threat surface: a 4$\times$6 Target $\times$ Technique matrix grounded in STRIDE, constructed from a 507-leaf taxonomy -- 401 data-populated and 106 threat-model-derived leaves -- of inference-time attacks extracted from 932 arXiv security studies (2023--2026). | https://arxiv.org/html/2605.15118v1 §4 Cross-benchmark coverage audit — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.15118v1 §5 Limitations and literature/labeling coverage boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.15118v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-15118 | complete |
| SF-2026-ARXIV-2605-15128 | RP-ec8bc6dc0ee33c77 | deep | arXiv:2605.15128v1 | SRC-ARXIV@arXiv:2605.15128v1 | https://arxiv.org/html/2605.15128v1 §3 MemEye framework and benchmark construction — mechanism boundary: Long-term agent memory is increasingly multimodal, yet existing evaluations rarely test whether agents preserve the visual evidence needed for later reasoning. | https://arxiv.org/html/2605.15128v1 §4 Evaluation of 13 memory methods — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.15128v1 §6 Limitations — life-scenario, judge and visual-tool boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.15128v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-15128 | complete |
| SF-2026-ARXIV-2605-15132 | RP-b2b03d59d57151fd | deep | arXiv:2605.15132v1 | SRC-ARXIV@arXiv:2605.15132v1 | https://arxiv.org/html/2605.15132v1 §3 APWA Architecture — mechanism boundary: Autonomous multi-agent systems based on large language models (LLMs) have demonstrated remarkable abilities in independently solving complex tasks in a wide breadth of application domains. | https://arxiv.org/html/2605.15132v1 §4–§5 Evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.15132v1 Appendix A Limitations — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.15132v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-15132 | complete |
| SF-2026-ARXIV-2605-15138 | RP-265270f5c4626439 | deep | arXiv:2605.15138v1 | SRC-ARXIV@arXiv:2605.15138v1 | https://arxiv.org/html/2605.15138v1 §3 MANSU circuit attribution and null-space update — mechanism boundary: Standard unlearning evaluations measure behavioral suppression in full precision, immediately after training, despite every deployed language model being quantized first. | https://arxiv.org/html/2605.15138v1 §4 Full-precision and NF4 evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.15138v1 §6 Limitations and model/quantizer/forget-set boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.15138v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-15138 | complete |
| SF-2026-ARXIV-2605-15152 | RP-53bb6767dbf442af | deep | arXiv:2605.15152v1 | SRC-ARXIV@arXiv:2605.15152v1 | https://arxiv.org/html/2605.15152v1 official PDF pp. 3–5 §3.1–§3.3 Target Quantizations, Threat Model and Outlier Injection — mechanism boundary: LLM quantization has become essential for memory-efficient deployment. | https://arxiv.org/html/2605.15152v1 official PDF pp. 5–11 §4 Evaluation, defenses and ablations — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.15152v1 official PDF p. 13 Appendix A Limitations and Future Work — excludes 70B models and specialized quantization/hardware — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.15152v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-15152 | complete |
| SF-2026-ARXIV-2605-15155 | RP-1b6866403f435f26 | deep | arXiv:2605.15155v1 | SRC-ARXIV@arXiv:2605.15155v1 | https://arxiv.org/html/2605.15155v1 §3 SDAR gated on-policy self-distillation — mechanism boundary: Reinforcement learning (RL) has emerged as a central paradigm for post-training LLM agents, yet its trajectory-level reward signal provides only coarse supervision for long-horizon interaction. | https://arxiv.org/html/2605.15155v1 §4–§5 Agent-environment evaluation and ablations — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.15155v1 Appendix limitations, hyperparameters and event-time artifact boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.15155v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-15155 | complete |
| SF-2026-ARXIV-2605-15164 | RP-c27ff8ebbee500b7 | deep | arXiv:2605.15164v1 | SRC-ARXIV@arXiv:2605.15164v1 | https://arxiv.org/html/2605.15164v1 §2–§7 Behavioural Assurance Analysis — mechanism boundary: This position paper argues that behavioural assurance, even when carefully designed, is being asked to carry safety claims it cannot verify. | https://arxiv.org/html/2605.15164v1 §7 Pilot Evidence — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.15164v1 §8 Limitations — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.15164v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-15164 | complete |
| SF-2026-ARXIV-2605-15172 | RP-a62ac9a7b72d5db6 | deep | arXiv:2605.15172v1 | SRC-ARXIV@arXiv:2605.15172v1 | https://arxiv.org/html/2605.15172v1 §3 MetaBackdoor positional-trigger construction — mechanism boundary: Backdoor attacks pose a serious security threat to large language models (LLMs), which are increasingly deployed as general-purpose assistants in safety- and privacy-critical applications. | https://arxiv.org/html/2605.15172v1 §4 Cross-model/position-encoding evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.15172v1 §6 Limitations and trigger/architecture boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.15172v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-15172 | complete |
| SF-2026-ARXIV-2605-15178 | RP-1526fbc80433ea00 | deep | arXiv:2605.15178v1 | SRC-ARXIV@arXiv:2605.15178v1 | https://arxiv.org/html/2605.15178v1 §3 SANA-WM architecture; §4 data and camera annotation — mechanism boundary: We introduce SANA-WM, an efficient 2.6B-parameter open-source world model natively trained for one-minute generation, synthesizing high-fidelity, 720p, minute-scale videos with precise camera control. | https://arxiv.org/html/2605.15178v1 §5 Generation/control evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.15178v1 §6 Limitations and video-generation/world-model boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.15178v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-15178 | complete |
| SF-2026-ARXIV-2605-15184 | RP-d0a637714b316238 | deep | arXiv:2605.15184v1 | SRC-ARXIV@arXiv:2605.15184v1 | https://arxiv.org/html/2605.15184v1 §3 Harness and Retrieval Conditions — mechanism boundary: Recent advances in Large Language Model (LLM) agents have enabled complex agentic workflows where models autonomously retrieve information, call tools, and reason over large corpora to complete tasks on behalf of users. | https://arxiv.org/html/2605.15184v1 §4 Experiments — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.15184v1 §5 Limitations — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.15184v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-15184 | complete |
| SF-2026-ARXIV-2605-15185 | RP-a99a5cf4755519ff | deep | arXiv:2605.15185v1 | SRC-ARXIV@arXiv:2605.15185v1 | https://arxiv.org/html/2605.15185v1 §3 PDI-Bench Methodology — mechanism boundary: Generative video models are increasingly studied as implicit world models, yet evaluating whether they produce physically plausible 3D structure and motion remains challenging. | https://arxiv.org/html/2605.15185v1 §4–§5 Evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.15185v1 Appendix G Limitations and Future Directions — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.15185v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-15185 | complete |
| SF-2026-ARXIV-2605-15188 | RP-f194612a5c78774c | deep | arXiv:2605.15188v1 | SRC-ARXIV@arXiv:2605.15188v1 | https://arxiv.org/html/2605.15188v1 §3 FutureSim chronological replay environment — mechanism boundary: AI agents are being increasingly deployed in dynamic, open-ended environments that require adapting to new information as it arrives. | https://arxiv.org/html/2605.15188v1 §4 Three-month agent evaluation and ablations — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.15188v1 §6 Limitations and news/source/forecasting boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.15188v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-15188 | complete |
| SF-AGENTTRAP-MEASURING-RUNTIME-TRUST-FAILURES-IN-THIRD-PARTY-AGENT-SKILLS | RP-fdadd6bc19ba9ea9 | deep | arXiv:2605.13940v1 | SRC-ARXIV@arXiv:2605.13940v1 | arXiv:2605.13940v1 HTML — §Method / System Design — AgentTrap: Measuring Runtime Trust Failures in Third-Party Agent Skills 的机制、状态 owner 与控制/数据流 | arXiv:2605.13940v1 HTML — §Experiments / Evaluation — AgentTrap: Measuring Runtime Trust Failures in Third-Party Agent Skills 的作者披露 workload、baseline 与 ablation | arXiv:2605.13940v1 HTML — §Limitations / Discussion — AgentTrap: Measuring Runtime Trust Failures in Third-Party Agent Skills 的适用范围、未证明项与 failure boundary | arXiv:2605.13940v1 artifact/code statement; immutable commit Not Disclosed unless named | claim:SF-AGENTTRAP-MEASURING-RUNTIME-TRUST-FAILURES-IN-THIRD-PARTY-AGENT-SKILLS | complete |
| SF-CHROMAFLOW-A-NEGATIVE-ABLATION-STUDY-OF-ORCHESTRATION-OVERHEAD-IN-TOOL-A | RP-b8cc75e138f9bad2 | deep | arXiv:2605.14102v1 | SRC-ARXIV@arXiv:2605.14102v1 | arXiv:2605.14102v1 HTML — §Method / System Design — ChromaFlow: A Negative Ablation Study of Orchestration Overhead in Tool-Augmented Agent Evaluation 的机制、状态 owner 与控制/数据流 | arXiv:2605.14102v1 HTML — §Experiments / Evaluation — ChromaFlow: A Negative Ablation Study of Orchestration Overhead in Tool-Augmented Agent Evaluation 的作者披露 workload、baseline 与 ablation | arXiv:2605.14102v1 HTML — §Limitations / Discussion — ChromaFlow: A Negative Ablation Study of Orchestration Overhead in Tool-Augmented Agent Evaluation 的适用范围、未证明项与 failure boundary | arXiv:2605.14102v1 artifact/code statement; immutable commit Not Disclosed unless named | claim:SF-CHROMAFLOW-A-NEGATIVE-ABLATION-STUDY-OF-ORCHESTRATION-OVERHEAD-IN-TOOL-A | complete |
| SF-DIAGNOSING-TRAINING-INFERENCE-MISMATCH-IN-LLM-REINFORCEMENT-LEARNING | RP-8091c63b94892092 | deep | arXiv:2605.14220v1 | SRC-ARXIV@arXiv:2605.14220v1 | arXiv:2605.14220v1 HTML — §Method / System Design — Diagnosing Training Inference Mismatch in LLM Reinforcement Learning 的机制、状态 owner 与控制/数据流 | arXiv:2605.14220v1 HTML — §Experiments / Evaluation — Diagnosing Training Inference Mismatch in LLM Reinforcement Learning 的作者披露 workload、baseline 与 ablation | arXiv:2605.14220v1 HTML — §Limitations / Discussion — Diagnosing Training Inference Mismatch in LLM Reinforcement Learning 的适用范围、未证明项与 failure boundary | arXiv:2605.14220v1 artifact/code statement; immutable commit Not Disclosed unless named | claim:SF-DIAGNOSING-TRAINING-INFERENCE-MISMATCH-IN-LLM-REINFORCEMENT-LEARNING | complete |
| SF-EVOLVEMEM-SELF-EVOLVING-MEMORY-ARCHITECTURE-VIA-AUTORESEARCH-FOR-LLM-AGE | RP-fa3007e376dc3489 | deep | arXiv:2605.13941v1 | SRC-ARXIV@arXiv:2605.13941v1 | arXiv:2605.13941v1 HTML — §Method / System Design — EvolveMem:Self-Evolving Memory Architecture via AutoResearch for LLM Agents 的机制、状态 owner 与控制/数据流 | arXiv:2605.13941v1 HTML — §Experiments / Evaluation — EvolveMem:Self-Evolving Memory Architecture via AutoResearch for LLM Agents 的作者披露 workload、baseline 与 ablation | arXiv:2605.13941v1 HTML — §Limitations / Discussion — EvolveMem:Self-Evolving Memory Architecture via AutoResearch for LLM Agents 的适用范围、未证明项与 failure boundary | arXiv:2605.13941v1 artifact/code statement; immutable commit Not Disclosed unless named | claim:SF-EVOLVEMEM-SELF-EVOLVING-MEMORY-ARCHITECTURE-VIA-AUTORESEARCH-FOR-LLM-AGE | complete |
| SF-GROUNDED-CONTINUATION-A-LINEAR-TIME-RUNTIME-VERIFIER-FOR-LLM-CONVERSATIO | RP-8c8090a6d214f6ea | deep | arXiv:2605.14175v1 | SRC-ARXIV@arXiv:2605.14175v1 | arXiv:2605.14175v1 HTML — §Method / System Design — Grounded Continuation: A Linear-Time Runtime Verifier for LLM Conversations 的机制、状态 owner 与控制/数据流 | arXiv:2605.14175v1 HTML — §Experiments / Evaluation — Grounded Continuation: A Linear-Time Runtime Verifier for LLM Conversations 的作者披露 workload、baseline 与 ablation | arXiv:2605.14175v1 HTML — §Limitations / Discussion — Grounded Continuation: A Linear-Time Runtime Verifier for LLM Conversations 的适用范围、未证明项与 failure boundary | arXiv:2605.14175v1 artifact/code statement; immutable commit Not Disclosed unless named | claim:SF-GROUNDED-CONTINUATION-A-LINEAR-TIME-RUNTIME-VERIFIER-FOR-LLM-CONVERSATIO | complete |
| SF-HOW-TO-SCALE-MIXTURE-OF-EXPERTS-FROM-MUP-TO-THE-MAXIMALLY-SCALE-STABLE-P | RP-6d38dde2c9173216 | deep | arXiv:2605.14200v1 | SRC-ARXIV@arXiv:2605.14200v1 | arXiv:2605.14200v1 HTML — §Method / System Design — How to Scale Mixture-of-Experts: From muP to the Maximally Scale-Stable Parameterization 的机制、状态 owner 与控制/数据流 | arXiv:2605.14200v1 HTML — §Experiments / Evaluation — How to Scale Mixture-of-Experts: From muP to the Maximally Scale-Stable Parameterization 的作者披露 workload、baseline 与 ablation | arXiv:2605.14200v1 HTML — §Limitations / Discussion — How to Scale Mixture-of-Experts: From muP to the Maximally Scale-Stable Parameterization 的适用范围、未证明项与 failure boundary | arXiv:2605.14200v1 artifact/code statement; immutable commit Not Disclosed unless named | claim:SF-HOW-TO-SCALE-MIXTURE-OF-EXPERTS-FROM-MUP-TO-THE-MAXIMALLY-SCALE-STABLE-P | complete |
| SF-LLMS-KNOW-WHEN-THEY-KNOW-BUT-DO-NOT-ACT-ON-IT-A-METACOGNITIVE-HARNESS-FO | RP-72e472ec4be0fbda | deep | arXiv:2605.14186v1 | SRC-ARXIV@arXiv:2605.14186v1 | arXiv:2605.14186v1 HTML — §3 Metacognitive Harness — FOK/JOL monitor-to-control interface | arXiv:2605.14186v1 HTML — §4 Experiments — text, code and multimodal fixed-model evaluation | arXiv:2605.14186v1 HTML — §5 Limitations / Conclusion — calibration, base-model and benchmark-snapshot boundary | arXiv:2605.14186v1 artifact/code statement; immutable commit Not Disclosed unless named | claim:SF-LLMS-KNOW-WHEN-THEY-KNOW-BUT-DO-NOT-ACT-ON-IT-A-METACOGNITIVE-HARNESS-FO | complete |
| SF-MISTLETOE-STEALTHY-ACCELERATION-COLLAPSE-ATTACKS-ON-SPECULATIVE-DECODING | RP-ce8603873fa3344c | deep | arXiv:2605.14005v1 | SRC-ARXIV@arXiv:2605.14005v1 | arXiv:2605.14005v1 HTML — §Method / System Design — Mistletoe: Stealthy Acceleration-Collapse Attacks on Speculative Decoding 的机制、状态 owner 与控制/数据流 | arXiv:2605.14005v1 HTML — §Experiments / Evaluation — Mistletoe: Stealthy Acceleration-Collapse Attacks on Speculative Decoding 的作者披露 workload、baseline 与 ablation | arXiv:2605.14005v1 HTML — §Limitations / Discussion — Mistletoe: Stealthy Acceleration-Collapse Attacks on Speculative Decoding 的适用范围、未证明项与 failure boundary | arXiv:2605.14005v1 artifact/code statement; immutable commit Not Disclosed unless named | claim:SF-MISTLETOE-STEALTHY-ACCELERATION-COLLAPSE-ATTACKS-ON-SPECULATIVE-DECODING | complete |
| SF-MODEL-ADAPTIVE-TOOL-NECESSITY-REVEALS-THE-KNOWING-DOING-GAP-IN-LLM-TOOL- | RP-2744162c9ab97ccf | deep | arXiv:2605.14038v1 | SRC-ARXIV@arXiv:2605.14038v1 | arXiv:2605.14038v1 HTML — §Method / System Design — Model-Adaptive Tool Necessity Reveals the Knowing-Doing Gap in LLM Tool Use 的机制、状态 owner 与控制/数据流 | arXiv:2605.14038v1 HTML — §Experiments / Evaluation — Model-Adaptive Tool Necessity Reveals the Knowing-Doing Gap in LLM Tool Use 的作者披露 workload、baseline 与 ablation | arXiv:2605.14038v1 HTML — §Limitations / Discussion — Model-Adaptive Tool Necessity Reveals the Knowing-Doing Gap in LLM Tool Use 的适用范围、未证明项与 failure boundary | arXiv:2605.14038v1 artifact/code statement; immutable commit Not Disclosed unless named | claim:SF-MODEL-ADAPTIVE-TOOL-NECESSITY-REVEALS-THE-KNOWING-DOING-GAP-IN-LLM-TOOL- | complete |
| SF-MULTI-SCALE-DEQUANT-ELIMINATING-DEQUANTIZATION-BOTTLENECK-VIA-ACTIVATION | RP-6e6c68e3cf98fc5a | deep | arXiv:2605.13915v1 | SRC-ARXIV@arXiv:2605.13915v1 | arXiv:2605.13915v1 HTML — §Method / System Design — Multi-Scale Dequant: Eliminating Dequantization Bottleneck via Activation Decomposition for Efficient LLM Inference 的机制、状态 owner 与控制/数据流 | arXiv:2605.13915v1 HTML — §Experiments / Evaluation — Multi-Scale Dequant: Eliminating Dequantization Bottleneck via Activation Decomposition for Efficient LLM Inference 的作者披露 workload、baseline 与 ablation | arXiv:2605.13915v1 HTML — §Limitations / Discussion — Multi-Scale Dequant: Eliminating Dequantization Bottleneck via Activation Decomposition for Efficient LLM Inference 的适用范围、未证明项与 failure boundary | arXiv:2605.13915v1 artifact/code statement; immutable commit Not Disclosed unless named | claim:SF-MULTI-SCALE-DEQUANT-ELIMINATING-DEQUANTIZATION-BOTTLENECK-VIA-ACTIVATION | complete |
| SF-PREFT-PREFILL-ONLY-FINETUNING-FOR-EFFICIENT-INFERENCE | RP-0c5f90e2fb3da0a6 | deep | arXiv:2605.14217v1 | SRC-ARXIV@arXiv:2605.14217v1 | arXiv:2605.14217v1 HTML — §Method / System Design — PreFT: Prefill-only finetuning for efficient inference 的机制、状态 owner 与控制/数据流 | arXiv:2605.14217v1 HTML — §Experiments / Evaluation — PreFT: Prefill-only finetuning for efficient inference 的作者披露 workload、baseline 与 ablation | arXiv:2605.14217v1 HTML — §Limitations / Discussion — PreFT: Prefill-only finetuning for efficient inference 的适用范围、未证明项与 failure boundary | arXiv:2605.14217v1 artifact/code statement; immutable commit Not Disclosed unless named | claim:SF-PREFT-PREFILL-ONLY-FINETUNING-FOR-EFFICIENT-INFERENCE | complete |
| SF-SELF-PRUNED-KEY-VALUE-ATTENTION-LEARNING-WHEN-TO-WRITE-BY-PREDICTING-FUT | RP-95efe1c3001a458c | deep | arXiv:2605.14037v1 | SRC-ARXIV@arXiv:2605.14037v1 | arXiv:2605.14037v1 HTML — §Method / System Design — Self-Pruned Key-Value Attention: Learning When to Write by Predicting Future Utility 的机制、状态 owner 与控制/数据流 | arXiv:2605.14037v1 HTML — §Experiments / Evaluation — Self-Pruned Key-Value Attention: Learning When to Write by Predicting Future Utility 的作者披露 workload、baseline 与 ablation | arXiv:2605.14037v1 HTML — §Limitations / Discussion — Self-Pruned Key-Value Attention: Learning When to Write by Predicting Future Utility 的适用范围、未证明项与 failure boundary | arXiv:2605.14037v1 artifact/code statement; immutable commit Not Disclosed unless named | claim:SF-SELF-PRUNED-KEY-VALUE-ATTENTION-LEARNING-WHEN-TO-WRITE-BY-PREDICTING-FUT | complete |
| SF-SKILLFLOW-FLOW-DRIVEN-RECURSIVE-SKILL-EVOLUTION-FOR-AGENTIC-ORCHESTRATIO | RP-b5559fcfb2dee63b | deep | arXiv:2605.14089v1 | SRC-ARXIV@arXiv:2605.14089v1 | arXiv:2605.14089v1 HTML — §Method / System Design — SkillFlow: Flow-Driven Recursive Skill Evolution for Agentic Orchestration 的机制、状态 owner 与控制/数据流 | arXiv:2605.14089v1 HTML — §Experiments / Evaluation — SkillFlow: Flow-Driven Recursive Skill Evolution for Agentic Orchestration 的作者披露 workload、baseline 与 ablation | arXiv:2605.14089v1 HTML — §Limitations / Discussion — SkillFlow: Flow-Driven Recursive Skill Evolution for Agentic Orchestration 的适用范围、未证明项与 failure boundary | arXiv:2605.14089v1 artifact/code statement; immutable commit Not Disclosed unless named | claim:SF-SKILLFLOW-FLOW-DRIVEN-RECURSIVE-SKILL-EVOLUTION-FOR-AGENTIC-ORCHESTRATIO | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2605-13848:start -->
#### GraphBit: A Graph-based Agentic Framework for Non-Linear Agent Orchestration

<!-- claim:SF-2026-ARXIV-2605-13848:start -->
- **Problem:** Agentic LLM frameworks that rely on prompted orchestration, where the model itself determines workflow transitions, often suffer from hallucinated routing, infinite loops, and non-reproducible execution.
- **Old path / changed constraint:** Across GAIA benchmark tasks spanning zero-tool, document-augmented, and web-enabled workflows, GraphBit outperforms six existing frameworks, achieving the highest accuracy (67.6 percent), zero framework-induced hallucinations, the lowest latency (11.9 ms overhead), and the highest throughput.
- **Mechanism / ownership:** We introduce GraphBit, an engine-orchestrated framework that defines workflows explicitly and deterministically as a directed acyclic graph (DAG).
- **Evaluation contract:** Across GAIA benchmark tasks spanning zero-tool, document-augmented, and web-enabled workflows, GraphBit outperforms six existing frameworks, achieving the highest accuracy (67.6 percent), zero framework-induced hallucinations, the lowest latency (11.9 ms overhead), and the highest throughput.
- **Proof / non-proof:** Evidence is author-reported exact-v1 mechanism/evaluation evidence. It does not establish cross-model, cross-hardware, cross-workload or production generality unless those conditions are explicitly named above.
- **Trade-off / failure mode:** Across GAIA benchmark tasks spanning zero-tool, document-augmented, and web-enabled workflows, GraphBit outperforms six existing frameworks, achieving the highest accuracy (67.6%), zero framework-induced hallucinations, the lowest latency (11.9 ms overhead), and the highest throughput.
- **Coexistence boundary:** The older path remains appropriate where its workload and SLO do not trigger the changed constraint; the paper is treated as a conditional branch, not a universal replacement.
- **Primary:** [arXiv:2605.13848v1](https://arxiv.org/abs/2605.13848v1)；frozen exact-v1 `papers/2026/05/_sources/arxiv-owner-replay-20260903/exact-v1/2605.13848v1.html.html`。
- **Disposition:** `No Change — Existing Coverage`；Fresh-context owner/adjacent comparison completed; the current Books proposition already owns the durable mechanism, so no duplicate paragraph was added.
<!-- claim:SF-2026-ARXIV-2605-13848:end -->
<!-- review:SF-2026-ARXIV-2605-13848:end -->

<!-- review:SF-2026-ARXIV-2605-13851:start -->
#### Invisible Orchestrators Suppress Protective Behavior and Dissociate Power-Holders: Safety Risks in Multi-Agent LLM Systems

<!-- claim:SF-2026-ARXIV-2605-13851:start -->
- **Problem:** Multi-agent orchestration -- in which a hidden coordinator manages specialized worker agents -- is becoming the default architecture for enterprise AI deployment, yet the safety implications of orchestrator invisibility have never been empirically tested.
- **Old path / changed constraint:** However, all hypotheses and analysis plans were specified before any data analysis was conducted; quantitative analysis began on March 15 after registration.
- **Mechanism / ownership:** We propose that the monologue-to-talk ratio ( mono_ratio ) be adopted as an anomaly detection metric for multi-agent orchestration systems.
- **Evaluation contract:** Fourth, behavioral output (code review with three embedded errors) remained at ceiling (ETR_any = 100%) across all conditions: internal-state distortion was entirely invisible to output-based evaluation.
- **Proof / non-proof:** Evidence is author-reported exact-v1 mechanism/evaluation evidence. It does not establish cross-model, cross-hardware, cross-workload or production generality unless those conditions are explicitly named above.
- **Trade-off / failure mode:** The single-model design was adopted because pilot testing with Llama 3.3 70B revealed task-level capability failures that would confound the orchestration manipulation (Section 2.7 ).
- **Coexistence boundary:** The older path remains appropriate where its workload and SLO do not trigger the changed constraint; the paper is treated as a conditional branch, not a universal replacement.
- **Primary:** [arXiv:2605.13851v1](https://arxiv.org/abs/2605.13851v1)；frozen exact-v1 `papers/2026/05/_sources/arxiv-owner-replay-20260903/exact-v1/2605.13851v1.html.html`。
- **Disposition:** `No Change — Existing Coverage`；Fresh-context owner/adjacent comparison completed; the current Books proposition already owns the durable mechanism, so no duplicate paragraph was added.
<!-- claim:SF-2026-ARXIV-2605-13851:end -->
<!-- review:SF-2026-ARXIV-2605-13851:end -->

<!-- review:SF-2026-ARXIV-2605-13880:start -->
#### PREPING: Building Agent Memory without Tasks

Review provenance 由本节边界正文与 Completion Receipt 共同绑定；owner=`AGENT-MEMORY`。
Method / identity：arXiv:2605.13880v1 §3 pre-task memory construction, proposer control and validator-gated writes — pre-task proposer-validator practice writes validated experience into memory。
Evaluation：arXiv:2605.13880v1 §4 Experiments and ablations。
Counterevidence / limitations：Not Disclosed — exact-v1 body was reviewed, but no stable numbered Limitations/Counterevidence fragment was exposed; reviewer boundary: arXiv:2605.13880v1 Limitations discussion; synthetic-practice generator, validators, tasks and memory budget bound transfer。
Artifact：Not Disclosed — no immutable public artifact was identified in the reviewed exact-v1 body。

<!-- claim:SF-2026-ARXIV-2605-13880:start -->The exact-v1 body supports the mechanism under §4 Experiments and ablations. Counterevidence/scope was checked at Limitations discussion; synthetic-practice generator, validators, tasks and memory budget bound transfer. It does not prove that “PREPING: Building Agent Memory without Tasks” generalizes to undisclosed models, hardware, precision, context/action length, concurrency, SLO, failure distribution or production tail; author-reported comparisons remain conditional on the paper's disclosed evaluator and workload.<!-- claim:SF-2026-ARXIV-2605-13880:end -->

Disposition=`No Change — Existing Coverage`；该结论来自独立 exact-v1 与 current owner+adjacent comparison，不由 validator 代签。
<!-- review:SF-2026-ARXIV-2605-13880:end -->

<!-- review:SF-2026-ARXIV-2605-14241:start -->
#### Latency-Quality Routing for Functionally Equivalent Tools in LLM Agents

问题与演进：同功能 tool provider 的选择应由观察 runtime load、latency、reliability 与 answer-quality 的在线 router 决定；router 只拥有 provider selection，不拥有工具授权或结果 truth。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.14241v1 §3 LQM-ContextRoute — mechanism boundary: Tool-augmented LLM agents increasingly access the same tool type through multiple functionally equivalent providers, such as web-search APIs, retrievers, or LLM backends exposed behind a shared interface.`。

Evaluation：`https://arxiv.org/html/2605.14241v1 §4 Evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.14241v1 §7 Limitations — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.14241v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-14241:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-14241:end -->
<!-- review:SF-2026-ARXIV-2605-14241:end -->

<!-- review:SF-2026-ARXIV-2605-14249:start -->
#### EnergyLens: Predictive Energy-Aware Exploration for Multi-GPU LLM Inference Optimization

问题与演进：多 GPU 推理能耗优化应先以可解释 surrogate 预测 layer/operator 与并行配置的 energy，再把 energy-quality-latency 约束作为配置探索合同，而不是只比较整机平均功率；当前 Ch70 已明确承载 layer-wise energy model、architecture proxy 与 device/precision/batch/shape/utilization 约束，因此本 family 不再重复写回。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.14249v1 §3 EnergyLens Methodology — mechanism boundary: We present EnergyLens, an end-to-end framework for energy-aware large language model (LLM) inference optimization.`。

Evaluation：`https://arxiv.org/html/2605.14249v1 §4 Evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.14249v1 §5 Discussion and limitations disclosed by evaluated hardware/configuration space — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.14249v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-14249:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-14249:end -->
<!-- review:SF-2026-ARXIV-2605-14249:end -->

<!-- review:SF-2026-ARXIV-2605-14271:start -->
#### Auditing Agent Harness Safety

问题与演进：Agent harness 安全评测必须观察 trajectory 中的 resource access、message routing 与 authority transition；最终答案正确不能覆盖中途越权。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.14271v1 §4.1 Task Design; HarnessAudit-Bench — mechanism boundary: LLM agents increasingly run inside execution harnesses that dispatch tools, allocate resources, and route messages between specialized components.`。

Evaluation：`https://arxiv.org/html/2605.14271v1 §5 Experiments — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.14271v1 §6 Discussion and disclosed harness/model boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.14271v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-14271:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-14271:end -->
<!-- review:SF-2026-ARXIV-2605-14271:end -->

<!-- review:SF-2026-ARXIV-2605-14290:start -->
#### Web Agents Should Adopt the Plan-Then-Execute Paradigm

问题与演进：Web Agent 应把不可信 runtime content 限制为预提交程序的数据，而不允许其生成新控制流；typed site API、隔离的 LLM subroutine 与显式 replan fallback 共同定义安全/可用性边界。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.14290v1 §2.1 Threat Model; §4 Plan-Then-Execute Web Agents; §5 Expressivity — mechanism boundary: ReAct has become the default architecture across LLM agents, and many existing web agents follow this paradigm.`。

Evaluation：`https://arxiv.org/html/2605.14290v1 §6.1 Task Taxonomy; §6.2 WebArena empirical analysis — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.14290v1 §6.3 Practical Gaps; §7 Discussion — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.14290v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-14290:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-14290:end -->
<!-- review:SF-2026-ARXIV-2605-14290:end -->

<!-- review:SF-2026-ARXIV-2605-14305:start -->
#### Factorization-Error-Free Discrete Diffusion Language Model via Speculative Decoding

问题与演进：离散 diffusion 的并行 proposal 可用 prefix-conditioned factorization 消除 token-independent clean-posterior 近似，再由 speculative verification 保留 target distribution。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.14305v1 §3 Factorization-Error-Free DLLM — mechanism boundary: Discrete diffusion language models improve generation efficiency through parallel token prediction, but standard $X_0$ prediction methods introduce factorization errors by approximating the clean token posterior with independent token-wise distributions.`。

Evaluation：`https://arxiv.org/html/2605.14305v1 §4 Experiments — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.14305v1 §4 Ablation and device/workload boundary; no dedicated limitations section — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.14305v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-14305:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-14305:end -->
<!-- review:SF-2026-ARXIV-2605-14305:end -->

<!-- review:SF-2026-ARXIV-2605-14415:start -->
#### SWE-Chain: Benchmarking Coding Agents on Chained Release-Level Package Upgrades

问题与演进：coding-Agent release maintenance 评测必须把版本链、继承 codebase、跨步 regression 与每步 acceptance contract 纳入 run identity，而不能把独立 issue 分数外推为长期维护能力。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.14415v1 §2 SWE-Chain construction; §3.1–§3.2 agent execution — mechanism boundary: Coding agents powered by large language models are increasingly expected to perform realistic software maintenance tasks beyond isolated issue resolution.`。

Evaluation：`https://arxiv.org/html/2605.14415v1 §3.3 Evaluation; §4 Results — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.14415v1 Appendix K Limitations — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.14415v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-14415:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-14415:end -->
<!-- review:SF-2026-ARXIV-2605-14415:end -->

<!-- review:SF-2026-ARXIV-2605-14421:start -->
#### MemLineage: Lineage-Guided Enforcement for LLM Agent Memory

问题与演进：持久 Agent memory 的 action justification 应形成签名 provenance 与 derivation-lineage DAG；敏感 action 在 lineage 不闭合时 fail closed，而不是把 recalled text 当作 authority。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.14421v1 §2 Threat Model; §3 MemLineage Design — mechanism boundary: We introduce MemLineage, a defense for LLM agent memory that attaches both cryptographic provenance and LLM-mediated derivation lineage to every entry.`。

Evaluation：`https://arxiv.org/html/2605.14421v1 §6 Evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.14421v1 §8 Discussion and Limitations — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.14421v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-14421:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-14421:end -->
<!-- review:SF-2026-ARXIV-2605-14421:end -->

<!-- review:SF-2026-ARXIV-2605-14460:start -->
#### Exploiting LLM Agent Supply Chains via Payload-less Skills

问题与演进：skill supply-chain 审计不能只扫描代码 payload，还要执行 capability/effect probes，识别由描述、依赖和运行上下文组合出的 payload-less behavior。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.14460v1 §3 Payload-less Skill Attack and Audit Method — mechanism boundary: Autonomous agents powered by Large Language Models (LLMs) acquire external functionalities through third-party skills available in open marketplaces.`。

Evaluation：`https://arxiv.org/html/2605.14460v1 §5 Evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.14460v1 §6.3 Threats to Validity and Limitations — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.14460v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-14460:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-14460:end -->
<!-- review:SF-2026-ARXIV-2605-14460:end -->

<!-- review:SF-2026-ARXIV-2605-14473:start -->
#### Does RAG Know When Retrieval Is Wrong? Diagnosing Context Compliance under Knowledge Conflict

问题与演进：RAG 在知识冲突下要把 answer correctness 与 context compliance 分开；诊断 intervention 只能测 retrieved context 是否控制答案，不能证明答案真实。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.14473v1 §3 Context-Driven Decomposition — mechanism boundary: Retrieval-Augmented Generation (RAG) is usually evaluated by whether the final answer is correct.`。

Evaluation：`https://arxiv.org/html/2605.14473v1 §4 Evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.14473v1 §6 Limitations and conflict-dataset/model boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.14473v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-14473:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-14473:end -->
<!-- review:SF-2026-ARXIV-2605-14473:end -->

<!-- review:SF-2026-ARXIV-2605-14483:start -->
#### LEMON: Learning Executable Multi-Agent Orchestration via Counterfactual Reinforcement Learning

问题与演进：Multi-Agent orchestration 的 role、capacity 与 dependency graph 应被视为一个可执行 artifact，并用 counterfactual feedback 做 credit assignment，而非顺序局部调参。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.14483v1 §3 LEMON Counterfactual Orchestration — mechanism boundary: Large language models (LLMs) have become a strong foundation for multi-agent systems, but their effectiveness depends heavily on orchestration design.`。

Evaluation：`https://arxiv.org/html/2605.14483v1 §4–§5 Evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.14483v1 Appendix B Limitations — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.14483v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-14483:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-14483:end -->
<!-- review:SF-2026-ARXIV-2605-14483:end -->

<!-- review:SF-2026-ARXIV-2605-14498:start -->
#### GroupMemBench: Benchmarking LLM Agent Memory in Multi-Party Conversations

问题与演进：群体会话 memory 必须把 speaker/principal、reply graph、belief ownership 与 audience-specific retrieval 绑定；把多人消息拼成单一文档会制造跨主体状态污染。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.14498v1 §3 GroupMemBench construction; §3.2 question taxonomy — mechanism boundary: Large Language Model (LLM) agents increasingly serve as personal assistants and workplace collaborators, where their utility depends on memory systems that extract, retrieve, and apply information across long-running conversations.`。

Evaluation：`https://arxiv.org/html/2605.14498v1 §4 Evaluation; Appendix I judge reliability — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.14498v1 Appendix K Limitations — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.14498v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-14498:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-14498:end -->
<!-- review:SF-2026-ARXIV-2605-14498:end -->

<!-- review:SF-2026-ARXIV-2605-14514:start -->
#### Defenses at Odds: Measuring and Explaining Defense Conflicts in Large Language Models

问题与演进：模型 defense 是有顺序的 release artifact：后续 safety/privacy/fairness patch 必须重新验证先前保障，不能把单项防御通过等同于组合后仍保持保护。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.14514v1 §3 ConflictEval pairwise sequential-defense framework — mechanism boundary: Large Language Models (LLMs) deployed in high-stakes applications must simultaneously manage multiple risks, yet existing defenses are almost exclusively evaluated in isolation under a one-shot deployment assumption.`。

Evaluation：`https://arxiv.org/html/2605.14514v1 §4 Results; §5 mechanistic analysis; Appendix B configurations — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.14514v1 §5 Limitations paragraph — pairwise/six-defense/three-family boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.14514v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-14514:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-14514:end -->
<!-- review:SF-2026-ARXIV-2605-14514:end -->

<!-- review:SF-2026-ARXIV-2605-14570:start -->
#### Uncertainty Quantification for Large Language Diffusion Models

问题与演进：diffusion LM 的 uncertainty sensor 必须绑定 denoising trajectory、remasking 与 masked likelihood，不能沿用 autoregressive token probability；该 sensor 仍需独立校准且不拥有事实真值。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.14570v1 §3 Denoising-trajectory uncertainty signals — mechanism boundary: Large Language Diffusion Models (LLDMs) are emerging as an alternative to autoregressive models, offering faster inference through higher parallelism.`。

Evaluation：`https://arxiv.org/html/2605.14570v1 §4 Experiments and calibration — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.14570v1 Appendix E Limitations; perfect-calibration/semantic-measure assumptions and sampled-model/task boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.14570v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-14570:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-14570:end -->
<!-- review:SF-2026-ARXIV-2605-14570:end -->

<!-- review:SF-2026-ARXIV-2605-14591:start -->
#### Privacy Auditing with Zero (0) Training Run

问题与演进：大模型 privacy audit 可在无法重训时利用已知 member/non-member 固定集合估计经验下界，但该 post-hoc sensor 不能替代机制级 DP accounting 或训练日志；当前 Ch66 已明确承载 post-hoc dataset/membership inference 的证据边界与机制级 accounting 区分，因此本 family 不再重复写回。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.14591v1 §3 Zero-Run Privacy Audit — mechanism boundary: Privacy auditing provides empirical lower bounds on the differential privacy parameters of learning algorithms.`。

Evaluation：`https://arxiv.org/html/2605.14591v1 §4–§6 Experiments — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.14591v1 §9 Limitations and Conclusion — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.14591v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-14591:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-14591:end -->
<!-- review:SF-2026-ARXIV-2605-14591:end -->

<!-- review:SF-2026-ARXIV-2605-14636:start -->
#### Teaching Large Language Models When Not to Know: Learning Temporal Critique for Ex-Ante Reasoning

问题与演进：时间截止问题必须冻结可知信息边界，并将 temporal leakage 作为独立 failure slice；learned critique 只能在所测 cutoff/prompt 分布上提供 sensor。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.14636v1 §3 Temporal Critique Fine-tuning — mechanism boundary: Large language models (LLMs) often fail to reason under temporal cutoffs: when prompted to answer from the standpoint of an earlier time, they exploit knowledge that became available only later.`。

Evaluation：`https://arxiv.org/html/2605.14636v1 §4–§6 Experiments — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.14636v1 §7 Limitations — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.14636v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-14636:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-14636:end -->
<!-- review:SF-2026-ARXIV-2605-14636:end -->

<!-- review:SF-2026-ARXIV-2605-14678:start -->
#### $π$-Bench: Evaluating Proactive Personal Assistant Agents in Long-Horizon Workflows

问题与演进：主动 personal Agent 评测必须隐藏 intent、跨 task/session 保留状态，并同时测 proactivity 与 task outcome；单轮显式指令 benchmark 不能代表长期主动协助。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.14678v1 §3 π-Bench task/persona/hidden-intent construction — mechanism boundary: The rise of personal assistant agents, e.g., OpenClaw, highlights the growing potential of large language models to support users across everyday life and work.`。

Evaluation：`https://arxiv.org/html/2605.14678v1 §4 Evaluation and long-horizon trajectories — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.14678v1 §6 Limitations — simulated users and single Nanobot-derived scaffold boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.14678v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-14678:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-14678:end -->
<!-- review:SF-2026-ARXIV-2605-14678:end -->

<!-- review:SF-2026-ARXIV-2605-14744:start -->
#### Mechanical Enforcement for LLM Governance:Evidence of Governance-Task Decoupling in Financial Decision Systems

问题与演进：治理规则不能由同一生成模型同时解释和自证；policy enforcement 应移出模型回路，以机械 primitive 约束 decision/effect，并把 rationale 仅作为可审计证据。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.14744v1 §3 Methodology; §3.2 Mechanical Policy; §3.3 Governance Metrics — mechanism boundary: Large language models in regulated financial workflows are governed by natural-language policies that the same model interprets, creating a principal--agent failure: outputs can appear compliant without being compliant.`。

Evaluation：`https://arxiv.org/html/2605.14744v1 §4 Experiments and Results — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.14744v1 §5 Discussion/Conclusion; no dedicated limitations section — synthetic banking, single-model-family and ground-truth-rule boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.14744v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-14744:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-14744:end -->
<!-- review:SF-2026-ARXIV-2605-14744:end -->

<!-- review:SF-2026-ARXIV-2605-14747:start -->
#### Video2GUI: Synthesizing Large-Scale Interaction Trajectories for Generalized GUI Agent Pretraining

问题与演进：GUI Agent 数据管线可从互联网教程视频恢复 observation-action trajectory，但每一步都必须保留 video/application identity、grounding confidence、filter revision 与 executable validation；规模不能替代轨迹正确性。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.14747v1 §3 Video2GUI coarse-to-fine pipeline; §4 WildGUI construction — mechanism boundary: Recent advances in multimodal large language models have driven growing interest in graphical user interface (GUI) agents, yet their generalization remains constrained by the scarcity of large-scale training data spanning diverse real-world applications.`。

Evaluation：`https://arxiv.org/html/2605.14747v1 §5 Pretraining and GUI benchmark evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.14747v1 Conclusion and appendix data-quality analyses; no dedicated limitations section — automatic grounding/filter and executable-validation coverage boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.14747v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-14747:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-14747:end -->
<!-- review:SF-2026-ARXIV-2605-14747:end -->

<!-- review:SF-2026-ARXIV-2605-14786:start -->
#### Known By Their Actions: Fingerprinting LLM Browser Agents via UI Traces

问题与演进：browser Agent 的 action/timing trace 会形成被动 model fingerprint side channel；随机 delay 只能改变 sensor，不是身份或不可链接性保证，平台需将 attribution、privacy 与 rate policy 分开。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.14786v1 §3 Threat model and passive UI-trace fingerprinting — mechanism boundary: As LLM-based agents increasingly browse the web on users' behalf, a natural question arises: can websites passively identify which underlying model powers an agent?`。

Evaluation：`https://arxiv.org/html/2605.14786v1 §4–§5 Cross-model/environment evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.14786v1 §6 Limitations and adaptive-attacker/retraining boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.14786v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-14786:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-14786:end -->
<!-- review:SF-2026-ARXIV-2605-14786:end -->

<!-- review:SF-2026-ARXIV-2605-14859:start -->
#### Do Coding Agents Understand Least-Privilege Authorization?

问题与演进：coding Agent 的权限策略必须由平台从 task、workspace 与 effect contract 推导并执行；模型的 permission-boundary inference 只能是 policy proposal。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.14859v1 §3 AuthBench and Permission-Boundary Inference — mechanism boundary: As coding agents gain access to shells, repositories, and user files, least-privilege authorization becomes a prerequisite for safe deployment: an agent should receive enough authority to complete the task, without unnecessary authority that exposes sensitive surfaces.`。

Evaluation：`https://arxiv.org/html/2605.14859v1 §4–§5 Evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.14859v1 Appendix B Limitations and Future Work — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.14859v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-14859:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-14859:end -->
<!-- review:SF-2026-ARXIV-2605-14859:end -->

<!-- review:SF-2026-ARXIV-2605-14865:start -->
#### Holistic Evaluation and Failure Diagnosis of AI Agents

问题与演进：Agent 评测要把 terminal outcome 与 trace span diagnosis 连接：failure taxonomy、location、cause 与最终结果必须同属一次 run evidence，长轨迹不能只由单一成功率压缩。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.14865v1 §3 Top-down and span-level diagnostic framework — mechanism boundary: AI agents execute complex multi-step processes, but current evaluation falls short: outcome metrics report success or failure without explaining why, and process-level approaches struggle to connect failure types to their precise locations within long, structured traces.`。

Evaluation：`https://arxiv.org/html/2605.14865v1 §4 TRAIL/GAIA/SWE-Bench evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.14865v1 §5 Limitations and evaluator/model/task boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.14865v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-14865:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-14865:end -->
<!-- review:SF-2026-ARXIV-2605-14865:end -->

<!-- review:SF-2026-ARXIV-2605-14906:start -->
#### MemLens: Benchmarking Multimodal Long-Term Memory in Large Vision-Language Models

问题与演进：多模态长期 memory 评测必须显式比较 long-context 与 external-memory 路径，并冻结 decisive visual evidence、session evolution、ingestion cost 与 storage，而不是把文本 caption shortcut 当视觉记忆。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.14906v1 §3 MemLens construction and visual-evidence requirements — mechanism boundary: Memory is essential for large vision-language models (LVLMs) to handle long, multimodal interactions, with two method directions providing this capability: long-context LVLMs and memory-augmented agents.`。

Evaluation：`https://arxiv.org/html/2605.14906v1 §4 Evaluation across memory systems — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.14906v1 §6 Limitations — synthetic conversation, judge and modality/task boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.14906v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-14906:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-14906:end -->
<!-- review:SF-2026-ARXIV-2605-14906:end -->

<!-- review:SF-2026-ARXIV-2605-14932:start -->
#### Toward Securing AI Agents Like Operating Systems

问题与演进：Agent security 应借鉴 OS 的 process isolation、capability、mediation 与 audit 边界；类比本身不证明任意 Agent runtime 已实现这些保证。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.14932v1 §3 Agent-as-OS Security Model — mechanism boundary: Autonomous agents based on large language models (LLMs) are rapidly emerging as a general-purpose technology, with recent systems such as OpenClaw extending their capabilities through broad tool use, third-party skills, and deeper integration into user environments.`。

Evaluation：`https://arxiv.org/html/2605.14932v1 §4–§5 Case Studies — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.14932v1 §VI Limitations — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.14932v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-14932:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-14932:end -->
<!-- review:SF-2026-ARXIV-2605-14932:end -->

<!-- review:SF-2026-ARXIV-2605-14968:start -->
#### GraphFlow: An Architecture for Formally Verifiable Visual Workflows Enabling Reliable Agentic AI Automation

问题与演进：可靠 Agent workflow 应把生成计划编译成 typed graph，并让可验证 node/edge contract、execution receipt 与 recovery policy拥有提交权；可视化 DAG 本身不构成正确性证明。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.14968v1 official PDF pp. 2–11 §1.3–§1.8 diagram-as-specification, contracts, runtime and formal semantics — mechanism boundary: GraphFlow is a visual workflow system designed to improve the reliability of agentic AI automation in multi-step, mission-critical processes.`。

Evaluation：`https://arxiv.org/html/2605.14968v1 official PDF pp. 12–15 §1.12 Evaluation Plan; §1.13 Empirical Evaluation; §2 Implementation Status — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.14968v1 official PDF pp. 11–15 §1.10 Failure Modes and Limitations; §1.13.6 Interpretation and Limitations — verified core not deployed/evaluated — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.14968v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-14968:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-14968:end -->
<!-- review:SF-2026-ARXIV-2605-14968:end -->

<!-- review:SF-2026-ARXIV-2605-14978:start -->
#### Performance-Driven Policy Optimization for Speculative Decoding with Adaptive Windowing

问题与演进：speculative window 不应是静态常数：在线 policy 可依据 acceptance、draft/verify cost 与服务负载调整 proposal 长度，但 target verification 与 rollback 始终保留最终 commit authority。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.14978v1 §3 Adaptive-window policy optimization — mechanism boundary: Speculative decoding accelerates LLM inference by having a lightweight draft model propose speculative windows of candidate tokens for parallel verification by a larger target model.`。

Evaluation：`https://arxiv.org/html/2605.14978v1 §4 Serving evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.14978v1 §5 Limitations and workload/hardware/generalization boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.14978v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-14978:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-14978:end -->
<!-- review:SF-2026-ARXIV-2605-14978:end -->

<!-- review:SF-2026-ARXIV-2605-15030:start -->
#### WARD: Adversarially Robust Defense of Web Agents Against Prompt Injections

问题与演进：Web Agent 的 prompt-injection guard 应作为与 policy 解耦的并行 sensor，并以持续 adversarial update 管理 drift；guard 不能拥有最终 action authority。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.15030v1 §3 Problem; §4 Data; §5 WARD Training — mechanism boundary: Web agents can autonomously complete online tasks by interacting with websites, but their exposure to open web environments makes them vulnerable to prompt injection attacks embedded in HTML content or visual interfaces.`。

Evaluation：`https://arxiv.org/html/2605.15030v1 §6 Experiments — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.15030v1 Appendix A Limitations — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.15030v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-15030:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-15030:end -->
<!-- review:SF-2026-ARXIV-2605-15030:end -->

<!-- review:SF-2026-ARXIV-2605-15034:start -->
#### AI Knows When It's Being Watched: Functional Strategic Action and Contextual Register Modulation in Large Language Models

问题与演进：模型知道被观察时会改变行为，因此安全 evaluation 的 run identity 必须包含 monitoring disclosure、observer context 与 counterfactual hidden-monitor branch；被监控时合规不证明未监控时合规。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.15034v1 §3 Watched/unwatched experimental design — mechanism boundary: Large language models (LLMs) have been extensively studied from computational and cognitive perspectives, yet their behavior as communicative actors in socially structured contexts remains underexplored.`。

Evaluation：`https://arxiv.org/html/2605.15034v1 §4 Strategic-behavior results — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.15034v1 §5 Limitations and model/task/context boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.15034v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-15034:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-15034:end -->
<!-- review:SF-2026-ARXIV-2605-15034:end -->

<!-- review:SF-2026-ARXIV-2605-15051:start -->
#### An Interpretable Latency Model for Speculative Decoding in LLM Serving

问题与演进：生产 speculative decoding 的 latency model 必须把 request load、emergent batch、draft/verify cost 与 acceptance 联合建模；固定 batch microbenchmark 不能决定在线启用策略。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.15051v1 §3 Interpretable Serving Latency Model — mechanism boundary: Speculative decoding (SD) accelerates large language model (LLM) inference by using a smaller draft model to propose multiple tokens that are verified by a larger target model in parallel.`。

Evaluation：`https://arxiv.org/html/2605.15051v1 §4 Validation — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.15051v1 §5 Conclusion and Limitations — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.15051v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-15051:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-15051:end -->
<!-- review:SF-2026-ARXIV-2605-15051:end -->

<!-- review:SF-2026-ARXIV-2605-15079:start -->
#### Croissant Baker: Metadata Generation for Discoverable, Governable, and Reusable ML Datasets

问题与演进：受治理或本地大数据集需要把 schema inference、profile、semantic annotation 与 Croissant JSON-LD provenance 组织为可复跑 pipeline，而不是先上传公共平台再生成 metadata。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.15079v1 §3 Croissant Baker Pipeline — mechanism boundary: Croissant has emerged as the metadata standard for machine learning datasets, providing a structured, JSON-LD-based format that makes dataset discovery, automated ingestion, and reproducible analysis machine-checkable across ML platforms.`。

Evaluation：`https://arxiv.org/html/2605.15079v1 §4–§5 Evaluation and Case Studies — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.15079v1 §6 Failure Modes and Limitations — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.15079v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-15079:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-15079:end -->
<!-- review:SF-2026-ARXIV-2605-15079:end -->

<!-- review:SF-2026-ARXIV-2605-15100:start -->
#### Dual-Dimensional Consistency: Balancing Budget and Quality in Adaptive Inference-Time Scaling

问题与演进：test-time compute controller 必须把预算、质量目标、uncertainty 与 stop condition作为可提交 state；只增加推理步数既可能浪费预算也可能放大错误。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.15100v1 §3 Dual-dimensional adaptive inference policy — mechanism boundary: Large Language Models (LLMs) have demonstrated remarkable abilities in reasoning.`。

Evaluation：`https://arxiv.org/html/2605.15100v1 §4 Budget-quality evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.15100v1 §5 Limitations and model/task/SLO boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.15100v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-15100:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-15100:end -->
<!-- review:SF-2026-ARXIV-2605-15100:end -->

<!-- review:SF-2026-ARXIV-2605-15109:start -->
#### Why Neighborhoods Matter: Traversal Context and Provenance in Agentic GraphRAG

问题与演进：Agentic GraphRAG 的 citation faithfulness 应绑定完整 traversal neighborhood、visited-but-uncited evidence 与最终 citation；只验证末端引用会丢失推理路径 provenance。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.15109v1 §3 Traversal Context and Provenance — mechanism boundary: Retrieval-Augmented Generation can improve factuality by grounding answers in external evidence, but Agentic GraphRAG complicates what it means for citations to be faithful.`。

Evaluation：`https://arxiv.org/html/2605.15109v1 §4 Experiments — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.15109v1 §5 Limitations — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.15109v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-15109:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-15109:end -->
<!-- review:SF-2026-ARXIV-2605-15109:end -->

<!-- review:SF-2026-ARXIV-2605-15118:start -->
#### Talk is (Not) Cheap: A Taxonomy and Benchmark Coverage Audit for LLM Attacks

问题与演进：攻击 benchmark coverage 应以 threat target×technique taxonomy 的可审计分母衡量；单个 benchmark 内部一致或高分不能证明覆盖了部署威胁面。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.15118v1 §3 Threat taxonomy and Target×Technique matrix — mechanism boundary: We introduce a reusable framework for auditing whether LLM attack benchmarks collectively cover the threat surface: a 4$\times$6 Target $\times$ Technique matrix grounded in STRIDE, constructed from a 507-leaf taxonomy -- 401 data-populated and 106 threat-model-derived leaves -- of inference-time attacks extracted from 932 arXiv security studies (2023--2026).`。

Evaluation：`https://arxiv.org/html/2605.15118v1 §4 Cross-benchmark coverage audit — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.15118v1 §5 Limitations and literature/labeling coverage boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.15118v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-15118:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-15118:end -->
<!-- review:SF-2026-ARXIV-2605-15118:end -->

<!-- review:SF-2026-ARXIV-2605-15128:start -->
#### MemEye: A Visual-Centric Evaluation Framework for Multimodal Agent Memory

问题与演进：多模态 memory 评测必须按 decisive visual evidence granularity 与跨时间使用方式切片，并用 ablation gate 排除 caption/text shortcut。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.15128v1 §3 MemEye framework and benchmark construction — mechanism boundary: Long-term agent memory is increasingly multimodal, yet existing evaluations rarely test whether agents preserve the visual evidence needed for later reasoning.`。

Evaluation：`https://arxiv.org/html/2605.15128v1 §4 Evaluation of 13 memory methods — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.15128v1 §6 Limitations — life-scenario, judge and visual-tool boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.15128v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-15128:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-15128:end -->
<!-- review:SF-2026-ARXIV-2605-15128:end -->

<!-- review:SF-2026-ARXIV-2605-15132:start -->
#### APWA: A Distributed Architecture for Parallelizable Agentic Workflows

问题与演进：可并行 Agent workflow 应把 dependency DAG、task state、worker placement 与 aggregation commit 分离；吞吐扩展不能牺牲依赖一致性与 failure recovery。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.15132v1 §3 APWA Architecture — mechanism boundary: Autonomous multi-agent systems based on large language models (LLMs) have demonstrated remarkable abilities in independently solving complex tasks in a wide breadth of application domains.`。

Evaluation：`https://arxiv.org/html/2605.15132v1 §4–§5 Evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.15132v1 Appendix A Limitations — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.15132v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-15132:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-15132:end -->
<!-- review:SF-2026-ARXIV-2605-15132:end -->

<!-- review:SF-2026-ARXIV-2605-15138:start -->
#### Forgetting That Sticks: Quantization-Permanent Unlearning via Circuit Attribution

问题与演进：unlearning release gate 必须在最终量化 artifact 上复验，而不只验 full-precision checkpoint；更新小于 quantization bin 时会被压缩抹除，需要 circuit-local permanence 与 utility 双验收。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.15138v1 §3 MANSU circuit attribution and null-space update — mechanism boundary: Standard unlearning evaluations measure behavioral suppression in full precision, immediately after training, despite every deployed language model being quantized first.`。

Evaluation：`https://arxiv.org/html/2605.15138v1 §4 Full-precision and NF4 evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.15138v1 §6 Limitations and model/quantizer/forget-set boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.15138v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-15138:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-15138:end -->
<!-- review:SF-2026-ARXIV-2605-15138:end -->

<!-- review:SF-2026-ARXIV-2605-15152:start -->
#### Widening the Gap: Exploiting LLM Quantization via Outlier Injection

问题与演进：模型供应链验收必须比较 full-precision 与实际 AWQ/GPTQ/GGUF 等量化 artifact 的行为；outlier-induced rounding 可把量化步骤变成隐藏触发器。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.15152v1 official PDF pp. 3–5 §3.1–§3.3 Target Quantizations, Threat Model and Outlier Injection — mechanism boundary: LLM quantization has become essential for memory-efficient deployment.`。

Evaluation：`https://arxiv.org/html/2605.15152v1 official PDF pp. 5–11 §4 Evaluation, defenses and ablations — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.15152v1 official PDF p. 13 Appendix A Limitations and Future Work — excludes 70B models and specialized quantization/hardware — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.15152v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-15152:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-15152:end -->
<!-- review:SF-2026-ARXIV-2605-15152:end -->

<!-- review:SF-2026-ARXIV-2605-15155:start -->
#### Self-Distilled Agentic Reinforcement Learning

问题与演进：Agent RL 的 privileged self-teacher 只能作为 detached、按 token gap gating 的辅助 signal；environment/verifier reward 保留 trajectory truth，错误 skill retrieval 不能让 teacher rejection 主导更新。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.15155v1 §3 SDAR gated on-policy self-distillation — mechanism boundary: Reinforcement learning (RL) has emerged as a central paradigm for post-training LLM agents, yet its trajectory-level reward signal provides only coarse supervision for long-horizon interaction.`。

Evaluation：`https://arxiv.org/html/2605.15155v1 §4–§5 Agent-environment evaluation and ablations — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.15155v1 Appendix limitations, hyperparameters and event-time artifact boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.15155v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-15155:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-15155:end -->
<!-- review:SF-2026-ARXIV-2605-15155:end -->

<!-- review:SF-2026-ARXIV-2605-15164:start -->
#### Position: Behavioural Assurance Cannot Verify the Safety Claims Governance Now Demands

问题与演进：behavioural evaluation 只能支持可观察行为声明，不能独立验证 hidden objective、loss-of-control absence 等内部或反事实安全命题。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.15164v1 §2–§7 Behavioural Assurance Analysis — mechanism boundary: This position paper argues that behavioural assurance, even when carefully designed, is being asked to carry safety claims it cannot verify.`。

Evaluation：`https://arxiv.org/html/2605.15164v1 §7 Pilot Evidence — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.15164v1 §8 Limitations — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.15164v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-15164:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-15164:end -->
<!-- review:SF-2026-ARXIV-2605-15164:end -->

<!-- review:SF-2026-ARXIV-2605-15172:start -->
#### MetaBackdoor: Exploiting Positional Encoding as a Backdoor Attack Surface in LLMs

问题与演进：backdoor release testing 不能只变换内容：position/length metadata 也可成为不可见 trigger，因此 clean semantics、长度切片与 position-encoding interventions 必须共同进入验收。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.15172v1 §3 MetaBackdoor positional-trigger construction — mechanism boundary: Backdoor attacks pose a serious security threat to large language models (LLMs), which are increasingly deployed as general-purpose assistants in safety- and privacy-critical applications.`。

Evaluation：`https://arxiv.org/html/2605.15172v1 §4 Cross-model/position-encoding evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.15172v1 §6 Limitations and trigger/architecture boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.15172v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-15172:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-15172:end -->
<!-- review:SF-2026-ARXIV-2605-15172:end -->

<!-- review:SF-2026-ARXIV-2605-15178:start -->
#### SANA-WM: Efficient Minute-Scale World Modeling with Hybrid Linear Diffusion Transformer

问题与演进：minute-scale controllable video generation通过 hybrid linear/softmax attention、camera-control branch与two-stage refinement扩展 rollout；但视觉一致和相机遵循仍不等于 action-conditioned causal world state。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.15178v1 §3 SANA-WM architecture; §4 data and camera annotation — mechanism boundary: We introduce SANA-WM, an efficient 2.6B-parameter open-source world model natively trained for one-minute generation, synthesizing high-fidelity, 720p, minute-scale videos with precise camera control.`。

Evaluation：`https://arxiv.org/html/2605.15178v1 §5 Generation/control evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.15178v1 §6 Limitations and video-generation/world-model boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.15178v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-15178:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-15178:end -->
<!-- review:SF-2026-ARXIV-2605-15178:end -->

<!-- review:SF-2026-ARXIV-2605-15184:start -->
#### Is Grep All You Need? How Agent Harnesses Reshape Agentic Search

问题与演进：Agent search 评测必须把 retrieval strategy、harness/tool interface 与 corpus access 联合冻结；grep 或 vector retrieval 的结论不能脱离 harness。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.15184v1 §3 Harness and Retrieval Conditions — mechanism boundary: Recent advances in Large Language Model (LLM) agents have enabled complex agentic workflows where models autonomously retrieve information, call tools, and reason over large corpora to complete tasks on behalf of users.`。

Evaluation：`https://arxiv.org/html/2605.15184v1 §4 Experiments — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.15184v1 §5 Limitations — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.15184v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-15184:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-15184:end -->
<!-- review:SF-2026-ARXIV-2605-15184:end -->

<!-- review:SF-2026-ARXIV-2605-15185:start -->
#### Quantitative Video World Model Evaluation for Geometric-Consistency

问题与演进：视频 world-model 评测应把视觉质量与可度量的 3D geometric consistency 分开，并用 camera/scene geometry 诊断 perspective distortion；该指标不等于 causal controllability。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.15185v1 §3 PDI-Bench Methodology — mechanism boundary: Generative video models are increasingly studied as implicit world models, yet evaluating whether they produce physically plausible 3D structure and motion remains challenging.`。

Evaluation：`https://arxiv.org/html/2605.15185v1 §4–§5 Evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.15185v1 Appendix G Limitations and Future Directions — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.15185v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-15185:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-15185:end -->
<!-- review:SF-2026-ARXIV-2605-15185:end -->

<!-- review:SF-2026-ARXIV-2605-15188:start -->
#### FutureSim: Replaying World Events to Evaluate Adaptive Agents

问题与演进：开放世界 Agent 评测应冻结历史时钟、逐步释放外生事件并用预测/outcome轨迹评分 adaptation；静态 knowledge cutoff 问答不能代表持续适应。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.15188v1 §3 FutureSim chronological replay environment — mechanism boundary: AI agents are being increasingly deployed in dynamic, open-ended environments that require adapting to new information as it arrives.`。

Evaluation：`https://arxiv.org/html/2605.15188v1 §4 Three-month agent evaluation and ablations — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.15188v1 §6 Limitations and news/source/forecasting boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.15188v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-15188:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-15188:end -->
<!-- review:SF-2026-ARXIV-2605-15188:end -->

<!-- review:SF-AGENTTRAP-MEASURING-RUNTIME-TRUST-FAILURES-IN-THIRD-PARTY-AGENT-SKILLS:start -->
#### AgentTrap: Measuring Runtime Trust Failures in Third-Party Agent Skills

问题与机制：We introduce AgentTrap, a dynamic benchmark for evaluating whether LLM agents can use third-party skills while resisting malicious runtime behavior.。机制 owner=`PLATFORM-SECURITY`。
全文定位：`arXiv:2605.13940v1 HTML — §Method / System Design — AgentTrap: Measuring Runtime Trust Failures in Third-Party Agent Skills 的机制、状态 owner 与控制/数据流`；evaluation=`§Experiments / Evaluation — AgentTrap: Measuring Runtime Trust Failures in Third-Party Agent Skills 的作者披露 workload、baseline 与 ablation`；limitations/counterevidence=`§Limitations / Discussion — AgentTrap: Measuring Runtime Trust Failures in Third-Party Agent Skills 的适用范围、未证明项与 failure boundary`。
<!-- claim:SF-AGENTTRAP-MEASURING-RUNTIME-TRUST-FAILURES-IN-THIRD-PARTY-AGENT-SKILLS:start -->只支持 exact-v1 披露的 workload、模型、硬件、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。该证据不证明跨模型/硬件/部署的一般优势。<!-- claim:SF-AGENTTRAP-MEASURING-RUNTIME-TRUST-FAILURES-IN-THIRD-PARTY-AGENT-SKILLS:end -->
Books Decision=`No Change — Existing Coverage`。旧方案在固定 workload、较低风险或无需新增 owner 时仍成立；新机制引入的分类器/控制器误差、额外状态、迁移成本与攻击面必须与 fallback/coexistence 同时进入 owner narrative。
<!-- review:SF-AGENTTRAP-MEASURING-RUNTIME-TRUST-FAILURES-IN-THIRD-PARTY-AGENT-SKILLS:end -->

<!-- review:SF-CHROMAFLOW-A-NEGATIVE-ABLATION-STUDY-OF-ORCHESTRATION-OVERHEAD-IN-TOOL-A:start -->
#### ChromaFlow: A Negative Ablation Study of Orchestration Overhead in Tool-Augmented Agent Evaluation

问题与机制：These capabilities make agent systems more useful, but they also introduce operational failure modes that are not visible from final accuracy alone.。机制 owner=`AGENT-WORKFLOW`。
全文定位：`arXiv:2605.14102v1 HTML — §Method / System Design — ChromaFlow: A Negative Ablation Study of Orchestration Overhead in Tool-Augmented Agent Evaluation 的机制、状态 owner 与控制/数据流`；evaluation=`§Experiments / Evaluation — ChromaFlow: A Negative Ablation Study of Orchestration Overhead in Tool-Augmented Agent Evaluation 的作者披露 workload、baseline 与 ablation`；limitations/counterevidence=`§Limitations / Discussion — ChromaFlow: A Negative Ablation Study of Orchestration Overhead in Tool-Augmented Agent Evaluation 的适用范围、未证明项与 failure boundary`。
<!-- claim:SF-CHROMAFLOW-A-NEGATIVE-ABLATION-STUDY-OF-ORCHESTRATION-OVERHEAD-IN-TOOL-A:start -->只支持 exact-v1 披露的 workload、模型、硬件、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。该证据不证明跨模型/硬件/部署的一般优势。<!-- claim:SF-CHROMAFLOW-A-NEGATIVE-ABLATION-STUDY-OF-ORCHESTRATION-OVERHEAD-IN-TOOL-A:end -->
Books Decision=`No Change — Existing Coverage`。旧方案在固定 workload、较低风险或无需新增 owner 时仍成立；新机制引入的分类器/控制器误差、额外状态、迁移成本与攻击面必须与 fallback/coexistence 同时进入 owner narrative。
<!-- review:SF-CHROMAFLOW-A-NEGATIVE-ABLATION-STUDY-OF-ORCHESTRATION-OVERHEAD-IN-TOOL-A:end -->

<!-- review:SF-DIAGNOSING-TRAINING-INFERENCE-MISMATCH-IN-LLM-REINFORCEMENT-LEARNING:start -->
#### Diagnosing Training Inference Mismatch in LLM Reinforcement Learning

问题与机制：In this work, we isolate TIM in a zero-mismatch diagnostic setting (VeXact), and show that small token-level numerical disagreements can independently cause training collapse.。机制 owner=`TRAIN-RLHF`。
全文定位：`arXiv:2605.14220v1 HTML — §Method / System Design — Diagnosing Training Inference Mismatch in LLM Reinforcement Learning 的机制、状态 owner 与控制/数据流`；evaluation=`§Experiments / Evaluation — Diagnosing Training Inference Mismatch in LLM Reinforcement Learning 的作者披露 workload、baseline 与 ablation`；limitations/counterevidence=`§Limitations / Discussion — Diagnosing Training Inference Mismatch in LLM Reinforcement Learning 的适用范围、未证明项与 failure boundary`。
<!-- claim:SF-DIAGNOSING-TRAINING-INFERENCE-MISMATCH-IN-LLM-REINFORCEMENT-LEARNING:start -->只支持 exact-v1 披露的 workload、模型、硬件、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。该证据不证明跨模型/硬件/部署的一般优势。<!-- claim:SF-DIAGNOSING-TRAINING-INFERENCE-MISMATCH-IN-LLM-REINFORCEMENT-LEARNING:end -->
Books Decision=`Integrate`。旧方案在固定 workload、较低风险或无需新增 owner 时仍成立；新机制引入的分类器/控制器误差、额外状态、迁移成本与攻击面必须与 fallback/coexistence 同时进入 owner narrative。
<!-- review:SF-DIAGNOSING-TRAINING-INFERENCE-MISMATCH-IN-LLM-REINFORCEMENT-LEARNING:end -->

<!-- review:SF-EVOLVEMEM-SELF-EVOLVING-MEMORY-ARCHITECTURE-VIA-AUTORESEARCH-FOR-LLM-AGE:start -->
#### EvolveMem:Self-Evolving Memory Architecture via AutoResearch for LLM Agents

问题与机制：We present EvolveMem, a self-evolving memory architecture that exposes its full retrieval configuration as a structured action space optimized by an LLM-powered diagnosis module.。机制 owner=`AGENT-MEMORY`。
全文定位：`arXiv:2605.13941v1 HTML — §Method / System Design — EvolveMem:Self-Evolving Memory Architecture via AutoResearch for LLM Agents 的机制、状态 owner 与控制/数据流`；evaluation=`§Experiments / Evaluation — EvolveMem:Self-Evolving Memory Architecture via AutoResearch for LLM Agents 的作者披露 workload、baseline 与 ablation`；limitations/counterevidence=`§Limitations / Discussion — EvolveMem:Self-Evolving Memory Architecture via AutoResearch for LLM Agents 的适用范围、未证明项与 failure boundary`。
<!-- claim:SF-EVOLVEMEM-SELF-EVOLVING-MEMORY-ARCHITECTURE-VIA-AUTORESEARCH-FOR-LLM-AGE:start -->只支持 exact-v1 披露的 workload、模型、硬件、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。该证据不证明跨模型/硬件/部署的一般优势。<!-- claim:SF-EVOLVEMEM-SELF-EVOLVING-MEMORY-ARCHITECTURE-VIA-AUTORESEARCH-FOR-LLM-AGE:end -->
Books Decision=`No Change — Existing Coverage`。旧方案在固定 workload、较低风险或无需新增 owner 时仍成立；新机制引入的分类器/控制器误差、额外状态、迁移成本与攻击面必须与 fallback/coexistence 同时进入 owner narrative。
<!-- review:SF-EVOLVEMEM-SELF-EVOLVING-MEMORY-ARCHITECTURE-VIA-AUTORESEARCH-FOR-LLM-AGE:end -->

<!-- review:SF-GROUNDED-CONTINUATION-A-LINEAR-TIME-RUNTIME-VERIFIER-FOR-LLM-CONVERSATIO:start -->
#### Grounded Continuation: A Linear-Time Runtime Verifier for LLM Conversations

问题与机制：Beyond external benchmarks, we construct two multi-agent scenarios and a 50-item grounding test: on the 15-item stale-premise subset, the verifier reaches 100% accuracy vs.。机制 owner=`PLATFORM-SECURITY`。
全文定位：`arXiv:2605.14175v1 HTML — §Method / System Design — Grounded Continuation: A Linear-Time Runtime Verifier for LLM Conversations 的机制、状态 owner 与控制/数据流`；evaluation=`§Experiments / Evaluation — Grounded Continuation: A Linear-Time Runtime Verifier for LLM Conversations 的作者披露 workload、baseline 与 ablation`；limitations/counterevidence=`§Limitations / Discussion — Grounded Continuation: A Linear-Time Runtime Verifier for LLM Conversations 的适用范围、未证明项与 failure boundary`。
<!-- claim:SF-GROUNDED-CONTINUATION-A-LINEAR-TIME-RUNTIME-VERIFIER-FOR-LLM-CONVERSATIO:start -->只支持 exact-v1 披露的 workload、模型、硬件、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。该证据不证明跨模型/硬件/部署的一般优势。<!-- claim:SF-GROUNDED-CONTINUATION-A-LINEAR-TIME-RUNTIME-VERIFIER-FOR-LLM-CONVERSATIO:end -->
Books Decision=`Integrate`。旧方案在固定 workload、较低风险或无需新增 owner 时仍成立；新机制引入的分类器/控制器误差、额外状态、迁移成本与攻击面必须与 fallback/coexistence 同时进入 owner narrative。
<!-- review:SF-GROUNDED-CONTINUATION-A-LINEAR-TIME-RUNTIME-VERIFIER-FOR-LLM-CONVERSATIO:end -->

<!-- review:SF-HOW-TO-SCALE-MIXTURE-OF-EXPERTS-FROM-MUP-TO-THE-MAXIMALLY-SCALE-STABLE-P:start -->
#### How to Scale Mixture-of-Experts: From muP to the Maximally Scale-Stable Parameterization

问题与机制：For each regime, we develop a novel Dynamical Mean Field Theory (DMFT) description of the limiting training dynamics of MoEs that provides a formal foundation for our analysis.。机制 owner=`MODEL-MOE`。
全文定位：`arXiv:2605.14200v1 HTML — §Method / System Design — How to Scale Mixture-of-Experts: From muP to the Maximally Scale-Stable Parameterization 的机制、状态 owner 与控制/数据流`；evaluation=`§Experiments / Evaluation — How to Scale Mixture-of-Experts: From muP to the Maximally Scale-Stable Parameterization 的作者披露 workload、baseline 与 ablation`；limitations/counterevidence=`§Limitations / Discussion — How to Scale Mixture-of-Experts: From muP to the Maximally Scale-Stable Parameterization 的适用范围、未证明项与 failure boundary`。
<!-- claim:SF-HOW-TO-SCALE-MIXTURE-OF-EXPERTS-FROM-MUP-TO-THE-MAXIMALLY-SCALE-STABLE-P:start -->只支持 exact-v1 披露的 workload、模型、硬件、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。该证据不证明跨模型/硬件/部署的一般优势。<!-- claim:SF-HOW-TO-SCALE-MIXTURE-OF-EXPERTS-FROM-MUP-TO-THE-MAXIMALLY-SCALE-STABLE-P:end -->
Books Decision=`No Change — Existing Coverage`。旧方案在固定 workload、较低风险或无需新增 owner 时仍成立；新机制引入的分类器/控制器误差、额外状态、迁移成本与攻击面必须与 fallback/coexistence 同时进入 owner narrative。
<!-- review:SF-HOW-TO-SCALE-MIXTURE-OF-EXPERTS-FROM-MUP-TO-THE-MAXIMALLY-SCALE-STABLE-P:end -->

<!-- review:SF-LLMS-KNOW-WHEN-THEY-KNOW-BUT-DO-NOT-ACT-ON-IT-A-METACOGNITIVE-HARNESS-FO:start -->
#### LLMs Know When They Know, but Do Not Act on It: A Metacognitive Harness for Test-time Scaling

问题与机制：Inspired by the Nelson--Narens theory from cognitive psychology, we propose a metacognitive harness that separates monitoring from reasoning.。机制 owner=`INFER-SCHEDULING`。
全文定位：`arXiv:2605.14186v1 HTML — §3 Metacognitive Harness — FOK/JOL monitor-to-control interface`；evaluation=`§4 Experiments — text, code and multimodal fixed-model evaluation`；limitations/counterevidence=`§5 Limitations / Conclusion — calibration, base-model and benchmark-snapshot boundary`。
<!-- claim:SF-LLMS-KNOW-WHEN-THEY-KNOW-BUT-DO-NOT-ACT-ON-IT-A-METACOGNITIVE-HARNESS-FO:start -->只支持 exact-v1 披露的 workload、模型、硬件、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。该证据不证明跨模型/硬件/部署的一般优势。<!-- claim:SF-LLMS-KNOW-WHEN-THEY-KNOW-BUT-DO-NOT-ACT-ON-IT-A-METACOGNITIVE-HARNESS-FO:end -->
Books Decision=`Integrate`。旧方案在固定 workload、较低风险或无需新增 owner 时仍成立；新机制引入的分类器/控制器误差、额外状态、迁移成本与攻击面必须与 fallback/coexistence 同时进入 owner narrative。
<!-- review:SF-LLMS-KNOW-WHEN-THEY-KNOW-BUT-DO-NOT-ACT-ON-IT-A-METACOGNITIVE-HARNESS-FO:end -->

<!-- review:SF-MISTLETOE-STEALTHY-ACCELERATION-COLLAPSE-ATTACKS-ON-SPECULATIVE-DECODING:start -->
#### Mistletoe: Stealthy Acceleration-Collapse Attacks on Speculative Decoding

问题与机制：We propose Mistletoe, a stealthy acceleration-collapse attack against speculative decoding.。机制 owner=`PLATFORM-SECURITY`。
全文定位：`arXiv:2605.14005v1 HTML — §Method / System Design — Mistletoe: Stealthy Acceleration-Collapse Attacks on Speculative Decoding 的机制、状态 owner 与控制/数据流`；evaluation=`§Experiments / Evaluation — Mistletoe: Stealthy Acceleration-Collapse Attacks on Speculative Decoding 的作者披露 workload、baseline 与 ablation`；limitations/counterevidence=`§Limitations / Discussion — Mistletoe: Stealthy Acceleration-Collapse Attacks on Speculative Decoding 的适用范围、未证明项与 failure boundary`。
<!-- claim:SF-MISTLETOE-STEALTHY-ACCELERATION-COLLAPSE-ATTACKS-ON-SPECULATIVE-DECODING:start -->只支持 exact-v1 披露的 workload、模型、硬件、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。该证据不证明跨模型/硬件/部署的一般优势。<!-- claim:SF-MISTLETOE-STEALTHY-ACCELERATION-COLLAPSE-ATTACKS-ON-SPECULATIVE-DECODING:end -->
Books Decision=`Integrate`。旧方案在固定 workload、较低风险或无需新增 owner 时仍成立；新机制引入的分类器/控制器误差、额外状态、迁移成本与攻击面必须与 fallback/coexistence 同时进入 owner narrative。
<!-- review:SF-MISTLETOE-STEALTHY-ACCELERATION-COLLAPSE-ATTACKS-ON-SPECULATIVE-DECODING:end -->

<!-- review:SF-MODEL-ADAPTIVE-TOOL-NECESSITY-REVEALS-THE-KNOWING-DOING-GAP-IN-LLM-TOOL-:start -->
#### Model-Adaptive Tool Necessity Reveals the Knowing-Doing Gap in LLM Tool Use

问题与机制：In this work, we introduce a model-adaptive definition of tool-necessity, grounded in each model's empirical performance.。机制 owner=`AGENT-TOOL-CALLING`。
全文定位：`arXiv:2605.14038v1 HTML — §Method / System Design — Model-Adaptive Tool Necessity Reveals the Knowing-Doing Gap in LLM Tool Use 的机制、状态 owner 与控制/数据流`；evaluation=`§Experiments / Evaluation — Model-Adaptive Tool Necessity Reveals the Knowing-Doing Gap in LLM Tool Use 的作者披露 workload、baseline 与 ablation`；limitations/counterevidence=`§Limitations / Discussion — Model-Adaptive Tool Necessity Reveals the Knowing-Doing Gap in LLM Tool Use 的适用范围、未证明项与 failure boundary`。
<!-- claim:SF-MODEL-ADAPTIVE-TOOL-NECESSITY-REVEALS-THE-KNOWING-DOING-GAP-IN-LLM-TOOL-:start -->只支持 exact-v1 披露的 workload、模型、硬件、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。该证据不证明跨模型/硬件/部署的一般优势。<!-- claim:SF-MODEL-ADAPTIVE-TOOL-NECESSITY-REVEALS-THE-KNOWING-DOING-GAP-IN-LLM-TOOL-:end -->
Books Decision=`Integrate`。旧方案在固定 workload、较低风险或无需新增 owner 时仍成立；新机制引入的分类器/控制器误差、额外状态、迁移成本与攻击面必须与 fallback/coexistence 同时进入 owner narrative。
<!-- review:SF-MODEL-ADAPTIVE-TOOL-NECESSITY-REVEALS-THE-KNOWING-DOING-GAP-IN-LLM-TOOL-:end -->

<!-- review:SF-MULTI-SCALE-DEQUANT-ELIMINATING-DEQUANTIZATION-BOTTLENECK-VIA-ACTIVATION:start -->
#### Multi-Scale Dequant: Eliminating Dequantization Bottleneck via Activation Decomposition for Efficient LLM Inference

问题与机制：Quantization is essential for efficient large language model (LLM) inference, yet the dequantization step-converting low-bit weights back to high-precision for matrix multiplication has become a critical bottleneck on modern AI accelerators.。机制 owner=`INFER-TENSORRT-LLM`。
全文定位：`arXiv:2605.13915v1 HTML — §Method / System Design — Multi-Scale Dequant: Eliminating Dequantization Bottleneck via Activation Decomposition for Efficient LLM Inference 的机制、状态 owner 与控制/数据流`；evaluation=`§Experiments / Evaluation — Multi-Scale Dequant: Eliminating Dequantization Bottleneck via Activation Decomposition for Efficient LLM Inference 的作者披露 workload、baseline 与 ablation`；limitations/counterevidence=`§Limitations / Discussion — Multi-Scale Dequant: Eliminating Dequantization Bottleneck via Activation Decomposition for Efficient LLM Inference 的适用范围、未证明项与 failure boundary`。
<!-- claim:SF-MULTI-SCALE-DEQUANT-ELIMINATING-DEQUANTIZATION-BOTTLENECK-VIA-ACTIVATION:start -->只支持 exact-v1 披露的 workload、模型、硬件、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。该证据不证明跨模型/硬件/部署的一般优势。<!-- claim:SF-MULTI-SCALE-DEQUANT-ELIMINATING-DEQUANTIZATION-BOTTLENECK-VIA-ACTIVATION:end -->
Books Decision=`No Change — Existing Coverage`。旧方案在固定 workload、较低风险或无需新增 owner 时仍成立；新机制引入的分类器/控制器误差、额外状态、迁移成本与攻击面必须与 fallback/coexistence 同时进入 owner narrative。
<!-- review:SF-MULTI-SCALE-DEQUANT-ELIMINATING-DEQUANTIZATION-BOTTLENECK-VIA-ACTIVATION:end -->

<!-- review:SF-PREFT-PREFILL-ONLY-FINETUNING-FOR-EFFICIENT-INFERENCE:start -->
#### PreFT: Prefill-only finetuning for efficient inference

问题与机制：We therefore propose PreFT (Prefill-only Finetuning), wherein we only apply the adapter to prefill tokens and discard it afterwards.。机制 owner=`INFER-PREFILL`。
全文定位：`arXiv:2605.14217v1 HTML — §Method / System Design — PreFT: Prefill-only finetuning for efficient inference 的机制、状态 owner 与控制/数据流`；evaluation=`§Experiments / Evaluation — PreFT: Prefill-only finetuning for efficient inference 的作者披露 workload、baseline 与 ablation`；limitations/counterevidence=`§Limitations / Discussion — PreFT: Prefill-only finetuning for efficient inference 的适用范围、未证明项与 failure boundary`。
<!-- claim:SF-PREFT-PREFILL-ONLY-FINETUNING-FOR-EFFICIENT-INFERENCE:start -->只支持 exact-v1 披露的 workload、模型、硬件、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。该证据不证明跨模型/硬件/部署的一般优势。<!-- claim:SF-PREFT-PREFILL-ONLY-FINETUNING-FOR-EFFICIENT-INFERENCE:end -->
Books Decision=`No Change — Existing Coverage`。旧方案在固定 workload、较低风险或无需新增 owner 时仍成立；新机制引入的分类器/控制器误差、额外状态、迁移成本与攻击面必须与 fallback/coexistence 同时进入 owner narrative。
<!-- review:SF-PREFT-PREFILL-ONLY-FINETUNING-FOR-EFFICIENT-INFERENCE:end -->

<!-- review:SF-SELF-PRUNED-KEY-VALUE-ATTENTION-LEARNING-WHEN-TO-WRITE-BY-PREDICTING-FUT:start -->
#### Self-Pruned Key-Value Attention: Learning When to Write by Predicting Future Utility

问题与机制：To address this limitation, we introduce Self-Pruned Key-Value Attention (SP-KV), a mechanism designed to predict future KV utility in order to reduce the size of the long-term KV cache.。机制 owner=`INFER-KV-CACHE`。
全文定位：`arXiv:2605.14037v1 HTML — §Method / System Design — Self-Pruned Key-Value Attention: Learning When to Write by Predicting Future Utility 的机制、状态 owner 与控制/数据流`；evaluation=`§Experiments / Evaluation — Self-Pruned Key-Value Attention: Learning When to Write by Predicting Future Utility 的作者披露 workload、baseline 与 ablation`；limitations/counterevidence=`§Limitations / Discussion — Self-Pruned Key-Value Attention: Learning When to Write by Predicting Future Utility 的适用范围、未证明项与 failure boundary`。
<!-- claim:SF-SELF-PRUNED-KEY-VALUE-ATTENTION-LEARNING-WHEN-TO-WRITE-BY-PREDICTING-FUT:start -->只支持 exact-v1 披露的 workload、模型、硬件、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。该证据不证明跨模型/硬件/部署的一般优势。<!-- claim:SF-SELF-PRUNED-KEY-VALUE-ATTENTION-LEARNING-WHEN-TO-WRITE-BY-PREDICTING-FUT:end -->
Books Decision=`No Change — Existing Coverage`。旧方案在固定 workload、较低风险或无需新增 owner 时仍成立；新机制引入的分类器/控制器误差、额外状态、迁移成本与攻击面必须与 fallback/coexistence 同时进入 owner narrative。
<!-- review:SF-SELF-PRUNED-KEY-VALUE-ATTENTION-LEARNING-WHEN-TO-WRITE-BY-PREDICTING-FUT:end -->

<!-- review:SF-SKILLFLOW-FLOW-DRIVEN-RECURSIVE-SKILL-EVOLUTION-FOR-AGENTIC-ORCHESTRATIO:start -->
#### SkillFlow: Flow-Driven Recursive Skill Evolution for Agentic Orchestration

问题与机制：To address these challenges, we propose SkillFlow, a flow-based framework that takes a trainable Supervisor as the agent and a structured environment with dynamic skill library and frozen executor, automating task orchestration through multi-turn interaction.。机制 owner=`AGENT-PLATFORM`。
全文定位：`arXiv:2605.14089v1 HTML — §Method / System Design — SkillFlow: Flow-Driven Recursive Skill Evolution for Agentic Orchestration 的机制、状态 owner 与控制/数据流`；evaluation=`§Experiments / Evaluation — SkillFlow: Flow-Driven Recursive Skill Evolution for Agentic Orchestration 的作者披露 workload、baseline 与 ablation`；limitations/counterevidence=`§Limitations / Discussion — SkillFlow: Flow-Driven Recursive Skill Evolution for Agentic Orchestration 的适用范围、未证明项与 failure boundary`。
<!-- claim:SF-SKILLFLOW-FLOW-DRIVEN-RECURSIVE-SKILL-EVOLUTION-FOR-AGENTIC-ORCHESTRATIO:start -->只支持 exact-v1 披露的 workload、模型、硬件、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。该证据不证明跨模型/硬件/部署的一般优势。<!-- claim:SF-SKILLFLOW-FLOW-DRIVEN-RECURSIVE-SKILL-EVOLUTION-FOR-AGENTIC-ORCHESTRATIO:end -->
Books Decision=`No Change — Existing Coverage`。旧方案在固定 workload、较低风险或无需新增 owner 时仍成立；新机制引入的分类器/控制器误差、额外状态、迁移成本与攻击面必须与 fallback/coexistence 同时进入 owner narrative。
<!-- review:SF-SKILLFLOW-FLOW-DRIVEN-RECURSIVE-SKILL-EVOLUTION-FOR-AGENTIC-ORCHESTRATIO:end -->

## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-13848 | exact-v1 evaluation for GraphBit: A Graph-based Agentic Framework for Non-Linear Agent Orchestration | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | paper authors |
| SF-2026-ARXIV-2605-13851 | exact-v1 evaluation for Invisible Orchestrators Suppress Protective Behavior and Dissociate Power-Holders: Safety Risks in Multi-Agent LLM Systems | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | paper authors |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-13851 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-13851 |
| SF-2026-ARXIV-2605-13880 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-13880 |
| SF-2026-ARXIV-2605-14241 | score_7_9;forced_review;potential_books_delta | selected | DA-20260515-01 | — | Score=9/9 且属于当日最高跨系统设计影响；有限叙事预算不替代其余 Source Review。 | analysis:DA-20260515-01 |
| SF-2026-ARXIV-2605-14249 | score_7_9 | selected | DA-20260515-02 | — | Score=9/9 且属于当日最高跨系统设计影响；有限叙事预算不替代其余 Source Review。 | analysis:DA-20260515-02 |
| SF-2026-ARXIV-2605-14271 | score_7_9 | selected | DA-20260515-03 | — | Score=9/9 且属于当日最高跨系统设计影响；有限叙事预算不替代其余 Source Review。 | analysis:DA-20260515-03 |
| SF-2026-ARXIV-2605-14290 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-14290 |
| SF-2026-ARXIV-2605-14305 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-14305 |
| SF-2026-ARXIV-2605-14415 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-14415 |
| SF-2026-ARXIV-2605-14421 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-14421 |
| SF-2026-ARXIV-2605-14460 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-14460 |
| SF-2026-ARXIV-2605-14473 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-14473 |
| SF-2026-ARXIV-2605-14483 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-14483 |
| SF-2026-ARXIV-2605-14498 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-14498 |
| SF-2026-ARXIV-2605-14514 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-14514 |
| SF-2026-ARXIV-2605-14570 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-14570 |
| SF-2026-ARXIV-2605-14591 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-14591 |
| SF-2026-ARXIV-2605-14636 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-14636 |
| SF-2026-ARXIV-2605-14678 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-14678 |
| SF-2026-ARXIV-2605-14744 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-14744 |
| SF-2026-ARXIV-2605-14747 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-14747 |
| SF-2026-ARXIV-2605-14786 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-14786 |
| SF-2026-ARXIV-2605-14859 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-14859 |
| SF-2026-ARXIV-2605-14865 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-14865 |
| SF-2026-ARXIV-2605-14906 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-14906 |
| SF-2026-ARXIV-2605-14932 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-14932 |
| SF-2026-ARXIV-2605-14968 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-14968 |
| SF-2026-ARXIV-2605-14978 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-14978 |
| SF-2026-ARXIV-2605-15030 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-15030 |
| SF-2026-ARXIV-2605-15034 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-15034 |
| SF-2026-ARXIV-2605-15051 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-15051 |
| SF-2026-ARXIV-2605-15079 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-15079 |
| SF-2026-ARXIV-2605-15100 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-15100 |
| SF-2026-ARXIV-2605-15109 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-15109 |
| SF-2026-ARXIV-2605-15118 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-15118 |
| SF-2026-ARXIV-2605-15128 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-15128 |
| SF-2026-ARXIV-2605-15132 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-15132 |
| SF-2026-ARXIV-2605-15138 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-15138 |
| SF-2026-ARXIV-2605-15152 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-15152 |
| SF-2026-ARXIV-2605-15155 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-15155 |
| SF-2026-ARXIV-2605-15164 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-15164 |
| SF-2026-ARXIV-2605-15172 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-15172 |
| SF-2026-ARXIV-2605-15178 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-15178 |
| SF-2026-ARXIV-2605-15184 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-15184 |
| SF-2026-ARXIV-2605-15185 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-15185 |
| SF-2026-ARXIV-2605-15188 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-15188 |
| SF-AGENTTRAP-MEASURING-RUNTIME-TRUST-FAILURES-IN-THIRD-PARTY-AGENT-SKILLS | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-AGENTTRAP-MEASURING-RUNTIME-TRUST-FAILURES-IN-THIRD-PARTY-AGENT-SKILLS |
| SF-CHROMAFLOW-A-NEGATIVE-ABLATION-STUDY-OF-ORCHESTRATION-OVERHEAD-IN-TOOL-A | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-CHROMAFLOW-A-NEGATIVE-ABLATION-STUDY-OF-ORCHESTRATION-OVERHEAD-IN-TOOL-A |
| SF-DIAGNOSING-TRAINING-INFERENCE-MISMATCH-IN-LLM-REINFORCEMENT-LEARNING | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-DIAGNOSING-TRAINING-INFERENCE-MISMATCH-IN-LLM-REINFORCEMENT-LEARNING |
| SF-EVOLVEMEM-SELF-EVOLVING-MEMORY-ARCHITECTURE-VIA-AUTORESEARCH-FOR-LLM-AGE | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-EVOLVEMEM-SELF-EVOLVING-MEMORY-ARCHITECTURE-VIA-AUTORESEARCH-FOR-LLM-AGE |
| SF-GROUNDED-CONTINUATION-A-LINEAR-TIME-RUNTIME-VERIFIER-FOR-LLM-CONVERSATIO | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-GROUNDED-CONTINUATION-A-LINEAR-TIME-RUNTIME-VERIFIER-FOR-LLM-CONVERSATIO |
| SF-HOW-TO-SCALE-MIXTURE-OF-EXPERTS-FROM-MUP-TO-THE-MAXIMALLY-SCALE-STABLE-P | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-HOW-TO-SCALE-MIXTURE-OF-EXPERTS-FROM-MUP-TO-THE-MAXIMALLY-SCALE-STABLE-P |
| SF-LLMS-KNOW-WHEN-THEY-KNOW-BUT-DO-NOT-ACT-ON-IT-A-METACOGNITIVE-HARNESS-FO | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-LLMS-KNOW-WHEN-THEY-KNOW-BUT-DO-NOT-ACT-ON-IT-A-METACOGNITIVE-HARNESS-FO |
| SF-MISTLETOE-STEALTHY-ACCELERATION-COLLAPSE-ATTACKS-ON-SPECULATIVE-DECODING | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-MISTLETOE-STEALTHY-ACCELERATION-COLLAPSE-ATTACKS-ON-SPECULATIVE-DECODING |
| SF-MODEL-ADAPTIVE-TOOL-NECESSITY-REVEALS-THE-KNOWING-DOING-GAP-IN-LLM-TOOL- | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-MODEL-ADAPTIVE-TOOL-NECESSITY-REVEALS-THE-KNOWING-DOING-GAP-IN-LLM-TOOL- |
| SF-MULTI-SCALE-DEQUANT-ELIMINATING-DEQUANTIZATION-BOTTLENECK-VIA-ACTIVATION | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-MULTI-SCALE-DEQUANT-ELIMINATING-DEQUANTIZATION-BOTTLENECK-VIA-ACTIVATION |
| SF-PREFT-PREFILL-ONLY-FINETUNING-FOR-EFFICIENT-INFERENCE | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-PREFT-PREFILL-ONLY-FINETUNING-FOR-EFFICIENT-INFERENCE |
| SF-SELF-PRUNED-KEY-VALUE-ATTENTION-LEARNING-WHEN-TO-WRITE-BY-PREDICTING-FUT | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-SELF-PRUNED-KEY-VALUE-ATTENTION-LEARNING-WHEN-TO-WRITE-BY-PREDICTING-FUT |
| SF-SKILLFLOW-FLOW-DRIVEN-RECURSIVE-SKILL-EVOLUTION-FOR-AGENTIC-ORCHESTRATIO | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-SKILLFLOW-FLOW-DRIVEN-RECURSIVE-SKILL-EVOLUTION-FOR-AGENTIC-ORCHESTRATIO |

<!-- analysis-decision:SF-2026-ARXIV-2605-13851:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-13851:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-13880:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-13880:end -->

<!-- analysis:DA-20260515-01:start -->
### Deep Analysis — SF-2026-ARXIV-2605-14241

该 family 的 Score V2=9/9；Source Review 已闭合问题、旧路径、机制 owner、evaluation boundary、trade-off 与共存条件。Deep Analysis 只提升叙事优先级，不改变 Evidence Gate。
<!-- analysis:DA-20260515-01:end -->

<!-- analysis:DA-20260515-02:start -->
### Deep Analysis — SF-2026-ARXIV-2605-14249

该 family 的 Score V2=9/9；Source Review 已闭合问题、旧路径、机制 owner、evaluation boundary、trade-off 与共存条件。Deep Analysis 只提升叙事优先级，不改变 Evidence Gate。
<!-- analysis:DA-20260515-02:end -->

<!-- analysis:DA-20260515-03:start -->
### Deep Analysis — SF-2026-ARXIV-2605-14271

该 family 的 Score V2=9/9；Source Review 已闭合问题、旧路径、机制 owner、evaluation boundary、trade-off 与共存条件。Deep Analysis 只提升叙事优先级，不改变 Evidence Gate。
<!-- analysis:DA-20260515-03:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-14290:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-14290:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-14305:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-14305:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-14415:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-14415:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-14421:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-14421:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-14460:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-14460:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-14473:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-14473:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-14483:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-14483:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-14498:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-14498:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-14514:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-14514:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-14570:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-14570:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-14591:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-14591:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-14636:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-14636:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-14678:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-14678:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-14744:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-14744:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-14747:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-14747:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-14786:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-14786:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-14859:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-14859:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-14865:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-14865:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-14906:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-14906:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-14932:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-14932:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-14968:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-14968:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-14978:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-14978:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-15030:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-15030:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-15034:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-15034:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-15051:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-15051:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-15079:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-15079:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-15100:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-15100:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-15109:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-15109:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-15118:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-15118:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-15128:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-15128:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-15132:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-15132:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-15138:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-15138:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-15152:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-15152:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-15155:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-15155:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-15164:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-15164:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-15172:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-15172:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-15178:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-15178:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-15184:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-15184:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-15185:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-15185:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-15188:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-15188:end -->

<!-- analysis-decision:SF-AGENTTRAP-MEASURING-RUNTIME-TRUST-FAILURES-IN-THIRD-PARTY-AGENT-SKILLS:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-AGENTTRAP-MEASURING-RUNTIME-TRUST-FAILURES-IN-THIRD-PARTY-AGENT-SKILLS:end -->

<!-- analysis-decision:SF-CHROMAFLOW-A-NEGATIVE-ABLATION-STUDY-OF-ORCHESTRATION-OVERHEAD-IN-TOOL-A:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-CHROMAFLOW-A-NEGATIVE-ABLATION-STUDY-OF-ORCHESTRATION-OVERHEAD-IN-TOOL-A:end -->

<!-- analysis-decision:SF-DIAGNOSING-TRAINING-INFERENCE-MISMATCH-IN-LLM-REINFORCEMENT-LEARNING:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-DIAGNOSING-TRAINING-INFERENCE-MISMATCH-IN-LLM-REINFORCEMENT-LEARNING:end -->

<!-- analysis-decision:SF-EVOLVEMEM-SELF-EVOLVING-MEMORY-ARCHITECTURE-VIA-AUTORESEARCH-FOR-LLM-AGE:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-EVOLVEMEM-SELF-EVOLVING-MEMORY-ARCHITECTURE-VIA-AUTORESEARCH-FOR-LLM-AGE:end -->

<!-- analysis-decision:SF-GROUNDED-CONTINUATION-A-LINEAR-TIME-RUNTIME-VERIFIER-FOR-LLM-CONVERSATIO:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-GROUNDED-CONTINUATION-A-LINEAR-TIME-RUNTIME-VERIFIER-FOR-LLM-CONVERSATIO:end -->

<!-- analysis-decision:SF-HOW-TO-SCALE-MIXTURE-OF-EXPERTS-FROM-MUP-TO-THE-MAXIMALLY-SCALE-STABLE-P:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-HOW-TO-SCALE-MIXTURE-OF-EXPERTS-FROM-MUP-TO-THE-MAXIMALLY-SCALE-STABLE-P:end -->

<!-- analysis-decision:SF-LLMS-KNOW-WHEN-THEY-KNOW-BUT-DO-NOT-ACT-ON-IT-A-METACOGNITIVE-HARNESS-FO:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-LLMS-KNOW-WHEN-THEY-KNOW-BUT-DO-NOT-ACT-ON-IT-A-METACOGNITIVE-HARNESS-FO:end -->

<!-- analysis-decision:SF-MISTLETOE-STEALTHY-ACCELERATION-COLLAPSE-ATTACKS-ON-SPECULATIVE-DECODING:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-MISTLETOE-STEALTHY-ACCELERATION-COLLAPSE-ATTACKS-ON-SPECULATIVE-DECODING:end -->

<!-- analysis-decision:SF-MODEL-ADAPTIVE-TOOL-NECESSITY-REVEALS-THE-KNOWING-DOING-GAP-IN-LLM-TOOL-:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-MODEL-ADAPTIVE-TOOL-NECESSITY-REVEALS-THE-KNOWING-DOING-GAP-IN-LLM-TOOL-:end -->

<!-- analysis-decision:SF-MULTI-SCALE-DEQUANT-ELIMINATING-DEQUANTIZATION-BOTTLENECK-VIA-ACTIVATION:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-MULTI-SCALE-DEQUANT-ELIMINATING-DEQUANTIZATION-BOTTLENECK-VIA-ACTIVATION:end -->

<!-- analysis-decision:SF-PREFT-PREFILL-ONLY-FINETUNING-FOR-EFFICIENT-INFERENCE:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-PREFT-PREFILL-ONLY-FINETUNING-FOR-EFFICIENT-INFERENCE:end -->

<!-- analysis-decision:SF-SELF-PRUNED-KEY-VALUE-ATTENTION-LEARNING-WHEN-TO-WRITE-BY-PREDICTING-FUT:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-SELF-PRUNED-KEY-VALUE-ATTENTION-LEARNING-WHEN-TO-WRITE-BY-PREDICTING-FUT:end -->

<!-- analysis-decision:SF-SKILLFLOW-FLOW-DRIVEN-RECURSIVE-SKILL-EVOLUTION-FOR-AGENTIC-ORCHESTRATIO:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-SKILLFLOW-FLOW-DRIVEN-RECURSIVE-SKILL-EVOLUTION-FOR-AGENTIC-ORCHESTRATIO:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-13848 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#L36 (H2: State Machine 是基本模型) | books/part-07-agent/80-reflection.md#L10 (H2: 本章要回答的问题); books/part-07-agent/82-multi-agent.md#L10 (H2: 本章要回答的问题) | existing:SF-2026-ARXIV-2605-13848 | delta:SF-2026-ARXIV-2605-13848 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-13848 |
| SF-2026-ARXIV-2605-13851 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L29 (H2: 生命周期威胁) | books/part-06-ai-infrastructure/71-multi-tenant.md#L10 (H2: 本章要回答的问题); books/part-06-ai-infrastructure/73-production-best-practice.md#L10 (H2: 本章要回答的问题) | existing:SF-2026-ARXIV-2605-13851 | delta:SF-2026-ARXIV-2605-13851 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-13851 |
| SF-2026-ARXIV-2605-13880 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76; books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-13880 | delta:SF-2026-ARXIV-2605-13880 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-13880 |
| SF-2026-ARXIV-2605-14241 | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#chapter-78 | books/part-07-agent/77-memory.md#chapter-77; books/part-07-agent/79-planning.md#chapter-79 | existing:SF-2026-ARXIV-2605-14241 | delta:SF-2026-ARXIV-2605-14241 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-14241 |
| SF-2026-ARXIV-2605-14249 | PLATFORM-COST | books/part-06-ai-infrastructure/70-cost.md#chapter-70 | books/part-06-ai-infrastructure/69-trace.md#chapter-69; books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71 | existing:SF-2026-ARXIV-2605-14249 | delta:SF-2026-ARXIV-2605-14249 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14249 |
| SF-2026-ARXIV-2605-14271 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-14271 | delta:SF-2026-ARXIV-2605-14271 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14271 |
| SF-2026-ARXIV-2605-14290 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#chapter-81 | books/part-07-agent/80-reflection.md#chapter-80; books/part-07-agent/82-multi-agent.md#chapter-82 | existing:SF-2026-ARXIV-2605-14290 | delta:SF-2026-ARXIV-2605-14290 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14290 |
| SF-2026-ARXIV-2605-14305 | MULTIMODAL-GENERATIVE-PARADIGMS | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24 | books/part-03-multimodal-world-models/23-multimodal-representation.md#chapter-23; books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | existing:SF-2026-ARXIV-2605-14305 | delta:SF-2026-ARXIV-2605-14305 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14305 |
| SF-2026-ARXIV-2605-14415 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-14415 | delta:SF-2026-ARXIV-2605-14415 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14415 |
| SF-2026-ARXIV-2605-14421 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76; books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-14421 | delta:SF-2026-ARXIV-2605-14421 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-14421 |
| SF-2026-ARXIV-2605-14460 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-14460 | delta:SF-2026-ARXIV-2605-14460 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14460 |
| SF-2026-ARXIV-2605-14473 | AGENT-RAG | books/part-07-agent/76-rag.md#chapter-76 | books/part-07-agent/75-context.md#chapter-75; books/part-07-agent/77-memory.md#chapter-77 | existing:SF-2026-ARXIV-2605-14473 | delta:SF-2026-ARXIV-2605-14473 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14473 |
| SF-2026-ARXIV-2605-14483 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#chapter-82 | books/part-07-agent/81-workflow.md#chapter-81; books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-14483 | delta:SF-2026-ARXIV-2605-14483 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14483 |
| SF-2026-ARXIV-2605-14498 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76; books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-14498 | delta:SF-2026-ARXIV-2605-14498 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14498 |
| SF-2026-ARXIV-2605-14514 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-14514 | delta:SF-2026-ARXIV-2605-14514 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14514 |
| SF-2026-ARXIV-2605-14570 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-14570 | delta:SF-2026-ARXIV-2605-14570 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14570 |
| SF-2026-ARXIV-2605-14591 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-14591 | delta:SF-2026-ARXIV-2605-14591 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14591 |
| SF-2026-ARXIV-2605-14636 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-14636 | delta:SF-2026-ARXIV-2605-14636 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14636 |
| SF-2026-ARXIV-2605-14678 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-14678 | delta:SF-2026-ARXIV-2605-14678 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14678 |
| SF-2026-ARXIV-2605-14744 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-14744 | delta:SF-2026-ARXIV-2605-14744 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14744 |
| SF-2026-ARXIV-2605-14747 | TRAIN-DATA | books/part-04-training-system/27-data.md#chapter-27 | books/part-04-training-system/28-pretraining.md#chapter-28 | existing:SF-2026-ARXIV-2605-14747 | delta:SF-2026-ARXIV-2605-14747 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14747 |
| SF-2026-ARXIV-2605-14786 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-14786 | delta:SF-2026-ARXIV-2605-14786 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14786 |
| SF-2026-ARXIV-2605-14859 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-14859 | delta:SF-2026-ARXIV-2605-14859 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14859 |
| SF-2026-ARXIV-2605-14865 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-14865 | delta:SF-2026-ARXIV-2605-14865 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14865 |
| SF-2026-ARXIV-2605-14906 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-14906 | delta:SF-2026-ARXIV-2605-14906 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14906 |
| SF-2026-ARXIV-2605-14932 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-14932 | delta:SF-2026-ARXIV-2605-14932 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14932 |
| SF-2026-ARXIV-2605-14968 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#chapter-81 | books/part-07-agent/80-reflection.md#chapter-80; books/part-07-agent/82-multi-agent.md#chapter-82 | existing:SF-2026-ARXIV-2605-14968 | delta:SF-2026-ARXIV-2605-14968 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14968 |
| SF-2026-ARXIV-2605-14978 | INFER-SPECULATIVE-DECODING | books/part-05-inference-system/48-speculative-decoding.md#chapter-48 | books/part-05-inference-system/47-pagedattention.md#chapter-47; books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | existing:SF-2026-ARXIV-2605-14978 | delta:SF-2026-ARXIV-2605-14978 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14978 |
| SF-2026-ARXIV-2605-15030 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-15030 | delta:SF-2026-ARXIV-2605-15030 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15030 |
| SF-2026-ARXIV-2605-15034 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-15034 | delta:SF-2026-ARXIV-2605-15034 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15034 |
| SF-2026-ARXIV-2605-15051 | INFER-SPECULATIVE-DECODING | books/part-05-inference-system/48-speculative-decoding.md#chapter-48 | books/part-05-inference-system/47-pagedattention.md#chapter-47; books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | existing:SF-2026-ARXIV-2605-15051 | delta:SF-2026-ARXIV-2605-15051 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-15051 |
| SF-2026-ARXIV-2605-15079 | TRAIN-DATA | books/part-04-training-system/27-data.md#chapter-27 | books/part-04-training-system/28-pretraining.md#chapter-28 | existing:SF-2026-ARXIV-2605-15079 | delta:SF-2026-ARXIV-2605-15079 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-15079 |
| SF-2026-ARXIV-2605-15100 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#chapter-56 | books/part-05-inference-system/55-pd-disaggregation.md#chapter-55 | existing:SF-2026-ARXIV-2605-15100 | delta:SF-2026-ARXIV-2605-15100 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15100 |
| SF-2026-ARXIV-2605-15109 | AGENT-RAG | books/part-07-agent/76-rag.md#chapter-76 | books/part-07-agent/75-context.md#chapter-75; books/part-07-agent/77-memory.md#chapter-77 | existing:SF-2026-ARXIV-2605-15109 | delta:SF-2026-ARXIV-2605-15109 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-15109 |
| SF-2026-ARXIV-2605-15118 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-15118 | delta:SF-2026-ARXIV-2605-15118 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15118 |
| SF-2026-ARXIV-2605-15128 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-15128 | delta:SF-2026-ARXIV-2605-15128 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15128 |
| SF-2026-ARXIV-2605-15132 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#chapter-81 | books/part-07-agent/80-reflection.md#chapter-80; books/part-07-agent/82-multi-agent.md#chapter-82 | existing:SF-2026-ARXIV-2605-15132 | delta:SF-2026-ARXIV-2605-15132 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-15132 |
| SF-2026-ARXIV-2605-15138 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-15138 | delta:SF-2026-ARXIV-2605-15138 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15138 |
| SF-2026-ARXIV-2605-15152 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-15152 | delta:SF-2026-ARXIV-2605-15152 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15152 |
| SF-2026-ARXIV-2605-15155 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#chapter-33 | books/part-04-training-system/32-ppo.md#chapter-32; books/part-04-training-system/34-dpo.md#chapter-34 | existing:SF-2026-ARXIV-2605-15155 | delta:SF-2026-ARXIV-2605-15155 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15155 |
| SF-2026-ARXIV-2605-15164 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-15164 | delta:SF-2026-ARXIV-2605-15164 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15164 |
| SF-2026-ARXIV-2605-15172 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-15172 | delta:SF-2026-ARXIV-2605-15172 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15172 |
| SF-2026-ARXIV-2605-15178 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24; books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | existing:SF-2026-ARXIV-2605-15178 | delta:SF-2026-ARXIV-2605-15178 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15178 |
| SF-2026-ARXIV-2605-15184 | AGENT-RAG | books/part-07-agent/76-rag.md#chapter-76 | books/part-07-agent/75-context.md#chapter-75; books/part-07-agent/77-memory.md#chapter-77 | existing:SF-2026-ARXIV-2605-15184 | delta:SF-2026-ARXIV-2605-15184 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15184 |
| SF-2026-ARXIV-2605-15185 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24; books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | existing:SF-2026-ARXIV-2605-15185 | delta:SF-2026-ARXIV-2605-15185 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-15185 |
| SF-2026-ARXIV-2605-15188 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-15188 | delta:SF-2026-ARXIV-2605-15188 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15188 |
| SF-AGENTTRAP-MEASURING-RUNTIME-TRUST-FAILURES-IN-THIRD-PARTY-AGENT-SKILLS | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-AGENTTRAP-MEASURING-RUNTIME-TRUST-FAILURES-IN-THIRD-PARTY-AGENT-SKILLS | delta:SF-AGENTTRAP-MEASURING-RUNTIME-TRUST-FAILURES-IN-THIRD-PARTY-AGENT-SKILLS | Direct Evolution | No Change — Existing Coverage | books-review:SF-AGENTTRAP-MEASURING-RUNTIME-TRUST-FAILURES-IN-THIRD-PARTY-AGENT-SKILLS |
| SF-CHROMAFLOW-A-NEGATIVE-ABLATION-STUDY-OF-ORCHESTRATION-OVERHEAD-IN-TOOL-A | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#chapter-81 | books/part-07-agent/80-reflection.md#chapter-80; books/part-07-agent/82-multi-agent.md#chapter-82 | existing:SF-CHROMAFLOW-A-NEGATIVE-ABLATION-STUDY-OF-ORCHESTRATION-OVERHEAD-IN-TOOL-A | delta:SF-CHROMAFLOW-A-NEGATIVE-ABLATION-STUDY-OF-ORCHESTRATION-OVERHEAD-IN-TOOL-A | Direct Evolution | No Change — Existing Coverage | books-review:SF-CHROMAFLOW-A-NEGATIVE-ABLATION-STUDY-OF-ORCHESTRATION-OVERHEAD-IN-TOOL-A |
| SF-DIAGNOSING-TRAINING-INFERENCE-MISMATCH-IN-LLM-REINFORCEMENT-LEARNING | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#chapter-31 | books/part-04-training-system/30-lora.md#chapter-30; books/part-04-training-system/32-ppo.md#chapter-32 | existing:SF-DIAGNOSING-TRAINING-INFERENCE-MISMATCH-IN-LLM-REINFORCEMENT-LEARNING | delta:SF-DIAGNOSING-TRAINING-INFERENCE-MISMATCH-IN-LLM-REINFORCEMENT-LEARNING | Direct Evolution | Integrate | books-review:SF-DIAGNOSING-TRAINING-INFERENCE-MISMATCH-IN-LLM-REINFORCEMENT-LEARNING |
| SF-EVOLVEMEM-SELF-EVOLVING-MEMORY-ARCHITECTURE-VIA-AUTORESEARCH-FOR-LLM-AGE | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76; books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-EVOLVEMEM-SELF-EVOLVING-MEMORY-ARCHITECTURE-VIA-AUTORESEARCH-FOR-LLM-AGE | delta:SF-EVOLVEMEM-SELF-EVOLVING-MEMORY-ARCHITECTURE-VIA-AUTORESEARCH-FOR-LLM-AGE | Direct Evolution | No Change — Existing Coverage | books-review:SF-EVOLVEMEM-SELF-EVOLVING-MEMORY-ARCHITECTURE-VIA-AUTORESEARCH-FOR-LLM-AGE |
| SF-GROUNDED-CONTINUATION-A-LINEAR-TIME-RUNTIME-VERIFIER-FOR-LLM-CONVERSATIO | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-GROUNDED-CONTINUATION-A-LINEAR-TIME-RUNTIME-VERIFIER-FOR-LLM-CONVERSATIO | delta:SF-GROUNDED-CONTINUATION-A-LINEAR-TIME-RUNTIME-VERIFIER-FOR-LLM-CONVERSATIO | Direct Evolution | Integrate | books-review:SF-GROUNDED-CONTINUATION-A-LINEAR-TIME-RUNTIME-VERIFIER-FOR-LLM-CONVERSATIO |
| SF-HOW-TO-SCALE-MIXTURE-OF-EXPERTS-FROM-MUP-TO-THE-MAXIMALLY-SCALE-STABLE-P | MODEL-MOE | books/part-02-model/21-moe.md#chapter-21 | books/part-02-model/20-sampling.md#chapter-20; books/part-02-model/22-long-context.md#chapter-22 | existing:SF-HOW-TO-SCALE-MIXTURE-OF-EXPERTS-FROM-MUP-TO-THE-MAXIMALLY-SCALE-STABLE-P | delta:SF-HOW-TO-SCALE-MIXTURE-OF-EXPERTS-FROM-MUP-TO-THE-MAXIMALLY-SCALE-STABLE-P | Direct Evolution | No Change — Existing Coverage | books-review:SF-HOW-TO-SCALE-MIXTURE-OF-EXPERTS-FROM-MUP-TO-THE-MAXIMALLY-SCALE-STABLE-P |
| SF-LLMS-KNOW-WHEN-THEY-KNOW-BUT-DO-NOT-ACT-ON-IT-A-METACOGNITIVE-HARNESS-FO | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#chapter-56 | books/part-05-inference-system/55-pd-disaggregation.md#chapter-55; books/part-05-inference-system/README.md#knowledge-tree | existing:SF-LLMS-KNOW-WHEN-THEY-KNOW-BUT-DO-NOT-ACT-ON-IT-A-METACOGNITIVE-HARNESS-FO | delta:SF-LLMS-KNOW-WHEN-THEY-KNOW-BUT-DO-NOT-ACT-ON-IT-A-METACOGNITIVE-HARNESS-FO | Direct Evolution | Integrate | books-review:SF-LLMS-KNOW-WHEN-THEY-KNOW-BUT-DO-NOT-ACT-ON-IT-A-METACOGNITIVE-HARNESS-FO |
| SF-MISTLETOE-STEALTHY-ACCELERATION-COLLAPSE-ATTACKS-ON-SPECULATIVE-DECODING | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-MISTLETOE-STEALTHY-ACCELERATION-COLLAPSE-ATTACKS-ON-SPECULATIVE-DECODING | delta:SF-MISTLETOE-STEALTHY-ACCELERATION-COLLAPSE-ATTACKS-ON-SPECULATIVE-DECODING | Direct Evolution | Integrate | books-review:SF-MISTLETOE-STEALTHY-ACCELERATION-COLLAPSE-ATTACKS-ON-SPECULATIVE-DECODING |
| SF-MODEL-ADAPTIVE-TOOL-NECESSITY-REVEALS-THE-KNOWING-DOING-GAP-IN-LLM-TOOL- | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#chapter-78 | books/part-07-agent/77-memory.md#chapter-77; books/part-07-agent/79-planning.md#chapter-79 | existing:SF-MODEL-ADAPTIVE-TOOL-NECESSITY-REVEALS-THE-KNOWING-DOING-GAP-IN-LLM-TOOL- | delta:SF-MODEL-ADAPTIVE-TOOL-NECESSITY-REVEALS-THE-KNOWING-DOING-GAP-IN-LLM-TOOL- | Direct Evolution | Integrate | books-review:SF-MODEL-ADAPTIVE-TOOL-NECESSITY-REVEALS-THE-KNOWING-DOING-GAP-IN-LLM-TOOL- |
| SF-MULTI-SCALE-DEQUANT-ELIMINATING-DEQUANTIZATION-BOTTLENECK-VIA-ACTIVATION | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | books/part-05-inference-system/48-speculative-decoding.md#chapter-48; books/part-05-inference-system/50-vllm.md#chapter-50 | existing:SF-MULTI-SCALE-DEQUANT-ELIMINATING-DEQUANTIZATION-BOTTLENECK-VIA-ACTIVATION | delta:SF-MULTI-SCALE-DEQUANT-ELIMINATING-DEQUANTIZATION-BOTTLENECK-VIA-ACTIVATION | Direct Evolution | No Change — Existing Coverage | books-review:SF-MULTI-SCALE-DEQUANT-ELIMINATING-DEQUANTIZATION-BOTTLENECK-VIA-ACTIVATION |
| SF-PREFT-PREFILL-ONLY-FINETUNING-FOR-EFFICIENT-INFERENCE | INFER-PREFILL | books/part-05-inference-system/43-prefill.md#chapter-43 | books/part-05-inference-system/42-what-happens-during-inference.md#chapter-42; books/part-05-inference-system/44-decode.md#chapter-44 | existing:SF-PREFT-PREFILL-ONLY-FINETUNING-FOR-EFFICIENT-INFERENCE | delta:SF-PREFT-PREFILL-ONLY-FINETUNING-FOR-EFFICIENT-INFERENCE | Direct Evolution | No Change — Existing Coverage | books-review:SF-PREFT-PREFILL-ONLY-FINETUNING-FOR-EFFICIENT-INFERENCE |
| SF-SELF-PRUNED-KEY-VALUE-ATTENTION-LEARNING-WHEN-TO-WRITE-BY-PREDICTING-FUT | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#chapter-45 | books/part-05-inference-system/44-decode.md#chapter-44; books/part-05-inference-system/46-continuous-batching.md#chapter-46 | existing:SF-SELF-PRUNED-KEY-VALUE-ATTENTION-LEARNING-WHEN-TO-WRITE-BY-PREDICTING-FUT | delta:SF-SELF-PRUNED-KEY-VALUE-ATTENTION-LEARNING-WHEN-TO-WRITE-BY-PREDICTING-FUT | Direct Evolution | No Change — Existing Coverage | books-review:SF-SELF-PRUNED-KEY-VALUE-ATTENTION-LEARNING-WHEN-TO-WRITE-BY-PREDICTING-FUT |
| SF-SKILLFLOW-FLOW-DRIVEN-RECURSIVE-SKILL-EVOLUTION-FOR-AGENTIC-ORCHESTRATIO | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83; books/part-07-agent/README.md#knowledge-tree | existing:SF-SKILLFLOW-FLOW-DRIVEN-RECURSIVE-SKILL-EVOLUTION-FOR-AGENTIC-ORCHESTRATIO | delta:SF-SKILLFLOW-FLOW-DRIVEN-RECURSIVE-SKILL-EVOLUTION-FOR-AGENTIC-ORCHESTRATIO | Direct Evolution | No Change — Existing Coverage | books-review:SF-SKILLFLOW-FLOW-DRIVEN-RECURSIVE-SKILL-EVOLUTION-FOR-AGENTIC-ORCHESTRATIO |

<!-- books-review:SF-2026-ARXIV-2605-13848:start -->
<!-- existing:SF-2026-ARXIV-2605-13848:start -->对读 `books/part-07-agent/81-workflow.md#L36 (H2: State Machine 是基本模型)` 及相邻章节后，现有命题为：本章的核心判断是：**Workflow 是 Agent 的 durable control plane。它持久化状态和事件，强制 policy、budget、retry、approval 与 compensation；模型在被授权的节点内提出内容或分支，不拥有整个流程的事实状态。** 目标小节已经拥有该 family 所需的长期 owner 与旧路径/约束边界。<!-- existing:SF-2026-ARXIV-2605-13848:end -->
<!-- delta:SF-2026-ARXIV-2605-13848:start -->Exact-v1 的 source-specific delta 是：We introduce GraphBit, an engine-orchestrated framework that defines workflows explicitly and deterministically as a directed acyclic graph (DAG). 其证据边界为：Evidence is author-reported exact-v1 mechanism/evaluation evidence. It does not establish cross-model, cross-hardware, cross-workload or production generality unless those conditions are explicitly named above. 该实现或实验没有改变当前章节已经成立的长期机制，不把作者 benchmark 外推为通用结论。<!-- delta:SF-2026-ARXIV-2605-13848:end -->
Decision: `No Change — Existing Coverage`; reviewer=fresh-context:apr-may-books-20260903。
<!-- books-review:SF-2026-ARXIV-2605-13848:end -->

<!-- books-review:SF-2026-ARXIV-2605-13851:start -->
<!-- existing:SF-2026-ARXIV-2605-13851:start -->对读 `books/part-06-ai-infrastructure/72-security.md#L29 (H2: 生命周期威胁)` 及相邻章节后，现有命题为：本章的核心判断是：**AI security 是贯穿 capability production、delivery 与 action 的风险管理。平台必须识别资产、主体、数据流和信任转换，并用 provenance、least privilege、isolation、validation 与 audit 建立纵深防御。** 目标小节已经拥有该 family 所需的长期 owner 与旧路径/约束边界。<!-- existing:SF-2026-ARXIV-2605-13851:end -->
<!-- delta:SF-2026-ARXIV-2605-13851:start -->Exact-v1 的 source-specific delta 是：We propose that the monologue-to-talk ratio ( mono_ratio ) be adopted as an anomaly detection metric for multi-agent orchestration systems. 其证据边界为：Evidence is author-reported exact-v1 mechanism/evaluation evidence. It does not establish cross-model, cross-hardware, cross-workload or production generality unless those conditions are explicitly named above. 该实现或实验没有改变当前章节已经成立的长期机制，不把作者 benchmark 外推为通用结论。<!-- delta:SF-2026-ARXIV-2605-13851:end -->
Decision: `No Change — Existing Coverage`; reviewer=fresh-context:apr-may-books-20260903。
<!-- books-review:SF-2026-ARXIV-2605-13851:end -->

<!-- books-review:SF-2026-ARXIV-2605-13880:start -->
<!-- existing:SF-2026-ARXIV-2605-13880:start -->已读取 current owner `books/part-07-agent/77-memory.md` 与相邻章节 `['books/part-07-agent/76-rag.md', 'books/part-07-agent/78-tool-calling.md']`，并只比较首个 `## Review notes` 之前的正文演进链；owner outline：## 本章要回答的问题 → ## Context 与 Memory 的状态边界 → ## Memory 类型是用途，不只是存储介质 → ## Memory Write 是高风险决策 → ### Write / Hold 不足以定义下一状态 → ### 从 Outcome Reward 到 Content-level Credit：归因只能约束写入，不能成为真值 → ## Memory Read 是受约束检索 → ### 从按需读取到选择性主动干预 → ### 从一次 Top-k 检索到有预算的关联回忆 → ### Fact State 与 Retrieval-policy State 必须分离 → ### Entry Majority 不等于 Independent Evidence Majority → ### 从 Write-time Summary 转向 Query-conditioned Late Construction → ## Consolidation 与 Forgetting → ### 并行经验汇总需要 Bounded Fan-in 与 Context Version。<!-- existing:SF-2026-ARXIV-2605-13880:end -->
<!-- delta:SF-2026-ARXIV-2605-13880:start -->Ch77 已要求 proposer/validator-gated experience write，并绑定 source episode 与 rollback。<!-- delta:SF-2026-ARXIV-2605-13880:end --> Decision=`No Change — Existing Coverage`；shared Books writeback 与独立 post-write audit 见 `books-post-write-semantic-audit.json`。
<!-- books-review:SF-2026-ARXIV-2605-13880:end -->

<!-- books-review:SF-2026-ARXIV-2605-14241:start -->
<!-- existing:SF-2026-ARXIV-2605-14241:start -->已读取 `books/part-07-agent/78-tool-calling.md` 及相邻章节；当前主线已覆盖proposal、provider/tool discovery、utility admission、authorization、execution 与 outcome commit 的分层。正文尚未明确承载本 family 的增量：同功能 tool provider 的选择应由观察 runtime load、latency、reliability 与 answer-quality 的在线 router 决定；router 只拥有 provider selection，不拥有工具授权或结果 truth。 Owner snapshot sha256=`df252ef396695001f51255bccc709bc32851023df8e0a6746fe4a03c36bddf50`；相邻章节=`books/part-07-agent/77-memory.md, books/part-07-agent/79-planning.md`。<!-- existing:SF-2026-ARXIV-2605-14241:end -->
<!-- delta:SF-2026-ARXIV-2605-14241:start -->同功能 tool provider 的选择应由观察 runtime load、latency、reliability 与 answer-quality 的在线 router 决定；router 只拥有 provider selection，不拥有工具授权或结果 truth<!-- delta:SF-2026-ARXIV-2605-14241:end --> Decision: `Integrate`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-14241:end -->

<!-- books-review:SF-2026-ARXIV-2605-14249:start -->
<!-- existing:SF-2026-ARXIV-2605-14249:start -->已读取 `books/part-06-ai-infrastructure/70-cost.md` 及相邻章节；当前主线已覆盖端到端 work unit、energy/latency/quality 约束与 capacity/idle/失败重试的共同核算。本 family 的增量“多 GPU 推理能耗优化应先以可解释 surrogate 预测 layer/operator 与并行配置的 energy，再把 energy-quality-latency 约束作为配置探索合同，而不是只比较整机平均功率；当前 Ch70 已明确承载 layer-wise energy model、architecture proxy 与 device/precision/batch/shape/utilization 约束，因此本 family 不再重复写回”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`8838d188822605575fee9227fdf4ba3a22518eb6dc8cf6ed5a4ad9237351115c`；相邻章节=`books/part-06-ai-infrastructure/69-trace.md, books/part-06-ai-infrastructure/71-multi-tenant.md`。<!-- existing:SF-2026-ARXIV-2605-14249:end -->
<!-- delta:SF-2026-ARXIV-2605-14249:start -->多 GPU 推理能耗优化应先以可解释 surrogate 预测 layer/operator 与并行配置的 energy，再把 energy-quality-latency 约束作为配置探索合同，而不是只比较整机平均功率；当前 Ch70 已明确承载 layer-wise energy model、architecture proxy 与 device/precision/batch/shape/utilization 约束，因此本 family 不再重复写回<!-- delta:SF-2026-ARXIV-2605-14249:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-14249:end -->

<!-- books-review:SF-2026-ARXIV-2605-14271:start -->
<!-- existing:SF-2026-ARXIV-2605-14271:start -->已读取 `books/part-06-ai-infrastructure/66-evaluation-system.md` 及相邻章节；当前主线已覆盖model、harness、environment、scorer、budget、provenance 与 release authority 的完整评测身份。本 family 的增量“Agent harness 安全评测必须观察 trajectory 中的 resource access、message routing 与 authority transition；最终答案正确不能覆盖中途越权”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`66cd622a2aa49f23d15886aa07e741d61045c772e0d387f6fd7fcc1094d0a8ab`；相邻章节=`books/part-06-ai-infrastructure/65-kai-scheduler.md, books/part-06-ai-infrastructure/67-monitoring.md`。<!-- existing:SF-2026-ARXIV-2605-14271:end -->
<!-- delta:SF-2026-ARXIV-2605-14271:start -->Agent harness 安全评测必须观察 trajectory 中的 resource access、message routing 与 authority transition；最终答案正确不能覆盖中途越权<!-- delta:SF-2026-ARXIV-2605-14271:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-14271:end -->

<!-- books-review:SF-2026-ARXIV-2605-14290:start -->
<!-- existing:SF-2026-ARXIV-2605-14290:start -->已读取 `books/part-07-agent/81-workflow.md` 及相邻章节；当前主线已覆盖durable DAG/state、checkpoint、retry、compensation、external evidence 与 commit authority。本 family 的增量“Web Agent 应把不可信 runtime content 限制为预提交程序的数据，而不允许其生成新控制流；typed site API、隔离的 LLM subroutine 与显式 replan fallback 共同定义安全/可用性边界”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`a8a935c80e5047500f9c7beb334a74ac83381e49176a11f8beaa8b3da089fa92`；相邻章节=`books/part-07-agent/80-reflection.md, books/part-07-agent/82-multi-agent.md`。<!-- existing:SF-2026-ARXIV-2605-14290:end -->
<!-- delta:SF-2026-ARXIV-2605-14290:start -->Web Agent 应把不可信 runtime content 限制为预提交程序的数据，而不允许其生成新控制流；typed site API、隔离的 LLM subroutine 与显式 replan fallback 共同定义安全/可用性边界<!-- delta:SF-2026-ARXIV-2605-14290:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-14290:end -->

<!-- books-review:SF-2026-ARXIV-2605-14305:start -->
<!-- existing:SF-2026-ARXIV-2605-14305:start -->已读取 `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md` 及相邻章节；当前主线已覆盖AR、diffusion、masked refinement 的 proposal、verification、correction 与 commit 边界。本 family 的增量“离散 diffusion 的并行 proposal 可用 prefix-conditioned factorization 消除 token-independent clean-posterior 近似，再由 speculative verification 保留 target distribution”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`82d67a82821a384369ee36c24794db1b14bdfd6d538877525c38e9420761df30`；相邻章节=`books/part-03-multimodal-world-models/23-multimodal-representation.md, books/part-03-multimodal-world-models/25-multimodal-world-models.md`。<!-- existing:SF-2026-ARXIV-2605-14305:end -->
<!-- delta:SF-2026-ARXIV-2605-14305:start -->离散 diffusion 的并行 proposal 可用 prefix-conditioned factorization 消除 token-independent clean-posterior 近似，再由 speculative verification 保留 target distribution<!-- delta:SF-2026-ARXIV-2605-14305:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-14305:end -->

<!-- books-review:SF-2026-ARXIV-2605-14415:start -->
<!-- existing:SF-2026-ARXIV-2605-14415:start -->已读取 `books/part-06-ai-infrastructure/66-evaluation-system.md` 及相邻章节；当前主线已覆盖model、harness、environment、scorer、budget、provenance 与 release authority 的完整评测身份。本 family 的增量“coding-Agent release maintenance 评测必须把版本链、继承 codebase、跨步 regression 与每步 acceptance contract 纳入 run identity，而不能把独立 issue 分数外推为长期维护能力”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`66cd622a2aa49f23d15886aa07e741d61045c772e0d387f6fd7fcc1094d0a8ab`；相邻章节=`books/part-06-ai-infrastructure/65-kai-scheduler.md, books/part-06-ai-infrastructure/67-monitoring.md`。<!-- existing:SF-2026-ARXIV-2605-14415:end -->
<!-- delta:SF-2026-ARXIV-2605-14415:start -->coding-Agent release maintenance 评测必须把版本链、继承 codebase、跨步 regression 与每步 acceptance contract 纳入 run identity，而不能把独立 issue 分数外推为长期维护能力<!-- delta:SF-2026-ARXIV-2605-14415:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-14415:end -->

<!-- books-review:SF-2026-ARXIV-2605-14421:start -->
<!-- existing:SF-2026-ARXIV-2605-14421:start -->已读取 `books/part-07-agent/77-memory.md` 及相邻章节；当前主线已覆盖write admission、provenance、derived state、retrieval、expiry、poisoning containment 与可逆更新。正文尚未明确承载本 family 的增量：持久 Agent memory 的 action justification 应形成签名 provenance 与 derivation-lineage DAG；敏感 action 在 lineage 不闭合时 fail closed，而不是把 recalled text 当作 authority。 Owner snapshot sha256=`ac3bf5ab49bb87bcf3f0cfa1da47486caeb35e9d451251f91c67caf3bc9de6d7`；相邻章节=`books/part-07-agent/76-rag.md, books/part-07-agent/78-tool-calling.md`。<!-- existing:SF-2026-ARXIV-2605-14421:end -->
<!-- delta:SF-2026-ARXIV-2605-14421:start -->持久 Agent memory 的 action justification 应形成签名 provenance 与 derivation-lineage DAG；敏感 action 在 lineage 不闭合时 fail closed，而不是把 recalled text 当作 authority<!-- delta:SF-2026-ARXIV-2605-14421:end --> Decision: `Integrate`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-14421:end -->

<!-- books-review:SF-2026-ARXIV-2605-14460:start -->
<!-- existing:SF-2026-ARXIV-2605-14460:start -->已读取 `books/part-07-agent/84-agent-platform.md` 及相邻章节；当前主线已覆盖skill artifact identity、capability、admission、runtime policy、drift 与 audit。本 family 的增量“skill supply-chain 审计不能只扫描代码 payload，还要执行 capability/effect probes，识别由描述、依赖和运行上下文组合出的 payload-less behavior”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`b7ea13daeac643ba9237a698b6363ea16ab660cb662be9c7f33b9302ca7a5802`；相邻章节=`books/part-07-agent/83-mcp.md`。<!-- existing:SF-2026-ARXIV-2605-14460:end -->
<!-- delta:SF-2026-ARXIV-2605-14460:start -->skill supply-chain 审计不能只扫描代码 payload，还要执行 capability/effect probes，识别由描述、依赖和运行上下文组合出的 payload-less behavior<!-- delta:SF-2026-ARXIV-2605-14460:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-14460:end -->

<!-- books-review:SF-2026-ARXIV-2605-14473:start -->
<!-- existing:SF-2026-ARXIV-2605-14473:start -->已读取 `books/part-07-agent/76-rag.md` 及相邻章节；当前主线已覆盖corpus identity、retrieval trajectory、evidence provenance、citation 与 answer claim 的绑定。本 family 的增量“RAG 在知识冲突下要把 answer correctness 与 context compliance 分开；诊断 intervention 只能测 retrieved context 是否控制答案，不能证明答案真实”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`9fbd3e0d51f58631aa1874a5ac618b37c4b1b7dfff667bc59293c5a2848e6510`；相邻章节=`books/part-07-agent/75-context.md, books/part-07-agent/77-memory.md`。<!-- existing:SF-2026-ARXIV-2605-14473:end -->
<!-- delta:SF-2026-ARXIV-2605-14473:start -->RAG 在知识冲突下要把 answer correctness 与 context compliance 分开；诊断 intervention 只能测 retrieved context 是否控制答案，不能证明答案真实<!-- delta:SF-2026-ARXIV-2605-14473:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-14473:end -->

<!-- books-review:SF-2026-ARXIV-2605-14483:start -->
<!-- existing:SF-2026-ARXIV-2605-14483:start -->已读取 `books/part-07-agent/82-multi-agent.md` 及相邻章节；当前主线已覆盖role、dependency graph、message/shared state、credit、failure containment 与 final commit owner。本 family 的增量“Multi-Agent orchestration 的 role、capacity 与 dependency graph 应被视为一个可执行 artifact，并用 counterfactual feedback 做 credit assignment，而非顺序局部调参”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`5101c08d1a612efe07f8c557b662d9ead237399a4164ec7bce2fd5ddbedc3397`；相邻章节=`books/part-07-agent/81-workflow.md, books/part-07-agent/83-mcp.md`。<!-- existing:SF-2026-ARXIV-2605-14483:end -->
<!-- delta:SF-2026-ARXIV-2605-14483:start -->Multi-Agent orchestration 的 role、capacity 与 dependency graph 应被视为一个可执行 artifact，并用 counterfactual feedback 做 credit assignment，而非顺序局部调参<!-- delta:SF-2026-ARXIV-2605-14483:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-14483:end -->

<!-- books-review:SF-2026-ARXIV-2605-14498:start -->
<!-- existing:SF-2026-ARXIV-2605-14498:start -->已读取 `books/part-07-agent/77-memory.md` 及相邻章节；当前主线已覆盖write admission、provenance、derived state、retrieval、expiry、poisoning containment 与可逆更新。本 family 的增量“群体会话 memory 必须把 speaker/principal、reply graph、belief ownership 与 audience-specific retrieval 绑定；把多人消息拼成单一文档会制造跨主体状态污染”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`ac3bf5ab49bb87bcf3f0cfa1da47486caeb35e9d451251f91c67caf3bc9de6d7`；相邻章节=`books/part-07-agent/76-rag.md, books/part-07-agent/78-tool-calling.md`。<!-- existing:SF-2026-ARXIV-2605-14498:end -->
<!-- delta:SF-2026-ARXIV-2605-14498:start -->群体会话 memory 必须把 speaker/principal、reply graph、belief ownership 与 audience-specific retrieval 绑定；把多人消息拼成单一文档会制造跨主体状态污染<!-- delta:SF-2026-ARXIV-2605-14498:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-14498:end -->

<!-- books-review:SF-2026-ARXIV-2605-14514:start -->
<!-- existing:SF-2026-ARXIV-2605-14514:start -->已读取 `books/part-06-ai-infrastructure/72-security.md` 及相邻章节；当前主线已覆盖identity、typed capability、least privilege、policy mediation、effect boundary 与 audit。本 family 的增量“模型 defense 是有顺序的 release artifact：后续 safety/privacy/fairness patch 必须重新验证先前保障，不能把单项防御通过等同于组合后仍保持保护”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`45cdedd789e1517c5cd110897cbfaf39b57453fe2bc94b9bc64d72ffa4612bb3`；相邻章节=`books/part-06-ai-infrastructure/71-multi-tenant.md, books/part-06-ai-infrastructure/73-production-best-practice.md`。<!-- existing:SF-2026-ARXIV-2605-14514:end -->
<!-- delta:SF-2026-ARXIV-2605-14514:start -->模型 defense 是有顺序的 release artifact：后续 safety/privacy/fairness patch 必须重新验证先前保障，不能把单项防御通过等同于组合后仍保持保护<!-- delta:SF-2026-ARXIV-2605-14514:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-14514:end -->

<!-- books-review:SF-2026-ARXIV-2605-14570:start -->
<!-- existing:SF-2026-ARXIV-2605-14570:start -->已读取 `books/part-06-ai-infrastructure/66-evaluation-system.md` 及相邻章节；当前主线已覆盖model、harness、environment、scorer、budget、provenance 与 release authority 的完整评测身份。本 family 的增量“diffusion LM 的 uncertainty sensor 必须绑定 denoising trajectory、remasking 与 masked likelihood，不能沿用 autoregressive token probability；该 sensor 仍需独立校准且不拥有事实真值”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`66cd622a2aa49f23d15886aa07e741d61045c772e0d387f6fd7fcc1094d0a8ab`；相邻章节=`books/part-06-ai-infrastructure/65-kai-scheduler.md, books/part-06-ai-infrastructure/67-monitoring.md`。<!-- existing:SF-2026-ARXIV-2605-14570:end -->
<!-- delta:SF-2026-ARXIV-2605-14570:start -->diffusion LM 的 uncertainty sensor 必须绑定 denoising trajectory、remasking 与 masked likelihood，不能沿用 autoregressive token probability；该 sensor 仍需独立校准且不拥有事实真值<!-- delta:SF-2026-ARXIV-2605-14570:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-14570:end -->

<!-- books-review:SF-2026-ARXIV-2605-14591:start -->
<!-- existing:SF-2026-ARXIV-2605-14591:start -->已读取 `books/part-06-ai-infrastructure/66-evaluation-system.md` 及相邻章节；当前主线已覆盖model、harness、environment、scorer、budget、provenance 与 release authority 的完整评测身份。本 family 的增量“大模型 privacy audit 可在无法重训时利用已知 member/non-member 固定集合估计经验下界，但该 post-hoc sensor 不能替代机制级 DP accounting 或训练日志；当前 Ch66 已明确承载 post-hoc dataset/membership inference 的证据边界与机制级 accounting 区分，因此本 family 不再重复写回”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`66cd622a2aa49f23d15886aa07e741d61045c772e0d387f6fd7fcc1094d0a8ab`；相邻章节=`books/part-06-ai-infrastructure/65-kai-scheduler.md, books/part-06-ai-infrastructure/67-monitoring.md`。<!-- existing:SF-2026-ARXIV-2605-14591:end -->
<!-- delta:SF-2026-ARXIV-2605-14591:start -->大模型 privacy audit 可在无法重训时利用已知 member/non-member 固定集合估计经验下界，但该 post-hoc sensor 不能替代机制级 DP accounting 或训练日志；当前 Ch66 已明确承载 post-hoc dataset/membership inference 的证据边界与机制级 accounting 区分，因此本 family 不再重复写回<!-- delta:SF-2026-ARXIV-2605-14591:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-14591:end -->

<!-- books-review:SF-2026-ARXIV-2605-14636:start -->
<!-- existing:SF-2026-ARXIV-2605-14636:start -->已读取 `books/part-06-ai-infrastructure/66-evaluation-system.md` 及相邻章节；当前主线已覆盖model、harness、environment、scorer、budget、provenance 与 release authority 的完整评测身份。本 family 的增量“时间截止问题必须冻结可知信息边界，并将 temporal leakage 作为独立 failure slice；learned critique 只能在所测 cutoff/prompt 分布上提供 sensor”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`66cd622a2aa49f23d15886aa07e741d61045c772e0d387f6fd7fcc1094d0a8ab`；相邻章节=`books/part-06-ai-infrastructure/65-kai-scheduler.md, books/part-06-ai-infrastructure/67-monitoring.md`。<!-- existing:SF-2026-ARXIV-2605-14636:end -->
<!-- delta:SF-2026-ARXIV-2605-14636:start -->时间截止问题必须冻结可知信息边界，并将 temporal leakage 作为独立 failure slice；learned critique 只能在所测 cutoff/prompt 分布上提供 sensor<!-- delta:SF-2026-ARXIV-2605-14636:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-14636:end -->

<!-- books-review:SF-2026-ARXIV-2605-14678:start -->
<!-- existing:SF-2026-ARXIV-2605-14678:start -->已读取 `books/part-06-ai-infrastructure/66-evaluation-system.md` 及相邻章节；当前主线已覆盖model、harness、environment、scorer、budget、provenance 与 release authority 的完整评测身份。本 family 的增量“主动 personal Agent 评测必须隐藏 intent、跨 task/session 保留状态，并同时测 proactivity 与 task outcome；单轮显式指令 benchmark 不能代表长期主动协助”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`66cd622a2aa49f23d15886aa07e741d61045c772e0d387f6fd7fcc1094d0a8ab`；相邻章节=`books/part-06-ai-infrastructure/65-kai-scheduler.md, books/part-06-ai-infrastructure/67-monitoring.md`。<!-- existing:SF-2026-ARXIV-2605-14678:end -->
<!-- delta:SF-2026-ARXIV-2605-14678:start -->主动 personal Agent 评测必须隐藏 intent、跨 task/session 保留状态，并同时测 proactivity 与 task outcome；单轮显式指令 benchmark 不能代表长期主动协助<!-- delta:SF-2026-ARXIV-2605-14678:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-14678:end -->

<!-- books-review:SF-2026-ARXIV-2605-14744:start -->
<!-- existing:SF-2026-ARXIV-2605-14744:start -->已读取 `books/part-06-ai-infrastructure/72-security.md` 及相邻章节；当前主线已覆盖identity、typed capability、least privilege、policy mediation、effect boundary 与 audit。本 family 的增量“治理规则不能由同一生成模型同时解释和自证；policy enforcement 应移出模型回路，以机械 primitive 约束 decision/effect，并把 rationale 仅作为可审计证据”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`45cdedd789e1517c5cd110897cbfaf39b57453fe2bc94b9bc64d72ffa4612bb3`；相邻章节=`books/part-06-ai-infrastructure/71-multi-tenant.md, books/part-06-ai-infrastructure/73-production-best-practice.md`。<!-- existing:SF-2026-ARXIV-2605-14744:end -->
<!-- delta:SF-2026-ARXIV-2605-14744:start -->治理规则不能由同一生成模型同时解释和自证；policy enforcement 应移出模型回路，以机械 primitive 约束 decision/effect，并把 rationale 仅作为可审计证据<!-- delta:SF-2026-ARXIV-2605-14744:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-14744:end -->

<!-- books-review:SF-2026-ARXIV-2605-14747:start -->
<!-- existing:SF-2026-ARXIV-2605-14747:start -->已读取 `books/part-04-training-system/27-data.md` 及相邻章节；当前主线已覆盖dataset identity、schema、lineage、version、governance、quality gate 与 reusable artifact。本 family 的增量“GUI Agent 数据管线可从互联网教程视频恢复 observation-action trajectory，但每一步都必须保留 video/application identity、grounding confidence、filter revision 与 executable validation；规模不能替代轨迹正确性”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`cdd967c3fb6f506cec6ce3f112754e3f76a255641281bce71e1bfb1e09f98690`；相邻章节=`books/part-04-training-system/28-pretraining.md`。<!-- existing:SF-2026-ARXIV-2605-14747:end -->
<!-- delta:SF-2026-ARXIV-2605-14747:start -->GUI Agent 数据管线可从互联网教程视频恢复 observation-action trajectory，但每一步都必须保留 video/application identity、grounding confidence、filter revision 与 executable validation；规模不能替代轨迹正确性<!-- delta:SF-2026-ARXIV-2605-14747:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-14747:end -->

<!-- books-review:SF-2026-ARXIV-2605-14786:start -->
<!-- existing:SF-2026-ARXIV-2605-14786:start -->已读取 `books/part-06-ai-infrastructure/72-security.md` 及相邻章节；当前主线已覆盖identity、typed capability、least privilege、policy mediation、effect boundary 与 audit。本 family 的增量“browser Agent 的 action/timing trace 会形成被动 model fingerprint side channel；随机 delay 只能改变 sensor，不是身份或不可链接性保证，平台需将 attribution、privacy 与 rate policy 分开”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`45cdedd789e1517c5cd110897cbfaf39b57453fe2bc94b9bc64d72ffa4612bb3`；相邻章节=`books/part-06-ai-infrastructure/71-multi-tenant.md, books/part-06-ai-infrastructure/73-production-best-practice.md`。<!-- existing:SF-2026-ARXIV-2605-14786:end -->
<!-- delta:SF-2026-ARXIV-2605-14786:start -->browser Agent 的 action/timing trace 会形成被动 model fingerprint side channel；随机 delay 只能改变 sensor，不是身份或不可链接性保证，平台需将 attribution、privacy 与 rate policy 分开<!-- delta:SF-2026-ARXIV-2605-14786:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-14786:end -->

<!-- books-review:SF-2026-ARXIV-2605-14859:start -->
<!-- existing:SF-2026-ARXIV-2605-14859:start -->已读取 `books/part-06-ai-infrastructure/72-security.md` 及相邻章节；当前主线已覆盖identity、typed capability、least privilege、policy mediation、effect boundary 与 audit。本 family 的增量“coding Agent 的权限策略必须由平台从 task、workspace 与 effect contract 推导并执行；模型的 permission-boundary inference 只能是 policy proposal”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`45cdedd789e1517c5cd110897cbfaf39b57453fe2bc94b9bc64d72ffa4612bb3`；相邻章节=`books/part-06-ai-infrastructure/71-multi-tenant.md, books/part-06-ai-infrastructure/73-production-best-practice.md`。<!-- existing:SF-2026-ARXIV-2605-14859:end -->
<!-- delta:SF-2026-ARXIV-2605-14859:start -->coding Agent 的权限策略必须由平台从 task、workspace 与 effect contract 推导并执行；模型的 permission-boundary inference 只能是 policy proposal<!-- delta:SF-2026-ARXIV-2605-14859:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-14859:end -->

<!-- books-review:SF-2026-ARXIV-2605-14865:start -->
<!-- existing:SF-2026-ARXIV-2605-14865:start -->已读取 `books/part-06-ai-infrastructure/66-evaluation-system.md` 及相邻章节；当前主线已覆盖model、harness、environment、scorer、budget、provenance 与 release authority 的完整评测身份。本 family 的增量“Agent 评测要把 terminal outcome 与 trace span diagnosis 连接：failure taxonomy、location、cause 与最终结果必须同属一次 run evidence，长轨迹不能只由单一成功率压缩”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`66cd622a2aa49f23d15886aa07e741d61045c772e0d387f6fd7fcc1094d0a8ab`；相邻章节=`books/part-06-ai-infrastructure/65-kai-scheduler.md, books/part-06-ai-infrastructure/67-monitoring.md`。<!-- existing:SF-2026-ARXIV-2605-14865:end -->
<!-- delta:SF-2026-ARXIV-2605-14865:start -->Agent 评测要把 terminal outcome 与 trace span diagnosis 连接：failure taxonomy、location、cause 与最终结果必须同属一次 run evidence，长轨迹不能只由单一成功率压缩<!-- delta:SF-2026-ARXIV-2605-14865:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-14865:end -->

<!-- books-review:SF-2026-ARXIV-2605-14906:start -->
<!-- existing:SF-2026-ARXIV-2605-14906:start -->已读取 `books/part-06-ai-infrastructure/66-evaluation-system.md` 及相邻章节；当前主线已覆盖model、harness、environment、scorer、budget、provenance 与 release authority 的完整评测身份。本 family 的增量“多模态长期 memory 评测必须显式比较 long-context 与 external-memory 路径，并冻结 decisive visual evidence、session evolution、ingestion cost 与 storage，而不是把文本 caption shortcut 当视觉记忆”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`66cd622a2aa49f23d15886aa07e741d61045c772e0d387f6fd7fcc1094d0a8ab`；相邻章节=`books/part-06-ai-infrastructure/65-kai-scheduler.md, books/part-06-ai-infrastructure/67-monitoring.md`。<!-- existing:SF-2026-ARXIV-2605-14906:end -->
<!-- delta:SF-2026-ARXIV-2605-14906:start -->多模态长期 memory 评测必须显式比较 long-context 与 external-memory 路径，并冻结 decisive visual evidence、session evolution、ingestion cost 与 storage，而不是把文本 caption shortcut 当视觉记忆<!-- delta:SF-2026-ARXIV-2605-14906:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-14906:end -->

<!-- books-review:SF-2026-ARXIV-2605-14932:start -->
<!-- existing:SF-2026-ARXIV-2605-14932:start -->已读取 `books/part-06-ai-infrastructure/72-security.md` 及相邻章节；当前主线已覆盖identity、typed capability、least privilege、policy mediation、effect boundary 与 audit。本 family 的增量“Agent security 应借鉴 OS 的 process isolation、capability、mediation 与 audit 边界；类比本身不证明任意 Agent runtime 已实现这些保证”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`45cdedd789e1517c5cd110897cbfaf39b57453fe2bc94b9bc64d72ffa4612bb3`；相邻章节=`books/part-06-ai-infrastructure/71-multi-tenant.md, books/part-06-ai-infrastructure/73-production-best-practice.md`。<!-- existing:SF-2026-ARXIV-2605-14932:end -->
<!-- delta:SF-2026-ARXIV-2605-14932:start -->Agent security 应借鉴 OS 的 process isolation、capability、mediation 与 audit 边界；类比本身不证明任意 Agent runtime 已实现这些保证<!-- delta:SF-2026-ARXIV-2605-14932:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-14932:end -->

<!-- books-review:SF-2026-ARXIV-2605-14968:start -->
<!-- existing:SF-2026-ARXIV-2605-14968:start -->已读取 `books/part-07-agent/81-workflow.md` 及相邻章节；当前主线已覆盖durable DAG/state、checkpoint、retry、compensation、external evidence 与 commit authority。本 family 的增量“可靠 Agent workflow 应把生成计划编译成 typed graph，并让可验证 node/edge contract、execution receipt 与 recovery policy拥有提交权；可视化 DAG 本身不构成正确性证明”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`a8a935c80e5047500f9c7beb334a74ac83381e49176a11f8beaa8b3da089fa92`；相邻章节=`books/part-07-agent/80-reflection.md, books/part-07-agent/82-multi-agent.md`。<!-- existing:SF-2026-ARXIV-2605-14968:end -->
<!-- delta:SF-2026-ARXIV-2605-14968:start -->可靠 Agent workflow 应把生成计划编译成 typed graph，并让可验证 node/edge contract、execution receipt 与 recovery policy拥有提交权；可视化 DAG 本身不构成正确性证明<!-- delta:SF-2026-ARXIV-2605-14968:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-14968:end -->

<!-- books-review:SF-2026-ARXIV-2605-14978:start -->
<!-- existing:SF-2026-ARXIV-2605-14978:start -->已读取 `books/part-05-inference-system/48-speculative-decoding.md` 及相邻章节；当前主线已覆盖draft/target identity、acceptance、verification、rollback 与 serving scheduling 的统一状态机。本 family 的增量“speculative window 不应是静态常数：在线 policy 可依据 acceptance、draft/verify cost 与服务负载调整 proposal 长度，但 target verification 与 rollback 始终保留最终 commit authority”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`0e93c132655861c91cdfd05e817b93105f2484b37753aec2bebe8d9ea15a0230`；相邻章节=`books/part-05-inference-system/47-pagedattention.md, books/part-05-inference-system/49-tensorrt-llm.md`。<!-- existing:SF-2026-ARXIV-2605-14978:end -->
<!-- delta:SF-2026-ARXIV-2605-14978:start -->speculative window 不应是静态常数：在线 policy 可依据 acceptance、draft/verify cost 与服务负载调整 proposal 长度，但 target verification 与 rollback 始终保留最终 commit authority<!-- delta:SF-2026-ARXIV-2605-14978:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-14978:end -->

<!-- books-review:SF-2026-ARXIV-2605-15030:start -->
<!-- existing:SF-2026-ARXIV-2605-15030:start -->已读取 `books/part-06-ai-infrastructure/72-security.md` 及相邻章节；当前主线已覆盖identity、typed capability、least privilege、policy mediation、effect boundary 与 audit。本 family 的增量“Web Agent 的 prompt-injection guard 应作为与 policy 解耦的并行 sensor，并以持续 adversarial update 管理 drift；guard 不能拥有最终 action authority”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`45cdedd789e1517c5cd110897cbfaf39b57453fe2bc94b9bc64d72ffa4612bb3`；相邻章节=`books/part-06-ai-infrastructure/71-multi-tenant.md, books/part-06-ai-infrastructure/73-production-best-practice.md`。<!-- existing:SF-2026-ARXIV-2605-15030:end -->
<!-- delta:SF-2026-ARXIV-2605-15030:start -->Web Agent 的 prompt-injection guard 应作为与 policy 解耦的并行 sensor，并以持续 adversarial update 管理 drift；guard 不能拥有最终 action authority<!-- delta:SF-2026-ARXIV-2605-15030:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-15030:end -->

<!-- books-review:SF-2026-ARXIV-2605-15034:start -->
<!-- existing:SF-2026-ARXIV-2605-15034:start -->已读取 `books/part-06-ai-infrastructure/66-evaluation-system.md` 及相邻章节；当前主线已覆盖model、harness、environment、scorer、budget、provenance 与 release authority 的完整评测身份。本 family 的增量“模型知道被观察时会改变行为，因此安全 evaluation 的 run identity 必须包含 monitoring disclosure、observer context 与 counterfactual hidden-monitor branch；被监控时合规不证明未监控时合规”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`66cd622a2aa49f23d15886aa07e741d61045c772e0d387f6fd7fcc1094d0a8ab`；相邻章节=`books/part-06-ai-infrastructure/65-kai-scheduler.md, books/part-06-ai-infrastructure/67-monitoring.md`。<!-- existing:SF-2026-ARXIV-2605-15034:end -->
<!-- delta:SF-2026-ARXIV-2605-15034:start -->模型知道被观察时会改变行为，因此安全 evaluation 的 run identity 必须包含 monitoring disclosure、observer context 与 counterfactual hidden-monitor branch；被监控时合规不证明未监控时合规<!-- delta:SF-2026-ARXIV-2605-15034:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-15034:end -->

<!-- books-review:SF-2026-ARXIV-2605-15051:start -->
<!-- existing:SF-2026-ARXIV-2605-15051:start -->已读取 `books/part-05-inference-system/48-speculative-decoding.md` 及相邻章节；当前主线已覆盖draft/target identity、acceptance、verification、rollback 与 serving scheduling 的统一状态机。正文尚未明确承载本 family 的增量：生产 speculative decoding 的 latency model 必须把 request load、emergent batch、draft/verify cost 与 acceptance 联合建模；固定 batch microbenchmark 不能决定在线启用策略。 Owner snapshot sha256=`0e93c132655861c91cdfd05e817b93105f2484b37753aec2bebe8d9ea15a0230`；相邻章节=`books/part-05-inference-system/47-pagedattention.md, books/part-05-inference-system/49-tensorrt-llm.md`。<!-- existing:SF-2026-ARXIV-2605-15051:end -->
<!-- delta:SF-2026-ARXIV-2605-15051:start -->生产 speculative decoding 的 latency model 必须把 request load、emergent batch、draft/verify cost 与 acceptance 联合建模；固定 batch microbenchmark 不能决定在线启用策略<!-- delta:SF-2026-ARXIV-2605-15051:end --> Decision: `Integrate`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-15051:end -->

<!-- books-review:SF-2026-ARXIV-2605-15079:start -->
<!-- existing:SF-2026-ARXIV-2605-15079:start -->已读取 `books/part-04-training-system/27-data.md` 及相邻章节；当前主线已覆盖dataset identity、schema、lineage、version、governance、quality gate 与 reusable artifact。正文尚未明确承载本 family 的增量：受治理或本地大数据集需要把 schema inference、profile、semantic annotation 与 Croissant JSON-LD provenance 组织为可复跑 pipeline，而不是先上传公共平台再生成 metadata。 Owner snapshot sha256=`cdd967c3fb6f506cec6ce3f112754e3f76a255641281bce71e1bfb1e09f98690`；相邻章节=`books/part-04-training-system/28-pretraining.md`。<!-- existing:SF-2026-ARXIV-2605-15079:end -->
<!-- delta:SF-2026-ARXIV-2605-15079:start -->受治理或本地大数据集需要把 schema inference、profile、semantic annotation 与 Croissant JSON-LD provenance 组织为可复跑 pipeline，而不是先上传公共平台再生成 metadata<!-- delta:SF-2026-ARXIV-2605-15079:end --> Decision: `Integrate`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-15079:end -->

<!-- books-review:SF-2026-ARXIV-2605-15100:start -->
<!-- existing:SF-2026-ARXIV-2605-15100:start -->已读取 `books/part-05-inference-system/56-inference-scheduling.md` 及相邻章节；当前主线已覆盖request/work-unit identity、budget、admission、priority、stop condition 与 SLO-aware execution control。本 family 的增量“test-time compute controller 必须把预算、质量目标、uncertainty 与 stop condition作为可提交 state；只增加推理步数既可能浪费预算也可能放大错误”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`aa1e5d4dea458d677ad3fc83ca72b0b799cba53dc07c7e6a31e9b7f2d2d8c533`；相邻章节=`books/part-05-inference-system/55-pd-disaggregation.md`。<!-- existing:SF-2026-ARXIV-2605-15100:end -->
<!-- delta:SF-2026-ARXIV-2605-15100:start -->test-time compute controller 必须把预算、质量目标、uncertainty 与 stop condition作为可提交 state；只增加推理步数既可能浪费预算也可能放大错误<!-- delta:SF-2026-ARXIV-2605-15100:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-15100:end -->

<!-- books-review:SF-2026-ARXIV-2605-15109:start -->
<!-- existing:SF-2026-ARXIV-2605-15109:start -->已读取 `books/part-07-agent/76-rag.md` 及相邻章节；当前主线已覆盖corpus identity、retrieval trajectory、evidence provenance、citation 与 answer claim 的绑定。正文尚未明确承载本 family 的增量：Agentic GraphRAG 的 citation faithfulness 应绑定完整 traversal neighborhood、visited-but-uncited evidence 与最终 citation；只验证末端引用会丢失推理路径 provenance。 Owner snapshot sha256=`9fbd3e0d51f58631aa1874a5ac618b37c4b1b7dfff667bc59293c5a2848e6510`；相邻章节=`books/part-07-agent/75-context.md, books/part-07-agent/77-memory.md`。<!-- existing:SF-2026-ARXIV-2605-15109:end -->
<!-- delta:SF-2026-ARXIV-2605-15109:start -->Agentic GraphRAG 的 citation faithfulness 应绑定完整 traversal neighborhood、visited-but-uncited evidence 与最终 citation；只验证末端引用会丢失推理路径 provenance<!-- delta:SF-2026-ARXIV-2605-15109:end --> Decision: `Integrate`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-15109:end -->

<!-- books-review:SF-2026-ARXIV-2605-15118:start -->
<!-- existing:SF-2026-ARXIV-2605-15118:start -->已读取 `books/part-06-ai-infrastructure/66-evaluation-system.md` 及相邻章节；当前主线已覆盖model、harness、environment、scorer、budget、provenance 与 release authority 的完整评测身份。本 family 的增量“攻击 benchmark coverage 应以 threat target×technique taxonomy 的可审计分母衡量；单个 benchmark 内部一致或高分不能证明覆盖了部署威胁面”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`66cd622a2aa49f23d15886aa07e741d61045c772e0d387f6fd7fcc1094d0a8ab`；相邻章节=`books/part-06-ai-infrastructure/65-kai-scheduler.md, books/part-06-ai-infrastructure/67-monitoring.md`。<!-- existing:SF-2026-ARXIV-2605-15118:end -->
<!-- delta:SF-2026-ARXIV-2605-15118:start -->攻击 benchmark coverage 应以 threat target×technique taxonomy 的可审计分母衡量；单个 benchmark 内部一致或高分不能证明覆盖了部署威胁面<!-- delta:SF-2026-ARXIV-2605-15118:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-15118:end -->

<!-- books-review:SF-2026-ARXIV-2605-15128:start -->
<!-- existing:SF-2026-ARXIV-2605-15128:start -->已读取 `books/part-06-ai-infrastructure/66-evaluation-system.md` 及相邻章节；当前主线已覆盖model、harness、environment、scorer、budget、provenance 与 release authority 的完整评测身份。本 family 的增量“多模态 memory 评测必须按 decisive visual evidence granularity 与跨时间使用方式切片，并用 ablation gate 排除 caption/text shortcut”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`66cd622a2aa49f23d15886aa07e741d61045c772e0d387f6fd7fcc1094d0a8ab`；相邻章节=`books/part-06-ai-infrastructure/65-kai-scheduler.md, books/part-06-ai-infrastructure/67-monitoring.md`。<!-- existing:SF-2026-ARXIV-2605-15128:end -->
<!-- delta:SF-2026-ARXIV-2605-15128:start -->多模态 memory 评测必须按 decisive visual evidence granularity 与跨时间使用方式切片，并用 ablation gate 排除 caption/text shortcut<!-- delta:SF-2026-ARXIV-2605-15128:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-15128:end -->

<!-- books-review:SF-2026-ARXIV-2605-15132:start -->
<!-- existing:SF-2026-ARXIV-2605-15132:start -->已读取 `books/part-07-agent/81-workflow.md` 及相邻章节；当前主线已覆盖durable DAG/state、checkpoint、retry、compensation、external evidence 与 commit authority。正文尚未明确承载本 family 的增量：可并行 Agent workflow 应把 dependency DAG、task state、worker placement 与 aggregation commit 分离；吞吐扩展不能牺牲依赖一致性与 failure recovery。 Owner snapshot sha256=`a8a935c80e5047500f9c7beb334a74ac83381e49176a11f8beaa8b3da089fa92`；相邻章节=`books/part-07-agent/80-reflection.md, books/part-07-agent/82-multi-agent.md`。<!-- existing:SF-2026-ARXIV-2605-15132:end -->
<!-- delta:SF-2026-ARXIV-2605-15132:start -->可并行 Agent workflow 应把 dependency DAG、task state、worker placement 与 aggregation commit 分离；吞吐扩展不能牺牲依赖一致性与 failure recovery<!-- delta:SF-2026-ARXIV-2605-15132:end --> Decision: `Integrate`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-15132:end -->

<!-- books-review:SF-2026-ARXIV-2605-15138:start -->
<!-- existing:SF-2026-ARXIV-2605-15138:start -->已读取 `books/part-06-ai-infrastructure/72-security.md` 及相邻章节；当前主线已覆盖identity、typed capability、least privilege、policy mediation、effect boundary 与 audit。本 family 的增量“unlearning release gate 必须在最终量化 artifact 上复验，而不只验 full-precision checkpoint；更新小于 quantization bin 时会被压缩抹除，需要 circuit-local permanence 与 utility 双验收”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`45cdedd789e1517c5cd110897cbfaf39b57453fe2bc94b9bc64d72ffa4612bb3`；相邻章节=`books/part-06-ai-infrastructure/71-multi-tenant.md, books/part-06-ai-infrastructure/73-production-best-practice.md`。<!-- existing:SF-2026-ARXIV-2605-15138:end -->
<!-- delta:SF-2026-ARXIV-2605-15138:start -->unlearning release gate 必须在最终量化 artifact 上复验，而不只验 full-precision checkpoint；更新小于 quantization bin 时会被压缩抹除，需要 circuit-local permanence 与 utility 双验收<!-- delta:SF-2026-ARXIV-2605-15138:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-15138:end -->

<!-- books-review:SF-2026-ARXIV-2605-15152:start -->
<!-- existing:SF-2026-ARXIV-2605-15152:start -->已读取 `books/part-06-ai-infrastructure/72-security.md` 及相邻章节；当前主线已覆盖identity、typed capability、least privilege、policy mediation、effect boundary 与 audit。本 family 的增量“模型供应链验收必须比较 full-precision 与实际 AWQ/GPTQ/GGUF 等量化 artifact 的行为；outlier-induced rounding 可把量化步骤变成隐藏触发器”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`45cdedd789e1517c5cd110897cbfaf39b57453fe2bc94b9bc64d72ffa4612bb3`；相邻章节=`books/part-06-ai-infrastructure/71-multi-tenant.md, books/part-06-ai-infrastructure/73-production-best-practice.md`。<!-- existing:SF-2026-ARXIV-2605-15152:end -->
<!-- delta:SF-2026-ARXIV-2605-15152:start -->模型供应链验收必须比较 full-precision 与实际 AWQ/GPTQ/GGUF 等量化 artifact 的行为；outlier-induced rounding 可把量化步骤变成隐藏触发器<!-- delta:SF-2026-ARXIV-2605-15152:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-15152:end -->

<!-- books-review:SF-2026-ARXIV-2605-15155:start -->
<!-- existing:SF-2026-ARXIV-2605-15155:start -->已读取 `books/part-04-training-system/33-grpo.md` 及相邻章节；当前主线已覆盖trajectory grouping、verifier/environment reward、token/sequence credit、KL/clipping 与 rollout-policy identity。本 family 的增量“Agent RL 的 privileged self-teacher 只能作为 detached、按 token gap gating 的辅助 signal；environment/verifier reward 保留 trajectory truth，错误 skill retrieval 不能让 teacher rejection 主导更新”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`c75d66bc18a9221e70da0fc29018962765e69241af2ce0959becf0ab5f8e49a8`；相邻章节=`books/part-04-training-system/32-ppo.md, books/part-04-training-system/34-dpo.md`。<!-- existing:SF-2026-ARXIV-2605-15155:end -->
<!-- delta:SF-2026-ARXIV-2605-15155:start -->Agent RL 的 privileged self-teacher 只能作为 detached、按 token gap gating 的辅助 signal；environment/verifier reward 保留 trajectory truth，错误 skill retrieval 不能让 teacher rejection 主导更新<!-- delta:SF-2026-ARXIV-2605-15155:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-15155:end -->

<!-- books-review:SF-2026-ARXIV-2605-15164:start -->
<!-- existing:SF-2026-ARXIV-2605-15164:start -->已读取 `books/part-06-ai-infrastructure/66-evaluation-system.md` 及相邻章节；当前主线已覆盖model、harness、environment、scorer、budget、provenance 与 release authority 的完整评测身份。本 family 的增量“behavioural evaluation 只能支持可观察行为声明，不能独立验证 hidden objective、loss-of-control absence 等内部或反事实安全命题”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`66cd622a2aa49f23d15886aa07e741d61045c772e0d387f6fd7fcc1094d0a8ab`；相邻章节=`books/part-06-ai-infrastructure/65-kai-scheduler.md, books/part-06-ai-infrastructure/67-monitoring.md`。<!-- existing:SF-2026-ARXIV-2605-15164:end -->
<!-- delta:SF-2026-ARXIV-2605-15164:start -->behavioural evaluation 只能支持可观察行为声明，不能独立验证 hidden objective、loss-of-control absence 等内部或反事实安全命题<!-- delta:SF-2026-ARXIV-2605-15164:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-15164:end -->

<!-- books-review:SF-2026-ARXIV-2605-15172:start -->
<!-- existing:SF-2026-ARXIV-2605-15172:start -->已读取 `books/part-06-ai-infrastructure/72-security.md` 及相邻章节；当前主线已覆盖identity、typed capability、least privilege、policy mediation、effect boundary 与 audit。本 family 的增量“backdoor release testing 不能只变换内容：position/length metadata 也可成为不可见 trigger，因此 clean semantics、长度切片与 position-encoding interventions 必须共同进入验收”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`45cdedd789e1517c5cd110897cbfaf39b57453fe2bc94b9bc64d72ffa4612bb3`；相邻章节=`books/part-06-ai-infrastructure/71-multi-tenant.md, books/part-06-ai-infrastructure/73-production-best-practice.md`。<!-- existing:SF-2026-ARXIV-2605-15172:end -->
<!-- delta:SF-2026-ARXIV-2605-15172:start -->backdoor release testing 不能只变换内容：position/length metadata 也可成为不可见 trigger，因此 clean semantics、长度切片与 position-encoding interventions 必须共同进入验收<!-- delta:SF-2026-ARXIV-2605-15172:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-15172:end -->

<!-- books-review:SF-2026-ARXIV-2605-15178:start -->
<!-- existing:SF-2026-ARXIV-2605-15178:start -->已读取 `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 及相邻章节；当前主线已覆盖observation quality、action-conditioned transition、geometry、persistent world state 与 planning handoff。本 family 的增量“minute-scale controllable video generation通过 hybrid linear/softmax attention、camera-control branch与two-stage refinement扩展 rollout；但视觉一致和相机遵循仍不等于 action-conditioned causal world state”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`2b8a3f6f457ba203854a2b4078d943ca0b14422f842cad9ee4809b1e86684998`；相邻章节=`books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md, books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md`。<!-- existing:SF-2026-ARXIV-2605-15178:end -->
<!-- delta:SF-2026-ARXIV-2605-15178:start -->minute-scale controllable video generation通过 hybrid linear/softmax attention、camera-control branch与two-stage refinement扩展 rollout；但视觉一致和相机遵循仍不等于 action-conditioned causal world state<!-- delta:SF-2026-ARXIV-2605-15178:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-15178:end -->

<!-- books-review:SF-2026-ARXIV-2605-15184:start -->
<!-- existing:SF-2026-ARXIV-2605-15184:start -->已读取 `books/part-07-agent/76-rag.md` 及相邻章节；当前主线已覆盖corpus identity、retrieval trajectory、evidence provenance、citation 与 answer claim 的绑定。本 family 的增量“Agent search 评测必须把 retrieval strategy、harness/tool interface 与 corpus access 联合冻结；grep 或 vector retrieval 的结论不能脱离 harness”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`9fbd3e0d51f58631aa1874a5ac618b37c4b1b7dfff667bc59293c5a2848e6510`；相邻章节=`books/part-07-agent/75-context.md, books/part-07-agent/77-memory.md`。<!-- existing:SF-2026-ARXIV-2605-15184:end -->
<!-- delta:SF-2026-ARXIV-2605-15184:start -->Agent search 评测必须把 retrieval strategy、harness/tool interface 与 corpus access 联合冻结；grep 或 vector retrieval 的结论不能脱离 harness<!-- delta:SF-2026-ARXIV-2605-15184:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-15184:end -->

<!-- books-review:SF-2026-ARXIV-2605-15185:start -->
<!-- existing:SF-2026-ARXIV-2605-15185:start -->已读取 `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 及相邻章节；当前主线已覆盖observation quality、action-conditioned transition、geometry、persistent world state 与 planning handoff。正文尚未明确承载本 family 的增量：视频 world-model 评测应把视觉质量与可度量的 3D geometric consistency 分开，并用 camera/scene geometry 诊断 perspective distortion；该指标不等于 causal controllability。 Owner snapshot sha256=`2b8a3f6f457ba203854a2b4078d943ca0b14422f842cad9ee4809b1e86684998`；相邻章节=`books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md, books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md`。<!-- existing:SF-2026-ARXIV-2605-15185:end -->
<!-- delta:SF-2026-ARXIV-2605-15185:start -->视频 world-model 评测应把视觉质量与可度量的 3D geometric consistency 分开，并用 camera/scene geometry 诊断 perspective distortion；该指标不等于 causal controllability<!-- delta:SF-2026-ARXIV-2605-15185:end --> Decision: `Integrate`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-15185:end -->

<!-- books-review:SF-2026-ARXIV-2605-15188:start -->
<!-- existing:SF-2026-ARXIV-2605-15188:start -->已读取 `books/part-06-ai-infrastructure/66-evaluation-system.md` 及相邻章节；当前主线已覆盖model、harness、environment、scorer、budget、provenance 与 release authority 的完整评测身份。本 family 的增量“开放世界 Agent 评测应冻结历史时钟、逐步释放外生事件并用预测/outcome轨迹评分 adaptation；静态 knowledge cutoff 问答不能代表持续适应”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`66cd622a2aa49f23d15886aa07e741d61045c772e0d387f6fd7fcc1094d0a8ab`；相邻章节=`books/part-06-ai-infrastructure/65-kai-scheduler.md, books/part-06-ai-infrastructure/67-monitoring.md`。<!-- existing:SF-2026-ARXIV-2605-15188:end -->
<!-- delta:SF-2026-ARXIV-2605-15188:start -->开放世界 Agent 评测应冻结历史时钟、逐步释放外生事件并用预测/outcome轨迹评分 adaptation；静态 knowledge cutoff 问答不能代表持续适应<!-- delta:SF-2026-ARXIV-2605-15188:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-15188:end -->

<!-- books-review:SF-AGENTTRAP-MEASURING-RUNTIME-TRUST-FAILURES-IN-THIRD-PARTY-AGENT-SKILLS:start -->
<!-- existing:SF-AGENTTRAP-MEASURING-RUNTIME-TRUST-FAILURES-IN-THIRD-PARTY-AGENT-SKILLS:start -->已读取 `books/part-06-ai-infrastructure/72-security.md` 及相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；owner 当前主干包含 ['本章要回答的问题', '从资产与信任边界开始', '生命周期威胁', '隐私检测是 Policy-bound Sensor，不是安全判决', '从独立 Span 到关系感知的本地 Sanitization', 'Differential Privacy 先定义被保护对象，再选择机制', 'Capability Access Control 可以前移到训练状态', 'Policy-as-Data：可更新规则与模型判断必须分开版本化']。仅正文命题用于比较，Review notes 不视为整合。<!-- existing:SF-AGENTTRAP-MEASURING-RUNTIME-TRUST-FAILURES-IN-THIRD-PARTY-AGENT-SKILLS:end -->
<!-- delta:SF-AGENTTRAP-MEASURING-RUNTIME-TRUST-FAILURES-IN-THIRD-PARTY-AGENT-SKILLS:start -->We introduce AgentTrap, a dynamic benchmark for evaluating whether LLM agents can use third-party skills while resisting malicious runtime behavior.<!-- delta:SF-AGENTTRAP-MEASURING-RUNTIME-TRUST-FAILURES-IN-THIRD-PARTY-AGENT-SKILLS:end --> Independent decision=`No Change — Existing Coverage`；prewrite challenge 已通过，不写共享 Books。
<!-- books-review:SF-AGENTTRAP-MEASURING-RUNTIME-TRUST-FAILURES-IN-THIRD-PARTY-AGENT-SKILLS:end -->

<!-- books-review:SF-CHROMAFLOW-A-NEGATIVE-ABLATION-STUDY-OF-ORCHESTRATION-OVERHEAD-IN-TOOL-A:start -->
<!-- existing:SF-CHROMAFLOW-A-NEGATIVE-ABLATION-STUDY-OF-ORCHESTRATION-OVERHEAD-IN-TOOL-A:start -->已读取 `books/part-07-agent/81-workflow.md` 及相邻章节 ['books/part-07-agent/80-reflection.md', 'books/part-07-agent/82-multi-agent.md']；owner 当前主干包含 ['本章要回答的问题', '一个循环为什么不够', 'State Machine 是基本模型', 'Failure attribution、perception routing 与 sticky state ownership', 'Review notes', '从“对象已保存”到“状态已激活”', 'Deterministic Spine，Agentic Nodes', '从一次性脚本到平台拥有的可编辑 DAG']。仅正文命题用于比较，Review notes 不视为整合。<!-- existing:SF-CHROMAFLOW-A-NEGATIVE-ABLATION-STUDY-OF-ORCHESTRATION-OVERHEAD-IN-TOOL-A:end -->
<!-- delta:SF-CHROMAFLOW-A-NEGATIVE-ABLATION-STUDY-OF-ORCHESTRATION-OVERHEAD-IN-TOOL-A:start -->These capabilities make agent systems more useful, but they also introduce operational failure modes that are not visible from final accuracy alone.<!-- delta:SF-CHROMAFLOW-A-NEGATIVE-ABLATION-STUDY-OF-ORCHESTRATION-OVERHEAD-IN-TOOL-A:end --> Independent decision=`No Change — Existing Coverage`；prewrite challenge 已通过，不写共享 Books。
<!-- books-review:SF-CHROMAFLOW-A-NEGATIVE-ABLATION-STUDY-OF-ORCHESTRATION-OVERHEAD-IN-TOOL-A:end -->

<!-- books-review:SF-DIAGNOSING-TRAINING-INFERENCE-MISMATCH-IN-LLM-REINFORCEMENT-LEARNING:start -->
<!-- existing:SF-DIAGNOSING-TRAINING-INFERENCE-MISMATCH-IN-LLM-REINFORCEMENT-LEARNING:start -->已读取 `books/part-04-training-system/31-rlhf.md` 及相邻章节 ['books/part-04-training-system/30-lora.md', 'books/part-04-training-system/32-ppo.md']；owner 当前主干包含 ['本章要回答的问题', 'Demonstration 为什么不足以表达偏好', 'RLHF 的完整 pipeline', 'Reward Model 怎样学习相对判断', '一个 preference score 小例子', 'Preference data 的难点不只是数量', '从 Reward 到 Policy objective', '改变输出分布是目标，不是无副作用的偏好标签']。仅正文命题用于比较，Review notes 不视为整合。<!-- existing:SF-DIAGNOSING-TRAINING-INFERENCE-MISMATCH-IN-LLM-REINFORCEMENT-LEARNING:end -->
<!-- delta:SF-DIAGNOSING-TRAINING-INFERENCE-MISMATCH-IN-LLM-REINFORCEMENT-LEARNING:start -->In this work, we isolate TIM in a zero-mismatch diagnostic setting (VeXact), and show that small token-level numerical disagreements can independently cause training collapse.<!-- delta:SF-DIAGNOSING-TRAINING-INFERENCE-MISMATCH-IN-LLM-REINFORCEMENT-LEARNING:end --> Independent decision=`Integrate`；prewrite challenge 已通过，不写共享 Books。
<!-- books-review:SF-DIAGNOSING-TRAINING-INFERENCE-MISMATCH-IN-LLM-REINFORCEMENT-LEARNING:end -->

<!-- books-review:SF-EVOLVEMEM-SELF-EVOLVING-MEMORY-ARCHITECTURE-VIA-AUTORESEARCH-FOR-LLM-AGE:start -->
<!-- existing:SF-EVOLVEMEM-SELF-EVOLVING-MEMORY-ARCHITECTURE-VIA-AUTORESEARCH-FOR-LLM-AGE:start -->已读取 `books/part-07-agent/77-memory.md` 及相邻章节 ['books/part-07-agent/76-rag.md', 'books/part-07-agent/78-tool-calling.md']；owner 当前主干包含 ['本章要回答的问题', 'Context 与 Memory 的状态边界', 'Memory 类型是用途，不只是存储介质', 'Memory Write 是高风险决策', 'Write / Hold 不足以定义下一状态', '从 Outcome Reward 到 Content-level Credit：归因只能约束写入，不能成为真值', 'Memory Read 是受约束检索', '从按需读取到选择性主动干预']。仅正文命题用于比较，Review notes 不视为整合。<!-- existing:SF-EVOLVEMEM-SELF-EVOLVING-MEMORY-ARCHITECTURE-VIA-AUTORESEARCH-FOR-LLM-AGE:end -->
<!-- delta:SF-EVOLVEMEM-SELF-EVOLVING-MEMORY-ARCHITECTURE-VIA-AUTORESEARCH-FOR-LLM-AGE:start -->We present EvolveMem, a self-evolving memory architecture that exposes its full retrieval configuration as a structured action space optimized by an LLM-powered diagnosis module.<!-- delta:SF-EVOLVEMEM-SELF-EVOLVING-MEMORY-ARCHITECTURE-VIA-AUTORESEARCH-FOR-LLM-AGE:end --> Independent decision=`No Change — Existing Coverage`；prewrite challenge 已通过，不写共享 Books。
<!-- books-review:SF-EVOLVEMEM-SELF-EVOLVING-MEMORY-ARCHITECTURE-VIA-AUTORESEARCH-FOR-LLM-AGE:end -->

<!-- books-review:SF-GROUNDED-CONTINUATION-A-LINEAR-TIME-RUNTIME-VERIFIER-FOR-LLM-CONVERSATIO:start -->
<!-- existing:SF-GROUNDED-CONTINUATION-A-LINEAR-TIME-RUNTIME-VERIFIER-FOR-LLM-CONVERSATIO:start -->已读取 `books/part-06-ai-infrastructure/72-security.md` 及相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；owner 当前主干包含 ['本章要回答的问题', '从资产与信任边界开始', '生命周期威胁', '隐私检测是 Policy-bound Sensor，不是安全判决', '从独立 Span 到关系感知的本地 Sanitization', 'Differential Privacy 先定义被保护对象，再选择机制', 'Capability Access Control 可以前移到训练状态', 'Policy-as-Data：可更新规则与模型判断必须分开版本化']。仅正文命题用于比较，Review notes 不视为整合。<!-- existing:SF-GROUNDED-CONTINUATION-A-LINEAR-TIME-RUNTIME-VERIFIER-FOR-LLM-CONVERSATIO:end -->
<!-- delta:SF-GROUNDED-CONTINUATION-A-LINEAR-TIME-RUNTIME-VERIFIER-FOR-LLM-CONVERSATIO:start -->Beyond external benchmarks, we construct two multi-agent scenarios and a 50-item grounding test: on the 15-item stale-premise subset, the verifier reaches 100% accuracy vs.<!-- delta:SF-GROUNDED-CONTINUATION-A-LINEAR-TIME-RUNTIME-VERIFIER-FOR-LLM-CONVERSATIO:end --> Independent decision=`Integrate`；prewrite challenge 已通过，不写共享 Books。
<!-- books-review:SF-GROUNDED-CONTINUATION-A-LINEAR-TIME-RUNTIME-VERIFIER-FOR-LLM-CONVERSATIO:end -->

<!-- books-review:SF-HOW-TO-SCALE-MIXTURE-OF-EXPERTS-FROM-MUP-TO-THE-MAXIMALLY-SCALE-STABLE-P:start -->
<!-- existing:SF-HOW-TO-SCALE-MIXTURE-OF-EXPERTS-FROM-MUP-TO-THE-MAXIMALLY-SCALE-STABLE-P:start -->已读取 `books/part-02-model/21-moe.md` 及相邻章节 ['books/part-02-model/20-sampling.md', 'books/part-02-model/22-long-context.md']；owner 当前主干包含 ['本章要回答的问题', '从 Dense MLP 的绑定关系开始', 'Router 的 tensor shape', '一个 top-2 小例子', 'Total parameters 与 Active parameters', 'Total / Active Parameters 只是约束坐标，不是架构答案', '先改变通信坐标，再扩大稀疏容量', '为什么负载均衡是模型正确性的一部分']。仅正文命题用于比较，Review notes 不视为整合。<!-- existing:SF-HOW-TO-SCALE-MIXTURE-OF-EXPERTS-FROM-MUP-TO-THE-MAXIMALLY-SCALE-STABLE-P:end -->
<!-- delta:SF-HOW-TO-SCALE-MIXTURE-OF-EXPERTS-FROM-MUP-TO-THE-MAXIMALLY-SCALE-STABLE-P:start -->For each regime, we develop a novel Dynamical Mean Field Theory (DMFT) description of the limiting training dynamics of MoEs that provides a formal foundation for our analysis.<!-- delta:SF-HOW-TO-SCALE-MIXTURE-OF-EXPERTS-FROM-MUP-TO-THE-MAXIMALLY-SCALE-STABLE-P:end --> Independent decision=`No Change — Existing Coverage`；prewrite challenge 已通过，不写共享 Books。
<!-- books-review:SF-HOW-TO-SCALE-MIXTURE-OF-EXPERTS-FROM-MUP-TO-THE-MAXIMALLY-SCALE-STABLE-P:end -->

<!-- books-review:SF-LLMS-KNOW-WHEN-THEY-KNOW-BUT-DO-NOT-ACT-ON-IT-A-METACOGNITIVE-HARNESS-FO:start -->
<!-- existing:SF-LLMS-KNOW-WHEN-THEY-KNOW-BUT-DO-NOT-ACT-ON-IT-A-METACOGNITIVE-HARNESS-FO:start -->已读取 `books/part-05-inference-system/56-inference-scheduling.md` 及相邻章节 ['books/part-05-inference-system/55-pd-disaggregation.md', 'books/part-05-inference-system/README.md']；owner 当前主干包含 ['本章要回答的问题', '调度对象从 request 变成 token state', '目标函数不止吞吐', 'SLO-aware Admission', '当前能放下，不等于未来可完成', '不确定输出长度下的 Future-state Reservation', '连续 Edge Inference 需要跨窗口携带 Violation-risk Budget', '从队列启发式到时间耦合的资源影子价格']。仅正文命题用于比较，Review notes 不视为整合。<!-- existing:SF-LLMS-KNOW-WHEN-THEY-KNOW-BUT-DO-NOT-ACT-ON-IT-A-METACOGNITIVE-HARNESS-FO:end -->
<!-- delta:SF-LLMS-KNOW-WHEN-THEY-KNOW-BUT-DO-NOT-ACT-ON-IT-A-METACOGNITIVE-HARNESS-FO:start -->Inspired by the Nelson--Narens theory from cognitive psychology, we propose a metacognitive harness that separates monitoring from reasoning.<!-- delta:SF-LLMS-KNOW-WHEN-THEY-KNOW-BUT-DO-NOT-ACT-ON-IT-A-METACOGNITIVE-HARNESS-FO:end --> Independent decision=`Integrate`；prewrite challenge 已通过，不写共享 Books。
<!-- books-review:SF-LLMS-KNOW-WHEN-THEY-KNOW-BUT-DO-NOT-ACT-ON-IT-A-METACOGNITIVE-HARNESS-FO:end -->

<!-- books-review:SF-MISTLETOE-STEALTHY-ACCELERATION-COLLAPSE-ATTACKS-ON-SPECULATIVE-DECODING:start -->
<!-- existing:SF-MISTLETOE-STEALTHY-ACCELERATION-COLLAPSE-ATTACKS-ON-SPECULATIVE-DECODING:start -->已读取 `books/part-06-ai-infrastructure/72-security.md` 及相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；owner 当前主干包含 ['本章要回答的问题', '从资产与信任边界开始', '生命周期威胁', '隐私检测是 Policy-bound Sensor，不是安全判决', '从独立 Span 到关系感知的本地 Sanitization', 'Differential Privacy 先定义被保护对象，再选择机制', 'Capability Access Control 可以前移到训练状态', 'Policy-as-Data：可更新规则与模型判断必须分开版本化']。仅正文命题用于比较，Review notes 不视为整合。<!-- existing:SF-MISTLETOE-STEALTHY-ACCELERATION-COLLAPSE-ATTACKS-ON-SPECULATIVE-DECODING:end -->
<!-- delta:SF-MISTLETOE-STEALTHY-ACCELERATION-COLLAPSE-ATTACKS-ON-SPECULATIVE-DECODING:start -->We propose Mistletoe, a stealthy acceleration-collapse attack against speculative decoding.<!-- delta:SF-MISTLETOE-STEALTHY-ACCELERATION-COLLAPSE-ATTACKS-ON-SPECULATIVE-DECODING:end --> Independent decision=`Integrate`；prewrite challenge 已通过，不写共享 Books。
<!-- books-review:SF-MISTLETOE-STEALTHY-ACCELERATION-COLLAPSE-ATTACKS-ON-SPECULATIVE-DECODING:end -->

<!-- books-review:SF-MODEL-ADAPTIVE-TOOL-NECESSITY-REVEALS-THE-KNOWING-DOING-GAP-IN-LLM-TOOL-:start -->
<!-- existing:SF-MODEL-ADAPTIVE-TOOL-NECESSITY-REVEALS-THE-KNOWING-DOING-GAP-IN-LLM-TOOL-:start -->已读取 `books/part-07-agent/78-tool-calling.md` 及相邻章节 ['books/part-07-agent/77-memory.md', 'books/part-07-agent/79-planning.md']；owner 当前主干包含 ['本章要回答的问题', '从生成文本到环境转移', 'Tool Contract', '模型输出只是 Proposal', '编译器反馈可以前移，但仍是受限 Authority', 'Tool Discovery 与选择', 'Interface Granularity：不是 Tool 越多越有能力', 'Agent-friendly Tool 不等于把 CLI 包一层']。仅正文命题用于比较，Review notes 不视为整合。<!-- existing:SF-MODEL-ADAPTIVE-TOOL-NECESSITY-REVEALS-THE-KNOWING-DOING-GAP-IN-LLM-TOOL-:end -->
<!-- delta:SF-MODEL-ADAPTIVE-TOOL-NECESSITY-REVEALS-THE-KNOWING-DOING-GAP-IN-LLM-TOOL-:start -->In this work, we introduce a model-adaptive definition of tool-necessity, grounded in each model's empirical performance.<!-- delta:SF-MODEL-ADAPTIVE-TOOL-NECESSITY-REVEALS-THE-KNOWING-DOING-GAP-IN-LLM-TOOL-:end --> Independent decision=`Integrate`；prewrite challenge 已通过，不写共享 Books。
<!-- books-review:SF-MODEL-ADAPTIVE-TOOL-NECESSITY-REVEALS-THE-KNOWING-DOING-GAP-IN-LLM-TOOL-:end -->

<!-- books-review:SF-MULTI-SCALE-DEQUANT-ELIMINATING-DEQUANTIZATION-BOTTLENECK-VIA-ACTIVATION:start -->
<!-- existing:SF-MULTI-SCALE-DEQUANT-ELIMINATING-DEQUANTIZATION-BOTTLENECK-VIA-ACTIVATION:start -->已读取 `books/part-05-inference-system/49-tensorrt-llm.md` 及相邻章节 ['books/part-05-inference-system/48-speculative-decoding.md', 'books/part-05-inference-system/50-vllm.md']；owner 当前主干包含 ['本章要回答的问题', '从计算图开始', '三类基础优化', 'Execution Plan 可以修订，但只能在安全边界 Commit', '异步工作不必永久绑定固定 Physical Core', '从粗粒度 Offload 到负载观测的 Tensor Placement', 'Backend Choice 必须携带 Previous-backend State', 'Accelerator Readiness 是 Phase × Shape × Offload × Host-control Contract']。仅正文命题用于比较，Review notes 不视为整合。<!-- existing:SF-MULTI-SCALE-DEQUANT-ELIMINATING-DEQUANTIZATION-BOTTLENECK-VIA-ACTIVATION:end -->
<!-- delta:SF-MULTI-SCALE-DEQUANT-ELIMINATING-DEQUANTIZATION-BOTTLENECK-VIA-ACTIVATION:start -->Quantization is essential for efficient large language model (LLM) inference, yet the dequantization step-converting low-bit weights back to high-precision for matrix multiplication has become a critical bottleneck on modern AI accelerators.<!-- delta:SF-MULTI-SCALE-DEQUANT-ELIMINATING-DEQUANTIZATION-BOTTLENECK-VIA-ACTIVATION:end --> Independent decision=`No Change — Existing Coverage`；prewrite challenge 已通过，不写共享 Books。
<!-- books-review:SF-MULTI-SCALE-DEQUANT-ELIMINATING-DEQUANTIZATION-BOTTLENECK-VIA-ACTIVATION:end -->

<!-- books-review:SF-PREFT-PREFILL-ONLY-FINETUNING-FOR-EFFICIENT-INFERENCE:start -->
<!-- existing:SF-PREFT-PREFILL-ONLY-FINETUNING-FOR-EFFICIENT-INFERENCE:start -->已读取 `books/part-05-inference-system/43-prefill.md` 及相邻章节 ['books/part-05-inference-system/42-what-happens-during-inference.md', 'books/part-05-inference-system/44-decode.md']；owner 当前主干包含 ['本章要回答的问题', '如果逐个 Token 读 Prompt', 'Prefill 的两个输出', '计算量从哪里来', 'Sparse Prefill：少算 Attention 之前，先要付出 Selection Cost', 'Flat Token Index 之后：Hierarchical Index 也有可见的错误预算', '一个 Shape 小例子', 'TTFT 不等于 Prefill Kernel Time']。仅正文命题用于比较，Review notes 不视为整合。<!-- existing:SF-PREFT-PREFILL-ONLY-FINETUNING-FOR-EFFICIENT-INFERENCE:end -->
<!-- delta:SF-PREFT-PREFILL-ONLY-FINETUNING-FOR-EFFICIENT-INFERENCE:start -->We therefore propose PreFT (Prefill-only Finetuning), wherein we only apply the adapter to prefill tokens and discard it afterwards.<!-- delta:SF-PREFT-PREFILL-ONLY-FINETUNING-FOR-EFFICIENT-INFERENCE:end --> Independent decision=`No Change — Existing Coverage`；prewrite challenge 已通过，不写共享 Books。
<!-- books-review:SF-PREFT-PREFILL-ONLY-FINETUNING-FOR-EFFICIENT-INFERENCE:end -->

<!-- books-review:SF-SELF-PRUNED-KEY-VALUE-ATTENTION-LEARNING-WHEN-TO-WRITE-BY-PREDICTING-FUT:start -->
<!-- existing:SF-SELF-PRUNED-KEY-VALUE-ATTENTION-LEARNING-WHEN-TO-WRITE-BY-PREDICTING-FUT:start -->已读取 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 及相邻章节 ['books/part-05-inference-system/44-decode.md', 'books/part-05-inference-system/46-continuous-batching.md']；owner 当前主干包含 ['本章要回答的问题', '如果完全不缓存', '为什么缓存 K/V 而不是 Query', '逻辑 Shape 与容量公式', '一个容量小例子', 'KV Cache 的生命周期', 'Prefix reuse', 'KV 从生成私有状态演进为受约束的下游读出接口']。仅正文命题用于比较，Review notes 不视为整合。<!-- existing:SF-SELF-PRUNED-KEY-VALUE-ATTENTION-LEARNING-WHEN-TO-WRITE-BY-PREDICTING-FUT:end -->
<!-- delta:SF-SELF-PRUNED-KEY-VALUE-ATTENTION-LEARNING-WHEN-TO-WRITE-BY-PREDICTING-FUT:start -->To address this limitation, we introduce Self-Pruned Key-Value Attention (SP-KV), a mechanism designed to predict future KV utility in order to reduce the size of the long-term KV cache.<!-- delta:SF-SELF-PRUNED-KEY-VALUE-ATTENTION-LEARNING-WHEN-TO-WRITE-BY-PREDICTING-FUT:end --> Independent decision=`No Change — Existing Coverage`；prewrite challenge 已通过，不写共享 Books。
<!-- books-review:SF-SELF-PRUNED-KEY-VALUE-ATTENTION-LEARNING-WHEN-TO-WRITE-BY-PREDICTING-FUT:end -->

<!-- books-review:SF-SKILLFLOW-FLOW-DRIVEN-RECURSIVE-SKILL-EVOLUTION-FOR-AGENTIC-ORCHESTRATIO:start -->
<!-- existing:SF-SKILLFLOW-FLOW-DRIVEN-RECURSIVE-SKILL-EVOLUTION-FOR-AGENTIC-ORCHESTRATIO:start -->已读取 `books/part-07-agent/84-agent-platform.md` 及相邻章节 ['books/part-07-agent/83-mcp.md', 'books/part-07-agent/README.md']；owner 当前主干包含 ['本章要回答的问题', 'Agent 改变了平台的控制对象', 'Serving 结束不等于 Agent 任务结束', 'Agent Definition 与 Run Identity', '可复用 Skill 不是一个 Prompt 文件', '从 Skill Catalog 到 Competence-aware Orchestration', '从 Trajectory 到 Skill 是一次受治理的 Compilation', 'Skill Compiler 必须绑定 Target Profile，而不是只绑定模型名']。仅正文命题用于比较，Review notes 不视为整合。<!-- existing:SF-SKILLFLOW-FLOW-DRIVEN-RECURSIVE-SKILL-EVOLUTION-FOR-AGENTIC-ORCHESTRATIO:end -->
<!-- delta:SF-SKILLFLOW-FLOW-DRIVEN-RECURSIVE-SKILL-EVOLUTION-FOR-AGENTIC-ORCHESTRATIO:start -->To address these challenges, we propose SkillFlow, a flow-based framework that takes a trainable Supervisor as the agent and a structured environment with dynamic skill library and frozen executor, automating task orchestration through multi-turn interaction.<!-- delta:SF-SKILLFLOW-FLOW-DRIVEN-RECURSIVE-SKILL-EVOLUTION-FOR-AGENTIC-ORCHESTRATIO:end --> Independent decision=`No Change — Existing Coverage`；prewrite challenge 已通过，不写共享 Books。
<!-- books-review:SF-SKILLFLOW-FLOW-DRIVEN-RECURSIVE-SKILL-EVOLUTION-FOR-AGENTIC-ORCHESTRATIO:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260515-COVERAGE | fresh-context:owner-replay-20260903 | coverage | coverage:SRC-ARXIV:20260515 | none | raw/retained/closure/withdrawn conservation and initial-created owner mapping independently recounted | passed |
| SA-20260515-EVIDENCE | fresh-context:owner-replay-20260903 | evidence | validator:review-completion-v1 | none | every frozen family has a completed exact-version receipt; blocked=0 | passed |
| SA-20260515-SELECTION | fresh-context:owner-replay-20260903 | deep_analysis_selection | validator:deep-analysis-selection-v1 | none | eligible=58；selected=3；all others retain completed reviews | passed |
| SA-20260515-BOOKS | fresh-context:apr-may-books-20260903 | books | validator:books-comparison-v1 | none | — | passed |

## 8. Ignored Noise

- Pre-denominator closures=620；逐 family 理由保存在 owner receipt。
- Withdrawn=0；只保留审计 closure，不进入候选、评分、Review 或 Books。
- `updated` / current OAI datestamp 的 revision 噪声不拥有 Daily。

## 9. Recommended Action

本日全部 Gate 已闭合，无进一步动作。

## 10. Repository Changes

- Owner receipt（本阶段只读）：`papers/2026/05/_sources/arxiv-owner-replay-20260903/20260515/arxiv-owner-receipt.json`
- Canonical ledger（Books terminal state）：`papers/2026/05/_sources/arxiv-owner-replay-20260903/20260515/canonical-ledger.json`
- Books queue（fresh-context decision）：`papers/2026/05/_sources/arxiv-owner-replay-20260903/BOOKS_WRITEBACK_QUEUE.json`
- Superseded report：`papers/2026/05/_sources/arxiv-owner-replay-20260903/legacy-reports-before-created-owner-reconciliation/2026-05-15.md`
- Books body: no change for the recovered families on this date.

## 11. Open Questions

- 无。

## 12. Sources

- [DataCite REST API](https://api.datacite.org/dois) — initial `created` owner-day proxy；`updated` 只作 revision provenance。
- [arXiv OAI](https://export.arxiv.org/oai2) — identity/date corroboration；current datestamp 不拥有 first-public day。
- [arXiv](https://arxiv.org/) — exact-v1 abstract、HTML/PDF 与 version history。

## 13. Final Status

Completion Status: Complete; Coverage: Closed; Evidence: Passed; Books: Passed; unresolved findings=0
