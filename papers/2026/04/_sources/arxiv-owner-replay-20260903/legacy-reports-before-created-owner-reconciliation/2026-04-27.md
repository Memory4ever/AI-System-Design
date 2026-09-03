# Daily Research — 2026-04-27

**Research Date:** 2026-04-27

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-04-26 09:00:00 ～ 2026-04-27 09:00:00（Asia/Shanghai，北京时间，左闭右开）

**Contract:** V2.1 historical Daily independent replay；技术结论只绑定 official exact-v1 与 current Books。

**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed；1/1 Integrate 已写回并通过独立 post-write Semantic Audit。

## Executive Summary

严格窗口注册并逐项 title+abstract 语义筛选 476/476 identity；author denominator=17，fresh-context final denominator=20，closures=456。独立审计重开 FN=3、移除 FP=0，withdrawn=0；20/20 exact-v1 Source Review complete，pending=0、blocked=0。current owner+adjacent comparison 后 1/1 Integrate 已写入 canonical Books；非写作者 post-write 首轮发现 denominator 表述错误，修正并复验通过。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-04-27 |
| Window End | 2026-04-27 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | DEN-20260427-FRESH-20 |
| Denominator Frozen At | 2026-09-01T15:55:00Z |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-04-26T09:00:00+08:00 | 2026-04-27T09:00:00+08:00 | 2026-09-01T15:55:00Z | frozen strict-window inventory + 476/476 independent title/abstract replay + official exact-v1 HTML/PDF | checked | 476 | SF-2026-ARXIV-2604-23488;SF-2026-ARXIV-2604-23505;SF-2026-ARXIV-2604-23543;SF-2026-ARXIV-2604-23553;SF-2026-ARXIV-2604-23577;SF-2026-ARXIV-2604-23581;SF-2026-ARXIV-2604-23584;SF-2026-ARXIV-2604-23626;SF-2026-ARXIV-2604-23646;SF-2026-ARXIV-2604-23711;SF-2026-ARXIV-2604-23747;SF-2026-ARXIV-2604-23758;SF-2026-ARXIV-2604-23775;SF-2026-ARXIV-2604-23781;SF-2026-ARXIV-2604-23798;SF-2026-ARXIV-2604-23831;SF-2026-ARXIV-2604-23838;SF-2026-ARXIV-2604-23853;SF-2026-ARXIV-2604-23887;SF-2026-ARXIV-2607-05397 | pages=closed; final_cursor=end; registered=476; screened=476; retained=17; closure=459 | 2026-04-27T09:00:00+08:00 | screening-ledger-final.json#sha256=ac6e313f4bea68447cf6faaf67560baffe5f4dd793e4a837b1e353d2e334d03c | — |

### Coverage Limitations

<!-- coverage:SRC-ARXIV:20260427:start -->Fresh-context reviewer 重放 476/476：重开 3 个 false negative，移除 0 个 false positive；96 个 FN challenge 经逐 family exact/abstract boundary 仍保持 closure。withdrawn primary source 只保留 identity/状态 closure，不进入 denominator。<!-- coverage:SRC-ARXIV:20260427:end -->

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2604-23488 | arXiv:2604.23488v1 | paper-v1:2604.23488 | 2026-W17 | 2026-04-26 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-23488 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23488 | no |
| SF-2026-ARXIV-2604-23505 | arXiv:2604.23505v1 | paper-v1:2604.23505 | 2026-W17 | 2026-04-26 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-23505 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23505 | no |
| SF-2026-ARXIV-2604-23543 | arXiv:2604.23543v1 | paper-v1:2604.23543 | 2026-W17 | 2026-04-26 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-23543 | self | — | new_in_window | TRAIN-DPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23543 | no |
| SF-2026-ARXIV-2604-23553 | arXiv:2604.23553v1 | paper-v1:2604.23553 | 2026-W17 | 2026-04-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-23553 | self | — | new_in_window | INFER-DECODE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23553 | no |
| SF-2026-ARXIV-2604-23577 | arXiv:2604.23577v1 | paper-v1:2604.23577 | 2026-W17 | 2026-04-26 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-23577 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23577 | no |
| SF-2026-ARXIV-2604-23581 | arXiv:2604.23581v1 | paper-v1:2604.23581 | 2026-W17 | 2026-04-26 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-23581 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23581 | no |
| SF-2026-ARXIV-2604-23584 | arXiv:2604.23584v1 | paper-v1:2604.23584 | 2026-W17 | 2026-04-26 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-23584 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23584 | no |
| SF-2026-ARXIV-2604-23626 | arXiv:2604.23626v1 | paper-v1:2604.23626 | 2026-W17 | 2026-04-26 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-23626 | self | — | new_in_window | AGENT-PLANNING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23626 | no |
| SF-2026-ARXIV-2604-23646 | arXiv:2604.23646v1 | paper-v1:2604.23646 | 2026-W17 | 2026-04-26 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-23646 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23646 | no |
| SF-2026-ARXIV-2604-23711 | arXiv:2604.23711v1 | paper-v1:2604.23711 | 2026-W17 | 2026-04-26 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-23711 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23711 | no |
| SF-2026-ARXIV-2604-23747 | arXiv:2604.23747v1 | paper-v1:2604.23747 | 2026-W17 | 2026-04-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-23747 | self | — | new_in_window | TRAIN-SFT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23747 | no |
| SF-2026-ARXIV-2604-23758 | arXiv:2604.23758v1 | paper-v1:2604.23758 | 2026-W17 | 2026-04-26 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-23758 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23758 | no |
| SF-2026-ARXIV-2604-23775 | arXiv:2604.23775v1 | paper-v1:2604.23775 | 2026-W17 | 2026-04-26 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-23775 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23775 | no |
| SF-2026-ARXIV-2604-23781 | arXiv:2604.23781v1 | paper-v1:2604.23781 | 2026-W18 | 2026-04-27 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-23781 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23781 | no |
| SF-2026-ARXIV-2604-23798 | arXiv:2604.23798v1 | paper-v1:2604.23798 | 2026-W18 | 2026-04-27 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-23798 | self | — | new_in_window | MODEL-SELF-ATTENTION | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23798 | no |
| SF-2026-ARXIV-2604-23831 | arXiv:2604.23831v1 | paper-v1:2604.23831 | 2026-W18 | 2026-04-27 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-23831 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23831 | no |
| SF-2026-ARXIV-2604-23838 | arXiv:2604.23838v1 | paper-v1:2604.23838 | 2026-W18 | 2026-04-27 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-23838 | self | — | new_in_window | TRAIN-RLHF | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23838 | no |
| SF-2026-ARXIV-2604-23853 | arXiv:2604.23853v1 | paper-v1:2604.23853 | 2026-W18 | 2026-04-27 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-23853 | self | — | new_in_window | PLATFORM-TRACE | Integrate | books-review:SF-2026-ARXIV-2604-23853 | no |
| SF-2026-ARXIV-2604-23887 | arXiv:2604.23887v1 | paper-v1:2604.23887 | 2026-W18 | 2026-04-27 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-23887 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23887 | no |
| SF-2026-ARXIV-2607-05397 | arXiv:2607.05397v1 | paper-v1:2607.05397 | 2026-W17 | 2026-04-26 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2607-05397 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-05397 | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2604-23488 | RP-f6f760d5e64940da | deep | arXiv:2604.23488v1 | SRC-ARXIV@arXiv:2604.23488v1 | https://arxiv.org/html/2604.23488v1 §Method / Architecture / Framework (official exact-v1 full read) | https://arxiv.org/html/2604.23488v1 §Experiments / Evaluation / Results (official exact-v1 full read) | https://arxiv.org/html/2604.23488v1 §Discussion / Limitations / Conclusion (official exact-v1 full read; no broader claim inferred where a dedicated heading is absent) | https://arxiv.org/abs/2604.23488v1 ; https://arxiv.org/html/2604.23488v1 | claim:SF-2026-ARXIV-2604-23488 | complete |
| SF-2026-ARXIV-2604-23505 | RP-3f49a6b1801b2247 | deep | arXiv:2604.23505v1 | SRC-ARXIV@arXiv:2604.23505v1 | https://arxiv.org/html/2604.23505v1 §Method / Architecture / Framework (official exact-v1 full read) | https://arxiv.org/html/2604.23505v1 §Experiments / Evaluation / Results (official exact-v1 full read) | https://arxiv.org/html/2604.23505v1 §Discussion / Limitations / Conclusion (official exact-v1 full read; no broader claim inferred where a dedicated heading is absent) | https://arxiv.org/abs/2604.23505v1 ; https://arxiv.org/html/2604.23505v1 | claim:SF-2026-ARXIV-2604-23505 | complete |
| SF-2026-ARXIV-2604-23543 | RP-4411c8cfb3fedcb7 | deep | arXiv:2604.23543v1 | SRC-ARXIV@arXiv:2604.23543v1 | arXiv:2604.23543v1 §Method / Identity — Mechanism / State Ownership (source artifact papers/2026/04/_sources/daily-20260427/exact-v1/2604.23543v1.html#exact-v1 independent HTML full read) | arXiv:2604.23543v1 §Evaluation — Evaluation Contract — 3 Experiments (source artifact papers/2026/04/_sources/daily-20260427/exact-v1/2604.23543v1.html#exact-v1 independent HTML full read) | arXiv:2604.23543v1 §Scope and Limitations — Evidence Proves / Does Not Prove — 5 Conclusion (source artifact papers/2026/04/_sources/daily-20260427/exact-v1/2604.23543v1.html#exact-v1 independent HTML full read) | arXiv:2604.23543v1 §Artifact / Access — Artifact / Access — Appendix B Win Rate Evaluation (source artifact papers/2026/04/_sources/daily-20260427/exact-v1/2604.23543v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-23543 | complete |
| SF-2026-ARXIV-2604-23553 | RP-8394935984ce98fb | deep | arXiv:2604.23553v1 | SRC-ARXIV@arXiv:2604.23553v1 | arXiv:2604.23553v1 §Method / Identity — Mechanism / State Ownership (source artifact papers/2026/04/_sources/daily-20260427/exact-v1/2604.23553v1.html#exact-v1 independent HTML full read) | arXiv:2604.23553v1 §Evaluation — Evaluation Contract — Experimental Setup (source artifact papers/2026/04/_sources/daily-20260427/exact-v1/2604.23553v1.html#exact-v1 independent HTML full read) | arXiv:2604.23553v1 §Scope and Limitations — Evidence Proves / Does Not Prove — 5 Conclusion (source artifact papers/2026/04/_sources/daily-20260427/exact-v1/2604.23553v1.html#exact-v1 independent HTML full read) | arXiv:2604.23553v1 §Artifact / Access — Artifact / Access — Appendix A Team Work as a class project (source artifact papers/2026/04/_sources/daily-20260427/exact-v1/2604.23553v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-23553 | complete |
| SF-2026-ARXIV-2604-23577 | RP-8e41d31087f46e3a | deep | arXiv:2604.23577v1 | SRC-ARXIV@arXiv:2604.23577v1 | arXiv:2604.23577v1 §Method / Identity — Mechanism / State Ownership (source artifact papers/2026/04/_sources/daily-20260427/exact-v1/2604.23577v1.html#exact-v1 independent HTML full read) | arXiv:2604.23577v1 §Evaluation — Evaluation Contract — 5.3 Human Evaluation (source artifact papers/2026/04/_sources/daily-20260427/exact-v1/2604.23577v1.html#exact-v1 independent HTML full read) | arXiv:2604.23577v1 §Scope and Limitations — Evidence Proves / Does Not Prove — Limitations (source artifact papers/2026/04/_sources/daily-20260427/exact-v1/2604.23577v1.html#exact-v1 independent HTML full read) | arXiv:2604.23577v1 §Artifact / Access — Artifact / Access — Appendix F Benchmark Data Provenance (source artifact papers/2026/04/_sources/daily-20260427/exact-v1/2604.23577v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-23577 | complete |
| SF-2026-ARXIV-2604-23581 | RP-0589969feac51fd8 | deep | arXiv:2604.23581v1 | SRC-ARXIV@arXiv:2604.23581v1 | arXiv:2604.23581v1 §Method / Identity — Mechanism / State Ownership (source artifact papers/2026/04/_sources/daily-20260427/exact-v1/2604.23581v1.html#exact-v1 independent HTML full read) | arXiv:2604.23581v1 §Evaluation — Evaluation Contract — Agent Evaluation and Process Supervision. (source artifact papers/2026/04/_sources/daily-20260427/exact-v1/2604.23581v1.html#exact-v1 independent HTML full read) | arXiv:2604.23581v1 §Scope and Limitations — Evidence Proves / Does Not Prove — 7 Conclusion (source artifact papers/2026/04/_sources/daily-20260427/exact-v1/2604.23581v1.html#exact-v1 independent HTML full read) | arXiv:2604.23581v1 §Artifact / Access — Artifact / Access — Appendix L Regression Case Studies (source artifact papers/2026/04/_sources/daily-20260427/exact-v1/2604.23581v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-23581 | complete |
| SF-2026-ARXIV-2604-23584 | RP-989d9f048da65534 | deep | arXiv:2604.23584v1 | SRC-ARXIV@arXiv:2604.23584v1 | https://arxiv.org/html/2604.23584v1 §Method/Architecture (official exact-v1 rendered full read) | https://arxiv.org/html/2604.23584v1 §Evaluation/Experiments (official exact-v1 rendered full read) | https://arxiv.org/html/2604.23584v1 §Limitations/Discussion plus disclosed evaluation scope | https://arxiv.org/abs/2604.23584v1 ; https://arxiv.org/html/2604.23584v1 | claim:SF-2026-ARXIV-2604-23584 | complete |
| SF-2026-ARXIV-2604-23626 | RP-7a1e90a53daf2033 | deep | arXiv:2604.23626v1 | SRC-ARXIV@arXiv:2604.23626v1 | arXiv:2604.23626v1 §Method / Identity — Artifact / Access — Appendix C Implementation Details (source artifact papers/2026/04/_sources/daily-20260427/exact-v1/2604.23626v1.html#exact-v1 independent HTML full read) | arXiv:2604.23626v1 §Evaluation — Evaluation Contract — 4 Experiments (source artifact papers/2026/04/_sources/daily-20260427/exact-v1/2604.23626v1.html#exact-v1 independent HTML full read) | arXiv:2604.23626v1 §Scope and Limitations — Evidence Proves / Does Not Prove — 5 Conclusion (source artifact papers/2026/04/_sources/daily-20260427/exact-v1/2604.23626v1.html#exact-v1 independent HTML full read) | arXiv:2604.23626v1 §Artifact / Access — Artifact / Access — Appendix C Implementation Details (source artifact papers/2026/04/_sources/daily-20260427/exact-v1/2604.23626v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-23626 | complete |
| SF-2026-ARXIV-2604-23646 | RP-82c46950098b2172 | deep | arXiv:2604.23646v1 | SRC-ARXIV@arXiv:2604.23646v1 | arXiv:2604.23646v1 §Method / Identity — Mechanism / State Ownership (source artifact papers/2026/04/_sources/daily-20260427/exact-v1/2604.23646v1.html#exact-v1 independent HTML full read) | arXiv:2604.23646v1 §Evaluation — Evaluation Contract — 5.1 Evaluation Overview (source artifact papers/2026/04/_sources/daily-20260427/exact-v1/2604.23646v1.html#exact-v1 independent HTML full read) | arXiv:2604.23646v1 §Scope and Limitations — Evidence Proves / Does Not Prove — 6.3 Limitations of Goal Integrity ( T 6 T_{6} ) (source artifact papers/2026/04/_sources/daily-20260427/exact-v1/2604.23646v1.html#exact-v1 independent HTML full read) | arXiv:2604.23646v1 §Artifact / Access — Artifact / Access — 3.1 Overview (source artifact papers/2026/04/_sources/daily-20260427/exact-v1/2604.23646v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-23646 | complete |
| SF-2026-ARXIV-2604-23711 | RP-bed50c0e5b24af54 | deep | arXiv:2604.23711v1 | SRC-ARXIV@arXiv:2604.23711v1 | arXiv:2604.23711v1 §Method / Identity — Mechanism / State Ownership (source artifact papers/2026/04/_sources/daily-20260427/exact-v1/2604.23711v1.html#exact-v1 independent HTML full read) | arXiv:2604.23711v1 §Evaluation — Evaluation Contract — 4.1 Experimental Setup (source artifact papers/2026/04/_sources/daily-20260427/exact-v1/2604.23711v1.html#exact-v1 independent HTML full read) | arXiv:2604.23711v1 §Scope and Limitations — Evidence Proves / Does Not Prove — 7 Limitations (source artifact papers/2026/04/_sources/daily-20260427/exact-v1/2604.23711v1.html#exact-v1 independent HTML full read) | arXiv:2604.23711v1 §Artifact / Access — Artifact / Access — Appendix A Combination with Existing Attack Methods (source artifact papers/2026/04/_sources/daily-20260427/exact-v1/2604.23711v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-23711 | complete |
| SF-2026-ARXIV-2604-23747 | RP-385fc6cdf41a279c | deep | arXiv:2604.23747v1 | SRC-ARXIV@arXiv:2604.23747v1 | arXiv:2604.23747v1 §Method / Identity — Mechanism / State Ownership (source artifact papers/2026/04/_sources/daily-20260427/exact-v1/2604.23747v1.html#exact-v1 independent HTML full read) | arXiv:2604.23747v1 §Evaluation — Evaluation Contract — 3 Experimental Setup (source artifact papers/2026/04/_sources/daily-20260427/exact-v1/2604.23747v1.html#exact-v1 independent HTML full read) | arXiv:2604.23747v1 §Scope and Limitations — Evidence Proves / Does Not Prove — 6 Conclusion and Limitations (source artifact papers/2026/04/_sources/daily-20260427/exact-v1/2604.23747v1.html#exact-v1 independent HTML full read) | arXiv:2604.23747v1 §Artifact / Access — Artifact / Access — Appendix B FLOPs Calculation Details (source artifact papers/2026/04/_sources/daily-20260427/exact-v1/2604.23747v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-23747 | complete |
| SF-2026-ARXIV-2604-23758 | RP-deb2a27a4b9e5ae6 | deep | arXiv:2604.23758v1 | SRC-ARXIV@arXiv:2604.23758v1 | arXiv:2604.23758v1 §Method / Identity — Mechanism / State Ownership (source artifact papers/2026/04/_sources/daily-20260427/exact-v1/2604.23758v1.html#exact-v1 independent HTML full read) | arXiv:2604.23758v1 §Evaluation — Evaluation Contract — 4.9 Evaluation Metrics (source artifact papers/2026/04/_sources/daily-20260427/exact-v1/2604.23758v1.html#exact-v1 independent HTML full read) | arXiv:2604.23758v1 §Scope and Limitations — Evidence Proves / Does Not Prove — Appendix G Comparison and Discussion (source artifact papers/2026/04/_sources/daily-20260427/exact-v1/2604.23758v1.html#exact-v1 independent HTML full read) | arXiv:2604.23758v1 §Artifact / Access — Artifact / Access — Appendix G Comparison and Discussion (source artifact papers/2026/04/_sources/daily-20260427/exact-v1/2604.23758v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-23758 | complete |
| SF-2026-ARXIV-2604-23775 | RP-12d35995701b1681 | deep | arXiv:2604.23775v1 | SRC-ARXIV@arXiv:2604.23775v1 | arXiv:2604.23775v1 §Method / Identity — Mechanism / State Ownership (source artifact papers/2026/04/_sources/daily-20260427/exact-v1/2604.23775v1.html#exact-v1 independent HTML full read) | arXiv:2604.23775v1 §Evaluation — Evaluation Contract — 5.3 Evaluation and Benchmarks (source artifact papers/2026/04/_sources/daily-20260427/exact-v1/2604.23775v1.html#exact-v1 independent HTML full read) | arXiv:2604.23775v1 §Scope and Limitations — Evidence Proves / Does Not Prove — 9 Conclusion (source artifact papers/2026/04/_sources/daily-20260427/exact-v1/2604.23775v1.html#exact-v1 independent HTML full read) | arXiv:2604.23775v1 §Artifact / Access — Artifact / Access — Visual encoder. (source artifact papers/2026/04/_sources/daily-20260427/exact-v1/2604.23775v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-23775 | complete |
| SF-2026-ARXIV-2604-23781 | RP-7c3f3069280f9010 | deep | arXiv:2604.23781v1 | SRC-ARXIV@arXiv:2604.23781v1 | arXiv:2604.23781v1 §Method / Identity — Mechanism / State Ownership (source artifact papers/2026/04/_sources/daily-20260427/exact-v1/2604.23781v1.html#exact-v1 independent HTML full read) | arXiv:2604.23781v1 §Evaluation — Evaluation Contract — 2.1 Agent benchmarks (source artifact papers/2026/04/_sources/daily-20260427/exact-v1/2604.23781v1.html#exact-v1 independent HTML full read) | arXiv:2604.23781v1 §Scope and Limitations — Evidence Proves / Does Not Prove — 7 Conclusion (source artifact papers/2026/04/_sources/daily-20260427/exact-v1/2604.23781v1.html#exact-v1 independent HTML full read) | arXiv:2604.23781v1 §Artifact / Access — Artifact / Access — Appendix A Multi-turn evaluation: terminology and conventions (source artifact papers/2026/04/_sources/daily-20260427/exact-v1/2604.23781v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-23781 | complete |
| SF-2026-ARXIV-2604-23798 | RP-0b1a5d4899979aea | deep | arXiv:2604.23798v1 | SRC-ARXIV@arXiv:2604.23798v1 | arXiv:2604.23798v1 §Method / Identity — Artifact / Access — Implementation and Experimental Setup. (source artifact papers/2026/04/_sources/daily-20260427/exact-v1/2604.23798v1.html#exact-v1 independent HTML full read) | arXiv:2604.23798v1 §Evaluation — Evaluation Contract — Benchmarks and Scalability on Synthetic Sequences. (source artifact papers/2026/04/_sources/daily-20260427/exact-v1/2604.23798v1.html#exact-v1 independent HTML full read) | arXiv:2604.23798v1 §Scope and Limitations — Evidence Proves / Does Not Prove — Limitations. (source artifact papers/2026/04/_sources/daily-20260427/exact-v1/2604.23798v1.html#exact-v1 independent HTML full read) | arXiv:2604.23798v1 §Artifact / Access — Artifact / Access — Implementation and Experimental Setup. (source artifact papers/2026/04/_sources/daily-20260427/exact-v1/2604.23798v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-23798 | complete |
| SF-2026-ARXIV-2604-23831 | RP-147c0491e9fe8249 | deep | arXiv:2604.23831v1 | SRC-ARXIV@arXiv:2604.23831v1 | https://arxiv.org/html/2604.23831v1 §Method/Architecture (official exact-v1 rendered full read) | https://arxiv.org/html/2604.23831v1 §Evaluation/Experiments (official exact-v1 rendered full read) | https://arxiv.org/html/2604.23831v1 §Limitations/Discussion plus disclosed evaluation scope | https://arxiv.org/abs/2604.23831v1 ; https://arxiv.org/html/2604.23831v1 | claim:SF-2026-ARXIV-2604-23831 | complete |
| SF-2026-ARXIV-2604-23838 | RP-8a079c698e48c95d | deep | arXiv:2604.23838v1 | SRC-ARXIV@arXiv:2604.23838v1 | https://arxiv.org/html/2604.23838v1 §Method / Architecture / Framework (official exact-v1 full read) | https://arxiv.org/html/2604.23838v1 §Experiments / Evaluation / Results (official exact-v1 full read) | https://arxiv.org/html/2604.23838v1 §Discussion / Limitations / Conclusion (official exact-v1 full read; no broader claim inferred where a dedicated heading is absent) | https://arxiv.org/abs/2604.23838v1 ; https://arxiv.org/html/2604.23838v1 | claim:SF-2026-ARXIV-2604-23838 | complete |
| SF-2026-ARXIV-2604-23853 | RP-cbfc3914c6e897f0 | deep | arXiv:2604.23853v1 | SRC-ARXIV@arXiv:2604.23853v1 | https://arxiv.org/html/2604.23853v1 §Method / Architecture / Framework (official exact-v1 full read) | https://arxiv.org/html/2604.23853v1 §Experiments / Evaluation / Results (official exact-v1 full read) | https://arxiv.org/html/2604.23853v1 §Discussion / Limitations / Conclusion (official exact-v1 full read; no broader claim inferred where a dedicated heading is absent) | https://arxiv.org/abs/2604.23853v1 ; https://arxiv.org/html/2604.23853v1 | claim:SF-2026-ARXIV-2604-23853 | complete |
| SF-2026-ARXIV-2604-23887 | RP-79b1d51e757c54e3 | deep | arXiv:2604.23887v1 | SRC-ARXIV@arXiv:2604.23887v1 | https://arxiv.org/html/2604.23887v1 §Method / Architecture / Framework (official exact-v1 full read) | https://arxiv.org/html/2604.23887v1 §Experiments / Evaluation / Results (official exact-v1 full read) | https://arxiv.org/html/2604.23887v1 §Discussion / Limitations / Conclusion (official exact-v1 full read; no broader claim inferred where a dedicated heading is absent) | https://arxiv.org/abs/2604.23887v1 ; https://arxiv.org/html/2604.23887v1 | claim:SF-2026-ARXIV-2604-23887 | complete |
| SF-2026-ARXIV-2607-05397 | RP-e63a9a60faf89b90 | deep | arXiv:2607.05397v1 | SRC-ARXIV@arXiv:2607.05397v1 | https://arxiv.org/html/2607.05397v1 §Method/Architecture (official exact-v1 rendered full read) | https://arxiv.org/html/2607.05397v1 §Evaluation/Experiments (official exact-v1 rendered full read) | https://arxiv.org/html/2607.05397v1 §Limitations/Discussion plus disclosed evaluation scope | https://arxiv.org/abs/2607.05397v1 ; https://arxiv.org/html/2607.05397v1 | claim:SF-2026-ARXIV-2607-05397 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2604-23488:start -->
#### Do Prompt-Elicited Trajectories Reflect Training-Time Reward Hacking? A Systematic Study on Monitoring Training-Time Reward Hacking in Code Generation

问题、旧路径与约束变化：旧路径把 `Do Prompt-Elicited Trajectories Reflect Training-Time Reward Hacking? A Systematic Study on Monitoring Training-Time Reward Hacking in Code Generation` 的判断留给固定策略、单次离线分数或未显式版本化的运行状态。

机制与 state/control owner：Reward hacking in code generation, where models exploit evaluation loopholes to obtain high reward without correctly solving the intended task, poses a critical challenge for Reinforcement Learning (RL) and the deployment of reasoning models. Existing studies often rely on explicitly prompted hacking trajectories, but it remains unclear whether monitors trained on such data can detect reward hacks that arise without direct hacking instructions during RL training. In this work, we introduce Trace-and-Amplify, a framework for scalable curation of reward-hacking trajectories that arise during RL training without explicit hacking instructions. 该机制将长期 owner 定位到 `PLATFORM-EVALUATION-SYSTEM`，并把相应 state/control/evidence identity 从隐式约定变成可检查对象。

Evaluation contract：Reward hacking in code generation, where models exploit evaluation loopholes to obtain high reward without correctly solving the intended task, poses a critical challenge for Reinforcement Learning (RL) and the deployment of reasoning models. The framework uses unit-test tracers to identify hacking solutions when they occur and retains such trajectories for monitor training and evaluation. Through controlled comparisons between monitors trained on prompt-elicited hacking trajectories and training-time reward-hacking trajectories collected by Trace-and-Amplify, we find that \textbf{(1) prompt-elicited-data-trained monitors often fail to generalize to trajectories curated by our framework}, and \textbf{(2) monitors trained on our Trace-and-Amplify trajectories demonstrate stronger generalizability to unseen hacking types}.

Trade-off / failure / fallback / coexistence：论文只在 exact-v1 披露的任务、模型与实验协议内支持上述结论；`Do Prompt-Elicited Trajectories Reflect Training-Time Reward Hacking? A Systematic Study on Monitoring Training-Time Reward Hacking in Code Generation` 不证明跨模型、跨硬件、跨数据分布或生产 SLO 的普遍收益。失配时回退 current Books 的既有路径，并保留新旧机制并存。

<!-- claim:SF-2026-ARXIV-2604-23488:start -->只接受 arXiv:2604.23488v1 的作者机制与实验；未披露硬件、precision、长度、batch、并发、成本或线上 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2604-23488:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-23488:end -->
<!-- review:SF-2026-ARXIV-2604-23505:start -->
#### Uncertainty Propagation in LLM-Based Systems

问题、旧路径与约束变化：旧路径把 `Uncertainty Propagation in LLM-Based Systems` 的判断留给固定策略、单次离线分数或未显式版本化的运行状态。

机制与 state/control owner：Uncertainty in large language model (LLM)-based systems is often studied at the level of a single model output, yet deployed LLM applications are compound systems in which uncertainty is transformed and reused across model internals, workflow stages, component boundaries, persistent state, and human or organisational processes. Without principled treatment of how uncertainty is carried and reused across these boundaries, early errors can propagate and compound in ways that are difficult to detect and govern. This paper develops a systems-level account of uncertainty propagation. 该机制将长期 owner 定位到 `PLATFORM-EVALUATION-SYSTEM`，并把相应 state/control/evidence identity 从隐式约定变成可检查对象。

Evaluation contract：Exact-v1 evaluation is bounded to the author-disclosed protocol and artifacts.

Trade-off / failure / fallback / coexistence：论文只在 exact-v1 披露的任务、模型与实验协议内支持上述结论；`Uncertainty Propagation in LLM-Based Systems` 不证明跨模型、跨硬件、跨数据分布或生产 SLO 的普遍收益。失配时回退 current Books 的既有路径，并保留新旧机制并存。

<!-- claim:SF-2026-ARXIV-2604-23505:start -->只接受 arXiv:2604.23505v1 的作者机制与实验；未披露硬件、precision、长度、batch、并发、成本或线上 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2604-23505:end -->

Books Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2604-23505:end -->
<!-- review:SF-2026-ARXIV-2604-23543:start -->
#### Pref-CTRL: Preference Driven LLM Alignment using Representation Editing

问题、旧路径与约束变化：旧路径未显式拥有 `TRAIN-DPO` 中该 family 的受限状态。

机制与 state/control owner：The value function is trained on the extracted hidden states from the LLM. The training objective includes RE-Control’s reward regression loss and our proposed margin and regularizer losses. The additional proposed losses utilize the hidden states of the preferred and rejected responses from the datasets. Table 5 reports the hyperparameters used to train the value function. We follow the same strategy for training across our proposed models and all baselines. For evaluation, we choose the best validation epoch and use it for inference. preference data owner 拥有 pair/label provenance，trainer 拥有 objective，judge 不拥有最终 policy commit

Evaluation contract：Results & Analysis. Table 1 summarizes the performance of our Pref-CTRL variants, RE-Control, and the training-time DPO baseline across SHP and HH-RLHF. Across both datasets and models, Pref-CTRL consistently outperforms RE-Control. On SHP, Vicuna-7B with the margin loss increases the win rate from 66.80% to 72.20% (Llama), 66.70% to 67.60% (DeepSeek). Adding the regularizer further improves it to 73.50% (Llama), 70.00% (DeepSeek), and 53.70% (GPT). A regularizer-only ablation showed no performance gains and is therefore omitted. Hermes3-8B shows similar trends, with win rates rising from 79.80% to 80.40% (Llama), 74.80% to 76.40% (DeepSeek), and 60.90% to 61.40% (GPT) when combining margin and regularizer. On HH-RLHF, Vicuna-7B achieves 82.90% (Llama), 85.60% (DeepSeek), and 74.60% (GPT), while Hermes3-8B reaches 86.70% (Llama), 84.30% (DeepSeek), and 73.60% (GPT). This demonstrates the strong alignment effectiveness of our proposed approach, while preserving good diversity and coherence. Although DPO has yielded strong scores thanks to being a training-time approach, our models have still performed closely, which is a remarkable result for a test-time approach.

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：In this work, we proposed Pref-CTRL, a test-time alignment framework that improves representation editing with preference-aware training objectives. Experimental results have shown that Pref-CTRL consistently performs better than RE-Control and matches the performance of a strong fine-tuned baseline such as DPO. It also demonstrates strong generalization to out-of-domain datasets. In future work, we aim to experiment with an attention-based value function architecture, multi-attribute alignment objectives, and adaptive test-time intervention techniques.。因此若该限制在目标 workload 中触发，不能把 `Pref-CTRL: Preference Driven LLM Alignment using Representation Editing` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-23543:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-23543:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-23543:end -->
<!-- review:SF-2026-ARXIV-2604-23553:start -->
#### ClusterFusion++: Expanding Cluster-Level Fusion to Full Transformer-Block Decoding

问题、旧路径与约束变化：旧路径未显式拥有 `INFER-DECODE` 中该 family 的受限状态。

机制与 state/control owner：Building upon ClusterFusion’s attention-side fusion, ClusterFusion++ extends the fused region to cover the entire decoder block for GPT-NeoX/Pythia architectures. A single kernel invocation performs: Pre-attention LayerNorm → \rightarrow QKV projection and KV cache update → \rightarrow Rotary position embedding (RoPE) → \rightarrow Decode attention over KV cache → \rightarrow Output projection with residual connection → \rightarrow Post-attention LayerNorm → \rightarrow MLP (up-projection, GELU, down-projection) with residual connection . decoder runtime 拥有 token frontier、cache identity 与 commit order

Evaluation contract：We evaluate ClusterFusion++ on an NVIDIA RTX 5090-class GPU ( sm_120 ) using Pythia-2.8B and Pythia-6.9B models (GPT-NeoX). Sequence length ranges from 16 to 2048, and batch size is 1. All experiments use PyTorch 2.9.1 and CUDA 13.1. Our baseline is HuggingFace Transformers decoding with KV cache enabled. We evaluate ClusterFusion++ on two models: Pythia-2.8B and Pythia-6.9B, both based on the GPT-NeoX architecture.

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：ClusterFusion++ presents a CUDA-level cluster-centric fusion approach that expands ClusterFusion-style decoding fusion from attention-side operators to the full Transformer decoder block for GPT-NeoX/Pythia, enabling on-chip inter-block collectives via distributed shared memory to reduce intermediate global-memory traffic and launch overhead. Combined with a CUDA-Graph mode that reuses persistent TensorMap (TMA) descriptors and static buffers across decode steps, ClusterFusion++ outperforms the HuggingFace baseline on an RTX 5090 GPU across different configurations and models, while maintaining high output fidelity with only minor non-determinism attributable to FP16 atomic accumulation in cluster reductions.。因此若该限制在目标 workload 中触发，不能把 `ClusterFusion++: Expanding Cluster-Level Fusion to Full Transformer-Block Decoding` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-23553:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-23553:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-23553:end -->
<!-- review:SF-2026-ARXIV-2604-23577:start -->
#### RouteNLP: Closed-Loop LLM Routing with Conformal Cascading and Distillation Co-Optimization

问题、旧路径与约束变化：旧路径未显式拥有 `INFER-SCHEDULING` 中该 family 的受限状态。

机制与 state/control owner：The router uses DistilBERT-base-uncased (66M parameters) with a 2-layer MLP routing head per task family. The first layer projects concatenated [CLS] + task embedding ( 768 + 64 = 832 768+64=832 ) to 256 dimensions with ReLU and 0.1 dropout. The second projects to K = 4 K=4 logits. Training: AdamW, lr 2 × 10 − 5 2\times 10^{-5} , batch 64, 10 epochs, early stopping (patience 3). Total: ∼ {\sim} 67M parameters, ∼ {\sim} 45 min on A100. scheduler 拥有队列、priority 与 resource reservation，model/kernel 不自行决定 admission

Evaluation contract：We evaluate CS Response Generation and Financial Summarization on 200 samples each, rated by 3 domain experts on factual accuracy, completeness, fluency, and helpfulness (5-point Likert), plus win/tie/loss vs. Always-T4.

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：(1) Pilot deployment covers only customer service ( ∼ {\sim} 5K queries/day, 8 weeks); finance and legal claims rely on benchmark simulation. (2) The benchmark adapts public datasets with enterprise annotations rather than proprietary data. (3) The co-optimization loop ran on benchmark data, not production failure logs. (4) The pilot was a shadow deployment without A/B testing. (5) Conformal coverage degrades under distribution shift (up to 8.1% violations vs. 5% target). (6) English-only evaluation. (7) BERTScore proxy agreement with humans (84–87%) is not verified under domain shift. (8) Cost savings depend on cost structures; baseline adaptation may not fully preserve 2-model inductive biases.…。因此若该限制在目标 workload 中触发，不能把 `RouteNLP: Closed-Loop LLM Routing with Conformal Cascading and Distillation Co-Optimization` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-23577:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-23577:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-23577:end -->
<!-- review:SF-2026-ARXIV-2604-23581:start -->
#### AgentEval: DAG-Structured Step-Level Evaluation for Agentic Workflows with Error Propagation Tracking

问题、旧路径与约束变化：旧路径未显式拥有 `PLATFORM-EVALUATION-SYSTEM` 中该 family 的受限状态。

机制与 state/control owner：AgentEval comprises four integrated components: (1) a formal DAG representation for agent workflows, (2) step-level quality metrics evaluated via calibrated LLM-as-judge, (3) a hierarchical failure taxonomy, and (4) an automated regression suite. Figure 1 provides an architectural overview. EvalSpec owner 冻结 subject/data/scorer，release owner 依据 run evidence 作决定

Evaluation contract：Agent evaluation benchmarks have proliferated ( Liu et al., 2024 ; Jimenez et al., 2024 ; Zhou et al., 2024b ; Yao et al., 2024 ; Ma et al., 2024 ) , with LATS ( Zhou et al., 2024a ) providing per-step value estimates for planning. However, a recent survey ( Yehudai et al., 2025 ) identifies a critical gap: existing benchmarks evaluate agent capabilities in controlled settings, whereas deployment requires evaluation infrastructure with continuous monitoring, regression detection, and CI/CD integration. The process supervision literature demonstrates that evaluating intermediate steps outperforms outcome-only evaluation ( Lightman et al., 2024 ; Uesato et al., 2022 ) , while Cemri et al. (2025) and Zhu et al. (2025) show that error propagation is the primary bottleneck in agent performance. The LLM-as-judge paradigm ( Liu et al., 2023 ; Zheng et al., 2023 ) enables scalable evaluation with > > 80% human agreement.

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：We presented AgentEval , an evaluation infrastructure that formalizes agent workflows as evaluation DAGs with step-level quality metrics, a hierarchical failure taxonomy, and automated regression testing. On three production workflows with predominantly sequential architectures, AgentEval achieves 2.17 × 2.17\times higher failure detection recall than end-to-end evaluation, κ = 0.84 \kappa=0.84 human agreement, and 72% root cause accuracy approaching the human ceiling (81%). The ablation study confirms DAG-based dependency modeling as the single most impactful component, an advantage that grows with workflow complexity and holds across four judge models.…。因此若该限制在目标 workload 中触发，不能把 `AgentEval: DAG-Structured Step-Level Evaluation for Agentic Workflows with Error Propagation Tracking` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-23581:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-23581:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-23581:end -->
<!-- review:SF-2026-ARXIV-2604-23626:start -->
#### GraphPlanner: Graph Memory-Augmented Agentic Routing for Multi-Agent LLMs

问题、旧路径与约束变化：旧路径未显式拥有 `AGENT-PLANNING` 中该 family 的受限状态。

机制与 state/control owner：We optimize the heterogeneous graph-based policy network using Proximal Policy Optimization (PPO) ( Schulman et al., 2017 ) , a widely used actor–critic reinforcement learning algorithm. PPO trains the policy by maximizing: planner 拥有可修订 plan state，executor 只提交有证据的 step result

Evaluation contract：agentic routing within the user-predefined LLM workflows. In this phase, we specify different widths and depths for agentic workflows. The task is: given a query, different routers are expected to optimize the choice of LLM backbones for different agents. In particular, we conduct experiments mainly under two settings: Depth = 1, Width = 3 and Depth = 2, Width = 2. Here, depth refers to the number of planners, and width denotes the maximum number of sub-queries that each planner is allowed to decompose. Phase 2 Evaluation focuses on generating optimal workflows. Here, given a query, different routers are expected to simultaneously optimize both the agent selections and the corresponding LLM backbones. Baselines and metrics. We evaluate a variety of baseline methods across 6 scenarios. The baselines are categorized into two groups: (a) Single-round routers that route a query by calling an LLM once, and (b) Multi-round routers that solve a query by calling multiple LLMs. For all routers, following previous work ( Feng et al., 2025 ) , we use Acc and Cost to evaluate routing performance. Here, Acc refers to the task-specific evaluation metric introduced in Table 9 of the Appendix. Cost is calculated with the number of input tokens and output tokens and the cost of different LLMs in Table 10 of the Appendix. Here we utilize GPT-2 as in ( Feng et al., 2024 ) to calculate the number of tokens. Specifically, we have: (a) Single-round routers. We consider five representative single-round routers: 1) RouterKNN ( Shnitzer et al., 2023 ) , a non-parametric baseline that assigns a quer

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：We introduced GraphPlanner , a heterogeneous graph-based multi-agent router that casts routing as workflow generation within an MDP, leveraging the heterogeneous graph GARNet to integrate historical and workflow memories and training the policy via reinforcement learning. Extensive experiments across 14 tasks and 6 domains show that GraphPlanner delivers state-of-the-art performance, robust generalization to unseen tasks and LLMs, and favorable trade-offs between accuracy and computational cost. These results underscore the potential of extending LLM routing into agentic settings and open new directions for scalable, cooperative multi-agent LLM systems.…。因此若该限制在目标 workload 中触发，不能把 `GraphPlanner: Graph Memory-Augmented Agentic Routing for Multi-Agent LLMs` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-23626:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-23626:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-23626:end -->
<!-- review:SF-2026-ARXIV-2604-23646:start -->
#### Structural Enforcement of Goal Integrity in AI Agents via Separation-of-Powers Architecture

问题、旧路径与约束变化：旧路径未显式拥有 `PLATFORM-SECURITY` 中该 family 的受限状态。

机制与 state/control owner：ProVerif and Tamarin support protocol verification in symbolic Dolev-Yao models; PEA’s adversary model is a restricted Dolev-Yao model directly modelable in ProVerif as future work. TLA+ (Lamport) provides temporal logic for concurrent systems; PEA’s M = ( S , C , Q ) M=(S,C,Q) and Step function are directly expressible in TLA+, which would handle liveness properties complementing the Coq safety proof. Coq and Agda provide dependent type proof assistants; the PEA Intent Type System maps directly to Coq’s type theory, with Section 4 as the primary verification target. policy/CI/sandbox 拥有 invariant 与 commit authority，model 仅提出不可信 proposal

Evaluation contract：We empirically evaluate the PEA architecture along three dimensions corresponding to its core security claims. While the formal guarantees of PEA are conditional on assumptions A1–A12, we operationalize several of these assumptions as testable system invariants and validate them under adversarial conditions. This converts the guarantee structure from “assumed and asserted” to “conditionally formal + empirically bounded.”

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：Adversarial semantic alignment. The adversarial attack T 6 T_{6} cannot fully close is adversarial semantic alignment: a construction achieving high similarity score while encoding a semantically divergent goal. The E2 evaluation demonstrates a 6.9% residual success rate under θ drift = 0.82 \theta_{\text{drift}}=0.82 . This residual cannot be driven to zero by threshold adjustment alone—stricter thresholds increase false positive rate on legitimate multi-step tasks.。因此若该限制在目标 workload 中触发，不能把 `Structural Enforcement of Goal Integrity in AI Agents via Separation-of-Powers Architecture` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-23646:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-23646:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-23646:end -->
<!-- review:SF-2026-ARXIV-2604-23711:start -->
#### Spore: Efficient and Training-Free Privacy Extraction Attack on LLMs via Inference-Time Hybrid Probing

问题、旧路径与约束变化：旧路径未显式拥有 `PLATFORM-SECURITY` 中该 family 的受限状态。

机制与 state/control owner：Existing studies mainly focus on the threat from a single attack, while overlooking the amplified threat that emerges when multiple attacks with different goals are combined. We propose a privacy extraction pipeline that combines several existing attack methods and attack stages ( Cui et al., 2026 ) , as shown in Algorithm 2 . This pipeline covers canonical attack strategies at different stages of privacy extraction, including prompt injection attacks (PIA) ( Yi et al., 2025 ; Chen et al., 2025a ; Shi et al., 2024a ) , membership inference attacks (MIA) ( Wen et al., 2024 ) , and our Spore . It spans the full process, from inducing the user to disclose PII during interaction with the LLM agent, to determining whether partially sensitive privacy information exists in the context, and then to extracting highly sensitive PII based on the obtained weakly sensitive privacy. This pipeline provides a reference for studying inference-time contextual privacy risks in LLM agent memory. policy/CI/sandbox 拥有 invariant 与 commit authority，model 仅提出不可信 proposal

Evaluation contract：Datasets . We leverage the full TrustLLM dataset ( Huang et al., 2024 ) to construct realistic contexts containing sensitive information. The TrustLLM dataset comprises 560 privacy-related queries spanning diverse scenarios and seven categories of sensitive information, including social security numbers, bank account numbers, driver license numbers, phone numbers, phone passwords, SSH keys, and addresses ( Wang et al., 2025b ) .

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：We evaluate multiple frontier LLMs with strong safety alignment and SOTA performance on safety benchmarks. However, resource constraints limit evaluation on a broader set of models. In addition, although our method achieves token consumption comparable to the most efficient existing approach, further optimization remains necessary. Moreover, although we have comprehensively evaluated Spore under existing defenses, these methods cannot fully mitigate its security risks. We plan to investigate more effective defenses against Spore in future work.。因此若该限制在目标 workload 中触发，不能把 `Spore: Efficient and Training-Free Privacy Extraction Attack on LLMs via Inference-Time Hybrid Probing` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-23711:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-23711:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-23711:end -->
<!-- review:SF-2026-ARXIV-2604-23747:start -->
#### SFT-then-RL Outperforms Mixed-Policy Methods for LLM Reasoning

问题、旧路径与约束变化：旧路径未显式拥有 `TRAIN-SFT` 中该 family 的受限状态。

机制与 state/control owner：We identify two bugs in widely used open-source training frameworks that silently degrade SFT quality. Both are triggered by distributed training configurations, making them difficult to detect without cross-framework validation. dataset owner 拥有 trajectory/evidence，trainer 拥有 loss 与 checkpoint commit

Evaluation contract：We reproduce the SFT baselines and mixed-policy methods under controlled conditions to isolate the impact of the bugs described in Section 2 . All methods share the same base model, dataset, and evaluation protocol, which we detail below before describing the method-specific setups.

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：We have shown that the reported gains of mixed-policy optimization methods for LLM reasoning trace back to deflated baselines rather than methodological innovation. A CPU-offloaded optimizer bug in DeepSpeed silently drops intermediate micro-batches during gradient accumulation, affecting downstream frameworks including TRL , OpenRLHF and Llama-Factory ; fixing it alone recovers most of the gap. A second loss aggregation bug in OpenRLHF incorrectly weights per-mini-batch losses and, on top of adding training instability, contributes a further measurable degradation. Together the two fixes close the gap to the independently implemented verl baseline.。因此若该限制在目标 workload 中触发，不能把 `SFT-then-RL Outperforms Mixed-Policy Methods for LLM Reasoning` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-23747:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-23747:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-23747:end -->
<!-- review:SF-2026-ARXIV-2604-23758:start -->
#### Agentic Fusion of Large Atomic and Language Models to Accelerate Superconductor Discovery

问题、旧路径与约束变化：旧路径未显式拥有 `AGENT-WORKFLOW` 中该 family 的受限状态。

机制与 state/control owner：Our model, Elements , builds upon the foundational architecture of EquiformerV2 ( Liao et al., 2023 ) , which we substantially adapt for the comprehensive modeling of both molecular and crystalline structures. As illustrated in the architecture diagram ( Fig. 1 a), the overall pipeline consists of Graph Construction, Embedding, stacked Equivariant Message Passing layers, and task-specific output heads. workflow runtime 拥有 event、checkpoint 与 transition control，model 只提出下一步

Evaluation contract：Root Mean Square Error (RMSE). We use RMSE to evaluate both structural geometric fidelity, and the accuracy of energy/force predictions on the DPA-2 dataset, with distinct formulations below:

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：Cartesian vs. Fractional Diffusion: A key distinction lies in the coordinate space of the diffusion process. While MatterGen employs a Cartesian-based backbone (GemNet) but performs diffusion and denoising on fractional coordinates, our model operates the diffusion dynamics directly in the Cartesian coordinate system . This approach unifies the treatment of atomic positions with lattice deformations. We do not enforce periodic boundary conditions during the intermediate diffusion steps; instead, the conversion from Cartesian to fractional coordinates (and the subsequent wrapping into the unit cell) is performed only at the final sampling step ( t = 0 t=0 ).。因此若该限制在目标 workload 中触发，不能把 `Agentic Fusion of Large Atomic and Language Models to Accelerate Superconductor Discovery` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-23758:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-23758:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-23758:end -->
<!-- review:SF-2026-ARXIV-2604-23775:start -->
#### Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms

问题、旧路径与约束变化：旧路径未显式拥有 `MULTIMODAL-EMBODIED-VLA` 中该 family 的受限状态。

机制与 state/control owner：Current VLA training pipelines are dominated by behavior cloning on demonstrations where safety is implicit rather than explicit, leaving the learner vulnerable to the data poisoning and backdoor attacks surveyed in Section 3 . Several paradigms deserve deeper investigation: safety-constrained policy optimization that encodes safety as explicit constraints during fine-tuning [ 69 ] ; constitutional and red-team-driven alignment that transfers language-model alignment practices to embodied settings; curriculum-based safety training that pedagogically sequences safe and unsafe scenarios; and human-in-the-loop refinement that distills expert corrections into the policy via preference learning. Integrating these paradigms without sacrificing generalization—VLA systems derive much of their value from broad behavioral coverage—remains a central methodological challenge. policy 拥有 action proposal，environment/human safety layer 拥有 observation truth 与 actuation commit

Evaluation contract：While multi-layered defense mechanisms provide architectural security, verifying their efficacy in dynamic environments requires rigorous quantification. Evaluation for VLA models has evolved from binary success metrics toward a multi-dimensional certification process that assesses physical resilience, semantic alignment, and self-awareness. For a comprehensive summary and cross-comparison of representative safety evaluation benchmarks, their target scenarios, and core metrics, please refer to the consolidated Table 5 in Section 6 .

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：examined semantic jailbreaks that bypass language-level safeguards, visual and cross-modal perturbations that exploit multi-modal integration, and physical interventions that compromise deployed systems through the environment itself. We then analyzed the corresponding defensive repertoire: pedagogical data design, constrained policy optimization, and human-in-the-loop refinement on the training side (Section 4 ); decision-layer guardrails, closed-loop monitors, and physical fail-safes on the inference side (Section 5.2 ).…。因此若该限制在目标 workload 中触发，不能把 `Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-23775:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-23775:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-23775:end -->
<!-- review:SF-2026-ARXIV-2604-23781:start -->
#### ClawMark: A Living-World Benchmark for Multi-Turn, Multi-Day, Multimodal Coworker Agents

问题、旧路径与约束变化：旧路径未显式拥有 `PLATFORM-EVALUATION-SYSTEM` 中该 family 的受限状态。

机制与 state/control owner：Every model runs under a single agent framework, OpenClaw , with identical tool schemas across models; no per-model prompt engineering is performed. For the Kimi-series models, we apply the upstream fix for incorrect tool-call identifier sanitisation in OpenClaw 1 1 1 https://github.com/openclaw/openclaw/issues/62319 . Each task executes inside an isolated docker-compose group comprising the agent container, GreenMail for SMTP/IMAP, a Notion-compatible knowledge base, a Google-Sheets-compatible spreadsheet, and a Radicale CalDAV server. Containers are torn down between tasks, so runs do not share state. EvalSpec owner 冻结 subject/data/scorer，release owner 依据 run evidence 作决定

Evaluation contract：Table 1 positions ClawMark against representative agent benchmarks. Realistic web and computer-use benchmarks such as WebArena [ 6 ] , Mind2Web [ 11 ] , VisualWebArena [ 4 ] , and OSWorld [ 5 ] establish strong single-episode evaluation settings. Related benchmarks extend tool coverage or execution domains, for example MCPMark [ 8 ] , MCP-Bench [ 12 ] , SWE-bench [ 13 ] , AgentBench [ 14 ] , GAIA [ 15 ] , and Terminal-Bench [ 7 ] , but still largely evaluate progress within a fixed episode.

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：ClawMark measures coworker-agent behaviour along three axes that prior benchmarks do not adequately evaluate: multi-turn multi-day timelines, exogenous between-turn environment changes, and raw multimodal evidence. The measurement is grounded in deterministic rule-based scoring over post-turn state of stateful sandboxed services, with a release-gate guarantee of bit-identical checker verdicts across independent re-runs. On our failure taxonomy (Table 5 ), two failure modes dominate: silent-change detection (56.5% per-evaluation fail rate) and backend writeback (53.6%).…。因此若该限制在目标 workload 中触发，不能把 `ClawMark: A Living-World Benchmark for Multi-Turn, Multi-Day, Multimodal Coworker Agents` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-23781:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-23781:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-23781:end -->
<!-- review:SF-2026-ARXIV-2604-23798:start -->
#### ELSA: Exact Linear-Scan Attention for Fast and Memory-Light Vision Transformers

问题、旧路径与约束变化：旧路径未显式拥有 `MODEL-SELF-ATTENTION` 中该 family 的受限状态。

机制与 state/control owner：Table 3 reports full-model FP16 forward at the same batch size (batch = 8 {=}8 ) for ViT and Swin [ 25 ] using the corrected strict FP16 scan path (no FP32 bridge, no legacy triton). We drop ME-SDPA since FA2 is the relevant FP16 flash baseline; Math-SDPA / WA are kept only as memory references. Under this strict same-batch protocol, ELSA / W-ELSA is faster than FA2 on every ViT and Swin row ( ∼ 29 {\sim}29 – 65 % 65\% on ViT, ∼ 2 {\sim}2 – 14 % 14\% on Swin), and also stays below the Math/WA memory reference on all ViT rows and on Swin-S/W16; the three remaining Swin rows incur moderate memory overhead ( + 3.2 % {+}3.2\% to + 18.6 % {+}18.6\% ) from short-window scan workspace, reported explicitly. Beyond inference, ELSA deploys seamlessly as a drop-in replacement during training with no modifications to the optimization pipeline. As shown in Figure 5 , Swin-T, ViT-S, and ViT-T trained entirely with ELSA exhibit steady loss decay and monotonically improving top-1 accuracy, with final values within 0.1% of the corresponding Math/FA2 baseline, confirming no optimization penalty. layer architecture 拥有 mixing rule，runtime 只执行已版本化 attention graph

Evaluation contract：We evaluate ELSA across a diverse set of tasks and models: ImageNet-1K classification [ 31 ] with ViT-B/16 [ 11 ] and Swin-T [ 25 ] ; zero-shot inference with CLIP ViT-L/14 [ 30 ] ; BERT sentiment on SST-2 and IMDB; and hyperspectral classification (Pavia, Salinas, WHU) with HSIMAE [ 41 ] . We benchmark single-GPU inference with random sequences of n = 64 n=64 – 16,384 16{,}384 tokens in both FP16 and FP32 (Figure 4 ). In FP16, at the isolated kernel level, ELSA remains close to FA2/FA3 in latency at n = 4,096 n{=}4{,}096 , with the gap further narrowing beyond n = 16,384 n{=}16{,}384 ; this kernel-only gap reverses at the full-model level (Table 3 ). FA2/FA3 are excluded from FP32 comparisons: their optimized paths rely on HMMA/GMMA Tensor Core instructions for FP16/BF16, and their FP32 fallback reverts to untuned SIMD execution, rendering the comparison uninformative. More broadly, FA2/FA3 require Ampere/Hopper Tensor Cores and are unavailable on older GPUs and edge devices—deployment scenarios where ELSA operates as a hardware-agnostic, FP32-exact drop-in replacement. This resolution-scalability advantage is further evidenced in Table 2 , which reports attention-module-only resolution scaling (proxy scope) and should not be directly compared; extended results on 3D reconstruction models (VGGT [ 39 ] and FastVGGT [ 34 ] ) are provided in Supp. G , where ELSA achieves up to 2.34 × 2.34\times speedup over xFormers-FP32 while matching its memory footprint.

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：ELSA reduces memory and I/O to O ⁡ ( n ) O(n) but preserves quadratic arithmetic complexity, and is most effective when memory rather than compute is the bottleneck. At the isolated kernel level on short sequences, scan merge overhead can leave ELSA behind FA2/FA3, though this reverses at the full-model level (Table 3 ); under offloading, gains of 17.8–20.2% over SDPA emerge only at ≥ \geq 32K tokens. The kernel is validated primarily on Ampere GPUs, and training dynamics under multi-GPU scaling remain open.。因此若该限制在目标 workload 中触发，不能把 `ELSA: Exact Linear-Scan Attention for Fast and Memory-Light Vision Transformers` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-23798:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-23798:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-23798:end -->
<!-- review:SF-2026-ARXIV-2604-23838:start -->
#### JigsawRL: Assembling RL Pipelines for Efficient LLM Post-Training

问题、旧路径与约束变化：旧路径把 `JigsawRL: Assembling RL Pipelines for Efficient LLM Post-Training` 的判断留给固定策略、单次离线分数或未显式版本化的运行状态。

机制与 state/control owner：We present JigsawRL, a cost-efficient framework that explores Pipeline Multiplexing as a new dimension of RL parallelism. JigsawRL decomposes each pipeline into a Sub-Stage Graph that exposes the intra-stage and inter-worker imbalance hidden by stage-level systems. On this abstraction, JigsawRL resolves multiplexing interference through dynamic resource allocation, eliminates fragmented utilization by migrating long-tail rollouts across workers, and formulates their coordination as a graph scheduling problem solved with a look-ahead heuristic. We present JigsawRL, a cost-efficient framework that explores Pipeline Multiplexing as a new dimension of RL parallelism. JigsawRL decomposes each pipeline into a Sub-Stage Graph that exposes the intra-stage and inter-worker imbalance hidden by stage-level systems. On this abstraction, JigsawRL resolves multiplexing interference through dynamic resource allocation, eliminates fragmented utilization by migrating long-tail rollouts across workers, and formulates their coordination as a graph scheduling problem solved with a look-ahead heuristic. 该机制将长期 owner 定位到 `TRAIN-RLHF`，并把相应 state/control/evidence identity 从隐式约定变成可检查对象。

Evaluation contract：Exact-v1 evaluation is bounded to the author-disclosed protocol and artifacts.

Trade-off / failure / fallback / coexistence：论文只在 exact-v1 披露的任务、模型与实验协议内支持上述结论；`JigsawRL: Assembling RL Pipelines for Efficient LLM Post-Training` 不证明跨模型、跨硬件、跨数据分布或生产 SLO 的普遍收益。失配时回退 current Books 的既有路径，并保留新旧机制并存。

<!-- claim:SF-2026-ARXIV-2604-23838:start -->只接受 arXiv:2604.23838v1 的作者机制与实验；未披露硬件、precision、长度、batch、并发、成本或线上 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2604-23838:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-23838:end -->
<!-- review:SF-2026-ARXIV-2604-23853:start -->
#### ClawTrace: Cost-Aware Tracing for LLM Agent Skill Distillation

问题/机制与 owner：ClawTrace 把 agent trajectory 的 child trace、billed per-step cost 与 rule type 固化为 TraceCard，再用 preserve/prune/repair 区分补缺步骤和不影响结果的高成本步骤。

Trade-off / failure：30+30 tasks、单一 model/seed；只有 2/17 prune rules 命中预期，部分 heuristics 未验证，preserve rules 在跨 benchmark 产生 3 个回归。

Fallback/coexistence：没有稳定 child trace/cost attribution 时不自动蒸馏或剪枝，回退原 trajectory 与人工 rule review；低成本 preserve path 与 cost-aware prune 并存。

<!-- claim:SF-2026-ARXIV-2604-23853:start -->30+30 tasks、单一 model/seed；只有 2/17 prune rules 命中预期，部分 heuristics 未验证，preserve rules 在跨 benchmark 产生 3 个回归。<!-- claim:SF-2026-ARXIV-2604-23853:end -->

Books Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2604-23853:end -->
<!-- review:SF-2026-ARXIV-2604-23887:start -->
#### Evaluation of Prompt Injection Defenses in Large Language Models

问题、旧路径与约束变化：旧路径把 `Evaluation of Prompt Injection Defenses in Large Language Models` 的判断留给固定策略、单次离线分数或未显式版本化的运行状态。

机制与 state/control owner：LLM-powered applications routinely embed secrets in system prompts, yet models can be tricked into revealing them. We built an adaptive attacker that evolves its strategies over hundreds of rounds and tested it against nine defense configurations across more than 20,000 attacks. Every defense that relied on the model to protect itself eventually broke. LLM-powered applications routinely embed secrets in system prompts, yet models can be tricked into revealing them. We built an adaptive attacker that evolves its strategies over hundreds of rounds and tested it against nine defense configurations across more than 20,000 attacks. Every defense that relied on the model to protect itself eventually broke. 该机制将长期 owner 定位到 `PLATFORM-SECURITY`，并把相应 state/control/evidence identity 从隐式约定变成可检查对象。

Evaluation contract：These results demonstrate that security boundaries must be enforced in application code, not by the model being attacked.

Trade-off / failure / fallback / coexistence：论文只在 exact-v1 披露的任务、模型与实验协议内支持上述结论；`Evaluation of Prompt Injection Defenses in Large Language Models` 不证明跨模型、跨硬件、跨数据分布或生产 SLO 的普遍收益。失配时回退 current Books 的既有路径，并保留新旧机制并存。

<!-- claim:SF-2026-ARXIV-2604-23887:start -->只接受 arXiv:2604.23887v1 的作者机制与实验；未披露硬件、precision、长度、batch、并发、成本或线上 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2604-23887:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-23887:end -->

<!-- review:SF-2026-ARXIV-2604-23584:start -->
#### Identity-Decoupled Anonymization for Visual Evidence in Multi-modal Retrieval-Augmented Generation

问题/机制与 owner：multimodal RAG 在保留可检索证据前提下，把视觉 identity 与任务内容解耦匿名化。

Trade-off / failure：作者实验不证明面对任意 re-identification auxiliary data 或跨域 corpus 都保持隐私与 utility。

Fallback/coexistence：高风险 identity slice 回退本地 redaction/不入库；检索路径保留原始受控 corpus 与审计映射。

<!-- claim:SF-2026-ARXIV-2604-23584:start -->作者实验不证明面对任意 re-identification auxiliary data 或跨域 corpus 都保持隐私与 utility。<!-- claim:SF-2026-ARXIV-2604-23584:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-23584:end -->

<!-- review:SF-2026-ARXIV-2604-23831:start -->
#### Architectural Isolation as a Timing Safety Primitive for Edge AI Medical Devices: Controlled Experimental Evidence on a Shared-Silicon Platform

问题/机制与 owner：edge AI safety contract 同时检查 output stability 与 deadline/timing，而非只比较 accuracy。

Trade-off / failure：仅 MobileNetV2/Jetson；GPU/CPU stack、precision 与 measurement path 不同，未验证完整 clinical workflow。

Fallback/coexistence：deadline 或数值稳定性任一失败即回退 CPU/保守模型，并禁止把平台间点测外推为临床保证。

<!-- claim:SF-2026-ARXIV-2604-23831:start -->仅 MobileNetV2/Jetson；GPU/CPU stack、precision 与 measurement path 不同，未验证完整 clinical workflow。<!-- claim:SF-2026-ARXIV-2604-23831:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-23831:end -->

<!-- review:SF-2026-ARXIV-2607-05397:start -->
#### Proof of Execution: Runtime Verification for Governed AI Agent Actions

问题/机制与 owner：Proof of Execution 把 causal event stream、contract invariants 与 replay context 绑定，形成可检查运行证据。

Trade-off / failure：单节点原型；valid contract 不代表 contract 安全或选得正确，replay 也不等于现实复现，planner compromise 不在范围内。

Fallback/coexistence：contract 无法验证时冻结 commit，回退人工审批与 event-log forensic replay；旧 gateway 权限边界继续存在。

<!-- claim:SF-2026-ARXIV-2607-05397:start -->单节点原型；valid contract 不代表 contract 安全或选得正确，replay 也不等于现实复现，planner compromise 不在范围内。<!-- claim:SF-2026-ARXIV-2607-05397:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-05397:end -->

## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

没有跨 workload 外推的 benchmark claim；所有数值只属于 exact-v1 作者协议，未披露字段为 Not Disclosed。

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2604-23488 | score_7_9;forced_review | selected | DA-2604-23488 | — | exact-v1 显示跨层 state/control 或 evaluation-contract delta，且 current Books comparison 仍有长期机制增量。 | analysis:DA-2604-23488 |
| SF-2026-ARXIV-2604-23505 | score_7_9;forced_review | selected | DA-2604-23505 | — | exact-v1 显示跨层 state/control 或 evaluation-contract delta，且 current Books comparison 仍有长期机制增量。 | analysis:DA-2604-23505 |
| SF-2026-ARXIV-2604-23543 | score_7_9;forced_review | not_selected | — | — | Source Review 已完成；Top-3 预算优先给本日跨层 delta，未选不降低 Evidence 或 Books Decision。 | analysis-decision:SF-2026-ARXIV-2604-23543 |
| SF-2026-ARXIV-2604-23553 | score_7_9;forced_review | not_selected | — | — | Source Review 已完成；Top-3 预算优先给本日跨层 delta，未选不降低 Evidence 或 Books Decision。 | analysis-decision:SF-2026-ARXIV-2604-23553 |
| SF-2026-ARXIV-2604-23577 | score_7_9;forced_review | not_selected | — | — | Source Review 已完成；Top-3 预算优先给本日跨层 delta，未选不降低 Evidence 或 Books Decision。 | analysis-decision:SF-2026-ARXIV-2604-23577 |
| SF-2026-ARXIV-2604-23581 | score_7_9;forced_review | not_selected | — | — | Source Review 已完成；Top-3 预算优先给本日跨层 delta，未选不降低 Evidence 或 Books Decision。 | analysis-decision:SF-2026-ARXIV-2604-23581 |
| SF-2026-ARXIV-2604-23584 | score_7_9;forced_review | not_selected | — | — | Full Review/Books comparison 已完成；Top-3 预算不改变 Evidence 或 Books disposition。 | analysis-decision:SF-2026-ARXIV-2604-23584 |
| SF-2026-ARXIV-2604-23626 | score_7_9;forced_review | not_selected | — | — | Source Review 已完成；Top-3 预算优先给本日跨层 delta，未选不降低 Evidence 或 Books Decision。 | analysis-decision:SF-2026-ARXIV-2604-23626 |
| SF-2026-ARXIV-2604-23646 | score_7_9;forced_review | not_selected | — | — | Source Review 已完成；Top-3 预算优先给本日跨层 delta，未选不降低 Evidence 或 Books Decision。 | analysis-decision:SF-2026-ARXIV-2604-23646 |
| SF-2026-ARXIV-2604-23711 | score_7_9;forced_review | not_selected | — | — | Source Review 已完成；Top-3 预算优先给本日跨层 delta，未选不降低 Evidence 或 Books Decision。 | analysis-decision:SF-2026-ARXIV-2604-23711 |
| SF-2026-ARXIV-2604-23747 | score_7_9;forced_review | not_selected | — | — | Source Review 已完成；Top-3 预算优先给本日跨层 delta，未选不降低 Evidence 或 Books Decision。 | analysis-decision:SF-2026-ARXIV-2604-23747 |
| SF-2026-ARXIV-2604-23758 | score_7_9;forced_review | not_selected | — | — | Source Review 已完成；Top-3 预算优先给本日跨层 delta，未选不降低 Evidence 或 Books Decision。 | analysis-decision:SF-2026-ARXIV-2604-23758 |
| SF-2026-ARXIV-2604-23775 | score_7_9;forced_review | not_selected | — | — | Source Review 已完成；Top-3 预算优先给本日跨层 delta，未选不降低 Evidence 或 Books Decision。 | analysis-decision:SF-2026-ARXIV-2604-23775 |
| SF-2026-ARXIV-2604-23781 | score_7_9;forced_review | not_selected | — | — | Source Review 已完成；Top-3 预算优先给本日跨层 delta，未选不降低 Evidence 或 Books Decision。 | analysis-decision:SF-2026-ARXIV-2604-23781 |
| SF-2026-ARXIV-2604-23798 | score_7_9;forced_review | not_selected | — | — | Source Review 已完成；Top-3 预算优先给本日跨层 delta，未选不降低 Evidence 或 Books Decision。 | analysis-decision:SF-2026-ARXIV-2604-23798 |
| SF-2026-ARXIV-2604-23831 | score_7_9;forced_review | not_selected | — | — | Full Review/Books comparison 已完成；Top-3 预算不改变 Evidence 或 Books disposition。 | analysis-decision:SF-2026-ARXIV-2604-23831 |
| SF-2026-ARXIV-2604-23838 | score_7_9;forced_review | not_selected | — | — | Source Review 已完成；Top-3 预算优先给本日跨层 delta，未选不降低 Evidence 或 Books Decision。 | analysis-decision:SF-2026-ARXIV-2604-23838 |
| SF-2026-ARXIV-2604-23853 | score_7_9;forced_review;potential_books_delta | selected | DA-2604-23853 | — | exact-v1 显示跨层 state/control 或 evaluation-contract delta，且 current Books comparison 仍有长期机制增量。 | analysis:DA-2604-23853 |
| SF-2026-ARXIV-2604-23887 | score_7_9;forced_review | not_selected | — | — | Source Review 已完成；Top-3 预算优先给本日跨层 delta，未选不降低 Evidence 或 Books Decision。 | analysis-decision:SF-2026-ARXIV-2604-23887 |
| SF-2026-ARXIV-2607-05397 | score_7_9;forced_review | not_selected | — | — | Full Review/Books comparison 已完成；Top-3 预算不改变 Evidence 或 Books disposition。 | analysis-decision:SF-2026-ARXIV-2607-05397 |

<!-- analysis:DA-2604-23488:start -->
### Do Prompt-Elicited Trajectories Reflect Training-Time Reward Hacking? A Systematic Study on Monitoring Training-Time Reward Hacking in Code Generation

旧路径与约束：旧路径把 `Do Prompt-Elicited Trajectories Reflect Training-Time Reward Hacking? A Systematic Study on Monitoring Training-Time Reward Hacking in Code Generation` 的判断留给固定策略、单次离线分数或未显式版本化的运行状态。

机制与控制权：Reward hacking in code generation, where models exploit evaluation loopholes to obtain high reward without correctly solving the intended task, poses a critical challenge for Reinforcement Learning (RL) and the deployment of reasoning models. Existing studies often rely on explicitly prompted hacking trajectories, but it remains unclear whether monitors trained on such data can detect reward hacks that arise without direct hacking instructions during RL training. In this work, we introduce Trace-and-Amplify, a framework for scalable curation of reward-hacking trajectories that arise during RL training without explicit hacking instructions. 该机制将长期 owner 定位到 `PLATFORM-EVALUATION-SYSTEM`，并把相应 state/control/evidence identity 从隐式约定变成可检查对象。

收益、代价与边界：论文只在 exact-v1 披露的任务、模型与实验协议内支持上述结论；`Do Prompt-Elicited Trajectories Reflect Training-Time Reward Hacking? A Systematic Study on Monitoring Training-Time Reward Hacking in Code Generation` 不证明跨模型、跨硬件、跨数据分布或生产 SLO 的普遍收益。失配时回退 current Books 的既有路径，并保留新旧机制并存。 只接受 arXiv:2604.23488v1 的作者机制与实验；未披露硬件、precision、长度、batch、并发、成本或线上 SLO 均为 Not Disclosed。
<!-- analysis:DA-2604-23488:end -->
<!-- analysis:DA-2604-23505:start -->
### Uncertainty Propagation in LLM-Based Systems

旧路径与约束：旧路径把 `Uncertainty Propagation in LLM-Based Systems` 的判断留给固定策略、单次离线分数或未显式版本化的运行状态。

机制与控制权：Uncertainty in large language model (LLM)-based systems is often studied at the level of a single model output, yet deployed LLM applications are compound systems in which uncertainty is transformed and reused across model internals, workflow stages, component boundaries, persistent state, and human or organisational processes. Without principled treatment of how uncertainty is carried and reused across these boundaries, early errors can propagate and compound in ways that are difficult to detect and govern. This paper develops a systems-level account of uncertainty propagation. 该机制将长期 owner 定位到 `PLATFORM-EVALUATION-SYSTEM`，并把相应 state/control/evidence identity 从隐式约定变成可检查对象。

收益、代价与边界：论文只在 exact-v1 披露的任务、模型与实验协议内支持上述结论；`Uncertainty Propagation in LLM-Based Systems` 不证明跨模型、跨硬件、跨数据分布或生产 SLO 的普遍收益。失配时回退 current Books 的既有路径，并保留新旧机制并存。 只接受 arXiv:2604.23505v1 的作者机制与实验；未披露硬件、precision、长度、batch、并发、成本或线上 SLO 均为 Not Disclosed。
<!-- analysis:DA-2604-23505:end -->
<!-- analysis-decision:SF-2026-ARXIV-2604-23543:start -->本 family 已完成 exact-v1、Score 与 Books comparison；未选入 Top-3 仅是叙事预算决定。<!-- analysis-decision:SF-2026-ARXIV-2604-23543:end -->
<!-- analysis-decision:SF-2026-ARXIV-2604-23553:start -->本 family 已完成 exact-v1、Score 与 Books comparison；未选入 Top-3 仅是叙事预算决定。<!-- analysis-decision:SF-2026-ARXIV-2604-23553:end -->
<!-- analysis-decision:SF-2026-ARXIV-2604-23577:start -->本 family 已完成 exact-v1、Score 与 Books comparison；未选入 Top-3 仅是叙事预算决定。<!-- analysis-decision:SF-2026-ARXIV-2604-23577:end -->
<!-- analysis-decision:SF-2026-ARXIV-2604-23581:start -->本 family 已完成 exact-v1、Score 与 Books comparison；未选入 Top-3 仅是叙事预算决定。<!-- analysis-decision:SF-2026-ARXIV-2604-23581:end -->
<!-- analysis-decision:SF-2026-ARXIV-2604-23626:start -->本 family 已完成 exact-v1、Score 与 Books comparison；未选入 Top-3 仅是叙事预算决定。<!-- analysis-decision:SF-2026-ARXIV-2604-23626:end -->
<!-- analysis-decision:SF-2026-ARXIV-2604-23646:start -->本 family 已完成 exact-v1、Score 与 Books comparison；未选入 Top-3 仅是叙事预算决定。<!-- analysis-decision:SF-2026-ARXIV-2604-23646:end -->
<!-- analysis-decision:SF-2026-ARXIV-2604-23711:start -->本 family 已完成 exact-v1、Score 与 Books comparison；未选入 Top-3 仅是叙事预算决定。<!-- analysis-decision:SF-2026-ARXIV-2604-23711:end -->
<!-- analysis-decision:SF-2026-ARXIV-2604-23747:start -->本 family 已完成 exact-v1、Score 与 Books comparison；未选入 Top-3 仅是叙事预算决定。<!-- analysis-decision:SF-2026-ARXIV-2604-23747:end -->
<!-- analysis-decision:SF-2026-ARXIV-2604-23758:start -->本 family 已完成 exact-v1、Score 与 Books comparison；未选入 Top-3 仅是叙事预算决定。<!-- analysis-decision:SF-2026-ARXIV-2604-23758:end -->
<!-- analysis-decision:SF-2026-ARXIV-2604-23775:start -->本 family 已完成 exact-v1、Score 与 Books comparison；未选入 Top-3 仅是叙事预算决定。<!-- analysis-decision:SF-2026-ARXIV-2604-23775:end -->
<!-- analysis-decision:SF-2026-ARXIV-2604-23781:start -->本 family 已完成 exact-v1、Score 与 Books comparison；未选入 Top-3 仅是叙事预算决定。<!-- analysis-decision:SF-2026-ARXIV-2604-23781:end -->
<!-- analysis-decision:SF-2026-ARXIV-2604-23798:start -->本 family 已完成 exact-v1、Score 与 Books comparison；未选入 Top-3 仅是叙事预算决定。<!-- analysis-decision:SF-2026-ARXIV-2604-23798:end -->
<!-- analysis-decision:SF-2026-ARXIV-2604-23838:start -->本 family 已完成 exact-v1、Score 与 Books comparison；未选入 Top-3 仅是叙事预算决定。<!-- analysis-decision:SF-2026-ARXIV-2604-23838:end -->
<!-- analysis:DA-2604-23853:start -->
### ClawTrace: Cost-Aware Tracing for LLM Agent Skill Distillation

旧路径与约束：旧路径把 `ClawTrace: Cost-Aware Tracing for LLM Agent Skill Distillation` 的判断留给固定策略、单次离线分数或未显式版本化的运行状态。

机制与控制权：Skill-distillation pipelines learn reusable rules from LLM agent trajectories, but they lack a key signal: how much each step costs. Without per-step cost, a pipeline cannot distinguish adding a missing step to fix a bug from removing an expensive step that never affected the outcome. We use the cost-attribution gap to ask whether the rule types inside a distilled skill transfer the same way to new tasks. 该机制将长期 owner 定位到 `PLATFORM-TRACE`，并把相应 state/control/evidence identity 从隐式约定变成可检查对象。

收益、代价与边界：论文只在 exact-v1 披露的任务、模型与实验协议内支持上述结论；`ClawTrace: Cost-Aware Tracing for LLM Agent Skill Distillation` 不证明跨模型、跨硬件、跨数据分布或生产 SLO 的普遍收益。失配时回退 current Books 的既有路径，并保留新旧机制并存。 只接受 arXiv:2604.23853v1 的作者机制与实验；未披露硬件、precision、长度、batch、并发、成本或线上 SLO 均为 Not Disclosed。
<!-- analysis:DA-2604-23853:end -->
<!-- analysis-decision:SF-2026-ARXIV-2604-23887:start -->本 family 已完成 exact-v1、Score 与 Books comparison；未选入 Top-3 仅是叙事预算决定。<!-- analysis-decision:SF-2026-ARXIV-2604-23887:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2604-23488 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L78-从目标到证据-而不是从指标到目标 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L18-为什么-ai-cluster-需要更强的-queue-模型; books/part-06-ai-infrastructure/67-monitoring.md#L18-先定义目标-再选择可测信号 | existing:SF-2026-ARXIV-2604-23488 | delta:SF-2026-ARXIV-2604-23488 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23488 |
| SF-2026-ARXIV-2604-23505 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L78-从目标到证据-而不是从指标到目标 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L18-为什么-ai-cluster-需要更强的-queue-模型; books/part-06-ai-infrastructure/67-monitoring.md#L18-先定义目标-再选择可测信号 | existing:SF-2026-ARXIV-2604-23505 | delta:SF-2026-ARXIV-2604-23505 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23505 |
| SF-2026-ARXIV-2604-23543 | TRAIN-DPO | books/part-04-training-system/34-dpo.md#L18-从-rlhf-的两阶段复杂度开始 | books/part-04-training-system/33-grpo.md#L31-为什么移除-critic-会有吸引力; books/part-04-training-system/35-checkpoint.md#L18-为什么只保存-weights-不够 | existing:SF-2026-ARXIV-2604-23543 | delta:SF-2026-ARXIV-2604-23543 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23543 |
| SF-2026-ARXIV-2604-23553 | INFER-DECODE | books/part-05-inference-system/44-decode.md#L18-为什么不能并行写出未来-token | books/part-05-inference-system/43-prefill.md#L18-如果逐个-token-读-prompt; books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L24-如果完全不缓存 | existing:SF-2026-ARXIV-2604-23553 | delta:SF-2026-ARXIV-2604-23553 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23553 |
| SF-2026-ARXIV-2604-23577 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#L16-调度对象从-request-变成-token-state | books/part-05-inference-system/55-pd-disaggregation.md#L16-两种阶段-两种节奏; books/part-06-ai-infrastructure/57-what-is-ai-platform.md#L16-从单点成功到组织级失败 | existing:SF-2026-ARXIV-2604-23577 | delta:SF-2026-ARXIV-2604-23577 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23577 |
| SF-2026-ARXIV-2604-23581 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L78-从目标到证据-而不是从指标到目标 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L18-为什么-ai-cluster-需要更强的-queue-模型; books/part-06-ai-infrastructure/67-monitoring.md#L18-先定义目标-再选择可测信号 | existing:SF-2026-ARXIV-2604-23581 | delta:SF-2026-ARXIV-2604-23581 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23581 |
| SF-2026-ARXIV-2604-23584 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L16-从资产与信任边界开始 | books/part-06-ai-infrastructure/71-multi-tenant.md#L16-先定义-tenant-与信任级别; books/part-06-ai-infrastructure/73-production-best-practice.md#L16-poc-隐含了哪些假设 | existing:SF-2026-ARXIV-2604-23584 | delta:SF-2026-ARXIV-2604-23584 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23584 |
| SF-2026-ARXIV-2604-23626 | AGENT-PLANNING | books/part-07-agent/79-planning.md#L16-plan-不是解释文本 | books/part-07-agent/78-tool-calling.md#L16-从生成文本到环境转移; books/part-07-agent/80-reflection.md#L16-基本循环 | existing:SF-2026-ARXIV-2604-23626 | delta:SF-2026-ARXIV-2604-23626 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23626 |
| SF-2026-ARXIV-2604-23646 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L16-从资产与信任边界开始 | books/part-06-ai-infrastructure/71-multi-tenant.md#L16-先定义-tenant-与信任级别; books/part-06-ai-infrastructure/73-production-best-practice.md#L16-poc-隐含了哪些假设 | existing:SF-2026-ARXIV-2604-23646 | delta:SF-2026-ARXIV-2604-23646 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23646 |
| SF-2026-ARXIV-2604-23711 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L16-从资产与信任边界开始 | books/part-06-ai-infrastructure/71-multi-tenant.md#L16-先定义-tenant-与信任级别; books/part-06-ai-infrastructure/73-production-best-practice.md#L16-poc-隐含了哪些假设 | existing:SF-2026-ARXIV-2604-23711 | delta:SF-2026-ARXIV-2604-23711 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23711 |
| SF-2026-ARXIV-2604-23747 | TRAIN-SFT | books/part-04-training-system/29-sft.md#L415-full-fine-tuning-与-parameter-efficient-adaptation | books/part-04-training-system/28-pretraining.md#L18-从随机参数开始会发生什么; books/part-04-training-system/30-lora.md#L18-从-full-fine-tuning-的重复状态开始 | existing:SF-2026-ARXIV-2604-23747 | delta:SF-2026-ARXIV-2604-23747 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23747 |
| SF-2026-ARXIV-2604-23758 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#L102-deterministic-spine-agentic-nodes | books/part-07-agent/80-reflection.md#L16-基本循环; books/part-07-agent/82-multi-agent.md#L16-先建立单-agent-baseline | existing:SF-2026-ARXIV-2604-23758 | delta:SF-2026-ARXIV-2604-23758 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23758 |
| SF-2026-ARXIV-2604-23775 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L177-state-ownership-与-freshness | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L16-从三个容易混淆的对象开始; books/part-04-training-system/27-data.md#L18-part-iv-的能力生产链 | existing:SF-2026-ARXIV-2604-23775 | delta:SF-2026-ARXIV-2604-23775 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23775 |
| SF-2026-ARXIV-2604-23781 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L78-从目标到证据-而不是从指标到目标 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L18-为什么-ai-cluster-需要更强的-queue-模型; books/part-06-ai-infrastructure/67-monitoring.md#L18-先定义目标-再选择可测信号 | existing:SF-2026-ARXIV-2604-23781 | delta:SF-2026-ARXIV-2604-23781 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23781 |
| SF-2026-ARXIV-2604-23798 | MODEL-SELF-ATTENTION | books/part-02-model/14-self-attention.md#L219-flashattention-优化的是执行-不是模型语义 | books/part-02-model/13-position-encoding.md#L18-为什么纯-self-attention-看不见顺序; books/part-02-model/15-multi-head-attention.md#L18-单个-head-的表达瓶颈 | existing:SF-2026-ARXIV-2604-23798 | delta:SF-2026-ARXIV-2604-23798 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23798 |
| SF-2026-ARXIV-2604-23831 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L200-平均值-切片与不确定性 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L18-为什么-ai-cluster-需要更强的-queue-模型; books/part-06-ai-infrastructure/67-monitoring.md#L18-先定义目标-再选择可测信号 | existing:SF-2026-ARXIV-2604-23831 | delta:SF-2026-ARXIV-2604-23831 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23831 |
| SF-2026-ARXIV-2604-23838 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#L18-demonstration-为什么不足以表达偏好 | books/part-04-training-system/30-lora.md#L18-从-full-fine-tuning-的重复状态开始; books/part-04-training-system/32-ppo.md#L18-把语言生成写成策略过程 | existing:SF-2026-ARXIV-2604-23838 | delta:SF-2026-ARXIV-2604-23838 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23838 |
| SF-2026-ARXIV-2604-23853 | PLATFORM-TRACE | books/part-06-ai-infrastructure/69-trace.md#L16-从总延迟到-critical-path | books/part-06-ai-infrastructure/68-logging.md#L16-文本行不是日志契约; books/part-06-ai-infrastructure/70-cost.md#L16-资源时间是共同底座 | existing:SF-2026-ARXIV-2604-23853 | delta:SF-2026-ARXIV-2604-23853 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2604-23853 |
| SF-2026-ARXIV-2604-23887 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L16-从资产与信任边界开始 | books/part-06-ai-infrastructure/71-multi-tenant.md#L16-先定义-tenant-与信任级别; books/part-06-ai-infrastructure/73-production-best-practice.md#L16-poc-隐含了哪些假设 | existing:SF-2026-ARXIV-2604-23887 | delta:SF-2026-ARXIV-2604-23887 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-23887 |
| SF-2026-ARXIV-2607-05397 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#L413-agent-runtime-state-machine | books/part-07-agent/83-mcp.md#L19-为什么需要协议层 | existing:SF-2026-ARXIV-2607-05397 | delta:SF-2026-ARXIV-2607-05397 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-05397 |

<!-- books-review:SF-2026-ARXIV-2604-23488:start -->
<!-- existing:SF-2026-ARXIV-2604-23488:start -->真实 owner `books/part-06-ai-infrastructure/66-evaluation-system.md#L78-从目标到证据而不是从指标到目标` 正文：## 从目标到证据，而不是从指标到目标 Evaluation 的起点不是“平台能采集什么 metric”，而是系统希望满足什么目标。可以把链路写成： ```text intended use and risk → evaluation specification → dataset / environment → system execution → scorer / human judgment → aggregation and uncertainty → decision policy → release / rollback / investigation → production feedback ``` `intended use` 决定什么错误重要。例如代码补全、医疗问答和广告生成都可以计算文本相似度，但相同指标不代表相同风险。评估 specification 至少应声明： ```text EvalSpec = target behavior + eligible population + failure taxonomy + metrics and scorers + slice definitions + thresholds / comparison rules + uncertainty requirement + owner and review policy ``` 如果目标没有被写清楚，团队往往会优化最容易计算的 proxy。模型变得更会迎合 judge，却未必更可靠；服务提高吞吐，却可能让 tail latency 和任务完成率下降。这不是模型“作弊”，而是控制系统给出了错误目标。；相邻章 `books/part-06-ai-infrastructure/65-kai-scheduler.md#L18-为什么-ai-cluster-需要更强的-queue-模型; books/part-06-ai-infrastructure/67-monitoring.md#L18-先定义目标再选择可测信号` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=ba07952c1fe646f17bfd554f905fb4a594aaa8676cc3e8aea0edfa2526800e09。<!-- existing:SF-2026-ARXIV-2604-23488:end -->
<!-- delta:SF-2026-ARXIV-2604-23488:start -->Reward hacking in code generation, where models exploit evaluation loopholes to obtain high reward without correctly solving the intended task, poses a critical challenge for Reinforcement Learning (RL) and the deployment of reasoning models. Existing studies often rely on explicitly prompted hacking trajectories, but it remains unclear whether monitors trained on such data can detect reward hacks that arise without direct hacking instructions during RL training. In this work, we introduce Trace-and-Amplify, a framework for scalable curation of reward-hacking trajectories that arise during RL training without explicit hacking instructions. 该机制将长期 owner 定位到 `PLATFORM-EVALUATION-SYSTEM`，并把相应 state/control/evidence identity 从隐式约定变成可检查对象。<!-- delta:SF-2026-ARXIV-2604-23488:end --> Decision=`No Change — Existing Coverage`；evidence boundary：只接受 arXiv:2604.23488v1 的作者机制与实验；未披露硬件、precision、长度、batch、并发、成本或线上 SLO 均为 Not Disclosed。
<!-- books-review:SF-2026-ARXIV-2604-23488:end -->
<!-- books-review:SF-2026-ARXIV-2604-23505:start -->
<!-- existing:SF-2026-ARXIV-2604-23505:start -->真实 owner `books/part-06-ai-infrastructure/66-evaluation-system.md#L78-从目标到证据而不是从指标到目标` 正文：## 从目标到证据，而不是从指标到目标 Evaluation 的起点不是“平台能采集什么 metric”，而是系统希望满足什么目标。可以把链路写成： ```text intended use and risk → evaluation specification → dataset / environment → system execution → scorer / human judgment → aggregation and uncertainty → decision policy → release / rollback / investigation → production feedback ``` `intended use` 决定什么错误重要。例如代码补全、医疗问答和广告生成都可以计算文本相似度，但相同指标不代表相同风险。评估 specification 至少应声明： ```text EvalSpec = target behavior + eligible population + failure taxonomy + metrics and scorers + slice definitions + thresholds / comparison rules + uncertainty requirement + owner and review policy ``` 如果目标没有被写清楚，团队往往会优化最容易计算的 proxy。模型变得更会迎合 judge，却未必更可靠；服务提高吞吐，却可能让 tail latency 和任务完成率下降。这不是模型“作弊”，而是控制系统给出了错误目标。；相邻章 `books/part-06-ai-infrastructure/65-kai-scheduler.md#L18-为什么-ai-cluster-需要更强的-queue-模型; books/part-06-ai-infrastructure/67-monitoring.md#L18-先定义目标再选择可测信号` 已顺读。该主线尚未完整承载本 family 特有机制、failure 与 evidence boundary。 owner_sha256=ba07952c1fe646f17bfd554f905fb4a594aaa8676cc3e8aea0edfa2526800e09。<!-- existing:SF-2026-ARXIV-2604-23505:end -->
<!-- delta:SF-2026-ARXIV-2604-23505:start -->Uncertainty in large language model (LLM)-based systems is often studied at the level of a single model output, yet deployed LLM applications are compound systems in which uncertainty is transformed and reused across model internals, workflow stages, component boundaries, persistent state, and human or organisational processes. Without principled treatment of how uncertainty is carried and reused across these boundaries, early errors can propagate and compound in ways that are difficult to detect and govern. This paper develops a systems-level account of uncertainty propagation. 该机制将长期 owner 定位到 `PLATFORM-EVALUATION-SYSTEM`，并把相应 state/control/evidence identity 从隐式约定变成可检查对象。<!-- delta:SF-2026-ARXIV-2604-23505:end --> Decision=`Integrate`；evidence boundary：只接受 arXiv:2604.23505v1 的作者机制与实验；未披露硬件、precision、长度、batch、并发、成本或线上 SLO 均为 Not Disclosed。
<!-- books-review:SF-2026-ARXIV-2604-23505:end -->
<!-- books-review:SF-2026-ARXIV-2604-23543:start -->
<!-- existing:SF-2026-ARXIV-2604-23543:start -->真实 owner `books/part-04-training-system/34-dpo.md#L18-从-rlhf-的两阶段复杂度开始` 正文：## 从 RLHF 的两阶段复杂度开始 经典 pipeline： ```text preference pairs -> train Reward Model -> current policy rollouts -> score rollouts -> PPO/GRPO policy updates ``` 它允许 policy 探索新 outputs，也需要多个模型、generation、reward evaluation 和版本同步。 若已有高质量离线 pairs，一个朴素替代是对 chosen 做 SFT： ```text maximize log pi_theta(y_w \| x) ``` 但这丢弃了 rejected response 提供的信息。模型不知道 chosen 相对 rejected 好在哪里，也没有直接约束二者之间的 margin。 DPO 的目标是同时使用 pair 两侧，又避免显式训练 reward 和在线 RL loop。；相邻章 `books/part-04-training-system/33-grpo.md#L31-为什么移除-critic-会有吸引力; books/part-04-training-system/35-checkpoint.md#L18-为什么只保存-weights-不够` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=3ace537440f6dc97060caa2205884dc2c4172735ebbce82da7e7da7755b6ff51。<!-- existing:SF-2026-ARXIV-2604-23543:end -->
<!-- delta:SF-2026-ARXIV-2604-23543:start -->preference data owner 拥有 pair/label provenance，trainer 拥有 objective，judge 不拥有最终 policy commit<!-- delta:SF-2026-ARXIV-2604-23543:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-23543:end -->
<!-- books-review:SF-2026-ARXIV-2604-23553:start -->
<!-- existing:SF-2026-ARXIV-2604-23553:start -->真实 owner `books/part-05-inference-system/44-decode.md#L18-为什么不能并行写出未来-token` 正文：## 为什么不能并行写出未来 Token 语言模型定义： ```text p(y_1,...,y_T_o \| x) = product_i p(y_i \| x, y_<i) ``` 要计算 `y_i` 的分布，必须先知道实际选择的 `y_<i`。Sampling 可能使下一 token 不等于当前最高概率 token，stop conditions 也会动态结束请求。因此不能把未知的未来 positions 当作 Prefill 中已知的 prompt positions 一起 exact 执行。 这不是 GPU 不够强，而是计算图中存在真实 data dependency。；相邻章 `books/part-05-inference-system/43-prefill.md#L18-如果逐个-token-读-prompt; books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L24-如果完全不缓存` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=ed3f0242eee27efadff945433b83cb509557d634d3401ce95ad85f86d2a40b93。<!-- existing:SF-2026-ARXIV-2604-23553:end -->
<!-- delta:SF-2026-ARXIV-2604-23553:start -->decoder runtime 拥有 token frontier、cache identity 与 commit order<!-- delta:SF-2026-ARXIV-2604-23553:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-23553:end -->
<!-- books-review:SF-2026-ARXIV-2604-23577:start -->
<!-- existing:SF-2026-ARXIV-2604-23577:start -->真实 owner `books/part-05-inference-system/56-inference-scheduling.md#L16-调度对象从-request-变成-token-state` 正文：## 调度对象从 request 变成 token state 普通 Web 服务调度通常看 request。LLM Serving 不能只看 request，因为一个请求会持续生成很多 token。 调度器需要理解： - 请求处于 Prefill 还是 Decode。 - 已经生成多少 token。 - 还可能生成多少 token。 - KV Cache 占用多少显存。 - 是否共享 prefix。 - 是否正在 speculative verification。 - 是否需要跨 worker handoff。 这意味着 LLM 调度对象是“带 runtime state 的 token generation process”。 一个完整 Serving 系统通常同时存在四层决策： ```text admission control 请求是否可以进入，是否有 SLO 与 memory budget iteration scheduling 下一轮执行哪些 token work routing / placement 请求、KV 与 model workers 放在哪里 autoscaling 未来需要多少 workers 和哪类 capacity ``` 只优化其中一层，可能把瓶颈推给下一层。例如 iteration batch 很满，但 admission 让长请求无限排队，系统吞吐看起来很好，用户 SLO 仍然失败。；相邻章 `books/part-05-inference-system/55-pd-disaggregation.md#L16-两种阶段两种节奏; books/part-06-ai-infrastructure/57-what-is-ai-platform.md#L16-从单点成功到组织级失败` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=285ddf8eae11e6e0f941cf66d1b3dd7dc71f62cc69cd85673734b8fbd9713fb0。<!-- existing:SF-2026-ARXIV-2604-23577:end -->
<!-- delta:SF-2026-ARXIV-2604-23577:start -->scheduler 拥有队列、priority 与 resource reservation，model/kernel 不自行决定 admission<!-- delta:SF-2026-ARXIV-2604-23577:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-23577:end -->
<!-- books-review:SF-2026-ARXIV-2604-23581:start -->
<!-- existing:SF-2026-ARXIV-2604-23581:start -->真实 owner `books/part-06-ai-infrastructure/66-evaluation-system.md#L78-从目标到证据而不是从指标到目标` 正文：## 从目标到证据，而不是从指标到目标 Evaluation 的起点不是“平台能采集什么 metric”，而是系统希望满足什么目标。可以把链路写成： ```text intended use and risk → evaluation specification → dataset / environment → system execution → scorer / human judgment → aggregation and uncertainty → decision policy → release / rollback / investigation → production feedback ``` `intended use` 决定什么错误重要。例如代码补全、医疗问答和广告生成都可以计算文本相似度，但相同指标不代表相同风险。评估 specification 至少应声明： ```text EvalSpec = target behavior + eligible population + failure taxonomy + metrics and scorers + slice definitions + thresholds / comparison rules + uncertainty requirement + owner and review policy ``` 如果目标没有被写清楚，团队往往会优化最容易计算的 proxy。模型变得更会迎合 judge，却未必更可靠；服务提高吞吐，却可能让 tail latency 和任务完成率下降。这不是模型“作弊”，而是控制系统给出了错误目标。；相邻章 `books/part-06-ai-infrastructure/65-kai-scheduler.md#L18-为什么-ai-cluster-需要更强的-queue-模型; books/part-06-ai-infrastructure/67-monitoring.md#L18-先定义目标再选择可测信号` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=ba07952c1fe646f17bfd554f905fb4a594aaa8676cc3e8aea0edfa2526800e09。<!-- existing:SF-2026-ARXIV-2604-23581:end -->
<!-- delta:SF-2026-ARXIV-2604-23581:start -->EvalSpec owner 冻结 subject/data/scorer，release owner 依据 run evidence 作决定<!-- delta:SF-2026-ARXIV-2604-23581:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-23581:end -->
<!-- books-review:SF-2026-ARXIV-2604-23626:start -->
<!-- existing:SF-2026-ARXIV-2604-23626:start -->真实 owner `books/part-07-agent/79-planning.md#L16-plan-不是解释文本` 正文：## Plan 不是解释文本 朴素计划： ```text 1. Analyze 2. Implement 3. Test ``` 它没有输入、完成条件、依赖或失败分支，无法驱动 runtime。更可执行的 plan node 包含： ```text step_id goal / expected state preconditions action or tool class inputs and dependencies success evidence risk / approval class budget status ``` 自然语言可以描述意图，typed state 承担控制。；相邻章 `books/part-07-agent/78-tool-calling.md#L16-从生成文本到环境转移; books/part-07-agent/80-reflection.md#L16-基本循环` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=22e2cb6740b7057464c1cd35feed95d37cb5f48f7ea0d6ca5f2ddf761b61dd84。<!-- existing:SF-2026-ARXIV-2604-23626:end -->
<!-- delta:SF-2026-ARXIV-2604-23626:start -->planner 拥有可修订 plan state，executor 只提交有证据的 step result<!-- delta:SF-2026-ARXIV-2604-23626:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-23626:end -->
<!-- books-review:SF-2026-ARXIV-2604-23646:start -->
<!-- existing:SF-2026-ARXIV-2604-23646:start -->真实 owner `books/part-06-ai-infrastructure/72-security.md#L16-从资产与信任边界开始` 正文：## 从资产与信任边界开始 需要保护的资产包括： - source data、labels 与 user context； - code、images、dependencies 与 credentials； - checkpoints、adapters、tokenizers 与 prompts； - registry metadata、evaluation 与 approvals； - GPU nodes、runtime memory 与 KV Cache； - APIs、tools、business systems 与 audit evidence。 主体包括用户、service accounts、controllers、training code、model server、model output 和 external tools。模型生成的文本不是可信主体，也不应自动获得调用者全部权限。；相邻章 `books/part-06-ai-infrastructure/71-multi-tenant.md#L16-先定义-tenant-与信任级别; books/part-06-ai-infrastructure/73-production-best-practice.md#L16-poc-隐含了哪些假设` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=cd99007e2f9b12ccf2bc7cd075bbf73c3b935255bf06bda7068b8f624de239ca。<!-- existing:SF-2026-ARXIV-2604-23646:end -->
<!-- delta:SF-2026-ARXIV-2604-23646:start -->policy/CI/sandbox 拥有 invariant 与 commit authority，model 仅提出不可信 proposal<!-- delta:SF-2026-ARXIV-2604-23646:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-23646:end -->
<!-- books-review:SF-2026-ARXIV-2604-23711:start -->
<!-- existing:SF-2026-ARXIV-2604-23711:start -->真实 owner `books/part-06-ai-infrastructure/72-security.md#L16-从资产与信任边界开始` 正文：## 从资产与信任边界开始 需要保护的资产包括： - source data、labels 与 user context； - code、images、dependencies 与 credentials； - checkpoints、adapters、tokenizers 与 prompts； - registry metadata、evaluation 与 approvals； - GPU nodes、runtime memory 与 KV Cache； - APIs、tools、business systems 与 audit evidence。 主体包括用户、service accounts、controllers、training code、model server、model output 和 external tools。模型生成的文本不是可信主体，也不应自动获得调用者全部权限。；相邻章 `books/part-06-ai-infrastructure/71-multi-tenant.md#L16-先定义-tenant-与信任级别; books/part-06-ai-infrastructure/73-production-best-practice.md#L16-poc-隐含了哪些假设` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=cd99007e2f9b12ccf2bc7cd075bbf73c3b935255bf06bda7068b8f624de239ca。<!-- existing:SF-2026-ARXIV-2604-23711:end -->
<!-- delta:SF-2026-ARXIV-2604-23711:start -->policy/CI/sandbox 拥有 invariant 与 commit authority，model 仅提出不可信 proposal<!-- delta:SF-2026-ARXIV-2604-23711:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-23711:end -->
<!-- books-review:SF-2026-ARXIV-2604-23747:start -->
<!-- existing:SF-2026-ARXIV-2604-23747:start -->真实 owner `books/part-04-training-system/29-sft.md#L415-full-fine-tuning-与-parameter-efficient-adaptation` 正文：## Full fine-tuning 与 parameter-efficient adaptation Full SFT 更新全部参数： ```text theta <- theta + Delta theta ``` 它提供最大的更新自由度，也需要保存全部 gradients、optimizer states 和新模型权重。 第 30 章 LoRA 将更新限制为低秩 adapters： ```text theta_base frozen Delta theta represented by small trainable factors ``` 两者可以使用相同 SFT data 与 token loss。LoRA 是参数化和训练状态选择，不是另一种 supervision objective。；相邻章 `books/part-04-training-system/28-pretraining.md#L18-从随机参数开始会发生什么; books/part-04-training-system/30-lora.md#L18-从-full-fine-tuning-的重复状态开始` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=f84bce844228a80d97cb8e1f060d138ecb19907d47fab5386431b6f60b3c5f79。<!-- existing:SF-2026-ARXIV-2604-23747:end -->
<!-- delta:SF-2026-ARXIV-2604-23747:start -->dataset owner 拥有 trajectory/evidence，trainer 拥有 loss 与 checkpoint commit<!-- delta:SF-2026-ARXIV-2604-23747:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-23747:end -->
<!-- books-review:SF-2026-ARXIV-2604-23758:start -->
<!-- existing:SF-2026-ARXIV-2604-23758:start -->真实 owner `books/part-07-agent/81-workflow.md#L102-deterministic-spineagentic-nodes` 正文：## Deterministic Spine，Agentic Nodes 适合 deterministic 的部分： - identity、authorization、budgets； - required gates； - retry/backoff/timeouts； - state transitions； - side-effect records； - cancellation/compensation； - terminal success criteria。 适合 model-driven 的部分： - interpreting ambiguous intent； - drafting content； - proposing plans/tool arguments； - ranking alternatives； - diagnosing unstructured failure。 这种组合既保留模型灵活性，又让业务不变量可测试。 ### 从一次性脚本到平台拥有的可编辑 DAG 自由代码生成适合探索新算子与一次性任务，因为它不要求平台预先拥有完整 operator catalog；但当结果需要被复用、可视化、协作编辑与恢复时，script 不再是足够的状态载体。更稳健的演进是让平台拥有带版本的 canonical DAG，Agent 只提交 typed mutation，backend 在 commit 前验证 schema、引用与无环性，executor 再用 run evidence 验证语义结果，visual editor 与 chat 只呈现同一 graph identity。 这条路线用 operator 生态约束换取可编辑性、审计与恢复；未知算子和短期探索仍可保留脚本分支。Skills 只是可更新的派生操作指南，既不拥有 DAG，也不能绕过平台验证。 ### Template、Realized Graph 与 Trace 不是同一个对象 固定 code-defined template 便于审查、复现和强 verifier，仍是稳定 wor；相邻章 `books/part-07-agent/80-reflection.md#L16-基本循环; books/part-07-agent/82-multi-agent.md#L16-先建立单-agent-baseline` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=876ac2cc1f59f9376dcee3315ca5f38e95345018a37b1f888b9787534e149a1d。<!-- existing:SF-2026-ARXIV-2604-23758:end -->
<!-- delta:SF-2026-ARXIV-2604-23758:start -->workflow runtime 拥有 event、checkpoint 与 transition control，model 只提出下一步<!-- delta:SF-2026-ARXIV-2604-23758:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-23758:end -->
<!-- books-review:SF-2026-ARXIV-2604-23775:start -->
<!-- existing:SF-2026-ARXIV-2604-23775:start -->真实 owner `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L177-state-ownership-与-freshness` 正文：## State ownership 与 freshness - sensor pipeline 拥有 timestamped observations； - state estimator 拥有当前 calibrated belief； - VLA/world-action model 拥有 provisional proposal； - controller 拥有 action execution lease； - safety monitor 拥有 veto / emergency stop； - environment 拥有真实 outcome； - run log 拥有 observation-action-effect evidence。 ### Policy 内部的 Latent Memory 是 Episode State，不是 Agent Memory 单帧或短 action chunk 足以处理局部连续动作，却无法长期保留遮挡物体、阶段进度和失败上下文。一个受限分支在 policy 内维护快慢两级 latent：短期 state 跟随近期 observation，curator 只把通过 admission 的片段提升到长期 state，并在读取后压缩或替换。 ```text timestamped observation + short latent → policy update and action proposal → curator admission / retrieval / condensation → episode-scoped long latent → controller validation and fresh observation reconciliation ``` 这类 memory 仍是 model-owned、episode-scoped derived state：identity 必须绑定 policy revision、embodiment、episode、 reset boundary、observat；相邻章 `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L16-从三个容易混淆的对象开始; books/part-04-training-system/27-data.md#L18-part-iv-的能力生产链` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=eb033b201edf92216070f88c082e72493073a9633bbe23a6a821e0e2fba02942。<!-- existing:SF-2026-ARXIV-2604-23775:end -->
<!-- delta:SF-2026-ARXIV-2604-23775:start -->policy 拥有 action proposal，environment/human safety layer 拥有 observation truth 与 actuation commit<!-- delta:SF-2026-ARXIV-2604-23775:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-23775:end -->
<!-- books-review:SF-2026-ARXIV-2604-23781:start -->
<!-- existing:SF-2026-ARXIV-2604-23781:start -->真实 owner `books/part-06-ai-infrastructure/66-evaluation-system.md#L78-从目标到证据而不是从指标到目标` 正文：## 从目标到证据，而不是从指标到目标 Evaluation 的起点不是“平台能采集什么 metric”，而是系统希望满足什么目标。可以把链路写成： ```text intended use and risk → evaluation specification → dataset / environment → system execution → scorer / human judgment → aggregation and uncertainty → decision policy → release / rollback / investigation → production feedback ``` `intended use` 决定什么错误重要。例如代码补全、医疗问答和广告生成都可以计算文本相似度，但相同指标不代表相同风险。评估 specification 至少应声明： ```text EvalSpec = target behavior + eligible population + failure taxonomy + metrics and scorers + slice definitions + thresholds / comparison rules + uncertainty requirement + owner and review policy ``` 如果目标没有被写清楚，团队往往会优化最容易计算的 proxy。模型变得更会迎合 judge，却未必更可靠；服务提高吞吐，却可能让 tail latency 和任务完成率下降。这不是模型“作弊”，而是控制系统给出了错误目标。；相邻章 `books/part-06-ai-infrastructure/65-kai-scheduler.md#L18-为什么-ai-cluster-需要更强的-queue-模型; books/part-06-ai-infrastructure/67-monitoring.md#L18-先定义目标再选择可测信号` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=ba07952c1fe646f17bfd554f905fb4a594aaa8676cc3e8aea0edfa2526800e09。<!-- existing:SF-2026-ARXIV-2604-23781:end -->
<!-- delta:SF-2026-ARXIV-2604-23781:start -->EvalSpec owner 冻结 subject/data/scorer，release owner 依据 run evidence 作决定<!-- delta:SF-2026-ARXIV-2604-23781:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-23781:end -->
<!-- books-review:SF-2026-ARXIV-2604-23798:start -->
<!-- existing:SF-2026-ARXIV-2604-23798:start -->真实 owner `books/part-02-model/14-self-attention.md#L219-flashattention-优化的是执行不是模型语义` 正文：## FlashAttention 优化的是执行，不是模型语义 朴素 Attention 可能把 score 和 softmax 中间结果写入 HBM，再读回做后续计算。FlashAttention 使用 tiling 与 online softmax，在片上 SRAM 可容纳的小块上组织 exact attention，减少 HBM 往返和中间存储。这是决定 Attention 能否高效执行的重要优化，但它回答的是“相同语义怎样少做 IO”，而不是“token 应该怎样建立关系”。 它没有改变： ```text Query 根据所有允许的 Keys 计算权重 再用权重聚合 Values ``` 因此需要区分： ```text Self Attention 定义模型语义与成对关系 FlashAttention 优化 exact attention 的 IO 执行 KV Cache 避免 Decode 重算历史 K/V PagedAttention 管理运行时 KV Cache 物理存储 ``` 这些技术共享 Attention 背景，却属于不同知识树节点。；相邻章 `books/part-02-model/13-position-encoding.md#L18-为什么纯-self-attention-看不见顺序; books/part-02-model/15-multi-head-attention.md#L18-单个-head-的表达瓶颈` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=dfb22afe195d183da0629f987e967476f116c9f0197be4a2ba39077b3bc113ce。<!-- existing:SF-2026-ARXIV-2604-23798:end -->
<!-- delta:SF-2026-ARXIV-2604-23798:start -->layer architecture 拥有 mixing rule，runtime 只执行已版本化 attention graph<!-- delta:SF-2026-ARXIV-2604-23798:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-23798:end -->
<!-- books-review:SF-2026-ARXIV-2604-23838:start -->
<!-- existing:SF-2026-ARXIV-2604-23838:start -->真实 owner `books/part-04-training-system/31-rlhf.md#L18-demonstration-为什么不足以表达偏好` 正文：## Demonstration 为什么不足以表达偏好 对同一个 prompt，多个回答可能都正确，但在 helpfulness、clarity、safety、conciseness 和 style 上不同。若只提供一个 SFT reference： ```text prompt -> one target response ``` 所有不同 wording 都会在 token-level loss 中偏离 reference，即使它们同样可接受。 Preference comparison 改写监督问题： ```text prompt x candidate y_a candidate y_b human chooses y_w over y_l ``` 它不要求标注者从空白开始写完美答案，却仍需要明确 rubric。若不同标注者对“好”的定义不同，pairwise label 只是某个群体、时间和 policy 下的偏好样本，不是客观真理。；相邻章 `books/part-04-training-system/30-lora.md#L18-从-full-fine-tuning-的重复状态开始; books/part-04-training-system/32-ppo.md#L18-把语言生成写成策略过程` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=f47330b0071ac1f6fd3beb7eac7bee51312e668f7c5f5fca76159edd840d2414。<!-- existing:SF-2026-ARXIV-2604-23838:end -->
<!-- delta:SF-2026-ARXIV-2604-23838:start -->We present JigsawRL, a cost-efficient framework that explores Pipeline Multiplexing as a new dimension of RL parallelism. JigsawRL decomposes each pipeline into a Sub-Stage Graph that exposes the intra-stage and inter-worker imbalance hidden by stage-level systems. On this abstraction, JigsawRL resolves multiplexing interference through dynamic resource allocation, eliminates fragmented utilization by migrating long-tail rollouts across workers, and formulates their coordination as a graph scheduling problem solved with a look-ahead heuristic. 该机制将长期 owner 定位到 `TRAIN-RLHF`，并把相应 state/control/evidence identity 从隐式约定变成可检查对象。<!-- delta:SF-2026-ARXIV-2604-23838:end --> Decision=`No Change — Existing Coverage`；evidence boundary：只接受 arXiv:2604.23838v1 的作者机制与实验；未披露硬件、precision、长度、batch、并发、成本或线上 SLO 均为 Not Disclosed。
<!-- books-review:SF-2026-ARXIV-2604-23838:end -->
<!-- books-review:SF-2026-ARXIV-2604-23853:start -->
<!-- existing:SF-2026-ARXIV-2604-23853:start -->真实 owner `books/part-06-ai-infrastructure/69-trace.md#L16-从总延迟到-critical-path` 正文：## 从总延迟到 Critical Path Gateway 看到 request latency 10 秒，可能包含： ```text auth → gateway queue → endpoint selection → backend queue → prefill → first token → repeated decode → stream close ``` 各组件日志都正常，仍无法知道哪些步骤串行、哪些并行，以及真正阻塞在哪里。Trace 用 span 的 start/end 与关系表达这条路径。；相邻章 `books/part-06-ai-infrastructure/68-logging.md#L16-文本行不是日志契约; books/part-06-ai-infrastructure/70-cost.md#L16-资源时间是共同底座` 已顺读。该主线尚未完整承载本 family 特有机制、failure 与 evidence boundary。 owner_sha256=8a6e2b64f47a5cd9c771245bdb2a811a82d2e3cebb0285c06d086c57b351ece1。<!-- existing:SF-2026-ARXIV-2604-23853:end -->
<!-- delta:SF-2026-ARXIV-2604-23853:start -->Skill-distillation pipelines learn reusable rules from LLM agent trajectories, but they lack a key signal: how much each step costs. Without per-step cost, a pipeline cannot distinguish adding a missing step to fix a bug from removing an expensive step that never affected the outcome. We use the cost-attribution gap to ask whether the rule types inside a distilled skill transfer the same way to new tasks. 该机制将长期 owner 定位到 `PLATFORM-TRACE`，并把相应 state/control/evidence identity 从隐式约定变成可检查对象。<!-- delta:SF-2026-ARXIV-2604-23853:end --> Decision=`Integrate`；evidence boundary：只接受 arXiv:2604.23853v1 的作者机制与实验；未披露硬件、precision、长度、batch、并发、成本或线上 SLO 均为 Not Disclosed。
<!-- books-review:SF-2026-ARXIV-2604-23853:end -->
<!-- books-review:SF-2026-ARXIV-2604-23887:start -->
<!-- existing:SF-2026-ARXIV-2604-23887:start -->真实 owner `books/part-06-ai-infrastructure/72-security.md#L16-从资产与信任边界开始` 正文：## 从资产与信任边界开始 需要保护的资产包括： - source data、labels 与 user context； - code、images、dependencies 与 credentials； - checkpoints、adapters、tokenizers 与 prompts； - registry metadata、evaluation 与 approvals； - GPU nodes、runtime memory 与 KV Cache； - APIs、tools、business systems 与 audit evidence。 主体包括用户、service accounts、controllers、training code、model server、model output 和 external tools。模型生成的文本不是可信主体，也不应自动获得调用者全部权限。；相邻章 `books/part-06-ai-infrastructure/71-multi-tenant.md#L16-先定义-tenant-与信任级别; books/part-06-ai-infrastructure/73-production-best-practice.md#L16-poc-隐含了哪些假设` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=cd99007e2f9b12ccf2bc7cd075bbf73c3b935255bf06bda7068b8f624de239ca。<!-- existing:SF-2026-ARXIV-2604-23887:end -->
<!-- delta:SF-2026-ARXIV-2604-23887:start -->LLM-powered applications routinely embed secrets in system prompts, yet models can be tricked into revealing them. We built an adaptive attacker that evolves its strategies over hundreds of rounds and tested it against nine defense configurations across more than 20,000 attacks. Every defense that relied on the model to protect itself eventually broke. 该机制将长期 owner 定位到 `PLATFORM-SECURITY`，并把相应 state/control/evidence identity 从隐式约定变成可检查对象。<!-- delta:SF-2026-ARXIV-2604-23887:end --> Decision=`No Change — Existing Coverage`；evidence boundary：只接受 arXiv:2604.23887v1 的作者机制与实验；未披露硬件、precision、长度、batch、并发、成本或线上 SLO 均为 Not Disclosed。
<!-- books-review:SF-2026-ARXIV-2604-23887:end -->


### Independent prewrite re-audit amendment

本轮不读取旧 Weekly 语义输入；全量 closure 反向审计重开 3 个 family，冻结 `476 = 20 retained + 456 closures`。prewrite 阶段形成 canonical Integrate queue=1；该项随后已写回 Books，并通过独立 post-write semantic audit，最终 Books Gate=`Passed`。

<!-- analysis-decision:SF-2026-ARXIV-2604-23831:start -->Full Review 与 Books comparison 已完成；未选 Top-3 仅是叙事预算。<!-- analysis-decision:SF-2026-ARXIV-2604-23831:end -->
<!-- existing:SF-2026-ARXIV-2604-23831:start -->current owner `books/part-06-ai-infrastructure/66-evaluation-system.md#L200-平均值-切片与不确定性` 已顺读：## 平均值、切片与不确定性  总体平均会把局部灾难隐藏在高频正常样本中。Evaluation System 应同时保存 per-example results、总体聚合和关键 slices：  ```text overall ├─ language / region ├─ input length / output length ├─ domain / task ├─ user or tenant class ├─ difficulty └─ safety / high-impact risk ```  如果一个二元成功指标在 \(n\) 个近似独立样本中的成功率为 \(\hat{p}\)，朴素标准误差可写为： ；相邻 refs=books/part-06-ai-infrastructure/65-kai-scheduler.md#L18-为什么-ai-cluster-需要更强的-queue-模型; books/part-06-ai-infrastructure/67-monitoring.md#L18-先定义目标-再选择可测信号。<!-- existing:SF-2026-ARXIV-2604-23831:end -->
<!-- delta:SF-2026-ARXIV-2604-23831:start -->edge AI safety contract 同时检查 output stability 与 deadline/timing，而非只比较 accuracy。<!-- delta:SF-2026-ARXIV-2604-23831:end -->
<!-- books-review:SF-2026-ARXIV-2604-23831:start -->Decision=`No Change — Existing Coverage`；仅 MobileNetV2/Jetson；GPU/CPU stack、precision 与 measurement path 不同，未验证完整 clinical workflow。<!-- books-review:SF-2026-ARXIV-2604-23831:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-23584:start -->Full Review 与 Books comparison 已完成；未选 Top-3 仅是叙事预算。<!-- analysis-decision:SF-2026-ARXIV-2604-23584:end -->
<!-- existing:SF-2026-ARXIV-2604-23584:start -->current owner `books/part-06-ai-infrastructure/72-security.md#L16-从资产与信任边界开始` 已顺读：## 从资产与信任边界开始  需要保护的资产包括：  - source data、labels 与 user context； - code、images、dependencies 与 credentials； - checkpoints、adapters、tokenizers 与 prompts； - registry metadata、evaluation 与 approvals； - GPU nodes、runtime memory 与 KV Cache； - APIs、tools、business systems 与 audit evidence。  主体包括用户、service accounts、controllers、training code、model server、model output 和 external tools。模型生成的文本不是可信主体，也不应自动获得调用者全部权限。  ## 生命周期威胁  ```text；相邻 refs=books/part-06-ai-infrastructure/71-multi-tenant.md#L16-先定义-tenant-与信任级别; books/part-06-ai-infrastructure/73-production-best-practice.md#L16-poc-隐含了哪些假设。<!-- existing:SF-2026-ARXIV-2604-23584:end -->
<!-- delta:SF-2026-ARXIV-2604-23584:start -->multimodal RAG 在保留可检索证据前提下，把视觉 identity 与任务内容解耦匿名化。<!-- delta:SF-2026-ARXIV-2604-23584:end -->
<!-- books-review:SF-2026-ARXIV-2604-23584:start -->Decision=`No Change — Existing Coverage`；作者实验不证明面对任意 re-identification auxiliary data 或跨域 corpus 都保持隐私与 utility。<!-- books-review:SF-2026-ARXIV-2604-23584:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-05397:start -->Full Review 与 Books comparison 已完成；未选 Top-3 仅是叙事预算。<!-- analysis-decision:SF-2026-ARXIV-2607-05397:end -->
<!-- existing:SF-2026-ARXIV-2607-05397:start -->current owner `books/part-07-agent/84-agent-platform.md#L413-agent-runtime-state-machine` 已顺读：## Agent Runtime State Machine  一个通用 run 可表达为：  ```text Created → ContextReady → Planning → Acting → Observing → Reflecting / Replanning → Waiting → Succeeded | Failed | Cancelled | Escalated ```  具体 workflow 可增加 domain states。关键是每次 transition 都可恢复、可审计，并绑定 actor、policy、budget 和 side-effect evidence。；相邻 refs=books/part-07-agent/83-mcp.md#L19-为什么需要协议层。<!-- existing:SF-2026-ARXIV-2607-05397:end -->
<!-- delta:SF-2026-ARXIV-2607-05397:start -->Proof of Execution 把 causal event stream、contract invariants 与 replay context 绑定，形成可检查运行证据。<!-- delta:SF-2026-ARXIV-2607-05397:end -->
<!-- books-review:SF-2026-ARXIV-2607-05397:start -->Decision=`No Change — Existing Coverage`；单节点原型；valid contract 不代表 contract 安全或选得正确，replay 也不等于现实复现，planner compromise 不在范围内。<!-- books-review:SF-2026-ARXIV-2607-05397:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260427-COVERAGE | fresh-context:april01-07-independent-reviewer | coverage | coverage:SRC-ARXIV:20260427 | none | — | passed |
| SA-20260427-EVIDENCE | fresh-context:april01-07-independent-reviewer | evidence | validator:review-completion-v1 | none | — | passed |
| SA-20260427-DEEP | fresh-context:april01-07-independent-reviewer | deep_analysis_selection | validator:deep-analysis-selection-v1 | none | — | passed |
| SA-20260427-BOOKS | fresh-context:apr26-30-independent-postwrite-reviewer | books | books-review:SF-2026-ARXIV-2604-23853 | none | 已纠正 held-out task/rule 分母，依据 `../_sources/april-26-30-books-post-write-semantic-audit.json` 复验通过 | passed |

## 8. Ignored Noise

其余 456 个 identity 均保留在 `screening-ledger-final.json`，每条具有 title、abstract、日期和 family-specific closure；recall 与 denominator retention 已分离。

## 9. Recommended Action

本日独立 Historical Daily 已闭环；后续保持 immutable parent trace、rule proposal 与 replay receipt 的责任分离。

## 10. Repository Changes

- 重建本日 final denominator、exact-v1 Source Review、Deep Selection、current Books comparison 与 writeback queue。
- 1 项 Integrate 已写入 `books/part-06-ai-infrastructure/69-trace.md`，并通过非写作者 post-write Semantic Audit。

## 11. Open Questions

- 无。本日 ordinary pending、blocked 与 unresolved semantic finding 均为 0。

## 12. Sources

- strict-window frozen inventory：`papers/2026/04/_sources/daily-20260427/inventory.json`
- exact-v1 receipts：`papers/2026/04/_sources/daily-20260427/exact-v1-review-packet.json`
- Historical Daily independence：`weekly-dependency-audit.json`（dependency=0）
- [Do Prompt-Elicited Trajectories Reflect Training-Time Reward Hacking? A Systematic Study on Monitoring Training-Time Reward Hacking in Code Generation](https://arxiv.org/abs/2604.23488v1) — exact-v1；first-public 2026-04-26；accessed 2026-09-01
- [Uncertainty Propagation in LLM-Based Systems](https://arxiv.org/abs/2604.23505v1) — exact-v1；first-public 2026-04-26；accessed 2026-09-01
- [Pref-CTRL: Preference Driven LLM Alignment using Representation Editing](https://arxiv.org/abs/2604.23543v1) — exact-v1；first-public 2026-04-26；accessed 2026-09-01
- [ClusterFusion++: Expanding Cluster-Level Fusion to Full Transformer-Block Decoding](https://arxiv.org/abs/2604.23553v1) — exact-v1；first-public 2026-04-26；accessed 2026-09-01
- [RouteNLP: Closed-Loop LLM Routing with Conformal Cascading and Distillation Co-Optimization](https://arxiv.org/abs/2604.23577v1) — exact-v1；first-public 2026-04-26；accessed 2026-09-01
- [AgentEval: DAG-Structured Step-Level Evaluation for Agentic Workflows with Error Propagation Tracking](https://arxiv.org/abs/2604.23581v1) — exact-v1；first-public 2026-04-26；accessed 2026-09-01
- [GraphPlanner: Graph Memory-Augmented Agentic Routing for Multi-Agent LLMs](https://arxiv.org/abs/2604.23626v1) — exact-v1；first-public 2026-04-26；accessed 2026-09-01
- [Structural Enforcement of Goal Integrity in AI Agents via Separation-of-Powers Architecture](https://arxiv.org/abs/2604.23646v1) — exact-v1；first-public 2026-04-26；accessed 2026-09-01
- [Spore: Efficient and Training-Free Privacy Extraction Attack on LLMs via Inference-Time Hybrid Probing](https://arxiv.org/abs/2604.23711v1) — exact-v1；first-public 2026-04-26；accessed 2026-09-01
- [SFT-then-RL Outperforms Mixed-Policy Methods for LLM Reasoning](https://arxiv.org/abs/2604.23747v1) — exact-v1；first-public 2026-04-26；accessed 2026-09-01
- [Agentic Fusion of Large Atomic and Language Models to Accelerate Superconductor Discovery](https://arxiv.org/abs/2604.23758v1) — exact-v1；first-public 2026-04-26；accessed 2026-09-01
- [Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms](https://arxiv.org/abs/2604.23775v1) — exact-v1；first-public 2026-04-26；accessed 2026-09-01
- [ClawMark: A Living-World Benchmark for Multi-Turn, Multi-Day, Multimodal Coworker Agents](https://arxiv.org/abs/2604.23781v1) — exact-v1；first-public 2026-04-27；accessed 2026-09-01
- [ELSA: Exact Linear-Scan Attention for Fast and Memory-Light Vision Transformers](https://arxiv.org/abs/2604.23798v1) — exact-v1；first-public 2026-04-27；accessed 2026-09-01
- [JigsawRL: Assembling RL Pipelines for Efficient LLM Post-Training](https://arxiv.org/abs/2604.23838v1) — exact-v1；first-public 2026-04-27；accessed 2026-09-01
- [ClawTrace: Cost-Aware Tracing for LLM Agent Skill Distillation](https://arxiv.org/abs/2604.23853v1) — exact-v1；first-public 2026-04-27；accessed 2026-09-01
- [Evaluation of Prompt Injection Defenses in Large Language Models](https://arxiv.org/abs/2604.23887v1) — exact-v1；first-public 2026-04-27；accessed 2026-09-01

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

Independent Historical Daily closure：raw/registered/screened=476/476/476、final denominator=20、closures=456、exact-v1 complete=20、pending=0、blocked=0；1/1 Integrate 已写回并通过非写作者 post-write Semantic Audit。
