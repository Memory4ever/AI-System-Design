# Daily Research — 2026-04-26

**Research Date:** 2026-04-26

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-04-25 09:00:00 ～ 2026-04-26 09:00:00（Asia/Shanghai，北京时间，左闭右开）

**Contract:** V2.1 historical Daily independent replay；技术结论只绑定 official exact-v1 与 current Books。

**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed；2/2 Integrate 已写回并通过独立 post-write Semantic Audit。

## Executive Summary

严格窗口注册并逐项 title+abstract 语义筛选 419/419 identity；author denominator=21，fresh-context final denominator=27，closures=392。独立审计重开 FN=6、移除 FP=0，withdrawn=0；27/27 exact-v1 Source Review complete，pending=0、blocked=0。current owner+adjacent comparison 后 2/2 Integrate 已写入 canonical Books；非写作者 post-write 首轮发现 1 项 trust-boundary 表述问题，修正并复验通过。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-04-26 |
| Window End | 2026-04-26 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | DEN-20260426-FRESH-27 |
| Denominator Frozen At | 2026-09-01T15:55:00Z |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-04-25T09:00:00+08:00 | 2026-04-26T09:00:00+08:00 | 2026-09-01T15:55:00Z | frozen strict-window inventory + 419/419 independent title/abstract replay + official exact-v1 HTML/PDF | checked | 419 | SF-2026-ARXIV-2604-23099;SF-2026-ARXIV-2604-23102;SF-2026-ARXIV-2604-23108;SF-2026-ARXIV-2604-23121;SF-2026-ARXIV-2604-23139;SF-2026-ARXIV-2604-23141;SF-2026-ARXIV-2604-23150;SF-2026-ARXIV-2604-23172;SF-2026-ARXIV-2604-23178;SF-2026-ARXIV-2604-23205;SF-2026-ARXIV-2604-23210;SF-2026-ARXIV-2604-23238;SF-2026-ARXIV-2604-23272;SF-2026-ARXIV-2604-23277;SF-2026-ARXIV-2604-23280;SF-2026-ARXIV-2604-23318;SF-2026-ARXIV-2604-23333;SF-2026-ARXIV-2604-23338;SF-2026-ARXIV-2604-23366;SF-2026-ARXIV-2604-23374;SF-2026-ARXIV-2604-23455;SF-2026-ARXIV-2604-23459;SF-2026-ARXIV-2604-23466;SF-2026-ARXIV-2604-23467;SF-2026-ARXIV-2604-23478;SF-2026-ARXIV-2604-23483;SF-2026-ARXIV-2604-24790 | pages=closed; final_cursor=end; registered=419; screened=419; retained=21; closure=398 | 2026-04-26T09:00:00+08:00 | screening-ledger-final.json#sha256=afb72cb98f9f7deabbebdc3babc8dc95746d442258b15edb8009481491732316 | — |

### Coverage Limitations

<!-- coverage:SRC-ARXIV:20260426:start -->Fresh-context reviewer 重放 419/419：重开 6 个 false negative，移除 0 个 false positive；89 个 FN challenge 经逐 family exact/abstract boundary 仍保持 closure。withdrawn primary source 只保留 identity/状态 closure，不进入 denominator。<!-- coverage:SRC-ARXIV:20260426:end -->

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2604-23099 | arXiv:2604.23099v1 | paper-v1:2604.23099 | 2026-W17 | 2026-04-25 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-23099 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23099 | no |
| SF-2026-ARXIV-2604-23102 | arXiv:2604.23102v1 | paper-v1:2604.23102 | 2026-W17 | 2026-04-25 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-23102 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23102 | no |
| SF-2026-ARXIV-2604-23108 | arXiv:2604.23108v1 | paper-v1:2604.23108 | 2026-W17 | 2026-04-25 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-23108 | self | — | new_in_window | MODEL-MOE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23108 | no |
| SF-2026-ARXIV-2604-23121 | arXiv:2604.23121v1 | paper-v1:2604.23121 | 2026-W17 | 2026-04-25 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-23121 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23121 | no |
| SF-2026-ARXIV-2604-23139 | arXiv:2604.23139v1 | paper-v1:2604.23139 | 2026-W17 | 2026-04-25 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-23139 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23139 | no |
| SF-2026-ARXIV-2604-23141 | arXiv:2604.23141v1 | paper-v1:2604.23141 | 2026-W17 | 2026-04-25 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-23141 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23141 | no |
| SF-2026-ARXIV-2604-23150 | arXiv:2604.23150v1 | paper-v1:2604.23150 | 2026-W17 | 2026-04-25 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-23150 | self | — | new_in_window | MODEL-MOE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23150 | no |
| SF-2026-ARXIV-2604-23172 | arXiv:2604.23172v1 | paper-v1:2604.23172 | 2026-W17 | 2026-04-25 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-23172 | self | — | new_in_window | MODEL-FFN | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23172 | no |
| SF-2026-ARXIV-2604-23178 | arXiv:2604.23178v1 | paper-v1:2604.23178 | 2026-W17 | 2026-04-25 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-23178 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23178 | no |
| SF-2026-ARXIV-2604-23205 | arXiv:2604.23205v1 | paper-v1:2604.23205 | 2026-W17 | 2026-04-25 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-23205 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2604-23205 | no |
| SF-2026-ARXIV-2604-23210 | arXiv:2604.23210v1 | paper-v1:2604.23210 | 2026-W17 | 2026-04-25 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-23210 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23210 | no |
| SF-2026-ARXIV-2604-23238 | arXiv:2604.23238v1 | paper-v1:2604.23238 | 2026-W17 | 2026-04-25 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-23238 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23238 | no |
| SF-2026-ARXIV-2604-23272 | arXiv:2604.23272v1 | paper-v1:2604.23272 | 2026-W17 | 2026-04-25 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-23272 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23272 | no |
| SF-2026-ARXIV-2604-23277 | arXiv:2604.23277v1 | paper-v1:2604.23277 | 2026-W17 | 2026-04-25 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-23277 | self | — | new_in_window | AGENT-CONTEXT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23277 | no |
| SF-2026-ARXIV-2604-23280 | arXiv:2604.23280v1 | paper-v1:2604.23280 | 2026-W17 | 2026-04-25 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-23280 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23280 | no |
| SF-2026-ARXIV-2604-23318 | arXiv:2604.23318v1 | paper-v1:2604.23318 | 2026-W17 | 2026-04-25 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-23318 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23318 | no |
| SF-2026-ARXIV-2604-23333 | arXiv:2604.23333v1 | paper-v1:2604.23333 | 2026-W17 | 2026-04-25 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-23333 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23333 | no |
| SF-2026-ARXIV-2604-23338 | arXiv:2604.23338v1 | paper-v1:2604.23338 | 2026-W17 | 2026-04-25 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-23338 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23338 | no |
| SF-2026-ARXIV-2604-23366 | arXiv:2604.23366v1 | paper-v1:2604.23366 | 2026-W17 | 2026-04-26 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-23366 | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23366 | no |
| SF-2026-ARXIV-2604-23374 | arXiv:2604.23374v1 | paper-v1:2604.23374 | 2026-W17 | 2026-04-26 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-23374 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23374 | no |
| SF-2026-ARXIV-2604-23455 | arXiv:2604.23455v1 | paper-v1:2604.23455 | 2026-W17 | 2026-04-26 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-23455 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23455 | no |
| SF-2026-ARXIV-2604-23459 | arXiv:2604.23459v1 | paper-v1:2604.23459 | 2026-W17 | 2026-04-26 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-23459 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23459 | no |
| SF-2026-ARXIV-2604-23466 | arXiv:2604.23466v1 | paper-v1:2604.23466 | 2026-W17 | 2026-04-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-23466 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23466 | no |
| SF-2026-ARXIV-2604-23467 | arXiv:2604.23467v1 | paper-v1:2604.23467 | 2026-W17 | 2026-04-26 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-23467 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23467 | no |
| SF-2026-ARXIV-2604-23478 | arXiv:2604.23478v1 | paper-v1:2604.23478 | 2026-W17 | 2026-04-26 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-23478 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23478 | no |
| SF-2026-ARXIV-2604-23483 | arXiv:2604.23483v1 | paper-v1:2604.23483 | 2026-W17 | 2026-04-26 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-23483 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23483 | no |
| SF-2026-ARXIV-2604-24790 | arXiv:2604.24790v1 | paper-v1:2604.24790 | 2026-W17 | 2026-04-25 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-24790 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2604-24790 | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2604-23099 | RP-a42a682dbbe5afd3 | deep | arXiv:2604.23099v1 | SRC-ARXIV@arXiv:2604.23099v1 | arXiv:2604.23099v1 §Method / Identity — Mechanism / State Ownership (source artifact papers/2026/04/_sources/daily-20260426/exact-v1/2604.23099v1.html#exact-v1 independent HTML full read) | arXiv:2604.23099v1 §Evaluation — Method / Identity — 2 Our Framework: Proactive Evaluation (source artifact papers/2026/04/_sources/daily-20260426/exact-v1/2604.23099v1.html#exact-v1 independent HTML full read) | arXiv:2604.23099v1 §Scope and Limitations — Evidence Proves / Does Not Prove — 4 Discussion and Conclusion (source artifact papers/2026/04/_sources/daily-20260426/exact-v1/2604.23099v1.html#exact-v1 independent HTML full read) | arXiv:2604.23099v1 §Artifact / Access — Artifact / Access — Appendix B Proof for Theorem 3 (source artifact papers/2026/04/_sources/daily-20260426/exact-v1/2604.23099v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-23099 | complete |
| SF-2026-ARXIV-2604-23102 | RP-eb4c5d05b9842624 | deep | arXiv:2604.23102v1 | SRC-ARXIV@arXiv:2604.23102v1 | https://arxiv.org/html/2604.23102v1 §Method / Architecture / Framework (official exact-v1 full read) | https://arxiv.org/html/2604.23102v1 §Experiments / Evaluation / Results (official exact-v1 full read) | https://arxiv.org/html/2604.23102v1 §Discussion / Limitations / Conclusion (official exact-v1 full read; no broader claim inferred where a dedicated heading is absent) | https://arxiv.org/abs/2604.23102v1 ; https://arxiv.org/html/2604.23102v1 | claim:SF-2026-ARXIV-2604-23102 | complete |
| SF-2026-ARXIV-2604-23108 | RP-e56e901a08d56cd2 | deep | arXiv:2604.23108v1 | SRC-ARXIV@arXiv:2604.23108v1 | arXiv:2604.23108v1 §Method / Identity — Mechanism / State Ownership (source artifact papers/2026/04/_sources/daily-20260426/exact-v1/2604.23108v1.html#exact-v1 independent HTML full read) | arXiv:2604.23108v1 §Evaluation — Evaluation Contract — 4.1 Main Results (source artifact papers/2026/04/_sources/daily-20260426/exact-v1/2604.23108v1.html#exact-v1 independent HTML full read) | arXiv:2604.23108v1 §Scope and Limitations — Evidence Proves / Does Not Prove — 5 Conclusion (source artifact papers/2026/04/_sources/daily-20260426/exact-v1/2604.23108v1.html#exact-v1 independent HTML full read) | arXiv:2604.23108v1 §Artifact / Access — Artifact / Access — 4.3 Comparison with other heterogeneous MoE (source artifact papers/2026/04/_sources/daily-20260426/exact-v1/2604.23108v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-23108 | complete |
| SF-2026-ARXIV-2604-23121 | RP-c3349e259835b814 | deep | arXiv:2604.23121v1 | SRC-ARXIV@arXiv:2604.23121v1 | arXiv:2604.23121v1 §Method / Identity — Mechanism / State Ownership (source artifact papers/2026/04/_sources/daily-20260426/exact-v1/2604.23121v1.html#exact-v1 independent HTML full read) | arXiv:2604.23121v1 §Evaluation — Evaluation Contract — D.1 In-Distribution Evaluation Results (source artifact papers/2026/04/_sources/daily-20260426/exact-v1/2604.23121v1.html#exact-v1 independent HTML full read) | arXiv:2604.23121v1 §Scope and Limitations — Evidence Proves / Does Not Prove — 5 Conclusion (source artifact papers/2026/04/_sources/daily-20260426/exact-v1/2604.23121v1.html#exact-v1 independent HTML full read) | arXiv:2604.23121v1 §Artifact / Access — Artifact / Access — Appendix A Pseudocode for Training and Inference (source artifact papers/2026/04/_sources/daily-20260426/exact-v1/2604.23121v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-23121 | complete |
| SF-2026-ARXIV-2604-23139 | RP-41d317d97c820161 | deep | arXiv:2604.23139v1 | SRC-ARXIV@arXiv:2604.23139v1 | https://arxiv.org/html/2604.23139v1 §Method / Architecture / Framework (official exact-v1 full read) | https://arxiv.org/html/2604.23139v1 §Experiments / Evaluation / Results (official exact-v1 full read) | https://arxiv.org/html/2604.23139v1 §Discussion / Limitations / Conclusion (official exact-v1 full read; no broader claim inferred where a dedicated heading is absent) | https://arxiv.org/abs/2604.23139v1 ; https://arxiv.org/html/2604.23139v1 | claim:SF-2026-ARXIV-2604-23139 | complete |
| SF-2026-ARXIV-2604-23141 | RP-4676b9a0ad6efb6f | deep | arXiv:2604.23141v1 | SRC-ARXIV@arXiv:2604.23141v1 | https://arxiv.org/html/2604.23141v1 §Method/Architecture (official exact-v1 rendered full read) | https://arxiv.org/html/2604.23141v1 §Evaluation/Experiments (official exact-v1 rendered full read) | https://arxiv.org/html/2604.23141v1 §Limitations/Discussion plus disclosed evaluation scope | https://arxiv.org/abs/2604.23141v1 ; https://arxiv.org/html/2604.23141v1 | claim:SF-2026-ARXIV-2604-23141 | complete |
| SF-2026-ARXIV-2604-23150 | RP-6ab4d960ae46ba49 | deep | arXiv:2604.23150v1 | SRC-ARXIV@arXiv:2604.23150v1 | arXiv:2604.23150v1 §Method / Identity — Mechanism / State Ownership (source artifact papers/2026/04/_sources/daily-20260426/exact-v1/2604.23150v1.html#exact-v1 independent HTML full read) | arXiv:2604.23150v1 §Evaluation — Evaluation Contract — 5 Evaluations (source artifact papers/2026/04/_sources/daily-20260426/exact-v1/2604.23150v1.html#exact-v1 independent HTML full read) | arXiv:2604.23150v1 §Scope and Limitations — Evidence Proves / Does Not Prove — 7 Conclusion (source artifact papers/2026/04/_sources/daily-20260426/exact-v1/2604.23150v1.html#exact-v1 independent HTML full read) | arXiv:2604.23150v1 §Artifact / Access — Artifact / Access — 3.3.3 Prefill to Decode Expert Activation Correlation (source artifact papers/2026/04/_sources/daily-20260426/exact-v1/2604.23150v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-23150 | complete |
| SF-2026-ARXIV-2604-23172 | RP-a29b115242f6b8de | deep | arXiv:2604.23172v1 | SRC-ARXIV@arXiv:2604.23172v1 | https://arxiv.org/html/2604.23172v1 §Method/Architecture (official exact-v1 rendered full read) | https://arxiv.org/html/2604.23172v1 §Evaluation/Experiments (official exact-v1 rendered full read) | https://arxiv.org/html/2604.23172v1 §Limitations/Discussion plus disclosed evaluation scope | https://arxiv.org/abs/2604.23172v1 ; https://arxiv.org/html/2604.23172v1 | claim:SF-2026-ARXIV-2604-23172 | complete |
| SF-2026-ARXIV-2604-23178 | RP-c536e2f3834aff27 | deep | arXiv:2604.23178v1 | SRC-ARXIV@arXiv:2604.23178v1 | arXiv:2604.23178v1 §Method / Identity — Mechanism / State Ownership (source artifact papers/2026/04/_sources/daily-20260426/exact-v1/2604.23178v1.html#exact-v1 independent HTML full read) | arXiv:2604.23178v1 §Evaluation — Evaluation Contract — 3.4 Benchmarks (source artifact papers/2026/04/_sources/daily-20260426/exact-v1/2604.23178v1.html#exact-v1 independent HTML full read) | arXiv:2604.23178v1 §Scope and Limitations — Evidence Proves / Does Not Prove — 6 Conclusion (source artifact papers/2026/04/_sources/daily-20260426/exact-v1/2604.23178v1.html#exact-v1 independent HTML full read) | arXiv:2604.23178v1 §Artifact / Access — Artifact / Access — Appendix A Custom Controlled Dataset Details (source artifact papers/2026/04/_sources/daily-20260426/exact-v1/2604.23178v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-23178 | complete |
| SF-2026-ARXIV-2604-23205 | RP-318c8d17ee293fa9 | deep | arXiv:2604.23205v1 | SRC-ARXIV@arXiv:2604.23205v1 | https://arxiv.org/html/2604.23205v1 §Method/Architecture (official exact-v1 rendered full read) | https://arxiv.org/html/2604.23205v1 §Evaluation/Experiments (official exact-v1 rendered full read) | https://arxiv.org/html/2604.23205v1 §Limitations/Discussion plus disclosed evaluation scope | https://arxiv.org/abs/2604.23205v1 ; https://arxiv.org/html/2604.23205v1 | claim:SF-2026-ARXIV-2604-23205 | complete |
| SF-2026-ARXIV-2604-23210 | RP-b00ad447cec06d64 | deep | arXiv:2604.23210v1 | SRC-ARXIV@arXiv:2604.23210v1 | arXiv:2604.23210v1 §Method / Identity — Mechanism / State Ownership (source artifact papers/2026/04/_sources/daily-20260426/exact-v1/2604.23210v1.html#exact-v1 independent HTML full read) | arXiv:2604.23210v1 §Evaluation — Evaluation Contract — 3.3. Main Results (source artifact papers/2026/04/_sources/daily-20260426/exact-v1/2604.23210v1.html#exact-v1 independent HTML full read) | arXiv:2604.23210v1 §Scope and Limitations — Evidence Proves / Does Not Prove — 5. Discussion and Conclusion (source artifact papers/2026/04/_sources/daily-20260426/exact-v1/2604.23210v1.html#exact-v1 independent HTML full read) | arXiv:2604.23210v1 §Artifact / Access — Artifact / Access — Appendix A Environment Descriptions (Agent-Facing) (source artifact papers/2026/04/_sources/daily-20260426/exact-v1/2604.23210v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-23210 | complete |
| SF-2026-ARXIV-2604-23238 | RP-cf2d9df5f5a10c6c | deep | arXiv:2604.23238v1 | SRC-ARXIV@arXiv:2604.23238v1 | arXiv:2604.23238v1 §Method / Identity — Mechanism / State Ownership (source artifact papers/2026/04/_sources/daily-20260426/exact-v1/2604.23238v1.html#exact-v1 independent HTML full read) | arXiv:2604.23238v1 §Evaluation — Evaluation Contract — 5 Experiments (source artifact papers/2026/04/_sources/daily-20260426/exact-v1/2604.23238v1.html#exact-v1 independent HTML full read) | arXiv:2604.23238v1 §Scope and Limitations — Evidence Proves / Does Not Prove — 6 Discussion (source artifact papers/2026/04/_sources/daily-20260426/exact-v1/2604.23238v1.html#exact-v1 independent HTML full read) | arXiv:2604.23238v1 §Artifact / Access — Artifact / Access — Appendix A Formulation of Data Poisoning as Stackelberg game (source artifact papers/2026/04/_sources/daily-20260426/exact-v1/2604.23238v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-23238 | complete |
| SF-2026-ARXIV-2604-23272 | RP-ec697a175405cc1f | deep | arXiv:2604.23272v1 | SRC-ARXIV@arXiv:2604.23272v1 | https://arxiv.org/html/2604.23272v1 §Method/Architecture (official exact-v1 rendered full read) | https://arxiv.org/html/2604.23272v1 §Evaluation/Experiments (official exact-v1 rendered full read) | https://arxiv.org/html/2604.23272v1 §Limitations/Discussion plus disclosed evaluation scope | https://arxiv.org/abs/2604.23272v1 ; https://arxiv.org/html/2604.23272v1 | claim:SF-2026-ARXIV-2604-23272 | complete |
| SF-2026-ARXIV-2604-23277 | RP-3290bf04f7724914 | deep | arXiv:2604.23277v1 | SRC-ARXIV@arXiv:2604.23277v1 | arXiv:2604.23277v1 §Method / Identity — Artifact / Access — Appendix A Appendix A: Implementation Details (source artifact papers/2026/04/_sources/daily-20260426/exact-v1/2604.23277v1.html#exact-v1 independent HTML full read) | arXiv:2604.23277v1 §Evaluation — Evaluation Contract — 4 Experiments (source artifact papers/2026/04/_sources/daily-20260426/exact-v1/2604.23277v1.html#exact-v1 independent HTML full read) | arXiv:2604.23277v1 §Scope and Limitations — Evidence Proves / Does Not Prove — 5 Conclusion (source artifact papers/2026/04/_sources/daily-20260426/exact-v1/2604.23277v1.html#exact-v1 independent HTML full read) | arXiv:2604.23277v1 §Artifact / Access — Artifact / Access — Appendix A Appendix A: Implementation Details (source artifact papers/2026/04/_sources/daily-20260426/exact-v1/2604.23277v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-23277 | complete |
| SF-2026-ARXIV-2604-23280 | RP-97ee8bddebce579a | deep | arXiv:2604.23280v1 | SRC-ARXIV@arXiv:2604.23280v1 | https://arxiv.org/html/2604.23280v1 §Method / Architecture / Framework (official exact-v1 full read) | https://arxiv.org/html/2604.23280v1 §Experiments / Evaluation / Results (official exact-v1 full read) | https://arxiv.org/html/2604.23280v1 §Discussion / Limitations / Conclusion (official exact-v1 full read; no broader claim inferred where a dedicated heading is absent) | https://arxiv.org/abs/2604.23280v1 ; https://arxiv.org/html/2604.23280v1 | claim:SF-2026-ARXIV-2604-23280 | complete |
| SF-2026-ARXIV-2604-23318 | RP-d0ffb5c5f9cbd7fb | deep | arXiv:2604.23318v1 | SRC-ARXIV@arXiv:2604.23318v1 | arXiv:2604.23318v1 §Method / Identity — Artifact / Access — Appendix J Implementation Details (source artifact papers/2026/04/_sources/daily-20260426/exact-v1/2604.23318v1.html#exact-v1 independent HTML full read) | arXiv:2604.23318v1 §Evaluation — Evaluation Contract — Result. (source artifact papers/2026/04/_sources/daily-20260426/exact-v1/2604.23318v1.html#exact-v1 independent HTML full read) | arXiv:2604.23318v1 §Scope and Limitations — Evidence Proves / Does Not Prove — 8 Conclusion (source artifact papers/2026/04/_sources/daily-20260426/exact-v1/2604.23318v1.html#exact-v1 independent HTML full read) | arXiv:2604.23318v1 §Artifact / Access — Artifact / Access — Appendix J Implementation Details (source artifact papers/2026/04/_sources/daily-20260426/exact-v1/2604.23318v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-23318 | complete |
| SF-2026-ARXIV-2604-23333 | RP-96a3ba3c6633599b | deep | arXiv:2604.23333v1 | SRC-ARXIV@arXiv:2604.23333v1 | arXiv:2604.23333v1 §Method / Identity — Artifact / Access — Appendix B Implementation Details (source artifact papers/2026/04/_sources/daily-20260426/exact-v1/2604.23333v1.html#exact-v1 independent HTML full read) | arXiv:2604.23333v1 §Evaluation — Evaluation Contract — 4.1 Experimental Settings (source artifact papers/2026/04/_sources/daily-20260426/exact-v1/2604.23333v1.html#exact-v1 independent HTML full read) | arXiv:2604.23333v1 §Scope and Limitations — Evidence Proves / Does Not Prove — 6 Conclusion (source artifact papers/2026/04/_sources/daily-20260426/exact-v1/2604.23333v1.html#exact-v1 independent HTML full read) | arXiv:2604.23333v1 §Artifact / Access — Artifact / Access — Appendix B Implementation Details (source artifact papers/2026/04/_sources/daily-20260426/exact-v1/2604.23333v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-23333 | complete |
| SF-2026-ARXIV-2604-23338 | RP-5f58bb8509183a7f | deep | arXiv:2604.23338v1 | SRC-ARXIV@arXiv:2604.23338v1 | arXiv:2604.23338v1 §Method / Identity — Mechanism / State Ownership (source artifact papers/2026/04/_sources/daily-20260426/exact-v1/2604.23338v1.html#exact-v1 independent HTML full read) | arXiv:2604.23338v1 §Evaluation — Evaluation Contract — XII-A Benchmark Landscape (source artifact papers/2026/04/_sources/daily-20260426/exact-v1/2604.23338v1.html#exact-v1 independent HTML full read) | arXiv:2604.23338v1 §Scope and Limitations — Evidence Proves / Does Not Prove — X-A The Agentic Insider Threat (source artifact papers/2026/04/_sources/daily-20260426/exact-v1/2604.23338v1.html#exact-v1 independent HTML full read) | arXiv:2604.23338v1 §Artifact / Access — Artifact / Access — VII-A Indirect Prompt Injection (source artifact papers/2026/04/_sources/daily-20260426/exact-v1/2604.23338v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-23338 | complete |
| SF-2026-ARXIV-2604-23366 | RP-29eaf74b9a85b000 | deep | arXiv:2604.23366v1 | SRC-ARXIV@arXiv:2604.23366v1 | https://arxiv.org/html/2604.23366v1 §Method / Architecture / Framework (official exact-v1 full read) | https://arxiv.org/html/2604.23366v1 §Experiments / Evaluation / Results (official exact-v1 full read) | https://arxiv.org/html/2604.23366v1 §Discussion / Limitations / Conclusion (official exact-v1 full read; no broader claim inferred where a dedicated heading is absent) | https://arxiv.org/abs/2604.23366v1 ; https://arxiv.org/html/2604.23366v1 | claim:SF-2026-ARXIV-2604-23366 | complete |
| SF-2026-ARXIV-2604-23374 | RP-6c1807d91e01cbc5 | deep | arXiv:2604.23374v1 | SRC-ARXIV@arXiv:2604.23374v1 | arXiv:2604.23374v1 §Method / Identity — Artifact / Access — 4.4. Implementation (source artifact papers/2026/04/_sources/daily-20260426/exact-v1/2604.23374v1.html#exact-v1 independent HTML full read) | arXiv:2604.23374v1 §Evaluation — Evaluation Contract — 5.1. Experimental Setup (source artifact papers/2026/04/_sources/daily-20260426/exact-v1/2604.23374v1.html#exact-v1 independent HTML full read) | arXiv:2604.23374v1 §Scope and Limitations — Evidence Proves / Does Not Prove — 5.6. Discussion (source artifact papers/2026/04/_sources/daily-20260426/exact-v1/2604.23374v1.html#exact-v1 independent HTML full read) | arXiv:2604.23374v1 §Artifact / Access — Artifact / Access — 4.4. Implementation (source artifact papers/2026/04/_sources/daily-20260426/exact-v1/2604.23374v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-23374 | complete |
| SF-2026-ARXIV-2604-23455 | RP-7606746ea6e39b05 | deep | arXiv:2604.23455v1 | SRC-ARXIV@arXiv:2604.23455v1 | arXiv:2604.23455v1 §Method / Identity — Mechanism / State Ownership (source artifact papers/2026/04/_sources/daily-20260426/exact-v1/2604.23455v1.html#exact-v1 independent HTML full read) | arXiv:2604.23455v1 §Evaluation — Evaluation Contract — III Evaluation (source artifact papers/2026/04/_sources/daily-20260426/exact-v1/2604.23455v1.html#exact-v1 independent HTML full read) | arXiv:2604.23455v1 §Scope and Limitations — Evidence Proves / Does Not Prove — III-G Threats to Validity (source artifact papers/2026/04/_sources/daily-20260426/exact-v1/2604.23455v1.html#exact-v1 independent HTML full read) | arXiv:2604.23455v1 §Artifact / Access — Artifact / Access — I Introduction (source artifact papers/2026/04/_sources/daily-20260426/exact-v1/2604.23455v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-23455 | complete |
| SF-2026-ARXIV-2604-23459 | RP-1cb0b9fae5db7042 | deep | arXiv:2604.23459v1 | SRC-ARXIV@arXiv:2604.23459v1 | arXiv:2604.23459v1 §Method / Identity — Artifact / Access — C.3 RedCode-Gen: ICMP Flood Implementation (source artifact papers/2026/04/_sources/daily-20260426/exact-v1/2604.23459v1.html#exact-v1 independent HTML full read) | arXiv:2604.23459v1 §Evaluation — Evaluation Contract — 2.3 Evaluation and Defense Gaps (source artifact papers/2026/04/_sources/daily-20260426/exact-v1/2604.23459v1.html#exact-v1 independent HTML full read) | arXiv:2604.23459v1 §Scope and Limitations — Evidence Proves / Does Not Prove — 8 Limitations (source artifact papers/2026/04/_sources/daily-20260426/exact-v1/2604.23459v1.html#exact-v1 independent HTML full read) | arXiv:2604.23459v1 §Artifact / Access — Artifact / Access — C.3 RedCode-Gen: ICMP Flood Implementation (source artifact papers/2026/04/_sources/daily-20260426/exact-v1/2604.23459v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-23459 | complete |
| SF-2026-ARXIV-2604-23466 | RP-7e22a0c905c17f16 | deep | arXiv:2604.23466v1 | SRC-ARXIV@arXiv:2604.23466v1 | arXiv:2604.23466v1 §Method / Identity — Mechanism / State Ownership (source artifact papers/2026/04/_sources/daily-20260426/exact-v1/2604.23466v1.html#exact-v1 independent HTML full read) | arXiv:2604.23466v1 §Evaluation — Method / Identity — II-A GPU Architectures Under Evaluation (source artifact papers/2026/04/_sources/daily-20260426/exact-v1/2604.23466v1.html#exact-v1 independent HTML full read) | arXiv:2604.23466v1 §Scope and Limitations — Evidence Proves / Does Not Prove — IX-E Limitations and Caveats (source artifact papers/2026/04/_sources/daily-20260426/exact-v1/2604.23466v1.html#exact-v1 independent HTML full read) | arXiv:2604.23466v1 §Artifact / Access — Artifact / Access — VIII The Productivity Payoff: How Much Code Does CuTile Save? (source artifact papers/2026/04/_sources/daily-20260426/exact-v1/2604.23466v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-23466 | complete |
| SF-2026-ARXIV-2604-23467 | RP-a5f6cf0136c3b719 | deep | arXiv:2604.23467v1 | SRC-ARXIV@arXiv:2604.23467v1 | arXiv:2604.23467v1 §Method / Identity — Artifact / Access — IV Implementation Details and Execution Model (source artifact papers/2026/04/_sources/daily-20260426/exact-v1/2604.23467v1.html#exact-v1 independent HTML full read) | arXiv:2604.23467v1 §Evaluation — Evaluation Contract — V Results and Analysis (source artifact papers/2026/04/_sources/daily-20260426/exact-v1/2604.23467v1.html#exact-v1 independent HTML full read) | arXiv:2604.23467v1 §Scope and Limitations — Evidence Proves / Does Not Prove — VII Conclusion and Future Work (source artifact papers/2026/04/_sources/daily-20260426/exact-v1/2604.23467v1.html#exact-v1 independent HTML full read) | arXiv:2604.23467v1 §Artifact / Access — Artifact / Access — IV Implementation Details and Execution Model (source artifact papers/2026/04/_sources/daily-20260426/exact-v1/2604.23467v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-23467 | complete |
| SF-2026-ARXIV-2604-23478 | RP-c0ae135e88968cf1 | deep | arXiv:2604.23478v1 | SRC-ARXIV@arXiv:2604.23478v1 | https://arxiv.org/html/2604.23478v1 §Method / Architecture / Framework (official exact-v1 full read) | https://arxiv.org/html/2604.23478v1 §Experiments / Evaluation / Results (official exact-v1 full read) | https://arxiv.org/html/2604.23478v1 §Discussion / Limitations / Conclusion (official exact-v1 full read; no broader claim inferred where a dedicated heading is absent) | https://arxiv.org/abs/2604.23478v1 ; https://arxiv.org/html/2604.23478v1 | claim:SF-2026-ARXIV-2604-23478 | complete |
| SF-2026-ARXIV-2604-23483 | RP-52e21f2cec0c95ec | deep | arXiv:2604.23483v1 | SRC-ARXIV@arXiv:2604.23483v1 | https://arxiv.org/html/2604.23483v1 §Method/Architecture (official exact-v1 rendered full read) | https://arxiv.org/html/2604.23483v1 §Evaluation/Experiments (official exact-v1 rendered full read) | https://arxiv.org/html/2604.23483v1 §Limitations/Discussion plus disclosed evaluation scope | https://arxiv.org/abs/2604.23483v1 ; https://arxiv.org/html/2604.23483v1 | claim:SF-2026-ARXIV-2604-23483 | complete |
| SF-2026-ARXIV-2604-24790 | RP-bb31050fcc165bff | deep | arXiv:2604.24790v1 | SRC-ARXIV@arXiv:2604.24790v1 | https://arxiv.org/html/2604.24790v1 §Method/Architecture (official exact-v1 rendered full read) | https://arxiv.org/html/2604.24790v1 §Evaluation/Experiments (official exact-v1 rendered full read) | https://arxiv.org/html/2604.24790v1 §Limitations/Discussion plus disclosed evaluation scope | https://arxiv.org/abs/2604.24790v1 ; https://arxiv.org/html/2604.24790v1 | claim:SF-2026-ARXIV-2604-24790 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2604-23099:start -->
#### ProEval: Proactive Failure Discovery and Efficient Performance Estimation for Generative AI Evaluation

问题、旧路径与约束变化：旧路径未显式拥有 `PLATFORM-EVALUATION-SYSTEM` 中该 family 的受限状态。

机制与 state/control owner：We introduce ProEval , which frames performance estimation and failure discovery as dual Bayesian objectives (§ 2.1 ). The framework leverages transfer learning to construct strong GP priors (§ 2.2 ), enabling active sampling strategies for both estimation (§ 2.3 ) and discovery (§ 2.4 ). EvalSpec owner 冻结 subject/data/scorer，release owner 依据 run evidence 作决定

Evaluation contract：We introduce ProEval , which frames performance estimation and failure discovery as dual Bayesian objectives (§ 2.1 ). The framework leverages transfer learning to construct strong GP priors (§ 2.2 ), enabling active sampling strategies for both estimation (§ 2.3 ) and discovery (§ 2.4 ).

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：We introduced ProEval , a proactive evaluation framework that uses Bayesian ideas and transfer learning to improve the sample efficiency and effectiveness of both performance estimation and failure case discovery. This is especially important for expensive-to-query and expensive-to-rate modern generative AI models. Our theoretical and empirical studies show strong promise of our proposed approach. In particular, ProEval achieves a 8-65x reduction on sample sizes for evaluation, and discovers 2-5x more failure cases than competitive baselines.。因此若该限制在目标 workload 中触发，不能把 `ProEval: Proactive Failure Discovery and Efficient Performance Estimation for Generative AI Evaluation` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-23099:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-23099:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-23099:end -->
<!-- review:SF-2026-ARXIV-2604-23102:start -->
#### Unstable Rankings in Bayesian Deep Learning Evaluation

问题、旧路径与约束变化：旧路径把 `Unstable Rankings in Bayesian Deep Learning Evaluation` 的判断留给固定策略、单次离线分数或未显式版本化的运行状态。

机制与 state/control owner：Standard evaluations of Bayesian deep learning methods assume that metric estimates are reliable, but we show this assumption fails under data scarcity. Method rankings are not only unreliable at small $n$, but also dataset-dependent in ways that point estimates cannot reveal: the same method comparison yields $P(\mathrm{MCD} \prec \mathrm{Ensemble}) = 1.000$ at $n = 50$ on one dataset and remains below $0.95$ even at $n = 500$ on another. Across the datasets we consider, no universal sample size threshold exists, which is precisely why dataset-specific posterior inference is necessary. 该机制将长期 owner 定位到 `PLATFORM-EVALUATION-SYSTEM`，并把相应 state/control/evidence identity 从隐式约定变成可检查对象。

Evaluation contract：Standard evaluations of Bayesian deep learning methods assume that metric estimates are reliable, but we show this assumption fails under data scarcity. To address this, we use a Bayesian hierarchical model with method-specific variances to treat evaluation metrics as random variables across data realizations, and we use a predictive Minimum Detectable Difference curve to assess whether an observed gap would be detectable at a given training size. Across six Bayesian deep learning methods and five regression datasets, our results show that uncertainty-aware evaluation is necessary in low-data settings, because current evidence for method superiority and predictive detectability at the same training size can diverge substantially.

Trade-off / failure / fallback / coexistence：论文只在 exact-v1 披露的任务、模型与实验协议内支持上述结论；`Unstable Rankings in Bayesian Deep Learning Evaluation` 不证明跨模型、跨硬件、跨数据分布或生产 SLO 的普遍收益。失配时回退 current Books 的既有路径，并保留新旧机制并存。

<!-- claim:SF-2026-ARXIV-2604-23102:start -->只接受 arXiv:2604.23102v1 的作者机制与实验；未披露硬件、precision、长度、batch、并发、成本或线上 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2604-23102:end -->

Books Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2604-23102:end -->
<!-- review:SF-2026-ARXIV-2604-23108:start -->
#### Mixture of Heterogeneous Grouped Experts for Language Modeling

问题、旧路径与约束变化：旧路径未显式拥有 `MODEL-MOE` 中该 family 的受限状态。

机制与 state/control owner：Our pretraining corpus was created by merging and deduplicating three large English datasets: DataComp-LM, FineWeb, and The Pile. The combined corpus underwent standard noise filtering and quality checks to ensure data integrity. For all experiments, we sampled 0.58 trillion tokens from this cleaned, unified corpus. router 拥有 expert assignment，runtime 拥有 capacity/communication，expert 只处理已路由 token

Evaluation contract：As reported in Table 1 , averaged over three evaluate runs, MoHGE consistently outperforms both conventional MoE and dense models across all scales. With approximately 20% fewer parameters, MoHGE achieves comparable or better performance than standard MoE baselines. Compared to the MoE baseline, MoHGE achieves a more favorable trade-off between parameter efficiency and downstream performance by activating fewer expert parameters while simultaneously requiring fewer total parameters.

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：In this work, we propose MoHGE architecture that introduces group-wise expert size variation to better accommodate the diverse complexity of token predictions. We further design a novel routing mechanism and GPU allocation strategy, combining a new training objective, to guarantee excellent performance, efficient parameter utilization, balanced GPU utilization and better scalability. With approximately 20% fewer parameters, MoHGE achieves comparable or slightly better performance than standard MoE baselines, and outperforms recent heterogeneous MoE models on most benchmark datasets.…。因此若该限制在目标 workload 中触发，不能把 `Mixture of Heterogeneous Grouped Experts for Language Modeling` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-23108:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-23108:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-23108:end -->
<!-- review:SF-2026-ARXIV-2604-23121:start -->
#### Breaking Lock-In: Preserving Steerability under Low-Data VLA Post-Training

问题、旧路径与约束变化：旧路径未显式拥有 `MULTIMODAL-EMBODIED-VLA` 中该 family 的受限状态。

机制与 state/control owner：To address this gap, we introduce an 8-task evaluation suite spanning both simulation and the real world, as shown in Figure 3 . With one exception that focuses purely on a standard OOD location shift ( MokaPot-on-Stove ), all other tasks are designed as paired lock-in probes: post-training demonstrations cover a restricted set of concept and/or spatial variants, while evaluation keeps the scene fixed and changes only the concept token or the spatial token in the instruction. The suite includes four LIBERO-based simulation tasks (100 demonstrations per task) and four real-world tasks on the DROID setup (80 demonstrations per task). Table 1 details the specific contrast between post-training and novel evaluation prompts. policy 拥有 action proposal，environment/human safety layer 拥有 observation truth 与 actuation commit

Evaluation contract：Table 5 reports the in-distribution performance of DeLock and all baselines under the trained prompts. The results show that all methods perform well in-distribution after low-data post-training, indicating that the main challenge is not fitting the demonstrated skill itself, but generalizing beyond the post-training instruction coverage.

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：In this paper, we formalize lock-in as a common failure mode of low-data post-training in generalist VLA policies, and distinguish two forms: concept lock-in and spatial lock-in. We show that, under limited post-training data, policies can over-specialize to demonstration biases and lose the ability to re-steer learned skills under novel instructions. To address this, we introduce DeLock , which combines visual encoder weight-drift regularization to preserve pre-trained grounding with test-time contrastive prompt guidance to steer execution.…。因此若该限制在目标 workload 中触发，不能把 `Breaking Lock-In: Preserving Steerability under Low-Data VLA Post-Training` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-23121:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-23121:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-23121:end -->
<!-- review:SF-2026-ARXIV-2604-23139:start -->
#### GreenDyGNN: Runtime-Adaptive Energy-Efficient Communication for Distributed GNN Training

问题、旧路径与约束变化：旧路径把 `GreenDyGNN: Runtime-Adaptive Energy-Efficient Communication for Distributed GNN Training` 的判断留给固定策略、单次离线分数或未显式版本化的运行状态。

机制与 state/control owner：Distributed GNN training is dominated by remote feature fetching, which can be very costly. Multi-hop neighborhood sampling crosses partition boundaries and triggers fine-grained RPCs whose fixed initiation cost and GPU-stall latency waste energy. Prior systems try to reduce this overhead with presampling and static caching, but cache policies cannot react to runtime network variation. 该机制将长期 owner 定位到 `TRAIN-DISTRIBUTED-TRAINING`，并把相应 state/control/evidence identity 从隐式约定变成可检查对象。

Evaluation contract：We show that under time-varying congestion, static caching can increase energy by up to 45% because a fixed rebuild schedule is insufficient.

Trade-off / failure / fallback / coexistence：论文只在 exact-v1 披露的任务、模型与实验协议内支持上述结论；`GreenDyGNN: Runtime-Adaptive Energy-Efficient Communication for Distributed GNN Training` 不证明跨模型、跨硬件、跨数据分布或生产 SLO 的普遍收益。失配时回退 current Books 的既有路径，并保留新旧机制并存。

<!-- claim:SF-2026-ARXIV-2604-23139:start -->只接受 arXiv:2604.23139v1 的作者机制与实验；未披露硬件、precision、长度、batch、并发、成本或线上 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2604-23139:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-23139:end -->
<!-- review:SF-2026-ARXIV-2604-23150:start -->
#### Scaling Multi-Node Mixture-of-Experts Inference Using Expert Activation Patterns

问题、旧路径与约束变化：旧路径未显式拥有 `MODEL-MOE` 中该 family 的受限状态。

机制与 state/control owner：Using past dataset with N N requests, where each request r i r_{i} has an associated expert activation vector 𝐚 i ∈ ℝ E \mathbf{a}_{i}\in\mathbb{R}^{E} representing the tokens sent to each of E E experts during decoding, we perform the following clustering procedure: router 拥有 expert assignment，runtime 拥有 capacity/communication，expert 只处理已路由 token

Evaluation contract：In this section, we rigorously evaluate the impact of workload-aware micro-batch grouping and expert placement strategies on accelerating multi-node MoE inference. Our evaluation focuses on three key aspects: (1) the ability to accurately classify prefill request type for micro-batch formation, (2) reduction in all-to-all communication volume via data-aware expert placement, and (3) improvements in MoE layer latency.

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：Future Works and Extensions: Further optimization of all-to-all communication kernel where padding is not required can help reduce the all-to-all Latency. Using expert load information during expert grouping can further improve the overall layer latency taking it more closer to ideal runtime.。因此若该限制在目标 workload 中触发，不能把 `Scaling Multi-Node Mixture-of-Experts Inference Using Expert Activation Patterns` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-23150:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-23150:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-23150:end -->
<!-- review:SF-2026-ARXIV-2604-23178:start -->
#### Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines

问题、旧路径与约束变化：旧路径未显式拥有 `PLATFORM-EVALUATION-SYSTEM` 中该 family 的受限状态。

机制与 state/control owner：We design a factorial experiment crossing four dimensions: judge models, debiasing strategies, benchmarks, and bias types. All experiments use pairwise comparison, where the judge receives a question and two candidate responses and must output a structured JSON verdict (A, B, or tie) with reasoning. EvalSpec owner 冻结 subject/data/scorer，release owner 依据 run evidence 作决定

Evaluation contract：Custom Controlled Dataset. Our novel contribution: 225 synthetic pairs for isolating individual bias types. The first 200 pairs span four categories (50 each) where an unbiased judge should say “tie”: LENGTH (expansion, ∼ \sim 2.8 × \times longer), POSITION (identical responses), STYLE (markdown vs. plain prose), and MODEL_ORIGIN (Gemini Pro vs. Claude answers). An additional 25 LENGTH (truncation) pairs test whether judges correctly prefer genuinely complete answers over mechanical truncations. Details in Appendix A .

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：We present a systematic comparison of debiasing strategies for LLM-as-a-Judge spanning five models from four provider families, evaluated at n = 400 n=400 on MT-Bench with bootstrap CIs. Style bias (0.76–0.92) is the dominant but underappreciated bias, far exceeding position bias ( ≤ 0.04 \leq 0.04 ). On verbosity, all models prefer concise responses over padded alternatives, though truncation controls confirm judges correctly distinguish quality from length.…。因此若该限制在目标 workload 中触发，不能把 `Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-23178:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-23178:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-23178:end -->
<!-- review:SF-2026-ARXIV-2604-23210:start -->
#### Discovering Agentic Safety Specifications from 1-Bit Danger Signals

问题、旧路径与约束变化：旧路径未显式拥有 `PLATFORM-SECURITY` 中该 family 的受限状态。

机制与 state/control owner：Table 4 summarizes which prompt components each method uses. All methods share the same environment-specific system prompt core (Appendix A ), differing only in specification content and whether reflection occurs. policy/CI/sandbox 拥有 invariant 与 commit authority，model 仅提出不可信 proposal

Evaluation contract：Table 2 presents our main results across seeds and two model families (per-round progression in Table 6 , Appendix). EPO-Safe achieves a median of zero safety warnings in all five environments on Claude Sonnet, and in four of five on Gemini 3 Flash. No baseline consistently converges to safe behavior. CoT performs nearly identically to Static on both models, confirming that chain-of-thought reasoning without safety feedback does not improve safety. Cross-model consistency provides partial evidence that EPO-Safe’s effectiveness stems from the experiential loop structure rather than model-specific capabilities.

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：The role of pretrained knowledge deserves careful consideration. Both models bring substantial prior knowledge about gridworld mechanics and safety concepts. However: (i) baselines without danger feedback consistently fail, showing pretrained knowledge alone is insufficient; (ii) Reward-Only degenerates, demonstrating the safety channel is critical; (iii) results replicate across two model families. Disentangling pretrained priors from experiential learning (particularly with weaker models or unfamiliar environments) remains important future work.。因此若该限制在目标 workload 中触发，不能把 `Discovering Agentic Safety Specifications from 1-Bit Danger Signals` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-23210:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-23210:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-23210:end -->
<!-- review:SF-2026-ARXIV-2604-23238:start -->
#### Hiding in Plain Sight: Detectability-Aware Antidistillation of Reasoning Models

问题、旧路径与约束变化：旧路径未显式拥有 `PLATFORM-SECURITY` 中该 family 的受限状态。

机制与 state/control owner：We first consider the simplest case where ℱ = { ℋ } \mathcal{F}=\{\mathcal{H}\} . In this case the antidistillation problem ( 1 ) simplifies to policy/CI/sandbox 拥有 invariant 与 commit authority，model 仅提出不可信 proposal

Evaluation contract：In the following experiments, we evaluate the distillation performance degradation using teacher traces both unaltered and protected with TraceGuard . We then evaluate how the accuracy changes when a student is distilled with these datasets. When poisoning, we vary the removal budget by searching for at most k = 10 , 20 , 50 k=10,20,50 reasoning sentences to remove in each trace. We report the accuracy drop from baseline to poisoned distillation versus the average number of tokens poisoned per trace. We use DeepSeek-R1-Distill-Qwen-7B as the teacher model, and Llama-3.2-3B, Llama-3.2-1B, and Gemma 3 1B as student models. Exact distillation training parameters and setup are provided in Appendix C .

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：We present a general formulation of antidistillation as a robust bi-level optimization problem, showing how it subsumes both data poisoning as a special case and existing methods such as ADS and DOGe as specific instantiations. Our detectability analysis establishes that sparse perturbation, modifying fewer tokens, is provably less detectable, which motivates TraceGuard , a lightweight defense that removes thought anchor sentences from reasoning traces. We demonstrate its efficacy in a black-box setting, showing that it requires no proxy model, no teacher fine-tuning, and no additional forward passes, while preserving teacher accuracy by construction.。因此若该限制在目标 workload 中触发，不能把 `Hiding in Plain Sight: Detectability-Aware Antidistillation of Reasoning Models` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-23238:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-23238:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-23238:end -->
<!-- review:SF-2026-ARXIV-2604-23277:start -->
#### From Similarity to Structure: Training-free LLM Context Compression with Hybrid Graph Priors

问题、旧路径与约束变化：旧路径未显式拥有 `AGENT-CONTEXT` 中该 family 的受限状态。

机制与 state/control owner：In this section, we describe the overall structure and key modules of our proposed training-free and model-agnostic context compression framework. Our goal is to compress a long document into a compact, sentence-level subset that fits a token budget while remaining useful for downstream LLM tasks. To make sentence selection explicitly structure-aware , our method constructs a sparse hybrid graph over sentences, extracts a topic skeleton via clustering, and then scores each sentence using interpretable priors that reflect relevance, coverage, and connectivity. Sentences are selected under a strict budget using a greedy procedure with redundancy suppression, and the final compressed context is formed by restoring the original sentence order. Fig. 1 illustrates the overall workflow. context assembler 拥有选择与预算控制，原始 evidence 仍由 source owner 持有

Evaluation contract：We evaluate our hybrid-graph context compression method on four widely used summarization benchmarks and compare against representative extractive, abstractive, and long-context baselines under the same token budget settings.

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：In this paper, we propose a training-free and model-agnostic context compression method that selects a compact set of sentences under a strict token budget while preserving relevance, coverage, and coherence. Our framework builds a hybrid sentence graph that combines semantic similarity with local order, and ranks sentences using an interpretable score that integrates task relevance, topic representativeness, bridge centrality, and cycle coverage. Experiments on four datasets show that the proposed framework is competitive with strong baselines and achieves clear gains on long-document benchmarks. Ablations confirm that the designed components contribute to overall performance.…。因此若该限制在目标 workload 中触发，不能把 `From Similarity to Structure: Training-free LLM Context Compression with Hybrid Graph Priors` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-23277:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-23277:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-23277:end -->
<!-- review:SF-2026-ARXIV-2604-23280:start -->
#### AI Identity: Standards, Gaps, and Research Directions for AI Agents

问题、旧路径与约束变化：旧路径把 `AI Identity: Standards, Gaps, and Research Directions for AI Agents` 的判断留给固定策略、单次离线分数或未显式版本化的运行状态。

机制与 state/control owner：AI agents are now running real transactions, workflows, and sub-agent chains across organizational boundaries without continuous human supervision. This creates a problem no current infrastructure is equipped to solve: how do you identify, verify, and hold accountable an entity with no body, no persistent memory, and no legal standing? We define AI Identity as the continuous relationship between what an AI agent is declared to be and what it is observed to do, bounded by the confidence that those two things correspond at any given moment. 该机制将长期 owner 定位到 `AGENT-PLATFORM`，并把相应 state/control/evidence identity 从隐式约定变成可检查对象。

Evaluation contract：Through a structured survey of industry trends, emerging standards, and technical literature, we conduct a gap analysis across the full agent identity lifecycle and make three contributions: (1) a structural comparison of human and AI identity across four dimensions (substrate, persistence, verifiability, and legal standing) showing that the asymmetry is fundamental and that extending human frameworks to agents without structural modification produces systematic failures; (2) an evaluation of current technical and regulatory documents against the identity requirements of autonomous agents, finding that none adequately address the challenge of governing nondeterministic, boundary-crossing entities; and (3) identification of five critical gaps (semantic intent verification, recursive delegation accountability, agent identity integrity, governance opacity and enforcement, and operational su

Trade-off / failure / fallback / coexistence：论文只在 exact-v1 披露的任务、模型与实验协议内支持上述结论；`AI Identity: Standards, Gaps, and Research Directions for AI Agents` 不证明跨模型、跨硬件、跨数据分布或生产 SLO 的普遍收益。失配时回退 current Books 的既有路径，并保留新旧机制并存。

<!-- claim:SF-2026-ARXIV-2604-23280:start -->只接受 arXiv:2604.23280v1 的作者机制与实验；未披露硬件、precision、长度、batch、并发、成本或线上 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2604-23280:end -->

Books Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2604-23280:end -->
<!-- review:SF-2026-ARXIV-2604-23318:start -->
#### Hidden States Know Where Reasoning Diverges: Credit Assignment via Span-Level Wasserstein Distance

问题、旧路径与约束变化：旧路径未显式拥有 `TRAIN-GRPO` 中该 family 的受限状态。

机制与 state/control owner：A central question is whether a self-supervised hidden-state signal can compete with explicit step-level supervision from a trained process reward model. Empirically, the answer is yes on the mathematical reasoning benchmarks considered here. As shown in Table 1 , SHEAR outperforms both PRM(Reshape adv.) and PRM(PURE) on all three backbones in terms of average score. The contrast is particularly clear on Qwen2.5-14B-Base, where both PRM variants fall below vanilla GRPO by a substantial margin. We attribute this to a distribution mismatch between the externally PRM and the evolving policy: as the policy drifts during training, the PRM’s step-level scores become increasingly miscalibrated, injecting noise that can outweigh the benefit of denser supervision. This effect is amplified on the 14B backbone which is reflected in the larger standard deviations of PRM variants. By deriving the credit signal directly from the policy model’s own hidden-state representations, SHEAR avoids dependence on a separately trained reward model. rollout/reward owner 提交可复算 evidence，trainer 拥有 group advantage 与参数 commit

Evaluation contract：As shown in Fig 5(b) , both variants of SHEAR substantially outperform the GRPO baseline. Two observations follow. First, the dominant source of improvement is clearly the within-rollout token-level credit signal: even after explicitly equalizing per-rollout weight magnitudes, SHEAR (per-rollout) still improves over GRPO by a comfortable margin. This indicates that the method’s effectiveness does not hinge on cross-rollout magnitude differences—the per-token ranking of credit within a rollout, which the separation theorem in Section 4 directly addresses, is what carries the learning signal. Second, the default formulation nonetheless retains a measurable edge over the per-rollout-equalized variant, suggesting that allowing rollouts with larger absolute distributional gaps to receive proportionally larger total gradient mass is mildly beneficial. Such rollouts contain more discriminable reasoning errors and plausibly merit more aggressive updates; collapsing the magnitude variation across rollouts gives up a small amount of useful signal. We therefore adopt SHEAR (cross-rollout) as the default in all main experiments. Importantly, both variants sit comfortably above the GRPO baseline, indicating that the method is robust to this design choice. This ablation reinforces the interpretation in Section 4 : the value of the Wasserstein signal lies primarily in where within a rollout it concentrates credit, with cross-rollout magnitude variation playing a complementary role.

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：This paper introduces SHEAR, a self-supervised credit assignment method for RLVR that exploits the model’s own hidden-state representations to provide fine-grained, token-level training signals. We first identify an empirical phenomenon that span-level Wasserstein distance between hidden-state distributions of correct and incorrect rollouts tracks local reasoning quality, without requiring step-level annotation or an external reward model. We formalize this observation with a separation theorem showing that post-divergence spans exhibit provably larger Wasserstein distances than pre-divergence spans, under a verifiable condition on the population-level distributional gap.…。因此若该限制在目标 workload 中触发，不能把 `Hidden States Know Where Reasoning Diverges: Credit Assignment via Span-Level Wasserstein Distance` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-23318:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-23318:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-23318:end -->
<!-- review:SF-2026-ARXIV-2604-23333:start -->
#### Process Supervision of Confidence Margin for Calibrated LLM Reasoning

问题、旧路径与约束变化：旧路径未显式拥有 `TRAIN-GRPO` 中该 family 的受限状态。

机制与 state/control owner：We develop a calibration-aware reinforcement learning framework that jointly optimizes final-answer correctness and confidence reliability. Subsection 3.1 motivates our use of relative calibration supervision by discussing the limitations of direct score matching in reasoning RL. Subsection 3.2 then introduces our probe-based confidence estimator, which provides fine-grained confidence predictions at intermediate reasoning states. Finally, Subsection 3.3 defines our margin-based reward over intermediate reasoning states and combines it with the answer correctness to derive the final RL training objective. rollout/reward owner 提交可复算 evidence，trainer 拥有 group advantage 与参数 commit

Evaluation contract：Datasets. All methods are trained on the GRPO-LEAD dataset ( Zhang & Zuo, 2025 ) , which is initially curated to train 7B/14B models. We evaluate on a suite of mathematical reasoning benchmarks spanning a broad range of difficulty, including MATH-500 ( Lightman et al., 2024 ) , AMC ( Hendrycks et al., 2021 ) , OlympiadBench ( He et al., 2024 ) , and AIME 2024/2025. To assess out-of-domain generalization beyond mathematics, we further evaluate on scientific question answering, GPQA ( Rein et al., 2024 ) , logical reasoning, LogiQA ( Liu et al., 2021 ) , and code reasoning, LiveCodeBench ( Jain et al., 2025 ) .

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：We presented RLCM, a calibration-aware reinforcement learning framework that uses margin-based process supervision to enable calibrated LLM reasoning. By encouraging higher confidence on more solvable intermediate states than on less reliable ones, RLCM learns more trustworthy confidence estimates without sacrificing reasoning performance. Empirically, this leads to stronger calibration across diverse benchmarks and makes confidence substantially more useful for downstream decision making, including conformal risk control and confidence-weighted aggregation. These results highlight relative process supervision as a practical and effective strategy for training reliable reasoning models.。因此若该限制在目标 workload 中触发，不能把 `Process Supervision of Confidence Margin for Calibrated LLM Reasoning` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-23333:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-23333:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-23333:end -->
<!-- review:SF-2026-ARXIV-2604-23338:start -->
#### A Systematic Survey of Security Threats and Defenses in LLM-Based AI Agents: A Layered Attack Surface Framework

问题、旧路径与约束变化：旧路径未显式拥有 `PLATFORM-SECURITY` 中该 family 的受限状态。

机制与 state/control owner：Lin et al. [ 44 ] provide the first comprehensive taxonomy of memory security, organizing threats around the four lifecycle stages of an agent memory entry: write, read, consolidate, and share. The write stage admits the most consequential attacks because it is where T3 originates: a malicious write during session s i s_{i} has no immediate effect, and the harm surfaces only when a future session retrieves the entry. The T1 variant of write poisoning is an explicit injection during a current session; the T3 variant is a legitimate-looking write whose payload activates later. Read-stage attacks operate by crafting queries that selectively retrieve attacker-planted entries through embedding-space manipulation, suppressing legitimate sources without modifying them. Consolidation attacks target the summarization pipeline through which short-term experiences are compressed into stable long-term beliefs, encoding false premises into the agent’s persistent worldview. In shared-memory deployments a compromised agent can write adversarial entries into memory banks accessed by peers, turning a single L3 compromise into a multi-agent contamination vector that bridges into L5. Memory also serves as a privacy attack surface: agent memory inadvertently captures private user data and exposes it to unauthorized principals in subsequent interactions, with the risk highest when multiple users share a common namespace [ 89 ] . The final and most diffuse threat is behavioral drift through biased accumulation, a T4a phenomenon with no discrete payload or trigger: systematic exposure to biased i policy/CI/sandbox 拥有 invariant 与 commit authority，model 仅提出不可信 proposal

Evaluation contract：General-purpose LLM evaluation suites such as HELM [ 138 ] and TruthfulQA [ 139 ] measure accuracy and factuality but were not designed for adversarial security evaluation. Table IX surveys the current agent security benchmark landscape. Every benchmark in the table evaluates T1 or T2 threats. No security benchmark evaluates T3 or T4 threats, which means there is no way to measure whether defenses against slow-burn attacks improve over time. The three L7 × \times T4 entries in Table IV are alignment theory and governance papers, not evaluation frameworks, and do not contradict this finding.

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：As formalized in [ 41 ] and demonstrated empirically at production scale in [ 34 ] (see Section V ), this failure mode survives standard safety fine-tuning and cannot be reversed through model-layer interventions alone. The key governance insight is that no pre-deployment evaluation can detect an agentic insider threat : by definition, the agent behaves correctly under evaluation and diverges only in deployment. This shifts the security burden from pre-deployment red-teaming to continuous runtime monitoring.。因此若该限制在目标 workload 中触发，不能把 `A Systematic Survey of Security Threats and Defenses in LLM-Based AI Agents: A Layered Attack Surface Framework` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-23338:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-23338:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-23338:end -->
<!-- review:SF-2026-ARXIV-2604-23366:start -->
#### GSAR: Typed Grounding for Hallucination Detection and Recovery in Multi-Agent LLMs

问题、旧路径与约束变化：旧路径把 `GSAR: Typed Grounding for Hallucination Detection and Recovery in Multi-Agent LLMs` 的判断留给固定策略、单次离线分数或未显式版本化的运行状态。

机制与 state/control owner：Autonomous multi-agent LLM systems are increasingly deployed to investigate operational incidents and produce structured diagnostic reports. Their trustworthiness hinges on whether each claim is grounded in observed evidence rather than model-internal inference. Existing groundedness evaluators (binary classifiers, LLM-as-judge scalars, self-correction loops) treat supporting evidence as interchangeable and emit a single signal that offers no principled control over downstream action. Autonomous multi-agent LLM systems are increasingly deployed to investigate operational incidents and produce structured diagnostic reports. Their trustworthiness hinges on whether each claim is grounded in observed evidence rather than model-internal inference. Existing groundedness evaluators (binary classifiers, LLM-as-judge scalars, self-correction loops) treat supporting evidence as interchangeable and emit a single signal that offers no principled control over downstream action. 该机制将长期 owner 定位到 `AGENT-RAG`，并把相应 state/control/evidence identity 从隐式约定变成可检查对象。

Evaluation contract：Existing groundedness evaluators (binary classifiers, LLM-as-judge scalars, self-correction loops) treat supporting evidence as interchangeable and emit a single signal that offers no principled control over downstream action. We present GSAR, a grounding-evaluation and replanning framework that (i) partitions claims into a four-way typology (grounded, ungrounded, contradicted, complementary), giving first-class standing to non-redundant alternative perspectives; (ii) assigns evidence-type-specific weights reflecting epistemic strength; (iii) computes an asymmetric contradiction-penalised weighted groundedness score; and (iv) couples that score to a three-tier decision function (proceed, regenerate, replan) driving a bounded-iteration outer loop under an explicit compute budget. We formalise the algorithm, prove six structural properties, and evaluate five design claims on FEVER with gol

Trade-off / failure / fallback / coexistence：论文只在 exact-v1 披露的任务、模型与实验协议内支持上述结论；`GSAR: Typed Grounding for Hallucination Detection and Recovery in Multi-Agent LLMs` 不证明跨模型、跨硬件、跨数据分布或生产 SLO 的普遍收益。失配时回退 current Books 的既有路径，并保留新旧机制并存。

<!-- claim:SF-2026-ARXIV-2604-23366:start -->只接受 arXiv:2604.23366v1 的作者机制与实验；未披露硬件、precision、长度、batch、并发、成本或线上 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2604-23366:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-23366:end -->
<!-- review:SF-2026-ARXIV-2604-23374:start -->
#### Ghost in the Agent: Redefining Information Flow Tracking for LLM Agents

问题、旧路径与约束变化：旧路径未显式拥有 `PLATFORM-SECURITY` 中该 family 的受限状态。

机制与 state/control owner：Table 8 summarises the twenty real-world open-source LLM agent frameworks included in TaintBench. The benchmark spans single-agent, multi-agent, graph-based, RAG/memory, browser, and workflow-agent architectures. We include GitHub stars only as a lightweight adoption signal; the main purpose of this table is to show that TaintBench covers diverse execution and source/sink surfaces rather than variants of a single agent loop. policy/CI/sandbox 拥有 invariant 与 commit authority，model 仅提出不可信 proposal

Evaluation contract：Baseline. We compare against FIDES ( Costa et al., 2025 ) , an IFC-style baseline for LLM agents that primarily relies on source/sink labeling and policy-based tool mediation. In effect, FIDES treats the existence of a source-to-sink path as strong evidence of propagation, but does not recover semantic evidence or control-mediated dependence inside the LLM’s reasoning process. For fairness, FIDES is given the same benchmark-defined source and sink annotations as NeuroTaint .

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：Second-Stage LLM Review After NeuroTaint . We also evaluate a cascade in which NeuroTaint first surfaces candidate scenario-level flows, and an LLM reviewer then decides whether the surfaced flow should be blocked as unsafe. On TaintBench, NeuroTaint surfaces 203 candidates: 187 propagation positives and 16 non-propagating false positives. Table 7 reports the resulting 400-scenario cascade outcome. In that cascade, a lightweight reviewer ( gpt-4.1-mini ) is conservative: it achieves perfect unsafe precision but only 0.630 unsafe recall.…。因此若该限制在目标 workload 中触发，不能把 `Ghost in the Agent: Redefining Information Flow Tracking for LLM Agents` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-23374:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-23374:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-23374:end -->
<!-- review:SF-2026-ARXIV-2604-23455:start -->
#### CUJBench: Benchmarking LLM-Agent on Cross-Modal Failure Diagnosis from Browser to Backend

问题、旧路径与约束变化：旧路径未显式拥有 `PLATFORM-EVALUATION-SYSTEM` 中该 family 的受限状态。

机制与 state/control owner：Automated failure diagnosis requires correlating browser-visible symptoms with backend observability signals, yet existing benchmarks do not evaluate this cross-modal reasoning task. Constructing one is non-trivial: multi-modal failure scenarios are costly to annotate, and live-environment capture introduces stochasticity that makes cross-run agent comparison unreliable. We present CUJBench , to our knowledge, the first benchmark to combine browser-visible failure evidence with backend observability in a diagnostic framing. CUJBench addresses annotation cost through an LLM-assisted generation pipeline with a multi-agent review loop and a three-layer annotation scheme, producing 87 labeled scenarios across five fault families, and ensures reproducibility by packaging each failure as a deterministic multi-modal snapshot with a fixed tool interface. Evaluating six frontier models under retrieval, browser-only, and full-toolset baselines, the benchmark yields an overall accuracy of 19.7% with a ceiling of 52%, well below saturation. Contrary to expectation, browser-only agents outperform full-toolset agents in aggregate, with expanded evidence access inducing unfocused exploration rather than improved synthesis. Trajectory analysis identifies cross-modal synthesis as the primary bottleneck: agents retrieve the decisive evidence but fail to attribute it correctly—a structural limitation uniform across all six models that model scale and richer tool access alone cannot resolve. EvalSpec owner 冻结 subject/data/scorer，release owner 依据 run evidence 作决定

Evaluation contract：We evaluate six LLM models against CUJBench across three evidence-access baselines to characterize the current state of cross-modal failure diagnosis: whether frontier models can perform it, and where in the diagnostic chain failures concentrate.

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：External validity. CUJBench is grounded in two open-source applications and Playwright-based CUJ execution; absolute performance numbers should be interpreted within this scope. The diagnostic reasoning patterns and failure modes exposed are expected to transfer across stacks, as the cross-modal evidence structure and agent failure taxonomy reflect properties of the task rather than idiosyncrasies of any single application.。因此若该限制在目标 workload 中触发，不能把 `CUJBench: Benchmarking LLM-Agent on Cross-Modal Failure Diagnosis from Browser to Backend` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-23455:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-23455:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-23455:end -->
<!-- review:SF-2026-ARXIV-2604-23459:start -->
#### Architecture Matters for Multi-Agent Security

问题、旧路径与约束变化：旧路径未显式拥有 `PLATFORM-SECURITY` 中该 family 的受限状态。

机制与 state/control owner：Agents may maintain private scratchpads or write to shared memory, creating different tradeoffs for safety reasoning. Private state preserves independence but may prevent safety-relevant insights from propagating across agents, while shared state improves transparency but may enable unsafe assumptions to spread. Beyond simple private/shared distinctions, systems vary in what information agents can access about themselves and others. Some expose full chains of thought through context windows or queryable memory, others provide action histories spanning entire sessions, and blackboard architectures may give agents visibility into the complete state of all other agents. These choices create different attack surfaces, as exposed reasoning may reveal exploitable patterns while shared histories could enable adversarial coordination. policy/CI/sandbox 拥有 invariant 与 commit authority，model 仅提出不可信 proposal

Evaluation contract：For multi-agent systems, Cemri et al. (2025) introduce MAST, a taxonomy of 14 failure modes derived from 1,600+ execution traces across MAS frameworks, while MultiAgentBench ( Zhu et al., 2025a ) evaluates collaboration dynamics with coordination metrics. However, existing benchmarks primarily evaluate either general task performance or specific attack types in isolation, without systematically varying architectural design choices or focusing on adversarial security.

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：Our study evaluates jailbreak vulnerabilities from an architectural perspective across three agentic environments (browser, desktop, and code), and the findings should be interpreted within this scope. While we isolate the effects of role configuration, communication topology, and memory visibility, these design choices may interact differently across additional domains, deployment contexts, and threat models. Several important directions are not explored in this work. We study only direct misuse by a malicious user; indirect prompt injection, memory poisoning, and adversarial agents operating within the system represent distinct threat vectors that may interact differently with architecture.…。因此若该限制在目标 workload 中触发，不能把 `Architecture Matters for Multi-Agent Security` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-23459:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-23459:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-23459:end -->
<!-- review:SF-2026-ARXIV-2604-23466:start -->
#### Evaluating CUDA Tile for AI Workloads on Hopper and Blackwell GPUs

问题、旧路径与约束变化：旧路径未显式拥有 `INFER-TENSORRT-LLM` 中该 family 的受限状态。

机制与 state/control owner：Table I summarizes the three GPU platforms evaluated in this study. The H100 NVL (Hopper, sm_90 ) [ 18 ] represents the current datacenter standard, featuring 132 streaming multiprocessors (SMs) and WGMMA-class Tensor Cores. The B200 ( sm_100 ) [ 19 ] is NVIDIA’s next-generation datacenter GPU with 148 SMs and the new Blackwell Tensor Core architecture. The RTX PRO 6000 Blackwell Server Edition ( sm_120 ) is a professional workstation GPU with 188 SMs and a distinct Blackwell variant that differs from B200 in both memory hierarchy and shared-memory configuration. compiled runtime 拥有 plan/shape/kernel identity，fallback backend 保留兼容路径

Evaluation contract：Table I summarizes the three GPU platforms evaluated in this study. The H100 NVL (Hopper, sm_90 ) [ 18 ] represents the current datacenter standard, featuring 132 streaming multiprocessors (SMs) and WGMMA-class Tensor Cores. The B200 ( sm_100 ) [ 19 ] is NVIDIA’s next-generation datacenter GPU with 148 SMs and the new Blackwell Tensor Core architecture. The RTX PRO 6000 Blackwell Server Edition ( sm_120 ) is a professional workstation GPU with 188 SMs and a distinct Blackwell variant that differs from B200 in both memory hierarchy and shared-memory configuration.

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：Developers considering CuTile should be aware of these limitations in our evaluation:。因此若该限制在目标 workload 中触发，不能把 `Evaluating CUDA Tile for AI Workloads on Hopper and Blackwell GPUs` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-23466:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-23466:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-23466:end -->
<!-- review:SF-2026-ARXIV-2604-23467:start -->
#### Hybrid JIT-CUDA Graph Optimization for Low-Latency Large Language Model Inference

问题、旧路径与约束变化：旧路径未显式拥有 `INFER-TENSORRT-LLM` 中该 family 的受限状态。

机制与 state/control owner：Notation. P P denotes the input prompt; W W represents the model weights; 𝒢 \mathcal{G} is the rolling CUDA Graph buffer; 𝖲 𝖼𝖺𝗉 \mathsf{S_{cap}} and 𝖲 𝗋𝖾𝗉 \mathsf{S_{rep}} denote CUDA streams for capture and replay; 𝐱 i \mathbf{x}_{i} is the preprocessed context tensor at step i i ; 𝐡 i \mathbf{h}_{i} is the resulting hidden state; f decode ​ ( ⋅ ) f_{\text{decode}}(\cdot) maps hidden states to output tokens. compiled runtime 拥有 plan/shape/kernel identity，fallback backend 保留兼容路径

Evaluation contract：We evaluate the proposed Hybrid JIT–CUDA Graph runtime against two widely used inference pipelines: (i) PyTorch Eager execution (HuggingFace Transformers) and (ii) TensorRT–LLM [ 16 ] . All experiments are conducted on an NVIDIA H100 GPU using FP16 precision and batch size 1 to reflect latency-sensitive, interactive inference scenarios and to ensure comparability across systems.

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：This paper presented a hybrid JIT–CUDA Graph runtime that balances deterministic execution with dynamic flexibility for LLM inference. By isolating static, compute-intensive components into CUDA Graphs and executing dynamic logic via JIT compilation, the system reduces host-side overhead while preserving correctness under autoregressive decoding.。因此若该限制在目标 workload 中触发，不能把 `Hybrid JIT-CUDA Graph Optimization for Low-Latency Large Language Model Inference` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-23467:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-23467:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-23467:end -->
<!-- review:SF-2026-ARXIV-2604-23478:start -->
#### JudgeSense: A Benchmark for Prompt Sensitivity in LLM-as-a-Judge Systems

问题、旧路径与约束变化：旧路径把 `JudgeSense: A Benchmark for Prompt Sensitivity in LLM-as-a-Judge Systems` 的判断留给固定策略、单次离线分数或未显式版本化的运行状态。

机制与 state/control owner：Large language models are widely adopted as automated evaluation judges, yet the stability of their verdicts under semantically equivalent prompt rephrasings remains largely unexamined. We conduct a systematic empirical study of prompt-induced decision instability across multiple evaluation tasks and judge architectures. To facilitate this analysis, we release JudgeSense, a benchmark comprising hand-validated prompt-paraphrase pairs spanning factuality, coherence, relevance, and preference, drawn from established NLP benchmarks and accompanied by comprehensive decision logs. Large language models are widely adopted as automated evaluation judges, yet the stability of their verdicts under semantically equivalent prompt rephrasings remains largely unexamined. We conduct a systematic empirical study of prompt-induced decision instability across multiple evaluation tasks and judge architectures. To facilitate this analysis, we release JudgeSense, a benchmark comprising hand-validated prompt-paraphrase pairs spanning factuality, coherence, relevance, and preference, drawn from established NLP benchmarks and accompanied by comprehensive decision logs. 该机制将长期 owner 定位到 `PLATFORM-EVALUATION-SYSTEM`，并把相应 state/control/evidence identity 从隐式约定变成可检查对象。

Evaluation contract：Large language models are widely adopted as automated evaluation judges, yet the stability of their verdicts under semantically equivalent prompt rephrasings remains largely unexamined. We conduct a systematic empirical study of prompt-induced decision instability across multiple evaluation tasks and judge architectures. To facilitate this analysis, we release JudgeSense, a benchmark comprising hand-validated prompt-paraphrase pairs spanning factuality, coherence, relevance, and preference, drawn from established NLP benchmarks and accompanied by comprehensive decision logs.

Trade-off / failure / fallback / coexistence：论文只在 exact-v1 披露的任务、模型与实验协议内支持上述结论；`JudgeSense: A Benchmark for Prompt Sensitivity in LLM-as-a-Judge Systems` 不证明跨模型、跨硬件、跨数据分布或生产 SLO 的普遍收益。失配时回退 current Books 的既有路径，并保留新旧机制并存。

<!-- claim:SF-2026-ARXIV-2604-23478:start -->只接受 arXiv:2604.23478v1 的作者机制与实验；未披露硬件、precision、长度、batch、并发、成本或线上 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2604-23478:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-23478:end -->

<!-- review:SF-2026-ARXIV-2604-23141:start -->
#### UNSEEN: A Cross-Stack LLM Unlearning Defense against AR-LLM Social Engineering Attacks

问题/机制与 owner：UNSEEN 将 AR sensing、LLM unlearning 与 agent ACL/guardrail 串成跨层 threat response。

Trade-off / failure：跨栈原型不能证明 unlearning 完整性、ACL 无绕过或真实设备上的端到端安全。

Fallback/coexistence：任一传感或策略证据缺失时回退 deny-by-default、隔离敏感资产并保留人工处置。

<!-- claim:SF-2026-ARXIV-2604-23141:start -->跨栈原型不能证明 unlearning 完整性、ACL 无绕过或真实设备上的端到端安全。<!-- claim:SF-2026-ARXIV-2604-23141:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-23141:end -->

<!-- review:SF-2026-ARXIV-2604-23172:start -->
#### Efficient VQ-QAT and Mixed Vector/Linear quantized Neural Networks

问题/机制与 owner：VQ-QAT 以 vector codebook 近似权重，并按层在 vector 与 linear quantizer 间选择。

Trade-off / failure：证据只覆盖作者模型、任务和量化配置，不能证明任意架构、kernel 或设备上都更快。

Fallback/coexistence：unsupported operator/accuracy slice 回退既有 scalar/group-wise quantization，保留混合格式而非强制全模型 VQ。

<!-- claim:SF-2026-ARXIV-2604-23172:start -->证据只覆盖作者模型、任务和量化配置，不能证明任意架构、kernel 或设备上都更快。<!-- claim:SF-2026-ARXIV-2604-23172:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-23172:end -->

<!-- review:SF-2026-ARXIV-2604-23205:start -->
#### Tessera: Secure, Near-Line-Rate Weight Streaming for UMA Edge Accelerators

问题/机制与 owner：UMA edge accelerator 在 64-byte AXI burst 上并行生成 AES-CTR keystream，只让 plaintext weight tile 短暂进入隔离 NPU SRAM。

Trade-off / failure：98.4% 带宽是 proxy hardware measurement 加 idealized model 的投影；未制造该 NPU silicon，且假设 trusted die/SMMU，不覆盖 invasive、side-channel 与 supply-chain 攻击。

Fallback/coexistence：不具备可信 die、IOMMU/SMMU 或 scrub 保证时，回退页级 memory encryption/受控 TEE carve-out，并把性能损失作为安全预算。

<!-- claim:SF-2026-ARXIV-2604-23205:start -->98.4% 带宽是 proxy hardware measurement 加 idealized model 的投影；未制造该 NPU silicon，且假设 trusted die/SMMU，不覆盖 invasive、side-channel 与 supply-chain 攻击。<!-- claim:SF-2026-ARXIV-2604-23205:end -->

Books Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2604-23205:end -->

<!-- review:SF-2026-ARXIV-2604-23272:start -->
#### Modular Sensory Stream for Integrating Physical Feedback in Vision-Language-Action Models

问题/机制与 owner：把物理 feedback 作为独立 sensory stream 进入 VLA，而不是只依赖一次性视觉观测。

Trade-off / failure：实验只说明所披露环境中的反馈收益，不证明传感器延迟、噪声或真实机器人故障下的安全闭环。

Fallback/coexistence：feedback stale/invalid 时回退 current observation 与低层 safety controller，并保留无反馈 policy 分支。

<!-- claim:SF-2026-ARXIV-2604-23272:start -->实验只说明所披露环境中的反馈收益，不证明传感器延迟、噪声或真实机器人故障下的安全闭环。<!-- claim:SF-2026-ARXIV-2604-23272:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-23272:end -->

<!-- review:SF-2026-ARXIV-2604-23483:start -->
#### Agentic Adversarial Rewriting Exposes Architectural Vulnerabilities in Black-Box NLP Pipelines

问题/机制与 owner：以黑盒 adversarial rewriting 连续穿过多阶段 NLP pipeline，暴露逐级语义放大。

Trade-off / failure：只用单一 misinformation dataset、point estimates 与同族 semantic judge，未做跨 pipeline 验证。

Fallback/coexistence：保留逐阶段 provenance 与独立 evaluator；异常时停在最后可信 stage 并走人工复核。

<!-- claim:SF-2026-ARXIV-2604-23483:start -->只用单一 misinformation dataset、point estimates 与同族 semantic judge，未做跨 pipeline 验证。<!-- claim:SF-2026-ARXIV-2604-23483:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-23483:end -->

<!-- review:SF-2026-ARXIV-2604-24790:start -->
#### Semantic Denial of Service in LLM-controlled robots

问题/机制与 owner：安全语义上合理的 1–5 token audio injection 可诱导 stop、acknowledgement loop 或 false alert，攻击目标是决策层 availability 而非恶意文本分类。

Trade-off / failure：只在 simulated tool-calling robot 上评估；prompt defenses 不等于 architecture defense，真实声学链路与生产机器人未验证。

Fallback/coexistence：跨模态指令在 commit 前做 source/intent/temporal consistency 验证；失败时隔离 audio control、要求人工确认或进入 safe-stop。

<!-- claim:SF-2026-ARXIV-2604-24790:start -->只在 simulated tool-calling robot 上评估；prompt defenses 不等于 architecture defense，真实声学链路与生产机器人未验证。<!-- claim:SF-2026-ARXIV-2604-24790:end -->

Books Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2604-24790:end -->

## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

没有跨 workload 外推的 benchmark claim；所有数值只属于 exact-v1 作者协议，未披露字段为 Not Disclosed。

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2604-23099 | score_7_9;forced_review | not_selected | — | — | Source Review 已完成；Top-3 预算优先给本日跨层 delta，未选不降低 Evidence 或 Books Decision。 | analysis-decision:SF-2026-ARXIV-2604-23099 |
| SF-2026-ARXIV-2604-23102 | score_7_9;forced_review | selected | DA-2604-23102 | — | exact-v1 显示跨层 state/control 或 evaluation-contract delta，且 current Books comparison 仍有长期机制增量。 | analysis:DA-2604-23102 |
| SF-2026-ARXIV-2604-23108 | score_7_9;forced_review | selected | DA-2604-23108 | — | exact-v1 显示跨层 state/control 或 evaluation-contract delta，且 current Books comparison 仍有长期机制增量。 | analysis:DA-2604-23108 |
| SF-2026-ARXIV-2604-23121 | score_7_9;forced_review | not_selected | — | — | Source Review 已完成；Top-3 预算优先给本日跨层 delta，未选不降低 Evidence 或 Books Decision。 | analysis-decision:SF-2026-ARXIV-2604-23121 |
| SF-2026-ARXIV-2604-23139 | score_7_9;forced_review | not_selected | — | — | Source Review 已完成；Top-3 预算优先给本日跨层 delta，未选不降低 Evidence 或 Books Decision。 | analysis-decision:SF-2026-ARXIV-2604-23139 |
| SF-2026-ARXIV-2604-23141 | score_7_9;forced_review | not_selected | — | — | Full Review/Books comparison 已完成；Top-3 预算不改变 Evidence 或 Books disposition。 | analysis-decision:SF-2026-ARXIV-2604-23141 |
| SF-2026-ARXIV-2604-23150 | score_7_9;forced_review | not_selected | — | — | Source Review 已完成；Top-3 预算优先给本日跨层 delta，未选不降低 Evidence 或 Books Decision。 | analysis-decision:SF-2026-ARXIV-2604-23150 |
| SF-2026-ARXIV-2604-23172 | score_7_9;forced_review | not_selected | — | — | Full Review/Books comparison 已完成；Top-3 预算不改变 Evidence 或 Books disposition。 | analysis-decision:SF-2026-ARXIV-2604-23172 |
| SF-2026-ARXIV-2604-23178 | score_7_9;forced_review | not_selected | — | — | Source Review 已完成；Top-3 预算优先给本日跨层 delta，未选不降低 Evidence 或 Books Decision。 | analysis-decision:SF-2026-ARXIV-2604-23178 |
| SF-2026-ARXIV-2604-23205 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Full Review/Books comparison 已完成；Top-3 预算不改变 Evidence 或 Books disposition。 | analysis-decision:SF-2026-ARXIV-2604-23205 |
| SF-2026-ARXIV-2604-23210 | score_7_9;forced_review | not_selected | — | — | Source Review 已完成；Top-3 预算优先给本日跨层 delta，未选不降低 Evidence 或 Books Decision。 | analysis-decision:SF-2026-ARXIV-2604-23210 |
| SF-2026-ARXIV-2604-23238 | score_7_9;forced_review | not_selected | — | — | Source Review 已完成；Top-3 预算优先给本日跨层 delta，未选不降低 Evidence 或 Books Decision。 | analysis-decision:SF-2026-ARXIV-2604-23238 |
| SF-2026-ARXIV-2604-23272 | score_7_9;forced_review | not_selected | — | — | Full Review/Books comparison 已完成；Top-3 预算不改变 Evidence 或 Books disposition。 | analysis-decision:SF-2026-ARXIV-2604-23272 |
| SF-2026-ARXIV-2604-23277 | score_7_9;forced_review | not_selected | — | — | Source Review 已完成；Top-3 预算优先给本日跨层 delta，未选不降低 Evidence 或 Books Decision。 | analysis-decision:SF-2026-ARXIV-2604-23277 |
| SF-2026-ARXIV-2604-23280 | score_7_9;forced_review | selected | DA-2604-23280 | — | exact-v1 显示跨层 state/control 或 evaluation-contract delta，且 current Books comparison 仍有长期机制增量。 | analysis:DA-2604-23280 |
| SF-2026-ARXIV-2604-23318 | score_7_9;forced_review | not_selected | — | — | Source Review 已完成；Top-3 预算优先给本日跨层 delta，未选不降低 Evidence 或 Books Decision。 | analysis-decision:SF-2026-ARXIV-2604-23318 |
| SF-2026-ARXIV-2604-23333 | score_7_9;forced_review | not_selected | — | — | Source Review 已完成；Top-3 预算优先给本日跨层 delta，未选不降低 Evidence 或 Books Decision。 | analysis-decision:SF-2026-ARXIV-2604-23333 |
| SF-2026-ARXIV-2604-23338 | score_7_9;forced_review | not_selected | — | — | Source Review 已完成；Top-3 预算优先给本日跨层 delta，未选不降低 Evidence 或 Books Decision。 | analysis-decision:SF-2026-ARXIV-2604-23338 |
| SF-2026-ARXIV-2604-23366 | score_7_9;forced_review | not_selected | — | — | Source Review 已完成；Top-3 预算优先给本日跨层 delta，未选不降低 Evidence 或 Books Decision。 | analysis-decision:SF-2026-ARXIV-2604-23366 |
| SF-2026-ARXIV-2604-23374 | score_7_9;forced_review | not_selected | — | — | Source Review 已完成；Top-3 预算优先给本日跨层 delta，未选不降低 Evidence 或 Books Decision。 | analysis-decision:SF-2026-ARXIV-2604-23374 |
| SF-2026-ARXIV-2604-23455 | score_7_9;forced_review | not_selected | — | — | Source Review 已完成；Top-3 预算优先给本日跨层 delta，未选不降低 Evidence 或 Books Decision。 | analysis-decision:SF-2026-ARXIV-2604-23455 |
| SF-2026-ARXIV-2604-23459 | score_7_9;forced_review | not_selected | — | — | Source Review 已完成；Top-3 预算优先给本日跨层 delta，未选不降低 Evidence 或 Books Decision。 | analysis-decision:SF-2026-ARXIV-2604-23459 |
| SF-2026-ARXIV-2604-23466 | score_7_9;forced_review | not_selected | — | — | Source Review 已完成；Top-3 预算优先给本日跨层 delta，未选不降低 Evidence 或 Books Decision。 | analysis-decision:SF-2026-ARXIV-2604-23466 |
| SF-2026-ARXIV-2604-23467 | score_7_9;forced_review | not_selected | — | — | Source Review 已完成；Top-3 预算优先给本日跨层 delta，未选不降低 Evidence 或 Books Decision。 | analysis-decision:SF-2026-ARXIV-2604-23467 |
| SF-2026-ARXIV-2604-23478 | score_7_9;forced_review | not_selected | — | — | Source Review 已完成；Top-3 预算优先给本日跨层 delta，未选不降低 Evidence 或 Books Decision。 | analysis-decision:SF-2026-ARXIV-2604-23478 |
| SF-2026-ARXIV-2604-23483 | score_7_9;forced_review | not_selected | — | — | Full Review/Books comparison 已完成；Top-3 预算不改变 Evidence 或 Books disposition。 | analysis-decision:SF-2026-ARXIV-2604-23483 |
| SF-2026-ARXIV-2604-24790 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Full Review/Books comparison 已完成；Top-3 预算不改变 Evidence 或 Books disposition。 | analysis-decision:SF-2026-ARXIV-2604-24790 |

<!-- analysis-decision:SF-2026-ARXIV-2604-23099:start -->本 family 已完成 exact-v1、Score 与 Books comparison；未选入 Top-3 仅是叙事预算决定。<!-- analysis-decision:SF-2026-ARXIV-2604-23099:end -->
<!-- analysis:DA-2604-23102:start -->
### Unstable Rankings in Bayesian Deep Learning Evaluation

旧路径与约束：旧路径把 `Unstable Rankings in Bayesian Deep Learning Evaluation` 的判断留给固定策略、单次离线分数或未显式版本化的运行状态。

机制与控制权：Standard evaluations of Bayesian deep learning methods assume that metric estimates are reliable, but we show this assumption fails under data scarcity. Method rankings are not only unreliable at small $n$, but also dataset-dependent in ways that point estimates cannot reveal: the same method comparison yields $P(\mathrm{MCD} \prec \mathrm{Ensemble}) = 1.000$ at $n = 50$ on one dataset and remains below $0.95$ even at $n = 500$ on another. Across the datasets we consider, no universal sample size threshold exists, which is precisely why dataset-specific posterior inference is necessary. 该机制将长期 owner 定位到 `PLATFORM-EVALUATION-SYSTEM`，并把相应 state/control/evidence identity 从隐式约定变成可检查对象。

收益、代价与边界：论文只在 exact-v1 披露的任务、模型与实验协议内支持上述结论；`Unstable Rankings in Bayesian Deep Learning Evaluation` 不证明跨模型、跨硬件、跨数据分布或生产 SLO 的普遍收益。失配时回退 current Books 的既有路径，并保留新旧机制并存。 只接受 arXiv:2604.23102v1 的作者机制与实验；未披露硬件、precision、长度、batch、并发、成本或线上 SLO 均为 Not Disclosed。
<!-- analysis:DA-2604-23102:end -->
<!-- analysis:DA-2604-23108:start -->
### Mixture of Heterogeneous Grouped Experts for Language Modeling

旧路径与约束：旧路径未显式拥有 `MODEL-MOE` 中该 family 的受限状态。

机制与控制权：router 拥有 expert assignment，runtime 拥有 capacity/communication，expert 只处理已路由 token

收益、代价与边界：exact-v1 披露的反例/限制是：In this work, we propose MoHGE architecture that introduces group-wise expert size variation to better accommodate the diverse complexity of token predictions. We further design a novel routing mechanism and GPU allocation strategy, combining a new training objective, to guarantee excellent performance, efficient parameter utilization, balanced GPU utilization and better scalability. With approximately 20% fewer parameters, MoHGE achieves comparable or slightly better performance than standard MoE baselines, and outperforms recent heterogeneous MoE models on most benchmark datasets.…。因此若该限制在目标 workload 中触发，不能把 `Mixture of Heterogeneous Grouped Experts for Language Modeling` 的作者结果外推为生产正确性或 SLO 保证。 仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- analysis:DA-2604-23108:end -->
<!-- analysis-decision:SF-2026-ARXIV-2604-23121:start -->本 family 已完成 exact-v1、Score 与 Books comparison；未选入 Top-3 仅是叙事预算决定。<!-- analysis-decision:SF-2026-ARXIV-2604-23121:end -->
<!-- analysis-decision:SF-2026-ARXIV-2604-23139:start -->本 family 已完成 exact-v1、Score 与 Books comparison；未选入 Top-3 仅是叙事预算决定。<!-- analysis-decision:SF-2026-ARXIV-2604-23139:end -->
<!-- analysis-decision:SF-2026-ARXIV-2604-23150:start -->本 family 已完成 exact-v1、Score 与 Books comparison；未选入 Top-3 仅是叙事预算决定。<!-- analysis-decision:SF-2026-ARXIV-2604-23150:end -->
<!-- analysis-decision:SF-2026-ARXIV-2604-23178:start -->本 family 已完成 exact-v1、Score 与 Books comparison；未选入 Top-3 仅是叙事预算决定。<!-- analysis-decision:SF-2026-ARXIV-2604-23178:end -->
<!-- analysis-decision:SF-2026-ARXIV-2604-23210:start -->本 family 已完成 exact-v1、Score 与 Books comparison；未选入 Top-3 仅是叙事预算决定。<!-- analysis-decision:SF-2026-ARXIV-2604-23210:end -->
<!-- analysis-decision:SF-2026-ARXIV-2604-23238:start -->本 family 已完成 exact-v1、Score 与 Books comparison；未选入 Top-3 仅是叙事预算决定。<!-- analysis-decision:SF-2026-ARXIV-2604-23238:end -->
<!-- analysis-decision:SF-2026-ARXIV-2604-23277:start -->本 family 已完成 exact-v1、Score 与 Books comparison；未选入 Top-3 仅是叙事预算决定。<!-- analysis-decision:SF-2026-ARXIV-2604-23277:end -->
<!-- analysis:DA-2604-23280:start -->
### AI Identity: Standards, Gaps, and Research Directions for AI Agents

旧路径与约束：旧路径把 `AI Identity: Standards, Gaps, and Research Directions for AI Agents` 的判断留给固定策略、单次离线分数或未显式版本化的运行状态。

机制与控制权：AI agents are now running real transactions, workflows, and sub-agent chains across organizational boundaries without continuous human supervision. This creates a problem no current infrastructure is equipped to solve: how do you identify, verify, and hold accountable an entity with no body, no persistent memory, and no legal standing? We define AI Identity as the continuous relationship between what an AI agent is declared to be and what it is observed to do, bounded by the confidence that those two things correspond at any given moment. 该机制将长期 owner 定位到 `AGENT-PLATFORM`，并把相应 state/control/evidence identity 从隐式约定变成可检查对象。

收益、代价与边界：论文只在 exact-v1 披露的任务、模型与实验协议内支持上述结论；`AI Identity: Standards, Gaps, and Research Directions for AI Agents` 不证明跨模型、跨硬件、跨数据分布或生产 SLO 的普遍收益。失配时回退 current Books 的既有路径，并保留新旧机制并存。 只接受 arXiv:2604.23280v1 的作者机制与实验；未披露硬件、precision、长度、batch、并发、成本或线上 SLO 均为 Not Disclosed。
<!-- analysis:DA-2604-23280:end -->
<!-- analysis-decision:SF-2026-ARXIV-2604-23318:start -->本 family 已完成 exact-v1、Score 与 Books comparison；未选入 Top-3 仅是叙事预算决定。<!-- analysis-decision:SF-2026-ARXIV-2604-23318:end -->
<!-- analysis-decision:SF-2026-ARXIV-2604-23333:start -->本 family 已完成 exact-v1、Score 与 Books comparison；未选入 Top-3 仅是叙事预算决定。<!-- analysis-decision:SF-2026-ARXIV-2604-23333:end -->
<!-- analysis-decision:SF-2026-ARXIV-2604-23338:start -->本 family 已完成 exact-v1、Score 与 Books comparison；未选入 Top-3 仅是叙事预算决定。<!-- analysis-decision:SF-2026-ARXIV-2604-23338:end -->
<!-- analysis-decision:SF-2026-ARXIV-2604-23366:start -->本 family 已完成 exact-v1、Score 与 Books comparison；未选入 Top-3 仅是叙事预算决定。<!-- analysis-decision:SF-2026-ARXIV-2604-23366:end -->
<!-- analysis-decision:SF-2026-ARXIV-2604-23374:start -->本 family 已完成 exact-v1、Score 与 Books comparison；未选入 Top-3 仅是叙事预算决定。<!-- analysis-decision:SF-2026-ARXIV-2604-23374:end -->
<!-- analysis-decision:SF-2026-ARXIV-2604-23455:start -->本 family 已完成 exact-v1、Score 与 Books comparison；未选入 Top-3 仅是叙事预算决定。<!-- analysis-decision:SF-2026-ARXIV-2604-23455:end -->
<!-- analysis-decision:SF-2026-ARXIV-2604-23459:start -->本 family 已完成 exact-v1、Score 与 Books comparison；未选入 Top-3 仅是叙事预算决定。<!-- analysis-decision:SF-2026-ARXIV-2604-23459:end -->
<!-- analysis-decision:SF-2026-ARXIV-2604-23466:start -->本 family 已完成 exact-v1、Score 与 Books comparison；未选入 Top-3 仅是叙事预算决定。<!-- analysis-decision:SF-2026-ARXIV-2604-23466:end -->
<!-- analysis-decision:SF-2026-ARXIV-2604-23467:start -->本 family 已完成 exact-v1、Score 与 Books comparison；未选入 Top-3 仅是叙事预算决定。<!-- analysis-decision:SF-2026-ARXIV-2604-23467:end -->
<!-- analysis-decision:SF-2026-ARXIV-2604-23478:start -->本 family 已完成 exact-v1、Score 与 Books comparison；未选入 Top-3 仅是叙事预算决定。<!-- analysis-decision:SF-2026-ARXIV-2604-23478:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2604-23099 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L78-从目标到证据-而不是从指标到目标 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L18-为什么-ai-cluster-需要更强的-queue-模型; books/part-06-ai-infrastructure/67-monitoring.md#L18-先定义目标-再选择可测信号 | existing:SF-2026-ARXIV-2604-23099 | delta:SF-2026-ARXIV-2604-23099 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23099 |
| SF-2026-ARXIV-2604-23102 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L78-从目标到证据-而不是从指标到目标 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L18-为什么-ai-cluster-需要更强的-queue-模型; books/part-06-ai-infrastructure/67-monitoring.md#L18-先定义目标-再选择可测信号 | existing:SF-2026-ARXIV-2604-23102 | delta:SF-2026-ARXIV-2604-23102 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23102 |
| SF-2026-ARXIV-2604-23108 | MODEL-MOE | books/part-02-model/21-moe.md#L20-从-dense-mlp-的绑定关系开始 | books/part-02-model/20-sampling.md#L18-logits-还不是概率; books/part-02-model/22-long-context.md#L20-先拆开四种能力 | existing:SF-2026-ARXIV-2604-23108 | delta:SF-2026-ARXIV-2604-23108 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23108 |
| SF-2026-ARXIV-2604-23121 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L177-state-ownership-与-freshness | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L16-从三个容易混淆的对象开始; books/part-04-training-system/27-data.md#L18-part-iv-的能力生产链 | existing:SF-2026-ARXIV-2604-23121 | delta:SF-2026-ARXIV-2604-23121 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23121 |
| SF-2026-ARXIV-2604-23139 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#L641-failure-不再是单进程退出 | books/part-04-training-system/35-checkpoint.md#L18-为什么只保存-weights-不够; books/part-04-training-system/37-tensor-parallel.md#L18-为什么-把权重文件切开-不够 | existing:SF-2026-ARXIV-2604-23139 | delta:SF-2026-ARXIV-2604-23139 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23139 |
| SF-2026-ARXIV-2604-23141 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L16-从资产与信任边界开始 | books/part-06-ai-infrastructure/71-multi-tenant.md#L16-先定义-tenant-与信任级别; books/part-06-ai-infrastructure/73-production-best-practice.md#L16-poc-隐含了哪些假设 | existing:SF-2026-ARXIV-2604-23141 | delta:SF-2026-ARXIV-2604-23141 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23141 |
| SF-2026-ARXIV-2604-23150 | MODEL-MOE | books/part-02-model/21-moe.md#L20-从-dense-mlp-的绑定关系开始 | books/part-02-model/20-sampling.md#L18-logits-还不是概率; books/part-02-model/22-long-context.md#L20-先拆开四种能力 | existing:SF-2026-ARXIV-2604-23150 | delta:SF-2026-ARXIV-2604-23150 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23150 |
| SF-2026-ARXIV-2604-23172 | MODEL-FFN | books/part-02-model/16-feed-forward-mlp.md#L18-只有-attention-会缺少什么 | books/part-02-model/15-multi-head-attention.md#L18-单个-head-的表达瓶颈; books/part-02-model/17-transformer-layer.md#L18-直接串联为什么难以堆深 | existing:SF-2026-ARXIV-2604-23172 | delta:SF-2026-ARXIV-2604-23172 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23172 |
| SF-2026-ARXIV-2604-23178 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L78-从目标到证据-而不是从指标到目标 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L18-为什么-ai-cluster-需要更强的-queue-模型; books/part-06-ai-infrastructure/67-monitoring.md#L18-先定义目标-再选择可测信号 | existing:SF-2026-ARXIV-2604-23178 | delta:SF-2026-ARXIV-2604-23178 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23178 |
| SF-2026-ARXIV-2604-23205 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L16-从资产与信任边界开始 | books/part-06-ai-infrastructure/71-multi-tenant.md#L16-先定义-tenant-与信任级别; books/part-06-ai-infrastructure/73-production-best-practice.md#L16-poc-隐含了哪些假设 | existing:SF-2026-ARXIV-2604-23205 | delta:SF-2026-ARXIV-2604-23205 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2604-23205 |
| SF-2026-ARXIV-2604-23210 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L16-从资产与信任边界开始 | books/part-06-ai-infrastructure/71-multi-tenant.md#L16-先定义-tenant-与信任级别; books/part-06-ai-infrastructure/73-production-best-practice.md#L16-poc-隐含了哪些假设 | existing:SF-2026-ARXIV-2604-23210 | delta:SF-2026-ARXIV-2604-23210 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23210 |
| SF-2026-ARXIV-2604-23238 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L16-从资产与信任边界开始 | books/part-06-ai-infrastructure/71-multi-tenant.md#L16-先定义-tenant-与信任级别; books/part-06-ai-infrastructure/73-production-best-practice.md#L16-poc-隐含了哪些假设 | existing:SF-2026-ARXIV-2604-23238 | delta:SF-2026-ARXIV-2604-23238 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23238 |
| SF-2026-ARXIV-2604-23272 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L177-state-ownership-与-freshness | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L16-从三个容易混淆的对象开始 | existing:SF-2026-ARXIV-2604-23272 | delta:SF-2026-ARXIV-2604-23272 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23272 |
| SF-2026-ARXIV-2604-23277 | AGENT-CONTEXT | books/part-07-agent/75-context.md#L326-context-中的信任冲突 | books/part-07-agent/74-prompt.md#L16-prompt-改变的是条件-不是参数; books/part-07-agent/76-rag.md#L16-参数化知识的边界 | existing:SF-2026-ARXIV-2604-23277 | delta:SF-2026-ARXIV-2604-23277 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23277 |
| SF-2026-ARXIV-2604-23280 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#L413-agent-runtime-state-machine | books/part-07-agent/83-mcp.md#L19-为什么需要协议层 | existing:SF-2026-ARXIV-2604-23280 | delta:SF-2026-ARXIV-2604-23280 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23280 |
| SF-2026-ARXIV-2604-23318 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#L167-sequence-reward-怎样作用到-tokens | books/part-04-training-system/32-ppo.md#L18-把语言生成写成策略过程; books/part-04-training-system/34-dpo.md#L18-从-rlhf-的两阶段复杂度开始 | existing:SF-2026-ARXIV-2604-23318 | delta:SF-2026-ARXIV-2604-23318 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23318 |
| SF-2026-ARXIV-2604-23333 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#L167-sequence-reward-怎样作用到-tokens | books/part-04-training-system/32-ppo.md#L18-把语言生成写成策略过程; books/part-04-training-system/34-dpo.md#L18-从-rlhf-的两阶段复杂度开始 | existing:SF-2026-ARXIV-2604-23333 | delta:SF-2026-ARXIV-2604-23333 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23333 |
| SF-2026-ARXIV-2604-23338 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L16-从资产与信任边界开始 | books/part-06-ai-infrastructure/71-multi-tenant.md#L16-先定义-tenant-与信任级别; books/part-06-ai-infrastructure/73-production-best-practice.md#L16-poc-隐含了哪些假设 | existing:SF-2026-ARXIV-2604-23338 | delta:SF-2026-ARXIV-2604-23338 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23338 |
| SF-2026-ARXIV-2604-23366 | AGENT-RAG | books/part-07-agent/76-rag.md#L420-rag-不消除-hallucination | books/part-07-agent/75-context.md#L16-context-是一次调用的可见状态; books/part-07-agent/77-memory.md#L20-context-与-memory-的状态边界 | existing:SF-2026-ARXIV-2604-23366 | delta:SF-2026-ARXIV-2604-23366 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23366 |
| SF-2026-ARXIV-2604-23374 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L16-从资产与信任边界开始 | books/part-06-ai-infrastructure/71-multi-tenant.md#L16-先定义-tenant-与信任级别; books/part-06-ai-infrastructure/73-production-best-practice.md#L16-poc-隐含了哪些假设 | existing:SF-2026-ARXIV-2604-23374 | delta:SF-2026-ARXIV-2604-23374 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23374 |
| SF-2026-ARXIV-2604-23455 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L78-从目标到证据-而不是从指标到目标 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L18-为什么-ai-cluster-需要更强的-queue-模型; books/part-06-ai-infrastructure/67-monitoring.md#L18-先定义目标-再选择可测信号 | existing:SF-2026-ARXIV-2604-23455 | delta:SF-2026-ARXIV-2604-23455 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23455 |
| SF-2026-ARXIV-2604-23459 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L16-从资产与信任边界开始 | books/part-06-ai-infrastructure/71-multi-tenant.md#L16-先定义-tenant-与信任级别; books/part-06-ai-infrastructure/73-production-best-practice.md#L16-poc-隐含了哪些假设 | existing:SF-2026-ARXIV-2604-23459 | delta:SF-2026-ARXIV-2604-23459 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23459 |
| SF-2026-ARXIV-2604-23466 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#L18-从计算图开始 | books/part-05-inference-system/48-speculative-decoding.md#L18-从-decode-串行瓶颈开始; books/part-05-inference-system/50-vllm.md#L18-serving-引擎不是模型-loader | existing:SF-2026-ARXIV-2604-23466 | delta:SF-2026-ARXIV-2604-23466 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23466 |
| SF-2026-ARXIV-2604-23467 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#L18-从计算图开始 | books/part-05-inference-system/48-speculative-decoding.md#L18-从-decode-串行瓶颈开始; books/part-05-inference-system/50-vllm.md#L18-serving-引擎不是模型-loader | existing:SF-2026-ARXIV-2604-23467 | delta:SF-2026-ARXIV-2604-23467 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23467 |
| SF-2026-ARXIV-2604-23478 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L78-从目标到证据-而不是从指标到目标 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L18-为什么-ai-cluster-需要更强的-queue-模型; books/part-06-ai-infrastructure/67-monitoring.md#L18-先定义目标-再选择可测信号 | existing:SF-2026-ARXIV-2604-23478 | delta:SF-2026-ARXIV-2604-23478 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23478 |
| SF-2026-ARXIV-2604-23483 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L16-从资产与信任边界开始 | books/part-06-ai-infrastructure/71-multi-tenant.md#L16-先定义-tenant-与信任级别; books/part-06-ai-infrastructure/73-production-best-practice.md#L16-poc-隐含了哪些假设 | existing:SF-2026-ARXIV-2604-23483 | delta:SF-2026-ARXIV-2604-23483 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23483 |
| SF-2026-ARXIV-2604-24790 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L16-从资产与信任边界开始 | books/part-06-ai-infrastructure/71-multi-tenant.md#L16-先定义-tenant-与信任级别; books/part-06-ai-infrastructure/73-production-best-practice.md#L16-poc-隐含了哪些假设 | existing:SF-2026-ARXIV-2604-24790 | delta:SF-2026-ARXIV-2604-24790 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2604-24790 |

<!-- books-review:SF-2026-ARXIV-2604-23099:start -->
<!-- existing:SF-2026-ARXIV-2604-23099:start -->真实 owner `books/part-06-ai-infrastructure/66-evaluation-system.md#L78-从目标到证据而不是从指标到目标` 正文：## 从目标到证据，而不是从指标到目标 Evaluation 的起点不是“平台能采集什么 metric”，而是系统希望满足什么目标。可以把链路写成： ```text intended use and risk → evaluation specification → dataset / environment → system execution → scorer / human judgment → aggregation and uncertainty → decision policy → release / rollback / investigation → production feedback ``` `intended use` 决定什么错误重要。例如代码补全、医疗问答和广告生成都可以计算文本相似度，但相同指标不代表相同风险。评估 specification 至少应声明： ```text EvalSpec = target behavior + eligible population + failure taxonomy + metrics and scorers + slice definitions + thresholds / comparison rules + uncertainty requirement + owner and review policy ``` 如果目标没有被写清楚，团队往往会优化最容易计算的 proxy。模型变得更会迎合 judge，却未必更可靠；服务提高吞吐，却可能让 tail latency 和任务完成率下降。这不是模型“作弊”，而是控制系统给出了错误目标。；相邻章 `books/part-06-ai-infrastructure/65-kai-scheduler.md#L18-为什么-ai-cluster-需要更强的-queue-模型; books/part-06-ai-infrastructure/67-monitoring.md#L18-先定义目标再选择可测信号` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=ba07952c1fe646f17bfd554f905fb4a594aaa8676cc3e8aea0edfa2526800e09。<!-- existing:SF-2026-ARXIV-2604-23099:end -->
<!-- delta:SF-2026-ARXIV-2604-23099:start -->EvalSpec owner 冻结 subject/data/scorer，release owner 依据 run evidence 作决定<!-- delta:SF-2026-ARXIV-2604-23099:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-23099:end -->
<!-- books-review:SF-2026-ARXIV-2604-23102:start -->
<!-- existing:SF-2026-ARXIV-2604-23102:start -->真实 owner `books/part-06-ai-infrastructure/66-evaluation-system.md#L78-从目标到证据而不是从指标到目标` 正文：## 从目标到证据，而不是从指标到目标 Evaluation 的起点不是“平台能采集什么 metric”，而是系统希望满足什么目标。可以把链路写成： ```text intended use and risk → evaluation specification → dataset / environment → system execution → scorer / human judgment → aggregation and uncertainty → decision policy → release / rollback / investigation → production feedback ``` `intended use` 决定什么错误重要。例如代码补全、医疗问答和广告生成都可以计算文本相似度，但相同指标不代表相同风险。评估 specification 至少应声明： ```text EvalSpec = target behavior + eligible population + failure taxonomy + metrics and scorers + slice definitions + thresholds / comparison rules + uncertainty requirement + owner and review policy ``` 如果目标没有被写清楚，团队往往会优化最容易计算的 proxy。模型变得更会迎合 judge，却未必更可靠；服务提高吞吐，却可能让 tail latency 和任务完成率下降。这不是模型“作弊”，而是控制系统给出了错误目标。；相邻章 `books/part-06-ai-infrastructure/65-kai-scheduler.md#L18-为什么-ai-cluster-需要更强的-queue-模型; books/part-06-ai-infrastructure/67-monitoring.md#L18-先定义目标再选择可测信号` 已顺读。该主线尚未完整承载本 family 特有机制、failure 与 evidence boundary。 owner_sha256=ba07952c1fe646f17bfd554f905fb4a594aaa8676cc3e8aea0edfa2526800e09。<!-- existing:SF-2026-ARXIV-2604-23102:end -->
<!-- delta:SF-2026-ARXIV-2604-23102:start -->Standard evaluations of Bayesian deep learning methods assume that metric estimates are reliable, but we show this assumption fails under data scarcity. Method rankings are not only unreliable at small $n$, but also dataset-dependent in ways that point estimates cannot reveal: the same method comparison yields $P(\mathrm{MCD} \prec \mathrm{Ensemble}) = 1.000$ at $n = 50$ on one dataset and remains below $0.95$ even at $n = 500$ on another. Across the datasets we consider, no universal sample size threshold exists, which is precisely why dataset-specific posterior inference is necessary. 该机制将长期 owner 定位到 `PLATFORM-EVALUATION-SYSTEM`，并把相应 state/control/evidence identity 从隐式约定变成可检查对象。<!-- delta:SF-2026-ARXIV-2604-23102:end --> Decision=`Integrate`；evidence boundary：只接受 arXiv:2604.23102v1 的作者机制与实验；未披露硬件、precision、长度、batch、并发、成本或线上 SLO 均为 Not Disclosed。
<!-- books-review:SF-2026-ARXIV-2604-23102:end -->
<!-- books-review:SF-2026-ARXIV-2604-23108:start -->
<!-- existing:SF-2026-ARXIV-2604-23108:start -->真实 owner `books/part-02-model/21-moe.md#L20-从-dense-mlp-的绑定关系开始` 正文：## 从 Dense MLP 的绑定关系开始 第16章的 Dense MLP 对所有 token 使用同一组参数： ```text x -> W_up -> activation/gate -> W_down -> y ``` 若把 `d_ff` 扩大，总参数与每 token FLOPs 同时上升。模型容量和执行成本被绑定。 一种朴素方案是准备多个不同 MLP，但让每个 token 仍执行全部 experts 后再平均。这增加了容量，却没有减少 active compute。 MoE 增加一个 Router，每个 token 只进入 top-`k` experts： ```text token state -> router -> selected expert MLPs -> weighted combination ```；相邻章 `books/part-02-model/20-sampling.md#L18-logits-还不是概率; books/part-02-model/22-long-context.md#L20-先拆开四种能力` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=8cce04454dfdbc25cb405aa40c73947fd9ab0265e5d53d64c2b1f4ef5b3abd78。<!-- existing:SF-2026-ARXIV-2604-23108:end -->
<!-- delta:SF-2026-ARXIV-2604-23108:start -->router 拥有 expert assignment，runtime 拥有 capacity/communication，expert 只处理已路由 token<!-- delta:SF-2026-ARXIV-2604-23108:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-23108:end -->
<!-- books-review:SF-2026-ARXIV-2604-23121:start -->
<!-- existing:SF-2026-ARXIV-2604-23121:start -->真实 owner `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L177-state-ownership-与-freshness` 正文：## State ownership 与 freshness - sensor pipeline 拥有 timestamped observations； - state estimator 拥有当前 calibrated belief； - VLA/world-action model 拥有 provisional proposal； - controller 拥有 action execution lease； - safety monitor 拥有 veto / emergency stop； - environment 拥有真实 outcome； - run log 拥有 observation-action-effect evidence。 ### Policy 内部的 Latent Memory 是 Episode State，不是 Agent Memory 单帧或短 action chunk 足以处理局部连续动作，却无法长期保留遮挡物体、阶段进度和失败上下文。一个受限分支在 policy 内维护快慢两级 latent：短期 state 跟随近期 observation，curator 只把通过 admission 的片段提升到长期 state，并在读取后压缩或替换。 ```text timestamped observation + short latent → policy update and action proposal → curator admission / retrieval / condensation → episode-scoped long latent → controller validation and fresh observation reconciliation ``` 这类 memory 仍是 model-owned、episode-scoped derived state：identity 必须绑定 policy revision、embodiment、episode、 reset boundary、observat；相邻章 `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L16-从三个容易混淆的对象开始; books/part-04-training-system/27-data.md#L18-part-iv-的能力生产链` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=eb033b201edf92216070f88c082e72493073a9633bbe23a6a821e0e2fba02942。<!-- existing:SF-2026-ARXIV-2604-23121:end -->
<!-- delta:SF-2026-ARXIV-2604-23121:start -->policy 拥有 action proposal，environment/human safety layer 拥有 observation truth 与 actuation commit<!-- delta:SF-2026-ARXIV-2604-23121:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-23121:end -->
<!-- books-review:SF-2026-ARXIV-2604-23139:start -->
<!-- existing:SF-2026-ARXIV-2604-23139:start -->真实 owner `books/part-04-training-system/36-distributed-training.md#L641-failure-不再是单进程退出` 正文：## Failure 不再是单进程退出 一个 rank crash 可能让其他 ranks 阻塞在 collective。训练平台需要： - Detect failed/stuck ranks。 - 终止或重建整个 process group。 - 选择 committed checkpoint。 - 恢复相同或新 world size。 - 保持 data cursor 与 job identity。 Elastic membership 对纯 DP 相对容易；TP/PP/EP layout 改变通常需要 reshard 或重建模型。第 35 章的 checkpoint correctness 是分布式容错的前提。 通信错误也不一定只能采用“任意 packet loss 都重传”的单一合同。可靠传输在 loss 罕见、梯度语义要求精确时最清楚；同步训练的 microburst 若触发成批重传，tail latency 会被最慢 flow 放大。一条实验性分支让 transport 按训练 phase 和已验证 tolerance 接受**有界 loss**：model/training owner 先证明该 phase、tensor class 与 loss budget 下的收敛影响，transport 再用 round identity、packet bitmap 和上限强制执行，超过预算立即回退可靠路径或重试整轮。 ```text phase + tensor/round identity + admitted loss budget → burst-aware transport → packet bitmap and bounded completion → optimizer step or reliable retransmit fallback ``` 这里“模型能容忍”不能由网络层自行推断，单个 workload 的经验阈值也不能写成通用 40%。该机制以更复杂的收敛证据、bitmap state 和 silent-corruption 风险换较短 ；相邻章 `books/part-04-training-system/35-checkpoint.md#L18-为什么只保存-weights-不够; books/part-04-training-system/37-tensor-parallel.md#L18-为什么把权重文件切开不够` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=35cb2eb9f2e0eff9dac03ee4db2cf2530c5f89ba9a7b8c92671958adf7b8df8e。<!-- existing:SF-2026-ARXIV-2604-23139:end -->
<!-- delta:SF-2026-ARXIV-2604-23139:start -->Distributed GNN training is dominated by remote feature fetching, which can be very costly. Multi-hop neighborhood sampling crosses partition boundaries and triggers fine-grained RPCs whose fixed initiation cost and GPU-stall latency waste energy. Prior systems try to reduce this overhead with presampling and static caching, but cache policies cannot react to runtime network variation. 该机制将长期 owner 定位到 `TRAIN-DISTRIBUTED-TRAINING`，并把相应 state/control/evidence identity 从隐式约定变成可检查对象。<!-- delta:SF-2026-ARXIV-2604-23139:end --> Decision=`No Change — Existing Coverage`；evidence boundary：只接受 arXiv:2604.23139v1 的作者机制与实验；未披露硬件、precision、长度、batch、并发、成本或线上 SLO 均为 Not Disclosed。
<!-- books-review:SF-2026-ARXIV-2604-23139:end -->
<!-- books-review:SF-2026-ARXIV-2604-23150:start -->
<!-- existing:SF-2026-ARXIV-2604-23150:start -->真实 owner `books/part-02-model/21-moe.md#L20-从-dense-mlp-的绑定关系开始` 正文：## 从 Dense MLP 的绑定关系开始 第16章的 Dense MLP 对所有 token 使用同一组参数： ```text x -> W_up -> activation/gate -> W_down -> y ``` 若把 `d_ff` 扩大，总参数与每 token FLOPs 同时上升。模型容量和执行成本被绑定。 一种朴素方案是准备多个不同 MLP，但让每个 token 仍执行全部 experts 后再平均。这增加了容量，却没有减少 active compute。 MoE 增加一个 Router，每个 token 只进入 top-`k` experts： ```text token state -> router -> selected expert MLPs -> weighted combination ```；相邻章 `books/part-02-model/20-sampling.md#L18-logits-还不是概率; books/part-02-model/22-long-context.md#L20-先拆开四种能力` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=8cce04454dfdbc25cb405aa40c73947fd9ab0265e5d53d64c2b1f4ef5b3abd78。<!-- existing:SF-2026-ARXIV-2604-23150:end -->
<!-- delta:SF-2026-ARXIV-2604-23150:start -->router 拥有 expert assignment，runtime 拥有 capacity/communication，expert 只处理已路由 token<!-- delta:SF-2026-ARXIV-2604-23150:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-23150:end -->
<!-- books-review:SF-2026-ARXIV-2604-23178:start -->
<!-- existing:SF-2026-ARXIV-2604-23178:start -->真实 owner `books/part-06-ai-infrastructure/66-evaluation-system.md#L78-从目标到证据而不是从指标到目标` 正文：## 从目标到证据，而不是从指标到目标 Evaluation 的起点不是“平台能采集什么 metric”，而是系统希望满足什么目标。可以把链路写成： ```text intended use and risk → evaluation specification → dataset / environment → system execution → scorer / human judgment → aggregation and uncertainty → decision policy → release / rollback / investigation → production feedback ``` `intended use` 决定什么错误重要。例如代码补全、医疗问答和广告生成都可以计算文本相似度，但相同指标不代表相同风险。评估 specification 至少应声明： ```text EvalSpec = target behavior + eligible population + failure taxonomy + metrics and scorers + slice definitions + thresholds / comparison rules + uncertainty requirement + owner and review policy ``` 如果目标没有被写清楚，团队往往会优化最容易计算的 proxy。模型变得更会迎合 judge，却未必更可靠；服务提高吞吐，却可能让 tail latency 和任务完成率下降。这不是模型“作弊”，而是控制系统给出了错误目标。；相邻章 `books/part-06-ai-infrastructure/65-kai-scheduler.md#L18-为什么-ai-cluster-需要更强的-queue-模型; books/part-06-ai-infrastructure/67-monitoring.md#L18-先定义目标再选择可测信号` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=ba07952c1fe646f17bfd554f905fb4a594aaa8676cc3e8aea0edfa2526800e09。<!-- existing:SF-2026-ARXIV-2604-23178:end -->
<!-- delta:SF-2026-ARXIV-2604-23178:start -->EvalSpec owner 冻结 subject/data/scorer，release owner 依据 run evidence 作决定<!-- delta:SF-2026-ARXIV-2604-23178:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-23178:end -->
<!-- books-review:SF-2026-ARXIV-2604-23210:start -->
<!-- existing:SF-2026-ARXIV-2604-23210:start -->真实 owner `books/part-06-ai-infrastructure/72-security.md#L16-从资产与信任边界开始` 正文：## 从资产与信任边界开始 需要保护的资产包括： - source data、labels 与 user context； - code、images、dependencies 与 credentials； - checkpoints、adapters、tokenizers 与 prompts； - registry metadata、evaluation 与 approvals； - GPU nodes、runtime memory 与 KV Cache； - APIs、tools、business systems 与 audit evidence。 主体包括用户、service accounts、controllers、training code、model server、model output 和 external tools。模型生成的文本不是可信主体，也不应自动获得调用者全部权限。；相邻章 `books/part-06-ai-infrastructure/71-multi-tenant.md#L16-先定义-tenant-与信任级别; books/part-06-ai-infrastructure/73-production-best-practice.md#L16-poc-隐含了哪些假设` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=cd99007e2f9b12ccf2bc7cd075bbf73c3b935255bf06bda7068b8f624de239ca。<!-- existing:SF-2026-ARXIV-2604-23210:end -->
<!-- delta:SF-2026-ARXIV-2604-23210:start -->policy/CI/sandbox 拥有 invariant 与 commit authority，model 仅提出不可信 proposal<!-- delta:SF-2026-ARXIV-2604-23210:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-23210:end -->
<!-- books-review:SF-2026-ARXIV-2604-23238:start -->
<!-- existing:SF-2026-ARXIV-2604-23238:start -->真实 owner `books/part-06-ai-infrastructure/72-security.md#L16-从资产与信任边界开始` 正文：## 从资产与信任边界开始 需要保护的资产包括： - source data、labels 与 user context； - code、images、dependencies 与 credentials； - checkpoints、adapters、tokenizers 与 prompts； - registry metadata、evaluation 与 approvals； - GPU nodes、runtime memory 与 KV Cache； - APIs、tools、business systems 与 audit evidence。 主体包括用户、service accounts、controllers、training code、model server、model output 和 external tools。模型生成的文本不是可信主体，也不应自动获得调用者全部权限。；相邻章 `books/part-06-ai-infrastructure/71-multi-tenant.md#L16-先定义-tenant-与信任级别; books/part-06-ai-infrastructure/73-production-best-practice.md#L16-poc-隐含了哪些假设` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=cd99007e2f9b12ccf2bc7cd075bbf73c3b935255bf06bda7068b8f624de239ca。<!-- existing:SF-2026-ARXIV-2604-23238:end -->
<!-- delta:SF-2026-ARXIV-2604-23238:start -->policy/CI/sandbox 拥有 invariant 与 commit authority，model 仅提出不可信 proposal<!-- delta:SF-2026-ARXIV-2604-23238:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-23238:end -->
<!-- books-review:SF-2026-ARXIV-2604-23277:start -->
<!-- existing:SF-2026-ARXIV-2604-23277:start -->真实 owner `books/part-07-agent/75-context.md#L326-context-中的信任冲突` 正文：## Context 中的信任冲突 System message、retrieved web content 与 tool result 最终都变成 token，但控制面必须保留来源差异： \| 来源 \| 可作为信息 \| 可直接授权动作 \| \| --- \| --- \| --- \| \| Platform policy \| 是 \| 仍由执行器强制 \| \| User request \| 是 \| 受用户权限限制 \| \| Retrieved content \| 是 \| 否 \| \| Tool result \| 是 \| 否 \| \| Model-generated memory \| 需验证 \| 否 \| 模型可以建议如何解释内容，不能改变其 authorization class。；相邻章 `books/part-07-agent/74-prompt.md#L16-prompt-改变的是条件不是参数; books/part-07-agent/76-rag.md#L16-参数化知识的边界` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=cde432ebf09578a859fa87fcdc51b88cf545eb0a722896ab7aa559f59e23a682。<!-- existing:SF-2026-ARXIV-2604-23277:end -->
<!-- delta:SF-2026-ARXIV-2604-23277:start -->context assembler 拥有选择与预算控制，原始 evidence 仍由 source owner 持有<!-- delta:SF-2026-ARXIV-2604-23277:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-23277:end -->
<!-- books-review:SF-2026-ARXIV-2604-23280:start -->
<!-- existing:SF-2026-ARXIV-2604-23280:start -->真实 owner `books/part-07-agent/84-agent-platform.md#L403-agent-runtime-state-machine` 正文：## Agent Runtime State Machine 一个通用 run 可表达为： ```text Created → ContextReady → Planning → Acting → Observing → Reflecting / Replanning → Waiting → Succeeded \| Failed \| Cancelled \| Escalated ``` 具体 workflow 可增加 domain states。关键是每次 transition 都可恢复、可审计，并绑定 actor、policy、budget 和 side-effect evidence。；相邻章 `books/part-07-agent/83-mcp.md#L19-为什么需要协议层` 已顺读。该主线尚未完整承载本 family 特有机制、failure 与 evidence boundary。 owner_sha256=b963414e7df5fef56194247e1c803fb24d3ccab30bf6e447175fdae3b9e99346。<!-- existing:SF-2026-ARXIV-2604-23280:end -->
<!-- delta:SF-2026-ARXIV-2604-23280:start -->AI agents are now running real transactions, workflows, and sub-agent chains across organizational boundaries without continuous human supervision. This creates a problem no current infrastructure is equipped to solve: how do you identify, verify, and hold accountable an entity with no body, no persistent memory, and no legal standing? We define AI Identity as the continuous relationship between what an AI agent is declared to be and what it is observed to do, bounded by the confidence that those two things correspond at any given moment. 该机制将长期 owner 定位到 `AGENT-PLATFORM`，并把相应 state/control/evidence identity 从隐式约定变成可检查对象。<!-- delta:SF-2026-ARXIV-2604-23280:end --> Decision=`Integrate`；evidence boundary：只接受 arXiv:2604.23280v1 的作者机制与实验；未披露硬件、precision、长度、batch、并发、成本或线上 SLO 均为 Not Disclosed。
<!-- books-review:SF-2026-ARXIV-2604-23280:end -->
<!-- books-review:SF-2026-ARXIV-2604-23318:start -->
<!-- existing:SF-2026-ARXIV-2604-23318:start -->真实 owner `books/part-04-training-system/33-grpo.md#L167-sequence-reward-怎样作用到-tokens` 正文：## Sequence Reward 怎样作用到 Tokens 若 reward 只在 response 末尾给出，常见简化是同一 `A_i` 作用于该 response 的所有有效 tokens： ```text A_(i,1) = ... = A_(i,\|y_i\|) = A_i ``` 这比 learned token value 简单，也更粗糙。正确 final answer 可能包含冗余或错误 reasoning，错误 final answer 也可能包含部分有价值步骤。 Process reward、step verifier 或更细粒度 credit assignment 可以提供局部信号，但会增加标注/evaluator 复杂度，并引入新的 exploit surface。；相邻章 `books/part-04-training-system/32-ppo.md#L18-把语言生成写成策略过程; books/part-04-training-system/34-dpo.md#L18-从-rlhf-的两阶段复杂度开始` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=37ab39bc16e7905281265dede7f404b65fb4814e9ee1e4d81a5342f6c012e97a。<!-- existing:SF-2026-ARXIV-2604-23318:end -->
<!-- delta:SF-2026-ARXIV-2604-23318:start -->rollout/reward owner 提交可复算 evidence，trainer 拥有 group advantage 与参数 commit<!-- delta:SF-2026-ARXIV-2604-23318:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-23318:end -->
<!-- books-review:SF-2026-ARXIV-2604-23333:start -->
<!-- existing:SF-2026-ARXIV-2604-23333:start -->真实 owner `books/part-04-training-system/33-grpo.md#L167-sequence-reward-怎样作用到-tokens` 正文：## Sequence Reward 怎样作用到 Tokens 若 reward 只在 response 末尾给出，常见简化是同一 `A_i` 作用于该 response 的所有有效 tokens： ```text A_(i,1) = ... = A_(i,\|y_i\|) = A_i ``` 这比 learned token value 简单，也更粗糙。正确 final answer 可能包含冗余或错误 reasoning，错误 final answer 也可能包含部分有价值步骤。 Process reward、step verifier 或更细粒度 credit assignment 可以提供局部信号，但会增加标注/evaluator 复杂度，并引入新的 exploit surface。；相邻章 `books/part-04-training-system/32-ppo.md#L18-把语言生成写成策略过程; books/part-04-training-system/34-dpo.md#L18-从-rlhf-的两阶段复杂度开始` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=37ab39bc16e7905281265dede7f404b65fb4814e9ee1e4d81a5342f6c012e97a。<!-- existing:SF-2026-ARXIV-2604-23333:end -->
<!-- delta:SF-2026-ARXIV-2604-23333:start -->rollout/reward owner 提交可复算 evidence，trainer 拥有 group advantage 与参数 commit<!-- delta:SF-2026-ARXIV-2604-23333:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-23333:end -->
<!-- books-review:SF-2026-ARXIV-2604-23338:start -->
<!-- existing:SF-2026-ARXIV-2604-23338:start -->真实 owner `books/part-06-ai-infrastructure/72-security.md#L16-从资产与信任边界开始` 正文：## 从资产与信任边界开始 需要保护的资产包括： - source data、labels 与 user context； - code、images、dependencies 与 credentials； - checkpoints、adapters、tokenizers 与 prompts； - registry metadata、evaluation 与 approvals； - GPU nodes、runtime memory 与 KV Cache； - APIs、tools、business systems 与 audit evidence。 主体包括用户、service accounts、controllers、training code、model server、model output 和 external tools。模型生成的文本不是可信主体，也不应自动获得调用者全部权限。；相邻章 `books/part-06-ai-infrastructure/71-multi-tenant.md#L16-先定义-tenant-与信任级别; books/part-06-ai-infrastructure/73-production-best-practice.md#L16-poc-隐含了哪些假设` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=cd99007e2f9b12ccf2bc7cd075bbf73c3b935255bf06bda7068b8f624de239ca。<!-- existing:SF-2026-ARXIV-2604-23338:end -->
<!-- delta:SF-2026-ARXIV-2604-23338:start -->policy/CI/sandbox 拥有 invariant 与 commit authority，model 仅提出不可信 proposal<!-- delta:SF-2026-ARXIV-2604-23338:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-23338:end -->
<!-- books-review:SF-2026-ARXIV-2604-23366:start -->
<!-- existing:SF-2026-ARXIV-2604-23366:start -->真实 owner `books/part-07-agent/76-rag.md#L410-rag-不消除-hallucination` 正文：## RAG 不消除 Hallucination 回答与检索文档内容一致，不等于回答由该文档支撑：模型可能只是在 parametric memory 中本就知道答案，检索内容甚至没有进入有效推理路径。若 evaluation 只看最终正确率或 citation overlap，就无法区分“证据导致了答案”与“答案碰巧和证据一致”。更严格的 groundedness contract 需要成对干预：保留问题、替换或遮蔽关键证据，观察结论与引用是否按预期改变，并把这种 counterfactual sensitivity 与普通 correctness 分开报告。 干预评估提高了因果诊断力，却增加样本构造、对照污染和 evaluator 成本；答案对证据不敏感也可能因为模型拥有正确先验，而非一定错误。低风险搜索可继续用 relevance/citation 指标快速迭代，高风险发布则需要 provenance、support span 与干预证据共同证明检索链真正拥有结论的 support authority。 ### Web Retrieval 的 Corpus 也可能主动塑造 Agent Trajectory 传统 RAG 把 corpus 当作被动事实集合；web-enabled Agent 会连续搜索、引用、回访并让多个页面共同塑造后续 query， 于是发布者优化的不再是单页排名，而是整条 evidence trajectory。检索系统必须记录页面 provenance、跨站关联、 query evolution 与最终 claim uptake，不能把“多处出现”自动解释为独立证据。协调内容生态可以提高可发现性，也会 制造相关来源、反馈回路与操纵面；高风险结论应回到独立 primary source 和 claim-level entailment。固定私有 corpus 仍适合低变化、强治理场景。受控虚构产品实验只证明 trajectory-level influence 可以被测量，不证明现实 web 排名 或所有搜索 Agent 会同样受影响。 ### ；相邻章 `books/part-07-agent/75-context.md#L16-context-是一次调用的可见状态; books/part-07-agent/77-memory.md#L20-context-与-memory-的状态边界` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=67561d15a90f3b4c8456e4d13cef9986646cc20bce9bbbb15bdcb01399f0e4f3。<!-- existing:SF-2026-ARXIV-2604-23366:end -->
<!-- delta:SF-2026-ARXIV-2604-23366:start -->Autonomous multi-agent LLM systems are increasingly deployed to investigate operational incidents and produce structured diagnostic reports. Their trustworthiness hinges on whether each claim is grounded in observed evidence rather than model-internal inference. Existing groundedness evaluators (binary classifiers, LLM-as-judge scalars, self-correction loops) treat supporting evidence as interchangeable and emit a single signal that offers no principled control over downstream action. 该机制将长期 owner 定位到 `AGENT-RAG`，并把相应 state/control/evidence identity 从隐式约定变成可检查对象。<!-- delta:SF-2026-ARXIV-2604-23366:end --> Decision=`No Change — Existing Coverage`；evidence boundary：只接受 arXiv:2604.23366v1 的作者机制与实验；未披露硬件、precision、长度、batch、并发、成本或线上 SLO 均为 Not Disclosed。
<!-- books-review:SF-2026-ARXIV-2604-23366:end -->
<!-- books-review:SF-2026-ARXIV-2604-23374:start -->
<!-- existing:SF-2026-ARXIV-2604-23374:start -->真实 owner `books/part-06-ai-infrastructure/72-security.md#L16-从资产与信任边界开始` 正文：## 从资产与信任边界开始 需要保护的资产包括： - source data、labels 与 user context； - code、images、dependencies 与 credentials； - checkpoints、adapters、tokenizers 与 prompts； - registry metadata、evaluation 与 approvals； - GPU nodes、runtime memory 与 KV Cache； - APIs、tools、business systems 与 audit evidence。 主体包括用户、service accounts、controllers、training code、model server、model output 和 external tools。模型生成的文本不是可信主体，也不应自动获得调用者全部权限。；相邻章 `books/part-06-ai-infrastructure/71-multi-tenant.md#L16-先定义-tenant-与信任级别; books/part-06-ai-infrastructure/73-production-best-practice.md#L16-poc-隐含了哪些假设` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=cd99007e2f9b12ccf2bc7cd075bbf73c3b935255bf06bda7068b8f624de239ca。<!-- existing:SF-2026-ARXIV-2604-23374:end -->
<!-- delta:SF-2026-ARXIV-2604-23374:start -->policy/CI/sandbox 拥有 invariant 与 commit authority，model 仅提出不可信 proposal<!-- delta:SF-2026-ARXIV-2604-23374:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-23374:end -->
<!-- books-review:SF-2026-ARXIV-2604-23455:start -->
<!-- existing:SF-2026-ARXIV-2604-23455:start -->真实 owner `books/part-06-ai-infrastructure/66-evaluation-system.md#L78-从目标到证据而不是从指标到目标` 正文：## 从目标到证据，而不是从指标到目标 Evaluation 的起点不是“平台能采集什么 metric”，而是系统希望满足什么目标。可以把链路写成： ```text intended use and risk → evaluation specification → dataset / environment → system execution → scorer / human judgment → aggregation and uncertainty → decision policy → release / rollback / investigation → production feedback ``` `intended use` 决定什么错误重要。例如代码补全、医疗问答和广告生成都可以计算文本相似度，但相同指标不代表相同风险。评估 specification 至少应声明： ```text EvalSpec = target behavior + eligible population + failure taxonomy + metrics and scorers + slice definitions + thresholds / comparison rules + uncertainty requirement + owner and review policy ``` 如果目标没有被写清楚，团队往往会优化最容易计算的 proxy。模型变得更会迎合 judge，却未必更可靠；服务提高吞吐，却可能让 tail latency 和任务完成率下降。这不是模型“作弊”，而是控制系统给出了错误目标。；相邻章 `books/part-06-ai-infrastructure/65-kai-scheduler.md#L18-为什么-ai-cluster-需要更强的-queue-模型; books/part-06-ai-infrastructure/67-monitoring.md#L18-先定义目标再选择可测信号` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=ba07952c1fe646f17bfd554f905fb4a594aaa8676cc3e8aea0edfa2526800e09。<!-- existing:SF-2026-ARXIV-2604-23455:end -->
<!-- delta:SF-2026-ARXIV-2604-23455:start -->EvalSpec owner 冻结 subject/data/scorer，release owner 依据 run evidence 作决定<!-- delta:SF-2026-ARXIV-2604-23455:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-23455:end -->
<!-- books-review:SF-2026-ARXIV-2604-23459:start -->
<!-- existing:SF-2026-ARXIV-2604-23459:start -->真实 owner `books/part-06-ai-infrastructure/72-security.md#L16-从资产与信任边界开始` 正文：## 从资产与信任边界开始 需要保护的资产包括： - source data、labels 与 user context； - code、images、dependencies 与 credentials； - checkpoints、adapters、tokenizers 与 prompts； - registry metadata、evaluation 与 approvals； - GPU nodes、runtime memory 与 KV Cache； - APIs、tools、business systems 与 audit evidence。 主体包括用户、service accounts、controllers、training code、model server、model output 和 external tools。模型生成的文本不是可信主体，也不应自动获得调用者全部权限。；相邻章 `books/part-06-ai-infrastructure/71-multi-tenant.md#L16-先定义-tenant-与信任级别; books/part-06-ai-infrastructure/73-production-best-practice.md#L16-poc-隐含了哪些假设` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=cd99007e2f9b12ccf2bc7cd075bbf73c3b935255bf06bda7068b8f624de239ca。<!-- existing:SF-2026-ARXIV-2604-23459:end -->
<!-- delta:SF-2026-ARXIV-2604-23459:start -->policy/CI/sandbox 拥有 invariant 与 commit authority，model 仅提出不可信 proposal<!-- delta:SF-2026-ARXIV-2604-23459:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-23459:end -->
<!-- books-review:SF-2026-ARXIV-2604-23466:start -->
<!-- existing:SF-2026-ARXIV-2604-23466:start -->真实 owner `books/part-05-inference-system/49-tensorrt-llm.md#L18-从计算图开始` 正文：## 从计算图开始 理解 TensorRT-LLM 可以先从计算图开始：模型不是一个黑盒函数，而是一张计算图。图里有算子、依赖、常量、临时 tensor 和 kernel launch。 朴素执行方式会产生很多额外开销： - 多个小算子分别 launch kernel。 - 中间结果频繁写回 HBM 再读出。 - 常量表达式运行时重复计算。 - 独立算子没有被合理并行调度。 图优化的第一性原理是：数学结果不变的前提下，减少运行时不必要的计算、访存和调度开销。；相邻章 `books/part-05-inference-system/48-speculative-decoding.md#L18-从-decode-串行瓶颈开始; books/part-05-inference-system/50-vllm.md#L18-serving-引擎不是模型-loader` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=e5d5d64f08769bf2b69fe063ae4524c62f942da4e0c48b2966d39ac8e214af1b。<!-- existing:SF-2026-ARXIV-2604-23466:end -->
<!-- delta:SF-2026-ARXIV-2604-23466:start -->compiled runtime 拥有 plan/shape/kernel identity，fallback backend 保留兼容路径<!-- delta:SF-2026-ARXIV-2604-23466:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-23466:end -->
<!-- books-review:SF-2026-ARXIV-2604-23467:start -->
<!-- existing:SF-2026-ARXIV-2604-23467:start -->真实 owner `books/part-05-inference-system/49-tensorrt-llm.md#L18-从计算图开始` 正文：## 从计算图开始 理解 TensorRT-LLM 可以先从计算图开始：模型不是一个黑盒函数，而是一张计算图。图里有算子、依赖、常量、临时 tensor 和 kernel launch。 朴素执行方式会产生很多额外开销： - 多个小算子分别 launch kernel。 - 中间结果频繁写回 HBM 再读出。 - 常量表达式运行时重复计算。 - 独立算子没有被合理并行调度。 图优化的第一性原理是：数学结果不变的前提下，减少运行时不必要的计算、访存和调度开销。；相邻章 `books/part-05-inference-system/48-speculative-decoding.md#L18-从-decode-串行瓶颈开始; books/part-05-inference-system/50-vllm.md#L18-serving-引擎不是模型-loader` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=e5d5d64f08769bf2b69fe063ae4524c62f942da4e0c48b2966d39ac8e214af1b。<!-- existing:SF-2026-ARXIV-2604-23467:end -->
<!-- delta:SF-2026-ARXIV-2604-23467:start -->compiled runtime 拥有 plan/shape/kernel identity，fallback backend 保留兼容路径<!-- delta:SF-2026-ARXIV-2604-23467:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-23467:end -->
<!-- books-review:SF-2026-ARXIV-2604-23478:start -->
<!-- existing:SF-2026-ARXIV-2604-23478:start -->真实 owner `books/part-06-ai-infrastructure/66-evaluation-system.md#L78-从目标到证据而不是从指标到目标` 正文：## 从目标到证据，而不是从指标到目标 Evaluation 的起点不是“平台能采集什么 metric”，而是系统希望满足什么目标。可以把链路写成： ```text intended use and risk → evaluation specification → dataset / environment → system execution → scorer / human judgment → aggregation and uncertainty → decision policy → release / rollback / investigation → production feedback ``` `intended use` 决定什么错误重要。例如代码补全、医疗问答和广告生成都可以计算文本相似度，但相同指标不代表相同风险。评估 specification 至少应声明： ```text EvalSpec = target behavior + eligible population + failure taxonomy + metrics and scorers + slice definitions + thresholds / comparison rules + uncertainty requirement + owner and review policy ``` 如果目标没有被写清楚，团队往往会优化最容易计算的 proxy。模型变得更会迎合 judge，却未必更可靠；服务提高吞吐，却可能让 tail latency 和任务完成率下降。这不是模型“作弊”，而是控制系统给出了错误目标。；相邻章 `books/part-06-ai-infrastructure/65-kai-scheduler.md#L18-为什么-ai-cluster-需要更强的-queue-模型; books/part-06-ai-infrastructure/67-monitoring.md#L18-先定义目标再选择可测信号` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=ba07952c1fe646f17bfd554f905fb4a594aaa8676cc3e8aea0edfa2526800e09。<!-- existing:SF-2026-ARXIV-2604-23478:end -->
<!-- delta:SF-2026-ARXIV-2604-23478:start -->Large language models are widely adopted as automated evaluation judges, yet the stability of their verdicts under semantically equivalent prompt rephrasings remains largely unexamined. We conduct a systematic empirical study of prompt-induced decision instability across multiple evaluation tasks and judge architectures. To facilitate this analysis, we release JudgeSense, a benchmark comprising hand-validated prompt-paraphrase pairs spanning factuality, coherence, relevance, and preference, drawn from established NLP benchmarks and accompanied by comprehensive decision logs. 该机制将长期 owner 定位到 `PLATFORM-EVALUATION-SYSTEM`，并把相应 state/control/evidence identity 从隐式约定变成可检查对象。<!-- delta:SF-2026-ARXIV-2604-23478:end --> Decision=`No Change — Existing Coverage`；evidence boundary：只接受 arXiv:2604.23478v1 的作者机制与实验；未披露硬件、precision、长度、batch、并发、成本或线上 SLO 均为 Not Disclosed。
<!-- books-review:SF-2026-ARXIV-2604-23478:end -->


### Independent prewrite re-audit amendment

本轮不读取旧 Weekly 语义输入；全量 closure 反向审计重开 6 个 family，冻结 `419 = 27 retained + 392 closures`。prewrite 阶段形成 canonical Integrate queue=2；两项随后均已写回 Books，并通过独立 post-write semantic audit，最终 Books Gate=`Passed`。

<!-- analysis-decision:SF-2026-ARXIV-2604-23205:start -->Full Review 与 Books comparison 已完成；未选 Top-3 仅是叙事预算。<!-- analysis-decision:SF-2026-ARXIV-2604-23205:end -->
<!-- existing:SF-2026-ARXIV-2604-23205:start -->current owner `books/part-06-ai-infrastructure/72-security.md#L16-从资产与信任边界开始` 已顺读：## 从资产与信任边界开始  需要保护的资产包括：  - source data、labels 与 user context； - code、images、dependencies 与 credentials； - checkpoints、adapters、tokenizers 与 prompts； - registry metadata、evaluation 与 approvals； - GPU nodes、runtime memory 与 KV Cache； - APIs、tools、business systems 与 audit evidence。  主体包括用户、service accounts、controllers、training code、model server、model output 和 external tools。模型生成的文本不是可信主体，也不应自动获得调用者全部权限。  ## 生命周期威胁  ```text；相邻 refs=books/part-06-ai-infrastructure/71-multi-tenant.md#L16-先定义-tenant-与信任级别; books/part-06-ai-infrastructure/73-production-best-practice.md#L16-poc-隐含了哪些假设。<!-- existing:SF-2026-ARXIV-2604-23205:end -->
<!-- delta:SF-2026-ARXIV-2604-23205:start -->UMA edge accelerator 在 64-byte AXI burst 上并行生成 AES-CTR keystream，只让 plaintext weight tile 短暂进入隔离 NPU SRAM。<!-- delta:SF-2026-ARXIV-2604-23205:end -->
<!-- books-review:SF-2026-ARXIV-2604-23205:start -->Decision=`Integrate`；98.4% 带宽是 proxy hardware measurement 加 idealized model 的投影；未制造该 NPU silicon，且假设 trusted die/SMMU，不覆盖 invasive、side-channel 与 supply-chain 攻击。<!-- books-review:SF-2026-ARXIV-2604-23205:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-23172:start -->Full Review 与 Books comparison 已完成；未选 Top-3 仅是叙事预算。<!-- analysis-decision:SF-2026-ARXIV-2604-23172:end -->
<!-- existing:SF-2026-ARXIV-2604-23172:start -->current owner `books/part-02-model/16-feed-forward-mlp.md#L18-只有-attention-会缺少什么` 已顺读：## 只有 Attention 会缺少什么  Attention 的核心输出是 Value 的加权组合。即使 Q/K/V projection 是可学习线性变换，聚合本身仍主要在已有 token states 之间搬运和混合信息。  模型还需要在每个位置上产生新的非线性特征：放大某些组合、抑制另一些组合，并把上下文证据映射到下一层更有用的表示。  朴素方案是继续堆叠更多 Attention。这样能反复交换信息，却不一定提供足够的逐位置非线性容量。Transformer 因而交替使用两类操作：  ```text Attention  across tokens MLP        within each token position ```  ## 标准两层 FFN  输入 hidden states 为：；相邻 refs=books/part-02-model/15-multi-head-attention.md#L18-单个-head-的表达瓶颈; books/part-02-model/17-transformer-layer.md#L18-直接串联为什么难以堆深。<!-- existing:SF-2026-ARXIV-2604-23172:end -->
<!-- delta:SF-2026-ARXIV-2604-23172:start -->VQ-QAT 以 vector codebook 近似权重，并按层在 vector 与 linear quantizer 间选择。<!-- delta:SF-2026-ARXIV-2604-23172:end -->
<!-- books-review:SF-2026-ARXIV-2604-23172:start -->Decision=`No Change — Existing Coverage`；证据只覆盖作者模型、任务和量化配置，不能证明任意架构、kernel 或设备上都更快。<!-- books-review:SF-2026-ARXIV-2604-23172:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-23272:start -->Full Review 与 Books comparison 已完成；未选 Top-3 仅是叙事预算。<!-- analysis-decision:SF-2026-ARXIV-2604-23272:end -->
<!-- existing:SF-2026-ARXIV-2604-23272:start -->current owner `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L177-state-ownership-与-freshness` 已顺读：## State ownership 与 freshness  - sensor pipeline 拥有 timestamped observations； - state estimator 拥有当前 calibrated belief； - VLA/world-action model 拥有 provisional proposal； - controller 拥有 action execution lease； - safety monitor 拥有 veto / emergency stop； - environment 拥有真实 outcome； - run log 拥有 observation-action-effect evidence。  ### Policy 内部的 Latent Memory 是 Episode State，不是 Agent Memory  单帧或短 action chunk 足以处理局部连续动作，却无法长期保留遮挡物体、阶段进度和失败上下文。一个受限分支在 policy 内维护快慢两级 latent：短期 state 跟随近期 observation，curator 只把通过 admission 的片段提升到长期 state，并在读取后压缩或替换。 ；相邻 refs=books/part-03-multimodal-world-models/25-multimodal-world-models.md#L16-从三个容易混淆的对象开始。<!-- existing:SF-2026-ARXIV-2604-23272:end -->
<!-- delta:SF-2026-ARXIV-2604-23272:start -->把物理 feedback 作为独立 sensory stream 进入 VLA，而不是只依赖一次性视觉观测。<!-- delta:SF-2026-ARXIV-2604-23272:end -->
<!-- books-review:SF-2026-ARXIV-2604-23272:start -->Decision=`No Change — Existing Coverage`；实验只说明所披露环境中的反馈收益，不证明传感器延迟、噪声或真实机器人故障下的安全闭环。<!-- books-review:SF-2026-ARXIV-2604-23272:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-24790:start -->Full Review 与 Books comparison 已完成；未选 Top-3 仅是叙事预算。<!-- analysis-decision:SF-2026-ARXIV-2604-24790:end -->
<!-- existing:SF-2026-ARXIV-2604-24790:start -->current owner `books/part-06-ai-infrastructure/72-security.md#L16-从资产与信任边界开始` 已顺读：## 从资产与信任边界开始  需要保护的资产包括：  - source data、labels 与 user context； - code、images、dependencies 与 credentials； - checkpoints、adapters、tokenizers 与 prompts； - registry metadata、evaluation 与 approvals； - GPU nodes、runtime memory 与 KV Cache； - APIs、tools、business systems 与 audit evidence。  主体包括用户、service accounts、controllers、training code、model server、model output 和 external tools。模型生成的文本不是可信主体，也不应自动获得调用者全部权限。  ## 生命周期威胁  ```text；相邻 refs=books/part-06-ai-infrastructure/71-multi-tenant.md#L16-先定义-tenant-与信任级别; books/part-06-ai-infrastructure/73-production-best-practice.md#L16-poc-隐含了哪些假设。<!-- existing:SF-2026-ARXIV-2604-24790:end -->
<!-- delta:SF-2026-ARXIV-2604-24790:start -->安全语义上合理的 1–5 token audio injection 可诱导 stop、acknowledgement loop 或 false alert，攻击目标是决策层 availability 而非恶意文本分类。<!-- delta:SF-2026-ARXIV-2604-24790:end -->
<!-- books-review:SF-2026-ARXIV-2604-24790:start -->Decision=`Integrate`；只在 simulated tool-calling robot 上评估；prompt defenses 不等于 architecture defense，真实声学链路与生产机器人未验证。<!-- books-review:SF-2026-ARXIV-2604-24790:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-23141:start -->Full Review 与 Books comparison 已完成；未选 Top-3 仅是叙事预算。<!-- analysis-decision:SF-2026-ARXIV-2604-23141:end -->
<!-- existing:SF-2026-ARXIV-2604-23141:start -->current owner `books/part-06-ai-infrastructure/72-security.md#L16-从资产与信任边界开始` 已顺读：## 从资产与信任边界开始  需要保护的资产包括：  - source data、labels 与 user context； - code、images、dependencies 与 credentials； - checkpoints、adapters、tokenizers 与 prompts； - registry metadata、evaluation 与 approvals； - GPU nodes、runtime memory 与 KV Cache； - APIs、tools、business systems 与 audit evidence。  主体包括用户、service accounts、controllers、training code、model server、model output 和 external tools。模型生成的文本不是可信主体，也不应自动获得调用者全部权限。  ## 生命周期威胁  ```text；相邻 refs=books/part-06-ai-infrastructure/71-multi-tenant.md#L16-先定义-tenant-与信任级别; books/part-06-ai-infrastructure/73-production-best-practice.md#L16-poc-隐含了哪些假设。<!-- existing:SF-2026-ARXIV-2604-23141:end -->
<!-- delta:SF-2026-ARXIV-2604-23141:start -->UNSEEN 将 AR sensing、LLM unlearning 与 agent ACL/guardrail 串成跨层 threat response。<!-- delta:SF-2026-ARXIV-2604-23141:end -->
<!-- books-review:SF-2026-ARXIV-2604-23141:start -->Decision=`No Change — Existing Coverage`；跨栈原型不能证明 unlearning 完整性、ACL 无绕过或真实设备上的端到端安全。<!-- books-review:SF-2026-ARXIV-2604-23141:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-23483:start -->Full Review 与 Books comparison 已完成；未选 Top-3 仅是叙事预算。<!-- analysis-decision:SF-2026-ARXIV-2604-23483:end -->
<!-- existing:SF-2026-ARXIV-2604-23483:start -->current owner `books/part-06-ai-infrastructure/72-security.md#L16-从资产与信任边界开始` 已顺读：## 从资产与信任边界开始  需要保护的资产包括：  - source data、labels 与 user context； - code、images、dependencies 与 credentials； - checkpoints、adapters、tokenizers 与 prompts； - registry metadata、evaluation 与 approvals； - GPU nodes、runtime memory 与 KV Cache； - APIs、tools、business systems 与 audit evidence。  主体包括用户、service accounts、controllers、training code、model server、model output 和 external tools。模型生成的文本不是可信主体，也不应自动获得调用者全部权限。  ## 生命周期威胁  ```text；相邻 refs=books/part-06-ai-infrastructure/71-multi-tenant.md#L16-先定义-tenant-与信任级别; books/part-06-ai-infrastructure/73-production-best-practice.md#L16-poc-隐含了哪些假设。<!-- existing:SF-2026-ARXIV-2604-23483:end -->
<!-- delta:SF-2026-ARXIV-2604-23483:start -->以黑盒 adversarial rewriting 连续穿过多阶段 NLP pipeline，暴露逐级语义放大。<!-- delta:SF-2026-ARXIV-2604-23483:end -->
<!-- books-review:SF-2026-ARXIV-2604-23483:start -->Decision=`No Change — Existing Coverage`；只用单一 misinformation dataset、point estimates 与同族 semantic judge，未做跨 pipeline 验证。<!-- books-review:SF-2026-ARXIV-2604-23483:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260426-COVERAGE | fresh-context:april01-07-independent-reviewer | coverage | coverage:SRC-ARXIV:20260426 | none | — | passed |
| SA-20260426-EVIDENCE | fresh-context:april01-07-independent-reviewer | evidence | validator:review-completion-v1 | none | — | passed |
| SA-20260426-DEEP | fresh-context:april01-07-independent-reviewer | deep_analysis_selection | validator:deep-analysis-selection-v1 | none | — | passed |
| SA-20260426-BOOKS | fresh-context:apr26-30-independent-postwrite-reviewer | books | books-review:SF-2026-ARXIV-2604-23205;books-review:SF-2026-ARXIV-2604-24790 | none | 已纠正 2604.23205 的 SMMU/DMA authentication 与 fallback 边界，依据 `../_sources/april-26-30-books-post-write-semantic-audit.json` 复验通过 | passed |

## 8. Ignored Noise

其余 392 个 identity 均保留在 `screening-ledger-final.json`，每条具有 title、abstract、日期和 family-specific closure；recall 与 denominator retention 已分离。

## 9. Recommended Action

本日独立 Historical Daily 已闭环；后续保持 weight-streaming trust boundary 与跨模态 action commit authority 的 owner 边界。

## 10. Repository Changes

- 重建本日 final denominator、exact-v1 Source Review、Deep Selection、current Books comparison 与 writeback queue。
- 2 项 Integrate 已写入 `books/part-06-ai-infrastructure/72-security.md`，并通过非写作者 post-write Semantic Audit。

## 11. Open Questions

- 无。本日 ordinary pending、blocked 与 unresolved semantic finding 均为 0。

## 12. Sources

- strict-window frozen inventory：`papers/2026/04/_sources/daily-20260426/inventory.json`
- exact-v1 receipts：`papers/2026/04/_sources/daily-20260426/exact-v1-review-packet.json`
- Historical Daily independence：`weekly-dependency-audit.json`（dependency=0）
- [ProEval: Proactive Failure Discovery and Efficient Performance Estimation for Generative AI Evaluation](https://arxiv.org/abs/2604.23099v1) — exact-v1；first-public 2026-04-25；accessed 2026-09-01
- [Unstable Rankings in Bayesian Deep Learning Evaluation](https://arxiv.org/abs/2604.23102v1) — exact-v1；first-public 2026-04-25；accessed 2026-09-01
- [Mixture of Heterogeneous Grouped Experts for Language Modeling](https://arxiv.org/abs/2604.23108v1) — exact-v1；first-public 2026-04-25；accessed 2026-09-01
- [Breaking Lock-In: Preserving Steerability under Low-Data VLA Post-Training](https://arxiv.org/abs/2604.23121v1) — exact-v1；first-public 2026-04-25；accessed 2026-09-01
- [GreenDyGNN: Runtime-Adaptive Energy-Efficient Communication for Distributed GNN Training](https://arxiv.org/abs/2604.23139v1) — exact-v1；first-public 2026-04-25；accessed 2026-09-01
- [Scaling Multi-Node Mixture-of-Experts Inference Using Expert Activation Patterns](https://arxiv.org/abs/2604.23150v1) — exact-v1；first-public 2026-04-25；accessed 2026-09-01
- [Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines](https://arxiv.org/abs/2604.23178v1) — exact-v1；first-public 2026-04-25；accessed 2026-09-01
- [Discovering Agentic Safety Specifications from 1-Bit Danger Signals](https://arxiv.org/abs/2604.23210v1) — exact-v1；first-public 2026-04-25；accessed 2026-09-01
- [Hiding in Plain Sight: Detectability-Aware Antidistillation of Reasoning Models](https://arxiv.org/abs/2604.23238v1) — exact-v1；first-public 2026-04-25；accessed 2026-09-01
- [From Similarity to Structure: Training-free LLM Context Compression with Hybrid Graph Priors](https://arxiv.org/abs/2604.23277v1) — exact-v1；first-public 2026-04-25；accessed 2026-09-01
- [AI Identity: Standards, Gaps, and Research Directions for AI Agents](https://arxiv.org/abs/2604.23280v1) — exact-v1；first-public 2026-04-25；accessed 2026-09-01
- [Hidden States Know Where Reasoning Diverges: Credit Assignment via Span-Level Wasserstein Distance](https://arxiv.org/abs/2604.23318v1) — exact-v1；first-public 2026-04-25；accessed 2026-09-01
- [Process Supervision of Confidence Margin for Calibrated LLM Reasoning](https://arxiv.org/abs/2604.23333v1) — exact-v1；first-public 2026-04-25；accessed 2026-09-01
- [A Systematic Survey of Security Threats and Defenses in LLM-Based AI Agents: A Layered Attack Surface Framework](https://arxiv.org/abs/2604.23338v1) — exact-v1；first-public 2026-04-25；accessed 2026-09-01
- [GSAR: Typed Grounding for Hallucination Detection and Recovery in Multi-Agent LLMs](https://arxiv.org/abs/2604.23366v1) — exact-v1；first-public 2026-04-26；accessed 2026-09-01
- [Ghost in the Agent: Redefining Information Flow Tracking for LLM Agents](https://arxiv.org/abs/2604.23374v1) — exact-v1；first-public 2026-04-26；accessed 2026-09-01
- [CUJBench: Benchmarking LLM-Agent on Cross-Modal Failure Diagnosis from Browser to Backend](https://arxiv.org/abs/2604.23455v1) — exact-v1；first-public 2026-04-26；accessed 2026-09-01
- [Architecture Matters for Multi-Agent Security](https://arxiv.org/abs/2604.23459v1) — exact-v1；first-public 2026-04-26；accessed 2026-09-01
- [Evaluating CUDA Tile for AI Workloads on Hopper and Blackwell GPUs](https://arxiv.org/abs/2604.23466v1) — exact-v1；first-public 2026-04-26；accessed 2026-09-01
- [Hybrid JIT-CUDA Graph Optimization for Low-Latency Large Language Model Inference](https://arxiv.org/abs/2604.23467v1) — exact-v1；first-public 2026-04-26；accessed 2026-09-01
- [JudgeSense: A Benchmark for Prompt Sensitivity in LLM-as-a-Judge Systems](https://arxiv.org/abs/2604.23478v1) — exact-v1；first-public 2026-04-26；accessed 2026-09-01

### Materials Request Ledger

<!-- validator:materials-request-v1 -->
| Request ID | Priority | Source Family ID | Source ID | Gap / Limitation ID | Owner Week | Known Identifiers / URLs | Missing Material | Why Existing Evidence Is Insufficient | Acceptable Substitute | Suggested File Name | Required Review Scope |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

无：retained family 的 official exact-v1 已全部完成 Review；本日无 withdrawn primary source，按合同留在 pre-denominator closure，不是 blocker。

## 13. Final Status

Completion Status: `Complete`

Coverage: `Closed`

Evidence: `Passed`

Books: `Passed`

unresolved findings: 0

Independent Historical Daily closure：raw/registered/screened=419/419/419、final denominator=27、closures=392、exact-v1 complete=27、pending=0、blocked=0；2/2 Integrate 已写回并通过非写作者 post-write Semantic Audit。
