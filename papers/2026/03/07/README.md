# Daily Research — 2026-03-07

**Research Date:** 2026-03-07

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-03-06 09:00:00 ～ 2026-03-07 09:00:00（Asia/Shanghai，左闭右开）

**Contract:** V2.1 Historical Daily independent Full Replay；既有 Weekly 未参与 discovery、分母、评分、Review、Books 判断或漏项校准；Weekly dependency=0。

**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed；fresh-context Coverage / Evidence / Selection / Books Semantic Audit 与必要的 post-write audit 均已闭合。

## Executive Summary

窗口内 raw identities=593，完成 title+abstract semantic screening=593/593；冻结 Candidate Denominator=31，pre-denominator closures=562。exact-v1 Review=31/31，withdrawn=0，blocked=0；Books Integrate proposal=2。

3 月 arXiv 的 `Submitted:v1` 与 `Updated:v1` 只作为版本 provenance，不承担事件归属。日报以 DataCite DOI `created/registered` 恢复 identity，再按官方 Sun–Thu 20:00 Eastern 公告时刻映射到北京时间半开窗口。公告落在 09:00 右边界时不归结束于该时刻的窗口，而归下一份日报。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-03-07 |
| Window End | 2026-03-07 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | sha256:0cf99bd5171cb326a085eb089e377362a304e5240a5b182cc35c26f5d7223158 |
| Denominator Frozen At | 2026-09-02T08:53:37Z |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-03-06T09:00:00+08:00 | 2026-03-07T09:00:00+08:00 | 2026-09-02T08:53:37Z | official arXiv March archive + scheduled announcement recovery + exact-v1 abs/HTML/PDF; registered categories; 593/593 semantic replay | checked | 31 | SF-2026-ARXIV-2603-04402; SF-2026-ARXIV-2603-04424; SF-2026-ARXIV-2603-04428; SF-2026-ARXIV-2603-04443; SF-2026-ARXIV-2603-04444; SF-2026-ARXIV-2603-04448; SF-2026-ARXIV-2603-04459; SF-2026-ARXIV-2603-04460; SF-2026-ARXIV-2603-04469; SF-2026-ARXIV-2603-04797; SF-2026-ARXIV-2603-04902; SF-2026-ARXIV-2603-04910; SF-2026-ARXIV-2603-04981; SF-2026-ARXIV-2603-05031; SF-2026-ARXIV-2603-05185; SF-2026-ARXIV-2603-05438; SF-2026-ARXIV-2603-05451; SF-2026-ARXIV-2603-05454; SF-2026-ARXIV-2603-04411; SF-2026-ARXIV-2603-04417; SF-2026-ARXIV-2603-04427; SF-2026-ARXIV-2603-04621; SF-2026-ARXIV-2603-04656; SF-2026-ARXIV-2603-04851; SF-2026-ARXIV-2603-05087; SF-2026-ARXIV-2603-05147; SF-2026-ARXIV-2603-05210; SF-2026-ARXIV-2603-05353; SF-2026-ARXIV-2603-05399; SF-2026-ARXIV-2603-04814; SF-2026-ARXIV-2603-04896 | Not Applicable — frozen shared archive receipt enumerates the complete owner batch | 2026-03-07T09:00:00+08:00 | papers/2026/03/_sources/daily-20260307/official-archive-membership-receipt.json; papers/2026/03/_sources/daily-20260307/screening-ledger-final.json; coverage:SRC-ARXIV:20260307 | — |

<!-- coverage:SRC-ARXIV:20260307:start -->本次独立重放以官方公告日程恢复 strict-window inventory；保留 exact-ID archive membership 与 exact-v1 identity/access。当前注册表在 2026-08-25 生效，不反推 2026-03 的机构来源为当日 Required；all raw title+abstract rows 已由独立 reviewer 逐项完成 FP/FN audit，Coverage Gate Closed。<!-- coverage:SRC-ARXIV:20260307:end -->

### Later-effective non-arXiv archival replay

虽然 20 个机构/发现来源的 registry Effective Date 为 2026-08-25、按合同不反推为本日 Required，父任务仍要求本次执行 bounded archival replay。独立收据为 `papers/2026/03/_sources/daily-20260307/non-arxiv-historical-replay-receipt.json`；状态计数为 `{"date_only_lead_unowned": 3, "enumerated_no_hit": 9, "historical_backstop_incomplete": 1, "historical_cursor_incomplete": 7}`。没有任何线索同时取得 strict-window first-public instant 与长期机制证据，因此新增 Candidate Source Family=0。

日期-only 边界线索（不归属、不评分、不进入分母）：

- `SRC-QWEN` — `2026-03-06` — [Qwen Code update](https://qwenlm.github.io/qwen-code-docs/en/blog/updates/)；官方页面没有精确发布时间/时区。

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-04402 | arXiv:2603.04402v1 | paper-v1:2603.04402 | 2026-W10 | 2026-03-06 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-04402 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-04402 | no |
| SF-2026-ARXIV-2603-04424 | arXiv:2603.04424v1 | paper-v1:2603.04424 | 2026-W10 | 2026-03-06 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-04424 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-04424 | no |
| SF-2026-ARXIV-2603-04428 | arXiv:2603.04428v1 | paper-v1:2603.04428 | 2026-W10 | 2026-03-06 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-04428 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-04428 | no |
| SF-2026-ARXIV-2603-04443 | arXiv:2603.04443v1 | paper-v1:2603.04443 | 2026-W10 | 2026-03-06 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-04443 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-04443 | no |
| SF-2026-ARXIV-2603-04444 | arXiv:2603.04444v1 | paper-v1:2603.04444 | 2026-W10 | 2026-03-06 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-04444 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-04444 | no |
| SF-2026-ARXIV-2603-04448 | arXiv:2603.04448v1 | paper-v1:2603.04448 | 2026-W10 | 2026-03-06 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-04448 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-04448 | no |
| SF-2026-ARXIV-2603-04459 | arXiv:2603.04459v1 | paper-v1:2603.04459 | 2026-W10 | 2026-03-06 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-04459 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-04459 | no |
| SF-2026-ARXIV-2603-04460 | arXiv:2603.04460v1 | paper-v1:2603.04460 | 2026-W10 | 2026-03-06 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-04460 | self | — | new_in_window | INFER-PREFILL | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-04460 | no |
| SF-2026-ARXIV-2603-04469 | arXiv:2603.04469v1 | paper-v1:2603.04469 | 2026-W10 | 2026-03-06 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-04469 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-04469 | no |
| SF-2026-ARXIV-2603-04797 | arXiv:2603.04797v1 | paper-v1:2603.04797 | 2026-W10 | 2026-03-06 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-04797 | self | — | new_in_window | INFER-GPU-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-04797 | no |
| SF-2026-ARXIV-2603-04902 | arXiv:2603.04902v1 | paper-v1:2603.04902 | 2026-W10 | 2026-03-06 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-04902 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-04902 | no |
| SF-2026-ARXIV-2603-04910 | arXiv:2603.04910v1 | paper-v1:2603.04910 | 2026-W10 | 2026-03-06 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-04910 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-04910 | no |
| SF-2026-ARXIV-2603-04981 | arXiv:2603.04981v1 | paper-v1:2603.04981 | 2026-W10 | 2026-03-06 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-04981 | self | — | new_in_window | TRAIN-DATA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-04981 | no |
| SF-2026-ARXIV-2603-05031 | arXiv:2603.05031v1 | paper-v1:2603.05031 | 2026-W10 | 2026-03-06 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-05031 | self | — | new_in_window | AGENT-TOOL-CALLING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05031 | no |
| SF-2026-ARXIV-2603-05185 | arXiv:2603.05185v1 | paper-v1:2603.05185 | 2026-W10 | 2026-03-06 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-05185 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05185 | no |
| SF-2026-ARXIV-2603-05438 | arXiv:2603.05438v1 | paper-v1:2603.05438 | 2026-W10 | 2026-03-06 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-05438 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05438 | no |
| SF-2026-ARXIV-2603-05451 | arXiv:2603.05451v1 | paper-v1:2603.05451 | 2026-W10 | 2026-03-06 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-05451 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05451 | no |
| SF-2026-ARXIV-2603-05454 | arXiv:2603.05454v1 | paper-v1:2603.05454 | 2026-W10 | 2026-03-06 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-05454 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05454 | no |
| SF-2026-ARXIV-2603-04411 | arXiv:2603.04411v1 | paper-v1:2603.04411 | 2026-W10 | 2026-03-06 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-04411 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-04411 | no |
| SF-2026-ARXIV-2603-04417 | arXiv:2603.04417v1 | paper-v1:2603.04417 | 2026-W10 | 2026-03-06 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-04417 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-04417 | no |
| SF-2026-ARXIV-2603-04427 | arXiv:2603.04427v1 | paper-v1:2603.04427 | 2026-W10 | 2026-03-06 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-04427 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-04427 | no |
| SF-2026-ARXIV-2603-04621 | arXiv:2603.04621v1 | paper-v1:2603.04621 | 2026-W10 | 2026-03-06 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-04621 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-04621 | no |
| SF-2026-ARXIV-2603-04656 | arXiv:2603.04656v1 | paper-v1:2603.04656 | 2026-W10 | 2026-03-06 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-04656 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-04656 | no |
| SF-2026-ARXIV-2603-04851 | arXiv:2603.04851v1 | paper-v1:2603.04851 | 2026-W10 | 2026-03-06 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2603-04851 | self | — | new_in_window | TRAIN-RLHF | Integrate | books-review:SF-2026-ARXIV-2603-04851 | no |
| SF-2026-ARXIV-2603-05087 | arXiv:2603.05087v1 | paper-v1:2603.05087 | 2026-W10 | 2026-03-06 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-05087 | self | — | new_in_window | PLATFORM-GPU-SCHEDULER | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05087 | no |
| SF-2026-ARXIV-2603-05147 | arXiv:2603.05147v1 | paper-v1:2603.05147 | 2026-W10 | 2026-03-06 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-05147 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05147 | no |
| SF-2026-ARXIV-2603-05210 | arXiv:2603.05210v1 | paper-v1:2603.05210 | 2026-W10 | 2026-03-06 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-05210 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05210 | no |
| SF-2026-ARXIV-2603-05353 | arXiv:2603.05353v1 | paper-v1:2603.05353 | 2026-W10 | 2026-03-06 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2603-05353 | self | — | new_in_window | INFER-KV-CACHE | Integrate | books-review:SF-2026-ARXIV-2603-05353 | no |
| SF-2026-ARXIV-2603-05399 | arXiv:2603.05399v1 | paper-v1:2603.05399 | 2026-W10 | 2026-03-06 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-05399 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05399 | no |
| SF-2026-ARXIV-2603-04814 | arXiv:2603.04814v1 | paper-v1:2603.04814 | 2026-W10 | 2026-03-06 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-04814 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-04814 | no |
| SF-2026-ARXIV-2603-04896 | arXiv:2603.04896v1 | paper-v1:2603.04896 | 2026-W10 | 2026-03-06 | SRC-ARXIV | 2 | 3 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-04896 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-04896 | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-04402 | RP-5d94917e0ffada62 | deep | arXiv:2603.04402v1 | SRC-ARXIV@arXiv:2603.04402v1 | https://arxiv.org/html/2603.04402v1#S3 — exact-v1 S3 — 3 The SearchGym Architecture (Method) | https://arxiv.org/html/2603.04402v1#S5 — exact-v1 S5 — 5 Experiments (Evaluation) | https://arxiv.org/html/2603.04402v1#S7 — exact-v1 S7 — 7 Conclusion: The Gym as a Laboratory (Limitations) | https://arxiv.org/html/2603.04402v1#S4 — exact-v1 S4 — 4 Config-Driven System Synthesis (Artifact) | claim:SF-2026-ARXIV-2603-04402 | complete |
| SF-2026-ARXIV-2603-04424 | RP-8b1bb4201fe52427 | deep | arXiv:2603.04424v1 | SRC-ARXIV@arXiv:2603.04424v1 | https://arxiv.org/html/2603.04424v1#S4.SS2 — exact-v1 S4.SS2 — 4.2 System Architecture Overview (Method) | https://arxiv.org/html/2603.04424v1#S6.SS1 — exact-v1 S6.SS1 — 6.1 Experimental Setup (Evaluation) | https://arxiv.org/html/2603.04424v1#S7 — exact-v1 S7 — 7 Discussion (Limitations) | https://arxiv.org/html/2603.04424v1#S5 — exact-v1 S5 — 5 Implementation (Artifact) | claim:SF-2026-ARXIV-2603-04424 | complete |
| SF-2026-ARXIV-2603-04428 | RP-04393ad09dee8e17 | deep | arXiv:2603.04428v1 | SRC-ARXIV@arXiv:2603.04428v1 | https://arxiv.org/html/2603.04428v1#A5 — exact-v1 A5 — Appendix E Perplexity Methodology (Method) | https://arxiv.org/html/2603.04428v1#S4 — exact-v1 S4 — 4 Evaluation (Evaluation) | https://arxiv.org/html/2603.04428v1#S5.SS6 — exact-v1 S5.SS6 — 5.6 Limitations (Limitations) | Not Disclosed — arXiv:2603.04428v1 exposes no dedicated Artifact / implementation section in the recovered exact-v1 body | claim:SF-2026-ARXIV-2603-04428 | complete |
| SF-2026-ARXIV-2603-04443 | RP-8881e423df307bfd | deep | arXiv:2603.04443v1 | SRC-ARXIV@arXiv:2603.04443v1 | https://arxiv.org/pdf/2603.04443v1#page=3 — PDF page 3; exact heading 3. Design Goals 4. AMV-L Overview (Method) | https://arxiv.org/pdf/2603.04443v1#page=7 — PDF page 7; exact heading 9.1 Experimental protocol (Evaluation) | https://arxiv.org/pdf/2603.04443v1#page=13 — PDF page 13; exact heading 10.4.6 Limitations and extensions Communications Societies (IEEE Cat. (Limitations) | https://arxiv.org/pdf/2603.04443v1#page=8 — PDF page 8; exact heading 9.6 Reproducibility (Artifact) | claim:SF-2026-ARXIV-2603-04443 | complete |
| SF-2026-ARXIV-2603-04444 | RP-d49477afd7931f6b | deep | arXiv:2603.04444v1 | SRC-ARXIV@arXiv:2603.04444v1 | https://arxiv.org/html/2603.04444v1#S8.SS5 — exact-v1 S8.SS5 — 8.5 Training Methodology (Method) | https://arxiv.org/html/2603.04444v1#S15 — exact-v1 S15 — 15 Evaluation (Evaluation) | https://arxiv.org/html/2603.04444v1#S17 — exact-v1 S17 — 17 Conclusion (Limitations) | https://arxiv.org/html/2603.04444v1#S14 — exact-v1 S14 — 14 Deployment (Artifact) | claim:SF-2026-ARXIV-2603-04444 | complete |
| SF-2026-ARXIV-2603-04448 | RP-e953bb5043017950 | deep | arXiv:2603.04448v1 | SRC-ARXIV@arXiv:2603.04448v1 | https://arxiv.org/html/2603.04448v1#S3.SS1 — exact-v1 S3.SS1 — 3.1 Overview (Method) | https://arxiv.org/html/2603.04448v1#S4 — exact-v1 S4 — 4 Quantitative Evaluation (Evaluation) | https://arxiv.org/html/2603.04448v1#S8 — exact-v1 S8 — 8 Limitations (Limitations) | https://arxiv.org/html/2603.04448v1#S3.SS6 — exact-v1 S3.SS6 — 3.6 Open Resources (Artifact) | claim:SF-2026-ARXIV-2603-04448 | complete |
| SF-2026-ARXIV-2603-04459 | RP-3c88e12524c0d41e | deep | arXiv:2603.04459v1 | SRC-ARXIV@arXiv:2603.04459v1 | https://arxiv.org/html/2603.04459v1#A12.SS1 — exact-v1 A12.SS1 — Selection of Correlation Analysis Method (Method) | https://arxiv.org/html/2603.04459v1#A9 — exact-v1 A9 — Appendix I Descriptive Statistical Analysis of Influence Evaluation (Evaluation) | https://arxiv.org/html/2603.04459v1#S8 — exact-v1 S8 — Discussion and Limitation (Limitations) | Not Disclosed — arXiv:2603.04459v1 exposes no dedicated Artifact / implementation section in the recovered exact-v1 body | claim:SF-2026-ARXIV-2603-04459 | complete |
| SF-2026-ARXIV-2603-04460 | RP-c49576a5c3dc8405 | deep | arXiv:2603.04460v1 | SRC-ARXIV@arXiv:2603.04460v1 | https://arxiv.org/html/2603.04460v1#S4 — exact-v1 S4 — 4 Method (Method) | https://arxiv.org/html/2603.04460v1#S5 — exact-v1 S5 — 5 Experiments (Evaluation) | https://arxiv.org/html/2603.04460v1#S6 — exact-v1 S6 — 6 Conclusion and Future Work (Limitations) | https://arxiv.org/html/2603.04460v1#S4.SS3.SSS0.Px2 — exact-v1 S4.SS3.SSS0.Px2 — Fused attention kernel implementation (Artifact) | claim:SF-2026-ARXIV-2603-04460 | complete |
| SF-2026-ARXIV-2603-04469 | RP-fb1f9b545dbab184 | deep | arXiv:2603.04469v1 | SRC-ARXIV@arXiv:2603.04469v1 | https://arxiv.org/html/2603.04469v1#S4 — exact-v1 S4 — 4 Method (Method) | https://arxiv.org/html/2603.04469v1#S5 — exact-v1 S5 — 5 Experiment (Evaluation) | https://arxiv.org/html/2603.04469v1#S6 — exact-v1 S6 — 6 Conclusion (Limitations) | Not Disclosed — arXiv:2603.04469v1 exposes no dedicated Artifact / implementation section in the recovered exact-v1 body | claim:SF-2026-ARXIV-2603-04469 | complete |
| SF-2026-ARXIV-2603-04797 | RP-74adead474f7e611 | deep | arXiv:2603.04797v1 | SRC-ARXIV@arXiv:2603.04797v1 | https://arxiv.org/html/2603.04797v1#S6.SS1 — exact-v1 S6.SS1 — VI-A Evaluation Methodology (Method) | https://arxiv.org/html/2603.04797v1#S6 — exact-v1 S6 — VI Evaluation (Evaluation) | https://arxiv.org/html/2603.04797v1#S2.SS4 — exact-v1 S2.SS4 — II-D Limitations of Serving-Oriented NMP Designs (Limitations) | https://arxiv.org/html/2603.04797v1#S5 — exact-v1 S5 — V Helios System Design (Artifact) | claim:SF-2026-ARXIV-2603-04797 | complete |
| SF-2026-ARXIV-2603-04902 | RP-152b9b3b777a6528 | deep | arXiv:2603.04902v1 | SRC-ARXIV@arXiv:2603.04902v1 | https://arxiv.org/html/2603.04902v1#S2 — exact-v1 S2 — 2 Privacy Flow Graph (Method) | https://arxiv.org/html/2603.04902v1#S4 — exact-v1 S4 — 4 Experiments (Evaluation) | https://arxiv.org/html/2603.04902v1#S4.SS1 — exact-v1 S4.SS1 — 4.1 Discussion (Limitations) | https://arxiv.org/html/2603.04902v1#S3 — exact-v1 S3 — 3 AgentSCOPE: A Contextual Integrity-focused Benchmark (Artifact) | claim:SF-2026-ARXIV-2603-04902 | complete |
| SF-2026-ARXIV-2603-04910 | RP-6031741a9217fee6 | deep | arXiv:2603.04910v1 | SRC-ARXIV@arXiv:2603.04910v1 | https://arxiv.org/html/2603.04910v1#S4 — exact-v1 S4 — IV Method (Method) | https://arxiv.org/html/2603.04910v1#S5 — exact-v1 S5 — V Experiments (Evaluation) | https://arxiv.org/html/2603.04910v1#S6 — exact-v1 S6 — VI Conclusion (Limitations) | https://arxiv.org/html/2603.04910v1#S5.SS1 — exact-v1 S5.SS1 — V-A Experimental Setup (Artifact) | claim:SF-2026-ARXIV-2603-04910 | complete |
| SF-2026-ARXIV-2603-04981 | RP-6745eb188afcf3f0 | deep | arXiv:2603.04981v1 | SRC-ARXIV@arXiv:2603.04981v1 | https://arxiv.org/html/2603.04981v1#S3 — exact-v1 S3 — 3 Method (Method) | https://arxiv.org/html/2603.04981v1#S4 — exact-v1 S4 — 4 Experiments (Evaluation) | https://arxiv.org/html/2603.04981v1#S5 — exact-v1 S5 — 5 Conclusion (Limitations) | Not Disclosed — arXiv:2603.04981v1 exposes no dedicated Artifact / implementation section in the recovered exact-v1 body | claim:SF-2026-ARXIV-2603-04981 | complete |
| SF-2026-ARXIV-2603-05031 | RP-ab998464e9294a12 | deep | arXiv:2603.05031v1 | SRC-ARXIV@arXiv:2603.05031v1 | https://arxiv.org/html/2603.05031v1#S5 — exact-v1 S5 — V AegisUI Framework (Method) | https://arxiv.org/html/2603.05031v1#S9 — exact-v1 S9 — IX Experimental Setup (Evaluation) | https://arxiv.org/html/2603.05031v1#S11 — exact-v1 S11 — XI Discussion (Limitations) | https://arxiv.org/html/2603.05031v1#S9 — exact-v1 S9 — IX Experimental Setup (Artifact) | claim:SF-2026-ARXIV-2603-05031 | complete |
| SF-2026-ARXIV-2603-05185 | RP-b64817e7eefe7904 | deep | arXiv:2603.05185v1 | SRC-ARXIV@arXiv:2603.05185v1 | https://arxiv.org/html/2603.05185v1#S3 — exact-v1 S3 — 3 Methodology (Method) | https://arxiv.org/html/2603.05185v1#S4 — exact-v1 S4 — 4 Experiments (Evaluation) | https://arxiv.org/html/2603.05185v1#S5 — exact-v1 S5 — 5 Conclusions (Limitations) | https://arxiv.org/html/2603.05185v1#S4.SS1.SSSx2 — exact-v1 S4.SS1.SSSx2 — Implementation Details. (Artifact) | claim:SF-2026-ARXIV-2603-05185 | complete |
| SF-2026-ARXIV-2603-05438 | RP-0dd122a220fabcbc | deep | arXiv:2603.05438v1 | SRC-ARXIV@arXiv:2603.05438v1 | https://arxiv.org/html/2603.05438v1#S3 — exact-v1 S3 — 3 Method (Method) | https://arxiv.org/html/2603.05438v1#S4 — exact-v1 S4 — 4 Experiment (Evaluation) | https://arxiv.org/html/2603.05438v1#S5 — exact-v1 S5 — 5 Conclusion (Limitations) | https://arxiv.org/html/2603.05438v1#S5a — exact-v1 S5a — E Details of CompACT tokenizer (Artifact) | claim:SF-2026-ARXIV-2603-05438 | complete |
| SF-2026-ARXIV-2603-05451 | RP-28380edbe1626a09 | deep | arXiv:2603.05451v1 | SRC-ARXIV@arXiv:2603.05451v1 | https://arxiv.org/html/2603.05451v1#S4 — exact-v1 S4 — 4 Language and Framework (Method) | https://arxiv.org/html/2603.05451v1#A1 — exact-v1 A1 — Appendix A Additional Details on Experiments and Benchmarking (Evaluation) | https://arxiv.org/html/2603.05451v1#S6 — exact-v1 S6 — 6 Discussion and Conclusion (Limitations) | https://arxiv.org/html/2603.05451v1#A1.SS1 — exact-v1 A1.SS1 — A.1 System and libraries (Artifact) | claim:SF-2026-ARXIV-2603-05451 | complete |
| SF-2026-ARXIV-2603-05454 | RP-3ee9b0ad8407c074 | deep | arXiv:2603.05454v1 | SRC-ARXIV@arXiv:2603.05454v1 | https://arxiv.org/html/2603.05454v1#S3 — exact-v1 S3 — 3 Method (Method) | https://arxiv.org/html/2603.05454v1#S4 — exact-v1 S4 — 4 Experiments (Evaluation) | https://arxiv.org/html/2603.05454v1#S5 — exact-v1 S5 — 5 Conclusion (Limitations) | https://arxiv.org/html/2603.05454v1#S4.SS1 — exact-v1 S4.SS1 — 4.1 Experimental Setup (Artifact) | claim:SF-2026-ARXIV-2603-05454 | complete |
| SF-2026-ARXIV-2603-04411 | RP-8f727c4882b0606e | deep | arXiv:2603.04411v1 | SRC-ARXIV@arXiv:2603.04411v1 | https://arxiv.org/html/2603.04411v1#S2.SS0.SSS0.Px3 — exact-v1 S2.SS0.SSS0.Px3 — Architecture-Intrinsic Methods (Method) | https://arxiv.org/html/2603.04411v1#S4 — exact-v1 S4 — 4 Experiments (Evaluation) | https://arxiv.org/html/2603.04411v1#S6 — exact-v1 S6 — 6 Conclusion (Limitations) | https://arxiv.org/html/2603.04411v1#S5.SS2.SSS0.Px1 — exact-v1 S5.SS2.SSS0.Px1 — Implementation Details (Artifact) | claim:SF-2026-ARXIV-2603-04411 | complete |
| SF-2026-ARXIV-2603-04417 | RP-1bd88ca865b3aaaf | deep | arXiv:2603.04417v1 | SRC-ARXIV@arXiv:2603.04417v1 | https://arxiv.org/pdf/2603.04417v1#page=4 — PDF page 4; exact heading 3. Experiment (Method) | https://arxiv.org/pdf/2603.04417v1#page=4 — PDF page 4; exact heading 3. Experiment (Evaluation) | https://arxiv.org/pdf/2603.04417v1#page=13 — PDF page 13; exact heading 6. Future Work & Limitations (Limitations) | https://arxiv.org/pdf/2603.04417v1#page=4 — PDF page 4; exact heading 3. Experiment (Artifact) | claim:SF-2026-ARXIV-2603-04417 | complete |
| SF-2026-ARXIV-2603-04427 | RP-2e30e9bef11aeedc | deep | arXiv:2603.04427v1 | SRC-ARXIV@arXiv:2603.04427v1 | https://arxiv.org/html/2603.04427v1#S2 — exact-v1 S2 — 2 Method (Method) | https://arxiv.org/html/2603.04427v1#S3 — exact-v1 S3 — 3 Experiments (Evaluation) | https://arxiv.org/html/2603.04427v1#S6.SS0.SSS0.Px1 — exact-v1 S6.SS0.SSS0.Px1 — Limitations. (Limitations) | https://arxiv.org/html/2603.04427v1#S3.SS5.SSS0.Px3 — exact-v1 S3.SS5.SSS0.Px3 — Deployment via factored keys. (Artifact) | claim:SF-2026-ARXIV-2603-04427 | complete |
| SF-2026-ARXIV-2603-04621 | RP-369b9b59987dcb2a | deep | arXiv:2603.04621v1 | SRC-ARXIV@arXiv:2603.04621v1 | https://arxiv.org/html/2603.04621v1#S4 — exact-v1 S4 — 4 Programming Model and Library Architecture (Method) | https://arxiv.org/html/2603.04621v1#S7 — exact-v1 S7 — 7 Experiments (Evaluation) | https://arxiv.org/html/2603.04621v1#S8 — exact-v1 S8 — 8 Discussion and Limitations (Limitations) | https://arxiv.org/html/2603.04621v1#S7.SS0.SSS0.Px1 — exact-v1 S7.SS0.SSS0.Px1 — Implementation parity (Artifact) | claim:SF-2026-ARXIV-2603-04621 | complete |
| SF-2026-ARXIV-2603-04656 | RP-3e91b241676f03ea | deep | arXiv:2603.04656v1 | SRC-ARXIV@arXiv:2603.04656v1 | https://arxiv.org/html/2603.04656v1#S3 — exact-v1 S3 — 3. Method (Method) | https://arxiv.org/html/2603.04656v1#S5 — exact-v1 S5 — 5. Experiments & Results (Evaluation) | https://arxiv.org/html/2603.04656v1#S7 — exact-v1 S7 — 7. Limitations (Limitations) | Not Disclosed — arXiv:2603.04656v1 exposes no dedicated Artifact / implementation section in the recovered exact-v1 body | claim:SF-2026-ARXIV-2603-04656 | complete |
| SF-2026-ARXIV-2603-04851 | RP-e04b0150ebabeba4 | deep | arXiv:2603.04851v1 | SRC-ARXIV@arXiv:2603.04851v1 | https://arxiv.org/html/2603.04851v1#S4 — exact-v1 §4 Martingale Decomposition of Harm, followed by §5–§9 gradient and recovery analysis (Method) | https://arxiv.org/html/2603.04851v1#A2 — exact-v1 A2 — Appendix B Proofs and Supplementary Results for Deep Alignment (Evaluation) | https://arxiv.org/html/2603.04851v1#Sx1 — exact-v1 Sx1 — Limitations (Limitations) | Not Disclosed — arXiv:2603.04851v1 exposes no dedicated Artifact / implementation section in the recovered exact-v1 body | claim:SF-2026-ARXIV-2603-04851 | complete |
| SF-2026-ARXIV-2603-05087 | RP-fc60c33559a0bf95 | deep | arXiv:2603.05087v1 | SRC-ARXIV@arXiv:2603.05087v1 | https://arxiv.org/html/2603.05087v1#S4 — exact-v1 S4 — 4. System Design (Method) | https://arxiv.org/html/2603.05087v1#S6.SS1 — exact-v1 S6.SS1 — 6.1. Experimental Setup (Evaluation) | https://arxiv.org/html/2603.05087v1#S4.SS3.SSS4 — exact-v1 S4.SS3.SSS4 — 4.3.4. Two-layer Structure Discussion (Limitations) | https://arxiv.org/html/2603.05087v1#S5 — exact-v1 S5 — 5. Implementation (Artifact) | claim:SF-2026-ARXIV-2603-05087 | complete |
| SF-2026-ARXIV-2603-05147 | RP-69ff1c4ade24695c | deep | arXiv:2603.05147v1 | SRC-ARXIV@arXiv:2603.05147v1 | https://arxiv.org/html/2603.05147v1#S3 — exact-v1 S3 — III METHOD (Method) | https://arxiv.org/html/2603.05147v1#S4 — exact-v1 S4 — IV EXPERIMENTAL RESULTS (Evaluation) | https://arxiv.org/html/2603.05147v1#S6 — exact-v1 S6 — VI LIMITATIONS AND FUTURE WORKS (Limitations) | https://arxiv.org/html/2603.05147v1#S3.SS4 — exact-v1 S3.SS4 — III-D Training (Artifact) | claim:SF-2026-ARXIV-2603-05147 | complete |
| SF-2026-ARXIV-2603-05210 | RP-521db16c84dfc14f | deep | arXiv:2603.05210v1 | SRC-ARXIV@arXiv:2603.05210v1 | https://arxiv.org/html/2603.05210v1#S2 — exact-v1 S2 — 2 Method (Method) | https://arxiv.org/html/2603.05210v1#S3 — exact-v1 S3 — 3 Experiments (Evaluation) | https://arxiv.org/html/2603.05210v1#S5 — exact-v1 S5 — 5 Limitations (Limitations) | Not Disclosed — arXiv:2603.05210v1 exposes no dedicated Artifact / implementation section in the recovered exact-v1 body | claim:SF-2026-ARXIV-2603-05210 | complete |
| SF-2026-ARXIV-2603-05353 | RP-33221452c2d3bd5c | deep | arXiv:2603.05353v1 | SRC-ARXIV@arXiv:2603.05353v1 | https://arxiv.org/html/2603.05353v1#S4 — exact-v1 S4 — 4 Method (Method) | https://arxiv.org/html/2603.05353v1#S6 — exact-v1 S6 — 6 Experiment (Evaluation) | https://arxiv.org/html/2603.05353v1#S8 — exact-v1 S8 — 8 Discussion (Limitations) | https://arxiv.org/html/2603.05353v1#A2 — exact-v1 A2 — Appendix B More Implementation Details (Artifact) | claim:SF-2026-ARXIV-2603-05353 | complete |
| SF-2026-ARXIV-2603-05399 | RP-db9487e30fa2fe05 | deep | arXiv:2603.05399v1 | SRC-ARXIV@arXiv:2603.05399v1 | https://arxiv.org/html/2603.05399v1#S3 — exact-v1 S3 — 3 Methodology (Method) | https://arxiv.org/html/2603.05399v1#S4 — exact-v1 S4 — 4 Experiments (Evaluation) | https://arxiv.org/html/2603.05399v1#S6 — exact-v1 S6 — 6 Discussion (Limitations) | https://arxiv.org/html/2603.05399v1#S4 — exact-v1 S4 — 4 Experiments (Artifact) | claim:SF-2026-ARXIV-2603-05399 | complete |
| SF-2026-ARXIV-2603-04814 | RP-04dad415c0ba4fcb | deep | arXiv:2603.04814v1 | SRC-ARXIV@arXiv:2603.04814v1 | https://arxiv.org/html/2603.04814v1#S3 — exact-v1 S3 — 3 Methodology (Method) | https://arxiv.org/html/2603.04814v1#S4 — exact-v1 S4 — 4 Experiments and Results (Evaluation) | https://arxiv.org/html/2603.04814v1#S5.SS2 — exact-v1 S5.SS2 — 5.2 Limitations (Limitations) | Not Disclosed — arXiv:2603.04814v1 exposes no dedicated Artifact / implementation section in the recovered exact-v1 body | claim:SF-2026-ARXIV-2603-04814 | complete |
| SF-2026-ARXIV-2603-04896 | RP-80a575315743bc3e | deep | arXiv:2603.04896v1 | SRC-ARXIV@arXiv:2603.04896v1 | https://arxiv.org/html/2603.04896v1#S3 — exact-v1 S3 — 3 Method (Method) | https://arxiv.org/html/2603.04896v1#S4 — exact-v1 S4 — 4 Experiment (Evaluation) | https://arxiv.org/html/2603.04896v1#S5 — exact-v1 S5 — 5 Conclusion (Limitations) | https://arxiv.org/html/2603.04896v1#S4.SS1 — exact-v1 S4.SS1 — 4.1 Implementation Details (Artifact) | claim:SF-2026-ARXIV-2603-04896 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2603-04402:start -->
#### SearchGym: A Modular Infrastructure for Cross-Platform Benchmarking and Hybrid Search Orchestration

问题与 changed constraint：搜索 Agent benchmark 分散在不同平台、接口和 retriever，结果不可归因于策略还是环境。

旧路径为何合理：在该约束未出现、规模较小或 workload 更稳定时，论文所比较的旧路径仍以更少状态、更短控制链和更成熟实现提供合理基线；不能因本论文出现而静默覆盖。

机制、state/data/control owner：SearchGym 提供模块化平台 adapter、统一 trace 和 hybrid search orchestration，使跨平台实验共享 contract。 对应 exact-v1 `S3 — 3 The SearchGym Architecture`；该机制由 `PLATFORM-EVALUATION-SYSTEM` 承载。原文定位摘录仅作核对：3 The SearchGym Architecture The core contribution of SearchGym is a formal separation between data representation, embedding strategies, and retrieval orchestration. This allows for a "config-driven" approach where the system is defined by its architecture rather than its implementation details. 3.1 Dataset: Decoupling Schema from Instance In SearchGym, a Dataset is the foundational layer. Unlike traditional systems that treat a corpus as a flat table, we define a dataset through two distinct lenses: • Channels: M

Evaluation contract：benchmark 只证明纳入平台和任务中的比较；不证明平台 API 漂移后仍可复现。 exact-v1 定位为 `S5 — 5 Experiments`；用于核对的原文摘录：5 Experiments We perform benchmark experiments to assess the robustness of the system. Currently, evaluation is performed holistically, but more fine-grained per-subset testing will be essential for diagnosing partial system failures. Given our limited computational and human resources, building a comprehensive custom benchmark from scratch is impractical. Instead, we adopt a "pretraining–finetuning" philosophy at the system level. We first evaluate on established English-language academic retrieval benchmarks [13]

证明与未证明：证据只支持上述 paper-specific workload 内的机制/测量关系；不支持把作者结果外推为其他模型、数据、硬件、精度、长度、batch、并发或 production SLO 的通用结论。

Trade-off、failure 与共存边界：可比性换来 adapter 维护和最小公分母抽象；单平台优化可直接使用原生接口。 反证/限制定位为 `S7 — 7 Conclusion: The Gym as a Laboratory`；用于核对的原文摘录：7 Conclusion: The Gym as a Laboratory SearchGym was conceived to bridge the gap between static academic benchmarks and the dynamic requirements of production-level RAG systems. By introducing a modular architecture centered on the Dataset, Vector Set, and App abstractions, we have moved away from rigid, one-size-fits-all pipelines toward a flexible design space. The strength of this platform lies in its dual nature.

Artifact / implementation：exact-v1 `S4 — 4 Config-Driven System Synthesis`；公开范围摘录：4 Config-Driven System Synthesis The most distinctive feature of SearchGym is its Compositional Config Algebra. Instead of manually instantiating classes, the entire system—from data loaders to routing logic—is generated from a hierarchical, typed configuration file 4. • Reproducibility: Every experiment is defined by a single config hash, ensuring that a sp。未公开的代码、commit、部署配置或复现实验不得由论文叙事反推。

<!-- claim:SF-2026-ARXIV-2603-04402:start -->只接受 arXiv:2603.04402v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。<!-- claim:SF-2026-ARXIV-2603-04402:end -->

Books Comparison：已读 `PLATFORM-EVALUATION-SYSTEM` 的 `books/part-06-ai-infrastructure/66-evaluation-system.md#从答案评分到可执行证据 (line 936)` 及相邻 `books/part-06-ai-infrastructure/65-kai-scheduler.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/67-monitoring.md#本章要回答的问题 (line 10)`；现有命题为“- `SF-2026-ARXIV-2606-21869` — primary `arXiv:2606.21869v1`；exact-v1 URL=`https://arxiv.org/html/2606.21869v1`；Method=`https://arxiv.org/html/2606.21869v1 — §3 Preliminaries — Energy Consumption and Measurement; Multilingual Dataset`；Evaluation=`https://arxiv.org/html/2606.21869v1 — §4 Results and Analysis — Common Setup; §4.1–§4.4; Appendix B Experimental Setups`；Non-proof=`https://arxiv.org/html/2606.21869v1 — §6 Conclusion; Environmental impact of this study; Translation quality and representation; Recommendatio”。Decision=`No Change — Existing Coverage`；该 author-side 判断仍待fresh-context Books reviewer，Integrate 项只进入日期队列。
<!-- review:SF-2026-ARXIV-2603-04402:end -->

<!-- review:SF-2026-ARXIV-2603-04424:start -->
#### When Scaling Fails: Network and Fabric Effects on Distributed GPU Training Performance

问题与 changed constraint：分布式训练扩容若只看 GPU 数，会忽略 fabric topology、oversubscription 和 collective contention，出现 scaling 反转。

旧路径为何合理：在该约束未出现、规模较小或 workload 更稳定时，论文所比较的旧路径仍以更少状态、更短控制链和更成熟实现提供合理基线；不能因本论文出现而静默覆盖。

机制、state/data/control owner：论文把网络/fabric 事件与训练 step/collective trace 对齐，定位何时 topology 成为训练 owner 约束。 对应 exact-v1 `S4.SS2 — 4.2 System Architecture Overview`；该机制由 `TRAIN-DISTRIBUTED-TRAINING` 承载。原文定位摘录仅作核对：4.2 System Architecture Overview Figure presents a high-level overview of the system design. The architecture introduces lightweight coordination controls and measurement hooks around the existing training execution path. The design consists of three logical layers: Execution Layer: Includes the standard forward pass, backward pass, and gradient computation performed by each GPU. No changes are made to model execution or kernel scheduling at this layer. Communication Layer: Wraps collective operations used for grad

Evaluation contract：结果只覆盖所测集群、模型和 collective；不证明同一阈值适用于其他 fabric。 exact-v1 定位为 `S6.SS1 — 6.1 Experimental Setup`；用于核对的原文摘录：6.1 Experimental Setup Experiments were conducted on multiple GPU clusters representative of modern training environments. Each cluster consists of multi-GPU nodes interconnected via a high-bandwidth network fabric. Nodes are configured with homogeneous GPU models and identical software stacks to isolate infrastructure effects from application-level variability. Training workloads follow a data-parallel execution model using synchronous gradient aggregation. Unless otherwise stated, all experiments use identical mo

证明与未证明：证据只支持上述 paper-specific workload 内的机制/测量关系；不支持把作者结果外推为其他模型、数据、硬件、精度、长度、batch、并发或 production SLO 的通用结论。

Trade-off、failure 与共存边界：网络感知 placement/并行提高效率但降低可调度池和容错弹性；小规模或均匀网络仍可简单扩容。 反证/限制定位为 `S7 — 7 Discussion`；用于核对的原文摘录：7 Discussion The results presented in this study highlight a fundamental gap between how distributed training systems are commonly reasoned about and how they behave in practice at scale. While modern machine learning frameworks provide strong abstractions that simplify distributed execution, these abstractions often obscure infrastructure-level effects that materially influence performance and reliability. A key obs

Artifact / implementation：exact-v1 `S5 — 5 Implementation`；公开范围摘录：5 Implementation This section describes how the proposed coordination mechanisms were implemented in a practical distributed training environment. The goal of the implementation is not to replace existing communication libraries or frameworks, but to introduce lightweight instrumentation and control that can coexist with standard training stacks and be incre。未公开的代码、commit、部署配置或复现实验不得由论文叙事反推。

<!-- claim:SF-2026-ARXIV-2603-04424:start -->只接受 arXiv:2603.04424v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。<!-- claim:SF-2026-ARXIV-2603-04424:end -->

Books Comparison：已读 `TRAIN-DISTRIBUTED-TRAINING` 的 `books/part-04-training-system/36-distributed-training.md#从本机协作到分布式执行 (line 65)` 及相邻 `books/part-04-training-system/35-checkpoint.md#本章要回答的问题 (line 10); books/part-04-training-system/37-tensor-parallel.md#本章要回答的问题 (line 10)`；现有命题为“MPI 把问题提升为并行程序的执行模型。它定义 process/rank、communicator、point-to-point、collective、topology、one-sided communication 等语义，使程序描述“哪些 participants 对哪些数据共同完成什么操作”。MPI implementation 可以选择 shared memory、network transport 或 accelerator-aware path；能否直接处理 device buffer 取决于具体 implementation 和构建能力，不能从 MPI 标准名称本身推出。”。Decision=`No Change — Existing Coverage`；该 author-side 判断仍待fresh-context Books reviewer，Integrate 项只进入日期队列。
<!-- review:SF-2026-ARXIV-2603-04424:end -->

<!-- review:SF-2026-ARXIV-2603-04428:start -->
#### Agent Memory Below the Prompt: Persistent Q4 KV Cache for Multi-Agent LLM Inference on Edge Devices

问题与 changed constraint：Edge multi-agent 反复重建 prompt/KV 会浪费延迟和能耗，普通 memory store 不能直接复用解码状态。

旧路径为何合理：在该约束未出现、规模较小或 workload 更稳定时，论文所比较的旧路径仍以更少状态、更短控制链和更成熟实现提供合理基线；不能因本论文出现而静默覆盖。

机制、state/data/control owner：论文将持久 Q4 KV 作为 prompt 下方的 agent memory，并管理跨 agent/session 的缓存 identity。 对应 exact-v1 `A5 — Appendix E Perplexity Methodology`；该机制由 `AGENT-MEMORY` 承载。原文定位摘录仅作核对：Appendix E Perplexity Methodology Section 4.8 reports perplexity measured with actual QuantizedKVCache objects. The methodology uses WikiText-2 text in 512-token sliding windows (256-token stride), evaluating 7,935 tokens per model. Both FP16 baseline and Q4 caches use identical model weights (4-bit quantized via mlx-lm). The Q4 KV cache uses group size 64, matching the production pipeline. Prior work on Q4 KV cache quality: KIVI Liu et al. [2024b] shows negligible downstream task degradation at 4 bits with per-cha

Evaluation contract：收益只对作者模型、edge device、Q4 与复用模式；不证明缓存跨权重/位置变化仍有效。 exact-v1 定位为 `S4 — 4 Evaluation`；用于核对的原文摘录：4 Evaluation 4.1 Setup Hardware. Apple MacBook Pro M4 Pro (MX2E3LL/A), 24 GB unified LPDDR5X, 273 GB/s bandwidth. Models. Gemma 3 12B Instruct (48 attention layers, 8 KV heads, head dim 256, GQA with 16 query heads). DeepSeek-Coder-V2-Lite 16B Instruct (27 layers, 16 KV heads, K=192/V=128, MLA). Llama 3.1 8B Instruct (32 layers, 8 KV heads, head dim 128, standard GQA). All at Q4 weights with Q4 KV cache. Methodology. Each configuration is measured 6 times; we report medians. Temperature 0.0 (greedy decoding, determ

证明与未证明：证据只支持上述 paper-specific workload 内的机制/测量关系；不支持把作者结果外推为其他模型、数据、硬件、精度、长度、batch、并发或 production SLO 的通用结论。

Trade-off、failure 与共存边界：低延迟换来 stale state、量化误差和隔离风险；低复用或模型频繁升级时应重建 KV。 反证/限制定位为 `S5.SS6 — 5.6 Limitations`；用于核对的原文摘录：5.6 Limitations Single device. All agents share one device. Multi-device extension would require cache transfer over Thunderbolt or network interconnects. Q4 quality impact. Section 4.8 measures perplexity with actual Q4 KV caches, showing 0.10 PPL (0.7%) for Gemma, 0.12 PPL (2.8%) for Llama, and 0.19 PPL (3.0%) for DeepSeek. These measurements use 512-token evaluation windows, which do not exercise Gemma’s sliding-w

Artifact / implementation：exact-v1 `Not Disclosed — arXiv:2603.04428v1 exposes no dedicated Artifact / implementation section in the recovered exact-v1 body`；公开范围摘录：Not Disclosed。未公开的代码、commit、部署配置或复现实验不得由论文叙事反推。

<!-- claim:SF-2026-ARXIV-2603-04428:start -->只接受 arXiv:2603.04428v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。<!-- claim:SF-2026-ARXIV-2603-04428:end -->

Books Comparison：已读 `AGENT-MEMORY` 的 `books/part-07-agent/77-memory.md#本章在知识树中的位置 (line 1191)` 及相邻 `books/part-07-agent/76-rag.md#本章要回答的问题 (line 10); books/part-07-agent/78-tool-calling.md#本章要回答的问题 (line 10)`；现有命题为“Prompt、Context、RAG、Memory 共同构成 Agent 的 information state。下一章引入 action：Tool Calling 如何把模型输出转换为对外部环境的 typed proposal，并由平台决定是否执行。”。Decision=`No Change — Existing Coverage`；该 author-side 判断仍待fresh-context Books reviewer，Integrate 项只进入日期队列。
<!-- review:SF-2026-ARXIV-2603-04428:end -->

<!-- review:SF-2026-ARXIV-2603-04443:start -->
#### AMV-L: Lifecycle-Managed Agent Memory for Tail-Latency Control in Long-Running LLM Systems

问题与 changed constraint：长运行 Agent memory 会无限增长并造成 tail latency；只按容量 eviction 不能表达创建、热度、压缩和淘汰阶段。

旧路径为何合理：在该约束未出现、规模较小或 workload 更稳定时，论文所比较的旧路径仍以更少状态、更短控制链和更成熟实现提供合理基线；不能因本论文出现而静默覆盖。

机制、state/data/control owner：AMV-L 用 lifecycle manager 管理 memory 的写入、分层、压缩和回收，以尾延迟 SLO 驱动状态迁移。 对应 exact-v1 `PDF page 3; exact heading 3. Design Goals 4. AMV-L Overview`；该机制由 `AGENT-MEMORY` 承载。原文定位摘录仅作核对：3. Design Goals 4. AMV-L Overview AMV-L is designed to replace age-based retention with AMV-L (Adaptive Memory Value Lifecycle) manages a lifecycle policy that explicitly controls the agent memory as a working-set control mechanism. The computational footprint of memory. The design is system assigns each memory item a continuously guided by four goals. updated scalar value that estimates utility and uses that G1. Bound request-path memory cost independently of value to determine two outcomes: the item’s lifecycle t

Evaluation contract：结果只覆盖作者 workload、层级和硬件；不证明所有 memory value 都可由访问热度代表。 exact-v1 定位为 `PDF page 7; exact heading 9.1 Experimental protocol`；用于核对的原文摘录：9.1 Experimental protocol construction. The warm-tier budget 𝑘is request- configurable with a small default. Warm selection Each experiment is executed in two sequential runs over supports two modes. In random mode, it samples the same workload trace: uniformly without replacement from a bounded warm 1. TTL run: the memory store is cleared and the pool. In recency mode, it selects warm candidates by system runs with TTL-based retention. sorting on last-use time with a fallback to creation time. These modes bound th

证明与未证明：证据只支持上述 paper-specific workload 内的机制/测量关系；不支持把作者结果外推为其他模型、数据、硬件、精度、长度、batch、并发或 production SLO 的通用结论。

Trade-off、failure 与共存边界：控制 tail latency 但增加预测、迁移和一致性；小 memory 或无 SLO 场景可直接保留。 反证/限制定位为 `PDF page 13; exact heading 10.4.6 Limitations and extensions Communications Societies (IEEE Cat.`；用于核对的原文摘录：10.4.6 Limitations and extensions Communications Societies (IEEE Cat. Our LRU baseline is purely recency-based. It does not No.03CH37428) vol. 1 417–426 vol.1 (2003). incorporate semantic utility signals, nor does it provide 5. Westhäußer, R., Minker, W. & Zepf, S. explicit mechanisms to preserve long-lived high-utility Enabling personalized long-term interactions in items under phase shifts. Hybrid policies that com

Artifact / implementation：exact-v1 `PDF page 8; exact heading 9.6 Reproducibility`；公开范围摘录：9.6 Reproducibility LRU achieves slightly higher throughput than AMV-L We record all configuration parameters, including TTL (38.2 vs 37.0 requests/s) and slightly lower median and window, tier thresholds, hysteresis margins, decay rates, p95 latency (154 vs 194 ms at p50, 922 vs 950 ms at reinforcement constants, retrieval budgets, and prompt- p95). However。未公开的代码、commit、部署配置或复现实验不得由论文叙事反推。

<!-- claim:SF-2026-ARXIV-2603-04443:start -->只接受 arXiv:2603.04443v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。<!-- claim:SF-2026-ARXIV-2603-04443:end -->

Books Comparison：已读 `AGENT-MEMORY` 的 `books/part-07-agent/77-memory.md#Memory Write 是高风险决策 (line 122)` 及相邻 `books/part-07-agent/76-rag.md#本章要回答的问题 (line 10); books/part-07-agent/78-tool-calling.md#本章要回答的问题 (line 10)`；现有命题为“只用最终 QA reward 训练 memory policy 成本低，也适合短链路、固定 schema 和容易人工检查的任务；但它不能回答某段中间 memory content 是否真正帮助了最终答案。一个实验性分支是固定 retrieval/answer interface，对 memory token 或 span 做 masking/counterfactual scoring，把对 answer score 的变化映射为 local process reward，再与 global outcome reward 合并。它把“这次答对了”推进为“哪些被写入的内容可能贡献了这次答案”，从而给 admission、update、compress 与 discard 更稠密的学习信号。”。Decision=`No Change — Existing Coverage`；该 author-side 判断仍待fresh-context Books reviewer，Integrate 项只进入日期队列。
<!-- review:SF-2026-ARXIV-2603-04443:end -->

<!-- review:SF-2026-ARXIV-2603-04444:start -->
#### vLLM Semantic Router: Signal Driven Decision Routing for Mixture-of-Modality Models

问题与 changed constraint：Mixture-of-Modality 请求对模型、encoder 和资源需求不同，静态 endpoint routing 无法从输入信号匹配执行路径。

旧路径为何合理：在该约束未出现、规模较小或 workload 更稳定时，论文所比较的旧路径仍以更少状态、更短控制链和更成熟实现提供合理基线；不能因本论文出现而静默覆盖。

机制、state/data/control owner：vLLM Semantic Router 从请求语义/模态信号选择后端与策略，把 routing decision 置于 serving admission。 对应 exact-v1 `S8.SS5 — 8.5 Training Methodology`；该机制由 `INFER-SCHEDULING` 承载。原文定位摘录仅作核对：8.5 Training Methodology All LoRA adapters are trained using PEFT [24] with the following protocol: • Base model: ModernBERT or mmBERT-32K (for long-context tasks). • Adapter configuration: Rank , applied to query and value projection matrices. • Training: Task-specific datasets with standard cross-entropy loss. • Export: Both LoRA-only (separate adapter files for hot-swapping) and merged (single model file for simplified deployment) formats. The modality classifier, for instance, is trained on a balanced mixture o

Evaluation contract：结果只对配置的模型池、信号和 traffic；不证明 router 在分布漂移下保持质量或公平。 exact-v1 定位为 `S15 — 15 Evaluation`；用于核对的原文摘录：15 Evaluation We evaluate the routing system across three dimensions: signal extraction efficiency, LoRA multi-task scaling, and end-to-end routing correctness. 15.1 Signal Extraction Latency Table 4 reports median and p99 latencies for each signal type on an NVIDIA A100 GPU with ModernBERT base model. Table 4: Signal extraction latency by type Signal Type Median p99 Requires ML Keyword ms ms No Context ms ms No Language ms ms No Authorization ms ms No Embedding ms ms Yes Domain ms ms Yes Fact-check ms ms Yes Modal

证明与未证明：证据只支持上述 paper-specific workload 内的机制/测量关系；不支持把作者结果外推为其他模型、数据、硬件、精度、长度、batch、并发或 production SLO 的通用结论。

Trade-off、failure 与共存边界：提高匹配效率但增加分类延迟、错误路由和 fallback；单模型服务无需语义 router。 反证/限制定位为 `S17 — 17 Conclusion`；用于核对的原文摘录：17 Conclusion We have presented vLLM Semantic Router, a signal-driven decision routing system for Mixture-of-Modality model deployments. The central contribution is composable signal orchestration: the three-layer architecture—signal extraction, Boolean decision evaluation, per-decision plugin chains—enables diverse deployment scenarios to be expressed as different configurations over the same framework, without code

Artifact / implementation：exact-v1 `S14 — 14 Deployment`；公开范围摘录：14 Deployment We describe the deployment architecture that enables the routing system to operate from single-node development to production Kubernetes [34] clusters. 14.1 Deployment Modes Local development. A single command (pip install vllm-sr && vllm-sr serve) bootstraps the complete stack: router, Envoy proxy, and dashboard. This lowers the barrier to exp。未公开的代码、commit、部署配置或复现实验不得由论文叙事反推。

<!-- claim:SF-2026-ARXIV-2603-04444:start -->只接受 arXiv:2603.04444v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。<!-- claim:SF-2026-ARXIV-2603-04444:end -->

Books Comparison：已读 `INFER-SCHEDULING` 的 `books/part-05-inference-system/56-inference-scheduling.md#Routing、Placement 与 Autoscaling (line 285)` 及相邻 `books/part-05-inference-system/55-pd-disaggregation.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/57-what-is-ai-platform.md#本章要回答的问题 (line 10)`；现有命题为“vPod 类抽象可以绑定 NPU generation、数量、interconnect、memory、parallel layout 与 compiler profile，再用经校准的 roofline/modeling 筛选满足 SLO 的 Pareto configurations。routing 选择现成 replica，placement 选择 contract，autoscaling 决定何时 materialize/retire；三者共享 workload estimate，却不能合并为一个瞬时 score。scale-up readiness、model loading 和 migration delay 必须进入 admission。”。Decision=`No Change — Existing Coverage`；该 author-side 判断仍待fresh-context Books reviewer，Integrate 项只进入日期队列。
<!-- review:SF-2026-ARXIV-2603-04444:end -->

<!-- review:SF-2026-ARXIV-2603-04448:start -->
#### SkillNet: Create, Evaluate, and Connect AI Skills

问题与 changed constraint：Skill registry 只存文件无法回答能力重复、质量、关系和可组合性，生态扩大后检索会退化。

旧路径为何合理：在该约束未出现、规模较小或 workload 更稳定时，论文所比较的旧路径仍以更少状态、更短控制链和更成熟实现提供合理基线；不能因本论文出现而静默覆盖。

机制、state/data/control owner：SkillNet 从经验抽象 Skill，建立 ontology，过滤合并并评估连接，使 Skill 成为有版本和关系的资产。 对应 exact-v1 `S3.SS1 — 3.1 Overview`；该机制由 `AGENT-PLATFORM` 承载。原文定位摘录仅作核对：3.1 Overview Figure 2: End-to-end Pipeline of SkillNet. SkillNet transforms heterogeneous user inputs and open internet resources into executable skills through automated skill creation and multi-dimensional evaluation, and organizes high-quality skills into a structured network to support search, download, analysis, and contribution. Figure 2 illustrates the overall architecture of SkillNet, which systematically creates, evaluates, and organizes high-quality skills for agent systems. SkillNet is designed to transf

Evaluation contract：定量与应用场景只覆盖作者数据和 evaluator；不证明自动抽象出的 Skill 在任意 Agent 中可移植。 exact-v1 定位为 `S4 — 4 Quantitative Evaluation`；用于核对的原文摘录：4 Quantitative Evaluation 4.1 Settings To quantitatively assess the effectiveness of SkillNet, we conduct experiments across three text-based simulated environments. ALFWorld [29] provides an embodied household environment, requiring agents to navigate and manipulate objects to complete daily tasks; WebShop [30] simulates realistic online shopping scenarios, where agents perform product search, comparison, and purchasing under specified constraints; and ScienceWorld [31] presents a virtual scientific laboratory in

证明与未证明：证据只支持上述 paper-specific workload 内的机制/测量关系；不支持把作者结果外推为其他模型、数据、硬件、精度、长度、batch、并发或 production SLO 的通用结论。

Trade-off、failure 与共存边界：生态治理换来 ontology/evaluation 成本和错误合并风险；小型人工 curated Skill 集仍更可控。 反证/限制定位为 `S8 — 8 Limitations`；用于核对的原文摘录：8 Limitations There remain several limitations in the present work. First, the coverage of skills is inevitably incomplete. Many capabilities in private or specialized domains cannot be incorporated, while low-frequency or highly tacit abilities are difficult to capture and consolidate within the repository, particularly when they resist explicit linguistic description. Second, the quality of self-constructed skills

Artifact / implementation：exact-v1 `S3.SS6 — 3.6 Open Resources`；公开范围摘录：3.6 Open Resources SkillNet provides a comprehensive open infrastructure for creating, evaluating, and organizing AI skills at scale. This includes a large-scale skill repository, a front-end website, an open access API, and a versatile Python toolkit (skillnet-ai), forming a unified ecosystem for skill management and utilization. The front-end website allow。未公开的代码、commit、部署配置或复现实验不得由论文叙事反推。

<!-- claim:SF-2026-ARXIV-2603-04448:start -->只接受 arXiv:2603.04448v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。<!-- claim:SF-2026-ARXIV-2603-04448:end -->

Books Comparison：已读 `AGENT-PLATFORM` 的 `books/part-07-agent/84-agent-platform.md#本章要回答的问题 (line 14)` 及相邻 `books/part-07-agent/83-mcp.md#本章要回答的问题 (line 10)`；现有命题为“本章的核心判断是：**Agent Platform 是 AI Platform 对有状态行动循环的扩展。它统一 Agent definition、run、context、memory、tools、workflow、evaluation 与 policy，但复用 Part VI 的 identity、resource、evidence、cost、tenancy、security 和 recovery substrate。**”。Decision=`No Change — Existing Coverage`；该 author-side 判断仍待fresh-context Books reviewer，Integrate 项只进入日期队列。
<!-- review:SF-2026-ARXIV-2603-04448:end -->

<!-- review:SF-2026-ARXIV-2603-04459:start -->
#### Benchmark of Benchmarks: Unpacking Influence and Code Repository Quality in LLM Safety Benchmarks

问题与 changed constraint：安全 benchmark 的引用影响力与代码仓库质量不等于测量有效性，但实践中常被当作可信代理。

旧路径为何合理：在该约束未出现、规模较小或 workload 更稳定时，论文所比较的旧路径仍以更少状态、更短控制链和更成熟实现提供合理基线；不能因本论文出现而静默覆盖。

机制、state/data/control owner：论文同时审计 benchmark influence 与 repository 可运行/维护属性，分离社会采用和 artifact quality。 对应 exact-v1 `A12.SS1 — Selection of Correlation Analysis Method`；该机制由 `PLATFORM-EVALUATION-SYSTEM` 承载。原文定位摘录仅作核对：Selection of Correlation Analysis Method The total number of samples in the Benchmark dataset is relatively limited. In our study, we included all relevant benchmark works that we retrieved, with a total size of 31. According to statistical guidelines, approximately ten observations per predictor are needed to obtain stable estimates in regression [107, 90, 78]. With eight independent variables, a size of 31 provides insufficient degrees of freedom for a robust multivariate analysis. A Multiple Linear Regression mo

Evaluation contract：结果证明所采样 benchmark 的差异；不证明高仓库质量意味着安全 construct validity。 exact-v1 定位为 `A9 — Appendix I Descriptive Statistical Analysis of Influence Evaluation`；用于核对的原文摘录：Appendix I Descriptive Statistical Analysis of Influence Evaluation (a) All. (b) Prompt injection. (c) Jailbreak. (d) Hallucination. Figure 5: Average values of five influence-related metrics on benchmark and non-benchmark papers. The average values of five influence-related metrics are presented in Figure 5. When considering all papers, we find that the average values of benchmark papers lag behind those of non-benchmark papers across all five influence-related metrics. Detailedly, on the metrics related to the ac

证明与未证明：证据只支持上述 paper-specific workload 内的机制/测量关系；不支持把作者结果外推为其他模型、数据、硬件、精度、长度、batch、并发或 production SLO 的通用结论。

Trade-off、failure 与共存边界：多维审计提高选择依据但增加维护与主观规则；早期探索可使用较轻清单，release gate 需更严格。 反证/限制定位为 `S8 — Discussion and Limitation`；用于核对的原文摘录：Discussion and Limitation Discussion Open Challenges. Some of the benchmark deficiencies mentioned may be inherently unsolvable. The LLM field evolves quickly, with frequent updates to popular libraries like vLLM [119], leading to structural changes and compatibility issues. Maintaining benchmark repositories requires continuous tracking, but this is difficult due to short-term academic funding and contributors’ shif

Artifact / implementation：exact-v1 `Not Disclosed — arXiv:2603.04459v1 exposes no dedicated Artifact / implementation section in the recovered exact-v1 body`；公开范围摘录：Not Disclosed。未公开的代码、commit、部署配置或复现实验不得由论文叙事反推。

<!-- claim:SF-2026-ARXIV-2603-04459:start -->只接受 arXiv:2603.04459v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。<!-- claim:SF-2026-ARXIV-2603-04459:end -->

Books Comparison：已读 `PLATFORM-EVALUATION-SYSTEM` 的 `books/part-06-ai-infrastructure/66-evaluation-system.md#从答案评分到可执行证据 (line 936)` 及相邻 `books/part-06-ai-infrastructure/65-kai-scheduler.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/67-monitoring.md#本章要回答的问题 (line 10)`；现有命题为“- `SF-2026-ARXIV-2606-21869` — primary `arXiv:2606.21869v1`；exact-v1 URL=`https://arxiv.org/html/2606.21869v1`；Method=`https://arxiv.org/html/2606.21869v1 — §3 Preliminaries — Energy Consumption and Measurement; Multilingual Dataset`；Evaluation=`https://arxiv.org/html/2606.21869v1 — §4 Results and Analysis — Common Setup; §4.1–§4.4; Appendix B Experimental Setups`；Non-proof=`https://arxiv.org/html/2606.21869v1 — §6 Conclusion; Environmental impact of this study; Translation quality and representation; Recommendatio”。Decision=`No Change — Existing Coverage`；该 author-side 判断仍待fresh-context Books reviewer，Integrate 项只进入日期队列。
<!-- review:SF-2026-ARXIV-2603-04459:end -->

<!-- review:SF-2026-ARXIV-2603-04460:start -->
#### VSPrefill: Vertical-Slash Sparse Attention with Lightweight Indexing for Long-Context Prefilling

问题与 changed constraint：长上下文 prefill 的全注意力成本高，通用稀疏模式又可能错过垂直/斜向长程依赖。

旧路径为何合理：在该约束未出现、规模较小或 workload 更稳定时，论文所比较的旧路径仍以更少状态、更短控制链和更成熟实现提供合理基线；不能因本论文出现而静默覆盖。

机制、state/data/control owner：VSPrefill 用 vertical-slash sparse pattern 与轻量索引选择 key block，专门优化 prefill 数据流。 对应 exact-v1 `S4 — 4 Method`；该机制由 `INFER-PREFILL` 承载。原文定位摘录仅作核对：4 Method This section presents VSPrefill, a lightweight-training sparse attention mechanism that predicts context-aware vertical-slash patterns with favorable computational efficiency. Although existing approaches such as FlexPrefill (Lai et al., 2025) and Sample Attention (Zhu et al., 2025) implicitly exploit vertical-slash structures through query sampling, they face a trade-off: single-point sampling incurs modest overhead yet fails to capture global patterns, whereas multi-point sampling reduces estimation vari

Evaluation contract：速度/质量只属于作者模型、长度、GPU 和 pattern；不证明所有任务注意力都呈该结构。 exact-v1 定位为 `S5 — 5 Experiments`；用于核对的原文摘录：5 Experiments We evaluate VSPrefill against state-of-the-art baselines to assess its performance in long-context scenarios. We first detail our experimental setup, including model architectures, benchmark datasets, and baseline methods. Subsequently, we analyze the performance across diverse tasks, examining both the preservation of accuracy and the acceleration of inference under varying sequence lengths. 5.1 Experimental Setup Models We evaluate VSPrefill on two widely adopted open-source LLMs: Qwen3-4B-Instruct

证明与未证明：证据只支持上述 paper-specific workload 内的机制/测量关系；不支持把作者结果外推为其他模型、数据、硬件、精度、长度、batch、并发或 production SLO 的通用结论。

Trade-off、failure 与共存边界：减少计算但引入索引和漏依赖风险；短上下文或依赖稠密任务仍用 full attention。 反证/限制定位为 `S6 — 6 Conclusion and Future Work`；用于核对的原文摘录：6 Conclusion and Future Work This paper introduces VSPrefill, a lightweight sparse attention mechanism that exploits the vertical-slash structural pattern inherent in long-context attention to accelerate LLM inference while preserving fidelity. Our approach employs a compact VSIndexer network to predict context-aware vertical and slash patterns per KV group with minimal training overhead, keeping the backbone frozen.

Artifact / implementation：exact-v1 `S4.SS3.SSS0.Px2 — Fused attention kernel implementation`；公开范围摘录：Fused attention kernel implementation Implementing vertical-slash sparse attention efficiently presents non-trivial engineering challenges, as standard FlashAttention tiling strategies assume contiguous memory access patterns which are violated by the non-contiguous query-key pairs in our sparsity pattern, and naive index precomputation would incur prohibiti。未公开的代码、commit、部署配置或复现实验不得由论文叙事反推。

<!-- claim:SF-2026-ARXIV-2603-04460:start -->只接受 arXiv:2603.04460v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。<!-- claim:SF-2026-ARXIV-2603-04460:end -->

Books Comparison：已读 `INFER-PREFILL` 的 `books/part-05-inference-system/43-prefill.md#自检问题 (line 365)` 及相邻 `books/part-05-inference-system/42-what-happens-during-inference.md#本章要回答的问题 (line 10); books/part-05-inference-system/44-decode.md#本章要回答的问题 (line 10)`；现有命题为“10. Sparse Prefill 的 selection overhead 为什么必须进入 TTFT，而不能只比较 attention kernel？”。Decision=`No Change — Existing Coverage`；该 author-side 判断仍待fresh-context Books reviewer，Integrate 项只进入日期队列。
<!-- review:SF-2026-ARXIV-2603-04460:end -->

<!-- review:SF-2026-ARXIV-2603-04469:start -->
#### Cross-Layer Semantic Flow Reconstruction for Attack Detection in Agentic Systems

问题与 changed constraint：Agent 攻击可跨 prompt、memory、tool response 和 workflow state 传播，单点内容扫描无法重建控制流。

旧路径为何合理：在该约束未出现、规模较小或 workload 更稳定时，论文所比较的旧路径仍以更少状态、更短控制链和更成熟实现提供合理基线；不能因本论文出现而静默覆盖。

机制、state/data/control owner：Cross-Layer Semantic Flow Reconstruction 将跨层事件关联为 provenance graph，再依据语义流识别从不可信输入到敏感 action 的路径。 对应 exact-v1 `S4 — 4 Method`；该机制由 `PLATFORM-SECURITY` 承载。原文定位摘录仅作核对：4 Method As illustrated in Figure 2, MAScope comprises three interconnected modules: (1) a Data Collection Module that captures fine-grained interaction data between agents and system entities; (2) a Semantic Extracting & Flow Reconstruction Module that analyzes unstructured interaction logs to extract semantic primitives and synthesize execution flows; and (3) a Trajectory Scrutiny Module that audits these reconstructed paths to identify and detect latent attack vectors. 4.1 Data Collection in MAS Building upon th

Evaluation contract：结果只覆盖作者 trace schema、攻击和 evaluator；不能证明图缺边时仍能发现攻击。 exact-v1 定位为 `S5 — 5 Experiment`；用于核对的原文摘录：5 Experiment In this section, we conduct experimental evaluations to answer two research questions, namely, RQ1. To what extent can MAScope accurately extract sensitive entities and operational primitives from unstructured agent interactions? and RQ2. How effective is MAScope in reconstructing multi-stage behavioral trajectories and detecting compound attack vectors against benign baselines? Table 3: Sensitive Information Extraction Performance Comparison (Baseline vs. HSEC Optimization) Attack Type Gemini-3 HSEC (

证明与未证明：证据只支持上述 paper-specific workload 内的机制/测量关系；不支持把作者结果外推为其他模型、数据、硬件、精度、长度、batch、并发或 production SLO 的通用结论。

Trade-off、failure 与共存边界：跨层可见性提高检测能力但增加追踪、隐私和误报成本；无持久状态的窄工具链可使用局部 guard。 反证/限制定位为 `S6 — 6 Conclusion`；用于核对的原文摘录：6 Conclusion This paper addresses the critical security voids in MAS, where autonomous execution renders traditional input guardrails insufficient. We proposed MAScope, a novel framework that shifts the defensive paradigm to execution-aware analysis by reconstructing cross-agent semantic flows. By bridging the semantic gap between high-level agent intents and low-level kernel artifacts, our methodology effectively is

Artifact / implementation：exact-v1 `Not Disclosed — arXiv:2603.04469v1 exposes no dedicated Artifact / implementation section in the recovered exact-v1 body`；公开范围摘录：Not Disclosed。未公开的代码、commit、部署配置或复现实验不得由论文叙事反推。

<!-- claim:SF-2026-ARXIV-2603-04469:start -->只接受 arXiv:2603.04469v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。<!-- claim:SF-2026-ARXIV-2603-04469:end -->

Books Comparison：已读 `PLATFORM-SECURITY` 的 `books/part-06-ai-infrastructure/72-security.md#从“文本是否恶意”到“谁获得了行为控制权” (line 336)` 及相邻 `books/part-06-ai-infrastructure/71-multi-tenant.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/73-production-best-practice.md#本章要回答的问题 (line 10)`；现有命题为“逐条扫描 message 或只在最终 action 上做 policy check，在通信拓扑固定、传播链短时简单有效；当一个污染信号经 message、shared memory、delegation 与 tool result 多次改写后，单 channel 告警既无法说明起点，也无法判断哪个 Agent 正在放大影响。运行时可以维护带 revision 的 cross-channel influence graph：各 channel adapter 只提交 observation，causal monitor 关联传播路径并提出 suspect source / edge，security policy 仍独立决定隔离、降权或阻断，不能把统计 attribution 当作 authorization。”。Decision=`No Change — Existing Coverage`；该 author-side 判断仍待fresh-context Books reviewer，Integrate 项只进入日期队列。
<!-- review:SF-2026-ARXIV-2603-04469:end -->

<!-- review:SF-2026-ARXIV-2603-04797:start -->
#### Hardware-Software Co-design for 3D-DRAM-based LLM Serving Accelerator

问题与 changed constraint：LLM serving 的 KV/weight 带宽与容量使传统 HBM hierarchy 受限，3D-DRAM 需要软件共同决定映射。

旧路径为何合理：在该约束未出现、规模较小或 workload 更稳定时，论文所比较的旧路径仍以更少状态、更短控制链和更成熟实现提供合理基线；不能因本论文出现而静默覆盖。

机制、state/data/control owner：论文联合 3D-DRAM accelerator 与 serving dataflow/placement，按模型状态访问模式设计硬件。 对应 exact-v1 `S6.SS1 — VI-A Evaluation Methodology`；该机制由 `INFER-GPU-MEMORY` 承载。原文定位摘录仅作核对：VI-A Evaluation Methodology Benchmarks: As listed in Table II, we adopt OPT 66B [88], LLaMA3 70B [15], Mixtral 8×22B [34], Qwen3 30B-A3B [80], and DeepSeek 236B [12] for evaluation, which cover both dense and MoE models with varying attention arithmetic intensities. All models use FP16 data type. For decoding latency comparison, due to capacity constraints, we set max batch size and context length to (32, 4K) for OPT/DeepSeek models, and to (64, 16K) for the other models. For serving performance comparison, followi

Evaluation contract：性能来自作者模型/模拟或原型；不证明封装、热、成本和软件生态。 exact-v1 定位为 `S6 — VI Evaluation`；用于核对的原文摘录：VI Evaluation TABLE II: Model Configurations Used for Evaluation Model Layer (Hidden, Interm.) (Q head, KV head) Expert OPT 66B 64 (9216, 36864) (72, 72) – (Dense) LLaMA3 70B 80 (8192, 28672) (64, 8) – (Dense) Mixtral 8×22B 56 (6144, 16384) (48, 8) 8 experts, top-2 Qwen3 30B-A3B 48 (2048, 768) (32, 4) 128 experts, top-8 DeepSeek 236B 60 (5120, 1536) (128, 128-full/1-latent) 160 experts, top-8 VI-A Evaluation Methodology Benchmarks: As listed in Table II, we adopt OPT 66B [88], LLaMA3 70B [15], Mixtral 8×22B [34], Q

证明与未证明：证据只支持上述 paper-specific workload 内的机制/测量关系；不支持把作者结果外推为其他模型、数据、硬件、精度、长度、batch、并发或 production SLO 的通用结论。

Trade-off、failure 与共存边界：更高带宽/容量换来专用硬件与映射锁定；快速变化模型仍适合通用 GPU。 反证/限制定位为 `S2.SS4 — II-D Limitations of Serving-Oriented NMP Designs`；用于核对的原文摘录：II-D Limitations of Serving-Oriented NMP Designs Although existing LLM-serving-oriented NMP designshave reported better performance than centralized processors, they lack support for dynamic KV cache management and fine-grained attention computation mechanisms, limiting their efficiency for highly dynamic serving workloads: Limitation #1: Coarse-grained KV cache management. As summarized in Table I, existing NMP desi

Artifact / implementation：exact-v1 `S5 — V Helios System Design`；公开范围摘录：V Helios System Design V-A Spatially-Aware KV Cache Allocation Demand Analysis: HB-Device contains two load balance demands: (1) Compute/Storage load: It enforces a balanced distribution of attention workloads across all PEs on the HB-Device. For each PE, as discussed in Sec. IV-A, online softmax and partial sum accumulation can be efficiently overlapped by。未公开的代码、commit、部署配置或复现实验不得由论文叙事反推。

<!-- claim:SF-2026-ARXIV-2603-04797:start -->只接受 arXiv:2603.04797v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。<!-- claim:SF-2026-ARXIV-2603-04797:end -->

Books Comparison：已读 `INFER-GPU-MEMORY` 的 `books/part-05-inference-system/54-gpu-memory.md#三类缓解路径 (line 306)` 及相邻 `books/part-05-inference-system/53-kserve-llm.md#本章要回答的问题 (line 10); books/part-05-inference-system/55-pd-disaggregation.md#本章要回答的问题 (line 10)`；现有命题为“权重因此从静态 artifact 扩展为受策略控制的 runtime state，也新增 calibration drift、prompt-conditioned policy、CPU-GPU traffic、mixed kernel 和失败恢复问题。quality policy、tenant 与 request identity 必须进入 trace；严格可复现、精度预算固定或 transfer cost 高时，静态 weights 仍更安全。当前证据限于三种 MoE、作者 workload 与无生产 arrival/tail-SLO 的实验。”。Decision=`No Change — Existing Coverage`；该 author-side 判断仍待fresh-context Books reviewer，Integrate 项只进入日期队列。
<!-- review:SF-2026-ARXIV-2603-04797:end -->

<!-- review:SF-2026-ARXIV-2603-04902:start -->
#### AgentSCOPE: Evaluating Contextual Privacy Across Agentic Workflows

问题与 changed constraint：Agent workflow 的隐私风险取决于上下文目的、角色和信息流；仅检测 PII 无法判断传递是否合规。

旧路径为何合理：在该约束未出现、规模较小或 workload 更稳定时，论文所比较的旧路径仍以更少状态、更短控制链和更成熟实现提供合理基线；不能因本论文出现而静默覆盖。

机制、state/data/control owner：AgentSCOPE 用 Privacy Flow Graph 表示 actor、context 与 transmission，并据 contextual integrity 构造 benchmark。 对应 exact-v1 `S2 — 2 Privacy Flow Graph`；该机制由 `PLATFORM-SECURITY` 承载。原文定位摘录仅作核对：2 Privacy Flow Graph The Privacy Flow Graph (PFG) operationalizes Contextual Integrity by modeling an agentic workflow as a sequence of explicit information-transfer events between four principal actors: the user, the agent, external tools, and downstream recipients. Each edge in the graph represents a concrete transmission of information (e.g., user → agent prompt, agent → email tool query, tool → agent retrieval, agent → final output), and every edge is annotated using the five CI attributes: sender, recipient, s

Evaluation contract：实验揭示所测 agent/workflow 的 privacy failure；不证明 graph policy 覆盖所有法律或组织规范。 exact-v1 定位为 `S4 — 4 Experiments`；用于核对的原文摘录：4 Experiments We evaluate seven state-of-the-art agentic models from OpenAI and Anthropic on the AgentSCOPE benchmark, measuring both utility and privacy. Utility is measured using Task Success Rate (TSR), defined as the percentage of scenarios in which the agent successfully completes the intended task end-to-end. For privacy, we report three metrics. Leak Rate (LR) measures explicit privacy violations at the output boundary. Pipeline Violation Rate (PVR) measures inappropriate information flows at intermediate st

证明与未证明：证据只支持上述 paper-specific workload 内的机制/测量关系；不支持把作者结果外推为其他模型、数据、硬件、精度、长度、batch、并发或 production SLO 的通用结论。

Trade-off、failure 与共存边界：语义化隐私检查提高精度但需要政策建模和 provenance；简单数据脱敏仍适合明确字段。 反证/限制定位为 `S4.SS1 — 4.1 Discussion`；用于核对的原文摘录：4.1 Discussion Figure 3: (Top) Core privacy and utility metrics on AgentSCOPE: Performance of state-of-the-art agentic models from OpenAI (GPT-4o family, GPT-4.1, GPT-5) and Anthropic (Claude Haiku, Claude Opus-4.5, Claude Sonnet-4.5) evaluated using the Privacy Flow Graph (PFG) framework on the AgentSCOPE benchmark. (Middle) Output-only leakage vs. full-pipeline violations: Comparison of Leak Rate (LR) and Pipeline

Artifact / implementation：exact-v1 `S3 — 3 AgentSCOPE: A Contextual Integrity-focused Benchmark`；公开范围摘录：3 AgentSCOPE: A Contextual Integrity-focused Benchmark Evaluating privacy across the full pipeline requires scenarios where violations can plausibly arise at different stages and where ground truth is available at each boundary. Existing benchmarks do not provide this: PrivacyLens, the closest existing benchmark, annotates only the output level and provides。未公开的代码、commit、部署配置或复现实验不得由论文叙事反推。

<!-- claim:SF-2026-ARXIV-2603-04902:start -->只接受 arXiv:2603.04902v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。<!-- claim:SF-2026-ARXIV-2603-04902:end -->

Books Comparison：已读 `PLATFORM-SECURITY` 的 `books/part-06-ai-infrastructure/72-security.md#Supply-chain Integrity (line 538)` 及相邻 `books/part-06-ai-infrastructure/71-multi-tenant.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/73-production-best-practice.md#本章要回答的问题 (line 10)`；现有命题为“Artifact 签名和 final-output check 能证明加载对象或发现最终错误，却不能在不可信 pipeline stage 之间定位哪一段改写了状态。一个 challenge-response 分支是由 verifier 持有 versioned canary 与受信 reference activation，在 live fp16 执行时比较每个 shard 的 intermediate state，并按校准 noise envelope 输出 suspect evidence。”。Decision=`No Change — Existing Coverage`；该 author-side 判断仍待fresh-context Books reviewer，Integrate 项只进入日期队列。
<!-- review:SF-2026-ARXIV-2603-04902:end -->

<!-- review:SF-2026-ARXIV-2603-04910:start -->
#### VPWEM: Non-Markovian Visuomotor Policy with Working and Episodic Memory

问题与 changed constraint：VLA 的 Markov observation 难以处理遮挡、迟延和长期目标，单一短期 memory 不足。

旧路径为何合理：在该约束未出现、规模较小或 workload 更稳定时，论文所比较的旧路径仍以更少状态、更短控制链和更成熟实现提供合理基线；不能因本论文出现而静默覆盖。

机制、state/data/control owner：VPWEM 将 working 与 episodic memory 接入 visuomotor policy，使动作依赖近期状态和历史事件。 对应 exact-v1 `S4 — IV Method`；该机制由 `MULTIMODAL-EMBODIED-VLA` 承载。原文定位摘录仅作核对：IV Method The overview of our VPWEM framework is illustrated in Figure 2. In addition to using observations within the context window as working meory (Section IV-A), we leverage a contextual memory compressor to distill essential information from observation tokens that have fallen outside this window into fixed-size summary tokens (Section IV-B). The resulting short-term working memory and long-term episodic memory provide complementary conditioning signals that jointly guide the action generation process (Sectio

Evaluation contract：结果只覆盖作者 robot/task 和 memory design；不证明 episodic retrieval 在分布外可靠。 exact-v1 定位为 `S5 — V Experiments`；用于核对的原文摘录：V Experiments V-A Experimental Setup Fig. 3: Three benchmarks in our experiments. Benchmark. We evaluate our method across three benchmarks, as shown in Figure 3: • MIKASA (Memory-Intensive Skills Assessment Suite for Agents) [32]. We use two memory-intensive tabletop manipulation tasks, ShellGameTouch-v0 and RememberColor3-v0. The former requires the policy to memorize the position of the ball after some time being covered by the cups and then interact with the cup the ball is under, whereas the latter requires it

证明与未证明：证据只支持上述 paper-specific workload 内的机制/测量关系；不支持把作者结果外推为其他模型、数据、硬件、精度、长度、batch、并发或 production SLO 的通用结论。

Trade-off、failure 与共存边界：处理非 Markov 状态但增加 stale memory 和检索延迟；完全可观测短任务仍用无记忆 policy。 反证/限制定位为 `S6 — VI Conclusion`；用于核对的原文摘录：VI Conclusion We presented VPWEM, a non-Markovian visuomotor policy learning framework that leverages complementary working and episodic memory. By employing a learnable compressor that distills historical observations into a compact episodic memory, our approach efficiently exploits temporal information without incurring prohibitive computational or storage costs. Extensive evaluations demonstrate that VPWEM substan

Artifact / implementation：exact-v1 `S5.SS1 — V-A Experimental Setup`；公开范围摘录：V-A Experimental Setup Fig. 3: Three benchmarks in our experiments. Benchmark. We evaluate our method across three benchmarks, as shown in Figure 3: • MIKASA (Memory-Intensive Skills Assessment Suite for Agents) [32]. We use two memory-intensive tabletop manipulation tasks, ShellGameTouch-v0 and RememberColor3-v0. The former requires the policy to memorize t。未公开的代码、commit、部署配置或复现实验不得由论文叙事反推。

<!-- claim:SF-2026-ARXIV-2603-04910:start -->只接受 arXiv:2603.04910v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。<!-- claim:SF-2026-ARXIV-2603-04910:end -->

Books Comparison：已读 `MULTIMODAL-EMBODIED-VLA` 的 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#Latency 与 control frequency (line 329)` 及相邻 `books/part-03-multimodal-world-models/25-multimodal-world-models.md#本章要回答的问题 (line 10); books/part-04-training-system/27-data.md#本章要回答的问题 (line 10)`；现有命题为“快慢分层把状态与控制频率拆开：慢速 multimodal policy 生成 chunk 与高层 context，快速 causal action expert 读取 latency-aligned force memory，对尚未 commit 的动作做有界修正。初始化时保持原 policy 行为，在线 human correction 则必须带 observation、force、原 proposal 与最终 action provenance。低层 safety controller 继续拥有执行 authority，reactive expert 只拥有 proposal correction。”。Decision=`No Change — Existing Coverage`；该 author-side 判断仍待fresh-context Books reviewer，Integrate 项只进入日期队列。
<!-- review:SF-2026-ARXIV-2603-04910:end -->

<!-- review:SF-2026-ARXIV-2603-04981:start -->
#### Rethinking Representativeness and Diversity in Dynamic Data Selection

问题与 changed constraint：动态数据选择中，代表性与多样性会随模型和数据分布变化；一次性静态 subset 很快失效。

旧路径为何合理：在该约束未出现、规模较小或 workload 更稳定时，论文所比较的旧路径仍以更少状态、更短控制链和更成熟实现提供合理基线；不能因本论文出现而静默覆盖。

机制、state/data/control owner：论文重新定义/联合优化 representativeness 与 diversity，并按训练反馈更新选择。 对应 exact-v1 `S3 — 3 Method`；该机制由 `TRAIN-DATA` 承载。原文定位摘录仅作核对：3 Method 3.1 Problem Setup and Overview Let be a labeled dataset, where is an input instance and its label. We perform dynamic data selection once per epoch. At epoch , we construct a subset with selection ratio by ranking examples using a time-dependent score : (1) We rethink two core notions for scoring examples: representativeness and diversity. Representativeness is defined as weighted coverage of dataset-level common/high-frequency feature factors, moving beyond local geometric centrality. Diversity is treated

Evaluation contract：结果只对作者数据、模型和选择预算；不证明指标等价于长期泛化或公平。 exact-v1 定位为 `S4 — 4 Experiments`；用于核对的原文摘录：4 Experiments Table 1: Accuracy (%) comparison on CIFAR-10/100. Random∗ denotes dynamic random selection. The reported ratios denote the selection ratios. Ours is highlighted in grey. ✓ = Dynamic, ✗ = Static. Backbone Method Type CIFAR-10 (Selection Ratio) CIFAR-100 (Selection Ratio) 70% 30% 70% 30% ResNet-18 Random ✗ 94.6↓1.5 90.2↓5.9 73.8↓4.9 69.7↓9.0 GraNd-4 (Paul et al., 2021) ✗ 95.3↓0.8 91.2↓4.9 74.6↓3.6 68.8↓9.4 MoDS (Xia et al., 2023) ✗ 93.9↓2.2 90.6↓5.5 74.6↓3.6 65.3↓12.9 MoSo (Tan et al., 2023) ✗ 95.3↓0.8

证明与未证明：证据只支持上述 paper-specific workload 内的机制/测量关系；不支持把作者结果外推为其他模型、数据、硬件、精度、长度、batch、并发或 production SLO 的通用结论。

Trade-off、failure 与共存边界：动态适配提高样本效用但增加选择开销和反馈偏差；稳定分布可使用静态 curated data。 反证/限制定位为 `S5 — 5 Conclusion`；用于核对的原文摘录：5 Conclusion This work rethinks dynamic data selection through two complementary lenses: representativeness as dataset-level coverage of high-frequency factors, and diversity as a process-level requirement enforced over epochs. Using a fixed sparse-unit probe in a plug-in feature space, we precompute offline scores for representativeness and diversity, and update selection online only through a usage-frequency penalt

Artifact / implementation：exact-v1 `Not Disclosed — arXiv:2603.04981v1 exposes no dedicated Artifact / implementation section in the recovered exact-v1 body`；公开范围摘录：Not Disclosed。未公开的代码、commit、部署配置或复现实验不得由论文叙事反推。

<!-- claim:SF-2026-ARXIV-2603-04981:start -->只接受 arXiv:2603.04981v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。<!-- claim:SF-2026-ARXIV-2603-04981:end -->

Books Comparison：已读 `TRAIN-DATA` 的 `books/part-04-training-system/27-data.md#Data lineage 是训练可复现性的前提 (line 562)` 及相邻 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#本章要回答的问题 (line 10); books/part-04-training-system/28-pretraining.md#本章要回答的问题 (line 10)`；现有命题为“- `SF-2026-ARXIV-2606-22142` — primary `arXiv:2606.22142v1`；exact-v1 URL=`https://arxiv.org/html/2606.22142v1`；Method=`https://arxiv.org/html/2606.22142v1 — §3 Method; §3.2 Agent-Native Governance Over Lifecycle Artifacts; §3.5 Data Health, Training Integration, and Version Governance`；Evaluation=`https://arxiv.org/html/2606.22142v1 — §4 Experiments; §4.1 Experimental Setup`；Non-proof=`https://arxiv.org/html/2606.22142v1 — §5 Limitations and Discussion`。”。Decision=`No Change — Existing Coverage`；该 author-side 判断仍待fresh-context Books reviewer，Integrate 项只进入日期队列。
<!-- review:SF-2026-ARXIV-2603-04981:end -->

<!-- review:SF-2026-ARXIV-2603-05031:start -->
#### AegisUI: Behavioral Anomaly Detection for Structured User Interface Protocols in AI Agent Systems

问题与 changed constraint：Agent 生成的结构化 UI payload 可以通过 schema 校验，却用标签/动作不一致诱导用户批准危险副作用。

旧路径为何合理：在该约束未出现、规模较小或 workload 更稳定时，论文所比较的旧路径仍以更少状态、更短控制链和更成熟实现提供合理基线；不能因本论文出现而静默覆盖。

机制、state/data/control owner：AegisUI 对 UI protocol 的可见语义、隐藏 action 和行为序列做一致性检测，把用户界面也纳入 tool authorization boundary。 对应 exact-v1 `S5 — V AegisUI Framework`；该机制由 `AGENT-TOOL-CALLING` 承载。原文定位摘录仅作核对：V AegisUI Framework The pipeline has four stages: generate, validate, extract, detect. Each stage reads the output of the previous one and writes its own. A single YAML config and a global seed (1337) control the entire run, so re-executing produces identical artifacts. Fig. 3: AegisUI pipeline. Each stage reads the prior output and produces its own artifacts. Generation. Benign payloads start from domain blueprints. For each domain (booking assistant, e-commerce, analytics dashboard, form submission, workflow appr

Evaluation contract：实验只证明所测 payload/攻击和检测器；不保证覆盖所有社会工程或动态 UI。 exact-v1 定位为 `S9 — IX Experimental Setup`；用于核对的原文摘录：IX Experimental Setup We split the 4,000-sample feature matrix 80/20 using stratified sampling (preserving the 3:1 class ratio), giving 3,200 training and 800 test samples. All three models evaluated on the same test set. Feature normalization: z-score scaling (zero mean, unit variance) fitted on training data and applied to test data. This matters most for the autoencoder, because MSE loss is sensitive to feature scale. The autoencoder trained on 2,400 benign training samples only. Isolation Forest and Random Fore

证明与未证明：证据只支持上述 paper-specific workload 内的机制/测量关系；不支持把作者结果外推为其他模型、数据、硬件、精度、长度、batch、并发或 production SLO 的通用结论。

Trade-off、failure 与共存边界：行为检查减少合法结构中的欺骗，却提高 latency 和误报；固定可信模板仍是更简单的高风险路径。 反证/限制定位为 `S11 — XI Discussion`；用于核对的原文摘录：XI Discussion The autoencoder is the practical story. Random Forest wins the numbers, but that requires labeled attack data. The autoencoder achieves 0.762 F1 without ever seeing a malicious payload during training. If you are rolling out a new agent system and have zero attack history, you can train the autoencoder on your benign traffic from day one and have a usable detector. You can always switch to a supervised

Artifact / implementation：exact-v1 `S9 — IX Experimental Setup`；公开范围摘录：IX Experimental Setup We split the 4,000-sample feature matrix 80/20 using stratified sampling (preserving the 3:1 class ratio), giving 3,200 training and 800 test samples. All three models evaluated on the same test set. Feature normalization: z-score scaling (zero mean, unit variance) fitted on training data and applied to test data. This matters most for。未公开的代码、commit、部署配置或复现实验不得由论文叙事反推。

<!-- claim:SF-2026-ARXIV-2603-05031:start -->只接受 arXiv:2603.05031v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。<!-- claim:SF-2026-ARXIV-2603-05031:end -->

Books Comparison：已读 `AGENT-TOOL-CALLING` 的 `books/part-07-agent/78-tool-calling.md#模型输出只是 Proposal (line 72)` 及相邻 `books/part-07-agent/77-memory.md#本章要回答的问题 (line 10); books/part-07-agent/79-planning.md#本章要回答的问题 (line 10)`；现有命题为“Schema 可以拒绝缺字段、错误类型或非法 enum；semantic validation 还要检查金额、目标资源、环境、时间窗口和当前状态。Authorization 必须使用真实 principal，不接受模型生成的 `tenant_id` 或 scope。”。Decision=`No Change — Existing Coverage`；该 author-side 判断仍待fresh-context Books reviewer，Integrate 项只进入日期队列。
<!-- review:SF-2026-ARXIV-2603-05031:end -->

<!-- review:SF-2026-ARXIV-2603-05185:start -->
#### Critic in the Loop: A Tri-System VLA Framework for Robust Long-Horizon Manipulation

问题与 changed constraint：长时程 manipulation 中，高层 VLA 计划会积累错误，低层 controller 又无法判断语义目标是否偏离。

旧路径为何合理：在该约束未出现、规模较小或 workload 更稳定时，论文所比较的旧路径仍以更少状态、更短控制链和更成熟实现提供合理基线；不能因本论文出现而静默覆盖。

机制、state/data/control owner：tri-system VLA 加入独立 critic，在 perception/reasoning-action 与执行反馈间审查并触发修正。 对应 exact-v1 `S3 — 3 Methodology`；该机制由 `MULTIMODAL-EMBODIED-VLA` 承载。原文定位摘录仅作核对：3 Methodology We propose a Tri-System Vision-Language-Action (VLA) architecture. This section formalizes the manipulation problem, details the Brain-Cerebellum backbone (Systems One and Two), introduces the visually-grounded Critic for state evaluation (System Three), delineates the dynamic scheduling mechanism, and concludes with a scalable, automated data annotation pipeline. 3.1 Problem Formulation We formulate long-horizon, language-conditioned manipulation as a dynamic robotic control policy . Unlike tradition

Evaluation contract：实验只证明作者 manipulation 任务中的恢复；不证明 critic 独立于 actor 错误或满足实时 SLO。 exact-v1 定位为 `S4 — 4 Experiments`；用于核对的原文摘录：4 Experiments To evaluate the effectiveness of our proposed Tri-System VLA, we conduct comprehensive real-world experiments. 4.1 Experimental Setup Hardware Platform. All real-world evaluations are conducted on the Cobot Magic ALOHA platform. This dual-arm robotic system features 7 degrees of freedom (DoF) per arm, enabling dexterous bimanual manipulation. The visual perception suite consists of three Intel RealSense D435 depth cameras: one mounted in a front-facing (head) position to capture the global workspace,

证明与未证明：证据只支持上述 paper-specific workload 内的机制/测量关系；不支持把作者结果外推为其他模型、数据、硬件、精度、长度、batch、并发或 production SLO 的通用结论。

Trade-off、failure 与共存边界：反馈纠错提高鲁棒性但增加 latency 和 correlated judge failure；短、确定动作仍可两层控制。 反证/限制定位为 `S5 — 5 Conclusions`；用于核对的原文摘录：5 Conclusions In this paper, we presented the Tri-System VLA, an architecture that synergizes high-level reasoning with continuous control via a critic-guided state evaluator (System Three). By decoupling "thinking" from "acting," our framework enables adaptive cognitive switching and autonomous error correction without requiring exhaustive emergency scenario data. Crucially, the architecture allows for the seamless

Artifact / implementation：exact-v1 `S4.SS1.SSSx2 — Implementation Details.`；公开范围摘录：Implementation Details. We instantiate our Brain-Cerebellum backbone (Systems One and Two) by extending the open-source pi0.5 architecture within the openpi framework [4]. We modify the base pi0.5 model to support autoregressive, discrete subtask text generation, serving as our global semantic planner (System Two). The continuous flow-matching action expert。未公开的代码、commit、部署配置或复现实验不得由论文叙事反推。

<!-- claim:SF-2026-ARXIV-2603-05185:start -->只接受 arXiv:2603.05185v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。<!-- claim:SF-2026-ARXIV-2603-05185:end -->

Books Comparison：已读 `MULTIMODAL-EMBODIED-VLA` 的 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#Edge 与云的分层 (line 499)` 及相邻 `books/part-03-multimodal-world-models/25-multimodal-world-models.md#本章要回答的问题 (line 10); books/part-04-training-system/27-data.md#本章要回答的问题 (line 10)`；现有命题为“高层 semantic planning 可以在云端使用大模型，低层 control 和 emergency response 必须靠近设备。hybrid system 的关键不是“模型放哪”，而是：”。Decision=`No Change — Existing Coverage`；该 author-side 判断仍待fresh-context Books reviewer，Integrate 项只进入日期队列。
<!-- review:SF-2026-ARXIV-2603-05185:end -->

<!-- review:SF-2026-ARXIV-2603-05438:start -->
#### Planning in 8 Tokens: A Compact Discrete Tokenizer for Latent World Model

问题与 changed constraint：latent world model 的规划 token 过长会增加 rollout 成本，过度压缩又会丢失可控状态。

旧路径为何合理：在该约束未出现、规模较小或 workload 更稳定时，论文所比较的旧路径仍以更少状态、更短控制链和更成熟实现提供合理基线；不能因本论文出现而静默覆盖。

机制、state/data/control owner：论文学习紧凑离散 tokenizer，用少量 token 表达 planning-relevant latent state。 对应 exact-v1 `S3 — 3 Method`；该机制由 `MULTIMODAL-WORLD-MODELS` 承载。原文定位摘录仅作核对：3 Method 3.1 Latent generative model as world model In this section, we first describe how a world model can be formulated as a latent generative model. The overall formulation is depicted in Fig. 1. We consider the standard world model setting where the objective is to predict future observations given current state and action. Formally, we denote observations (e.g., video frames) as and actions as .22 2 In navigation settings, actions are 3-dimensional, representing changes in -axis, -axis, and yaw. The formulati

Evaluation contract：8-token 结果只属于作者环境、tokenizer 和 planner；不证明 token 保留所有安全相关因素。 exact-v1 定位为 `S4 — 4 Experiment`；用于核对的原文摘录：4 Experiment 4.1 Experimental Settings We evaluate CompACT across two key aspects: (1) tokenization quality through reconstruction metrics, and (2) planning effectiveness through action-conditioned world models in navigation and manipulation tasks. This dual evaluation validates our hypothesis that extreme compression preserves planning-critical information while enabling efficient decision-time planning. Task conductive. We evaluate CompACT on the following tasks: (1) Image reconstruction: Reconstructing original

证明与未证明：证据只支持上述 paper-specific workload 内的机制/测量关系；不支持把作者结果外推为其他模型、数据、硬件、精度、长度、batch、并发或 production SLO 的通用结论。

Trade-off、failure 与共存边界：规划更快但产生信息瓶颈与不可解释 code；复杂/开放世界仍需更丰富状态。 反证/限制定位为 `S5 — 5 Conclusion`；用于核对的原文摘录：5 Conclusion In this work, we present CompACT, a compact tokenizer that achieves extreme compression by representing images with only 16 or 8 discrete tokens while preserving planning-critical information. The key insight enabling this compression is our use of frozen vision foundation models as the encoder backbone: by leveraging pretrained semantic representations, our tokenizer naturally prioritizes high-level spa

Artifact / implementation：exact-v1 `S5a — E Details of CompACT tokenizer`；公开范围摘录：E Details of CompACT tokenizer Tab. 9 and Tab. 10 summarize the training and model architecture hyperparameters of CompACT, respectively. Tokenizer architecture. We use frozen DINOv3-B [61] in the encoder . In DINOv3-B, we re-initialized the last layer normalization’s affine parameters (weight and bias to 1 and 0, respectively). We found that using pretraine。未公开的代码、commit、部署配置或复现实验不得由论文叙事反推。

<!-- claim:SF-2026-ARXIV-2603-05438:start -->只接受 arXiv:2603.05438v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。<!-- claim:SF-2026-ARXIV-2603-05438:end -->

Books Comparison：已读 `MULTIMODAL-WORLD-MODELS` 的 `books/part-03-multimodal-world-models/25-multimodal-world-models.md#从机制演进到系统设计 (line 640)` 及相邻 `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#本章要回答的问题 (line 10); books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#本章要回答的问题 (line 10)`；现有命题为“从视频生成进入 World Model 的关键约束变化，是输出不再只需“看起来合理”，而要在给定 action 后保持可修正的 environment transition。系统因此从下一帧生成，演进到 latent state、action-conditioned rollout、持久 landmark/memory 与 observation reconciliation；state owner 必须区分预测状态、已观测事实和计划假设。”。Decision=`No Change — Existing Coverage`；该 author-side 判断仍待fresh-context Books reviewer，Integrate 项只进入日期队列。
<!-- review:SF-2026-ARXIV-2603-05438:end -->

<!-- review:SF-2026-ARXIV-2603-05451:start -->
#### FlashAttention-4: Algorithm and Kernel Pipelining Co-Design for Asymmetric Hardware Scaling

问题与 changed constraint：新硬件计算/带宽缩放不对称，旧 FlashAttention pipeline 的 stage 平衡会失效。

旧路径为何合理：在该约束未出现、规模较小或 workload 更稳定时，论文所比较的旧路径仍以更少状态、更短控制链和更成熟实现提供合理基线；不能因本论文出现而静默覆盖。

机制、state/data/control owner：FlashAttention-4 联合重排算法 tiles 与 kernel pipeline，使 load、compute 和 reduce 匹配非对称硬件。 对应 exact-v1 `S4 — 4 Language and Framework`；该机制由 `INFER-TENSORRT-LLM` 承载。原文定位摘录仅作核对：4 Language and Framework We write FlashAttention-4 entirely in CuTe-DSL [21], embedded in Python, without any component in CUDA C++. The CuTe-DSL compiler takes the source code in Python, lowers to PTX, then uses the PTX compiler (ptxas) to finally produce the assembly code (SASS). Full expressivity with clean abstractions. The CuTe-DSL programming model is isomorphic to CUTLASS C++, ensuring that FlashAttention-4 retains the full expressivity of low-level GPU programming while benefiting from the productivity gain

Evaluation contract：性能绑定作者 GPU、dtype、shape、并发和 kernel；不证明未来硬件或所有 attention 变体。 exact-v1 定位为 `A1 — Appendix A Additional Details on Experiments and Benchmarking`；用于核对的原文摘录：Appendix A Additional Details on Experiments and Benchmarking A.1 System and libraries We benchmark the speed on a B100 180GB SXM6 (1000W). We warmup with 5 runs, then repeat the benchmarks 10 times, and take the average timing. We generally used the latest versions of the libraries at the time of writing (March 2025). Specifically, we use: • CUDA 13.1 • FlashAttention 2.8.3 • Triton 3.6 • PyTorch 2.10.0 • CuTe-DSL 4.4.1 For cuDNN, in the main paper, we compare to cuDNN 9.13 and the latest version cuDNN 9.19.1.2. S

证明与未证明：证据只支持上述 paper-specific workload 内的机制/测量关系；不支持把作者结果外推为其他模型、数据、硬件、精度、长度、batch、并发或 production SLO 的通用结论。

Trade-off、failure 与共存边界：硬件特化带来速度但增加复杂度、shape cliff 和维护；不支持平台继续使用通用 SDPA。 反证/限制定位为 `S6 — 6 Discussion and Conclusion`；用于核对的原文摘录：6 Discussion and Conclusion FlashAttention-4 addresses asymmetric hardware scaling, where tensor cores are so fast that the dominant bottlenecks shift to shared-memory traffic and exponential throughput, motivating algorithmic and kernel co-design to mitigate these limits. We redesign the pipeline around fully asynchronous MMA to overlap softmax with larger-tiled matmuls and introduce software-emulated exponential an

Artifact / implementation：exact-v1 `A1.SS1 — A.1 System and libraries`；公开范围摘录：A.1 System and libraries We benchmark the speed on a B100 180GB SXM6 (1000W). We warmup with 5 runs, then repeat the benchmarks 10 times, and take the average timing. We generally used the latest versions of the libraries at the time of writing (March 2025). Specifically, we use: • CUDA 13.1 • FlashAttention 2.8.3 • Triton 3.6 • PyTorch 2.10.0 • CuTe-DSL 4.4。未公开的代码、commit、部署配置或复现实验不得由论文叙事反推。

<!-- claim:SF-2026-ARXIV-2603-05451:start -->只接受 arXiv:2603.05451v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。<!-- claim:SF-2026-ARXIV-2603-05451:end -->

Books Comparison：已读 `INFER-TENSORRT-LLM` 的 `books/part-05-inference-system/49-tensorrt-llm.md#TMA 解决搬运，不负责矩阵计算 (line 341)` 及相邻 `books/part-05-inference-system/48-speculative-decoding.md#本章要回答的问题 (line 10); books/part-05-inference-system/50-vllm.md#本章要回答的问题 (line 10)`；现有命题为“Tensor Memory Accelerator（TMA）在 Hopper（compute capability 9.0）引入，用于把 1D 到多维 tensor tiles 在 global memory 与 shared memory 之间做 bulk asynchronous transfer。Tensor map 描述 base address、shape、stride、element type、interleave/swizzle 等信息；少量 threads 可以发起大块搬运，不必让每个元素先经过普通 registers 和逐元素地址计算。”。Decision=`No Change — Existing Coverage`；该 author-side 判断仍待fresh-context Books reviewer，Integrate 项只进入日期队列。
<!-- review:SF-2026-ARXIV-2603-05451:end -->

<!-- review:SF-2026-ARXIV-2603-05454:start -->
#### Beyond Scattered Acceptance: Fast and Coherent Inference for DLMs via Longest Stable Prefixes

问题与 changed constraint：Diffusion LM 的 block/token 接受若零散，会破坏连贯进展并增加迭代与状态提交成本。

旧路径为何合理：在该约束未出现、规模较小或 workload 更稳定时，论文所比较的旧路径仍以更少状态、更短控制链和更成熟实现提供合理基线；不能因本论文出现而静默覆盖。

机制、state/data/control owner：论文选择 longest stable prefix 作为连续 commit 单元，使 DLM 在多轮修正中保留一致前缀。 对应 exact-v1 `S3 — 3 Method`；该机制由 `MULTIMODAL-GENERATIVE-PARADIGMS` 承载。原文定位摘录仅作核对：3 Method In this section, we detail our proposed approach for accelerating Diffusion Language Model (DLM) inference. We begin by formalizing the standard discrete diffusion framework and pinpointing the inherent inefficiencies of conventional scheduling strategies. We then introduce the Longest Stable Prefix (LSP) scheduler, a training-free, model-agnostic paradigm designed to overcome these limitations. We break down its core components: a stability diagnostic, an adaptive sizing mechanism, and a structural bounda

Evaluation contract：速度/质量只对作者 DLM、稳定判据和任务；不证明 prefix stability 等价于全局正确。 exact-v1 定位为 `S4 — 4 Experiments`；用于核对的原文摘录：4 Experiments 4.1 Experimental Setup Models and Benchmarks. Our empirical evaluation is conducted on two prominent open-source Diffusion Language Models, LLaDA-8B (Nie et al., 2025) and Dream-7B (Ye et al., 2025), to demonstrate the general applicability of our scheduling approach. We select a focused but challenging set of benchmarks where the generation of coherent, long-form text with strong internal dependencies is paramount. For assessing performance on mathematical reasoning, we use GSM8K (Cobbe et al., 2021)

证明与未证明：证据只支持上述 paper-specific workload 内的机制/测量关系；不支持把作者结果外推为其他模型、数据、硬件、精度、长度、batch、并发或 production SLO 的通用结论。

Trade-off、failure 与共存边界：连贯提交减少回滚但可能保守等待或固化早期错误；高并行且可自由修正任务可继续 scattered acceptance。 反证/限制定位为 `S5 — 5 Conclusion`；用于核对的原文摘录：5 Conclusion In this work, we identified scattered token acceptance as a primary algorithmic and systemic bottleneck that throttles the practical inference speed of Diffusion Language Models. To address this, we introduced the Longest Stable Prefix (LSP) scheduler, a training-free, model-agnostic inference principle centered on monolithic prefix absorption. By atomically committing the longest contiguous and stable b

Artifact / implementation：exact-v1 `S4.SS1 — 4.1 Experimental Setup`；公开范围摘录：4.1 Experimental Setup Models and Benchmarks. Our empirical evaluation is conducted on two prominent open-source Diffusion Language Models, LLaDA-8B (Nie et al., 2025) and Dream-7B (Ye et al., 2025), to demonstrate the general applicability of our scheduling approach. We select a focused but challenging set of benchmarks where the generation of coherent, lon。未公开的代码、commit、部署配置或复现实验不得由论文叙事反推。

<!-- claim:SF-2026-ARXIV-2603-05454:start -->只接受 arXiv:2603.05454v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。<!-- claim:SF-2026-ARXIV-2603-05454:end -->

Books Comparison：已读 `MULTIMODAL-GENERATIVE-PARADIGMS` 的 `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#本章要回答的问题 (line 12)` 及相邻 `books/part-03-multimodal-world-models/23-multimodal-representation.md#本章要回答的问题 (line 10); books/part-03-multimodal-world-models/25-multimodal-world-models.md#本章要回答的问题 (line 10)`；现有命题为“为什么文本生成长期以 Autoregressive 为主，而图像和视频大量采用 Diffusion？Masked Diffusion 为什么能并行生成多个 token，却带来 mutable output、cache invalidation 和 streaming 难题？Block Diffusion、draft tree 和 correction loop 是同一条路线吗？”。Decision=`No Change — Existing Coverage`；该 author-side 判断仍待fresh-context Books reviewer，Integrate 项只进入日期队列。
<!-- review:SF-2026-ARXIV-2603-05454:end -->

<!-- review:SF-2026-ARXIV-2603-04411:start -->
#### One Size Does Not Fit All: Token-Wise Adaptive Compression for KV Cache

问题与 changed constraint：统一 KV 压缩率忽略 token 重要性变化，会在不重要 token 上浪费状态或删除关键 token。

旧路径为何合理：在该约束未出现、规模较小或 workload 更稳定时，论文所比较的旧路径仍以更少状态、更短控制链和更成熟实现提供合理基线；不能因本论文出现而静默覆盖。

机制、state/data/control owner：论文按 token 动态选择压缩强度，使 KV precision/retention 成为 token-wise decision。 对应 exact-v1 `S2.SS0.SSS0.Px3 — Architecture-Intrinsic Methods`；该机制由 `INFER-KV-CACHE` 承载。原文定位摘录仅作核对：Architecture-Intrinsic Methods These methods fundamentally alter the attention architecture, necessitating pre-training from scratch or computationally expensive retraining. GQA (Grouped Query Attention) [Ainslie et al., 2023] mitigates the memory bottleneck by grouping multiple query heads to share a single key-value head, offering a balanced trade-off between the quality of Multi-Head Attention (MHA) [Vaswani et al., 2017] and the efficiency of Multi-Query Attention (MQA) [Shazeer, 2019]. MLA (Multi-Head Latent A

Evaluation contract：质量与内存只绑定作者模型、任务和压缩器；不证明重要性估计在分布外稳定。 exact-v1 定位为 `S4 — 4 Experiments`；用于核对的原文摘录：4 Experiments Table 1: Zero-shot performance on short-context benchmarks. “Avg” denotes the average score across these five tasks. Bold indicates the best performance under comparable compression rates (excluding Full Cache). Method Rate ARC-C ARC-E PIQA Wino Hella Avg Llama-3-8B Full Cache 100% 45.76 70.02 80.85 71.51 74.68 68.56 Palu 50% 39.32 63.84 77.58 67.80 69.00 63.51 MatryoshkaKV 50% 38.64 60.49 78.02 63.14 67.36 61.53 DynaKV 47% 44.75 67.37 80.36 67.64 71.70 66.36 Palu 30% 29.15 27.51 71.60 60.62 57.19 49.

证明与未证明：证据只支持上述 paper-specific workload 内的机制/测量关系；不支持把作者结果外推为其他模型、数据、硬件、精度、长度、batch、并发或 production SLO 的通用结论。

Trade-off、failure 与共存边界：细粒度节省更多状态但增加 metadata 和 kernel irregularity；均匀短上下文可用固定压缩。 反证/限制定位为 `S6 — 6 Conclusion`；用于核对的原文摘录：6 Conclusion In this work, we introduce DynaKV, a novel post-training framework for low-rank KV cache compression. To the best of our knowledge, DynaKV is the first approach to move beyond the rigid “one-size-fits-all" compression paradigm by implementing a token-adaptive strategy. By dynamically allocating compression rates based on the semantic significance of individual tokens, our method effectively resolves the

Artifact / implementation：exact-v1 `S5.SS2.SSS0.Px1 — Implementation Details`；公开范围摘录：Implementation Details It is important to note a specific constraint in this integration. Since DynaKV performs a joint spectral decomposition across all attention heads to maximize global information retention, the compressed latent representations are shared. Consequently, we cannot perform head-specific token eviction. Instead, we adopt a global token evi。未公开的代码、commit、部署配置或复现实验不得由论文叙事反推。

<!-- claim:SF-2026-ARXIV-2603-04411:start -->只接受 arXiv:2603.04411v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。<!-- claim:SF-2026-ARXIV-2603-04411:end -->

Books Comparison：已读 `INFER-KV-CACHE` 的 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#一致性不变量 (line 773)` 及相邻 `books/part-05-inference-system/44-decode.md#本章要回答的问题 (line 10); books/part-05-inference-system/46-continuous-batching.md#本章要回答的问题 (line 10)`；现有命题为“RoPE/position policy、compression revision 与 generation boundary，不能被一个模糊的“video cache”标识覆盖。”。Decision=`No Change — Existing Coverage`；该 author-side 判断仍待fresh-context Books reviewer，Integrate 项只进入日期队列。
<!-- review:SF-2026-ARXIV-2603-04411:end -->

<!-- review:SF-2026-ARXIV-2603-04417:start -->
#### Same Input, Different Scores: A Multi Model Study on the Inconsistency of LLM Judge

问题与 changed constraint：LLM judge 对相同输入在模型和重复运行间给出不同分数，单次平均掩盖 evaluator identity 与方差。

旧路径为何合理：在该约束未出现、规模较小或 workload 更稳定时，论文所比较的旧路径仍以更少状态、更短控制链和更成熟实现提供合理基线；不能因本论文出现而静默覆盖。

机制、state/data/control owner：论文跨多 judge/model 重复测量一致性，将 variance 与 disagreement 纳入 evaluation contract。 对应 exact-v1 `PDF page 4; exact heading 3. Experiment`；该机制由 `PLATFORM-EVALUATION-SYSTEM` 承载。原文定位摘录仅作核对：3. Experiment The questions used in this study were sourced from an enterprise chatbot deployment built on a retrieval‑augmented generation (RAG) architecture. As these questions originate from real user interactions, they naturally span a diverse range of categories and reflect authentic information‑seeking behaviour. Due to privacy constraints and the inclusion of proprietary organizational knowledge in the answers, the dataset cannot be released publicly. The use of an internal enterprise dataset also reduces th

Evaluation contract：研究证明所测 judge/任务存在不一致；不证明任何替代 judge 天然可靠，也不提供绝对真值。 exact-v1 定位为 `PDF page 4; exact heading 3. Experiment`；用于核对的原文摘录：3. Experiment The questions used in this study were sourced from an enterprise chatbot deployment built on a retrieval‑augmented generation (RAG) architecture. As these questions originate from real user interactions, they naturally span a diverse range of categories and reflect authentic information‑seeking behaviour. Due to privacy constraints and the inclusion of proprietary organizational knowledge in the answers, the dataset cannot be released publicly. The use of an internal enterprise dataset also reduces th

证明与未证明：证据只支持上述 paper-specific workload 内的机制/测量关系；不支持把作者结果外推为其他模型、数据、硬件、精度、长度、batch、并发或 production SLO 的通用结论。

Trade-off、failure 与共存边界：重复/多 judge 提高不确定性可见性但增加成本；低风险筛选可容忍单 judge，release gate 不应。 反证/限制定位为 `PDF page 13; exact heading 6. Future Work & Limitations`；用于核对的原文摘录：6. Future Work & Limitations This study opens several avenues for further exploration. One natural extension is to examine how prompt design influences scoring stability, and whether prompt‑engineering strategies can meaningfully reduce inconsistency across runs. Given that our evaluation relied on a single, fixed prompt template, future work could test alternative formulations—such as more structured instructions, c

Artifact / implementation：exact-v1 `PDF page 4; exact heading 3. Experiment`；公开范围摘录：3. Experiment The questions used in this study were sourced from an enterprise chatbot deployment built on a retrieval‑augmented generation (RAG) architecture. As these questions originate from real user interactions, they naturally span a diverse range of categories and reflect authentic information‑seeking behaviour. Due to privacy constraints and the incl。未公开的代码、commit、部署配置或复现实验不得由论文叙事反推。

<!-- claim:SF-2026-ARXIV-2603-04417:start -->只接受 arXiv:2603.04417v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。<!-- claim:SF-2026-ARXIV-2603-04417:end -->

Books Comparison：已读 `PLATFORM-EVALUATION-SYSTEM` 的 `books/part-06-ai-infrastructure/66-evaluation-system.md#从答案评分到可执行证据 (line 936)` 及相邻 `books/part-06-ai-infrastructure/65-kai-scheduler.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/67-monitoring.md#本章要回答的问题 (line 10)`；现有命题为“- `SF-2026-ARXIV-2606-21869` — primary `arXiv:2606.21869v1`；exact-v1 URL=`https://arxiv.org/html/2606.21869v1`；Method=`https://arxiv.org/html/2606.21869v1 — §3 Preliminaries — Energy Consumption and Measurement; Multilingual Dataset`；Evaluation=`https://arxiv.org/html/2606.21869v1 — §4 Results and Analysis — Common Setup; §4.1–§4.4; Appendix B Experimental Setups`；Non-proof=`https://arxiv.org/html/2606.21869v1 — §6 Conclusion; Environmental impact of this study; Translation quality and representation; Recommendatio”。Decision=`No Change — Existing Coverage`；该 author-side 判断仍待fresh-context Books reviewer，Integrate 项只进入日期队列。
<!-- review:SF-2026-ARXIV-2603-04417:end -->

<!-- review:SF-2026-ARXIV-2603-04427:start -->
#### Thin Keys, Full Values: Reducing KV Cache via Low-Dimensional Attention Selection

问题与 changed constraint：KV key 和 value 对 attention 选择与内容恢复承担不同责任，等宽压缩可能在 value 上损失过多。

旧路径为何合理：在该约束未出现、规模较小或 workload 更稳定时，论文所比较的旧路径仍以更少状态、更短控制链和更成熟实现提供合理基线；不能因本论文出现而静默覆盖。

机制、state/data/control owner：Thin Keys, Full Values 只把 key 投影到低维用于选择，保留完整 value 承载内容。 对应 exact-v1 `S2 — 2 Method`；该机制由 `INFER-KV-CACHE` 承载。原文定位摘录仅作核对：2 Method 2.1 Asymmetric Attention In multi-head attention with heads, standard transformers set for all of , , and . We decouple this by introducing , the total dimensionality for queries and keys: (5) For each head , the attention computation is: (6) (7) (8) (9) Critically, no projection is needed between the attention weight computation and the value aggregation: the attention weights are scalars regardless of , and they multiply of any dimensionality. When , this reduces to standard multi-head attention. When ,

Evaluation contract：内存/质量结果绑定作者 attention、projection 和任务；不证明低维 key 对所有 head/层保序。 exact-v1 定位为 `S3 — 3 Experiments`；用于核对的原文摘录：3 Experiments We validate asymmetric attention through seven experiments of increasing complexity: two controlled algorithmic tasks that isolate positional and content-based selection, two language modeling benchmarks at 10M-parameter scale, post-training SVD compression with fine-tuning recovery on GPT-2, a 125M-parameter LLaMA model confirming architecture generality, and SVD + fine-tuning at 7B scale on Mistral-7B. Experiments 1–4 use a standard transformer decoder with pre-norm layer normalization, GELU activat

证明与未证明：证据只支持上述 paper-specific workload 内的机制/测量关系；不支持把作者结果外推为其他模型、数据、硬件、精度、长度、batch、并发或 production SLO 的通用结论。

Trade-off、failure 与共存边界：保 value 提高质量但节省上限低于双侧压缩，且增加 mixed-layout kernel；内存极紧时仍需压 value。 反证/限制定位为 `S6.SS0.SSS0.Px1 — Limitations.`；用于核对的原文摘录：Limitations. Our training-from-scratch experiments use models up to 125M parameters, though SVD + fine-tuning is validated at 7B scale (Mistral-7B). The consistent 2% residual gap at 75% K cache reduction across GPT-2 (124M) and Mistral-7B (7.2B)—a 58 scale difference—provides strong evidence that the approach generalizes. However, training from scratch with asymmetric attention at 7B+ scale remains future work. Addi

Artifact / implementation：exact-v1 `S3.SS5.SSS0.Px3 — Deployment via factored keys.`；公开范围摘录：Deployment via factored keys. The SVD factorization provides a direct path to KV cache reduction. Given where and , we can split the computation: (store in cache — small) (15) (compute at query time — discarded) (16) The attention scores are preserved exactly: (17) The key cache now stores -dimensional vectors instead of -dimensional ones, while is absorbed。未公开的代码、commit、部署配置或复现实验不得由论文叙事反推。

<!-- claim:SF-2026-ARXIV-2603-04427:start -->只接受 arXiv:2603.04427v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。<!-- claim:SF-2026-ARXIV-2603-04427:end -->

Books Comparison：已读 `INFER-KV-CACHE` 的 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#一致性不变量 (line 885)` 及相邻 `books/part-05-inference-system/44-decode.md#本章要回答的问题 (line 10); books/part-05-inference-system/46-continuous-batching.md#本章要回答的问题 (line 10)`；现有命题为“PD 分离中固定 codec 在某些 model、layer、length 或网络状态下有效，在另一些场景会让 encode/decode 超过节省的传输。Service-aware planner 可把 quantization、sparsity、chunking 与 recomposition 视为策略空间，用离线 profiling 在 quality、latency、bandwidth 和 GPU budget 下选 plan，并把 chosen policy 绑定 cache/transfer identity。它用更好适配换 profile 成本、search drift 和更复杂 fallback；未命中已验证 workload 时应回退原始 KV 或保守 codec。作者 benchmark 不构成跨硬件通用压缩收益。”。Decision=`No Change — Existing Coverage`；该 author-side 判断仍待fresh-context Books reviewer，Integrate 项只进入日期队列。
<!-- review:SF-2026-ARXIV-2603-04427:end -->

<!-- review:SF-2026-ARXIV-2603-04621:start -->
#### DuaLip-GPU Technical Report

问题与 changed constraint：GPU execution 若只优化单算子，会在双路径/流水衔接、内存与同步上留下系统瓶颈。

旧路径为何合理：在该约束未出现、规模较小或 workload 更稳定时，论文所比较的旧路径仍以更少状态、更短控制链和更成熟实现提供合理基线；不能因本论文出现而静默覆盖。

机制、state/data/control owner：DuaLip-GPU 设计双 pipeline 协同计算和数据搬运，以端到端 plan 管理 overlap。 对应 exact-v1 `S4 — 4 Programming Model and Library Architecture`；该机制由 `INFER-TENSORRT-LLM` 承载。原文定位摘录仅作核对：4 Programming Model and Library Architecture The previous Scala Spark version of DuaLip [7] enabled the first production deployments, but it supported only two rigid schemas and relied on an object model that made extensions costly. Its runtime also fit poorly with common numerical tooling and Python workflows, so diagnostics and tuning were largely manual. We re-architect LP solving in an imperative, operator-level array/tensor programming model (PyTorch-style, define-by-run) rather than a task-level “call a solve

Evaluation contract：技术报告结果绑定作者 kernel、shape 与 GPU；不证明框架集成、并发和数值边界。 exact-v1 定位为 `S7 — 7 Experiments`；用于核对的原文摘录：7 Experiments We evaluate the proposed PyTorch implementation of DuaLip along three axes: (i) numerical parity with the production Scala implementation, (ii) system-level performance and multi-GPU scaling, and (iii) the impact of algorithmic enhancements such as preconditioning and regularization continuation. We use synthetic matching data to enable controlled scaling of problem size and sparsity. The data generation procedure and complete experimental setup are described in Appendix B. Implementation parity We fi

证明与未证明：证据只支持上述 paper-specific workload 内的机制/测量关系；不支持把作者结果外推为其他模型、数据、硬件、精度、长度、batch、并发或 production SLO 的通用结论。

Trade-off、failure 与共存边界：更强 overlap 换来调度和资源竞争复杂度；算子小或无可重叠 I/O 时普通执行更简单。 反证/限制定位为 `S8 — 8 Discussion and Limitations`；用于核对的原文摘录：8 Discussion and Limitations This report provided an overview of the principal architectural choices, algorithmic improvements, and GPU implementation strategies needed to address extreme-scale matching problems in an industrial setting. A natural next step is to further evaluate the core dual-ascent method on standard linear programming benchmarks beyond matching. In addition, because suitable real-world public data

Artifact / implementation：exact-v1 `S7.SS0.SSS0.Px1 — Implementation parity`；公开范围摘录：Implementation parity We first verify numerical equivalence between the PyTorch implementation and the original Scala solver. Figure 1 compares the dual objective trajectories across accelerated gradient descent (AGD) iterations in single- and multi-GPU settings. The trajectories exhibit near-perfect overlap across all configurations, confirming implementati。未公开的代码、commit、部署配置或复现实验不得由论文叙事反推。

<!-- claim:SF-2026-ARXIV-2603-04621:start -->只接受 arXiv:2603.04621v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。<!-- claim:SF-2026-ARXIV-2603-04621:end -->

Books Comparison：已读 `INFER-TENSORRT-LLM` 的 `books/part-05-inference-system/49-tensorrt-llm.md#本章要回答的问题 (line 16)` 及相邻 `books/part-05-inference-system/48-speculative-decoding.md#本章要回答的问题 (line 10); books/part-05-inference-system/50-vllm.md#本章要回答的问题 (line 10)`；现有命题为“这里的 `stack` 很重要。当前官方文档覆盖的不只是离线构建计算图，也包括 runtime、in-flight batching、paged KV caching、quantization 以及多 GPU/多节点执行。把 TensorRT-LLM 固定理解成“先编译一个静态 engine”会低估它已经扩展出的 Serving 能力；但本章仍以 GPU execution optimization 为主线，避免写成版本功能目录。”。Decision=`No Change — Existing Coverage`；该 author-side 判断仍待fresh-context Books reviewer，Integrate 项只进入日期队列。
<!-- review:SF-2026-ARXIV-2603-04621:end -->

<!-- review:SF-2026-ARXIV-2603-04656:start -->
#### iAgentBench: Benchmarking Sensemaking Capabilities of Information-Seeking Agents on High-Traffic Topics

问题与 changed constraint：信息搜索 Agent 可检索多个片段却不能综合冲突证据，单 passage QA 不能测这种 sensemaking。

旧路径为何合理：在该约束未出现、规模较小或 workload 更稳定时，论文所比较的旧路径仍以更少状态、更短控制链和更成熟实现提供合理基线；不能因本论文出现而静默覆盖。

机制、state/data/control owner：iAgentBench 将多源检索、证据关系、冲突消解和最终回答绑定为同一评估任务。 对应 exact-v1 `S3 — 3. Method`；该机制由 `PLATFORM-EVALUATION-SYSTEM` 承载。原文定位摘录仅作核对：3. Method iAgentBench is a dynamic, open-domain QA benchmark construction pipeline designed to evaluate cross-document sensemaking for information-seeking agents. The key idea is to start from realistic, traffic-driven topics, retrieve a query-conditioned corpus from the web, build a compact structured representation of how themes in that corpus relate, and then generate questions whose answers depend on multiple themes and the explicit links between them. Figure 1 summarizes the pipeline. Figure 1. Overview of the

Evaluation contract：结果只属于所测高流量主题、搜索快照与 judge；不证明覆盖开放世界事实变化。 exact-v1 定位为 `S5 — 5. Experiments & Results`；用于核对的原文摘录：5. Experiments & Results In this section, we evaluate how evidence access and evidence integration affect end-to-end QA performance, and how iAgentBench compares to standard ODQA benchmarks. We compare four widely adopted LLMs under three inference settings: Base (no external tools), RAG (first page of retrieved documents from SearxNG (SearXNG contributors, )), and Reflexion (agentic self-reflection over retrieved evidence (Shinn et al., 2023)). We report accuracy on two standard ODQA benchmarks, SimpleQA (Wei et a

证明与未证明：证据只支持上述 paper-specific workload 内的机制/测量关系；不支持把作者结果外推为其他模型、数据、硬件、精度、长度、batch、并发或 production SLO 的通用结论。

Trade-off、failure 与共存边界：多源任务提高真实性但引入时效、搜索排名与标注不确定；固定单文档集仍适合检索组件回归。 反证/限制定位为 `S7 — 7. Limitations`；用于核对的原文摘录：7. Limitations Cost of dynamic construction. Dynamic benchmarking increases cost relative to static QA datasets. iAgentBench requires retrieval, query-conditioned graph construction, and generation whenever a new evaluation window is produced, increasing compute and API overhead. This is an inherent trade-off of evaluating retrieval-augmented and agentic systems under evolving information. Dependence on generative mo

Artifact / implementation：exact-v1 `Not Disclosed — arXiv:2603.04656v1 exposes no dedicated Artifact / implementation section in the recovered exact-v1 body`；公开范围摘录：Not Disclosed。未公开的代码、commit、部署配置或复现实验不得由论文叙事反推。

<!-- claim:SF-2026-ARXIV-2603-04656:start -->只接受 arXiv:2603.04656v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。<!-- claim:SF-2026-ARXIV-2603-04656:end -->

Books Comparison：已读 `PLATFORM-EVALUATION-SYSTEM` 的 `books/part-06-ai-infrastructure/66-evaluation-system.md#Scorer 不是绝对真相 (line 1719)` 及相邻 `books/part-06-ai-infrastructure/65-kai-scheduler.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/67-monitoring.md#本章要回答的问题 (line 10)`；现有命题为“明确 issue、固定 tests 的 benchmark 对局部修复仍然理想：输入、预期行为与失败位置清楚，回归也容易复现。但从零构建 repository 时，agent 常先面对不完整 product intent。若只看最终 tests，需求从未被告知与 agent 已获得需求却没有正确实现会被压成同一种失败，评测无法判断问题出在 information access 还是 execution conversion。”。Decision=`No Change — Existing Coverage`；该 author-side 判断仍待fresh-context Books reviewer，Integrate 项只进入日期队列。
<!-- review:SF-2026-ARXIV-2603-04656:end -->

<!-- review:SF-2026-ARXIV-2603-04851:start -->
#### Why Is RLHF Alignment Shallow? A Gradient Analysis

问题与 changed constraint：RLHF 安全对齐常表现为局部、易被绕过，但只看行为无法定位为何更新集中在少数 token/决策位置。

旧路径为何合理：在该约束未出现、规模较小或 workload 更稳定时，论文所比较的旧路径仍以更少状态、更短控制链和更成熟实现提供合理基线；不能因本论文出现而静默覆盖。

机制、state/data/control owner：论文以序列 harm 的 martingale/协方差分解刻画 gradient，使 alignment locality 成为可分析的 objective property。 对应 exact-v1 `https://arxiv.org/html/2603.04851v1#S4 — exact-v1 §4 Martingale Decomposition of Harm, followed by §5–§9 gradient and recovery analysis (Method)`；该机制由 `TRAIN-RLHF` 承载。原文定位摘录仅作核对：Not Disclosed

Evaluation contract：理论在定义与假设下成立，实验证据不证明所有对齐方法都浅或所有模型共享同一层结构。 exact-v1 定位为 `A2 — Appendix B Proofs and Supplementary Results for Deep Alignment`；用于核对的原文摘录：Appendix B Proofs and Supplementary Results for Deep Alignment This appendix provides full proofs for the results in Section 9 and additional remarks on their scope. B.1 Recovery Gradient Bound Lemma 28 (Recovery Gradient Bound). The recovery gradient satisfies (61) If uniformly, then . Proof. The argument is identical in structure to the proof of Theorem 13. Write . For a fixed prefix , by Cauchy–Schwarz applied coordinate-wise: (62) Summing over coordinates and using (since ): (63) where . Taking the outer expect

证明与未证明：证据只支持上述 paper-specific workload 内的机制/测量关系；不支持把作者结果外推为其他模型、数据、硬件、精度、长度、batch、并发或 production SLO 的通用结论。

Trade-off、failure 与共存边界：定向更新节省样本却可能留下未覆盖后缀与分布外路径；更全面约束会增加能力损失和优化难度。 反证/限制定位为 `Sx1 — Limitations`；用于核对的原文摘录：Limitations We now discuss the limitations of our work. These limitations suggest important directions for future work and caveats for interpreting our results. We analyze gradients with respect to output distributions . Representation-level interventions such as circuit breakers and activation steering operate on internal model states and may achieve alignment depth through mechanisms we do not capture. Formalizing

Artifact / implementation：exact-v1 `Not Disclosed — arXiv:2603.04851v1 exposes no dedicated Artifact / implementation section in the recovered exact-v1 body`；公开范围摘录：Not Disclosed。未公开的代码、commit、部署配置或复现实验不得由论文叙事反推。

<!-- claim:SF-2026-ARXIV-2603-04851:start -->只接受 arXiv:2603.04851v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。<!-- claim:SF-2026-ARXIV-2603-04851:end -->

Books Comparison：已读 `TRAIN-RLHF` 的 `books/part-04-training-system/31-rlhf.md#Sequence reward 与 token updates 的错位 (line 225)` 及相邻 `books/part-04-training-system/30-lora.md#本章要回答的问题 (line 10); books/part-04-training-system/32-ppo.md#本章要回答的问题 (line 10)`；现有命题为“Reward Model 通常在完整 response 后给出 scalar，而 policy 逐 token 生成；sequence outcome 本身不能指出哪个 token 导致好坏，长序列、稀疏 reward 与延迟反馈会放大 credit-assignment 方差。”。Decision=`Integrate`；该 author-side 判断仍待fresh-context Books reviewer，Integrate 项只进入日期队列。
<!-- review:SF-2026-ARXIV-2603-04851:end -->

<!-- review:SF-2026-ARXIV-2603-05087:start -->
#### PromptTuner: SLO-Aware Elastic System for LLM Prompt Tuning

问题与 changed constraint：多租户 prompt tuning 的任务大小与 SLO 不同，静态 GPU allocation 会造成排队或资源浪费。

旧路径为何合理：在该约束未出现、规模较小或 workload 更稳定时，论文所比较的旧路径仍以更少状态、更短控制链和更成熟实现提供合理基线；不能因本论文出现而静默覆盖。

机制、state/data/control owner：PromptTuner 将 job profile、deadline 与 elastic resource control 连接，让 admission/scaling 依据可测训练 work 而变化。 对应 exact-v1 `S4 — 4. System Design`；该机制由 `PLATFORM-GPU-SCHEDULER` 承载。原文定位摘录仅作核对：4. System Design We introduce PromptTuner, an SLO-aware elastic cluster management system for LPT workloads. We begin with the design insights and overview, followed by the illustration of its two key components: Prompt Bank and Workload Scheduler. 4.1. Design Insights The design of PromptTuner is motivated by two insights. Our first insight is that LPT tasks can reuse the prompts optimized for similar tasks as their initial prompt to reduce the number of tuning iterations needed to achieve the desired accuracy. Ex

Evaluation contract：结果只支持所测模型、GPU 和到达分布；不证明 profile 对新 prompt/data 保持校准。 exact-v1 定位为 `S6.SS1 — 6.1. Experimental Setup`；用于核对的原文摘录：6.1. Experimental Setup Testbed. We set up PromptTuner in a physical GPU cluster. Each GPU server has eight NVIDIA A100-80GB GPUs and one 200Gbs HDR InfiniBand. It features an Intel Xeon 8369B 2.90GHz CPU with 64 cores, 256 GB RAM, and PCIe-III. PromptTuner provisions at most 4 GPU servers. We adopt Memcached 1.5.22 to set up an Elastic Cache service for communication among GPU servers. Workload Construction. We evaluate three representative LLMs (GPT-Base, GPT-Large, Vicuna-7B) on 12 datasets, as shown in Table 6.

证明与未证明：证据只支持上述 paper-specific workload 内的机制/测量关系；不支持把作者结果外推为其他模型、数据、硬件、精度、长度、batch、并发或 production SLO 的通用结论。

Trade-off、failure 与共存边界：弹性提高利用率却增加迁移、干扰和预测误差；稳定独占任务仍适合固定资源。 反证/限制定位为 `S4.SS3.SSS4 — 4.3.4. Two-layer Structure Discussion`；用于核对的原文摘录：4.3.4. Two-layer Structure Discussion The prevalent similarities among prompts suggest that clustering similar prompts can avoid unnecessary score assessment with minor speedup benefit loss. The study in §6.3 indicates that a two-layer data structure can identify effective initial prompts within 10 seconds. Additionally, we construct a three-layer structure using K-medoid clustering, but encounter convergence issues

Artifact / implementation：exact-v1 `S5 — 5. Implementation`；公开范围摘录：5. Implementation 5.1. Multi-GPU Execution We implement LPT jobs with 2000 lines of Python code atop Transformers 2.4.1 and PyTorch 2.1 and deploy them as containerized GPU Knative functions to pre-load the LPT runtime and LLM weights in the GPU. Each Knative function accepts a set of parameters described in Table 3 and responds to users with the optimized p。未公开的代码、commit、部署配置或复现实验不得由论文叙事反推。

<!-- claim:SF-2026-ARXIV-2603-05087:start -->只接受 arXiv:2603.05087v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。<!-- claim:SF-2026-ARXIV-2603-05087:end -->

Books Comparison：已读 `PLATFORM-GPU-SCHEDULER` 的 `books/part-06-ai-infrastructure/63-gpu-scheduler.md#与推理 Scheduler 的边界 (line 243)` 及相邻 `books/part-06-ai-infrastructure/62-gateway.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/64-volcano.md#本章要回答的问题 (line 10)`；现有命题为“time-slicing、MPS 与 MIG 都假设 runtime 与隔离边界相对明确；当 CUDA 与 Vulkan 等不同 API 共享同一设备时，空间复用还会引入跨 API 的 allocation、同步与地址可见性问题。平台不能只把两类进程放在同一 GPU 上就宣称共享成功：scheduler 要拥有可审计的 resource partition，driver/runtime 要拥有 synchronization 与 memory-safety contract，workload identity 还必须绑定 API、context 和 device state。”。Decision=`No Change — Existing Coverage`；该 author-side 判断仍待fresh-context Books reviewer，Integrate 项只进入日期队列。
<!-- review:SF-2026-ARXIV-2603-05087:end -->

<!-- review:SF-2026-ARXIV-2603-05147:start -->
#### Act, Think or Abstain: Complexity-Aware Adaptive Inference for Vision-Language-Action Models

问题与 changed constraint：VLA 每一步都长推理会错过控制周期，永远快速行动又会在复杂状态犯错。

旧路径为何合理：在该约束未出现、规模较小或 workload 更稳定时，论文所比较的旧路径仍以更少状态、更短控制链和更成熟实现提供合理基线；不能因本论文出现而静默覆盖。

机制、state/data/control owner：论文按状态复杂度在 act、think、abstain 三条路径间选择，将推理预算和安全拒绝纳入 controller。 对应 exact-v1 `S3 — III METHOD`；该机制由 `MULTIMODAL-EMBODIED-VLA` 承载。原文定位摘录仅作核对：III METHOD Our approach leverages SmolVLA [13] as the reference Vision-Language-Action architecture, which integrates a pretrained SmolVLM-2 [19] backbone with an action expert optimized via flow-matching [20]. To enable the agent to be aware of task complexity and act accordingly, we propose a pipeline that transforms the embeddings extracted from the VLM into a routing mechanism for adaptive inference. In Section III-A, we define the extraction and preprocessing of multimodal features from the VLM backbone. We th

Evaluation contract：收益只覆盖作者复杂度估计、机器人和任务；不证明门控在未知风险中校准。 exact-v1 定位为 `S4 — IV EXPERIMENTAL RESULTS`；用于核对的原文摘录：IV EXPERIMENTAL RESULTS In this section, we provide a comprehensive evaluation of our framework across a diverse set of robotic manipulation tasks. Our experiments are designed to validate the system’s ability to infer the task complexity at inference time and select an optimal execution strategy. We assess the performance of our pipeline using the LIBERO and LIBERO-PRO benchmarks, focusing on scenarios where standard VLAs typically struggle due to distribution shifts. Specifically, we aim to address the following

证明与未证明：证据只支持上述 paper-specific workload 内的机制/测量关系；不支持把作者结果外推为其他模型、数据、硬件、精度、长度、batch、并发或 production SLO 的通用结论。

Trade-off、failure 与共存边界：自适应计算降低平均 latency，但错误门控会延迟或危险行动；固定安全关键回路仍需确定性控制。 反证/限制定位为 `S6 — VI LIMITATIONS AND FUTURE WORKS`；用于核对的原文摘录：VI LIMITATIONS AND FUTURE WORKS While our vision-only GMM exhibits convincing performances, there is still a gap in recovering partially OOD tasks that are classified as ID. This is probably due to the transition between Act, Think, and Abstain being managed as a classification problem, and thus creating rigid boundaries at the edges of the distribution shifts. A possible solution for this might be treating the probl

Artifact / implementation：exact-v1 `S3.SS4 — III-D Training`；公开范围摘录：III-D Training To ground our system, we selected HuggingFaceVLA/smolvla_libero, which is pre-trained on LIBERO [25]. We define a suite of training datasets categorized by the three levels of distribution shift (i.e., ID, partially OOD, OOD). We consider the original LIBERO tasks to be in-distribution (ID), as the model has been fine-tuned on them, representi。未公开的代码、commit、部署配置或复现实验不得由论文叙事反推。

<!-- claim:SF-2026-ARXIV-2603-05147:start -->只接受 arXiv:2603.05147v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。<!-- claim:SF-2026-ARXIV-2603-05147:end -->

Books Comparison：已读 `MULTIMODAL-EMBODIED-VLA` 的 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#从模块化机器人到 VLA (line 90)` 及相邻 `books/part-03-multimodal-world-models/25-multimodal-world-models.md#本章要回答的问题 (line 10); books/part-04-training-system/27-data.md#本章要回答的问题 (line 10)`；现有命题为“把 vision/language hidden state 直接送入 action head，接口最短，在 viewpoint、task 与 action schema 稳定时也最简单；但 joint training 同时允许 action loss 直接改写通用 semantic representation。数据较窄或 real-scene visual shift 较大时，instruction generation、object grounding 与 local action direction 可能被同一 latent 中的冲突梯度一起扰动。”。Decision=`No Change — Existing Coverage`；该 author-side 判断仍待fresh-context Books reviewer，Integrate 项只进入日期队列。
<!-- review:SF-2026-ARXIV-2603-05147:end -->

<!-- review:SF-2026-ARXIV-2603-05210:start -->
#### Balancing Coverage and Draft Latency in Vocabulary Trimming for Faster Speculative Decoding

问题与 changed constraint：speculative decoding 缩小 draft vocabulary 可降低草稿延迟，却会降低 target token 覆盖和接受率。

旧路径为何合理：在该约束未出现、规模较小或 workload 更稳定时，论文所比较的旧路径仍以更少状态、更短控制链和更成熟实现提供合理基线；不能因本论文出现而静默覆盖。

机制、state/data/control owner：论文联合选择 vocabulary coverage 与 draft cost，在模型/工作负载上寻找平衡点。 对应 exact-v1 `S2 — 2 Method`；该机制由 `INFER-SPECULATIVE-DECODING` 承载。原文定位摘录仅作核对：2 Method In this work, we present a vocabulary trimming approach for speculative decoding that optimizes the trade-off between token coverage and draft model latency. Our method consists of five components: (1) formulating vocabulary selection as constrained optimization, (2) computing token coverage from training data, (3) estimating draft model FLOPs, (4) defining a utility function, and (5) optimizing via Tree-structured Parzen Estimator. 2.1 Problem Formulation Let denote the target model’s vocabulary with toke

Evaluation contract：速度只属于作者词表、模型配对和硬件；不证明静态 trimmed vocabulary 对领域漂移稳健。 exact-v1 定位为 `S3 — 3 Experiments`；用于核对的原文摘录：3 Experiments To evaluate our approach, we adopt Llama-3.1-8B-Instruct Grattafiori et al. (2024) as the target model and use datasets to regenerate responses with Llama-3.1-8B-Instruct, ensuring alignment between the draft model and the target model it is trained to accelerate. We then measure the inference throughput of the resulting draft model using the SpecForge framework Li et al. (2025a) together with the SGLang inference engine Zheng et al. (2024). All experiments are conducted with 3 independent runs, and w

证明与未证明：证据只支持上述 paper-specific workload 内的机制/测量关系；不支持把作者结果外推为其他模型、数据、硬件、精度、长度、batch、并发或 production SLO 的通用结论。

Trade-off、failure 与共存边界：更快 draft 换来覆盖缺口与 fallback；开放域或低可预测文本应保留更大词表。 反证/限制定位为 `S5 — 5 Limitations`；用于核对的原文摘录：5 Limitations Our approach has several limitations. First, we evaluate only on LLaMA-3.1-8B-Instruct as the target model; generalization to other model families (e.g., Qwen, Gemma, Mistral) and larger model scales (70B, 405B) remains to be validated. Second, our approach requires training the draft model with the reduced vocabulary, unlike inference-time methods such as VocabTrim Goel et al. (2025) that prune the voc

Artifact / implementation：exact-v1 `Not Disclosed — arXiv:2603.05210v1 exposes no dedicated Artifact / implementation section in the recovered exact-v1 body`；公开范围摘录：Not Disclosed。未公开的代码、commit、部署配置或复现实验不得由论文叙事反推。

<!-- claim:SF-2026-ARXIV-2603-05210:start -->只接受 arXiv:2603.05210v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。<!-- claim:SF-2026-ARXIV-2603-05210:end -->

Books Comparison：已读 `INFER-SPECULATIVE-DECODING` 的 `books/part-05-inference-system/48-speculative-decoding.md#本章要回答的问题 (line 16)` 及相邻 `books/part-05-inference-system/47-pagedattention.md#本章要回答的问题 (line 10); books/part-05-inference-system/49-tensorrt-llm.md#本章要回答的问题 (line 10)`；现有命题为“本章的核心判断是：**Speculative Decoding 用额外且便宜的 proposal work，换取一次 target-model verification 推进多个 output tokens；经典算法通过 acceptance 与 residual sampling 保持 target distribution，而不是用 draft model 改写模型行为。**”。Decision=`No Change — Existing Coverage`；该 author-side 判断仍待fresh-context Books reviewer，Integrate 项只进入日期队列。
<!-- review:SF-2026-ARXIV-2603-05210:end -->

<!-- review:SF-2026-ARXIV-2603-05353:start -->
#### InfoFlow KV: Information-Flow-Aware KV Recomputation for Long Context

问题与 changed constraint：文档级预计算 KV 会丢失跨文档 causal dependency；全量重新 prefill 又消除缓存收益。

旧路径为何合理：在该约束未出现、规模较小或 workload 更稳定时，论文所比较的旧路径仍以更少状态、更短控制链和更成熟实现提供合理基线；不能因本论文出现而静默覆盖。

机制、state/data/control owner：InfoFlow KV 根据跨 token 信息流选择需要重算的局部状态，使缓存复用和因果修复共享一个选择 contract。 对应 exact-v1 `S4 — 4 Method`；该机制由 `INFER-KV-CACHE` 承载。原文定位摘录仅作核对：4 Method In this section, we introduce our method for selecting recomputation targets by jointly considering token semantic relevance and positional influence, with the goal of facilitating information propagation during decoding. 4.1 Input Chunking and Prefilling Let the input consist of tokens, which we partition into disjoint chunks . Each chunk serves as a basic unit for prefilling and can correspond to a naturally independent segment (e.g., a document or an image), or a contiguous partition of a single long in

Evaluation contract：结果只属于作者长文任务、模型和信息流估计；不证明未选 token 对答案无影响。 exact-v1 定位为 `S6 — 6 Experiment`；用于核对的原文摘录：6 Experiment 6.1 Experiment Setup Methods. We compare our approach against a set of representative baselines and prior KV recomputation methods. Across all experiments, we evaluate the following inference strategies: (i) Baseline, which performs full-context prefilling without chunking; (ii) No Recompute, which applies chunk-wise prefilling without any KV recomputation; (iii) Our, the proposed semantic- and position-aware selective KV recomputation method; (iv) Our + Reorder, which further incorporates the segment

证明与未证明：证据只支持上述 paper-specific workload 内的机制/测量关系；不支持把作者结果外推为其他模型、数据、硬件、精度、长度、batch、并发或 production SLO 的通用结论。

Trade-off、failure 与共存边界：选择性重算节省 prefill，却引入估计成本和遗漏依赖风险；高风险或短 context 仍应完整 prefill。 反证/限制定位为 `S8 — 8 Discussion`；用于核对的原文摘录：8 Discussion Recomputation Efficiency under Irregular Attention Masks Selective KV recomputation requires attending a dynamically selected subset of tokens to the full context under a causal constraint, resulting in an irregular attention mask that is neither fully dense nor strictly causal. Such patterns are not efficiently supported by existing optimized attention kernels (e.g., FlashAttention), leading to suboptim

Artifact / implementation：exact-v1 `A2 — Appendix B More Implementation Details`；公开范围摘录：Appendix B More Implementation Details Norm Layer Selection. To determine which Transformer layer to use for identifying important tokens, we perform a layer-wise analysis on Qwen models. Specifically, we evaluate prompt–context attention norms extracted from different layers and measure their downstream impact on long-context retrieval accuracy. We find tha。未公开的代码、commit、部署配置或复现实验不得由论文叙事反推。

<!-- claim:SF-2026-ARXIV-2603-05353:start -->只接受 arXiv:2603.05353v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。<!-- claim:SF-2026-ARXIV-2603-05353:end -->

Books Comparison：已读 `INFER-KV-CACHE` 的 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#Structured knowledge 只有进入 physical access plan 才改变 KV 成本 (line 152)` 及相邻 `books/part-05-inference-system/44-decode.md#本章要回答的问题 (line 10); books/part-05-inference-system/46-continuous-batching.md#本章要回答的问题 (line 10)`；现有命题为“逻辑 prompt 保持不变时，physical-read optimization 可以只读取计划区域，但 access plan 必须绑定模型、tokenization、KV layout 与 knowledge revision；依赖不确定或验证失败时应回退 full context。”。Decision=`Integrate`；该 author-side 判断仍待fresh-context Books reviewer，Integrate 项只进入日期队列。
<!-- review:SF-2026-ARXIV-2603-05353:end -->

<!-- review:SF-2026-ARXIV-2603-05399:start -->
#### Judge Reliability Harness: Stress Testing the Reliability of LLM Judges

问题与 changed constraint：LLM judge 平均相关性无法揭示顺序、风格、重复和对抗输入下的可靠性退化。

旧路径为何合理：在该约束未出现、规模较小或 workload 更稳定时，论文所比较的旧路径仍以更少状态、更短控制链和更成熟实现提供合理基线；不能因本论文出现而静默覆盖。

机制、state/data/control owner：Judge Reliability Harness 对 judge 进行成组 stress test 并保存 evaluator/version/seed 证据。 对应 exact-v1 `S3 — 3 Methodology`；该机制由 `PLATFORM-EVALUATION-SYSTEM` 承载。原文定位摘录仅作核对：3 Methodology In this section, we outline and describe the reliability tests used to systematically evaluate LLM judge reliability. Each test reveals a different dimension of reliability/robustness through the generation and validation of synthetically generated data. Each run proceeds in four stages: (1) the seed dataset is loaded and normalized into a common schema (2) synthetic data pipelines are run to generate and validate perturbed items that probe different failure modes, (3) the judge is evaluated on the ge

Evaluation contract：结果揭示所测 judge 的 failure；不证明 harness 场景穷尽真实偏差或能给出真值。 exact-v1 定位为 `S4 — 4 Experiments`；用于核对的原文摘录：4 Experiments This section describes the experimental setup used to evaluate the Judge Reliability Harness. We specify the benchmarks, rubrics, and model judges considered, the configuration of the reliability tests, and the computational budget and implementation details. It also outlines the evaluation protocol for comparing alternative judge configurations. We evaluate the judge reliability harness by applying it to characterize the reliability of four LLM judges across four benchmark datasets. The experiments d

证明与未证明：证据只支持上述 paper-specific workload 内的机制/测量关系；不支持把作者结果外推为其他模型、数据、硬件、精度、长度、batch、并发或 production SLO 的通用结论。

Trade-off、failure 与共存边界：系统性压力测试增加样本与人审成本；探索性排序可用单 judge，发布结论需多证据。 反证/限制定位为 `S6 — 6 Discussion`；用于核对的原文摘录：6 Discussion The empirical findings highlight a fundamental tension in the current evaluation ecosystem: although LLM judges are now central to benchmarking and research workflows, their reliability varies sharply across tasks, perturbation families, and model choices. Several clear patterns emerge from our stress tests. Judge output robustness is highly task-dependent. Models that appear stable in binary safety-clas

Artifact / implementation：exact-v1 `S4 — 4 Experiments`；公开范围摘录：4 Experiments This section describes the experimental setup used to evaluate the Judge Reliability Harness. We specify the benchmarks, rubrics, and model judges considered, the configuration of the reliability tests, and the computational budget and implementation details. It also outlines the evaluation protocol for comparing alternative judge configuration。未公开的代码、commit、部署配置或复现实验不得由论文叙事反推。

<!-- claim:SF-2026-ARXIV-2603-05399:start -->只接受 arXiv:2603.05399v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。<!-- claim:SF-2026-ARXIV-2603-05399:end -->

Books Comparison：已读 `PLATFORM-EVALUATION-SYSTEM` 的 `books/part-06-ai-infrastructure/66-evaluation-system.md#从答案评分到可执行证据 (line 930)` 及相邻 `books/part-06-ai-infrastructure/65-kai-scheduler.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/67-monitoring.md#本章要回答的问题 (line 10)`；现有命题为“把每语言生成能耗与 accuracy、tokenization expansion 分开记录；evaluation/model card 需声明 per-language energy，而不能用英语平均值代表多语言部署。 Hardness Adjusted Transfer 以 target performance 相对 source-language ability 校正，避免把 source accuracy 提升误报成 cross-lingual transfer 进步。 selective prediction 除 calibration/ranking 还要报告 score granularity：可用阈值数量决定 operator 能选择多少风险工作点；多查询扩大分辨率但增加成本且可能伤害强模型排序。”。Decision=`No Change — Existing Coverage`；该 author-side 判断仍待fresh-context Books reviewer，Integrate 项只进入日期队列。
<!-- review:SF-2026-ARXIV-2603-05399:end -->

<!-- review:SF-2026-ARXIV-2603-04814:start -->
#### Beyond the Context Window: A Cost-Performance Analysis of Fact-Based Memory vs. Long-Context LLMs for Persistent Agents

问题与 changed constraint：持久 Agent 既可反复发送完整历史，也可抽取事实到 memory；只比较回答质量会掩盖 token、延迟和写入损失。

旧路径为何合理：在该约束未出现、规模较小或 workload 更稳定时，论文所比较的旧路径仍以更少状态、更短控制链和更成熟实现提供合理基线；不能因本论文出现而静默覆盖。

机制、state/data/control owner：工作在同一任务上联合比较 long-context 与 fact memory 的成本、检索和质量，形成 architecture selection contract。 对应 exact-v1 `S3 — 3 Methodology`；该机制由 `AGENT-MEMORY` 承载。原文定位摘录仅作核对：3 Methodology We conducted a comparative study to evaluate the performance and economic feasibility of fact-based memory systems against long-context LLMs. This section outlines the architectural setup of our memory baseline, the datasets employed, the evaluation metrics, and the framework for our cost-performance analysis. 3.1 Memory System Baseline (Mem0) The memory-augmented baseline was implemented using the Mem0 Open Source framework Chhikara et al. (2025) with a custom configuration. The system architecture c

Evaluation contract：结果绑定 Mem0、模型、历史长度和任务；不证明事实抽取对开放对话始终无损。 exact-v1 定位为 `S4 — 4 Experiments and Results`；用于核对的原文摘录：4 Experiments and Results We evaluate the memory system and the long-context baselines along two dimensions: accuracy on factual recall tasks and cost as a function of interaction volume. All models and pricing details are described in Sections 3.1, 3.2 and 3.5. 4.1 Accuracy Results Table 3 reports accuracy across the three evaluation datasets for the Memory System (Mem0), LC GPT-5-mini, and LC GPT-OSS-120B. Dataset Memory System LC GPT-5-mini LC GPT-OSS-120B LoCoMo 57.68 92.85 81.69 PersonaMem v2 62.48 69.75 60.50

证明与未证明：证据只支持上述 paper-specific workload 内的机制/测量关系；不支持把作者结果外推为其他模型、数据、硬件、精度、长度、batch、并发或 production SLO 的通用结论。

Trade-off、failure 与共存边界：结构化 memory 降低重复 context 成本，却引入 extraction/retrieval errors；短会话或高保真需求仍适合 full context。 反证/限制定位为 `S5.SS2 — 5.2 Limitations`；用于核对的原文摘录：5.2 Limitations Single memory architecture. This study uses Mem0’s flat-typed extraction pipeline as the sole memory baseline Chhikara et al. (2025). More structured approaches—such as temporal semantic memory Su et al. (2026), or hierarchical engram-based systems Hu et al. (2026)—may recover recall that flat extraction loses, and could alter the accuracy comparison. The findings reported here characterize the accura

Artifact / implementation：exact-v1 `Not Disclosed — arXiv:2603.04814v1 exposes no dedicated Artifact / implementation section in the recovered exact-v1 body`；公开范围摘录：Not Disclosed。未公开的代码、commit、部署配置或复现实验不得由论文叙事反推。

<!-- claim:SF-2026-ARXIV-2603-04814:start -->只接受 arXiv:2603.04814v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。<!-- claim:SF-2026-ARXIV-2603-04814:end -->

Books Comparison：已读 `AGENT-MEMORY` 的 `books/part-07-agent/77-memory.md#Memory Read 是受约束检索 (line 265)` 及相邻 `books/part-07-agent/76-rag.md#本章要回答的问题 (line 10); books/part-07-agent/78-tool-calling.md#本章要回答的问题 (line 10)`；现有命题为“Late construction 把不可逆信息损失延后，却增加每次查询的计算、judge/calibration 漂移和并发更新一致性；它也没有消除 deletion propagation、ACL 或 freshness 问题。查询重复且 schema 稳定时，预计算 summary 仍可能更便宜；高风险回答还应让最终 claim 回指 raw evidence。现有 LongMemEval/LoCoMo 结果只支持作者 workload 下的 accuracy/context trade-off，不证明更低的全生命周期成本。”。Decision=`No Change — Existing Coverage`；该 author-side 判断仍待fresh-context Books reviewer，Integrate 项只进入日期队列。
<!-- review:SF-2026-ARXIV-2603-04814:end -->

<!-- review:SF-2026-ARXIV-2603-04896:start -->
#### Authorize-on-Demand: Dynamic Authorization with Legality-Aware Intellectual Property Protection for VLMs

问题与 changed constraint：模型 IP 保护若只在训练时嵌入静态水印，无法随部署域、许可状态和用户 authority 动态改变。

旧路径为何合理：在该约束未出现、规模较小或 workload 更稳定时，论文所比较的旧路径仍以更少状态、更短控制链和更成熟实现提供合理基线；不能因本论文出现而静默覆盖。

机制、state/data/control owner：Authorize-on-Demand 把 legality context 与运行时授权决策连接，使同一 VLM 的可用能力受可撤销 policy 控制。 对应 exact-v1 `S3 — 3 Method`；该机制由 `PLATFORM-SECURITY` 承载。原文定位摘录仅作核对：3 Method Figure 2: (a) During training, authorized data (), extended data (), and unauthorized data () are simultaneously processed by the frozen CLIP visual encoder to extract visual features (, , ). The image projector and domain projector generate image tokens () and domain-discriminative tokens () for the three domains, respectively. In parallel, an encryption projector produces a credential token for authorized data. These tokens are concatenated and fed into the frozen text encoder , producing the correspondi

Evaluation contract：结果只支持作者授权任务与攻击；不证明 watermark/门控可抵抗模型抽取或权重修改。 exact-v1 定位为 `S4 — 4 Experiment`；用于核对的原文摘录：4 Experiment 4.1 Implementation Details We comprehensively evaluate the effectiveness of the proposed AoD-IP framework against SOTA methods [37, 35, 33, 15, 12, 34] on multiple public benchmarks: • Office-31 [26] contains images from three domains, namely Amazon (Am), Dslr (Ds), and Webcam (We), covering 31 object categories with more than 4,000 images. • Office-Home-65 [31] consists of four visually distinct domains, including Art (Ar), Clipart (Cl), Product (Pr), and Real-World (Re), spanning 65 categories and ov

证明与未证明：证据只支持上述 paper-specific workload 内的机制/测量关系；不支持把作者结果外推为其他模型、数据、硬件、精度、长度、batch、并发或 production SLO 的通用结论。

Trade-off、failure 与共存边界：动态授权增加可撤销性，却引入 policy availability、误拒和 bypass 面；封闭环境可使用部署级 ACL。 反证/限制定位为 `S5 — 5 Conclusion`；用于核对的原文摘录：5 Conclusion The rapid advancement of VLMs has raised growing concerns over model intellectual property (IP) security. We propose (AoD-IP), a novel dynamic authorization framework that introduces a lightweight authorization module for flexible, user-controlled authorization and a dual-path inference strategy for simultaneous legality verification and task prediction. Experiments demonstrate that AoD-IP delivers robus

Artifact / implementation：exact-v1 `S4.SS1 — 4.1 Implementation Details`；公开范围摘录：4.1 Implementation Details We comprehensively evaluate the effectiveness of the proposed AoD-IP framework against SOTA methods [37, 35, 33, 15, 12, 34] on multiple public benchmarks: • Office-31 [26] contains images from three domains, namely Amazon (Am), Dslr (Ds), and Webcam (We), covering 31 object categories with more than 4,000 images. • Office-Home-65。未公开的代码、commit、部署配置或复现实验不得由论文叙事反推。

<!-- claim:SF-2026-ARXIV-2603-04896:start -->只接受 arXiv:2603.04896v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。<!-- claim:SF-2026-ARXIV-2603-04896:end -->

Books Comparison：已读 `PLATFORM-SECURITY` 的 `books/part-06-ai-infrastructure/72-security.md#风险管理而不是一次性认证 (line 1091)` 及相邻 `books/part-06-ai-infrastructure/71-multi-tenant.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/73-production-best-practice.md#本章要回答的问题 (line 10)`；现有命题为“- `SF-2026-ARXIV-2606-22019` — primary `arXiv:2606.22019v1`；exact-v1 URL=`https://arxiv.org/html/2606.22019v1`；Method=`https://arxiv.org/html/2606.22019v1 — §2 Audit model: carriers, screens, and ablations; §6 The audit lifecycle: which handle is sound in which channel?`；Evaluation=`https://arxiv.org/html/2606.22019v1 — §3 A controlled body channel is screenable: coverage predicts transfer; §4 Vocabulary-carried token traits evade initialization-alignment screens; §5 The carrier is signal-dependent, and moving it m”。Decision=`No Change — Existing Coverage`；该 author-side 判断仍待fresh-context Books reviewer，Integrate 项只进入日期队列。
<!-- review:SF-2026-ARXIV-2603-04896:end -->

## 4. Benchmark Contracts

None — 本日报不把作者结果或摘要数字重标为可跨 workload 外推的 benchmark claim。

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-04402 | score_7_9 | selected | DA-20260307-1 | — | 从完整 eligibility frontier 中优先覆盖独立 owner 的 durable state/control 或 evaluation contract 变化。 | analysis:DA-20260307-1 |
| SF-2026-ARXIV-2603-04424 | score_7_9 | selected | DA-20260307-2 | — | 从完整 eligibility frontier 中优先覆盖独立 owner 的 durable state/control 或 evaluation contract 变化。 | analysis:DA-20260307-2 |
| SF-2026-ARXIV-2603-04428 | score_7_9 | selected | DA-20260307-3 | — | 从完整 eligibility frontier 中优先覆盖独立 owner 的 durable state/control 或 evaluation contract 变化。 | analysis:DA-20260307-3 |
| SF-2026-ARXIV-2603-04443 | score_7_9 | not_selected | — | — | Full Source Review 已完成；相对三个叙事单元，其机制由相同 owner 或较窄 workload 承载。 | analysis-decision:SF-2026-ARXIV-2603-04443 |
| SF-2026-ARXIV-2603-04444 | score_7_9 | not_selected | — | — | Full Source Review 已完成；相对三个叙事单元，其机制由相同 owner 或较窄 workload 承载。 | analysis-decision:SF-2026-ARXIV-2603-04444 |
| SF-2026-ARXIV-2603-04448 | score_7_9 | not_selected | — | — | Full Source Review 已完成；相对三个叙事单元，其机制由相同 owner 或较窄 workload 承载。 | analysis-decision:SF-2026-ARXIV-2603-04448 |
| SF-2026-ARXIV-2603-04459 | score_7_9 | not_selected | — | — | Full Source Review 已完成；相对三个叙事单元，其机制由相同 owner 或较窄 workload 承载。 | analysis-decision:SF-2026-ARXIV-2603-04459 |
| SF-2026-ARXIV-2603-04460 | score_7_9 | not_selected | — | — | Full Source Review 已完成；相对三个叙事单元，其机制由相同 owner 或较窄 workload 承载。 | analysis-decision:SF-2026-ARXIV-2603-04460 |
| SF-2026-ARXIV-2603-04469 | score_7_9 | not_selected | — | — | Full Source Review 已完成；相对三个叙事单元，其机制由相同 owner 或较窄 workload 承载。 | analysis-decision:SF-2026-ARXIV-2603-04469 |
| SF-2026-ARXIV-2603-04797 | score_7_9 | not_selected | — | — | Full Source Review 已完成；相对三个叙事单元，其机制由相同 owner 或较窄 workload 承载。 | analysis-decision:SF-2026-ARXIV-2603-04797 |
| SF-2026-ARXIV-2603-04902 | score_7_9 | not_selected | — | — | Full Source Review 已完成；相对三个叙事单元，其机制由相同 owner 或较窄 workload 承载。 | analysis-decision:SF-2026-ARXIV-2603-04902 |
| SF-2026-ARXIV-2603-04910 | score_7_9 | not_selected | — | — | Full Source Review 已完成；相对三个叙事单元，其机制由相同 owner 或较窄 workload 承载。 | analysis-decision:SF-2026-ARXIV-2603-04910 |
| SF-2026-ARXIV-2603-04981 | score_7_9 | not_selected | — | — | Full Source Review 已完成；相对三个叙事单元，其机制由相同 owner 或较窄 workload 承载。 | analysis-decision:SF-2026-ARXIV-2603-04981 |
| SF-2026-ARXIV-2603-05031 | score_7_9 | not_selected | — | — | Full Source Review 已完成；相对三个叙事单元，其机制由相同 owner 或较窄 workload 承载。 | analysis-decision:SF-2026-ARXIV-2603-05031 |
| SF-2026-ARXIV-2603-05185 | score_7_9 | not_selected | — | — | Full Source Review 已完成；相对三个叙事单元，其机制由相同 owner 或较窄 workload 承载。 | analysis-decision:SF-2026-ARXIV-2603-05185 |
| SF-2026-ARXIV-2603-05438 | score_7_9 | not_selected | — | — | Full Source Review 已完成；相对三个叙事单元，其机制由相同 owner 或较窄 workload 承载。 | analysis-decision:SF-2026-ARXIV-2603-05438 |
| SF-2026-ARXIV-2603-05451 | score_7_9 | not_selected | — | — | Full Source Review 已完成；相对三个叙事单元，其机制由相同 owner 或较窄 workload 承载。 | analysis-decision:SF-2026-ARXIV-2603-05451 |
| SF-2026-ARXIV-2603-05454 | score_7_9 | not_selected | — | — | Full Source Review 已完成；相对三个叙事单元，其机制由相同 owner 或较窄 workload 承载。 | analysis-decision:SF-2026-ARXIV-2603-05454 |
| SF-2026-ARXIV-2603-04411 | score_7_9 | not_selected | — | — | Full Source Review 已完成；相对三个叙事单元，其机制由相同 owner 或较窄 workload 承载。 | analysis-decision:SF-2026-ARXIV-2603-04411 |
| SF-2026-ARXIV-2603-04417 | score_7_9 | not_selected | — | — | Full Source Review 已完成；相对三个叙事单元，其机制由相同 owner 或较窄 workload 承载。 | analysis-decision:SF-2026-ARXIV-2603-04417 |
| SF-2026-ARXIV-2603-04427 | score_7_9 | not_selected | — | — | Full Source Review 已完成；相对三个叙事单元，其机制由相同 owner 或较窄 workload 承载。 | analysis-decision:SF-2026-ARXIV-2603-04427 |
| SF-2026-ARXIV-2603-04621 | score_7_9 | not_selected | — | — | Full Source Review 已完成；相对三个叙事单元，其机制由相同 owner 或较窄 workload 承载。 | analysis-decision:SF-2026-ARXIV-2603-04621 |
| SF-2026-ARXIV-2603-04656 | score_7_9 | not_selected | — | — | Full Source Review 已完成；相对三个叙事单元，其机制由相同 owner 或较窄 workload 承载。 | analysis-decision:SF-2026-ARXIV-2603-04656 |
| SF-2026-ARXIV-2603-04851 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | Full Source Review 已完成；相对三个叙事单元，其机制由相同 owner 或较窄 workload 承载。 | analysis-decision:SF-2026-ARXIV-2603-04851 |
| SF-2026-ARXIV-2603-05087 | score_7_9 | not_selected | — | — | Full Source Review 已完成；相对三个叙事单元，其机制由相同 owner 或较窄 workload 承载。 | analysis-decision:SF-2026-ARXIV-2603-05087 |
| SF-2026-ARXIV-2603-05147 | score_7_9 | not_selected | — | — | Full Source Review 已完成；相对三个叙事单元，其机制由相同 owner 或较窄 workload 承载。 | analysis-decision:SF-2026-ARXIV-2603-05147 |
| SF-2026-ARXIV-2603-05210 | score_7_9 | not_selected | — | — | Full Source Review 已完成；相对三个叙事单元，其机制由相同 owner 或较窄 workload 承载。 | analysis-decision:SF-2026-ARXIV-2603-05210 |
| SF-2026-ARXIV-2603-05353 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | Full Source Review 已完成；相对三个叙事单元，其机制由相同 owner 或较窄 workload 承载。 | analysis-decision:SF-2026-ARXIV-2603-05353 |
| SF-2026-ARXIV-2603-05399 | score_7_9 | not_selected | — | — | Full Source Review 已完成；相对三个叙事单元，其机制由相同 owner 或较窄 workload 承载。 | analysis-decision:SF-2026-ARXIV-2603-05399 |
| SF-2026-ARXIV-2603-04814 | score_7_9 | not_selected | — | — | Full Source Review 已完成；相对三个叙事单元，其机制由相同 owner 或较窄 workload 承载。 | analysis-decision:SF-2026-ARXIV-2603-04814 |
| SF-2026-ARXIV-2603-04896 | score_7_9 | not_selected | — | — | Full Source Review 已完成；相对三个叙事单元，其机制由相同 owner 或较窄 workload 承载。 | analysis-decision:SF-2026-ARXIV-2603-04896 |

<!-- analysis:DA-20260307-1:start -->
### DA-20260307-1 — SearchGym: A Modular Infrastructure for Cross-Platform Benchmarking and Hybrid Search Orchestration

旧路径在 changed constraint 未出现时仍然合理；该工作把新的状态、数据或控制责任交给 `PLATFORM-EVALUATION-SYSTEM`。exact-v1 机制为：SearchGym 提供模块化平台 adapter、统一 trace 和 hybrid search orchestration，使跨平台实验共享 contract。 证据只证明作者 evaluation contract，不能外推未披露配置。代价、failure 与下一重压力受以下边界约束：只接受 arXiv:2603.04402v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。
<!-- analysis:DA-20260307-1:end -->

<!-- analysis:DA-20260307-2:start -->
### DA-20260307-2 — When Scaling Fails: Network and Fabric Effects on Distributed GPU Training Performance

旧路径在 changed constraint 未出现时仍然合理；该工作把新的状态、数据或控制责任交给 `TRAIN-DISTRIBUTED-TRAINING`。exact-v1 机制为：论文把网络/fabric 事件与训练 step/collective trace 对齐，定位何时 topology 成为训练 owner 约束。 证据只证明作者 evaluation contract，不能外推未披露配置。代价、failure 与下一重压力受以下边界约束：只接受 arXiv:2603.04424v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。
<!-- analysis:DA-20260307-2:end -->

<!-- analysis:DA-20260307-3:start -->
### DA-20260307-3 — Agent Memory Below the Prompt: Persistent Q4 KV Cache for Multi-Agent LLM Inference on Edge Devices

旧路径在 changed constraint 未出现时仍然合理；该工作把新的状态、数据或控制责任交给 `AGENT-MEMORY`。exact-v1 机制为：论文将持久 Q4 KV 作为 prompt 下方的 agent memory，并管理跨 agent/session 的缓存 identity。 证据只证明作者 evaluation contract，不能外推未披露配置。代价、failure 与下一重压力受以下边界约束：只接受 arXiv:2603.04428v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。
<!-- analysis:DA-20260307-3:end -->

<!-- analysis-decision:SF-2026-ARXIV-2603-04443:start -->
`AMV-L: Lifecycle-Managed Agent Memory for Tail-Latency Control in Long-Running LLM Systems` 已完成 full review，但不占用有限叙事单元；这不改变它的 Review Completion。
<!-- analysis-decision:SF-2026-ARXIV-2603-04443:end -->

<!-- analysis-decision:SF-2026-ARXIV-2603-04444:start -->
`vLLM Semantic Router: Signal Driven Decision Routing for Mixture-of-Modality Models` 已完成 full review，但不占用有限叙事单元；这不改变它的 Review Completion。
<!-- analysis-decision:SF-2026-ARXIV-2603-04444:end -->

<!-- analysis-decision:SF-2026-ARXIV-2603-04448:start -->
`SkillNet: Create, Evaluate, and Connect AI Skills` 已完成 full review，但不占用有限叙事单元；这不改变它的 Review Completion。
<!-- analysis-decision:SF-2026-ARXIV-2603-04448:end -->

<!-- analysis-decision:SF-2026-ARXIV-2603-04459:start -->
`Benchmark of Benchmarks: Unpacking Influence and Code Repository Quality in LLM Safety Benchmarks` 已完成 full review，但不占用有限叙事单元；这不改变它的 Review Completion。
<!-- analysis-decision:SF-2026-ARXIV-2603-04459:end -->

<!-- analysis-decision:SF-2026-ARXIV-2603-04460:start -->
`VSPrefill: Vertical-Slash Sparse Attention with Lightweight Indexing for Long-Context Prefilling` 已完成 full review，但不占用有限叙事单元；这不改变它的 Review Completion。
<!-- analysis-decision:SF-2026-ARXIV-2603-04460:end -->

<!-- analysis-decision:SF-2026-ARXIV-2603-04469:start -->
`Cross-Layer Semantic Flow Reconstruction for Attack Detection in Agentic Systems` 已完成 full review，但不占用有限叙事单元；这不改变它的 Review Completion。
<!-- analysis-decision:SF-2026-ARXIV-2603-04469:end -->

<!-- analysis-decision:SF-2026-ARXIV-2603-04797:start -->
`Hardware-Software Co-design for 3D-DRAM-based LLM Serving Accelerator` 已完成 full review，但不占用有限叙事单元；这不改变它的 Review Completion。
<!-- analysis-decision:SF-2026-ARXIV-2603-04797:end -->

<!-- analysis-decision:SF-2026-ARXIV-2603-04902:start -->
`AgentSCOPE: Evaluating Contextual Privacy Across Agentic Workflows` 已完成 full review，但不占用有限叙事单元；这不改变它的 Review Completion。
<!-- analysis-decision:SF-2026-ARXIV-2603-04902:end -->

<!-- analysis-decision:SF-2026-ARXIV-2603-04910:start -->
`VPWEM: Non-Markovian Visuomotor Policy with Working and Episodic Memory` 已完成 full review，但不占用有限叙事单元；这不改变它的 Review Completion。
<!-- analysis-decision:SF-2026-ARXIV-2603-04910:end -->

<!-- analysis-decision:SF-2026-ARXIV-2603-04981:start -->
`Rethinking Representativeness and Diversity in Dynamic Data Selection` 已完成 full review，但不占用有限叙事单元；这不改变它的 Review Completion。
<!-- analysis-decision:SF-2026-ARXIV-2603-04981:end -->

<!-- analysis-decision:SF-2026-ARXIV-2603-05031:start -->
`AegisUI: Behavioral Anomaly Detection for Structured User Interface Protocols in AI Agent Systems` 已完成 full review，但不占用有限叙事单元；这不改变它的 Review Completion。
<!-- analysis-decision:SF-2026-ARXIV-2603-05031:end -->

<!-- analysis-decision:SF-2026-ARXIV-2603-05185:start -->
`Critic in the Loop: A Tri-System VLA Framework for Robust Long-Horizon Manipulation` 已完成 full review，但不占用有限叙事单元；这不改变它的 Review Completion。
<!-- analysis-decision:SF-2026-ARXIV-2603-05185:end -->

<!-- analysis-decision:SF-2026-ARXIV-2603-05438:start -->
`Planning in 8 Tokens: A Compact Discrete Tokenizer for Latent World Model` 已完成 full review，但不占用有限叙事单元；这不改变它的 Review Completion。
<!-- analysis-decision:SF-2026-ARXIV-2603-05438:end -->

<!-- analysis-decision:SF-2026-ARXIV-2603-05451:start -->
`FlashAttention-4: Algorithm and Kernel Pipelining Co-Design for Asymmetric Hardware Scaling` 已完成 full review，但不占用有限叙事单元；这不改变它的 Review Completion。
<!-- analysis-decision:SF-2026-ARXIV-2603-05451:end -->

<!-- analysis-decision:SF-2026-ARXIV-2603-05454:start -->
`Beyond Scattered Acceptance: Fast and Coherent Inference for DLMs via Longest Stable Prefixes` 已完成 full review，但不占用有限叙事单元；这不改变它的 Review Completion。
<!-- analysis-decision:SF-2026-ARXIV-2603-05454:end -->

<!-- analysis-decision:SF-2026-ARXIV-2603-04411:start -->
`One Size Does Not Fit All: Token-Wise Adaptive Compression for KV Cache` 已完成 full review，但不占用有限叙事单元；这不改变它的 Review Completion。
<!-- analysis-decision:SF-2026-ARXIV-2603-04411:end -->

<!-- analysis-decision:SF-2026-ARXIV-2603-04417:start -->
`Same Input, Different Scores: A Multi Model Study on the Inconsistency of LLM Judge` 已完成 full review，但不占用有限叙事单元；这不改变它的 Review Completion。
<!-- analysis-decision:SF-2026-ARXIV-2603-04417:end -->

<!-- analysis-decision:SF-2026-ARXIV-2603-04427:start -->
`Thin Keys, Full Values: Reducing KV Cache via Low-Dimensional Attention Selection` 已完成 full review，但不占用有限叙事单元；这不改变它的 Review Completion。
<!-- analysis-decision:SF-2026-ARXIV-2603-04427:end -->

<!-- analysis-decision:SF-2026-ARXIV-2603-04621:start -->
`DuaLip-GPU Technical Report` 已完成 full review，但不占用有限叙事单元；这不改变它的 Review Completion。
<!-- analysis-decision:SF-2026-ARXIV-2603-04621:end -->

<!-- analysis-decision:SF-2026-ARXIV-2603-04656:start -->
`iAgentBench: Benchmarking Sensemaking Capabilities of Information-Seeking Agents on High-Traffic Topics` 已完成 full review，但不占用有限叙事单元；这不改变它的 Review Completion。
<!-- analysis-decision:SF-2026-ARXIV-2603-04656:end -->

<!-- analysis-decision:SF-2026-ARXIV-2603-04851:start -->
`Why Is RLHF Alignment Shallow? A Gradient Analysis` 已完成 full review，但不占用有限叙事单元；这不改变它的 Review Completion。
<!-- analysis-decision:SF-2026-ARXIV-2603-04851:end -->

<!-- analysis-decision:SF-2026-ARXIV-2603-05087:start -->
`PromptTuner: SLO-Aware Elastic System for LLM Prompt Tuning` 已完成 full review，但不占用有限叙事单元；这不改变它的 Review Completion。
<!-- analysis-decision:SF-2026-ARXIV-2603-05087:end -->

<!-- analysis-decision:SF-2026-ARXIV-2603-05147:start -->
`Act, Think or Abstain: Complexity-Aware Adaptive Inference for Vision-Language-Action Models` 已完成 full review，但不占用有限叙事单元；这不改变它的 Review Completion。
<!-- analysis-decision:SF-2026-ARXIV-2603-05147:end -->

<!-- analysis-decision:SF-2026-ARXIV-2603-05210:start -->
`Balancing Coverage and Draft Latency in Vocabulary Trimming for Faster Speculative Decoding` 已完成 full review，但不占用有限叙事单元；这不改变它的 Review Completion。
<!-- analysis-decision:SF-2026-ARXIV-2603-05210:end -->

<!-- analysis-decision:SF-2026-ARXIV-2603-05353:start -->
`InfoFlow KV: Information-Flow-Aware KV Recomputation for Long Context` 已完成 full review，但不占用有限叙事单元；这不改变它的 Review Completion。
<!-- analysis-decision:SF-2026-ARXIV-2603-05353:end -->

<!-- analysis-decision:SF-2026-ARXIV-2603-05399:start -->
`Judge Reliability Harness: Stress Testing the Reliability of LLM Judges` 已完成 full review，但不占用有限叙事单元；这不改变它的 Review Completion。
<!-- analysis-decision:SF-2026-ARXIV-2603-05399:end -->

<!-- analysis-decision:SF-2026-ARXIV-2603-04814:start -->
`Beyond the Context Window: A Cost-Performance Analysis of Fact-Based Memory vs. Long-Context LLMs for Persistent Agents` 已完成 full review，但不占用有限叙事单元；这不改变它的 Review Completion。
<!-- analysis-decision:SF-2026-ARXIV-2603-04814:end -->

<!-- analysis-decision:SF-2026-ARXIV-2603-04896:start -->
`Authorize-on-Demand: Dynamic Authorization with Legality-Aware Intellectual Property Protection for VLMs` 已完成 full review，但不占用有限叙事单元；这不改变它的 Review Completion。
<!-- analysis-decision:SF-2026-ARXIV-2603-04896:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-04402 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#从答案评分到可执行证据 (line 936) | books/part-06-ai-infrastructure/65-kai-scheduler.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/67-monitoring.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2603-04402 | delta:SF-2026-ARXIV-2603-04402 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-04402 |
| SF-2026-ARXIV-2603-04424 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#从本机协作到分布式执行 (line 65) | books/part-04-training-system/35-checkpoint.md#本章要回答的问题 (line 10); books/part-04-training-system/37-tensor-parallel.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2603-04424 | delta:SF-2026-ARXIV-2603-04424 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-04424 |
| SF-2026-ARXIV-2603-04428 | AGENT-MEMORY | books/part-07-agent/77-memory.md#本章在知识树中的位置 (line 1191) | books/part-07-agent/76-rag.md#本章要回答的问题 (line 10); books/part-07-agent/78-tool-calling.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2603-04428 | delta:SF-2026-ARXIV-2603-04428 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-04428 |
| SF-2026-ARXIV-2603-04443 | AGENT-MEMORY | books/part-07-agent/77-memory.md#Memory Write 是高风险决策 (line 122) | books/part-07-agent/76-rag.md#本章要回答的问题 (line 10); books/part-07-agent/78-tool-calling.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2603-04443 | delta:SF-2026-ARXIV-2603-04443 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-04443 |
| SF-2026-ARXIV-2603-04444 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#Routing、Placement 与 Autoscaling (line 285) | books/part-05-inference-system/55-pd-disaggregation.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/57-what-is-ai-platform.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2603-04444 | delta:SF-2026-ARXIV-2603-04444 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-04444 |
| SF-2026-ARXIV-2603-04448 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#本章要回答的问题 (line 14) | books/part-07-agent/83-mcp.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2603-04448 | delta:SF-2026-ARXIV-2603-04448 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-04448 |
| SF-2026-ARXIV-2603-04459 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#从答案评分到可执行证据 (line 936) | books/part-06-ai-infrastructure/65-kai-scheduler.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/67-monitoring.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2603-04459 | delta:SF-2026-ARXIV-2603-04459 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-04459 |
| SF-2026-ARXIV-2603-04460 | INFER-PREFILL | books/part-05-inference-system/43-prefill.md#自检问题 (line 365) | books/part-05-inference-system/42-what-happens-during-inference.md#本章要回答的问题 (line 10); books/part-05-inference-system/44-decode.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2603-04460 | delta:SF-2026-ARXIV-2603-04460 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-04460 |
| SF-2026-ARXIV-2603-04469 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#从“文本是否恶意”到“谁获得了行为控制权” (line 336) | books/part-06-ai-infrastructure/71-multi-tenant.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/73-production-best-practice.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2603-04469 | delta:SF-2026-ARXIV-2603-04469 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-04469 |
| SF-2026-ARXIV-2603-04797 | INFER-GPU-MEMORY | books/part-05-inference-system/54-gpu-memory.md#三类缓解路径 (line 306) | books/part-05-inference-system/53-kserve-llm.md#本章要回答的问题 (line 10); books/part-05-inference-system/55-pd-disaggregation.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2603-04797 | delta:SF-2026-ARXIV-2603-04797 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-04797 |
| SF-2026-ARXIV-2603-04902 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#Supply-chain Integrity (line 538) | books/part-06-ai-infrastructure/71-multi-tenant.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/73-production-best-practice.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2603-04902 | delta:SF-2026-ARXIV-2603-04902 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-04902 |
| SF-2026-ARXIV-2603-04910 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#Latency 与 control frequency (line 329) | books/part-03-multimodal-world-models/25-multimodal-world-models.md#本章要回答的问题 (line 10); books/part-04-training-system/27-data.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2603-04910 | delta:SF-2026-ARXIV-2603-04910 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-04910 |
| SF-2026-ARXIV-2603-04981 | TRAIN-DATA | books/part-04-training-system/27-data.md#Data lineage 是训练可复现性的前提 (line 562) | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#本章要回答的问题 (line 10); books/part-04-training-system/28-pretraining.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2603-04981 | delta:SF-2026-ARXIV-2603-04981 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-04981 |
| SF-2026-ARXIV-2603-05031 | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#模型输出只是 Proposal (line 72) | books/part-07-agent/77-memory.md#本章要回答的问题 (line 10); books/part-07-agent/79-planning.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2603-05031 | delta:SF-2026-ARXIV-2603-05031 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05031 |
| SF-2026-ARXIV-2603-05185 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#Edge 与云的分层 (line 499) | books/part-03-multimodal-world-models/25-multimodal-world-models.md#本章要回答的问题 (line 10); books/part-04-training-system/27-data.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2603-05185 | delta:SF-2026-ARXIV-2603-05185 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05185 |
| SF-2026-ARXIV-2603-05438 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#从机制演进到系统设计 (line 640) | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#本章要回答的问题 (line 10); books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2603-05438 | delta:SF-2026-ARXIV-2603-05438 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05438 |
| SF-2026-ARXIV-2603-05451 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#TMA 解决搬运，不负责矩阵计算 (line 341) | books/part-05-inference-system/48-speculative-decoding.md#本章要回答的问题 (line 10); books/part-05-inference-system/50-vllm.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2603-05451 | delta:SF-2026-ARXIV-2603-05451 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05451 |
| SF-2026-ARXIV-2603-05454 | MULTIMODAL-GENERATIVE-PARADIGMS | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#本章要回答的问题 (line 12) | books/part-03-multimodal-world-models/23-multimodal-representation.md#本章要回答的问题 (line 10); books/part-03-multimodal-world-models/25-multimodal-world-models.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2603-05454 | delta:SF-2026-ARXIV-2603-05454 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05454 |
| SF-2026-ARXIV-2603-04411 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#一致性不变量 (line 773) | books/part-05-inference-system/44-decode.md#本章要回答的问题 (line 10); books/part-05-inference-system/46-continuous-batching.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2603-04411 | delta:SF-2026-ARXIV-2603-04411 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-04411 |
| SF-2026-ARXIV-2603-04417 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#从答案评分到可执行证据 (line 936) | books/part-06-ai-infrastructure/65-kai-scheduler.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/67-monitoring.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2603-04417 | delta:SF-2026-ARXIV-2603-04417 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-04417 |
| SF-2026-ARXIV-2603-04427 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#一致性不变量 (line 885) | books/part-05-inference-system/44-decode.md#本章要回答的问题 (line 10); books/part-05-inference-system/46-continuous-batching.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2603-04427 | delta:SF-2026-ARXIV-2603-04427 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-04427 |
| SF-2026-ARXIV-2603-04621 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#本章要回答的问题 (line 16) | books/part-05-inference-system/48-speculative-decoding.md#本章要回答的问题 (line 10); books/part-05-inference-system/50-vllm.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2603-04621 | delta:SF-2026-ARXIV-2603-04621 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-04621 |
| SF-2026-ARXIV-2603-04656 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#Scorer 不是绝对真相 (line 1719) | books/part-06-ai-infrastructure/65-kai-scheduler.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/67-monitoring.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2603-04656 | delta:SF-2026-ARXIV-2603-04656 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-04656 |
| SF-2026-ARXIV-2603-04851 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#Harm Horizon：Sequence Reward 的 Gradient 可能天然局部 (line 244) | books/part-04-training-system/30-lora.md#本章要回答的问题 (line 10); books/part-04-training-system/32-ppo.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2603-04851 | delta:SF-2026-ARXIV-2603-04851 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2603-04851 |
| SF-2026-ARXIV-2603-05087 | PLATFORM-GPU-SCHEDULER | books/part-06-ai-infrastructure/63-gpu-scheduler.md#与推理 Scheduler 的边界 (line 243) | books/part-06-ai-infrastructure/62-gateway.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/64-volcano.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2603-05087 | delta:SF-2026-ARXIV-2603-05087 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05087 |
| SF-2026-ARXIV-2603-05147 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#从模块化机器人到 VLA (line 90) | books/part-03-multimodal-world-models/25-multimodal-world-models.md#本章要回答的问题 (line 10); books/part-04-training-system/27-data.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2603-05147 | delta:SF-2026-ARXIV-2603-05147 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05147 |
| SF-2026-ARXIV-2603-05210 | INFER-SPECULATIVE-DECODING | books/part-05-inference-system/48-speculative-decoding.md#本章要回答的问题 (line 16) | books/part-05-inference-system/47-pagedattention.md#本章要回答的问题 (line 10); books/part-05-inference-system/49-tensorrt-llm.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2603-05210 | delta:SF-2026-ARXIV-2603-05210 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05210 |
| SF-2026-ARXIV-2603-05353 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#Structured knowledge 只有进入 physical access plan 才改变 KV 成本 (line 152) | books/part-05-inference-system/44-decode.md#本章要回答的问题 (line 10); books/part-05-inference-system/46-continuous-batching.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2603-05353 | delta:SF-2026-ARXIV-2603-05353 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2603-05353 |
| SF-2026-ARXIV-2603-05399 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#从答案评分到可执行证据 (line 930) | books/part-06-ai-infrastructure/65-kai-scheduler.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/67-monitoring.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2603-05399 | delta:SF-2026-ARXIV-2603-05399 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05399 |
| SF-2026-ARXIV-2603-04814 | AGENT-MEMORY | books/part-07-agent/77-memory.md#Memory Read 是受约束检索 (line 265) | books/part-07-agent/76-rag.md#本章要回答的问题 (line 10); books/part-07-agent/78-tool-calling.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2603-04814 | delta:SF-2026-ARXIV-2603-04814 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-04814 |
| SF-2026-ARXIV-2603-04896 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#风险管理而不是一次性认证 (line 1091) | books/part-06-ai-infrastructure/71-multi-tenant.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/73-production-best-practice.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2603-04896 | delta:SF-2026-ARXIV-2603-04896 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-04896 |

<!-- existing:SF-2026-ARXIV-2603-04402:start -->
author-side 已读 current owner `PLATFORM-EVALUATION-SYSTEM` 的具体命题：- `SF-2026-ARXIV-2606-21869` — primary `arXiv:2606.21869v1`；exact-v1 URL=`https://arxiv.org/html/2606.21869v1`；Method=`https://arxiv.org/html/2606.21869v1 — §3 Preliminaries — Energy Consumption and Measurement; Multilingual Dataset`；Evaluation=`https://arxiv.org/html/2606.21869v1 — §4 Results and Analysis — Common Setup; §4.1–§4.4; Appendix B Experimental Setups`；Non-proof=`https://arxiv.org/html/2606.21869v1 — §6 Conclusion; Environmental impact of this study; Translation quality and representation; Recommendatio
<!-- existing:SF-2026-ARXIV-2603-04402:end -->

<!-- delta:SF-2026-ARXIV-2603-04402:start -->
SearchGym 提供模块化平台 adapter、统一 trace 和 hybrid search orchestration，使跨平台实验共享 contract。
<!-- delta:SF-2026-ARXIV-2603-04402:end -->

<!-- books-review:SF-2026-ARXIV-2603-04402:start -->
Decision=`No Change — Existing Coverage`；owner=`PLATFORM-EVALUATION-SYSTEM`；target=`books/part-06-ai-infrastructure/66-evaluation-system.md#从答案评分到可执行证据 (line 936)`；adjacent=`books/part-06-ai-infrastructure/65-kai-scheduler.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/67-monitoring.md#本章要回答的问题 (line 10)`。证据边界：只接受 arXiv:2603.04402v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。 该判断尚未由 fresh-context Books reviewer 接受；Integrate 项只进入日期 queue，不写共享 Books。
<!-- books-review:SF-2026-ARXIV-2603-04402:end -->

<!-- existing:SF-2026-ARXIV-2603-04424:start -->
author-side 已读 current owner `TRAIN-DISTRIBUTED-TRAINING` 的具体命题：MPI 把问题提升为并行程序的执行模型。它定义 process/rank、communicator、point-to-point、collective、topology、one-sided communication 等语义，使程序描述“哪些 participants 对哪些数据共同完成什么操作”。MPI implementation 可以选择 shared memory、network transport 或 accelerator-aware path；能否直接处理 device buffer 取决于具体 implementation 和构建能力，不能从 MPI 标准名称本身推出。
<!-- existing:SF-2026-ARXIV-2603-04424:end -->

<!-- delta:SF-2026-ARXIV-2603-04424:start -->
论文把网络/fabric 事件与训练 step/collective trace 对齐，定位何时 topology 成为训练 owner 约束。
<!-- delta:SF-2026-ARXIV-2603-04424:end -->

<!-- books-review:SF-2026-ARXIV-2603-04424:start -->
Decision=`No Change — Existing Coverage`；owner=`TRAIN-DISTRIBUTED-TRAINING`；target=`books/part-04-training-system/36-distributed-training.md#从本机协作到分布式执行 (line 65)`；adjacent=`books/part-04-training-system/35-checkpoint.md#本章要回答的问题 (line 10); books/part-04-training-system/37-tensor-parallel.md#本章要回答的问题 (line 10)`。证据边界：只接受 arXiv:2603.04424v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。 该判断尚未由 fresh-context Books reviewer 接受；Integrate 项只进入日期 queue，不写共享 Books。
<!-- books-review:SF-2026-ARXIV-2603-04424:end -->

<!-- existing:SF-2026-ARXIV-2603-04428:start -->
author-side 已读 current owner `AGENT-MEMORY` 的具体命题：Prompt、Context、RAG、Memory 共同构成 Agent 的 information state。下一章引入 action：Tool Calling 如何把模型输出转换为对外部环境的 typed proposal，并由平台决定是否执行。
<!-- existing:SF-2026-ARXIV-2603-04428:end -->

<!-- delta:SF-2026-ARXIV-2603-04428:start -->
论文将持久 Q4 KV 作为 prompt 下方的 agent memory，并管理跨 agent/session 的缓存 identity。
<!-- delta:SF-2026-ARXIV-2603-04428:end -->

<!-- books-review:SF-2026-ARXIV-2603-04428:start -->
Decision=`No Change — Existing Coverage`；owner=`AGENT-MEMORY`；target=`books/part-07-agent/77-memory.md#本章在知识树中的位置 (line 1191)`；adjacent=`books/part-07-agent/76-rag.md#本章要回答的问题 (line 10); books/part-07-agent/78-tool-calling.md#本章要回答的问题 (line 10)`。证据边界：只接受 arXiv:2603.04428v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。 该判断尚未由 fresh-context Books reviewer 接受；Integrate 项只进入日期 queue，不写共享 Books。
<!-- books-review:SF-2026-ARXIV-2603-04428:end -->

<!-- existing:SF-2026-ARXIV-2603-04443:start -->
author-side 已读 current owner `AGENT-MEMORY` 的具体命题：只用最终 QA reward 训练 memory policy 成本低，也适合短链路、固定 schema 和容易人工检查的任务；但它不能回答某段中间 memory content 是否真正帮助了最终答案。一个实验性分支是固定 retrieval/answer interface，对 memory token 或 span 做 masking/counterfactual scoring，把对 answer score 的变化映射为 local process reward，再与 global outcome reward 合并。它把“这次答对了”推进为“哪些被写入的内容可能贡献了这次答案”，从而给 admission、update、compress 与 discard 更稠密的学习信号。
<!-- existing:SF-2026-ARXIV-2603-04443:end -->

<!-- delta:SF-2026-ARXIV-2603-04443:start -->
AMV-L 用 lifecycle manager 管理 memory 的写入、分层、压缩和回收，以尾延迟 SLO 驱动状态迁移。
<!-- delta:SF-2026-ARXIV-2603-04443:end -->

<!-- books-review:SF-2026-ARXIV-2603-04443:start -->
Decision=`No Change — Existing Coverage`；owner=`AGENT-MEMORY`；target=`books/part-07-agent/77-memory.md#Memory Write 是高风险决策 (line 122)`；adjacent=`books/part-07-agent/76-rag.md#本章要回答的问题 (line 10); books/part-07-agent/78-tool-calling.md#本章要回答的问题 (line 10)`。证据边界：只接受 arXiv:2603.04443v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。 该判断尚未由 fresh-context Books reviewer 接受；Integrate 项只进入日期 queue，不写共享 Books。
<!-- books-review:SF-2026-ARXIV-2603-04443:end -->

<!-- existing:SF-2026-ARXIV-2603-04444:start -->
author-side 已读 current owner `INFER-SCHEDULING` 的具体命题：vPod 类抽象可以绑定 NPU generation、数量、interconnect、memory、parallel layout 与 compiler profile，再用经校准的 roofline/modeling 筛选满足 SLO 的 Pareto configurations。routing 选择现成 replica，placement 选择 contract，autoscaling 决定何时 materialize/retire；三者共享 workload estimate，却不能合并为一个瞬时 score。scale-up readiness、model loading 和 migration delay 必须进入 admission。
<!-- existing:SF-2026-ARXIV-2603-04444:end -->

<!-- delta:SF-2026-ARXIV-2603-04444:start -->
vLLM Semantic Router 从请求语义/模态信号选择后端与策略，把 routing decision 置于 serving admission。
<!-- delta:SF-2026-ARXIV-2603-04444:end -->

<!-- books-review:SF-2026-ARXIV-2603-04444:start -->
Decision=`No Change — Existing Coverage`；owner=`INFER-SCHEDULING`；target=`books/part-05-inference-system/56-inference-scheduling.md#Routing、Placement 与 Autoscaling (line 285)`；adjacent=`books/part-05-inference-system/55-pd-disaggregation.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/57-what-is-ai-platform.md#本章要回答的问题 (line 10)`。证据边界：只接受 arXiv:2603.04444v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。 该判断尚未由 fresh-context Books reviewer 接受；Integrate 项只进入日期 queue，不写共享 Books。
<!-- books-review:SF-2026-ARXIV-2603-04444:end -->

<!-- existing:SF-2026-ARXIV-2603-04448:start -->
author-side 已读 current owner `AGENT-PLATFORM` 的具体命题：本章的核心判断是：**Agent Platform 是 AI Platform 对有状态行动循环的扩展。它统一 Agent definition、run、context、memory、tools、workflow、evaluation 与 policy，但复用 Part VI 的 identity、resource、evidence、cost、tenancy、security 和 recovery substrate。**
<!-- existing:SF-2026-ARXIV-2603-04448:end -->

<!-- delta:SF-2026-ARXIV-2603-04448:start -->
SkillNet 从经验抽象 Skill，建立 ontology，过滤合并并评估连接，使 Skill 成为有版本和关系的资产。
<!-- delta:SF-2026-ARXIV-2603-04448:end -->

<!-- books-review:SF-2026-ARXIV-2603-04448:start -->
Decision=`No Change — Existing Coverage`；owner=`AGENT-PLATFORM`；target=`books/part-07-agent/84-agent-platform.md#本章要回答的问题 (line 14)`；adjacent=`books/part-07-agent/83-mcp.md#本章要回答的问题 (line 10)`。证据边界：只接受 arXiv:2603.04448v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。 该判断尚未由 fresh-context Books reviewer 接受；Integrate 项只进入日期 queue，不写共享 Books。
<!-- books-review:SF-2026-ARXIV-2603-04448:end -->

<!-- existing:SF-2026-ARXIV-2603-04459:start -->
author-side 已读 current owner `PLATFORM-EVALUATION-SYSTEM` 的具体命题：- `SF-2026-ARXIV-2606-21869` — primary `arXiv:2606.21869v1`；exact-v1 URL=`https://arxiv.org/html/2606.21869v1`；Method=`https://arxiv.org/html/2606.21869v1 — §3 Preliminaries — Energy Consumption and Measurement; Multilingual Dataset`；Evaluation=`https://arxiv.org/html/2606.21869v1 — §4 Results and Analysis — Common Setup; §4.1–§4.4; Appendix B Experimental Setups`；Non-proof=`https://arxiv.org/html/2606.21869v1 — §6 Conclusion; Environmental impact of this study; Translation quality and representation; Recommendatio
<!-- existing:SF-2026-ARXIV-2603-04459:end -->

<!-- delta:SF-2026-ARXIV-2603-04459:start -->
论文同时审计 benchmark influence 与 repository 可运行/维护属性，分离社会采用和 artifact quality。
<!-- delta:SF-2026-ARXIV-2603-04459:end -->

<!-- books-review:SF-2026-ARXIV-2603-04459:start -->
Decision=`No Change — Existing Coverage`；owner=`PLATFORM-EVALUATION-SYSTEM`；target=`books/part-06-ai-infrastructure/66-evaluation-system.md#从答案评分到可执行证据 (line 936)`；adjacent=`books/part-06-ai-infrastructure/65-kai-scheduler.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/67-monitoring.md#本章要回答的问题 (line 10)`。证据边界：只接受 arXiv:2603.04459v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。 该判断尚未由 fresh-context Books reviewer 接受；Integrate 项只进入日期 queue，不写共享 Books。
<!-- books-review:SF-2026-ARXIV-2603-04459:end -->

<!-- existing:SF-2026-ARXIV-2603-04460:start -->
author-side 已读 current owner `INFER-PREFILL` 的具体命题：10. Sparse Prefill 的 selection overhead 为什么必须进入 TTFT，而不能只比较 attention kernel？
<!-- existing:SF-2026-ARXIV-2603-04460:end -->

<!-- delta:SF-2026-ARXIV-2603-04460:start -->
VSPrefill 用 vertical-slash sparse pattern 与轻量索引选择 key block，专门优化 prefill 数据流。
<!-- delta:SF-2026-ARXIV-2603-04460:end -->

<!-- books-review:SF-2026-ARXIV-2603-04460:start -->
Decision=`No Change — Existing Coverage`；owner=`INFER-PREFILL`；target=`books/part-05-inference-system/43-prefill.md#自检问题 (line 365)`；adjacent=`books/part-05-inference-system/42-what-happens-during-inference.md#本章要回答的问题 (line 10); books/part-05-inference-system/44-decode.md#本章要回答的问题 (line 10)`。证据边界：只接受 arXiv:2603.04460v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。 该判断尚未由 fresh-context Books reviewer 接受；Integrate 项只进入日期 queue，不写共享 Books。
<!-- books-review:SF-2026-ARXIV-2603-04460:end -->

<!-- existing:SF-2026-ARXIV-2603-04469:start -->
author-side 已读 current owner `PLATFORM-SECURITY` 的具体命题：逐条扫描 message 或只在最终 action 上做 policy check，在通信拓扑固定、传播链短时简单有效；当一个污染信号经 message、shared memory、delegation 与 tool result 多次改写后，单 channel 告警既无法说明起点，也无法判断哪个 Agent 正在放大影响。运行时可以维护带 revision 的 cross-channel influence graph：各 channel adapter 只提交 observation，causal monitor 关联传播路径并提出 suspect source / edge，security policy 仍独立决定隔离、降权或阻断，不能把统计 attribution 当作 authorization。
<!-- existing:SF-2026-ARXIV-2603-04469:end -->

<!-- delta:SF-2026-ARXIV-2603-04469:start -->
Cross-Layer Semantic Flow Reconstruction 将跨层事件关联为 provenance graph，再依据语义流识别从不可信输入到敏感 action 的路径。
<!-- delta:SF-2026-ARXIV-2603-04469:end -->

<!-- books-review:SF-2026-ARXIV-2603-04469:start -->
Decision=`No Change — Existing Coverage`；owner=`PLATFORM-SECURITY`；target=`books/part-06-ai-infrastructure/72-security.md#从“文本是否恶意”到“谁获得了行为控制权” (line 336)`；adjacent=`books/part-06-ai-infrastructure/71-multi-tenant.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/73-production-best-practice.md#本章要回答的问题 (line 10)`。证据边界：只接受 arXiv:2603.04469v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。 该判断尚未由 fresh-context Books reviewer 接受；Integrate 项只进入日期 queue，不写共享 Books。
<!-- books-review:SF-2026-ARXIV-2603-04469:end -->

<!-- existing:SF-2026-ARXIV-2603-04797:start -->
author-side 已读 current owner `INFER-GPU-MEMORY` 的具体命题：权重因此从静态 artifact 扩展为受策略控制的 runtime state，也新增 calibration drift、prompt-conditioned policy、CPU-GPU traffic、mixed kernel 和失败恢复问题。quality policy、tenant 与 request identity 必须进入 trace；严格可复现、精度预算固定或 transfer cost 高时，静态 weights 仍更安全。当前证据限于三种 MoE、作者 workload 与无生产 arrival/tail-SLO 的实验。
<!-- existing:SF-2026-ARXIV-2603-04797:end -->

<!-- delta:SF-2026-ARXIV-2603-04797:start -->
论文联合 3D-DRAM accelerator 与 serving dataflow/placement，按模型状态访问模式设计硬件。
<!-- delta:SF-2026-ARXIV-2603-04797:end -->

<!-- books-review:SF-2026-ARXIV-2603-04797:start -->
Decision=`No Change — Existing Coverage`；owner=`INFER-GPU-MEMORY`；target=`books/part-05-inference-system/54-gpu-memory.md#三类缓解路径 (line 306)`；adjacent=`books/part-05-inference-system/53-kserve-llm.md#本章要回答的问题 (line 10); books/part-05-inference-system/55-pd-disaggregation.md#本章要回答的问题 (line 10)`。证据边界：只接受 arXiv:2603.04797v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。 该判断尚未由 fresh-context Books reviewer 接受；Integrate 项只进入日期 queue，不写共享 Books。
<!-- books-review:SF-2026-ARXIV-2603-04797:end -->

<!-- existing:SF-2026-ARXIV-2603-04902:start -->
author-side 已读 current owner `PLATFORM-SECURITY` 的具体命题：Artifact 签名和 final-output check 能证明加载对象或发现最终错误，却不能在不可信 pipeline stage 之间定位哪一段改写了状态。一个 challenge-response 分支是由 verifier 持有 versioned canary 与受信 reference activation，在 live fp16 执行时比较每个 shard 的 intermediate state，并按校准 noise envelope 输出 suspect evidence。
<!-- existing:SF-2026-ARXIV-2603-04902:end -->

<!-- delta:SF-2026-ARXIV-2603-04902:start -->
AgentSCOPE 用 Privacy Flow Graph 表示 actor、context 与 transmission，并据 contextual integrity 构造 benchmark。
<!-- delta:SF-2026-ARXIV-2603-04902:end -->

<!-- books-review:SF-2026-ARXIV-2603-04902:start -->
Decision=`No Change — Existing Coverage`；owner=`PLATFORM-SECURITY`；target=`books/part-06-ai-infrastructure/72-security.md#Supply-chain Integrity (line 538)`；adjacent=`books/part-06-ai-infrastructure/71-multi-tenant.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/73-production-best-practice.md#本章要回答的问题 (line 10)`。证据边界：只接受 arXiv:2603.04902v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。 该判断尚未由 fresh-context Books reviewer 接受；Integrate 项只进入日期 queue，不写共享 Books。
<!-- books-review:SF-2026-ARXIV-2603-04902:end -->

<!-- existing:SF-2026-ARXIV-2603-04910:start -->
author-side 已读 current owner `MULTIMODAL-EMBODIED-VLA` 的具体命题：快慢分层把状态与控制频率拆开：慢速 multimodal policy 生成 chunk 与高层 context，快速 causal action expert 读取 latency-aligned force memory，对尚未 commit 的动作做有界修正。初始化时保持原 policy 行为，在线 human correction 则必须带 observation、force、原 proposal 与最终 action provenance。低层 safety controller 继续拥有执行 authority，reactive expert 只拥有 proposal correction。
<!-- existing:SF-2026-ARXIV-2603-04910:end -->

<!-- delta:SF-2026-ARXIV-2603-04910:start -->
VPWEM 将 working 与 episodic memory 接入 visuomotor policy，使动作依赖近期状态和历史事件。
<!-- delta:SF-2026-ARXIV-2603-04910:end -->

<!-- books-review:SF-2026-ARXIV-2603-04910:start -->
Decision=`No Change — Existing Coverage`；owner=`MULTIMODAL-EMBODIED-VLA`；target=`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#Latency 与 control frequency (line 329)`；adjacent=`books/part-03-multimodal-world-models/25-multimodal-world-models.md#本章要回答的问题 (line 10); books/part-04-training-system/27-data.md#本章要回答的问题 (line 10)`。证据边界：只接受 arXiv:2603.04910v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。 该判断尚未由 fresh-context Books reviewer 接受；Integrate 项只进入日期 queue，不写共享 Books。
<!-- books-review:SF-2026-ARXIV-2603-04910:end -->

<!-- existing:SF-2026-ARXIV-2603-04981:start -->
author-side 已读 current owner `TRAIN-DATA` 的具体命题：- `SF-2026-ARXIV-2606-22142` — primary `arXiv:2606.22142v1`；exact-v1 URL=`https://arxiv.org/html/2606.22142v1`；Method=`https://arxiv.org/html/2606.22142v1 — §3 Method; §3.2 Agent-Native Governance Over Lifecycle Artifacts; §3.5 Data Health, Training Integration, and Version Governance`；Evaluation=`https://arxiv.org/html/2606.22142v1 — §4 Experiments; §4.1 Experimental Setup`；Non-proof=`https://arxiv.org/html/2606.22142v1 — §5 Limitations and Discussion`。
<!-- existing:SF-2026-ARXIV-2603-04981:end -->

<!-- delta:SF-2026-ARXIV-2603-04981:start -->
论文重新定义/联合优化 representativeness 与 diversity，并按训练反馈更新选择。
<!-- delta:SF-2026-ARXIV-2603-04981:end -->

<!-- books-review:SF-2026-ARXIV-2603-04981:start -->
Decision=`No Change — Existing Coverage`；owner=`TRAIN-DATA`；target=`books/part-04-training-system/27-data.md#Data lineage 是训练可复现性的前提 (line 562)`；adjacent=`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#本章要回答的问题 (line 10); books/part-04-training-system/28-pretraining.md#本章要回答的问题 (line 10)`。证据边界：只接受 arXiv:2603.04981v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。 该判断尚未由 fresh-context Books reviewer 接受；Integrate 项只进入日期 queue，不写共享 Books。
<!-- books-review:SF-2026-ARXIV-2603-04981:end -->

<!-- existing:SF-2026-ARXIV-2603-05031:start -->
author-side 已读 current owner `AGENT-TOOL-CALLING` 的具体命题：Schema 可以拒绝缺字段、错误类型或非法 enum；semantic validation 还要检查金额、目标资源、环境、时间窗口和当前状态。Authorization 必须使用真实 principal，不接受模型生成的 `tenant_id` 或 scope。
<!-- existing:SF-2026-ARXIV-2603-05031:end -->

<!-- delta:SF-2026-ARXIV-2603-05031:start -->
AegisUI 对 UI protocol 的可见语义、隐藏 action 和行为序列做一致性检测，把用户界面也纳入 tool authorization boundary。
<!-- delta:SF-2026-ARXIV-2603-05031:end -->

<!-- books-review:SF-2026-ARXIV-2603-05031:start -->
Decision=`No Change — Existing Coverage`；owner=`AGENT-TOOL-CALLING`；target=`books/part-07-agent/78-tool-calling.md#模型输出只是 Proposal (line 72)`；adjacent=`books/part-07-agent/77-memory.md#本章要回答的问题 (line 10); books/part-07-agent/79-planning.md#本章要回答的问题 (line 10)`。证据边界：只接受 arXiv:2603.05031v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。 该判断尚未由 fresh-context Books reviewer 接受；Integrate 项只进入日期 queue，不写共享 Books。
<!-- books-review:SF-2026-ARXIV-2603-05031:end -->

<!-- existing:SF-2026-ARXIV-2603-05185:start -->
author-side 已读 current owner `MULTIMODAL-EMBODIED-VLA` 的具体命题：高层 semantic planning 可以在云端使用大模型，低层 control 和 emergency response 必须靠近设备。hybrid system 的关键不是“模型放哪”，而是：
<!-- existing:SF-2026-ARXIV-2603-05185:end -->

<!-- delta:SF-2026-ARXIV-2603-05185:start -->
tri-system VLA 加入独立 critic，在 perception/reasoning-action 与执行反馈间审查并触发修正。
<!-- delta:SF-2026-ARXIV-2603-05185:end -->

<!-- books-review:SF-2026-ARXIV-2603-05185:start -->
Decision=`No Change — Existing Coverage`；owner=`MULTIMODAL-EMBODIED-VLA`；target=`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#Edge 与云的分层 (line 499)`；adjacent=`books/part-03-multimodal-world-models/25-multimodal-world-models.md#本章要回答的问题 (line 10); books/part-04-training-system/27-data.md#本章要回答的问题 (line 10)`。证据边界：只接受 arXiv:2603.05185v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。 该判断尚未由 fresh-context Books reviewer 接受；Integrate 项只进入日期 queue，不写共享 Books。
<!-- books-review:SF-2026-ARXIV-2603-05185:end -->

<!-- existing:SF-2026-ARXIV-2603-05438:start -->
author-side 已读 current owner `MULTIMODAL-WORLD-MODELS` 的具体命题：从视频生成进入 World Model 的关键约束变化，是输出不再只需“看起来合理”，而要在给定 action 后保持可修正的 environment transition。系统因此从下一帧生成，演进到 latent state、action-conditioned rollout、持久 landmark/memory 与 observation reconciliation；state owner 必须区分预测状态、已观测事实和计划假设。
<!-- existing:SF-2026-ARXIV-2603-05438:end -->

<!-- delta:SF-2026-ARXIV-2603-05438:start -->
论文学习紧凑离散 tokenizer，用少量 token 表达 planning-relevant latent state。
<!-- delta:SF-2026-ARXIV-2603-05438:end -->

<!-- books-review:SF-2026-ARXIV-2603-05438:start -->
Decision=`No Change — Existing Coverage`；owner=`MULTIMODAL-WORLD-MODELS`；target=`books/part-03-multimodal-world-models/25-multimodal-world-models.md#从机制演进到系统设计 (line 640)`；adjacent=`books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#本章要回答的问题 (line 10); books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#本章要回答的问题 (line 10)`。证据边界：只接受 arXiv:2603.05438v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。 该判断尚未由 fresh-context Books reviewer 接受；Integrate 项只进入日期 queue，不写共享 Books。
<!-- books-review:SF-2026-ARXIV-2603-05438:end -->

<!-- existing:SF-2026-ARXIV-2603-05451:start -->
author-side 已读 current owner `INFER-TENSORRT-LLM` 的具体命题：Tensor Memory Accelerator（TMA）在 Hopper（compute capability 9.0）引入，用于把 1D 到多维 tensor tiles 在 global memory 与 shared memory 之间做 bulk asynchronous transfer。Tensor map 描述 base address、shape、stride、element type、interleave/swizzle 等信息；少量 threads 可以发起大块搬运，不必让每个元素先经过普通 registers 和逐元素地址计算。
<!-- existing:SF-2026-ARXIV-2603-05451:end -->

<!-- delta:SF-2026-ARXIV-2603-05451:start -->
FlashAttention-4 联合重排算法 tiles 与 kernel pipeline，使 load、compute 和 reduce 匹配非对称硬件。
<!-- delta:SF-2026-ARXIV-2603-05451:end -->

<!-- books-review:SF-2026-ARXIV-2603-05451:start -->
Decision=`No Change — Existing Coverage`；owner=`INFER-TENSORRT-LLM`；target=`books/part-05-inference-system/49-tensorrt-llm.md#TMA 解决搬运，不负责矩阵计算 (line 341)`；adjacent=`books/part-05-inference-system/48-speculative-decoding.md#本章要回答的问题 (line 10); books/part-05-inference-system/50-vllm.md#本章要回答的问题 (line 10)`。证据边界：只接受 arXiv:2603.05451v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。 该判断尚未由 fresh-context Books reviewer 接受；Integrate 项只进入日期 queue，不写共享 Books。
<!-- books-review:SF-2026-ARXIV-2603-05451:end -->

<!-- existing:SF-2026-ARXIV-2603-05454:start -->
author-side 已读 current owner `MULTIMODAL-GENERATIVE-PARADIGMS` 的具体命题：为什么文本生成长期以 Autoregressive 为主，而图像和视频大量采用 Diffusion？Masked Diffusion 为什么能并行生成多个 token，却带来 mutable output、cache invalidation 和 streaming 难题？Block Diffusion、draft tree 和 correction loop 是同一条路线吗？
<!-- existing:SF-2026-ARXIV-2603-05454:end -->

<!-- delta:SF-2026-ARXIV-2603-05454:start -->
论文选择 longest stable prefix 作为连续 commit 单元，使 DLM 在多轮修正中保留一致前缀。
<!-- delta:SF-2026-ARXIV-2603-05454:end -->

<!-- books-review:SF-2026-ARXIV-2603-05454:start -->
Decision=`No Change — Existing Coverage`；owner=`MULTIMODAL-GENERATIVE-PARADIGMS`；target=`books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#本章要回答的问题 (line 12)`；adjacent=`books/part-03-multimodal-world-models/23-multimodal-representation.md#本章要回答的问题 (line 10); books/part-03-multimodal-world-models/25-multimodal-world-models.md#本章要回答的问题 (line 10)`。证据边界：只接受 arXiv:2603.05454v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。 该判断尚未由 fresh-context Books reviewer 接受；Integrate 项只进入日期 queue，不写共享 Books。
<!-- books-review:SF-2026-ARXIV-2603-05454:end -->

<!-- existing:SF-2026-ARXIV-2603-04411:start -->
author-side 已读 current owner `INFER-KV-CACHE` 的具体命题：RoPE/position policy、compression revision 与 generation boundary，不能被一个模糊的“video cache”标识覆盖。
<!-- existing:SF-2026-ARXIV-2603-04411:end -->

<!-- delta:SF-2026-ARXIV-2603-04411:start -->
论文按 token 动态选择压缩强度，使 KV precision/retention 成为 token-wise decision。
<!-- delta:SF-2026-ARXIV-2603-04411:end -->

<!-- books-review:SF-2026-ARXIV-2603-04411:start -->
Decision=`No Change — Existing Coverage`；owner=`INFER-KV-CACHE`；target=`books/part-05-inference-system/45-why-kv-cache-speeds-up.md#一致性不变量 (line 773)`；adjacent=`books/part-05-inference-system/44-decode.md#本章要回答的问题 (line 10); books/part-05-inference-system/46-continuous-batching.md#本章要回答的问题 (line 10)`。证据边界：只接受 arXiv:2603.04411v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。 该判断尚未由 fresh-context Books reviewer 接受；Integrate 项只进入日期 queue，不写共享 Books。
<!-- books-review:SF-2026-ARXIV-2603-04411:end -->

<!-- existing:SF-2026-ARXIV-2603-04417:start -->
author-side 已读 current owner `PLATFORM-EVALUATION-SYSTEM` 的具体命题：- `SF-2026-ARXIV-2606-21869` — primary `arXiv:2606.21869v1`；exact-v1 URL=`https://arxiv.org/html/2606.21869v1`；Method=`https://arxiv.org/html/2606.21869v1 — §3 Preliminaries — Energy Consumption and Measurement; Multilingual Dataset`；Evaluation=`https://arxiv.org/html/2606.21869v1 — §4 Results and Analysis — Common Setup; §4.1–§4.4; Appendix B Experimental Setups`；Non-proof=`https://arxiv.org/html/2606.21869v1 — §6 Conclusion; Environmental impact of this study; Translation quality and representation; Recommendatio
<!-- existing:SF-2026-ARXIV-2603-04417:end -->

<!-- delta:SF-2026-ARXIV-2603-04417:start -->
论文跨多 judge/model 重复测量一致性，将 variance 与 disagreement 纳入 evaluation contract。
<!-- delta:SF-2026-ARXIV-2603-04417:end -->

<!-- books-review:SF-2026-ARXIV-2603-04417:start -->
Decision=`No Change — Existing Coverage`；owner=`PLATFORM-EVALUATION-SYSTEM`；target=`books/part-06-ai-infrastructure/66-evaluation-system.md#从答案评分到可执行证据 (line 936)`；adjacent=`books/part-06-ai-infrastructure/65-kai-scheduler.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/67-monitoring.md#本章要回答的问题 (line 10)`。证据边界：只接受 arXiv:2603.04417v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。 该判断尚未由 fresh-context Books reviewer 接受；Integrate 项只进入日期 queue，不写共享 Books。
<!-- books-review:SF-2026-ARXIV-2603-04417:end -->

<!-- existing:SF-2026-ARXIV-2603-04427:start -->
author-side 已读 current owner `INFER-KV-CACHE` 的具体命题：PD 分离中固定 codec 在某些 model、layer、length 或网络状态下有效，在另一些场景会让 encode/decode 超过节省的传输。Service-aware planner 可把 quantization、sparsity、chunking 与 recomposition 视为策略空间，用离线 profiling 在 quality、latency、bandwidth 和 GPU budget 下选 plan，并把 chosen policy 绑定 cache/transfer identity。它用更好适配换 profile 成本、search drift 和更复杂 fallback；未命中已验证 workload 时应回退原始 KV 或保守 codec。作者 benchmark 不构成跨硬件通用压缩收益。
<!-- existing:SF-2026-ARXIV-2603-04427:end -->

<!-- delta:SF-2026-ARXIV-2603-04427:start -->
Thin Keys, Full Values 只把 key 投影到低维用于选择，保留完整 value 承载内容。
<!-- delta:SF-2026-ARXIV-2603-04427:end -->

<!-- books-review:SF-2026-ARXIV-2603-04427:start -->
Decision=`No Change — Existing Coverage`；owner=`INFER-KV-CACHE`；target=`books/part-05-inference-system/45-why-kv-cache-speeds-up.md#一致性不变量 (line 885)`；adjacent=`books/part-05-inference-system/44-decode.md#本章要回答的问题 (line 10); books/part-05-inference-system/46-continuous-batching.md#本章要回答的问题 (line 10)`。证据边界：只接受 arXiv:2603.04427v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。 该判断尚未由 fresh-context Books reviewer 接受；Integrate 项只进入日期 queue，不写共享 Books。
<!-- books-review:SF-2026-ARXIV-2603-04427:end -->

<!-- existing:SF-2026-ARXIV-2603-04621:start -->
author-side 已读 current owner `INFER-TENSORRT-LLM` 的具体命题：这里的 `stack` 很重要。当前官方文档覆盖的不只是离线构建计算图，也包括 runtime、in-flight batching、paged KV caching、quantization 以及多 GPU/多节点执行。把 TensorRT-LLM 固定理解成“先编译一个静态 engine”会低估它已经扩展出的 Serving 能力；但本章仍以 GPU execution optimization 为主线，避免写成版本功能目录。
<!-- existing:SF-2026-ARXIV-2603-04621:end -->

<!-- delta:SF-2026-ARXIV-2603-04621:start -->
DuaLip-GPU 设计双 pipeline 协同计算和数据搬运，以端到端 plan 管理 overlap。
<!-- delta:SF-2026-ARXIV-2603-04621:end -->

<!-- books-review:SF-2026-ARXIV-2603-04621:start -->
Decision=`No Change — Existing Coverage`；owner=`INFER-TENSORRT-LLM`；target=`books/part-05-inference-system/49-tensorrt-llm.md#本章要回答的问题 (line 16)`；adjacent=`books/part-05-inference-system/48-speculative-decoding.md#本章要回答的问题 (line 10); books/part-05-inference-system/50-vllm.md#本章要回答的问题 (line 10)`。证据边界：只接受 arXiv:2603.04621v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。 该判断尚未由 fresh-context Books reviewer 接受；Integrate 项只进入日期 queue，不写共享 Books。
<!-- books-review:SF-2026-ARXIV-2603-04621:end -->

<!-- existing:SF-2026-ARXIV-2603-04656:start -->
author-side 已读 current owner `PLATFORM-EVALUATION-SYSTEM` 的具体命题：明确 issue、固定 tests 的 benchmark 对局部修复仍然理想：输入、预期行为与失败位置清楚，回归也容易复现。但从零构建 repository 时，agent 常先面对不完整 product intent。若只看最终 tests，需求从未被告知与 agent 已获得需求却没有正确实现会被压成同一种失败，评测无法判断问题出在 information access 还是 execution conversion。
<!-- existing:SF-2026-ARXIV-2603-04656:end -->

<!-- delta:SF-2026-ARXIV-2603-04656:start -->
iAgentBench 将多源检索、证据关系、冲突消解和最终回答绑定为同一评估任务。
<!-- delta:SF-2026-ARXIV-2603-04656:end -->

<!-- books-review:SF-2026-ARXIV-2603-04656:start -->
Decision=`No Change — Existing Coverage`；owner=`PLATFORM-EVALUATION-SYSTEM`；target=`books/part-06-ai-infrastructure/66-evaluation-system.md#Scorer 不是绝对真相 (line 1719)`；adjacent=`books/part-06-ai-infrastructure/65-kai-scheduler.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/67-monitoring.md#本章要回答的问题 (line 10)`。证据边界：只接受 arXiv:2603.04656v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。 该判断尚未由 fresh-context Books reviewer 接受；Integrate 项只进入日期 queue，不写共享 Books。
<!-- books-review:SF-2026-ARXIV-2603-04656:end -->

<!-- existing:SF-2026-ARXIV-2603-04851:start -->
author-side 已读 current owner `TRAIN-RLHF` 的具体命题：Reward Model 通常在完整 response 后给出 scalar，而 policy 逐 token 生成；sequence outcome 本身不能指出哪个 token 导致好坏，长序列、稀疏 reward 与延迟反馈会放大 credit-assignment 方差。
<!-- existing:SF-2026-ARXIV-2603-04851:end -->

<!-- delta:SF-2026-ARXIV-2603-04851:start -->
论文以序列 harm 的 martingale/协方差分解刻画 gradient，使 alignment locality 成为可分析的 objective property。
<!-- delta:SF-2026-ARXIV-2603-04851:end -->

<!-- books-review:SF-2026-ARXIV-2603-04851:start -->
Decision=`Integrate`；owner=`TRAIN-RLHF`；target=`books/part-04-training-system/31-rlhf.md#Harm Horizon：Sequence Reward 的 Gradient 可能天然局部 (line 244)`；adjacent=`books/part-04-training-system/30-lora.md#本章要回答的问题 (line 10); books/part-04-training-system/32-ppo.md#本章要回答的问题 (line 10)`。证据边界：只接受 arXiv:2603.04851v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。已写入共享 Books，marker=`source-family:SF-2026-ARXIV-2603-04851`；仍待非作者 post-write semantic audit，因此 Books Gate 保持 Open。
<!-- books-review:SF-2026-ARXIV-2603-04851:end -->

<!-- existing:SF-2026-ARXIV-2603-05087:start -->
author-side 已读 current owner `PLATFORM-GPU-SCHEDULER` 的具体命题：time-slicing、MPS 与 MIG 都假设 runtime 与隔离边界相对明确；当 CUDA 与 Vulkan 等不同 API 共享同一设备时，空间复用还会引入跨 API 的 allocation、同步与地址可见性问题。平台不能只把两类进程放在同一 GPU 上就宣称共享成功：scheduler 要拥有可审计的 resource partition，driver/runtime 要拥有 synchronization 与 memory-safety contract，workload identity 还必须绑定 API、context 和 device state。
<!-- existing:SF-2026-ARXIV-2603-05087:end -->

<!-- delta:SF-2026-ARXIV-2603-05087:start -->
PromptTuner 将 job profile、deadline 与 elastic resource control 连接，让 admission/scaling 依据可测训练 work 而变化。
<!-- delta:SF-2026-ARXIV-2603-05087:end -->

<!-- books-review:SF-2026-ARXIV-2603-05087:start -->
Decision=`No Change — Existing Coverage`；owner=`PLATFORM-GPU-SCHEDULER`；target=`books/part-06-ai-infrastructure/63-gpu-scheduler.md#与推理 Scheduler 的边界 (line 243)`；adjacent=`books/part-06-ai-infrastructure/62-gateway.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/64-volcano.md#本章要回答的问题 (line 10)`。证据边界：只接受 arXiv:2603.05087v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。 该判断尚未由 fresh-context Books reviewer 接受；Integrate 项只进入日期 queue，不写共享 Books。
<!-- books-review:SF-2026-ARXIV-2603-05087:end -->

<!-- existing:SF-2026-ARXIV-2603-05147:start -->
author-side 已读 current owner `MULTIMODAL-EMBODIED-VLA` 的具体命题：把 vision/language hidden state 直接送入 action head，接口最短，在 viewpoint、task 与 action schema 稳定时也最简单；但 joint training 同时允许 action loss 直接改写通用 semantic representation。数据较窄或 real-scene visual shift 较大时，instruction generation、object grounding 与 local action direction 可能被同一 latent 中的冲突梯度一起扰动。
<!-- existing:SF-2026-ARXIV-2603-05147:end -->

<!-- delta:SF-2026-ARXIV-2603-05147:start -->
论文按状态复杂度在 act、think、abstain 三条路径间选择，将推理预算和安全拒绝纳入 controller。
<!-- delta:SF-2026-ARXIV-2603-05147:end -->

<!-- books-review:SF-2026-ARXIV-2603-05147:start -->
Decision=`No Change — Existing Coverage`；owner=`MULTIMODAL-EMBODIED-VLA`；target=`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#从模块化机器人到 VLA (line 90)`；adjacent=`books/part-03-multimodal-world-models/25-multimodal-world-models.md#本章要回答的问题 (line 10); books/part-04-training-system/27-data.md#本章要回答的问题 (line 10)`。证据边界：只接受 arXiv:2603.05147v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。 该判断尚未由 fresh-context Books reviewer 接受；Integrate 项只进入日期 queue，不写共享 Books。
<!-- books-review:SF-2026-ARXIV-2603-05147:end -->

<!-- existing:SF-2026-ARXIV-2603-05210:start -->
author-side 已读 current owner `INFER-SPECULATIVE-DECODING` 的具体命题：本章的核心判断是：**Speculative Decoding 用额外且便宜的 proposal work，换取一次 target-model verification 推进多个 output tokens；经典算法通过 acceptance 与 residual sampling 保持 target distribution，而不是用 draft model 改写模型行为。**
<!-- existing:SF-2026-ARXIV-2603-05210:end -->

<!-- delta:SF-2026-ARXIV-2603-05210:start -->
论文联合选择 vocabulary coverage 与 draft cost，在模型/工作负载上寻找平衡点。
<!-- delta:SF-2026-ARXIV-2603-05210:end -->

<!-- books-review:SF-2026-ARXIV-2603-05210:start -->
Decision=`No Change — Existing Coverage`；owner=`INFER-SPECULATIVE-DECODING`；target=`books/part-05-inference-system/48-speculative-decoding.md#本章要回答的问题 (line 16)`；adjacent=`books/part-05-inference-system/47-pagedattention.md#本章要回答的问题 (line 10); books/part-05-inference-system/49-tensorrt-llm.md#本章要回答的问题 (line 10)`。证据边界：只接受 arXiv:2603.05210v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。 该判断尚未由 fresh-context Books reviewer 接受；Integrate 项只进入日期 queue，不写共享 Books。
<!-- books-review:SF-2026-ARXIV-2603-05210:end -->

<!-- existing:SF-2026-ARXIV-2603-05353:start -->
author-side 已读 current owner `INFER-KV-CACHE` 的具体命题：逻辑 prompt 保持不变时，physical-read optimization 可以只读取计划区域，但 access plan 必须绑定模型、tokenization、KV layout 与 knowledge revision；依赖不确定或验证失败时应回退 full context。
<!-- existing:SF-2026-ARXIV-2603-05353:end -->

<!-- delta:SF-2026-ARXIV-2603-05353:start -->
InfoFlow KV 根据跨 token 信息流选择需要重算的局部状态，使缓存复用和因果修复共享一个选择 contract。
<!-- delta:SF-2026-ARXIV-2603-05353:end -->

<!-- books-review:SF-2026-ARXIV-2603-05353:start -->
Decision=`Integrate`；owner=`INFER-KV-CACHE`；target=`books/part-05-inference-system/45-why-kv-cache-speeds-up.md#Structured knowledge 只有进入 physical access plan 才改变 KV 成本 (line 152)`；adjacent=`books/part-05-inference-system/44-decode.md#本章要回答的问题 (line 10); books/part-05-inference-system/46-continuous-batching.md#本章要回答的问题 (line 10)`。证据边界：只接受 arXiv:2603.05353v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。 该判断尚未由 fresh-context Books reviewer 接受；Integrate 项只进入日期 queue，不写共享 Books。
<!-- books-review:SF-2026-ARXIV-2603-05353:end -->

<!-- existing:SF-2026-ARXIV-2603-05399:start -->
author-side 已读 current owner `PLATFORM-EVALUATION-SYSTEM` 的具体命题：把每语言生成能耗与 accuracy、tokenization expansion 分开记录；evaluation/model card 需声明 per-language energy，而不能用英语平均值代表多语言部署。 Hardness Adjusted Transfer 以 target performance 相对 source-language ability 校正，避免把 source accuracy 提升误报成 cross-lingual transfer 进步。 selective prediction 除 calibration/ranking 还要报告 score granularity：可用阈值数量决定 operator 能选择多少风险工作点；多查询扩大分辨率但增加成本且可能伤害强模型排序。
<!-- existing:SF-2026-ARXIV-2603-05399:end -->

<!-- delta:SF-2026-ARXIV-2603-05399:start -->
Judge Reliability Harness 对 judge 进行成组 stress test 并保存 evaluator/version/seed 证据。
<!-- delta:SF-2026-ARXIV-2603-05399:end -->

<!-- books-review:SF-2026-ARXIV-2603-05399:start -->
Decision=`No Change — Existing Coverage`；owner=`PLATFORM-EVALUATION-SYSTEM`；target=`books/part-06-ai-infrastructure/66-evaluation-system.md#从答案评分到可执行证据 (line 930)`；adjacent=`books/part-06-ai-infrastructure/65-kai-scheduler.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/67-monitoring.md#本章要回答的问题 (line 10)`。证据边界：只接受 arXiv:2603.05399v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。 该判断尚未由 fresh-context Books reviewer 接受；Integrate 项只进入日期 queue，不写共享 Books。
<!-- books-review:SF-2026-ARXIV-2603-05399:end -->

<!-- existing:SF-2026-ARXIV-2603-04814:start -->
author-side 已读 current owner `AGENT-MEMORY` 的具体命题：Late construction 把不可逆信息损失延后，却增加每次查询的计算、judge/calibration 漂移和并发更新一致性；它也没有消除 deletion propagation、ACL 或 freshness 问题。查询重复且 schema 稳定时，预计算 summary 仍可能更便宜；高风险回答还应让最终 claim 回指 raw evidence。现有 LongMemEval/LoCoMo 结果只支持作者 workload 下的 accuracy/context trade-off，不证明更低的全生命周期成本。
<!-- existing:SF-2026-ARXIV-2603-04814:end -->

<!-- delta:SF-2026-ARXIV-2603-04814:start -->
工作在同一任务上联合比较 long-context 与 fact memory 的成本、检索和质量，形成 architecture selection contract。
<!-- delta:SF-2026-ARXIV-2603-04814:end -->

<!-- books-review:SF-2026-ARXIV-2603-04814:start -->
Decision=`No Change — Existing Coverage`；owner=`AGENT-MEMORY`；target=`books/part-07-agent/77-memory.md#Memory Read 是受约束检索 (line 265)`；adjacent=`books/part-07-agent/76-rag.md#本章要回答的问题 (line 10); books/part-07-agent/78-tool-calling.md#本章要回答的问题 (line 10)`。证据边界：只接受 arXiv:2603.04814v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。 该判断尚未由 fresh-context Books reviewer 接受；Integrate 项只进入日期 queue，不写共享 Books。
<!-- books-review:SF-2026-ARXIV-2603-04814:end -->

<!-- existing:SF-2026-ARXIV-2603-04896:start -->
author-side 已读 current owner `PLATFORM-SECURITY` 的具体命题：- `SF-2026-ARXIV-2606-22019` — primary `arXiv:2606.22019v1`；exact-v1 URL=`https://arxiv.org/html/2606.22019v1`；Method=`https://arxiv.org/html/2606.22019v1 — §2 Audit model: carriers, screens, and ablations; §6 The audit lifecycle: which handle is sound in which channel?`；Evaluation=`https://arxiv.org/html/2606.22019v1 — §3 A controlled body channel is screenable: coverage predicts transfer; §4 Vocabulary-carried token traits evade initialization-alignment screens; §5 The carrier is signal-dependent, and moving it m
<!-- existing:SF-2026-ARXIV-2603-04896:end -->

<!-- delta:SF-2026-ARXIV-2603-04896:start -->
Authorize-on-Demand 把 legality context 与运行时授权决策连接，使同一 VLM 的可用能力受可撤销 policy 控制。
<!-- delta:SF-2026-ARXIV-2603-04896:end -->

<!-- books-review:SF-2026-ARXIV-2603-04896:start -->
Decision=`No Change — Existing Coverage`；owner=`PLATFORM-SECURITY`；target=`books/part-06-ai-infrastructure/72-security.md#风险管理而不是一次性认证 (line 1091)`；adjacent=`books/part-06-ai-infrastructure/71-multi-tenant.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/73-production-best-practice.md#本章要回答的问题 (line 10)`。证据边界：只接受 arXiv:2603.04896v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。 该判断尚未由 fresh-context Books reviewer 接受；Integrate 项只进入日期 queue，不写共享 Books。
<!-- books-review:SF-2026-ARXIV-2603-04896:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260307-COVERAGE | fresh-context:march-lane-b-reviewer | coverage | coverage:SRC-ARXIV:20260307 | — | accepted: strict-window raw inventory、逐项 screening、withdrawn closure 与 weekly_dependency=0 已复核 | passed |
| SA-20260307-EVIDENCE | fresh-context:march-lane-b-reviewer | evidence | validator:review-completion-v1 | — | accepted: retained family 均完成 exact-v1 review，blocked/unverified/disputed=0 | passed |
| SA-20260307-SELECTION | fresh-context:march-lane-b-reviewer | deep_analysis_selection | validator:deep-analysis-selection-v1 | — | accepted: fresh-context false-positive / false-negative 与 Deep Analysis selection 已复核 | passed |
| SA-20260307-BOOKS | fresh-context:march-lane-b-reviewer | books | validator:books-comparison-v1 | — | accepted: Integrate 项已写入 canonical owner，且非写作者 post-write audit 通过 | passed |

## 8. Ignored Noise

562 个 pre-denominator closure 保存在 `papers/2026/03/_sources/daily-20260307/screening-ledger-final.json`；每个 family 保存 identity、title、abstract 与具体排除理由。withdrawn=0。

## 9. Recommended Action

本日 2 项长期机制已完成 exact-v1 证据审阅、canonical owner 写回与非写作者 post-write Semantic Audit；后续仅在 primary revision 或新反证出现时重开。

## 10. Repository Changes

- 新增或幂等更新本日 Daily 与可复算 source packet。
- 完成 2 项 Books Integration：
- 更新并复核 `books/part-04-training-system/31-rlhf.md`。
- 更新并复核 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md`。
- 未修改 Weekly；未 stage、commit 或 push。

## 11. Open Questions

- 普通 Gate finding=0；blocked / unverified / disputed=0。
- 论文自身未证明边界保留在各 Source Review 的 Claim Boundary 中；它们不是本次流程 pending。

## 12. Sources

- [arXiv:2603.04402v1](https://arxiv.org/abs/2603.04402v1) — official announcement instant `2026-03-06T09:00:00+08:00`；按半开窗口 owner report=`2026-03-07`；访问日期 2026-09-02。
- [arXiv:2603.04424v1](https://arxiv.org/abs/2603.04424v1) — official announcement instant `2026-03-06T09:00:00+08:00`；按半开窗口 owner report=`2026-03-07`；访问日期 2026-09-02。
- [arXiv:2603.04428v1](https://arxiv.org/abs/2603.04428v1) — official announcement instant `2026-03-06T09:00:00+08:00`；按半开窗口 owner report=`2026-03-07`；访问日期 2026-09-02。
- [arXiv:2603.04443v1](https://arxiv.org/abs/2603.04443v1) — official announcement instant `2026-03-06T09:00:00+08:00`；按半开窗口 owner report=`2026-03-07`；访问日期 2026-09-02。
- [arXiv:2603.04444v1](https://arxiv.org/abs/2603.04444v1) — official announcement instant `2026-03-06T09:00:00+08:00`；按半开窗口 owner report=`2026-03-07`；访问日期 2026-09-02。
- [arXiv:2603.04448v1](https://arxiv.org/abs/2603.04448v1) — official announcement instant `2026-03-06T09:00:00+08:00`；按半开窗口 owner report=`2026-03-07`；访问日期 2026-09-02。
- [arXiv:2603.04459v1](https://arxiv.org/abs/2603.04459v1) — official announcement instant `2026-03-06T09:00:00+08:00`；按半开窗口 owner report=`2026-03-07`；访问日期 2026-09-02。
- [arXiv:2603.04460v1](https://arxiv.org/abs/2603.04460v1) — official announcement instant `2026-03-06T09:00:00+08:00`；按半开窗口 owner report=`2026-03-07`；访问日期 2026-09-02。
- [arXiv:2603.04469v1](https://arxiv.org/abs/2603.04469v1) — official announcement instant `2026-03-06T09:00:00+08:00`；按半开窗口 owner report=`2026-03-07`；访问日期 2026-09-02。
- [arXiv:2603.04797v1](https://arxiv.org/abs/2603.04797v1) — official announcement instant `2026-03-06T09:00:00+08:00`；按半开窗口 owner report=`2026-03-07`；访问日期 2026-09-02。
- [arXiv:2603.04902v1](https://arxiv.org/abs/2603.04902v1) — official announcement instant `2026-03-06T09:00:00+08:00`；按半开窗口 owner report=`2026-03-07`；访问日期 2026-09-02。
- [arXiv:2603.04910v1](https://arxiv.org/abs/2603.04910v1) — official announcement instant `2026-03-06T09:00:00+08:00`；按半开窗口 owner report=`2026-03-07`；访问日期 2026-09-02。
- [arXiv:2603.04981v1](https://arxiv.org/abs/2603.04981v1) — official announcement instant `2026-03-06T09:00:00+08:00`；按半开窗口 owner report=`2026-03-07`；访问日期 2026-09-02。
- [arXiv:2603.05031v1](https://arxiv.org/abs/2603.05031v1) — official announcement instant `2026-03-06T09:00:00+08:00`；按半开窗口 owner report=`2026-03-07`；访问日期 2026-09-02。
- [arXiv:2603.05185v1](https://arxiv.org/abs/2603.05185v1) — official announcement instant `2026-03-06T09:00:00+08:00`；按半开窗口 owner report=`2026-03-07`；访问日期 2026-09-02。
- [arXiv:2603.05438v1](https://arxiv.org/abs/2603.05438v1) — official announcement instant `2026-03-06T09:00:00+08:00`；按半开窗口 owner report=`2026-03-07`；访问日期 2026-09-02。
- [arXiv:2603.05451v1](https://arxiv.org/abs/2603.05451v1) — official announcement instant `2026-03-06T09:00:00+08:00`；按半开窗口 owner report=`2026-03-07`；访问日期 2026-09-02。
- [arXiv:2603.05454v1](https://arxiv.org/abs/2603.05454v1) — official announcement instant `2026-03-06T09:00:00+08:00`；按半开窗口 owner report=`2026-03-07`；访问日期 2026-09-02。
- [arXiv:2603.04411v1](https://arxiv.org/abs/2603.04411v1) — official announcement instant `2026-03-06T09:00:00+08:00`；按半开窗口 owner report=`2026-03-07`；访问日期 2026-09-02。
- [arXiv:2603.04417v1](https://arxiv.org/abs/2603.04417v1) — official announcement instant `2026-03-06T09:00:00+08:00`；按半开窗口 owner report=`2026-03-07`；访问日期 2026-09-02。
- [arXiv:2603.04427v1](https://arxiv.org/abs/2603.04427v1) — official announcement instant `2026-03-06T09:00:00+08:00`；按半开窗口 owner report=`2026-03-07`；访问日期 2026-09-02。
- [arXiv:2603.04621v1](https://arxiv.org/abs/2603.04621v1) — official announcement instant `2026-03-06T09:00:00+08:00`；按半开窗口 owner report=`2026-03-07`；访问日期 2026-09-02。
- [arXiv:2603.04656v1](https://arxiv.org/abs/2603.04656v1) — official announcement instant `2026-03-06T09:00:00+08:00`；按半开窗口 owner report=`2026-03-07`；访问日期 2026-09-02。
- [arXiv:2603.04851v1](https://arxiv.org/abs/2603.04851v1) — official announcement instant `2026-03-06T09:00:00+08:00`；按半开窗口 owner report=`2026-03-07`；访问日期 2026-09-02。
- [arXiv:2603.05087v1](https://arxiv.org/abs/2603.05087v1) — official announcement instant `2026-03-06T09:00:00+08:00`；按半开窗口 owner report=`2026-03-07`；访问日期 2026-09-02。
- [arXiv:2603.05147v1](https://arxiv.org/abs/2603.05147v1) — official announcement instant `2026-03-06T09:00:00+08:00`；按半开窗口 owner report=`2026-03-07`；访问日期 2026-09-02。
- [arXiv:2603.05210v1](https://arxiv.org/abs/2603.05210v1) — official announcement instant `2026-03-06T09:00:00+08:00`；按半开窗口 owner report=`2026-03-07`；访问日期 2026-09-02。
- [arXiv:2603.05353v1](https://arxiv.org/abs/2603.05353v1) — official announcement instant `2026-03-06T09:00:00+08:00`；按半开窗口 owner report=`2026-03-07`；访问日期 2026-09-02。
- [arXiv:2603.05399v1](https://arxiv.org/abs/2603.05399v1) — official announcement instant `2026-03-06T09:00:00+08:00`；按半开窗口 owner report=`2026-03-07`；访问日期 2026-09-02。
- [arXiv:2603.04814v1](https://arxiv.org/abs/2603.04814v1) — official announcement instant `2026-03-06T09:00:00+08:00`；按半开窗口 owner report=`2026-03-07`；访问日期 2026-09-02。
- [arXiv:2603.04896v1](https://arxiv.org/abs/2603.04896v1) — official announcement instant `2026-03-06T09:00:00+08:00`；按半开窗口 owner report=`2026-03-07`；访问日期 2026-09-02。

## 13. Final Status

- Completion Status: `Complete`
- Coverage: `Closed`
- Evidence: `Passed`
- Books: `Passed`
- unresolved findings: 0
