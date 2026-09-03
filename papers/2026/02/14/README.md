# Daily Research — 2026-02-14

**Research Date:** 2026-02-14

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-02-13 09:00:00 ～ 2026-02-14 09:00:00（Asia/Shanghai，左闭右开）

**Contract:** V2.1 Historical Daily independent Full Replay；既有 Weekly 未参与 discovery、分母、评分、Review、Books 判断或漏项校准；Weekly dependency=0。

**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed；全月 fresh-context 四域语义审计已通过（`papers/2026/02/_sources/february-fresh-context-audit.json`），本日 unresolved findings=0。

## Executive Summary

窗口 raw identities=628，title+abstract semantic screening=628/628；Candidate Denominator=32，pre-denominator closures=596。exact-v1 Review=32/32，withdrawn=0，blocked=0；Books Integrate=3。

本日报以官方 arXiv 公告时刻映射北京时间半开窗口；DataCite 只恢复 identity 与 registry timestamp，不把 Submitted:v1、DOI created 或后续 revision 误当作报告归属。withdrawn family 只保留在 pre-denominator closure，不进入候选、评分、Review 或 Books。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-02-14 |
| Window End | 2026-02-14 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | sha256:e1281801674c07779ab93562c4e45b47839dbcd1a43ec751939301e45936bfa1 |
| Denominator Frozen At | 2026-09-03T07:01:18Z |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-02-13T09:00:00+08:00 | 2026-02-14T09:00:00+08:00 | 2026-09-03T07:01:18Z | DataCite identity recovery + official arXiv announcement schedule + registered-category full title/abstract screen + exact-v1 HTML/PDF | checked | 32 | SF-2026-ARXIV-2602-11882; SF-2026-ARXIV-2602-11291; SF-2026-ARXIV-2602-11301; SF-2026-ARXIV-2602-11327; SF-2026-ARXIV-2602-11521; SF-2026-ARXIV-2602-11530; SF-2026-ARXIV-2602-11543; SF-2026-ARXIV-2602-11688; SF-2026-ARXIV-2602-11790; SF-2026-ARXIV-2602-12029; SF-2026-ARXIV-2602-12151; SF-2026-ARXIV-2602-11184; SF-2026-ARXIV-2602-11192; SF-2026-ARXIV-2602-11224; SF-2026-ARXIV-2602-11287; SF-2026-ARXIV-2602-11348; SF-2026-ARXIV-2602-11456; SF-2026-ARXIV-2602-11470; SF-2026-ARXIV-2602-11506; SF-2026-ARXIV-2602-11510; SF-2026-ARXIV-2602-11513; SF-2026-ARXIV-2602-11574; SF-2026-ARXIV-2602-11686; SF-2026-ARXIV-2602-11749; SF-2026-ARXIV-2602-11786; SF-2026-ARXIV-2602-11877; SF-2026-ARXIV-2602-11937; SF-2026-ARXIV-2602-11964; SF-2026-ARXIV-2602-12194; SF-2026-ARXIV-2602-12244; SF-2026-ARXIV-2602-12271; SF-2026-ARXIV-2602-12281 | pages=100; DOI prefixes=00..99; final_cursor=end; screened=628 | 2026-02-14T09:00:00+08:00 | papers/2026/02/_sources/daily-20260214/coverage-receipt.json; papers/2026/02/_sources/daily-20260214/screening-ledger-final.json; coverage:SRC-ARXIV:20260214 | — |

<!-- coverage:SRC-ARXIV:20260214:start -->628 个注册身份均已按 title+abstract 逐项筛选；596 个具体拒绝理由保存在 ledger。当前注册表的其他来源在 2026-08-25 才生效，不反推为 2 月 Required。全月 receipt 已完成 false-positive / false-negative、日期归属与撤稿审计，本日 Coverage Gate=Closed。<!-- coverage:SRC-ARXIV:20260214:end -->

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2602-11882 | arXiv:2602.11882v1 | paper-v1:2602.11882 | 2026-W07 | 2026-02-13 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-11882 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-11882 | no |
| SF-2026-ARXIV-2602-11291 | arXiv:2602.11291v1 | paper-v1:2602.11291 | 2026-W07 | 2026-02-13 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-11291 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-11291 | no |
| SF-2026-ARXIV-2602-11301 | arXiv:2602.11301v1 | paper-v1:2602.11301 | 2026-W07 | 2026-02-13 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-11301 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-11301 | no |
| SF-2026-ARXIV-2602-11327 | arXiv:2602.11327v1 | paper-v1:2602.11327 | 2026-W07 | 2026-02-13 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-11327 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-11327 | no |
| SF-2026-ARXIV-2602-11521 | arXiv:2602.11521v1 | paper-v1:2602.11521 | 2026-W07 | 2026-02-13 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-11521 | self | — | new_in_window | INFER-GPU-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-11521 | no |
| SF-2026-ARXIV-2602-11530 | arXiv:2602.11530v1 | paper-v1:2602.11530 | 2026-W07 | 2026-02-13 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-11530 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-11530 | no |
| SF-2026-ARXIV-2602-11543 | arXiv:2602.11543v1 | paper-v1:2602.11543 | 2026-W07 | 2026-02-13 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-11543 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-11543 | no |
| SF-2026-ARXIV-2602-11688 | arXiv:2602.11688v1 | paper-v1:2602.11688 | 2026-W07 | 2026-02-13 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-11688 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-11688 | no |
| SF-2026-ARXIV-2602-11790 | arXiv:2602.11790v1 | paper-v1:2602.11790 | 2026-W07 | 2026-02-13 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-11790 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-11790 | no |
| SF-2026-ARXIV-2602-12029 | arXiv:2602.12029v1 | paper-v1:2602.12029 | 2026-W07 | 2026-02-13 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-12029 | self | — | new_in_window | INFER-PD-DISAGGREGATION | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-12029 | no |
| SF-2026-ARXIV-2602-12151 | arXiv:2602.12151v1 | paper-v1:2602.12151 | 2026-W07 | 2026-02-13 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-12151 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-12151 | no |
| SF-2026-ARXIV-2602-11184 | arXiv:2602.11184v1 | paper-v1:2602.11184 | 2026-W07 | 2026-02-13 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-11184 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-11184 | no |
| SF-2026-ARXIV-2602-11192 | arXiv:2602.11192v1 | paper-v1:2602.11192 | 2026-W07 | 2026-02-13 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-11192 | self | — | new_in_window | INFER-GPU-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-11192 | no |
| SF-2026-ARXIV-2602-11224 | arXiv:2602.11224v1 | paper-v1:2602.11224 | 2026-W07 | 2026-02-13 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-11224 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-11224 | no |
| SF-2026-ARXIV-2602-11287 | arXiv:2602.11287v1 | paper-v1:2602.11287 | 2026-W07 | 2026-02-13 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-11287 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-11287 | no |
| SF-2026-ARXIV-2602-11348 | arXiv:2602.11348v1 | paper-v1:2602.11348 | 2026-W07 | 2026-02-13 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-11348 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-11348 | no |
| SF-2026-ARXIV-2602-11456 | arXiv:2602.11456v1 | paper-v1:2602.11456 | 2026-W07 | 2026-02-13 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2602-11456 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Integrate | books-review:SF-2026-ARXIV-2602-11456 | no |
| SF-2026-ARXIV-2602-11470 | arXiv:2602.11470v1 | paper-v1:2602.11470 | 2026-W07 | 2026-02-13 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-11470 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-11470 | no |
| SF-2026-ARXIV-2602-11506 | arXiv:2602.11506v1 | paper-v1:2602.11506 | 2026-W07 | 2026-02-13 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-11506 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-11506 | no |
| SF-2026-ARXIV-2602-11510 | arXiv:2602.11510v1 | paper-v1:2602.11510 | 2026-W07 | 2026-02-13 | SRC-ARXIV | 2 | 3 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-11510 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-11510 | no |
| SF-2026-ARXIV-2602-11513 | arXiv:2602.11513v1 | paper-v1:2602.11513 | 2026-W07 | 2026-02-13 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-11513 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-11513 | no |
| SF-2026-ARXIV-2602-11574 | arXiv:2602.11574v1 | paper-v1:2602.11574 | 2026-W07 | 2026-02-13 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-11574 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-11574 | no |
| SF-2026-ARXIV-2602-11686 | arXiv:2602.11686v1 | paper-v1:2602.11686 | 2026-W07 | 2026-02-13 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-11686 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-11686 | no |
| SF-2026-ARXIV-2602-11749 | arXiv:2602.11749v1 | paper-v1:2602.11749 | 2026-W07 | 2026-02-13 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2602-11749 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2602-11749 | no |
| SF-2026-ARXIV-2602-11786 | arXiv:2602.11786v1 | paper-v1:2602.11786 | 2026-W07 | 2026-02-13 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2602-11786 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2602-11786 | no |
| SF-2026-ARXIV-2602-11877 | arXiv:2602.11877v1 | paper-v1:2602.11877 | 2026-W07 | 2026-02-13 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-11877 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-11877 | no |
| SF-2026-ARXIV-2602-11937 | arXiv:2602.11937v1 | paper-v1:2602.11937 | 2026-W07 | 2026-02-13 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-11937 | self | — | new_in_window | MODEL-MOE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-11937 | no |
| SF-2026-ARXIV-2602-11964 | arXiv:2602.11964v1 | paper-v1:2602.11964 | 2026-W07 | 2026-02-13 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-11964 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-11964 | no |
| SF-2026-ARXIV-2602-12194 | arXiv:2602.12194v1 | paper-v1:2602.12194 | 2026-W07 | 2026-02-13 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-12194 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-12194 | no |
| SF-2026-ARXIV-2602-12244 | arXiv:2602.12244v1 | paper-v1:2602.12244 | 2026-W07 | 2026-02-13 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-12244 | self | — | new_in_window | AGENT-PLANNING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-12244 | no |
| SF-2026-ARXIV-2602-12271 | arXiv:2602.12271v1 | paper-v1:2602.12271 | 2026-W07 | 2026-02-13 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-12271 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-12271 | no |
| SF-2026-ARXIV-2602-12281 | arXiv:2602.12281v1 | paper-v1:2602.12281 | 2026-W07 | 2026-02-13 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-12281 | self | — | new_in_window | TRAIN-RLHF | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-12281 | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2602-11882 | RP-f964884a566041b4 | deep | arXiv:2602.11882v1 | SRC-ARXIV@arXiv:2602.11882v1 | arXiv:2602.11882v1 HTML — §Quantization implementation details. [facet=method]; https://arxiv.org/html/2602.11882v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11882v1.html; sha256:07a3799dc9cffd5ff7e4011c22cec72f36be745b118f574462ca9277b68ddc56 | arXiv:2602.11882v1 HTML — §Evaluation protocol. [facet=evaluation]; https://arxiv.org/html/2602.11882v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11882v1.html; sha256:07a3799dc9cffd5ff7e4011c22cec72f36be745b118f574462ca9277b68ddc56 | arXiv:2602.11882v1 HTML — §5 Discussion, Limitations, and Outlook [facet=limitations]; https://arxiv.org/html/2602.11882v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11882v1.html; sha256:07a3799dc9cffd5ff7e4011c22cec72f36be745b118f574462ca9277b68ddc56 | External link observed in exact-v1 body: https://github.com/suraj-ranganath/DINO-MBQuant; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence | claim:SF-2026-ARXIV-2602-11882 | complete |
| SF-2026-ARXIV-2602-11291 | RP-3d4fb38f0f67e8ca | deep | arXiv:2602.11291v1 | SRC-ARXIV@arXiv:2602.11291v1 | arXiv:2602.11291v1 HTML — §4.3 Pipeline for VLA under Hierarchical World Model Guidance [facet=method]; https://arxiv.org/html/2602.11291v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11291v1.html; sha256:48a5c7ac38ffc3367b67a3599e55dc3d02a6141539c1215067794b21dd66849f | arXiv:2602.11291v1 HTML — §5.2 Benchmark and evaluation [facet=evaluation]; https://arxiv.org/html/2602.11291v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11291v1.html; sha256:48a5c7ac38ffc3367b67a3599e55dc3d02a6141539c1215067794b21dd66849f | arXiv:2602.11291v1 HTML — §7 Limitations [facet=limitations]; https://arxiv.org/html/2602.11291v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11291v1.html; sha256:48a5c7ac38ffc3367b67a3599e55dc3d02a6141539c1215067794b21dd66849f | Not Disclosed — arXiv:2602.11291v1 does not disclose a public repository, release, commit, or executable artifact used by this review | claim:SF-2026-ARXIV-2602-11291 | complete |
| SF-2026-ARXIV-2602-11301 | RP-e3116cc7000ada41 | deep | arXiv:2602.11301v1 | SRC-ARXIV@arXiv:2602.11301v1 | arXiv:2602.11301v1 PDF — §3 Architecture Overview: 12-Domain Ecosystem and Minimal Stack [facet=method]; https://arxiv.org/pdf/2602.11301v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11301v1.pdf.txt; sha256:a6e180042a3a33e559db454da6a60ce043a935cc84121247140faea00373e194 | Not Disclosed — exact-v1 PDF 全文已审计但未提供独立 Evaluation 章节 [facet=evaluation]; https://arxiv.org/pdf/2602.11301v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11301v1.pdf.txt; sha256:a6e180042a3a33e559db454da6a60ce043a935cc84121247140faea00373e194 | arXiv:2602.11301v1 PDF — §7 Discussion and Conclusion [facet=limitations]; https://arxiv.org/pdf/2602.11301v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11301v1.pdf.txt; sha256:a6e180042a3a33e559db454da6a60ce043a935cc84121247140faea00373e194 | Not Disclosed — arXiv:2602.11301v1 does not disclose a public repository, release, commit, or executable artifact used by this review | claim:SF-2026-ARXIV-2602-11301 | complete |
| SF-2026-ARXIV-2602-11327 | RP-a9cb48a615042a9c | deep | arXiv:2602.11327v1 | SRC-ARXIV@arXiv:2602.11327v1 | arXiv:2602.11327v1 HTML — §6.1 Assessment Methodology [facet=method]; https://arxiv.org/html/2602.11327v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11327v1.html; sha256:68ad113b187a165024ec13c8e3ccffe820fb2acebc074dcbad484893003a9123 | arXiv:2602.11327v1 HTML — §6.2 Lifecycle-Based Evaluation Framework [facet=evaluation]; https://arxiv.org/html/2602.11327v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11327v1.html; sha256:68ad113b187a165024ec13c8e3ccffe820fb2acebc074dcbad484893003a9123 | arXiv:2602.11327v1 HTML — §4.1.4 Absence of limitations on token lifetime [facet=limitations]; https://arxiv.org/html/2602.11327v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11327v1.html; sha256:68ad113b187a165024ec13c8e3ccffe820fb2acebc074dcbad484893003a9123 | External link observed in exact-v1 body: https://github.com/a2aproject/A2A; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence | claim:SF-2026-ARXIV-2602-11327 | complete |
| SF-2026-ARXIV-2602-11521 | RP-7729435103c2495a | deep | arXiv:2602.11521v1 | SRC-ARXIV@arXiv:2602.11521v1 | arXiv:2602.11521v1 HTML — §4. PAM: System Overview [facet=method]; https://arxiv.org/html/2602.11521v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11521v1.html; sha256:16b46703bc068edd2605bd36dc3626f91b986774eb4f3f09a78209ca30564f34 | arXiv:2602.11521v1 HTML — §7.1. Evaluation Methodology [facet=evaluation]; https://arxiv.org/html/2602.11521v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11521v1.html; sha256:16b46703bc068edd2605bd36dc3626f91b986774eb4f3f09a78209ca30564f34 | arXiv:2602.11521v1 HTML — §3.1. Limitations of Layered PIM [facet=limitations]; https://arxiv.org/html/2602.11521v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11521v1.html; sha256:16b46703bc068edd2605bd36dc3626f91b986774eb4f3f09a78209ca30564f34 | External link observed in exact-v1 body: https://github.com/CMU-SAFARI/ramulator2; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence | claim:SF-2026-ARXIV-2602-11521 | complete |
| SF-2026-ARXIV-2602-11530 | RP-3c0ac817417e7352 | deep | arXiv:2602.11530v1 | SRC-ARXIV@arXiv:2602.11530v1 | arXiv:2602.11530v1 HTML — §III-A Methodology [facet=method]; https://arxiv.org/html/2602.11530v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11530v1.html; sha256:1c9a10530f5f9b52d28ea7115948b767771b423cadaf9847644c5e27ac17186f | arXiv:2602.11530v1 HTML — §V-B User Experience (TTFT, SLO Violation) and Throughput [facet=evaluation]; https://arxiv.org/html/2602.11530v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11530v1.html; sha256:1c9a10530f5f9b52d28ea7115948b767771b423cadaf9847644c5e27ac17186f | arXiv:2602.11530v1 HTML — §VII Future work [facet=limitations]; https://arxiv.org/html/2602.11530v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11530v1.html; sha256:1c9a10530f5f9b52d28ea7115948b767771b423cadaf9847644c5e27ac17186f | External link observed in exact-v1 body: https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence | claim:SF-2026-ARXIV-2602-11530 | complete |
| SF-2026-ARXIV-2602-11543 | RP-d70b8edb1a7f0318 | deep | arXiv:2602.11543v1 | SRC-ARXIV@arXiv:2602.11543v1 | arXiv:2602.11543v1 HTML — §3.2 Overall Framework [facet=method]; https://arxiv.org/html/2602.11543v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11543v1.html; sha256:b66d2c017b09658d80077d4cc01afe674717f7db482ee92ca96156db02830900 | arXiv:2602.11543v1 HTML — §4.2 Main Results [facet=evaluation]; https://arxiv.org/html/2602.11543v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11543v1.html; sha256:b66d2c017b09658d80077d4cc01afe674717f7db482ee92ca96156db02830900 | arXiv:2602.11543v1 HTML — §5 Conclusion [facet=limitations]; https://arxiv.org/html/2602.11543v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11543v1.html; sha256:b66d2c017b09658d80077d4cc01afe674717f7db482ee92ca96156db02830900 | External link observed in exact-v1 body: https://github.com/openlm-research/open_llama; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence | claim:SF-2026-ARXIV-2602-11543 | complete |
| SF-2026-ARXIV-2602-11688 | RP-29646fc2af361026 | deep | arXiv:2602.11688v1 | SRC-ARXIV@arXiv:2602.11688v1 | arXiv:2602.11688v1 HTML — §3.2 Design objective and signal requirements [facet=method]; https://arxiv.org/html/2602.11688v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11688v1.html; sha256:a150b223e1c43847ebf626dc7681666640ab3471b6636acdaf8bd6680bc8f081 | arXiv:2602.11688v1 HTML — §4 Experimental Evaluation [facet=evaluation]; https://arxiv.org/html/2602.11688v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11688v1.html; sha256:a150b223e1c43847ebf626dc7681666640ab3471b6636acdaf8bd6680bc8f081 | arXiv:2602.11688v1 HTML — §Methodological limitations. [facet=limitations]; https://arxiv.org/html/2602.11688v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11688v1.html; sha256:a150b223e1c43847ebf626dc7681666640ab3471b6636acdaf8bd6680bc8f081 | External link observed in exact-v1 body: https://github.com/atoniolo76/gotoni/tree/benchmark-load-balancing; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence | claim:SF-2026-ARXIV-2602-11688 | complete |
| SF-2026-ARXIV-2602-11790 | RP-a0acd752ef60438c | deep | arXiv:2602.11790v1 | SRC-ARXIV@arXiv:2602.11790v1 | arXiv:2602.11790v1 HTML — §4.1. System Overview [facet=method]; https://arxiv.org/html/2602.11790v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11790v1.html; sha256:8a7b73191d979f83f6c4ee72085a1887c48e5853e6c05644892d6e5327145a64 | arXiv:2602.11790v1 HTML — §5.2. Main Results [facet=evaluation]; https://arxiv.org/html/2602.11790v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11790v1.html; sha256:8a7b73191d979f83f6c4ee72085a1887c48e5853e6c05644892d6e5327145a64 | arXiv:2602.11790v1 HTML — §5.4. Error Analysis [facet=limitations]; https://arxiv.org/html/2602.11790v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11790v1.html; sha256:8a7b73191d979f83f6c4ee72085a1887c48e5853e6c05644892d6e5327145a64 | External link observed in exact-v1 body: https://github.com/MiniMax-AI; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence | claim:SF-2026-ARXIV-2602-11790 | complete |
| SF-2026-ARXIV-2602-12029 | RP-f040f7b6d0bfa9f2 | deep | arXiv:2602.12029v1 | SRC-ARXIV@arXiv:2602.12029v1 | arXiv:2602.12029v1 HTML — §3 Method [facet=method]; https://arxiv.org/html/2602.12029v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.12029v1.html; sha256:5dc19e6a7e410b100e9332abeb6c80a792db1ab0133c38cf2a466406b7655d3e | arXiv:2602.12029v1 HTML — §B.3 Results with a different backbone model [facet=evaluation]; https://arxiv.org/html/2602.12029v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.12029v1.html; sha256:5dc19e6a7e410b100e9332abeb6c80a792db1ab0133c38cf2a466406b7655d3e | Not Disclosed — exact-v1 HTML has no independent limitations or counterevidence section; a positive conclusion does not replace that facet [facet=limitations]; https://arxiv.org/html/2602.12029v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.12029v1.html; sha256:5dc19e6a7e410b100e9332abeb6c80a792db1ab0133c38cf2a466406b7655d3e | External link observed in exact-v1 body: https://github.com/langchain-ai/langchain; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence | claim:SF-2026-ARXIV-2602-12029 | complete |
| SF-2026-ARXIV-2602-12151 | RP-9924737e50e71b00 | deep | arXiv:2602.12151v1 | SRC-ARXIV@arXiv:2602.12151v1 | arXiv:2602.12151v1 HTML — §5.4 Algorithm Efficiency [facet=method]; https://arxiv.org/html/2602.12151v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.12151v1.html; sha256:88f25ff2bc397e76fec016e78fc618499fd4389fd16c9e538e62376eb70cb40d | arXiv:2602.12151v1 HTML — §5.3 Case and Ablation Studies [facet=evaluation]; https://arxiv.org/html/2602.12151v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.12151v1.html; sha256:88f25ff2bc397e76fec016e78fc618499fd4389fd16c9e538e62376eb70cb40d | arXiv:2602.12151v1 HTML — §Appendix C Extended Discussion [facet=limitations]; https://arxiv.org/html/2602.12151v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.12151v1.html; sha256:88f25ff2bc397e76fec016e78fc618499fd4389fd16c9e538e62376eb70cb40d | External link observed in exact-v1 body: https://github.com/Azure/AzurePublicDataset; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence | claim:SF-2026-ARXIV-2602-12151 | complete |
| SF-2026-ARXIV-2602-11184 | RP-5b0d19ecef978366 | deep | arXiv:2602.11184v1 | SRC-ARXIV@arXiv:2602.11184v1 | arXiv:2602.11184v1 HTML — §2.2 MoE LLMs Compression Methods [facet=method]; https://arxiv.org/html/2602.11184v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11184v1.html; sha256:75487528350fe2aa0862dd12da635bd67d86a9da082b978c89e7f14748049796 | arXiv:2602.11184v1 HTML — §Main results. [facet=evaluation]; https://arxiv.org/html/2602.11184v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11184v1.html; sha256:75487528350fe2aa0862dd12da635bd67d86a9da082b978c89e7f14748049796 | arXiv:2602.11184v1 HTML — §A.12 Limitations [facet=limitations]; https://arxiv.org/html/2602.11184v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11184v1.html; sha256:75487528350fe2aa0862dd12da635bd67d86a9da082b978c89e7f14748049796 | Not Disclosed — arXiv:2602.11184v1 does not disclose a public repository, release, commit, or executable artifact used by this review | claim:SF-2026-ARXIV-2602-11184 | complete |
| SF-2026-ARXIV-2602-11192 | RP-0b8a4ff439cae78b | deep | arXiv:2602.11192v1 | SRC-ARXIV@arXiv:2602.11192v1 | arXiv:2602.11192v1 HTML — §3 Method [facet=method]; https://arxiv.org/html/2602.11192v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11192v1.html; sha256:3f8aee6bfd89c58483fad702f44a9093dad3b3914c91a05d48d3b4dd5367555a | arXiv:2602.11192v1 HTML — §4.2 Main Results [facet=evaluation]; https://arxiv.org/html/2602.11192v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11192v1.html; sha256:3f8aee6bfd89c58483fad702f44a9093dad3b3914c91a05d48d3b4dd5367555a | arXiv:2602.11192v1 HTML — §5 Conclusion [facet=limitations]; https://arxiv.org/html/2602.11192v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11192v1.html; sha256:3f8aee6bfd89c58483fad702f44a9093dad3b3914c91a05d48d3b4dd5367555a | Not Disclosed — arXiv:2602.11192v1 does not disclose a public repository, release, commit, or executable artifact used by this review | claim:SF-2026-ARXIV-2602-11192 | complete |
| SF-2026-ARXIV-2602-11224 | RP-154f2f9a1713817c | deep | arXiv:2602.11224v1 | SRC-ARXIV@arXiv:2602.11224v1 | arXiv:2602.11224v1 HTML — §3. Agent-Diff [facet=method]; https://arxiv.org/html/2602.11224v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11224v1.html; sha256:7b2a95fb3ff2946545faf754e7d1b36e4ec72d08d22399411c7b261d02096160 | arXiv:2602.11224v1 HTML — §4. Evaluation Methodology [facet=evaluation]; https://arxiv.org/html/2602.11224v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11224v1.html; sha256:7b2a95fb3ff2946545faf754e7d1b36e4ec72d08d22399411c7b261d02096160 | arXiv:2602.11224v1 HTML — §6.3. Failure and Recovery Modes [facet=limitations]; https://arxiv.org/html/2602.11224v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11224v1.html; sha256:7b2a95fb3ff2946545faf754e7d1b36e4ec72d08d22399411c7b261d02096160 | External link observed in exact-v1 body: https://github.com/agent-diff-bench/agent-diff; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence | claim:SF-2026-ARXIV-2602-11224 | complete |
| SF-2026-ARXIV-2602-11287 | RP-fcca4999fcb5cff9 | deep | arXiv:2602.11287v1 | SRC-ARXIV@arXiv:2602.11287v1 | arXiv:2602.11287v1 HTML — §II HiFloat4 [facet=method]; https://arxiv.org/html/2602.11287v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11287v1.html; sha256:36e60d7f92ac43c280a2336b4816e74bef8d02b06646f0b138c3ced6f4261dd5 | arXiv:2602.11287v1 HTML — §IV Language Model Inference with HiFloat4 [facet=evaluation]; https://arxiv.org/html/2602.11287v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11287v1.html; sha256:36e60d7f92ac43c280a2336b4816e74bef8d02b06646f0b138c3ced6f4261dd5 | arXiv:2602.11287v1 HTML — §V Conclusion [facet=limitations]; https://arxiv.org/html/2602.11287v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11287v1.html; sha256:36e60d7f92ac43c280a2336b4816e74bef8d02b06646f0b138c3ced6f4261dd5 | Not Disclosed — arXiv:2602.11287v1 does not disclose a public repository, release, commit, or executable artifact used by this review | claim:SF-2026-ARXIV-2602-11287 | complete |
| SF-2026-ARXIV-2602-11348 | RP-1033dc0ee7bf5d40 | deep | arXiv:2602.11348v1 | SRC-ARXIV@arXiv:2602.11348v1 | arXiv:2602.11348v1 HTML — §2.1 Design Principles [facet=method]; https://arxiv.org/html/2602.11348v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11348v1.html; sha256:5f925e8b2cc0513f02b649b94b7a71672d170dd6bec4ccc8ace794558b018fd4 | arXiv:2602.11348v1 HTML — §A.1 Main Results [facet=evaluation]; https://arxiv.org/html/2602.11348v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11348v1.html; sha256:5f925e8b2cc0513f02b649b94b7a71672d170dd6bec4ccc8ace794558b018fd4 | arXiv:2602.11348v1 HTML — §5 Limitations [facet=limitations]; https://arxiv.org/html/2602.11348v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11348v1.html; sha256:5f925e8b2cc0513f02b649b94b7a71672d170dd6bec4ccc8ace794558b018fd4 | External link observed in exact-v1 body: https://github.com/keven-cyber/agentnoisebench; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence | claim:SF-2026-ARXIV-2602-11348 | complete |
| SF-2026-ARXIV-2602-11456 | RP-adc5e02665ef824c | deep | arXiv:2602.11456v1 | SRC-ARXIV@arXiv:2602.11456v1 | arXiv:2602.11456v1 HTML — §5. System Design [facet=method]; https://arxiv.org/html/2602.11456v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11456v1.html; sha256:2a45fb64933d98b48153d0dcf984e7f894245845e80ef6f894a1857cdcff2632 | arXiv:2602.11456v1 HTML — §7.2. End-to-End Results [facet=evaluation]; https://arxiv.org/html/2602.11456v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11456v1.html; sha256:2a45fb64933d98b48153d0dcf984e7f894245845e80ef6f894a1857cdcff2632 | arXiv:2602.11456v1 HTML — §6. Discussion [facet=limitations]; https://arxiv.org/html/2602.11456v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11456v1.html; sha256:2a45fb64933d98b48153d0dcf984e7f894245845e80ef6f894a1857cdcff2632 | External link observed in exact-v1 body: https://github.com/PrimeIntellect-ai/prime-rl; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence | claim:SF-2026-ARXIV-2602-11456 | complete |
| SF-2026-ARXIV-2602-11470 | RP-ea0f9917edd8b9d7 | deep | arXiv:2602.11470v1 | SRC-ARXIV@arXiv:2602.11470v1 | arXiv:2602.11470v1 HTML — §3. System Overview [facet=method]; https://arxiv.org/html/2602.11470v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11470v1.html; sha256:e9079fc5c6cdb3985999387c89eab42d90bc0747c35a318eac17ec1d3841400b | arXiv:2602.11470v1 HTML — §7.3. End-to-end Performance Evaluation [facet=evaluation]; https://arxiv.org/html/2602.11470v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11470v1.html; sha256:e9079fc5c6cdb3985999387c89eab42d90bc0747c35a318eac17ec1d3841400b | arXiv:2602.11470v1 HTML — §7.4. Discussions on Accuracy [facet=limitations]; https://arxiv.org/html/2602.11470v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11470v1.html; sha256:e9079fc5c6cdb3985999387c89eab42d90bc0747c35a318eac17ec1d3841400b | External link observed in exact-v1 body: https://github.com/tuneinsight/lattigo; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence | claim:SF-2026-ARXIV-2602-11470 | complete |
| SF-2026-ARXIV-2602-11506 | RP-d99b7b08be66d525 | deep | arXiv:2602.11506v1 | SRC-ARXIV@arXiv:2602.11506v1 | arXiv:2602.11506v1 HTML — §3 Methodology: The Integrated Standard Roofline Framework [facet=method]; https://arxiv.org/html/2602.11506v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11506v1.html; sha256:2c15160129cd0378c3cb0df54927d4f9a8c6baa7b886129f1b3c3bd827a8ce58 | arXiv:2602.11506v1 HTML — §4 Comprehensive Characterization Study [facet=evaluation]; https://arxiv.org/html/2602.11506v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11506v1.html; sha256:2c15160129cd0378c3cb0df54927d4f9a8c6baa7b886129f1b3c3bd827a8ce58 | arXiv:2602.11506v1 HTML — §Appendix B Future Work [facet=limitations]; https://arxiv.org/html/2602.11506v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11506v1.html; sha256:2c15160129cd0378c3cb0df54927d4f9a8c6baa7b886129f1b3c3bd827a8ce58 | External link observed in exact-v1 body: https://github.com/banbu-ai/roofline_bench; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence | claim:SF-2026-ARXIV-2602-11506 | complete |
| SF-2026-ARXIV-2602-11510 | RP-1be66ec093fb33b1 | deep | arXiv:2602.11510v1 | SRC-ARXIV@arXiv:2602.11510v1 | arXiv:2602.11510v1 HTML — §IV AgentLeak Benchmark Design [facet=method]; https://arxiv.org/html/2602.11510v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11510v1.html; sha256:d743053774158cc209c1d780d4db14bd22d4074fceceab6056e150ed0374f5c7 | arXiv:2602.11510v1 HTML — §VI Evaluation and Results [facet=evaluation]; https://arxiv.org/html/2602.11510v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11510v1.html; sha256:d743053774158cc209c1d780d4db14bd22d4074fceceab6056e150ed0374f5c7 | arXiv:2602.11510v1 HTML — §VII-D Limitations [facet=limitations]; https://arxiv.org/html/2602.11510v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11510v1.html; sha256:d743053774158cc209c1d780d4db14bd22d4074fceceab6056e150ed0374f5c7 | External link observed in exact-v1 body: https://github.com/Privatris/AgentLeak; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence | claim:SF-2026-ARXIV-2602-11510 | complete |
| SF-2026-ARXIV-2602-11513 | RP-f87a527f97bd7162 | deep | arXiv:2602.11513v1 | SRC-ARXIV@arXiv:2602.11513v1 | arXiv:2602.11513v1 HTML — §4 Methodology [facet=method]; https://arxiv.org/html/2602.11513v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11513v1.html; sha256:cf311d4cb48fb545fcb6931babd1420440e5d8cbd11724a193803e63b3ce0461 | arXiv:2602.11513v1 HTML — §B.4 Additional Experimental Results [facet=evaluation]; https://arxiv.org/html/2602.11513v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11513v1.html; sha256:cf311d4cb48fb545fcb6931babd1420440e5d8cbd11724a193803e63b3ce0461 | Not Disclosed — exact-v1 HTML has no independent limitations or counterevidence section; a positive conclusion does not replace that facet [facet=limitations]; https://arxiv.org/html/2602.11513v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11513v1.html; sha256:cf311d4cb48fb545fcb6931babd1420440e5d8cbd11724a193803e63b3ce0461 | Not Disclosed — arXiv:2602.11513v1 does not disclose a public repository, release, commit, or executable artifact used by this review | claim:SF-2026-ARXIV-2602-11513 | complete |
| SF-2026-ARXIV-2602-11574 | RP-fa07f5b2c917f0c4 | deep | arXiv:2602.11574v1 | SRC-ARXIV@arXiv:2602.11574v1 | arXiv:2602.11574v1 HTML — §3 Methodology [facet=method]; https://arxiv.org/html/2602.11574v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11574v1.html; sha256:c35081da968c7e6dedadffe4b60677d4857e5a67fc40bcac43811a73f94d9172 | arXiv:2602.11574v1 HTML — §4 Experiments [facet=evaluation]; https://arxiv.org/html/2602.11574v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11574v1.html; sha256:c35081da968c7e6dedadffe4b60677d4857e5a67fc40bcac43811a73f94d9172 | arXiv:2602.11574v1 HTML — §4.6 Error Analysis [facet=limitations]; https://arxiv.org/html/2602.11574v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11574v1.html; sha256:c35081da968c7e6dedadffe4b60677d4857e5a67fc40bcac43811a73f94d9172 | External link observed in exact-v1 body: https://github.com/langchain-ai/langchain; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence | claim:SF-2026-ARXIV-2602-11574 | complete |
| SF-2026-ARXIV-2602-11686 | RP-b458035fdd1fc4ff | deep | arXiv:2602.11686v1 | SRC-ARXIV@arXiv:2602.11686v1 | arXiv:2602.11686v1 HTML — §3.1. FSEP: Fully Sharded Expert Parallelism [facet=method]; https://arxiv.org/html/2602.11686v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11686v1.html; sha256:eb4959c55ba3fbc9008ae8a0f1d4ffa834e01d252e0f94a7fc52f910a6108507 | arXiv:2602.11686v1 HTML — §5.2. End-to-End Performance [facet=evaluation]; https://arxiv.org/html/2602.11686v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11686v1.html; sha256:eb4959c55ba3fbc9008ae8a0f1d4ffa834e01d252e0f94a7fc52f910a6108507 | arXiv:2602.11686v1 HTML — §7. Discussion [facet=limitations]; https://arxiv.org/html/2602.11686v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11686v1.html; sha256:eb4959c55ba3fbc9008ae8a0f1d4ffa834e01d252e0f94a7fc52f910a6108507 | Disclosed author artifact: https://github.com/Fizzmy/LAER-MoE-AE; exact manuscript commit/tag Not Disclosed | claim:SF-2026-ARXIV-2602-11686 | complete |
| SF-2026-ARXIV-2602-11749 | RP-2f86f8d3722c6f3a | deep | arXiv:2602.11749v1 | SRC-ARXIV@arXiv:2602.11749v1 | arXiv:2602.11749v1 HTML — §3 Method [facet=method]; https://arxiv.org/html/2602.11749v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11749v1.html; sha256:ef61bffdff81c51b5bf3bf5a2e877044507913fc784ce8e0e300556fbc7eff00 | arXiv:2602.11749v1 HTML — §Appendix C False Positive Evaluation on Safe Tasks [facet=evaluation]; https://arxiv.org/html/2602.11749v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11749v1.html; sha256:ef61bffdff81c51b5bf3bf5a2e877044507913fc784ce8e0e300556fbc7eff00 | arXiv:2602.11749v1 HTML — §5 Discussion [facet=limitations]; https://arxiv.org/html/2602.11749v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11749v1.html; sha256:ef61bffdff81c51b5bf3bf5a2e877044507913fc784ce8e0e300556fbc7eff00 | External link observed in exact-v1 body: https://github.com/langchain-ai/langchain; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence | claim:SF-2026-ARXIV-2602-11749 | complete |
| SF-2026-ARXIV-2602-11786 | RP-fe7e4679918a5cc0 | deep | arXiv:2602.11786v1 | SRC-ARXIV@arXiv:2602.11786v1 | arXiv:2602.11786v1 HTML — §3 Methodology [facet=method]; https://arxiv.org/html/2602.11786v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11786v1.html; sha256:b7394fa874309cd7191b83b87a413453fc83d7619091a7450c9e8e9a67635afb | arXiv:2602.11786v1 HTML — §4.3 Phase 2B: Depth-Oriented Evaluation Under Repeated Sampling [facet=evaluation]; https://arxiv.org/html/2602.11786v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11786v1.html; sha256:b7394fa874309cd7191b83b87a413453fc83d7619091a7450c9e8e9a67635afb | arXiv:2602.11786v1 HTML — §A.7 Limitations of LLM-as-judge [facet=limitations]; https://arxiv.org/html/2602.11786v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11786v1.html; sha256:b7394fa874309cd7191b83b87a413453fc83d7619091a7450c9e8e9a67635afb | Not Disclosed — arXiv:2602.11786v1 does not disclose a public repository, release, commit, or executable artifact used by this review | claim:SF-2026-ARXIV-2602-11786 | complete |
| SF-2026-ARXIV-2602-11877 | RP-a5a7debecadcecb9 | deep | arXiv:2602.11877v1 | SRC-ARXIV@arXiv:2602.11877v1 | arXiv:2602.11877v1 HTML — §4 Methodology [facet=method]; https://arxiv.org/html/2602.11877v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11877v1.html; sha256:041e9c41ab54a246ce1c92544fef3ceb8261b618e06bc65ef3ee8dee2f5863f7 | arXiv:2602.11877v1 HTML — §Router Ability. [facet=evaluation]; https://arxiv.org/html/2602.11877v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11877v1.html; sha256:041e9c41ab54a246ce1c92544fef3ceb8261b618e06bc65ef3ee8dee2f5863f7 | arXiv:2602.11877v1 HTML — §Limitations [facet=limitations]; https://arxiv.org/html/2602.11877v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11877v1.html; sha256:041e9c41ab54a246ce1c92544fef3ceb8261b618e06bc65ef3ee8dee2f5863f7 | External link observed in exact-v1 body: https://github.com/IAAR-Shanghai/xVerify; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence | claim:SF-2026-ARXIV-2602-11877 | complete |
| SF-2026-ARXIV-2602-11937 | RP-dbfcbcc61c0dbed1 | deep | arXiv:2602.11937v1 | SRC-ARXIV@arXiv:2602.11937v1 | arXiv:2602.11937v1 HTML — §2 Puzzle Optimization [facet=method]; https://arxiv.org/html/2602.11937v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11937v1.html; sha256:81124f3be1b3b50c4995e2b32c8fee5df74bac458eb9e8011c7e7d06bba23c9e | arXiv:2602.11937v1 HTML — §4.1 Inference Efficiency [facet=evaluation]; https://arxiv.org/html/2602.11937v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11937v1.html; sha256:81124f3be1b3b50c4995e2b32c8fee5df74bac458eb9e8011c7e7d06bba23c9e | arXiv:2602.11937v1 HTML — §5 Discussion [facet=limitations]; https://arxiv.org/html/2602.11937v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11937v1.html; sha256:81124f3be1b3b50c4995e2b32c8fee5df74bac458eb9e8011c7e7d06bba23c9e | External link observed in exact-v1 body: https://github.com/NVIDIA-NeMo/Skills; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence | claim:SF-2026-ARXIV-2602-11937 | complete |
| SF-2026-ARXIV-2602-11964 | RP-a0e2597693708c59 | deep | arXiv:2602.11964v1 | SRC-ARXIV@arXiv:2602.11964v1 | arXiv:2602.11964v1 HTML — §4.2 Scenario design and annotation protocol [facet=method]; https://arxiv.org/html/2602.11964v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11964v1.html; sha256:33867dac751b1d0921776da6e74d85a54ee3c306c826721ccfe2cf843853097b | arXiv:2602.11964v1 HTML — §5.1 Core results [facet=evaluation]; https://arxiv.org/html/2602.11964v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11964v1.html; sha256:33867dac751b1d0921776da6e74d85a54ee3c306c826721ccfe2cf843853097b | arXiv:2602.11964v1 HTML — §6 Conclusion & discussion [facet=limitations]; https://arxiv.org/html/2602.11964v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11964v1.html; sha256:33867dac751b1d0921776da6e74d85a54ee3c306c826721ccfe2cf843853097b | External link observed in exact-v1 body: https://github.com/eval-sys/mcpmark; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence | claim:SF-2026-ARXIV-2602-11964 | complete |
| SF-2026-ARXIV-2602-12194 | RP-90ba97b65e91b491 | deep | arXiv:2602.12194v1 | SRC-ARXIV@arXiv:2602.12194v1 | arXiv:2602.12194v1 HTML — §5 Our MalTool [facet=method]; https://arxiv.org/html/2602.12194v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.12194v1.html; sha256:86fb4d83d5064cd399d777272f2c4374e0dc0af7d08875898ab7467f36edf36e | arXiv:2602.12194v1 HTML — §6 Evaluating MalTool [facet=evaluation]; https://arxiv.org/html/2602.12194v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.12194v1.html; sha256:86fb4d83d5064cd399d777272f2c4374e0dc0af7d08875898ab7467f36edf36e | arXiv:2602.12194v1 HTML — §8 Discussion and Limitations [facet=limitations]; https://arxiv.org/html/2602.12194v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.12194v1.html; sha256:86fb4d83d5064cd399d777272f2c4374e0dc0af7d08875898ab7467f36edf36e | External link observed in exact-v1 body: https://github.com/Tencent/AI-Infra-Guard; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence | claim:SF-2026-ARXIV-2602-12194 | complete |
| SF-2026-ARXIV-2602-12244 | RP-61d88b09b045871b | deep | arXiv:2602.12244v1 | SRC-ARXIV@arXiv:2602.12244v1 | arXiv:2602.12244v1 HTML — §III Overview [facet=method]; https://arxiv.org/html/2602.12244v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.12244v1.html; sha256:c9e7b0fb36c5585b9cec94ac7380ae8609d2aabb18cf4478e0a34b7c79db5423 | arXiv:2602.12244v1 HTML — §V-A Inference and Evaluation [facet=evaluation]; https://arxiv.org/html/2602.12244v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.12244v1.html; sha256:c9e7b0fb36c5585b9cec94ac7380ae8609d2aabb18cf4478e0a34b7c79db5423 | arXiv:2602.12244v1 HTML — §VII Conclusion & Limitations [facet=limitations]; https://arxiv.org/html/2602.12244v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.12244v1.html; sha256:c9e7b0fb36c5585b9cec94ac7380ae8609d2aabb18cf4478e0a34b7c79db5423 | Not Disclosed — arXiv:2602.12244v1 does not disclose a public repository, release, commit, or executable artifact used by this review | claim:SF-2026-ARXIV-2602-12244 | complete |
| SF-2026-ARXIV-2602-12271 | RP-304e3192c10df1c1 | deep | arXiv:2602.12271v1 | SRC-ARXIV@arXiv:2602.12271v1 | arXiv:2602.12271v1 HTML — §4.3 Finetuning and Efficient Implementation [facet=method]; https://arxiv.org/html/2602.12271v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.12271v1.html; sha256:1d055e54551643b9ba31d1ccf05347b4dc62f13389ca6343a278b8ce7004c491 | arXiv:2602.12271v1 HTML — §5.3 Efficiency Evaluations [facet=evaluation]; https://arxiv.org/html/2602.12271v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.12271v1.html; sha256:1d055e54551643b9ba31d1ccf05347b4dc62f13389ca6343a278b8ce7004c491 | arXiv:2602.12271v1 HTML — §3.1 Approximation Error Analysis [facet=limitations]; https://arxiv.org/html/2602.12271v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.12271v1.html; sha256:1d055e54551643b9ba31d1ccf05347b4dc62f13389ca6343a278b8ce7004c491 | External link observed in exact-v1 body: https://github.com/Infini-AI-Lab/MonarchRT; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence | claim:SF-2026-ARXIV-2602-12271 | complete |
| SF-2026-ARXIV-2602-12281 | RP-9d936a262e84806d | deep | arXiv:2602.12281v1 | SRC-ARXIV@arXiv:2602.12281v1 | arXiv:2602.12281v1 HTML — §4 Method [facet=method]; https://arxiv.org/html/2602.12281v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.12281v1.html; sha256:03a663e9d70f0f708896662286497a6086d64aa00b6fac1f2d251790d308c7db | arXiv:2602.12281v1 HTML — §5.4 Simulation Evaluation Results [facet=evaluation]; https://arxiv.org/html/2602.12281v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.12281v1.html; sha256:03a663e9d70f0f708896662286497a6086d64aa00b6fac1f2d251790d308c7db | arXiv:2602.12281v1 HTML — §6 Conclusion [facet=limitations]; https://arxiv.org/html/2602.12281v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.12281v1.html; sha256:03a663e9d70f0f708896662286497a6086d64aa00b6fac1f2d251790d308c7db | External link observed in exact-v1 body: https://huggingface.co/juexzz/INTACT-pi0-finetune-bridge; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence | claim:SF-2026-ARXIV-2602-12281 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2602-11882:start -->
### Where Bits Matter in World Model Planning: A Paired Mixed-Bit Study for Efficient Spatial Reasoning

- **Review route:** `deep`；Primary=`arXiv:2602.11882v1`；owner=`INFER-TENSORRT-LLM`。

- **问题与旧路径：** `Where Bits Matter in World Model Planning: A Paired Mixed-Bit Study for Efficient Spatial Reasoning` 是否在 `INFER-TENSORRT-LLM` 中改变已有状态、数据或控制责任；旧路径仍成立于：通用 eager 执行便于调试且无需额外编译状态。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.11882v1 HTML — §Quantization implementation details.` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 graph lowering、kernel/precision 选择与执行计划版本。触发约束是：模型规模、算子形态和 SLO 使执行计划、精度与 kernel 选择成为主要成本。

- **State / data / control owner：** `INFER-TENSORRT-LLM` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** External link observed in exact-v1 body: https://github.com/suraj-ranganath/DINO-MBQuant; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.11882v1 HTML — §Evaluation protocol.`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.11882v1 HTML — §5 Discussion, Limitations, and Outlook`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：工作负载小、形状动态或调试优先时 eager 路径仍合理。

<!-- claim:SF-2026-ARXIV-2602-11882:start -->
- **Claim boundary:** 只支持 arXiv:2602.11882v1 实际披露的机制与实验。方法定位为 arXiv:2602.11882v1 HTML — §Quantization implementation details.；验证定位为 arXiv:2602.11882v1 HTML — §Evaluation protocol.；边界定位为 arXiv:2602.11882v1 HTML — §5 Discussion, Limitations, and Outlook。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-11882:end -->
<!-- review:SF-2026-ARXIV-2602-11882:end -->

<!-- review:SF-2026-ARXIV-2602-11291:start -->
### H-WM: Robotic Task and Motion Planning Guided by Hierarchical World Model

- **Review route:** `deep`；Primary=`arXiv:2602.11291v1`；owner=`MULTIMODAL-WORLD-MODELS`。

- **问题与旧路径：** `H-WM: Robotic Task and Motion Planning Guided by Hierarchical World Model` 是否在 `MULTIMODAL-WORLD-MODELS` 中改变已有状态、数据或控制责任；旧路径仍成立于：下一帧生成可学习外观连续性，但不必显式承担动作可控的状态转移。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.11291v1 HTML — §4.3 Pipeline for VLA under Hierarchical World Model Guidance` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 latent state、action-conditioned transition 与 rollout commitment。触发约束是：规划与闭环评估要求预测 action-conditioned transition，而非只生成逼真视频。

- **State / data / control owner：** `MULTIMODAL-WORLD-MODELS` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** Not Disclosed — arXiv:2602.11291v1 does not disclose a public repository, release, commit, or executable artifact used by this review

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.11291v1 HTML — §5.2 Benchmark and evaluation`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.11291v1 HTML — §7 Limitations`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：只需内容生成而不需要因果控制时普通 video model 仍足够。

<!-- claim:SF-2026-ARXIV-2602-11291:start -->
- **Claim boundary:** 只支持 arXiv:2602.11291v1 实际披露的机制与实验。方法定位为 arXiv:2602.11291v1 HTML — §4.3 Pipeline for VLA under Hierarchical World Model Guidance；验证定位为 arXiv:2602.11291v1 HTML — §5.2 Benchmark and evaluation；边界定位为 arXiv:2602.11291v1 HTML — §7 Limitations。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-11291:end -->
<!-- review:SF-2026-ARXIV-2602-11291:end -->

<!-- review:SF-2026-ARXIV-2602-11301:start -->
### The PBSAI Governance Ecosystem: A Multi-Agent AI Reference Architecture for Securing Enterprise AI Estates

- **Review route:** `deep`；Primary=`arXiv:2602.11301v1`；owner=`PLATFORM-SECURITY`。

- **问题与旧路径：** `The PBSAI Governance Ecosystem: A Multi-Agent AI Reference Architecture for Securing Enterprise AI Estates` 是否在 `PLATFORM-SECURITY` 中改变已有状态、数据或控制责任；旧路径仍成立于：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.11301v1 PDF — §3 Architecture Overview: 12-Domain Ecosystem and Minimal Stack` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 身份、授权、数据流、策略执行点与审计证据。触发约束是：工具、记忆和多 agent 委托把不可信内容转化为可执行控制流。

- **State / data / control owner：** `PLATFORM-SECURITY` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** Not Disclosed — arXiv:2602.11301v1 does not disclose a public repository, release, commit, or executable artifact used by this review

- **Evaluation contract：** exact-v1 未披露可独立定位的 evaluation（`Not Disclosed — exact-v1 PDF 全文已审计但未提供独立 Evaluation 章节`）；因此不声称经验收益。已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.11301v1 PDF — §7 Discussion and Conclusion`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：无工具、无持久状态的只读场景仍可采用较薄边界。

<!-- claim:SF-2026-ARXIV-2602-11301:start -->
- **Claim boundary:** 只支持 arXiv:2602.11301v1 实际披露的机制与实验。方法定位为 arXiv:2602.11301v1 PDF — §3 Architecture Overview: 12-Domain Ecosystem and Minimal Stack；evaluation facet 未独立披露，不声称经验收益；边界定位为 arXiv:2602.11301v1 PDF — §7 Discussion and Conclusion。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-11301:end -->
<!-- review:SF-2026-ARXIV-2602-11301:end -->

<!-- review:SF-2026-ARXIV-2602-11327:start -->
### Security Threat Modeling for Emerging AI-Agent Protocols: A Comparative Analysis of MCP, A2A, Agora, and ANP

- **Review route:** `deep`；Primary=`arXiv:2602.11327v1`；owner=`PLATFORM-SECURITY`。

- **问题与旧路径：** `Security Threat Modeling for Emerging AI-Agent Protocols: A Comparative Analysis of MCP, A2A, Agora, and ANP` 是否在 `PLATFORM-SECURITY` 中改变已有状态、数据或控制责任；旧路径仍成立于：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.11327v1 HTML — §6.1 Assessment Methodology` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 身份、授权、数据流、策略执行点与审计证据。触发约束是：工具、记忆和多 agent 委托把不可信内容转化为可执行控制流。

- **State / data / control owner：** `PLATFORM-SECURITY` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** External link observed in exact-v1 body: https://github.com/a2aproject/A2A; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.11327v1 HTML — §6.2 Lifecycle-Based Evaluation Framework`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.11327v1 HTML — §4.1.4 Absence of limitations on token lifetime`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：无工具、无持久状态的只读场景仍可采用较薄边界。

<!-- claim:SF-2026-ARXIV-2602-11327:start -->
- **Claim boundary:** 只支持 arXiv:2602.11327v1 实际披露的机制与实验。方法定位为 arXiv:2602.11327v1 HTML — §6.1 Assessment Methodology；验证定位为 arXiv:2602.11327v1 HTML — §6.2 Lifecycle-Based Evaluation Framework；边界定位为 arXiv:2602.11327v1 HTML — §4.1.4 Absence of limitations on token lifetime。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-11327:end -->
<!-- review:SF-2026-ARXIV-2602-11327:end -->

<!-- review:SF-2026-ARXIV-2602-11521:start -->
### PAM: Processing Across Memory Hierarchy for Efficient KV-centric LLM Serving System

- **Review route:** `deep`；Primary=`arXiv:2602.11521v1`；owner=`INFER-GPU-MEMORY`。

- **问题与旧路径：** `PAM: Processing Across Memory Hierarchy for Efficient KV-centric LLM Serving System` 是否在 `INFER-GPU-MEMORY` 中改变已有状态、数据或控制责任；旧路径仍成立于：权重与运行时状态常驻单设备，状态最透明。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.11521v1 HTML — §4. PAM: System Overview` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 权重、KV、临时张量的 placement、lifetime 与迁移控制。触发约束是：容量、带宽和并发超过单设备预算后，放置、迁移与回收成为控制问题。

- **State / data / control owner：** `INFER-GPU-MEMORY` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** External link observed in exact-v1 body: https://github.com/CMU-SAFARI/ramulator2; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.11521v1 HTML — §7.1. Evaluation Methodology`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.11521v1 HTML — §3.1. Limitations of Layered PIM`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：模型可完整驻留且负载稳定时静态常驻仍更简单。

<!-- claim:SF-2026-ARXIV-2602-11521:start -->
- **Claim boundary:** 只支持 arXiv:2602.11521v1 实际披露的机制与实验。方法定位为 arXiv:2602.11521v1 HTML — §4. PAM: System Overview；验证定位为 arXiv:2602.11521v1 HTML — §7.1. Evaluation Methodology；边界定位为 arXiv:2602.11521v1 HTML — §3.1. Limitations of Layered PIM。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-11521:end -->
<!-- review:SF-2026-ARXIV-2602-11521:end -->

<!-- review:SF-2026-ARXIV-2602-11530:start -->
### PASCAL: A Phase-Aware Scheduling Algorithm for Serving Reasoning-based Large Language Models

- **Review route:** `deep`；Primary=`arXiv:2602.11530v1`；owner=`INFER-SCHEDULING`。

- **问题与旧路径：** `PASCAL: A Phase-Aware Scheduling Algorithm for Serving Reasoning-based Large Language Models` 是否在 `INFER-SCHEDULING` 中改变已有状态、数据或控制责任；旧路径仍成立于：FIFO 或静态批次在请求同质时易预测、易实现。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.11530v1 HTML — §III-A Methodology` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 准入、批处理、优先级、路由和资源选择。触发约束是：长度、阶段、SLO、模型和 agent fan-out 的异质性使排队决策决定整体尾延迟。

- **State / data / control owner：** `INFER-SCHEDULING` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** External link observed in exact-v1 body: https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.11530v1 HTML — §V-B User Experience (TTFT, SLO Violation) and Throughput`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.11530v1 HTML — §VII Future work`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：同质离线吞吐任务仍可使用简单静态策略。

<!-- claim:SF-2026-ARXIV-2602-11530:start -->
- **Claim boundary:** 只支持 arXiv:2602.11530v1 实际披露的机制与实验。方法定位为 arXiv:2602.11530v1 HTML — §III-A Methodology；验证定位为 arXiv:2602.11530v1 HTML — §V-B User Experience (TTFT, SLO Violation) and Throughput；边界定位为 arXiv:2602.11530v1 HTML — §VII Future work。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-11530:end -->
<!-- review:SF-2026-ARXIV-2602-11530:end -->

<!-- review:SF-2026-ARXIV-2602-11543:start -->
### Pretraining A Large Language Model using Distributed GPUs: A Memory-Efficient Decentralized Paradigm

- **Review route:** `deep`；Primary=`arXiv:2602.11543v1`；owner=`TRAIN-DISTRIBUTED-TRAINING`。

- **问题与旧路径：** `Pretraining A Large Language Model using Distributed GPUs: A Memory-Efficient Decentralized Paradigm` 是否在 `TRAIN-DISTRIBUTED-TRAINING` 中改变已有状态、数据或控制责任；旧路径仍成立于：单机或纯数据并行状态最少、同步语义清晰。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.11543v1 HTML — §3.2 Overall Framework` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 训练状态分片、collective、同步与故障恢复。触发约束是：参数、optimizer state 和通信规模越过单设备边界。

- **State / data / control owner：** `TRAIN-DISTRIBUTED-TRAINING` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** External link observed in exact-v1 body: https://github.com/openlm-research/open_llama; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.11543v1 HTML — §4.2 Main Results`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.11543v1 HTML — §5 Conclusion`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：模型可装入单机且通信占比高时简单并行仍更优。

<!-- claim:SF-2026-ARXIV-2602-11543:start -->
- **Claim boundary:** 只支持 arXiv:2602.11543v1 实际披露的机制与实验。方法定位为 arXiv:2602.11543v1 HTML — §3.2 Overall Framework；验证定位为 arXiv:2602.11543v1 HTML — §4.2 Main Results；边界定位为 arXiv:2602.11543v1 HTML — §5 Conclusion。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-11543:end -->
<!-- review:SF-2026-ARXIV-2602-11543:end -->

<!-- review:SF-2026-ARXIV-2602-11688:start -->
### GORGO: Online Tuning for Cross-Region Network-Aware LLM Serving

- **Review route:** `deep`；Primary=`arXiv:2602.11688v1`；owner=`INFER-SCHEDULING`。

- **问题与旧路径：** `GORGO: Online Tuning for Cross-Region Network-Aware LLM Serving` 是否在 `INFER-SCHEDULING` 中改变已有状态、数据或控制责任；旧路径仍成立于：FIFO 或静态批次在请求同质时易预测、易实现。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.11688v1 HTML — §3.2 Design objective and signal requirements` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 准入、批处理、优先级、路由和资源选择。触发约束是：长度、阶段、SLO、模型和 agent fan-out 的异质性使排队决策决定整体尾延迟。

- **State / data / control owner：** `INFER-SCHEDULING` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** External link observed in exact-v1 body: https://github.com/atoniolo76/gotoni/tree/benchmark-load-balancing; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.11688v1 HTML — §4 Experimental Evaluation`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.11688v1 HTML — §Methodological limitations.`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：同质离线吞吐任务仍可使用简单静态策略。

<!-- claim:SF-2026-ARXIV-2602-11688:start -->
- **Claim boundary:** 只支持 arXiv:2602.11688v1 实际披露的机制与实验。方法定位为 arXiv:2602.11688v1 HTML — §3.2 Design objective and signal requirements；验证定位为 arXiv:2602.11688v1 HTML — §4 Experimental Evaluation；边界定位为 arXiv:2602.11688v1 HTML — §Methodological limitations.。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-11688:end -->
<!-- review:SF-2026-ARXIV-2602-11688:end -->

<!-- review:SF-2026-ARXIV-2602-11790:start -->
### Beyond End-to-End Video Models: An LLM-Based Multi-Agent System for Educational Video Generation

- **Review route:** `deep`；Primary=`arXiv:2602.11790v1`；owner=`AGENT-WORKFLOW`。

- **问题与旧路径：** `Beyond End-to-End Video Models: An LLM-Based Multi-Agent System for Educational Video Generation` 是否在 `AGENT-WORKFLOW` 中改变已有状态、数据或控制责任；旧路径仍成立于：把 agent loop 留在进程内代码，开发快且控制流直观。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.11790v1 HTML — §4.1. System Overview` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 workflow graph、checkpoint、重试与演进状态。触发约束是：长任务、失败恢复和运行时重写要求控制流成为可验证、可持久化的对象。

- **State / data / control owner：** `AGENT-WORKFLOW` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** External link observed in exact-v1 body: https://github.com/MiniMax-AI; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.11790v1 HTML — §5.2. Main Results`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.11790v1 HTML — §5.4. Error Analysis`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：短暂、幂等任务仍可采用轻量进程内循环。

<!-- claim:SF-2026-ARXIV-2602-11790:start -->
- **Claim boundary:** 只支持 arXiv:2602.11790v1 实际披露的机制与实验。方法定位为 arXiv:2602.11790v1 HTML — §4.1. System Overview；验证定位为 arXiv:2602.11790v1 HTML — §5.2. Main Results；边界定位为 arXiv:2602.11790v1 HTML — §5.4. Error Analysis。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-11790:end -->
<!-- review:SF-2026-ARXIV-2602-11790:end -->

<!-- review:SF-2026-ARXIV-2602-12029:start -->
### PrefillShare: A Shared Prefill Module for KV Reuse in Multi-LLM Disaggregated Serving

- **Review route:** `deep`；Primary=`arXiv:2602.12029v1`；owner=`INFER-PD-DISAGGREGATION`。

- **问题与旧路径：** `PrefillShare: A Shared Prefill Module for KV Reuse in Multi-LLM Disaggregated Serving` 是否在 `INFER-PD-DISAGGREGATION` 中改变已有状态、数据或控制责任；旧路径仍成立于：prefill 与 decode 共置便于共享权重和 KV，低负载下最少网络跳转。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.12029v1 HTML — §3 Method` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 阶段拆分、KV handoff 与资源池选择。触发约束是：多轮请求的阶段成本和到达分布分化，使单一资源池难同时满足 TTFT 与 TPOT。

- **State / data / control owner：** `INFER-PD-DISAGGREGATION` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** External link observed in exact-v1 body: https://github.com/langchain-ai/langchain; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.12029v1 HTML — §B.3 Results with a different backbone model`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** exact-v1 未披露独立 limitations（`Not Disclosed — exact-v1 HTML has no independent limitations or counterevidence section; a positive conclusion does not replace that facet`）；这意味着审阅必须缩小主张，而不是把缺口当作反证。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：负载较小或网络成本占主导时共置仍更合适。

<!-- claim:SF-2026-ARXIV-2602-12029:start -->
- **Claim boundary:** 只支持 arXiv:2602.12029v1 实际披露的机制与实验。方法定位为 arXiv:2602.12029v1 HTML — §3 Method；验证定位为 arXiv:2602.12029v1 HTML — §B.3 Results with a different backbone model；独立 limitations 未披露，因而采用更窄主张。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-12029:end -->
<!-- review:SF-2026-ARXIV-2602-12029:end -->

<!-- review:SF-2026-ARXIV-2602-12151:start -->
### OServe: Accelerating LLM Serving via Spatial-Temporal Workload Orchestration

- **Review route:** `deep`；Primary=`arXiv:2602.12151v1`；owner=`INFER-SCHEDULING`。

- **问题与旧路径：** `OServe: Accelerating LLM Serving via Spatial-Temporal Workload Orchestration` 是否在 `INFER-SCHEDULING` 中改变已有状态、数据或控制责任；旧路径仍成立于：FIFO 或静态批次在请求同质时易预测、易实现。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.12151v1 HTML — §5.4 Algorithm Efficiency` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 准入、批处理、优先级、路由和资源选择。触发约束是：长度、阶段、SLO、模型和 agent fan-out 的异质性使排队决策决定整体尾延迟。

- **State / data / control owner：** `INFER-SCHEDULING` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** External link observed in exact-v1 body: https://github.com/Azure/AzurePublicDataset; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.12151v1 HTML — §5.3 Case and Ablation Studies`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.12151v1 HTML — §Appendix C Extended Discussion`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：同质离线吞吐任务仍可使用简单静态策略。

<!-- claim:SF-2026-ARXIV-2602-12151:start -->
- **Claim boundary:** 只支持 arXiv:2602.12151v1 实际披露的机制与实验。方法定位为 arXiv:2602.12151v1 HTML — §5.4 Algorithm Efficiency；验证定位为 arXiv:2602.12151v1 HTML — §5.3 Case and Ablation Studies；边界定位为 arXiv:2602.12151v1 HTML — §Appendix C Extended Discussion。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-12151:end -->
<!-- review:SF-2026-ARXIV-2602-12151:end -->

<!-- review:SF-2026-ARXIV-2602-11184:start -->
### KBVQ-MoE: KLT-guided SVD with Bias-Corrected Vector Quantization for MoE Large Language Models

- **Review route:** `deep`；Primary=`arXiv:2602.11184v1`；owner=`INFER-TENSORRT-LLM`。

- **问题与旧路径：** `KBVQ-MoE: KLT-guided SVD with Bias-Corrected Vector Quantization for MoE Large Language Models` 是否在 `INFER-TENSORRT-LLM` 中改变已有状态、数据或控制责任；旧路径仍成立于：通用 eager 执行便于调试且无需额外编译状态。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.11184v1 HTML — §2.2 MoE LLMs Compression Methods` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 graph lowering、kernel/precision 选择与执行计划版本。触发约束是：模型规模、算子形态和 SLO 使执行计划、精度与 kernel 选择成为主要成本。

- **State / data / control owner：** `INFER-TENSORRT-LLM` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** Not Disclosed — arXiv:2602.11184v1 does not disclose a public repository, release, commit, or executable artifact used by this review

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.11184v1 HTML — §Main results.`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.11184v1 HTML — §A.12 Limitations`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：工作负载小、形状动态或调试优先时 eager 路径仍合理。

<!-- claim:SF-2026-ARXIV-2602-11184:start -->
- **Claim boundary:** 只支持 arXiv:2602.11184v1 实际披露的机制与实验。方法定位为 arXiv:2602.11184v1 HTML — §2.2 MoE LLMs Compression Methods；验证定位为 arXiv:2602.11184v1 HTML — §Main results.；边界定位为 arXiv:2602.11184v1 HTML — §A.12 Limitations。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-11184:end -->
<!-- review:SF-2026-ARXIV-2602-11184:end -->

<!-- review:SF-2026-ARXIV-2602-11192:start -->
### MELINOE: Fine-Tuning Enables Memory-Efficient Inference for Mixture-of-Experts Models

- **Review route:** `deep`；Primary=`arXiv:2602.11192v1`；owner=`INFER-GPU-MEMORY`。

- **问题与旧路径：** `MELINOE: Fine-Tuning Enables Memory-Efficient Inference for Mixture-of-Experts Models` 是否在 `INFER-GPU-MEMORY` 中改变已有状态、数据或控制责任；旧路径仍成立于：权重与运行时状态常驻单设备，状态最透明。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.11192v1 HTML — §3 Method` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 权重、KV、临时张量的 placement、lifetime 与迁移控制。触发约束是：容量、带宽和并发超过单设备预算后，放置、迁移与回收成为控制问题。

- **State / data / control owner：** `INFER-GPU-MEMORY` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** Not Disclosed — arXiv:2602.11192v1 does not disclose a public repository, release, commit, or executable artifact used by this review

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.11192v1 HTML — §4.2 Main Results`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.11192v1 HTML — §5 Conclusion`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：模型可完整驻留且负载稳定时静态常驻仍更简单。

<!-- claim:SF-2026-ARXIV-2602-11192:start -->
- **Claim boundary:** 只支持 arXiv:2602.11192v1 实际披露的机制与实验。方法定位为 arXiv:2602.11192v1 HTML — §3 Method；验证定位为 arXiv:2602.11192v1 HTML — §4.2 Main Results；边界定位为 arXiv:2602.11192v1 HTML — §5 Conclusion。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-11192:end -->
<!-- review:SF-2026-ARXIV-2602-11192:end -->

<!-- review:SF-2026-ARXIV-2602-11224:start -->
### Agent-Diff: Benchmarking LLM Agents on Enterprise API Tasks via Code Execution with State-Diff-Based Evaluation

- **Review route:** `deep`；Primary=`arXiv:2602.11224v1`；owner=`PLATFORM-EVALUATION-SYSTEM`。

- **问题与旧路径：** `Agent-Diff: Benchmarking LLM Agents on Enterprise API Tasks via Code Execution with State-Diff-Based Evaluation` 是否在 `PLATFORM-EVALUATION-SYSTEM` 中改变已有状态、数据或控制责任；旧路径仍成立于：单一离线分数便于比较版本。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.11224v1 HTML — §3. Agent-Diff` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 evaluation contract、覆盖分母、evidence lineage 与 release gate。触发约束是：agent、长时程和多模态系统把失败分散到状态、工具与环境交互链。

- **State / data / control owner：** `PLATFORM-EVALUATION-SYSTEM` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** External link observed in exact-v1 body: https://github.com/agent-diff-bench/agent-diff; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.11224v1 HTML — §4. Evaluation Methodology`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.11224v1 HTML — §6.3. Failure and Recovery Modes`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：窄任务且 failure surface 稳定时单指标仍可作为局部信号。

<!-- claim:SF-2026-ARXIV-2602-11224:start -->
- **Claim boundary:** 只支持 arXiv:2602.11224v1 实际披露的机制与实验。方法定位为 arXiv:2602.11224v1 HTML — §3. Agent-Diff；验证定位为 arXiv:2602.11224v1 HTML — §4. Evaluation Methodology；边界定位为 arXiv:2602.11224v1 HTML — §6.3. Failure and Recovery Modes。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-11224:end -->
<!-- review:SF-2026-ARXIV-2602-11224:end -->

<!-- review:SF-2026-ARXIV-2602-11287:start -->
### HiFloat4 Format for Language Model Inference

- **Review route:** `deep`；Primary=`arXiv:2602.11287v1`；owner=`INFER-TENSORRT-LLM`。

- **问题与旧路径：** `HiFloat4 Format for Language Model Inference` 是否在 `INFER-TENSORRT-LLM` 中改变已有状态、数据或控制责任；旧路径仍成立于：通用 eager 执行便于调试且无需额外编译状态。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.11287v1 HTML — §II HiFloat4` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 graph lowering、kernel/precision 选择与执行计划版本。触发约束是：模型规模、算子形态和 SLO 使执行计划、精度与 kernel 选择成为主要成本。

- **State / data / control owner：** `INFER-TENSORRT-LLM` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** Not Disclosed — arXiv:2602.11287v1 does not disclose a public repository, release, commit, or executable artifact used by this review

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.11287v1 HTML — §IV Language Model Inference with HiFloat4`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.11287v1 HTML — §V Conclusion`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：工作负载小、形状动态或调试优先时 eager 路径仍合理。

<!-- claim:SF-2026-ARXIV-2602-11287:start -->
- **Claim boundary:** 只支持 arXiv:2602.11287v1 实际披露的机制与实验。方法定位为 arXiv:2602.11287v1 HTML — §II HiFloat4；验证定位为 arXiv:2602.11287v1 HTML — §IV Language Model Inference with HiFloat4；边界定位为 arXiv:2602.11287v1 HTML — §V Conclusion。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-11287:end -->
<!-- review:SF-2026-ARXIV-2602-11287:end -->

<!-- review:SF-2026-ARXIV-2602-11348:start -->
### AgentNoiseBench: Benchmarking Robustness of Tool-Using LLM Agents Under Noisy Condition

- **Review route:** `deep`；Primary=`arXiv:2602.11348v1`；owner=`PLATFORM-EVALUATION-SYSTEM`。

- **问题与旧路径：** `AgentNoiseBench: Benchmarking Robustness of Tool-Using LLM Agents Under Noisy Condition` 是否在 `PLATFORM-EVALUATION-SYSTEM` 中改变已有状态、数据或控制责任；旧路径仍成立于：单一离线分数便于比较版本。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.11348v1 HTML — §2.1 Design Principles` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 evaluation contract、覆盖分母、evidence lineage 与 release gate。触发约束是：agent、长时程和多模态系统把失败分散到状态、工具与环境交互链。

- **State / data / control owner：** `PLATFORM-EVALUATION-SYSTEM` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** External link observed in exact-v1 body: https://github.com/keven-cyber/agentnoisebench; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.11348v1 HTML — §A.1 Main Results`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.11348v1 HTML — §5 Limitations`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：窄任务且 failure surface 稳定时单指标仍可作为局部信号。

<!-- claim:SF-2026-ARXIV-2602-11348:start -->
- **Claim boundary:** 只支持 arXiv:2602.11348v1 实际披露的机制与实验。方法定位为 arXiv:2602.11348v1 HTML — §2.1 Design Principles；验证定位为 arXiv:2602.11348v1 HTML — §A.1 Main Results；边界定位为 arXiv:2602.11348v1 HTML — §5 Limitations。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-11348:end -->
<!-- review:SF-2026-ARXIV-2602-11348:end -->

<!-- review:SF-2026-ARXIV-2602-11456:start -->
### AuroraRL: Fast, Fault-Tolerant, and Cost-Efficient Reinforcement Learning over Decentralized Network

- **Review route:** `deep`；Primary=`arXiv:2602.11456v1`；owner=`TRAIN-DISTRIBUTED-TRAINING`。

- **问题与旧路径：** `AuroraRL: Fast, Fault-Tolerant, and Cost-Efficient Reinforcement Learning over Decentralized Network` 是否在 `TRAIN-DISTRIBUTED-TRAINING` 中改变已有状态、数据或控制责任；旧路径仍成立于：单机或纯数据并行状态最少、同步语义清晰。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.11456v1 HTML — §5. System Design` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 训练状态分片、collective、同步与故障恢复。触发约束是：参数、optimizer state 和通信规模越过单设备边界。

- **State / data / control owner：** `TRAIN-DISTRIBUTED-TRAINING` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** External link observed in exact-v1 body: https://github.com/PrimeIntellect-ai/prime-rl; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.11456v1 HTML — §7.2. End-to-End Results`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.11456v1 HTML — §6. Discussion`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：模型可装入单机且通信占比高时简单并行仍更优。

<!-- claim:SF-2026-ARXIV-2602-11456:start -->
- **Claim boundary:** 只支持 arXiv:2602.11456v1 实际披露的机制与实验。方法定位为 arXiv:2602.11456v1 HTML — §5. System Design；验证定位为 arXiv:2602.11456v1 HTML — §7.2. End-to-End Results；边界定位为 arXiv:2602.11456v1 HTML — §6. Discussion。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-11456:end -->
<!-- review:SF-2026-ARXIV-2602-11456:end -->

<!-- review:SF-2026-ARXIV-2602-11470:start -->
### Cachemir: Fully Homomorphic Encrypted Inference of Generative Large Language Model with KV Cache

- **Review route:** `deep`；Primary=`arXiv:2602.11470v1`；owner=`PLATFORM-SECURITY`。

- **问题与旧路径：** `Cachemir: Fully Homomorphic Encrypted Inference of Generative Large Language Model with KV Cache` 是否在 `PLATFORM-SECURITY` 中改变已有状态、数据或控制责任；旧路径仍成立于：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.11470v1 HTML — §3. System Overview` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 身份、授权、数据流、策略执行点与审计证据。触发约束是：工具、记忆和多 agent 委托把不可信内容转化为可执行控制流。

- **State / data / control owner：** `PLATFORM-SECURITY` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** External link observed in exact-v1 body: https://github.com/tuneinsight/lattigo; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.11470v1 HTML — §7.3. End-to-end Performance Evaluation`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.11470v1 HTML — §7.4. Discussions on Accuracy`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：无工具、无持久状态的只读场景仍可采用较薄边界。

<!-- claim:SF-2026-ARXIV-2602-11470:start -->
- **Claim boundary:** 只支持 arXiv:2602.11470v1 实际披露的机制与实验。方法定位为 arXiv:2602.11470v1 HTML — §3. System Overview；验证定位为 arXiv:2602.11470v1 HTML — §7.3. End-to-end Performance Evaluation；边界定位为 arXiv:2602.11470v1 HTML — §7.4. Discussions on Accuracy。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-11470:end -->
<!-- review:SF-2026-ARXIV-2602-11470:end -->

<!-- review:SF-2026-ARXIV-2602-11506:start -->
### RooflineBench: A Benchmarking Framework for On-Device LLMs via Roofline Analysis

- **Review route:** `deep`；Primary=`arXiv:2602.11506v1`；owner=`PLATFORM-EVALUATION-SYSTEM`。

- **问题与旧路径：** `RooflineBench: A Benchmarking Framework for On-Device LLMs via Roofline Analysis` 是否在 `PLATFORM-EVALUATION-SYSTEM` 中改变已有状态、数据或控制责任；旧路径仍成立于：单一离线分数便于比较版本。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.11506v1 HTML — §3 Methodology: The Integrated Standard Roofline Framework` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 evaluation contract、覆盖分母、evidence lineage 与 release gate。触发约束是：agent、长时程和多模态系统把失败分散到状态、工具与环境交互链。

- **State / data / control owner：** `PLATFORM-EVALUATION-SYSTEM` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** External link observed in exact-v1 body: https://github.com/banbu-ai/roofline_bench; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.11506v1 HTML — §4 Comprehensive Characterization Study`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.11506v1 HTML — §Appendix B Future Work`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：窄任务且 failure surface 稳定时单指标仍可作为局部信号。

<!-- claim:SF-2026-ARXIV-2602-11506:start -->
- **Claim boundary:** 只支持 arXiv:2602.11506v1 实际披露的机制与实验。方法定位为 arXiv:2602.11506v1 HTML — §3 Methodology: The Integrated Standard Roofline Framework；验证定位为 arXiv:2602.11506v1 HTML — §4 Comprehensive Characterization Study；边界定位为 arXiv:2602.11506v1 HTML — §Appendix B Future Work。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-11506:end -->
<!-- review:SF-2026-ARXIV-2602-11506:end -->

<!-- review:SF-2026-ARXIV-2602-11510:start -->
### AgentLeak: A Benchmark for Internal-Channel Privacy Leakage in Multi-Agent LLM Systems

- **Review route:** `deep`；Primary=`arXiv:2602.11510v1`；owner=`PLATFORM-SECURITY`。

- **问题与旧路径：** `AgentLeak: A Benchmark for Internal-Channel Privacy Leakage in Multi-Agent LLM Systems` 是否在 `PLATFORM-SECURITY` 中改变已有状态、数据或控制责任；旧路径仍成立于：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.11510v1 HTML — §IV AgentLeak Benchmark Design` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 身份、授权、数据流、策略执行点与审计证据。触发约束是：工具、记忆和多 agent 委托把不可信内容转化为可执行控制流。

- **State / data / control owner：** `PLATFORM-SECURITY` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** External link observed in exact-v1 body: https://github.com/Privatris/AgentLeak; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.11510v1 HTML — §VI Evaluation and Results`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.11510v1 HTML — §VII-D Limitations`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：无工具、无持久状态的只读场景仍可采用较薄边界。

<!-- claim:SF-2026-ARXIV-2602-11510:start -->
- **Claim boundary:** 只支持 arXiv:2602.11510v1 实际披露的机制与实验。方法定位为 arXiv:2602.11510v1 HTML — §IV AgentLeak Benchmark Design；验证定位为 arXiv:2602.11510v1 HTML — §VI Evaluation and Results；边界定位为 arXiv:2602.11510v1 HTML — §VII-D Limitations。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-11510:end -->
<!-- review:SF-2026-ARXIV-2602-11510:end -->

<!-- review:SF-2026-ARXIV-2602-11513:start -->
### Differentially Private and Communication Efficient Large Language Model Split Inference via Stochastic Quantization and Soft Prompt

- **Review route:** `deep`；Primary=`arXiv:2602.11513v1`；owner=`PLATFORM-SECURITY`。

- **问题与旧路径：** `Differentially Private and Communication Efficient Large Language Model Split Inference via Stochastic Quantization and Soft Prompt` 是否在 `PLATFORM-SECURITY` 中改变已有状态、数据或控制责任；旧路径仍成立于：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.11513v1 HTML — §4 Methodology` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 身份、授权、数据流、策略执行点与审计证据。触发约束是：工具、记忆和多 agent 委托把不可信内容转化为可执行控制流。

- **State / data / control owner：** `PLATFORM-SECURITY` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** Not Disclosed — arXiv:2602.11513v1 does not disclose a public repository, release, commit, or executable artifact used by this review

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.11513v1 HTML — §B.4 Additional Experimental Results`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** exact-v1 未披露独立 limitations（`Not Disclosed — exact-v1 HTML has no independent limitations or counterevidence section; a positive conclusion does not replace that facet`）；这意味着审阅必须缩小主张，而不是把缺口当作反证。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：无工具、无持久状态的只读场景仍可采用较薄边界。

<!-- claim:SF-2026-ARXIV-2602-11513:start -->
- **Claim boundary:** 只支持 arXiv:2602.11513v1 实际披露的机制与实验。方法定位为 arXiv:2602.11513v1 HTML — §4 Methodology；验证定位为 arXiv:2602.11513v1 HTML — §B.4 Additional Experimental Results；独立 limitations 未披露，因而采用更窄主张。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-11513:end -->
<!-- review:SF-2026-ARXIV-2602-11513:end -->

<!-- review:SF-2026-ARXIV-2602-11574:start -->
### Learning to Configure Agentic AI Systems

- **Review route:** `deep`；Primary=`arXiv:2602.11574v1`；owner=`AGENT-PLATFORM`。

- **问题与旧路径：** `Learning to Configure Agentic AI Systems` 是否在 `AGENT-PLATFORM` 中改变已有状态、数据或控制责任；旧路径仍成立于：应用内 agent loop 上手快且状态较少。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.11574v1 HTML — §3 Methodology` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 agent artifact、runtime、policy、evidence 与 lifecycle control。触发约束是：生产中的多租户、长任务、权限与恢复要求独立平台责任。

- **State / data / control owner：** `AGENT-PLATFORM` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** External link observed in exact-v1 body: https://github.com/langchain-ai/langchain; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.11574v1 HTML — §4 Experiments`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.11574v1 HTML — §4.6 Error Analysis`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：单用户、短时、无外部副作用的任务仍可内嵌运行。

<!-- claim:SF-2026-ARXIV-2602-11574:start -->
- **Claim boundary:** 只支持 arXiv:2602.11574v1 实际披露的机制与实验。方法定位为 arXiv:2602.11574v1 HTML — §3 Methodology；验证定位为 arXiv:2602.11574v1 HTML — §4 Experiments；边界定位为 arXiv:2602.11574v1 HTML — §4.6 Error Analysis。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-11574:end -->
<!-- review:SF-2026-ARXIV-2602-11574:end -->

<!-- review:SF-2026-ARXIV-2602-11686:start -->
### LAER-MoE: Load-Adaptive Expert Re-layout for Efficient Mixture-of-Experts Training

- **Review route:** `deep`；Primary=`arXiv:2602.11686v1`；owner=`TRAIN-DISTRIBUTED-TRAINING`。

- **问题与旧路径：** `LAER-MoE: Load-Adaptive Expert Re-layout for Efficient Mixture-of-Experts Training` 是否在 `TRAIN-DISTRIBUTED-TRAINING` 中改变已有状态、数据或控制责任；旧路径仍成立于：单机或纯数据并行状态最少、同步语义清晰。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.11686v1 HTML — §3.1. FSEP: Fully Sharded Expert Parallelism` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 训练状态分片、collective、同步与故障恢复。触发约束是：参数、optimizer state 和通信规模越过单设备边界。

- **State / data / control owner：** `TRAIN-DISTRIBUTED-TRAINING` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** Disclosed author artifact: https://github.com/Fizzmy/LAER-MoE-AE; exact manuscript commit/tag Not Disclosed

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.11686v1 HTML — §5.2. End-to-End Performance`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.11686v1 HTML — §7. Discussion`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：模型可装入单机且通信占比高时简单并行仍更优。

<!-- claim:SF-2026-ARXIV-2602-11686:start -->
- **Claim boundary:** 只支持 arXiv:2602.11686v1 实际披露的机制与实验。方法定位为 arXiv:2602.11686v1 HTML — §3.1. FSEP: Fully Sharded Expert Parallelism；验证定位为 arXiv:2602.11686v1 HTML — §5.2. End-to-End Performance；边界定位为 arXiv:2602.11686v1 HTML — §7. Discussion。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-11686:end -->
<!-- review:SF-2026-ARXIV-2602-11686:end -->

<!-- review:SF-2026-ARXIV-2602-11749:start -->
### AIR: Improving Agent Safety through Incident Response

- **Review route:** `deep`；Primary=`arXiv:2602.11749v1`；owner=`PLATFORM-SECURITY`。

- **问题与旧路径：** `AIR: Improving Agent Safety through Incident Response` 是否在 `PLATFORM-SECURITY` 中改变已有状态、数据或控制责任；旧路径仍成立于：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.11749v1 HTML — §3 Method` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 身份、授权、数据流、策略执行点与审计证据。触发约束是：工具、记忆和多 agent 委托把不可信内容转化为可执行控制流。

- **State / data / control owner：** `PLATFORM-SECURITY` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** External link observed in exact-v1 body: https://github.com/langchain-ai/langchain; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.11749v1 HTML — §Appendix C False Positive Evaluation on Safe Tasks`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.11749v1 HTML — §5 Discussion`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：无工具、无持久状态的只读场景仍可采用较薄边界。

<!-- claim:SF-2026-ARXIV-2602-11749:start -->
- **Claim boundary:** 只支持 arXiv:2602.11749v1 实际披露的机制与实验。方法定位为 arXiv:2602.11749v1 HTML — §3 Method；验证定位为 arXiv:2602.11749v1 HTML — §Appendix C False Positive Evaluation on Safe Tasks；边界定位为 arXiv:2602.11749v1 HTML — §5 Discussion。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-11749:end -->
<!-- review:SF-2026-ARXIV-2602-11749:end -->

<!-- review:SF-2026-ARXIV-2602-11786:start -->
### Evaluating LLM Safety Under Repeated Inference via Accelerated Prompt Stress Testing

- **Review route:** `deep`；Primary=`arXiv:2602.11786v1`；owner=`PLATFORM-EVALUATION-SYSTEM`。

- **问题与旧路径：** `Evaluating LLM Safety Under Repeated Inference via Accelerated Prompt Stress Testing` 是否在 `PLATFORM-EVALUATION-SYSTEM` 中改变已有状态、数据或控制责任；旧路径仍成立于：单一离线分数便于比较版本。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.11786v1 HTML — §3 Methodology` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 evaluation contract、覆盖分母、evidence lineage 与 release gate。触发约束是：agent、长时程和多模态系统把失败分散到状态、工具与环境交互链。

- **State / data / control owner：** `PLATFORM-EVALUATION-SYSTEM` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** Not Disclosed — arXiv:2602.11786v1 does not disclose a public repository, release, commit, or executable artifact used by this review

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.11786v1 HTML — §4.3 Phase 2B: Depth-Oriented Evaluation Under Repeated Sampling`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.11786v1 HTML — §A.7 Limitations of LLM-as-judge`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：窄任务且 failure surface 稳定时单指标仍可作为局部信号。

<!-- claim:SF-2026-ARXIV-2602-11786:start -->
- **Claim boundary:** 只支持 arXiv:2602.11786v1 实际披露的机制与实验。方法定位为 arXiv:2602.11786v1 HTML — §3 Methodology；验证定位为 arXiv:2602.11786v1 HTML — §4.3 Phase 2B: Depth-Oriented Evaluation Under Repeated Sampling；边界定位为 arXiv:2602.11786v1 HTML — §A.7 Limitations of LLM-as-judge。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-11786:end -->
<!-- review:SF-2026-ARXIV-2602-11786:end -->

<!-- review:SF-2026-ARXIV-2602-11877:start -->
### Towards Fair and Comprehensive Evaluation of Routers in Collaborative LLM Systems

- **Review route:** `deep`；Primary=`arXiv:2602.11877v1`；owner=`PLATFORM-EVALUATION-SYSTEM`。

- **问题与旧路径：** `Towards Fair and Comprehensive Evaluation of Routers in Collaborative LLM Systems` 是否在 `PLATFORM-EVALUATION-SYSTEM` 中改变已有状态、数据或控制责任；旧路径仍成立于：单一离线分数便于比较版本。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.11877v1 HTML — §4 Methodology` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 evaluation contract、覆盖分母、evidence lineage 与 release gate。触发约束是：agent、长时程和多模态系统把失败分散到状态、工具与环境交互链。

- **State / data / control owner：** `PLATFORM-EVALUATION-SYSTEM` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** External link observed in exact-v1 body: https://github.com/IAAR-Shanghai/xVerify; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.11877v1 HTML — §Router Ability.`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.11877v1 HTML — §Limitations`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：窄任务且 failure surface 稳定时单指标仍可作为局部信号。

<!-- claim:SF-2026-ARXIV-2602-11877:start -->
- **Claim boundary:** 只支持 arXiv:2602.11877v1 实际披露的机制与实验。方法定位为 arXiv:2602.11877v1 HTML — §4 Methodology；验证定位为 arXiv:2602.11877v1 HTML — §Router Ability.；边界定位为 arXiv:2602.11877v1 HTML — §Limitations。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-11877:end -->
<!-- review:SF-2026-ARXIV-2602-11877:end -->

<!-- review:SF-2026-ARXIV-2602-11937:start -->
### Extending Puzzle for Mixture-of-Experts Reasoning Models with Application to GPT-OSS Acceleration

- **Review route:** `deep`；Primary=`arXiv:2602.11937v1`；owner=`MODEL-MOE`。

- **问题与旧路径：** `Extending Puzzle for Mixture-of-Experts Reasoning Models with Application to GPT-OSS Acceleration` 是否在 `MODEL-MOE` 中改变已有状态、数据或控制责任；旧路径仍成立于：dense 层让每个 token 经过同一参数路径，训练与部署最规则。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.11937v1 HTML — §2 Puzzle Optimization` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 expert 选择、capacity、placement 与通信。触发约束是：容量扩大后，激活成本和通信使全参数计算不可持续。

- **State / data / control owner：** `MODEL-MOE` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** External link observed in exact-v1 body: https://github.com/NVIDIA-NeMo/Skills; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.11937v1 HTML — §4.1 Inference Efficiency`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.11937v1 HTML — §5 Discussion`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：规模较小、负载难预测或通信昂贵时 dense 仍可能占优。

<!-- claim:SF-2026-ARXIV-2602-11937:start -->
- **Claim boundary:** 只支持 arXiv:2602.11937v1 实际披露的机制与实验。方法定位为 arXiv:2602.11937v1 HTML — §2 Puzzle Optimization；验证定位为 arXiv:2602.11937v1 HTML — §4.1 Inference Efficiency；边界定位为 arXiv:2602.11937v1 HTML — §5 Discussion。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-11937:end -->
<!-- review:SF-2026-ARXIV-2602-11937:end -->

<!-- review:SF-2026-ARXIV-2602-11964:start -->
### Gaia2: Benchmarking LLM Agents on Dynamic and Asynchronous Environments

- **Review route:** `deep`；Primary=`arXiv:2602.11964v1`；owner=`PLATFORM-EVALUATION-SYSTEM`。

- **问题与旧路径：** `Gaia2: Benchmarking LLM Agents on Dynamic and Asynchronous Environments` 是否在 `PLATFORM-EVALUATION-SYSTEM` 中改变已有状态、数据或控制责任；旧路径仍成立于：单一离线分数便于比较版本。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.11964v1 HTML — §4.2 Scenario design and annotation protocol` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 evaluation contract、覆盖分母、evidence lineage 与 release gate。触发约束是：agent、长时程和多模态系统把失败分散到状态、工具与环境交互链。

- **State / data / control owner：** `PLATFORM-EVALUATION-SYSTEM` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** External link observed in exact-v1 body: https://github.com/eval-sys/mcpmark; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.11964v1 HTML — §5.1 Core results`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.11964v1 HTML — §6 Conclusion & discussion`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：窄任务且 failure surface 稳定时单指标仍可作为局部信号。

<!-- claim:SF-2026-ARXIV-2602-11964:start -->
- **Claim boundary:** 只支持 arXiv:2602.11964v1 实际披露的机制与实验。方法定位为 arXiv:2602.11964v1 HTML — §4.2 Scenario design and annotation protocol；验证定位为 arXiv:2602.11964v1 HTML — §5.1 Core results；边界定位为 arXiv:2602.11964v1 HTML — §6 Conclusion & discussion。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-11964:end -->
<!-- review:SF-2026-ARXIV-2602-11964:end -->

<!-- review:SF-2026-ARXIV-2602-12194:start -->
### MalTool: Malicious Tool Attacks on LLM Agents

- **Review route:** `deep`；Primary=`arXiv:2602.12194v1`；owner=`PLATFORM-SECURITY`。

- **问题与旧路径：** `MalTool: Malicious Tool Attacks on LLM Agents` 是否在 `PLATFORM-SECURITY` 中改变已有状态、数据或控制责任；旧路径仍成立于：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.12194v1 HTML — §5 Our MalTool` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 身份、授权、数据流、策略执行点与审计证据。触发约束是：工具、记忆和多 agent 委托把不可信内容转化为可执行控制流。

- **State / data / control owner：** `PLATFORM-SECURITY` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** External link observed in exact-v1 body: https://github.com/Tencent/AI-Infra-Guard; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.12194v1 HTML — §6 Evaluating MalTool`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.12194v1 HTML — §8 Discussion and Limitations`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：无工具、无持久状态的只读场景仍可采用较薄边界。

<!-- claim:SF-2026-ARXIV-2602-12194:start -->
- **Claim boundary:** 只支持 arXiv:2602.12194v1 实际披露的机制与实验。方法定位为 arXiv:2602.12194v1 HTML — §5 Our MalTool；验证定位为 arXiv:2602.12194v1 HTML — §6 Evaluating MalTool；边界定位为 arXiv:2602.12194v1 HTML — §8 Discussion and Limitations。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-12194:end -->
<!-- review:SF-2026-ARXIV-2602-12194:end -->

<!-- review:SF-2026-ARXIV-2602-12244:start -->
### Any House Any Task: Scalable Long-Horizon Planning for Abstract Human Tasks

- **Review route:** `deep`；Primary=`arXiv:2602.12244v1`；owner=`AGENT-PLANNING`。

- **问题与旧路径：** `Any House Any Task: Scalable Long-Horizon Planning for Abstract Human Tasks` 是否在 `AGENT-PLANNING` 中改变已有状态、数据或控制责任；旧路径仍成立于：按当前 prompt 即时选择下一步，在短任务中无需维护额外 epistemic state。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.12244v1 HTML — §III Overview` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 计划路由、证据需求与停止条件。触发约束是：自演化与长链任务需要区分已知、未知和可验证的下一步。

- **State / data / control owner：** `AGENT-PLANNING` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** Not Disclosed — arXiv:2602.12244v1 does not disclose a public repository, release, commit, or executable artifact used by this review

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.12244v1 HTML — §V-A Inference and Evaluation`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.12244v1 HTML — §VII Conclusion & Limitations`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：目标明确且一步可完成时直接执行仍更稳健。

<!-- claim:SF-2026-ARXIV-2602-12244:start -->
- **Claim boundary:** 只支持 arXiv:2602.12244v1 实际披露的机制与实验。方法定位为 arXiv:2602.12244v1 HTML — §III Overview；验证定位为 arXiv:2602.12244v1 HTML — §V-A Inference and Evaluation；边界定位为 arXiv:2602.12244v1 HTML — §VII Conclusion & Limitations。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-12244:end -->
<!-- review:SF-2026-ARXIV-2602-12244:end -->

<!-- review:SF-2026-ARXIV-2602-12271:start -->
### MonarchRT: Efficient Attention for Real-Time Video Generation

- **Review route:** `deep`；Primary=`arXiv:2602.12271v1`；owner=`INFER-TENSORRT-LLM`。

- **问题与旧路径：** `MonarchRT: Efficient Attention for Real-Time Video Generation` 是否在 `INFER-TENSORRT-LLM` 中改变已有状态、数据或控制责任；旧路径仍成立于：通用 eager 执行便于调试且无需额外编译状态。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.12271v1 HTML — §4.3 Finetuning and Efficient Implementation` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 graph lowering、kernel/precision 选择与执行计划版本。触发约束是：模型规模、算子形态和 SLO 使执行计划、精度与 kernel 选择成为主要成本。

- **State / data / control owner：** `INFER-TENSORRT-LLM` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** External link observed in exact-v1 body: https://github.com/Infini-AI-Lab/MonarchRT; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.12271v1 HTML — §5.3 Efficiency Evaluations`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.12271v1 HTML — §3.1 Approximation Error Analysis`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：工作负载小、形状动态或调试优先时 eager 路径仍合理。

<!-- claim:SF-2026-ARXIV-2602-12271:start -->
- **Claim boundary:** 只支持 arXiv:2602.12271v1 实际披露的机制与实验。方法定位为 arXiv:2602.12271v1 HTML — §4.3 Finetuning and Efficient Implementation；验证定位为 arXiv:2602.12271v1 HTML — §5.3 Efficiency Evaluations；边界定位为 arXiv:2602.12271v1 HTML — §3.1 Approximation Error Analysis。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-12271:end -->
<!-- review:SF-2026-ARXIV-2602-12271:end -->

<!-- review:SF-2026-ARXIV-2602-12281:start -->
### Scaling Verification Can Be More Effective than Scaling Policy Learning for Vision-Language-Action Alignment

- **Review route:** `deep`；Primary=`arXiv:2602.12281v1`；owner=`TRAIN-RLHF`。

- **问题与旧路径：** `Scaling Verification Can Be More Effective than Scaling Policy Learning for Vision-Language-Action Alignment` 是否在 `TRAIN-RLHF` 中改变已有状态、数据或控制责任；旧路径仍成立于：固定后训练配方便于重复和对比。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.12281v1 HTML — §4 Method` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 rollout、reward、policy/reference 与更新 freshness。触发约束是：模型规模、奖励来源和任务 horizon 改变后，同一配方的排序可能反转。

- **State / data / control owner：** `TRAIN-RLHF` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** External link observed in exact-v1 body: https://huggingface.co/juexzz/INTACT-pi0-finetune-bridge; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.12281v1 HTML — §5.4 Simulation Evaluation Results`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.12281v1 HTML — §6 Conclusion`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：反馈稳定、任务窄且分布固定时成熟配方仍可复用。

<!-- claim:SF-2026-ARXIV-2602-12281:start -->
- **Claim boundary:** 只支持 arXiv:2602.12281v1 实际披露的机制与实验。方法定位为 arXiv:2602.12281v1 HTML — §4 Method；验证定位为 arXiv:2602.12281v1 HTML — §5.4 Simulation Evaluation Results；边界定位为 arXiv:2602.12281v1 HTML — §6 Conclusion。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-12281:end -->
<!-- review:SF-2026-ARXIV-2602-12281:end -->

## 4. Benchmark Contracts

None — 作者实验只在各 Source Review 的 evaluation contract 内支持机制判断；本日报不发布可跨 workload 外推的 benchmark claim。

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2602-11882 | score_7_9 | selected | DA-20260214-1 | — | 在同日 eligibility frontier 中优先选择 Total=9 且形成独立 `INFER-TENSORRT-LLM` 系统责任链的 family。 | analysis:DA-20260214-1 |
| SF-2026-ARXIV-2602-11291 | score_7_9 | selected | DA-20260214-2 | — | 在同日 eligibility frontier 中优先选择 Total=8 且形成独立 `MULTIMODAL-WORLD-MODELS` 系统责任链的 family。 | analysis:DA-20260214-2 |
| SF-2026-ARXIV-2602-11301 | score_7_9 | selected | DA-20260214-3 | — | 在同日 eligibility frontier 中优先选择 Total=8 且形成独立 `PLATFORM-SECURITY` 系统责任链的 family。 | analysis:DA-20260214-3 |
| SF-2026-ARXIV-2602-11327 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `PLATFORM-SECURITY`；同 owner 已有更高优先级叙事单元，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-11327 |
| SF-2026-ARXIV-2602-11521 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `INFER-GPU-MEMORY`；跨层影响较已选单元更窄，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-11521 |
| SF-2026-ARXIV-2602-11530 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `INFER-SCHEDULING`；跨层影响较已选单元更窄，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-11530 |
| SF-2026-ARXIV-2602-11543 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `TRAIN-DISTRIBUTED-TRAINING`；跨层影响较已选单元更窄，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-11543 |
| SF-2026-ARXIV-2602-11688 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `INFER-SCHEDULING`；跨层影响较已选单元更窄，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-11688 |
| SF-2026-ARXIV-2602-11790 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `AGENT-WORKFLOW`；跨层影响较已选单元更窄，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-11790 |
| SF-2026-ARXIV-2602-12029 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `INFER-PD-DISAGGREGATION`；跨层影响较已选单元更窄，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-12029 |
| SF-2026-ARXIV-2602-12151 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `INFER-SCHEDULING`；跨层影响较已选单元更窄，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-12151 |
| SF-2026-ARXIV-2602-11184 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `INFER-TENSORRT-LLM`；同 owner 已有更高优先级叙事单元，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-11184 |
| SF-2026-ARXIV-2602-11192 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `INFER-GPU-MEMORY`；跨层影响较已选单元更窄，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-11192 |
| SF-2026-ARXIV-2602-11224 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `PLATFORM-EVALUATION-SYSTEM`；跨层影响较已选单元更窄，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-11224 |
| SF-2026-ARXIV-2602-11287 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `INFER-TENSORRT-LLM`；同 owner 已有更高优先级叙事单元，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-11287 |
| SF-2026-ARXIV-2602-11348 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `PLATFORM-EVALUATION-SYSTEM`；跨层影响较已选单元更窄，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-11348 |
| SF-2026-ARXIV-2602-11456 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `TRAIN-DISTRIBUTED-TRAINING`；跨层影响较已选单元更窄，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-11456 |
| SF-2026-ARXIV-2602-11470 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `PLATFORM-SECURITY`；同 owner 已有更高优先级叙事单元，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-11470 |
| SF-2026-ARXIV-2602-11506 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `PLATFORM-EVALUATION-SYSTEM`；跨层影响较已选单元更窄，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-11506 |
| SF-2026-ARXIV-2602-11510 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `PLATFORM-SECURITY`；同 owner 已有更高优先级叙事单元，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-11510 |
| SF-2026-ARXIV-2602-11513 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `PLATFORM-SECURITY`；同 owner 已有更高优先级叙事单元，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-11513 |
| SF-2026-ARXIV-2602-11574 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `AGENT-PLATFORM`；跨层影响较已选单元更窄，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-11574 |
| SF-2026-ARXIV-2602-11686 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `TRAIN-DISTRIBUTED-TRAINING`；跨层影响较已选单元更窄，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-11686 |
| SF-2026-ARXIV-2602-11749 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `PLATFORM-SECURITY`；同 owner 已有更高优先级叙事单元，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-11749 |
| SF-2026-ARXIV-2602-11786 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `PLATFORM-EVALUATION-SYSTEM`；跨层影响较已选单元更窄，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-11786 |
| SF-2026-ARXIV-2602-11877 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `PLATFORM-EVALUATION-SYSTEM`；跨层影响较已选单元更窄，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-11877 |
| SF-2026-ARXIV-2602-11937 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `MODEL-MOE`；跨层影响较已选单元更窄，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-11937 |
| SF-2026-ARXIV-2602-11964 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `PLATFORM-EVALUATION-SYSTEM`；跨层影响较已选单元更窄，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-11964 |
| SF-2026-ARXIV-2602-12194 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `PLATFORM-SECURITY`；同 owner 已有更高优先级叙事单元，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-12194 |
| SF-2026-ARXIV-2602-12244 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `AGENT-PLANNING`；跨层影响较已选单元更窄，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-12244 |
| SF-2026-ARXIV-2602-12271 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `INFER-TENSORRT-LLM`；同 owner 已有更高优先级叙事单元，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-12271 |
| SF-2026-ARXIV-2602-12281 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `TRAIN-RLHF`；跨层影响较已选单元更窄，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-12281 |

<!-- analysis:DA-20260214-1:start -->
### DA-20260214-1 — Where Bits Matter in World Model Planning: A Paired Mixed-Bit Study for Efficient Spatial Reasoning

旧路径在原 workload 下保持较低状态与控制开销；约束变化后，该 family 把新增机制责任定位到 `INFER-TENSORRT-LLM`。exact-v1 的 `arXiv:2602.11882v1 HTML — §Quantization implementation details.` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 graph lowering、kernel/precision 选择与执行计划版本。触发约束是：模型规模、算子形态和 SLO 使执行计划、精度与 kernel 选择成为主要成本。 公开验证定位在 `arXiv:2602.11882v1 HTML — §Evaluation protocol.`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。 代价、failure mode 与旧方案共存边界由以下证据限制：限制或反证定位在 `arXiv:2602.11882v1 HTML — §5 Discussion, Limitations, and Outlook`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：工作负载小、形状动态或调试优先时 eager 路径仍合理。
<!-- analysis:DA-20260214-1:end -->

<!-- analysis:DA-20260214-2:start -->
### DA-20260214-2 — H-WM: Robotic Task and Motion Planning Guided by Hierarchical World Model

旧路径在原 workload 下保持较低状态与控制开销；约束变化后，该 family 把新增机制责任定位到 `MULTIMODAL-WORLD-MODELS`。exact-v1 的 `arXiv:2602.11291v1 HTML — §4.3 Pipeline for VLA under Hierarchical World Model Guidance` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 latent state、action-conditioned transition 与 rollout commitment。触发约束是：规划与闭环评估要求预测 action-conditioned transition，而非只生成逼真视频。 公开验证定位在 `arXiv:2602.11291v1 HTML — §5.2 Benchmark and evaluation`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。 代价、failure mode 与旧方案共存边界由以下证据限制：限制或反证定位在 `arXiv:2602.11291v1 HTML — §7 Limitations`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：只需内容生成而不需要因果控制时普通 video model 仍足够。
<!-- analysis:DA-20260214-2:end -->

<!-- analysis:DA-20260214-3:start -->
### DA-20260214-3 — The PBSAI Governance Ecosystem: A Multi-Agent AI Reference Architecture for Securing Enterprise AI Estates

旧路径在原 workload 下保持较低状态与控制开销；约束变化后，该 family 把新增机制责任定位到 `PLATFORM-SECURITY`。exact-v1 的 `arXiv:2602.11301v1 PDF — §3 Architecture Overview: 12-Domain Ecosystem and Minimal Stack` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 身份、授权、数据流、策略执行点与审计证据。触发约束是：工具、记忆和多 agent 委托把不可信内容转化为可执行控制流。 exact-v1 未披露可独立定位的 evaluation（`Not Disclosed — exact-v1 PDF 全文已审计但未提供独立 Evaluation 章节`）；因此不声称经验收益。已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。 代价、failure mode 与旧方案共存边界由以下证据限制：限制或反证定位在 `arXiv:2602.11301v1 PDF — §7 Discussion and Conclusion`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：无工具、无持久状态的只读场景仍可采用较薄边界。
<!-- analysis:DA-20260214-3:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-11327:start -->
`Security Threat Modeling for Emerging AI-Agent Protocols: A Comparative Analysis of MCP, A2A, Agora, and ANP` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-11327:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-11521:start -->
`PAM: Processing Across Memory Hierarchy for Efficient KV-centric LLM Serving System` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-11521:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-11530:start -->
`PASCAL: A Phase-Aware Scheduling Algorithm for Serving Reasoning-based Large Language Models` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-11530:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-11543:start -->
`Pretraining A Large Language Model using Distributed GPUs: A Memory-Efficient Decentralized Paradigm` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-11543:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-11688:start -->
`GORGO: Online Tuning for Cross-Region Network-Aware LLM Serving` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-11688:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-11790:start -->
`Beyond End-to-End Video Models: An LLM-Based Multi-Agent System for Educational Video Generation` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-11790:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-12029:start -->
`PrefillShare: A Shared Prefill Module for KV Reuse in Multi-LLM Disaggregated Serving` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-12029:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-12151:start -->
`OServe: Accelerating LLM Serving via Spatial-Temporal Workload Orchestration` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-12151:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-11184:start -->
`KBVQ-MoE: KLT-guided SVD with Bias-Corrected Vector Quantization for MoE Large Language Models` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-11184:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-11192:start -->
`MELINOE: Fine-Tuning Enables Memory-Efficient Inference for Mixture-of-Experts Models` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-11192:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-11224:start -->
`Agent-Diff: Benchmarking LLM Agents on Enterprise API Tasks via Code Execution with State-Diff-Based Evaluation` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-11224:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-11287:start -->
`HiFloat4 Format for Language Model Inference` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-11287:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-11348:start -->
`AgentNoiseBench: Benchmarking Robustness of Tool-Using LLM Agents Under Noisy Condition` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-11348:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-11456:start -->
`AuroraRL: Fast, Fault-Tolerant, and Cost-Efficient Reinforcement Learning over Decentralized Network` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-11456:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-11470:start -->
`Cachemir: Fully Homomorphic Encrypted Inference of Generative Large Language Model with KV Cache` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-11470:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-11506:start -->
`RooflineBench: A Benchmarking Framework for On-Device LLMs via Roofline Analysis` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-11506:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-11510:start -->
`AgentLeak: A Benchmark for Internal-Channel Privacy Leakage in Multi-Agent LLM Systems` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-11510:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-11513:start -->
`Differentially Private and Communication Efficient Large Language Model Split Inference via Stochastic Quantization and Soft Prompt` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-11513:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-11574:start -->
`Learning to Configure Agentic AI Systems` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-11574:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-11686:start -->
`LAER-MoE: Load-Adaptive Expert Re-layout for Efficient Mixture-of-Experts Training` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-11686:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-11749:start -->
`AIR: Improving Agent Safety through Incident Response` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-11749:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-11786:start -->
`Evaluating LLM Safety Under Repeated Inference via Accelerated Prompt Stress Testing` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-11786:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-11877:start -->
`Towards Fair and Comprehensive Evaluation of Routers in Collaborative LLM Systems` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-11877:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-11937:start -->
`Extending Puzzle for Mixture-of-Experts Reasoning Models with Application to GPT-OSS Acceleration` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-11937:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-11964:start -->
`Gaia2: Benchmarking LLM Agents on Dynamic and Asynchronous Environments` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-11964:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-12194:start -->
`MalTool: Malicious Tool Attacks on LLM Agents` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-12194:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-12244:start -->
`Any House Any Task: Scalable Long-Horizon Planning for Abstract Human Tasks` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-12244:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-12271:start -->
`MonarchRT: Efficient Attention for Real-Time Video Generation` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-12271:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-12281:start -->
`Scaling Verification Can Be More Effective than Scaling Policy Learning for Vision-Language-Action Alignment` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-12281:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2602-11882 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#trade-off (line 1235) | books/part-05-inference-system/48-speculative-decoding.md#本章要回答的问题 (line 10); books/part-05-inference-system/50-vllm.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-11882 | delta:SF-2026-ARXIV-2602-11882 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-11882 |
| SF-2026-ARXIV-2602-11291 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#演进路线 (line 107) | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#本章要回答的问题 (line 10); books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-11291 | delta:SF-2026-ARXIV-2602-11291 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-11291 |
| SF-2026-ARXIV-2602-11301 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#风险管理而不是一次性认证 (line 1106) | books/part-06-ai-infrastructure/71-multi-tenant.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/73-production-best-practice.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-11301 | delta:SF-2026-ARXIV-2602-11301 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-11301 |
| SF-2026-ARXIV-2602-11327 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#风险管理而不是一次性认证 (line 1106) | books/part-06-ai-infrastructure/71-multi-tenant.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/73-production-best-practice.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-11327 | delta:SF-2026-ARXIV-2602-11327 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-11327 |
| SF-2026-ARXIV-2602-11521 | INFER-GPU-MEMORY | books/part-05-inference-system/54-gpu-memory.md#硬件升级不是最终答案 (line 333) | books/part-05-inference-system/53-kserve-llm.md#本章要回答的问题 (line 10); books/part-05-inference-system/55-pd-disaggregation.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-11521 | delta:SF-2026-ARXIV-2602-11521 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-11521 |
| SF-2026-ARXIV-2602-11530 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#iteration-scheduling (line 251) | books/part-05-inference-system/55-pd-disaggregation.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/57-what-is-ai-platform.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-11530 | delta:SF-2026-ARXIV-2602-11530 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-11530 |
| SF-2026-ARXIV-2602-11543 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#variable-length-batch-让并行计划成为-runtime-state (line 976) | books/part-04-training-system/35-checkpoint.md#本章要回答的问题 (line 10); books/part-04-training-system/37-tensor-parallel.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-11543 | delta:SF-2026-ARXIV-2602-11543 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-11543 |
| SF-2026-ARXIV-2602-11688 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#routingplacement-与-autoscaling (line 303) | books/part-05-inference-system/55-pd-disaggregation.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/57-what-is-ai-platform.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-11688 | delta:SF-2026-ARXIV-2602-11688 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-11688 |
| SF-2026-ARXIV-2602-11790 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#deterministic-spineagentic-nodes (line 102) | books/part-07-agent/80-reflection.md#本章要回答的问题 (line 10); books/part-07-agent/82-multi-agent.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-11790 | delta:SF-2026-ARXIV-2602-11790 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-11790 |
| SF-2026-ARXIV-2602-12029 | INFER-PD-DISAGGREGATION | books/part-05-inference-system/55-pd-disaggregation.md#transfer-cost-下界 (line 106) | books/part-05-inference-system/54-gpu-memory.md#本章要回答的问题 (line 10); books/part-05-inference-system/56-inference-scheduling.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-12029 | delta:SF-2026-ARXIV-2602-12029 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-12029 |
| SF-2026-ARXIV-2602-12151 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#routingplacement-与-autoscaling (line 510) | books/part-05-inference-system/55-pd-disaggregation.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/57-what-is-ai-platform.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-12151 | delta:SF-2026-ARXIV-2602-12151 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-12151 |
| SF-2026-ARXIV-2602-11184 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#量化为什么不自动带来加速 (line 570) | books/part-05-inference-system/48-speculative-decoding.md#本章要回答的问题 (line 10); books/part-05-inference-system/50-vllm.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-11184 | delta:SF-2026-ARXIV-2602-11184 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-11184 |
| SF-2026-ARXIV-2602-11192 | INFER-GPU-MEMORY | books/part-05-inference-system/54-gpu-memory.md#三类缓解路径 (line 297) | books/part-05-inference-system/53-kserve-llm.md#本章要回答的问题 (line 10); books/part-05-inference-system/55-pd-disaggregation.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-11192 | delta:SF-2026-ARXIV-2602-11192 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-11192 |
| SF-2026-ARXIV-2602-11224 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#从答案评分到可执行证据 (line 950) | books/part-06-ai-infrastructure/65-kai-scheduler.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/67-monitoring.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-11224 | delta:SF-2026-ARXIV-2602-11224 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-11224 |
| SF-2026-ARXIV-2602-11287 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#build-time-与-runtime-time (line 953) | books/part-05-inference-system/48-speculative-decoding.md#本章要回答的问题 (line 10); books/part-05-inference-system/50-vllm.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-11287 | delta:SF-2026-ARXIV-2602-11287 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-11287 |
| SF-2026-ARXIV-2602-11348 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#评估对象有四个层次 (line 689) | books/part-06-ai-infrastructure/65-kai-scheduler.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/67-monitoring.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-11348 | delta:SF-2026-ARXIV-2602-11348 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-11348 |
| SF-2026-ARXIV-2602-11456 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#failure-不再是单进程退出 (line 749) | books/part-04-training-system/35-checkpoint.md#本章要回答的问题 (line 10); books/part-04-training-system/37-tensor-parallel.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-11456 | delta:SF-2026-ARXIV-2602-11456 | Principle Reuse | Integrate | books-review:SF-2026-ARXIV-2602-11456 |
| SF-2026-ARXIV-2602-11470 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#风险管理而不是一次性认证 (line 1137) | books/part-06-ai-infrastructure/71-multi-tenant.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/73-production-best-practice.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-11470 | delta:SF-2026-ARXIV-2602-11470 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-11470 |
| SF-2026-ARXIV-2602-11506 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#评估对象有四个层次 (line 737) | books/part-06-ai-infrastructure/65-kai-scheduler.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/67-monitoring.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-11506 | delta:SF-2026-ARXIV-2602-11506 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-11506 |
| SF-2026-ARXIV-2602-11510 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#从-trace-检查到受限状态空间验证 (line 573) | books/part-06-ai-infrastructure/71-multi-tenant.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/73-production-best-practice.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-11510 | delta:SF-2026-ARXIV-2602-11510 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-11510 |
| SF-2026-ARXIV-2602-11513 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#风险管理而不是一次性认证 (line 1149) | books/part-06-ai-infrastructure/71-multi-tenant.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/73-production-best-practice.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-11513 | delta:SF-2026-ARXIV-2602-11513 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-11513 |
| SF-2026-ARXIV-2602-11574 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#scheduling-不只是-gpu (line 536) | books/part-07-agent/83-mcp.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-11574 | delta:SF-2026-ARXIV-2602-11574 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-11574 |
| SF-2026-ARXIV-2602-11686 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#每种并行直接切什么 (line 517) | books/part-04-training-system/35-checkpoint.md#本章要回答的问题 (line 10); books/part-04-training-system/37-tensor-parallel.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-11686 | delta:SF-2026-ARXIV-2602-11686 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-11686 |
| SF-2026-ARXIV-2602-11749 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#风险管理而不是一次性认证 (line 1073) | books/part-06-ai-infrastructure/71-multi-tenant.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/73-production-best-practice.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-11749 | delta:SF-2026-ARXIV-2602-11749 | Principle Reuse | Integrate | books-review:SF-2026-ARXIV-2602-11749 |
| SF-2026-ARXIV-2602-11786 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#action-control-需要-sensitivity-与-invariance-双臂证据 (line 2487) | books/part-06-ai-infrastructure/65-kai-scheduler.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/67-monitoring.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-11786 | delta:SF-2026-ARXIV-2602-11786 | Principle Reuse | Integrate | books-review:SF-2026-ARXIV-2602-11786 |
| SF-2026-ARXIV-2602-11877 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#从目标到证据而不是从指标到目标 (line 123) | books/part-06-ai-infrastructure/65-kai-scheduler.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/67-monitoring.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-11877 | delta:SF-2026-ARXIV-2602-11877 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-11877 |
| SF-2026-ARXIV-2602-11937 | MODEL-MOE | books/part-02-model/21-moe.md#从参数化-router-到带检索记忆的-router (line 473) | books/part-02-model/20-sampling.md#本章要回答的问题 (line 10); books/part-02-model/22-long-context.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-11937 | delta:SF-2026-ARXIV-2602-11937 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-11937 |
| SF-2026-ARXIV-2602-11964 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#评估对象有四个层次 (line 534) | books/part-06-ai-infrastructure/65-kai-scheduler.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/67-monitoring.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-11964 | delta:SF-2026-ARXIV-2602-11964 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-11964 |
| SF-2026-ARXIV-2602-12194 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#从-trace-检查到受限状态空间验证 (line 573) | books/part-06-ai-infrastructure/71-multi-tenant.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/73-production-best-practice.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-12194 | delta:SF-2026-ARXIV-2602-12194 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-12194 |
| SF-2026-ARXIV-2602-12244 | AGENT-PLANNING | books/part-07-agent/79-planning.md#goalconstraint-与-policy (line 252) | books/part-07-agent/78-tool-calling.md#本章要回答的问题 (line 10); books/part-07-agent/80-reflection.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-12244 | delta:SF-2026-ARXIV-2602-12244 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-12244 |
| SF-2026-ARXIV-2602-12271 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#专用加速器首先是一份-workload-contract (line 1102) | books/part-05-inference-system/48-speculative-decoding.md#本章要回答的问题 (line 10); books/part-05-inference-system/50-vllm.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-12271 | delta:SF-2026-ARXIV-2602-12271 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-12271 |
| SF-2026-ARXIV-2602-12281 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#evaluation-必须独立于-reward-model (line 539) | books/part-04-training-system/30-lora.md#本章要回答的问题 (line 10); books/part-04-training-system/32-ppo.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-12281 | delta:SF-2026-ARXIV-2602-12281 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-12281 |

<!-- existing:SF-2026-ARXIV-2602-11882:start -->
已对读当前 owner `INFER-TENSORRT-LLM` 在 `books/part-05-inference-system/49-tensorrt-llm.md#trade-off (line 1235)` 的命题：### Quantization Correctness 不能只看 Accuracy
<!-- existing:SF-2026-ARXIV-2602-11882:end -->

<!-- delta:SF-2026-ARXIV-2602-11882:start -->
exact-v1 的 `arXiv:2602.11882v1 HTML — §Quantization implementation details.` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 graph lowering、kernel/precision 选择与执行计划版本。触发约束是：模型规模、算子形态和 SLO 使执行计划、精度与 kernel 选择成为主要成本。
<!-- delta:SF-2026-ARXIV-2602-11882:end -->

<!-- books-review:SF-2026-ARXIV-2602-11882:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-05-inference-system/48-speculative-decoding.md#本章要回答的问题 (line 10); books/part-05-inference-system/50-vllm.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.11882v1 实际披露的机制与实验。方法定位为 arXiv:2602.11882v1 HTML — §Quantization implementation details.；验证定位为 arXiv:2602.11882v1 HTML — §Evaluation protocol.；边界定位为 arXiv:2602.11882v1 HTML — §5 Discussion, Limitations, and Outlook。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-11882:end -->

<!-- existing:SF-2026-ARXIV-2602-11291:start -->
已对读当前 owner `MULTIMODAL-WORLD-MODELS` 在 `books/part-03-multimodal-world-models/25-multimodal-world-models.md#演进路线 (line 107)` 的命题：### 从单尺度预测到 Abstraction × Timescale Hierarchy
<!-- existing:SF-2026-ARXIV-2602-11291:end -->

<!-- delta:SF-2026-ARXIV-2602-11291:start -->
exact-v1 的 `arXiv:2602.11291v1 HTML — §4.3 Pipeline for VLA under Hierarchical World Model Guidance` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 latent state、action-conditioned transition 与 rollout commitment。触发约束是：规划与闭环评估要求预测 action-conditioned transition，而非只生成逼真视频。
<!-- delta:SF-2026-ARXIV-2602-11291:end -->

<!-- books-review:SF-2026-ARXIV-2602-11291:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#本章要回答的问题 (line 10); books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.11291v1 实际披露的机制与实验。方法定位为 arXiv:2602.11291v1 HTML — §4.3 Pipeline for VLA under Hierarchical World Model Guidance；验证定位为 arXiv:2602.11291v1 HTML — §5.2 Benchmark and evaluation；边界定位为 arXiv:2602.11291v1 HTML — §7 Limitations。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-11291:end -->

<!-- existing:SF-2026-ARXIV-2602-11301:start -->
已对读当前 owner `PLATFORM-SECURITY` 在 `books/part-06-ai-infrastructure/72-security.md#风险管理而不是一次性认证 (line 1106)` 的命题：### Agent authority BOM、channel coverage 与 executable PoV
<!-- existing:SF-2026-ARXIV-2602-11301:end -->

<!-- delta:SF-2026-ARXIV-2602-11301:start -->
exact-v1 的 `arXiv:2602.11301v1 PDF — §3 Architecture Overview: 12-Domain Ecosystem and Minimal Stack` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 身份、授权、数据流、策略执行点与审计证据。触发约束是：工具、记忆和多 agent 委托把不可信内容转化为可执行控制流。
<!-- delta:SF-2026-ARXIV-2602-11301:end -->

<!-- books-review:SF-2026-ARXIV-2602-11301:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-06-ai-infrastructure/71-multi-tenant.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/73-production-best-practice.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.11301v1 实际披露的机制与实验。方法定位为 arXiv:2602.11301v1 PDF — §3 Architecture Overview: 12-Domain Ecosystem and Minimal Stack；evaluation facet 未独立披露，不声称经验收益；边界定位为 arXiv:2602.11301v1 PDF — §7 Discussion and Conclusion。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-11301:end -->

<!-- existing:SF-2026-ARXIV-2602-11327:start -->
已对读当前 owner `PLATFORM-SECURITY` 在 `books/part-06-ai-infrastructure/72-security.md#风险管理而不是一次性认证 (line 1106)` 的命题：### Agent authority BOM、channel coverage 与 executable PoV
<!-- existing:SF-2026-ARXIV-2602-11327:end -->

<!-- delta:SF-2026-ARXIV-2602-11327:start -->
exact-v1 的 `arXiv:2602.11327v1 HTML — §6.1 Assessment Methodology` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 身份、授权、数据流、策略执行点与审计证据。触发约束是：工具、记忆和多 agent 委托把不可信内容转化为可执行控制流。
<!-- delta:SF-2026-ARXIV-2602-11327:end -->

<!-- books-review:SF-2026-ARXIV-2602-11327:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-06-ai-infrastructure/71-multi-tenant.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/73-production-best-practice.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.11327v1 实际披露的机制与实验。方法定位为 arXiv:2602.11327v1 HTML — §6.1 Assessment Methodology；验证定位为 arXiv:2602.11327v1 HTML — §6.2 Lifecycle-Based Evaluation Framework；边界定位为 arXiv:2602.11327v1 HTML — §4.1.4 Absence of limitations on token lifetime。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-11327:end -->

<!-- existing:SF-2026-ARXIV-2602-11521:start -->
已对读当前 owner `INFER-GPU-MEMORY` 在 `books/part-05-inference-system/54-gpu-memory.md#硬件升级不是最终答案 (line 333)` 的命题：### 从单设备 HBM 到异构近数据与池化状态
<!-- existing:SF-2026-ARXIV-2602-11521:end -->

<!-- delta:SF-2026-ARXIV-2602-11521:start -->
exact-v1 的 `arXiv:2602.11521v1 HTML — §4. PAM: System Overview` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 权重、KV、临时张量的 placement、lifetime 与迁移控制。触发约束是：容量、带宽和并发超过单设备预算后，放置、迁移与回收成为控制问题。
<!-- delta:SF-2026-ARXIV-2602-11521:end -->

<!-- books-review:SF-2026-ARXIV-2602-11521:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-05-inference-system/53-kserve-llm.md#本章要回答的问题 (line 10); books/part-05-inference-system/55-pd-disaggregation.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.11521v1 实际披露的机制与实验。方法定位为 arXiv:2602.11521v1 HTML — §4. PAM: System Overview；验证定位为 arXiv:2602.11521v1 HTML — §7.1. Evaluation Methodology；边界定位为 arXiv:2602.11521v1 HTML — §3.1. Limitations of Layered PIM。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-11521:end -->

<!-- existing:SF-2026-ARXIV-2602-11530:start -->
已对读当前 owner `INFER-SCHEDULING` 在 `books/part-05-inference-system/56-inference-scheduling.md#iteration-scheduling (line 251)` 的命题：### Exclusive Batching 的 Phase Switch 是 Workload-dependent State
<!-- existing:SF-2026-ARXIV-2602-11530:end -->

<!-- delta:SF-2026-ARXIV-2602-11530:start -->
exact-v1 的 `arXiv:2602.11530v1 HTML — §III-A Methodology` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 准入、批处理、优先级、路由和资源选择。触发约束是：长度、阶段、SLO、模型和 agent fan-out 的异质性使排队决策决定整体尾延迟。
<!-- delta:SF-2026-ARXIV-2602-11530:end -->

<!-- books-review:SF-2026-ARXIV-2602-11530:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-05-inference-system/55-pd-disaggregation.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/57-what-is-ai-platform.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.11530v1 实际披露的机制与实验。方法定位为 arXiv:2602.11530v1 HTML — §III-A Methodology；验证定位为 arXiv:2602.11530v1 HTML — §V-B User Experience (TTFT, SLO Violation) and Throughput；边界定位为 arXiv:2602.11530v1 HTML — §VII Future work。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-11530:end -->

<!-- existing:SF-2026-ARXIV-2602-11543:start -->
已对读当前 owner `TRAIN-DISTRIBUTED-TRAINING` 在 `books/part-04-training-system/36-distributed-training.md#variable-length-batch-让并行计划成为-runtime-state (line 976)` 的命题：### 无中心异步聚合必须守恒在途质量
<!-- existing:SF-2026-ARXIV-2602-11543:end -->

<!-- delta:SF-2026-ARXIV-2602-11543:start -->
exact-v1 的 `arXiv:2602.11543v1 HTML — §3.2 Overall Framework` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 训练状态分片、collective、同步与故障恢复。触发约束是：参数、optimizer state 和通信规模越过单设备边界。
<!-- delta:SF-2026-ARXIV-2602-11543:end -->

<!-- books-review:SF-2026-ARXIV-2602-11543:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-04-training-system/35-checkpoint.md#本章要回答的问题 (line 10); books/part-04-training-system/37-tensor-parallel.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.11543v1 实际披露的机制与实验。方法定位为 arXiv:2602.11543v1 HTML — §3.2 Overall Framework；验证定位为 arXiv:2602.11543v1 HTML — §4.2 Main Results；边界定位为 arXiv:2602.11543v1 HTML — §5 Conclusion。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-11543:end -->

<!-- existing:SF-2026-ARXIV-2602-11688:start -->
已对读当前 owner `INFER-SCHEDULING` 在 `books/part-05-inference-system/56-inference-scheduling.md#routingplacement-与-autoscaling (line 303)` 的命题：### 低带宽拓扑要联合预算 Hops、Bytes 与 Steps
<!-- existing:SF-2026-ARXIV-2602-11688:end -->

<!-- delta:SF-2026-ARXIV-2602-11688:start -->
exact-v1 的 `arXiv:2602.11688v1 HTML — §3.2 Design objective and signal requirements` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 准入、批处理、优先级、路由和资源选择。触发约束是：长度、阶段、SLO、模型和 agent fan-out 的异质性使排队决策决定整体尾延迟。
<!-- delta:SF-2026-ARXIV-2602-11688:end -->

<!-- books-review:SF-2026-ARXIV-2602-11688:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-05-inference-system/55-pd-disaggregation.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/57-what-is-ai-platform.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.11688v1 实际披露的机制与实验。方法定位为 arXiv:2602.11688v1 HTML — §3.2 Design objective and signal requirements；验证定位为 arXiv:2602.11688v1 HTML — §4 Experimental Evaluation；边界定位为 arXiv:2602.11688v1 HTML — §Methodological limitations.。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-11688:end -->

<!-- existing:SF-2026-ARXIV-2602-11790:start -->
已对读当前 owner `AGENT-WORKFLOW` 在 `books/part-07-agent/81-workflow.md#deterministic-spineagentic-nodes (line 102)` 的命题：## Deterministic Spine，Agentic Nodes
<!-- existing:SF-2026-ARXIV-2602-11790:end -->

<!-- delta:SF-2026-ARXIV-2602-11790:start -->
exact-v1 的 `arXiv:2602.11790v1 HTML — §4.1. System Overview` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 workflow graph、checkpoint、重试与演进状态。触发约束是：长任务、失败恢复和运行时重写要求控制流成为可验证、可持久化的对象。
<!-- delta:SF-2026-ARXIV-2602-11790:end -->

<!-- books-review:SF-2026-ARXIV-2602-11790:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-07-agent/80-reflection.md#本章要回答的问题 (line 10); books/part-07-agent/82-multi-agent.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.11790v1 实际披露的机制与实验。方法定位为 arXiv:2602.11790v1 HTML — §4.1. System Overview；验证定位为 arXiv:2602.11790v1 HTML — §5.2. Main Results；边界定位为 arXiv:2602.11790v1 HTML — §5.4. Error Analysis。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-11790:end -->

<!-- existing:SF-2026-ARXIV-2602-12029:start -->
已对读当前 owner `INFER-PD-DISAGGREGATION` 在 `books/part-05-inference-system/55-pd-disaggregation.md#transfer-cost-下界 (line 106)` 的命题：### 从 Full Transfer 到 Demand-corrected Selective Transfer
<!-- existing:SF-2026-ARXIV-2602-12029:end -->

<!-- delta:SF-2026-ARXIV-2602-12029:start -->
exact-v1 的 `arXiv:2602.12029v1 HTML — §3 Method` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 阶段拆分、KV handoff 与资源池选择。触发约束是：多轮请求的阶段成本和到达分布分化，使单一资源池难同时满足 TTFT 与 TPOT。
<!-- delta:SF-2026-ARXIV-2602-12029:end -->

<!-- books-review:SF-2026-ARXIV-2602-12029:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-05-inference-system/54-gpu-memory.md#本章要回答的问题 (line 10); books/part-05-inference-system/56-inference-scheduling.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.12029v1 实际披露的机制与实验。方法定位为 arXiv:2602.12029v1 HTML — §3 Method；验证定位为 arXiv:2602.12029v1 HTML — §B.3 Results with a different backbone model；独立 limitations 未披露，因而采用更窄主张。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-12029:end -->

<!-- existing:SF-2026-ARXIV-2602-12151:start -->
已对读当前 owner `INFER-SCHEDULING` 在 `books/part-05-inference-system/56-inference-scheduling.md#routingplacement-与-autoscaling (line 510)` 的命题：### 异质 DAG 需要 Readiness、Residency 与 Deadline 共享一条控制链
<!-- existing:SF-2026-ARXIV-2602-12151:end -->

<!-- delta:SF-2026-ARXIV-2602-12151:start -->
exact-v1 的 `arXiv:2602.12151v1 HTML — §5.4 Algorithm Efficiency` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 准入、批处理、优先级、路由和资源选择。触发约束是：长度、阶段、SLO、模型和 agent fan-out 的异质性使排队决策决定整体尾延迟。
<!-- delta:SF-2026-ARXIV-2602-12151:end -->

<!-- books-review:SF-2026-ARXIV-2602-12151:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-05-inference-system/55-pd-disaggregation.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/57-what-is-ai-platform.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.12151v1 实际披露的机制与实验。方法定位为 arXiv:2602.12151v1 HTML — §5.4 Algorithm Efficiency；验证定位为 arXiv:2602.12151v1 HTML — §5.3 Case and Ablation Studies；边界定位为 arXiv:2602.12151v1 HTML — §Appendix C Extended Discussion。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-12151:end -->

<!-- existing:SF-2026-ARXIV-2602-11184:start -->
已对读当前 owner `INFER-TENSORRT-LLM` 在 `books/part-05-inference-system/49-tensorrt-llm.md#量化为什么不自动带来加速 (line 570)` 的命题：### MoE 的 Calibration Identity 必须覆盖 Expert Activation Distribution
<!-- existing:SF-2026-ARXIV-2602-11184:end -->

<!-- delta:SF-2026-ARXIV-2602-11184:start -->
exact-v1 的 `arXiv:2602.11184v1 HTML — §2.2 MoE LLMs Compression Methods` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 graph lowering、kernel/precision 选择与执行计划版本。触发约束是：模型规模、算子形态和 SLO 使执行计划、精度与 kernel 选择成为主要成本。
<!-- delta:SF-2026-ARXIV-2602-11184:end -->

<!-- books-review:SF-2026-ARXIV-2602-11184:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-05-inference-system/48-speculative-decoding.md#本章要回答的问题 (line 10); books/part-05-inference-system/50-vllm.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.11184v1 实际披露的机制与实验。方法定位为 arXiv:2602.11184v1 HTML — §2.2 MoE LLMs Compression Methods；验证定位为 arXiv:2602.11184v1 HTML — §Main results.；边界定位为 arXiv:2602.11184v1 HTML — §A.12 Limitations。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-11184:end -->

<!-- existing:SF-2026-ARXIV-2602-11192:start -->
已对读当前 owner `INFER-GPU-MEMORY` 在 `books/part-05-inference-system/54-gpu-memory.md#三类缓解路径 (line 297)` 的命题：### Weights 与 KV 的联合 HBM 预算：可提交的运行时精度页
<!-- existing:SF-2026-ARXIV-2602-11192:end -->

<!-- delta:SF-2026-ARXIV-2602-11192:start -->
exact-v1 的 `arXiv:2602.11192v1 HTML — §3 Method` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 权重、KV、临时张量的 placement、lifetime 与迁移控制。触发约束是：容量、带宽和并发超过单设备预算后，放置、迁移与回收成为控制问题。
<!-- delta:SF-2026-ARXIV-2602-11192:end -->

<!-- books-review:SF-2026-ARXIV-2602-11192:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-05-inference-system/53-kserve-llm.md#本章要回答的问题 (line 10); books/part-05-inference-system/55-pd-disaggregation.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.11192v1 实际披露的机制与实验。方法定位为 arXiv:2602.11192v1 HTML — §3 Method；验证定位为 arXiv:2602.11192v1 HTML — §4.2 Main Results；边界定位为 arXiv:2602.11192v1 HTML — §5 Conclusion。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-11192:end -->

<!-- existing:SF-2026-ARXIV-2602-11224:start -->
已对读当前 owner `PLATFORM-EVALUATION-SYSTEM` 在 `books/part-06-ai-infrastructure/66-evaluation-system.md#从答案评分到可执行证据 (line 950)` 的命题：## 从答案评分到可执行证据
<!-- existing:SF-2026-ARXIV-2602-11224:end -->

<!-- delta:SF-2026-ARXIV-2602-11224:start -->
exact-v1 的 `arXiv:2602.11224v1 HTML — §3. Agent-Diff` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 evaluation contract、覆盖分母、evidence lineage 与 release gate。触发约束是：agent、长时程和多模态系统把失败分散到状态、工具与环境交互链。
<!-- delta:SF-2026-ARXIV-2602-11224:end -->

<!-- books-review:SF-2026-ARXIV-2602-11224:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-06-ai-infrastructure/65-kai-scheduler.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/67-monitoring.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.11224v1 实际披露的机制与实验。方法定位为 arXiv:2602.11224v1 HTML — §3. Agent-Diff；验证定位为 arXiv:2602.11224v1 HTML — §4. Evaluation Methodology；边界定位为 arXiv:2602.11224v1 HTML — §6.3. Failure and Recovery Modes。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-11224:end -->

<!-- existing:SF-2026-ARXIV-2602-11287:start -->
已对读当前 owner `INFER-TENSORRT-LLM` 在 `books/part-05-inference-system/49-tensorrt-llm.md#build-time-与-runtime-time (line 953)` 的命题：固定一种低比特格式便于 kernel 与 artifact 管理，但训练和 direct-cast inference 对 exponent range 与 mantissa precision 的压力并不相同。可切换模式的 microscaling block 让同一量化家族在训练阶段保留更细尾数、在推理阶段扩大动态范围；因此执行计划必须把 block size、shared scale、mode、目标硬件和转换阶段共同写入 format identity。收益是减少重复校准路径，代价是 kernel 分支、验证矩阵与跨设备可移植性变复杂；模式判断错误会把局部溢出或舍入误差扩散到整块。硬件不支持该布局或 workload 分布稳定时，单一格式仍是更可审计的选择。当前证据只覆盖作者披露的格式与任务，不能外推为任意模型上的通用精度收益。
<!-- existing:SF-2026-ARXIV-2602-11287:end -->

<!-- delta:SF-2026-ARXIV-2602-11287:start -->
exact-v1 的 `arXiv:2602.11287v1 HTML — §II HiFloat4` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 graph lowering、kernel/precision 选择与执行计划版本。触发约束是：模型规模、算子形态和 SLO 使执行计划、精度与 kernel 选择成为主要成本。
<!-- delta:SF-2026-ARXIV-2602-11287:end -->

<!-- books-review:SF-2026-ARXIV-2602-11287:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-05-inference-system/48-speculative-decoding.md#本章要回答的问题 (line 10); books/part-05-inference-system/50-vllm.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.11287v1 实际披露的机制与实验。方法定位为 arXiv:2602.11287v1 HTML — §II HiFloat4；验证定位为 arXiv:2602.11287v1 HTML — §IV Language Model Inference with HiFloat4；边界定位为 arXiv:2602.11287v1 HTML — §V Conclusion。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-11287:end -->

<!-- existing:SF-2026-ARXIV-2602-11348:start -->
已对读当前 owner `PLATFORM-EVALUATION-SYSTEM` 在 `books/part-06-ai-infrastructure/66-evaluation-system.md#评估对象有四个层次 (line 689)` 的命题：### 从 Perfect API 到累积故障：Agent 评测必须控制 Environment Complexity
<!-- existing:SF-2026-ARXIV-2602-11348:end -->

<!-- delta:SF-2026-ARXIV-2602-11348:start -->
exact-v1 的 `arXiv:2602.11348v1 HTML — §2.1 Design Principles` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 evaluation contract、覆盖分母、evidence lineage 与 release gate。触发约束是：agent、长时程和多模态系统把失败分散到状态、工具与环境交互链。
<!-- delta:SF-2026-ARXIV-2602-11348:end -->

<!-- books-review:SF-2026-ARXIV-2602-11348:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-06-ai-infrastructure/65-kai-scheduler.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/67-monitoring.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.11348v1 实际披露的机制与实验。方法定位为 arXiv:2602.11348v1 HTML — §2.1 Design Principles；验证定位为 arXiv:2602.11348v1 HTML — §A.1 Main Results；边界定位为 arXiv:2602.11348v1 HTML — §5 Limitations。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-11348:end -->

<!-- existing:SF-2026-ARXIV-2602-11456:start -->
已对读当前 owner `TRAIN-DISTRIBUTED-TRAINING` 在 `books/part-04-training-system/36-distributed-training.md#failure-不再是单进程退出 (line 749)` 的命题：### 通信对象从无类型字节演进为有版本的训练状态
<!-- existing:SF-2026-ARXIV-2602-11456:end -->

<!-- delta:SF-2026-ARXIV-2602-11456:start -->
exact-v1 的 `arXiv:2602.11456v1 HTML — §5. System Design` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 训练状态分片、collective、同步与故障恢复。触发约束是：参数、optimizer state 和通信规模越过单设备边界。
<!-- delta:SF-2026-ARXIV-2602-11456:end -->

<!-- books-review:SF-2026-ARXIV-2602-11456:start -->
Decision=`Integrate`：现有命题原先未完整承载该 family 的长期机制责任；写回已在 canonical owner 中完成，并通过唯一 marker、正文位置和 claim-boundary 的 post-write fresh-context audit。 相邻章节已定位为 `books/part-04-training-system/35-checkpoint.md#本章要回答的问题 (line 10); books/part-04-training-system/37-tensor-parallel.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.11456v1 实际披露的机制与实验。方法定位为 arXiv:2602.11456v1 HTML — §5. System Design；验证定位为 arXiv:2602.11456v1 HTML — §7.2. End-to-End Results；边界定位为 arXiv:2602.11456v1 HTML — §6. Discussion。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-11456:end -->

<!-- existing:SF-2026-ARXIV-2602-11470:start -->
已对读当前 owner `PLATFORM-SECURITY` 在 `books/part-06-ai-infrastructure/72-security.md#风险管理而不是一次性认证 (line 1137)` 的命题：### 隐私不是一个开关，而是明文边界的重新分配
<!-- existing:SF-2026-ARXIV-2602-11470:end -->

<!-- delta:SF-2026-ARXIV-2602-11470:start -->
exact-v1 的 `arXiv:2602.11470v1 HTML — §3. System Overview` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 身份、授权、数据流、策略执行点与审计证据。触发约束是：工具、记忆和多 agent 委托把不可信内容转化为可执行控制流。
<!-- delta:SF-2026-ARXIV-2602-11470:end -->

<!-- books-review:SF-2026-ARXIV-2602-11470:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-06-ai-infrastructure/71-multi-tenant.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/73-production-best-practice.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.11470v1 实际披露的机制与实验。方法定位为 arXiv:2602.11470v1 HTML — §3. System Overview；验证定位为 arXiv:2602.11470v1 HTML — §7.3. End-to-end Performance Evaluation；边界定位为 arXiv:2602.11470v1 HTML — §7.4. Discussions on Accuracy。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-11470:end -->

<!-- existing:SF-2026-ARXIV-2602-11506:start -->
已对读当前 owner `PLATFORM-EVALUATION-SYSTEM` 在 `books/part-06-ai-infrastructure/66-evaluation-system.md#评估对象有四个层次 (line 737)` 的命题：若环境由 LLM 根据 declarative state/rules 动态生成 observation，它位于 mock 与 deterministic simulator 之间： YAML/schema 使任务状态和 rubric 可检查，语言生成又允许探索隐含需求；代价是 simulator 自身可能违反规则、 泄漏答案或用与被测 Agent 相关的模型制造共同偏差。Run identity 必须绑定 state schema、transition rules、world- model prompt/checkpoint、seed、consistency tests 和 hidden-state access。Implicit Intelligence 的受控实验支持这种 evidence tier，不把作者的一致性数字写成 deterministic execution guarantee。
<!-- existing:SF-2026-ARXIV-2602-11506:end -->

<!-- delta:SF-2026-ARXIV-2602-11506:start -->
exact-v1 的 `arXiv:2602.11506v1 HTML — §3 Methodology: The Integrated Standard Roofline Framework` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 evaluation contract、覆盖分母、evidence lineage 与 release gate。触发约束是：agent、长时程和多模态系统把失败分散到状态、工具与环境交互链。
<!-- delta:SF-2026-ARXIV-2602-11506:end -->

<!-- books-review:SF-2026-ARXIV-2602-11506:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-06-ai-infrastructure/65-kai-scheduler.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/67-monitoring.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.11506v1 实际披露的机制与实验。方法定位为 arXiv:2602.11506v1 HTML — §3 Methodology: The Integrated Standard Roofline Framework；验证定位为 arXiv:2602.11506v1 HTML — §4 Comprehensive Characterization Study；边界定位为 arXiv:2602.11506v1 HTML — §Appendix B Future Work。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-11506:end -->

<!-- existing:SF-2026-ARXIV-2602-11510:start -->
已对读当前 owner `PLATFORM-SECURITY` 在 `books/part-06-ai-infrastructure/72-security.md#从-trace-检查到受限状态空间验证 (line 573)` 的命题：Contract evaluator 是 reference monitor 的一个受限实现，不是原始事实传感器。`tone_score`、PII flag 或 confidence 等字段仍由独立 extractor 产生，其版本、误差和缺失必须传播为 Unknown；概率阈值、reference distribution 与 recovery success 也会漂移。`arXiv:2602.22302v1` 的 exact-v1 只支持 §3 的 contract 语义、§4.3 composition、§5 的 reference architecture、作者 benchmark/实验与 §8.2 限制，不证明 live production Agent 已满足形式保证。feature 不可验证、contract 冲突、composition 假设失效或 action 不可逆时，应 fail closed、sandbox 或人工审批；静态 policy、trace audit 与有界 model checking 继续作为更强或更便宜的共存分支。
<!-- existing:SF-2026-ARXIV-2602-11510:end -->

<!-- delta:SF-2026-ARXIV-2602-11510:start -->
exact-v1 的 `arXiv:2602.11510v1 HTML — §IV AgentLeak Benchmark Design` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 身份、授权、数据流、策略执行点与审计证据。触发约束是：工具、记忆和多 agent 委托把不可信内容转化为可执行控制流。
<!-- delta:SF-2026-ARXIV-2602-11510:end -->

<!-- books-review:SF-2026-ARXIV-2602-11510:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-06-ai-infrastructure/71-multi-tenant.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/73-production-best-practice.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.11510v1 实际披露的机制与实验。方法定位为 arXiv:2602.11510v1 HTML — §IV AgentLeak Benchmark Design；验证定位为 arXiv:2602.11510v1 HTML — §VI Evaluation and Results；边界定位为 arXiv:2602.11510v1 HTML — §VII-D Limitations。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-11510:end -->

<!-- existing:SF-2026-ARXIV-2602-11513:start -->
已对读当前 owner `PLATFORM-SECURITY` 在 `books/part-06-ai-infrastructure/72-security.md#风险管理而不是一次性认证 (line 1149)` 的命题：### 从输入窗口到中间激活与权重：Observer State 决定隐私边界
<!-- existing:SF-2026-ARXIV-2602-11513:end -->

<!-- delta:SF-2026-ARXIV-2602-11513:start -->
exact-v1 的 `arXiv:2602.11513v1 HTML — §4 Methodology` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 身份、授权、数据流、策略执行点与审计证据。触发约束是：工具、记忆和多 agent 委托把不可信内容转化为可执行控制流。
<!-- delta:SF-2026-ARXIV-2602-11513:end -->

<!-- books-review:SF-2026-ARXIV-2602-11513:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-06-ai-infrastructure/71-multi-tenant.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/73-production-best-practice.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.11513v1 实际披露的机制与实验。方法定位为 arXiv:2602.11513v1 HTML — §4 Methodology；验证定位为 arXiv:2602.11513v1 HTML — §B.4 Additional Experimental Results；独立 limitations 未披露，因而采用更窄主张。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-11513:end -->

<!-- existing:SF-2026-ARXIV-2602-11574:start -->
已对读当前 owner `AGENT-PLATFORM` 在 `books/part-07-agent/84-agent-platform.md#scheduling-不只是-gpu (line 536)` 的命题：资源调度之上还有一层 configuration scheduling：同一 query 可以选择单 Agent、并行/串行协作、不同 tools、 Prompt 和 reasoning budget。固定 workflow 最容易测试，却会让简单请求承担复杂拓扑成本，也让困难请求缺少必要 验证。平台可维护一个版本化 option catalog，并让 policy 在 admission 时选择配置：
<!-- existing:SF-2026-ARXIV-2602-11574:end -->

<!-- delta:SF-2026-ARXIV-2602-11574:start -->
exact-v1 的 `arXiv:2602.11574v1 HTML — §3 Methodology` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 agent artifact、runtime、policy、evidence 与 lifecycle control。触发约束是：生产中的多租户、长任务、权限与恢复要求独立平台责任。
<!-- delta:SF-2026-ARXIV-2602-11574:end -->

<!-- books-review:SF-2026-ARXIV-2602-11574:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-07-agent/83-mcp.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.11574v1 实际披露的机制与实验。方法定位为 arXiv:2602.11574v1 HTML — §3 Methodology；验证定位为 arXiv:2602.11574v1 HTML — §4 Experiments；边界定位为 arXiv:2602.11574v1 HTML — §4.6 Error Analysis。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-11574:end -->

<!-- existing:SF-2026-ARXIV-2602-11686:start -->
已对读当前 owner `TRAIN-DISTRIBUTED-TRAINING` 在 `books/part-04-training-system/36-distributed-training.md#每种并行直接切什么 (line 517)` 的命题：### Expert Parallel 从静态放置到动态 Token + Weight Spill
<!-- existing:SF-2026-ARXIV-2602-11686:end -->

<!-- delta:SF-2026-ARXIV-2602-11686:start -->
exact-v1 的 `arXiv:2602.11686v1 HTML — §3.1. FSEP: Fully Sharded Expert Parallelism` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 训练状态分片、collective、同步与故障恢复。触发约束是：参数、optimizer state 和通信规模越过单设备边界。
<!-- delta:SF-2026-ARXIV-2602-11686:end -->

<!-- books-review:SF-2026-ARXIV-2602-11686:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-04-training-system/35-checkpoint.md#本章要回答的问题 (line 10); books/part-04-training-system/37-tensor-parallel.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.11686v1 实际披露的机制与实验。方法定位为 arXiv:2602.11686v1 HTML — §3.1. FSEP: Fully Sharded Expert Parallelism；验证定位为 arXiv:2602.11686v1 HTML — §5.2. End-to-End Performance；边界定位为 arXiv:2602.11686v1 HTML — §7. Discussion。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-11686:end -->

<!-- existing:SF-2026-ARXIV-2602-11749:start -->
已对读当前 owner `PLATFORM-SECURITY` 在 `books/part-06-ai-infrastructure/72-security.md#风险管理而不是一次性认证 (line 1073)` 的命题：## 风险管理而不是一次性认证
<!-- existing:SF-2026-ARXIV-2602-11749:end -->

<!-- delta:SF-2026-ARXIV-2602-11749:start -->
exact-v1 的 `arXiv:2602.11749v1 HTML — §3 Method` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 身份、授权、数据流、策略执行点与审计证据。触发约束是：工具、记忆和多 agent 委托把不可信内容转化为可执行控制流。
<!-- delta:SF-2026-ARXIV-2602-11749:end -->

<!-- books-review:SF-2026-ARXIV-2602-11749:start -->
Decision=`Integrate`：现有命题原先未完整承载该 family 的长期机制责任；写回已在 canonical owner 中完成，并通过唯一 marker、正文位置和 claim-boundary 的 post-write fresh-context audit。 相邻章节已定位为 `books/part-06-ai-infrastructure/71-multi-tenant.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/73-production-best-practice.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.11749v1 实际披露的机制与实验。方法定位为 arXiv:2602.11749v1 HTML — §3 Method；验证定位为 arXiv:2602.11749v1 HTML — §Appendix C False Positive Evaluation on Safe Tasks；边界定位为 arXiv:2602.11749v1 HTML — §5 Discussion。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-11749:end -->

<!-- existing:SF-2026-ARXIV-2602-11786:start -->
已对读当前 owner `PLATFORM-EVALUATION-SYSTEM` 在 `books/part-06-ai-infrastructure/66-evaluation-system.md#action-control-需要-sensitivity-与-invariance-双臂证据 (line 2487)` 的命题：### Safety Evaluation 还需要 Depth-oriented Repeated Inference
<!-- existing:SF-2026-ARXIV-2602-11786:end -->

<!-- delta:SF-2026-ARXIV-2602-11786:start -->
exact-v1 的 `arXiv:2602.11786v1 HTML — §3 Methodology` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 evaluation contract、覆盖分母、evidence lineage 与 release gate。触发约束是：agent、长时程和多模态系统把失败分散到状态、工具与环境交互链。
<!-- delta:SF-2026-ARXIV-2602-11786:end -->

<!-- books-review:SF-2026-ARXIV-2602-11786:start -->
Decision=`Integrate`：现有命题原先未完整承载该 family 的长期机制责任；写回已在 canonical owner 中完成，并通过唯一 marker、正文位置和 claim-boundary 的 post-write fresh-context audit。 相邻章节已定位为 `books/part-06-ai-infrastructure/65-kai-scheduler.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/67-monitoring.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.11786v1 实际披露的机制与实验。方法定位为 arXiv:2602.11786v1 HTML — §3 Methodology；验证定位为 arXiv:2602.11786v1 HTML — §4.3 Phase 2B: Depth-Oriented Evaluation Under Repeated Sampling；边界定位为 arXiv:2602.11786v1 HTML — §A.7 Limitations of LLM-as-judge。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-11786:end -->

<!-- existing:SF-2026-ARXIV-2602-11877:start -->
已对读当前 owner `PLATFORM-EVALUATION-SYSTEM` 在 `books/part-06-ai-infrastructure/66-evaluation-system.md#从目标到证据而不是从指标到目标 (line 123)` 的命题：这把 uncertainty 从一次性 benchmark 变成 release state，却依赖 calibration sample 与部署分布的 exchangeability。现有结果覆盖三类 model family、八个以 classification/MCQ 为主的任务序列；`m=200`、低于 1% replay 的结论不能外推到开放式 generation，后者在论文中仍属探索。Exchangeability 或 coverage Gate 失败时应冻结 promotion，回退上一组 model/calibration artifacts；accuracy 与 coverage 两条 Gate 必须并存，不能相互抵消。
<!-- existing:SF-2026-ARXIV-2602-11877:end -->

<!-- delta:SF-2026-ARXIV-2602-11877:start -->
exact-v1 的 `arXiv:2602.11877v1 HTML — §4 Methodology` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 evaluation contract、覆盖分母、evidence lineage 与 release gate。触发约束是：agent、长时程和多模态系统把失败分散到状态、工具与环境交互链。
<!-- delta:SF-2026-ARXIV-2602-11877:end -->

<!-- books-review:SF-2026-ARXIV-2602-11877:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-06-ai-infrastructure/65-kai-scheduler.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/67-monitoring.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.11877v1 实际披露的机制与实验。方法定位为 arXiv:2602.11877v1 HTML — §4 Methodology；验证定位为 arXiv:2602.11877v1 HTML — §Router Ability.；边界定位为 arXiv:2602.11877v1 HTML — §Limitations。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-11877:end -->

<!-- existing:SF-2026-ARXIV-2602-11937:start -->
已对读当前 owner `MODEL-MOE` 在 `books/part-02-model/21-moe.md#从参数化-router-到带检索记忆的-router (line 473)` 的命题：### Post-training 后再增加可跳过路径，不等于删除旧 Experts
<!-- existing:SF-2026-ARXIV-2602-11937:end -->

<!-- delta:SF-2026-ARXIV-2602-11937:start -->
exact-v1 的 `arXiv:2602.11937v1 HTML — §2 Puzzle Optimization` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 expert 选择、capacity、placement 与通信。触发约束是：容量扩大后，激活成本和通信使全参数计算不可持续。
<!-- delta:SF-2026-ARXIV-2602-11937:end -->

<!-- books-review:SF-2026-ARXIV-2602-11937:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-02-model/20-sampling.md#本章要回答的问题 (line 10); books/part-02-model/22-long-context.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.11937v1 实际披露的机制与实验。方法定位为 arXiv:2602.11937v1 HTML — §2 Puzzle Optimization；验证定位为 arXiv:2602.11937v1 HTML — §4.1 Inference Efficiency；边界定位为 arXiv:2602.11937v1 HTML — §5 Discussion。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-11937:end -->

<!-- existing:SF-2026-ARXIV-2602-11964:start -->
已对读当前 owner `PLATFORM-EVALUATION-SYSTEM` 在 `books/part-06-ai-infrastructure/66-evaluation-system.md#评估对象有四个层次 (line 534)` 的命题：### Living-world Evaluation：外生变化必须进入 Run Identity
<!-- existing:SF-2026-ARXIV-2602-11964:end -->

<!-- delta:SF-2026-ARXIV-2602-11964:start -->
exact-v1 的 `arXiv:2602.11964v1 HTML — §4.2 Scenario design and annotation protocol` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 evaluation contract、覆盖分母、evidence lineage 与 release gate。触发约束是：agent、长时程和多模态系统把失败分散到状态、工具与环境交互链。
<!-- delta:SF-2026-ARXIV-2602-11964:end -->

<!-- books-review:SF-2026-ARXIV-2602-11964:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-06-ai-infrastructure/65-kai-scheduler.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/67-monitoring.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.11964v1 实际披露的机制与实验。方法定位为 arXiv:2602.11964v1 HTML — §4.2 Scenario design and annotation protocol；验证定位为 arXiv:2602.11964v1 HTML — §5.1 Core results；边界定位为 arXiv:2602.11964v1 HTML — §6 Conclusion & discussion。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-11964:end -->

<!-- existing:SF-2026-ARXIV-2602-12194:start -->
已对读当前 owner `PLATFORM-SECURITY` 在 `books/part-06-ai-infrastructure/72-security.md#从-trace-检查到受限状态空间验证 (line 573)` 的命题：Contract evaluator 是 reference monitor 的一个受限实现，不是原始事实传感器。`tone_score`、PII flag 或 confidence 等字段仍由独立 extractor 产生，其版本、误差和缺失必须传播为 Unknown；概率阈值、reference distribution 与 recovery success 也会漂移。`arXiv:2602.22302v1` 的 exact-v1 只支持 §3 的 contract 语义、§4.3 composition、§5 的 reference architecture、作者 benchmark/实验与 §8.2 限制，不证明 live production Agent 已满足形式保证。feature 不可验证、contract 冲突、composition 假设失效或 action 不可逆时，应 fail closed、sandbox 或人工审批；静态 policy、trace audit 与有界 model checking 继续作为更强或更便宜的共存分支。
<!-- existing:SF-2026-ARXIV-2602-12194:end -->

<!-- delta:SF-2026-ARXIV-2602-12194:start -->
exact-v1 的 `arXiv:2602.12194v1 HTML — §5 Our MalTool` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 身份、授权、数据流、策略执行点与审计证据。触发约束是：工具、记忆和多 agent 委托把不可信内容转化为可执行控制流。
<!-- delta:SF-2026-ARXIV-2602-12194:end -->

<!-- books-review:SF-2026-ARXIV-2602-12194:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-06-ai-infrastructure/71-multi-tenant.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/73-production-best-practice.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.12194v1 实际披露的机制与实验。方法定位为 arXiv:2602.12194v1 HTML — §5 Our MalTool；验证定位为 arXiv:2602.12194v1 HTML — §6 Evaluating MalTool；边界定位为 arXiv:2602.12194v1 HTML — §8 Discussion and Limitations。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-12194:end -->

<!-- existing:SF-2026-ARXIV-2602-12244:start -->
已对读当前 owner `AGENT-PLANNING` 在 `books/part-07-agent/79-planning.md#goalconstraint-与-policy (line 252)` 的命题：### 从 Project Brief 到可验证 Task Contracts
<!-- existing:SF-2026-ARXIV-2602-12244:end -->

<!-- delta:SF-2026-ARXIV-2602-12244:start -->
exact-v1 的 `arXiv:2602.12244v1 HTML — §III Overview` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 计划路由、证据需求与停止条件。触发约束是：自演化与长链任务需要区分已知、未知和可验证的下一步。
<!-- delta:SF-2026-ARXIV-2602-12244:end -->

<!-- books-review:SF-2026-ARXIV-2602-12244:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-07-agent/78-tool-calling.md#本章要回答的问题 (line 10); books/part-07-agent/80-reflection.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.12244v1 实际披露的机制与实验。方法定位为 arXiv:2602.12244v1 HTML — §III Overview；验证定位为 arXiv:2602.12244v1 HTML — §V-A Inference and Evaluation；边界定位为 arXiv:2602.12244v1 HTML — §VII Conclusion & Limitations。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-12244:end -->

<!-- existing:SF-2026-ARXIV-2602-12271:start -->
已对读当前 owner `INFER-TENSORRT-LLM` 在 `books/part-05-inference-system/49-tensorrt-llm.md#专用加速器首先是一份-workload-contract (line 1102)` 的命题：## 专用加速器首先是一份 Workload Contract
<!-- existing:SF-2026-ARXIV-2602-12271:end -->

<!-- delta:SF-2026-ARXIV-2602-12271:start -->
exact-v1 的 `arXiv:2602.12271v1 HTML — §4.3 Finetuning and Efficient Implementation` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 graph lowering、kernel/precision 选择与执行计划版本。触发约束是：模型规模、算子形态和 SLO 使执行计划、精度与 kernel 选择成为主要成本。
<!-- delta:SF-2026-ARXIV-2602-12271:end -->

<!-- books-review:SF-2026-ARXIV-2602-12271:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-05-inference-system/48-speculative-decoding.md#本章要回答的问题 (line 10); books/part-05-inference-system/50-vllm.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.12271v1 实际披露的机制与实验。方法定位为 arXiv:2602.12271v1 HTML — §4.3 Finetuning and Efficient Implementation；验证定位为 arXiv:2602.12271v1 HTML — §5.3 Efficiency Evaluations；边界定位为 arXiv:2602.12271v1 HTML — §3.1 Approximation Error Analysis。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-12271:end -->

<!-- existing:SF-2026-ARXIV-2602-12281:start -->
已对读当前 owner `TRAIN-RLHF` 在 `books/part-04-training-system/31-rlhf.md#evaluation-必须独立于-reward-model (line 539)` 的命题：## Evaluation 必须独立于 Reward Model
<!-- existing:SF-2026-ARXIV-2602-12281:end -->

<!-- delta:SF-2026-ARXIV-2602-12281:start -->
exact-v1 的 `arXiv:2602.12281v1 HTML — §4 Method` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 rollout、reward、policy/reference 与更新 freshness。触发约束是：模型规模、奖励来源和任务 horizon 改变后，同一配方的排序可能反转。
<!-- delta:SF-2026-ARXIV-2602-12281:end -->

<!-- books-review:SF-2026-ARXIV-2602-12281:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-04-training-system/30-lora.md#本章要回答的问题 (line 10); books/part-04-training-system/32-ppo.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.12281v1 实际披露的机制与实验。方法定位为 arXiv:2602.12281v1 HTML — §4 Method；验证定位为 arXiv:2602.12281v1 HTML — §5.4 Simulation Evaluation Results；边界定位为 arXiv:2602.12281v1 HTML — §6 Conclusion。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-12281:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
<!-- audit-receipt:FCSA-2026-02-FINAL:20260214:start -->
全月验收：`papers/2026/02/_sources/february-fresh-context-audit.json`；本日受审收据：`papers/2026/02/_sources/daily-20260214/screening-ledger-author.json`、`papers/2026/02/_sources/daily-20260214/screening-ledger-final.json`、`papers/2026/02/_sources/daily-20260214/exact-v1-review-packet.json`、`papers/2026/02/_sources/daily-20260214/books-current-content-comparison.json`、`papers/2026/02/_sources/daily-20260214/BOOKS_WRITEBACK_QUEUE.json`。
<!-- audit-receipt:FCSA-2026-02-FINAL:20260214:end -->

| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260214-COVERAGE-FINAL | fresh-context:february-independent-reviewer | coverage | coverage:SRC-ARXIV:20260214; audit-receipt:FCSA-2026-02-FINAL:20260214 | — | 本日 raw=628、retained=32、closures=596；全月 FP/FN、日期与撤稿 finding 均已解决 | passed |
| SA-20260214-EVIDENCE-FINAL | fresh-context:february-independent-reviewer | evidence | review:SF-2026-ARXIV-2602-11882; review:SF-2026-ARXIV-2602-11291; review:SF-2026-ARXIV-2602-11301; review:SF-2026-ARXIV-2602-11327; review:SF-2026-ARXIV-2602-11521; review:SF-2026-ARXIV-2602-11530; review:SF-2026-ARXIV-2602-11543; review:SF-2026-ARXIV-2602-11688; review:SF-2026-ARXIV-2602-11790; review:SF-2026-ARXIV-2602-12029; review:SF-2026-ARXIV-2602-12151; review:SF-2026-ARXIV-2602-11184; review:SF-2026-ARXIV-2602-11192; review:SF-2026-ARXIV-2602-11224; review:SF-2026-ARXIV-2602-11287; review:SF-2026-ARXIV-2602-11348; review:SF-2026-ARXIV-2602-11456; review:SF-2026-ARXIV-2602-11470; review:SF-2026-ARXIV-2602-11506; review:SF-2026-ARXIV-2602-11510; review:SF-2026-ARXIV-2602-11513; review:SF-2026-ARXIV-2602-11574; review:SF-2026-ARXIV-2602-11686; review:SF-2026-ARXIV-2602-11749; review:SF-2026-ARXIV-2602-11786; review:SF-2026-ARXIV-2602-11877; review:SF-2026-ARXIV-2602-11937; review:SF-2026-ARXIV-2602-11964; review:SF-2026-ARXIV-2602-12194; review:SF-2026-ARXIV-2602-12244; review:SF-2026-ARXIV-2602-12271; review:SF-2026-ARXIV-2602-12281; audit-receipt:FCSA-2026-02-FINAL:20260214 | — | exact-v1 complete=32、blocked=0；locator、excerpt、RP 与 claim boundary 已验收 | passed |
| SA-20260214-SELECTION-FINAL | fresh-context:february-independent-reviewer | deep_analysis_selection | validator:deep-analysis-selection-v1; audit-receipt:FCSA-2026-02-FINAL:20260214 | — | 本日完整 eligibility frontier 与最多三个叙事单元已验收，未选择项均保留显式理由 | passed |
| SA-20260214-BOOKS-POSTWRITE-FINAL | fresh-context:february-independent-reviewer | books | books-review:SF-2026-ARXIV-2602-11882; books-review:SF-2026-ARXIV-2602-11291; books-review:SF-2026-ARXIV-2602-11301; books-review:SF-2026-ARXIV-2602-11327; books-review:SF-2026-ARXIV-2602-11521; books-review:SF-2026-ARXIV-2602-11530; books-review:SF-2026-ARXIV-2602-11543; books-review:SF-2026-ARXIV-2602-11688; books-review:SF-2026-ARXIV-2602-11790; books-review:SF-2026-ARXIV-2602-12029; books-review:SF-2026-ARXIV-2602-12151; books-review:SF-2026-ARXIV-2602-11184; books-review:SF-2026-ARXIV-2602-11192; books-review:SF-2026-ARXIV-2602-11224; books-review:SF-2026-ARXIV-2602-11287; books-review:SF-2026-ARXIV-2602-11348; books-review:SF-2026-ARXIV-2602-11456; books-review:SF-2026-ARXIV-2602-11470; books-review:SF-2026-ARXIV-2602-11506; books-review:SF-2026-ARXIV-2602-11510; books-review:SF-2026-ARXIV-2602-11513; books-review:SF-2026-ARXIV-2602-11574; books-review:SF-2026-ARXIV-2602-11686; books-review:SF-2026-ARXIV-2602-11749; books-review:SF-2026-ARXIV-2602-11786; books-review:SF-2026-ARXIV-2602-11877; books-review:SF-2026-ARXIV-2602-11937; books-review:SF-2026-ARXIV-2602-11964; books-review:SF-2026-ARXIV-2602-12194; books-review:SF-2026-ARXIV-2602-12244; books-review:SF-2026-ARXIV-2602-12271; books-review:SF-2026-ARXIV-2602-12281; audit-receipt:FCSA-2026-02-FINAL:20260214 | — | 本日 Integrate=3；canonical owner、相邻命题、disposition 与 post-write/no-writeback 状态已验收 | passed |

## 8. Ignored Noise

596 个 pre-denominator closure 保存在 `papers/2026/02/_sources/daily-20260214/screening-ledger-final.json`；每项含 identity、title、abstract 与 family-specific reason。withdrawn=0，撤稿不留 selected 痕迹。

## 9. Recommended Action

本日四域 Gate 已关闭；保留 `papers/2026/02/_sources/february-fresh-context-audit.json` 与本地冻结收据。仅在 primary evidence、撤稿状态或公共合同变化时重新打开对应 scope。

## 10. Repository Changes

- promotion 更新 `papers/2026/02/14/README.md` 与本日 `_sources` 最终状态收据。
- 本步骤不修改 Books 或 Weekly，也不 stage、commit 或 push；此前已验收的 Books 写回由本日 queue 记录 post-write 状态。

## 11. Open Questions

- 无 Gate 阻塞项；论文自身未证明的边界继续保留在 Claim Boundary 中，不构成未解决流程 finding。

## 12. Sources

- [arXiv:2602.11882v1](https://arxiv.org/abs/2602.11882v1) — official exact-v1；first-public `2026-02-13T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.11291v1](https://arxiv.org/abs/2602.11291v1) — official exact-v1；first-public `2026-02-13T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.11301v1](https://arxiv.org/abs/2602.11301v1) — official exact-v1；first-public `2026-02-13T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.11327v1](https://arxiv.org/abs/2602.11327v1) — official exact-v1；first-public `2026-02-13T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.11521v1](https://arxiv.org/abs/2602.11521v1) — official exact-v1；first-public `2026-02-13T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.11530v1](https://arxiv.org/abs/2602.11530v1) — official exact-v1；first-public `2026-02-13T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.11543v1](https://arxiv.org/abs/2602.11543v1) — official exact-v1；first-public `2026-02-13T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.11688v1](https://arxiv.org/abs/2602.11688v1) — official exact-v1；first-public `2026-02-13T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.11790v1](https://arxiv.org/abs/2602.11790v1) — official exact-v1；first-public `2026-02-13T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.12029v1](https://arxiv.org/abs/2602.12029v1) — official exact-v1；first-public `2026-02-13T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.12151v1](https://arxiv.org/abs/2602.12151v1) — official exact-v1；first-public `2026-02-13T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.11184v1](https://arxiv.org/abs/2602.11184v1) — official exact-v1；first-public `2026-02-13T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.11192v1](https://arxiv.org/abs/2602.11192v1) — official exact-v1；first-public `2026-02-13T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.11224v1](https://arxiv.org/abs/2602.11224v1) — official exact-v1；first-public `2026-02-13T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.11287v1](https://arxiv.org/abs/2602.11287v1) — official exact-v1；first-public `2026-02-13T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.11348v1](https://arxiv.org/abs/2602.11348v1) — official exact-v1；first-public `2026-02-13T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.11456v1](https://arxiv.org/abs/2602.11456v1) — official exact-v1；first-public `2026-02-13T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.11470v1](https://arxiv.org/abs/2602.11470v1) — official exact-v1；first-public `2026-02-13T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.11506v1](https://arxiv.org/abs/2602.11506v1) — official exact-v1；first-public `2026-02-13T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.11510v1](https://arxiv.org/abs/2602.11510v1) — official exact-v1；first-public `2026-02-13T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.11513v1](https://arxiv.org/abs/2602.11513v1) — official exact-v1；first-public `2026-02-13T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.11574v1](https://arxiv.org/abs/2602.11574v1) — official exact-v1；first-public `2026-02-13T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.11686v1](https://arxiv.org/abs/2602.11686v1) — official exact-v1；first-public `2026-02-13T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.11749v1](https://arxiv.org/abs/2602.11749v1) — official exact-v1；first-public `2026-02-13T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.11786v1](https://arxiv.org/abs/2602.11786v1) — official exact-v1；first-public `2026-02-13T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.11877v1](https://arxiv.org/abs/2602.11877v1) — official exact-v1；first-public `2026-02-13T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.11937v1](https://arxiv.org/abs/2602.11937v1) — official exact-v1；first-public `2026-02-13T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.11964v1](https://arxiv.org/abs/2602.11964v1) — official exact-v1；first-public `2026-02-13T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.12194v1](https://arxiv.org/abs/2602.12194v1) — official exact-v1；first-public `2026-02-13T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.12244v1](https://arxiv.org/abs/2602.12244v1) — official exact-v1；first-public `2026-02-13T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.12271v1](https://arxiv.org/abs/2602.12271v1) — official exact-v1；first-public `2026-02-13T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.12281v1](https://arxiv.org/abs/2602.12281v1) — official exact-v1；first-public `2026-02-13T09:00:00+08:00`；访问日期 2026-09-02。

## 13. Final Status

Completion Status=`Complete`；Coverage=`Closed`；Evidence=`Passed`；Books=`Passed`；Unresolved Findings=0。最终 raw=628、retained=32、closures=596、exact-v1 reviews=32、blocked=0。
