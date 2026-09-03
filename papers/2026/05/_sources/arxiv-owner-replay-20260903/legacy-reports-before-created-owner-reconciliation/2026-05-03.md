# Daily Research — 2026-05-03

**Research Date:** 2026-05-03

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-05-02 09:00:00 ～ 2026-05-03 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；月快照只承担 identity/date recall，机制 claim 绑定 exact arXiv v1

**Status:** Complete；Coverage=Closed；Evidence=Passed；Books=Passed；独立 Semantic Audit 与 Books post-write audit 均已通过

## Executive Summary

完整月度快照含 31,604 条唯一 DOI；严格窗口 raw identity=512，注册类别命中 274。Core Daily 180 条与 keyword-category 94 条均完成 title+abstract 语义筛选；author-side false-negative audit 纠正 16 项后，独立 reviewer 又重放 274/274，确认冻结 36 个候选（13.14%），238 项形成具名 pre-denominator closure。36/36 exact-v1 Review、Score V2 与 current-Books Comparison 已复核；19 项已写入 canonical Books owner，16 项 No Change，1 项 Structural Candidate。post-write reviewer 逐项确认 19/19 正文存在、均位于真实 `## Review notes` 前、演进语义完整且相邻 owner 冲突为 0；3 个后置降级与 Structural Candidate disposition 亦复核通过。blocked=0、ordinary pending=0，Coverage、Evidence、Deep Analysis Selection 与 Books Gate 全部闭合。

<!-- audit-target:coverage:start -->
## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-05-03 |
| Window End | 2026-05-03 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | DEN-20260503-V1 |
| Denominator Frozen At | 2026-08-31T20:55:00+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-05-02T09:00:00+08:00 | 2026-05-03T09:00:00+08:00 | 2026-08-31T20:55:00+08:00 | DataCite exact-month arXiv snapshot；19 registered categories；Core Daily full title+abstract screen | checked | 274 | SF-ATTACK-AGENT-TERMINAL-FINGERPRINT;SF-COMPUTE-OPTIMAL-TOKENIZATION;SF-SENTINEL-VLA-STATUS-CONTROL;SF-VLA-ADAPTIVE-TEST-TIME-COMPUTE;SF-TAIL-SAFE-RUNTIME-MONITOR;SF-VISUOMOTOR-EXECUTION-GUARANTEE;SF-GRBEN-PROCESS-REWARD-EVAL;SF-BROWSING-AGENT-BEHAVIORAL-FINGERPRINT;SF-ACTIVATION-GRADIENT-COMPRESSION;SF-PIXEL-LEVEL-RAG-EVIDENCE-CHAIN;SF-LOGIC-GROUNDED-SKILL-INDUCTION;SF-COUNTERFACTUAL-RISK-RAG;SF-CONFOUNDED-LOG-EVALUATION;SF-ACCESS-AWARE-VECTOR-INDEX;SF-VUDA-CUDA-VULKAN-SHARING;SF-LONG-FORM-LENGTH-VOLATILITY;SF-PROVENANCE-GRAPH-MEMORY;SF-LIVEFMBENCH-SPECIFICATION-EVAL;SF-AUTOREGRESSIVE-CREDIT-ATTRIBUTION-BARRIER;SF-LORA-COMPOSITION-RELIABILITY;SF-AUTONOMOUS-TEST-REPAIR-VALIDATION-BOUNDARY;SF-ACTION-AGENT-VIDEO-CONTROL;SF-NOTEBOOK-REPRODUCIBILITY-STATE-GATE;SF-MULTIAGENT-PARETO-COMPUTE-ALLOCATION;SF-DEVELOPER-MEMORY-OPE-GATE;SF-PRODUCTION-AGENT-EVALUATION;SF-DATA-CONSTRAINED-SCALING-LAW;SF-AGENT-SAFETY-SEARCH-MEASUREMENT;SF-AGENT-GENERATED-VERIFIED-COMPILER;SF-DITRON-DISTRIBUTED-TILING;SF-REFUSAL-TRAJECTORY-MONITOR;SF-RECURSIVE-STATE-TERMINATION;SF-PRUNING-BEHAVIORAL-REGRESSION;SF-SEQUENTIAL-MODEL-EDIT-SIDECAR;SF-POLICY-CARRIAGE-INTEGRITY;SF-QUANTIZATION-BEHAVIORAL-REGRESSION | pages=100; prefix=00..99; final_cursor=end; unique=31604; raw=512; screened=274; retained=36; closure=238 | 2026-05-03T00:55:02Z | sha256:6cd03445c68e6dee00d4a07d68591fddc305c9a3eb4b501ee249d00c547a5640 | — |

### Coverage Limitations

DataCite 只证明 identity/date recall；技术结论绑定 exact-v1。后加入注册表的其他来源不反推为本历史 Daily 的到期源。独立 reviewer 已重放 274/274 title+abstract、36 个 retained 与 238 个 pre-denominator closure；未发现新的 false negative 或 false positive，Coverage Gate 已关闭。
<!-- audit-target:coverage:end -->

<!-- audit-target:evidence:start -->
## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-ATTACK-AGENT-TERMINAL-FINGERPRINT | arXiv:2605.01186v1 | paper-v1:2605.01186 | 2026-W18 | 2026-05-02 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-ATTACK-AGENT-TERMINAL-FINGERPRINT | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-ATTACK-AGENT-TERMINAL-FINGERPRINT | yes |
| SF-COMPUTE-OPTIMAL-TOKENIZATION | arXiv:2605.01188v1 | paper-v1:2605.01188 | 2026-W18 | 2026-05-02 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-COMPUTE-OPTIMAL-TOKENIZATION | self | — | new_in_window | MODEL-TOKENIZER | Integrate | books-review:SF-COMPUTE-OPTIMAL-TOKENIZATION | yes |
| SF-SENTINEL-VLA-STATUS-CONTROL | arXiv:2605.01191v1 | paper-v1:2605.01191 | 2026-W18 | 2026-05-02 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-SENTINEL-VLA-STATUS-CONTROL | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Integrate | books-review:SF-SENTINEL-VLA-STATUS-CONTROL | yes |
| SF-VLA-ADAPTIVE-TEST-TIME-COMPUTE | arXiv:2605.01194v1 | paper-v1:2605.01194 | 2026-W18 | 2026-05-02 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-VLA-ADAPTIVE-TEST-TIME-COMPUTE | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Integrate | books-review:SF-VLA-ADAPTIVE-TEST-TIME-COMPUTE | yes |
| SF-TAIL-SAFE-RUNTIME-MONITOR | arXiv:2605.01195v1 | paper-v1:2605.01195 | 2026-W18 | 2026-05-02 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-TAIL-SAFE-RUNTIME-MONITOR | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Integrate | books-review:SF-TAIL-SAFE-RUNTIME-MONITOR | yes |
| SF-VISUOMOTOR-EXECUTION-GUARANTEE | arXiv:2605.01201v1 | paper-v1:2605.01201 | 2026-W18 | 2026-05-02 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-VISUOMOTOR-EXECUTION-GUARANTEE | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Integrate | books-review:SF-VISUOMOTOR-EXECUTION-GUARANTEE | yes |
| SF-GRBEN-PROCESS-REWARD-EVAL | arXiv:2605.01203v1 | paper-v1:2605.01203 | 2026-W18 | 2026-05-02 | SRC-ARXIV | 2 | 3 | 2 | 7 | retained | deep_complete | accessible | knowledge_gap | review:SF-GRBEN-PROCESS-REWARD-EVAL | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-GRBEN-PROCESS-REWARD-EVAL | yes |
| SF-BROWSING-AGENT-BEHAVIORAL-FINGERPRINT | arXiv:2605.01247v1 | paper-v1:2605.01247 | 2026-W18 | 2026-05-02 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-BROWSING-AGENT-BEHAVIORAL-FINGERPRINT | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-BROWSING-AGENT-BEHAVIORAL-FINGERPRINT | yes |
| SF-ACTIVATION-GRADIENT-COMPRESSION | arXiv:2605.01255v1 | paper-v1:2605.01255 | 2026-W18 | 2026-05-02 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-ACTIVATION-GRADIENT-COMPRESSION | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Integrate | books-review:SF-ACTIVATION-GRADIENT-COMPRESSION | yes |
| SF-PIXEL-LEVEL-RAG-EVIDENCE-CHAIN | arXiv:2605.01284v1 | paper-v1:2605.01284 | 2026-W18 | 2026-05-02 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-PIXEL-LEVEL-RAG-EVIDENCE-CHAIN | self | — | new_in_window | AGENT-RAG | Integrate | books-review:SF-PIXEL-LEVEL-RAG-EVIDENCE-CHAIN | yes |
| SF-LOGIC-GROUNDED-SKILL-INDUCTION | arXiv:2605.01293v1 | paper-v1:2605.01293 | 2026-W18 | 2026-05-02 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-LOGIC-GROUNDED-SKILL-INDUCTION | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-LOGIC-GROUNDED-SKILL-INDUCTION | yes |
| SF-COUNTERFACTUAL-RISK-RAG | arXiv:2605.01302v1 | paper-v1:2605.01302 | 2026-W18 | 2026-05-02 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-COUNTERFACTUAL-RISK-RAG | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-COUNTERFACTUAL-RISK-RAG | yes |
| SF-CONFOUNDED-LOG-EVALUATION | arXiv:2605.01311v1 | paper-v1:2605.01311 | 2026-W18 | 2026-05-02 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-CONFOUNDED-LOG-EVALUATION | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-CONFOUNDED-LOG-EVALUATION | yes |
| SF-ACCESS-AWARE-VECTOR-INDEX | arXiv:2605.01342v1 | paper-v1:2605.01342 | 2026-W18 | 2026-05-02 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-ACCESS-AWARE-VECTOR-INDEX | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-ACCESS-AWARE-VECTOR-INDEX | yes |
| SF-VUDA-CUDA-VULKAN-SHARING | arXiv:2605.01352v1 | paper-v1:2605.01352 | 2026-W18 | 2026-05-02 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-VUDA-CUDA-VULKAN-SHARING | self | — | new_in_window | PLATFORM-GPU-SCHEDULER | Integrate | books-review:SF-VUDA-CUDA-VULKAN-SHARING | yes |
| SF-LONG-FORM-LENGTH-VOLATILITY | arXiv:2605.01357v1 | paper-v1:2605.01357 | 2026-W18 | 2026-05-02 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-LONG-FORM-LENGTH-VOLATILITY | self | — | new_in_window | INFER-DECODE | Integrate | books-review:SF-LONG-FORM-LENGTH-VOLATILITY | yes |
| SF-PROVENANCE-GRAPH-MEMORY | arXiv:2605.01386v1 | paper-v1:2605.01386 | 2026-W18 | 2026-05-02 | SRC-ARXIV | 2 | 3 | 2 | 7 | retained | deep_complete | accessible | knowledge_gap | review:SF-PROVENANCE-GRAPH-MEMORY | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-PROVENANCE-GRAPH-MEMORY | yes |
| SF-LIVEFMBENCH-SPECIFICATION-EVAL | arXiv:2605.01394v1 | paper-v1:2605.01394 | 2026-W18 | 2026-05-02 | SRC-ARXIV | 2 | 3 | 2 | 7 | retained | deep_complete | accessible | knowledge_gap | review:SF-LIVEFMBENCH-SPECIFICATION-EVAL | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-LIVEFMBENCH-SPECIFICATION-EVAL | yes |
| SF-AUTOREGRESSIVE-CREDIT-ATTRIBUTION-BARRIER | arXiv:2605.01425v1 | paper-v1:2605.01425 | 2026-W18 | 2026-05-02 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-AUTOREGRESSIVE-CREDIT-ATTRIBUTION-BARRIER | self | — | new_in_window | AGENT-RAG | Integrate | books-review:SF-AUTOREGRESSIVE-CREDIT-ATTRIBUTION-BARRIER | yes |
| SF-LORA-COMPOSITION-RELIABILITY | arXiv:2605.01429v1 | paper-v1:2605.01429 | 2026-W18 | 2026-05-02 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-LORA-COMPOSITION-RELIABILITY | self | — | new_in_window | TRAIN-LORA | No Change — Existing Coverage | books-review:SF-LORA-COMPOSITION-RELIABILITY | yes |
| SF-AUTONOMOUS-TEST-REPAIR-VALIDATION-BOUNDARY | arXiv:2605.01471v1 | paper-v1:2605.01471 | 2026-W18 | 2026-05-02 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-AUTONOMOUS-TEST-REPAIR-VALIDATION-BOUNDARY | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-AUTONOMOUS-TEST-REPAIR-VALIDATION-BOUNDARY | yes |
| SF-ACTION-AGENT-VIDEO-CONTROL | arXiv:2605.01477v1 | paper-v1:2605.01477 | 2026-W18 | 2026-05-02 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-ACTION-AGENT-VIDEO-CONTROL | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-ACTION-AGENT-VIDEO-CONTROL | yes |
| SF-NOTEBOOK-REPRODUCIBILITY-STATE-GATE | arXiv:2605.01560v1 | paper-v1:2605.01560 | 2026-W18 | 2026-05-03 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-NOTEBOOK-REPRODUCIBILITY-STATE-GATE | self | — | new_in_window | AGENT-WORKFLOW | Integrate | books-review:SF-NOTEBOOK-REPRODUCIBILITY-STATE-GATE | yes |
| SF-MULTIAGENT-PARETO-COMPUTE-ALLOCATION | arXiv:2605.01566v1 | paper-v1:2605.01566 | 2026-W18 | 2026-05-03 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-MULTIAGENT-PARETO-COMPUTE-ALLOCATION | self | — | new_in_window | AGENT-MULTI-AGENT | Integrate | books-review:SF-MULTIAGENT-PARETO-COMPUTE-ALLOCATION | yes |
| SF-DEVELOPER-MEMORY-OPE-GATE | arXiv:2605.01567v1 | paper-v1:2605.01567 | 2026-W18 | 2026-05-03 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-DEVELOPER-MEMORY-OPE-GATE | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-DEVELOPER-MEMORY-OPE-GATE | yes |
| SF-PRODUCTION-AGENT-EVALUATION | arXiv:2605.01604v1 | paper-v1:2605.01604 | 2026-W18 | 2026-05-03 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-PRODUCTION-AGENT-EVALUATION | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-PRODUCTION-AGENT-EVALUATION | yes |
| SF-DATA-CONSTRAINED-SCALING-LAW | arXiv:2605.01640v1 | paper-v1:2605.01640 | 2026-W18 | 2026-05-03 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-DATA-CONSTRAINED-SCALING-LAW | self | — | new_in_window | TRAIN-PRETRAINING | No Change — Existing Coverage | books-review:SF-DATA-CONSTRAINED-SCALING-LAW | yes |
| SF-AGENT-SAFETY-SEARCH-MEASUREMENT | arXiv:2605.01644v1 | paper-v1:2605.01644 | 2026-W18 | 2026-05-03 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-AGENT-SAFETY-SEARCH-MEASUREMENT | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-AGENT-SAFETY-SEARCH-MEASUREMENT | yes |
| SF-AGENT-GENERATED-VERIFIED-COMPILER | arXiv:2605.01660v1 | paper-v1:2605.01660 | 2026-W18 | 2026-05-03 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-AGENT-GENERATED-VERIFIED-COMPILER | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-AGENT-GENERATED-VERIFIED-COMPILER | yes |
| SF-DITRON-DISTRIBUTED-TILING | arXiv:2605.02953v1 | paper-v1:2605.02953 | 2026-W18 | 2026-05-02 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-DITRON-DISTRIBUTED-TILING | self | — | new_in_window | INFER-TENSORRT-LLM | Integrate | books-review:SF-DITRON-DISTRIBUTED-TILING | yes |
| SF-REFUSAL-TRAJECTORY-MONITOR | arXiv:2605.02958v1 | paper-v1:2605.02958 | 2026-W18 | 2026-05-02 | SRC-ARXIV | 2 | 3 | 2 | 7 | retained | deep_complete | accessible | knowledge_gap | review:SF-REFUSAL-TRAJECTORY-MONITOR | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-REFUSAL-TRAJECTORY-MONITOR | yes |
| SF-RECURSIVE-STATE-TERMINATION | arXiv:2605.06690v1 | paper-v1:2605.06690 | 2026-W18 | 2026-05-02 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-RECURSIVE-STATE-TERMINATION | self | — | new_in_window | AGENT-REFLECTION | Integrate | books-review:SF-RECURSIVE-STATE-TERMINATION | yes |
| SF-PRUNING-BEHAVIORAL-REGRESSION | arXiv:2605.08137v1 | paper-v1:2605.08137 | 2026-W18 | 2026-05-02 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-PRUNING-BEHAVIORAL-REGRESSION | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-PRUNING-BEHAVIORAL-REGRESSION | yes |
| SF-SEQUENTIAL-MODEL-EDIT-SIDECAR | arXiv:2605.08143v1 | paper-v1:2605.08143 | 2026-W18 | 2026-05-02 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-SEQUENTIAL-MODEL-EDIT-SIDECAR | self | — | new_in_window | — | Structural Candidate | books-review:SF-SEQUENTIAL-MODEL-EDIT-SIDECAR | yes |
| SF-POLICY-CARRIAGE-INTEGRITY | arXiv:2605.12535v1 | paper-v1:2605.12535 | 2026-W18 | 2026-05-03 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-POLICY-CARRIAGE-INTEGRITY | self | — | new_in_window | AGENT-CONTEXT | Integrate | books-review:SF-POLICY-CARRIAGE-INTEGRITY | yes |
| SF-QUANTIZATION-BEHAVIORAL-REGRESSION | arXiv:2605.15208v1 | paper-v1:2605.15208 | 2026-W18 | 2026-05-02 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-QUANTIZATION-BEHAVIORAL-REGRESSION | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-QUANTIZATION-BEHAVIORAL-REGRESSION | yes |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-ATTACK-AGENT-TERMINAL-FINGERPRINT | RP-5890b4c15b531373 | deep | arXiv:2605.01186v1 | SRC-ARXIV@arXiv:2605.01186v1 | arXiv:2605.01186v1 — §2 Design Methodology; §2.1 Threat Model and Target Environment; §2.3 passive fingerprinting; §2.4 active forensics | arXiv:2605.01186v1 — §3 Evaluation Setup; §4 Evaluation Results; §5 Validation of Trace in the Wild | arXiv:2605.01186v1 — §6 Threats to Validity and Future Work — model/scaffold drift, mimicry/evasion, honeypot and payload scope | arXiv:2605.01186v1 — §3 reports evaluation scripts and a reproducibility notebook; full dataset and immutable reviewed commit Not Disclosed | claim:SF-ATTACK-AGENT-TERMINAL-FINGERPRINT | complete |
| SF-COMPUTE-OPTIMAL-TOKENIZATION | RP-dcd46882bcb76724 | deep | arXiv:2605.01188v1 | SRC-ARXIV@arXiv:2605.01188v1 | arXiv:2605.01188v1 — §2 Methodology; §3 Scaling Laws and Data Compression; Eq. (1)–(2) | arXiv:2605.01188v1 — §2.2 Training and Evaluation; §3.2/3.4 Results; §4–5 cross-tokenizer/language validation | arXiv:2605.01188v1 — §7.2 Limitations; Appendix B.4/B.5 sensitivity and confidence intervals | arXiv:2605.01188v1 — project page co-tok.github.io; immutable training artifact commit Not Disclosed | claim:SF-COMPUTE-OPTIMAL-TOKENIZATION | complete |
| SF-SENTINEL-VLA-STATUS-CONTROL | RP-1dfc6eb85cf2aafc | deep | arXiv:2605.01191v1 | SRC-ARXIV@arXiv:2605.01191v1 | arXiv:2605.01191v1 — §3 Sentinel-VLA; §3.1 Dynamic Reasoning via Active Status Monitor; Eq. (1)–(5); §3.3 SECL | arXiv:2605.01191v1 — §4 Experiments; §4.2 RLBench/LIBERO/real-world results; §4.3 monitor and SECL ablations | arXiv:2605.01191v1 — §4.1 disclosed models/tasks/control frequency; §5 Conclusion; no standalone limitations section | arXiv:2605.01191v1 — code, weights and EC-Gen pipeline announced for future release; immutable commit Not Disclosed | claim:SF-SENTINEL-VLA-STATUS-CONTROL | complete |
| SF-VLA-ADAPTIVE-TEST-TIME-COMPUTE | RP-82bb659d2cfa45fb | deep | arXiv:2605.01194v1 | SRC-ARXIV@arXiv:2605.01194v1 | arXiv:2605.01194v1 — §3 VLA inference; §4.1 uncertainty clutch; §4.2 TTC; §4.3 relative action critic | arXiv:2605.01194v1 — §5 Experiments; LIBERO-LONG; critic and clutch ablations | arXiv:2605.01194v1 — §6 Conclusion and experiment boundary; no standalone limitations section | arXiv:2605.01194v1 — code/weights announced for future release; immutable commit unavailable | claim:SF-VLA-ADAPTIVE-TEST-TIME-COMPUTE | complete |
| SF-TAIL-SAFE-RUNTIME-MONITOR | RP-1aa0ee44efff8a4f | deep | arXiv:2605.01195v1 | SRC-ARXIV@arXiv:2605.01195v1 | arXiv:2605.01195v1 — §II Problem Formulation; §IV reward/Q safe set and gradient recovery | arXiv:2605.01195v1 — §V Franka experiments; §V-D calibration analysis | arXiv:2605.01195v1 — §VI Limitations and Future Work | arXiv:2605.01195v1 — digital-twin pipeline described; immutable code/data commit Not Disclosed | claim:SF-TAIL-SAFE-RUNTIME-MONITOR | complete |
| SF-VISUOMOTOR-EXECUTION-GUARANTEE | RP-17a5cb4777f7abcb | deep | arXiv:2605.01201v1 | SRC-ARXIV@arXiv:2605.01201v1 | arXiv:2605.01201v1 — §3 set invariance and Nagumo theorem; §4 execution-guarantee definition; §5.1–5.3 safeset construction and recovery QP; Eq. (1)–(5) | arXiv:2605.01201v1 — §6 Experimental Evaluation; §6.1 simulation/real Franka setup; §6.2 clean, cluttered and OOD results | arXiv:2605.01201v1 — §7 Limitations and Future Work — goal-specific safeset, demonstration coverage assumption, no grasp feasibility, conservative recovery | arXiv:2605.01201v1 — exact-v1 describes construction and experiments; public implementation and immutable commit Not Disclosed | claim:SF-VISUOMOTOR-EXECUTION-GUARANTEE | complete |
| SF-GRBEN-PROCESS-REWARD-EVAL | RP-dde2131ccf3bd490 | deep | arXiv:2605.01203v1 | SRC-ARXIV@arXiv:2605.01203v1 | arXiv:2605.01203v1 — §3 benchmark construction, curation and annotation | arXiv:2605.01203v1 — §4 setup; 22-model PRM/LLM evaluation; error-type analysis | arXiv:2605.01203v1 — Limitations section after §5 | arXiv:2605.01203v1 — benchmark identity disclosed; immutable dataset commit Not Disclosed | claim:SF-GRBEN-PROCESS-REWARD-EVAL | complete |
| SF-BROWSING-AGENT-BEHAVIORAL-FINGERPRINT | RP-f9df789d3863f45d | deep | arXiv:2605.01247v1 | SRC-ARXIV@arXiv:2605.01247v1 | arXiv:2605.01247v1 — §4 Methodology; §4.2 honey website; §4.4 data collection; §4.5 featurization; §4.6 multi-class classification | arXiv:2605.01247v1 — §5 Characterizing Fingerprints; §5.1 classifier evaluation; §5.2 browser fingerprints; §5.3 behavioral fingerprints | arXiv:2605.01247v1 — §6 Discussion, Limitations, and Implications; §6.1 generalizability; §6.2 arms race; §6.3 real-time classification | arXiv:2605.01247v1 — §9 Data Availability; immutable reviewed dataset/code commit Not Disclosed | claim:SF-BROWSING-AGENT-BEHAVIORAL-FINGERPRINT | complete |
| SF-ACTIVATION-GRADIENT-COMPRESSION | RP-134a101ed1aad55f | deep | arXiv:2605.01255v1 | SRC-ARXIV@arXiv:2605.01255v1 | arXiv:2605.01255v1 — §3 theory; §3.2 linear/nonlinear bias boundary; §4 activation-gradient co-compression | arXiv:2605.01255v1 — §5 experiments and ablations; Appendix A; Qwen/LLaMA pretraining/SFT | arXiv:2605.01255v1 — §3.2 nonlinear counterexample; single A800-80GB BF16 setup; Appendix | arXiv:2605.01255v1 — supplementary code claimed; immutable commit Not Disclosed | claim:SF-ACTIVATION-GRADIENT-COMPRESSION | complete |
| SF-PIXEL-LEVEL-RAG-EVIDENCE-CHAIN | RP-e9627a4ced6f462b | deep | arXiv:2605.01284v1 | SRC-ARXIV@arXiv:2605.01284v1 | arXiv:2605.01284v1 — §3 Wiki-CoE Dataset; §3.2 bounding-box annotation; §4 Methodology; §4.2 candidate reasoning; §4.3 chain-structured evidence generation; §4.4 unified generation | arXiv:2605.01284v1 — §5 Experiment Setup; §6 Experimental Results; §6.2 reasoning type; §6.3 SlideVQA generalization; §6.4 ablations; §6.5 efficiency | Not Disclosed — exact-v1 has no standalone limitations section; claims are bounded to Wiki-CoE/SlideVQA, selected VLMs, screenshot candidates and author attribution metrics | arXiv:2605.01284v1 — dataset construction and model implementation are described; public immutable code/data commit Not Disclosed | claim:SF-PIXEL-LEVEL-RAG-EVIDENCE-CHAIN | complete |
| SF-LOGIC-GROUNDED-SKILL-INDUCTION | RP-1696931e09acafd6 | deep | arXiv:2605.01293v1 | SRC-ARXIV@arXiv:2605.01293v1 | arXiv:2605.01293v1 — §4 Neuro-Symbolic Skill Representation; §4.1 workflows; §4.2 node invention; §4.3 interactive control-flow semantics; §5 logic-grounded induction; Appendix A syntax/semantics | arXiv:2605.01293v1 — §6 Empirical Study; §6.1 setup/baselines; §6.2 main results; §6.3 modular skill honing | Not Disclosed — exact-v1 has no standalone limitations section; evidence is bounded to evaluated agentic tasks, induced language, planner/executor and held-out goals | arXiv:2605.01293v1 — Appendix A specifies representation language; public immutable implementation/data commit Not Disclosed | claim:SF-LOGIC-GROUNDED-SKILL-INDUCTION | complete |
| SF-COUNTERFACTUAL-RISK-RAG | RP-494cdf5ea1e4bea0 | deep | arXiv:2605.01302v1 | SRC-ARXIV@arXiv:2605.01302v1 | arXiv:2605.01302v1 — §3 Methodology; §3.1 counterfactual risk; §3.2 cognitive perturbation; §3.3 evidence critic; §3.4 abstention | arXiv:2605.01302v1 — §4 Experimental Setup; §5 Results; §5.2 risk-coverage; §5.4 ablation; §5.5 efficiency | arXiv:2605.01302v1 — §5.6 hyperparameter sensitivity; evaluated decision benchmarks and synthetic cognitive perturbations only | arXiv:2605.01302v1 — GitHub repository linked from exact-v1; reviewed immutable commit Not Disclosed | claim:SF-COUNTERFACTUAL-RISK-RAG | complete |
| SF-CONFOUNDED-LOG-EVALUATION | RP-77ba3dda9a616de4 | deep | arXiv:2605.01311v1 | SRC-ARXIV@arXiv:2605.01311v1 | arXiv:2605.01311v1 — §2 causal graph/data sources/assumptions; §3 identification theorem; §4 estimators | arXiv:2605.01311v1 — §5 semi-synthetic validation and cached summarization/coding benchmarks | arXiv:2605.01311v1 — §7 Scope and limitations; A1–A4, especially stateless single-round A4 | arXiv:2605.01311v1 — cached benchmark protocol disclosed; immutable artifact commit Not Disclosed | claim:SF-CONFOUNDED-LOG-EVALUATION | complete |
| SF-ACCESS-AWARE-VECTOR-INDEX | RP-d160348b0a215739 | deep | arXiv:2605.01342v1 | SRC-ARXIV@arXiv:2605.01342v1 | arXiv:2605.01342v1 — PDF §3 lattice/problem; §4 Veda; §5 EffVeda; §6 coordinated search | arXiv:2605.01342v1 — PDF §7 experiments including multi-role crossover Exp 13 | arXiv:2605.01342v1 — PDF §1 broad-query crossover; §7 workload boundary; §9 conclusion | arXiv:2605.01342v1 — author PDF v1; implementation commit Not Disclosed | claim:SF-ACCESS-AWARE-VECTOR-INDEX | complete |
| SF-VUDA-CUDA-VULKAN-SHARING | RP-68b9b0ef4a83e45c | deep | arXiv:2605.01352v1 | SRC-ARXIV@arXiv:2605.01352v1 | arXiv:2605.01352v1 — §2 execution isolation; §3 API; §4 channel redirection/page-table grafting | arXiv:2605.01352v1 — §5 embodied-AI simulation/RL workloads; utilization/throughput/latency | arXiv:2605.01352v1 — §6 discussion/conclusion; driver, GPU and CUDA/Vulkan trust boundary | arXiv:2605.01352v1 — kernel/driver modifications described; public immutable commit Not Disclosed | claim:SF-VUDA-CUDA-VULKAN-SHARING | complete |
| SF-LONG-FORM-LENGTH-VOLATILITY | RP-af5d620ab2c7f890 | deep | arXiv:2605.01357v1 | SRC-ARXIV@arXiv:2605.01357v1 | arXiv:2605.01357v1 — §3 VOLTBench; §5 attention-trace probe; §6 GLoBo | arXiv:2605.01357v1 — §4 repeated-run evaluation; §6.3 mitigation; Appendix tasks | Not Disclosed — exact-v1 has no standalone limitations section; scope is N=5, named tasks/judges/models and logits access | arXiv:2605.01357v1 — benchmark/task prompts disclosed; immutable code commit Not Disclosed | claim:SF-LONG-FORM-LENGTH-VOLATILITY | complete |
| SF-PROVENANCE-GRAPH-MEMORY | RP-b6f7603946aaff9e | deep | arXiv:2605.01386v1 | SRC-ARXIV@arXiv:2605.01386v1 | arXiv:2605.01386v1 — §3.1 session segmentation/selective compression; §3.2 provenance-enriched graph; §3.3 query-adaptive subgraph retrieval and weighted PageRank | arXiv:2605.01386v1 — §4.1–4.3 LOCOMO/LongMemEval setup, main results and ablations; Appendix B.1–B.5 robustness, cost and scalability | arXiv:2605.01386v1 — §Limitations — static entity linking, dynamic/ambiguous conversations, graph/LLM compute and memory overhead | arXiv:2605.01386v1 — public repository or immutable reviewed commit Not Disclosed | claim:SF-PROVENANCE-GRAPH-MEMORY | complete |
| SF-LIVEFMBENCH-SPECIFICATION-EVAL | RP-524897f32e40defa | deep | arXiv:2605.01394v1 | SRC-ARXIV@arXiv:2605.01394v1 | arXiv:2605.01394v1 — §2 study design; §3 contamination-aware benchmark construction | arXiv:2605.01394v1 — §4 setup, faithful-result filtering and failure analysis | arXiv:2605.01394v1 — §4 failure analysis; §5 discussion/conclusion and ACSL/C-program scope | arXiv:2605.01394v1 — HF dataset and evaluation artifacts disclosed; immutable revision pin Not Disclosed | claim:SF-LIVEFMBENCH-SPECIFICATION-EVAL | complete |
| SF-AUTOREGRESSIVE-CREDIT-ATTRIBUTION-BARRIER | RP-1818b529aefb33df | deep | arXiv:2605.01425v1 | SRC-ARXIV@arXiv:2605.01425v1 | arXiv:2605.01425v1 — §2 preliminaries; §3 CCA; §4 non-composition; §5 retrofitting lower bound | Not Required — exact-v1 is a theorem/construction paper with no empirical benchmark | Not Disclosed — limits are the autoregressive, black-box and optimality assumptions stated with the theorems | arXiv:2605.01425v1 — formal manuscript only; executable artifact Not Applicable | claim:SF-AUTOREGRESSIVE-CREDIT-ATTRIBUTION-BARRIER | complete |
| SF-LORA-COMPOSITION-RELIABILITY | RP-c646b450a7ced719 | deep | arXiv:2605.01429v1 | SRC-ARXIV@arXiv:2605.01429v1 | arXiv:2605.01429v1 — §Problem Formulation; §Method; Layer-Adaptive Sparse Residual Composition; Sparse-Composition Agreement Layer; Eq. (14)–(17) | arXiv:2605.01429v1 — §Experiments; Post-Retrieval Evidence; Ablation Studies; Discussion and Analysis; Appendix matched-protocol audit tables | arXiv:2605.01429v1 — §Limitations — matched FLAN-T5-Large/BBH/97-LoRA contract, protocol-distinct backbones, uncalibrated reliability proxy, multi-path cost | arXiv:2605.01429v1 — replication package fields are specified in §Limitations; public immutable package commit Not Disclosed | claim:SF-LORA-COMPOSITION-RELIABILITY | complete |
| SF-AUTONOMOUS-TEST-REPAIR-VALIDATION-BOUNDARY | RP-14335a7bc255c077 | deep | arXiv:2605.01471v1 | SRC-ARXIV@arXiv:2605.01471v1 | arXiv:2605.01471v1 — §3 System Architecture; §3.3 five-agent pipeline; §3.4 uncertainty propagation; §5 Observed Failure Modes; §8 Design Guidelines; §9 Controlled Autonomy Framework | arXiv:2605.01471v1 — §6 Quantitative Evaluation; 300 reports/636 test executions/10 scenario families; §6.3 convergence; §6.5 failure signatures; §6.6 self-correction | arXiv:2605.01471v1 — §10 Threats to Validity — single anonymized production-like UI prototype, model/framework/configuration and observational case-study scope | arXiv:2605.01471v1 — §12 Data Availability; Zenodo archive is linked, but immutable implementation commit Not Disclosed | claim:SF-AUTONOMOUS-TEST-REPAIR-VALIDATION-BOUNDARY | complete |
| SF-ACTION-AGENT-VIDEO-CONTROL | RP-eea6a3eefe70a032 | deep | arXiv:2605.01477v1 | SRC-ARXIV@arXiv:2605.01477v1 | arXiv:2605.01477v1 — §III-A video rehearsal; §III-B FlowDiT action denoising; receding-horizon design | arXiv:2605.01477v1 — §IV–V simulation/real G1 and multi-embodiment evaluation | arXiv:2605.01477v1 — §VI Discussion/Limitations; 5–15s clips; narrow spaces; real open-loop 17 trials | arXiv:2605.01477v1 — model/checkpoint identity described; immutable release commit Not Disclosed | claim:SF-ACTION-AGENT-VIDEO-CONTROL | complete |
| SF-NOTEBOOK-REPRODUCIBILITY-STATE-GATE | RP-059b008671b644a7 | deep | arXiv:2605.01560v1 | SRC-ARXIV@arXiv:2605.01560v1 | arXiv:2605.01560v1 — §3 notebook execution semantics; §3.3 reproducibility; §4 dynamic analysis; §4.1 instrumentation state; §4.2 read/write tracking; §4.3 well-formedness; §4.4 correctness; §5 implementation | arXiv:2605.01560v1 — §6 Evaluation; §6.1 overhead; §6.2 real-world rerun-consistency violations; §6.3 repair | Not Disclosed — exact-v1 has no standalone limitations section; implementation is bounded by instrumented Python/notebook state, modeled cells/files and observable read/write effects | arXiv:2605.01560v1 — §10 Availability; implementation is described, but immutable reviewed repository commit Not Disclosed | claim:SF-NOTEBOOK-REPRODUCIBILITY-STATE-GATE | complete |
| SF-MULTIAGENT-PARETO-COMPUTE-ALLOCATION | RP-249bc377f6dacab8 | deep | arXiv:2605.01566v1 | SRC-ARXIV@arXiv:2605.01566v1 | arXiv:2605.01566v1 — §3 Method; compute-normalized comparison of self-consistency, self-refinement, debate and mixture-of-agents; Appendix A–B model/compute accounting | arXiv:2605.01566v1 — §4 Experiments; §4.1 equal-compute efficiency; §4.2 task difficulty; §4.3 scaling ratio; §4.4 small-vs-large models; §4.5 mixed-vs-uniform MoA; Appendix D | Not Disclosed — exact-v1 has no standalone limitations section; conclusions are bounded to MMLU-Pro/BBH, 34 configurations, tested model sizes and token-based compute estimates | arXiv:2605.01566v1 — prompts and compute formulas are disclosed in appendices; immutable code/result artifact Not Disclosed | claim:SF-MULTIAGENT-PARETO-COMPUTE-ALLOCATION | complete |
| SF-DEVELOPER-MEMORY-OPE-GATE | RP-52c8cd8cc03cd099 | deep | arXiv:2605.01567v1 | SRC-ARXIV@arXiv:2605.01567v1 | arXiv:2605.01567v1 — §2.1 framework; §2.4 deterministic decision; §2.5 feedback normalization; §2.6 delayed reward; §2.7 shadow policy; §2.8 OPE gate; §2.9 governance | arXiv:2605.01567v1 — §3.1–3.8 deterministic 200-case benchmark, controlled baselines, claim gate, patch replay, latency and residual failures | arXiv:2605.01567v1 — §3.4 claim gate; §3.7 latency regression; §3.8 residual failures; §4 Discussion | arXiv:2605.01567v1 — local-first MCP implementation described; official-client interoperability and immutable public commit Not Disclosed | claim:SF-DEVELOPER-MEMORY-OPE-GATE | complete |
| SF-PRODUCTION-AGENT-EVALUATION | RP-1a7904c84168c6bf | deep | arXiv:2605.01604v1 | SRC-ARXIV@arXiv:2605.01604v1 | arXiv:2605.01604v1 — §3 seven production failure modes; §5 PAEF dimensions; §5.2–5.7 definitions and architecture | arXiv:2605.01604v1 — §6 Empirical Evaluation; §6.2–6.5 four public-benchmark experiments | arXiv:2605.01604v1 — §7.3 Limitations — no production data, black-box agents, threshold calibration | arXiv:2605.01604v1 — reference implementation linked in exact-v1; immutable reviewed commit Not Disclosed | claim:SF-PRODUCTION-AGENT-EVALUATION | complete |
| SF-DATA-CONSTRAINED-SCALING-LAW | RP-11db1b0c05a5b6b4 | deep | arXiv:2605.01640v1 | SRC-ARXIV@arXiv:2605.01640v1 | arXiv:2605.01640v1 — §3 setup; §4 additive repetition penalty and scaling law; equations 6–8 | arXiv:2605.01640v1 — §5 validation; §6 weight-decay case; OLMES 19 tasks | arXiv:2605.01640v1 — §7 limitations; ≤1B models, ≤16 epochs, no frontier extrapolation | arXiv:2605.01640v1 — training details in Appendix B; immutable code/data commit Not Disclosed | claim:SF-DATA-CONSTRAINED-SCALING-LAW | complete |
| SF-AGENT-SAFETY-SEARCH-MEASUREMENT | RP-5845007b1f78523a | deep | arXiv:2605.01644v1 | SRC-ARXIV@arXiv:2605.01644v1 | arXiv:2605.01644v1 — §2 deployment configuration; §3 BOA priority search/tree expansion | arXiv:2605.01644v1 — §4 unsafe-trajectory discovery, model/defense/attack comparison and cost | arXiv:2605.01644v1 — §5 discussion; likelihood budget, judger and environment completeness boundary | arXiv:2605.01644v1 — system design disclosed; immutable repository commit Not Disclosed | claim:SF-AGENT-SAFETY-SEARCH-MEASUREMENT | complete |
| SF-AGENT-GENERATED-VERIFIED-COMPILER | RP-a599cb0548c83da6 | deep | arXiv:2605.01660v1 | SRC-ARXIV@arXiv:2605.01660v1 | arXiv:2605.01660v1 — §2 Compiler and Development Overview; §2.1 verification overview; §2.2 rationale; §3 Development Process; §3.1 workflow | arXiv:2605.01660v1 — §4 Validation Technique Evaluation; §4.1 testing; §4.2 certificate checks; §4.3 verification; §4.4 audits; §5.2–5.6 compiler theorems/performance/compile time | arXiv:2605.01660v1 — §2.1–2.2 trust boundary and §4 validation scope — parser/pretty-printer and environment/model assumptions remain outside the verified AST-to-assembly theorem | arXiv:2605.01660v1 — Axon compiler/proofs are described as Lean artifacts; public immutable repository commit used by this review Not Disclosed | claim:SF-AGENT-GENERATED-VERIFIED-COMPILER | complete |
| SF-DITRON-DISTRIBUTED-TILING | RP-3c7f705d80273f2b | deep | arXiv:2605.02953v1 | SRC-ARXIV@arXiv:2605.02953v1 | arXiv:2605.02953v1 — §3 Core/Device/Task hierarchy; swizzling; code generation | arXiv:2605.02953v1 — §4 inference/training kernels, vLLM and NVIDIA/AMD experiments | arXiv:2605.02953v1 — §2.2 model limitations; §5 deployment/portability boundary | arXiv:2605.02953v1 — enterprise deployment claimed; public immutable compiler commit Not Disclosed | claim:SF-DITRON-DISTRIBUTED-TILING | complete |
| SF-REFUSAL-TRAJECTORY-MONITOR | RP-63f32c026531ff00 | deep | arXiv:2605.02958v1 | SRC-ARXIV@arXiv:2605.02958v1 | arXiv:2605.02958v1 — §3 causal tracing; §4 SALO sparse activation operator | arXiv:2605.02958v1 — §5 jailbreak families/operating point; §6 adaptive and encoded-input analysis | arXiv:2605.02958v1 — §7 Limitations | arXiv:2605.02958v1 — white-box hidden-state implementation described; immutable commit Not Disclosed | claim:SF-REFUSAL-TRAJECTORY-MONITOR | complete |
| SF-RECURSIVE-STATE-TERMINATION | RP-5ad9d814d8f16d76 | deep | arXiv:2605.06690v1 | SRC-ARXIV@arXiv:2605.06690v1 | arXiv:2605.06690v1 — §2 epistemic state graph; §3 operators; §4 order-gap; §5 non-degeneracy theorem | Not Required — exact-v1 provides formal examples and application sketches, not an end-to-end empirical benchmark | Not Disclosed — result is local and linearized; exact-v1 proves neither global convergence nor truth | arXiv:2605.06690v1 — formal manuscript; executable artifact Not Applicable | claim:SF-RECURSIVE-STATE-TERMINATION | complete |
| SF-PRUNING-BEHAVIORAL-REGRESSION | RP-2589c45aa464cdc4 | deep | arXiv:2605.08137v1 | SRC-ARXIV@arXiv:2605.08137v1 | arXiv:2605.08137v1 — §IV models/pruning/data/protocol/metrics | arXiv:2605.08137v1 — §V–VI 3 models × 3 methods × 4 sparsities × 5 seeds; edge storage/latency | arXiv:2605.08137v1 — §VII-C Limitations; unstructured post-training pruning only | arXiv:2605.08137v1 — evaluation records described; immutable code/data commit Not Disclosed | claim:SF-PRUNING-BEHAVIORAL-REGRESSION | complete |
| SF-SEQUENTIAL-MODEL-EDIT-SIDECAR | RP-f3ecbba24c226a0d | deep | arXiv:2605.08143v1 | SRC-ARXIV@arXiv:2605.08143v1 | arXiv:2605.08143v1 — §2.1 problem formulation; §2.2 normalized codebook; §2.3 damped Hopfield retrieval; §2.4 codebook update/routing | arXiv:2605.08143v1 — §3.1–3.4 ZsRE/WikiBigEdit/UnKE, 10K/50K sequential edits, cross-model results and ablations; Appendix E large-scale stability | arXiv:2605.08143v1 — §4 Conclusion — codebook memory grows linearly; deployed one-step variant is not covered by the multi-step convergence result; temporal conflicts and multi-hop edits remain open | arXiv:2605.08143v1 — GitHub code/logs linked in exact-v1; immutable reviewed commit Not Disclosed | claim:SF-SEQUENTIAL-MODEL-EDIT-SIDECAR | complete |
| SF-POLICY-CARRIAGE-INTEGRITY | RP-901cc416e4919a61 | deep | arXiv:2605.12535v1 | SRC-ARXIV@arXiv:2605.12535v1 | arXiv:2605.12535v1 — §2 threat model/failure families; §3 SafeContext admission, persistence, binding | arXiv:2605.12535v1 — §4 pressure replay over AutoGen/tau3 and OpenHands/SWE-bench traces | arXiv:2605.12535v1 — §5 Discussion and Limitations; state-level result, unsafe behavior not established | arXiv:2605.12535v1 — data governance/freeze described; immutable reference implementation commit Not Disclosed | claim:SF-POLICY-CARRIAGE-INTEGRITY | complete |
| SF-QUANTIZATION-BEHAVIORAL-REGRESSION | RP-e5ff94d39f0dce33 | deep | arXiv:2605.15208v1 | SRC-ARXIV@arXiv:2605.15208v1 | arXiv:2605.15208v1 — §IV-A/B quantization and controlled protocol | arXiv:2605.15208v1 — §IV-C results across 3 models, BF16–3bit, BBQ, 5 seeds | arXiv:2605.15208v1 — §V-B Limitations; model/task/quantizer scope | arXiv:2605.15208v1 — 911,100 inference records described; immutable code/data commit Not Disclosed | claim:SF-QUANTIZATION-BEHAVIORAL-REGRESSION | complete |

### Source Reviews
<!-- review:SF-ATTACK-AGENT-TERMINAL-FINGERPRINT:start -->
### Trace

攻击 Agent 的 provider/model identity 通常不可从一次 tool call 直接获得，但 terminal session 会留下 command-order 与 bigram 行为痕迹。Trace 先以 TF-IDF/LinearSVC 被动分类 model family，再按 family 路由 defensive prompt-injection payload 做 active forensics。exact-v1 的 2,028-session CTF/container 实验、scaffold-LOSO、evasion 与 proprietary-scaffold 检查只支持所测七个 family/三类 scaffold；classifier 会受 scaffold、mimicry、模型更新和 DPI 可规避性影响，DPI 本身还可能污染调查。Security 章节已将黑盒行为 fingerprint 定义为可漂移的风险 sensor，而非身份凭证，并要求不确定时回退限流/隔离，因此该 family 不重复写入。

<!-- claim:SF-ATTACK-AGENT-TERMINAL-FINGERPRINT:start -->证据边界：只接受 arXiv exact-v1 在上述 method/evaluation contract 内的作者主张；未披露硬件、precision、并发、SLO、artifact commit 或生产条件写 Not Disclosed，不作外推。<!-- claim:SF-ATTACK-AGENT-TERMINAL-FINGERPRINT:end -->
<!-- review:SF-ATTACK-AGENT-TERMINAL-FINGERPRINT:end -->
<!-- review:SF-COMPUTE-OPTIMAL-TOKENIZATION:start -->
### Compute Optimal Tokenization

Token 计数把 tokenizer 的 compression rate 偷渡进 scaling law；同一字节信息被切成不同 token 数时，tokens-per-parameter 不能跨 tokenizer 比较。exact-v1 在 988 个 latent-tokenized 与 320 个 subword 模型上把数据单位改为 bytes，并显示 compute-optimal bytes/parameter 更稳定，而最佳 compression rate 会随 compute 和语言变化。证据支持 tokenizer 是 Training/Inference 的共同设计变量；实验仍受 BLT/Llama-style architecture、DCLM、C4、50M–6.7B 与给定 FLOPs 区间约束，不能外推到 frontier MoE、多模态或任意 domain。

<!-- claim:SF-COMPUTE-OPTIMAL-TOKENIZATION:start -->证据边界：只接受 arXiv exact-v1 在上述 method/evaluation contract 内的作者主张；未披露硬件、precision、并发、SLO、artifact commit 或生产条件写 Not Disclosed，不作外推。<!-- claim:SF-COMPUTE-OPTIMAL-TOKENIZATION:end -->
<!-- review:SF-COMPUTE-OPTIMAL-TOKENIZATION:end -->
<!-- review:SF-SENTINEL-VLA-STATUS-CONTROL:start -->
### Sentinel-VLA

固定每步深思会破坏实时控制，完全 reactive VLA 又无法识别错误状态。Sentinel-VLA 用 status-monitor expert 把 control state 显式分为 Initial、Normal、New-subtask 与 Error，只有非 Normal 才更新 thought memory 或触发 recovery；action expert 消费 observation、status 与 memory。exact-v1 在 RLBench、LIBERO-LONG 与三项实机任务报告收益并做 monitor/SECL ablation，但 status label 来自合成 error pipeline，代码仍未发布，也没有证明 OOD 校准、hard deadline 或独立 safety envelope；因此 monitor 只拥有 reasoning trigger，低层 controller 仍拥有物理 commit。

<!-- claim:SF-SENTINEL-VLA-STATUS-CONTROL:start -->证据边界：只接受 arXiv exact-v1 在上述 method/evaluation contract 内的作者主张；未披露硬件、precision、并发、SLO、artifact commit 或生产条件写 Not Disclosed，不作外推。<!-- claim:SF-SENTINEL-VLA-STATUS-CONTROL:end -->
<!-- review:SF-SENTINEL-VLA-STATUS-CONTROL:end -->
<!-- review:SF-VLA-ADAPTIVE-TEST-TIME-COMPUTE:start -->
### VLA-ATTC

固定 compute 的 VLA 对简单状态浪费延迟，对模糊状态又缺少 deliberation。该机制让 uncertainty clutch 只在必要时把 control flow 从单次 proposal 切到候选采样，再由 pairwise relative critic 选择动作。作者在 LIBERO-LONG/PI0.5 配置报告 failure reduction，但未证明 uncertainty 在真实机器人或 distribution shift 下校准，且 critic error 会把额外 compute 变成更自信的错误；low-level controller 与 safety envelope 仍拥有 commit。

<!-- claim:SF-VLA-ADAPTIVE-TEST-TIME-COMPUTE:start -->证据边界：只接受 arXiv exact-v1 在上述 method/evaluation contract 内的作者主张；未披露硬件、precision、并发、SLO、artifact commit 或生产条件写 Not Disclosed，不作外推。<!-- claim:SF-VLA-ADAPTIVE-TEST-TIME-COMPUTE:end -->
<!-- review:SF-VLA-ADAPTIVE-TEST-TIME-COMPUTE:end -->
<!-- review:SF-TAIL-SAFE-RUNTIME-MONITOR:start -->
### TAIL-Safe

仅靠 imitation policy 的 nominal action 无法感知 compounding drift。TAIL-Safe 把 visibility、recognizability、graspability 聚合为 Lipschitz Q，并以零超水平集作为经验 safe set；proposal 越界时，watchdog 用 action-gradient recovery 把候选拉回。它把 monitor/veto 从 actor 中分离，但只验证 deterministic policy，safe set 固定，digital twin 在接触任务上有 optimistic gap，且没有外部 safety baseline；因此是 empirical runtime guard，不是形式 certificate。

<!-- claim:SF-TAIL-SAFE-RUNTIME-MONITOR:start -->证据边界：只接受 arXiv exact-v1 在上述 method/evaluation contract 内的作者主张；未披露硬件、precision、并发、SLO、artifact commit 或生产条件写 Not Disclosed，不作外推。<!-- claim:SF-TAIL-SAFE-RUNTIME-MONITOR:end -->
<!-- review:SF-TAIL-SAFE-RUNTIME-MONITOR:end -->
<!-- review:SF-VISUOMOTOR-EXECUTION-GUARANTEE:start -->
### Visuomotor Execution Guarantee

只看 task success 会把‘成功但越过危险状态’与可靠执行混在一起。该工作从 demonstrations 和冻结视觉 encoder 构造 visibility/recognizability safeset，用 Nagumo sub-tangentiality 把它解释为 control-invariant region，再以 QP recovery controller 对 nominal policy action 做最小投影。exact-v1 的 Franka 仿真与实机结果支持所测 Lift/Candy-Sorting、clean/clutter/OOD 条件下的 execution guarantee，但其所谓 guarantee 等于 safeset 内达到该 policy 的 best-known success，并依赖 fully actuated、line-of-sight、goal-specific demonstration coverage；它不证明任意安全属性、动态目标、grasp feasibility 或未知 embodiment。长期增量是把 safety 从 learned actor 的 confidence 外移为 safeset certificate + recovery + controller commit。

<!-- claim:SF-VISUOMOTOR-EXECUTION-GUARANTEE:start -->证据边界：只接受 arXiv exact-v1 在上述 method/evaluation contract 内的作者主张；未披露硬件、precision、并发、SLO、artifact commit 或生产条件写 Not Disclosed，不作外推。<!-- claim:SF-VISUOMOTOR-EXECUTION-GUARANTEE:end -->
<!-- review:SF-VISUOMOTOR-EXECUTION-GUARANTEE:end -->
<!-- review:SF-GRBEN-PROCESS-REWARD-EVAL:start -->
### GR-Ben

PRM 在数学过程上表现良好并不证明能识别 science/logic 中的 knowledge 与 computational error。GR-Ben 把过程错误检测拆为两个 domain、九个 subdomain，并对 22 个模型比较。它强化了 evaluation 必须分 slice/error type 的既有结论，但公开 general-reasoning PRM 只覆盖 VersaPRM，任务仍偏 academic，未形成新的系统 owner 或 release contract，故不重复写入。

<!-- claim:SF-GRBEN-PROCESS-REWARD-EVAL:start -->证据边界：只接受 arXiv exact-v1 在上述 method/evaluation contract 内的作者主张；未披露硬件、precision、并发、SLO、artifact commit 或生产条件写 Not Disclosed，不作外推。<!-- claim:SF-GRBEN-PROCESS-REWARD-EVAL:end -->
<!-- review:SF-GRBEN-PROCESS-REWARD-EVAL:end -->
<!-- review:SF-BROWSING-AGENT-BEHAVIORAL-FINGERPRINT:start -->
### FP-Agent

真实浏览器会削弱传统 bot flag 与 browser fingerprint 的区分力，网站仍可从 typing、scroll 与 mouse trajectory 提取行为 sensor。FP-Agent 在 instrumented honey site 上比较七种 browsing agent 与人类、三类任务，并显示 behavioral features 比共享 browser features 更有区分度。该结果不证明开放流量上的稳定身份：任务、browser automation、agent version 与反检测策略都会漂移，实时 false-positive cost 也未由受控研究闭合。Security 章节已经把 web-agent attribution 写成 TLS/HTTP/browser-action 多层 fingerprint，由 policy engine 只据此 throttle/challenge，classifier 漂移时回退行为限流；故 No Change。

<!-- claim:SF-BROWSING-AGENT-BEHAVIORAL-FINGERPRINT:start -->证据边界：只接受 arXiv exact-v1 在上述 method/evaluation contract 内的作者主张；未披露硬件、precision、并发、SLO、artifact commit 或生产条件写 Not Disclosed，不作外推。<!-- claim:SF-BROWSING-AGENT-BEHAVIORAL-FINGERPRINT:end -->
<!-- review:SF-BROWSING-AGENT-BEHAVIORAL-FINGERPRINT:end -->
<!-- review:SF-ACTIVATION-GRADIENT-COMPRESSION:start -->
### Activation Compression in LLMs

activation memory 不能像 optimizer state 一样无条件压缩：unbiased activation compression 经过 linear operator 仍可保持无偏，而 nonlinear operator 会引入系统性 gradient bias。论文据此只压 linear paths，并复用低秩 activation factors 压 gradient，给出 variance/convergence 界和单 A800 的模型实验。结果不覆盖 nonlinear 全路径、distributed communication、checkpointing 组合或不同 precision；机制应作为 memory–variance–compute 分支，而非默认替换 rematerialization。

<!-- claim:SF-ACTIVATION-GRADIENT-COMPRESSION:start -->证据边界：只接受 arXiv exact-v1 在上述 method/evaluation contract 内的作者主张；未披露硬件、precision、并发、SLO、artifact commit 或生产条件写 Not Disclosed，不作外推。<!-- claim:SF-ACTIVATION-GRADIENT-COMPRESSION:end -->
<!-- review:SF-ACTIVATION-GRADIENT-COMPRESSION:end -->
<!-- review:SF-PIXEL-LEVEL-RAG-EVIDENCE-CHAIN:start -->
### Chain of Evidence

text-only parsing 会丢掉表格、图形与 layout 的空间关系，也只能把 citation 粗略指到整篇文档。Chain of Evidence 让 VLM 在检索到的 page/slide screenshots 上生成带 bounding boxes 的多跳 evidence chain，再据该 chain 回答。exact-v1 的 Wiki-CoE、SlideVQA、ablation 与 efficiency 实验支持所测 visual-document workload 的定位/回答收益，但 bounding box 仍是模型生成的 locator，不自动证明 source authority、claim entailment 或 corpus completeness，也未覆盖动态页面和 event-time revision。长期增量是把 RAG evidence identity 从 document/chunk 扩展到 modality-native region 与 hop dependency，同时保留原始可回取 source。

<!-- claim:SF-PIXEL-LEVEL-RAG-EVIDENCE-CHAIN:start -->证据边界：只接受 arXiv exact-v1 在上述 method/evaluation contract 内的作者主张；未披露硬件、precision、并发、SLO、artifact commit 或生产条件写 Not Disclosed，不作外推。<!-- claim:SF-PIXEL-LEVEL-RAG-EVIDENCE-CHAIN:end -->
<!-- review:SF-PIXEL-LEVEL-RAG-EVIDENCE-CHAIN:end -->
<!-- review:SF-LOGIC-GROUNDED-SKILL-INDUCTION:start -->
### Neuro-Symbolic Skill Induction

把 trajectory 直接总结成 state-blind script 会丢失分支条件与变量依赖，运行环境变化后容易把偶然步骤当通用 skill。NSI 把 traces 提升为带 node、control flow、dynamic variable binding 与交互语义的 logic-grounded program，并允许通过 reflective planning 在线修订。exact-v1 的有限 agentic-task 实验支持所测任务上的 few-shot induction 与 modular honing，不证明开放工具环境里的 side-effect safety、权限、并发、termination 或 skill admission。Agent Platform 已把 trajectory→typed/versioned Skill 明确定义为 artifact compilation，并要求 held-out evaluation、permission/smoke-test、publish/supersede/rollback；Workflow 也已拥有 durable control-flow state，因此 No Change。

<!-- claim:SF-LOGIC-GROUNDED-SKILL-INDUCTION:start -->证据边界：只接受 arXiv exact-v1 在上述 method/evaluation contract 内的作者主张；未披露硬件、precision、并发、SLO、artifact commit 或生产条件写 Not Disclosed，不作外推。<!-- claim:SF-LOGIC-GROUNDED-SKILL-INDUCTION:end -->
<!-- review:SF-LOGIC-GROUNDED-SKILL-INDUCTION:end -->
<!-- review:SF-COUNTERFACTUAL-RISK-RAG:start -->
### CoRM-RAG

semantic relevance 在 false-premise 或 confirmation-bias query 上会优先检索支持错误前提的文档。CoRM-RAG 用认知扰动构造 counterfactual training pairs，蒸馏 Evidence Critic，并以 risk threshold 决定 retrieve 或 abstain。exact-v1 支持所测 decision benchmarks 上的 robustness/risk-coverage 结果，但不证明 critic 跨领域校准、来源 authority、claim entailment 或生产 corpus drift。当前 RAG 章节已经把 relevance 降为候选生成信号，并用 sufficiency、independent check、abstain/escalate 承载相同长期设计，因此作为受限证据 No Change。

<!-- claim:SF-COUNTERFACTUAL-RISK-RAG:start -->证据边界：只接受 arXiv exact-v1 在上述 method/evaluation contract 内的作者主张；未披露硬件、precision、并发、SLO、artifact commit 或生产条件写 Not Disclosed，不作外推。<!-- claim:SF-COUNTERFACTUAL-RISK-RAG:end -->
<!-- review:SF-COUNTERFACTUAL-RISK-RAG:end -->
<!-- review:SF-CONFOUNDED-LOG-EVALUATION:start -->
### The Partial Testimony of Logs

生产日志中的 model choice 与 user/context 同时影响评分，raw outcome comparison 估计的是不同自选人群。exact-v1 证明小规模 randomized EXP 与 offline SIM 才共同 identify causal model value，OBS 只能在 identification 后降低方差。该结论依赖 randomization、consistency、positivity 与无 latent mediator confounding；A4 对 adaptive/multi-round agent 不成立，因此日志规模不能替代实验设计，simulator 也不是 ground truth。

<!-- claim:SF-CONFOUNDED-LOG-EVALUATION:start -->证据边界：只接受 arXiv exact-v1 在上述 method/evaluation contract 内的作者主张；未披露硬件、precision、并发、SLO、artifact commit 或生产条件写 Not Disclosed，不作外推。<!-- claim:SF-CONFOUNDED-LOG-EVALUATION:end -->
<!-- review:SF-CONFOUNDED-LOG-EVALUATION:end -->
<!-- review:SF-ACCESS-AWARE-VECTOR-INDEX:start -->
### Authorized Vector Retrieval via Access-Aware Indexing

global ANN 后过滤会让 unauthorized vectors 占用 beam 并破坏 recall；为每个 role 建 oracle index 又产生复制爆炸。Veda 把 RBAC role-combination blocks 组织成 lattice，在 storage amplification budget 下 copy/merge，并由 per-role query plan 先搜 pure nodes、用 global top-k bound 剪枝 impure nodes。收益绑定 role 稳定、union semantics 与作者 HNSW workload；授权范围很宽时 global index 仍更便宜，policy revision、delete consistency 与 side-channel 仍未解决。

<!-- claim:SF-ACCESS-AWARE-VECTOR-INDEX:start -->证据边界：只接受 arXiv exact-v1 在上述 method/evaluation contract 内的作者主张；未披露硬件、precision、并发、SLO、artifact commit 或生产条件写 Not Disclosed，不作外推。<!-- claim:SF-ACCESS-AWARE-VECTOR-INDEX:end -->
<!-- review:SF-ACCESS-AWARE-VECTOR-INDEX:end -->
<!-- review:SF-VUDA-CUDA-VULKAN-SHARING:start -->
### VUDA

embodied simulation 把 CUDA physics 与 Vulkan rendering 放在同卡却被 context/scheduling-group 隔离，时间复用无法利用互补空洞。VUDA 通过 channel redirection 把 CUDA stream 纳入 Vulkan scheduling domain，并 graft 隔离 address space 的 page tables，避免 critical-path copy。作者 workload 支持特定 GPU/driver 下的空间并发收益，但这是侵入式 driver trust boundary；地址隔离、同步、preemption 与跨版本兼容一旦不成立，应回退时间复用。

<!-- claim:SF-VUDA-CUDA-VULKAN-SHARING:start -->证据边界：只接受 arXiv exact-v1 在上述 method/evaluation contract 内的作者主张；未披露硬件、precision、并发、SLO、artifact commit 或生产条件写 Not Disclosed，不作外推。<!-- claim:SF-VUDA-CUDA-VULKAN-SHARING:end -->
<!-- review:SF-VUDA-CUDA-VULKAN-SHARING:end -->
<!-- review:SF-LONG-FORM-LENGTH-VOLATILITY:start -->
### Long-Form Length Volatility

单次长输出质量掩盖 repeated-run token length 的方差，而方差会直接放大 capacity、cost 与 deadline 风险。VOLTBench 将 structured/unstructured task 的长度稳定性单独测量，GLoBo 用 logits boosting 抑制观察到的 failure-token pattern。作者结果只绑定少量重复、给定模型、LLM judge/执行式 scorer 和 logits access；attention correlation 不是因果机制，固定 max-token/模板约束在确定性 SLO 下仍更简单。

<!-- claim:SF-LONG-FORM-LENGTH-VOLATILITY:start -->证据边界：只接受 arXiv exact-v1 在上述 method/evaluation contract 内的作者主张；未披露硬件、precision、并发、SLO、artifact commit 或生产条件写 Not Disclosed，不作外推。<!-- claim:SF-LONG-FORM-LENGTH-VOLATILITY:end -->
<!-- review:SF-LONG-FORM-LENGTH-VOLATILITY:end -->
<!-- review:SF-PROVENANCE-GRAPH-MEMORY:start -->
### MemORAI

Flat top-k memory 把 episode granularity、事实来源和关联扩展压成一个 similarity score。MemORAI 先做 session/topic segmentation 与 selective compression，再把 entity、turn、segment 和 provenance 写入 multi-relational graph，读取时按 query 构造子图并动态加权 PageRank。exact-v1 在 LOCOMO/LongMemEval、三种 backbone 与 component ablation 上支持该组合在所测 workload 的 retrieval/generation 增益，但 static entity linking、歧义 coreference、实时 graph cost、concurrent update、ACL/deletion propagation 均未闭合。Memory 章节已经形成 authorized anchor recall → bounded graph expansion → provenance merge 的相同主线，因此 No Change。

<!-- claim:SF-PROVENANCE-GRAPH-MEMORY:start -->证据边界：只接受 arXiv exact-v1 在上述 method/evaluation contract 内的作者主张；未披露硬件、precision、并发、SLO、artifact commit 或生产条件写 Not Disclosed，不作外推。<!-- claim:SF-PROVENANCE-GRAPH-MEMORY:end -->
<!-- review:SF-PROVENANCE-GRAPH-MEMORY:end -->
<!-- review:SF-LIVEFMBENCH-SPECIFICATION-EVAL:start -->
### LiveFMBench

直接用 prover pass 计算 specification accuracy 会把忽略 code context 或欺骗 verifier 的 unfaithful output 计为成功。LiveFMBench 加入 2025 新样本和 faithful filtering 后报告约 20% 的准确率回落，并比较 sampling、thinking 与 agent pipeline。该证据是现有 EvalSpec 中 contamination、adversarial metric gaming 与 semantic judge 分层的具体案例，范围限 ACSL/C，不形成新的长期机制，故 No Change。

<!-- claim:SF-LIVEFMBENCH-SPECIFICATION-EVAL:start -->证据边界：只接受 arXiv exact-v1 在上述 method/evaluation contract 内的作者主张；未披露硬件、precision、并发、SLO、artifact commit 或生产条件写 Not Disclosed，不作外推。<!-- claim:SF-LIVEFMBENCH-SPECIFICATION-EVAL:end -->
<!-- review:SF-LIVEFMBENCH-SPECIFICATION-EVAL:end -->
<!-- review:SF-AUTOREGRESSIVE-CREDIT-ATTRIBUTION-BARRIER:start -->
### Counterfactual Credit Attribution Barriers

next-token predictor 满足 counterfactual credit attribution 不代表整段 autoregressive generation 也满足，因为小的 token-level依赖会沿序列组合；事后给黑盒模型补 credit 在弱 optimality 条件下还需要随输出长度指数增长的 query。它否定了两条自然但错误的 attribution 路线。结论是 theorem-bound，不是工程 benchmark；若系统需要 provenance，应在 retrieval/context/decoding 时保留 source relation，而不能指望 final answer 后廉价重建。

<!-- claim:SF-AUTOREGRESSIVE-CREDIT-ATTRIBUTION-BARRIER:start -->证据边界：只接受 arXiv exact-v1 在上述 method/evaluation contract 内的作者主张；未披露硬件、precision、并发、SLO、artifact commit 或生产条件写 Not Disclosed，不作外推。<!-- claim:SF-AUTOREGRESSIVE-CREDIT-ATTRIBUTION-BARRIER:end -->
<!-- review:SF-AUTOREGRESSIVE-CREDIT-ATTRIBUTION-BARRIER:end -->
<!-- review:SF-LORA-COMPOSITION-RELIABILITY:start -->
### SCALE-LoRA

按 task 检索到相关 adapters 不代表这些低秩更新在参数空间兼容。SCALE-LoRA 保留 linear anchor，把 block-wise adapter directions residualize 后按 norm/alignment guard 组合；更高成本分支生成多个 sparse composition views，用 agreement、support-loss proxy 与 oracle headroom 做 post-retrieval audit。作者明确 single-view LASRC 的 task-stratified CI 跨零，support loss 不是 calibrated query-accuracy estimator，多路径也没有 fixed serving stack 的 latency/GPU-memory 证明。长期增量不是宣称某个 merge 算法普遍最优，而是把 retrieve → compose → reliability audit → promote 变成带 adapter-pool identity、matched controls 与 path-cost receipt 的 lifecycle。

<!-- claim:SF-LORA-COMPOSITION-RELIABILITY:start -->证据边界：只接受 arXiv exact-v1 在上述 method/evaluation contract 内的作者主张；未披露硬件、precision、并发、SLO、artifact commit 或生产条件写 Not Disclosed，不作外推。<!-- claim:SF-LORA-COMPOSITION-RELIABILITY:end -->
<!-- review:SF-LORA-COMPOSITION-RELIABILITY:end -->
<!-- review:SF-AUTONOMOUS-TEST-REPAIR-VALIDATION-BOUNDARY:start -->
### Practical Limits of Autonomous Test Repair

把 test pass 当 repair objective 在人工指定 oracle 稳定时成本低，但 autonomous loop 可以通过弱化 assertion 或删除失败 test 来制造表面 convergence。该 case study 记录了 300 reports、636 executions、非收敛 retry、无可执行 artifact、environment failure，并直接观察到 assertion weakening 与 scope deletion；因此 pass rate 必须与原始 test intent、coverage inventory、artifact existence 和 mutation diff 共同验收。证据受单一 anonymized UI prototype、10 scenario families 与 observational design 限制，不证明所有 coding agent 的 failure rate。长期增量是把 semantic oracle 与 scope ownership 放在 repair agent 之外，并对 assertion/test-set 变更设置人工或独立 verifier gate。

<!-- claim:SF-AUTONOMOUS-TEST-REPAIR-VALIDATION-BOUNDARY:start -->证据边界：只接受 arXiv exact-v1 在上述 method/evaluation contract 内的作者主张；未披露硬件、precision、并发、SLO、artifact commit 或生产条件写 Not Disclosed，不作外推。<!-- claim:SF-AUTONOMOUS-TEST-REPAIR-VALIDATION-BOUNDARY:end -->
<!-- review:SF-AUTONOMOUS-TEST-REPAIR-VALIDATION-BOUNDARY:end -->
<!-- review:SF-ACTION-AGENT-VIDEO-CONTROL:start -->
### Action Agent

论文把 agentic video imagination 与 action diffusion 拆成两阶段，说明 visual plan 与 controller 的 representation/latency contract 必须分开。真实 G1 仅 17 次 open-loop trial，视频片段 5–15 秒且窄空间失败增加；因此不证明 closed-loop safety 或 video realism 等于 controllable dynamics。Ch26 已明确拥有 video/latent imagination → action proposal → controller/environment feedback 的主线和同样边界，故只保留证据，不重复写入。

<!-- claim:SF-ACTION-AGENT-VIDEO-CONTROL:start -->证据边界：只接受 arXiv exact-v1 在上述 method/evaluation contract 内的作者主张；未披露硬件、precision、并发、SLO、artifact commit 或生产条件写 Not Disclosed，不作外推。<!-- claim:SF-ACTION-AGENT-VIDEO-CONTROL:end -->
<!-- review:SF-ACTION-AGENT-VIDEO-CONTROL:end -->
<!-- review:SF-NOTEBOOK-REPRODUCIBILITY-STATE-GATE:start -->
### FlowBook

保存 notebook 文件与执行顺序仍无法证明当前 outputs 可由 clean run 重现，因为 out-of-order cells 会在共享 store 中留下 hidden mutation。FlowBook 把 reproducibility 定义为从 empty store 按 top-to-bottom 执行得到当前记录 outputs，并在 cell boundary 跟踪 read/write set、标记 stale cells、阻止破坏 rerun consistency 的操作。exact-v1 给出 semantics、preservation/reproducibility/progress 证明与 real-notebook evaluation，但对未建模外部服务、native extension、随机性、并发和不可观察 side effect 不提供保证。长期增量是把 notebook 从版本化步骤容器推进为带 clean-state equivalence 与 stale-state gate 的 workflow artifact。

<!-- claim:SF-NOTEBOOK-REPRODUCIBILITY-STATE-GATE:start -->证据边界：只接受 arXiv exact-v1 在上述 method/evaluation contract 内的作者主张；未披露硬件、precision、并发、SLO、artifact commit 或生产条件写 Not Disclosed，不作外推。<!-- claim:SF-NOTEBOOK-REPRODUCIBILITY-STATE-GATE:end -->
<!-- review:SF-NOTEBOOK-REPRODUCIBILITY-STATE-GATE:end -->
<!-- review:SF-MULTIAGENT-PARETO-COMPUTE-ALLOCATION:start -->
### Pareto-Optimal Test-Time Scaling

比较 multi-agent、self-consistency 与 refinement 时，固定 sample/agent 数会让更昂贵 pipeline 看起来更强，却无法回答同一预算该选哪个。该工作把 34 个配置放入 accuracy–compute Pareto front，并在相同 token-compute 预算下比较并行 generations、sequential aggregations、debate rounds 与 model size。结果只覆盖 MMLU-Pro/BBH、作者模型池与 token-based estimate；API latency、KV/communication、并发、能耗、相关错误和开放式工具任务均未纳入，不能把某一 topology 宣称为普遍最优。长期增量是让 Multi-Agent admission 先绑定可复算 compute budget 与 single-agent baselines，再按 task difficulty/quality frontier 决定协调。

<!-- claim:SF-MULTIAGENT-PARETO-COMPUTE-ALLOCATION:start -->证据边界：只接受 arXiv exact-v1 在上述 method/evaluation contract 内的作者主张；未披露硬件、precision、并发、SLO、artifact commit 或生产条件写 Not Disclosed，不作外推。<!-- claim:SF-MULTIAGENT-PARETO-COMPUTE-ALLOCATION:end -->
<!-- review:SF-MULTIAGENT-PARETO-COMPUTE-ALLOCATION:end -->
<!-- review:SF-DEVELOPER-MEMORY-OPE-GATE:start -->
### RL Developer Memory

coding-agent memory access 会改变 patch 与验证结论，因此不能只按 embedding similarity 返回。该架构把 retrieval 记为带 propensity 的 decision event，将异构 feedback 归一成 bounded reward，把 verified resolution 反链到原事件，并让 learned residual policy 先 shadow、再经 OPE 才可 canary。作者同 commit 实验没有证明 accuracy gain，且披露 latency regression、40 个 residual failures 与 official MCP client 未支持。Memory 章节已要求 provenance、feedback/verifier、writer-reader authority 分离、shadow/canary、abstain 与 rollback，故该 family 强化现有 contract，不重复写入。

<!-- claim:SF-DEVELOPER-MEMORY-OPE-GATE:start -->证据边界：只接受 arXiv exact-v1 在上述 method/evaluation contract 内的作者主张；未披露硬件、precision、并发、SLO、artifact commit 或生产条件写 Not Disclosed，不作外推。<!-- claim:SF-DEVELOPER-MEMORY-OPE-GATE:end -->
<!-- review:SF-DEVELOPER-MEMORY-OPE-GATE:end -->
<!-- review:SF-PRODUCTION-AGENT-EVALUATION:start -->
### PAEF

单次 benchmark 不能观察长链 error cascade、tool availability 与 truth 解耦、输出分布漂移或 explanation-decision divergence。PAEF 把这些压力拆为 cascade uncertainty、tool reliability、distribution health、explanation validity 与 cross-surface consistency，并要求持续观测。虽然摘要称 billion-event observations，§7.3 明确实验没有 production data，阈值也未校准；因此不能把结果当生产有效性证明。Evaluation 章节已拥有 trajectory/component receipts、drift、offline→shadow→canary→online、per-example slice 与 scorer identity，故 No Change。

<!-- claim:SF-PRODUCTION-AGENT-EVALUATION:start -->证据边界：只接受 arXiv exact-v1 在上述 method/evaluation contract 内的作者主张；未披露硬件、precision、并发、SLO、artifact commit 或生产条件写 Not Disclosed，不作外推。<!-- claim:SF-PRODUCTION-AGENT-EVALUATION:end -->
<!-- review:SF-PRODUCTION-AGENT-EVALUATION:end -->
<!-- review:SF-DATA-CONSTRAINED-SCALING-LAW:start -->
### Data-Constrained Scaling Laws

Chinchilla 默认 token 独立唯一；当高质量数据被重复，旧 effective-data saturation 会低估 overfitting。论文把 repetition penalty 作为与 unique-data benefit 并列的项，得到超过阈值后应把 compute 给模型容量而非继续 epoch 的条件分支，并用 weight decay 案例显示 penalty coefficient 可改变。范围只有 15M–1B、50M–6B unique tokens、至多 16 epochs，不能当作 frontier 常数。

<!-- claim:SF-DATA-CONSTRAINED-SCALING-LAW:start -->证据边界：只接受 arXiv exact-v1 在上述 method/evaluation contract 内的作者主张；未披露硬件、precision、并发、SLO、artifact commit 或生产条件写 Not Disclosed，不作外推。<!-- claim:SF-DATA-CONSTRAINED-SCALING-LAW:end -->
<!-- review:SF-DATA-CONSTRAINED-SCALING-LAW:end -->
<!-- review:SF-AGENT-SAFETY-SEARCH-MEASUREMENT:start -->
### Agent Safety Measurement by Search

greedy 或少量 sample 的 safe rate 看不到低概率但预算内的不可逆 action trajectory。BOA 把 model、decoder、prompt、environment、judger 与 likelihood budget 冻结为 deployment configuration，再在单轮 token 与多轮 interaction tree 中搜索 unsafe path。它能发现 sampled eval 漏掉的 path，但 score 仍受 search completeness、budget、judger 和环境模型约束；不是形式概率证明。

<!-- claim:SF-AGENT-SAFETY-SEARCH-MEASUREMENT:start -->证据边界：只接受 arXiv exact-v1 在上述 method/evaluation contract 内的作者主张；未披露硬件、precision、并发、SLO、artifact commit 或生产条件写 Not Disclosed，不作外推。<!-- claim:SF-AGENT-SAFETY-SEARCH-MEASUREMENT:end -->
<!-- review:SF-AGENT-SAFETY-SEARCH-MEASUREMENT:end -->
<!-- review:SF-AGENT-GENERATED-VERIFIED-COMPILER:start -->
### Axon Verified Compiler

coding agent 能快速生成 compiler 与 proof code，但‘有测试’仍可能漏掉环境模型，人工 audit 也不随代码量线性扩展。Axon 将 AST→assembly correctness 放进 Lean theorem，优化 pass 生成可检查 certificate；testing 发现环境假设问题，certificate checker/verification 管理语义正确性，audit 只处理未验证边界。exact-v1 不证明 parser、pretty-printer、host/toolchain、spec 本身或所有性能目标；机器证明只覆盖形式化 statement。长期增量是按 artifact boundary 组合 testing、translation validation、machine-checked proof 与 audit，而不是让 agent 或单一 validator 同时拥有 specification 与 accept 权。

<!-- claim:SF-AGENT-GENERATED-VERIFIED-COMPILER:start -->证据边界：只接受 arXiv exact-v1 在上述 method/evaluation contract 内的作者主张；未披露硬件、precision、并发、SLO、artifact commit 或生产条件写 Not Disclosed，不作外推。<!-- claim:SF-AGENT-GENERATED-VERIFIED-COMPILER:end -->
<!-- review:SF-AGENT-GENERATED-VERIFIED-COMPILER:end -->
<!-- review:SF-DITRON-DISTRIBUTED-TILING:start -->
### DITRON

单机 tensor DSL 的 tile 不知道跨设备 topology，分布式 library 又把 kernel 固定成不可编程 primitive。DITRON 用 Core/Device/Task 三层 tile 把 local memory、device communication 和 task mapping 放进一个 compiler plan，并以 compute–communication swizzling 生成后端。作者结果支持所测 cluster/kernel/vLLM 的收益，但硬件、版本、precision、topology 与生产数据未完整公开，企业节省数字不能外推；expert library 在稳定算子仍是可靠 baseline。

<!-- claim:SF-DITRON-DISTRIBUTED-TILING:start -->证据边界：只接受 arXiv exact-v1 在上述 method/evaluation contract 内的作者主张；未披露硬件、precision、并发、SLO、artifact commit 或生产条件写 Not Disclosed，不作外推。<!-- claim:SF-DITRON-DISTRIBUTED-TILING:end -->
<!-- review:SF-DITRON-DISTRIBUTED-TILING:end -->
<!-- review:SF-REFUSAL-TRAJECTORY-MONITOR:start -->
### Refusal Trajectory Monitoring

terminal refusal direction 可能被 GCG 抑制而上游 layer-token trajectory 仍保留，SALO 因而把 hidden-state volume 作为 white-box sensor。它在给定 Qwen/Llama/Mistral 与 XSTest operating point 上改善若干 attack detection；但 causal sufficiency 不等于 necessity，encoded intent 可让模型根本不形成 trajectory，且内部 sensor 与被攻击模型共故障。Security 章节已要求 independent layered guardrails、固定 operating point 与 adaptive red-team，故作为受限案例 No Change。

<!-- claim:SF-REFUSAL-TRAJECTORY-MONITOR:start -->证据边界：只接受 arXiv exact-v1 在上述 method/evaluation contract 内的作者主张；未披露硬件、precision、并发、SLO、artifact commit 或生产条件写 Not Disclosed，不作外推。<!-- claim:SF-REFUSAL-TRAJECTORY-MONITOR:end -->
<!-- review:SF-REFUSAL-TRAJECTORY-MONITOR:end -->
<!-- review:SF-RECURSIVE-STATE-TERMINATION:start -->
### Recursive State and Termination

recursive reasoning 若只保存 transcript，就无法区分 claim、evidence、open question 与 confidence，也缺少可审计 stop signal。论文把它们显式为 epistemic state graph，并比较 expand→consolidate 与 consolidate→expand 的 order-gap；局部 gap 小表示两种更新近似交换。非退化定理只说明该 signal 何时不为代数空值，不证明 global convergence、正确性或成本最优，故应作为 termination sensor 与预算/外部 verifier 联用。

<!-- claim:SF-RECURSIVE-STATE-TERMINATION:start -->证据边界：只接受 arXiv exact-v1 在上述 method/evaluation contract 内的作者主张；未披露硬件、precision、并发、SLO、artifact commit 或生产条件写 Not Disclosed，不作外推。<!-- claim:SF-RECURSIVE-STATE-TERMINATION:end -->
<!-- review:SF-RECURSIVE-STATE-TERMINATION:end -->
<!-- review:SF-PRUNING-BEHAVIORAL-REGRESSION:start -->
### Pruning Behavioral Regression

perplexity 保持不代表压缩后 alignment behavior 等价。作者在三个 instruct 模型、三种 pruning、四档 sparsity、BBQ 与五 seeds 上观察到 Wanda 可近似保 perplexity 却放大 stereotype reliance；同时 unstructured zeroing 在所测 edge hardware 没有 storage/latency 收益。结果不覆盖 structured/N:M、pruning-aware finetune 或其他 safety slices，机制解释仍是推断；它支持 release gate 必须测行为 transition 与真实 deploy artifact。

<!-- claim:SF-PRUNING-BEHAVIORAL-REGRESSION:start -->证据边界：只接受 arXiv exact-v1 在上述 method/evaluation contract 内的作者主张；未披露硬件、precision、并发、SLO、artifact commit 或生产条件写 Not Disclosed，不作外推。<!-- claim:SF-PRUNING-BEHAVIORAL-REGRESSION:end -->
<!-- review:SF-PRUNING-BEHAVIORAL-REGRESSION:end -->
<!-- review:SF-SEQUENTIAL-MODEL-EDIT-SIDECAR:start -->
### HoReN

部署后事实修正若直接改 shared weights，会让连续小样本 edit 累积干扰；外部 memory editor 避免 base-weight drift，却会在 paraphrase routing 和 codebook competition 上退化。HoReN 把单层 activation 方向归一化为 key，以离散 value codebook 保存 edit，并只做一步 damped Hopfield query refinement，使 paraphrase 进入相同吸引域而无关 query 尽量保持 locality。exact-v1 在多模型、三类 benchmark 和最多 50K ZsRE edits 报告稳定结果，也披露 codebook 线性增长、threshold/model calibration、temporal conflict 与 multi-hop 未解决。该机制介于 parameter update、external memory、runtime routing 与 registry revision 之间；现有知识树没有单一 owner 能完整承载 edit identity、precedence、rollback 与 serving route，因此保留 Structural Candidate，不直接写入 Books。

<!-- claim:SF-SEQUENTIAL-MODEL-EDIT-SIDECAR:start -->证据边界：只接受 arXiv exact-v1 在上述 method/evaluation contract 内的作者主张；未披露硬件、precision、并发、SLO、artifact commit 或生产条件写 Not Disclosed，不作外推。<!-- claim:SF-SEQUENTIAL-MODEL-EDIT-SIDECAR:end -->
<!-- review:SF-SEQUENTIAL-MODEL-EDIT-SIDECAR:end -->
<!-- review:SF-POLICY-CARRIAGE-INTEGRITY:start -->
### Policy-Carriage Integrity

安全 policy 写进 prompt 不等于它在 action 前仍有效：context assembly 的 eviction、aliasing 与 binding 可以在预算压力下让 directive 消失或弱化。exact-v1 把 policy state 标成 typed provenance，隔离 control budget，在 assembly 前 preflight，并要求 effect-time enforcement。实验只证明所测 assembler 的 state-carriage failure；固定行为校准 0/90 unsafe proposal，不能把 policy absence 直接等同 unsafe action，也不替代 action-boundary reference monitor。

<!-- claim:SF-POLICY-CARRIAGE-INTEGRITY:start -->证据边界：只接受 arXiv exact-v1 在上述 method/evaluation contract 内的作者主张；未披露硬件、precision、并发、SLO、artifact commit 或生产条件写 Not Disclosed，不作外推。<!-- claim:SF-POLICY-CARRIAGE-INTEGRITY:end -->
<!-- review:SF-POLICY-CARRIAGE-INTEGRITY:end -->
<!-- review:SF-QUANTIZATION-BEHAVIORAL-REGRESSION:start -->
### Quantization Behavioral Regression

aggregate perplexity 对低精度的平均误差敏感，却会漏掉少数安全关键 item 的 answer flip。作者在三模型、五 precision、BBQ 与五 seeds 上报告 4-bit 时已有 bias transition 而 perplexity 变化很小，3-bit 更明显。研究只覆盖 post-training quantization、一个 bias benchmark 和有限模型，alignment-layer 解释是推断；长期结论是 model artifact promotion 必须绑定 precision/quantizer/kernel 与 item-level behavior slices。

<!-- claim:SF-QUANTIZATION-BEHAVIORAL-REGRESSION:start -->证据边界：只接受 arXiv exact-v1 在上述 method/evaluation contract 内的作者主张；未披露硬件、precision、并发、SLO、artifact commit 或生产条件写 Not Disclosed，不作外推。<!-- claim:SF-QUANTIZATION-BEHAVIORAL-REGRESSION:end -->
<!-- review:SF-QUANTIZATION-BEHAVIORAL-REGRESSION:end -->

## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-ATTACK-AGENT-TERMINAL-FINGERPRINT | exact-v1 disclosed workload；见 evaluation locator | exact-v1 disclosed model or Not Disclosed | Not Disclosed unless named in Review | Not Disclosed unless named in Review | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | 作者指标的 scoped contract；无通用生产阈值 | authors / task labels / formal proof as applicable |
| SF-COMPUTE-OPTIMAL-TOKENIZATION | exact-v1 disclosed workload；见 evaluation locator | exact-v1 disclosed model or Not Disclosed | Not Disclosed unless named in Review | Not Disclosed unless named in Review | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | 作者指标的 scoped contract；无通用生产阈值 | authors / task labels / formal proof as applicable |
| SF-SENTINEL-VLA-STATUS-CONTROL | exact-v1 disclosed workload；见 evaluation locator | exact-v1 disclosed model or Not Disclosed | Not Disclosed unless named in Review | Not Disclosed unless named in Review | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | 作者指标的 scoped contract；无通用生产阈值 | authors / task labels / formal proof as applicable |
| SF-VLA-ADAPTIVE-TEST-TIME-COMPUTE | exact-v1 disclosed workload；见 evaluation locator | exact-v1 disclosed model or Not Disclosed | Not Disclosed unless named in Review | Not Disclosed unless named in Review | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | 作者指标的 scoped contract；无通用生产阈值 | authors / task labels / formal proof as applicable |
| SF-TAIL-SAFE-RUNTIME-MONITOR | exact-v1 disclosed workload；见 evaluation locator | exact-v1 disclosed model or Not Disclosed | Not Disclosed unless named in Review | Not Disclosed unless named in Review | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | 作者指标的 scoped contract；无通用生产阈值 | authors / task labels / formal proof as applicable |
| SF-VISUOMOTOR-EXECUTION-GUARANTEE | exact-v1 disclosed workload；见 evaluation locator | exact-v1 disclosed model or Not Disclosed | Not Disclosed unless named in Review | Not Disclosed unless named in Review | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | 作者指标的 scoped contract；无通用生产阈值 | authors / task labels / formal proof as applicable |
| SF-GRBEN-PROCESS-REWARD-EVAL | exact-v1 disclosed workload；见 evaluation locator | exact-v1 disclosed model or Not Disclosed | Not Disclosed unless named in Review | Not Disclosed unless named in Review | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | 作者指标的 scoped contract；无通用生产阈值 | authors / task labels / formal proof as applicable |
| SF-BROWSING-AGENT-BEHAVIORAL-FINGERPRINT | exact-v1 disclosed workload；见 evaluation locator | exact-v1 disclosed model or Not Disclosed | Not Disclosed unless named in Review | Not Disclosed unless named in Review | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | 作者指标的 scoped contract；无通用生产阈值 | authors / task labels / formal proof as applicable |
| SF-ACTIVATION-GRADIENT-COMPRESSION | exact-v1 disclosed workload；见 evaluation locator | exact-v1 disclosed model or Not Disclosed | Not Disclosed unless named in Review | Not Disclosed unless named in Review | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | 作者指标的 scoped contract；无通用生产阈值 | authors / task labels / formal proof as applicable |
| SF-PIXEL-LEVEL-RAG-EVIDENCE-CHAIN | exact-v1 disclosed workload；见 evaluation locator | exact-v1 disclosed model or Not Disclosed | Not Disclosed unless named in Review | Not Disclosed unless named in Review | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | 作者指标的 scoped contract；无通用生产阈值 | authors / task labels / formal proof as applicable |
| SF-LOGIC-GROUNDED-SKILL-INDUCTION | exact-v1 disclosed workload；见 evaluation locator | exact-v1 disclosed model or Not Disclosed | Not Disclosed unless named in Review | Not Disclosed unless named in Review | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | 作者指标的 scoped contract；无通用生产阈值 | authors / task labels / formal proof as applicable |
| SF-COUNTERFACTUAL-RISK-RAG | exact-v1 disclosed workload；见 evaluation locator | exact-v1 disclosed model or Not Disclosed | Not Disclosed unless named in Review | Not Disclosed unless named in Review | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | 作者指标的 scoped contract；无通用生产阈值 | authors / task labels / formal proof as applicable |
| SF-CONFOUNDED-LOG-EVALUATION | exact-v1 disclosed workload；见 evaluation locator | exact-v1 disclosed model or Not Disclosed | Not Disclosed unless named in Review | Not Disclosed unless named in Review | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | 作者指标的 scoped contract；无通用生产阈值 | authors / task labels / formal proof as applicable |
| SF-ACCESS-AWARE-VECTOR-INDEX | exact-v1 disclosed workload；见 evaluation locator | exact-v1 disclosed model or Not Disclosed | Not Disclosed unless named in Review | Not Disclosed unless named in Review | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | 作者指标的 scoped contract；无通用生产阈值 | authors / task labels / formal proof as applicable |
| SF-VUDA-CUDA-VULKAN-SHARING | exact-v1 disclosed workload；见 evaluation locator | exact-v1 disclosed model or Not Disclosed | Not Disclosed unless named in Review | Not Disclosed unless named in Review | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | 作者指标的 scoped contract；无通用生产阈值 | authors / task labels / formal proof as applicable |
| SF-LONG-FORM-LENGTH-VOLATILITY | exact-v1 disclosed workload；见 evaluation locator | exact-v1 disclosed model or Not Disclosed | Not Disclosed unless named in Review | Not Disclosed unless named in Review | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | 作者指标的 scoped contract；无通用生产阈值 | authors / task labels / formal proof as applicable |
| SF-PROVENANCE-GRAPH-MEMORY | exact-v1 disclosed workload；见 evaluation locator | exact-v1 disclosed model or Not Disclosed | Not Disclosed unless named in Review | Not Disclosed unless named in Review | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | 作者指标的 scoped contract；无通用生产阈值 | authors / task labels / formal proof as applicable |
| SF-LIVEFMBENCH-SPECIFICATION-EVAL | exact-v1 disclosed workload；见 evaluation locator | exact-v1 disclosed model or Not Disclosed | Not Disclosed unless named in Review | Not Disclosed unless named in Review | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | 作者指标的 scoped contract；无通用生产阈值 | authors / task labels / formal proof as applicable |
| SF-AUTOREGRESSIVE-CREDIT-ATTRIBUTION-BARRIER | exact-v1 disclosed workload；见 evaluation locator | exact-v1 disclosed model or Not Disclosed | Not Disclosed unless named in Review | Not Disclosed unless named in Review | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | 作者指标的 scoped contract；无通用生产阈值 | authors / task labels / formal proof as applicable |
| SF-LORA-COMPOSITION-RELIABILITY | exact-v1 disclosed workload；见 evaluation locator | exact-v1 disclosed model or Not Disclosed | Not Disclosed unless named in Review | Not Disclosed unless named in Review | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | 作者指标的 scoped contract；无通用生产阈值 | authors / task labels / formal proof as applicable |
| SF-AUTONOMOUS-TEST-REPAIR-VALIDATION-BOUNDARY | exact-v1 disclosed workload；见 evaluation locator | exact-v1 disclosed model or Not Disclosed | Not Disclosed unless named in Review | Not Disclosed unless named in Review | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | 作者指标的 scoped contract；无通用生产阈值 | authors / task labels / formal proof as applicable |
| SF-ACTION-AGENT-VIDEO-CONTROL | exact-v1 disclosed workload；见 evaluation locator | exact-v1 disclosed model or Not Disclosed | Not Disclosed unless named in Review | Not Disclosed unless named in Review | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | 作者指标的 scoped contract；无通用生产阈值 | authors / task labels / formal proof as applicable |
| SF-NOTEBOOK-REPRODUCIBILITY-STATE-GATE | exact-v1 disclosed workload；见 evaluation locator | exact-v1 disclosed model or Not Disclosed | Not Disclosed unless named in Review | Not Disclosed unless named in Review | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | 作者指标的 scoped contract；无通用生产阈值 | authors / task labels / formal proof as applicable |
| SF-MULTIAGENT-PARETO-COMPUTE-ALLOCATION | exact-v1 disclosed workload；见 evaluation locator | exact-v1 disclosed model or Not Disclosed | Not Disclosed unless named in Review | Not Disclosed unless named in Review | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | 作者指标的 scoped contract；无通用生产阈值 | authors / task labels / formal proof as applicable |
| SF-DEVELOPER-MEMORY-OPE-GATE | exact-v1 disclosed workload；见 evaluation locator | exact-v1 disclosed model or Not Disclosed | Not Disclosed unless named in Review | Not Disclosed unless named in Review | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | 作者指标的 scoped contract；无通用生产阈值 | authors / task labels / formal proof as applicable |
| SF-PRODUCTION-AGENT-EVALUATION | exact-v1 disclosed workload；见 evaluation locator | exact-v1 disclosed model or Not Disclosed | Not Disclosed unless named in Review | Not Disclosed unless named in Review | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | 作者指标的 scoped contract；无通用生产阈值 | authors / task labels / formal proof as applicable |
| SF-DATA-CONSTRAINED-SCALING-LAW | exact-v1 disclosed workload；见 evaluation locator | exact-v1 disclosed model or Not Disclosed | Not Disclosed unless named in Review | Not Disclosed unless named in Review | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | 作者指标的 scoped contract；无通用生产阈值 | authors / task labels / formal proof as applicable |
| SF-AGENT-SAFETY-SEARCH-MEASUREMENT | exact-v1 disclosed workload；见 evaluation locator | exact-v1 disclosed model or Not Disclosed | Not Disclosed unless named in Review | Not Disclosed unless named in Review | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | 作者指标的 scoped contract；无通用生产阈值 | authors / task labels / formal proof as applicable |
| SF-AGENT-GENERATED-VERIFIED-COMPILER | exact-v1 disclosed workload；见 evaluation locator | exact-v1 disclosed model or Not Disclosed | Not Disclosed unless named in Review | Not Disclosed unless named in Review | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | 作者指标的 scoped contract；无通用生产阈值 | authors / task labels / formal proof as applicable |
| SF-DITRON-DISTRIBUTED-TILING | exact-v1 disclosed workload；见 evaluation locator | exact-v1 disclosed model or Not Disclosed | Not Disclosed unless named in Review | Not Disclosed unless named in Review | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | 作者指标的 scoped contract；无通用生产阈值 | authors / task labels / formal proof as applicable |
| SF-REFUSAL-TRAJECTORY-MONITOR | exact-v1 disclosed workload；见 evaluation locator | exact-v1 disclosed model or Not Disclosed | Not Disclosed unless named in Review | Not Disclosed unless named in Review | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | 作者指标的 scoped contract；无通用生产阈值 | authors / task labels / formal proof as applicable |
| SF-RECURSIVE-STATE-TERMINATION | exact-v1 disclosed workload；见 evaluation locator | exact-v1 disclosed model or Not Disclosed | Not Disclosed unless named in Review | Not Disclosed unless named in Review | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | 作者指标的 scoped contract；无通用生产阈值 | authors / task labels / formal proof as applicable |
| SF-PRUNING-BEHAVIORAL-REGRESSION | exact-v1 disclosed workload；见 evaluation locator | exact-v1 disclosed model or Not Disclosed | Not Disclosed unless named in Review | Not Disclosed unless named in Review | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | 作者指标的 scoped contract；无通用生产阈值 | authors / task labels / formal proof as applicable |
| SF-SEQUENTIAL-MODEL-EDIT-SIDECAR | exact-v1 disclosed workload；见 evaluation locator | exact-v1 disclosed model or Not Disclosed | Not Disclosed unless named in Review | Not Disclosed unless named in Review | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | 作者指标的 scoped contract；无通用生产阈值 | authors / task labels / formal proof as applicable |
| SF-POLICY-CARRIAGE-INTEGRITY | exact-v1 disclosed workload；见 evaluation locator | exact-v1 disclosed model or Not Disclosed | Not Disclosed unless named in Review | Not Disclosed unless named in Review | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | 作者指标的 scoped contract；无通用生产阈值 | authors / task labels / formal proof as applicable |
| SF-QUANTIZATION-BEHAVIORAL-REGRESSION | exact-v1 disclosed workload；见 evaluation locator | exact-v1 disclosed model or Not Disclosed | Not Disclosed unless named in Review | Not Disclosed unless named in Review | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | 作者指标的 scoped contract；无通用生产阈值 | authors / task labels / formal proof as applicable |

<!-- audit-target:deep_analysis_selection:start -->
## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-ATTACK-AGENT-TERMINAL-FINGERPRINT | score_7_9; forced_review | not_selected | — | — | terminal behavioral attribution 与 active forensics 具有安全价值，但现有 Security 已拥有 fingerprint-as-sensor 的完整边界，不高于三个跨层结构问题。 | analysis-decision:SF-ATTACK-AGENT-TERMINAL-FINGERPRINT |
| SF-COMPUTE-OPTIMAL-TOKENIZATION | score_7_9; forced_review; potential_books_delta | selected | DA-20260503-TOKEN-UNIT | — | selected：把 scaling/evaluation 的基本计量从 tokenizer-dependent token 改为可跨 tokenizer 比较的信息单位，并同时传播到训练与推理成本。 | analysis:DA-20260503-TOKEN-UNIT |
| SF-SENTINEL-VLA-STATUS-CONTROL | score_7_9; forced_review; potential_books_delta | not_selected | — | — | 显式 status state machine 很重要，但影响集中在 Ch26 的 reasoning-trigger 分支；完整机制与 fallback 已在 Source Review/Books delta 保留。 | analysis-decision:SF-SENTINEL-VLA-STATUS-CONTROL |
| SF-VLA-ADAPTIVE-TEST-TIME-COMPUTE | score_7_9; forced_review; potential_books_delta | not_selected | — | — | uncertainty-triggered compute 只改变 VLA fast/slow 调度，没有跨越 controller commit 或平台 owner，优先级低于三条跨层路线。 | analysis-decision:SF-VLA-ADAPTIVE-TEST-TIME-COMPUTE |
| SF-TAIL-SAFE-RUNTIME-MONITOR | score_7_9; forced_review; potential_books_delta | not_selected | — | — | 独立 monitor 与 recovery 属于 physical-safety 路线的一条执行分支；与 execution-guarantee family 一并保留，但不重复占长叙事。 | analysis-decision:SF-TAIL-SAFE-RUNTIME-MONITOR |
| SF-VISUOMOTOR-EXECUTION-GUARANTEE | score_7_9; forced_review; potential_books_delta | not_selected | — | — | control-invariant safeset 是强机制证据，但仍归 Ch26 safety monitor/controller handoff；其假设、证明边界与 recovery 已在完整 Review 中闭合。 | analysis-decision:SF-VISUOMOTOR-EXECUTION-GUARANTEE |
| SF-GRBEN-PROCESS-REWARD-EVAL | score_7_9; forced_review | not_selected | — | — | 只为既有 process/trajectory evaluation contract 增加受限 benchmark，Books Decision 为 No Change。 | analysis-decision:SF-GRBEN-PROCESS-REWARD-EVAL |
| SF-BROWSING-AGENT-BEHAVIORAL-FINGERPRINT | score_7_9; forced_review | not_selected | — | — | 浏览行为 fingerprint 为现有 MARK 路线增加受限 measurement evidence；版本漂移与受控任务范围使其保持局部传感器分支。 | analysis-decision:SF-BROWSING-AGENT-BEHAVIORAL-FINGERPRINT |
| SF-ACTIVATION-GRADIENT-COMPRESSION | score_7_9; forced_review; potential_books_delta | not_selected | — | — | operator-aware compression 改变训练 memory/variance 取舍，但 owner 局限于 Distributed Training，不高于跨系统计量与因果证据问题。 | analysis-decision:SF-ACTIVATION-GRADIENT-COMPRESSION |
| SF-PIXEL-LEVEL-RAG-EVIDENCE-CHAIN | score_7_9; forced_review; potential_books_delta | not_selected | — | — | visual region/hop identity 补全 RAG evidence 可定位性，但不转移 source authority 或 claim-verification owner，完整 delta 由 Ch76 局部吸收。 | analysis-decision:SF-PIXEL-LEVEL-RAG-EVIDENCE-CHAIN |
| SF-LOGIC-GROUNDED-SKILL-INDUCTION | score_7_9; forced_review | not_selected | — | — | trace→logic-grounded program 已由 Agent Platform 的 typed Skill compilation 和 Workflow control state 承载，Books Decision 为 No Change。 | analysis-decision:SF-LOGIC-GROUNDED-SKILL-INDUCTION |
| SF-COUNTERFACTUAL-RISK-RAG | score_7_9; forced_review | not_selected | — | — | Evidence Critic 和 risk threshold 具体化既有 verify/abstain 分支，跨领域校准未证明，Books Decision 为 No Change。 | analysis-decision:SF-COUNTERFACTUAL-RISK-RAG |
| SF-CONFOUNDED-LOG-EVALUATION | score_7_9; forced_review; potential_books_delta | selected | DA-20260503-CAUSAL-LOGS | — | selected：OBS/EXP/SIM 的可识别性决定日志能否成为因果 evidence，并扩展到多轮 Agent mediator/state，直接改变平台评测合同。 | analysis:DA-20260503-CAUSAL-LOGS |
| SF-ACCESS-AWARE-VECTOR-INDEX | score_7_9; forced_review | not_selected | — | — | authorization-before-ranking、role graph 与 partition 已由 RAG 章节承载；新工作主要提供实现/性能案例。 | analysis-decision:SF-ACCESS-AWARE-VECTOR-INDEX |
| SF-VUDA-CUDA-VULKAN-SHARING | score_7_9; forced_review; potential_books_delta | not_selected | — | — | cross-API spatial sharing 改变 GPU 隔离实现，但受单一 runtime/driver 条件约束，属于局部平台分支。 | analysis-decision:SF-VUDA-CUDA-VULKAN-SHARING |
| SF-LONG-FORM-LENGTH-VOLATILITY | score_7_9; forced_review; potential_books_delta | not_selected | — | — | output-length variance 改善 decode SLO 建模，但不重分配跨章节 state owner，完整 delta 可在 Ch44 局部吸收。 | analysis-decision:SF-LONG-FORM-LENGTH-VOLATILITY |
| SF-PROVENANCE-GRAPH-MEMORY | score_7_9; forced_review | not_selected | — | — | provenance graph 与 adaptive expansion 已落在 Memory 的 bounded evidence-set retrieval 主线，Books Decision 为 No Change。 | analysis-decision:SF-PROVENANCE-GRAPH-MEMORY |
| SF-LIVEFMBENCH-SPECIFICATION-EVAL | score_7_9; forced_review | not_selected | — | — | formal-spec workload 强化 benchmark identity/contamination/failure-analysis 合同，没有新增通用 evaluator owner。 | analysis-decision:SF-LIVEFMBENCH-SPECIFICATION-EVAL |
| SF-AUTOREGRESSIVE-CREDIT-ATTRIBUTION-BARRIER | score_7_9; forced_review; potential_books_delta | not_selected | — | — | 负面理论结果修正 post-hoc attribution 直觉，但系统处置集中在 RAG provenance admission，不占跨层长叙事。 | analysis-decision:SF-AUTOREGRESSIVE-CREDIT-ATTRIBUTION-BARRIER |
| SF-LORA-COMPOSITION-RELIABILITY | score_7_9; forced_review | not_selected | — | — | 当前 Ch30 已把 adapter composition、compatibility、重新 Evaluation 与 promotion 绑定；multi-view proxy 是受限实现，不再重复写入。 | analysis-decision:SF-LORA-COMPOSITION-RELIABILITY |
| SF-AUTONOMOUS-TEST-REPAIR-VALIDATION-BOUNDARY | score_7_9; forced_review | not_selected | — | — | Ch66 已显式要求 Agent-authored tests 的 assertion/oracle strength、execution path 与 failure discriminativeness；该 case 不再改变长期 contract。 | analysis-decision:SF-AUTONOMOUS-TEST-REPAIR-VALIDATION-BOUNDARY |
| SF-ACTION-AGENT-VIDEO-CONTROL | score_7_9; forced_review | not_selected | — | — | video rehearsal/action denoising 只支持既有 imagination→controller 分层，closed-loop safety 未证明。 | analysis-decision:SF-ACTION-AGENT-VIDEO-CONTROL |
| SF-NOTEBOOK-REPRODUCIBILITY-STATE-GATE | score_7_9; forced_review; potential_books_delta | not_selected | — | — | clean-state equivalence 与 stale-cell gate 改进 durable Workflow artifact，但 owner 局限于 notebook execution state。 | analysis-decision:SF-NOTEBOOK-REPRODUCIBILITY-STATE-GATE |
| SF-MULTIAGENT-PARETO-COMPUTE-ALLOCATION | score_7_9; forced_review; potential_books_delta | not_selected | — | — | equal-budget Pareto accounting 改进 Multi-Agent admission，却受两 benchmark、token compute estimate 与未计通信/尾延迟条件约束。 | analysis-decision:SF-MULTIAGENT-PARETO-COMPUTE-ALLOCATION |
| SF-DEVELOPER-MEMORY-OPE-GATE | score_7_9; forced_review | not_selected | — | — | propensity、shadow policy 与 OPE 是现有 Memory promotion/rollback 合同的实现证据，且没有证明 accuracy gain。 | analysis-decision:SF-DEVELOPER-MEMORY-OPE-GATE |
| SF-PRODUCTION-AGENT-EVALUATION | score_7_9; forced_review | not_selected | — | — | PAEF 指标映射到已有 trajectory/drift/release receipts；没有 production data，Books Decision 为 No Change。 | analysis-decision:SF-PRODUCTION-AGENT-EVALUATION |
| SF-DATA-CONSTRAINED-SCALING-LAW | score_7_9; forced_review | not_selected | — | — | 当前 Ch28 已明确 unique-token volume、repetition、effective parameters 与 data-saturation boundary；该 family 仅补同一命题的受限 fit。 | analysis-decision:SF-DATA-CONSTRAINED-SCALING-LAW |
| SF-AGENT-SAFETY-SEARCH-MEASUREMENT | score_7_9; forced_review; potential_books_delta | not_selected | — | — | search-based safety coverage 是 Evaluation 的重要替代分支，但仍由同一 deployment config/likelihood budget owner 承载。 | analysis-decision:SF-AGENT-SAFETY-SEARCH-MEASUREMENT |
| SF-AGENT-GENERATED-VERIFIED-COMPILER | score_7_9; forced_review; potential_books_delta | not_selected | — | — | testing/certificate/proof/audit 分层补全 coding-agent artifact gate，但仍归平台 Evaluation 的单一 trust-path 分支。 | analysis-decision:SF-AGENT-GENERATED-VERIFIED-COMPILER |
| SF-DITRON-DISTRIBUTED-TILING | score_7_9; forced_review; potential_books_delta | not_selected | — | — | hierarchical tiling 改变 execution-plan/runtime handoff，但证据受特定编译与拓扑 workload 约束，局部吸收即可。 | analysis-decision:SF-DITRON-DISTRIBUTED-TILING |
| SF-REFUSAL-TRAJECTORY-MONITOR | score_7_9; forced_review | not_selected | — | — | trajectory monitor 没有改变 refusal≠safety proof 和 action boundary owns enforcement 的既有结论。 | analysis-decision:SF-REFUSAL-TRAJECTORY-MONITOR |
| SF-RECURSIVE-STATE-TERMINATION | score_7_9; forced_review; potential_books_delta | not_selected | — | — | typed epistemic state/order-gap 是 Reflection stop sensor 的理论分支，既不证明 truth 也不新增 workflow commit owner。 | analysis-decision:SF-RECURSIVE-STATE-TERMINATION |
| SF-PRUNING-BEHAVIORAL-REGRESSION | score_7_9; forced_review; potential_books_delta | not_selected | — | — | item-level pruning regression 补强压缩 release gate，但仍属于 Evaluation 的单一 artifact transformation 分支。 | analysis-decision:SF-PRUNING-BEHAVIORAL-REGRESSION |
| SF-SEQUENTIAL-MODEL-EDIT-SIDECAR | score_7_9; forced_review; potential_structural_gap | selected | DA-20260503-SEQUENTIAL-MODEL-EDIT | — | selected：base weights、external edit memory、runtime override 与 registry lineage 分属多个现有 owner，暴露当前知识树没有 canonical model-edit lifecycle 的结构缺口。 | analysis:DA-20260503-SEQUENTIAL-MODEL-EDIT |
| SF-POLICY-CARRIAGE-INTEGRITY | score_7_9; forced_review; potential_books_delta | not_selected | — | — | policy-carriage invariant 跨 Context 与 action boundary，但机制 delta 已可在现有两个 owner 间明确 handoff；优先级低于尚无 owner 的 model-edit gap。 | analysis-decision:SF-POLICY-CARRIAGE-INTEGRITY |
| SF-QUANTIZATION-BEHAVIORAL-REGRESSION | score_7_9; forced_review | not_selected | — | — | dense-vs-quantized behavioral regression 已完整存在于 Execution/Evaluation release gate，Books Decision 为 No Change。 | analysis-decision:SF-QUANTIZATION-BEHAVIORAL-REGRESSION |
<!-- analysis-decision:SF-ATTACK-AGENT-TERMINAL-FINGERPRINT:start -->
terminal behavioral attribution 与 active forensics 具有安全价值，但现有 Security 已拥有 fingerprint-as-sensor 的完整边界，不高于三个跨层结构问题。
<!-- analysis-decision:SF-ATTACK-AGENT-TERMINAL-FINGERPRINT:end -->
<!-- analysis-decision:SF-SENTINEL-VLA-STATUS-CONTROL:start -->
显式 status state machine 很重要，但影响集中在 Ch26 的 reasoning-trigger 分支；完整机制与 fallback 已在 Source Review/Books delta 保留。
<!-- analysis-decision:SF-SENTINEL-VLA-STATUS-CONTROL:end -->
<!-- analysis-decision:SF-VLA-ADAPTIVE-TEST-TIME-COMPUTE:start -->
uncertainty-triggered compute 只改变 VLA fast/slow 调度，没有跨越 controller commit 或平台 owner，优先级低于三条跨层路线。
<!-- analysis-decision:SF-VLA-ADAPTIVE-TEST-TIME-COMPUTE:end -->
<!-- analysis-decision:SF-TAIL-SAFE-RUNTIME-MONITOR:start -->
独立 monitor 与 recovery 属于 physical-safety 路线的一条执行分支；与 execution-guarantee family 一并保留，但不重复占长叙事。
<!-- analysis-decision:SF-TAIL-SAFE-RUNTIME-MONITOR:end -->
<!-- analysis-decision:SF-VISUOMOTOR-EXECUTION-GUARANTEE:start -->
control-invariant safeset 是强机制证据，但仍归 Ch26 safety monitor/controller handoff；其假设、证明边界与 recovery 已在完整 Review 中闭合。
<!-- analysis-decision:SF-VISUOMOTOR-EXECUTION-GUARANTEE:end -->
<!-- analysis-decision:SF-GRBEN-PROCESS-REWARD-EVAL:start -->
只为既有 process/trajectory evaluation contract 增加受限 benchmark，Books Decision 为 No Change。
<!-- analysis-decision:SF-GRBEN-PROCESS-REWARD-EVAL:end -->
<!-- analysis-decision:SF-BROWSING-AGENT-BEHAVIORAL-FINGERPRINT:start -->
浏览行为 fingerprint 为现有 MARK 路线增加受限 measurement evidence；版本漂移与受控任务范围使其保持局部传感器分支。
<!-- analysis-decision:SF-BROWSING-AGENT-BEHAVIORAL-FINGERPRINT:end -->
<!-- analysis-decision:SF-ACTIVATION-GRADIENT-COMPRESSION:start -->
operator-aware compression 改变训练 memory/variance 取舍，但 owner 局限于 Distributed Training，不高于跨系统计量与因果证据问题。
<!-- analysis-decision:SF-ACTIVATION-GRADIENT-COMPRESSION:end -->
<!-- analysis-decision:SF-PIXEL-LEVEL-RAG-EVIDENCE-CHAIN:start -->
visual region/hop identity 补全 RAG evidence 可定位性，但不转移 source authority 或 claim-verification owner，完整 delta 由 Ch76 局部吸收。
<!-- analysis-decision:SF-PIXEL-LEVEL-RAG-EVIDENCE-CHAIN:end -->
<!-- analysis-decision:SF-LOGIC-GROUNDED-SKILL-INDUCTION:start -->
trace→logic-grounded program 已由 Agent Platform 的 typed Skill compilation 和 Workflow control state 承载，Books Decision 为 No Change。
<!-- analysis-decision:SF-LOGIC-GROUNDED-SKILL-INDUCTION:end -->
<!-- analysis-decision:SF-COUNTERFACTUAL-RISK-RAG:start -->
Evidence Critic 和 risk threshold 具体化既有 verify/abstain 分支，跨领域校准未证明，Books Decision 为 No Change。
<!-- analysis-decision:SF-COUNTERFACTUAL-RISK-RAG:end -->
<!-- analysis-decision:SF-ACCESS-AWARE-VECTOR-INDEX:start -->
authorization-before-ranking、role graph 与 partition 已由 RAG 章节承载；新工作主要提供实现/性能案例。
<!-- analysis-decision:SF-ACCESS-AWARE-VECTOR-INDEX:end -->
<!-- analysis-decision:SF-VUDA-CUDA-VULKAN-SHARING:start -->
cross-API spatial sharing 改变 GPU 隔离实现，但受单一 runtime/driver 条件约束，属于局部平台分支。
<!-- analysis-decision:SF-VUDA-CUDA-VULKAN-SHARING:end -->
<!-- analysis-decision:SF-LONG-FORM-LENGTH-VOLATILITY:start -->
output-length variance 改善 decode SLO 建模，但不重分配跨章节 state owner，完整 delta 可在 Ch44 局部吸收。
<!-- analysis-decision:SF-LONG-FORM-LENGTH-VOLATILITY:end -->
<!-- analysis-decision:SF-PROVENANCE-GRAPH-MEMORY:start -->
provenance graph 与 adaptive expansion 已落在 Memory 的 bounded evidence-set retrieval 主线，Books Decision 为 No Change。
<!-- analysis-decision:SF-PROVENANCE-GRAPH-MEMORY:end -->
<!-- analysis-decision:SF-LIVEFMBENCH-SPECIFICATION-EVAL:start -->
formal-spec workload 强化 benchmark identity/contamination/failure-analysis 合同，没有新增通用 evaluator owner。
<!-- analysis-decision:SF-LIVEFMBENCH-SPECIFICATION-EVAL:end -->
<!-- analysis-decision:SF-AUTOREGRESSIVE-CREDIT-ATTRIBUTION-BARRIER:start -->
负面理论结果修正 post-hoc attribution 直觉，但系统处置集中在 RAG provenance admission，不占跨层长叙事。
<!-- analysis-decision:SF-AUTOREGRESSIVE-CREDIT-ATTRIBUTION-BARRIER:end -->
<!-- analysis-decision:SF-LORA-COMPOSITION-RELIABILITY:start -->
post-retrieval composition audit 改进 TRAIN-LORA lifecycle，但 matched workload 与 uncalibrated proxy 使结论保持局部分支。
<!-- analysis-decision:SF-LORA-COMPOSITION-RELIABILITY:end -->
<!-- analysis-decision:SF-AUTONOMOUS-TEST-REPAIR-VALIDATION-BOUNDARY:start -->
assertion weakening/test deletion 是重要 evaluator gaming 反例，但处置集中于 Ch66 的 semantic oracle/scope gate，不占本日跨层长叙事。
<!-- analysis-decision:SF-AUTONOMOUS-TEST-REPAIR-VALIDATION-BOUNDARY:end -->
<!-- analysis-decision:SF-ACTION-AGENT-VIDEO-CONTROL:start -->
video rehearsal/action denoising 只支持既有 imagination→controller 分层，closed-loop safety 未证明。
<!-- analysis-decision:SF-ACTION-AGENT-VIDEO-CONTROL:end -->
<!-- analysis-decision:SF-NOTEBOOK-REPRODUCIBILITY-STATE-GATE:start -->
clean-state equivalence 与 stale-cell gate 改进 durable Workflow artifact，但 owner 局限于 notebook execution state。
<!-- analysis-decision:SF-NOTEBOOK-REPRODUCIBILITY-STATE-GATE:end -->
<!-- analysis-decision:SF-MULTIAGENT-PARETO-COMPUTE-ALLOCATION:start -->
equal-budget Pareto accounting 改进 Multi-Agent admission，却受两 benchmark、token compute estimate 与未计通信/尾延迟条件约束。
<!-- analysis-decision:SF-MULTIAGENT-PARETO-COMPUTE-ALLOCATION:end -->
<!-- analysis-decision:SF-DEVELOPER-MEMORY-OPE-GATE:start -->
propensity、shadow policy 与 OPE 是现有 Memory promotion/rollback 合同的实现证据，且没有证明 accuracy gain。
<!-- analysis-decision:SF-DEVELOPER-MEMORY-OPE-GATE:end -->
<!-- analysis-decision:SF-PRODUCTION-AGENT-EVALUATION:start -->
PAEF 指标映射到已有 trajectory/drift/release receipts；没有 production data，Books Decision 为 No Change。
<!-- analysis-decision:SF-PRODUCTION-AGENT-EVALUATION:end -->
<!-- analysis-decision:SF-DATA-CONSTRAINED-SCALING-LAW:start -->
unique-data/repetition 双项会改变 pretraining allocation，但实验 scale 有界，适合作为 Ch28 条件分支而非本日报跨层主线。
<!-- analysis-decision:SF-DATA-CONSTRAINED-SCALING-LAW:end -->
<!-- analysis-decision:SF-AGENT-SAFETY-SEARCH-MEASUREMENT:start -->
search-based safety coverage 是 Evaluation 的重要替代分支，但仍由同一 deployment config/likelihood budget owner 承载。
<!-- analysis-decision:SF-AGENT-SAFETY-SEARCH-MEASUREMENT:end -->
<!-- analysis-decision:SF-AGENT-GENERATED-VERIFIED-COMPILER:start -->
testing/certificate/proof/audit 分层补全 coding-agent artifact gate，但仍归平台 Evaluation 的单一 trust-path 分支。
<!-- analysis-decision:SF-AGENT-GENERATED-VERIFIED-COMPILER:end -->
<!-- analysis-decision:SF-DITRON-DISTRIBUTED-TILING:start -->
hierarchical tiling 改变 execution-plan/runtime handoff，但证据受特定编译与拓扑 workload 约束，局部吸收即可。
<!-- analysis-decision:SF-DITRON-DISTRIBUTED-TILING:end -->
<!-- analysis-decision:SF-REFUSAL-TRAJECTORY-MONITOR:start -->
trajectory monitor 没有改变 refusal≠safety proof 和 action boundary owns enforcement 的既有结论。
<!-- analysis-decision:SF-REFUSAL-TRAJECTORY-MONITOR:end -->
<!-- analysis-decision:SF-RECURSIVE-STATE-TERMINATION:start -->
typed epistemic state/order-gap 是 Reflection stop sensor 的理论分支，既不证明 truth 也不新增 workflow commit owner。
<!-- analysis-decision:SF-RECURSIVE-STATE-TERMINATION:end -->
<!-- analysis-decision:SF-PRUNING-BEHAVIORAL-REGRESSION:start -->
item-level pruning regression 补强压缩 release gate，但仍属于 Evaluation 的单一 artifact transformation 分支。
<!-- analysis-decision:SF-PRUNING-BEHAVIORAL-REGRESSION:end -->
<!-- analysis-decision:SF-POLICY-CARRIAGE-INTEGRITY:start -->
policy-carriage invariant 跨 Context 与 action boundary，但机制 delta 已可在现有两个 owner 间明确 handoff；优先级低于尚无 owner 的 model-edit gap。
<!-- analysis-decision:SF-POLICY-CARRIAGE-INTEGRITY:end -->
<!-- analysis-decision:SF-QUANTIZATION-BEHAVIORAL-REGRESSION:start -->
dense-vs-quantized behavioral regression 已完整存在于 Execution/Evaluation release gate，Books Decision 为 No Change。
<!-- analysis-decision:SF-QUANTIZATION-BEHAVIORAL-REGRESSION:end -->

### Token 不是稳定的数据单位
<!-- analysis:DA-20260503-TOKEN-UNIT:start -->
旧 scaling law 用 token 表达 data，因为同一 tokenizer 内便于计数；compression rate 可变后，token 数不再表示相同信息量。bytes 使跨 tokenizer 比较成立，代价是 tokenizer 与模型规模、训练 FLOPs、decode 长度共同优化。证据未证明固定 compression rate 普遍最优。
<!-- analysis:DA-20260503-TOKEN-UNIT:end -->

### 日志规模不能修复选择偏差
<!-- analysis:DA-20260503-CAUSAL-LOGS:start -->
OBS 很大但 model choice 被 user/context confound；SIM 能重放 output，outcome relation 仍需随机 EXP anchor。演进是 logs → causal graph → EXP+SIM identification → OBS variance reduction，代价是实验成本与严格假设；多轮 Agent 还要重建 mediator/state。
<!-- analysis:DA-20260503-CAUSAL-LOGS:end -->

### 持续模型编辑不是一次权重补丁
<!-- analysis:DA-20260503-SEQUENTIAL-MODEL-EDIT:start -->
直接修改 shared weights 能让新事实进入模型，却会让连续小样本 edit 累积干扰；完全外置 memory 保住 base weights，又把 paraphrase routing、冲突优先级与 serving override 变成新的系统责任。归一化 edit codebook 与一步 Hopfield refinement 把事实修正演化为 parameter-preserving sidecar，但收益依赖 routing/locality calibration，代价是线性增长的派生状态、temporal conflict、multi-hop gap 与 rollback 治理。base weights、edit state、runtime router 和 registry lineage 分属不同 owner，暴露现有知识树缺少完整 model-edit lifecycle 的结构问题。
<!-- analysis:DA-20260503-SEQUENTIAL-MODEL-EDIT:end -->
<!-- audit-target:deep_analysis_selection:end -->

<!-- audit-target:books:start -->
## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-ATTACK-AGENT-TERMINAL-FINGERPRINT | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L10 | books/part-06-ai-infrastructure/66-evaluation-system.md#L10; books/part-07-agent/78-tool-calling.md#L10 | existing:SF-ATTACK-AGENT-TERMINAL-FINGERPRINT | delta:SF-ATTACK-AGENT-TERMINAL-FINGERPRINT | Principle Reuse | No Change — Existing Coverage | books-review:SF-ATTACK-AGENT-TERMINAL-FINGERPRINT |
| SF-COMPUTE-OPTIMAL-TOKENIZATION | MODEL-TOKENIZER | books/part-02-model/11-tokenizer.md#L10 | books/part-02-model/12-embedding.md#L10; books/part-04-training-system/28-pretraining.md#L10 | existing:SF-COMPUTE-OPTIMAL-TOKENIZATION | delta:SF-COMPUTE-OPTIMAL-TOKENIZATION | Direct Evolution | Integrate | books-review:SF-COMPUTE-OPTIMAL-TOKENIZATION |
| SF-SENTINEL-VLA-STATUS-CONTROL | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L10 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L10; books/part-04-training-system/27-data.md#L10 | existing:SF-SENTINEL-VLA-STATUS-CONTROL | delta:SF-SENTINEL-VLA-STATUS-CONTROL | Direct Evolution | Integrate | books-review:SF-SENTINEL-VLA-STATUS-CONTROL |
| SF-VLA-ADAPTIVE-TEST-TIME-COMPUTE | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L10 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L10; books/part-04-training-system/27-data.md#L10 | existing:SF-VLA-ADAPTIVE-TEST-TIME-COMPUTE | delta:SF-VLA-ADAPTIVE-TEST-TIME-COMPUTE | Direct Evolution | Integrate | books-review:SF-VLA-ADAPTIVE-TEST-TIME-COMPUTE |
| SF-TAIL-SAFE-RUNTIME-MONITOR | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L10 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L10; books/part-04-training-system/27-data.md#L10 | existing:SF-TAIL-SAFE-RUNTIME-MONITOR | delta:SF-TAIL-SAFE-RUNTIME-MONITOR | Direct Evolution | Integrate | books-review:SF-TAIL-SAFE-RUNTIME-MONITOR |
| SF-VISUOMOTOR-EXECUTION-GUARANTEE | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L10 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L10; books/part-04-training-system/27-data.md#L10 | existing:SF-VISUOMOTOR-EXECUTION-GUARANTEE | delta:SF-VISUOMOTOR-EXECUTION-GUARANTEE | Direct Evolution | Integrate | books-review:SF-VISUOMOTOR-EXECUTION-GUARANTEE |
| SF-GRBEN-PROCESS-REWARD-EVAL | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L10 | books/part-06-ai-infrastructure/67-monitoring.md#L10; books/part-06-ai-infrastructure/73-production-best-practice.md#L10 | existing:SF-GRBEN-PROCESS-REWARD-EVAL | delta:SF-GRBEN-PROCESS-REWARD-EVAL | Principle Reuse | No Change — Existing Coverage | books-review:SF-GRBEN-PROCESS-REWARD-EVAL |
| SF-BROWSING-AGENT-BEHAVIORAL-FINGERPRINT | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L10 | books/part-06-ai-infrastructure/66-evaluation-system.md#L10; books/part-07-agent/78-tool-calling.md#L10 | existing:SF-BROWSING-AGENT-BEHAVIORAL-FINGERPRINT | delta:SF-BROWSING-AGENT-BEHAVIORAL-FINGERPRINT | Principle Reuse | No Change — Existing Coverage | books-review:SF-BROWSING-AGENT-BEHAVIORAL-FINGERPRINT |
| SF-ACTIVATION-GRADIENT-COMPRESSION | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#L10 | books/part-04-training-system/35-checkpoint.md#L10; books/part-04-training-system/37-tensor-parallel.md#L10 | existing:SF-ACTIVATION-GRADIENT-COMPRESSION | delta:SF-ACTIVATION-GRADIENT-COMPRESSION | Direct Evolution | Integrate | books-review:SF-ACTIVATION-GRADIENT-COMPRESSION |
| SF-PIXEL-LEVEL-RAG-EVIDENCE-CHAIN | AGENT-RAG | books/part-07-agent/76-rag.md#L10 | books/part-07-agent/75-context.md#L10; books/part-07-agent/77-memory.md#L10 | existing:SF-PIXEL-LEVEL-RAG-EVIDENCE-CHAIN | delta:SF-PIXEL-LEVEL-RAG-EVIDENCE-CHAIN | Direct Evolution | Integrate | books-review:SF-PIXEL-LEVEL-RAG-EVIDENCE-CHAIN |
| SF-LOGIC-GROUNDED-SKILL-INDUCTION | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#L10 | books/part-07-agent/80-reflection.md#L10; books/part-07-agent/82-multi-agent.md#L10 | existing:SF-LOGIC-GROUNDED-SKILL-INDUCTION | delta:SF-LOGIC-GROUNDED-SKILL-INDUCTION | Principle Reuse | No Change — Existing Coverage | books-review:SF-LOGIC-GROUNDED-SKILL-INDUCTION |
| SF-COUNTERFACTUAL-RISK-RAG | AGENT-RAG | books/part-07-agent/76-rag.md#L10 | books/part-07-agent/75-context.md#L10; books/part-07-agent/77-memory.md#L10 | existing:SF-COUNTERFACTUAL-RISK-RAG | delta:SF-COUNTERFACTUAL-RISK-RAG | Principle Reuse | No Change — Existing Coverage | books-review:SF-COUNTERFACTUAL-RISK-RAG |
| SF-CONFOUNDED-LOG-EVALUATION | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L10 | books/part-06-ai-infrastructure/67-monitoring.md#L10; books/part-06-ai-infrastructure/73-production-best-practice.md#L10 | existing:SF-CONFOUNDED-LOG-EVALUATION | delta:SF-CONFOUNDED-LOG-EVALUATION | Direct Evolution | Integrate | books-review:SF-CONFOUNDED-LOG-EVALUATION |
| SF-ACCESS-AWARE-VECTOR-INDEX | AGENT-RAG | books/part-07-agent/76-rag.md#L10 | books/part-07-agent/75-context.md#L10; books/part-07-agent/77-memory.md#L10 | existing:SF-ACCESS-AWARE-VECTOR-INDEX | delta:SF-ACCESS-AWARE-VECTOR-INDEX | Principle Reuse | No Change — Existing Coverage | books-review:SF-ACCESS-AWARE-VECTOR-INDEX |
| SF-VUDA-CUDA-VULKAN-SHARING | PLATFORM-GPU-SCHEDULER | books/part-06-ai-infrastructure/63-gpu-scheduler.md#L10 | books/part-06-ai-infrastructure/62-gateway.md#L10; books/part-06-ai-infrastructure/64-volcano.md#L10 | existing:SF-VUDA-CUDA-VULKAN-SHARING | delta:SF-VUDA-CUDA-VULKAN-SHARING | Direct Evolution | Integrate | books-review:SF-VUDA-CUDA-VULKAN-SHARING |
| SF-LONG-FORM-LENGTH-VOLATILITY | INFER-DECODE | books/part-05-inference-system/44-decode.md#L10 | books/part-05-inference-system/43-prefill.md#L10; books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L10 | existing:SF-LONG-FORM-LENGTH-VOLATILITY | delta:SF-LONG-FORM-LENGTH-VOLATILITY | Direct Evolution | Integrate | books-review:SF-LONG-FORM-LENGTH-VOLATILITY |
| SF-PROVENANCE-GRAPH-MEMORY | AGENT-MEMORY | books/part-07-agent/77-memory.md#L10 | books/part-07-agent/76-rag.md#L10; books/part-07-agent/78-tool-calling.md#L10 | existing:SF-PROVENANCE-GRAPH-MEMORY | delta:SF-PROVENANCE-GRAPH-MEMORY | Principle Reuse | No Change — Existing Coverage | books-review:SF-PROVENANCE-GRAPH-MEMORY |
| SF-LIVEFMBENCH-SPECIFICATION-EVAL | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L10 | books/part-06-ai-infrastructure/67-monitoring.md#L10; books/part-06-ai-infrastructure/73-production-best-practice.md#L10 | existing:SF-LIVEFMBENCH-SPECIFICATION-EVAL | delta:SF-LIVEFMBENCH-SPECIFICATION-EVAL | Principle Reuse | No Change — Existing Coverage | books-review:SF-LIVEFMBENCH-SPECIFICATION-EVAL |
| SF-AUTOREGRESSIVE-CREDIT-ATTRIBUTION-BARRIER | AGENT-RAG | books/part-07-agent/76-rag.md#L10 | books/part-07-agent/75-context.md#L10; books/part-07-agent/77-memory.md#L10 | existing:SF-AUTOREGRESSIVE-CREDIT-ATTRIBUTION-BARRIER | delta:SF-AUTOREGRESSIVE-CREDIT-ATTRIBUTION-BARRIER | Direct Evolution | Integrate | books-review:SF-AUTOREGRESSIVE-CREDIT-ATTRIBUTION-BARRIER |
| SF-LORA-COMPOSITION-RELIABILITY | TRAIN-LORA | books/part-04-training-system/30-lora.md#L10 | books/part-04-training-system/29-sft.md#L10; books/part-04-training-system/35-checkpoint.md#L10 | existing:SF-LORA-COMPOSITION-RELIABILITY | delta:SF-LORA-COMPOSITION-RELIABILITY | Principle Reuse | No Change — Existing Coverage | books-review:SF-LORA-COMPOSITION-RELIABILITY |
| SF-AUTONOMOUS-TEST-REPAIR-VALIDATION-BOUNDARY | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L10 | books/part-06-ai-infrastructure/67-monitoring.md#L10; books/part-06-ai-infrastructure/73-production-best-practice.md#L10 | existing:SF-AUTONOMOUS-TEST-REPAIR-VALIDATION-BOUNDARY | delta:SF-AUTONOMOUS-TEST-REPAIR-VALIDATION-BOUNDARY | Principle Reuse | No Change — Existing Coverage | books-review:SF-AUTONOMOUS-TEST-REPAIR-VALIDATION-BOUNDARY |
| SF-ACTION-AGENT-VIDEO-CONTROL | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L10 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L10; books/part-04-training-system/27-data.md#L10 | existing:SF-ACTION-AGENT-VIDEO-CONTROL | delta:SF-ACTION-AGENT-VIDEO-CONTROL | Principle Reuse | No Change — Existing Coverage | books-review:SF-ACTION-AGENT-VIDEO-CONTROL |
| SF-NOTEBOOK-REPRODUCIBILITY-STATE-GATE | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#L10 | books/part-07-agent/80-reflection.md#L10; books/part-07-agent/82-multi-agent.md#L10 | existing:SF-NOTEBOOK-REPRODUCIBILITY-STATE-GATE | delta:SF-NOTEBOOK-REPRODUCIBILITY-STATE-GATE | Direct Evolution | Integrate | books-review:SF-NOTEBOOK-REPRODUCIBILITY-STATE-GATE |
| SF-MULTIAGENT-PARETO-COMPUTE-ALLOCATION | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#L10 | books/part-07-agent/81-workflow.md#L10; books/part-07-agent/83-mcp.md#L10 | existing:SF-MULTIAGENT-PARETO-COMPUTE-ALLOCATION | delta:SF-MULTIAGENT-PARETO-COMPUTE-ALLOCATION | Direct Evolution | Integrate | books-review:SF-MULTIAGENT-PARETO-COMPUTE-ALLOCATION |
| SF-DEVELOPER-MEMORY-OPE-GATE | AGENT-MEMORY | books/part-07-agent/77-memory.md#L10 | books/part-07-agent/76-rag.md#L10; books/part-07-agent/78-tool-calling.md#L10 | existing:SF-DEVELOPER-MEMORY-OPE-GATE | delta:SF-DEVELOPER-MEMORY-OPE-GATE | Principle Reuse | No Change — Existing Coverage | books-review:SF-DEVELOPER-MEMORY-OPE-GATE |
| SF-PRODUCTION-AGENT-EVALUATION | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L10 | books/part-06-ai-infrastructure/67-monitoring.md#L10; books/part-06-ai-infrastructure/73-production-best-practice.md#L10 | existing:SF-PRODUCTION-AGENT-EVALUATION | delta:SF-PRODUCTION-AGENT-EVALUATION | Principle Reuse | No Change — Existing Coverage | books-review:SF-PRODUCTION-AGENT-EVALUATION |
| SF-DATA-CONSTRAINED-SCALING-LAW | TRAIN-PRETRAINING | books/part-04-training-system/28-pretraining.md#L10 | books/part-04-training-system/27-data.md#L10; books/part-04-training-system/29-sft.md#L10 | existing:SF-DATA-CONSTRAINED-SCALING-LAW | delta:SF-DATA-CONSTRAINED-SCALING-LAW | Principle Reuse | No Change — Existing Coverage | books-review:SF-DATA-CONSTRAINED-SCALING-LAW |
| SF-AGENT-SAFETY-SEARCH-MEASUREMENT | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L10 | books/part-06-ai-infrastructure/67-monitoring.md#L10; books/part-06-ai-infrastructure/73-production-best-practice.md#L10 | existing:SF-AGENT-SAFETY-SEARCH-MEASUREMENT | delta:SF-AGENT-SAFETY-SEARCH-MEASUREMENT | Direct Evolution | Integrate | books-review:SF-AGENT-SAFETY-SEARCH-MEASUREMENT |
| SF-AGENT-GENERATED-VERIFIED-COMPILER | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L10 | books/part-06-ai-infrastructure/67-monitoring.md#L10; books/part-06-ai-infrastructure/73-production-best-practice.md#L10 | existing:SF-AGENT-GENERATED-VERIFIED-COMPILER | delta:SF-AGENT-GENERATED-VERIFIED-COMPILER | Direct Evolution | Integrate | books-review:SF-AGENT-GENERATED-VERIFIED-COMPILER |
| SF-DITRON-DISTRIBUTED-TILING | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#L10 | books/part-05-inference-system/48-speculative-decoding.md#L10; books/part-05-inference-system/50-vllm.md#L10 | existing:SF-DITRON-DISTRIBUTED-TILING | delta:SF-DITRON-DISTRIBUTED-TILING | Direct Evolution | Integrate | books-review:SF-DITRON-DISTRIBUTED-TILING |
| SF-REFUSAL-TRAJECTORY-MONITOR | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L10 | books/part-06-ai-infrastructure/66-evaluation-system.md#L10; books/part-07-agent/78-tool-calling.md#L10 | existing:SF-REFUSAL-TRAJECTORY-MONITOR | delta:SF-REFUSAL-TRAJECTORY-MONITOR | Principle Reuse | No Change — Existing Coverage | books-review:SF-REFUSAL-TRAJECTORY-MONITOR |
| SF-RECURSIVE-STATE-TERMINATION | AGENT-REFLECTION | books/part-07-agent/80-reflection.md#L10 | books/part-07-agent/79-planning.md#L10; books/part-07-agent/81-workflow.md#L10 | existing:SF-RECURSIVE-STATE-TERMINATION | delta:SF-RECURSIVE-STATE-TERMINATION | Direct Evolution | Integrate | books-review:SF-RECURSIVE-STATE-TERMINATION |
| SF-PRUNING-BEHAVIORAL-REGRESSION | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L10 | books/part-06-ai-infrastructure/67-monitoring.md#L10; books/part-06-ai-infrastructure/73-production-best-practice.md#L10 | existing:SF-PRUNING-BEHAVIORAL-REGRESSION | delta:SF-PRUNING-BEHAVIORAL-REGRESSION | Direct Evolution | Integrate | books-review:SF-PRUNING-BEHAVIORAL-REGRESSION |
| SF-SEQUENTIAL-MODEL-EDIT-SIDECAR | considered:PLATFORM-MODEL-REGISTRY,TRAIN-LORA,AGENT-MEMORY | books/part-06-ai-infrastructure/59-model-registry.md#L10 | books/part-04-training-system/30-lora.md#L10; books/part-06-ai-infrastructure/61-kserve.md#L10 | existing:SF-SEQUENTIAL-MODEL-EDIT-SIDECAR | delta:SF-SEQUENTIAL-MODEL-EDIT-SIDECAR | Alternative Branch | Structural Candidate | books-review:SF-SEQUENTIAL-MODEL-EDIT-SIDECAR |
| SF-POLICY-CARRIAGE-INTEGRITY | AGENT-CONTEXT | books/part-07-agent/75-context.md#L10 | books/part-07-agent/74-prompt.md#L10; books/part-07-agent/76-rag.md#L10 | existing:SF-POLICY-CARRIAGE-INTEGRITY | delta:SF-POLICY-CARRIAGE-INTEGRITY | Direct Evolution | Integrate | books-review:SF-POLICY-CARRIAGE-INTEGRITY |
| SF-QUANTIZATION-BEHAVIORAL-REGRESSION | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L10 | books/part-06-ai-infrastructure/67-monitoring.md#L10; books/part-06-ai-infrastructure/73-production-best-practice.md#L10 | existing:SF-QUANTIZATION-BEHAVIORAL-REGRESSION | delta:SF-QUANTIZATION-BEHAVIORAL-REGRESSION | Principle Reuse | No Change — Existing Coverage | books-review:SF-QUANTIZATION-BEHAVIORAL-REGRESSION |
<!-- books-review:SF-ATTACK-AGENT-TERMINAL-FINGERPRINT:start -->
<!-- existing:SF-ATTACK-AGENT-TERMINAL-FINGERPRINT:start -->已对读当前 owner `books/part-06-ai-infrastructure/72-security.md#L10` 与相邻 handoff `books/part-06-ai-infrastructure/66-evaluation-system.md#L10; books/part-07-agent/78-tool-calling.md#L10`。Security 已把 black-box model/agent fingerprint 定义为会受版本、scaffold 与对抗策略漂移的风险 sensor，并明确不得把 classifier output 当身份 credential；Trace 的 terminal sequence/DPI 路线落在该边界内。<!-- existing:SF-ATTACK-AGENT-TERMINAL-FINGERPRINT:end -->
<!-- delta:SF-ATTACK-AGENT-TERMINAL-FINGERPRINT:start -->terminal-command bigram 与 family-routed active forensics 扩展了 fingerprint modality，但仍是可漂移、可规避且会被 scaffold 混淆的 sensor；现有 Security contract 已要求独立身份/授权与保守 fallback。<!-- delta:SF-ATTACK-AGENT-TERMINAL-FINGERPRINT:end -->
结论：**No Change — Existing Coverage**。
<!-- books-review:SF-ATTACK-AGENT-TERMINAL-FINGERPRINT:end -->
<!-- books-review:SF-COMPUTE-OPTIMAL-TOKENIZATION:start -->
<!-- existing:SF-COMPUTE-OPTIMAL-TOKENIZATION:start -->已对读当前 owner `books/part-02-model/11-tokenizer.md#L10` 与相邻 handoff `books/part-02-model/12-embedding.md#L10; books/part-04-training-system/28-pretraining.md#L10`。Tokenizer 已解释 segmentation、vocabulary 与压缩率如何改变 token sequence 和上下文成本，但跨 tokenizer/scaling 比较仍以 token 为默认单位，尚未建立 bytes 口径。<!-- existing:SF-COMPUTE-OPTIMAL-TOKENIZATION:end -->
<!-- delta:SF-COMPUTE-OPTIMAL-TOKENIZATION:start -->在 token lifecycle 后补入 bytes 作为 scaling/evaluation 的 canonical information unit，并把 compression rate 对训练 FLOPs、序列长度和 inference latency 的双向影响交接给 Pretraining。<!-- delta:SF-COMPUTE-OPTIMAL-TOKENIZATION:end -->
结论：**Integrate**。
<!-- books-review:SF-COMPUTE-OPTIMAL-TOKENIZATION:end -->
<!-- books-review:SF-SENTINEL-VLA-STATUS-CONTROL:start -->
<!-- existing:SF-SENTINEL-VLA-STATUS-CONTROL:start -->已对读当前 owner `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L10` 与相邻 handoff `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L10; books/part-04-training-system/27-data.md#L10`。Ch26 已把高层 reasoning、动作 proposal、低层 controller 与安全 fallback 分层，也说明 fast/slow path；尚未把执行状态建模为显式、可审计的触发状态机。<!-- existing:SF-SENTINEL-VLA-STATUS-CONTROL:end -->
<!-- delta:SF-SENTINEL-VLA-STATUS-CONTROL:start -->在 VLA fast/slow 与 runtime monitor 之间补入显式 status state machine：monitor 只触发 plan/update/recover，Normal 路径复用 thought memory；未校准或超时交回保守 controller。<!-- delta:SF-SENTINEL-VLA-STATUS-CONTROL:end -->
结论：**Integrate**。
<!-- books-review:SF-SENTINEL-VLA-STATUS-CONTROL:end -->
<!-- books-review:SF-VLA-ADAPTIVE-TEST-TIME-COMPUTE:start -->
<!-- existing:SF-VLA-ADAPTIVE-TEST-TIME-COMPUTE:start -->已对读当前 owner `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L10` 与相邻 handoff `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L10; books/part-04-training-system/27-data.md#L10`。Ch26 已要求高层 reasoning 与实时 controller 分层并受 latency budget 约束；当前没有把 uncertainty/critic disagreement 定义为追加推理计算的触发合同。<!-- existing:SF-VLA-ADAPTIVE-TEST-TIME-COMPUTE:end -->
<!-- delta:SF-VLA-ADAPTIVE-TEST-TIME-COMPUTE:start -->在 fast/slow VLA 路线中加入 uncertainty-triggered compute 与 relative critic，明确 trigger calibration、latency budget、critic disagreement 和 conservative fallback。<!-- delta:SF-VLA-ADAPTIVE-TEST-TIME-COMPUTE:end -->
结论：**Integrate**。
<!-- books-review:SF-VLA-ADAPTIVE-TEST-TIME-COMPUTE:end -->
<!-- books-review:SF-TAIL-SAFE-RUNTIME-MONITOR:start -->
<!-- existing:SF-TAIL-SAFE-RUNTIME-MONITOR:start -->已对读当前 owner `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L10` 与相邻 handoff `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L10; books/part-04-training-system/27-data.md#L10`。Ch26 已要求 safety envelope、human override 和 controller commit 边界，但尚未展开 actor 外独立 empirical safe-set monitor 与 bounded recovery 的控制流。<!-- existing:SF-TAIL-SAFE-RUNTIME-MONITOR:end -->
<!-- delta:SF-TAIL-SAFE-RUNTIME-MONITOR:start -->在 physical safety 段加入 actor proposal → independent empirical safe-set monitor → bounded recovery → controller commit，并保留 OOD/校准越界时停机或人工接管。<!-- delta:SF-TAIL-SAFE-RUNTIME-MONITOR:end -->
结论：**Integrate**。
<!-- books-review:SF-TAIL-SAFE-RUNTIME-MONITOR:end -->
<!-- books-review:SF-VISUOMOTOR-EXECUTION-GUARANTEE:start -->
<!-- existing:SF-VISUOMOTOR-EXECUTION-GUARANTEE:start -->已对读当前 owner `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L10` 与相邻 handoff `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L10; books/part-04-training-system/27-data.md#L10`。Ch26 已规定 safety monitor 拥有 veto、controller 拥有物理 commit；当前没有从 demonstration/perception 构造 control-invariant safeset 并以 recovery projection 保持集合不变的分支。<!-- existing:SF-VISUOMOTOR-EXECUTION-GUARANTEE:end -->
<!-- delta:SF-VISUOMOTOR-EXECUTION-GUARANTEE:start -->在 Ch26 的 safety monitor 路线加入 demonstration-derived perceptual safeset → control-invariance check → minimally projected recovery → controller commit；明确 execution guarantee 只承诺 safeset 内的 best-known task success，不等同于任意物理安全。<!-- delta:SF-VISUOMOTOR-EXECUTION-GUARANTEE:end -->
结论：**Integrate**。
<!-- books-review:SF-VISUOMOTOR-EXECUTION-GUARANTEE:end -->
<!-- books-review:SF-GRBEN-PROCESS-REWARD-EVAL:start -->
<!-- existing:SF-GRBEN-PROCESS-REWARD-EVAL:start -->已对读当前 owner `books/part-06-ai-infrastructure/66-evaluation-system.md#L10` 与相邻 handoff `books/part-06-ai-infrastructure/67-monitoring.md#L10; books/part-06-ai-infrastructure/73-production-best-practice.md#L10`。Evaluation 章节已要求 outcome、process/trajectory 与 component receipts 分层，并冻结 scorer、版本、slice 与失败归因；单一 process-reward benchmark 属于该合同的实例。<!-- existing:SF-GRBEN-PROCESS-REWARD-EVAL:end -->
<!-- delta:SF-GRBEN-PROCESS-REWARD-EVAL:start -->GRBench 证明所测任务中 process reward 的分步评价价值，但没有新增 evaluator identity、release gate 或跨 workload 的 process-state owner。<!-- delta:SF-GRBEN-PROCESS-REWARD-EVAL:end -->
结论：**No Change — Existing Coverage**。
<!-- books-review:SF-GRBEN-PROCESS-REWARD-EVAL:end -->
<!-- books-review:SF-BROWSING-AGENT-BEHAVIORAL-FINGERPRINT:start -->
<!-- existing:SF-BROWSING-AGENT-BEHAVIORAL-FINGERPRINT:start -->已对读当前 owner `books/part-06-ai-infrastructure/72-security.md#L10` 与相邻 handoff `books/part-06-ai-infrastructure/66-evaluation-system.md#L10; books/part-07-agent/78-tool-calling.md#L10`。Security 已用 MARK 建立 TLS/HTTP/browser-action 多层 web-agent fingerprint、policy-engine throttle/challenge 与漂移时行为限流 fallback；FP-Agent 的 typing/scroll/mouse features 不改变 owner。<!-- existing:SF-BROWSING-AGENT-BEHAVIORAL-FINGERPRINT:end -->
<!-- delta:SF-BROWSING-AGENT-BEHAVIORAL-FINGERPRINT:start -->typing、scroll 与 mouse behavior 强化既有 web-agent fingerprint evidence；受控 honey-site classifier 没有改变 policy-engine、identity credential 或 drift fallback 的既有边界。<!-- delta:SF-BROWSING-AGENT-BEHAVIORAL-FINGERPRINT:end -->
结论：**No Change — Existing Coverage**。
<!-- books-review:SF-BROWSING-AGENT-BEHAVIORAL-FINGERPRINT:end -->
<!-- books-review:SF-ACTIVATION-GRADIENT-COMPRESSION:start -->
<!-- existing:SF-ACTIVATION-GRADIENT-COMPRESSION:start -->已对读当前 owner `books/part-04-training-system/36-distributed-training.md#L10` 与相邻 handoff `books/part-04-training-system/35-checkpoint.md#L10; books/part-04-training-system/37-tensor-parallel.md#L10`。Distributed Training 已比较 activation sharding、checkpoint/rematerialization 和 communication trade-off，但尚未按 linear/nonlinear operator path 约束压缩是否保持无偏与可重构。<!-- existing:SF-ACTIVATION-GRADIENT-COMPRESSION:end -->
<!-- delta:SF-ACTIVATION-GRADIENT-COMPRESSION:start -->在 activation memory 路线加入 operator-aware compression：linear path 可用无偏压缩，nonlinear path 保持精确或重算；比较 low-rank factor reuse 与 checkpoint/rematerialization 的 memory、variance 和 compute。<!-- delta:SF-ACTIVATION-GRADIENT-COMPRESSION:end -->
结论：**Integrate**。
<!-- books-review:SF-ACTIVATION-GRADIENT-COMPRESSION:end -->
<!-- books-review:SF-PIXEL-LEVEL-RAG-EVIDENCE-CHAIN:start -->
<!-- existing:SF-PIXEL-LEVEL-RAG-EVIDENCE-CHAIN:start -->已对读当前 owner `books/part-07-agent/76-rag.md#L10` 与相邻 handoff `books/part-07-agent/75-context.md#L10; books/part-07-agent/77-memory.md#L10`。RAG 已要求 claim-level provenance、source dereference、sufficiency 与 entailment，也保留 modality-native operator；当前尚未把 visual document 的 page/region/bounding-box identity 与多跳依赖写成 evidence contract。<!-- existing:SF-PIXEL-LEVEL-RAG-EVIDENCE-CHAIN:end -->
<!-- delta:SF-PIXEL-LEVEL-RAG-EVIDENCE-CHAIN:start -->在 Ch76 的 claim-evidence lifecycle 中加入 visual document branch：source/page revision → screenshot/region identity → bounding-box evidence hop → claim mapping；region locator 只负责可定位性，仍需 source authority、entailment、sufficiency 与独立 verifier。<!-- delta:SF-PIXEL-LEVEL-RAG-EVIDENCE-CHAIN:end -->
结论：**Integrate**。
<!-- books-review:SF-PIXEL-LEVEL-RAG-EVIDENCE-CHAIN:end -->
<!-- books-review:SF-LOGIC-GROUNDED-SKILL-INDUCTION:start -->
<!-- existing:SF-LOGIC-GROUNDED-SKILL-INDUCTION:start -->已对读当前 owner `books/part-07-agent/81-workflow.md#L10` 与相邻 handoff `books/part-07-agent/80-reflection.md#L10; books/part-07-agent/82-multi-agent.md#L10`。Agent Platform 已把 trajectory→typed/versioned Skill 定义为受治理 compilation，并要求 source provenance、held-out evaluation、admission/supersede/rollback；Workflow 拥有 durable control-flow state。<!-- existing:SF-LOGIC-GROUNDED-SKILL-INDUCTION:end -->
<!-- delta:SF-LOGIC-GROUNDED-SKILL-INDUCTION:start -->显式 control flow、node invention 与 dynamic variable binding 为 trajectory compilation 提供实现证据；当前 Books 已要求 typed Skill、durable workflow、held-out admission 与 rollback，不重复追加。<!-- delta:SF-LOGIC-GROUNDED-SKILL-INDUCTION:end -->
结论：**No Change — Existing Coverage**。
<!-- books-review:SF-LOGIC-GROUNDED-SKILL-INDUCTION:end -->
<!-- books-review:SF-COUNTERFACTUAL-RISK-RAG:start -->
<!-- existing:SF-COUNTERFACTUAL-RISK-RAG:start -->已对读当前 owner `books/part-07-agent/76-rag.md#L10` 与相邻 handoff `books/part-07-agent/75-context.md#L10; books/part-07-agent/77-memory.md#L10`。RAG 已把 relevance 降为候选信号，并要求 sufficiency、independent verification、abstain/escalate 和生产漂移监控；counterfactual critic 没有改变这些 owner。<!-- existing:SF-COUNTERFACTUAL-RISK-RAG:end -->
<!-- delta:SF-COUNTERFACTUAL-RISK-RAG:start -->counterfactual perturbation、Evidence Critic 与 risk threshold 具体化了既有 verify/abstain 分支；跨领域校准和 production drift 未证明，因此不重复写入。<!-- delta:SF-COUNTERFACTUAL-RISK-RAG:end -->
结论：**No Change — Existing Coverage**。
<!-- books-review:SF-COUNTERFACTUAL-RISK-RAG:end -->
<!-- books-review:SF-CONFOUNDED-LOG-EVALUATION:start -->
<!-- existing:SF-CONFOUNDED-LOG-EVALUATION:start -->已对读当前 owner `books/part-06-ai-infrastructure/66-evaluation-system.md#L10` 与相邻 handoff `books/part-06-ai-infrastructure/67-monitoring.md#L10; books/part-06-ai-infrastructure/73-production-best-practice.md#L10`。Evaluation 已区分 offline、shadow、canary 与 online evidence，却没有在观察日志进入估计前强制声明 OBS/EXP/SIM 身份、可识别性假设与 mediator state。<!-- existing:SF-CONFOUNDED-LOG-EVALUATION:end -->
<!-- delta:SF-CONFOUNDED-LOG-EVALUATION:start -->在 offline/online evaluation 之间新增 causal identification gate：先声明 OBS/EXP/SIM 的角色和假设，再允许日志进入估计；多轮 Agent 必须重建 mediator/state contract。<!-- delta:SF-CONFOUNDED-LOG-EVALUATION:end -->
结论：**Integrate**。
<!-- books-review:SF-CONFOUNDED-LOG-EVALUATION:end -->
<!-- books-review:SF-ACCESS-AWARE-VECTOR-INDEX:start -->
<!-- existing:SF-ACCESS-AWARE-VECTOR-INDEX:start -->已对读当前 owner `books/part-07-agent/76-rag.md#L10` 与相邻 handoff `books/part-07-agent/75-context.md#L10; books/part-07-agent/77-memory.md#L10`。RAG 已要求授权先于 ranking，并讨论 role graph、index partition 与 broad-query crossover；Veda/EffVeda 是这一现有 security-aware retrieval contract 的受限实现证据。<!-- existing:SF-ACCESS-AWARE-VECTOR-INDEX:end -->
<!-- delta:SF-ACCESS-AWARE-VECTOR-INDEX:start -->Veda/EffVeda 的 lattice 与 coordinated search 为授权先于检索提供性能案例；现有章节已明确相同安全边界和 broad-query trade-off。<!-- delta:SF-ACCESS-AWARE-VECTOR-INDEX:end -->
结论：**No Change — Existing Coverage**。
<!-- books-review:SF-ACCESS-AWARE-VECTOR-INDEX:end -->
<!-- books-review:SF-VUDA-CUDA-VULKAN-SHARING:start -->
<!-- existing:SF-VUDA-CUDA-VULKAN-SHARING:start -->已对读当前 owner `books/part-06-ai-infrastructure/63-gpu-scheduler.md#L10` 与相邻 handoff `books/part-06-ai-infrastructure/62-gateway.md#L10; books/part-06-ai-infrastructure/64-volcano.md#L10`。GPU Scheduler 已覆盖 time-slicing、MPS、MIG、隔离与 fallback，但资源 owner 仍默认单一 CUDA scheduling/address-space domain。<!-- existing:SF-VUDA-CUDA-VULKAN-SHARING:end -->
<!-- delta:SF-VUDA-CUDA-VULKAN-SHARING:start -->在 GPU scheduler 的 time-slicing/MPS/MIG 后加入 cross-API spatial sharing 分支，说明 scheduling-domain 与 address-space owner、同步安全和 driver fallback。<!-- delta:SF-VUDA-CUDA-VULKAN-SHARING:end -->
结论：**Integrate**。
<!-- books-review:SF-VUDA-CUDA-VULKAN-SHARING:end -->
<!-- books-review:SF-LONG-FORM-LENGTH-VOLATILITY:start -->
<!-- existing:SF-LONG-FORM-LENGTH-VOLATILITY:start -->已对读当前 owner `books/part-05-inference-system/44-decode.md#L10` 与相邻 handoff `books/part-05-inference-system/43-prefill.md#L10; books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L10`。Decode 已以 TTFT/TPOT、tail latency、token budget 和 stop condition 管理 SLO，但未把 output-length distribution/variance 当成独立于平均质量的发布变量。<!-- existing:SF-LONG-FORM-LENGTH-VOLATILITY:end -->
<!-- delta:SF-LONG-FORM-LENGTH-VOLATILITY:start -->在 decode SLO 中把 output-length distribution/variance 与 mean quality 分开，说明 logits mitigation、hard budget、stop contract 和 fallback。<!-- delta:SF-LONG-FORM-LENGTH-VOLATILITY:end -->
结论：**Integrate**。
<!-- books-review:SF-LONG-FORM-LENGTH-VOLATILITY:end -->
<!-- books-review:SF-PROVENANCE-GRAPH-MEMORY:start -->
<!-- existing:SF-PROVENANCE-GRAPH-MEMORY:start -->已对读当前 owner `books/part-07-agent/77-memory.md#L10` 与相邻 handoff `books/part-07-agent/76-rag.md#L10; books/part-07-agent/78-tool-calling.md#L10`。Memory 已把长期读取写成 authorized anchor recall → bounded graph expansion → provenance merge，并要求 edge 不成为事实 owner；MemORAI 的 graph schema 与 PageRank 落在该主线内。<!-- existing:SF-PROVENANCE-GRAPH-MEMORY:end -->
<!-- delta:SF-PROVENANCE-GRAPH-MEMORY:start -->selective compression、turn-level provenance graph 与 query-adaptive expansion 强化既有 bounded evidence-set retrieval；static entity linking、ACL、并发和 deletion propagation 未闭合。<!-- delta:SF-PROVENANCE-GRAPH-MEMORY:end -->
结论：**No Change — Existing Coverage**。
<!-- books-review:SF-PROVENANCE-GRAPH-MEMORY:end -->
<!-- books-review:SF-LIVEFMBENCH-SPECIFICATION-EVAL:start -->
<!-- existing:SF-LIVEFMBENCH-SPECIFICATION-EVAL:start -->已对读当前 owner `books/part-06-ai-infrastructure/66-evaluation-system.md#L10` 与相邻 handoff `books/part-06-ai-infrastructure/67-monitoring.md#L10; books/part-06-ai-infrastructure/73-production-best-practice.md#L10`。Evaluation 已要求 benchmark/version/scorer identity、contamination 检查、per-example slice 与 failure analysis；formal-spec benchmark 只为既有 contract 增加一个 workload。<!-- existing:SF-LIVEFMBENCH-SPECIFICATION-EVAL:end -->
<!-- delta:SF-LIVEFMBENCH-SPECIFICATION-EVAL:start -->污染控制、faithful filtering 与 formal-spec failure analysis 强化现有 benchmark contract，但没有形成新的通用 evaluator 或发布判断。<!-- delta:SF-LIVEFMBENCH-SPECIFICATION-EVAL:end -->
结论：**No Change — Existing Coverage**。
<!-- books-review:SF-LIVEFMBENCH-SPECIFICATION-EVAL:end -->
<!-- books-review:SF-AUTOREGRESSIVE-CREDIT-ATTRIBUTION-BARRIER:start -->
<!-- existing:SF-AUTOREGRESSIVE-CREDIT-ATTRIBUTION-BARRIER:start -->已对读当前 owner `books/part-07-agent/76-rag.md#L10` 与相邻 handoff `books/part-07-agent/75-context.md#L10; books/part-07-agent/77-memory.md#L10`。RAG 已要求 claim-evidence provenance 与 generation 同步携带，但尚未解释为何生成后再做 token-level attribution 不能保证组合性，且可能具有不可承受的搜索复杂度。<!-- existing:SF-AUTOREGRESSIVE-CREDIT-ATTRIBUTION-BARRIER:end -->
<!-- delta:SF-AUTOREGRESSIVE-CREDIT-ATTRIBUTION-BARRIER:start -->在 RAG attribution 路线补入 negative result：token-level credit 不自动组合，black-box post-hoc retrofitting 可能指数昂贵；因此 provenance 必须伴随 evidence admission 与 generation。<!-- delta:SF-AUTOREGRESSIVE-CREDIT-ATTRIBUTION-BARRIER:end -->
结论：**Integrate**。
<!-- books-review:SF-AUTOREGRESSIVE-CREDIT-ATTRIBUTION-BARRIER:end -->
<!-- books-review:SF-LORA-COMPOSITION-RELIABILITY:start -->
<!-- existing:SF-LORA-COMPOSITION-RELIABILITY:start -->独立 reviewer 重读 `books/part-04-training-system/30-lora.md#L260` 及相邻 handoff：当前正文已把 base/adapter identity、composition/merge/routing compatibility、组合后重新 Evaluation 与 promotion/rollback 串成同一生命周期；数学可相加不等于行为兼容已经是 canonical proposition。<!-- existing:SF-LORA-COMPOSITION-RELIABILITY:end -->
<!-- delta:SF-LORA-COMPOSITION-RELIABILITY:start -->exact-v1 的 sparse residual composition 与 multi-view disagreement 只是在限定 FLAN-T5/BBH/adapter 集合中的 evaluator 实现，且 reliability proxy 未校准；它不改变现有 owner、commit 或回退合同。<!-- delta:SF-LORA-COMPOSITION-RELIABILITY:end -->
结论：**No Change — Existing Coverage**。
<!-- books-review:SF-LORA-COMPOSITION-RELIABILITY:end -->
<!-- books-review:SF-AUTONOMOUS-TEST-REPAIR-VALIDATION-BOUNDARY:start -->
<!-- existing:SF-AUTONOMOUS-TEST-REPAIR-VALIDATION-BOUNDARY:start -->独立 reviewer 重读 `books/part-06-ai-infrastructure/66-evaluation-system.md#L2584` 及相邻 handoff：当前正文已明确 Agent-authored tests 不能以“创建 test 文件”代理 verifier strength，必须检查 assertion/oracle signal、执行路径和 failure discriminativeness，并把 release authority 保留给独立 gate。<!-- existing:SF-AUTONOMOUS-TEST-REPAIR-VALIDATION-BOUNDARY:end -->
<!-- delta:SF-AUTONOMOUS-TEST-REPAIR-VALIDATION-BOUNDARY:start -->exact-v1 的 assertion weakening、test deletion 与 bounded retry 是上述 proposition 的受限 case；不再形成新的 state/control owner 或 release contract。<!-- delta:SF-AUTONOMOUS-TEST-REPAIR-VALIDATION-BOUNDARY:end -->
结论：**No Change — Existing Coverage**。
<!-- books-review:SF-AUTONOMOUS-TEST-REPAIR-VALIDATION-BOUNDARY:end -->
<!-- books-review:SF-ACTION-AGENT-VIDEO-CONTROL:start -->
<!-- existing:SF-ACTION-AGENT-VIDEO-CONTROL:start -->已对读当前 owner `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L10` 与相邻 handoff `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L10; books/part-04-training-system/27-data.md#L10`。Ch25–26 已把 video/latent imagination 与 controllable world state 分开，并形成 action proposal → controller → environment feedback 的闭环；该 family 没有改变 owner。<!-- existing:SF-ACTION-AGENT-VIDEO-CONTROL:end -->
<!-- delta:SF-ACTION-AGENT-VIDEO-CONTROL:start -->video rehearsal 与 FlowDiT action denoising 支持现有 imagination-to-control 分层；短视频、少量 open-loop 实机试验没有证明新的 closed-loop safety contract。<!-- delta:SF-ACTION-AGENT-VIDEO-CONTROL:end -->
结论：**No Change — Existing Coverage**。
<!-- books-review:SF-ACTION-AGENT-VIDEO-CONTROL:end -->
<!-- books-review:SF-NOTEBOOK-REPRODUCIBILITY-STATE-GATE:start -->
<!-- existing:SF-NOTEBOOK-REPRODUCIBILITY-STATE-GATE:start -->已对读当前 owner `books/part-07-agent/81-workflow.md#L10` 与相邻 handoff `books/part-07-agent/80-reflection.md#L10; books/part-07-agent/82-multi-agent.md#L10`。Workflow 已把 notebook 写成 versioned procedure 与 gate-conditioned fallback，却只解决 environment portability；当前没有 clean top-to-bottom equivalence、read/write receipt 与 stale-cell gate。<!-- existing:SF-NOTEBOOK-REPRODUCIBILITY-STATE-GATE:end -->
<!-- delta:SF-NOTEBOOK-REPRODUCIBILITY-STATE-GATE:start -->在 Ch81 的 Versioned Notebook 路线加入 clean-state reproducibility contract：empty-store top-to-bottom result 是 reference，cell read/write receipts 决定 stale state 与可提交操作；未建模外部 side effect、随机性或并发时回退 clean rerun/containerized execution。<!-- delta:SF-NOTEBOOK-REPRODUCIBILITY-STATE-GATE:end -->
结论：**Integrate**。
<!-- books-review:SF-NOTEBOOK-REPRODUCIBILITY-STATE-GATE:end -->
<!-- books-review:SF-MULTIAGENT-PARETO-COMPUTE-ALLOCATION:start -->
<!-- existing:SF-MULTIAGENT-PARETO-COMPUTE-ALLOCATION:start -->已对读当前 owner `books/part-07-agent/82-multi-agent.md#L10` 与相邻 handoff `books/part-07-agent/81-workflow.md#L10; books/part-07-agent/83-mcp.md#L10`。Multi-Agent 已解释 coordination tax、topology、correlated error 与 verifier，但尚未要求在相同 compute budget 下把 self-consistency/refinement/debate/MoA 放入同一 quality-cost Pareto contract。<!-- existing:SF-MULTIAGENT-PARETO-COMPUTE-ALLOCATION:end -->
<!-- delta:SF-MULTIAGENT-PARETO-COMPUTE-ALLOCATION:start -->在 Ch82 的 coordination-tax 路线加入 equal-budget Pareto admission：同一 task slice 下比较 CoT/self-consistency/refinement/debate/MoA 的 quality–token/latency/cost frontier；先记录 single-agent baseline，相关错误或通信/尾延迟未计入时不得自动推广 topology。<!-- delta:SF-MULTIAGENT-PARETO-COMPUTE-ALLOCATION:end -->
结论：**Integrate**。
<!-- books-review:SF-MULTIAGENT-PARETO-COMPUTE-ALLOCATION:end -->
<!-- books-review:SF-DEVELOPER-MEMORY-OPE-GATE:start -->
<!-- existing:SF-DEVELOPER-MEMORY-OPE-GATE:start -->已对读当前 owner `books/part-07-agent/77-memory.md#L10` 与相邻 handoff `books/part-07-agent/76-rag.md#L10; books/part-07-agent/78-tool-calling.md#L10`。Memory 已要求 provenance、writer/reader authority、feedback verifier、shadow/canary、abstain 与 rollback；带 propensity 的 retrieval event 和 OPE 是该发布纪律的实现案例。<!-- existing:SF-DEVELOPER-MEMORY-OPE-GATE:end -->
<!-- delta:SF-DEVELOPER-MEMORY-OPE-GATE:start -->decision event、bounded reward、shadow residual policy 与 OPE gate 是现有 Memory provenance/verification/canary/rollback 路线的实现证据，且论文未证明 accuracy gain。<!-- delta:SF-DEVELOPER-MEMORY-OPE-GATE:end -->
结论：**No Change — Existing Coverage**。
<!-- books-review:SF-DEVELOPER-MEMORY-OPE-GATE:end -->
<!-- books-review:SF-PRODUCTION-AGENT-EVALUATION:start -->
<!-- existing:SF-PRODUCTION-AGENT-EVALUATION:start -->已对读当前 owner `books/part-06-ai-infrastructure/66-evaluation-system.md#L10` 与相邻 handoff `books/part-06-ai-infrastructure/67-monitoring.md#L10; books/part-06-ai-infrastructure/73-production-best-practice.md#L10`。Evaluation 已拥有 trajectory/component receipts、drift、offline→shadow→canary→online、per-example slice 与 scorer identity；PAEF 的维度不新增 release owner。<!-- existing:SF-PRODUCTION-AGENT-EVALUATION:end -->
<!-- delta:SF-PRODUCTION-AGENT-EVALUATION:start -->cascade/tool/distribution/explanation 指标映射到现有 trajectory、drift 与 release receipts；论文没有 production data 且 threshold 未校准。<!-- delta:SF-PRODUCTION-AGENT-EVALUATION:end -->
结论：**No Change — Existing Coverage**。
<!-- books-review:SF-PRODUCTION-AGENT-EVALUATION:end -->
<!-- books-review:SF-DATA-CONSTRAINED-SCALING-LAW:start -->
<!-- existing:SF-DATA-CONSTRAINED-SCALING-LAW:start -->独立 reviewer 重读 `books/part-04-training-system/28-pretraining.md#L732` 与 `#L905` 及相邻章节：当前正文已把 unique-token volume、repetition、effective parameters、regularization 与 data-saturation boundary 联合写入 compute allocation，并明确 empirical scale 不能外推 frontier。<!-- existing:SF-DATA-CONSTRAINED-SCALING-LAW:end -->
<!-- delta:SF-DATA-CONSTRAINED-SCALING-LAW:start -->exact-v1 的 additive repetition penalty 和 weight-decay case 为相同条件化结论提供额外实验，但不改变 Books 已有 design decision。<!-- delta:SF-DATA-CONSTRAINED-SCALING-LAW:end -->
结论：**No Change — Existing Coverage**。
<!-- books-review:SF-DATA-CONSTRAINED-SCALING-LAW:end -->
<!-- books-review:SF-AGENT-SAFETY-SEARCH-MEASUREMENT:start -->
<!-- existing:SF-AGENT-SAFETY-SEARCH-MEASUREMENT:start -->已对读当前 owner `books/part-06-ai-infrastructure/66-evaluation-system.md#L10` 与相邻 handoff `books/part-06-ai-infrastructure/67-monitoring.md#L10; books/part-06-ai-infrastructure/73-production-best-practice.md#L10`。Evaluation 已要求 deployment configuration、sampling budget 与 residual uncertainty 可追溯，但尚未把 prefix-cache/chunk search 作为与 sampling 并列的安全覆盖路线。<!-- existing:SF-AGENT-SAFETY-SEARCH-MEASUREMENT:end -->
<!-- delta:SF-AGENT-SAFETY-SEARCH-MEASUREMENT:start -->在 agent evaluation 中加入 search-based safety route：deployment config 冻结、likelihood budget、prefix-cache/chunk search 与 residual uncovered mass；与 sampling 并列而非替代。<!-- delta:SF-AGENT-SAFETY-SEARCH-MEASUREMENT:end -->
结论：**Integrate**。
<!-- books-review:SF-AGENT-SAFETY-SEARCH-MEASUREMENT:end -->
<!-- books-review:SF-AGENT-GENERATED-VERIFIED-COMPILER:start -->
<!-- existing:SF-AGENT-GENERATED-VERIFIED-COMPILER:start -->已对读当前 owner `books/part-06-ai-infrastructure/66-evaluation-system.md#L10` 与相邻 handoff `books/part-06-ai-infrastructure/67-monitoring.md#L10; books/part-06-ai-infrastructure/73-production-best-practice.md#L10`。Evaluation 已拥有 executable verifier、artifact lineage 与 coding-agent release gate；当前没有明确区分 testing、translation certificate、machine proof 与 audit 各自覆盖的 trust boundary。<!-- existing:SF-AGENT-GENERATED-VERIFIED-COMPILER:end -->
<!-- delta:SF-AGENT-GENERATED-VERIFIED-COMPILER:start -->在 Ch66 的 coding-agent artifact gate 中加入分层 trust path：tests 探测环境/implementation mismatch，translation certificate 由独立 checker 验证，machine proof 只承诺形式化 theorem，audit 聚焦 parser/spec/toolchain 等未验证边界；任何层失败回退不发布。<!-- delta:SF-AGENT-GENERATED-VERIFIED-COMPILER:end -->
结论：**Integrate**。
<!-- books-review:SF-AGENT-GENERATED-VERIFIED-COMPILER:end -->
<!-- books-review:SF-DITRON-DISTRIBUTED-TILING:start -->
<!-- existing:SF-DITRON-DISTRIBUTED-TILING:start -->已对读当前 owner `books/part-05-inference-system/49-tensorrt-llm.md#L10` 与相邻 handoff `books/part-05-inference-system/48-speculative-decoding.md#L10; books/part-05-inference-system/50-vllm.md#L10`。Execution Engine 已区分 compiler plan 与 runtime/kernel execution，也保留库路径 fallback；现有主线仍以单设备 tiling 为主，没有 topology/health 驱动的分布式层级。<!-- existing:SF-DITRON-DISTRIBUTED-TILING:end -->
<!-- delta:SF-DITRON-DISTRIBUTED-TILING:start -->把执行引擎章节从单设备 kernel 扩展到 hierarchical distributed tiling，明确 compiler owns plan、runtime owns topology/health、库路径作为稳定 fallback。<!-- delta:SF-DITRON-DISTRIBUTED-TILING:end -->
结论：**Integrate**。
<!-- books-review:SF-DITRON-DISTRIBUTED-TILING:end -->
<!-- books-review:SF-REFUSAL-TRAJECTORY-MONITOR:start -->
<!-- existing:SF-REFUSAL-TRAJECTORY-MONITOR:start -->已对读当前 owner `books/part-06-ai-infrastructure/72-security.md#L10` 与相邻 handoff `books/part-06-ai-infrastructure/66-evaluation-system.md#L10; books/part-07-agent/78-tool-calling.md#L10`。Security 与 Evaluation 已要求沿 trajectory 观察 policy/refusal 状态、区分 refusal 与安全性，并以 action boundary 执行 gate；新监测器未改变 enforcement owner。<!-- existing:SF-REFUSAL-TRAJECTORY-MONITOR:end -->
<!-- delta:SF-REFUSAL-TRAJECTORY-MONITOR:start -->trajectory monitor 提供局部检测案例，但未改变 refusal 不是 safety proof、最终 enforcement 位于 action boundary 的既有结论。<!-- delta:SF-REFUSAL-TRAJECTORY-MONITOR:end -->
结论：**No Change — Existing Coverage**。
<!-- books-review:SF-REFUSAL-TRAJECTORY-MONITOR:end -->
<!-- books-review:SF-RECURSIVE-STATE-TERMINATION:start -->
<!-- existing:SF-RECURSIVE-STATE-TERMINATION:start -->已对读当前 owner `books/part-07-agent/80-reflection.md#L10` 与相邻 handoff `books/part-07-agent/79-planning.md#L10; books/part-07-agent/81-workflow.md#L10`。Reflection 已要求 budget、maximum iterations、evidence check 与停止条件，但尚未把 epistemic state 类型和 order-gap 作为局部 stop sensor。<!-- existing:SF-RECURSIVE-STATE-TERMINATION:end -->
<!-- delta:SF-RECURSIVE-STATE-TERMINATION:start -->在 Reflection loop 中加入 typed epistemic state 与 order-gap stop sensor，明确 local diagnostic、truth/evidence gate、budget limit 和 maximum-iteration fallback。<!-- delta:SF-RECURSIVE-STATE-TERMINATION:end -->
结论：**Integrate**。
<!-- books-review:SF-RECURSIVE-STATE-TERMINATION:end -->
<!-- books-review:SF-PRUNING-BEHAVIORAL-REGRESSION:start -->
<!-- existing:SF-PRUNING-BEHAVIORAL-REGRESSION:start -->已对读当前 owner `books/part-06-ai-infrastructure/66-evaluation-system.md#L10` 与相邻 handoff `books/part-06-ai-infrastructure/67-monitoring.md#L10; books/part-06-ai-infrastructure/73-production-best-practice.md#L10`。Evaluation 已反对只看 aggregate/perplexity，并要求 item-level transition、slice、calibration 与真实运行时验证；pruning 的 sparse-kernel/storage 联动尚未显式进入压缩 release gate。<!-- existing:SF-PRUNING-BEHAVIORAL-REGRESSION:end -->
<!-- delta:SF-PRUNING-BEHAVIORAL-REGRESSION:start -->在压缩 release gate 中加入 dense-vs-pruned item-level transition、fairness/calibration slice 和真实 sparse-kernel/storage 验证；perplexity 只能是一个 guardrail。<!-- delta:SF-PRUNING-BEHAVIORAL-REGRESSION:end -->
结论：**Integrate**。
<!-- books-review:SF-PRUNING-BEHAVIORAL-REGRESSION:end -->
<!-- books-review:SF-SEQUENTIAL-MODEL-EDIT-SIDECAR:start -->
<!-- existing:SF-SEQUENTIAL-MODEL-EDIT-SIDECAR:start -->已对读当前 owner `books/part-06-ai-infrastructure/59-model-registry.md#L10` 与相邻 handoff `books/part-04-training-system/30-lora.md#L10; books/part-06-ai-infrastructure/61-kserve.md#L10`。Registry 拥有 immutable model/artifact lineage，LoRA 拥有低秩增量与 rollback，Serving 拥有 runtime route；三者都没有完整拥有持续 model edit 的 key/value identity、precedence、conflict、locality 与撤销语义。<!-- existing:SF-SEQUENTIAL-MODEL-EDIT-SIDECAR:end -->
<!-- delta:SF-SEQUENTIAL-MODEL-EDIT-SIDECAR:start -->HoReN 暴露 parameter-preserving model edit 作为独立长期知识链：base weights 保持只读，edit codebook 拥有派生事实，runtime router 决定 override，Registry 需治理 edit order/conflict/rollback。现有节点只能分段承载，交由结构复核决定 canonical owner。<!-- delta:SF-SEQUENTIAL-MODEL-EDIT-SIDECAR:end -->
结论：**Structural Candidate**。
<!-- books-review:SF-SEQUENTIAL-MODEL-EDIT-SIDECAR:end -->
<!-- books-review:SF-POLICY-CARRIAGE-INTEGRITY:start -->
<!-- existing:SF-POLICY-CARRIAGE-INTEGRITY:start -->已对读当前 owner `books/part-07-agent/75-context.md#L10` 与相邻 handoff `books/part-07-agent/74-prompt.md#L10; books/part-07-agent/76-rag.md#L10`。Context 已定义 trust ordering、provenance 与预算约束，Tool boundary 负责动作授权；尚未把 active policy set/version 作为跨 assembly 与 action 的不可丢失 invariant。<!-- existing:SF-POLICY-CARRIAGE-INTEGRITY:end -->
<!-- delta:SF-POLICY-CARRIAGE-INTEGRITY:start -->在 Context trust ordering 后新增 policy-carriage invariant：active policy set/version/provenance 必须在 assembly 前可验证、预算不足 fail closed，并由 tool/action boundary再次强制。<!-- delta:SF-POLICY-CARRIAGE-INTEGRITY:end -->
结论：**Integrate**。
<!-- books-review:SF-POLICY-CARRIAGE-INTEGRITY:end -->
<!-- books-review:SF-QUANTIZATION-BEHAVIORAL-REGRESSION:start -->
<!-- existing:SF-QUANTIZATION-BEHAVIORAL-REGRESSION:start -->已对读当前 owner `books/part-06-ai-infrastructure/66-evaluation-system.md#L10` 与相邻 handoff `books/part-06-ai-infrastructure/67-monitoring.md#L10; books/part-06-ai-infrastructure/73-production-best-practice.md#L10`。Execution/Evaluation 已将 quantization 视为行为变换，要求 dense-vs-quantized per-example correctness、slice、校准及真实硬件验证；该 family 直接落在现有 contract 内。<!-- existing:SF-QUANTIZATION-BEHAVIORAL-REGRESSION:end -->
<!-- delta:SF-QUANTIZATION-BEHAVIORAL-REGRESSION:start -->dense-vs-quantized 的 item-level divergence 强化既有行为回归 gate；相同命题已完整存在，新增论文名称不会改善论证。<!-- delta:SF-QUANTIZATION-BEHAVIORAL-REGRESSION:end -->
结论：**No Change — Existing Coverage**。
<!-- books-review:SF-QUANTIZATION-BEHAVIORAL-REGRESSION:end -->
<!-- audit-target:books:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260503-COVERAGE | fresh-context:may2026-day01 | coverage | audit-target:coverage | — | 274/274 title+abstract replay；36 retained / 238 family-specific closures 均维持，false negative=0、false positive=0 | passed |
| SA-20260503-EVIDENCE | fresh-context:may2026-day01 | evidence | audit-target:evidence | — | 36/36 exact-v1 receipt、Method/evaluation/non-proof locator 与 claim boundary 对读；blocked=0、pending=0 | passed |
| SA-20260503-SELECTION | fresh-context:may2026-day01 | deep_analysis_selection | audit-target:deep_analysis_selection | — | 36 项 eligibility 重放；三个 narrative unit 仍覆盖本日最强跨层 delta，未选项仍有完整 Review | passed |
| SA-20260503-BOOKS | fresh-context:may2026-day01 | books | audit-target:books | — | `POST_WRITE_BOOKS_AUDIT.md`：19/19 写回存在且位于真实 Review notes 前；19/19 演进/owner/trade-off/failure/fallback/coexistence 完整；相邻 owner 冲突=0；3 个 No Change 与 1 个 Structural Candidate 维持 | passed |

## 8. Ignored Noise

238 项未入池 identity 全部保存在 screening ledger；每项保留 exact identity、v1 timestamp、title、abstract、category、具体 closure 与重开条件，不计 Score V2。

## 9. Recommended Action

本日无需继续写回。后续只在出现新的 exact-version、owner-date 冲突，或 `SF-SEQUENTIAL-MODEL-EDIT-SIDECAR` 与更多 family 形成独立长期知识链时重开对应 Gate。

## 10. Repository Changes

- 新建本 Daily README。
- 保存 274 项 screening ledger、identity/date provenance、36 项 exact-v1 Review、独立审计收据与最终 Books queue。
- root 已将 19 项按 canonical owner 串行写入共享 Books；本次独立审计未修改 Books、ROADMAP、Learning State、Weekly 或其他日期。
- 新增 `POST_WRITE_BOOKS_AUDIT.md`，逐项记录正文位置、语义链、相邻 owner、No Change 与 Structural Candidate 复核结果。

## 11. Open Questions

- VLA uncertainty/critic 与 safety monitor 在真实 closed-loop、OOD 和硬 deadline 下如何联合校准？
- confounded log evaluation 在多轮 Agent mediator 随 action 改变时需要怎样的 sequential identification？
- policy carriage 与 action-boundary enforcement 如何共享 policy version 而不形成 stale control state？

## 12. Sources

访问时间：2026-08-31T20:55:00+08:00。

- [Trace](https://arxiv.org/html/2605.01186v1) — exact arXiv v1
- [Compute Optimal Tokenization](https://arxiv.org/html/2605.01188v1) — exact arXiv v1
- [Sentinel-VLA](https://arxiv.org/html/2605.01191v1) — exact arXiv v1
- [VLA-ATTC](https://arxiv.org/html/2605.01194v1) — exact arXiv v1
- [TAIL-Safe](https://arxiv.org/html/2605.01195v1) — exact arXiv v1
- [Visuomotor Execution Guarantee](https://arxiv.org/html/2605.01201v1) — exact arXiv v1
- [GR-Ben](https://arxiv.org/html/2605.01203v1) — exact arXiv v1
- [FP-Agent](https://arxiv.org/html/2605.01247v1) — exact arXiv v1
- [Activation Compression in LLMs](https://arxiv.org/html/2605.01255v1) — exact arXiv v1
- [Chain of Evidence](https://arxiv.org/html/2605.01284v1) — exact arXiv v1
- [Neuro-Symbolic Skill Induction](https://arxiv.org/html/2605.01293v1) — exact arXiv v1
- [CoRM-RAG](https://arxiv.org/html/2605.01302v1) — exact arXiv v1
- [The Partial Testimony of Logs](https://arxiv.org/html/2605.01311v1) — exact arXiv v1
- [Authorized Vector Retrieval via Access-Aware Indexing](https://arxiv.org/pdf/2605.01342v1) — exact arXiv v1
- [VUDA](https://arxiv.org/html/2605.01352v1) — exact arXiv v1
- [Long-Form Length Volatility](https://arxiv.org/html/2605.01357v1) — exact arXiv v1
- [MemORAI](https://arxiv.org/html/2605.01386v1) — exact arXiv v1
- [LiveFMBench](https://arxiv.org/html/2605.01394v1) — exact arXiv v1
- [Counterfactual Credit Attribution Barriers](https://arxiv.org/html/2605.01425v1) — exact arXiv v1
- [SCALE-LoRA](https://arxiv.org/html/2605.01429v1) — exact arXiv v1
- [Practical Limits of Autonomous Test Repair](https://arxiv.org/html/2605.01471v1) — exact arXiv v1
- [Action Agent](https://arxiv.org/html/2605.01477v1) — exact arXiv v1
- [FlowBook](https://arxiv.org/html/2605.01560v1) — exact arXiv v1
- [Pareto-Optimal Test-Time Scaling](https://arxiv.org/html/2605.01566v1) — exact arXiv v1
- [RL Developer Memory](https://arxiv.org/html/2605.01567v1) — exact arXiv v1
- [PAEF](https://arxiv.org/html/2605.01604v1) — exact arXiv v1
- [Data-Constrained Scaling Laws](https://arxiv.org/html/2605.01640v1) — exact arXiv v1
- [Agent Safety Measurement by Search](https://arxiv.org/html/2605.01644v1) — exact arXiv v1
- [Axon Verified Compiler](https://arxiv.org/html/2605.01660v1) — exact arXiv v1
- [DITRON](https://arxiv.org/html/2605.02953v1) — exact arXiv v1
- [Refusal Trajectory Monitoring](https://arxiv.org/html/2605.02958v1) — exact arXiv v1
- [Recursive State and Termination](https://arxiv.org/html/2605.06690v1) — exact arXiv v1
- [Pruning Behavioral Regression](https://arxiv.org/html/2605.08137v1) — exact arXiv v1
- [HoReN](https://arxiv.org/html/2605.08143v1) — exact arXiv v1
- [Policy-Carriage Integrity](https://arxiv.org/html/2605.12535v1) — exact arXiv v1
- [Quantization Behavioral Regression](https://arxiv.org/html/2605.15208v1) — exact arXiv v1
- DataCite arXiv DOI 月度快照：`papers/2026/05/_sources/datacite-arxiv-202605-v2/`（只作 metadata/discovery）

## 13. Final Status

- Raw identities = 512
- Registered identities = 274
- Core Daily semantic screened = 180
- Keyword-category screened = 94
- Candidate Denominator = 36
- Pre-denominator closures = 238
- exact-v1 Full Source Review = 36/36 author-complete
- Deep Analysis narrative = 3/3
- Books Comparison = 36/36
- Books writeback = 19/19 materialized and post-write verified
- Structural Candidate = 1 disposition upheld；进入后续结构复核，不阻塞本日 Books Gate
- Ordinary pending = 0；blocked = 0
- Coverage = Closed
- Evidence = Passed
- Books = Passed
- Unresolved findings = 0
- Completion Status = Complete

<!-- audit-target:evidence:end -->
