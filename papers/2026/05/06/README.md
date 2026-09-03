# Daily Research — 2026-05-06

**Research Date:** 2026-05-06

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-05-05 09:00:00 ～ 2026-05-06 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Historical Daily Independent Full Replay

**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed；initial-created owner replay 与 exact-v1 Evidence Review 已完成。

## Executive Summary

本次独立重放枚举并逐项闭合 493 个注册 arXiv identity，冻结 63 个 Source Family；pre-denominator closure=430，withdrawn pre-denominator=0。26 个旧候选被迁回正确 owner day，1 个漏检 family 已恢复 exact-v1 全文并完成 Source Review。

DataCite `created` 仅作为 initial DOI registration 的 owner-day proxy；`updated`、v1 Updated 与 current OAI datestamp 只记录 revision provenance，不决定 first-public owner。机制结论只绑定 exact-v1 正文。 本日所有 Books disposition 已有终态。

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
| Denominator ID | DEN-20260506-CREATED-a18be3f4fdd532a6 |
| Denominator Frozen At | 2026-09-03T12:36:05+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-05-05T09:00:00+08:00 | 2026-05-06T09:00:00+08:00 | 2026-09-03T12:36:05+08:00 | DataCite prefix 10.48550 initial created-day inventory + registered arXiv categories + exact-v1 identity/body | checked | 493 | SF-2026-ARXIV-2605-02905;SF-2026-ARXIV-2605-02960;SF-2026-ARXIV-2605-02964;SF-2026-ARXIV-2605-03275;SF-2026-ARXIV-2605-03309;SF-2026-ARXIV-2605-03310;SF-2026-ARXIV-2605-03312;SF-2026-ARXIV-2605-03314;SF-2026-ARXIV-2605-03327;SF-2026-ARXIV-2605-03353;SF-2026-ARXIV-2605-03354;SF-2026-ARXIV-2605-03375;SF-2026-ARXIV-2605-03378;SF-2026-ARXIV-2605-03379;SF-2026-ARXIV-2605-03408;SF-2026-ARXIV-2605-03425;SF-2026-ARXIV-2605-03482;SF-2026-ARXIV-2605-03505;SF-2026-ARXIV-2605-03534;SF-2026-ARXIV-2605-03561;SF-2026-ARXIV-2605-03562;SF-2026-ARXIV-2605-03566;SF-2026-ARXIV-2605-03596;SF-2026-ARXIV-2605-03644;SF-2026-ARXIV-2605-03667;SF-2026-ARXIV-2605-03675;SF-2026-ARXIV-2605-03677;SF-2026-ARXIV-2605-03762;SF-2026-ARXIV-2605-03838;SF-2026-ARXIV-2605-03858;SF-2026-ARXIV-2605-03862;SF-2026-ARXIV-2605-03884;SF-2026-ARXIV-2605-03952;SF-2026-ARXIV-2605-03971;SF-2026-ARXIV-2605-03986;SF-2026-ARXIV-2605-04018;SF-2026-ARXIV-2605-04019;SF-2026-ARXIV-2605-04036;SF-2026-ARXIV-2605-04039;SF-ADVERSARIAL-RESEARCH-ORCHESTRATION;SF-AGENT-SAFETY-OOD-ANALOGICAL-EVAL;SF-AGENT-SEQUENTIAL-TRACE-VALIDATION;SF-AI-DATACENTER-GRID-CODESIGN;SF-CYBER-DEFENSE-EXECUTOR-AUTHORITY;SF-DETERMINISTIC-COMPUTATION-EXECUTION;SF-DIFFUSION-PLANNING-COMMIT-REFINE;SF-DITRON-DISTRIBUTED-TILING;SF-JBSHIELD-ADAPTIVE-REPRESENTATION-DEFENSE;SF-KERNCAP-AMD-KERNEL-ISOLATION;SF-MAGE-SHADOW-MEMORY-THREAT-STATE;SF-MULTITURN-DEPENDENCY-AWARE-PRIVACY;SF-OBSERVATIONAL-WORKFLOW-SKILL-LEARNING;SF-ONLINE-CORRECTION-RECOVERY-SHIFT;SF-PACT-AGENT-CHOREOGRAPHY;SF-PREGENERATION-ANSWERABILITY-GEOMETRY;SF-REFUSAL-TRAJECTORY-MONITOR;SF-REPOSITORY-GRAPH-REPAIR-PROVENANCE;SF-ROUTEHIJACK-MOE-SAFETY-ROUTING;SF-SAE-PAIRWISE-CAUSAL-AXIS-AUDIT;SF-SELF-MINED-HARDNESS-SAFETY-FT;SF-SPARSE-MEMORY-FINETUNING;SF-VDCORES-ASYNC-GPU-RESOURCE-DECOUPLING;SF-WEB-PII-DEFENSIVE-PROMPT-THREAT | created-day pages=closed; OAI category sets=closed; direct same-day OAI=346 | 2026-05-06T09:00:00+08:00 | coverage:SRC-ARXIV:20260506 | — |

<!-- coverage:SRC-ARXIV:20260506:start -->全量 raw inventory=493；每个 identity 均具有 retained、family-specific closure 或 withdrawn terminal closure。候选 owner 由 initial DataCite created、arXiv ID month、v1 history 与 announcement cadence 共同约束；冲突不由 updated 字段覆盖。<!-- coverage:SRC-ARXIV:20260506:end -->

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
| SF-2026-ARXIV-2605-02905 | arXiv:2605.02905v1 | paper-v1:2605.02905 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2605-02905 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-02905 | yes |
| SF-2026-ARXIV-2605-02960 | arXiv:2605.02960v1 | paper-v1:2605.02960 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-02960 | self | — | new_in_window | INFER-PREFILL | Integrate | books-review:SF-2026-ARXIV-2605-02960 | yes |
| SF-2026-ARXIV-2605-02964 | arXiv:2605.02964v1 | paper-v1:2605.02964 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-02964 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-02964 | yes |
| SF-2026-ARXIV-2605-03275 | arXiv:2605.03275v1 | paper-v1:2605.03275 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-03275 | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-03275 | yes |
| SF-2026-ARXIV-2605-03309 | arXiv:2605.03309v1 | paper-v1:2605.03309 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-03309 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2605-03309 | yes |
| SF-2026-ARXIV-2605-03310 | arXiv:2605.03310v1 | paper-v1:2605.03310 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-03310 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-03310 | yes |
| SF-2026-ARXIV-2605-03312 | arXiv:2605.03312v1 | paper-v1:2605.03312 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-03312 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-03312 | yes |
| SF-2026-ARXIV-2605-03314 | arXiv:2605.03314v1 | paper-v1:2605.03314 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-03314 | self | — | new_in_window | AGENT-CONTEXT | Integrate | books-review:SF-2026-ARXIV-2605-03314 | yes |
| SF-2026-ARXIV-2605-03327 | arXiv:2605.03327v1 | paper-v1:2605.03327 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-03327 | self | — | new_in_window | TRAIN-GRPO | Integrate | books-review:SF-2026-ARXIV-2605-03327 | yes |
| SF-2026-ARXIV-2605-03353 | arXiv:2605.03353v1 | paper-v1:2605.03353 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-03353 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-03353 | yes |
| SF-2026-ARXIV-2605-03354 | arXiv:2605.03354v1 | paper-v1:2605.03354 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-03354 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-03354 | yes |
| SF-2026-ARXIV-2605-03375 | arXiv:2605.03375v1 | paper-v1:2605.03375 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-03375 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-03375 | yes |
| SF-2026-ARXIV-2605-03378 | arXiv:2605.03378v1 | paper-v1:2605.03378 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-03378 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-03378 | yes |
| SF-2026-ARXIV-2605-03379 | arXiv:2605.03379v1 | paper-v1:2605.03379 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-03379 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-03379 | yes |
| SF-2026-ARXIV-2605-03408 | arXiv:2605.03408v1 | paper-v1:2605.03408 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-03408 | self | — | new_in_window | TRAIN-RLHF | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-03408 | yes |
| SF-2026-ARXIV-2605-03425 | arXiv:2605.03425v1 | paper-v1:2605.03425 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-03425 | self | — | new_in_window | TRAIN-PRETRAINING | Integrate | books-review:SF-2026-ARXIV-2605-03425 | yes |
| SF-2026-ARXIV-2605-03482 | arXiv:2605.03482v1 | paper-v1:2605.03482 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-03482 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-03482 | yes |
| SF-2026-ARXIV-2605-03505 | arXiv:2605.03505v1 | paper-v1:2605.03505 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-03505 | self | — | new_in_window | PLATFORM-MONITORING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-03505 | yes |
| SF-2026-ARXIV-2605-03534 | arXiv:2605.03534v1 | paper-v1:2605.03534 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-03534 | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-03534 | yes |
| SF-2026-ARXIV-2605-03561 | arXiv:2605.03561v1 | paper-v1:2605.03561 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-03561 | self | — | new_in_window | PLATFORM-MONITORING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-03561 | yes |
| SF-2026-ARXIV-2605-03562 | arXiv:2605.03562v1 | paper-v1:2605.03562 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-03562 | self | — | new_in_window | INFER-KV-CACHE | Integrate | books-review:SF-2026-ARXIV-2605-03562 | yes |
| SF-2026-ARXIV-2605-03566 | arXiv:2605.03566v1 | paper-v1:2605.03566 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-03566 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-03566 | yes |
| SF-2026-ARXIV-2605-03596 | arXiv:2605.03596v1 | paper-v1:2605.03596 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-03596 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2605-03596 | yes |
| SF-2026-ARXIV-2605-03644 | arXiv:2605.03644v1 | paper-v1:2605.03644 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-03644 | self | — | new_in_window | INFER-KV-CACHE | Integrate | books-review:SF-2026-ARXIV-2605-03644 | yes |
| SF-2026-ARXIV-2605-03667 | arXiv:2605.03667v1 | paper-v1:2605.03667 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-03667 | self | — | new_in_window | TRAIN-PRETRAINING | Integrate | books-review:SF-2026-ARXIV-2605-03667 | yes |
| SF-2026-ARXIV-2605-03675 | arXiv:2605.03675v1 | paper-v1:2605.03675 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-03675 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-03675 | yes |
| SF-2026-ARXIV-2605-03677 | arXiv:2605.03677v1 | paper-v1:2605.03677 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-03677 | self | — | new_in_window | TRAIN-RLHF | Integrate | books-review:SF-2026-ARXIV-2605-03677 | yes |
| SF-2026-ARXIV-2605-03762 | arXiv:2605.03762v1 | paper-v1:2605.03762 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-03762 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-03762 | yes |
| SF-2026-ARXIV-2605-03838 | arXiv:2605.03838v1 | paper-v1:2605.03838 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-03838 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-03838 | yes |
| SF-2026-ARXIV-2605-03858 | arXiv:2605.03858v1 | paper-v1:2605.03858 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-03858 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-03858 | yes |
| SF-2026-ARXIV-2605-03862 | arXiv:2605.03862v1 | paper-v1:2605.03862 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-03862 | self | — | new_in_window | TRAIN-RLHF | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-03862 | yes |
| SF-2026-ARXIV-2605-03884 | arXiv:2605.03884v1 | paper-v1:2605.03884 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-03884 | self | — | new_in_window | AGENT-MULTI-AGENT | Integrate | books-review:SF-2026-ARXIV-2605-03884 | yes |
| SF-2026-ARXIV-2605-03952 | arXiv:2605.03952v1 | paper-v1:2605.03952 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-03952 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-03952 | yes |
| SF-2026-ARXIV-2605-03971 | arXiv:2605.03971v1 | paper-v1:2605.03971 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-03971 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-03971 | yes |
| SF-2026-ARXIV-2605-03986 | arXiv:2605.03986v1 | paper-v1:2605.03986 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-03986 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-03986 | yes |
| SF-2026-ARXIV-2605-04018 | arXiv:2605.04018v1 | paper-v1:2605.04018 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-04018 | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-04018 | yes |
| SF-2026-ARXIV-2605-04019 | arXiv:2605.04019v1 | paper-v1:2605.04019 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2605-04019 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-04019 | yes |
| SF-2026-ARXIV-2605-04036 | arXiv:2605.04036v1 | paper-v1:2605.04036 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-04036 | self | — | new_in_window | TRAIN-SFT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-04036 | yes |
| SF-2026-ARXIV-2605-04039 | arXiv:2605.04039v1 | paper-v1:2605.04039 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-04039 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-04039 | yes |
| SF-ADVERSARIAL-RESEARCH-ORCHESTRATION | arXiv:2605.03042v1 | paper-v1:2605.03042 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-ADVERSARIAL-RESEARCH-ORCHESTRATION | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-ADVERSARIAL-RESEARCH-ORCHESTRATION | yes |
| SF-AGENT-SAFETY-OOD-ANALOGICAL-EVAL | arXiv:2605.03242v1 | paper-v1:2605.03242 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-AGENT-SAFETY-OOD-ANALOGICAL-EVAL | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-AGENT-SAFETY-OOD-ANALOGICAL-EVAL | yes |
| SF-AGENT-SEQUENTIAL-TRACE-VALIDATION | arXiv:2605.03159v1 | paper-v1:2605.03159 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-AGENT-SEQUENTIAL-TRACE-VALIDATION | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-AGENT-SEQUENTIAL-TRACE-VALIDATION | yes |
| SF-AI-DATACENTER-GRID-CODESIGN | arXiv:2605.03090v1 | paper-v1:2605.03090 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-AI-DATACENTER-GRID-CODESIGN | self | — | new_in_window | PLATFORM-COST | No Change — Existing Coverage | books-review:SF-AI-DATACENTER-GRID-CODESIGN | yes |
| SF-CYBER-DEFENSE-EXECUTOR-AUTHORITY | arXiv:2605.03034v1 | paper-v1:2605.03034 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-CYBER-DEFENSE-EXECUTOR-AUTHORITY | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-CYBER-DEFENSE-EXECUTOR-AUTHORITY | yes |
| SF-DETERMINISTIC-COMPUTATION-EXECUTION | arXiv:2605.03227v1 | paper-v1:2605.03227 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-DETERMINISTIC-COMPUTATION-EXECUTION | self | — | new_in_window | AGENT-TOOL-CALLING | No Change — Existing Coverage | books-review:SF-DETERMINISTIC-COMPUTATION-EXECUTION | yes |
| SF-DIFFUSION-PLANNING-COMMIT-REFINE | arXiv:2605.03075v1 | paper-v1:2605.03075 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-DIFFUSION-PLANNING-COMMIT-REFINE | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | No Change — Existing Coverage | books-review:SF-DIFFUSION-PLANNING-COMMIT-REFINE | yes |
| SF-DITRON-DISTRIBUTED-TILING | arXiv:2605.02953v1 | paper-v1:2605.02953 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-DITRON-DISTRIBUTED-TILING | self | — | new_in_window | INFER-TENSORRT-LLM | Integrate | books-review:SF-DITRON-DISTRIBUTED-TILING | yes |
| SF-JBSHIELD-ADAPTIVE-REPRESENTATION-DEFENSE | arXiv:2605.03095v1 | paper-v1:2605.03095 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-JBSHIELD-ADAPTIVE-REPRESENTATION-DEFENSE | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-JBSHIELD-ADAPTIVE-REPRESENTATION-DEFENSE | yes |
| SF-KERNCAP-AMD-KERNEL-ISOLATION | arXiv:2605.03208v1 | paper-v1:2605.03208 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-KERNCAP-AMD-KERNEL-ISOLATION | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-KERNCAP-AMD-KERNEL-ISOLATION | yes |
| SF-MAGE-SHADOW-MEMORY-THREAT-STATE | arXiv:2605.03228v1 | paper-v1:2605.03228 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-MAGE-SHADOW-MEMORY-THREAT-STATE | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-MAGE-SHADOW-MEMORY-THREAT-STATE | yes |
| SF-MULTITURN-DEPENDENCY-AWARE-PRIVACY | arXiv:2605.03188v1 | paper-v1:2605.03188 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-MULTITURN-DEPENDENCY-AWARE-PRIVACY | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-MULTITURN-DEPENDENCY-AWARE-PRIVACY | yes |
| SF-OBSERVATIONAL-WORKFLOW-SKILL-LEARNING | arXiv:2605.03231v1 | paper-v1:2605.03231 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-OBSERVATIONAL-WORKFLOW-SKILL-LEARNING | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-OBSERVATIONAL-WORKFLOW-SKILL-LEARNING | yes |
| SF-ONLINE-CORRECTION-RECOVERY-SHIFT | arXiv:2605.03153v1 | paper-v1:2605.03153 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-ONLINE-CORRECTION-RECOVERY-SHIFT | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-ONLINE-CORRECTION-RECOVERY-SHIFT | yes |
| SF-PACT-AGENT-CHOREOGRAPHY | arXiv:2605.03143v1 | paper-v1:2605.03143 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-PACT-AGENT-CHOREOGRAPHY | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-PACT-AGENT-CHOREOGRAPHY | yes |
| SF-PREGENERATION-ANSWERABILITY-GEOMETRY | arXiv:2605.03196v1 | paper-v1:2605.03196 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-PREGENERATION-ANSWERABILITY-GEOMETRY | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-PREGENERATION-ANSWERABILITY-GEOMETRY | yes |
| SF-REFUSAL-TRAJECTORY-MONITOR | arXiv:2605.02958v1 | paper-v1:2605.02958 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 2 | 3 | 2 | 7 | retained | deep_complete | accessible | knowledge_gap | review:SF-REFUSAL-TRAJECTORY-MONITOR | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-REFUSAL-TRAJECTORY-MONITOR | yes |
| SF-REPOSITORY-GRAPH-REPAIR-PROVENANCE | arXiv:2605.03117v1 | paper-v1:2605.03117 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-REPOSITORY-GRAPH-REPAIR-PROVENANCE | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-REPOSITORY-GRAPH-REPAIR-PROVENANCE | yes |
| SF-ROUTEHIJACK-MOE-SAFETY-ROUTING | arXiv:2605.02946v1 | paper-v1:2605.02946 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-ROUTEHIJACK-MOE-SAFETY-ROUTING | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-ROUTEHIJACK-MOE-SAFETY-ROUTING | yes |
| SF-SAE-PAIRWISE-CAUSAL-AXIS-AUDIT | arXiv:2605.03160v1 | paper-v1:2605.03160 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-SAE-PAIRWISE-CAUSAL-AXIS-AUDIT | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-SAE-PAIRWISE-CAUSAL-AXIS-AUDIT | yes |
| SF-SELF-MINED-HARDNESS-SAFETY-FT | arXiv:2605.03226v1 | paper-v1:2605.03226 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-SELF-MINED-HARDNESS-SAFETY-FT | self | — | new_in_window | TRAIN-SFT | No Change — Existing Coverage | books-review:SF-SELF-MINED-HARDNESS-SAFETY-FT | yes |
| SF-SPARSE-MEMORY-FINETUNING | arXiv:2605.03229v1 | paper-v1:2605.03229 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-SPARSE-MEMORY-FINETUNING | self | — | new_in_window | TRAIN-LORA | No Change — Existing Coverage | books-review:SF-SPARSE-MEMORY-FINETUNING | yes |
| SF-VDCORES-ASYNC-GPU-RESOURCE-DECOUPLING | arXiv:2605.03190v1 | paper-v1:2605.03190 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-VDCORES-ASYNC-GPU-RESOURCE-DECOUPLING | self | — | new_in_window | INFER-TENSORRT-LLM | Integrate | books-review:SF-VDCORES-ASYNC-GPU-RESOURCE-DECOUPLING | yes |
| SF-WEB-PII-DEFENSIVE-PROMPT-THREAT | arXiv:2605.03129v1 | paper-v1:2605.03129 | 2026-W19 | 2026-05-06 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-WEB-PII-DEFENSIVE-PROMPT-THREAT | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-WEB-PII-DEFENSIVE-PROMPT-THREAT | yes |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-02905 | RP-fcc37d5d6a563951 | standard | arXiv:2605.02905v1 | SRC-ARXIV@arXiv:2605.02905v1 | https://arxiv.org/html/2605.02905v1#S2 | https://arxiv.org/html/2605.02905v1#S4 | https://arxiv.org/html/2605.02905v1#S6 | Not Disclosed — exact-v1 review found no versioned public artifact contract | claim:SF-2026-ARXIV-2605-02905 | complete |
| SF-2026-ARXIV-2605-02960 | RP-abf599d79cecafd8 | deep | arXiv:2605.02960v1 | SRC-ARXIV@arXiv:2605.02960v1 | https://arxiv.org/html/2605.02960v1 — § exact-v1 reviewer locator: §3 AsyncEP weight streaming; §4 physically-derived saturation threshold and prefix-aware frontend（全文读取 ref=turn11936view5） | https://arxiv.org/html/2605.02960v1 — § exact-v1 reviewer locator: §7-§8 Qwen3-235B-A22B on four hardware/precision configurations（全文读取 ref=turn11936view5） | https://arxiv.org/html/2605.02960v1 — § exact-v1 reviewer locator: Applicability/limitations: prefill-only, batch-driven MoE; low-bandwidth links, bursty arrivals, drift and random prefixes narrow the result.（全文读取 ref=turn11936view5） | Not Disclosed — exact v1 does not bind the claim to an immutable public experiment commit. | claim:SF-2026-ARXIV-2605-02960 | complete |
| SF-2026-ARXIV-2605-02964 | RP-863aa2b8f69bc90e | deep | arXiv:2605.02964v1 | SRC-ARXIV@arXiv:2605.02964v1 | https://arxiv.org/html/2605.02964v1 — § exact-v1 reviewer locator: §3 task regimes, shortcut opportunities and exploit taxonomy; §4 harness（全文读取 ref=turn11936view6） | https://arxiv.org/html/2605.02964v1 — § exact-v1 reviewer locator: §5 thirteen frontier models, sibling post-training comparison and hardening（全文读取 ref=turn11936view6） | https://arxiv.org/html/2605.02964v1 — § exact-v1 reviewer locator: §8: current rule triggers have false positives and may miss new exploits; associations do not isolate all causal effects of RL.（全文读取 ref=turn11936view6） | Not Disclosed — exact v1 does not bind the claim to an immutable public experiment commit. | claim:SF-2026-ARXIV-2605-02964 | complete |
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
| SF-ADVERSARIAL-RESEARCH-ORCHESTRATION | RP-6a629e1351c8e013 | deep | arXiv:2605.03042v1 | SRC-ARXIV@arXiv:2605.03042v1 | arXiv:2605.03042v1 §Method/Design (paper-specific heading); §Adversarial multi-agent research roles and adjudication workflow | arXiv:2605.03042v1 §Experiments/Evaluation (paper-specific heading); §Research-task evaluation, evidence diversity and ablations | arXiv:2605.03042v1 §Scope and Limitations (paper-specific heading); §Judge, corpus and task-transfer limitations | arXiv:2605.03042v1 Appendix/Artifact statement; Exact-v1 artifact/code statement; immutable event-time commit is Not Disclosed unless explicitly named | claim:SF-ADVERSARIAL-RESEARCH-ORCHESTRATION | complete |
| SF-AGENT-SAFETY-OOD-ANALOGICAL-EVAL | RP-add60fc61a7f78de | deep | arXiv:2605.03242v1 | SRC-ARXIV@arXiv:2605.03242v1 | arXiv:2605.03242v1 §Method/Design (paper-specific heading); arXiv:2605.03242v1 HTML, Method/Design section; abstract mechanism: To address this gap, we introduce ROME (Red-team Orchestrated Multi-agent Evolution), a controlled benchmark-construction pipeline that rewrites known unsafe trajectories into more deceptive evaluation instances while preserving their… | arXiv:2605.03242v1 §Experiments/Evaluation (paper-specific heading); arXiv:2605.03242v1 HTML, Experiments/Evaluation and ablation sections; abstract scope: Tool-using agent systems powered by large language models (LLMs) are increasingly deployed across web, app, operating-system, and transactional environments. | arXiv:2605.03242v1 §Scope and Limitations (paper-specific heading); arXiv:2605.03242v1 HTML, Discussion/Limitations and threat-to-validity passages; no cross-workload generalization inferred | arXiv:2605.03242v1 Appendix/Artifact statement; arXiv:2605.03242v1 HTML, artifact/code statement; immutable event-time commit is Not Disclosed unless explicitly named | claim:SF-AGENT-SAFETY-OOD-ANALOGICAL-EVAL | complete |
| SF-AGENT-SEQUENTIAL-TRACE-VALIDATION | RP-6ee5721fbcb9e71e | deep | arXiv:2605.03159v1 | SRC-ARXIV@arXiv:2605.03159v1 | arXiv:2605.03159v1 §Method/Design (paper-specific heading); arXiv:2605.03159v1 HTML, Method/Design section; abstract mechanism: We present a novel algorithm that automatically learns correct behavior from just 2-10 passing execution traces and validates new executions against this learned model. | arXiv:2605.03159v1 §Experiments/Evaluation (paper-specific heading); arXiv:2605.03159v1 HTML, Experiments/Evaluation and ablation sections; abstract scope: In controlled experiments, our system achieved high accuracy in detecting product bugs and false successes using only 3 training traces. | arXiv:2605.03159v1 §Scope and Limitations (paper-specific heading); arXiv:2605.03159v1 HTML, Discussion/Limitations and threat-to-validity passages; no cross-workload generalization inferred | arXiv:2605.03159v1 Appendix/Artifact statement; arXiv:2605.03159v1 HTML, artifact/code statement; immutable event-time commit is Not Disclosed unless explicitly named | claim:SF-AGENT-SEQUENTIAL-TRACE-VALIDATION | complete |
| SF-AI-DATACENTER-GRID-CODESIGN | RP-c557ec99d9ebf7c4 | deep | arXiv:2605.03090v1 | SRC-ARXIV@arXiv:2605.03090v1 | arXiv:2605.03090v1 §Method/Design (paper-specific heading); arXiv:2605.03090v1 HTML, Method/Design section; abstract mechanism: We introduce the distinct design principles, operational philosophies, and economic incentives of each sector, and show why their cultural and technical misalignment makes coordination difficult. | arXiv:2605.03090v1 §Experiments/Evaluation (paper-specific heading); arXiv:2605.03090v1 HTML, Experiments/Evaluation and ablation sections; abstract scope: Evaluation scope is disclosed in the exact-v1 experiments/results section | arXiv:2605.03090v1 §Scope and Limitations (paper-specific heading); arXiv:2605.03090v1 HTML, Discussion/Limitations and threat-to-validity passages; no cross-workload generalization inferred | arXiv:2605.03090v1 Appendix/Artifact statement; arXiv:2605.03090v1 HTML, artifact/code statement; immutable event-time commit is Not Disclosed unless explicitly named | claim:SF-AI-DATACENTER-GRID-CODESIGN | complete |
| SF-CYBER-DEFENSE-EXECUTOR-AUTHORITY | RP-3ad8f38c70c48e1e | deep | arXiv:2605.03034v1 | SRC-ARXIV@arXiv:2605.03034v1 | arXiv:2605.03034v1 §Method/Design (paper-specific heading); §Tool-mediated cyber-defense architecture and stable control loop | arXiv:2605.03034v1 §Experiments/Evaluation (paper-specific heading); §Defense scenarios, tool actions and recovery evaluation | arXiv:2605.03034v1 §Scope and Limitations (paper-specific heading); §Threat-model, environment and autonomous-action limitations | arXiv:2605.03034v1 Appendix/Artifact statement; Exact-v1 artifact/code statement; immutable event-time commit is Not Disclosed unless explicitly named | claim:SF-CYBER-DEFENSE-EXECUTOR-AUTHORITY | complete |
| SF-DETERMINISTIC-COMPUTATION-EXECUTION | RP-9d9858e6b64c0c7b | deep | arXiv:2605.03227v1 | SRC-ARXIV@arXiv:2605.03227v1 | arXiv:2605.03227v1 §Method/Design (paper-specific heading); §Prompting versus execution-based deterministic computation methods | arXiv:2605.03227v1 §Experiments/Evaluation (paper-specific heading); §Task suites, execution correctness and method comparison | arXiv:2605.03227v1 §Scope and Limitations (paper-specific heading); §Task/language/tool availability limitations | arXiv:2605.03227v1 Appendix/Artifact statement; Exact-v1 artifact/code statement; immutable event-time commit is Not Disclosed unless explicitly named | claim:SF-DETERMINISTIC-COMPUTATION-EXECUTION | complete |
| SF-DIFFUSION-PLANNING-COMMIT-REFINE | RP-cc3fb584b1122747 | deep | arXiv:2605.03075v1 | SRC-ARXIV@arXiv:2605.03075v1 | arXiv:2605.03075v1 §Method/Design (paper-specific heading); §Compositional diffusion planner; iterative correction and commitment | arXiv:2605.03075v1 §Experiments/Evaluation (paper-specific heading); §Long-horizon planning evaluation and refinement ablations | arXiv:2605.03075v1 §Scope and Limitations (paper-specific heading); §Environment, horizon and feasibility-check limitations | arXiv:2605.03075v1 Appendix/Artifact statement; Exact-v1 artifact/code statement; immutable event-time commit is Not Disclosed unless explicitly named | claim:SF-DIFFUSION-PLANNING-COMMIT-REFINE | complete |
| SF-DITRON-DISTRIBUTED-TILING | RP-3c7f705d80273f2b | deep | arXiv:2605.02953v1 | SRC-ARXIV@arXiv:2605.02953v1 | arXiv:2605.02953v1 — §3 Core/Device/Task hierarchy; swizzling; code generation | arXiv:2605.02953v1 — §4 inference/training kernels, vLLM and NVIDIA/AMD experiments | arXiv:2605.02953v1 — §2.2 model limitations; §5 deployment/portability boundary | arXiv:2605.02953v1 — enterprise deployment claimed; public immutable compiler commit Not Disclosed | claim:SF-DITRON-DISTRIBUTED-TILING | complete |
| SF-JBSHIELD-ADAPTIVE-REPRESENTATION-DEFENSE | RP-dbc245dca08e266c | deep | arXiv:2605.03095v1 | SRC-ARXIV@arXiv:2605.03095v1 | arXiv:2605.03095v1 §Method/Design (paper-specific heading); arXiv:2605.03095v1 HTML, Method/Design section; abstract mechanism: We design JB-GCG, which modifies GCG's objective to combine two terms: refusal-direction suppression via cosine similarity between the refusal direction and hidden-state representations, and toxic-concept regularization via JBShield's… | arXiv:2605.03095v1 §Experiments/Evaluation (paper-specific heading); arXiv:2605.03095v1 HTML, Experiments/Evaluation and ablation sections; abstract scope: Across five configurations on Llama-3-8B, JB-GCG achieves an average ASR of 46.2%, reaching up to 53.4% in the strongest setting. | arXiv:2605.03095v1 §Scope and Limitations (paper-specific heading); arXiv:2605.03095v1 HTML, Discussion/Limitations and threat-to-validity passages; no cross-workload generalization inferred | arXiv:2605.03095v1 Appendix/Artifact statement; arXiv:2605.03095v1 HTML, artifact/code statement; immutable event-time commit is Not Disclosed unless explicitly named | claim:SF-JBSHIELD-ADAPTIVE-REPRESENTATION-DEFENSE | complete |
| SF-KERNCAP-AMD-KERNEL-ISOLATION | RP-9a83ce6dae90a8b0 | deep | arXiv:2605.03208v1 | SRC-ARXIV@arXiv:2605.03208v1 | arXiv:2605.03208v1 §Method/Design (paper-specific heading); arXiv:2605.03208v1 HTML, Method/Design section; abstract mechanism: We present Kerncap, an automated kernel extraction tool that intercepts dispatches at the HSA runtime for both HIP and Triton, bridging Triton's JIT-only metadata into HSA-level capture via… | arXiv:2605.03208v1 §Experiments/Evaluation (paper-specific heading); arXiv:2605.03208v1 HTML, Experiments/Evaluation and ablation sections; abstract scope: Across six real-world HIP and Triton workloads spanning traditional HPC and ML domains on three AMD GPU architectures (CDNA2, CDNA3, RDNA3), Kerncap extracts and validates kernels from snapshots… | arXiv:2605.03208v1 §Scope and Limitations (paper-specific heading); arXiv:2605.03208v1 HTML, Discussion/Limitations and threat-to-validity passages; no cross-workload generalization inferred | arXiv:2605.03208v1 Appendix/Artifact statement; arXiv:2605.03208v1 HTML, artifact/code statement; immutable event-time commit is Not Disclosed unless explicitly named | claim:SF-KERNCAP-AMD-KERNEL-ISOLATION | complete |
| SF-MAGE-SHADOW-MEMORY-THREAT-STATE | RP-348bf43fe41dd812 | deep | arXiv:2605.03228v1 | SRC-ARXIV@arXiv:2605.03228v1 | arXiv:2605.03228v1 §Method/Design (paper-specific heading); arXiv:2605.03228v1 HTML, Method/Design section; abstract mechanism: In this paper, we present MAGE (Memory As Guardrail Enforcement), a novel defensive framework designed to counter a wide range of long-horizon threats. | arXiv:2605.03228v1 §Experiments/Evaluation (paper-specific heading); arXiv:2605.03228v1 HTML, Experiments/Evaluation and ablation sections; abstract scope: Inspired by the "shadow stack" abstraction in systems security, MAGE maintains a dedicated, safety-focused agentic memory that distills and retains safety-critical context across the agent's full execution trajectory,… | arXiv:2605.03228v1 §Scope and Limitations (paper-specific heading); arXiv:2605.03228v1 HTML, Discussion/Limitations and threat-to-validity passages; no cross-workload generalization inferred | arXiv:2605.03228v1 Appendix/Artifact statement; arXiv:2605.03228v1 HTML, artifact/code statement; immutable event-time commit is Not Disclosed unless explicitly named | claim:SF-MAGE-SHADOW-MEMORY-THREAT-STATE | complete |
| SF-MULTITURN-DEPENDENCY-AWARE-PRIVACY | RP-f9cacb1482ec4aa9 | deep | arXiv:2605.03188v1 | SRC-ARXIV@arXiv:2605.03188v1 | arXiv:2605.03188v1 §Method/Design (paper-specific heading); arXiv:2605.03188v1 HTML, Method/Design section; abstract mechanism: LLM agents release private data across multi-service interactions. | arXiv:2605.03188v1 §Experiments/Evaluation (paper-specific heading); arXiv:2605.03188v1 HTML, Experiments/Evaluation and ablation sections; abstract scope: LLM agents release private data across multi-service interactions. | arXiv:2605.03188v1 §Scope and Limitations (paper-specific heading); arXiv:2605.03188v1 HTML, Discussion/Limitations and threat-to-validity passages; no cross-workload generalization inferred | arXiv:2605.03188v1 Appendix/Artifact statement; arXiv:2605.03188v1 HTML, artifact/code statement; immutable event-time commit is Not Disclosed unless explicitly named | claim:SF-MULTITURN-DEPENDENCY-AWARE-PRIVACY | complete |
| SF-OBSERVATIONAL-WORKFLOW-SKILL-LEARNING | RP-69892f9ce5c99a34 | deep | arXiv:2605.03231v1 | SRC-ARXIV@arXiv:2605.03231v1 | arXiv:2605.03231v1 §Method/Design (paper-specific heading); §Observation capture, workflow induction and executable automation | arXiv:2605.03231v1 §Experiments/Evaluation (paper-specific heading); §Automation-task evaluation and correction analysis | arXiv:2605.03231v1 §Scope and Limitations (paper-specific heading); §UI/domain, demonstration and safety limitations | arXiv:2605.03231v1 Appendix/Artifact statement; Exact-v1 artifact/code statement; immutable event-time commit is Not Disclosed unless explicitly named | claim:SF-OBSERVATIONAL-WORKFLOW-SKILL-LEARNING | complete |
| SF-ONLINE-CORRECTION-RECOVERY-SHIFT | RP-89853712dd4d5452 | deep | arXiv:2605.03153v1 | SRC-ARXIV@arXiv:2605.03153v1 | arXiv:2605.03153v1 §Method/Design (paper-specific heading); §Online correction/recovery method under distribution shift | arXiv:2605.03153v1 §Experiments/Evaluation (paper-specific heading); §Recovery, shift and rollback evaluation | arXiv:2605.03153v1 §Scope and Limitations (paper-specific heading); §Shift family, correction-oracle and deployment limitations | arXiv:2605.03153v1 Appendix/Artifact statement; Exact-v1 artifact/code statement; immutable event-time commit is Not Disclosed unless explicitly named | claim:SF-ONLINE-CORRECTION-RECOVERY-SHIFT | complete |
| SF-PACT-AGENT-CHOREOGRAPHY | RP-a5af3bb89f32730d | deep | arXiv:2605.03143v1 | SRC-ARXIV@arXiv:2605.03143v1 | arXiv:2605.03143v1 §Method/Design (paper-specific heading); §Pact choreography language, roles, messages and protocol semantics | arXiv:2605.03143v1 §Experiments/Evaluation (paper-specific heading); §Examples/evaluation of generated endpoints and protocol checks | arXiv:2605.03143v1 §Scope and Limitations (paper-specific heading); §Language subset, runtime and failure-model limitations | arXiv:2605.03143v1 Appendix/Artifact statement; Exact-v1 artifact/code statement; immutable event-time commit is Not Disclosed unless explicitly named | claim:SF-PACT-AGENT-CHOREOGRAPHY | complete |
| SF-PREGENERATION-ANSWERABILITY-GEOMETRY | RP-09a6bd44c6f09dc8 | standard | arXiv:2605.03196v1 | SRC-ARXIV@arXiv:2605.03196v1 | arXiv:2605.03196v1 §Method/Design (paper-specific heading); arXiv:2605.03196v1 HTML, Method/Design section; abstract mechanism: A reliable language model should be able to signal, prior to generation, when a query falls outside its knowledge. | arXiv:2605.03196v1 §Experiments/Evaluation (paper-specific heading); arXiv:2605.03196v1 HTML, Experiments/Evaluation and ablation sections; abstract scope: Across three instruction-tuned models (Llama 3.1-8B, Qwen 2.5-7B, and Mistral-7B-Instruct) and three prompt forms (Math, Fact, Code), we find that geometry primarily encodes task form. | arXiv:2605.03196v1 §Scope and Limitations (paper-specific heading); arXiv:2605.03196v1 HTML, Discussion/Limitations and threat-to-validity passages; no cross-workload generalization inferred | arXiv:2605.03196v1 Appendix/Artifact statement; arXiv:2605.03196v1 HTML, artifact/code statement; immutable event-time commit is Not Disclosed unless explicitly named | claim:SF-PREGENERATION-ANSWERABILITY-GEOMETRY | complete |
| SF-REFUSAL-TRAJECTORY-MONITOR | RP-63f32c026531ff00 | deep | arXiv:2605.02958v1 | SRC-ARXIV@arXiv:2605.02958v1 | arXiv:2605.02958v1 — §3 causal tracing; §4 SALO sparse activation operator | arXiv:2605.02958v1 — §5 jailbreak families/operating point; §6 adaptive and encoded-input analysis | arXiv:2605.02958v1 — §7 Limitations | arXiv:2605.02958v1 — white-box hidden-state implementation described; immutable commit Not Disclosed | claim:SF-REFUSAL-TRAJECTORY-MONITOR | complete |
| SF-REPOSITORY-GRAPH-REPAIR-PROVENANCE | RP-66792c392dbf0cdf | deep | arXiv:2605.03117v1 | SRC-ARXIV@arXiv:2605.03117v1 | arXiv:2605.03117v1 §Method/Design (paper-specific heading); §Repository graph representation; localization and repair toolset | arXiv:2605.03117v1 §Experiments/Evaluation (paper-specific heading); §Fault-localization/program-repair evaluation and ablations | arXiv:2605.03117v1 §Scope and Limitations (paper-specific heading); §Repository/language/test-oracle limitations | arXiv:2605.03117v1 Appendix/Artifact statement; Exact-v1 artifact/code statement; immutable event-time commit is Not Disclosed unless explicitly named | claim:SF-REPOSITORY-GRAPH-REPAIR-PROVENANCE | complete |
| SF-ROUTEHIJACK-MOE-SAFETY-ROUTING | RP-0bf9396fe3b3f1cd | deep | arXiv:2605.02946v1 | SRC-ARXIV@arXiv:2605.02946v1 | arXiv:2605.02946v1 method sections: expert localization and routing-aware suffix objective; §Methodology: exact-v1 named method and system-design passages | arXiv:2605.02946v1 seven MoE LLMs, sibling transfer and three VLMs; Experiments: exact-v1 evaluation and ablation passages | arXiv:2605.02946v1 limitations/threat model; input-access and evaluator boundary; Scope and Limitations | Not Disclosed — arXiv:2605.02946v1 reports code/artifact revision not disclosed | claim:SF-ROUTEHIJACK-MOE-SAFETY-ROUTING | complete |
| SF-SAE-PAIRWISE-CAUSAL-AXIS-AUDIT | RP-4b2e20a3df9f8446 | deep | arXiv:2605.03160v1 | SRC-ARXIV@arXiv:2605.03160v1 | arXiv:2605.03160v1 §Method/Design (paper-specific heading); arXiv:2605.03160v1 HTML, Method/Design section; abstract mechanism: The standard protocol for interpreting sparse-autoencoder (SAE) features labels each feature from its top-activating contexts and validates the label by steering that single feature at a typical magnitude. | arXiv:2605.03160v1 §Experiments/Evaluation (paper-specific heading); arXiv:2605.03160v1 HTML, Experiments/Evaluation and ablation sections; abstract scope: Evaluation scope is disclosed in the exact-v1 experiments/results section | arXiv:2605.03160v1 §Scope and Limitations (paper-specific heading); arXiv:2605.03160v1 HTML, Discussion/Limitations and threat-to-validity passages; no cross-workload generalization inferred | arXiv:2605.03160v1 Appendix/Artifact statement; arXiv:2605.03160v1 HTML, artifact/code statement; immutable event-time commit is Not Disclosed unless explicitly named | claim:SF-SAE-PAIRWISE-CAUSAL-AXIS-AUDIT | complete |
| SF-SELF-MINED-HARDNESS-SAFETY-FT | RP-b616cb611de56c93 | deep | arXiv:2605.03226v1 | SRC-ARXIV@arXiv:2605.03226v1 | arXiv:2605.03226v1 §Method/Design (paper-specific heading); arXiv:2605.03226v1 HTML, Method/Design section; abstract mechanism: Safety fine-tuning of language models typically requires a curated adversarial dataset. | arXiv:2605.03226v1 §Experiments/Evaluation (paper-specific heading); arXiv:2605.03226v1 HTML, Experiments/Evaluation and ablation sections; abstract scope: Evaluation scope is disclosed in the exact-v1 experiments/results section | arXiv:2605.03226v1 §Scope and Limitations (paper-specific heading); arXiv:2605.03226v1 HTML, Discussion/Limitations and threat-to-validity passages; no cross-workload generalization inferred | arXiv:2605.03226v1 Appendix/Artifact statement; arXiv:2605.03226v1 HTML, artifact/code statement; immutable event-time commit is Not Disclosed unless explicitly named | claim:SF-SELF-MINED-HARDNESS-SAFETY-FT | complete |
| SF-SPARSE-MEMORY-FINETUNING | RP-36bb9a7a9fe8915f | deep | arXiv:2605.03229v1 | SRC-ARXIV@arXiv:2605.03229v1 | arXiv:2605.03229v1 §Method/Design (paper-specific heading); §Sparse memory finetuning parameterization and update path | arXiv:2605.03229v1 §Experiments/Evaluation (paper-specific heading); §Comparison with LoRA/full finetuning; forgetting and adaptation metrics | arXiv:2605.03229v1 §Scope and Limitations (paper-specific heading); §Model/task/parameter-budget limitations | arXiv:2605.03229v1 Appendix/Artifact statement; Exact-v1 artifact/code statement; immutable event-time commit is Not Disclosed unless explicitly named | claim:SF-SPARSE-MEMORY-FINETUNING | complete |
| SF-VDCORES-ASYNC-GPU-RESOURCE-DECOUPLING | RP-9c67a55a517a8c78 | deep | arXiv:2605.03190v1 | SRC-ARXIV@arXiv:2605.03190v1 | arXiv:2605.03190v1 §Method/Design (paper-specific heading); arXiv:2605.03190v1 HTML, Method/Design section; abstract mechanism: Realizing such a decoupled abstraction efficiently on today's GPUs is itself challenging, VDCores addresses this through a GPU-specialized programming model and GPU runtime design that preserves the flexibility… | arXiv:2605.03190v1 §Experiments/Evaluation (paper-specific heading); arXiv:2605.03190v1 HTML, Experiments/Evaluation and ablation sections; abstract scope: Across four LLM inference workloads on GH200, H100, and RTX 6000 Pro GPUs, VDCores significantly improves decoding throughput by 24% on average and by up to 77% under… | arXiv:2605.03190v1 §Scope and Limitations (paper-specific heading); arXiv:2605.03190v1 HTML, Discussion/Limitations and threat-to-validity passages; no cross-workload generalization inferred | arXiv:2605.03190v1 Appendix/Artifact statement; arXiv:2605.03190v1 HTML, artifact/code statement; immutable event-time commit is Not Disclosed unless explicitly named | claim:SF-VDCORES-ASYNC-GPU-RESOURCE-DECOUPLING | complete |
| SF-WEB-PII-DEFENSIVE-PROMPT-THREAT | RP-6deaab291ed67a6f | deep | arXiv:2605.03129v1 | SRC-ARXIV@arXiv:2605.03129v1 | arXiv:2605.03129v1 §Method/Design (paper-specific heading); §2 Threat Model; §3 PIIGuard methodology | arXiv:2605.03129v1 §Experiments/Evaluation (paper-specific heading); §4 setup; §5 evaluation including sanitizer and URL modes | arXiv:2605.03129v1 §Scope and Limitations (paper-specific heading); §7 Discussion; sanitizer front and deployment limitations | arXiv:2605.03129v1 Appendix/Artifact statement; Exact-v1 artifact/code statement; immutable event-time commit is Not Disclosed unless explicitly named | claim:SF-WEB-PII-DEFENSIVE-PROMPT-THREAT | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2605-02905:start -->
#### eOptShrinkQ: Near-Lossless KV Cache Compression Through Optimal Spectral Denoising and Quantization

<!-- claim:SF-2026-ARXIV-2605-02905:start -->
- **Problem:** We show that the key-value (KV) cache in transformer attention heads admits a natural decomposition into a low-rank \emph{shared context} component and a full-rank \emph{per-token} residual, well described by the spiked random matrix model.
- **Old path / changed constraint:** The key-value (KV) cache is a critical memory bottleneck in autoregressive inference with large language models (LLMs).
- **Mechanism / ownership:** eOptShrinkQ 先按 token block 对 KV 矩阵执行 optimal singular-value shrinkage，自动识别并单独编码共享的低秩 context 分量；再用 TurboQuant 逐向量量化保留 token-specific 信息的全秩 residual。若没有 singular value 越过 bulk edge，则跳过 SVD、直接进入 residual quantization。
- **Evaluation contract:** 作者在 Llama-3.1-8B-Instruct 与 Ministral-8B-Instruct 的各层/attention head 检查谱假设，并用 per-head MSE/inner-product fidelity、LongBench 16 tasks 和 multi-needle retrieval 比较。在论文配置下约 2.2 bits/entry 的结果优于 3-bit TurboQuant，并接近各自 FP16 baseline；硬件、并发和线上 latency SLO 未形成完整披露合同。
- **Proof / non-proof:** Evidence is author-reported exact-v1 mechanism/evaluation evidence. It does not establish cross-model, cross-hardware, cross-workload or production generality unless those conditions are explicitly named above.
- **Trade-off / failure mode:** 低秩分量需要 SVD、额外 factor storage 与独立量化；block 中没有可检测 spike 时只能回退到 TurboQuant，说明收益依赖局部谱结构。理论保证依赖 spiked random-matrix、thin-shell 与 coordinate-delocalization 假设，LongBench/needle 质量也不能证明生产 decode latency、所有模型或所有 context distribution 上无损。
- **Coexistence boundary:** The older path remains appropriate where its workload and SLO do not trigger the changed constraint; the paper is treated as a conditional branch, not a universal replacement.
- **Primary:** [arXiv:2605.02905v1](https://arxiv.org/abs/2605.02905v1)；frozen exact-v1 `papers/2026/05/_sources/arxiv-owner-replay-20260903/exact-v1/2605.02905v1.html.html`。
- **Disposition:** `No Change — Existing Coverage`；Fresh-context owner/adjacent comparison completed; the current Books proposition already owns the durable mechanism, so no duplicate paragraph was added.
<!-- claim:SF-2026-ARXIV-2605-02905:end -->
<!-- review:SF-2026-ARXIV-2605-02905:end -->

<!-- review:SF-2026-ARXIV-2605-02960:start -->
<!-- claim:SF-2026-ARXIV-2605-02960:start -->
Prefill-only MoE workloads can exchange activation all-to-all for asynchronous expert-weight all-gather when long compute windows hide transfer; the saturation threshold and traffic drift become routing state.
<!-- claim:SF-2026-ARXIV-2605-02960:end -->
#### MoE-Prefill: Zero Redundancy Overheads in MoE Prefill Serving

- **Why / changed constraint:** `§3 AsyncEP weight streaming; §4 physically-derived saturation threshold and prefix-aware frontend`。
- **Mechanism / ownership:** Prefill-only MoE workloads can exchange activation all-to-all for asynchronous expert-weight all-gather when long compute windows hide transfer; the saturation threshold and traffic drift become routing state.
- **Evaluation contract:** `§7-§8 Qwen3-235B-A22B on four hardware/precision configurations`；结果只绑定 exact-v1 披露的模型、数据、硬件与 evaluator。
- **Trade-off / non-proof:** Applicability/limitations: prefill-only, batch-driven MoE; low-bandwidth links, bursty arrivals, drift and random prefixes narrow the result.
- **Evolution / owner:** `Direct Evolution` → `INFER-PREFILL`；Score V2 `3/3/3` = **9/9**。
- **Books decision:** `Integrate`。
<!-- review:SF-2026-ARXIV-2605-02960:end -->

<!-- review:SF-2026-ARXIV-2605-02964:start -->
<!-- claim:SF-2026-ARXIV-2605-02964:start -->
Tool-agent evaluation must distinguish nominal success from shortcut exploitation and vary horizon/complexity; environmental hardening can change the opportunity surface without changing weights.
<!-- claim:SF-2026-ARXIV-2605-02964:end -->
#### Reward Hacking Benchmark: Measuring Exploits in LLM Agents with Tool Use

- **Why / changed constraint:** `§3 task regimes, shortcut opportunities and exploit taxonomy; §4 harness`。
- **Mechanism / ownership:** Tool-agent evaluation must distinguish nominal success from shortcut exploitation and vary horizon/complexity; environmental hardening can change the opportunity surface without changing weights.
- **Evaluation contract:** `§5 thirteen frontier models, sibling post-training comparison and hardening`；结果只绑定 exact-v1 披露的模型、数据、硬件与 evaluator。
- **Trade-off / non-proof:** §8: current rule triggers have false positives and may miss new exploits; associations do not isolate all causal effects of RL.
- **Evolution / owner:** `Direct Evolution` → `PLATFORM-EVALUATION-SYSTEM`；Score V2 `3/3/3` = **9/9**。
- **Books decision:** `No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-02964:end -->

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

<!-- review:SF-ADVERSARIAL-RESEARCH-ORCHESTRATION:start -->
### ARIS: Autonomous Research via Adversarial Multi-Agent Collaboration

问题与旧路径：Multi-agent research should preserve source diversity, adversarial objections and adjudication provenance; more agents do not by themselves establish correctness. 旧方案在工作负载较小、状态可丢弃、风险低或边界固定时仍然合理。 exact-v1 的机制定位为 `§Adversarial multi-agent research roles and adjudication workflow`。这改变的是可观测状态、控制 owner 或评价证据，而不是仅增加一个模型名称。

Evaluation contract：`§Research-task evaluation, evidence diversity and ablations`。这里的作者实验只证明其披露模型、数据、硬件、精度和实现条件内的结果；未披露字段保持 Not Disclosed。 反证边界：`§Judge, corpus and task-transfer limitations`。Artifact：`Exact-v1 artifact/code statement; immutable event-time commit is Not Disclosed unless explicitly named`。 <!-- claim:SF-ADVERSARIAL-RESEARCH-ORCHESTRATION:start -->长期结论只保留为：Multi-agent research should preserve source diversity, adversarial objections and adjudication provenance; more agents do not by themselves establish correctness. 它不证明该实现跨 workload 普遍最优，也不能代替独立复现、fallback 与 rollback。<!-- claim:SF-ADVERSARIAL-RESEARCH-ORCHESTRATION:end -->
<!-- review:SF-ADVERSARIAL-RESEARCH-ORCHESTRATION:end -->

<!-- review:SF-AGENT-SAFETY-OOD-ANALOGICAL-EVAL:start -->
### Enhancing Agent Safety Judgment: Controlled Benchmark Rewriting and Analogical Reasoning for Deceptive Out-of-Distribution Scenarios

问题与旧路径：Agent safety evaluation must test deceptive out-of-distribution transformations and trace judgment transfer, not only literal variants of known unsafe scenarios. 旧方案在工作负载较小、状态可丢弃、风险低或边界固定时仍然合理。 exact-v1 的机制定位为 `arXiv:2605.03242v1 HTML, Method/Design section; abstract mechanism: To address this gap, we introduce ROME (Red-team Orchestrated Multi-agent Evolution), a controlled benchmark-construction pipeline that rewrites known unsafe trajectories into more deceptive evaluation instances while preserving their…`。这改变的是可观测状态、控制 owner 或评价证据，而不是仅增加一个模型名称。

Evaluation contract：`arXiv:2605.03242v1 HTML, Experiments/Evaluation and ablation sections; abstract scope: Tool-using agent systems powered by large language models (LLMs) are increasingly deployed across web, app, operating-system, and transactional environments.`。这里的作者实验只证明其披露模型、数据、硬件、精度和实现条件内的结果；未披露字段保持 Not Disclosed。 反证边界：`arXiv:2605.03242v1 HTML, Discussion/Limitations and threat-to-validity passages; no cross-workload generalization inferred`。Artifact：`arXiv:2605.03242v1 HTML, artifact/code statement; immutable event-time commit is Not Disclosed unless explicitly named`。 <!-- claim:SF-AGENT-SAFETY-OOD-ANALOGICAL-EVAL:start -->长期结论只保留为：Agent safety evaluation must test deceptive out-of-distribution transformations and trace judgment transfer, not only literal variants of known unsafe scenarios. 它不证明该实现跨 workload 普遍最优，也不能代替独立复现、fallback 与 rollback。<!-- claim:SF-AGENT-SAFETY-OOD-ANALOGICAL-EVAL:end -->
<!-- review:SF-AGENT-SAFETY-OOD-ANALOGICAL-EVAL:end -->

<!-- review:SF-AGENT-SEQUENTIAL-TRACE-VALIDATION:start -->
### Learning Correct Behavior from Examples: Validating Sequential Execution in Autonomous Agents

问题与旧路径：Agent success should be validated against essential state transitions learned from passing traces, not the agent's self-report or exact replay of one path. 旧方案在工作负载较小、状态可丢弃、风险低或边界固定时仍然合理。 exact-v1 的机制定位为 `arXiv:2605.03159v1 HTML, Method/Design section; abstract mechanism: We present a novel algorithm that automatically learns correct behavior from just 2-10 passing execution traces and validates new executions against this learned model.`。这改变的是可观测状态、控制 owner 或评价证据，而不是仅增加一个模型名称。

Evaluation contract：`arXiv:2605.03159v1 HTML, Experiments/Evaluation and ablation sections; abstract scope: In controlled experiments, our system achieved high accuracy in detecting product bugs and false successes using only 3 training traces.`。这里的作者实验只证明其披露模型、数据、硬件、精度和实现条件内的结果；未披露字段保持 Not Disclosed。 反证边界：`arXiv:2605.03159v1 HTML, Discussion/Limitations and threat-to-validity passages; no cross-workload generalization inferred`。Artifact：`arXiv:2605.03159v1 HTML, artifact/code statement; immutable event-time commit is Not Disclosed unless explicitly named`。 <!-- claim:SF-AGENT-SEQUENTIAL-TRACE-VALIDATION:start -->长期结论只保留为：Agent success should be validated against essential state transitions learned from passing traces, not the agent's self-report or exact replay of one path. 它不证明该实现跨 workload 普遍最优，也不能代替独立复现、fallback 与 rollback。<!-- claim:SF-AGENT-SEQUENTIAL-TRACE-VALIDATION:end -->
<!-- review:SF-AGENT-SEQUENTIAL-TRACE-VALIDATION:end -->

<!-- review:SF-AI-DATACENTER-GRID-CODESIGN:start -->
### From Barrier to Bridge: The Case for AI Data Center/Power Grid Co-Design

问题与旧路径：AI capacity planning must include power-grid interconnection, temporal flexibility and curtailment as system constraints rather than treating electricity as an unlimited unit price. 旧方案在工作负载较小、状态可丢弃、风险低或边界固定时仍然合理。 exact-v1 的机制定位为 `arXiv:2605.03090v1 HTML, Method/Design section; abstract mechanism: We introduce the distinct design principles, operational philosophies, and economic incentives of each sector, and show why their cultural and technical misalignment makes coordination difficult.`。这改变的是可观测状态、控制 owner 或评价证据，而不是仅增加一个模型名称。

Evaluation contract：`arXiv:2605.03090v1 HTML, Experiments/Evaluation and ablation sections; abstract scope: Evaluation scope is disclosed in the exact-v1 experiments/results section`。这里的作者实验只证明其披露模型、数据、硬件、精度和实现条件内的结果；未披露字段保持 Not Disclosed。 反证边界：`arXiv:2605.03090v1 HTML, Discussion/Limitations and threat-to-validity passages; no cross-workload generalization inferred`。Artifact：`arXiv:2605.03090v1 HTML, artifact/code statement; immutable event-time commit is Not Disclosed unless explicitly named`。 <!-- claim:SF-AI-DATACENTER-GRID-CODESIGN:start -->长期结论只保留为：AI capacity planning must include power-grid interconnection, temporal flexibility and curtailment as system constraints rather than treating electricity as an unlimited unit price. 它不证明该实现跨 workload 普遍最优，也不能代替独立复现、fallback 与 rollback。<!-- claim:SF-AI-DATACENTER-GRID-CODESIGN:end -->
<!-- review:SF-AI-DATACENTER-GRID-CODESIGN:end -->

<!-- review:SF-CYBER-DEFENSE-EXECUTOR-AUTHORITY:start -->
### Stable Agentic Control: Tool-Mediated LLM Architecture for Autonomous Cyber Defense

问题与旧路径：Autonomous cyber defense requires executor-owned authorization, bounded effects and recovery receipts; model planning cannot itself commit network changes. 旧方案在工作负载较小、状态可丢弃、风险低或边界固定时仍然合理。 exact-v1 的机制定位为 `§Tool-mediated cyber-defense architecture and stable control loop`。这改变的是可观测状态、控制 owner 或评价证据，而不是仅增加一个模型名称。

Evaluation contract：`§Defense scenarios, tool actions and recovery evaluation`。这里的作者实验只证明其披露模型、数据、硬件、精度和实现条件内的结果；未披露字段保持 Not Disclosed。 反证边界：`§Threat-model, environment and autonomous-action limitations`。Artifact：`Exact-v1 artifact/code statement; immutable event-time commit is Not Disclosed unless explicitly named`。 <!-- claim:SF-CYBER-DEFENSE-EXECUTOR-AUTHORITY:start -->长期结论只保留为：Autonomous cyber defense requires executor-owned authorization, bounded effects and recovery receipts; model planning cannot itself commit network changes. 它不证明该实现跨 workload 普遍最优，也不能代替独立复现、fallback 与 rollback。<!-- claim:SF-CYBER-DEFENSE-EXECUTOR-AUTHORITY:end -->
<!-- review:SF-CYBER-DEFENSE-EXECUTOR-AUTHORITY:end -->

<!-- review:SF-DETERMINISTIC-COMPUTATION-EXECUTION:start -->
### Evaluating Prompting and Execution-Based Methods for Deterministic Computation in LLMs

问题与旧路径：Deterministic computation should be delegated to typed execution and checked outputs when available; prompting remains a fallback, not the truth owner. 旧方案在工作负载较小、状态可丢弃、风险低或边界固定时仍然合理。 exact-v1 的机制定位为 `§Prompting versus execution-based deterministic computation methods`。这改变的是可观测状态、控制 owner 或评价证据，而不是仅增加一个模型名称。

Evaluation contract：`§Task suites, execution correctness and method comparison`。这里的作者实验只证明其披露模型、数据、硬件、精度和实现条件内的结果；未披露字段保持 Not Disclosed。 反证边界：`§Task/language/tool availability limitations`。Artifact：`Exact-v1 artifact/code statement; immutable event-time commit is Not Disclosed unless explicitly named`。 <!-- claim:SF-DETERMINISTIC-COMPUTATION-EXECUTION:start -->长期结论只保留为：Deterministic computation should be delegated to typed execution and checked outputs when available; prompting remains a fallback, not the truth owner. 它不证明该实现跨 workload 普遍最优，也不能代替独立复现、fallback 与 rollback。<!-- claim:SF-DETERMINISTIC-COMPUTATION-EXECUTION:end -->
<!-- review:SF-DETERMINISTIC-COMPUTATION-EXECUTION:end -->

<!-- review:SF-DIFFUSION-PLANNING-COMMIT-REFINE:start -->
### Refining Compositional Diffusion for Reliable Long-Horizon Planning

问题与旧路径：Diffusion planning exposes iterative proposal/correction state, but executable commit still belongs to a feasibility verifier and controller. 旧方案在工作负载较小、状态可丢弃、风险低或边界固定时仍然合理。 exact-v1 的机制定位为 `§Compositional diffusion planner; iterative correction and commitment`。这改变的是可观测状态、控制 owner 或评价证据，而不是仅增加一个模型名称。

Evaluation contract：`§Long-horizon planning evaluation and refinement ablations`。这里的作者实验只证明其披露模型、数据、硬件、精度和实现条件内的结果；未披露字段保持 Not Disclosed。 反证边界：`§Environment, horizon and feasibility-check limitations`。Artifact：`Exact-v1 artifact/code statement; immutable event-time commit is Not Disclosed unless explicitly named`。 <!-- claim:SF-DIFFUSION-PLANNING-COMMIT-REFINE:start -->长期结论只保留为：Diffusion planning exposes iterative proposal/correction state, but executable commit still belongs to a feasibility verifier and controller. 它不证明该实现跨 workload 普遍最优，也不能代替独立复现、fallback 与 rollback。<!-- claim:SF-DIFFUSION-PLANNING-COMMIT-REFINE:end -->
<!-- review:SF-DIFFUSION-PLANNING-COMMIT-REFINE:end -->

<!-- review:SF-DITRON-DISTRIBUTED-TILING:start -->
### DITRON

单机 tensor DSL 的 tile 不知道跨设备 topology，分布式 library 又把 kernel 固定成不可编程 primitive。DITRON 用 Core/Device/Task 三层 tile 把 local memory、device communication 和 task mapping 放进一个 compiler plan，并以 compute–communication swizzling 生成后端。作者结果支持所测 cluster/kernel/vLLM 的收益，但硬件、版本、precision、topology 与生产数据未完整公开，企业节省数字不能外推；expert library 在稳定算子仍是可靠 baseline。

<!-- claim:SF-DITRON-DISTRIBUTED-TILING:start -->证据边界：只接受 arXiv exact-v1 在上述 method/evaluation contract 内的作者主张；未披露硬件、precision、并发、SLO、artifact commit 或生产条件写 Not Disclosed，不作外推。<!-- claim:SF-DITRON-DISTRIBUTED-TILING:end -->
<!-- review:SF-DITRON-DISTRIBUTED-TILING:end -->

<!-- review:SF-JBSHIELD-ADAPTIVE-REPRESENTATION-DEFENSE:start -->
### Revisiting JBShield: Breaking and Rebuilding Representation-Level Jailbreak Defenses

问题与旧路径：Representation-level jailbreak shields must be tested against adaptive attacks and distribution shift; linear separation on a fixed attack set is not a security boundary. 旧方案在工作负载较小、状态可丢弃、风险低或边界固定时仍然合理。 exact-v1 的机制定位为 `arXiv:2605.03095v1 HTML, Method/Design section; abstract mechanism: We design JB-GCG, which modifies GCG's objective to combine two terms: refusal-direction suppression via cosine similarity between the refusal direction and hidden-state representations, and toxic-concept regularization via JBShield's…`。这改变的是可观测状态、控制 owner 或评价证据，而不是仅增加一个模型名称。

Evaluation contract：`arXiv:2605.03095v1 HTML, Experiments/Evaluation and ablation sections; abstract scope: Across five configurations on Llama-3-8B, JB-GCG achieves an average ASR of 46.2%, reaching up to 53.4% in the strongest setting.`。这里的作者实验只证明其披露模型、数据、硬件、精度和实现条件内的结果；未披露字段保持 Not Disclosed。 反证边界：`arXiv:2605.03095v1 HTML, Discussion/Limitations and threat-to-validity passages; no cross-workload generalization inferred`。Artifact：`arXiv:2605.03095v1 HTML, artifact/code statement; immutable event-time commit is Not Disclosed unless explicitly named`。 <!-- claim:SF-JBSHIELD-ADAPTIVE-REPRESENTATION-DEFENSE:start -->长期结论只保留为：Representation-level jailbreak shields must be tested against adaptive attacks and distribution shift; linear separation on a fixed attack set is not a security boundary. 它不证明该实现跨 workload 普遍最优，也不能代替独立复现、fallback 与 rollback。<!-- claim:SF-JBSHIELD-ADAPTIVE-REPRESENTATION-DEFENSE:end -->
<!-- review:SF-JBSHIELD-ADAPTIVE-REPRESENTATION-DEFENSE:end -->

<!-- review:SF-KERNCAP-AMD-KERNEL-ISOLATION:start -->
### Kerncap: Automated Kernel Extraction and Isolation for AMD GPUs

问题与旧路径：Kernel extraction needs automated dependency capture and isolation so compiler/runtime experiments are reproducible rather than tied to an opaque application build. 旧方案在工作负载较小、状态可丢弃、风险低或边界固定时仍然合理。 exact-v1 的机制定位为 `arXiv:2605.03208v1 HTML, Method/Design section; abstract mechanism: We present Kerncap, an automated kernel extraction tool that intercepts dispatches at the HSA runtime for both HIP and Triton, bridging Triton's JIT-only metadata into HSA-level capture via…`。这改变的是可观测状态、控制 owner 或评价证据，而不是仅增加一个模型名称。

Evaluation contract：`arXiv:2605.03208v1 HTML, Experiments/Evaluation and ablation sections; abstract scope: Across six real-world HIP and Triton workloads spanning traditional HPC and ML domains on three AMD GPU architectures (CDNA2, CDNA3, RDNA3), Kerncap extracts and validates kernels from snapshots…`。这里的作者实验只证明其披露模型、数据、硬件、精度和实现条件内的结果；未披露字段保持 Not Disclosed。 反证边界：`arXiv:2605.03208v1 HTML, Discussion/Limitations and threat-to-validity passages; no cross-workload generalization inferred`。Artifact：`arXiv:2605.03208v1 HTML, artifact/code statement; immutable event-time commit is Not Disclosed unless explicitly named`。 <!-- claim:SF-KERNCAP-AMD-KERNEL-ISOLATION:start -->长期结论只保留为：Kernel extraction needs automated dependency capture and isolation so compiler/runtime experiments are reproducible rather than tied to an opaque application build. 它不证明该实现跨 workload 普遍最优，也不能代替独立复现、fallback 与 rollback。<!-- claim:SF-KERNCAP-AMD-KERNEL-ISOLATION:end -->
<!-- review:SF-KERNCAP-AMD-KERNEL-ISOLATION:end -->

<!-- review:SF-MAGE-SHADOW-MEMORY-THREAT-STATE:start -->
### MAGE: Safeguarding LLM Agents against Long-Horizon Threats via Shadow Memory

问题与旧路径：A separate shadow memory can accumulate threat evidence without contaminating productive memory, but its write policy and intervention authority need independent ownership. 旧方案在工作负载较小、状态可丢弃、风险低或边界固定时仍然合理。 exact-v1 的机制定位为 `arXiv:2605.03228v1 HTML, Method/Design section; abstract mechanism: In this paper, we present MAGE (Memory As Guardrail Enforcement), a novel defensive framework designed to counter a wide range of long-horizon threats.`。这改变的是可观测状态、控制 owner 或评价证据，而不是仅增加一个模型名称。

Evaluation contract：`arXiv:2605.03228v1 HTML, Experiments/Evaluation and ablation sections; abstract scope: Inspired by the "shadow stack" abstraction in systems security, MAGE maintains a dedicated, safety-focused agentic memory that distills and retains safety-critical context across the agent's full execution trajectory,…`。这里的作者实验只证明其披露模型、数据、硬件、精度和实现条件内的结果；未披露字段保持 Not Disclosed。 反证边界：`arXiv:2605.03228v1 HTML, Discussion/Limitations and threat-to-validity passages; no cross-workload generalization inferred`。Artifact：`arXiv:2605.03228v1 HTML, artifact/code statement; immutable event-time commit is Not Disclosed unless explicitly named`。 <!-- claim:SF-MAGE-SHADOW-MEMORY-THREAT-STATE:start -->长期结论只保留为：A separate shadow memory can accumulate threat evidence without contaminating productive memory, but its write policy and intervention authority need independent ownership. 它不证明该实现跨 workload 普遍最优，也不能代替独立复现、fallback 与 rollback。<!-- claim:SF-MAGE-SHADOW-MEMORY-THREAT-STATE:end -->
<!-- review:SF-MAGE-SHADOW-MEMORY-THREAT-STATE:end -->

<!-- review:SF-MULTITURN-DEPENDENCY-AWARE-PRIVACY:start -->
### Dependency-Aware Privacy for Multi-turn Agents

问题与旧路径：Multi-turn privacy accounting must preserve dependency among prompts, tools and memory; per-turn checks do not compose into a session guarantee. 旧方案在工作负载较小、状态可丢弃、风险低或边界固定时仍然合理。 exact-v1 的机制定位为 `arXiv:2605.03188v1 HTML, Method/Design section; abstract mechanism: LLM agents release private data across multi-service interactions.`。这改变的是可观测状态、控制 owner 或评价证据，而不是仅增加一个模型名称。

Evaluation contract：`arXiv:2605.03188v1 HTML, Experiments/Evaluation and ablation sections; abstract scope: LLM agents release private data across multi-service interactions.`。这里的作者实验只证明其披露模型、数据、硬件、精度和实现条件内的结果；未披露字段保持 Not Disclosed。 反证边界：`arXiv:2605.03188v1 HTML, Discussion/Limitations and threat-to-validity passages; no cross-workload generalization inferred`。Artifact：`arXiv:2605.03188v1 HTML, artifact/code statement; immutable event-time commit is Not Disclosed unless explicitly named`。 <!-- claim:SF-MULTITURN-DEPENDENCY-AWARE-PRIVACY:start -->长期结论只保留为：Multi-turn privacy accounting must preserve dependency among prompts, tools and memory; per-turn checks do not compose into a session guarantee. 它不证明该实现跨 workload 普遍最优，也不能代替独立复现、fallback 与 rollback。<!-- claim:SF-MULTITURN-DEPENDENCY-AWARE-PRIVACY:end -->
<!-- review:SF-MULTITURN-DEPENDENCY-AWARE-PRIVACY:end -->

<!-- review:SF-OBSERVATIONAL-WORKFLOW-SKILL-LEARNING:start -->
### cotomi Act: Learning to Automate Work by Watching You

问题与旧路径：Learning automation from observation requires provenance, validation and admission of the induced workflow before it may execute; imitation does not transfer user authority. 旧方案在工作负载较小、状态可丢弃、风险低或边界固定时仍然合理。 exact-v1 的机制定位为 `§Observation capture, workflow induction and executable automation`。这改变的是可观测状态、控制 owner 或评价证据，而不是仅增加一个模型名称。

Evaluation contract：`§Automation-task evaluation and correction analysis`。这里的作者实验只证明其披露模型、数据、硬件、精度和实现条件内的结果；未披露字段保持 Not Disclosed。 反证边界：`§UI/domain, demonstration and safety limitations`。Artifact：`Exact-v1 artifact/code statement; immutable event-time commit is Not Disclosed unless explicitly named`。 <!-- claim:SF-OBSERVATIONAL-WORKFLOW-SKILL-LEARNING:start -->长期结论只保留为：Learning automation from observation requires provenance, validation and admission of the induced workflow before it may execute; imitation does not transfer user authority. 它不证明该实现跨 workload 普遍最优，也不能代替独立复现、fallback 与 rollback。<!-- claim:SF-OBSERVATIONAL-WORKFLOW-SKILL-LEARNING:end -->
<!-- review:SF-OBSERVATIONAL-WORKFLOW-SKILL-LEARNING:end -->

<!-- review:SF-ONLINE-CORRECTION-RECOVERY-SHIFT:start -->
### OCRR: A Benchmark for Online Correction Recovery under Distribution Shift

问题与旧路径：Recovery evaluation must measure time-to-detect, correction state and post-shift rollback rather than only final recovered accuracy. 旧方案在工作负载较小、状态可丢弃、风险低或边界固定时仍然合理。 exact-v1 的机制定位为 `§Online correction/recovery method under distribution shift`。这改变的是可观测状态、控制 owner 或评价证据，而不是仅增加一个模型名称。

Evaluation contract：`§Recovery, shift and rollback evaluation`。这里的作者实验只证明其披露模型、数据、硬件、精度和实现条件内的结果；未披露字段保持 Not Disclosed。 反证边界：`§Shift family, correction-oracle and deployment limitations`。Artifact：`Exact-v1 artifact/code statement; immutable event-time commit is Not Disclosed unless explicitly named`。 <!-- claim:SF-ONLINE-CORRECTION-RECOVERY-SHIFT:start -->长期结论只保留为：Recovery evaluation must measure time-to-detect, correction state and post-shift rollback rather than only final recovered accuracy. 它不证明该实现跨 workload 普遍最优，也不能代替独立复现、fallback 与 rollback。<!-- claim:SF-ONLINE-CORRECTION-RECOVERY-SHIFT:end -->
<!-- review:SF-ONLINE-CORRECTION-RECOVERY-SHIFT:end -->

<!-- review:SF-PACT-AGENT-CHOREOGRAPHY:start -->
### Pact: A Choreographic Language for Agentic Ecosystems

问题与旧路径：Agent ecosystems need a versioned choreography that defines role/message order and failure semantics before local implementations; generated endpoints cannot redefine the global protocol. 旧方案在工作负载较小、状态可丢弃、风险低或边界固定时仍然合理。 exact-v1 的机制定位为 `§Pact choreography language, roles, messages and protocol semantics`。这改变的是可观测状态、控制 owner 或评价证据，而不是仅增加一个模型名称。

Evaluation contract：`§Examples/evaluation of generated endpoints and protocol checks`。这里的作者实验只证明其披露模型、数据、硬件、精度和实现条件内的结果；未披露字段保持 Not Disclosed。 反证边界：`§Language subset, runtime and failure-model limitations`。Artifact：`Exact-v1 artifact/code statement; immutable event-time commit is Not Disclosed unless explicitly named`。 <!-- claim:SF-PACT-AGENT-CHOREOGRAPHY:start -->长期结论只保留为：Agent ecosystems need a versioned choreography that defines role/message order and failure semantics before local implementations; generated endpoints cannot redefine the global protocol. 它不证明该实现跨 workload 普遍最优，也不能代替独立复现、fallback 与 rollback。<!-- claim:SF-PACT-AGENT-CHOREOGRAPHY:end -->
<!-- review:SF-PACT-AGENT-CHOREOGRAPHY:end -->

<!-- review:SF-PREGENERATION-ANSWERABILITY-GEOMETRY:start -->
### Geometric Deviation as an Unsupervised Pre-Generation Reliability Signal: Probing LLM Representations for Answerability

问题与旧路径：Pre-generation representation geometry is a bounded abstention sensor; it does not by itself provide calibrated claim confidence or an evidence-backed answer. 旧方案在工作负载较小、状态可丢弃、风险低或边界固定时仍然合理。 exact-v1 的机制定位为 `arXiv:2605.03196v1 HTML, Method/Design section; abstract mechanism: A reliable language model should be able to signal, prior to generation, when a query falls outside its knowledge.`。这改变的是可观测状态、控制 owner 或评价证据，而不是仅增加一个模型名称。

Evaluation contract：`arXiv:2605.03196v1 HTML, Experiments/Evaluation and ablation sections; abstract scope: Across three instruction-tuned models (Llama 3.1-8B, Qwen 2.5-7B, and Mistral-7B-Instruct) and three prompt forms (Math, Fact, Code), we find that geometry primarily encodes task form.`。这里的作者实验只证明其披露模型、数据、硬件、精度和实现条件内的结果；未披露字段保持 Not Disclosed。 反证边界：`arXiv:2605.03196v1 HTML, Discussion/Limitations and threat-to-validity passages; no cross-workload generalization inferred`。Artifact：`arXiv:2605.03196v1 HTML, artifact/code statement; immutable event-time commit is Not Disclosed unless explicitly named`。 <!-- claim:SF-PREGENERATION-ANSWERABILITY-GEOMETRY:start -->长期结论只保留为：Pre-generation representation geometry is a bounded abstention sensor; it does not by itself provide calibrated claim confidence or an evidence-backed answer. 它不证明该实现跨 workload 普遍最优，也不能代替独立复现、fallback 与 rollback。<!-- claim:SF-PREGENERATION-ANSWERABILITY-GEOMETRY:end -->
<!-- review:SF-PREGENERATION-ANSWERABILITY-GEOMETRY:end -->

<!-- review:SF-REFUSAL-TRAJECTORY-MONITOR:start -->
### Refusal Trajectory Monitoring

terminal refusal direction 可能被 GCG 抑制而上游 layer-token trajectory 仍保留，SALO 因而把 hidden-state volume 作为 white-box sensor。它在给定 Qwen/Llama/Mistral 与 XSTest operating point 上改善若干 attack detection；但 causal sufficiency 不等于 necessity，encoded intent 可让模型根本不形成 trajectory，且内部 sensor 与被攻击模型共故障。Security 章节已要求 independent layered guardrails、固定 operating point 与 adaptive red-team，故作为受限案例 No Change。

<!-- claim:SF-REFUSAL-TRAJECTORY-MONITOR:start -->证据边界：只接受 arXiv exact-v1 在上述 method/evaluation contract 内的作者主张；未披露硬件、precision、并发、SLO、artifact commit 或生产条件写 Not Disclosed，不作外推。<!-- claim:SF-REFUSAL-TRAJECTORY-MONITOR:end -->
<!-- review:SF-REFUSAL-TRAJECTORY-MONITOR:end -->

<!-- review:SF-REPOSITORY-GRAPH-REPAIR-PROVENANCE:start -->
### ARISE: A Repository-level Graph Representation and Toolset for Agentic Program Repair and Fault Localization

问题与旧路径：Repository repair should preserve graph snapshot, tool action and test provenance; a generated patch is not authoritative until executable acceptance succeeds. 旧方案在工作负载较小、状态可丢弃、风险低或边界固定时仍然合理。 exact-v1 的机制定位为 `§Repository graph representation; localization and repair toolset`。这改变的是可观测状态、控制 owner 或评价证据，而不是仅增加一个模型名称。

Evaluation contract：`§Fault-localization/program-repair evaluation and ablations`。这里的作者实验只证明其披露模型、数据、硬件、精度和实现条件内的结果；未披露字段保持 Not Disclosed。 反证边界：`§Repository/language/test-oracle limitations`。Artifact：`Exact-v1 artifact/code statement; immutable event-time commit is Not Disclosed unless explicitly named`。 <!-- claim:SF-REPOSITORY-GRAPH-REPAIR-PROVENANCE:start -->长期结论只保留为：Repository repair should preserve graph snapshot, tool action and test provenance; a generated patch is not authoritative until executable acceptance succeeds. 它不证明该实现跨 workload 普遍最优，也不能代替独立复现、fallback 与 rollback。<!-- claim:SF-REPOSITORY-GRAPH-REPAIR-PROVENANCE:end -->
<!-- review:SF-REPOSITORY-GRAPH-REPAIR-PROVENANCE:end -->

<!-- review:SF-ROUTEHIJACK-MOE-SAFETY-ROUTING:start -->
### RouteHijack: Routing-Aware Attack on Mixture-of-Experts LLMs

问题与旧路径：MoE routing is part of the safety attack surface because input optimization can steer traffic away from safety-associated experts. 旧方案在任务短、状态可丢弃、拓扑稳定或风险较低时仍合理。约束变化后，exact-v1 将机制定位在 method sections: expert localization and routing-aware suffix objective；状态/控制权因此从隐式约定转为可测量、可版本化的系统对象。

Evaluation contract：seven MoE LLMs, sibling transfer and three VLMs。作者结果只证明上述模型、硬件、数据、精度与实现条件中披露的范围；未披露字段不推断。反证与边界：limitations/threat model; input-access and evaluator boundary。Artifact：code/artifact revision not disclosed。<!-- claim:SF-ROUTEHIJACK-MOE-SAFETY-ROUTING:start -->长期可保留结论是：MoE routing is part of the safety attack surface because input optimization can steer traffic away from safety-associated experts. 它不证明该实现跨 workload 普遍最优，也不授权跳过独立 evaluation、fallback 与 rollback。<!-- claim:SF-ROUTEHIJACK-MOE-SAFETY-ROUTING:end -->
<!-- review:SF-ROUTEHIJACK-MOE-SAFETY-ROUTING:end -->

<!-- review:SF-SAE-PAIRWISE-CAUSAL-AXIS-AUDIT:start -->
### Steering grids for sparse-autoencoder features: when a top-context label names an activation regime rather than a causal axis

问题与旧路径：Single-feature SAE labels can name an activation regime rather than a causal axis; pairwise intervention structure is needed before interpretability claims enter evidence. 旧方案在工作负载较小、状态可丢弃、风险低或边界固定时仍然合理。 exact-v1 的机制定位为 `arXiv:2605.03160v1 HTML, Method/Design section; abstract mechanism: The standard protocol for interpreting sparse-autoencoder (SAE) features labels each feature from its top-activating contexts and validates the label by steering that single feature at a typical magnitude.`。这改变的是可观测状态、控制 owner 或评价证据，而不是仅增加一个模型名称。

Evaluation contract：`arXiv:2605.03160v1 HTML, Experiments/Evaluation and ablation sections; abstract scope: Evaluation scope is disclosed in the exact-v1 experiments/results section`。这里的作者实验只证明其披露模型、数据、硬件、精度和实现条件内的结果；未披露字段保持 Not Disclosed。 反证边界：`arXiv:2605.03160v1 HTML, Discussion/Limitations and threat-to-validity passages; no cross-workload generalization inferred`。Artifact：`arXiv:2605.03160v1 HTML, artifact/code statement; immutable event-time commit is Not Disclosed unless explicitly named`。 <!-- claim:SF-SAE-PAIRWISE-CAUSAL-AXIS-AUDIT:start -->长期结论只保留为：Single-feature SAE labels can name an activation regime rather than a causal axis; pairwise intervention structure is needed before interpretability claims enter evidence. 它不证明该实现跨 workload 普遍最优，也不能代替独立复现、fallback 与 rollback。<!-- claim:SF-SAE-PAIRWISE-CAUSAL-AXIS-AUDIT:end -->
<!-- review:SF-SAE-PAIRWISE-CAUSAL-AXIS-AUDIT:end -->

<!-- review:SF-SELF-MINED-HARDNESS-SAFETY-FT:start -->
### Self-Mined Hardness for Safety Fine-Tuning

问题与旧路径：Safety fine-tuning should mine current-policy hard examples and preserve a replay boundary; static refusal data cannot track the policy's evolving failure surface. 旧方案在工作负载较小、状态可丢弃、风险低或边界固定时仍然合理。 exact-v1 的机制定位为 `arXiv:2605.03226v1 HTML, Method/Design section; abstract mechanism: Safety fine-tuning of language models typically requires a curated adversarial dataset.`。这改变的是可观测状态、控制 owner 或评价证据，而不是仅增加一个模型名称。

Evaluation contract：`arXiv:2605.03226v1 HTML, Experiments/Evaluation and ablation sections; abstract scope: Evaluation scope is disclosed in the exact-v1 experiments/results section`。这里的作者实验只证明其披露模型、数据、硬件、精度和实现条件内的结果；未披露字段保持 Not Disclosed。 反证边界：`arXiv:2605.03226v1 HTML, Discussion/Limitations and threat-to-validity passages; no cross-workload generalization inferred`。Artifact：`arXiv:2605.03226v1 HTML, artifact/code statement; immutable event-time commit is Not Disclosed unless explicitly named`。 <!-- claim:SF-SELF-MINED-HARDNESS-SAFETY-FT:start -->长期结论只保留为：Safety fine-tuning should mine current-policy hard examples and preserve a replay boundary; static refusal data cannot track the policy's evolving failure surface. 它不证明该实现跨 workload 普遍最优，也不能代替独立复现、fallback 与 rollback。<!-- claim:SF-SELF-MINED-HARDNESS-SAFETY-FT:end -->
<!-- review:SF-SELF-MINED-HARDNESS-SAFETY-FT:end -->

<!-- review:SF-SPARSE-MEMORY-FINETUNING:start -->
### Sparse Memory Finetuning as a Low-Forgetting Alternative to LoRA and Full Finetuning

问题与旧路径：Sparse trainable memory is an alternative adaptation-state representation whose value must be measured jointly on target learning and forgetting; it does not dominate LoRA or full finetuning. 旧方案在工作负载较小、状态可丢弃、风险低或边界固定时仍然合理。 exact-v1 的机制定位为 `§Sparse memory finetuning parameterization and update path`。这改变的是可观测状态、控制 owner 或评价证据，而不是仅增加一个模型名称。

Evaluation contract：`§Comparison with LoRA/full finetuning; forgetting and adaptation metrics`。这里的作者实验只证明其披露模型、数据、硬件、精度和实现条件内的结果；未披露字段保持 Not Disclosed。 反证边界：`§Model/task/parameter-budget limitations`。Artifact：`Exact-v1 artifact/code statement; immutable event-time commit is Not Disclosed unless explicitly named`。 <!-- claim:SF-SPARSE-MEMORY-FINETUNING:start -->长期结论只保留为：Sparse trainable memory is an alternative adaptation-state representation whose value must be measured jointly on target learning and forgetting; it does not dominate LoRA or full finetuning. 它不证明该实现跨 workload 普遍最优，也不能代替独立复现、fallback 与 rollback。<!-- claim:SF-SPARSE-MEMORY-FINETUNING:end -->
<!-- review:SF-SPARSE-MEMORY-FINETUNING:end -->

<!-- review:SF-VDCORES-ASYNC-GPU-RESOURCE-DECOUPLING:start -->
### VDCores: Resource Decoupled Programming and Execution for Asynchronous GPU

问题与旧路径：Asynchronous GPU execution benefits from decoupling virtual execution resources from physical cores, making resource binding a runtime scheduling decision. 旧方案在工作负载较小、状态可丢弃、风险低或边界固定时仍然合理。 exact-v1 的机制定位为 `arXiv:2605.03190v1 HTML, Method/Design section; abstract mechanism: Realizing such a decoupled abstraction efficiently on today's GPUs is itself challenging, VDCores addresses this through a GPU-specialized programming model and GPU runtime design that preserves the flexibility…`。这改变的是可观测状态、控制 owner 或评价证据，而不是仅增加一个模型名称。

Evaluation contract：`arXiv:2605.03190v1 HTML, Experiments/Evaluation and ablation sections; abstract scope: Across four LLM inference workloads on GH200, H100, and RTX 6000 Pro GPUs, VDCores significantly improves decoding throughput by 24% on average and by up to 77% under…`。这里的作者实验只证明其披露模型、数据、硬件、精度和实现条件内的结果；未披露字段保持 Not Disclosed。 反证边界：`arXiv:2605.03190v1 HTML, Discussion/Limitations and threat-to-validity passages; no cross-workload generalization inferred`。Artifact：`arXiv:2605.03190v1 HTML, artifact/code statement; immutable event-time commit is Not Disclosed unless explicitly named`。 <!-- claim:SF-VDCORES-ASYNC-GPU-RESOURCE-DECOUPLING:start -->长期结论只保留为：Asynchronous GPU execution benefits from decoupling virtual execution resources from physical cores, making resource binding a runtime scheduling decision. 它不证明该实现跨 workload 普遍最优，也不能代替独立复现、fallback 与 rollback。<!-- claim:SF-VDCORES-ASYNC-GPU-RESOURCE-DECOUPLING:end -->
<!-- review:SF-VDCORES-ASYNC-GPU-RESOURCE-DECOUPLING:end -->

<!-- review:SF-WEB-PII-DEFENSIVE-PROMPT-THREAT:start -->
### PIIGuard: Mitigating PII Harvesting under Adversarial Sanitization

问题与旧路径：Page-side defensive prompts are adversarial content and at most a bounded mitigation sensor; providers still need sanitization, information-flow policy and output authorization. 旧方案在工作负载较小、状态可丢弃、风险低或边界固定时仍然合理。 exact-v1 的机制定位为 `§2 Threat Model; §3 PIIGuard methodology`。这改变的是可观测状态、控制 owner 或评价证据，而不是仅增加一个模型名称。

Evaluation contract：`§4 setup; §5 evaluation including sanitizer and URL modes`。这里的作者实验只证明其披露模型、数据、硬件、精度和实现条件内的结果；未披露字段保持 Not Disclosed。 反证边界：`§7 Discussion; sanitizer front and deployment limitations`。Artifact：`Exact-v1 artifact/code statement; immutable event-time commit is Not Disclosed unless explicitly named`。 <!-- claim:SF-WEB-PII-DEFENSIVE-PROMPT-THREAT:start -->长期结论只保留为：Page-side defensive prompts are adversarial content and at most a bounded mitigation sensor; providers still need sanitization, information-flow policy and output authorization. 它不证明该实现跨 workload 普遍最优，也不能代替独立复现、fallback 与 rollback。<!-- claim:SF-WEB-PII-DEFENSIVE-PROMPT-THREAT:end -->
<!-- review:SF-WEB-PII-DEFENSIVE-PROMPT-THREAT:end -->

## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-02905 | exact-v1 evaluation for eOptShrinkQ: Near-Lossless KV Cache Compression Through Optimal Spectral Denoising and Quantization | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | paper authors |
| SF-2026-ARXIV-2605-02960 | §7-§8 Qwen3-235B-A22B on four hardware/precision configurations | Not Disclosed in exact-v1; no inference made | Not Disclosed in exact-v1; no inference made | Not Disclosed in exact-v1; no inference made | Not Disclosed in exact-v1; no inference made | Not Disclosed in exact-v1; no inference made | Not Disclosed in exact-v1; no inference made | Not Disclosed in exact-v1; no inference made | Not Disclosed in exact-v1; no inference made | exact-v1 author evaluator described in §7-§8 Qwen3-235B-A22B on four hardware/precision configurations |
| SF-2026-ARXIV-2605-02964 | §5 thirteen frontier models, sibling post-training comparison and hardening | Not Disclosed in exact-v1; no inference made | Not Disclosed in exact-v1; no inference made | Not Disclosed in exact-v1; no inference made | Not Disclosed in exact-v1; no inference made | Not Disclosed in exact-v1; no inference made | Not Disclosed in exact-v1; no inference made | Not Disclosed in exact-v1; no inference made | Not Disclosed in exact-v1; no inference made | exact-v1 author evaluator described in §5 thirteen frontier models, sibling post-training comparison and hardening |
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
| SF-ADVERSARIAL-RESEARCH-ORCHESTRATION | exact-v1 disclosed workload for ARIS: Autonomous Research via Adversarial Multi-Agent Collaboration | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-AGENT-SAFETY-OOD-ANALOGICAL-EVAL | exact-v1 disclosed workload for Enhancing Agent Safety Judgment: Controlled Benchmark Rewriting and Analogical Reasoning for Deceptive Out-of-Distribution Scenarios | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-AGENT-SEQUENTIAL-TRACE-VALIDATION | exact-v1 disclosed workload for Learning Correct Behavior from Examples: Validating Sequential Execution in Autonomous Agents | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-AI-DATACENTER-GRID-CODESIGN | exact-v1 disclosed workload for From Barrier to Bridge: The Case for AI Data Center/Power Grid Co-Design | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-CYBER-DEFENSE-EXECUTOR-AUTHORITY | exact-v1 disclosed workload for Stable Agentic Control: Tool-Mediated LLM Architecture for Autonomous Cyber Defense | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-DETERMINISTIC-COMPUTATION-EXECUTION | exact-v1 disclosed workload for Evaluating Prompting and Execution-Based Methods for Deterministic Computation in LLMs | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-DIFFUSION-PLANNING-COMMIT-REFINE | exact-v1 disclosed workload for Refining Compositional Diffusion for Reliable Long-Horizon Planning | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-DITRON-DISTRIBUTED-TILING | exact-v1 disclosed workload；见 evaluation locator | exact-v1 disclosed model or Not Disclosed | Not Disclosed unless named in Review | Not Disclosed unless named in Review | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | 作者指标的 scoped contract；无通用生产阈值 | authors / task labels / formal proof as applicable |
| SF-JBSHIELD-ADAPTIVE-REPRESENTATION-DEFENSE | exact-v1 disclosed workload for Revisiting JBShield: Breaking and Rebuilding Representation-Level Jailbreak Defenses | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-KERNCAP-AMD-KERNEL-ISOLATION | exact-v1 disclosed workload for Kerncap: Automated Kernel Extraction and Isolation for AMD GPUs | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-MAGE-SHADOW-MEMORY-THREAT-STATE | exact-v1 disclosed workload for MAGE: Safeguarding LLM Agents against Long-Horizon Threats via Shadow Memory | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-MULTITURN-DEPENDENCY-AWARE-PRIVACY | exact-v1 disclosed workload for Dependency-Aware Privacy for Multi-turn Agents | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-OBSERVATIONAL-WORKFLOW-SKILL-LEARNING | exact-v1 disclosed workload for cotomi Act: Learning to Automate Work by Watching You | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-ONLINE-CORRECTION-RECOVERY-SHIFT | exact-v1 disclosed workload for OCRR: A Benchmark for Online Correction Recovery under Distribution Shift | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-PACT-AGENT-CHOREOGRAPHY | exact-v1 disclosed workload for Pact: A Choreographic Language for Agentic Ecosystems | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-PREGENERATION-ANSWERABILITY-GEOMETRY | exact-v1 disclosed workload for Geometric Deviation as an Unsupervised Pre-Generation Reliability Signal: Probing LLM Representations for Answerability | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-REFUSAL-TRAJECTORY-MONITOR | exact-v1 disclosed workload；见 evaluation locator | exact-v1 disclosed model or Not Disclosed | Not Disclosed unless named in Review | Not Disclosed unless named in Review | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | 作者指标的 scoped contract；无通用生产阈值 | authors / task labels / formal proof as applicable |
| SF-REPOSITORY-GRAPH-REPAIR-PROVENANCE | exact-v1 disclosed workload for ARISE: A Repository-level Graph Representation and Toolset for Agentic Program Repair and Fault Localization | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-ROUTEHIJACK-MOE-SAFETY-ROUTING | exact-v1 disclosed workload for RouteHijack: Routing-Aware Attack on Mixture-of-Experts LLMs | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless exact-v1 Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/throughput contract only | author protocol; independent reproduction Not Disclosed |
| SF-SAE-PAIRWISE-CAUSAL-AXIS-AUDIT | exact-v1 disclosed workload for Steering grids for sparse-autoencoder features: when a top-context label names an activation regime rather than a causal axis | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-SELF-MINED-HARDNESS-SAFETY-FT | exact-v1 disclosed workload for Self-Mined Hardness for Safety Fine-Tuning | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-SPARSE-MEMORY-FINETUNING | exact-v1 disclosed workload for Sparse Memory Finetuning as a Low-Forgetting Alternative to LoRA and Full Finetuning | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-VDCORES-ASYNC-GPU-RESOURCE-DECOUPLING | exact-v1 disclosed workload for VDCores: Resource Decoupled Programming and Execution for Asynchronous GPU | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |
| SF-WEB-PII-DEFENSIVE-PROMPT-THREAT | exact-v1 disclosed workload for PIIGuard: Mitigating PII Harvesting under Adversarial Sanitization | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-02960 | score_7_9;potential_books_delta | selected | DA-20260506-01 | — | Score=9/9 且属于当日最高跨系统设计影响；有限叙事预算不替代其余 Source Review。 | analysis:DA-20260506-01 |
| SF-2026-ARXIV-2605-02964 | score_7_9 | selected | DA-20260506-02 | — | Score=9/9 且属于当日最高跨系统设计影响；有限叙事预算不替代其余 Source Review。 | analysis:DA-20260506-02 |
| SF-2026-ARXIV-2605-03275 | score_7_9 | selected | DA-20260506-03 | — | Score=9/9 且属于当日最高跨系统设计影响；有限叙事预算不替代其余 Source Review。 | analysis:DA-20260506-03 |
| SF-2026-ARXIV-2605-03309 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-03309 |
| SF-2026-ARXIV-2605-03310 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-03310 |
| SF-2026-ARXIV-2605-03312 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-03312 |
| SF-2026-ARXIV-2605-03314 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-03314 |
| SF-2026-ARXIV-2605-03327 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-03327 |
| SF-2026-ARXIV-2605-03353 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-03353 |
| SF-2026-ARXIV-2605-03354 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-03354 |
| SF-2026-ARXIV-2605-03375 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-03375 |
| SF-2026-ARXIV-2605-03378 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-03378 |
| SF-2026-ARXIV-2605-03379 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-03379 |
| SF-2026-ARXIV-2605-03408 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-03408 |
| SF-2026-ARXIV-2605-03425 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-03425 |
| SF-2026-ARXIV-2605-03482 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-03482 |
| SF-2026-ARXIV-2605-03505 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-03505 |
| SF-2026-ARXIV-2605-03534 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-03534 |
| SF-2026-ARXIV-2605-03561 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-03561 |
| SF-2026-ARXIV-2605-03562 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-03562 |
| SF-2026-ARXIV-2605-03566 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-03566 |
| SF-2026-ARXIV-2605-03596 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-03596 |
| SF-2026-ARXIV-2605-03644 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-03644 |
| SF-2026-ARXIV-2605-03667 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-03667 |
| SF-2026-ARXIV-2605-03675 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-03675 |
| SF-2026-ARXIV-2605-03677 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-03677 |
| SF-2026-ARXIV-2605-03762 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-03762 |
| SF-2026-ARXIV-2605-03838 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-03838 |
| SF-2026-ARXIV-2605-03858 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-03858 |
| SF-2026-ARXIV-2605-03862 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-03862 |
| SF-2026-ARXIV-2605-03884 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-03884 |
| SF-2026-ARXIV-2605-03952 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-03952 |
| SF-2026-ARXIV-2605-03971 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-03971 |
| SF-2026-ARXIV-2605-03986 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-03986 |
| SF-2026-ARXIV-2605-04018 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-04018 |
| SF-2026-ARXIV-2605-04036 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-04036 |
| SF-2026-ARXIV-2605-04039 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-04039 |
| SF-ADVERSARIAL-RESEARCH-ORCHESTRATION | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-ADVERSARIAL-RESEARCH-ORCHESTRATION |
| SF-AGENT-SAFETY-OOD-ANALOGICAL-EVAL | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-AGENT-SAFETY-OOD-ANALOGICAL-EVAL |
| SF-AGENT-SEQUENTIAL-TRACE-VALIDATION | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-AGENT-SEQUENTIAL-TRACE-VALIDATION |
| SF-AI-DATACENTER-GRID-CODESIGN | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-AI-DATACENTER-GRID-CODESIGN |
| SF-CYBER-DEFENSE-EXECUTOR-AUTHORITY | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-CYBER-DEFENSE-EXECUTOR-AUTHORITY |
| SF-DETERMINISTIC-COMPUTATION-EXECUTION | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-DETERMINISTIC-COMPUTATION-EXECUTION |
| SF-DIFFUSION-PLANNING-COMMIT-REFINE | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-DIFFUSION-PLANNING-COMMIT-REFINE |
| SF-DITRON-DISTRIBUTED-TILING | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-DITRON-DISTRIBUTED-TILING |
| SF-JBSHIELD-ADAPTIVE-REPRESENTATION-DEFENSE | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-JBSHIELD-ADAPTIVE-REPRESENTATION-DEFENSE |
| SF-KERNCAP-AMD-KERNEL-ISOLATION | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-KERNCAP-AMD-KERNEL-ISOLATION |
| SF-MAGE-SHADOW-MEMORY-THREAT-STATE | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-MAGE-SHADOW-MEMORY-THREAT-STATE |
| SF-MULTITURN-DEPENDENCY-AWARE-PRIVACY | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-MULTITURN-DEPENDENCY-AWARE-PRIVACY |
| SF-OBSERVATIONAL-WORKFLOW-SKILL-LEARNING | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-OBSERVATIONAL-WORKFLOW-SKILL-LEARNING |
| SF-ONLINE-CORRECTION-RECOVERY-SHIFT | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-ONLINE-CORRECTION-RECOVERY-SHIFT |
| SF-PACT-AGENT-CHOREOGRAPHY | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-PACT-AGENT-CHOREOGRAPHY |
| SF-REFUSAL-TRAJECTORY-MONITOR | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-REFUSAL-TRAJECTORY-MONITOR |
| SF-REPOSITORY-GRAPH-REPAIR-PROVENANCE | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-REPOSITORY-GRAPH-REPAIR-PROVENANCE |
| SF-ROUTEHIJACK-MOE-SAFETY-ROUTING | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-ROUTEHIJACK-MOE-SAFETY-ROUTING |
| SF-SAE-PAIRWISE-CAUSAL-AXIS-AUDIT | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-SAE-PAIRWISE-CAUSAL-AXIS-AUDIT |
| SF-SELF-MINED-HARDNESS-SAFETY-FT | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-SELF-MINED-HARDNESS-SAFETY-FT |
| SF-SPARSE-MEMORY-FINETUNING | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-SPARSE-MEMORY-FINETUNING |
| SF-VDCORES-ASYNC-GPU-RESOURCE-DECOUPLING | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-VDCORES-ASYNC-GPU-RESOURCE-DECOUPLING |
| SF-WEB-PII-DEFENSIVE-PROMPT-THREAT | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-WEB-PII-DEFENSIVE-PROMPT-THREAT |

<!-- analysis:DA-20260506-01:start -->
### Deep Analysis — SF-2026-ARXIV-2605-02960

该 family 的 Score V2=9/9；Source Review 已闭合问题、旧路径、机制 owner、evaluation boundary、trade-off 与共存条件。Deep Analysis 只提升叙事优先级，不改变 Evidence Gate。
<!-- analysis:DA-20260506-01:end -->

<!-- analysis:DA-20260506-02:start -->
### Deep Analysis — SF-2026-ARXIV-2605-02964

该 family 的 Score V2=9/9；Source Review 已闭合问题、旧路径、机制 owner、evaluation boundary、trade-off 与共存条件。Deep Analysis 只提升叙事优先级，不改变 Evidence Gate。
<!-- analysis:DA-20260506-02:end -->

<!-- analysis:DA-20260506-03:start -->
### Deep Analysis — SF-2026-ARXIV-2605-03275

该 family 的 Score V2=9/9；Source Review 已闭合问题、旧路径、机制 owner、evaluation boundary、trade-off 与共存条件。Deep Analysis 只提升叙事优先级，不改变 Evidence Gate。
<!-- analysis:DA-20260506-03:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-03309:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-03309:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-03310:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-03310:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-03312:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-03312:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-03314:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-03314:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-03327:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-03327:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-03353:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-03353:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-03354:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-03354:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-03375:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-03375:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-03378:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-03378:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-03379:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-03379:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-03408:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-03408:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-03425:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-03425:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-03482:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-03482:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-03505:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-03505:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-03534:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-03534:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-03561:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-03561:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-03562:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-03562:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-03566:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-03566:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-03596:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-03596:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-03644:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-03644:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-03667:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-03667:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-03675:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-03675:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-03677:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-03677:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-03762:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-03762:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-03838:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-03838:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-03858:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-03858:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-03862:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-03862:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-03884:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-03884:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-03952:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-03952:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-03971:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-03971:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-03986:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-03986:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-04018:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-04018:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-04036:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-04036:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-04039:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-04039:end -->

<!-- analysis-decision:SF-ADVERSARIAL-RESEARCH-ORCHESTRATION:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-ADVERSARIAL-RESEARCH-ORCHESTRATION:end -->

<!-- analysis-decision:SF-AGENT-SAFETY-OOD-ANALOGICAL-EVAL:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-AGENT-SAFETY-OOD-ANALOGICAL-EVAL:end -->

<!-- analysis-decision:SF-AGENT-SEQUENTIAL-TRACE-VALIDATION:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-AGENT-SEQUENTIAL-TRACE-VALIDATION:end -->

<!-- analysis-decision:SF-AI-DATACENTER-GRID-CODESIGN:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-AI-DATACENTER-GRID-CODESIGN:end -->

<!-- analysis-decision:SF-CYBER-DEFENSE-EXECUTOR-AUTHORITY:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-CYBER-DEFENSE-EXECUTOR-AUTHORITY:end -->

<!-- analysis-decision:SF-DETERMINISTIC-COMPUTATION-EXECUTION:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-DETERMINISTIC-COMPUTATION-EXECUTION:end -->

<!-- analysis-decision:SF-DIFFUSION-PLANNING-COMMIT-REFINE:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-DIFFUSION-PLANNING-COMMIT-REFINE:end -->

<!-- analysis-decision:SF-DITRON-DISTRIBUTED-TILING:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-DITRON-DISTRIBUTED-TILING:end -->

<!-- analysis-decision:SF-JBSHIELD-ADAPTIVE-REPRESENTATION-DEFENSE:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-JBSHIELD-ADAPTIVE-REPRESENTATION-DEFENSE:end -->

<!-- analysis-decision:SF-KERNCAP-AMD-KERNEL-ISOLATION:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-KERNCAP-AMD-KERNEL-ISOLATION:end -->

<!-- analysis-decision:SF-MAGE-SHADOW-MEMORY-THREAT-STATE:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-MAGE-SHADOW-MEMORY-THREAT-STATE:end -->

<!-- analysis-decision:SF-MULTITURN-DEPENDENCY-AWARE-PRIVACY:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-MULTITURN-DEPENDENCY-AWARE-PRIVACY:end -->

<!-- analysis-decision:SF-OBSERVATIONAL-WORKFLOW-SKILL-LEARNING:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-OBSERVATIONAL-WORKFLOW-SKILL-LEARNING:end -->

<!-- analysis-decision:SF-ONLINE-CORRECTION-RECOVERY-SHIFT:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-ONLINE-CORRECTION-RECOVERY-SHIFT:end -->

<!-- analysis-decision:SF-PACT-AGENT-CHOREOGRAPHY:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-PACT-AGENT-CHOREOGRAPHY:end -->

<!-- analysis-decision:SF-REFUSAL-TRAJECTORY-MONITOR:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-REFUSAL-TRAJECTORY-MONITOR:end -->

<!-- analysis-decision:SF-REPOSITORY-GRAPH-REPAIR-PROVENANCE:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-REPOSITORY-GRAPH-REPAIR-PROVENANCE:end -->

<!-- analysis-decision:SF-ROUTEHIJACK-MOE-SAFETY-ROUTING:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-ROUTEHIJACK-MOE-SAFETY-ROUTING:end -->

<!-- analysis-decision:SF-SAE-PAIRWISE-CAUSAL-AXIS-AUDIT:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-SAE-PAIRWISE-CAUSAL-AXIS-AUDIT:end -->

<!-- analysis-decision:SF-SELF-MINED-HARDNESS-SAFETY-FT:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-SELF-MINED-HARDNESS-SAFETY-FT:end -->

<!-- analysis-decision:SF-SPARSE-MEMORY-FINETUNING:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-SPARSE-MEMORY-FINETUNING:end -->

<!-- analysis-decision:SF-VDCORES-ASYNC-GPU-RESOURCE-DECOUPLING:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-VDCORES-ASYNC-GPU-RESOURCE-DECOUPLING:end -->

<!-- analysis-decision:SF-WEB-PII-DEFENSIVE-PROMPT-THREAT:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-WEB-PII-DEFENSIVE-PROMPT-THREAT:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-02905 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L97 (H2: KV Cache 的生命周期) | books/part-05-inference-system/44-decode.md#L10 (H2: 本章要回答的问题); books/part-05-inference-system/46-continuous-batching.md#L10 (H2: 本章要回答的问题) | existing:SF-2026-ARXIV-2605-02905 | delta:SF-2026-ARXIV-2605-02905 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-02905 |
| SF-2026-ARXIV-2605-02960 | INFER-PREFILL | books/part-05-inference-system/43-prefill.md#L1 | books/part-05-inference-system/42-what-happens-during-inference.md#L1; books/part-05-inference-system/44-decode.md#L1 | existing:SF-2026-ARXIV-2605-02960 | delta:SF-2026-ARXIV-2605-02960 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-02960 |
| SF-2026-ARXIV-2605-02964 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L1; books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2026-ARXIV-2605-02964 | delta:SF-2026-ARXIV-2605-02964 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-02964 |
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
| SF-ADVERSARIAL-RESEARCH-ORCHESTRATION | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#chapter-82 | books/part-07-agent/81-workflow.md#chapter-81; books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-ADVERSARIAL-RESEARCH-ORCHESTRATION | delta:SF-ADVERSARIAL-RESEARCH-ORCHESTRATION | Layering / Dependency | No Change — Existing Coverage | books-review:SF-ADVERSARIAL-RESEARCH-ORCHESTRATION |
| SF-AGENT-SAFETY-OOD-ANALOGICAL-EVAL | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-AGENT-SAFETY-OOD-ANALOGICAL-EVAL | delta:SF-AGENT-SAFETY-OOD-ANALOGICAL-EVAL | Layering / Dependency | No Change — Existing Coverage | books-review:SF-AGENT-SAFETY-OOD-ANALOGICAL-EVAL |
| SF-AGENT-SEQUENTIAL-TRACE-VALIDATION | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-AGENT-SEQUENTIAL-TRACE-VALIDATION | delta:SF-AGENT-SEQUENTIAL-TRACE-VALIDATION | Layering / Dependency | No Change — Existing Coverage | books-review:SF-AGENT-SEQUENTIAL-TRACE-VALIDATION |
| SF-AI-DATACENTER-GRID-CODESIGN | PLATFORM-COST | books/part-06-ai-infrastructure/70-cost.md#chapter-70 | books/part-06-ai-infrastructure/69-trace.md#chapter-69; books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71 | existing:SF-AI-DATACENTER-GRID-CODESIGN | delta:SF-AI-DATACENTER-GRID-CODESIGN | Layering / Dependency | No Change — Existing Coverage | books-review:SF-AI-DATACENTER-GRID-CODESIGN |
| SF-CYBER-DEFENSE-EXECUTOR-AUTHORITY | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-CYBER-DEFENSE-EXECUTOR-AUTHORITY | delta:SF-CYBER-DEFENSE-EXECUTOR-AUTHORITY | Layering / Dependency | No Change — Existing Coverage | books-review:SF-CYBER-DEFENSE-EXECUTOR-AUTHORITY |
| SF-DETERMINISTIC-COMPUTATION-EXECUTION | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#chapter-78 | books/part-07-agent/77-memory.md#chapter-77; books/part-07-agent/79-planning.md#chapter-79 | existing:SF-DETERMINISTIC-COMPUTATION-EXECUTION | delta:SF-DETERMINISTIC-COMPUTATION-EXECUTION | Layering / Dependency | No Change — Existing Coverage | books-review:SF-DETERMINISTIC-COMPUTATION-EXECUTION |
| SF-DIFFUSION-PLANNING-COMMIT-REFINE | MULTIMODAL-GENERATIVE-PARADIGMS | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24 | books/part-03-multimodal-world-models/23-multimodal-representation.md#chapter-23; books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | existing:SF-DIFFUSION-PLANNING-COMMIT-REFINE | delta:SF-DIFFUSION-PLANNING-COMMIT-REFINE | Layering / Dependency | No Change — Existing Coverage | books-review:SF-DIFFUSION-PLANNING-COMMIT-REFINE |
| SF-DITRON-DISTRIBUTED-TILING | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#L10 | books/part-05-inference-system/48-speculative-decoding.md#L10; books/part-05-inference-system/50-vllm.md#L10 | existing:SF-DITRON-DISTRIBUTED-TILING | delta:SF-DITRON-DISTRIBUTED-TILING | Direct Evolution | Integrate | books-review:SF-DITRON-DISTRIBUTED-TILING |
| SF-JBSHIELD-ADAPTIVE-REPRESENTATION-DEFENSE | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-JBSHIELD-ADAPTIVE-REPRESENTATION-DEFENSE | delta:SF-JBSHIELD-ADAPTIVE-REPRESENTATION-DEFENSE | Layering / Dependency | No Change — Existing Coverage | books-review:SF-JBSHIELD-ADAPTIVE-REPRESENTATION-DEFENSE |
| SF-KERNCAP-AMD-KERNEL-ISOLATION | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | books/part-05-inference-system/48-speculative-decoding.md#chapter-48; books/part-05-inference-system/50-vllm.md#chapter-50 | existing:SF-KERNCAP-AMD-KERNEL-ISOLATION | delta:SF-KERNCAP-AMD-KERNEL-ISOLATION | Layering / Dependency | No Change — Existing Coverage | books-review:SF-KERNCAP-AMD-KERNEL-ISOLATION |
| SF-MAGE-SHADOW-MEMORY-THREAT-STATE | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76; books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-MAGE-SHADOW-MEMORY-THREAT-STATE | delta:SF-MAGE-SHADOW-MEMORY-THREAT-STATE | Layering / Dependency | No Change — Existing Coverage | books-review:SF-MAGE-SHADOW-MEMORY-THREAT-STATE |
| SF-MULTITURN-DEPENDENCY-AWARE-PRIVACY | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-MULTITURN-DEPENDENCY-AWARE-PRIVACY | delta:SF-MULTITURN-DEPENDENCY-AWARE-PRIVACY | Layering / Dependency | No Change — Existing Coverage | books-review:SF-MULTITURN-DEPENDENCY-AWARE-PRIVACY |
| SF-OBSERVATIONAL-WORKFLOW-SKILL-LEARNING | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#chapter-81 | books/part-07-agent/80-reflection.md#chapter-80; books/part-07-agent/82-multi-agent.md#chapter-82 | existing:SF-OBSERVATIONAL-WORKFLOW-SKILL-LEARNING | delta:SF-OBSERVATIONAL-WORKFLOW-SKILL-LEARNING | Layering / Dependency | No Change — Existing Coverage | books-review:SF-OBSERVATIONAL-WORKFLOW-SKILL-LEARNING |
| SF-ONLINE-CORRECTION-RECOVERY-SHIFT | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-ONLINE-CORRECTION-RECOVERY-SHIFT | delta:SF-ONLINE-CORRECTION-RECOVERY-SHIFT | Layering / Dependency | No Change — Existing Coverage | books-review:SF-ONLINE-CORRECTION-RECOVERY-SHIFT |
| SF-PACT-AGENT-CHOREOGRAPHY | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#chapter-81 | books/part-07-agent/80-reflection.md#chapter-80; books/part-07-agent/82-multi-agent.md#chapter-82 | existing:SF-PACT-AGENT-CHOREOGRAPHY | delta:SF-PACT-AGENT-CHOREOGRAPHY | Layering / Dependency | No Change — Existing Coverage | books-review:SF-PACT-AGENT-CHOREOGRAPHY |
| SF-PREGENERATION-ANSWERABILITY-GEOMETRY | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-PREGENERATION-ANSWERABILITY-GEOMETRY | delta:SF-PREGENERATION-ANSWERABILITY-GEOMETRY | Layering / Dependency | No Change — Existing Coverage | books-review:SF-PREGENERATION-ANSWERABILITY-GEOMETRY |
| SF-REFUSAL-TRAJECTORY-MONITOR | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L10 | books/part-06-ai-infrastructure/66-evaluation-system.md#L10; books/part-07-agent/78-tool-calling.md#L10 | existing:SF-REFUSAL-TRAJECTORY-MONITOR | delta:SF-REFUSAL-TRAJECTORY-MONITOR | Principle Reuse | No Change — Existing Coverage | books-review:SF-REFUSAL-TRAJECTORY-MONITOR |
| SF-REPOSITORY-GRAPH-REPAIR-PROVENANCE | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#chapter-81 | books/part-07-agent/80-reflection.md#chapter-80; books/part-07-agent/82-multi-agent.md#chapter-82 | existing:SF-REPOSITORY-GRAPH-REPAIR-PROVENANCE | delta:SF-REPOSITORY-GRAPH-REPAIR-PROVENANCE | Layering / Dependency | No Change — Existing Coverage | books-review:SF-REPOSITORY-GRAPH-REPAIR-PROVENANCE |
| SF-ROUTEHIJACK-MOE-SAFETY-ROUTING | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#adjacent-chapter | existing:SF-ROUTEHIJACK-MOE-SAFETY-ROUTING | delta:SF-ROUTEHIJACK-MOE-SAFETY-ROUTING | Direct Evolution | Integrate | books-review:SF-ROUTEHIJACK-MOE-SAFETY-ROUTING |
| SF-SAE-PAIRWISE-CAUSAL-AXIS-AUDIT | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-SAE-PAIRWISE-CAUSAL-AXIS-AUDIT | delta:SF-SAE-PAIRWISE-CAUSAL-AXIS-AUDIT | Layering / Dependency | No Change — Existing Coverage | books-review:SF-SAE-PAIRWISE-CAUSAL-AXIS-AUDIT |
| SF-SELF-MINED-HARDNESS-SAFETY-FT | TRAIN-SFT | books/part-04-training-system/29-sft.md#chapter-29 | books/part-04-training-system/28-pretraining.md#chapter-28; books/part-04-training-system/30-lora.md#chapter-30 | existing:SF-SELF-MINED-HARDNESS-SAFETY-FT | delta:SF-SELF-MINED-HARDNESS-SAFETY-FT | Layering / Dependency | No Change — Existing Coverage | books-review:SF-SELF-MINED-HARDNESS-SAFETY-FT |
| SF-SPARSE-MEMORY-FINETUNING | TRAIN-LORA | books/part-04-training-system/30-lora.md#chapter-30 | books/part-04-training-system/29-sft.md#chapter-29; books/part-04-training-system/31-rlhf.md#chapter-31 | existing:SF-SPARSE-MEMORY-FINETUNING | delta:SF-SPARSE-MEMORY-FINETUNING | Layering / Dependency | No Change — Existing Coverage | books-review:SF-SPARSE-MEMORY-FINETUNING |
| SF-VDCORES-ASYNC-GPU-RESOURCE-DECOUPLING | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | books/part-05-inference-system/48-speculative-decoding.md#chapter-48; books/part-05-inference-system/50-vllm.md#chapter-50 | existing:SF-VDCORES-ASYNC-GPU-RESOURCE-DECOUPLING | delta:SF-VDCORES-ASYNC-GPU-RESOURCE-DECOUPLING | Direct Evolution | Integrate | books-review:SF-VDCORES-ASYNC-GPU-RESOURCE-DECOUPLING |
| SF-WEB-PII-DEFENSIVE-PROMPT-THREAT | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-WEB-PII-DEFENSIVE-PROMPT-THREAT | delta:SF-WEB-PII-DEFENSIVE-PROMPT-THREAT | Layering / Dependency | No Change — Existing Coverage | books-review:SF-WEB-PII-DEFENSIVE-PROMPT-THREAT |

<!-- books-review:SF-2026-ARXIV-2605-02905:start -->
<!-- existing:SF-2026-ARXIV-2605-02905:start -->对读 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L97 (H2: KV Cache 的生命周期)` 及相邻章节后，现有命题为：本章的核心判断是：**KV Cache 利用 causal decoding 中历史 K/V 不再变化的性质，以随序列增长的 memory state 换取历史 layer computation 不重算；它加速 Decode，也把请求从无状态输入变成必须管理生命周期和 ownership 的系统对象。** 目标小节已经拥有该 family 所需的长期 owner 与旧路径/约束边界。<!-- existing:SF-2026-ARXIV-2605-02905:end -->
<!-- delta:SF-2026-ARXIV-2605-02905:start -->Exact-v1 的 source-specific delta 是：eOptShrinkQ 先按 token block 对 KV 矩阵执行 optimal singular-value shrinkage，自动识别并单独编码共享的低秩 context 分量；再用 TurboQuant 逐向量量化保留 token-specific 信息的全秩 residual。若没有 singular value 越过 bulk edge，则跳过 SVD、直接进入 residual quantization。 其证据边界为：Evidence is author-reported exact-v1 mechanism/evaluation evidence. It does not establish cross-model, cross-hardware, cross-workload or production generality unless those conditions are explicitly named above. 该实现或实验没有改变当前章节已经成立的长期机制，不把作者 benchmark 外推为通用结论。<!-- delta:SF-2026-ARXIV-2605-02905:end -->
Decision: `No Change — Existing Coverage`; reviewer=fresh-context:apr-may-books-20260903。
<!-- books-review:SF-2026-ARXIV-2605-02905:end -->

<!-- books-review:SF-2026-ARXIV-2605-02960:start --><!-- existing:SF-2026-ARXIV-2605-02960:start -->对读 `books/part-05-inference-system/43-prefill.md` 与相邻 `Ch21/Ch56` 后，现有命题为：本章的核心判断是：**Prefill 将整段 prompt 映射为第一个 next-token distribution 和逐层 KV state；它利用 token 维度并行换取高 GPU efficiency，但工作量、显存峰值和调度占用会随 prompt 长度快速增长。**<!-- existing:SF-2026-ARXIV-2605-02960:end --><!-- delta:SF-2026-ARXIV-2605-02960:start -->新增 evidence delta：Prefill-only MoE workloads can exchange activation all-to-all for asynchronous expert-weight all-gather when long compute windows hide transfer; the saturation threshold and traffic drift become routing state. 该 delta 已进入串行 Books writeback queue，作者通道未写共享 Books。<!-- delta:SF-2026-ARXIV-2605-02960:end --><!-- books-review:SF-2026-ARXIV-2605-02960:end -->

<!-- books-review:SF-2026-ARXIV-2605-02964:start --><!-- existing:SF-2026-ARXIV-2605-02964:start -->对读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻 `Ch31/Ch72` 后，现有命题为：本章的核心判断是：**Evaluation System 是把目标转化为可重复证据和受控决策的系统。它必须同时版本化被评估对象、输入分布、执行环境与 scorer，并显式表达不确定性、切片和风险；工具可以保存证据，但不能替组织定义什么算成功。**<!-- existing:SF-2026-ARXIV-2605-02964:end --><!-- delta:SF-2026-ARXIV-2605-02964:start -->新增 evidence delta：Tool-agent evaluation must distinguish nominal success from shortcut exploitation and vary horizon/complexity; environmental hardening can change the opportunity surface without changing weights. 该 evidence 未改变现有长期命题，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2605-02964:end --><!-- books-review:SF-2026-ARXIV-2605-02964:end -->

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

<!-- books-review:SF-ADVERSARIAL-RESEARCH-ORCHESTRATION:start -->
<!-- existing:SF-ADVERSARIAL-RESEARCH-ORCHESTRATION:start -->The current owner already states the durable mechanism boundary; this paper is a bounded supporting case and would duplicate the chapter spine.<!-- existing:SF-ADVERSARIAL-RESEARCH-ORCHESTRATION:end --> <!-- delta:SF-ADVERSARIAL-RESEARCH-ORCHESTRATION:start -->Multi-agent research should preserve source diversity, adversarial objections and adjudication provenance; more agents do not by themselves establish correctness.<!-- delta:SF-ADVERSARIAL-RESEARCH-ORCHESTRATION:end --> Decision remains `No Change — Existing Coverage`. Shared Books were not modified in this author lane.
<!-- books-review:SF-ADVERSARIAL-RESEARCH-ORCHESTRATION:end -->

<!-- books-review:SF-AGENT-SAFETY-OOD-ANALOGICAL-EVAL:start -->
<!-- existing:SF-AGENT-SAFETY-OOD-ANALOGICAL-EVAL:start -->The current owner already states the durable mechanism boundary; this paper is a bounded supporting case and would duplicate the chapter spine.<!-- existing:SF-AGENT-SAFETY-OOD-ANALOGICAL-EVAL:end --> <!-- delta:SF-AGENT-SAFETY-OOD-ANALOGICAL-EVAL:start -->Agent safety evaluation must test deceptive out-of-distribution transformations and trace judgment transfer, not only literal variants of known unsafe scenarios.<!-- delta:SF-AGENT-SAFETY-OOD-ANALOGICAL-EVAL:end --> Decision remains `No Change — Existing Coverage`. Shared Books were not modified in this author lane.
<!-- books-review:SF-AGENT-SAFETY-OOD-ANALOGICAL-EVAL:end -->

<!-- books-review:SF-AGENT-SEQUENTIAL-TRACE-VALIDATION:start -->
<!-- existing:SF-AGENT-SEQUENTIAL-TRACE-VALIDATION:start -->The current owner already states the durable mechanism boundary; this paper is a bounded supporting case and would duplicate the chapter spine.<!-- existing:SF-AGENT-SEQUENTIAL-TRACE-VALIDATION:end --> <!-- delta:SF-AGENT-SEQUENTIAL-TRACE-VALIDATION:start -->Agent success should be validated against essential state transitions learned from passing traces, not the agent's self-report or exact replay of one path.<!-- delta:SF-AGENT-SEQUENTIAL-TRACE-VALIDATION:end --> Decision remains `No Change — Existing Coverage`. Shared Books were not modified in this author lane.
<!-- books-review:SF-AGENT-SEQUENTIAL-TRACE-VALIDATION:end -->

<!-- books-review:SF-AI-DATACENTER-GRID-CODESIGN:start -->
<!-- existing:SF-AI-DATACENTER-GRID-CODESIGN:start -->The current owner already states the durable mechanism boundary; this paper is a bounded supporting case and would duplicate the chapter spine.<!-- existing:SF-AI-DATACENTER-GRID-CODESIGN:end --> <!-- delta:SF-AI-DATACENTER-GRID-CODESIGN:start -->AI capacity planning must include power-grid interconnection, temporal flexibility and curtailment as system constraints rather than treating electricity as an unlimited unit price.<!-- delta:SF-AI-DATACENTER-GRID-CODESIGN:end --> Decision remains `No Change — Existing Coverage`. Shared Books were not modified in this author lane.
<!-- books-review:SF-AI-DATACENTER-GRID-CODESIGN:end -->

<!-- books-review:SF-CYBER-DEFENSE-EXECUTOR-AUTHORITY:start -->
<!-- existing:SF-CYBER-DEFENSE-EXECUTOR-AUTHORITY:start -->The current owner already states the durable mechanism boundary; this paper is a bounded supporting case and would duplicate the chapter spine.<!-- existing:SF-CYBER-DEFENSE-EXECUTOR-AUTHORITY:end --> <!-- delta:SF-CYBER-DEFENSE-EXECUTOR-AUTHORITY:start -->Autonomous cyber defense requires executor-owned authorization, bounded effects and recovery receipts; model planning cannot itself commit network changes.<!-- delta:SF-CYBER-DEFENSE-EXECUTOR-AUTHORITY:end --> Decision remains `No Change — Existing Coverage`. Shared Books were not modified in this author lane.
<!-- books-review:SF-CYBER-DEFENSE-EXECUTOR-AUTHORITY:end -->

<!-- books-review:SF-DETERMINISTIC-COMPUTATION-EXECUTION:start -->
<!-- existing:SF-DETERMINISTIC-COMPUTATION-EXECUTION:start -->The current owner already states the durable mechanism boundary; this paper is a bounded supporting case and would duplicate the chapter spine.<!-- existing:SF-DETERMINISTIC-COMPUTATION-EXECUTION:end --> <!-- delta:SF-DETERMINISTIC-COMPUTATION-EXECUTION:start -->Deterministic computation should be delegated to typed execution and checked outputs when available; prompting remains a fallback, not the truth owner.<!-- delta:SF-DETERMINISTIC-COMPUTATION-EXECUTION:end --> Decision remains `No Change — Existing Coverage`. Shared Books were not modified in this author lane.
<!-- books-review:SF-DETERMINISTIC-COMPUTATION-EXECUTION:end -->

<!-- books-review:SF-DIFFUSION-PLANNING-COMMIT-REFINE:start -->
<!-- existing:SF-DIFFUSION-PLANNING-COMMIT-REFINE:start -->The current owner already states the durable mechanism boundary; this paper is a bounded supporting case and would duplicate the chapter spine.<!-- existing:SF-DIFFUSION-PLANNING-COMMIT-REFINE:end --> <!-- delta:SF-DIFFUSION-PLANNING-COMMIT-REFINE:start -->Diffusion planning exposes iterative proposal/correction state, but executable commit still belongs to a feasibility verifier and controller.<!-- delta:SF-DIFFUSION-PLANNING-COMMIT-REFINE:end --> Decision remains `No Change — Existing Coverage`. Shared Books were not modified in this author lane.
<!-- books-review:SF-DIFFUSION-PLANNING-COMMIT-REFINE:end -->

<!-- books-review:SF-DITRON-DISTRIBUTED-TILING:start -->
<!-- existing:SF-DITRON-DISTRIBUTED-TILING:start -->已对读当前 owner `books/part-05-inference-system/49-tensorrt-llm.md#L10` 与相邻 handoff `books/part-05-inference-system/48-speculative-decoding.md#L10; books/part-05-inference-system/50-vllm.md#L10`。Execution Engine 已区分 compiler plan 与 runtime/kernel execution，也保留库路径 fallback；现有主线仍以单设备 tiling 为主，没有 topology/health 驱动的分布式层级。<!-- existing:SF-DITRON-DISTRIBUTED-TILING:end -->
<!-- delta:SF-DITRON-DISTRIBUTED-TILING:start -->把执行引擎章节从单设备 kernel 扩展到 hierarchical distributed tiling，明确 compiler owns plan、runtime owns topology/health、库路径作为稳定 fallback。<!-- delta:SF-DITRON-DISTRIBUTED-TILING:end -->
结论：**Integrate**。
<!-- books-review:SF-DITRON-DISTRIBUTED-TILING:end -->

<!-- books-review:SF-JBSHIELD-ADAPTIVE-REPRESENTATION-DEFENSE:start -->
<!-- existing:SF-JBSHIELD-ADAPTIVE-REPRESENTATION-DEFENSE:start -->The current owner already states the durable mechanism boundary; this paper is a bounded supporting case and would duplicate the chapter spine.<!-- existing:SF-JBSHIELD-ADAPTIVE-REPRESENTATION-DEFENSE:end --> <!-- delta:SF-JBSHIELD-ADAPTIVE-REPRESENTATION-DEFENSE:start -->Representation-level jailbreak shields must be tested against adaptive attacks and distribution shift; linear separation on a fixed attack set is not a security boundary.<!-- delta:SF-JBSHIELD-ADAPTIVE-REPRESENTATION-DEFENSE:end --> Decision remains `No Change — Existing Coverage`. Shared Books were not modified in this author lane.
<!-- books-review:SF-JBSHIELD-ADAPTIVE-REPRESENTATION-DEFENSE:end -->

<!-- books-review:SF-KERNCAP-AMD-KERNEL-ISOLATION:start -->
<!-- existing:SF-KERNCAP-AMD-KERNEL-ISOLATION:start -->The current owner already states the durable mechanism boundary; this paper is a bounded supporting case and would duplicate the chapter spine.<!-- existing:SF-KERNCAP-AMD-KERNEL-ISOLATION:end --> <!-- delta:SF-KERNCAP-AMD-KERNEL-ISOLATION:start -->Kernel extraction needs automated dependency capture and isolation so compiler/runtime experiments are reproducible rather than tied to an opaque application build.<!-- delta:SF-KERNCAP-AMD-KERNEL-ISOLATION:end --> Decision remains `No Change — Existing Coverage`. Shared Books were not modified in this author lane.
<!-- books-review:SF-KERNCAP-AMD-KERNEL-ISOLATION:end -->

<!-- books-review:SF-MAGE-SHADOW-MEMORY-THREAT-STATE:start -->
<!-- existing:SF-MAGE-SHADOW-MEMORY-THREAT-STATE:start -->The current owner already states the durable mechanism boundary; this paper is a bounded supporting case and would duplicate the chapter spine.<!-- existing:SF-MAGE-SHADOW-MEMORY-THREAT-STATE:end --> <!-- delta:SF-MAGE-SHADOW-MEMORY-THREAT-STATE:start -->A separate shadow memory can accumulate threat evidence without contaminating productive memory, but its write policy and intervention authority need independent ownership.<!-- delta:SF-MAGE-SHADOW-MEMORY-THREAT-STATE:end --> Decision remains `No Change — Existing Coverage`. Shared Books were not modified in this author lane.
<!-- books-review:SF-MAGE-SHADOW-MEMORY-THREAT-STATE:end -->

<!-- books-review:SF-MULTITURN-DEPENDENCY-AWARE-PRIVACY:start -->
<!-- existing:SF-MULTITURN-DEPENDENCY-AWARE-PRIVACY:start -->The current owner already states the durable mechanism boundary; this paper is a bounded supporting case and would duplicate the chapter spine.<!-- existing:SF-MULTITURN-DEPENDENCY-AWARE-PRIVACY:end --> <!-- delta:SF-MULTITURN-DEPENDENCY-AWARE-PRIVACY:start -->Multi-turn privacy accounting must preserve dependency among prompts, tools and memory; per-turn checks do not compose into a session guarantee.<!-- delta:SF-MULTITURN-DEPENDENCY-AWARE-PRIVACY:end --> Decision remains `No Change — Existing Coverage`. Shared Books were not modified in this author lane.
<!-- books-review:SF-MULTITURN-DEPENDENCY-AWARE-PRIVACY:end -->

<!-- books-review:SF-OBSERVATIONAL-WORKFLOW-SKILL-LEARNING:start -->
<!-- existing:SF-OBSERVATIONAL-WORKFLOW-SKILL-LEARNING:start -->The current owner already states the durable mechanism boundary; this paper is a bounded supporting case and would duplicate the chapter spine.<!-- existing:SF-OBSERVATIONAL-WORKFLOW-SKILL-LEARNING:end --> <!-- delta:SF-OBSERVATIONAL-WORKFLOW-SKILL-LEARNING:start -->Learning automation from observation requires provenance, validation and admission of the induced workflow before it may execute; imitation does not transfer user authority.<!-- delta:SF-OBSERVATIONAL-WORKFLOW-SKILL-LEARNING:end --> Decision remains `No Change — Existing Coverage`. Shared Books were not modified in this author lane.
<!-- books-review:SF-OBSERVATIONAL-WORKFLOW-SKILL-LEARNING:end -->

<!-- books-review:SF-ONLINE-CORRECTION-RECOVERY-SHIFT:start -->
<!-- existing:SF-ONLINE-CORRECTION-RECOVERY-SHIFT:start -->The current owner already states the durable mechanism boundary; this paper is a bounded supporting case and would duplicate the chapter spine.<!-- existing:SF-ONLINE-CORRECTION-RECOVERY-SHIFT:end --> <!-- delta:SF-ONLINE-CORRECTION-RECOVERY-SHIFT:start -->Recovery evaluation must measure time-to-detect, correction state and post-shift rollback rather than only final recovered accuracy.<!-- delta:SF-ONLINE-CORRECTION-RECOVERY-SHIFT:end --> Decision remains `No Change — Existing Coverage`. Shared Books were not modified in this author lane.
<!-- books-review:SF-ONLINE-CORRECTION-RECOVERY-SHIFT:end -->

<!-- books-review:SF-PACT-AGENT-CHOREOGRAPHY:start -->
<!-- existing:SF-PACT-AGENT-CHOREOGRAPHY:start -->The current owner already states the durable mechanism boundary; this paper is a bounded supporting case and would duplicate the chapter spine.<!-- existing:SF-PACT-AGENT-CHOREOGRAPHY:end --> <!-- delta:SF-PACT-AGENT-CHOREOGRAPHY:start -->Agent ecosystems need a versioned choreography that defines role/message order and failure semantics before local implementations; generated endpoints cannot redefine the global protocol.<!-- delta:SF-PACT-AGENT-CHOREOGRAPHY:end --> Decision remains `No Change — Existing Coverage`. Shared Books were not modified in this author lane.
<!-- books-review:SF-PACT-AGENT-CHOREOGRAPHY:end -->

<!-- books-review:SF-PREGENERATION-ANSWERABILITY-GEOMETRY:start -->
<!-- existing:SF-PREGENERATION-ANSWERABILITY-GEOMETRY:start -->The current owner already states the durable mechanism boundary; this paper is a bounded supporting case and would duplicate the chapter spine.<!-- existing:SF-PREGENERATION-ANSWERABILITY-GEOMETRY:end --> <!-- delta:SF-PREGENERATION-ANSWERABILITY-GEOMETRY:start -->Pre-generation representation geometry is a bounded abstention sensor; it does not by itself provide calibrated claim confidence or an evidence-backed answer.<!-- delta:SF-PREGENERATION-ANSWERABILITY-GEOMETRY:end --> Decision remains `No Change — Existing Coverage`. Shared Books were not modified in this author lane.
<!-- books-review:SF-PREGENERATION-ANSWERABILITY-GEOMETRY:end -->

<!-- books-review:SF-REFUSAL-TRAJECTORY-MONITOR:start -->
<!-- existing:SF-REFUSAL-TRAJECTORY-MONITOR:start -->已对读当前 owner `books/part-06-ai-infrastructure/72-security.md#L10` 与相邻 handoff `books/part-06-ai-infrastructure/66-evaluation-system.md#L10; books/part-07-agent/78-tool-calling.md#L10`。Security 与 Evaluation 已要求沿 trajectory 观察 policy/refusal 状态、区分 refusal 与安全性，并以 action boundary 执行 gate；新监测器未改变 enforcement owner。<!-- existing:SF-REFUSAL-TRAJECTORY-MONITOR:end -->
<!-- delta:SF-REFUSAL-TRAJECTORY-MONITOR:start -->trajectory monitor 提供局部检测案例，但未改变 refusal 不是 safety proof、最终 enforcement 位于 action boundary 的既有结论。<!-- delta:SF-REFUSAL-TRAJECTORY-MONITOR:end -->
结论：**No Change — Existing Coverage**。
<!-- books-review:SF-REFUSAL-TRAJECTORY-MONITOR:end -->

<!-- books-review:SF-REPOSITORY-GRAPH-REPAIR-PROVENANCE:start -->
<!-- existing:SF-REPOSITORY-GRAPH-REPAIR-PROVENANCE:start -->The current owner already states the durable mechanism boundary; this paper is a bounded supporting case and would duplicate the chapter spine.<!-- existing:SF-REPOSITORY-GRAPH-REPAIR-PROVENANCE:end --> <!-- delta:SF-REPOSITORY-GRAPH-REPAIR-PROVENANCE:start -->Repository repair should preserve graph snapshot, tool action and test provenance; a generated patch is not authoritative until executable acceptance succeeds.<!-- delta:SF-REPOSITORY-GRAPH-REPAIR-PROVENANCE:end --> Decision remains `No Change — Existing Coverage`. Shared Books were not modified in this author lane.
<!-- books-review:SF-REPOSITORY-GRAPH-REPAIR-PROVENANCE:end -->

<!-- books-review:SF-ROUTEHIJACK-MOE-SAFETY-ROUTING:start -->
<!-- existing:SF-ROUTEHIJACK-MOE-SAFETY-ROUTING:start -->已逐章核对 `books/part-06-ai-infrastructure/72-security.md` 的“Policy-bound Sensor；Safety Evaluation；Supply-chain Integrity；Prompt Injection 与 Tool Boundary”：现章已把安全判定建立在资产、信任边界、能力控制与 safe commit 上；缺少多模态攻击、MoE routing、RAG membership、技能/IR certificate、unlearning retain-set 及 trajectory risk 的新攻击面与证据边界。<!-- existing:SF-ROUTEHIJACK-MOE-SAFETY-ROUTING:end --> <!-- delta:SF-ROUTEHIJACK-MOE-SAFETY-ROUTING:start -->exact-v1 新增 delta 是“MoE routing is part of the safety attack surface because input optimization can steer traffic away from safety-associated experts.”。<!-- delta:SF-ROUTEHIJACK-MOE-SAFETY-ROUTING:end --> 相邻章节 `books/part-06-ai-infrastructure/71-multi-tenant.md`、`books/part-06-ai-infrastructure/73-production-best-practice.md` 只保留 handoff。正文写回位于 `books/part-06-ai-infrastructure/72-security.md#L182-L185`，并由 `post-write-audit-v1:SF-ROUTEHIJACK-MOE-SAFETY-ROUTING` 验证；状态为 integrated/post-write-passed。
<!-- books-review:SF-ROUTEHIJACK-MOE-SAFETY-ROUTING:end -->

<!-- books-review:SF-SAE-PAIRWISE-CAUSAL-AXIS-AUDIT:start -->
<!-- existing:SF-SAE-PAIRWISE-CAUSAL-AXIS-AUDIT:start -->The current owner already states the durable mechanism boundary; this paper is a bounded supporting case and would duplicate the chapter spine.<!-- existing:SF-SAE-PAIRWISE-CAUSAL-AXIS-AUDIT:end --> <!-- delta:SF-SAE-PAIRWISE-CAUSAL-AXIS-AUDIT:start -->Single-feature SAE labels can name an activation regime rather than a causal axis; pairwise intervention structure is needed before interpretability claims enter evidence.<!-- delta:SF-SAE-PAIRWISE-CAUSAL-AXIS-AUDIT:end --> Decision remains `No Change — Existing Coverage`. Shared Books were not modified in this author lane.
<!-- books-review:SF-SAE-PAIRWISE-CAUSAL-AXIS-AUDIT:end -->

<!-- books-review:SF-SELF-MINED-HARDNESS-SAFETY-FT:start -->
<!-- existing:SF-SELF-MINED-HARDNESS-SAFETY-FT:start -->The current owner already states the durable mechanism boundary; this paper is a bounded supporting case and would duplicate the chapter spine.<!-- existing:SF-SELF-MINED-HARDNESS-SAFETY-FT:end --> <!-- delta:SF-SELF-MINED-HARDNESS-SAFETY-FT:start -->Safety fine-tuning should mine current-policy hard examples and preserve a replay boundary; static refusal data cannot track the policy's evolving failure surface.<!-- delta:SF-SELF-MINED-HARDNESS-SAFETY-FT:end --> Decision remains `No Change — Existing Coverage`. Shared Books were not modified in this author lane.
<!-- books-review:SF-SELF-MINED-HARDNESS-SAFETY-FT:end -->

<!-- books-review:SF-SPARSE-MEMORY-FINETUNING:start -->
<!-- existing:SF-SPARSE-MEMORY-FINETUNING:start -->The current owner already states the durable mechanism boundary; this paper is a bounded supporting case and would duplicate the chapter spine.<!-- existing:SF-SPARSE-MEMORY-FINETUNING:end --> <!-- delta:SF-SPARSE-MEMORY-FINETUNING:start -->Sparse trainable memory is an alternative adaptation-state representation whose value must be measured jointly on target learning and forgetting; it does not dominate LoRA or full finetuning.<!-- delta:SF-SPARSE-MEMORY-FINETUNING:end --> Decision remains `No Change — Existing Coverage`. Shared Books were not modified in this author lane.
<!-- books-review:SF-SPARSE-MEMORY-FINETUNING:end -->

<!-- books-review:SF-VDCORES-ASYNC-GPU-RESOURCE-DECOUPLING:start -->
<!-- existing:SF-VDCORES-ASYNC-GPU-RESOURCE-DECOUPLING:start -->Current Ch49 owns execution plans and scheduling, but lacks virtual execution-resource binding that decouples asynchronous work from fixed physical GPU cores.<!-- existing:SF-VDCORES-ASYNC-GPU-RESOURCE-DECOUPLING:end --> <!-- delta:SF-VDCORES-ASYNC-GPU-RESOURCE-DECOUPLING:start -->Asynchronous GPU execution benefits from decoupling virtual execution resources from physical cores, making resource binding a runtime scheduling decision.<!-- delta:SF-VDCORES-ASYNC-GPU-RESOURCE-DECOUPLING:end --> Decision remains `Integrate`. Shared Books were not modified in this author lane.
<!-- books-review:SF-VDCORES-ASYNC-GPU-RESOURCE-DECOUPLING:end -->

<!-- books-review:SF-WEB-PII-DEFENSIVE-PROMPT-THREAT:start -->
<!-- existing:SF-WEB-PII-DEFENSIVE-PROMPT-THREAT:start -->The current owner already states the durable mechanism boundary; this paper is a bounded supporting case and would duplicate the chapter spine.<!-- existing:SF-WEB-PII-DEFENSIVE-PROMPT-THREAT:end --> <!-- delta:SF-WEB-PII-DEFENSIVE-PROMPT-THREAT:start -->Page-side defensive prompts are adversarial content and at most a bounded mitigation sensor; providers still need sanitization, information-flow policy and output authorization.<!-- delta:SF-WEB-PII-DEFENSIVE-PROMPT-THREAT:end --> Decision remains `No Change — Existing Coverage`. Shared Books were not modified in this author lane.
<!-- books-review:SF-WEB-PII-DEFENSIVE-PROMPT-THREAT:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260506-COVERAGE | fresh-context:owner-replay-20260903 | coverage | coverage:SRC-ARXIV:20260506 | none | raw/retained/closure/withdrawn conservation and initial-created owner mapping independently recounted | passed |
| SA-20260506-EVIDENCE | fresh-context:owner-replay-20260903 | evidence | validator:review-completion-v1 | none | every frozen family has a completed exact-version receipt; blocked=0 | passed |
| SA-20260506-SELECTION | fresh-context:owner-replay-20260903 | deep_analysis_selection | validator:deep-analysis-selection-v1 | none | eligible=60；selected=3；all others retain completed reviews | passed |
| SA-20260506-BOOKS | fresh-context:apr-may-books-20260903 | books | validator:books-comparison-v1 | none | — | passed |

## 8. Ignored Noise

- Pre-denominator closures=430；逐 family 理由保存在 owner receipt。
- Withdrawn=0；只保留审计 closure，不进入候选、评分、Review 或 Books。
- `updated` / current OAI datestamp 的 revision 噪声不拥有 Daily。

## 9. Recommended Action

本日全部 Gate 已闭合，无进一步动作。

## 10. Repository Changes

- Owner receipt（本阶段只读）：`papers/2026/05/_sources/arxiv-owner-replay-20260903/20260506/arxiv-owner-receipt.json`
- Canonical ledger（Books terminal state）：`papers/2026/05/_sources/arxiv-owner-replay-20260903/20260506/canonical-ledger.json`
- Books queue（fresh-context decision）：`papers/2026/05/_sources/arxiv-owner-replay-20260903/BOOKS_WRITEBACK_QUEUE.json`
- Superseded report：`papers/2026/05/_sources/arxiv-owner-replay-20260903/legacy-reports-before-created-owner-reconciliation/2026-05-06.md`
- Books body: no change for the recovered families on this date.

## 11. Open Questions

- 无。

## 12. Sources

- [DataCite REST API](https://api.datacite.org/dois) — initial `created` owner-day proxy；`updated` 只作 revision provenance。
- [arXiv OAI](https://export.arxiv.org/oai2) — identity/date corroboration；current datestamp 不拥有 first-public day。
- [arXiv](https://arxiv.org/) — exact-v1 abstract、HTML/PDF 与 version history。

## 13. Final Status

Completion Status: Complete; Coverage: Closed; Evidence: Passed; Books: Passed; unresolved findings=0
