# Daily Research — 2026-06-25

**Research Date:** 2026-06-25

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-06-24 09:00:00 ～ 2026-06-25 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；全量枚举与语义筛选冻结候选分母，技术 claim 回到 exact-version primary evidence 与事件时 artifact receipt

**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed，fresh-context Semantic Audit 状态见第 7 节

## Executive Summary

Beijing window `[2026-06-24 09:00, 2026-06-25 09:00)` contains 510 registered identities. Full 510/510 semantic screening freezes 68 durable families and 442 family-specific closures. Route-negative audit is 127/127 with four promotions. Exact-v1 Evidence is 68/68 and full-frontier Selection chose three narratives. The 68/68 post-write fresh audit verified 63 unique-owner integrations plus five absent No Change families with zero unresolved finding.

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-06-25 |
| Window End | 2026-06-25 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | daily-v2.1:2026-06-25:9dcf324622a37ab5 |
| Denominator Frozen At | 2026-08-29T14:30:00+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-06-24T09:00:00+08:00 | 2026-06-25T09:00:00+08:00 | 2026-08-29T14:30:00+08:00 | frozen DataCite prefix snapshots; exact-v1 UTC window; all registered categories | checked | 510 | SF-2026-ARXIV-2606-25274; SF-2026-ARXIV-2606-25285; SF-2026-ARXIV-2606-25296; SF-2026-ARXIV-2606-25342; SF-2026-ARXIV-2606-25349; SF-2026-ARXIV-2606-25353; SF-2026-ARXIV-2606-25366; SF-2026-ARXIV-2606-25371; SF-2026-ARXIV-2606-25388; SF-2026-ARXIV-2606-25410; SF-2026-ARXIV-2606-25426; SF-2026-ARXIV-2606-25447; SF-2026-ARXIV-2606-25449; SF-2026-ARXIV-2606-25453; SF-2026-ARXIV-2606-25467; SF-2026-ARXIV-2606-25487; SF-2026-ARXIV-2606-25514; SF-2026-ARXIV-2606-25519; SF-2026-ARXIV-2606-25532; SF-2026-ARXIV-2606-25548; SF-2026-ARXIV-2606-25575; SF-2026-ARXIV-2606-25592; SF-2026-ARXIV-2606-25605; SF-2026-ARXIV-2606-25608; SF-2026-ARXIV-2606-25622; SF-2026-ARXIV-2606-25656; SF-2026-ARXIV-2606-25658; SF-2026-ARXIV-2606-25674; SF-2026-ARXIV-2606-25700; SF-2026-ARXIV-2606-25705; SF-2026-ARXIV-2606-25721; SF-2026-ARXIV-2606-25759; SF-2026-ARXIV-2606-25760; SF-2026-ARXIV-2606-25782; SF-2026-ARXIV-2606-25797; SF-2026-ARXIV-2606-25819; SF-2026-ARXIV-2606-25838; SF-2026-ARXIV-2606-25863; SF-2026-ARXIV-2606-25871; SF-2026-ARXIV-2606-25987; SF-2026-ARXIV-2606-25996; SF-2026-ARXIV-2606-26021; SF-2026-ARXIV-2606-26027; SF-2026-ARXIV-2606-26028; SF-2026-ARXIV-2606-26057; SF-2026-ARXIV-2606-26071; SF-2026-ARXIV-2606-26185; SF-2026-ARXIV-2606-26211; SF-2026-ARXIV-2606-26257; SF-2026-ARXIV-2606-26298; SF-2026-ARXIV-2606-26300; SF-2026-ARXIV-2606-26341; SF-2026-ARXIV-2606-26344; SF-2026-ARXIV-2606-26356; SF-2026-ARXIV-2606-26377; SF-2026-ARXIV-2606-26383; SF-2026-ARXIV-2606-26429; SF-2026-ARXIV-2606-26439; SF-2026-ARXIV-2606-26441; SF-2026-ARXIV-2606-26442; SF-2026-ARXIV-2606-26449; SF-2026-ARXIV-2606-26453; SF-2026-ARXIV-2606-26456; SF-2026-ARXIV-2606-26463; SF-2026-ARXIV-2606-26472; SF-2026-ARXIV-2606-26479; SF-2026-ARXIV-2606-26488; SF-2026-ARXIV-2606-26492 | pages=40; final_cursor=end; 510 unique identities | 2026-06-25T01:00:00Z | ../_sources/daily-20260625/screening-ledger.json; ../_sources/daily-20260625/denominator-full-semantic-audit-v1.tsv; coverage:SRC-ARXIV:20260625 | — |

<!-- coverage:SRC-ARXIV:20260625:start -->
All 321 Core, 62 keyword-routed and 127 route-negative identities were screened. Frozen arithmetic: `510 = 68 retained + 442 closures`; keyword routing was recall-only; route-negative FN=`2606.25467, 2606.25575, 2606.25592, 2606.26456`.
<!-- coverage:SRC-ARXIV:20260625:end -->

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-25274 | arXiv:2606.25274v1 | paper-v1:2606.25274 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25274 | self | — | new_in_window | AGENT-PLANNING | Integrate | books-review:SF-2026-ARXIV-2606-25274 | yes |
| SF-2026-ARXIV-2606-25285 | arXiv:2606.25285v1 | paper-v1:2606.25285 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25285 | self | — | new_in_window | INFER-GPU-MEMORY | Integrate | books-review:SF-2026-ARXIV-2606-25285 | yes |
| SF-2026-ARXIV-2606-25296 | arXiv:2606.25296v1 | paper-v1:2606.25296 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25296 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-25296 | yes |
| SF-2026-ARXIV-2606-25342 | arXiv:2606.25342v1 | paper-v1:2606.25342 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25342 | self | — | new_in_window | MODEL-LONG-CONTEXT | Integrate | books-review:SF-2026-ARXIV-2606-25342 | yes |
| SF-2026-ARXIV-2606-25349 | arXiv:2606.25349v1 | paper-v1:2606.25349 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25349 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-25349 | yes |
| SF-2026-ARXIV-2606-25353 | arXiv:2606.25353v1 | paper-v1:2606.25353 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25353 | self | — | new_in_window | INFER-PREFILL | Integrate | books-review:SF-2026-ARXIV-2606-25353 | yes |
| SF-2026-ARXIV-2606-25366 | arXiv:2606.25366v1 | paper-v1:2606.25366 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25366 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-25366 | yes |
| SF-2026-ARXIV-2606-25371 | arXiv:2606.25371v1 | paper-v1:2606.25371 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25371 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-25371 | yes |
| SF-2026-ARXIV-2606-25388 | arXiv:2606.25388v1 | paper-v1:2606.25388 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25388 | self | — | new_in_window | TRAIN-DATA | Integrate | books-review:SF-2026-ARXIV-2606-25388 | yes |
| SF-2026-ARXIV-2606-25410 | arXiv:2606.25410v1 | paper-v1:2606.25410 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25410 | self | — | new_in_window | TRAIN-DATA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-25410 | yes |
| SF-2026-ARXIV-2606-25426 | arXiv:2606.25426v1 | paper-v1:2606.25426 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25426 | self | — | new_in_window | INFER-PREFILL | Integrate | books-review:SF-2026-ARXIV-2606-25426 | yes |
| SF-2026-ARXIV-2606-25447 | arXiv:2606.25447v1 | paper-v1:2606.25447 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25447 | self | — | new_in_window | AGENT-WORKFLOW | Integrate | books-review:SF-2026-ARXIV-2606-25447 | yes |
| SF-2026-ARXIV-2606-25449 | arXiv:2606.25449v1 | paper-v1:2606.25449 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25449 | self | — | new_in_window | AGENT-MEMORY | Integrate | books-review:SF-2026-ARXIV-2606-25449 | yes |
| SF-2026-ARXIV-2606-25453 | arXiv:2606.25453v1 | paper-v1:2606.25453 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25453 | self | — | new_in_window | INFER-TENSORRT-LLM | Integrate | books-review:SF-2026-ARXIV-2606-25453 | yes |
| SF-2026-ARXIV-2606-25467 | arXiv:2606.25467v1 | paper-v1:2606.25467 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25467 | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-2026-ARXIV-2606-25467 | yes |
| SF-2026-ARXIV-2606-25487 | arXiv:2606.25487v1 | paper-v1:2606.25487 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25487 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2606-25487 | yes |
| SF-2026-ARXIV-2606-25514 | arXiv:2606.25514v1 | paper-v1:2606.25514 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25514 | self | — | new_in_window | AGENT-MULTI-AGENT | Integrate | books-review:SF-2026-ARXIV-2606-25514 | yes |
| SF-2026-ARXIV-2606-25519 | arXiv:2606.25519v1 | paper-v1:2606.25519 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25519 | self | — | new_in_window | INFER-GPU-MEMORY | Integrate | books-review:SF-2026-ARXIV-2606-25519 | yes |
| SF-2026-ARXIV-2606-25532 | arXiv:2606.25532v1 | paper-v1:2606.25532 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25532 | self | — | new_in_window | PLATFORM-FOUNDATIONS | Integrate | books-review:SF-2026-ARXIV-2606-25532 | yes |
| SF-2026-ARXIV-2606-25548 | arXiv:2606.25548v1 | paper-v1:2606.25548 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25548 | self | — | new_in_window | TRAIN-DATA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-25548 | yes |
| SF-2026-ARXIV-2606-25575 | arXiv:2606.25575v1 | paper-v1:2606.25575 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25575 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Integrate | books-review:SF-2026-ARXIV-2606-25575 | yes |
| SF-2026-ARXIV-2606-25592 | arXiv:2606.25592v1 | paper-v1:2606.25592 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25592 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-25592 | yes |
| SF-2026-ARXIV-2606-25605 | arXiv:2606.25605v1 | paper-v1:2606.25605 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25605 | self | — | new_in_window | AGENT-TOOL-CALLING | Integrate | books-review:SF-2026-ARXIV-2606-25605 | yes |
| SF-2026-ARXIV-2606-25608 | arXiv:2606.25608v1 | paper-v1:2606.25608 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25608 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-25608 | yes |
| SF-2026-ARXIV-2606-25622 | arXiv:2606.25622v1 | paper-v1:2606.25622 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25622 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2606-25622 | yes |
| SF-2026-ARXIV-2606-25656 | arXiv:2606.25656v1 | paper-v1:2606.25656 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25656 | self | — | new_in_window | AGENT-RAG | Integrate | books-review:SF-2026-ARXIV-2606-25656 | yes |
| SF-2026-ARXIV-2606-25658 | arXiv:2606.25658v1 | paper-v1:2606.25658 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25658 | self | — | new_in_window | AGENT-MEMORY | Integrate | books-review:SF-2026-ARXIV-2606-25658 | yes |
| SF-2026-ARXIV-2606-25674 | arXiv:2606.25674v1 | paper-v1:2606.25674 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25674 | self | — | new_in_window | AGENT-RAG | Integrate | books-review:SF-2026-ARXIV-2606-25674 | yes |
| SF-2026-ARXIV-2606-25700 | arXiv:2606.25700v1 | paper-v1:2606.25700 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25700 | self | — | new_in_window | TRAIN-LORA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-25700 | yes |
| SF-2026-ARXIV-2606-25705 | arXiv:2606.25705v1 | paper-v1:2606.25705 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25705 | self | — | new_in_window | AGENT-TOOL-CALLING | Integrate | books-review:SF-2026-ARXIV-2606-25705 | yes |
| SF-2026-ARXIV-2606-25721 | arXiv:2606.25721v1 | paper-v1:2606.25721 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25721 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-25721 | yes |
| SF-2026-ARXIV-2606-25759 | arXiv:2606.25759v1 | paper-v1:2606.25759 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25759 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Integrate | books-review:SF-2026-ARXIV-2606-25759 | yes |
| SF-2026-ARXIV-2606-25760 | arXiv:2606.25760v1 | paper-v1:2606.25760 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25760 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2606-25760 | yes |
| SF-2026-ARXIV-2606-25782 | arXiv:2606.25782v1 | paper-v1:2606.25782 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25782 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2606-25782 | yes |
| SF-2026-ARXIV-2606-25797 | arXiv:2606.25797v1 | paper-v1:2606.25797 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25797 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-25797 | yes |
| SF-2026-ARXIV-2606-25819 | arXiv:2606.25819v1 | paper-v1:2606.25819 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25819 | self | — | new_in_window | AGENT-TOOL-CALLING | Integrate | books-review:SF-2026-ARXIV-2606-25819 | yes |
| SF-2026-ARXIV-2606-25838 | arXiv:2606.25838v1 | paper-v1:2606.25838 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25838 | self | — | new_in_window | INFER-REQUEST-LIFECYCLE | Integrate | books-review:SF-2026-ARXIV-2606-25838 | yes |
| SF-2026-ARXIV-2606-25863 | arXiv:2606.25863v1 | paper-v1:2606.25863 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25863 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-25863 | yes |
| SF-2026-ARXIV-2606-25871 | arXiv:2606.25871v1 | paper-v1:2606.25871 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25871 | self | — | new_in_window | TRAIN-DATA | Integrate | books-review:SF-2026-ARXIV-2606-25871 | yes |
| SF-2026-ARXIV-2606-25987 | arXiv:2606.25987v1 | paper-v1:2606.25987 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25987 | self | — | new_in_window | AGENT-TOOL-CALLING | Integrate | books-review:SF-2026-ARXIV-2606-25987 | yes |
| SF-2026-ARXIV-2606-25996 | arXiv:2606.25996v1 | paper-v1:2606.25996 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25996 | self | — | new_in_window | TRAIN-DATA | Integrate | books-review:SF-2026-ARXIV-2606-25996 | yes |
| SF-2026-ARXIV-2606-26021 | arXiv:2606.26021v1 | paper-v1:2606.26021 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26021 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-26021 | yes |
| SF-2026-ARXIV-2606-26027 | arXiv:2606.26027v1 | paper-v1:2606.26027 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26027 | self | — | new_in_window | TRAIN-GRPO | Integrate | books-review:SF-2026-ARXIV-2606-26027 | yes |
| SF-2026-ARXIV-2606-26028 | arXiv:2606.26028v1 | paper-v1:2606.26028 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26028 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-26028 | yes |
| SF-2026-ARXIV-2606-26057 | arXiv:2606.26057v1 | paper-v1:2606.26057 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26057 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-26057 | yes |
| SF-2026-ARXIV-2606-26071 | arXiv:2606.26071v1 | paper-v1:2606.26071 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26071 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2606-26071 | yes |
| SF-2026-ARXIV-2606-26185 | arXiv:2606.26185v1 | paper-v1:2606.26185 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26185 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2606-26185 | yes |
| SF-2026-ARXIV-2606-26211 | arXiv:2606.26211v1 | paper-v1:2606.26211 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26211 | self | — | new_in_window | AGENT-MCP | Integrate | books-review:SF-2026-ARXIV-2606-26211 | yes |
| SF-2026-ARXIV-2606-26257 | arXiv:2606.26257v1 | paper-v1:2606.26257 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26257 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-26257 | yes |
| SF-2026-ARXIV-2606-26298 | arXiv:2606.26298v1 | paper-v1:2606.26298 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26298 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-26298 | yes |
| SF-2026-ARXIV-2606-26300 | arXiv:2606.26300v1 | paper-v1:2606.26300 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26300 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2606-26300 | yes |
| SF-2026-ARXIV-2606-26341 | arXiv:2606.26341v1 | paper-v1:2606.26341 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26341 | self | — | new_in_window | PLATFORM-GPU-SCHEDULER | Integrate | books-review:SF-2026-ARXIV-2606-26341 | yes |
| SF-2026-ARXIV-2606-26344 | arXiv:2606.26344v1 | paper-v1:2606.26344 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26344 | self | — | new_in_window | INFER-TENSORRT-LLM | Integrate | books-review:SF-2026-ARXIV-2606-26344 | yes |
| SF-2026-ARXIV-2606-26356 | arXiv:2606.26356v1 | paper-v1:2606.26356 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26356 | self | — | new_in_window | AGENT-PROMPT | Integrate | books-review:SF-2026-ARXIV-2606-26356 | yes |
| SF-2026-ARXIV-2606-26377 | arXiv:2606.26377v1 | paper-v1:2606.26377 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26377 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-26377 | yes |
| SF-2026-ARXIV-2606-26383 | arXiv:2606.26383v1 | paper-v1:2606.26383 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26383 | self | — | new_in_window | PLATFORM-MONITORING | Integrate | books-review:SF-2026-ARXIV-2606-26383 | yes |
| SF-2026-ARXIV-2606-26429 | arXiv:2606.26429v1 | paper-v1:2606.26429 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26429 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2606-26429 | yes |
| SF-2026-ARXIV-2606-26439 | arXiv:2606.26439v1 | paper-v1:2606.26439 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26439 | self | — | new_in_window | AGENT-RAG | Integrate | books-review:SF-2026-ARXIV-2606-26439 | yes |
| SF-2026-ARXIV-2606-26441 | arXiv:2606.26441v1 | paper-v1:2606.26441 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26441 | self | — | new_in_window | AGENT-RAG | Integrate | books-review:SF-2026-ARXIV-2606-26441 | yes |
| SF-2026-ARXIV-2606-26442 | arXiv:2606.26442v1 | paper-v1:2606.26442 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26442 | self | — | new_in_window | AGENT-WORKFLOW | Integrate | books-review:SF-2026-ARXIV-2606-26442 | yes |
| SF-2026-ARXIV-2606-26449 | arXiv:2606.26449v1 | paper-v1:2606.26449 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26449 | self | — | new_in_window | PLATFORM-TRACE | Integrate | books-review:SF-2026-ARXIV-2606-26449 | yes |
| SF-2026-ARXIV-2606-26453 | arXiv:2606.26453v1 | paper-v1:2606.26453 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26453 | self | — | new_in_window | INFER-TENSORRT-LLM | Integrate | books-review:SF-2026-ARXIV-2606-26453 | yes |
| SF-2026-ARXIV-2606-26456 | arXiv:2606.26456v1 | paper-v1:2606.26456 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26456 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2606-26456 | yes |
| SF-2026-ARXIV-2606-26463 | arXiv:2606.26463v1 | paper-v1:2606.26463 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26463 | self | — | new_in_window | AGENT-PLANNING | Integrate | books-review:SF-2026-ARXIV-2606-26463 | yes |
| SF-2026-ARXIV-2606-26472 | arXiv:2606.26472v1 | paper-v1:2606.26472 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26472 | self | — | new_in_window | INFER-KV-CACHE | Integrate | books-review:SF-2026-ARXIV-2606-26472 | yes |
| SF-2026-ARXIV-2606-26479 | arXiv:2606.26479v1 | paper-v1:2606.26479 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26479 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-26479 | yes |
| SF-2026-ARXIV-2606-26488 | arXiv:2606.26488v1 | paper-v1:2606.26488 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26488 | self | — | new_in_window | INFER-GPU-MEMORY | Integrate | books-review:SF-2026-ARXIV-2606-26488 | yes |
| SF-2026-ARXIV-2606-26492 | arXiv:2606.26492v1 | paper-v1:2606.26492 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26492 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2606-26492 | yes |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-25274 | RP-016bcf8aca420eca | deep | arXiv:2606.25274v1 | SRC-ARXIV@arXiv:2606.25274v1 | https://arxiv.org/html/2606.25274v1 — §3 Problem Definition; 4 Method; 4.2 Candidate Expansion; 4.3 UC-Beam | https://arxiv.org/html/2606.25274v1 — §5 Experiments; 5.1 Implemented Evidence; 6 Analysis | https://arxiv.org/html/2606.25274v1 — §7 Limitations | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25274 | complete |
| SF-2026-ARXIV-2606-25285 | RP-af8cc5ec3e0840a1 | deep | arXiv:2606.25285v1 | SRC-ARXIV@arXiv:2606.25285v1 | https://arxiv.org/html/2606.25285v1 — §3 EPTS: Elastic Post-Training Sparsity | https://arxiv.org/html/2606.25285v1 — §4 Experiments; Experimental Setup; Main Results | https://arxiv.org/html/2606.25285v1 — §Limitations and Discussion | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25285 | complete |
| SF-2026-ARXIV-2606-25296 | RP-8b2d6ed1f7415f59 | deep | arXiv:2606.25296v1 | SRC-ARXIV@arXiv:2606.25296v1 | https://arxiv.org/html/2606.25296v1 — §SafeGen Methodology; Assertion Generation; Fault Criticality Evaluation | https://arxiv.org/html/2606.25296v1 — §Experimental Evaluation; Functional-Safety Case Studies | https://arxiv.org/html/2606.25296v1 — §Threats to Validity; Limitations | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25296 | complete |
| SF-2026-ARXIV-2606-25342 | RP-bfb0ae3361bfc654 | deep | arXiv:2606.25342v1 | SRC-ARXIV@arXiv:2606.25342v1 | https://arxiv.org/html/2606.25342v1 — §Parametric Attention and Lifelong In-Context Learning formulation | https://arxiv.org/html/2606.25342v1 — §Experiments; Lifelong sequence results | https://arxiv.org/html/2606.25342v1 — §Discussion; finite-memory and task-family limitations | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25342 | complete |
| SF-2026-ARXIV-2606-25349 | RP-8195d95a2633e1fd | deep | arXiv:2606.25349v1 | SRC-ARXIV@arXiv:2606.25349v1 | https://arxiv.org/html/2606.25349v1 — §IV Two-Party Secure Inference Algorithm; V Storage-Communication Trade-off; VI Fused Relinearization and Rotation | https://arxiv.org/html/2606.25349v1 — §VII Evaluation | https://arxiv.org/html/2606.25349v1 — §VIII Conclusion; exact-v1 analytical-evaluation-only note | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25349 | complete |
| SF-2026-ARXIV-2606-25353 | RP-c5e41c6065465ab0 | deep | arXiv:2606.25353v1 | SRC-ARXIV@arXiv:2606.25353v1 | https://arxiv.org/html/2606.25353v1 — §3 Architecture; 3.1 Weight-Attention Decoupled Organization; 4 Implementation | https://arxiv.org/html/2606.25353v1 — §5 Experiment Setup; 6 Evaluation | https://arxiv.org/html/2606.25353v1 — §7 Discussion; 7.2 Future Works | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25353 | complete |
| SF-2026-ARXIV-2606-25366 | RP-12cd3776551d8d3f | deep | arXiv:2606.25366v1 | SRC-ARXIV@arXiv:2606.25366v1 | https://arxiv.org/html/2606.25366v1 — §III System and Testbed; IV Verified Runtime Shield; VII Adaptation-Aware Runtime Assurance | https://arxiv.org/html/2606.25366v1 — §VIII Robustness; IX Integrated Evaluation | https://arxiv.org/html/2606.25366v1 — §XI-D Limitations | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25366 | complete |
| SF-2026-ARXIV-2606-25371 | RP-892bebb25476d387 | deep | arXiv:2606.25371v1 | SRC-ARXIV@arXiv:2606.25371v1 | https://arxiv.org/html/2606.25371v1 — §III Problem Setup; IV Conformal Recovery-Deadline Certificate | https://arxiv.org/html/2606.25371v1 — §V Experiments | https://arxiv.org/html/2606.25371v1 — §VI-D Limitations | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25371 | complete |
| SF-2026-ARXIV-2606-25388 | RP-d70161adcb54fa76 | deep | arXiv:2606.25388v1 | SRC-ARXIV@arXiv:2606.25388v1 | https://arxiv.org/html/2606.25388v1 — §III System Overview; IV Methodology; IV-F Execution-Guided Validation and Control | https://arxiv.org/html/2606.25388v1 — §V Experimental Evaluation; V-A Experimental Setup | https://arxiv.org/html/2606.25388v1 — §VII Discussion and Future Work | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25388 | complete |
| SF-2026-ARXIV-2606-25410 | RP-a06733fa049bd38d | deep | arXiv:2606.25410v1 | SRC-ARXIV@arXiv:2606.25410v1 | https://arxiv.org/html/2606.25410v1 — §3 Proposed Method; 3.1 Importance Score Calculation; 3.2 Weight Rescaling | https://arxiv.org/html/2606.25410v1 — §4 Experiments; 4.1 Experimental Setup; 4.4 Results | https://arxiv.org/html/2606.25410v1 — §5 Conclusion; class-forgetting experimental scope | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25410 | complete |
| SF-2026-ARXIV-2606-25426 | RP-0552e898756ed601 | deep | arXiv:2606.25426v1 | SRC-ARXIV@arXiv:2606.25426v1 | https://arxiv.org/html/2606.25426v1 — §3 Method; 3.1 Three-level cache blocking; 3.2 Weight pre-packing | https://arxiv.org/html/2606.25426v1 — §4 Evaluation; 4.1 Experimental setup; 4.7 End-to-end prefill GEMM measurement | https://arxiv.org/html/2606.25426v1 — §6 Conclusion; Limitations | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25426 | complete |
| SF-2026-ARXIV-2606-25447 | RP-f6dfc5ff2438b294 | deep | arXiv:2606.25447v1 | SRC-ARXIV@arXiv:2606.25447v1 | https://arxiv.org/html/2606.25447v1 — §3 Experiment Setup; 3.2 Harness; 3.3 Tool Schema; 3.4 Task Type | https://arxiv.org/html/2606.25447v1 — §4 Analysis; 4.1 Evaluation Protocol; 4.4 OOD Robustness | https://arxiv.org/html/2606.25447v1 — §B Benchmark Details; C Experimental Details; stated ALFWorld boundary | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25447 | complete |
| SF-2026-ARXIV-2606-25449 | RP-78fb62ea4ed5abe1 | deep | arXiv:2606.25449v1 | SRC-ARXIV@arXiv:2606.25449v1 | https://arxiv.org/html/2606.25449v1 — §3 Brittle Memory and Reclaim Evaluation; 3.2 Reclaim Protocol | https://arxiv.org/html/2606.25449v1 — §4 Experimental Setup; 5 Results; 5.7 Boundary of the Fix | https://arxiv.org/html/2606.25449v1 — §7 Limitations | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25449 | complete |
| SF-2026-ARXIV-2606-25453 | RP-9e3cce4961c0b96c | deep | arXiv:2606.25453v1 | SRC-ARXIV@arXiv:2606.25453v1 | https://arxiv.org/html/2606.25453v1 — §III EmuGEMM-I; IV EmuGEMM-II | https://arxiv.org/html/2606.25453v1 — §V Evaluation; V-B Experimental Setup; V-F Precision-Throughput-Memory Trade-off | https://arxiv.org/html/2606.25453v1 — §V-G Limitations | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25453 | complete |
| SF-2026-ARXIV-2606-25467 | RP-aec0e13356c5eef8 | deep | arXiv:2606.25467v1 | SRC-ARXIV@arXiv:2606.25467v1 | https://arxiv.org/html/2606.25467v1 — §III Request-Resource Coupling Model; IV RQ-SAFE Online Orchestration | https://arxiv.org/html/2606.25467v1 — §V Experimental Evaluation; V-A Experimental Setup | https://arxiv.org/html/2606.25467v1 — §D-B Runtime Boundary and Fallback; G Implementation Scope Clarifications | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25467 | complete |
| SF-2026-ARXIV-2606-25487 | RP-10b4253c673aafd5 | deep | arXiv:2606.25487v1 | SRC-ARXIV@arXiv:2606.25487v1 | https://arxiv.org/html/2606.25487v1 — §3 Setup; Appendix A Prompts, wrappers, and attack configuration | https://arxiv.org/html/2606.25487v1 — §4 Results; 4.1 Calibration against human labels; 4.3 white-box attack | https://arxiv.org/html/2606.25487v1 — §6 Limitations | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25487 | complete |
| SF-2026-ARXIV-2606-25514 | RP-7784341993231506 | deep | arXiv:2606.25514v1 | SRC-ARXIV@arXiv:2606.25514v1 | https://arxiv.org/html/2606.25514v1 — §2 Adaptive Multi-Agent Issue Resolution; 2.6 Event-Driven Synchronous Communication | https://arxiv.org/html/2606.25514v1 — §3 Evaluation; 3.2 Analysis of Exclusive Fixes and Failures | https://arxiv.org/html/2606.25514v1 — §5 Threats to Validity | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25514 | complete |
| SF-2026-ARXIV-2606-25519 | RP-de7e921f96b11cd1 | deep | arXiv:2606.25519v1 | SRC-ARXIV@arXiv:2606.25519v1 | https://arxiv.org/html/2606.25519v1 — §3 Experimental Setup; 5 Quantization Inflates Reasoning Tokens; 6 Anatomy | https://arxiv.org/html/2606.25519v1 — §D Additional evaluation details; D.1 Benchmarks and evaluation protocol | https://arxiv.org/html/2606.25519v1 — §7 Can We Reduce Reasoning-Token Inflation; D.2 Model details | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25519 | complete |
| SF-2026-ARXIV-2606-25532 | RP-a888d42f1d5133eb | deep | arXiv:2606.25532v1 | SRC-ARXIV@arXiv:2606.25532v1 | https://arxiv.org/html/2606.25532v1 — §Physically constrained multi-agent discovery engine; Evolutionary Knowledge Graph and algorithmic chain of thought | https://arxiv.org/html/2606.25532v1 — §Hardware-compliance evaluation and discovered-system validation | https://arxiv.org/html/2606.25532v1 — §Exact-v1 research-prototype and evaluated hardware-design boundary | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25532 | complete |
| SF-2026-ARXIV-2606-25548 | RP-511e7faf5b6a96de | deep | arXiv:2606.25548v1 | SRC-ARXIV@arXiv:2606.25548v1 | https://arxiv.org/html/2606.25548v1 — §4 Transcoders-based Concept Removal; 4.1 BLOCK Framework | https://arxiv.org/html/2606.25548v1 — §5 Empirical Evaluation; 5.1 Experimental Setup; 5.4 Robustness | https://arxiv.org/html/2606.25548v1 — §G Limitations; D.1 Model-Architecture-Dependent Subtleties | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25548 | complete |
| SF-2026-ARXIV-2606-25575 | RP-756a47a3ef188a2d | deep | arXiv:2606.25575v1 | SRC-ARXIV@arXiv:2606.25575v1 | https://arxiv.org/html/2606.25575v1 — §Variable-autonomy architecture; task-phase authority transfer; always-available release gesture | https://arxiv.org/html/2606.25575v1 — §44-participant user study; five bimanual tasks; policy-variant success | https://arxiv.org/html/2606.25575v1 — §Single wearable-hand embodiment, known objects, five tools, and short-horizon study | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25575 | complete |
| SF-2026-ARXIV-2606-25592 | RP-0e797107eb2deab0 | deep | arXiv:2606.25592v1 | SRC-ARXIV@arXiv:2606.25592v1 | https://arxiv.org/html/2606.25592v1 — §2 Visual Prompt Attack and Defense; 2.2 VPA-Guard | https://arxiv.org/html/2606.25592v1 — §3 VVA-Bench; 3.2 Evaluation Protocol; 4 Main Experiments | https://arxiv.org/html/2606.25592v1 — §E.1 Limitations; E.4 Human-in-the-loop Discussion | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25592 | complete |
| SF-2026-ARXIV-2606-25605 | RP-6bf3b401e811ea67 | deep | arXiv:2606.25605v1 | SRC-ARXIV@arXiv:2606.25605v1 | https://arxiv.org/html/2606.25605v1 — §3 Problem Definition; 4 Experimental Setup; 7 Transparent Two-Pass Execution | https://arxiv.org/html/2606.25605v1 — §5 Empirical Findings; 7.3 Experimental Evaluation; 7.4 Cost and Latency | https://arxiv.org/html/2606.25605v1 — §7.5 Failure Cases and Limitations; 8.4 Limitations | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25605 | complete |
| SF-2026-ARXIV-2606-25608 | RP-50f7baec1957195c | deep | arXiv:2606.25608v1 | SRC-ARXIV@arXiv:2606.25608v1 | https://arxiv.org/html/2606.25608v1 — §V Proposed Method: Multi-LLM System; V-B Multi-LLM architecture with HybridRAG | https://arxiv.org/html/2606.25608v1 — §VI Initial Evaluation | https://arxiv.org/html/2606.25608v1 — §V-C Restrictions of our architecture; VII Future Research | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25608 | complete |
| SF-2026-ARXIV-2606-25622 | RP-1672753b6890e9b1 | deep | arXiv:2606.25622v1 | SRC-ARXIV@arXiv:2606.25622v1 | https://arxiv.org/html/2606.25622v1 — §IV Theoretical Framework: MAS Architecture and Experimental Setup | https://arxiv.org/html/2606.25622v1 — §V Results & Discussion | https://arxiv.org/html/2606.25622v1 — §VI Limitations & Future Work | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25622 | complete |
| SF-2026-ARXIV-2606-25656 | RP-a8a4288ea1019dad | deep | arXiv:2606.25656v1 | SRC-ARXIV@arXiv:2606.25656v1 | https://arxiv.org/html/2606.25656v1 — §3 Methods; 3.2 Regular RAG; 3.3 GraphRAG; 3.4 Modular and Agentic RAG; 3.5 Context Optimization | https://arxiv.org/html/2606.25656v1 — §4 Experimental setup; 5 Experimental results | https://arxiv.org/html/2606.25656v1 — §6 Conclusions and future work; C Retrieval-Generation Gap | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25656 | complete |
| SF-2026-ARXIV-2606-25658 | RP-fc0db43307b98122 | deep | arXiv:2606.25658v1 | SRC-ARXIV@arXiv:2606.25658v1 | https://arxiv.org/html/2606.25658v1 — §3 Method; 3.2 Online Semantic Basis; 3.3 Dynamic Visual Memory Bank | https://arxiv.org/html/2606.25658v1 — §4 Experiment; 4.1 Benchmarks and Metrics; 4.2 Implementation | https://arxiv.org/html/2606.25658v1 — §A Limitations | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25658 | complete |
| SF-2026-ARXIV-2606-25674 | RP-512e4777874b68ca | deep | arXiv:2606.25674v1 | SRC-ARXIV@arXiv:2606.25674v1 | https://arxiv.org/html/2606.25674v1 — §3 Method; 3.2 Low-bit Embedding Backbone; 3.5 Multi-precision Embedding Quantization | https://arxiv.org/html/2606.25674v1 — §4 Experiments; 4.1 Experimental Setup; B Evaluation Details | https://arxiv.org/html/2606.25674v1 — §4.4 Analysis; task-type sensitivity to quantization | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25674 | complete |
| SF-2026-ARXIV-2606-25700 | RP-60a85adbcc4a5361 | deep | arXiv:2606.25700v1 | SRC-ARXIV@arXiv:2606.25700v1 | https://arxiv.org/html/2606.25700v1 — §III Methods; III-B Training; III-C Architecture | https://arxiv.org/html/2606.25700v1 — §IV Results; IV-B Computation calculation | https://arxiv.org/html/2606.25700v1 — §V Discussion; V-A Choice of rank; V-C Computation | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25700 | complete |
| SF-2026-ARXIV-2606-25705 | RP-8703e249715f19ca | deep | arXiv:2606.25705v1 | SRC-ARXIV@arXiv:2606.25705v1 | https://arxiv.org/html/2606.25705v1 — §3 Methodology; 3.1 Query Selection, Expansion and Saturation; 3.2 Roll-out with Emulator | https://arxiv.org/html/2606.25705v1 — §4 Experiments and Results | https://arxiv.org/html/2606.25705v1 — §5 Conclusion; short-paper and emulator-only boundary | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25705 | complete |
| SF-2026-ARXIV-2606-25721 | RP-045fc2758d4f7c34 | deep | arXiv:2606.25721v1 | SRC-ARXIV@arXiv:2606.25721v1 | https://arxiv.org/html/2606.25721v1 — §4 Method; 4.1 Keyword Searching; 4.2 Secondary Verification | https://arxiv.org/html/2606.25721v1 — §5 Evaluation; 5.1 Setup; 5.2 Results | https://arxiv.org/html/2606.25721v1 — §6 Discussion; baseline and hyperparameter sensitivity | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25721 | complete |
| SF-2026-ARXIV-2606-25759 | RP-16e55de266034d8f | deep | arXiv:2606.25759v1 | SRC-ARXIV@arXiv:2606.25759v1 | https://arxiv.org/html/2606.25759v1 — §3 System Overview; 4 Operating-Profile Calibration; 5 Runtime Binding and Bucket Routing | https://arxiv.org/html/2606.25759v1 — §7 Closed-Loop Cluster Evaluation; 7.1 Evaluation Setup and Scope | https://arxiv.org/html/2606.25759v1 — §9 Limitations and Future Work; A.4 Evaluation Environment and Measurement Boundary | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25759 | complete |
| SF-2026-ARXIV-2606-25760 | RP-9237df1d3b71b376 | deep | arXiv:2606.25760v1 | SRC-ARXIV@arXiv:2606.25760v1 | https://arxiv.org/html/2606.25760v1 — §3 Benchmark and Evaluation Protocol; 7 Inductive-Conformal Click Disks | https://arxiv.org/html/2606.25760v1 — §4 UQ Generalizes Selectively; 5 Graded Error and Calibration | https://arxiv.org/html/2606.25760v1 — §A4 Out-of-distribution analysis; A5 Methods deferred; A25 vendor protocol details | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25760 | complete |
| SF-2026-ARXIV-2606-25782 | RP-7b17a11c2c138280 | deep | arXiv:2606.25782v1 | SRC-ARXIV@arXiv:2606.25782v1 | https://arxiv.org/html/2606.25782v1 — §2 Dataset; 3 Adversarial Attack Methodology; 4 Safety Judge Panel | https://arxiv.org/html/2606.25782v1 — §5 Evaluation Protocol; 6 Results; 6.3 Cost and Latency Trade-offs | https://arxiv.org/html/2606.25782v1 — §OOD holdout and multi-turn attack boundary; 0.B Inference Throughput and Latency | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25782 | complete |
| SF-2026-ARXIV-2606-25797 | RP-43e49516d2f38761 | deep | arXiv:2606.25797v1 | SRC-ARXIV@arXiv:2606.25797v1 | https://arxiv.org/html/2606.25797v1 — §3 Improving Online MDP-SMC; 3.2 Confidence Sequences; 3.4 Confidence Sequence MDP-SMC | https://arxiv.org/html/2606.25797v1 — §4 Implementation and Experimental Evaluation | https://arxiv.org/html/2606.25797v1 — §0.A Assumptions on Sampling Access and Knowledge; 0.B Reusing Confidence is Incorrect | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25797 | complete |
| SF-2026-ARXIV-2606-25819 | RP-233fd55b344e93ff | deep | arXiv:2606.25819v1 | SRC-ARXIV@arXiv:2606.25819v1 | https://arxiv.org/html/2606.25819v1 — §ToolBench-X; Problem Formulation; Benchmark Construction; Reliability Hazard Injection | https://arxiv.org/html/2606.25819v1 — §Experiments; Experimental Setup; Further Analysis; Error Analysis | https://arxiv.org/html/2606.25819v1 — §Canonical recovery-path construction and five injected-hazard boundary | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25819 | complete |
| SF-2026-ARXIV-2606-25838 | RP-a78497f8f1bd3611 | deep | arXiv:2606.25838v1 | SRC-ARXIV@arXiv:2606.25838v1 | https://arxiv.org/html/2606.25838v1 — §III Method; IV Confidence-Aware Routing | https://arxiv.org/html/2606.25838v1 — §V Experiments; V-A Evaluation protocol; VI Deployment Patterns | https://arxiv.org/html/2606.25838v1 — §VII-C Limitations and future work | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25838 | complete |
| SF-2026-ARXIV-2606-25863 | RP-32b62b7531d48a0d | deep | arXiv:2606.25863v1 | SRC-ARXIV@arXiv:2606.25863v1 | https://arxiv.org/pdf/2606.25863v1 — §PDF §3 Research Design; §3.3 PatchLens static analysis and build-system resolution | https://arxiv.org/pdf/2606.25863v1 — §PDF §4 Results; 1,192 Linux, 289 FFmpeg, 100 PHP patches | https://arxiv.org/pdf/2606.25863v1 — §PDF threats to validity; compile-time C/C++ and project-specific build-resolver boundary | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25863 | complete |
| SF-2026-ARXIV-2606-25871 | RP-dc28dab74d734629 | deep | arXiv:2606.25871v1 | SRC-ARXIV@arXiv:2606.25871v1 | https://arxiv.org/html/2606.25871v1 — §3 Our Approach; 3.1 System Architecture; 3.3 Per-Class Isotonic Calibration; 3.4 Cascade Decision Logic | https://arxiv.org/html/2606.25871v1 — §4 Experiments and Evaluation; 4.2 Dataset and Setup; 4.5 Cascade Performance | https://arxiv.org/html/2606.25871v1 — §5 Production Deployment and Discussion; sponsored-search relevance boundary | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25871 | complete |
| SF-2026-ARXIV-2606-25987 | RP-eb31acb4bae587ac | deep | arXiv:2606.25987v1 | SRC-ARXIV@arXiv:2606.25987v1 | https://arxiv.org/html/2606.25987v1 — §3 Formal Engine; 3.2 Architecture; 4 Weave of Formal Thought | https://arxiv.org/html/2606.25987v1 — §5 WoFT Improves Surface Modeling; 5.1 Experimental setup | https://arxiv.org/html/2606.25987v1 — §6 Next Steps and Research Vision; technical-report preliminary-results boundary | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25987 | complete |
| SF-2026-ARXIV-2606-25996 | RP-344dab5093061ed0 | deep | arXiv:2606.25996v1 | SRC-ARXIV@arXiv:2606.25996v1 | https://arxiv.org/html/2606.25996v1 — §2 Autodata; 2.1 Agentic Self-Instruct; 4 Meta Optimization of the Data Scientist | https://arxiv.org/html/2606.25996v1 — §3 Experiments; CS, legal, and scientific reasoning tasks | https://arxiv.org/html/2606.25996v1 — §6 Conclusion and Discussion; Hacking & limitations; A Token Efficiency and Truncation | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25996 | complete |
| SF-2026-ARXIV-2606-26021 | RP-428ae67b93cc5415 | deep | arXiv:2606.26021v1 | SRC-ARXIV@arXiv:2606.26021v1 | https://arxiv.org/html/2606.26021v1 — §V Attention-based MIA; VI Inference-Time Hardening Against MIAs | https://arxiv.org/html/2606.26021v1 — §IV Tabular FMs Under Standard MIAs; V-B and VI-B Experimental Results | https://arxiv.org/html/2606.26021v1 — §VIII-C Limitations and opportunities; I Context size | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-26021 | complete |
| SF-2026-ARXIV-2606-26027 | RP-bbe015028632c835 | deep | arXiv:2606.26027v1 | SRC-ARXIV@arXiv:2606.26027v1 | https://arxiv.org/html/2606.26027v1 — §4 Method; 4.2 catastrophic collapse; 4.4 supervisory fixes | https://arxiv.org/html/2606.26027v1 — §5 Experiments; 5.1 Dataset and Models; D Detailed Evaluation | https://arxiv.org/html/2606.26027v1 — §B Training Details; C Qwen3 Training; E Training Dynamic | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-26027 | complete |
| SF-2026-ARXIV-2606-26028 | RP-350a830c5abafdfe | deep | arXiv:2606.26028v1 | SRC-ARXIV@arXiv:2606.26028v1 | https://arxiv.org/html/2606.26028v1 — §3 System Model: ERC-8004 Protocol; 7 Reputation Market Security | https://arxiv.org/html/2606.26028v1 — §4 Dataset; 5 Agent Identity and Adoption; 6 Reputation Market | https://arxiv.org/html/2606.26028v1 — §9 Limitations and Future Work; C x402 attribution challenges | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-26028 | complete |
| SF-2026-ARXIV-2606-26057 | RP-5d0d84a2880f0eca | deep | arXiv:2606.26057v1 | SRC-ARXIV@arXiv:2606.26057v1 | https://arxiv.org/html/2606.26057v1 — §2 Threat Model; 3 Requirements; 4 Design; 5 Implementation | https://arxiv.org/html/2606.26057v1 — §6 Evaluation; 6.4 Machine-Checked Fail-Closed Invariant; 6.5 Live containment | https://arxiv.org/html/2606.26057v1 — §8.3 Limitations and Future Work; Artifact and Reproducibility | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-26057 | complete |
| SF-2026-ARXIV-2606-26071 | RP-c205d94ba3531c8c | deep | arXiv:2606.26071v1 | SRC-ARXIV@arXiv:2606.26071v1 | https://arxiv.org/html/2606.26071v1 — §4 Protocol and Methods; 5 Environments; 7 Methodological Insights | https://arxiv.org/html/2606.26071v1 — §6 Case Studies; 8 Recommendations | https://arxiv.org/html/2606.26071v1 — §10 Limitations and Future Work; negative-results and confounding boundary | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-26071 | complete |
| SF-2026-ARXIV-2606-26185 | RP-3c8114a102a5f867 | deep | arXiv:2606.26185v1 | SRC-ARXIV@arXiv:2606.26185v1 | https://arxiv.org/html/2606.26185v1 — §Temperature-control and reproducibility protocol for LLM-as-judge safety evaluation | https://arxiv.org/html/2606.26185v1 — §Cross-temperature, repeat-run and judge-agreement evaluation | https://arxiv.org/html/2606.26185v1 — §Temperature control is necessary but not sufficient; prompt/model/vendor drift remains | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-26185 | complete |
| SF-2026-ARXIV-2606-26211 | RP-80cfa89873050b29 | deep | arXiv:2606.26211v1 | SRC-ARXIV@arXiv:2606.26211v1 | https://arxiv.org/html/2606.26211v1 — §Data Facts metadata schema; provenance, semantics, constraints and exchange contract | https://arxiv.org/html/2606.26211v1 — §NANDini multi-agent exchange examples and schema coverage | https://arxiv.org/html/2606.26211v1 — §Single ecosystem prototype; no proof of cross-vendor enforcement or semantic completeness | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-26211 | complete |
| SF-2026-ARXIV-2606-26257 | RP-a840d100b5b37ba1 | deep | arXiv:2606.26257v1 | SRC-ARXIV@arXiv:2606.26257v1 | https://arxiv.org/html/2606.26257v1 — §Dataset Usage Inference formulation without shadow models or held-out data | https://arxiv.org/html/2606.26257v1 — §Exact-v1 membership/dataset inference experiments and ablations | https://arxiv.org/html/2606.26257v1 — §Requires the paper's observable score/query regime; not per-record legal attribution | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-26257 | complete |
| SF-2026-ARXIV-2606-26298 | RP-e90143e57ba29e80 | deep | arXiv:2606.26298v1 | SRC-ARXIV@arXiv:2606.26298v1 | https://arxiv.org/html/2606.26298v1 — §Governing Actions, Not Agents; Institutional Attestation model | https://arxiv.org/html/2606.26298v1 — §Action-level attestation scenarios and governance analysis | https://arxiv.org/html/2606.26298v1 — §Institutional model is a governance proposal, not a deployed enforcement benchmark | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-26298 | complete |
| SF-2026-ARXIV-2606-26300 | RP-a3d4d472369add93 | deep | arXiv:2606.26300v1 | SRC-ARXIV@arXiv:2606.26300v1 | https://arxiv.org/html/2606.26300v1 — §Verification Horizon formulation for coding-agent rewards | https://arxiv.org/html/2606.26300v1 — §Reward-verification experiments across coding horizons | https://arxiv.org/html/2606.26300v1 — §No universal reward verifier; longer horizons and hidden environment state remain | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-26300 | complete |
| SF-2026-ARXIV-2606-26341 | RP-62a53e0dfb8b0cbd | deep | arXiv:2606.26341v1 | SRC-ARXIV@arXiv:2606.26341v1 | https://arxiv.org/html/2606.26341v1 — §Many Problems One GPU batching and nonlinear-optimization execution design | https://arxiv.org/html/2606.26341v1 — §GPU scaling experiments across problem families | https://arxiv.org/html/2606.26341v1 — §Only disclosed nonlinear solvers/problem shapes; no cluster-level scheduling or isolation proof | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-26341 | complete |
| SF-2026-ARXIV-2606-26344 | RP-d3775e238667e27e | deep | arXiv:2606.26344v1 | SRC-ARXIV@arXiv:2606.26344v1 | https://arxiv.org/html/2606.26344v1 — §Axon synthesizing superoptimizer; tensor-program search and verification | https://arxiv.org/html/2606.26344v1 — §Kernel synthesis evaluation and generated-program performance | https://arxiv.org/html/2606.26344v1 — §Covered tensor operators/hardware only; verifier does not prove arbitrary numerical equivalence | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-26344 | complete |
| SF-2026-ARXIV-2606-26356 | RP-1701767ba01a558b | deep | arXiv:2606.26356v1 | SRC-ARXIV@arXiv:2606.26356v1 | https://arxiv.org/html/2606.26356v1 — §Instruction Bleed formulation; prompt-composed module interference | https://arxiv.org/html/2606.26356v1 — §Cross-module interference experiments and mitigations | https://arxiv.org/html/2606.26356v1 — §Prompt/module families tested do not establish universal isolation or adversarial robustness | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-26356 | complete |
| SF-2026-ARXIV-2606-26377 | RP-4eab22709fa045af | deep | arXiv:2606.26377v1 | SRC-ARXIV@arXiv:2606.26377v1 | https://arxiv.org/html/2606.26377v1 — §Unified intent-and-harm verification defense | https://arxiv.org/html/2606.26377v1 — §Threat-generation and defense evaluation | https://arxiv.org/html/2606.26377v1 — §Evaluated threat families and judges only; intent inference is not proof of harmless execution | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-26377 | complete |
| SF-2026-ARXIV-2606-26383 | RP-ac135c6a5d88e8a6 | deep | arXiv:2606.26383v1 | SRC-ARXIV@arXiv:2606.26383v1 | https://arxiv.org/html/2606.26383v1 — §SOLAR speed-of-light performance model; bottleneck decomposition and bound calculation | https://arxiv.org/html/2606.26383v1 — §Predicted-vs-observed latency and throughput analysis | https://arxiv.org/html/2606.26383v1 — §Analytical bounds depend on calibrated hardware/workload parameters and omit undisclosed runtime effects | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-26383 | complete |
| SF-2026-ARXIV-2606-26429 | RP-474420728a35e81f | deep | arXiv:2606.26429v1 | SRC-ARXIV@arXiv:2606.26429v1 | https://arxiv.org/html/2606.26429v1 — §DualEval joint model-item calibration | https://arxiv.org/html/2606.26429v1 — §Unified LLM evaluation experiments and calibration analysis | https://arxiv.org/html/2606.26429v1 — §Joint calibration assumes the evaluated item/model pool; new distributions require refitting | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-26429 | complete |
| SF-2026-ARXIV-2606-26439 | RP-719f8cf401637f6c | deep | arXiv:2606.26439v1 | SRC-ARXIV@arXiv:2606.26439v1 | https://arxiv.org/html/2606.26439v1 — §TileMaxSim IO-aware GPU MaxSim scoring; dimension tiling and fused product quantization | https://arxiv.org/html/2606.26439v1 — §GPU retrieval throughput, latency and quality evaluation | https://arxiv.org/html/2606.26439v1 — §Evaluated MaxSim layouts and GPUs only; index update and distributed consistency are not proved | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-26439 | complete |
| SF-2026-ARXIV-2606-26441 | RP-f85ba64bfb48adc3 | deep | arXiv:2606.26441v1 | SRC-ARXIV@arXiv:2606.26441v1 | https://arxiv.org/html/2606.26441v1 — §GPUSparse learned sparse retrieval with parallel inverted indices | https://arxiv.org/html/2606.26441v1 — §Retrieval quality, latency and GPU scaling experiments | https://arxiv.org/html/2606.26441v1 — §Static benchmark indexes do not prove high-churn update cost, multi-tenant isolation or cross-node scaling | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-26441 | complete |
| SF-2026-ARXIV-2606-26442 | RP-f88d7df11eb06aa1 | deep | arXiv:2606.26442v1 | SRC-ARXIV@arXiv:2606.26442v1 | https://arxiv.org/html/2606.26442v1 — §AXLE cloud infrastructure for Lean 4 utilities; remote execution and artifact handling | https://arxiv.org/html/2606.26442v1 — §Utility execution, throughput and theorem-proving workflow evaluation | https://arxiv.org/html/2606.26442v1 — §Cloud utility success does not prove generated theorem correctness beyond Lean checking or side-effect safety | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-26442 | complete |
| SF-2026-ARXIV-2606-26449 | RP-d72cae0c540f10e8 | deep | arXiv:2606.26449v1 | SRC-ARXIV@arXiv:2606.26449v1 | https://arxiv.org/html/2606.26449v1 — §ProvenAI provenance-native trace schema and evidence links | https://arxiv.org/html/2606.26449v1 — §Generated-answer trace/evidence evaluation | https://arxiv.org/html/2606.26449v1 — §Trace completeness depends on instrumented producers; provenance does not imply source truth | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-26449 | complete |
| SF-2026-ARXIV-2606-26453 | RP-12bb1a00d99b8459 | deep | arXiv:2606.26453v1 | SRC-ARXIV@arXiv:2606.26453v1 | https://arxiv.org/html/2606.26453v1 — §Micro-profiling tools as expert surrogates for LLM CUDA optimization | https://arxiv.org/html/2606.26453v1 — §Generated-kernel correctness, profiling and speed evaluation | https://arxiv.org/html/2606.26453v1 — §Evaluated CUDA tasks and toolchain only; profile-guided generation needs deterministic correctness fallback | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-26453 | complete |
| SF-2026-ARXIV-2606-26456 | RP-8eee1c405b6c239d | deep | arXiv:2606.26456v1 | SRC-ARXIV@arXiv:2606.26456v1 | https://arxiv.org/html/2606.26456v1 — §Safety-Aware Mutation Testing proposal and interaction-aware mutant model | https://arxiv.org/html/2606.26456v1 — §Simulation-based ADS testing protocol and proposed adequacy criterion | https://arxiv.org/html/2606.26456v1 — §Vision paper: no completed empirical stop-rule validation; ADS component/fault model is provisional | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-26456 | complete |
| SF-2026-ARXIV-2606-26463 | RP-8c1db9b261f0cdfb | deep | arXiv:2606.26463v1 | SRC-ARXIV@arXiv:2606.26463v1 | https://arxiv.org/html/2606.26463v1 — §Variable-delay real-time RL; lightweight gate selects state-dependent planning budget | https://arxiv.org/html/2606.26463v1 — §Pac-Man, Tetris, Snake, Speed Hex and Speed Go evaluation | https://arxiv.org/html/2606.26463v1 — §Game planners and timing model do not prove benefit under production tool latency or safety deadlines | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-26463 | complete |
| SF-2026-ARXIV-2606-26472 | RP-e3d9f91fb4679a39 | deep | arXiv:2606.26472v1 | SRC-ARXIV@arXiv:2606.26472v1 | https://arxiv.org/html/2606.26472v1 — §Epiphany score from forward-pass representation change; attention-matrix-free eviction | https://arxiv.org/html/2606.26472v1 — §Long-reasoning cache/quality evaluation and 16x feasible-context claim | https://arxiv.org/html/2606.26472v1 — §Model/task transfer and representation-score drift are unproved; quality regression requires full-KV fallback | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-26472 | complete |
| SF-2026-ARXIV-2606-26479 | RP-78e667e5a31d3387 | deep | arXiv:2606.26479v1 | SRC-ARXIV@arXiv:2606.26479v1 | https://arxiv.org/html/2606.26479v1 — §Out-of-band prompt-injection defenses organized as reference monitors and integrity policies | https://arxiv.org/html/2606.26479v1 — §Adaptive evaluation methodology against policy-aware attackers | https://arxiv.org/html/2606.26479v1 — §Position/evaluation paper; static AgentDojo results do not establish adaptive robustness | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-26479 | complete |
| SF-2026-ARXIV-2606-26488 | RP-d7749d159f45fab3 | deep | arXiv:2606.26488v1 | SRC-ARXIV@arXiv:2606.26488v1 | https://arxiv.org/html/2606.26488v1 — §Compression of recursive reasoners across precision, pruning, distillation and attention variants | https://arxiv.org/html/2606.26488v1 — §Three tasks and two recursive architectures; local vs puzzle-exact accuracy | https://arxiv.org/html/2606.26488v1 — §Edge recursive models only; token-level preservation does not imply global-reasoning preservation | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-26488 | complete |
| SF-2026-ARXIV-2606-26492 | RP-1b91478a3f182589 | deep | arXiv:2606.26492v1 | SRC-ARXIV@arXiv:2606.26492v1 | https://arxiv.org/html/2606.26492v1 — §Within-program versus leave-program-out diagnostic design | https://arxiv.org/html/2606.26492v1 — §DynFault: 5,542 traces from 38 DL programs; balanced-accuracy gap analysis | https://arxiv.org/html/2606.26492v1 — §Fault-injected programs and studied diagnosers do not prove production root-cause validity | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-26492 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2606-25274:start -->
### 2606.25274 — UC-Search: Risk-Aware Test-Time Search for Delayed Constrained Time-Series Control

**问题与旧路径。** Time-series deployments often need delayed feasible decisions, not only accurate forecasts.

**机制、状态与控制流。** `3 Problem Definition; 4 Method; 4.2 Candidate Expansion; 4.3 UC-Beam` 所定义的源特定机制用于以候选扩展或实时 gate 分配规划预算，并在超时或低置信度时回退；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `7 Limitations` 是 `UC-Search: Risk-Aware Test-Time Search for Delayed Constrained Time-Series Control` 的 source-specific 反例/局限边界；若运行条件离开 `5 Experiments; 5.1 Implemented Evidence; 6 Analysis` 的验证域，`AGENT-PLANNING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25274:start -->
Claim boundary：仅 `arXiv:2606.25274v1`；未证明边界定位 `https://arxiv.org/html/2606.25274v1 — §7 Limitations`。
<!-- claim:SF-2026-ARXIV-2606-25274:end -->
<!-- review:SF-2026-ARXIV-2606-25274:end -->

<!-- review:SF-2026-ARXIV-2606-25285:start -->
### 2606.25285 — EPTS: Elastic Post-Training Sparsity for Efficient Large Language Model Compression

**问题与旧路径。** Post-Training Sparsity (PTS) has emerged as a crucial paradigm for compressing Large Language Models to facilitate efficient deployment on resource-constrained devices.

**机制、状态与控制流。** `3 EPTS: Elastic Post-Training Sparsity` 所定义的源特定机制用于把稀疏、量化或压缩决策绑定到显存预算和质量回退；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Limitations and Discussion` 是 `EPTS: Elastic Post-Training Sparsity for Efficient Large Language Model Compression` 的 source-specific 反例/局限边界；若运行条件离开 `4 Experiments; Experimental Setup; Main Results` 的验证域，`INFER-GPU-MEMORY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25285:start -->
Claim boundary：仅 `arXiv:2606.25285v1`；未证明边界定位 `https://arxiv.org/html/2606.25285v1 — §Limitations and Discussion`。
<!-- claim:SF-2026-ARXIV-2606-25285:end -->
<!-- review:SF-2026-ARXIV-2606-25285:end -->

<!-- review:SF-2026-ARXIV-2606-25296:start -->
### 2606.25296 — SafeGen: LLM-Driven Assertion Generation and Fault Criticality Evaluation for Functional Safety

**问题与旧路径。** With advances in autonomous driving and electric vehicle technologies, functional safety has become a critical requirement in automotive chip design.

**机制、状态与控制流。** `SafeGen Methodology; Assertion Generation; Fault Criticality Evaluation` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Threats to Validity; Limitations` 是 `SafeGen: LLM-Driven Assertion Generation and Fault Criticality Evaluation for Functional Safety` 的 source-specific 反例/局限边界；若运行条件离开 `Experimental Evaluation; Functional-Safety Case Studies` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25296:start -->
Claim boundary：仅 `arXiv:2606.25296v1`；未证明边界定位 `https://arxiv.org/html/2606.25296v1 — §Threats to Validity; Limitations`。
<!-- claim:SF-2026-ARXIV-2606-25296:end -->
<!-- review:SF-2026-ARXIV-2606-25296:end -->

<!-- review:SF-2026-ARXIV-2606-25342:start -->
### 2606.25342 — Lifelong In-Context Learning with Transformers Requires Parametric Forms of Attention

**问题与旧路径。** Lifelong continual learning remains an obstacle on the path to human-like intelligence.

**机制、状态与控制流。** `Parametric Attention and Lifelong In-Context Learning formulation` 所定义的源特定机制用于把跨段记忆从隐式上下文提升为可更新的长期参数状态，并由模型路径决定写入与读取；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Discussion; finite-memory and task-family limitations` 是 `Lifelong In-Context Learning with Transformers Requires Parametric Forms of Attention` 的 source-specific 反例/局限边界；若运行条件离开 `Experiments; Lifelong sequence results` 的验证域，`MODEL-LONG-CONTEXT` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25342:start -->
Claim boundary：仅 `arXiv:2606.25342v1`；未证明边界定位 `https://arxiv.org/html/2606.25342v1 — §Discussion; finite-memory and task-family limitations`。
<!-- claim:SF-2026-ARXIV-2606-25342:end -->
<!-- review:SF-2026-ARXIV-2606-25342:end -->

<!-- review:SF-2026-ARXIV-2606-25349:start -->
### 2606.25349 — General Techniques for Reducing Key-Switching Overhead in Privacy-Preserving Two-Party Transformer Inference

**问题与旧路径。** In secure two-party Transformer inference, linear layers are typically evaluated using Fully Homomorphic Encryption (FHE) through plaintext-ciphertext or ciphertext-ciphertext matrix multiplications, where key switching primarily occurs and dominates computational overhead in both FHE-based and hybrid FHE-MPC systems.

**机制、状态与控制流。** `IV Two-Party Secure Inference Algorithm; V Storage-Communication Trade-off; VI Fused Relinearization and Rotation` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `VIII Conclusion; exact-v1 analytical-evaluation-only note` 是 `General Techniques for Reducing Key-Switching Overhead in Privacy-Preserving Two-Party Transformer Inference` 的 source-specific 反例/局限边界；若运行条件离开 `VII Evaluation` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25349:start -->
Claim boundary：仅 `arXiv:2606.25349v1`；未证明边界定位 `https://arxiv.org/html/2606.25349v1 — §VIII Conclusion; exact-v1 analytical-evaluation-only note`。
<!-- claim:SF-2026-ARXIV-2606-25349:end -->
<!-- review:SF-2026-ARXIV-2606-25349:end -->

<!-- review:SF-2026-ARXIV-2606-25353:start -->
### 2606.25353 — Cache-Resident LLM Inference in GB-Scale Last-Level Caches

**问题与旧路径。** Large language model (LLM) inference is increasingly dominated by data movement across the memory hierarchy.

**机制、状态与控制流。** `3 Architecture; 3.1 Weight-Attention Decoupled Organization; 4 Implementation` 所定义的源特定机制用于把权重、attention 与 cache-blocking 路径拆成可独立放置和优化的前缀计算状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `7 Discussion; 7.2 Future Works` 是 `Cache-Resident LLM Inference in GB-Scale Last-Level Caches` 的 source-specific 反例/局限边界；若运行条件离开 `5 Experiment Setup; 6 Evaluation` 的验证域，`INFER-PREFILL` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25353:start -->
Claim boundary：仅 `arXiv:2606.25353v1`；未证明边界定位 `https://arxiv.org/html/2606.25353v1 — §7 Discussion; 7.2 Future Works`。
<!-- claim:SF-2026-ARXIV-2606-25353:end -->
<!-- review:SF-2026-ARXIV-2606-25353:end -->

<!-- review:SF-2026-ARXIV-2606-25366:start -->
### 2606.25366 — Reliability-Asymmetric Spacecraft Autonomy: Co-Designing a Capable Learned GNC Stack with a Verified, Adaptation-Aware Runtime Shield

**问题与旧路径。** Deep-space missions need onboard autonomy that is both capable and certifiable.

**机制、状态与控制流。** `III System and Testbed; IV Verified Runtime Shield; VII Adaptation-Aware Runtime Assurance` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `XI-D Limitations` 是 `Reliability-Asymmetric Spacecraft Autonomy: Co-Designing a Capable Learned GNC Stack with a Verified, Adaptation-Aware Runtime Shield` 的 source-specific 反例/局限边界；若运行条件离开 `VIII Robustness; IX Integrated Evaluation` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25366:start -->
Claim boundary：仅 `arXiv:2606.25366v1`；未证明边界定位 `https://arxiv.org/html/2606.25366v1 — §XI-D Limitations`。
<!-- claim:SF-2026-ARXIV-2606-25366:end -->
<!-- review:SF-2026-ARXIV-2606-25366:end -->

<!-- review:SF-2026-ARXIV-2606-25371:start -->
### 2606.25371 — Conformal Recovery-Deadline Certificates for Runtime Assurance of Adapting Controllers

**问题与旧路径。** Runtime assurance (RTA) protects a safety-critical system by switching from an advanced controller to a verified safe controller when a monitored condition is violated.

**机制、状态与控制流。** `III Problem Setup; IV Conformal Recovery-Deadline Certificate` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `VI-D Limitations` 是 `Conformal Recovery-Deadline Certificates for Runtime Assurance of Adapting Controllers` 的 source-specific 反例/局限边界；若运行条件离开 `V Experiments` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25371:start -->
Claim boundary：仅 `arXiv:2606.25371v1`；未证明边界定位 `https://arxiv.org/html/2606.25371v1 — §VI-D Limitations`。
<!-- claim:SF-2026-ARXIV-2606-25371:end -->
<!-- review:SF-2026-ARXIV-2606-25371:end -->

<!-- review:SF-2026-ARXIV-2606-25388:start -->
### 2606.25388 — TabClean: Reusable LLM-Synthesized Programs for Tabular Data Cleaning

**问题与旧路径。** Reliable analytics and machine-learning pipelines depend on clean tabular data, yet production tables often contain missing values, typographical errors, inconsistent formats, violated dependencies, unit mismatches, and ambiguous categorical values.

**机制、状态与控制流。** `III System Overview; IV Methodology; IV-F Execution-Guided Validation and Control` 所定义的源特定机制用于把数据选择、校准或验证结果变成训练前可审计的数据控制状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `VII Discussion and Future Work` 是 `TabClean: Reusable LLM-Synthesized Programs for Tabular Data Cleaning` 的 source-specific 反例/局限边界；若运行条件离开 `V Experimental Evaluation; V-A Experimental Setup` 的验证域，`TRAIN-DATA` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25388:start -->
Claim boundary：仅 `arXiv:2606.25388v1`；未证明边界定位 `https://arxiv.org/html/2606.25388v1 — §VII Discussion and Future Work`。
<!-- claim:SF-2026-ARXIV-2606-25388:end -->
<!-- review:SF-2026-ARXIV-2606-25388:end -->

<!-- review:SF-2026-ARXIV-2606-25410:start -->
### 2606.25410 — DFMU: Data-Frugal Machine Unlearning

**问题与旧路径。** Machine unlearning is an emerging domain that ensures the safe removal of elements (includes concepts, attributes, entity and class) from the trained model along with least drop in model performance.

**机制、状态与控制流。** `3 Proposed Method; 3.1 Importance Score Calculation; 3.2 Weight Rescaling` 所定义的源特定机制用于把数据选择、校准或验证结果变成训练前可审计的数据控制状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `5 Conclusion; class-forgetting experimental scope` 是 `DFMU: Data-Frugal Machine Unlearning` 的 source-specific 反例/局限边界；若运行条件离开 `4 Experiments; 4.1 Experimental Setup; 4.4 Results` 的验证域，`TRAIN-DATA` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25410:start -->
Claim boundary：仅 `arXiv:2606.25410v1`；未证明边界定位 `https://arxiv.org/html/2606.25410v1 — §5 Conclusion; class-forgetting experimental scope`。
<!-- claim:SF-2026-ARXIV-2606-25410:end -->
<!-- review:SF-2026-ARXIV-2606-25410:end -->

<!-- review:SF-2026-ARXIV-2606-25426:start -->
### 2606.25426 — Above the Inner Loop: Exceeding Accelerate at LLM Prefill GEMM on the M1 AMX

**问题与旧路径。** On Apple Silicon the fp32 GEMMs dominating LLM prefill are dispatched by Accelerate to a matrix coprocessor (AMX) on the M1-M3.

**机制、状态与控制流。** `3 Method; 3.1 Three-level cache blocking; 3.2 Weight pre-packing` 所定义的源特定机制用于把权重、attention 与 cache-blocking 路径拆成可独立放置和优化的前缀计算状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `6 Conclusion; Limitations` 是 `Above the Inner Loop: Exceeding Accelerate at LLM Prefill GEMM on the M1 AMX` 的 source-specific 反例/局限边界；若运行条件离开 `4 Evaluation; 4.1 Experimental setup; 4.7 End-to-end prefill GEMM measurement` 的验证域，`INFER-PREFILL` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25426:start -->
Claim boundary：仅 `arXiv:2606.25426v1`；未证明边界定位 `https://arxiv.org/html/2606.25426v1 — §6 Conclusion; Limitations`。
<!-- claim:SF-2026-ARXIV-2606-25426:end -->
<!-- review:SF-2026-ARXIV-2606-25426:end -->

<!-- review:SF-2026-ARXIV-2606-25447:start -->
### 2606.25447 — The Interplay of Harness Design and Post-Training in LLM Agents

**问题与旧路径。** Tool-integrated LLM agents are often wrapped within a harness: the scaffolding that determines which tools are exposed, how they are described, and what auxiliary information accompanies each per-step observation.

**机制、状态与控制流。** `3 Experiment Setup; 3.2 Harness; 3.3 Tool Schema; 3.4 Task Type` 所定义的源特定机制用于把执行 harness、远端 utility 与 artifact handoff 变成可观测工作流状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `B Benchmark Details; C Experimental Details; stated ALFWorld boundary` 是 `The Interplay of Harness Design and Post-Training in LLM Agents` 的 source-specific 反例/局限边界；若运行条件离开 `4 Analysis; 4.1 Evaluation Protocol; 4.4 OOD Robustness` 的验证域，`AGENT-WORKFLOW` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25447:start -->
Claim boundary：仅 `arXiv:2606.25447v1`；未证明边界定位 `https://arxiv.org/html/2606.25447v1 — §B Benchmark Details; C Experimental Details; stated ALFWorld boundary`。
<!-- claim:SF-2026-ARXIV-2606-25447:end -->
<!-- review:SF-2026-ARXIV-2606-25447:end -->

<!-- review:SF-2026-ARXIV-2606-25449:start -->
### 2606.25449 — Reclaim Evaluation: A Lossy Memory Is Worse Than an Empty One

**问题与旧路径。** A language model's memory can be worse than no memory at all when the model or its interface is disposed to act on it: a memory that keeps a wrong conclusion but drops the work behind it leads a model to re-emit the stale value as a confident answer, where an empty memory leads it to abstain.

**机制、状态与控制流。** `3 Brittle Memory and Reclaim Evaluation; 3.2 Reclaim Protocol` 所定义的源特定机制用于把动态记忆写入、回收与失效变成有 owner 的持久状态迁移；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `7 Limitations` 是 `Reclaim Evaluation: A Lossy Memory Is Worse Than an Empty One` 的 source-specific 反例/局限边界；若运行条件离开 `4 Experimental Setup; 5 Results; 5.7 Boundary of the Fix` 的验证域，`AGENT-MEMORY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25449:start -->
Claim boundary：仅 `arXiv:2606.25449v1`；未证明边界定位 `https://arxiv.org/html/2606.25449v1 — §7 Limitations`。
<!-- claim:SF-2026-ARXIV-2606-25449:end -->
<!-- review:SF-2026-ARXIV-2606-25449:end -->

<!-- review:SF-2026-ARXIV-2606-25453:start -->
### 2606.25453 — EmuGEMM: Fused Tensor Core Kernels for Precision Emulation in Matrix Multiplication

**问题与旧路径。** Modern GPUs devote an increasing silicon budget to low-precision matrix-multiplication units, widening the precision-throughput gap for scientific computing workloads.

**机制、状态与控制流。** `III EmuGEMM-I; IV EmuGEMM-II` 所定义的源特定机制用于以可验证搜索或 profiling 反馈驱动 kernel 选择，同时保留确定性正确性路径；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `V-G Limitations` 是 `EmuGEMM: Fused Tensor Core Kernels for Precision Emulation in Matrix Multiplication` 的 source-specific 反例/局限边界；若运行条件离开 `V Evaluation; V-B Experimental Setup; V-F Precision-Throughput-Memory Trade-off` 的验证域，`INFER-TENSORRT-LLM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25453:start -->
Claim boundary：仅 `arXiv:2606.25453v1`；未证明边界定位 `https://arxiv.org/html/2606.25453v1 — §V-G Limitations`。
<!-- claim:SF-2026-ARXIV-2606-25453:end -->
<!-- review:SF-2026-ARXIV-2606-25453:end -->

<!-- review:SF-2026-ARXIV-2606-25467:start -->
### 2606.25467 — RQ-SAFE: Coupled Request-Resource Scheduling for Online Edge SFC-DAGs

**问题与旧路径。** Intent-driven edge services allow multiple virtual network function (VNF) segments in a service function chain directed acyclic graph (SFC-DAG) to be locally reordered without changing service semantics, creating richer request-side orchestration freedom.

**机制、状态与控制流。** `III Request-Resource Coupling Model; IV RQ-SAFE Online Orchestration` 所定义的源特定机制用于让在线编排器共同持有请求资源耦合、准入和降级状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `D-B Runtime Boundary and Fallback; G Implementation Scope Clarifications` 是 `RQ-SAFE: Coupled Request-Resource Scheduling for Online Edge SFC-DAGs` 的 source-specific 反例/局限边界；若运行条件离开 `V Experimental Evaluation; V-A Experimental Setup` 的验证域，`INFER-SCHEDULING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25467:start -->
Claim boundary：仅 `arXiv:2606.25467v1`；未证明边界定位 `https://arxiv.org/html/2606.25467v1 — §D-B Runtime Boundary and Fallback; G Implementation Scope Clarifications`。
<!-- claim:SF-2026-ARXIV-2606-25467:end -->
<!-- review:SF-2026-ARXIV-2606-25467:end -->

<!-- review:SF-2026-ARXIV-2606-25487:start -->
### 2606.25487 — How Reliable Is Your Jailbreak Judge? Calibration and Adversarial Robustness of Automated ASR Scoring

**问题与旧路径。** Almost every paper on LLM jailbreaks and prompt injection reports an attack-success rate (ASR), and that number is assigned not by people but by an automated judge: either a safety classifier trained for the task, or a general chat model prompted to grade.

**机制、状态与控制流。** `3 Setup; Appendix A Prompts, wrappers, and attack configuration` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `6 Limitations` 是 `How Reliable Is Your Jailbreak Judge? Calibration and Adversarial Robustness of Automated ASR Scoring` 的 source-specific 反例/局限边界；若运行条件离开 `4 Results; 4.1 Calibration against human labels; 4.3 white-box attack` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25487:start -->
Claim boundary：仅 `arXiv:2606.25487v1`；未证明边界定位 `https://arxiv.org/html/2606.25487v1 — §6 Limitations`。
<!-- claim:SF-2026-ARXIV-2606-25487:end -->
<!-- review:SF-2026-ARXIV-2606-25487:end -->

<!-- review:SF-2026-ARXIV-2606-25514:start -->
### 2606.25514 — Unlocking Model Potentials Through Adaptive Multi-Agent Scaffolding for Efficient Issue Resolution

**问题与旧路径。** Resolving issues with ambiguous and incomplete descriptions, particularly concerning complex bugs, requires a sophisticated, long-horizon workflow.

**机制、状态与控制流。** `2 Adaptive Multi-Agent Issue Resolution; 2.6 Event-Driven Synchronous Communication` 所定义的源特定机制用于把事件通信、角色分工与失败升级纳入多 Agent 协调状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `5 Threats to Validity` 是 `Unlocking Model Potentials Through Adaptive Multi-Agent Scaffolding for Efficient Issue Resolution` 的 source-specific 反例/局限边界；若运行条件离开 `3 Evaluation; 3.2 Analysis of Exclusive Fixes and Failures` 的验证域，`AGENT-MULTI-AGENT` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25514:start -->
Claim boundary：仅 `arXiv:2606.25514v1`；未证明边界定位 `https://arxiv.org/html/2606.25514v1 — §5 Threats to Validity`。
<!-- claim:SF-2026-ARXIV-2606-25514:end -->
<!-- review:SF-2026-ARXIV-2606-25514:end -->

<!-- review:SF-2026-ARXIV-2606-25519:start -->
### 2606.25519 — Quantization Inflates Reasoning: Token Inflation as a Hidden Cost of Low-Bit Reasoning Models

**问题与旧路径。** Quantization is widely used to reduce the inference cost of large language models, but its effect on reasoning models is not fully captured by final-answer accuracy or per-token latency.

**机制、状态与控制流。** `3 Experimental Setup; 5 Quantization Inflates Reasoning Tokens; 6 Anatomy` 所定义的源特定机制用于把稀疏、量化或压缩决策绑定到显存预算和质量回退；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `7 Can We Reduce Reasoning-Token Inflation; D.2 Model details` 是 `Quantization Inflates Reasoning: Token Inflation as a Hidden Cost of Low-Bit Reasoning Models` 的 source-specific 反例/局限边界；若运行条件离开 `D Additional evaluation details; D.1 Benchmarks and evaluation protocol` 的验证域，`INFER-GPU-MEMORY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25519:start -->
Claim boundary：仅 `arXiv:2606.25519v1`；未证明边界定位 `https://arxiv.org/html/2606.25519v1 — §7 Can We Reduce Reasoning-Token Inflation; D.2 Model details`。
<!-- claim:SF-2026-ARXIV-2606-25519:end -->
<!-- review:SF-2026-ARXIV-2606-25519:end -->

<!-- review:SF-2026-ARXIV-2606-25532:start -->
### 2606.25532 — Agentic evolution of physically constrained foundation models

**问题与旧路径。** Artificial intelligence increasingly drives automated scientific discovery, yet contemporary generalist agents lack physical grounding, frequently hallucinating hardware-incompatible designs.

**机制、状态与控制流。** `Physically constrained multi-agent discovery engine; Evolutionary Knowledge Graph and algorithmic chain of thought` 所定义的源特定机制用于把硬件约束和发现链纳入平台设计候选的验收边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Exact-v1 research-prototype and evaluated hardware-design boundary` 是 `Agentic evolution of physically constrained foundation models` 的 source-specific 反例/局限边界；若运行条件离开 `Hardware-compliance evaluation and discovered-system validation` 的验证域，`PLATFORM-FOUNDATIONS` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25532:start -->
Claim boundary：仅 `arXiv:2606.25532v1`；未证明边界定位 `https://arxiv.org/html/2606.25532v1 — §Exact-v1 research-prototype and evaluated hardware-design boundary`。
<!-- claim:SF-2026-ARXIV-2606-25532:end -->
<!-- review:SF-2026-ARXIV-2606-25532:end -->

<!-- review:SF-2026-ARXIV-2606-25548:start -->
### 2606.25548 — Concept Removal for Frontier Image Generative Models

**问题与旧路径。** Image generative models are trained on massive, largely uncurated internet-scale datasets that contain undesirable visual concepts.

**机制、状态与控制流。** `4 Transcoders-based Concept Removal; 4.1 BLOCK Framework` 所定义的源特定机制用于把数据选择、校准或验证结果变成训练前可审计的数据控制状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `G Limitations; D.1 Model-Architecture-Dependent Subtleties` 是 `Concept Removal for Frontier Image Generative Models` 的 source-specific 反例/局限边界；若运行条件离开 `5 Empirical Evaluation; 5.1 Experimental Setup; 5.4 Robustness` 的验证域，`TRAIN-DATA` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25548:start -->
Claim boundary：仅 `arXiv:2606.25548v1`；未证明边界定位 `https://arxiv.org/html/2606.25548v1 — §G Limitations; D.1 Model-Architecture-Dependent Subtleties`。
<!-- claim:SF-2026-ARXIV-2606-25548:end -->
<!-- review:SF-2026-ARXIV-2606-25548:end -->

<!-- review:SF-2026-ARXIV-2606-25575:start -->
### 2606.25575 — One Body, Two Minds: Variable Autonomy Approach for a Co-embodied Robotic Hand

**问题与旧路径。** Assistive robotic systems face a fundamental trade-off: fully autonomous systems lack user agency, while fully user-controlled systems demand continuous cognitive effort.

**机制、状态与控制流。** `Variable-autonomy architecture; task-phase authority transfer; always-available release gesture` 所定义的源特定机制用于把任务阶段、共享自治等级和人工接管手势纳入动作控制回路；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Single wearable-hand embodiment, known objects, five tools, and short-horizon study` 是 `One Body, Two Minds: Variable Autonomy Approach for a Co-embodied Robotic Hand` 的 source-specific 反例/局限边界；若运行条件离开 `44-participant user study; five bimanual tasks; policy-variant success` 的验证域，`MULTIMODAL-EMBODIED-VLA` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25575:start -->
Claim boundary：仅 `arXiv:2606.25575v1`；未证明边界定位 `https://arxiv.org/html/2606.25575v1 — §Single wearable-hand embodiment, known objects, five tools, and short-horizon study`。
<!-- claim:SF-2026-ARXIV-2606-25575:end -->
<!-- review:SF-2026-ARXIV-2606-25575:end -->

<!-- review:SF-2026-ARXIV-2606-25592:start -->
### 2606.25592 — VPA-Guard: Defending and Benchmarking Image-to-Video Generation Against Visual Prompt Attacks

**问题与旧路径。** Recent advancements in Image-to-Video (I2V) generation have transformed input images from simple appearance references into interactive control interfaces where visual cues such as arrows, sketches, and emojis orchestrate complex video dynamics with unprecedented controllability.

**机制、状态与控制流。** `2 Visual Prompt Attack and Defense; 2.2 VPA-Guard` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `E.1 Limitations; E.4 Human-in-the-loop Discussion` 是 `VPA-Guard: Defending and Benchmarking Image-to-Video Generation Against Visual Prompt Attacks` 的 source-specific 反例/局限边界；若运行条件离开 `3 VVA-Bench; 3.2 Evaluation Protocol; 4 Main Experiments` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25592:start -->
Claim boundary：仅 `arXiv:2606.25592v1`；未证明边界定位 `https://arxiv.org/html/2606.25592v1 — §E.1 Limitations; E.4 Human-in-the-loop Discussion`。
<!-- claim:SF-2026-ARXIV-2606-25592:end -->
<!-- review:SF-2026-ARXIV-2606-25592:end -->

<!-- review:SF-2026-ARXIV-2606-25605:start -->
### 2606.25605 — Constraint Tax in Open-Weight LLMs: An Empirical Study of Tool Calling Suppression Under Structured Output Constraints

**问题与旧路径。** Tool Calling and Structured Output are two core capabilities of modern Agent systems, yet their interaction under joint deployment conditions remains insufficiently understood.

**机制、状态与控制流。** `3 Problem Definition; 4 Experimental Setup; 7 Transparent Two-Pass Execution` 所定义的源特定机制用于把工具候选、模拟执行和恢复路径置于真实副作用 commit 之前；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `7.5 Failure Cases and Limitations; 8.4 Limitations` 是 `Constraint Tax in Open-Weight LLMs: An Empirical Study of Tool Calling Suppression Under Structured Output Constraints` 的 source-specific 反例/局限边界；若运行条件离开 `5 Empirical Findings; 7.3 Experimental Evaluation; 7.4 Cost and Latency` 的验证域，`AGENT-TOOL-CALLING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25605:start -->
Claim boundary：仅 `arXiv:2606.25605v1`；未证明边界定位 `https://arxiv.org/html/2606.25605v1 — §7.5 Failure Cases and Limitations; 8.4 Limitations`。
<!-- claim:SF-2026-ARXIV-2606-25605:end -->
<!-- review:SF-2026-ARXIV-2606-25605:end -->

<!-- review:SF-2026-ARXIV-2606-25608:start -->
### 2606.25608 — An Approach for a Supporting Multi-LLM System for Automated Certification Based on the German IT-Grundschutz

**问题与旧路径。** This paper presents a novel approach to perform semi-automated BSI IT-Grundschutz certification using a MultiLarge Language Model system (MLS) with Hybrid RetrievalAugmented Generation (HybridRAG).

**机制、状态与控制流。** `V Proposed Method: Multi-LLM System; V-B Multi-LLM architecture with HybridRAG` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `V-C Restrictions of our architecture; VII Future Research` 是 `An Approach for a Supporting Multi-LLM System for Automated Certification Based on the German IT-Grundschutz` 的 source-specific 反例/局限边界；若运行条件离开 `VI Initial Evaluation` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25608:start -->
Claim boundary：仅 `arXiv:2606.25608v1`；未证明边界定位 `https://arxiv.org/html/2606.25608v1 — §V-C Restrictions of our architecture; VII Future Research`。
<!-- claim:SF-2026-ARXIV-2606-25608:end -->
<!-- review:SF-2026-ARXIV-2606-25608:end -->

<!-- review:SF-2026-ARXIV-2606-25622:start -->
### 2606.25622 — Probabilistic Agents in Deterministic Audits: Evaluating Multi-Agent Systems for Automated Audits Based on the German IT-Grundschutz

**问题与旧路径。** The NIS-2 Directive mandates robust Risk Management from thousands of small and medium enterprises.

**机制、状态与控制流。** `IV Theoretical Framework: MAS Architecture and Experimental Setup` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `VI Limitations & Future Work` 是 `Probabilistic Agents in Deterministic Audits: Evaluating Multi-Agent Systems for Automated Audits Based on the German IT-Grundschutz` 的 source-specific 反例/局限边界；若运行条件离开 `V Results & Discussion` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25622:start -->
Claim boundary：仅 `arXiv:2606.25622v1`；未证明边界定位 `https://arxiv.org/html/2606.25622v1 — §VI Limitations & Future Work`。
<!-- claim:SF-2026-ARXIV-2606-25622:end -->
<!-- review:SF-2026-ARXIV-2606-25622:end -->

<!-- review:SF-2026-ARXIV-2606-25656:start -->
### 2606.25656 — Is GraphRAG Needed? From Basic RAG to Graph-/Agentic Solutions with Context Optimization

**问题与旧路径。** As advanced RAG variants like GraphRAG and Agentic RAG emerge, one leading question is when and how to use them.

**机制、状态与控制流。** `3 Methods; 3.2 Regular RAG; 3.3 GraphRAG; 3.4 Modular and Agentic RAG; 3.5 Context Optimization` 所定义的源特定机制用于把检索索引、量化、GPU scorer 与更新一致性拆成显式数据面状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `6 Conclusions and future work; C Retrieval-Generation Gap` 是 `Is GraphRAG Needed? From Basic RAG to Graph-/Agentic Solutions with Context Optimization` 的 source-specific 反例/局限边界；若运行条件离开 `4 Experimental setup; 5 Experimental results` 的验证域，`AGENT-RAG` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25656:start -->
Claim boundary：仅 `arXiv:2606.25656v1`；未证明边界定位 `https://arxiv.org/html/2606.25656v1 — §6 Conclusions and future work; C Retrieval-Generation Gap`。
<!-- claim:SF-2026-ARXIV-2606-25656:end -->
<!-- review:SF-2026-ARXIV-2606-25656:end -->

<!-- review:SF-2026-ARXIV-2606-25658:start -->
### 2606.25658 — Towards a Dynamic and Fixed-budget Memory Bank for Efficient Streaming Video Understanding

**问题与旧路径。** Currently, streaming video understanding is still a daunting task for existing \emph{multimodal large language models} (MLLMs).

**机制、状态与控制流。** `3 Method; 3.2 Online Semantic Basis; 3.3 Dynamic Visual Memory Bank` 所定义的源特定机制用于把动态记忆写入、回收与失效变成有 owner 的持久状态迁移；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `A Limitations` 是 `Towards a Dynamic and Fixed-budget Memory Bank for Efficient Streaming Video Understanding` 的 source-specific 反例/局限边界；若运行条件离开 `4 Experiment; 4.1 Benchmarks and Metrics; 4.2 Implementation` 的验证域，`AGENT-MEMORY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25658:start -->
Claim boundary：仅 `arXiv:2606.25658v1`；未证明边界定位 `https://arxiv.org/html/2606.25658v1 — §A Limitations`。
<!-- claim:SF-2026-ARXIV-2606-25658:end -->
<!-- review:SF-2026-ARXIV-2606-25658:end -->

<!-- review:SF-2026-ARXIV-2606-25674:start -->
### 2606.25674 — BitNet Text Embeddings

**问题与旧路径。** LLM-based text embedders have substantially improved retrieval and semantic representation quality, but their deployment remains costly: large backbone models slow down embedding inference, while high-dimensional full-precision embeddings impose substantial storage and bandwidth overhead on large-scale indexes.

**机制、状态与控制流。** `3 Method; 3.2 Low-bit Embedding Backbone; 3.5 Multi-precision Embedding Quantization` 所定义的源特定机制用于把检索索引、量化、GPU scorer 与更新一致性拆成显式数据面状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `4.4 Analysis; task-type sensitivity to quantization` 是 `BitNet Text Embeddings` 的 source-specific 反例/局限边界；若运行条件离开 `4 Experiments; 4.1 Experimental Setup; B Evaluation Details` 的验证域，`AGENT-RAG` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25674:start -->
Claim boundary：仅 `arXiv:2606.25674v1`；未证明边界定位 `https://arxiv.org/html/2606.25674v1 — §4.4 Analysis; task-type sensitivity to quantization`。
<!-- claim:SF-2026-ARXIV-2606-25674:end -->
<!-- review:SF-2026-ARXIV-2606-25674:end -->

<!-- review:SF-2026-ARXIV-2606-25700:start -->
### 2606.25700 — Memory-Efficient Policy Libraries with Low-Rank Adaptation in Reinforcement Learning

**问题与旧路径。** When fine-tuning Large Language Models (LLMs), there has been success in minimizing both memory usage and computation with Parameter-Efficient Fine-Tuning (PEFT), like Low Rank Adaptation (LoRA).

**机制、状态与控制流。** `III Methods; III-B Training; III-C Architecture` 所定义的源特定机制用于把秩、适配器容量与计算预算绑定为显式训练配置；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `V Discussion; V-A Choice of rank; V-C Computation` 是 `Memory-Efficient Policy Libraries with Low-Rank Adaptation in Reinforcement Learning` 的 source-specific 反例/局限边界；若运行条件离开 `IV Results; IV-B Computation calculation` 的验证域，`TRAIN-LORA` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25700:start -->
Claim boundary：仅 `arXiv:2606.25700v1`；未证明边界定位 `https://arxiv.org/html/2606.25700v1 — §V Discussion; V-A Choice of rank; V-C Computation`。
<!-- claim:SF-2026-ARXIV-2606-25700:end -->
<!-- review:SF-2026-ARXIV-2606-25700:end -->

<!-- review:SF-2026-ARXIV-2606-25705:start -->
### 2606.25705 — GUI agent: Guided Exploration of User-Sensitive Screens

**问题与旧路径。** LLM agents are increasingly being used to automate tasks for users within an open GUI environment.

**机制、状态与控制流。** `3 Methodology; 3.1 Query Selection, Expansion and Saturation; 3.2 Roll-out with Emulator` 所定义的源特定机制用于把工具候选、模拟执行和恢复路径置于真实副作用 commit 之前；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `5 Conclusion; short-paper and emulator-only boundary` 是 `GUI agent: Guided Exploration of User-Sensitive Screens` 的 source-specific 反例/局限边界；若运行条件离开 `4 Experiments and Results` 的验证域，`AGENT-TOOL-CALLING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25705:start -->
Claim boundary：仅 `arXiv:2606.25705v1`；未证明边界定位 `https://arxiv.org/html/2606.25705v1 — §5 Conclusion; short-paper and emulator-only boundary`。
<!-- claim:SF-2026-ARXIV-2606-25705:end -->
<!-- review:SF-2026-ARXIV-2606-25705:end -->

<!-- review:SF-2026-ARXIV-2606-25721:start -->
### 2606.25721 — Tracing Target Answers in Poisoned Retrieval Corpora via Token Influence Attribution

**问题与旧路径。** Retrieval-Augmented Generation (RAG) systems are vulnerable to corpus poisoning attacks that manipulate model outputs through malicious retrieved documents.

**机制、状态与控制流。** `4 Method; 4.1 Keyword Searching; 4.2 Secondary Verification` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `6 Discussion; baseline and hyperparameter sensitivity` 是 `Tracing Target Answers in Poisoned Retrieval Corpora via Token Influence Attribution` 的 source-specific 反例/局限边界；若运行条件离开 `5 Evaluation; 5.1 Setup; 5.2 Results` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25721:start -->
Claim boundary：仅 `arXiv:2606.25721v1`；未证明边界定位 `https://arxiv.org/html/2606.25721v1 — §6 Discussion; baseline and hyperparameter sensitivity`。
<!-- claim:SF-2026-ARXIV-2606-25721:end -->
<!-- review:SF-2026-ARXIV-2606-25721:end -->

<!-- review:SF-2026-ARXIV-2606-25759:start -->
### 2606.25759 — NEURON-Fabric: Architecture-Runtime Co-Design for Controlled Low-Bit Gradient Communication

**问题与旧路径。** Large-scale neural-network training repeatedly aggregates gradients across devices, making communication a central cost in distributed learning.

**机制、状态与控制流。** `3 System Overview; 4 Operating-Profile Calibration; 5 Runtime Binding and Bucket Routing` 所定义的源特定机制用于把集群运行剖面映射为运行时 bucket 与并行绑定状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `9 Limitations and Future Work; A.4 Evaluation Environment and Measurement Boundary` 是 `NEURON-Fabric: Architecture-Runtime Co-Design for Controlled Low-Bit Gradient Communication` 的 source-specific 反例/局限边界；若运行条件离开 `7 Closed-Loop Cluster Evaluation; 7.1 Evaluation Setup and Scope` 的验证域，`TRAIN-DISTRIBUTED-TRAINING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25759:start -->
Claim boundary：仅 `arXiv:2606.25759v1`；未证明边界定位 `https://arxiv.org/html/2606.25759v1 — §9 Limitations and Future Work; A.4 Evaluation Environment and Measurement Boundary`。
<!-- claim:SF-2026-ARXIV-2606-25759:end -->
<!-- review:SF-2026-ARXIV-2606-25759:end -->

<!-- review:SF-2026-ARXIV-2606-25760:start -->
### 2606.25760 — Uncertainty Quantification for Computer-Use Agents: A Benchmark across Vision-Language Models and GUI Grounding Datasets

**问题与旧路径。** Computer-use agents turn vision-language model (VLM) predictions into executable GUI clicks, so reliable uncertainty estimates are essential for rejection, calibration, miss-severity ranking, and spatial safety regions.

**机制、状态与控制流。** `3 Benchmark and Evaluation Protocol; 7 Inductive-Conformal Click Disks` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `A4 Out-of-distribution analysis; A5 Methods deferred; A25 vendor protocol details` 是 `Uncertainty Quantification for Computer-Use Agents: A Benchmark across Vision-Language Models and GUI Grounding Datasets` 的 source-specific 反例/局限边界；若运行条件离开 `4 UQ Generalizes Selectively; 5 Graded Error and Calibration` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25760:start -->
Claim boundary：仅 `arXiv:2606.25760v1`；未证明边界定位 `https://arxiv.org/html/2606.25760v1 — §A4 Out-of-distribution analysis; A5 Methods deferred; A25 vendor protocol details`。
<!-- claim:SF-2026-ARXIV-2606-25760:end -->
<!-- review:SF-2026-ARXIV-2606-25760:end -->

<!-- review:SF-2026-ARXIV-2606-25782:start -->
### 2606.25782 — Do Encoders Suffice? A Systematic Comparison of Encoder and Decoder Safety Judges for LLM Adversarial Evaluation

**问题与旧路径。** With the widespread adoption of large language models (LLMs) in chatbots and everyday applications, companies increasingly need guardrails that are effective while remaining low-cost and low-latency.

**机制、状态与控制流。** `2 Dataset; 3 Adversarial Attack Methodology; 4 Safety Judge Panel` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `OOD holdout and multi-turn attack boundary; 0.B Inference Throughput and Latency` 是 `Do Encoders Suffice? A Systematic Comparison of Encoder and Decoder Safety Judges for LLM Adversarial Evaluation` 的 source-specific 反例/局限边界；若运行条件离开 `5 Evaluation Protocol; 6 Results; 6.3 Cost and Latency Trade-offs` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25782:start -->
Claim boundary：仅 `arXiv:2606.25782v1`；未证明边界定位 `https://arxiv.org/html/2606.25782v1 — §OOD holdout and multi-turn attack boundary; 0.B Inference Throughput and Latency`。
<!-- claim:SF-2026-ARXIV-2606-25782:end -->
<!-- review:SF-2026-ARXIV-2606-25782:end -->

<!-- review:SF-2026-ARXIV-2606-25797:start -->
### 2606.25797 — Confidence Sequences for Online Statistical Model Checking of Markov Decision Processes

**问题与旧路径。** Markov decision processes (MDPs) are a classic model of decision making under uncertainty, exhibiting both non-deterministic choice as well as probabilistic uncertainty.

**机制、状态与控制流。** `3 Improving Online MDP-SMC; 3.2 Confidence Sequences; 3.4 Confidence Sequence MDP-SMC` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `0.A Assumptions on Sampling Access and Knowledge; 0.B Reusing Confidence is Incorrect` 是 `Confidence Sequences for Online Statistical Model Checking of Markov Decision Processes` 的 source-specific 反例/局限边界；若运行条件离开 `4 Implementation and Experimental Evaluation` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25797:start -->
Claim boundary：仅 `arXiv:2606.25797v1`；未证明边界定位 `https://arxiv.org/html/2606.25797v1 — §0.A Assumptions on Sampling Access and Knowledge; 0.B Reusing Confidence is Incorrect`。
<!-- claim:SF-2026-ARXIV-2606-25797:end -->
<!-- review:SF-2026-ARXIV-2606-25797:end -->

<!-- review:SF-2026-ARXIV-2606-25819:start -->
### 2606.25819 — Beyond Function Calling: Benchmarking Tool-Using Agents under Tool-Environment Unreliability

**问题与旧路径。** Large language models are increasingly deployed as agents that solve tasks by interacting with external tool environments.

**机制、状态与控制流。** `ToolBench-X; Problem Formulation; Benchmark Construction; Reliability Hazard Injection` 所定义的源特定机制用于把工具候选、模拟执行和恢复路径置于真实副作用 commit 之前；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Canonical recovery-path construction and five injected-hazard boundary` 是 `Beyond Function Calling: Benchmarking Tool-Using Agents under Tool-Environment Unreliability` 的 source-specific 反例/局限边界；若运行条件离开 `Experiments; Experimental Setup; Further Analysis; Error Analysis` 的验证域，`AGENT-TOOL-CALLING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25819:start -->
Claim boundary：仅 `arXiv:2606.25819v1`；未证明边界定位 `https://arxiv.org/html/2606.25819v1 — §Canonical recovery-path construction and five injected-hazard boundary`。
<!-- claim:SF-2026-ARXIV-2606-25819:end -->
<!-- review:SF-2026-ARXIV-2606-25819:end -->

<!-- review:SF-2026-ARXIV-2606-25838:start -->
### 2606.25838 — Edges Before Embeddings: A Confidence-Aware Blur Gate for Vision-Language Pipelines

**问题与旧路径。** Production vision pipelines silently degrade on blurry input, wasting compute on downstream OCR, retrieval, and vision-language model (VLM) calls that cannot recover a usable output.

**机制、状态与控制流。** `III Method; IV Confidence-Aware Routing` 所定义的源特定机制用于让路由器基于请求置信度持有后端选择与回退权；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `VII-C Limitations and future work` 是 `Edges Before Embeddings: A Confidence-Aware Blur Gate for Vision-Language Pipelines` 的 source-specific 反例/局限边界；若运行条件离开 `V Experiments; V-A Evaluation protocol; VI Deployment Patterns` 的验证域，`INFER-REQUEST-LIFECYCLE` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25838:start -->
Claim boundary：仅 `arXiv:2606.25838v1`；未证明边界定位 `https://arxiv.org/html/2606.25838v1 — §VII-C Limitations and future work`。
<!-- claim:SF-2026-ARXIV-2606-25838:end -->
<!-- review:SF-2026-ARXIV-2606-25838:end -->

<!-- review:SF-2026-ARXIV-2606-25863:start -->
### 2606.25863 — Automated Detection of Configuration-Specific Security Vulnerabilities via Patch Analysis

**问题与旧路径。** We study how security patches in highly configurable C/C++ systems map onto the space of compile-time variants.

**机制、状态与控制流。** `PDF §3 Research Design; §3.3 PatchLens static analysis and build-system resolution` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `PDF threats to validity; compile-time C/C++ and project-specific build-resolver boundary` 是 `Automated Detection of Configuration-Specific Security Vulnerabilities via Patch Analysis` 的 source-specific 反例/局限边界；若运行条件离开 `PDF §4 Results; 1,192 Linux, 289 FFmpeg, 100 PHP patches` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25863:start -->
Claim boundary：仅 `arXiv:2606.25863v1`；未证明边界定位 `https://arxiv.org/pdf/2606.25863v1 — §PDF threats to validity; compile-time C/C++ and project-specific build-resolver boundary`。
<!-- claim:SF-2026-ARXIV-2606-25863:end -->
<!-- review:SF-2026-ARXIV-2606-25863:end -->

<!-- review:SF-2026-ARXIV-2606-25871:start -->
### 2606.25871 — AutoRelAnnotator: Calibrated Model Cascades for Cost-Efficient Relevance Evaluation in Sponsored Search

**问题与旧路径。** How can we generate high-quality relevance annotations at scale without the cost and delays of human labeling?

**机制、状态与控制流。** `3 Our Approach; 3.1 System Architecture; 3.3 Per-Class Isotonic Calibration; 3.4 Cascade Decision Logic` 所定义的源特定机制用于把数据选择、校准或验证结果变成训练前可审计的数据控制状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `5 Production Deployment and Discussion; sponsored-search relevance boundary` 是 `AutoRelAnnotator: Calibrated Model Cascades for Cost-Efficient Relevance Evaluation in Sponsored Search` 的 source-specific 反例/局限边界；若运行条件离开 `4 Experiments and Evaluation; 4.2 Dataset and Setup; 4.5 Cascade Performance` 的验证域，`TRAIN-DATA` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25871:start -->
Claim boundary：仅 `arXiv:2606.25871v1`；未证明边界定位 `https://arxiv.org/html/2606.25871v1 — §5 Production Deployment and Discussion; sponsored-search relevance boundary`。
<!-- claim:SF-2026-ARXIV-2606-25871:end -->
<!-- review:SF-2026-ARXIV-2606-25871:end -->

<!-- review:SF-2026-ARXIV-2606-25987:start -->
### 2606.25987 — Weave of Formal Thought

**问题与旧路径。** Large language models (LLMs) attain remarkable surface fluency on code, yet they neither formally guarantee the syntactic validity of their output nor leverage the hierarchical structure defining the target language.

**机制、状态与控制流。** `3 Formal Engine; 3.2 Architecture; 4 Weave of Formal Thought` 所定义的源特定机制用于把工具候选、模拟执行和恢复路径置于真实副作用 commit 之前；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `6 Next Steps and Research Vision; technical-report preliminary-results boundary` 是 `Weave of Formal Thought` 的 source-specific 反例/局限边界；若运行条件离开 `5 WoFT Improves Surface Modeling; 5.1 Experimental setup` 的验证域，`AGENT-TOOL-CALLING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25987:start -->
Claim boundary：仅 `arXiv:2606.25987v1`；未证明边界定位 `https://arxiv.org/html/2606.25987v1 — §6 Next Steps and Research Vision; technical-report preliminary-results boundary`。
<!-- claim:SF-2026-ARXIV-2606-25987:end -->
<!-- review:SF-2026-ARXIV-2606-25987:end -->

<!-- review:SF-2026-ARXIV-2606-25996:start -->
### 2606.25996 — Autodata: An agentic data scientist to create high quality synthetic data

**问题与旧路径。** We introduce Autodata, a general method that enables AI agents to act as data scientists who build high quality training and evaluation data.

**机制、状态与控制流。** `2 Autodata; 2.1 Agentic Self-Instruct; 4 Meta Optimization of the Data Scientist` 所定义的源特定机制用于把数据选择、校准或验证结果变成训练前可审计的数据控制状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `6 Conclusion and Discussion; Hacking & limitations; A Token Efficiency and Truncation` 是 `Autodata: An agentic data scientist to create high quality synthetic data` 的 source-specific 反例/局限边界；若运行条件离开 `3 Experiments; CS, legal, and scientific reasoning tasks` 的验证域，`TRAIN-DATA` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25996:start -->
Claim boundary：仅 `arXiv:2606.25996v1`；未证明边界定位 `https://arxiv.org/html/2606.25996v1 — §6 Conclusion and Discussion; Hacking & limitations; A Token Efficiency and Truncation`。
<!-- claim:SF-2026-ARXIV-2606-25996:end -->
<!-- review:SF-2026-ARXIV-2606-25996:end -->

<!-- review:SF-2026-ARXIV-2606-26021:start -->
### 2606.26021 — Privacy Vulnerabilities of Attention Layers in Tabular Foundation Models and Protection of High-Risk Queries

**问题与旧路径。** Tabular foundation models are commonly assumed to present limited privacy concerns as they are often pre-trained on large collections of synthetic data.

**机制、状态与控制流。** `V Attention-based MIA; VI Inference-Time Hardening Against MIAs` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `VIII-C Limitations and opportunities; I Context size` 是 `Privacy Vulnerabilities of Attention Layers in Tabular Foundation Models and Protection of High-Risk Queries` 的 source-specific 反例/局限边界；若运行条件离开 `IV Tabular FMs Under Standard MIAs; V-B and VI-B Experimental Results` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26021:start -->
Claim boundary：仅 `arXiv:2606.26021v1`；未证明边界定位 `https://arxiv.org/html/2606.26021v1 — §VIII-C Limitations and opportunities; I Context size`。
<!-- claim:SF-2026-ARXIV-2606-26021:end -->
<!-- review:SF-2026-ARXIV-2606-26021:end -->

<!-- review:SF-2026-ARXIV-2606-26027:start -->
### 2606.26027 — Why Multi-Step Tool-Use Reinforcement Learning Collapses and How Supervisory Signals Fix It

**问题与旧路径。** Tool use enables large language models (LLMs) to perform complex tasks, and recent agentic reinforcement learning (RL) methods show promise for enhancing model capabilities.

**机制、状态与控制流。** `4 Method; 4.2 catastrophic collapse; 4.4 supervisory fixes` 所定义的源特定机制用于把崩溃信号与监督修复绑定到策略更新门控；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `B Training Details; C Qwen3 Training; E Training Dynamic` 是 `Why Multi-Step Tool-Use Reinforcement Learning Collapses and How Supervisory Signals Fix It` 的 source-specific 反例/局限边界；若运行条件离开 `5 Experiments; 5.1 Dataset and Models; D Detailed Evaluation` 的验证域，`TRAIN-GRPO` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26027:start -->
Claim boundary：仅 `arXiv:2606.26027v1`；未证明边界定位 `https://arxiv.org/html/2606.26027v1 — §B Training Details; C Qwen3 Training; E Training Dynamic`。
<!-- claim:SF-2026-ARXIV-2606-26027:end -->
<!-- review:SF-2026-ARXIV-2606-26027:end -->

<!-- review:SF-2026-ARXIV-2606-26028:start -->
### 2606.26028 — Can Trustless Agents Be Trusted? An Empirical Study of the ERC-8004 Decentralized AI Agent Ecosystem

**问题与旧路径。** As autonomous AI agents increasingly transact across organizational boundaries, a fundamental trust challenge emerges: how can an agent assess whether an unknown counterpart is trustworthy?

**机制、状态与控制流。** `3 System Model: ERC-8004 Protocol; 7 Reputation Market Security` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `9 Limitations and Future Work; C x402 attribution challenges` 是 `Can Trustless Agents Be Trusted? An Empirical Study of the ERC-8004 Decentralized AI Agent Ecosystem` 的 source-specific 反例/局限边界；若运行条件离开 `4 Dataset; 5 Agent Identity and Adoption; 6 Reputation Market` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26028:start -->
Claim boundary：仅 `arXiv:2606.26028v1`；未证明边界定位 `https://arxiv.org/html/2606.26028v1 — §9 Limitations and Future Work; C x402 attribution challenges`。
<!-- claim:SF-2026-ARXIV-2606-26028:end -->
<!-- review:SF-2026-ARXIV-2606-26028:end -->

<!-- review:SF-2026-ARXIV-2606-26057:start -->
### 2606.26057 — The Unfireable Safety Kernel: Execution-Time AI Alignment for AI Agents and Other Escapable AI Systems

**问题与旧路径。** AI agents are granted access to tools, APIs, and other infrastructure, making them active principals in those systems.

**机制、状态与控制流。** `2 Threat Model; 3 Requirements; 4 Design; 5 Implementation` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `8.3 Limitations and Future Work; Artifact and Reproducibility` 是 `The Unfireable Safety Kernel: Execution-Time AI Alignment for AI Agents and Other Escapable AI Systems` 的 source-specific 反例/局限边界；若运行条件离开 `6 Evaluation; 6.4 Machine-Checked Fail-Closed Invariant; 6.5 Live containment` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26057:start -->
Claim boundary：仅 `arXiv:2606.26057v1`；未证明边界定位 `https://arxiv.org/html/2606.26057v1 — §8.3 Limitations and Future Work; Artifact and Reproducibility`。
<!-- claim:SF-2026-ARXIV-2606-26057:end -->
<!-- review:SF-2026-ARXIV-2606-26057:end -->

<!-- review:SF-2026-ARXIV-2606-26071:start -->
### 2606.26071 — Model Forensics: Investigating Whether Concerning Behavior Reflects Misalignment

**问题与旧路径。** A central goal of safety research is determining whether a model is misaligned.

**机制、状态与控制流。** `4 Protocol and Methods; 5 Environments; 7 Methodological Insights` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `10 Limitations and Future Work; negative-results and confounding boundary` 是 `Model Forensics: Investigating Whether Concerning Behavior Reflects Misalignment` 的 source-specific 反例/局限边界；若运行条件离开 `6 Case Studies; 8 Recommendations` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26071:start -->
Claim boundary：仅 `arXiv:2606.26071v1`；未证明边界定位 `https://arxiv.org/html/2606.26071v1 — §10 Limitations and Future Work; negative-results and confounding boundary`。
<!-- claim:SF-2026-ARXIV-2606-26071:end -->
<!-- review:SF-2026-ARXIV-2606-26071:end -->

<!-- review:SF-2026-ARXIV-2606-26185:start -->
### 2606.26185 — Necessary but Not Sufficient: Temperature Control and Reproducibility in LLM-as-Judge Safety Evaluations

**问题与旧路径。** LLM-as-judge ("grader") components are now standard in evaluation harnesses, including safety evaluations where a pass/fail verdict may gate downstream deployment decisions.

**机制、状态与控制流。** `Temperature-control and reproducibility protocol for LLM-as-judge safety evaluation` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Temperature control is necessary but not sufficient; prompt/model/vendor drift remains` 是 `Necessary but Not Sufficient: Temperature Control and Reproducibility in LLM-as-Judge Safety Evaluations` 的 source-specific 反例/局限边界；若运行条件离开 `Cross-temperature, repeat-run and judge-agreement evaluation` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26185:start -->
Claim boundary：仅 `arXiv:2606.26185v1`；未证明边界定位 `https://arxiv.org/html/2606.26185v1 — §Temperature control is necessary but not sufficient; prompt/model/vendor drift remains`。
<!-- claim:SF-2026-ARXIV-2606-26185:end -->
<!-- review:SF-2026-ARXIV-2606-26185:end -->

<!-- review:SF-2026-ARXIV-2606-26211:start -->
### 2606.26211 — Data Facts: A Metadata Schema for Structured Data Exchange in the NANDini Multi-Agent Ecosystem

**问题与旧路径。** NANDini (Networked Agents Natural Distillation of Interconnected Nodal Intelligence) envisions an automated ecosystem where intelligent agents independently create, process, and exchange data to drive decisions at scale.

**机制、状态与控制流。** `Data Facts metadata schema; provenance, semantics, constraints and exchange contract` 所定义的源特定机制用于以带 provenance、语义和约束的 Data Facts 作为跨 Agent 交换契约；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Single ecosystem prototype; no proof of cross-vendor enforcement or semantic completeness` 是 `Data Facts: A Metadata Schema for Structured Data Exchange in the NANDini Multi-Agent Ecosystem` 的 source-specific 反例/局限边界；若运行条件离开 `NANDini multi-agent exchange examples and schema coverage` 的验证域，`AGENT-MCP` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26211:start -->
Claim boundary：仅 `arXiv:2606.26211v1`；未证明边界定位 `https://arxiv.org/html/2606.26211v1 — §Single ecosystem prototype; no proof of cross-vendor enforcement or semantic completeness`。
<!-- claim:SF-2026-ARXIV-2606-26211:end -->
<!-- review:SF-2026-ARXIV-2606-26211:end -->

<!-- review:SF-2026-ARXIV-2606-26257:start -->
### 2606.26257 — Dataset Usage Inference without Shadow Models or Held-out Data

**问题与旧路径。** How much of my data was used to train a machine learning model?

**机制、状态与控制流。** `Dataset Usage Inference formulation without shadow models or held-out data` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Requires the paper's observable score/query regime; not per-record legal attribution` 是 `Dataset Usage Inference without Shadow Models or Held-out Data` 的 source-specific 反例/局限边界；若运行条件离开 `Exact-v1 membership/dataset inference experiments and ablations` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26257:start -->
Claim boundary：仅 `arXiv:2606.26257v1`；未证明边界定位 `https://arxiv.org/html/2606.26257v1 — §Requires the paper's observable score/query regime; not per-record legal attribution`。
<!-- claim:SF-2026-ARXIV-2606-26257:end -->
<!-- review:SF-2026-ARXIV-2606-26257:end -->

<!-- review:SF-2026-ARXIV-2606-26298:start -->
### 2606.26298 — Governing Actions, Not Agents: Institutional Attestation as a Governance Model for Autonomous AI Systems

**问题与旧路径。** Autonomous AI agents may begin to perform consequential, irreversible actions such as clinical prescribing and production software deployment.

**机制、状态与控制流。** `Governing Actions, Not Agents; Institutional Attestation model` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Institutional model is a governance proposal, not a deployed enforcement benchmark` 是 `Governing Actions, Not Agents: Institutional Attestation as a Governance Model for Autonomous AI Systems` 的 source-specific 反例/局限边界；若运行条件离开 `Action-level attestation scenarios and governance analysis` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26298:start -->
Claim boundary：仅 `arXiv:2606.26298v1`；未证明边界定位 `https://arxiv.org/html/2606.26298v1 — §Institutional model is a governance proposal, not a deployed enforcement benchmark`。
<!-- claim:SF-2026-ARXIV-2606-26298:end -->
<!-- review:SF-2026-ARXIV-2606-26298:end -->

<!-- review:SF-2026-ARXIV-2606-26300:start -->
### 2606.26300 — The Verification Horizon: No Silver Bullet for Coding Agent Rewards

**问题与旧路径。** A classical intuition holds that verifying a solution is easier than producing one.

**机制、状态与控制流。** `Verification Horizon formulation for coding-agent rewards` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `No universal reward verifier; longer horizons and hidden environment state remain` 是 `The Verification Horizon: No Silver Bullet for Coding Agent Rewards` 的 source-specific 反例/局限边界；若运行条件离开 `Reward-verification experiments across coding horizons` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26300:start -->
Claim boundary：仅 `arXiv:2606.26300v1`；未证明边界定位 `https://arxiv.org/html/2606.26300v1 — §No universal reward verifier; longer horizons and hidden environment state remain`。
<!-- claim:SF-2026-ARXIV-2606-26300:end -->
<!-- review:SF-2026-ARXIV-2606-26300:end -->

<!-- review:SF-2026-ARXIV-2606-26341:start -->
### 2606.26341 — Scaling Nonlinear Optimization: Many Problems One GPU

**问题与旧路径。** Many robotics problems, including trajectory optimization, inverse kinematics, and contact-rich motion planning, reduce to nonlinear programs (NLPs).

**机制、状态与控制流。** `Many Problems One GPU batching and nonlinear-optimization execution design` 所定义的源特定机制用于把异构问题批处理与 GPU 执行配置作为调度状态，而非模型内部细节；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Only disclosed nonlinear solvers/problem shapes; no cluster-level scheduling or isolation proof` 是 `Scaling Nonlinear Optimization: Many Problems One GPU` 的 source-specific 反例/局限边界；若运行条件离开 `GPU scaling experiments across problem families` 的验证域，`PLATFORM-GPU-SCHEDULER` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26341:start -->
Claim boundary：仅 `arXiv:2606.26341v1`；未证明边界定位 `https://arxiv.org/html/2606.26341v1 — §Only disclosed nonlinear solvers/problem shapes; no cluster-level scheduling or isolation proof`。
<!-- claim:SF-2026-ARXIV-2606-26341:end -->
<!-- review:SF-2026-ARXIV-2606-26341:end -->

<!-- review:SF-2026-ARXIV-2606-26344:start -->
### 2606.26344 — Axon: A Synthesizing Superoptimizer for Tensor Programs

**问题与旧路径。** Writing high performance kernels for AI accelerators requires deep expertise in tiling, instruction selection, data layout, and operator fusion placing a significant burden on programmers.

**机制、状态与控制流。** `Axon synthesizing superoptimizer; tensor-program search and verification` 所定义的源特定机制用于以可验证搜索或 profiling 反馈驱动 kernel 选择，同时保留确定性正确性路径；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Covered tensor operators/hardware only; verifier does not prove arbitrary numerical equivalence` 是 `Axon: A Synthesizing Superoptimizer for Tensor Programs` 的 source-specific 反例/局限边界；若运行条件离开 `Kernel synthesis evaluation and generated-program performance` 的验证域，`INFER-TENSORRT-LLM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26344:start -->
Claim boundary：仅 `arXiv:2606.26344v1`；未证明边界定位 `https://arxiv.org/html/2606.26344v1 — §Covered tensor operators/hardware only; verifier does not prove arbitrary numerical equivalence`。
<!-- claim:SF-2026-ARXIV-2606-26344:end -->
<!-- review:SF-2026-ARXIV-2606-26344:end -->

<!-- review:SF-2026-ARXIV-2606-26356:start -->
### 2606.26356 — Instruction Bleed: Cross-Module Interference in Prompt-Composed Agentic Systems

**问题与旧路径。** Practitioners of prompt-composed agentic systems report a recurring failure mode: editing one prompt module silently shifts the behavior of others despite no shared variable or executable dependency.

**机制、状态与控制流。** `Instruction Bleed formulation; prompt-composed module interference` 所定义的源特定机制用于把模块间指令干扰作为可测试的组合边界，而非默认隔离；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Prompt/module families tested do not establish universal isolation or adversarial robustness` 是 `Instruction Bleed: Cross-Module Interference in Prompt-Composed Agentic Systems` 的 source-specific 反例/局限边界；若运行条件离开 `Cross-module interference experiments and mitigations` 的验证域，`AGENT-PROMPT` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26356:start -->
Claim boundary：仅 `arXiv:2606.26356v1`；未证明边界定位 `https://arxiv.org/html/2606.26356v1 — §Prompt/module families tested do not establish universal isolation or adversarial robustness`。
<!-- claim:SF-2026-ARXIV-2606-26356:end -->
<!-- review:SF-2026-ARXIV-2606-26356:end -->

<!-- review:SF-2026-ARXIV-2606-26377:start -->
### 2606.26377 — Verifying Intent and Harm: A Unified Defense Against LLM-Generated Threats

**问题与旧路径。** Large language models (LLMs) are increasingly deployed in interactive applications, yet they remain vulnerable to adversarial interactions that induce harmful, deceptive, or policy-violating outputs.

**机制、状态与控制流。** `Unified intent-and-harm verification defense` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Evaluated threat families and judges only; intent inference is not proof of harmless execution` 是 `Verifying Intent and Harm: A Unified Defense Against LLM-Generated Threats` 的 source-specific 反例/局限边界；若运行条件离开 `Threat-generation and defense evaluation` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26377:start -->
Claim boundary：仅 `arXiv:2606.26377v1`；未证明边界定位 `https://arxiv.org/html/2606.26377v1 — §Evaluated threat families and judges only; intent inference is not proof of harmless execution`。
<!-- claim:SF-2026-ARXIV-2606-26377:end -->
<!-- review:SF-2026-ARXIV-2606-26377:end -->

<!-- review:SF-2026-ARXIV-2606-26383:start -->
### 2606.26383 — SOLAR: AI-Powered Speed-of-Light Performance Analysis

**问题与旧路径。** How fast could a deep-learning model run on target hardware, and how far is today's implementation from that limit?

**机制、状态与控制流。** `SOLAR speed-of-light performance model; bottleneck decomposition and bound calculation` 所定义的源特定机制用于以校准后的硬件与 workload 参数分解性能上界和瓶颈；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Analytical bounds depend on calibrated hardware/workload parameters and omit undisclosed runtime effects` 是 `SOLAR: AI-Powered Speed-of-Light Performance Analysis` 的 source-specific 反例/局限边界；若运行条件离开 `Predicted-vs-observed latency and throughput analysis` 的验证域，`PLATFORM-MONITORING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26383:start -->
Claim boundary：仅 `arXiv:2606.26383v1`；未证明边界定位 `https://arxiv.org/html/2606.26383v1 — §Analytical bounds depend on calibrated hardware/workload parameters and omit undisclosed runtime effects`。
<!-- claim:SF-2026-ARXIV-2606-26383:end -->
<!-- review:SF-2026-ARXIV-2606-26383:end -->

<!-- review:SF-2026-ARXIV-2606-26429:start -->
### 2606.26429 — DualEval: Joint Model-Item Calibration for Unified LLM Evaluation

**问题与旧路径。** Current LLM evaluation relies on two complementary but often disconnected signals: static benchmarks with objective correctness labels and arena-style preference data that better reflect open-ended user interactions.

**机制、状态与控制流。** `DualEval joint model-item calibration` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Joint calibration assumes the evaluated item/model pool; new distributions require refitting` 是 `DualEval: Joint Model-Item Calibration for Unified LLM Evaluation` 的 source-specific 反例/局限边界；若运行条件离开 `Unified LLM evaluation experiments and calibration analysis` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26429:start -->
Claim boundary：仅 `arXiv:2606.26429v1`；未证明边界定位 `https://arxiv.org/html/2606.26429v1 — §Joint calibration assumes the evaluated item/model pool; new distributions require refitting`。
<!-- claim:SF-2026-ARXIV-2606-26429:end -->
<!-- review:SF-2026-ARXIV-2606-26429:end -->

<!-- review:SF-2026-ARXIV-2606-26439:start -->
### 2606.26439 — TileMaxSim: IO-Aware GPU MaxSim Scoring with Dimension Tiling and Fused Product Quantization

**问题与旧路径。** Multi-vector retrieval models such as ColBERT achieve state-of-the-art accuracy through fine-grained token-level MaxSim scoring, yet existing GPU implementations leave most hardware performance unused.

**机制、状态与控制流。** `TileMaxSim IO-aware GPU MaxSim scoring; dimension tiling and fused product quantization` 所定义的源特定机制用于把检索索引、量化、GPU scorer 与更新一致性拆成显式数据面状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Evaluated MaxSim layouts and GPUs only; index update and distributed consistency are not proved` 是 `TileMaxSim: IO-Aware GPU MaxSim Scoring with Dimension Tiling and Fused Product Quantization` 的 source-specific 反例/局限边界；若运行条件离开 `GPU retrieval throughput, latency and quality evaluation` 的验证域，`AGENT-RAG` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26439:start -->
Claim boundary：仅 `arXiv:2606.26439v1`；未证明边界定位 `https://arxiv.org/html/2606.26439v1 — §Evaluated MaxSim layouts and GPUs only; index update and distributed consistency are not proved`。
<!-- claim:SF-2026-ARXIV-2606-26439:end -->
<!-- review:SF-2026-ARXIV-2606-26439:end -->

<!-- review:SF-2026-ARXIV-2606-26441:start -->
### 2606.26441 — GPUSparse: GPU-Accelerated Learned Sparse Retrieval with Parallel Inverted Indices

**问题与旧路径。** Learned sparse retrieval models such as SPLADE achieve retrieval quality competitive with dense models while preserving the interpretability and exact-match advantages of sparse representations.

**机制、状态与控制流。** `GPUSparse learned sparse retrieval with parallel inverted indices` 所定义的源特定机制用于把检索索引、量化、GPU scorer 与更新一致性拆成显式数据面状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Static benchmark indexes do not prove high-churn update cost, multi-tenant isolation or cross-node scaling` 是 `GPUSparse: GPU-Accelerated Learned Sparse Retrieval with Parallel Inverted Indices` 的 source-specific 反例/局限边界；若运行条件离开 `Retrieval quality, latency and GPU scaling experiments` 的验证域，`AGENT-RAG` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26441:start -->
Claim boundary：仅 `arXiv:2606.26441v1`；未证明边界定位 `https://arxiv.org/html/2606.26441v1 — §Static benchmark indexes do not prove high-churn update cost, multi-tenant isolation or cross-node scaling`。
<!-- claim:SF-2026-ARXIV-2606-26441:end -->
<!-- review:SF-2026-ARXIV-2606-26441:end -->

<!-- review:SF-2026-ARXIV-2606-26442:start -->
### 2606.26442 — AXLE: A Cloud Infrastructure for Lean 4 Theorem Proving Utilities

**问题与旧路径。** We present AXLE (Axiom Lean Engine), a cloud service for Lean 4 proof manipulation, extraction, and verification.

**机制、状态与控制流。** `AXLE cloud infrastructure for Lean 4 utilities; remote execution and artifact handling` 所定义的源特定机制用于把执行 harness、远端 utility 与 artifact handoff 变成可观测工作流状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Cloud utility success does not prove generated theorem correctness beyond Lean checking or side-effect safety` 是 `AXLE: A Cloud Infrastructure for Lean 4 Theorem Proving Utilities` 的 source-specific 反例/局限边界；若运行条件离开 `Utility execution, throughput and theorem-proving workflow evaluation` 的验证域，`AGENT-WORKFLOW` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26442:start -->
Claim boundary：仅 `arXiv:2606.26442v1`；未证明边界定位 `https://arxiv.org/html/2606.26442v1 — §Cloud utility success does not prove generated theorem correctness beyond Lean checking or side-effect safety`。
<!-- claim:SF-2026-ARXIV-2606-26442:end -->
<!-- review:SF-2026-ARXIV-2606-26442:end -->

<!-- review:SF-2026-ARXIV-2606-26449:start -->
### 2606.26449 — ProvenAI: Provenance-Native Traces of Evidence in Generated Answers

**问题与旧路径。** Retrieval-augmented systems routinely present citations alongside generated answers, yet a citation does not confirm that the corresponding source meaningfully shaped the output.

**机制、状态与控制流。** `ProvenAI provenance-native trace schema and evidence links` 所定义的源特定机制用于让证据生产者写入 provenance 链，消费者据此追踪而不把来源等同于真值；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Trace completeness depends on instrumented producers; provenance does not imply source truth` 是 `ProvenAI: Provenance-Native Traces of Evidence in Generated Answers` 的 source-specific 反例/局限边界；若运行条件离开 `Generated-answer trace/evidence evaluation` 的验证域，`PLATFORM-TRACE` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26449:start -->
Claim boundary：仅 `arXiv:2606.26449v1`；未证明边界定位 `https://arxiv.org/html/2606.26449v1 — §Trace completeness depends on instrumented producers; provenance does not imply source truth`。
<!-- claim:SF-2026-ARXIV-2606-26449:end -->
<!-- review:SF-2026-ARXIV-2606-26449:end -->

<!-- review:SF-2026-ARXIV-2606-26453:start -->
### 2606.26453 — Optimizing CUDA like a Human: Micro-Profiling Tools as Expert Surrogates for LLM-Based GPU Kernel Optimization

**问题与旧路径。** We present KernelPro, a closed-loop multi-agent system that automatically generates, profiles, and iteratively optimizes GPU kernel code by integrating large language model (LLM) code generation with hardware profiler feedback and pluggable bottleneck detection tools.

**机制、状态与控制流。** `Micro-profiling tools as expert surrogates for LLM CUDA optimization` 所定义的源特定机制用于以可验证搜索或 profiling 反馈驱动 kernel 选择，同时保留确定性正确性路径；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Evaluated CUDA tasks and toolchain only; profile-guided generation needs deterministic correctness fallback` 是 `Optimizing CUDA like a Human: Micro-Profiling Tools as Expert Surrogates for LLM-Based GPU Kernel Optimization` 的 source-specific 反例/局限边界；若运行条件离开 `Generated-kernel correctness, profiling and speed evaluation` 的验证域，`INFER-TENSORRT-LLM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26453:start -->
Claim boundary：仅 `arXiv:2606.26453v1`；未证明边界定位 `https://arxiv.org/html/2606.26453v1 — §Evaluated CUDA tasks and toolchain only; profile-guided generation needs deterministic correctness fallback`。
<!-- claim:SF-2026-ARXIV-2606-26453:end -->
<!-- review:SF-2026-ARXIV-2606-26453:end -->

<!-- review:SF-2026-ARXIV-2606-26456:start -->
### 2606.26456 — Towards Safety-Aware Mutation Testing for Autonomous Driving Systems

**问题与旧路径。** Simulation-based testing is essential for ensuring the safety of Autonomous Driving Systems (ADS), yet the community lacks a systematic criterion for determining when we can safely stop additional test scenario generation.

**机制、状态与控制流。** `Safety-Aware Mutation Testing proposal and interaction-aware mutant model` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Vision paper: no completed empirical stop-rule validation; ADS component/fault model is provisional` 是 `Towards Safety-Aware Mutation Testing for Autonomous Driving Systems` 的 source-specific 反例/局限边界；若运行条件离开 `Simulation-based ADS testing protocol and proposed adequacy criterion` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26456:start -->
Claim boundary：仅 `arXiv:2606.26456v1`；未证明边界定位 `https://arxiv.org/html/2606.26456v1 — §Vision paper: no completed empirical stop-rule validation; ADS component/fault model is provisional`。
<!-- claim:SF-2026-ARXIV-2606-26456:end -->
<!-- review:SF-2026-ARXIV-2606-26456:end -->

<!-- review:SF-2026-ARXIV-2606-26463:start -->
### 2606.26463 — Finding the Time to Think: Learning Planning Budgets in Real-Time RL

**问题与旧路径。** Deliberating takes time.

**机制、状态与控制流。** `Variable-delay real-time RL; lightweight gate selects state-dependent planning budget` 所定义的源特定机制用于以候选扩展或实时 gate 分配规划预算，并在超时或低置信度时回退；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Game planners and timing model do not prove benefit under production tool latency or safety deadlines` 是 `Finding the Time to Think: Learning Planning Budgets in Real-Time RL` 的 source-specific 反例/局限边界；若运行条件离开 `Pac-Man, Tetris, Snake, Speed Hex and Speed Go evaluation` 的验证域，`AGENT-PLANNING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26463:start -->
Claim boundary：仅 `arXiv:2606.26463v1`；未证明边界定位 `https://arxiv.org/html/2606.26463v1 — §Game planners and timing model do not prove benefit under production tool latency or safety deadlines`。
<!-- claim:SF-2026-ARXIV-2606-26463:end -->
<!-- review:SF-2026-ARXIV-2606-26463:end -->

<!-- review:SF-2026-ARXIV-2606-26472:start -->
### 2606.26472 — Epiphany-Aware KV Cache Eviction Without the Attention Matrix

**问题与旧路径。** As reasoning models emit chains of thought tens of thousands of tokens long, KV cache increasingly becomes a deployment bottleneck.

**机制、状态与控制流。** `Epiphany score from forward-pass representation change; attention-matrix-free eviction` 所定义的源特定机制用于以表征变化分数驱动逐 token KV 驱逐，并保留完整 KV 回退；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Model/task transfer and representation-score drift are unproved; quality regression requires full-KV fallback` 是 `Epiphany-Aware KV Cache Eviction Without the Attention Matrix` 的 source-specific 反例/局限边界；若运行条件离开 `Long-reasoning cache/quality evaluation and 16x feasible-context claim` 的验证域，`INFER-KV-CACHE` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26472:start -->
Claim boundary：仅 `arXiv:2606.26472v1`；未证明边界定位 `https://arxiv.org/html/2606.26472v1 — §Model/task transfer and representation-score drift are unproved; quality regression requires full-KV fallback`。
<!-- claim:SF-2026-ARXIV-2606-26472:end -->
<!-- review:SF-2026-ARXIV-2606-26472:end -->

<!-- review:SF-2026-ARXIV-2606-26479:start -->
### 2606.26479 — Adaptive Evaluation of Out-of-Band Defenses Against Prompt Injection in LLM Agents

**问题与旧路径。** Recent work (2024 to 2026) has converged on a strategy for defending tool-using LLM agents against indirect prompt injection: rather than training the model to refuse malicious instructions, enforce security outside the model with a deterministic policy that mediates the agent's actions.

**机制、状态与控制流。** `Out-of-band prompt-injection defenses organized as reference monitors and integrity policies` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Position/evaluation paper; static AgentDojo results do not establish adaptive robustness` 是 `Adaptive Evaluation of Out-of-Band Defenses Against Prompt Injection in LLM Agents` 的 source-specific 反例/局限边界；若运行条件离开 `Adaptive evaluation methodology against policy-aware attackers` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26479:start -->
Claim boundary：仅 `arXiv:2606.26479v1`；未证明边界定位 `https://arxiv.org/html/2606.26479v1 — §Position/evaluation paper; static AgentDojo results do not establish adaptive robustness`。
<!-- claim:SF-2026-ARXIV-2606-26479:end -->
<!-- review:SF-2026-ARXIV-2606-26479:end -->

<!-- review:SF-2026-ARXIV-2606-26488:start -->
### 2606.26488 — What Survives When You Compress a Recursive Reasoner for the Edge?

**问题与旧路径。** Recursive reasoning models can solve complex structured tasks with only a few million parameters by repeatedly updating a latent state.

**机制、状态与控制流。** `Compression of recursive reasoners across precision, pruning, distillation and attention variants` 所定义的源特定机制用于把稀疏、量化或压缩决策绑定到显存预算和质量回退；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Edge recursive models only; token-level preservation does not imply global-reasoning preservation` 是 `What Survives When You Compress a Recursive Reasoner for the Edge?` 的 source-specific 反例/局限边界；若运行条件离开 `Three tasks and two recursive architectures; local vs puzzle-exact accuracy` 的验证域，`INFER-GPU-MEMORY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26488:start -->
Claim boundary：仅 `arXiv:2606.26488v1`；未证明边界定位 `https://arxiv.org/html/2606.26488v1 — §Edge recursive models only; token-level preservation does not imply global-reasoning preservation`。
<!-- claim:SF-2026-ARXIV-2606-26488:end -->
<!-- review:SF-2026-ARXIV-2606-26488:end -->

<!-- review:SF-2026-ARXIV-2606-26492:start -->
### 2606.26492 — Evaluation-Strategy Gap in Fault Diagnosis of Deep Learning Programs

**问题与旧路径。** Deep Learning (DL) programs can fail during training for many reasons, and diagnosing the cause is a costly and time-consuming maintenance task.

**机制、状态与控制流。** `Within-program versus leave-program-out diagnostic design` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Fault-injected programs and studied diagnosers do not prove production root-cause validity` 是 `Evaluation-Strategy Gap in Fault Diagnosis of Deep Learning Programs` 的 source-specific 反例/局限边界；若运行条件离开 `DynFault: 5,542 traces from 38 DL programs; balanced-accuracy gap analysis` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26492:start -->
Claim boundary：仅 `arXiv:2606.26492v1`；未证明边界定位 `https://arxiv.org/html/2606.26492v1 — §Fault-injected programs and studied diagnosers do not prove production root-cause validity`。
<!-- claim:SF-2026-ARXIV-2606-26492:end -->
<!-- review:SF-2026-ARXIV-2606-26492:end -->

## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-25274 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-25285 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-25296 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-25342 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-25349 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-25353 | Not Disclosed | Not Disclosed | GB-scale last-level-cache server CPUs | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | end-to-end performance; analytical-model validation; context-length/batch sensitivity |
| SF-2026-ARXIV-2606-25366 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-25371 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-25388 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-25410 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-25426 | Not Disclosed | Not Disclosed | Apple M1 AMX | FP32 bit-exact | 128-token prefill | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | 12 LLM prefill GEMMs and llama.cpp full-forward tokens/s |
| SF-2026-ARXIV-2606-25447 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-25449 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-25453 | Not Disclosed | Not Disclosed | NVIDIA Hopper and Blackwell GPUs | INT8 Tensor Core emulation of higher precision | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | kernel efficiency, end-to-end throughput, precision-memory trade-off |
| SF-2026-ARXIV-2606-25467 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-25487 | 596 human-labeled HarmBench completions; 30 confident true positives for white-box GCG | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | precision, recall, wrapper flip rate and white-box attack success |
| SF-2026-ARXIV-2606-25514 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-25519 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-25532 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-25548 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-25575 | 44 participants; five bimanual tasks | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | completion time, task success and 7-point acceptance ratings |
| SF-2026-ARXIV-2606-25592 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-25605 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-25608 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-25622 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-25656 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-25658 | Not Disclosed | LLaVA-OneVision and Qwen2.5-VL | Not Disclosed | Not Disclosed | hour-long streaming video; 12k visual-token memory budget | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | streaming/offline accuracy, compression ratio and storage |
| SF-2026-ARXIV-2606-25674 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-25700 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-25705 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-25721 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-25759 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-25760 | 27 UQ methods across VLMs and GUI-grounding datasets | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | AUROC, PRR, graded severity, calibration and conformal click disks |
| SF-2026-ARXIV-2606-25782 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-25797 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-25819 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-25838 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-25863 | 1,192 Linux kernel, 289 FFmpeg and 100 PHP patches | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | VIC extraction coverage, manual precision, formula size and CVE-text recall |
| SF-2026-ARXIV-2606-25871 | six production offline use cases; 150M+ annotations | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | accuracy, calibration gain and cascade compute cost |
| SF-2026-ARXIV-2606-25987 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-25996 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-26021 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-26027 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-26028 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-26057 | 1,000 migration fixtures; 17 adversarial classes; 80+ robustness tests | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | byte equivalence, reject equivalence, latency and machine-checked fail-closed invariant |
| SF-2026-ARXIV-2606-26071 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-26185 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-26211 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-26257 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-26298 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-26300 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-26341 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-26344 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-26356 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-26377 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-26383 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-26429 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-26439 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-26441 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-26442 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-26449 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-26453 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-26456 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-26463 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-26472 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-26479 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-26488 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-26492 | 5,542 fault-injected training traces from 38 DL programs | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | within-program versus leave-program-out balanced accuracy |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-25274 | score_7_9; potential_books_delta | not_selected | — | — | 未入选长叙事：`7 Limitations` 是 `UC-Search: Risk-Aware Test-Time Search for Delayed Constrained Time-Series Control` 的 source-specific 反例/局限边界；若运行条件离开 `5 Experiments; 5.1 Implemented Evidence; 6 Analysis` 的验证域，`AGENT-PLANNING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。 | analysis-decision:SF-2026-ARXIV-2606-25274 |
| SF-2026-ARXIV-2606-25285 | score_7_9; potential_books_delta | not_selected | — | — | 未入选长叙事：`Limitations and Discussion` 是 `EPTS: Elastic Post-Training Sparsity for Efficient Large Language Model Compression` 的 source-specific 反例/局限边界；若运行条件离开 `4 Experiments; Experimental Setup; Main Results` 的验证域，`INFER-GPU-MEMORY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。 | analysis-decision:SF-2026-ARXIV-2606-25285 |
| SF-2026-ARXIV-2606-25296 | score_7_9; potential_books_delta | not_selected | — | — | 未入选长叙事：`Threats to Validity; Limitations` 是 `SafeGen: LLM-Driven Assertion Generation and Fault Criticality Evaluation for Functional Safety` 的 source-specific 反例/局限边界；若运行条件离开 `Experimental Evaluation; Functional-Safety Case Studies` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。 | analysis-decision:SF-2026-ARXIV-2606-25296 |
| SF-2026-ARXIV-2606-25342 | score_7_9; potential_books_delta | not_selected | — | — | 未入选长叙事：`Discussion; finite-memory and task-family limitations` 是 `Lifelong In-Context Learning with Transformers Requires Parametric Forms of Attention` 的 source-specific 反例/局限边界；若运行条件离开 `Experiments; Lifelong sequence results` 的验证域，`MODEL-LONG-CONTEXT` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。 | analysis-decision:SF-2026-ARXIV-2606-25342 |
| SF-2026-ARXIV-2606-25349 | score_7_9; potential_books_delta | not_selected | — | — | 未入选长叙事：`VIII Conclusion; exact-v1 analytical-evaluation-only note` 是 `General Techniques for Reducing Key-Switching Overhead in Privacy-Preserving Two-Party Transformer Inference` 的 source-specific 反例/局限边界；若运行条件离开 `VII Evaluation` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。 | analysis-decision:SF-2026-ARXIV-2606-25349 |
| SF-2026-ARXIV-2606-25353 | score_7_9; potential_books_delta | selected | DA-20260625-2606-25353 | — | 入选：`3 Architecture; 3.1 Weight-Attention Decoupled Organization; 4 Implementation` 所定义的源特定机制用于把权重、attention 与 cache-blocking 路径拆成可独立放置和优化的前缀计算状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。 | analysis:DA-20260625-2606-25353 |
| SF-2026-ARXIV-2606-25366 | score_7_9; potential_books_delta | not_selected | — | — | 未入选长叙事：`XI-D Limitations` 是 `Reliability-Asymmetric Spacecraft Autonomy: Co-Designing a Capable Learned GNC Stack with a Verified, Adaptation-Aware Runtime Shield` 的 source-specific 反例/局限边界；若运行条件离开 `VIII Robustness; IX Integrated Evaluation` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。 | analysis-decision:SF-2026-ARXIV-2606-25366 |
| SF-2026-ARXIV-2606-25371 | score_7_9; potential_books_delta | not_selected | — | — | 未入选长叙事：`VI-D Limitations` 是 `Conformal Recovery-Deadline Certificates for Runtime Assurance of Adapting Controllers` 的 source-specific 反例/局限边界；若运行条件离开 `V Experiments` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。 | analysis-decision:SF-2026-ARXIV-2606-25371 |
| SF-2026-ARXIV-2606-25388 | score_7_9; potential_books_delta | not_selected | — | — | 未入选长叙事：`VII Discussion and Future Work` 是 `TabClean: Reusable LLM-Synthesized Programs for Tabular Data Cleaning` 的 source-specific 反例/局限边界；若运行条件离开 `V Experimental Evaluation; V-A Experimental Setup` 的验证域，`TRAIN-DATA` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。 | analysis-decision:SF-2026-ARXIV-2606-25388 |
| SF-2026-ARXIV-2606-25410 | score_7_9 | not_selected | — | — | 未入选长叙事：`5 Conclusion; class-forgetting experimental scope` 是 `DFMU: Data-Frugal Machine Unlearning` 的 source-specific 反例/局限边界；若运行条件离开 `4 Experiments; 4.1 Experimental Setup; 4.4 Results` 的验证域，`TRAIN-DATA` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。 | analysis-decision:SF-2026-ARXIV-2606-25410 |
| SF-2026-ARXIV-2606-25426 | score_7_9; potential_books_delta | not_selected | — | — | 未入选长叙事：`6 Conclusion; Limitations` 是 `Above the Inner Loop: Exceeding Accelerate at LLM Prefill GEMM on the M1 AMX` 的 source-specific 反例/局限边界；若运行条件离开 `4 Evaluation; 4.1 Experimental setup; 4.7 End-to-end prefill GEMM measurement` 的验证域，`INFER-PREFILL` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。 | analysis-decision:SF-2026-ARXIV-2606-25426 |
| SF-2026-ARXIV-2606-25447 | score_7_9; potential_books_delta | not_selected | — | — | 未入选长叙事：`B Benchmark Details; C Experimental Details; stated ALFWorld boundary` 是 `The Interplay of Harness Design and Post-Training in LLM Agents` 的 source-specific 反例/局限边界；若运行条件离开 `4 Analysis; 4.1 Evaluation Protocol; 4.4 OOD Robustness` 的验证域，`AGENT-WORKFLOW` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。 | analysis-decision:SF-2026-ARXIV-2606-25447 |
| SF-2026-ARXIV-2606-25449 | score_7_9; potential_books_delta | not_selected | — | — | 未入选长叙事：`7 Limitations` 是 `Reclaim Evaluation: A Lossy Memory Is Worse Than an Empty One` 的 source-specific 反例/局限边界；若运行条件离开 `4 Experimental Setup; 5 Results; 5.7 Boundary of the Fix` 的验证域，`AGENT-MEMORY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。 | analysis-decision:SF-2026-ARXIV-2606-25449 |
| SF-2026-ARXIV-2606-25453 | score_7_9; potential_books_delta | not_selected | — | — | 未入选长叙事：`V-G Limitations` 是 `EmuGEMM: Fused Tensor Core Kernels for Precision Emulation in Matrix Multiplication` 的 source-specific 反例/局限边界；若运行条件离开 `V Evaluation; V-B Experimental Setup; V-F Precision-Throughput-Memory Trade-off` 的验证域，`INFER-TENSORRT-LLM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。 | analysis-decision:SF-2026-ARXIV-2606-25453 |
| SF-2026-ARXIV-2606-25467 | score_7_9; potential_books_delta | not_selected | — | — | 未入选长叙事：`D-B Runtime Boundary and Fallback; G Implementation Scope Clarifications` 是 `RQ-SAFE: Coupled Request-Resource Scheduling for Online Edge SFC-DAGs` 的 source-specific 反例/局限边界；若运行条件离开 `V Experimental Evaluation; V-A Experimental Setup` 的验证域，`INFER-SCHEDULING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。 | analysis-decision:SF-2026-ARXIV-2606-25467 |
| SF-2026-ARXIV-2606-25487 | score_7_9; potential_books_delta | not_selected | — | — | 未入选长叙事：`6 Limitations` 是 `How Reliable Is Your Jailbreak Judge? Calibration and Adversarial Robustness of Automated ASR Scoring` 的 source-specific 反例/局限边界；若运行条件离开 `4 Results; 4.1 Calibration against human labels; 4.3 white-box attack` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。 | analysis-decision:SF-2026-ARXIV-2606-25487 |
| SF-2026-ARXIV-2606-25514 | score_7_9; potential_books_delta | not_selected | — | — | 未入选长叙事：`5 Threats to Validity` 是 `Unlocking Model Potentials Through Adaptive Multi-Agent Scaffolding for Efficient Issue Resolution` 的 source-specific 反例/局限边界；若运行条件离开 `3 Evaluation; 3.2 Analysis of Exclusive Fixes and Failures` 的验证域，`AGENT-MULTI-AGENT` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。 | analysis-decision:SF-2026-ARXIV-2606-25514 |
| SF-2026-ARXIV-2606-25519 | score_7_9; potential_books_delta | not_selected | — | — | 未入选长叙事：`7 Can We Reduce Reasoning-Token Inflation; D.2 Model details` 是 `Quantization Inflates Reasoning: Token Inflation as a Hidden Cost of Low-Bit Reasoning Models` 的 source-specific 反例/局限边界；若运行条件离开 `D Additional evaluation details; D.1 Benchmarks and evaluation protocol` 的验证域，`INFER-GPU-MEMORY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。 | analysis-decision:SF-2026-ARXIV-2606-25519 |
| SF-2026-ARXIV-2606-25532 | score_7_9; potential_books_delta | not_selected | — | — | 未入选长叙事：`Exact-v1 research-prototype and evaluated hardware-design boundary` 是 `Agentic evolution of physically constrained foundation models` 的 source-specific 反例/局限边界；若运行条件离开 `Hardware-compliance evaluation and discovered-system validation` 的验证域，`PLATFORM-FOUNDATIONS` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。 | analysis-decision:SF-2026-ARXIV-2606-25532 |
| SF-2026-ARXIV-2606-25548 | score_7_9 | not_selected | — | — | 未入选长叙事：`G Limitations; D.1 Model-Architecture-Dependent Subtleties` 是 `Concept Removal for Frontier Image Generative Models` 的 source-specific 反例/局限边界；若运行条件离开 `5 Empirical Evaluation; 5.1 Experimental Setup; 5.4 Robustness` 的验证域，`TRAIN-DATA` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。 | analysis-decision:SF-2026-ARXIV-2606-25548 |
| SF-2026-ARXIV-2606-25575 | score_7_9; potential_books_delta | not_selected | — | — | 未入选长叙事：`Single wearable-hand embodiment, known objects, five tools, and short-horizon study` 是 `One Body, Two Minds: Variable Autonomy Approach for a Co-embodied Robotic Hand` 的 source-specific 反例/局限边界；若运行条件离开 `44-participant user study; five bimanual tasks; policy-variant success` 的验证域，`MULTIMODAL-EMBODIED-VLA` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。 | analysis-decision:SF-2026-ARXIV-2606-25575 |
| SF-2026-ARXIV-2606-25592 | score_7_9; potential_books_delta | not_selected | — | — | 未入选长叙事：`E.1 Limitations; E.4 Human-in-the-loop Discussion` 是 `VPA-Guard: Defending and Benchmarking Image-to-Video Generation Against Visual Prompt Attacks` 的 source-specific 反例/局限边界；若运行条件离开 `3 VVA-Bench; 3.2 Evaluation Protocol; 4 Main Experiments` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。 | analysis-decision:SF-2026-ARXIV-2606-25592 |
| SF-2026-ARXIV-2606-25605 | score_7_9; potential_books_delta | not_selected | — | — | 未入选长叙事：`7.5 Failure Cases and Limitations; 8.4 Limitations` 是 `Constraint Tax in Open-Weight LLMs: An Empirical Study of Tool Calling Suppression Under Structured Output Constraints` 的 source-specific 反例/局限边界；若运行条件离开 `5 Empirical Findings; 7.3 Experimental Evaluation; 7.4 Cost and Latency` 的验证域，`AGENT-TOOL-CALLING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。 | analysis-decision:SF-2026-ARXIV-2606-25605 |
| SF-2026-ARXIV-2606-25608 | score_7_9 | not_selected | — | — | 未入选长叙事：`V-C Restrictions of our architecture; VII Future Research` 是 `An Approach for a Supporting Multi-LLM System for Automated Certification Based on the German IT-Grundschutz` 的 source-specific 反例/局限边界；若运行条件离开 `VI Initial Evaluation` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。 | analysis-decision:SF-2026-ARXIV-2606-25608 |
| SF-2026-ARXIV-2606-25622 | score_7_9; potential_books_delta | not_selected | — | — | 未入选长叙事：`VI Limitations & Future Work` 是 `Probabilistic Agents in Deterministic Audits: Evaluating Multi-Agent Systems for Automated Audits Based on the German IT-Grundschutz` 的 source-specific 反例/局限边界；若运行条件离开 `V Results & Discussion` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。 | analysis-decision:SF-2026-ARXIV-2606-25622 |
| SF-2026-ARXIV-2606-25656 | score_7_9; potential_books_delta | not_selected | — | — | 未入选长叙事：`6 Conclusions and future work; C Retrieval-Generation Gap` 是 `Is GraphRAG Needed? From Basic RAG to Graph-/Agentic Solutions with Context Optimization` 的 source-specific 反例/局限边界；若运行条件离开 `4 Experimental setup; 5 Experimental results` 的验证域，`AGENT-RAG` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。 | analysis-decision:SF-2026-ARXIV-2606-25656 |
| SF-2026-ARXIV-2606-25658 | score_7_9; potential_books_delta | not_selected | — | — | 未入选长叙事：`A Limitations` 是 `Towards a Dynamic and Fixed-budget Memory Bank for Efficient Streaming Video Understanding` 的 source-specific 反例/局限边界；若运行条件离开 `4 Experiment; 4.1 Benchmarks and Metrics; 4.2 Implementation` 的验证域，`AGENT-MEMORY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。 | analysis-decision:SF-2026-ARXIV-2606-25658 |
| SF-2026-ARXIV-2606-25674 | score_7_9; potential_books_delta | not_selected | — | — | 未入选长叙事：`4.4 Analysis; task-type sensitivity to quantization` 是 `BitNet Text Embeddings` 的 source-specific 反例/局限边界；若运行条件离开 `4 Experiments; 4.1 Experimental Setup; B Evaluation Details` 的验证域，`AGENT-RAG` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。 | analysis-decision:SF-2026-ARXIV-2606-25674 |
| SF-2026-ARXIV-2606-25700 | score_7_9 | not_selected | — | — | 未入选长叙事：`V Discussion; V-A Choice of rank; V-C Computation` 是 `Memory-Efficient Policy Libraries with Low-Rank Adaptation in Reinforcement Learning` 的 source-specific 反例/局限边界；若运行条件离开 `IV Results; IV-B Computation calculation` 的验证域，`TRAIN-LORA` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。 | analysis-decision:SF-2026-ARXIV-2606-25700 |
| SF-2026-ARXIV-2606-25705 | score_7_9; potential_books_delta | not_selected | — | — | 未入选长叙事：`5 Conclusion; short-paper and emulator-only boundary` 是 `GUI agent: Guided Exploration of User-Sensitive Screens` 的 source-specific 反例/局限边界；若运行条件离开 `4 Experiments and Results` 的验证域，`AGENT-TOOL-CALLING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。 | analysis-decision:SF-2026-ARXIV-2606-25705 |
| SF-2026-ARXIV-2606-25721 | score_7_9; potential_books_delta | not_selected | — | — | 未入选长叙事：`6 Discussion; baseline and hyperparameter sensitivity` 是 `Tracing Target Answers in Poisoned Retrieval Corpora via Token Influence Attribution` 的 source-specific 反例/局限边界；若运行条件离开 `5 Evaluation; 5.1 Setup; 5.2 Results` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。 | analysis-decision:SF-2026-ARXIV-2606-25721 |
| SF-2026-ARXIV-2606-25759 | score_7_9; potential_books_delta | not_selected | — | — | 未入选长叙事：`9 Limitations and Future Work; A.4 Evaluation Environment and Measurement Boundary` 是 `NEURON-Fabric: Architecture-Runtime Co-Design for Controlled Low-Bit Gradient Communication` 的 source-specific 反例/局限边界；若运行条件离开 `7 Closed-Loop Cluster Evaluation; 7.1 Evaluation Setup and Scope` 的验证域，`TRAIN-DISTRIBUTED-TRAINING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。 | analysis-decision:SF-2026-ARXIV-2606-25759 |
| SF-2026-ARXIV-2606-25760 | score_7_9; potential_books_delta | not_selected | — | — | 未入选长叙事：`A4 Out-of-distribution analysis; A5 Methods deferred; A25 vendor protocol details` 是 `Uncertainty Quantification for Computer-Use Agents: A Benchmark across Vision-Language Models and GUI Grounding Datasets` 的 source-specific 反例/局限边界；若运行条件离开 `4 UQ Generalizes Selectively; 5 Graded Error and Calibration` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。 | analysis-decision:SF-2026-ARXIV-2606-25760 |
| SF-2026-ARXIV-2606-25782 | score_7_9; potential_books_delta | not_selected | — | — | 未入选长叙事：`OOD holdout and multi-turn attack boundary; 0.B Inference Throughput and Latency` 是 `Do Encoders Suffice? A Systematic Comparison of Encoder and Decoder Safety Judges for LLM Adversarial Evaluation` 的 source-specific 反例/局限边界；若运行条件离开 `5 Evaluation Protocol; 6 Results; 6.3 Cost and Latency Trade-offs` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。 | analysis-decision:SF-2026-ARXIV-2606-25782 |
| SF-2026-ARXIV-2606-25797 | score_7_9 | not_selected | — | — | 未入选长叙事：`0.A Assumptions on Sampling Access and Knowledge; 0.B Reusing Confidence is Incorrect` 是 `Confidence Sequences for Online Statistical Model Checking of Markov Decision Processes` 的 source-specific 反例/局限边界；若运行条件离开 `4 Implementation and Experimental Evaluation` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。 | analysis-decision:SF-2026-ARXIV-2606-25797 |
| SF-2026-ARXIV-2606-25819 | score_7_9; potential_books_delta | selected | DA-20260625-2606-25819 | — | 入选：`ToolBench-X; Problem Formulation; Benchmark Construction; Reliability Hazard Injection` 所定义的源特定机制用于把工具候选、模拟执行和恢复路径置于真实副作用 commit 之前；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。 | analysis:DA-20260625-2606-25819 |
| SF-2026-ARXIV-2606-25838 | score_7_9; potential_books_delta | not_selected | — | — | 未入选长叙事：`VII-C Limitations and future work` 是 `Edges Before Embeddings: A Confidence-Aware Blur Gate for Vision-Language Pipelines` 的 source-specific 反例/局限边界；若运行条件离开 `V Experiments; V-A Evaluation protocol; VI Deployment Patterns` 的验证域，`INFER-REQUEST-LIFECYCLE` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。 | analysis-decision:SF-2026-ARXIV-2606-25838 |
| SF-2026-ARXIV-2606-25863 | score_7_9; potential_books_delta | not_selected | — | — | 未入选长叙事：`PDF threats to validity; compile-time C/C++ and project-specific build-resolver boundary` 是 `Automated Detection of Configuration-Specific Security Vulnerabilities via Patch Analysis` 的 source-specific 反例/局限边界；若运行条件离开 `PDF §4 Results; 1,192 Linux, 289 FFmpeg, 100 PHP patches` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。 | analysis-decision:SF-2026-ARXIV-2606-25863 |
| SF-2026-ARXIV-2606-25871 | score_7_9; potential_books_delta | not_selected | — | — | 未入选长叙事：`5 Production Deployment and Discussion; sponsored-search relevance boundary` 是 `AutoRelAnnotator: Calibrated Model Cascades for Cost-Efficient Relevance Evaluation in Sponsored Search` 的 source-specific 反例/局限边界；若运行条件离开 `4 Experiments and Evaluation; 4.2 Dataset and Setup; 4.5 Cascade Performance` 的验证域，`TRAIN-DATA` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。 | analysis-decision:SF-2026-ARXIV-2606-25871 |
| SF-2026-ARXIV-2606-25987 | score_7_9; potential_books_delta | not_selected | — | — | 未入选长叙事：`6 Next Steps and Research Vision; technical-report preliminary-results boundary` 是 `Weave of Formal Thought` 的 source-specific 反例/局限边界；若运行条件离开 `5 WoFT Improves Surface Modeling; 5.1 Experimental setup` 的验证域，`AGENT-TOOL-CALLING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。 | analysis-decision:SF-2026-ARXIV-2606-25987 |
| SF-2026-ARXIV-2606-25996 | score_7_9; potential_books_delta | not_selected | — | — | 未入选长叙事：`6 Conclusion and Discussion; Hacking & limitations; A Token Efficiency and Truncation` 是 `Autodata: An agentic data scientist to create high quality synthetic data` 的 source-specific 反例/局限边界；若运行条件离开 `3 Experiments; CS, legal, and scientific reasoning tasks` 的验证域，`TRAIN-DATA` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。 | analysis-decision:SF-2026-ARXIV-2606-25996 |
| SF-2026-ARXIV-2606-26021 | score_7_9; potential_books_delta | not_selected | — | — | 未入选长叙事：`VIII-C Limitations and opportunities; I Context size` 是 `Privacy Vulnerabilities of Attention Layers in Tabular Foundation Models and Protection of High-Risk Queries` 的 source-specific 反例/局限边界；若运行条件离开 `IV Tabular FMs Under Standard MIAs; V-B and VI-B Experimental Results` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。 | analysis-decision:SF-2026-ARXIV-2606-26021 |
| SF-2026-ARXIV-2606-26027 | score_7_9; potential_books_delta | not_selected | — | — | 未入选长叙事：`B Training Details; C Qwen3 Training; E Training Dynamic` 是 `Why Multi-Step Tool-Use Reinforcement Learning Collapses and How Supervisory Signals Fix It` 的 source-specific 反例/局限边界；若运行条件离开 `5 Experiments; 5.1 Dataset and Models; D Detailed Evaluation` 的验证域，`TRAIN-GRPO` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。 | analysis-decision:SF-2026-ARXIV-2606-26027 |
| SF-2026-ARXIV-2606-26028 | score_7_9; potential_books_delta | not_selected | — | — | 未入选长叙事：`9 Limitations and Future Work; C x402 attribution challenges` 是 `Can Trustless Agents Be Trusted? An Empirical Study of the ERC-8004 Decentralized AI Agent Ecosystem` 的 source-specific 反例/局限边界；若运行条件离开 `4 Dataset; 5 Agent Identity and Adoption; 6 Reputation Market` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。 | analysis-decision:SF-2026-ARXIV-2606-26028 |
| SF-2026-ARXIV-2606-26057 | score_7_9; potential_books_delta | selected | DA-20260625-2606-26057 | — | 入选：`2 Threat Model; 3 Requirements; 4 Design; 5 Implementation` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。 | analysis:DA-20260625-2606-26057 |
| SF-2026-ARXIV-2606-26071 | score_7_9; potential_books_delta | not_selected | — | — | 未入选长叙事：`10 Limitations and Future Work; negative-results and confounding boundary` 是 `Model Forensics: Investigating Whether Concerning Behavior Reflects Misalignment` 的 source-specific 反例/局限边界；若运行条件离开 `6 Case Studies; 8 Recommendations` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。 | analysis-decision:SF-2026-ARXIV-2606-26071 |
| SF-2026-ARXIV-2606-26185 | score_7_9; potential_books_delta | not_selected | — | — | 未入选长叙事：`Temperature control is necessary but not sufficient; prompt/model/vendor drift remains` 是 `Necessary but Not Sufficient: Temperature Control and Reproducibility in LLM-as-Judge Safety Evaluations` 的 source-specific 反例/局限边界；若运行条件离开 `Cross-temperature, repeat-run and judge-agreement evaluation` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。 | analysis-decision:SF-2026-ARXIV-2606-26185 |
| SF-2026-ARXIV-2606-26211 | score_7_9; potential_books_delta | not_selected | — | — | 未入选长叙事：`Single ecosystem prototype; no proof of cross-vendor enforcement or semantic completeness` 是 `Data Facts: A Metadata Schema for Structured Data Exchange in the NANDini Multi-Agent Ecosystem` 的 source-specific 反例/局限边界；若运行条件离开 `NANDini multi-agent exchange examples and schema coverage` 的验证域，`AGENT-MCP` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。 | analysis-decision:SF-2026-ARXIV-2606-26211 |
| SF-2026-ARXIV-2606-26257 | score_7_9; potential_books_delta | not_selected | — | — | 未入选长叙事：`Requires the paper's observable score/query regime; not per-record legal attribution` 是 `Dataset Usage Inference without Shadow Models or Held-out Data` 的 source-specific 反例/局限边界；若运行条件离开 `Exact-v1 membership/dataset inference experiments and ablations` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。 | analysis-decision:SF-2026-ARXIV-2606-26257 |
| SF-2026-ARXIV-2606-26298 | score_7_9; potential_books_delta | not_selected | — | — | 未入选长叙事：`Institutional model is a governance proposal, not a deployed enforcement benchmark` 是 `Governing Actions, Not Agents: Institutional Attestation as a Governance Model for Autonomous AI Systems` 的 source-specific 反例/局限边界；若运行条件离开 `Action-level attestation scenarios and governance analysis` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。 | analysis-decision:SF-2026-ARXIV-2606-26298 |
| SF-2026-ARXIV-2606-26300 | score_7_9; potential_books_delta | not_selected | — | — | 未入选长叙事：`No universal reward verifier; longer horizons and hidden environment state remain` 是 `The Verification Horizon: No Silver Bullet for Coding Agent Rewards` 的 source-specific 反例/局限边界；若运行条件离开 `Reward-verification experiments across coding horizons` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。 | analysis-decision:SF-2026-ARXIV-2606-26300 |
| SF-2026-ARXIV-2606-26341 | score_7_9; potential_books_delta | not_selected | — | — | 未入选长叙事：`Only disclosed nonlinear solvers/problem shapes; no cluster-level scheduling or isolation proof` 是 `Scaling Nonlinear Optimization: Many Problems One GPU` 的 source-specific 反例/局限边界；若运行条件离开 `GPU scaling experiments across problem families` 的验证域，`PLATFORM-GPU-SCHEDULER` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。 | analysis-decision:SF-2026-ARXIV-2606-26341 |
| SF-2026-ARXIV-2606-26344 | score_7_9; potential_books_delta | not_selected | — | — | 未入选长叙事：`Covered tensor operators/hardware only; verifier does not prove arbitrary numerical equivalence` 是 `Axon: A Synthesizing Superoptimizer for Tensor Programs` 的 source-specific 反例/局限边界；若运行条件离开 `Kernel synthesis evaluation and generated-program performance` 的验证域，`INFER-TENSORRT-LLM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。 | analysis-decision:SF-2026-ARXIV-2606-26344 |
| SF-2026-ARXIV-2606-26356 | score_7_9; potential_books_delta | not_selected | — | — | 未入选长叙事：`Prompt/module families tested do not establish universal isolation or adversarial robustness` 是 `Instruction Bleed: Cross-Module Interference in Prompt-Composed Agentic Systems` 的 source-specific 反例/局限边界；若运行条件离开 `Cross-module interference experiments and mitigations` 的验证域，`AGENT-PROMPT` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。 | analysis-decision:SF-2026-ARXIV-2606-26356 |
| SF-2026-ARXIV-2606-26377 | score_7_9; potential_books_delta | not_selected | — | — | 未入选长叙事：`Evaluated threat families and judges only; intent inference is not proof of harmless execution` 是 `Verifying Intent and Harm: A Unified Defense Against LLM-Generated Threats` 的 source-specific 反例/局限边界；若运行条件离开 `Threat-generation and defense evaluation` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。 | analysis-decision:SF-2026-ARXIV-2606-26377 |
| SF-2026-ARXIV-2606-26383 | score_7_9; potential_books_delta | not_selected | — | — | 未入选长叙事：`Analytical bounds depend on calibrated hardware/workload parameters and omit undisclosed runtime effects` 是 `SOLAR: AI-Powered Speed-of-Light Performance Analysis` 的 source-specific 反例/局限边界；若运行条件离开 `Predicted-vs-observed latency and throughput analysis` 的验证域，`PLATFORM-MONITORING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。 | analysis-decision:SF-2026-ARXIV-2606-26383 |
| SF-2026-ARXIV-2606-26429 | score_7_9; potential_books_delta | not_selected | — | — | 未入选长叙事：`Joint calibration assumes the evaluated item/model pool; new distributions require refitting` 是 `DualEval: Joint Model-Item Calibration for Unified LLM Evaluation` 的 source-specific 反例/局限边界；若运行条件离开 `Unified LLM evaluation experiments and calibration analysis` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。 | analysis-decision:SF-2026-ARXIV-2606-26429 |
| SF-2026-ARXIV-2606-26439 | score_7_9; potential_books_delta | not_selected | — | — | 未入选长叙事：`Evaluated MaxSim layouts and GPUs only; index update and distributed consistency are not proved` 是 `TileMaxSim: IO-Aware GPU MaxSim Scoring with Dimension Tiling and Fused Product Quantization` 的 source-specific 反例/局限边界；若运行条件离开 `GPU retrieval throughput, latency and quality evaluation` 的验证域，`AGENT-RAG` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。 | analysis-decision:SF-2026-ARXIV-2606-26439 |
| SF-2026-ARXIV-2606-26441 | score_7_9; potential_books_delta | not_selected | — | — | 未入选长叙事：`Static benchmark indexes do not prove high-churn update cost, multi-tenant isolation or cross-node scaling` 是 `GPUSparse: GPU-Accelerated Learned Sparse Retrieval with Parallel Inverted Indices` 的 source-specific 反例/局限边界；若运行条件离开 `Retrieval quality, latency and GPU scaling experiments` 的验证域，`AGENT-RAG` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。 | analysis-decision:SF-2026-ARXIV-2606-26441 |
| SF-2026-ARXIV-2606-26442 | score_7_9; potential_books_delta | not_selected | — | — | 未入选长叙事：`Cloud utility success does not prove generated theorem correctness beyond Lean checking or side-effect safety` 是 `AXLE: A Cloud Infrastructure for Lean 4 Theorem Proving Utilities` 的 source-specific 反例/局限边界；若运行条件离开 `Utility execution, throughput and theorem-proving workflow evaluation` 的验证域，`AGENT-WORKFLOW` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。 | analysis-decision:SF-2026-ARXIV-2606-26442 |
| SF-2026-ARXIV-2606-26449 | score_7_9; potential_books_delta | not_selected | — | — | 未入选长叙事：`Trace completeness depends on instrumented producers; provenance does not imply source truth` 是 `ProvenAI: Provenance-Native Traces of Evidence in Generated Answers` 的 source-specific 反例/局限边界；若运行条件离开 `Generated-answer trace/evidence evaluation` 的验证域，`PLATFORM-TRACE` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。 | analysis-decision:SF-2026-ARXIV-2606-26449 |
| SF-2026-ARXIV-2606-26453 | score_7_9; potential_books_delta | not_selected | — | — | 未入选长叙事：`Evaluated CUDA tasks and toolchain only; profile-guided generation needs deterministic correctness fallback` 是 `Optimizing CUDA like a Human: Micro-Profiling Tools as Expert Surrogates for LLM-Based GPU Kernel Optimization` 的 source-specific 反例/局限边界；若运行条件离开 `Generated-kernel correctness, profiling and speed evaluation` 的验证域，`INFER-TENSORRT-LLM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。 | analysis-decision:SF-2026-ARXIV-2606-26453 |
| SF-2026-ARXIV-2606-26456 | score_7_9; potential_books_delta | not_selected | — | — | 未入选长叙事：`Vision paper: no completed empirical stop-rule validation; ADS component/fault model is provisional` 是 `Towards Safety-Aware Mutation Testing for Autonomous Driving Systems` 的 source-specific 反例/局限边界；若运行条件离开 `Simulation-based ADS testing protocol and proposed adequacy criterion` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。 | analysis-decision:SF-2026-ARXIV-2606-26456 |
| SF-2026-ARXIV-2606-26463 | score_7_9; potential_books_delta | not_selected | — | — | 未入选长叙事：`Game planners and timing model do not prove benefit under production tool latency or safety deadlines` 是 `Finding the Time to Think: Learning Planning Budgets in Real-Time RL` 的 source-specific 反例/局限边界；若运行条件离开 `Pac-Man, Tetris, Snake, Speed Hex and Speed Go evaluation` 的验证域，`AGENT-PLANNING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。 | analysis-decision:SF-2026-ARXIV-2606-26463 |
| SF-2026-ARXIV-2606-26472 | score_7_9; potential_books_delta | not_selected | — | — | 未入选长叙事：`Model/task transfer and representation-score drift are unproved; quality regression requires full-KV fallback` 是 `Epiphany-Aware KV Cache Eviction Without the Attention Matrix` 的 source-specific 反例/局限边界；若运行条件离开 `Long-reasoning cache/quality evaluation and 16x feasible-context claim` 的验证域，`INFER-KV-CACHE` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。 | analysis-decision:SF-2026-ARXIV-2606-26472 |
| SF-2026-ARXIV-2606-26479 | score_7_9; potential_books_delta | not_selected | — | — | 未入选长叙事：`Position/evaluation paper; static AgentDojo results do not establish adaptive robustness` 是 `Adaptive Evaluation of Out-of-Band Defenses Against Prompt Injection in LLM Agents` 的 source-specific 反例/局限边界；若运行条件离开 `Adaptive evaluation methodology against policy-aware attackers` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。 | analysis-decision:SF-2026-ARXIV-2606-26479 |
| SF-2026-ARXIV-2606-26488 | score_7_9; potential_books_delta | not_selected | — | — | 未入选长叙事：`Edge recursive models only; token-level preservation does not imply global-reasoning preservation` 是 `What Survives When You Compress a Recursive Reasoner for the Edge?` 的 source-specific 反例/局限边界；若运行条件离开 `Three tasks and two recursive architectures; local vs puzzle-exact accuracy` 的验证域，`INFER-GPU-MEMORY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。 | analysis-decision:SF-2026-ARXIV-2606-26488 |
| SF-2026-ARXIV-2606-26492 | score_7_9; potential_books_delta | not_selected | — | — | 未入选长叙事：`Fault-injected programs and studied diagnosers do not prove production root-cause validity` 是 `Evaluation-Strategy Gap in Fault Diagnosis of Deep Learning Programs` 的 source-specific 反例/局限边界；若运行条件离开 `DynFault: 5,542 traces from 38 DL programs; balanced-accuracy gap analysis` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。 | analysis-decision:SF-2026-ARXIV-2606-26492 |

<!-- analysis-decision:SF-2026-ARXIV-2606-25274:start -->
未入选长叙事：`7 Limitations` 是 `UC-Search: Risk-Aware Test-Time Search for Delayed Constrained Time-Series Control` 的 source-specific 反例/局限边界；若运行条件离开 `5 Experiments; 5.1 Implemented Evidence; 6 Analysis` 的验证域，`AGENT-PLANNING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。
<!-- analysis-decision:SF-2026-ARXIV-2606-25274:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25285:start -->
未入选长叙事：`Limitations and Discussion` 是 `EPTS: Elastic Post-Training Sparsity for Efficient Large Language Model Compression` 的 source-specific 反例/局限边界；若运行条件离开 `4 Experiments; Experimental Setup; Main Results` 的验证域，`INFER-GPU-MEMORY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。
<!-- analysis-decision:SF-2026-ARXIV-2606-25285:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25296:start -->
未入选长叙事：`Threats to Validity; Limitations` 是 `SafeGen: LLM-Driven Assertion Generation and Fault Criticality Evaluation for Functional Safety` 的 source-specific 反例/局限边界；若运行条件离开 `Experimental Evaluation; Functional-Safety Case Studies` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。
<!-- analysis-decision:SF-2026-ARXIV-2606-25296:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25342:start -->
未入选长叙事：`Discussion; finite-memory and task-family limitations` 是 `Lifelong In-Context Learning with Transformers Requires Parametric Forms of Attention` 的 source-specific 反例/局限边界；若运行条件离开 `Experiments; Lifelong sequence results` 的验证域，`MODEL-LONG-CONTEXT` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。
<!-- analysis-decision:SF-2026-ARXIV-2606-25342:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25349:start -->
未入选长叙事：`VIII Conclusion; exact-v1 analytical-evaluation-only note` 是 `General Techniques for Reducing Key-Switching Overhead in Privacy-Preserving Two-Party Transformer Inference` 的 source-specific 反例/局限边界；若运行条件离开 `VII Evaluation` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。
<!-- analysis-decision:SF-2026-ARXIV-2606-25349:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25366:start -->
未入选长叙事：`XI-D Limitations` 是 `Reliability-Asymmetric Spacecraft Autonomy: Co-Designing a Capable Learned GNC Stack with a Verified, Adaptation-Aware Runtime Shield` 的 source-specific 反例/局限边界；若运行条件离开 `VIII Robustness; IX Integrated Evaluation` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。
<!-- analysis-decision:SF-2026-ARXIV-2606-25366:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25371:start -->
未入选长叙事：`VI-D Limitations` 是 `Conformal Recovery-Deadline Certificates for Runtime Assurance of Adapting Controllers` 的 source-specific 反例/局限边界；若运行条件离开 `V Experiments` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。
<!-- analysis-decision:SF-2026-ARXIV-2606-25371:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25388:start -->
未入选长叙事：`VII Discussion and Future Work` 是 `TabClean: Reusable LLM-Synthesized Programs for Tabular Data Cleaning` 的 source-specific 反例/局限边界；若运行条件离开 `V Experimental Evaluation; V-A Experimental Setup` 的验证域，`TRAIN-DATA` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。
<!-- analysis-decision:SF-2026-ARXIV-2606-25388:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25410:start -->
未入选长叙事：`5 Conclusion; class-forgetting experimental scope` 是 `DFMU: Data-Frugal Machine Unlearning` 的 source-specific 反例/局限边界；若运行条件离开 `4 Experiments; 4.1 Experimental Setup; 4.4 Results` 的验证域，`TRAIN-DATA` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。
<!-- analysis-decision:SF-2026-ARXIV-2606-25410:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25426:start -->
未入选长叙事：`6 Conclusion; Limitations` 是 `Above the Inner Loop: Exceeding Accelerate at LLM Prefill GEMM on the M1 AMX` 的 source-specific 反例/局限边界；若运行条件离开 `4 Evaluation; 4.1 Experimental setup; 4.7 End-to-end prefill GEMM measurement` 的验证域，`INFER-PREFILL` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。
<!-- analysis-decision:SF-2026-ARXIV-2606-25426:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25447:start -->
未入选长叙事：`B Benchmark Details; C Experimental Details; stated ALFWorld boundary` 是 `The Interplay of Harness Design and Post-Training in LLM Agents` 的 source-specific 反例/局限边界；若运行条件离开 `4 Analysis; 4.1 Evaluation Protocol; 4.4 OOD Robustness` 的验证域，`AGENT-WORKFLOW` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。
<!-- analysis-decision:SF-2026-ARXIV-2606-25447:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25449:start -->
未入选长叙事：`7 Limitations` 是 `Reclaim Evaluation: A Lossy Memory Is Worse Than an Empty One` 的 source-specific 反例/局限边界；若运行条件离开 `4 Experimental Setup; 5 Results; 5.7 Boundary of the Fix` 的验证域，`AGENT-MEMORY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。
<!-- analysis-decision:SF-2026-ARXIV-2606-25449:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25453:start -->
未入选长叙事：`V-G Limitations` 是 `EmuGEMM: Fused Tensor Core Kernels for Precision Emulation in Matrix Multiplication` 的 source-specific 反例/局限边界；若运行条件离开 `V Evaluation; V-B Experimental Setup; V-F Precision-Throughput-Memory Trade-off` 的验证域，`INFER-TENSORRT-LLM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。
<!-- analysis-decision:SF-2026-ARXIV-2606-25453:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25467:start -->
未入选长叙事：`D-B Runtime Boundary and Fallback; G Implementation Scope Clarifications` 是 `RQ-SAFE: Coupled Request-Resource Scheduling for Online Edge SFC-DAGs` 的 source-specific 反例/局限边界；若运行条件离开 `V Experimental Evaluation; V-A Experimental Setup` 的验证域，`INFER-SCHEDULING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。
<!-- analysis-decision:SF-2026-ARXIV-2606-25467:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25487:start -->
未入选长叙事：`6 Limitations` 是 `How Reliable Is Your Jailbreak Judge? Calibration and Adversarial Robustness of Automated ASR Scoring` 的 source-specific 反例/局限边界；若运行条件离开 `4 Results; 4.1 Calibration against human labels; 4.3 white-box attack` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。
<!-- analysis-decision:SF-2026-ARXIV-2606-25487:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25514:start -->
未入选长叙事：`5 Threats to Validity` 是 `Unlocking Model Potentials Through Adaptive Multi-Agent Scaffolding for Efficient Issue Resolution` 的 source-specific 反例/局限边界；若运行条件离开 `3 Evaluation; 3.2 Analysis of Exclusive Fixes and Failures` 的验证域，`AGENT-MULTI-AGENT` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。
<!-- analysis-decision:SF-2026-ARXIV-2606-25514:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25519:start -->
未入选长叙事：`7 Can We Reduce Reasoning-Token Inflation; D.2 Model details` 是 `Quantization Inflates Reasoning: Token Inflation as a Hidden Cost of Low-Bit Reasoning Models` 的 source-specific 反例/局限边界；若运行条件离开 `D Additional evaluation details; D.1 Benchmarks and evaluation protocol` 的验证域，`INFER-GPU-MEMORY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。
<!-- analysis-decision:SF-2026-ARXIV-2606-25519:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25532:start -->
未入选长叙事：`Exact-v1 research-prototype and evaluated hardware-design boundary` 是 `Agentic evolution of physically constrained foundation models` 的 source-specific 反例/局限边界；若运行条件离开 `Hardware-compliance evaluation and discovered-system validation` 的验证域，`PLATFORM-FOUNDATIONS` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。
<!-- analysis-decision:SF-2026-ARXIV-2606-25532:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25548:start -->
未入选长叙事：`G Limitations; D.1 Model-Architecture-Dependent Subtleties` 是 `Concept Removal for Frontier Image Generative Models` 的 source-specific 反例/局限边界；若运行条件离开 `5 Empirical Evaluation; 5.1 Experimental Setup; 5.4 Robustness` 的验证域，`TRAIN-DATA` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。
<!-- analysis-decision:SF-2026-ARXIV-2606-25548:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25575:start -->
未入选长叙事：`Single wearable-hand embodiment, known objects, five tools, and short-horizon study` 是 `One Body, Two Minds: Variable Autonomy Approach for a Co-embodied Robotic Hand` 的 source-specific 反例/局限边界；若运行条件离开 `44-participant user study; five bimanual tasks; policy-variant success` 的验证域，`MULTIMODAL-EMBODIED-VLA` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。
<!-- analysis-decision:SF-2026-ARXIV-2606-25575:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25592:start -->
未入选长叙事：`E.1 Limitations; E.4 Human-in-the-loop Discussion` 是 `VPA-Guard: Defending and Benchmarking Image-to-Video Generation Against Visual Prompt Attacks` 的 source-specific 反例/局限边界；若运行条件离开 `3 VVA-Bench; 3.2 Evaluation Protocol; 4 Main Experiments` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。
<!-- analysis-decision:SF-2026-ARXIV-2606-25592:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25605:start -->
未入选长叙事：`7.5 Failure Cases and Limitations; 8.4 Limitations` 是 `Constraint Tax in Open-Weight LLMs: An Empirical Study of Tool Calling Suppression Under Structured Output Constraints` 的 source-specific 反例/局限边界；若运行条件离开 `5 Empirical Findings; 7.3 Experimental Evaluation; 7.4 Cost and Latency` 的验证域，`AGENT-TOOL-CALLING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。
<!-- analysis-decision:SF-2026-ARXIV-2606-25605:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25608:start -->
未入选长叙事：`V-C Restrictions of our architecture; VII Future Research` 是 `An Approach for a Supporting Multi-LLM System for Automated Certification Based on the German IT-Grundschutz` 的 source-specific 反例/局限边界；若运行条件离开 `VI Initial Evaluation` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。
<!-- analysis-decision:SF-2026-ARXIV-2606-25608:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25622:start -->
未入选长叙事：`VI Limitations & Future Work` 是 `Probabilistic Agents in Deterministic Audits: Evaluating Multi-Agent Systems for Automated Audits Based on the German IT-Grundschutz` 的 source-specific 反例/局限边界；若运行条件离开 `V Results & Discussion` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。
<!-- analysis-decision:SF-2026-ARXIV-2606-25622:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25656:start -->
未入选长叙事：`6 Conclusions and future work; C Retrieval-Generation Gap` 是 `Is GraphRAG Needed? From Basic RAG to Graph-/Agentic Solutions with Context Optimization` 的 source-specific 反例/局限边界；若运行条件离开 `4 Experimental setup; 5 Experimental results` 的验证域，`AGENT-RAG` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。
<!-- analysis-decision:SF-2026-ARXIV-2606-25656:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25658:start -->
未入选长叙事：`A Limitations` 是 `Towards a Dynamic and Fixed-budget Memory Bank for Efficient Streaming Video Understanding` 的 source-specific 反例/局限边界；若运行条件离开 `4 Experiment; 4.1 Benchmarks and Metrics; 4.2 Implementation` 的验证域，`AGENT-MEMORY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。
<!-- analysis-decision:SF-2026-ARXIV-2606-25658:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25674:start -->
未入选长叙事：`4.4 Analysis; task-type sensitivity to quantization` 是 `BitNet Text Embeddings` 的 source-specific 反例/局限边界；若运行条件离开 `4 Experiments; 4.1 Experimental Setup; B Evaluation Details` 的验证域，`AGENT-RAG` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。
<!-- analysis-decision:SF-2026-ARXIV-2606-25674:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25700:start -->
未入选长叙事：`V Discussion; V-A Choice of rank; V-C Computation` 是 `Memory-Efficient Policy Libraries with Low-Rank Adaptation in Reinforcement Learning` 的 source-specific 反例/局限边界；若运行条件离开 `IV Results; IV-B Computation calculation` 的验证域，`TRAIN-LORA` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。
<!-- analysis-decision:SF-2026-ARXIV-2606-25700:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25705:start -->
未入选长叙事：`5 Conclusion; short-paper and emulator-only boundary` 是 `GUI agent: Guided Exploration of User-Sensitive Screens` 的 source-specific 反例/局限边界；若运行条件离开 `4 Experiments and Results` 的验证域，`AGENT-TOOL-CALLING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。
<!-- analysis-decision:SF-2026-ARXIV-2606-25705:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25721:start -->
未入选长叙事：`6 Discussion; baseline and hyperparameter sensitivity` 是 `Tracing Target Answers in Poisoned Retrieval Corpora via Token Influence Attribution` 的 source-specific 反例/局限边界；若运行条件离开 `5 Evaluation; 5.1 Setup; 5.2 Results` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。
<!-- analysis-decision:SF-2026-ARXIV-2606-25721:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25759:start -->
未入选长叙事：`9 Limitations and Future Work; A.4 Evaluation Environment and Measurement Boundary` 是 `NEURON-Fabric: Architecture-Runtime Co-Design for Controlled Low-Bit Gradient Communication` 的 source-specific 反例/局限边界；若运行条件离开 `7 Closed-Loop Cluster Evaluation; 7.1 Evaluation Setup and Scope` 的验证域，`TRAIN-DISTRIBUTED-TRAINING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。
<!-- analysis-decision:SF-2026-ARXIV-2606-25759:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25760:start -->
未入选长叙事：`A4 Out-of-distribution analysis; A5 Methods deferred; A25 vendor protocol details` 是 `Uncertainty Quantification for Computer-Use Agents: A Benchmark across Vision-Language Models and GUI Grounding Datasets` 的 source-specific 反例/局限边界；若运行条件离开 `4 UQ Generalizes Selectively; 5 Graded Error and Calibration` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。
<!-- analysis-decision:SF-2026-ARXIV-2606-25760:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25782:start -->
未入选长叙事：`OOD holdout and multi-turn attack boundary; 0.B Inference Throughput and Latency` 是 `Do Encoders Suffice? A Systematic Comparison of Encoder and Decoder Safety Judges for LLM Adversarial Evaluation` 的 source-specific 反例/局限边界；若运行条件离开 `5 Evaluation Protocol; 6 Results; 6.3 Cost and Latency Trade-offs` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。
<!-- analysis-decision:SF-2026-ARXIV-2606-25782:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25797:start -->
未入选长叙事：`0.A Assumptions on Sampling Access and Knowledge; 0.B Reusing Confidence is Incorrect` 是 `Confidence Sequences for Online Statistical Model Checking of Markov Decision Processes` 的 source-specific 反例/局限边界；若运行条件离开 `4 Implementation and Experimental Evaluation` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。
<!-- analysis-decision:SF-2026-ARXIV-2606-25797:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25838:start -->
未入选长叙事：`VII-C Limitations and future work` 是 `Edges Before Embeddings: A Confidence-Aware Blur Gate for Vision-Language Pipelines` 的 source-specific 反例/局限边界；若运行条件离开 `V Experiments; V-A Evaluation protocol; VI Deployment Patterns` 的验证域，`INFER-REQUEST-LIFECYCLE` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。
<!-- analysis-decision:SF-2026-ARXIV-2606-25838:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25863:start -->
未入选长叙事：`PDF threats to validity; compile-time C/C++ and project-specific build-resolver boundary` 是 `Automated Detection of Configuration-Specific Security Vulnerabilities via Patch Analysis` 的 source-specific 反例/局限边界；若运行条件离开 `PDF §4 Results; 1,192 Linux, 289 FFmpeg, 100 PHP patches` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。
<!-- analysis-decision:SF-2026-ARXIV-2606-25863:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25871:start -->
未入选长叙事：`5 Production Deployment and Discussion; sponsored-search relevance boundary` 是 `AutoRelAnnotator: Calibrated Model Cascades for Cost-Efficient Relevance Evaluation in Sponsored Search` 的 source-specific 反例/局限边界；若运行条件离开 `4 Experiments and Evaluation; 4.2 Dataset and Setup; 4.5 Cascade Performance` 的验证域，`TRAIN-DATA` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。
<!-- analysis-decision:SF-2026-ARXIV-2606-25871:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25987:start -->
未入选长叙事：`6 Next Steps and Research Vision; technical-report preliminary-results boundary` 是 `Weave of Formal Thought` 的 source-specific 反例/局限边界；若运行条件离开 `5 WoFT Improves Surface Modeling; 5.1 Experimental setup` 的验证域，`AGENT-TOOL-CALLING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。
<!-- analysis-decision:SF-2026-ARXIV-2606-25987:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25996:start -->
未入选长叙事：`6 Conclusion and Discussion; Hacking & limitations; A Token Efficiency and Truncation` 是 `Autodata: An agentic data scientist to create high quality synthetic data` 的 source-specific 反例/局限边界；若运行条件离开 `3 Experiments; CS, legal, and scientific reasoning tasks` 的验证域，`TRAIN-DATA` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。
<!-- analysis-decision:SF-2026-ARXIV-2606-25996:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26021:start -->
未入选长叙事：`VIII-C Limitations and opportunities; I Context size` 是 `Privacy Vulnerabilities of Attention Layers in Tabular Foundation Models and Protection of High-Risk Queries` 的 source-specific 反例/局限边界；若运行条件离开 `IV Tabular FMs Under Standard MIAs; V-B and VI-B Experimental Results` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。
<!-- analysis-decision:SF-2026-ARXIV-2606-26021:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26027:start -->
未入选长叙事：`B Training Details; C Qwen3 Training; E Training Dynamic` 是 `Why Multi-Step Tool-Use Reinforcement Learning Collapses and How Supervisory Signals Fix It` 的 source-specific 反例/局限边界；若运行条件离开 `5 Experiments; 5.1 Dataset and Models; D Detailed Evaluation` 的验证域，`TRAIN-GRPO` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。
<!-- analysis-decision:SF-2026-ARXIV-2606-26027:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26028:start -->
未入选长叙事：`9 Limitations and Future Work; C x402 attribution challenges` 是 `Can Trustless Agents Be Trusted? An Empirical Study of the ERC-8004 Decentralized AI Agent Ecosystem` 的 source-specific 反例/局限边界；若运行条件离开 `4 Dataset; 5 Agent Identity and Adoption; 6 Reputation Market` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。
<!-- analysis-decision:SF-2026-ARXIV-2606-26028:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26071:start -->
未入选长叙事：`10 Limitations and Future Work; negative-results and confounding boundary` 是 `Model Forensics: Investigating Whether Concerning Behavior Reflects Misalignment` 的 source-specific 反例/局限边界；若运行条件离开 `6 Case Studies; 8 Recommendations` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。
<!-- analysis-decision:SF-2026-ARXIV-2606-26071:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26185:start -->
未入选长叙事：`Temperature control is necessary but not sufficient; prompt/model/vendor drift remains` 是 `Necessary but Not Sufficient: Temperature Control and Reproducibility in LLM-as-Judge Safety Evaluations` 的 source-specific 反例/局限边界；若运行条件离开 `Cross-temperature, repeat-run and judge-agreement evaluation` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。
<!-- analysis-decision:SF-2026-ARXIV-2606-26185:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26211:start -->
未入选长叙事：`Single ecosystem prototype; no proof of cross-vendor enforcement or semantic completeness` 是 `Data Facts: A Metadata Schema for Structured Data Exchange in the NANDini Multi-Agent Ecosystem` 的 source-specific 反例/局限边界；若运行条件离开 `NANDini multi-agent exchange examples and schema coverage` 的验证域，`AGENT-MCP` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。
<!-- analysis-decision:SF-2026-ARXIV-2606-26211:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26257:start -->
未入选长叙事：`Requires the paper's observable score/query regime; not per-record legal attribution` 是 `Dataset Usage Inference without Shadow Models or Held-out Data` 的 source-specific 反例/局限边界；若运行条件离开 `Exact-v1 membership/dataset inference experiments and ablations` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。
<!-- analysis-decision:SF-2026-ARXIV-2606-26257:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26298:start -->
未入选长叙事：`Institutional model is a governance proposal, not a deployed enforcement benchmark` 是 `Governing Actions, Not Agents: Institutional Attestation as a Governance Model for Autonomous AI Systems` 的 source-specific 反例/局限边界；若运行条件离开 `Action-level attestation scenarios and governance analysis` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。
<!-- analysis-decision:SF-2026-ARXIV-2606-26298:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26300:start -->
未入选长叙事：`No universal reward verifier; longer horizons and hidden environment state remain` 是 `The Verification Horizon: No Silver Bullet for Coding Agent Rewards` 的 source-specific 反例/局限边界；若运行条件离开 `Reward-verification experiments across coding horizons` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。
<!-- analysis-decision:SF-2026-ARXIV-2606-26300:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26341:start -->
未入选长叙事：`Only disclosed nonlinear solvers/problem shapes; no cluster-level scheduling or isolation proof` 是 `Scaling Nonlinear Optimization: Many Problems One GPU` 的 source-specific 反例/局限边界；若运行条件离开 `GPU scaling experiments across problem families` 的验证域，`PLATFORM-GPU-SCHEDULER` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。
<!-- analysis-decision:SF-2026-ARXIV-2606-26341:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26344:start -->
未入选长叙事：`Covered tensor operators/hardware only; verifier does not prove arbitrary numerical equivalence` 是 `Axon: A Synthesizing Superoptimizer for Tensor Programs` 的 source-specific 反例/局限边界；若运行条件离开 `Kernel synthesis evaluation and generated-program performance` 的验证域，`INFER-TENSORRT-LLM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。
<!-- analysis-decision:SF-2026-ARXIV-2606-26344:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26356:start -->
未入选长叙事：`Prompt/module families tested do not establish universal isolation or adversarial robustness` 是 `Instruction Bleed: Cross-Module Interference in Prompt-Composed Agentic Systems` 的 source-specific 反例/局限边界；若运行条件离开 `Cross-module interference experiments and mitigations` 的验证域，`AGENT-PROMPT` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。
<!-- analysis-decision:SF-2026-ARXIV-2606-26356:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26377:start -->
未入选长叙事：`Evaluated threat families and judges only; intent inference is not proof of harmless execution` 是 `Verifying Intent and Harm: A Unified Defense Against LLM-Generated Threats` 的 source-specific 反例/局限边界；若运行条件离开 `Threat-generation and defense evaluation` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。
<!-- analysis-decision:SF-2026-ARXIV-2606-26377:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26383:start -->
未入选长叙事：`Analytical bounds depend on calibrated hardware/workload parameters and omit undisclosed runtime effects` 是 `SOLAR: AI-Powered Speed-of-Light Performance Analysis` 的 source-specific 反例/局限边界；若运行条件离开 `Predicted-vs-observed latency and throughput analysis` 的验证域，`PLATFORM-MONITORING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。
<!-- analysis-decision:SF-2026-ARXIV-2606-26383:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26429:start -->
未入选长叙事：`Joint calibration assumes the evaluated item/model pool; new distributions require refitting` 是 `DualEval: Joint Model-Item Calibration for Unified LLM Evaluation` 的 source-specific 反例/局限边界；若运行条件离开 `Unified LLM evaluation experiments and calibration analysis` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。
<!-- analysis-decision:SF-2026-ARXIV-2606-26429:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26439:start -->
未入选长叙事：`Evaluated MaxSim layouts and GPUs only; index update and distributed consistency are not proved` 是 `TileMaxSim: IO-Aware GPU MaxSim Scoring with Dimension Tiling and Fused Product Quantization` 的 source-specific 反例/局限边界；若运行条件离开 `GPU retrieval throughput, latency and quality evaluation` 的验证域，`AGENT-RAG` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。
<!-- analysis-decision:SF-2026-ARXIV-2606-26439:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26441:start -->
未入选长叙事：`Static benchmark indexes do not prove high-churn update cost, multi-tenant isolation or cross-node scaling` 是 `GPUSparse: GPU-Accelerated Learned Sparse Retrieval with Parallel Inverted Indices` 的 source-specific 反例/局限边界；若运行条件离开 `Retrieval quality, latency and GPU scaling experiments` 的验证域，`AGENT-RAG` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。
<!-- analysis-decision:SF-2026-ARXIV-2606-26441:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26442:start -->
未入选长叙事：`Cloud utility success does not prove generated theorem correctness beyond Lean checking or side-effect safety` 是 `AXLE: A Cloud Infrastructure for Lean 4 Theorem Proving Utilities` 的 source-specific 反例/局限边界；若运行条件离开 `Utility execution, throughput and theorem-proving workflow evaluation` 的验证域，`AGENT-WORKFLOW` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。
<!-- analysis-decision:SF-2026-ARXIV-2606-26442:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26449:start -->
未入选长叙事：`Trace completeness depends on instrumented producers; provenance does not imply source truth` 是 `ProvenAI: Provenance-Native Traces of Evidence in Generated Answers` 的 source-specific 反例/局限边界；若运行条件离开 `Generated-answer trace/evidence evaluation` 的验证域，`PLATFORM-TRACE` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。
<!-- analysis-decision:SF-2026-ARXIV-2606-26449:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26453:start -->
未入选长叙事：`Evaluated CUDA tasks and toolchain only; profile-guided generation needs deterministic correctness fallback` 是 `Optimizing CUDA like a Human: Micro-Profiling Tools as Expert Surrogates for LLM-Based GPU Kernel Optimization` 的 source-specific 反例/局限边界；若运行条件离开 `Generated-kernel correctness, profiling and speed evaluation` 的验证域，`INFER-TENSORRT-LLM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。
<!-- analysis-decision:SF-2026-ARXIV-2606-26453:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26456:start -->
未入选长叙事：`Vision paper: no completed empirical stop-rule validation; ADS component/fault model is provisional` 是 `Towards Safety-Aware Mutation Testing for Autonomous Driving Systems` 的 source-specific 反例/局限边界；若运行条件离开 `Simulation-based ADS testing protocol and proposed adequacy criterion` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。
<!-- analysis-decision:SF-2026-ARXIV-2606-26456:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26463:start -->
未入选长叙事：`Game planners and timing model do not prove benefit under production tool latency or safety deadlines` 是 `Finding the Time to Think: Learning Planning Budgets in Real-Time RL` 的 source-specific 反例/局限边界；若运行条件离开 `Pac-Man, Tetris, Snake, Speed Hex and Speed Go evaluation` 的验证域，`AGENT-PLANNING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。
<!-- analysis-decision:SF-2026-ARXIV-2606-26463:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26472:start -->
未入选长叙事：`Model/task transfer and representation-score drift are unproved; quality regression requires full-KV fallback` 是 `Epiphany-Aware KV Cache Eviction Without the Attention Matrix` 的 source-specific 反例/局限边界；若运行条件离开 `Long-reasoning cache/quality evaluation and 16x feasible-context claim` 的验证域，`INFER-KV-CACHE` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。
<!-- analysis-decision:SF-2026-ARXIV-2606-26472:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26479:start -->
未入选长叙事：`Position/evaluation paper; static AgentDojo results do not establish adaptive robustness` 是 `Adaptive Evaluation of Out-of-Band Defenses Against Prompt Injection in LLM Agents` 的 source-specific 反例/局限边界；若运行条件离开 `Adaptive evaluation methodology against policy-aware attackers` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。
<!-- analysis-decision:SF-2026-ARXIV-2606-26479:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26488:start -->
未入选长叙事：`Edge recursive models only; token-level preservation does not imply global-reasoning preservation` 是 `What Survives When You Compress a Recursive Reasoner for the Edge?` 的 source-specific 反例/局限边界；若运行条件离开 `Three tasks and two recursive architectures; local vs puzzle-exact accuracy` 的验证域，`INFER-GPU-MEMORY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。
<!-- analysis-decision:SF-2026-ARXIV-2606-26488:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26492:start -->
未入选长叙事：`Fault-injected programs and studied diagnosers do not prove production root-cause validity` 是 `Evaluation-Strategy Gap in Fault Diagnosis of Deep Learning Programs` 的 source-specific 反例/局限边界；若运行条件离开 `DynFault: 5,542 traces from 38 DL programs; balanced-accuracy gap analysis` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。；Books disposition 独立保留。
<!-- analysis-decision:SF-2026-ARXIV-2606-26492:end -->

### Selected Analysis Narratives

<!-- analysis:DA-20260625-2606-26057:start -->
### The Unfireable Safety Kernel: Execution-Time AI Alignment for AI Agents and Other Escapable AI Systems

`2 Threat Model; 3 Requirements; 4 Design; 5 Implementation` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

`8.3 Limitations and Future Work; Artifact and Reproducibility` 是 `The Unfireable Safety Kernel: Execution-Time AI Alignment for AI Agents and Other Escapable AI Systems` 的 source-specific 反例/局限边界；若运行条件离开 `6 Evaluation; 6.4 Machine-Checked Fail-Closed Invariant; 6.5 Live containment` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- analysis:DA-20260625-2606-26057:end -->

<!-- analysis:DA-20260625-2606-25353:start -->
### Cache-Resident LLM Inference in GB-Scale Last-Level Caches

`3 Architecture; 3.1 Weight-Attention Decoupled Organization; 4 Implementation` 所定义的源特定机制用于把权重、attention 与 cache-blocking 路径拆成可独立放置和优化的前缀计算状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

`7 Discussion; 7.2 Future Works` 是 `Cache-Resident LLM Inference in GB-Scale Last-Level Caches` 的 source-specific 反例/局限边界；若运行条件离开 `5 Experiment Setup; 6 Evaluation` 的验证域，`INFER-PREFILL` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- analysis:DA-20260625-2606-25353:end -->

<!-- analysis:DA-20260625-2606-25819:start -->
### Beyond Function Calling: Benchmarking Tool-Using Agents under Tool-Environment Unreliability

`ToolBench-X; Problem Formulation; Benchmark Construction; Reliability Hazard Injection` 所定义的源特定机制用于把工具候选、模拟执行和恢复路径置于真实副作用 commit 之前；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

`Canonical recovery-path construction and five injected-hazard boundary` 是 `Beyond Function Calling: Benchmarking Tool-Using Agents under Tool-Environment Unreliability` 的 source-specific 反例/局限边界；若运行条件离开 `Experiments; Experimental Setup; Further Analysis; Error Analysis` 的验证域，`AGENT-TOOL-CALLING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- analysis:DA-20260625-2606-25819:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-25274 | AGENT-PLANNING | books/part-07-agent/79-planning.md#L140 | books/part-07-agent/80-reflection.md#L73 | existing:SF-2026-ARXIV-2606-25274 | delta:SF-2026-ARXIV-2606-25274 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25274 |
| SF-2026-ARXIV-2606-25285 | INFER-GPU-MEMORY | books/part-05-inference-system/54-gpu-memory.md#L186 | books/part-05-inference-system/55-pd-disaggregation.md#L409 | existing:SF-2026-ARXIV-2606-25285 | delta:SF-2026-ARXIV-2606-25285 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25285 |
| SF-2026-ARXIV-2606-25296 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L204 | books/part-06-ai-infrastructure/71-multi-tenant.md#L33 | existing:SF-2026-ARXIV-2606-25296 | delta:SF-2026-ARXIV-2606-25296 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25296 |
| SF-2026-ARXIV-2606-25342 | MODEL-LONG-CONTEXT | books/part-02-model/22-long-context.md#L374 | books/part-02-model/19-kv-cache.md#L131 | existing:SF-2026-ARXIV-2606-25342 | delta:SF-2026-ARXIV-2606-25342 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25342 |
| SF-2026-ARXIV-2606-25349 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L204 | books/part-06-ai-infrastructure/71-multi-tenant.md#L33 | existing:SF-2026-ARXIV-2606-25349 | delta:SF-2026-ARXIV-2606-25349 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25349 |
| SF-2026-ARXIV-2606-25353 | INFER-PREFILL | books/part-05-inference-system/43-prefill.md#L33 | books/part-05-inference-system/42-what-happens-during-inference.md#L117 | existing:SF-2026-ARXIV-2606-25353 | delta:SF-2026-ARXIV-2606-25353 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25353 |
| SF-2026-ARXIV-2606-25366 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L204 | books/part-06-ai-infrastructure/71-multi-tenant.md#L33 | existing:SF-2026-ARXIV-2606-25366 | delta:SF-2026-ARXIV-2606-25366 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25366 |
| SF-2026-ARXIV-2606-25371 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L204 | books/part-06-ai-infrastructure/71-multi-tenant.md#L33 | existing:SF-2026-ARXIV-2606-25371 | delta:SF-2026-ARXIV-2606-25371 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25371 |
| SF-2026-ARXIV-2606-25388 | TRAIN-DATA | books/part-04-training-system/27-data.md#L130 | books/part-04-training-system/28-pretraining.md#L244 | existing:SF-2026-ARXIV-2606-25388 | delta:SF-2026-ARXIV-2606-25388 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25388 |
| SF-2026-ARXIV-2606-25410 | TRAIN-DATA | books/part-04-training-system/27-data.md#L130 | books/part-04-training-system/28-pretraining.md#L244 | existing:SF-2026-ARXIV-2606-25410 | delta:SF-2026-ARXIV-2606-25410 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-25410 |
| SF-2026-ARXIV-2606-25426 | INFER-PREFILL | books/part-05-inference-system/43-prefill.md#L33 | books/part-05-inference-system/42-what-happens-during-inference.md#L117 | existing:SF-2026-ARXIV-2606-25426 | delta:SF-2026-ARXIV-2606-25426 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25426 |
| SF-2026-ARXIV-2606-25447 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#L36 | books/part-07-agent/78-tool-calling.md#L37 | existing:SF-2026-ARXIV-2606-25447 | delta:SF-2026-ARXIV-2606-25447 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25447 |
| SF-2026-ARXIV-2606-25449 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L900 | books/part-07-agent/76-rag.md#L57 | existing:SF-2026-ARXIV-2606-25449 | delta:SF-2026-ARXIV-2606-25449 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25449 |
| SF-2026-ARXIV-2606-25453 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#L630 | books/part-05-inference-system/48-speculative-decoding.md#L113 | existing:SF-2026-ARXIV-2606-25453 | delta:SF-2026-ARXIV-2606-25453 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25453 |
| SF-2026-ARXIV-2606-25467 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#L227 | books/part-05-inference-system/46-continuous-batching.md#L75 | existing:SF-2026-ARXIV-2606-25467 | delta:SF-2026-ARXIV-2606-25467 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25467 |
| SF-2026-ARXIV-2606-25487 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L136 | books/part-06-ai-infrastructure/59-model-registry.md#L118 | existing:SF-2026-ARXIV-2606-25487 | delta:SF-2026-ARXIV-2606-25487 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25487 |
| SF-2026-ARXIV-2606-25514 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#L240 | books/part-07-agent/81-workflow.md#L36 | existing:SF-2026-ARXIV-2606-25514 | delta:SF-2026-ARXIV-2606-25514 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25514 |
| SF-2026-ARXIV-2606-25519 | INFER-GPU-MEMORY | books/part-05-inference-system/54-gpu-memory.md#L186 | books/part-05-inference-system/55-pd-disaggregation.md#L409 | existing:SF-2026-ARXIV-2606-25519 | delta:SF-2026-ARXIV-2606-25519 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25519 |
| SF-2026-ARXIV-2606-25532 | PLATFORM-FOUNDATIONS | books/part-06-ai-infrastructure/57-what-is-ai-platform.md#L61 | books/part-06-ai-infrastructure/58-kubeflow.md#L71 | existing:SF-2026-ARXIV-2606-25532 | delta:SF-2026-ARXIV-2606-25532 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25532 |
| SF-2026-ARXIV-2606-25548 | TRAIN-DATA | books/part-04-training-system/27-data.md#L130 | books/part-04-training-system/28-pretraining.md#L244 | existing:SF-2026-ARXIV-2606-25548 | delta:SF-2026-ARXIV-2606-25548 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-25548 |
| SF-2026-ARXIV-2606-25575 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L179 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L259 | existing:SF-2026-ARXIV-2606-25575 | delta:SF-2026-ARXIV-2606-25575 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25575 |
| SF-2026-ARXIV-2606-25592 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L204 | books/part-06-ai-infrastructure/71-multi-tenant.md#L33 | existing:SF-2026-ARXIV-2606-25592 | delta:SF-2026-ARXIV-2606-25592 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25592 |
| SF-2026-ARXIV-2606-25605 | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#L55 | books/part-07-agent/81-workflow.md#L36 | existing:SF-2026-ARXIV-2606-25605 | delta:SF-2026-ARXIV-2606-25605 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25605 |
| SF-2026-ARXIV-2606-25608 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L204 | books/part-06-ai-infrastructure/71-multi-tenant.md#L33 | existing:SF-2026-ARXIV-2606-25608 | delta:SF-2026-ARXIV-2606-25608 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-25608 |
| SF-2026-ARXIV-2606-25622 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L136 | books/part-06-ai-infrastructure/59-model-registry.md#L118 | existing:SF-2026-ARXIV-2606-25622 | delta:SF-2026-ARXIV-2606-25622 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25622 |
| SF-2026-ARXIV-2606-25656 | AGENT-RAG | books/part-07-agent/76-rag.md#L51 | books/part-07-agent/77-memory.md#L113 | existing:SF-2026-ARXIV-2606-25656 | delta:SF-2026-ARXIV-2606-25656 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25656 |
| SF-2026-ARXIV-2606-25658 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L900 | books/part-07-agent/76-rag.md#L57 | existing:SF-2026-ARXIV-2606-25658 | delta:SF-2026-ARXIV-2606-25658 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25658 |
| SF-2026-ARXIV-2606-25674 | AGENT-RAG | books/part-07-agent/76-rag.md#L51 | books/part-07-agent/77-memory.md#L113 | existing:SF-2026-ARXIV-2606-25674 | delta:SF-2026-ARXIV-2606-25674 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25674 |
| SF-2026-ARXIV-2606-25700 | TRAIN-LORA | books/part-04-training-system/30-lora.md#L145 | books/part-04-training-system/29-sft.md#L194 | existing:SF-2026-ARXIV-2606-25700 | delta:SF-2026-ARXIV-2606-25700 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-25700 |
| SF-2026-ARXIV-2606-25705 | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#L55 | books/part-07-agent/81-workflow.md#L36 | existing:SF-2026-ARXIV-2606-25705 | delta:SF-2026-ARXIV-2606-25705 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25705 |
| SF-2026-ARXIV-2606-25721 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L204 | books/part-06-ai-infrastructure/71-multi-tenant.md#L33 | existing:SF-2026-ARXIV-2606-25721 | delta:SF-2026-ARXIV-2606-25721 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25721 |
| SF-2026-ARXIV-2606-25759 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#L646 | books/part-04-training-system/37-tensor-parallel.md#L243 | existing:SF-2026-ARXIV-2606-25759 | delta:SF-2026-ARXIV-2606-25759 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25759 |
| SF-2026-ARXIV-2606-25760 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L136 | books/part-06-ai-infrastructure/59-model-registry.md#L118 | existing:SF-2026-ARXIV-2606-25760 | delta:SF-2026-ARXIV-2606-25760 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25760 |
| SF-2026-ARXIV-2606-25782 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L136 | books/part-06-ai-infrastructure/59-model-registry.md#L118 | existing:SF-2026-ARXIV-2606-25782 | delta:SF-2026-ARXIV-2606-25782 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25782 |
| SF-2026-ARXIV-2606-25797 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L136 | books/part-06-ai-infrastructure/59-model-registry.md#L118 | existing:SF-2026-ARXIV-2606-25797 | delta:SF-2026-ARXIV-2606-25797 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-25797 |
| SF-2026-ARXIV-2606-25819 | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#L55 | books/part-07-agent/81-workflow.md#L36 | existing:SF-2026-ARXIV-2606-25819 | delta:SF-2026-ARXIV-2606-25819 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25819 |
| SF-2026-ARXIV-2606-25838 | INFER-REQUEST-LIFECYCLE | books/part-05-inference-system/42-what-happens-during-inference.md#L80 | books/part-05-inference-system/43-prefill.md#L33 | existing:SF-2026-ARXIV-2606-25838 | delta:SF-2026-ARXIV-2606-25838 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25838 |
| SF-2026-ARXIV-2606-25863 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L204 | books/part-06-ai-infrastructure/71-multi-tenant.md#L33 | existing:SF-2026-ARXIV-2606-25863 | delta:SF-2026-ARXIV-2606-25863 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25863 |
| SF-2026-ARXIV-2606-25871 | TRAIN-DATA | books/part-04-training-system/27-data.md#L130 | books/part-04-training-system/28-pretraining.md#L244 | existing:SF-2026-ARXIV-2606-25871 | delta:SF-2026-ARXIV-2606-25871 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25871 |
| SF-2026-ARXIV-2606-25987 | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#L55 | books/part-07-agent/81-workflow.md#L36 | existing:SF-2026-ARXIV-2606-25987 | delta:SF-2026-ARXIV-2606-25987 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25987 |
| SF-2026-ARXIV-2606-25996 | TRAIN-DATA | books/part-04-training-system/27-data.md#L130 | books/part-04-training-system/28-pretraining.md#L244 | existing:SF-2026-ARXIV-2606-25996 | delta:SF-2026-ARXIV-2606-25996 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25996 |
| SF-2026-ARXIV-2606-26021 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L204 | books/part-06-ai-infrastructure/71-multi-tenant.md#L33 | existing:SF-2026-ARXIV-2606-26021 | delta:SF-2026-ARXIV-2606-26021 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-26021 |
| SF-2026-ARXIV-2606-26027 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#L231 | books/part-04-training-system/32-ppo.md#L330 | existing:SF-2026-ARXIV-2606-26027 | delta:SF-2026-ARXIV-2606-26027 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-26027 |
| SF-2026-ARXIV-2606-26028 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L204 | books/part-06-ai-infrastructure/71-multi-tenant.md#L33 | existing:SF-2026-ARXIV-2606-26028 | delta:SF-2026-ARXIV-2606-26028 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-26028 |
| SF-2026-ARXIV-2606-26057 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L204 | books/part-06-ai-infrastructure/71-multi-tenant.md#L33 | existing:SF-2026-ARXIV-2606-26057 | delta:SF-2026-ARXIV-2606-26057 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-26057 |
| SF-2026-ARXIV-2606-26071 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L136 | books/part-06-ai-infrastructure/59-model-registry.md#L118 | existing:SF-2026-ARXIV-2606-26071 | delta:SF-2026-ARXIV-2606-26071 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-26071 |
| SF-2026-ARXIV-2606-26185 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L136 | books/part-06-ai-infrastructure/59-model-registry.md#L118 | existing:SF-2026-ARXIV-2606-26185 | delta:SF-2026-ARXIV-2606-26185 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-26185 |
| SF-2026-ARXIV-2606-26211 | AGENT-MCP | books/part-07-agent/83-mcp.md#L83 | books/part-07-agent/84-agent-platform.md#L20 | existing:SF-2026-ARXIV-2606-26211 | delta:SF-2026-ARXIV-2606-26211 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-26211 |
| SF-2026-ARXIV-2606-26257 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L204 | books/part-06-ai-infrastructure/71-multi-tenant.md#L33 | existing:SF-2026-ARXIV-2606-26257 | delta:SF-2026-ARXIV-2606-26257 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-26257 |
| SF-2026-ARXIV-2606-26298 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L204 | books/part-06-ai-infrastructure/71-multi-tenant.md#L33 | existing:SF-2026-ARXIV-2606-26298 | delta:SF-2026-ARXIV-2606-26298 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-26298 |
| SF-2026-ARXIV-2606-26300 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L136 | books/part-06-ai-infrastructure/59-model-registry.md#L118 | existing:SF-2026-ARXIV-2606-26300 | delta:SF-2026-ARXIV-2606-26300 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-26300 |
| SF-2026-ARXIV-2606-26341 | PLATFORM-GPU-SCHEDULER | books/part-06-ai-infrastructure/63-gpu-scheduler.md#L141 | books/part-06-ai-infrastructure/64-volcano.md#L44 | existing:SF-2026-ARXIV-2606-26341 | delta:SF-2026-ARXIV-2606-26341 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-26341 |
| SF-2026-ARXIV-2606-26344 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#L630 | books/part-05-inference-system/48-speculative-decoding.md#L113 | existing:SF-2026-ARXIV-2606-26344 | delta:SF-2026-ARXIV-2606-26344 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-26344 |
| SF-2026-ARXIV-2606-26356 | AGENT-PROMPT | books/part-07-agent/74-prompt.md#L46 | books/part-07-agent/75-context.md#L308 | existing:SF-2026-ARXIV-2606-26356 | delta:SF-2026-ARXIV-2606-26356 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-26356 |
| SF-2026-ARXIV-2606-26377 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L204 | books/part-06-ai-infrastructure/71-multi-tenant.md#L33 | existing:SF-2026-ARXIV-2606-26377 | delta:SF-2026-ARXIV-2606-26377 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-26377 |
| SF-2026-ARXIV-2606-26383 | PLATFORM-MONITORING | books/part-06-ai-infrastructure/67-monitoring.md#L18 | books/part-06-ai-infrastructure/68-logging.md#L16 | existing:SF-2026-ARXIV-2606-26383 | delta:SF-2026-ARXIV-2606-26383 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-26383 |
| SF-2026-ARXIV-2606-26429 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L136 | books/part-06-ai-infrastructure/59-model-registry.md#L118 | existing:SF-2026-ARXIV-2606-26429 | delta:SF-2026-ARXIV-2606-26429 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-26429 |
| SF-2026-ARXIV-2606-26439 | AGENT-RAG | books/part-07-agent/76-rag.md#L51 | books/part-07-agent/77-memory.md#L113 | existing:SF-2026-ARXIV-2606-26439 | delta:SF-2026-ARXIV-2606-26439 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-26439 |
| SF-2026-ARXIV-2606-26441 | AGENT-RAG | books/part-07-agent/76-rag.md#L51 | books/part-07-agent/77-memory.md#L113 | existing:SF-2026-ARXIV-2606-26441 | delta:SF-2026-ARXIV-2606-26441 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-26441 |
| SF-2026-ARXIV-2606-26442 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#L36 | books/part-07-agent/78-tool-calling.md#L37 | existing:SF-2026-ARXIV-2606-26442 | delta:SF-2026-ARXIV-2606-26442 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-26442 |
| SF-2026-ARXIV-2606-26449 | PLATFORM-TRACE | books/part-06-ai-infrastructure/69-trace.md#L33 | books/part-06-ai-infrastructure/68-logging.md#L66 | existing:SF-2026-ARXIV-2606-26449 | delta:SF-2026-ARXIV-2606-26449 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-26449 |
| SF-2026-ARXIV-2606-26453 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#L630 | books/part-05-inference-system/48-speculative-decoding.md#L113 | existing:SF-2026-ARXIV-2606-26453 | delta:SF-2026-ARXIV-2606-26453 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-26453 |
| SF-2026-ARXIV-2606-26456 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L136 | books/part-06-ai-infrastructure/59-model-registry.md#L118 | existing:SF-2026-ARXIV-2606-26456 | delta:SF-2026-ARXIV-2606-26456 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-26456 |
| SF-2026-ARXIV-2606-26463 | AGENT-PLANNING | books/part-07-agent/79-planning.md#L140 | books/part-07-agent/80-reflection.md#L73 | existing:SF-2026-ARXIV-2606-26463 | delta:SF-2026-ARXIV-2606-26463 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-26463 |
| SF-2026-ARXIV-2606-26472 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L97 | books/part-05-inference-system/44-decode.md#L31 | existing:SF-2026-ARXIV-2606-26472 | delta:SF-2026-ARXIV-2606-26472 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-26472 |
| SF-2026-ARXIV-2606-26479 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L204 | books/part-06-ai-infrastructure/71-multi-tenant.md#L33 | existing:SF-2026-ARXIV-2606-26479 | delta:SF-2026-ARXIV-2606-26479 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-26479 |
| SF-2026-ARXIV-2606-26488 | INFER-GPU-MEMORY | books/part-05-inference-system/54-gpu-memory.md#L186 | books/part-05-inference-system/55-pd-disaggregation.md#L409 | existing:SF-2026-ARXIV-2606-26488 | delta:SF-2026-ARXIV-2606-26488 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-26488 |
| SF-2026-ARXIV-2606-26492 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L136 | books/part-06-ai-infrastructure/59-model-registry.md#L118 | existing:SF-2026-ARXIV-2606-26492 | delta:SF-2026-ARXIV-2606-26492 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-26492 |

<!-- existing:SF-2026-ARXIV-2606-25274:start -->
At `books/part-07-agent/79-planning.md#L140`, the current owner already establishes the base responsibility for 以候选扩展或实时 gate 分配规划预算，并在超时或低置信度时回退; `books/part-07-agent/80-reflection.md#L73` only consumes the handoff. It does not yet state `3 Problem Definition; 4 Method; 4.2 Candidate Expansion; 4.3 UC-Beam`.
<!-- existing:SF-2026-ARXIV-2606-25274:end -->

<!-- delta:SF-2026-ARXIV-2606-25274:start -->
`3 Problem Definition; 4 Method; 4.2 Candidate Expansion; 4.3 UC-Beam` 所定义的源特定机制用于以候选扩展或实时 gate 分配规划预算，并在超时或低置信度时回退；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25274:end -->

<!-- books-review:SF-2026-ARXIV-2606-25274:start -->
Direct Evolution; Integrate. `7 Limitations` 是 `UC-Search: Risk-Aware Test-Time Search for Delayed Constrained Time-Series Control` 的 source-specific 反例/局限边界；若运行条件离开 `5 Experiments; 5.1 Implemented Evidence; 6 Analysis` 的验证域，`AGENT-PLANNING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25274:end -->

<!-- existing:SF-2026-ARXIV-2606-25285:start -->
At `books/part-05-inference-system/54-gpu-memory.md#L186`, the current owner already establishes the base responsibility for 把稀疏、量化或压缩决策绑定到显存预算和质量回退; `books/part-05-inference-system/55-pd-disaggregation.md#L409` only consumes the handoff. It does not yet state `3 EPTS: Elastic Post-Training Sparsity`.
<!-- existing:SF-2026-ARXIV-2606-25285:end -->

<!-- delta:SF-2026-ARXIV-2606-25285:start -->
`3 EPTS: Elastic Post-Training Sparsity` 所定义的源特定机制用于把稀疏、量化或压缩决策绑定到显存预算和质量回退；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25285:end -->

<!-- books-review:SF-2026-ARXIV-2606-25285:start -->
Direct Evolution; Integrate. `Limitations and Discussion` 是 `EPTS: Elastic Post-Training Sparsity for Efficient Large Language Model Compression` 的 source-specific 反例/局限边界；若运行条件离开 `4 Experiments; Experimental Setup; Main Results` 的验证域，`INFER-GPU-MEMORY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25285:end -->

<!-- existing:SF-2026-ARXIV-2606-25296:start -->
At `books/part-06-ai-infrastructure/72-security.md#L204`, the current owner already establishes the base responsibility for 把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界; `books/part-06-ai-infrastructure/71-multi-tenant.md#L33` only consumes the handoff. It does not yet state `SafeGen Methodology; Assertion Generation; Fault Criticality Evaluation`.
<!-- existing:SF-2026-ARXIV-2606-25296:end -->

<!-- delta:SF-2026-ARXIV-2606-25296:start -->
`SafeGen Methodology; Assertion Generation; Fault Criticality Evaluation` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25296:end -->

<!-- books-review:SF-2026-ARXIV-2606-25296:start -->
Direct Evolution; Integrate. `Threats to Validity; Limitations` 是 `SafeGen: LLM-Driven Assertion Generation and Fault Criticality Evaluation for Functional Safety` 的 source-specific 反例/局限边界；若运行条件离开 `Experimental Evaluation; Functional-Safety Case Studies` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25296:end -->

<!-- existing:SF-2026-ARXIV-2606-25342:start -->
At `books/part-02-model/22-long-context.md#L374`, the current owner already establishes the base responsibility for 把跨段记忆从隐式上下文提升为可更新的长期参数状态，并由模型路径决定写入与读取; `books/part-02-model/19-kv-cache.md#L131` only consumes the handoff. It does not yet state `Parametric Attention and Lifelong In-Context Learning formulation`.
<!-- existing:SF-2026-ARXIV-2606-25342:end -->

<!-- delta:SF-2026-ARXIV-2606-25342:start -->
`Parametric Attention and Lifelong In-Context Learning formulation` 所定义的源特定机制用于把跨段记忆从隐式上下文提升为可更新的长期参数状态，并由模型路径决定写入与读取；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25342:end -->

<!-- books-review:SF-2026-ARXIV-2606-25342:start -->
Direct Evolution; Integrate. `Discussion; finite-memory and task-family limitations` 是 `Lifelong In-Context Learning with Transformers Requires Parametric Forms of Attention` 的 source-specific 反例/局限边界；若运行条件离开 `Experiments; Lifelong sequence results` 的验证域，`MODEL-LONG-CONTEXT` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25342:end -->

<!-- existing:SF-2026-ARXIV-2606-25349:start -->
At `books/part-06-ai-infrastructure/72-security.md#L204`, the current owner already establishes the base responsibility for 把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界; `books/part-06-ai-infrastructure/71-multi-tenant.md#L33` only consumes the handoff. It does not yet state `IV Two-Party Secure Inference Algorithm; V Storage-Communication Trade-off; VI Fused Relinearization and Rotation`.
<!-- existing:SF-2026-ARXIV-2606-25349:end -->

<!-- delta:SF-2026-ARXIV-2606-25349:start -->
`IV Two-Party Secure Inference Algorithm; V Storage-Communication Trade-off; VI Fused Relinearization and Rotation` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25349:end -->

<!-- books-review:SF-2026-ARXIV-2606-25349:start -->
Direct Evolution; Integrate. `VIII Conclusion; exact-v1 analytical-evaluation-only note` 是 `General Techniques for Reducing Key-Switching Overhead in Privacy-Preserving Two-Party Transformer Inference` 的 source-specific 反例/局限边界；若运行条件离开 `VII Evaluation` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25349:end -->

<!-- existing:SF-2026-ARXIV-2606-25353:start -->
At `books/part-05-inference-system/43-prefill.md#L33`, the current owner already establishes the base responsibility for 把权重、attention 与 cache-blocking 路径拆成可独立放置和优化的前缀计算状态; `books/part-05-inference-system/42-what-happens-during-inference.md#L117` only consumes the handoff. It does not yet state `3 Architecture; 3.1 Weight-Attention Decoupled Organization; 4 Implementation`.
<!-- existing:SF-2026-ARXIV-2606-25353:end -->

<!-- delta:SF-2026-ARXIV-2606-25353:start -->
`3 Architecture; 3.1 Weight-Attention Decoupled Organization; 4 Implementation` 所定义的源特定机制用于把权重、attention 与 cache-blocking 路径拆成可独立放置和优化的前缀计算状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25353:end -->

<!-- books-review:SF-2026-ARXIV-2606-25353:start -->
Direct Evolution; Integrate. `7 Discussion; 7.2 Future Works` 是 `Cache-Resident LLM Inference in GB-Scale Last-Level Caches` 的 source-specific 反例/局限边界；若运行条件离开 `5 Experiment Setup; 6 Evaluation` 的验证域，`INFER-PREFILL` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25353:end -->

<!-- existing:SF-2026-ARXIV-2606-25366:start -->
At `books/part-06-ai-infrastructure/72-security.md#L204`, the current owner already establishes the base responsibility for 把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界; `books/part-06-ai-infrastructure/71-multi-tenant.md#L33` only consumes the handoff. It does not yet state `III System and Testbed; IV Verified Runtime Shield; VII Adaptation-Aware Runtime Assurance`.
<!-- existing:SF-2026-ARXIV-2606-25366:end -->

<!-- delta:SF-2026-ARXIV-2606-25366:start -->
`III System and Testbed; IV Verified Runtime Shield; VII Adaptation-Aware Runtime Assurance` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25366:end -->

<!-- books-review:SF-2026-ARXIV-2606-25366:start -->
Direct Evolution; Integrate. `XI-D Limitations` 是 `Reliability-Asymmetric Spacecraft Autonomy: Co-Designing a Capable Learned GNC Stack with a Verified, Adaptation-Aware Runtime Shield` 的 source-specific 反例/局限边界；若运行条件离开 `VIII Robustness; IX Integrated Evaluation` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25366:end -->

<!-- existing:SF-2026-ARXIV-2606-25371:start -->
At `books/part-06-ai-infrastructure/72-security.md#L204`, the current owner already establishes the base responsibility for 把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界; `books/part-06-ai-infrastructure/71-multi-tenant.md#L33` only consumes the handoff. It does not yet state `III Problem Setup; IV Conformal Recovery-Deadline Certificate`.
<!-- existing:SF-2026-ARXIV-2606-25371:end -->

<!-- delta:SF-2026-ARXIV-2606-25371:start -->
`III Problem Setup; IV Conformal Recovery-Deadline Certificate` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25371:end -->

<!-- books-review:SF-2026-ARXIV-2606-25371:start -->
Direct Evolution; Integrate. `VI-D Limitations` 是 `Conformal Recovery-Deadline Certificates for Runtime Assurance of Adapting Controllers` 的 source-specific 反例/局限边界；若运行条件离开 `V Experiments` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25371:end -->

<!-- existing:SF-2026-ARXIV-2606-25388:start -->
At `books/part-04-training-system/27-data.md#L130`, the current owner already establishes the base responsibility for 把数据选择、校准或验证结果变成训练前可审计的数据控制状态; `books/part-04-training-system/28-pretraining.md#L244` only consumes the handoff. It does not yet state `III System Overview; IV Methodology; IV-F Execution-Guided Validation and Control`.
<!-- existing:SF-2026-ARXIV-2606-25388:end -->

<!-- delta:SF-2026-ARXIV-2606-25388:start -->
`III System Overview; IV Methodology; IV-F Execution-Guided Validation and Control` 所定义的源特定机制用于把数据选择、校准或验证结果变成训练前可审计的数据控制状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25388:end -->

<!-- books-review:SF-2026-ARXIV-2606-25388:start -->
Direct Evolution; Integrate. `VII Discussion and Future Work` 是 `TabClean: Reusable LLM-Synthesized Programs for Tabular Data Cleaning` 的 source-specific 反例/局限边界；若运行条件离开 `V Experimental Evaluation; V-A Experimental Setup` 的验证域，`TRAIN-DATA` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25388:end -->

<!-- existing:SF-2026-ARXIV-2606-25410:start -->
At `books/part-04-training-system/27-data.md#L130`, the current owner already states the durable proposition that 把数据选择、校准或验证结果变成训练前可审计的数据控制状态; `3 Proposed Method; 3.1 Importance Score Calculation; 3.2 Weight Rescaling` is confirmatory evidence, while `books/part-04-training-system/28-pretraining.md#L244` remains a consumer rather than a second owner.
<!-- existing:SF-2026-ARXIV-2606-25410:end -->

<!-- delta:SF-2026-ARXIV-2606-25410:start -->
`3 Proposed Method; 3.1 Importance Score Calculation; 3.2 Weight Rescaling` 所定义的源特定机制用于把数据选择、校准或验证结果变成训练前可审计的数据控制状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25410:end -->

<!-- books-review:SF-2026-ARXIV-2606-25410:start -->
Layering / Dependency; No Change — Existing Coverage. `5 Conclusion; class-forgetting experimental scope` 是 `DFMU: Data-Frugal Machine Unlearning` 的 source-specific 反例/局限边界；若运行条件离开 `4 Experiments; 4.1 Experimental Setup; 4.4 Results` 的验证域，`TRAIN-DATA` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25410:end -->

<!-- existing:SF-2026-ARXIV-2606-25426:start -->
At `books/part-05-inference-system/43-prefill.md#L33`, the current owner already establishes the base responsibility for 把权重、attention 与 cache-blocking 路径拆成可独立放置和优化的前缀计算状态; `books/part-05-inference-system/42-what-happens-during-inference.md#L117` only consumes the handoff. It does not yet state `3 Method; 3.1 Three-level cache blocking; 3.2 Weight pre-packing`.
<!-- existing:SF-2026-ARXIV-2606-25426:end -->

<!-- delta:SF-2026-ARXIV-2606-25426:start -->
`3 Method; 3.1 Three-level cache blocking; 3.2 Weight pre-packing` 所定义的源特定机制用于把权重、attention 与 cache-blocking 路径拆成可独立放置和优化的前缀计算状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25426:end -->

<!-- books-review:SF-2026-ARXIV-2606-25426:start -->
Direct Evolution; Integrate. `6 Conclusion; Limitations` 是 `Above the Inner Loop: Exceeding Accelerate at LLM Prefill GEMM on the M1 AMX` 的 source-specific 反例/局限边界；若运行条件离开 `4 Evaluation; 4.1 Experimental setup; 4.7 End-to-end prefill GEMM measurement` 的验证域，`INFER-PREFILL` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25426:end -->

<!-- existing:SF-2026-ARXIV-2606-25447:start -->
At `books/part-07-agent/81-workflow.md#L36`, the current owner already establishes the base responsibility for 把执行 harness、远端 utility 与 artifact handoff 变成可观测工作流状态; `books/part-07-agent/78-tool-calling.md#L37` only consumes the handoff. It does not yet state `3 Experiment Setup; 3.2 Harness; 3.3 Tool Schema; 3.4 Task Type`.
<!-- existing:SF-2026-ARXIV-2606-25447:end -->

<!-- delta:SF-2026-ARXIV-2606-25447:start -->
`3 Experiment Setup; 3.2 Harness; 3.3 Tool Schema; 3.4 Task Type` 所定义的源特定机制用于把执行 harness、远端 utility 与 artifact handoff 变成可观测工作流状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25447:end -->

<!-- books-review:SF-2026-ARXIV-2606-25447:start -->
Direct Evolution; Integrate. `B Benchmark Details; C Experimental Details; stated ALFWorld boundary` 是 `The Interplay of Harness Design and Post-Training in LLM Agents` 的 source-specific 反例/局限边界；若运行条件离开 `4 Analysis; 4.1 Evaluation Protocol; 4.4 OOD Robustness` 的验证域，`AGENT-WORKFLOW` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25447:end -->

<!-- existing:SF-2026-ARXIV-2606-25449:start -->
At `books/part-07-agent/77-memory.md#L900`, the current owner already establishes the base responsibility for 把动态记忆写入、回收与失效变成有 owner 的持久状态迁移; `books/part-07-agent/76-rag.md#L57` only consumes the handoff. It does not yet state `3 Brittle Memory and Reclaim Evaluation; 3.2 Reclaim Protocol`.
<!-- existing:SF-2026-ARXIV-2606-25449:end -->

<!-- delta:SF-2026-ARXIV-2606-25449:start -->
`3 Brittle Memory and Reclaim Evaluation; 3.2 Reclaim Protocol` 所定义的源特定机制用于把动态记忆写入、回收与失效变成有 owner 的持久状态迁移；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25449:end -->

<!-- books-review:SF-2026-ARXIV-2606-25449:start -->
Direct Evolution; Integrate. `7 Limitations` 是 `Reclaim Evaluation: A Lossy Memory Is Worse Than an Empty One` 的 source-specific 反例/局限边界；若运行条件离开 `4 Experimental Setup; 5 Results; 5.7 Boundary of the Fix` 的验证域，`AGENT-MEMORY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25449:end -->

<!-- existing:SF-2026-ARXIV-2606-25453:start -->
At `books/part-05-inference-system/49-tensorrt-llm.md#L630`, the current owner already establishes the base responsibility for 以可验证搜索或 profiling 反馈驱动 kernel 选择，同时保留确定性正确性路径; `books/part-05-inference-system/48-speculative-decoding.md#L113` only consumes the handoff. It does not yet state `III EmuGEMM-I; IV EmuGEMM-II`.
<!-- existing:SF-2026-ARXIV-2606-25453:end -->

<!-- delta:SF-2026-ARXIV-2606-25453:start -->
`III EmuGEMM-I; IV EmuGEMM-II` 所定义的源特定机制用于以可验证搜索或 profiling 反馈驱动 kernel 选择，同时保留确定性正确性路径；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25453:end -->

<!-- books-review:SF-2026-ARXIV-2606-25453:start -->
Direct Evolution; Integrate. `V-G Limitations` 是 `EmuGEMM: Fused Tensor Core Kernels for Precision Emulation in Matrix Multiplication` 的 source-specific 反例/局限边界；若运行条件离开 `V Evaluation; V-B Experimental Setup; V-F Precision-Throughput-Memory Trade-off` 的验证域，`INFER-TENSORRT-LLM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25453:end -->

<!-- existing:SF-2026-ARXIV-2606-25467:start -->
At `books/part-05-inference-system/56-inference-scheduling.md#L227`, the current owner already establishes the base responsibility for 让在线编排器共同持有请求资源耦合、准入和降级状态; `books/part-05-inference-system/46-continuous-batching.md#L75` only consumes the handoff. It does not yet state `III Request-Resource Coupling Model; IV RQ-SAFE Online Orchestration`.
<!-- existing:SF-2026-ARXIV-2606-25467:end -->

<!-- delta:SF-2026-ARXIV-2606-25467:start -->
`III Request-Resource Coupling Model; IV RQ-SAFE Online Orchestration` 所定义的源特定机制用于让在线编排器共同持有请求资源耦合、准入和降级状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25467:end -->

<!-- books-review:SF-2026-ARXIV-2606-25467:start -->
Direct Evolution; Integrate. `D-B Runtime Boundary and Fallback; G Implementation Scope Clarifications` 是 `RQ-SAFE: Coupled Request-Resource Scheduling for Online Edge SFC-DAGs` 的 source-specific 反例/局限边界；若运行条件离开 `V Experimental Evaluation; V-A Experimental Setup` 的验证域，`INFER-SCHEDULING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25467:end -->

<!-- existing:SF-2026-ARXIV-2606-25487:start -->
At `books/part-06-ai-infrastructure/66-evaluation-system.md#L136`, the current owner already establishes the base responsibility for 把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态; `books/part-06-ai-infrastructure/59-model-registry.md#L118` only consumes the handoff. It does not yet state `3 Setup; Appendix A Prompts, wrappers, and attack configuration`.
<!-- existing:SF-2026-ARXIV-2606-25487:end -->

<!-- delta:SF-2026-ARXIV-2606-25487:start -->
`3 Setup; Appendix A Prompts, wrappers, and attack configuration` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25487:end -->

<!-- books-review:SF-2026-ARXIV-2606-25487:start -->
Direct Evolution; Integrate. `6 Limitations` 是 `How Reliable Is Your Jailbreak Judge? Calibration and Adversarial Robustness of Automated ASR Scoring` 的 source-specific 反例/局限边界；若运行条件离开 `4 Results; 4.1 Calibration against human labels; 4.3 white-box attack` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25487:end -->

<!-- existing:SF-2026-ARXIV-2606-25514:start -->
At `books/part-07-agent/82-multi-agent.md#L240`, the current owner already establishes the base responsibility for 把事件通信、角色分工与失败升级纳入多 Agent 协调状态; `books/part-07-agent/81-workflow.md#L36` only consumes the handoff. It does not yet state `2 Adaptive Multi-Agent Issue Resolution; 2.6 Event-Driven Synchronous Communication`.
<!-- existing:SF-2026-ARXIV-2606-25514:end -->

<!-- delta:SF-2026-ARXIV-2606-25514:start -->
`2 Adaptive Multi-Agent Issue Resolution; 2.6 Event-Driven Synchronous Communication` 所定义的源特定机制用于把事件通信、角色分工与失败升级纳入多 Agent 协调状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25514:end -->

<!-- books-review:SF-2026-ARXIV-2606-25514:start -->
Direct Evolution; Integrate. `5 Threats to Validity` 是 `Unlocking Model Potentials Through Adaptive Multi-Agent Scaffolding for Efficient Issue Resolution` 的 source-specific 反例/局限边界；若运行条件离开 `3 Evaluation; 3.2 Analysis of Exclusive Fixes and Failures` 的验证域，`AGENT-MULTI-AGENT` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25514:end -->

<!-- existing:SF-2026-ARXIV-2606-25519:start -->
At `books/part-05-inference-system/54-gpu-memory.md#L186`, the current owner already establishes the base responsibility for 把稀疏、量化或压缩决策绑定到显存预算和质量回退; `books/part-05-inference-system/55-pd-disaggregation.md#L409` only consumes the handoff. It does not yet state `3 Experimental Setup; 5 Quantization Inflates Reasoning Tokens; 6 Anatomy`.
<!-- existing:SF-2026-ARXIV-2606-25519:end -->

<!-- delta:SF-2026-ARXIV-2606-25519:start -->
`3 Experimental Setup; 5 Quantization Inflates Reasoning Tokens; 6 Anatomy` 所定义的源特定机制用于把稀疏、量化或压缩决策绑定到显存预算和质量回退；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25519:end -->

<!-- books-review:SF-2026-ARXIV-2606-25519:start -->
Direct Evolution; Integrate. `7 Can We Reduce Reasoning-Token Inflation; D.2 Model details` 是 `Quantization Inflates Reasoning: Token Inflation as a Hidden Cost of Low-Bit Reasoning Models` 的 source-specific 反例/局限边界；若运行条件离开 `D Additional evaluation details; D.1 Benchmarks and evaluation protocol` 的验证域，`INFER-GPU-MEMORY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25519:end -->

<!-- existing:SF-2026-ARXIV-2606-25532:start -->
At `books/part-06-ai-infrastructure/57-what-is-ai-platform.md#L61`, the current owner already establishes the base responsibility for 把硬件约束和发现链纳入平台设计候选的验收边界; `books/part-06-ai-infrastructure/58-kubeflow.md#L71` only consumes the handoff. It does not yet state `Physically constrained multi-agent discovery engine; Evolutionary Knowledge Graph and algorithmic chain of thought`.
<!-- existing:SF-2026-ARXIV-2606-25532:end -->

<!-- delta:SF-2026-ARXIV-2606-25532:start -->
`Physically constrained multi-agent discovery engine; Evolutionary Knowledge Graph and algorithmic chain of thought` 所定义的源特定机制用于把硬件约束和发现链纳入平台设计候选的验收边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25532:end -->

<!-- books-review:SF-2026-ARXIV-2606-25532:start -->
Direct Evolution; Integrate. `Exact-v1 research-prototype and evaluated hardware-design boundary` 是 `Agentic evolution of physically constrained foundation models` 的 source-specific 反例/局限边界；若运行条件离开 `Hardware-compliance evaluation and discovered-system validation` 的验证域，`PLATFORM-FOUNDATIONS` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25532:end -->

<!-- existing:SF-2026-ARXIV-2606-25548:start -->
At `books/part-04-training-system/27-data.md#L130`, the current owner already states the durable proposition that 把数据选择、校准或验证结果变成训练前可审计的数据控制状态; `4 Transcoders-based Concept Removal; 4.1 BLOCK Framework` is confirmatory evidence, while `books/part-04-training-system/28-pretraining.md#L244` remains a consumer rather than a second owner.
<!-- existing:SF-2026-ARXIV-2606-25548:end -->

<!-- delta:SF-2026-ARXIV-2606-25548:start -->
`4 Transcoders-based Concept Removal; 4.1 BLOCK Framework` 所定义的源特定机制用于把数据选择、校准或验证结果变成训练前可审计的数据控制状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25548:end -->

<!-- books-review:SF-2026-ARXIV-2606-25548:start -->
Layering / Dependency; No Change — Existing Coverage. `G Limitations; D.1 Model-Architecture-Dependent Subtleties` 是 `Concept Removal for Frontier Image Generative Models` 的 source-specific 反例/局限边界；若运行条件离开 `5 Empirical Evaluation; 5.1 Experimental Setup; 5.4 Robustness` 的验证域，`TRAIN-DATA` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25548:end -->

<!-- existing:SF-2026-ARXIV-2606-25575:start -->
At `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L179`, the current owner already establishes the base responsibility for 把任务阶段、共享自治等级和人工接管手势纳入动作控制回路; `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L259` only consumes the handoff. It does not yet state `Variable-autonomy architecture; task-phase authority transfer; always-available release gesture`.
<!-- existing:SF-2026-ARXIV-2606-25575:end -->

<!-- delta:SF-2026-ARXIV-2606-25575:start -->
`Variable-autonomy architecture; task-phase authority transfer; always-available release gesture` 所定义的源特定机制用于把任务阶段、共享自治等级和人工接管手势纳入动作控制回路；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25575:end -->

<!-- books-review:SF-2026-ARXIV-2606-25575:start -->
Direct Evolution; Integrate. `Single wearable-hand embodiment, known objects, five tools, and short-horizon study` 是 `One Body, Two Minds: Variable Autonomy Approach for a Co-embodied Robotic Hand` 的 source-specific 反例/局限边界；若运行条件离开 `44-participant user study; five bimanual tasks; policy-variant success` 的验证域，`MULTIMODAL-EMBODIED-VLA` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25575:end -->

<!-- existing:SF-2026-ARXIV-2606-25592:start -->
At `books/part-06-ai-infrastructure/72-security.md#L204`, the current owner already establishes the base responsibility for 把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界; `books/part-06-ai-infrastructure/71-multi-tenant.md#L33` only consumes the handoff. It does not yet state `2 Visual Prompt Attack and Defense; 2.2 VPA-Guard`.
<!-- existing:SF-2026-ARXIV-2606-25592:end -->

<!-- delta:SF-2026-ARXIV-2606-25592:start -->
`2 Visual Prompt Attack and Defense; 2.2 VPA-Guard` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25592:end -->

<!-- books-review:SF-2026-ARXIV-2606-25592:start -->
Direct Evolution; Integrate. `E.1 Limitations; E.4 Human-in-the-loop Discussion` 是 `VPA-Guard: Defending and Benchmarking Image-to-Video Generation Against Visual Prompt Attacks` 的 source-specific 反例/局限边界；若运行条件离开 `3 VVA-Bench; 3.2 Evaluation Protocol; 4 Main Experiments` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25592:end -->

<!-- existing:SF-2026-ARXIV-2606-25605:start -->
At `books/part-07-agent/78-tool-calling.md#L55`, the current owner already establishes the base responsibility for 把工具候选、模拟执行和恢复路径置于真实副作用 commit 之前; `books/part-07-agent/81-workflow.md#L36` only consumes the handoff. It does not yet state `3 Problem Definition; 4 Experimental Setup; 7 Transparent Two-Pass Execution`.
<!-- existing:SF-2026-ARXIV-2606-25605:end -->

<!-- delta:SF-2026-ARXIV-2606-25605:start -->
`3 Problem Definition; 4 Experimental Setup; 7 Transparent Two-Pass Execution` 所定义的源特定机制用于把工具候选、模拟执行和恢复路径置于真实副作用 commit 之前；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25605:end -->

<!-- books-review:SF-2026-ARXIV-2606-25605:start -->
Direct Evolution; Integrate. `7.5 Failure Cases and Limitations; 8.4 Limitations` 是 `Constraint Tax in Open-Weight LLMs: An Empirical Study of Tool Calling Suppression Under Structured Output Constraints` 的 source-specific 反例/局限边界；若运行条件离开 `5 Empirical Findings; 7.3 Experimental Evaluation; 7.4 Cost and Latency` 的验证域，`AGENT-TOOL-CALLING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25605:end -->

<!-- existing:SF-2026-ARXIV-2606-25608:start -->
At `books/part-06-ai-infrastructure/72-security.md#L204`, the current owner already states the durable proposition that 把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界; `V Proposed Method: Multi-LLM System; V-B Multi-LLM architecture with HybridRAG` is confirmatory evidence, while `books/part-06-ai-infrastructure/71-multi-tenant.md#L33` remains a consumer rather than a second owner.
<!-- existing:SF-2026-ARXIV-2606-25608:end -->

<!-- delta:SF-2026-ARXIV-2606-25608:start -->
`V Proposed Method: Multi-LLM System; V-B Multi-LLM architecture with HybridRAG` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25608:end -->

<!-- books-review:SF-2026-ARXIV-2606-25608:start -->
Layering / Dependency; No Change — Existing Coverage. `V-C Restrictions of our architecture; VII Future Research` 是 `An Approach for a Supporting Multi-LLM System for Automated Certification Based on the German IT-Grundschutz` 的 source-specific 反例/局限边界；若运行条件离开 `VI Initial Evaluation` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25608:end -->

<!-- existing:SF-2026-ARXIV-2606-25622:start -->
At `books/part-06-ai-infrastructure/66-evaluation-system.md#L136`, the current owner already establishes the base responsibility for 把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态; `books/part-06-ai-infrastructure/59-model-registry.md#L118` only consumes the handoff. It does not yet state `IV Theoretical Framework: MAS Architecture and Experimental Setup`.
<!-- existing:SF-2026-ARXIV-2606-25622:end -->

<!-- delta:SF-2026-ARXIV-2606-25622:start -->
`IV Theoretical Framework: MAS Architecture and Experimental Setup` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25622:end -->

<!-- books-review:SF-2026-ARXIV-2606-25622:start -->
Direct Evolution; Integrate. `VI Limitations & Future Work` 是 `Probabilistic Agents in Deterministic Audits: Evaluating Multi-Agent Systems for Automated Audits Based on the German IT-Grundschutz` 的 source-specific 反例/局限边界；若运行条件离开 `V Results & Discussion` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25622:end -->

<!-- existing:SF-2026-ARXIV-2606-25656:start -->
At `books/part-07-agent/76-rag.md#L51`, the current owner already establishes the base responsibility for 把检索索引、量化、GPU scorer 与更新一致性拆成显式数据面状态; `books/part-07-agent/77-memory.md#L113` only consumes the handoff. It does not yet state `3 Methods; 3.2 Regular RAG; 3.3 GraphRAG; 3.4 Modular and Agentic RAG; 3.5 Context Optimization`.
<!-- existing:SF-2026-ARXIV-2606-25656:end -->

<!-- delta:SF-2026-ARXIV-2606-25656:start -->
`3 Methods; 3.2 Regular RAG; 3.3 GraphRAG; 3.4 Modular and Agentic RAG; 3.5 Context Optimization` 所定义的源特定机制用于把检索索引、量化、GPU scorer 与更新一致性拆成显式数据面状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25656:end -->

<!-- books-review:SF-2026-ARXIV-2606-25656:start -->
Direct Evolution; Integrate. `6 Conclusions and future work; C Retrieval-Generation Gap` 是 `Is GraphRAG Needed? From Basic RAG to Graph-/Agentic Solutions with Context Optimization` 的 source-specific 反例/局限边界；若运行条件离开 `4 Experimental setup; 5 Experimental results` 的验证域，`AGENT-RAG` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25656:end -->

<!-- existing:SF-2026-ARXIV-2606-25658:start -->
At `books/part-07-agent/77-memory.md#L900`, the current owner already establishes the base responsibility for 把动态记忆写入、回收与失效变成有 owner 的持久状态迁移; `books/part-07-agent/76-rag.md#L57` only consumes the handoff. It does not yet state `3 Method; 3.2 Online Semantic Basis; 3.3 Dynamic Visual Memory Bank`.
<!-- existing:SF-2026-ARXIV-2606-25658:end -->

<!-- delta:SF-2026-ARXIV-2606-25658:start -->
`3 Method; 3.2 Online Semantic Basis; 3.3 Dynamic Visual Memory Bank` 所定义的源特定机制用于把动态记忆写入、回收与失效变成有 owner 的持久状态迁移；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25658:end -->

<!-- books-review:SF-2026-ARXIV-2606-25658:start -->
Direct Evolution; Integrate. `A Limitations` 是 `Towards a Dynamic and Fixed-budget Memory Bank for Efficient Streaming Video Understanding` 的 source-specific 反例/局限边界；若运行条件离开 `4 Experiment; 4.1 Benchmarks and Metrics; 4.2 Implementation` 的验证域，`AGENT-MEMORY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25658:end -->

<!-- existing:SF-2026-ARXIV-2606-25674:start -->
At `books/part-07-agent/76-rag.md#L51`, the current owner already establishes the base responsibility for 把检索索引、量化、GPU scorer 与更新一致性拆成显式数据面状态; `books/part-07-agent/77-memory.md#L113` only consumes the handoff. It does not yet state `3 Method; 3.2 Low-bit Embedding Backbone; 3.5 Multi-precision Embedding Quantization`.
<!-- existing:SF-2026-ARXIV-2606-25674:end -->

<!-- delta:SF-2026-ARXIV-2606-25674:start -->
`3 Method; 3.2 Low-bit Embedding Backbone; 3.5 Multi-precision Embedding Quantization` 所定义的源特定机制用于把检索索引、量化、GPU scorer 与更新一致性拆成显式数据面状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25674:end -->

<!-- books-review:SF-2026-ARXIV-2606-25674:start -->
Direct Evolution; Integrate. `4.4 Analysis; task-type sensitivity to quantization` 是 `BitNet Text Embeddings` 的 source-specific 反例/局限边界；若运行条件离开 `4 Experiments; 4.1 Experimental Setup; B Evaluation Details` 的验证域，`AGENT-RAG` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25674:end -->

<!-- existing:SF-2026-ARXIV-2606-25700:start -->
At `books/part-04-training-system/30-lora.md#L145`, the current owner already states the durable proposition that 把秩、适配器容量与计算预算绑定为显式训练配置; `III Methods; III-B Training; III-C Architecture` is confirmatory evidence, while `books/part-04-training-system/29-sft.md#L194` remains a consumer rather than a second owner.
<!-- existing:SF-2026-ARXIV-2606-25700:end -->

<!-- delta:SF-2026-ARXIV-2606-25700:start -->
`III Methods; III-B Training; III-C Architecture` 所定义的源特定机制用于把秩、适配器容量与计算预算绑定为显式训练配置；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25700:end -->

<!-- books-review:SF-2026-ARXIV-2606-25700:start -->
Layering / Dependency; No Change — Existing Coverage. `V Discussion; V-A Choice of rank; V-C Computation` 是 `Memory-Efficient Policy Libraries with Low-Rank Adaptation in Reinforcement Learning` 的 source-specific 反例/局限边界；若运行条件离开 `IV Results; IV-B Computation calculation` 的验证域，`TRAIN-LORA` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25700:end -->

<!-- existing:SF-2026-ARXIV-2606-25705:start -->
At `books/part-07-agent/78-tool-calling.md#L55`, the current owner already establishes the base responsibility for 把工具候选、模拟执行和恢复路径置于真实副作用 commit 之前; `books/part-07-agent/81-workflow.md#L36` only consumes the handoff. It does not yet state `3 Methodology; 3.1 Query Selection, Expansion and Saturation; 3.2 Roll-out with Emulator`.
<!-- existing:SF-2026-ARXIV-2606-25705:end -->

<!-- delta:SF-2026-ARXIV-2606-25705:start -->
`3 Methodology; 3.1 Query Selection, Expansion and Saturation; 3.2 Roll-out with Emulator` 所定义的源特定机制用于把工具候选、模拟执行和恢复路径置于真实副作用 commit 之前；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25705:end -->

<!-- books-review:SF-2026-ARXIV-2606-25705:start -->
Direct Evolution; Integrate. `5 Conclusion; short-paper and emulator-only boundary` 是 `GUI agent: Guided Exploration of User-Sensitive Screens` 的 source-specific 反例/局限边界；若运行条件离开 `4 Experiments and Results` 的验证域，`AGENT-TOOL-CALLING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25705:end -->

<!-- existing:SF-2026-ARXIV-2606-25721:start -->
At `books/part-06-ai-infrastructure/72-security.md#L204`, the current owner already establishes the base responsibility for 把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界; `books/part-06-ai-infrastructure/71-multi-tenant.md#L33` only consumes the handoff. It does not yet state `4 Method; 4.1 Keyword Searching; 4.2 Secondary Verification`.
<!-- existing:SF-2026-ARXIV-2606-25721:end -->

<!-- delta:SF-2026-ARXIV-2606-25721:start -->
`4 Method; 4.1 Keyword Searching; 4.2 Secondary Verification` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25721:end -->

<!-- books-review:SF-2026-ARXIV-2606-25721:start -->
Direct Evolution; Integrate. `6 Discussion; baseline and hyperparameter sensitivity` 是 `Tracing Target Answers in Poisoned Retrieval Corpora via Token Influence Attribution` 的 source-specific 反例/局限边界；若运行条件离开 `5 Evaluation; 5.1 Setup; 5.2 Results` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25721:end -->

<!-- existing:SF-2026-ARXIV-2606-25759:start -->
At `books/part-04-training-system/36-distributed-training.md#L646`, the current owner already establishes the base responsibility for 把集群运行剖面映射为运行时 bucket 与并行绑定状态; `books/part-04-training-system/37-tensor-parallel.md#L243` only consumes the handoff. It does not yet state `3 System Overview; 4 Operating-Profile Calibration; 5 Runtime Binding and Bucket Routing`.
<!-- existing:SF-2026-ARXIV-2606-25759:end -->

<!-- delta:SF-2026-ARXIV-2606-25759:start -->
`3 System Overview; 4 Operating-Profile Calibration; 5 Runtime Binding and Bucket Routing` 所定义的源特定机制用于把集群运行剖面映射为运行时 bucket 与并行绑定状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25759:end -->

<!-- books-review:SF-2026-ARXIV-2606-25759:start -->
Direct Evolution; Integrate. `9 Limitations and Future Work; A.4 Evaluation Environment and Measurement Boundary` 是 `NEURON-Fabric: Architecture-Runtime Co-Design for Controlled Low-Bit Gradient Communication` 的 source-specific 反例/局限边界；若运行条件离开 `7 Closed-Loop Cluster Evaluation; 7.1 Evaluation Setup and Scope` 的验证域，`TRAIN-DISTRIBUTED-TRAINING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25759:end -->

<!-- existing:SF-2026-ARXIV-2606-25760:start -->
At `books/part-06-ai-infrastructure/66-evaluation-system.md#L136`, the current owner already establishes the base responsibility for 把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态; `books/part-06-ai-infrastructure/59-model-registry.md#L118` only consumes the handoff. It does not yet state `3 Benchmark and Evaluation Protocol; 7 Inductive-Conformal Click Disks`.
<!-- existing:SF-2026-ARXIV-2606-25760:end -->

<!-- delta:SF-2026-ARXIV-2606-25760:start -->
`3 Benchmark and Evaluation Protocol; 7 Inductive-Conformal Click Disks` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25760:end -->

<!-- books-review:SF-2026-ARXIV-2606-25760:start -->
Direct Evolution; Integrate. `A4 Out-of-distribution analysis; A5 Methods deferred; A25 vendor protocol details` 是 `Uncertainty Quantification for Computer-Use Agents: A Benchmark across Vision-Language Models and GUI Grounding Datasets` 的 source-specific 反例/局限边界；若运行条件离开 `4 UQ Generalizes Selectively; 5 Graded Error and Calibration` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25760:end -->

<!-- existing:SF-2026-ARXIV-2606-25782:start -->
At `books/part-06-ai-infrastructure/66-evaluation-system.md#L136`, the current owner already establishes the base responsibility for 把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态; `books/part-06-ai-infrastructure/59-model-registry.md#L118` only consumes the handoff. It does not yet state `2 Dataset; 3 Adversarial Attack Methodology; 4 Safety Judge Panel`.
<!-- existing:SF-2026-ARXIV-2606-25782:end -->

<!-- delta:SF-2026-ARXIV-2606-25782:start -->
`2 Dataset; 3 Adversarial Attack Methodology; 4 Safety Judge Panel` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25782:end -->

<!-- books-review:SF-2026-ARXIV-2606-25782:start -->
Direct Evolution; Integrate. `OOD holdout and multi-turn attack boundary; 0.B Inference Throughput and Latency` 是 `Do Encoders Suffice? A Systematic Comparison of Encoder and Decoder Safety Judges for LLM Adversarial Evaluation` 的 source-specific 反例/局限边界；若运行条件离开 `5 Evaluation Protocol; 6 Results; 6.3 Cost and Latency Trade-offs` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25782:end -->

<!-- existing:SF-2026-ARXIV-2606-25797:start -->
At `books/part-06-ai-infrastructure/66-evaluation-system.md#L136`, the current owner already states the durable proposition that 把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态; `3 Improving Online MDP-SMC; 3.2 Confidence Sequences; 3.4 Confidence Sequence MDP-SMC` is confirmatory evidence, while `books/part-06-ai-infrastructure/59-model-registry.md#L118` remains a consumer rather than a second owner.
<!-- existing:SF-2026-ARXIV-2606-25797:end -->

<!-- delta:SF-2026-ARXIV-2606-25797:start -->
`3 Improving Online MDP-SMC; 3.2 Confidence Sequences; 3.4 Confidence Sequence MDP-SMC` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25797:end -->

<!-- books-review:SF-2026-ARXIV-2606-25797:start -->
Layering / Dependency; No Change — Existing Coverage. `0.A Assumptions on Sampling Access and Knowledge; 0.B Reusing Confidence is Incorrect` 是 `Confidence Sequences for Online Statistical Model Checking of Markov Decision Processes` 的 source-specific 反例/局限边界；若运行条件离开 `4 Implementation and Experimental Evaluation` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25797:end -->

<!-- existing:SF-2026-ARXIV-2606-25819:start -->
At `books/part-07-agent/78-tool-calling.md#L55`, the current owner already establishes the base responsibility for 把工具候选、模拟执行和恢复路径置于真实副作用 commit 之前; `books/part-07-agent/81-workflow.md#L36` only consumes the handoff. It does not yet state `ToolBench-X; Problem Formulation; Benchmark Construction; Reliability Hazard Injection`.
<!-- existing:SF-2026-ARXIV-2606-25819:end -->

<!-- delta:SF-2026-ARXIV-2606-25819:start -->
`ToolBench-X; Problem Formulation; Benchmark Construction; Reliability Hazard Injection` 所定义的源特定机制用于把工具候选、模拟执行和恢复路径置于真实副作用 commit 之前；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25819:end -->

<!-- books-review:SF-2026-ARXIV-2606-25819:start -->
Direct Evolution; Integrate. `Canonical recovery-path construction and five injected-hazard boundary` 是 `Beyond Function Calling: Benchmarking Tool-Using Agents under Tool-Environment Unreliability` 的 source-specific 反例/局限边界；若运行条件离开 `Experiments; Experimental Setup; Further Analysis; Error Analysis` 的验证域，`AGENT-TOOL-CALLING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25819:end -->

<!-- existing:SF-2026-ARXIV-2606-25838:start -->
At `books/part-05-inference-system/42-what-happens-during-inference.md#L80`, the current owner already establishes the base responsibility for 让路由器基于请求置信度持有后端选择与回退权; `books/part-05-inference-system/43-prefill.md#L33` only consumes the handoff. It does not yet state `III Method; IV Confidence-Aware Routing`.
<!-- existing:SF-2026-ARXIV-2606-25838:end -->

<!-- delta:SF-2026-ARXIV-2606-25838:start -->
`III Method; IV Confidence-Aware Routing` 所定义的源特定机制用于让路由器基于请求置信度持有后端选择与回退权；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25838:end -->

<!-- books-review:SF-2026-ARXIV-2606-25838:start -->
Direct Evolution; Integrate. `VII-C Limitations and future work` 是 `Edges Before Embeddings: A Confidence-Aware Blur Gate for Vision-Language Pipelines` 的 source-specific 反例/局限边界；若运行条件离开 `V Experiments; V-A Evaluation protocol; VI Deployment Patterns` 的验证域，`INFER-REQUEST-LIFECYCLE` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25838:end -->

<!-- existing:SF-2026-ARXIV-2606-25863:start -->
At `books/part-06-ai-infrastructure/72-security.md#L204`, the current owner already establishes the base responsibility for 把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界; `books/part-06-ai-infrastructure/71-multi-tenant.md#L33` only consumes the handoff. It does not yet state `PDF §3 Research Design; §3.3 PatchLens static analysis and build-system resolution`.
<!-- existing:SF-2026-ARXIV-2606-25863:end -->

<!-- delta:SF-2026-ARXIV-2606-25863:start -->
`PDF §3 Research Design; §3.3 PatchLens static analysis and build-system resolution` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25863:end -->

<!-- books-review:SF-2026-ARXIV-2606-25863:start -->
Direct Evolution; Integrate. `PDF threats to validity; compile-time C/C++ and project-specific build-resolver boundary` 是 `Automated Detection of Configuration-Specific Security Vulnerabilities via Patch Analysis` 的 source-specific 反例/局限边界；若运行条件离开 `PDF §4 Results; 1,192 Linux, 289 FFmpeg, 100 PHP patches` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25863:end -->

<!-- existing:SF-2026-ARXIV-2606-25871:start -->
At `books/part-04-training-system/27-data.md#L130`, the current owner already establishes the base responsibility for 把数据选择、校准或验证结果变成训练前可审计的数据控制状态; `books/part-04-training-system/28-pretraining.md#L244` only consumes the handoff. It does not yet state `3 Our Approach; 3.1 System Architecture; 3.3 Per-Class Isotonic Calibration; 3.4 Cascade Decision Logic`.
<!-- existing:SF-2026-ARXIV-2606-25871:end -->

<!-- delta:SF-2026-ARXIV-2606-25871:start -->
`3 Our Approach; 3.1 System Architecture; 3.3 Per-Class Isotonic Calibration; 3.4 Cascade Decision Logic` 所定义的源特定机制用于把数据选择、校准或验证结果变成训练前可审计的数据控制状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25871:end -->

<!-- books-review:SF-2026-ARXIV-2606-25871:start -->
Direct Evolution; Integrate. `5 Production Deployment and Discussion; sponsored-search relevance boundary` 是 `AutoRelAnnotator: Calibrated Model Cascades for Cost-Efficient Relevance Evaluation in Sponsored Search` 的 source-specific 反例/局限边界；若运行条件离开 `4 Experiments and Evaluation; 4.2 Dataset and Setup; 4.5 Cascade Performance` 的验证域，`TRAIN-DATA` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25871:end -->

<!-- existing:SF-2026-ARXIV-2606-25987:start -->
At `books/part-07-agent/78-tool-calling.md#L55`, the current owner already establishes the base responsibility for 把工具候选、模拟执行和恢复路径置于真实副作用 commit 之前; `books/part-07-agent/81-workflow.md#L36` only consumes the handoff. It does not yet state `3 Formal Engine; 3.2 Architecture; 4 Weave of Formal Thought`.
<!-- existing:SF-2026-ARXIV-2606-25987:end -->

<!-- delta:SF-2026-ARXIV-2606-25987:start -->
`3 Formal Engine; 3.2 Architecture; 4 Weave of Formal Thought` 所定义的源特定机制用于把工具候选、模拟执行和恢复路径置于真实副作用 commit 之前；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25987:end -->

<!-- books-review:SF-2026-ARXIV-2606-25987:start -->
Direct Evolution; Integrate. `6 Next Steps and Research Vision; technical-report preliminary-results boundary` 是 `Weave of Formal Thought` 的 source-specific 反例/局限边界；若运行条件离开 `5 WoFT Improves Surface Modeling; 5.1 Experimental setup` 的验证域，`AGENT-TOOL-CALLING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25987:end -->

<!-- existing:SF-2026-ARXIV-2606-25996:start -->
At `books/part-04-training-system/27-data.md#L130`, the current owner already establishes the base responsibility for 把数据选择、校准或验证结果变成训练前可审计的数据控制状态; `books/part-04-training-system/28-pretraining.md#L244` only consumes the handoff. It does not yet state `2 Autodata; 2.1 Agentic Self-Instruct; 4 Meta Optimization of the Data Scientist`.
<!-- existing:SF-2026-ARXIV-2606-25996:end -->

<!-- delta:SF-2026-ARXIV-2606-25996:start -->
`2 Autodata; 2.1 Agentic Self-Instruct; 4 Meta Optimization of the Data Scientist` 所定义的源特定机制用于把数据选择、校准或验证结果变成训练前可审计的数据控制状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25996:end -->

<!-- books-review:SF-2026-ARXIV-2606-25996:start -->
Direct Evolution; Integrate. `6 Conclusion and Discussion; Hacking & limitations; A Token Efficiency and Truncation` 是 `Autodata: An agentic data scientist to create high quality synthetic data` 的 source-specific 反例/局限边界；若运行条件离开 `3 Experiments; CS, legal, and scientific reasoning tasks` 的验证域，`TRAIN-DATA` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25996:end -->

<!-- existing:SF-2026-ARXIV-2606-26021:start -->
At `books/part-06-ai-infrastructure/72-security.md#L204`, the current owner already establishes the base responsibility for 把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界; `books/part-06-ai-infrastructure/71-multi-tenant.md#L33` only consumes the handoff. It does not yet state `V Attention-based MIA; VI Inference-Time Hardening Against MIAs`.
<!-- existing:SF-2026-ARXIV-2606-26021:end -->

<!-- delta:SF-2026-ARXIV-2606-26021:start -->
`V Attention-based MIA; VI Inference-Time Hardening Against MIAs` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-26021:end -->

<!-- books-review:SF-2026-ARXIV-2606-26021:start -->
Direct Evolution; Integrate. `VIII-C Limitations and opportunities; I Context size` 是 `Privacy Vulnerabilities of Attention Layers in Tabular Foundation Models and Protection of High-Risk Queries` 的 source-specific 反例/局限边界；若运行条件离开 `IV Tabular FMs Under Standard MIAs; V-B and VI-B Experimental Results` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-26021:end -->

<!-- existing:SF-2026-ARXIV-2606-26027:start -->
At `books/part-04-training-system/33-grpo.md#L231`, the current owner already establishes the base responsibility for 把崩溃信号与监督修复绑定到策略更新门控; `books/part-04-training-system/32-ppo.md#L330` only consumes the handoff. It does not yet state `4 Method; 4.2 catastrophic collapse; 4.4 supervisory fixes`.
<!-- existing:SF-2026-ARXIV-2606-26027:end -->

<!-- delta:SF-2026-ARXIV-2606-26027:start -->
`4 Method; 4.2 catastrophic collapse; 4.4 supervisory fixes` 所定义的源特定机制用于把崩溃信号与监督修复绑定到策略更新门控；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-26027:end -->

<!-- books-review:SF-2026-ARXIV-2606-26027:start -->
Direct Evolution; Integrate. `B Training Details; C Qwen3 Training; E Training Dynamic` 是 `Why Multi-Step Tool-Use Reinforcement Learning Collapses and How Supervisory Signals Fix It` 的 source-specific 反例/局限边界；若运行条件离开 `5 Experiments; 5.1 Dataset and Models; D Detailed Evaluation` 的验证域，`TRAIN-GRPO` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-26027:end -->

<!-- existing:SF-2026-ARXIV-2606-26028:start -->
At `books/part-06-ai-infrastructure/72-security.md#L204`, the current owner already establishes the base responsibility for 把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界; `books/part-06-ai-infrastructure/71-multi-tenant.md#L33` only consumes the handoff. It does not yet state `3 System Model: ERC-8004 Protocol; 7 Reputation Market Security`.
<!-- existing:SF-2026-ARXIV-2606-26028:end -->

<!-- delta:SF-2026-ARXIV-2606-26028:start -->
`3 System Model: ERC-8004 Protocol; 7 Reputation Market Security` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-26028:end -->

<!-- books-review:SF-2026-ARXIV-2606-26028:start -->
Direct Evolution; Integrate. `9 Limitations and Future Work; C x402 attribution challenges` 是 `Can Trustless Agents Be Trusted? An Empirical Study of the ERC-8004 Decentralized AI Agent Ecosystem` 的 source-specific 反例/局限边界；若运行条件离开 `4 Dataset; 5 Agent Identity and Adoption; 6 Reputation Market` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-26028:end -->

<!-- existing:SF-2026-ARXIV-2606-26057:start -->
At `books/part-06-ai-infrastructure/72-security.md#L204`, the current owner already establishes the base responsibility for 把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界; `books/part-06-ai-infrastructure/71-multi-tenant.md#L33` only consumes the handoff. It does not yet state `2 Threat Model; 3 Requirements; 4 Design; 5 Implementation`.
<!-- existing:SF-2026-ARXIV-2606-26057:end -->

<!-- delta:SF-2026-ARXIV-2606-26057:start -->
`2 Threat Model; 3 Requirements; 4 Design; 5 Implementation` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-26057:end -->

<!-- books-review:SF-2026-ARXIV-2606-26057:start -->
Direct Evolution; Integrate. `8.3 Limitations and Future Work; Artifact and Reproducibility` 是 `The Unfireable Safety Kernel: Execution-Time AI Alignment for AI Agents and Other Escapable AI Systems` 的 source-specific 反例/局限边界；若运行条件离开 `6 Evaluation; 6.4 Machine-Checked Fail-Closed Invariant; 6.5 Live containment` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-26057:end -->

<!-- existing:SF-2026-ARXIV-2606-26071:start -->
At `books/part-06-ai-infrastructure/66-evaluation-system.md#L136`, the current owner already establishes the base responsibility for 把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态; `books/part-06-ai-infrastructure/59-model-registry.md#L118` only consumes the handoff. It does not yet state `4 Protocol and Methods; 5 Environments; 7 Methodological Insights`.
<!-- existing:SF-2026-ARXIV-2606-26071:end -->

<!-- delta:SF-2026-ARXIV-2606-26071:start -->
`4 Protocol and Methods; 5 Environments; 7 Methodological Insights` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-26071:end -->

<!-- books-review:SF-2026-ARXIV-2606-26071:start -->
Direct Evolution; Integrate. `10 Limitations and Future Work; negative-results and confounding boundary` 是 `Model Forensics: Investigating Whether Concerning Behavior Reflects Misalignment` 的 source-specific 反例/局限边界；若运行条件离开 `6 Case Studies; 8 Recommendations` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-26071:end -->

<!-- existing:SF-2026-ARXIV-2606-26185:start -->
At `books/part-06-ai-infrastructure/66-evaluation-system.md#L136`, the current owner already establishes the base responsibility for 把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态; `books/part-06-ai-infrastructure/59-model-registry.md#L118` only consumes the handoff. It does not yet state `Temperature-control and reproducibility protocol for LLM-as-judge safety evaluation`.
<!-- existing:SF-2026-ARXIV-2606-26185:end -->

<!-- delta:SF-2026-ARXIV-2606-26185:start -->
`Temperature-control and reproducibility protocol for LLM-as-judge safety evaluation` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-26185:end -->

<!-- books-review:SF-2026-ARXIV-2606-26185:start -->
Direct Evolution; Integrate. `Temperature control is necessary but not sufficient; prompt/model/vendor drift remains` 是 `Necessary but Not Sufficient: Temperature Control and Reproducibility in LLM-as-Judge Safety Evaluations` 的 source-specific 反例/局限边界；若运行条件离开 `Cross-temperature, repeat-run and judge-agreement evaluation` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-26185:end -->

<!-- existing:SF-2026-ARXIV-2606-26211:start -->
At `books/part-07-agent/83-mcp.md#L83`, the current owner already establishes the base responsibility for 以带 provenance、语义和约束的 Data Facts 作为跨 Agent 交换契约; `books/part-07-agent/84-agent-platform.md#L20` only consumes the handoff. It does not yet state `Data Facts metadata schema; provenance, semantics, constraints and exchange contract`.
<!-- existing:SF-2026-ARXIV-2606-26211:end -->

<!-- delta:SF-2026-ARXIV-2606-26211:start -->
`Data Facts metadata schema; provenance, semantics, constraints and exchange contract` 所定义的源特定机制用于以带 provenance、语义和约束的 Data Facts 作为跨 Agent 交换契约；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-26211:end -->

<!-- books-review:SF-2026-ARXIV-2606-26211:start -->
Direct Evolution; Integrate. `Single ecosystem prototype; no proof of cross-vendor enforcement or semantic completeness` 是 `Data Facts: A Metadata Schema for Structured Data Exchange in the NANDini Multi-Agent Ecosystem` 的 source-specific 反例/局限边界；若运行条件离开 `NANDini multi-agent exchange examples and schema coverage` 的验证域，`AGENT-MCP` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-26211:end -->

<!-- existing:SF-2026-ARXIV-2606-26257:start -->
At `books/part-06-ai-infrastructure/72-security.md#L204`, the current owner already establishes the base responsibility for 把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界; `books/part-06-ai-infrastructure/71-multi-tenant.md#L33` only consumes the handoff. It does not yet state `Dataset Usage Inference formulation without shadow models or held-out data`.
<!-- existing:SF-2026-ARXIV-2606-26257:end -->

<!-- delta:SF-2026-ARXIV-2606-26257:start -->
`Dataset Usage Inference formulation without shadow models or held-out data` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-26257:end -->

<!-- books-review:SF-2026-ARXIV-2606-26257:start -->
Direct Evolution; Integrate. `Requires the paper's observable score/query regime; not per-record legal attribution` 是 `Dataset Usage Inference without Shadow Models or Held-out Data` 的 source-specific 反例/局限边界；若运行条件离开 `Exact-v1 membership/dataset inference experiments and ablations` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-26257:end -->

<!-- existing:SF-2026-ARXIV-2606-26298:start -->
At `books/part-06-ai-infrastructure/72-security.md#L204`, the current owner already establishes the base responsibility for 把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界; `books/part-06-ai-infrastructure/71-multi-tenant.md#L33` only consumes the handoff. It does not yet state `Governing Actions, Not Agents; Institutional Attestation model`.
<!-- existing:SF-2026-ARXIV-2606-26298:end -->

<!-- delta:SF-2026-ARXIV-2606-26298:start -->
`Governing Actions, Not Agents; Institutional Attestation model` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-26298:end -->

<!-- books-review:SF-2026-ARXIV-2606-26298:start -->
Direct Evolution; Integrate. `Institutional model is a governance proposal, not a deployed enforcement benchmark` 是 `Governing Actions, Not Agents: Institutional Attestation as a Governance Model for Autonomous AI Systems` 的 source-specific 反例/局限边界；若运行条件离开 `Action-level attestation scenarios and governance analysis` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-26298:end -->

<!-- existing:SF-2026-ARXIV-2606-26300:start -->
At `books/part-06-ai-infrastructure/66-evaluation-system.md#L136`, the current owner already establishes the base responsibility for 把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态; `books/part-06-ai-infrastructure/59-model-registry.md#L118` only consumes the handoff. It does not yet state `Verification Horizon formulation for coding-agent rewards`.
<!-- existing:SF-2026-ARXIV-2606-26300:end -->

<!-- delta:SF-2026-ARXIV-2606-26300:start -->
`Verification Horizon formulation for coding-agent rewards` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-26300:end -->

<!-- books-review:SF-2026-ARXIV-2606-26300:start -->
Direct Evolution; Integrate. `No universal reward verifier; longer horizons and hidden environment state remain` 是 `The Verification Horizon: No Silver Bullet for Coding Agent Rewards` 的 source-specific 反例/局限边界；若运行条件离开 `Reward-verification experiments across coding horizons` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-26300:end -->

<!-- existing:SF-2026-ARXIV-2606-26341:start -->
At `books/part-06-ai-infrastructure/63-gpu-scheduler.md#L141`, the current owner already establishes the base responsibility for 把异构问题批处理与 GPU 执行配置作为调度状态，而非模型内部细节; `books/part-06-ai-infrastructure/64-volcano.md#L44` only consumes the handoff. It does not yet state `Many Problems One GPU batching and nonlinear-optimization execution design`.
<!-- existing:SF-2026-ARXIV-2606-26341:end -->

<!-- delta:SF-2026-ARXIV-2606-26341:start -->
`Many Problems One GPU batching and nonlinear-optimization execution design` 所定义的源特定机制用于把异构问题批处理与 GPU 执行配置作为调度状态，而非模型内部细节；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-26341:end -->

<!-- books-review:SF-2026-ARXIV-2606-26341:start -->
Direct Evolution; Integrate. `Only disclosed nonlinear solvers/problem shapes; no cluster-level scheduling or isolation proof` 是 `Scaling Nonlinear Optimization: Many Problems One GPU` 的 source-specific 反例/局限边界；若运行条件离开 `GPU scaling experiments across problem families` 的验证域，`PLATFORM-GPU-SCHEDULER` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-26341:end -->

<!-- existing:SF-2026-ARXIV-2606-26344:start -->
At `books/part-05-inference-system/49-tensorrt-llm.md#L630`, the current owner already establishes the base responsibility for 以可验证搜索或 profiling 反馈驱动 kernel 选择，同时保留确定性正确性路径; `books/part-05-inference-system/48-speculative-decoding.md#L113` only consumes the handoff. It does not yet state `Axon synthesizing superoptimizer; tensor-program search and verification`.
<!-- existing:SF-2026-ARXIV-2606-26344:end -->

<!-- delta:SF-2026-ARXIV-2606-26344:start -->
`Axon synthesizing superoptimizer; tensor-program search and verification` 所定义的源特定机制用于以可验证搜索或 profiling 反馈驱动 kernel 选择，同时保留确定性正确性路径；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-26344:end -->

<!-- books-review:SF-2026-ARXIV-2606-26344:start -->
Direct Evolution; Integrate. `Covered tensor operators/hardware only; verifier does not prove arbitrary numerical equivalence` 是 `Axon: A Synthesizing Superoptimizer for Tensor Programs` 的 source-specific 反例/局限边界；若运行条件离开 `Kernel synthesis evaluation and generated-program performance` 的验证域，`INFER-TENSORRT-LLM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-26344:end -->

<!-- existing:SF-2026-ARXIV-2606-26356:start -->
At `books/part-07-agent/74-prompt.md#L46`, the current owner already establishes the base responsibility for 把模块间指令干扰作为可测试的组合边界，而非默认隔离; `books/part-07-agent/75-context.md#L308` only consumes the handoff. It does not yet state `Instruction Bleed formulation; prompt-composed module interference`.
<!-- existing:SF-2026-ARXIV-2606-26356:end -->

<!-- delta:SF-2026-ARXIV-2606-26356:start -->
`Instruction Bleed formulation; prompt-composed module interference` 所定义的源特定机制用于把模块间指令干扰作为可测试的组合边界，而非默认隔离；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-26356:end -->

<!-- books-review:SF-2026-ARXIV-2606-26356:start -->
Direct Evolution; Integrate. `Prompt/module families tested do not establish universal isolation or adversarial robustness` 是 `Instruction Bleed: Cross-Module Interference in Prompt-Composed Agentic Systems` 的 source-specific 反例/局限边界；若运行条件离开 `Cross-module interference experiments and mitigations` 的验证域，`AGENT-PROMPT` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-26356:end -->

<!-- existing:SF-2026-ARXIV-2606-26377:start -->
At `books/part-06-ai-infrastructure/72-security.md#L204`, the current owner already establishes the base responsibility for 把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界; `books/part-06-ai-infrastructure/71-multi-tenant.md#L33` only consumes the handoff. It does not yet state `Unified intent-and-harm verification defense`.
<!-- existing:SF-2026-ARXIV-2606-26377:end -->

<!-- delta:SF-2026-ARXIV-2606-26377:start -->
`Unified intent-and-harm verification defense` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-26377:end -->

<!-- books-review:SF-2026-ARXIV-2606-26377:start -->
Direct Evolution; Integrate. `Evaluated threat families and judges only; intent inference is not proof of harmless execution` 是 `Verifying Intent and Harm: A Unified Defense Against LLM-Generated Threats` 的 source-specific 反例/局限边界；若运行条件离开 `Threat-generation and defense evaluation` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-26377:end -->

<!-- existing:SF-2026-ARXIV-2606-26383:start -->
At `books/part-06-ai-infrastructure/67-monitoring.md#L18`, the current owner already establishes the base responsibility for 以校准后的硬件与 workload 参数分解性能上界和瓶颈; `books/part-06-ai-infrastructure/68-logging.md#L16` only consumes the handoff. It does not yet state `SOLAR speed-of-light performance model; bottleneck decomposition and bound calculation`.
<!-- existing:SF-2026-ARXIV-2606-26383:end -->

<!-- delta:SF-2026-ARXIV-2606-26383:start -->
`SOLAR speed-of-light performance model; bottleneck decomposition and bound calculation` 所定义的源特定机制用于以校准后的硬件与 workload 参数分解性能上界和瓶颈；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-26383:end -->

<!-- books-review:SF-2026-ARXIV-2606-26383:start -->
Direct Evolution; Integrate. `Analytical bounds depend on calibrated hardware/workload parameters and omit undisclosed runtime effects` 是 `SOLAR: AI-Powered Speed-of-Light Performance Analysis` 的 source-specific 反例/局限边界；若运行条件离开 `Predicted-vs-observed latency and throughput analysis` 的验证域，`PLATFORM-MONITORING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-26383:end -->

<!-- existing:SF-2026-ARXIV-2606-26429:start -->
At `books/part-06-ai-infrastructure/66-evaluation-system.md#L136`, the current owner already establishes the base responsibility for 把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态; `books/part-06-ai-infrastructure/59-model-registry.md#L118` only consumes the handoff. It does not yet state `DualEval joint model-item calibration`.
<!-- existing:SF-2026-ARXIV-2606-26429:end -->

<!-- delta:SF-2026-ARXIV-2606-26429:start -->
`DualEval joint model-item calibration` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-26429:end -->

<!-- books-review:SF-2026-ARXIV-2606-26429:start -->
Direct Evolution; Integrate. `Joint calibration assumes the evaluated item/model pool; new distributions require refitting` 是 `DualEval: Joint Model-Item Calibration for Unified LLM Evaluation` 的 source-specific 反例/局限边界；若运行条件离开 `Unified LLM evaluation experiments and calibration analysis` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-26429:end -->

<!-- existing:SF-2026-ARXIV-2606-26439:start -->
At `books/part-07-agent/76-rag.md#L51`, the current owner already establishes the base responsibility for 把检索索引、量化、GPU scorer 与更新一致性拆成显式数据面状态; `books/part-07-agent/77-memory.md#L113` only consumes the handoff. It does not yet state `TileMaxSim IO-aware GPU MaxSim scoring; dimension tiling and fused product quantization`.
<!-- existing:SF-2026-ARXIV-2606-26439:end -->

<!-- delta:SF-2026-ARXIV-2606-26439:start -->
`TileMaxSim IO-aware GPU MaxSim scoring; dimension tiling and fused product quantization` 所定义的源特定机制用于把检索索引、量化、GPU scorer 与更新一致性拆成显式数据面状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-26439:end -->

<!-- books-review:SF-2026-ARXIV-2606-26439:start -->
Direct Evolution; Integrate. `Evaluated MaxSim layouts and GPUs only; index update and distributed consistency are not proved` 是 `TileMaxSim: IO-Aware GPU MaxSim Scoring with Dimension Tiling and Fused Product Quantization` 的 source-specific 反例/局限边界；若运行条件离开 `GPU retrieval throughput, latency and quality evaluation` 的验证域，`AGENT-RAG` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-26439:end -->

<!-- existing:SF-2026-ARXIV-2606-26441:start -->
At `books/part-07-agent/76-rag.md#L51`, the current owner already establishes the base responsibility for 把检索索引、量化、GPU scorer 与更新一致性拆成显式数据面状态; `books/part-07-agent/77-memory.md#L113` only consumes the handoff. It does not yet state `GPUSparse learned sparse retrieval with parallel inverted indices`.
<!-- existing:SF-2026-ARXIV-2606-26441:end -->

<!-- delta:SF-2026-ARXIV-2606-26441:start -->
`GPUSparse learned sparse retrieval with parallel inverted indices` 所定义的源特定机制用于把检索索引、量化、GPU scorer 与更新一致性拆成显式数据面状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-26441:end -->

<!-- books-review:SF-2026-ARXIV-2606-26441:start -->
Direct Evolution; Integrate. `Static benchmark indexes do not prove high-churn update cost, multi-tenant isolation or cross-node scaling` 是 `GPUSparse: GPU-Accelerated Learned Sparse Retrieval with Parallel Inverted Indices` 的 source-specific 反例/局限边界；若运行条件离开 `Retrieval quality, latency and GPU scaling experiments` 的验证域，`AGENT-RAG` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-26441:end -->

<!-- existing:SF-2026-ARXIV-2606-26442:start -->
At `books/part-07-agent/81-workflow.md#L36`, the current owner already establishes the base responsibility for 把执行 harness、远端 utility 与 artifact handoff 变成可观测工作流状态; `books/part-07-agent/78-tool-calling.md#L37` only consumes the handoff. It does not yet state `AXLE cloud infrastructure for Lean 4 utilities; remote execution and artifact handling`.
<!-- existing:SF-2026-ARXIV-2606-26442:end -->

<!-- delta:SF-2026-ARXIV-2606-26442:start -->
`AXLE cloud infrastructure for Lean 4 utilities; remote execution and artifact handling` 所定义的源特定机制用于把执行 harness、远端 utility 与 artifact handoff 变成可观测工作流状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-26442:end -->

<!-- books-review:SF-2026-ARXIV-2606-26442:start -->
Direct Evolution; Integrate. `Cloud utility success does not prove generated theorem correctness beyond Lean checking or side-effect safety` 是 `AXLE: A Cloud Infrastructure for Lean 4 Theorem Proving Utilities` 的 source-specific 反例/局限边界；若运行条件离开 `Utility execution, throughput and theorem-proving workflow evaluation` 的验证域，`AGENT-WORKFLOW` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-26442:end -->

<!-- existing:SF-2026-ARXIV-2606-26449:start -->
At `books/part-06-ai-infrastructure/69-trace.md#L33`, the current owner already establishes the base responsibility for 让证据生产者写入 provenance 链，消费者据此追踪而不把来源等同于真值; `books/part-06-ai-infrastructure/68-logging.md#L66` only consumes the handoff. It does not yet state `ProvenAI provenance-native trace schema and evidence links`.
<!-- existing:SF-2026-ARXIV-2606-26449:end -->

<!-- delta:SF-2026-ARXIV-2606-26449:start -->
`ProvenAI provenance-native trace schema and evidence links` 所定义的源特定机制用于让证据生产者写入 provenance 链，消费者据此追踪而不把来源等同于真值；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-26449:end -->

<!-- books-review:SF-2026-ARXIV-2606-26449:start -->
Direct Evolution; Integrate. `Trace completeness depends on instrumented producers; provenance does not imply source truth` 是 `ProvenAI: Provenance-Native Traces of Evidence in Generated Answers` 的 source-specific 反例/局限边界；若运行条件离开 `Generated-answer trace/evidence evaluation` 的验证域，`PLATFORM-TRACE` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-26449:end -->

<!-- existing:SF-2026-ARXIV-2606-26453:start -->
At `books/part-05-inference-system/49-tensorrt-llm.md#L630`, the current owner already establishes the base responsibility for 以可验证搜索或 profiling 反馈驱动 kernel 选择，同时保留确定性正确性路径; `books/part-05-inference-system/48-speculative-decoding.md#L113` only consumes the handoff. It does not yet state `Micro-profiling tools as expert surrogates for LLM CUDA optimization`.
<!-- existing:SF-2026-ARXIV-2606-26453:end -->

<!-- delta:SF-2026-ARXIV-2606-26453:start -->
`Micro-profiling tools as expert surrogates for LLM CUDA optimization` 所定义的源特定机制用于以可验证搜索或 profiling 反馈驱动 kernel 选择，同时保留确定性正确性路径；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-26453:end -->

<!-- books-review:SF-2026-ARXIV-2606-26453:start -->
Direct Evolution; Integrate. `Evaluated CUDA tasks and toolchain only; profile-guided generation needs deterministic correctness fallback` 是 `Optimizing CUDA like a Human: Micro-Profiling Tools as Expert Surrogates for LLM-Based GPU Kernel Optimization` 的 source-specific 反例/局限边界；若运行条件离开 `Generated-kernel correctness, profiling and speed evaluation` 的验证域，`INFER-TENSORRT-LLM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-26453:end -->

<!-- existing:SF-2026-ARXIV-2606-26456:start -->
At `books/part-06-ai-infrastructure/66-evaluation-system.md#L136`, the current owner already establishes the base responsibility for 把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态; `books/part-06-ai-infrastructure/59-model-registry.md#L118` only consumes the handoff. It does not yet state `Safety-Aware Mutation Testing proposal and interaction-aware mutant model`.
<!-- existing:SF-2026-ARXIV-2606-26456:end -->

<!-- delta:SF-2026-ARXIV-2606-26456:start -->
`Safety-Aware Mutation Testing proposal and interaction-aware mutant model` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-26456:end -->

<!-- books-review:SF-2026-ARXIV-2606-26456:start -->
Direct Evolution; Integrate. `Vision paper: no completed empirical stop-rule validation; ADS component/fault model is provisional` 是 `Towards Safety-Aware Mutation Testing for Autonomous Driving Systems` 的 source-specific 反例/局限边界；若运行条件离开 `Simulation-based ADS testing protocol and proposed adequacy criterion` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-26456:end -->

<!-- existing:SF-2026-ARXIV-2606-26463:start -->
At `books/part-07-agent/79-planning.md#L140`, the current owner already establishes the base responsibility for 以候选扩展或实时 gate 分配规划预算，并在超时或低置信度时回退; `books/part-07-agent/80-reflection.md#L73` only consumes the handoff. It does not yet state `Variable-delay real-time RL; lightweight gate selects state-dependent planning budget`.
<!-- existing:SF-2026-ARXIV-2606-26463:end -->

<!-- delta:SF-2026-ARXIV-2606-26463:start -->
`Variable-delay real-time RL; lightweight gate selects state-dependent planning budget` 所定义的源特定机制用于以候选扩展或实时 gate 分配规划预算，并在超时或低置信度时回退；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-26463:end -->

<!-- books-review:SF-2026-ARXIV-2606-26463:start -->
Direct Evolution; Integrate. `Game planners and timing model do not prove benefit under production tool latency or safety deadlines` 是 `Finding the Time to Think: Learning Planning Budgets in Real-Time RL` 的 source-specific 反例/局限边界；若运行条件离开 `Pac-Man, Tetris, Snake, Speed Hex and Speed Go evaluation` 的验证域，`AGENT-PLANNING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-26463:end -->

<!-- existing:SF-2026-ARXIV-2606-26472:start -->
At `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L97`, the current owner already establishes the base responsibility for 以表征变化分数驱动逐 token KV 驱逐，并保留完整 KV 回退; `books/part-05-inference-system/44-decode.md#L31` only consumes the handoff. It does not yet state `Epiphany score from forward-pass representation change; attention-matrix-free eviction`.
<!-- existing:SF-2026-ARXIV-2606-26472:end -->

<!-- delta:SF-2026-ARXIV-2606-26472:start -->
`Epiphany score from forward-pass representation change; attention-matrix-free eviction` 所定义的源特定机制用于以表征变化分数驱动逐 token KV 驱逐，并保留完整 KV 回退；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-26472:end -->

<!-- books-review:SF-2026-ARXIV-2606-26472:start -->
Direct Evolution; Integrate. `Model/task transfer and representation-score drift are unproved; quality regression requires full-KV fallback` 是 `Epiphany-Aware KV Cache Eviction Without the Attention Matrix` 的 source-specific 反例/局限边界；若运行条件离开 `Long-reasoning cache/quality evaluation and 16x feasible-context claim` 的验证域，`INFER-KV-CACHE` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-26472:end -->

<!-- existing:SF-2026-ARXIV-2606-26479:start -->
At `books/part-06-ai-infrastructure/72-security.md#L204`, the current owner already establishes the base responsibility for 把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界; `books/part-06-ai-infrastructure/71-multi-tenant.md#L33` only consumes the handoff. It does not yet state `Out-of-band prompt-injection defenses organized as reference monitors and integrity policies`.
<!-- existing:SF-2026-ARXIV-2606-26479:end -->

<!-- delta:SF-2026-ARXIV-2606-26479:start -->
`Out-of-band prompt-injection defenses organized as reference monitors and integrity policies` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-26479:end -->

<!-- books-review:SF-2026-ARXIV-2606-26479:start -->
Direct Evolution; Integrate. `Position/evaluation paper; static AgentDojo results do not establish adaptive robustness` 是 `Adaptive Evaluation of Out-of-Band Defenses Against Prompt Injection in LLM Agents` 的 source-specific 反例/局限边界；若运行条件离开 `Adaptive evaluation methodology against policy-aware attackers` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-26479:end -->

<!-- existing:SF-2026-ARXIV-2606-26488:start -->
At `books/part-05-inference-system/54-gpu-memory.md#L186`, the current owner already establishes the base responsibility for 把稀疏、量化或压缩决策绑定到显存预算和质量回退; `books/part-05-inference-system/55-pd-disaggregation.md#L409` only consumes the handoff. It does not yet state `Compression of recursive reasoners across precision, pruning, distillation and attention variants`.
<!-- existing:SF-2026-ARXIV-2606-26488:end -->

<!-- delta:SF-2026-ARXIV-2606-26488:start -->
`Compression of recursive reasoners across precision, pruning, distillation and attention variants` 所定义的源特定机制用于把稀疏、量化或压缩决策绑定到显存预算和质量回退；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-26488:end -->

<!-- books-review:SF-2026-ARXIV-2606-26488:start -->
Direct Evolution; Integrate. `Edge recursive models only; token-level preservation does not imply global-reasoning preservation` 是 `What Survives When You Compress a Recursive Reasoner for the Edge?` 的 source-specific 反例/局限边界；若运行条件离开 `Three tasks and two recursive architectures; local vs puzzle-exact accuracy` 的验证域，`INFER-GPU-MEMORY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-26488:end -->

<!-- existing:SF-2026-ARXIV-2606-26492:start -->
At `books/part-06-ai-infrastructure/66-evaluation-system.md#L136`, the current owner already establishes the base responsibility for 把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态; `books/part-06-ai-infrastructure/59-model-registry.md#L118` only consumes the handoff. It does not yet state `Within-program versus leave-program-out diagnostic design`.
<!-- existing:SF-2026-ARXIV-2606-26492:end -->

<!-- delta:SF-2026-ARXIV-2606-26492:start -->
`Within-program versus leave-program-out diagnostic design` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-26492:end -->

<!-- books-review:SF-2026-ARXIV-2606-26492:start -->
Direct Evolution; Integrate. `Fault-injected programs and studied diagnosers do not prove production root-cause validity` 是 `Evaluation-Strategy Gap in Fault Diagnosis of Deep Learning Programs` 的 source-specific 反例/局限边界；若运行条件离开 `DynFault: 5,542 traces from 38 DL programs; balanced-accuracy gap analysis` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-26492:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260625-COVERAGE-V1 | fresh-context:jun25-v1 | coverage | coverage:SRC-ARXIV:20260625 | — | 510/510 title+abstract; denominator 68; closures 442; route-negative 127/127 with four promoted FN; 2606.25601 false-positive closed before freeze | passed |
| SA-20260625-EVIDENCE-V1 | fresh-context:jun25-v1 | evidence | review:SF-2026-ARXIV-2606-25274; review:SF-2026-ARXIV-2606-25285; review:SF-2026-ARXIV-2606-25296; review:SF-2026-ARXIV-2606-25342; review:SF-2026-ARXIV-2606-25349; review:SF-2026-ARXIV-2606-25353; review:SF-2026-ARXIV-2606-25366; review:SF-2026-ARXIV-2606-25371; review:SF-2026-ARXIV-2606-25388; review:SF-2026-ARXIV-2606-25410; review:SF-2026-ARXIV-2606-25426; review:SF-2026-ARXIV-2606-25447; review:SF-2026-ARXIV-2606-25449; review:SF-2026-ARXIV-2606-25453; review:SF-2026-ARXIV-2606-25467; review:SF-2026-ARXIV-2606-25487; review:SF-2026-ARXIV-2606-25514; review:SF-2026-ARXIV-2606-25519; review:SF-2026-ARXIV-2606-25532; review:SF-2026-ARXIV-2606-25548; review:SF-2026-ARXIV-2606-25575; review:SF-2026-ARXIV-2606-25592; review:SF-2026-ARXIV-2606-25605; review:SF-2026-ARXIV-2606-25608; review:SF-2026-ARXIV-2606-25622; review:SF-2026-ARXIV-2606-25656; review:SF-2026-ARXIV-2606-25658; review:SF-2026-ARXIV-2606-25674; review:SF-2026-ARXIV-2606-25700; review:SF-2026-ARXIV-2606-25705; review:SF-2026-ARXIV-2606-25721; review:SF-2026-ARXIV-2606-25759; review:SF-2026-ARXIV-2606-25760; review:SF-2026-ARXIV-2606-25782; review:SF-2026-ARXIV-2606-25797; review:SF-2026-ARXIV-2606-25819; review:SF-2026-ARXIV-2606-25838; review:SF-2026-ARXIV-2606-25863; review:SF-2026-ARXIV-2606-25871; review:SF-2026-ARXIV-2606-25987; review:SF-2026-ARXIV-2606-25996; review:SF-2026-ARXIV-2606-26021; review:SF-2026-ARXIV-2606-26027; review:SF-2026-ARXIV-2606-26028; review:SF-2026-ARXIV-2606-26057; review:SF-2026-ARXIV-2606-26071; review:SF-2026-ARXIV-2606-26185; review:SF-2026-ARXIV-2606-26211; review:SF-2026-ARXIV-2606-26257; review:SF-2026-ARXIV-2606-26298; review:SF-2026-ARXIV-2606-26300; review:SF-2026-ARXIV-2606-26341; review:SF-2026-ARXIV-2606-26344; review:SF-2026-ARXIV-2606-26356; review:SF-2026-ARXIV-2606-26377; review:SF-2026-ARXIV-2606-26383; review:SF-2026-ARXIV-2606-26429; review:SF-2026-ARXIV-2606-26439; review:SF-2026-ARXIV-2606-26441; review:SF-2026-ARXIV-2606-26442; review:SF-2026-ARXIV-2606-26449; review:SF-2026-ARXIV-2606-26453; review:SF-2026-ARXIV-2606-26456; review:SF-2026-ARXIV-2606-26463; review:SF-2026-ARXIV-2606-26472; review:SF-2026-ARXIV-2606-26479; review:SF-2026-ARXIV-2606-26488; review:SF-2026-ARXIV-2606-26492 | — | 68/68 exact-v1 full texts; source-specific Method/Evaluation/counterevidence/artifact locators and ten-field contracts | passed |
| SA-20260625-SELECTION-V1 | fresh-context:jun25-v1 | deep_analysis_selection | analysis-decision:SF-2026-ARXIV-2606-25274; analysis-decision:SF-2026-ARXIV-2606-25285; analysis-decision:SF-2026-ARXIV-2606-25296; analysis-decision:SF-2026-ARXIV-2606-25342; analysis-decision:SF-2026-ARXIV-2606-25349; analysis:DA-20260625-2606-25353; analysis-decision:SF-2026-ARXIV-2606-25366; analysis-decision:SF-2026-ARXIV-2606-25371; analysis-decision:SF-2026-ARXIV-2606-25388; analysis-decision:SF-2026-ARXIV-2606-25410; analysis-decision:SF-2026-ARXIV-2606-25426; analysis-decision:SF-2026-ARXIV-2606-25447; analysis-decision:SF-2026-ARXIV-2606-25449; analysis-decision:SF-2026-ARXIV-2606-25453; analysis-decision:SF-2026-ARXIV-2606-25467; analysis-decision:SF-2026-ARXIV-2606-25487; analysis-decision:SF-2026-ARXIV-2606-25514; analysis-decision:SF-2026-ARXIV-2606-25519; analysis-decision:SF-2026-ARXIV-2606-25532; analysis-decision:SF-2026-ARXIV-2606-25548; analysis-decision:SF-2026-ARXIV-2606-25575; analysis-decision:SF-2026-ARXIV-2606-25592; analysis-decision:SF-2026-ARXIV-2606-25605; analysis-decision:SF-2026-ARXIV-2606-25608; analysis-decision:SF-2026-ARXIV-2606-25622; analysis-decision:SF-2026-ARXIV-2606-25656; analysis-decision:SF-2026-ARXIV-2606-25658; analysis-decision:SF-2026-ARXIV-2606-25674; analysis-decision:SF-2026-ARXIV-2606-25700; analysis-decision:SF-2026-ARXIV-2606-25705; analysis-decision:SF-2026-ARXIV-2606-25721; analysis-decision:SF-2026-ARXIV-2606-25759; analysis-decision:SF-2026-ARXIV-2606-25760; analysis-decision:SF-2026-ARXIV-2606-25782; analysis-decision:SF-2026-ARXIV-2606-25797; analysis:DA-20260625-2606-25819; analysis-decision:SF-2026-ARXIV-2606-25838; analysis-decision:SF-2026-ARXIV-2606-25863; analysis-decision:SF-2026-ARXIV-2606-25871; analysis-decision:SF-2026-ARXIV-2606-25987; analysis-decision:SF-2026-ARXIV-2606-25996; analysis-decision:SF-2026-ARXIV-2606-26021; analysis-decision:SF-2026-ARXIV-2606-26027; analysis-decision:SF-2026-ARXIV-2606-26028; analysis:DA-20260625-2606-26057; analysis-decision:SF-2026-ARXIV-2606-26071; analysis-decision:SF-2026-ARXIV-2606-26185; analysis-decision:SF-2026-ARXIV-2606-26211; analysis-decision:SF-2026-ARXIV-2606-26257; analysis-decision:SF-2026-ARXIV-2606-26298; analysis-decision:SF-2026-ARXIV-2606-26300; analysis-decision:SF-2026-ARXIV-2606-26341; analysis-decision:SF-2026-ARXIV-2606-26344; analysis-decision:SF-2026-ARXIV-2606-26356; analysis-decision:SF-2026-ARXIV-2606-26377; analysis-decision:SF-2026-ARXIV-2606-26383; analysis-decision:SF-2026-ARXIV-2606-26429; analysis-decision:SF-2026-ARXIV-2606-26439; analysis-decision:SF-2026-ARXIV-2606-26441; analysis-decision:SF-2026-ARXIV-2606-26442; analysis-decision:SF-2026-ARXIV-2606-26449; analysis-decision:SF-2026-ARXIV-2606-26453; analysis-decision:SF-2026-ARXIV-2606-26456; analysis-decision:SF-2026-ARXIV-2606-26463; analysis-decision:SF-2026-ARXIV-2606-26472; analysis-decision:SF-2026-ARXIV-2606-26479; analysis-decision:SF-2026-ARXIV-2606-26488; analysis-decision:SF-2026-ARXIV-2606-26492 | — | Full 68/68 frontier rerun after Evidence; three winners frozen and 65 bounded non-selections | passed |
| SA-20260625-BOOKS-POSTWRITE-V1 | fresh-context:jun25-postwrite-v1 | books | books-review:SF-2026-ARXIV-2606-25274; books-review:SF-2026-ARXIV-2606-25285; books-review:SF-2026-ARXIV-2606-25296; books-review:SF-2026-ARXIV-2606-25342; books-review:SF-2026-ARXIV-2606-25349; books-review:SF-2026-ARXIV-2606-25353; books-review:SF-2026-ARXIV-2606-25366; books-review:SF-2026-ARXIV-2606-25371; books-review:SF-2026-ARXIV-2606-25388; books-review:SF-2026-ARXIV-2606-25410; books-review:SF-2026-ARXIV-2606-25426; books-review:SF-2026-ARXIV-2606-25447; books-review:SF-2026-ARXIV-2606-25449; books-review:SF-2026-ARXIV-2606-25453; books-review:SF-2026-ARXIV-2606-25467; books-review:SF-2026-ARXIV-2606-25487; books-review:SF-2026-ARXIV-2606-25514; books-review:SF-2026-ARXIV-2606-25519; books-review:SF-2026-ARXIV-2606-25532; books-review:SF-2026-ARXIV-2606-25548; books-review:SF-2026-ARXIV-2606-25575; books-review:SF-2026-ARXIV-2606-25592; books-review:SF-2026-ARXIV-2606-25605; books-review:SF-2026-ARXIV-2606-25608; books-review:SF-2026-ARXIV-2606-25622; books-review:SF-2026-ARXIV-2606-25656; books-review:SF-2026-ARXIV-2606-25658; books-review:SF-2026-ARXIV-2606-25674; books-review:SF-2026-ARXIV-2606-25700; books-review:SF-2026-ARXIV-2606-25705; books-review:SF-2026-ARXIV-2606-25721; books-review:SF-2026-ARXIV-2606-25759; books-review:SF-2026-ARXIV-2606-25760; books-review:SF-2026-ARXIV-2606-25782; books-review:SF-2026-ARXIV-2606-25797; books-review:SF-2026-ARXIV-2606-25819; books-review:SF-2026-ARXIV-2606-25838; books-review:SF-2026-ARXIV-2606-25863; books-review:SF-2026-ARXIV-2606-25871; books-review:SF-2026-ARXIV-2606-25987; books-review:SF-2026-ARXIV-2606-25996; books-review:SF-2026-ARXIV-2606-26021; books-review:SF-2026-ARXIV-2606-26027; books-review:SF-2026-ARXIV-2606-26028; books-review:SF-2026-ARXIV-2606-26057; books-review:SF-2026-ARXIV-2606-26071; books-review:SF-2026-ARXIV-2606-26185; books-review:SF-2026-ARXIV-2606-26211; books-review:SF-2026-ARXIV-2606-26257; books-review:SF-2026-ARXIV-2606-26298; books-review:SF-2026-ARXIV-2606-26300; books-review:SF-2026-ARXIV-2606-26341; books-review:SF-2026-ARXIV-2606-26344; books-review:SF-2026-ARXIV-2606-26356; books-review:SF-2026-ARXIV-2606-26377; books-review:SF-2026-ARXIV-2606-26383; books-review:SF-2026-ARXIV-2606-26429; books-review:SF-2026-ARXIV-2606-26439; books-review:SF-2026-ARXIV-2606-26441; books-review:SF-2026-ARXIV-2606-26442; books-review:SF-2026-ARXIV-2606-26449; books-review:SF-2026-ARXIV-2606-26453; books-review:SF-2026-ARXIV-2606-26456; books-review:SF-2026-ARXIV-2606-26463; books-review:SF-2026-ARXIV-2606-26472; books-review:SF-2026-ARXIV-2606-26479; books-review:SF-2026-ARXIV-2606-26488; books-review:SF-2026-ARXIV-2606-26492 | — | Prewrite comparison passed; then 63/63 Integrate unique-owner body and exact-v1 Review note plus 5/5 No Change absence/handoff revalidation passed; `../_sources/daily-20260625/POST_WRITE_FRESH_AUDIT_V1.md` | passed |

## 8. Ignored Noise

The 442 family-specific closures remain row-addressable in `denominator-full-semantic-audit-v1.tsv`; keyword routing was recall-only and all 127 route-negative identities were audited.

### Materials and Access

- 68/68 retained families completed official exact-v1 primary-source review. Official arXiv HTML was used except `2606.25863v1`, whose exact-v1 official PDF was the recorded fallback; no abstract-text anchor was used.

## 9. Recommended Action

- Final Books disposition: 63 Integrate across 25 unique owner files; 5 No Change handoffs.
- Books Gate passed after the 68/68 post-write fresh audit.
- Preserve the frozen denominator and reopen only when versioned primary evidence changes a recorded mechanism, owner, evaluation contract or non-proof boundary.

## 10. Repository Changes

- The accepted 63-family writeback remains in 25 shared Books owner files; this canonical migration changed only the 2026-06-25 Daily, its date-local packet and date-specific validation scripts.
- `docs/LEARNING_STATE.md` and monthly indexes remained read-only.

## 11. Open Questions

- Which exact-v1 mechanisms remain stable under unseen workloads is future research, not an unresolved Gate finding.
- Which runtime calibration values remain stable after model, hardware or workload distribution changes is a research continuation, not an unresolved Gate finding.

## 12. Sources

- [UC-Search: Risk-Aware Test-Time Search for Delayed Constrained Time-Series Control](https://arxiv.org/abs/2606.25274v1) — first-public（Asia/Shanghai）：2026-06-24；accessed：2026-08-29
- [EPTS: Elastic Post-Training Sparsity for Efficient Large Language Model Compression](https://arxiv.org/abs/2606.25285v1) — first-public（Asia/Shanghai）：2026-06-24；accessed：2026-08-29
- [SafeGen: LLM-Driven Assertion Generation and Fault Criticality Evaluation for Functional Safety](https://arxiv.org/abs/2606.25296v1) — first-public（Asia/Shanghai）：2026-06-24；accessed：2026-08-29
- [Lifelong In-Context Learning with Transformers Requires Parametric Forms of Attention](https://arxiv.org/abs/2606.25342v1) — first-public（Asia/Shanghai）：2026-06-24；accessed：2026-08-29
- [General Techniques for Reducing Key-Switching Overhead in Privacy-Preserving Two-Party Transformer Inference](https://arxiv.org/abs/2606.25349v1) — first-public（Asia/Shanghai）：2026-06-24；accessed：2026-08-29
- [Cache-Resident LLM Inference in GB-Scale Last-Level Caches](https://arxiv.org/abs/2606.25353v1) — first-public（Asia/Shanghai）：2026-06-24；accessed：2026-08-29
- [Reliability-Asymmetric Spacecraft Autonomy: Co-Designing a Capable Learned GNC Stack with a Verified, Adaptation-Aware Runtime Shield](https://arxiv.org/abs/2606.25366v1) — first-public（Asia/Shanghai）：2026-06-24；accessed：2026-08-29
- [Conformal Recovery-Deadline Certificates for Runtime Assurance of Adapting Controllers](https://arxiv.org/abs/2606.25371v1) — first-public（Asia/Shanghai）：2026-06-24；accessed：2026-08-29
- [TabClean: Reusable LLM-Synthesized Programs for Tabular Data Cleaning](https://arxiv.org/abs/2606.25388v1) — first-public（Asia/Shanghai）：2026-06-24；accessed：2026-08-29
- [DFMU: Data-Frugal Machine Unlearning](https://arxiv.org/abs/2606.25410v1) — first-public（Asia/Shanghai）：2026-06-24；accessed：2026-08-29
- [Above the Inner Loop: Exceeding Accelerate at LLM Prefill GEMM on the M1 AMX](https://arxiv.org/abs/2606.25426v1) — first-public（Asia/Shanghai）：2026-06-24；accessed：2026-08-29
- [The Interplay of Harness Design and Post-Training in LLM Agents](https://arxiv.org/abs/2606.25447v1) — first-public（Asia/Shanghai）：2026-06-24；accessed：2026-08-29
- [Reclaim Evaluation: A Lossy Memory Is Worse Than an Empty One](https://arxiv.org/abs/2606.25449v1) — first-public（Asia/Shanghai）：2026-06-24；accessed：2026-08-29
- [EmuGEMM: Fused Tensor Core Kernels for Precision Emulation in Matrix Multiplication](https://arxiv.org/abs/2606.25453v1) — first-public（Asia/Shanghai）：2026-06-24；accessed：2026-08-29
- [RQ-SAFE: Coupled Request-Resource Scheduling for Online Edge SFC-DAGs](https://arxiv.org/abs/2606.25467v1) — first-public（Asia/Shanghai）：2026-06-24；accessed：2026-08-29
- [How Reliable Is Your Jailbreak Judge? Calibration and Adversarial Robustness of Automated ASR Scoring](https://arxiv.org/abs/2606.25487v1) — first-public（Asia/Shanghai）：2026-06-24；accessed：2026-08-29
- [Unlocking Model Potentials Through Adaptive Multi-Agent Scaffolding for Efficient Issue Resolution](https://arxiv.org/abs/2606.25514v1) — first-public（Asia/Shanghai）：2026-06-24；accessed：2026-08-29
- [Quantization Inflates Reasoning: Token Inflation as a Hidden Cost of Low-Bit Reasoning Models](https://arxiv.org/abs/2606.25519v1) — first-public（Asia/Shanghai）：2026-06-24；accessed：2026-08-29
- [Agentic evolution of physically constrained foundation models](https://arxiv.org/abs/2606.25532v1) — first-public（Asia/Shanghai）：2026-06-24；accessed：2026-08-29
- [Concept Removal for Frontier Image Generative Models](https://arxiv.org/abs/2606.25548v1) — first-public（Asia/Shanghai）：2026-06-24；accessed：2026-08-29
- [One Body, Two Minds: Variable Autonomy Approach for a Co-embodied Robotic Hand](https://arxiv.org/abs/2606.25575v1) — first-public（Asia/Shanghai）：2026-06-24；accessed：2026-08-29
- [VPA-Guard: Defending and Benchmarking Image-to-Video Generation Against Visual Prompt Attacks](https://arxiv.org/abs/2606.25592v1) — first-public（Asia/Shanghai）：2026-06-24；accessed：2026-08-29
- [Constraint Tax in Open-Weight LLMs: An Empirical Study of Tool Calling Suppression Under Structured Output Constraints](https://arxiv.org/abs/2606.25605v1) — first-public（Asia/Shanghai）：2026-06-24；accessed：2026-08-29
- [An Approach for a Supporting Multi-LLM System for Automated Certification Based on the German IT-Grundschutz](https://arxiv.org/abs/2606.25608v1) — first-public（Asia/Shanghai）：2026-06-24；accessed：2026-08-29
- [Probabilistic Agents in Deterministic Audits: Evaluating Multi-Agent Systems for Automated Audits Based on the German IT-Grundschutz](https://arxiv.org/abs/2606.25622v1) — first-public（Asia/Shanghai）：2026-06-24；accessed：2026-08-29
- [Is GraphRAG Needed? From Basic RAG to Graph-/Agentic Solutions with Context Optimization](https://arxiv.org/abs/2606.25656v1) — first-public（Asia/Shanghai）：2026-06-24；accessed：2026-08-29
- [Towards a Dynamic and Fixed-budget Memory Bank for Efficient Streaming Video Understanding](https://arxiv.org/abs/2606.25658v1) — first-public（Asia/Shanghai）：2026-06-24；accessed：2026-08-29
- [BitNet Text Embeddings](https://arxiv.org/abs/2606.25674v1) — first-public（Asia/Shanghai）：2026-06-24；accessed：2026-08-29
- [Memory-Efficient Policy Libraries with Low-Rank Adaptation in Reinforcement Learning](https://arxiv.org/abs/2606.25700v1) — first-public（Asia/Shanghai）：2026-06-24；accessed：2026-08-29
- [GUI agent: Guided Exploration of User-Sensitive Screens](https://arxiv.org/abs/2606.25705v1) — first-public（Asia/Shanghai）：2026-06-24；accessed：2026-08-29
- [Tracing Target Answers in Poisoned Retrieval Corpora via Token Influence Attribution](https://arxiv.org/abs/2606.25721v1) — first-public（Asia/Shanghai）：2026-06-24；accessed：2026-08-29
- [NEURON-Fabric: Architecture-Runtime Co-Design for Controlled Low-Bit Gradient Communication](https://arxiv.org/abs/2606.25759v1) — first-public（Asia/Shanghai）：2026-06-24；accessed：2026-08-29
- [Uncertainty Quantification for Computer-Use Agents: A Benchmark across Vision-Language Models and GUI Grounding Datasets](https://arxiv.org/abs/2606.25760v1) — first-public（Asia/Shanghai）：2026-06-24；accessed：2026-08-29
- [Do Encoders Suffice? A Systematic Comparison of Encoder and Decoder Safety Judges for LLM Adversarial Evaluation](https://arxiv.org/abs/2606.25782v1) — first-public（Asia/Shanghai）：2026-06-24；accessed：2026-08-29
- [Confidence Sequences for Online Statistical Model Checking of Markov Decision Processes](https://arxiv.org/abs/2606.25797v1) — first-public（Asia/Shanghai）：2026-06-24；accessed：2026-08-29
- [Beyond Function Calling: Benchmarking Tool-Using Agents under Tool-Environment Unreliability](https://arxiv.org/abs/2606.25819v1) — first-public（Asia/Shanghai）：2026-06-24；accessed：2026-08-29
- [Edges Before Embeddings: A Confidence-Aware Blur Gate for Vision-Language Pipelines](https://arxiv.org/abs/2606.25838v1) — first-public（Asia/Shanghai）：2026-06-24；accessed：2026-08-29
- [Automated Detection of Configuration-Specific Security Vulnerabilities via Patch Analysis](https://arxiv.org/abs/2606.25863v1) — first-public（Asia/Shanghai）：2026-06-24；accessed：2026-08-29
- [AutoRelAnnotator: Calibrated Model Cascades for Cost-Efficient Relevance Evaluation in Sponsored Search](https://arxiv.org/abs/2606.25871v1) — first-public（Asia/Shanghai）：2026-06-24；accessed：2026-08-29
- [Weave of Formal Thought](https://arxiv.org/abs/2606.25987v1) — first-public（Asia/Shanghai）：2026-06-24；accessed：2026-08-29
- [Autodata: An agentic data scientist to create high quality synthetic data](https://arxiv.org/abs/2606.25996v1) — first-public（Asia/Shanghai）：2026-06-24；accessed：2026-08-29
- [Privacy Vulnerabilities of Attention Layers in Tabular Foundation Models and Protection of High-Risk Queries](https://arxiv.org/abs/2606.26021v1) — first-public（Asia/Shanghai）：2026-06-24；accessed：2026-08-29
- [Why Multi-Step Tool-Use Reinforcement Learning Collapses and How Supervisory Signals Fix It](https://arxiv.org/abs/2606.26027v1) — first-public（Asia/Shanghai）：2026-06-24；accessed：2026-08-29
- [Can Trustless Agents Be Trusted? An Empirical Study of the ERC-8004 Decentralized AI Agent Ecosystem](https://arxiv.org/abs/2606.26028v1) — first-public（Asia/Shanghai）：2026-06-24；accessed：2026-08-29
- [The Unfireable Safety Kernel: Execution-Time AI Alignment for AI Agents and Other Escapable AI Systems](https://arxiv.org/abs/2606.26057v1) — first-public（Asia/Shanghai）：2026-06-24；accessed：2026-08-29
- [Model Forensics: Investigating Whether Concerning Behavior Reflects Misalignment](https://arxiv.org/abs/2606.26071v1) — first-public（Asia/Shanghai）：2026-06-24；accessed：2026-08-29
- [Necessary but Not Sufficient: Temperature Control and Reproducibility in LLM-as-Judge Safety Evaluations](https://arxiv.org/abs/2606.26185v1) — first-public（Asia/Shanghai）：2026-06-24；accessed：2026-08-29
- [Data Facts: A Metadata Schema for Structured Data Exchange in the NANDini Multi-Agent Ecosystem](https://arxiv.org/abs/2606.26211v1) — first-public（Asia/Shanghai）：2026-06-24；accessed：2026-08-29
- [Dataset Usage Inference without Shadow Models or Held-out Data](https://arxiv.org/abs/2606.26257v1) — first-public（Asia/Shanghai）：2026-06-24；accessed：2026-08-29
- [Governing Actions, Not Agents: Institutional Attestation as a Governance Model for Autonomous AI Systems](https://arxiv.org/abs/2606.26298v1) — first-public（Asia/Shanghai）：2026-06-24；accessed：2026-08-29
- [The Verification Horizon: No Silver Bullet for Coding Agent Rewards](https://arxiv.org/abs/2606.26300v1) — first-public（Asia/Shanghai）：2026-06-24；accessed：2026-08-29
- [Scaling Nonlinear Optimization: Many Problems One GPU](https://arxiv.org/abs/2606.26341v1) — first-public（Asia/Shanghai）：2026-06-24；accessed：2026-08-29
- [Axon: A Synthesizing Superoptimizer for Tensor Programs](https://arxiv.org/abs/2606.26344v1) — first-public（Asia/Shanghai）：2026-06-24；accessed：2026-08-29
- [Instruction Bleed: Cross-Module Interference in Prompt-Composed Agentic Systems](https://arxiv.org/abs/2606.26356v1) — first-public（Asia/Shanghai）：2026-06-24；accessed：2026-08-29
- [Verifying Intent and Harm: A Unified Defense Against LLM-Generated Threats](https://arxiv.org/abs/2606.26377v1) — first-public（Asia/Shanghai）：2026-06-24；accessed：2026-08-29
- [SOLAR: AI-Powered Speed-of-Light Performance Analysis](https://arxiv.org/abs/2606.26383v1) — first-public（Asia/Shanghai）：2026-06-24；accessed：2026-08-29
- [DualEval: Joint Model-Item Calibration for Unified LLM Evaluation](https://arxiv.org/abs/2606.26429v1) — first-public（Asia/Shanghai）：2026-06-24；accessed：2026-08-29
- [TileMaxSim: IO-Aware GPU MaxSim Scoring with Dimension Tiling and Fused Product Quantization](https://arxiv.org/abs/2606.26439v1) — first-public（Asia/Shanghai）：2026-06-24；accessed：2026-08-29
- [GPUSparse: GPU-Accelerated Learned Sparse Retrieval with Parallel Inverted Indices](https://arxiv.org/abs/2606.26441v1) — first-public（Asia/Shanghai）：2026-06-24；accessed：2026-08-29
- [AXLE: A Cloud Infrastructure for Lean 4 Theorem Proving Utilities](https://arxiv.org/abs/2606.26442v1) — first-public（Asia/Shanghai）：2026-06-24；accessed：2026-08-29
- [ProvenAI: Provenance-Native Traces of Evidence in Generated Answers](https://arxiv.org/abs/2606.26449v1) — first-public（Asia/Shanghai）：2026-06-24；accessed：2026-08-29
- [Optimizing CUDA like a Human: Micro-Profiling Tools as Expert Surrogates for LLM-Based GPU Kernel Optimization](https://arxiv.org/abs/2606.26453v1) — first-public（Asia/Shanghai）：2026-06-24；accessed：2026-08-29
- [Towards Safety-Aware Mutation Testing for Autonomous Driving Systems](https://arxiv.org/abs/2606.26456v1) — first-public（Asia/Shanghai）：2026-06-24；accessed：2026-08-29
- [Finding the Time to Think: Learning Planning Budgets in Real-Time RL](https://arxiv.org/abs/2606.26463v1) — first-public（Asia/Shanghai）：2026-06-24；accessed：2026-08-29
- [Epiphany-Aware KV Cache Eviction Without the Attention Matrix](https://arxiv.org/abs/2606.26472v1) — first-public（Asia/Shanghai）：2026-06-24；accessed：2026-08-29
- [Adaptive Evaluation of Out-of-Band Defenses Against Prompt Injection in LLM Agents](https://arxiv.org/abs/2606.26479v1) — first-public（Asia/Shanghai）：2026-06-24；accessed：2026-08-29
- [What Survives When You Compress a Recursive Reasoner for the Edge?](https://arxiv.org/abs/2606.26488v1) — first-public（Asia/Shanghai）：2026-06-24；accessed：2026-08-29
- [Evaluation-Strategy Gap in Fault Diagnosis of Deep Learning Programs](https://arxiv.org/abs/2606.26492v1) — first-public（Asia/Shanghai）：2026-06-24；accessed：2026-08-29
- [Research Sources Registry](../../../../docs/RESEARCH_SOURCES.md) — source roles、cadence 与 evidence scope 的权威注册表
- Date-local receipts：`../_sources/daily-20260625/source-review-receipts-v2.1.json`、`deep-analysis-selection-v1.json`、`books-comparison-v1.json`、`POST_WRITE_FRESH_AUDIT_V1.md`

## 13. Final Status

Daily V2.1 的 Coverage=`Closed`、Evidence=`Passed`、Books=`Passed`；Completion Status=`Complete`；unresolved findings: `0`。机器校验只证明接口一致，语义结论仍由第 7 节记录的 fresh-context audit 承担。
