# Daily Research — 2026-06-11

**Research Date:** 2026-06-11

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-06-10 09:00:00 ～ 2026-06-11 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；559/559 identities 完成 title+abstract semantic screening，技术 claim 仅来自 exact-v1 primary evidence 与已冻结 source packet

**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed，fresh-context Semantic Audit 无未解决 finding

> Strict V2.1 reconstruction for `DEN-20260611-559031`. Books writeback was serialized through root; this lane performed the independent post-write audit.

## Executive Summary

The Beijing window contains 559 registered arXiv identities. Full 559/559 title+abstract semantic screening freezes 31 durable AI-system families and 528 row-specific closures. All 31 exact-v1 Reviews, benchmark contracts and full-frontier selection decisions pass fresh semantic audit. Root merged 26 Integrate families into 12 unique owners; five No Change families were rechecked against existing owner/adjacent coverage. The 31/31 post-write fresh-context audit resolved one Daily-only owner finding for 2606.12370 and closed Books Gate.

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-06-11 |
| Window End | 2026-06-11 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | DEN-20260611-559031 |
| Denominator Frozen At | 2026-08-29T23:15:00+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-06-10T09:00:00+08:00 | 2026-06-11T09:00:00+08:00 | 2026-08-29T23:15:00+08:00 | Frozen DataCite DOI-prefix snapshots; Core full enumeration; 559/559 semantic screen | checked | 559 | SF-2026-ARXIV-2606-11543; SF-2026-ARXIV-2606-11632; SF-2026-ARXIV-2606-11671; SF-2026-ARXIV-2606-11686; SF-2026-ARXIV-2606-11688; SF-2026-ARXIV-2606-11690; SF-2026-ARXIV-2606-11718; SF-2026-ARXIV-2606-11806; SF-2026-ARXIV-2606-11871; SF-2026-ARXIV-2606-11878; SF-2026-ARXIV-2606-11916; SF-2026-ARXIV-2606-11949; SF-2026-ARXIV-2606-11998; SF-2026-ARXIV-2606-12243; SF-2026-ARXIV-2606-12320; SF-2026-ARXIV-2606-12329; SF-2026-ARXIV-2606-12370; SF-2026-ARXIV-2606-12385; SF-2026-ARXIV-2606-12487; SF-2026-ARXIV-2606-12556; SF-2026-ARXIV-2606-12688; SF-2026-ARXIV-2606-12703; SF-2026-ARXIV-2606-12736; SF-2026-ARXIV-2606-12737; SF-2026-ARXIV-2606-12764; SF-2026-ARXIV-2606-12765; SF-2026-ARXIV-2606-13708; SF-2026-ARXIV-2606-14779; SF-2026-ARXIV-2606-14783; SF-2026-ARXIV-2606-18284; SF-2026-ARXIV-2606-18286 | pages=40, records=40000/40000, final cursor=end; 559 unique in-window identities | 2026-06-11T01:00:00Z | ../_sources/daily-20260611/screening-ledger.json; ../_sources/daily-20260611/denominator-full-semantic-audit-v1.tsv; coverage:SRC-ARXIV:20260611 | — |

<!-- coverage:SRC-ARXIV:20260611:start -->
All 559 identities were read at title+abstract level. Full-retain and full-closure surfaces were audited; keyword routes were not used as admission decisions. Frozen result: 31 retained, 528 closures.
<!-- coverage:SRC-ARXIV:20260611:end -->

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-11543 | arXiv:2606.11543v1 | paper-v1:2606.11543 | 2026-W24 | 2026-06-10 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-11543 | self | — | new_in_window | AGENT-REFLECTION | Integrate | books-review:SF-2026-ARXIV-2606-11543 | yes |
| SF-2026-ARXIV-2606-11632 | arXiv:2606.11632v1 | paper-v1:2606.11632 | 2026-W24 | 2026-06-10 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-11632 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-11632 | yes |
| SF-2026-ARXIV-2606-11671 | arXiv:2606.11671v1 | paper-v1:2606.11671 | 2026-W24 | 2026-06-10 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-11671 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-11671 | yes |
| SF-2026-ARXIV-2606-11686 | arXiv:2606.11686v1 | paper-v1:2606.11686 | 2026-W24 | 2026-06-10 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-11686 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2606-11686 | yes |
| SF-2026-ARXIV-2606-11688 | arXiv:2606.11688v1 | paper-v1:2606.11688 | 2026-W24 | 2026-06-10 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-11688 | self | — | new_in_window | AGENT-WORKFLOW | Integrate | books-review:SF-2026-ARXIV-2606-11688 | yes |
| SF-2026-ARXIV-2606-11690 | arXiv:2606.11690v1 | paper-v1:2606.11690 | 2026-W24 | 2026-06-10 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-11690 | self | — | new_in_window | PLATFORM-COST | Integrate | books-review:SF-2026-ARXIV-2606-11690 | yes |
| SF-2026-ARXIV-2606-11718 | arXiv:2606.11718v1 | paper-v1:2606.11718 | 2026-W24 | 2026-06-10 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-11718 | self | — | new_in_window | INFER-GPU-MEMORY | Integrate | books-review:SF-2026-ARXIV-2606-11718 | yes |
| SF-2026-ARXIV-2606-11806 | arXiv:2606.11806v1 | paper-v1:2606.11806 | 2026-W24 | 2026-06-10 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-11806 | self | — | new_in_window | AGENT-MEMORY | Integrate | books-review:SF-2026-ARXIV-2606-11806 | yes |
| SF-2026-ARXIV-2606-11871 | arXiv:2606.11871v1 | paper-v1:2606.11871 | 2026-W24 | 2026-06-10 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-11871 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-11871 | yes |
| SF-2026-ARXIV-2606-11878 | arXiv:2606.11878v1 | paper-v1:2606.11878 | 2026-W24 | 2026-06-10 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-11878 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-11878 | yes |
| SF-2026-ARXIV-2606-11916 | arXiv:2606.11916v1 | paper-v1:2606.11916 | 2026-W24 | 2026-06-10 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-11916 | self | — | new_in_window | PLATFORM-MONITORING | Integrate | books-review:SF-2026-ARXIV-2606-11916 | yes |
| SF-2026-ARXIV-2606-11949 | arXiv:2606.11949v1 | paper-v1:2606.11949 | 2026-W24 | 2026-06-10 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-11949 | self | — | new_in_window | PLATFORM-MONITORING | Integrate | books-review:SF-2026-ARXIV-2606-11949 | yes |
| SF-2026-ARXIV-2606-11998 | arXiv:2606.11998v1 | paper-v1:2606.11998 | 2026-W24 | 2026-06-10 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-11998 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-11998 | yes |
| SF-2026-ARXIV-2606-12243 | arXiv:2606.12243v1 | paper-v1:2606.12243 | 2026-W24 | 2026-06-10 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-12243 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-12243 | yes |
| SF-2026-ARXIV-2606-12320 | arXiv:2606.12320v1 | paper-v1:2606.12320 | 2026-W24 | 2026-06-10 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-12320 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-12320 | yes |
| SF-2026-ARXIV-2606-12329 | arXiv:2606.12329v1 | paper-v1:2606.12329 | 2026-W24 | 2026-06-10 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-12329 | self | — | new_in_window | AGENT-MEMORY | Integrate | books-review:SF-2026-ARXIV-2606-12329 | yes |
| SF-2026-ARXIV-2606-12370 | arXiv:2606.12370v1 | paper-v1:2606.12370 | 2026-W24 | 2026-06-10 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-12370 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-12370 | yes |
| SF-2026-ARXIV-2606-12385 | arXiv:2606.12385v1 | paper-v1:2606.12385 | 2026-W24 | 2026-06-10 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-12385 | self | — | new_in_window | TRAIN-DATA | Integrate | books-review:SF-2026-ARXIV-2606-12385 | yes |
| SF-2026-ARXIV-2606-12487 | arXiv:2606.12487v1 | paper-v1:2606.12487 | 2026-W24 | 2026-06-10 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-12487 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-12487 | yes |
| SF-2026-ARXIV-2606-12556 | arXiv:2606.12556v1 | paper-v1:2606.12556 | 2026-W24 | 2026-06-10 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-12556 | self | — | new_in_window | INFER-GPU-MEMORY | Integrate | books-review:SF-2026-ARXIV-2606-12556 | yes |
| SF-2026-ARXIV-2606-12688 | arXiv:2606.12688v1 | paper-v1:2606.12688 | 2026-W24 | 2026-06-10 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-12688 | self | — | new_in_window | INFER-KSERVE-TOPOLOGY | Integrate | books-review:SF-2026-ARXIV-2606-12688 | yes |
| SF-2026-ARXIV-2606-12703 | arXiv:2606.12703v1 | paper-v1:2606.12703 | 2026-W24 | 2026-06-10 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-12703 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-12703 | yes |
| SF-2026-ARXIV-2606-12736 | arXiv:2606.12736v1 | paper-v1:2606.12736 | 2026-W24 | 2026-06-10 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-12736 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-12736 | yes |
| SF-2026-ARXIV-2606-12737 | arXiv:2606.12737v1 | paper-v1:2606.12737 | 2026-W24 | 2026-06-10 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-12737 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-12737 | yes |
| SF-2026-ARXIV-2606-12764 | arXiv:2606.12764v1 | paper-v1:2606.12764 | 2026-W24 | 2026-06-11 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-12764 | self | — | new_in_window | TRAIN-DATA | Integrate | books-review:SF-2026-ARXIV-2606-12764 | yes |
| SF-2026-ARXIV-2606-12765 | arXiv:2606.12765v1 | paper-v1:2606.12765 | 2026-W24 | 2026-06-11 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-12765 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-12765 | yes |
| SF-2026-ARXIV-2606-13708 | arXiv:2606.13708v1 | paper-v1:2606.13708 | 2026-W24 | 2026-06-10 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-13708 | self | — | new_in_window | INFER-PD-DISAGGREGATION | Integrate | books-review:SF-2026-ARXIV-2606-13708 | yes |
| SF-2026-ARXIV-2606-14779 | arXiv:2606.14779v1 | paper-v1:2606.14779 | 2026-W24 | 2026-06-10 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-14779 | self | — | new_in_window | INFER-GPU-MEMORY | Integrate | books-review:SF-2026-ARXIV-2606-14779 | yes |
| SF-2026-ARXIV-2606-14783 | arXiv:2606.14783v1 | paper-v1:2606.14783 | 2026-W24 | 2026-06-10 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-14783 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-14783 | yes |
| SF-2026-ARXIV-2606-18284 | arXiv:2606.18284v1 | paper-v1:2606.18284 | 2026-W24 | 2026-06-10 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-18284 | self | — | new_in_window | TRAIN-DATA | Integrate | books-review:SF-2026-ARXIV-2606-18284 | yes |
| SF-2026-ARXIV-2606-18286 | arXiv:2606.18286v1 | paper-v1:2606.18286 | 2026-W24 | 2026-06-10 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-18286 | self | — | new_in_window | TRAIN-SFT | Integrate | books-review:SF-2026-ARXIV-2606-18286 | yes |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-11543 | RP-996ddbe635b42759 | deep | arXiv:2606.11543v1 | SRC-ARXIV@arXiv:2606.11543v1 | arXiv:2606.11543v1 §3 Method; §§3.2–3.4 controlled variants/runtime evidence | arXiv:2606.11543v1 §4 Experiments; §4.1 setup; §§4.2–4.5 | arXiv:2606.11543v1 §6 Limitations; Appendix E layout sensitivity | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-11543 | complete |
| SF-2026-ARXIV-2606-11632 | RP-4e9fd9e26590524b | deep | arXiv:2606.11632v1 | SRC-ARXIV@arXiv:2606.11632v1 | arXiv:2606.11632v1 §§3–5 SAB model, airlock and broker | arXiv:2606.11632v1 §7 Evaluation Methodology and Targets; §7.3 setup | arXiv:2606.11632v1 §9 Discussion and Limitations; §9.2 | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-11632 | complete |
| SF-2026-ARXIV-2606-11671 | RP-cb041cc73e0cfe1f | deep | arXiv:2606.11671v1 | SRC-ARXIV@arXiv:2606.11671v1 | arXiv:2606.11671v1 §3 Runtime Skill Audit; §4 implementation | arXiv:2606.11671v1 §5 Evaluation | arXiv:2606.11671v1 §7 Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-11671 | complete |
| SF-2026-ARXIV-2606-11686 | RP-0ce3f06f8207f473 | deep | arXiv:2606.11686v1 | SRC-ARXIV@arXiv:2606.11686v1 | arXiv:2606.11686v1 §3 Layer-Isolated Evaluation; taxonomy and pure mode | arXiv:2606.11686v1 §4 Evaluation; controlled regression injection | arXiv:2606.11686v1 §5 Discussion; no dedicated limitations section | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-11686 | complete |
| SF-2026-ARXIV-2606-11688 | RP-4a4a6c0c5ab9aedf | deep | arXiv:2606.11688v1 | SRC-ARXIV@arXiv:2606.11688v1 | arXiv:2606.11688v1 §3 Method; §4 theorem; §5 System | arXiv:2606.11688v1 §6 Empirical evaluation; §6.5 scaled corpus | arXiv:2606.11688v1 §7 Limitations; Appendix A auditor boundary | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-11688 | complete |
| SF-2026-ARXIV-2606-11690 | RP-0181f38c7f1189ab | deep | arXiv:2606.11690v1 | SRC-ARXIV@arXiv:2606.11690v1 | arXiv:2606.11690v1 §3 Concurrency-Aware Cost Framework | arXiv:2606.11690v1 §4 Experimental Setup; §5 Results | arXiv:2606.11690v1 §6.8 Scope; §6.9 Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-11690 | complete |
| SF-2026-ARXIV-2606-11718 | RP-69008b395e54945b | deep | arXiv:2606.11718v1 | SRC-ARXIV@arXiv:2606.11718v1 | arXiv:2606.11718v1 §III Chiplet-Contiguous Layout | arXiv:2606.11718v1 §IV Evaluation; §IV-A methodology | arXiv:2606.11718v1 §V Conclusion; no dedicated limitations section | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-11718 | complete |
| SF-2026-ARXIV-2606-11806 | RP-e59717310c0c9142 | deep | arXiv:2606.11806v1 | SRC-ARXIV@arXiv:2606.11806v1 | arXiv:2606.11806v1 §3 Experience Serving in Production | arXiv:2606.11806v1 §4 setup; §5 Results; Appendices E–G | arXiv:2606.11806v1 §4.4 claim boundary; Appendix H interpretation scope | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-11806 | complete |
| SF-2026-ARXIV-2606-11871 | RP-ef1e562ab221a22b | deep | arXiv:2606.11871v1 | SRC-ARXIV@arXiv:2606.11871v1 | arXiv:2606.11871v1 §III threat model; §§IV–V design/implementation | arXiv:2606.11871v1 §VI Evaluation; §VII backend cost | arXiv:2606.11871v1 §VI-H portability boundaries; §VIII Discussion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-11871 | complete |
| SF-2026-ARXIV-2606-11878 | RP-32f0c5e2c40380f3 | deep | arXiv:2606.11878v1 | SRC-ARXIV@arXiv:2606.11878v1 | arXiv:2606.11878v1 §§III–V participation authority and CSC | arXiv:2606.11878v1 §VI evidence; §VII-D mitigation results | arXiv:2606.11878v1 §VII-E Cost and Limits; §VIII Discussion and Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-11878 | complete |
| SF-2026-ARXIV-2606-11916 | RP-4c1dd32fa7aadd61 | deep | arXiv:2606.11916v1 | SRC-ARXIV@arXiv:2606.11916v1 | arXiv:2606.11916v1 §III Methodology | arXiv:2606.11916v1 §IV Results; §§IV-A–IV-E | arXiv:2606.11916v1 §V Threats to Validity | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-11916 | complete |
| SF-2026-ARXIV-2606-11949 | RP-cbb84c907331e88b | deep | arXiv:2606.11949v1 | SRC-ARXIV@arXiv:2606.11949v1 | arXiv:2606.11949v1 §3 Methods; §§3.1–3.10 | arXiv:2606.11949v1 §4 setup; §5 Results | arXiv:2606.11949v1 §6.5 Limitations; §5.4 ground-truth regimes | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-11949 | complete |
| SF-2026-ARXIV-2606-11998 | RP-a0357c5c1450f9fc | deep | arXiv:2606.11998v1 | SRC-ARXIV@arXiv:2606.11998v1 | arXiv:2606.11998v1 §3 Methods; §3.1 threat model/protocol | arXiv:2606.11998v1 §4 Results; Appendix C red/blue teaming | arXiv:2606.11998v1 §5 Discussion, Transparent CoT assumption and Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-11998 | complete |
| SF-2026-ARXIV-2606-12243 | RP-e1d58c24fbbef53e | deep | arXiv:2606.12243v1 | SRC-ARXIV@arXiv:2606.12243v1 | arXiv:2606.12243v1 §3 Methodology; §§3.2–3.5 | arXiv:2606.12243v1 §4 Experiments | arXiv:2606.12243v1 §4.4 additional analysis; §5 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-12243 | complete |
| SF-2026-ARXIV-2606-12320 | RP-c7a9413d6eff0ccb | deep | arXiv:2606.12320v1 | SRC-ARXIV@arXiv:2606.12320v1 | arXiv:2606.12320v1 §§3–8 threat model, five planes and composed architecture | arXiv:2606.12320v1 §9 case studies; §10 validation roadmap | arXiv:2606.12320v1 §11 Limitations and Open Questions | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-12320 | complete |
| SF-2026-ARXIV-2606-12329 | RP-6a541eae325447a5 | deep | arXiv:2606.12329v1 | SRC-ARXIV@arXiv:2606.12329v1 | arXiv:2606.12329v1 §3 System Design; §§4–6 architecture/implementation | arXiv:2606.12329v1 §7 Evaluation | arXiv:2606.12329v1 §8 Limitations and Future Work | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-12329 | complete |
| SF-2026-ARXIV-2606-12370 | RP-71b997b43c07d9de | deep | arXiv:2606.12370v1 | SRC-ARXIV@arXiv:2606.12370v1 | arXiv:2606.12370v1 §§3–5 entropy bound, TV loss and adaptation | arXiv:2606.12370v1 §6 Experiments | arXiv:2606.12370v1 §7.8 top-k instability; §9 Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-12370 | complete |
| SF-2026-ARXIV-2606-12385 | RP-5916d2239148b67e | deep | arXiv:2606.12385v1 | SRC-ARXIV@arXiv:2606.12385v1 | arXiv:2606.12385v1 §3 Design of ModSleuth | arXiv:2606.12385v1 §4 Evaluation; §5 Findings | arXiv:2606.12385v1 Appendix A verification; Appendix D disclosure gaps | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-12385 | complete |
| SF-2026-ARXIV-2606-12487 | RP-710220e92dc50112 | deep | arXiv:2606.12487v1 | SRC-ARXIV@arXiv:2606.12487v1 | arXiv:2606.12487v1 §3 Method; §3.3 policy | arXiv:2606.12487v1 §4 Experiments; §4.9 efficiency | arXiv:2606.12487v1 §7 Discussion; no dedicated limitations section | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-12487 | complete |
| SF-2026-ARXIV-2606-12556 | RP-81fba4a12f5f4ea3 | deep | arXiv:2606.12556v1 | SRC-ARXIV@arXiv:2606.12556v1 | arXiv:2606.12556v1 §3 CXL-Hybrid Architecture; §4 ITME | arXiv:2606.12556v1 §5 methodology; §6 evaluation | arXiv:2606.12556v1 §8 Conclusion; no dedicated limitations section | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-12556 | complete |
| SF-2026-ARXIV-2606-12688 | RP-ab92c7098135ca05 | deep | arXiv:2606.12688v1 | SRC-ARXIV@arXiv:2606.12688v1 | arXiv:2606.12688v1 §3 Walk Graph; §§3.1–3.3 | arXiv:2606.12688v1 §4 Evaluation; Appendix I reproducibility | arXiv:2606.12688v1 Appendix H Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-12688 | complete |
| SF-2026-ARXIV-2606-12703 | RP-8791d707f84992b4 | deep | arXiv:2606.12703v1 | SRC-ARXIV@arXiv:2606.12703v1 | arXiv:2606.12703v1 §III threat model; §§IV–VI impossibility/SMSR/certificate | arXiv:2606.12703v1 §VII Evaluation | arXiv:2606.12703v1 §VIII Discussion; provenance-key and smoothing assumptions | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-12703 | complete |
| SF-2026-ARXIV-2606-12736 | RP-40d1a5721369303e | deep | arXiv:2606.12736v1 | SRC-ARXIV@arXiv:2606.12736v1 | arXiv:2606.12736v1 §4 Methods; §4.1 framework | arXiv:2606.12736v1 §2 Results across domains; §2.6 errors | arXiv:2606.12736v1 §3 Discussion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-12736 | complete |
| SF-2026-ARXIV-2606-12737 | RP-63617c69014aabde | deep | arXiv:2606.12737v1 | SRC-ARXIV@arXiv:2606.12737v1 | arXiv:2606.12737v1 §3 PI-Hunter; §§3.1–3.3 | arXiv:2606.12737v1 §4 Experiments; Appendices B–D | arXiv:2606.12737v1 §4.4 ablations; §5 Conclusion; no dedicated limitations section | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-12737 | complete |
| SF-2026-ARXIV-2606-12764 | RP-0a5dfd6e61a7c8a9 | deep | arXiv:2606.12764v1 | SRC-ARXIV@arXiv:2606.12764v1 | arXiv:2606.12764v1 §3 Counterfactual functional memorization | arXiv:2606.12764v1 §4 Results; Appendices A–C/E | arXiv:2606.12764v1 §4 result scope; no dedicated limitations section | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-12764 | complete |
| SF-2026-ARXIV-2606-12765 | RP-24038dbbc9671b56 | deep | arXiv:2606.12765v1 | SRC-ARXIV@arXiv:2606.12765v1 | arXiv:2606.12765v1 §3 Methodology; §§4–8 characterization | arXiv:2606.12765v1 §§4–8 measurements and fused-kernel result | arXiv:2606.12765v1 §10 Discussion and limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-12765 | complete |
| SF-2026-ARXIV-2606-13708 | RP-9dec73ad083a40a9 | deep | arXiv:2606.13708v1 | SRC-ARXIV@arXiv:2606.13708v1 | arXiv:2606.13708v1 §3 Tiara Design; compiler/verifier | arXiv:2606.13708v1 §4 Evaluation; §§4.5–4.6 AI workloads | arXiv:2606.13708v1 §6 Conclusion; no dedicated limitations section | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-13708 | complete |
| SF-2026-ARXIV-2606-14779 | RP-91c37041f50a19bc | deep | arXiv:2606.14779v1 | SRC-ARXIV@arXiv:2606.14779v1 | arXiv:2606.14779v1 §IV Design; KV orchestrator and passthrough | arXiv:2606.14779v1 §V Evaluation | arXiv:2606.14779v1 §VI Discussion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-14779 | complete |
| SF-2026-ARXIV-2606-14783 | RP-60234e3e692ab07a | deep | arXiv:2606.14783v1 | SRC-ARXIV@arXiv:2606.14783v1 | arXiv:2606.14783v1 §2 Threat Model; §§4–8 mechanism/defense | arXiv:2606.14783v1 §3 setup; §§4–7 experiments | arXiv:2606.14783v1 §8 Defense Boundary; §9 deployment implications | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-14783 | complete |
| SF-2026-ARXIV-2606-18284 | RP-9d5e9586a5980f9a | deep | arXiv:2606.18284v1 | SRC-ARXIV@arXiv:2606.18284v1 | arXiv:2606.18284v1 §3 Probe Rewards; §5 probe data/selection | arXiv:2606.18284v1 §§4 and 6 Evaluation/Results | arXiv:2606.18284v1 §7 Limitations; mode-collapse findings | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-18284 | complete |
| SF-2026-ARXIV-2606-18286 | RP-c8dae86a49cd767b | deep | arXiv:2606.18286v1 | SRC-ARXIV@arXiv:2606.18286v1 | arXiv:2606.18286v1 §5 Method; §§5.1–5.4 | arXiv:2606.18286v1 §6 Experiments; Appendix A | arXiv:2606.18286v1 §7 Conclusion; Appendix C runtime analysis | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-18286 | complete |

## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-11543 | Disclosed — 82 SkillsBench tasks × 3 conditions × 5 trials | Disclosed — GPT-5.4 high reasoning | Not Disclosed — hosted runtime hardware is not identified | Not Disclosed | Not Disclosed as one universal contract — task-specific lengths remain exact-v1-bound | Not Disclosed as one universal contract — task-specific limits remain exact-v1-bound | Not Disclosed as one universal contract — trial count is not relabeled as batch | Not Disclosed unless stated in workload — worker/trial parallelism is not serving concurrency | Not Disclosed — research metrics are not a production SLO | Disclosed — exact-v1 evaluation locator reports outcome plus mechanism-specific cost/failure metrics |
| SF-2026-ARXIV-2606-11632 | Disclosed — 500 contracts × five trials; 2,500 admissions | Disclosed — Go SAB prototype, OPA, PostgreSQL ledger, three-validator SQA | Single-node local workstation; exact CPU/GPU not disclosed | Not applicable — control-plane prototype | Not Disclosed as one universal contract — task-specific lengths remain exact-v1-bound | Not Disclosed as one universal contract — task-specific limits remain exact-v1-bound | Not Disclosed as one universal contract — trial count is not relabeled as batch | Not Disclosed unless stated in workload — worker/trial parallelism is not serving concurrency | Not Disclosed — research metrics are not a production SLO | Disclosed — exact-v1 evaluation locator reports outcome plus mechanism-specific cost/failure metrics |
| SF-2026-ARXIV-2606-11671 | Disclosed — 100 OpenClaw skills with static baselines and evolving attacks | Disclosed — LLM-assisted profiler/task generator/trace judge; exact models not fully disclosed | Not Disclosed | Not Disclosed | Not Disclosed as one universal contract — task-specific lengths remain exact-v1-bound | Not Disclosed as one universal contract — task-specific limits remain exact-v1-bound | Not Disclosed as one universal contract — trial count is not relabeled as batch | Not Disclosed unless stated in workload — worker/trial parallelism is not serving concurrency | Not Disclosed — research metrics are not a production SLO | Disclosed — exact-v1 evaluation locator reports outcome plus mechanism-specific cost/failure metrics |
| SF-2026-ARXIV-2606-11686 | Disclosed — 238 cases across 23 slices; seven injected regressions; two tenants | Disclosed — No-LLM deterministic ordering-agent scaffold | Not Disclosed | Not applicable — deterministic harness | Not Disclosed as one universal contract — task-specific lengths remain exact-v1-bound | Not Disclosed as one universal contract — task-specific limits remain exact-v1-bound | Not Disclosed as one universal contract — trial count is not relabeled as batch | Not Disclosed unless stated in workload — worker/trial parallelism is not serving concurrency | Not Disclosed — research metrics are not a production SLO | Disclosed — exact-v1 evaluation locator reports outcome plus mechanism-specific cost/failure metrics |
| SF-2026-ARXIV-2606-11688 | Disclosed — 3,150 paired cells; 70 tasks including 50 SWE-bench Lite | Disclosed — Three systems × three models; model identities partly withheld | Not Disclosed | Not Disclosed | Not Disclosed as one universal contract — task-specific lengths remain exact-v1-bound | Not Disclosed as one universal contract — task-specific limits remain exact-v1-bound | Not Disclosed as one universal contract — trial count is not relabeled as batch | Not Disclosed unless stated in workload — worker/trial parallelism is not serving concurrency | Not Disclosed — research metrics are not a production SLO | Disclosed — exact-v1 evaluation locator reports outcome plus mechanism-specific cost/failure metrics |
| SF-2026-ARXIV-2606-11690 | Disclosed — 42 H100 benchmarks plus 56 A100 cross-hardware runs, 1–10 rps and saturation sweeps | Disclosed — Dense, ultra-sparse MoE and sparse MoE models | NVIDIA H100 and A100 80GB PCIe | FP16 and FP8 where supported | Not Disclosed as one universal contract — task-specific lengths remain exact-v1-bound | Not Disclosed as one universal contract — task-specific limits remain exact-v1-bound | Not Disclosed as one universal contract — trial count is not relabeled as batch | Not Disclosed unless stated in workload — worker/trial parallelism is not serving concurrency | Not Disclosed — research metrics are not a production SLO | Disclosed — exact-v1 evaluation locator reports outcome plus mechanism-specific cost/failure metrics |
| SF-2026-ARXIV-2606-11718 | Disclosed — Qwen3-30B and Llama-3.1-70B inference/training GEMM shapes | Disclosed — Qwen3-30B; Llama-3.1-70B | Modeled multi-chiplet GPU; exact product not claimed | Not Disclosed | Not Disclosed as one universal contract — task-specific lengths remain exact-v1-bound | Not Disclosed as one universal contract — task-specific limits remain exact-v1-bound | Not Disclosed as one universal contract — trial count is not relabeled as batch | Not Disclosed unless stated in workload — worker/trial parallelism is not serving concurrency | Not Disclosed — research metrics are not a production SLO | Disclosed — exact-v1 evaluation locator reports outcome plus mechanism-specific cost/failure metrics |
| SF-2026-ARXIV-2606-11806 | Disclosed — Production moderation plus tool-use and GPQA contrast tasks | Disclosed — Reasoning/instruct model variants disclosed in Appendix A.4 | Not Disclosed — hosted serving hardware not identified | Not Disclosed | Not Disclosed as one universal contract — task-specific lengths remain exact-v1-bound | Not Disclosed as one universal contract — task-specific limits remain exact-v1-bound | Not Disclosed as one universal contract — trial count is not relabeled as batch | Not Disclosed unless stated in workload — worker/trial parallelism is not serving concurrency | Not Disclosed — research metrics are not a production SLO | Disclosed — exact-v1 evaluation locator reports outcome plus mechanism-specific cost/failure metrics |
| SF-2026-ARXIV-2606-11871 | Disclosed — 77 CUDA artifacts; 51,621 sites; 52.2M dynamic checks | Disclosed — CUDA SASS binaries | NVIDIA CUDA testbed; exact GPU bound in §VI-A | Not applicable — binary instrumentation | Not Disclosed as one universal contract — task-specific lengths remain exact-v1-bound | Not Disclosed as one universal contract — task-specific limits remain exact-v1-bound | Not Disclosed as one universal contract — trial count is not relabeled as batch | Not Disclosed unless stated in workload — worker/trial parallelism is not serving concurrency | Not Disclosed — research metrics are not a production SLO | Disclosed — exact-v1 evaluation locator reports outcome plus mechanism-specific cost/failure metrics |
| SF-2026-ARXIV-2606-11878 | Disclosed — CUDA contract-conformance suite across four authority dimensions | Disclosed — CUDA collective primitives and CIC wrapper | NVIDIA CUDA testbed; exact GPU in evidence appendix | Not applicable | Not Disclosed as one universal contract — task-specific lengths remain exact-v1-bound | Not Disclosed as one universal contract — task-specific limits remain exact-v1-bound | Not Disclosed as one universal contract — trial count is not relabeled as batch | Not Disclosed unless stated in workload — worker/trial parallelism is not serving concurrency | Not Disclosed — research metrics are not a production SLO | Disclosed — exact-v1 evaluation locator reports outcome plus mechanism-specific cost/failure metrics |
| SF-2026-ARXIV-2606-11916 | Disclosed — 216-hour campaign; six co-located deployments; Poisson stress | Disclosed — Qwen2.5-7B-Instruct on vLLM, Triton-vLLM and PyTorch/HF | One host with 3× NVIDIA L40S | Not Disclosed | Not Disclosed as one universal contract — task-specific lengths remain exact-v1-bound | Not Disclosed as one universal contract — task-specific limits remain exact-v1-bound | Not Disclosed as one universal contract — trial count is not relabeled as batch | Not Disclosed unless stated in workload — worker/trial parallelism is not serving concurrency | Not Disclosed — research metrics are not a production SLO | Disclosed — exact-v1 evaluation locator reports outcome plus mechanism-specific cost/failure metrics |
| SF-2026-ARXIV-2606-11949 | Disclosed — 4 classifiers × 5 shifts × 20 seeds × 2 windows; 800 cells | Disclosed — Four deployed safety classifiers | Not Disclosed | Not Disclosed | Not Disclosed as one universal contract — task-specific lengths remain exact-v1-bound | Not Disclosed as one universal contract — task-specific limits remain exact-v1-bound | Not Disclosed as one universal contract — trial count is not relabeled as batch | Not Disclosed unless stated in workload — worker/trial parallelism is not serving concurrency | Not Disclosed — research metrics are not a production SLO | Disclosed — exact-v1 evaluation locator reports outcome plus mechanism-specific cost/failure metrics |
| SF-2026-ARXIV-2606-11998 | Disclosed — Multi-turn BashArena software-engineering tasks | Disclosed — Trusted, untrusted-agent and intermediate-monitor model configurations | Not Disclosed — API/runtime hardware not identified | Not Disclosed | Not Disclosed as one universal contract — task-specific lengths remain exact-v1-bound | Not Disclosed as one universal contract — task-specific limits remain exact-v1-bound | Not Disclosed as one universal contract — trial count is not relabeled as batch | Not Disclosed unless stated in workload — worker/trial parallelism is not serving concurrency | Not Disclosed — research metrics are not a production SLO | Disclosed — exact-v1 evaluation locator reports outcome plus mechanism-specific cost/failure metrics |
| SF-2026-ARXIV-2606-12243 | Disclosed — Four tasks across T5/Gemma model families | Disclosed — T5 and Gemma families | Disclosed in §4.1; no cross-paper normalization | Disclosed in §4.1 where applicable | Not Disclosed as one universal contract — task-specific lengths remain exact-v1-bound | Not Disclosed as one universal contract — task-specific limits remain exact-v1-bound | Not Disclosed as one universal contract — trial count is not relabeled as batch | Not Disclosed unless stated in workload — worker/trial parallelism is not serving concurrency | Not Disclosed — research metrics are not a production SLO | Disclosed — exact-v1 evaluation locator reports outcome plus mechanism-specific cost/failure metrics |
| SF-2026-ARXIV-2606-12320 | Disclosed — Seven canonical workflow threats plus production case studies | Disclosed — Reference architecture; not a model benchmark | Not applicable | Not applicable | Not Disclosed as one universal contract — task-specific lengths remain exact-v1-bound | Not Disclosed as one universal contract — task-specific limits remain exact-v1-bound | Not Disclosed as one universal contract — trial count is not relabeled as batch | Not Disclosed unless stated in workload — worker/trial parallelism is not serving concurrency | Not Disclosed — research metrics are not a production SLO | Disclosed — exact-v1 evaluation locator reports outcome plus mechanism-specific cost/failure metrics |
| SF-2026-ARXIV-2606-12329 | Disclosed — Two-month self-study, 10 projects, 207 events | Disclosed — Local-first projectmem with MCP/CLI | Local developer environment; hardware not disclosed | Not applicable | Not Disclosed as one universal contract — task-specific lengths remain exact-v1-bound | Not Disclosed as one universal contract — task-specific limits remain exact-v1-bound | Not Disclosed as one universal contract — trial count is not relabeled as batch | Not Disclosed unless stated in workload — worker/trial parallelism is not serving concurrency | Not Disclosed — research metrics are not a production SLO | Disclosed — exact-v1 evaluation locator reports outcome plus mechanism-specific cost/failure metrics |
| SF-2026-ARXIV-2606-12370 | Disclosed — RL math/reasoning workloads and MTP acceptance/throughput sweeps | Disclosed — Multiple MTP-enabled LLM scales | Disclosed in experimental appendix | Disclosed in experimental appendix | Not Disclosed as one universal contract — task-specific lengths remain exact-v1-bound | Not Disclosed as one universal contract — task-specific limits remain exact-v1-bound | Not Disclosed as one universal contract — trial count is not relabeled as batch | Not Disclosed unless stated in workload — worker/trial parallelism is not serving concurrency | Not Disclosed — research metrics are not a production SLO | Disclosed — exact-v1 evaluation locator reports outcome plus mechanism-specific cost/failure metrics |
| SF-2026-ARXIV-2606-12385 | Disclosed — Public-artifact dependency reconstruction across target LLMs | Disclosed — Agentic ModSleuth plus audited model artifacts | Not Disclosed — document analysis workload | Not applicable | Not Disclosed as one universal contract — task-specific lengths remain exact-v1-bound | Not Disclosed as one universal contract — task-specific limits remain exact-v1-bound | Not Disclosed as one universal contract — trial count is not relabeled as batch | Not Disclosed unless stated in workload — worker/trial parallelism is not serving concurrency | Not Disclosed — research metrics are not a production SLO | Disclosed — exact-v1 evaluation locator reports outcome plus mechanism-specific cost/failure metrics |
| SF-2026-ARXIV-2606-12487 | Disclosed — Perplexity, zero-shot QA, reasoning and efficiency across dense/MoE LLMs | Disclosed — Multiple dense and MoE PTQ backbones | Disclosed in §4.2; exact accelerator remains paper-bound | W4A4/KV4 with phase-aware higher precision | Not Disclosed as one universal contract — task-specific lengths remain exact-v1-bound | Not Disclosed as one universal contract — task-specific limits remain exact-v1-bound | Not Disclosed as one universal contract — trial count is not relabeled as batch | Not Disclosed unless stated in workload — worker/trial parallelism is not serving concurrency | Not Disclosed — research metrics are not a production SLO | Disclosed — exact-v1 evaluation locator reports outcome plus mechanism-specific cost/failure metrics |
| SF-2026-ARXIV-2606-12556 | Disclosed — Weight and KV offload across GPU, host, CXL and NVMe-oF tiers | Disclosed — LLM inference configurations disclosed in §5.1 | SK hynix CMM, PCIe Gen5 NVMe SSDs and FPGA prototype | Not Disclosed | Not Disclosed as one universal contract — task-specific lengths remain exact-v1-bound | Not Disclosed as one universal contract — task-specific limits remain exact-v1-bound | Not Disclosed as one universal contract — trial count is not relabeled as batch | Not Disclosed unless stated in workload — worker/trial parallelism is not serving concurrency | Not Disclosed — research metrics are not a production SLO | Disclosed — exact-v1 evaluation locator reports outcome plus mechanism-specific cost/failure metrics |
| SF-2026-ARXIV-2606-12688 | Disclosed — BAGEL, Qwen3-Omni, Orpheus and V-JEPA2 composite workloads | Disclosed — BAGEL-7B, Qwen3-Omni-30B-A3B, Orpheus-3B, V-JEPA2 | Single 4×H100 node or 8×H200 node | Model-specific; not normalized as one precision | Not Disclosed as one universal contract — task-specific lengths remain exact-v1-bound | Not Disclosed as one universal contract — task-specific limits remain exact-v1-bound | Not Disclosed as one universal contract — trial count is not relabeled as batch | Not Disclosed unless stated in workload — worker/trial parallelism is not serving concurrency | Not Disclosed — research metrics are not a production SLO | Disclosed — exact-v1 evaluation locator reports outcome plus mechanism-specific cost/failure metrics |
| SF-2026-ARXIV-2606-12703 | Disclosed — 15 enterprise scenarios; 3,150 repeated plus 450 production-scale trials | Disclosed — Persistent RAG-agent configurations; second-agent generality check | Not Disclosed | Not Disclosed | Not Disclosed as one universal contract — task-specific lengths remain exact-v1-bound | Not Disclosed as one universal contract — task-specific limits remain exact-v1-bound | Not Disclosed as one universal contract — trial count is not relabeled as batch | Not Disclosed unless stated in workload — worker/trial parallelism is not serving concurrency | Not Disclosed — research metrics are not a production SLO | Disclosed — exact-v1 evaluation locator reports outcome plus mechanism-specific cost/failure metrics |
| SF-2026-ARXIV-2606-12736 | Disclosed — Approximately 200 scientific tasks across multiple scales/domains | Disclosed — Diverse agent-agnostic systems | Not Disclosed — heterogeneous/API agents | Not Disclosed | Not Disclosed as one universal contract — task-specific lengths remain exact-v1-bound | Not Disclosed as one universal contract — task-specific limits remain exact-v1-bound | Not Disclosed as one universal contract — trial count is not relabeled as batch | Not Disclosed unless stated in workload — worker/trial parallelism is not serving concurrency | Not Disclosed — research metrics are not a production SLO | Disclosed — exact-v1 evaluation locator reports outcome plus mechanism-specific cost/failure metrics |
| SF-2026-ARXIV-2606-12737 | Disclosed — Multiple agent benchmarks, architectures, attacks and defenses | Disclosed — Agent and evaluator models disclosed in §4.1 | Not Disclosed — hosted model hardware | Not Disclosed | Not Disclosed as one universal contract — task-specific lengths remain exact-v1-bound | Not Disclosed as one universal contract — task-specific limits remain exact-v1-bound | Not Disclosed as one universal contract — trial count is not relabeled as batch | Not Disclosed unless stated in workload — worker/trial parallelism is not serving concurrency | Not Disclosed — research metrics are not a production SLO | Disclosed — exact-v1 evaluation locator reports outcome plus mechanism-specific cost/failure metrics |
| SF-2026-ARXIV-2606-12764 | Disclosed — Python function-signature continuations with execution-based and LLM-judge functional comparison | Disclosed — OLMo-3-32B midtrained target versus pretrained reference | Not Disclosed | Not Disclosed | Not Disclosed as one universal contract — task-specific lengths remain exact-v1-bound | Not Disclosed as one universal contract — task-specific limits remain exact-v1-bound | Not Disclosed as one universal contract — trial count is not relabeled as batch | Not Disclosed unless stated in workload — worker/trial parallelism is not serving concurrency | Not Disclosed — research metrics are not a production SLO | Disclosed — exact-v1 evaluation locator reports outcome plus mechanism-specific cost/failure metrics |
| SF-2026-ARXIV-2606-12765 | Disclosed — Metal 4.1 matmul2d microbenchmarks and fused GEMM+bias+GELU | Disclosed — Metal Performance Primitives tensor path | Single Apple M4 Max GPU | fp8 E4M3, fp16, accumulator ≥fp32 evidence | Not Disclosed as one universal contract — task-specific lengths remain exact-v1-bound | Not Disclosed as one universal contract — task-specific limits remain exact-v1-bound | Not Disclosed as one universal contract — trial count is not relabeled as batch | Not Disclosed unless stated in workload — worker/trial parallelism is not serving concurrency | Not Disclosed — research metrics are not a production SLO | Disclosed — exact-v1 evaluation locator reports outcome plus mechanism-specific cost/failure metrics |
| SF-2026-ARXIV-2606-13708 | Disclosed — Graph, page-table, lock, MoE gather and disaggregated PagedAttention | Disclosed — PagedAttention 8KB blocks; MoE 32 experts | FPGA-based memory-side NIC prototype | Not applicable | Not Disclosed as one universal contract — task-specific lengths remain exact-v1-bound | Not Disclosed as one universal contract — task-specific limits remain exact-v1-bound | Not Disclosed as one universal contract — trial count is not relabeled as batch | Not Disclosed unless stated in workload — worker/trial parallelism is not serving concurrency | Not Disclosed — research metrics are not a production SLO | Disclosed — exact-v1 evaluation locator reports outcome plus mechanism-specific cost/failure metrics |
| SF-2026-ARXIV-2606-14779 | Disclosed — Long-context KV offload and TTFT/I/O sweeps | Disclosed — Llama-3.1-8B, GPT-OSS-20B, Qwen3-30B-A3B | Multi-host-memory and SSD testbed disclosed in §V-A | Model/KV precision disclosed in §V-A | Not Disclosed as one universal contract — task-specific lengths remain exact-v1-bound | Not Disclosed as one universal contract — task-specific limits remain exact-v1-bound | Not Disclosed as one universal contract — trial count is not relabeled as batch | Not Disclosed unless stated in workload — worker/trial parallelism is not serving concurrency | Not Disclosed — research metrics are not a production SLO | Disclosed — exact-v1 evaluation locator reports outcome plus mechanism-specific cost/failure metrics |
| SF-2026-ARXIV-2606-14783 | Disclosed — Held-out access-code inversion, clutter/degradation/transfer and defense ablations | Disclosed — Gemma4/Fuyu vs Qwen3-VL/InternVL/LLaVA controls | Not Disclosed | Token/value quantization tested as ineffective value-level defense | Not Disclosed as one universal contract — task-specific lengths remain exact-v1-bound | Not Disclosed as one universal contract — task-specific limits remain exact-v1-bound | Not Disclosed as one universal contract — trial count is not relabeled as batch | Not Disclosed unless stated in workload — worker/trial parallelism is not serving concurrency | Not Disclosed — research metrics are not a production SLO | Disclosed — exact-v1 evaluation locator reports outcome plus mechanism-specific cost/failure metrics |
| SF-2026-ARXIV-2606-18284 | Disclosed — Math, code and SWE task generation across model scales | Disclosed — Qwen2.5-3B/7B and Qwen3.5-27B solver settings | Not Disclosed | Not Disclosed | Not Disclosed as one universal contract — task-specific lengths remain exact-v1-bound | Not Disclosed as one universal contract — task-specific limits remain exact-v1-bound | Not Disclosed as one universal contract — trial count is not relabeled as batch | Not Disclosed unless stated in workload — worker/trial parallelism is not serving concurrency | Not Disclosed — research metrics are not a production SLO | Disclosed — exact-v1 evaluation locator reports outcome plus mechanism-specific cost/failure metrics |
| SF-2026-ARXIV-2606-18286 | Disclosed — Six code-generation benchmarks | Disclosed — Qwen2.5-Coder-1.5B-Instruct and comparison models | Disclosed in Appendix A.3; exact accelerator remains v1-bound | Training precision disclosed in Appendix A.3 | Not Disclosed as one universal contract — task-specific lengths remain exact-v1-bound | Not Disclosed as one universal contract — task-specific limits remain exact-v1-bound | Not Disclosed as one universal contract — trial count is not relabeled as batch | Not Disclosed unless stated in workload — worker/trial parallelism is not serving concurrency | Not Disclosed — research metrics are not a production SLO | Disclosed — exact-v1 evaluation locator reports outcome plus mechanism-specific cost/failure metrics |

**Source Reviews**

<!-- review:SF-2026-ARXIV-2606-11543:start -->
### 2606.11543 — SkillJuror: Measuring How Agent Skill Organization Changes Runtime Behavior

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：Skill 的目录组织本身会改变资源读取与有效采用轨迹；Progressive Disclosure 必须以知识等价变体、trajectory evidence 与 verifier outcome 联合评测。

**State / data / control owner。** `AGENT-REFLECTION` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.11543v1 §4 Experiments; §4.1 setup; §§4.2–4.5` 支持 `82 SkillsBench tasks × 3 conditions × 5 trials`；模型 `GPT-5.4 high reasoning`；硬件 `Not Disclosed — hosted runtime hardware is not identified`；精度 `Not Disclosed`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.11543v1 §3 Method; §§3.2–3.4 controlled variants/runtime evidence`；counterevidence locator：`arXiv:2606.11543v1 §6 Limitations; Appendix E layout sensitivity`。

**Trade-off / failure / coexistence / evolution。** 按需资源降低入口负担但可能产生 fanout tax；精确格式、阈值或长 artifact pipeline 仍适合 flat/local instructions。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-11543:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.11543v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-11543:end -->
<!-- review:SF-2026-ARXIV-2606-11543:end -->

<!-- review:SF-2026-ARXIV-2606-11632:start -->
### 2606.11632 — Sovereign Assurance Boundary: Certificate-Bound Admission for Agentic Infrastructure

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：Agent proposal 必须编译为 typed contract，并绑定 evidence digest、policy/revocation epoch 与 scoped broker identity 后才可成为执行 authority。

**State / data / control owner。** `PLATFORM-SECURITY` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.11632v1 §7 Evaluation Methodology and Targets; §7.3 setup` 支持 `500 contracts × five trials; 2,500 admissions`；模型 `Go SAB prototype, OPA, PostgreSQL ledger, three-validator SQA`；硬件 `Single-node local workstation; exact CPU/GPU not disclosed`；精度 `Not applicable — control-plane prototype`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.11632v1 §§3–5 SAB model, airlock and broker`；counterevidence locator：`arXiv:2606.11632v1 §9 Discussion and Limitations; §9.2`。

**Trade-off / failure / coexistence / evolution。** 证书化增加 admission latency 和 TCB；证据陈旧、policy/validator 漂移或 emergency bypass 会破坏保证，IAM 仍保留。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-11632:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.11632v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-11632:end -->
<!-- review:SF-2026-ARXIV-2606-11632:end -->

<!-- review:SF-2026-ARXIV-2606-11671:start -->
### 2606.11671 — Runtime Skill Audit: Targeted Runtime Probing for Agent Skill Security

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：Skill 安全不能只审静态文件；应按 capability profile 构造 targeted runtime context，在 sandbox 中执行并以 trace evidence 标注行为。

**State / data / control owner。** `PLATFORM-SECURITY` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.11671v1 §5 Evaluation` 支持 `100 OpenClaw skills with static baselines and evolving attacks`；模型 `LLM-assisted profiler/task generator/trace judge; exact models not fully disclosed`；硬件 `Not Disclosed`；精度 `Not Disclosed`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.11671v1 §3 Runtime Skill Audit; §4 implementation`；counterevidence locator：`arXiv:2606.11671v1 §7 Limitations`。

**Trade-off / failure / coexistence / evolution。** 动态探测覆盖 context-dependent behavior，却不穷尽 trigger；模型化 task/judge 会漂移，静态扫描仍是廉价第一层。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-11671:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.11671v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-11671:end -->
<!-- review:SF-2026-ARXIV-2606-11671:end -->

<!-- review:SF-2026-ARXIV-2606-11686:start -->
### 2606.11686 — Layer-Isolated Evaluation: Gating the Deterministic Scaffold of a Production LLM Agent with a No-LLM, Regression-Locked Test Harness

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：生产 Agent 的 deterministic scaffold 应按 ontology/intent/routing/decomposition/escalation/safety/memory 分层，用 no-LLM regression-locked slices 阻止 aggregate pass rate 掩盖局部回归。

**State / data / control owner。** `PLATFORM-EVALUATION-SYSTEM` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.11686v1 §4 Evaluation; controlled regression injection` 支持 `238 cases across 23 slices; seven injected regressions; two tenants`；模型 `No-LLM deterministic ordering-agent scaffold`；硬件 `Not Disclosed`；精度 `Not applicable — deterministic harness`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.11686v1 §3 Layer-Isolated Evaluation; taxonomy and pure mode`；counterevidence locator：`arXiv:2606.11686v1 §5 Discussion; no dedicated limitations section`。

**Trade-off / failure / coexistence / evolution。** 分层 gate 定位快但只覆盖显式 scaffold；端到端 stochastic behavior 与未被 exercise 的 layer 仍需独立评测。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-11686:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.11686v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-11686:end -->
<!-- review:SF-2026-ARXIV-2606-11686:end -->

<!-- review:SF-2026-ARXIV-2606-11688:start -->
### 2606.11688 — Goal-Autopilot: A Verifiable Anti-Fabrication Firewall for Unattended Long-Horizon Agents

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：长程 Agent 应把 durable FSM、stateless ticks、falsifiable gate 与 terminal hard floor 外置，使未执行/未通过 gate 时最多 honest stall，不能宣告完成。

**State / data / control owner。** `AGENT-WORKFLOW` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.11688v1 §6 Empirical evaluation; §6.5 scaled corpus` 支持 `3,150 paired cells; 70 tasks including 50 SWE-bench Lite`；模型 `Three systems × three models; model identities partly withheld`；硬件 `Not Disclosed`；精度 `Not Disclosed`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.11688v1 §3 Method; §4 theorem; §5 System`；counterevidence locator：`arXiv:2606.11688v1 §7 Limitations; Appendix A auditor boundary`。

**Trade-off / failure / coexistence / evolution。** hard floor 用 coverage 换 honesty；定理依赖 gate soundness、floor enforcement 与 plan coverage，不能证明任务本身正确。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-11688:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.11688v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-11688:end -->
<!-- review:SF-2026-ARXIV-2606-11688:end -->

<!-- review:SF-2026-ARXIV-2606-11690:start -->
### 2606.11690 — Beyond Per-Token Pricing: A Concurrency-Aware Methodology for LLM Infrastructure Cost Estimation

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：LLM 成本必须把 offered load λ 经 Little's Law 映射为 in-flight concurrency 与实际利用率；固定 100% utilization 的每 token 估价会系统性误导低负载自托管。

**State / data / control owner。** `PLATFORM-COST` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.11690v1 §4 Experimental Setup; §5 Results` 支持 `42 H100 benchmarks plus 56 A100 cross-hardware runs, 1–10 rps and saturation sweeps`；模型 `Dense, ultra-sparse MoE and sparse MoE models`；硬件 `NVIDIA H100 and A100 80GB PCIe`；精度 `FP16 and FP8 where supported`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.11690v1 §3 Concurrency-Aware Cost Framework`；counterevidence locator：`arXiv:2606.11690v1 §6.8 Scope; §6.9 Limitations`。

**Trade-off / failure / coexistence / evolution。** 真实 meter 提高归因但需要 workload replay；burst、prefix cache、I/O shape 与硬件 FP8 支持会改变 crossover。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-11690:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.11690v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-11690:end -->
<!-- review:SF-2026-ARXIV-2606-11690:end -->

<!-- review:SF-2026-ARXIV-2606-11718:start -->
### 2606.11718 — Making Locality-aware GEMM Compatible with Page-Granularity Placement on Chiplet GPUs

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：Chiplet GPU 的 GEMM locality 需要让 chiplet-local tiles 在 global address space 连续，使 page-granularity placement 与 CTA affinity 一致。

**State / data / control owner。** `INFER-GPU-MEMORY` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.11718v1 §IV Evaluation; §IV-A methodology` 支持 `Qwen3-30B and Llama-3.1-70B inference/training GEMM shapes`；模型 `Qwen3-30B; Llama-3.1-70B`；硬件 `Modeled multi-chiplet GPU; exact product not claimed`；精度 `Not Disclosed`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.11718v1 §III Chiplet-Contiguous Layout`；counterevidence locator：`arXiv:2606.11718v1 §V Conclusion; no dedicated limitations section`。

**Trade-off / failure / coexistence / evolution。** 布局变换减少 remote HBM traffic，却要求 runtime/compiler 重排；对非 GEMM、动态 shape 或不同 interleave policy 不构成普遍收益。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-11718:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.11718v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-11718:end -->
<!-- review:SF-2026-ARXIV-2606-11718:end -->

<!-- review:SF-2026-ARXIV-2606-11806:start -->
### 2606.11806 — External Experience Serving in Production LLM Systems: A Deployment-Oriented Study of Quality-Cost Trade-offs

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：生产 experience serving 要按 task cost structure 在 no experience、global injection 与 selective retrieval 间选择，以 quality、prompt cost、latency 与 break-even 联合决策。

**State / data / control owner。** `AGENT-MEMORY` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.11806v1 §4 setup; §5 Results; Appendices E–G` 支持 `Production moderation plus tool-use and GPQA contrast tasks`；模型 `Reasoning/instruct model variants disclosed in Appendix A.4`；硬件 `Not Disclosed — hosted serving hardware not identified`；精度 `Not Disclosed`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.11806v1 §3 Experience Serving in Production`；counterevidence locator：`arXiv:2606.11806v1 §4.4 claim boundary; Appendix H interpretation scope`。

**Trade-off / failure / coexistence / evolution。** selective retrieval 控制 prompt burden，但 miss/over-trigger 与 selector overhead 会伤害质量；规则少或高度共享时 global compact 仍成立。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-11806:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.11806v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-11806:end -->
<!-- review:SF-2026-ARXIV-2606-11806:end -->

<!-- review:SF-2026-ARXIV-2606-11871:start -->
### 2606.11871 — WarpGuard: Protected-Site Control-Flow Integrity for CUDA SASS Binaries

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：CUDA binary security 的 owner 是 executed SASS consumption site；protected-site CFI 必须恢复 site policy、验证 forward/backward transfer 并对 unsupported surface 显式出账。

**State / data / control owner。** `PLATFORM-SECURITY` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.11871v1 §VI Evaluation; §VII backend cost` 支持 `77 CUDA artifacts; 51,621 sites; 52.2M dynamic checks`；模型 `CUDA SASS binaries`；硬件 `NVIDIA CUDA testbed; exact GPU bound in §VI-A`；精度 `Not applicable — binary instrumentation`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.11871v1 §III threat model; §§IV–V design/implementation`；counterevidence locator：`arXiv:2606.11871v1 §VI-H portability boundaries; §VIII Discussion`。

**Trade-off / failure / coexistence / evolution。** SASS-level enforcement覆盖真实执行面但增加 instrumentation/callback cost；未恢复 site 必须 fail closed 或留在 denominator 外。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-11871:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.11871v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-11871:end -->
<!-- review:SF-2026-ARXIV-2606-11871:end -->

<!-- review:SF-2026-ARXIV-2606-11878:start -->
### 2606.11878 — Gerrymandering the Warp: Non-Control-Data Attacks on CUDA Collective Decisions

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：GPU collective 的 mask、predicate、source lane、descriptor 与 epoch 是 authority-bearing non-control data；应在 collective 使用前绑定 membership/contribution/role/time。

**State / data / control owner。** `PLATFORM-SECURITY` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.11878v1 §VI evidence; §VII-D mitigation results` 支持 `CUDA contract-conformance suite across four authority dimensions`；模型 `CUDA collective primitives and CIC wrapper`；硬件 `NVIDIA CUDA testbed; exact GPU in evidence appendix`；精度 `Not applicable`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.11878v1 §§III–V participation authority and CSC`；counterevidence locator：`arXiv:2606.11878v1 §VII-E Cost and Limits; §VIII Discussion and Limitations`。

**Trade-off / failure / coexistence / evolution。** CIC 防止 range-valid metadata 扭曲授权，却需保存 reference membership/epoch；普通 CFI 不覆盖此语义面。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-11878:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.11878v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-11878:end -->
<!-- review:SF-2026-ARXIV-2606-11878:end -->

<!-- review:SF-2026-ARXIV-2606-11916:start -->
### 2606.11916 — Characterizing Software Aging in GPU-Based LLM Serving Systems

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：LLM serving release 不能只测分钟级峰值；应在 host/device/client 三面进行长时 aging campaign，并用 autocorrelation-aware statistics 区分 leak、runtime 与 workload regime。

**State / data / control owner。** `PLATFORM-MONITORING` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.11916v1 §IV Results; §§IV-A–IV-E` 支持 `216-hour campaign; six co-located deployments; Poisson stress`；模型 `Qwen2.5-7B-Instruct on vLLM, Triton-vLLM and PyTorch/HF`；硬件 `One host with 3× NVIDIA L40S`；精度 `Not Disclosed`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.11916v1 §III Methodology`；counterevidence locator：`arXiv:2606.11916v1 §V Threats to Validity`。

**Trade-off / failure / coexistence / evolution。** 长时 campaign 昂贵且 co-location 可能混入 contention；短基准仍适合 kernel 回归，但不能替代 rejuvenation evidence。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-11916:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.11916v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-11916:end -->
<!-- review:SF-2026-ARXIV-2606-11916:end -->

<!-- review:SF-2026-ARXIV-2606-11949:start -->
### 2606.11949 — Online Shift Detection and Conformal Adaptation for Deployed Safety Classifiers

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：deployed safety classifier 需要 reference-window calibration、sequential alarm、multiplicity control 与 alarm-triggered conformal abstention；shift sensor 与安全 authority 分离。

**State / data / control owner。** `PLATFORM-MONITORING` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.11949v1 §4 setup; §5 Results` 支持 `4 classifiers × 5 shifts × 20 seeds × 2 windows; 800 cells`；模型 `Four deployed safety classifiers`；硬件 `Not Disclosed`；精度 `Not Disclosed`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.11949v1 §3 Methods; §§3.1–3.10`；counterevidence locator：`arXiv:2606.11949v1 §6.5 Limitations; §5.4 ground-truth regimes`。

**Trade-off / failure / coexistence / evolution。** 检测可能对 target attack 无信号，density ratio 也会退化；abstention 恢复 coverage 不等于阻止攻击。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-11949:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.11949v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-11949:end -->
<!-- review:SF-2026-ARXIV-2606-11949:end -->

<!-- review:SF-2026-ARXIV-2606-11998:start -->
### 2606.11998 — Bootstrapped Monitoring: Leveraging Transparent Reasoning to Oversee Stronger AI Agents

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：trusted monitor 能力落后时，可用更强 untrusted monitor 评估 action，再让 weaker trusted model 监督其透明推理；control graph 要显式保存 collusion threat model。

**State / data / control owner。** `PLATFORM-SECURITY` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.11998v1 §4 Results; Appendix C red/blue teaming` 支持 `Multi-turn BashArena software-engineering tasks`；模型 `Trusted, untrusted-agent and intermediate-monitor model configurations`；硬件 `Not Disclosed — API/runtime hardware not identified`；精度 `Not Disclosed`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.11998v1 §3 Methods; §3.1 threat model/protocol`；counterevidence locator：`arXiv:2606.11998v1 §5 Discussion, Transparent CoT assumption and Limitations`。

**Trade-off / failure / coexistence / evolution。** bootstrapping 延长弱 monitor 生命周期，却依赖 transparent CoT；隐藏推理、steganography 或共同盲点会失效。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-11998:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.11998v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-11998:end -->
<!-- review:SF-2026-ARXIV-2606-11998:end -->

<!-- review:SF-2026-ARXIV-2606-12243:start -->
### 2606.12243 — VIA-SD: Verification via Intra-Model Routing for Speculative Decoding

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：把 draft verification 从二元 accept/full-recompute 演进为 direct/slim/full 三层，并用 intra-model routing 选择 verifier 资源。

**State / data / control owner。** `INFER-SPECULATIVE-DECODING` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.12243v1 §4 Experiments` 支持 `Four tasks across T5/Gemma model families`；模型 `T5 and Gemma families`；硬件 `Disclosed in §4.1; no cross-paper normalization`；精度 `Disclosed in §4.1 where applicable`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.12243v1 §3 Methodology; §§3.2–3.5`；counterevidence locator：`arXiv:2606.12243v1 §4.4 additional analysis; §5 Conclusion`。

**Trade-off / failure / coexistence / evolution。** slim verifier 节约 full-model calls 但引入 routing error/threshold；exact rejection contract 与 full verifier fallback 必须保留。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-12243:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.12243v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-12243:end -->
<!-- review:SF-2026-ARXIV-2606-12243:end -->

<!-- review:SF-2026-ARXIV-2606-12320:start -->
### 2606.12320 — A Five-Plane Reference Architecture for Runtime Governance of Production AI Agents

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：生产 Agent governance 应分 reasoning/network/identity/endpoint/data 五平面，并把 stop-anywhere mediation、capability attenuation、TTL 与 structured audit 组合为 cross-plane control。

**State / data / control owner。** `PLATFORM-SECURITY` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.12320v1 §9 case studies; §10 validation roadmap` 支持 `Seven canonical workflow threats plus production case studies`；模型 `Reference architecture; not a model benchmark`；硬件 `Not applicable`；精度 `Not applicable`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.12320v1 §§3–8 threat model, five planes and composed architecture`；counterevidence locator：`arXiv:2606.12320v1 §11 Limitations and Open Questions`。

**Trade-off / failure / coexistence / evolution。** 多平面提高可中断性与归因，却增加 latency/state consistency/TCB；reference architecture 不证明生产效果。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-12320:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.12320v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-12320:end -->
<!-- review:SF-2026-ARXIV-2606-12320:end -->

<!-- review:SF-2026-ARXIV-2606-12329:start -->
### 2606.12329 — PROJECTMEM: A Local-First, Event-Sourced Memory and Judgment Layer for AI Coding Agents

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：Coding-agent memory 可用 append-only typed event log 作 authoritative state，并确定性投影摘要；pre-action gate 只消费既有 failure/fragility evidence。

**State / data / control owner。** `AGENT-MEMORY` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.12329v1 §7 Evaluation` 支持 `Two-month self-study, 10 projects, 207 events`；模型 `Local-first projectmem with MCP/CLI`；硬件 `Local developer environment; hardware not disclosed`；精度 `Not applicable`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.12329v1 §3 System Design; §§4–6 architecture/implementation`；counterevidence locator：`arXiv:2606.12329v1 §8 Limitations and Future Work`。

**Trade-off / failure / coexistence / evolution。** event sourcing 提供 provenance/rollback，但 self-study 不能证明跨团队收益；错误 judgment 仍需 supersession 与关闭开关。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-12329:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.12329v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-12329:end -->
<!-- review:SF-2026-ARXIV-2606-12329:end -->

<!-- review:SF-2026-ARXIV-2606-12370:start -->
### 2606.12370 — Breaking Entropy Bounds: Accelerating RL Training via MTP with Rejection Sampling

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：RL rollout acceleration 中 MTP acceptance 受 policy entropy 与 draft mismatch 联合约束；rejection sampling 与 TV objective 比 target-only 接受对 policy update 更平滑。

**State / data / control owner。** `INFER-SPECULATIVE-DECODING` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.12370v1 §6 Experiments` 支持 `RL math/reasoning workloads and MTP acceptance/throughput sweeps`；模型 `Multiple MTP-enabled LLM scales`；硬件 `Disclosed in experimental appendix`；精度 `Disclosed in experimental appendix`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.12370v1 §§3–5 entropy bound, TV loss and adaptation`；counterevidence locator：`arXiv:2606.12370v1 §7.8 top-k instability; §9 Limitations`。

**Trade-off / failure / coexistence / evolution。** 更新 MTP 提升 rollout throughput 却增加训练耦合；top-k TV 不稳，完整 rejection sampling 是 correctness fallback；TRAIN-RLHF 只消费 rollout throughput 与 policy-update handoff。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-12370:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.12370v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-12370:end -->
<!-- review:SF-2026-ARXIV-2606-12370:end -->

<!-- review:SF-2026-ARXIV-2606-12385:start -->
### 2606.12385 — Which Models Are Our Models Built On? Auditing Invisible Dependencies in Modern LLMs

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：模型卡不足以表达递归 training dependencies；provenance 应以 artifact identity 和 operation-centered edges 递归解析生成、过滤、judge 与 selection 关系。

**State / data / control owner。** `TRAIN-DATA` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.12385v1 §4 Evaluation; §5 Findings` 支持 `Public-artifact dependency reconstruction across target LLMs`；模型 `Agentic ModSleuth plus audited model artifacts`；硬件 `Not Disclosed — document analysis workload`；精度 `Not applicable`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.12385v1 §3 Design of ModSleuth`；counterevidence locator：`arXiv:2606.12385v1 Appendix A verification; Appendix D disclosure gaps`。

**Trade-off / failure / coexistence / evolution。** 递归发现提高 lineage 但受公开文档缺失和 entity resolution 错误限制；它是 audit evidence，不是完整 SBOM guarantee。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-12385:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.12385v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-12385:end -->
<!-- review:SF-2026-ARXIV-2606-12385:end -->

<!-- review:SF-2026-ARXIV-2606-12487:start -->
### 2606.12487 — DynamicPTQ: Mitigating Activation Quantization Collapse via Residual-Stream Dynamics

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：4-bit activation/KV PTQ 需要观察 residual stream 的 phase-wise jump，并对关键相位采用 mixed precision，而非只做静态 rotation smoothing。

**State / data / control owner。** `INFER-TENSORRT-LLM` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.12487v1 §4 Experiments; §4.9 efficiency` 支持 `Perplexity, zero-shot QA, reasoning and efficiency across dense/MoE LLMs`；模型 `Multiple dense and MoE PTQ backbones`；硬件 `Disclosed in §4.2; exact accelerator remains paper-bound`；精度 `W4A4/KV4 with phase-aware higher precision`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.12487v1 §3 Method; §3.3 policy`；counterevidence locator：`arXiv:2606.12487v1 §7 Discussion; no dedicated limitations section`。

**Trade-off / failure / coexistence / evolution。** mixed precision 减少 collapse 却削弱全 4-bit memory/throughput 收益；新 backbone 需重新 calibration。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-12487:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.12487v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-12487:end -->
<!-- review:SF-2026-ARXIV-2606-12487:end -->

<!-- review:SF-2026-ARXIV-2606-12556:start -->
### 2606.12556 — ITME: Inference Tiered Memory Expansion with Disaggregated CXL-Hybrid Memories

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：长 context state 可跨 GPU/host/CXL-hybrid/NVMe 构成 byte-addressable tier，并利用 model-weight/prefix access 可预测性做 multi-tier DMA prefetch。

**State / data / control owner。** `INFER-GPU-MEMORY` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.12556v1 §5 methodology; §6 evaluation` 支持 `Weight and KV offload across GPU, host, CXL and NVMe-oF tiers`；模型 `LLM inference configurations disclosed in §5.1`；硬件 `SK hynix CMM, PCIe Gen5 NVMe SSDs and FPGA prototype`；精度 `Not Disclosed`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.12556v1 §3 CXL-Hybrid Architecture; §4 ITME`；counterevidence locator：`arXiv:2606.12556v1 §8 Conclusion; no dedicated limitations section`。

**Trade-off / failure / coexistence / evolution。** 扩容降低 HBM pressure，却增加预取错误、fabric contention 和硬件成本；不可预测 KV access 仍需普通 paging。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-12556:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.12556v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-12556:end -->
<!-- review:SF-2026-ARXIV-2606-12556:end -->

<!-- review:SF-2026-ARXIV-2606-12688:start -->
### 2606.12688 — M*: A Modular, Extensible, Serving System for Multimodal Models

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：复合多模态模型的 serving contract 应从固定 stage DAG 演进为 model graph + named walks，显式支持 seq/parallel/loop/dynamic-loop/stream 与 component placement。

**State / data / control owner。** `INFER-KSERVE-TOPOLOGY` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.12688v1 §4 Evaluation; Appendix I reproducibility` 支持 `BAGEL, Qwen3-Omni, Orpheus and V-JEPA2 composite workloads`；模型 `BAGEL-7B, Qwen3-Omni-30B-A3B, Orpheus-3B, V-JEPA2`；硬件 `Single 4×H100 node or 8×H200 node`；精度 `Model-specific; not normalized as one precision`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.12688v1 §3 Walk Graph; §§3.1–3.3`；counterevidence locator：`arXiv:2606.12688v1 Appendix H Limitations`。

**Trade-off / failure / coexistence / evolution。** 通用 graph runtime 减少 glue code，却把 state machine、placement、tensor transport 与 per-component batch 变成新控制面；专用引擎仍可能更简单。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-12688:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.12688v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-12688:end -->
<!-- review:SF-2026-ARXIV-2606-12688:end -->

<!-- review:SF-2026-ARXIV-2606-12703:start -->
### 2606.12703 — SMSR: Certified Defence Against Runtime Memory Poisoning in Persistent LLM Agent Systems

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：Persistent memory poisoning 的 certified boundary 必须在 write-time 做 cryptographic provenance，并在 query-time 对 authenticated adversary 做 randomized ablation 与 verdict aggregation。

**State / data / control owner。** `PLATFORM-SECURITY` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.12703v1 §VII Evaluation` 支持 `15 enterprise scenarios; 3,150 repeated plus 450 production-scale trials`；模型 `Persistent RAG-agent configurations; second-agent generality check`；硬件 `Not Disclosed`；精度 `Not Disclosed`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.12703v1 §III threat model; §§IV–VI impossibility/SMSR/certificate`；counterevidence locator：`arXiv:2606.12703v1 §VIII Discussion; provenance-key and smoothing assumptions`。

**Trade-off / failure / coexistence / evolution。** HMAC 阻止 unsigned injection 不处理合法凭据滥用；smoothing 增加多次 retrieval/inference 成本且证书依赖 threat bound。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-12703:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.12703v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-12703:end -->
<!-- review:SF-2026-ARXIV-2606-12703:end -->

<!-- review:SF-2026-ARXIV-2606-12736:start -->
### 2606.12736 — Benchmarking AI Agents for Addressing Scientific Challenges Across Scales

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：Scientific agent evaluation 需要 interactive environment、stepwise verification、domain slices 与 open-ended failure taxonomy，不能把 research 压成静态最终答案。

**State / data / control owner。** `PLATFORM-EVALUATION-SYSTEM` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.12736v1 §2 Results across domains; §2.6 errors` 支持 `Approximately 200 scientific tasks across multiple scales/domains`；模型 `Diverse agent-agnostic systems`；硬件 `Not Disclosed — heterogeneous/API agents`；精度 `Not Disclosed`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.12736v1 §4 Methods; §4.1 framework`；counterevidence locator：`arXiv:2606.12736v1 §3 Discussion`。

**Trade-off / failure / coexistence / evolution。** step verifier 提高诊断性但依赖领域 rubric；novel insight 与 self-directed exploration 仍难可靠验证。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-12736:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.12736v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-12736:end -->
<!-- review:SF-2026-ARXIV-2606-12736:end -->

<!-- review:SF-2026-ARXIV-2606-12737:start -->
### 2606.12737 — PI-Hunter: Automated Red-Teaming for Exposing and Localizing Prompt Injections

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：Prompt-injection red team 应从 attack-success search 扩为 source-aware test construction、feedback evolution、verification 与 localization，输出可修复 attack surface。

**State / data / control owner。** `PLATFORM-SECURITY` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.12737v1 §4 Experiments; Appendices B–D` 支持 `Multiple agent benchmarks, architectures, attacks and defenses`；模型 `Agent and evaluator models disclosed in §4.1`；硬件 `Not Disclosed — hosted model hardware`；精度 `Not Disclosed`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.12737v1 §3 PI-Hunter; §§3.1–3.3`；counterevidence locator：`arXiv:2606.12737v1 §4.4 ablations; §5 Conclusion; no dedicated limitations section`。

**Trade-off / failure / coexistence / evolution。** 更广 exposure 不等于防御；搜索受 mutation/evaluator repertoire 约束，held-out attacks 与 runtime enforcement 仍必要。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-12737:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.12737v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-12737:end -->
<!-- review:SF-2026-ARXIV-2606-12737:end -->

<!-- review:SF-2026-ARXIV-2606-12764:start -->
### 2606.12764 — Detecting Functional Memorization in Code Language Models

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：Code training-data audit 必须检测 functional equivalence，而不能只依赖文本 overlap；应以 exposed target 对未 exposed reference 做 counterfactual execution comparison。

**State / data / control owner。** `TRAIN-DATA` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.12764v1 §4 Results; Appendices A–C/E` 支持 `Python function-signature continuations with execution-based and LLM-judge functional comparison`；模型 `OLMo-3-32B midtrained target versus pretrained reference`；硬件 `Not Disclosed`；精度 `Not Disclosed`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.12764v1 §3 Counterfactual functional memorization`；counterevidence locator：`arXiv:2606.12764v1 §4 result scope; no dedicated limitations section`。

**Trade-off / failure / coexistence / evolution。** execution 更接近语义但覆盖有限输入；LLM judge 是受 operating point 约束的 proxy，不能替代 license/provenance evidence。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-12764:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.12764v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-12764:end -->
<!-- review:SF-2026-ARXIV-2606-12764:end -->

<!-- review:SF-2026-ARXIV-2606-12765:start -->
### 2606.12765 — Rigel: Reverse-Engineering the Metal 4.1 Tensor Compute Path on the Apple M4 Max GPU

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：Low-precision backend contract 必须通过 checksum/provenance microbench 分离 interface support、真正加速、accumulator width、execution rail 与 fragment layout。

**State / data / control owner。** `INFER-TENSORRT-LLM` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.12765v1 §§4–8 measurements and fused-kernel result` 支持 `Metal 4.1 matmul2d microbenchmarks and fused GEMM+bias+GELU`；模型 `Metal Performance Primitives tensor path`；硬件 `Single Apple M4 Max GPU`；精度 `fp8 E4M3, fp16, accumulator ≥fp32 evidence`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.12765v1 §3 Methodology; §§4–8 characterization`；counterevidence locator：`arXiv:2606.12765v1 §10 Discussion and limitations`。

**Trade-off / failure / coexistence / evolution。** 单芯片逆向结果不能外推其他 Apple generations；fp8 在该硬件省 footprint 而非提高吞吐。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-12765:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.12765v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-12765:end -->
<!-- review:SF-2026-ARXIV-2606-12765:end -->

<!-- review:SF-2026-ARXIV-2606-13708:start -->
### 2606.13708 — Tiara: A Programmable Line-Rate ISA for Remote Memory Access

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：Remote-memory indirection 可用 memory-side NIC 上预注册、静态可验证的 compact ISA 执行，把依赖链从多 RTT 收敛为一次 request。

**State / data / control owner。** `INFER-PD-DISAGGREGATION` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.13708v1 §4 Evaluation; §§4.5–4.6 AI workloads` 支持 `Graph, page-table, lock, MoE gather and disaggregated PagedAttention`；模型 `PagedAttention 8KB blocks; MoE 32 experts`；硬件 `FPGA-based memory-side NIC prototype`；精度 `Not applicable`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.13708v1 §3 Tiara Design; compiler/verifier`；counterevidence locator：`arXiv:2606.13708v1 §6 Conclusion; no dedicated limitations section`。

**Trade-off / failure / coexistence / evolution。** line-rate operator 降低 RTT，却限制程序表达力并扩大 NIC TCB；复杂/动态逻辑仍需 CPU/RPC fallback。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-13708:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.13708v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-13708:end -->
<!-- review:SF-2026-ARXIV-2606-13708:end -->

<!-- review:SF-2026-ARXIV-2606-14779:start -->
### 2606.14779 — Unified KV Pooling to Accelerate Long-Context LLM Serving

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：KV offload 不应串行穿过单 host/SSD；应把多 DRAM/SSD 汇成 bandwidth-weighted pool，并以 user-space SPDK bypass filesystem。

**State / data / control owner。** `INFER-GPU-MEMORY` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.14779v1 §V Evaluation` 支持 `Long-context KV offload and TTFT/I/O sweeps`；模型 `Llama-3.1-8B, GPT-OSS-20B, Qwen3-30B-A3B`；硬件 `Multi-host-memory and SSD testbed disclosed in §V-A`；精度 `Model/KV precision disclosed in §V-A`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.14779v1 §IV Design; KV orchestrator and passthrough`；counterevidence locator：`arXiv:2606.14779v1 §VI Discussion`。

**Trade-off / failure / coexistence / evolution。** pooling 降低 blocked I/O，却引入 allocator metadata、failure recovery 与 SPDK 运维成本；短 context/HBM-resident path 仍更简单。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-14779:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.14779v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-14779:end -->
<!-- review:SF-2026-ARXIV-2606-14779:end -->

<!-- review:SF-2026-ARXIV-2606-14783:start -->
### 2606.14783 — The Vision Encoder as a Privacy Boundary: Visual-Token Side Channels in Encoder-Free Vision-Language Models

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：Encoder-free VLM 的 visual tokens 与 layer-0 KV 可能成为 output filter 之前的可逆 privacy side channel；architecture 与 cache access 必须进入 threat model。

**State / data / control owner。** `PLATFORM-SECURITY` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.14783v1 §3 setup; §§4–7 experiments` 支持 `Held-out access-code inversion, clutter/degradation/transfer and defense ablations`；模型 `Gemma4/Fuyu vs Qwen3-VL/InternVL/LLaVA controls`；硬件 `Not Disclosed`；精度 `Token/value quantization tested as ineffective value-level defense`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.14783v1 §2 Threat Model; §§4–8 mechanism/defense`；counterevidence locator：`arXiv:2606.14783v1 §8 Defense Boundary; §9 deployment implications`。

**Trade-off / failure / coexistence / evolution。** 降低 spatial sampling 可减泄漏但可能损失 OCR/细节能力；value noise/quantization 不构成通用缓解。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-14783:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.14783v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-14783:end -->
<!-- review:SF-2026-ARXIV-2606-14783:end -->

<!-- review:SF-2026-ARXIV-2606-18284:start -->
### 2606.18284 — Breaking the Solver Bottleneck: Training Task Generators at the Learnable Frontier

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：训练 task generator 时可用一次 solver-labeled pool 训练 activation probe，把 targeted solve-rate 作为 amortized reward；最终仍由 held-out solver 验证。

**State / data / control owner。** `TRAIN-DATA` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.18284v1 §§4 and 6 Evaluation/Results` 支持 `Math, code and SWE task generation across model scales`；模型 `Qwen2.5-3B/7B and Qwen3.5-27B solver settings`；硬件 `Not Disclosed`；精度 `Not Disclosed`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.18284v1 §3 Probe Rewards; §5 probe data/selection`；counterevidence locator：`arXiv:2606.18284v1 §7 Limitations; mode-collapse findings`。

**Trade-off / failure / coexistence / evolution。** probe 降低 inner-loop solver cost，但 reward hacking、mode collapse 与 solver drift 要求 held-out solver gate。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-18284:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.18284v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-18284:end -->
<!-- review:SF-2026-ARXIV-2606-18284:end -->

<!-- review:SF-2026-ARXIV-2606-18286:start -->
### 2606.18286 — CODEBLOCK: Learning to Supervise Code at the Right Granularity

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：Code SFT 的 sparse supervision unit 应是 syntax-complete、data-flow-connected code block，而非孤立 high-loss token；完整 response 继续作 context。

**State / data / control owner。** `TRAIN-SFT` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.18286v1 §6 Experiments; Appendix A` 支持 `Six code-generation benchmarks`；模型 `Qwen2.5-Coder-1.5B-Instruct and comparison models`；硬件 `Disclosed in Appendix A.3; exact accelerator remains v1-bound`；精度 `Training precision disclosed in Appendix A.3`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.18286v1 §5 Method; §§5.1–5.4`；counterevidence locator：`arXiv:2606.18286v1 §7 Conclusion; Appendix C runtime analysis`。

**Trade-off / failure / coexistence / evolution。** 仅 1.9% supervised tokens 降低 loss work，却依赖 parser/data-flow correctness；错误 block 边界会删除必要 credit，full-token SFT 仍是稳健基线。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-18286:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.18286v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-18286:end -->
<!-- review:SF-2026-ARXIV-2606-18286:end -->

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-11543 | score_7_9; potential_books_delta | not_selected | — | — | Retained after full review, but subsumed in narrative priority by three non-overlapping units; review remains authoritative. | analysis-decision:SF-2026-ARXIV-2606-11543 |
| SF-2026-ARXIV-2606-11632 | score_7_9; potential_books_delta | selected | DA-20260611-ADMISSION | — | Selected after 31/31 frontier comparison for non-overlapping control-plane, reliability, or serving-abstraction novelty. | analysis:DA-20260611-ADMISSION |
| SF-2026-ARXIV-2606-11671 | score_7_9; potential_books_delta | not_selected | — | — | Retained after full review, but subsumed in narrative priority by three non-overlapping units; review remains authoritative. | analysis-decision:SF-2026-ARXIV-2606-11671 |
| SF-2026-ARXIV-2606-11686 | score_7_9; potential_books_delta | not_selected | — | — | Retained after full review, but subsumed in narrative priority by three non-overlapping units; review remains authoritative. | analysis-decision:SF-2026-ARXIV-2606-11686 |
| SF-2026-ARXIV-2606-11688 | score_7_9; potential_books_delta | not_selected | — | — | Retained after full review, but subsumed in narrative priority by three non-overlapping units; review remains authoritative. | analysis-decision:SF-2026-ARXIV-2606-11688 |
| SF-2026-ARXIV-2606-11690 | score_7_9; potential_books_delta | not_selected | — | — | Retained after full review, but subsumed in narrative priority by three non-overlapping units; review remains authoritative. | analysis-decision:SF-2026-ARXIV-2606-11690 |
| SF-2026-ARXIV-2606-11718 | score_7_9; potential_books_delta | not_selected | — | — | Retained after full review, but subsumed in narrative priority by three non-overlapping units; review remains authoritative. | analysis-decision:SF-2026-ARXIV-2606-11718 |
| SF-2026-ARXIV-2606-11806 | score_7_9; potential_books_delta | not_selected | — | — | Retained after full review, but subsumed in narrative priority by three non-overlapping units; review remains authoritative. | analysis-decision:SF-2026-ARXIV-2606-11806 |
| SF-2026-ARXIV-2606-11871 | score_7_9; potential_books_delta | not_selected | — | — | Retained after full review, but subsumed in narrative priority by three non-overlapping units; review remains authoritative. | analysis-decision:SF-2026-ARXIV-2606-11871 |
| SF-2026-ARXIV-2606-11878 | score_7_9; potential_books_delta | not_selected | — | — | Retained after full review, but subsumed in narrative priority by three non-overlapping units; review remains authoritative. | analysis-decision:SF-2026-ARXIV-2606-11878 |
| SF-2026-ARXIV-2606-11916 | score_7_9; potential_books_delta | selected | DA-20260611-AGING | — | Selected after 31/31 frontier comparison for non-overlapping control-plane, reliability, or serving-abstraction novelty. | analysis:DA-20260611-AGING |
| SF-2026-ARXIV-2606-11949 | score_7_9; potential_books_delta | not_selected | — | — | Retained after full review, but subsumed in narrative priority by three non-overlapping units; review remains authoritative. | analysis-decision:SF-2026-ARXIV-2606-11949 |
| SF-2026-ARXIV-2606-11998 | score_7_9; potential_books_delta | not_selected | — | — | Retained after full review, but subsumed in narrative priority by three non-overlapping units; review remains authoritative. | analysis-decision:SF-2026-ARXIV-2606-11998 |
| SF-2026-ARXIV-2606-12243 | score_7_9 | not_selected | — | — | Retained after full review, but subsumed in narrative priority by three non-overlapping units; review remains authoritative. | analysis-decision:SF-2026-ARXIV-2606-12243 |
| SF-2026-ARXIV-2606-12320 | score_7_9; potential_books_delta | not_selected | — | — | Retained after full review, but subsumed in narrative priority by three non-overlapping units; review remains authoritative. | analysis-decision:SF-2026-ARXIV-2606-12320 |
| SF-2026-ARXIV-2606-12329 | score_7_9; potential_books_delta | not_selected | — | — | Retained after full review, but subsumed in narrative priority by three non-overlapping units; review remains authoritative. | analysis-decision:SF-2026-ARXIV-2606-12329 |
| SF-2026-ARXIV-2606-12370 | score_7_9 | not_selected | — | — | Retained after full review, but subsumed in narrative priority by three non-overlapping units; review remains authoritative. | analysis-decision:SF-2026-ARXIV-2606-12370 |
| SF-2026-ARXIV-2606-12385 | score_7_9; potential_books_delta | not_selected | — | — | Retained after full review, but subsumed in narrative priority by three non-overlapping units; review remains authoritative. | analysis-decision:SF-2026-ARXIV-2606-12385 |
| SF-2026-ARXIV-2606-12487 | score_7_9 | not_selected | — | — | Retained after full review, but subsumed in narrative priority by three non-overlapping units; review remains authoritative. | analysis-decision:SF-2026-ARXIV-2606-12487 |
| SF-2026-ARXIV-2606-12556 | score_7_9; potential_books_delta | not_selected | — | — | Retained after full review, but subsumed in narrative priority by three non-overlapping units; review remains authoritative. | analysis-decision:SF-2026-ARXIV-2606-12556 |
| SF-2026-ARXIV-2606-12688 | score_7_9; potential_books_delta | selected | DA-20260611-COMPOSITE-SERVING | — | Selected after 31/31 frontier comparison for non-overlapping control-plane, reliability, or serving-abstraction novelty. | analysis:DA-20260611-COMPOSITE-SERVING |
| SF-2026-ARXIV-2606-12703 | score_7_9; potential_books_delta | not_selected | — | — | Retained after full review, but subsumed in narrative priority by three non-overlapping units; review remains authoritative. | analysis-decision:SF-2026-ARXIV-2606-12703 |
| SF-2026-ARXIV-2606-12736 | score_7_9 | not_selected | — | — | Retained after full review, but subsumed in narrative priority by three non-overlapping units; review remains authoritative. | analysis-decision:SF-2026-ARXIV-2606-12736 |
| SF-2026-ARXIV-2606-12737 | score_7_9; potential_books_delta | not_selected | — | — | Retained after full review, but subsumed in narrative priority by three non-overlapping units; review remains authoritative. | analysis-decision:SF-2026-ARXIV-2606-12737 |
| SF-2026-ARXIV-2606-12764 | score_7_9; potential_books_delta | not_selected | — | — | Retained after full review, but subsumed in narrative priority by three non-overlapping units; review remains authoritative. | analysis-decision:SF-2026-ARXIV-2606-12764 |
| SF-2026-ARXIV-2606-12765 | score_7_9 | not_selected | — | — | Retained after full review, but subsumed in narrative priority by three non-overlapping units; review remains authoritative. | analysis-decision:SF-2026-ARXIV-2606-12765 |
| SF-2026-ARXIV-2606-13708 | score_7_9; potential_books_delta | not_selected | — | — | Retained after full review, but subsumed in narrative priority by three non-overlapping units; review remains authoritative. | analysis-decision:SF-2026-ARXIV-2606-13708 |
| SF-2026-ARXIV-2606-14779 | score_7_9; potential_books_delta | not_selected | — | — | Retained after full review, but subsumed in narrative priority by three non-overlapping units; review remains authoritative. | analysis-decision:SF-2026-ARXIV-2606-14779 |
| SF-2026-ARXIV-2606-14783 | score_7_9; potential_books_delta | not_selected | — | — | Retained after full review, but subsumed in narrative priority by three non-overlapping units; review remains authoritative. | analysis-decision:SF-2026-ARXIV-2606-14783 |
| SF-2026-ARXIV-2606-18284 | score_7_9; potential_books_delta | not_selected | — | — | Retained after full review, but subsumed in narrative priority by three non-overlapping units; review remains authoritative. | analysis-decision:SF-2026-ARXIV-2606-18284 |
| SF-2026-ARXIV-2606-18286 | score_7_9; potential_books_delta | not_selected | — | — | Retained after full review, but subsumed in narrative priority by three non-overlapping units; review remains authoritative. | analysis-decision:SF-2026-ARXIV-2606-18286 |

<!-- analysis-decision:SF-2026-ARXIV-2606-11543:start -->
Skill 的目录组织本身会改变资源读取与有效采用轨迹；Progressive Disclosure 必须以知识等价变体、trajectory evidence 与 verifier outcome 联合评测。 It did not outrank the three selected non-overlapping units for today's compact analysis.
<!-- analysis-decision:SF-2026-ARXIV-2606-11543:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-11671:start -->
Skill 安全不能只审静态文件；应按 capability profile 构造 targeted runtime context，在 sandbox 中执行并以 trace evidence 标注行为。 It did not outrank the three selected non-overlapping units for today's compact analysis.
<!-- analysis-decision:SF-2026-ARXIV-2606-11671:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-11686:start -->
生产 Agent 的 deterministic scaffold 应按 ontology/intent/routing/decomposition/escalation/safety/memory 分层，用 no-LLM regression-locked slices 阻止 aggregate pass rate 掩盖局部回归。 It did not outrank the three selected non-overlapping units for today's compact analysis.
<!-- analysis-decision:SF-2026-ARXIV-2606-11686:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-11688:start -->
长程 Agent 应把 durable FSM、stateless ticks、falsifiable gate 与 terminal hard floor 外置，使未执行/未通过 gate 时最多 honest stall，不能宣告完成。 It did not outrank the three selected non-overlapping units for today's compact analysis.
<!-- analysis-decision:SF-2026-ARXIV-2606-11688:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-11690:start -->
LLM 成本必须把 offered load λ 经 Little's Law 映射为 in-flight concurrency 与实际利用率；固定 100% utilization 的每 token 估价会系统性误导低负载自托管。 It did not outrank the three selected non-overlapping units for today's compact analysis.
<!-- analysis-decision:SF-2026-ARXIV-2606-11690:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-11718:start -->
Chiplet GPU 的 GEMM locality 需要让 chiplet-local tiles 在 global address space 连续，使 page-granularity placement 与 CTA affinity 一致。 It did not outrank the three selected non-overlapping units for today's compact analysis.
<!-- analysis-decision:SF-2026-ARXIV-2606-11718:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-11806:start -->
生产 experience serving 要按 task cost structure 在 no experience、global injection 与 selective retrieval 间选择，以 quality、prompt cost、latency 与 break-even 联合决策。 It did not outrank the three selected non-overlapping units for today's compact analysis.
<!-- analysis-decision:SF-2026-ARXIV-2606-11806:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-11871:start -->
CUDA binary security 的 owner 是 executed SASS consumption site；protected-site CFI 必须恢复 site policy、验证 forward/backward transfer 并对 unsupported surface 显式出账。 It did not outrank the three selected non-overlapping units for today's compact analysis.
<!-- analysis-decision:SF-2026-ARXIV-2606-11871:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-11878:start -->
GPU collective 的 mask、predicate、source lane、descriptor 与 epoch 是 authority-bearing non-control data；应在 collective 使用前绑定 membership/contribution/role/time。 It did not outrank the three selected non-overlapping units for today's compact analysis.
<!-- analysis-decision:SF-2026-ARXIV-2606-11878:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-11949:start -->
deployed safety classifier 需要 reference-window calibration、sequential alarm、multiplicity control 与 alarm-triggered conformal abstention；shift sensor 与安全 authority 分离。 It did not outrank the three selected non-overlapping units for today's compact analysis.
<!-- analysis-decision:SF-2026-ARXIV-2606-11949:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-11998:start -->
trusted monitor 能力落后时，可用更强 untrusted monitor 评估 action，再让 weaker trusted model 监督其透明推理；control graph 要显式保存 collusion threat model。 It did not outrank the three selected non-overlapping units for today's compact analysis.
<!-- analysis-decision:SF-2026-ARXIV-2606-11998:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-12243:start -->
把 draft verification 从二元 accept/full-recompute 演进为 direct/slim/full 三层，并用 intra-model routing 选择 verifier 资源。 It did not outrank the three selected non-overlapping units for today's compact analysis.
<!-- analysis-decision:SF-2026-ARXIV-2606-12243:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-12320:start -->
生产 Agent governance 应分 reasoning/network/identity/endpoint/data 五平面，并把 stop-anywhere mediation、capability attenuation、TTL 与 structured audit 组合为 cross-plane control。 It did not outrank the three selected non-overlapping units for today's compact analysis.
<!-- analysis-decision:SF-2026-ARXIV-2606-12320:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-12329:start -->
Coding-agent memory 可用 append-only typed event log 作 authoritative state，并确定性投影摘要；pre-action gate 只消费既有 failure/fragility evidence。 It did not outrank the three selected non-overlapping units for today's compact analysis.
<!-- analysis-decision:SF-2026-ARXIV-2606-12329:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-12370:start -->
RL rollout acceleration 中 MTP acceptance 受 policy entropy 与 draft mismatch 联合约束；rejection sampling 与 TV objective 比 target-only 接受对 policy update 更平滑。 It did not outrank the three selected non-overlapping units for today's compact analysis.
<!-- analysis-decision:SF-2026-ARXIV-2606-12370:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-12385:start -->
模型卡不足以表达递归 training dependencies；provenance 应以 artifact identity 和 operation-centered edges 递归解析生成、过滤、judge 与 selection 关系。 It did not outrank the three selected non-overlapping units for today's compact analysis.
<!-- analysis-decision:SF-2026-ARXIV-2606-12385:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-12487:start -->
4-bit activation/KV PTQ 需要观察 residual stream 的 phase-wise jump，并对关键相位采用 mixed precision，而非只做静态 rotation smoothing。 It did not outrank the three selected non-overlapping units for today's compact analysis.
<!-- analysis-decision:SF-2026-ARXIV-2606-12487:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-12556:start -->
长 context state 可跨 GPU/host/CXL-hybrid/NVMe 构成 byte-addressable tier，并利用 model-weight/prefix access 可预测性做 multi-tier DMA prefetch。 It did not outrank the three selected non-overlapping units for today's compact analysis.
<!-- analysis-decision:SF-2026-ARXIV-2606-12556:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-12703:start -->
Persistent memory poisoning 的 certified boundary 必须在 write-time 做 cryptographic provenance，并在 query-time 对 authenticated adversary 做 randomized ablation 与 verdict aggregation。 It did not outrank the three selected non-overlapping units for today's compact analysis.
<!-- analysis-decision:SF-2026-ARXIV-2606-12703:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-12736:start -->
Scientific agent evaluation 需要 interactive environment、stepwise verification、domain slices 与 open-ended failure taxonomy，不能把 research 压成静态最终答案。 It did not outrank the three selected non-overlapping units for today's compact analysis.
<!-- analysis-decision:SF-2026-ARXIV-2606-12736:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-12737:start -->
Prompt-injection red team 应从 attack-success search 扩为 source-aware test construction、feedback evolution、verification 与 localization，输出可修复 attack surface。 It did not outrank the three selected non-overlapping units for today's compact analysis.
<!-- analysis-decision:SF-2026-ARXIV-2606-12737:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-12764:start -->
Code training-data audit 必须检测 functional equivalence，而不能只依赖文本 overlap；应以 exposed target 对未 exposed reference 做 counterfactual execution comparison。 It did not outrank the three selected non-overlapping units for today's compact analysis.
<!-- analysis-decision:SF-2026-ARXIV-2606-12764:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-12765:start -->
Low-precision backend contract 必须通过 checksum/provenance microbench 分离 interface support、真正加速、accumulator width、execution rail 与 fragment layout。 It did not outrank the three selected non-overlapping units for today's compact analysis.
<!-- analysis-decision:SF-2026-ARXIV-2606-12765:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-13708:start -->
Remote-memory indirection 可用 memory-side NIC 上预注册、静态可验证的 compact ISA 执行，把依赖链从多 RTT 收敛为一次 request。 It did not outrank the three selected non-overlapping units for today's compact analysis.
<!-- analysis-decision:SF-2026-ARXIV-2606-13708:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-14779:start -->
KV offload 不应串行穿过单 host/SSD；应把多 DRAM/SSD 汇成 bandwidth-weighted pool，并以 user-space SPDK bypass filesystem。 It did not outrank the three selected non-overlapping units for today's compact analysis.
<!-- analysis-decision:SF-2026-ARXIV-2606-14779:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-14783:start -->
Encoder-free VLM 的 visual tokens 与 layer-0 KV 可能成为 output filter 之前的可逆 privacy side channel；architecture 与 cache access 必须进入 threat model。 It did not outrank the three selected non-overlapping units for today's compact analysis.
<!-- analysis-decision:SF-2026-ARXIV-2606-14783:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-18284:start -->
训练 task generator 时可用一次 solver-labeled pool 训练 activation probe，把 targeted solve-rate 作为 amortized reward；最终仍由 held-out solver 验证。 It did not outrank the three selected non-overlapping units for today's compact analysis.
<!-- analysis-decision:SF-2026-ARXIV-2606-18284:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-18286:start -->
Code SFT 的 sparse supervision unit 应是 syntax-complete、data-flow-connected code block，而非孤立 high-loss token；完整 response 继续作 context。 It did not outrank the three selected non-overlapping units for today's compact analysis.
<!-- analysis-decision:SF-2026-ARXIV-2606-18286:end -->

<!-- analysis:DA-20260611-ADMISSION:start -->
### DA-20260611-ADMISSION
Proposal is not authority: typed contract, evidence digest, policy/revocation version and broker identity must all bind before a model proposal mutates production state.
<!-- analysis:DA-20260611-ADMISSION:end -->

<!-- analysis:DA-20260611-AGING:start -->
### DA-20260611-AGING
Serving reliability is time-dependent: host/device/client signals and autocorrelation-aware long campaigns are required before rejuvenation or release decisions.
<!-- analysis:DA-20260611-AGING:end -->

<!-- analysis:DA-20260611-COMPOSITE-SERVING:start -->
### DA-20260611-COMPOSITE-SERVING
Composite multimodal serving requires request walks over a component graph, because fixed stage DAGs cannot express loops, per-request paths, streaming edges and component-level placement together.
<!-- analysis:DA-20260611-COMPOSITE-SERVING:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-11543 | AGENT-REFLECTION | books/part-07-agent/80-reflection.md#L1 | books/part-07-agent/81-workflow.md#L1; books/part-07-agent/84-agent-platform.md#L1 | existing:SF-2026-ARXIV-2606-11543 | delta:SF-2026-ARXIV-2606-11543 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-11543 |
| SF-2026-ARXIV-2606-11632 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/71-multi-tenant.md#L1; books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2606-11632 | delta:SF-2026-ARXIV-2606-11632 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-11632 |
| SF-2026-ARXIV-2606-11671 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/71-multi-tenant.md#L1; books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2606-11671 | delta:SF-2026-ARXIV-2606-11671 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-11671 |
| SF-2026-ARXIV-2606-11686 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-06-ai-infrastructure/67-monitoring.md#L1; books/part-07-agent/81-workflow.md#L1 | existing:SF-2026-ARXIV-2606-11686 | delta:SF-2026-ARXIV-2606-11686 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-11686 |
| SF-2026-ARXIV-2606-11688 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#L1 | books/part-07-agent/80-reflection.md#L1; books/part-07-agent/82-multi-agent.md#L1 | existing:SF-2026-ARXIV-2606-11688 | delta:SF-2026-ARXIV-2606-11688 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-11688 |
| SF-2026-ARXIV-2606-11690 | PLATFORM-COST | books/part-06-ai-infrastructure/70-cost.md#L1 | books/part-05-inference-system/56-inference-scheduling.md#L1; books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2026-ARXIV-2606-11690 | delta:SF-2026-ARXIV-2606-11690 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-11690 |
| SF-2026-ARXIV-2606-11718 | INFER-GPU-MEMORY | books/part-05-inference-system/54-gpu-memory.md#L1 | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L1; books/part-05-inference-system/55-pd-disaggregation.md#L1 | existing:SF-2026-ARXIV-2606-11718 | delta:SF-2026-ARXIV-2606-11718 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-11718 |
| SF-2026-ARXIV-2606-11806 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L1 | books/part-07-agent/75-context.md#L1; books/part-07-agent/76-rag.md#L1 | existing:SF-2026-ARXIV-2606-11806 | delta:SF-2026-ARXIV-2606-11806 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-11806 |
| SF-2026-ARXIV-2606-11871 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/71-multi-tenant.md#L1; books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2606-11871 | delta:SF-2026-ARXIV-2606-11871 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-11871 |
| SF-2026-ARXIV-2606-11878 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/71-multi-tenant.md#L1; books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2606-11878 | delta:SF-2026-ARXIV-2606-11878 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-11878 |
| SF-2026-ARXIV-2606-11916 | PLATFORM-MONITORING | books/part-06-ai-infrastructure/67-monitoring.md#L1 | books/part-06-ai-infrastructure/66-evaluation-system.md#L1; books/part-06-ai-infrastructure/69-trace.md#L1 | existing:SF-2026-ARXIV-2606-11916 | delta:SF-2026-ARXIV-2606-11916 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-11916 |
| SF-2026-ARXIV-2606-11949 | PLATFORM-MONITORING | books/part-06-ai-infrastructure/67-monitoring.md#L1 | books/part-06-ai-infrastructure/66-evaluation-system.md#L1; books/part-06-ai-infrastructure/69-trace.md#L1 | existing:SF-2026-ARXIV-2606-11949 | delta:SF-2026-ARXIV-2606-11949 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-11949 |
| SF-2026-ARXIV-2606-11998 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/71-multi-tenant.md#L1; books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2606-11998 | delta:SF-2026-ARXIV-2606-11998 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-11998 |
| SF-2026-ARXIV-2606-12243 | INFER-SPECULATIVE-DECODING | books/part-05-inference-system/48-speculative-decoding.md#L1 | books/part-05-inference-system/44-decode.md#L1; books/part-04-training-system/31-rlhf.md#L1; books/part-05-inference-system/49-tensorrt-llm.md#L1 | existing:SF-2026-ARXIV-2606-12243 | delta:SF-2026-ARXIV-2606-12243 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-12243 |
| SF-2026-ARXIV-2606-12320 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/71-multi-tenant.md#L1; books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2606-12320 | delta:SF-2026-ARXIV-2606-12320 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-12320 |
| SF-2026-ARXIV-2606-12329 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L1 | books/part-07-agent/75-context.md#L1; books/part-07-agent/76-rag.md#L1 | existing:SF-2026-ARXIV-2606-12329 | delta:SF-2026-ARXIV-2606-12329 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-12329 |
| SF-2026-ARXIV-2606-12370 | INFER-SPECULATIVE-DECODING | books/part-05-inference-system/48-speculative-decoding.md#L1 | books/part-05-inference-system/44-decode.md#L1; books/part-04-training-system/31-rlhf.md#L1; books/part-05-inference-system/49-tensorrt-llm.md#L1 | existing:SF-2026-ARXIV-2606-12370 | delta:SF-2026-ARXIV-2606-12370 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-12370 |
| SF-2026-ARXIV-2606-12385 | TRAIN-DATA | books/part-04-training-system/27-data.md#L1 | books/part-04-training-system/28-pretraining.md#L1; books/part-06-ai-infrastructure/59-model-registry.md#L1 | existing:SF-2026-ARXIV-2606-12385 | delta:SF-2026-ARXIV-2606-12385 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-12385 |
| SF-2026-ARXIV-2606-12487 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#L1 | books/part-05-inference-system/48-speculative-decoding.md#L1; books/part-05-inference-system/50-vllm.md#L1 | existing:SF-2026-ARXIV-2606-12487 | delta:SF-2026-ARXIV-2606-12487 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-12487 |
| SF-2026-ARXIV-2606-12556 | INFER-GPU-MEMORY | books/part-05-inference-system/54-gpu-memory.md#L1 | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L1; books/part-05-inference-system/55-pd-disaggregation.md#L1 | existing:SF-2026-ARXIV-2606-12556 | delta:SF-2026-ARXIV-2606-12556 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-12556 |
| SF-2026-ARXIV-2606-12688 | INFER-KSERVE-TOPOLOGY | books/part-05-inference-system/53-kserve-llm.md#L1 | books/part-05-inference-system/42-what-happens-during-inference.md#L1; books/part-05-inference-system/56-inference-scheduling.md#L1 | existing:SF-2026-ARXIV-2606-12688 | delta:SF-2026-ARXIV-2606-12688 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-12688 |
| SF-2026-ARXIV-2606-12703 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/71-multi-tenant.md#L1; books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2606-12703 | delta:SF-2026-ARXIV-2606-12703 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-12703 |
| SF-2026-ARXIV-2606-12736 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-06-ai-infrastructure/67-monitoring.md#L1; books/part-07-agent/81-workflow.md#L1 | existing:SF-2026-ARXIV-2606-12736 | delta:SF-2026-ARXIV-2606-12736 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-12736 |
| SF-2026-ARXIV-2606-12737 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/71-multi-tenant.md#L1; books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2606-12737 | delta:SF-2026-ARXIV-2606-12737 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-12737 |
| SF-2026-ARXIV-2606-12764 | TRAIN-DATA | books/part-04-training-system/27-data.md#L1 | books/part-04-training-system/28-pretraining.md#L1; books/part-06-ai-infrastructure/59-model-registry.md#L1 | existing:SF-2026-ARXIV-2606-12764 | delta:SF-2026-ARXIV-2606-12764 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-12764 |
| SF-2026-ARXIV-2606-12765 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#L1 | books/part-05-inference-system/48-speculative-decoding.md#L1; books/part-05-inference-system/50-vllm.md#L1 | existing:SF-2026-ARXIV-2606-12765 | delta:SF-2026-ARXIV-2606-12765 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-12765 |
| SF-2026-ARXIV-2606-13708 | INFER-PD-DISAGGREGATION | books/part-05-inference-system/55-pd-disaggregation.md#L1 | books/part-05-inference-system/54-gpu-memory.md#L1; books/part-05-inference-system/56-inference-scheduling.md#L1 | existing:SF-2026-ARXIV-2606-13708 | delta:SF-2026-ARXIV-2606-13708 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-13708 |
| SF-2026-ARXIV-2606-14779 | INFER-GPU-MEMORY | books/part-05-inference-system/54-gpu-memory.md#L1 | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L1; books/part-05-inference-system/55-pd-disaggregation.md#L1 | existing:SF-2026-ARXIV-2606-14779 | delta:SF-2026-ARXIV-2606-14779 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-14779 |
| SF-2026-ARXIV-2606-14783 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/71-multi-tenant.md#L1; books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2606-14783 | delta:SF-2026-ARXIV-2606-14783 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-14783 |
| SF-2026-ARXIV-2606-18284 | TRAIN-DATA | books/part-04-training-system/27-data.md#L1 | books/part-04-training-system/28-pretraining.md#L1; books/part-06-ai-infrastructure/59-model-registry.md#L1 | existing:SF-2026-ARXIV-2606-18284 | delta:SF-2026-ARXIV-2606-18284 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-18284 |
| SF-2026-ARXIV-2606-18286 | TRAIN-SFT | books/part-04-training-system/29-sft.md#L1 | books/part-04-training-system/27-data.md#L1; books/part-04-training-system/31-rlhf.md#L1 | existing:SF-2026-ARXIV-2606-18286 | delta:SF-2026-ARXIV-2606-18286 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-18286 |

<!-- existing:SF-2026-ARXIV-2606-11543:start -->
Owner `AGENT-REFLECTION` and adjacent chapters were read; existing proposition was compared against exact-v1, including coexistence and failure boundaries.
<!-- existing:SF-2026-ARXIV-2606-11543:end -->

<!-- delta:SF-2026-ARXIV-2606-11543:start -->
Skill 的目录组织本身会改变资源读取与有效采用轨迹；Progressive Disclosure 必须以知识等价变体、trajectory evidence 与 verifier outcome 联合评测。
<!-- delta:SF-2026-ARXIV-2606-11543:end -->

<!-- books-review:SF-2026-ARXIV-2606-11543:start -->
Owner `AGENT-REFLECTION`; relation `Direct Evolution`; disposition `Integrate`; adjacent handoff `books/part-07-agent/81-workflow.md; books/part-07-agent/84-agent-platform.md`.
<!-- books-review:SF-2026-ARXIV-2606-11543:end -->

<!-- existing:SF-2026-ARXIV-2606-11632:start -->
Owner `PLATFORM-SECURITY` and adjacent chapters were read; existing proposition was compared against exact-v1, including coexistence and failure boundaries.
<!-- existing:SF-2026-ARXIV-2606-11632:end -->

<!-- delta:SF-2026-ARXIV-2606-11632:start -->
Agent proposal 必须编译为 typed contract，并绑定 evidence digest、policy/revocation epoch 与 scoped broker identity 后才可成为执行 authority。
<!-- delta:SF-2026-ARXIV-2606-11632:end -->

<!-- books-review:SF-2026-ARXIV-2606-11632:start -->
Owner `PLATFORM-SECURITY`; relation `Direct Evolution`; disposition `Integrate`; adjacent handoff `books/part-06-ai-infrastructure/71-multi-tenant.md; books/part-06-ai-infrastructure/73-production-best-practice.md`.
<!-- books-review:SF-2026-ARXIV-2606-11632:end -->

<!-- existing:SF-2026-ARXIV-2606-11671:start -->
Owner `PLATFORM-SECURITY` and adjacent chapters were read; existing proposition was compared against exact-v1, including coexistence and failure boundaries.
<!-- existing:SF-2026-ARXIV-2606-11671:end -->

<!-- delta:SF-2026-ARXIV-2606-11671:start -->
Skill 安全不能只审静态文件；应按 capability profile 构造 targeted runtime context，在 sandbox 中执行并以 trace evidence 标注行为。
<!-- delta:SF-2026-ARXIV-2606-11671:end -->

<!-- books-review:SF-2026-ARXIV-2606-11671:start -->
Owner `PLATFORM-SECURITY`; relation `Direct Evolution`; disposition `Integrate`; adjacent handoff `books/part-06-ai-infrastructure/71-multi-tenant.md; books/part-06-ai-infrastructure/73-production-best-practice.md`.
<!-- books-review:SF-2026-ARXIV-2606-11671:end -->

<!-- existing:SF-2026-ARXIV-2606-11686:start -->
Owner `PLATFORM-EVALUATION-SYSTEM` and adjacent chapters were read; existing proposition was compared against exact-v1, including coexistence and failure boundaries.
<!-- existing:SF-2026-ARXIV-2606-11686:end -->

<!-- delta:SF-2026-ARXIV-2606-11686:start -->
生产 Agent 的 deterministic scaffold 应按 ontology/intent/routing/decomposition/escalation/safety/memory 分层，用 no-LLM regression-locked slices 阻止 aggregate pass rate 掩盖局部回归。
<!-- delta:SF-2026-ARXIV-2606-11686:end -->

<!-- books-review:SF-2026-ARXIV-2606-11686:start -->
Owner `PLATFORM-EVALUATION-SYSTEM`; relation `Direct Evolution`; disposition `Integrate`; adjacent handoff `books/part-06-ai-infrastructure/67-monitoring.md; books/part-07-agent/81-workflow.md`.
<!-- books-review:SF-2026-ARXIV-2606-11686:end -->

<!-- existing:SF-2026-ARXIV-2606-11688:start -->
Owner `AGENT-WORKFLOW` and adjacent chapters were read; existing proposition was compared against exact-v1, including coexistence and failure boundaries.
<!-- existing:SF-2026-ARXIV-2606-11688:end -->

<!-- delta:SF-2026-ARXIV-2606-11688:start -->
长程 Agent 应把 durable FSM、stateless ticks、falsifiable gate 与 terminal hard floor 外置，使未执行/未通过 gate 时最多 honest stall，不能宣告完成。
<!-- delta:SF-2026-ARXIV-2606-11688:end -->

<!-- books-review:SF-2026-ARXIV-2606-11688:start -->
Owner `AGENT-WORKFLOW`; relation `Direct Evolution`; disposition `Integrate`; adjacent handoff `books/part-07-agent/80-reflection.md; books/part-07-agent/82-multi-agent.md`.
<!-- books-review:SF-2026-ARXIV-2606-11688:end -->

<!-- existing:SF-2026-ARXIV-2606-11690:start -->
Owner `PLATFORM-COST` and adjacent chapters were read; existing proposition was compared against exact-v1, including coexistence and failure boundaries.
<!-- existing:SF-2026-ARXIV-2606-11690:end -->

<!-- delta:SF-2026-ARXIV-2606-11690:start -->
LLM 成本必须把 offered load λ 经 Little's Law 映射为 in-flight concurrency 与实际利用率；固定 100% utilization 的每 token 估价会系统性误导低负载自托管。
<!-- delta:SF-2026-ARXIV-2606-11690:end -->

<!-- books-review:SF-2026-ARXIV-2606-11690:start -->
Owner `PLATFORM-COST`; relation `Direct Evolution`; disposition `Integrate`; adjacent handoff `books/part-05-inference-system/56-inference-scheduling.md; books/part-06-ai-infrastructure/67-monitoring.md`.
<!-- books-review:SF-2026-ARXIV-2606-11690:end -->

<!-- existing:SF-2026-ARXIV-2606-11718:start -->
Owner `INFER-GPU-MEMORY` and adjacent chapters were read; existing proposition was compared against exact-v1, including coexistence and failure boundaries.
<!-- existing:SF-2026-ARXIV-2606-11718:end -->

<!-- delta:SF-2026-ARXIV-2606-11718:start -->
Chiplet GPU 的 GEMM locality 需要让 chiplet-local tiles 在 global address space 连续，使 page-granularity placement 与 CTA affinity 一致。
<!-- delta:SF-2026-ARXIV-2606-11718:end -->

<!-- books-review:SF-2026-ARXIV-2606-11718:start -->
Owner `INFER-GPU-MEMORY`; relation `Direct Evolution`; disposition `Integrate`; adjacent handoff `books/part-05-inference-system/45-why-kv-cache-speeds-up.md; books/part-05-inference-system/55-pd-disaggregation.md`.
<!-- books-review:SF-2026-ARXIV-2606-11718:end -->

<!-- existing:SF-2026-ARXIV-2606-11806:start -->
Owner `AGENT-MEMORY` and adjacent chapters were read; existing proposition was compared against exact-v1, including coexistence and failure boundaries.
<!-- existing:SF-2026-ARXIV-2606-11806:end -->

<!-- delta:SF-2026-ARXIV-2606-11806:start -->
生产 experience serving 要按 task cost structure 在 no experience、global injection 与 selective retrieval 间选择，以 quality、prompt cost、latency 与 break-even 联合决策。
<!-- delta:SF-2026-ARXIV-2606-11806:end -->

<!-- books-review:SF-2026-ARXIV-2606-11806:start -->
Owner `AGENT-MEMORY`; relation `Direct Evolution`; disposition `Integrate`; adjacent handoff `books/part-07-agent/75-context.md; books/part-07-agent/76-rag.md`.
<!-- books-review:SF-2026-ARXIV-2606-11806:end -->

<!-- existing:SF-2026-ARXIV-2606-11871:start -->
Owner `PLATFORM-SECURITY` and adjacent chapters were read; existing proposition was compared against exact-v1, including coexistence and failure boundaries.
<!-- existing:SF-2026-ARXIV-2606-11871:end -->

<!-- delta:SF-2026-ARXIV-2606-11871:start -->
CUDA binary security 的 owner 是 executed SASS consumption site；protected-site CFI 必须恢复 site policy、验证 forward/backward transfer 并对 unsupported surface 显式出账。
<!-- delta:SF-2026-ARXIV-2606-11871:end -->

<!-- books-review:SF-2026-ARXIV-2606-11871:start -->
Owner `PLATFORM-SECURITY`; relation `Direct Evolution`; disposition `Integrate`; adjacent handoff `books/part-06-ai-infrastructure/71-multi-tenant.md; books/part-06-ai-infrastructure/73-production-best-practice.md`.
<!-- books-review:SF-2026-ARXIV-2606-11871:end -->

<!-- existing:SF-2026-ARXIV-2606-11878:start -->
Owner `PLATFORM-SECURITY` and adjacent chapters were read; existing proposition was compared against exact-v1, including coexistence and failure boundaries.
<!-- existing:SF-2026-ARXIV-2606-11878:end -->

<!-- delta:SF-2026-ARXIV-2606-11878:start -->
GPU collective 的 mask、predicate、source lane、descriptor 与 epoch 是 authority-bearing non-control data；应在 collective 使用前绑定 membership/contribution/role/time。
<!-- delta:SF-2026-ARXIV-2606-11878:end -->

<!-- books-review:SF-2026-ARXIV-2606-11878:start -->
Owner `PLATFORM-SECURITY`; relation `Direct Evolution`; disposition `Integrate`; adjacent handoff `books/part-06-ai-infrastructure/71-multi-tenant.md; books/part-06-ai-infrastructure/73-production-best-practice.md`.
<!-- books-review:SF-2026-ARXIV-2606-11878:end -->

<!-- existing:SF-2026-ARXIV-2606-11916:start -->
Owner `PLATFORM-MONITORING` and adjacent chapters were read; existing proposition was compared against exact-v1, including coexistence and failure boundaries.
<!-- existing:SF-2026-ARXIV-2606-11916:end -->

<!-- delta:SF-2026-ARXIV-2606-11916:start -->
LLM serving release 不能只测分钟级峰值；应在 host/device/client 三面进行长时 aging campaign，并用 autocorrelation-aware statistics 区分 leak、runtime 与 workload regime。
<!-- delta:SF-2026-ARXIV-2606-11916:end -->

<!-- books-review:SF-2026-ARXIV-2606-11916:start -->
Owner `PLATFORM-MONITORING`; relation `Direct Evolution`; disposition `Integrate`; adjacent handoff `books/part-06-ai-infrastructure/66-evaluation-system.md; books/part-06-ai-infrastructure/69-trace.md`.
<!-- books-review:SF-2026-ARXIV-2606-11916:end -->

<!-- existing:SF-2026-ARXIV-2606-11949:start -->
Owner `PLATFORM-MONITORING` and adjacent chapters were read; existing proposition was compared against exact-v1, including coexistence and failure boundaries.
<!-- existing:SF-2026-ARXIV-2606-11949:end -->

<!-- delta:SF-2026-ARXIV-2606-11949:start -->
deployed safety classifier 需要 reference-window calibration、sequential alarm、multiplicity control 与 alarm-triggered conformal abstention；shift sensor 与安全 authority 分离。
<!-- delta:SF-2026-ARXIV-2606-11949:end -->

<!-- books-review:SF-2026-ARXIV-2606-11949:start -->
Owner `PLATFORM-MONITORING`; relation `Direct Evolution`; disposition `Integrate`; adjacent handoff `books/part-06-ai-infrastructure/66-evaluation-system.md; books/part-06-ai-infrastructure/69-trace.md`.
<!-- books-review:SF-2026-ARXIV-2606-11949:end -->

<!-- existing:SF-2026-ARXIV-2606-11998:start -->
Owner `PLATFORM-SECURITY` and adjacent chapters were read; existing proposition was compared against exact-v1, including coexistence and failure boundaries.
<!-- existing:SF-2026-ARXIV-2606-11998:end -->

<!-- delta:SF-2026-ARXIV-2606-11998:start -->
trusted monitor 能力落后时，可用更强 untrusted monitor 评估 action，再让 weaker trusted model 监督其透明推理；control graph 要显式保存 collusion threat model。
<!-- delta:SF-2026-ARXIV-2606-11998:end -->

<!-- books-review:SF-2026-ARXIV-2606-11998:start -->
Owner `PLATFORM-SECURITY`; relation `Direct Evolution`; disposition `Integrate`; adjacent handoff `books/part-06-ai-infrastructure/71-multi-tenant.md; books/part-06-ai-infrastructure/73-production-best-practice.md`.
<!-- books-review:SF-2026-ARXIV-2606-11998:end -->

<!-- existing:SF-2026-ARXIV-2606-12243:start -->
Owner `INFER-SPECULATIVE-DECODING` and adjacent chapters were read; existing proposition was compared against exact-v1, including coexistence and failure boundaries.
<!-- existing:SF-2026-ARXIV-2606-12243:end -->

<!-- delta:SF-2026-ARXIV-2606-12243:start -->
把 draft verification 从二元 accept/full-recompute 演进为 direct/slim/full 三层，并用 intra-model routing 选择 verifier 资源。
<!-- delta:SF-2026-ARXIV-2606-12243:end -->

<!-- books-review:SF-2026-ARXIV-2606-12243:start -->
Owner `INFER-SPECULATIVE-DECODING`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`; adjacent handoff `books/part-05-inference-system/44-decode.md; books/part-04-training-system/31-rlhf.md; books/part-05-inference-system/49-tensorrt-llm.md`.
<!-- books-review:SF-2026-ARXIV-2606-12243:end -->

<!-- existing:SF-2026-ARXIV-2606-12320:start -->
Owner `PLATFORM-SECURITY` and adjacent chapters were read; existing proposition was compared against exact-v1, including coexistence and failure boundaries.
<!-- existing:SF-2026-ARXIV-2606-12320:end -->

<!-- delta:SF-2026-ARXIV-2606-12320:start -->
生产 Agent governance 应分 reasoning/network/identity/endpoint/data 五平面，并把 stop-anywhere mediation、capability attenuation、TTL 与 structured audit 组合为 cross-plane control。
<!-- delta:SF-2026-ARXIV-2606-12320:end -->

<!-- books-review:SF-2026-ARXIV-2606-12320:start -->
Owner `PLATFORM-SECURITY`; relation `Direct Evolution`; disposition `Integrate`; adjacent handoff `books/part-06-ai-infrastructure/71-multi-tenant.md; books/part-06-ai-infrastructure/73-production-best-practice.md`.
<!-- books-review:SF-2026-ARXIV-2606-12320:end -->

<!-- existing:SF-2026-ARXIV-2606-12329:start -->
Owner `AGENT-MEMORY` and adjacent chapters were read; existing proposition was compared against exact-v1, including coexistence and failure boundaries.
<!-- existing:SF-2026-ARXIV-2606-12329:end -->

<!-- delta:SF-2026-ARXIV-2606-12329:start -->
Coding-agent memory 可用 append-only typed event log 作 authoritative state，并确定性投影摘要；pre-action gate 只消费既有 failure/fragility evidence。
<!-- delta:SF-2026-ARXIV-2606-12329:end -->

<!-- books-review:SF-2026-ARXIV-2606-12329:start -->
Owner `AGENT-MEMORY`; relation `Direct Evolution`; disposition `Integrate`; adjacent handoff `books/part-07-agent/75-context.md; books/part-07-agent/76-rag.md`.
<!-- books-review:SF-2026-ARXIV-2606-12329:end -->

<!-- existing:SF-2026-ARXIV-2606-12370:start -->
Owner `INFER-SPECULATIVE-DECODING` and adjacent chapters were read; existing proposition was compared against exact-v1, including coexistence and failure boundaries.
<!-- existing:SF-2026-ARXIV-2606-12370:end -->

<!-- delta:SF-2026-ARXIV-2606-12370:start -->
RL rollout acceleration 中 MTP acceptance 受 policy entropy 与 draft mismatch 联合约束；rejection sampling 与 TV objective 比 target-only 接受对 policy update 更平滑。
<!-- delta:SF-2026-ARXIV-2606-12370:end -->

<!-- books-review:SF-2026-ARXIV-2606-12370:start -->
Owner `INFER-SPECULATIVE-DECODING`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`; adjacent handoff `books/part-05-inference-system/44-decode.md; books/part-04-training-system/31-rlhf.md; books/part-05-inference-system/49-tensorrt-llm.md`.
<!-- books-review:SF-2026-ARXIV-2606-12370:end -->

<!-- existing:SF-2026-ARXIV-2606-12385:start -->
Owner `TRAIN-DATA` and adjacent chapters were read; existing proposition was compared against exact-v1, including coexistence and failure boundaries.
<!-- existing:SF-2026-ARXIV-2606-12385:end -->

<!-- delta:SF-2026-ARXIV-2606-12385:start -->
模型卡不足以表达递归 training dependencies；provenance 应以 artifact identity 和 operation-centered edges 递归解析生成、过滤、judge 与 selection 关系。
<!-- delta:SF-2026-ARXIV-2606-12385:end -->

<!-- books-review:SF-2026-ARXIV-2606-12385:start -->
Owner `TRAIN-DATA`; relation `Direct Evolution`; disposition `Integrate`; adjacent handoff `books/part-04-training-system/28-pretraining.md; books/part-06-ai-infrastructure/59-model-registry.md`.
<!-- books-review:SF-2026-ARXIV-2606-12385:end -->

<!-- existing:SF-2026-ARXIV-2606-12487:start -->
Owner `INFER-TENSORRT-LLM` and adjacent chapters were read; existing proposition was compared against exact-v1, including coexistence and failure boundaries.
<!-- existing:SF-2026-ARXIV-2606-12487:end -->

<!-- delta:SF-2026-ARXIV-2606-12487:start -->
4-bit activation/KV PTQ 需要观察 residual stream 的 phase-wise jump，并对关键相位采用 mixed precision，而非只做静态 rotation smoothing。
<!-- delta:SF-2026-ARXIV-2606-12487:end -->

<!-- books-review:SF-2026-ARXIV-2606-12487:start -->
Owner `INFER-TENSORRT-LLM`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`; adjacent handoff `books/part-05-inference-system/48-speculative-decoding.md; books/part-05-inference-system/50-vllm.md`.
<!-- books-review:SF-2026-ARXIV-2606-12487:end -->

<!-- existing:SF-2026-ARXIV-2606-12556:start -->
Owner `INFER-GPU-MEMORY` and adjacent chapters were read; existing proposition was compared against exact-v1, including coexistence and failure boundaries.
<!-- existing:SF-2026-ARXIV-2606-12556:end -->

<!-- delta:SF-2026-ARXIV-2606-12556:start -->
长 context state 可跨 GPU/host/CXL-hybrid/NVMe 构成 byte-addressable tier，并利用 model-weight/prefix access 可预测性做 multi-tier DMA prefetch。
<!-- delta:SF-2026-ARXIV-2606-12556:end -->

<!-- books-review:SF-2026-ARXIV-2606-12556:start -->
Owner `INFER-GPU-MEMORY`; relation `Direct Evolution`; disposition `Integrate`; adjacent handoff `books/part-05-inference-system/45-why-kv-cache-speeds-up.md; books/part-05-inference-system/55-pd-disaggregation.md`.
<!-- books-review:SF-2026-ARXIV-2606-12556:end -->

<!-- existing:SF-2026-ARXIV-2606-12688:start -->
Owner `INFER-KSERVE-TOPOLOGY` and adjacent chapters were read; existing proposition was compared against exact-v1, including coexistence and failure boundaries.
<!-- existing:SF-2026-ARXIV-2606-12688:end -->

<!-- delta:SF-2026-ARXIV-2606-12688:start -->
复合多模态模型的 serving contract 应从固定 stage DAG 演进为 model graph + named walks，显式支持 seq/parallel/loop/dynamic-loop/stream 与 component placement。
<!-- delta:SF-2026-ARXIV-2606-12688:end -->

<!-- books-review:SF-2026-ARXIV-2606-12688:start -->
Owner `INFER-KSERVE-TOPOLOGY`; relation `Direct Evolution`; disposition `Integrate`; adjacent handoff `books/part-05-inference-system/42-what-happens-during-inference.md; books/part-05-inference-system/56-inference-scheduling.md`.
<!-- books-review:SF-2026-ARXIV-2606-12688:end -->

<!-- existing:SF-2026-ARXIV-2606-12703:start -->
Owner `PLATFORM-SECURITY` and adjacent chapters were read; existing proposition was compared against exact-v1, including coexistence and failure boundaries.
<!-- existing:SF-2026-ARXIV-2606-12703:end -->

<!-- delta:SF-2026-ARXIV-2606-12703:start -->
Persistent memory poisoning 的 certified boundary 必须在 write-time 做 cryptographic provenance，并在 query-time 对 authenticated adversary 做 randomized ablation 与 verdict aggregation。
<!-- delta:SF-2026-ARXIV-2606-12703:end -->

<!-- books-review:SF-2026-ARXIV-2606-12703:start -->
Owner `PLATFORM-SECURITY`; relation `Direct Evolution`; disposition `Integrate`; adjacent handoff `books/part-06-ai-infrastructure/71-multi-tenant.md; books/part-06-ai-infrastructure/73-production-best-practice.md`.
<!-- books-review:SF-2026-ARXIV-2606-12703:end -->

<!-- existing:SF-2026-ARXIV-2606-12736:start -->
Owner `PLATFORM-EVALUATION-SYSTEM` and adjacent chapters were read; existing proposition was compared against exact-v1, including coexistence and failure boundaries.
<!-- existing:SF-2026-ARXIV-2606-12736:end -->

<!-- delta:SF-2026-ARXIV-2606-12736:start -->
Scientific agent evaluation 需要 interactive environment、stepwise verification、domain slices 与 open-ended failure taxonomy，不能把 research 压成静态最终答案。
<!-- delta:SF-2026-ARXIV-2606-12736:end -->

<!-- books-review:SF-2026-ARXIV-2606-12736:start -->
Owner `PLATFORM-EVALUATION-SYSTEM`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`; adjacent handoff `books/part-06-ai-infrastructure/67-monitoring.md; books/part-07-agent/81-workflow.md`.
<!-- books-review:SF-2026-ARXIV-2606-12736:end -->

<!-- existing:SF-2026-ARXIV-2606-12737:start -->
Owner `PLATFORM-SECURITY` and adjacent chapters were read; existing proposition was compared against exact-v1, including coexistence and failure boundaries.
<!-- existing:SF-2026-ARXIV-2606-12737:end -->

<!-- delta:SF-2026-ARXIV-2606-12737:start -->
Prompt-injection red team 应从 attack-success search 扩为 source-aware test construction、feedback evolution、verification 与 localization，输出可修复 attack surface。
<!-- delta:SF-2026-ARXIV-2606-12737:end -->

<!-- books-review:SF-2026-ARXIV-2606-12737:start -->
Owner `PLATFORM-SECURITY`; relation `Direct Evolution`; disposition `Integrate`; adjacent handoff `books/part-06-ai-infrastructure/71-multi-tenant.md; books/part-06-ai-infrastructure/73-production-best-practice.md`.
<!-- books-review:SF-2026-ARXIV-2606-12737:end -->

<!-- existing:SF-2026-ARXIV-2606-12764:start -->
Owner `TRAIN-DATA` and adjacent chapters were read; existing proposition was compared against exact-v1, including coexistence and failure boundaries.
<!-- existing:SF-2026-ARXIV-2606-12764:end -->

<!-- delta:SF-2026-ARXIV-2606-12764:start -->
Code training-data audit 必须检测 functional equivalence，而不能只依赖文本 overlap；应以 exposed target 对未 exposed reference 做 counterfactual execution comparison。
<!-- delta:SF-2026-ARXIV-2606-12764:end -->

<!-- books-review:SF-2026-ARXIV-2606-12764:start -->
Owner `TRAIN-DATA`; relation `Direct Evolution`; disposition `Integrate`; adjacent handoff `books/part-04-training-system/28-pretraining.md; books/part-06-ai-infrastructure/59-model-registry.md`.
<!-- books-review:SF-2026-ARXIV-2606-12764:end -->

<!-- existing:SF-2026-ARXIV-2606-12765:start -->
Owner `INFER-TENSORRT-LLM` and adjacent chapters were read; existing proposition was compared against exact-v1, including coexistence and failure boundaries.
<!-- existing:SF-2026-ARXIV-2606-12765:end -->

<!-- delta:SF-2026-ARXIV-2606-12765:start -->
Low-precision backend contract 必须通过 checksum/provenance microbench 分离 interface support、真正加速、accumulator width、execution rail 与 fragment layout。
<!-- delta:SF-2026-ARXIV-2606-12765:end -->

<!-- books-review:SF-2026-ARXIV-2606-12765:start -->
Owner `INFER-TENSORRT-LLM`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`; adjacent handoff `books/part-05-inference-system/48-speculative-decoding.md; books/part-05-inference-system/50-vllm.md`.
<!-- books-review:SF-2026-ARXIV-2606-12765:end -->

<!-- existing:SF-2026-ARXIV-2606-13708:start -->
Owner `INFER-PD-DISAGGREGATION` and adjacent chapters were read; existing proposition was compared against exact-v1, including coexistence and failure boundaries.
<!-- existing:SF-2026-ARXIV-2606-13708:end -->

<!-- delta:SF-2026-ARXIV-2606-13708:start -->
Remote-memory indirection 可用 memory-side NIC 上预注册、静态可验证的 compact ISA 执行，把依赖链从多 RTT 收敛为一次 request。
<!-- delta:SF-2026-ARXIV-2606-13708:end -->

<!-- books-review:SF-2026-ARXIV-2606-13708:start -->
Owner `INFER-PD-DISAGGREGATION`; relation `Direct Evolution`; disposition `Integrate`; adjacent handoff `books/part-05-inference-system/54-gpu-memory.md; books/part-05-inference-system/56-inference-scheduling.md`.
<!-- books-review:SF-2026-ARXIV-2606-13708:end -->

<!-- existing:SF-2026-ARXIV-2606-14779:start -->
Owner `INFER-GPU-MEMORY` and adjacent chapters were read; existing proposition was compared against exact-v1, including coexistence and failure boundaries.
<!-- existing:SF-2026-ARXIV-2606-14779:end -->

<!-- delta:SF-2026-ARXIV-2606-14779:start -->
KV offload 不应串行穿过单 host/SSD；应把多 DRAM/SSD 汇成 bandwidth-weighted pool，并以 user-space SPDK bypass filesystem。
<!-- delta:SF-2026-ARXIV-2606-14779:end -->

<!-- books-review:SF-2026-ARXIV-2606-14779:start -->
Owner `INFER-GPU-MEMORY`; relation `Direct Evolution`; disposition `Integrate`; adjacent handoff `books/part-05-inference-system/45-why-kv-cache-speeds-up.md; books/part-05-inference-system/55-pd-disaggregation.md`.
<!-- books-review:SF-2026-ARXIV-2606-14779:end -->

<!-- existing:SF-2026-ARXIV-2606-14783:start -->
Owner `PLATFORM-SECURITY` and adjacent chapters were read; existing proposition was compared against exact-v1, including coexistence and failure boundaries.
<!-- existing:SF-2026-ARXIV-2606-14783:end -->

<!-- delta:SF-2026-ARXIV-2606-14783:start -->
Encoder-free VLM 的 visual tokens 与 layer-0 KV 可能成为 output filter 之前的可逆 privacy side channel；architecture 与 cache access 必须进入 threat model。
<!-- delta:SF-2026-ARXIV-2606-14783:end -->

<!-- books-review:SF-2026-ARXIV-2606-14783:start -->
Owner `PLATFORM-SECURITY`; relation `Direct Evolution`; disposition `Integrate`; adjacent handoff `books/part-06-ai-infrastructure/71-multi-tenant.md; books/part-06-ai-infrastructure/73-production-best-practice.md`.
<!-- books-review:SF-2026-ARXIV-2606-14783:end -->

<!-- existing:SF-2026-ARXIV-2606-18284:start -->
Owner `TRAIN-DATA` and adjacent chapters were read; existing proposition was compared against exact-v1, including coexistence and failure boundaries.
<!-- existing:SF-2026-ARXIV-2606-18284:end -->

<!-- delta:SF-2026-ARXIV-2606-18284:start -->
训练 task generator 时可用一次 solver-labeled pool 训练 activation probe，把 targeted solve-rate 作为 amortized reward；最终仍由 held-out solver 验证。
<!-- delta:SF-2026-ARXIV-2606-18284:end -->

<!-- books-review:SF-2026-ARXIV-2606-18284:start -->
Owner `TRAIN-DATA`; relation `Direct Evolution`; disposition `Integrate`; adjacent handoff `books/part-04-training-system/28-pretraining.md; books/part-06-ai-infrastructure/59-model-registry.md`.
<!-- books-review:SF-2026-ARXIV-2606-18284:end -->

<!-- existing:SF-2026-ARXIV-2606-18286:start -->
Owner `TRAIN-SFT` and adjacent chapters were read; existing proposition was compared against exact-v1, including coexistence and failure boundaries.
<!-- existing:SF-2026-ARXIV-2606-18286:end -->

<!-- delta:SF-2026-ARXIV-2606-18286:start -->
Code SFT 的 sparse supervision unit 应是 syntax-complete、data-flow-connected code block，而非孤立 high-loss token；完整 response 继续作 context。
<!-- delta:SF-2026-ARXIV-2606-18286:end -->

<!-- books-review:SF-2026-ARXIV-2606-18286:start -->
Owner `TRAIN-SFT`; relation `Direct Evolution`; disposition `Integrate`; adjacent handoff `books/part-04-training-system/27-data.md; books/part-04-training-system/31-rlhf.md`.
<!-- books-review:SF-2026-ARXIV-2606-18286:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260611-COVERAGE-V1 | fresh-context:jun11-v1 | coverage | coverage:SRC-ARXIV:20260611 | — | 559/559 full semantic screen; denominator 31/559; closures 528 | passed |
| SA-20260611-EVIDENCE-V1 | fresh-context:jun11-v1 | evidence | review:SF-2026-ARXIV-2606-11543; review:SF-2026-ARXIV-2606-11632; review:SF-2026-ARXIV-2606-11671; review:SF-2026-ARXIV-2606-11686; review:SF-2026-ARXIV-2606-11688; review:SF-2026-ARXIV-2606-11690; review:SF-2026-ARXIV-2606-11718; review:SF-2026-ARXIV-2606-11806; review:SF-2026-ARXIV-2606-11871; review:SF-2026-ARXIV-2606-11878; review:SF-2026-ARXIV-2606-11916; review:SF-2026-ARXIV-2606-11949; review:SF-2026-ARXIV-2606-11998; review:SF-2026-ARXIV-2606-12243; review:SF-2026-ARXIV-2606-12320; review:SF-2026-ARXIV-2606-12329; review:SF-2026-ARXIV-2606-12370; review:SF-2026-ARXIV-2606-12385; review:SF-2026-ARXIV-2606-12487; review:SF-2026-ARXIV-2606-12556; review:SF-2026-ARXIV-2606-12688; review:SF-2026-ARXIV-2606-12703; review:SF-2026-ARXIV-2606-12736; review:SF-2026-ARXIV-2606-12737; review:SF-2026-ARXIV-2606-12764; review:SF-2026-ARXIV-2606-12765; review:SF-2026-ARXIV-2606-13708; review:SF-2026-ARXIV-2606-14779; review:SF-2026-ARXIV-2606-14783; review:SF-2026-ARXIV-2606-18284; review:SF-2026-ARXIV-2606-18286 | — | 31/31 exact-v1 method/evaluation/limitations and benchmark contracts | passed |
| SA-20260611-SELECTION-V1 | fresh-context:jun11-v1 | deep_analysis_selection | analysis-decision:SF-2026-ARXIV-2606-11543; analysis:DA-20260611-ADMISSION; analysis-decision:SF-2026-ARXIV-2606-11671; analysis-decision:SF-2026-ARXIV-2606-11686; analysis-decision:SF-2026-ARXIV-2606-11688; analysis-decision:SF-2026-ARXIV-2606-11690; analysis-decision:SF-2026-ARXIV-2606-11718; analysis-decision:SF-2026-ARXIV-2606-11806; analysis-decision:SF-2026-ARXIV-2606-11871; analysis-decision:SF-2026-ARXIV-2606-11878; analysis:DA-20260611-AGING; analysis-decision:SF-2026-ARXIV-2606-11949; analysis-decision:SF-2026-ARXIV-2606-11998; analysis-decision:SF-2026-ARXIV-2606-12243; analysis-decision:SF-2026-ARXIV-2606-12320; analysis-decision:SF-2026-ARXIV-2606-12329; analysis-decision:SF-2026-ARXIV-2606-12370; analysis-decision:SF-2026-ARXIV-2606-12385; analysis-decision:SF-2026-ARXIV-2606-12487; analysis-decision:SF-2026-ARXIV-2606-12556; analysis:DA-20260611-COMPOSITE-SERVING; analysis-decision:SF-2026-ARXIV-2606-12703; analysis-decision:SF-2026-ARXIV-2606-12736; analysis-decision:SF-2026-ARXIV-2606-12737; analysis-decision:SF-2026-ARXIV-2606-12764; analysis-decision:SF-2026-ARXIV-2606-12765; analysis-decision:SF-2026-ARXIV-2606-13708; analysis-decision:SF-2026-ARXIV-2606-14779; analysis-decision:SF-2026-ARXIV-2606-14783; analysis-decision:SF-2026-ARXIV-2606-18284; analysis-decision:SF-2026-ARXIV-2606-18286 | — | 31/31 frontier; three selected | passed |
| SA-20260611-BOOKS-POSTWRITE-V1 | fresh-context:jun11-postwrite-v1 | books | books-review:SF-2026-ARXIV-2606-11543; books-review:SF-2026-ARXIV-2606-11632; books-review:SF-2026-ARXIV-2606-11671; books-review:SF-2026-ARXIV-2606-11686; books-review:SF-2026-ARXIV-2606-11688; books-review:SF-2026-ARXIV-2606-11690; books-review:SF-2026-ARXIV-2606-11718; books-review:SF-2026-ARXIV-2606-11806; books-review:SF-2026-ARXIV-2606-11871; books-review:SF-2026-ARXIV-2606-11878; books-review:SF-2026-ARXIV-2606-11916; books-review:SF-2026-ARXIV-2606-11949; books-review:SF-2026-ARXIV-2606-11998; books-review:SF-2026-ARXIV-2606-12243; books-review:SF-2026-ARXIV-2606-12320; books-review:SF-2026-ARXIV-2606-12329; books-review:SF-2026-ARXIV-2606-12370; books-review:SF-2026-ARXIV-2606-12385; books-review:SF-2026-ARXIV-2606-12487; books-review:SF-2026-ARXIV-2606-12556; books-review:SF-2026-ARXIV-2606-12688; books-review:SF-2026-ARXIV-2606-12703; books-review:SF-2026-ARXIV-2606-12736; books-review:SF-2026-ARXIV-2606-12737; books-review:SF-2026-ARXIV-2606-12764; books-review:SF-2026-ARXIV-2606-12765; books-review:SF-2026-ARXIV-2606-13708; books-review:SF-2026-ARXIV-2606-14779; books-review:SF-2026-ARXIV-2606-14783; books-review:SF-2026-ARXIV-2606-18284; books-review:SF-2026-ARXIV-2606-18286 | — | resolved F-0611-OWNER-12370 to INFER-SPECULATIVE-DECODING with TRAIN-RLHF adjacent; 26/26 writebacks, 5/5 No Change and 31/31 owner/adjacent handoffs passed; `papers/2026/06/_sources/daily-20260611/POST_WRITE_FRESH_AUDIT_V1.md` | passed |

### Materials and Access

- DataCite snapshots are frozen discovery/identity/abstract evidence only.
- Primary manuscript evidence is the official `https://arxiv.org/html/<id>v1` path.
- Direct shell transfer reset; official HTML was reviewed through the working web path.

## 8. Ignored Noise

- 528 identities were closed before the denominator with family-specific semantic reasons in `denominator-full-semantic-audit-v1.tsv`; they remain preserved for recall audit instead of being promoted into the Candidate Ledger.

## 9. Recommended Action

- `Integrate`: 26 families were merged by root into 12 unique ROADMAP owners; each exact-v1 family ID occurs once in its target Books file.
- `No Change — Existing Coverage`: 5 families remain Daily evidence only because the durable mechanism and fallback boundary already exist in the owner or explicit adjacent chapter.
- Finding `F-0611-OWNER-12370` was confined to Daily routing: MTP acceptance/TV/rejection correctness belongs to `INFER-SPECULATIVE-DECODING`; `TRAIN-RLHF` consumes rollout throughput and policy-update consequences as an adjacent handoff.

## 10. Repository Changes

- Root performed the serialized Books writeback across the 12 files listed in `BOOKS_INTEGRATION_QUEUE_V1.md`.
- This lane updated the 2026-06-11 Daily, source receipts, finalizer and post-write audit only; it did not stage, commit, push or modify Books.

## 11. Open Questions

- How should runtime-skill probes, policy epochs and certificate revocation be recalibrated when evidence or threat distributions drift?
- Which aging signals can safely trigger rejuvenation without turning a deployment-specific campaign into a universal threshold?
- How should graph-serving placement, tiered memory and PD handoff share backpressure and failure semantics under mixed workloads?
- How should event-sourced experience and persistent-memory certificates expire or supersede incorrect historical judgments?
- These are research continuations, not unresolved Gate findings.

## 12. Sources

- [arXiv:2606.11543v1 — SkillJuror: Measuring How Agent Skill Organization Changes Runtime Behavior](https://arxiv.org/html/2606.11543v1) — first-public `2026-06-10`；accessed `2026-08-29`；Source Family `SF-2026-ARXIV-2606-11543`。
- [arXiv:2606.11632v1 — Sovereign Assurance Boundary: Certificate-Bound Admission for Agentic Infrastructure](https://arxiv.org/html/2606.11632v1) — first-public `2026-06-10`；accessed `2026-08-29`；Source Family `SF-2026-ARXIV-2606-11632`。
- [arXiv:2606.11671v1 — Runtime Skill Audit: Targeted Runtime Probing for Agent Skill Security](https://arxiv.org/html/2606.11671v1) — first-public `2026-06-10`；accessed `2026-08-29`；Source Family `SF-2026-ARXIV-2606-11671`。
- [arXiv:2606.11686v1 — Layer-Isolated Evaluation: Gating the Deterministic Scaffold of a Production LLM Agent with a No-LLM, Regression-Locked Test Harness](https://arxiv.org/html/2606.11686v1) — first-public `2026-06-10`；accessed `2026-08-29`；Source Family `SF-2026-ARXIV-2606-11686`。
- [arXiv:2606.11688v1 — Goal-Autopilot: A Verifiable Anti-Fabrication Firewall for Unattended Long-Horizon Agents](https://arxiv.org/html/2606.11688v1) — first-public `2026-06-10`；accessed `2026-08-29`；Source Family `SF-2026-ARXIV-2606-11688`。
- [arXiv:2606.11690v1 — Beyond Per-Token Pricing: A Concurrency-Aware Methodology for LLM Infrastructure Cost Estimation](https://arxiv.org/html/2606.11690v1) — first-public `2026-06-10`；accessed `2026-08-29`；Source Family `SF-2026-ARXIV-2606-11690`。
- [arXiv:2606.11718v1 — Making Locality-aware GEMM Compatible with Page-Granularity Placement on Chiplet GPUs](https://arxiv.org/html/2606.11718v1) — first-public `2026-06-10`；accessed `2026-08-29`；Source Family `SF-2026-ARXIV-2606-11718`。
- [arXiv:2606.11806v1 — External Experience Serving in Production LLM Systems: A Deployment-Oriented Study of Quality-Cost Trade-offs](https://arxiv.org/html/2606.11806v1) — first-public `2026-06-10`；accessed `2026-08-29`；Source Family `SF-2026-ARXIV-2606-11806`。
- [arXiv:2606.11871v1 — WarpGuard: Protected-Site Control-Flow Integrity for CUDA SASS Binaries](https://arxiv.org/html/2606.11871v1) — first-public `2026-06-10`；accessed `2026-08-29`；Source Family `SF-2026-ARXIV-2606-11871`。
- [arXiv:2606.11878v1 — Gerrymandering the Warp: Non-Control-Data Attacks on CUDA Collective Decisions](https://arxiv.org/html/2606.11878v1) — first-public `2026-06-10`；accessed `2026-08-29`；Source Family `SF-2026-ARXIV-2606-11878`。
- [arXiv:2606.11916v1 — Characterizing Software Aging in GPU-Based LLM Serving Systems](https://arxiv.org/html/2606.11916v1) — first-public `2026-06-10`；accessed `2026-08-29`；Source Family `SF-2026-ARXIV-2606-11916`。
- [arXiv:2606.11949v1 — Online Shift Detection and Conformal Adaptation for Deployed Safety Classifiers](https://arxiv.org/html/2606.11949v1) — first-public `2026-06-10`；accessed `2026-08-29`；Source Family `SF-2026-ARXIV-2606-11949`。
- [arXiv:2606.11998v1 — Bootstrapped Monitoring: Leveraging Transparent Reasoning to Oversee Stronger AI Agents](https://arxiv.org/html/2606.11998v1) — first-public `2026-06-10`；accessed `2026-08-29`；Source Family `SF-2026-ARXIV-2606-11998`。
- [arXiv:2606.12243v1 — VIA-SD: Verification via Intra-Model Routing for Speculative Decoding](https://arxiv.org/html/2606.12243v1) — first-public `2026-06-10`；accessed `2026-08-29`；Source Family `SF-2026-ARXIV-2606-12243`。
- [arXiv:2606.12320v1 — A Five-Plane Reference Architecture for Runtime Governance of Production AI Agents](https://arxiv.org/html/2606.12320v1) — first-public `2026-06-10`；accessed `2026-08-29`；Source Family `SF-2026-ARXIV-2606-12320`。
- [arXiv:2606.12329v1 — PROJECTMEM: A Local-First, Event-Sourced Memory and Judgment Layer for AI Coding Agents](https://arxiv.org/html/2606.12329v1) — first-public `2026-06-10`；accessed `2026-08-29`；Source Family `SF-2026-ARXIV-2606-12329`。
- [arXiv:2606.12370v1 — Breaking Entropy Bounds: Accelerating RL Training via MTP with Rejection Sampling](https://arxiv.org/html/2606.12370v1) — first-public `2026-06-10`；accessed `2026-08-29`；Source Family `SF-2026-ARXIV-2606-12370`。
- [arXiv:2606.12385v1 — Which Models Are Our Models Built On? Auditing Invisible Dependencies in Modern LLMs](https://arxiv.org/html/2606.12385v1) — first-public `2026-06-10`；accessed `2026-08-29`；Source Family `SF-2026-ARXIV-2606-12385`。
- [arXiv:2606.12487v1 — DynamicPTQ: Mitigating Activation Quantization Collapse via Residual-Stream Dynamics](https://arxiv.org/html/2606.12487v1) — first-public `2026-06-10`；accessed `2026-08-29`；Source Family `SF-2026-ARXIV-2606-12487`。
- [arXiv:2606.12556v1 — ITME: Inference Tiered Memory Expansion with Disaggregated CXL-Hybrid Memories](https://arxiv.org/html/2606.12556v1) — first-public `2026-06-10`；accessed `2026-08-29`；Source Family `SF-2026-ARXIV-2606-12556`。
- [arXiv:2606.12688v1 — M*: A Modular, Extensible, Serving System for Multimodal Models](https://arxiv.org/html/2606.12688v1) — first-public `2026-06-10`；accessed `2026-08-29`；Source Family `SF-2026-ARXIV-2606-12688`。
- [arXiv:2606.12703v1 — SMSR: Certified Defence Against Runtime Memory Poisoning in Persistent LLM Agent Systems](https://arxiv.org/html/2606.12703v1) — first-public `2026-06-10`；accessed `2026-08-29`；Source Family `SF-2026-ARXIV-2606-12703`。
- [arXiv:2606.12736v1 — Benchmarking AI Agents for Addressing Scientific Challenges Across Scales](https://arxiv.org/html/2606.12736v1) — first-public `2026-06-10`；accessed `2026-08-29`；Source Family `SF-2026-ARXIV-2606-12736`。
- [arXiv:2606.12737v1 — PI-Hunter: Automated Red-Teaming for Exposing and Localizing Prompt Injections](https://arxiv.org/html/2606.12737v1) — first-public `2026-06-10`；accessed `2026-08-29`；Source Family `SF-2026-ARXIV-2606-12737`。
- [arXiv:2606.12764v1 — Detecting Functional Memorization in Code Language Models](https://arxiv.org/html/2606.12764v1) — first-public `2026-06-11`；accessed `2026-08-29`；Source Family `SF-2026-ARXIV-2606-12764`。
- [arXiv:2606.12765v1 — Rigel: Reverse-Engineering the Metal 4.1 Tensor Compute Path on the Apple M4 Max GPU](https://arxiv.org/html/2606.12765v1) — first-public `2026-06-11`；accessed `2026-08-29`；Source Family `SF-2026-ARXIV-2606-12765`。
- [arXiv:2606.13708v1 — Tiara: A Programmable Line-Rate ISA for Remote Memory Access](https://arxiv.org/html/2606.13708v1) — first-public `2026-06-10`；accessed `2026-08-29`；Source Family `SF-2026-ARXIV-2606-13708`。
- [arXiv:2606.14779v1 — Unified KV Pooling to Accelerate Long-Context LLM Serving](https://arxiv.org/html/2606.14779v1) — first-public `2026-06-10`；accessed `2026-08-29`；Source Family `SF-2026-ARXIV-2606-14779`。
- [arXiv:2606.14783v1 — The Vision Encoder as a Privacy Boundary: Visual-Token Side Channels in Encoder-Free Vision-Language Models](https://arxiv.org/html/2606.14783v1) — first-public `2026-06-10`；accessed `2026-08-29`；Source Family `SF-2026-ARXIV-2606-14783`。
- [arXiv:2606.18284v1 — Breaking the Solver Bottleneck: Training Task Generators at the Learnable Frontier](https://arxiv.org/html/2606.18284v1) — first-public `2026-06-10`；accessed `2026-08-29`；Source Family `SF-2026-ARXIV-2606-18284`。
- [arXiv:2606.18286v1 — CODEBLOCK: Learning to Supervise Code at the Right Granularity](https://arxiv.org/html/2606.18286v1) — first-public `2026-06-10`；accessed `2026-08-29`；Source Family `SF-2026-ARXIV-2606-18286`。
- `SRC-ARXIV` registry contract：`docs/RESEARCH_SOURCES.md`。

## 13. Final Status

- Status: Complete.
- Coverage Gate: Closed.
- Evidence Gate: Passed.
- Books Gate: Passed.
- Fresh-context Semantic Audit: Passed；unresolved findings = 0.
