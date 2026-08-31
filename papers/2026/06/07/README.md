# Daily Research — 2026-06-07

**Research Date:** 2026-06-07

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-06-06 09:00:00 ～ 2026-06-07 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；261/261 identities 完成 title+abstract semantic screening，技术 claim 仅来自 exact-v1 primary evidence 与已冻结 source packet

**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed，fresh-context Semantic Audit 无未解决 finding

## Executive Summary

Four official DataCite DOI-prefix snapshots yielded 4,000 raw overread records and 261 unique identities in the Beijing window. Full title+abstract semantic screening froze `261 = 23 retained + 238 family-specific closures`, including independent review of all 46 keyword-route negatives. Exact-v1 review is complete for 23/23 families after `2606.08317v1` was recovered from the official 18-page PDF; HTML remains unavailable but is no longer an Evidence blocker. Corrected-contract Selection conserves `23 retained = 18 eligible + 5 non-eligible`: the mutually exclusive 18-family main frontier yields exactly three non-overlapping analysis units, while five Score-6 families retain source-specific closures outside the canonical table. Books comparison covers 23/23 families: six Integrate and seventeen No Change; all six Integrate mechanisms were restored to their canonical owner chapters and then checked against the full 23-family disposition set. The recovered family is No Change because its conceptual paradigm-level selection model does not supersede Ch57's existing workload-specific platform admission contract.

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-06-07 |
| Window End | 2026-06-07 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | DEN-20260607-76380553 |
| Denominator Frozen At | 2026-08-29T21:45:00+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-06-06T09:00:00+08:00 | 2026-06-07T09:00:00+08:00 | 2026-08-29T21:45:00+08:00 | DataCite DOI-prefix `2606.06`–`.09`; exact v1 creation timestamp; 261/261 full title+abstract screen | checked | 261 | SF-2026-ARXIV-2606-07923; SF-2026-ARXIV-2606-07936; SF-2026-ARXIV-2606-07943; SF-2026-ARXIV-2606-07950; SF-2026-ARXIV-2606-07957; SF-2026-ARXIV-2606-07968; SF-2026-ARXIV-2606-07970; SF-2026-ARXIV-2606-07992; SF-2026-ARXIV-2606-08049; SF-2026-ARXIV-2606-08094; SF-2026-ARXIV-2606-08106; SF-2026-ARXIV-2606-08197; SF-2026-ARXIV-2606-08200; SF-2026-ARXIV-2606-08302; SF-2026-ARXIV-2606-08317; SF-2026-ARXIV-2606-08340; SF-2026-ARXIV-2606-08346; SF-2026-ARXIV-2606-08348; SF-2026-ARXIV-2606-08367; SF-2026-ARXIV-2606-08372; SF-2026-ARXIV-2606-08381; SF-2026-ARXIV-2606-08382; SF-2026-ARXIV-2606-09916 | pages=4; 1,000 rows/page; final cursor=end; 4,000 raw overread; strict time filter | 2026-06-07T01:00:00Z | ../_sources/daily-20260607/registered-hit-screening.json; ../_sources/daily-20260607/candidate-denominator.json; coverage:SRC-ARXIV:20260607 | — |

<!-- coverage:SRC-ARXIV:20260607:start -->
All 190 Core, 25 keyword-routed non-Core and 46 route-negative identities were semantically screened. The frozen arithmetic is `261 = 23 retain + 238 closure`; closures are family-specific and remain row-addressable in `candidate-denominator.tsv`.
<!-- coverage:SRC-ARXIV:20260607:end -->

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-07923 | arXiv:2606.07923v1 | paper-v1:2606.07923 | 2026-W23 | 2026-06-06 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-07923 | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-2026-ARXIV-2606-07923 | yes |
| SF-2026-ARXIV-2606-07936 | arXiv:2606.07936v1 | paper-v1:2606.07936 | 2026-W23 | 2026-06-06 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-07936 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-07936 | yes |
| SF-2026-ARXIV-2606-07943 | arXiv:2606.07943v1 | paper-v1:2606.07943 | 2026-W23 | 2026-06-06 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | release_security_contract | review:SF-2026-ARXIV-2606-07943 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-07943 | yes |
| SF-2026-ARXIV-2606-07950 | arXiv:2606.07950v1 | paper-v1:2606.07950 | 2026-W23 | 2026-06-06 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-07950 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-07950 | yes |
| SF-2026-ARXIV-2606-07957 | arXiv:2606.07957v1 | paper-v1:2606.07957 | 2026-W23 | 2026-06-06 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | release_security_contract | review:SF-2026-ARXIV-2606-07957 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-07957 | yes |
| SF-2026-ARXIV-2606-07968 | arXiv:2606.07968v1 | paper-v1:2606.07968 | 2026-W23 | 2026-06-06 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-07968 | self | — | new_in_window | PLATFORM-MONITORING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-07968 | yes |
| SF-2026-ARXIV-2606-07970 | arXiv:2606.07970v1 | paper-v1:2606.07970 | 2026-W23 | 2026-06-06 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-07970 | self | — | new_in_window | TRAIN-SFT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-07970 | yes |
| SF-2026-ARXIV-2606-07992 | arXiv:2606.07992v1 | paper-v1:2606.07992 | 2026-W23 | 2026-06-06 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-07992 | self | — | new_in_window | AGENT-MCP | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-07992 | yes |
| SF-2026-ARXIV-2606-08049 | arXiv:2606.08049v1 | paper-v1:2606.08049 | 2026-W23 | 2026-06-06 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-08049 | self | — | new_in_window | AGENT-WORKFLOW | Integrate | books-review:SF-2026-ARXIV-2606-08049 | yes |
| SF-2026-ARXIV-2606-08094 | arXiv:2606.08094v1 | paper-v1:2606.08094 | 2026-W23 | 2026-06-06 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-08094 | self | — | new_in_window | INFER-REQUEST-LIFECYCLE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08094 | yes |
| SF-2026-ARXIV-2606-08106 | arXiv:2606.08106v1 | paper-v1:2606.08106 | 2026-W23 | 2026-06-06 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-08106 | self | — | new_in_window | AGENT-PLATFORM | Integrate | books-review:SF-2026-ARXIV-2606-08106 | yes |
| SF-2026-ARXIV-2606-08197 | arXiv:2606.08197v1 | paper-v1:2606.08197 | 2026-W23 | 2026-06-06 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-08197 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08197 | yes |
| SF-2026-ARXIV-2606-08200 | arXiv:2606.08200v1 | paper-v1:2606.08200 | 2026-W23 | 2026-06-06 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-08200 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2606-08200 | yes |
| SF-2026-ARXIV-2606-08302 | arXiv:2606.08302v1 | paper-v1:2606.08302 | 2026-W23 | 2026-06-06 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-08302 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08302 | yes |
| SF-2026-ARXIV-2606-08317 | arXiv:2606.08317v1 | paper-v1:2606.08317 | 2026-W23 | 2026-06-06 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-08317 | self | — | new_in_window | PLATFORM-FOUNDATIONS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08317 | yes |
| SF-2026-ARXIV-2606-08340 | arXiv:2606.08340v1 | paper-v1:2606.08340 | 2026-W23 | 2026-06-06 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-08340 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08340 | yes |
| SF-2026-ARXIV-2606-08346 | arXiv:2606.08346v1 | paper-v1:2606.08346 | 2026-W23 | 2026-06-06 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-08346 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08346 | yes |
| SF-2026-ARXIV-2606-08348 | arXiv:2606.08348v1 | paper-v1:2606.08348 | 2026-W23 | 2026-06-06 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-08348 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08348 | yes |
| SF-2026-ARXIV-2606-08367 | arXiv:2606.08367v1 | paper-v1:2606.08367 | 2026-W23 | 2026-06-06 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-08367 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08367 | yes |
| SF-2026-ARXIV-2606-08372 | arXiv:2606.08372v1 | paper-v1:2606.08372 | 2026-W23 | 2026-06-06 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | release_security_contract | review:SF-2026-ARXIV-2606-08372 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08372 | yes |
| SF-2026-ARXIV-2606-08381 | arXiv:2606.08381v1 | paper-v1:2606.08381 | 2026-W23 | 2026-06-07 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-08381 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08381 | yes |
| SF-2026-ARXIV-2606-08382 | arXiv:2606.08382v1 | paper-v1:2606.08382 | 2026-W23 | 2026-06-07 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-08382 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08382 | yes |
| SF-2026-ARXIV-2606-09916 | arXiv:2606.09916v1 | paper-v1:2606.09916 | 2026-W23 | 2026-06-06 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-09916 | self | — | new_in_window | INFER-KV-CACHE | Integrate | books-review:SF-2026-ARXIV-2606-09916 | yes |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-07923 | RP-c680c902d7ada098 | deep | arXiv:2606.07923v1 | SRC-ARXIV@arXiv:2606.07923v1 | arXiv:2606.07923v1 §3 Larch; §§3.1–3.4 state, A2C, selectivity planner and latency-hiding pipeline | arXiv:2606.07923v1 §4 Experimental Evaluation; §4.1 setup; §§4.2–4.8 results, sensitivity, oracle and ablation | arXiv:2606.07923v1 §5 Discussion and Conclusion; §4.8 delayed-update counterevidence | Not Disclosed — no immutable event-time artifact revision identified | claim:SF-2026-ARXIV-2606-07923 | complete |
| SF-2026-ARXIV-2606-07936 | RP-6950153e4880d488 | deep | arXiv:2606.07936v1 | SRC-ARXIV@arXiv:2606.07936v1 | arXiv:2606.07936v1 §3 Reporting Criteria and Codebook; §4 Dataset and Methods | arXiv:2606.07936v1 §5 Results over 284 manually reviewed and 1.8k+ LLM-assisted papers | arXiv:2606.07936v1 §6 Discussion and recommendations; the codebook measures reporting, not intrinsic judgment correctness | arXiv:2606.07936v1 https://github.com/larchlab/Illusions-of-the-Gold-Standard — repository disclosed; event-time commit not pinned | claim:SF-2026-ARXIV-2606-07936 | complete |
| SF-2026-ARXIV-2606-07943 | RP-591bf06bdf9452a5 | deep | arXiv:2606.07943v1 | SRC-ARXIV@arXiv:2606.07943v1 | arXiv:2606.07943v1 §3 Poise Attack; §§3.1–3.5 eligibility, placement, generation and execution postcondition | arXiv:2606.07943v1 §4 Experimental Setup; §5 Results on Skill-Inject and SkillsBench | arXiv:2606.07943v1 §6 Limitations; audit false positives and eligible-task restriction | arXiv:2606.07943v1 SkillSafety/SkillTester artifact disclosed in manuscript; immutable event-time commit not pinned | claim:SF-2026-ARXIV-2606-07943 | complete |
| SF-2026-ARXIV-2606-07950 | RP-f45a8584f6534d21 | deep | arXiv:2606.07950v1 | SRC-ARXIV@arXiv:2606.07950v1 | arXiv:2606.07950v1 §4 CoDaPO; confidence/difficulty value, update weighting and within-mini-batch resampling | arXiv:2606.07950v1 §5 Experiments; §5.1 setup; Appendix C.6 implementation details | arXiv:2606.07950v1 §6 Conclusion; Appendix dynamic-difficulty analysis and fixed-compute boundary | arXiv:2606.07950v1 https://github.com/tmlr-group/CoDaPO — repository disclosed; event-time commit not pinned | claim:SF-2026-ARXIV-2606-07950 | complete |
| SF-2026-ARXIV-2606-07957 | RP-614affaa0c0ed258 | deep | arXiv:2606.07957v1 | SRC-ARXIV@arXiv:2606.07957v1 | arXiv:2606.07957v1 §4 Demand-Driven Architecture; formal derivation and bidirectional catalogue/asset triggers | arXiv:2606.07957v1 §8 Evaluation Methodology; complexity analysis and worked example, not executed measurements | arXiv:2606.07957v1 §10 Limitations; rule correctness and alert prioritization explicitly out of scope | Not Disclosed — architecture paper provides no executable artifact | claim:SF-2026-ARXIV-2606-07957 | complete |
| SF-2026-ARXIV-2606-07968 | RP-2131f7f81797e463 | deep | arXiv:2606.07968v1 | SRC-ARXIV@arXiv:2606.07968v1 | arXiv:2606.07968v1 §IV RecurGuard; recurrence, volume and progress signals with three-chunk termination | arXiv:2606.07968v1 §VI Experimental Setup; §VII Results and adaptive stress tests | arXiv:2606.07968v1 §XI Limitations; exposed-trace dependency and topical adaptive miss boundary | Not Disclosed — no immutable event-time artifact revision identified | claim:SF-2026-ARXIV-2606-07968 | complete |
| SF-2026-ARXIV-2606-07970 | RP-cc8fa4627aa85b66 | standard | arXiv:2606.07970v1 | SRC-ARXIV@arXiv:2606.07970v1 | arXiv:2606.07970v1 §3 Methods; bi-level Patcher inner attack and parallel implementation | arXiv:2606.07970v1 §4 Experiments; §4.1 setup and full-parameter attack transfer | arXiv:2606.07970v1 §6 Limitations and Conclusion; stronger simulated attacks remain a bounded threat-model proxy | arXiv:2606.07970v1 https://github.com/haomingwen/patcher — repository disclosed; event-time commit not pinned | claim:SF-2026-ARXIV-2606-07970 | complete |
| SF-2026-ARXIV-2606-07992 | RP-8ef9550c4fbe545e | deep | arXiv:2606.07992v1 | SRC-ARXIV@arXiv:2606.07992v1 | arXiv:2606.07992v1 §3 Methodology; seven-dimensional mutation space and controlled error-path injection | arXiv:2606.07992v1 §4 Evaluation; Appendix C.1 controlled tool-error protocol | arXiv:2606.07992v1 §5 Discussion and Conclusion; production guardrails and controlled-environment boundary | Not Disclosed — no immutable event-time artifact revision identified | claim:SF-2026-ARXIV-2606-07992 | complete |
| SF-2026-ARXIV-2606-08049 | RP-6c3238020ccefa82 | deep | arXiv:2606.08049v1 | SRC-ARXIV@arXiv:2606.08049v1 | arXiv:2606.08049v1 §3 SKILL.nb; selective formalization, versioned notebook and gate-conditioned local fallback; Appendix A | arXiv:2606.08049v1 §4 Experiments; shared Evaluation Protocol and WebArena/Mind2Web/GitLab migration slices | arXiv:2606.08049v1 §5 Limitations; Appendix A.8 lifecycle and environment-drift boundaries | Not Disclosed — no immutable event-time artifact revision identified | claim:SF-2026-ARXIV-2606-08049 | complete |
| SF-2026-ARXIV-2606-08094 | RP-1ba2dc9941ddd337 | deep | arXiv:2606.08094v1 | SRC-ARXIV@arXiv:2606.08094v1 | arXiv:2606.08094v1 §3 Runtime Design; §3.3 cached prefix/action expert and Algorithm 1 solver loop | arXiv:2606.08094v1 §4 Evaluation; §4.1 setup and 200-episode LIBERO-Object protocol | arXiv:2606.08094v1 §5 Limitations; deployment portability does not prove every VLA architecture behaviorally identical | arXiv:2606.08094v1 https://fai-modelopt-tech.github.io/vla-cpp.github.io/ — project, code and scaffold disclosed; commit not pinned | claim:SF-2026-ARXIV-2606-08094 | complete |
| SF-2026-ARXIV-2606-08106 | RP-181e2165eeb1d7c6 | deep | arXiv:2606.08106v1 | SRC-ARXIV@arXiv:2606.08106v1 | arXiv:2606.08106v1 §4 PACE; paired testing-by-betting e-process and Algorithm 1 commit gate | arXiv:2606.08106v1 §5 Experiments on prompt self-evolution with hidden real/no-gain conditions | arXiv:2606.08106v1 §6 Limitations; per-decision guarantee is not a global lifetime guarantee | Not Disclosed — no immutable event-time artifact revision identified | claim:SF-2026-ARXIV-2606-08106 | complete |
| SF-2026-ARXIV-2606-08197 | RP-1acca2d61481dff4 | deep | arXiv:2606.08197v1 | SRC-ARXIV@arXiv:2606.08197v1 | arXiv:2606.08197v1 §III AlignFed Framework; §IV version grouping, semantic calibration and fairness weighting | arXiv:2606.08197v1 §V Experimental Evaluation; §V-A setup | arXiv:2606.08197v1 §VI Conclusion and stated simulation/heterogeneous-edge scope | Not Disclosed — no immutable event-time artifact revision identified | claim:SF-2026-ARXIV-2606-08197 | complete |
| SF-2026-ARXIV-2606-08200 | RP-c424724066337887 | deep | arXiv:2606.08200v1 | SRC-ARXIV@arXiv:2606.08200v1 | arXiv:2606.08200v1 §3 Online Agent-as-a-Judge; in-world situation generation through native dialogue/action | arXiv:2606.08200v1 §4 Experiments; §4.1 life-simulation setup and human-label agreement | arXiv:2606.08200v1 §5 Discussion; evaluator intervention can change the trajectory it measures | Not Disclosed — no immutable event-time artifact revision identified | claim:SF-2026-ARXIV-2606-08200 | complete |
| SF-2026-ARXIV-2606-08302 | RP-e8b9b36b8d6d533f | standard | arXiv:2606.08302v1 | SRC-ARXIV@arXiv:2606.08302v1 | arXiv:2606.08302v1 §IV attention-head analysis; §V HACK++ calibration, decoupled attention/cache budgets and adaptive allocation | arXiv:2606.08302v1 §VI Experiments across VAR generation and understanding tasks | arXiv:2606.08302v1 §VII Conclusion; one-time calibration and VAR-specific head taxonomy bound transfer | Not Disclosed — no immutable event-time artifact revision identified | claim:SF-2026-ARXIV-2606-08302 | complete |
| SF-2026-ARXIV-2606-08317 | RP-18157f439471a95b | standard | arXiv:2606.08317v1 | SRC-ARXIV@arXiv:2606.08317v1 | arXiv:2606.08317v1 §II Methodology: Literature Selection and Analysis Framework; §VI-A Evaluation Dimensions; §IX-B Database Architecture Selection Framework, Stages 1–3 and scoring formula | arXiv:2606.08317v1 §VI-B Table I directional performance characteristics; §IX-D financial-fraud case study, Tables IV–V | arXiv:2606.08317v1 §IX-B Framework Limitations; §XI Limitations | Not Disclosed — exact-v1 PDF names no executable framework artifact or immutable repository revision | claim:SF-2026-ARXIV-2606-08317 | complete |
| SF-2026-ARXIV-2606-08340 | RP-b725cf5e0838ba57 | deep | arXiv:2606.08340v1 | SRC-ARXIV@arXiv:2606.08340v1 | arXiv:2606.08340v1 §3 alem benchmark design; procedural coordination tasks, communication and difficulty controls | arXiv:2606.08340v1 §4 Experiments; §4.1 zero-shot 13-LLM team setup and MARL reference | arXiv:2606.08340v1 §6 Limitations and Future Work; benchmark world and zero-shot policy scope | arXiv:2606.08340v1 https://github.com/alem-world/alem-env — repository disclosed; event-time commit not pinned | claim:SF-2026-ARXIV-2606-08340 | complete |
| SF-2026-ARXIV-2606-08346 | RP-fbdeac65cf8a68f0 | standard | arXiv:2606.08346v1 | SRC-ARXIV@arXiv:2606.08346v1 | arXiv:2606.08346v1 §3 CATPO; informativeness score, critique-guided healing and normalized tree weighting | arXiv:2606.08346v1 §4 Experiments; §4.1 Qwen2.5-Math-1.5B on MATH and four test benchmarks | arXiv:2606.08346v1 §5 Conclusion; single base-model/math-training regime and critique cost bound generality | Not Disclosed — no immutable event-time artifact revision identified | claim:SF-2026-ARXIV-2606-08346 | complete |
| SF-2026-ARXIV-2606-08348 | RP-73a84954614a1376 | deep | arXiv:2606.08348v1 | SRC-ARXIV@arXiv:2606.08348v1 | arXiv:2606.08348v1 §3 Bayesian-Agent; verified trajectories, posterior skill beliefs, actions and guardrails | arXiv:2606.08348v1 §4 Experiments across RealFin-Bench, SOP-Bench, Lifelong AgentBench and harness ablations | arXiv:2606.08348v1 §5 Limitations; posterior repair depends on verifiable task artifacts | arXiv:2606.08348v1 https://github.com/DataArcTech/Bayesian-Agent — repository disclosed; event-time commit not pinned | claim:SF-2026-ARXIV-2606-08348 | complete |
| SF-2026-ARXIV-2606-08367 | RP-5bf143c8206aefbc | deep | arXiv:2606.08367v1 | SRC-ARXIV@arXiv:2606.08367v1 | arXiv:2606.08367v1 §3 Platform Design; persistent memories, 120+ tools, live data and consequential governance | arXiv:2606.08367v1 §5.1 setup; §5.2 15-day cross-vendor results across five parallel worlds | arXiv:2606.08367v1 §8 Limitations; one 15-day simulation cannot establish deployment-timescale causality | arXiv:2606.08367v1 Prompts, logs and configurations released; immutable event-time revision not identified | claim:SF-2026-ARXIV-2606-08367 | complete |
| SF-2026-ARXIV-2606-08372 | RP-57893c6b157cfb73 | deep | arXiv:2606.08372v1 | SRC-ARXIV@arXiv:2606.08372v1 | arXiv:2606.08372v1 §2 taxonomy and attack families; §4 memorization test and RA-as-MIA reduction | arXiv:2606.08372v1 §3 empirical study of 14 attacks, 9 generators and 5 datasets; §4 interpretation tests | arXiv:2606.08372v1 §5.3 Limitations; black-box single-record released-table threat model | arXiv:2606.08372v1 Attack infrastructure disclosed through NIST CRC context; immutable event-time revision not pinned | claim:SF-2026-ARXIV-2606-08372 | complete |
| SF-2026-ARXIV-2606-08381 | RP-25e072b721b16333 | standard | arXiv:2606.08381v1 | SRC-ARXIV@arXiv:2606.08381v1 | arXiv:2606.08381v1 §3 comparative black-box framework; semantic-space divergence against a reference model set | arXiv:2606.08381v1 §4 Case Studies of previously reported provider-specific alignment behavior | arXiv:2606.08381v1 Limitations section; relative divergence detects difference, not absolute truth or provider intent | Not Disclosed — no immutable event-time artifact revision identified | claim:SF-2026-ARXIV-2606-08381 | complete |
| SF-2026-ARXIV-2606-08382 | RP-332f47a0d4240ac0 | deep | arXiv:2606.08382v1 | SRC-ARXIV@arXiv:2606.08382v1 | arXiv:2606.08382v1 §3 STAR-KV; differentiable thresholds, key/value-specific factorization and rank-aware quantization | arXiv:2606.08382v1 §4 Experiments; Appendix A.4 kernel and benchmark details | arXiv:2606.08382v1 §5 Conclusion and ablations; low-rank sensitivity is model/workload dependent | arXiv:2606.08382v1 https://github.com/PriyanshBhatnagar/STAR-KV — repository disclosed; event-time commit not pinned | claim:SF-2026-ARXIV-2606-08382 | complete |
| SF-2026-ARXIV-2606-09916 | RP-ab539df83510650e | deep | arXiv:2606.09916v1 | SRC-ARXIV@arXiv:2606.09916v1 | arXiv:2606.09916v1 §3 IntentKV; session QueryMemory, residual scorer and slot-map sentinel redirection | arXiv:2606.09916v1 §4 Experiments; §4.1 BCP setup and longest-query stress slice | arXiv:2606.09916v1 § Limitations (exact heading); learned pruning keeps base LLM fixed but does not prove universal task preservation | Not Disclosed — no immutable event-time artifact revision identified | claim:SF-2026-ARXIV-2606-09916 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2606-07923:start -->
<!-- claim:SF-2026-ARXIV-2606-07923:start -->
Larch: Learned Query Optimization for Semantic Predicates 处理的问题是：Online selectivity learning plus exact per-row ordering makes semantic-predicate token cost query-planner state rather than an opaque LLM charge.。旧路径把这一变化隐藏在静态规则、一次性分数、全局预算或事后处置中；exact-v1 的机制锚点是 `§3 Larch; §§3.1–3.4 state, A2C, selectivity planner and latency-hiding pipeline`。状态 owner 为 `INFER-SCHEDULING`：数据面保存该论文特有的观测与派生状态，控制面只执行其显式 gate/order/termination/commit 动作，evidence plane 则由 `§4 Experimental Evaluation; §4.1 setup; §§4.2–4.8 results, sensitivity, oracle and ablation` 提供可复核结果。

评估证明边界：workload=`Three real datasets plus three semantic-filter workloads and synthetic selectivity/horizon sweeps`；model=`Semantic-filter LLM backends and lightweight A2C/selectivity models; exact backend matrix is workload-specific`；evaluator=`Token use/cost overhead, convergence, sensitivity, oracle comparison and update latency`。它不证明未披露的 hardware/precision/batch/concurrency/SLO，也不把实验性阈值、预算或观察到的 latency 冒充生产 SLO；对应反证与外推边界在 `§5 Discussion and Conclusion; §4.8 delayed-update counterevidence`。

取舍、failure、共存与演进：Larch-Sel buys token savings with an online estimator whose errors can reorder individual rows; static PZ/Quest-style plans remain the fallback before enough labels accrue or when embeddings are unavailable. Its evolution is from global heuristic order to learned per-row selectivity plus exact dynamic programming, not a new semantic operator. Artifact 边界：`Not Disclosed — no immutable event-time artifact revision identified`。
<!-- claim:SF-2026-ARXIV-2606-07923:end -->
<!-- review:SF-2026-ARXIV-2606-07923:end -->
<!-- review:SF-2026-ARXIV-2606-07936:start -->
<!-- claim:SF-2026-ARXIV-2606-07936:start -->
Illusions of the Gold Standard: A Large-scale Analysis of Human Evaluation Protocols for Long-form Text Generation 处理的问题是：Twenty reproducibility fields separate what human judges measured, who judged, and how judgments may be interpreted; this changes the evaluation receipt contract.。旧路径把这一变化隐藏在静态规则、一次性分数、全局预算或事后处置中；exact-v1 的机制锚点是 `§3 Reporting Criteria and Codebook; §4 Dataset and Methods`。状态 owner 为 `PLATFORM-EVALUATION-SYSTEM`：数据面保存该论文特有的观测与派生状态，控制面只执行其显式 gate/order/termination/commit 动作，evidence plane 则由 `§5 Results over 284 manually reviewed and 1.8k+ LLM-assisted papers` 提供可复核结果。

评估证明边界：workload=`284 confirmed manual *CL 2023–2025 papers plus LLM-assisted labeling of the remaining long-form/human-evaluation corpus`；model=`GPT-4o-mini-2025-04-16 for automatic annotation; Gemini-2.5-Pro and Claude-3.7-Sonnet-20250219 in model-selection pilot`；evaluator=`Manual IAA; GPT-4o-mini selection on 26 papers; independent 125-paper/3,875-label validation; bootstrap reporting rates`。它不证明未披露的 hardware/precision/batch/concurrency/SLO，也不把实验性阈值、预算或观察到的 latency 冒充生产 SLO；对应反证与外推边界在 `§6 Discussion and recommendations; the codebook measures reporting, not intrinsic judgment correctness`。

取舍、failure、共存与演进：A twenty-field codebook raises reporting cost and can measure whether a study is reproducible without proving that its human judgments are valid. It coexists with task-specific quality rubrics: the contribution is a receipt schema for who judged, what was measured and how results may be interpreted. Artifact 边界：`https://github.com/larchlab/Illusions-of-the-Gold-Standard — repository disclosed; event-time commit not pinned`。
<!-- claim:SF-2026-ARXIV-2606-07936:end -->
<!-- review:SF-2026-ARXIV-2606-07936:end -->
<!-- review:SF-2026-ARXIV-2606-07943:start -->
<!-- claim:SF-2026-ARXIV-2606-07943:start -->
Poise: Position-Aware One-Instruction Skill Injection for Silent Execution on LLM Agents 处理的问题是：Postcondition-validated payload execution jointly with legitimate-task success changes skill-poisoning evidence from invocation to completed side effect, while position controls stealth and reliability.。旧路径把这一变化隐藏在静态规则、一次性分数、全局预算或事后处置中；exact-v1 的机制锚点是 `§3 Poise Attack; §§3.1–3.5 eligibility, placement, generation and execution postcondition`。状态 owner 为 `PLATFORM-SECURITY`：数据面保存该论文特有的观测与派生状态，控制面只执行其显式 gate/order/termination/commit 动作，evidence plane 则由 `§4 Experimental Setup; §5 Results on Skill-Inject and SkillsBench` 提供可复核结果。

评估证明边界：workload=`Skill-Inject 25 eligible tasks ×3 harms and SkillsBench 27 tasks ×3, two trials/configuration`；model=`codex+gpt-5.2; OpenClaw+DeepSeek-V4-Flash/Pro; Claude Code+Sonnet-4.6`；evaluator=`Joint ASR, task verifier, postcondition verifier and four-judge SkillTester delta alerts`。它不证明未披露的 hardware/precision/batch/concurrency/SLO，也不把实验性阈值、预算或观察到的 latency 冒充生产 SLO；对应反证与外推边界在 `§6 Limitations; audit false positives and eligible-task restriction`。

取舍、failure、共存与演进：Moving the payload from YAML to a locally plausible body position trades visibility for dependence on the agent reading that position. The joint verifier avoids invocation-only false success, while SkillTester's high clean-skill false-positive rate shows that LLM alerts cannot replace sandbox effect evidence or conservative skill admission. Artifact 边界：`SkillSafety/SkillTester artifact disclosed in manuscript; immutable event-time commit not pinned`。
<!-- claim:SF-2026-ARXIV-2606-07943:end -->
<!-- review:SF-2026-ARXIV-2606-07943:end -->
<!-- review:SF-2026-ARXIV-2606-07950:start -->
<!-- claim:SF-2026-ARXIV-2606-07950:start -->
The Easy, the Hard, and the Learnable: Confidence and Difficulty-Adaptive Policy Optimization for LLM Reasoning 处理的问题是：Confidence, empirical difficulty, and shrinking group advantage become explicit rollout-allocation state used for both resampling and update weighting under fixed compute.。旧路径把这一变化隐藏在静态规则、一次性分数、全局预算或事后处置中；exact-v1 的机制锚点是 `§4 CoDaPO; confidence/difficulty value, update weighting and within-mini-batch resampling`。状态 owner 为 `TRAIN-GRPO`：数据面保存该论文特有的观测与派生状态，控制面只执行其显式 gate/order/termination/commit 动作，evidence plane 则由 `§5 Experiments; §5.1 setup; Appendix C.6 implementation details` 提供可复核结果。

评估证明边界：workload=`MATH training and twelve reported math, general-reasoning and code benchmarks`；model=`Llama-3.2-1B-Instruct; Qwen2.5-Math-1.5B and 7B`；evaluator=`Accuracy across twelve benchmarks, confidence/difficulty dynamics and fixed-compute comparison`。它不证明未披露的 hardware/precision/batch/concurrency/SLO，也不把实验性阈值、预算或观察到的 latency 冒充生产 SLO；对应反证与外推边界在 `§6 Conclusion; Appendix dynamic-difficulty analysis and fixed-compute boundary`。

取舍、failure、共存与演进：Difficulty-aware resampling concentrates fixed rollout compute but can starve examples whose value estimate is initially wrong; uniform GRPO remains the neutral branch when confidence and empirical difficulty are unreliable. The result supports compute reallocation within the tested regimes, not a universal optimizer ordering. Artifact 边界：`https://github.com/tmlr-group/CoDaPO — repository disclosed; event-time commit not pinned`。
<!-- claim:SF-2026-ARXIV-2606-07950:end -->
<!-- review:SF-2026-ARXIV-2606-07950:end -->
<!-- review:SF-2026-ARXIV-2606-07957:start -->
<!-- claim:SF-2026-ARXIV-2606-07957:start -->
Demand-Driven Vulnerability Detection for Cloud Security Posture Management: Removing Human Rule Authoring from the Disclosure-to-Protection Critical Path 处理的问题是：CSPM rules become tenant-local derived state maintained bidirectionally from catalogue entries and the live asset graph, removing vendor release cadence from the protection critical path.。旧路径把这一变化隐藏在静态规则、一次性分数、全局预算或事后处置中；exact-v1 的机制锚点是 `§4 Demand-Driven Architecture; formal derivation and bidirectional catalogue/asset triggers`。状态 owner 为 `PLATFORM-SECURITY`：数据面保存该论文特有的观测与派生状态，控制面只执行其显式 gate/order/termination/commit 动作，evidence plane 则由 `§8 Evaluation Methodology; complexity analysis and worked example, not executed measurements` 提供可复核结果。

评估证明边界：workload=`No executed benchmark — formal semantics, complexity analysis, worked example and proposed evaluation methodology`；model=`Not Disclosed — no model evaluated`；evaluator=`Methodology proposes latency/resource evaluation; paper explicitly does not prove rule correctness or alert priority`。它不证明未披露的 hardware/precision/batch/concurrency/SLO，也不把实验性阈值、预算或观察到的 latency 冒充生产 SLO；对应反证与外推边界在 `§10 Limitations; rule correctness and alert prioritization explicitly out of scope`。

取舍、failure、共存与演进：Tenant-local rule derivation shortens vendor cadence but makes catalogue freshness, asset-graph correctness and rule garbage collection tenant responsibilities. Centrally authored rules remain necessary for predicates not derivable from structured feeds; the paper explicitly leaves rule correctness and alert priority outside its proof. Artifact 边界：`Not Disclosed — architecture paper provides no executable artifact`。
<!-- claim:SF-2026-ARXIV-2606-07957:end -->
<!-- review:SF-2026-ARXIV-2606-07957:end -->
<!-- review:SF-2026-ARXIV-2606-07968:start -->
<!-- claim:SF-2026-ARXIV-2606-07968:start -->
RecurGuard: Runtime Monitoring for Reasoning-Token Consumption Attacks 处理的问题是：A generation-time monitor combines recurrence, volume growth, and task progress over consecutive chunks and owns early termination of reasoning-token consumption attacks.。旧路径把这一变化隐藏在静态规则、一次性分数、全局预算或事后处置中；exact-v1 的机制锚点是 `§IV RecurGuard; recurrence, volume and progress signals with three-chunk termination`。状态 owner 为 `PLATFORM-MONITORING`：数据面保存该论文特有的观测与派生状态，控制面只执行其显式 gate/order/termination/commit 动作，evidence plane 则由 `§VI Experimental Setup; §VII Results and adaptive stress tests` 提供可复核结果。

评估证明边界：workload=`OverThink, ExtendAttack, held-out QA/code/math/summarization and adaptive stress tests`；model=`DS-R1-Qwen-7B primary; DS-R1-Llama-8B, Qwen3-8B, Llama3.1-8B, Sonnet-4.5 and Opus-4.7 slices`；evaluator=`TPR/FPR, joint miss rate, token amplification and post-hoc QDM fallback`。它不证明未披露的 hardware/precision/batch/concurrency/SLO，也不把实验性阈值、预算或观察到的 latency 冒充生产 SLO；对应反证与外推边界在 `§XI Limitations; exposed-trace dependency and topical adaptive miss boundary`。

取舍、failure、共存与演进：Early termination saves billed reasoning tokens only when traces are observable and the three signals remain anomalous; topical adaptive attacks expose a roughly 50% joint-miss boundary. QDM therefore remains a post-hoc fallback, and the monitor must not terminate benign long reasoning from a single transient alarm. Artifact 边界：`Not Disclosed — no immutable event-time artifact revision identified`。
<!-- claim:SF-2026-ARXIV-2606-07968:end -->
<!-- review:SF-2026-ARXIV-2606-07968:end -->
<!-- review:SF-2026-ARXIV-2606-07970:start -->
<!-- claim:SF-2026-ARXIV-2606-07970:start -->
Defending Against Malicious Finetuning by Scaling Train-time Adversarial Attacks 处理的问题是：Train-time adversarial attack strength becomes an inner-loop robustness control, with parallel execution preserving the stronger full-parameter threat model.。旧路径把这一变化隐藏在静态规则、一次性分数、全局预算或事后处置中；exact-v1 的机制锚点是 `§3 Methods; bi-level Patcher inner attack and parallel implementation`。状态 owner 为 `TRAIN-SFT`：数据面保存该论文特有的观测与派生状态，控制面只执行其显式 gate/order/termination/commit 动作，evidence plane 则由 `§4 Experiments; §4.1 setup and full-parameter attack transfer` 提供可复核结果。

评估证明边界：workload=`Beavertails/PKU-SafeRLHF/ToxicDPO-v2 test attacks; AdvBench, Beavertails and HEx-PHI ASR; Alpaca utility`；model=`Qwen2.5-1.5B main/ablation; Qwen3-4B and Llama3-8B generalization; Qwen3-Max harmfulness judge`；evaluator=`Attack Success Rate on three safety sets, utility, transfer and wall-clock; fully poisoned and larger-malicious-set failures retained`。它不证明未披露的 hardware/precision/batch/concurrency/SLO，也不把实验性阈值、预算或观察到的 latency 冒充生产 SLO；对应反证与外推边界在 `§6 Limitations and Conclusion; stronger simulated attacks remain a bounded threat-model proxy`。

取舍、failure、共存与演进：A stronger inner attack improves robustness to full-parameter malicious fine-tuning at extra train-time compute; the parallel algorithm reduces wall time without removing that compute. Conventional SFT alignment remains cheaper for weaker threat models, and success against simulated attacks does not certify every future poisoning strategy. Artifact 边界：`https://github.com/haomingwen/patcher — repository disclosed; event-time commit not pinned`。
<!-- claim:SF-2026-ARXIV-2606-07970:end -->
<!-- review:SF-2026-ARXIV-2606-07970:end -->
<!-- review:SF-2026-ARXIV-2606-07992:start -->
<!-- claim:SF-2026-ARXIV-2606-07992:start -->
VATS: Exploiting Implicit Authority in Error-Path Injection via Systematic Mutation 处理的问题是：Tool errors are an authority-bearing ingress path; mutation across error structure and language changes MCP trust from tool output validation to error-loop admission and containment.。旧路径把这一变化隐藏在静态规则、一次性分数、全局预算或事后处置中；exact-v1 的机制锚点是 `§3 Methodology; seven-dimensional mutation space and controlled error-path injection`。状态 owner 为 `AGENT-MCP`：数据面保存该论文特有的观测与派生状态，控制面只执行其显式 gate/order/termination/commit 动作，evidence plane 则由 `§4 Evaluation; Appendix C.1 controlled tool-error protocol` 提供可复核结果。

评估证明边界：workload=`Controlled MCP tool-error JSON with seven mutation dimensions and email-exfiltration effect`；model=`Gemini-3.1-Pro, GPT-5.5, GLM-5.1, Qwen3-Coder`；evaluator=`Injection compliance/ASR by error structure plus production-guardrail comparison`。它不证明未披露的 hardware/precision/batch/concurrency/SLO，也不把实验性阈值、预算或观察到的 latency 冒充生产 SLO；对应反证与外推边界在 `§5 Discussion and Conclusion; production guardrails and controlled-environment boundary`。

取舍、failure、共存与演进：Systematic mutation widens coverage of MCP error paths but the experiment's controlled tool errors and exfiltration action do not reproduce every production framework. Framework guardrails can still contain the path; the durable change is to treat errors as authority-bearing inputs rather than to ban tool error text. Artifact 边界：`Not Disclosed — no immutable event-time artifact revision identified`。
<!-- claim:SF-2026-ARXIV-2606-07992:end -->
<!-- review:SF-2026-ARXIV-2606-07992:end -->
<!-- review:SF-2026-ARXIV-2606-08049:start -->
<!-- claim:SF-2026-ARXIV-2606-08049:start -->
SKILL.nb: Selective Formalization and Gated Execution for Durable Agent Workflows 处理的问题是：Versioned notebooks make each reusable step auditable state and let validation gates choose code execution or local natural-language fallback when environments drift.。旧路径把这一变化隐藏在静态规则、一次性分数、全局预算或事后处置中；exact-v1 的机制锚点是 `§3 SKILL.nb; selective formalization, versioned notebook and gate-conditioned local fallback; Appendix A`。状态 owner 为 `AGENT-WORKFLOW`：数据面保存该论文特有的观测与派生状态，控制面只执行其显式 gate/order/termination/commit 动作，evidence plane 则由 `§4 Experiments; shared Evaluation Protocol and WebArena/Mind2Web/GitLab migration slices` 提供可复核结果。

评估证明边界：workload=`WebArena-Verified, Mind2Web cross-site/domain and GitLab 15.7→16.11/18.9 migration`；model=`Agent model/backend matrix is experiment-specific; no single evaluated model identity`；evaluator=`Success, retained success, bounded-repair recovery/regression and migration gap`。它不证明未披露的 hardware/precision/batch/concurrency/SLO，也不把实验性阈值、预算或观察到的 latency 冒充生产 SLO；对应反证与外推边界在 `§5 Limitations; Appendix A.8 lifecycle and environment-drift boundaries`。

取舍、failure、共存与演进：Versioned notebooks add maintenance and gate design, and a stale gate can reject reusable code or trigger excessive natural-language fallback. One-shot free-form workflows remain useful for non-repeated tasks; SKILL.nb evolves durable workflows by localizing failure and repair evidence at each step. Artifact 边界：`Not Disclosed — no immutable event-time artifact revision identified`。
<!-- claim:SF-2026-ARXIV-2606-08049:end -->
<!-- review:SF-2026-ARXIV-2606-08049:end -->
<!-- review:SF-2026-ARXIV-2606-08094:start -->
<!-- claim:SF-2026-ARXIV-2606-08094:start -->
vla.cpp: A Unified Inference Runtime for Vision-Language-Action Models 处理的问题是：A single C++ runtime owns cached vision-language prefix state, cross-attending action-expert solver steps, portable model bundles, and one request protocol across VLA families.。旧路径把这一变化隐藏在静态规则、一次性分数、全局预算或事后处置中；exact-v1 的机制锚点是 `§3 Runtime Design; §3.3 cached prefix/action expert and Algorithm 1 solver loop`。状态 owner 为 `INFER-REQUEST-LIFECYCLE`：数据面保存该论文特有的观测与派生状态，控制面只执行其显式 gate/order/termination/commit 动作，evidence plane 则由 `§4 Evaluation; §4.1 setup and 200-episode LIBERO-Object protocol` 提供可复核结果。

评估证明边界：workload=`LIBERO-Object 10 tasks ×20 episodes per architecture and ALOHA moving-target stress test`；model=`Seven VLA architectures spanning five backbones/four action heads`；evaluator=`Episode success, behavioral match, latency, memory footprint and cross-hardware roofline`。它不证明未披露的 hardware/precision/batch/concurrency/SLO，也不把实验性阈值、预算或观察到的 latency 冒充生产 SLO；对应反证与外推边界在 `§5 Limitations; deployment portability does not prove every VLA architecture behaviorally identical`。

取舍、failure、共存与演进：One portable runtime reduces Python-stack drift but requires architecture adapters, self-contained bundle conversion and hardware-specific kernels. Generic PyTorch remains the development branch for unsupported models; batch-1 roofline results identify utilization as the tested lever without proving all robot control loops meet real-time deadlines. Artifact 边界：`https://fai-modelopt-tech.github.io/vla-cpp.github.io/ — project, code and scaffold disclosed; commit not pinned`。
<!-- claim:SF-2026-ARXIV-2606-08094:end -->
<!-- review:SF-2026-ARXIV-2606-08094:end -->
<!-- review:SF-2026-ARXIV-2606-08106:start -->
<!-- claim:SF-2026-ARXIV-2606-08106:start -->
PACE: Anytime-Valid Acceptance Tests for Self-Evolving Agents 处理的问题是：Anytime-valid paired tests move self-evolution authority from noisy score improvement to a false-commit-controlled acceptor that remains valid under optional stopping.。旧路径把这一变化隐藏在静态规则、一次性分数、全局预算或事后处置中；exact-v1 的机制锚点是 `§4 PACE; paired testing-by-betting e-process and Algorithm 1 commit gate`。状态 owner 为 `AGENT-PLATFORM`：数据面保存该论文特有的观测与派生状态，控制面只执行其显式 gate/order/termination/commit 动作，evidence plane 则由 `§5 Experiments on prompt self-evolution with hidden real/no-gain conditions` 提供可复核结果。

评估证明边界：workload=`Prompt self-evolution on GSM8K, SVAMP and ARC-Challenge with hidden-real-gain and no-gain regimes`；model=`Qwen2.5 0.5B–3B agents`；evaluator=`False/harmful commits, held-out accuracy, variance and evaluation cost`。它不证明未披露的 hardware/precision/batch/concurrency/SLO，也不把实验性阈值、预算或观察到的 latency 冒充生产 SLO；对应反证与外推边界在 `§6 Limitations; per-decision guarantee is not a global lifetime guarantee`。

取舍、failure、共存与演进：PACE spends paired evaluations to avoid noisy commits and may delay acceptance of small real gains. Greedy acceptance remains faster when errors are cheap, but self-modifying production agents need the per-candidate false-commit bound; optional-stopping validity must not be misstated as a lifetime family-wise guarantee. Artifact 边界：`Not Disclosed — no immutable event-time artifact revision identified`。
<!-- claim:SF-2026-ARXIV-2606-08106:end -->
<!-- review:SF-2026-ARXIV-2606-08106:end -->
<!-- review:SF-2026-ARXIV-2606-08197:start -->
<!-- claim:SF-2026-ARXIV-2606-08197:start -->
AlignFed: Alignment-Aware Asynchronous Federated Fine-Tuning for Large Language Models in Heterogeneous Edge Environments 处理的问题是：Version grouping, calibration-set semantic alignment, and freshness/participation weighting make staleness and fairness explicit asynchronous federated aggregation state.。旧路径把这一变化隐藏在静态规则、一次性分数、全局预算或事后处置中；exact-v1 的机制锚点是 `§III AlignFed Framework; §IV version grouping, semantic calibration and fairness weighting`。状态 owner 为 `TRAIN-DISTRIBUTED-TRAINING`：数据面保存该论文特有的观测与派生状态，控制面只执行其显式 gate/order/termination/commit 动作，evidence plane 则由 `§V Experimental Evaluation; §V-A setup` 提供可复核结果。

评估证明边界：workload=`Heterogeneous asynchronous federated fine-tuning under non-IID data and staleness`；model=`Llama3-8B and Qwen3-8B`；evaluator=`Convergence, accuracy, fairness, staleness robustness, latency and communication`。它不证明未披露的 hardware/precision/batch/concurrency/SLO，也不把实验性阈值、预算或观察到的 latency 冒充生产 SLO；对应反证与外推边界在 `§VI Conclusion and stated simulation/heterogeneous-edge scope`。

取舍、failure、共存与演进：Version grouping and calibration reduce stale semantic drift but introduce calibration data, grouping delay and fairness weighting into the aggregator. Synchronous FFT remains simpler under homogeneous clients; AlignFed is the heterogeneous asynchronous branch and its single-A100 FP16 experiment does not establish large fleet SLOs. Artifact 边界：`Not Disclosed — no immutable event-time artifact revision identified`。
<!-- claim:SF-2026-ARXIV-2606-08197:end -->
<!-- review:SF-2026-ARXIV-2606-08197:end -->
<!-- review:SF-2026-ARXIV-2606-08200:start -->
<!-- claim:SF-2026-ARXIV-2606-08200:start -->
Online Agent-as-a-Judge: Situation-Generating Evaluation for Interactive Agents 处理的问题是：An in-world evaluator actively creates criterion-relevant situations through native dialogue/action, changing evaluation from passive trajectory scoring to coverage-seeking intervention.。旧路径把这一变化隐藏在静态规则、一次性分数、全局预算或事后处置中；exact-v1 的机制锚点是 `§3 Online Agent-as-a-Judge; in-world situation generation through native dialogue/action`。状态 owner 为 `PLATFORM-EVALUATION-SYSTEM`：数据面保存该论文特有的观测与派生状态，控制面只执行其显式 gate/order/termination/commit 动作，evidence plane 则由 `§4 Experiments; §4.1 life-simulation setup and human-label agreement` 提供可复核结果。

评估证明边界：workload=`Life simulation: five characters, 32 social criteria, three target backends × three seeds`；model=`Target-agent backends vary; all automated judges use GPT-5.4-mini`；evaluator=`Criteria coverage and agreement with human labels versus passive judges`。它不证明未披露的 hardware/precision/batch/concurrency/SLO，也不把实验性阈值、预算或观察到的 latency 冒充生产 SLO；对应反证与外推边界在 `§5 Discussion; evaluator intervention can change the trajectory it measures`。

取舍、failure、共存与演进：An active judge improves criterion coverage by changing the situation, so its actions become part of the evidence-generating treatment and may confound natural behavior. Passive trajectory scoring remains necessary for observational questions; the two modes must be reported separately and the judge must never repair the target trajectory. Artifact 边界：`Not Disclosed — no immutable event-time artifact revision identified`。
<!-- claim:SF-2026-ARXIV-2606-08200:end -->
<!-- review:SF-2026-ARXIV-2606-08200:end -->
<!-- review:SF-2026-ARXIV-2606-08302:start -->
<!-- claim:SF-2026-ARXIV-2606-08302:start -->
HACK++: Towards More Effective Head-Aware Key-Value Compression for Efficient Visual Autoregressive Modeling 处理的问题是：Head role, layer, and generation step control separate attention and retained-cache budgets for visual autoregressive decoding instead of applying one global compression ratio.。旧路径把这一变化隐藏在静态规则、一次性分数、全局预算或事后处置中；exact-v1 的机制锚点是 `§IV attention-head analysis; §V HACK++ calibration, decoupled attention/cache budgets and adaptive allocation`。状态 owner 为 `INFER-KV-CACHE`：数据面保存该论文特有的观测与派生状态，控制面只执行其显式 gate/order/termination/commit 动作，evidence plane 则由 `§VI Experiments across VAR generation and understanding tasks` 提供可复核结果。

评估证明边界：workload=`Multiple VAR models over text-to-image, class-conditional and unified understanding/generation tasks`；model=`Infinity-2B/8B and additional VAR models in §VI`；evaluator=`Generation quality, task accuracy, attention/cache budget and robustness to 1% cache`。它不证明未披露的 hardware/precision/batch/concurrency/SLO，也不把实验性阈值、预算或观察到的 latency 冒充生产 SLO；对应反证与外推边界在 `§VII Conclusion; one-time calibration and VAR-specific head taxonomy bound transfer`。

取舍、failure、共存与演进：Head-type calibration and separate attention/cache budgets improve aggressive VAR compression but can age when model, layer behavior or generation regime changes. Global compression remains the simpler branch; HACK++ is VAR-specific evidence and does not displace general LLM KV retention owners. Artifact 边界：`Not Disclosed — no immutable event-time artifact revision identified`。
<!-- claim:SF-2026-ARXIV-2606-08302:end -->
<!-- review:SF-2026-ARXIV-2606-08302:end -->
<!-- review:SF-2026-ARXIV-2606-08317:start -->
<!-- claim:SF-2026-ARXIV-2606-08317:start -->
Architectural Evolution and Selection Framework for Database Systems in AI-Ready Data Platforms 处理的问题是：Nine dimensions, workload characterization, constraint filtering, and compatibility scoring make polyglot database choice a reviewable platform decision rather than intuition.。旧路径把这一变化隐藏在静态规则、一次性分数、全局预算或事后处置中；exact-v1 的机制锚点是 `§II Methodology: Literature Selection and Analysis Framework; §VI-A Evaluation Dimensions; §IX-B Database Architecture Selection Framework, Stages 1–3 and scoring formula`。状态 owner 为 `PLATFORM-FOUNDATIONS`：数据面保存该论文特有的观测与派生状态，控制面只执行其显式 gate/order/termination/commit 动作，evidence plane 则由 `§VI-B Table I directional performance characteristics; §IX-D financial-fraud case study, Tables IV–V` 提供可复核结果。

评估证明边界：workload=`Conceptual comparison of 13 database paradigms plus one representative financial-fraud architecture case; Table I ranges are directional literature synthesis, not a controlled benchmark`；model=`Not Disclosed — no model is evaluated`；evaluator=`Qualitative compatibility values 1/2/3 weighted by workload importance; financial case maximum score 90; no product-level empirical evaluator`。它不证明未披露的 hardware/precision/batch/concurrency/SLO，也不把实验性阈值、预算或观察到的 latency 冒充生产 SLO；对应反证与外推边界在 `§IX-B Framework Limitations; §XI Limitations`。

取舍、failure、共存与演进：Workload profiling and hard filtering make architecture choice auditable, but the compatibility values are qualitative paradigm-level judgments and the fraud example is illustrative rather than a controlled product benchmark. Existing platform admission and one-size-fits-all safeguards remain the owner contract; product-specific measurements, deployment constraints and empirical validation must precede any commit. Artifact 边界：`Not Disclosed — exact-v1 PDF names no executable framework artifact or immutable repository revision`。
<!-- claim:SF-2026-ARXIV-2606-08317:end -->
<!-- review:SF-2026-ARXIV-2606-08317:end -->
<!-- review:SF-2026-ARXIV-2606-08340:start -->
<!-- claim:SF-2026-ARXIV-2606-08340:start -->
Benchmarking Open-Ended Multi-Agent Coordination in Language Agents 处理的问题是：A long-horizon world separates individual task reward from coordination reward while controlling communication, role specialization, and coordination difficulty.。旧路径把这一变化隐藏在静态规则、一次性分数、全局预算或事后处置中；exact-v1 的机制锚点是 `§3 alem benchmark design; procedural coordination tasks, communication and difficulty controls`。状态 owner 为 `AGENT-MULTI-AGENT`：数据面保存该论文特有的观测与派生状态，控制面只执行其显式 gate/order/termination/commit 动作，evidence plane 则由 `§4 Experiments; §4.1 zero-shot 13-LLM team setup and MARL reference` 提供可复核结果。

评估证明边界：workload=`Procedural long-horizon alem world across coordination difficulty; homogeneous teams and MARL references`；model=`13 modern LLMs zero-shot; named frontier examples include Gemini-3.1-Pro-High and GPT-5.4-High`；evaluator=`Normalized return split into base-task and coordination reward; communication/memory/reasoning ablations`。它不证明未披露的 hardware/precision/batch/concurrency/SLO，也不把实验性阈值、预算或观察到的 latency 冒充生产 SLO；对应反证与外推边界在 `§6 Limitations and Future Work; benchmark world and zero-shot policy scope`。

取舍、failure、共存与演进：Alem makes coordination measurable by imposing a particular procedural ecology, reward split and communication channel; strong return there need not transfer to open production teams. Short structured benchmarks remain useful for isolated skills, while alem adds long-horizon coordination stress rather than a universal agent ranking. Artifact 边界：`https://github.com/alem-world/alem-env — repository disclosed; event-time commit not pinned`。
<!-- claim:SF-2026-ARXIV-2606-08340:end -->
<!-- review:SF-2026-ARXIV-2606-08340:end -->
<!-- review:SF-2026-ARXIV-2606-08346:start -->
<!-- claim:SF-2026-ARXIV-2606-08346:start -->
CATPO: Critique-Augmented Tree Policy Optimization 处理的问题是：Tree outcome diversity and policy-reward decorrelation identify low-signal rollout trees; critique-guided grafting repairs all-fail branches before informativeness-weighted updates.。旧路径把这一变化隐藏在静态规则、一次性分数、全局预算或事后处置中；exact-v1 的机制锚点是 `§3 CATPO; informativeness score, critique-guided healing and normalized tree weighting`。状态 owner 为 `TRAIN-GRPO`：数据面保存该论文特有的观测与派生状态，控制面只执行其显式 gate/order/termination/commit 动作，evidence plane 则由 `§4 Experiments; §4.1 Qwen2.5-Math-1.5B on MATH and four test benchmarks` 提供可复核结果。

评估证明边界：workload=`Qwen2.5-Math-1.5B trained on MATH; AIME24, MATH-500, OlympiadBench and MinervaMath`；model=`Qwen2.5-Math-1.5B`；evaluator=`Pass@1/Avg@8 and macro accuracy; tree-informativeness/healing ablations`。它不证明未披露的 hardware/precision/batch/concurrency/SLO，也不把实验性阈值、预算或观察到的 latency 冒充生产 SLO；对应反证与外推边界在 `§5 Conclusion; single base-model/math-training regime and critique cost bound generality`。

取舍、failure、共存与演进：Critique-guided healing recovers all-fail trees but adds critique generation and can graft a persuasive wrong repair. Flat GRPO/TreeRPO remain simpler when trees already contain mixed outcomes; evidence is limited to one math model/training corpus and four math benchmarks. Artifact 边界：`Not Disclosed — no immutable event-time artifact revision identified`。
<!-- claim:SF-2026-ARXIV-2606-08346:end -->
<!-- review:SF-2026-ARXIV-2606-08346:end -->
<!-- review:SF-2026-ARXIV-2606-08348:start -->
<!-- claim:SF-2026-ARXIV-2606-08348:start -->
Bayesian-Agent: Posterior-Guided Skill Evolution for LLM Agent Harnesses 处理的问题是：Verified trajectories and posterior beliefs turn skills into evidence-bearing lifecycle objects with auditable update and guardrail actions across harnesses.。旧路径把这一变化隐藏在静态规则、一次性分数、全局预算或事后处置中；exact-v1 的机制锚点是 `§3 Bayesian-Agent; verified trajectories, posterior skill beliefs, actions and guardrails`。状态 owner 为 `AGENT-PLATFORM`：数据面保存该论文特有的观测与派生状态，控制面只执行其显式 gate/order/termination/commit 动作，evidence plane 则由 `§4 Experiments across RealFin-Bench, SOP-Bench, Lifelong AgentBench and harness ablations` 提供可复核结果。

评估证明边界：workload=`SOP-Bench, Lifelong AgentBench and RealFin-Bench across native, GenericAgent, mini-swe-agent and Claude Code backends`；model=`deepseek-v4-flash and deepseek-v4-pro for Bayesian variants; Claude Sonnet-4.6, Claude Opus-4.6 and GPT-5.4 comparison rows`；evaluator=`Task accuracy, token accounting, efficiency, full/incremental repair and backend/model ablations`。它不证明未披露的 hardware/precision/batch/concurrency/SLO，也不把实验性阈值、预算或观察到的 latency 冒充生产 SLO；对应反证与外推边界在 `§5 Limitations; posterior repair depends on verifiable task artifacts`。

取舍、failure、共存与演进：Posterior skill actions are only as trustworthy as priors, verified trajectory artifacts and the harness's failure taxonomy; sparse evidence can make repair conservative. Raw empirical rates remain transparent with abundant homogeneous trials, while Bayesian-Agent owns finite-sample cross-harness uncertainty rather than model-weight learning. Artifact 边界：`https://github.com/DataArcTech/Bayesian-Agent — repository disclosed; event-time commit not pinned`。
<!-- claim:SF-2026-ARXIV-2606-08348:end -->
<!-- review:SF-2026-ARXIV-2606-08348:end -->
<!-- review:SF-2026-ARXIV-2606-08367:start -->
<!-- claim:SF-2026-ARXIV-2606-08367:start -->
Emergence World: A Platform for Evaluating Long-Horizon Multi-Agent Autonomy 处理的问题是：Continuously running heterogeneous agent populations, persistent memories, consequential governance, and live exogenous data expose drift and cross-influence absent from exam-style evaluation.。旧路径把这一变化隐藏在静态规则、一次性分数、全局预算或事后处置中；exact-v1 的机制锚点是 `§3 Platform Design; persistent memories, 120+ tools, live data and consequential governance`。状态 owner 为 `PLATFORM-EVALUATION-SYSTEM`：数据面保存该论文特有的观测与派生状态，控制面只执行其显式 gate/order/termination/commit 动作，evidence plane 则由 `§5.1 setup; §5.2 15-day cross-vendor results across five parallel worlds` 提供可复核结果。

评估证明边界：workload=`15 days, five parallel worlds, ten agents/world, 120+ tools and three memories`；model=`Claude Sonnet-4.6, Grok-4.1-Fast, Gemini-3-Flash, GPT-5-mini and mixed population`；evaluator=`Cross-world behavioral trajectories, governance stability/collapse and released logs`。它不证明未披露的 hardware/precision/batch/concurrency/SLO，也不把实验性阈值、预算或观察到的 latency 冒充生产 SLO；对应反证与外推边界在 `§8 Limitations; one 15-day simulation cannot establish deployment-timescale causality`。

取舍、failure、共存与演进：Continuous worlds expose drift and cross-influence at the cost of API nondeterminism, high run expense and difficult causal attribution. Exam-style benchmarks remain the controlled complement; a 15-day, five-world observation demonstrates observability, not deployment-timescale safety or vendor superiority. Artifact 边界：`Prompts, logs and configurations released; immutable event-time revision not identified`。
<!-- claim:SF-2026-ARXIV-2606-08367:end -->
<!-- review:SF-2026-ARXIV-2606-08367:end -->
<!-- review:SF-2026-ARXIV-2606-08372:start -->
<!-- claim:SF-2026-ARXIV-2606-08372:start -->
SoK: Reconstruction Attacks on Synthetic Tabular Data (Insights from Winning the NIST CRC) 处理的问题是：A memorization test distinguishes population reconstruction from training-record leakage and maps reconstruction and membership inference to one comparable privacy-risk scale.。旧路径把这一变化隐藏在静态规则、一次性分数、全局预算或事后处置中；exact-v1 的机制锚点是 `§2 taxonomy and attack families; §4 memorization test and RA-as-MIA reduction`。状态 owner 为 `PLATFORM-SECURITY`：数据面保存该论文特有的观测与派生状态，控制面只执行其显式 gate/order/termination/commit 动作，evidence plane 则由 `§3 empirical study of 14 attacks, 9 generators and 5 datasets; §4 interpretation tests` 提供可复核结果。

评估证明边界：workload=`14 attacks ×9 synthetic-data generators ×5 datasets; QI sizes 3–16; DP epsilon sweeps`；model=`Classifiers, graphical models and diffusion/generative attack families; not one LLM`；evaluator=`Rarity-weighted reconstruction advantage, train/holdout memorization gap and RA-as-MIA comparison`。它不证明未披露的 hardware/precision/batch/concurrency/SLO，也不把实验性阈值、预算或观察到的 latency 冒充生产 SLO；对应反证与外推边界在 `§5.3 Limitations; black-box single-record released-table threat model`。

取舍、failure、共存与演进：The unified risk scale improves comparability but remains a black-box, single-record released-table threat model; model inversion, aggregate reconstruction and coordinated targets stay separate branches. The train/holdout gap prevents high reconstruction accuracy from being mislabeled as memorization, especially for rare records. Artifact 边界：`Attack infrastructure disclosed through NIST CRC context; immutable event-time revision not pinned`。
<!-- claim:SF-2026-ARXIV-2606-08372:end -->
<!-- review:SF-2026-ARXIV-2606-08372:end -->
<!-- review:SF-2026-ARXIV-2606-08381:start -->
<!-- claim:SF-2026-ARXIV-2606-08381:start -->
Auditing Proprietary Alignment in Large Language Models: A Comparative Framework Without a Ground-Truth Standard 处理的问题是：Reference-set-relative semantic divergence provides a black-box audit contract for provider-specific alignment when absolute ground truth is unavailable.。旧路径把这一变化隐藏在静态规则、一次性分数、全局预算或事后处置中；exact-v1 的机制锚点是 `§3 comparative black-box framework; semantic-space divergence against a reference model set`。状态 owner 为 `PLATFORM-EVALUATION-SYSTEM`：数据面保存该论文特有的观测与派生状态，控制面只执行其显式 gate/order/termination/commit 动作，evidence plane 则由 `§4 Case Studies of previously reported provider-specific alignment behavior` 提供可复核结果。

评估证明边界：workload=`Three black-box cases: DeepSeek-R1 on China- and US-sensitive domains, and Meta AI Chat/Llama 4 on Meta-related topics`；model=`DeepSeek-R1 and Meta AI Chat/Llama 4 targets; diverse baseline ensemble; GPT-5.2 and Gemini-3.1-Flash-Lite judges; four embedding models`；evaluator=`Welch one-sided t-test, bootstrap median test, target-permutation diagnostic; relative divergence not absolute correctness or intent`。它不证明未披露的 hardware/precision/batch/concurrency/SLO，也不把实验性阈值、预算或观察到的 latency 冒充生产 SLO；对应反证与外推边界在 `Limitations section; relative divergence detects difference, not absolute truth or provider intent`。

取舍、failure、共存与演进：Relative semantic divergence depends on the reference-set composition and can detect systematic difference without identifying truth, provider intent or harm. Ground-truth task evaluation remains necessary where labels exist; this framework is the black-box comparative branch for otherwise unobservable policy variation. Artifact 边界：`Not Disclosed — no immutable event-time artifact revision identified`。
<!-- claim:SF-2026-ARXIV-2606-08381:end -->
<!-- review:SF-2026-ARXIV-2606-08381:end -->
<!-- review:SF-2026-ARXIV-2606-08382:start -->
<!-- claim:SF-2026-ARXIV-2606-08382:start -->
STAR-KV: Low-Rank KV Cache Compression via Soft Thresholding for Adaptive Rank Control 处理的问题是：Differentiable head/block thresholds, sensitivity-specific factorization, and rank-aware mixed precision turn KV rank into adaptive runtime compression state backed by kernels.。旧路径把这一变化隐藏在静态规则、一次性分数、全局预算或事后处置中；exact-v1 的机制锚点是 `§3 STAR-KV; differentiable thresholds, key/value-specific factorization and rank-aware quantization`。状态 owner 为 `INFER-KV-CACHE`：数据面保存该论文特有的观测与派生状态，控制面只执行其显式 gate/order/termination/commit 动作，evidence plane 则由 `§4 Experiments; Appendix A.4 kernel and benchmark details` 提供可复核结果。

评估证明边界：workload=`WikiText-2 perplexity, six LM-Eval tasks, LongBench and 4K RULER plus kernel/throughput slices`；model=`LongChat-7B-v1.5, Llama-2-7B, Llama-3-8B-Instruct and Llama-3.1-8B-Instruct long-context slice`；evaluator=`Perplexity, zero-shot accuracy, LongBench/RULER, compression, attention speedup and end-to-end throughput`。它不证明未披露的 hardware/precision/batch/concurrency/SLO，也不把实验性阈值、预算或观察到的 latency 冒充生产 SLO；对应反证与外推边界在 `§5 Conclusion and ablations; low-rank sensitivity is model/workload dependent`。

取舍、failure、共存与演进：Adaptive rank and mixed precision need learned thresholds, decomposition choices and custom Triton kernels; sensitivity can move across heads, blocks, models and workloads. Fixed-rank compression remains easier to deploy, and throughput gains cannot be transferred beyond the disclosed GPU/kernel slices. Artifact 边界：`https://github.com/PriyanshBhatnagar/STAR-KV — repository disclosed; event-time commit not pinned`。
<!-- claim:SF-2026-ARXIV-2606-08382:end -->
<!-- review:SF-2026-ARXIV-2606-08382:end -->
<!-- review:SF-2026-ARXIV-2606-09916:start -->
<!-- claim:SF-2026-ARXIV-2606-09916:start -->
IntentKV: Cross-Turn Intent-Aware KV Cache Pruning for Agent Inference 处理的问题是：Cross-turn QueryMemory controls live-token retention while slot-map redirection preserves surviving rows, RoPE phase, and prefix-cache identity during eviction.。旧路径把这一变化隐藏在静态规则、一次性分数、全局预算或事后处置中；exact-v1 的机制锚点是 `§3 IntentKV; session QueryMemory, residual scorer and slot-map sentinel redirection`。状态 owner 为 `INFER-KV-CACHE`：数据面保存该论文特有的观测与派生状态，控制面只执行其显式 gate/order/termination/commit 动作，evidence plane 则由 `§4 Experiments; §4.1 BCP setup and longest-query stress slice` 提供可复核结果。

评估证明边界：workload=`BCP agent benchmark plus the 100 longest commonly completed Qwen2.5-14B queries`；model=`Qwen3-8B and Qwen2.5-14B`；evaluator=`Task accuracy, peak request tokens, worst-case raw KV reads and full-cache fidelity`。它不证明未披露的 hardware/precision/batch/concurrency/SLO，也不把实验性阈值、预算或观察到的 latency 冒充生产 SLO；对应反证与外推边界在 `§ Limitations (exact heading); learned pruning keeps base LLM fixed but does not prove universal task preservation`。

取舍、failure、共存与演进：QueryMemory scoring adds session state and can irreversibly drop evidence when intent changes; sentinel redirection preserves physical identity but not information already evicted. Full cache remains the correctness fallback, while budgeted pruning is justified only by the BCP fidelity and read-volume evidence reported for the two Qwen models. Artifact 边界：`Not Disclosed — no immutable event-time artifact revision identified`。
<!-- claim:SF-2026-ARXIV-2606-09916:end -->
<!-- review:SF-2026-ARXIV-2606-09916:end -->

## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-07923 | Three real datasets plus three semantic-filter workloads and synthetic selectivity/horizon sweeps | Semantic-filter LLM backends and lightweight A2C/selectivity models; exact backend matrix is workload-specific | Not Disclosed — §4.1 does not bind one hardware topology to every result | Not Disclosed | Rows/documents with precomputed embeddings; no token length contract | Filter outcomes and token calls; no output-token length contract | Not Disclosed | Not Disclosed | Not Disclosed — token cost is an outcome, not an acceptance SLO | Token use/cost overhead, convergence, sensitivity, oracle comparison and update latency |
| SF-2026-ARXIV-2606-07936 | 284 confirmed manual *CL 2023–2025 papers plus LLM-assisted labeling of the remaining long-form/human-evaluation corpus | GPT-4o-mini-2025-04-16 for automatic annotation; Gemini-2.5-Pro and Claude-3.7-Sonnet-20250219 in model-selection pilot | Not Disclosed | Not Disclosed | Abstract, introduction, candidate human-evaluation sections and appendix passages | Five chunks of codebook answers as flat JSON; up to two full reruns after validation failure | Not Disclosed — question chunks are separate API calls, not a disclosed batch size | Not Disclosed | Only fields with held-out validation accuracy >0.75 are reported; this is a reporting threshold, not service SLO | Manual IAA; GPT-4o-mini selection on 26 papers; independent 125-paper/3,875-label validation; bootstrap reporting rates |
| SF-2026-ARXIV-2606-07943 | Skill-Inject 25 eligible tasks ×3 harms and SkillsBench 27 tasks ×3, two trials/configuration | codex+gpt-5.2; OpenClaw+DeepSeek-V4-Flash/Pro; Claude Code+Sonnet-4.6 | Docker/Harbor sandbox; host accelerator not disclosed | Not Disclosed | Skill files and task contexts; no fixed token length | One injected instruction plus legitimate task completion | Not Disclosed | Not Disclosed | ASR requires sandbox postcondition and passing legitimate-task verifier | Joint ASR, task verifier, postcondition verifier and four-judge SkillTester delta alerts |
| SF-2026-ARXIV-2606-07950 | MATH training and twelve reported math, general-reasoning and code benchmarks | Llama-3.2-1B-Instruct; Qwen2.5-Math-1.5B and 7B | 4×NVIDIA A100 | Not Disclosed | Dataset-defined prompts; no fixed input length | Evaluation uses 32 responses at temperature 0.6; no fixed output cap disclosed | 16; 8 rollouts per group | Not Disclosed | Not Disclosed | Accuracy across twelve benchmarks, confidence/difficulty dynamics and fixed-compute comparison |
| SF-2026-ARXIV-2606-07957 | No executed benchmark — formal semantics, complexity analysis, worked example and proposed evaluation methodology | Not Disclosed — no model evaluated | Not Disclosed | Not Disclosed | Catalogue entries and live asset graphs; no fixed size | Derived tenant-local rules | Not Disclosed | Not Disclosed | Not Disclosed | Methodology proposes latency/resource evaluation; paper explicitly does not prove rule correctness or alert priority |
| SF-2026-ARXIV-2606-07968 | OverThink, ExtendAttack, held-out QA/code/math/summarization and adaptive stress tests | DS-R1-Qwen-7B primary; DS-R1-Llama-8B, Qwen3-8B, Llama3.1-8B, Sonnet-4.5 and Opus-4.7 slices | NVIDIA A100 for open models; count/topology not disclosed | Not Disclosed | Prompt/task dependent | Reasoning trace analyzed in 64-word chunks | Not Disclosed | Not Disclosed | Three consecutive anomalous chunks is termination policy, not a service SLO | TPR/FPR, joint miss rate, token amplification and post-hoc QDM fallback |
| SF-2026-ARXIV-2606-07970 | Beavertails/PKU-SafeRLHF/ToxicDPO-v2 test attacks; AdvBench, Beavertails and HEx-PHI ASR; Alpaca utility | Qwen2.5-1.5B main/ablation; Qwen3-4B and Llama3-8B generalization; Qwen3-Max harmfulness judge | Not Disclosed | Not Disclosed | 200 unsafe Beavertails plus 800 GSM8K samples in default test-time mix | Maximum 256 generated tokens; temperature 0.6 and top-p 0.9 | Global batch 4 for attack, defense, baselines and test-time attack | Parallel attack/defense loops use stale attack vectors; worker concurrency not disclosed | Not Disclosed | Attack Success Rate on three safety sets, utility, transfer and wall-clock; fully poisoned and larger-malicious-set failures retained |
| SF-2026-ARXIV-2606-07992 | Controlled MCP tool-error JSON with seven mutation dimensions and email-exfiltration effect | Gemini-3.1-Pro, GPT-5.5, GLM-5.1, Qwen3-Coder | Provider APIs; hardware not disclosed | Not Disclosed | Controlled agent/tool contexts; no fixed token length | Tool-call compliance/effect | Not Disclosed | Not Disclosed | Not Disclosed | Injection compliance/ASR by error structure plus production-guardrail comparison |
| SF-2026-ARXIV-2606-08049 | WebArena-Verified, Mind2Web cross-site/domain and GitLab 15.7→16.11/18.9 migration | Agent model/backend matrix is experiment-specific; no single evaluated model identity | Not Disclosed | Not Disclosed | Workflow steps, pages and notebook evidence; no fixed token length | Task actions, screenshots and traces | Not Disclosed | Three re-executions for durability; not concurrency | Gates are per-step validity policies, not service SLOs | Success, retained success, bounded-repair recovery/regression and migration gap |
| SF-2026-ARXIV-2606-08094 | LIBERO-Object 10 tasks ×20 episodes per architecture and ALOHA moving-target stress test | Seven VLA architectures spanning five backbones/four action heads | RTX 3060; Jetson AGX Orin; 8GB Jetson Orin Nano | Model/package-specific; no one precision contract | Vision-language prefix and robot observation; no fixed token length | Action-expert solver steps | Batch 1 | One request at a time in roofline slice; broader concurrency not disclosed | Not Disclosed | Episode success, behavioral match, latency, memory footprint and cross-hardware roofline |
| SF-2026-ARXIV-2606-08106 | Prompt self-evolution on GSM8K, SVAMP and ARC-Challenge with hidden-real-gain and no-gain regimes | Qwen2.5 0.5B–3B agents | Not Disclosed | Not Disclosed | Paired identical evaluation instances | Commit/reject decisions and task answers | Not Disclosed | Sequential optional stopping; no concurrent execution contract | User-set per-candidate false-commit probability | False/harmful commits, held-out accuracy, variance and evaluation cost |
| SF-2026-ARXIV-2606-08197 | Heterogeneous asynchronous federated fine-tuning under non-IID data and staleness | Llama3-8B and Qwen3-8B | Single NVIDIA A100 | FP16 | Maximum sequence length 650 | Not Disclosed | Batch 1 | Asynchronous clients; fixed concurrent-client count not disclosed | Communication budget ≤50MB is a constraint, not latency SLO | Convergence, accuracy, fairness, staleness robustness, latency and communication |
| SF-2026-ARXIV-2606-08200 | Life simulation: five characters, 32 social criteria, three target backends × three seeds | Target-agent backends vary; all automated judges use GPT-5.4-mini | Provider APIs; hardware not disclosed | Not Disclosed | Interactive social histories; no fixed token length | Dialogue/actions and criterion evidence | Not Disclosed | Five-character world; no request concurrency contract | Not Disclosed | Criteria coverage and agreement with human labels versus passive judges |
| SF-2026-ARXIV-2606-08302 | Multiple VAR models over text-to-image, class-conditional and unified understanding/generation tasks | Infinity-2B/8B and additional VAR models in §VI | Not Disclosed | Not Disclosed | Multi-scale visual-token histories | Generated images/tokens | Not Disclosed | Not Disclosed | 30% attention/10% cache are budgets, not SLOs | Generation quality, task accuracy, attention/cache budget and robustness to 1% cache |
| SF-2026-ARXIV-2606-08317 | Conceptual comparison of 13 database paradigms plus one representative financial-fraud architecture case; Table I ranges are directional literature synthesis, not a controlled benchmark | Not Disclosed — no model is evaluated | Not Disclosed | Not Disclosed | Workload profile over nine architectural dimensions; no fixed input length | Ranked paradigm/architecture recommendation; no fixed output length | Not Disclosed | Not Disclosed | Not Disclosed | Qualitative compatibility values 1/2/3 weighted by workload importance; financial case maximum score 90; no product-level empirical evaluator |
| SF-2026-ARXIV-2606-08340 | Procedural long-horizon alem world across coordination difficulty; homogeneous teams and MARL references | 13 modern LLMs zero-shot; named frontier examples include Gemini-3.1-Pro-High and GPT-5.4-High | Not Disclosed | Not Disclosed | World observations and communication histories | Actions/messages over long horizons | Not Disclosed | Team size/configuration disclosed per environment; serving concurrency not disclosed | Not Disclosed | Normalized return split into base-task and coordination reward; communication/memory/reasoning ablations |
| SF-2026-ARXIV-2606-08346 | Qwen2.5-Math-1.5B trained on MATH; AIME24, MATH-500, OlympiadBench and MinervaMath | Qwen2.5-Math-1.5B | Not Disclosed | Not Disclosed | MATH problems and rollout trees | Tree continuations/critiques | Not Disclosed | Not Disclosed | Not Disclosed | Pass@1/Avg@8 and macro accuracy; tree-informativeness/healing ablations |
| SF-2026-ARXIV-2606-08348 | SOP-Bench, Lifelong AgentBench and RealFin-Bench across native, GenericAgent, mini-swe-agent and Claude Code backends | deepseek-v4-flash and deepseek-v4-pro for Bayesian variants; Claude Sonnet-4.6, Claude Opus-4.6 and GPT-5.4 comparison rows | Not Disclosed | Not Disclosed | Verified task trajectories with benchmark/context/failure-mode/token/turn/latency features | Task artifacts plus skill actions; table reports input/output/total tokens | Not Disclosed | Not Disclosed | Posterior action thresholds are lifecycle policy, not service SLO | Task accuracy, token accounting, efficiency, full/incremental repair and backend/model ablations |
| SF-2026-ARXIV-2606-08367 | 15 days, five parallel worlds, ten agents/world, 120+ tools and three memories | Claude Sonnet-4.6, Grok-4.1-Fast, Gemini-3-Flash, GPT-5-mini and mixed population | Live provider APIs; hardware not disclosed | Not Disclosed | Persistent world plus live weather/news/internet inputs | Actions, governance outcomes and logs | Not Disclosed | Ten agents/world; request concurrency not disclosed | Not Disclosed | Cross-world behavioral trajectories, governance stability/collapse and released logs |
| SF-2026-ARXIV-2606-08372 | 14 attacks ×9 synthetic-data generators ×5 datasets; QI sizes 3–16; DP epsilon sweeps | Classifiers, graphical models and diffusion/generative attack families; not one LLM | Not Disclosed | Not Disclosed | Tabular released datasets and target quasi-identifiers | Predicted hidden attributes | Not Disclosed | Not Disclosed | Not Disclosed | Rarity-weighted reconstruction advantage, train/holdout memorization gap and RA-as-MIA comparison |
| SF-2026-ARXIV-2606-08381 | Three black-box cases: DeepSeek-R1 on China- and US-sensitive domains, and Meta AI Chat/Llama 4 on Meta-related topics | DeepSeek-R1 and Meta AI Chat/Llama 4 targets; diverse baseline ensemble; GPT-5.2 and Gemini-3.1-Flash-Lite judges; four embedding models | Provider APIs; hardware not disclosed | Not Disclosed | Shared case-specific prompts generated with GPT-4o; fixed token lengths not disclosed | Black-box responses, embeddings and ordinal judge labels | Not Disclosed | Not Disclosed | Statistical alpha=0.05 is a hypothesis threshold, not service SLO | Welch one-sided t-test, bootstrap median test, target-permutation diagnostic; relative divergence not absolute correctness or intent |
| SF-2026-ARXIV-2606-08382 | WikiText-2 perplexity, six LM-Eval tasks, LongBench and 4K RULER plus kernel/throughput slices | LongChat-7B-v1.5, Llama-2-7B, Llama-3-8B-Instruct and Llama-3.1-8B-Instruct long-context slice | RTX Pro 6000 for <6 GPU-hour 3,000-sample calibration; single RTX 4090 for attention/kernel latency | FP16 SDPA baseline; first 20% channels 4-bit and remainder 3-bit for average 3.2-bit quantized slice | Benchmark-defined; RULER explicitly 4K | Benchmark-defined generation lengths | Not Disclosed | Not Disclosed | Not Disclosed | Perplexity, zero-shot accuracy, LongBench/RULER, compression, attention speedup and end-to-end throughput |
| SF-2026-ARXIV-2606-09916 | BCP agent benchmark plus the 100 longest commonly completed Qwen2.5-14B queries | Qwen3-8B and Qwen2.5-14B | Not Disclosed | Not Disclosed | Trajectory histories; 8k live-KV budget in primary slice | Agent responses/tool trajectories | Not Disclosed | Not Disclosed | 8k is a KV budget, not a latency SLO | Task accuracy, peak request tokens, worst-case raw KV reads and full-cache fidelity |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-07923 | score_7_9; potential_books_delta | not_selected | — | — | Larch is the strongest semantic-query cost candidate and remains an Integrate proposal, but its planner delta is confined to AI_FILTER ordering and overlaps the selected runtime-state axis less broadly than IntentKV's cross-turn identity-preserving cache transition. | analysis-decision:SF-2026-ARXIV-2606-07923 |
| SF-2026-ARXIV-2606-07936 | score_7_9 | not_selected | — | — | The human-evaluation reporting codebook changes receipt completeness, yet it audits published protocol fields rather than controlling a running evaluator; Online Agent-as-a-Judge and PACE expose more direct control/evidence transitions in this frontier. | analysis-decision:SF-2026-ARXIV-2606-07936 |
| SF-2026-ARXIV-2606-07943 | score_7_9; potential_books_delta; forced_review | selected | DA-20260607-SECURITY | — | Poise is the frontier's strongest non-overlapping security unit because it binds hidden skill placement to both verified side effect and legitimate-task success, exposing an admission failure that ordinary invocation metrics miss. | analysis:DA-20260607-SECURITY |
| SF-2026-ARXIV-2606-07950 | score_7_9 | not_selected | — | — | CoDaPO provides a useful fixed-compute rollout allocation policy, but confidence/difficulty resampling is a narrower training optimization than PACE's statistically valid authority to commit self-evolution changes. | analysis-decision:SF-2026-ARXIV-2606-07950 |
| SF-2026-ARXIV-2606-07957 | score_7_9; forced_review | not_selected | — | — | Demand-driven CSPM changes rule derivation ownership but reports an evaluation methodology rather than executed measurements; Poise provides stronger completed-effect security evidence for deep analysis while this architecture remains independently No Change. | analysis-decision:SF-2026-ARXIV-2606-07957 |
| SF-2026-ARXIV-2606-07968 | score_7_9 | not_selected | — | — | RecurGuard gives a concrete early-termination monitor with strong non-adaptive detection, but its exposed-trace dependency and topical adaptive miss boundary make it narrower than Poise's end-to-end skill admission/effect contract. | analysis-decision:SF-2026-ARXIV-2606-07968 |
| SF-2026-ARXIV-2606-07992 | score_7_9 | not_selected | — | — | VATS establishes the MCP error loop as an authority-bearing ingress path, but controlled injection compliance is less durable than Poise's joint postcondition plus legitimate-task verifier and varies with production guardrails. | analysis-decision:SF-2026-ARXIV-2606-07992 |
| SF-2026-ARXIV-2606-08049 | score_7_9; potential_books_delta | not_selected | — | — | SKILL.nb is an Integrate-quality workflow lifecycle mechanism, but its notebook/gate realization is an execution artifact branch; PACE isolates the more general acceptor authority and false-commit guarantee selected for self-evolution. | analysis-decision:SF-2026-ARXIV-2606-08049 |
| SF-2026-ARXIV-2606-08094 | score_7_9 | not_selected | — | — | vla.cpp is strong portable-runtime evidence across three hardware tiers, but its seven VLA adapters and batch-1 roofline form a specialized deployment branch rather than a cross-turn inference-state contract. | analysis-decision:SF-2026-ARXIV-2606-08094 |
| SF-2026-ARXIV-2606-08106 | score_7_9; potential_books_delta | selected | DA-20260607-EVOLUTION | — | PACE is the strongest lifecycle-governance unit because it moves commit authority into an anytime-valid acceptor and quantifies both false and harmful self-modification under optional stopping. | analysis:DA-20260607-EVOLUTION |
| SF-2026-ARXIV-2606-08197 | score_7_9 | not_selected | — | — | AlignFed makes staleness, semantic calibration and participation fairness explicit, yet the single-A100 edge simulation is less cross-cutting than the selected acceptor and runtime-state mechanisms. | analysis-decision:SF-2026-ARXIV-2606-08197 |
| SF-2026-ARXIV-2606-08200 | score_7_9; potential_books_delta | not_selected | — | — | Online Agent-as-a-Judge survives as an Integrate proposal because intervention changes evidence acquisition, but its life-simulation criteria coverage is a narrower evaluator branch than PACE's reusable commit-control result. | analysis-decision:SF-2026-ARXIV-2606-08200 |
| SF-2026-ARXIV-2606-08340 | score_7_9 | not_selected | — | — | Alem cleanly separates individual and coordination reward across 13 LLMs, but the procedural world is a benchmark owner rather than a new production coordination-control mechanism; it remains No Change against Ch82. | analysis-decision:SF-2026-ARXIV-2606-08340 |
| SF-2026-ARXIV-2606-08348 | score_7_9 | not_selected | — | — | Bayesian-Agent provides evidence-bearing posterior skill actions across harnesses, but its guarantee depends on verifiable artifacts and specified priors; PACE offers the sharper optional-stopping commit boundary for the selected evolution unit. | analysis-decision:SF-2026-ARXIV-2606-08348 |
| SF-2026-ARXIV-2606-08367 | score_7_9 | not_selected | — | — | Emergence World expands duration, heterogeneity and consequential governance, but five 15-day worlds demonstrate observability rather than a causal control mechanism; it remains a platform-evaluation alternative. | analysis-decision:SF-2026-ARXIV-2606-08367 |
| SF-2026-ARXIV-2606-08372 | score_7_9; forced_review | not_selected | — | — | The reconstruction SoK contributes the strongest privacy interpretation result in the set, but its released-table black-box threat model is orthogonal to the selected agent security and runtime chains and is already owned by the security evaluation branch. | analysis-decision:SF-2026-ARXIV-2606-08372 |
| SF-2026-ARXIV-2606-08382 | score_7_9 | not_selected | — | — | STAR-KV delivers adaptive low-rank thresholds, quantization and kernels, but Ch45 already owns variable-rank low-rank compression; IntentKV adds the less-covered cross-turn intent plus prefix-identity transition and is therefore selected. | analysis-decision:SF-2026-ARXIV-2606-08382 |
| SF-2026-ARXIV-2606-09916 | score_7_9; potential_books_delta | selected | DA-20260607-RUNTIME | — | IntentKV is the strongest runtime-state unit because QueryMemory changes retention across turns while slot-map redirection explicitly preserves surviving KV rows, RoPE phase and prefix-cache identity. | analysis:DA-20260607-RUNTIME |

<!-- analysis-decision:SF-2026-ARXIV-2606-07923:start -->
Larch is the strongest semantic-query cost candidate and remains an Integrate proposal, but its planner delta is confined to AI_FILTER ordering and overlaps the selected runtime-state axis less broadly than IntentKV's cross-turn identity-preserving cache transition.
<!-- analysis-decision:SF-2026-ARXIV-2606-07923:end -->
<!-- analysis-decision:SF-2026-ARXIV-2606-07936:start -->
The human-evaluation reporting codebook changes receipt completeness, yet it audits published protocol fields rather than controlling a running evaluator; Online Agent-as-a-Judge and PACE expose more direct control/evidence transitions in this frontier.
<!-- analysis-decision:SF-2026-ARXIV-2606-07936:end -->
<!-- analysis-decision:SF-2026-ARXIV-2606-07950:start -->
CoDaPO provides a useful fixed-compute rollout allocation policy, but confidence/difficulty resampling is a narrower training optimization than PACE's statistically valid authority to commit self-evolution changes.
<!-- analysis-decision:SF-2026-ARXIV-2606-07950:end -->
<!-- analysis-decision:SF-2026-ARXIV-2606-07957:start -->
Demand-driven CSPM changes rule derivation ownership but reports an evaluation methodology rather than executed measurements; Poise provides stronger completed-effect security evidence for deep analysis while this architecture remains independently No Change.
<!-- analysis-decision:SF-2026-ARXIV-2606-07957:end -->
<!-- analysis-decision:SF-2026-ARXIV-2606-07968:start -->
RecurGuard gives a concrete early-termination monitor with strong non-adaptive detection, but its exposed-trace dependency and topical adaptive miss boundary make it narrower than Poise's end-to-end skill admission/effect contract.
<!-- analysis-decision:SF-2026-ARXIV-2606-07968:end -->
<!-- analysis-decision:SF-2026-ARXIV-2606-07992:start -->
VATS establishes the MCP error loop as an authority-bearing ingress path, but controlled injection compliance is less durable than Poise's joint postcondition plus legitimate-task verifier and varies with production guardrails.
<!-- analysis-decision:SF-2026-ARXIV-2606-07992:end -->
<!-- analysis-decision:SF-2026-ARXIV-2606-08049:start -->
SKILL.nb is an Integrate-quality workflow lifecycle mechanism, but its notebook/gate realization is an execution artifact branch; PACE isolates the more general acceptor authority and false-commit guarantee selected for self-evolution.
<!-- analysis-decision:SF-2026-ARXIV-2606-08049:end -->
<!-- analysis-decision:SF-2026-ARXIV-2606-08094:start -->
vla.cpp is strong portable-runtime evidence across three hardware tiers, but its seven VLA adapters and batch-1 roofline form a specialized deployment branch rather than a cross-turn inference-state contract.
<!-- analysis-decision:SF-2026-ARXIV-2606-08094:end -->
<!-- analysis-decision:SF-2026-ARXIV-2606-08197:start -->
AlignFed makes staleness, semantic calibration and participation fairness explicit, yet the single-A100 edge simulation is less cross-cutting than the selected acceptor and runtime-state mechanisms.
<!-- analysis-decision:SF-2026-ARXIV-2606-08197:end -->
<!-- analysis-decision:SF-2026-ARXIV-2606-08200:start -->
Online Agent-as-a-Judge survives as an Integrate proposal because intervention changes evidence acquisition, but its life-simulation criteria coverage is a narrower evaluator branch than PACE's reusable commit-control result.
<!-- analysis-decision:SF-2026-ARXIV-2606-08200:end -->
<!-- analysis-decision:SF-2026-ARXIV-2606-08340:start -->
Alem cleanly separates individual and coordination reward across 13 LLMs, but the procedural world is a benchmark owner rather than a new production coordination-control mechanism; it remains No Change against Ch82.
<!-- analysis-decision:SF-2026-ARXIV-2606-08340:end -->
<!-- analysis-decision:SF-2026-ARXIV-2606-08348:start -->
Bayesian-Agent provides evidence-bearing posterior skill actions across harnesses, but its guarantee depends on verifiable artifacts and specified priors; PACE offers the sharper optional-stopping commit boundary for the selected evolution unit.
<!-- analysis-decision:SF-2026-ARXIV-2606-08348:end -->
<!-- analysis-decision:SF-2026-ARXIV-2606-08367:start -->
Emergence World expands duration, heterogeneity and consequential governance, but five 15-day worlds demonstrate observability rather than a causal control mechanism; it remains a platform-evaluation alternative.
<!-- analysis-decision:SF-2026-ARXIV-2606-08367:end -->
<!-- analysis-decision:SF-2026-ARXIV-2606-08372:start -->
The reconstruction SoK contributes the strongest privacy interpretation result in the set, but its released-table black-box threat model is orthogonal to the selected agent security and runtime chains and is already owned by the security evaluation branch.
<!-- analysis-decision:SF-2026-ARXIV-2606-08372:end -->
<!-- analysis-decision:SF-2026-ARXIV-2606-08382:start -->
STAR-KV delivers adaptive low-rank thresholds, quantization and kernels, but Ch45 already owns variable-rank low-rank compression; IntentKV adds the less-covered cross-turn intent plus prefix-identity transition and is therefore selected.
<!-- analysis-decision:SF-2026-ARXIV-2606-08382:end -->

### Non-eligible family-specific closures

`23 retained = 18 eligible + 5 non-eligible`；两组互斥且并集等于冻结 Candidate Denominator。下表不属于 canonical Selection 主表，`non_eligible` 也不等于 `not_selected`。

| Source Family ID | Score V2 | Review Override | Eligibility Signals | Family-specific Closure | Narrative Ref |
| --- | ---: | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-07970 | 6/9 | none | none | Score V2=6/9、Review Override=`none`；train-time adversarial attack 只形成 TRAIN-SFT 内的受限 robustness branch，未提出新的跨 owner 状态、结构缺口、Books correction 或 pre-Books `potential_books_delta`。 | analysis-ineligible:SF-2026-ARXIV-2606-07970 |
| SF-2026-ARXIV-2606-08302 | 6/9 | none | none | Score V2=6/9、Review Override=`none`；head/layer/step-aware VAR cache compression 是视觉自回归 workload 的局部压缩分支，未改变通用 KV identity owner，也没有 structural/cross-cutting correction 或 pre-Books `potential_books_delta`。 | analysis-ineligible:SF-2026-ARXIV-2606-08302 |
| SF-2026-ARXIV-2606-08317 | 6/9 | none | none | Score V2=6/9、Review Override=`none`；九维数据库 taxonomy、filter 与 compatibility score 是概念性选择框架，exact-v1 没有 product-level empirical evaluator，因而不构成平台 admission owner 的新机制、结构缺口或 pre-Books `potential_books_delta`。 | analysis-ineligible:SF-2026-ARXIV-2606-08317 |
| SF-2026-ARXIV-2606-08346 | 6/9 | none | none | Score V2=6/9、Review Override=`none`；critique-guided grafting 只修复 CATPO 的 all-fail rollout tree，是 TRAIN-GRPO 内的局部训练分支，未改变跨系统 control ownership，也没有 correction/structural gap 或 pre-Books `potential_books_delta`。 | analysis-ineligible:SF-2026-ARXIV-2606-08346 |
| SF-2026-ARXIV-2606-08381 | 6/9 | none | none | Score V2=6/9、Review Override=`none`；reference-set-relative divergence 只能审计 provider 间语义差异，不能判定 truth、intent、harm 或 release authority，因此未形成新的 evaluation/release contract、结构缺口或 pre-Books `potential_books_delta`。 | analysis-ineligible:SF-2026-ARXIV-2606-08381 |

<!-- analysis-ineligible:SF-2026-ARXIV-2606-07970:start -->
Score V2=6/9、Review Override=`none`；train-time adversarial attack 只形成 TRAIN-SFT 内的受限 robustness branch，未提出新的跨 owner 状态、结构缺口、Books correction 或 pre-Books `potential_books_delta`。 该 closure 只关闭长叙事 eligibility；Source Review、Benchmark Contract 与 Books Comparison 仍按 retained family 完整执行。
<!-- analysis-ineligible:SF-2026-ARXIV-2606-07970:end -->
<!-- analysis-ineligible:SF-2026-ARXIV-2606-08302:start -->
Score V2=6/9、Review Override=`none`；head/layer/step-aware VAR cache compression 是视觉自回归 workload 的局部压缩分支，未改变通用 KV identity owner，也没有 structural/cross-cutting correction 或 pre-Books `potential_books_delta`。 该 closure 只关闭长叙事 eligibility；Source Review、Benchmark Contract 与 Books Comparison 仍按 retained family 完整执行。
<!-- analysis-ineligible:SF-2026-ARXIV-2606-08302:end -->
<!-- analysis-ineligible:SF-2026-ARXIV-2606-08317:start -->
Score V2=6/9、Review Override=`none`；九维数据库 taxonomy、filter 与 compatibility score 是概念性选择框架，exact-v1 没有 product-level empirical evaluator，因而不构成平台 admission owner 的新机制、结构缺口或 pre-Books `potential_books_delta`。 该 closure 只关闭长叙事 eligibility；Source Review、Benchmark Contract 与 Books Comparison 仍按 retained family 完整执行。
<!-- analysis-ineligible:SF-2026-ARXIV-2606-08317:end -->
<!-- analysis-ineligible:SF-2026-ARXIV-2606-08346:start -->
Score V2=6/9、Review Override=`none`；critique-guided grafting 只修复 CATPO 的 all-fail rollout tree，是 TRAIN-GRPO 内的局部训练分支，未改变跨系统 control ownership，也没有 correction/structural gap 或 pre-Books `potential_books_delta`。 该 closure 只关闭长叙事 eligibility；Source Review、Benchmark Contract 与 Books Comparison 仍按 retained family 完整执行。
<!-- analysis-ineligible:SF-2026-ARXIV-2606-08346:end -->
<!-- analysis-ineligible:SF-2026-ARXIV-2606-08381:start -->
Score V2=6/9、Review Override=`none`；reference-set-relative divergence 只能审计 provider 间语义差异，不能判定 truth、intent、harm 或 release authority，因此未形成新的 evaluation/release contract、结构缺口或 pre-Books `potential_books_delta`。 该 closure 只关闭长叙事 eligibility；Source Review、Benchmark Contract 与 Books Comparison 仍按 retained family 完整执行。
<!-- analysis-ineligible:SF-2026-ARXIV-2606-08381:end -->

**Selected Deep Analysis Narratives**

<!-- analysis:DA-20260607-SECURITY:start -->
Poise exposes why skill admission cannot stop at content scanning or invocation detection. The evidence object must join three identities: the exact skill position, the verified external side effect, and the legitimate-task verifier. This is selected over the other security families because it changes the release/admission contract without depending on a vendor-specific runtime; its SkillTester false-positive result also prevents treating an LLM audit alert as ground truth.
<!-- analysis:DA-20260607-SECURITY:end -->

<!-- analysis:DA-20260607-EVOLUTION:start -->
PACE separates proposer quality from commit authority. Reusing the same noisy dev estimate across hundreds of proposals creates adaptive multiple testing; the acceptor, not the proposer, owns whether state changes. Paired anytime-valid evidence controls each candidate's false-commit probability under optional stopping, while the paper explicitly does not claim a global lifetime error bound. This is the frontier's clearest durable self-evolution gate.
<!-- analysis:DA-20260607-EVOLUTION:end -->

<!-- analysis:DA-20260607-RUNTIME:start -->
IntentKV makes cross-turn intent a session-owned cache policy while preserving the identity constraints that prefix sharing and RoPE require. QueryMemory may change which tokens remain live, but slot-map sentinel redirection prevents eviction from silently renumbering survivors. The selected mechanism therefore connects semantic retention to physical KV state without equating an 8k budget or observed read reduction with a production latency SLO.
<!-- analysis:DA-20260607-RUNTIME:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-07923 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#L358 | ROADMAP.md#L1; books/part-05-inference-system/56-inference-scheduling.md#L10 | existing:SF-2026-ARXIV-2606-07923 | delta:SF-2026-ARXIV-2606-07923 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-07923 |
| SF-2026-ARXIV-2606-07936 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L335 | ROADMAP.md#L1; books/part-06-ai-infrastructure/66-evaluation-system.md#L10 | existing:SF-2026-ARXIV-2606-07936 | delta:SF-2026-ARXIV-2606-07936 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-07936 |
| SF-2026-ARXIV-2606-07943 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L367 | ROADMAP.md#L1; books/part-06-ai-infrastructure/72-security.md#L10 | existing:SF-2026-ARXIV-2606-07943 | delta:SF-2026-ARXIV-2606-07943 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-07943 |
| SF-2026-ARXIV-2606-07950 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#L10 | ROADMAP.md#L1; books/part-04-training-system/33-grpo.md#L10 | existing:SF-2026-ARXIV-2606-07950 | delta:SF-2026-ARXIV-2606-07950 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-07950 |
| SF-2026-ARXIV-2606-07957 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L367 | ROADMAP.md#L1; books/part-06-ai-infrastructure/72-security.md#L10 | existing:SF-2026-ARXIV-2606-07957 | delta:SF-2026-ARXIV-2606-07957 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-07957 |
| SF-2026-ARXIV-2606-07968 | PLATFORM-MONITORING | books/part-06-ai-infrastructure/67-monitoring.md#L10 | ROADMAP.md#L1; books/part-06-ai-infrastructure/67-monitoring.md#L10 | existing:SF-2026-ARXIV-2606-07968 | delta:SF-2026-ARXIV-2606-07968 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-07968 |
| SF-2026-ARXIV-2606-07970 | TRAIN-SFT | books/part-04-training-system/29-sft.md#L10 | ROADMAP.md#L1; books/part-04-training-system/29-sft.md#L10 | existing:SF-2026-ARXIV-2606-07970 | delta:SF-2026-ARXIV-2606-07970 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-07970 |
| SF-2026-ARXIV-2606-07992 | AGENT-MCP | books/part-07-agent/78-tool-calling.md#L10 | ROADMAP.md#L1; books/part-07-agent/78-tool-calling.md#L10 | existing:SF-2026-ARXIV-2606-07992 | delta:SF-2026-ARXIV-2606-07992 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-07992 |
| SF-2026-ARXIV-2606-08049 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#L159 | ROADMAP.md#L1; books/part-07-agent/81-workflow.md#L10 | existing:SF-2026-ARXIV-2606-08049 | delta:SF-2026-ARXIV-2606-08049 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-08049 |
| SF-2026-ARXIV-2606-08094 | INFER-REQUEST-LIFECYCLE | books/part-05-inference-system/42-what-happens-during-inference.md#L10 | ROADMAP.md#L1; books/part-05-inference-system/42-what-happens-during-inference.md#L10 | existing:SF-2026-ARXIV-2606-08094 | delta:SF-2026-ARXIV-2606-08094 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08094 |
| SF-2026-ARXIV-2606-08106 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#L343 | ROADMAP.md#L1; books/part-07-agent/84-agent-platform.md#L10 | existing:SF-2026-ARXIV-2606-08106 | delta:SF-2026-ARXIV-2606-08106 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-08106 |
| SF-2026-ARXIV-2606-08197 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#L10 | ROADMAP.md#L1; books/part-04-training-system/36-distributed-training.md#L10 | existing:SF-2026-ARXIV-2606-08197 | delta:SF-2026-ARXIV-2606-08197 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08197 |
| SF-2026-ARXIV-2606-08200 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L335 | ROADMAP.md#L1; books/part-06-ai-infrastructure/66-evaluation-system.md#L10 | existing:SF-2026-ARXIV-2606-08200 | delta:SF-2026-ARXIV-2606-08200 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-08200 |
| SF-2026-ARXIV-2606-08302 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L292 | ROADMAP.md#L1; books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L10 | existing:SF-2026-ARXIV-2606-08302 | delta:SF-2026-ARXIV-2606-08302 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08302 |
| SF-2026-ARXIV-2606-08317 | PLATFORM-FOUNDATIONS | books/part-06-ai-infrastructure/57-what-is-ai-platform.md#L10 | books/part-06-ai-infrastructure/58-kubeflow.md#L10 | existing:SF-2026-ARXIV-2606-08317 | delta:SF-2026-ARXIV-2606-08317 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08317 |
| SF-2026-ARXIV-2606-08340 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#L10 | ROADMAP.md#L1; books/part-07-agent/82-multi-agent.md#L10 | existing:SF-2026-ARXIV-2606-08340 | delta:SF-2026-ARXIV-2606-08340 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08340 |
| SF-2026-ARXIV-2606-08346 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#L10 | ROADMAP.md#L1; books/part-04-training-system/33-grpo.md#L10 | existing:SF-2026-ARXIV-2606-08346 | delta:SF-2026-ARXIV-2606-08346 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08346 |
| SF-2026-ARXIV-2606-08348 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#L343 | ROADMAP.md#L1; books/part-07-agent/84-agent-platform.md#L10 | existing:SF-2026-ARXIV-2606-08348 | delta:SF-2026-ARXIV-2606-08348 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08348 |
| SF-2026-ARXIV-2606-08367 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L335 | ROADMAP.md#L1; books/part-06-ai-infrastructure/66-evaluation-system.md#L10 | existing:SF-2026-ARXIV-2606-08367 | delta:SF-2026-ARXIV-2606-08367 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08367 |
| SF-2026-ARXIV-2606-08372 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L367 | ROADMAP.md#L1; books/part-06-ai-infrastructure/72-security.md#L10 | existing:SF-2026-ARXIV-2606-08372 | delta:SF-2026-ARXIV-2606-08372 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08372 |
| SF-2026-ARXIV-2606-08381 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L335 | ROADMAP.md#L1; books/part-06-ai-infrastructure/66-evaluation-system.md#L10 | existing:SF-2026-ARXIV-2606-08381 | delta:SF-2026-ARXIV-2606-08381 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08381 |
| SF-2026-ARXIV-2606-08382 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L292 | ROADMAP.md#L1; books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L10 | existing:SF-2026-ARXIV-2606-08382 | delta:SF-2026-ARXIV-2606-08382 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08382 |
| SF-2026-ARXIV-2606-09916 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L292 | ROADMAP.md#L1; books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L10 | existing:SF-2026-ARXIV-2606-09916 | delta:SF-2026-ARXIV-2606-09916 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-09916 |

<!-- books-review:SF-2026-ARXIV-2606-07923:start -->
Compared `Larch: Learned Query Optimization for Semantic Predicates` against `books/part-05-inference-system/56-inference-scheduling.md#L358` and its ROADMAP-adjacent owner.

<!-- existing:SF-2026-ARXIV-2606-07923:start -->
Ch56 已把 KV residency 和 pipeline state 变成可调度成本，但没有 semantic predicate 的逐行 selectivity 学习与精确短路排序。
<!-- existing:SF-2026-ARXIV-2606-07923:end -->

<!-- delta:SF-2026-ARXIV-2606-07923:start -->
Online selectivity learning plus exact per-row ordering makes semantic-predicate token cost query-planner state rather than an opaque LLM charge. 只补这一条机制、non-proof 与旧路径共存边界。
<!-- delta:SF-2026-ARXIV-2606-07923:end -->

Decision: `Integrate`. Exact-v1 does not transfer ownership or generalize beyond its evaluator contract.
<!-- books-review:SF-2026-ARXIV-2606-07923:end -->
<!-- books-review:SF-2026-ARXIV-2606-07936:start -->
Compared `Illusions of the Gold Standard: A Large-scale Analysis of Human Evaluation Protocols for Long-form Text Generation` against `books/part-06-ai-infrastructure/66-evaluation-system.md#L335` and its ROADMAP-adjacent owner.

<!-- existing:SF-2026-ARXIV-2606-07936:start -->
Ch66 已把 judge 变成有预算的 evidence acquisition policy，但没有 evaluator 通过环境原生 action 主动制造 criterion-relevant situation 的干预边界。
<!-- existing:SF-2026-ARXIV-2606-07936:end -->

<!-- delta:SF-2026-ARXIV-2606-07936:start -->
Twenty reproducibility fields separate what human judges measured, who judged, and how judgments may be interpreted; this changes the evaluation receipt contract. 是已有 owner contract 的实例、benchmark、理论分支或受限替代，不新增独立长期命题。
<!-- delta:SF-2026-ARXIV-2606-07936:end -->

Decision: `No Change — Existing Coverage`. Exact-v1 does not transfer ownership or generalize beyond its evaluator contract.
<!-- books-review:SF-2026-ARXIV-2606-07936:end -->
<!-- books-review:SF-2026-ARXIV-2606-07943:start -->
Compared `Poise: Position-Aware One-Instruction Skill Injection for Silent Execution on LLM Agents` against `books/part-06-ai-infrastructure/72-security.md#L367` and its ROADMAP-adjacent owner.

<!-- existing:SF-2026-ARXIV-2606-07943:start -->
Ch72 已定义持久 Skill 的 supply-chain lifecycle、admission 和 revocation，但没有位置感知单指令、静默副作用与合法任务联合通过的攻击证据。
<!-- existing:SF-2026-ARXIV-2606-07943:end -->

<!-- delta:SF-2026-ARXIV-2606-07943:start -->
Postcondition-validated payload execution jointly with legitimate-task success changes skill-poisoning evidence from invocation to completed side effect, while position controls stealth and reliability. 只补这一条机制、non-proof 与旧路径共存边界。
<!-- delta:SF-2026-ARXIV-2606-07943:end -->

Decision: `Integrate`. Exact-v1 does not transfer ownership or generalize beyond its evaluator contract.
<!-- books-review:SF-2026-ARXIV-2606-07943:end -->
<!-- books-review:SF-2026-ARXIV-2606-07950:start -->
Compared `The Easy, the Hard, and the Learnable: Confidence and Difficulty-Adaptive Policy Optimization for LLM Reasoning` against `books/part-04-training-system/33-grpo.md#L10` and its ROADMAP-adjacent owner.

<!-- existing:SF-2026-ARXIV-2606-07950:start -->
`TRAIN-GRPO` 当前章节已经覆盖该 family 的主机制类别、owner 边界与常见 failure mode。
<!-- existing:SF-2026-ARXIV-2606-07950:end -->

<!-- delta:SF-2026-ARXIV-2606-07950:start -->
Confidence, empirical difficulty, and shrinking group advantage become explicit rollout-allocation state used for both resampling and update weighting under fixed compute. 是已有 owner contract 的实例、benchmark、理论分支或受限替代，不新增独立长期命题。
<!-- delta:SF-2026-ARXIV-2606-07950:end -->

Decision: `No Change — Existing Coverage`. Exact-v1 does not transfer ownership or generalize beyond its evaluator contract.
<!-- books-review:SF-2026-ARXIV-2606-07950:end -->
<!-- books-review:SF-2026-ARXIV-2606-07957:start -->
Compared `Demand-Driven Vulnerability Detection for Cloud Security Posture Management: Removing Human Rule Authoring from the Disclosure-to-Protection Critical Path` against `books/part-06-ai-infrastructure/72-security.md#L367` and its ROADMAP-adjacent owner.

<!-- existing:SF-2026-ARXIV-2606-07957:start -->
Ch72 已定义持久 Skill 的 supply-chain lifecycle、admission 和 revocation，但没有位置感知单指令、静默副作用与合法任务联合通过的攻击证据。
<!-- existing:SF-2026-ARXIV-2606-07957:end -->

<!-- delta:SF-2026-ARXIV-2606-07957:start -->
CSPM rules become tenant-local derived state maintained bidirectionally from catalogue entries and the live asset graph, removing vendor release cadence from the protection critical path. 是已有 owner contract 的实例、benchmark、理论分支或受限替代，不新增独立长期命题。
<!-- delta:SF-2026-ARXIV-2606-07957:end -->

Decision: `No Change — Existing Coverage`. Exact-v1 does not transfer ownership or generalize beyond its evaluator contract.
<!-- books-review:SF-2026-ARXIV-2606-07957:end -->
<!-- books-review:SF-2026-ARXIV-2606-07968:start -->
Compared `RecurGuard: Runtime Monitoring for Reasoning-Token Consumption Attacks` against `books/part-06-ai-infrastructure/67-monitoring.md#L10` and its ROADMAP-adjacent owner.

<!-- existing:SF-2026-ARXIV-2606-07968:start -->
`PLATFORM-MONITORING` 当前章节已经覆盖该 family 的主机制类别、owner 边界与常见 failure mode。
<!-- existing:SF-2026-ARXIV-2606-07968:end -->

<!-- delta:SF-2026-ARXIV-2606-07968:start -->
A generation-time monitor combines recurrence, volume growth, and task progress over consecutive chunks and owns early termination of reasoning-token consumption attacks. 是已有 owner contract 的实例、benchmark、理论分支或受限替代，不新增独立长期命题。
<!-- delta:SF-2026-ARXIV-2606-07968:end -->

Decision: `No Change — Existing Coverage`. Exact-v1 does not transfer ownership or generalize beyond its evaluator contract.
<!-- books-review:SF-2026-ARXIV-2606-07968:end -->
<!-- books-review:SF-2026-ARXIV-2606-07970:start -->
Compared `Defending Against Malicious Finetuning by Scaling Train-time Adversarial Attacks` against `books/part-04-training-system/29-sft.md#L10` and its ROADMAP-adjacent owner.

<!-- existing:SF-2026-ARXIV-2606-07970:start -->
`TRAIN-SFT` 当前章节已经覆盖该 family 的主机制类别、owner 边界与常见 failure mode。
<!-- existing:SF-2026-ARXIV-2606-07970:end -->

<!-- delta:SF-2026-ARXIV-2606-07970:start -->
Train-time adversarial attack strength becomes an inner-loop robustness control, with parallel execution preserving the stronger full-parameter threat model. 是已有 owner contract 的实例、benchmark、理论分支或受限替代，不新增独立长期命题。
<!-- delta:SF-2026-ARXIV-2606-07970:end -->

Decision: `No Change — Existing Coverage`. Exact-v1 does not transfer ownership or generalize beyond its evaluator contract.
<!-- books-review:SF-2026-ARXIV-2606-07970:end -->
<!-- books-review:SF-2026-ARXIV-2606-07992:start -->
Compared `VATS: Exploiting Implicit Authority in Error-Path Injection via Systematic Mutation` against `books/part-07-agent/78-tool-calling.md#L10` and its ROADMAP-adjacent owner.

<!-- existing:SF-2026-ARXIV-2606-07992:start -->
`AGENT-MCP` 当前章节已经覆盖该 family 的主机制类别、owner 边界与常见 failure mode。
<!-- existing:SF-2026-ARXIV-2606-07992:end -->

<!-- delta:SF-2026-ARXIV-2606-07992:start -->
Tool errors are an authority-bearing ingress path; mutation across error structure and language changes MCP trust from tool output validation to error-loop admission and containment. 是已有 owner contract 的实例、benchmark、理论分支或受限替代，不新增独立长期命题。
<!-- delta:SF-2026-ARXIV-2606-07992:end -->

Decision: `No Change — Existing Coverage`. Exact-v1 does not transfer ownership or generalize beyond its evaluator contract.
<!-- books-review:SF-2026-ARXIV-2606-07992:end -->
<!-- books-review:SF-2026-ARXIV-2606-08049:start -->
Compared `SKILL.nb: Selective Formalization and Gated Execution for Durable Agent Workflows` against `books/part-07-agent/81-workflow.md#L159` and its ROADMAP-adjacent owner.

<!-- existing:SF-2026-ARXIV-2606-08049:start -->
Ch81 已有 split-gated self-evolution asset，但没有以 versioned notebook 为逐步 owner 的 code/NL 局部回退与多模态证据链。
<!-- existing:SF-2026-ARXIV-2606-08049:end -->

<!-- delta:SF-2026-ARXIV-2606-08049:start -->
Versioned notebooks make each reusable step auditable state and let validation gates choose code execution or local natural-language fallback when environments drift. 只补这一条机制、non-proof 与旧路径共存边界。
<!-- delta:SF-2026-ARXIV-2606-08049:end -->

Decision: `Integrate`. Exact-v1 does not transfer ownership or generalize beyond its evaluator contract.
<!-- books-review:SF-2026-ARXIV-2606-08049:end -->
<!-- books-review:SF-2026-ARXIV-2606-08094:start -->
Compared `vla.cpp: A Unified Inference Runtime for Vision-Language-Action Models` against `books/part-05-inference-system/42-what-happens-during-inference.md#L10` and its ROADMAP-adjacent owner.

<!-- existing:SF-2026-ARXIV-2606-08094:start -->
`INFER-REQUEST-LIFECYCLE` 当前章节已经覆盖该 family 的主机制类别、owner 边界与常见 failure mode。
<!-- existing:SF-2026-ARXIV-2606-08094:end -->

<!-- delta:SF-2026-ARXIV-2606-08094:start -->
A single C++ runtime owns cached vision-language prefix state, cross-attending action-expert solver steps, portable model bundles, and one request protocol across VLA families. 是已有 owner contract 的实例、benchmark、理论分支或受限替代，不新增独立长期命题。
<!-- delta:SF-2026-ARXIV-2606-08094:end -->

Decision: `No Change — Existing Coverage`. Exact-v1 does not transfer ownership or generalize beyond its evaluator contract.
<!-- books-review:SF-2026-ARXIV-2606-08094:end -->
<!-- books-review:SF-2026-ARXIV-2606-08106:start -->
Compared `PACE: Anytime-Valid Acceptance Tests for Self-Evolving Agents` against `books/part-07-agent/84-agent-platform.md#L343` and its ROADMAP-adjacent owner.

<!-- existing:SF-2026-ARXIV-2606-08106:start -->
Ch84 已有 Skill compiler/admission 与 executable evidence，但没有 optional-stopping 下 false-commit-controlled 的统计 acceptor。
<!-- existing:SF-2026-ARXIV-2606-08106:end -->

<!-- delta:SF-2026-ARXIV-2606-08106:start -->
Anytime-valid paired tests move self-evolution authority from noisy score improvement to a false-commit-controlled acceptor that remains valid under optional stopping. 只补这一条机制、non-proof 与旧路径共存边界。
<!-- delta:SF-2026-ARXIV-2606-08106:end -->

Decision: `Integrate`. Exact-v1 does not transfer ownership or generalize beyond its evaluator contract.
<!-- books-review:SF-2026-ARXIV-2606-08106:end -->
<!-- books-review:SF-2026-ARXIV-2606-08197:start -->
Compared `AlignFed: Alignment-Aware Asynchronous Federated Fine-Tuning for Large Language Models in Heterogeneous Edge Environments` against `books/part-04-training-system/36-distributed-training.md#L10` and its ROADMAP-adjacent owner.

<!-- existing:SF-2026-ARXIV-2606-08197:start -->
`TRAIN-DISTRIBUTED-TRAINING` 当前章节已经覆盖该 family 的主机制类别、owner 边界与常见 failure mode。
<!-- existing:SF-2026-ARXIV-2606-08197:end -->

<!-- delta:SF-2026-ARXIV-2606-08197:start -->
Version grouping, calibration-set semantic alignment, and freshness/participation weighting make staleness and fairness explicit asynchronous federated aggregation state. 是已有 owner contract 的实例、benchmark、理论分支或受限替代，不新增独立长期命题。
<!-- delta:SF-2026-ARXIV-2606-08197:end -->

Decision: `No Change — Existing Coverage`. Exact-v1 does not transfer ownership or generalize beyond its evaluator contract.
<!-- books-review:SF-2026-ARXIV-2606-08197:end -->
<!-- books-review:SF-2026-ARXIV-2606-08200:start -->
Compared `Online Agent-as-a-Judge: Situation-Generating Evaluation for Interactive Agents` against `books/part-06-ai-infrastructure/66-evaluation-system.md#L335` and its ROADMAP-adjacent owner.

<!-- existing:SF-2026-ARXIV-2606-08200:start -->
Ch66 已把 judge 变成有预算的 evidence acquisition policy，但没有 evaluator 通过环境原生 action 主动制造 criterion-relevant situation 的干预边界。
<!-- existing:SF-2026-ARXIV-2606-08200:end -->

<!-- delta:SF-2026-ARXIV-2606-08200:start -->
An in-world evaluator actively creates criterion-relevant situations through native dialogue/action, changing evaluation from passive trajectory scoring to coverage-seeking intervention. 只补这一条机制、non-proof 与旧路径共存边界。
<!-- delta:SF-2026-ARXIV-2606-08200:end -->

Decision: `Integrate`. Exact-v1 does not transfer ownership or generalize beyond its evaluator contract.
<!-- books-review:SF-2026-ARXIV-2606-08200:end -->
<!-- books-review:SF-2026-ARXIV-2606-08302:start -->
Compared `HACK++: Towards More Effective Head-Aware Key-Value Compression for Efficient Visual Autoregressive Modeling` against `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L292` and its ROADMAP-adjacent owner.

<!-- existing:SF-2026-ARXIV-2606-08302:start -->
Ch45 已有 workload-semantic retention、variable-rank low-rank compression 与 prefix identity；缺少跨 turn QueryMemory 和 sentinel slot-map 保持行/相位/前缀身份的删除机制。
<!-- existing:SF-2026-ARXIV-2606-08302:end -->

<!-- delta:SF-2026-ARXIV-2606-08302:start -->
Head role, layer, and generation step control separate attention and retained-cache budgets for visual autoregressive decoding instead of applying one global compression ratio. 是已有 owner contract 的实例、benchmark、理论分支或受限替代，不新增独立长期命题。
<!-- delta:SF-2026-ARXIV-2606-08302:end -->

Decision: `No Change — Existing Coverage`. Exact-v1 does not transfer ownership or generalize beyond its evaluator contract.
<!-- books-review:SF-2026-ARXIV-2606-08302:end -->
<!-- books-review:SF-2026-ARXIV-2606-08317:start -->
Compared `Architectural Evolution and Selection Framework for Database Systems in AI-Ready Data Platforms` against `books/part-06-ai-infrastructure/57-what-is-ai-platform.md#L10` and its ROADMAP-adjacent owner.

<!-- existing:SF-2026-ARXIV-2606-08317:start -->
Ch57 已把平台定义为 workload-specific identity/state/policy/evidence contract，并以 intent→admission→reconciliation 闭环和 one-size-fits-all failure 约束架构选择；概念性数据库 taxonomy 不新增独立 owner。
<!-- existing:SF-2026-ARXIV-2606-08317:end -->

<!-- delta:SF-2026-ARXIV-2606-08317:start -->
Nine dimensions, workload characterization, constraint filtering, and compatibility scoring make polyglot database choice a reviewable platform decision rather than intuition. 是已有 owner contract 的实例、benchmark、理论分支或受限替代，不新增独立长期命题。
<!-- delta:SF-2026-ARXIV-2606-08317:end -->

Decision: `No Change — Existing Coverage`. Exact-v1 does not transfer ownership or generalize beyond its evaluator contract.
<!-- books-review:SF-2026-ARXIV-2606-08317:end -->
<!-- books-review:SF-2026-ARXIV-2606-08340:start -->
Compared `Benchmarking Open-Ended Multi-Agent Coordination in Language Agents` against `books/part-07-agent/82-multi-agent.md#L10` and its ROADMAP-adjacent owner.

<!-- existing:SF-2026-ARXIV-2606-08340:start -->
`AGENT-MULTI-AGENT` 当前章节已经覆盖该 family 的主机制类别、owner 边界与常见 failure mode。
<!-- existing:SF-2026-ARXIV-2606-08340:end -->

<!-- delta:SF-2026-ARXIV-2606-08340:start -->
A long-horizon world separates individual task reward from coordination reward while controlling communication, role specialization, and coordination difficulty. 是已有 owner contract 的实例、benchmark、理论分支或受限替代，不新增独立长期命题。
<!-- delta:SF-2026-ARXIV-2606-08340:end -->

Decision: `No Change — Existing Coverage`. Exact-v1 does not transfer ownership or generalize beyond its evaluator contract.
<!-- books-review:SF-2026-ARXIV-2606-08340:end -->
<!-- books-review:SF-2026-ARXIV-2606-08346:start -->
Compared `CATPO: Critique-Augmented Tree Policy Optimization` against `books/part-04-training-system/33-grpo.md#L10` and its ROADMAP-adjacent owner.

<!-- existing:SF-2026-ARXIV-2606-08346:start -->
`TRAIN-GRPO` 当前章节已经覆盖该 family 的主机制类别、owner 边界与常见 failure mode。
<!-- existing:SF-2026-ARXIV-2606-08346:end -->

<!-- delta:SF-2026-ARXIV-2606-08346:start -->
Tree outcome diversity and policy-reward decorrelation identify low-signal rollout trees; critique-guided grafting repairs all-fail branches before informativeness-weighted updates. 是已有 owner contract 的实例、benchmark、理论分支或受限替代，不新增独立长期命题。
<!-- delta:SF-2026-ARXIV-2606-08346:end -->

Decision: `No Change — Existing Coverage`. Exact-v1 does not transfer ownership or generalize beyond its evaluator contract.
<!-- books-review:SF-2026-ARXIV-2606-08346:end -->
<!-- books-review:SF-2026-ARXIV-2606-08348:start -->
Compared `Bayesian-Agent: Posterior-Guided Skill Evolution for LLM Agent Harnesses` against `books/part-07-agent/84-agent-platform.md#L343` and its ROADMAP-adjacent owner.

<!-- existing:SF-2026-ARXIV-2606-08348:start -->
Ch84 已有 Skill compiler/admission 与 executable evidence，但没有 optional-stopping 下 false-commit-controlled 的统计 acceptor。
<!-- existing:SF-2026-ARXIV-2606-08348:end -->

<!-- delta:SF-2026-ARXIV-2606-08348:start -->
Verified trajectories and posterior beliefs turn skills into evidence-bearing lifecycle objects with auditable update and guardrail actions across harnesses. 是已有 owner contract 的实例、benchmark、理论分支或受限替代，不新增独立长期命题。
<!-- delta:SF-2026-ARXIV-2606-08348:end -->

Decision: `No Change — Existing Coverage`. Exact-v1 does not transfer ownership or generalize beyond its evaluator contract.
<!-- books-review:SF-2026-ARXIV-2606-08348:end -->
<!-- books-review:SF-2026-ARXIV-2606-08367:start -->
Compared `Emergence World: A Platform for Evaluating Long-Horizon Multi-Agent Autonomy` against `books/part-06-ai-infrastructure/66-evaluation-system.md#L335` and its ROADMAP-adjacent owner.

<!-- existing:SF-2026-ARXIV-2606-08367:start -->
Ch66 已把 judge 变成有预算的 evidence acquisition policy，但没有 evaluator 通过环境原生 action 主动制造 criterion-relevant situation 的干预边界。
<!-- existing:SF-2026-ARXIV-2606-08367:end -->

<!-- delta:SF-2026-ARXIV-2606-08367:start -->
Continuously running heterogeneous agent populations, persistent memories, consequential governance, and live exogenous data expose drift and cross-influence absent from exam-style evaluation. 是已有 owner contract 的实例、benchmark、理论分支或受限替代，不新增独立长期命题。
<!-- delta:SF-2026-ARXIV-2606-08367:end -->

Decision: `No Change — Existing Coverage`. Exact-v1 does not transfer ownership or generalize beyond its evaluator contract.
<!-- books-review:SF-2026-ARXIV-2606-08367:end -->
<!-- books-review:SF-2026-ARXIV-2606-08372:start -->
Compared `SoK: Reconstruction Attacks on Synthetic Tabular Data (Insights from Winning the NIST CRC)` against `books/part-06-ai-infrastructure/72-security.md#L367` and its ROADMAP-adjacent owner.

<!-- existing:SF-2026-ARXIV-2606-08372:start -->
Ch72 已定义持久 Skill 的 supply-chain lifecycle、admission 和 revocation，但没有位置感知单指令、静默副作用与合法任务联合通过的攻击证据。
<!-- existing:SF-2026-ARXIV-2606-08372:end -->

<!-- delta:SF-2026-ARXIV-2606-08372:start -->
A memorization test distinguishes population reconstruction from training-record leakage and maps reconstruction and membership inference to one comparable privacy-risk scale. 是已有 owner contract 的实例、benchmark、理论分支或受限替代，不新增独立长期命题。
<!-- delta:SF-2026-ARXIV-2606-08372:end -->

Decision: `No Change — Existing Coverage`. Exact-v1 does not transfer ownership or generalize beyond its evaluator contract.
<!-- books-review:SF-2026-ARXIV-2606-08372:end -->
<!-- books-review:SF-2026-ARXIV-2606-08381:start -->
Compared `Auditing Proprietary Alignment in Large Language Models: A Comparative Framework Without a Ground-Truth Standard` against `books/part-06-ai-infrastructure/66-evaluation-system.md#L335` and its ROADMAP-adjacent owner.

<!-- existing:SF-2026-ARXIV-2606-08381:start -->
Ch66 已把 judge 变成有预算的 evidence acquisition policy，但没有 evaluator 通过环境原生 action 主动制造 criterion-relevant situation 的干预边界。
<!-- existing:SF-2026-ARXIV-2606-08381:end -->

<!-- delta:SF-2026-ARXIV-2606-08381:start -->
Reference-set-relative semantic divergence provides a black-box audit contract for provider-specific alignment when absolute ground truth is unavailable. 是已有 owner contract 的实例、benchmark、理论分支或受限替代，不新增独立长期命题。
<!-- delta:SF-2026-ARXIV-2606-08381:end -->

Decision: `No Change — Existing Coverage`. Exact-v1 does not transfer ownership or generalize beyond its evaluator contract.
<!-- books-review:SF-2026-ARXIV-2606-08381:end -->
<!-- books-review:SF-2026-ARXIV-2606-08382:start -->
Compared `STAR-KV: Low-Rank KV Cache Compression via Soft Thresholding for Adaptive Rank Control` against `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L292` and its ROADMAP-adjacent owner.

<!-- existing:SF-2026-ARXIV-2606-08382:start -->
Ch45 已有 workload-semantic retention、variable-rank low-rank compression 与 prefix identity；缺少跨 turn QueryMemory 和 sentinel slot-map 保持行/相位/前缀身份的删除机制。
<!-- existing:SF-2026-ARXIV-2606-08382:end -->

<!-- delta:SF-2026-ARXIV-2606-08382:start -->
Differentiable head/block thresholds, sensitivity-specific factorization, and rank-aware mixed precision turn KV rank into adaptive runtime compression state backed by kernels. 是已有 owner contract 的实例、benchmark、理论分支或受限替代，不新增独立长期命题。
<!-- delta:SF-2026-ARXIV-2606-08382:end -->

Decision: `No Change — Existing Coverage`. Exact-v1 does not transfer ownership or generalize beyond its evaluator contract.
<!-- books-review:SF-2026-ARXIV-2606-08382:end -->
<!-- books-review:SF-2026-ARXIV-2606-09916:start -->
Compared `IntentKV: Cross-Turn Intent-Aware KV Cache Pruning for Agent Inference` against `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L292` and its ROADMAP-adjacent owner.

<!-- existing:SF-2026-ARXIV-2606-09916:start -->
Ch45 已有 workload-semantic retention、variable-rank low-rank compression 与 prefix identity；缺少跨 turn QueryMemory 和 sentinel slot-map 保持行/相位/前缀身份的删除机制。
<!-- existing:SF-2026-ARXIV-2606-09916:end -->

<!-- delta:SF-2026-ARXIV-2606-09916:start -->
Cross-turn QueryMemory controls live-token retention while slot-map redirection preserves surviving rows, RoPE phase, and prefix-cache identity during eviction. 只补这一条机制、non-proof 与旧路径共存边界。
<!-- delta:SF-2026-ARXIV-2606-09916:end -->

Decision: `Integrate`. Exact-v1 does not transfer ownership or generalize beyond its evaluator contract.
<!-- books-review:SF-2026-ARXIV-2606-09916:end -->

`SF-2026-ARXIV-2606-08317` is recovered and resolved as `No Change — Existing Coverage`: the exact-v1 PDF supports a conceptual workload/profile/filter/score branch, while Ch57 already owns workload-specific platform admission and the paper explicitly lacks product-level empirical validation.

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260607-COVERAGE | fresh-context:jun07-denominator-v1 | coverage | coverage:SRC-ARXIV:20260607 | — | 261/261 identities and all 46 route negatives re-read; 23+238 arithmetic and hashes reproduced | passed |
| SA-20260607-EVIDENCE | fresh-context:jun07-exact-v1-recovery-v2 | evidence | review:SF-2026-ARXIV-2606-07923; review:SF-2026-ARXIV-2606-07936; review:SF-2026-ARXIV-2606-07943; review:SF-2026-ARXIV-2606-07950; review:SF-2026-ARXIV-2606-07957; review:SF-2026-ARXIV-2606-07968; review:SF-2026-ARXIV-2606-07970; review:SF-2026-ARXIV-2606-07992; review:SF-2026-ARXIV-2606-08049; review:SF-2026-ARXIV-2606-08094; review:SF-2026-ARXIV-2606-08106; review:SF-2026-ARXIV-2606-08197; review:SF-2026-ARXIV-2606-08200; review:SF-2026-ARXIV-2606-08302; review:SF-2026-ARXIV-2606-08317; review:SF-2026-ARXIV-2606-08340; review:SF-2026-ARXIV-2606-08346; review:SF-2026-ARXIV-2606-08348; review:SF-2026-ARXIV-2606-08367; review:SF-2026-ARXIV-2606-08372; review:SF-2026-ARXIV-2606-08381; review:SF-2026-ARXIV-2606-08382; review:SF-2026-ARXIV-2606-09916 | none | 23/23 exact-v1 reviews and benchmark contracts passed; 2606.08317 method, illustrative evaluation and non-proof boundaries were recovered from the official v1 PDF | passed |
| SA-20260607-SELECTION | fresh-context:jun07-frontier-v2 | deep_analysis_selection | analysis-decision:SF-2026-ARXIV-2606-07923; analysis-decision:SF-2026-ARXIV-2606-07936; analysis:DA-20260607-SECURITY; analysis-decision:SF-2026-ARXIV-2606-07950; analysis-decision:SF-2026-ARXIV-2606-07957; analysis-decision:SF-2026-ARXIV-2606-07968; analysis-decision:SF-2026-ARXIV-2606-07992; analysis-decision:SF-2026-ARXIV-2606-08049; analysis-decision:SF-2026-ARXIV-2606-08094; analysis:DA-20260607-EVOLUTION; analysis-decision:SF-2026-ARXIV-2606-08197; analysis-decision:SF-2026-ARXIV-2606-08200; analysis-decision:SF-2026-ARXIV-2606-08340; analysis-decision:SF-2026-ARXIV-2606-08348; analysis-decision:SF-2026-ARXIV-2606-08367; analysis-decision:SF-2026-ARXIV-2606-08372; analysis-decision:SF-2026-ARXIV-2606-08382; analysis:DA-20260607-RUNTIME; analysis-ineligible:SF-2026-ARXIV-2606-07970; analysis-ineligible:SF-2026-ARXIV-2606-08302; analysis-ineligible:SF-2026-ARXIV-2606-08317; analysis-ineligible:SF-2026-ARXIV-2606-08346; analysis-ineligible:SF-2026-ARXIV-2606-08381 | — | corrected-contract conservation reproduced: 23 retained = 18 eligible + 5 non-eligible, disjoint union; main table has only eligible families, five bounded closures stay outside it, and three non-overlapping units remain selected | passed |
| SA-20260607-BOOKS | fresh-context:jun07-postrecovery-v2 | books | books-review:SF-2026-ARXIV-2606-07923; books-review:SF-2026-ARXIV-2606-07936; books-review:SF-2026-ARXIV-2606-07943; books-review:SF-2026-ARXIV-2606-07950; books-review:SF-2026-ARXIV-2606-07957; books-review:SF-2026-ARXIV-2606-07968; books-review:SF-2026-ARXIV-2606-07970; books-review:SF-2026-ARXIV-2606-07992; books-review:SF-2026-ARXIV-2606-08049; books-review:SF-2026-ARXIV-2606-08094; books-review:SF-2026-ARXIV-2606-08106; books-review:SF-2026-ARXIV-2606-08197; books-review:SF-2026-ARXIV-2606-08200; books-review:SF-2026-ARXIV-2606-08302; books-review:SF-2026-ARXIV-2606-08317; books-review:SF-2026-ARXIV-2606-08340; books-review:SF-2026-ARXIV-2606-08346; books-review:SF-2026-ARXIV-2606-08348; books-review:SF-2026-ARXIV-2606-08367; books-review:SF-2026-ARXIV-2606-08372; books-review:SF-2026-ARXIV-2606-08381; books-review:SF-2026-ARXIV-2606-08382; books-review:SF-2026-ARXIV-2606-09916 | none | 6/6 Integrate正文与Review note通过；17/17 No Change（含恢复的2606.08317）无Books泄漏；owner/adjacent与证据边界复核通过 | passed |

### Recovered Materials Receipt

- `SF-2026-ARXIV-2606-08317`: official exact-v1 PDF `https://arxiv.org/pdf/2606.08317v1`, 18 pages, fully reviewed; official HTML still returns Internal Error.
- Recovery closed the sole Materials Request. The review binds §II/§VI-A/§IX-B method identity, §VI-B/§IX-D illustrative evaluation, and §IX-B/§XI non-proof boundaries; no secondary summary was promoted.

## 8. Ignored Noise

The 238 pre-denominator closures are not unreviewed noise. Each retains title, abstract, route, family-specific closure class and reopen condition in the frozen denominator ledger. None is scored or leaked into Selection or Books.

## 9. Recommended Action

保持本日 Complete；只有 exact-version revision、artifact provenance 或 Books owner 证据发生变化时才重开真实受影响的 Gate，不因展示迁移重复研究。

## 10. Repository Changes

This lane restores the 06-07 Daily, exact-v1 recovery receipts, full comparison and deterministic renderer. It also restores six Books integrations in Ch45, Ch56, Ch66, Ch72, Ch81 and Ch84; the recovered `2606.08317v1` family remains No Change and required no additional Books write. Nothing was staged, committed or pushed.

## 11. Open Questions

- None for this Daily. The sole Conditional blocker is resolved and the 23/23 recovery audit has zero unresolved findings.

## 12. Sources

- [Larch: Learned Query Optimization for Semantic Predicates](https://arxiv.org/abs/2606.07923v1) — first-public：2026-06-06；accessed：2026-08-29
- [Illusions of the Gold Standard: A Large-scale Analysis of Human Evaluation Protocols for Long-form Text Generation](https://arxiv.org/abs/2606.07936v1) — first-public：2026-06-06；accessed：2026-08-29
- [Poise: Position-Aware One-Instruction Skill Injection for Silent Execution on LLM Agents](https://arxiv.org/abs/2606.07943v1) — first-public：2026-06-06；accessed：2026-08-29
- [The Easy, the Hard, and the Learnable: Confidence and Difficulty-Adaptive Policy Optimization for LLM Reasoning](https://arxiv.org/abs/2606.07950v1) — first-public：2026-06-06；accessed：2026-08-29
- [Demand-Driven Vulnerability Detection for Cloud Security Posture Management: Removing Human Rule Authoring from the Disclosure-to-Protection Critical Path](https://arxiv.org/abs/2606.07957v1) — first-public：2026-06-06；accessed：2026-08-29
- [RecurGuard: Runtime Monitoring for Reasoning-Token Consumption Attacks](https://arxiv.org/abs/2606.07968v1) — first-public：2026-06-06；accessed：2026-08-29
- [Defending Against Malicious Finetuning by Scaling Train-time Adversarial Attacks](https://arxiv.org/abs/2606.07970v1) — first-public：2026-06-06；accessed：2026-08-29
- [VATS: Exploiting Implicit Authority in Error-Path Injection via Systematic Mutation](https://arxiv.org/abs/2606.07992v1) — first-public：2026-06-06；accessed：2026-08-29
- [SKILL.nb: Selective Formalization and Gated Execution for Durable Agent Workflows](https://arxiv.org/abs/2606.08049v1) — first-public：2026-06-06；accessed：2026-08-29
- [vla.cpp: A Unified Inference Runtime for Vision-Language-Action Models](https://arxiv.org/abs/2606.08094v1) — first-public：2026-06-06；accessed：2026-08-29
- [PACE: Anytime-Valid Acceptance Tests for Self-Evolving Agents](https://arxiv.org/abs/2606.08106v1) — first-public：2026-06-06；accessed：2026-08-29
- [AlignFed: Alignment-Aware Asynchronous Federated Fine-Tuning for Large Language Models in Heterogeneous Edge Environments](https://arxiv.org/abs/2606.08197v1) — first-public：2026-06-06；accessed：2026-08-29
- [Online Agent-as-a-Judge: Situation-Generating Evaluation for Interactive Agents](https://arxiv.org/abs/2606.08200v1) — first-public：2026-06-06；accessed：2026-08-29
- [HACK++: Towards More Effective Head-Aware Key-Value Compression for Efficient Visual Autoregressive Modeling](https://arxiv.org/abs/2606.08302v1) — first-public：2026-06-06；accessed：2026-08-29
- [Architectural Evolution and Selection Framework for Database Systems in AI-Ready Data Platforms](https://arxiv.org/abs/2606.08317v1) — first-public：2026-06-06；accessed：2026-08-29
- [Benchmarking Open-Ended Multi-Agent Coordination in Language Agents](https://arxiv.org/abs/2606.08340v1) — first-public：2026-06-06；accessed：2026-08-29
- [CATPO: Critique-Augmented Tree Policy Optimization](https://arxiv.org/abs/2606.08346v1) — first-public：2026-06-06；accessed：2026-08-29
- [Bayesian-Agent: Posterior-Guided Skill Evolution for LLM Agent Harnesses](https://arxiv.org/abs/2606.08348v1) — first-public：2026-06-06；accessed：2026-08-29
- [Emergence World: A Platform for Evaluating Long-Horizon Multi-Agent Autonomy](https://arxiv.org/abs/2606.08367v1) — first-public：2026-06-06；accessed：2026-08-29
- [SoK: Reconstruction Attacks on Synthetic Tabular Data (Insights from Winning the NIST CRC)](https://arxiv.org/abs/2606.08372v1) — first-public：2026-06-06；accessed：2026-08-29
- [Auditing Proprietary Alignment in Large Language Models: A Comparative Framework Without a Ground-Truth Standard](https://arxiv.org/abs/2606.08381v1) — first-public：2026-06-07；accessed：2026-08-29
- [STAR-KV: Low-Rank KV Cache Compression via Soft Thresholding for Adaptive Rank Control](https://arxiv.org/abs/2606.08382v1) — first-public：2026-06-07；accessed：2026-08-29
- [IntentKV: Cross-Turn Intent-Aware KV Cache Pruning for Agent Inference](https://arxiv.org/abs/2606.09916v1) — first-public：2026-06-06；accessed：2026-08-29
- [Research Sources Registry](../../../../docs/RESEARCH_SOURCES.md) — source roles、cadence 与 evidence scope 的权威注册表

## 13. Final Status

Daily V2.1 的 Coverage=Closed、Evidence=Passed、Books=Passed；Completion Status=Complete。261 个 raw identities 已闭合为 23 个 retained families 与 238 个 family-specific pre-denominator closures；Selection 守恒为 18 个 eligible 主表 family + 5 个具名 non-eligible closure，互斥且并集为 23，selected 仍为 3；23/23 Source Review 与 Books Decision 均已通过 fresh-context audit，未解决 finding 为 0。
