# Daily Research — 2026-05-04

**Research Date:** 2026-05-04

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-05-03 09:00:00 ～ 2026-05-04 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Historical Daily Independent Full Replay

**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed；initial-created owner replay 与 exact-v1 Evidence Review 已完成。

## Executive Summary

本次独立重放枚举并逐项闭合 387 个注册 arXiv identity，冻结 37 个 Source Family；pre-denominator closure=350，withdrawn pre-denominator=0。37 个旧候选被迁回正确 owner day，0 个漏检 family 已恢复 exact-v1 全文并完成 Source Review。

DataCite `created` 仅作为 initial DOI registration 的 owner-day proxy；`updated`、v1 Updated 与 current OAI datestamp 只记录 revision provenance，不决定 first-public owner。机制结论只绑定 exact-v1 正文。 本日所有 Books disposition 已有终态。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-05-04 |
| Window End | 2026-05-04 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | DEN-20260504-CREATED-4205e9a11dfec12a |
| Denominator Frozen At | 2026-09-03T12:36:05+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-05-03T09:00:00+08:00 | 2026-05-04T09:00:00+08:00 | 2026-09-03T12:36:05+08:00 | DataCite prefix 10.48550 initial created-day inventory + registered arXiv categories + exact-v1 identity/body | checked | 387 | SF-2026-ARXIV-2605-00066;SF-2026-ARXIV-2605-00081;SF-2026-ARXIV-2605-00136;SF-2026-ARXIV-2605-00155;SF-2026-ARXIV-2605-00161;SF-2026-ARXIV-2605-00180;SF-2026-ARXIV-2605-00206;SF-2026-ARXIV-2605-00226;SF-2026-ARXIV-2605-00254;SF-2026-ARXIV-2605-00267;SF-2026-ARXIV-2605-00300;SF-2026-ARXIV-2605-00314;SF-AEM-AGENTIC-RL-ENTROPY-CREDIT;SF-AFFORDANCE-HARNESS-VERIFICATION-GATED-SKILLS;SF-AGENT-CAPSULES-QUALITY-GATED-GRANULARITY;SF-AGOQ-ACTIVATION-GRADIENT-QUANTIZATION;SF-AUTOMAT-CLAIM-REPRODUCTION-CONTRACT;SF-BREW-WATERMARK-DESIGNATED-VERIFICATION;SF-CLEANBASE-RAG-DOCUMENT-GRAPH;SF-EVICT-MOE-VERIFICATION-UTILITY;SF-EVOLVING-MEMORY-TWO-STAGE-OPTIMIZATION;SF-FORWARD-REPLAY-MODEL-EDIT-TARGETS;SF-IEFF-CONTINUOUS-FEATURE-FADING;SF-LIGHTKV-PROMPT-GUIDED-VISION-KV;SF-LLM-EMU-NATIVE-RUNTIME-EMULATION;SF-LWD-FLEET-OFFLINE-ONLINE-ROBOT-RL;SF-MATHARENA-LIVING-EVALUATION;SF-MEMROUTER-WRITE-ADMISSION;SF-PERSEUS-MEGAKERNEL-SIGNAL-ORDERING;SF-PROMPT-SCORE-VARIANCE-RELIABILITY;SF-RUNAGENT-CONSTRAINT-GUIDED-EXECUTION;SF-SAGA-WORKFLOW-ATOMIC-SCHEDULING;SF-SIMFA-ASYNC-GPU-SIMULATION;SF-SKILL-VERIFIABLE-ARTIFACT;SF-TOOL-CALL-UTILITY-GATE;SF-UCPO-CORRECT-SOLUTION-DIVERSITY;SF-VLM-VISUAL-JAILBREAK-CROSS-MODAL-GAP | created-day pages=closed; OAI category sets=closed; direct same-day OAI=269 | 2026-05-04T09:00:00+08:00 | coverage:SRC-ARXIV:20260504 | — |

<!-- coverage:SRC-ARXIV:20260504:start -->全量 raw inventory=387；每个 identity 均具有 retained、family-specific closure 或 withdrawn terminal closure。候选 owner 由 initial DataCite created、arXiv ID month、v1 history 与 announcement cadence 共同约束；冲突不由 updated 字段覆盖。<!-- coverage:SRC-ARXIV:20260504:end -->

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
| SF-2026-ARXIV-2605-00066 | arXiv:2605.00066v1 | paper-v1:2605.00066 | 2026-W19 | 2026-05-04 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-00066 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-00066 | yes |
| SF-2026-ARXIV-2605-00081 | arXiv:2605.00081v1 | paper-v1:2605.00081 | 2026-W19 | 2026-05-04 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | release_security_contract | review:SF-2026-ARXIV-2605-00081 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-00081 | yes |
| SF-2026-ARXIV-2605-00136 | arXiv:2605.00136v1 | paper-v1:2605.00136 | 2026-W19 | 2026-05-04 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-00136 | self | — | new_in_window | AGENT-TOOL-CALLING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-00136 | yes |
| SF-2026-ARXIV-2605-00155 | arXiv:2605.00155v1 | paper-v1:2605.00155 | 2026-W19 | 2026-05-04 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2605-00155 | self | — | new_in_window | TRAIN-RLHF | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-00155 | yes |
| SF-2026-ARXIV-2605-00161 | arXiv:2605.00161v1 | paper-v1:2605.00161 | 2026-W19 | 2026-05-04 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-00161 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-00161 | yes |
| SF-2026-ARXIV-2605-00180 | arXiv:2605.00180v1 | paper-v1:2605.00180 | 2026-W19 | 2026-05-04 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-00180 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-00180 | yes |
| SF-2026-ARXIV-2605-00206 | arXiv:2605.00206v1 | paper-v1:2605.00206 | 2026-W19 | 2026-05-04 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-00206 | self | — | new_in_window | MODEL-DECODER-ONLY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-00206 | yes |
| SF-2026-ARXIV-2605-00226 | arXiv:2605.00226v1 | paper-v1:2605.00226 | 2026-W19 | 2026-05-04 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-00226 | self | — | new_in_window | AGENT-PLANNING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-00226 | yes |
| SF-2026-ARXIV-2605-00254 | arXiv:2605.00254v1 | paper-v1:2605.00254 | 2026-W19 | 2026-05-04 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-00254 | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-2026-ARXIV-2605-00254 | yes |
| SF-2026-ARXIV-2605-00267 | arXiv:2605.00267v1 | paper-v1:2605.00267 | 2026-W19 | 2026-05-04 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | release_security_contract | review:SF-2026-ARXIV-2605-00267 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-00267 | yes |
| SF-2026-ARXIV-2605-00300 | arXiv:2605.00300v1 | paper-v1:2605.00300 | 2026-W19 | 2026-05-04 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-00300 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2605-00300 | yes |
| SF-2026-ARXIV-2605-00314 | arXiv:2605.00314v1 | paper-v1:2605.00314 | 2026-W19 | 2026-05-04 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | release_security_contract | review:SF-2026-ARXIV-2605-00314 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2605-00314 | yes |
| SF-AEM-AGENTIC-RL-ENTROPY-CREDIT | arXiv:2605.00425v1 | paper-v1:2605.00425 | 2026-W19 | 2026-05-04 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-AEM-AGENTIC-RL-ENTROPY-CREDIT | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-AEM-AGENTIC-RL-ENTROPY-CREDIT | yes |
| SF-AFFORDANCE-HARNESS-VERIFICATION-GATED-SKILLS | arXiv:2605.00663v1 | paper-v1:2605.00663 | 2026-W19 | 2026-05-04 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-AFFORDANCE-HARNESS-VERIFICATION-GATED-SKILLS | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-AFFORDANCE-HARNESS-VERIFICATION-GATED-SKILLS | yes |
| SF-AGENT-CAPSULES-QUALITY-GATED-GRANULARITY | arXiv:2605.00410v1 | paper-v1:2605.00410 | 2026-W19 | 2026-05-04 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-AGENT-CAPSULES-QUALITY-GATED-GRANULARITY | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-AGENT-CAPSULES-QUALITY-GATED-GRANULARITY | yes |
| SF-AGOQ-ACTIVATION-GRADIENT-QUANTIZATION | arXiv:2605.00539v1 | paper-v1:2605.00539 | 2026-W19 | 2026-05-04 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-AGOQ-ACTIVATION-GRADIENT-QUANTIZATION | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | No Change — Existing Coverage | books-review:SF-AGOQ-ACTIVATION-GRADIENT-QUANTIZATION | yes |
| SF-AUTOMAT-CLAIM-REPRODUCTION-CONTRACT | arXiv:2605.00803v1 | paper-v1:2605.00803 | 2026-W19 | 2026-05-04 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-AUTOMAT-CLAIM-REPRODUCTION-CONTRACT | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-AUTOMAT-CLAIM-REPRODUCTION-CONTRACT | yes |
| SF-BREW-WATERMARK-DESIGNATED-VERIFICATION | arXiv:2605.00348v1 | paper-v1:2605.00348 | 2026-W19 | 2026-05-04 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-BREW-WATERMARK-DESIGNATED-VERIFICATION | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-BREW-WATERMARK-DESIGNATED-VERIFICATION | yes |
| SF-CLEANBASE-RAG-DOCUMENT-GRAPH | arXiv:2605.00460v1 | paper-v1:2605.00460 | 2026-W19 | 2026-05-04 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-CLEANBASE-RAG-DOCUMENT-GRAPH | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-CLEANBASE-RAG-DOCUMENT-GRAPH | yes |
| SF-EVICT-MOE-VERIFICATION-UTILITY | arXiv:2605.00342v1 | paper-v1:2605.00342 | 2026-W19 | 2026-05-04 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-EVICT-MOE-VERIFICATION-UTILITY | self | — | new_in_window | INFER-SPECULATIVE-DECODING | No Change — Existing Coverage | books-review:SF-EVICT-MOE-VERIFICATION-UTILITY | yes |
| SF-EVOLVING-MEMORY-TWO-STAGE-OPTIMIZATION | arXiv:2605.00702v1 | paper-v1:2605.00702 | 2026-W19 | 2026-05-04 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-EVOLVING-MEMORY-TWO-STAGE-OPTIMIZATION | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-EVOLVING-MEMORY-TWO-STAGE-OPTIMIZATION | yes |
| SF-FORWARD-REPLAY-MODEL-EDIT-TARGETS | arXiv:2605.00358v1 | paper-v1:2605.00358 | 2026-W19 | 2026-05-04 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-FORWARD-REPLAY-MODEL-EDIT-TARGETS | self | — | new_in_window | — | Structural Candidate | books-review:SF-FORWARD-REPLAY-MODEL-EDIT-TARGETS | yes |
| SF-IEFF-CONTINUOUS-FEATURE-FADING | arXiv:2605.00324v1 | paper-v1:2605.00324 | 2026-W19 | 2026-05-04 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-IEFF-CONTINUOUS-FEATURE-FADING | self | — | new_in_window | PLATFORM-PRODUCTION | Integrate | books-review:SF-IEFF-CONTINUOUS-FEATURE-FADING | yes |
| SF-LIGHTKV-PROMPT-GUIDED-VISION-KV | arXiv:2605.00789v1 | paper-v1:2605.00789 | 2026-W19 | 2026-05-04 | SRC-ARXIV | 2 | 3 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-LIGHTKV-PROMPT-GUIDED-VISION-KV | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-LIGHTKV-PROMPT-GUIDED-VISION-KV | yes |
| SF-LLM-EMU-NATIVE-RUNTIME-EMULATION | arXiv:2605.00616v1 | paper-v1:2605.00616 | 2026-W19 | 2026-05-04 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-LLM-EMU-NATIVE-RUNTIME-EMULATION | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-LLM-EMU-NATIVE-RUNTIME-EMULATION | yes |
| SF-LWD-FLEET-OFFLINE-ONLINE-ROBOT-RL | arXiv:2605.00416v1 | paper-v1:2605.00416 | 2026-W19 | 2026-05-04 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-LWD-FLEET-OFFLINE-ONLINE-ROBOT-RL | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Integrate | books-review:SF-LWD-FLEET-OFFLINE-ONLINE-ROBOT-RL | yes |
| SF-MATHARENA-LIVING-EVALUATION | arXiv:2605.00674v1 | paper-v1:2605.00674 | 2026-W19 | 2026-05-04 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-MATHARENA-LIVING-EVALUATION | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-MATHARENA-LIVING-EVALUATION | yes |
| SF-MEMROUTER-WRITE-ADMISSION | arXiv:2605.00356v1 | paper-v1:2605.00356 | 2026-W19 | 2026-05-04 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-MEMROUTER-WRITE-ADMISSION | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-MEMROUTER-WRITE-ADMISSION | yes |
| SF-PERSEUS-MEGAKERNEL-SIGNAL-ORDERING | arXiv:2605.00686v1 | paper-v1:2605.00686 | 2026-W19 | 2026-05-04 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-PERSEUS-MEGAKERNEL-SIGNAL-ORDERING | self | — | new_in_window | INFER-TENSORRT-LLM | Integrate | books-review:SF-PERSEUS-MEGAKERNEL-SIGNAL-ORDERING | yes |
| SF-PROMPT-SCORE-VARIANCE-RELIABILITY | arXiv:2605.00326v1 | paper-v1:2605.00326 | 2026-W19 | 2026-05-04 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-PROMPT-SCORE-VARIANCE-RELIABILITY | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-PROMPT-SCORE-VARIANCE-RELIABILITY | yes |
| SF-RUNAGENT-CONSTRAINT-GUIDED-EXECUTION | arXiv:2605.00798v1 | paper-v1:2605.00798 | 2026-W19 | 2026-05-04 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-RUNAGENT-CONSTRAINT-GUIDED-EXECUTION | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-RUNAGENT-CONSTRAINT-GUIDED-EXECUTION | yes |
| SF-SAGA-WORKFLOW-ATOMIC-SCHEDULING | arXiv:2605.00528v1 | paper-v1:2605.00528 | 2026-W19 | 2026-05-04 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-SAGA-WORKFLOW-ATOMIC-SCHEDULING | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-SAGA-WORKFLOW-ATOMIC-SCHEDULING | yes |
| SF-SIMFA-ASYNC-GPU-SIMULATION | arXiv:2605.00555v1 | paper-v1:2605.00555 | 2026-W19 | 2026-05-04 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-SIMFA-ASYNC-GPU-SIMULATION | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-SIMFA-ASYNC-GPU-SIMULATION | yes |
| SF-SKILL-VERIFIABLE-ARTIFACT | arXiv:2605.00424v1 | paper-v1:2605.00424 | 2026-W19 | 2026-05-04 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-SKILL-VERIFIABLE-ARTIFACT | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-SKILL-VERIFIABLE-ARTIFACT | yes |
| SF-TOOL-CALL-UTILITY-GATE | arXiv:2605.00737v1 | paper-v1:2605.00737 | 2026-W19 | 2026-05-04 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-TOOL-CALL-UTILITY-GATE | self | — | new_in_window | AGENT-TOOL-CALLING | Integrate | books-review:SF-TOOL-CALL-UTILITY-GATE | yes |
| SF-UCPO-CORRECT-SOLUTION-DIVERSITY | arXiv:2605.00365v1 | paper-v1:2605.00365 | 2026-W19 | 2026-05-04 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-UCPO-CORRECT-SOLUTION-DIVERSITY | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-UCPO-CORRECT-SOLUTION-DIVERSITY | yes |
| SF-VLM-VISUAL-JAILBREAK-CROSS-MODAL-GAP | arXiv:2605.00583v1 | paper-v1:2605.00583 | 2026-W19 | 2026-05-04 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-VLM-VISUAL-JAILBREAK-CROSS-MODAL-GAP | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-VLM-VISUAL-JAILBREAK-CROSS-MODAL-GAP | yes |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-00066 | RP-b256a98e02edce7e | deep | arXiv:2605.00066v1 | SRC-ARXIV@arXiv:2605.00066v1 | https://arxiv.org/html/2605.00066v1 — §3 cross-benchmark metric mapping and correlation protocol | https://arxiv.org/html/2605.00066v1 — §4 NAVSIM and Bench2Drive cross-benchmark results and sensitivity | https://arxiv.org/html/2605.00066v1 — §5 selected benchmarks/models and correlation do not establish causality or real-world safety | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2605-00066 | complete |
| SF-2026-ARXIV-2605-00081 | RP-f14b7451bc2abe88 | deep | arXiv:2605.00081v1 | SRC-ARXIV@arXiv:2605.00081v1 | https://arxiv.org/html/2605.00081v1 — §2-6 threat assumptions, contract language, dual-layer observability and enforcement | https://arxiv.org/html/2605.00081v1 — §7 examples and policy-composition analysis | https://arxiv.org/html/2605.00081v1 — §8 impossibility/scope boundary; disclosed framework is not proof of all semantic safety | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2605-00081 | complete |
| SF-2026-ARXIV-2605-00136 | RP-0c1e52b0f31dc627 | deep | arXiv:2605.00136v1 | SRC-ARXIV@arXiv:2605.00136v1 | https://arxiv.org/html/2605.00136v1 — §3-4 decomposition of tool protocol, selection and execution costs | https://arxiv.org/html/2605.00136v1 — §5 controlled tool-use diagnosis across models/tasks | https://arxiv.org/html/2605.00136v1 — §6/discussion task and framework scope; no universal tax constant | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2605-00136 | complete |
| SF-2026-ARXIV-2605-00155 | RP-04a48ab11447f01c | standard | arXiv:2605.00155v1 | SRC-ARXIV@arXiv:2605.00155v1 | https://arxiv.org/html/2605.00155v1 — §3-5 Wasserstein ambiguity set and robust regret objective | https://arxiv.org/html/2605.00155v1 — §6 experiments and ablations on specified preference datasets/models | Not Disclosed — exact-v1 has no dedicated limitations section; author experiments do not establish universal robustness radius | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2605-00155 | complete |
| SF-2026-ARXIV-2605-00161 | RP-aa657a548813d802 | deep | arXiv:2605.00161v1 | SRC-ARXIV@arXiv:2605.00161v1 | https://arxiv.org/html/2605.00161v1 — §2-3 consistency objective and diffusion language-model mechanism | https://arxiv.org/html/2605.00161v1 — §4-5 language-model evaluations and ablations | https://arxiv.org/html/2605.00161v1 — §6 Conclusion — exact-v1 has no dedicated limitations section; workloads do not prove replacement of autoregressive generation | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2605-00161 | complete |
| SF-2026-ARXIV-2605-00180 | RP-e93e4da3b4fae9c2 | deep | arXiv:2605.00180v1 | SRC-ARXIV@arXiv:2605.00180v1 | https://arxiv.org/html/2605.00180v1 — §3 graph profile construction and cold-start transfer | https://arxiv.org/html/2605.00180v1 — §4-5 new-model routing experiments, baselines and ablations | https://arxiv.org/html/2605.00180v1 — §6 Conclusion — exact-v1 has no dedicated limitations section; tested model/task graph and offline traces bound the conclusion | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2605-00180 | complete |
| SF-2026-ARXIV-2605-00206 | RP-9117d40ba6929c79 | deep | arXiv:2605.00206v1 | SRC-ARXIV@arXiv:2605.00206v1 | https://arxiv.org/html/2605.00206v1 — §2-4 nonlinear recurrence and parallel-training construction | https://arxiv.org/html/2605.00206v1 — §5 model/task evaluations and ablations | https://arxiv.org/html/2605.00206v1 — §6 limitations on scale, recurrence stability and broader workloads | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2605-00206 | complete |
| SF-2026-ARXIV-2605-00226 | RP-c679621d6ca55676 | deep | arXiv:2605.00226v1 | SRC-ARXIV@arXiv:2605.00226v1 | https://arxiv.org/html/2605.00226v1 — §3 strategic-play tasks, internal/verbal probes and Bayesian Coherence Coefficient | https://arxiv.org/html/2605.00226v1 — §4 repeated games, Kuhn Poker and Chameleon evaluations | Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: selected games/probes do not establish causal access to latent beliefs or general decision competence | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2605-00226 | complete |
| SF-2026-ARXIV-2605-00254 | RP-8f98fbe491ce3d22 | deep | arXiv:2605.00254v1 | SRC-ARXIV@arXiv:2605.00254v1 | https://arxiv.org/html/2605.00254v1 — §3-5 topology/cost model, placement and routing mechanisms | https://arxiv.org/html/2605.00254v1 — §6 serving scenarios and topology comparisons | https://arxiv.org/html/2605.00254v1 — §7 Conclusion — exact-v1 has no dedicated limitations section; scenario assumptions and cost model are not universal production measurements | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2605-00254 | complete |
| SF-2026-ARXIV-2605-00267 | RP-519dc6303a8b4fcf | deep | arXiv:2605.00267v1 | SRC-ARXIV@arXiv:2605.00267v1 | https://arxiv.org/html/2605.00267v1 — §3-4 jailbreak construction and capability-preservation protocol | https://arxiv.org/html/2605.00267v1 — §5 general and agentic task evaluations | https://arxiv.org/html/2605.00267v1 — §6 limitations: selected frontier models, attacks and tasks; no deployment prevalence claim | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2605-00267 | complete |
| SF-2026-ARXIV-2605-00300 | RP-fdcd665c797fb1a8 | deep | arXiv:2605.00300v1 | SRC-ARXIV@arXiv:2605.00300v1 | https://arxiv.org/html/2605.00300v1 — §3 endpoint-centric continuous benchmark and measurement protocol | https://arxiv.org/html/2605.00300v1 — §4-5 preference/cognition/energy evaluations | https://arxiv.org/html/2605.00300v1 — §6 discussion and limitations on provider drift, observability and evaluator scope | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2605-00300 | complete |
| SF-2026-ARXIV-2605-00314 | RP-65299a52b0456f54 | deep | arXiv:2605.00314v1 | SRC-ARXIV@arXiv:2605.00314v1 | https://arxiv.org/html/2605.00314v1 — §3-5 representation synthesis, Datalog constraints and audit pipeline | https://arxiv.org/html/2605.00314v1 — §6 evaluation over skill corpus, attack cases and hardware setup | https://arxiv.org/html/2605.00314v1 — §7 Conclusion — exact-v1 has no dedicated limitations section; static abstraction cannot prove dynamic runtime safety | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2605-00314 | complete |
| SF-AEM-AGENTIC-RL-ENTROPY-CREDIT | RP-92d74858f162bf8a | deep | arXiv:2605.00425v1 | SRC-ARXIV@arXiv:2605.00425v1 | arXiv:2605.00425v1 §§3–4 response-level entropy geometry and adaptive modulation; §Methodology: exact-v1 named method and system-design passages | arXiv:2605.00425v1 §5 ALFWorld, WebShop and SWE-bench-Verified across 1.5B–32B models; Experiments: exact-v1 evaluation and ablation passages | arXiv:2605.00425v1 §6 compute cost and Appendix D base-RL/implementation boundary; Scope and Limitations | Not Disclosed — arXiv:2605.00425v1 reports algorithm and prompts disclosed; immutable code revision not established | claim:SF-AEM-AGENTIC-RL-ENTROPY-CREDIT | complete |
| SF-AFFORDANCE-HARNESS-VERIFICATION-GATED-SKILLS | RP-ad7ef0d5d522bc57 | deep | arXiv:2605.00663v1 | SRC-ARXIV@arXiv:2605.00663v1 | arXiv:2605.00663v1 harness architecture, verifier gate and skill orchestration sections; §Methodology: exact-v1 named method and system-design passages | arXiv:2605.00663v1 affordance/skill execution experiments and failure analysis; Experiments: exact-v1 evaluation and ablation passages | arXiv:2605.00663v1 open-world perception, verifier and embodiment boundary; Scope and Limitations | Not Disclosed — arXiv:2605.00663v1 reports harness artifact described; immutable revision not established | claim:SF-AFFORDANCE-HARNESS-VERIFICATION-GATED-SKILLS | complete |
| SF-AGENT-CAPSULES-QUALITY-GATED-GRANULARITY | RP-b461542f5a52f345 | deep | arXiv:2605.00410v1 | SRC-ARXIV@arXiv:2605.00410v1 | arXiv:2605.00410v1 §§4–9 programming model, mode ladder and quality controller; §Methodology: exact-v1 named method and system-design passages | arXiv:2605.00410v1 §§10–12 four topologies and LangGraph/DSPy comparisons; Experiments: exact-v1 evaluation and ablation passages | arXiv:2605.00410v1 §13 limitations and §7.4 negative result; Scope and Limitations | arXiv:2605.00410v1 GitHub v1.0-arxiv tag linked by exact-v1 | claim:SF-AGENT-CAPSULES-QUALITY-GATED-GRANULARITY | complete |
| SF-AGOQ-ACTIVATION-GRADIENT-QUANTIZATION | RP-c879eda0f82f2997 | deep | arXiv:2605.00539v1 | SRC-ARXIV@arXiv:2605.00539v1 | arXiv:2605.00539v1 method sections: layer/stage activation policy and 8-bit gradient All-Reduce; §Methodology: exact-v1 named method and system-design passages | arXiv:2605.00539v1 experiments on 8B–32B LLaMA up to 64 GPUs; Experiments: exact-v1 evaluation and ablation passages | arXiv:2605.00539v1 ablation/discussion; architecture, precision and cluster boundary; Scope and Limitations | Not Disclosed — arXiv:2605.00539v1 reports implementation availability noted; event-time commit not pinned | claim:SF-AGOQ-ACTIVATION-GRADIENT-QUANTIZATION | complete |
| SF-AUTOMAT-CLAIM-REPRODUCTION-CONTRACT | RP-56ddc586e4e7b0bb | deep | arXiv:2605.00803v1 | SRC-ARXIV@arXiv:2605.00803v1 | arXiv:2605.00803v1 §§2–4 AutoMat task construction and execution harness; §Methodology: exact-v1 named method and system-design passages | arXiv:2605.00803v1 multi-agent/model reproduction results and error analysis; Experiments: exact-v1 evaluation and ablation passages | arXiv:2605.00803v1 limitations/ethics; materials-science and expert-curation boundary; Scope and Limitations | Not Disclosed — arXiv:2605.00803v1 reports benchmark artifact linked; immutable revision not established | claim:SF-AUTOMAT-CLAIM-REPRODUCTION-CONTRACT | complete |
| SF-BREW-WATERMARK-DESIGNATED-VERIFICATION | RP-a46b6433f621f2da | deep | arXiv:2605.00348v1 | SRC-ARXIV@arXiv:2605.00348v1 | arXiv:2605.00348v1 §§3–4 designated-codeword verification, block embedding and FPR/FNR bounds; §Methodology: exact-v1 named method and system-design passages | arXiv:2605.00348v1 §5 plus Appendix D attacks, ablations and detection metrics; Experiments: exact-v1 evaluation and ablation passages | arXiv:2605.00348v1 §3.3 adaptive-shift limitation and attack/model scope; Scope and Limitations | Not Disclosed — arXiv:2605.00348v1 reports implementation details disclosed; immutable repository revision not established | claim:SF-BREW-WATERMARK-DESIGNATED-VERIFICATION | complete |
| SF-CLEANBASE-RAG-DOCUMENT-GRAPH | RP-f5c6e22f9a382be6 | standard | arXiv:2605.00460v1 | SRC-ARXIV@arXiv:2605.00460v1 | arXiv:2605.00460v1 §§3–4 similarity graph, threshold and clique detector; §Methodology: exact-v1 named method and system-design passages | arXiv:2605.00460v1 §5 experiments and theoretical FP/FN bounds; Experiments: exact-v1 evaluation and ablation passages | arXiv:2605.00460v1 limitations/adaptive-attacker and embedding-distribution boundary; Scope and Limitations | Not Disclosed — arXiv:2605.00460v1 reports GitHub linked in v1; immutable commit not pinned | claim:SF-CLEANBASE-RAG-DOCUMENT-GRAPH | complete |
| SF-EVICT-MOE-VERIFICATION-UTILITY | RP-0ca52ab5bad49429 | deep | arXiv:2605.00342v1 | SRC-ARXIV@arXiv:2605.00342v1 | arXiv:2605.00342v1 §§2.2–3.3 cost model, accepted-length estimate, tree truncation and SGLang integration; §Methodology: exact-v1 named method and system-design passages | arXiv:2605.00342v1 §4 and Appendix B experiments/ablation; Experiments: exact-v1 evaluation and ablation passages | arXiv:2605.00342v1 §3.2.3 profiling boundary and §4 workload contract; no dedicated limitations heading; Scope and Limitations | Not Disclosed — arXiv:2605.00342v1 reports implementation described in SGLang; immutable commit not disclosed | claim:SF-EVICT-MOE-VERIFICATION-UTILITY | complete |
| SF-EVOLVING-MEMORY-TWO-STAGE-OPTIMIZATION | RP-9e68a3445a0a02db | deep | arXiv:2605.00702v1 | SRC-ARXIV@arXiv:2605.00702v1 | arXiv:2605.00702v1 two-stage optimization for memory extraction/update and use; §Methodology: exact-v1 named method and system-design passages | arXiv:2605.00702v1 long-horizon personalization evaluations and ablations; Experiments: exact-v1 evaluation and ablation passages | arXiv:2605.00702v1 preference-memory task, judge and model-family boundary; Scope and Limitations | Not Disclosed — arXiv:2605.00702v1 reports artifact revision not disclosed | claim:SF-EVOLVING-MEMORY-TWO-STAGE-OPTIMIZATION | complete |
| SF-FORWARD-REPLAY-MODEL-EDIT-TARGETS | RP-8d22a855019393c1 | deep | arXiv:2605.00358v1 | SRC-ARXIV@arXiv:2605.00358v1 | arXiv:2605.00358v1 §4.1 Theoretical grounding; §5 Our method; Appendix A.3–A.4; §Methodology: exact-v1 named method and system-design passages | arXiv:2605.00358v1 §6 Experiments; §6.2 Results; Appendix A.8; Experiments: exact-v1 evaluation and ablation passages | arXiv:2605.00358v1 §7 Conclusion and Limitations; first-order/Jacobian and LTE scope; Scope and Limitations | Not Disclosed — arXiv:2605.00358v1 reports §1 code link; immutable event-time commit not pinned | claim:SF-FORWARD-REPLAY-MODEL-EDIT-TARGETS | complete |
| SF-IEFF-CONTINUOUS-FEATURE-FADING | RP-39d6220bd7796dbf | deep | arXiv:2605.00324v1 | SRC-ARXIV@arXiv:2605.00324v1 | arXiv:2605.00324v1 §§2–4 IEFF architecture, fading controller and rollback; §Methodology: exact-v1 named method and system-design passages | arXiv:2605.00324v1 §5 offline/online CTR/CVR evaluation; Experiments: exact-v1 evaluation and ablation passages | arXiv:2605.00324v1 §6 and §7 limitations/future work; Scope and Limitations | Not Disclosed — arXiv:2605.00324v1 reports artifact revision not disclosed | claim:SF-IEFF-CONTINUOUS-FEATURE-FADING | complete |
| SF-LIGHTKV-PROMPT-GUIDED-VISION-KV | RP-ed4a620838598fdf | deep | arXiv:2605.00789v1 | SRC-ARXIV@arXiv:2605.00789v1 | arXiv:2605.00789v1 method sections: prompt-guided message passing and progressive vision-token compression; §Methodology: exact-v1 named method and system-design passages | arXiv:2605.00789v1 eight LVLMs/eight public benchmarks; Experiments: exact-v1 evaluation and ablation passages | arXiv:2605.00789v1 ablation/limitations; visual-task and selected-token boundary; Scope and Limitations | Not Disclosed — arXiv:2605.00789v1 reports artifact revision not disclosed | claim:SF-LIGHTKV-PROMPT-GUIDED-VISION-KV | complete |
| SF-LLM-EMU-NATIVE-RUNTIME-EMULATION | RP-1ad891f2342053e1 | deep | arXiv:2605.00616v1 | SRC-ARXIV@arXiv:2605.00616v1 | arXiv:2605.00616v1 §§2–4 vLLM-native emulation and profile sampler; §Methodology: exact-v1 named method and system-design passages | arXiv:2605.00616v1 §5 two GPU/four-model/arrival-process evaluation; Experiments: exact-v1 evaluation and ablation passages | arXiv:2605.00616v1 §6 limitations; TTFT and profile portability boundary; Scope and Limitations | Not Disclosed — arXiv:2605.00616v1 reports vLLM modification described; immutable commit not disclosed | claim:SF-LLM-EMU-NATIVE-RUNTIME-EMULATION | complete |
| SF-LWD-FLEET-OFFLINE-ONLINE-ROBOT-RL | RP-6fb5658ec6ea2dbd | deep | arXiv:2605.00416v1 | SRC-ARXIV@arXiv:2605.00416v1 | arXiv:2605.00416v1 method sections for DIVL/QAM and fleet data loop; §Methodology: exact-v1 named method and system-design passages | arXiv:2605.00416v1 real-robot evaluation: 16 robots, 8 tasks; Experiments: exact-v1 evaluation and ablation passages | arXiv:2605.00416v1 limitations/appendices; one fleet and flow-policy scope; Scope and Limitations | Not Disclosed — arXiv:2605.00416v1 reports project artifact linked; immutable event-time commit not established | claim:SF-LWD-FLEET-OFFLINE-ONLINE-ROBOT-RL | complete |
| SF-MATHARENA-LIVING-EVALUATION | RP-a0c0df23f8c0f3d1 | deep | arXiv:2605.00674v1 | SRC-ARXIV@arXiv:2605.00674v1 | arXiv:2605.00674v1 platform/task lifecycle and continuously refreshed evaluation design; §Methodology: exact-v1 named method and system-design passages | arXiv:2605.00674v1 competition/problem-set evaluations and model comparisons; Experiments: exact-v1 evaluation and ablation passages | arXiv:2605.00674v1 mathematics-only, organizer and contamination boundary; Scope and Limitations | Not Disclosed — arXiv:2605.00674v1 reports platform is public; event-time dataset revision not pinned | claim:SF-MATHARENA-LIVING-EVALUATION | complete |
| SF-MEMROUTER-WRITE-ADMISSION | RP-b47db74143381690 | deep | arXiv:2605.00356v1 | SRC-ARXIV@arXiv:2605.00356v1 | arXiv:2605.00356v1 §§3–4 write-side router and matched harness; §Methodology: exact-v1 named method and system-design passages | arXiv:2605.00356v1 §5 LoCoMo evaluation and factorial analysis; Experiments: exact-v1 evaluation and ablation passages | arXiv:2605.00356v1 limitations/discussion and matched-QA-backbone boundary; Scope and Limitations | Not Disclosed — arXiv:2605.00356v1 reports code/artifact revision not disclosed | claim:SF-MEMROUTER-WRITE-ADMISSION | complete |
| SF-PERSEUS-MEGAKERNEL-SIGNAL-ORDERING | RP-0dc70b385150ff7a | deep | arXiv:2605.00686v1 | SRC-ARXIV@arXiv:2605.00686v1 | arXiv:2605.00686v1 §§3–5 root cause, decoupled signaling, NIC ordering and implementation; §Methodology: exact-v1 named method and system-design passages | arXiv:2605.00686v1 §6 multi-platform/backend/model evaluation and ablation; Experiments: exact-v1 evaluation and ablation passages | arXiv:2605.00686v1 §8 discussion; transport, topology and compute/communication regime boundary; Scope and Limitations | Not Disclosed — arXiv:2605.00686v1 reports Triton-distributed case described; event-time patch not pinned | claim:SF-PERSEUS-MEGAKERNEL-SIGNAL-ORDERING | complete |
| SF-PROMPT-SCORE-VARIANCE-RELIABILITY | RP-eb0e42f8f47106cb | deep | arXiv:2605.00326v1 | SRC-ARXIV@arXiv:2605.00326v1 | arXiv:2605.00326v1 §§3–4 cross-prompt quantities and mean-ensemble method; §Methodology: exact-v1 named method and system-design passages | arXiv:2605.00326v1 §§5–6 locked 15-prompt protocol across 7 models and 2 datasets; Appendix C/F; Experiments: exact-v1 evaluation and ablation passages | arXiv:2605.00326v1 §7 discussion and explicit non-implications; ranking/calibration boundary; Scope and Limitations | Not Disclosed — arXiv:2605.00326v1 reports Appendix E.6 names code and analysis artifacts; immutable commit not established | claim:SF-PROMPT-SCORE-VARIANCE-RELIABILITY | complete |
| SF-RUNAGENT-CONSTRAINT-GUIDED-EXECUTION | RP-160007e201b336ac | deep | arXiv:2605.00798v1 | SRC-ARXIV@arXiv:2605.00798v1 | arXiv:2605.00798v1 system/method sections: agentic language, constraints, rubrics and correction; §Methodology: exact-v1 named method and system-design passages | arXiv:2605.00798v1 Natural-plan and SciBench evaluation; Experiments: exact-v1 evaluation and ablation passages | arXiv:2605.00798v1 limitations/discussion; plan quality and evaluator boundary; Scope and Limitations | Not Disclosed — arXiv:2605.00798v1 reports platform artifact revision not disclosed | claim:SF-RUNAGENT-CONSTRAINT-GUIDED-EXECUTION | complete |
| SF-SAGA-WORKFLOW-ATOMIC-SCHEDULING | RP-e42731e1fed8aed7 | deep | arXiv:2605.00528v1 | SRC-ARXIV@arXiv:2605.00528v1 | arXiv:2605.00528v1 §§3–8 AEG, cache, batching, AFS and implementation; §Methodology: exact-v1 named method and system-design passages | arXiv:2605.00528v1 §9 64-A100 evaluation and ablations; Experiments: exact-v1 evaluation and ablation passages | arXiv:2605.00528v1 §1.5 explicit limitations and §9.8 trade-offs; Scope and Limitations | Not Disclosed — arXiv:2605.00528v1 reports vLLM-based implementation; immutable event-time patch not disclosed | claim:SF-SAGA-WORKFLOW-ATOMIC-SCHEDULING | complete |
| SF-SIMFA-ASYNC-GPU-SIMULATION | RP-91041a28fef4034f | deep | arXiv:2605.00555v1 | SRC-ARXIV@arXiv:2605.00555v1 | arXiv:2605.00555v1 §§3–5 traffic model, event-driven TMA simulation and FA3 trace translation; §Methodology: exact-v1 named method and system-design passages | arXiv:2605.00555v1 §§5–6 H800 end-to-end and analytical-model validation; Experiments: exact-v1 evaluation and ablation passages | arXiv:2605.00555v1 §4.1 abstraction scope and §7 simulator/model comparison boundary; Scope and Limitations | Not Disclosed — arXiv:2605.00555v1 reports instrumented FA3/simulator described; immutable artifact revision not established | claim:SF-SIMFA-ASYNC-GPU-SIMULATION | complete |
| SF-SKILL-VERIFIABLE-ARTIFACT | RP-121370dbc45b1d38 | deep | arXiv:2605.00424v1 | SRC-ARXIV@arXiv:2605.00424v1 | arXiv:2605.00424v1 trust schema, biconditional criterion and runtime profile; §Methodology: exact-v1 named method and system-design passages | arXiv:2605.00424v1 adversarial-ensemble exercise/reference runtime; Experiments: exact-v1 evaluation and ablation passages | arXiv:2605.00424v1 threat model and verification-level boundary; Scope and Limitations | Not Disclosed — arXiv:2605.00424v1 reports reference implementation linked; immutable revision not established | claim:SF-SKILL-VERIFIABLE-ARTIFACT | complete |
| SF-TOOL-CALL-UTILITY-GATE | RP-7a6a5aedb42b288a | deep | arXiv:2605.00737v1 | SRC-ARXIV@arXiv:2605.00737v1 | arXiv:2605.00737v1 tool-call utility model, assessment protocol and optimization framework; §Methodology: exact-v1 named method and system-design passages | arXiv:2605.00737v1 multi-model/tool-use evaluations and cost-quality ablations; Experiments: exact-v1 evaluation and ablation passages | arXiv:2605.00737v1 toolset, task and evaluator boundary; Scope and Limitations | Not Disclosed — arXiv:2605.00737v1 reports framework artifact revision not disclosed | claim:SF-TOOL-CALL-UTILITY-GATE | complete |
| SF-UCPO-CORRECT-SOLUTION-DIVERSITY | RP-29b50af1113451fa | deep | arXiv:2605.00365v1 | SRC-ARXIV@arXiv:2605.00365v1 | arXiv:2605.00365v1 §§2–4 collapse analysis, optimality criteria and UCPO objective; §Methodology: exact-v1 named method and system-design passages | arXiv:2605.00365v1 §5 and appendices across 3 models/5 math benchmarks; Experiments: exact-v1 evaluation and ablation passages | arXiv:2605.00365v1 discussion/limitations; correct-set observability and math-only scope; Scope and Limitations | Not Disclosed — arXiv:2605.00365v1 reports paper-linked GitHub; event-time commit not pinned | claim:SF-UCPO-CORRECT-SOLUTION-DIVERSITY | complete |
| SF-VLM-VISUAL-JAILBREAK-CROSS-MODAL-GAP | RP-2c008ac7b9cd3ccc | deep | arXiv:2605.00583v1 | SRC-ARXIV@arXiv:2605.00583v1 | arXiv:2605.00583v1 §3 four visual attack constructions and shared protocol; §Methodology: exact-v1 named method and system-design passages | arXiv:2605.00583v1 §4 six frontier VLM evaluation with judge aggregation; Experiments: exact-v1 evaluation and ablation passages | arXiv:2605.00583v1 §5 discussion, limitations and mitigations; threat-model and judge boundary; Scope and Limitations | Not Disclosed — arXiv:2605.00583v1 reports paper-linked GitHub; immutable event-time commit not pinned | claim:SF-VLM-VISUAL-JAILBREAK-CROSS-MODAL-GAP | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2605-00066:start -->
<!-- claim:SF-2026-ARXIV-2605-00066:start -->
Open-loop perception/planning metrics 不能自动代理 closed-loop outcome；跨 benchmark 相关性必须先对齐 policy、environment、horizon、intervention 与 failure definition。
<!-- claim:SF-2026-ARXIV-2605-00066:end -->
#### Do Open-Loop Metrics Predict Closed-Loop Driving? A Cross-Benchmark Correlation Study of NAVSIM and Bench2Drive

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§3 cross-benchmark metric mapping and correlation protocol`。
- **Mechanism / ownership:** Open-loop perception/planning metrics 不能自动代理 closed-loop outcome；跨 benchmark 相关性必须先对齐 policy、environment、horizon、intervention 与 failure definition。
- **Evaluation contract:** `§4 NAVSIM and Bench2Drive cross-benchmark results and sensitivity`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `§5 selected benchmarks/models and correlation do not establish causality or real-world safety`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Principle Reuse` → `PLATFORM-EVALUATION-SYSTEM`；Score V2 `3/3/3` = **9/9**。
- **Books decision:** `No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-00066:end -->

<!-- review:SF-2026-ARXIV-2605-00081:start -->
<!-- claim:SF-2026-ARXIV-2605-00081:start -->
Agent security 不能只判断 intent 或输出文本；可执行 effect 必须在独立 mediation boundary 由 typed contract、authorization 和 audit 拦截，且模型层与执行层各自保留可观测责任。
<!-- claim:SF-2026-ARXIV-2605-00081:end -->
#### Alignment Contracts for Agentic Security Systems

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§2-6 threat assumptions, contract language, dual-layer observability and enforcement`。
- **Mechanism / ownership:** Agent security 不能只判断 intent 或输出文本；可执行 effect 必须在独立 mediation boundary 由 typed contract、authorization 和 audit 拦截，且模型层与执行层各自保留可观测责任。
- **Evaluation contract:** `§7 examples and policy-composition analysis`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `§8 impossibility/scope boundary; disclosed framework is not proof of all semantic safety`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Direct Evolution` → `PLATFORM-SECURITY`；Score V2 `3/3/3` = **9/9**。
- **Books decision:** `No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-00081:end -->

<!-- review:SF-2026-ARXIV-2605-00136:start -->
<!-- claim:SF-2026-ARXIV-2605-00136:start -->
Tool-use accuracy 必须拆开协议格式成本、selection/argument error、transport/runtime failure 与真实工具收益；更多工具或更长 schema 会征收 context 和 routing tax，不能把失败都归因于模型不会调用。
<!-- claim:SF-2026-ARXIV-2605-00136:end -->
#### Are Tools All We Need? Unveiling the Tool-Use Tax in LLM Agents

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§3-4 decomposition of tool protocol, selection and execution costs`。
- **Mechanism / ownership:** Tool-use accuracy 必须拆开协议格式成本、selection/argument error、transport/runtime failure 与真实工具收益；更多工具或更长 schema 会征收 context 和 routing tax，不能把失败都归因于模型不会调用。
- **Evaluation contract:** `§5 controlled tool-use diagnosis across models/tasks`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `§6/discussion task and framework scope; no universal tax constant`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Explanatory Analogy` → `AGENT-TOOL-CALLING`；Score V2 `2/3/3` = **8/9**。
- **Books decision:** `No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-00136:end -->

<!-- review:SF-2026-ARXIV-2605-00155:start -->
<!-- claim:SF-2026-ARXIV-2605-00155:start -->
Preference optimization can treat annotator/reward uncertainty as a distributional ambiguity set and optimize worst-case regret, but robustness radius and reference policy become new control assumptions rather than removing reward misspecification.
<!-- claim:SF-2026-ARXIV-2605-00155:end -->
#### Wasserstein Distributionally Robust Regret Optimization for Reinforcement Learning from Human Feedback

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§3-5 Wasserstein ambiguity set and robust regret objective`。
- **Mechanism / ownership:** Preference optimization can treat annotator/reward uncertainty as a distributional ambiguity set and optimize worst-case regret, but robustness radius and reference policy become new control assumptions rather than removing reward misspecification.
- **Evaluation contract:** `§6 experiments and ablations on specified preference datasets/models`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `Not Disclosed — exact-v1 has no dedicated limitations section; author experiments do not establish universal robustness radius`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Principle Reuse` → `TRAIN-RLHF`；Score V2 `2/2/2` = **6/9**。
- **Books decision:** `No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-00155:end -->

<!-- review:SF-2026-ARXIV-2605-00161:start -->
<!-- claim:SF-2026-ARXIV-2605-00161:start -->
Consistent diffusion language modeling narrows train/inference inconsistency by coupling conditional denoising states; it trades token-sequential commitment for iterative correction and does not erase sampling-step, cache or rollback costs.
<!-- claim:SF-2026-ARXIV-2605-00161:end -->
#### Consistent Diffusion Language Models

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§2-3 consistency objective and diffusion language-model mechanism`。
- **Mechanism / ownership:** Consistent diffusion language modeling narrows train/inference inconsistency by coupling conditional denoising states; it trades token-sequential commitment for iterative correction and does not erase sampling-step, cache or rollback costs.
- **Evaluation contract:** `§4-5 language-model evaluations and ablations`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `§6 Conclusion — exact-v1 has no dedicated limitations section; workloads do not prove replacement of autoregressive generation`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Alternative Branch` → `MULTIMODAL-GENERATIVE-PARADIGMS`；Score V2 `2/2/3` = **7/9**。
- **Books decision:** `No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-00161:end -->

<!-- review:SF-2026-ARXIV-2605-00180:start -->
<!-- claim:SF-2026-ARXIV-2605-00180:start -->
Model routing 的 cold start 不是缺少一个静态 leaderboard，而是缺少 workload-conditioned profile；图结构从已知模型迁移观测可降低探索成本，但 profile staleness、uncertainty 和 online fallback 必须进入 admission/routing contract。
<!-- claim:SF-2026-ARXIV-2605-00180:end -->
#### RouteProfile: Graph-Based Profiling for Cold-Start LLM Routing

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§3 graph profile construction and cold-start transfer`。
- **Mechanism / ownership:** Model routing 的 cold start 不是缺少一个静态 leaderboard，而是缺少 workload-conditioned profile；图结构从已知模型迁移观测可降低探索成本，但 profile staleness、uncertainty 和 online fallback 必须进入 admission/routing contract。
- **Evaluation contract:** `§4-5 new-model routing experiments, baselines and ablations`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `§6 Conclusion — exact-v1 has no dedicated limitations section; tested model/task graph and offline traces bound the conclusion`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Direct Evolution` → `INFER-SCHEDULING`；Score V2 `3/3/3` = **9/9**。
- **Books decision:** `No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-00180:end -->

<!-- review:SF-2026-ARXIV-2605-00206:start -->
<!-- claim:SF-2026-ARXIV-2605-00206:start -->
Nonlinear recurrent latent state can be trained with a parallel surrogate and executed recurrently, shifting the bottleneck from explicit token history toward state-transition stability and train/decode equivalence.
<!-- claim:SF-2026-ARXIV-2605-00206:end -->
#### State Stream Transformer (SST) V2: Parallel Training of Nonlinear Recurrence for Latent Space Reasoning

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§2-4 nonlinear recurrence and parallel-training construction`。
- **Mechanism / ownership:** Nonlinear recurrent latent state can be trained with a parallel surrogate and executed recurrently, shifting the bottleneck from explicit token history toward state-transition stability and train/decode equivalence.
- **Evaluation contract:** `§5 model/task evaluations and ablations`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `§6 limitations on scale, recurrence stability and broader workloads`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Alternative Branch` → `MODEL-DECODER-ONLY`；Score V2 `2/2/3` = **7/9**。
- **Books decision:** `No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-00206:end -->

<!-- review:SF-2026-ARXIV-2605-00226:start -->
<!-- claim:SF-2026-ARXIV-2605-00226:start -->
Strategic failure can be decomposed into observation→belief update and belief→action selection gaps; verbalized belief and action accuracy should not be treated as one undifferentiated planning score.
<!-- claim:SF-2026-ARXIV-2605-00226:end -->
#### Why Do LLMs Struggle in Strategic Play? Broken Links Between Observations, Beliefs, and Actions

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§3 strategic-play tasks, internal/verbal probes and Bayesian Coherence Coefficient`。
- **Mechanism / ownership:** Strategic failure can be decomposed into observation→belief update and belief→action selection gaps; verbalized belief and action accuracy should not be treated as one undifferentiated planning score.
- **Evaluation contract:** `§4 repeated games, Kuhn Poker and Chameleon evaluations`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: selected games/probes do not establish causal access to latent beliefs or general decision competence`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Explanatory Analogy` → `AGENT-PLANNING`；Score V2 `3/2/3` = **8/9**。
- **Books decision:** `No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-00226:end -->

<!-- review:SF-2026-ARXIV-2605-00254:start -->
<!-- claim:SF-2026-ARXIV-2605-00254:start -->
MoE serving topology 必须把 expert placement、token skew、all-to-all bytes、network tiers 与 replica cost 联合建模；更便宜的 topology 会把平均带宽收益换成 hotspot、reconfiguration 和 failure-domain 压力。
<!-- claim:SF-2026-ARXIV-2605-00254:end -->
#### Rethinking Network Topologies for Cost-Effective Mixture-of-Experts LLM Serving

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§3-5 topology/cost model, placement and routing mechanisms`。
- **Mechanism / ownership:** MoE serving topology 必须把 expert placement、token skew、all-to-all bytes、network tiers 与 replica cost 联合建模；更便宜的 topology 会把平均带宽收益换成 hotspot、reconfiguration 和 failure-domain 压力。
- **Evaluation contract:** `§6 serving scenarios and topology comparisons`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `§7 Conclusion — exact-v1 has no dedicated limitations section; scenario assumptions and cost model are not universal production measurements`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Direct Evolution` → `INFER-SCHEDULING`；Score V2 `3/3/3` = **9/9**。
- **Books decision:** `Integrate`。
<!-- review:SF-2026-ARXIV-2605-00254:end -->

<!-- review:SF-2026-ARXIV-2605-00267:start -->
<!-- claim:SF-2026-ARXIV-2605-00267:start -->
Jailbreak 后保留通用能力意味着 safety case 不能依赖能力退化；风险控制必须落在 action authority、sandbox、monitoring 与 outcome evidence，而不是假设越狱模型不可完成复杂任务。
<!-- claim:SF-2026-ARXIV-2605-00267:end -->
#### Jailbroken Frontier Models Retain Their Capabilities

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§3-4 jailbreak construction and capability-preservation protocol`。
- **Mechanism / ownership:** Jailbreak 后保留通用能力意味着 safety case 不能依赖能力退化；风险控制必须落在 action authority、sandbox、monitoring 与 outcome evidence，而不是假设越狱模型不可完成复杂任务。
- **Evaluation contract:** `§5 general and agentic task evaluations`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `§6 limitations: selected frontier models, attacks and tasks; no deployment prevalence claim`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Explanatory Analogy` → `PLATFORM-SECURITY`；Score V2 `3/3/3` = **9/9**。
- **Books decision:** `No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-00267:end -->

<!-- review:SF-2026-ARXIV-2605-00300:start -->
<!-- claim:SF-2026-ARXIV-2605-00300:start -->
Inference benchmark 的原子对象可以是 endpoint/model configuration，而不是模型名称；能耗、质量、延迟与请求策略必须在连续、版本化 contract 中共同记录，且偏好结论不能脱离 evaluator 与 workload。
<!-- claim:SF-2026-ARXIV-2605-00300:end -->
#### Token Arena: A Continuous Benchmark Unifying Energy and Cognition in AI Inference

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§3 endpoint-centric continuous benchmark and measurement protocol`。
- **Mechanism / ownership:** Inference benchmark 的原子对象可以是 endpoint/model configuration，而不是模型名称；能耗、质量、延迟与请求策略必须在连续、版本化 contract 中共同记录，且偏好结论不能脱离 evaluator 与 workload。
- **Evaluation contract:** `§4-5 preference/cognition/energy evaluations`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `§6 discussion and limitations on provider drift, observability and evaluator scope`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Direct Evolution` → `PLATFORM-EVALUATION-SYSTEM`；Score V2 `3/3/3` = **9/9**。
- **Books decision:** `Integrate`。
<!-- review:SF-2026-ARXIV-2605-00300:end -->

<!-- review:SF-2026-ARXIV-2605-00314:start -->
<!-- claim:SF-2026-ARXIV-2605-00314:start -->
Agent skill 审计需要把自然语言/代码能力合成为可查询的约束表示，再在调用前检查 source→sink、permission 与 effect；静态分析提高可解释性，却受表示不完备、动态行为与环境依赖限制。
<!-- claim:SF-2026-ARXIV-2605-00314:end -->
#### Semia: Auditing Agent Skills via Constraint-Guided Representation Synthesis

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§3-5 representation synthesis, Datalog constraints and audit pipeline`。
- **Mechanism / ownership:** Agent skill 审计需要把自然语言/代码能力合成为可查询的约束表示，再在调用前检查 source→sink、permission 与 effect；静态分析提高可解释性，却受表示不完备、动态行为与环境依赖限制。
- **Evaluation contract:** `§6 evaluation over skill corpus, attack cases and hardware setup`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `§7 Conclusion — exact-v1 has no dedicated limitations section; static abstraction cannot prove dynamic runtime safety`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Layering / Dependency` → `PLATFORM-SECURITY`；Score V2 `3/3/3` = **9/9**。
- **Books decision:** `Integrate`。
<!-- review:SF-2026-ARXIV-2605-00314:end -->

<!-- review:SF-AEM-AGENTIC-RL-ENTROPY-CREDIT:start -->
### AEM: Adaptive Entropy Modulation for Multi-Turn Agentic Reinforcement Learning

问题与旧路径：Multi-turn agentic RL can use response-level entropy dynamics as an intrinsic credit and exploration-control signal without a separate process reward model. 旧方案在任务短、状态可丢弃、拓扑稳定或风险较低时仍合理。约束变化后，exact-v1 将机制定位在 §§3–4 response-level entropy geometry and adaptive modulation；状态/控制权因此从隐式约定转为可测量、可版本化的系统对象。

Evaluation contract：§5 ALFWorld, WebShop and SWE-bench-Verified across 1.5B–32B models。作者结果只证明上述模型、硬件、数据、精度与实现条件中披露的范围；未披露字段不推断。反证与边界：§6 compute cost and Appendix D base-RL/implementation boundary。Artifact：algorithm and prompts disclosed; immutable code revision not established。<!-- claim:SF-AEM-AGENTIC-RL-ENTROPY-CREDIT:start -->长期可保留结论是：Multi-turn agentic RL can use response-level entropy dynamics as an intrinsic credit and exploration-control signal without a separate process reward model. 它不证明该实现跨 workload 普遍最优，也不授权跳过独立 evaluation、fallback 与 rollback。<!-- claim:SF-AEM-AGENTIC-RL-ENTROPY-CREDIT:end -->
<!-- review:SF-AEM-AGENTIC-RL-ENTROPY-CREDIT:end -->

<!-- review:SF-AFFORDANCE-HARNESS-VERIFICATION-GATED-SKILLS:start -->
### Affordance Agent Harness: Verification-Gated Skill Orchestration

问题与旧路径：Skill orchestration needs verifier-owned admission and failure recovery; perceptual affordance confidence cannot directly authorize action. 旧方案在任务短、状态可丢弃、拓扑稳定或风险较低时仍合理。约束变化后，exact-v1 将机制定位在 harness architecture, verifier gate and skill orchestration sections；状态/控制权因此从隐式约定转为可测量、可版本化的系统对象。

Evaluation contract：affordance/skill execution experiments and failure analysis。作者结果只证明上述模型、硬件、数据、精度与实现条件中披露的范围；未披露字段不推断。反证与边界：open-world perception, verifier and embodiment boundary。Artifact：harness artifact described; immutable revision not established。<!-- claim:SF-AFFORDANCE-HARNESS-VERIFICATION-GATED-SKILLS:start -->长期可保留结论是：Skill orchestration needs verifier-owned admission and failure recovery; perceptual affordance confidence cannot directly authorize action. 它不证明该实现跨 workload 普遍最优，也不授权跳过独立 evaluation、fallback 与 rollback。<!-- claim:SF-AFFORDANCE-HARNESS-VERIFICATION-GATED-SKILLS:end -->
<!-- review:SF-AFFORDANCE-HARNESS-VERIFICATION-GATED-SKILLS:end -->

<!-- review:SF-AGENT-CAPSULES-QUALITY-GATED-GRANULARITY:start -->
### Agent Capsules: Quality-Gated Granularity Control for Multi-Agent LLM Pipelines

问题与旧路径：Agent dispatch granularity is a runtime decision gated by measured workload quality, not a static pipeline property. 旧方案在任务短、状态可丢弃、拓扑稳定或风险较低时仍合理。约束变化后，exact-v1 将机制定位在 §§4–9 programming model, mode ladder and quality controller；状态/控制权因此从隐式约定转为可测量、可版本化的系统对象。

Evaluation contract：§§10–12 four topologies and LangGraph/DSPy comparisons。作者结果只证明上述模型、硬件、数据、精度与实现条件中披露的范围；未披露字段不推断。反证与边界：§13 limitations and §7.4 negative result。Artifact：GitHub v1.0-arxiv tag linked by exact-v1。<!-- claim:SF-AGENT-CAPSULES-QUALITY-GATED-GRANULARITY:start -->长期可保留结论是：Agent dispatch granularity is a runtime decision gated by measured workload quality, not a static pipeline property. 它不证明该实现跨 workload 普遍最优，也不授权跳过独立 evaluation、fallback 与 rollback。<!-- claim:SF-AGENT-CAPSULES-QUALITY-GATED-GRANULARITY:end -->
<!-- review:SF-AGENT-CAPSULES-QUALITY-GATED-GRANULARITY:end -->

<!-- review:SF-AGOQ-ACTIVATION-GRADIENT-QUANTIZATION:start -->
### AGoQ: Activation and Gradient Quantization for Memory-Efficient Distributed Training of LLMs

问题与旧路径：Activation bit width and gradient communication precision become layer/stage-aware training-runtime policies. 旧方案在任务短、状态可丢弃、拓扑稳定或风险较低时仍合理。约束变化后，exact-v1 将机制定位在 method sections: layer/stage activation policy and 8-bit gradient All-Reduce；状态/控制权因此从隐式约定转为可测量、可版本化的系统对象。

Evaluation contract：experiments on 8B–32B LLaMA up to 64 GPUs。作者结果只证明上述模型、硬件、数据、精度与实现条件中披露的范围；未披露字段不推断。反证与边界：ablation/discussion; architecture, precision and cluster boundary。Artifact：implementation availability noted; event-time commit not pinned。<!-- claim:SF-AGOQ-ACTIVATION-GRADIENT-QUANTIZATION:start -->长期可保留结论是：Activation bit width and gradient communication precision become layer/stage-aware training-runtime policies. 它不证明该实现跨 workload 普遍最优，也不授权跳过独立 evaluation、fallback 与 rollback。<!-- claim:SF-AGOQ-ACTIVATION-GRADIENT-QUANTIZATION:end -->
<!-- review:SF-AGOQ-ACTIVATION-GRADIENT-QUANTIZATION:end -->

<!-- review:SF-AUTOMAT-CLAIM-REPRODUCTION-CONTRACT:start -->
### Can Coding Agents Reproduce Findings in Computational Materials Science?

问题与旧路径：Coding-agent evaluation must include procedure recovery, toolchain execution and claim-evidence adjudication, not code-generation success alone. 旧方案在任务短、状态可丢弃、拓扑稳定或风险较低时仍合理。约束变化后，exact-v1 将机制定位在 §§2–4 AutoMat task construction and execution harness；状态/控制权因此从隐式约定转为可测量、可版本化的系统对象。

Evaluation contract：multi-agent/model reproduction results and error analysis。作者结果只证明上述模型、硬件、数据、精度与实现条件中披露的范围；未披露字段不推断。反证与边界：limitations/ethics; materials-science and expert-curation boundary。Artifact：benchmark artifact linked; immutable revision not established。<!-- claim:SF-AUTOMAT-CLAIM-REPRODUCTION-CONTRACT:start -->长期可保留结论是：Coding-agent evaluation must include procedure recovery, toolchain execution and claim-evidence adjudication, not code-generation success alone. 它不证明该实现跨 workload 普遍最优，也不授权跳过独立 evaluation、fallback 与 rollback。<!-- claim:SF-AUTOMAT-CLAIM-REPRODUCTION-CONTRACT:end -->
<!-- review:SF-AUTOMAT-CLAIM-REPRODUCTION-CONTRACT:end -->

<!-- review:SF-BREW-WATERMARK-DESIGNATED-VERIFICATION:start -->
### Block-wise Codeword Embedding for Reliable Multi-bit Text Watermarking

问题与旧路径：Multi-bit watermark extraction and provenance detection are different contracts; designated-codeword verification makes false-positive control explicit. 旧方案在任务短、状态可丢弃、拓扑稳定或风险较低时仍合理。约束变化后，exact-v1 将机制定位在 §§3–4 designated-codeword verification, block embedding and FPR/FNR bounds；状态/控制权因此从隐式约定转为可测量、可版本化的系统对象。

Evaluation contract：§5 plus Appendix D attacks, ablations and detection metrics。作者结果只证明上述模型、硬件、数据、精度与实现条件中披露的范围；未披露字段不推断。反证与边界：§3.3 adaptive-shift limitation and attack/model scope。Artifact：implementation details disclosed; immutable repository revision not established。<!-- claim:SF-BREW-WATERMARK-DESIGNATED-VERIFICATION:start -->长期可保留结论是：Multi-bit watermark extraction and provenance detection are different contracts; designated-codeword verification makes false-positive control explicit. 它不证明该实现跨 workload 普遍最优，也不授权跳过独立 evaluation、fallback 与 rollback。<!-- claim:SF-BREW-WATERMARK-DESIGNATED-VERIFICATION:end -->
<!-- review:SF-BREW-WATERMARK-DESIGNATED-VERIFICATION:end -->

<!-- review:SF-CLEANBASE-RAG-DOCUMENT-GRAPH:start -->
### CleanBase: Detecting Malicious Documents in RAG Knowledge Databases

问题与旧路径：RAG ingestion needs document-level security evidence; similarity-clique detection is one bounded sensor rather than a trust proof. 旧方案在任务短、状态可丢弃、拓扑稳定或风险较低时仍合理。约束变化后，exact-v1 将机制定位在 §§3–4 similarity graph, threshold and clique detector；状态/控制权因此从隐式约定转为可测量、可版本化的系统对象。

Evaluation contract：§5 experiments and theoretical FP/FN bounds。作者结果只证明上述模型、硬件、数据、精度与实现条件中披露的范围；未披露字段不推断。反证与边界：limitations/adaptive-attacker and embedding-distribution boundary。Artifact：GitHub linked in v1; immutable commit not pinned。<!-- claim:SF-CLEANBASE-RAG-DOCUMENT-GRAPH:start -->长期可保留结论是：RAG ingestion needs document-level security evidence; similarity-clique detection is one bounded sensor rather than a trust proof. 它不证明该实现跨 workload 普遍最优，也不授权跳过独立 evaluation、fallback 与 rollback。<!-- claim:SF-CLEANBASE-RAG-DOCUMENT-GRAPH:end -->
<!-- review:SF-CLEANBASE-RAG-DOCUMENT-GRAPH:end -->

<!-- review:SF-EVICT-MOE-VERIFICATION-UTILITY:start -->
### Making Every Verified Token Count: Adaptive Verification for MoE Speculative Decoding

问题与旧路径：MoE speculative verification is scheduled by accepted-token utility against the union-of-experts verification cost. 旧方案在任务短、状态可丢弃、拓扑稳定或风险较低时仍合理。约束变化后，exact-v1 将机制定位在 §§2.2–3.3 cost model, accepted-length estimate, tree truncation and SGLang integration；状态/控制权因此从隐式约定转为可测量、可版本化的系统对象。

Evaluation contract：§4 and Appendix B experiments/ablation。作者结果只证明上述模型、硬件、数据、精度与实现条件中披露的范围；未披露字段不推断。反证与边界：§3.2.3 profiling boundary and §4 workload contract; no dedicated limitations heading。Artifact：implementation described in SGLang; immutable commit not disclosed。<!-- claim:SF-EVICT-MOE-VERIFICATION-UTILITY:start -->长期可保留结论是：MoE speculative verification is scheduled by accepted-token utility against the union-of-experts verification cost. 它不证明该实现跨 workload 普遍最优，也不授权跳过独立 evaluation、fallback 与 rollback。<!-- claim:SF-EVICT-MOE-VERIFICATION-UTILITY:end -->
<!-- review:SF-EVICT-MOE-VERIFICATION-UTILITY:end -->

<!-- review:SF-EVOLVING-MEMORY-TWO-STAGE-OPTIMIZATION:start -->
### Learning How and What to Memorize: Cognition-Inspired Two-Stage Optimization for Evolving Memory

问题与旧路径：Long-term memory needs separately optimized write/update behavior and answer-time use; static hand-written memory update rules are not a durable policy. 旧方案在任务短、状态可丢弃、拓扑稳定或风险较低时仍合理。约束变化后，exact-v1 将机制定位在 two-stage optimization for memory extraction/update and use；状态/控制权因此从隐式约定转为可测量、可版本化的系统对象。

Evaluation contract：long-horizon personalization evaluations and ablations。作者结果只证明上述模型、硬件、数据、精度与实现条件中披露的范围；未披露字段不推断。反证与边界：preference-memory task, judge and model-family boundary。Artifact：artifact revision not disclosed。<!-- claim:SF-EVOLVING-MEMORY-TWO-STAGE-OPTIMIZATION:start -->长期可保留结论是：Long-term memory needs separately optimized write/update behavior and answer-time use; static hand-written memory update rules are not a durable policy. 它不证明该实现跨 workload 普遍最优，也不授权跳过独立 evaluation、fallback 与 rollback。<!-- claim:SF-EVOLVING-MEMORY-TWO-STAGE-OPTIMIZATION:end -->
<!-- review:SF-EVOLVING-MEMORY-TWO-STAGE-OPTIMIZATION:end -->

<!-- review:SF-FORWARD-REPLAY-MODEL-EDIT-TARGETS:start -->
### From Backward Spreading to Forward Replay: Revisiting Target Construction in LLM Parameter Editing

问题与旧路径：exact-v1 §§4–5 证明 backward spreading 把 final-layer residual 线性分配到早层时隐含 Jacobian eigenvector/正定条件；forward replay 改由首个编辑层的 anchor 沿真实 downstream dynamics 生成兼容 target。该机制把 parameter edit 从局部优化技巧提升为跨层 state-transition 与 compatibility contract；现有知识树没有稳定的 model-edit lifecycle owner，进入 Structural Candidate。 旧方案在任务短、状态可丢弃、拓扑稳定或风险较低时仍合理。约束变化后，exact-v1 将机制定位在 §4.1 Theoretical grounding; §5 Our method; Appendix A.3–A.4；状态/控制权因此从隐式约定转为可测量、可版本化的系统对象。

Evaluation contract：§6 Experiments; §6.2 Results; Appendix A.8。作者结果只证明上述模型、硬件、数据、精度与实现条件中披露的范围；未披露字段不推断。反证与边界：§7 Conclusion and Limitations; first-order/Jacobian and LTE scope。Artifact：§1 code link; immutable event-time commit not pinned。<!-- claim:SF-FORWARD-REPLAY-MODEL-EDIT-TARGETS:start -->长期可保留结论是：Supports cross-layer target compatibility for locate-then-edit methods under the evaluated model/edit regimes; does not establish safe sequential editing, provenance, rollback, or production knowledge-lifecycle correctness. 它不证明该实现跨 workload 普遍最优，也不授权跳过独立 evaluation、fallback 与 rollback。<!-- claim:SF-FORWARD-REPLAY-MODEL-EDIT-TARGETS:end -->
<!-- review:SF-FORWARD-REPLAY-MODEL-EDIT-TARGETS:end -->

<!-- review:SF-IEFF-CONTINUOUS-FEATURE-FADING:start -->
### Intelligent Elastic Feature Fading: Enabling Model Retrain-Free Feature Efficiency Rollouts at Scale

问题与旧路径：Serving-time reversible feature fading lets recurring training absorb a bounded distribution shift without a rollout-specific retrain. 旧方案在任务短、状态可丢弃、拓扑稳定或风险较低时仍合理。约束变化后，exact-v1 将机制定位在 §§2–4 IEFF architecture, fading controller and rollback；状态/控制权因此从隐式约定转为可测量、可版本化的系统对象。

Evaluation contract：§5 offline/online CTR/CVR evaluation。作者结果只证明上述模型、硬件、数据、精度与实现条件中披露的范围；未披露字段不推断。反证与边界：§6 and §7 limitations/future work。Artifact：artifact revision not disclosed。<!-- claim:SF-IEFF-CONTINUOUS-FEATURE-FADING:start -->长期可保留结论是：Serving-time reversible feature fading lets recurring training absorb a bounded distribution shift without a rollout-specific retrain. 它不证明该实现跨 workload 普遍最优，也不授权跳过独立 evaluation、fallback 与 rollback。<!-- claim:SF-IEFF-CONTINUOUS-FEATURE-FADING:end -->
<!-- review:SF-IEFF-CONTINUOUS-FEATURE-FADING:end -->

<!-- review:SF-LIGHTKV-PROMPT-GUIDED-VISION-KV:start -->
### Make Your LVLM KV Cache More Lightweight

问题与旧路径：Vision-token KV compression is prompt-conditioned and must preserve modality/token/position identity; the mechanism is a bounded implementation case. 旧方案在任务短、状态可丢弃、拓扑稳定或风险较低时仍合理。约束变化后，exact-v1 将机制定位在 method sections: prompt-guided message passing and progressive vision-token compression；状态/控制权因此从隐式约定转为可测量、可版本化的系统对象。

Evaluation contract：eight LVLMs/eight public benchmarks。作者结果只证明上述模型、硬件、数据、精度与实现条件中披露的范围；未披露字段不推断。反证与边界：ablation/limitations; visual-task and selected-token boundary。Artifact：artifact revision not disclosed。<!-- claim:SF-LIGHTKV-PROMPT-GUIDED-VISION-KV:start -->长期可保留结论是：Vision-token KV compression is prompt-conditioned and must preserve modality/token/position identity; the mechanism is a bounded implementation case. 它不证明该实现跨 workload 普遍最优，也不授权跳过独立 evaluation、fallback 与 rollback。<!-- claim:SF-LIGHTKV-PROMPT-GUIDED-VISION-KV:end -->
<!-- review:SF-LIGHTKV-PROMPT-GUIDED-VISION-KV:end -->

<!-- review:SF-LLM-EMU-NATIVE-RUNTIME-EMULATION:start -->
### LLM-Emu: Native Runtime Emulation of LLM Inference via Profile-Driven Sampling

问题与旧路径：A serving emulator preserves the real HTTP, scheduler, KV and output paths while replacing only GPU execution with profiled samples. 旧方案在任务短、状态可丢弃、拓扑稳定或风险较低时仍合理。约束变化后，exact-v1 将机制定位在 §§2–4 vLLM-native emulation and profile sampler；状态/控制权因此从隐式约定转为可测量、可版本化的系统对象。

Evaluation contract：§5 two GPU/four-model/arrival-process evaluation。作者结果只证明上述模型、硬件、数据、精度与实现条件中披露的范围；未披露字段不推断。反证与边界：§6 limitations; TTFT and profile portability boundary。Artifact：vLLM modification described; immutable commit not disclosed。<!-- claim:SF-LLM-EMU-NATIVE-RUNTIME-EMULATION:start -->长期可保留结论是：A serving emulator preserves the real HTTP, scheduler, KV and output paths while replacing only GPU execution with profiled samples. 它不证明该实现跨 workload 普遍最优，也不授权跳过独立 evaluation、fallback 与 rollback。<!-- claim:SF-LLM-EMU-NATIVE-RUNTIME-EMULATION:end -->
<!-- review:SF-LLM-EMU-NATIVE-RUNTIME-EMULATION:end -->

<!-- review:SF-LWD-FLEET-OFFLINE-ONLINE-ROBOT-RL:start -->
### Learning While Deploying: Fleet-Scale Reinforcement Learning for Generalist Robot Policies

问题与旧路径：Deployment, intervention capture, offline-to-online value learning and redeployment form a versioned embodied-learning loop. 旧方案在任务短、状态可丢弃、拓扑稳定或风险较低时仍合理。约束变化后，exact-v1 将机制定位在 method sections for DIVL/QAM and fleet data loop；状态/控制权因此从隐式约定转为可测量、可版本化的系统对象。

Evaluation contract：real-robot evaluation: 16 robots, 8 tasks。作者结果只证明上述模型、硬件、数据、精度与实现条件中披露的范围；未披露字段不推断。反证与边界：limitations/appendices; one fleet and flow-policy scope。Artifact：project artifact linked; immutable event-time commit not established。<!-- claim:SF-LWD-FLEET-OFFLINE-ONLINE-ROBOT-RL:start -->长期可保留结论是：Deployment, intervention capture, offline-to-online value learning and redeployment form a versioned embodied-learning loop. 它不证明该实现跨 workload 普遍最优，也不授权跳过独立 evaluation、fallback 与 rollback。<!-- claim:SF-LWD-FLEET-OFFLINE-ONLINE-ROBOT-RL:end -->
<!-- review:SF-LWD-FLEET-OFFLINE-ONLINE-ROBOT-RL:end -->

<!-- review:SF-MATHARENA-LIVING-EVALUATION:start -->
### Beyond Benchmarks: MathArena as an Evaluation Platform for Mathematics with LLMs

问题与旧路径：Evaluation for fast-moving capabilities needs continuously refreshed, contamination-resistant tasks with versioned scoring rather than a static benchmark snapshot. 旧方案在任务短、状态可丢弃、拓扑稳定或风险较低时仍合理。约束变化后，exact-v1 将机制定位在 platform/task lifecycle and continuously refreshed evaluation design；状态/控制权因此从隐式约定转为可测量、可版本化的系统对象。

Evaluation contract：competition/problem-set evaluations and model comparisons。作者结果只证明上述模型、硬件、数据、精度与实现条件中披露的范围；未披露字段不推断。反证与边界：mathematics-only, organizer and contamination boundary。Artifact：platform is public; event-time dataset revision not pinned。<!-- claim:SF-MATHARENA-LIVING-EVALUATION:start -->长期可保留结论是：Evaluation for fast-moving capabilities needs continuously refreshed, contamination-resistant tasks with versioned scoring rather than a static benchmark snapshot. 它不证明该实现跨 workload 普遍最优，也不授权跳过独立 evaluation、fallback 与 rollback。<!-- claim:SF-MATHARENA-LIVING-EVALUATION:end -->
<!-- review:SF-MATHARENA-LIVING-EVALUATION:end -->

<!-- review:SF-MEMROUTER-WRITE-ADMISSION:start -->
### MemRouter: Memory-as-Embedding Routing for Long-Term Conversational Agents

问题与旧路径：Memory write admission becomes an independently trained, measurable control plane rather than generation-time narration. 旧方案在任务短、状态可丢弃、拓扑稳定或风险较低时仍合理。约束变化后，exact-v1 将机制定位在 §§3–4 write-side router and matched harness；状态/控制权因此从隐式约定转为可测量、可版本化的系统对象。

Evaluation contract：§5 LoCoMo evaluation and factorial analysis。作者结果只证明上述模型、硬件、数据、精度与实现条件中披露的范围；未披露字段不推断。反证与边界：limitations/discussion and matched-QA-backbone boundary。Artifact：code/artifact revision not disclosed。<!-- claim:SF-MEMROUTER-WRITE-ADMISSION:start -->长期可保留结论是：Memory write admission becomes an independently trained, measurable control plane rather than generation-time narration. 它不证明该实现跨 workload 普遍最优，也不授权跳过独立 evaluation、fallback 与 rollback。<!-- claim:SF-MEMROUTER-WRITE-ADMISSION:end -->
<!-- review:SF-MEMROUTER-WRITE-ADMISSION:end -->

<!-- review:SF-PERSEUS-MEGAKERNEL-SIGNAL-ORDERING:start -->
### Eliminating Hidden Serialization in Multi-Node Megakernel Communication

问题与旧路径：Fine-grained MoE overlap fails across nodes when per-transfer fences serialize the NIC; signaling and ordering ownership must be separated. 旧方案在任务短、状态可丢弃、拓扑稳定或风险较低时仍合理。约束变化后，exact-v1 将机制定位在 §§3–5 root cause, decoupled signaling, NIC ordering and implementation；状态/控制权因此从隐式约定转为可测量、可版本化的系统对象。

Evaluation contract：§6 multi-platform/backend/model evaluation and ablation。作者结果只证明上述模型、硬件、数据、精度与实现条件中披露的范围；未披露字段不推断。反证与边界：§8 discussion; transport, topology and compute/communication regime boundary。Artifact：Triton-distributed case described; event-time patch not pinned。<!-- claim:SF-PERSEUS-MEGAKERNEL-SIGNAL-ORDERING:start -->长期可保留结论是：Fine-grained MoE overlap fails across nodes when per-transfer fences serialize the NIC; signaling and ordering ownership must be separated. 它不证明该实现跨 workload 普遍最优，也不授权跳过独立 evaluation、fallback 与 rollback。<!-- claim:SF-PERSEUS-MEGAKERNEL-SIGNAL-ORDERING:end -->
<!-- review:SF-PERSEUS-MEGAKERNEL-SIGNAL-ORDERING:end -->

<!-- review:SF-PROMPT-SCORE-VARIANCE-RELIABILITY:start -->
### Prompt-Induced Score Variance in Zero-Shot Binary Vision-Language Safety Classification

问题与旧路径：A deployable safety score must be tested across semantically equivalent prompts; one first-token probability is not a stable confidence contract. 旧方案在任务短、状态可丢弃、拓扑稳定或风险较低时仍合理。约束变化后，exact-v1 将机制定位在 §§3–4 cross-prompt quantities and mean-ensemble method；状态/控制权因此从隐式约定转为可测量、可版本化的系统对象。

Evaluation contract：§§5–6 locked 15-prompt protocol across 7 models and 2 datasets; Appendix C/F。作者结果只证明上述模型、硬件、数据、精度与实现条件中披露的范围；未披露字段不推断。反证与边界：§7 discussion and explicit non-implications; ranking/calibration boundary。Artifact：Appendix E.6 names code and analysis artifacts; immutable commit not established。<!-- claim:SF-PROMPT-SCORE-VARIANCE-RELIABILITY:start -->长期可保留结论是：A deployable safety score must be tested across semantically equivalent prompts; one first-token probability is not a stable confidence contract. 它不证明该实现跨 workload 普遍最优，也不授权跳过独立 evaluation、fallback 与 rollback。<!-- claim:SF-PROMPT-SCORE-VARIANCE-RELIABILITY:end -->
<!-- review:SF-PROMPT-SCORE-VARIANCE-RELIABILITY:end -->

<!-- review:SF-RUNAGENT-CONSTRAINT-GUIDED-EXECUTION:start -->
### RunAgent: Interpreting Natural-Language Plans with Constraint-Guided Execution

问题与旧路径：Natural-language plans need an executable intermediate representation with step constraints, rubrics and recovery transitions. 旧方案在任务短、状态可丢弃、拓扑稳定或风险较低时仍合理。约束变化后，exact-v1 将机制定位在 system/method sections: agentic language, constraints, rubrics and correction；状态/控制权因此从隐式约定转为可测量、可版本化的系统对象。

Evaluation contract：Natural-plan and SciBench evaluation。作者结果只证明上述模型、硬件、数据、精度与实现条件中披露的范围；未披露字段不推断。反证与边界：limitations/discussion; plan quality and evaluator boundary。Artifact：platform artifact revision not disclosed。<!-- claim:SF-RUNAGENT-CONSTRAINT-GUIDED-EXECUTION:start -->长期可保留结论是：Natural-language plans need an executable intermediate representation with step constraints, rubrics and recovery transitions. 它不证明该实现跨 workload 普遍最优，也不授权跳过独立 evaluation、fallback 与 rollback。<!-- claim:SF-RUNAGENT-CONSTRAINT-GUIDED-EXECUTION:end -->
<!-- review:SF-RUNAGENT-CONSTRAINT-GUIDED-EXECUTION:end -->

<!-- review:SF-SAGA-WORKFLOW-ATOMIC-SCHEDULING:start -->
### SAGA: Workflow-Atomic Scheduling for AI Agent Inference on GPU Clusters

问题与旧路径：Agent workflow, not isolated request, becomes the scheduling/fairness/cache-lifetime unit. 旧方案在任务短、状态可丢弃、拓扑稳定或风险较低时仍合理。约束变化后，exact-v1 将机制定位在 §§3–8 AEG, cache, batching, AFS and implementation；状态/控制权因此从隐式约定转为可测量、可版本化的系统对象。

Evaluation contract：§9 64-A100 evaluation and ablations。作者结果只证明上述模型、硬件、数据、精度与实现条件中披露的范围；未披露字段不推断。反证与边界：§1.5 explicit limitations and §9.8 trade-offs。Artifact：vLLM-based implementation; immutable event-time patch not disclosed。<!-- claim:SF-SAGA-WORKFLOW-ATOMIC-SCHEDULING:start -->长期可保留结论是：Agent workflow, not isolated request, becomes the scheduling/fairness/cache-lifetime unit. 它不证明该实现跨 workload 普遍最优，也不授权跳过独立 evaluation、fallback 与 rollback。<!-- claim:SF-SAGA-WORKFLOW-ATOMIC-SCHEDULING:end -->
<!-- review:SF-SAGA-WORKFLOW-ATOMIC-SCHEDULING:end -->

<!-- review:SF-SIMFA-ASYNC-GPU-SIMULATION:start -->
### Sim-FA: A GPGPU Simulator Framework for Fine-Grained Asynchronous Pipeline Analysis

问题与旧路径：GPU performance evidence for asynchronous attention pipelines must model TMA, barriers, warp specialization and cache traffic rather than rely on a coarse roofline alone. 旧方案在任务短、状态可丢弃、拓扑稳定或风险较低时仍合理。约束变化后，exact-v1 将机制定位在 §§3–5 traffic model, event-driven TMA simulation and FA3 trace translation；状态/控制权因此从隐式约定转为可测量、可版本化的系统对象。

Evaluation contract：§§5–6 H800 end-to-end and analytical-model validation。作者结果只证明上述模型、硬件、数据、精度与实现条件中披露的范围；未披露字段不推断。反证与边界：§4.1 abstraction scope and §7 simulator/model comparison boundary。Artifact：instrumented FA3/simulator described; immutable artifact revision not established。<!-- claim:SF-SIMFA-ASYNC-GPU-SIMULATION:start -->长期可保留结论是：GPU performance evidence for asynchronous attention pipelines must model TMA, barriers, warp specialization and cache traffic rather than rely on a coarse roofline alone. 它不证明该实现跨 workload 普遍最优，也不授权跳过独立 evaluation、fallback 与 rollback。<!-- claim:SF-SIMFA-ASYNC-GPU-SIMULATION:end -->
<!-- review:SF-SIMFA-ASYNC-GPU-SIMULATION:end -->

<!-- review:SF-SKILL-VERIFIABLE-ARTIFACT:start -->
### Skills as Verifiable Artifacts: A Trust Schema and a Biconditional Correctness Criterion for Human-in-the-Loop Agent Runtimes

问题与旧路径：Agent skills are untrusted executable artifacts whose verification level must gate capabilities and human approval. 旧方案在任务短、状态可丢弃、拓扑稳定或风险较低时仍合理。约束变化后，exact-v1 将机制定位在 trust schema, biconditional criterion and runtime profile；状态/控制权因此从隐式约定转为可测量、可版本化的系统对象。

Evaluation contract：adversarial-ensemble exercise/reference runtime。作者结果只证明上述模型、硬件、数据、精度与实现条件中披露的范围；未披露字段不推断。反证与边界：threat model and verification-level boundary。Artifact：reference implementation linked; immutable revision not established。<!-- claim:SF-SKILL-VERIFIABLE-ARTIFACT:start -->长期可保留结论是：Agent skills are untrusted executable artifacts whose verification level must gate capabilities and human approval. 它不证明该实现跨 workload 普遍最优，也不授权跳过独立 evaluation、fallback 与 rollback。<!-- claim:SF-SKILL-VERIFIABLE-ARTIFACT:end -->
<!-- review:SF-SKILL-VERIFIABLE-ARTIFACT:end -->

<!-- review:SF-TOOL-CALL-UTILITY-GATE:start -->
### To Call or Not to Call: A Framework to Assess and Optimize LLM Tool Calling

问题与旧路径：Tool invocation is an admission decision whose benefit, latency and failure cost must be estimated; availability alone does not justify a call. 旧方案在任务短、状态可丢弃、拓扑稳定或风险较低时仍合理。约束变化后，exact-v1 将机制定位在 tool-call utility model, assessment protocol and optimization framework；状态/控制权因此从隐式约定转为可测量、可版本化的系统对象。

Evaluation contract：multi-model/tool-use evaluations and cost-quality ablations。作者结果只证明上述模型、硬件、数据、精度与实现条件中披露的范围；未披露字段不推断。反证与边界：toolset, task and evaluator boundary。Artifact：framework artifact revision not disclosed。<!-- claim:SF-TOOL-CALL-UTILITY-GATE:start -->长期可保留结论是：Tool invocation is an admission decision whose benefit, latency and failure cost must be estimated; availability alone does not justify a call. 它不证明该实现跨 workload 普遍最优，也不授权跳过独立 evaluation、fallback 与 rollback。<!-- claim:SF-TOOL-CALL-UTILITY-GATE:end -->
<!-- review:SF-TOOL-CALL-UTILITY-GATE:end -->

<!-- review:SF-UCPO-CORRECT-SOLUTION-DIVERSITY:start -->
### Uniform-Correct Policy Optimization: Breaking RLVR's Indifference to Diversity

问题与旧路径：RLVR objectives can be indifferent among correct modes; a conditional uniformity term makes diversity an explicit optimization contract. 旧方案在任务短、状态可丢弃、拓扑稳定或风险较低时仍合理。约束变化后，exact-v1 将机制定位在 §§2–4 collapse analysis, optimality criteria and UCPO objective；状态/控制权因此从隐式约定转为可测量、可版本化的系统对象。

Evaluation contract：§5 and appendices across 3 models/5 math benchmarks。作者结果只证明上述模型、硬件、数据、精度与实现条件中披露的范围；未披露字段不推断。反证与边界：discussion/limitations; correct-set observability and math-only scope。Artifact：paper-linked GitHub; event-time commit not pinned。<!-- claim:SF-UCPO-CORRECT-SOLUTION-DIVERSITY:start -->长期可保留结论是：RLVR objectives can be indifferent among correct modes; a conditional uniformity term makes diversity an explicit optimization contract. 它不证明该实现跨 workload 普遍最优，也不授权跳过独立 evaluation、fallback 与 rollback。<!-- claim:SF-UCPO-CORRECT-SOLUTION-DIVERSITY:end -->
<!-- review:SF-UCPO-CORRECT-SOLUTION-DIVERSITY:end -->

<!-- review:SF-VLM-VISUAL-JAILBREAK-CROSS-MODAL-GAP:start -->
### Jailbreaking Vision-Language Models Through the Visual Modality

问题与旧路径：Safety post-training and threat models must treat the visual channel as an active intent-bearing attack surface rather than assume text-domain alignment composes across modalities. 旧方案在任务短、状态可丢弃、拓扑稳定或风险较低时仍合理。约束变化后，exact-v1 将机制定位在 §3 four visual attack constructions and shared protocol；状态/控制权因此从隐式约定转为可测量、可版本化的系统对象。

Evaluation contract：§4 six frontier VLM evaluation with judge aggregation。作者结果只证明上述模型、硬件、数据、精度与实现条件中披露的范围；未披露字段不推断。反证与边界：§5 discussion, limitations and mitigations; threat-model and judge boundary。Artifact：paper-linked GitHub; immutable event-time commit not pinned。<!-- claim:SF-VLM-VISUAL-JAILBREAK-CROSS-MODAL-GAP:start -->长期可保留结论是：Safety post-training and threat models must treat the visual channel as an active intent-bearing attack surface rather than assume text-domain alignment composes across modalities. 它不证明该实现跨 workload 普遍最优，也不授权跳过独立 evaluation、fallback 与 rollback。<!-- claim:SF-VLM-VISUAL-JAILBREAK-CROSS-MODAL-GAP:end -->
<!-- review:SF-VLM-VISUAL-JAILBREAK-CROSS-MODAL-GAP:end -->

## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-00066 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2605-00081 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2605-00136 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2605-00155 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2605-00161 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2605-00180 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2605-00206 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2605-00226 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2605-00254 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2605-00267 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2605-00300 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2605-00314 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-AEM-AGENTIC-RL-ENTROPY-CREDIT | exact-v1 disclosed workload for AEM: Adaptive Entropy Modulation for Multi-Turn Agentic Reinforcement Learning | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless exact-v1 Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/throughput contract only | author protocol; independent reproduction Not Disclosed |
| SF-AFFORDANCE-HARNESS-VERIFICATION-GATED-SKILLS | exact-v1 disclosed workload for Affordance Agent Harness: Verification-Gated Skill Orchestration | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless exact-v1 Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/throughput contract only | author protocol; independent reproduction Not Disclosed |
| SF-AGENT-CAPSULES-QUALITY-GATED-GRANULARITY | exact-v1 disclosed workload for Agent Capsules: Quality-Gated Granularity Control for Multi-Agent LLM Pipelines | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless exact-v1 Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/throughput contract only | author protocol; independent reproduction Not Disclosed |
| SF-AGOQ-ACTIVATION-GRADIENT-QUANTIZATION | exact-v1 disclosed workload for AGoQ: Activation and Gradient Quantization for Memory-Efficient Distributed Training of LLMs | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless exact-v1 Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/throughput contract only | author protocol; independent reproduction Not Disclosed |
| SF-AUTOMAT-CLAIM-REPRODUCTION-CONTRACT | exact-v1 disclosed workload for Can Coding Agents Reproduce Findings in Computational Materials Science? | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless exact-v1 Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/throughput contract only | author protocol; independent reproduction Not Disclosed |
| SF-BREW-WATERMARK-DESIGNATED-VERIFICATION | exact-v1 disclosed workload for Block-wise Codeword Embedding for Reliable Multi-bit Text Watermarking | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless exact-v1 Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/throughput contract only | author protocol; independent reproduction Not Disclosed |
| SF-CLEANBASE-RAG-DOCUMENT-GRAPH | exact-v1 disclosed workload for CleanBase: Detecting Malicious Documents in RAG Knowledge Databases | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless exact-v1 Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/throughput contract only | author protocol; independent reproduction Not Disclosed |
| SF-EVICT-MOE-VERIFICATION-UTILITY | exact-v1 disclosed workload for Making Every Verified Token Count: Adaptive Verification for MoE Speculative Decoding | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless exact-v1 Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/throughput contract only | author protocol; independent reproduction Not Disclosed |
| SF-EVOLVING-MEMORY-TWO-STAGE-OPTIMIZATION | exact-v1 disclosed workload for Learning How and What to Memorize: Cognition-Inspired Two-Stage Optimization for Evolving Memory | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless exact-v1 Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/throughput contract only | author protocol; independent reproduction Not Disclosed |
| SF-FORWARD-REPLAY-MODEL-EDIT-TARGETS | exact-v1 disclosed workload for From Backward Spreading to Forward Replay: Revisiting Target Construction in LLM Parameter Editing | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless exact-v1 Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/throughput contract only | author protocol; independent reproduction Not Disclosed |
| SF-IEFF-CONTINUOUS-FEATURE-FADING | exact-v1 disclosed workload for Intelligent Elastic Feature Fading: Enabling Model Retrain-Free Feature Efficiency Rollouts at Scale | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless exact-v1 Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/throughput contract only | author protocol; independent reproduction Not Disclosed |
| SF-LIGHTKV-PROMPT-GUIDED-VISION-KV | exact-v1 disclosed workload for Make Your LVLM KV Cache More Lightweight | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless exact-v1 Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/throughput contract only | author protocol; independent reproduction Not Disclosed |
| SF-LLM-EMU-NATIVE-RUNTIME-EMULATION | exact-v1 disclosed workload for LLM-Emu: Native Runtime Emulation of LLM Inference via Profile-Driven Sampling | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless exact-v1 Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/throughput contract only | author protocol; independent reproduction Not Disclosed |
| SF-LWD-FLEET-OFFLINE-ONLINE-ROBOT-RL | exact-v1 disclosed workload for Learning While Deploying: Fleet-Scale Reinforcement Learning for Generalist Robot Policies | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless exact-v1 Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/throughput contract only | author protocol; independent reproduction Not Disclosed |
| SF-MATHARENA-LIVING-EVALUATION | exact-v1 disclosed workload for Beyond Benchmarks: MathArena as an Evaluation Platform for Mathematics with LLMs | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless exact-v1 Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/throughput contract only | author protocol; independent reproduction Not Disclosed |
| SF-MEMROUTER-WRITE-ADMISSION | exact-v1 disclosed workload for MemRouter: Memory-as-Embedding Routing for Long-Term Conversational Agents | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless exact-v1 Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/throughput contract only | author protocol; independent reproduction Not Disclosed |
| SF-PERSEUS-MEGAKERNEL-SIGNAL-ORDERING | exact-v1 disclosed workload for Eliminating Hidden Serialization in Multi-Node Megakernel Communication | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless exact-v1 Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/throughput contract only | author protocol; independent reproduction Not Disclosed |
| SF-PROMPT-SCORE-VARIANCE-RELIABILITY | exact-v1 disclosed workload for Prompt-Induced Score Variance in Zero-Shot Binary Vision-Language Safety Classification | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless exact-v1 Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/throughput contract only | author protocol; independent reproduction Not Disclosed |
| SF-RUNAGENT-CONSTRAINT-GUIDED-EXECUTION | exact-v1 disclosed workload for RunAgent: Interpreting Natural-Language Plans with Constraint-Guided Execution | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless exact-v1 Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/throughput contract only | author protocol; independent reproduction Not Disclosed |
| SF-SAGA-WORKFLOW-ATOMIC-SCHEDULING | exact-v1 disclosed workload for SAGA: Workflow-Atomic Scheduling for AI Agent Inference on GPU Clusters | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless exact-v1 Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/throughput contract only | author protocol; independent reproduction Not Disclosed |
| SF-SIMFA-ASYNC-GPU-SIMULATION | exact-v1 disclosed workload for Sim-FA: A GPGPU Simulator Framework for Fine-Grained Asynchronous Pipeline Analysis | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless exact-v1 Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/throughput contract only | author protocol; independent reproduction Not Disclosed |
| SF-SKILL-VERIFIABLE-ARTIFACT | exact-v1 disclosed workload for Skills as Verifiable Artifacts: A Trust Schema and a Biconditional Correctness Criterion for Human-in-the-Loop Agent Runtimes | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless exact-v1 Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/throughput contract only | author protocol; independent reproduction Not Disclosed |
| SF-TOOL-CALL-UTILITY-GATE | exact-v1 disclosed workload for To Call or Not to Call: A Framework to Assess and Optimize LLM Tool Calling | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless exact-v1 Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/throughput contract only | author protocol; independent reproduction Not Disclosed |
| SF-UCPO-CORRECT-SOLUTION-DIVERSITY | exact-v1 disclosed workload for Uniform-Correct Policy Optimization: Breaking RLVR's Indifference to Diversity | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless exact-v1 Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/throughput contract only | author protocol; independent reproduction Not Disclosed |
| SF-VLM-VISUAL-JAILBREAK-CROSS-MODAL-GAP | exact-v1 disclosed workload for Jailbreaking Vision-Language Models Through the Visual Modality | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless exact-v1 Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/throughput contract only | author protocol; independent reproduction Not Disclosed |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-00066 | score_7_9;forced_review | selected | DA-20260504-01 | — | Score=9/9 且属于当日最高跨系统设计影响；有限叙事预算不替代其余 Source Review。 | analysis:DA-20260504-01 |
| SF-2026-ARXIV-2605-00081 | score_7_9;forced_review | selected | DA-20260504-02 | — | Score=9/9 且属于当日最高跨系统设计影响；有限叙事预算不替代其余 Source Review。 | analysis:DA-20260504-02 |
| SF-2026-ARXIV-2605-00136 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-00136 |
| SF-2026-ARXIV-2605-00161 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-00161 |
| SF-2026-ARXIV-2605-00180 | score_7_9;forced_review | selected | DA-20260504-03 | — | Score=9/9 且属于当日最高跨系统设计影响；有限叙事预算不替代其余 Source Review。 | analysis:DA-20260504-03 |
| SF-2026-ARXIV-2605-00206 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-00206 |
| SF-2026-ARXIV-2605-00226 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-00226 |
| SF-2026-ARXIV-2605-00254 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-00254 |
| SF-2026-ARXIV-2605-00267 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-00267 |
| SF-2026-ARXIV-2605-00300 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-00300 |
| SF-2026-ARXIV-2605-00314 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-00314 |
| SF-AEM-AGENTIC-RL-ENTROPY-CREDIT | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-AEM-AGENTIC-RL-ENTROPY-CREDIT |
| SF-AFFORDANCE-HARNESS-VERIFICATION-GATED-SKILLS | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-AFFORDANCE-HARNESS-VERIFICATION-GATED-SKILLS |
| SF-AGENT-CAPSULES-QUALITY-GATED-GRANULARITY | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-AGENT-CAPSULES-QUALITY-GATED-GRANULARITY |
| SF-AGOQ-ACTIVATION-GRADIENT-QUANTIZATION | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-AGOQ-ACTIVATION-GRADIENT-QUANTIZATION |
| SF-AUTOMAT-CLAIM-REPRODUCTION-CONTRACT | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-AUTOMAT-CLAIM-REPRODUCTION-CONTRACT |
| SF-BREW-WATERMARK-DESIGNATED-VERIFICATION | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-BREW-WATERMARK-DESIGNATED-VERIFICATION |
| SF-EVICT-MOE-VERIFICATION-UTILITY | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-EVICT-MOE-VERIFICATION-UTILITY |
| SF-EVOLVING-MEMORY-TWO-STAGE-OPTIMIZATION | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-EVOLVING-MEMORY-TWO-STAGE-OPTIMIZATION |
| SF-FORWARD-REPLAY-MODEL-EDIT-TARGETS | score_7_9;forced_review;potential_structural_gap | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-FORWARD-REPLAY-MODEL-EDIT-TARGETS |
| SF-IEFF-CONTINUOUS-FEATURE-FADING | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-IEFF-CONTINUOUS-FEATURE-FADING |
| SF-LIGHTKV-PROMPT-GUIDED-VISION-KV | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-LIGHTKV-PROMPT-GUIDED-VISION-KV |
| SF-LLM-EMU-NATIVE-RUNTIME-EMULATION | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-LLM-EMU-NATIVE-RUNTIME-EMULATION |
| SF-LWD-FLEET-OFFLINE-ONLINE-ROBOT-RL | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-LWD-FLEET-OFFLINE-ONLINE-ROBOT-RL |
| SF-MATHARENA-LIVING-EVALUATION | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-MATHARENA-LIVING-EVALUATION |
| SF-MEMROUTER-WRITE-ADMISSION | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-MEMROUTER-WRITE-ADMISSION |
| SF-PERSEUS-MEGAKERNEL-SIGNAL-ORDERING | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-PERSEUS-MEGAKERNEL-SIGNAL-ORDERING |
| SF-PROMPT-SCORE-VARIANCE-RELIABILITY | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-PROMPT-SCORE-VARIANCE-RELIABILITY |
| SF-RUNAGENT-CONSTRAINT-GUIDED-EXECUTION | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-RUNAGENT-CONSTRAINT-GUIDED-EXECUTION |
| SF-SAGA-WORKFLOW-ATOMIC-SCHEDULING | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-SAGA-WORKFLOW-ATOMIC-SCHEDULING |
| SF-SIMFA-ASYNC-GPU-SIMULATION | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-SIMFA-ASYNC-GPU-SIMULATION |
| SF-SKILL-VERIFIABLE-ARTIFACT | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-SKILL-VERIFIABLE-ARTIFACT |
| SF-TOOL-CALL-UTILITY-GATE | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-TOOL-CALL-UTILITY-GATE |
| SF-UCPO-CORRECT-SOLUTION-DIVERSITY | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-UCPO-CORRECT-SOLUTION-DIVERSITY |
| SF-VLM-VISUAL-JAILBREAK-CROSS-MODAL-GAP | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-VLM-VISUAL-JAILBREAK-CROSS-MODAL-GAP |

<!-- analysis:DA-20260504-01:start -->
### Deep Analysis — SF-2026-ARXIV-2605-00066

该 family 的 Score V2=9/9；Source Review 已闭合问题、旧路径、机制 owner、evaluation boundary、trade-off 与共存条件。Deep Analysis 只提升叙事优先级，不改变 Evidence Gate。
<!-- analysis:DA-20260504-01:end -->

<!-- analysis:DA-20260504-02:start -->
### Deep Analysis — SF-2026-ARXIV-2605-00081

该 family 的 Score V2=9/9；Source Review 已闭合问题、旧路径、机制 owner、evaluation boundary、trade-off 与共存条件。Deep Analysis 只提升叙事优先级，不改变 Evidence Gate。
<!-- analysis:DA-20260504-02:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-00136:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-00136:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-00161:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-00161:end -->

<!-- analysis:DA-20260504-03:start -->
### Deep Analysis — SF-2026-ARXIV-2605-00180

该 family 的 Score V2=9/9；Source Review 已闭合问题、旧路径、机制 owner、evaluation boundary、trade-off 与共存条件。Deep Analysis 只提升叙事优先级，不改变 Evidence Gate。
<!-- analysis:DA-20260504-03:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-00206:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-00206:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-00226:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-00226:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-00254:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-00254:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-00267:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-00267:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-00300:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-00300:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-00314:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-00314:end -->

<!-- analysis-decision:SF-AEM-AGENTIC-RL-ENTROPY-CREDIT:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-AEM-AGENTIC-RL-ENTROPY-CREDIT:end -->

<!-- analysis-decision:SF-AFFORDANCE-HARNESS-VERIFICATION-GATED-SKILLS:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-AFFORDANCE-HARNESS-VERIFICATION-GATED-SKILLS:end -->

<!-- analysis-decision:SF-AGENT-CAPSULES-QUALITY-GATED-GRANULARITY:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-AGENT-CAPSULES-QUALITY-GATED-GRANULARITY:end -->

<!-- analysis-decision:SF-AGOQ-ACTIVATION-GRADIENT-QUANTIZATION:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-AGOQ-ACTIVATION-GRADIENT-QUANTIZATION:end -->

<!-- analysis-decision:SF-AUTOMAT-CLAIM-REPRODUCTION-CONTRACT:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-AUTOMAT-CLAIM-REPRODUCTION-CONTRACT:end -->

<!-- analysis-decision:SF-BREW-WATERMARK-DESIGNATED-VERIFICATION:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-BREW-WATERMARK-DESIGNATED-VERIFICATION:end -->

<!-- analysis-decision:SF-EVICT-MOE-VERIFICATION-UTILITY:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-EVICT-MOE-VERIFICATION-UTILITY:end -->

<!-- analysis-decision:SF-EVOLVING-MEMORY-TWO-STAGE-OPTIMIZATION:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-EVOLVING-MEMORY-TWO-STAGE-OPTIMIZATION:end -->

<!-- analysis-decision:SF-FORWARD-REPLAY-MODEL-EDIT-TARGETS:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-FORWARD-REPLAY-MODEL-EDIT-TARGETS:end -->

<!-- analysis-decision:SF-IEFF-CONTINUOUS-FEATURE-FADING:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-IEFF-CONTINUOUS-FEATURE-FADING:end -->

<!-- analysis-decision:SF-LIGHTKV-PROMPT-GUIDED-VISION-KV:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-LIGHTKV-PROMPT-GUIDED-VISION-KV:end -->

<!-- analysis-decision:SF-LLM-EMU-NATIVE-RUNTIME-EMULATION:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-LLM-EMU-NATIVE-RUNTIME-EMULATION:end -->

<!-- analysis-decision:SF-LWD-FLEET-OFFLINE-ONLINE-ROBOT-RL:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-LWD-FLEET-OFFLINE-ONLINE-ROBOT-RL:end -->

<!-- analysis-decision:SF-MATHARENA-LIVING-EVALUATION:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-MATHARENA-LIVING-EVALUATION:end -->

<!-- analysis-decision:SF-MEMROUTER-WRITE-ADMISSION:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-MEMROUTER-WRITE-ADMISSION:end -->

<!-- analysis-decision:SF-PERSEUS-MEGAKERNEL-SIGNAL-ORDERING:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-PERSEUS-MEGAKERNEL-SIGNAL-ORDERING:end -->

<!-- analysis-decision:SF-PROMPT-SCORE-VARIANCE-RELIABILITY:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-PROMPT-SCORE-VARIANCE-RELIABILITY:end -->

<!-- analysis-decision:SF-RUNAGENT-CONSTRAINT-GUIDED-EXECUTION:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-RUNAGENT-CONSTRAINT-GUIDED-EXECUTION:end -->

<!-- analysis-decision:SF-SAGA-WORKFLOW-ATOMIC-SCHEDULING:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-SAGA-WORKFLOW-ATOMIC-SCHEDULING:end -->

<!-- analysis-decision:SF-SIMFA-ASYNC-GPU-SIMULATION:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-SIMFA-ASYNC-GPU-SIMULATION:end -->

<!-- analysis-decision:SF-SKILL-VERIFIABLE-ARTIFACT:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-SKILL-VERIFIABLE-ARTIFACT:end -->

<!-- analysis-decision:SF-TOOL-CALL-UTILITY-GATE:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-TOOL-CALL-UTILITY-GATE:end -->

<!-- analysis-decision:SF-UCPO-CORRECT-SOLUTION-DIVERSITY:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-UCPO-CORRECT-SOLUTION-DIVERSITY:end -->

<!-- analysis-decision:SF-VLM-VISUAL-JAILBREAK-CROSS-MODAL-GAP:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-VLM-VISUAL-JAILBREAK-CROSS-MODAL-GAP:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-00066 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L35 | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L27; books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2026-ARXIV-2605-00066 | delta:SF-2026-ARXIV-2605-00066 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-00066 |
| SF-2026-ARXIV-2605-00081 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L14 | books/part-07-agent/78-tool-calling.md#L14; books/part-07-agent/84-agent-platform.md#L74 | existing:SF-2026-ARXIV-2605-00081 | delta:SF-2026-ARXIV-2605-00081 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-00081 |
| SF-2026-ARXIV-2605-00136 | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#L42 | books/part-07-agent/81-workflow.md#L1; books/part-07-agent/84-agent-platform.md#L50 | existing:SF-2026-ARXIV-2605-00136 | delta:SF-2026-ARXIV-2605-00136 | Explanatory Analogy | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-00136 |
| SF-2026-ARXIV-2605-00155 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#L168 | books/part-04-training-system/32-ppo.md#L1; books/part-04-training-system/34-dpo.md#L1 | existing:SF-2026-ARXIV-2605-00155 | delta:SF-2026-ARXIV-2605-00155 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-00155 |
| SF-2026-ARXIV-2605-00161 | MULTIMODAL-GENERATIVE-PARADIGMS | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L1 | books/part-02-model/18-decoder-only.md#L1; books/part-05-inference-system/48-speculative-decoding.md#L1 | existing:SF-2026-ARXIV-2605-00161 | delta:SF-2026-ARXIV-2605-00161 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-00161 |
| SF-2026-ARXIV-2605-00180 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#L35 | books/part-05-inference-system/52-distributed-inference.md#L1; books/part-06-ai-infrastructure/63-resource-scheduling.md#L1 | existing:SF-2026-ARXIV-2605-00180 | delta:SF-2026-ARXIV-2605-00180 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-00180 |
| SF-2026-ARXIV-2605-00206 | MODEL-DECODER-ONLY | books/part-02-model/18-decoder-only.md#L1 | books/part-02-model/15-attention.md#L1; books/part-04-training-system/36-distributed-training.md#L1 | existing:SF-2026-ARXIV-2605-00206 | delta:SF-2026-ARXIV-2605-00206 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-00206 |
| SF-2026-ARXIV-2605-00226 | AGENT-PLANNING | books/part-07-agent/79-planning.md#L1 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1; books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | existing:SF-2026-ARXIV-2605-00226 | delta:SF-2026-ARXIV-2605-00226 | Explanatory Analogy | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-00226 |
| SF-2026-ARXIV-2605-00254 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#L35 | books/part-05-inference-system/52-distributed-inference.md#L1; books/part-05-inference-system/55-inference-memory-optimization.md#L1 | existing:SF-2026-ARXIV-2605-00254 | delta:SF-2026-ARXIV-2605-00254 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-00254 |
| SF-2026-ARXIV-2605-00267 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L14 | books/part-06-ai-infrastructure/66-evaluation-system.md#L18; books/part-07-agent/84-agent-platform.md#L74 | existing:SF-2026-ARXIV-2605-00267 | delta:SF-2026-ARXIV-2605-00267 | Explanatory Analogy | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-00267 |
| SF-2026-ARXIV-2605-00300 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L35 | books/part-05-inference-system/56-inference-scheduling.md#L55; books/part-06-ai-infrastructure/69-cost-management.md#L1 | existing:SF-2026-ARXIV-2605-00300 | delta:SF-2026-ARXIV-2605-00300 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-00300 |
| SF-2026-ARXIV-2605-00314 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L14 | books/part-07-agent/78-tool-calling.md#L42; books/part-07-agent/83-mcp.md#L40 | existing:SF-2026-ARXIV-2605-00314 | delta:SF-2026-ARXIV-2605-00314 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2605-00314 |
| SF-AEM-AGENTIC-RL-ENTROPY-CREDIT | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#chapter-33 | books/part-04-training-system/32-ppo.md#adjacent-chapter | existing:SF-AEM-AGENTIC-RL-ENTROPY-CREDIT | delta:SF-AEM-AGENTIC-RL-ENTROPY-CREDIT | Layering / Dependency | No Change — Existing Coverage | books-review:SF-AEM-AGENTIC-RL-ENTROPY-CREDIT |
| SF-AFFORDANCE-HARNESS-VERIFICATION-GATED-SKILLS | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#adjacent-chapter | existing:SF-AFFORDANCE-HARNESS-VERIFICATION-GATED-SKILLS | delta:SF-AFFORDANCE-HARNESS-VERIFICATION-GATED-SKILLS | Layering / Dependency | No Change — Existing Coverage | books-review:SF-AFFORDANCE-HARNESS-VERIFICATION-GATED-SKILLS |
| SF-AGENT-CAPSULES-QUALITY-GATED-GRANULARITY | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#adjacent-chapter | existing:SF-AGENT-CAPSULES-QUALITY-GATED-GRANULARITY | delta:SF-AGENT-CAPSULES-QUALITY-GATED-GRANULARITY | Layering / Dependency | No Change — Existing Coverage | books-review:SF-AGENT-CAPSULES-QUALITY-GATED-GRANULARITY |
| SF-AGOQ-ACTIVATION-GRADIENT-QUANTIZATION | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#chapter-36 | books/part-04-training-system/35-checkpoint.md#adjacent-chapter | existing:SF-AGOQ-ACTIVATION-GRADIENT-QUANTIZATION | delta:SF-AGOQ-ACTIVATION-GRADIENT-QUANTIZATION | Layering / Dependency | No Change — Existing Coverage | books-review:SF-AGOQ-ACTIVATION-GRADIENT-QUANTIZATION |
| SF-AUTOMAT-CLAIM-REPRODUCTION-CONTRACT | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#adjacent-chapter | existing:SF-AUTOMAT-CLAIM-REPRODUCTION-CONTRACT | delta:SF-AUTOMAT-CLAIM-REPRODUCTION-CONTRACT | Layering / Dependency | No Change — Existing Coverage | books-review:SF-AUTOMAT-CLAIM-REPRODUCTION-CONTRACT |
| SF-BREW-WATERMARK-DESIGNATED-VERIFICATION | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#adjacent-chapter | existing:SF-BREW-WATERMARK-DESIGNATED-VERIFICATION | delta:SF-BREW-WATERMARK-DESIGNATED-VERIFICATION | Layering / Dependency | No Change — Existing Coverage | books-review:SF-BREW-WATERMARK-DESIGNATED-VERIFICATION |
| SF-CLEANBASE-RAG-DOCUMENT-GRAPH | AGENT-RAG | books/part-07-agent/76-rag.md#chapter-76 | books/part-07-agent/75-context.md#adjacent-chapter | existing:SF-CLEANBASE-RAG-DOCUMENT-GRAPH | delta:SF-CLEANBASE-RAG-DOCUMENT-GRAPH | Layering / Dependency | No Change — Existing Coverage | books-review:SF-CLEANBASE-RAG-DOCUMENT-GRAPH |
| SF-EVICT-MOE-VERIFICATION-UTILITY | INFER-SPECULATIVE-DECODING | books/part-05-inference-system/48-speculative-decoding.md#chapter-48 | books/part-05-inference-system/47-pagedattention.md#adjacent-chapter | existing:SF-EVICT-MOE-VERIFICATION-UTILITY | delta:SF-EVICT-MOE-VERIFICATION-UTILITY | Layering / Dependency | No Change — Existing Coverage | books-review:SF-EVICT-MOE-VERIFICATION-UTILITY |
| SF-EVOLVING-MEMORY-TWO-STAGE-OPTIMIZATION | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#adjacent-chapter | existing:SF-EVOLVING-MEMORY-TWO-STAGE-OPTIMIZATION | delta:SF-EVOLVING-MEMORY-TWO-STAGE-OPTIMIZATION | Layering / Dependency | No Change — Existing Coverage | books-review:SF-EVOLVING-MEMORY-TWO-STAGE-OPTIMIZATION |
| SF-FORWARD-REPLAY-MODEL-EDIT-TARGETS | considered:PLATFORM-MODEL-REGISTRY,TRAIN-LORA,AGENT-MEMORY | books/part-06-ai-infrastructure/59-model-registry.md#L10 | books/part-04-training-system/30-lora.md#L10; books/part-07-agent/77-memory.md#L10 | existing:SF-FORWARD-REPLAY-MODEL-EDIT-TARGETS | delta:SF-FORWARD-REPLAY-MODEL-EDIT-TARGETS | Alternative Branch | Structural Candidate | books-review:SF-FORWARD-REPLAY-MODEL-EDIT-TARGETS |
| SF-IEFF-CONTINUOUS-FEATURE-FADING | PLATFORM-PRODUCTION | books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | books/part-06-ai-infrastructure/72-security.md#adjacent-chapter | existing:SF-IEFF-CONTINUOUS-FEATURE-FADING | delta:SF-IEFF-CONTINUOUS-FEATURE-FADING | Direct Evolution | Integrate | books-review:SF-IEFF-CONTINUOUS-FEATURE-FADING |
| SF-LIGHTKV-PROMPT-GUIDED-VISION-KV | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#chapter-45 | books/part-05-inference-system/44-decode.md#adjacent-chapter | existing:SF-LIGHTKV-PROMPT-GUIDED-VISION-KV | delta:SF-LIGHTKV-PROMPT-GUIDED-VISION-KV | Layering / Dependency | No Change — Existing Coverage | books-review:SF-LIGHTKV-PROMPT-GUIDED-VISION-KV |
| SF-LLM-EMU-NATIVE-RUNTIME-EMULATION | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#adjacent-chapter | existing:SF-LLM-EMU-NATIVE-RUNTIME-EMULATION | delta:SF-LLM-EMU-NATIVE-RUNTIME-EMULATION | Layering / Dependency | No Change — Existing Coverage | books-review:SF-LLM-EMU-NATIVE-RUNTIME-EMULATION |
| SF-LWD-FLEET-OFFLINE-ONLINE-ROBOT-RL | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#adjacent-chapter | existing:SF-LWD-FLEET-OFFLINE-ONLINE-ROBOT-RL | delta:SF-LWD-FLEET-OFFLINE-ONLINE-ROBOT-RL | Direct Evolution | Integrate | books-review:SF-LWD-FLEET-OFFLINE-ONLINE-ROBOT-RL |
| SF-MATHARENA-LIVING-EVALUATION | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#adjacent-chapter | existing:SF-MATHARENA-LIVING-EVALUATION | delta:SF-MATHARENA-LIVING-EVALUATION | Layering / Dependency | No Change — Existing Coverage | books-review:SF-MATHARENA-LIVING-EVALUATION |
| SF-MEMROUTER-WRITE-ADMISSION | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#adjacent-chapter | existing:SF-MEMROUTER-WRITE-ADMISSION | delta:SF-MEMROUTER-WRITE-ADMISSION | Layering / Dependency | No Change — Existing Coverage | books-review:SF-MEMROUTER-WRITE-ADMISSION |
| SF-PERSEUS-MEGAKERNEL-SIGNAL-ORDERING | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | books/part-05-inference-system/48-speculative-decoding.md#adjacent-chapter | existing:SF-PERSEUS-MEGAKERNEL-SIGNAL-ORDERING | delta:SF-PERSEUS-MEGAKERNEL-SIGNAL-ORDERING | Direct Evolution | Integrate | books-review:SF-PERSEUS-MEGAKERNEL-SIGNAL-ORDERING |
| SF-PROMPT-SCORE-VARIANCE-RELIABILITY | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#adjacent-chapter | existing:SF-PROMPT-SCORE-VARIANCE-RELIABILITY | delta:SF-PROMPT-SCORE-VARIANCE-RELIABILITY | Layering / Dependency | No Change — Existing Coverage | books-review:SF-PROMPT-SCORE-VARIANCE-RELIABILITY |
| SF-RUNAGENT-CONSTRAINT-GUIDED-EXECUTION | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#chapter-81 | books/part-07-agent/80-reflection.md#adjacent-chapter | existing:SF-RUNAGENT-CONSTRAINT-GUIDED-EXECUTION | delta:SF-RUNAGENT-CONSTRAINT-GUIDED-EXECUTION | Layering / Dependency | No Change — Existing Coverage | books-review:SF-RUNAGENT-CONSTRAINT-GUIDED-EXECUTION |
| SF-SAGA-WORKFLOW-ATOMIC-SCHEDULING | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#chapter-56 | books/part-05-inference-system/55-pd-disaggregation.md#adjacent-chapter | existing:SF-SAGA-WORKFLOW-ATOMIC-SCHEDULING | delta:SF-SAGA-WORKFLOW-ATOMIC-SCHEDULING | Layering / Dependency | No Change — Existing Coverage | books-review:SF-SAGA-WORKFLOW-ATOMIC-SCHEDULING |
| SF-SIMFA-ASYNC-GPU-SIMULATION | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | books/part-05-inference-system/48-speculative-decoding.md#adjacent-chapter | existing:SF-SIMFA-ASYNC-GPU-SIMULATION | delta:SF-SIMFA-ASYNC-GPU-SIMULATION | Layering / Dependency | No Change — Existing Coverage | books-review:SF-SIMFA-ASYNC-GPU-SIMULATION |
| SF-SKILL-VERIFIABLE-ARTIFACT | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#adjacent-chapter | existing:SF-SKILL-VERIFIABLE-ARTIFACT | delta:SF-SKILL-VERIFIABLE-ARTIFACT | Layering / Dependency | No Change — Existing Coverage | books-review:SF-SKILL-VERIFIABLE-ARTIFACT |
| SF-TOOL-CALL-UTILITY-GATE | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#chapter-78 | books/part-07-agent/77-memory.md#adjacent-chapter | existing:SF-TOOL-CALL-UTILITY-GATE | delta:SF-TOOL-CALL-UTILITY-GATE | Direct Evolution | Integrate | books-review:SF-TOOL-CALL-UTILITY-GATE |
| SF-UCPO-CORRECT-SOLUTION-DIVERSITY | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#chapter-33 | books/part-04-training-system/32-ppo.md#adjacent-chapter | existing:SF-UCPO-CORRECT-SOLUTION-DIVERSITY | delta:SF-UCPO-CORRECT-SOLUTION-DIVERSITY | Layering / Dependency | No Change — Existing Coverage | books-review:SF-UCPO-CORRECT-SOLUTION-DIVERSITY |
| SF-VLM-VISUAL-JAILBREAK-CROSS-MODAL-GAP | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#adjacent-chapter | existing:SF-VLM-VISUAL-JAILBREAK-CROSS-MODAL-GAP | delta:SF-VLM-VISUAL-JAILBREAK-CROSS-MODAL-GAP | Layering / Dependency | No Change — Existing Coverage | books-review:SF-VLM-VISUAL-JAILBREAK-CROSS-MODAL-GAP |

<!-- books-review:SF-2026-ARXIV-2605-00066:start -->
<!-- existing:SF-2026-ARXIV-2605-00066:start -->
已核对 `books/part-06-ai-infrastructure/66-evaluation-system.md#L35` 与 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L27; books/part-06-ai-infrastructure/67-monitoring.md#L1`；现有正文已拥有该 state/control/evidence boundary。
<!-- existing:SF-2026-ARXIV-2605-00066:end -->
<!-- delta:SF-2026-ARXIV-2605-00066:start -->
本 family 只收紧机制证据或适用边界，不产生新的长期命题；保留为受限 evidence case。
<!-- delta:SF-2026-ARXIV-2605-00066:end -->
演进关系 `Principle Reuse`；决定 `No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-00066:end -->

<!-- books-review:SF-2026-ARXIV-2605-00081:start -->
<!-- existing:SF-2026-ARXIV-2605-00081:start -->
已核对 `books/part-06-ai-infrastructure/72-security.md#L14` 与 `books/part-07-agent/78-tool-calling.md#L14; books/part-07-agent/84-agent-platform.md#L74`；现有正文已拥有该 state/control/evidence boundary。
<!-- existing:SF-2026-ARXIV-2605-00081:end -->
<!-- delta:SF-2026-ARXIV-2605-00081:start -->
本 family 只收紧机制证据或适用边界，不产生新的长期命题；保留为受限 evidence case。
<!-- delta:SF-2026-ARXIV-2605-00081:end -->
演进关系 `Direct Evolution`；决定 `No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-00081:end -->

<!-- books-review:SF-2026-ARXIV-2605-00136:start -->
<!-- existing:SF-2026-ARXIV-2605-00136:start -->
已核对 `books/part-07-agent/78-tool-calling.md#L42` 与 `books/part-07-agent/81-workflow.md#L1; books/part-07-agent/84-agent-platform.md#L50`；现有正文已拥有该 state/control/evidence boundary。
<!-- existing:SF-2026-ARXIV-2605-00136:end -->
<!-- delta:SF-2026-ARXIV-2605-00136:start -->
本 family 只收紧机制证据或适用边界，不产生新的长期命题；保留为受限 evidence case。
<!-- delta:SF-2026-ARXIV-2605-00136:end -->
演进关系 `Explanatory Analogy`；决定 `No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-00136:end -->

<!-- books-review:SF-2026-ARXIV-2605-00155:start -->
<!-- existing:SF-2026-ARXIV-2605-00155:start -->
已核对 `books/part-04-training-system/31-rlhf.md#L168` 与 `books/part-04-training-system/32-ppo.md#L1; books/part-04-training-system/34-dpo.md#L1`；现有正文已拥有该 state/control/evidence boundary。
<!-- existing:SF-2026-ARXIV-2605-00155:end -->
<!-- delta:SF-2026-ARXIV-2605-00155:start -->
本 family 只收紧机制证据或适用边界，不产生新的长期命题；保留为受限 evidence case。
<!-- delta:SF-2026-ARXIV-2605-00155:end -->
演进关系 `Principle Reuse`；决定 `No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-00155:end -->

<!-- books-review:SF-2026-ARXIV-2605-00161:start -->
<!-- existing:SF-2026-ARXIV-2605-00161:start -->
已核对 `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L1` 与 `books/part-02-model/18-decoder-only.md#L1; books/part-05-inference-system/48-speculative-decoding.md#L1`；现有正文已拥有该 state/control/evidence boundary。
<!-- existing:SF-2026-ARXIV-2605-00161:end -->
<!-- delta:SF-2026-ARXIV-2605-00161:start -->
本 family 只收紧机制证据或适用边界，不产生新的长期命题；保留为受限 evidence case。
<!-- delta:SF-2026-ARXIV-2605-00161:end -->
演进关系 `Alternative Branch`；决定 `No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-00161:end -->

<!-- books-review:SF-2026-ARXIV-2605-00180:start -->
<!-- existing:SF-2026-ARXIV-2605-00180:start -->
已核对 `books/part-05-inference-system/56-inference-scheduling.md#L35` 与 `books/part-05-inference-system/52-distributed-inference.md#L1; books/part-06-ai-infrastructure/63-resource-scheduling.md#L1`；现有正文已拥有该 state/control/evidence boundary。
<!-- existing:SF-2026-ARXIV-2605-00180:end -->
<!-- delta:SF-2026-ARXIV-2605-00180:start -->
本 family 只收紧机制证据或适用边界，不产生新的长期命题；保留为受限 evidence case。
<!-- delta:SF-2026-ARXIV-2605-00180:end -->
演进关系 `Direct Evolution`；决定 `No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-00180:end -->

<!-- books-review:SF-2026-ARXIV-2605-00206:start -->
<!-- existing:SF-2026-ARXIV-2605-00206:start -->
已核对 `books/part-02-model/18-decoder-only.md#L1` 与 `books/part-02-model/15-attention.md#L1; books/part-04-training-system/36-distributed-training.md#L1`；现有正文已拥有该 state/control/evidence boundary。
<!-- existing:SF-2026-ARXIV-2605-00206:end -->
<!-- delta:SF-2026-ARXIV-2605-00206:start -->
本 family 只收紧机制证据或适用边界，不产生新的长期命题；保留为受限 evidence case。
<!-- delta:SF-2026-ARXIV-2605-00206:end -->
演进关系 `Alternative Branch`；决定 `No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-00206:end -->

<!-- books-review:SF-2026-ARXIV-2605-00226:start -->
<!-- existing:SF-2026-ARXIV-2605-00226:start -->
已核对 `books/part-07-agent/79-planning.md#L1` 与 `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1; books/part-06-ai-infrastructure/66-evaluation-system.md#L1`；现有正文已拥有该 state/control/evidence boundary。
<!-- existing:SF-2026-ARXIV-2605-00226:end -->
<!-- delta:SF-2026-ARXIV-2605-00226:start -->
本 family 只收紧机制证据或适用边界，不产生新的长期命题；保留为受限 evidence case。
<!-- delta:SF-2026-ARXIV-2605-00226:end -->
演进关系 `Explanatory Analogy`；决定 `No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-00226:end -->

<!-- books-review:SF-2026-ARXIV-2605-00254:start -->
<!-- existing:SF-2026-ARXIV-2605-00254:start -->
Ch52/Ch56 已拥有 distributed inference 的 placement、network tier、hotspot 与 scheduling state。
<!-- existing:SF-2026-ARXIV-2605-00254:end -->
<!-- delta:SF-2026-ARXIV-2605-00254:start -->
尚未把 MoE expert placement、token skew、all-to-all bytes、topology cost 与 reconfiguration/failure domain 联合为一个 serving decision。
<!-- delta:SF-2026-ARXIV-2605-00254:end -->
演进关系 `Direct Evolution`；决定 `Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-00254:end -->

<!-- books-review:SF-2026-ARXIV-2605-00267:start -->
<!-- existing:SF-2026-ARXIV-2605-00267:start -->
已核对 `books/part-06-ai-infrastructure/72-security.md#L14` 与 `books/part-06-ai-infrastructure/66-evaluation-system.md#L18; books/part-07-agent/84-agent-platform.md#L74`；现有正文已拥有该 state/control/evidence boundary。
<!-- existing:SF-2026-ARXIV-2605-00267:end -->
<!-- delta:SF-2026-ARXIV-2605-00267:start -->
本 family 只收紧机制证据或适用边界，不产生新的长期命题；保留为受限 evidence case。
<!-- delta:SF-2026-ARXIV-2605-00267:end -->
演进关系 `Explanatory Analogy`；决定 `No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-00267:end -->

<!-- books-review:SF-2026-ARXIV-2605-00300:start -->
<!-- existing:SF-2026-ARXIV-2605-00300:start -->
Ch66 已要求 benchmark 冻结 workload、evaluator、版本与 evidence；Ch69 拥有成本维度。
<!-- existing:SF-2026-ARXIV-2605-00300:end -->
<!-- delta:SF-2026-ARXIV-2605-00300:start -->
尚未把 endpoint/model configuration 定义为版本化原子对象，并在同一连续 contract 记录能耗、质量、延迟、价格与可靠性。
<!-- delta:SF-2026-ARXIV-2605-00300:end -->
演进关系 `Direct Evolution`；决定 `Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-00300:end -->

<!-- books-review:SF-2026-ARXIV-2605-00314:start -->
<!-- existing:SF-2026-ARXIV-2605-00314:start -->
Ch72 已拥有 tool/skill 的 artifact、capability、data-flow 与 runtime-effect 审计边界。
<!-- existing:SF-2026-ARXIV-2605-00314:end -->
<!-- delta:SF-2026-ARXIV-2605-00314:start -->
尚未说明如何由自然语言和代码合成有限 SDL fact base，再由 Datalog 约束检查 source-to-sink、permission 与 effect。
<!-- delta:SF-2026-ARXIV-2605-00314:end -->
演进关系 `Layering / Dependency`；决定 `Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-00314:end -->

<!-- books-review:SF-AEM-AGENTIC-RL-ENTROPY-CREDIT:start -->
<!-- existing:SF-AEM-AGENTIC-RL-ENTROPY-CREDIT:start -->已核对 `books/part-04-training-system/33-grpo.md` 与相邻章节：Ch33 已有 entropy controller、hard outcome gate 与 exploration trade-off；response-level modulation 属实验性 credit 分支。<!-- existing:SF-AEM-AGENTIC-RL-ENTROPY-CREDIT:end --> <!-- delta:SF-AEM-AGENTIC-RL-ENTROPY-CREDIT:start -->exact-v1 新增 delta 是“Multi-turn agentic RL can use response-level entropy dynamics as an intrinsic credit and exploration-control signal without a separate process reward model.”。<!-- delta:SF-AEM-AGENTIC-RL-ENTROPY-CREDIT:end --> 当前决定为 `No Change — Existing Coverage`；不创建重复正文，只保留 evidence boundary。
<!-- books-review:SF-AEM-AGENTIC-RL-ENTROPY-CREDIT:end -->

<!-- books-review:SF-AFFORDANCE-HARNESS-VERIFICATION-GATED-SKILLS:start -->
<!-- existing:SF-AFFORDANCE-HARNESS-VERIFICATION-GATED-SKILLS:start -->已核对 `books/part-07-agent/84-agent-platform.md` 与相邻章节：Ch84 已要求 verifier-owned skill admission、capability envelope、failure recovery；affordance confidence 不能直接授权行动。<!-- existing:SF-AFFORDANCE-HARNESS-VERIFICATION-GATED-SKILLS:end --> <!-- delta:SF-AFFORDANCE-HARNESS-VERIFICATION-GATED-SKILLS:start -->exact-v1 新增 delta 是“Skill orchestration needs verifier-owned admission and failure recovery; perceptual affordance confidence cannot directly authorize action.”。<!-- delta:SF-AFFORDANCE-HARNESS-VERIFICATION-GATED-SKILLS:end --> 当前决定为 `No Change — Existing Coverage`；不创建重复正文，只保留 evidence boundary。
<!-- books-review:SF-AFFORDANCE-HARNESS-VERIFICATION-GATED-SKILLS:end -->

<!-- books-review:SF-AGENT-CAPSULES-QUALITY-GATED-GRANULARITY:start -->
<!-- existing:SF-AGENT-CAPSULES-QUALITY-GATED-GRANULARITY:start -->已核对 `books/part-07-agent/84-agent-platform.md` 与相邻章节：Ch84 已把 model/tool/skill/runtime profile、质量证据和预算组成可版本化 dispatch policy；capsule granularity 是其实现分支。<!-- existing:SF-AGENT-CAPSULES-QUALITY-GATED-GRANULARITY:end --> <!-- delta:SF-AGENT-CAPSULES-QUALITY-GATED-GRANULARITY:start -->exact-v1 新增 delta 是“Agent dispatch granularity is a runtime decision gated by measured workload quality, not a static pipeline property.”。<!-- delta:SF-AGENT-CAPSULES-QUALITY-GATED-GRANULARITY:end --> 当前决定为 `No Change — Existing Coverage`；不创建重复正文，只保留 evidence boundary。
<!-- books-review:SF-AGENT-CAPSULES-QUALITY-GATED-GRANULARITY:end -->

<!-- books-review:SF-AGOQ-ACTIVATION-GRADIENT-QUANTIZATION:start -->
<!-- existing:SF-AGOQ-ACTIVATION-GRADIENT-QUANTIZATION:start -->已核对 `books/part-04-training-system/36-distributed-training.md` 与相邻章节：Ch36–41 已把 activation/gradient precision、layer/stage policy 与 collective communication 联合，AGoQ 是精度策略实例。<!-- existing:SF-AGOQ-ACTIVATION-GRADIENT-QUANTIZATION:end --> <!-- delta:SF-AGOQ-ACTIVATION-GRADIENT-QUANTIZATION:start -->exact-v1 新增 delta 是“Activation bit width and gradient communication precision become layer/stage-aware training-runtime policies.”。<!-- delta:SF-AGOQ-ACTIVATION-GRADIENT-QUANTIZATION:end --> 当前决定为 `No Change — Existing Coverage`；不创建重复正文，只保留 evidence boundary。
<!-- books-review:SF-AGOQ-ACTIVATION-GRADIENT-QUANTIZATION:end -->

<!-- books-review:SF-AUTOMAT-CLAIM-REPRODUCTION-CONTRACT:start -->
<!-- existing:SF-AUTOMAT-CLAIM-REPRODUCTION-CONTRACT:start -->已核对 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节：Ch66 已把 executable reproduction、toolchain、claim-evidence adjudication 和 environment identity 作为 evaluation contract。<!-- existing:SF-AUTOMAT-CLAIM-REPRODUCTION-CONTRACT:end --> <!-- delta:SF-AUTOMAT-CLAIM-REPRODUCTION-CONTRACT:start -->exact-v1 新增 delta 是“Coding-agent evaluation must include procedure recovery, toolchain execution and claim-evidence adjudication, not code-generation success alone.”。<!-- delta:SF-AUTOMAT-CLAIM-REPRODUCTION-CONTRACT:end --> 当前决定为 `No Change — Existing Coverage`；不创建重复正文，只保留 evidence boundary。
<!-- books-review:SF-AUTOMAT-CLAIM-REPRODUCTION-CONTRACT:end -->

<!-- books-review:SF-BREW-WATERMARK-DESIGNATED-VERIFICATION:start -->
<!-- existing:SF-BREW-WATERMARK-DESIGNATED-VERIFICATION:start -->已核对 `books/part-06-ai-infrastructure/72-security.md` 与相邻章节：Ch72 已把 watermark 限定为 sensor，并要求 FPR/FNR、metadata/signature/attestation 分层；designated codeword 是 bounded implementation。<!-- existing:SF-BREW-WATERMARK-DESIGNATED-VERIFICATION:end --> <!-- delta:SF-BREW-WATERMARK-DESIGNATED-VERIFICATION:start -->exact-v1 新增 delta 是“Multi-bit watermark extraction and provenance detection are different contracts; designated-codeword verification makes false-positive control explicit.”。<!-- delta:SF-BREW-WATERMARK-DESIGNATED-VERIFICATION:end --> 当前决定为 `No Change — Existing Coverage`；不创建重复正文，只保留 evidence boundary。
<!-- books-review:SF-BREW-WATERMARK-DESIGNATED-VERIFICATION:end -->

<!-- books-review:SF-CLEANBASE-RAG-DOCUMENT-GRAPH:start -->
<!-- existing:SF-CLEANBASE-RAG-DOCUMENT-GRAPH:start -->已核对 `books/part-07-agent/76-rag.md` 与相邻章节：Ch76 已有 RAG ingestion provenance/poison sensor；similarity clique 不能提升为 trust proof，维持 bounded sensor。<!-- existing:SF-CLEANBASE-RAG-DOCUMENT-GRAPH:end --> <!-- delta:SF-CLEANBASE-RAG-DOCUMENT-GRAPH:start -->exact-v1 新增 delta 是“RAG ingestion needs document-level security evidence; similarity-clique detection is one bounded sensor rather than a trust proof.”。<!-- delta:SF-CLEANBASE-RAG-DOCUMENT-GRAPH:end --> 当前决定为 `No Change — Existing Coverage`；不创建重复正文，只保留 evidence boundary。
<!-- books-review:SF-CLEANBASE-RAG-DOCUMENT-GRAPH:end -->

<!-- books-review:SF-EVICT-MOE-VERIFICATION-UTILITY:start -->
<!-- existing:SF-EVICT-MOE-VERIFICATION-UTILITY:start -->已核对 `books/part-05-inference-system/48-speculative-decoding.md` 与相邻章节：Ch48 已把 acceptance、verify length、expert union/residency/transfer 与 workload contract 联合；EVICT 是该主线的 MoE 实例。<!-- existing:SF-EVICT-MOE-VERIFICATION-UTILITY:end --> <!-- delta:SF-EVICT-MOE-VERIFICATION-UTILITY:start -->exact-v1 新增 delta 是“MoE speculative verification is scheduled by accepted-token utility against the union-of-experts verification cost.”。<!-- delta:SF-EVICT-MOE-VERIFICATION-UTILITY:end --> 当前决定为 `No Change — Existing Coverage`；不创建重复正文，只保留 evidence boundary。
<!-- books-review:SF-EVICT-MOE-VERIFICATION-UTILITY:end -->

<!-- books-review:SF-EVOLVING-MEMORY-TWO-STAGE-OPTIMIZATION:start -->
<!-- existing:SF-EVOLVING-MEMORY-TWO-STAGE-OPTIMIZATION:start -->已核对 `books/part-07-agent/77-memory.md` 与相邻章节：Ch77 已分离 memory activation/write/update/use policy，并要求 raw trajectory、version、rollback 与 held-out evaluation。<!-- existing:SF-EVOLVING-MEMORY-TWO-STAGE-OPTIMIZATION:end --> <!-- delta:SF-EVOLVING-MEMORY-TWO-STAGE-OPTIMIZATION:start -->exact-v1 新增 delta 是“Long-term memory needs separately optimized write/update behavior and answer-time use; static hand-written memory update rules are not a durable policy.”。<!-- delta:SF-EVOLVING-MEMORY-TWO-STAGE-OPTIMIZATION:end --> 当前决定为 `No Change — Existing Coverage`；不创建重复正文，只保留 evidence boundary。
<!-- books-review:SF-EVOLVING-MEMORY-TWO-STAGE-OPTIMIZATION:end -->

<!-- books-review:SF-FORWARD-REPLAY-MODEL-EDIT-TARGETS:start -->
<!-- existing:SF-FORWARD-REPLAY-MODEL-EDIT-TARGETS:start -->已核对 `books/part-06-ai-infrastructure/59-model-registry.md` 与相邻章节：现 ROADMAP 没有 parameter/model editing lifecycle owner；不得塞入 Training 或 Memory 章节，等待结构复核。<!-- existing:SF-FORWARD-REPLAY-MODEL-EDIT-TARGETS:end --> <!-- delta:SF-FORWARD-REPLAY-MODEL-EDIT-TARGETS:start -->exact-v1 新增 delta 是“exact-v1 §§4–5 证明 backward spreading 把 final-layer residual 线性分配到早层时隐含 Jacobian eigenvector/正定条件；forward replay 改由首个编辑层的 anchor 沿真实 downstream dynamics 生成兼容 target。该机制把 parameter edit 从局部优化技巧提升为跨层 state-transition 与 compatibility contract；现有知识树没有稳定的 model-edit lifecycle owner，进入 Structural Candidate。”。<!-- delta:SF-FORWARD-REPLAY-MODEL-EDIT-TARGETS:end --> 当前决定为 `Structural Candidate`；现有节点只作相邻定位，不把 parameter editing 强塞入该章，等待季度结构复核。
<!-- books-review:SF-FORWARD-REPLAY-MODEL-EDIT-TARGETS:end -->

<!-- books-review:SF-IEFF-CONTINUOUS-FEATURE-FADING:start -->
<!-- existing:SF-IEFF-CONTINUOUS-FEATURE-FADING:start -->已逐章核对 `books/part-06-ai-infrastructure/73-production-best-practice.md` 的“Progressive Delivery；Feedback 必须回到生命周期”：现章已把上线写成 readiness、渐进交付、反馈和 rollback 的生命周期；缺少的是连续 schema 迁移与 SuperBatch crash-recovery 如何成为可版本化控制状态。<!-- existing:SF-IEFF-CONTINUOUS-FEATURE-FADING:end --> <!-- delta:SF-IEFF-CONTINUOUS-FEATURE-FADING:start -->exact-v1 新增 delta 是“Serving-time reversible feature fading lets recurring training absorb a bounded distribution shift without a rollout-specific retrain.”。<!-- delta:SF-IEFF-CONTINUOUS-FEATURE-FADING:end --> 相邻章节 `books/part-06-ai-infrastructure/72-security.md`、`books/part-07-agent/74-prompt.md` 只保留 handoff。正文写回位于 `books/part-06-ai-infrastructure/73-production-best-practice.md#L91-L107`，并由 `post-write-audit-v1:SF-IEFF-CONTINUOUS-FEATURE-FADING` 验证；状态为 integrated/post-write-passed。
<!-- books-review:SF-IEFF-CONTINUOUS-FEATURE-FADING:end -->

<!-- books-review:SF-LIGHTKV-PROMPT-GUIDED-VISION-KV:start -->
<!-- existing:SF-LIGHTKV-PROMPT-GUIDED-VISION-KV:start -->已核对 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 与相邻章节：Ch45 已覆盖 token/modality/position identity 与 KV compression 的 workload/quality boundary；LightKV 是视觉分支。<!-- existing:SF-LIGHTKV-PROMPT-GUIDED-VISION-KV:end --> <!-- delta:SF-LIGHTKV-PROMPT-GUIDED-VISION-KV:start -->exact-v1 新增 delta 是“Vision-token KV compression is prompt-conditioned and must preserve modality/token/position identity; the mechanism is a bounded implementation case.”。<!-- delta:SF-LIGHTKV-PROMPT-GUIDED-VISION-KV:end --> 当前决定为 `No Change — Existing Coverage`；不创建重复正文，只保留 evidence boundary。
<!-- books-review:SF-LIGHTKV-PROMPT-GUIDED-VISION-KV:end -->

<!-- books-review:SF-LLM-EMU-NATIVE-RUNTIME-EMULATION:start -->
<!-- existing:SF-LLM-EMU-NATIVE-RUNTIME-EMULATION:start -->已核对 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节：Ch66 已要求真实 runtime path、scheduler/KV identity、trace replay 与 calibrated simulator boundary；LLM-Emu 是受限实现。<!-- existing:SF-LLM-EMU-NATIVE-RUNTIME-EMULATION:end --> <!-- delta:SF-LLM-EMU-NATIVE-RUNTIME-EMULATION:start -->exact-v1 新增 delta 是“A serving emulator preserves the real HTTP, scheduler, KV and output paths while replacing only GPU execution with profiled samples.”。<!-- delta:SF-LLM-EMU-NATIVE-RUNTIME-EMULATION:end --> 当前决定为 `No Change — Existing Coverage`；不创建重复正文，只保留 evidence boundary。
<!-- books-review:SF-LLM-EMU-NATIVE-RUNTIME-EMULATION:end -->

<!-- books-review:SF-LWD-FLEET-OFFLINE-ONLINE-ROBOT-RL:start -->
<!-- existing:SF-LWD-FLEET-OFFLINE-ONLINE-ROBOT-RL:start -->已逐章核对 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 的“闭环主干；State ownership 与 freshness；数据演进”：现章已建立 perception-action-environment feedback、状态 freshness 与 sim-to-real 边界；缺少 fleet deployment/intervention/offline-online/redeployment 的版本化学习循环。<!-- existing:SF-LWD-FLEET-OFFLINE-ONLINE-ROBOT-RL:end --> <!-- delta:SF-LWD-FLEET-OFFLINE-ONLINE-ROBOT-RL:start -->exact-v1 新增 delta 是“Deployment, intervention capture, offline-to-online value learning and redeployment form a versioned embodied-learning loop.”。<!-- delta:SF-LWD-FLEET-OFFLINE-ONLINE-ROBOT-RL:end --> 相邻章节 `books/part-03-multimodal-world-models/25-multimodal-world-models.md`、`books/part-04-training-system/27-data.md` 只保留 handoff。正文写回位于 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L255-L270`，并由 `post-write-audit-v1:SF-LWD-FLEET-OFFLINE-ONLINE-ROBOT-RL` 验证；状态为 integrated/post-write-passed。
<!-- books-review:SF-LWD-FLEET-OFFLINE-ONLINE-ROBOT-RL:end -->

<!-- books-review:SF-MATHARENA-LIVING-EVALUATION:start -->
<!-- existing:SF-MATHARENA-LIVING-EVALUATION:start -->已核对 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节：Ch66 已建立 living evaluation、task/version identity、contamination control 与 release gate；MathArena 是领域实例。<!-- existing:SF-MATHARENA-LIVING-EVALUATION:end --> <!-- delta:SF-MATHARENA-LIVING-EVALUATION:start -->exact-v1 新增 delta 是“Evaluation for fast-moving capabilities needs continuously refreshed, contamination-resistant tasks with versioned scoring rather than a static benchmark snapshot.”。<!-- delta:SF-MATHARENA-LIVING-EVALUATION:end --> 当前决定为 `No Change — Existing Coverage`；不创建重复正文，只保留 evidence boundary。
<!-- books-review:SF-MATHARENA-LIVING-EVALUATION:end -->

<!-- books-review:SF-MEMROUTER-WRITE-ADMISSION:start -->
<!-- existing:SF-MEMROUTER-WRITE-ADMISSION:start -->已核对 `books/part-07-agent/77-memory.md` 与相邻章节：Ch77 已把 Memory Write 定义为独立高风险 admission，分离 writer/verifier/reader authority 并要求 rollback receipt。<!-- existing:SF-MEMROUTER-WRITE-ADMISSION:end --> <!-- delta:SF-MEMROUTER-WRITE-ADMISSION:start -->exact-v1 新增 delta 是“Memory write admission becomes an independently trained, measurable control plane rather than generation-time narration.”。<!-- delta:SF-MEMROUTER-WRITE-ADMISSION:end --> 当前决定为 `No Change — Existing Coverage`；不创建重复正文，只保留 evidence boundary。
<!-- books-review:SF-MEMROUTER-WRITE-ADMISSION:end -->

<!-- books-review:SF-PERSEUS-MEGAKERNEL-SIGNAL-ORDERING:start -->
<!-- existing:SF-PERSEUS-MEGAKERNEL-SIGNAL-ORDERING:start -->已逐章核对 `books/part-05-inference-system/49-tensorrt-llm.md` 的“从计算图到执行选择；TMA；FlashAttention；Build-time 与 Runtime-time”：现章已建立执行计划、kernel、搬运和量化边界；缺少异步 attention 仿真、跨节点 megakernel signaling、exit-aligned pretraining 与 MLIR semantic verification 四类 admission evidence。<!-- existing:SF-PERSEUS-MEGAKERNEL-SIGNAL-ORDERING:end --> <!-- delta:SF-PERSEUS-MEGAKERNEL-SIGNAL-ORDERING:start -->exact-v1 新增 delta 是“Fine-grained MoE overlap fails across nodes when per-transfer fences serialize the NIC; signaling and ordering ownership must be separated.”。<!-- delta:SF-PERSEUS-MEGAKERNEL-SIGNAL-ORDERING:end --> 相邻章节 `books/part-05-inference-system/48-speculative-decoding.md`、`books/part-05-inference-system/50-vllm.md` 只保留 handoff。正文写回位于 `books/part-05-inference-system/49-tensorrt-llm.md#L60-L72`，并由 `post-write-audit-v1:SF-PERSEUS-MEGAKERNEL-SIGNAL-ORDERING` 验证；状态为 integrated/post-write-passed。
<!-- books-review:SF-PERSEUS-MEGAKERNEL-SIGNAL-ORDERING:end -->

<!-- books-review:SF-PROMPT-SCORE-VARIANCE-RELIABILITY:start -->
<!-- existing:SF-PROMPT-SCORE-VARIANCE-RELIABILITY:start -->已核对 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节：Ch66 已要求 prompt distribution、重复采样、相关性、校准与 evaluation identity；单一 first-token score 不得冒充稳定置信度已被明确覆盖。<!-- existing:SF-PROMPT-SCORE-VARIANCE-RELIABILITY:end --> <!-- delta:SF-PROMPT-SCORE-VARIANCE-RELIABILITY:start -->exact-v1 新增 delta 是“A deployable safety score must be tested across semantically equivalent prompts; one first-token probability is not a stable confidence contract.”。<!-- delta:SF-PROMPT-SCORE-VARIANCE-RELIABILITY:end --> 当前决定为 `No Change — Existing Coverage`；不创建重复正文，只保留 evidence boundary。
<!-- books-review:SF-PROMPT-SCORE-VARIANCE-RELIABILITY:end -->

<!-- books-review:SF-RUNAGENT-CONSTRAINT-GUIDED-EXECUTION:start -->
<!-- existing:SF-RUNAGENT-CONSTRAINT-GUIDED-EXECUTION:start -->已核对 `books/part-07-agent/81-workflow.md` 与相邻章节：Ch81 已把 natural-language plan 编译成 typed DAG/state machine，具有 precondition、transition、recovery 与 commit owner。<!-- existing:SF-RUNAGENT-CONSTRAINT-GUIDED-EXECUTION:end --> <!-- delta:SF-RUNAGENT-CONSTRAINT-GUIDED-EXECUTION:start -->exact-v1 新增 delta 是“Natural-language plans need an executable intermediate representation with step constraints, rubrics and recovery transitions.”。<!-- delta:SF-RUNAGENT-CONSTRAINT-GUIDED-EXECUTION:end --> 当前决定为 `No Change — Existing Coverage`；不创建重复正文，只保留 evidence boundary。
<!-- books-review:SF-RUNAGENT-CONSTRAINT-GUIDED-EXECUTION:end -->

<!-- books-review:SF-SAGA-WORKFLOW-ATOMIC-SCHEDULING:start -->
<!-- existing:SF-SAGA-WORKFLOW-ATOMIC-SCHEDULING:start -->已核对 `books/part-05-inference-system/56-inference-scheduling.md` 与相邻章节：Ch56 已把 workflow DAG、tool gap、session affinity、KV residency 与 fairness 作为调度状态；request 不再是唯一单位。<!-- existing:SF-SAGA-WORKFLOW-ATOMIC-SCHEDULING:end --> <!-- delta:SF-SAGA-WORKFLOW-ATOMIC-SCHEDULING:start -->exact-v1 新增 delta 是“Agent workflow, not isolated request, becomes the scheduling/fairness/cache-lifetime unit.”。<!-- delta:SF-SAGA-WORKFLOW-ATOMIC-SCHEDULING:end --> 当前决定为 `No Change — Existing Coverage`；不创建重复正文，只保留 evidence boundary。
<!-- books-review:SF-SAGA-WORKFLOW-ATOMIC-SCHEDULING:end -->

<!-- books-review:SF-SIMFA-ASYNC-GPU-SIMULATION:start -->
<!-- existing:SF-SIMFA-ASYNC-GPU-SIMULATION:start -->已核对 `books/part-05-inference-system/49-tensorrt-llm.md` 与相邻章节：Ch49 已承载 TMA、barrier、warp specialization、cache traffic 与 execution evidence；SimFA 是评估该执行合同的模拟器。<!-- existing:SF-SIMFA-ASYNC-GPU-SIMULATION:end --> <!-- delta:SF-SIMFA-ASYNC-GPU-SIMULATION:start -->exact-v1 新增 delta 是“GPU performance evidence for asynchronous attention pipelines must model TMA, barriers, warp specialization and cache traffic rather than rely on a coarse roofline alone.”。<!-- delta:SF-SIMFA-ASYNC-GPU-SIMULATION:end --> 当前决定为 `No Change — Existing Coverage`；不创建重复正文，只保留 evidence boundary。
<!-- books-review:SF-SIMFA-ASYNC-GPU-SIMULATION:end -->

<!-- books-review:SF-SKILL-VERIFIABLE-ARTIFACT:start -->
<!-- existing:SF-SKILL-VERIFIABLE-ARTIFACT:start -->已核对 `books/part-06-ai-infrastructure/72-security.md` 与相邻章节：Ch72/Ch84 已把 skill 视为 untrusted executable artifact，以签名 provenance、admission、capability 与 human approval 分级。<!-- existing:SF-SKILL-VERIFIABLE-ARTIFACT:end --> <!-- delta:SF-SKILL-VERIFIABLE-ARTIFACT:start -->exact-v1 新增 delta 是“Agent skills are untrusted executable artifacts whose verification level must gate capabilities and human approval.”。<!-- delta:SF-SKILL-VERIFIABLE-ARTIFACT:end --> 当前决定为 `No Change — Existing Coverage`；不创建重复正文，只保留 evidence boundary。
<!-- books-review:SF-SKILL-VERIFIABLE-ARTIFACT:end -->

<!-- books-review:SF-TOOL-CALL-UTILITY-GATE:start -->
<!-- existing:SF-TOOL-CALL-UTILITY-GATE:start -->已逐章核对 `books/part-07-agent/78-tool-calling.md` 的“模型输出只是 Proposal；Side-effect Class 决定控制”：现章已把 tool call 视为 proposal 并由 side-effect contract 控制；缺少 benefit/latency/failure cost 共同决定是否调用的 utility admission。<!-- existing:SF-TOOL-CALL-UTILITY-GATE:end --> <!-- delta:SF-TOOL-CALL-UTILITY-GATE:start -->exact-v1 新增 delta 是“Tool invocation is an admission decision whose benefit, latency and failure cost must be estimated; availability alone does not justify a call.”。<!-- delta:SF-TOOL-CALL-UTILITY-GATE:end --> 相邻章节 `books/part-07-agent/77-memory.md`、`books/part-07-agent/79-planning.md` 只保留 handoff。正文写回位于 `books/part-07-agent/78-tool-calling.md#L115-L125`，并由 `post-write-audit-v1:SF-TOOL-CALL-UTILITY-GATE` 验证；状态为 integrated/post-write-passed。
<!-- books-review:SF-TOOL-CALL-UTILITY-GATE:end -->

<!-- books-review:SF-UCPO-CORRECT-SOLUTION-DIVERSITY:start -->
<!-- existing:SF-UCPO-CORRECT-SOLUTION-DIVERSITY:start -->已核对 `books/part-04-training-system/33-grpo.md` 与相邻章节：Ch33 已明确 verified-correct trajectories 内的 mode diversity 和 conditional-uniformity pressure；UCPO 不再改变 owner。<!-- existing:SF-UCPO-CORRECT-SOLUTION-DIVERSITY:end --> <!-- delta:SF-UCPO-CORRECT-SOLUTION-DIVERSITY:start -->exact-v1 新增 delta 是“RLVR objectives can be indifferent among correct modes; a conditional uniformity term makes diversity an explicit optimization contract.”。<!-- delta:SF-UCPO-CORRECT-SOLUTION-DIVERSITY:end --> 当前决定为 `No Change — Existing Coverage`；不创建重复正文，只保留 evidence boundary。
<!-- books-review:SF-UCPO-CORRECT-SOLUTION-DIVERSITY:end -->

<!-- books-review:SF-VLM-VISUAL-JAILBREAK-CROSS-MODAL-GAP:start -->
<!-- existing:SF-VLM-VISUAL-JAILBREAK-CROSS-MODAL-GAP:start -->已核对 `books/part-06-ai-infrastructure/72-security.md` 与相邻章节：Ch72 已明确 visual channel 是 intent-bearing attack surface，并要求跨模态 threat model、sensor 与 safe commit 分离。<!-- existing:SF-VLM-VISUAL-JAILBREAK-CROSS-MODAL-GAP:end --> <!-- delta:SF-VLM-VISUAL-JAILBREAK-CROSS-MODAL-GAP:start -->exact-v1 新增 delta 是“Safety post-training and threat models must treat the visual channel as an active intent-bearing attack surface rather than assume text-domain alignment composes across modalities.”。<!-- delta:SF-VLM-VISUAL-JAILBREAK-CROSS-MODAL-GAP:end --> 当前决定为 `No Change — Existing Coverage`；不创建重复正文，只保留 evidence boundary。
<!-- books-review:SF-VLM-VISUAL-JAILBREAK-CROSS-MODAL-GAP:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260504-COVERAGE | fresh-context:owner-replay-20260903 | coverage | coverage:SRC-ARXIV:20260504 | none | raw/retained/closure/withdrawn conservation and initial-created owner mapping independently recounted | passed |
| SA-20260504-EVIDENCE | fresh-context:owner-replay-20260903 | evidence | validator:review-completion-v1 | none | every frozen family has a completed exact-version receipt; blocked=0 | passed |
| SA-20260504-SELECTION | fresh-context:owner-replay-20260903 | deep_analysis_selection | validator:deep-analysis-selection-v1 | none | eligible=35；selected=3；all others retain completed reviews | passed |
| SA-20260504-BOOKS | fresh-context:apr-may-books-20260903 | books | validator:books-comparison-v1 | none | — | passed |

## 8. Ignored Noise

- Pre-denominator closures=350；逐 family 理由保存在 owner receipt。
- Withdrawn=0；只保留审计 closure，不进入候选、评分、Review 或 Books。
- `updated` / current OAI datestamp 的 revision 噪声不拥有 Daily。

## 9. Recommended Action

本日全部 Gate 已闭合，无进一步动作。

## 10. Repository Changes

- Owner receipt（本阶段只读）：`papers/2026/05/_sources/arxiv-owner-replay-20260903/20260504/arxiv-owner-receipt.json`
- Canonical ledger（Books terminal state）：`papers/2026/05/_sources/arxiv-owner-replay-20260903/20260504/canonical-ledger.json`
- Books queue（fresh-context decision）：`papers/2026/05/_sources/arxiv-owner-replay-20260903/BOOKS_WRITEBACK_QUEUE.json`
- Superseded report：`papers/2026/05/_sources/arxiv-owner-replay-20260903/legacy-reports-before-created-owner-reconciliation/2026-05-04.md`
- Books body: no change for the recovered families on this date.

## 11. Open Questions

- 无。

## 12. Sources

- [DataCite REST API](https://api.datacite.org/dois) — initial `created` owner-day proxy；`updated` 只作 revision provenance。
- [arXiv OAI](https://export.arxiv.org/oai2) — identity/date corroboration；current datestamp 不拥有 first-public day。
- [arXiv](https://arxiv.org/) — exact-v1 abstract、HTML/PDF 与 version history。

## 13. Final Status

Completion Status: Complete; Coverage: Closed; Evidence: Passed; Books: Passed; unresolved findings=0
