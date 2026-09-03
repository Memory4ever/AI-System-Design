# Daily Research — 2026-02-11

**Research Date:** 2026-02-11

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-02-10 09:00:00 ～ 2026-02-11 09:00:00（Asia/Shanghai，左闭右开）

**Contract:** V2.1 Historical Daily independent Full Replay；既有 Weekly 未参与 discovery、分母、评分、Review、Books 判断或漏项校准；Weekly dependency=0。

**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed；全月 fresh-context 四域语义审计已通过（`papers/2026/02/_sources/february-fresh-context-audit.json`），本日 unresolved findings=0。

## Executive Summary

窗口 raw identities=1173，title+abstract semantic screening=1173/1173；Candidate Denominator=35，pre-denominator closures=1138。exact-v1 Review=35/35，withdrawn=0，blocked=0；Books Integrate=5。

本日报以官方 arXiv 公告时刻映射北京时间半开窗口；DataCite 只恢复 identity 与 registry timestamp，不把 Submitted:v1、DOI created 或后续 revision 误当作报告归属。withdrawn family 只保留在 pre-denominator closure，不进入候选、评分、Review 或 Books。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-02-11 |
| Window End | 2026-02-11 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | sha256:990978e286ca875f4499208722d0c49ba304c743862d569520b89ee9f6f076d4 |
| Denominator Frozen At | 2026-09-03T07:01:18Z |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-02-10T09:00:00+08:00 | 2026-02-11T09:00:00+08:00 | 2026-09-03T07:01:18Z | DataCite identity recovery + official arXiv announcement schedule + registered-category full title/abstract screen + exact-v1 HTML/PDF | checked | 35 | SF-2026-ARXIV-2602-07186; SF-2026-ARXIV-2602-07306; SF-2026-ARXIV-2602-07379; SF-2026-ARXIV-2602-07721; SF-2026-ARXIV-2602-07878; SF-2026-ARXIV-2602-08007; SF-2026-ARXIV-2602-08847; SF-2026-ARXIV-2602-07120; SF-2026-ARXIV-2602-07223; SF-2026-ARXIV-2602-07263; SF-2026-ARXIV-2602-07265; SF-2026-ARXIV-2602-07397; SF-2026-ARXIV-2602-07398; SF-2026-ARXIV-2602-07595; SF-2026-ARXIV-2602-07616; SF-2026-ARXIV-2602-07840; SF-2026-ARXIV-2602-07962; SF-2026-ARXIV-2602-07996; SF-2026-ARXIV-2602-08005; SF-2026-ARXIV-2602-08060; SF-2026-ARXIV-2602-08237; SF-2026-ARXIV-2602-08296; SF-2026-ARXIV-2602-08343; SF-2026-ARXIV-2602-08382; SF-2026-ARXIV-2602-08401; SF-2026-ARXIV-2602-08404; SF-2026-ARXIV-2602-08412; SF-2026-ARXIV-2602-08563; SF-2026-ARXIV-2602-08585; SF-2026-ARXIV-2602-08621; SF-2026-ARXIV-2602-08722; SF-2026-ARXIV-2602-08747; SF-2026-ARXIV-2602-08798; SF-2026-ARXIV-2602-08905; SF-2026-ARXIV-2602-08968 | pages=100; DOI prefixes=00..99; final_cursor=end; screened=1173 | 2026-02-11T09:00:00+08:00 | papers/2026/02/_sources/daily-20260211/coverage-receipt.json; papers/2026/02/_sources/daily-20260211/screening-ledger-final.json; coverage:SRC-ARXIV:20260211 | — |

<!-- coverage:SRC-ARXIV:20260211:start -->1173 个注册身份均已按 title+abstract 逐项筛选；1138 个具体拒绝理由保存在 ledger。当前注册表的其他来源在 2026-08-25 才生效，不反推为 2 月 Required。全月 receipt 已完成 false-positive / false-negative、日期归属与撤稿审计，本日 Coverage Gate=Closed。<!-- coverage:SRC-ARXIV:20260211:end -->

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2602-07186 | arXiv:2602.07186v1 | paper-v1:2602.07186 | 2026-W07 | 2026-02-10 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-07186 | self | — | new_in_window | TRAIN-RLHF | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-07186 | no |
| SF-2026-ARXIV-2602-07306 | arXiv:2602.07306v1 | paper-v1:2602.07306 | 2026-W07 | 2026-02-10 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2602-07306 | self | — | new_in_window | MODEL-TRANSFORMER-LAYER | Integrate | books-review:SF-2026-ARXIV-2602-07306 | no |
| SF-2026-ARXIV-2602-07379 | arXiv:2602.07379v1 | paper-v1:2602.07379 | 2026-W07 | 2026-02-10 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-07379 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-07379 | no |
| SF-2026-ARXIV-2602-07721 | arXiv:2602.07721v1 | paper-v1:2602.07721 | 2026-W07 | 2026-02-10 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-07721 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-07721 | no |
| SF-2026-ARXIV-2602-07878 | arXiv:2602.07878v1 | paper-v1:2602.07878 | 2026-W07 | 2026-02-10 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-07878 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-07878 | no |
| SF-2026-ARXIV-2602-08007 | arXiv:2602.08007v1 | paper-v1:2602.08007 | 2026-W07 | 2026-02-10 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-08007 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-08007 | no |
| SF-2026-ARXIV-2602-08847 | arXiv:2602.08847v1 | paper-v1:2602.08847 | 2026-W07 | 2026-02-10 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-08847 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-08847 | no |
| SF-2026-ARXIV-2602-07120 | arXiv:2602.07120v1 | paper-v1:2602.07120 | 2026-W07 | 2026-02-10 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2602-07120 | self | — | new_in_window | MODEL-SAMPLING | Integrate | books-review:SF-2026-ARXIV-2602-07120 | no |
| SF-2026-ARXIV-2602-07223 | arXiv:2602.07223v1 | paper-v1:2602.07223 | 2026-W07 | 2026-02-10 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-07223 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-07223 | no |
| SF-2026-ARXIV-2602-07263 | arXiv:2602.07263v1 | paper-v1:2602.07263 | 2026-W07 | 2026-02-10 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-07263 | self | — | new_in_window | TRAIN-LORA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-07263 | no |
| SF-2026-ARXIV-2602-07265 | arXiv:2602.07265v1 | paper-v1:2602.07265 | 2026-W07 | 2026-02-10 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2602-07265 | self | — | new_in_window | MODEL-MOE | Integrate | books-review:SF-2026-ARXIV-2602-07265 | no |
| SF-2026-ARXIV-2602-07397 | arXiv:2602.07397v1 | paper-v1:2602.07397 | 2026-W07 | 2026-02-10 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-07397 | self | — | new_in_window | MODEL-LONG-CONTEXT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-07397 | no |
| SF-2026-ARXIV-2602-07398 | arXiv:2602.07398v1 | paper-v1:2602.07398 | 2026-W07 | 2026-02-10 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-07398 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-07398 | no |
| SF-2026-ARXIV-2602-07595 | arXiv:2602.07595v1 | paper-v1:2602.07595 | 2026-W07 | 2026-02-10 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-07595 | self | — | new_in_window | TRAIN-RLHF | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-07595 | no |
| SF-2026-ARXIV-2602-07616 | arXiv:2602.07616v1 | paper-v1:2602.07616 | 2026-W07 | 2026-02-10 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-07616 | self | — | new_in_window | MODEL-MOE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-07616 | no |
| SF-2026-ARXIV-2602-07840 | arXiv:2602.07840v1 | paper-v1:2602.07840 | 2026-W07 | 2026-02-10 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-07840 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-07840 | no |
| SF-2026-ARXIV-2602-07962 | arXiv:2602.07962v1 | paper-v1:2602.07962 | 2026-W07 | 2026-02-10 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-07962 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-07962 | no |
| SF-2026-ARXIV-2602-07996 | arXiv:2602.07996v1 | paper-v1:2602.07996 | 2026-W07 | 2026-02-10 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-07996 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-07996 | no |
| SF-2026-ARXIV-2602-08005 | arXiv:2602.08005v1 | paper-v1:2602.08005 | 2026-W07 | 2026-02-10 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-08005 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-08005 | no |
| SF-2026-ARXIV-2602-08060 | arXiv:2602.08060v1 | paper-v1:2602.08060 | 2026-W07 | 2026-02-10 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-08060 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-08060 | no |
| SF-2026-ARXIV-2602-08237 | arXiv:2602.08237v1 | paper-v1:2602.08237 | 2026-W07 | 2026-02-10 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-08237 | self | — | new_in_window | TRAIN-RLHF | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-08237 | no |
| SF-2026-ARXIV-2602-08296 | arXiv:2602.08296v1 | paper-v1:2602.08296 | 2026-W07 | 2026-02-10 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-08296 | self | — | new_in_window | PLATFORM-GPU-SCHEDULER | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-08296 | no |
| SF-2026-ARXIV-2602-08343 | arXiv:2602.08343v1 | paper-v1:2602.08343 | 2026-W07 | 2026-02-10 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-08343 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-08343 | no |
| SF-2026-ARXIV-2602-08382 | arXiv:2602.08382v1 | paper-v1:2602.08382 | 2026-W07 | 2026-02-10 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-08382 | self | — | new_in_window | MODEL-LONG-CONTEXT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-08382 | no |
| SF-2026-ARXIV-2602-08401 | arXiv:2602.08401v1 | paper-v1:2602.08401 | 2026-W07 | 2026-02-10 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-08401 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-08401 | no |
| SF-2026-ARXIV-2602-08404 | arXiv:2602.08404v1 | paper-v1:2602.08404 | 2026-W07 | 2026-02-10 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-08404 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-08404 | no |
| SF-2026-ARXIV-2602-08412 | arXiv:2602.08412v1 | paper-v1:2602.08412 | 2026-W07 | 2026-02-10 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-08412 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-08412 | no |
| SF-2026-ARXIV-2602-08563 | arXiv:2602.08563v1 | paper-v1:2602.08563 | 2026-W07 | 2026-02-10 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2602-08563 | self | — | new_in_window | AGENT-MEMORY | Integrate | books-review:SF-2026-ARXIV-2602-08563 | no |
| SF-2026-ARXIV-2602-08585 | arXiv:2602.08585v1 | paper-v1:2602.08585 | 2026-W07 | 2026-02-10 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-08585 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-08585 | no |
| SF-2026-ARXIV-2602-08621 | arXiv:2602.08621v1 | paper-v1:2602.08621 | 2026-W07 | 2026-02-10 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-08621 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-08621 | no |
| SF-2026-ARXIV-2602-08722 | arXiv:2602.08722v1 | paper-v1:2602.08722 | 2026-W07 | 2026-02-10 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-08722 | self | — | new_in_window | INFER-PREFILL | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-08722 | no |
| SF-2026-ARXIV-2602-08747 | arXiv:2602.08747v1 | paper-v1:2602.08747 | 2026-W07 | 2026-02-10 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2602-08747 | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-2026-ARXIV-2602-08747 | no |
| SF-2026-ARXIV-2602-08798 | arXiv:2602.08798v1 | paper-v1:2602.08798 | 2026-W07 | 2026-02-10 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-08798 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-08798 | no |
| SF-2026-ARXIV-2602-08905 | arXiv:2602.08905v1 | paper-v1:2602.08905 | 2026-W07 | 2026-02-10 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-08905 | self | — | new_in_window | TRAIN-RLHF | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-08905 | no |
| SF-2026-ARXIV-2602-08968 | arXiv:2602.08968v1 | paper-v1:2602.08968 | 2026-W07 | 2026-02-10 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-08968 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-08968 | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2602-07186 | RP-b217f191889bdf87 | deep | arXiv:2602.07186v1 | SRC-ARXIV@arXiv:2602.07186v1 | arXiv:2602.07186v1 HTML — §4.2 Uncertainty-Driven Reward Design [facet=method]; https://arxiv.org/html/2602.07186v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.07186v1.html; sha256:b3fc31d21cf4834478a221292fb81aa91ebdd65b3a34d468b3cfcbfdbbc8a416 | arXiv:2602.07186v1 HTML — §3.2 Evaluation Results [facet=evaluation]; https://arxiv.org/html/2602.07186v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.07186v1.html; sha256:b3fc31d21cf4834478a221292fb81aa91ebdd65b3a34d468b3cfcbfdbbc8a416 | arXiv:2602.07186v1 HTML — §5.3 Ablation Study (RQ2) [facet=limitations]; https://arxiv.org/html/2602.07186v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.07186v1.html; sha256:b3fc31d21cf4834478a221292fb81aa91ebdd65b3a34d468b3cfcbfdbbc8a416 | Not Disclosed — arXiv:2602.07186v1 does not disclose a public repository, release, commit, or executable artifact used by this review | claim:SF-2026-ARXIV-2602-07186 | complete |
| SF-2026-ARXIV-2602-07306 | RP-235fffc4345bf04d | deep | arXiv:2602.07306v1 | SRC-ARXIV@arXiv:2602.07306v1 | arXiv:2602.07306v1 HTML — §2 The Parallel Track Transformer Architecture [facet=method]; https://arxiv.org/html/2602.07306v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.07306v1.html; sha256:a3140ae8dc6fe73f3775b1c73e0c8c6cfe993af3f582b6cbfa467a451cc62d5b | arXiv:2602.07306v1 HTML — §3.3 Serving Evaluation [facet=evaluation]; https://arxiv.org/html/2602.07306v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.07306v1.html; sha256:a3140ae8dc6fe73f3775b1c73e0c8c6cfe993af3f582b6cbfa467a451cc62d5b | Not Disclosed — exact-v1 HTML has no independent limitations or counterevidence section; a positive conclusion does not replace that facet [facet=limitations]; https://arxiv.org/html/2602.07306v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.07306v1.html; sha256:a3140ae8dc6fe73f3775b1c73e0c8c6cfe993af3f582b6cbfa467a451cc62d5b | External link observed in exact-v1 body: https://github.com/kingoflolz/mesh-transformer-jax; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence | claim:SF-2026-ARXIV-2602-07306 | complete |
| SF-2026-ARXIV-2602-07379 | RP-e38805839b5a40f8 | deep | arXiv:2602.07379v1 | SRC-ARXIV@arXiv:2602.07379v1 | arXiv:2602.07379v1 HTML — §3.1 Framework [facet=method]; https://arxiv.org/html/2602.07379v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.07379v1.html; sha256:02db8d35cba19cf18325fac1a0425310a29efc5052cc54ef44a06569518ae8f9 | arXiv:2602.07379v1 HTML — §4 Evaluation [facet=evaluation]; https://arxiv.org/html/2602.07379v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.07379v1.html; sha256:02db8d35cba19cf18325fac1a0425310a29efc5052cc54ef44a06569518ae8f9 | arXiv:2602.07379v1 HTML — §5 Discussion [facet=limitations]; https://arxiv.org/html/2602.07379v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.07379v1.html; sha256:02db8d35cba19cf18325fac1a0425310a29efc5052cc54ef44a06569518ae8f9 | Not Disclosed — arXiv:2602.07379v1 does not disclose a public repository, release, commit, or executable artifact used by this review | claim:SF-2026-ARXIV-2602-07379 | complete |
| SF-2026-ARXIV-2602-07721 | RP-afee5c489339f6f8 | deep | arXiv:2602.07721v1 | SRC-ARXIV@arXiv:2602.07721v1 | arXiv:2602.07721v1 HTML — §4 The ParisKV Framework [facet=method]; https://arxiv.org/html/2602.07721v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.07721v1.html; sha256:5b4a760a378b0abef0b7f0aa946790cf79516a2fae0dcd3b3bea604de26ca154 | arXiv:2602.07721v1 HTML — §5.2 Efficiency evaluation [facet=evaluation]; https://arxiv.org/html/2602.07721v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.07721v1.html; sha256:5b4a760a378b0abef0b7f0aa946790cf79516a2fae0dcd3b3bea604de26ca154 | arXiv:2602.07721v1 HTML — §5.3 Ablation Studies [facet=limitations]; https://arxiv.org/html/2602.07721v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.07721v1.html; sha256:5b4a760a378b0abef0b7f0aa946790cf79516a2fae0dcd3b3bea604de26ca154 | Not Disclosed — arXiv:2602.07721v1 does not disclose a public repository, release, commit, or executable artifact used by this review | claim:SF-2026-ARXIV-2602-07721 | complete |
| SF-2026-ARXIV-2602-07878 | RP-e6d1cc40ffeded8a | deep | arXiv:2602.07878v1 | SRC-ARXIV@arXiv:2602.07878v1 | arXiv:2602.07878v1 HTML — §C.2 Comparison of Time-Series Modeling Methods [facet=method]; https://arxiv.org/html/2602.07878v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.07878v1.html; sha256:8cb481967a064d9c6900f73f18589a994975849e0844233ccd458e4e31c2e8da | arXiv:2602.07878v1 HTML — §6.2 Main Results [facet=evaluation]; https://arxiv.org/html/2602.07878v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.07878v1.html; sha256:8cb481967a064d9c6900f73f18589a994975849e0844233ccd458e4e31c2e8da | arXiv:2602.07878v1 HTML — §B.2 More Discussions on Model-Specific Characteristics [facet=limitations]; https://arxiv.org/html/2602.07878v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.07878v1.html; sha256:8cb481967a064d9c6900f73f18589a994975849e0844233ccd458e4e31c2e8da | External link observed in exact-v1 body: https://github.com/NVIDIA/TensorRT-LLM; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence | claim:SF-2026-ARXIV-2602-07878 | complete |
| SF-2026-ARXIV-2602-08007 | RP-61682a8193399c0c | deep | arXiv:2602.08007v1 | SRC-ARXIV@arXiv:2602.08007v1 | arXiv:2602.08007v1 HTML — §3.3 TSR-Adam: Two-Sided Low-Rank Core Synchronization [facet=method]; https://arxiv.org/html/2602.08007v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.08007v1.html; sha256:c6d8014a489f601bb62cabfdf2552eb238c8571212711aa4e09e06160ae8e0f8 | arXiv:2602.08007v1 HTML — §4.2 Main Results: Pretraining Communication Efficiency [facet=evaluation]; https://arxiv.org/html/2602.08007v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.08007v1.html; sha256:c6d8014a489f601bb62cabfdf2552eb238c8571212711aa4e09e06160ae8e0f8 | arXiv:2602.08007v1 HTML — §4.3 Ablations: Two-Sidedness, Randomized SVD, and Subspace Refresh Interval [facet=limitations]; https://arxiv.org/html/2602.08007v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.08007v1.html; sha256:c6d8014a489f601bb62cabfdf2552eb238c8571212711aa4e09e06160ae8e0f8 | External link observed in exact-v1 body: https://github.com/DKmiyan/TSR-Adam; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence | claim:SF-2026-ARXIV-2602-08007 | complete |
| SF-2026-ARXIV-2602-08847 | RP-f3ac63beadd13ac3 | deep | arXiv:2602.08847v1 | SRC-ARXIV@arXiv:2602.08847v1 | arXiv:2602.08847v1 HTML — §4 Methodology [facet=method]; https://arxiv.org/html/2602.08847v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.08847v1.html; sha256:e7e2f9ca4b3324c998a009a4ee4873cf82fe34459eaffe2dbbd03cbf5e18520d | arXiv:2602.08847v1 HTML — §5.4 Ablation Study [facet=evaluation]; https://arxiv.org/html/2602.08847v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.08847v1.html; sha256:e7e2f9ca4b3324c998a009a4ee4873cf82fe34459eaffe2dbbd03cbf5e18520d | arXiv:2602.08847v1 HTML — §6 Conclusions and Limitations [facet=limitations]; https://arxiv.org/html/2602.08847v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.08847v1.html; sha256:e7e2f9ca4b3324c998a009a4ee4873cf82fe34459eaffe2dbbd03cbf5e18520d | External link observed in exact-v1 body: https://github.com/THUDM/slime; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence | claim:SF-2026-ARXIV-2602-08847 | complete |
| SF-2026-ARXIV-2602-07120 | RP-675889657933e383 | deep | arXiv:2602.07120v1 | SRC-ARXIV@arXiv:2602.07120v1 | arXiv:2602.07120v1 HTML — §3.5 Putting Anchored Decoding together [facet=method]; https://arxiv.org/html/2602.07120v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.07120v1.html; sha256:7a07a9ac613a13eba72b80d4a0bb2f480bc4971529dee30018478f0ea744342c | arXiv:2602.07120v1 HTML — §5.1 Risk–utility trade-offs [facet=evaluation]; https://arxiv.org/html/2602.07120v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.07120v1.html; sha256:7a07a9ac613a13eba72b80d4a0bb2f480bc4971529dee30018478f0ea744342c | arXiv:2602.07120v1 HTML — §A.3 Limitations and Future Work [facet=limitations]; https://arxiv.org/html/2602.07120v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.07120v1.html; sha256:7a07a9ac613a13eba72b80d4a0bb2f480bc4971529dee30018478f0ea744342c | External link observed in exact-v1 body: https://github.com/facebookresearch/lingua; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence | claim:SF-2026-ARXIV-2602-07120 | complete |
| SF-2026-ARXIV-2602-07223 | RP-2cbb8335b30ec1bf | deep | arXiv:2602.07223v1 | SRC-ARXIV@arXiv:2602.07223v1 | arXiv:2602.07223v1 HTML — §4 Implementation [facet=method]; https://arxiv.org/html/2602.07223v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.07223v1.html; sha256:e4a2f89be9cdef6e14a4e765a5db4c7d1594442910822909fd585e27c6b4609e | arXiv:2602.07223v1 HTML — §5.2 Reasoning Workloads with Short Input Context [facet=evaluation]; https://arxiv.org/html/2602.07223v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.07223v1.html; sha256:e4a2f89be9cdef6e14a4e765a5db4c7d1594442910822909fd585e27c6b4609e | Not Disclosed — exact-v1 HTML has no independent limitations or counterevidence section; a positive conclusion does not replace that facet [facet=limitations]; https://arxiv.org/html/2602.07223v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.07223v1.html; sha256:e4a2f89be9cdef6e14a4e765a5db4c7d1594442910822909fd585e27c6b4609e | Not Disclosed — arXiv:2602.07223v1 does not disclose a public repository, release, commit, or executable artifact used by this review | claim:SF-2026-ARXIV-2602-07223 | complete |
| SF-2026-ARXIV-2602-07263 | RP-3fc875e424e64937 | deep | arXiv:2602.07263v1 | SRC-ARXIV@arXiv:2602.07263v1 | arXiv:2602.07263v1 HTML — §3 tLoRA Design [facet=method]; https://arxiv.org/html/2602.07263v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.07263v1.html; sha256:d0cccb067652d3fc7d5e3c8f183430c4b9e52414fef024d172a42dc6d7c62fec | arXiv:2602.07263v1 HTML — §4 Evaluation [facet=evaluation]; https://arxiv.org/html/2602.07263v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.07263v1.html; sha256:d0cccb067652d3fc7d5e3c8f183430c4b9e52414fef024d172a42dc6d7c62fec | arXiv:2602.07263v1 HTML — §A.2 Job completion time ablation studies [facet=limitations]; https://arxiv.org/html/2602.07263v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.07263v1.html; sha256:d0cccb067652d3fc7d5e3c8f183430c4b9e52414fef024d172a42dc6d7c62fec | Not Disclosed — arXiv:2602.07263v1 does not disclose a public repository, release, commit, or executable artifact used by this review | claim:SF-2026-ARXIV-2602-07263 | complete |
| SF-2026-ARXIV-2602-07265 | RP-9ae33bfd254b81e5 | deep | arXiv:2602.07265v1 | SRC-ARXIV@arXiv:2602.07265v1 | arXiv:2602.07265v1 HTML — §3.4 Practical Algorithm [facet=method]; https://arxiv.org/html/2602.07265v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.07265v1.html; sha256:daaf04987b70db265bbfa1f15f557b2a88edbb094131b2ed138f8ad58fa074ff | arXiv:2602.07265v1 HTML — §6 Experiments [facet=evaluation]; https://arxiv.org/html/2602.07265v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.07265v1.html; sha256:daaf04987b70db265bbfa1f15f557b2a88edbb094131b2ed138f8ad58fa074ff | Not Disclosed — exact-v1 HTML has no independent limitations or counterevidence section; a positive conclusion does not replace that facet [facet=limitations]; https://arxiv.org/html/2602.07265v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.07265v1.html; sha256:daaf04987b70db265bbfa1f15f557b2a88edbb094131b2ed138f8ad58fa074ff | External link observed in exact-v1 body: https://huggingface.co/datasets/math-ai/aime25; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence | claim:SF-2026-ARXIV-2602-07265 | complete |
| SF-2026-ARXIV-2602-07397 | RP-f1873c8d174a987a | deep | arXiv:2602.07397v1 | SRC-ARXIV@arXiv:2602.07397v1 | arXiv:2602.07397v1 HTML — §2 Sketch and Walk [facet=method]; https://arxiv.org/html/2602.07397v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.07397v1.html; sha256:e0a7a603e94d09535010c0c0128bdc28a74742e5f9f7bdae9b456421746fc3f6 | arXiv:2602.07397v1 HTML — §4.3 Efficiency Evaluation [facet=evaluation]; https://arxiv.org/html/2602.07397v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.07397v1.html; sha256:e0a7a603e94d09535010c0c0128bdc28a74742e5f9f7bdae9b456421746fc3f6 | arXiv:2602.07397v1 HTML — §4.4 Ablation Studies [facet=limitations]; https://arxiv.org/html/2602.07397v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.07397v1.html; sha256:e0a7a603e94d09535010c0c0128bdc28a74742e5f9f7bdae9b456421746fc3f6 | Not Disclosed — arXiv:2602.07397v1 does not disclose a public repository, release, commit, or executable artifact used by this review | claim:SF-2026-ARXIV-2602-07397 | complete |
| SF-2026-ARXIV-2602-07398 | RP-bcf8dd418ac5ace5 | deep | arXiv:2602.07398v1 | SRC-ARXIV@arXiv:2602.07398v1 | arXiv:2602.07398v1 HTML — §5.1 System Overview [facet=method]; https://arxiv.org/html/2602.07398v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.07398v1.html; sha256:512794be3eeb375dc4bc81df1d8f745782a2421a1a4986cd47b620ee55cca455 | arXiv:2602.07398v1 HTML — §6.1 Evaluation on Benchmarks [facet=evaluation]; https://arxiv.org/html/2602.07398v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.07398v1.html; sha256:512794be3eeb375dc4bc81df1d8f745782a2421a1a4986cd47b620ee55cca455 | arXiv:2602.07398v1 HTML — §7 Discussion [facet=limitations]; https://arxiv.org/html/2602.07398v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.07398v1.html; sha256:512794be3eeb375dc4bc81df1d8f745782a2421a1a4986cd47b620ee55cca455 | External link observed in exact-v1 body: https://github.com/ruoyaow/agentsys-memory; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence | claim:SF-2026-ARXIV-2602-07398 | complete |
| SF-2026-ARXIV-2602-07595 | RP-6b8f99b11edf7abb | deep | arXiv:2602.07595v1 | SRC-ARXIV@arXiv:2602.07595v1 | arXiv:2602.07595v1 HTML — §6.1 A Ray-based Resource-Efficient Parallel Framework for GRPO [facet=method]; https://arxiv.org/html/2602.07595v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.07595v1.html; sha256:9ab63807a5054c50f9a4e3471a7c1e6857725a3cd9561b1b86ce744ec063daef | arXiv:2602.07595v1 HTML — §7.3 Objective Evaluation: Benchmarks and Ablations [facet=evaluation]; https://arxiv.org/html/2602.07595v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.07595v1.html; sha256:9ab63807a5054c50f9a4e3471a7c1e6857725a3cd9561b1b86ce744ec063daef | arXiv:2602.07595v1 HTML — §8 Conclusion [facet=limitations]; https://arxiv.org/html/2602.07595v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.07595v1.html; sha256:9ab63807a5054c50f9a4e3471a7c1e6857725a3cd9561b1b86ce744ec063daef | External link observed in exact-v1 body: https://github.com/Tele-AI; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence | claim:SF-2026-ARXIV-2602-07595 | complete |
| SF-2026-ARXIV-2602-07616 | RP-828f7833cfd8c191 | deep | arXiv:2602.07616v1 | SRC-ARXIV@arXiv:2602.07616v1 | arXiv:2602.07616v1 PDF — §method for Efficient batch decoding in MoE models. SERE dynamically reduces [facet=method]; https://arxiv.org/pdf/2602.07616v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.07616v1.pdf.txt; sha256:87f294e61b076139c40f796bcafea47fd730b8e333d4d4898ce0f10c8936d5ab | arXiv:2602.07616v1 PDF — §experiments are conducted on NVIDIA H20 GPUs. [facet=evaluation]; https://arxiv.org/pdf/2602.07616v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.07616v1.pdf.txt; sha256:87f294e61b076139c40f796bcafea47fd730b8e333d4d4898ce0f10c8936d5ab | Not Disclosed — exact-v1 PDF 全文已审计但未提供独立 Limitations 章节 [facet=limitations]; https://arxiv.org/pdf/2602.07616v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.07616v1.pdf.txt; sha256:87f294e61b076139c40f796bcafea47fd730b8e333d4d4898ce0f10c8936d5ab | External link observed in exact-v1 body: https://github.com/JL-Cheng/SERE; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence | claim:SF-2026-ARXIV-2602-07616 | complete |
| SF-2026-ARXIV-2602-07840 | RP-51eee0dce903ef16 | deep | arXiv:2602.07840v1 | SRC-ARXIV@arXiv:2602.07840v1 | arXiv:2602.07840v1 HTML — §3. Problem Formulation and Framework [facet=method]; https://arxiv.org/html/2602.07840v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.07840v1.html; sha256:42b98709da74a813686d396c96a72227038916999a5e07388f51d479d78b192f | arXiv:2602.07840v1 HTML — §5.3. Experiments: Optimizing the Student Model [facet=evaluation]; https://arxiv.org/html/2602.07840v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.07840v1.html; sha256:42b98709da74a813686d396c96a72227038916999a5e07388f51d479d78b192f | Not Disclosed — exact-v1 HTML 全文已审计但未提供独立 Limitations 章节 [facet=limitations]; https://arxiv.org/html/2602.07840v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.07840v1.html; sha256:42b98709da74a813686d396c96a72227038916999a5e07388f51d479d78b192f | Not Disclosed — arXiv:2602.07840v1 does not disclose a public repository, release, commit, or executable artifact used by this review | claim:SF-2026-ARXIV-2602-07840 | complete |
| SF-2026-ARXIV-2602-07962 | RP-d57c0fc892c9c371 | deep | arXiv:2602.07962v1 | SRC-ARXIV@arXiv:2602.07962v1 | arXiv:2602.07962v1 HTML — §2.3 Implementation [facet=method]; https://arxiv.org/html/2602.07962v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.07962v1.html; sha256:48e3bcc4a14cc84a09426182eb847418f0339350e5bf167087fbb6451d22a3eb | arXiv:2602.07962v1 HTML — §3.2 Main Results [facet=evaluation]; https://arxiv.org/html/2602.07962v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.07962v1.html; sha256:48e3bcc4a14cc84a09426182eb847418f0339350e5bf167087fbb6451d22a3eb | arXiv:2602.07962v1 HTML — §3.3 Failure Mode Analysis [facet=limitations]; https://arxiv.org/html/2602.07962v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.07962v1.html; sha256:48e3bcc4a14cc84a09426182eb847418f0339350e5bf167087fbb6451d22a3eb | External link observed in exact-v1 body: https://github.com/gkamradt/LLMTest_NeedleInAHaystack; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence | claim:SF-2026-ARXIV-2602-07962 | complete |
| SF-2026-ARXIV-2602-07996 | RP-28bebe5782c77672 | deep | arXiv:2602.07996v1 | SRC-ARXIV@arXiv:2602.07996v1 | arXiv:2602.07996v1 HTML — §3.2 Cue Families [facet=method]; https://arxiv.org/html/2602.07996v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.07996v1.html; sha256:fc65bd63705ea7cdb99ceb7ef020e91ac2894bec97c75a938331105eae2cdff3 | arXiv:2602.07996v1 HTML — §LLM judges exhibit a strong and largely unacknowledged recency bias. [facet=evaluation]; https://arxiv.org/html/2602.07996v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.07996v1.html; sha256:fc65bd63705ea7cdb99ceb7ef020e91ac2894bec97c75a938331105eae2cdff3 | arXiv:2602.07996v1 HTML — §6 Limitations [facet=limitations]; https://arxiv.org/html/2602.07996v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.07996v1.html; sha256:fc65bd63705ea7cdb99ceb7ef020e91ac2894bec97c75a938331105eae2cdff3 | Not Disclosed — arXiv:2602.07996v1 does not disclose a public repository, release, commit, or executable artifact used by this review | claim:SF-2026-ARXIV-2602-07996 | complete |
| SF-2026-ARXIV-2602-08005 | RP-13a5106dc0c9a868 | deep | arXiv:2602.08005v1 | SRC-ARXIV@arXiv:2602.08005v1 | arXiv:2602.08005v1 HTML — §4.3 Sparse-vLLM Implementation [facet=method]; https://arxiv.org/html/2602.08005v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.08005v1.html; sha256:65dcdc39e06d2ba3f6d4577898582ae2fe0696dae85f0683a50f61fe00430e41 | arXiv:2602.08005v1 HTML — §Evaluation [facet=evaluation]; https://arxiv.org/html/2602.08005v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.08005v1.html; sha256:65dcdc39e06d2ba3f6d4577898582ae2fe0696dae85f0683a50f61fe00430e41 | arXiv:2602.08005v1 HTML — §B.5 Detailed Latency Profiling and Future Optimization [facet=limitations]; https://arxiv.org/html/2602.08005v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.08005v1.html; sha256:65dcdc39e06d2ba3f6d4577898582ae2fe0696dae85f0683a50f61fe00430e41 | External link observed in exact-v1 body: https://github.com/CURRENTF/Sparse-vLLM; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence | claim:SF-2026-ARXIV-2602-08005 | complete |
| SF-2026-ARXIV-2602-08060 | RP-10891568a984e0ff | deep | arXiv:2602.08060v1 | SRC-ARXIV@arXiv:2602.08060v1 | arXiv:2602.08060v1 HTML — §III Heterogeneous Mapping Framework for Speculative Sampling [facet=method]; https://arxiv.org/html/2602.08060v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.08060v1.html; sha256:bd3b57958350c24f269a29a8eb00bd6ac944ff7bc46cc7509f68bb40798cab44 | arXiv:2602.08060v1 HTML — §IV Experimental Setup and Evaluation [facet=evaluation]; https://arxiv.org/html/2602.08060v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.08060v1.html; sha256:bd3b57958350c24f269a29a8eb00bd6ac944ff7bc46cc7509f68bb40798cab44 | arXiv:2602.08060v1 HTML — §IV-D Validation and Discussion [facet=limitations]; https://arxiv.org/html/2602.08060v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.08060v1.html; sha256:bd3b57958350c24f269a29a8eb00bd6ac944ff7bc46cc7509f68bb40798cab44 | External link observed in exact-v1 body: https://github.com/intel/neural-compressor; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence | claim:SF-2026-ARXIV-2602-08060 | complete |
| SF-2026-ARXIV-2602-08237 | RP-5f340ec4d6ae4725 | deep | arXiv:2602.08237v1 | SRC-ARXIV@arXiv:2602.08237v1 | arXiv:2602.08237v1 PDF — §Method [facet=method]; https://arxiv.org/pdf/2602.08237v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.08237v1.pdf.txt; sha256:74e67b974145268564aff0a9f692366ea5e24a57529cb29f477e397a289b79c2 | arXiv:2602.08237v1 PDF — §Evaluation. Benchmarks. We evaluate all models on two challenging long-context QA [facet=evaluation]; https://arxiv.org/pdf/2602.08237v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.08237v1.pdf.txt; sha256:74e67b974145268564aff0a9f692366ea5e24a57529cb29f477e397a289b79c2 | arXiv:2602.08237v1 PDF — §Limitations [facet=limitations]; https://arxiv.org/pdf/2602.08237v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.08237v1.pdf.txt; sha256:74e67b974145268564aff0a9f692366ea5e24a57529cb29f477e397a289b79c2 | External link observed in exact-v1 body: https://github.com/XYaoooo/reconstruction; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence | claim:SF-2026-ARXIV-2602-08237 | complete |
| SF-2026-ARXIV-2602-08296 | RP-26f9b981dfd1fc9c | deep | arXiv:2602.08296v1 | SRC-ARXIV@arXiv:2602.08296v1 | arXiv:2602.08296v1 HTML — §4. MonkeyTree System Design [facet=method]; https://arxiv.org/html/2602.08296v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.08296v1.html; sha256:d347dfd1eaf708d6355adbabc47467f221d220e35aa7f308995fe2a6ba32e861 | arXiv:2602.08296v1 HTML — §6. Evaluation [facet=evaluation]; https://arxiv.org/html/2602.08296v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.08296v1.html; sha256:d347dfd1eaf708d6355adbabc47467f221d220e35aa7f308995fe2a6ba32e861 | arXiv:2602.08296v1 HTML — §8. Discussion [facet=limitations]; https://arxiv.org/html/2602.08296v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.08296v1.html; sha256:d347dfd1eaf708d6355adbabc47467f221d220e35aa7f308995fe2a6ba32e861 | External link observed in exact-v1 body: https://huggingface.co/meta-llama/Llama-2-70b; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence | claim:SF-2026-ARXIV-2602-08296 | complete |
| SF-2026-ARXIV-2602-08343 | RP-10209ec6609c69e6 | deep | arXiv:2602.08343v1 | SRC-ARXIV@arXiv:2602.08343v1 | arXiv:2602.08343v1 HTML — §E.1 Methodology [facet=method]; https://arxiv.org/html/2602.08343v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.08343v1.html; sha256:9c7b138e3fc6b69cb9cf782db41d317fa8e3d9c60e33fe3119f3bfadd8cc3804 | arXiv:2602.08343v1 HTML — §5.2 Main Results [facet=evaluation]; https://arxiv.org/html/2602.08343v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.08343v1.html; sha256:9c7b138e3fc6b69cb9cf782db41d317fa8e3d9c60e33fe3119f3bfadd8cc3804 | arXiv:2602.08343v1 HTML — §6 Discussion [facet=limitations]; https://arxiv.org/html/2602.08343v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.08343v1.html; sha256:9c7b138e3fc6b69cb9cf782db41d317fa8e3d9c60e33fe3119f3bfadd8cc3804 | Not Disclosed — arXiv:2602.08343v1 does not disclose a public repository, release, commit, or executable artifact used by this review | claim:SF-2026-ARXIV-2602-08343 | complete |
| SF-2026-ARXIV-2602-08382 | RP-437aedf28e997300 | deep | arXiv:2602.08382v1 | SRC-ARXIV@arXiv:2602.08382v1 | arXiv:2602.08382v1 HTML — §Appendix A Implementation Details [facet=method]; https://arxiv.org/html/2602.08382v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.08382v1.html; sha256:775835449601421ecc8888d878ab676bb29a0abc5cb49c39215ce85ddeec66d8 | arXiv:2602.08382v1 HTML — §4.2 Main Results [facet=evaluation]; https://arxiv.org/html/2602.08382v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.08382v1.html; sha256:775835449601421ecc8888d878ab676bb29a0abc5cb49c39215ce85ddeec66d8 | arXiv:2602.08382v1 HTML — §Appendix C Failure Mode Analysis [facet=limitations]; https://arxiv.org/html/2602.08382v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.08382v1.html; sha256:775835449601421ecc8888d878ab676bb29a0abc5cb49c39215ce85ddeec66d8 | Not Disclosed — arXiv:2602.08382v1 does not disclose a public repository, release, commit, or executable artifact used by this review | claim:SF-2026-ARXIV-2602-08382 | complete |
| SF-2026-ARXIV-2602-08401 | RP-7a5abff095c0decc | deep | arXiv:2602.08401v1 | SRC-ARXIV@arXiv:2602.08401v1 | arXiv:2602.08401v1 HTML — §IV Methodology [facet=method]; https://arxiv.org/html/2602.08401v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.08401v1.html; sha256:ba3b04085dfaff6f3591f89a1da4d4524bf7a7c53a8d6ffae9cfec27ebdfc230 | arXiv:2602.08401v1 HTML — §VII Evaluation [facet=evaluation]; https://arxiv.org/html/2602.08401v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.08401v1.html; sha256:ba3b04085dfaff6f3591f89a1da4d4524bf7a7c53a8d6ffae9cfec27ebdfc230 | arXiv:2602.08401v1 HTML — §VIII Conclusion [facet=limitations]; https://arxiv.org/html/2602.08401v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.08401v1.html; sha256:ba3b04085dfaff6f3591f89a1da4d4524bf7a7c53a8d6ffae9cfec27ebdfc230 | External link observed in exact-v1 body: https://huggingface.co/Qwen/Qwen3-Embedding-0.6B; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence | claim:SF-2026-ARXIV-2602-08401 | complete |
| SF-2026-ARXIV-2602-08404 | RP-e00a0a0907bdfd57 | deep | arXiv:2602.08404v1 | SRC-ARXIV@arXiv:2602.08404v1 | arXiv:2602.08404v1 HTML — §3.2 Delayed Caching for Decoded Tokens (DCD) [facet=method]; https://arxiv.org/html/2602.08404v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.08404v1.html; sha256:bd2bb62576294a3f8199eda0bc5fb372444bbf830237755cce312618af877996 | arXiv:2602.08404v1 HTML — §4.2 Main Results [facet=evaluation]; https://arxiv.org/html/2602.08404v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.08404v1.html; sha256:bd2bb62576294a3f8199eda0bc5fb372444bbf830237755cce312618af877996 | arXiv:2602.08404v1 HTML — §4.3 Ablation Study and Analysis [facet=limitations]; https://arxiv.org/html/2602.08404v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.08404v1.html; sha256:bd2bb62576294a3f8199eda0bc5fb372444bbf830237755cce312618af877996 | External link observed in exact-v1 body: https://github.com/PKU-SEC-Lab/TEAM-MoE-dLLM; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence | claim:SF-2026-ARXIV-2602-08404 | complete |
| SF-2026-ARXIV-2602-08412 | RP-0bdfb68a520458cc | deep | arXiv:2602.08412v1 | SRC-ARXIV@arXiv:2602.08412v1 | arXiv:2602.08412v1 HTML — §2.4 Attack Primitives [facet=method]; https://arxiv.org/html/2602.08412v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.08412v1.html; sha256:96d9a1ce761e0744f39da004369a4e4d33b5c05a805bca14c26d3656bfe169a2 | arXiv:2602.08412v1 HTML — §3.2 Main Results and Analysis [facet=evaluation]; https://arxiv.org/html/2602.08412v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.08412v1.html; sha256:96d9a1ce761e0744f39da004369a4e4d33b5c05a805bca14c26d3656bfe169a2 | arXiv:2602.08412v1 HTML — §4 Conclusion and Future Work [facet=limitations]; https://arxiv.org/html/2602.08412v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.08412v1.html; sha256:96d9a1ce761e0744f39da004369a4e4d33b5c05a805bca14c26d3656bfe169a2 | External link observed in exact-v1 body: https://github.com/AstorYH/PASB; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence | claim:SF-2026-ARXIV-2602-08412 | complete |
| SF-2026-ARXIV-2602-08563 | RP-e2f3f4ba901015df | deep | arXiv:2602.08563v1 | SRC-ARXIV@arXiv:2602.08563v1 | arXiv:2602.08563v1 HTML — §III Implicit Memory in LLMs: Definition, Threat Model, and Feasibility [facet=method]; https://arxiv.org/html/2602.08563v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.08563v1.html; sha256:bf28aed1a945d6bb863dee8f57f2386e5c976ce3a17dd0116ea26c3d386846a3 | arXiv:2602.08563v1 HTML — §VII Time Bomb: A Temporal Backdoor via Implicit Memory [facet=evaluation]; https://arxiv.org/html/2602.08563v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.08563v1.html; sha256:bf28aed1a945d6bb863dee8f57f2386e5c976ce3a17dd0116ea26c3d386846a3 | arXiv:2602.08563v1 HTML — §IX Future Directions [facet=limitations]; https://arxiv.org/html/2602.08563v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.08563v1.html; sha256:bf28aed1a945d6bb863dee8f57f2386e5c976ce3a17dd0116ea26c3d386846a3 | External link observed in exact-v1 body: https://github.com/microsoft/implicitMemory; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence | claim:SF-2026-ARXIV-2602-08563 | complete |
| SF-2026-ARXIV-2602-08585 | RP-8cadc8118b07354a | deep | arXiv:2602.08585v1 | SRC-ARXIV@arXiv:2602.08585v1 | arXiv:2602.08585v1 HTML — §4.3 Practical Implementation: Offline Profiling [facet=method]; https://arxiv.org/html/2602.08585v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.08585v1.html; sha256:5932b8dfaaab4bec3121aa9b197856c7eb83514ab7b3e062970b981f1c30db44 | arXiv:2602.08585v1 HTML — §5.4 Ablation Study [facet=evaluation]; https://arxiv.org/html/2602.08585v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.08585v1.html; sha256:5932b8dfaaab4bec3121aa9b197856c7eb83514ab7b3e062970b981f1c30db44 | arXiv:2602.08585v1 HTML — §Limitation of Heuristic Metric. [facet=limitations]; https://arxiv.org/html/2602.08585v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.08585v1.html; sha256:5932b8dfaaab4bec3121aa9b197856c7eb83514ab7b3e062970b981f1c30db44 | External link observed in exact-v1 body: https://github.com/NVIDIA/kvpress; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence | claim:SF-2026-ARXIV-2602-08585 | complete |
| SF-2026-ARXIV-2602-08621 | RP-52acd6c2bcf2cf46 | deep | arXiv:2602.08621v1 | SRC-ARXIV@arXiv:2602.08621v1 | arXiv:2602.08621v1 HTML — §Our Proposed F-SOUR [facet=method]; https://arxiv.org/html/2602.08621v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.08621v1.html; sha256:011080080f3faed442947266362e7771066039cae6ea87915346987a8e1b168d | arXiv:2602.08621v1 HTML — §Experimental Results [facet=evaluation]; https://arxiv.org/html/2602.08621v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.08621v1.html; sha256:011080080f3faed442947266362e7771066039cae6ea87915346987a8e1b168d | arXiv:2602.08621v1 HTML — §Appendix G Limitations and Future Work [facet=limitations]; https://arxiv.org/html/2602.08621v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.08621v1.html; sha256:011080080f3faed442947266362e7771066039cae6ea87915346987a8e1b168d | External link observed in exact-v1 body: https://github.com/TrustAIRLab/UnsafeMoE; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence | claim:SF-2026-ARXIV-2602-08621 | complete |
| SF-2026-ARXIV-2602-08722 | RP-d60ee260c9b84021 | deep | arXiv:2602.08722v1 | SRC-ARXIV@arXiv:2602.08722v1 | arXiv:2602.08722v1 HTML — §3 QuoKA Method [facet=method]; https://arxiv.org/html/2602.08722v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.08722v1.html; sha256:92a9f7906721a79388c9b94f3c65aad3d4ecc0426600827b05a753efa5f5c798 | arXiv:2602.08722v1 HTML — §4 results [facet=evaluation]; https://arxiv.org/html/2602.08722v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.08722v1.html; sha256:92a9f7906721a79388c9b94f3c65aad3d4ecc0426600827b05a753efa5f5c798 | arXiv:2602.08722v1 HTML — §4.5 Ablation study [facet=limitations]; https://arxiv.org/html/2602.08722v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.08722v1.html; sha256:92a9f7906721a79388c9b94f3c65aad3d4ecc0426600827b05a753efa5f5c798 | External link observed in exact-v1 body: https://github.com/gkamradt/LLMTest_NeedleInAHaystack; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence | claim:SF-2026-ARXIV-2602-08722 | complete |
| SF-2026-ARXIV-2602-08747 | RP-10ac2474b92608fa | deep | arXiv:2602.08747v1 | SRC-ARXIV@arXiv:2602.08747v1 | arXiv:2602.08747v1 HTML — §4. System Design [facet=method]; https://arxiv.org/html/2602.08747v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.08747v1.html; sha256:992fd36b100f87b075667b718b9ef299d5770e6e746763b8c72a36d66ba61864 | arXiv:2602.08747v1 HTML — §5. Evaluation [facet=evaluation]; https://arxiv.org/html/2602.08747v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.08747v1.html; sha256:992fd36b100f87b075667b718b9ef299d5770e6e746763b8c72a36d66ba61864 | arXiv:2602.08747v1 HTML — §7. Applicable to Other Workload [facet=limitations]; https://arxiv.org/html/2602.08747v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.08747v1.html; sha256:992fd36b100f87b075667b718b9ef299d5770e6e746763b8c72a36d66ba61864 | External link observed in exact-v1 body: https://github.com/langchain-ai/langchain; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence | claim:SF-2026-ARXIV-2602-08747 | complete |
| SF-2026-ARXIV-2602-08798 | RP-f7c478b680456d5a | deep | arXiv:2602.08798v1 | SRC-ARXIV@arXiv:2602.08798v1 | arXiv:2602.08798v1 HTML — §4.1 CryptoGen Framework [facet=method]; https://arxiv.org/html/2602.08798v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.08798v1.html; sha256:84ee788100e8693aa3d61d0ea40025bb754100347a2b33589c902cc2e9d020ac | arXiv:2602.08798v1 HTML — §6.3 Breakdown Analysis of a Single Transformer Block [facet=evaluation]; https://arxiv.org/html/2602.08798v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.08798v1.html; sha256:84ee788100e8693aa3d61d0ea40025bb754100347a2b33589c902cc2e9d020ac | Not Disclosed — exact-v1 HTML has no independent limitations or counterevidence section; a positive conclusion does not replace that facet [facet=limitations]; https://arxiv.org/html/2602.08798v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.08798v1.html; sha256:84ee788100e8693aa3d61d0ea40025bb754100347a2b33589c902cc2e9d020ac | External link observed in exact-v1 body: https://github.com/microsoft/SEAL; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence | claim:SF-2026-ARXIV-2602-08798 | complete |
| SF-2026-ARXIV-2602-08905 | RP-25cb35008ca97726 | deep | arXiv:2602.08905v1 | SRC-ARXIV@arXiv:2602.08905v1 | arXiv:2602.08905v1 HTML — §5.2 Implementation Details [facet=method]; https://arxiv.org/html/2602.08905v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.08905v1.html; sha256:5dc9b85470be41e3e1ec4ac48c89a5fae4a91765baba284ae02f8d1c3697abc5 | arXiv:2602.08905v1 HTML — §5.3 Main Results [facet=evaluation]; https://arxiv.org/html/2602.08905v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.08905v1.html; sha256:5dc9b85470be41e3e1ec4ac48c89a5fae4a91765baba284ae02f8d1c3697abc5 | arXiv:2602.08905v1 HTML — §7 Conclusion and Future Work [facet=limitations]; https://arxiv.org/html/2602.08905v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.08905v1.html; sha256:5dc9b85470be41e3e1ec4ac48c89a5fae4a91765baba284ae02f8d1c3697abc5 | External link observed in exact-v1 body: https://github.com/Jiayi-Pan/TinyZeroAccessed:; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence | claim:SF-2026-ARXIV-2602-08905 | complete |
| SF-2026-ARXIV-2602-08968 | RP-f7e02f83cec3e078 | deep | arXiv:2602.08968v1 | SRC-ARXIV@arXiv:2602.08968v1 | arXiv:2602.08968v1 HTML — §2.3 SWM Evaluation Suite: Tasks, Planning Algorithms, and Baselines [facet=method]; https://arxiv.org/html/2602.08968v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.08968v1.html; sha256:f59bc6716c914264e9ebac85f87b2a2351ff6606ab1dc5d1214866049c084f73 | arXiv:2602.08968v1 HTML — §2.3 SWM Evaluation Suite: Tasks, Planning Algorithms, and Baselines [facet=evaluation]; https://arxiv.org/html/2602.08968v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.08968v1.html; sha256:f59bc6716c914264e9ebac85f87b2a2351ff6606ab1dc5d1214866049c084f73 | arXiv:2602.08968v1 HTML — §4 Conclusion and Future Directions [facet=limitations]; https://arxiv.org/html/2602.08968v1; papers/2026/02/_sources/daily-20260211/exact-v1-bodies/2602.08968v1.html; sha256:f59bc6716c914264e9ebac85f87b2a2351ff6606ab1dc5d1214866049c084f73 | Not Disclosed — arXiv:2602.08968v1 does not disclose a public repository, release, commit, or executable artifact used by this review | claim:SF-2026-ARXIV-2602-08968 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2602-07186:start -->
### The Value of Variance: Mitigating Debate Collapse in Multi-Agent Systems via Uncertainty-Driven Policy Optimization

- **Review route:** `deep`；Primary=`arXiv:2602.07186v1`；owner=`TRAIN-RLHF`。

- **问题与旧路径：** `The Value of Variance: Mitigating Debate Collapse in Multi-Agent Systems via Uncertainty-Driven Policy Optimization` 是否在 `TRAIN-RLHF` 中改变已有状态、数据或控制责任；旧路径仍成立于：固定后训练配方便于重复和对比。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.07186v1 HTML — §4.2 Uncertainty-Driven Reward Design` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 rollout、reward、policy/reference 与更新 freshness。触发约束是：模型规模、奖励来源和任务 horizon 改变后，同一配方的排序可能反转。

- **State / data / control owner：** `TRAIN-RLHF` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** Not Disclosed — arXiv:2602.07186v1 does not disclose a public repository, release, commit, or executable artifact used by this review

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.07186v1 HTML — §3.2 Evaluation Results`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.07186v1 HTML — §5.3 Ablation Study (RQ2)`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：反馈稳定、任务窄且分布固定时成熟配方仍可复用。

<!-- claim:SF-2026-ARXIV-2602-07186:start -->
- **Claim boundary:** 只支持 arXiv:2602.07186v1 实际披露的机制与实验。方法定位为 arXiv:2602.07186v1 HTML — §4.2 Uncertainty-Driven Reward Design；验证定位为 arXiv:2602.07186v1 HTML — §3.2 Evaluation Results；边界定位为 arXiv:2602.07186v1 HTML — §5.3 Ablation Study (RQ2)。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-07186:end -->
<!-- review:SF-2026-ARXIV-2602-07186:end -->

<!-- review:SF-2026-ARXIV-2602-07306:start -->
### Parallel Track Transformers: Enabling Fast GPU Inference with Reduced Synchronization

- **Review route:** `deep`；Primary=`arXiv:2602.07306v1`；owner=`MODEL-TRANSFORMER-LAYER`。

- **问题与旧路径：** `Parallel Track Transformers: Enabling Fast GPU Inference with Reduced Synchronization` 是否在 `MODEL-TRANSFORMER-LAYER` 中改变已有状态、数据或控制责任；旧路径仍成立于：串行 attention 与 FFN block 的依赖和残差路径最直接，也最容易验证。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.07306v1 HTML — §2 The Parallel Track Transformer Architecture` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 layer topology、residual merge、activation flow 与 synchronization boundary。触发约束是：跨设备执行把 block 内同步次数、分支合并和 collective placement 变成一等约束。

- **State / data / control owner：** `MODEL-TRANSFORMER-LAYER` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** External link observed in exact-v1 body: https://github.com/kingoflolz/mesh-transformer-jax; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.07306v1 HTML — §3.3 Serving Evaluation`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** exact-v1 未披露独立 limitations（`Not Disclosed — exact-v1 HTML has no independent limitations or counterevidence section; a positive conclusion does not replace that facet`）；这意味着审阅必须缩小主张，而不是把缺口当作反证。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：单设备或通信不占主导时，标准串行 Transformer layer 仍更简单可靠。

<!-- claim:SF-2026-ARXIV-2602-07306:start -->
- **Claim boundary:** 只支持 arXiv:2602.07306v1 实际披露的机制与实验。方法定位为 arXiv:2602.07306v1 HTML — §2 The Parallel Track Transformer Architecture；验证定位为 arXiv:2602.07306v1 HTML — §3.3 Serving Evaluation；独立 limitations 未披露，因而采用更窄主张。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-07306:end -->
<!-- review:SF-2026-ARXIV-2602-07306:end -->

<!-- review:SF-2026-ARXIV-2602-07379:start -->
### Aegis: Towards Governance, Integrity, and Security of AI Voice Agents

- **Review route:** `deep`；Primary=`arXiv:2602.07379v1`；owner=`PLATFORM-SECURITY`。

- **问题与旧路径：** `Aegis: Towards Governance, Integrity, and Security of AI Voice Agents` 是否在 `PLATFORM-SECURITY` 中改变已有状态、数据或控制责任；旧路径仍成立于：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.07379v1 HTML — §3.1 Framework` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 身份、授权、数据流、策略执行点与审计证据。触发约束是：工具、记忆和多 agent 委托把不可信内容转化为可执行控制流。

- **State / data / control owner：** `PLATFORM-SECURITY` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** Not Disclosed — arXiv:2602.07379v1 does not disclose a public repository, release, commit, or executable artifact used by this review

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.07379v1 HTML — §4 Evaluation`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.07379v1 HTML — §5 Discussion`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：无工具、无持久状态的只读场景仍可采用较薄边界。

<!-- claim:SF-2026-ARXIV-2602-07379:start -->
- **Claim boundary:** 只支持 arXiv:2602.07379v1 实际披露的机制与实验。方法定位为 arXiv:2602.07379v1 HTML — §3.1 Framework；验证定位为 arXiv:2602.07379v1 HTML — §4 Evaluation；边界定位为 arXiv:2602.07379v1 HTML — §5 Discussion。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-07379:end -->
<!-- review:SF-2026-ARXIV-2602-07379:end -->

<!-- review:SF-2026-ARXIV-2602-07721:start -->
### ParisKV: Fast and Drift-Robust KV-Cache Retrieval for Long-Context LLMs

- **Review route:** `deep`；Primary=`arXiv:2602.07721v1`；owner=`INFER-KV-CACHE`。

- **问题与旧路径：** `ParisKV: Fast and Drift-Robust KV-Cache Retrieval for Long-Context LLMs` 是否在 `INFER-KV-CACHE` 中改变已有状态、数据或控制责任；旧路径仍成立于：完整、逐 token 保存 KV，换取语义透明和最低重算风险。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.07721v1 HTML — §4 The ParisKV Framework` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 KV 的 identity、压缩、复用、放置与失效状态。触发约束是：长上下文、多会话和异构层级使 KV 容量、带宽及身份成为主瓶颈。

- **State / data / control owner：** `INFER-KV-CACHE` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** Not Disclosed — arXiv:2602.07721v1 does not disclose a public repository, release, commit, or executable artifact used by this review

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.07721v1 HTML — §5.2 Efficiency evaluation`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.07721v1 HTML — §5.3 Ablation Studies`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：小 batch、短上下文或严格 exactness 场景仍宜保留完整 KV。

<!-- claim:SF-2026-ARXIV-2602-07721:start -->
- **Claim boundary:** 只支持 arXiv:2602.07721v1 实际披露的机制与实验。方法定位为 arXiv:2602.07721v1 HTML — §4 The ParisKV Framework；验证定位为 arXiv:2602.07721v1 HTML — §5.2 Efficiency evaluation；边界定位为 arXiv:2602.07721v1 HTML — §5.3 Ablation Studies。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-07721:end -->
<!-- review:SF-2026-ARXIV-2602-07721:end -->

<!-- review:SF-2026-ARXIV-2602-07878:start -->
### Rethinking Latency Denial-of-Service: Attacking the LLM Serving Framework, Not the Model

- **Review route:** `deep`；Primary=`arXiv:2602.07878v1`；owner=`PLATFORM-SECURITY`。

- **问题与旧路径：** `Rethinking Latency Denial-of-Service: Attacking the LLM Serving Framework, Not the Model` 是否在 `PLATFORM-SECURITY` 中改变已有状态、数据或控制责任；旧路径仍成立于：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.07878v1 HTML — §C.2 Comparison of Time-Series Modeling Methods` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 身份、授权、数据流、策略执行点与审计证据。触发约束是：工具、记忆和多 agent 委托把不可信内容转化为可执行控制流。

- **State / data / control owner：** `PLATFORM-SECURITY` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** External link observed in exact-v1 body: https://github.com/NVIDIA/TensorRT-LLM; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.07878v1 HTML — §6.2 Main Results`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.07878v1 HTML — §B.2 More Discussions on Model-Specific Characteristics`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：无工具、无持久状态的只读场景仍可采用较薄边界。

<!-- claim:SF-2026-ARXIV-2602-07878:start -->
- **Claim boundary:** 只支持 arXiv:2602.07878v1 实际披露的机制与实验。方法定位为 arXiv:2602.07878v1 HTML — §C.2 Comparison of Time-Series Modeling Methods；验证定位为 arXiv:2602.07878v1 HTML — §6.2 Main Results；边界定位为 arXiv:2602.07878v1 HTML — §B.2 More Discussions on Model-Specific Characteristics。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-07878:end -->
<!-- review:SF-2026-ARXIV-2602-07878:end -->

<!-- review:SF-2026-ARXIV-2602-08007:start -->
### From $O(mn)$ to $O(r^2)$: Two-Sided Low-Rank Communication for Adam in Distributed Training with Memory Efficiency

- **Review route:** `deep`；Primary=`arXiv:2602.08007v1`；owner=`TRAIN-DISTRIBUTED-TRAINING`。

- **问题与旧路径：** `From $O(mn)$ to $O(r^2)$: Two-Sided Low-Rank Communication for Adam in Distributed Training with Memory Efficiency` 是否在 `TRAIN-DISTRIBUTED-TRAINING` 中改变已有状态、数据或控制责任；旧路径仍成立于：单机或纯数据并行状态最少、同步语义清晰。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.08007v1 HTML — §3.3 TSR-Adam: Two-Sided Low-Rank Core Synchronization` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 训练状态分片、collective、同步与故障恢复。触发约束是：参数、optimizer state 和通信规模越过单设备边界。

- **State / data / control owner：** `TRAIN-DISTRIBUTED-TRAINING` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** External link observed in exact-v1 body: https://github.com/DKmiyan/TSR-Adam; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.08007v1 HTML — §4.2 Main Results: Pretraining Communication Efficiency`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.08007v1 HTML — §4.3 Ablations: Two-Sidedness, Randomized SVD, and Subspace Refresh Interval`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：模型可装入单机且通信占比高时简单并行仍更优。

<!-- claim:SF-2026-ARXIV-2602-08007:start -->
- **Claim boundary:** 只支持 arXiv:2602.08007v1 实际披露的机制与实验。方法定位为 arXiv:2602.08007v1 HTML — §3.3 TSR-Adam: Two-Sided Low-Rank Core Synchronization；验证定位为 arXiv:2602.08007v1 HTML — §4.2 Main Results: Pretraining Communication Efficiency；边界定位为 arXiv:2602.08007v1 HTML — §4.3 Ablations: Two-Sidedness, Randomized SVD, and Subspace Refresh Interval。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-08007:end -->
<!-- review:SF-2026-ARXIV-2602-08007:end -->

<!-- review:SF-2026-ARXIV-2602-08847:start -->
### Dr. MAS: Stable Reinforcement Learning for Multi-Agent LLM Systems

- **Review route:** `deep`；Primary=`arXiv:2602.08847v1`；owner=`AGENT-MULTI-AGENT`。

- **问题与旧路径：** `Dr. MAS: Stable Reinforcement Learning for Multi-Agent LLM Systems` 是否在 `AGENT-MULTI-AGENT` 中改变已有状态、数据或控制责任；旧路径仍成立于：单 agent 保持单一上下文与控制流，最易归因。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.08847v1 HTML — §4 Methodology` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 拓扑、消息、共享状态、路由与停止条件。触发约束是：任务分解、异构能力与并行协作引入通信、共享状态和信用分配问题。

- **State / data / control owner：** `AGENT-MULTI-AGENT` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** External link observed in exact-v1 body: https://github.com/THUDM/slime; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.08847v1 HTML — §5.4 Ablation Study`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.08847v1 HTML — §6 Conclusions and Limitations`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：任务规模小或共享状态成本高时单 agent 仍更稳健。

<!-- claim:SF-2026-ARXIV-2602-08847:start -->
- **Claim boundary:** 只支持 arXiv:2602.08847v1 实际披露的机制与实验。方法定位为 arXiv:2602.08847v1 HTML — §4 Methodology；验证定位为 arXiv:2602.08847v1 HTML — §5.4 Ablation Study；边界定位为 arXiv:2602.08847v1 HTML — §6 Conclusions and Limitations。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-08847:end -->
<!-- review:SF-2026-ARXIV-2602-08847:end -->

<!-- review:SF-2026-ARXIV-2602-07120:start -->
### Anchored Decoding: Provably Reducing Copyright Risk for Any Language Model

- **Review route:** `deep`；Primary=`arXiv:2602.07120v1`；owner=`MODEL-SAMPLING`。

- **问题与旧路径：** `Anchored Decoding: Provably Reducing Copyright Risk for Any Language Model` 是否在 `MODEL-SAMPLING` 中改变已有状态、数据或控制责任；旧路径仍成立于：固定 decoding rule 直接从模型分布采样，状态最少且语义清楚。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.07120v1 HTML — §3.5 Putting Anchored Decoding together` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 logit transformation、proposal distribution、verification 与 token commit。触发约束是：安全、质量或计算预算需要在 token commit 前动态改变候选分布。

- **State / data / control owner：** `MODEL-SAMPLING` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** External link observed in exact-v1 body: https://github.com/facebookresearch/lingua; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.07120v1 HTML — §5.1 Risk–utility trade-offs`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.07120v1 HTML — §A.3 Limitations and Future Work`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：模型分布已经满足约束或 exact sampling 更重要时固定 decoding 仍是基线。

<!-- claim:SF-2026-ARXIV-2602-07120:start -->
- **Claim boundary:** 只支持 arXiv:2602.07120v1 实际披露的机制与实验。方法定位为 arXiv:2602.07120v1 HTML — §3.5 Putting Anchored Decoding together；验证定位为 arXiv:2602.07120v1 HTML — §5.1 Risk–utility trade-offs；边界定位为 arXiv:2602.07120v1 HTML — §A.3 Limitations and Future Work。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-07120:end -->
<!-- review:SF-2026-ARXIV-2602-07120:end -->

<!-- review:SF-2026-ARXIV-2602-07223:start -->
### Vegas: Self-Speculative Decoding with Verification-Guided Sparse Attention

- **Review route:** `deep`；Primary=`arXiv:2602.07223v1`；owner=`INFER-SPECULATIVE-DECODING`。

- **问题与旧路径：** `Vegas: Self-Speculative Decoding with Verification-Guided Sparse Attention` 是否在 `INFER-SPECULATIVE-DECODING` 中改变已有状态、数据或控制责任；旧路径仍成立于：逐 token 串行验证保持 exactness，且不维护额外 draft 状态。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.07223v1 HTML — §4 Implementation` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 proposal、验证、接受/回滚与缓存提交状态。触发约束是：decode 的串行依赖限制利用率，促使系统用廉价 proposal 换取并行验证。

- **State / data / control owner：** `INFER-SPECULATIVE-DECODING` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** Not Disclosed — arXiv:2602.07223v1 does not disclose a public repository, release, commit, or executable artifact used by this review

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.07223v1 HTML — §5.2 Reasoning Workloads with Short Input Context`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** exact-v1 未披露独立 limitations（`Not Disclosed — exact-v1 HTML has no independent limitations or counterevidence section; a positive conclusion does not replace that facet`）；这意味着审阅必须缩小主张，而不是把缺口当作反证。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：接受率低、draft 成本高或状态提交复杂时普通 decode 仍成立。

<!-- claim:SF-2026-ARXIV-2602-07223:start -->
- **Claim boundary:** 只支持 arXiv:2602.07223v1 实际披露的机制与实验。方法定位为 arXiv:2602.07223v1 HTML — §4 Implementation；验证定位为 arXiv:2602.07223v1 HTML — §5.2 Reasoning Workloads with Short Input Context；独立 limitations 未披露，因而采用更窄主张。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-07223:end -->
<!-- review:SF-2026-ARXIV-2602-07223:end -->

<!-- review:SF-2026-ARXIV-2602-07263:start -->
### tLoRA: Efficient Multi-LoRA Training with Elastic Shared Super-Models

- **Review route:** `deep`；Primary=`arXiv:2602.07263v1`；owner=`TRAIN-LORA`。

- **问题与旧路径：** `tLoRA: Efficient Multi-LoRA Training with Elastic Shared Super-Models` 是否在 `TRAIN-LORA` 中改变已有状态、数据或控制责任；旧路径仍成立于：全参数微调保持统一参数语义，模型较小时最简单。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.07263v1 HTML — §3 tLoRA Design` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 base weight identity、adapter state、merge 与 serving compatibility。触发约束是：参数、显存与多租户 adapter 数量增长后需要隔离可训练增量。

- **State / data / control owner：** `TRAIN-LORA` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** Not Disclosed — arXiv:2602.07263v1 does not disclose a public repository, release, commit, or executable artifact used by this review

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.07263v1 HTML — §4 Evaluation`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.07263v1 HTML — §A.2 Job completion time ablation studies`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：单任务、资源充足且最终只交付一个模型时全参数微调仍成立。

<!-- claim:SF-2026-ARXIV-2602-07263:start -->
- **Claim boundary:** 只支持 arXiv:2602.07263v1 实际披露的机制与实验。方法定位为 arXiv:2602.07263v1 HTML — §3 tLoRA Design；验证定位为 arXiv:2602.07263v1 HTML — §4 Evaluation；边界定位为 arXiv:2602.07263v1 HTML — §A.2 Job completion time ablation studies。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-07263:end -->
<!-- review:SF-2026-ARXIV-2602-07263:end -->

<!-- review:SF-2026-ARXIV-2602-07265:start -->
### XShare: Collaborative in-Batch Expert Sharing for Faster MoE Inference

- **Review route:** `deep`；Primary=`arXiv:2602.07265v1`；owner=`MODEL-MOE`。

- **问题与旧路径：** `XShare: Collaborative in-Batch Expert Sharing for Faster MoE Inference` 是否在 `MODEL-MOE` 中改变已有状态、数据或控制责任；旧路径仍成立于：dense 层让每个 token 经过同一参数路径，训练与部署最规则。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.07265v1 HTML — §3.4 Practical Algorithm` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 expert 选择、capacity、placement 与通信。触发约束是：容量扩大后，激活成本和通信使全参数计算不可持续。

- **State / data / control owner：** `MODEL-MOE` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** External link observed in exact-v1 body: https://huggingface.co/datasets/math-ai/aime25; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.07265v1 HTML — §6 Experiments`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** exact-v1 未披露独立 limitations（`Not Disclosed — exact-v1 HTML has no independent limitations or counterevidence section; a positive conclusion does not replace that facet`）；这意味着审阅必须缩小主张，而不是把缺口当作反证。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：规模较小、负载难预测或通信昂贵时 dense 仍可能占优。

<!-- claim:SF-2026-ARXIV-2602-07265:start -->
- **Claim boundary:** 只支持 arXiv:2602.07265v1 实际披露的机制与实验。方法定位为 arXiv:2602.07265v1 HTML — §3.4 Practical Algorithm；验证定位为 arXiv:2602.07265v1 HTML — §6 Experiments；独立 limitations 未披露，因而采用更窄主张。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-07265:end -->
<!-- review:SF-2026-ARXIV-2602-07265:end -->

<!-- review:SF-2026-ARXIV-2602-07397:start -->
### Scout Before You Attend: Sketch-and-Walk Sparse Attention for Efficient LLM Inference

- **Review route:** `deep`；Primary=`arXiv:2602.07397v1`；owner=`MODEL-LONG-CONTEXT`。

- **问题与旧路径：** `Scout Before You Attend: Sketch-and-Walk Sparse Attention for Efficient LLM Inference` 是否在 `MODEL-LONG-CONTEXT` 中改变已有状态、数据或控制责任；旧路径仍成立于：全量 attention 保留任意 token 交互，在中短序列上最直接。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.07397v1 HTML — §2 Sketch and Walk` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 上下文选择、层次化表示和可访问记忆的语义边界。触发约束是：序列增长令计算、显存和信息稀释同时恶化。

- **State / data / control owner：** `MODEL-LONG-CONTEXT` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** Not Disclosed — arXiv:2602.07397v1 does not disclose a public repository, release, commit, or executable artifact used by this review

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.07397v1 HTML — §4.3 Efficiency Evaluation`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.07397v1 HTML — §4.4 Ablation Studies`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：任务确实依赖密集全局交互且长度可控时全量 attention 仍是基线。

<!-- claim:SF-2026-ARXIV-2602-07397:start -->
- **Claim boundary:** 只支持 arXiv:2602.07397v1 实际披露的机制与实验。方法定位为 arXiv:2602.07397v1 HTML — §2 Sketch and Walk；验证定位为 arXiv:2602.07397v1 HTML — §4.3 Efficiency Evaluation；边界定位为 arXiv:2602.07397v1 HTML — §4.4 Ablation Studies。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-07397:end -->
<!-- review:SF-2026-ARXIV-2602-07397:end -->

<!-- review:SF-2026-ARXIV-2602-07398:start -->
### AgentSys: Secure and Dynamic LLM Agents Through Explicit Hierarchical Memory Management

- **Review route:** `deep`；Primary=`arXiv:2602.07398v1`；owner=`AGENT-MEMORY`。

- **问题与旧路径：** `AgentSys: Secure and Dynamic LLM Agents Through Explicit Hierarchical Memory Management` 是否在 `AGENT-MEMORY` 中改变已有状态、数据或控制责任；旧路径仍成立于：把全部历史直接放回 context，短会话下最忠实也最少引入派生状态。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.07398v1 HTML — §5.1 System Overview` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 memory 的写入、版本、检索与失效控制权。触发约束是：长时交互、容量和权限约束迫使系统决定何时写、如何索引、何时遗忘。

- **State / data / control owner：** `AGENT-MEMORY` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** External link observed in exact-v1 body: https://github.com/ruoyaow/agentsys-memory; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.07398v1 HTML — §6.1 Evaluation on Benchmarks`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.07398v1 HTML — §7 Discussion`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：短会话或不可接受派生状态漂移时仍应回退原始 context。

<!-- claim:SF-2026-ARXIV-2602-07398:start -->
- **Claim boundary:** 只支持 arXiv:2602.07398v1 实际披露的机制与实验。方法定位为 arXiv:2602.07398v1 HTML — §5.1 System Overview；验证定位为 arXiv:2602.07398v1 HTML — §6.1 Evaluation on Benchmarks；边界定位为 arXiv:2602.07398v1 HTML — §7 Discussion。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-07398:end -->
<!-- review:SF-2026-ARXIV-2602-07398:end -->

<!-- review:SF-2026-ARXIV-2602-07595:start -->
### TeleBoost: A Systematic Alignment Framework for High-Fidelity, Controllable, and Robust Video Generation

- **Review route:** `deep`；Primary=`arXiv:2602.07595v1`；owner=`TRAIN-RLHF`。

- **问题与旧路径：** `TeleBoost: A Systematic Alignment Framework for High-Fidelity, Controllable, and Robust Video Generation` 是否在 `TRAIN-RLHF` 中改变已有状态、数据或控制责任；旧路径仍成立于：固定后训练配方便于重复和对比。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.07595v1 HTML — §6.1 A Ray-based Resource-Efficient Parallel Framework for GRPO` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 rollout、reward、policy/reference 与更新 freshness。触发约束是：模型规模、奖励来源和任务 horizon 改变后，同一配方的排序可能反转。

- **State / data / control owner：** `TRAIN-RLHF` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** External link observed in exact-v1 body: https://github.com/Tele-AI; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.07595v1 HTML — §7.3 Objective Evaluation: Benchmarks and Ablations`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.07595v1 HTML — §8 Conclusion`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：反馈稳定、任务窄且分布固定时成熟配方仍可复用。

<!-- claim:SF-2026-ARXIV-2602-07595:start -->
- **Claim boundary:** 只支持 arXiv:2602.07595v1 实际披露的机制与实验。方法定位为 arXiv:2602.07595v1 HTML — §6.1 A Ray-based Resource-Efficient Parallel Framework for GRPO；验证定位为 arXiv:2602.07595v1 HTML — §7.3 Objective Evaluation: Benchmarks and Ablations；边界定位为 arXiv:2602.07595v1 HTML — §8 Conclusion。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-07595:end -->
<!-- review:SF-2026-ARXIV-2602-07595:end -->

<!-- review:SF-2026-ARXIV-2602-07616:start -->
### SERE: Similarity-based Expert Re-routing for Efficient Batch Decoding in MoE Models

- **Review route:** `deep`；Primary=`arXiv:2602.07616v1`；owner=`MODEL-MOE`。

- **问题与旧路径：** `SERE: Similarity-based Expert Re-routing for Efficient Batch Decoding in MoE Models` 是否在 `MODEL-MOE` 中改变已有状态、数据或控制责任；旧路径仍成立于：dense 层让每个 token 经过同一参数路径，训练与部署最规则。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.07616v1 PDF — §method for Efficient batch decoding in MoE models. SERE dynamically reduces` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 expert 选择、capacity、placement 与通信。触发约束是：容量扩大后，激活成本和通信使全参数计算不可持续。

- **State / data / control owner：** `MODEL-MOE` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** External link observed in exact-v1 body: https://github.com/JL-Cheng/SERE; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.07616v1 PDF — §experiments are conducted on NVIDIA H20 GPUs.`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** exact-v1 未披露独立 limitations（`Not Disclosed — exact-v1 PDF 全文已审计但未提供独立 Limitations 章节`）；这意味着审阅必须缩小主张，而不是把缺口当作反证。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：规模较小、负载难预测或通信昂贵时 dense 仍可能占优。

<!-- claim:SF-2026-ARXIV-2602-07616:start -->
- **Claim boundary:** 只支持 arXiv:2602.07616v1 实际披露的机制与实验。方法定位为 arXiv:2602.07616v1 PDF — §method for Efficient batch decoding in MoE models. SERE dynamically reduces；验证定位为 arXiv:2602.07616v1 PDF — §experiments are conducted on NVIDIA H20 GPUs.；独立 limitations 未披露，因而采用更窄主张。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-07616:end -->
<!-- review:SF-2026-ARXIV-2602-07616:end -->

<!-- review:SF-2026-ARXIV-2602-07840:start -->
### SAGE: Scalable AI Governance &amp; Evaluation

- **Review route:** `deep`；Primary=`arXiv:2602.07840v1`；owner=`PLATFORM-EVALUATION-SYSTEM`。

- **问题与旧路径：** `SAGE: Scalable AI Governance &amp; Evaluation` 是否在 `PLATFORM-EVALUATION-SYSTEM` 中改变已有状态、数据或控制责任；旧路径仍成立于：单一离线分数便于比较版本。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.07840v1 HTML — §3. Problem Formulation and Framework` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 evaluation contract、覆盖分母、evidence lineage 与 release gate。触发约束是：agent、长时程和多模态系统把失败分散到状态、工具与环境交互链。

- **State / data / control owner：** `PLATFORM-EVALUATION-SYSTEM` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** Not Disclosed — arXiv:2602.07840v1 does not disclose a public repository, release, commit, or executable artifact used by this review

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.07840v1 HTML — §5.3. Experiments: Optimizing the Student Model`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** exact-v1 未披露独立 limitations（`Not Disclosed — exact-v1 HTML 全文已审计但未提供独立 Limitations 章节`）；这意味着审阅必须缩小主张，而不是把缺口当作反证。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：窄任务且 failure surface 稳定时单指标仍可作为局部信号。

<!-- claim:SF-2026-ARXIV-2602-07840:start -->
- **Claim boundary:** 只支持 arXiv:2602.07840v1 实际披露的机制与实验。方法定位为 arXiv:2602.07840v1 HTML — §3. Problem Formulation and Framework；验证定位为 arXiv:2602.07840v1 HTML — §5.3. Experiments: Optimizing the Student Model；独立 limitations 未披露，因而采用更窄主张。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-07840:end -->
<!-- review:SF-2026-ARXIV-2602-07840:end -->

<!-- review:SF-2026-ARXIV-2602-07962:start -->
### LOCA-bench: Benchmarking Language Agents Under Controllable and Extreme Context Growth

- **Review route:** `deep`；Primary=`arXiv:2602.07962v1`；owner=`PLATFORM-EVALUATION-SYSTEM`。

- **问题与旧路径：** `LOCA-bench: Benchmarking Language Agents Under Controllable and Extreme Context Growth` 是否在 `PLATFORM-EVALUATION-SYSTEM` 中改变已有状态、数据或控制责任；旧路径仍成立于：单一离线分数便于比较版本。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.07962v1 HTML — §2.3 Implementation` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 evaluation contract、覆盖分母、evidence lineage 与 release gate。触发约束是：agent、长时程和多模态系统把失败分散到状态、工具与环境交互链。

- **State / data / control owner：** `PLATFORM-EVALUATION-SYSTEM` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** External link observed in exact-v1 body: https://github.com/gkamradt/LLMTest_NeedleInAHaystack; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.07962v1 HTML — §3.2 Main Results`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.07962v1 HTML — §3.3 Failure Mode Analysis`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：窄任务且 failure surface 稳定时单指标仍可作为局部信号。

<!-- claim:SF-2026-ARXIV-2602-07962:start -->
- **Claim boundary:** 只支持 arXiv:2602.07962v1 实际披露的机制与实验。方法定位为 arXiv:2602.07962v1 HTML — §2.3 Implementation；验证定位为 arXiv:2602.07962v1 HTML — §3.2 Main Results；边界定位为 arXiv:2602.07962v1 HTML — §3.3 Failure Mode Analysis。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-07962:end -->
<!-- review:SF-2026-ARXIV-2602-07962:end -->

<!-- review:SF-2026-ARXIV-2602-07996:start -->
### The Judge Who Never Admits: Hidden Shortcuts in LLM-based Evaluation

- **Review route:** `deep`；Primary=`arXiv:2602.07996v1`；owner=`PLATFORM-EVALUATION-SYSTEM`。

- **问题与旧路径：** `The Judge Who Never Admits: Hidden Shortcuts in LLM-based Evaluation` 是否在 `PLATFORM-EVALUATION-SYSTEM` 中改变已有状态、数据或控制责任；旧路径仍成立于：单一离线分数便于比较版本。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.07996v1 HTML — §3.2 Cue Families` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 evaluation contract、覆盖分母、evidence lineage 与 release gate。触发约束是：agent、长时程和多模态系统把失败分散到状态、工具与环境交互链。

- **State / data / control owner：** `PLATFORM-EVALUATION-SYSTEM` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** Not Disclosed — arXiv:2602.07996v1 does not disclose a public repository, release, commit, or executable artifact used by this review

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.07996v1 HTML — §LLM judges exhibit a strong and largely unacknowledged recency bias.`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.07996v1 HTML — §6 Limitations`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：窄任务且 failure surface 稳定时单指标仍可作为局部信号。

<!-- claim:SF-2026-ARXIV-2602-07996:start -->
- **Claim boundary:** 只支持 arXiv:2602.07996v1 实际披露的机制与实验。方法定位为 arXiv:2602.07996v1 HTML — §3.2 Cue Families；验证定位为 arXiv:2602.07996v1 HTML — §LLM judges exhibit a strong and largely unacknowledged recency bias.；边界定位为 arXiv:2602.07996v1 HTML — §6 Limitations。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-07996:end -->
<!-- review:SF-2026-ARXIV-2602-07996:end -->

<!-- review:SF-2026-ARXIV-2602-08005:start -->
### DeltaKV: Residual-Based KV Cache Compression via Long-Range Similarity

- **Review route:** `deep`；Primary=`arXiv:2602.08005v1`；owner=`INFER-KV-CACHE`。

- **问题与旧路径：** `DeltaKV: Residual-Based KV Cache Compression via Long-Range Similarity` 是否在 `INFER-KV-CACHE` 中改变已有状态、数据或控制责任；旧路径仍成立于：完整、逐 token 保存 KV，换取语义透明和最低重算风险。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.08005v1 HTML — §4.3 Sparse-vLLM Implementation` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 KV 的 identity、压缩、复用、放置与失效状态。触发约束是：长上下文、多会话和异构层级使 KV 容量、带宽及身份成为主瓶颈。

- **State / data / control owner：** `INFER-KV-CACHE` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** External link observed in exact-v1 body: https://github.com/CURRENTF/Sparse-vLLM; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.08005v1 HTML — §Evaluation`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.08005v1 HTML — §B.5 Detailed Latency Profiling and Future Optimization`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：小 batch、短上下文或严格 exactness 场景仍宜保留完整 KV。

<!-- claim:SF-2026-ARXIV-2602-08005:start -->
- **Claim boundary:** 只支持 arXiv:2602.08005v1 实际披露的机制与实验。方法定位为 arXiv:2602.08005v1 HTML — §4.3 Sparse-vLLM Implementation；验证定位为 arXiv:2602.08005v1 HTML — §Evaluation；边界定位为 arXiv:2602.08005v1 HTML — §B.5 Detailed Latency Profiling and Future Optimization。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-08005:end -->
<!-- review:SF-2026-ARXIV-2602-08005:end -->

<!-- review:SF-2026-ARXIV-2602-08060:start -->
### Compiler-Assisted Speculative Sampling for Accelerated LLM Inference on Heterogeneous Edge Devices

- **Review route:** `deep`；Primary=`arXiv:2602.08060v1`；owner=`INFER-SPECULATIVE-DECODING`。

- **问题与旧路径：** `Compiler-Assisted Speculative Sampling for Accelerated LLM Inference on Heterogeneous Edge Devices` 是否在 `INFER-SPECULATIVE-DECODING` 中改变已有状态、数据或控制责任；旧路径仍成立于：逐 token 串行验证保持 exactness，且不维护额外 draft 状态。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.08060v1 HTML — §III Heterogeneous Mapping Framework for Speculative Sampling` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 proposal、验证、接受/回滚与缓存提交状态。触发约束是：decode 的串行依赖限制利用率，促使系统用廉价 proposal 换取并行验证。

- **State / data / control owner：** `INFER-SPECULATIVE-DECODING` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** External link observed in exact-v1 body: https://github.com/intel/neural-compressor; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.08060v1 HTML — §IV Experimental Setup and Evaluation`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.08060v1 HTML — §IV-D Validation and Discussion`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：接受率低、draft 成本高或状态提交复杂时普通 decode 仍成立。

<!-- claim:SF-2026-ARXIV-2602-08060:start -->
- **Claim boundary:** 只支持 arXiv:2602.08060v1 实际披露的机制与实验。方法定位为 arXiv:2602.08060v1 HTML — §III Heterogeneous Mapping Framework for Speculative Sampling；验证定位为 arXiv:2602.08060v1 HTML — §IV Experimental Setup and Evaluation；边界定位为 arXiv:2602.08060v1 HTML — §IV-D Validation and Discussion。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-08060:end -->
<!-- review:SF-2026-ARXIV-2602-08060:end -->

<!-- review:SF-2026-ARXIV-2602-08237:start -->
### Document Reconstruction Unlocks Scalable Long-Context RLVR

- **Review route:** `deep`；Primary=`arXiv:2602.08237v1`；owner=`TRAIN-RLHF`。

- **问题与旧路径：** `Document Reconstruction Unlocks Scalable Long-Context RLVR` 是否在 `TRAIN-RLHF` 中改变已有状态、数据或控制责任；旧路径仍成立于：固定后训练配方便于重复和对比。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.08237v1 PDF — §Method` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 rollout、reward、policy/reference 与更新 freshness。触发约束是：模型规模、奖励来源和任务 horizon 改变后，同一配方的排序可能反转。

- **State / data / control owner：** `TRAIN-RLHF` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** External link observed in exact-v1 body: https://github.com/XYaoooo/reconstruction; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.08237v1 PDF — §Evaluation. Benchmarks. We evaluate all models on two challenging long-context QA`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.08237v1 PDF — §Limitations`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：反馈稳定、任务窄且分布固定时成熟配方仍可复用。

<!-- claim:SF-2026-ARXIV-2602-08237:start -->
- **Claim boundary:** 只支持 arXiv:2602.08237v1 实际披露的机制与实验。方法定位为 arXiv:2602.08237v1 PDF — §Method；验证定位为 arXiv:2602.08237v1 PDF — §Evaluation. Benchmarks. We evaluate all models on two challenging long-context QA；边界定位为 arXiv:2602.08237v1 PDF — §Limitations。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-08237:end -->
<!-- review:SF-2026-ARXIV-2602-08237:end -->

<!-- review:SF-2026-ARXIV-2602-08296:start -->
### MonkeyTree: Near-Minimal Congestion for Multi-tenant Training via Migration

- **Review route:** `deep`；Primary=`arXiv:2602.08296v1`；owner=`PLATFORM-GPU-SCHEDULER`。

- **问题与旧路径：** `MonkeyTree: Near-Minimal Congestion for Multi-tenant Training via Migration` 是否在 `PLATFORM-GPU-SCHEDULER` 中改变已有状态、数据或控制责任；旧路径仍成立于：独占 GPU 提供最清晰的隔离和性能归因。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.08296v1 HTML — §4. MonkeyTree System Design` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 GPU slice、隔离、配额与抢占控制。触发约束是：并发 workload 与成本压力要求共享，同时又不能破坏确定性。

- **State / data / control owner：** `PLATFORM-GPU-SCHEDULER` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** External link observed in exact-v1 body: https://huggingface.co/meta-llama/Llama-2-70b; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.08296v1 HTML — §6. Evaluation`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.08296v1 HTML — §8. Discussion`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：高风险或稳定满载任务仍宜独占。

<!-- claim:SF-2026-ARXIV-2602-08296:start -->
- **Claim boundary:** 只支持 arXiv:2602.08296v1 实际披露的机制与实验。方法定位为 arXiv:2602.08296v1 HTML — §4. MonkeyTree System Design；验证定位为 arXiv:2602.08296v1 HTML — §6. Evaluation；边界定位为 arXiv:2602.08296v1 HTML — §8. Discussion。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-08296:end -->
<!-- review:SF-2026-ARXIV-2602-08296:end -->

<!-- review:SF-2026-ARXIV-2602-08343:start -->
### ManifoldKV: Training-Free KV Cache Compression via Euclidean Outlier Detection

- **Review route:** `deep`；Primary=`arXiv:2602.08343v1`；owner=`INFER-KV-CACHE`。

- **问题与旧路径：** `ManifoldKV: Training-Free KV Cache Compression via Euclidean Outlier Detection` 是否在 `INFER-KV-CACHE` 中改变已有状态、数据或控制责任；旧路径仍成立于：完整、逐 token 保存 KV，换取语义透明和最低重算风险。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.08343v1 HTML — §E.1 Methodology` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 KV 的 identity、压缩、复用、放置与失效状态。触发约束是：长上下文、多会话和异构层级使 KV 容量、带宽及身份成为主瓶颈。

- **State / data / control owner：** `INFER-KV-CACHE` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** Not Disclosed — arXiv:2602.08343v1 does not disclose a public repository, release, commit, or executable artifact used by this review

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.08343v1 HTML — §5.2 Main Results`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.08343v1 HTML — §6 Discussion`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：小 batch、短上下文或严格 exactness 场景仍宜保留完整 KV。

<!-- claim:SF-2026-ARXIV-2602-08343:start -->
- **Claim boundary:** 只支持 arXiv:2602.08343v1 实际披露的机制与实验。方法定位为 arXiv:2602.08343v1 HTML — §E.1 Methodology；验证定位为 arXiv:2602.08343v1 HTML — §5.2 Main Results；边界定位为 arXiv:2602.08343v1 HTML — §6 Discussion。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-08343:end -->
<!-- review:SF-2026-ARXIV-2602-08343:end -->

<!-- review:SF-2026-ARXIV-2602-08382:start -->
### Dynamic Long Context Reasoning over Compressed Memory via End-to-End Reinforcement Learning

- **Review route:** `deep`；Primary=`arXiv:2602.08382v1`；owner=`MODEL-LONG-CONTEXT`。

- **问题与旧路径：** `Dynamic Long Context Reasoning over Compressed Memory via End-to-End Reinforcement Learning` 是否在 `MODEL-LONG-CONTEXT` 中改变已有状态、数据或控制责任；旧路径仍成立于：全量 attention 保留任意 token 交互，在中短序列上最直接。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.08382v1 HTML — §Appendix A Implementation Details` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 上下文选择、层次化表示和可访问记忆的语义边界。触发约束是：序列增长令计算、显存和信息稀释同时恶化。

- **State / data / control owner：** `MODEL-LONG-CONTEXT` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** Not Disclosed — arXiv:2602.08382v1 does not disclose a public repository, release, commit, or executable artifact used by this review

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.08382v1 HTML — §4.2 Main Results`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.08382v1 HTML — §Appendix C Failure Mode Analysis`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：任务确实依赖密集全局交互且长度可控时全量 attention 仍是基线。

<!-- claim:SF-2026-ARXIV-2602-08382:start -->
- **Claim boundary:** 只支持 arXiv:2602.08382v1 实际披露的机制与实验。方法定位为 arXiv:2602.08382v1 HTML — §Appendix A Implementation Details；验证定位为 arXiv:2602.08382v1 HTML — §4.2 Main Results；边界定位为 arXiv:2602.08382v1 HTML — §Appendix C Failure Mode Analysis。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-08382:end -->
<!-- review:SF-2026-ARXIV-2602-08382:end -->

<!-- review:SF-2026-ARXIV-2602-08401:start -->
### On Protecting Agentic Systems' Intellectual Property via Watermarking

- **Review route:** `deep`；Primary=`arXiv:2602.08401v1`；owner=`PLATFORM-SECURITY`。

- **问题与旧路径：** `On Protecting Agentic Systems' Intellectual Property via Watermarking` 是否在 `PLATFORM-SECURITY` 中改变已有状态、数据或控制责任；旧路径仍成立于：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.08401v1 HTML — §IV Methodology` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 身份、授权、数据流、策略执行点与审计证据。触发约束是：工具、记忆和多 agent 委托把不可信内容转化为可执行控制流。

- **State / data / control owner：** `PLATFORM-SECURITY` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** External link observed in exact-v1 body: https://huggingface.co/Qwen/Qwen3-Embedding-0.6B; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.08401v1 HTML — §VII Evaluation`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.08401v1 HTML — §VIII Conclusion`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：无工具、无持久状态的只读场景仍可采用较薄边界。

<!-- claim:SF-2026-ARXIV-2602-08401:start -->
- **Claim boundary:** 只支持 arXiv:2602.08401v1 实际披露的机制与实验。方法定位为 arXiv:2602.08401v1 HTML — §IV Methodology；验证定位为 arXiv:2602.08401v1 HTML — §VII Evaluation；边界定位为 arXiv:2602.08401v1 HTML — §VIII Conclusion。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-08401:end -->
<!-- review:SF-2026-ARXIV-2602-08401:end -->

<!-- review:SF-2026-ARXIV-2602-08404:start -->
### TEAM: Temporal-Spatial Consistency Guided Expert Activation for MoE Diffusion Language Model Acceleration

- **Review route:** `deep`；Primary=`arXiv:2602.08404v1`；owner=`INFER-TENSORRT-LLM`。

- **问题与旧路径：** `TEAM: Temporal-Spatial Consistency Guided Expert Activation for MoE Diffusion Language Model Acceleration` 是否在 `INFER-TENSORRT-LLM` 中改变已有状态、数据或控制责任；旧路径仍成立于：通用 eager 执行便于调试且无需额外编译状态。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.08404v1 HTML — §3.2 Delayed Caching for Decoded Tokens (DCD)` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 graph lowering、kernel/precision 选择与执行计划版本。触发约束是：模型规模、算子形态和 SLO 使执行计划、精度与 kernel 选择成为主要成本。

- **State / data / control owner：** `INFER-TENSORRT-LLM` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** External link observed in exact-v1 body: https://github.com/PKU-SEC-Lab/TEAM-MoE-dLLM; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.08404v1 HTML — §4.2 Main Results`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.08404v1 HTML — §4.3 Ablation Study and Analysis`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：工作负载小、形状动态或调试优先时 eager 路径仍合理。

<!-- claim:SF-2026-ARXIV-2602-08404:start -->
- **Claim boundary:** 只支持 arXiv:2602.08404v1 实际披露的机制与实验。方法定位为 arXiv:2602.08404v1 HTML — §3.2 Delayed Caching for Decoded Tokens (DCD)；验证定位为 arXiv:2602.08404v1 HTML — §4.2 Main Results；边界定位为 arXiv:2602.08404v1 HTML — §4.3 Ablation Study and Analysis。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-08404:end -->
<!-- review:SF-2026-ARXIV-2602-08404:end -->

<!-- review:SF-2026-ARXIV-2602-08412:start -->
### From Assistant to Double Agent: Formalizing and Benchmarking Attacks on OpenClaw for Personalized Local AI Agent

- **Review route:** `deep`；Primary=`arXiv:2602.08412v1`；owner=`PLATFORM-SECURITY`。

- **问题与旧路径：** `From Assistant to Double Agent: Formalizing and Benchmarking Attacks on OpenClaw for Personalized Local AI Agent` 是否在 `PLATFORM-SECURITY` 中改变已有状态、数据或控制责任；旧路径仍成立于：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.08412v1 HTML — §2.4 Attack Primitives` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 身份、授权、数据流、策略执行点与审计证据。触发约束是：工具、记忆和多 agent 委托把不可信内容转化为可执行控制流。

- **State / data / control owner：** `PLATFORM-SECURITY` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** External link observed in exact-v1 body: https://github.com/AstorYH/PASB; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.08412v1 HTML — §3.2 Main Results and Analysis`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.08412v1 HTML — §4 Conclusion and Future Work`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：无工具、无持久状态的只读场景仍可采用较薄边界。

<!-- claim:SF-2026-ARXIV-2602-08412:start -->
- **Claim boundary:** 只支持 arXiv:2602.08412v1 实际披露的机制与实验。方法定位为 arXiv:2602.08412v1 HTML — §2.4 Attack Primitives；验证定位为 arXiv:2602.08412v1 HTML — §3.2 Main Results and Analysis；边界定位为 arXiv:2602.08412v1 HTML — §4 Conclusion and Future Work。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-08412:end -->
<!-- review:SF-2026-ARXIV-2602-08412:end -->

<!-- review:SF-2026-ARXIV-2602-08563:start -->
### Stateless Yet Not Forgetful: Implicit Memory as a Hidden Channel in LLMs

- **Review route:** `deep`；Primary=`arXiv:2602.08563v1`；owner=`AGENT-MEMORY`。

- **问题与旧路径：** `Stateless Yet Not Forgetful: Implicit Memory as a Hidden Channel in LLMs` 是否在 `AGENT-MEMORY` 中改变已有状态、数据或控制责任；旧路径仍成立于：把全部历史直接放回 context，短会话下最忠实也最少引入派生状态。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.08563v1 HTML — §III Implicit Memory in LLMs: Definition, Threat Model, and Feasibility` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 memory 的写入、版本、检索与失效控制权。触发约束是：长时交互、容量和权限约束迫使系统决定何时写、如何索引、何时遗忘。

- **State / data / control owner：** `AGENT-MEMORY` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** External link observed in exact-v1 body: https://github.com/microsoft/implicitMemory; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.08563v1 HTML — §VII Time Bomb: A Temporal Backdoor via Implicit Memory`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.08563v1 HTML — §IX Future Directions`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：短会话或不可接受派生状态漂移时仍应回退原始 context。

<!-- claim:SF-2026-ARXIV-2602-08563:start -->
- **Claim boundary:** 只支持 arXiv:2602.08563v1 实际披露的机制与实验。方法定位为 arXiv:2602.08563v1 HTML — §III Implicit Memory in LLMs: Definition, Threat Model, and Feasibility；验证定位为 arXiv:2602.08563v1 HTML — §VII Time Bomb: A Temporal Backdoor via Implicit Memory；边界定位为 arXiv:2602.08563v1 HTML — §IX Future Directions。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-08563:end -->
<!-- review:SF-2026-ARXIV-2602-08563:end -->

<!-- review:SF-2026-ARXIV-2602-08585:start -->
### Predicting Future Utility: Global Combinatorial Optimization for Task-Agnostic KV Cache Eviction

- **Review route:** `deep`；Primary=`arXiv:2602.08585v1`；owner=`INFER-KV-CACHE`。

- **问题与旧路径：** `Predicting Future Utility: Global Combinatorial Optimization for Task-Agnostic KV Cache Eviction` 是否在 `INFER-KV-CACHE` 中改变已有状态、数据或控制责任；旧路径仍成立于：完整、逐 token 保存 KV，换取语义透明和最低重算风险。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.08585v1 HTML — §4.3 Practical Implementation: Offline Profiling` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 KV 的 identity、压缩、复用、放置与失效状态。触发约束是：长上下文、多会话和异构层级使 KV 容量、带宽及身份成为主瓶颈。

- **State / data / control owner：** `INFER-KV-CACHE` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** External link observed in exact-v1 body: https://github.com/NVIDIA/kvpress; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.08585v1 HTML — §5.4 Ablation Study`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.08585v1 HTML — §Limitation of Heuristic Metric.`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：小 batch、短上下文或严格 exactness 场景仍宜保留完整 KV。

<!-- claim:SF-2026-ARXIV-2602-08585:start -->
- **Claim boundary:** 只支持 arXiv:2602.08585v1 实际披露的机制与实验。方法定位为 arXiv:2602.08585v1 HTML — §4.3 Practical Implementation: Offline Profiling；验证定位为 arXiv:2602.08585v1 HTML — §5.4 Ablation Study；边界定位为 arXiv:2602.08585v1 HTML — §Limitation of Heuristic Metric.。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-08585:end -->
<!-- review:SF-2026-ARXIV-2602-08585:end -->

<!-- review:SF-2026-ARXIV-2602-08621:start -->
### Sparse Models, Sparse Safety: Unsafe Routes in Mixture-of-Experts LLMs

- **Review route:** `deep`；Primary=`arXiv:2602.08621v1`；owner=`PLATFORM-SECURITY`。

- **问题与旧路径：** `Sparse Models, Sparse Safety: Unsafe Routes in Mixture-of-Experts LLMs` 是否在 `PLATFORM-SECURITY` 中改变已有状态、数据或控制责任；旧路径仍成立于：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.08621v1 HTML — §Our Proposed F-SOUR` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 身份、授权、数据流、策略执行点与审计证据。触发约束是：工具、记忆和多 agent 委托把不可信内容转化为可执行控制流。

- **State / data / control owner：** `PLATFORM-SECURITY` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** External link observed in exact-v1 body: https://github.com/TrustAIRLab/UnsafeMoE; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.08621v1 HTML — §Experimental Results`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.08621v1 HTML — §Appendix G Limitations and Future Work`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：无工具、无持久状态的只读场景仍可采用较薄边界。

<!-- claim:SF-2026-ARXIV-2602-08621:start -->
- **Claim boundary:** 只支持 arXiv:2602.08621v1 实际披露的机制与实验。方法定位为 arXiv:2602.08621v1 HTML — §Our Proposed F-SOUR；验证定位为 arXiv:2602.08621v1 HTML — §Experimental Results；边界定位为 arXiv:2602.08621v1 HTML — §Appendix G Limitations and Future Work。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-08621:end -->
<!-- review:SF-2026-ARXIV-2602-08621:end -->

<!-- review:SF-2026-ARXIV-2602-08722:start -->
### QUOKA: Query-Oriented KV Selection For Efficient LLM Prefill

- **Review route:** `deep`；Primary=`arXiv:2602.08722v1`；owner=`INFER-PREFILL`。

- **问题与旧路径：** `QUOKA: Query-Oriented KV Selection For Efficient LLM Prefill` 是否在 `INFER-PREFILL` 中改变已有状态、数据或控制责任；旧路径仍成立于：Prefill 对完整 prompt 做 dense forward，语义与实现最直接。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.08722v1 HTML — §3 QuoKA Method` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 prompt token、attention work、prefill plan 与 KV materialization。触发约束是：长输入和异构硬件使 token 选择、并行与带宽成为 TTFT 主约束。

- **State / data / control owner：** `INFER-PREFILL` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** External link observed in exact-v1 body: https://github.com/gkamradt/LLMTest_NeedleInAHaystack; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.08722v1 HTML — §4 results`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.08722v1 HTML — §4.5 Ablation study`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：输入较短或 exact dense attention 必须保留时完整 Prefill 仍合理。

<!-- claim:SF-2026-ARXIV-2602-08722:start -->
- **Claim boundary:** 只支持 arXiv:2602.08722v1 实际披露的机制与实验。方法定位为 arXiv:2602.08722v1 HTML — §3 QuoKA Method；验证定位为 arXiv:2602.08722v1 HTML — §4 results；边界定位为 arXiv:2602.08722v1 HTML — §4.5 Ablation study。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-08722:end -->
<!-- review:SF-2026-ARXIV-2602-08722:end -->

<!-- review:SF-2026-ARXIV-2602-08747:start -->
### PARD: Enhancing Goodput for Inference Pipeline via Proactive Request Dropping

- **Review route:** `deep`；Primary=`arXiv:2602.08747v1`；owner=`INFER-SCHEDULING`。

- **问题与旧路径：** `PARD: Enhancing Goodput for Inference Pipeline via Proactive Request Dropping` 是否在 `INFER-SCHEDULING` 中改变已有状态、数据或控制责任；旧路径仍成立于：FIFO 或静态批次在请求同质时易预测、易实现。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.08747v1 HTML — §4. System Design` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 准入、批处理、优先级、路由和资源选择。触发约束是：长度、阶段、SLO、模型和 agent fan-out 的异质性使排队决策决定整体尾延迟。

- **State / data / control owner：** `INFER-SCHEDULING` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** External link observed in exact-v1 body: https://github.com/langchain-ai/langchain; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.08747v1 HTML — §5. Evaluation`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.08747v1 HTML — §7. Applicable to Other Workload`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：同质离线吞吐任务仍可使用简单静态策略。

<!-- claim:SF-2026-ARXIV-2602-08747:start -->
- **Claim boundary:** 只支持 arXiv:2602.08747v1 实际披露的机制与实验。方法定位为 arXiv:2602.08747v1 HTML — §4. System Design；验证定位为 arXiv:2602.08747v1 HTML — §5. Evaluation；边界定位为 arXiv:2602.08747v1 HTML — §7. Applicable to Other Workload。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-08747:end -->
<!-- review:SF-2026-ARXIV-2602-08747:end -->

<!-- review:SF-2026-ARXIV-2602-08798:start -->
### CryptoGen: Secure Transformer Generation with Encrypted KV-Cache Reuse

- **Review route:** `deep`；Primary=`arXiv:2602.08798v1`；owner=`PLATFORM-SECURITY`。

- **问题与旧路径：** `CryptoGen: Secure Transformer Generation with Encrypted KV-Cache Reuse` 是否在 `PLATFORM-SECURITY` 中改变已有状态、数据或控制责任；旧路径仍成立于：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.08798v1 HTML — §4.1 CryptoGen Framework` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 身份、授权、数据流、策略执行点与审计证据。触发约束是：工具、记忆和多 agent 委托把不可信内容转化为可执行控制流。

- **State / data / control owner：** `PLATFORM-SECURITY` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** External link observed in exact-v1 body: https://github.com/microsoft/SEAL; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.08798v1 HTML — §6.3 Breakdown Analysis of a Single Transformer Block`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** exact-v1 未披露独立 limitations（`Not Disclosed — exact-v1 HTML has no independent limitations or counterevidence section; a positive conclusion does not replace that facet`）；这意味着审阅必须缩小主张，而不是把缺口当作反证。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：无工具、无持久状态的只读场景仍可采用较薄边界。

<!-- claim:SF-2026-ARXIV-2602-08798:start -->
- **Claim boundary:** 只支持 arXiv:2602.08798v1 实际披露的机制与实验。方法定位为 arXiv:2602.08798v1 HTML — §4.1 CryptoGen Framework；验证定位为 arXiv:2602.08798v1 HTML — §6.3 Breakdown Analysis of a Single Transformer Block；独立 limitations 未披露，因而采用更窄主张。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-08798:end -->
<!-- review:SF-2026-ARXIV-2602-08798:end -->

<!-- review:SF-2026-ARXIV-2602-08905:start -->
### Efficient and Stable Reinforcement Learning for Diffusion Language Models

- **Review route:** `deep`；Primary=`arXiv:2602.08905v1`；owner=`TRAIN-RLHF`。

- **问题与旧路径：** `Efficient and Stable Reinforcement Learning for Diffusion Language Models` 是否在 `TRAIN-RLHF` 中改变已有状态、数据或控制责任；旧路径仍成立于：固定后训练配方便于重复和对比。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.08905v1 HTML — §5.2 Implementation Details` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 rollout、reward、policy/reference 与更新 freshness。触发约束是：模型规模、奖励来源和任务 horizon 改变后，同一配方的排序可能反转。

- **State / data / control owner：** `TRAIN-RLHF` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** External link observed in exact-v1 body: https://github.com/Jiayi-Pan/TinyZeroAccessed:; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.08905v1 HTML — §5.3 Main Results`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.08905v1 HTML — §7 Conclusion and Future Work`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：反馈稳定、任务窄且分布固定时成熟配方仍可复用。

<!-- claim:SF-2026-ARXIV-2602-08905:start -->
- **Claim boundary:** 只支持 arXiv:2602.08905v1 实际披露的机制与实验。方法定位为 arXiv:2602.08905v1 HTML — §5.2 Implementation Details；验证定位为 arXiv:2602.08905v1 HTML — §5.3 Main Results；边界定位为 arXiv:2602.08905v1 HTML — §7 Conclusion and Future Work。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-08905:end -->
<!-- review:SF-2026-ARXIV-2602-08905:end -->

<!-- review:SF-2026-ARXIV-2602-08968:start -->
### stable-worldmodel-v1: Reproducible World Modeling Research and Evaluation

- **Review route:** `deep`；Primary=`arXiv:2602.08968v1`；owner=`PLATFORM-EVALUATION-SYSTEM`。

- **问题与旧路径：** `stable-worldmodel-v1: Reproducible World Modeling Research and Evaluation` 是否在 `PLATFORM-EVALUATION-SYSTEM` 中改变已有状态、数据或控制责任；旧路径仍成立于：单一离线分数便于比较版本。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.08968v1 HTML — §2.3 SWM Evaluation Suite: Tasks, Planning Algorithms, and Baselines` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 evaluation contract、覆盖分母、evidence lineage 与 release gate。触发约束是：agent、长时程和多模态系统把失败分散到状态、工具与环境交互链。

- **State / data / control owner：** `PLATFORM-EVALUATION-SYSTEM` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** Not Disclosed — arXiv:2602.08968v1 does not disclose a public repository, release, commit, or executable artifact used by this review

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.08968v1 HTML — §2.3 SWM Evaluation Suite: Tasks, Planning Algorithms, and Baselines`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.08968v1 HTML — §4 Conclusion and Future Directions`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：窄任务且 failure surface 稳定时单指标仍可作为局部信号。

<!-- claim:SF-2026-ARXIV-2602-08968:start -->
- **Claim boundary:** 只支持 arXiv:2602.08968v1 实际披露的机制与实验。方法定位为 arXiv:2602.08968v1 HTML — §2.3 SWM Evaluation Suite: Tasks, Planning Algorithms, and Baselines；验证定位为 arXiv:2602.08968v1 HTML — §2.3 SWM Evaluation Suite: Tasks, Planning Algorithms, and Baselines；边界定位为 arXiv:2602.08968v1 HTML — §4 Conclusion and Future Directions。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-08968:end -->
<!-- review:SF-2026-ARXIV-2602-08968:end -->

## 4. Benchmark Contracts

None — 作者实验只在各 Source Review 的 evaluation contract 内支持机制判断；本日报不发布可跨 workload 外推的 benchmark claim。

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2602-07186 | score_7_9 | selected | DA-20260211-1 | — | 在同日 eligibility frontier 中优先选择 Total=9 且形成独立 `TRAIN-RLHF` 系统责任链的 family。 | analysis:DA-20260211-1 |
| SF-2026-ARXIV-2602-07306 | score_7_9; forced_review; potential_books_delta | selected | DA-20260211-2 | — | 在同日 eligibility frontier 中优先选择 Total=8 且形成独立 `MODEL-TRANSFORMER-LAYER` 系统责任链的 family。 | analysis:DA-20260211-2 |
| SF-2026-ARXIV-2602-07379 | score_7_9 | selected | DA-20260211-3 | — | 在同日 eligibility frontier 中优先选择 Total=8 且形成独立 `PLATFORM-SECURITY` 系统责任链的 family。 | analysis:DA-20260211-3 |
| SF-2026-ARXIV-2602-07721 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `INFER-KV-CACHE`；跨层影响较已选单元更窄，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-07721 |
| SF-2026-ARXIV-2602-07878 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `PLATFORM-SECURITY`；同 owner 已有更高优先级叙事单元，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-07878 |
| SF-2026-ARXIV-2602-08007 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `TRAIN-DISTRIBUTED-TRAINING`；跨层影响较已选单元更窄，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-08007 |
| SF-2026-ARXIV-2602-08847 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `AGENT-MULTI-AGENT`；跨层影响较已选单元更窄，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-08847 |
| SF-2026-ARXIV-2602-07120 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `MODEL-SAMPLING`；跨层影响较已选单元更窄，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-07120 |
| SF-2026-ARXIV-2602-07223 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `INFER-SPECULATIVE-DECODING`；跨层影响较已选单元更窄，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-07223 |
| SF-2026-ARXIV-2602-07263 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `TRAIN-LORA`；跨层影响较已选单元更窄，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-07263 |
| SF-2026-ARXIV-2602-07265 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `MODEL-MOE`；跨层影响较已选单元更窄，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-07265 |
| SF-2026-ARXIV-2602-07397 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `MODEL-LONG-CONTEXT`；跨层影响较已选单元更窄，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-07397 |
| SF-2026-ARXIV-2602-07398 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `AGENT-MEMORY`；跨层影响较已选单元更窄，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-07398 |
| SF-2026-ARXIV-2602-07595 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `TRAIN-RLHF`；同 owner 已有更高优先级叙事单元，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-07595 |
| SF-2026-ARXIV-2602-07616 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `MODEL-MOE`；跨层影响较已选单元更窄，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-07616 |
| SF-2026-ARXIV-2602-07840 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `PLATFORM-EVALUATION-SYSTEM`；跨层影响较已选单元更窄，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-07840 |
| SF-2026-ARXIV-2602-07962 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `PLATFORM-EVALUATION-SYSTEM`；跨层影响较已选单元更窄，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-07962 |
| SF-2026-ARXIV-2602-07996 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `PLATFORM-EVALUATION-SYSTEM`；跨层影响较已选单元更窄，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-07996 |
| SF-2026-ARXIV-2602-08005 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `INFER-KV-CACHE`；跨层影响较已选单元更窄，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-08005 |
| SF-2026-ARXIV-2602-08060 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `INFER-SPECULATIVE-DECODING`；跨层影响较已选单元更窄，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-08060 |
| SF-2026-ARXIV-2602-08237 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `TRAIN-RLHF`；同 owner 已有更高优先级叙事单元，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-08237 |
| SF-2026-ARXIV-2602-08296 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `PLATFORM-GPU-SCHEDULER`；跨层影响较已选单元更窄，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-08296 |
| SF-2026-ARXIV-2602-08343 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `INFER-KV-CACHE`；跨层影响较已选单元更窄，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-08343 |
| SF-2026-ARXIV-2602-08382 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `MODEL-LONG-CONTEXT`；跨层影响较已选单元更窄，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-08382 |
| SF-2026-ARXIV-2602-08401 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `PLATFORM-SECURITY`；同 owner 已有更高优先级叙事单元，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-08401 |
| SF-2026-ARXIV-2602-08404 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `INFER-TENSORRT-LLM`；跨层影响较已选单元更窄，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-08404 |
| SF-2026-ARXIV-2602-08412 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `PLATFORM-SECURITY`；同 owner 已有更高优先级叙事单元，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-08412 |
| SF-2026-ARXIV-2602-08563 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `AGENT-MEMORY`；跨层影响较已选单元更窄，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-08563 |
| SF-2026-ARXIV-2602-08585 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `INFER-KV-CACHE`；跨层影响较已选单元更窄，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-08585 |
| SF-2026-ARXIV-2602-08621 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `PLATFORM-SECURITY`；同 owner 已有更高优先级叙事单元，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-08621 |
| SF-2026-ARXIV-2602-08722 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `INFER-PREFILL`；跨层影响较已选单元更窄，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-08722 |
| SF-2026-ARXIV-2602-08747 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `INFER-SCHEDULING`；跨层影响较已选单元更窄，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-08747 |
| SF-2026-ARXIV-2602-08798 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `PLATFORM-SECURITY`；同 owner 已有更高优先级叙事单元，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-08798 |
| SF-2026-ARXIV-2602-08905 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `TRAIN-RLHF`；同 owner 已有更高优先级叙事单元，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-08905 |
| SF-2026-ARXIV-2602-08968 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `PLATFORM-EVALUATION-SYSTEM`；跨层影响较已选单元更窄，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-08968 |

<!-- analysis:DA-20260211-1:start -->
### DA-20260211-1 — The Value of Variance: Mitigating Debate Collapse in Multi-Agent Systems via Uncertainty-Driven Policy Optimization

旧路径在原 workload 下保持较低状态与控制开销；约束变化后，该 family 把新增机制责任定位到 `TRAIN-RLHF`。exact-v1 的 `arXiv:2602.07186v1 HTML — §4.2 Uncertainty-Driven Reward Design` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 rollout、reward、policy/reference 与更新 freshness。触发约束是：模型规模、奖励来源和任务 horizon 改变后，同一配方的排序可能反转。 公开验证定位在 `arXiv:2602.07186v1 HTML — §3.2 Evaluation Results`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。 代价、failure mode 与旧方案共存边界由以下证据限制：限制或反证定位在 `arXiv:2602.07186v1 HTML — §5.3 Ablation Study (RQ2)`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：反馈稳定、任务窄且分布固定时成熟配方仍可复用。
<!-- analysis:DA-20260211-1:end -->

<!-- analysis:DA-20260211-2:start -->
### DA-20260211-2 — Parallel Track Transformers: Enabling Fast GPU Inference with Reduced Synchronization

旧路径在原 workload 下保持较低状态与控制开销；约束变化后，该 family 把新增机制责任定位到 `MODEL-TRANSFORMER-LAYER`。exact-v1 的 `arXiv:2602.07306v1 HTML — §2 The Parallel Track Transformer Architecture` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 layer topology、residual merge、activation flow 与 synchronization boundary。触发约束是：跨设备执行把 block 内同步次数、分支合并和 collective placement 变成一等约束。 公开验证定位在 `arXiv:2602.07306v1 HTML — §3.3 Serving Evaluation`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。 代价、failure mode 与旧方案共存边界由以下证据限制：exact-v1 未披露独立 limitations（`Not Disclosed — exact-v1 HTML has no independent limitations or counterevidence section; a positive conclusion does not replace that facet`）；这意味着审阅必须缩小主张，而不是把缺口当作反证。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：单设备或通信不占主导时，标准串行 Transformer layer 仍更简单可靠。
<!-- analysis:DA-20260211-2:end -->

<!-- analysis:DA-20260211-3:start -->
### DA-20260211-3 — Aegis: Towards Governance, Integrity, and Security of AI Voice Agents

旧路径在原 workload 下保持较低状态与控制开销；约束变化后，该 family 把新增机制责任定位到 `PLATFORM-SECURITY`。exact-v1 的 `arXiv:2602.07379v1 HTML — §3.1 Framework` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 身份、授权、数据流、策略执行点与审计证据。触发约束是：工具、记忆和多 agent 委托把不可信内容转化为可执行控制流。 公开验证定位在 `arXiv:2602.07379v1 HTML — §4 Evaluation`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。 代价、failure mode 与旧方案共存边界由以下证据限制：限制或反证定位在 `arXiv:2602.07379v1 HTML — §5 Discussion`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：无工具、无持久状态的只读场景仍可采用较薄边界。
<!-- analysis:DA-20260211-3:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-07721:start -->
`ParisKV: Fast and Drift-Robust KV-Cache Retrieval for Long-Context LLMs` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-07721:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-07878:start -->
`Rethinking Latency Denial-of-Service: Attacking the LLM Serving Framework, Not the Model` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-07878:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-08007:start -->
`From $O(mn)$ to $O(r^2)$: Two-Sided Low-Rank Communication for Adam in Distributed Training with Memory Efficiency` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-08007:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-08847:start -->
`Dr. MAS: Stable Reinforcement Learning for Multi-Agent LLM Systems` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-08847:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-07120:start -->
`Anchored Decoding: Provably Reducing Copyright Risk for Any Language Model` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-07120:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-07223:start -->
`Vegas: Self-Speculative Decoding with Verification-Guided Sparse Attention` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-07223:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-07263:start -->
`tLoRA: Efficient Multi-LoRA Training with Elastic Shared Super-Models` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-07263:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-07265:start -->
`XShare: Collaborative in-Batch Expert Sharing for Faster MoE Inference` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-07265:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-07397:start -->
`Scout Before You Attend: Sketch-and-Walk Sparse Attention for Efficient LLM Inference` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-07397:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-07398:start -->
`AgentSys: Secure and Dynamic LLM Agents Through Explicit Hierarchical Memory Management` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-07398:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-07595:start -->
`TeleBoost: A Systematic Alignment Framework for High-Fidelity, Controllable, and Robust Video Generation` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-07595:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-07616:start -->
`SERE: Similarity-based Expert Re-routing for Efficient Batch Decoding in MoE Models` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-07616:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-07840:start -->
`SAGE: Scalable AI Governance &amp; Evaluation` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-07840:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-07962:start -->
`LOCA-bench: Benchmarking Language Agents Under Controllable and Extreme Context Growth` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-07962:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-07996:start -->
`The Judge Who Never Admits: Hidden Shortcuts in LLM-based Evaluation` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-07996:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-08005:start -->
`DeltaKV: Residual-Based KV Cache Compression via Long-Range Similarity` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-08005:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-08060:start -->
`Compiler-Assisted Speculative Sampling for Accelerated LLM Inference on Heterogeneous Edge Devices` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-08060:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-08237:start -->
`Document Reconstruction Unlocks Scalable Long-Context RLVR` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-08237:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-08296:start -->
`MonkeyTree: Near-Minimal Congestion for Multi-tenant Training via Migration` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-08296:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-08343:start -->
`ManifoldKV: Training-Free KV Cache Compression via Euclidean Outlier Detection` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-08343:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-08382:start -->
`Dynamic Long Context Reasoning over Compressed Memory via End-to-End Reinforcement Learning` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-08382:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-08401:start -->
`On Protecting Agentic Systems' Intellectual Property via Watermarking` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-08401:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-08404:start -->
`TEAM: Temporal-Spatial Consistency Guided Expert Activation for MoE Diffusion Language Model Acceleration` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-08404:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-08412:start -->
`From Assistant to Double Agent: Formalizing and Benchmarking Attacks on OpenClaw for Personalized Local AI Agent` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-08412:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-08563:start -->
`Stateless Yet Not Forgetful: Implicit Memory as a Hidden Channel in LLMs` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-08563:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-08585:start -->
`Predicting Future Utility: Global Combinatorial Optimization for Task-Agnostic KV Cache Eviction` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-08585:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-08621:start -->
`Sparse Models, Sparse Safety: Unsafe Routes in Mixture-of-Experts LLMs` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-08621:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-08722:start -->
`QUOKA: Query-Oriented KV Selection For Efficient LLM Prefill` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-08722:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-08747:start -->
`PARD: Enhancing Goodput for Inference Pipeline via Proactive Request Dropping` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-08747:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-08798:start -->
`CryptoGen: Secure Transformer Generation with Encrypted KV-Cache Reuse` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-08798:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-08905:start -->
`Efficient and Stable Reinforcement Learning for Diffusion Language Models` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-08905:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-08968:start -->
`stable-worldmodel-v1: Reproducible World Modeling Research and Evaluation` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-08968:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2602-07186 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#preference-data-的难点不只是数量 (line 143) | books/part-04-training-system/30-lora.md#本章要回答的问题 (line 10); books/part-04-training-system/32-ppo.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-07186 | delta:SF-2026-ARXIV-2602-07186 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-07186 |
| SF-2026-ARXIV-2602-07306 | MODEL-TRANSFORMER-LAYER | books/part-02-model/17-transformer-layer.md#layer-堆叠后发生什么 (line 430) | books/part-02-model/16-feed-forward-mlp.md#本章要回答的问题 (line 10); books/part-02-model/18-decoder-only.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-07306 | delta:SF-2026-ARXIV-2602-07306 | Principle Reuse | Integrate | books-review:SF-2026-ARXIV-2602-07306 |
| SF-2026-ARXIV-2602-07379 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#隐私检测是-policy-bound-sensor不是安全判决 (line 149) | books/part-06-ai-infrastructure/71-multi-tenant.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/73-production-best-practice.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-07379 | delta:SF-2026-ARXIV-2602-07379 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-07379 |
| SF-2026-ARXIV-2602-07721 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#一致性不变量 (line 717) | books/part-05-inference-system/44-decode.md#本章要回答的问题 (line 10); books/part-05-inference-system/46-continuous-batching.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-07721 | delta:SF-2026-ARXIV-2602-07721 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-07721 |
| SF-2026-ARXIV-2602-07878 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#availability-与-abuse (line 1025) | books/part-06-ai-infrastructure/71-multi-tenant.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/73-production-best-practice.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-07878 | delta:SF-2026-ARXIV-2602-07878 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-07878 |
| SF-2026-ARXIV-2602-08007 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#每种并行直接切什么 (line 563) | books/part-04-training-system/35-checkpoint.md#本章要回答的问题 (line 10); books/part-04-training-system/37-tensor-parallel.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-08007 | delta:SF-2026-ARXIV-2602-08007 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-08007 |
| SF-2026-ARXIV-2602-08847 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#verification-与-aggregation (line 521) | books/part-07-agent/81-workflow.md#本章要回答的问题 (line 10); books/part-07-agent/83-mcp.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-08847 | delta:SF-2026-ARXIV-2602-08847 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-08847 |
| SF-2026-ARXIV-2602-07120 | MODEL-SAMPLING | books/part-02-model/20-sampling.md#自检问题 (line 411) | books/part-02-model/19-kv-cache.md#本章要回答的问题 (line 10); books/part-02-model/21-moe.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-07120 | delta:SF-2026-ARXIV-2602-07120 | Principle Reuse | Integrate | books-review:SF-2026-ARXIV-2602-07120 |
| SF-2026-ARXIV-2602-07223 | INFER-SPECULATIVE-DECODING | books/part-05-inference-system/48-speculative-decoding.md#verify-length-不是孤立的固定超参数 (line 272) | books/part-05-inference-system/47-pagedattention.md#本章要回答的问题 (line 10); books/part-05-inference-system/49-tensorrt-llm.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-07223 | delta:SF-2026-ARXIV-2602-07223 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-07223 |
| SF-2026-ARXIV-2602-07263 | TRAIN-LORA | books/part-04-training-system/30-lora.md#merge-与动态-adapter-是两种资产策略 (line 297) | books/part-04-training-system/29-sft.md#本章要回答的问题 (line 10); books/part-04-training-system/31-rlhf.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-07263 | delta:SF-2026-ARXIV-2602-07263 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-07263 |
| SF-2026-ARXIV-2602-07265 | MODEL-MOE | books/part-02-model/21-moe.md#推理时为什么仍然不免费 (line 376) | books/part-02-model/20-sampling.md#本章要回答的问题 (line 10); books/part-02-model/22-long-context.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-07265 | delta:SF-2026-ARXIV-2602-07265 | Principle Reuse | Integrate | books-review:SF-2026-ARXIV-2602-07265 |
| SF-2026-ARXIV-2602-07397 | MODEL-LONG-CONTEXT | books/part-02-model/22-long-context.md#路线二改变-attention-连接 (line 121) | books/part-02-model/21-moe.md#本章要回答的问题 (line 10); books/part-03-multimodal-world-models/23-multimodal-representation.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-07397 | delta:SF-2026-ARXIV-2602-07397 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-07397 |
| SF-2026-ARXIV-2602-07398 | AGENT-MEMORY | books/part-07-agent/77-memory.md#派生-memory-的组织适用性与验证 (line 793) | books/part-07-agent/76-rag.md#本章要回答的问题 (line 10); books/part-07-agent/78-tool-calling.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-07398 | delta:SF-2026-ARXIV-2602-07398 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-07398 |
| SF-2026-ARXIV-2602-07595 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#rlhfrlaif-与-verifiable-reward (line 481) | books/part-04-training-system/30-lora.md#本章要回答的问题 (line 10); books/part-04-training-system/32-ppo.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-07595 | delta:SF-2026-ARXIV-2602-07595 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-07595 |
| SF-2026-ARXIV-2602-07616 | MODEL-MOE | books/part-02-model/21-moe.md#从参数化-router-到带检索记忆的-router (line 473) | books/part-02-model/20-sampling.md#本章要回答的问题 (line 10); books/part-02-model/22-long-context.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-07616 | delta:SF-2026-ARXIV-2602-07616 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-07616 |
| SF-2026-ARXIV-2602-07840 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#scorer-不是绝对真相 (line 1540) | books/part-06-ai-infrastructure/65-kai-scheduler.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/67-monitoring.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-07840 | delta:SF-2026-ARXIV-2602-07840 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-07840 |
| SF-2026-ARXIV-2602-07962 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#第一个不变量评估声明必须绑定完整对象 (line 179) | books/part-06-ai-infrastructure/65-kai-scheduler.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/67-monitoring.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-07962 | delta:SF-2026-ARXIV-2602-07962 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-07962 |
| SF-2026-ARXIV-2602-07996 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#评估对象有四个层次 (line 437) | books/part-06-ai-infrastructure/65-kai-scheduler.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/67-monitoring.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-07996 | delta:SF-2026-ARXIV-2602-07996 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-07996 |
| SF-2026-ARXIV-2602-08005 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#kv-cache-的生命周期 (line 427) | books/part-05-inference-system/44-decode.md#本章要回答的问题 (line 10); books/part-05-inference-system/46-continuous-batching.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-08005 | delta:SF-2026-ARXIV-2602-08005 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-08005 |
| SF-2026-ARXIV-2602-08060 | INFER-SPECULATIVE-DECODING | books/part-05-inference-system/48-speculative-decoding.md#drafter-的演进从辅助模型到受治理的-serving-artifact (line 520) | books/part-05-inference-system/47-pagedattention.md#本章要回答的问题 (line 10); books/part-05-inference-system/49-tensorrt-llm.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-08060 | delta:SF-2026-ARXIV-2602-08060 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-08060 |
| SF-2026-ARXIV-2602-08237 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#ppogrpodpo-分别接住什么 (line 537) | books/part-04-training-system/30-lora.md#本章要回答的问题 (line 10); books/part-04-training-system/32-ppo.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-08237 | delta:SF-2026-ARXIV-2602-08237 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-08237 |
| SF-2026-ARXIV-2602-08296 | PLATFORM-GPU-SCHEDULER | books/part-06-ai-infrastructure/63-gpu-scheduler.md#从固定-job-shape-到-elastic-configuration-portfolio (line 160) | books/part-06-ai-infrastructure/62-gateway.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/64-volcano.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-08296 | delta:SF-2026-ARXIV-2602-08296 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-08296 |
| SF-2026-ARXIV-2602-08343 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#kv-cache-的生命周期 (line 543) | books/part-05-inference-system/44-decode.md#本章要回答的问题 (line 10); books/part-05-inference-system/46-continuous-batching.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-08343 | delta:SF-2026-ARXIV-2602-08343 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-08343 |
| SF-2026-ARXIV-2602-08382 | MODEL-LONG-CONTEXT | books/part-02-model/22-long-context.md#路线六让模型在-test-time-更新内部记忆 (line 386) | books/part-02-model/21-moe.md#本章要回答的问题 (line 10); books/part-03-multimodal-world-models/23-multimodal-representation.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-08382 | delta:SF-2026-ARXIV-2602-08382 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-08382 |
| SF-2026-ARXIV-2602-08401 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#从-trace-检查到受限状态空间验证 (line 564) | books/part-06-ai-infrastructure/71-multi-tenant.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/73-production-best-practice.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-08401 | delta:SF-2026-ARXIV-2602-08401 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-08401 |
| SF-2026-ARXIV-2602-08404 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#build-time-与-runtime-time (line 969) | books/part-05-inference-system/48-speculative-decoding.md#本章要回答的问题 (line 10); books/part-05-inference-system/50-vllm.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-08404 | delta:SF-2026-ARXIV-2602-08404 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-08404 |
| SF-2026-ARXIV-2602-08412 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#从资产与信任边界开始 (line 20) | books/part-06-ai-infrastructure/71-multi-tenant.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/73-production-best-practice.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-08412 | delta:SF-2026-ARXIV-2602-08412 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-08412 |
| SF-2026-ARXIV-2602-08563 | AGENT-MEMORY | books/part-07-agent/77-memory.md#graph-memory-的-relation-也需要-provenance (line 1243) | books/part-07-agent/76-rag.md#本章要回答的问题 (line 10); books/part-07-agent/78-tool-calling.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-08563 | delta:SF-2026-ARXIV-2602-08563 | Principle Reuse | Integrate | books-review:SF-2026-ARXIV-2602-08563 |
| SF-2026-ARXIV-2602-08585 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#kv-cache-的生命周期 (line 543) | books/part-05-inference-system/44-decode.md#本章要回答的问题 (line 10); books/part-05-inference-system/46-continuous-batching.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-08585 | delta:SF-2026-ARXIV-2602-08585 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-08585 |
| SF-2026-ARXIV-2602-08621 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#从-trace-检查到受限状态空间验证 (line 573) | books/part-06-ai-infrastructure/71-multi-tenant.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/73-production-best-practice.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-08621 | delta:SF-2026-ARXIV-2602-08621 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-08621 |
| SF-2026-ARXIV-2602-08722 | INFER-PREFILL | books/part-05-inference-system/43-prefill.md#计算量从哪里来 (line 78) | books/part-05-inference-system/42-what-happens-during-inference.md#本章要回答的问题 (line 10); books/part-05-inference-system/44-decode.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-08722 | delta:SF-2026-ARXIV-2602-08722 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-08722 |
| SF-2026-ARXIV-2602-08747 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#slo-aware-admission (line 59) | books/part-05-inference-system/55-pd-disaggregation.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/57-what-is-ai-platform.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-08747 | delta:SF-2026-ARXIV-2602-08747 | Principle Reuse | Integrate | books-review:SF-2026-ARXIV-2602-08747 |
| SF-2026-ARXIV-2602-08798 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#风险管理而不是一次性认证 (line 1137) | books/part-06-ai-infrastructure/71-multi-tenant.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/73-production-best-practice.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-08798 | delta:SF-2026-ARXIV-2602-08798 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-08798 |
| SF-2026-ARXIV-2602-08905 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#rlhfrlaif-与-verifiable-reward (line 481) | books/part-04-training-system/30-lora.md#本章要回答的问题 (line 10); books/part-04-training-system/32-ppo.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-08905 | delta:SF-2026-ARXIV-2602-08905 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-08905 |
| SF-2026-ARXIV-2602-08968 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#工程实践从最小可信闭环开始 (line 2167) | books/part-06-ai-infrastructure/65-kai-scheduler.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/67-monitoring.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-08968 | delta:SF-2026-ARXIV-2602-08968 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-08968 |

<!-- existing:SF-2026-ARXIV-2602-07186:start -->
已对读当前 owner `TRAIN-RLHF` 在 `books/part-04-training-system/31-rlhf.md#preference-data-的难点不只是数量 (line 143)` 的命题：### Pluralistic Aggregation 不能把 Group State 压成一个平均 Reward
<!-- existing:SF-2026-ARXIV-2602-07186:end -->

<!-- delta:SF-2026-ARXIV-2602-07186:start -->
exact-v1 的 `arXiv:2602.07186v1 HTML — §4.2 Uncertainty-Driven Reward Design` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 rollout、reward、policy/reference 与更新 freshness。触发约束是：模型规模、奖励来源和任务 horizon 改变后，同一配方的排序可能反转。
<!-- delta:SF-2026-ARXIV-2602-07186:end -->

<!-- books-review:SF-2026-ARXIV-2602-07186:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-04-training-system/30-lora.md#本章要回答的问题 (line 10); books/part-04-training-system/32-ppo.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.07186v1 实际披露的机制与实验。方法定位为 arXiv:2602.07186v1 HTML — §4.2 Uncertainty-Driven Reward Design；验证定位为 arXiv:2602.07186v1 HTML — §3.2 Evaluation Results；边界定位为 arXiv:2602.07186v1 HTML — §5.3 Ablation Study (RQ2)。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-07186:end -->

<!-- existing:SF-2026-ARXIV-2602-07306:start -->
已对读当前 owner `MODEL-TRANSFORMER-LAYER` 在 `books/part-02-model/17-transformer-layer.md#layer-堆叠后发生什么 (line 430)` 的命题：## Layer 堆叠后发生什么
<!-- existing:SF-2026-ARXIV-2602-07306:end -->

<!-- delta:SF-2026-ARXIV-2602-07306:start -->
exact-v1 的 `arXiv:2602.07306v1 HTML — §2 The Parallel Track Transformer Architecture` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 layer topology、residual merge、activation flow 与 synchronization boundary。触发约束是：跨设备执行把 block 内同步次数、分支合并和 collective placement 变成一等约束。
<!-- delta:SF-2026-ARXIV-2602-07306:end -->

<!-- books-review:SF-2026-ARXIV-2602-07306:start -->
Decision=`Integrate`：现有命题原先未完整承载该 family 的长期机制责任；写回已在 canonical owner 中完成，并通过唯一 marker、正文位置和 claim-boundary 的 post-write fresh-context audit。 相邻章节已定位为 `books/part-02-model/16-feed-forward-mlp.md#本章要回答的问题 (line 10); books/part-02-model/18-decoder-only.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.07306v1 实际披露的机制与实验。方法定位为 arXiv:2602.07306v1 HTML — §2 The Parallel Track Transformer Architecture；验证定位为 arXiv:2602.07306v1 HTML — §3.3 Serving Evaluation；独立 limitations 未披露，因而采用更窄主张。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-07306:end -->

<!-- existing:SF-2026-ARXIV-2602-07379:start -->
已对读当前 owner `PLATFORM-SECURITY` 在 `books/part-06-ai-infrastructure/72-security.md#隐私检测是-policy-bound-sensor不是安全判决 (line 149)` 的命题：protected attribute + privacy unit → versioned agent pipeline → enumerated observable channels and observer permissions → channel-specific / combined attacker → leakage measurement with calibrated evaluator → mitigation and re-test under the same observation contract
<!-- existing:SF-2026-ARXIV-2602-07379:end -->

<!-- delta:SF-2026-ARXIV-2602-07379:start -->
exact-v1 的 `arXiv:2602.07379v1 HTML — §3.1 Framework` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 身份、授权、数据流、策略执行点与审计证据。触发约束是：工具、记忆和多 agent 委托把不可信内容转化为可执行控制流。
<!-- delta:SF-2026-ARXIV-2602-07379:end -->

<!-- books-review:SF-2026-ARXIV-2602-07379:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-06-ai-infrastructure/71-multi-tenant.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/73-production-best-practice.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.07379v1 实际披露的机制与实验。方法定位为 arXiv:2602.07379v1 HTML — §3.1 Framework；验证定位为 arXiv:2602.07379v1 HTML — §4 Evaluation；边界定位为 arXiv:2602.07379v1 HTML — §5 Discussion。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-07379:end -->

<!-- existing:SF-2026-ARXIV-2602-07721:start -->
已对读当前 owner `INFER-KV-CACHE` 在 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#一致性不变量 (line 717)` 的命题：### 从反应式 Recall 到预测式 Prefetch
<!-- existing:SF-2026-ARXIV-2602-07721:end -->

<!-- delta:SF-2026-ARXIV-2602-07721:start -->
exact-v1 的 `arXiv:2602.07721v1 HTML — §4 The ParisKV Framework` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 KV 的 identity、压缩、复用、放置与失效状态。触发约束是：长上下文、多会话和异构层级使 KV 容量、带宽及身份成为主瓶颈。
<!-- delta:SF-2026-ARXIV-2602-07721:end -->

<!-- books-review:SF-2026-ARXIV-2602-07721:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-05-inference-system/44-decode.md#本章要回答的问题 (line 10); books/part-05-inference-system/46-continuous-batching.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.07721v1 实际披露的机制与实验。方法定位为 arXiv:2602.07721v1 HTML — §4 The ParisKV Framework；验证定位为 arXiv:2602.07721v1 HTML — §5.2 Efficiency evaluation；边界定位为 arXiv:2602.07721v1 HTML — §5.3 Ablation Studies。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-07721:end -->

<!-- existing:SF-2026-ARXIV-2602-07878:start -->
已对读当前 owner `PLATFORM-SECURITY` 在 `books/part-06-ai-infrastructure/72-security.md#availability-与-abuse (line 1025)` 的命题：### Exactness 保持不变时，加速路径仍可能被定向击穿
<!-- existing:SF-2026-ARXIV-2602-07878:end -->

<!-- delta:SF-2026-ARXIV-2602-07878:start -->
exact-v1 的 `arXiv:2602.07878v1 HTML — §C.2 Comparison of Time-Series Modeling Methods` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 身份、授权、数据流、策略执行点与审计证据。触发约束是：工具、记忆和多 agent 委托把不可信内容转化为可执行控制流。
<!-- delta:SF-2026-ARXIV-2602-07878:end -->

<!-- books-review:SF-2026-ARXIV-2602-07878:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-06-ai-infrastructure/71-multi-tenant.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/73-production-best-practice.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.07878v1 实际披露的机制与实验。方法定位为 arXiv:2602.07878v1 HTML — §C.2 Comparison of Time-Series Modeling Methods；验证定位为 arXiv:2602.07878v1 HTML — §6.2 Main Results；边界定位为 arXiv:2602.07878v1 HTML — §B.2 More Discussions on Model-Specific Characteristics。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-07878:end -->

<!-- existing:SF-2026-ARXIV-2602-08007:start -->
已对读当前 owner `TRAIN-DISTRIBUTED-TRAINING` 在 `books/part-04-training-system/36-distributed-training.md#每种并行直接切什么 (line 563)` 的命题：### 从 Dense Collective 到 Optimizer-aware Sparse Support
<!-- existing:SF-2026-ARXIV-2602-08007:end -->

<!-- delta:SF-2026-ARXIV-2602-08007:start -->
exact-v1 的 `arXiv:2602.08007v1 HTML — §3.3 TSR-Adam: Two-Sided Low-Rank Core Synchronization` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 训练状态分片、collective、同步与故障恢复。触发约束是：参数、optimizer state 和通信规模越过单设备边界。
<!-- delta:SF-2026-ARXIV-2602-08007:end -->

<!-- books-review:SF-2026-ARXIV-2602-08007:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-04-training-system/35-checkpoint.md#本章要回答的问题 (line 10); books/part-04-training-system/37-tensor-parallel.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.08007v1 实际披露的机制与实验。方法定位为 arXiv:2602.08007v1 HTML — §3.3 TSR-Adam: Two-Sided Low-Rank Core Synchronization；验证定位为 arXiv:2602.08007v1 HTML — §4.2 Main Results: Pretraining Communication Efficiency；边界定位为 arXiv:2602.08007v1 HTML — §4.3 Ablations: Two-Sidedness, Randomized SVD, and Subspace Refresh Interval。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-08007:end -->

<!-- existing:SF-2026-ARXIV-2602-08847:start -->
已对读当前 owner `AGENT-MULTI-AGENT` 在 `books/part-07-agent/82-multi-agent.md#verification-与-aggregation (line 521)` 的命题：### Verification Delay 也是拓扑控制状态
<!-- existing:SF-2026-ARXIV-2602-08847:end -->

<!-- delta:SF-2026-ARXIV-2602-08847:start -->
exact-v1 的 `arXiv:2602.08847v1 HTML — §4 Methodology` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 拓扑、消息、共享状态、路由与停止条件。触发约束是：任务分解、异构能力与并行协作引入通信、共享状态和信用分配问题。
<!-- delta:SF-2026-ARXIV-2602-08847:end -->

<!-- books-review:SF-2026-ARXIV-2602-08847:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-07-agent/81-workflow.md#本章要回答的问题 (line 10); books/part-07-agent/83-mcp.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.08847v1 实际披露的机制与实验。方法定位为 arXiv:2602.08847v1 HTML — §4 Methodology；验证定位为 arXiv:2602.08847v1 HTML — §5.4 Ablation Study；边界定位为 arXiv:2602.08847v1 HTML — §6 Conclusions and Limitations。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-08847:end -->

<!-- existing:SF-2026-ARXIV-2602-07120:start -->
已对读当前 owner `MODEL-SAMPLING` 在 `books/part-02-model/20-sampling.md#自检问题 (line 411)` 的命题：### Anchored Decoding 把版权风险编译为序列信息预算
<!-- existing:SF-2026-ARXIV-2602-07120:end -->

<!-- delta:SF-2026-ARXIV-2602-07120:start -->
exact-v1 的 `arXiv:2602.07120v1 HTML — §3.5 Putting Anchored Decoding together` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 logit transformation、proposal distribution、verification 与 token commit。触发约束是：安全、质量或计算预算需要在 token commit 前动态改变候选分布。
<!-- delta:SF-2026-ARXIV-2602-07120:end -->

<!-- books-review:SF-2026-ARXIV-2602-07120:start -->
Decision=`Integrate`：现有命题原先未完整承载该 family 的长期机制责任；写回已在 canonical owner 中完成，并通过唯一 marker、正文位置和 claim-boundary 的 post-write fresh-context audit。 相邻章节已定位为 `books/part-02-model/19-kv-cache.md#本章要回答的问题 (line 10); books/part-02-model/21-moe.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.07120v1 实际披露的机制与实验。方法定位为 arXiv:2602.07120v1 HTML — §3.5 Putting Anchored Decoding together；验证定位为 arXiv:2602.07120v1 HTML — §5.1 Risk–utility trade-offs；边界定位为 arXiv:2602.07120v1 HTML — §A.3 Limitations and Future Work。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-07120:end -->

<!-- existing:SF-2026-ARXIV-2602-07223:start -->
已对读当前 owner `INFER-SPECULATIVE-DECODING` 在 `books/part-05-inference-system/48-speculative-decoding.md#verify-length-不是孤立的固定超参数 (line 272)` 的命题：### Verification 可以稀疏化，但 Exactness 不能稀疏化
<!-- existing:SF-2026-ARXIV-2602-07223:end -->

<!-- delta:SF-2026-ARXIV-2602-07223:start -->
exact-v1 的 `arXiv:2602.07223v1 HTML — §4 Implementation` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 proposal、验证、接受/回滚与缓存提交状态。触发约束是：decode 的串行依赖限制利用率，促使系统用廉价 proposal 换取并行验证。
<!-- delta:SF-2026-ARXIV-2602-07223:end -->

<!-- books-review:SF-2026-ARXIV-2602-07223:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-05-inference-system/47-pagedattention.md#本章要回答的问题 (line 10); books/part-05-inference-system/49-tensorrt-llm.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.07223v1 实际披露的机制与实验。方法定位为 arXiv:2602.07223v1 HTML — §4 Implementation；验证定位为 arXiv:2602.07223v1 HTML — §5.2 Reasoning Workloads with Short Input Context；独立 limitations 未披露，因而采用更窄主张。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-07223:end -->

<!-- existing:SF-2026-ARXIV-2602-07263:start -->
已对读当前 owner `TRAIN-LORA` 在 `books/part-04-training-system/30-lora.md#merge-与动态-adapter-是两种资产策略 (line 297)` 的命题：### 多租户 Fine-tuning：从共享权重转向复用 Backbone 执行
<!-- existing:SF-2026-ARXIV-2602-07263:end -->

<!-- delta:SF-2026-ARXIV-2602-07263:start -->
exact-v1 的 `arXiv:2602.07263v1 HTML — §3 tLoRA Design` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 base weight identity、adapter state、merge 与 serving compatibility。触发约束是：参数、显存与多租户 adapter 数量增长后需要隔离可训练增量。
<!-- delta:SF-2026-ARXIV-2602-07263:end -->

<!-- books-review:SF-2026-ARXIV-2602-07263:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-04-training-system/29-sft.md#本章要回答的问题 (line 10); books/part-04-training-system/31-rlhf.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.07263v1 实际披露的机制与实验。方法定位为 arXiv:2602.07263v1 HTML — §3 tLoRA Design；验证定位为 arXiv:2602.07263v1 HTML — §4 Evaluation；边界定位为 arXiv:2602.07263v1 HTML — §A.2 Job completion time ablation studies。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-07263:end -->

<!-- existing:SF-2026-ARXIV-2602-07265:start -->
已对读当前 owner `MODEL-MOE` 在 `books/part-02-model/21-moe.md#推理时为什么仍然不免费 (line 376)` 的命题：## 推理时为什么仍然不免费
<!-- existing:SF-2026-ARXIV-2602-07265:end -->

<!-- delta:SF-2026-ARXIV-2602-07265:start -->
exact-v1 的 `arXiv:2602.07265v1 HTML — §3.4 Practical Algorithm` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 expert 选择、capacity、placement 与通信。触发约束是：容量扩大后，激活成本和通信使全参数计算不可持续。
<!-- delta:SF-2026-ARXIV-2602-07265:end -->

<!-- books-review:SF-2026-ARXIV-2602-07265:start -->
Decision=`Integrate`：现有命题原先未完整承载该 family 的长期机制责任；写回已在 canonical owner 中完成，并通过唯一 marker、正文位置和 claim-boundary 的 post-write fresh-context audit。 相邻章节已定位为 `books/part-02-model/20-sampling.md#本章要回答的问题 (line 10); books/part-02-model/22-long-context.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.07265v1 实际披露的机制与实验。方法定位为 arXiv:2602.07265v1 HTML — §3.4 Practical Algorithm；验证定位为 arXiv:2602.07265v1 HTML — §6 Experiments；独立 limitations 未披露，因而采用更窄主张。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-07265:end -->

<!-- existing:SF-2026-ARXIV-2602-07397:start -->
已对读当前 owner `MODEL-LONG-CONTEXT` 在 `books/part-02-model/22-long-context.md#路线二改变-attention-连接 (line 121)` 的命题：### Conditional Attention 的路由粒度必须匹配执行粒度
<!-- existing:SF-2026-ARXIV-2602-07397:end -->

<!-- delta:SF-2026-ARXIV-2602-07397:start -->
exact-v1 的 `arXiv:2602.07397v1 HTML — §2 Sketch and Walk` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 上下文选择、层次化表示和可访问记忆的语义边界。触发约束是：序列增长令计算、显存和信息稀释同时恶化。
<!-- delta:SF-2026-ARXIV-2602-07397:end -->

<!-- books-review:SF-2026-ARXIV-2602-07397:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-02-model/21-moe.md#本章要回答的问题 (line 10); books/part-03-multimodal-world-models/23-multimodal-representation.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.07397v1 实际披露的机制与实验。方法定位为 arXiv:2602.07397v1 HTML — §2 Sketch and Walk；验证定位为 arXiv:2602.07397v1 HTML — §4.3 Efficiency Evaluation；边界定位为 arXiv:2602.07397v1 HTML — §4.4 Ablation Studies。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-07397:end -->

<!-- existing:SF-2026-ARXIV-2602-07398:start -->
已对读当前 owner `AGENT-MEMORY` 在 `books/part-07-agent/77-memory.md#派生-memory-的组织适用性与验证 (line 793)` 的命题：### Memory Visibility 是固定协议，不是模型的临时选择
<!-- existing:SF-2026-ARXIV-2602-07398:end -->

<!-- delta:SF-2026-ARXIV-2602-07398:start -->
exact-v1 的 `arXiv:2602.07398v1 HTML — §5.1 System Overview` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 memory 的写入、版本、检索与失效控制权。触发约束是：长时交互、容量和权限约束迫使系统决定何时写、如何索引、何时遗忘。
<!-- delta:SF-2026-ARXIV-2602-07398:end -->

<!-- books-review:SF-2026-ARXIV-2602-07398:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-07-agent/76-rag.md#本章要回答的问题 (line 10); books/part-07-agent/78-tool-calling.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.07398v1 实际披露的机制与实验。方法定位为 arXiv:2602.07398v1 HTML — §5.1 System Overview；验证定位为 arXiv:2602.07398v1 HTML — §6.1 Evaluation on Benchmarks；边界定位为 arXiv:2602.07398v1 HTML — §7 Discussion。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-07398:end -->

<!-- existing:SF-2026-ARXIV-2602-07595:start -->
已对读当前 owner `TRAIN-RLHF` 在 `books/part-04-training-system/31-rlhf.md#rlhfrlaif-与-verifiable-reward (line 481)` 的命题：### 后训练分支的本质差异是 State Distribution
<!-- existing:SF-2026-ARXIV-2602-07595:end -->

<!-- delta:SF-2026-ARXIV-2602-07595:start -->
exact-v1 的 `arXiv:2602.07595v1 HTML — §6.1 A Ray-based Resource-Efficient Parallel Framework for GRPO` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 rollout、reward、policy/reference 与更新 freshness。触发约束是：模型规模、奖励来源和任务 horizon 改变后，同一配方的排序可能反转。
<!-- delta:SF-2026-ARXIV-2602-07595:end -->

<!-- books-review:SF-2026-ARXIV-2602-07595:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-04-training-system/30-lora.md#本章要回答的问题 (line 10); books/part-04-training-system/32-ppo.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.07595v1 实际披露的机制与实验。方法定位为 arXiv:2602.07595v1 HTML — §6.1 A Ray-based Resource-Efficient Parallel Framework for GRPO；验证定位为 arXiv:2602.07595v1 HTML — §7.3 Objective Evaluation: Benchmarks and Ablations；边界定位为 arXiv:2602.07595v1 HTML — §8 Conclusion。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-07595:end -->

<!-- existing:SF-2026-ARXIV-2602-07616:start -->
已对读当前 owner `MODEL-MOE` 在 `books/part-02-model/21-moe.md#从参数化-router-到带检索记忆的-router (line 473)` 的命题：### Post-training 后再增加可跳过路径，不等于删除旧 Experts
<!-- existing:SF-2026-ARXIV-2602-07616:end -->

<!-- delta:SF-2026-ARXIV-2602-07616:start -->
exact-v1 的 `arXiv:2602.07616v1 PDF — §method for Efficient batch decoding in MoE models. SERE dynamically reduces` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 expert 选择、capacity、placement 与通信。触发约束是：容量扩大后，激活成本和通信使全参数计算不可持续。
<!-- delta:SF-2026-ARXIV-2602-07616:end -->

<!-- books-review:SF-2026-ARXIV-2602-07616:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-02-model/20-sampling.md#本章要回答的问题 (line 10); books/part-02-model/22-long-context.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.07616v1 实际披露的机制与实验。方法定位为 arXiv:2602.07616v1 PDF — §method for Efficient batch decoding in MoE models. SERE dynamically reduces；验证定位为 arXiv:2602.07616v1 PDF — §experiments are conducted on NVIDIA H20 GPUs.；独立 limitations 未披露，因而采用更窄主张。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-07616:end -->

<!-- existing:SF-2026-ARXIV-2602-07840:start -->
已对读当前 owner `PLATFORM-EVALUATION-SYSTEM` 在 `books/part-06-ai-infrastructure/66-evaluation-system.md#scorer-不是绝对真相 (line 1540)` 的命题：因此 reward judge 的验收应加入 policy-shifted red team、独立 holdout oracle、跨 judge transfer、artifact sampling 与停止条件， 并同时观察 training-judge reward 和外部 evidence。Examining Reasoning LLMs-as-Judges 的合成 preference 实验说明 reasoning judge 仍可被策略利用，且 reasoning compute 不能替代 distillation；它不证明所有 reasoning judge 更差，也不证明某公开排行榜失效。 规则、程序或 executable verifier 在可形式化域继续优先；开放域的 model judge 必须保留 disagreement、abstain 和人工升级，而 不能同时独占训练 reward 与 release authority。
<!-- existing:SF-2026-ARXIV-2602-07840:end -->

<!-- delta:SF-2026-ARXIV-2602-07840:start -->
exact-v1 的 `arXiv:2602.07840v1 HTML — §3. Problem Formulation and Framework` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 evaluation contract、覆盖分母、evidence lineage 与 release gate。触发约束是：agent、长时程和多模态系统把失败分散到状态、工具与环境交互链。
<!-- delta:SF-2026-ARXIV-2602-07840:end -->

<!-- books-review:SF-2026-ARXIV-2602-07840:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-06-ai-infrastructure/65-kai-scheduler.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/67-monitoring.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.07840v1 实际披露的机制与实验。方法定位为 arXiv:2602.07840v1 HTML — §3. Problem Formulation and Framework；验证定位为 arXiv:2602.07840v1 HTML — §5.3. Experiments: Optimizing the Student Model；独立 limitations 未披露，因而采用更窄主张。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-07840:end -->

<!-- existing:SF-2026-ARXIV-2602-07962:start -->
已对读当前 owner `PLATFORM-EVALUATION-SYSTEM` 在 `books/part-06-ai-infrastructure/66-evaluation-system.md#第一个不变量评估声明必须绑定完整对象 (line 179)` 的命题：### Evaluation Identity 必须包含 Harness 与 Environment
<!-- existing:SF-2026-ARXIV-2602-07962:end -->

<!-- delta:SF-2026-ARXIV-2602-07962:start -->
exact-v1 的 `arXiv:2602.07962v1 HTML — §2.3 Implementation` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 evaluation contract、覆盖分母、evidence lineage 与 release gate。触发约束是：agent、长时程和多模态系统把失败分散到状态、工具与环境交互链。
<!-- delta:SF-2026-ARXIV-2602-07962:end -->

<!-- books-review:SF-2026-ARXIV-2602-07962:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-06-ai-infrastructure/65-kai-scheduler.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/67-monitoring.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.07962v1 实际披露的机制与实验。方法定位为 arXiv:2602.07962v1 HTML — §2.3 Implementation；验证定位为 arXiv:2602.07962v1 HTML — §3.2 Main Results；边界定位为 arXiv:2602.07962v1 HTML — §3.3 Failure Mode Analysis。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-07962:end -->

<!-- existing:SF-2026-ARXIV-2602-07996:start -->
已对读当前 owner `PLATFORM-EVALUATION-SYSTEM` 在 `books/part-06-ai-infrastructure/66-evaluation-system.md#评估对象有四个层次 (line 437)` 的命题：Deep Research 进一步要求把 final report 拆成多个 evidence planes：report synthesis quality、claim-level factuality/provenance、trajectory/process quality 与 environment/tool contract。四者不能平均成一个分数后丢失： 写得完整可能掩盖 unsupported claim，过程看似规范也可能没有真正取得证据。MiroEval 只在其 snapshot、judge 与 tool budget 下支持这种分层；live-web drift、judge calibration 与 trace privacy 仍需要独立治理。
<!-- existing:SF-2026-ARXIV-2602-07996:end -->

<!-- delta:SF-2026-ARXIV-2602-07996:start -->
exact-v1 的 `arXiv:2602.07996v1 HTML — §3.2 Cue Families` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 evaluation contract、覆盖分母、evidence lineage 与 release gate。触发约束是：agent、长时程和多模态系统把失败分散到状态、工具与环境交互链。
<!-- delta:SF-2026-ARXIV-2602-07996:end -->

<!-- books-review:SF-2026-ARXIV-2602-07996:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-06-ai-infrastructure/65-kai-scheduler.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/67-monitoring.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.07996v1 实际披露的机制与实验。方法定位为 arXiv:2602.07996v1 HTML — §3.2 Cue Families；验证定位为 arXiv:2602.07996v1 HTML — §LLM judges exhibit a strong and largely unacknowledged recency bias.；边界定位为 arXiv:2602.07996v1 HTML — §6 Limitations。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-07996:end -->

<!-- existing:SF-2026-ARXIV-2602-08005:start -->
已对读当前 owner `INFER-KV-CACHE` 在 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#kv-cache-的生命周期 (line 427)` 的命题：### 从统一跨层共享到 Token × Depth 自适应残差
<!-- existing:SF-2026-ARXIV-2602-08005:end -->

<!-- delta:SF-2026-ARXIV-2602-08005:start -->
exact-v1 的 `arXiv:2602.08005v1 HTML — §4.3 Sparse-vLLM Implementation` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 KV 的 identity、压缩、复用、放置与失效状态。触发约束是：长上下文、多会话和异构层级使 KV 容量、带宽及身份成为主瓶颈。
<!-- delta:SF-2026-ARXIV-2602-08005:end -->

<!-- books-review:SF-2026-ARXIV-2602-08005:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-05-inference-system/44-decode.md#本章要回答的问题 (line 10); books/part-05-inference-system/46-continuous-batching.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.08005v1 实际披露的机制与实验。方法定位为 arXiv:2602.08005v1 HTML — §4.3 Sparse-vLLM Implementation；验证定位为 arXiv:2602.08005v1 HTML — §Evaluation；边界定位为 arXiv:2602.08005v1 HTML — §B.5 Detailed Latency Profiling and Future Optimization。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-08005:end -->

<!-- existing:SF-2026-ARXIV-2602-08060:start -->
已对读当前 owner `INFER-SPECULATIVE-DECODING` 在 `books/part-05-inference-system/48-speculative-decoding.md#drafter-的演进从辅助模型到受治理的-serving-artifact (line 520)` 的命题：### Edge / Cloud 分离：Draft 复用把 Verify Depth 变成网络控制问题
<!-- existing:SF-2026-ARXIV-2602-08060:end -->

<!-- delta:SF-2026-ARXIV-2602-08060:start -->
exact-v1 的 `arXiv:2602.08060v1 HTML — §III Heterogeneous Mapping Framework for Speculative Sampling` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 proposal、验证、接受/回滚与缓存提交状态。触发约束是：decode 的串行依赖限制利用率，促使系统用廉价 proposal 换取并行验证。
<!-- delta:SF-2026-ARXIV-2602-08060:end -->

<!-- books-review:SF-2026-ARXIV-2602-08060:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-05-inference-system/47-pagedattention.md#本章要回答的问题 (line 10); books/part-05-inference-system/49-tensorrt-llm.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.08060v1 实际披露的机制与实验。方法定位为 arXiv:2602.08060v1 HTML — §III Heterogeneous Mapping Framework for Speculative Sampling；验证定位为 arXiv:2602.08060v1 HTML — §IV Experimental Setup and Evaluation；边界定位为 arXiv:2602.08060v1 HTML — §IV-D Validation and Discussion。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-08060:end -->

<!-- existing:SF-2026-ARXIV-2602-08237:start -->
已对读当前 owner `TRAIN-RLHF` 在 `books/part-04-training-system/31-rlhf.md#ppogrpodpo-分别接住什么 (line 537)` 的命题：DPO 不训练显式 Reward Model，也不在 fine-tuning loop 内做 on-policy rollout，但仍依赖 preference data 和 reference policy。GRPO 可以使用 learned reward，也可以使用 verifiable reward；“移除 critic”不等于移除所有 reward design。
<!-- existing:SF-2026-ARXIV-2602-08237:end -->

<!-- delta:SF-2026-ARXIV-2602-08237:start -->
exact-v1 的 `arXiv:2602.08237v1 PDF — §Method` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 rollout、reward、policy/reference 与更新 freshness。触发约束是：模型规模、奖励来源和任务 horizon 改变后，同一配方的排序可能反转。
<!-- delta:SF-2026-ARXIV-2602-08237:end -->

<!-- books-review:SF-2026-ARXIV-2602-08237:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-04-training-system/30-lora.md#本章要回答的问题 (line 10); books/part-04-training-system/32-ppo.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.08237v1 实际披露的机制与实验。方法定位为 arXiv:2602.08237v1 PDF — §Method；验证定位为 arXiv:2602.08237v1 PDF — §Evaluation. Benchmarks. We evaluate all models on two challenging long-context QA；边界定位为 arXiv:2602.08237v1 PDF — §Limitations。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-08237:end -->

<!-- existing:SF-2026-ARXIV-2602-08296:start -->
已对读当前 owner `PLATFORM-GPU-SCHEDULER` 在 `books/part-06-ai-infrastructure/63-gpu-scheduler.md#从固定-job-shape-到-elastic-configuration-portfolio (line 160)` 的命题：## 从固定 Job Shape 到 Elastic Configuration Portfolio
<!-- existing:SF-2026-ARXIV-2602-08296:end -->

<!-- delta:SF-2026-ARXIV-2602-08296:start -->
exact-v1 的 `arXiv:2602.08296v1 HTML — §4. MonkeyTree System Design` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 GPU slice、隔离、配额与抢占控制。触发约束是：并发 workload 与成本压力要求共享，同时又不能破坏确定性。
<!-- delta:SF-2026-ARXIV-2602-08296:end -->

<!-- books-review:SF-2026-ARXIV-2602-08296:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-06-ai-infrastructure/62-gateway.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/64-volcano.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.08296v1 实际披露的机制与实验。方法定位为 arXiv:2602.08296v1 HTML — §4. MonkeyTree System Design；验证定位为 arXiv:2602.08296v1 HTML — §6. Evaluation；边界定位为 arXiv:2602.08296v1 HTML — §8. Discussion。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-08296:end -->

<!-- existing:SF-2026-ARXIV-2602-08343:start -->
已对读当前 owner `INFER-KV-CACHE` 在 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#kv-cache-的生命周期 (line 543)` 的命题：### 从昂贵 Oracle 到 Learned Eviction Policy
<!-- existing:SF-2026-ARXIV-2602-08343:end -->

<!-- delta:SF-2026-ARXIV-2602-08343:start -->
exact-v1 的 `arXiv:2602.08343v1 HTML — §E.1 Methodology` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 KV 的 identity、压缩、复用、放置与失效状态。触发约束是：长上下文、多会话和异构层级使 KV 容量、带宽及身份成为主瓶颈。
<!-- delta:SF-2026-ARXIV-2602-08343:end -->

<!-- books-review:SF-2026-ARXIV-2602-08343:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-05-inference-system/44-decode.md#本章要回答的问题 (line 10); books/part-05-inference-system/46-continuous-batching.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.08343v1 实际披露的机制与实验。方法定位为 arXiv:2602.08343v1 HTML — §E.1 Methodology；验证定位为 arXiv:2602.08343v1 HTML — §5.2 Main Results；边界定位为 arXiv:2602.08343v1 HTML — §6 Discussion。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-08343:end -->

<!-- existing:SF-2026-ARXIV-2602-08382:start -->
已对读当前 owner `MODEL-LONG-CONTEXT` 在 `books/part-02-model/22-long-context.md#路线六让模型在-test-time-更新内部记忆 (line 386)` 的命题：## 路线六：让模型在 Test Time 更新内部记忆
<!-- existing:SF-2026-ARXIV-2602-08382:end -->

<!-- delta:SF-2026-ARXIV-2602-08382:start -->
exact-v1 的 `arXiv:2602.08382v1 HTML — §Appendix A Implementation Details` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 上下文选择、层次化表示和可访问记忆的语义边界。触发约束是：序列增长令计算、显存和信息稀释同时恶化。
<!-- delta:SF-2026-ARXIV-2602-08382:end -->

<!-- books-review:SF-2026-ARXIV-2602-08382:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-02-model/21-moe.md#本章要回答的问题 (line 10); books/part-03-multimodal-world-models/23-multimodal-representation.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.08382v1 实际披露的机制与实验。方法定位为 arXiv:2602.08382v1 HTML — §Appendix A Implementation Details；验证定位为 arXiv:2602.08382v1 HTML — §4.2 Main Results；边界定位为 arXiv:2602.08382v1 HTML — §Appendix C Failure Mode Analysis。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-08382:end -->

<!-- existing:SF-2026-ARXIV-2602-08401:start -->
已对读当前 owner `PLATFORM-SECURITY` 在 `books/part-06-ai-infrastructure/72-security.md#从-trace-检查到受限状态空间验证 (line 564)` 的命题：形式证明的强度来自假设，而不是数学符号本身。Bounded active domain、identifier-renaming equivariance、有限 tool semantics 与可枚举 transition 一旦被 schema evolution、外部副作用、概率 policy 或无限对象打破，证明便不覆盖真实 系统。Formal Verification of Agentic Systems 提供这一受限分支的理论证据，不证明任意 LLM Agent 可验证；trace、 simulation、canary 与 incident evidence 因而继续存在。
<!-- existing:SF-2026-ARXIV-2602-08401:end -->

<!-- delta:SF-2026-ARXIV-2602-08401:start -->
exact-v1 的 `arXiv:2602.08401v1 HTML — §IV Methodology` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 身份、授权、数据流、策略执行点与审计证据。触发约束是：工具、记忆和多 agent 委托把不可信内容转化为可执行控制流。
<!-- delta:SF-2026-ARXIV-2602-08401:end -->

<!-- books-review:SF-2026-ARXIV-2602-08401:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-06-ai-infrastructure/71-multi-tenant.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/73-production-best-practice.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.08401v1 实际披露的机制与实验。方法定位为 arXiv:2602.08401v1 HTML — §IV Methodology；验证定位为 arXiv:2602.08401v1 HTML — §VII Evaluation；边界定位为 arXiv:2602.08401v1 HTML — §VIII Conclusion。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-08401:end -->

<!-- existing:SF-2026-ARXIV-2602-08404:start -->
已对读当前 owner `INFER-TENSORRT-LLM` 在 `books/part-05-inference-system/49-tensorrt-llm.md#build-time-与-runtime-time (line 969)` 的命题：### Diffusion Block 内的 Expert Stability 可以变成受限 I/O Hint
<!-- existing:SF-2026-ARXIV-2602-08404:end -->

<!-- delta:SF-2026-ARXIV-2602-08404:start -->
exact-v1 的 `arXiv:2602.08404v1 HTML — §3.2 Delayed Caching for Decoded Tokens (DCD)` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 graph lowering、kernel/precision 选择与执行计划版本。触发约束是：模型规模、算子形态和 SLO 使执行计划、精度与 kernel 选择成为主要成本。
<!-- delta:SF-2026-ARXIV-2602-08404:end -->

<!-- books-review:SF-2026-ARXIV-2602-08404:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-05-inference-system/48-speculative-decoding.md#本章要回答的问题 (line 10); books/part-05-inference-system/50-vllm.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.08404v1 实际披露的机制与实验。方法定位为 arXiv:2602.08404v1 HTML — §3.2 Delayed Caching for Decoded Tokens (DCD)；验证定位为 arXiv:2602.08404v1 HTML — §4.2 Main Results；边界定位为 arXiv:2602.08404v1 HTML — §4.3 Ablation Study and Analysis。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-08404:end -->

<!-- existing:SF-2026-ARXIV-2602-08412:start -->
已对读当前 owner `PLATFORM-SECURITY` 在 `books/part-06-ai-infrastructure/72-security.md#从资产与信任边界开始 (line 20)` 的命题：- source data、labels 与 user context； - code、images、dependencies 与 credentials； - checkpoints、adapters、tokenizers 与 prompts； - registry metadata、evaluation 与 approvals； - GPU nodes、runtime memory 与 KV Cache； - APIs、tools、business systems 与 audit evidence。
<!-- existing:SF-2026-ARXIV-2602-08412:end -->

<!-- delta:SF-2026-ARXIV-2602-08412:start -->
exact-v1 的 `arXiv:2602.08412v1 HTML — §2.4 Attack Primitives` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 身份、授权、数据流、策略执行点与审计证据。触发约束是：工具、记忆和多 agent 委托把不可信内容转化为可执行控制流。
<!-- delta:SF-2026-ARXIV-2602-08412:end -->

<!-- books-review:SF-2026-ARXIV-2602-08412:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-06-ai-infrastructure/71-multi-tenant.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/73-production-best-practice.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.08412v1 实际披露的机制与实验。方法定位为 arXiv:2602.08412v1 HTML — §2.4 Attack Primitives；验证定位为 arXiv:2602.08412v1 HTML — §3.2 Main Results and Analysis；边界定位为 arXiv:2602.08412v1 HTML — §4 Conclusion and Future Work。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-08412:end -->

<!-- existing:SF-2026-ARXIV-2602-08563:start -->
已对读当前 owner `AGENT-MEMORY` 在 `books/part-07-agent/77-memory.md#graph-memory-的-relation-也需要-provenance (line 1243)` 的命题：### Stateless API 仍可能承载跨调用的 Implicit Memory
<!-- existing:SF-2026-ARXIV-2602-08563:end -->

<!-- delta:SF-2026-ARXIV-2602-08563:start -->
exact-v1 的 `arXiv:2602.08563v1 HTML — §III Implicit Memory in LLMs: Definition, Threat Model, and Feasibility` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 memory 的写入、版本、检索与失效控制权。触发约束是：长时交互、容量和权限约束迫使系统决定何时写、如何索引、何时遗忘。
<!-- delta:SF-2026-ARXIV-2602-08563:end -->

<!-- books-review:SF-2026-ARXIV-2602-08563:start -->
Decision=`Integrate`：现有命题原先未完整承载该 family 的长期机制责任；写回已在 canonical owner 中完成，并通过唯一 marker、正文位置和 claim-boundary 的 post-write fresh-context audit。 相邻章节已定位为 `books/part-07-agent/76-rag.md#本章要回答的问题 (line 10); books/part-07-agent/78-tool-calling.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.08563v1 实际披露的机制与实验。方法定位为 arXiv:2602.08563v1 HTML — §III Implicit Memory in LLMs: Definition, Threat Model, and Feasibility；验证定位为 arXiv:2602.08563v1 HTML — §VII Time Bomb: A Temporal Backdoor via Implicit Memory；边界定位为 arXiv:2602.08563v1 HTML — §IX Future Directions。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-08563:end -->

<!-- existing:SF-2026-ARXIV-2602-08585:start -->
已对读当前 owner `INFER-KV-CACHE` 在 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#kv-cache-的生命周期 (line 543)` 的命题：### 从昂贵 Oracle 到 Learned Eviction Policy
<!-- existing:SF-2026-ARXIV-2602-08585:end -->

<!-- delta:SF-2026-ARXIV-2602-08585:start -->
exact-v1 的 `arXiv:2602.08585v1 HTML — §4.3 Practical Implementation: Offline Profiling` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 KV 的 identity、压缩、复用、放置与失效状态。触发约束是：长上下文、多会话和异构层级使 KV 容量、带宽及身份成为主瓶颈。
<!-- delta:SF-2026-ARXIV-2602-08585:end -->

<!-- books-review:SF-2026-ARXIV-2602-08585:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-05-inference-system/44-decode.md#本章要回答的问题 (line 10); books/part-05-inference-system/46-continuous-batching.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.08585v1 实际披露的机制与实验。方法定位为 arXiv:2602.08585v1 HTML — §4.3 Practical Implementation: Offline Profiling；验证定位为 arXiv:2602.08585v1 HTML — §5.4 Ablation Study；边界定位为 arXiv:2602.08585v1 HTML — §Limitation of Heuristic Metric.。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-08585:end -->

<!-- existing:SF-2026-ARXIV-2602-08621:start -->
已对读当前 owner `PLATFORM-SECURITY` 在 `books/part-06-ai-infrastructure/72-security.md#从-trace-检查到受限状态空间验证 (line 573)` 的命题：Contract evaluator 是 reference monitor 的一个受限实现，不是原始事实传感器。`tone_score`、PII flag 或 confidence 等字段仍由独立 extractor 产生，其版本、误差和缺失必须传播为 Unknown；概率阈值、reference distribution 与 recovery success 也会漂移。`arXiv:2602.22302v1` 的 exact-v1 只支持 §3 的 contract 语义、§4.3 composition、§5 的 reference architecture、作者 benchmark/实验与 §8.2 限制，不证明 live production Agent 已满足形式保证。feature 不可验证、contract 冲突、composition 假设失效或 action 不可逆时，应 fail closed、sandbox 或人工审批；静态 policy、trace audit 与有界 model checking 继续作为更强或更便宜的共存分支。
<!-- existing:SF-2026-ARXIV-2602-08621:end -->

<!-- delta:SF-2026-ARXIV-2602-08621:start -->
exact-v1 的 `arXiv:2602.08621v1 HTML — §Our Proposed F-SOUR` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 身份、授权、数据流、策略执行点与审计证据。触发约束是：工具、记忆和多 agent 委托把不可信内容转化为可执行控制流。
<!-- delta:SF-2026-ARXIV-2602-08621:end -->

<!-- books-review:SF-2026-ARXIV-2602-08621:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-06-ai-infrastructure/71-multi-tenant.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/73-production-best-practice.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.08621v1 实际披露的机制与实验。方法定位为 arXiv:2602.08621v1 HTML — §Our Proposed F-SOUR；验证定位为 arXiv:2602.08621v1 HTML — §Experimental Results；边界定位为 arXiv:2602.08621v1 HTML — §Appendix G Limitations and Future Work。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-08621:end -->

<!-- existing:SF-2026-ARXIV-2602-08722:start -->
已对读当前 owner `INFER-PREFILL` 在 `books/part-05-inference-system/43-prefill.md#计算量从哪里来 (line 78)` 的命题：跳层并未自动降低 peak KV capacity，也可能只减少部分 layer compute；动态 selection 则新增 scoring、compaction 与 irregular gather。完整 Prefill 在 prompt 短、实现简单性或 correctness-first 时继续成立。任何 sparse/skip plan 都必须分别报告 selection cost、KV materialization、TTFT、Decode quality 与 fallback，而不能只引用 attention FLOPs。
<!-- existing:SF-2026-ARXIV-2602-08722:end -->

<!-- delta:SF-2026-ARXIV-2602-08722:start -->
exact-v1 的 `arXiv:2602.08722v1 HTML — §3 QuoKA Method` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 prompt token、attention work、prefill plan 与 KV materialization。触发约束是：长输入和异构硬件使 token 选择、并行与带宽成为 TTFT 主约束。
<!-- delta:SF-2026-ARXIV-2602-08722:end -->

<!-- books-review:SF-2026-ARXIV-2602-08722:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-05-inference-system/42-what-happens-during-inference.md#本章要回答的问题 (line 10); books/part-05-inference-system/44-decode.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.08722v1 实际披露的机制与实验。方法定位为 arXiv:2602.08722v1 HTML — §3 QuoKA Method；验证定位为 arXiv:2602.08722v1 HTML — §4 results；边界定位为 arXiv:2602.08722v1 HTML — §4.5 Ablation study。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-08722:end -->

<!-- existing:SF-2026-ARXIV-2602-08747:start -->
已对读当前 owner `INFER-SCHEDULING` 在 `books/part-05-inference-system/56-inference-scheduling.md#slo-aware-admission (line 59)` 的命题：## SLO-aware Admission
<!-- existing:SF-2026-ARXIV-2602-08747:end -->

<!-- delta:SF-2026-ARXIV-2602-08747:start -->
exact-v1 的 `arXiv:2602.08747v1 HTML — §4. System Design` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 准入、批处理、优先级、路由和资源选择。触发约束是：长度、阶段、SLO、模型和 agent fan-out 的异质性使排队决策决定整体尾延迟。
<!-- delta:SF-2026-ARXIV-2602-08747:end -->

<!-- books-review:SF-2026-ARXIV-2602-08747:start -->
Decision=`Integrate`：现有命题原先未完整承载该 family 的长期机制责任；写回已在 canonical owner 中完成，并通过唯一 marker、正文位置和 claim-boundary 的 post-write fresh-context audit。 相邻章节已定位为 `books/part-05-inference-system/55-pd-disaggregation.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/57-what-is-ai-platform.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.08747v1 实际披露的机制与实验。方法定位为 arXiv:2602.08747v1 HTML — §4. System Design；验证定位为 arXiv:2602.08747v1 HTML — §5. Evaluation；边界定位为 arXiv:2602.08747v1 HTML — §7. Applicable to Other Workload。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-08747:end -->

<!-- existing:SF-2026-ARXIV-2602-08798:start -->
已对读当前 owner `PLATFORM-SECURITY` 在 `books/part-06-ai-infrastructure/72-security.md#风险管理而不是一次性认证 (line 1137)` 的命题：### 隐私不是一个开关，而是明文边界的重新分配
<!-- existing:SF-2026-ARXIV-2602-08798:end -->

<!-- delta:SF-2026-ARXIV-2602-08798:start -->
exact-v1 的 `arXiv:2602.08798v1 HTML — §4.1 CryptoGen Framework` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 身份、授权、数据流、策略执行点与审计证据。触发约束是：工具、记忆和多 agent 委托把不可信内容转化为可执行控制流。
<!-- delta:SF-2026-ARXIV-2602-08798:end -->

<!-- books-review:SF-2026-ARXIV-2602-08798:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-06-ai-infrastructure/71-multi-tenant.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/73-production-best-practice.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.08798v1 实际披露的机制与实验。方法定位为 arXiv:2602.08798v1 HTML — §4.1 CryptoGen Framework；验证定位为 arXiv:2602.08798v1 HTML — §6.3 Breakdown Analysis of a Single Transformer Block；独立 limitations 未披露，因而采用更窄主张。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-08798:end -->

<!-- existing:SF-2026-ARXIV-2602-08905:start -->
已对读当前 owner `TRAIN-RLHF` 在 `books/part-04-training-system/31-rlhf.md#rlhfrlaif-与-verifiable-reward (line 481)` 的命题：### 后训练分支的本质差异是 State Distribution
<!-- existing:SF-2026-ARXIV-2602-08905:end -->

<!-- delta:SF-2026-ARXIV-2602-08905:start -->
exact-v1 的 `arXiv:2602.08905v1 HTML — §5.2 Implementation Details` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 rollout、reward、policy/reference 与更新 freshness。触发约束是：模型规模、奖励来源和任务 horizon 改变后，同一配方的排序可能反转。
<!-- delta:SF-2026-ARXIV-2602-08905:end -->

<!-- books-review:SF-2026-ARXIV-2602-08905:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-04-training-system/30-lora.md#本章要回答的问题 (line 10); books/part-04-training-system/32-ppo.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.08905v1 实际披露的机制与实验。方法定位为 arXiv:2602.08905v1 HTML — §5.2 Implementation Details；验证定位为 arXiv:2602.08905v1 HTML — §5.3 Main Results；边界定位为 arXiv:2602.08905v1 HTML — §7 Conclusion and Future Work。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-08905:end -->

<!-- existing:SF-2026-ARXIV-2602-08968:start -->
已对读当前 owner `PLATFORM-EVALUATION-SYSTEM` 在 `books/part-06-ai-infrastructure/66-evaluation-system.md#工程实践从最小可信闭环开始 (line 2167)` 的命题：### Evaluation Object 必须携带依赖图、时间与可复现条件
<!-- existing:SF-2026-ARXIV-2602-08968:end -->

<!-- delta:SF-2026-ARXIV-2602-08968:start -->
exact-v1 的 `arXiv:2602.08968v1 HTML — §2.3 SWM Evaluation Suite: Tasks, Planning Algorithms, and Baselines` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 evaluation contract、覆盖分母、evidence lineage 与 release gate。触发约束是：agent、长时程和多模态系统把失败分散到状态、工具与环境交互链。
<!-- delta:SF-2026-ARXIV-2602-08968:end -->

<!-- books-review:SF-2026-ARXIV-2602-08968:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-06-ai-infrastructure/65-kai-scheduler.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/67-monitoring.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.08968v1 实际披露的机制与实验。方法定位为 arXiv:2602.08968v1 HTML — §2.3 SWM Evaluation Suite: Tasks, Planning Algorithms, and Baselines；验证定位为 arXiv:2602.08968v1 HTML — §2.3 SWM Evaluation Suite: Tasks, Planning Algorithms, and Baselines；边界定位为 arXiv:2602.08968v1 HTML — §4 Conclusion and Future Directions。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-08968:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
<!-- audit-receipt:FCSA-2026-02-FINAL:20260211:start -->
全月验收：`papers/2026/02/_sources/february-fresh-context-audit.json`；本日受审收据：`papers/2026/02/_sources/daily-20260211/screening-ledger-author.json`、`papers/2026/02/_sources/daily-20260211/screening-ledger-final.json`、`papers/2026/02/_sources/daily-20260211/exact-v1-review-packet.json`、`papers/2026/02/_sources/daily-20260211/books-current-content-comparison.json`、`papers/2026/02/_sources/daily-20260211/BOOKS_WRITEBACK_QUEUE.json`。
<!-- audit-receipt:FCSA-2026-02-FINAL:20260211:end -->

| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260211-COVERAGE-FINAL | fresh-context:february-independent-reviewer | coverage | coverage:SRC-ARXIV:20260211; audit-receipt:FCSA-2026-02-FINAL:20260211 | — | 本日 raw=1173、retained=35、closures=1138；全月 FP/FN、日期与撤稿 finding 均已解决 | passed |
| SA-20260211-EVIDENCE-FINAL | fresh-context:february-independent-reviewer | evidence | review:SF-2026-ARXIV-2602-07186; review:SF-2026-ARXIV-2602-07306; review:SF-2026-ARXIV-2602-07379; review:SF-2026-ARXIV-2602-07721; review:SF-2026-ARXIV-2602-07878; review:SF-2026-ARXIV-2602-08007; review:SF-2026-ARXIV-2602-08847; review:SF-2026-ARXIV-2602-07120; review:SF-2026-ARXIV-2602-07223; review:SF-2026-ARXIV-2602-07263; review:SF-2026-ARXIV-2602-07265; review:SF-2026-ARXIV-2602-07397; review:SF-2026-ARXIV-2602-07398; review:SF-2026-ARXIV-2602-07595; review:SF-2026-ARXIV-2602-07616; review:SF-2026-ARXIV-2602-07840; review:SF-2026-ARXIV-2602-07962; review:SF-2026-ARXIV-2602-07996; review:SF-2026-ARXIV-2602-08005; review:SF-2026-ARXIV-2602-08060; review:SF-2026-ARXIV-2602-08237; review:SF-2026-ARXIV-2602-08296; review:SF-2026-ARXIV-2602-08343; review:SF-2026-ARXIV-2602-08382; review:SF-2026-ARXIV-2602-08401; review:SF-2026-ARXIV-2602-08404; review:SF-2026-ARXIV-2602-08412; review:SF-2026-ARXIV-2602-08563; review:SF-2026-ARXIV-2602-08585; review:SF-2026-ARXIV-2602-08621; review:SF-2026-ARXIV-2602-08722; review:SF-2026-ARXIV-2602-08747; review:SF-2026-ARXIV-2602-08798; review:SF-2026-ARXIV-2602-08905; review:SF-2026-ARXIV-2602-08968; audit-receipt:FCSA-2026-02-FINAL:20260211 | — | exact-v1 complete=35、blocked=0；locator、excerpt、RP 与 claim boundary 已验收 | passed |
| SA-20260211-SELECTION-FINAL | fresh-context:february-independent-reviewer | deep_analysis_selection | validator:deep-analysis-selection-v1; audit-receipt:FCSA-2026-02-FINAL:20260211 | — | 本日完整 eligibility frontier 与最多三个叙事单元已验收，未选择项均保留显式理由 | passed |
| SA-20260211-BOOKS-POSTWRITE-FINAL | fresh-context:february-independent-reviewer | books | books-review:SF-2026-ARXIV-2602-07186; books-review:SF-2026-ARXIV-2602-07306; books-review:SF-2026-ARXIV-2602-07379; books-review:SF-2026-ARXIV-2602-07721; books-review:SF-2026-ARXIV-2602-07878; books-review:SF-2026-ARXIV-2602-08007; books-review:SF-2026-ARXIV-2602-08847; books-review:SF-2026-ARXIV-2602-07120; books-review:SF-2026-ARXIV-2602-07223; books-review:SF-2026-ARXIV-2602-07263; books-review:SF-2026-ARXIV-2602-07265; books-review:SF-2026-ARXIV-2602-07397; books-review:SF-2026-ARXIV-2602-07398; books-review:SF-2026-ARXIV-2602-07595; books-review:SF-2026-ARXIV-2602-07616; books-review:SF-2026-ARXIV-2602-07840; books-review:SF-2026-ARXIV-2602-07962; books-review:SF-2026-ARXIV-2602-07996; books-review:SF-2026-ARXIV-2602-08005; books-review:SF-2026-ARXIV-2602-08060; books-review:SF-2026-ARXIV-2602-08237; books-review:SF-2026-ARXIV-2602-08296; books-review:SF-2026-ARXIV-2602-08343; books-review:SF-2026-ARXIV-2602-08382; books-review:SF-2026-ARXIV-2602-08401; books-review:SF-2026-ARXIV-2602-08404; books-review:SF-2026-ARXIV-2602-08412; books-review:SF-2026-ARXIV-2602-08563; books-review:SF-2026-ARXIV-2602-08585; books-review:SF-2026-ARXIV-2602-08621; books-review:SF-2026-ARXIV-2602-08722; books-review:SF-2026-ARXIV-2602-08747; books-review:SF-2026-ARXIV-2602-08798; books-review:SF-2026-ARXIV-2602-08905; books-review:SF-2026-ARXIV-2602-08968; audit-receipt:FCSA-2026-02-FINAL:20260211 | — | 本日 Integrate=5；canonical owner、相邻命题、disposition 与 post-write/no-writeback 状态已验收 | passed |

## 8. Ignored Noise

1138 个 pre-denominator closure 保存在 `papers/2026/02/_sources/daily-20260211/screening-ledger-final.json`；每项含 identity、title、abstract 与 family-specific reason。withdrawn=0，撤稿不留 selected 痕迹。

## 9. Recommended Action

本日四域 Gate 已关闭；保留 `papers/2026/02/_sources/february-fresh-context-audit.json` 与本地冻结收据。仅在 primary evidence、撤稿状态或公共合同变化时重新打开对应 scope。

## 10. Repository Changes

- promotion 更新 `papers/2026/02/11/README.md` 与本日 `_sources` 最终状态收据。
- 本步骤不修改 Books 或 Weekly，也不 stage、commit 或 push；此前已验收的 Books 写回由本日 queue 记录 post-write 状态。

## 11. Open Questions

- 无 Gate 阻塞项；论文自身未证明的边界继续保留在 Claim Boundary 中，不构成未解决流程 finding。

## 12. Sources

- [arXiv:2602.07186v1](https://arxiv.org/abs/2602.07186v1) — official exact-v1；first-public `2026-02-10T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.07306v1](https://arxiv.org/abs/2602.07306v1) — official exact-v1；first-public `2026-02-10T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.07379v1](https://arxiv.org/abs/2602.07379v1) — official exact-v1；first-public `2026-02-10T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.07721v1](https://arxiv.org/abs/2602.07721v1) — official exact-v1；first-public `2026-02-10T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.07878v1](https://arxiv.org/abs/2602.07878v1) — official exact-v1；first-public `2026-02-10T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.08007v1](https://arxiv.org/abs/2602.08007v1) — official exact-v1；first-public `2026-02-10T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.08847v1](https://arxiv.org/abs/2602.08847v1) — official exact-v1；first-public `2026-02-10T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.07120v1](https://arxiv.org/abs/2602.07120v1) — official exact-v1；first-public `2026-02-10T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.07223v1](https://arxiv.org/abs/2602.07223v1) — official exact-v1；first-public `2026-02-10T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.07263v1](https://arxiv.org/abs/2602.07263v1) — official exact-v1；first-public `2026-02-10T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.07265v1](https://arxiv.org/abs/2602.07265v1) — official exact-v1；first-public `2026-02-10T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.07397v1](https://arxiv.org/abs/2602.07397v1) — official exact-v1；first-public `2026-02-10T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.07398v1](https://arxiv.org/abs/2602.07398v1) — official exact-v1；first-public `2026-02-10T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.07595v1](https://arxiv.org/abs/2602.07595v1) — official exact-v1；first-public `2026-02-10T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.07616v1](https://arxiv.org/abs/2602.07616v1) — official exact-v1；first-public `2026-02-10T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.07840v1](https://arxiv.org/abs/2602.07840v1) — official exact-v1；first-public `2026-02-10T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.07962v1](https://arxiv.org/abs/2602.07962v1) — official exact-v1；first-public `2026-02-10T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.07996v1](https://arxiv.org/abs/2602.07996v1) — official exact-v1；first-public `2026-02-10T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.08005v1](https://arxiv.org/abs/2602.08005v1) — official exact-v1；first-public `2026-02-10T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.08060v1](https://arxiv.org/abs/2602.08060v1) — official exact-v1；first-public `2026-02-10T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.08237v1](https://arxiv.org/abs/2602.08237v1) — official exact-v1；first-public `2026-02-10T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.08296v1](https://arxiv.org/abs/2602.08296v1) — official exact-v1；first-public `2026-02-10T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.08343v1](https://arxiv.org/abs/2602.08343v1) — official exact-v1；first-public `2026-02-10T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.08382v1](https://arxiv.org/abs/2602.08382v1) — official exact-v1；first-public `2026-02-10T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.08401v1](https://arxiv.org/abs/2602.08401v1) — official exact-v1；first-public `2026-02-10T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.08404v1](https://arxiv.org/abs/2602.08404v1) — official exact-v1；first-public `2026-02-10T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.08412v1](https://arxiv.org/abs/2602.08412v1) — official exact-v1；first-public `2026-02-10T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.08563v1](https://arxiv.org/abs/2602.08563v1) — official exact-v1；first-public `2026-02-10T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.08585v1](https://arxiv.org/abs/2602.08585v1) — official exact-v1；first-public `2026-02-10T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.08621v1](https://arxiv.org/abs/2602.08621v1) — official exact-v1；first-public `2026-02-10T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.08722v1](https://arxiv.org/abs/2602.08722v1) — official exact-v1；first-public `2026-02-10T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.08747v1](https://arxiv.org/abs/2602.08747v1) — official exact-v1；first-public `2026-02-10T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.08798v1](https://arxiv.org/abs/2602.08798v1) — official exact-v1；first-public `2026-02-10T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.08905v1](https://arxiv.org/abs/2602.08905v1) — official exact-v1；first-public `2026-02-10T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.08968v1](https://arxiv.org/abs/2602.08968v1) — official exact-v1；first-public `2026-02-10T09:00:00+08:00`；访问日期 2026-09-02。

## 13. Final Status

Completion Status=`Complete`；Coverage=`Closed`；Evidence=`Passed`；Books=`Passed`；Unresolved Findings=0。最终 raw=1173、retained=35、closures=1138、exact-v1 reviews=35、blocked=0。
