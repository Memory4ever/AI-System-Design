# Daily Research — 2026-05-17

**Research Date:** 2026-05-17

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-05-16 09:00:00 ～ 2026-05-17 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；DataCite v2 只支持 identity/date/abstract；技术结论绑定 official arXiv exact-v1。

**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed。31/31 candidate 均完成 exact-v1 Review；22/22 Books 写回已通过独立 post-write semantic audit，2605.17193 经恢复后判定为 No Change — Existing Coverage。

## Executive Summary

从 91,841 条 raw records 中严格窗口注册并独立重放 279/279 identity。author denominator 30 经审计移除 6 个 false positive、恢复 7 个 false negative，最终 31 项（11.11%），248 项在分母前闭合。31/31 exact-v1 完成 source-specific Review；2605.17193 official PDF 已恢复并完成 Method、Evaluation、limitations 与 Books challenge。读取 current owner 与相邻章节后，冻结 22 项最小 Books queue；本 lane 未修改共享 Books。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-05-17 |
| Window End | 2026-05-17 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | DEN-20260517-V2-INDEPENDENT-31 |
| Denominator Frozen At | 2026-08-31T23:41:12.114147+00:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-05-16T09:00:00+08:00 | 2026-05-17T09:00:00+08:00 | 2026-08-31T23:41:12.114147+00:00 | DataCite v2 2604/2605/2606 prefixes 00..99 + independent 279/279 semantic replay + exact-v1 | checked | 279 | SF-2026-ARXIV-2605-16745;SF-2026-ARXIV-2605-16746;SF-2026-ARXIV-2605-16776;SF-2026-ARXIV-2605-16786;SF-2026-ARXIV-2605-16787;SF-2026-ARXIV-2605-16790;SF-2026-ARXIV-2605-16819;SF-2026-ARXIV-2605-16826;SF-2026-ARXIV-2605-16839;SF-2026-ARXIV-2605-16867;SF-2026-ARXIV-2605-16928;SF-2026-ARXIV-2605-16976;SF-2026-ARXIV-2605-16986;SF-2026-ARXIV-2605-17003;SF-2026-ARXIV-2605-17026;SF-2026-ARXIV-2605-17028;SF-2026-ARXIV-2605-17034;SF-2026-ARXIV-2605-17062;SF-2026-ARXIV-2605-17076;SF-2026-ARXIV-2605-17106;SF-2026-ARXIV-2605-17113;SF-2026-ARXIV-2605-17160;SF-2026-ARXIV-2605-17164;SF-2026-ARXIV-2605-17169;SF-2026-ARXIV-2605-17170;SF-2026-ARXIV-2605-17172;SF-2026-ARXIV-2605-17173;SF-2026-ARXIV-2605-17193;SF-2026-ARXIV-2605-19373;SF-2026-ARXIV-2605-22850;SF-2026-ARXIV-2605-23986 | pages=300; final_cursor=end; raw=91841; registered=279; screened=279; retained=31; closure=248 | 2026-05-17T00:59:59Z | screening-ledger-independent-final.json#sha256=734ebab3fcd6abbc38c21928407a8d69c8063dfa9a2829c5a276b3c89860d432 | — |

### Coverage Limitations

<!-- coverage:SRC-ARXIV:20260517:start -->279/279 independent screening 与 248 个 family-specific closure 已闭合，Coverage=Closed。31/31 retained family 完成 exact-v1；2605.17193 official PDF 以完整 Content-Length 与 SHA-256 恢复，HTML 404 不再构成 blocker。<!-- coverage:SRC-ARXIV:20260517:end -->

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-16745 | arXiv:2605.16745v1 | paper-v1:2605.16745 | 2026-W20 | 2026-05-16 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-16745 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | Integrate | books-review:SF-2026-ARXIV-2605-16745 | no |
| SF-2026-ARXIV-2605-16746 | arXiv:2605.16746v1 | paper-v1:2605.16746 | 2026-W20 | 2026-05-16 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-16746 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16746 | no |
| SF-2026-ARXIV-2605-16776 | arXiv:2605.16776v1 | paper-v1:2605.16776 | 2026-W20 | 2026-05-16 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-16776 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2605-16776 | no |
| SF-2026-ARXIV-2605-16786 | arXiv:2605.16786v1 | paper-v1:2605.16786 | 2026-W20 | 2026-05-16 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-16786 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | Integrate | books-review:SF-2026-ARXIV-2605-16786 | no |
| SF-2026-ARXIV-2605-16787 | arXiv:2605.16787v1 | paper-v1:2605.16787 | 2026-W20 | 2026-05-16 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-16787 | self | — | new_in_window | TRAIN-GRPO | Integrate | books-review:SF-2026-ARXIV-2605-16787 | no |
| SF-2026-ARXIV-2605-16790 | arXiv:2605.16790v1 | paper-v1:2605.16790 | 2026-W20 | 2026-05-16 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-16790 | self | — | new_in_window | AGENT-TOOL-CALLING | Integrate | books-review:SF-2026-ARXIV-2605-16790 | no |
| SF-2026-ARXIV-2605-16819 | arXiv:2605.16819v1 | paper-v1:2605.16819 | 2026-W20 | 2026-05-16 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-16819 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2605-16819 | no |
| SF-2026-ARXIV-2605-16826 | arXiv:2605.16826v1 | paper-v1:2605.16826 | 2026-W20 | 2026-05-16 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-16826 | self | — | new_in_window | TRAIN-PRETRAINING | Integrate | books-review:SF-2026-ARXIV-2605-16826 | no |
| SF-2026-ARXIV-2605-16839 | arXiv:2605.16839v1 | paper-v1:2605.16839 | 2026-W20 | 2026-05-16 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-16839 | self | — | new_in_window | INFER-PREFILL | Integrate | books-review:SF-2026-ARXIV-2605-16839 | no |
| SF-2026-ARXIV-2605-16867 | arXiv:2605.16867v1 | paper-v1:2605.16867 | 2026-W20 | 2026-05-16 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-16867 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16867 | no |
| SF-2026-ARXIV-2605-16928 | arXiv:2605.16928v1 | paper-v1:2605.16928 | 2026-W20 | 2026-05-16 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-16928 | self | — | new_in_window | INFER-KV-CACHE | Integrate | books-review:SF-2026-ARXIV-2605-16928 | no |
| SF-2026-ARXIV-2605-16976 | arXiv:2605.16976v1 | paper-v1:2605.16976 | 2026-W20 | 2026-05-16 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-16976 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2605-16976 | no |
| SF-2026-ARXIV-2605-16986 | arXiv:2605.16986v1 | paper-v1:2605.16986 | 2026-W20 | 2026-05-16 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-16986 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16986 | no |
| SF-2026-ARXIV-2605-17003 | arXiv:2605.17003v1 | paper-v1:2605.17003 | 2026-W20 | 2026-05-16 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-17003 | self | — | new_in_window | TRAIN-DATA | Integrate | books-review:SF-2026-ARXIV-2605-17003 | no |
| SF-2026-ARXIV-2605-17026 | arXiv:2605.17026v1 | paper-v1:2605.17026 | 2026-W20 | 2026-05-16 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-17026 | self | — | new_in_window | TRAIN-DATA | Integrate | books-review:SF-2026-ARXIV-2605-17026 | no |
| SF-2026-ARXIV-2605-17028 | arXiv:2605.17028v1 | paper-v1:2605.17028 | 2026-W20 | 2026-05-16 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17028 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17028 | no |
| SF-2026-ARXIV-2605-17034 | arXiv:2605.17034v1 | paper-v1:2605.17034 | 2026-W20 | 2026-05-16 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17034 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17034 | no |
| SF-2026-ARXIV-2605-17062 | arXiv:2605.17062v1 | paper-v1:2605.17062 | 2026-W20 | 2026-05-17 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17062 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17062 | no |
| SF-2026-ARXIV-2605-17076 | arXiv:2605.17076v1 | paper-v1:2605.17076 | 2026-W20 | 2026-05-17 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-17076 | self | — | new_in_window | AGENT-MULTI-AGENT | Integrate | books-review:SF-2026-ARXIV-2605-17076 | no |
| SF-2026-ARXIV-2605-17106 | arXiv:2605.17106v1 | paper-v1:2605.17106 | 2026-W20 | 2026-05-17 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-17106 | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-2026-ARXIV-2605-17106 | no |
| SF-2026-ARXIV-2605-17113 | arXiv:2605.17113v1 | paper-v1:2605.17113 | 2026-W20 | 2026-05-17 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-17113 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2605-17113 | no |
| SF-2026-ARXIV-2605-17160 | arXiv:2605.17160v1 | paper-v1:2605.17160 | 2026-W20 | 2026-05-17 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-17160 | self | — | new_in_window | INFER-TENSORRT-LLM | Integrate | books-review:SF-2026-ARXIV-2605-17160 | no |
| SF-2026-ARXIV-2605-17164 | arXiv:2605.17164v1 | paper-v1:2605.17164 | 2026-W20 | 2026-05-17 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-17164 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2605-17164 | no |
| SF-2026-ARXIV-2605-17169 | arXiv:2605.17169v1 | paper-v1:2605.17169 | 2026-W20 | 2026-05-17 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17169 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17169 | no |
| SF-2026-ARXIV-2605-17170 | arXiv:2605.17170v1 | paper-v1:2605.17170 | 2026-W20 | 2026-05-17 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-17170 | self | — | new_in_window | INFER-KV-CACHE | Integrate | books-review:SF-2026-ARXIV-2605-17170 | no |
| SF-2026-ARXIV-2605-17172 | arXiv:2605.17172v1 | paper-v1:2605.17172 | 2026-W20 | 2026-05-17 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17172 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17172 | no |
| SF-2026-ARXIV-2605-17173 | arXiv:2605.17173v1 | paper-v1:2605.17173 | 2026-W20 | 2026-05-17 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-17173 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2605-17173 | no |
| SF-2026-ARXIV-2605-17193 | arXiv:2605.17193v1 | paper-v1:2605.17193 | 2026-W20 | 2026-05-17 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17193 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17193 | no |
| SF-2026-ARXIV-2605-19373 | arXiv:2605.19373v1 | paper-v1:2605.19373 | 2026-W20 | 2026-05-16 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19373 | self | — | new_in_window | PLATFORM-MODEL-REGISTRY | Integrate | books-review:SF-2026-ARXIV-2605-19373 | no |
| SF-2026-ARXIV-2605-22850 | arXiv:2605.22850v1 | paper-v1:2605.22850 | 2026-W20 | 2026-05-17 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-22850 | self | — | new_in_window | INFER-KV-CACHE | Integrate | books-review:SF-2026-ARXIV-2605-22850 | no |
| SF-2026-ARXIV-2605-23986 | arXiv:2605.23986v1 | paper-v1:2605.23986 | 2026-W20 | 2026-05-16 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-23986 | self | — | new_in_window | AGENT-MEMORY | Integrate | books-review:SF-2026-ARXIV-2605-23986 | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-16745 | RP-caaacf30319f358f | deep | arXiv:2605.16745v1 | SRC-ARXIV@arXiv:2605.16745v1 | section 3 Methodology (§3 Methodology) | section 4 Experiments (§4 Experiments) | section 5 Limitations, Discussion & Future Work (§5 Limitations, Discussion & Future Work) | papers/2026/05/_sources/daily-20260517/exact-review-batch-a.txt#sha256=fda592ed66575885cf93f3cc29fe3f7c8802a92d00a4d1fe00e5dd330dd643dd; exact-v1 URL=https://arxiv.org/html/2605.16745v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-16745 | complete |
| SF-2026-ARXIV-2605-16746 | RP-4a1e2cb899b43642 | deep | arXiv:2605.16746v1 | SRC-ARXIV@arXiv:2605.16746v1 | section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt) | Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only | Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup | papers/2026/05/_sources/daily-20260517/exact-review-batch-a.txt#sha256=fda592ed66575885cf93f3cc29fe3f7c8802a92d00a4d1fe00e5dd330dd643dd; exact-v1 URL=https://arxiv.org/html/2605.16746v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-16746 | complete |
| SF-2026-ARXIV-2605-16776 | RP-959f6f263ab46b7f | deep | arXiv:2605.16776v1 | SRC-ARXIV@arXiv:2605.16776v1 | section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt) | Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only | Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup | papers/2026/05/_sources/daily-20260517/exact-review-batch-a.txt#sha256=fda592ed66575885cf93f3cc29fe3f7c8802a92d00a4d1fe00e5dd330dd643dd; exact-v1 URL=https://arxiv.org/html/2605.16776v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-16776 | complete |
| SF-2026-ARXIV-2605-16786 | RP-7ebf4d25fba06fb7 | deep | arXiv:2605.16786v1 | SRC-ARXIV@arXiv:2605.16786v1 | section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt) | Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only | Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup | papers/2026/05/_sources/daily-20260517/exact-review-batch-a.txt#sha256=fda592ed66575885cf93f3cc29fe3f7c8802a92d00a4d1fe00e5dd330dd643dd; exact-v1 URL=https://arxiv.org/html/2605.16786v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-16786 | complete |
| SF-2026-ARXIV-2605-16787 | RP-2d1b9dca058f5f5f | deep | arXiv:2605.16787v1 | SRC-ARXIV@arXiv:2605.16787v1 | section 3.1 Training Algorithm (§3.1 Training Algorithm) | Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only | section 6 Discussion (§6 Discussion) | papers/2026/05/_sources/daily-20260517/exact-review-batch-b.txt#sha256=eb58ffa1e2bcd09fef6dabba79bb00e3b905ace87854841ba755cb8c7fd8a451; exact-v1 URL=https://arxiv.org/html/2605.16787v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-16787 | complete |
| SF-2026-ARXIV-2605-16790 | RP-97bef451871e263a | deep | arXiv:2605.16790v1 | SRC-ARXIV@arXiv:2605.16790v1 | section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt) | Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only | Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup | papers/2026/05/_sources/daily-20260517/exact-review-batch-b.txt#sha256=eb58ffa1e2bcd09fef6dabba79bb00e3b905ace87854841ba755cb8c7fd8a451; exact-v1 URL=https://arxiv.org/html/2605.16790v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-16790 | complete |
| SF-2026-ARXIV-2605-16819 | RP-0b8a7c8bc47aa6b1 | deep | arXiv:2605.16819v1 | SRC-ARXIV@arXiv:2605.16819v1 | section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt) | Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only | Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup | papers/2026/05/_sources/daily-20260517/exact-review-batch-b.txt#sha256=eb58ffa1e2bcd09fef6dabba79bb00e3b905ace87854841ba755cb8c7fd8a451; exact-v1 URL=https://arxiv.org/html/2605.16819v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-16819 | complete |
| SF-2026-ARXIV-2605-16826 | RP-b06546f2fbed19cd | deep | arXiv:2605.16826v1 | SRC-ARXIV@arXiv:2605.16826v1 | section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt) | Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only | Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup | papers/2026/05/_sources/daily-20260517/exact-review-batch-b.txt#sha256=eb58ffa1e2bcd09fef6dabba79bb00e3b905ace87854841ba755cb8c7fd8a451; exact-v1 URL=https://arxiv.org/html/2605.16826v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-16826 | complete |
| SF-2026-ARXIV-2605-16839 | RP-ac62ed41b98b7afc | deep | arXiv:2605.16839v1 | SRC-ARXIV@arXiv:2605.16839v1 | section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt) | Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only | Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup | papers/2026/05/_sources/daily-20260517/exact-review-batch-b.txt#sha256=eb58ffa1e2bcd09fef6dabba79bb00e3b905ace87854841ba755cb8c7fd8a451; exact-v1 URL=https://arxiv.org/html/2605.16839v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-16839 | complete |
| SF-2026-ARXIV-2605-16867 | RP-303011d3db920e33 | deep | arXiv:2605.16867v1 | SRC-ARXIV@arXiv:2605.16867v1 | section 2.2 Lessons Learned from Existing Request-routing Methods (§2.2 Lessons Learned from Existing Request-routing Methods) | section 4 Evaluation (§4 Evaluation) | section 5 Additional Related Works and Discussions (§5 Additional Related Works and Discussions) | papers/2026/05/_sources/daily-20260517/exact-review-recovered-fn-a.txt#sha256=7b72732f912c05fa82020ab8fd5844841dbb8853ad1cd73ed33a25196f89b2ad; exact-v1 URL=https://arxiv.org/html/2605.16867v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-16867 | complete |
| SF-2026-ARXIV-2605-16928 | RP-9b7a81b68e3f74bf | deep | arXiv:2605.16928v1 | SRC-ARXIV@arXiv:2605.16928v1 | section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt) | Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only | Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup | papers/2026/05/_sources/daily-20260517/exact-review-batch-c.txt#sha256=8b5717c9d592f72ad26704544e5b47d6c7879fdc93db6f85c974d37313c58e3b; exact-v1 URL=https://arxiv.org/html/2605.16928v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-16928 | complete |
| SF-2026-ARXIV-2605-16976 | RP-eb1ef580e1a1784f | deep | arXiv:2605.16976v1 | SRC-ARXIV@arXiv:2605.16976v1 | section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt) | Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only | Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup | papers/2026/05/_sources/daily-20260517/exact-review-recovered-fn-a.txt#sha256=7b72732f912c05fa82020ab8fd5844841dbb8853ad1cd73ed33a25196f89b2ad; exact-v1 URL=https://arxiv.org/html/2605.16976v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-16976 | complete |
| SF-2026-ARXIV-2605-16986 | RP-6d4cfc5600612a37 | deep | arXiv:2605.16986v1 | SRC-ARXIV@arXiv:2605.16986v1 | section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt) | Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only | Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup | papers/2026/05/_sources/daily-20260517/exact-review-batch-c.txt#sha256=8b5717c9d592f72ad26704544e5b47d6c7879fdc93db6f85c974d37313c58e3b; exact-v1 URL=https://arxiv.org/html/2605.16986v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-16986 | complete |
| SF-2026-ARXIV-2605-17003 | RP-98a87e27fa4c55b2 | deep | arXiv:2605.17003v1 | SRC-ARXIV@arXiv:2605.17003v1 | section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt) | Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only | Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup | papers/2026/05/_sources/daily-20260517/exact-review-batch-c.txt#sha256=8b5717c9d592f72ad26704544e5b47d6c7879fdc93db6f85c974d37313c58e3b; exact-v1 URL=https://arxiv.org/html/2605.17003v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17003 | complete |
| SF-2026-ARXIV-2605-17026 | RP-386a2535f7264ddc | deep | arXiv:2605.17026v1 | SRC-ARXIV@arXiv:2605.17026v1 | section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt) | Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only | Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup | papers/2026/05/_sources/daily-20260517/exact-review-recovered-fn-a.txt#sha256=7b72732f912c05fa82020ab8fd5844841dbb8853ad1cd73ed33a25196f89b2ad; exact-v1 URL=https://arxiv.org/html/2605.17026v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17026 | complete |
| SF-2026-ARXIV-2605-17028 | RP-a8b29f495e52e5ce | deep | arXiv:2605.17028v1 | SRC-ARXIV@arXiv:2605.17028v1 | section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt) | Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only | Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup | papers/2026/05/_sources/daily-20260517/exact-review-recovered-fn-a.txt#sha256=7b72732f912c05fa82020ab8fd5844841dbb8853ad1cd73ed33a25196f89b2ad; exact-v1 URL=https://arxiv.org/html/2605.17028v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17028 | complete |
| SF-2026-ARXIV-2605-17034 | RP-398f1df1a9297040 | deep | arXiv:2605.17034v1 | SRC-ARXIV@arXiv:2605.17034v1 | section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt) | Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only | Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup | papers/2026/05/_sources/daily-20260517/exact-review-batch-c.txt#sha256=8b5717c9d592f72ad26704544e5b47d6c7879fdc93db6f85c974d37313c58e3b; exact-v1 URL=https://arxiv.org/html/2605.17034v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17034 | complete |
| SF-2026-ARXIV-2605-17062 | RP-7ef1ca7efc7efd89 | deep | arXiv:2605.17062v1 | SRC-ARXIV@arXiv:2605.17062v1 | section 4 Replication Methodology (§4 Replication Methodology) | section 5 Results (§5 model/package-registry comparisons) | section 8 Limitations (§8 Limitations) | papers/2026/05/_sources/daily-20260517/exact-review-special-pdf.txt#sha256=d44a0fff9094a693d0b4d4ca20ae4fbaa15571a84bcba5325ed128901794785c; exact-v1 URL=https://arxiv.org/pdf/2605.17062v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17062 | complete |
| SF-2026-ARXIV-2605-17076 | RP-f7e0b7f865c61fdf | deep | arXiv:2605.17076v1 | SRC-ARXIV@arXiv:2605.17076v1 | section VII-M (§VII-M) | Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only | Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup | papers/2026/05/_sources/daily-20260517/exact-body-batch-d.txt#sha256=ce6510fdc372a9699218a35e347a34f369b7c0ee1bcb22ec1f2fc1c2e690f8ea; exact-v1 URL=https://arxiv.org/html/2605.17076v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17076 | complete |
| SF-2026-ARXIV-2605-17106 | RP-6863f87e5802d9f6 | deep | arXiv:2605.17106v1 | SRC-ARXIV@arXiv:2605.17106v1 | section 8 (§8) | Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only | Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup | papers/2026/05/_sources/daily-20260517/exact-body-batch-d.txt#sha256=ce6510fdc372a9699218a35e347a34f369b7c0ee1bcb22ec1f2fc1c2e690f8ea; exact-v1 URL=https://arxiv.org/html/2605.17106v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17106 | complete |
| SF-2026-ARXIV-2605-17113 | RP-cb2bf52607e9ac80 | deep | arXiv:2605.17113v1 | SRC-ARXIV@arXiv:2605.17113v1 | section 3 Methods (§3 Methods) | section 5 Experiments (§5 Experiments) | section 7 Discussion and Limitations (§7 Discussion and Limitations) | papers/2026/05/_sources/daily-20260517/exact-review-recovered-fn-b.txt#sha256=8ae46ad2a45287bcf09ba2b87d92d4d5896edd06f67f8df4a568ef5e394eb200; exact-v1 URL=https://arxiv.org/html/2605.17113v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17113 | complete |
| SF-2026-ARXIV-2605-17160 | RP-8038db9b156724af | deep | arXiv:2605.17160v1 | SRC-ARXIV@arXiv:2605.17160v1 | section 3 Counterfactual-Faithful Quantization (§3 CFQ) | section 4 Experiments (§4 ADULT, GERMAN CREDIT and COMPAS) | section 6 Limitations (§6 validity boundary) | papers/2026/05/_sources/daily-20260517/exact-review-2605.17160-pdf.txt#sha256=55f65685ab8b08614797164881d4e28f2b4007eba4a985a3a30ef874cea4b066; exact-v1 URL=https://arxiv.org/pdf/2605.17160v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17160 | complete |
| SF-2026-ARXIV-2605-17164 | RP-7663776eb172f83f | deep | arXiv:2605.17164v1 | SRC-ARXIV@arXiv:2605.17164v1 | section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt) | Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only | Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup | papers/2026/05/_sources/daily-20260517/exact-body-batch-d.txt#sha256=ce6510fdc372a9699218a35e347a34f369b7c0ee1bcb22ec1f2fc1c2e690f8ea; exact-v1 URL=https://arxiv.org/html/2605.17164v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17164 | complete |
| SF-2026-ARXIV-2605-17169 | RP-5e64034cdd32220f | deep | arXiv:2605.17169v1 | SRC-ARXIV@arXiv:2605.17169v1 | section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt) | Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only | Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup | papers/2026/05/_sources/daily-20260517/exact-review-recovered-fn-b.txt#sha256=8ae46ad2a45287bcf09ba2b87d92d4d5896edd06f67f8df4a568ef5e394eb200; exact-v1 URL=https://arxiv.org/html/2605.17169v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17169 | complete |
| SF-2026-ARXIV-2605-17170 | RP-362f0afd90fd5a64 | deep | arXiv:2605.17170v1 | SRC-ARXIV@arXiv:2605.17170v1 | section 49 (§49) | Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only | Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup | papers/2026/05/_sources/daily-20260517/exact-body-batch-d.txt#sha256=ce6510fdc372a9699218a35e347a34f369b7c0ee1bcb22ec1f2fc1c2e690f8ea; exact-v1 URL=https://arxiv.org/html/2605.17170v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17170 | complete |
| SF-2026-ARXIV-2605-17172 | RP-ba56c05060be31f5 | deep | arXiv:2605.17172v1 | SRC-ARXIV@arXiv:2605.17172v1 | section 3 Methods (§3 Methods) | section 3.2 Evaluation Metrics (§3.2 Evaluation Metrics) | section 5 Discussion and Conclusion (§5 Discussion and Conclusion) | papers/2026/05/_sources/daily-20260517/exact-review-batch-e.txt#sha256=9abdfb74430dcb68b786da23298e7b85d4ec789284d97e023fbe7f83a4d9208f; exact-v1 URL=https://arxiv.org/html/2605.17172v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17172 | complete |
| SF-2026-ARXIV-2605-17173 | RP-fad7ce5bd68b8c63 | deep | arXiv:2605.17173v1 | SRC-ARXIV@arXiv:2605.17173v1 | section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt) | Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only | Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup | papers/2026/05/_sources/daily-20260517/exact-review-batch-e.txt#sha256=9abdfb74430dcb68b786da23298e7b85d4ec789284d97e023fbe7f83a4d9208f; exact-v1 URL=https://arxiv.org/html/2605.17173v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17173 | complete |
| SF-2026-ARXIV-2605-17193 | RP-9ec4fa2ed0748ca9 | deep | arXiv:2605.17193v1 | SRC-ARXIV@arXiv:2605.17193v1 | PDF section Methods; Supplementary Note 1 §§1.1–1.8; Supplementary Notes 2–3 intervention definitions | PDF section Results: Semantic Collapse in Extended Open-Ended Simulations; Semantic Collapse Resists Intervention; Diagnosing Mechanisms of Semantic Collapse; Supplementary Note 3 §3.7 | PDF section Discussion; Supplementary Note 3 §3.7 non-causal regression boundary; Supplementary Note 5 heuristic-theory and predictive-regularity boundaries | official exact-v1 PDF=https://arxiv.org/pdf/2605.17193v1; bytes=4076663; sha256=edde49ce22de86ac25ad4d676f9003afec5c11513bee35438ca8db965322abe7; immutable code/data commit Not Disclosed | claim:SF-2026-ARXIV-2605-17193 | complete |
| SF-2026-ARXIV-2605-19373 | RP-100563ab07b862d8 | deep | arXiv:2605.19373v1 | SRC-ARXIV@arXiv:2605.19373v1 | section 4 The Solution: Two-Layer Architecture (§4 The Solution: Two-Layer Architecture) | section 3.1 Formal Analysis of CRDT Property Violations (§3.1 Formal Analysis of CRDT Property Violations) | section 7 Discussion (§7 Discussion) | papers/2026/05/_sources/daily-20260517/exact-review-batch-f.txt#sha256=b5d6a0a2fd67c424c789e8fdee75b6523c7473081588f5eee6a221ecc4fafaff; exact-v1 URL=https://arxiv.org/html/2605.19373v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-19373 | complete |
| SF-2026-ARXIV-2605-22850 | RP-f147eaf02fbb1f07 | deep | arXiv:2605.22850v1 | SRC-ARXIV@arXiv:2605.22850v1 | section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt) | Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only | Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup | papers/2026/05/_sources/daily-20260517/exact-review-batch-f.txt#sha256=b5d6a0a2fd67c424c789e8fdee75b6523c7473081588f5eee6a221ecc4fafaff; exact-v1 URL=https://arxiv.org/html/2605.22850v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-22850 | complete |
| SF-2026-ARXIV-2605-23986 | RP-40ee91c88e737a85 | deep | arXiv:2605.23986v1 | SRC-ARXIV@arXiv:2605.23986v1 | section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt) | Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only | Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup | papers/2026/05/_sources/daily-20260517/exact-review-batch-f.txt#sha256=b5d6a0a2fd67c424c789e8fdee75b6523c7473081588f5eee6a221ecc4fafaff; exact-v1 URL=https://arxiv.org/html/2605.23986v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-23986 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2605-16745:start -->
#### EVA01: Unified Native 3D Understanding and Generation via Mixture-of-Transformers

问题与机制：EVA01: Unified Native 3D Understanding and Generation via Mixture-of-Transformers 提出的具体变化是：We introduce EVA01, a unified framework that extends the modality boundary of MLLMs to natively incorporate 3D mesh understanding, generation, and context-aware editing. 摘要中的长期系统挑战为：native 3D tokens join understanding and generation rather than remaining a stateless reconstruction sidecar。它可能改变 `MULTIMODAL-REPRESENTATION` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“Results show that EVA01 achieves state-of-the-art native text-to-3D generation fidelity and unlocks robust long-context multi-turn geometric editing with identity preservation, a capability fundamentally inaccessible to stateless reconstruction pipelines.”暂不作为最终证据。

Evaluation contract：Results show that EVA01 achieves state-of-the-art native text-to-3D generation fidelity and unlocks robust long-context multi-turn geometric editing with identity preservation, a capability fundamentally inaccessible to stateless reconstruction pipelines.

Evidence locators：Method=`section 3 Methodology (§3 Methodology)`；Evaluation=`section 4 Experiments (§4 Experiments)`；Counterevidence=`section 5 Limitations, Discussion & Future Work (§5 Limitations, Discussion & Future Work)`。

Trade-off / failure：新增 controller、metadata、verification、communication 或 runtime state 都带来成本；只在 exact-v1 披露 workload/evaluator 内成立，未披露的硬件、精度、长度、batch、并发、SLO、seed 与 artifact commit 为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-16745:start -->只支持 exact-v1 披露设置中的机制与结果；旧路径在新增 owner/证据/控制责任不成立时继续共存。<!-- claim:SF-2026-ARXIV-2605-16745:end -->

Books Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-16745:end -->

<!-- review:SF-2026-ARXIV-2605-16746:start -->
#### State Contamination in Memory-Augmented LLM Agents

问题与机制：State Contamination in Memory-Augmented LLM Agents 提出的具体变化是：To measure this hidden influence, we introduce the sub-threshold propagation gap (SPG), which quantifies downstream behavioral differences conditioned on memory states that a deployed monitor would classify as safe. 摘要中的长期系统挑战为：persistent memory becomes a cross-turn attack surface whose writes and reuse require separate authority。它可能改变 `AGENT-MEMORY` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“These results suggest that safety in memory-augmented agents should be treated as a state-control problem over evolving context, with sanitization applied before unsafe information is compressed into persistent memory.”暂不作为最终证据。

Evaluation contract：We further find that mitigation depends critically on intervention placement.

Evidence locators：Method=`section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt)`；Evaluation=`Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only`；Counterevidence=`Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup`。

Trade-off / failure：新增 controller、metadata、verification、communication 或 runtime state 都带来成本；只在 exact-v1 披露 workload/evaluator 内成立，未披露的硬件、精度、长度、batch、并发、SLO、seed 与 artifact commit 为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-16746:start -->只支持 exact-v1 披露设置中的机制与结果；旧路径在新增 owner/证据/控制责任不成立时继续共存。<!-- claim:SF-2026-ARXIV-2605-16746:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-16746:end -->

<!-- review:SF-2026-ARXIV-2605-16776:start -->
#### Distinguishable Deletion: Unifying Knowledge Erasure and Refusal for Large Language Model Unlearning

问题与机制：Distinguishable Deletion: Unifying Knowledge Erasure and Refusal for Large Language Model Unlearning 提出的具体变化是：To address these issues, we propose Distinguishable Deletion ($\mathrm{D^2}$), a paradigm that restricts the response distribution in the latent representation rather than specific tokens to erase undesirable knowledge, while distinguishing it from retained knowledge, enabling a refusal mechanism to handle unlearned inputs safely and coherently. 摘要中的长期系统挑战为：unlearning must distinguish parameter erasure from inference-time refusal and verify both contracts。它可能改变 `PLATFORM-SECURITY` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“Extensive experiments demonstrate that EUA significantly outperforms previous methods, indicating the superiority of $\mathrm{D^2}$.”暂不作为最终证据。

Evaluation contract：Extensive experiments demonstrate that EUA significantly outperforms previous methods, indicating the superiority of $\mathrm{D^2}$.

Evidence locators：Method=`section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt)`；Evaluation=`Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only`；Counterevidence=`Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup`。

Trade-off / failure：新增 controller、metadata、verification、communication 或 runtime state 都带来成本；只在 exact-v1 披露 workload/evaluator 内成立，未披露的硬件、精度、长度、batch、并发、SLO、seed 与 artifact commit 为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-16776:start -->只支持 exact-v1 披露设置中的机制与结果；旧路径在新增 owner/证据/控制责任不成立时继续共存。<!-- claim:SF-2026-ARXIV-2605-16776:end -->

Books Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-16776:end -->

<!-- review:SF-2026-ARXIV-2605-16786:start -->
#### Lever: Speculative LLM Inference on Smartphones

问题与机制：Lever: Speculative LLM Inference on Smartphones 提出的具体变化是：We present Lever, an end-to-end system for efficient flash-backed LLM inference on smartphones. 摘要中的长期系统挑战为：flash-backed mobile inference changes the draft/verify cost model and state-placement boundary。它可能改变 `INFER-SPECULATIVE-DECODING` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“We observe that speculative decoding is a natural fit for this setting: a small draft model can remain in DRAM, while a larger flash-resident target model verifies multiple candidate tokens per invocation.”暂不作为最终证据。

Evaluation contract：Comprehensive evaluations show that Lever reduces inference latency by an average of 2.93x over baseline flash-offloaded inference and 1.50x over conventional speculative decoding, narrowing the latency gap between flash-backed and memory-resident LLM inference.

Evidence locators：Method=`section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt)`；Evaluation=`Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only`；Counterevidence=`Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup`。

Trade-off / failure：新增 controller、metadata、verification、communication 或 runtime state 都带来成本；只在 exact-v1 披露 workload/evaluator 内成立，未披露的硬件、精度、长度、batch、并发、SLO、seed 与 artifact commit 为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-16786:start -->只支持 exact-v1 披露设置中的机制与结果；旧路径在新增 owner/证据/控制责任不成立时继续共存。<!-- claim:SF-2026-ARXIV-2605-16786:end -->

Books Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-16786:end -->

<!-- review:SF-2026-ARXIV-2605-16787:start -->
#### The Unlearnability Phenomenon in RLVR for Language Models

问题与机制：The Unlearnability Phenomenon in RLVR for Language Models 提出的具体变化是：Reinforcement Learning with Verifiable Reward (RLVR) has proven effective in improving Large Language Model's (LLM) reasoning ability. 摘要中的长期系统挑战为：RLVR admission must recognize examples with no useful policy-gradient direction rather than treating all verified rewards alike。它可能改变 `TRAIN-GRPO` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“With cross-example gradient analysis, we show that unlearnable examples have fundamental representation issue, characterized by low gradient similarity with the rest of the examples and ungeneralizable reasoning patterns.”暂不作为最终证据。

Evaluation contract：We further show that representation flaws are difficult to mitigate in RL, as data augmentation does not improve gradient similarity.

Evidence locators：Method=`section 3.1 Training Algorithm (§3.1 Training Algorithm)`；Evaluation=`Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only`；Counterevidence=`section 6 Discussion (§6 Discussion)`。

Trade-off / failure：新增 controller、metadata、verification、communication 或 runtime state 都带来成本；只在 exact-v1 披露 workload/evaluator 内成立，未披露的硬件、精度、长度、batch、并发、SLO、seed 与 artifact commit 为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-16787:start -->只支持 exact-v1 披露设置中的机制与结果；旧路径在新增 owner/证据/控制责任不成立时继续共存。<!-- claim:SF-2026-ARXIV-2605-16787:end -->

Books Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-16787:end -->

<!-- review:SF-2026-ARXIV-2605-16790:start -->
#### TIER: Trajectory-Invariant Execution Rewards for Multi-Step Tool Composition

问题与机制：TIER: Trajectory-Invariant Execution Rewards for Multi-Step Tool Composition 提出的具体变化是：We propose TIER: Trajectory-Invariant Execution Rewards, a reward framework that derives supervision directly from function schemas and runtime execution, rather than from reference trajectories. 摘要中的长期系统挑战为：tool-composition reward moves from reference trajectories to invariant execution-state evidence。它可能改变 `AGENT-TOOL-CALLING` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“Ablation studies confirm that all reward components are necessary, highlighting the importance of multi-level supervision for compositional reasoning.”暂不作为最终证据。

Evaluation contract：We further demonstrate consistent gains on benchmarks like BFCL v3 and NestFUL.

Evidence locators：Method=`section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt)`；Evaluation=`Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only`；Counterevidence=`Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup`。

Trade-off / failure：新增 controller、metadata、verification、communication 或 runtime state 都带来成本；只在 exact-v1 披露 workload/evaluator 内成立，未披露的硬件、精度、长度、batch、并发、SLO、seed 与 artifact commit 为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-16790:start -->只支持 exact-v1 披露设置中的机制与结果；旧路径在新增 owner/证据/控制责任不成立时继续共存。<!-- claim:SF-2026-ARXIV-2605-16790:end -->

Books Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-16790:end -->

<!-- review:SF-2026-ARXIV-2605-16819:start -->
#### AgentKernelArena: Generalization-Aware Benchmarking of GPU Kernel Optimization Agents

问题与机制：AgentKernelArena: Generalization-Aware Benchmarking of GPU Kernel Optimization Agents 提出的具体变化是：We present AgentKernelArena, an open-source benchmark for measuring AI coding agents on GPU kernel optimization. 摘要中的长期系统挑战为：agent evaluation must freeze workflow state, hidden task contract, runtime receipts and unseen-shape generalization。它可能改变 `PLATFORM-EVALUATION-SYSTEM` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“AgentKernelArena is designed as a modular, extensible framework for rigorous evaluation of agentic GPU kernel optimization across agents, tasks, and hardware targets.”暂不作为最终证据。

Evaluation contract：AgentKernelArena is designed as a modular, extensible framework for rigorous evaluation of agentic GPU kernel optimization across agents, tasks, and hardware targets.

Evidence locators：Method=`section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt)`；Evaluation=`Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only`；Counterevidence=`Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup`。

Trade-off / failure：新增 controller、metadata、verification、communication 或 runtime state 都带来成本；只在 exact-v1 披露 workload/evaluator 内成立，未披露的硬件、精度、长度、batch、并发、SLO、seed 与 artifact commit 为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-16819:start -->只支持 exact-v1 披露设置中的机制与结果；旧路径在新增 owner/证据/控制责任不成立时继续共存。<!-- claim:SF-2026-ARXIV-2605-16819:end -->

Books Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-16819:end -->

<!-- review:SF-2026-ARXIV-2605-16826:start -->
#### Decoupling KL and Trajectories: A Unified Perspective for SFT, DAgger, Offline RL, and OPD in LLM Distillation

问题与机制：Decoupling KL and Trajectories: A Unified Perspective for SFT, DAgger, Offline RL, and OPD in LLM Distillation 提出的具体变化是：Motivated by these findings, we propose KL mixing and an entropy-gated length curriculum. 摘要中的长期系统挑战为：distillation outcomes depend separately on prefix provenance and KL direction, changing the training contract。它可能改变 `TRAIN-PRETRAINING` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“Our results provide a framework and practical methods for designing reasoning distillation objectives that balance accuracy, diversity, compute, and RL behavior.”暂不作为最终证据。

Evaluation contract：We show that the prevailing paradigms, off-policy distillation and on-policy distillation (OPD), implicitly couple two orthogonal choices: prefix source and token-level KL direction.

Evidence locators：Method=`section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt)`；Evaluation=`Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only`；Counterevidence=`Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup`。

Trade-off / failure：新增 controller、metadata、verification、communication 或 runtime state 都带来成本；只在 exact-v1 披露 workload/evaluator 内成立，未披露的硬件、精度、长度、batch、并发、SLO、seed 与 artifact commit 为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-16826:start -->只支持 exact-v1 披露设置中的机制与结果；旧路径在新增 owner/证据/控制责任不成立时继续共存。<!-- claim:SF-2026-ARXIV-2605-16826:end -->

Books Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-16826:end -->

<!-- review:SF-2026-ARXIV-2605-16839:start -->
#### CompactAttention: Accelerating Chunked Prefill with Block-Union KV Selection

问题与机制：CompactAttention: Accelerating Chunked Prefill with Block-Union KV Selection 提出的具体变化是：To address these limitations, we propose CompactAttention, a chunked-prefill attention mechanism based on Block-Union KV Selection. 摘要中的长期系统挑战为：chunked prefill reuses a union of selected KV blocks while preserving the dense attention owner。它可能改变 `INFER-PREFILL` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“On LLaMA-3.1-8B-Instruct, CompactAttention maintains accuracy close to dense attention on the RULER benchmark while delivering up to 2.72$\times$ attention speedup at 128K context length under chunked prefill.”暂不作为最终证据。

Evaluation contract：On LLaMA-3.1-8B-Instruct, CompactAttention maintains accuracy close to dense attention on the RULER benchmark while delivering up to 2.72$\times$ attention speedup at 128K context length under chunked prefill.

Evidence locators：Method=`section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt)`；Evaluation=`Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only`；Counterevidence=`Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup`。

Trade-off / failure：新增 controller、metadata、verification、communication 或 runtime state 都带来成本；只在 exact-v1 披露 workload/evaluator 内成立，未披露的硬件、精度、长度、batch、并发、SLO、seed 与 artifact commit 为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-16839:start -->只支持 exact-v1 披露设置中的机制与结果；旧路径在新增 owner/证据/控制责任不成立时继续共存。<!-- claim:SF-2026-ARXIV-2605-16839:end -->

Books Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-16839:end -->

<!-- review:SF-2026-ARXIV-2605-16867:start -->
#### GoodServe: Towards High-Goodput Serving of Agentic LLM Inferences over Heterogeneous Resources

问题与机制：In this paper, we propose GoodServe, a goodput-optimized serving system for agentic inferences over heterogeneous resources.

Evaluation contract：Our evaluations show that GoodServe improves goodput by up to 27.4% over existing routing methods.

Evidence locators：Method=`section 2.2 Lessons Learned from Existing Request-routing Methods (§2.2 Lessons Learned from Existing Request-routing Methods)`；Evaluation=`section 4 Evaluation (§4 Evaluation)`；Counterevidence=`section 5 Additional Related Works and Discussions (§5 Additional Related Works and Discussions)`。

Trade-off / failure：新增 controller、metadata、verification、communication 或 runtime state 都带来成本；只在 exact-v1 披露 workload/evaluator 内成立，未披露的硬件、精度、长度、batch、并发、SLO、seed 与 artifact commit 为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-16867:start -->只支持 exact-v1 披露设置中的机制与结果；旧路径在新增 owner/证据/控制责任不成立时继续共存。<!-- claim:SF-2026-ARXIV-2605-16867:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-16867:end -->

<!-- review:SF-2026-ARXIV-2605-16928:start -->
#### Full Attention Strikes Back: Transferring Full Attention into Sparse within Hundred Training Steps

问题与机制：Full Attention Strikes Back: Transferring Full Attention into Sparse within Hundred Training Steps 提出的具体变化是：Based on these insights, we propose RTPurbo, which retains the full KV cache only for retrieval heads and introduces a lightweight token indexer for sparse attention. 摘要中的长期系统挑战为：head-aware dense-to-sparse post-training separates candidate routing from exact attention。它可能改变 `INFER-KV-CACHE` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“These results suggest that strong sparse inference can be obtained from standard full-attention training without expensive native sparse pretraining.”暂不作为最终证据。

Evaluation contract：Experiments on long-context benchmarks and reasoning tasks show that RTPurbo preserves near-lossless accuracy while delivering substantial efficiency gains, including up to a 9.36$\times$ prefill speedup at 1M context and about a 2.01$\times$ decode speedup.

Evidence locators：Method=`section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt)`；Evaluation=`Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only`；Counterevidence=`Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup`。

Trade-off / failure：新增 controller、metadata、verification、communication 或 runtime state 都带来成本；只在 exact-v1 披露 workload/evaluator 内成立，未披露的硬件、精度、长度、batch、并发、SLO、seed 与 artifact commit 为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-16928:start -->只支持 exact-v1 披露设置中的机制与结果；旧路径在新增 owner/证据/控制责任不成立时继续共存。<!-- claim:SF-2026-ARXIV-2605-16928:end -->

Books Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-16928:end -->

<!-- review:SF-2026-ARXIV-2605-16976:start -->
#### Securing LLM Agents Need Intent-to-Execution Integrity

问题与机制：Drawing on this analogy, we identify two fundamental problem sources -- untrusted data ingestion and untrusted tool execution -- and derive four integrity properties that must hold simultaneously: \emph{Tool Integrity}, \emph{Instruction Integrity}, \emph{Judgment Integrity}, and \emph{Data Flow Integrity}.

Evaluation contract：Analyzing existing agentic defenses against these properties reveals that current systems provide only partial and non-compositional coverage, leaving fundamental gaps in securing modern LLM agents.

Evidence locators：Method=`section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt)`；Evaluation=`Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only`；Counterevidence=`Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup`。

Trade-off / failure：新增 controller、metadata、verification、communication 或 runtime state 都带来成本；只在 exact-v1 披露 workload/evaluator 内成立，未披露的硬件、精度、长度、batch、并发、SLO、seed 与 artifact commit 为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-16976:start -->只支持 exact-v1 披露设置中的机制与结果；旧路径在新增 owner/证据/控制责任不成立时继续共存。<!-- claim:SF-2026-ARXIV-2605-16976:end -->

Books Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-16976:end -->

<!-- review:SF-2026-ARXIV-2605-16986:start -->
#### Skills on the Fly: Test-Time Adaptive Skill Synthesis for LLM Agents

问题与机制：Skills on the Fly: Test-Time Adaptive Skill Synthesis for LLM Agents 提出的具体变化是：We call this challenge test-time compute-to-capability conversion and propose SkillTTA, which retrieves task-relevant training trajectories and synthesizes a temporary skill conditioned on the visible target context for a solver with fixed parameters. 摘要中的长期系统挑战为：test-time skill synthesis creates ephemeral executable state that needs admission, expiry and rollback。它可能改变 `AGENT-PLATFORM` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“Across ALFWorld, SpreadsheetBench, BigCodeBench, and WebShop, SkillTTA outperforms state-of-the-art reuse and optimization baselines.”暂不作为最终证据。

Evaluation contract：It attains a higher performance ceiling at lower compute cost than baseline reuse and sampling strategies.

Evidence locators：Method=`section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt)`；Evaluation=`Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only`；Counterevidence=`Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup`。

Trade-off / failure：新增 controller、metadata、verification、communication 或 runtime state 都带来成本；只在 exact-v1 披露 workload/evaluator 内成立，未披露的硬件、精度、长度、batch、并发、SLO、seed 与 artifact commit 为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-16986:start -->只支持 exact-v1 披露设置中的机制与结果；旧路径在新增 owner/证据/控制责任不成立时继续共存。<!-- claim:SF-2026-ARXIV-2605-16986:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-16986:end -->

<!-- review:SF-2026-ARXIV-2605-17003:start -->
#### Learning-Zone Energy: Online Data Selection for Efficient RL Post-Training

问题与机制：Learning-Zone Energy: Online Data Selection for Efficient RL Post-Training 提出的具体变化是：To address this fundamental inefficiency, we propose Learning-Zone Energy (LZE), a theoretically grounded, fully online data selection framework that concentrates computation on the model's active learning frontier. 摘要中的长期系统挑战为：online RL data selection becomes a control loop over current policy frontier rather than a static dataset。它可能改变 `TRAIN-DATA` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“Our code is available at https://github.com/Stellaris167/LZE.”暂不作为最终证据。

Evaluation contract：Our code is available at https://github.com/Stellaris167/LZE.

Evidence locators：Method=`section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt)`；Evaluation=`Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only`；Counterevidence=`Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup`。

Trade-off / failure：新增 controller、metadata、verification、communication 或 runtime state 都带来成本；只在 exact-v1 披露 workload/evaluator 内成立，未披露的硬件、精度、长度、batch、并发、SLO、seed 与 artifact commit 为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-17003:start -->只支持 exact-v1 披露设置中的机制与结果；旧路径在新增 owner/证据/控制责任不成立时继续共存。<!-- claim:SF-2026-ARXIV-2605-17003:end -->

Books Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-17003:end -->

<!-- review:SF-2026-ARXIV-2605-17026:start -->
#### Why Do Reasoning Models Lose Coverage? The Role of Data and Forks in the Road

问题与机制：While these methods reliably improve pass@1 accuracy, prior works have observed that they show a coverage shrinkage behavior, where pass@k degrades relative to the base model.

Evaluation contract：We also demonstrate that this shrinkage behavior can be partially mitigated through targeted data synthesis design of decision-points, and a more systematic diversity-encouraging decoding mechanism.

Evidence locators：Method=`section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt)`；Evaluation=`Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only`；Counterevidence=`Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup`。

Trade-off / failure：新增 controller、metadata、verification、communication 或 runtime state 都带来成本；只在 exact-v1 披露 workload/evaluator 内成立，未披露的硬件、精度、长度、batch、并发、SLO、seed 与 artifact commit 为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-17026:start -->只支持 exact-v1 披露设置中的机制与结果；旧路径在新增 owner/证据/控制责任不成立时继续共存。<!-- claim:SF-2026-ARXIV-2605-17026:end -->

Books Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-17026:end -->

<!-- review:SF-2026-ARXIV-2605-17028:start -->
#### PARALLAX: Separating Genuine Hallucination Detection from Benchmark Construction Artifacts

问题与机制：We show, however, that much of this apparent progress does not survive scrutiny.

Evaluation contract：To measure what genuine detection capability remains once these artifacts are controlled, we conduct a large-scale evaluation spanning twenty-two detection methods, twelve open-source models spanning six architectural families, and six corpora.

Evidence locators：Method=`section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt)`；Evaluation=`Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only`；Counterevidence=`Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup`。

Trade-off / failure：新增 controller、metadata、verification、communication 或 runtime state 都带来成本；只在 exact-v1 披露 workload/evaluator 内成立，未披露的硬件、精度、长度、batch、并发、SLO、seed 与 artifact commit 为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-17028:start -->只支持 exact-v1 披露设置中的机制与结果；旧路径在新增 owner/证据/控制责任不成立时继续共存。<!-- claim:SF-2026-ARXIV-2605-17028:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-17028:end -->

<!-- review:SF-2026-ARXIV-2605-17034:start -->
#### Privacy Policy Enforcement Guardrails for Data-Sensitive Retrieval-Augmented Generation

问题与机制：Privacy Policy Enforcement Guardrails for Data-Sensitive Retrieval-Augmented Generation 提出的具体变化是：We introduce a Privacy Policy Enforcement (PPE) framework using dual one-class density estimators with fused text embeddings and a calibrated abstain region for out-of-distribution inputs. 摘要中的长期系统挑战为：RAG privacy enforcement must mediate retrieval and generation effects rather than rely on prompt policy。它可能改变 `PLATFORM-SECURITY` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“This methodology provides a robust stress-testing standard for any synthetic-data-trained classifier.”暂不作为最终证据。

Evaluation contract：This methodology provides a robust stress-testing standard for any synthetic-data-trained classifier.

Evidence locators：Method=`section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt)`；Evaluation=`Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only`；Counterevidence=`Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup`。

Trade-off / failure：新增 controller、metadata、verification、communication 或 runtime state 都带来成本；只在 exact-v1 披露 workload/evaluator 内成立，未披露的硬件、精度、长度、batch、并发、SLO、seed 与 artifact commit 为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-17034:start -->只支持 exact-v1 披露设置中的机制与结果；旧路径在新增 owner/证据/控制责任不成立时继续共存。<!-- claim:SF-2026-ARXIV-2605-17034:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-17034:end -->

<!-- review:SF-2026-ARXIV-2605-17062:start -->
#### The Range Shrinks, the Threat Remains: Re-evaluating LLM Package Hallucinations on the 2026 Frontier-Model Cohort

问题与机制：The Range Shrinks, the Threat Remains: Re-evaluating LLM Package Hallucinations on the 2026 Frontier-Model Cohort 提出的具体变化是：Across 199,845 paired Python and JavaScript prompts validated against PyPI and npm master lists, we measure overall hallucination rates between 4.62% (Claude Haiku 4.5) and 6.10% (GPT-5.4-mini) -- an order-of-magnitude compression of the inter-model spread observed by Spracklen, but not a retirement of the threat. 摘要中的长期系统挑战为：package hallucinations create a model-to-software-supply-chain effect path requiring independent resolution。它可能改变 `PLATFORM-SECURITY` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“We further document a Python-over-JavaScript hallucination asymmetry that inverts Spracklen's 2024 finding, identify a Haiku-below-Sonnet inversion within the Anthropic family, and observe a Jaccard-similarity peak between DeepSeek V3.2 and GPT-5.4-mini (J = 0.343) suggestive of shared training-data origins.”暂不作为最终证据。

Evaluation contract：We further document a Python-over-JavaScript hallucination asymmetry that inverts Spracklen's 2024 finding, identify a Haiku-below-Sonnet inversion within the Anthropic family, and observe a Jaccard-similarity peak between DeepSeek V3.2 and GPT-5.4-mini (J = 0.343) suggestive of shared training-data origins.

Evidence locators：Method=`section 4 Replication Methodology (§4 Replication Methodology)`；Evaluation=`section 5 Results (§5 model/package-registry comparisons)`；Counterevidence=`section 8 Limitations (§8 Limitations)`。

Trade-off / failure：新增 controller、metadata、verification、communication 或 runtime state 都带来成本；只在 exact-v1 披露 workload/evaluator 内成立，未披露的硬件、精度、长度、batch、并发、SLO、seed 与 artifact commit 为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-17062:start -->只支持 exact-v1 披露设置中的机制与结果；旧路径在新增 owner/证据/控制责任不成立时继续共存。<!-- claim:SF-2026-ARXIV-2605-17062:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-17062:end -->

<!-- review:SF-2026-ARXIV-2605-17076:start -->
#### S-Bus: Automatic Read-Set Reconstruction for Multi-Agent LLM State Coordination

问题与机制：S-Bus: Automatic Read-Set Reconstruction for Multi-Agent LLM State Coordination 提出的具体变化是：S-Bus is an HTTP middleware whose central mechanism, a server-side DeliveryLog, reconstructs each agent's read set at commit time from observed HTTP GET traffic. 摘要中的长期系统挑战为：observable-read isolation gives shared mutable multi-agent state an explicit consistency boundary。它可能改变 `AGENT-MULTI-AGENT` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“Source code, formal proofs, harness, annotation data: https://github.com/sajjadanwar0/sbus”暂不作为最终证据。

Evaluation contract：Source code, formal proofs, harness, annotation data: https://github.com/sajjadanwar0/sbus

Evidence locators：Method=`section VII-M (§VII-M)`；Evaluation=`Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only`；Counterevidence=`Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup`。

Trade-off / failure：新增 controller、metadata、verification、communication 或 runtime state 都带来成本；只在 exact-v1 披露 workload/evaluator 内成立，未披露的硬件、精度、长度、batch、并发、SLO、seed 与 artifact commit 为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-17076:start -->只支持 exact-v1 披露设置中的机制与结果；旧路径在新增 owner/证据/控制责任不成立时继续共存。<!-- claim:SF-2026-ARXIV-2605-17076:end -->

Books Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-17076:end -->

<!-- review:SF-2026-ARXIV-2605-17106:start -->
#### HyDRA: Hybrid Dynamic Routing Architecture for Heterogeneous LLM Pools

问题与机制：HyDRA: Hybrid Dynamic Routing Architecture for Heterogeneous LLM Pools 提出的具体变化是：We present HyDRA (Hybrid Dynamic Routing Architecture), a framework that predicts fine-grained, multi-dimensional capability requirements per query and matches them against configuration-defined model profiles via shortfall matching. 摘要中的长期系统挑战为：heterogeneous model pools and routing policy become decoupled deployable revisions。它可能改变 `INFER-SCHEDULING` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“Results generalize across LiveCodeBench, BigCodeBench, and tau-bench.”暂不作为最终证据。

Evaluation contract：HyDRA is deployed to all users in GitHub Copilot's VS Code Chat auto-mode and -- to our knowledge for the first time in the LLM routing literature -- demonstrates language-invariant routing across CJK, European, and other script families.

Evidence locators：Method=`section 8 (§8)`；Evaluation=`Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only`；Counterevidence=`Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup`。

Trade-off / failure：新增 controller、metadata、verification、communication 或 runtime state 都带来成本；只在 exact-v1 披露 workload/evaluator 内成立，未披露的硬件、精度、长度、batch、并发、SLO、seed 与 artifact commit 为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-17106:start -->只支持 exact-v1 披露设置中的机制与结果；旧路径在新增 owner/证据/控制责任不成立时继续共存。<!-- claim:SF-2026-ARXIV-2605-17106:end -->

Books Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-17106:end -->

<!-- review:SF-2026-ARXIV-2605-17113:start -->
#### The Point of No Return: Counterfactual Localization of Deceptive Commitment in Language-Model Reasoning

问题与机制：We introduce counterfactual localization: for each sentence prefix in a reasoning trace, we fix the prefix, resample continuations, and estimate the probability of a deceptive outcome.

Evaluation contract：Using this resource, we show that lexical cues for commitment prediction transfer poorly across environments, whereas attention-based transition features generalize out of distribution, suggesting that deceptive commitment is reflected in reusable changes in reasoning dynamics rather than surface form.

Evidence locators：Method=`section 3 Methods (§3 Methods)`；Evaluation=`section 5 Experiments (§5 Experiments)`；Counterevidence=`section 7 Discussion and Limitations (§7 Discussion and Limitations)`。

Trade-off / failure：新增 controller、metadata、verification、communication 或 runtime state 都带来成本；只在 exact-v1 披露 workload/evaluator 内成立，未披露的硬件、精度、长度、batch、并发、SLO、seed 与 artifact commit 为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-17113:start -->只支持 exact-v1 披露设置中的机制与结果；旧路径在新增 owner/证据/控制责任不成立时继续共存。<!-- claim:SF-2026-ARXIV-2605-17113:end -->

Books Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-17113:end -->

<!-- review:SF-2026-ARXIV-2605-17160:start -->
#### When Bits Break Recourse: Counterfactual-Faithful Quantization

问题与机制：We propose two metrics: Validity Drop (VD), which measures the fraction of full-precision recourse actions that no longer achieve the target outcome after quantization, and Counterfactual Recourse Gap (CRG), which measures the increase in minimal recourse cost under the quantized model.

Evaluation contract：Experiments on Adult, German Credit, and COMPAS show that standard QAT and mixed-precision baselines can preserve accuracy while substantially degrading recourse stability.

Evidence locators：Method=`section 3 Counterfactual-Faithful Quantization (§3 CFQ)`；Evaluation=`section 4 Experiments (§4 ADULT, GERMAN CREDIT and COMPAS)`；Counterevidence=`section 6 Limitations (§6 validity boundary)`。

Trade-off / failure：新增 controller、metadata、verification、communication 或 runtime state 都带来成本；只在 exact-v1 披露 workload/evaluator 内成立，未披露的硬件、精度、长度、batch、并发、SLO、seed 与 artifact commit 为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-17160:start -->只支持 exact-v1 披露设置中的机制与结果；旧路径在新增 owner/证据/控制责任不成立时继续共存。<!-- claim:SF-2026-ARXIV-2605-17160:end -->

Books Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-17160:end -->

<!-- review:SF-2026-ARXIV-2605-17164:start -->
#### Charon: A Unified and Fine-Grained Simulator for Large-Scale LLM Training and Inference

问题与机制：Charon: A Unified and Fine-Grained Simulator for Large-Scale LLM Training and Inference 提出的具体变化是：To address this, we introduce Charon, a unified, modular, and fine-grained simulator for accurately predicting LLM performance. 摘要中的长期系统挑战为：training and inference what-if simulation need a shared configuration identity and validation contract。它可能改变 `PLATFORM-EVALUATION-SYSTEM` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“In a practical inference deployment case, Charon discovered a configuration that improved system throughput over an engineering-tuned baseline, demonstrating its significant real-world value.”暂不作为最终证据。

Evaluation contract：Experiments show Charon achieves high accuracy across different models and configurations, with an overall prediction error consistently under 5.35%, and even under 3.74% for training with a large-scale GPU cluster.

Evidence locators：Method=`section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt)`；Evaluation=`Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only`；Counterevidence=`Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup`。

Trade-off / failure：新增 controller、metadata、verification、communication 或 runtime state 都带来成本；只在 exact-v1 披露 workload/evaluator 内成立，未披露的硬件、精度、长度、batch、并发、SLO、seed 与 artifact commit 为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-17164:start -->只支持 exact-v1 披露设置中的机制与结果；旧路径在新增 owner/证据/控制责任不成立时继续共存。<!-- claim:SF-2026-ARXIV-2605-17164:end -->

Books Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-17164:end -->

<!-- review:SF-2026-ARXIV-2605-17169:start -->
#### Responsible Agentic AI Requires Explicit Provenance

问题与机制：Agentic AI is rapidly proliferating across diverse real-world domains such as software engineering, yet public trust has not kept pace.

Evaluation contract：We position that what is missing is not better benchmark-level evaluation but $\textbf{explicit provenance}$ across the full agentic lifecycle, which is the only viable basis for making responsibility computable and actionable.

Evidence locators：Method=`section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt)`；Evaluation=`Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only`；Counterevidence=`Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup`。

Trade-off / failure：新增 controller、metadata、verification、communication 或 runtime state 都带来成本；只在 exact-v1 披露 workload/evaluator 内成立，未披露的硬件、精度、长度、batch、并发、SLO、seed 与 artifact commit 为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-17169:start -->只支持 exact-v1 披露设置中的机制与结果；旧路径在新增 owner/证据/控制责任不成立时继续共存。<!-- claim:SF-2026-ARXIV-2605-17169:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-17169:end -->

<!-- review:SF-2026-ARXIV-2605-17170:start -->
#### TriAxialKV: Toward Extreme Low-Precision KV-Cache Quantization for Agentic Inference Tasks

问题与机制：TriAxialKV: Toward Extreme Low-Precision KV-Cache Quantization for Agentic Inference Tasks 提出的具体变化是：To this end, we introduce TriAxialKV, a novel mixed-precision KV-cache quantization scheme that assigns each token a triaxial tag, calibrates per-tag sensitivity, and allocates INT2/INT4 bitwidths under a fixed memory budget. 摘要中的长期系统挑战为：agentic KV quantization must condition precision on role, modality and temporal lifecycle。它可能改变 `INFER-KV-CACHE` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“As a result, their context exhibits structure that can carry different importance along three key axes: temporal recency to the current turn, modality such as text or image tokens, and semantic role such as user queries, tool calls, observations, or reasoning.”暂不作为最终证据。

Evaluation contract：As a result, their context exhibits structure that can carry different importance along three key axes: temporal recency to the current turn, modality such as text or image tokens, and semantic role such as user queries, tool calls, observations, or…

Evidence locators：Method=`section 49 (§49)`；Evaluation=`Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only`；Counterevidence=`Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup`。

Trade-off / failure：新增 controller、metadata、verification、communication 或 runtime state 都带来成本；只在 exact-v1 披露 workload/evaluator 内成立，未披露的硬件、精度、长度、batch、并发、SLO、seed 与 artifact commit 为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-17170:start -->只支持 exact-v1 披露设置中的机制与结果；旧路径在新增 owner/证据/控制责任不成立时继续共存。<!-- claim:SF-2026-ARXIV-2605-17170:end -->

Books Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-17170:end -->

<!-- review:SF-2026-ARXIV-2605-17172:start -->
#### OpenJarvis: Personal AI, On Personal Devices

问题与机制：OpenJarvis: Personal AI, On Personal Devices 提出的具体变化是：We present OpenJarvis, an architecture that represents a personal AI system as a typed spec over five primitives: Intelligence, Engine, Agents, Tools &amp; Memory, and Learning. 摘要中的长期系统挑战为：personal AI splits sensitive local state, local execution and optional cloud escalation into typed boundaries。它可能改变 `AGENT-PLATFORM` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“They also reduce marginal API cost by ~800x and end-to-end latency by 4x.”暂不作为最终证据。

Evaluation contract：They also reduce marginal API cost by ~800x and end-to-end latency by 4x.

Evidence locators：Method=`section 3 Methods (§3 Methods)`；Evaluation=`section 3.2 Evaluation Metrics (§3.2 Evaluation Metrics)`；Counterevidence=`section 5 Discussion and Conclusion (§5 Discussion and Conclusion)`。

Trade-off / failure：新增 controller、metadata、verification、communication 或 runtime state 都带来成本；只在 exact-v1 披露 workload/evaluator 内成立，未披露的硬件、精度、长度、batch、并发、SLO、seed 与 artifact commit 为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-17172:start -->只支持 exact-v1 披露设置中的机制与结果；旧路径在新增 owner/证据/控制责任不成立时继续共存。<!-- claim:SF-2026-ARXIV-2605-17172:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-17172:end -->

<!-- review:SF-2026-ARXIV-2605-17173:start -->
#### Why Do Safety Guardrails Degrade Across Languages?

问题与机制：Why Do Safety Guardrails Degrade Across Languages? 提出的具体变化是：We introduce a latent variable model, a Multi-Group Item Response Theory (IRT) framework, that decouples language-agnostic safety robustness ($θ$), intrinsic prompt hardness ($β$), global language processing difficulty ($γ$), and a prompt-specific cross-lingual safety gap ($τ$). 摘要中的长期系统挑战为：multilingual safety evaluation must decompose the failure factors hidden by aggregate jailbreak rate。它可能改变 `PLATFORM-EVALUATION-SYSTEM` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“Our framework reveals concept-language vulnerabilities that aggregate metrics obscure, enabling fairer cross-lingual safety evaluation and targeted improvements in dataset construction.”暂不作为最终证据。

Evaluation contract：Our framework reveals concept-language vulnerabilities that aggregate metrics obscure, enabling fairer cross-lingual safety evaluation and targeted improvements in dataset construction.

Evidence locators：Method=`section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt)`；Evaluation=`Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only`；Counterevidence=`Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup`。

Trade-off / failure：新增 controller、metadata、verification、communication 或 runtime state 都带来成本；只在 exact-v1 披露 workload/evaluator 内成立，未披露的硬件、精度、长度、batch、并发、SLO、seed 与 artifact commit 为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-17173:start -->只支持 exact-v1 披露设置中的机制与结果；旧路径在新增 owner/证据/控制责任不成立时继续共存。<!-- claim:SF-2026-ARXIV-2605-17173:end -->

Books Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-17173:end -->

<!-- review:SF-2026-ARXIV-2605-17193:start -->
#### Multi-LLM Systems Exhibit Robust Semantic Collapse

问题与机制：旧假设是增加 Agent、模型异质性、讨论轮数或表面采样多样性能够持续扩大搜索空间；当各 Agent 的后续 Context 反复由同一闭环中的模型输出构成时，历史不再是独立证据，而会成为递归 conditioning state。exact-v1 在作者披露的 closed-loop text simulations 中把 lexical diversity、within-run semantic displacement 与 aligned cross-run diversity 分开测量，显示词汇继续增长时语义支持仍可收缩。

Evaluation contract：三种主要模型各进行三次 1,000-round triadic run，其余干预通常使用 200 rounds、每条件三次；十二类干预覆盖 temperature、output budget、prompt、retrieval packing、model mixing、uncensored variants、activation steering、GRPO、population size、framework 与 noise。论文报告 62 个 baseline comparisons 经 Bonferroni correction 后没有正且显著的 semantic-diversity 改善。该结论绑定作者选择的模型、closed-loop scaffold、embedding model、window statistics 与 run-level clustering。

Trade-off / failure：结果支持把“独立 evidence 与外部 renewal”作为 Multi-Agent admission 条件，而不是继续增加同源对话；但它不证明开放工具环境、外部人类/数据持续注入、不同任务拓扑或所有语义度量都会 collapse。Supplementary Note 3 明确回归不构成机制或因果证明，Supplementary Note 5 也把 recursive-channel 理论作为 heuristic guide；immutable code/data commit 为 Not Disclosed。

Evidence locators：Method=`PDF section Methods; Supplementary Note 1 §§1.1–1.8; Supplementary Notes 2–3 intervention definitions`；Evaluation=`PDF section Results: Semantic Collapse in Extended Open-Ended Simulations; Semantic Collapse Resists Intervention; Diagnosing Mechanisms of Semantic Collapse; Supplementary Note 3 §3.7`；Counterevidence=`PDF section Discussion; Supplementary Note 3 §3.7 non-causal regression boundary; Supplementary Note 5 heuristic-theory and predictive-regularity boundaries`；Artifact=`official exact-v1 PDF=https://arxiv.org/pdf/2605.17193v1; bytes=4076663; sha256=edde49ce22de86ac25ad4d676f9003afec5c11513bee35438ca8db965322abe7; immutable code/data commit Not Disclosed`。

<!-- claim:SF-2026-ARXIV-2605-17193:start -->exact-v1 只支持作者 closed-loop、text-only、多模型/多轮与所列 intervention protocol 下的 semantic contraction；不支持“所有 Multi-Agent 都必然退化”，也不证明 recursive-channel explanation 为因果机制。<!-- claim:SF-2026-ARXIV-2605-17193:end -->

Books Decision=`No Change — Existing Coverage`：Ch82 已明确拥有同源 Agent 的 correlated error、证据独立性、趋同风险、coordination tax 与 single-Agent / independent verifier fallback；该论文强化现有判断，但没有新增独立状态 owner 或控制机制。
<!-- review:SF-2026-ARXIV-2605-17193:end -->

<!-- review:SF-2026-ARXIV-2605-19373:start -->
#### Conflict-Free Replicated Data Types for Neural Network Model Merging: A Two-Layer Architecture Enabling CRDT-Compliant Model Merging Across 26 Strategies

问题与机制：Conflict-Free Replicated Data Types for Neural Network Model Merging: A Two-Layer Architecture Enabling CRDT-Compliant Model Merging Across 26 Strategies 提出的具体变化是：To resolve this, we present a two-layer architecture -- CRDTMergeState -- that wraps any merge strategy in a CRDT-compliant (Conflict-Free Replicated Data Type) layer. 摘要中的长期系统挑战为：distributed model merging requires a conflict-free state wrapper because weight merges are not CRDT operations。它可能改变 `PLATFORM-MODEL-REGISTRY` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“We prove that this separation guarantees Strong Eventual Consistency: all replicas receiving the same contributions compute identical merged models, regardless of message ordering.”暂不作为最终证据。

Evaluation contract：The reference implementation is available as crdt-merge v0.9.4.

Evidence locators：Method=`section 4 The Solution: Two-Layer Architecture (§4 The Solution: Two-Layer Architecture)`；Evaluation=`section 3.1 Formal Analysis of CRDT Property Violations (§3.1 Formal Analysis of CRDT Property Violations)`；Counterevidence=`section 7 Discussion (§7 Discussion)`。

Trade-off / failure：新增 controller、metadata、verification、communication 或 runtime state 都带来成本；只在 exact-v1 披露 workload/evaluator 内成立，未披露的硬件、精度、长度、batch、并发、SLO、seed 与 artifact commit 为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-19373:start -->只支持 exact-v1 披露设置中的机制与结果；旧路径在新增 owner/证据/控制责任不成立时继续共存。<!-- claim:SF-2026-ARXIV-2605-19373:end -->

Books Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-19373:end -->

<!-- review:SF-2026-ARXIV-2605-22850:start -->
#### ObjectCache: Layerwise Object-Storage Retrieval for KV Cache Reuse

问题与机制：ObjectCache: Layerwise Object-Storage Retrieval for KV Cache Reuse 提出的具体变化是：We propose ObjectCache, which co-designs the storage protocol and transfer schedule so that the storage server delivers KV cache data in the order the GPU consumes it, overlapping data transfer with compute across concurrent requests. 摘要中的长期系统挑战为：prefix KV reuse crosses local memory into layerwise object-store retrieval with explicit object identity。它可能改变 `INFER-KV-CACHE` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“Under shared bandwidth caps, our scheduler reduces added TTFT by 1.2--1.8x compared with equal bandwidth sharing.”暂不作为最终证据。

Evaluation contract：Under shared bandwidth caps, our scheduler reduces added TTFT by 1.2--1.8x compared with equal bandwidth sharing.

Evidence locators：Method=`section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt)`；Evaluation=`Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only`；Counterevidence=`Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup`。

Trade-off / failure：新增 controller、metadata、verification、communication 或 runtime state 都带来成本；只在 exact-v1 披露 workload/evaluator 内成立，未披露的硬件、精度、长度、batch、并发、SLO、seed 与 artifact commit 为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-22850:start -->只支持 exact-v1 披露设置中的机制与结果；旧路径在新增 owner/证据/控制责任不成立时继续共存。<!-- claim:SF-2026-ARXIV-2605-22850:end -->

Books Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-22850:end -->

<!-- review:SF-2026-ARXIV-2605-23986:start -->
#### MemForest: An Efficient Agent Memory System with Hierarchical Temporal Indexing

问题与机制：MemForest: An Efficient Agent Memory System with Hierarchical Temporal Indexing 提出的具体变化是：To address these challenges, we present MemForest, a memory framework that reformulates agent memory as a write-efficient temporal data-management problem. 摘要中的长期系统挑战为：hierarchical temporal indexing removes state-dependent generation from the memory write critical path。它可能改变 `AGENT-MEMORY` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“These results show that MemForest reduces memory-freshness latency while retaining strong answer quality.”暂不作为最终证据。

Evaluation contract：These results show that MemForest reduces memory-freshness latency while retaining strong answer quality.

Evidence locators：Method=`section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt)`；Evaluation=`Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only`；Counterevidence=`Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup`。

Trade-off / failure：新增 controller、metadata、verification、communication 或 runtime state 都带来成本；只在 exact-v1 披露 workload/evaluator 内成立，未披露的硬件、精度、长度、batch、并发、SLO、seed 与 artifact commit 为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-23986:start -->只支持 exact-v1 披露设置中的机制与结果；旧路径在新增 owner/证据/控制责任不成立时继续共存。<!-- claim:SF-2026-ARXIV-2605-23986:end -->

Books Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-23986:end -->

## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

作者 headline 不外推；未在 exact-v1 明确披露的字段保持 Not Disclosed。

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-16745 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | 完整 Source Review 已完成或被精确 blocker 冻结；Top-3 不改变审计义务 | analysis-decision:SF-2026-ARXIV-2605-16745 |
| SF-2026-ARXIV-2605-16746 | score_7_9 | not_selected | — | — | 完整 Source Review 已完成或被精确 blocker 冻结；Top-3 不改变审计义务 | analysis-decision:SF-2026-ARXIV-2605-16746 |
| SF-2026-ARXIV-2605-16776 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | 完整 Source Review 已完成或被精确 blocker 冻结；Top-3 不改变审计义务 | analysis-decision:SF-2026-ARXIV-2605-16776 |
| SF-2026-ARXIV-2605-16786 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | 完整 Source Review 已完成或被精确 blocker 冻结；Top-3 不改变审计义务 | analysis-decision:SF-2026-ARXIV-2605-16786 |
| SF-2026-ARXIV-2605-16787 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | 完整 Source Review 已完成或被精确 blocker 冻结；Top-3 不改变审计义务 | analysis-decision:SF-2026-ARXIV-2605-16787 |
| SF-2026-ARXIV-2605-16790 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | 完整 Source Review 已完成或被精确 blocker 冻结；Top-3 不改变审计义务 | analysis-decision:SF-2026-ARXIV-2605-16790 |
| SF-2026-ARXIV-2605-16819 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | 完整 Source Review 已完成或被精确 blocker 冻结；Top-3 不改变审计义务 | analysis-decision:SF-2026-ARXIV-2605-16819 |
| SF-2026-ARXIV-2605-16826 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | 完整 Source Review 已完成或被精确 blocker 冻结；Top-3 不改变审计义务 | analysis-decision:SF-2026-ARXIV-2605-16826 |
| SF-2026-ARXIV-2605-16839 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | 完整 Source Review 已完成或被精确 blocker 冻结；Top-3 不改变审计义务 | analysis-decision:SF-2026-ARXIV-2605-16839 |
| SF-2026-ARXIV-2605-16867 | score_7_9 | not_selected | — | — | 完整 Source Review 已完成或被精确 blocker 冻结；Top-3 不改变审计义务 | analysis-decision:SF-2026-ARXIV-2605-16867 |
| SF-2026-ARXIV-2605-16928 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | 完整 Source Review 已完成或被精确 blocker 冻结；Top-3 不改变审计义务 | analysis-decision:SF-2026-ARXIV-2605-16928 |
| SF-2026-ARXIV-2605-16976 | score_7_9;forced_review;potential_books_delta | selected | DA-INTENT-EFFECT | — | 跨层持久状态或安全 effect commit 变化最强 | analysis:DA-INTENT-EFFECT |
| SF-2026-ARXIV-2605-16986 | score_7_9 | not_selected | — | — | 完整 Source Review 已完成或被精确 blocker 冻结；Top-3 不改变审计义务 | analysis-decision:SF-2026-ARXIV-2605-16986 |
| SF-2026-ARXIV-2605-17003 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | 完整 Source Review 已完成或被精确 blocker 冻结；Top-3 不改变审计义务 | analysis-decision:SF-2026-ARXIV-2605-17003 |
| SF-2026-ARXIV-2605-17026 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | 完整 Source Review 已完成或被精确 blocker 冻结；Top-3 不改变审计义务 | analysis-decision:SF-2026-ARXIV-2605-17026 |
| SF-2026-ARXIV-2605-17028 | score_7_9 | not_selected | — | — | 完整 Source Review 已完成或被精确 blocker 冻结；Top-3 不改变审计义务 | analysis-decision:SF-2026-ARXIV-2605-17028 |
| SF-2026-ARXIV-2605-17034 | score_7_9 | not_selected | — | — | 完整 Source Review 已完成或被精确 blocker 冻结；Top-3 不改变审计义务 | analysis-decision:SF-2026-ARXIV-2605-17034 |
| SF-2026-ARXIV-2605-17062 | score_7_9 | not_selected | — | — | 完整 Source Review 已完成或被精确 blocker 冻结；Top-3 不改变审计义务 | analysis-decision:SF-2026-ARXIV-2605-17062 |
| SF-2026-ARXIV-2605-17076 | score_7_9;forced_review;potential_books_delta | selected | DA-SHARED-STATE | — | 跨层持久状态或安全 effect commit 变化最强 | analysis:DA-SHARED-STATE |
| SF-2026-ARXIV-2605-17106 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | 完整 Source Review 已完成或被精确 blocker 冻结；Top-3 不改变审计义务 | analysis-decision:SF-2026-ARXIV-2605-17106 |
| SF-2026-ARXIV-2605-17113 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | 完整 Source Review 已完成或被精确 blocker 冻结；Top-3 不改变审计义务 | analysis-decision:SF-2026-ARXIV-2605-17113 |
| SF-2026-ARXIV-2605-17160 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | 完整 Source Review 已完成或被精确 blocker 冻结；Top-3 不改变审计义务 | analysis-decision:SF-2026-ARXIV-2605-17160 |
| SF-2026-ARXIV-2605-17164 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | 完整 Source Review 已完成或被精确 blocker 冻结；Top-3 不改变审计义务 | analysis-decision:SF-2026-ARXIV-2605-17164 |
| SF-2026-ARXIV-2605-17169 | score_7_9 | not_selected | — | — | 完整 Source Review 已完成或被精确 blocker 冻结；Top-3 不改变审计义务 | analysis-decision:SF-2026-ARXIV-2605-17169 |
| SF-2026-ARXIV-2605-17170 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | 完整 Source Review 已完成或被精确 blocker 冻结；Top-3 不改变审计义务 | analysis-decision:SF-2026-ARXIV-2605-17170 |
| SF-2026-ARXIV-2605-17172 | score_7_9 | not_selected | — | — | 完整 Source Review 已完成或被精确 blocker 冻结；Top-3 不改变审计义务 | analysis-decision:SF-2026-ARXIV-2605-17172 |
| SF-2026-ARXIV-2605-17173 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | 完整 Source Review 已完成或被精确 blocker 冻结；Top-3 不改变审计义务 | analysis-decision:SF-2026-ARXIV-2605-17173 |
| SF-2026-ARXIV-2605-17193 | score_7_9 | not_selected | — | — | exact-v1 Review 已恢复并完成；Top-3 不改变审计义务，且 current Books comparison 判定 No Change | analysis-decision:SF-2026-ARXIV-2605-17193 |
| SF-2026-ARXIV-2605-19373 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | 完整 Source Review 已完成或被精确 blocker 冻结；Top-3 不改变审计义务 | analysis-decision:SF-2026-ARXIV-2605-19373 |
| SF-2026-ARXIV-2605-22850 | score_7_9;forced_review;potential_books_delta | selected | DA-OBJECT-KV | — | 跨层持久状态或安全 effect commit 变化最强 | analysis:DA-OBJECT-KV |
| SF-2026-ARXIV-2605-23986 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | 完整 Source Review 已完成或被精确 blocker 冻结；Top-3 不改变审计义务 | analysis-decision:SF-2026-ARXIV-2605-23986 |

<!-- analysis:DA-SHARED-STATE:start -->### Multi-Agent shared state：从 last-write-wins 到 observable-read isolation

独立 Agent 在私有状态上工作时无需全局一致性；共享可变 workspace 会出现 silent overwrite 与 stale read。S-Bus 重建 read set、记录 observable dependency，再由 coordination bus 控制可见写入。收益是把一致性从 prompt 约定提升为 runtime contract；代价是 dependency tracking、串行化热点和错误 read-set。低并发或无共享 side effect 时旧路径仍成立。<!-- analysis:DA-SHARED-STATE:end -->

<!-- analysis:DA-OBJECT-KV:start -->### KV reuse：从本机 prefix cache 到 layerwise object identity

内存内复用简单但容量和节点生命周期受限；ObjectCache 把各层 KV 作为可检索对象放入 object storage，并按 layer/prefix identity 流式恢复。收益是跨请求/节点扩展复用；代价是对象索引、远端 I/O、版本兼容和 miss fallback。热前缀与低延迟场景仍应保留本地 cache。<!-- analysis:DA-OBJECT-KV:end -->

<!-- analysis:DA-INTENT-EFFECT:start -->### Agent security：从 intent classification 到 intent–execution binding

只判断 prompt 是否恶意，不能证明最终 tool call 与用户意图一致。Intent-to-execution integrity 需要保存任务意图、解析后的 capability、参数、effect 与 approval receipt，再在执行前比对。收益是阻止语义漂移取得副作用 authority；代价是 intent parser false positive/negative、交互成本和版本化 policy。无法可靠解析时回退最小权限与人工批准。<!-- analysis:DA-INTENT-EFFECT:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-16745:start -->该 family 已完成独立 Review 或精确 blocker 冻结；未进入 Top-3 不等于未审计。<!-- analysis-decision:SF-2026-ARXIV-2605-16745:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-16746:start -->该 family 已完成独立 Review 或精确 blocker 冻结；未进入 Top-3 不等于未审计。<!-- analysis-decision:SF-2026-ARXIV-2605-16746:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-16776:start -->该 family 已完成独立 Review 或精确 blocker 冻结；未进入 Top-3 不等于未审计。<!-- analysis-decision:SF-2026-ARXIV-2605-16776:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-16786:start -->该 family 已完成独立 Review 或精确 blocker 冻结；未进入 Top-3 不等于未审计。<!-- analysis-decision:SF-2026-ARXIV-2605-16786:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-16787:start -->该 family 已完成独立 Review 或精确 blocker 冻结；未进入 Top-3 不等于未审计。<!-- analysis-decision:SF-2026-ARXIV-2605-16787:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-16790:start -->该 family 已完成独立 Review 或精确 blocker 冻结；未进入 Top-3 不等于未审计。<!-- analysis-decision:SF-2026-ARXIV-2605-16790:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-16819:start -->该 family 已完成独立 Review 或精确 blocker 冻结；未进入 Top-3 不等于未审计。<!-- analysis-decision:SF-2026-ARXIV-2605-16819:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-16826:start -->该 family 已完成独立 Review 或精确 blocker 冻结；未进入 Top-3 不等于未审计。<!-- analysis-decision:SF-2026-ARXIV-2605-16826:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-16839:start -->该 family 已完成独立 Review 或精确 blocker 冻结；未进入 Top-3 不等于未审计。<!-- analysis-decision:SF-2026-ARXIV-2605-16839:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-16867:start -->该 family 已完成独立 Review 或精确 blocker 冻结；未进入 Top-3 不等于未审计。<!-- analysis-decision:SF-2026-ARXIV-2605-16867:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-16928:start -->该 family 已完成独立 Review 或精确 blocker 冻结；未进入 Top-3 不等于未审计。<!-- analysis-decision:SF-2026-ARXIV-2605-16928:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-16986:start -->该 family 已完成独立 Review 或精确 blocker 冻结；未进入 Top-3 不等于未审计。<!-- analysis-decision:SF-2026-ARXIV-2605-16986:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17003:start -->该 family 已完成独立 Review 或精确 blocker 冻结；未进入 Top-3 不等于未审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17003:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17026:start -->该 family 已完成独立 Review 或精确 blocker 冻结；未进入 Top-3 不等于未审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17026:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17028:start -->该 family 已完成独立 Review 或精确 blocker 冻结；未进入 Top-3 不等于未审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17028:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17034:start -->该 family 已完成独立 Review 或精确 blocker 冻结；未进入 Top-3 不等于未审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17034:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17062:start -->该 family 已完成独立 Review 或精确 blocker 冻结；未进入 Top-3 不等于未审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17062:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17106:start -->该 family 已完成独立 Review 或精确 blocker 冻结；未进入 Top-3 不等于未审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17106:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17113:start -->该 family 已完成独立 Review 或精确 blocker 冻结；未进入 Top-3 不等于未审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17113:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17160:start -->该 family 已完成独立 Review 或精确 blocker 冻结；未进入 Top-3 不等于未审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17160:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17164:start -->该 family 已完成独立 Review 或精确 blocker 冻结；未进入 Top-3 不等于未审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17164:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17169:start -->该 family 已完成独立 Review 或精确 blocker 冻结；未进入 Top-3 不等于未审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17169:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17170:start -->该 family 已完成独立 Review 或精确 blocker 冻结；未进入 Top-3 不等于未审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17170:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17172:start -->该 family 已完成独立 Review 或精确 blocker 冻结；未进入 Top-3 不等于未审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17172:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17173:start -->该 family 已完成独立 Review 或精确 blocker 冻结；未进入 Top-3 不等于未审计。<!-- analysis-decision:SF-2026-ARXIV-2605-17173:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17193:start -->该 family 已完成 exact-v1 Review 与 current Books challenge；未进入 Top-3 不等于未审计，No Change 也不等于低分。<!-- analysis-decision:SF-2026-ARXIV-2605-17193:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-19373:start -->该 family 已完成独立 Review 或精确 blocker 冻结；未进入 Top-3 不等于未审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19373:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-23986:start -->该 family 已完成独立 Review 或精确 blocker 冻结；未进入 Top-3 不等于未审计。<!-- analysis-decision:SF-2026-ARXIV-2605-23986:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-16745 | MULTIMODAL-REPRESENTATION | books/part-03-multimodal-world-models/23-multimodal-representation.md#chapter-23 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24 | existing:SF-2026-ARXIV-2605-16745 | delta:SF-2026-ARXIV-2605-16745 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-16745 |
| SF-2026-ARXIV-2605-16746 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76; books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-16746 | delta:SF-2026-ARXIV-2605-16746 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16746 |
| SF-2026-ARXIV-2605-16776 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-16776 | delta:SF-2026-ARXIV-2605-16776 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-16776 |
| SF-2026-ARXIV-2605-16786 | INFER-SPECULATIVE-DECODING | books/part-05-inference-system/48-speculative-decoding.md#chapter-48 | books/part-05-inference-system/47-pagedattention.md#chapter-47; books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | existing:SF-2026-ARXIV-2605-16786 | delta:SF-2026-ARXIV-2605-16786 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-16786 |
| SF-2026-ARXIV-2605-16787 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#chapter-33 | books/part-04-training-system/32-ppo.md#chapter-32; books/part-04-training-system/34-dpo.md#chapter-34 | existing:SF-2026-ARXIV-2605-16787 | delta:SF-2026-ARXIV-2605-16787 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-16787 |
| SF-2026-ARXIV-2605-16790 | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#chapter-78 | books/part-07-agent/77-memory.md#chapter-77; books/part-07-agent/79-planning.md#chapter-79 | existing:SF-2026-ARXIV-2605-16790 | delta:SF-2026-ARXIV-2605-16790 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-16790 |
| SF-2026-ARXIV-2605-16819 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-16819 | delta:SF-2026-ARXIV-2605-16819 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-16819 |
| SF-2026-ARXIV-2605-16826 | TRAIN-PRETRAINING | books/part-04-training-system/28-pretraining.md#chapter-28 | books/part-04-training-system/27-data.md#chapter-27; books/part-04-training-system/29-sft.md#chapter-29 | existing:SF-2026-ARXIV-2605-16826 | delta:SF-2026-ARXIV-2605-16826 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-16826 |
| SF-2026-ARXIV-2605-16839 | INFER-PREFILL | books/part-05-inference-system/43-prefill.md#chapter-43 | books/part-05-inference-system/42-what-happens-during-inference.md#chapter-42; books/part-05-inference-system/44-decode.md#chapter-44 | existing:SF-2026-ARXIV-2605-16839 | delta:SF-2026-ARXIV-2605-16839 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-16839 |
| SF-2026-ARXIV-2605-16867 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#chapter-56 | books/part-05-inference-system/55-pd-disaggregation.md#chapter-55 | existing:SF-2026-ARXIV-2605-16867 | delta:SF-2026-ARXIV-2605-16867 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16867 |
| SF-2026-ARXIV-2605-16928 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#chapter-45 | books/part-05-inference-system/44-decode.md#chapter-44; books/part-05-inference-system/46-continuous-batching.md#chapter-46 | existing:SF-2026-ARXIV-2605-16928 | delta:SF-2026-ARXIV-2605-16928 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-16928 |
| SF-2026-ARXIV-2605-16976 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-16976 | delta:SF-2026-ARXIV-2605-16976 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-16976 |
| SF-2026-ARXIV-2605-16986 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-16986 | delta:SF-2026-ARXIV-2605-16986 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16986 |
| SF-2026-ARXIV-2605-17003 | TRAIN-DATA | books/part-04-training-system/27-data.md#chapter-27 | books/part-04-training-system/28-pretraining.md#chapter-28 | existing:SF-2026-ARXIV-2605-17003 | delta:SF-2026-ARXIV-2605-17003 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-17003 |
| SF-2026-ARXIV-2605-17026 | TRAIN-DATA | books/part-04-training-system/27-data.md#chapter-27 | books/part-04-training-system/28-pretraining.md#chapter-28 | existing:SF-2026-ARXIV-2605-17026 | delta:SF-2026-ARXIV-2605-17026 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-17026 |
| SF-2026-ARXIV-2605-17028 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-17028 | delta:SF-2026-ARXIV-2605-17028 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17028 |
| SF-2026-ARXIV-2605-17034 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-17034 | delta:SF-2026-ARXIV-2605-17034 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17034 |
| SF-2026-ARXIV-2605-17062 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-17062 | delta:SF-2026-ARXIV-2605-17062 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17062 |
| SF-2026-ARXIV-2605-17076 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#chapter-82 | books/part-07-agent/81-workflow.md#chapter-81; books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-17076 | delta:SF-2026-ARXIV-2605-17076 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-17076 |
| SF-2026-ARXIV-2605-17106 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#chapter-56 | books/part-05-inference-system/55-pd-disaggregation.md#chapter-55 | existing:SF-2026-ARXIV-2605-17106 | delta:SF-2026-ARXIV-2605-17106 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-17106 |
| SF-2026-ARXIV-2605-17113 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-17113 | delta:SF-2026-ARXIV-2605-17113 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-17113 |
| SF-2026-ARXIV-2605-17160 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | books/part-05-inference-system/48-speculative-decoding.md#chapter-48; books/part-05-inference-system/50-vllm.md#chapter-50 | existing:SF-2026-ARXIV-2605-17160 | delta:SF-2026-ARXIV-2605-17160 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-17160 |
| SF-2026-ARXIV-2605-17164 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-17164 | delta:SF-2026-ARXIV-2605-17164 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-17164 |
| SF-2026-ARXIV-2605-17169 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-17169 | delta:SF-2026-ARXIV-2605-17169 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17169 |
| SF-2026-ARXIV-2605-17170 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#chapter-45 | books/part-05-inference-system/44-decode.md#chapter-44; books/part-05-inference-system/46-continuous-batching.md#chapter-46 | existing:SF-2026-ARXIV-2605-17170 | delta:SF-2026-ARXIV-2605-17170 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-17170 |
| SF-2026-ARXIV-2605-17172 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-17172 | delta:SF-2026-ARXIV-2605-17172 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17172 |
| SF-2026-ARXIV-2605-17173 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-17173 | delta:SF-2026-ARXIV-2605-17173 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-17173 |
| SF-2026-ARXIV-2605-17193 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#chapter-82 | books/part-07-agent/81-workflow.md#chapter-81; books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-17193 | delta:SF-2026-ARXIV-2605-17193 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17193 |
| SF-2026-ARXIV-2605-19373 | PLATFORM-MODEL-REGISTRY | books/part-06-ai-infrastructure/59-model-registry.md#chapter-59 | books/part-06-ai-infrastructure/58-kubeflow.md#chapter-58; books/part-06-ai-infrastructure/60-training-operator.md#chapter-60 | existing:SF-2026-ARXIV-2605-19373 | delta:SF-2026-ARXIV-2605-19373 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19373 |
| SF-2026-ARXIV-2605-22850 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#chapter-45 | books/part-05-inference-system/44-decode.md#chapter-44; books/part-05-inference-system/46-continuous-batching.md#chapter-46 | existing:SF-2026-ARXIV-2605-22850 | delta:SF-2026-ARXIV-2605-22850 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-22850 |
| SF-2026-ARXIV-2605-23986 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76; books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-23986 | delta:SF-2026-ARXIV-2605-23986 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-23986 |

<!-- books-review:SF-2026-ARXIV-2605-16745:start -->
<!-- existing:SF-2026-ARXIV-2605-16745:start -->已逐章读取 `books/part-03-multimodal-world-models/23-multimodal-representation.md` 与相邻章节 ['books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md']；当前正文拥有 surrounding principle，但尚未显式承载 `EVA01: Unified Native 3D Understanding and Generation via Mixture-of-Transformers` 改变的 state/data/control/evidence boundary。 owner_sha256=cde0ccfed7241f74e706727568f977cfe98384d75b2483b4c57eedc44fa486c4。<!-- existing:SF-2026-ARXIV-2605-16745:end -->
<!-- delta:SF-2026-ARXIV-2605-16745:start -->EVA01: Unified Native 3D Understanding and Generation via Mixture-of-Transformers 提出的具体变化是：We introduce EVA01, a unified framework that extends the modality boundary of MLLMs to natively incorporate 3D mesh understanding, generation, and context-aware editing. 摘要中的长期系统挑战为：native 3D tokens join understanding and generation rather than remaining a stateless reconstruction sidecar。它可能改变 `MULTIMODAL-REPRESENTATION` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“Results show that EVA01 achieves state-of-the-art native text-to-3D generation fidelity and unlocks robust long-context multi-turn geometric editing with identity preservation, a capability fundamentally inaccessible to stateless reconstruction pipelines.”暂不作为最终证据。<!-- delta:SF-2026-ARXIV-2605-16745:end --> Decision=`Integrate`；non-author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-16745:end -->
<!-- books-review:SF-2026-ARXIV-2605-16746:start -->
<!-- existing:SF-2026-ARXIV-2605-16746:start -->`books/part-07-agent/77-memory.md` 已以更一般的 `AGENT-MEMORY` 演进链承载该问题的 owner、commit/evidence boundary、failure fallback 与旧路径共存；本 family 只增加受限实现或 benchmark evidence。 owner_sha256=ac3bf5ab49bb87bcf3f0cfa1da47486caeb35e9d451251f91c67caf3bc9de6d7。<!-- existing:SF-2026-ARXIV-2605-16746:end -->
<!-- delta:SF-2026-ARXIV-2605-16746:start -->State Contamination in Memory-Augmented LLM Agents 提出的具体变化是：To measure this hidden influence, we introduce the sub-threshold propagation gap (SPG), which quantifies downstream behavioral differences conditioned on memory states that a deployed monitor would classify as safe. 摘要中的长期系统挑战为：persistent memory becomes a cross-turn attack surface whose writes and reuse require separate authority。它可能改变 `AGENT-MEMORY` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“These results suggest that safety in memory-augmented agents should be treated as a state-control problem over evolving context, with sanitization applied before unsafe information is compressed into persistent memory.”暂不作为最终证据。<!-- delta:SF-2026-ARXIV-2605-16746:end --> Decision=`No Change — Existing Coverage`；non-author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-16746:end -->
<!-- books-review:SF-2026-ARXIV-2605-16776:start -->
<!-- existing:SF-2026-ARXIV-2605-16776:start -->已逐章读取 `books/part-06-ai-infrastructure/72-security.md` 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；当前正文拥有 surrounding principle，但尚未显式承载 `Distinguishable Deletion: Unifying Knowledge Erasure and Refusal for Large Language Model Unlearning` 改变的 state/data/control/evidence boundary。 owner_sha256=b4a3cdb8a1a37d72b85afa4def5d2fd3756d9432a2a7ddd0c60732f5bdbf9c1d。<!-- existing:SF-2026-ARXIV-2605-16776:end -->
<!-- delta:SF-2026-ARXIV-2605-16776:start -->Distinguishable Deletion: Unifying Knowledge Erasure and Refusal for Large Language Model Unlearning 提出的具体变化是：To address these issues, we propose Distinguishable Deletion ($\mathrm{D^2}$), a paradigm that restricts the response distribution in the latent representation rather than specific tokens to erase undesirable knowledge, while distinguishing it from retained knowledge, enabling a refusal mechanism to handle unlearned inputs safely and coherently. 摘要中的长期系统挑战为：unlearning must distinguish parameter erasure from inference-time refusal and verify both contracts。它可能改变 `PLATFORM-SECURITY` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“Extensive experiments demonstrate that EUA significantly outperforms previous methods, indicating the superiority of $\mathrm{D^2}$.”暂不作为最终证据。<!-- delta:SF-2026-ARXIV-2605-16776:end --> Decision=`Integrate`；non-author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-16776:end -->
<!-- books-review:SF-2026-ARXIV-2605-16786:start -->
<!-- existing:SF-2026-ARXIV-2605-16786:start -->已逐章读取 `books/part-05-inference-system/48-speculative-decoding.md` 与相邻章节 ['books/part-05-inference-system/47-pagedattention.md', 'books/part-05-inference-system/49-tensorrt-llm.md']；当前正文拥有 surrounding principle，但尚未显式承载 `Lever: Speculative LLM Inference on Smartphones` 改变的 state/data/control/evidence boundary。 owner_sha256=6e03731cbbf82d3455fb4df123c710eee96e98d84d4c80680ad56e47c9b84dc3。<!-- existing:SF-2026-ARXIV-2605-16786:end -->
<!-- delta:SF-2026-ARXIV-2605-16786:start -->Lever: Speculative LLM Inference on Smartphones 提出的具体变化是：We present Lever, an end-to-end system for efficient flash-backed LLM inference on smartphones. 摘要中的长期系统挑战为：flash-backed mobile inference changes the draft/verify cost model and state-placement boundary。它可能改变 `INFER-SPECULATIVE-DECODING` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“We observe that speculative decoding is a natural fit for this setting: a small draft model can remain in DRAM, while a larger flash-resident target model verifies multiple candidate tokens per invocation.”暂不作为最终证据。<!-- delta:SF-2026-ARXIV-2605-16786:end --> Decision=`Integrate`；non-author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-16786:end -->
<!-- books-review:SF-2026-ARXIV-2605-16787:start -->
<!-- existing:SF-2026-ARXIV-2605-16787:start -->已逐章读取 `books/part-04-training-system/33-grpo.md` 与相邻章节 ['books/part-04-training-system/32-ppo.md', 'books/part-04-training-system/34-dpo.md']；当前正文拥有 surrounding principle，但尚未显式承载 `The Unlearnability Phenomenon in RLVR for Language Models` 改变的 state/data/control/evidence boundary。 owner_sha256=c75d66bc18a9221e70da0fc29018962765e69241af2ce0959becf0ab5f8e49a8。<!-- existing:SF-2026-ARXIV-2605-16787:end -->
<!-- delta:SF-2026-ARXIV-2605-16787:start -->The Unlearnability Phenomenon in RLVR for Language Models 提出的具体变化是：Reinforcement Learning with Verifiable Reward (RLVR) has proven effective in improving Large Language Model's (LLM) reasoning ability. 摘要中的长期系统挑战为：RLVR admission must recognize examples with no useful policy-gradient direction rather than treating all verified rewards alike。它可能改变 `TRAIN-GRPO` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“With cross-example gradient analysis, we show that unlearnable examples have fundamental representation issue, characterized by low gradient similarity with the rest of the examples and ungeneralizable reasoning patterns.”暂不作为最终证据。<!-- delta:SF-2026-ARXIV-2605-16787:end --> Decision=`Integrate`；non-author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-16787:end -->
<!-- books-review:SF-2026-ARXIV-2605-16790:start -->
<!-- existing:SF-2026-ARXIV-2605-16790:start -->已逐章读取 `books/part-07-agent/78-tool-calling.md` 与相邻章节 ['books/part-07-agent/77-memory.md', 'books/part-07-agent/79-planning.md']；当前正文拥有 surrounding principle，但尚未显式承载 `TIER: Trajectory-Invariant Execution Rewards for Multi-Step Tool Composition` 改变的 state/data/control/evidence boundary。 owner_sha256=73f2708a56d1c3852ff08cba8240fd7021f192a4778636a241608de26bbbb2e4。<!-- existing:SF-2026-ARXIV-2605-16790:end -->
<!-- delta:SF-2026-ARXIV-2605-16790:start -->TIER: Trajectory-Invariant Execution Rewards for Multi-Step Tool Composition 提出的具体变化是：We propose TIER: Trajectory-Invariant Execution Rewards, a reward framework that derives supervision directly from function schemas and runtime execution, rather than from reference trajectories. 摘要中的长期系统挑战为：tool-composition reward moves from reference trajectories to invariant execution-state evidence。它可能改变 `AGENT-TOOL-CALLING` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“Ablation studies confirm that all reward components are necessary, highlighting the importance of multi-level supervision for compositional reasoning.”暂不作为最终证据。<!-- delta:SF-2026-ARXIV-2605-16790:end --> Decision=`Integrate`；non-author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-16790:end -->
<!-- books-review:SF-2026-ARXIV-2605-16819:start -->
<!-- existing:SF-2026-ARXIV-2605-16819:start -->已逐章读取 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前正文拥有 surrounding principle，但尚未显式承载 `AgentKernelArena: Generalization-Aware Benchmarking of GPU Kernel Optimization Agents` 改变的 state/data/control/evidence boundary。 owner_sha256=089fc06685d0e6238733d8b293222afd04aeacd6d35cf016f2c21fe13c9e8ef1。<!-- existing:SF-2026-ARXIV-2605-16819:end -->
<!-- delta:SF-2026-ARXIV-2605-16819:start -->AgentKernelArena: Generalization-Aware Benchmarking of GPU Kernel Optimization Agents 提出的具体变化是：We present AgentKernelArena, an open-source benchmark for measuring AI coding agents on GPU kernel optimization. 摘要中的长期系统挑战为：agent evaluation must freeze workflow state, hidden task contract, runtime receipts and unseen-shape generalization。它可能改变 `PLATFORM-EVALUATION-SYSTEM` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“AgentKernelArena is designed as a modular, extensible framework for rigorous evaluation of agentic GPU kernel optimization across agents, tasks, and hardware targets.”暂不作为最终证据。<!-- delta:SF-2026-ARXIV-2605-16819:end --> Decision=`Integrate`；non-author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-16819:end -->
<!-- books-review:SF-2026-ARXIV-2605-16826:start -->
<!-- existing:SF-2026-ARXIV-2605-16826:start -->已逐章读取 `books/part-04-training-system/28-pretraining.md` 与相邻章节 ['books/part-04-training-system/27-data.md', 'books/part-04-training-system/29-sft.md']；当前正文拥有 surrounding principle，但尚未显式承载 `Decoupling KL and Trajectories: A Unified Perspective for SFT, DAgger, Offline RL, and OPD in LLM Distillation` 改变的 state/data/control/evidence boundary。 owner_sha256=0eca9f709aa5037490fd8ccf36118c63b0a7a18c7abb5e68100e8b89473faf65。<!-- existing:SF-2026-ARXIV-2605-16826:end -->
<!-- delta:SF-2026-ARXIV-2605-16826:start -->Decoupling KL and Trajectories: A Unified Perspective for SFT, DAgger, Offline RL, and OPD in LLM Distillation 提出的具体变化是：Motivated by these findings, we propose KL mixing and an entropy-gated length curriculum. 摘要中的长期系统挑战为：distillation outcomes depend separately on prefix provenance and KL direction, changing the training contract。它可能改变 `TRAIN-PRETRAINING` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“Our results provide a framework and practical methods for designing reasoning distillation objectives that balance accuracy, diversity, compute, and RL behavior.”暂不作为最终证据。<!-- delta:SF-2026-ARXIV-2605-16826:end --> Decision=`Integrate`；non-author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-16826:end -->
<!-- books-review:SF-2026-ARXIV-2605-16839:start -->
<!-- existing:SF-2026-ARXIV-2605-16839:start -->已逐章读取 `books/part-05-inference-system/43-prefill.md` 与相邻章节 ['books/part-05-inference-system/42-what-happens-during-inference.md', 'books/part-05-inference-system/44-decode.md']；当前正文拥有 surrounding principle，但尚未显式承载 `CompactAttention: Accelerating Chunked Prefill with Block-Union KV Selection` 改变的 state/data/control/evidence boundary。 owner_sha256=dc847cff021d99b03c0e59549275c3564437e632f8614a227ef9be66a999076d。<!-- existing:SF-2026-ARXIV-2605-16839:end -->
<!-- delta:SF-2026-ARXIV-2605-16839:start -->CompactAttention: Accelerating Chunked Prefill with Block-Union KV Selection 提出的具体变化是：To address these limitations, we propose CompactAttention, a chunked-prefill attention mechanism based on Block-Union KV Selection. 摘要中的长期系统挑战为：chunked prefill reuses a union of selected KV blocks while preserving the dense attention owner。它可能改变 `INFER-PREFILL` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“On LLaMA-3.1-8B-Instruct, CompactAttention maintains accuracy close to dense attention on the RULER benchmark while delivering up to 2.72$\times$ attention speedup at 128K context length under chunked prefill.”暂不作为最终证据。<!-- delta:SF-2026-ARXIV-2605-16839:end --> Decision=`Integrate`；non-author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-16839:end -->
<!-- books-review:SF-2026-ARXIV-2605-16867:start -->
<!-- existing:SF-2026-ARXIV-2605-16867:start -->`books/part-05-inference-system/56-inference-scheduling.md` 已以更一般的 `INFER-SCHEDULING` 演进链承载该问题的 owner、commit/evidence boundary、failure fallback 与旧路径共存；本 family 只增加受限实现或 benchmark evidence。 owner_sha256=1e3e8c3dff17a6bd79b65130176926b9f10cb1e2ff5bf3e042d4ccee6c302280。<!-- existing:SF-2026-ARXIV-2605-16867:end -->
<!-- delta:SF-2026-ARXIV-2605-16867:start -->In this paper, we propose GoodServe, a goodput-optimized serving system for agentic inferences over heterogeneous resources.<!-- delta:SF-2026-ARXIV-2605-16867:end --> Decision=`No Change — Existing Coverage`；non-author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-16867:end -->
<!-- books-review:SF-2026-ARXIV-2605-16928:start -->
<!-- existing:SF-2026-ARXIV-2605-16928:start -->已逐章读取 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 与相邻章节 ['books/part-05-inference-system/44-decode.md', 'books/part-05-inference-system/46-continuous-batching.md']；当前正文拥有 surrounding principle，但尚未显式承载 `Full Attention Strikes Back: Transferring Full Attention into Sparse within Hundred Training Steps` 改变的 state/data/control/evidence boundary。 owner_sha256=94425d5fe4db0238e99350a5a0299edb408dcffcdb7b32453c76854a9dbc8e86。<!-- existing:SF-2026-ARXIV-2605-16928:end -->
<!-- delta:SF-2026-ARXIV-2605-16928:start -->Full Attention Strikes Back: Transferring Full Attention into Sparse within Hundred Training Steps 提出的具体变化是：Based on these insights, we propose RTPurbo, which retains the full KV cache only for retrieval heads and introduces a lightweight token indexer for sparse attention. 摘要中的长期系统挑战为：head-aware dense-to-sparse post-training separates candidate routing from exact attention。它可能改变 `INFER-KV-CACHE` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“These results suggest that strong sparse inference can be obtained from standard full-attention training without expensive native sparse pretraining.”暂不作为最终证据。<!-- delta:SF-2026-ARXIV-2605-16928:end --> Decision=`Integrate`；non-author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-16928:end -->
<!-- books-review:SF-2026-ARXIV-2605-16976:start -->
<!-- existing:SF-2026-ARXIV-2605-16976:start -->已逐章读取 `books/part-06-ai-infrastructure/72-security.md` 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；当前正文拥有 surrounding principle，但尚未显式承载 `Securing LLM Agents Need Intent-to-Execution Integrity` 改变的 state/data/control/evidence boundary。 owner_sha256=b4a3cdb8a1a37d72b85afa4def5d2fd3756d9432a2a7ddd0c60732f5bdbf9c1d。<!-- existing:SF-2026-ARXIV-2605-16976:end -->
<!-- delta:SF-2026-ARXIV-2605-16976:start -->Drawing on this analogy, we identify two fundamental problem sources -- untrusted data ingestion and untrusted tool execution -- and derive four integrity properties that must hold simultaneously: \emph{Tool Integrity}, \emph{Instruction Integrity}, \emph{Judgment Integrity}, and \emph{Data Flow Integrity}.<!-- delta:SF-2026-ARXIV-2605-16976:end --> Decision=`Integrate`；non-author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-16976:end -->
<!-- books-review:SF-2026-ARXIV-2605-16986:start -->
<!-- existing:SF-2026-ARXIV-2605-16986:start -->`books/part-07-agent/84-agent-platform.md` 已以更一般的 `AGENT-PLATFORM` 演进链承载该问题的 owner、commit/evidence boundary、failure fallback 与旧路径共存；本 family 只增加受限实现或 benchmark evidence。 owner_sha256=c90613b1e2cab33b382c0cff6ae0226e44b2d66b051e12a15174eae9c5fc6cdc。<!-- existing:SF-2026-ARXIV-2605-16986:end -->
<!-- delta:SF-2026-ARXIV-2605-16986:start -->Skills on the Fly: Test-Time Adaptive Skill Synthesis for LLM Agents 提出的具体变化是：We call this challenge test-time compute-to-capability conversion and propose SkillTTA, which retrieves task-relevant training trajectories and synthesizes a temporary skill conditioned on the visible target context for a solver with fixed parameters. 摘要中的长期系统挑战为：test-time skill synthesis creates ephemeral executable state that needs admission, expiry and rollback。它可能改变 `AGENT-PLATFORM` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“Across ALFWorld, SpreadsheetBench, BigCodeBench, and WebShop, SkillTTA outperforms state-of-the-art reuse and optimization baselines.”暂不作为最终证据。<!-- delta:SF-2026-ARXIV-2605-16986:end --> Decision=`No Change — Existing Coverage`；non-author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-16986:end -->
<!-- books-review:SF-2026-ARXIV-2605-17003:start -->
<!-- existing:SF-2026-ARXIV-2605-17003:start -->已逐章读取 `books/part-04-training-system/27-data.md` 与相邻章节 ['books/part-04-training-system/28-pretraining.md']；当前正文拥有 surrounding principle，但尚未显式承载 `Learning-Zone Energy: Online Data Selection for Efficient RL Post-Training` 改变的 state/data/control/evidence boundary。 owner_sha256=9e54b8820f3288dddf939ad59b0cfec8944d21573c4b03a10227688eb11a5ef1。<!-- existing:SF-2026-ARXIV-2605-17003:end -->
<!-- delta:SF-2026-ARXIV-2605-17003:start -->Learning-Zone Energy: Online Data Selection for Efficient RL Post-Training 提出的具体变化是：To address this fundamental inefficiency, we propose Learning-Zone Energy (LZE), a theoretically grounded, fully online data selection framework that concentrates computation on the model's active learning frontier. 摘要中的长期系统挑战为：online RL data selection becomes a control loop over current policy frontier rather than a static dataset。它可能改变 `TRAIN-DATA` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“Our code is available at https://github.com/Stellaris167/LZE.”暂不作为最终证据。<!-- delta:SF-2026-ARXIV-2605-17003:end --> Decision=`Integrate`；non-author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17003:end -->
<!-- books-review:SF-2026-ARXIV-2605-17026:start -->
<!-- existing:SF-2026-ARXIV-2605-17026:start -->已逐章读取 `books/part-04-training-system/27-data.md` 与相邻章节 ['books/part-04-training-system/28-pretraining.md']；当前正文拥有 surrounding principle，但尚未显式承载 `Why Do Reasoning Models Lose Coverage? The Role of Data and Forks in the Road` 改变的 state/data/control/evidence boundary。 owner_sha256=9e54b8820f3288dddf939ad59b0cfec8944d21573c4b03a10227688eb11a5ef1。<!-- existing:SF-2026-ARXIV-2605-17026:end -->
<!-- delta:SF-2026-ARXIV-2605-17026:start -->While these methods reliably improve pass@1 accuracy, prior works have observed that they show a coverage shrinkage behavior, where pass@k degrades relative to the base model.<!-- delta:SF-2026-ARXIV-2605-17026:end --> Decision=`Integrate`；non-author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17026:end -->
<!-- books-review:SF-2026-ARXIV-2605-17028:start -->
<!-- existing:SF-2026-ARXIV-2605-17028:start -->`books/part-06-ai-infrastructure/66-evaluation-system.md` 已以更一般的 `PLATFORM-EVALUATION-SYSTEM` 演进链承载该问题的 owner、commit/evidence boundary、failure fallback 与旧路径共存；本 family 只增加受限实现或 benchmark evidence。 owner_sha256=089fc06685d0e6238733d8b293222afd04aeacd6d35cf016f2c21fe13c9e8ef1。<!-- existing:SF-2026-ARXIV-2605-17028:end -->
<!-- delta:SF-2026-ARXIV-2605-17028:start -->We show, however, that much of this apparent progress does not survive scrutiny.<!-- delta:SF-2026-ARXIV-2605-17028:end --> Decision=`No Change — Existing Coverage`；non-author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17028:end -->
<!-- books-review:SF-2026-ARXIV-2605-17034:start -->
<!-- existing:SF-2026-ARXIV-2605-17034:start -->`books/part-06-ai-infrastructure/72-security.md` 已以更一般的 `PLATFORM-SECURITY` 演进链承载该问题的 owner、commit/evidence boundary、failure fallback 与旧路径共存；本 family 只增加受限实现或 benchmark evidence。 owner_sha256=b4a3cdb8a1a37d72b85afa4def5d2fd3756d9432a2a7ddd0c60732f5bdbf9c1d。<!-- existing:SF-2026-ARXIV-2605-17034:end -->
<!-- delta:SF-2026-ARXIV-2605-17034:start -->Privacy Policy Enforcement Guardrails for Data-Sensitive Retrieval-Augmented Generation 提出的具体变化是：We introduce a Privacy Policy Enforcement (PPE) framework using dual one-class density estimators with fused text embeddings and a calibrated abstain region for out-of-distribution inputs. 摘要中的长期系统挑战为：RAG privacy enforcement must mediate retrieval and generation effects rather than rely on prompt policy。它可能改变 `PLATFORM-SECURITY` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“This methodology provides a robust stress-testing standard for any synthetic-data-trained classifier.”暂不作为最终证据。<!-- delta:SF-2026-ARXIV-2605-17034:end --> Decision=`No Change — Existing Coverage`；non-author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17034:end -->
<!-- books-review:SF-2026-ARXIV-2605-17062:start -->
<!-- existing:SF-2026-ARXIV-2605-17062:start -->`books/part-06-ai-infrastructure/72-security.md` 已以更一般的 `PLATFORM-SECURITY` 演进链承载该问题的 owner、commit/evidence boundary、failure fallback 与旧路径共存；本 family 只增加受限实现或 benchmark evidence。 owner_sha256=b4a3cdb8a1a37d72b85afa4def5d2fd3756d9432a2a7ddd0c60732f5bdbf9c1d。<!-- existing:SF-2026-ARXIV-2605-17062:end -->
<!-- delta:SF-2026-ARXIV-2605-17062:start -->The Range Shrinks, the Threat Remains: Re-evaluating LLM Package Hallucinations on the 2026 Frontier-Model Cohort 提出的具体变化是：Across 199,845 paired Python and JavaScript prompts validated against PyPI and npm master lists, we measure overall hallucination rates between 4.62% (Claude Haiku 4.5) and 6.10% (GPT-5.4-mini) -- an order-of-magnitude compression of the inter-model spread observed by Spracklen, but not a retirement of the threat. 摘要中的长期系统挑战为：package hallucinations create a model-to-software-supply-chain effect path requiring independent resolution。它可能改变 `PLATFORM-SECURITY` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“We further document a Python-over-JavaScript hallucination asymmetry that inverts Spracklen's 2024 finding, identify a Haiku-below-Sonnet inversion within the Anthropic family, and observe a Jaccard-similarity peak between DeepSeek V3.2 and GPT-5.4-mini (J = 0.343) suggestive of shared training-data origins.”暂不作为最终证据。<!-- delta:SF-2026-ARXIV-2605-17062:end --> Decision=`No Change — Existing Coverage`；non-author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17062:end -->
<!-- books-review:SF-2026-ARXIV-2605-17076:start -->
<!-- existing:SF-2026-ARXIV-2605-17076:start -->已逐章读取 `books/part-07-agent/82-multi-agent.md` 与相邻章节 ['books/part-07-agent/81-workflow.md', 'books/part-07-agent/83-mcp.md']；当前正文拥有 surrounding principle，但尚未显式承载 `S-Bus: Automatic Read-Set Reconstruction for Multi-Agent LLM State Coordination` 改变的 state/data/control/evidence boundary。 owner_sha256=948a0d2dac39b1e241adb0b692a057f0b8ef5411dda794e210d733cba06fa3d3。<!-- existing:SF-2026-ARXIV-2605-17076:end -->
<!-- delta:SF-2026-ARXIV-2605-17076:start -->S-Bus: Automatic Read-Set Reconstruction for Multi-Agent LLM State Coordination 提出的具体变化是：S-Bus is an HTTP middleware whose central mechanism, a server-side DeliveryLog, reconstructs each agent's read set at commit time from observed HTTP GET traffic. 摘要中的长期系统挑战为：observable-read isolation gives shared mutable multi-agent state an explicit consistency boundary。它可能改变 `AGENT-MULTI-AGENT` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“Source code, formal proofs, harness, annotation data: https://github.com/sajjadanwar0/sbus”暂不作为最终证据。<!-- delta:SF-2026-ARXIV-2605-17076:end --> Decision=`Integrate`；non-author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17076:end -->
<!-- books-review:SF-2026-ARXIV-2605-17106:start -->
<!-- existing:SF-2026-ARXIV-2605-17106:start -->已逐章读取 `books/part-05-inference-system/56-inference-scheduling.md` 与相邻章节 ['books/part-05-inference-system/55-pd-disaggregation.md']；当前正文拥有 surrounding principle，但尚未显式承载 `HyDRA: Hybrid Dynamic Routing Architecture for Heterogeneous LLM Pools` 改变的 state/data/control/evidence boundary。 owner_sha256=1e3e8c3dff17a6bd79b65130176926b9f10cb1e2ff5bf3e042d4ccee6c302280。<!-- existing:SF-2026-ARXIV-2605-17106:end -->
<!-- delta:SF-2026-ARXIV-2605-17106:start -->HyDRA: Hybrid Dynamic Routing Architecture for Heterogeneous LLM Pools 提出的具体变化是：We present HyDRA (Hybrid Dynamic Routing Architecture), a framework that predicts fine-grained, multi-dimensional capability requirements per query and matches them against configuration-defined model profiles via shortfall matching. 摘要中的长期系统挑战为：heterogeneous model pools and routing policy become decoupled deployable revisions。它可能改变 `INFER-SCHEDULING` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“Results generalize across LiveCodeBench, BigCodeBench, and tau-bench.”暂不作为最终证据。<!-- delta:SF-2026-ARXIV-2605-17106:end --> Decision=`Integrate`；non-author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17106:end -->
<!-- books-review:SF-2026-ARXIV-2605-17113:start -->
<!-- existing:SF-2026-ARXIV-2605-17113:start -->已逐章读取 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前正文拥有 surrounding principle，但尚未显式承载 `The Point of No Return: Counterfactual Localization of Deceptive Commitment in Language-Model Reasoning` 改变的 state/data/control/evidence boundary。 owner_sha256=089fc06685d0e6238733d8b293222afd04aeacd6d35cf016f2c21fe13c9e8ef1。<!-- existing:SF-2026-ARXIV-2605-17113:end -->
<!-- delta:SF-2026-ARXIV-2605-17113:start -->We introduce counterfactual localization: for each sentence prefix in a reasoning trace, we fix the prefix, resample continuations, and estimate the probability of a deceptive outcome.<!-- delta:SF-2026-ARXIV-2605-17113:end --> Decision=`Integrate`；non-author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17113:end -->
<!-- books-review:SF-2026-ARXIV-2605-17160:start -->
<!-- existing:SF-2026-ARXIV-2605-17160:start -->已逐章读取 `books/part-05-inference-system/49-tensorrt-llm.md` 与相邻章节 ['books/part-05-inference-system/48-speculative-decoding.md', 'books/part-05-inference-system/50-vllm.md']；当前正文拥有 surrounding principle，但尚未显式承载 `When Bits Break Recourse: Counterfactual-Faithful Quantization` 改变的 state/data/control/evidence boundary。 owner_sha256=8ee7425b911361c8e1e632272a759a2ae9eb63723aeb30c1237bc304ce07fb7b。<!-- existing:SF-2026-ARXIV-2605-17160:end -->
<!-- delta:SF-2026-ARXIV-2605-17160:start -->We propose two metrics: Validity Drop (VD), which measures the fraction of full-precision recourse actions that no longer achieve the target outcome after quantization, and Counterfactual Recourse Gap (CRG), which measures the increase in minimal recourse cost under the quantized model.<!-- delta:SF-2026-ARXIV-2605-17160:end --> Decision=`Integrate`；non-author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17160:end -->
<!-- books-review:SF-2026-ARXIV-2605-17164:start -->
<!-- existing:SF-2026-ARXIV-2605-17164:start -->已逐章读取 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前正文拥有 surrounding principle，但尚未显式承载 `Charon: A Unified and Fine-Grained Simulator for Large-Scale LLM Training and Inference` 改变的 state/data/control/evidence boundary。 owner_sha256=089fc06685d0e6238733d8b293222afd04aeacd6d35cf016f2c21fe13c9e8ef1。<!-- existing:SF-2026-ARXIV-2605-17164:end -->
<!-- delta:SF-2026-ARXIV-2605-17164:start -->Charon: A Unified and Fine-Grained Simulator for Large-Scale LLM Training and Inference 提出的具体变化是：To address this, we introduce Charon, a unified, modular, and fine-grained simulator for accurately predicting LLM performance. 摘要中的长期系统挑战为：training and inference what-if simulation need a shared configuration identity and validation contract。它可能改变 `PLATFORM-EVALUATION-SYSTEM` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“In a practical inference deployment case, Charon discovered a configuration that improved system throughput over an engineering-tuned baseline, demonstrating its significant real-world value.”暂不作为最终证据。<!-- delta:SF-2026-ARXIV-2605-17164:end --> Decision=`Integrate`；non-author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17164:end -->
<!-- books-review:SF-2026-ARXIV-2605-17169:start -->
<!-- existing:SF-2026-ARXIV-2605-17169:start -->`books/part-07-agent/84-agent-platform.md` 已以更一般的 `AGENT-PLATFORM` 演进链承载该问题的 owner、commit/evidence boundary、failure fallback 与旧路径共存；本 family 只增加受限实现或 benchmark evidence。 owner_sha256=c90613b1e2cab33b382c0cff6ae0226e44b2d66b051e12a15174eae9c5fc6cdc。<!-- existing:SF-2026-ARXIV-2605-17169:end -->
<!-- delta:SF-2026-ARXIV-2605-17169:start -->Agentic AI is rapidly proliferating across diverse real-world domains such as software engineering, yet public trust has not kept pace.<!-- delta:SF-2026-ARXIV-2605-17169:end --> Decision=`No Change — Existing Coverage`；non-author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17169:end -->
<!-- books-review:SF-2026-ARXIV-2605-17170:start -->
<!-- existing:SF-2026-ARXIV-2605-17170:start -->已逐章读取 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 与相邻章节 ['books/part-05-inference-system/44-decode.md', 'books/part-05-inference-system/46-continuous-batching.md']；当前正文拥有 surrounding principle，但尚未显式承载 `TriAxialKV: Toward Extreme Low-Precision KV-Cache Quantization for Agentic Inference Tasks` 改变的 state/data/control/evidence boundary。 owner_sha256=94425d5fe4db0238e99350a5a0299edb408dcffcdb7b32453c76854a9dbc8e86。<!-- existing:SF-2026-ARXIV-2605-17170:end -->
<!-- delta:SF-2026-ARXIV-2605-17170:start -->TriAxialKV: Toward Extreme Low-Precision KV-Cache Quantization for Agentic Inference Tasks 提出的具体变化是：To this end, we introduce TriAxialKV, a novel mixed-precision KV-cache quantization scheme that assigns each token a triaxial tag, calibrates per-tag sensitivity, and allocates INT2/INT4 bitwidths under a fixed memory budget. 摘要中的长期系统挑战为：agentic KV quantization must condition precision on role, modality and temporal lifecycle。它可能改变 `INFER-KV-CACHE` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“As a result, their context exhibits structure that can carry different importance along three key axes: temporal recency to the current turn, modality such as text or image tokens, and semantic role such as user queries, tool calls, observations, or reasoning.”暂不作为最终证据。<!-- delta:SF-2026-ARXIV-2605-17170:end --> Decision=`Integrate`；non-author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17170:end -->
<!-- books-review:SF-2026-ARXIV-2605-17172:start -->
<!-- existing:SF-2026-ARXIV-2605-17172:start -->`books/part-07-agent/84-agent-platform.md` 已以更一般的 `AGENT-PLATFORM` 演进链承载该问题的 owner、commit/evidence boundary、failure fallback 与旧路径共存；本 family 只增加受限实现或 benchmark evidence。 owner_sha256=c90613b1e2cab33b382c0cff6ae0226e44b2d66b051e12a15174eae9c5fc6cdc。<!-- existing:SF-2026-ARXIV-2605-17172:end -->
<!-- delta:SF-2026-ARXIV-2605-17172:start -->OpenJarvis: Personal AI, On Personal Devices 提出的具体变化是：We present OpenJarvis, an architecture that represents a personal AI system as a typed spec over five primitives: Intelligence, Engine, Agents, Tools &amp; Memory, and Learning. 摘要中的长期系统挑战为：personal AI splits sensitive local state, local execution and optional cloud escalation into typed boundaries。它可能改变 `AGENT-PLATFORM` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“They also reduce marginal API cost by ~800x and end-to-end latency by 4x.”暂不作为最终证据。<!-- delta:SF-2026-ARXIV-2605-17172:end --> Decision=`No Change — Existing Coverage`；non-author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17172:end -->
<!-- books-review:SF-2026-ARXIV-2605-17173:start -->
<!-- existing:SF-2026-ARXIV-2605-17173:start -->已逐章读取 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前正文拥有 surrounding principle，但尚未显式承载 `Why Do Safety Guardrails Degrade Across Languages?` 改变的 state/data/control/evidence boundary。 owner_sha256=089fc06685d0e6238733d8b293222afd04aeacd6d35cf016f2c21fe13c9e8ef1。<!-- existing:SF-2026-ARXIV-2605-17173:end -->
<!-- delta:SF-2026-ARXIV-2605-17173:start -->Why Do Safety Guardrails Degrade Across Languages? 提出的具体变化是：We introduce a latent variable model, a Multi-Group Item Response Theory (IRT) framework, that decouples language-agnostic safety robustness ($θ$), intrinsic prompt hardness ($β$), global language processing difficulty ($γ$), and a prompt-specific cross-lingual safety gap ($τ$). 摘要中的长期系统挑战为：multilingual safety evaluation must decompose the failure factors hidden by aggregate jailbreak rate。它可能改变 `PLATFORM-EVALUATION-SYSTEM` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“Our framework reveals concept-language vulnerabilities that aggregate metrics obscure, enabling fairer cross-lingual safety evaluation and targeted improvements in dataset construction.”暂不作为最终证据。<!-- delta:SF-2026-ARXIV-2605-17173:end --> Decision=`Integrate`；non-author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17173:end -->
<!-- books-review:SF-2026-ARXIV-2605-17193:start -->
<!-- existing:SF-2026-ARXIV-2605-17193:start -->Ch82 已说明 same-model/context agents 共享 correlated error，只有独立 evidence、可验证接口或真实责任分解才可能产生增量；正文还保留趋同、coordination tax、single-Agent、independent proposals、deterministic verifier 与人工 adjudication fallback。Ch81 只拥有 durable workflow state，Ch83 只拥有 protocol interoperability。<!-- existing:SF-2026-ARXIV-2605-17193:end -->
<!-- delta:SF-2026-ARXIV-2605-17193:start -->exact-v1 在作者 closed-loop text simulations 中提供纵向 evidence：词汇变化可继续增长而语义支持收缩，十二类已测 surface/deep intervention 在 Bonferroni correction 后没有显著提升；但 regression 非 causal，recursive-channel theory 是 heuristic，且未覆盖外部 evidence renewal。<!-- delta:SF-2026-ARXIV-2605-17193:end --> Decision=`No Change — Existing Coverage`；无需新增 Books queue 或重复正文。
<!-- books-review:SF-2026-ARXIV-2605-17193:end -->
<!-- books-review:SF-2026-ARXIV-2605-19373:start -->
<!-- existing:SF-2026-ARXIV-2605-19373:start -->已逐章读取 `books/part-06-ai-infrastructure/59-model-registry.md` 与相邻章节 ['books/part-06-ai-infrastructure/58-kubeflow.md', 'books/part-06-ai-infrastructure/60-training-operator.md']；当前正文拥有 surrounding principle，但尚未显式承载 `Conflict-Free Replicated Data Types for Neural Network Model Merging: A Two-Layer Architecture Enabling CRDT-Compliant Model Merging Across 26 Strategies` 改变的 state/data/control/evidence boundary。 owner_sha256=7691a4f16c4ed6ecd5e5eb8487324292df7cfb82b3c10aee71730bc70a0f4290。<!-- existing:SF-2026-ARXIV-2605-19373:end -->
<!-- delta:SF-2026-ARXIV-2605-19373:start -->Conflict-Free Replicated Data Types for Neural Network Model Merging: A Two-Layer Architecture Enabling CRDT-Compliant Model Merging Across 26 Strategies 提出的具体变化是：To resolve this, we present a two-layer architecture -- CRDTMergeState -- that wraps any merge strategy in a CRDT-compliant (Conflict-Free Replicated Data Type) layer. 摘要中的长期系统挑战为：distributed model merging requires a conflict-free state wrapper because weight merges are not CRDT operations。它可能改变 `PLATFORM-MODEL-REGISTRY` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“We prove that this separation guarantees Strong Eventual Consistency: all replicas receiving the same contributions compute identical merged models, regardless of message ordering.”暂不作为最终证据。<!-- delta:SF-2026-ARXIV-2605-19373:end --> Decision=`Integrate`；non-author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-19373:end -->
<!-- books-review:SF-2026-ARXIV-2605-22850:start -->
<!-- existing:SF-2026-ARXIV-2605-22850:start -->已逐章读取 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 与相邻章节 ['books/part-05-inference-system/44-decode.md', 'books/part-05-inference-system/46-continuous-batching.md']；当前正文拥有 surrounding principle，但尚未显式承载 `ObjectCache: Layerwise Object-Storage Retrieval for KV Cache Reuse` 改变的 state/data/control/evidence boundary。 owner_sha256=94425d5fe4db0238e99350a5a0299edb408dcffcdb7b32453c76854a9dbc8e86。<!-- existing:SF-2026-ARXIV-2605-22850:end -->
<!-- delta:SF-2026-ARXIV-2605-22850:start -->ObjectCache: Layerwise Object-Storage Retrieval for KV Cache Reuse 提出的具体变化是：We propose ObjectCache, which co-designs the storage protocol and transfer schedule so that the storage server delivers KV cache data in the order the GPU consumes it, overlapping data transfer with compute across concurrent requests. 摘要中的长期系统挑战为：prefix KV reuse crosses local memory into layerwise object-store retrieval with explicit object identity。它可能改变 `INFER-KV-CACHE` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“Under shared bandwidth caps, our scheduler reduces added TTFT by 1.2--1.8x compared with equal bandwidth sharing.”暂不作为最终证据。<!-- delta:SF-2026-ARXIV-2605-22850:end --> Decision=`Integrate`；non-author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-22850:end -->
<!-- books-review:SF-2026-ARXIV-2605-23986:start -->
<!-- existing:SF-2026-ARXIV-2605-23986:start -->已逐章读取 `books/part-07-agent/77-memory.md` 与相邻章节 ['books/part-07-agent/76-rag.md', 'books/part-07-agent/78-tool-calling.md']；当前正文拥有 surrounding principle，但尚未显式承载 `MemForest: An Efficient Agent Memory System with Hierarchical Temporal Indexing` 改变的 state/data/control/evidence boundary。 owner_sha256=ac3bf5ab49bb87bcf3f0cfa1da47486caeb35e9d451251f91c67caf3bc9de6d7。<!-- existing:SF-2026-ARXIV-2605-23986:end -->
<!-- delta:SF-2026-ARXIV-2605-23986:start -->MemForest: An Efficient Agent Memory System with Hierarchical Temporal Indexing 提出的具体变化是：To address these challenges, we present MemForest, a memory framework that reformulates agent memory as a write-efficient temporal data-management problem. 摘要中的长期系统挑战为：hierarchical temporal indexing removes state-dependent generation from the memory write critical path。它可能改变 `AGENT-MEMORY` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“These results show that MemForest reduces memory-freshness latency while retaining strong answer quality.”暂不作为最终证据。<!-- delta:SF-2026-ARXIV-2605-23986:end --> Decision=`Integrate`；non-author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-23986:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260517-COVERAGE | fresh-context:may2026-day02 | coverage | coverage:SRC-ARXIV:20260517 | none | denominator 30→31 after six named false-positive removals and seven false-negative recoveries; 279/279 reclosed | passed |
| SA-20260517-EVIDENCE | fresh-context:may2026-day02 | evidence | review:SF-2026-ARXIV-2605-16745 | none | 31/31 exact-v1 reviews complete; recovered PDF identity, locators and non-proof boundary independently reconciled | passed |
| SA-20260517-DEEP | fresh-context:may2026-day02 | deep_analysis_selection | analysis:DA-SHARED-STATE; analysis:DA-OBJECT-KV; analysis:DA-INTENT-EFFECT | none | selected the three strongest cross-layer state/effect deltas | passed |
| SA-20260517-BOOKS | fresh-context:may2026-day02-postwrite | books | books-review:SF-2026-ARXIV-2605-16745 | none | 22/22 owner mechanisms and queue-declared adjacent chapters independently verified in books-post-write-semantic-audit.json; ordinary pending=0 | passed |

## 8. Ignored Noise

248 项 family-specific closure 位于 `papers/2026/05/_sources/daily-20260517/screening-ledger-independent-final.json`；其中 6 个 author false positive 被具名降级，7 个 false negative 被恢复。

## 9. Recommended Action

22/22 queue 已由 root 串行写回并通过独立 post-write semantic audit；2605.17193 exact-v1 恢复后判定 No Change — Existing Coverage。ordinary pending=0、external blocker=0，无新增 Books 写回。

## 10. Repository Changes

- 新增/更新 05-17 date-local independent ledger、exact-v1 receipts、Books comparison/queue、audit 与 canonical Daily；恢复 2605.17193 official exact-v1 PDF 并关闭唯一 Materials Request。
- 本 post-write reviewer 未修改共享 Books；仅审计 root 已完成的写回，未 stage、commit 或 push。

## 11. Open Questions

- 无；当前 denominator、Evidence、Books Decision 与 post-write audit 均无未解决项。

## 12. Sources
- [EVA01: Unified Native 3D Understanding and Generation via Mixture-of-Transformers](https://arxiv.org/html/2605.16745v1) — exact-v1；first-public 2026-05-16；accessed 2026-09-01
- [State Contamination in Memory-Augmented LLM Agents](https://arxiv.org/html/2605.16746v1) — exact-v1；first-public 2026-05-16；accessed 2026-09-01
- [Distinguishable Deletion: Unifying Knowledge Erasure and Refusal for Large Language Model Unlearning](https://arxiv.org/html/2605.16776v1) — exact-v1；first-public 2026-05-16；accessed 2026-09-01
- [Lever: Speculative LLM Inference on Smartphones](https://arxiv.org/html/2605.16786v1) — exact-v1；first-public 2026-05-16；accessed 2026-09-01
- [The Unlearnability Phenomenon in RLVR for Language Models](https://arxiv.org/html/2605.16787v1) — exact-v1；first-public 2026-05-16；accessed 2026-09-01
- [TIER: Trajectory-Invariant Execution Rewards for Multi-Step Tool Composition](https://arxiv.org/html/2605.16790v1) — exact-v1；first-public 2026-05-16；accessed 2026-09-01
- [AgentKernelArena: Generalization-Aware Benchmarking of GPU Kernel Optimization Agents](https://arxiv.org/html/2605.16819v1) — exact-v1；first-public 2026-05-16；accessed 2026-09-01
- [Decoupling KL and Trajectories: A Unified Perspective for SFT, DAgger, Offline RL, and OPD in LLM Distillation](https://arxiv.org/html/2605.16826v1) — exact-v1；first-public 2026-05-16；accessed 2026-09-01
- [CompactAttention: Accelerating Chunked Prefill with Block-Union KV Selection](https://arxiv.org/html/2605.16839v1) — exact-v1；first-public 2026-05-16；accessed 2026-09-01
- [GoodServe: Towards High-Goodput Serving of Agentic LLM Inferences over Heterogeneous Resources](https://arxiv.org/html/2605.16867v1) — exact-v1；first-public 2026-05-16；accessed 2026-09-01
- [Full Attention Strikes Back: Transferring Full Attention into Sparse within Hundred Training Steps](https://arxiv.org/html/2605.16928v1) — exact-v1；first-public 2026-05-16；accessed 2026-09-01
- [Securing LLM Agents Need Intent-to-Execution Integrity](https://arxiv.org/html/2605.16976v1) — exact-v1；first-public 2026-05-16；accessed 2026-09-01
- [Skills on the Fly: Test-Time Adaptive Skill Synthesis for LLM Agents](https://arxiv.org/html/2605.16986v1) — exact-v1；first-public 2026-05-16；accessed 2026-09-01
- [Learning-Zone Energy: Online Data Selection for Efficient RL Post-Training](https://arxiv.org/html/2605.17003v1) — exact-v1；first-public 2026-05-16；accessed 2026-09-01
- [Why Do Reasoning Models Lose Coverage? The Role of Data and Forks in the Road](https://arxiv.org/html/2605.17026v1) — exact-v1；first-public 2026-05-16；accessed 2026-09-01
- [PARALLAX: Separating Genuine Hallucination Detection from Benchmark Construction Artifacts](https://arxiv.org/html/2605.17028v1) — exact-v1；first-public 2026-05-16；accessed 2026-09-01
- [Privacy Policy Enforcement Guardrails for Data-Sensitive Retrieval-Augmented Generation](https://arxiv.org/html/2605.17034v1) — exact-v1；first-public 2026-05-16；accessed 2026-09-01
- [The Range Shrinks, the Threat Remains: Re-evaluating LLM Package Hallucinations on the 2026 Frontier-Model Cohort](https://arxiv.org/html/2605.17062v1) — exact-v1；first-public 2026-05-16；accessed 2026-09-01
- [S-Bus: Automatic Read-Set Reconstruction for Multi-Agent LLM State Coordination](https://arxiv.org/html/2605.17076v1) — exact-v1；first-public 2026-05-16；accessed 2026-09-01
- [HyDRA: Hybrid Dynamic Routing Architecture for Heterogeneous LLM Pools](https://arxiv.org/html/2605.17106v1) — exact-v1；first-public 2026-05-16；accessed 2026-09-01
- [The Point of No Return: Counterfactual Localization of Deceptive Commitment in Language-Model Reasoning](https://arxiv.org/html/2605.17113v1) — exact-v1；first-public 2026-05-16；accessed 2026-09-01
- [When Bits Break Recourse: Counterfactual-Faithful Quantization](https://arxiv.org/html/2605.17160v1) — exact-v1；first-public 2026-05-16；accessed 2026-09-01
- [Charon: A Unified and Fine-Grained Simulator for Large-Scale LLM Training and Inference](https://arxiv.org/html/2605.17164v1) — exact-v1；first-public 2026-05-16；accessed 2026-09-01
- [Responsible Agentic AI Requires Explicit Provenance](https://arxiv.org/html/2605.17169v1) — exact-v1；first-public 2026-05-16；accessed 2026-09-01
- [TriAxialKV: Toward Extreme Low-Precision KV-Cache Quantization for Agentic Inference Tasks](https://arxiv.org/html/2605.17170v1) — exact-v1；first-public 2026-05-16；accessed 2026-09-01
- [OpenJarvis: Personal AI, On Personal Devices](https://arxiv.org/html/2605.17172v1) — exact-v1；first-public 2026-05-16；accessed 2026-09-01
- [Why Do Safety Guardrails Degrade Across Languages?](https://arxiv.org/html/2605.17173v1) — exact-v1；first-public 2026-05-16；accessed 2026-09-01
- [Multi-LLM Systems Exhibit Robust Semantic Collapse](https://arxiv.org/pdf/2605.17193v1) — official exact-v1 PDF；first-public 2026-05-16；accessed 2026-09-01
- [Conflict-Free Replicated Data Types for Neural Network Model Merging: A Two-Layer Architecture Enabling CRDT-Compliant Model Merging Across 26 Strategies](https://arxiv.org/html/2605.19373v1) — exact-v1；first-public 2026-05-16；accessed 2026-09-01
- [ObjectCache: Layerwise Object-Storage Retrieval for KV Cache Reuse](https://arxiv.org/html/2605.22850v1) — exact-v1；first-public 2026-05-16；accessed 2026-09-01
- [MemForest: An Efficient Agent Memory System with Hierarchical Temporal Indexing](https://arxiv.org/html/2605.23986v1) — exact-v1；first-public 2026-05-16；accessed 2026-09-01

### Materials Request Ledger

No open materials requests. The former `MR-2605-17193-V1` was closed by `RECOVERY_2605.17193.md`.

## 13. Final Status

Completion Status: `Complete`

Coverage: `Closed`

Evidence: `Passed`

Books: `Passed`

unresolved findings: 0

确定性 Coverage、31/31 candidate Evidence、31/31 current Books comparison 与 22/22 Books 写回均已闭合；2605.17193 exact-v1 已恢复并判定 No Change — Existing Coverage。ordinary pending=0、external blocker=0。
