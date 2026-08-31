# Daily Research — 2026-06-02

**Research Date:** 2026-06-02

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-06-01 09:00:00 ～ 2026-06-02 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；19 个注册 category Atom snapshot 负责 identity/date recall，机制与 benchmark claim 只绑定 exact arXiv v1 HTML/PDF

**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed，fresh-context Semantic Audit 无未解决 finding

## Executive Summary

736 条 raw identity 已按官方 arXiv first-submission metadata 全量复核；identifier 前缀与序号不承担日期语义，736 条均由官方 `published` 时间确认属于本窗口。fresh-context denominator audit 将旧 52 项收紧为 28 项（3.80%）：31 个旧候选进入具名 pre-denominator closure，7 个原 closure 在全量 false-negative audit 中恢复。相对 V2 Strict，`AsymCache` 是唯一新增 false negative，0 个既有 retain 被撤销。fresh evidence audit 已完成 28/28 项 exact-v1 Review，普通 pending=0、blocked=0；其中 `2606.09864v1` 与 `2606.28343v1` 通过官方 exact-v1 PDF 恢复，不再保留 Materials Request。Books Comparison 的 19 项 Integrate 已完成串行写回；独立 post-write audit 复核了 22/22 旧 marker、5/5 新 integration、28 retained 与 708 closures，并在 14 条 retained/revised marker 的 exact-v1 Review notes 补齐后关闭唯一 finding。Coverage Gate 已 Closed，Evidence 与 Books Gate 已 Passed，Completion 已闭合。

<!-- audit-target:coverage:start -->
## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-06-02 |
| Window End | 2026-06-02 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | DEN-20260602-V3-FRESH |
| Denominator Frozen At | 2026-08-28T18:30:00+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-06-01T09:00:00+08:00 | 2026-06-02T09:00:00+08:00 | 2026-08-28T18:30:00+08:00 | 19 category Atom snapshots; official published metadata; 736/736 fresh full-population title+abstract reconciliation | checked | 736 | SF-KV-QUANT-ALIGNMENT-COLLAPSE;SF-SKILL-INJECTION-GUARDIAN;SF-ROBOTRUSTBENCH-WORLD-MODEL;SF-EXECUTION-GROUNDED-CODING-AGENT-SECURITY;SF-OPTCC-ASYMMETRIC-ALLREDUCE;SF-GAIATRACE-VIDUR-AGENT;SF-SPARSEX-SEGMENT-KV;SF-ADAPTIVE-AUTO-HARNESS;SF-CONSERVE-CONVERSATION-PLACEMENT;SF-COMPRESSION-UNCERTAINTY;SF-ASYNC-INFERENCE-OVERHEADS;SF-DRIFT-TELBENCH;SF-CONSENT-INTEGRITY;SF-DFLARE-DIFFUSION-SPECULATION;SF-STRAGGLER-AWARE-RL-GROUP;SF-SECLAW-SPEC-DRIVEN-SECURITY;SF-HARNESS1-EXTERNALIZED-STATE;SF-LLMFI-ERROR-PROPAGATION;SF-PEFT-SCALE;SF-GHOST-TOOL-ISSUE-PRIVACY;SF-SKILLHARM-LIFECYCLE;SF-COSMOS3-OMNIMODAL;SF-CROWDED-EMBEDDING-EXTERNALITY;SF-ECHELON-AGGREGATE-ONLY-ADAPTATION;SF-GATEAI-OPERATING-POINT-EVAL;SF-KFORGE-CROSS-PLATFORM-KERNEL;SF-ASYMCACHE-MULTI-SEGMENT;SF-DRIFTSCHED-TOKEN-DRIFT | pages=19; final_cursor=end; unique=736; identity=736; semantic_screen=736; retained=28; closure=708 | 2026-06-02T00:59:39Z | coverage:SRC-ARXIV:20260602-v3-fresh | — |

<!-- coverage:SRC-ARXIV:20260602-v3-fresh:start -->`identity-provenance-v2-strict.json` 保存 736/736 official submission metadata 与 DOI provenance；`screening-ledger-v3-fresh.tsv` 保存 fresh audit 的每一项 retain 或 family-specific closure，并绑定 hash。高序号、`2607` 或 `2608` identifier 均未被用作日期推断。<!-- coverage:SRC-ARXIV:20260602-v3-fresh:end -->

### Coverage Limitations

官方 Atom `published` 字段证明 first submission time；snapshot 的 observed version 可能晚于 v1，因此只承担 identity/recall，不承担候选机制 claim。28 项 retained claim 均已绑定 exact-v1 HTML/PDF；`2606.09864v1` 当前 metadata 已出现后续版本，因此机制与实验只引用官方 v1 PDF。`2606.28343v1` 也以官方 v1 PDF 复核。arXiv 仍是作者稿，不等于 peer review 或生产复现；未披露的 immutable artifact commit、线上并发与生产 SLO 不由作者 benchmark 反推。Required Daily 其他来源的 Effective Date 晚于本历史窗口，不追溯为到期源。
<!-- audit-target:coverage:end -->

<!-- audit-target:evidence:start -->
## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-KV-QUANT-ALIGNMENT-COLLAPSE | arXiv:2606.09864v1 | paper-v1:2606.09864 | 2026-W23 | 2026-06-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-KV-QUANT-ALIGNMENT-COLLAPSE | self | — | new_in_window | INFER-KV-CACHE | Integrate | books-review:SF-KV-QUANT-ALIGNMENT-COLLAPSE | yes |
| SF-SKILL-INJECTION-GUARDIAN | arXiv:2606.01567v1 | paper-v1:2606.01567 | 2026-W23 | 2026-06-01 | SRC-ARXIV | 2 | 3 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-SKILL-INJECTION-GUARDIAN | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-SKILL-INJECTION-GUARDIAN | yes |
| SF-ROBOTRUSTBENCH-WORLD-MODEL | arXiv:2606.01600v1 | paper-v1:2606.01600 | 2026-W23 | 2026-06-01 | SRC-ARXIV | 2 | 3 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-ROBOTRUSTBENCH-WORLD-MODEL | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-ROBOTRUSTBENCH-WORLD-MODEL | yes |
| SF-EXECUTION-GROUNDED-CODING-AGENT-SECURITY | arXiv:2607.22569v1 | paper-v1:2607.22569 | 2026-W23 | 2026-06-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-EXECUTION-GROUNDED-CODING-AGENT-SECURITY | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-EXECUTION-GROUNDED-CODING-AGENT-SECURITY | yes |
| SF-OPTCC-ASYMMETRIC-ALLREDUCE | arXiv:2606.01680v1 | paper-v1:2606.01680 | 2026-W23 | 2026-06-01 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-OPTCC-ASYMMETRIC-ALLREDUCE | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Integrate | books-review:SF-OPTCC-ASYMMETRIC-ALLREDUCE | yes |
| SF-GAIATRACE-VIDUR-AGENT | arXiv:2606.01725v1 | paper-v1:2606.01725 | 2026-W23 | 2026-06-01 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-GAIATRACE-VIDUR-AGENT | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-GAIATRACE-VIDUR-AGENT | yes |
| SF-SPARSEX-SEGMENT-KV | arXiv:2606.01751v1 | paper-v1:2606.01751 | 2026-W23 | 2026-06-01 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-SPARSEX-SEGMENT-KV | self | — | new_in_window | INFER-KV-CACHE | Integrate | books-review:SF-SPARSEX-SEGMENT-KV | yes |
| SF-ADAPTIVE-AUTO-HARNESS | arXiv:2606.01770v1 | paper-v1:2606.01770 | 2026-W23 | 2026-06-01 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-ADAPTIVE-AUTO-HARNESS | self | — | new_in_window | AGENT-PLATFORM | Integrate | books-review:SF-ADAPTIVE-AUTO-HARNESS | yes |
| SF-CONSERVE-CONVERSATION-PLACEMENT | arXiv:2606.01839v1 | paper-v1:2606.01839 | 2026-W23 | 2026-06-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-CONSERVE-CONVERSATION-PLACEMENT | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-CONSERVE-CONVERSATION-PLACEMENT | yes |
| SF-COMPRESSION-UNCERTAINTY | arXiv:2606.01850v1 | paper-v1:2606.01850 | 2026-W23 | 2026-06-01 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-COMPRESSION-UNCERTAINTY | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-COMPRESSION-UNCERTAINTY | yes |
| SF-ASYNC-INFERENCE-OVERHEADS | arXiv:2606.01927v1 | paper-v1:2606.01927 | 2026-W23 | 2026-06-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-ASYNC-INFERENCE-OVERHEADS | self | — | new_in_window | INFER-REQUEST-LIFECYCLE | Integrate | books-review:SF-ASYNC-INFERENCE-OVERHEADS | yes |
| SF-DRIFT-TELBENCH | arXiv:2606.02060v1 | paper-v1:2606.02060 | 2026-W23 | 2026-06-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-DRIFT-TELBENCH | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-DRIFT-TELBENCH | yes |
| SF-CONSENT-INTEGRITY | arXiv:2606.02668v1 | paper-v1:2606.02668 | 2026-W23 | 2026-06-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-CONSENT-INTEGRITY | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-CONSENT-INTEGRITY | yes |
| SF-DFLARE-DIFFUSION-SPECULATION | arXiv:2606.02091v1 | paper-v1:2606.02091 | 2026-W23 | 2026-06-01 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-DFLARE-DIFFUSION-SPECULATION | self | — | new_in_window | INFER-SPECULATIVE-DECODING | Integrate | books-review:SF-DFLARE-DIFFUSION-SPECULATION | yes |
| SF-STRAGGLER-AWARE-RL-GROUP | arXiv:2606.02218v1 | paper-v1:2606.02218 | 2026-W23 | 2026-06-01 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-STRAGGLER-AWARE-RL-GROUP | self | — | new_in_window | TRAIN-GRPO | Integrate | books-review:SF-STRAGGLER-AWARE-RL-GROUP | yes |
| SF-SECLAW-SPEC-DRIVEN-SECURITY | arXiv:2606.02302v1 | paper-v1:2606.02302 | 2026-W23 | 2026-06-01 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-SECLAW-SPEC-DRIVEN-SECURITY | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-SECLAW-SPEC-DRIVEN-SECURITY | yes |
| SF-HARNESS1-EXTERNALIZED-STATE | arXiv:2606.02373v1 | paper-v1:2606.02373 | 2026-W23 | 2026-06-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-HARNESS1-EXTERNALIZED-STATE | self | — | new_in_window | AGENT-CONTEXT | No Change — Existing Coverage | books-review:SF-HARNESS1-EXTERNALIZED-STATE | yes |
| SF-LLMFI-ERROR-PROPAGATION | arXiv:2606.02430v1 | paper-v1:2606.02430 | 2026-W23 | 2026-06-01 | SRC-ARXIV | 2 | 3 | 2 | 7 | retained | deep_complete | accessible | knowledge_gap | review:SF-LLMFI-ERROR-PROPAGATION | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-LLMFI-ERROR-PROPAGATION | yes |
| SF-PEFT-SCALE | arXiv:2606.02437v1 | paper-v1:2606.02437 | 2026-W23 | 2026-06-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-PEFT-SCALE | self | — | new_in_window | PLATFORM-MODEL-REGISTRY | No Change — Existing Coverage | books-review:SF-PEFT-SCALE | yes |
| SF-GHOST-TOOL-ISSUE-PRIVACY | arXiv:2606.02483v1 | paper-v1:2606.02483 | 2026-W23 | 2026-06-01 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-GHOST-TOOL-ISSUE-PRIVACY | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-GHOST-TOOL-ISSUE-PRIVACY | yes |
| SF-SKILLHARM-LIFECYCLE | arXiv:2606.02540v1 | paper-v1:2606.02540 | 2026-W23 | 2026-06-01 | SRC-ARXIV | 2 | 3 | 2 | 7 | retained | deep_complete | accessible | knowledge_gap | review:SF-SKILLHARM-LIFECYCLE | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-SKILLHARM-LIFECYCLE | yes |
| SF-COSMOS3-OMNIMODAL | arXiv:2606.02800v1 | paper-v1:2606.02800 | 2026-W23 | 2026-06-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-COSMOS3-OMNIMODAL | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-COSMOS3-OMNIMODAL | yes |
| SF-CROWDED-EMBEDDING-EXTERNALITY | arXiv:2606.28343v1 | paper-v1:2606.28343 | 2026-W23 | 2026-06-01 | SRC-ARXIV | 2 | 3 | 2 | 7 | retained | deep_complete | accessible | knowledge_gap | review:SF-CROWDED-EMBEDDING-EXTERNALITY | self | — | new_in_window | AGENT-RAG | Integrate | books-review:SF-CROWDED-EMBEDDING-EXTERNALITY | yes |
| SF-ECHELON-AGGREGATE-ONLY-ADAPTATION | arXiv:2606.02958v1 | paper-v1:2606.02958 | 2026-W23 | 2026-06-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-ECHELON-AGGREGATE-ONLY-ADAPTATION | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Integrate | books-review:SF-ECHELON-AGGREGATE-ONLY-ADAPTATION | yes |
| SF-GATEAI-OPERATING-POINT-EVAL | arXiv:2606.02959v1 | paper-v1:2606.02959 | 2026-W23 | 2026-06-01 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-GATEAI-OPERATING-POINT-EVAL | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-GATEAI-OPERATING-POINT-EVAL | yes |
| SF-KFORGE-CROSS-PLATFORM-KERNEL | arXiv:2606.02963v1 | paper-v1:2606.02963 | 2026-W23 | 2026-06-01 | SRC-ARXIV | 2 | 3 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-KFORGE-CROSS-PLATFORM-KERNEL | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-KFORGE-CROSS-PLATFORM-KERNEL | yes |
| SF-ASYMCACHE-MULTI-SEGMENT | arXiv:2606.02964v1 | paper-v1:2606.02964 | 2026-W23 | 2026-06-01 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-ASYMCACHE-MULTI-SEGMENT | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-ASYMCACHE-MULTI-SEGMENT | yes |
| SF-DRIFTSCHED-TOKEN-DRIFT | arXiv:2606.02982v1 | paper-v1:2606.02982 | 2026-W23 | 2026-06-01 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-DRIFTSCHED-TOKEN-DRIFT | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-DRIFTSCHED-TOKEN-DRIFT | yes |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-KV-QUANT-ALIGNMENT-COLLAPSE | RP-cfe9ad50ebb2e8cd | deep | arXiv:2606.09864v1 | SRC-ARXIV@arXiv:2606.09864v1 | arXiv:2606.09864v1 §3 ConditionalFlip/PCR diagnostic, layer spread and four-step protocol | arXiv:2606.09864v1 §§4–5 plus Apps. A.6–A.10 and B.14–B.15; 11 models, 1,894 prompts, real-dtype and vLLM FP8 checks | arXiv:2606.09864v1 §6 and Appendix H; refusal evaluator, prompt sets, model families, quantizers and deployment scope | arXiv:2606.09864v1 Code repository is linked in exact-v1; immutable event-time commit Not Disclosed | claim:SF-KV-QUANT-ALIGNMENT-COLLAPSE | complete |
| SF-SKILL-INJECTION-GUARDIAN | RP-e6d640757b981b3c | deep | arXiv:2606.01567v1 | SRC-ARXIV@arXiv:2606.01567v1 | arXiv:2606.01567v1 §3 Extended Threat Evaluation; §3.1 Guardian Defense Subagent | arXiv:2606.01567v1 §4 Experimental Setup and Results | arXiv:2606.01567v1 §6 Limitations; §7 Ethics Statement | Not Disclosed — no immutable event-time code artifact identified | claim:SF-SKILL-INJECTION-GUARDIAN | complete |
| SF-ROBOTRUSTBENCH-WORLD-MODEL | RP-6780643eab2e3987 | deep | arXiv:2606.01600v1 | SRC-ARXIV@arXiv:2606.01600v1 | arXiv:2606.01600v1 §3 Benchmark Construction; §4 Evaluation | arXiv:2606.01600v1 §5 Experiment; §5.1 Evaluated Video World Models; §5.2 Overall Evaluation Results; §5.4 Analysis of Trustworthiness Failures | arXiv:2606.01600v1 §Limitations (unnumbered exact heading); §Ethical Considerations | arXiv:2606.01600v1 Appendices B–D generation/evaluation protocols; no immutable dataset revision disclosed | claim:SF-ROBOTRUSTBENCH-WORLD-MODEL | complete |
| SF-EXECUTION-GROUNDED-CODING-AGENT-SECURITY | RP-741f86c04d40e238 | deep | arXiv:2607.22569v1 | SRC-ARXIV@arXiv:2607.22569v1 | arXiv:2607.22569v1 §3 execution-grounded red-team workload and oracle | arXiv:2607.22569v1 §§4–5 multi-agent/model execution results | arXiv:2607.22569v1 §6 limitations | arXiv:2607.22569v1 Controlled Docker sandbox; immutable artifact revision Not Disclosed | claim:SF-EXECUTION-GROUNDED-CODING-AGENT-SECURITY | complete |
| SF-OPTCC-ASYMMETRIC-ALLREDUCE | RP-70ba76259b0ae84f | deep | arXiv:2606.01680v1 | SRC-ARXIV@arXiv:2606.01680v1 | arXiv:2606.01680v1 §3 Theoretical Lower Bounds; §4 Algorithm Design | arXiv:2606.01680v1 §5 Evaluation; Appendix A Summary of Optimality Results | arXiv:2606.01680v1 §4.4 Extensions; §6 Conclusion | Not Disclosed — no immutable implementation revision in manuscript | claim:SF-OPTCC-ASYMMETRIC-ALLREDUCE | complete |
| SF-GAIATRACE-VIDUR-AGENT | RP-652030197e76a627 | deep | arXiv:2606.01725v1 | SRC-ARXIV@arXiv:2606.01725v1 | arXiv:2606.01725v1 §§3.1–3.3 GAIATrace collection and Vidur-Agent simulator | arXiv:2606.01725v1 §§4–5 trace characterization and system simulation | arXiv:2606.01725v1 §3.2 trace-collection scope and §5 simulation setup; no dedicated limitations section in exact-v1; two systems/GAIA and simulator-model boundary | arXiv:2606.01725v1 Artifact promised upon publication; immutable event-time revision Not Disclosed | claim:SF-GAIATRACE-VIDUR-AGENT | complete |
| SF-SPARSEX-SEGMENT-KV | RP-4252ad979632454c | deep | arXiv:2606.01751v1 | SRC-ARXIV@arXiv:2606.01751v1 | arXiv:2606.01751v1 §3 Algorithm; §4 System Design | arXiv:2606.01751v1 §5 Evaluation | arXiv:2606.01751v1 §1.2 Limitations of Existing Methods; §5 workload/evaluation boundaries; no dedicated limitations section | Not Disclosed — event-time immutable engine patch not identified | claim:SF-SPARSEX-SEGMENT-KV | complete |
| SF-ADAPTIVE-AUTO-HARNESS | RP-28b7d8f0942cc428 | deep | arXiv:2606.01770v1 | SRC-ARXIV@arXiv:2606.01770v1 | arXiv:2606.01770v1 §3 Method; §3.3 Stateful Multi-Agent Evolution; §3.4 Harness-Tree Routing; §3.5 Human Steering | arXiv:2606.01770v1 §4 Experiments; §§4.4–4.6 component analyses | arXiv:2606.01770v1 §6 Limitations; Appendices B–J | Not Disclosed — paper-linked release path; exact event-time commit not pinned | claim:SF-ADAPTIVE-AUTO-HARNESS | complete |
| SF-CONSERVE-CONVERSATION-PLACEMENT | RP-63c848131b2f6f47 | deep | arXiv:2606.01839v1 | SRC-ARXIV@arXiv:2606.01839v1 | arXiv:2606.01839v1 §3 Characterization of Agentic Workloads; §4 ConServe | arXiv:2606.01839v1 §5 Evaluation; §5.1 Experiment Setup | arXiv:2606.01839v1 §6 Related Work; §7 Conclusion; no dedicated limitations section | Not Disclosed — vLLM/LMCache implementation described, but no immutable event-time commit identified | claim:SF-CONSERVE-CONVERSATION-PLACEMENT | complete |
| SF-COMPRESSION-UNCERTAINTY | RP-55cd63f624b2f4b2 | deep | arXiv:2606.01850v1 | SRC-ARXIV@arXiv:2606.01850v1 | arXiv:2606.01850v1 §3 Background; §4 Benchmark Design | arXiv:2606.01850v1 §5 Experiments and Analysis; §§5.1–5.6 | arXiv:2606.01850v1 §5.7 Discussion; §6 Conclusion; no dedicated limitations section | Not Disclosed — Appendix A prompting and score breakdown; immutable benchmark artifact not pinned | claim:SF-COMPRESSION-UNCERTAINTY | complete |
| SF-ASYNC-INFERENCE-OVERHEADS | RP-cc449a94bb863137 | deep | arXiv:2606.01927v1 | SRC-ARXIV@arXiv:2606.01927v1 | arXiv:2606.01927v1 §3 Design Overview; §§4–7 scheduling, I/O, sampling and implementation | arXiv:2606.01927v1 §8 Evaluation; §8.1 Experimental Setup | arXiv:2606.01927v1 §9 Limitations and Future Work | arXiv:2606.01927v1 §7 Implementation; Appendix A Parallel Output Processing; no immutable commit identified | claim:SF-ASYNC-INFERENCE-OVERHEADS | complete |
| SF-DRIFT-TELBENCH | RP-919675209f979db3 | deep | arXiv:2606.02060v1 | SRC-ARXIV@arXiv:2606.02060v1 | arXiv:2606.02060v1 §3 Dataset; §4 DRIFT | arXiv:2606.02060v1 §5 Experiment; §6 Further Analysis | arXiv:2606.02060v1 §5.1 Experiment Settings; §7 Conclusion; no dedicated limitations section | Not Disclosed — benchmark release/version not used as claim evidence | claim:SF-DRIFT-TELBENCH | complete |
| SF-CONSENT-INTEGRITY | RP-d592ea55f12d0e22 | deep | arXiv:2606.02668v1 | SRC-ARXIV@arXiv:2606.02668v1 | arXiv:2606.02668v1 §III Threat Model; §IV Property; §§V–VIII design, analysis and implementation | arXiv:2606.02668v1 §IX Evaluation; §IX.B Threats to Validity | arXiv:2606.02668v1 §X Limitations and Future Work | Not Disclosed — prototype described in §VIII; total mediation/trusted path assumed, not implemented | claim:SF-CONSENT-INTEGRITY | complete |
| SF-DFLARE-DIFFUSION-SPECULATION | RP-41f6022cb6788dde | deep | arXiv:2606.02091v1 | SRC-ARXIV@arXiv:2606.02091v1 | arXiv:2606.02091v1 §4 Method | arXiv:2606.02091v1 §5 Experiments; §5.1 Setup; §6 Analysis | arXiv:2606.02091v1 Limitations; §7 Conclusion | arXiv:2606.02091v1 Appendix A.1 Training Implementation; A.3 Compute Resources; A.5 Ablation Results | claim:SF-DFLARE-DIFFUSION-SPECULATION | complete |
| SF-STRAGGLER-AWARE-RL-GROUP | RP-5134573456d2afec | deep | arXiv:2606.02218v1 | SRC-ARXIV@arXiv:2606.02218v1 | arXiv:2606.02218v1 §3 Motivation; §4 Methodology; §4.4 Controller Implementation and System Design | arXiv:2606.02218v1 §5 Experiments; §5.1 Experimental Settings; §5.6 Posterior Risk Analysis | arXiv:2606.02218v1 Limitations; §6 Conclusion | arXiv:2606.02218v1 Appendix C Implementation Details; Appendix D Controller Hyperparameters | claim:SF-STRAGGLER-AWARE-RL-GROUP | complete |
| SF-SECLAW-SPEC-DRIVEN-SECURITY | RP-a28c0109ea05defe | standard | arXiv:2606.02302v1 | SRC-ARXIV@arXiv:2606.02302v1 | arXiv:2606.02302v1 §3.2 spec-driven task synthesis; §3.3 Docker execution and trajectory logging | arXiv:2606.02302v1 §4 Further Exploration only; cross-model and cross-harness evaluation is proposed, not reported | arXiv:2606.02302v1 Title marks preliminary/in-progress work; no dedicated limitations section in exact-v1; generated-task and environment representativeness remain untested | arXiv:2606.02302v1 Repository is linked, but immutable event-time commit is Not Disclosed | claim:SF-SECLAW-SPEC-DRIVEN-SECURITY | complete |
| SF-HARNESS1-EXTERNALIZED-STATE | RP-76309dac5b6ca759 | deep | arXiv:2606.02373v1 | SRC-ARXIV@arXiv:2606.02373v1 | arXiv:2606.02373v1 §2 Harness-1; §2.1 Policy actions; §2.2 Derived-state rendering | arXiv:2606.02373v1 §3 Experiments | arXiv:2606.02373v1 Appendix B Limitations, Ethics, and Broader Impact | Not Disclosed — immutable runnable harness revision not used | claim:SF-HARNESS1-EXTERNALIZED-STATE | complete |
| SF-LLMFI-ERROR-PROPAGATION | RP-17a32d7a6957455f | deep | arXiv:2606.02430v1 | SRC-ARXIV@arXiv:2606.02430v1 | arXiv:2606.02430v1 §3 LLMFI: Large Language Model Fault Injector; §4 LLM Resilience Analysis with LLMFI | arXiv:2606.02430v1 §4.1 Evaluation Setups; §4.2 Evaluation Approach; §5 Error Propagation Analysis with LLMFI | arXiv:2606.02430v1 §6 Implications for Error Mitigation; §7 Conclusion and Future Works; no dedicated limitations section | Not Disclosed — LLMFI implementation described, but no immutable event-time revision identified | claim:SF-LLMFI-ERROR-PROPAGATION | complete |
| SF-PEFT-SCALE | RP-72cd5ccc7832b890 | deep | arXiv:2606.02437v1 | SRC-ARXIV@arXiv:2606.02437v1 | arXiv:2606.02437v1 §2 Three Scaling Axes; §3 Scale Up; §4 Scale Down; §5 Scale Out; §6 Infrastructure | arXiv:2606.02437v1 §3.3 operational evidence; §4.1 adapter-regime evidence; §5.1 personal-policy evidence; no unified evaluation section | arXiv:2606.02437v1 §3.4 Scale-Induced Failure Modes; §6.4–6.5 mobility/residency boundaries; no dedicated limitations section | Not Disclosed — MinT is related infrastructure, not immutable paper artifact | claim:SF-PEFT-SCALE | complete |
| SF-GHOST-TOOL-ISSUE-PRIVACY | RP-3ede06631dfd20b9 | deep | arXiv:2606.02483v1 | SRC-ARXIV@arXiv:2606.02483v1 | arXiv:2606.02483v1 §3 Ghost Calls and the Privacy Boundary; §4 Speculative Tool Privacy Contracts | arXiv:2606.02483v1 §5 Evaluation; Appendix B Evaluation Tables | arXiv:2606.02483v1 §7 Conclusion; §Limitations (unnumbered exact heading) | arXiv:2606.02483v1 Appendix A Contract Mechanism Details; Appendix D Reproducibility and Artifact Manifest | claim:SF-GHOST-TOOL-ISSUE-PRIVACY | complete |
| SF-SKILLHARM-LIFECYCLE | RP-a4b6d3d4fa586b83 | deep | arXiv:2606.02540v1 | SRC-ARXIV@arXiv:2606.02540v1 | arXiv:2606.02540v1 §3 Threat Model; §4 Automated Construction; lifecycle attack scenarios | arXiv:2606.02540v1 §5 Experiments; §5.3 Further Analysis; Appendix E defense analysis | arXiv:2606.02540v1 §6 Conclusion; no dedicated limitations section | Not Disclosed — benchmark construction details in Appendices B–D; immutable dataset revision not pinned | claim:SF-SKILLHARM-LIFECYCLE | complete |
| SF-COSMOS3-OMNIMODAL | RP-cb2599c40ae0d149 | deep | arXiv:2606.02800v1 | SRC-ARXIV@arXiv:2606.02800v1 | arXiv:2606.02800v1 §2 Model Architecture; §3 Data; §4 Training | arXiv:2606.02800v1 §6 Results; §6.1 Reasoner Evaluation; §6.2 Generator Evaluation | arXiv:2606.02800v1 §3–4 data/training disclosure boundaries; §6.3 Generator User Guide; no dedicated limitations section in v1 | Not Disclosed — current repository/model artifacts not used as event-time mechanism evidence | claim:SF-COSMOS3-OMNIMODAL | complete |
| SF-CROWDED-EMBEDDING-EXTERNALITY | RP-48a1cf68a714cadb | deep | arXiv:2606.28343v1 | SRC-ARXIV@arXiv:2606.28343v1 | arXiv:2606.28343v1 §§2–3 static crowding model and McKean–Vlasov/Wasserstein mean-field dynamics | arXiv:2606.28343v1 §§4–5 finite simulations, phase-transition checks and practical retrieval illustration; Appendix D HNSW/hubness discussion | arXiv:2606.28343v1 §6 Limitations: one-to-one relevance, thermodynamic-limit dynamics, finite-system transfer and mitigation remain unverified | arXiv:2606.28343v1 Appendices contain proofs and update-rule derivations; implementation artifact and immutable revision Not Disclosed | claim:SF-CROWDED-EMBEDDING-EXTERNALITY | complete |
| SF-ECHELON-AGGREGATE-ONLY-ADAPTATION | RP-642bfb15591eff05 | deep | arXiv:2606.02958v1 | SRC-ARXIV@arXiv:2606.02958v1 | arXiv:2606.02958v1 §§3–5 information-flow contract and three execution planes | arXiv:2606.02958v1 §§7–8 budget-matched/WAN/privacy audit | arXiv:2606.02958v1 §4 threat scope; §9 limitations | arXiv:2606.02958v1 §10 reproducibility; immutable event-time revision Not Disclosed | claim:SF-ECHELON-AGGREGATE-ONLY-ADAPTATION | complete |
| SF-GATEAI-OPERATING-POINT-EVAL | RP-e0427c8d232638bd | deep | arXiv:2606.02959v1 | SRC-ARXIV@arXiv:2606.02959v1 | arXiv:2606.02959v1 §2.1–2.12 trace identity, grouped CV, threshold and calibration | arXiv:2606.02959v1 §§3–5 corpus, results and latency | arXiv:2606.02959v1 §§2.13–2.14 limitations and contamination | arXiv:2606.02959v1 JSONL checkpoints described; immutable repository revision Not Disclosed | claim:SF-GATEAI-OPERATING-POINT-EVAL | complete |
| SF-KFORGE-CROSS-PLATFORM-KERNEL | RP-f79ea22641064f59 | deep | arXiv:2606.02963v1 | SRC-ARXIV@arXiv:2606.02963v1 | arXiv:2606.02963v1 §III Synthesis, Performance Analysis and Verification Agents | arXiv:2606.02963v1 §IV Case Studies; §IV.A Microbenchmark and End-to-End Evaluation | arXiv:2606.02963v1 §V Limitations and Future Work; §VI Conclusion | Not Disclosed — generated kernels are described, but no immutable event-time artifact revision identified | claim:SF-KFORGE-CROSS-PLATFORM-KERNEL | complete |
| SF-ASYMCACHE-MULTI-SEGMENT | RP-060a65caa47c2863 | deep | arXiv:2606.02964v1 | SRC-ARXIV@arXiv:2606.02964v1 | arXiv:2606.02964v1 §3 Observation and Motivation; §4 Asymmetric Cache Block Manager; §5 AsymCache Runtime | arXiv:2606.02964v1 §6 Evaluation; §6.1 Experimental Setup; §6.5 Integration with Agentic System | arXiv:2606.02964v1 §7 Discussion and Related Works; §8 Conclusion; no dedicated limitations section | arXiv:2606.02964v1 §5.3 Implementation; no immutable code revision identified | claim:SF-ASYMCACHE-MULTI-SEGMENT | complete |
| SF-DRIFTSCHED-TOKEN-DRIFT | RP-45c82b3be1b640db | deep | arXiv:2606.02982v1 | SRC-ARXIV@arXiv:2606.02982v1 | arXiv:2606.02982v1 §II Methodology and System Architecture | arXiv:2606.02982v1 §III Experimental Setup; §IV Results and Analysis | arXiv:2606.02982v1 §IV.E Tail Latency; §IV.I GPU Utilization; §V Conclusion; no dedicated limitations section | arXiv:2606.02982v1 §III.C Hardware and Software Environment; no immutable scheduler revision identified | claim:SF-DRIFTSCHED-TOKEN-DRIFT | complete |

### Source Reviews

<!-- review:SF-KV-QUANT-ALIGNMENT-COLLAPSE:start -->
### KV Quantization Alignment Collapse

KV quantization 通常只以 perplexity、task accuracy 与 memory 验收，但 refusal behavior 依赖低维 activation subspace，可能在这些 aggregate metric 几乎不变时发生 model-specific phase transition。论文用 ConditionalFlip、layer scan、per-channel reduction 与 layer spread 诊断 mitigation；证据覆盖 11 个 3.8B–72B 模型、五个 safety benchmarks 和生产 vLLM FP8 case，但仍受 refusal evaluator、prompt set、量化器与 post-training family 约束。结论是压缩 artifact 必须重新做行为/安全 release evaluation，而不是存在统一 safe bit-width。 <!-- claim:SF-KV-QUANT-ALIGNMENT-COLLAPSE:start -->证据边界绑定 exact-v1 与上述 workload；不得把作者结果外推成跨模型/跨部署普遍结论。<!-- claim:SF-KV-QUANT-ALIGNMENT-COLLAPSE:end -->
<!-- review:SF-KV-QUANT-ALIGNMENT-COLLAPSE:end -->
<!-- review:SF-SKILL-INJECTION-GUARDIAN:start -->
### Skill Injection Guardian

Skill 文档既是操作知识又是未信任输入。static guardian 在发布前重写，dynamic guardian 在读取时中介；两者降低所测三类 agent 的攻击成功率，却新增 guardian 自身的模型错误、重写语义漂移与运行成本。reframing 仍能改变攻击效果，说明“过滤一次”不是信任证明。<!-- claim:SF-SKILL-INJECTION-GUARDIAN:start -->可证明的是 Skill 必须经过 provenance、capability 与 runtime mediation；不能证明 guardian 单点足以替代 sandbox、least privilege 和 effect-level authorization。
<!-- claim:SF-SKILL-INJECTION-GUARDIAN:end -->
<!-- review:SF-SKILL-INJECTION-GUARDIAN:end -->
<!-- review:SF-ROBOTRUSTBENCH-WORLD-MODEL:start -->
### RoboTrustBench

只在可行、安全指令上评价生成视频，容易把视觉连贯误当作 world-model trust。该 benchmark 从真实 DROID 初态构造 normal、constraint-sensitive、counterfactual、adversarial 四类 instruction-image pair，并把 entity、时空、interaction、instruction 与 safety 拆成 13 项 human/MLLM criteria。<!-- claim:SF-ROBOTRUSTBENCH-WORLD-MODEL:start -->它支持“world-model evaluation 必须加入不可行与危险条件并区分视觉质量和物理/安全判断”；所有评估仍是离线生成视频，没有在真实机器人执行，也不能把 judge agreement 升级为 action-conditioned causal correctness。
<!-- claim:SF-ROBOTRUSTBENCH-WORLD-MODEL:end -->
<!-- review:SF-ROBOTRUSTBENCH-WORLD-MODEL:end -->
<!-- review:SF-EXECUTION-GROUNDED-CODING-AGENT-SECURITY:start -->
### Execution-Grounded Coding-Agent Security

语言层 refusal 无法证明 coding agent 没有修改文件、startup hook 或运行环境。论文把危险操作包装进测试、调试与 crash reproduction workload，并用 tool trace、runtime output 与 filesystem diff 的 execution oracle 判定实际副作用。它证明所测 agent/framework 在任务伪装下存在显著 execution gap；Docker sandbox、RedCode-derived goal pool 与预定义 predicate 会漏掉 partial harm，不能外推为生产风险率。长期结论是安全 Gate 的 truth owner 必须是 effect evidence，而不是回复文本。 <!-- claim:SF-EXECUTION-GROUNDED-CODING-AGENT-SECURITY:start -->证据边界绑定 exact-v1 与上述 workload；不得把作者结果外推成跨模型/跨部署普遍结论。<!-- claim:SF-EXECUTION-GROUNDED-CODING-AGENT-SECURITY:end -->
<!-- review:SF-EXECUTION-GROUNDED-CODING-AGENT-SECURITY:end -->
<!-- review:SF-OPTCC-ASYMMETRIC-ALLREDUCE:start -->
### OptCC

标准 ring 在某一 server NIC 降速后让所有 rank 受最慢 hop 约束。论文先给非对称带宽下界，再以四阶段 schedule 重排 reduce、scatter、allgather 与局部转发，使健康路径不必全程等待退化路径。<!-- claim:SF-OPTCC-ASYMMETRIC-ALLREDUCE:start -->证据支持“collective algorithm 必须消费当前 topology/bandwidth state”这一机制；它不证明无额外 buffer、控制开销或多故障下仍保持同样收益。旧 ring 在对称网络、故障直接 fail-stop 或恢复时间短时仍更简单。
<!-- claim:SF-OPTCC-ASYMMETRIC-ALLREDUCE:end -->
<!-- review:SF-OPTCC-ASYMMETRIC-ALLREDUCE:end -->
<!-- review:SF-GAIATRACE-VIDUR-AGENT:start -->
### GAIATrace / Vidur-Agent

传统 serving trace 以单 query 为单位，无法表达 agent task 内的依赖、tool latency 与多模型阶段。论文将 task/query/tool dependency 外置为可重放 trace，并扩展 simulator 以消费 KV/prefix cache、PD、routing 与 scheduling 配置。它证明所测两套 agent 的 task-level latency 与 TTFT/TPOT 会错位，也证明负载变化会移动瓶颈；没有证明两套 GAIA trace 能代表所有 agent workload，开源 artifact 在 v1 仍是发布承诺。 <!-- claim:SF-GAIATRACE-VIDUR-AGENT:start -->证据边界绑定 exact-v1 与上述 workload；不得把作者结果外推成跨模型/跨部署普遍结论。<!-- claim:SF-GAIATRACE-VIDUR-AGENT:end -->
<!-- review:SF-GAIATRACE-VIDUR-AGENT:end -->
<!-- review:SF-SPARSEX-SEGMENT-KV:start -->
### SparseX

Prefix cache 只复用完全相同的前缀，而真实 RAG/Agent 内容常以非前缀 segment 重现。SparseX 先对 segment 做 RoPE 对齐，再用 Sparse-Q 找需修正 token，在一次 forward 中重算局部 KV。<!-- claim:SF-SPARSEX-SEGMENT-KV:start -->论文证明的是所测模型/长度下 segment reuse 的可行性，不是任意切片均等价；segment identity 仍必须绑定 tokenization、position、model/adapter 与 correction policy，边界依赖或 selector drift 时要回退 dense Prefill。
<!-- claim:SF-SPARSEX-SEGMENT-KV:end -->
<!-- review:SF-SPARSEX-SEGMENT-KV:end -->
<!-- review:SF-ADAPTIVE-AUTO-HARNESS:start -->
### Adaptive Auto-Harness

单一 harness 在固定 benchmark 上反复优化时合理，但 open-ended task stream 会累积 history、domain shift 与 specialization conflict。Adaptive Auto-Harness 把持续 evolution、solve-time harness-tree routing 和 human steering 分成三个控制面，并保存 stateful evolution history。三类流式 benchmark 与 ablation 支持该分工在给定系统中减轻峰值后退化；不能证明自动演化不会 reward-hack，也没有把 human intervention、branch retirement、artifact provenance 与生产 rollback 全部闭合。<!-- claim:SF-ADAPTIVE-AUTO-HARNESS:start -->本报告只保留上述 exact-v1 机制、实验边界与 failure mode，不把作者 benchmark 外推为通用生产结论。<!-- claim:SF-ADAPTIVE-AUTO-HARNESS:end -->
<!-- review:SF-ADAPTIVE-AUTO-HARNESS:end -->
<!-- review:SF-CONSERVE-CONVERSATION-PLACEMENT:start -->
### ConServe

逐 turn 决定 PD placement 必须预测尚不可见的 output length、tool delay 与 KV growth。ConServe 把调度单位提升为 conversation：首轮长 Prefill 交给 prefiller，KV 只迁移一次，随后会话固定到一个 decoder；调度器只读取 first-turn input length 与 decoder KV occupancy。<!-- claim:SF-CONSERVE-CONVERSATION-PLACEMENT:start -->作者在四张 A40、Qwen3-0.6B replay 与 SWE-agent traces 上证明这一 owner change 可减少预测依赖；不证明所有 agent conversation 都有稳定两阶段结构，模型、工具或负载变化时仍需迁移、再平衡与 admission fallback。
<!-- claim:SF-CONSERVE-CONVERSATION-PLACEMENT:end -->
<!-- review:SF-CONSERVE-CONVERSATION-PLACEMENT:end -->
<!-- review:SF-COMPRESSION-UNCERTAINTY:start -->
### Compression Uncertainty

压缩评估通常只比较 accuracy/perplexity，却可能遗漏置信集合扩大与 selective-risk 变化。论文以 conformal prediction 在 12 个 LLM、量化/稀疏配置与五项任务上分离 accuracy 和 uncertainty，观察到规模依赖与阈值式 inflation。它证明 deployment gate 不能由 accuracy 单指标代理；不证明 conformal coverage 在 distribution shift、生成式开放答案或线上 calibration drift 下自动保持，也未给统一 latency/SLO。<!-- claim:SF-COMPRESSION-UNCERTAINTY:start -->本报告只保留上述 exact-v1 机制、实验边界与 failure mode，不把作者 benchmark 外推为通用生产结论。<!-- claim:SF-COMPRESSION-UNCERTAINTY:end -->
<!-- review:SF-COMPRESSION-UNCERTAINTY:end -->
<!-- review:SF-ASYNC-INFERENCE-OVERHEADS:start -->
### Albireo / Non-scalable Inference Overheads

扩大 Tensor Parallel degree 可以释放每卡 KV 空间，却会放大 scheduler、I/O、sampling 等不能随 GPU 数缩短的 host/runtime 比例。Albireo 将 scheduling 与 I/O 和 GPU compute 重叠，并把 sampling 沿 sequence parallel 化，以移动 Amdahl 最优点而不改模型。<!-- claim:SF-ASYNC-INFERENCE-OVERHEADS:start -->证据支持 inference scaling 必须分别计量 model-parallel compute、communication 与 non-scalable control path；作者基准和 production deployment 不能证明任意 runtime/模型都得到相同收益，异步 overlap 还引入 buffer lifetime、ordering、backpressure 与 late-result failure mode。
<!-- claim:SF-ASYNC-INFERENCE-OVERHEADS:end -->
<!-- review:SF-ASYNC-INFERENCE-OVERHEADS:end -->
<!-- review:SF-DRIFT-TELBENCH:start -->
### DRIFT / TELBench

final-answer evaluator 只能看到失败结果，不能定位 trajectory 中第一次有害承诺。TELBench 将 2,790 条轨迹切成 semantic spans，并建立 1,000-instance localization benchmark；DRIFT 再按 claim 跟踪 evidence、support 与传播。<!-- claim:SF-DRIFT-TELBENCH:start -->证据支持 outcome → span → claim propagation 的诊断分层，但 LLM-assisted annotation、framework/backbone mix 与 benchmark construction 不能证明 locator 找到真实因果根因；它是 failure sensor，不是 truth owner。
<!-- claim:SF-DRIFT-TELBENCH:end -->
<!-- review:SF-DRIFT-TELBENCH:end -->
<!-- review:SF-CONSENT-INTEGRITY:start -->
### Consent Integrity

由 agent 自己撰写 approval summary 时，人批准的是可伪造 narration 而非真实 action。Consent Integrity 要求可信 mediator 从 boundary event 解码、渲染并 bind-to-execution；未知 action 必须显示 uninspectable，而不能静默通过。GTFOBins/tldr 结果揭示 trust-list 在 silent pass 与 over-prompting 间的硬 trade-off；原型没有实现 total mediation 与 trusted path，因此是安全属性和 proof-of-concept，不是已完成防御。<!-- claim:SF-CONSENT-INTEGRITY:start -->本报告只保留上述 exact-v1 机制、实验边界与 failure mode，不把作者 benchmark 外推为通用生产结论。<!-- claim:SF-CONSENT-INTEGRITY:end -->
<!-- review:SF-CONSENT-INTEGRITY:end -->
<!-- review:SF-DFLARE-DIFFUSION-SPECULATION:start -->
### DFlare

Block diffusion speculation 同时提议一块 token，旧 draft 让所有 draft layer 共享少数 target-layer 融合表示，形成容量瓶颈。DFlare 让每个 draft layer 学习自己的多 target-layer fusion，并扩大 draft depth 与训练数据，再由 target 并行验证。<!-- claim:SF-DFLARE-DIFFUSION-SPECULATION:start -->六类 benchmark 支持“draft capacity 与 conditioning interface 共同限制 acceptance/speed”这一实验性分支；结果绑定三种 target、训练数据和作者实现，不能外推为 diffusion 解码普遍优于 AR，也不能省略 target verification、rollback 与 distribution/quality contract。
<!-- claim:SF-DFLARE-DIFFUSION-SPECULATION:end -->
<!-- review:SF-DFLARE-DIFFUSION-SPECULATION:end -->
<!-- review:SF-STRAGGLER-AWARE-RL-GROUP:start -->
### Straggler-Aware Group Control

固定 rollout group 保留同步 on-policy 与组内 normalization，但 group 越大，极长 rollout 阻塞 reward/update 的概率越高。SAGC 把 group size 作为在线受约束控制变量，根据 observed rollout behavior 与长期 straggler-rate risk 调整，而不是改成无界 stale async。<!-- claim:SF-STRAGGLER-AWARE-RL-GROUP:start -->GRPO/DAPO 实验支持动态 group 可以在所测训练栈改善 wall-clock 且保持 reward/quality；不能证明 controller 在 workload shift、reward drift 或不同 rollout service 下仍校准。最小固定组在负载稳定、可预测性优先时仍更简单。
<!-- claim:SF-STRAGGLER-AWARE-RL-GROUP:end -->
<!-- review:SF-STRAGGLER-AWARE-RL-GROUP:end -->
<!-- review:SF-SECLAW-SPEC-DRIVEN-SECURITY:start -->
### SeClaw

静态攻击 prompt 与 final-answer judge 看不到 agent 在文件、权限、Skill/MCP 与命令执行中的中间副作用。SeClaw exact-v1 提出用结构化 risk/deployment/tool spec 生成任务，在 Docker 中重建执行环境并记录 trajectory；但稿件标题已明确是 preliminary/in-progress，正文只给出框架与后续评测计划，没有跨模型/跨 harness 的结果或独立 limitations 章节。因此它只能作为现有 security EvalSpec 思路的早期实现案例，不能证明该流程已形成可复现 benchmark，也不构成新的 Books 机制。 <!-- claim:SF-SECLAW-SPEC-DRIVEN-SECURITY:start -->证据边界绑定 exact-v1 与上述 workload；不得把作者结果外推成跨模型/跨部署普遍结论。<!-- claim:SF-SECLAW-SPEC-DRIVEN-SECURITY:end -->
<!-- review:SF-SECLAW-SPEC-DRIVEN-SECURITY:end -->
<!-- review:SF-HARNESS1-EXTERNALIZED-STATE:start -->
### Harness-1

纯 transcript policy 同时承担搜索决策与候选池、证据链接、verification record、压缩摘要等可恢复 bookkeeping。Harness-1 让环境拥有这些状态，policy 通过 edit actions 改写；这缩短 policy 需要隐式记忆的控制面。<!-- claim:SF-HARNESS1-EXTERNALIZED-STATE:start -->实验只证明特定 20B agent、search tasks 与训练配方下的收益；harness state 仍可能 stale、被错误压缩或与网页事实分叉，因此必须 version、provenance、rebuild，并保留 final verification。
<!-- claim:SF-HARNESS1-EXTERNALIZED-STATE:end -->
<!-- review:SF-HARNESS1-EXTERNALIZED-STATE:end -->
<!-- review:SF-LLMFI-ERROR-PROPAGATION:start -->
### LLMFI

只对 final token 或 aggregate accuracy 做 fault test，会掩盖 fault 在 layer、operation、token 与 task 间如何传播。LLMFI 以确定性 fault injection 在三种 open-weight LLM、13 类任务中定位 resilience pattern，并区分检测与软件 mitigation。<!-- claim:SF-LLMFI-ERROR-PROPAGATION:start -->该研究支持 evaluation subject 必须绑定 injection site、bit/error model、model/task 与 observable outcome；模拟 fault 不给出现实发生率，也不证明作者四种 mitigation 覆盖 GPU、network、kernel 与 checkpoint 的真实故障分布。
<!-- claim:SF-LLMFI-ERROR-PROPAGATION:end -->
<!-- review:SF-LLMFI-ERROR-PROPAGATION:end -->
<!-- review:SF-PEFT-SCALE:start -->
### PEFT Scale Up / Down / Out

论文把 adapter 从“便宜微调”重述为共享 base 上的持久局部状态，并区分更强 prior、adapter 最小可靠容量、百万实例治理三轴。<!-- claim:SF-PEFT-SCALE:start -->它支持 adapter identity/revision/provenance/evaluation/residency 必须分层，但不证明每个用户都应持有 adapter，也不能把 population 数量等同同时驻留数量。现有 Model Registry 章节已经拥有该长期合同，故不重复写入。
<!-- claim:SF-PEFT-SCALE:end -->
<!-- review:SF-PEFT-SCALE:end -->
<!-- review:SF-GHOST-TOOL-ISSUE-PRIVACY:start -->
### Ghost Tool Calls

Speculative tool dispatch 即使 read-only、最终放弃，也已把推断出的用户意图交给外部 observer；commit-time cleanup 无法撤回 disclosure。论文把“被观察”从 state mutation 中分离为 issue-time effect，并让 policy 在发送前抑制或投影 argument/destination。<!-- claim:SF-GHOST-TOOL-ISSUE-PRIVACY:start -->三套 corpus、12 种 policy 的原型支持 privacy boundary 必须在 dispatch 前执行；它不证明 prototype 覆盖真实 provider retention、timing side channel 或多工具 workflow。低风险本地 pure function 可继续 speculation，外部 observer 则需 issue-time contract。
<!-- claim:SF-GHOST-TOOL-ISSUE-PRIVACY:end -->
<!-- review:SF-GHOST-TOOL-ISSUE-PRIVACY:end -->
<!-- review:SF-SKILLHARM-LIFECYCLE:start -->
### SkillHarm

一次 session 的 poisoned skill 测试会漏掉 persistent package 被静默改写后在未来复用触发的 harm。SkillHarm 把 fixed-payload 与 self-mutating poisoning 放进 skill lifecycle，并按 data、environment、autonomy 构造 879 个攻击样本。作者结果显示当前 defenses 在该 harness 下仍脆弱；ASR 受 agent 是否读取 poisoned file 影响，未触发不等于抵抗，benchmark 也不能证明所有 skill ecosystem 的真实发生率。<!-- claim:SF-SKILLHARM-LIFECYCLE:start -->本报告只保留上述 exact-v1 机制、实验边界与 failure mode，不把作者 benchmark 外推为通用生产结论。<!-- claim:SF-SKILLHARM-LIFECYCLE:end -->
<!-- review:SF-SKILLHARM-LIFECYCLE:end -->
<!-- review:SF-COSMOS3-OMNIMODAL:start -->
### Cosmos 3

统一 token arrangement 与 mixture-of-transformers 接口可处理 language/image/video/audio/action，但 reasoner 与 generator 仍有不同 data、objective 与 output contract。<!-- claim:SF-COSMOS3-OMNIMODAL:start -->证据支持统一 interface 不等于统一 state owner；作者 benchmark 受模型、数据与 evaluator 限制，不能证明生成视频就是可控 world transition，也不能用 leaderboard 代替 intervention/closed-loop evaluation。
<!-- claim:SF-COSMOS3-OMNIMODAL:end -->
<!-- review:SF-COSMOS3-OMNIMODAL:end -->
<!-- review:SF-CROWDED-EMBEDDING-EXTERNALITY:start -->
### Crowded Embedding Space

逐 query 评测把 retrieval 看作独立调用，但共享 embedding/index 是随 corpus composition 变化的公共状态。论文的 mean-field model 给出多数文档密度增长导致 minority target 从 shortlist 中突变式消失的机制，并指出 HNSW hub routing 可能放大 crowding。理论依赖一对一 relevance、热力学极限与分布假设，mitigation 尚未被充分实证；可沉淀的是 index population/revision 本身属于 evidence contract，而非接受普适阈值。 <!-- claim:SF-CROWDED-EMBEDDING-EXTERNALITY:start -->证据边界绑定 exact-v1 与上述 workload；不得把作者结果外推成跨模型/跨部署普遍结论。<!-- claim:SF-CROWDED-EMBEDDING-EXTERNALITY:end -->
<!-- review:SF-CROWDED-EMBEDDING-EXTERNALITY:end -->
<!-- review:SF-ECHELON-AGGREGATE-ONLY-ADAPTATION:start -->
### Echelon

传统 federated/decentralized training 常把隐私作为算法附加层，而 Echelon 先冻结跨行政边界的信息流：device parameters、activations、optimizer state 与 individual update 不得外流，global plane 只消费 boundary aggregate 与少量控制 metadata。三层执行面、buffered semi-async aggregation 与 drift-aware outer cadence 都服务于该 invariant。实验只覆盖 1B LoRA、短序列、主要两边界和 honest-but-curious threat model；它不提供 differential privacy，也不证明 full-parameter/大规模边界同样稳定。 <!-- claim:SF-ECHELON-AGGREGATE-ONLY-ADAPTATION:start -->证据边界绑定 exact-v1 与上述 workload；不得把作者结果外推成跨模型/跨部署普遍结论。<!-- claim:SF-ECHELON-AGGREGATE-ONLY-ADAPTATION:end -->
<!-- review:SF-ECHELON-AGGREGATE-ONLY-ADAPTATION:end -->
<!-- review:SF-GATEAI-OPERATING-POINT-EVAL:start -->
### Gate AI

安全 detector benchmark 若按数据集单独调 threshold，会把 operating-point 差异伪装成模型能力差异。论文固定 content-hashed trace、group-aware cross-validation、inner-validation threshold、matched-FPR 与 bootstrap CI，并显式标注外部 published numbers。它强化了现有 EvalSpec 的 version/threshold/leakage contract；公开数据污染、跨数据集语义近重复与第三方 baseline 不可比仍限制结论，因此不需要新增 owner。 <!-- claim:SF-GATEAI-OPERATING-POINT-EVAL:start -->证据边界绑定 exact-v1 与上述 workload；不得把作者结果外推成跨模型/跨部署普遍结论。<!-- claim:SF-GATEAI-OPERATING-POINT-EVAL:end -->
<!-- review:SF-GATEAI-OPERATING-POINT-EVAL:end -->
<!-- review:SF-KFORGE-CROSS-PLATFORM-KERNEL:start -->
### KForge

异构 accelerator 让同一算子面对不同 programming model、compiler 与 profiler；一次性 code generation 无法同时保证正确与快。KForge 让 generation agent 消费 compile/correctness feedback，performance agent 消费 profiler evidence，交替执行 functional 与 optimization passes。<!-- claim:SF-KFORGE-CROSS-PLATFORM-KERNEL:start -->B200 与 Intel Arc B580 case study 支持 execution plan 必须绑定 target backend、compiler、shape、dtype 与 verifier；少量平台结果不能证明跨架构泛化，GUI/API profiler 与 LLM suggestion 也不替代 executable correctness gate。现有 execution-plan owner 已承载该机制。
<!-- claim:SF-KFORGE-CROSS-PLATFORM-KERNEL:end -->
<!-- review:SF-KFORGE-CROSS-PLATFORM-KERNEL:end -->
<!-- review:SF-ASYMCACHE-MULTI-SEGMENT:start -->
### Multi-Segment Attention / AsymCache

Lossless KV tiering 若只按 frequency/position 保留 block，可能让 GPU attention 反复处理昂贵的非连续段。AsymCache 让 cache manager 同时考虑 hit rate 与 position-aware recompute cost，用 Multi-Segment Attention 消费不连续 context，并由 adaptive chunking 保持设备利用率。<!-- claim:SF-ASYMCACHE-MULTI-SEGMENT:start -->作者 workload 支持 physical residency 必须读取 kernel execution cost，而非只看 logical reuse；不证明所有 attention kernel、Paged layout 或 agent serving 都得到同样收益。已有 Ch45 已拥有 recoverable tiering、logical-to-physical eviction 与 kernel compatibility。
<!-- claim:SF-ASYMCACHE-MULTI-SEGMENT:end -->
<!-- review:SF-ASYMCACHE-MULTI-SEGMENT:end -->
<!-- review:SF-DRIFTSCHED-TOKEN-DRIFT:start -->
### DriftSched

admission-time token estimate 在多租户生成中会随真实 output 进度漂移；固定 classification 将误差留给 queue imbalance 与 tail。DriftSched 把估计值作为可修订状态，用 runtime observation 校准 token budget，再比较 FIFO、priority、weighted、SJF 与 aging。<!-- claim:SF-DRIFTSCHED-TOKEN-DRIFT:start -->单 L4 的合成/重放 workload 支持 scheduler 应持续 reconcile estimated 与 observed work；论文同时显示 policy 选择影响可能大于 calibration。它不证明 SJF 在 fairness、deadline 或 adversarial tenant 下最优，必须保留 aging/admission 与 estimation-failure fallback。
<!-- claim:SF-DRIFTSCHED-TOKEN-DRIFT:end -->
<!-- review:SF-DRIFTSCHED-TOKEN-DRIFT:end -->

## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-KV-QUANT-ALIGNMENT-COLLAPSE | KV-cache quantized instruction models on 1,894 safety prompts | 11 instruction-tuned models, 3.8B–72B | RTX 3090 for 7B–9B, A100 80GB for 24B–47B, 8 GPUs for 72B; vLLM v0.13.0 check on RTX 3090 | FP16 baseline; simulated/packed 2–8 bit KV and FP8 e4m3/e5m2 vLLM cases | Five safety benchmarks totaling 1,894 prompts; max_new_tokens=256 | Not Disclosed | Not Disclosed | Not Disclosed | Memory overhead plus refusal preservation; no universal production threshold | ConditionalFlip, Wilson CI, WildGuard-7B, PPL/task/safety benchmarks |
| SF-SKILL-INJECTION-GUARDIAN | skill-injection attacks and benign utility | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | ASR + utility | Not Disclosed |
| SF-ROBOTRUSTBENCH-WORLD-MODEL | 1,207 instruction-image pairs across normal, constraint, counterfactual and adversarial scenarios | Not Disclosed | Not Disclosed | Not Disclosed | initial image + instruction | generated manipulation video | Not Disclosed | Not Required — offline corpus evaluation | 13 criteria across six trust dimensions; no runtime SLO | human raters + MLLM evaluators |
| SF-EXECUTION-GROUNDED-CODING-AGENT-SECURITY | Coding-agent software-engineering tasks carrying unsafe operations | Multiple agent frameworks/model backbones | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Verified unsafe execution, not text refusal | Tool/runtime/filesystem execution oracle |
| SF-OPTCC-ASYMMETRIC-ALLREDUCE | AllReduce with asymmetric NIC failures | collective microbenchmarks | Not Disclosed | Not Disclosed | Not Disclosed | Not Required — collective | Not Disclosed | Not Disclosed | completion time/bandwidth | Not Disclosed |
| SF-GAIATRACE-VIDUR-AGENT | Two multi-model agents on GAIA; trace-driven serving simulation | MiroThinker/OWL with heterogeneous sub-models | Simulated configurations; collection hardware not a universal baseline | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Task latency plus query TTFT/TPOT | Trace replay and simulator outputs |
| SF-SPARSEX-SEGMENT-KV | repeated non-prefix segments in long-context serving | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | TTFT/throughput/quality | Not Disclosed |
| SF-ADAPTIVE-AUTO-HARNESS | three streaming benchmark families plus evolution/routing/human-steering ablations | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | task success and peak/post-peak behavior; no production SLO | authors; benchmark evaluators in exact-v1 |
| SF-CONSERVE-CONVERSATION-PLACEMENT | replayed SWE-agent multi-turn traces from SWE-bench_bm25_13K | trace generator Qwen3-Coder-30B-A3B-Instruct; served Qwen3-0.6B | 4× NVIDIA A40; three power-capped to 2/3 of 300W TDP | Not Disclosed | average disclosed workload ≈15K input tokens/conversation | average disclosed workload ≈1K output tokens/conversation | Not Disclosed | Not Disclosed | p95 first-effective-token, last-turn TBT, throughput and energy | Not Disclosed |
| SF-COMPRESSION-UNCERTAINTY | 12 LLMs across five NLP tasks under quantization and sparsification | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | classification/generation output per task | Not Disclosed | Not Required — no serving concurrency claim | accuracy plus conformal coverage/set-size or selective-risk effects; no latency SLO | authors; task labels and conformal protocol |
| SF-ASYNC-INFERENCE-OVERHEADS | online LLM serving across model/benchmark and production traces | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | throughput, latency, GPU utilization and energy | Not Disclosed |
| SF-DRIFT-TELBENCH | trajectory-span error localization | two frameworks, three backbones | Not Disclosed | Not Disclosed | semantic-span trajectories | locator output | Not Disclosed | Not Disclosed | localization metrics | LLM-assisted expert review |
| SF-CONSENT-INTEGRITY | Not Disclosed | no model-quality comparison; trusted mediator/prototype configuration | Not Disclosed | Not Disclosed | command/action representation | approval rendering and bound execution result | Not Disclosed | Not Disclosed | inspectability, silent pass and over-prompting; no complete-mediation claim | authors; corpus-derived checks |
| SF-DFLARE-DIFFUSION-SPECULATION | GSM8K, MATH500, AIME25, HumanEval, MBPP and MTBench | Qwen3-4B; Qwen3-8B; GPT-OSS-20B | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | wall-clock speedup with task quality | Not Disclosed |
| SF-STRAGGLER-AWARE-RL-GROUP | synchronous GRPO/DAPO rollouts and downstream reasoning evaluation | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | variable rollout length is the controlled straggler signal | Not Disclosed | Not Disclosed | wall-clock, straggler rate, reward and downstream quality | Not Disclosed |
| SF-SECLAW-SPEC-DRIVEN-SECURITY | Proposed autonomous-agent security tasks with tools | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Proposed security outcome and trajectory reproducibility | Not Disclosed |
| SF-HARNESS1-EXTERNALIZED-STATE | search-agent tasks | Harness-1 20B + baselines | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | task success | Not Disclosed |
| SF-LLMFI-ERROR-PROPAGATION | deterministic fault injection over 13 reasoning/language/math/code tasks | three core dense open-weight LLMs (3.80B–8.54B) plus supplementary models | NVIDIA A100 40GB; AMD EPYC 7742; 1TB RAM; CUDA 12.3 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Required — controlled inference trials, not serving concurrency | task outcome and propagation/resilience metrics | Not Disclosed |
| SF-PEFT-SCALE | scale-up/down/out systems synthesis with embedded case evidence; no uniform benchmark | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | quality/resource/governance trade-offs; no uniform SLO | Not Disclosed |
| SF-GHOST-TOOL-ISSUE-PRIVACY | static plan, real planner, paired-frontier replay and pooled corpora | Claude Opus 4.7 planner/adversary; Haiku 4.5 and GPT-4o-mini cross-adversaries | hosted model/tool endpoints; no GPU contract | Not Disclosed | task/tool-argument dependent | speculative tool call / intent inference output | Not Disclosed | Not Disclosed | intent leakage, utility, cost and gate calibration | authors + independent adversary seeds |
| SF-SKILLHARM-LIFECYCLE | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | author research metric; no production threshold claimed | authors; evaluator details in exact-v1 evaluation section |
| SF-COSMOS3-OMNIMODAL | multimodal understanding/generation/action suites | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | global batch 512 for disclosed Reasoner stage; token-budget packing for Generator | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-CROWDED-EMBEDDING-EXTERNALITY | Shared embedding spaces for retrieval-augmented agents | Mean-field/finite retrieval simulations | Not Disclosed | Not Disclosed | Corpus-size/density sweep | Not Disclosed | Not Disclosed | Not Disclosed | Minority retrieval probability and shortlist reachability | Theory plus scoped simulations |
| SF-ECHELON-AGGREGATE-ONLY-ADAPTATION | 1B Llama-family LoRA across privacy boundaries | 1B Llama-family | WAN/emulated and cross-region; exact accelerators scoped by paper | Mixed precision | Sequence length 32 | Not Disclosed | Micro-batch 6, grad accumulation 4 | Not Disclosed | Validation loss, bytes, wall-clock, sync count, audit invariant | Budget-matched comparison and message-schema audit |
| SF-GATEAI-OPERATING-POINT-EVAL | Prompt-injection/jailbreak detector evaluation | Black-box detector plus published baselines | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | FPR/F1/calibration/latency at fixed operating point | Leakage-resistant CV and matched-FPR protocol |
| SF-KFORGE-CROSS-PLATFORM-KERNEL | gpt-oss-20b end-to-end inference and 37 GEMM+tail kernels | kernel-generation/performance-analysis agents; gpt-oss-20b | NVIDIA B200; Intel Arc B580 | mixed precision selected per generated kernel | Not Disclosed | Not Required — kernel/model execution | Not Disclosed | Not Disclosed | executable correctness plus throughput/speedup | compiler/test oracle + authors |
| SF-ASYMCACHE-MULTI-SEGMENT | lossless KV eviction/reconstruction and agent-serving integration | Not Disclosed | AMD EPYC 9K84; 4× NVIDIA H20 96GB; NVLink; CUDA 12.8 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | TTFT, TPOT and job latency | Not Disclosed |
| SF-DRIFTSCHED-TOKEN-DRIFT | heterogeneous multi-tenant inference under sustained contention | Not Disclosed | NVIDIA L4; Ubuntu; vLLM; Redis | Not Disclosed | estimated vs observed input/work class | runtime token generation is the drift variable | Not Disclosed | Not Disclosed | median/P99 latency, queue wait, estimate MAE/RMSE and utilization | Not Disclosed |

## 5. Deep Analysis Selection

<!-- audit-target:deep_analysis_selection:start -->
<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-KV-QUANT-ALIGNMENT-COLLAPSE | score_7_9;forced_review;potential_books_delta | not_selected | — | — | V2=9/9；Alignment Collapse Under KV Cache Quantization: Diagnosis and Mitigation establishes serving_evaluation_contract, but its delta is confined to its canonical owner and is less cross-cutting than the three selected units; its exact-v1 review and Books duty remain complete. | analysis-decision:SF-KV-QUANT-ALIGNMENT-COLLAPSE |
| SF-SKILL-INJECTION-GUARDIAN | score_7_9 | not_selected | — | — | V2=7/9；Defenses & Enablers For Skill Injection Attacks on Terminal Based Agents establishes security_release_contract, but its delta is confined to its canonical owner and is less cross-cutting than the three selected units; its exact-v1 review and Books duty remain complete. | analysis-decision:SF-SKILL-INJECTION-GUARDIAN |
| SF-ROBOTRUSTBENCH-WORLD-MODEL | score_7_9 | not_selected | — | — | V2=7/9；RoboTrustBench: Benchmarking the Trustworthiness of Video World Models for Robotic Manipulation establishes evaluation_contract, but its delta is confined to its canonical owner and is less cross-cutting than the three selected units; its exact-v1 review and Books duty remain complete. | analysis-decision:SF-ROBOTRUSTBENCH-WORLD-MODEL |
| SF-EXECUTION-GROUNDED-CODING-AGENT-SECURITY | score_7_9;forced_review;potential_books_delta | selected | DA-20260602-AGENT-SLO | — | V2=9/9；execution_evidence_contract provides this day's clearest cross-cutting owner/evidence delta; selection does not change review depth. | analysis:DA-20260602-AGENT-SLO |
| SF-OPTCC-ASYMMETRIC-ALLREDUCE | score_7_9;forced_review;potential_books_delta | not_selected | — | — | V2=8/9；Don't Let a Few Network Failures Slow the Entire AllReduce establishes communication_control_state, but its delta is confined to its canonical owner and is less cross-cutting than the three selected units; its exact-v1 review and Books duty remain complete. | analysis-decision:SF-OPTCC-ASYMMETRIC-ALLREDUCE |
| SF-GAIATRACE-VIDUR-AGENT | score_7_9;forced_review;potential_books_delta | selected | DA-20260602-AGENT-SLO | — | V2=8/9；agentic_serving_evaluation_contract provides this day's clearest cross-cutting owner/evidence delta; selection does not change review depth. | analysis:DA-20260602-AGENT-SLO |
| SF-SPARSEX-SEGMENT-KV | score_7_9;forced_review;potential_books_delta | not_selected | — | — | V2=8/9；SparseX: Efficient Segment-Level KV Cache Sharing for Interleaved LLM Serving establishes runtime_state_identity, but its delta is confined to its canonical owner and is less cross-cutting than the three selected units; its exact-v1 review and Books duty remain complete. | analysis-decision:SF-SPARSEX-SEGMENT-KV |
| SF-ADAPTIVE-AUTO-HARNESS | score_7_9;forced_review;potential_books_delta | not_selected | — | — | V2=8/9；Adaptive Auto-Harness: Sustained Self-Improvement for Agentic System Deployment on Open-Ended Task Streams establishes workflow_control_state, but its delta is confined to its canonical owner and is less cross-cutting than the three selected units; its exact-v1 review and Books duty remain complete. | analysis-decision:SF-ADAPTIVE-AUTO-HARNESS |
| SF-CONSERVE-CONVERSATION-PLACEMENT | score_7_9;forced_review;potential_books_delta | not_selected | — | — | V2=9/9；Observation, Not Prediction: Conversation-Level Disaggregated Scheduling for Agentic Serving establishes placement_state_ownership, but its delta is confined to its canonical owner and is less cross-cutting than the three selected units; its exact-v1 review and Books duty remain complete. | analysis-decision:SF-CONSERVE-CONVERSATION-PLACEMENT |
| SF-COMPRESSION-UNCERTAINTY | score_7_9;forced_review;potential_books_delta | not_selected | — | — | V2=8/9；Does Compression Preserve Uncertainty? A Unified Benchmark for Quantized and Sparse LLMs via Conformal Prediction establishes evaluation_contract, but its delta is confined to its canonical owner and is less cross-cutting than the three selected units; its exact-v1 review and Books duty remain complete. | analysis-decision:SF-COMPRESSION-UNCERTAINTY |
| SF-ASYNC-INFERENCE-OVERHEADS | score_7_9;forced_review;potential_books_delta | not_selected | — | — | V2=9/9；Scaling LLM Inference Beyond Amdahl`s Limits via Eliminating Non-Scalable Overheads establishes runtime_control_path, but its delta is confined to its canonical owner and is less cross-cutting than the three selected units; its exact-v1 review and Books duty remain complete. | analysis-decision:SF-ASYNC-INFERENCE-OVERHEADS |
| SF-DRIFT-TELBENCH | score_7_9;forced_review;potential_books_delta | not_selected | — | — | V2=9/9；Where Do Deep-Research Agents Go Wrong? Span-Level Error Localization in Agent Trajectories establishes failure_evidence_contract, but its delta is confined to its canonical owner and is less cross-cutting than the three selected units; its exact-v1 review and Books duty remain complete. | analysis-decision:SF-DRIFT-TELBENCH |
| SF-CONSENT-INTEGRITY | score_7_9;forced_review;potential_books_delta | not_selected | — | — | V2=9/9；What You Approve Is What Executes: Consent Integrity for Black-Box LLM Agents establishes consent_effect_integrity, but its delta is confined to its canonical owner and is less cross-cutting than the three selected units; its exact-v1 review and Books duty remain complete. | analysis-decision:SF-CONSENT-INTEGRITY |
| SF-DFLARE-DIFFUSION-SPECULATION | score_7_9;forced_review;potential_books_delta | not_selected | — | — | V2=8/9；DFlare: Scaling Up Draft Capacity for Block Diffusion Speculative Decoding establishes speculative_commit_contract, but its delta is confined to its canonical owner and is less cross-cutting than the three selected units; its exact-v1 review and Books duty remain complete. | analysis-decision:SF-DFLARE-DIFFUSION-SPECULATION |
| SF-STRAGGLER-AWARE-RL-GROUP | score_7_9;forced_review;potential_books_delta | not_selected | — | — | V2=8/9；Faster Synchronous On-Policy RL via Straggler-Aware Group Sizing establishes distributed_training_control_state, but its delta is confined to its canonical owner and is less cross-cutting than the three selected units; its exact-v1 review and Books duty remain complete. | analysis-decision:SF-STRAGGLER-AWARE-RL-GROUP |
| SF-HARNESS1-EXTERNALIZED-STATE | score_7_9;forced_review | not_selected | — | — | V2=9/9；Harness-1: Reinforcement Learning for Search Agents with State-Externalizing Harnesses establishes externalized_workflow_state, but its delta is confined to its canonical owner and is less cross-cutting than the three selected units; its exact-v1 review and Books duty remain complete. | analysis-decision:SF-HARNESS1-EXTERNALIZED-STATE |
| SF-LLMFI-ERROR-PROPAGATION | score_7_9;forced_review;potential_books_delta | not_selected | — | — | V2=7/9；Not All Errors Are Equal: A Systematic Study of Error Propagation in Large Language Model Inference establishes failure_evidence_contract, but its delta is confined to its canonical owner and is less cross-cutting than the three selected units; its exact-v1 review and Books duty remain complete. | analysis-decision:SF-LLMFI-ERROR-PROPAGATION |
| SF-PEFT-SCALE | score_7_9 | not_selected | — | — | V2=9/9；On the Scaling of PEFT: Towards Million Personal Models of Trillion Parameters establishes artifact_identity_and_residency, but its delta is confined to its canonical owner and is less cross-cutting than the three selected units; its exact-v1 review and Books duty remain complete. | analysis-decision:SF-PEFT-SCALE |
| SF-GHOST-TOOL-ISSUE-PRIVACY | score_7_9;forced_review;potential_books_delta | not_selected | — | — | V2=8/9；Ghost Tool Calls: Issue-Time Privacy for Speculative Agent Tools establishes tool_effect_authorization, but its delta is confined to its canonical owner and is less cross-cutting than the three selected units; its exact-v1 review and Books duty remain complete. | analysis-decision:SF-GHOST-TOOL-ISSUE-PRIVACY |
| SF-SKILLHARM-LIFECYCLE | score_7_9;forced_review;potential_books_delta | not_selected | — | — | V2=7/9；SkillHarm: Lifecycle-Aware Skill-Based Attacks via Automated Construction establishes skill_lifecycle_trust_contract, but its delta is confined to its canonical owner and is less cross-cutting than the three selected units; its exact-v1 review and Books duty remain complete. | analysis-decision:SF-SKILLHARM-LIFECYCLE |
| SF-COSMOS3-OMNIMODAL | score_7_9;forced_review | not_selected | — | — | V2=9/9；Cosmos 3: Omnimodal World Models for Physical AI establishes world_state_and_action_contract, but its delta is confined to its canonical owner and is less cross-cutting than the three selected units; its exact-v1 review and Books duty remain complete. | analysis-decision:SF-COSMOS3-OMNIMODAL |
| SF-CROWDED-EMBEDDING-EXTERNALITY | score_7_9;forced_review;potential_books_delta | not_selected | — | — | V2=7/9；The Crowded Embedding Space: A Mean-Field Mechanism for Emergent Marginalization in Retrieval-Augmented Agents establishes shared_retrieval_state_externality, but its delta is confined to its canonical owner and is less cross-cutting than the three selected units; its exact-v1 review and Books duty remain complete. | analysis-decision:SF-CROWDED-EMBEDDING-EXTERNALITY |
| SF-ECHELON-AGGREGATE-ONLY-ADAPTATION | score_7_9;forced_review;potential_books_delta | selected | DA-20260602-BOUNDARY-STATE | — | V2=9/9；privacy_boundary_training_state provides this day's clearest cross-cutting owner/evidence delta; selection does not change review depth. | analysis:DA-20260602-BOUNDARY-STATE |
| SF-GATEAI-OPERATING-POINT-EVAL | score_7_9 | not_selected | — | — | V2=8/9；Gate AI: LLM Security Benchmark Evaluation Methodology and Results establishes security_operating_point_contract, but its delta is confined to its canonical owner and is less cross-cutting than the three selected units; its exact-v1 review and Books duty remain complete. | analysis-decision:SF-GATEAI-OPERATING-POINT-EVAL |
| SF-KFORGE-CROSS-PLATFORM-KERNEL | score_7_9 | not_selected | — | — | V2=7/9；KForge: LLM-Driven Cross-Platform Kernel Generation for AI Accelerators establishes execution_plan_portability, but its delta is confined to its canonical owner and is less cross-cutting than the three selected units; its exact-v1 review and Books duty remain complete. | analysis-decision:SF-KFORGE-CROSS-PLATFORM-KERNEL |
| SF-ASYMCACHE-MULTI-SEGMENT | score_7_9 | not_selected | — | — | V2=8/9；Multi-Segment Attention: Enabling Efficient KV-Cache Management for Faster Large Language Model Serving establishes kernel_cost_aware_residency_control, but its delta is confined to its canonical owner and is less cross-cutting than the three selected units; its exact-v1 review and Books duty remain complete. | analysis-decision:SF-ASYMCACHE-MULTI-SEGMENT |
| SF-DRIFTSCHED-TOKEN-DRIFT | score_7_9;forced_review;potential_books_delta | not_selected | — | — | V2=8/9；DriftSched: Adaptive QoS-Aware Scheduling under Runtime Token Drift for Multi-Tenant GPU Inference establishes runtime_drift_control_state, but its delta is confined to its canonical owner and is less cross-cutting than the three selected units; its exact-v1 review and Books duty remain complete. | analysis-decision:SF-DRIFTSCHED-TOKEN-DRIFT |

<!-- analysis-decision:SF-KV-QUANT-ALIGNMENT-COLLAPSE:start -->V2=9/9；Alignment Collapse Under KV Cache Quantization: Diagnosis and Mitigation establishes serving_evaluation_contract, but its delta is confined to its canonical owner and is less cross-cutting than the three selected units; its exact-v1 review and Books duty remain complete.<!-- analysis-decision:SF-KV-QUANT-ALIGNMENT-COLLAPSE:end -->
<!-- analysis-decision:SF-SKILL-INJECTION-GUARDIAN:start -->V2=7/9；Defenses & Enablers For Skill Injection Attacks on Terminal Based Agents establishes security_release_contract, but its delta is confined to its canonical owner and is less cross-cutting than the three selected units; its exact-v1 review and Books duty remain complete.<!-- analysis-decision:SF-SKILL-INJECTION-GUARDIAN:end -->
<!-- analysis-decision:SF-ROBOTRUSTBENCH-WORLD-MODEL:start -->V2=7/9；RoboTrustBench: Benchmarking the Trustworthiness of Video World Models for Robotic Manipulation establishes evaluation_contract, but its delta is confined to its canonical owner and is less cross-cutting than the three selected units; its exact-v1 review and Books duty remain complete.<!-- analysis-decision:SF-ROBOTRUSTBENCH-WORLD-MODEL:end -->
<!-- analysis-decision:SF-OPTCC-ASYMMETRIC-ALLREDUCE:start -->V2=8/9；Don't Let a Few Network Failures Slow the Entire AllReduce establishes communication_control_state, but its delta is confined to its canonical owner and is less cross-cutting than the three selected units; its exact-v1 review and Books duty remain complete.<!-- analysis-decision:SF-OPTCC-ASYMMETRIC-ALLREDUCE:end -->
<!-- analysis-decision:SF-SPARSEX-SEGMENT-KV:start -->V2=8/9；SparseX: Efficient Segment-Level KV Cache Sharing for Interleaved LLM Serving establishes runtime_state_identity, but its delta is confined to its canonical owner and is less cross-cutting than the three selected units; its exact-v1 review and Books duty remain complete.<!-- analysis-decision:SF-SPARSEX-SEGMENT-KV:end -->
<!-- analysis-decision:SF-ADAPTIVE-AUTO-HARNESS:start -->V2=8/9；Adaptive Auto-Harness: Sustained Self-Improvement for Agentic System Deployment on Open-Ended Task Streams establishes workflow_control_state, but its delta is confined to its canonical owner and is less cross-cutting than the three selected units; its exact-v1 review and Books duty remain complete.<!-- analysis-decision:SF-ADAPTIVE-AUTO-HARNESS:end -->
<!-- analysis-decision:SF-CONSERVE-CONVERSATION-PLACEMENT:start -->V2=9/9；Observation, Not Prediction: Conversation-Level Disaggregated Scheduling for Agentic Serving establishes placement_state_ownership, but its delta is confined to its canonical owner and is less cross-cutting than the three selected units; its exact-v1 review and Books duty remain complete.<!-- analysis-decision:SF-CONSERVE-CONVERSATION-PLACEMENT:end -->
<!-- analysis-decision:SF-COMPRESSION-UNCERTAINTY:start -->V2=8/9；Does Compression Preserve Uncertainty? A Unified Benchmark for Quantized and Sparse LLMs via Conformal Prediction establishes evaluation_contract, but its delta is confined to its canonical owner and is less cross-cutting than the three selected units; its exact-v1 review and Books duty remain complete.<!-- analysis-decision:SF-COMPRESSION-UNCERTAINTY:end -->
<!-- analysis-decision:SF-ASYNC-INFERENCE-OVERHEADS:start -->V2=9/9；Scaling LLM Inference Beyond Amdahl`s Limits via Eliminating Non-Scalable Overheads establishes runtime_control_path, but its delta is confined to its canonical owner and is less cross-cutting than the three selected units; its exact-v1 review and Books duty remain complete.<!-- analysis-decision:SF-ASYNC-INFERENCE-OVERHEADS:end -->
<!-- analysis-decision:SF-DRIFT-TELBENCH:start -->V2=9/9；Where Do Deep-Research Agents Go Wrong? Span-Level Error Localization in Agent Trajectories establishes failure_evidence_contract, but its delta is confined to its canonical owner and is less cross-cutting than the three selected units; its exact-v1 review and Books duty remain complete.<!-- analysis-decision:SF-DRIFT-TELBENCH:end -->
<!-- analysis-decision:SF-CONSENT-INTEGRITY:start -->V2=9/9；What You Approve Is What Executes: Consent Integrity for Black-Box LLM Agents establishes consent_effect_integrity, but its delta is confined to its canonical owner and is less cross-cutting than the three selected units; its exact-v1 review and Books duty remain complete.<!-- analysis-decision:SF-CONSENT-INTEGRITY:end -->
<!-- analysis-decision:SF-DFLARE-DIFFUSION-SPECULATION:start -->V2=8/9；DFlare: Scaling Up Draft Capacity for Block Diffusion Speculative Decoding establishes speculative_commit_contract, but its delta is confined to its canonical owner and is less cross-cutting than the three selected units; its exact-v1 review and Books duty remain complete.<!-- analysis-decision:SF-DFLARE-DIFFUSION-SPECULATION:end -->
<!-- analysis-decision:SF-STRAGGLER-AWARE-RL-GROUP:start -->V2=8/9；Faster Synchronous On-Policy RL via Straggler-Aware Group Sizing establishes distributed_training_control_state, but its delta is confined to its canonical owner and is less cross-cutting than the three selected units; its exact-v1 review and Books duty remain complete.<!-- analysis-decision:SF-STRAGGLER-AWARE-RL-GROUP:end -->
<!-- analysis-decision:SF-HARNESS1-EXTERNALIZED-STATE:start -->V2=9/9；Harness-1: Reinforcement Learning for Search Agents with State-Externalizing Harnesses establishes externalized_workflow_state, but its delta is confined to its canonical owner and is less cross-cutting than the three selected units; its exact-v1 review and Books duty remain complete.<!-- analysis-decision:SF-HARNESS1-EXTERNALIZED-STATE:end -->
<!-- analysis-decision:SF-LLMFI-ERROR-PROPAGATION:start -->V2=7/9；Not All Errors Are Equal: A Systematic Study of Error Propagation in Large Language Model Inference establishes failure_evidence_contract, but its delta is confined to its canonical owner and is less cross-cutting than the three selected units; its exact-v1 review and Books duty remain complete.<!-- analysis-decision:SF-LLMFI-ERROR-PROPAGATION:end -->
<!-- analysis-decision:SF-PEFT-SCALE:start -->V2=9/9；On the Scaling of PEFT: Towards Million Personal Models of Trillion Parameters establishes artifact_identity_and_residency, but its delta is confined to its canonical owner and is less cross-cutting than the three selected units; its exact-v1 review and Books duty remain complete.<!-- analysis-decision:SF-PEFT-SCALE:end -->
<!-- analysis-decision:SF-GHOST-TOOL-ISSUE-PRIVACY:start -->V2=8/9；Ghost Tool Calls: Issue-Time Privacy for Speculative Agent Tools establishes tool_effect_authorization, but its delta is confined to its canonical owner and is less cross-cutting than the three selected units; its exact-v1 review and Books duty remain complete.<!-- analysis-decision:SF-GHOST-TOOL-ISSUE-PRIVACY:end -->
<!-- analysis-decision:SF-SKILLHARM-LIFECYCLE:start -->V2=7/9；SkillHarm: Lifecycle-Aware Skill-Based Attacks via Automated Construction establishes skill_lifecycle_trust_contract, but its delta is confined to its canonical owner and is less cross-cutting than the three selected units; its exact-v1 review and Books duty remain complete.<!-- analysis-decision:SF-SKILLHARM-LIFECYCLE:end -->
<!-- analysis-decision:SF-COSMOS3-OMNIMODAL:start -->V2=9/9；Cosmos 3: Omnimodal World Models for Physical AI establishes world_state_and_action_contract, but its delta is confined to its canonical owner and is less cross-cutting than the three selected units; its exact-v1 review and Books duty remain complete.<!-- analysis-decision:SF-COSMOS3-OMNIMODAL:end -->
<!-- analysis-decision:SF-CROWDED-EMBEDDING-EXTERNALITY:start -->V2=7/9；The Crowded Embedding Space: A Mean-Field Mechanism for Emergent Marginalization in Retrieval-Augmented Agents establishes shared_retrieval_state_externality, but its delta is confined to its canonical owner and is less cross-cutting than the three selected units; its exact-v1 review and Books duty remain complete.<!-- analysis-decision:SF-CROWDED-EMBEDDING-EXTERNALITY:end -->
<!-- analysis-decision:SF-GATEAI-OPERATING-POINT-EVAL:start -->V2=8/9；Gate AI: LLM Security Benchmark Evaluation Methodology and Results establishes security_operating_point_contract, but its delta is confined to its canonical owner and is less cross-cutting than the three selected units; its exact-v1 review and Books duty remain complete.<!-- analysis-decision:SF-GATEAI-OPERATING-POINT-EVAL:end -->
<!-- analysis-decision:SF-KFORGE-CROSS-PLATFORM-KERNEL:start -->V2=7/9；KForge: LLM-Driven Cross-Platform Kernel Generation for AI Accelerators establishes execution_plan_portability, but its delta is confined to its canonical owner and is less cross-cutting than the three selected units; its exact-v1 review and Books duty remain complete.<!-- analysis-decision:SF-KFORGE-CROSS-PLATFORM-KERNEL:end -->
<!-- analysis-decision:SF-ASYMCACHE-MULTI-SEGMENT:start -->V2=8/9；Multi-Segment Attention: Enabling Efficient KV-Cache Management for Faster Large Language Model Serving establishes kernel_cost_aware_residency_control, but its delta is confined to its canonical owner and is less cross-cutting than the three selected units; its exact-v1 review and Books duty remain complete.<!-- analysis-decision:SF-ASYMCACHE-MULTI-SEGMENT:end -->
<!-- analysis-decision:SF-DRIFTSCHED-TOKEN-DRIFT:start -->V2=8/9；DriftSched: Adaptive QoS-Aware Scheduling under Runtime Token Drift for Multi-Tenant GPU Inference establishes runtime_drift_control_state, but its delta is confined to its canonical owner and is less cross-cutting than the three selected units; its exact-v1 review and Books duty remain complete.<!-- analysis-decision:SF-DRIFTSCHED-TOKEN-DRIFT:end -->

### Full-frontier non-eligible closures

<!-- analysis-noneligible:SF-SECLAW-SPEC-DRIVEN-SECURITY:start -->`SF-SECLAW-SPEC-DRIVEN-SECURITY`：Score V2=6/9、Review Override=`none`，且 pre-Books review 不满足 `score_7_9`、`forced_review`、`potential_books_delta`、`potential_structural_gap` 或 `cross_cutting_correction`。因此按 REPORT_CONTRACTS §3.5 保留在主 Selection eligible pool 之外；其 exact-v1 Standard Review、十字段 Benchmark Contract 与 No Change Books Comparison 仍然完整，不能把 non-eligible closure 误写成 `not_selected`。<!-- analysis-noneligible:SF-SECLAW-SPEC-DRIVEN-SECURITY:end -->

<!-- analysis:DA-20260602-AGENT-SLO:start -->
### Agent workload 把 query SLO 推进为 task/effect evidence

Agent 系统不再能用单次 LLM query 的 TTFT、文本 refusal 或 final answer 代表整体正确性。trace-driven serving 把 task dependency 暴露给 scheduler；security evaluation 则把 tool/runtime/filesystem effect 暴露给 release Gate。共同变化是 evidence owner 从 transcript 移到可重放的 task graph 与 environment state，代价是 trace schema、sandbox fidelity 与 predicate coverage 成为新的 failure mode。
<!-- analysis:DA-20260602-AGENT-SLO:end -->

<!-- analysis:DA-20260602-BOUNDARY-STATE:start -->
### 分布式控制从平均拓扑推进到显式 boundary state

对称 collective、固定 group size 与自由交换 update 在原约束下合理；非对称链路、straggler 与行政隐私边界出现后，control plane 必须消费 bandwidth、participation、staleness 与 allowed-message type。收益是故障/治理条件下仍能推进，代价是动态控制误判、额外 buffer 与审计面；旧同步方案在拓扑稳定、边界一致时仍更简单。
<!-- analysis:DA-20260602-BOUNDARY-STATE:end -->

<!-- audit-target:deep_analysis_selection:end -->

## 6. Books Comparison

<!-- audit-target:books:start -->
<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-KV-QUANT-ALIGNMENT-COLLAPSE | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L10 | books/part-05-inference-system/44-decode.md#L10;books/part-05-inference-system/49-tensorrt-llm.md#L10 | existing:SF-KV-QUANT-ALIGNMENT-COLLAPSE | delta:SF-KV-QUANT-ALIGNMENT-COLLAPSE | Direct Evolution | Integrate | books-review:SF-KV-QUANT-ALIGNMENT-COLLAPSE |
| SF-SKILL-INJECTION-GUARDIAN | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L418 | books/part-07-agent/78-tool-calling.md#L10;books/part-07-agent/83-mcp.md#L10 | existing:SF-SKILL-INJECTION-GUARDIAN | delta:SF-SKILL-INJECTION-GUARDIAN | Layering / Dependency | No Change — Existing Coverage | books-review:SF-SKILL-INJECTION-GUARDIAN |
| SF-ROBOTRUSTBENCH-WORLD-MODEL | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L416 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L10;books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L365 | existing:SF-ROBOTRUSTBENCH-WORLD-MODEL | delta:SF-ROBOTRUSTBENCH-WORLD-MODEL | Layering / Dependency | No Change — Existing Coverage | books-review:SF-ROBOTRUSTBENCH-WORLD-MODEL |
| SF-EXECUTION-GROUNDED-CODING-AGENT-SECURITY | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L10 | books/part-06-ai-infrastructure/66-evaluation-system.md#L10;books/part-07-agent/84-agent-platform.md#L10 | existing:SF-EXECUTION-GROUNDED-CODING-AGENT-SECURITY | delta:SF-EXECUTION-GROUNDED-CODING-AGENT-SECURITY | Direct Evolution | Integrate | books-review:SF-EXECUTION-GROUNDED-CODING-AGENT-SECURITY |
| SF-OPTCC-ASYMMETRIC-ALLREDUCE | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#L136 | books/part-04-training-system/37-tensor-parallel.md#L10;books/part-04-training-system/40-megatron.md#L10 | existing:SF-OPTCC-ASYMMETRIC-ALLREDUCE | delta:SF-OPTCC-ASYMMETRIC-ALLREDUCE | Direct Evolution | Integrate | books-review:SF-OPTCC-ASYMMETRIC-ALLREDUCE |
| SF-GAIATRACE-VIDUR-AGENT | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#L10 | books/part-05-inference-system/42-what-happens-during-inference.md#L10;books/part-05-inference-system/55-pd-disaggregation.md#L10 | existing:SF-GAIATRACE-VIDUR-AGENT | delta:SF-GAIATRACE-VIDUR-AGENT | Direct Evolution | Integrate | books-review:SF-GAIATRACE-VIDUR-AGENT |
| SF-SPARSEX-SEGMENT-KV | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L110 | books/part-05-inference-system/43-prefill.md#L10;books/part-05-inference-system/47-pagedattention.md#L10 | existing:SF-SPARSEX-SEGMENT-KV | delta:SF-SPARSEX-SEGMENT-KV | Direct Evolution | Integrate | books-review:SF-SPARSEX-SEGMENT-KV |
| SF-ADAPTIVE-AUTO-HARNESS | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#L10 | books/part-07-agent/81-workflow.md#L10;books/part-07-agent/82-multi-agent.md#L10 | existing:SF-ADAPTIVE-AUTO-HARNESS | delta:SF-ADAPTIVE-AUTO-HARNESS | Direct Evolution | Integrate | books-review:SF-ADAPTIVE-AUTO-HARNESS |
| SF-CONSERVE-CONVERSATION-PLACEMENT | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#L14 | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L754;books/part-05-inference-system/55-pd-disaggregation.md#L10 | existing:SF-CONSERVE-CONVERSATION-PLACEMENT | delta:SF-CONSERVE-CONVERSATION-PLACEMENT | Direct Evolution | Integrate | books-review:SF-CONSERVE-CONVERSATION-PLACEMENT |
| SF-COMPRESSION-UNCERTAINTY | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L10 | books/part-06-ai-infrastructure/67-monitoring.md#L10;books/part-06-ai-infrastructure/73-production-best-practice.md#L10 | existing:SF-COMPRESSION-UNCERTAINTY | delta:SF-COMPRESSION-UNCERTAINTY | Direct Evolution | Integrate | books-review:SF-COMPRESSION-UNCERTAINTY |
| SF-ASYNC-INFERENCE-OVERHEADS | INFER-REQUEST-LIFECYCLE | books/part-05-inference-system/42-what-happens-during-inference.md#L37 | books/part-05-inference-system/49-tensorrt-llm.md#L12;books/part-05-inference-system/50-vllm.md#L247 | existing:SF-ASYNC-INFERENCE-OVERHEADS | delta:SF-ASYNC-INFERENCE-OVERHEADS | Direct Evolution | Integrate | books-review:SF-ASYNC-INFERENCE-OVERHEADS |
| SF-DRIFT-TELBENCH | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L252 | books/part-06-ai-infrastructure/69-trace.md#L10;books/part-07-agent/80-reflection.md#L10 | existing:SF-DRIFT-TELBENCH | delta:SF-DRIFT-TELBENCH | Direct Evolution | Integrate | books-review:SF-DRIFT-TELBENCH |
| SF-CONSENT-INTEGRITY | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L10 | books/part-07-agent/78-tool-calling.md#L10;books/part-07-agent/83-mcp.md#L10 | existing:SF-CONSENT-INTEGRITY | delta:SF-CONSENT-INTEGRITY | Direct Evolution | Integrate | books-review:SF-CONSENT-INTEGRITY |
| SF-DFLARE-DIFFUSION-SPECULATION | INFER-SPECULATIVE-DECODING | books/part-05-inference-system/48-speculative-decoding.md#L268 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L10;books/part-05-inference-system/50-vllm.md#L73 | existing:SF-DFLARE-DIFFUSION-SPECULATION | delta:SF-DFLARE-DIFFUSION-SPECULATION | Direct Evolution | Integrate | books-review:SF-DFLARE-DIFFUSION-SPECULATION |
| SF-STRAGGLER-AWARE-RL-GROUP | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#L14 | books/part-04-training-system/32-ppo.md#L10;books/part-04-training-system/41-deepspeed.md#L10 | existing:SF-STRAGGLER-AWARE-RL-GROUP | delta:SF-STRAGGLER-AWARE-RL-GROUP | Direct Evolution | Integrate | books-review:SF-STRAGGLER-AWARE-RL-GROUP |
| SF-SECLAW-SPEC-DRIVEN-SECURITY | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L10 | books/part-06-ai-infrastructure/66-evaluation-system.md#L10;books/part-07-agent/84-agent-platform.md#L10 | existing:SF-SECLAW-SPEC-DRIVEN-SECURITY | delta:SF-SECLAW-SPEC-DRIVEN-SECURITY | Principle Reuse | No Change — Existing Coverage | books-review:SF-SECLAW-SPEC-DRIVEN-SECURITY |
| SF-HARNESS1-EXTERNALIZED-STATE | AGENT-CONTEXT | books/part-07-agent/75-context.md#L165 | books/part-07-agent/76-rag.md#L10;books/part-07-agent/77-memory.md#L10 | existing:SF-HARNESS1-EXTERNALIZED-STATE | delta:SF-HARNESS1-EXTERNALIZED-STATE | Direct Evolution | No Change — Existing Coverage | books-review:SF-HARNESS1-EXTERNALIZED-STATE |
| SF-LLMFI-ERROR-PROPAGATION | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L613 | books/part-06-ai-infrastructure/67-monitoring.md#L10;books/part-05-inference-system/42-what-happens-during-inference.md#L14 | existing:SF-LLMFI-ERROR-PROPAGATION | delta:SF-LLMFI-ERROR-PROPAGATION | Direct Evolution | Integrate | books-review:SF-LLMFI-ERROR-PROPAGATION |
| SF-PEFT-SCALE | PLATFORM-MODEL-REGISTRY | books/part-06-ai-infrastructure/59-model-registry.md#L70 | books/part-04-training-system/30-lora.md#L10;books/part-06-ai-infrastructure/61-kserve.md#L10 | existing:SF-PEFT-SCALE | delta:SF-PEFT-SCALE | Layering / Dependency | No Change — Existing Coverage | books-review:SF-PEFT-SCALE |
| SF-GHOST-TOOL-ISSUE-PRIVACY | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L522 | books/part-07-agent/78-tool-calling.md#L10;books/part-07-agent/81-workflow.md#L10 | existing:SF-GHOST-TOOL-ISSUE-PRIVACY | delta:SF-GHOST-TOOL-ISSUE-PRIVACY | Direct Evolution | Integrate | books-review:SF-GHOST-TOOL-ISSUE-PRIVACY |
| SF-SKILLHARM-LIFECYCLE | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L10 | books/part-07-agent/78-tool-calling.md#L10;books/part-07-agent/83-mcp.md#L10 | existing:SF-SKILLHARM-LIFECYCLE | delta:SF-SKILLHARM-LIFECYCLE | Direct Evolution | Integrate | books-review:SF-SKILLHARM-LIFECYCLE |
| SF-COSMOS3-OMNIMODAL | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L542 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L10;books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L10 | existing:SF-COSMOS3-OMNIMODAL | delta:SF-COSMOS3-OMNIMODAL | Layering / Dependency | No Change — Existing Coverage | books-review:SF-COSMOS3-OMNIMODAL |
| SF-CROWDED-EMBEDDING-EXTERNALITY | AGENT-RAG | books/part-07-agent/76-rag.md#L10 | books/part-07-agent/75-context.md#L10;books/part-07-agent/77-memory.md#L10 | existing:SF-CROWDED-EMBEDDING-EXTERNALITY | delta:SF-CROWDED-EMBEDDING-EXTERNALITY | Direct Evolution | Integrate | books-review:SF-CROWDED-EMBEDDING-EXTERNALITY |
| SF-ECHELON-AGGREGATE-ONLY-ADAPTATION | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#L10 | books/part-04-training-system/35-checkpoint.md#L10;books/part-04-training-system/37-tensor-parallel.md#L10 | existing:SF-ECHELON-AGGREGATE-ONLY-ADAPTATION | delta:SF-ECHELON-AGGREGATE-ONLY-ADAPTATION | Direct Evolution | Integrate | books-review:SF-ECHELON-AGGREGATE-ONLY-ADAPTATION |
| SF-GATEAI-OPERATING-POINT-EVAL | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L10 | books/part-06-ai-infrastructure/65-observability.md#L10;books/part-06-ai-infrastructure/72-security.md#L10 | existing:SF-GATEAI-OPERATING-POINT-EVAL | delta:SF-GATEAI-OPERATING-POINT-EVAL | Principle Reuse | No Change — Existing Coverage | books-review:SF-GATEAI-OPERATING-POINT-EVAL |
| SF-KFORGE-CROSS-PLATFORM-KERNEL | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#L217 | books/part-06-ai-infrastructure/66-evaluation-system.md#L815;books/part-05-inference-system/56-inference-scheduling.md#L383 | existing:SF-KFORGE-CROSS-PLATFORM-KERNEL | delta:SF-KFORGE-CROSS-PLATFORM-KERNEL | Principle Reuse | No Change — Existing Coverage | books-review:SF-KFORGE-CROSS-PLATFORM-KERNEL |
| SF-ASYMCACHE-MULTI-SEGMENT | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L311 | books/part-05-inference-system/47-pagedattention.md#L10;books/part-05-inference-system/49-tensorrt-llm.md#L147 | existing:SF-ASYMCACHE-MULTI-SEGMENT | delta:SF-ASYMCACHE-MULTI-SEGMENT | Layering / Dependency | No Change — Existing Coverage | books-review:SF-ASYMCACHE-MULTI-SEGMENT |
| SF-DRIFTSCHED-TOKEN-DRIFT | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#L176 | books/part-05-inference-system/46-continuous-batching.md#L10;books/part-06-ai-infrastructure/66-evaluation-system.md#L10 | existing:SF-DRIFTSCHED-TOKEN-DRIFT | delta:SF-DRIFTSCHED-TOKEN-DRIFT | Direct Evolution | Integrate | books-review:SF-DRIFTSCHED-TOKEN-DRIFT |

<!-- existing:SF-KV-QUANT-ALIGNMENT-COLLAPSE:start -->KV identity 已绑定 model/token/position/precision，量化需 workload-specific validation。<!-- existing:SF-KV-QUANT-ALIGNMENT-COLLAPSE:end -->
<!-- delta:SF-KV-QUANT-ALIGNMENT-COLLAPSE:start -->把 alignment behavior 与 refusal evaluator 加入 KV precision artifact 的 release contract。<!-- delta:SF-KV-QUANT-ALIGNMENT-COLLAPSE:end -->
<!-- books-review:SF-KV-QUANT-ALIGNMENT-COLLAPSE:start -->Root 已完成最小串行写回；当前 owner 与相邻章节、正文机制及 exact-v1 Review note 已通过 post-write audit。<!-- books-review:SF-KV-QUANT-ALIGNMENT-COLLAPSE:end -->
<!-- existing:SF-SKILL-INJECTION-GUARDIAN:start -->Ch72 已分离 untrusted input、authorization 与 effect。<!-- existing:SF-SKILL-INJECTION-GUARDIAN:end -->
<!-- delta:SF-SKILL-INJECTION-GUARDIAN:start -->Guardian 提供 defense-in-depth 案例，不替代现有安全合同。<!-- delta:SF-SKILL-INJECTION-GUARDIAN:end -->
<!-- books-review:SF-SKILL-INJECTION-GUARDIAN:start -->existing:SF-SKILL-INJECTION-GUARDIAN Ch72 已将 prompt/skill input 与 authorization/effect 分离；delta:SF-SKILL-INJECTION-GUARDIAN 提供 guardian 受限案例。Ch78 owns tool invocation，Ch83 owns protocol trust，均不拥有平台安全策略。<!-- books-review:SF-SKILL-INJECTION-GUARDIAN:end -->
<!-- existing:SF-ROBOTRUSTBENCH-WORLD-MODEL:start -->Ch25 已明确 video quality、one-step prediction 与 action-conditioned world truth 不能互相替代。<!-- existing:SF-ROBOTRUSTBENCH-WORLD-MODEL:end -->
<!-- delta:SF-ROBOTRUSTBENCH-WORLD-MODEL:start -->RoboTrustBench 增加 constraint/counterfactual/adversarial scenario 证据，但没有新的长期机制。<!-- delta:SF-ROBOTRUSTBENCH-WORLD-MODEL:end -->
<!-- books-review:SF-ROBOTRUSTBENCH-WORLD-MODEL:start -->existing:SF-ROBOTRUSTBENCH-WORLD-MODEL Ch25 已明确 video quality 不证明 controllable transition；delta:SF-ROBOTRUSTBENCH-WORLD-MODEL 只是扩展 scenario/evaluator。Ch24 owns generation factorization，Ch26 owns physical execution，均不拥有 world-model truth contract，故 No Change。<!-- books-review:SF-ROBOTRUSTBENCH-WORLD-MODEL:end -->
<!-- existing:SF-EXECUTION-GROUNDED-CODING-AGENT-SECURITY:start -->安全章节已区分 proposal、authorization、execution 与 observation。<!-- existing:SF-EXECUTION-GROUNDED-CODING-AGENT-SECURITY:end -->
<!-- delta:SF-EXECUTION-GROUNDED-CODING-AGENT-SECURITY:start -->把 filesystem/runtime side effect predicate 固化为 coding-agent release test，而非用 language refusal 代替。<!-- delta:SF-EXECUTION-GROUNDED-CODING-AGENT-SECURITY:end -->
<!-- books-review:SF-EXECUTION-GROUNDED-CODING-AGENT-SECURITY:start -->Root 已完成最小串行写回；当前 owner 与相邻章节、正文机制及 exact-v1 Review note 已通过 post-write audit。<!-- books-review:SF-EXECUTION-GROUNDED-CODING-AGENT-SECURITY:end -->
<!-- existing:SF-OPTCC-ASYMMETRIC-ALLREDUCE:start -->Ch36 只具体比较正常拓扑下的 collective。<!-- existing:SF-OPTCC-ASYMMETRIC-ALLREDUCE:end -->
<!-- delta:SF-OPTCC-ASYMMETRIC-ALLREDUCE:start -->增加退化链路仍在线时的 bandwidth-state schedule 与下界。<!-- delta:SF-OPTCC-ASYMMETRIC-ALLREDUCE:end -->
<!-- books-review:SF-OPTCC-ASYMMETRIC-ALLREDUCE:start -->existing:SF-OPTCC-ASYMMETRIC-ALLREDUCE Ch36 只比较对称 topology 下 collective；delta:SF-OPTCC-ASYMMETRIC-ALLREDUCE 增加退化链路仍在线时的 bandwidth-state schedule 与 lower-bound contract，已写入 Ch36“非对称链路下”段。Ch37 owns tensor partition，Ch40 owns integrated runtime，不拥有 collective algorithm。<!-- books-review:SF-OPTCC-ASYMMETRIC-ALLREDUCE:end -->
<!-- existing:SF-GAIATRACE-VIDUR-AGENT:start -->调度已按 request/token/runtime state 建模。<!-- existing:SF-GAIATRACE-VIDUR-AGENT:end -->
<!-- delta:SF-GAIATRACE-VIDUR-AGENT:start -->Agentic serving 的 SLO owner 必须上移到 task DAG；per-query TTFT/TPOT 只能作为子阶段证据。<!-- delta:SF-GAIATRACE-VIDUR-AGENT:end -->
<!-- books-review:SF-GAIATRACE-VIDUR-AGENT:start -->Root 已完成最小串行写回；当前 owner 与相邻章节、正文机制及 exact-v1 Review note 已通过 post-write audit。<!-- books-review:SF-GAIATRACE-VIDUR-AGENT:end -->
<!-- existing:SF-SPARSEX-SEGMENT-KV:start -->Ch45 的复用基线是 identity-compatible identical prefix。<!-- existing:SF-SPARSEX-SEGMENT-KV:end -->
<!-- delta:SF-SPARSEX-SEGMENT-KV:start -->增加 position-aligned segment reuse、selective correction 与 dense fallback。<!-- delta:SF-SPARSEX-SEGMENT-KV:end -->
<!-- books-review:SF-SPARSEX-SEGMENT-KV:start -->existing:SF-SPARSEX-SEGMENT-KV Ch45 只明确 identical-prefix reuse；delta:SF-SPARSEX-SEGMENT-KV 增加非前缀 segment 的 position-aligned reuse、selective correction 与 dense fallback，已写入 Prefix reuse 后的 Segment Reuse 段。Ch43 owns Prefill compute，Ch47 owns block allocation，不拥有 logical cache identity。<!-- books-review:SF-SPARSEX-SEGMENT-KV:end -->
<!-- existing:SF-ADAPTIVE-AUTO-HARNESS:start -->Ch84 已要求 harness、policy、tool schema 与 evaluation run 版本化；Ch81/Ch82 分别拥有 durable execution state 和协作边界。<!-- existing:SF-ADAPTIVE-AUTO-HARNESS:end -->
<!-- delta:SF-ADAPTIVE-AUTO-HARNESS:start -->单一 harness 在固定 benchmark 上反复优化时合理，但 open-ended task stream 会累积 history、domain shift 与 specialization conflict。<!-- delta:SF-ADAPTIVE-AUTO-HARNESS:end -->
<!-- books-review:SF-ADAPTIVE-AUTO-HARNESS:start -->比较 Ch84 与 workflow/multi-agent 边界后确认：open-ended task stream 需要把 harness history、specialization route、human intervention 与 rollback 作为 platform state，而非一次 benchmark 配置；已写入 Ch84 Adaptive Harness 段。<!-- books-review:SF-ADAPTIVE-AUTO-HARNESS:end -->
<!-- existing:SF-CONSERVE-CONVERSATION-PLACEMENT:start -->Ch56 已区分 routing、placement、iteration scheduling 与 KV locality，却主要按 request/turn 组织。<!-- existing:SF-CONSERVE-CONVERSATION-PLACEMENT:end -->
<!-- delta:SF-CONSERVE-CONVERSATION-PLACEMENT:start -->补 conversation-lifetime placement：一次 KV transfer 后固定 decoder，以可观察 state 取代逐 turn prediction。<!-- delta:SF-CONSERVE-CONVERSATION-PLACEMENT:end -->
<!-- books-review:SF-CONSERVE-CONVERSATION-PLACEMENT:start -->existing:SF-CONSERVE-CONVERSATION-PLACEMENT Ch56 已有 routing/placement/KV locality，但缺 conversation-lifetime owner；delta:SF-CONSERVE-CONVERSATION-PLACEMENT 应插在 request placement 后。Ch45 owns cache identity，Ch55 owns PD transfer，均不决定会话全生命周期 placement。<!-- books-review:SF-CONSERVE-CONVERSATION-PLACEMENT:end -->
<!-- existing:SF-COMPRESSION-UNCERTAINTY:start -->Ch66 已把 EvalSpec、calibration、slice、release threshold 与 rollback evidence 绑定；Ch67/Ch73 承接线上 drift 与生产 gate。<!-- existing:SF-COMPRESSION-UNCERTAINTY:end -->
<!-- delta:SF-COMPRESSION-UNCERTAINTY:start -->压缩评估通常只比较 accuracy/perplexity，却可能遗漏置信集合扩大与 selective-risk 变化。<!-- delta:SF-COMPRESSION-UNCERTAINTY:end -->
<!-- books-review:SF-COMPRESSION-UNCERTAINTY:start -->比较 Ch66/Ch67/Ch73 后确认：压缩 release 不能只守 accuracy/perplexity，还需同时比较 coverage、set size/selective risk 与 calibration drift；这是 Ch66 的 evaluation-contract 补全。<!-- books-review:SF-COMPRESSION-UNCERTAINTY:end -->
<!-- existing:SF-ASYNC-INFERENCE-OVERHEADS:start -->Ch42 已描述长期 request state machine，但没有展开 host/control non-scalable fraction 如何限制 TP。<!-- existing:SF-ASYNC-INFERENCE-OVERHEADS:end -->
<!-- delta:SF-ASYNC-INFERENCE-OVERHEADS:start -->补 scheduling/I/O overlap、sequence-parallel sampling 与 Amdahl optimal-TP 边界。<!-- delta:SF-ASYNC-INFERENCE-OVERHEADS:end -->
<!-- books-review:SF-ASYNC-INFERENCE-OVERHEADS:start -->existing:SF-ASYNC-INFERENCE-OVERHEADS Ch42 只描述请求状态机；delta:SF-ASYNC-INFERENCE-OVERHEADS 补 TP 扩展时 host/control non-scalable fraction 与 overlap，已写入 Engine loop 与指标定义之间。Ch49 owns kernel plan，Ch50 owns concrete vLLM engine，均不拥有全局 request-lifecycle cost decomposition。<!-- books-review:SF-ASYNC-INFERENCE-OVERHEADS:end -->
<!-- existing:SF-DRIFT-TELBENCH:start -->Ch66 已要求 process diagnosis，而非只看 final score。<!-- existing:SF-DRIFT-TELBENCH:end -->
<!-- delta:SF-DRIFT-TELBENCH:start -->补 outcome→span→first harmful commitment→claim propagation。<!-- delta:SF-DRIFT-TELBENCH:end -->
<!-- books-review:SF-DRIFT-TELBENCH:start -->existing:SF-DRIFT-TELBENCH Ch66 已要求过程诊断；delta:SF-DRIFT-TELBENCH 补 outcome→span→first harmful commitment→claim propagation 且强调 locator 非 root-cause truth，已与 LLMFI 合并写入 Failure Localization 段。Ch69 owns trace transport，Ch80 owns agent retry policy，不拥有 evaluation truth。<!-- books-review:SF-DRIFT-TELBENCH:end -->
<!-- existing:SF-CONSENT-INTEGRITY:start -->Ch72 已要求 intent、policy、approval 与 effect 可回溯；Ch78/Ch83 拥有 action proposal 与 protocol envelope。<!-- existing:SF-CONSENT-INTEGRITY:end -->
<!-- delta:SF-CONSENT-INTEGRITY:start -->由 agent 自己撰写 approval summary 时，人批准的是可伪造 narration 而非真实 action。<!-- delta:SF-CONSENT-INTEGRITY:end -->
<!-- books-review:SF-CONSENT-INTEGRITY:start -->比较 Ch72/Ch78/Ch83 后确认：approval UI 必须由 trusted renderer 从 executable action 生成并 bind-to-execution；无法检查时应降级或拒绝，而非让 agent narration 代理真实效果。该机制归 Ch72。<!-- books-review:SF-CONSENT-INTEGRITY:end -->
<!-- existing:SF-DFLARE-DIFFUSION-SPECULATION:start -->Ch48 已写 parallel diffusion draft、target verification 与 rollback。<!-- existing:SF-DFLARE-DIFFUSION-SPECULATION:end -->
<!-- delta:SF-DFLARE-DIFFUSION-SPECULATION:start -->增加 per-draft-layer target-feature fusion 作为扩大 draft capacity 的机制与成本。<!-- delta:SF-DFLARE-DIFFUSION-SPECULATION:end -->
<!-- books-review:SF-DFLARE-DIFFUSION-SPECULATION:start -->existing:SF-DFLARE-DIFFUSION-SPECULATION Ch48 已有 diffusion proposal 与 target verification；delta:SF-DFLARE-DIFFUSION-SPECULATION 增加 layer-wise target feature injection、draft-depth scaling 和 data coupling。Ch24 owns generation factorization，Ch50 owns runtime implementation，均不拥有 speculation acceptance contract。<!-- books-review:SF-DFLARE-DIFFUSION-SPECULATION:end -->
<!-- existing:SF-STRAGGLER-AWARE-RL-GROUP:start -->Ch33 已拥有 group-relative objective、rollout state 与 stale-policy boundary。<!-- existing:SF-STRAGGLER-AWARE-RL-GROUP:end -->
<!-- delta:SF-STRAGGLER-AWARE-RL-GROUP:start -->增加在保持同步 on-policy 下按 posterior straggler risk 动态选择 group size。<!-- delta:SF-STRAGGLER-AWARE-RL-GROUP:end -->
<!-- books-review:SF-STRAGGLER-AWARE-RL-GROUP:start -->existing:SF-STRAGGLER-AWARE-RL-GROUP Ch33 已拥有 group statistics/rollout invariants；delta:SF-STRAGGLER-AWARE-RL-GROUP 增加同步 group-size controller 和 risk budget。Ch32 owns PPO objective，Ch41 owns distributed framework，均不拥有 GRPO group semantics。<!-- books-review:SF-STRAGGLER-AWARE-RL-GROUP:end -->
<!-- existing:SF-SECLAW-SPEC-DRIVEN-SECURITY:start -->安全章节要求 sandbox、least privilege 与 effect-level evidence。<!-- existing:SF-SECLAW-SPEC-DRIVEN-SECURITY:end -->
<!-- delta:SF-SECLAW-SPEC-DRIVEN-SECURITY:start -->未形成超出现有 security EvalSpec 的已验证长期结论；保留为 preliminary implementation case。<!-- delta:SF-SECLAW-SPEC-DRIVEN-SECURITY:end -->
<!-- books-review:SF-SECLAW-SPEC-DRIVEN-SECURITY:start -->Fresh current-tree comparison 确认现有 owner 已覆盖该长期命题，无 Books mutation；No Change handoff 已通过 post-write audit。<!-- books-review:SF-SECLAW-SPEC-DRIVEN-SECURITY:end -->
<!-- existing:SF-HARNESS1-EXTERNALIZED-STATE:start -->Ch75 已定义调用内 working context 与持久 memory 的边界。<!-- existing:SF-HARNESS1-EXTERNALIZED-STATE:end -->
<!-- delta:SF-HARNESS1-EXTERNALIZED-STATE:start -->补 policy decision 与可重建 bookkeeping 的 owner 分离。<!-- delta:SF-HARNESS1-EXTERNALIZED-STATE:end -->
<!-- books-review:SF-HARNESS1-EXTERNALIZED-STATE:start -->Ch75 已存在“Semantic Policy 与 Recoverable Bookkeeping 应分 Owner”，完整覆盖 policy action、versioned working state、bounded renderer、raw evidence 与 crash/replay 边界；本 family 作为既有机制的 exact-v1 evidence，不再重复写入。Ch76 owns retrieval，Ch77 owns persistent derived memory，不拥有单次 search harness working state。<!-- books-review:SF-HARNESS1-EXTERNALIZED-STATE:end -->
<!-- existing:SF-LLMFI-ERROR-PROPAGATION:start -->Ch66 已要求 fault campaign 绑定 subject、injection、scorer 与复现状态。<!-- existing:SF-LLMFI-ERROR-PROPAGATION:end -->
<!-- delta:SF-LLMFI-ERROR-PROPAGATION:start -->补 LLM inference 中 layer/operation/token/task 的 propagation chain 与 mitigation evidence boundary。<!-- delta:SF-LLMFI-ERROR-PROPAGATION:end -->
<!-- books-review:SF-LLMFI-ERROR-PROPAGATION:start -->existing:SF-LLMFI-ERROR-PROPAGATION Ch66 已有 fault injection，但未沿 LLM inference layer/operator/token/task 写 propagation；delta:SF-LLMFI-ERROR-PROPAGATION 已与 DRIFT 合并写入 Failure Localization。Ch67 owns telemetry，Ch42 owns normal request lifecycle，均不拥有 evaluation fault model。<!-- books-review:SF-LLMFI-ERROR-PROPAGATION:end -->
<!-- existing:SF-PEFT-SCALE:start -->Ch59 已拥有 adapter identity、revision、evaluation 与 residency。<!-- existing:SF-PEFT-SCALE:end -->
<!-- delta:SF-PEFT-SCALE:start -->Scale Up/Down/Out 只重新组织同一长期合同。<!-- delta:SF-PEFT-SCALE:end -->
<!-- books-review:SF-PEFT-SCALE:start -->existing:SF-PEFT-SCALE Ch59 已拥有 adapter identity、revision、evaluation 与 residency；delta:SF-PEFT-SCALE 只是 Scale Up/Down/Out 的重新组织。Ch30 owns training mechanism，Ch61 owns deployment，不拥有 population registry。<!-- books-review:SF-PEFT-SCALE:end -->
<!-- existing:SF-GHOST-TOOL-ISSUE-PRIVACY:start -->Ch72 已把 model proposal 与 effect-time authorization 分开，但未单列 speculative observation disclosure。<!-- existing:SF-GHOST-TOOL-ISSUE-PRIVACY:end -->
<!-- delta:SF-GHOST-TOOL-ISSUE-PRIVACY:start -->增加 issue-time observation effect：外部调用发送即泄露，commit-time cleanup 不能撤回。<!-- delta:SF-GHOST-TOOL-ISSUE-PRIVACY:end -->
<!-- books-review:SF-GHOST-TOOL-ISSUE-PRIVACY:start -->existing:SF-GHOST-TOOL-ISSUE-PRIVACY Ch72 已有 effect-time authorization；delta:SF-GHOST-TOOL-ISSUE-PRIVACY 增加 external observation 在 dispatch 时已 commit 的 privacy contract。Ch78 owns call schema，Ch81 owns durable workflow，不拥有平台 privacy authority。<!-- books-review:SF-GHOST-TOOL-ISSUE-PRIVACY:end -->
<!-- existing:SF-SKILLHARM-LIFECYCLE:start -->Ch72 已覆盖 skill provenance、signature、least privilege、sandbox 与 revoke；Ch78/Ch83 提供 invocation/MCP handoff。<!-- existing:SF-SKILLHARM-LIFECYCLE:end -->
<!-- delta:SF-SKILLHARM-LIFECYCLE:start -->一次 session 的 poisoned skill 测试会漏掉 persistent package 被静默改写后在未来复用触发的 harm。<!-- delta:SF-SKILLHARM-LIFECYCLE:end -->
<!-- books-review:SF-SKILLHARM-LIFECYCLE:start -->比较 Ch72/Ch78/Ch83 后确认：现有边界偏向单次 invocation，尚未明确持久 skill 被修改、复用与跨 session 传播时的 lifecycle receipt；已写入 Ch72 的持久 Skill supply-chain 路线。<!-- books-review:SF-SKILLHARM-LIFECYCLE:end -->
<!-- existing:SF-COSMOS3-OMNIMODAL:start -->Ch25 已分离 reason、execute 与 render 的状态责任。<!-- existing:SF-COSMOS3-OMNIMODAL:end -->
<!-- delta:SF-COSMOS3-OMNIMODAL:start -->统一 MoT interface 仍保留不同输出 owner，作为新受限证据。<!-- delta:SF-COSMOS3-OMNIMODAL:end -->
<!-- books-review:SF-COSMOS3-OMNIMODAL:start -->Ch25 已存在“把 Reason、Execute 与 Render 拆成不同状态责任”，并明确 executable transition、visual proxy、renderer、代码安全与 state/proxy drift；统一接口只是该分层的受限实现，不形成新的长期 owner delta。Ch24 owns factorization，Ch26 owns physical control。<!-- books-review:SF-COSMOS3-OMNIMODAL:end -->
<!-- existing:SF-CROWDED-EMBEDDING-EXTERNALITY:start -->RAG 已要求 index/version/provenance 与 retrieval metric。<!-- existing:SF-CROWDED-EMBEDDING-EXTERNALITY:end -->
<!-- delta:SF-CROWDED-EMBEDDING-EXTERNALITY:start -->把 corpus population density 与 cross-tenant crowding 作为共享 index failure mode 和 release monitor。<!-- delta:SF-CROWDED-EMBEDDING-EXTERNALITY:end -->
<!-- books-review:SF-CROWDED-EMBEDDING-EXTERNALITY:start -->Root 已完成最小串行写回；当前 owner 与相邻章节、正文机制及 exact-v1 Review note 已通过 post-write audit。<!-- books-review:SF-CROWDED-EMBEDDING-EXTERNALITY:end -->
<!-- existing:SF-ECHELON-AGGREGATE-ONLY-ADAPTATION:start -->分布式训练按 model/optimizer/gradient state 与 communication 拆分。<!-- existing:SF-ECHELON-AGGREGATE-ONLY-ADAPTATION:end -->
<!-- delta:SF-ECHELON-AGGREGATE-ONLY-ADAPTATION:start -->新增 administrative boundary 作为不可跨越的数据/状态 owner，并把 typed aggregate 与 audit log 变成训练协议。<!-- delta:SF-ECHELON-AGGREGATE-ONLY-ADAPTATION:end -->
<!-- books-review:SF-ECHELON-AGGREGATE-ONLY-ADAPTATION:start -->Root 已完成最小串行写回；当前 owner 与相邻章节、正文机制及 exact-v1 Review note 已通过 post-write audit。<!-- books-review:SF-ECHELON-AGGREGATE-ONLY-ADAPTATION:end -->
<!-- existing:SF-GATEAI-OPERATING-POINT-EVAL:start -->EvalSpec 已要求 dataset/version/threshold/evaluator 与 release gate 绑定。<!-- existing:SF-GATEAI-OPERATING-POINT-EVAL:end -->
<!-- delta:SF-GATEAI-OPERATING-POINT-EVAL:start -->提供具体的 grouped-split、matched-FPR 与 contamination disclosure 实例。<!-- delta:SF-GATEAI-OPERATING-POINT-EVAL:end -->
<!-- books-review:SF-GATEAI-OPERATING-POINT-EVAL:start -->Fresh current-tree comparison 确认现有 owner 已覆盖该长期命题，无 Books mutation；No Change handoff 已通过 post-write audit。<!-- books-review:SF-GATEAI-OPERATING-POINT-EVAL:end -->
<!-- existing:SF-KFORGE-CROSS-PLATFORM-KERNEL:start -->Ch49 已把 compile、profile、kernel search、target hardware 与 executable validation 绑定到 execution plan。<!-- existing:SF-KFORGE-CROSS-PLATFORM-KERNEL:end -->
<!-- delta:SF-KFORGE-CROSS-PLATFORM-KERNEL:start -->双 Agent 迭代只是现有 compile/profile/verify loop 的实现案例。<!-- delta:SF-KFORGE-CROSS-PLATFORM-KERNEL:end -->
<!-- books-review:SF-KFORGE-CROSS-PLATFORM-KERNEL:start -->existing:SF-KFORGE-CROSS-PLATFORM-KERNEL Ch49 已拥有 target/backend/shape/dtype/compiler/profile/executable-verifier chain；delta:SF-KFORGE-CROSS-PLATFORM-KERNEL 只是 collaborative-agent implementation。Ch66 owns benchmark verdict，Ch56 owns fleet placement，均不拥有 kernel plan，故 No Change。<!-- books-review:SF-KFORGE-CROSS-PLATFORM-KERNEL:end -->
<!-- existing:SF-ASYMCACHE-MULTI-SEGMENT:start -->Ch45 已把 logical utility 映射到 physical page eviction，并保留 recoverable tiering。<!-- existing:SF-ASYMCACHE-MULTI-SEGMENT:end -->
<!-- delta:SF-ASYMCACHE-MULTI-SEGMENT:start -->Multi-Segment Attention 提供 kernel-cost-aware residency 案例，不改变 cache owner。<!-- delta:SF-ASYMCACHE-MULTI-SEGMENT:end -->
<!-- books-review:SF-ASYMCACHE-MULTI-SEGMENT:start -->existing:SF-ASYMCACHE-MULTI-SEGMENT Ch45 已有 logical utility 到 physical eviction 与 kernel compatibility；delta:SF-ASYMCACHE-MULTI-SEGMENT 是 MSA/adaptive-chunk 实例。Ch47 owns block allocator，Ch49 owns kernels，均不拥有 logical cache lifecycle，故 No Change。<!-- books-review:SF-ASYMCACHE-MULTI-SEGMENT:end -->
<!-- existing:SF-DRIFTSCHED-TOKEN-DRIFT:start -->Ch56 已要求 length predictor/calibration loop 消费 actual completion，并保留 fairness。<!-- existing:SF-DRIFTSCHED-TOKEN-DRIFT:end -->
<!-- delta:SF-DRIFTSCHED-TOKEN-DRIFT:start -->补 admission estimate 与 runtime token drift 的持续 reconciliation、SJF/aging coexistence。<!-- delta:SF-DRIFTSCHED-TOKEN-DRIFT:end -->
<!-- books-review:SF-DRIFTSCHED-TOKEN-DRIFT:start -->existing:SF-DRIFTSCHED-TOKEN-DRIFT Ch56 要求 predictor 由 actual completion 校准；delta:SF-DRIFTSCHED-TOKEN-DRIFT 补显式 drift state、SJF/aging trade-off 与反馈周期。Ch46 owns iteration batching，Ch66 owns calibration evidence，均不拥有 queue policy。<!-- books-review:SF-DRIFTSCHED-TOKEN-DRIFT:end -->
<!-- audit-target:books:end -->

<!-- audit-target:evidence:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260602-V3-COVERAGE | fresh-context:jun02-postwrite-v4 | coverage | audit-target:coverage | — | — | passed |
| SA-20260602-V2-EVIDENCE | fresh-context:jun02-postwrite-v4 | evidence | audit-target:evidence | — | — | passed |
| SA-20260602-V2-SELECTION | fresh-context:jun02-postwrite-v4 | deep_analysis_selection | audit-target:deep_analysis_selection | — | — | passed |
| SA-20260602-V2-BOOKS | fresh-context:jun02-postwrite-v4 | books | audit-target:books | — | 14 条 exact-v1 Review notes 已写入 Ch33/36/42/45/48/56/66/72/84，并由 POST_WRITE_FRESH_AUDIT_V4 targeted recheck 逐条验收 | passed |

Identity/date 736/736、title+abstract denominator FP/FN 736/736、Evidence 28/28 complete；ordinary pending=0、blocked=0。Score V2、RP、Benchmark Contract、Selection 与 Books Comparison 均仅对最终 denominator 重建。独立 post-write audit 已完成 22/22 marker、5/5 新 integration、28 retained 与 708 closures；唯一 traceability finding 在 14 条 exact-v1 Review notes 补齐并复核后关闭。

## 8. Ignored Noise

708 项不是静默删除：其 official identity、摘要 digest、closure class 与 family-specific semantic challenge 均保存在 `../_sources/daily-20260602/screening-ledger-v3-fresh.tsv`。ROADMAP 可映射、AI 相关、局部方法改进或单领域 benchmark 本身不足以进入 denominator。

## 9. Recommended Action

19 项 Source Family 的 Books Decision 已完成写回：12 项既有 marker 按 exact-v1 evidence 保留，两项机制边界已修正，四项来自降级 family 的专属机制已撤回，四项需重新举证的文字已删除或降级为显式设计合同；五项真正新增的长期结论分别进入 `INFER-KV-CACHE`、`PLATFORM-SECURITY`、`INFER-SCHEDULING`、`AGENT-RAG` 与 `TRAIN-DISTRIBUTED-TRAINING`。具体变更与证据边界记录在 `../_sources/daily-20260602/ROOT_BOOKS_RECONCILIATION_V3.md`；独立验收记录在 `../_sources/daily-20260602/POST_WRITE_FRESH_AUDIT_V4.md`。Books Gate 已在 14 条 retained/revised marker 的 exact-v1 Review notes 补齐并 targeted recheck 后通过。

## 10. Repository Changes

- 新增 736-row identity provenance、strict denominator audit、strict screening ledger、owner recovery ledger、Evidence/Books Comparison receipt、22-marker fresh audit 与 root Books reconciliation receipt。
- 通过官方 exact-v1 PDF 恢复两项先前 blocked family；当前材料 blocker 为 0。
- 已按 marker audit 修正/撤回错误吸收，并把五项新长期结论写入 Ch36、Ch45、Ch56、Ch72 与 Ch76；Ch33、Ch48、Ch49、Ch66 的边界同步收紧，Ch26 的无 owner 机制已移除。
- 新增独立 post-write audit；22/22 marker、5/5 新 integration、28 retained 与 708 closures 均已验收，14 条 Review-note traceability finding 已修复并复核。
- 本 Daily 为 `Complete`；Coverage Gate 为 `Closed`，Evidence 与 Books Gate 均为 `Passed`。
- 未执行 stage、commit 或 push。

## 11. Open Questions

1. agent task-level SLO 如何与 query TTFT/TPOT、tool latency 和 success probability 建立可分解 budget？
2. KV precision artifact 的 safety evaluator 应按 model/revision/quantizer 如何版本化，才能避免统一 safe bit-width 假设？

## 12. Sources

- Strict identity/denominator packet: `../_sources/daily-20260602/`
- Alignment Collapse Under KV Cache Quantization: Diagnosis and Mitigation: https://arxiv.org/pdf/2606.09864v1
- Defenses & Enablers For Skill Injection Attacks on Terminal Based Agents: https://arxiv.org/html/2606.01567v1
- RoboTrustBench: Benchmarking the Trustworthiness of Video World Models for Robotic Manipulation: https://arxiv.org/html/2606.01600v1
- Execution-Grounded Security Testing for Coding Agents in Software Engineering Pipelines: https://arxiv.org/html/2607.22569v1
- Don't Let a Few Network Failures Slow the Entire AllReduce: https://arxiv.org/html/2606.01680v1
- Characterization of Multi-Model Agentic AI Systems on General Tasks via Trace-Driven Simulation: https://arxiv.org/html/2606.01725v1
- SparseX: Efficient Segment-Level KV Cache Sharing for Interleaved LLM Serving: https://arxiv.org/html/2606.01751v1
- Adaptive Auto-Harness: Sustained Self-Improvement for Agentic System Deployment on Open-Ended Task Streams: https://arxiv.org/html/2606.01770v1
- Observation, Not Prediction: Conversation-Level Disaggregated Scheduling for Agentic Serving: https://arxiv.org/html/2606.01839v1
- Does Compression Preserve Uncertainty? A Unified Benchmark for Quantized and Sparse LLMs via Conformal Prediction: https://arxiv.org/html/2606.01850v1
- Scaling LLM Inference Beyond Amdahl`s Limits via Eliminating Non-Scalable Overheads: https://arxiv.org/html/2606.01927v1
- Where Do Deep-Research Agents Go Wrong? Span-Level Error Localization in Agent Trajectories: https://arxiv.org/html/2606.02060v1
- What You Approve Is What Executes: Consent Integrity for Black-Box LLM Agents: https://arxiv.org/html/2606.02668v1
- DFlare: Scaling Up Draft Capacity for Block Diffusion Speculative Decoding: https://arxiv.org/html/2606.02091v1
- Faster Synchronous On-Policy RL via Straggler-Aware Group Sizing: https://arxiv.org/html/2606.02218v1
- SeClaw: Spec-Driven Security Task Synthesis for Evaluating Autonomous Agents: https://arxiv.org/html/2606.02302v1
- Harness-1: Reinforcement Learning for Search Agents with State-Externalizing Harnesses: https://arxiv.org/html/2606.02373v1
- Not All Errors Are Equal: A Systematic Study of Error Propagation in Large Language Model Inference: https://arxiv.org/html/2606.02430v1
- On the Scaling of PEFT: Towards Million Personal Models of Trillion Parameters: https://arxiv.org/html/2606.02437v1
- Ghost Tool Calls: Issue-Time Privacy for Speculative Agent Tools: https://arxiv.org/html/2606.02483v1
- SkillHarm: Lifecycle-Aware Skill-Based Attacks via Automated Construction: https://arxiv.org/html/2606.02540v1
- Cosmos 3: Omnimodal World Models for Physical AI: https://arxiv.org/html/2606.02800v1
- The Crowded Embedding Space: A Mean-Field Mechanism for Emergent Marginalization in Retrieval-Augmented Agents: https://arxiv.org/pdf/2606.28343v1
- Echelon: Auditable Aggregate-Only Language-Model Adaptation Across Privacy Boundaries: https://arxiv.org/html/2606.02958v1
- Gate AI: LLM Security Benchmark Evaluation Methodology and Results: https://arxiv.org/html/2606.02959v1
- KForge: LLM-Driven Cross-Platform Kernel Generation for AI Accelerators: https://arxiv.org/html/2606.02963v1
- Multi-Segment Attention: Enabling Efficient KV-Cache Management for Faster Large Language Model Serving: https://arxiv.org/html/2606.02964v1
- DriftSched: Adaptive QoS-Aware Scheduling under Runtime Token Drift for Multi-Tenant GPU Inference: https://arxiv.org/html/2606.02982v1

## 13. Final Status

Daily V2.1 的 Coverage、Evidence、Deep Analysis Selection 与 Books Decision 均已完成；fresh-context Semantic Audit 无未解决 finding，三个 Gate 均已闭合。
